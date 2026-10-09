from pathlib import Path
import json
import sympy as s
p,r,z,U,V,y,m=s.symbols('p r z U V y m');x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');b=Path(__file__).parent
j=json.loads((b/'explore-mf6-principal-quartic-function-2026-10-08.json').read_text());hs=json.loads((b/'explore-mf6-principal-first-normal-filter-2026-10-08.json').read_text());forms=[s.sympify(e) for e in j['forms']]
results=[]
for ell,r0,p0 in [(13,0,12),(23,0,5),(101,2,4),(101,4,6),(103,2,30)]:
 def mod(v):
  v=s.cancel(v);return int(s.numer(v))*pow(int(s.denom(v)),-1,ell)%ell
 cs=[mod(s.sympify(e).subs({p:p0,r:r0})) for e in j['coefficients']]
 F=sum(c*f for c,f in zip(cs,forms));Fp=s.Poly(F,x0,x1,x2,x3,domain=s.QQ);F=sum(mod(c)*x0**mon[0]*x1**mon[1]*x2**mon[2]*x3**mon[3] for mon,c in Fp.terms())
 h=s.Poly(sum(mod(s.sympify(e).subs({p:p0,r:r0}))*z**i for i,e in enumerate(hs['h_coefficients'])),z,modulus=ell)
 print('sample',ell,r0,p0,'hfactor',s.factor_list(h.as_expr(),modulus=ell),flush=True)
 roots=[z0 for z0 in range(ell) if h.eval(z0)%ell==0 and h.diff().eval(z0)%ell==0]
 A=1+r0*z;B=1+p0*z;bs=mod(s.Rational(p0,p0-r0));bt=mod(s.Rational(-r0,p0-r0))
 raw=s.Poly(s.expand(F.subs({x0:1,x1:z,x2:z**3+V,x3:z**4+U+mod(s.Rational(3,2))*z*V})),U,V,z,modulus=ell)
 # remod before coordinate substitution to avoid enormous rational coefficients.
 raw=s.Poly(raw.as_expr().subs({U:bt*m+A*y,V:-bs*m+B*y}),m,y,z,modulus=ell)
 def coeff(da,db):return s.Poly(sum(int(c)*z**dz for (dm,dy,dz),c in raw.terms() if dm==da and dy==db),z,modulus=ell)
 hactual=coeff(1,0);Q=coeff(0,2);E=coeff(1,1);R=coeff(2,0);K=coeff(0,3)
 P=2*p0+12*r0*r0+16*r0+9;delta=(2*r0+1)*(8*p0+12*r0*r0+4*r0+3)-p0*P*z
 for z0 in roots:
  row={'ell':ell,'r':r0,'p':p0,'z':z0,'h':int(hactual.eval(z0))%ell,'h1':int(hactual.diff().eval(z0))%ell,'h2':mod(hactual.diff().diff().eval(z0)/s.Integer(2)),'Q':int(Q.eval(z0))%ell,'E':int(E.eval(z0))%ell,'R':int(R.eval(z0))%ell,'K':int(K.eval(z0))%ell,'delta':int(delta.subs(z,z0))%ell};results.append(row);print(row,flush=True)
(b/'explore-mf6-principal-modular-jets-2026-10-08.json').write_text(json.dumps({'status':'MODULAR OBSERVATIONS only','rows':results},indent=2)+'\n')
