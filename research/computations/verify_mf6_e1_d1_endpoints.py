#!/usr/bin/env python3
"""Complete six e1,d2=1 endpoint fibers and their all-mate exclusion.

Fixed C0, characteristic zero. Complete 35-column ambient matrices,
exact quadratic-field ranks, actual cubic residues, explicit dominant
localized-plane parametrization, full support and branch-value gluing.
No universal positive-D2 classification is asserted.
"""
from pathlib import Path
import hashlib
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

x0,x1,x2,x3,z,w,U,V,y,m,r=s.symbols('x0 x1 x2 x3 z w U V y m r')
xs=(x0,x1,x2,x3)
mon=[x0**i*x1**j*x2**k*x3**(4-i-j-k)
     for i in range(4,-1,-1) for j in range(4-i,-1,-1) for k in range(4-i-j,-1,-1)]
finite={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}
infinity={x3:1,x2:w,x1:w**3+2*U,x0:w**4+V/2+3*w*U}
qr=12*r*r+4*r+3
root=(-1+2*s.sqrt(-2))/6
rinv=-4*r-s.Rational(4,3)
def reduced(expr):
    return s.Add(*[s.rem(c,qr,r)*z**powers[0]*w**powers[1]*y**powers[2]*m**powers[3]
                  for powers,c in s.Poly(s.expand(expr),z,w,y,m).terms()])
def vector(F):
    p=s.Poly(F,*xs)
    return s.Matrix([p.coeff_monomial(term) for term in mon])
def jets(forms,A,B,bs,bt,delta,Gamma,chart):
    expr=[s.expand(F.subs(chart).subs({U:bt*m+A*y,V:-bs*m+B*y})) for F in forms]
    h=[p.coeff(m,1).coeff(y,0) for p in expr]
    Q=[p.coeff(m,0).coeff(y,2) for p in expr]
    T=[s.expand(Gamma*p.coeff(m,1).coeff(y,1)
                -delta*p.coeff(m,0).coeff(y,3)) for p in expr]
    return expr,h,Q,T
def full_matrix(A,B,bs,bt,delta,Gamma):
    expr,h,Q,T=jets(mon,A,B,bs,bt,delta,Gamma,finite)
    restrictions=[[p.coeff(m,0).coeff(y,0) for p in expr],
                  [p.coeff(m,0).coeff(y,1) for p in expr],
                  [s.expand(delta*q-Gamma*hh) for q,hh in zip(Q,h)]]
    rows=[]
    for polys in restrictions:
        degree=max(s.degree(p,z) if p else 0 for p in polys)
        rows.extend([[p.coeff(z,i) for p in polys] for i in range(degree+1)])
    return s.Matrix(rows)

Ac=x0*x0*x2-x1**3
Dc=x2**3-x1*x3*x3
R0=x0**3*x3-(r+s.Rational(3,2))*x0*x0*x1*x2+(r+s.Rational(1,2))*x1**4
R1=x0*x3**3+(r-s.Rational(7,6))*x1*x2*x3*x3+(s.Rational(1,6)-r)*x2**4
FL=R1-(r+s.Rational(1,3))*x3*Dc
FR=R0-x0*Ac
CL=2*x0*x3*x3-2*x1*x2*x3+x1*x3*x3-x2**3
CR=x0*x0*x2-x0*x0*x3+x0*x1*x2-x1**3
matrices={}
records=[]
for side in ['finite','infinity']:
    if side=='finite':
        params=[r*z,1+z,-1/r,s.Integer(1),z,-(qr+12*r+6+(6*r+9)*z+3*z*z)/8]
        form,cubic=FL,CL
    else:
        params=[1+r*z,s.Integer(1),s.Integer(0),s.Integer(1),s.Integer(1),s.Integer(0)]
        form,cubic=FR,CR
    rational=[p.subs(r,-s.Rational(1,2)) for p in params]
    Mhalf=full_matrix(*rational)
    assert Mhalf.rank()==31
    cvectors=s.Matrix.hstack(*[vector(x*cubic) for x in xs])
    assert cvectors.rank()==4 and Mhalf*cvectors==s.zeros(Mhalf.rows,4)
    # Entire algebraic boundary, not just the displayed nonzero vector.
    Mroot=full_matrix(*[p.subs(r,root) for p in params])
    DM=DomainMatrix.from_Matrix(Mroot).convert_to(QQ.algebraic_field(s.sqrt(-2)))
    assert DM.rank()==34
    assert (Mroot*vector(form.subs(r,root))).applyfunc(s.simplify)==s.zeros(Mroot.rows,1)
    records.append({'side':side,'half_rank':31,'half_cubic':str(cubic),
                    'algebraic_rank':34,'algebraic_unique_quartic':str(form)})

# Left actual finite cubic residue. Nonzero coefficient at z4 and S~z7
# imply excess3, so these endpoints cannot realize MF6 type(1,3).
params=[r*z,1+z,-rinv,s.Integer(1),z,-(12*r+6+(6*r+9)*z+3*z*z)/8]
expr,h,Q,T=jets([FL],*params,finite)
assert reduced(z*Q[0]-params[5]*h[0])==0
hl,Tl=reduced(h[0]),reduced(T[0])
assert s.expand(hl-s.Rational(2,3)*(3*r+1)*z**8)==0
assert all(Tl.coeff(z,i)==0 for i in range(4))
assert s.expand(Tl.coeff(z,4)-8*r/9)==0
assert s.gcd(r,qr)==s.gcd(3*r+1,qr)==1

# Right actual second chart; the support/frame transition is not frozen.
Gi=(r-s.Rational(3,2))+(9*r+s.Rational(3,2))*w+3*w*w
params=[r+w,w,rinv,-rinv,w,Gi]
expr,h,Q,T=jets([FR],*params,infinity)
assert reduced(w*Q[0]-Gi*h[0])==0
hr,Tr=reduced(h[0]),reduced(T[0])
assert s.expand(hr-w**8)==0
assert all(Tr.coeff(w,i)==0 for i in range(4))
assert s.expand(Tr.coeff(w,4)+4*(4*r+3)/27)==0
assert s.gcd(4*r+3,qr)==1

# All-degree right-carrier obstruction on a localized plane. No finite
# normalization claim is used: a dominant explicit map suffices.
u,v,kappa=s.symbols('u v kappa')
a=kappa+1
X1=u*u*((u+a)*v-u)/(u+kappa)
X0=u*X1
surface=(x0**3*x3-a*x0*x0*x1*x2+kappa*x1**4-x0**3*x2+x0*x1**3)
assert s.factor(surface.subs({x0:X0,x1:X1,x2:v,x3:1}))==0
delta=v-u
cofactor=u*v*(u+v)+kappa*v*v+kappa*u*v-u*u
assert s.factor((u+kappa)*(X1-v**3)+delta*cofactor)==0
assert s.factor(X0-v**4-u*(X1-v**3)+delta*v**3)==0
assert cofactor.subs(v,0)==-u*u
branch=a*v/(1-v)
assert X1.subs(u,0)==X0.subs(u,0)==0
assert s.factor(X1.subs(u,branch))==s.factor(X0.subs(u,branch))==0
assert s.factor((u+kappa).subs(u,branch)-(v+kappa)/(1-v))==0
assert s.factor((v-u).subs(u,branch)+v*(v+kappa)/(1-v))==0

# Left unique member is a torus transform of coordinate reversal of the
# conjugate right member. Torus weights: R1=12, x3*Dc=13.
reverse={x0:x3,x1:x2,x2:x1,x3:x0}
conjugate=-r-s.Rational(1,3)
reversed_FR=FR.subs(r,conjugate).subs(reverse,simultaneous=True)
assert s.expand(reversed_FR-R1-x3*Dc)==0
lam=conjugate
torus={x0:x0,x1:lam*x1,x2:lam**3*x2,x3:lam**4*x3}
assert s.expand(reversed_FR.subs(torus,simultaneous=True)-lam**12*FL)==0
assert s.gcd(lam,qr)==1

record={'status':'PASS complete six endpoint spaces and all-mate obstruction',
        'scope':'Fixed C0, char0, e1,d2=1 with a0=0 or b1=0 only; principal direction sextic remains open',
        'fibers':records,
        'left_h':str(hl),'left_T':str(Tl),'right_h':str(hr),'right_T':str(Tr),
        'localized_map':{'X0':str(X0),'X1':str(X1),'X2':'v','X3':'1'},
        'cofactor':str(cofactor),'unit_ratio_condition':'n+k=0, then (-kappa)^n=1 impossible norm1/3',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'sympy':s.__version__}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: six complete 35-column quartic fibers; two rational fixed-cubic fibers, four unique algebraic carriers')
print('PASS: both defective endpoint cubic excesses are exactly3, so MF6 type(1,3) is excluded there')
print('PASS: explicit localized-plane map, full inverse support and double-line branch ratio')
print('RESULT: all six e1,d2=1 endpoint orbits admit no mate supported solely on C0, for every mate degree')
print('OPEN: principal a0*b1!=0 direction sextic and e1,d2=2 defective incidence')
