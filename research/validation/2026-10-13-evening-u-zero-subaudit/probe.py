from pathlib import Path
import sympy as s
import json,hashlib,time
start=time.time()
d,a,B,G,J,p,q,D,r,T,tt=s.symbols('delta a B G J p q D r T tt')
path=Path('research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt')
F=s.sympify(path.read_text().replace('^','**'),locals={'delta':d,'a':a,'B':B,'G':G,'J':J,'p':p})
Bs=(D-d*d)/q; aas=d/q+2*d*d/q**2-D/q**2
Gs=-(3-q)*D; Js=q*(2-q)*D
sub={a:aas,B:Bs,G:Gs,J:Js}
Pc=q*q-6*q+6; P6=q*q-3*q+3
L1=3*(d+d*d/q)*(q-1)**2*Pc+d*q*(3-2*q)*Pc-3*d*d*(q-1)**2*(q-3)
L2=3*q*(q-1)*(2*d*(q-1)+q*(q-2))*(d+d*d/q)**2-6*d*q*(q-1)*(d*d+d*(3*q-4)+q*(q-2))*(d+d*d/q)+d**5*q+3*d**4*(q-1)*(3*q-2)+6*d**3*q*(q-1)*(2*q-3)+3*d*d*q*q*(q-1)*(q-2)
print('L1_U',s.factor(L1),flush=True); print('L2_U',s.factor(L2),flush=True)
cs={}
for n in range(1,5):
    cn=s.factor(s.diff(F,p,n).subs({p:q}).subs(sub,simultaneous=True)/s.factorial(n))
    cs[n]=cn
    print('taylor',n,cn,flush=True)
A2=((3*d*d+G)*q*(2-q)+J*(3-q))*r*r+d*(d*d*q*(q-3)+3*B*q*(2-q)+G*(2-q)-J)*r+d*d*(B*q*(q-3)-G)
print('A2U',s.factor(A2.subs(sub,simultaneous=True)),flush=True)
rs=d*(3-q)/(3*(2-q)); Ts=d*d*P6/(9*(2-q)**2)
J0=q*T*T+(d*r+B-q*(2*r*r+r-a))*T+r**3*(q*r-d)
E=s.factor(J0.subs(sub,simultaneous=True).subs({r:rs,T:Ts},simultaneous=True))
print('offdiag J0',E,flush=True)
print('Js_U',Js,flush=True)
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'frozen_F_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'coefficients':{str(n):str(c) for n,c in cs.items()},'L1U':str(s.factor(L1)),'L2U':str(s.factor(L2)),'offdiagonal_J0':str(E),'elapsed_seconds':time.time()-start}
Path('research/validation/2026-10-13-evening-u-zero-subaudit/probe-artifacts.json').write_text(json.dumps(out,indent=2)+'\n')
