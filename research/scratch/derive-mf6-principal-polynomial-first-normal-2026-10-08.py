from pathlib import Path
import json,hashlib
import sympy as s
p,r,b,z=s.symbols('p r b z');x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');base=Path(__file__).parent
src=base/'mf6-principal-weighted-kernel-2026-10-08.json';j=json.loads(src.read_text());H=s.sympify(j['H']).subs(b,1);ns=[s.sympify(e).subs(b,1) for e in j['kernel_columns'][0]];forms=[s.sympify(e) for e in j['forms']]
def rem(e):return s.rem(s.expand(e),H,p)
curve={x0:1,x1:z,x2:z**3,x3:z**4}
fu=[s.Poly(s.diff(f,x3).subs(curve),z) for f in forms];fv=[s.Poly((s.diff(f,x2)+s.Rational(3,2)*z*s.diff(f,x3)).subs(curve),z) for f in forms]
fuc=[rem(sum(n*f.nth(i) for n,f in zip(ns,fu))) for i in range(10)];fvc=[rem(sum(n*f.nth(i) for n,f in zip(ns,fv))) for i in range(10)]
h=[]
for i in range(9):h.append(rem(-fuc[i] if i==0 else -fuc[i]-p*h[-1]))
assert rem(fuc[9]+p*h[8])==0
for i in range(10):assert rem(fvc[i]-(h[i] if i<9 else 0)-(r*h[i-1] if i>0 else 0))==0
constant=s.gcd_list([s.Poly(e,p,r).content() for e in h]);h=[s.cancel(e/constant) for e in h];print('unit content removed',constant,'h sizes',[len(str(e)) for e in h],flush=True)
record={'status':'PASS actual polynomial first-normal h, complete two-component identity','input':src.name,'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'H':str(H),'kernel_column':0,'quartic_coefficients':list(map(str,ns)),'forms':j['forms'],'removed_constant':str(constant),'h_coefficients':list(map(str,h)),'identity':'FU=-(1+p*z)*h*constant; FV=(1+r*z)*h*constant modulo H','first_column_row1':str(ns[1]),'candidate_definition':'H=0 and first_column_row1*det(Sylvester(h,h_z))=0, plus declared chart-complement points','no_exception_list_claim':True,'samples':[]}
for ell,r0,p0 in [(101,2,4),(101,4,6),(103,2,30)]:
 def mod(v):return int(s.numer(v))*pow(int(s.denom(v)),-1,ell)%ell
 assert int(H.subs({r:r0,p:p0}))%ell==0
 values=[mod(e.subs({r:r0,p:p0})) for e in h];poly=s.Poly(sum(c*z**i for i,c in enumerate(values)),z,modulus=ell);assert poly.degree()==8 and s.gcd(poly,poly.diff()).degree()==0
 resultant=mod(s.resultant(poly.as_expr(),poly.diff().as_expr(),z))
 assert resultant!=0 and int(ns[1].subs({r:r0,p:p0}))%ell!=0
 print('sample',ell,r0,p0,'resultant',resultant,flush=True);record['samples'].append({'ell':ell,'r':r0,'p':p0,'h':str(poly.as_expr()),'resultant':resultant,'row1':int(ns[1].subs({r:r0,p:p0}))%ell})
record['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();(base/'mf6-principal-polynomial-first-normal-2026-10-08.json').write_text(json.dumps(record,indent=2)+'\n');print('DONE',flush=True)
