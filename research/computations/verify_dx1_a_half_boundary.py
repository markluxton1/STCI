#!/usr/bin/env python3
"""Exact verifier for the divisor 2a+1=0 on the dx=1 P-044 slice.

Uses the persisted dx=1 obstruction numerators directly.  It checks that
a=-1/2, on the dx=1 chart x!=0, gives either b=-2 (the P-045 family)
or u=bx-a=0, hence Delta=0.  Removing the common factor x is valid only
on that chart; the unsaturated residual ideal also contains x=0.
"""
import sympy as sp
b,x=sp.symbols("b x")
a=sp.Rational(-1,2)
# Numerators copied from branch_dx1_p044.out, then specialized a=-1/2.
Q1=-32*a**5-144*a**4*b**2*x-1120*a**4*b*x-2304*a**4*x+16*a**4-384*a**3*b**2*x-2304*a**3*b*x-3072*a**3*x+80*a**3-48*a**2*b**3*x**2-448*a**2*b**2*x**2-472*a**2*b**2*x-960*a**2*b*x**2-2096*a**2*b*x-1600*a**2*x+88*a**2-64*a*b**3*x**2-512*a*b**2*x**2-288*a*b**2*x-640*a*b*x**2-864*a*b*x+768*a*x**2-192*a*x+46*a-4*b**4*x**3-64*b**3*x**3-36*b**3*x**2-352*b**2*x**3-304*b**2*x**2-81*b**2*x-768*b*x**3-528*b*x**2-190*b*x-576*x**3+9
Q3=-16*a**4-32*a**3*b*x-192*a**3*x-48*a**3-96*a**2*b**2*x**2+24*a**2*b**2*x-960*a**2*b*x**2-48*a**2*b*x-2304*a**2*x**2-672*a**2*x-72*a**2+8*a*b**3*x**2+48*a*b**2*x**2+60*a*b**2*x-480*a*b*x**2+120*a*b*x-1856*a*x**2-384*a*x-44*a+4*b**4*x**3+48*b**3*x**3+12*b**3*x**2+288*b**2*x**3+168*b**2*x**2+36*b**2*x+704*b*x**3+384*b*x**2+116*b*x+576*x**3-9
R4=-20*a**3-20*a**2*b**2*x-124*a**2*b*x-368*a**2*x-64*a**2+2*a*b**3*x**2-36*a*b**2*x**2-40*a*b**2*x-280*a*b*x**2-206*a*b*x-720*a*x**2-604*a*x-63*a+4*b**3*x**2-18*b**2*x**2-18*b**2*x-116*b*x**2-63*b*x-288*x**2-180*x-18
Q4=2*(b+2)*R4
Q5=16*a**4+48*a**3*b**2*x+256*a**3*b*x+576*a**3*x+64*a**3+36*a**2*b**4*x**2+384*a**2*b**3*x**2+1888*a**2*b**2*x**2+112*a**2*b**2*x+4608*a**2*b*x**2+512*a**2*b*x+5184*a**2*x**2+1216*a**2*x+88*a**2+70*a*b**4*x**2+576*a*b**3*x**2+2096*a*b**2*x**2+60*a*b**2*x+3456*a*b*x**2+160*a*b*x+3040*a*x**2+528*a*x+48*a+2*b**5*x**3-4*b**4*x**3+36*b**4*x**2-80*b**3*x**3+192*b**3*x**2-352*b**2*x**3+400*b**2*x**2-736*b*x**3+192*b*x**2-48*b*x-576*x**3+9
F=[sp.factor(q) for q in (Q1,Q3,Q4,Q5)]
for f in F:
    assert sp.rem(f,(b+2)**2,b,x)==0
res=[sp.factor(f/(b+2)**2) for f in F]
# Away from b=-2 and x=0, remove the verified common x factor.  Ordinary
# membership below is in the divided ideal, which has the same localized
# ideal on this chart; no ordinary membership in the undivided ideal is used.
assert all(sp.rem(f,x,b,x)==0 for f in res)
res_on_chart=[sp.cancel(f/x) for f in res]
assert all(sp.Poly(f,b,x,domain=sp.QQ).as_expr()==f for f in res_on_chart)
G=sp.groebner(res_on_chart,b,x,order="lex",domain=sp.QQ)
u=b*x+sp.Rational(1,2)
assert G.reduce(u)[1]==0
print("VERIFIED: on a=-1/2 and x!=0, P-044 implies b=-2 or u=0.")
