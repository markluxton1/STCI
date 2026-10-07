#!/usr/bin/env python3
"""Low-defect e=1 BF annihilator and exact sample carrier ranks.

For xi=c1 z^-1+c2 z^-2+c3 z^-3 in H1(O(-4)), a degree-one
section delta=d0+d1*z kills xi in H1(O(-3)) iff
c1*d0+c2*d1=c2*d0+c3*d1=0.  Hence the nonprimitive d2=1
incidence is c1*c3-c2**2=0, with delta unique off xi=0.

The three exact sample carrier computations are recorded in the companion
research note; this file certifies the obstruction-side determinantal claim
and the sample quotient/defect data used there.
"""
import sympy as sp

a0,a1,b0,b1,d0,d1=sp.symbols("a0 a1 b0 b1 d0 d1")
c1=-b1*(2*a0*b1+12*a1**2+16*a1*b0+9*b0**2)
c2=-(2*a1+b0)*(8*a0*b1+12*a1**2+4*a1*b0+3*b0**2)
c3=-2*a0*(2*a0*b1+36*a1**2+16*a1*b0+3*b0**2)
H=sp.Matrix([[c1,c2],[c2,c3]])
detH=sp.expand(c1*c3-c2**2)
assert sp.factor(H.det()-detH)==0

samples=[
    ((-8,-3, 2,-3),(288,1152,4608),(4,-1)),
    ((-8,-2,-4,-4),(1536,3072,6144),(2,-1)),
    ((-8,-1,-2,-4),(576,1152,2304),(2,-1)),
]
for q,expected,delta in samples:
    sub=dict(zip((a0,a1,b0,b1),q))
    cc=tuple(int(sp.expand(c).subs(sub)) for c in (c1,c2,c3))
    assert cc==expected
    assert q[0]*q[3]-q[1]*q[2] != 0
    assert int(detH.subs(sub))==0
    dd=sp.Matrix(delta)
    assert H.subs(sub)*dd==sp.zeros(2,1)

print("e=1 d2=1 determinantal annihilator certified")
