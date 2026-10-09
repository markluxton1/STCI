#!/usr/bin/env python3
"""Exact local counterexample to scheme-theoretic R subset lifted C."""
import sympy as s

w, z, X, Y, Z, P, Q, R = s.symbols("w z X Y Z P Q R")
image = s.Matrix([-w**3-w*z**2, -w**2-z**2, z])
F = X**2+Y**2*(Y+Z**2)
assert s.expand(F.subs(dict(zip((X,Y,Z),image)))) == 0
J = image.jacobian([w,z])
minors = [J[[i,j],:].det() for i,j in ((0,1),(0,2),(1,2))]
G = s.groebner(minors,w,z)
assert list(G) == [w,z**2]

# C: X=-2Z^3,Y=-2Z^2 has parameter Z. Lift c:w=z.
pulled = [image[0]+2*z**3,image[1]+2*z**2]
assert all(s.expand(f.subs(w,z)) == 0 for f in pulled)
cofactors = [s.cancel(f/(w-z)) for f in pulled]
assert list(s.groebner(cofactors,w,z)) == [w+z,z**2]
assert G.reduce(w-z)[1] == -z

# Pullback of the original hypersurface Jacobian equals conductor times
# differential ramification: J_X B = Y B * (w,z^2).
jacobian = [s.diff(F,t).subs(dict(zip((X,Y,Z),image))) for t in (X,Y,Z)]
cofactor_jacobian = [s.cancel(f/image[1]) for f in jacobian]
assert list(s.groebner(cofactor_jacobian,w,z)) == [w,z**2]

# Explicit analytic/polynomial coordinate identification with T_(2,3,infinity).
# P=X+iYZ,Q=Y,R=2iZ; P^2+Q^3-PQR=F.
assert s.expand((P**2+Q**3-P*Q*R).subs({P:X+s.I*Y*Z,Q:Y,R:2*s.I*Z})-F) == 0
print("PASS: actual differential Fitting ideal (w,z²), full inverse support,")
print("noncontainment of the smooth lift, exact conductor/Jacobian product,")
print("and T_(2,3,infinity) semi-log-canonical normal-form identification.")
