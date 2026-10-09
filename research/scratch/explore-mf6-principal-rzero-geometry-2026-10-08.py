from pathlib import Path
import json,sympy as s
p,r,b,z,U,V,y,m=s.symbols('p r b z U V y m');x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');HERE=Path(__file__).parent
j=json.loads((HERE/'mf6-principal-weighted-kernel-2026-10-08.json').read_text());H0=8*p**3-16*p*p+6*p-9
coeff=[s.rem(s.sympify(e).subs({r:0,b:1}),H0,p) for e in j['kernel_columns'][0]]
assert any(e!=0 for e in coeff)
# r=0 gives Bezout m-frame U=y,V=-m+(1+pz)y.
F=s.expand(sum(c*s.sympify(f) for c,f in zip(coeff,j['forms'])))
chart={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}
jet=s.expand(F.subs(chart).subs({U:y,V:-m+(1+p*z)*y}))
jet=s.Poly(jet,p,z,m,y).as_expr()
quant={}
for name,mi,yi in [('h',1,0),('Q',0,2),('E',1,1),('R',2,0),('K',0,3)]:
 e=s.rem(s.expand(jet.coeff(m,mi).coeff(y,yi)),H0,p);quant[name]=s.expand(e)
 print(name,'factored',s.factor(e),flush=True)
alpha=s.CRootOf(H0,0);field=s.QQ.algebraic_field(alpha)
ph=s.Poly(quant['h'].subs(p,alpha),z,domain=field)
print('h factors',s.factor_list(ph),flush=True)
for name in ('E','R','K'):
 q=s.Poly(quant[name].subs(p,alpha),z,domain=field)
 g=ph.gcd(q)
 print('gcd h',name,g.as_expr(),flush=True)
# Export finite algebraic-field Jacobian checks; all three embeddings remain.
def m2(e):return str(e).replace('**','^')
source='A=QQ[p];\nK=toField(A/ideal('+m2(H0)+'));\nR=K[x0,x1,x2,x3];\nF='+m2(F)+';\nJ=ideal(diff(x0,F),diff(x1,F),diff(x2,F),diff(x3,F));\nprint(\"Jacobian dimension/degree\",dim(R/J),degree(R/J));\nprint(\"saturated Jacobian\",saturate(J,ideal(x0,x1,x2,x3)));\n'
(HERE/'explore-mf6-principal-rzero-geometry-2026-10-08.m2').write_text(source)
(HERE/'explore-mf6-principal-rzero-geometry-2026-10-08.json').write_text(json.dumps({'scope':'r0,H0irreduciblecubic; unique polynomial carrier generator0','H0':str(H0),'F':str(F),'coefficients':list(map(str,coeff)),'jets':{k:str(e) for k,e in quant.items()}},indent=2)+'\n')
print('SAVED',flush=True)
