#!/usr/bin/env python3
"""Universal second-frame reduction for MF6 e=0,(d2,d3)=(4,5).

The elimination uses the full quartic incidence, not its generic kernel.
The saved generic kernel is only an additional direct chart check.
"""
import json
from pathlib import Path
import sympy as s
import verify_mf6_type3 as a

z = a.z
w, y, f, g, fp = s.symbols("w y f g fp")
A, B, m, yp, mp = s.symbols("A B m yp mp")


def cut(expr):
    expr = s.expand(expr)
    return s.Add(*[expr.coeff(y, i) * y**i for i in range(4)])


# Compute the nonlinear transition with the actual new support parameter W.
c = s.Rational(3, 2)*z - 1
Dinv = z**-4*(1-c*y/z**4+(c*c/z**8-f/z**4)*y*y
               +(-g/z**4+2*c*f/z**8-c**3/z**12)*y**3)
W = cut((z**3+y)*Dinv)
ap = cut(z*Dinv-cut(W**3))
bp = cut(Dinv-cut(W**4))
Yprime = cut(-3*cut(W*ap)+2*bp)
Mprime = cut(ap/2+Yprime)
assert Mprime.coeff(y, 1) == 0
b1, b2, c1 = Yprime.coeff(y, 1), Yprime.coeff(y, 2), W.coeff(y, 1)
assert b1 == z**-7
finf = s.factor(Mprime.coeff(y, 2)/b1**2)
p2 = (-3*z**5+6*z**4-12*z**3+24*z**2)/8
assert s.expand(finf-z**7*f-p2) == 0
finf_dz = s.diff(finf, z)+s.diff(finf, f)*fp
ginf = s.factor((Mprime.coeff(y, 3)-2*finf*b1*b2
                 +z*z*finf_dz*c1*b1*b1)/b1**3)
C = -2*z**11+9*z**10-12*z**9
E = -z**12/2+z**11
P = 7*z**9/16-25*z**8/8+9*z**7-14*z**6+19*z**5-18*z**4
assert s.expand(ginf-z**14*g-C*f-E*fp-P) == 0

delta = A*(z*z+2*z)+B*(z**3-4*z)+z**4+8*z+16
R = A+B*(z-2)+z*z-2*z+4
delta_inf = s.expand(w**4*delta.subs(z, 1/w))
gamma_inf = 6*A*w+6*B*(1-2*w)+48*w*w
f2 = s.Rational(3, 8)*R/delta
assert s.cancel((z**7*f2+p2)-gamma_inf.subs(w, 1/z)/delta_inf.subs(w, 1/z)) == 0

# J depends only on the specified triple. For every incidence quartic,
# w^9 T_inf = w^8 T(1/w)-S_inf Jhat.
J = s.expand(3*R*delta*C+3*(s.diff(R,z)*delta-R*s.diff(delta,z))*E
             +8*delta*delta*P)
Jpoly = s.Poly(J,z)
assert Jpoly.degree() == 17
assert Jpoly.nth(17) == s.Rational(1,2)
Jhat = s.expand(w**17*J.subs(z,1/w))
j = [s.expand(Jhat).coeff(w,i) for i in range(9)]

# All incidence quartics have nonzero first-normal coefficient h:
# the first-normal kernel of the complete mixed quartic space is q^2,
# whose quadratic restriction to m=0 is nonzero.
U,V = a.U,a.V
hmat = s.Matrix([[jet.coeff_monomial(U).coeff(a.z,i) for jet in a.jets]
                 for i in range(10)])
assert hmat.rank() == 7
hv = hmat.nullspace()[0]
Fh = s.expand(sum(v*F for v,F in zip(hv,a.mixed)))
q = a.a.q
ratio = s.cancel(Fh/q**2)
assert not ratio.free_symbols and ratio != 0
hjet = s.expand(Fh.subs(a.a.sub))
Qh = s.expand(hjet.subs(U,-V)).coeff(V,2)
assert Qh != 0

# Direct homogeneous chart check using a known incidence vector. This does
# not classify special nullspaces. Universal validity follows from the
# formal-root transition verified above.
data = json.loads((Path(__file__).parents[1]/"scratch"/"mf6_type4_incidence.json").read_text())
vector = [s.sympify(v) for v in data["kernel"]]
jet = s.expand(sum(v*jet.as_expr() for v,jet in zip(vector,a.jets)))
h = jet.coeff(U,1).coeff(V,0)
Q = s.expand(jet.subs(U,-V)).coeff(V,2)
assert s.expand(delta*Q+s.Rational(3,8)*R*h) == 0
S = s.cancel(h/delta)
assert s.denom(S) == 1
moving = s.expand(jet.subs({U:m-y,V:y}))
Em = moving.coeff(m,1).coeff(y,1)
Km = moving.coeff(m,0).coeff(y,3)
T = s.expand(3*R*Em+8*delta*Km)
subinf = {a.a.x3:1,a.a.x2:w,a.a.x1:w**3+2*(mp-yp),
          a.a.x0:w**4+yp/2+3*w*(mp-yp)}
infjets = [s.expand(F.subs(subinf)) for F in a.mixed]
h_inf = s.expand(sum(v*jet.coeff(mp,1).coeff(yp,0)
                      for v,jet in zip(vector,infjets)))
E_inf = s.expand(sum(v*jet.coeff(mp,1).coeff(yp,1)
                      for v,jet in zip(vector,infjets)))
K_inf = s.expand(sum(v*jet.coeff(mp,0).coeff(yp,3)
                      for v,jet in zip(vector,infjets)))
S_inf = s.expand(w**5*S.subs(z,1/w))
assert s.expand(h_inf-delta_inf*S_inf) == 0
T_inf = s.expand(8*gamma_inf*E_inf+8*delta_inf*K_inf)
assert s.expand(w**9*T_inf-w**8*T.subs(z,1/w)+S_inf*Jhat) == 0

# If total excess <=1, a nonzero section L=l0+l1*z of O(1) annihilates
# the cubic class on the zero divisor of S. From the transition, T has
# degree deg(S)+3 even when S loses affine degree. Thus LT=SQ has deg Q<=4.
# The second-chart condition is equivalent to
# w^4 Q(1/w)-(l0*w+l1)Jhat divisible by w^9.
# Coefficients 5,...,8 therefore require this four-by-two matrix to have
# rank at most one. No generic quartic vector enters this reduction.
boundary = s.Matrix([[j[i-1],j[i]] for i in range(5,9)])
minors = [s.expand(boundary[[i,k],:].det()) for i in range(4)
          for k in range(i+1,4)]
gb = s.groebner(minors,A,B,order="lex",domain=s.QQ)
expected = [(A-12)**2,(A-12)*(B-4),(B-4)**2]
assert [s.expand(p.as_expr()) for p in gb.polys] == [s.expand(p) for p in expected]
assert boundary.subs({A:12,B:4}) == s.zeros(4,2)
print("PASS: actual nonlinear chart transformation through cubic order")
print("PASS: universal w^9*T_inf=w^8*T(1/w)-S_inf*Jhat; Jhat(0)=1/2")
print("PASS: every nonzero incidence quartic has S != 0")
print("PASS: independent direct generic quartic chart expansion")
print("PASS: annihilation boundary minors have ideal ((A-12)^2,(A-12)(B-4),(B-4)^2)")
print("RESULT: every e=0 type(4,5) candidate forces triple parameters (A,B)=(12,4)")
