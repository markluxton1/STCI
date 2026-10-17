#!/usr/bin/env python3
"""Exact e=1 double-to-triple BF obstruction for C0=[s^4:s^3t:st^3:t^4].

For L=O(-6), write the quotient N_C^*=O(-7)^2 -> L as
A=a0+a1*z, B=b0+b1*z.  Projective basepoint-freeness is
Delta=a0*b1-a1*b0 != 0.

The moving-coordinate ambient transition gives the quadratic cocycle h2.
Its z^-1,z^-2,z^-3 coefficients represent
H^1(Hom(M,L^2))=H^1(O(-4)).
This verifier checks the closed formulas and the exact resultant-open
decomposition of their common zero locus.
"""
import sympy as sp

a0,a1,b0,b1,z,t=sp.symbols("a0 a1 b0 b1 z t")
Delta=a0*b1-a1*b0

c1=-b1*(2*a0*b1+12*a1**2+16*a1*b0+9*b0**2)
c2=-(2*a1+b0)*(8*a0*b1+12*a1**2+4*a1*b0+3*b0**2)
c3=-2*a0*(2*a0*b1+36*a1**2+16*a1*b0+3*b0**2)

# Scaling is immaterial: these are 8 times the Cech coordinates.
F=[sp.expand(c1),sp.expand(c2),sp.expand(c3)]

# Main curve: b0=-2a1 and a0*b1=-8a1^2.  On it Delta=-6a1^2.
main_sub={b0:-2*a1,b1:-8*a1**2/a0}
assert all(sp.cancel(f.subs(main_sub))==0 for f in F)
assert sp.cancel(Delta.subs(main_sub))==-6*a1**2

# Boundary a0=b1=0. Put r=b0/a1.  Delta=-r*a1^2, and the only
# remaining equation is (r+2)(3r^2+4r+12)=0.
r=sp.symbols("r")
boundary={a0:0,b1:0,b0:r*a1}
Fb=[sp.factor(f.subs(boundary)) for f in F]
assert Fb[0]==0 and Fb[2]==0
assert sp.factor(Fb[1])==-a1**3*(r+2)*(3*r**2+4*r+12)
assert sp.factor(Delta.subs(boundary))==-r*a1**2

# Exact localization certificate: Groebner basis after adjoining t*Delta-1.
G=sp.groebner(F+[t*Delta-1],t,a0,a1,b0,b1,order="lex")
E=[sp.factor(p.as_expr()) for p in G.polys]
needed=[
 a0*(3*b0**2*t+2),
 b1*(3*b0**2*t+2),
 a0*(2*a1+b0),
 b1*(2*a1+b0),
 a0*(a0*b1+2*b0**2),
 b1*(a0*b1+2*b0**2),
]
for q in needed:
    assert any(sp.expand(e-q)==0 or sp.expand(e+q)==0 for e in E), q

print("e=1 BF triple-obstruction locus verified on Delta != 0")
print("main: b0=-2*a1, a0*b1=-8*a1^2")
print("boundary: a0=b1=0, r=b0/a1 in {-2, roots(3r^2+4r+12)}")
