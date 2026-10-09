#!/usr/bin/env python3
"""Verify the first endpoint-family dual at k^2-4k+5=0 exactly.

Default verification uses only Python's standard library.  --regenerate
reduces the saved rational ancestor and Macaulay2 dual using SymPy, and
writes the independently checkable certificate.  All 18 tensor columns
are checked for every lower coefficient lambda, at both geometric roots.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import itertools
import json
import sys

HERE = Path(__file__).resolve().parent
CERT = HERE / 'session_localcoh_q2_dual_audit_2026_10_07.json'
INPUTS = ['localcoh-incidence-tensor.txt', 'localcoh-incidence-bases.txt',
          'localcoh-symbol-top.json', 'session-localcoh-origin-family-1-seed.json',
          'session-localcoh-origin-family-1-exception-q2-dual.txt',
          'session-localcoh-origin-family-1-exception-q2-evaluations.txt',
          'session-localcoh-origin-family-1-exception-q2.m2']
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))


def regenerate():
    import sympy as s
    k, lam, t = s.symbols('k lam t')
    modulus = k*k-4*k+5

    def field_reduce(value):
        numerator, denominator = s.fraction(s.cancel(value))
        # Every denominator must be a unit, not merely be formally discarded.
        denominator = s.rem(denominator, modulus, k)
        assert denominator != 0
        answer = s.rem(s.rem(numerator, modulus, k)*
                       s.invert(denominator, modulus, k), modulus, k)
        return [str(s.expand(answer).coeff(k, j)) for j in range(2)]

    def polynomial(value):
        poly = s.Poly(value, lam)
        result = []
        for (power,), coefficient in poly.terms():
            pair = field_reduce(coefficient)
            if pair != ['0', '0']:
                result.append([power, *pair])
        return result

    data = json.loads((HERE/INPUTS[3]).read_text())
    seed = [s.sympify(v, locals={'k': k}) for v in data['seed']]
    kernel = [s.Rational(v) for v in data['kernel']]
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
    assert resultant != ['0', '0']
    CERT.write_text(json.dumps({
        'coordinate_sha256': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                              for name in INPUTS},
        'defining_polynomial': 'k^2-4k+5',
        'field_relation': 'k^2=4k-5; discriminant=-4, irreducible over QQ',
        'alpha': [polynomial(v+lam*c) for v, c in zip(seed, kernel)],
        'dual': [polynomial(v) for v in dual],
        'direction_p': [field_reduce(s.expand(p).coeff(t, j)) for j in range(3)],
        'direction_r': [field_reduce(s.expand(r).coeff(t, j)) for j in range(3)],
        'primitive_resultant': resultant,
        'scope': 'First rational endpoint family; both k^2-4k+5 roots; every lambda',
        'status': 'EXACT MODULO-POLYNOMIAL CERTIFICATE TO BE VERIFIED'
    }, indent=2)+'\n')


def plus(a, b):
    return (a[0]+b[0], a[1]+b[1])


def times(a, b):
    return (a[0]*b[0]-5*a[1]*b[1],
            a[0]*b[1]+a[1]*b[0]+4*a[1]*b[1])


def rational_times(a, c):
    return (a[0]*c, a[1]*c)


def decode(terms):
    result = {}
    for power, a, b in terms:
        assert power >= 0 and power not in result
        pair = (Q(a), Q(b))
        if pair != ZERO:
            result[power] = pair
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


def verify():
    data = json.loads(CERT.read_text())
    for name, expected in data['coordinate_sha256'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected, name
    assert data['defining_polynomial'] == 'k^2-4k+5'
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
    # Check the actual affine line of lifts, not just an unrelated kernel.
    p, r = [{j: tuple(map(Q, pair)) for j, pair in enumerate(data[key])
             if tuple(map(Q, pair)) != ZERO}
            for key in ('direction_p', 'direction_r')]
    top = []
    for i in range(4):
        symbol = multiply({1: ONE}, multiply(power(p, i), power(r, 3-i)))
        top.extend(symbol.get(j, ZERO) for j in range(8))
    matrix = [[Q(value) for value in row] for row in
              json.loads((HERE/INPUTS[2]).read_text())['matrix']]
    for row, expected in zip(matrix, top):
        value = {}
        for coefficient, element in zip(row, alpha):
            value = add(value, scale(element, coefficient))
        assert value == ({} if expected == ZERO else {0: expected})
    p0, p1, p2 = [p.get(j, ZERO) for j in range(3)]
    r0, r1, r2 = [r.get(j, ZERO) for j in range(3)]
    primitive_resultant = field_determinant([
        [p2, p1, p0, ZERO], [ZERO, p2, p1, p0],
        [r2, r1, r0, ZERO], [ZERO, r2, r1, r0]])
    assert primitive_resultant == tuple(map(Q, data['primitive_resultant'])) != ZERO
    for col in range(18):
        value = {}
        for row in range(74):
            entry = {}
            for i in range(30):
                entry = add(entry, scale(alpha[i], tensor[row][18*i+col]))
            value = add(value, multiply(dual[row], entry))
        assert not value, ('failed actual tensor column', col, value)
    print('PASS: actual pure-top lift and all 18 dual identities over QQ[k]/(k^2-4k+5)[lambda].')
    print('PASS: n^T u=1 identically and the homogeneous direction resultant is a field unit.')
    print('PROVED: the q2 exceptional locus is excluded at both geometric roots, for every lambda.')


if __name__ == '__main__':
    if '--regenerate' in sys.argv:
        regenerate()
    verify()
