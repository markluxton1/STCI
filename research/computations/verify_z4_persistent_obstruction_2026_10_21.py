#!/usr/bin/env python3
"""Exact mod-4 check for the Z4 persistent obstruction. Requires SymPy."""
import sympy as S
a,b,h,d,alpha,beta,gamma,delta=S.symbols("a b h d alpha beta gamma delta")
C1=h*(a*h+3*b**2-5*b*d+3*d**2)
C2=(b-d)*(4*a*h+3*b**2-8*b*d+6*d**2)
C3=a*(a*h+9*b**2-23*b*d+15*d**2)
subs={a:2*alpha,b:2*beta,h:2*gamma,d:1+2*delta}
for C,expected in zip((C1,C2,C3),(2*gamma,2,2*alpha)):
    P=S.Poly(S.expand((C-expected).subs(subs)),alpha,beta,gamma,delta)
    assert all(int(coeff)%4==0 for coeff in P.coeffs())
print("Universal polynomial congruence modulo 4: (2gamma,2,2alpha)")
vectors=[]
for A,G in ((0,0),(1,0),(0,1),(1,1)):
    values=[int(C.subs({a:2*A,b:0,h:2*G,d:1}))%4 for C in (C1,C2,C3)]
    assert values==[2*G,2,2*A]
    vectors.append([G,1,A])
    print(f"admissible a={2*A}, b=0, h={2*G}, d=1: divided {vectors[-1]}")
diffs=[[(v[i]-vectors[0][i])%2 for i in range(3)] for v in vectors[1:]]
assert diffs[0]==[0,0,1] and diffs[1]==[1,0,0]
assert S.Matrix(diffs).rank()==2
print("Variation rank over F2: 2; quotient dimension: 1")
x,y=S.symbols("x y")
D4=S.expand(((x+y)**4-x**4-y**4)/2)
assert D4==2*x**3*y+3*x**2*y**2+2*x*y**3
print("Divided fourth-power defect:",D4)
