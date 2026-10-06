#!/usr/bin/env python3
"""Exact regular-(4,6) investigations for C0; see adjacent research note.

This script derives quartic normal images rather than importing coefficients.
"""
import sympy as sp
x0,x1,x2,x3,z,U,V,lam=sp.symbols('x0 x1 x2 x3 z U V lam')
xs=(x0,x1,x2,x3)
q=x0*x3-x1*x2
A=x0**2*x2-x1**3
B=x0*x2**2-x1**2*x3
D=x2**3-x1*x3**2

def mons(d):
    return [x0**i*x1**j*x2**k*x3**(d-i-j-k) for i in range(d,-1,-1) for j in range(d-i,-1,-1) for k in range(d-i-j,-1,-1)]
def vector(f,d):
    p=sp.Poly(f,*xs)
    return sp.Matrix([p.coeff_monomial(m) for m in mons(d)])
def basis(forms,d):
    m=sp.Matrix.hstack(*[vector(f,d) for f in forms])
    return [sp.expand(forms[i]) for i in m.rref()[1]]
I4=basis([q*m for m in mons(2)]+[f*x for f in (A,B,D) for x in xs],4)
K6=[q*f for f in I4]+[A**2,A*B,B**2,B*D,D**2]
assert len(I4)==18 and sp.Matrix.hstack(*[vector(f,6) for f in K6]).rank()==23
sub={x0:1,x1:z,x2:z**3+V,x3:z**4+U+sp.Rational(3,2)*z*V}
normal=[sp.Poly(sp.expand(f.subs(sub)),U,V) for f in I4]
W4=sp.Matrix([[p.coeff_monomial(U).coeff(z,j) for p in normal] for j in range(10)]+[[p.coeff_monomial(V).coeff(z,j) for p in normal] for j in range(10)])
assert W4.rank()==17
pure_kernel=W4[:10,:].nullspace()
pure=[sp.expand(sum(v[i]*I4[i] for i in range(18))) for v in pure_kernel]
assert len(pure)==8
print('Pure normal quartic basis, followed by h(z),R(z) where F|V=0=R U^2+...:')
for f in pure:
    p=sp.Poly(sp.expand(f.subs(sub)),U,V)
    print(sp.factor(f), '; h=',sp.factor(p.coeff_monomial(V)),'; R=',sp.factor(p.coeff_monomial(U**2)),flush=True)

# Closed basis used in the theorem (replace the sign of the first basis entry).
P6=x0*x1*x3**2+x0*x2**3-2*x1**2*x2*x3
P7=2*x0*x2**2*x3-x1**2*x3**2-x1*x2**3
P9=2*x0*x3**3-3*x1*x2*x3**2+x2**4
closed=[x0*A,x1*A,x2*A,x3*A,P6,P7,P9,q**2]
assert sp.Matrix.hstack(*[vector(f,4) for f in closed]).rank()==8
assert all(W4[:10,:]*v==sp.zeros(10,1) for v in pure_kernel)
coeff=sp.symbols('c0 c1 c3 c4 c6 c7 c9 kappa')
F=sp.expand(sum(c*f for c,f in zip(coeff,closed)))
pF=sp.Poly(sp.expand(F.subs(sub)),U,V)
h=coeff[0]+coeff[1]*z+coeff[2]*z**3+coeff[3]*z**4+coeff[4]*z**6+coeff[5]*z**7+coeff[6]*z**9
R=coeff[7]+coeff[4]*z-coeff[5]*z**2+3*coeff[6]*z**4
assert sp.expand(pF.coeff_monomial(V)-h)==0
assert sp.expand(pF.coeff_monomial(U**2)-R)==0
assert pF.coeff_monomial(U)==0

# The residual rho of a pure quartic on the quadric.  Variables aa,bb
# describe the first ruling; ss,tt describe the second.
aa,bb,ss,tt=sp.symbols('aa bb ss tt')
segre={x0:aa*ss,x1:aa*tt,x2:bb*ss,x3:bb*tt}
Ceq=bb*ss**3-aa*tt**3
rho=sp.cancel(F.subs(segre)/Ceq)
assert sp.Poly(rho,aa,bb,ss,tt).total_degree()==4
assert sp.expand(rho.subs({aa:0,bb:1,tt:1}))==coeff[6]*ss
# With c9=0 the entire aa=0 ruling is a component of rho.
assert sp.expand(rho.subs({aa:0,coeff[6]:0}))==0
# At C_infinity, c9 != 0 gives a smooth ambient carrier; rho crosses C once.
F_inf=sp.expand(F.subs({x3:1,x0:sp.Symbol('xx'),x1:sp.Symbol('yy'),x2:sp.Symbol('ww')}))
xx,yy,ww=sp.symbols('xx yy ww')
assert sp.diff(F_inf,xx).subs({xx:0,yy:0,ww:0})==2*coeff[6]
assert sp.diff(rho.subs({bb:1,tt:1}),ss).subs({aa:0,ss:0})==coeff[6]

# Highest U^2 coefficient of a general thick sextic detects D^2 only.
normal6=[sp.Poly(sp.expand(f.subs(sub)),U,V) for f in K6]
assert [p.coeff_monomial(U**2).coeff(z,10) for p in normal6]==[0]*22+[4]
# Hence G_2 divisible by V implies sigma divisible by aa.
assert sp.expand(D.subs(segre)-bb**2*Ceq)==0
assert sp.expand(A.subs(segre)-aa**2*Ceq)==0

# Universal cubic-contact rigidity.  Match the leading c9 coefficient and
# subtract a scalar multiple of F.  The remaining F' has c9'=0.
r0,r1,r3,r4,r6,r7,rlam=sp.symbols('r0 r1 r3 r4 r6 r7 rlam')
hp=r0+r1*z+r3*z**3+r4*z**4+r6*z**6+r7*z**7
Rp=rlam+r6*z-r7*z**2
E=sp.expand(h*Rp-hp*R)
assert E.coeff(z,11)==-4*coeff[6]*r7
assert E.subs(r7,0).coeff(z,10)==-2*coeff[6]*r6
assert E.subs({r7:0,r6:0}).coeff(z,9)==coeff[6]*rlam
assert sp.expand(E.subs({r7:0,r6:0,rlam:0})+hp.subs({r7:0,r6:0})*R)==0

# Check the formal cubic coefficient directly, without a normal transition.
s2,s3=sp.symbols('s2 s3')
Fp=sp.expand(r0*closed[0]+r1*closed[1]+r3*closed[2]+r4*closed[3]+r6*closed[4]+r7*closed[5]+rlam*q**2)
pFp=sp.Poly(sp.expand(Fp.subs(sub)),U,V)
Gnormal=sp.expand(V**2+(U+sp.Rational(3,2)*z*V-z*V)*pFp.as_expr())
g3=sp.expand(Gnormal.subs(V,s2*U**2+s3*U**3)).coeff(U,3)
assert sp.expand(g3-(Rp+hp*s2))==0
assert sp.cancel(g3.subs(s2,-R/h)-E/h)==0
print('PASS: pure e=0 (4,6) exclusion identities and cubic-contact rigidity')
