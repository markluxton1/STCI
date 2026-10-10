#!/usr/bin/env python3
"""Exact identities for the displayed ribbon [2,2] pencil only."""
import json
import sympy as s

x,y,v,w,z,U,V=s.symbols('x y v w z U V')
E=[x*z-y*y,x*v-y*z,x*w-y*v,y*v-z*z,y*w-z*v,z*w-v*v]
Q1=2*E[1]+E[3]-E[4]
Q2=E[0]-2*E[1]-E[2]/2+E[4]+E[5]/4
A=-2*y+v; R1=2*x*v+y*v-y*w
L=x+2*y-v+w/4
R=-y*y-2*x*v-(x*w-y*v)/2+y*w-v*v/4
ell=2*y-v; q=-2*x*v+y*w
assert s.expand(Q1+z*z-A*z-R1)==0
assert s.expand(Q2-L*z-R)==0
assert s.expand(E[3]-Q1-ell*z-q)==0
lift={x:U**4,y:U**3*V,v:U*V**3,w:V**4,z:U**2*V**2}
assert all(s.expand(e.subs(lift))==0 for e in E)
assert s.expand(L.subs(lift)-(U**2+U*V-V**2/2)**2)==0
Rc=s.expand(R.subs(x,-2*y+v-w/4))
det=(s.hessian(Rc,(y,v,w))/2).det()
assert det==s.Rational(243,128)
G=s.groebner([Rc],y,v,w,order='lex')
T=2*q+A*ell
N=q*q+A*q*ell-R1*ell*ell
T2=G.reduce(s.expand(T.subs(x,-2*y+v-w/4)**2))[1]
Nr=G.reduce(s.expand(N.subs(x,-2*y+v-w/4)))[1]
pt=s.Poly(T2,y,v,w); pn=s.Poly(Nr,y,v,w)
tc=[pt.coeff_monomial(y*v**3),pt.coeff_monomial(y*v**2*w)]
nc=[pn.coeff_monomial(y*v**3),pn.coeff_monomial(y*v**2*w)]
minor=tc[0]*nc[1]-tc[1]*nc[0]
assert tc==[114,336] and nc==[1,4] and minor==120
print(json.dumps({'status':'PASS','conic_determinant':str(det),
 'trace_squared_coefficients':list(map(int,tc)),
 'norm_coefficients':list(map(int,nc)),'minor':int(minor),
 'scope':'displayed pencil only; no complete repeated-root coverage'}))
