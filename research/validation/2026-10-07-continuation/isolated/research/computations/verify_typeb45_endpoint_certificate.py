#!/usr/bin/env python3
"""Check the terminal exact certificates in the proposed type-B (4,5) closure.

This script deliberately has a narrow epistemic scope.  It verifies the final
polynomial/rational identities reported by the formal-neighborhood
calculation.  It does *not* derive the transition recursion, prove that all
discarded terms are Cech coboundaries, or establish that the dense and boundary
charts exhaust the type-B parameter space.  Those steps remain mathematical
proof obligations in the research record.
"""

import sympy as sp


z, x = sp.symbols("z x")

# Dense-chart survivor (r,s)=(0,-1/2).
Q = 3 * z**2 + 6 * z + 4
P = (
    81 * z**8
    + 486 * z**7
    + 1341 * z**6
    + 2160 * z**5
    + 2204 * z**4
    + 1464 * z**3
    + 656 * z**2
    + 224 * z
    + 64
)
R = (
    81 * z**7
    + 486 * z**6
    + 1341 * z**5
    + 2160 * z**4
    + 2204 * z**3
    + 1464 * z**2
    + 608 * z
    + 128
)

h4 = -8 * P / (Q * z)
assert sp.factor(h4 + 128 / z + 8 * R / Q) == 0
assert sp.expand(P - 16 * Q - z * R) == 0
assert -128 != 0

# Boundary chart b0=0 after x=t^2.  The Bezout identity certifies that the
# rank-one equation q0=0 and the nonzero-t obstruction factor p0=0 have no
# common root in any characteristic not dividing 17.  The characteristic-zero
# research program is the present target.
q0 = 1 - 8 * x + 12 * x**2 - 72 * x**3
p0 = 36 * x**2 + 3 * x + 1
bezout = 3 * (20 * x + 3) * q0 + 4 * (30 * x**2 - 3 * x + 2) * p0
assert sp.expand(bezout) == 17
assert sp.gcd(q0, p0) == 1

print("PASS: dense and boundary type-B endpoint certificates hold exactly")
