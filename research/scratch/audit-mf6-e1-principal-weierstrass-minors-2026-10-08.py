from pathlib import Path
import json,time
import sympy as s
p,r,x,w=s.symbols('p r x w')
b=Path(__file__).parent;j=json.loads((b/'audit-mf6-e1-principal-raw-minors-2026-10-08.json').read_text())
H=s.sympify(j['H']);A=-w**3+8*w*w-12*w+72;C=2*(w*w-6*w+36);E=A*x*x-2*C*x+C
assert s.expand(H.subs({r:x-s.Rational(1,2),p:-2+4*x+w*x*x})+8*x**4*E)==0
out=[]
for m in j['minors']:
 raw=s.sympify(m['factors'][-1][0]);tick=time.monotonic()
 e=s.Poly(raw.subs({r:x-s.Rational(1,2),p:-2+4*x+w*x*x}).expand(),x,w)
 xmin=min(k[0] for k,c in e.terms());ee=s.expand(e.as_expr()/x**xmin)
 print('omit',m['omitted'],'seconds',time.monotonic()-tick,'tacnode factor x^',xmin,'after degrees',s.degree(ee,x),s.degree(ee,w),'terms',len(s.Poly(ee,x,w).terms()),flush=True)
 out.append({'omitted':m['omitted'],'x_exponent':int(xmin),'residual':str(ee)})
 (b/'audit-mf6-e1-principal-weierstrass-minors-2026-10-08.json').write_text(json.dumps({'A':str(A),'C':str(C),'relation':str(E),'transformed':out},indent=2)+'\n')
