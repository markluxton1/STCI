import sys,json,sympy as s
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'computations'))
import verify_mf6_type3 as a
A,B=s.symbols('A B');z=a.z
j=json.load(open(Path(__file__).with_name('mf6_type4_incidence.json')))
M=s.Matrix([[s.sympify(e,locals={'A':A,'B':B,'z':z}) for e in row] for row in j['matrix'][:7]])
for aa,bb in [(12,4),(-12,-2),(0,1+s.sqrt(-3)),(-12,-2+6*s.I)]:
 mat=M.subs({A:aa,B:bb}); ns=mat.nullspace();print('FIBER',aa,bb,'rank',8-len(ns),'basis',flush=True)
 for v in ns:
  F=s.expand(sum(c*f for c,f in zip(v,a.mixed))); print(s.factor(F,extension=[s.sqrt(-3),s.I]),flush=True)
  delta=z*(z+2)*(aa+bb*(z-2)+z**2-2*z+4)+16
  h=s.expand(F.subs(a.a.sub)).coeff(a.U,1).coeff(a.V,0)
  S=s.cancel(h/delta,extension=[s.sqrt(-3),s.I]); print('S',s.factor(S,extension=[s.sqrt(-3),s.I]),flush=True)
