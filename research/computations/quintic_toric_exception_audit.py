"""Independent specialization audit for the three exceptional center curves.

Print exact denominator, leading-coefficient and parameter-boundary evidence;
verify the universal residual-factor identities used by the companion note.
No calculation on the remaining M locus is performed.
"""
import json, sympy as s, hashlib
from pathlib import Path
m,n,k,t,l=s.symbols('m n k t l')
p=Path(__file__).with_name('quintic_toric_finite_centers.json')
audit=Path(__file__).with_name('quintic_toric_exception_centers.py')
print('SHA256_INPUT',hashlib.sha256(p.read_bytes()).hexdigest(),flush=True)
print('SHA256_SCRIPT',hashlib.sha256(audit.read_bytes()).hexdigest(),flush=True)
data=json.loads(p.read_text()); W=s.expand(sum(s.sympify(v,locals={'m':m,'n':n})*t**int(i) for i,v in data['generic_W_coefficients_low_to_high'].items()))
Delta=m*m-4*n; K0=m*m-n+3*m+3; d=m*m+2*n+3*m*n
N=m**4+6*m**3*n+9*m*m*n*n+m*m*n+9*m*n**3-6*m*n*n-2*n*n
H=d*t*t-2*(m*m+2*n+3*m)*t+3*(m+2); D=t*(t+1)*H
subs={'V1':{m:k,n:-(k*k+6*k+6)/2},'V2':{m:-2*k/(1+6*k+6*k*k),n:-2*k*k/(1+6*k+6*k*k)}}
mu=-12*(k+3)/(k*k+27); xu=6+(k-3)*mu/2
subs['U0']={m:mu,n:s.factor((xu-mu*mu)/2)}
for name,sub in subs.items():
 print(name,'m,n',*[str(s.factor(sub[x])) for x in (m,n)],flush=True)
 for expr,label in ((Delta,'Delta'),(K0,'K0'),(d,'d'),(N,'N'),(d*N,'LC_W')):
  print(name,label,s.factor(expr.subs(sub)),flush=True)
 w=s.Poly(s.cancel(W.subs(sub)),t); z=s.Poly(s.cancel((D*s.diff(W,t)).subs(sub)),t)
 rem=s.Poly(s.rem(z,w),t)
 den=s.factor(s.lcm_list([s.fraction(s.cancel(c))[1] for c in rem.all_coeffs()]))
 print(name,'W_degree',w.degree(),'W_coeff_den_lcm',s.factor(s.lcm_list([s.denom(s.cancel(c)) for c in w.all_coeffs()])),flush=True)
 print(name,'REM_den_lcm',den,flush=True)
 nums=[s.fraction(s.cancel(c))[0] for c in rem.all_coeffs()]
 print(name,'REM_num_gcd',s.factor(s.gcd_list(nums)),flush=True)
print('PARAM_POLE_GCD_U0',s.gcd(k*k+27,k+3),flush=True)
print('PARAM_POLE_GCD_V2',s.gcd(1+6*k+6*k*k,k),flush=True)
a=3*m*n; b=3*(m+2); c=m*m+2*n+3*m; e=m*m+2*n+6*m*n+6*n*n; K=-Delta*K0
Ac=t; Bc=t**3*(t+1); Cc=t*t*(t+1); Dc=t*(t+1); Ec=(t+1)**2
A=Ac+l*a; B=Bc+l*b; C=Cc+l*c; DD=Dc+l*d; E=Ec+l*e
for name,expr in [('R',A*E*C-DD**3),('T',A*B*E-C*DD**2)]:
 poly=s.Poly(s.expand(expr),l)
 assert poly.nth(0)==0
 cleared=s.expand(K*K*poly.nth(1)-K*D*poly.nth(2)+D*D*poly.nth(3))
 quo,rem=s.div(cleared,s.expand(t*(t+1)*W),t)
 assert s.expand(rem)==0
 print('UNIVERSAL_FACTOR',name,'K^2*(equation/l) at l=-D/K = t(t+1)W *',s.factor(quo),flush=True)

# Complete affine parameter coverage and the separately tested omitted point.
assert s.factor(s.Poly(W,t).LC()-d*N)==0
U0=m**4+4*m*m*n+4*n*n+3*m**3+6*m*n+3*m*m-12*n
V1=m*m+2*n+6*m+6; V2=m*m+2*n+6*m*n+6*n*n
for name,eq in [('U0',U0),('V1',V1),('V2',V2)]:
 assert s.factor(eq.subs(subs[name]))==0
 print(name,'param_identity=0')
x=m*m+2*n; y=2*x+3*m-6
assert s.expand(y*y+27*m*m+36*m-36-4*U0)==0
print('U0 conic transform exact')
for name,pt in [('U0_base',{m:0,n:3}),('U0_infinity',{m:0,n:0}),('V2_origin',{m:0,n:0}),('V2_omitted',{m:0,n:-s.Rational(1,3)})]:
 print(name,'Delta,K0,d,N=',*[str(s.factor(e.subs(pt))) for e in [Delta,K0,d,N]])
 if name=='V2_omitted':
  w=s.Poly(W.subs(pt),t); z=s.Poly((D*s.diff(W,t)).subs(pt),t)
  rem=s.rem(z,w)
  print('W_omitted=',s.factor(w.as_expr()))
  print('D_omitted=',s.factor(D.subs(pt)))
  print('REM_omitted=',s.factor(rem.as_expr()))
  print('GCD_numerators=',s.gcd_list([s.fraction(s.cancel(c))[0] for c in rem.all_coeffs()]))
print('PASS')
