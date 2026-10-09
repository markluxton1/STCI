#!/usr/bin/env python3
"""Exact top-direction classification on h=t,p(0)=0,r(0)=1.

This retains the exceptional a1=-1/2 family. The a2=0 primitive family is
transported to the already certified parity family by the actual involution.
No multiplier exclusion is claimed for the other two families.
"""
from pathlib import Path
import json
import sympy as s

HERE=Path(__file__).resolve().parent
t,a1,a2,b1,b2,k,z=s.symbols('t a1 a2 b1 b2 k z')
top=json.loads((HERE/'localcoh-symbol-top.json').read_text())
p=a1*t+a2*t*t
r=1+b1*t+b2*t*t
c=s.Matrix([s.expand(t*p**i*r**(3-i)).coeff(t,j)
            for i in range(4) for j in range(8)])
equations=list(s.Matrix(top['annihilator'])*c)
assert equations[0]==0
assert s.expand(equations[1]+3*(8*a1*a1*a2-b1))==0
last=s.factor(equations[2].subs(b1,8*a1*a1*a2))
expected=4*a2*(2*a1+1)*((2*a1+1)**2*b2+
           2*a2*a2*(2*a1-1)*(16*a1**4+8*a1*a1+5))
assert s.expand(last-expected)==0
b2_k=-2*(2*k-1)*(16*k**4+8*k*k+5)/(2*k+1)**2
families=[]
for label,values in [('boundary-rational',{a1:k,a2:1,b1:8*k*k,b2:b2_k}),
                     ('boundary-exceptional',{a1:-s.Rational(1,2),a2:1,b1:2,b2:z})]:
    assert all(s.factor(eq.subs(values))==0 for eq in equations)
    pp,rr=s.factor(p.subs(values)),s.factor(r.subs(values))
    delta=s.factor(s.resultant(pp,rr,t))
    families.append({'label':label,'p':str(pp),'r':str(rr),'resultant':str(delta)})
assert s.expand(s.resultant(t*(-s.Rational(1,2)+t),1+2*t+z*t*t,t)-(z+8)/4)==0
# Reverse parity: a2=0, b1=0, homogeneous primitivity means a1*b2!=0.
# Torus sets b2=1. The normal-dual involution sends (a1*t,1+t²) to
# ((1+t²)/2,2*a1*t), i.e. normalized parity (1+t²,4*a1*t).
families.append({'label':'reverse-parity','p':'a1*t','r':'1+t**2',
                 'open_condition':'a1 != 0',
                 'status':'EXCLUDED by existing parity dual after actual ambient involution'})
(HERE/'session-localcoh-origin-boundary.json').write_text(json.dumps({
    'scope':'h=t,p0=0,r0=1 primitive e=2 directions',
    'normalization':'a2 nonzero normalized to1 by torus; a2=0 reverse parity',
    'families':families,
    'status':'EXACT CLASSIFICATION; first two multiplier incidence families OPEN'
},indent=2)+'\n')
print('PASS: boundary top equations split into rational, exceptional, and reverse-parity families.')
print('PASS: exceptional family retained; homogeneous resultant=(b2+8)/4.')
