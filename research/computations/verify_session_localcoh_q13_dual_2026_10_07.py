#!/usr/bin/env python3
"""Check all thirteen Q13 endpoint directions for every lower coefficient.

Default verification uses only the Python standard library and exact
rationals. --regenerate derives its coefficient certificate from the
saved actual rational seed and complete Macaulay2 polynomial dual.
"""
from fractions import Fraction as Q
from pathlib import Path
import ast
import functools
import hashlib
import itertools
import json
import sys

HERE = Path(__file__).resolve().parent
CERT = HERE/'session_localcoh_q13_dual_audit_2026_10_07.json'
INPUTS = ['localcoh-incidence-tensor.txt', 'localcoh-incidence-bases.txt',
          'localcoh-symbol-top.json', 'session-localcoh-origin-family-1-seed.json',
          'session-localcoh-origin-family-1-exception-q13-dual.txt',
          'session-localcoh-origin-family-1-exception-q13-evaluations.txt',
          'session-localcoh-origin-family-1-exception-q13.m2',
          'generate_session_localcoh_q13_module_2026_10_07.py']
DEGREE = 13
MODULUS = (-379834, -966908, -1210068, -571463, 62256, 454897,
           272968, 94014, -39642, -26574, -11268, 2889, 1620, 729)
ZERO = (Q(0),)*DEGREE
ONE = (Q(1),)+(Q(0),)*(DEGREE-1)
RELATION = tuple(Q(-value, MODULUS[-1]) for value in MODULUS[:-1])


def regenerate():
    import sympy as s
    k, lam, t = s.symbols('k lam t')
    modulus = 729*k**13+1620*k**12+2889*k**11-11268*k**10-26574*k**9-39642*k**8+94014*k**7+272968*k**6+454897*k**5+62256*k**4-571463*k**3-1210068*k**2-966908*k-379834
    assert s.Poly(modulus, k, modulus=53).is_irreducible

    def field_reduce(value):
        numerator, denominator = s.fraction(s.cancel(value))
        assert not denominator.has(lam)
        denominator = s.rem(denominator, modulus, k)
        assert denominator != 0
        answer = s.rem(s.rem(numerator, modulus, k)*
                       s.invert(denominator, modulus, k), modulus, k)
        return [str(s.expand(answer).coeff(k, j)) for j in range(DEGREE)]

    def polynomial(value):
        answer = []
        for (power,), coefficient in s.Poly(value, lam).terms():
            coefficients = field_reduce(coefficient)
            if coefficients != ['0']*DEGREE:
                answer.append([power, *coefficients])
        return answer

    data = json.loads((HERE/INPUTS[3]).read_text())
    seed = [s.sympify(v, locals={'k': k}) for v in data['seed']]
    kernel = list(map(s.Rational, data['kernel']))
    dual = []
    for row, line in enumerate((HERE/INPUTS[4]).read_text().splitlines()):
        index, value = line.split(maxsplit=1)
        assert int(index) == row
        dual.append(s.sympify(value.replace('^', '**').replace('lambda', 'lam'),
                             locals={'k': k, 'lam': lam}))
    family = data['family']
    p = 1+s.sympify(family['a1'], locals={'k': k})*t + \
        s.sympify(family['a2'], locals={'k': k})*t*t
    r = 1+s.sympify(family['b1'], locals={'k': k})*t + \
        s.sympify(family['b2'], locals={'k': k})*t*t
    resultant = field_reduce(s.resultant(p, r, t))
    assert resultant != ['0']*DEGREE
    CERT.write_text(json.dumps({
        'coordinate_sha256': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                              for name in INPUTS},
        'defining_polynomial': '729*k^13+1620*k^12+2889*k^11-11268*k^10-26574*k^9-39642*k^8+94014*k^7+272968*k^6+454897*k^5+62256*k^4-571463*k^3-1210068*k^2-966908*k-379834',
        'field_relation': 'k^13=sum(-MODULUS[j]*k^j/729,j=0..12)',
        'irreducibility_prime': 53,
        'alpha': [polynomial(v+lam*c) for v, c in zip(seed, kernel)],
        'dual': list(map(polynomial, dual)),
        'direction_p': [field_reduce(s.expand(p).coeff(t, j)) for j in range(3)],
        'direction_r': [field_reduce(s.expand(r).coeff(t, j)) for j in range(3)],
        'primitive_resultant': resultant,
        'scope': 'First rational endpoint family; all thirteen Q13 roots; every lambda',
        'status': 'EXACT CERTIFICATE VERIFIED BY THIS SCRIPT'
    }, indent=2)+'\n')


def plus(a, b):
    return tuple(x+y for x, y in zip(a, b))


def times(a, b):
    product = [Q(0)]*(2*DEGREE-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            product[i+j] += x*y
    for power in range(2*DEGREE-2, DEGREE-1, -1):
        coefficient = product[power]
        for j, value in enumerate(RELATION):
            product[power-DEGREE+j] += coefficient*value
    return tuple(product[:DEGREE])


def rational_times(a, c):
    return tuple(x*c for x in a)


@functools.lru_cache(maxsize=None)
def inverse(a):
    """Invert by solving the exact rational multiplication matrix."""
    assert a != ZERO
    columns = [times(a, tuple(Q(i == j) for i in range(DEGREE)))
               for j in range(DEGREE)]
    matrix = [[columns[col][row] for col in range(DEGREE)]+[ONE[row]]
              for row in range(DEGREE)]
    for col in range(DEGREE):
        pivot = next(row for row in range(col, DEGREE) if matrix[row][col])
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        leading = matrix[col][col]
        matrix[col] = [value/leading for value in matrix[col]]
        for row in range(DEGREE):
            if row != col and matrix[row][col]:
                leading = matrix[row][col]
                matrix[row] = [value-leading*entry
                               for value, entry in zip(matrix[row], matrix[col])]
    answer = tuple(row[-1] for row in matrix)
    assert times(a, answer) == ONE
    return answer


@functools.lru_cache(maxsize=None)
def evaluate(expression):
    """Derive certificate coefficients directly from saved rational sources.

    Only integers, k, rational arithmetic, and nonnegative integral powers
    are admitted. This parser neither evaluates Python code nor uses SymPy.
    """
    node = ast.parse(expression, mode='eval').body

    def visit(item):
        if isinstance(item, ast.Constant) and type(item.value) is int:
            return rational_times(ONE, Q(item.value))
        if isinstance(item, ast.Name) and item.id == 'k':
            return (Q(0), Q(1))+(Q(0),)*(DEGREE-2)
        if isinstance(item, ast.UnaryOp):
            value = visit(item.operand)
            if isinstance(item.op, ast.USub):
                return rational_times(value, Q(-1))
            assert isinstance(item.op, ast.UAdd)
            return value
        assert isinstance(item, ast.BinOp)
        left = visit(item.left)
        if isinstance(item.op, ast.Pow):
            assert isinstance(item.right, ast.Constant)
            assert type(item.right.value) is int and item.right.value >= 0
            result = ONE
            for _ in range(item.right.value):
                result = times(result, left)
            return result
        right = visit(item.right)
        if isinstance(item.op, ast.Add):
            return plus(left, right)
        if isinstance(item.op, ast.Sub):
            return plus(left, rational_times(right, Q(-1)))
        if isinstance(item.op, ast.Mult):
            return times(left, right)
        assert isinstance(item.op, ast.Div)
        return times(left, inverse(right))

    return visit(node)


def decode(terms):
    result = {}
    for power, *coefficients in terms:
        assert len(coefficients) == DEGREE and power >= 0 and power not in result
        value = tuple(map(Q, coefficients))
        if value != ZERO:
            result[power] = value
    return result


def add(a, b):
    result = dict(a)
    for power, coefficient in b.items():
        value = plus(result.get(power, ZERO), coefficient)
        if value == ZERO:
            result.pop(power, None)
        else:
            result[power] = value
    return result


def scale(a, c):
    return {power: rational_times(value, c) for power, value in a.items()
            if rational_times(value, c) != ZERO}


def multiply(a, b):
    result = {}
    for i, x in a.items():
        for j, y in b.items():
            result = add(result, {i+j: times(x, y)})
    return result


def power(a, n):
    result = {0: ONE}
    for _ in range(n):
        result = multiply(result, a)
    return result


def field_determinant(matrix):
    result = ZERO
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(matrix)) for j in range(i+1, len(matrix)))
        term = ONE
        for row, col in enumerate(permutation):
            term = times(term, matrix[row][col])
        result = plus(result, rational_times(term, Q((-1)**inversions)))
    return result


def verify_irreducibility():
    # Prime degree 13: x^(53^13)=x and gcd(f,x^53-x)=1.
    p = 53
    inverse = pow(MODULUS[-1], -1, p)
    modulus = [(value*inverse) % p for value in MODULUS]

    def trim(value):
        while value and value[-1] == 0:
            value.pop()
        return value

    def remainder(value, divisor):
        value = trim([v % p for v in value])
        inverse = pow(divisor[-1], -1, p)
        while len(value) >= len(divisor):
            coefficient = value[-1]*inverse % p
            offset = len(value)-len(divisor)
            for j, entry in enumerate(divisor):
                value[offset+j] = (value[offset+j]-coefficient*entry) % p
            trim(value)
        return value

    def product(a, b):
        result = [0]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                result[i+j] += x*y
        return remainder(result, modulus)

    def modular_power(a, exponent):
        result = [1]
        while exponent:
            if exponent & 1:
                result = product(result, a)
            a = product(a, a)
            exponent >>= 1
        return result

    def subtract_x(value):
        value = value+[0]*(max(2-len(value), 0))
        value[1] = (value[1]-1) % p
        return trim(value)

    assert subtract_x(modular_power([0, 1], p**DEGREE)) == []
    a, b = modulus, subtract_x(modular_power([0, 1], p))
    while b:
        a, b = b, remainder(a, b)
    assert len(a) == 1


def verify():
    verify_irreducibility()
    data = json.loads(CERT.read_text())
    for name, expected in data['coordinate_sha256'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected, name
    assert data['defining_polynomial'] == '729*k^13+1620*k^12+2889*k^11-11268*k^10-26574*k^9-39642*k^8+94014*k^7+272968*k^6+454897*k^5+62256*k^4-571463*k^3-1210068*k^2-966908*k-379834'
    assert data['irreducibility_prime'] == 53
    alpha, dual = [list(map(decode, data[key])) for key in ('alpha', 'dual')]
    assert len(alpha) == 30 and len(dual) == 74
    assert dual[72] == {0: ONE}
    tensor = [[Q(0)]*542 for _ in range(74)]
    lines = (HERE/INPUTS[0]).read_text().splitlines()
    assert lines[0] == '30 18 74 542'
    for line in lines[1:]:
        row, col, value = line.split()
        tensor[int(row)][int(col)] += Q(value)
    assert [row[540] for row in tensor] == [Q(i == 72) for i in range(74)]
    assert [row[541] for row in tensor] == [Q(i == 73) for i in range(74)]
    p, r = [{j: tuple(map(Q, coefficients))
             for j, coefficients in enumerate(data[key])
             if tuple(map(Q, coefficients)) != ZERO}
            for key in ('direction_p', 'direction_r')]
    top = []
    for i in range(4):
        symbol = multiply({1: ONE}, multiply(power(p, i), power(r, 3-i)))
        top.extend(symbol.get(j, ZERO) for j in range(8))
    matrix = [[Q(value) for value in row] for row in
              json.loads((HERE/INPUTS[2]).read_text())['matrix']]
    assert len(matrix) == len(top) == 32
    # This is the entire affine fibre, not an arbitrary sample of lifts.
    seed_data = json.loads((HERE/INPUTS[3]).read_text())
    kernel = list(map(Q, seed_data['kernel']))
    assert len(kernel) == 30 and any(kernel)
    for coordinate, slope, rational_seed in zip(alpha, kernel, seed_data['seed']):
        assert set(coordinate).issubset({0, 1})
        assert coordinate.get(1, ZERO) == rational_times(ONE, slope)
        assert coordinate.get(0, ZERO) == evaluate(rational_seed)
    family = seed_data['family']
    assert [p.get(j, ZERO) for j in range(3)] == [
        ONE, evaluate(family['a1']), evaluate(family['a2'])]
    assert [r.get(j, ZERO) for j in range(3)] == [
        ONE, evaluate(family['b1']), evaluate(family['b2'])]
    echelon = [row[:] for row in matrix]
    rank = 0
    for col in range(30):
        pivot = next((i for i in range(rank, len(echelon)) if echelon[i][col]), None)
        if pivot is None:
            continue
        echelon[rank], echelon[pivot] = echelon[pivot], echelon[rank]
        coefficient = echelon[rank][col]
        echelon[rank] = [v/coefficient for v in echelon[rank]]
        for i in range(rank+1, len(echelon)):
            coefficient = echelon[i][col]
            if coefficient:
                echelon[i] = [v-coefficient*w for v, w in
                              zip(echelon[i], echelon[rank])]
        rank += 1
    assert rank == 29
    for row, expected in zip(matrix, top):
        value = {}
        for coefficient, element in zip(row, alpha):
            value = add(value, scale(element, coefficient))
        assert value == ({} if expected == ZERO else {0: expected})
    p0, p1, p2 = [p.get(j, ZERO) for j in range(3)]
    r0, r1, r2 = [r.get(j, ZERO) for j in range(3)]
    resultant = field_determinant([
        [p2, p1, p0, ZERO], [ZERO, p2, p1, p0],
        [r2, r1, r0, ZERO], [ZERO, r2, r1, r0]])
    assert resultant == tuple(map(Q, data['primitive_resultant'])) != ZERO
    for col in range(18):
        value = {}
        for row in range(74):
            entry = {}
            for i in range(30):
                entry = add(entry, scale(alpha[i], tensor[row][18*i+col]))
            value = add(value, multiply(dual[row], entry))
        assert not value, ('failed actual tensor column', col, value)
    print('PASS: Q13 irreducibility modulo 53, actual pure-top affine lift, and primitive homogeneous direction.')
    print('PASS: all 18 polynomial dual identities over QQ[k]/Q13[lambda] and n^T u=1.')
    print('PROVED: the Q13 exceptional locus is excluded at all thirteen geometric roots, for every lambda.')


if __name__ == '__main__':
    if '--regenerate' in sys.argv:
        regenerate()
    verify()
