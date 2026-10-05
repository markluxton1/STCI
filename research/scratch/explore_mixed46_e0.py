#!/usr/bin/env python3
"""Exploratory mixed-constant e=0 regular (4,6) contact equations."""
import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('jet46',Path(__file__).parents[1]/'computations/verify_mixed46_regular.py')
j=importlib.util.module_from_spec(spec); spec.loader.exec_module(j)
sp=j.sp
z,U,V=j.z,j.U,j.V
W=j.W4
Lmat=W[:10,:]-W[10:,:]
vs=Lmat.nullspace()
forms=[sp.expand(sum(v[i]*j.I4[i] for i in range(18))) for v in vs]
print('Mixed U+V quartic basis:')
for f in forms:
 p=sp.Poly(sp.expand(f.subs(j.sub).subs(U,-V)),V)
 h=sp.Poly(sp.expand(f.subs(j.sub)),U,V).coeff_monomial(U)
 print('F=',sp.factor(f),'; h=',sp.factor(h),'; R=',sp.factor(p.coeff_monomial(V**2)),flush=True)
Tc=64*j.A-16*j.B+j.D
Q=z/sp.Integer(2)-1
Tnormal=sp.Poly(sp.expand(Tc.subs(j.sub)),U,V)
M=sp.expand(Tnormal.as_expr().subs(U,-V)).coeff(V,1)
print('M=',sp.factor(M),'M²/Q=',sp.factor(M**2/Q))
# Solve Fp U-V first-normal difference so its restriction to U=-V equals -M²/Q V.
target=-sp.cancel(M**2/Q)
tv=sp.Matrix([sp.expand(target).coeff(z,i) for i in range(10)])
coeffp=sp.linsolve((W[10:,:]-W[:10,:],tv))
print('First-normal sextic lift solutions:',coeffp)
# A cleaner basis by prescribed h and the independent q^2 coefficient.
H=[sp.Integer(1),2*z+z**2,z**3,2*z**4+z**5,z**6,2*z**7+z**8,z**9]
piv=W.rref()[1]
WP=W[:,list(piv)]
def lift(P,Q):
 tv=sp.Matrix([sp.expand(P).coeff(z,i) for i in range(10)]+[sp.expand(Q).coeff(z,i) for i in range(10)])
 cs=list(sp.linsolve((WP,tv)))[0]
 return sp.expand(sum(c*j.I4[i] for c,i in zip(cs,piv)))
canon=[lift(h,h) for h in H]+[j.q**2]
print('Canonical mixed h/R:')
for h,f in zip(H+[0],canon):
 R=sp.expand(f.subs(j.sub).subs(U,-V)).coeff(V,2)
 print('h=',h,'R=',sp.factor(R),'; F=',sp.factor(f),flush=True)
# Choose the sextic square lift with its eight free quartic coefficients zero.
sol=list(coeffp)[0]
params=set().union(*[s.free_symbols for s in sol])
params.difference_update({z})
Fp0=sp.expand(sum(c.subs(dict.fromkeys(params,0))*f for c,f in zip(sol,j.I4)))
G0=sp.expand(Tc**2+j.q*Fp0)
print('Fp0=',sp.factor(Fp0))
# Contact data in m=U+V, t=V coordinates.
m,t=sp.symbols('m t')
nsub={U:m-t,V:t}
fcs=sp.symbols('a0 a2 a3 a5 a6 a8 a9 kap')
f=sp.expand(sum(c*g for c,g in zip(fcs,canon)))
nf=sp.Poly(sp.expand(f.subs(j.sub).subs(nsub)),m,t)
h=sp.expand(nf.coeff_monomial(m)); R=sp.expand(nf.coeff_monomial(t**2))
nG0=sp.Poly(sp.expand(G0.subs(j.sub).subs(nsub)),m,t)
assert nG0.coeff_monomial(t**2)==0
B2=sp.expand(nG0.coeff_monomial(m*t)); C3=sp.expand(nG0.coeff_monomial(t**3))
print('G0 cross B2=',sp.factor(B2),'C3=',sp.factor(C3))
# Write correction Fp1 as general mixed-direction quartic.
bcs=sp.symbols('b0 b2 b3 b5 b6 b8 b9 ell')
fp=sp.expand(sum(c*g for c,g in zip(bcs,canon)))
nfp=sp.Poly(sp.expand(fp.subs(j.sub).subs(nsub)),m,t)
hp=nfp.coeff_monomial(m); Rp=nfp.coeff_monomial(t**2)
# G2: m*(B2*t+Q*hp*t+ ...), so eliminating F gives the cubic equation.
E=sp.expand(h*(C3+Q*Rp)-R*(B2+Q*hp))
print('Cubic equation degrees:',sp.degree(E,z))
for deg in range(sp.degree(E,z),-1,-1):
 ce=sp.factor(E.coeff(z,deg))
 print('eq',deg,'=',ce,flush=True)
print('G0 factor=',sp.factor(G0))
# Evaluate augmented ranks for generic rational quartics through cubic order.
for avals in ([1,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0],[1,2,3,4,5,6,7,8]):
 ee=sp.expand(E.subs(dict(zip(fcs,avals))))
 equations=[ee.coeff(z,k) for k in range(13)]
 MM,rhs=sp.linear_eq_to_matrix(equations,bcs)
 print('sample',avals,'h(2)=',h.subs(dict(zip(fcs,avals))).subs(z,2),'cubic ranks',MM.rank(),MM.row_join(rhs).rank(),flush=True)
 if MM.rank()==MM.row_join(rhs).rank():
  print('solution',sp.linsolve((MM,rhs),bcs),flush=True)
bs=[8192,4096,-1024,-1024,-128,64,16,512]
assert sp.expand(E.subs(dict(zip(bcs,bs))))==0
Gstar=sp.expand(G0+j.q*sum(c*g for c,g in zip(bs,canon)))
ngs=sp.Poly(sp.expand(Gstar.subs(j.sub).subs(nsub)),m,t)
print('Gstar factor=',sp.factor(Gstar))
for ij in [(2,0),(1,1),(0,2),(0,3),(1,2),(0,4)]:
 print('Gstar normal',ij,sp.factor(ngs.coeff_monomial(m**ij[0]*t**ij[1])),flush=True)
I3=[j.q*x for x in j.xs]+[j.A,j.B,j.D]
n3=[sp.Poly(sp.expand(g.subs(j.sub)),U,V) for g in I3]
L3=sp.Matrix([[p.coeff_monomial(U).coeff(z,i)-p.coeff_monomial(V).coeff(z,i) for p in n3] for i in range(6)])
print('mixed constant cubic space dim',len(L3.nullspace()))
for cv in L3.nullspace():
 ss=sp.expand(sum(c*g for c,g in zip(cv,I3)))
 print('mixed cubic=',sp.factor(ss),'normalh=',sp.factor(sp.Poly(ss.subs(j.sub),U,V).coeff_monomial(U)))
