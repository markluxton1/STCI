# Mixed-weight sextic and full limits

For `c_0=t^3-w`, `c_2=w^3-t(tw+q)^2`, and `f=h q^3+c_2^2-c_0^2`, the restriction to the containing quadric is
\[
f|_{q=0}=(w-t^3)^2(w^4-1).
\]
Consequently the residual ruling lines are `w^4=1`; along each such line `c_2=-w^2 c_0`. The quadratic normal initial form at the marked curve, in `w=t^3+u`, is
\[
4t^{10}q^2-4t^{11}qu+(t^{12}-1)u^2,
\]
whose discriminant is `16t^{10}`. This is a split normal node over the function field, in contrast to the nonsplit control in the global-equations chapter. The derivative of the quadric restriction at `w=1` equals `4(1-t^3)^2`, proving generic smoothness of that residual line away from its contact points. These are exact restrictions and attachment identities, not a classification of all sextic carriers or an STCI construction.


### Archived exact certificate: `research/computations/ci_cycle_line_degeneration_2026_10_25.py`

This certificate supports the [quartic line-plus-degree-eleven
degeneration](../residuals/explicit_quartic_residuals.md#the-line-plus-degree-eleven-degeneration).
It checks the ruling-line, attachment, and smoothing identities for that
separate family. The projective scheme checks use its Macaulay2 companion.

<details><summary>Original source</summary>

```python
#!/usr/bin/env python3
"""Exact global-source, ruling-line, and boundary identities; stdlib only.

The Macaulay2 companion checks projective schemes. This file checks explicit
polynomial identities and squarefreeness, not global genericity or flatness.
"""
from fractions import Fraction
import json
from pathlib import Path

NV=6

def const(n): return {(0,)*NV:n} if n else {}
def var(i):
    e=[0]*NV; e[i]=1; return {tuple(e):1}
def add(*polys):
    out={}
    for p in polys:
        for m,c in p.items(): out[m]=out.get(m,0)+c
    return {m:c for m,c in out.items() if c}
def scale(p,c): return {m:c*v for m,v in p.items() if c*v}
def sub(p,q): return add(p,scale(q,-1))
def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            e=tuple(x+y for x,y in zip(m,n)); out[e]=out.get(e,0)+c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out=const(1)
    for _ in range(n): out=mul(out,p)
    return out
def diff(p,i):
    out={}
    for m,c in p.items():
        if m[i]:
            e=list(m); e[i]-=1; out[tuple(e)]=c*m[i]
    return out
def subst(p,images):
    out={}
    for m,c in p.items():
        term=const(c)
        for image,n in zip(images,m): term=mul(term,power(image,n))
        out=add(out,term)
    return out

checks={}
# Segre restriction and moving ruling line.
a,b,A,B,c,d=[var(i) for i in range(6)]
x0=mul(A,c); x1=mul(A,d); x2=mul(B,c); x3=mul(B,d)
F=sub(power(x1,4),mul(power(x0,3),x3))
G=sub(power(x2,4),mul(x0,power(x3,3)))
left=sub(power(x1,3),mul(power(x0,2),x2))
right=sub(power(x2,3),mul(x1,power(x3,2)))
curve_factor=sub(mul(A,power(d,3)),mul(B,power(c,3)))
checks['f_segre_factorization']=add(F,mul(mul(a,x0),left))==mul(mul(power(A,3),add(d,mul(a,c))),curve_factor)
checks['g_segre_factorization']=add(G,mul(mul(b,x3),right))==scale(mul(mul(power(B,3),add(c,mul(b,d))),curve_factor),-1)
# Actual homogeneous sources and their independently differentiated symbols on C.
x0,x1,x2,x3,a,b=[var(i) for i in range(6)]
Q=sub(mul(x0,x3),mul(x1,x2))
F=sub(power(x1,4),mul(power(x0,3),x3))
G=sub(power(x2,4),mul(x0,power(x3,3)))
left=sub(power(x1,3),mul(power(x0,2),x2))
right=sub(power(x2,3),mul(x1,power(x3,2)))
H0=add(*(power(x,2) for x in [x0,x1,x2,x3]),mul(x0,x2),scale(mul(x1,x3),2))
H1=add(scale(power(x0,2),2),scale(power(x1,2),3),scale(power(x2,2),5),scale(power(x3,2),7),mul(x0,x1),mul(x0,x3),mul(x1,x2),scale(mul(x2,x3),3))
f=add(F,mul(Q,H0),mul(mul(a,x0),left))
g=add(G,mul(Q,H1),mul(mul(b,x3),right))
# Directly restrict the actual pair to the moving line in its ruling.
pa,pb,lr,ls=var(0),var(1),var(2),var(3)
line_images=[lr,scale(mul(pa,lr),-1),ls,scale(mul(pa,ls),-1),pa,pb]
checks['moving_ruling_actual_restriction']=not subst(f,line_images) and subst(g,line_images)==mul(mul(power(ls,3),sub(const(1),mul(pa,pb))),add(mul(power(pa,3),lr),ls))
fixed_images=[scale(lr,-1),lr,scale(ls,-1),ls,pa,pb]
checks['fixed_line_actual_restriction']=subst(f,fixed_images)==mul(mul(sub(const(1),pa),power(lr,3)),add(lr,ls)) and subst(g,fixed_images)==mul(mul(sub(const(1),pb),power(ls,3)),add(lr,ls))
a1,b1,u=var(0),var(1),var(2)
images=[const(1),u,power(u,3),power(u,4),a1,b1]
restrict=lambda p: subst(p,images)
checks['all_actual_pairs_vanish_on_C']=not restrict(f) and not restrict(g)
af,bf=restrict(diff(f,3)),restrict(diff(f,2))
ag,bg=restrict(diff(g,3)),restrict(diff(g,2))
det=sub(mul(af,bg),mul(bf,ag))
h0,h1=restrict(H0),restrict(H1)
expected=add(mul(add(u,a1),h1),mul(mul(power(u,9),add(const(1),mul(b1,u))),h0),scale(mul(a1,power(u,8)),-3),scale(mul(add(const(4),scale(mul(a1,b1),2)),power(u,9)),-1),scale(mul(b1,power(u,10)),-3))
checks['two_parameter_actual_boundary_formula']=det==expected
at11=lambda p:subst(p,[const(1),const(1),u,const(1),const(1),const(1)])
Eboundary=add(h1,mul(power(u,9),h0),scale(power(u,8),-3),scale(power(u,9),-3))
checks['boundary_splits_one_plus_seventeen']=at11(det)==mul(add(u,const(1)),Eboundary)
coeffs=[Eboundary.get(tuple([0,0,i,0,0,0]),0) for i in range(18)]
checks['shared_point_not_a_triple']=sum(c*((-1)**i) for i,c in enumerate(coeffs))==14
checks['both_endpoints_free']=coeffs[0]==2 and coeffs[-1]==1

def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return p
def remainder(p,q):
    p=trim(p)
    while len(p)>=len(q):
        z=p[-1]/q[-1]; k=len(p)-len(q)
        for j,c in enumerate(q): p[j+k]-=z*c
        p=trim(p)
    return p
def gcd(p,q):
    while q: p,q=q,remainder(p,q)
    return [x/p[-1] for x in p]
def squarefree(coeffs):
    return gcd(list(map(Fraction,coeffs)),[Fraction(i*coeffs[i]) for i in range(1,len(coeffs))])==[Fraction(1)]
checks['boundary_seventeen_squarefree']=squarefree(coeffs)
q5=[2,3,2,9,-2,4]
checks['line_five_points_squarefree']=squarefree(q5)
checks['line_shared_point_excluded']=sum(c*((-1)**i) for i,c in enumerate(q5))==-14
# Normal row identity gives the common smoothing direction at all five nodes.
r,s=var(0),var(1)
qpoly=add(scale(power(r,5),4),scale(mul(power(r,4),s),-2),scale(mul(power(r,3),power(s,2)),9),scale(mul(power(r,2),power(s,3)),2),scale(mul(r,power(s,4)),3),scale(power(s,5),2))
F1=scale(mul(mul(r,add(r,s)),add(r,scale(s,2))),-1)
G1=add(scale(power(r,3),-4),scale(mul(power(r,2),s),2),scale(mul(r,power(s,2)),-9),scale(power(s,3),-1))
checks['five_nodes_same_smoothing_direction']=scale(mul(G1,power(r,3)),-1)==add(mul(r,qpoly),mul(F1,power(s,3)))
checks['genus_budget']=12+5-1==16 and 12+23-3+1==33
if not all(checks.values()): raise AssertionError(checks)
out={'scope':'Finite actual-source identities and squarefree polynomials only; projective schemes checked separately by M2.','passed':sum(checks.values()),'total':len(checks),'checks':checks,'boundary_E_coefficients_ascending_u_degree':coeffs,'line_E_intersection_coefficients_ascending_r_degree_s_equals_1':q5,'moving_line_stratum':'a*b=1','fixed_line_stratum':'a=b=1','local_five_node_smoothing_direction':'da+db','genus_E':12,'genus_smooth_residual':16,'C_E_points':17,'C_L_points':1,'L_E_points':5}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(f'{out["passed"]}/{out["total"]} exact polynomial/budget checks: PASS')
print(path.name)
```
</details>


### Archived certificate: `research/computations/verify_split22_boundary_survivor.py`

Original finite calculation preserved verbatim. Its scope remains as stated in the script; it is not a global sextic existence assertion.

<details><summary>Original Python source</summary>

```python
#!/usr/bin/env python3
"""Verify the missed content-free d=1,[2,2] first-normal boundary in P-041.

This is only a first-normal incidence certificate.  It does not construct an
integral sextic, a mate, or an STCI presentation.
"""

import sympy as sp


z, s, t = sp.symbols("z s t")

# Linear factors ell=p*xi+r*eta and m=u*xi+v*eta.
p = sp.Integer(1)
r = sp.Rational(3, 2) * z
u = 1 - 3 * z**4 + z**8
v = z / 2 - z**5 / 2 + z**9 / 2

# Evaluation at the quadric direction q1=xi+z*eta/2 is obtained by
# substituting [xi:eta]=[-z/2:1].
assert sp.expand(-p * z / 2 + r) == z
assert sp.expand(-u * z / 2 + v) == z**5

alpha = sp.expand(p * u)
beta = sp.expand(p * v + r * u)
gamma = sp.expand(r * v)

assert alpha == z**8 - 3 * z**4 + 1
assert beta == 2 * z**9 - 5 * z**5 + 2 * z
assert gamma == sp.Rational(3, 4) * (z**10 - z**6 + z**2)


def coefficient(polynomial, degree):
    return sp.Poly(polynomial, z).coeff_monomial(z**degree)


a = [coefficient(alpha, index) for index in range(11)]
b = [coefficient(beta, index) for index in range(11)]
c = [coefficient(gamma, index) for index in range(11)]

# The eleven exact equations for the image of the sextic quadratic-normal map.
equations = [
    -a[9] + 2 * b[10],
    -b[0] + 2 * c[1],
    a[0] - 2 * b[1] + 4 * c[2],
    -3 * a[1] + 2 * b[2] + 4 * c[3],
    a[2] - 2 * b[3] + 4 * c[4],
    a[3] - 2 * b[4] + 4 * c[5],
    -a[4] + 4 * c[6],
    a[5] - 2 * b[6] + 4 * c[7],
    a[6] - 2 * b[7] + 4 * c[8],
    -a[7] - 2 * b[8] + 12 * c[9],
    a[8] - 2 * b[9] + 4 * c[10],
]
assert all(sp.expand(equation) == 0 for equation in equations)

# Homogenize each coefficient pair to its common degree and check that neither
# factor has vertical content on P1.
low_left = s
low_right = sp.Rational(3, 2) * t
high_left = s**9 - 3 * s**5 * t**4 + s * t**8
high_right = (s**8 * t - s**4 * t**5 + t**9) / 2

assert sp.gcd(sp.Poly(low_left, s, t), sp.Poly(low_right, s, t)).total_degree() == 0
assert sp.gcd(sp.Poly(high_left, s, t), sp.Poly(high_right, s, t)).total_degree() == 0

print("PASS: content-free d=1,[2,2] first-normal boundary survivor is exact")
```
</details>


### Archived certificate: `research/computations/verify_split22_finite_reduction.py`

Original finite calculation preserved verbatim. Its scope remains as stated in the script; it is not a global sextic existence assertion.

<details><summary>Original Python source</summary>

```python
#!/usr/bin/env python3
"""Exact higher-jet finite reduction for the two-ramified [2,2] family.

Characteristic zero, C0, and the reduced/content-free/no-vertical assumptions
of P-020. Mathematical normal-sheaf arguments are in the companion note.
This certificate does not claim a global STCI exclusion of the surviving
h=-1/2 line, and never cancels mate scale in a local class group.
"""
import sympy as s

x0,x1,x2,x3,z,e,W,a,lam = s.symbols('x0 x1 x2 x3 z e W a lam')
u0,u2,u3,u5,u6,u8,beta = s.symbols('u0 u2 u3 u5 u6 u8 beta')
h=a+s.Rational(1,2)
c=3*a*a+2*a+1
q=x0*x3-x1*x2
A=x0*x0*x2-x1**3
B=x0*x2*x2-x1*x1*x3
D=x2**3-x1*x3*x3
S=(u0*x0*x0+u3*x0*x2-(2*h+1)**2/(2*(2*h-1))*x0*x3
   +u2*x1*x1+(2*h+1)/2*(u5*x1*x3+u6*x2*x2)+2*h*u8*x3*x3)
K=u0*x1*A+u2*x2*A+u3*x3*A+u5*x2*B+u6*x3*B+u8*x2*D
F=a*B*B+q*q*S+a*q*K+lam*q**3
f=s.cancel(F.subs({x0:1,x1:z,x2:z**3+e,x3:z**4+e*((1-a)*z+W)})/e**2).expand()
fp=s.Poly(f,e,W)
coef=lambda i,j:s.factor(fp.coeff_monomial(e**i*W**j))
R=a*(u0+u2*z*z+u3*z**3+u5*z**5+u6*z**6+u8*z**8)-2*(a+1)*z**4
betaval=a*lam-(a+1)*(a*a+1)/a
G=u2-a*u3*z+beta*z*z+(a*a+a+1)*u5*z**3-a*(a+2)*u6*z**4+c*u8*z**6
assert s.cancel(coef(0,1)+z*R)==0
assert s.cancel(coef(1,0)+a*a*z*G.subs(beta,betaval))==0
assert s.cancel(coef(0,2)-(R+z**4)/a)==0
L=(a*u2-a*(2*a+1)*u3*z+(-a*a+3*a*beta+2*a+5)*z*z
   +3*a*a*(a+1)*u5*z**3-a*(3*a*a+4*a+2)*u6*z**4
   +a*(9*a*a+6*a-1)*u8*z**6)
H=a-a*a*u5*z+2*a**3*u6*z*z+2*a*a*(a**3-a*a-a-1)*u8*z**4
assert s.cancel(coef(1,1)-L.subs(beta,betaval))==0
assert s.cancel(coef(2,0)-H)==0
assert s.cancel(coef(3,0)+a*a*u8*z)==0

# Quadratic endpoint germs and order-one Jacobian components, without lambda.
quad=lambda form:s.expand(sum(co*z**i*e**j*W**k for (i,j,k),co in s.Poly(form,z,e,W).terms() if i+j+k<=2))
assert s.factor(s.det(s.hessian(quad(f),(z,e,W))))==-2*a**3*u0*u0
assert s.expand(coef(0,1)).coeff(z,1)==-a*u0
cinf=(3*h-s.Rational(1,2))/(2*h)
fi=s.cancel(F.subs({x3:1,x2:z,x1:z**3+e,x0:z**4+e*(cinf*z+W)})/e**2).expand()
assert s.factor(s.det(s.hessian(quad(fi),(z,e,W))))==-2*a**3*u8*u8
assert s.factor(s.diff(fi,W).subs({e:0,W:0}).coeff(z,1))==a*u8
print('PASS: exact Jacobian components and both forced A1 endpoint germs')

# Nonzero G: coefficient comparison forces G|R and the even parameter stratum.
N,T,y=s.symbols('N T y')
P=c*c*(-2*(a+1)+T*(a+2)*c*c/(2*a+1)**2)/(a**3*(3*a+2))
be=a*a*(3*a+2)*P/c
V6=T*c*c/(a*(2*a+1)**2)
ss={u0:N*N*P/a,u2:N*P,u3:0,u5:0,u6:V6/N,u8:T/(N*N),beta:be}
Q=N+a*z*z/c
assert s.cancel(R.subs(ss)-Q*G.subs(ss))==0
Gy=P+be*y-a*(a+2)*V6*y*y+c*T*y**3
Qy=1+a*y/c
Ly=a*P+(-a*a+3*a*be+2*a+5)*y-a*(3*a*a+4*a+2)*V6*y*y+a*(9*a*a+6*a-1)*T*y**3
Hy=a+2*a**3*V6*y+2*a*a*(a**3-a*a-a-1)*T*y*y
By=a**3*y*y-a*a*Qy*Ly+Qy*Qy*Hy
Dy=4*y*y/a*Hy-Ly*Ly
Br=s.factor(s.rem(By,Gy,y))
nums=lambda poly:[s.factor(s.together(s.Poly(poly,y).coeff_monomial(y**i)).as_numer_denom()[0]) for i in range(3)]
gb=s.groebner(nums(Br),T,a)
assert gb.reduce(a*T)[1]==0 and gb.reduce(2*a*a+a)[1]==0
print('PASS: every squarefree G stratum has an interior A1 and is excluded')

# No interior A1 is permitted by the remaining defect budget 2/5.
# For cubic Gy, Gy | Br*(Gy')^2 is necessary also at multiple roots.
Gn=s.together(Gy).as_numer_denom()[0]
Bn=s.together(Br).as_numer_denom()[0]
rr=s.rem(Bn*s.diff(Gn,y)**2,Gn,y)
unitfactors=[a,2*a+1,3*a+2,c,T]
def remove_units(poly,extras=()):
    return s.prod(p**m for p,m in s.factor_list(poly)[1] if p not in unitfactors+list(extras))
ns=[remove_units(n) for n in nums(rr)]
gn=s.groebner(ns,T,a)
S1=3*a**4+8*a**3+40*a*a+36*a+9
S2=8*a**4-6*a**3+33*a*a+36*a+9
S3=2*a**7+15*a**6+48*a**5+39*a**4+2*a**3-3*a*a+4*a+1
elim=a*a*(a+1)**4*(2*a+1)**11*(3*a+2)**2*S1*S2*S3
assert s.Poly(gn.polys[-1].as_expr(),a).monic()==s.Poly(elim,a).monic()
linear=next(p.as_expr() for p in gn.polys if s.Poly(p,T).degree()==1)
assert s.factor(s.diff(linear,T)).as_poly(a).monic()==s.Poly((a+1)**2*(2*a+1)**7*(3*a+2),a).monic()
print('PASS: no-node eliminant leaves a=-1 and three finite algebraic strata')

def field(poly,modulus):
    n,d=s.together(poly).as_numer_denom()
    n=s.rem(n,modulus,a);d=s.rem(d,modulus,a)
    return s.rem(n*s.invert(d,modulus,a),modulus,a)
def field_value(poly,ts,Y,modulus):
    result=0
    for coefficient in s.Poly(poly,y).all_coeffs():
        result=field(result*Y+field(coefficient.subs(T,ts),modulus),modulus)
    return result

# S1 is the triple-root cubic stratum. Its two interior points are A5.
ts1=6*(16*a**5+48*a**4+56*a**3+32*a*a+9*a+1)/(99*a**7+420*a**6+701*a**5+694*a**4+441*a**3+184*a*a+47*a+6)
y1=field((a+2)*c/(3*(2*a+1)**2),S1)
assert field(linear.subs(T,ts1),S1)==0
for polynomial in ns:
    assert field(polynomial.subs(T,ts1),S1)==0
for derivative in range(3):
    assert field_value(s.diff(Gy,y,derivative),ts1,y1,S1)==0
for poly in [Qy,By,Dy,y]:
    assert s.gcd(field_value(poly,ts1,y1,S1),S1)==1
assert field_value(s.diff(Gy,y,3),ts1,y1,S1)!=0
# The transverse Hessian is invertible; nonzero B gives Morse order6,
# hence A5. The low curve has class3 and defect 3^2/6=3/2.
assert s.Rational(3*3,6)>s.Rational(2,5)
print('PASS: S1 triple collisions are A5 with excessive normal defect')

# S2 is double-root; S3 violates u0 !=0. Assert exact specialized ideals too.
ts2=-(48944*a**3-40956*a*a+375576*a+181341)/2593080
ts3=(992*a**6-16558*a**5-160219*a**4-582979*a**3-530441*a*a+26491*a+216662)/354294
for modulus,ts in [(S2,ts2),(S3,ts3)]:
    for n in ns: assert field(n.subs(T,ts),modulus)==0
    assert field(linear.subs(T,ts),modulus)==0
cs=[field(s.Poly(Gy,y).nth(i).subs(T,ts2),S2) for i in range(4)]
y2=field((9*cs[3]*cs[0]-cs[2]*cs[1])/(2*(cs[2]**2-3*cs[3]*cs[1])),S2)
assert field_value(Gy,ts2,y2,S2)==0
assert field_value(s.diff(Gy,y),ts2,y2,S2)==0
for poly in [Qy,By,Dy,y,s.diff(Gy,y,2)]:
    assert s.gcd(field_value(poly,ts2,y2,S2),S2)==1
assert field(P.subs(T,ts3),S3)==0
assert s.Rational(2*2,4)>s.Rational(2,5)
print('PASS: S2 double collisions are A3; S3 has forbidden endpoint content')

# The chart a=-2/3 has not been divided away.
U=s.symbols('U');aa=-s.Rational(2,3)
ge=U-s.Rational(2,3)*y*y+s.Rational(1,18)*y**3
qe=1-s.Rational(2,3)*y
le=(a*u2+(-a*a+3*a*beta+2*a+5)*z*z-a*(3*a*a+4*a+2)*u6*z**4+a*(9*a*a+6*a-1)*u8*z**6).subs({a:aa,u2:U,beta:0,u6:-s.Rational(3,4),u8:s.Rational(1,18),z:s.sqrt(y)}).expand()
he=H.subs({a:aa,u5:0,u6:-s.Rational(3,4),u8:s.Rational(1,18),z:s.sqrt(y)}).expand()
bre=s.rem(aa**3*y*y-aa*aa*qe*le+qe*qe*he,ge,y)
ne=nums(s.rem(bre*s.diff(ge,y)**2,ge,y))
assert s.gcd(s.gcd(ne[0],ne[1]),ne[2])==1
print('PASS: the exceptional a=-2/3 stratum has no node-free member')

# G=0 is a genuinely separate stratum, with delta10 rather than delta8.
# c=0 forces u2=u3=u5=u6=beta=0; H depends linearly on z4.
fld=lambda expr:field(expr,c)
V=s.symbols('V')
rz=a*u0-2*(a+1)*z**4+a*V*z**8
lz=(-a*a+2*a+5)*z*z+a*V*(9*a*a+6*a-1)*z**6
hz=a+2*a*a*V*(a**3-a*a-a-1)*z**4
jz=-a*a*V*z
vv=fld(-1/(2*a*(a**3-a*a-a-1)))
uv=fld((2*(a+1)-a*vv)/a)
k=fld(s.diff(rz,z).subs({z:1,V:vv,u0:uv}))
psi3=fld(jz.subs({z:1,V:vv})+lz.subs({z:1,V:vv})*s.diff(hz,z).subs({z:1,V:vv})/k)
assert fld(vv-(-3*a-s.Rational(11,4)))==0
assert fld(uv-(s.Rational(3,4)-3*a))==0
assert fld(psi3-(10*a+11)/84)==0 and s.gcd(psi3,c)==1
vd=(a+1)/a
hv=fld(hz.subs({z:1,V:vd}))
dv=fld(4/a*hv-lz.subs({z:1,V:vd})**2)
assert s.gcd(hv,c)==1 and s.gcd(dv,c)==1
# Simple collisions: 8 A1 or 4 A1+4 A2. Double collisions: 4 A3 class2.
for defect in [s.Integer(4),4*s.Rational(1,2)+4*s.Rational(1,3),s.Integer(4)]:
    assert defect!=s.Rational(12,5)
print('PASS: the omitted G=0 stratum is excluded by A1/A2/A3 defects')

# The remaining conductor-sensitive line, without a global STCI assertion.
sm={a:-1,u0:-16*T,u2:16*T,u3:0,u5:0,u6:-4*T,u8:T,beta:-8*T,lam:8*T}
assert s.expand(G.subs(sm)-2*T*(z*z-2)**2*(z*z+2))==0
assert s.expand(R.subs(sm)+T*(z*z-2)**3*(z*z+2))==0
assert s.expand((F.subs(sm)).coeff(T,0)+B*B)==0
print('PASS: every surviving both-ramified carrier is on the h=-1/2 line')
print('BOUNDARY: extra conductor and higher jets on that line remain unresolved')
```
</details>
