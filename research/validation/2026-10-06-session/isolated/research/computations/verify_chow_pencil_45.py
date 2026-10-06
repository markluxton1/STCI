#!/usr/bin/env python3
"""Exact restricted-Chow certificates for degree-(4,5) pairs on C_0.

The script verifies the linear-space dimensions, the displayed basis of a
simple excluded quartic space, the stronger 13- and 28-dimensional carrier
exclusions, the Chow-form restriction to a Schubert pencil, and the
coefficientwise beta-adic orders used in the resultant argument.  It also
checks an explicit irreducible-quartic pair which passes this pencil and fails
the reversed pencil, demonstrating that one pencil is not exhaustive.
"""

import sympy as sp


x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")
xs = (x0, x1, x2, x3)
beta, gamma, U, V = sp.symbols("beta gamma U V")

q = x0 * x3 - x1 * x2
A = x0**2 * x2 - x1**3
B = x0 * x2**2 - x1**2 * x3
D = x2**3 - x1 * x3**2


def exponent_tuples(number_of_variables, total, prefix=()):
    if number_of_variables == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from exponent_tuples(
            number_of_variables - 1, total - first, prefix + (first,)
        )


def monomial(exponents):
    return sp.prod(variable**power for variable, power in zip(xs, exponents))


def coefficient_vector(polynomial, monomials):
    poly = sp.Poly(sp.expand(polynomial), *xs)
    return sp.Matrix([poly.coeff_monomial(term) for term in monomials])


def ideal_component(degree):
    monomials = [monomial(e) for e in exponent_tuples(4, degree)]
    columns = []
    for generator, generator_degree in ((q, 2), (A, 3), (B, 3), (D, 3)):
        for e in exponent_tuples(4, degree - generator_degree):
            columns.append(coefficient_vector(monomial(e) * generator, monomials))
    spanning_matrix = sp.Matrix.hstack(*columns)
    basis_matrix = sp.Matrix.hstack(*spanning_matrix.columnspace())
    return monomials, basis_matrix


def intersect_monomial_space(degree, allowed):
    monomials, ideal_basis = ideal_component(degree)
    exponent_list = [sp.Poly(term, *xs).monoms()[0] for term in monomials]
    forbidden_rows = [
        index for index, exponents in enumerate(exponent_list) if not allowed(exponents)
    ]
    constraints = ideal_basis.extract(forbidden_rows, range(ideal_basis.cols))
    nullspace = constraints.nullspace()
    intersection = ideal_basis * sp.Matrix.hstack(*nullspace)
    intersection_basis = sp.Matrix.hstack(*intersection.columnspace())
    return monomials, ideal_basis, intersection_basis


def polynomial_from_vector(vector, monomials):
    return sp.expand(sum(coefficient * term for coefficient, term in zip(vector, monomials)))


def is_divisible_by(polynomial, variable, exponent):
    expanded = sp.Poly(sp.expand(polynomial), beta, gamma, U, V)
    return expanded.is_zero or min(term[0][0] for term in expanded.terms()) >= exponent


# The explicit Chow quartic on the pencil x1=0, gamma*x3=beta*x0.
p01, p02, p03, p12, p13, p23 = sp.symbols("p01 p02 p03 p12 p13 p23")
chow = (
    -p02**3 * p23
    + 2 * p02**2 * p13**2
    - 4 * p02 * p03**2 * p13
    - 5 * p02 * p03 * p12 * p13
    - p02 * p12**2 * p13
    + p03**4
    + 3 * p03**3 * p12
    + 3 * p03**2 * p12**2
    + p03 * p12**3
    - p01 * p13**3
)
assert sp.expand(
    chow.subs({p01: beta, p02: 0, p03: 0, p12: 0, p13: gamma, p23: 0})
    + beta * gamma**3
) == 0

# K_d=I(C_0)_d intersect (x1,x3^2)_d.
allowed_double_x3 = lambda e: e[1] >= 1 or e[3] >= 2
monomials4, ideal4, K4 = intersect_monomial_space(4, allowed_double_x3)
monomials5, ideal5, K5 = intersect_monomial_space(5, allowed_double_x3)
assert (ideal4.cols, ideal5.cols) == (18, 35)
assert (K4.cols, K5.cols) == (10, 25)

displayed_K4 = (
    x0 * x1 * q,
    x0 * x3 * q,
    x1**2 * q,
    x1 * x2 * q,
    x1 * x3 * q,
    x2 * x3 * q,
    x3**2 * q,
    x1 * A,
    x1 * B,
    x1 * D,
)
displayed_matrix = sp.Matrix.hstack(
    *(coefficient_vector(term, monomials4) for term in displayed_K4)
)
assert displayed_matrix.rank() == 10
assert sp.Matrix.hstack(K4, displayed_matrix).rank() == 10

line_substitution = {x0: gamma * U, x1: 0, x2: V, x3: beta * U}
for column in range(K4.cols):
    restriction = polynomial_from_vector(K4[:, column], monomials4).subs(line_substitution)
    assert is_divisible_by(restriction, beta, 2)
for column in range(K5.cols):
    restriction = polynomial_from_vector(K5[:, column], monomials5).subs(line_substitution)
    assert is_divisible_by(restriction, beta, 2)

# The larger spaces cut out by (x1,x3) have the stated dimensions.  If both
# members lie there, their restrictions share U (or vanish), so the binary
# resultant is identically zero on the pencil.
allowed_base_line = lambda e: e[1] >= 1 or e[3] >= 1
_, _, base4 = intersect_monomial_space(4, allowed_base_line)
_, _, base5 = intersect_monomial_space(5, allowed_base_line)
assert (base4.cols, base5.cols) == (14, 30)
for basis, monomials in ((base4, monomials4), (base5, monomials5)):
    for column in range(basis.cols):
        restriction = sp.expand(
            polynomial_from_vector(basis[:, column], monomials).subs(line_substitution)
        )
        assert restriction == 0 or sp.rem(restriction, U, U) == 0

# Stronger carrier spaces:
# J4=I4 intersect (x1,x2*x3,x3^2), J5=I5 intersect
# (x1,x3^2,x2^2*x3).
allowed_strong4 = (
    lambda e: e[1] >= 1 or (e[2] >= 1 and e[3] >= 1) or e[3] >= 2
)
allowed_strong5 = (
    lambda e: e[1] >= 1 or e[3] >= 2 or (e[2] >= 2 and e[3] >= 1)
)
_, _, J4 = intersect_monomial_space(4, allowed_strong4)
_, _, J5 = intersect_monomial_space(5, allowed_strong5)
assert (J4.cols, J5.cols) == (13, 28)

for column in range(J4.cols):
    restriction = sp.expand(
        polynomial_from_vector(J4[:, column], monomials4).subs(line_substitution)
    )
    assert is_divisible_by(restriction, beta, 1)
    if restriction != 0:
        residual = sp.cancel(restriction / beta).subs(beta, 0)
        assert sp.rem(residual, V, V) == 0

for column in range(J5.cols):
    restriction = sp.expand(
        polynomial_from_vector(J5[:, column], monomials5).subs(line_substitution)
    )
    assert is_divisible_by(restriction, beta, 1)
    if restriction != 0:
        residual = sp.cancel(restriction / beta).subs(beta, 0)
        assert sp.rem(residual, V**2, V) == 0

# A pair that passes the first pencil exactly, but fails its coordinate
# reversal.  This is a route-limitation certificate, not an STCI candidate.
survivor_F = (
    x0**3 * x2
    - x0**3 * x3
    + x0**2 * x1 * x2
    - x0 * x1**3
    - x1**2 * x3**2
    + x1 * x2**3
)
survivor_G = (
    x0**4 * x2
    - x0**4 * x3
    + x0**3 * x1 * x2
    - x0**2 * x1**3
    - x1 * x2**2 * x3**2
    - x1 * x2 * x3**3
    + x2**5
    + x2**4 * x3
)
s, t = sp.symbols("s t")
curve_substitution = {x0: s**4, x1: s**3 * t, x2: s * t**3, x3: t**4}
assert sp.expand(survivor_F.subs(curve_substitution)) == 0
assert sp.expand(survivor_G.subs(curve_substitution)) == 0

first_F = sp.factor(survivor_F.subs(line_substitution))
first_G = sp.factor(survivor_G.subs(line_substitution))
assert sp.expand(first_F - gamma**3 * U**3 * (V - beta * U)) == 0
assert sp.expand(
    first_G - (gamma**4 * U**4 * (V - beta * U) + V**4 * (V + beta * U))
) == 0
assert sp.factor(
    sp.resultant(sp.expand(first_F.subs(U, 1)), sp.expand(first_G.subs(U, 1)), V)
) == -2 * beta**5 * gamma**15

reversed_substitution = {x0: beta * U, x1: V, x2: 0, x3: gamma * U}
reversed_F = sp.factor(survivor_F.subs(reversed_substitution))
reversed_G = sp.factor(survivor_G.subs(reversed_substitution))
assert sp.rem(reversed_F, U, U) == 0
assert sp.rem(reversed_G, U, U) == 0
assert sp.resultant(
    sp.expand(reversed_F.subs(V, 1)), sp.expand(reversed_G.subs(V, 1)), U
) == 0

# As a quadratic in x3, survivor_F has a discriminant of odd x2-degree,
# hence is not a square over the algebraic closure of Q(x0,x1).  Together
# with primitive coefficients this proves absolute irreducibility.
discriminant = sp.discriminant(survivor_F, x3)
assert sp.degree(discriminant, x2) == 3
coefficients_x3 = sp.Poly(survivor_F, x3).all_coeffs()
assert sp.gcd(coefficients_x3[0], coefficients_x3[1]) == 1

print("PASS: restricted Chow-pencil (4,5) exclusion certificates hold exactly")
