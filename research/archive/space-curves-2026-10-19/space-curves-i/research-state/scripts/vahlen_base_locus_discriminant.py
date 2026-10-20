#!/usr/bin/env python3
"""Exact base-locus discriminant calculations for the Vahlen cubic P3.

This complements, rather than repeats, the universal elimination recorded in
ARTIFACT-20260821-022.  All cubics in I_C(3) contain the forced line G.  The
script computes two explicit incidence mechanisms for singular members:

* singularity on G, from the resultant of the two normal quadratic forms; and
* singularity on C, from the kernel of the normal-gradient evaluation map.

It uses SymPy plus the exact cubic basis exposed by vahlen_quintic_exact.py.
"""
import runpy
import sympy as sp

state = runpy.run_path("research-state/scripts/vahlen_quintic_exact.py")
K, ms = state["K"], state["ms"]
u = sp.symbols("U0:4")
a = sp.symbols("a0:4")
s, t, r = sp.symbols("s t r")

def cubic(v):
    return sp.expand(sum(c * sp.prod(u[j] ** m[j] for j in range(4))
                         for c, m in zip(v, ms)))

basis = [cubic(v) for v in K]
F = sp.expand(sum(a[i] * basis[i] for i in range(4)))
# Derive the image line anew, directly from rational points of the residual
# conic q=3yz-5xz-5xy+7x^2.  This intentionally avoids the formatted line
# output in the older script, whose monomial display order is unsuitable here.
V = state["V"]
x, y, z = sp.symbols("x y z")
def eval_section(section, point):
    return sum(coef * point[0]**m[0] * point[1]**m[1] * point[2]**m[2]
               for m, coef in section.items())
points = []
for yy in [0, 4, 5, 6]:
    zz = sp.Rational(5*yy-7, 3*yy-5)
    points.append((sp.Integer(1), sp.Integer(yy), zz))
images = [tuple(eval_section(section, p) for section in V) for p in points]
line_kernel = sp.Matrix(images).nullspace()
assert len(line_kernel) == 2
l1 = sp.expand(sum(line_kernel[0][i] * u[i] for i in range(4)))
l2 = sp.expand(sum(line_kernel[1][i] * u[i] for i in range(4)))
print("directly reconstructed line equations for G:")
print(l1)
print(l2)

# Solve the two line equations to parametrize G, then verify every cubic basis
# element vanishes identically on it.
sol_line = sp.solve([l1, l2], [u[0], u[1]], dict=True)[0]
gsub = {u[0]: sol_line[u[0]].subs({u[2]: s, u[3]: t}),
        u[1]: sol_line[u[1]].subs({u[2]: s, u[3]: t}), u[2]: s, u[3]: t}
assert all(sp.expand(B.subs(gsub)) == 0 for B in basis)

# Solve F=l1*Q1+l2*Q2 with Q1,Q2 quadrics.  The representation is not unique;
# its restrictions to G are unique, which is all the resultant requires.
qmons = [u[i]*u[j] for i in range(4) for j in range(i, 4)]
x = sp.symbols("x0:20")
Q1 = sum(x[i] * qmons[i] for i in range(10))
Q2 = sum(x[10+i] * qmons[i] for i in range(10))
eq = sp.Poly(sp.expand(F-l1*Q1-l2*Q2), *u)
sol = sp.linsolve([z for _, z in eq.terms()], x)
v = list(next(iter(sol)))
Q1 = sp.expand(Q1.subs(dict(zip(x, v))))
Q2 = sp.expand(Q2.subs(dict(zip(x, v))))

# A homogeneous parametrization of G=V(l1,l2): (U0:U1:U2:U3)
# = (5s+5t : 5t : 3s : 3t).
q1g = sp.factor(Q1.subs(gsub))
q2g = sp.factor(Q2.subs(gsub))
resG = sp.factor(sp.resultant(q1g.subs(t, 1), q2g.subs(t, 1), s))
print("line G singularity resultant (up to nonzero scalar):")
print(resG)
print("degrees in a:", sp.Poly(resG, *a).total_degree())

# Parametrization of C from ARTIFACT-20260821-012.  The gradient of every
# cubic through C annihilates the tangent direction, so its coefficient matrix
# has rank at most two.  A rank-two minor certifies the generic rank is exactly
# two; its 2-dimensional kernel gives the singular cubics at each point.
U = state["U"]
image = [sum(sp.Integer(c)*s**(5-i)*t**i for i, c in enumerate(row)) for row in U]
gcd_CG = sp.factor(sp.gcd(sp.Poly(l1.subs(dict(zip(u, image))), s, t),
                         sp.Poly(l2.subs(dict(zip(u, image))), s, t)).as_expr())
print("scheme-theoretic C-intersection polynomial on G (up to scalar):")
print(gcd_CG)
grad = sp.Matrix([[sp.diff(B, uj).subs(dict(zip(u, image))) for B in basis]
                  for uj in u])
minor = sp.factor(grad.extract([0, 1], [0, 1]).det())
print("a 2x2 normal-gradient minor along C:")
print(minor)
print("rank at (s:t)=(0:1):", grad.subs({s: 0, t: 1}).rank())
print("coefficient kernel at (0:1):")
print([tuple(z) for z in grad.subs({s: 0, t: 1}).nullspace()])
