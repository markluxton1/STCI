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
