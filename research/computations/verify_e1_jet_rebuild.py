#!/usr/bin/env python3
"""Rebuild certificate for the e=1 primitive-triple quartic carrier lane.

Base geometry:
 C=[s^4:s^3t:st^3:t^4],
 affine chart [1,z,z^3+v,z^4+u+3*z*v/2].
On the main BF triple component normalize
 A=1+t*z, B=-2*t-8*t^2*z, t != 0.

The script reconstructs I_C(4), I_C2(4), the BF quadratic correction,
the second-contact matrix, its kernel, and the actual two ambient
quartics spanning I_C3(4). No random specialization is used.
"""
import sympy as sp

z,u,v,e,t=sp.symbols("z u v e t", nonzero=True)
x,y,Z,W=sp.symbols("x y Z W")
A=1+t*z
B=-2*t-8*t**2*z
Delta=-6*t**2
assert Delta != 0

# BF double-to-triple cocycle and chart correction.
wr=sp.diff(A,z)*B-A*sp.diff(B,z)
h2=sp.expand(-(2*A+z*B)*(12*A**2+3*z**2*B**2+4*z**2*wr)/(8*z**5))
gamma=sp.expand(sum(q for q in sp.Add.make_args(h2)
                    if q.as_powers_dict().get(z,0)>=0))

# Degree-four ambient monomials.
exps=[]
for i in range(5):
 for j in range(5-i):
  for k in range(5-i-j):
   exps.append((i,j,k,4-i-j-k))
ambient=[x**i*y**j*Z**k*W**l for i,j,k,l in exps]
chart=(1,z,z**3+v,z**4+u+sp.Rational(3,2)*z*v)
mons=[sp.expand(sp.prod(q**n for q,n in zip(chart,E))) for E in exps]

# I_C(4).
const=sp.Matrix([[sp.Poly(f.subs({u:0,v:0}),z).nth(d)
                  for f in mons] for d in range(17)])
N=sp.Matrix.hstack(*const.nullspace())
assert N.cols==18
quartics=[sp.expand(sum(N[j,i]*ambient[j] for j in range(35)))
          for i in range(18)]
qcharts=[sp.expand(sum(N[j,i]*mons[j] for j in range(35)))
         for i in range(18)]

# I_C2(4): normal symbol h(B,-A), h degree <=8.
cs=sp.symbols("c0:18")
hs=sp.symbols("h0:9")
Fc=sum(c*f for c,f in zip(cs,qcharts))
du=sp.expand(sp.diff(Fc,u).subs({u:0,v:0}))
dv=sp.expand(sp.diff(Fc,v).subs({u:0,v:0}))
h=sum(hs[i]*z**i for i in range(9))
eq=[]
for p in (sp.expand(du-h*B),sp.expand(dv+h*A)):
 P=sp.Poly(p,z)
 eq.extend(P.nth(d) for d in range(14))
M2,_=sp.linear_eq_to_matrix(eq,list(cs)+list(hs))
basis2=M2.nullspace()
assert len(basis2)==7

ambient2=[]
hs2=[]
contact=[]
for q in basis2:
 Famb=sp.expand(sum(q[i,0]*quartics[i] for i in range(18)))
 Fch=sp.expand(sum(q[i,0]*qcharts[i] for i in range(18)))
 hh=sp.expand(sum(q[18+i,0]*z**i for i in range(9)))
 straight=sp.Poly(sp.expand(Fch.subs({u:A*e,v:B*e})),e)
 assert sp.expand(straight.nth(1))==0
 ambient2.append(Famb)
 hs2.append(hh)
 contact.append(sp.expand(straight.nth(2)-hh*gamma))

degrees=sorted({m[0] for c in contact for m in sp.Poly(c,z).monoms()})
M3=sp.Matrix([[sp.Poly(c,z).nth(d) for c in contact] for d in degrees])
assert M3.rank()==5
K=M3.nullspace()
assert len(K)==2

F3=[]
for k in K:
 f=sp.factor(sum(k[i,0]*ambient2[i] for i in range(7)))
 F3.append(f)
assert all(sp.Poly(f,x,y,Z,W).total_degree()==4 for f in F3)

# Fixed-factor test over QQ(t): gcd must be one unless a common surface factor exists.
g=sp.factor(sp.gcd(sp.Poly(F3[0],x,y,Z,W,domain=sp.QQ.frac_field(t)),
                  sp.Poly(F3[1],x,y,Z,W,domain=sp.QQ.frac_field(t))).as_expr())
print("I_C2(4) dimension = 7")
print("second-contact rank = 5")
print("I_C3(4) dimension = 2")
print("gcd(F0,F1) =",g)
for i,f in enumerate(F3):
 print("F%d ="%i,sp.factor(f))
