#!/usr/bin/env python3
"""Provisional exact e=0 part of a shorter characteristic-zero (4,4) exclusion.

Independent inputs, stated rather than tested: balanced conormal O(-7)^2,
finite-flat quasiprimitive/BF filtration and Gorenstein duality.  This code
reconstructs all quartics in 35 ambient monomials and checks the NEW
multiplicity-three obstruction after the (4,4) numerical BF reduction.
Uses SymPy; no repository verifier or generated data are imported.
"""
import sympy as s

z, ell, m, eps = s.symbols('z ell m eps')
x0,x1,x2,x3,U,V = s.symbols('x0 x1 x2 x3 U V')
xs=(x0,x1,x2,x3)
mons=[x0**i*x1**j*x2**k*x3**(4-i-j-k)
      for i in range(4,-1,-1) for j in range(4-i,-1,-1)
      for k in range(4-i-j,-1,-1)]
assert len(mons)==35
sub={x0:1,x1:z,x2:z**3+V,x3:z**4+U+s.Rational(3,2)*z*V}
jets=[s.Poly(s.expand(f.subs(sub)),U,V) for f in mons]

# Exact ambient chart transition through quadratic order, no inherited formula.
def cocycle(Uexpr,Vexpr, quotient):
    denominator=z**4+Uexpr+s.Rational(3,2)*z*Vexpr
    W=(z**3+Vexpr)/denominator
    a=z/denominator-W**3
    b=1/denominator-W**4
    Up=a/2
    Vp=-3*W*a+2*b
    return s.expand(s.series(quotient(Up,Vp),eps,0,3).removeO()).coeff(eps,2)*z**7
h=s.expand(cocycle(-eps,eps,lambda up,vp:up+vp))
h0=s.expand(cocycle(0,eps,lambda up,vp:up))
hi=s.expand(cocycle(eps,0,lambda up,vp:vp))
assert h==3/z**5-s.Rational(3,2)/z**4+s.Rational(3,4)/z**3-s.Rational(3,8)/z**2
assert h0==-s.Rational(3,8)/z**2
assert hi==3/z**5

def killing_matrix(c):
    # Multiplication by a degree-three defect section, H1(O(-7))->H1(O(-4)).
    return s.Matrix([[s.expand(z**j*c).coeff(z,-i) for j in range(4)] for i in range(1,4)])
K=killing_matrix(h)
assert K.nullspace()==[s.Matrix([0,2,1,0])]
assert killing_matrix(h0).nullspace()==[s.Matrix([0,0,1,0]),s.Matrix([0,0,0,1])]
assert killing_matrix(hi).nullspace()==[s.Matrix([1,0,0,0]),s.Matrix([0,1,0,0])]
delta=z*(z+2)
gamma=s.Rational(3,8)
assert s.expand(delta*h)==-gamma+6/z**4

# For a chart with normal kernel m and transverse quotient ell, the unique
# triple has m=(gamma/delta)*ell^2 over k(z).  Polynomial identities below
# impose global quartic containment.  H0(Hom(M,L^2(D)))=H0(O(-4))=0
# means no omitted free regular correction can change this triple.
def coefficient_rows(errors):
    errors=[s.expand(e) for e in errors]
    deg=max([s.degree(e,z) for e in errors if e!=0],default=0)
    return [[e.coeff(z,i) for e in errors] for i in range(int(deg)+1)]
def contact_matrix(Uexpr,Vexpr,delta,gamma,mcoefficient):
    restriction=[s.Poly(s.expand(j.as_expr().subs({U:Uexpr,V:Vexpr})),ell) for j in jets]
    e0=[r.coeff_monomial(1) for r in restriction]
    e1=[r.coeff_monomial(ell) for r in restriction]
    e2=[s.expand(delta*r.coeff_monomial(ell**2)+gamma*j.coeff_monomial(mcoefficient)) for r,j in zip(restriction,jets)]
    return s.Matrix(coefficient_rows(e0)+coefficient_rows(e1)+coefficient_rows(e2))

def coefficient_vector(f):
    p=s.Poly(s.expand(f),*xs)
    return s.Matrix([p.coeff_monomial(mm) for mm in mons])

# Compact explicit generators of the complete open-orbit quartic pencil.
q=x0*x3-x1*x2
A=x0**2*x2-x1**3
B=x0*x2**2-x1**2*x3
D=x2**3-x1*x3**2
F0=-(x2+x3)*(16*A+(16*x0+8*x1)*q)+(4*x2+x3)*B-x2**2*q
F1=x2*D-256*x1*A-4*q*(64*x0*x1+16*x0*x2+4*x0*x3+32*x1**2+4*x1*x2+4*x1*x3+2*x2**2+x2*x3)
T=contact_matrix(-ell,ell,delta,gamma,U)
assert T.rank()==33
assert T*coefficient_vector(F0)==s.zeros(T.rows,1)
assert T*coefficient_vector(F1)==s.zeros(T.rows,1)
assert s.Matrix.hstack(coefficient_vector(F0),coefficient_vector(F1)).rank()==2

# The first two contacts agree; the cubic contacts do not agree.  The
# determinant proves generic intersection length exactly three for the
# independent quartics, so it cannot be the length-four (4,4) structure.
def third_data(f):
    p=s.Poly(s.expand(f.subs(sub).subs({U:m-ell,V:ell})),m,ell)
    h=s.factor(p.coeff_monomial(m))
    r2=p.coeff_monomial(ell**2)
    r3=p.coeff_monomial(ell**3)
    mixed=p.coeff_monomial(m*ell)
    assert s.cancel(r2+h*gamma/delta)==0
    cubic=s.factor(r3+mixed*gamma/delta)
    return h,cubic
hF0,tF0=third_data(F0)
hF1,tF1=third_data(F1)
assert s.factor(hF0)==-2*z**3*(z+2)**3
assert s.factor(hF1)==-2*z*(z+2)*(z**2+4)*(z**4+16)
assert s.cancel(tF0+(z+4)/8)==0
assert s.cancel(tF1+(z**5+2*z**4+16*z**2-16*z+96)/(8*z*(z+2)))==0
assert s.factor(hF0*tF1-hF1*tF0)==32*z*(z-2)*(z+2)

# Endpoint quotient theta=0: every degree-three annihilator is z^2(a+bz).
# The factor (a+bz) cancels from the containment identity, leaving precisely
# the degree-two defect test below.  At theta=infinity every annihilator
# is (a+bz), and it cancels in the same way.  These larger test spaces are
# therefore exhaustive even if some proposed triples are not pure.
T0=contact_matrix(0,ell,z**2,s.Rational(3,8),U)
Ti=contact_matrix(ell,0,1,0,V)
assert T0.rank()==31 and Ti.rank()==31
for x in xs:
    assert T0*coefficient_vector(x*D)==s.zeros(T0.rows,1)
    assert Ti*coefficient_vector(x*A)==s.zeros(Ti.rows,1)
assert s.Matrix.hstack(*[coefficient_vector(x*D) for x in xs]).rank()==4
assert s.Matrix.hstack(*[coefficient_vector(x*A) for x in xs]).rank()==4

print('PASS: all degree-three e=0 defect annihilators on the three torus orbits')
print('PASS: complete open-orbit quartic contact space is <F0,F1>')
print('PASS: cubic contact determinant is 32*z*(z-2)*(z+2), not zero')
print('PASS: endpoint quartic contact spaces are D*S1 and A*S1')
print('RESULT: the (4,4), e=0 BF type cannot occur in characteristic zero')

# New simultaneous-pencil consequence of the previously accepted e=1
# primitive-triple classification.  These contact expressions are explicit
# inherited inputs from 2026-10-07-session-mf6-e1-independent-audit.md section4;
# this script checks ONLY the new determinants, not that classification.
p=4*z**2+2*z+1
hp0=p*64*z**3/1024
hp1=p*(64*z**6+8*z**3+1)/1024
tp0=(2*z+1)*(1536*z**5+1152*z**4+448*z**3+48*z**2-24*z+4)
tp1=(2*z+1)*(1536*z**8+1152*z**7+448*z**6+240*z**5+120*z**4+60*z**3+30*z**2+15*z+8)
assert s.factor(hp0*tp1-hp1*tp0)==(2*z-1)**3*(2*z+1)*(4*z**2+2*z+1)/256
r=s.symbols('r')
assert s.gcd(r,12*r**2+4*r+3)==1
assert s.factor(1*(8*r*z**3/9)-((2*r+s.Rational(2,3))*z**8)*0)==8*r*z**3/9
print('PASS: inherited e=1 principal and algebraic quartic pencils have nonzero cubic contact determinants')
print('SCOPE: e=1 completeness and the quadric orbit remain inherited accepted inputs')
