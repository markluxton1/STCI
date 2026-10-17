#!/usr/bin/env python3
"""Reconstruct every type-A (4,5) quotient chart and the terminal obstruction.

Characteristic-zero exact arithmetic. This independently derives the quotient
rank equations, excludes the two exceptional quotient lines by triple
flatness, and reconstructs the unique remaining triple/quadruple route from
the moving ambient coordinate W. It computes the final H^1(O(-9)) class rather
than merely testing the numerical vector recorded in P-025.

The mathematical justification for interpreting the calculations as
Banica--Forster extension obstructions is in
research/notes/2026-10-05-typea-audit.md.
"""

import sympy as sp

z = sp.symbols("z", nonzero=True)
theta = sp.symbols("theta")
MAX_NORMAL_DEGREE = 4


def clean(poly):
    result = {}
    for ij, coefficient in poly.items():
        if sum(ij) <= MAX_NORMAL_DEGREE:
            coefficient = sp.cancel(coefficient)
            if coefficient != 0:
                result[ij] = coefficient
    return result


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
            index = (i + k, j + ell)
            if sum(index) <= MAX_NORMAL_DEGREE:
                result[index] = result.get(index, 0) + left_coefficient * right_coefficient
    return clean(result)


def power(poly, exponent):
    result = constant(1)
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def constant(value):
    return {(0, 0): sp.sympify(value)}


M = {(1, 0): sp.Integer(1)}
ELL = {(0, 1): sp.Integer(1)}


def exact_transition(u, v):
    """Return the moving coordinate W and exact split conormal jets."""
    a = v
    b = add(u, scale(sp.Rational(3, 2) * z, v))
    normalized_b = scale(z**-4, b)
    inverse_denominator = constant(0)
    for degree in range(MAX_NORMAL_DEGREE + 1):
        inverse_denominator = add(
            inverse_denominator,
            scale((-1) ** degree * z**-4, power(normalized_b, degree)),
        )
    W = multiply(add(constant(z**3), a), inverse_denominator)
    a_prime = add(scale(z, inverse_denominator), scale(-1, power(W, 3)))
    b_prime = add(inverse_denominator, scale(-1, power(W, 4)))
    u_prime = scale(sp.Rational(1, 2), a_prime)
    v_prime = add(scale(-3, multiply(W, a_prime)), scale(2, b_prime))
    return W, u_prime, v_prime


# Reconstruct the finite quotient chart and the genuinely missing chart.
MAX_NORMAL_DEGREE = 2
_, u_prime, v_prime = exact_transition(add(M, scale(-theta, ELL)), ELL)
m_prime = add(u_prime, scale(theta, v_prime))
h2 = sp.expand(m_prime[(0, 2)] * z**7)
assert sp.simplify(h2 - 3 * (
    theta**3 / z**5 - theta**2 / (2 * z**4)
    + theta / (4 * z**3) - 1 / (8 * z**2)
)) == 0

# Multiplication by delta in H^0(O(3)) must kill H^1(O(-7)) in H^1(O(-4)).
d0, d1, d2, d3 = sp.symbols("d0 d1 d2 d3")
delta = d0 + d1 * z + d2 * z**2 + d3 * z**3
kill_equations = [sp.expand(delta * h2).coeff(z, -index) for index in range(1, 4)]
rank_matrix = sp.Matrix([
    [sp.diff(equation, variable) for variable in (d0, d1, d2, d3)]
    for equation in kill_equations
]) * sp.Rational(8, 3)
assert rank_matrix == sp.Matrix([
    [0, -1, 2 * theta, -4 * theta**2],
    [-1, 2 * theta, -4 * theta**2, 8 * theta**3],
    [2 * theta, -4 * theta**2, 8 * theta**3, 0],
])
assert rank_matrix[:, [0, 1, 3]].det() == -16 * theta**4
assert rank_matrix * sp.Matrix([0, 2 * theta, 1, 0]) == sp.zeros(3, 1)
assert rank_matrix.subs(theta, 0).rank() == 2
assert sp.expand(z * (z + 2 * theta) * h2) == 6 * theta**4 / z**4 - sp.Rational(3, 8)

# At theta=0, delta=z^2(d2+d3*z), gamma_U=3(d2+d3*z)/8,
# gamma_V=0. The additional projective linear factor is a common zero.
assert sp.expand((d2 * z**2 + d3 * z**3) * h2.subs(theta, 0)) == -sp.Rational(3, 8) * (d2 + d3 * z)
_, u_infinity, v_infinity = exact_transition(ELL, M)
h_infinity = sp.expand(v_infinity[(0, 2)] * z**7)
assert h_infinity == 3 / z**5
assert [sp.expand(delta * h_infinity).coeff(z, -index) for index in range(1, 4)] == [0, 3 * d3, 3 * d2]

# The ambient diagonal torus carries every nonzero theta to theta=1.
MAX_NORMAL_DEGREE = 4
W, u_prime, v_prime = exact_transition(add(M, scale(-1, ELL)), ELL)
m_v = add(u_prime, v_prime)
ell_v = v_prime
delta_u = z * (z + 2)
gamma_u = sp.Rational(3, 8)
delta_v = add(W, scale(2, power(W, 2)))
gamma_v = sp.Integer(6)
A_u = add(scale(delta_u, M), scale(-gamma_u, power(ELL, 2)))
A_v = add(multiply(delta_v, m_v), scale(-gamma_v, power(ell_v, 2)))
p3 = sp.cancel(A_v[(1, 0)] / delta_u)
assert p3 == z**-10
remainder = add(A_v, scale(-p3, A_u))
assert remainder.get((0, 2), 0) == 0
q_b = remainder.get((1, 1), 0)
q_d = remainder.get((0, 3), 0)
h3 = sp.expand(sp.cancel((q_b * gamma_u * delta_u + q_d * delta_u**2) / p3))
assert h3 == z / 16 + sp.Rational(1, 4) + 8 / z**5 - 64 / z**6 - 144 / z**7
assert all(h3.coeff(z, -index) == 0 for index in range(1, 5))
rho_u = -(z + 4) / 16
rho_v_at_w = 8 - 64 / z - 144 / z**2
assert sp.simplify(h3 + rho_u - z**-5 * rho_v_at_w) == 0
assert sp.gcd(delta_u, rho_u) == 1
w = sp.symbols("w")
assert sp.gcd(w + 2 * w**2, 8 - 64 * w - 144 * w**2) == 1
rho_v = add(add(constant(8), scale(-64, W)), scale(-144, power(W, 2)))

# Exact quadruple generators. Both gamma charts are units, and (delta,rho)=1.
E_u = add(scale(delta_u, A_u), scale(-rho_u / gamma_u, multiply(M, ELL)))
E_v = add(multiply(delta_v, A_v), scale(-1 / gamma_v, multiply(rho_v, multiply(m_v, ell_v))))
H_u = add(scale(delta_u, multiply(M, ELL)), scale(-gamma_u, power(ELL, 3)))
H_v = add(multiply(delta_v, multiply(m_v, ell_v)), scale(-gamma_v, power(ell_v, 3)))
p4 = sp.cancel(E_v[(1, 0)] / delta_u**2)
assert p4 == z**-13

# Generic primitive coordinates evaluate the conormal maps. Every assigned
# generator image is regular; relations extend across delta=0 by torsion-free
# target descent. See the note for that justification.
ell = sp.symbols("ell")
m_order3 = gamma_u / delta_u * ell**2 + rho_u / delta_u**3 * ell**3
m_order4 = m_order3 + rho_u**2 / (gamma_u * delta_u**5) * ell**4


def evaluate_layer(poly, order, replacement):
    expression = 0
    for (i, j), coefficient in poly.items():
        if 2 * i + j <= order:
            expression += coefficient * replacement**i * ell**j
    return sp.cancel(sp.expand(expression).coeff(ell, order) * delta_u**2)


phi3 = lambda poly: evaluate_layer(poly, 3, m_order3)
phi4 = lambda poly: evaluate_layer(poly, 4, m_order4)
assert sp.simplify(phi3(A_v) - z**-15 * rho_v_at_w) == 0
assert sp.simplify(phi3(multiply(m_v, ell_v)) - z**-15 * gamma_v * (1 / z + 2 / z**2)) == 0
assert phi3(power(m_v, 2)) == 0
assert sp.simplify(phi3(power(ell_v, 3)) - z**-15 * (1 / z + 2 / z**2)**2) == 0

assert phi4(E_u) == 0
assert phi4(power(M, 2)) == gamma_u**2
assert phi4(H_u) == rho_u
assert sp.simplify(phi4(power(ELL, 4)) - delta_u**2) == 0
assert sp.simplify(phi4(power(m_v, 2)) - z**-22 * gamma_v**2) == 0
assert sp.simplify(phi4(H_v) - z**-22 * rho_v_at_w) == 0
assert sp.simplify(phi4(power(ell_v, 4)) - z**-22 * (1 / z + 2 / z**2)**2) == 0
h4 = sp.expand(sp.cancel(phi4(E_v) / p4))
expected_h4 = (
    -sp.Rational(5, 384) - sp.Rational(5, 64) / z
    - sp.Rational(5, 96) / z**2 + sp.Rational(5, 48) / z**3
    - sp.Rational(5, 24) / z**4 + sp.Rational(5, 12) / z**5
    - sp.Rational(5, 6) / z**6 + sp.Rational(5, 3) / z**7
    + 10 / z**8 - sp.Rational(124, 3) / z**9
    + 168 / z**10 + 432 / z**11
)
assert sp.expand(h4 - expected_h4) == 0
coordinates = tuple(h4.coeff(z, -index) for index in range(1, 9))
recorded_coordinates = (
    -sp.Rational(15, 512), -sp.Rational(5, 256), sp.Rational(5, 128),
    -sp.Rational(5, 64), sp.Rational(5, 32), -sp.Rational(5, 16),
    sp.Rational(5, 8), sp.Rational(15, 4),
)
assert coordinates == tuple(sp.Rational(8, 3) * value for value in recorded_coordinates)
assert coordinates[0] != 0
print("PASS: all type-A quotient strata, unique quadruple route, and terminal obstruction reconstructed")
print("H^1(O(-9)) coordinates:", coordinates)
print("The vector is 8/3 times the vector previously recorded in P-025.")
