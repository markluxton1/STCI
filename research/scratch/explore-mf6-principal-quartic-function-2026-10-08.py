from pathlib import Path
import json,time
import sympy as s
p,r=s.symbols('p r');b=Path(__file__).parent
j=json.loads((b/'session-mf6-e1-principal-contact-2026-10-08.json').read_text());a=json.loads((b/'audit-mf6-e1-principal-raw-minors-2026-10-08.json').read_text());k=json.loads((b/'session-mf6-e1-principal-minors-2026-10-08.json').read_text());H=s.sympify(j['H']);T=2*p-4*r*r-4*r-1
N=s.Matrix([[s.sympify(e) for e in row] for row in j['first_kernel']]);N=N*s.diag(*[1/s.sympify(e) for e in k['first_frame_column_divisors']]);N=N.applyfunc(s.cancel)
cof=s.zeros(7,1)
for record in a['minors']:
 i=record['omitted'];minor=s.sympify(record['coefficient'])*s.prod(s.sympify(f)**n for f,n in record['factors']);minor=s.cancel(minor/(p*(2*r-1)**4*T**7));cof[i]=(-1)**i*minor
print('cofactors stripped only shared units',flush=True)
fs=[]
for row in range(18):
 f=s.rem(s.expand(sum(N[row,i]*cof[i] for i in range(7))),H,p);fs.append(s.expand(f));print('row',row,'degree',s.total_degree(fs[-1]),flush=True)
gcd=s.factor(s.gcd_list(fs));print('polynomial common factor',gcd,flush=True)
fs=[s.cancel(f/gcd) for f in fs]
K=s.QQ.frac_field(r);h=s.Poly(H,p,domain=K);polys=[s.Poly(f,p,domain=K) for f in fs]
print('primitive source rows degrees',[(f.degree(),max(s.degree(s.numer(c),r) for c in f.all_coeffs())) for f in polys],flush=True)
inverse=s.invert(polys[1],h);print('normalizing coefficient 1',flush=True)
normalized=[]
for index,f in enumerate(polys):
 out=-(f*inverse).rem(h).as_expr();out=s.cancel(out);normalized.append(str(out));print('normalized',index,'length',len(str(out)),flush=True)
(b/'explore-mf6-principal-quartic-function-2026-10-08.json').write_text(json.dumps({'H':str(H),'scope':'H=0 on valid frame plus coefficient row1 nonzero; generic rational family only','normalization':'I4 row1=-1','coefficients':normalized,'forms':j['I4'],'common_polynomial_factor':str(gcd)},indent=2)+'\n')
print('DONE',flush=True)
