#!/usr/bin/env python3
"""Verify the degree-four rank-one conormal counterfamily from P-039.

The script proves that the displayed quartics lie in I(C_0), have a
nonconstant proportional first-symbol ratio, and are coprime over Q(lambda).
It does not assert that they possess a common local-cohomology ancestor.
"""

import sympy as sp


x, y, z, w = sp.symbols("x y z w")
s, t = sp.symbols("s t")
a, b, lam = sp.symbols("a b lambda")

q = x * w - y * z
A = x**2 * z - y**3
F = x * A + lam * y**2 * q
G = y * A + lam * x * z * q

curve = {x: s**4, y: s**3 * t, z: s * t**3, w: t**4}
assert sp.expand(F.subs(curve)) == 0
assert sp.expand(G.subs(curve)) == 0

# On x=1, use A=a and q=b to first order.
normal_chart = {x: 1, y: t, z: t**3 + a, w: t**4 + t * a + b}
F_chart = sp.expand(F.subs(normal_chart))
G_chart = sp.expand(G.subs(normal_chart))


def first_normal_row(polynomial):
    coefficient_a = sp.diff(polynomial, a).subs({a: 0, b: 0})
    coefficient_b = sp.diff(polynomial, b).subs({a: 0, b: 0})
    return sp.expand(coefficient_a), sp.expand(coefficient_b)


assert first_normal_row(F_chart) == (1, lam * t**2)
assert first_normal_row(G_chart) == (t, lam * t**3)

# Exact identities proving coprimality when lambda is nonzero.
assert sp.expand(x * z * F - y**2 * G - A**2) == 0
assert sp.expand(-y * F + x * G - lam * A * q) == 0

coefficient_field = sp.QQ.frac_field(lam)
F_poly = sp.Poly(F, x, y, z, w, domain=coefficient_field)
G_poly = sp.Poly(G, x, y, z, w, domain=coefficient_field)
assert sp.gcd(F_poly, G_poly).as_expr() == 1

print("PASS: the coprime nonconstant-ratio degree-four family is exact")
