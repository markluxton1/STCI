#!/usr/bin/env python3
"""Exact cleared-polynomial audit of the second endpoint family.

Default verification uses Python's standard library. --regenerate uses
SymPy to clear the saved complete rational polynomial dual and ancestor.
Every denominator exception is retained explicitly.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import itertools
import json
import sys

HERE = Path(__file__).resolve().parent
STEM = 'session-localcoh-origin-family-2'
CERT = HERE/'session_localcoh_family2_generic_dual_audit_2026_10_08.json'
SPEC = importlib.util.spec_from_file_location(
    'unchanged_generic_dual', HERE/'session-localcoh-origin-generic-dual.py')
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
BASE.INDEX, BASE.STEM, BASE.CERT = 2, STEM, CERT
add, scale, multiply, decode = BASE.add, BASE.scale, BASE.multiply, BASE.decode
ONE = {(0, 0): Q(1)}


def power(value, exponent):
    result = ONE
    for _ in range(exponent):
        result = multiply(result, value)
    return result


def determinant(matrix):
    answer = {}
    for permutation in itertools.permutations(range(len(matrix))):
        sign = (-1)**sum(permutation[i] > permutation[j]
                         for i in range(len(matrix)) for j in range(i+1, len(matrix)))
        term = ONE
        for row, col in enumerate(permutation):
            term = multiply(term, matrix[row][col])
        answer = add(answer, scale(term, Q(sign)))
    return answer


def univariate(coefficients):
    return {(i, 0): Q(value) for i, value in enumerate(coefficients) if Q(value)}


def polynomial_gcd(first, second):
    """Monic gcd over QQ[k], for independent exception-scope checks."""
    assert all(j == 0 for i, j in first) and all(j == 0 for i, j in second)

    def remainder(value, divisor):
        value = dict(value)
        degree = max(i for i, j in divisor)
        leading = divisor[degree, 0]
        while value and max(i for i, j in value) >= degree:
            offset = max(i for i, j in value)-degree
            coefficient = value[degree+offset, 0]/leading
            shifted = {(i+offset, 0): coefficient*c for (i, j), c in divisor.items()}
            value = add(value, scale(shifted, Q(-1)))
        return value

    while second:
        first, second = second, remainder(first, second)
    return scale(first, Q(1)/first[max(i for i, j in first), 0]) if first else {}


def regenerate():
    import sympy as s
    BASE.regenerate()
    data = json.loads(CERT.read_text())
    k, t = s.symbols('k t')

    def expression(terms):
        assert all(j == 0 for i, j, value in terms)
        return sum(s.Rational(value)*k**i for i, j, value in terms)

    def terms(value):
        return [[i, 0, str(coefficient)] for (i,), coefficient in s.Poly(value, k).terms()
                if coefficient]

    saved = json.loads((HERE/(STEM+'-seed.json')).read_text())
    family = saved['family']
    pp = 1+s.sympify(family['a1'], locals={'k': k})*t + \
        s.sympify(family['a2'], locals={'k': k})*t*t
    rr = 1+s.sympify(family['b1'], locals={'k': k})*t + \
        s.sympify(family['b2'], locals={'k': k})*t*t
    p = [s.expand(pp).coeff(t, j) for j in range(3)]
    r = [s.expand(rr).coeff(t, j) for j in range(3)]
    direction_denominator = s.Integer(1)
    for value in p+r:
        direction_denominator = s.lcm(direction_denominator, s.denom(s.cancel(value)))
    P = [s.cancel(direction_denominator*v) for v in p]
    R = [s.cancel(direction_denominator*v) for v in r]
    res = s.factor(s.det(s.Matrix([[p[2], p[1], p[0], 0], [0, p[2], p[1], p[0]],
                                  [r[2], r[1], r[0], 0], [0, r[2], r[1], r[0]]])))
    assert s.cancel(res-s.sympify(family['resultant'], locals={'k': k})) == 0
    numerator, denominator = s.fraction(res)
    target = expression(data['dual_on_u'])
    scalar, factors = s.factor_list(target)
    chart = (k-1)*(k+1)
    primitive = (k*k+2*k+3)*(3*k**4-2*k**3-6*k*k-18*k-9)
    exceptions = []
    for factor, exponent in factors:
        if s.degree(s.gcd(factor, chart), k) > 0:
            kind = 'OUTSIDE CHART'
        elif s.degree(s.gcd(factor, primitive), k) > 0:
            kind = 'NONPRIMITIVE'
        else:
            kind = 'OPEN PRIMITIVE EXCEPTION'
            assert s.gcd(factor, s.diff(factor, k)) == 1
            assert s.gcd(factor, chart*primitive) == 1
            exceptions.append(factor)
        data.setdefault('exception_factors', []).append({
            'polynomial': str(factor), 'terms': terms(factor),
            'exponent': int(exponent), 'degree': int(s.degree(factor, k)), 'kind': kind})
    for i, factor in enumerate(exceptions):
        for other in exceptions[i+1:]:
            assert s.gcd(factor, other) == 1
    data.update({
        'factorization_scalar': str(scalar),
        'direction_denominator': terms(direction_denominator),
        'direction_P': list(map(terms, P)), 'direction_R': list(map(terms, R)),
        'primitive_resultant_numerator': terms(numerator),
        'primitive_resultant_denominator': terms(denominator),
        'primitive_resultant_formula': str(res),
        'chart_factor': terms(chart), 'nonprimitive_factor': terms(primitive),
        'open_primitive_parameter_count': sum(int(s.degree(value, k)) for value in exceptions),
        'status': 'EXACT POLYNOMIAL CERTIFICATE VERIFIED BY THIS SCRIPT'
    })
    for name in [STEM+'.m2', STEM+'-evaluations.txt', 'session-localcoh-origin-generic-dual.py']:
        data['coordinate_sha256'][name] = hashlib.sha256((HERE/name).read_bytes()).hexdigest()
    CERT.write_text(json.dumps(data, indent=2)+'\n')
    print('Actual homogeneous direction resultant:', res)
    print('Primitive denominator-exception parameter count:', data['open_primitive_parameter_count'])
    for factor in data['exception_factors']:
        print(factor['kind']+': '+factor['polynomial'])


def verify():
    data = json.loads(CERT.read_text())
    BASE.verify()
    alpha = list(map(decode, data['alpha']))
    ancestor_denominator = decode(data['ancestor_denominator'])
    direction_denominator = decode(data['direction_denominator'])
    assert ancestor_denominator and direction_denominator
    assert all(j == 0 for i, j in ancestor_denominator)
    assert all(j == 0 for i, j in direction_denominator)
    km, kp = univariate([-1, 1]), univariate([1, 1])
    assert ancestor_denominator == scale(multiply(power(km, 9), power(kp, 9)), Q(120))
    assert direction_denominator == scale(multiply(power(km, 3), power(kp, 3)), Q(2))
    kernel = list(map(Q, json.loads((HERE/(STEM+'-seed.json')).read_text())['kernel']))
    assert len(kernel) == 30 and any(kernel)
    for coordinate, slope in zip(alpha, kernel):
        assert all(j <= 1 for i, j in coordinate)
        actual = {(i, 0): value for (i, j), value in coordinate.items() if j == 1}
        assert actual == scale(ancestor_denominator, slope)
    matrix = [[Q(value) for value in row] for row in
              json.loads((HERE/'localcoh-symbol-top.json').read_text())['matrix']]
    assert len(matrix) == 32 and all(len(row) == 30 for row in matrix)
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
                echelon[i] = [v-coefficient*w for v, w in zip(echelon[i], echelon[rank])]
        rank += 1
    assert rank == 29
    P, R = [list(map(decode, data[key])) for key in ('direction_P', 'direction_R')]
    assert len(P) == len(R) == 3
    assert P[0] == R[0] == direction_denominator
    qplus = univariate([3, 2, 1])
    qminus = univariate([-1, -2, 1])
    expected_coefficients = [
        (univariate([3, 0, 1]), univariate([2, 0, -2])),
        (scale(qplus, Q(-1)), scale(power(kp, 2), Q(2))),
        (multiply(univariate([-3, 1]), qplus), multiply(power(km, 2), kp)),
        (scale(multiply(multiply(univariate([1, 0, 1]), qminus), qplus), Q(-2)),
         multiply(power(km, 3), power(kp, 3)))
    ]
    for value, (numerator, denominator) in zip(P[1:]+R[1:], expected_coefficients):
        assert multiply(value, denominator) == multiply(direction_denominator, numerator)

    # Polynomial coefficient arrays in the independent curve coordinate t.
    def t_multiply(first, second):
        answer = [{} for _ in range(len(first)+len(second)-1)]
        for i, a in enumerate(first):
            for j, b in enumerate(second):
                answer[i+j] = add(answer[i+j], multiply(a, b))
        return answer

    def t_power(value, exponent):
        result = [ONE]
        for _ in range(exponent):
            result = t_multiply(result, value)
        return result

    top = []
    for i in range(4):
        values = [{}]+t_multiply(t_power(P, i), t_power(R, 3-i))
        assert len(values) == 8
        top.extend(values)
    for row, expected in zip(matrix, top):
        actual = {}
        for coefficient, value in zip(row, alpha):
            actual = add(actual, scale(value, coefficient))
        assert multiply(power(direction_denominator, 3), actual) == \
            multiply(ancestor_denominator, expected)
    res = determinant([[P[2], P[1], P[0], {}], [{}, P[2], P[1], P[0]],
                       [R[2], R[1], R[0], {}], [{}, R[2], R[1], R[0]]])
    numerator = decode(data['primitive_resultant_numerator'])
    denominator = decode(data['primitive_resultant_denominator'])
    assert numerator and denominator
    assert multiply(res, denominator) == multiply(power(direction_denominator, 4), numerator)
    factorization = {(0, 0): Q(data['factorization_scalar'])}
    chart = multiply(km, kp)
    primitive = multiply(qplus, univariate([-9, -18, -6, -2, 3]))
    assert decode(data['chart_factor']) == chart
    assert decode(data['nonprimitive_factor']) == primitive
    open_factors = []
    for factor in data['exception_factors']:
        polynomial = decode(factor['terms'])
        assert all(j == 0 for i, j in polynomial)
        assert max(i for i, j in polynomial) == factor['degree']
        factorization = multiply(factorization, power(polynomial, factor['exponent']))
        chart_gcd = polynomial_gcd(polynomial, chart)
        primitive_gcd = polynomial_gcd(polynomial, primitive)
        if factor['kind'] == 'OUTSIDE CHART':
            assert max(i for i, j in chart_gcd) > 0
        elif factor['kind'] == 'NONPRIMITIVE':
            assert max(i for i, j in primitive_gcd) > 0
        else:
            assert factor['kind'] == 'OPEN PRIMITIVE EXCEPTION'
            assert chart_gcd == primitive_gcd == ONE
            derivative = {(i-1, 0): coefficient*i for (i, j), coefficient in polynomial.items()
                          if i}
            assert polynomial_gcd(polynomial, derivative) == ONE
            for other in open_factors:
                assert polynomial_gcd(polynomial, other) == ONE
            open_factors.append(polynomial)
    assert factorization == decode(data['dual_on_u'])
    assert sum(max(i for i, j in factor) for factor in open_factors) == \
        data['open_primitive_parameter_count']
    targets = [[Q(0), Q(0)] for _ in range(74)]
    for line in (HERE/'localcoh-incidence-tensor.txt').read_text().splitlines()[1:]:
        row, col, value = line.split()
        if int(col) >= 540:
            targets[int(row)][int(col)-540] += Q(value)
    assert targets == [[Q(i == 72), Q(i == 73)] for i in range(74)]
    print('PASS: complete affine fibre, rank29 actual top map and all 32 cleared pure-top identities.')
    print('PASS: homogeneous quadratic resultant and displayed denominator factorization.')
    print('OPEN:', data['open_primitive_parameter_count'],
          'primitive parameter points exceptional to this dual, with every lambda retained.')


if __name__ == '__main__':
    if '--regenerate' in sys.argv:
        regenerate()
    verify()
