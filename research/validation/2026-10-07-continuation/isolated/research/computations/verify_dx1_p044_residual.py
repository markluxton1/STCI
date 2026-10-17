#!/usr/bin/env python3
"""Exact diagnostic for the residual dx=1 P-044 branch.

On dx=1 put u=bx-a. Away from x=0, 2a+1=0, and b+2=0,
P-044 implies R2=R4=Q5=0, where Q2=(2a+1)R2 and
Q4=2(b+2)R4. We eliminate u twice and check that the residual
resultant factors are coprime in QQ[a,x].
"""
import sympy as sp
a,b,x,u=sp.symbols("a b x u")
R2=(-8*a**3*b-64*a**3+80*a**2*b**2*x+640*a**2*b*x+36*a**2*b+1152*a**2*x+72*a**2+124*a*b**2*x+824*a*b*x+70*a*b+1008*a*x+116*a+20*b**3*x**2+256*b**2*x**2+92*b**2*x+1008*b*x**2+604*b*x+45*b+1152*x**2+720*x+72)
R4=(-20*a**3-20*a**2*b**2*x-124*a**2*b*x-368*a**2*x-64*a**2+2*a*b**3*x**2-36*a*b**2*x**2-40*a*b**2*x-280*a*b*x**2-206*a*b*x-720*a*x**2-604*a*x-63*a+4*b**3*x**2-18*b**2*x**2-18*b**2*x-116*b*x**2-63*b*x-288*x**2-180*x-18)
Q5=(16*a**4+48*a**3*b**2*x+256*a**3*b*x+576*a**3*x+64*a**3+36*a**2*b**4*x**2+384*a**2*b**3*x**2+1888*a**2*b**2*x**2+112*a**2*b**2*x+4608*a**2*b*x**2+512*a**2*b*x+5184*a**2*x**2+1216*a**2*x+88*a**2+70*a*b**4*x**2+576*a*b**3*x**2+2096*a*b**2*x**2+60*a*b**2*x+3456*a*b*x**2+160*a*b*x+3040*a*x**2+528*a*x+48*a+2*b**5*x**3-4*b**4*x**3+36*b**4*x**2-80*b**3*x**3+192*b**3*x**2-352*b**2*x**3+400*b**2*x**2-736*b*x**3+192*b*x**2-48*b*x-576*x**3+9)

def numerator_after_u(expr):
    return sp.Poly(sp.fraction(sp.cancel(expr.subs(b,(a+u)/x)))[0],u,a,x).as_expr()

r2=numerator_after_u(R2); r4=numerator_after_u(R4); q5=numerator_after_u(Q5)
assert [sp.degree(f,u) for f in (r2,r4,q5)] == [3,3,5]
res24=sp.factor(sp.resultant(r2,r4,u))
res25=sp.factor(sp.resultant(r2,q5,u))
assert sp.rem(res24,-36*x*(2*a+1),a,x)==0
assert sp.rem(res25,-36*x**2*(2*a+1)**2,a,x)==0
P24=sp.cancel(res24/(-36*x*(2*a+1)))
P25=sp.cancel(res25/(-36*x**2*(2*a+1)**2))
assert sp.Poly(P24,a,x).as_expr()==P24
assert sp.Poly(P25,a,x).as_expr()==P25
assert sp.gcd(sp.Poly(P24,a,x),sp.Poly(P25,a,x)).as_expr()==1
print("VERIFIED: resultant identities and gcd(P24,P25)=1.")
print("CAUTION: this does not prove residual-open emptiness; saturation remains OPEN.")
