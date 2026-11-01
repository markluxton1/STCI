"""Corrected exact finite-pair center gate for the toric source.

The script verifies the PGL2 orbit formula, the generic residual polynomial,
its symmetric coefficient formulas, the Q(P)=0 stratum, the infinity fiber,
and the d=0 finite-center divisibility test. It leaves the exact remaining
incidence on U0*V1*V2*M=0 explicit rather than claiming its exclusion.
"""
import json
import sys
import sympy as s

u,v,r,q,t,l,m,n=s.symbols('u v r q t l m n')
U,V=u+v,q*u+r*v
pe=[s.Poly(f,u,v).coeff_monomial(u**2*v**2)
    for f in (U**4,U**3*V,U**2*V**2,U*V**3,V**4)]
expected=[6,3*(r+q),r**2+4*r*q+q**2,3*r*q*(r+q),6*r**2*q**2]
assert all(s.expand(x-y)==0 for x,y in zip(pe,expected))
assert s.det(s.Matrix([[1,1],[q,r]]))==r-q
p0,p1,p2,p3,p4=expected
a=p3; b=p0+p1; c=p1+p2; d=p2+p3; e=p2+2*p3+p4

# Marked source point c(t) and arbitrary projection fiber line c(t)+lambda P.
Ac=t; Bc=t**3*(t+1); Cc=t**2*(t+1); Dc=t*(t+1); Ec=(t+1)**2
AA=Ac+l*a; BB=Bc+l*b; CC=Cc+l*c; DD=Dc+l*d; EE=Ec+l*e
Qline=s.expand(BB*DD-CC**2)
Rline=s.expand(AA*EE*CC-DD**3)
Tline=s.expand(AA*BB*EE-CC*DD**2)
K=s.factor(b*d-c**2)
H=s.expand(d*t**2-2*c*t+b)
L=t*(t+1)*H
assert s.expand(Qline-l*(L+l*K))==0

# Symmetric coordinates and source-center invariants.
def symmetric(expr):
    form,rem,_=s.symmetrize(s.factor(expr),[r,q],formal=True)
    assert s.factor(rem)==0
    return s.factor(form.subs({s.Symbol('s1'):m,s.Symbol('s2'):n}))
Kmn=symmetric(K)
K0=m**2-n+3*m+3
dmn=m**2+2*n+3*m*n
N=m**4+6*m**3*n+9*m**2*n**2+m**2*n+9*m*n**3-6*m*n**2-2*n**2
Disc=m**2-4*n
assert s.factor(Kmn+Disc*K0)==0
Rpoint=s.factor(3*m*n*(m**2+2*n+6*m*n+6*n**2)*(m**2+2*n+3*m)-dmn**3)
assert s.factor(Rpoint+Disc*N)==0

# Solve Q=0 on the nonzero-lambda branch and compute generic common residual W.
lam=s.factor(-L/K)
FR=s.together((Rline/l).subs(l,lam)).as_numer_denom()[0]
FT=s.together((Tline/l).subs(l,lam)).as_numer_denom()[0]
common=s.factor(s.gcd(s.Poly(FR,t),s.Poly(FT,t)).as_expr())
W=s.factor(common/(t*(t+1)*(r-q)**2))
Wpoly=s.Poly(W,t)
assert Wpoly.degree()==5
Wcoeff={}
Wrems={}
for i in range(6):
    coeff=Wpoly.coeff_monomial(t**i)
    form,rem,_=s.symmetrize(s.factor(coeff),[r,q],formal=True)
    Wrems[str(i)]=str(s.factor(rem))
    assert s.factor(rem)==0
    Wcoeff[i]=s.factor(form.subs({s.Symbol('s1'):m,s.Symbol('s2'):n}))
Wmn=sum(Wcoeff[i]*t**i for i in range(6))

U0=m**4+4*m**2*n+4*n**2+3*m**3+6*m*n+3*m**2-12*n
V1=m**2+2*n+6*m+6
V2=m**2+2*n+6*m*n+6*n**2
M=(11*m**4+15*m**3*n+36*m**3+21*m**2*n**2+8*m**2*n+39*m**2
   +9*m*n**3+30*m*n**2-45*m*n+27*m+6*n**3+8*n**2-30*n+18)
assert s.factor(Wcoeff[5]-dmn*N)==0
assert s.factor(Wmn.subs(t,0)-K0*U0)==0
assert s.factor(Wmn.subs(t,-1)+K0*V1*V2)==0
ResRaw=s.factor(s.resultant(W,H,t))
Res=symmetric(ResRaw)
assert s.factor(Res-Disc**4*dmn**2*K0**3*M)==0

# Full-inverse point at the projective parameter infinity.
# c_infinity=(0,1,0,0,0), so Q(c_inf+lambda P)=lambda(d+lambda K),
# R(c_inf+lambda P)=lambda^3 R(P). The toric syzygy B*R-C*T+D^2*Q=0
# shows T also vanishes at lambda=-d/K whenever R(P)=0 and d!=0.
AAi=l*a; BBi=1+l*b; CCi=l*c; DDi=l*d; EEi=l*e
Qinf=s.factor(BBi*DDi-CCi**2)
Rinf=s.factor(AAi*EEi*CCi-DDi**3)
assert s.expand(Qinf-l*(d+l*K))==0
assert s.factor(Rinf-l**3*(a*e*c-d**3))==0

# On d=0, n=-m^2/(3m+2). K!=0 and r!=q imply m not in {0,-1,-2};
# then W has degree 4. Exact remainder condition W | [t(t+1)H]^5
# reduces to a scalar gcd whose only parameter root is m=-2 (diagonal).
nd=-m**2/(3*m+2)
W_d=s.factor(Wmn.subs(n,nd))
# Rewrite H directly in symmetric coordinates on this stratum.
bm=3*(m+2); cm=m**2+2*nd+3*m; dm=s.factor(m**2+2*nd+3*m*nd)
Hd=s.factor(dm*t**2-2*cm*t+bm)
Ld=t*(t+1)*Hd
rem_d=s.rem(s.Poly(Ld**5,t),s.Poly(W_d,t)).as_expr()
remnums=[s.together(c0).as_numer_denom()[0] for c0 in s.Poly(rem_d,t).all_coeffs()]
rem_gcd=s.factor(s.gcd_list(remnums))
assert s.factor(dm)==0
assert s.factor(rem_gcd/(m+2)**5) != 0
assert s.factor(rem_gcd)==243*(m+2)**5
# On the d=0 relation, K0=3(m+1)^2(m+2)/(3m+2),
# Disc=3m^2(m+2)/(3m+2): K!=0 and r!=q exclude m=-1,-2 and m=0.
assert s.factor(K0.subs(n,nd)-3*(m+1)**2*(m+2)/(3*m+2))==0
assert s.factor(Disc.subs(n,nd)-3*m**2*(m+2)/(3*m+2))==0

# Q(P)=0 (K=0) finite-pair exclusion.
# b=0 and K0=0 force m=-2,n=1 (r=q=-1); c=0 and K0=0 give
# (-2,1) or (-1,1). The latter has P=(-3,3,0,0,3), T(P)=-27,
# and t=0,lambda=-1/3 gives [1:-1:0:0:0] on X.
bm=3*(m+2); cm=m**2+2*n+3*m
assert s.solve([K0,bm],[m,n],dict=True)==[{m:-2,n:1}]
assert set((sol[m],sol[n]) for sol in s.solve([K0,cm],[m,n],dict=True))=={(-2,1),(-1,1)}
Pspecial=(-3,3,0,0,3)
Qspecial=Pspecial[1]*Pspecial[3]-Pspecial[2]**2
Rspecial=Pspecial[0]*Pspecial[4]*Pspecial[2]-Pspecial[3]**3
Tspecial=Pspecial[0]*Pspecial[1]*Pspecial[4]-Pspecial[2]*Pspecial[3]**2
assert (Qspecial,Rspecial,Tspecial)==(0,0,-27)
extra=(1,-1,0,0,0)
assert (extra[1]*extra[3]-extra[2]**2,
        extra[0]*extra[4]*extra[2]-extra[3]**3,
        extra[0]*extra[1]*extra[4]-extra[2]*extra[3]**2)==(0,0,0)

record={
 "execution":{"command":f"python3 {__file__}",
              "python":sys.version.split()[0],"sympy":s.__version__},
 "orbit_formula":{"GL2_change":"U=u+v, V=q*u+r*v","coefficient_u2v2":[str(x) for x in pe],
                   "determinant":"r-q","symmetric_parameters":"m=r+q, n=r*q"},
 "center":{"a":"3*m*n","b":"3*(m+2)","c":"m^2+2*n+3*m","d":"m^2+2*n+3*m*n",
           "e":"m^2+2*n+6*m*n+6*n^2","K_QP":str(Kmn)},
 "R_at_center":str(Rpoint),
 "generic_W_coefficients_low_to_high":{str(i):str(Wcoeff[i]) for i in range(6)},
 "symmetrize_remainders":Wrems,
 "W_leading":str(Wcoeff[5]),"W_at_0":str(s.factor(Wmn.subs(t,0))),
 "W_at_minus1":str(s.factor(Wmn.subs(t,-1))),"resultant_W_H":str(Res),
 "corrected_generic_extra_point_gate":"For finite distinct r,q with K!=0 and d*N*U0*V1*V2*M!=0, W has degree 5 and no root in {0,-1} union {H=0}; hence a finite off-c inverse point exists.",
 "finite_exception_factors":{
   "d":"m^2+2*n+3*m*n","N":str(N),"U0":str(U0),"V1":str(V1),"V2":str(V2),"M":str(M)},
 "infinity_fiber":{"Q":"lambda*(d+lambda*K)","R":"lambda^3*R(P)",
   "extra_condition":"d!=0 and R(P)=0, equivalently d!=0 and N=0 for r!=q."},
 "d_zero_curve":"n=-m^2/(3*m+2); W has degree 4 for admissible distinct centers. Numerators of rem_t([t(t+1)H]^5,W) have gcd 243*(m+2)^5, whose only root m=-2 is diagonal; thus no full inverse support on d=0.",
 "Q_P_zero":"All admissible finite distinct-pair centers on Q(P)=0 have an extra point, by the explicit cases in the accompanying message.",
 "exact_remaining_finite_incidence":"Only U0*V1*V2*M=0 with Disc*K0*d*N!=0 remains. For each such specialization, let W_actual be the common residual gcd of the specialized R/l,T/l after lambda=-t(t+1)H/K, with universal t(t+1) factors removed. Full inverse support is equivalent to W_actual!=0 and rad(W_actual) dividing rad(t(t+1)H); when deg W_actual<=5 this is W_actual | [t(t+1)H]^5. No classification of this residual incidence is claimed.",
 "scope":"Finite distinct-pair orbit chart only; one-infinity chart is handled separately."
}
print(json.dumps(record,indent=2))
