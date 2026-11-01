"""Root-support diagnostics on U0, V1, V2; M remains unresolved.

Review status and remaining coverage are recorded in the companion research note.
"""
import json,sys,sympy as s
from pathlib import Path
m,n,t,k=s.symbols('m n t k')
data=json.loads(Path(__file__).with_name('quintic_toric_finite_centers.json').read_text())
W=s.expand(sum(s.sympify(v,locals={'m':m,'n':n})*t**int(i)
               for i,v in data['generic_W_coefficients_low_to_high'].items()))
d=m**2+2*n+3*m*n
H=d*t**2-2*(m**2+2*n+3*m)*t+3*(m+2)
D=t*(t+1)*H
Delta=m**2-4*n; K0=m**2-n+3*m+3
N=m**4+6*m**3*n+9*m**2*n**2+m**2*n+9*m*n**3-6*m*n**2-2*n**2
U0=m**4+4*m**2*n+4*n**2+3*m**3+6*m*n+3*m**2-12*n
V1=m**2+2*n+6*m+6
V2=m**2+2*n+6*m*n+6*n**2

def support_rem_gcd(sub):
    w=s.Poly(s.cancel(W.subs(sub)),t,domain='EX')
    z=s.Poly(s.cancel((D*s.diff(W,t)).subs(sub)),t,domain='EX')
    rem=s.rem(z,w)
    nums=[s.fraction(s.cancel(c))[0] for c in rem.all_coeffs()]
    return s.factor(s.gcd_list(nums)), s.factor(w.as_expr())

# In characteristic zero, for nonzero W, Supp(W) subset Supp(D)
# iff W divides D*W': at a root of W of multiplicity e, W' has order e-1.
# V1 is a graph over m.
g1,w1=support_rem_gcd({m:k,n:-(k**2+6*k+6)/2})
assert s.factor(g1-81*(k+2)**4)==0 and s.Poly(g1,k).degree()>0
assert s.factor(g1-81*(k+2)**4)==0
v1cand={m:-2,n:s.Integer(1)}
assert s.factor(Delta.subs(v1cand))==0

# V2 conic from (0,0); handle m=0 separately.
sub2={m:-2*k/(1+6*k+6*k**2),n:-2*k**2/(1+6*k+6*k**2)}
g2,w2=support_rem_gcd(sub2)
assert s.factor(g2-81*(2*k+1)**4*(10*k**2+6*k+1))==0
v2zero={m:0,n:0}; v2half={m:-2,n:1}
assert s.factor(Delta.subs(v2zero))==0 and s.factor(Delta.subs(v2half))==0
root_poly=10*k**2+6*k+1
mroot=s.factor(sub2[m]); nroot=s.factor(sub2[n])
assert s.rem(s.together(K0.subs({m:mroot,n:nroot})).as_numer_denom()[0],root_poly,k)==0
v2miss={m:0,n:-s.Rational(1,3)}
assert s.factor(V2.subs(v2miss))==0
miss_gcd,wm=support_rem_gcd(v2miss)
assert miss_gcd==800

# U0 conic rational parametrization from the point (m,n)=(0,3).
# Let x=m^2+2n, y=2x+3m-6, then y^2=-27m^2-36m+36 and y=6+k*m.
mu=s.factor(-12*(k+3)/(k**2+27))
yu=s.factor(6+k*mu)
xu=s.factor(6+(k-3)*mu/2)
nu=s.factor((xu-mu**2)/2)
assert s.factor(U0.subs({m:mu,n:nu}))==0
g0,w0=support_rem_gcd({m:mu,n:nu})
assert s.factor(g0-139968*(k-3)**3*(k+3)*(k**2-12*k+63))==0
assert s.factor(g0.subs(k,3))==0 and s.factor(g0.subs(k,-3))==0
ucand={m:-2,n:1}
assert s.factor(Delta.subs(ucand))==0
u_tangent={m:0,n:3}; u_infty={m:0,n:0}
assert s.factor(K0.subs(u_tangent))==0 and s.factor(Delta.subs(u_infty))==0
Knum=s.together(K0.subs({m:mu,n:nu})).as_numer_denom()[0]
assert s.rem(Knum,k**2-12*k+63,k)==0

out={
 'execution':{'command':f'python3 {__file__}',
              'python':sys.version.split()[0],'sympy':s.__version__},
 'root_support_criterion':'In char 0, for nonzero W and D=t(t+1)H, Supp(W) subset Supp(D) iff W divides D*dW/dt. For each root alpha of multiplicity e in W, ord_alpha(Wprime)=e-1, so divisibility is equivalent to D(alpha)=0.',
 'U0':{'param':'m=-12(k+3)/(k^2+27), x=m^2+2n, y=2x+3m-6=6+km, n=(x-m^2)/2',
       'coefficient_gcd_of_remainder_DWprime_mod_W':str(g0),'candidate_roots':'k=3 gives (m,n)=(-2,1), Delta=0; k=-3 gives (0,3), K0=0; roots of k^2-12k+63 have K0=0',
       'parameter_boundary':'k tends to infinity at the affine point (m,n)=(0,0), where Delta=0; k^2+27=0 are parameter poles and give no finite affine center'},
 'V1':{'param':'m=k, n=-(k^2+6k+6)/2','coefficient_gcd_of_remainder_DWprime_mod_W':str(g1),
       'only_candidate':'k=-2 gives (m,n)=(-2,1), Delta=0'},
 'V2':{'param':'m=-2k/(1+6k+6k^2), n=km (covers m!=0)',
       'coefficient_gcd_of_remainder_DWprime_mod_W':str(g2),
       'candidate_roots':'k=-1/2 gives (-2,1), Delta=0; roots of 10k^2+6k+1 have K0=0; k=0 is not a zero of the remainder gcd',
       'omitted_affine_point':{'point':'(m,n)=(0,-1/3)','coefficient_gcd_of_remainder_DWprime_mod_W':str(miss_gcd),'W_specialized':str(wm)}},
 'conclusion':'The specialized universal W fails the root-support criterion at every point of U0,V1,V2 satisfying the reviewed open conditions Delta*K0*d*N!=0. At the only candidate roots, a displayed open-condition factor vanishes. M=0 remains unresolved; no finiteness or emptiness conclusion is certified by this script.',
 'scope':'Finite distinct-pair chart only; separate one-infinity chart untouched.'}
print(json.dumps(out,indent=2))
