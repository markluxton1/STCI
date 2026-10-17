from pathlib import Path
import json,time
import sympy as s
p,r,z=s.symbols('p r z');x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');b=Path(__file__).parent
j=json.loads((b/'explore-mf6-principal-quartic-function-2026-10-08.json').read_text());H=s.sympify(j['H']);cs=[s.cancel(s.sympify(e)) for e in j['coefficients']];D=s.lcm_list([s.denom(e) for e in cs]);D=s.factor(D);print('common denominator',D,flush=True)
ns=[s.Poly(s.cancel(e*D),p,r,domain=s.QQ).as_expr() for e in cs]
forms=[s.sympify(e) for e in j['forms']];fu=[s.Poly(s.diff(f,x3).subs({x0:1,x1:z,x2:z**3,x3:z**4}),z) for f in forms]
a=[s.rem(s.expand(sum(n*f.nth(i) for n,f in zip(ns,fu))),H,p) for i in range(10)]
h=[]
for i in range(9):
 e=-a[i] if i==0 else -a[i]-p*h[-1]
 h.append(s.rem(s.expand(e),H,p))
assert s.rem(s.expand(a[9]+p*h[8]),H,p)==0
common=s.factor(s.gcd_list(h));h=[s.cancel(e/common) for e in h];print('coefficient gcd',common,flush=True);print('h degree',max(i for i,e in enumerate(h) if e!=0),'sizes',[len(str(e)) for e in h],flush=True)
A,B=1+r*z,1+p*z
E0=[]
for f in forms:
 uu=s.diff(f,x3,2)/2
 uv=s.diff(f,x2,x3)+s.Rational(3,2)*z*s.diff(f,x3,2)
 vv=(s.diff(f,x2,2)+3*z*s.diff(f,x2,x3)+s.Rational(9,4)*z**2*s.diff(f,x3,2))/2
 E0.append(s.Poly(s.expand((-2*r*A*uu+(-r*B-p*A)*uv-2*p*B*vv).subs({x0:1,x1:z,x2:z**3,x3:z**4})),z))
E=[s.rem(s.expand(sum(n*f.nth(i) for n,f in zip(ns,E0))),H,p) for i in range(11)]
Egcd=s.factor(s.gcd_list(E));E=[s.cancel(e/Egcd) for e in E];print('E coefficient gcd',Egcd,'sizes',[len(str(e)) for e in E],flush=True)
record={'status':'DERIVED actual first-normal coefficient, no generic squarefreeness assertion','H':str(H),'coefficient_denominator':str(D),'removed_common_factor':str(common),'h_coefficients':list(map(str,h)),'relation':'dF/dx3 along C0 = -(1+p*z)*h * removed_common_factor / coefficient_denominator','degree':8,'normalization_denominator_fibers_retained':True,'E_coefficients':list(map(str,E)),'E_coefficient_gcd':str(Egcd),'E_relation':'actual finite mixed quadratic E = recorded_E * E_coefficient_gcd / (D*(p-r))','samples':[]}
for ell,r0,p0 in [(13,0,12),(17,0,8),(23,0,5),(31,0,0),(101,0,0)]:
 if int(H.subs({p:p0,r:r0}))%ell:continue
 if int(D.subs({r:r0}))%ell==0:continue
 values=[(lambda v: int(s.numer(v))*pow(int(s.denom(v)),-1,ell)%ell)(e.subs({p:p0,r:r0})) for e in h];f=s.Poly(sum(c*z**i for i,c in enumerate(values)),z,modulus=ell)
 ef=s.Poly(sum((lambda v: int(s.numer(v))*pow(int(s.denom(v)),-1,ell)%ell)(e.subs({p:p0,r:r0}))*z**i for i,e in enumerate(E)),z,modulus=ell);gcd=s.gcd(f,f.diff());triple=s.gcd(gcd,ef);print('E gcd',str(triple.as_expr()),'Edegree',ef.degree(),flush=True);print('sample',ell,r0,p0,'degree',f.degree(),'gcddegree',gcd.degree(),'factor',s.factor_list(f.as_expr(),modulus=ell),flush=True)
 record['samples'].append({'ell':ell,'r':r0,'p':p0,'h':str(f.as_expr()),'degree':f.degree(),'gcd_degree':gcd.degree(),'E':str(ef.as_expr()),'triple_gcd':str(triple.as_expr()),'triple_gcd_degree':triple.degree(),'factorization':str(s.factor_list(f.as_expr(),modulus=ell))})
(b/'explore-mf6-principal-first-normal-filter-2026-10-08.json').write_text(json.dumps(record,indent=2)+'\n');print('DONE',flush=True)
