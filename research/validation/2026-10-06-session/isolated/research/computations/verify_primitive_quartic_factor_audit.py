#!/usr/bin/env python3
"""Independent quadratic-cocycle and quartic-factor audit for e=2 on C0.

Uses the persisted universal lift list, verifies its ambient first symbols,
and reconstructs contact from ordinary polynomial Taylor expansion. The
quadratic cocycle is recomputed from the ambient transition without using
the universal Laurent-jet implementation. No sample ranks are extrapolated.
"""
import json
from pathlib import Path
import sympy as sp

BASE = Path(__file__).resolve().parents[1]
data = json.loads((BASE / "scratch/primitive47universal/quartic_contact.json").read_text())
a0, a1, a2, b0, b1, b2, z, w, u, v, eps = sp.symbols("a0 a1 a2 b0 b1 b2 z w u v eps")
params = {str(s): s for s in (a0, a1, a2, b0, b1, b2)}
A = a0 + a1*z + a2*z**2
B = b0 + b1*z + b2*z**2
Av = a2 + a1*w + a0*w**2
Bv = b2 + b1*w + b0*w**2
W1 = -z**-5*A - sp.Rational(1, 2)*z**-4*B
up2 = -sp.Rational(5, 2)*z**-11*A**2 - 3*z**-10*A*B - sp.Rational(3, 8)*z**-9*B**2
vp2 = 3*z**-12*A**2 - z**-11*A*B - sp.Rational(9, 4)*z**-10*B**2
h2_direct = sp.expand(z**9 * (
    Bv.subs(w, 1/z)*up2 - Av.subs(w, 1/z)*vp2
    + (sp.diff(Bv, w).subs(w, 1/z)*A
       - sp.diff(Av, w).subs(w, 1/z)*B)*z**-7*W1))
wronskian = sp.diff(A, z)*B - A*sp.diff(B, z)
h2_formula = sp.expand(-(2*A+z*B)*(12*A**2+3*z**2*B**2+4*z**2*wronskian)/(8*z**5))
assert sp.expand(h2_direct-h2_formula) == 0

restriction = {b0: -2*a1, b1: -2*a2}
A = sp.expand(A.subs(restriction))
B = sp.expand(B.subs(restriction))
h2 = sp.expand(h2_direct.subs(restriction))
gamma = sum(term for term in sp.Add.make_args(h2)
            if term.as_powers_dict().get(z, 0) >= 0)
q0 = 2*a0+b2*z**3
assert sp.expand(2*A+z*B-q0) == 0

exponents = [tuple(es) for es in data["monomials"]]
lifts = [[sp.sympify(c, locals=params) for c in cs] for cs in data["lifts"]]
chart = (1, z, z**3+v, z**4+u+sp.Rational(3, 2)*z*v)
monomials = [sp.expand(sp.prod(xi**e for xi, e in zip(chart, es))) for es in exponents]
# Independently verify the entire ambient quartic first-symbol image.
constants = sp.Matrix([[sp.Poly(f.subs({u: 0, v: 0}), z).nth(d)
                        for f in monomials] for d in range(17)])
ideal_basis = sp.Matrix.hstack(*constants.nullspace())
assert constants.rank() == 17 and ideal_basis.cols == 18
normal = sp.Matrix([[sp.Poly(sp.diff(f, variable).subs({u: 0, v: 0}), z).nth(d)
                     for f in monomials]
                    for variable in (u, v) for d in range(14)]) * ideal_basis
assert all(c == 0 for c in normal[10:14, :])
assert all(c == 0 for c in normal[24:28, :])
symbol = normal.extract(list(range(10))+list(range(14, 24)), list(range(18)))
assert symbol.rank() == 17
assert all(c == 0 for c in symbol[1, :]-2*symbol[12, :])
assert all(c == 0 for c in symbol[4, :]-2*symbol[15, :])
assert all(c == 0 for c in symbol[7, :]-2*symbol[18, :])
# Rank seventeen in the twenty-dimensional target proves those three
# independent equations are exhaustive; the kernel has dimension one.
F = [sp.expand(sum(c*m for c, m in zip(cs, monomials))) for cs in lifts]
hdegrees = data["hdegrees"]
expected_h = [z**d for d in hdegrees] + [sp.Integer(0)]
M_rows = []
contact = []
for f, h in zip(F, expected_h):
    straight = sp.Poly(sp.expand(f.subs({u: A*eps, v: B*eps})), eps)
    assert straight.nth(0) == 0
    assert sp.expand(sp.diff(f, u).subs({u: 0, v: 0}) - h*B) == 0
    assert sp.expand(sp.diff(f, v).subs({u: 0, v: 0}) + h*A) == 0
    assert straight.nth(1) == 0
    contact.append(sp.expand(straight.nth(2)-h*gamma))
degrees = sorted({e[0] for c in contact for e in sp.Poly(c, z).monoms()})
M = sp.Matrix([[sp.Poly(c, z).nth(d) for c in contact] for d in degrees])
persisted_M = sp.Matrix([[sp.sympify(c, locals=params) for c in row]
                        for row in data["matrix2"]])
assert M == persisted_M
assert M[0:3, 4:7].det() == -a0**8
assert sp.expand(M.extract([4, 5, 6], [0, 1, 6]).det()+b2**8/sp.Integer(256)) == 0
# The global upper-rank statement has no specialization/generic-rank gap.
assert M.rank() == 3

x, y, Z, W = sp.symbols("x y Z W")
Q = x*W-y*Z
T = sp.expand(Q*(2*a0*a1*x+2*a0*a2*y+a1*b2*Z+a2*b2*W)
              +a0**2*(x**2*Z-y**3)
              +a0*b2*(x*Z**2-y**2*W)
              -b2**2*(y*W**2-Z**3)/4)
Tchart = sp.expand(T.subs({x: 1, y: z, Z: z**3+v,
                          W: z**4+u+sp.Rational(3, 2)*z*v}))
assert Tchart.subs({u: 0, v: 0}) == 0
assert sp.expand(sp.diff(Tchart, u).subs({u: 0, v: 0})+q0*B/2) == 0
assert sp.expand(sp.diff(Tchart, v).subs({u: 0, v: 0})-q0*A/2) == 0
straight_T = sp.Poly(sp.expand(Tchart.subs({u: A*eps, v: B*eps})), eps)
assert sp.expand(straight_T.nth(2)+q0*gamma/2) == 0

ambient_lifts = [sp.Poly(sum(c*sp.prod(t**e for t, e in zip((x, y, Z, W), es))
                             for c, es in zip(cs, exponents)), x, y, Z, W)
                 for cs in lifts]
q2 = sp.Poly(Q**2, x, y, Z, W)
q2_pivot = (2, 0, 0, 2)
degrees_index = {d: i for i, d in enumerate(hdegrees)}
kernel_vectors = []
for linear, power in zip((x, y, Z, W), (0, 1, 3, 4)):
    h = sp.Poly(sp.expand(-q0*z**power/2), z)
    vec = [h.nth(d) for d in hdegrees] + [sp.Integer(0)]
    diff = sp.Poly(T*linear, x, y, Z, W)-sum(c*f for c, f in zip(vec, ambient_lifts))
    vec[-1] = diff.coeff_monomial(q2_pivot)
    assert diff-vec[-1]*q2 == 0
    assert M*sp.Matrix(vec) == sp.zeros(M.rows, 1)
    kernel_vectors.append(vec)
kernel = sp.Matrix.hstack(*(sp.Matrix(c) for c in kernel_vectors))
assert kernel.rank() == 4
# The same four products also satisfy the independently stored cubic layer.
M3 = sp.Matrix([[sp.sympify(c, locals=params) for c in row]
               for row in data["matrix3"]])
assert all(sp.expand(c) == 0 for c in M3*kernel)

D = a0**2*b2**2+6*a0*a1*a2*b2+4*a0*a2**3-2*a1**3*b2
assert sp.expand(D.subs({a0: 0, b2: 0})) == 0
# Nonzero T is visible at each point of the resultant-open locus.
assert sp.Poly(T, x, y, Z, W).coeff_monomial(y**3) == -a0**2
assert sp.Poly(T, x, y, Z, W).coeff_monomial(Z**3) == b2**2/4
print("INDEPENDENT QUADRATIC COCYCLE AND UNIVERSAL QUARTIC FACTOR AUDIT PASSED")
