#!/usr/bin/env python3
"""Explore the corrected type-B second-neighborhood obstruction for (4,5).

This remains research scratch, not a proved project result.  An earlier version
froze the quotient coefficients while changing embedded charts.  That is
incorrect: the coefficients themselves acquire normal-direction corrections.
The three formulas below are the corrected Cech coordinates.  The discarded
frozen-frame coordinates differ by a nonzero multiple of the determinant and
must not be used.
"""

import sympy as sp

z = sp.symbols("z", nonzero=True)
a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1")

alpha = a0 + a1 * z
beta = b0 + b1 * z
Delta = sp.expand(a0 * b1 - a1 * b0)
assert Delta != 0  # geometrically, restrict to the open set Delta != 0

c1 = sp.factor(
    b1 * (2 * a0 * b1 + 12 * a1**2 + 16 * a1 * b0 + 9 * b0**2) / 8
)
c2 = sp.factor(
    (2 * a1 + b0)
    * (8 * a0 * b1 + 12 * a1**2 + 4 * a1 * b0 + 3 * b0**2)
    / 8
)
c3 = sp.factor(
    a0 * (2 * a0 * b1 + 36 * a1**2 + 16 * a1 * b0 + 3 * b0**2) / 4
)
coords = [c1, c2, c3]
h = c1 / z + c2 / z**2 + c3 / z**3

print("Delta =", Delta)
print("corrected h =", h)
for j, c in enumerate(coords, 1):
    print(f"c{j} =", c)

# A degree-one divisor with equation d=d0+d1*z kills h iff the functional
# represented by h annihilates d*H^0(O(1)).  In Cech coordinates this can
# also be checked directly by multiplying h by d and asking that the two
# H^1(O(-3)) coordinates vanish.
d0, d1 = sp.symbols("d0 d1")
dh = sp.expand((d0 + d1 * z) * h)
kill = [sp.factor(dh.coeff(z, -j)) for j in range(1, 3)]
print("kill equations =", kill)
rank_one = sp.factor(c1 * c3 - c2**2)
print("kill determinant =", rank_one)

# On c1 != 0 and the rank-one locus, delta=c2-c1*z is the unique killing
# section up to scale.  The next lci/epimorphism condition at its root has
# coefficient c1^2, so it is automatically nonzero on this chart.
delta = c2 - c1 * z
delta_h = sp.expand(delta * h)
assert sp.factor(delta_h.coeff(z, -1)) == 0
assert sp.factor(delta_h.coeff(z, -2)) == -rank_one
print("canonical killing section on c1!=0:", delta)
print("remaining coefficient modulo rank-one equation:", c1**2)
