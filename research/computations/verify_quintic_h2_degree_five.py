#!/usr/bin/env python3
"""Exact QQ certificate for the quintic h2 degree-five incidence exclusion.

Run at repository root: python research/computations/verify_quintic_h2_degree_five.py
Requires sympy. Reads the authoritative primitive conductor, not saved q_i exports.
"""
from pathlib import Path
import sympy as s

delta,a,B,G,J,p=s.symbols("delta a B G J p")
path=Path("research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt")
raw=path.read_text().strip()
F=s.Poly(s.sympify(raw.replace("^","**"),locals=locals()),p)
assert F.degree()==8
assert s.factor(F.nth(0).subs(J,0))==0
assert s.factor(F.nth(1).subs(J,0))==-2*G*(G+3*delta**2)**2*(G+delta**2+2*B)

# On the admissible open, the simple zero and support ODE force w=a=B=0.
# Common-factor equations then give R=0 and v as below.
T=3*G+4*delta**2
v=-delta*(delta+1)/T
U=-delta-delta**2
L=delta**2-3*delta
N=L*T-G*U
R=9*G**2+2*G*delta**3+22*G*delta**2-4*G*delta+2*delta**5+12*delta**4-6*delta**3
assert s.expand(2*delta*T*T-U*N-2*delta*R)==0
f=s.Poly(F.as_expr().subs({a:0,B:0,J:0}),p)
assert f.nth(8)==0
q5=f.nth(7)
q4=f.nth(6)-v*q5
q3=f.nth(5)-v*q4
assert s.expand(q5-delta**7)==0
P=s.cancel(T*(q4-5*v*q5))
S=s.cancel(T**2*(q3-10*v**2*q5))
assert s.denom(P)==1 and s.denom(S)==1
rP=s.factor(s.resultant(R,P,G))
rS=s.factor(s.resultant(R,S,G))
fdelta=40*delta**5-323*delta**4-2018*delta**3-288*delta**2-600*delta+156
gdelta=(128*delta**7+4720*delta**6+600*delta**5-58408*delta**4
        +124123*delta**3+2484*delta**2+44376*delta-11016)
assert s.expand(rP-6*delta**13*(delta+1)**2*fdelta)==0
assert s.expand(rS+9*delta**15*(delta+1)**4*gdelta)==0
assert s.gcd(s.Poly(fdelta,delta),s.Poly(gdelta,delta)).degree()==0
print("PASS: degree-five support incidence empty on the prescribed open")
