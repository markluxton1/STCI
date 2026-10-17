#!/usr/bin/env python3
"""Actual moving cubic transition of the principal e1,d2=4 canonical triple.

Exploratory exact derivation of its single intrinsic extension coordinate.
No stratum is excluded by this source alone. The normalized theta=1
triple and all homogeneous defect sections, including infinity zeros,
are retained. No frozen support-coordinate transition is used.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

z,y,f,w=s.symbols('z y f w')
d=s.symbols('d0:5')
delta=sum(value*z**j for j,value in enumerate(d))
delta_inf=sum(value*w**(4-j) for j,value in enumerate(d))
A,B=1+z,-2-8*z
gamma=192*z+96


def cut(value):
    value=s.expand(value)
    return s.Add(*[value.coeff(y,j)*y**j for j in range(4)])


U=A*y+s.Rational(1,6)*f*y*y
V=B*y-s.Rational(4,3)*f*y*y
b=U+s.Rational(3,2)*z*V
inv=cut(z**-4*(1-b/z**4+b*b/z**8-b**3/z**12))
W=cut((z**3+V)*inv)
ap=cut(z*inv-cut(W**3))
bp=cut(inv-cut(W**4))
Up=ap/2
Vp=cut(-3*cut(W*ap)+2*bp)
Ap,Bp=1+W,-8-2*W
mp=cut(Bp*Up-Ap*Vp)
yp=cut(-Up/3-Vp/6)
assert mp.coeff(y,1)==0
assert s.expand(yp.coeff(y,1)-z**-6)==0
dp=cut(delta_inf.subs(w,W))
gp=3*W+6
relation=cut(dp*mp+cut((cut(dp*gp)+1)*cut(yp*yp)))
f2=-gamma-1/delta
quad=s.cancel(relation.coeff(y,2).subs(f,f2))
assert quad==0
third=s.expand(relation.coeff(y,3))
eta=s.cancel(z**12*delta*third.subs(f,f2))
assert s.denom(eta).is_Integer or s.denom(eta).is_Pow
eta=s.expand(eta)
coordinate=s.factor(eta.coeff(z,-1))
assert s.degree(coordinate,*d)<=2
record={
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope':'principal A=1+z,B=-2-8z; e1,d2=4; theta=1; actual moving support chart',
    'f2':str(f2),
    'second_quotient_y_transition':'y_infinity=z^-6*y+terms order>=2',
    'intrinsic_extension_laurent':str(eta),
    'intrinsic_H1_O_minus2_coordinate':str(coordinate),
    'necessary_splitting_equation':str(coordinate)+'=0',
    'normalization':'delta any nonzero homogeneous quartic; theta nonzero normalized1',
    'status':'EXACT DERIVATION; global cocycle identification and quartic rank intersection require independent audit',
    'open':'principal degree4 defect incidence not excluded'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: actual moving quadratic relation cancels, quotient y transition matches O(-6).')
print('Intrinsic H1(O(-2)) coordinate:',coordinate)
print('OPEN: independent identification and intersection with the full quartic rank incidence.')
