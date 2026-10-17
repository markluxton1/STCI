#!/usr/bin/env python3
"""Exact algebra for the conductor example in the literature-refresh note,
over Q.

Checks the smooth-scroll normalization example, the twisted-cubic basis,
the isolated point in the full inverse image, and the explicit ordinary
twisted-cubic STCI pair. The all-exponent unit obstruction is proved by
valuations in `research/notes/2026-10-05-literature-new-routes.md`, not
inferred from finite powers checked here.
"""

import sympy as sp

x, y, z, xi, w, s, t, u, r = sp.symbols("x y z xi w s t u r")

# S(1,2) -> the cubic pinch surface, with normalization coordinate xi.
scroll = [x * xi - y * z, x * w - y * xi, z * w - xi**2]
scroll_param = {x: u * s, y: u * t, z: s**2, xi: s * t, w: t**2}
assert all(sp.expand(f.subs(scroll_param)) == 0 for f in scroll)
assert sp.expand((x**2 * w - y**2 * z).subs(scroll_param)) == 0

# Gamma=(xi-z-x-y=0) is a hyperplane section of S.
curve = {
    x: s**2 * (t - s),
    y: s * t * (t - s),
    z: s**2 * (s + t),
    xi: s * t * (s + t),
    w: t**2 * (s + t),
}
assert all(sp.expand(f.subs(curve)) == 0 for f in scroll)
assert sp.expand((xi - z - x - y).subs(curve)) == 0
basis = [s**3, s**2 * t, s * t**2, t**3]
basis_matrix = sp.Matrix(
    [[sp.Poly(curve[v], s, t).coeff_monomial(m) for m in basis]
     for v in (x, y, z, w)]
)
assert basis_matrix.det() == 2

# These coordinates are twice the standard twisted-cubic coordinates.
linear = [z - x, z + x, 2 * y + z + x, 2 * w - 2 * y - z - x]
for form, monomial in zip(linear, basis):
    assert sp.expand(form.subs(curve)) == 2 * monomial

l0, l1, l2, l3 = linear
curve_ideal = [l0 * l2 - l1**2, l0 * l3 - l1 * l2, l1 * l3 - l2**2]
assert all(sp.expand(f.subs(curve)) == 0 for f in curve_ideal)

# On z=1 the normalization is x=u,y=ur,xi=r,w=r^2.
chart = {x: u, y: u * r, z: 1, xi: r, w: r**2}
h = r - 1 - u * (1 + r)
pulled = [sp.expand(f.subs(chart)) for f in curve_ideal]
expected = [h * u, h * (r + 1)]
pull_gb = sp.groebner(pulled, u, r, order="lex")
expected_gb = sp.groebner(expected, u, r, order="lex")
assert list(pull_gb) == list(expected_gb)
assert h.subs({u: 0, r: -1}) == -2
# Therefore (h) and (u,r+1) are comaximal, and the pullback is their
# intersection/product. The second component is an isolated reduced point.
assert sp.expand(h + 2 - (r + 1) * (1 - u)) == 0

# Residue-unit obstruction over k(r^2) subset k(r): its conjugate ratio
# has a zero at r=-1 and a pole at r=1, so cannot be torsion.
ratio = (-r - 1) / (r - 1)
assert sp.limit((r - 1) * ratio, r, 1) == -2
assert sp.limit(ratio / (r + 1), r, -1) == sp.Rational(1, 2)

# C is nevertheless STCI on a different carrier. In standard coordinates,
# Q=l0*l2-l1^2 and T=l0*l3^2-2*l1*l2*l3+l2^3 cut out a twisted cubic.
mate = l0 * l3**2 - 2 * l1 * l2 * l3 + l2**3
assert sp.expand(mate.subs(curve)) == 0
a, b, c = sp.symbols("a b c")
# Use independent standard coordinates for the check.
v0, v1, v2, v3 = sp.symbols("v0 v1 v2 v3")
standard_mate = v0 * v3**2 - 2 * v1 * v2 * v3 + v2**3
assert sp.expand(standard_mate.subs({v0: a**2, v1: a*b, v2: b**2, v3: c}) - (a*c-b**3)**2) == 0

print("PASS: scroll identities; twisted-cubic basis determinant 2;")
print("      full inverse-image ideal = (h) intersect (u,r+1);")
print("      nonconstant residue ratio; independent (2,3) STCI certificate.")
