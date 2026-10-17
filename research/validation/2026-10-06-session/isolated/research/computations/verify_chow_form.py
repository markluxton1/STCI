"""Exact Chow-form check for the monomial rational quartic C_0.

For a line in P^3 written as the intersection of the hyperplanes

    A_0 x_0 + ... + A_3 x_3 = 0,
    B_0 x_0 + ... + B_3 x_3 = 0,

the Chow form of C_0 = [s^4:s^3 t:s t^3:t^4] is the resultant of the two
pulled-back binary quartics.  This script verifies a compact expression in
the Pluecker coordinates p_ij = A_i B_j - A_j B_i.
"""

import sympy as sp


x = sp.symbols("x")
A = sp.symbols("A0:4")
B = sp.symbols("B0:4")

f = A[0] + A[1] * x + A[2] * x**3 + A[3] * x**4
g = B[0] + B[1] * x + B[2] * x**3 + B[3] * x**4
resultant = sp.expand(sp.resultant(f, g, x))


def minor(i, j):
    return A[i] * B[j] - A[j] * B[i]


p01 = minor(0, 1)
p02 = minor(0, 2)
p03 = minor(0, 3)
p12 = minor(1, 2)
p13 = minor(1, 3)
p23 = minor(2, 3)

chow_form = (
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

assert sp.expand(resultant - chow_form) == 0

# Each displayed summand has Pluecker degree four, as required for the Chow
# form of a degree-four curve.  The expanded resultant is separately
# homogeneous of bidegree (4,4) in the A and B hyperplane coefficients.
pluecker_symbols = sp.symbols("p01 p02 p03 p12 p13 p23")
P01, P02, P03, P12, P13, P23 = pluecker_symbols
abstract_chow_form = (
    -P02**3 * P23
    + 2 * P02**2 * P13**2
    - 4 * P02 * P03**2 * P13
    - 5 * P02 * P03 * P12 * P13
    - P02 * P12**2 * P13
    + P03**4
    + 3 * P03**3 * P12
    + 3 * P03**2 * P12**2
    + P03 * P12**3
    - P01 * P13**3
)
assert sp.Poly(abstract_chow_form, *pluecker_symbols).is_homogeneous
assert sp.Poly(abstract_chow_form, *pluecker_symbols).total_degree() == 4

expanded = sp.Poly(resultant, *A, *B)
assert all(sum(monomial[:4]) == 4 for monomial, _ in expanded.terms())
assert all(sum(monomial[4:]) == 4 for monomial, _ in expanded.terms())

print("PASS: the 10-term Pluecker quartic equals the exact line resultant")
