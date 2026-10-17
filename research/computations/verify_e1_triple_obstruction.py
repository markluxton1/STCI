#!/usr/bin/env python3
"""Exact e=1 double-to-triple BF obstruction for C0=[s^4:s^3t:st^3:t^4]."""
import sympy as sp
a0,a1,b0,b1,z,T=sp.symbols("a0 a1 b0 b1 z T")
Delta=a0*b1-a1*b0
c1=-b1*(2*a0*b1+12*a1**2+16*a1*b0+9*b0**2)
c2=-(2*a1+b0)*(8*a0*b1+12*a1**2+4*a1*b0+3*b0**2)
c3=-2*a0*(2*a0*b1+36*a1**2+16*a1*b0+3*b0**2)
F=[sp.expand(c1),sp.expand(c2),sp.expand(c3)]
main={b0:-2*a1,b1:-8*a1**2/a0}
assert all(sp.cancel(f.subs(main))==0 for f in F)
assert sp.cancel(Delta.subs(main))==-6*a1**2
r=sp.symbols("r")
bd={a0:0,b1:0,b0:r*a1}
Fb=[sp.factor(f.subs(bd)) for f in F]
assert Fb[0]==0 and Fb[2]==0
assert sp.factor(Fb[1])==-a1**3*(r+2)*(3*r**2+4*r+12)
G=sp.groebner(F+[T*Delta-1],T,a0,a1,b0,b1,order="lex")
E=[sp.factor(p.as_expr()) for p in G.polys]
needed=[a0*(3*b0**2*T+2),b1*(3*b0**2*T+2),
        a0*(2*a1+b0),b1*(2*a1+b0),
        a0*(a0*b1+2*b0**2),b1*(a0*b1+2*b0**2)]
for q in needed:
 assert any(sp.expand(e-q)==0 or sp.expand(e+q)==0 for e in E)
print("e=1 BF triple locus certified")
