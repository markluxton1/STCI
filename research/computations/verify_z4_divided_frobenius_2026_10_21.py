#!/usr/bin/env python3
import sympy as s
from math import comb
u,X,Y=s.symbols('u X Y')
a,b,h,d,A,B,H,D=s.symbols('a b h d A B H D')
F=u**4-(u**4+X)
G=s.expand((u**3+Y)**4-(u**4+X)**3)
assert s.expand(F+X)==0
assert s.expand(G-(4*u**9*Y+6*u**6*Y**2+4*u**3*Y**3+Y**4-3*u**8*X-3*u**4*X**2-X**3))==0
C=[h*(a*h+3*b*b-5*b*d+3*d*d),(b-d)*(4*a*h+3*b*b-8*b*d+6*d*d),a*(a*h+9*b*b-23*b*d+15*d*d)]
for expr,expected in zip(C,[2*H,2,2*A]):
    poly=s.Poly(s.expand(expr.subs({a:2*A,b:2*B,h:2*H,d:1+2*D})-expected),A,B,H,D)
    assert all(coef%4==0 for coef in poly.coeffs())
def valuation(n,p):
    v=0
    while n%p==0: n//=p;v+=1
    return v
for p in (2,3,5,7):
    for r in (1,2,3):
        q=p**r
        assert all(valuation(comb(q,j),p)==r-valuation(j,p) for j in range(1,q))
print("PASS: integral U equations, universal mod-4 Cech coefficients, sample binomial valuations")
