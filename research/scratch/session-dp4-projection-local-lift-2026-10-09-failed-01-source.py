#!/usr/bin/env python3
"""Literal certificates for the four-A1 dP4 projection containing C0.

The paired proof supplies normality, finite birationality and the
all-mate singleton-fiber obstruction. These are not inferred solely
from a successful symbolic run.
"""
import json
import sympy as sp

r, p, z, q, t, u, v = sp.symbols("r p z q t u v")
a = p+4*z+4*q
b = -r-3*p-2*z
c = -p-3*z-2*q
d = -z-3*q-2*t
e = p+2*z+q
M = sp.Matrix([[0,1,4,4,0],[-1,-3,-2,0,0],[0,-1,-3,-2,0],
               [0,0,-1,-3,-2],[0,1,2,1,0]])
assert M.det() == 2
Q1 = sp.expand(a*e-c**2)
Q2 = sp.expand(b*d-c**2)
L = r-3*p-6*q+4*t
D = -p**2-2*p*q+6*p*t-4*q**2+3*q*r+2*r*t
F = sp.expand(D**2-p*q*L**2)
assert sp.expand(Q1-(p*q-z**2)) == 0
assert sp.expand(Q2-7*Q1-D-L*z) == 0
assert sp.expand(sp.resultant(Q1,Q2,z)-F) == 0
assert sp.Poly(F,r,p,q,t).is_homogeneous
assert sp.Poly(F,r,p,q,t).total_degree() == 4
assert Q1.subs({r:0,p:0,z:1,q:0,t:0}) == -1
assert Q2.subs({r:0,p:0,z:1,q:0,t:0}) == -7

param = {r:u**4,p:u**3*v,z:u**2*v**2,q:u*v**3,t:v**4}
for equation in (Q1,Q2,F):
    assert sp.expand(equation.subs(param)) == 0
Lc = (u**2-4*u*v+2*v**2)*(u**2+u*v+2*v**2)
assert sp.expand(L.subs(param)-Lc) == 0
assert sp.expand(D.subs(param)+u**2*v**2*Lc) == 0
f1 = u**2-4*u+2
f2 = u**2+u+2
assert sp.discriminant(f1,u) == 8
assert sp.discriminant(f2,u) == -7
assert sp.resultant(f1,f2,u) == 50
assert Lc.subs({u:0,v:1}) == 4
assert Lc.subs({u:1,v:0}) == 1

# Complete quotient-module relations of B over k[r,p,q,t].
assert sp.expand(z*(D+L*z)-(D*z+L*p*q)-L*(z**2-p*q)) == 0
assert sp.expand(D*(D+L*z)-L*(D*z+L*p*q)-F) == 0
Gamma = sp.expand(D.subs(r,3*p+6*q-4*t))
assert Gamma == -p**2+7*p*q+14*q**2+12*p*t-8*t**2
assert (sp.hessian(Gamma,(p,q,t))/2).det() == -294

L_at_vertices = []
for vertex in (0,1,3,4):
    point = M.inv()[:,vertex]
    L_at_vertices.append(L.subs(dict(zip((r,p,z,q,t),point))))
assert L_at_vertices == [-14,-1,-2,-28]

# An actual quadric with Weil divisor 2 times the lifted RNC.
Q = sp.expand(a*b+a*d+b*e+4*d*e+2*a*c+2*b*c+6*c**2+4*c*d+4*c*e)
assert Q == -6*p*q-2*p*t+p*z-q*r+2*q*z+6*z**2
assert sp.expand(Q.subs(param)) == 0
s0,s1,h0,h1 = sp.symbols("s0 s1 h0 h1")
cover = {
    sp.Symbol("a"):s0**2*h0**2,
    sp.Symbol("b"):s0**2*h1**2,
    sp.Symbol("c"):s0*s1*h0*h1,
    sp.Symbol("d"):s1**2*h0**2,
    sp.Symbol("e"):s1**2*h1**2,
}
aa,bb,cc,dd,ee = (sp.Symbol(w) for w in ("a","b","c","d","e"))
Qabc = aa*bb+aa*dd+bb*ee+4*dd*ee+2*aa*cc+2*bb*cc+6*cc**2+4*cc*dd+4*cc*ee
f = s0**2*h0*h1+s0*s1*h0**2+s0*s1*h1**2+2*s1**2*h0*h1
assert sp.expand(Qabc.subs(cover)-f**2) == 0
assert sp.factor(sp.discriminant(f,h0)) == h1**2*(s0**4+4*s1**4)

# At all four C0-conductor crossings the other lift has Q != 0.
# On S, Q=(p+2q)z-2pt-qr. Switching z to -z sends its value on
# the RNC to -2(p+2q)u^2v^2; its coefficient never vanishes at Lc=0.
assert sp.resultant(f1*f2,u**2+2,u) == 64
other_Q = sp.factor(Q.subs({r:u**4,p:u**3*v,z:-u**2*v**2,q:u*v**3,t:v**4}))
assert other_Q == -2*u**3*v**3*(u**2+2*v**2)

print(json.dumps({
    "status":"PASS",
    "scope":"four-A1 dP4 projection containing fixed C0; no projected mate is asserted",
    "coordinate_change_determinant":2,
    "carrier_factored_expression":"D^2-p*q*L^2",
    "L":str(L),"D":str(D),
    "carrier_degree":4,
    "birational_inverse":"z=-D/L",
    "conductor_ideal":["L","D"],
    "conductor_conic":str(Gamma),
    "conductor_conic_matrix_determinant":-294,
    "conductor_on_C0":str(Lc),
    "conductor_crossings_distinct":4,
    "L_at_A1_vertices":[str(x) for x in L_at_vertices],
    "quadric_divisor_twice_lifted_curve":str(Q),
    "quadric_on_other_lift":str(other_Q),
    "interpretation":"The proof shows a finite birational singular normalization and rules out every mate for this specific projected carrier by its nonsingleton fibers over C0."
},indent=2))
