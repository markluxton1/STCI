#!/usr/bin/env python3
"""Exact balanced top-symbol image for the 30-dimensional T4(-7) space.

M2-exported stage numerators h/(q^4 B^4). On x=1 put t=y,
a=z-t^3, q=w-t*z. Balanced conormal coordinates are
u=q-ta/2, v=a. At normal order one, B=t^3 a-t^2q,
u=q/2-B/(2t^2), v=q/t+B/t^3.
For each i=0,...,3 the residue of h u^i v^(3-i) is the coefficient
of q^3 B^3 in the degree-six normal numerator, divided by det=t^3.
These four residues are divided-power coefficients of the cubic symbol.
"""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parent
x,y,z,w,t,a,q,b=s.symbols('x y z w t a q b')
lines=(ROOT/'localcoh-symbol-numerators.txt').read_text().splitlines()
columns=[]
for line in lines:
    h=s.sympify(line.replace('^','**'),locals={'x':x,'y':y,'z':z,'w':w})
    h0=s.Poly(s.expand(h.subs({x:1,y:t,z:t**3+a,w:t**4+t*a+q})),a,q)
    assert all(i+j>=3 for i,j in h0.monoms())
    h3=sum(c*a**i*q**j for (i,j),c in h0.terms() if i+j==3)
    h3=s.expand(h3.subs(a,(b+t**2*q)/t**3))
    u=q/s.Integer(2)-b/(2*t**2)
    v=q/t+b/t**3
    c=[]
    for i in range(4):
        expr=s.Poly(s.expand(h3*u**i*v**(3-i)),q,b).coeff_monomial(q**3*b**3)/t**3
        expr=s.cancel(expr)
        assert s.denom(expr).is_Integer
        assert s.degree(expr,t)<=7
        c.append(expr)
    columns.append(c)
M=s.Matrix([[s.expand(c[i]).coeff(t,j) for c in columns] for i in range(4) for j in range(8)])
assert M.shape==(32,30) and M.rank()==29
ann=M.T.nullspace()
assert len(ann)==3
print('rank top map = 29, kernel dimension = 1')
print('annihilator of top-image, coefficient order c_i t^j:')
rows=[]
for r in ann:
    den=s.ilcm(*(s.denom(v) for v in r))
    r=[int(den*v) for v in r]
    g=s.igcd(*r)
    r=[v//g for v in r]
    if next(v for v in r if v)!=abs(next(v for v in r if v)):r=[-v for v in r]
    print({f'c{i}[t^{j}]':r[8*i+j] for i in range(4) for j in range(8) if r[8*i+j]})
    rows.append(r)
(ROOT/'localcoh-symbol-top.json').write_text(json.dumps({'columns':[[str(c) for c in col] for col in columns],'matrix':[[str(v) for v in row] for row in M.tolist()],'annihilator':rows},indent=2)+'\n')
