import sys,json,sympy as s
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'computations'))
import verify_mf6_defect12 as a
z,y,m,w=s.symbols('z y m w')
# Match the nonzero z symbol in the reconstructed ideal jets.
z=a.z
A=1+z;B=-2-8*z;d=-6;bezs=s.Rational(4,3);bezt=s.Rational(1,6)
gamma=192*z+96
j=json.load(open(Path(__file__).with_name('session-mf6-e1-primitive.json')))[0]
ns=[list(map(s.sympify,v)) for v in j['kernel']]
Fs=[s.expand(sum(c*F for c,F in zip(v,a.I4))) for v in ns]
alpha,beta=s.symbols('alpha beta');F=alpha*Fs[0]+beta*Fs[1]
moving=s.expand(F.subs(a.sub).subs({a.U:bezt*m+A*y,a.V:-bezs*m+B*y}))
h=moving.coeff(m,1).coeff(y,0);E=moving.coeff(m,1).coeff(y,1);K=moving.coeff(m,0).coeff(y,3)
T=s.expand(gamma*E-K)
assert s.expand(moving.coeff(m,0).coeff(y,2)-gamma*h)==0
print('GENERIC ORBIT h',s.factor(h),flush=True); print('T',s.factor(T),flush=True)
print('degrees',s.degree(h,z),s.degree(T,z),flush=True)
print('resultant',s.factor(s.resultant(h.subs(beta,1),T.subs(beta,1),z)),flush=True)
Path(__file__).with_name('session-mf6-e1-generic-poles.json').write_text(json.dumps({'h':str(h),'T':str(T),'quartics':list(map(str,Fs))},indent=2)+'\n')

# Direct infinity chart for the unique beta=0 pencil boundary.
Av=1+w;Bv=-8-2*w;bsinf=-s.Rational(1,3);btinf=-s.Rational(1,6)
ginf=3*w+6
ui=btinf*m+Av*y;vi=-bsinf*m+Bv*y
subinf={a.x3:1,a.x2:w,a.x1:w**3+2*ui,a.x0:w**4+vi/2+3*w*ui}
mi=s.expand(Fs[0].subs(subinf));hi=mi.coeff(m,1).coeff(y,0)
Ei=mi.coeff(m,1).coeff(y,1);Ki=mi.coeff(m,0).coeff(y,3);Ti=s.expand(ginf*Ei-Ki)
assert s.expand(mi.coeff(m,0).coeff(y,2)-ginf*hi)==0
print('beta0 infinity h',s.factor(hi),'T',s.factor(Ti),flush=True)

# The algebraic primitive directions h2=0 have exact straight embeddings.
r=(-1+2*s.sqrt(-2))/6;Ar=r*z;Br=1
restrictions=[s.expand(j.as_expr().subs({a.U:Ar*y,a.V:y})) for j in a.jets]
rows=[]
for k in [1,2]:
 exprs=[j.coeff(y,k) for j in restrictions]
 n=max(s.degree(e,z) if e else 0 for e in exprs)
 rows +=[[s.expand(e).coeff(z,i) for e in exprs] for i in range(n+1)]
M=s.Matrix(rows);DM=DomainMatrix.from_Matrix(M).convert_to(QQ.algebraic_field(s.sqrt(-2)))
null=DM.nullspace().to_Matrix();print('ALGEBRAIC ORBIT rank',18-null.rows,'kernel',null.rows,flush=True)
FFs=[s.expand(sum(c*F for c,F in zip(v,a.I4))) for v in null.tolist()]
for f in FFs:print('ALG F',f,flush=True)
Path(__file__).with_name('session-mf6-e1-algebraic-fiber.json').write_text(json.dumps({'r':str(r),'rank':18-null.rows,'quartics':list(map(str,FFs)),'matrix':[[str(c) for c in row] for row in M.tolist()]},indent=2)+'\n')
