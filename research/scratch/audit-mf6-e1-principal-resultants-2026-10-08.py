from pathlib import Path
import json,time
import sympy as s
p,r=s.symbols('p r');b=Path(__file__).parent;j=json.loads((b/'audit-mf6-e1-principal-raw-minors-2026-10-08.json').read_text());H=s.sympify(j['H']);out=[]
for m in j['minors'][:2]:
 f=s.sympify(m['factors'][-1][0]);tick=time.monotonic();q=s.resultant(H,f,p)
 print('resultant',m['omitted'],'seconds',time.monotonic()-tick,'degree',s.degree(q,r),flush=True)
 fac=s.factor_list(q);print('factors',[(s.degree(f,r),n) for f,n in fac[1]],flush=True)
 out.append({'omitted':m['omitted'],'resultant':str(q),'coefficient':str(fac[0]),'factors':[[str(f),int(n)] for f,n in fac[1]]})
 (b/'audit-mf6-e1-principal-resultants-2026-10-08.json').write_text(json.dumps({'resultants':out},indent=2)+'\n')
if len(out)==2:
 gcd=s.factor(s.gcd(s.sympify(out[0]['resultant']),s.sympify(out[1]['resultant'])))
 print('RESULTANT GCD',gcd,flush=True)
