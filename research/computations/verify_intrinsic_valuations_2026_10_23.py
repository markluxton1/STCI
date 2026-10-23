#!/usr/bin/env python3
"""Exact, stdlib-only checks for the provisional coefficient-valuation note.

This checks examples and formulas, not the general valuation constructions,
accepted global mu4 theorem, or characteristic-zero (4,4) exclusion.
"""
from fractions import Fraction
from math import comb


def clean(poly, characteristic=0):
    if characteristic:
        poly = {m: c % characteristic for m, c in poly.items()}
    return {m: c for m, c in poly.items() if c}


def add(a, b, characteristic=0):
    result = dict(a)
    for monomial, coefficient in b.items():
        result[monomial] = result.get(monomial, 0) + coefficient
    return clean(result, characteristic)


def scale(a, factor):
    return clean({m: factor * c for m, c in a.items()})


def multiply(a, b, characteristic=0):
    result = {}
    for m, c in a.items():
        for n, d in b.items():
            exponent = tuple(i + j for i, j in zip(m, n))
            result[exponent] = result.get(exponent, 0) + c * d
    return clean(result, characteristic)


def power(a, exponent, characteristic=0):
    dimension = len(next(iter(a)))
    result = {(0,) * dimension: 1}
    for _ in range(exponent):
        result = multiply(result, a, characteristic)
    return result


def weighted_value(poly, weights):
    assert poly
    return min(sum(Fraction(e) * w for e, w in zip(m, weights)) for m in poly)


def lowest_normal_degree(poly):
    return min(m[1] + m[2] for m in poly)


def derivative(poly, variable, characteristic=0):
    result = {}
    for monomial, coefficient in poly.items():
        exponent = monomial[variable]
        if exponent:
            reduced = list(monomial)
            reduced[variable] -= 1
            reduced = tuple(reduced)
            result[reduced] = result.get(reduced, 0) + exponent * coefficient
    return clean(result, characteristic)


def substitute(poly, images, characteristic=0):
    dimension = len(next(iter(images[0])))
    result = {}
    for monomial, coefficient in poly.items():
        term = {(0,) * dimension: coefficient}
        for exponent, image in zip(monomial, images):
            term = multiply(term, power(image, exponent, characteristic), characteristic)
        result = add(result, term, characteristic)
    return result


def standard_monomials(generators, bound):
    return {
        (i, j)
        for i in range(bound)
        for j in range(bound)
        if not any(i >= a and j >= b for a, b in generators)
    }


def main():
    # Variables are (z,U,V); coefficients are integers, exactly.
    z = {(1, 0, 0): 1}
    u = {(0, 1, 0): 1}
    v = {(0, 0, 1): 1}
    f = scale(u, -1)
    g = add(power(add(power(z, 3), v), 4),
            scale(power(add(power(z, 4), u), 3), -1))
    p = add(power(add(power(z, 3), v), 4), scale(power(z, 12), -1))
    expected_p = {(0, 0, 4): 1, (3, 0, 3): 4,
                  (6, 0, 2): 6, (9, 0, 1): 4}
    assert p == expected_p
    h = add(add(scale(power(z, 8), 3),
                scale(multiply(power(z, 4), u), 3)), power(u, 2))
    assert add(g, scale(multiply(h, f), -1)) == p
    assert clean(p, 2) == {(0, 0, 4): 1}
    assert add(clean(g, 2), scale(multiply(clean(h, 2), clean(f, 2), 2), -1), 2) == clean(p, 2)
    assert lowest_normal_degree(p) == 1
    assert lowest_normal_degree(clean(p, 2)) == 4
    assert lowest_normal_degree(clean(g, 2)) == 1

    # All term weights at the critical rho=3 are exactly 12.
    assert {sum(Fraction(e) * w for e, w in zip(m, (1, 17, 3))) for m in p} == {12}
    for rho in (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3),
                Fraction(7, 2), Fraction(4), Fraction(5)):
        char_zero = weighted_value(p, (1, 17, rho))
        char_two = weighted_value(clean(p, 2), (1, 17, rho))
        assert char_zero == min(4 * rho, 9 + rho)
        assert char_two == 4 * rho
    observed = []
    for rho in (Fraction(1), Fraction(3), Fraction(4)):
        values = tuple(min(Fraction(17), weighted_value(clean(p, char), (1, 17, rho)))
                       for char in (0, 2))
        observed.append(values)
    assert observed == [(4, 4), (12, 12), (13, 16)]

    # Substitute V=z^3*xi into P and divide by z^12.
    q = {}
    for (z_exp, u_exp, v_exp), coefficient in p.items():
        assert u_exp == 0
        assert z_exp + 3 * v_exp == 12
        q[v_exp] = coefficient
    assert q == {1: 4, 2: 6, 3: 4, 4: 1}
    assert q == {i: comb(4, i) for i in range(1, 5)}
    assert {i: c % 2 for i, c in q.items() if c % 2} == {4: 1}
    assert q[1] == 4 and q[1] % 2 == 0

    # Characteristic-two pencil: write lambda=b^4. All derivatives vanish
    # on x0=b^2*x3, and H there is (x1+b*x2)^4.
    variables = [{tuple(int(i == j) for i in range(5)): 1} for j in range(5)]
    x0, x1, x2, x3, b = variables
    lam = power(b, 4, 2)
    surface = add(add(power(x1, 4, 2), multiply(power(x0, 3, 2), x3, 2), 2),
                  add(multiply(lam, power(x2, 4, 2), 2),
                      multiply(lam, multiply(x0, power(x3, 3, 2), 2), 2), 2), 2)
    common = add(power(x0, 2, 2), multiply(lam, power(x3, 2, 2), 2), 2)
    gradients = [derivative(surface, i, 2) for i in range(4)]
    assert gradients[0] == multiply(x3, common, 2)
    assert gradients[1] == gradients[2] == {}
    assert gradients[3] == multiply(x0, common, 2)
    plane_images = [multiply(power(b, 2, 2), x3, 2), x1, x2, x3, b]
    restricted = substitute(surface, plane_images, 2)
    assert restricted == power(add(x1, multiply(b, x2, 2), 2), 4, 2)
    assert all(substitute(d, plane_images, 2) == {} for d in gradients)
    line_images = [multiply(power(b, 2, 2), x3, 2), multiply(b, x2, 2), x2, x3, b]
    assert substitute(surface, line_images, 2) == {}
    # lambda=a^8 makes the moving first symbol 1+lambda*z^8 one eighth power.
    az = {(1, 1): 1}
    unit = {(0, 0): 1}
    moving = add(unit, power(az, 8, 2), 2)
    assert moving == power(add(unit, az, 2), 8, 2)
    assert derivative(moving, 0, 2) == {}

    # New variables (U',V') have apparent weights (1,1), but V'-U'=V
    # has true old-chart weight 2. The residue relation is necessary.
    up = u
    vp = add(v, u)
    assert weighted_value(up, (0, 1, 2)) == 1
    assert weighted_value(vp, (0, 1, 2)) == 1
    difference_in_old_chart = add(vp, scale(up, -1))
    assert difference_in_old_chart == v
    assert weighted_value(difference_in_old_chart, (0, 1, 2)) == 2
    difference_in_new_chart = {(1, 0): -1, (0, 1): 1}
    assert weighted_value(difference_in_new_chart, (1, 1)) == 1

    # Explicit equal ideal-value / unequal-colength example.
    j1 = ((2, 0), (0, 2))
    j2 = ((2, 0), (1, 1), (0, 2))
    assert standard_monomials(j1, 3) == {(0, 0), (1, 0), (0, 1), (1, 1)}
    assert standard_monomials(j2, 3) == {(0, 0), (1, 0), (0, 1)}
    for a in (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5)):
        for b in (Fraction(1, 3), Fraction(1), Fraction(3), Fraction(7)):
            assert min(2 * a, 2 * b) == min(2 * a, a + b, 2 * b)
    assert len(standard_monomials(((1, 0), (0, 1)), 5)) == 1
    assert len(standard_monomials(((1, 0), (0, 4)), 5)) == 4

    # The divergent-tail counterexample has term value -n^2+n*alpha.
    # For every tested alpha, values are strictly decreasing once n>alpha.
    for alpha in (Fraction(1, 2), Fraction(1), Fraction(3), Fraction(12)):
        for n in range(15, 25):
            assert -(n + 1) ** 2 + (n + 1) * alpha < -n ** 2 + n * alpha
    print("PASS: exact cancellation and characteristic reduction")
    print("PASS: coefficient/normal values (rho=1,3,4):", observed)
    print("PASS: critical residue polynomial, coordinate-change failure")
    print("PASS: characteristic-two moving symbol and singular surface line")
    print("PASS: equal scalar ideal values with colengths 4 and 3")
    print("Scope: explicit examples only; no new global (4,4) exclusion")


if __name__ == '__main__':
    main()
