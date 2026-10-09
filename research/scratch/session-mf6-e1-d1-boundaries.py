"""Exploratory exact complete quartic fibers for six e1,d2=1 endpoints.

Not a universal exclusion; no generated input or research-module import.
Writes exact ranks, complete fibers, and both-chart cubic residues.
"""
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ

x0,x1,x2,x3,z,w,U,V,y,m,r=s.symbols('x0 x1 x2 x3 z w U V y m r')
mon=[x0**i*x1**j*x2**k*x3**(4-i-j-k)
     for i in range(4,-1,-1) for j in range(4-i,-1,-1) for k in range(4-i-j,-1,-1)]
finite={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}
infinity={x3:1,x2:w,x1:w**3+2*U,x0:w**4+V/2+3*w*U}
qr=12*r*r+4*r+3
root=(-1+2*s.sqrt(-2))/6

def reduce_r(expr):
    return s.Add(*[s.rem(c,qr,r)*z**powers[0]*w**powers[1]*y**powers[2]*m**powers[3]
                  for powers,c in s.Poly(s.expand(expr),z,w,y,m).terms()])

def coefficients(polys,variable):
    degree=max(s.degree(p,variable) if p else 0 for p in polys)
    return [[p.coeff(variable,i) for p in polys] for i in range(degree+1)]

def jets(forms,A,B,bs,bt,delta,Gamma,chart):
    exprs=[s.expand(F.subs(chart).subs({U:bt*m+A*y,V:-bs*m+B*y})) for F in forms]
    h=[p.coeff(m,1).coeff(y,0) for p in exprs]
    Q=[p.coeff(m,0).coeff(y,2) for p in exprs]
    E=[p.coeff(m,1).coeff(y,1) for p in exprs]
    K=[p.coeff(m,0).coeff(y,3) for p in exprs]
    T=[s.expand(Gamma*e-delta*k) for e,k in zip(E,K)]
    return exprs,h,Q,T

results=[]
for side in ['finite','infinity']:
    if side=='finite':
        A,B=r*z,1+z;bs,bt=-1/r,s.Integer(1)
        delta=z;Gamma=-(qr+12*r+6+(6*r+9)*z+3*z*z)/8
        Ai,Bi=r,1+w;bsi,bti=1/r,s.Integer(0)
        di,Gi=s.Integer(1),s.Integer(0)
    else:
        A,B=1+r*z,s.Integer(1);bs,bt=s.Integer(0),s.Integer(1)
        delta=s.Integer(1);Gamma=s.Integer(0)
        Ai,Bi=r+w,w;bsi,bti=1/r,-1/r
        di=w;Gi=(36*r*r+16*r+3)/4+(9*r+s.Rational(3,2))*w+3*w*w
    for root_kind in ['r=-1/2','quadratic-root']:
        rr=-s.Rational(1,2) if root_kind=='r=-1/2' else root
        kwargs=[s.simplify(value.subs(r,rr)) if hasattr(value,'subs') else value
                for value in [A,B,bs,bt,delta,Gamma]]
        expr,h,Q,T=jets(mon,*kwargs,finite)
        restrictions=[[p.coeff(m,0).coeff(y,0) for p in expr],
                      [p.coeff(m,0).coeff(y,1) for p in expr],
                      [s.expand(kwargs[4]*q-kwargs[5]*hh) for q,hh in zip(Q,h)]]
        rows=[]
        for polys in restrictions: rows+=coefficients(polys,z)
        matrix=s.Matrix(rows)
        domain=QQ if root_kind=='r=-1/2' else QQ.algebraic_field(s.sqrt(-2))
        DM=DomainMatrix.from_Matrix(matrix).convert_to(domain)
        null=DM.nullspace().to_Matrix()
        forms=[s.expand(sum(c*f for c,f in zip(vector,mon))) for vector in null.tolist()]
        rank=DM.rank()
        assert rank+len(forms)==35
        print(side,root_kind,'rank',rank,'kernel',len(forms),flush=True)
        if len(forms)>0:
            print('common factor',s.factor(s.gcd_list(forms),extension=s.sqrt(-2)),flush=True)
        record={'side':side,'root_kind':root_kind,'rank':rank,'quartic_dimension':len(forms),
                'quartics':list(map(str,forms)),'common_factor':str(s.gcd_list(forms))}
        k2=[s.simplify(value.subs(r,rr)) if hasattr(value,'subs') else value
            for value in [Ai,Bi,bsi,bti,di,Gi]]
        for tag,params,ch in [('finite',kwargs,finite),('infinity',k2,infinity)]:
            ej,hj,Qj,Tj=jets(forms,*params,ch)
            assert all(s.simplify(s.expand(params[4]*qq-params[5]*hh))==0
                       for qq,hh in zip(Qj,hj))
            S=[s.cancel(hh/params[4]) for hh in hj]
            record[tag+'_S']=list(map(str,S))
            record[tag+'_T']=list(map(str,Tj))
            for SS in S:
                s.Poly(SS,z if tag=='finite' else w,extension=s.sqrt(-2))
        results.append(record)
Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2)+'\n')
print('SAVED full finite-fiber matrices and cubic residue pencils; conjugation retains other roots',flush=True)
