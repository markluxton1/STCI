#!/usr/bin/env python3
"""Independently reproduce the b0=0 type-B (4,5) boundary obstruction.

The calculation uses exact sparse arithmetic in
Q(t,z)[m,l]/(m,l)^4 and the full moving quotient coordinate W.  It accepts
the already-derived Banica--Forster delta/gamma chart data as input, then
checks the transition reduction, all six Cech coordinates, and the Bezout
unit certificate.  It does not cover the distinct b1=0, a0=0 boundary corner.
"""

import sympy as sp


t, z = sp.symbols("t z")
MAX_NORMAL_DEGREE = 3


def clean(poly):
    return {
        ij: sp.cancel(coefficient)
        for ij, coefficient in poly.items()
        if coefficient != 0 and sum(ij) <= MAX_NORMAL_DEGREE
    }


def add(left, right):
    result = dict(left)
    for ij, coefficient in right.items():
        result[ij] = result.get(ij, 0) + coefficient
    return clean(result)


def scale(coefficient, poly):
    return clean({ij: coefficient * value for ij, value in poly.items()})


def multiply(left, right):
    result = {}
    for (i, j), left_coefficient in left.items():
        for (k, ell), right_coefficient in right.items():
            if i + j + k + ell <= MAX_NORMAL_DEGREE:
                index = (i + k, j + ell)
                result[index] = (
                    result.get(index, 0) + left_coefficient * right_coefficient
                )
    return clean(result)


def power(poly, exponent):
    result = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def constant(value):
    return {(0, 0): sp.sympify(value)}


M = {(1, 0): sp.Integer(1)}
ELL = {(0, 1): sp.Integer(1)}

# b0=0, a0=b1=1, a1=t.
u = add(scale(t, M), scale(1 + t * z, ELL))
v = add(M, scale(z, ELL))
a = v
b = add(u, scale(sp.Rational(3, 2) * z, v))

normalized_b = scale(z**-4, b)
inverse_denominator = scale(
    z**-4,
    add(
        add(constant(1), scale(-1, normalized_b)),
        add(power(normalized_b, 2), scale(-1, power(normalized_b, 3))),
    ),
)
W = multiply(add(constant(z**3), a), inverse_denominator)
a_prime = add(scale(z, inverse_denominator), scale(-1, power(W, 3)))
b_prime = add(inverse_denominator, scale(-1, power(W, 4)))
u_prime = scale(sp.Rational(1, 2), a_prime)
v_prime = add(scale(-3, multiply(W, a_prime)), scale(2, b_prime))
m_v = add(scale(-1, u_prime), multiply(add(constant(t), W), v_prime))
ell_v = v_prime

delta_u = 2 * (12 * t**3 + 8 * t - (6 * t**2 + 1) * z)
gamma_u = (18 * t**2 * z**2 - 24 * t**2 - 18 * t * z + 3 * z**2 + 2) / 4
delta_v = add(scale(24 * t**3 + 16 * t, W), constant(-(12 * t**2 + 2)))
gamma_v = scale(
    2,
    add(
        add(
            constant(108 * t**5 + 24 * t**3 - 5 * t),
            scale(108 * t**4 + 54 * t**2 - 3, W),
        ),
        scale(36 * t**3 + 24 * t, power(W, 2)),
    ),
)
A_v = add(multiply(delta_v, m_v), scale(-1, multiply(gamma_v, power(ell_v, 2))))

rank_relation = 1 - 8 * t**2 + 12 * t**4 - 72 * t**6


def reduce_mod_rank_relation(expression):
    expression = sp.cancel(expression)
    numerator, denominator = sp.fraction(expression)
    coefficient_field = sp.QQ.frac_field(z)
    relation = sp.Poly(rank_relation, t, domain=coefficient_field)
    numerator_poly = sp.Poly(numerator, t, domain=coefficient_field).rem(relation)
    denominator_poly = sp.Poly(denominator, t, domain=coefficient_field).rem(
        relation
    )
    if denominator_poly.degree() > 0:
        inverse = sp.invert(denominator_poly, relation)
        return sp.factor((numerator_poly * inverse).rem(relation).as_expr())
    return sp.factor(numerator_poly.as_expr() / denominator_poly.as_expr())


A_v = {ij: reduce_mod_rank_relation(coefficient) for ij, coefficient in A_v.items()}
p = reduce_mod_rank_relation(A_v[(1, 0)] / delta_u)

remainder_1 = dict(A_v)
remainder_1[(1, 0)] = reduce_mod_rank_relation(
    remainder_1.get((1, 0), 0) - p * delta_u
)
remainder_1[(0, 2)] = reduce_mod_rank_relation(
    remainder_1.get((0, 2), 0) + p * gamma_u
)
remainder_1 = clean(remainder_1)
q_b = reduce_mod_rank_relation(remainder_1.get((1, 1), 0))
q_c = reduce_mod_rank_relation(remainder_1.get((2, 0), 0))
remainder_2 = dict(remainder_1)
remainder_2[(1, 1)] = 0
remainder_2[(2, 0)] = 0
remainder_2 = clean(remainder_2)
q_d = reduce_mod_rank_relation(remainder_2.get((0, 3), 0))

assert reduce_mod_rank_relation(p - z**-9) == 0
assert set(remainder_2).issubset({(0, 3), (1, 2), (2, 1), (3, 0)})

h3 = reduce_mod_rank_relation(
    (q_b * gamma_u * delta_u + q_d * delta_u**2) / p
)
h3_expanded = sp.expand(h3)
expected = (
    -24 * t * (6 * t**2 - 3 * t + 1) * (6 * t**2 + 3 * t + 1),
    -24 * (9 * t**4 - 12 * t**2 + 1),
    -24 * t * (36 * t**4 - 9 * t**2 + 2),
    16 * (3 * t**4 - 16 * t**2 + 2),
    -8 * t * (636 * t**4 - 80 * t**2 + 1),
    16 * (3 * t**2 - 1) * (62 * t**2 - 7),
)
for index, expected_coefficient in enumerate(expected, 1):
    actual = reduce_mod_rank_relation(h3_expanded.coeff(z, -index))
    assert reduce_mod_rank_relation(actual - expected_coefficient) == 0

# Independently recover the second-neighborhood rank-one equation.
h2 = (
    (2 + 2 * t * z + z**2)
    * (12 + 24 * t * z + (12 * t**2 - 4) * z**2 + 3 * z**4)
    / (8 * z**5)
)
coordinates = [
    reduce_mod_rank_relation(sp.expand(h2).coeff(z, -index))
    for index in range(1, 4)
]
assert all(
    reduce_mod_rank_relation(actual - target) == 0
    for actual, target in zip(
        coordinates,
        ((1 + 6 * t**2) / 4, t * (2 + 3 * t**2), (1 + 18 * t**2) / 2),
    )
)
assert sp.simplify(coordinates[0] * coordinates[2] - coordinates[1] ** 2 - rank_relation / 8) == 0

# H1 is a unit on the complete rank-one boundary scheme in characteristic 0.
x = sp.symbols("x")
q0 = 1 - 8 * x + 12 * x**2 - 72 * x**3
p0 = 36 * x**2 + 3 * x + 1
assert sp.expand((12 * x**2 - 4 * x + 2) * (1 + 6 * x) + q0) == 3
assert sp.expand(
    3 * (20 * x + 3) * q0 + 4 * (30 * x**2 - 3 * x + 2) * p0
) == 17
assert sp.gcd(q0, p0) == 1

print("PASS: the b0=0 type-B boundary obstruction is reproduced exactly")
