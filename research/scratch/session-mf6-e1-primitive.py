"""Explore the full quartic containment of all primitive e=1 triples."""
import sys,json,sympy as s
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'computations'))
import verify_mf6_defect12 as a
z,y=a.z,s.symbols('y'); r=s.symbols('r')

def data(A,B):
 D=s.diff(A,z)*B-A*s.diff(B,z)
 h2=s.expand(-(2*A+z*B)*(12*A*A+3*z*z*B*B+4*z*z*D)/(8*z**5))
 assert all(s.simplify(h2.coeff(z,-i))==0 for i in range(1,4))
 gu=s.Add(*[term for term in s.Add.make_args(h2) if term.as_powers_dict().get(z,0)>=0])
 d=s.expand(A.subs(z,0)*s.diff(B,z)-s.diff(A,z)*B.subs(z,0));assert d!=0
 bezs=s.diff(B,z)/d;bezt=-s.diff(A,z)/d
 assert s.expand(bezs*A+bezt*B)==1
 sub={a.U:A*y-bezt*gu*y*y,a.V:B*y+bezs*gu*y*y}
 restrictions=[s.Poly(s.expand(j.as_expr().subs(sub)),y) for j in a.jets]
 rows=[]
 for power in [1,2]:
  exprs=[j.coeff_monomial(y**power) for j in restrictions]
  n=max(s.degree(e,z) if e else 0 for e in exprs)
  rows.extend([[s.expand(e).coeff(z,i) for e in exprs] for i in range(n+1)])
 M=s.Matrix(rows);ns=M.nullspace();print('A,B',A,B,'gamma',gu,'rank',M.rank(),'kernel',len(ns),flush=True)
 Fs=[s.expand(sum(c*F for c,F in zip(v,a.I4))) for v in ns]
 for F in Fs:print('F',s.factor(F),flush=True)
 return {'A':str(A),'B':str(B),'gamma':str(gu),'matrix':[[str(v) for v in row] for row in M.tolist()],'kernel':[[str(v) for v in row] for row in ns],'quartics':list(map(str,Fs))}
results=[data(1+z,-2-8*z),data(-z/s.Integer(2),s.Integer(1))]
Path(__file__).with_name('session-mf6-e1-primitive.json').write_text(json.dumps(results,indent=2)+'\n')
