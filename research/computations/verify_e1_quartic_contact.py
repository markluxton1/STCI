#!/usr/bin/env python3
"""Exact quartic contact calculation on the e=1 primitive-triple locus.

Fixed curve C0=[s^4:s^3t:st^3:t^4], chart
[1,z,z^3+v,z^4+u+3*z*v/2].
For a linear quotient A,B defining L=O(-6), this script constructs the
entire quartic ideal, imposes first-symbol proportionality to (B,-A),
and then the canonical triple correction from the BF Cech cocycle.
It computes exact ranks after imposing each component of the e=1
triple-obstruction locus.
"""
import sympy as sp
from itertools import combinations

a0,a1,b0,b1,z,u,v,eps=sp.symbols("a0 a1 b0 b1 z u v eps")
x,y,Z,W=sp.symbols("x y Z W")
A=a0+a1*z
B=b0+b1*z
D=a0*b1-a1*b0
wr=sp.diff(A,z)*B-A*sp.diff(B,z)
h2=sp.expand(-(2*A+z*B)*(12*A**2+3*z**2*B**2+4*z**2*wr)/(8*z**5))
gamma=sp.expand(sum(t for t in sp.Add.make_args(h2) if t.as_powers_dict().get(z,0)>=0))

# all degree-four ambient monomials
exps=[]
for i in range(5):
 for j in range(5-i):
  for k in range(5-i-j):
   l=4-i-j-k
   exps.append((i,j,k,l))
chart=(1,z,z**3+v,z**4+u+sp.Rational(3,2)*z*v)
mons=[sp.expand(sp.prod(q**e for q,e in zip(chart,E))) for E in exps]
const=sp.Matrix([[sp.Poly(f.subs({u:0,v:0}),z).nth(d) for f in mons] for d in range(17)])
I=sp.Matrix.hstack(*const.nullspace())
assert I.cols==18
Fs=[sp.expand(sum(I[j,i]*mons[j] for j in range(35))) for i in range(18)]

# A quartic through the double has first normal symbol h*(B,-A).
# Solve simultaneously for its 18 ideal coefficients and h in H0(O(8)).
cs=sp.symbols("c0:18")
hs=sp.symbols("h0:9")
F=sum(c*f for c,f in zip(cs,Fs))
du=sp.expand(sp.diff(F,u).subs({u:0,v:0}))
dv=sp.expand(sp.diff(F,v).subs({u:0,v:0}))
h=sum(hs[i]*z**i for i in range(9))
eqpoly=[sp.expand(du-h*B),sp.expand(dv+h*A)]
eqs=[]
for p in eqpoly:
 P=sp.Poly(p,z)
 eqs += [P.nth(d) for d in range(14)]
vars=list(cs)+list(hs)
Mat,_=sp.linear_eq_to_matrix(eqs,vars)
ns=Mat.nullspace()
# expected dim: K_R 6 plus Q^2 = 7
assert len(ns)==7
lifts=[]
hlist=[]
for q in ns:
 coeff=q[:18,0]
 lifts.append(sp.expand(sum(coeff[i]*Fs[i] for i in range(18))))
 hlist.append(sp.expand(sum(q[18+i,0]*z**i for i in range(9))))

contact=[]
for f,hh in zip(lifts,hlist):
 straight=sp.Poly(sp.expand(f.subs({u:A*eps,v:B*eps})),eps)
 assert sp.expand(straight.nth(1))==0
 contact.append(sp.expand(straight.nth(2)-hh*gamma))
degrees=sorted({m[0] for c in contact for m in sp.Poly(c,z).monoms()})
M=sp.Matrix([[sp.Poly(c,z).nth(d) for c in contact] for d in degrees])

# main triple component: b0=-2a1, a0*b1=-8a1^2.
# Work on a0 != 0 and substitute b1.
Mm=sp.simplify(M.subs({b0:-2*a1,b1:-8*a1**2/a0}))
# Generic exact rank over QQ(a0,a1)
rm=Mm.rank()
print("precontact dimension",len(ns),"contact rows",M.rows)
print("main rank",rm,"kernel",7-rm)
# boundary directions a0=b1=0, b0=r*a1
r=sp.symbols("r")
Mb=sp.simplify(M.subs({a0:0,b1:0,b0:r*a1}))
for rv in [-2,(-2+4*sp.sqrt(2)*sp.I)/3,(-2-4*sp.sqrt(2)*sp.I)/3]:
 Mr=sp.simplify(Mb.subs(r,rv))
 print("boundary",rv,"rank",Mr.rank(),"kernel",7-Mr.rank())

# Persist matrices in a compact inspectable form.
print("main nonzero maximal minor search")
for rows in combinations(range(Mm.rows),rm):
 for cols in combinations(range(7),rm):
  det=sp.factor(Mm.extract(rows,cols).det())
  if det!=0:
   print(rows,cols,det)
   raise SystemExit
