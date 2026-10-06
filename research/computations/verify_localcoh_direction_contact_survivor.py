#!/usr/bin/env python3
"""Exact coprime e=0 third-contact survivor and highest-ancestor audit.

The pair defeats a tangent-contact exclusion; the final rational-coefficient
audit decides only this explicit pair, not its contact chart.
"""
import sympy as sp

x,y,z,w,t,U,V=sp.symbols('x y z w t U V')
q=x*w-y*z;A=x*x*z-y**3;B=x*z*z-y*y*w;C=y*w*w-z**3
T=q*(2*x+2*y-2*z-2*w)+A-2*B-C
P6=x*y*w*w+x*z**3-2*y*y*z*w
P7=2*x*z*z*w-y*y*w*w-y*z**3
P9=2*x*w**3-3*y*z*w*w+z**4
# The complement quartics have first symbols (2h,h), and may be obtained
# directly from the universal lift in verify_localcoh_direction_image.py.
K4=w*w*y*y-y*z**3+w*w*x*y-2*w*y*y*z+x*z**3
K5=w*w*y*z-z**4+2*w*w*x*z-2*w*y*z*z-w*w*y*y+2*w*x*z*z-y*z**3
K6=w**3*y-w*z**3+2*w**3*x-3*w*w*y*z+z**4
# K4,K5,K6 above must agree with the e0 universal-lift basis at lambda=2.
L=[x*T,y*T,z*T,w*T,K4,K5,K6,q*q]
fc=[sp.Rational(2,9),-sp.Rational(5,9),sp.Rational(4,9),-sp.Rational(7,9),1,0,-1,2]
gc=[sp.Rational(1,9),-sp.Rational(1,3),sp.Rational(2,9),sp.Rational(1,3),0,1,0,1]
F=sp.expand(sum(c*f for c,f in zip(fc,L)))
G=sp.expand(sum(c*f for c,f in zip(gc,L)))
assert sp.gcd(F,G)==1
chart={x:1,y:t,z:t**3+V,w:t**4+U+sp.Rational(3,2)*t*V}
f=sp.Poly(sp.expand(F.subs(chart)),U,V)
g=sp.Poly(sp.expand(G.subs(chart)),U,V)
hf=f.coeff_monomial(V);hg=g.coeff_monomial(V)
assert sp.expand(f.coeff_monomial(U)-2*hf)==0
assert sp.expand(g.coeff_monomial(U)-2*hg)==0
bf=f.coeff_monomial(U*U)-2*f.coeff_monomial(U*V)+4*f.coeff_monomial(V*V)
bg=g.coeff_monomial(U*U)-2*g.coeff_monomial(U*V)+4*g.coeff_monomial(V*V)
assert sp.expand(hf*bg-hg*bf)==0
D=t**4-t**3-3*t*t-t+1
assert sp.Poly(sp.gcd(hf,hg),t).monic().as_expr()==D
print('F=',sp.factor(9*F));print('G=',sp.factor(9*G))
print('hF=',sp.factor(hf),'hG=',sp.factor(hg))
print('bF=',sp.factor(bf),'bG=',sp.factor(bg))
print('PASS: coprime ambient pair with exact second transverse contact')

# Localize generically on C.  The module inverse monomial U^(-i-1)V^(-j-1)
# has normal order i+j+1. An order-four ancestor therefore uses i+j<=3.
supports=[(i,j) for d in range(4) for i in range(d+1) for j in [d-i]]
cs=sp.symbols('c0:'+str(len(supports)))
out=[(i,j) for d in range(3) for i in range(d+1) for j in [d-i]]
rows=[];rhs=[]
for poly,target in [(f,1),(g,t*t)]:
    for a,b in out:
        rows.append([poly.coeff_monomial(U**(i-a)*V**(j-b)) if i>=a and j>=b else 0 for i,j in supports])
        rhs.append(target if (a,b)==(0,0) else 0)
mat=sp.Matrix(rows);target=sp.Matrix(rhs)
solution=sp.linsolve((mat,target),cs)
assert solution is not sp.EmptySet
sol=list(solution)[0]
print('generic inverse coefficient solution =',tuple(sp.factor(v) for v in sol))
top=[sp.factor(sol[i]) for i,(a,b) in enumerate(supports) if a+b==3]
pole_denominator=5*t**4-2*t**3+6*t**2-2*t+5
pole_numerator=(t+1)*D*(2*t**6-3*t**5+2*t**4-3*t**3-2*t+1)
highest=pole_numerator/pole_denominator
assert all(sp.cancel(value-multiple*highest)==0
           for value,multiple in zip(top,(8,-4,2,-1)))
assert sp.Poly(sp.gcd(pole_numerator,pole_denominator),t).degree()==0
assert sp.Poly(pole_denominator,t).degree()==4
assert all(not (value.free_symbols & set(cs)) for value in top)
print('PASS: forced highest coefficient has uncancelled finite poles; no global quartic ancestor')
print('highest coefficients=',top)
for v in top:
    print('highest numerator=',sp.factor(sp.together(v).as_numer_denom()[0]),'denominator=',sp.factor(sp.together(v).as_numer_denom()[1]))
