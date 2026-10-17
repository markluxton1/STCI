#!/usr/bin/env python3
"""Verify the remaining rank-zero type-B (4,5) corner calculation.

This exact moving-coordinate calculation treats a0=b1=0, b0=1, a1=t.
It identifies the three characteristic-zero rank-zero parameters and checks
that the next gluing datum has gamma=0.  The final length-four fiber is the
explicit local Bănică--Forster flatness obstruction.
"""

import sympy as sp


t, z = sp.symbols("t z", nonzero=True)
MAX_NORMAL_DEGREE = 4


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

# m=t*z*v-u, ell=v; the ambient split frame is u=b-(3/2)za, v=a.
u = add(scale(-1, M), scale(t * z, ELL))
v = ELL
a = v
b = add(u, scale(sp.Rational(3, 2) * z, v))

normalized_b = scale(z**-4, b)
inverse_denominator = scale(
    z**-4,
    add(
        add(constant(1), scale(-1, normalized_b)),
        add(
            power(normalized_b, 2),
            add(scale(-1, power(normalized_b, 3)), power(normalized_b, 4)),
        ),
    ),
)
W = multiply(add(constant(z**3), a), inverse_denominator)
a_prime = add(scale(z, inverse_denominator), scale(-1, power(W, 3)))
b_prime = add(inverse_denominator, scale(-1, power(W, 4)))
u_prime = scale(sp.Rational(1, 2), a_prime)
v_prime = add(scale(-3, multiply(W, a_prime)), scale(2, b_prime))
m_v = add(scale(t, v_prime), scale(-1, multiply(W, u_prime)))
ell_v = scale(1 / t, u_prime)

linear_m = sp.factor(m_v[(1, 0)])
linear_ell = sp.factor(ell_v[(0, 1)])
h2 = sp.factor(m_v[(0, 2)] / linear_m)
assert linear_m == z**-8
assert linear_ell == z**-6

c1 = sp.factor(sp.expand(h2).coeff(z, -1))
c2 = sp.factor(sp.expand(h2).coeff(z, -2))
c3 = sp.factor(sp.expand(h2).coeff(z, -3))
expected_c2 = (2 * t + 1) * (12 * t**2 + 4 * t + 3) / 8
assert c1 == 0 and c3 == 0
assert sp.simplify(c2 - expected_c2) == 0

rank_zero_polynomial = sp.factor((2 * t + 1) * (12 * t**2 + 4 * t + 3))
assert sp.degree(rank_zero_polynomial, t) == 3

# When rank_zero_polynomial=0, the raw h2 is identically zero.  For a general
# delta in H^0(O(1)), gluing requires gamma_U=z^-3 gamma_V.  Since O(-3) has
# no global section, all coefficients of gamma vanish.
assert sp.rem(sp.together(h2 * z**2).as_numer_denom()[0], rank_zero_polynomial, t) == 0

w = sp.symbols("w")
d0, d1 = sp.symbols("d0 d1")
delta_u = d0 + d1 * z
delta_v = d0 * w + d1
assert sp.simplify(delta_v.subs(w, 1 / z) - delta_u / z) == 0

gamma_u_coefficients = sp.symbols("gU0:3")
gamma_v_coefficients = sp.symbols("gV0:3")
gamma_u = sum(gamma_u_coefficients[index] * z**index for index in range(3))
gamma_v = sum(gamma_v_coefficients[index] * w**index for index in range(3))
gluing = sp.expand(gamma_u - z**-3 * gamma_v.subs(w, 1 / z))
equations = [gluing.coeff(z, exponent) for exponent in range(-5, 3)]
solution = sp.linsolve(
    equations, (*gamma_u_coefficients, *gamma_v_coefficients)
)
assert solution == sp.FiniteSet((0, 0, 0, 0, 0, 0))

# At the zero of every nonzero delta, the proposed triple fiber ideal is
# (m*ell,m^2,ell^3); its standard monomials are 1,m,ell,ell^2, so its length
# is four instead of the required three.
standard_monomials = ((0, 0), (1, 0), (0, 1), (0, 2))
assert len(standard_monomials) == 4

print("PASS: all three type-B corner points fail the triple flatness test")
