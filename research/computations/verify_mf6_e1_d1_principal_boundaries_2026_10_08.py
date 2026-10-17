#!/usr/bin/env python3
"""Complete ambient quartic spaces at principal elliptic frame boundaries.

Rebuilds all 35 ambient columns, with the correct alternative defect
section when c1=c2=0. Does not specialize a generic nullspace frame.
Exact characteristic-zero computations; no global STCI conclusion.
"""
from pathlib import Path
import hashlib,json,argparse
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

z,U,V,y,m,t=s.symbols('z U V y m t')
x0,x1,x2,x3=s.symbols('x0 x1 x2 x3'); xs=x0,x1,x2,x3
mon=[x0**i*x1**j*x2**k*x3**(4-i-j-k)
     for i in range(4,-1,-1) for j in range(4-i,-1,-1) for k in range(4-i-j,-1,-1)]
chart={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}

def compute(name,r,p,b,field):
    def canon(e): return field.to_sympy(field.from_sympy(s.cancel(e)))
    def polycanon(e,var=z):
        return s.Add(*[canon(c)*var**power[0] for power,c in s.Poly(s.expand(e),var).terms()])
    A,B=1+r*z,b+p*z
    det=canon(p-r*b)
    assert det!=0
    bs,bt=canon(p/det),canon(-r/det)
    h2=s.expand(-(2*A+z*B)*(12*A*A+3*z*z*B*B
              +4*z*z*(s.diff(A,z)*B-A*s.diff(B,z)))/(8*z**5))
    cocycle=[canon(h2.coeff(z,-i)) for i in (1,2,3)]
    assert canon(cocycle[0]*cocycle[2]-cocycle[1]**2)==0
    if cocycle[0]!=0:
        delta=polycanon(-8*cocycle[1]+8*cocycle[0]*z)
    else:
        assert cocycle[1]==0 and cocycle[2]!=0
        delta=s.Integer(1)
    Gamma=polycanon(s.Add(*[s.expand(delta*h2).coeff(z,i)*z**i for i in range(3)]))
    expr=[s.expand(F.subs(chart).subs({U:bt*m+A*y,V:-bs*m+B*y})) for F in mon]
    restrictions=[[polycanon(F.coeff(m,0).coeff(y,0)) for F in expr],
                  [polycanon(F.coeff(m,0).coeff(y,1)) for F in expr],
                  [polycanon(delta*F.coeff(m,0).coeff(y,2)
                             -Gamma*F.coeff(m,1).coeff(y,0)) for F in expr]]
    rows=[]
    for polys in restrictions:
        deg=max(s.degree(e,z) if e else 0 for e in polys)
        rows.extend([[e.coeff(z,i) for e in polys] for i in range(deg+1)])
    M=s.Matrix(rows)
    DM=DomainMatrix.from_Matrix(M).convert_to(field)
    null=DM.nullspace().to_Matrix().T
    assert DM.rank()+null.cols==35
    expected_rank=31 if name=='node_cubic' else 34
    assert DM.rank()==expected_rank
    assert (DM*DomainMatrix.from_Matrix(null).convert_to(field)).is_zero_matrix
    forms=[]
    for col in range(null.cols):
        vector=list(null[:,col]); lead=next(c for c in vector if c!=0)
        vector=[canon(c/lead) for c in vector]
        forms.append(s.expand(sum(c*f for c,f in zip(vector,mon))))
    factors=[]
    if field==QQ:
        factors=[str(s.factor(F)) for F in forms]
    if name=='node_cubic':
        cubic=s.cancel(forms[0]/x0)
        assert s.denom(cubic)==1 and s.Poly(cubic,*xs).total_degree()==3
        assert [s.cancel(F/cubic) for F in forms]==[x0,x1,x0+x1/2+x2/2,x3]
    if s.degree(delta,z)==1:
        assert canon(s.resultant(delta,Gamma,z))!=0
    else:
        # The alternative section is nonzero on this affine chart.
        # Its sole zero is infinity; the surviving c3 provides the
        # nonzero opposite-chart quadratic correction there.
        assert delta==1 and cocycle[2]!=0
    print(name,'rank',DM.rank(),'dimension',len(forms),'delta',delta,flush=True)
    out={'name':name,'r':str(r),'p':str(p),'b0':str(b),
         'field':str(field),'direction_A':str(A),'direction_B':str(B),
         'quadratic_cocycle':list(map(str,cocycle)),'delta':str(delta),'Gamma':str(Gamma),
         'complete_35column_rank':DM.rank(),'quartic_dimension':len(forms),
         'quartic_basis':list(map(str,forms)),'rational_factorizations':factors}
    return out

parser=argparse.ArgumentParser();parser.add_argument('--scope',default='all',choices=['rational','quadratic','infinity','all'])
args=parser.parse_args(); results=[]
if args.scope in ['rational','all']:
    for name,r,p in [('node_cubic',s.Rational(1,2),s.Integer(2)),
                      ('rhalf_unique',s.Rational(1,2),s.Integer(8)),
                      ('Szero_unique',-s.Rational(1,6),s.Rational(2,3))]:
        results.append(compute(name,r,p,s.Integer(1),QQ))
if args.scope in ['quadratic','all']:
    assert s.Poly(12*t*t+20*t+11,t).is_irreducible
    root=(-5+2*s.sqrt(-2))/6
    results.append(compute('c1zero_infinity_defect',root,2*root+1,s.Integer(1),QQ.algebraic_field(s.sqrt(-2))))
if args.scope in ['infinity','all']:
    assert s.Poly(t**3-8*t*t+12*t-72,t).is_irreducible
    assert s.discriminant(t**3-8*t*t+12*t-72,t)!=0
    root=s.CRootOf(t**3-8*t*t+12*t-72,0)
    results.append(compute('b0zero_cubic_orbit',s.Integer(1),root,s.Integer(0),QQ.algebraic_field(root)))

record={'scope':'Fixed C0, char0, e1,d2=1; only finite principal frame boundaries listed',
        'method':'Fresh all35 ambient monomials and full restriction/first-normal/quadratic-contact matrix',
        'algebraic_scope':'A displayed irreducible quadratic/cubic field calculation covers every conjugate geometric point',
        'fibers':results,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sympy':s.__version__}
Path(__file__).with_name(Path(__file__).stem+'_'+args.scope+'.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS complete quartic spaces in requested exceptional chart scope',flush=True)
