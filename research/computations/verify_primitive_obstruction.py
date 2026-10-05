#!/usr/bin/env python3
"""Check the quadratic transition jet used for the C0 primitive-triple obstruction."""

import sympy as sp

z, epsilon, u, v = sp.symbols("z epsilon u v")
a = epsilon * v
b = epsilon * (u + sp.Rational(3, 2) * z * v)
w = (z**3 + a) / (z**4 + b)
a_prime = z / (z**4 + b) - w**3
b_prime = 1 / (z**4 + b) - w**4
u_prime = sp.Rational(1, 2) * a_prime
v_prime = -3 * w * a_prime + 2 * b_prime

quadratic_u = (
    -sp.Rational(5, 2) * z**-11 * u**2
    - 3 * z**-10 * u * v
    - sp.Rational(3, 8) * z**-9 * v**2
)
quadratic_v = (
    3 * z**-12 * u**2
    - z**-11 * u * v
    - sp.Rational(9, 4) * z**-10 * v**2
)

for expression, linear, quadratic in (
    (u_prime, z**-7 * u, quadratic_u),
    (v_prime, z**-7 * v, quadratic_v),
):
    jet = sp.series(expression, epsilon, 0, 3).removeO()
    assert sp.simplify(sp.diff(jet, epsilon).subs(epsilon, 0) - linear) == 0
    assert (
        sp.simplify(
            sp.diff(jet, epsilon, 2).subs(epsilon, 0) / 2 - quadratic
        )
        == 0
    )

print("PRIMITIVE-TRIPLE QUADRATIC JET VERIFIED")
