"""Small exact principal contact reconstruction, elliptic direction curve.

No global exclusion. First-normal space is reduced over a rational
function field before considering the contact rank on H=0.
"""
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ, GF
p,r,z,U,V,y,m=s.symbols('p r z U V y m')
x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');xs=x0,x1,x2,x3
mon=[x0**i*x1**j*x2**k*x3**(4-i-j-k)
     for i in range(4,-1,-1) for j in range(4-i,-1,-1) for k in range(4-i-j,-1,-1)]
support=s.Matrix([[int(s.Poly(f.subs({x0:1,x1:z,x2:z**3,x3:z**4}),z).degree()==i)
                   for f in mon] for i in range(17)])
I4=[s.expand(sum(c*f for c,f in zip(vec,mon))) for vec in support.nullspace()]
assert len(I4)==18
chart={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}
A,B=1+r*z,1+p*z;bs,bt=p/(p-r),-r/(p-r)
h2=s.expand(-(2*A+z*B)*(12*A*A+3*z*z*B*B
           +4*z*z*(s.diff(A,z)*B-A*s.diff(B,z)))/(8*z**5))
c=[s.factor(h2.coeff(z,-i)) for i in(1,2,3)]
H=s.expand(64*(c[0]*c[2]-c[1]*c[1]))
delta=s.expand(-8*c[1]+8*c[0]*z)
Gamma=s.Add(*[s.expand(delta*h2).coeff(z,i)*z**i for i in range(3)])
assert s.factor(s.resultant(delta,Gamma,z)-p**4*(2*p+12*r*r+16*r+9)**4/8)==0
j=[s.expand(f.subs(chart).subs({U:bt*m+A*y,V:-bs*m+B*y})) for f in I4]
F1=[s.expand(e.coeff(m,0).coeff(y,1)) for e in j]
Q=[s.expand(e.coeff(m,0).coeff(y,2)) for e in j]
h=[s.expand(e.coeff(m,1).coeff(y,0)) for e in j]
F2=[s.cancel((p-r)*(delta*q-Gamma*hh)) for q,hh in zip(Q,h)]
def rows(polys):
    return [[s.expand(e).coeff(z,i) for e in polys]
            for i in range(max(s.degree(e,z) if e else 0 for e in polys)+1)]
M1,M2=s.Matrix(rows(F1)),s.Matrix(rows(F2))
M=M1.col_join(M2)
for ell,pp in [(13,12),(17,8),(23,5)]:
    assert int(H.subs({r:0,p:pp}))%ell==0
    def rank_mod(matrix):
        reduced=matrix.subs({r:0,p:pp}).applyfunc(
            lambda entry:int(s.numer(entry))*pow(int(s.denom(entry)),-1,ell)%ell)
        return DomainMatrix.from_Matrix(reduced).convert_to(GF(ell)).rank()
    print('curve modular specialization',ell,pp,'first rank',rank_mod(M1),'full rank',rank_mod(M),flush=True)
print('fraction-field first-normal reduction',flush=True)
domain=QQ.frac_field(r,p)
DM1=DomainMatrix.from_Matrix(M1).convert_to(domain)
ns=DM1.nullspace().to_Matrix().T
assert (M1*ns).applyfunc(s.cancel)==s.zeros(M1.rows,ns.cols)
print('generic first-normal kernel',ns.cols,'entry lengths',
      [sum(len(str(x)) for x in ns[:,i]) for i in range(ns.cols)],flush=True)
contact=(M2*ns).applyfunc(s.cancel)
print('reduced contact shape',contact.shape,flush=True)
record={'scope':'principal b0=1,a0=1; chart pP!=0 and determinantp-r!=0',
        'I4':list(map(str,I4)),'H':str(H),'delta':str(delta),'Gamma':str(Gamma),
        'M1':[[str(c) for c in row] for row in M1.tolist()],
        'M2':[[str(c) for c in row] for row in M2.tolist()],
        'first_kernel':[[str(c) for c in row] for row in ns.tolist()],
        'reduced_contact':[[str(c) for c in row] for row in contact.tolist()]}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('SAVED exact contact matrix; complete rank-drop ideal not yet computed',flush=True)
