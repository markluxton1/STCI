#!/usr/bin/env python3
"""All primitive e=1 triples and exclusion of MF6 type (d2,d3)=(0,4).

Characteristic zero, fixed C0. Reconstruct full quartic spaces in every
actual torus orbit; retain both charts and all pencil boundary members.
"""
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import QQ
import verify_mf6_defect12 as a

z,U,V,xs=a.z,a.U,a.V,a.xs
x0,x1,x2,x3=xs
u,v,y,m,w=s.symbols('u v y m w')
a0,a1,b0,b1,inverse=s.symbols('a0 a1 b0 b1 inverse')
A=a0+a1*z;B=b0+b1*z
Av=a1+a0*w;Bv=b1+b0*w
D=s.diff(A,z)*B-A*s.diff(B,z)
h2=s.expand(-(2*A+z*B)*(12*A*A+3*z*z*B*B+4*z*z*D)/(8*z**5))

def cut(expr):
    expr=s.expand(expr)
    return s.Add(*[expr.coeff(y,i)*y**i for i in range(3)])

# Independently reconstruct the moving support coordinate through order2.
u0=A*y;v0=B*y;b=u0+s.Rational(3,2)*z*v0
inv=z**-4*(1-b/z**4+b*b/z**8)
W=cut((z**3+v0)*inv)
ap=cut(z*inv-cut(W**3));bp=cut(inv-cut(W**4))
up=ap/2;vp=cut(-3*cut(W*ap)+2*bp)
mp=cut(Bv.subs(w,W)*up-Av.subs(w,W)*vp)
assert mp.coeff(y,1)==0
assert s.expand(z**8*mp.coeff(y,2)-h2)==0
coords=[s.factor(h2.coeff(z,-i)) for i in range(1,4)]
expected=[-b1*(2*a0*b1+12*a1*a1+16*a1*b0+9*b0*b0)/8,
          -(2*a1+b0)*(8*a0*b1+12*a1*a1+4*a1*b0+3*b0*b0)/8,
          -a0*(2*a0*b1+36*a1*a1+16*a1*b0+3*b0*b0)/4]
assert all(s.expand(p-q)==0 for p,q in zip(coords,expected))
determinant=a0*b1-a1*b0
sat=s.groebner(coords+[inverse*determinant-1],inverse,a0,a1,b0,b1,
                order='lex',domain=s.QQ)
for relation in [a0*(2*a1+b0),b1*(2*a1+b0)]:
    assert sat.reduce(relation)[1]==0
# The complete zero-locus classification is the short case argument in the
# companion note. These relations give its principal branch. The boundary
# a0=b1=0 has exactly the displayed three nonzero roots.
r=s.symbols('r')
assert s.expand(coords[1].subs({a0:0,a1:r,b0:1,b1:0})
                +(2*r+1)*(12*r*r+4*r+3)/8)==0
for c in coords:
    assert s.expand(c.subs({a1:-b0/2,a0:-2*b0*b0/b1}))==0


def triple_matrix(A0,B0,gamma,bezs,bezt):
    assert s.expand(bezs*A0+bezt*B0)==1
    sub={U:A0*y-bezt*gamma*y*y,V:B0*y+bezs*gamma*y*y}
    jets=[s.expand(j.as_expr().subs(sub)) for j in a.jets]
    assert all(j.coeff(y,0)==0 for j in jets)
    rows=[]
    for power in [1,2]:
        coeffs=[j.coeff(y,power) for j in jets]
        degree=max(s.degree(c,z) if c else 0 for c in coeffs)
        rows.extend([[s.expand(c).coeff(z,i) for c in coeffs]
                     for i in range(degree+1)])
    return s.Matrix(rows)

# Orbit1: A=1+z,B=-2-8z. The actual torus normalization is in the note.
As=1+z;Bs=-2-8*z;gamma=192*z+96
assert s.expand(h2.subs({a0:1,a1:1,b0:-2,b1:-8})
                -(gamma-6*z**-4-3*z**-5))==0
bezs=s.Rational(4,3);bezt=s.Rational(1,6)
M=triple_matrix(As,Bs,gamma,bezs,bezt)
assert M.rank()==16
quartics=[s.expand(sum(c*F for c,F in zip(vec,a.I4))) for vec in M.nullspace()]
assert len(quartics)==2
alpha,beta=s.symbols('alpha beta')
F=alpha*quartics[0]+beta*quartics[1]
jet=s.expand(F.subs(a.sub).subs({U:bezt*m+As*y,V:-bezs*m+Bs*y}))
h=jet.coeff(m,1).coeff(y,0)
E=jet.coeff(m,1).coeff(y,1);K=jet.coeff(m,0).coeff(y,3)
T=s.expand(gamma*E-K)
assert s.expand(jet.coeff(m,0).coeff(y,2)-gamma*h)==0
h_expected=(4*z*z+2*z+1)*(64*alpha*z**3+64*beta*z**6+8*beta*z**3+beta)/1024
T_expected=(2*z+1)*(1536*alpha*z**5+1152*alpha*z**4+448*alpha*z**3
    +48*alpha*z*z-24*alpha*z+4*alpha+1536*beta*z**8+1152*beta*z**7
    +448*beta*z**6+240*beta*z**5+120*beta*z**4+60*beta*z**3
    +30*beta*z*z+15*beta*z+8*beta)
assert s.expand(h-h_expected)==0 and s.expand(T-T_expected)==0
assert s.expand(s.resultant(h.subs(beta,1),T.subs(beta,1),z)
                +s.Rational(27,2**26)*(8*alpha-1)*(8*alpha+3)**3)==0
for value,degree in [(s.Rational(1,8),1),(-s.Rational(3,8),2)]:
    hh=s.expand(h.subs({alpha:value,beta:1}))
    tt=s.expand(T.subs({alpha:value,beta:1}))
    assert s.degree(hh,z)==8
    assert s.degree(s.gcd(hh,tt),z)==degree
# Every beta!=0 therefore gives finite cubic polar degree at least6.
h0=s.expand(h.subs({alpha:1,beta:0}));T0=s.expand(T.subs({alpha:1,beta:0}))
assert s.degree(h0,z)==5 and s.degree(s.gcd(h0,T0),z)==2
# The remaining member has finite degree3 and infinity degree3.
Asinf=1+w;Bsinf=-8-2*w;sin=-s.Rational(1,3);tin=-s.Rational(1,6)
gammainf=3*w+6
ui=tin*m+Asinf*y;vi=-sin*m+Bsinf*y
subinf={x3:1,x2:w,x1:w**3+2*ui,x0:w**4+vi/2+3*w*ui}
inf=s.expand(quartics[0].subs(subinf))
hi=inf.coeff(m,1).coeff(y,0);Ei=inf.coeff(m,1).coeff(y,1);Ki=inf.coeff(m,0).coeff(y,3)
Ti=s.expand(gammainf*Ei-Ki)
assert s.expand(hi-w**3*(w*w+2*w+4)/16)==0
assert s.expand(Ti+(w+2)*(w*w+2*w+4)*(3*w**3+3*w*w-4*w+2)/16)==0
assert s.expand(inf.coeff(m,0).coeff(y,2)-gammainf*hi)==0
assert Ti.subs(w,0)!=0

# Orbit2: A=-z/2,B=1 gives exactly the unique-quadric multiples.
Mq=triple_matrix(-z/2,s.Integer(1),s.Integer(0),s.Integer(0),s.Integer(1))
assert Mq.rank()==8
quarticsq=[s.expand(sum(c*F for c,F in zip(vec,a.I4))) for vec in Mq.nullspace()]
expectedq=[a.q*monomial for monomial in a.monomials(2)]
assert a.vectors(expectedq,4).rank()==10
assert a.vectors(quarticsq+expectedq,4).rank()==10

# Orbits3,4 are conjugate over the exact quadratic field. Every assertion
# below is a polynomial identity modulo q(r), or a rank over that field;
# conjugation gives the other root without an omitted specialization.
q=12*r*r+4*r+3

def modq(expr):
    expr=s.expand(expr)
    return s.Add(*[
        s.rem(coeff,q,r)*z**monomial[0]*w**monomial[1]*y**monomial[2]*m**monomial[3]
        for monomial,coeff in s.Poly(expr,z,w,y,m).terms()])

Fr0=x0**3*x3-(r+s.Rational(3,2))*x0*x0*x1*x2+(r+s.Rational(1,2))*x1**4
Fr1=x0*x3**3+(r-s.Rational(7,6))*x1*x2*x3*x3+(s.Rational(1,6)-r)*x2**4
# Straight primitive triple: gamma=0, U=r*z*y,V=y.
Mr=triple_matrix(r*z,s.Integer(1),s.Integer(0),s.Integer(0),s.Integer(1))
root=(-1+2*s.sqrt(-2))/6
DM=DomainMatrix.from_Matrix(Mr.subs(r,root)).convert_to(QQ.algebraic_field(s.sqrt(-2)))
assert DM.rank()==16
for form in [Fr0,Fr1]:
    jj=s.expand(form.subs(a.sub).subs({U:r*z*y,V:y}))
    assert modq(jj.coeff(y,1))==0 and modq(jj.coeff(y,2))==0
assert a.vectors([Fr0,Fr1],4).rank()==2
assert a.vectors(a.I4+[Fr0,Fr1],4).rank()==18
# Full rank16 kernel is exactly the displayed pencil.
rinv=-4*r-s.Rational(4,3)
assert s.rem(s.expand(r*rinv-1),q,r)==0
jr=s.expand((alpha*Fr0+beta*Fr1).subs(a.sub).subs({U:r*z*y+m,V:y}))
hr=modq(jr.coeff(m,1).coeff(y,0));Kr=modq(jr.coeff(m,0).coeff(y,3))
assert s.expand(hr-alpha-beta*(2*r+s.Rational(2,3))*z**8)==0
assert s.expand(Kr+beta*s.Rational(8,9)*r*z**3)==0
assert s.gcd(2*r+s.Rational(2,3),q)==1 and s.gcd(r,q)==1
# beta!=0 gives eight finite poles if alpha!=0, five if alpha=0.
# beta=0 must be handled on the actual second chart.
ui=r*y;vi=w*y-rinv*m
subinf={x3:1,x2:w,x1:w**3+2*ui,x0:w**4+vi/2+3*w*ui}
ifr=s.expand(Fr0.subs(subinf))
hrinf=modq(ifr.coeff(m,1).coeff(y,0));Krinf=modq(ifr.coeff(m,0).coeff(y,3))
assert s.expand(hrinf-w**8)==0
assert modq(ifr.coeff(m,0).coeff(y,2))==0
assert s.expand(Krinf-(s.Rational(16,27)*r+s.Rational(4,9))*w**3)==0
assert s.gcd(s.Rational(16,27)*r+s.Rational(4,9),q)==1
# Thus the beta=0 member has exactly five infinity cubic poles.
print('PASS: universal e=1 quadratic cocycle and saturated primitive-direction constraints')
print('PASS: generic direction orbit has complete quartic pencil; every member has deg D3>=6')
print('PASS: r=-1/2 orbit has only unique-quadric multiples')
print('PASS: conjugate quadratic-root orbits have complete quartic pencils; deg D3>=5')
print('RESULT: MF6 e=1 type (d2,d3)=(0,4) is excluded on fixed C0')
