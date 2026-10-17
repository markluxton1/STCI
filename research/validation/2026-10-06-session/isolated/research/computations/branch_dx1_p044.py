#!/usr/bin/env python3
from pathlib import Path
import re
import sympy as sp

x,a,b,d=sp.symbols("x a b d")
u=b*x-a
src=Path(__file__).with_name("e2_full4_obstruction_2026-10-05.txt").read_text()
Gs=[]
for i in range(1,6):
    m=re.search(rf"^G{i} = (.+)$",src,re.M)
    assert m
    Gs.append(sp.sympify(m.group(1),locals={"x":x,"a":a,"b":b,"d":d}))

Qs=[]
for i,G in enumerate(Gs,1):
    num,den=sp.fraction(sp.cancel(G.subs(d,1/x)))
    num=sp.expand(num)
    q,r=sp.div(num,u,a)
    assert r==0
    Qs.append(sp.factor(q))
    print("Q",i,"den",sp.factor(den),"=",sp.factor(q))

boundary=[sp.factor(q.subs(b,-2)) for q in Qs]
print("\nBOUNDARY")
for i,q in enumerate(boundary,1):
    print("Q",i,"=",q)
    assert sp.expand(q.subs(a,-sp.Rational(1,2)))==0

res=[]
for q in boundary:
    qq,rr=sp.div(q,2*a+1,a)
    assert rr==0
    res.append(sp.factor(qq))

g=res[0]
for q in res[1:]:
    g=sp.factor(sp.gcd(g,q))
print("\nresidual gcd =",g)

nonzero=[q for q in res if q != 0]
GB=sp.groebner(nonzero,a,x,order="lex",domain=sp.QQ)
print("residual Groebner basis")
for q in GB.polys:
    print(sp.factor(q.as_expr()))

print("\nRESIDUAL VIA R5")
a_alt=-8*x-sp.Rational(3,2)
for i,q in enumerate(nonzero,1):
    print(i, sp.factor(q.subs(a,a_alt)))
g2=sp.Poly(nonzero[0].subs(a,a_alt),x,domain=sp.QQ)
for q in nonzero[1:]:
    g2=sp.gcd(g2,sp.Poly(q.subs(a,a_alt),x,domain=sp.QQ))
print("univariate gcd =",sp.factor(g2.as_expr()))
