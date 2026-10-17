import sys,json,sympy as s
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'computations'))
import verify_mf6_type3 as a
A,B=s.symbols('A B');z=a.z
j=json.load(open(Path(__file__).with_name('mf6_type4_incidence.json')))
M=s.Matrix([[s.sympify(e,locals={'A':A,'B':B,'z':z}) for e in row] for row in j['matrix'][:7]])
ns=M.subs({A:12,B:4}).nullspace()
quartics=[s.expand(sum(c*f for c,f in zip(v,a.mixed))) for v in ns]
assert len(quartics)==4
C=s.cancel(quartics[0]/a.a.x0)
assert s.denom(C)==1
assert a.a.vectors(quartics+[C*x for x in a.a.xs],4).rank()==4
assert a.a.vectors([C*x for x in a.a.xs],4).rank()==4
# Normalize cubic integer content.
C=s.Poly(C,*a.a.xs).clear_denoms()[1].primitive()[1].as_expr()
print('CUBIC',C,flush=True)
print('PASS complete special fiber is C*H0(O(1)); all quartics have plane factor',flush=True)
json.dump({'A':12,'B':4,'rank':4,'cubic':str(C),'quartics':[str(F) for F in quartics],'basis':[list(map(str,v)) for v in ns]},open(Path(__file__).with_name('session-mf6-special-fiber.json'),'w'),indent=2)
