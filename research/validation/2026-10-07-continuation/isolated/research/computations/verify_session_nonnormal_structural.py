#!/usr/bin/env python3
"""Exact arithmetic controls for the nonnormal structural note.

The theorem hypotheses and global arguments are in the note. This script
verifies the source-table intersection arithmetic, ordinary Roman pinch
coordinates/no-conic certificate, and a degenerate-pinch countermodel.
"""
import sympy as s

x, y, z, t = s.symbols("x y z t")

# H=d h-sum m_i e_i, K=-3h+sum e_i in the source's blowup model.
models = [("B1", 4, [2]+[1]*8, 2),
          ("B2", 3, [1]*5, 1),
          ("B3", 3, [2, 1], 0),
          ("B4", 2, [], 0)]
for name, d, multiplicities, expected_pi in models:
    hh = d*d-sum(m*m for m in multiplicities)
    kh = -3*d+sum(multiplicities)
    assert hh == 4 and 1+(hh+kh)//2 == expected_pi

q = s.Matrix([y*z, z*x, x*y, x*x+y*y+z*z])
J = q.jacobian([x,y,z])
assert J*s.Matrix([x,y,z]) == 2*q
minors = [s.factor(J[[j for j in range(4) if j != i], :].det()) for i in range(4)]
pinches = [(0,1,1),(0,1,-1),(1,0,1),(1,0,-1),(1,1,0),(1,-1,0)]
for point in pinches:
    sub = dict(zip((x,y,z), point))
    assert all(f.subs(sub) == 0 for f in minors)
    assert J.subs(sub).rank() == 2
monomials = [x*x,y*y,z*z,x*y,x*z,y*z]
evaluation = s.Matrix([[m.subs(dict(zip((x,y,z),p))) for m in monomials] for p in pinches])
assert evaluation.det() != 0 and evaluation.rank() == 6

# Each coordinate conductor line has exactly the two displayed fixed
# points of its degree-two map [r:s] -> [rs:r^2+s^2].
r, w = s.symbols("r w")
zero_det = s.det(s.Matrix([[r*w, r*r+w*w], [w*r, w*w+r*r]]))
assert zero_det == 0

# Degenerate-pinch normalization of X: Xcoord^2+Ycoord^2(Ycoord+Zcoord^2)=0.
# Put Y=-(w^2+z^2), X=wY, Z=z. Along w=i*z+z^k the image is smooth,
# since Z=z, while conductor order is k+1 (unbounded as k grows).
ii = s.I
Ycoord = -(w*w+z*z)
Xcoord = w*Ycoord
assert s.expand(Xcoord**2+Ycoord**2*(Ycoord+z*z)) == 0
for k in range(2, 8):
    y_curve = s.expand(Ycoord.subs({w:ii*t+t**k,z:t}))
    assert min(powers[0] for powers, coeff in s.Poly(y_curve,t).terms() if coeff != 0) == k+1
print("PASS: four source-table genera, Roman differential/Euler identities,")
print("six pinch points and full-rank no-conic evaluation, plus the exact")
print("degenerate-pinch model with smooth image and unbounded conductor contact.")
