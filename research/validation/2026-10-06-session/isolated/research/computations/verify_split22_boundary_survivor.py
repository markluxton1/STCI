#!/usr/bin/env python3
"""Verify the missed content-free d=1,[2,2] first-normal boundary in P-041.

This is only a first-normal incidence certificate.  It does not construct an
integral sextic, a mate, or an STCI presentation.
"""

import sympy as sp


z, s, t = sp.symbols("z s t")

# Linear factors ell=p*xi+r*eta and m=u*xi+v*eta.
p = sp.Integer(1)
r = sp.Rational(3, 2) * z
u = 1 - 3 * z**4 + z**8
v = z / 2 - z**5 / 2 + z**9 / 2

# Evaluation at the quadric direction q1=xi+z*eta/2 is obtained by
# substituting [xi:eta]=[-z/2:1].
assert sp.expand(-p * z / 2 + r) == z
assert sp.expand(-u * z / 2 + v) == z**5

alpha = sp.expand(p * u)
beta = sp.expand(p * v + r * u)
gamma = sp.expand(r * v)

assert alpha == z**8 - 3 * z**4 + 1
assert beta == 2 * z**9 - 5 * z**5 + 2 * z
assert gamma == sp.Rational(3, 4) * (z**10 - z**6 + z**2)


def coefficient(polynomial, degree):
    return sp.Poly(polynomial, z).coeff_monomial(z**degree)


a = [coefficient(alpha, index) for index in range(11)]
b = [coefficient(beta, index) for index in range(11)]
c = [coefficient(gamma, index) for index in range(11)]

# The eleven exact equations for the image of the sextic quadratic-normal map.
equations = [
    -a[9] + 2 * b[10],
    -b[0] + 2 * c[1],
    a[0] - 2 * b[1] + 4 * c[2],
    -3 * a[1] + 2 * b[2] + 4 * c[3],
    a[2] - 2 * b[3] + 4 * c[4],
    a[3] - 2 * b[4] + 4 * c[5],
    -a[4] + 4 * c[6],
    a[5] - 2 * b[6] + 4 * c[7],
    a[6] - 2 * b[7] + 4 * c[8],
    -a[7] - 2 * b[8] + 12 * c[9],
    a[8] - 2 * b[9] + 4 * c[10],
]
assert all(sp.expand(equation) == 0 for equation in equations)

# Homogenize each coefficient pair to its common degree and check that neither
# factor has vertical content on P1.
low_left = s
low_right = sp.Rational(3, 2) * t
high_left = s**9 - 3 * s**5 * t**4 + s * t**8
high_right = (s**8 * t - s**4 * t**5 + t**9) / 2

assert sp.gcd(sp.Poly(low_left, s, t), sp.Poly(low_right, s, t)).total_degree() == 0
assert sp.gcd(sp.Poly(high_left, s, t), sp.Poly(high_right, s, t)).total_degree() == 0

print("PASS: content-free d=1,[2,2] first-normal boundary survivor is exact")
