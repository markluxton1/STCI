"""Discover exact ideal-membership witnesses; not a sampling computation."""
import json,sympy as s
from pathlib import Path
alpha,beta,z=s.symbols('alpha beta z')
A,B=alpha+12,beta+4
R=A+B*(z-2)+z*z-2*z+4;delta=z*(z+2)*R+16
C=-2*z**11+9*z**10-12*z**9;D=-z**12/2+z**11
P=7*z**9/16-25*z**8/8+9*z**7-14*z**6+19*z**5-18*z**4
J=s.Poly(s.expand(3*R*delta*C+3*(s.diff(R,z)*delta-R*s.diff(delta,z))*D+8*delta**2*P),z)
boundary=s.Matrix([[J.nth(18-i),J.nth(17-i)] for i in range(5,9)])
minors=[s.expand(boundary[[i,k],:].det()) for i in range(4) for k in range(i+1,4)]
targets=[alpha**2,alpha*beta,beta**2]
for d in range(5):
 ms=[alpha**i*beta**j for i in range(d+1) for j in range(d+1-i)]
 cols=[s.Poly(p*m,alpha,beta) for p in minors for m in ms]
 monoms=sorted(set(mon for p in cols for mon,c in p.terms()))
 mat=s.Matrix([[p.coeff_monomial(alpha**i*beta**j) for p in cols] for i,j in monoms])
 vecs=[s.Matrix([s.Poly(t,alpha,beta).coeff_monomial(alpha**i*beta**j) for i,j in monoms]) for t in targets]
 if mat.rank()!=mat.row_join(s.Matrix.hstack(*vecs)).rank():
  print('not enough degree',d,mat.shape,flush=True);continue
 witnesses=[]
 for target,vec in zip(targets,vecs):
  sol,params=mat.gauss_jordan_solve(vec)
  sol=sol.subs({p:0 for p in params})
  ws=[s.expand(sum(sol[i*len(ms)+k]*m for k,m in enumerate(ms))) for i in range(6)]
  assert s.expand(sum(w*p for w,p in zip(ws,minors))-target)==0
  witnesses.append(ws)
 print('FOUND DEGREE',d,flush=True)
 for ws in witnesses: print(ws,flush=True)
 out=Path(__file__).with_name('session-mf6-minor-membership.json')
 out.write_text(json.dumps({'variables':['alpha','beta'],'minors':list(map(str,minors)),'targets':list(map(str,targets)),'witnesses':[list(map(str,ws)) for ws in witnesses],'coefficient_degree':d},indent=2)+'\n')
 break
else: print('No witness found within degree4',flush=True)
