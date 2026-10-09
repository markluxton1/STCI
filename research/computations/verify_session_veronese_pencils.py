#!/usr/bin/env python3
"""Exact normal forms, fibers and conductor jets for Veronese pencils.

Exhaustiveness is the direct linear-algebra proof in the companion note.
No broad search or source classification is imported by this verifier.
"""
import sympy as s

x,y,z,a,b,c,d,alpha,beta,D,eta,eps = s.symbols("x y z a b c d alpha beta D eta eps")

def qmatrix(q):
    variables=(x,y,z)
    return s.Matrix(3,3,lambda i,j:s.diff(q,variables[i],variables[j])/2)

A2=s.Matrix([[0,1,0],[1,0,0],[0,0,1]])
B2=s.diag(1,0,1)
A3=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
B3=s.Matrix([[0,0,0],[0,0,1],[0,1,0]])
AK=s.Matrix([[0,1,0],[1,0,0],[0,0,0]])
BK=s.Matrix([[0,0,1],[0,0,0],[1,0,0]])
q2=[y*y,x*z,y*z,z*z-x*y-x*x]
q3=[x*x,x*y,z*z,y*y-x*z]
qK=[x*x,y*y,y*z,z*z]

for AA,BB,forms in ((A2,B2,q2),(A3,B3,q3),(AK,BK,qK)):
    for q in forms:
        QQ=qmatrix(q)
        assert s.trace(AA*QQ)==0 and s.trace(BB*QQ)==0
assert s.factor((alpha*A2+beta*B2).det()) == -alpha**2*(alpha+beta)
assert s.factor((alpha*A3+beta*B3).det()) == -alpha**3
assert (alpha*AK+beta*BK).det()==0

F2=c**4-a*d*c*c-a*a*b*c-a*a*b*b
F3=(b*b-a*d)**2-a**3*c
FK=b*d-c*c
for F,forms in ((F2,q2),(F3,q3),(FK,qK)):
    assert s.expand(F.subs(dict(zip((a,b,c,d),forms))))==0
assert s.gcd(a*c*c,c**4-a*a*b*c-a*a*b*b)==1
assert s.gcd(a**3,(b*b-a*d)**2)==1

# Codimension-one transverse tangent cones are squares, not nodes.
transverse2=s.Poly(F2.subs({b:1,d:D}),a,c)
lowest2=sum(coeff*a**powers[0]*c**powers[1] for powers,coeff in transverse2.terms() if sum(powers)==2)
assert lowest2==-a*a
transverse3=s.Poly(F3.subs({c:1,d:D}),a,b)
lowest3=sum(coeff*a**powers[0]*b**powers[1] for powers,coeff in transverse3.terms() if sum(powers)==2)
assert lowest3==D*D*a*a

# Distinct leading branch coefficients give conductor exponents 2 and 3.
leading2=s.expand(F2.subs({b:1,d:D,a:eta*c**2})).coeff(c,4)
assert leading2==1-D*eta-eta**2
assert s.discriminant(leading2,eta)==D**2+4
leading3=s.expand(F3.subs({c:1,d:D,a:b*b/D+eps*b**3})).coeff(b,6)
assert s.factor(leading3-(D*D*eps*eps-D**-3))==0

# Rational inverses on dense opens; Kronecker map has a generic involution.
assert s.cancel(q2[1]/q2[2])==x/y
assert s.cancel(q2[2]/q2[0])==z/y
assert s.cancel(q3[1]/q3[0])==y/x
assert s.cancel((q3[1]/q3[0])**2-q3[3]/q3[0])==z/x
assert all(s.expand(q.subs(x,-x)-q)==0 for q in qK)

# At determinant roots the regular centers still have rank two, never one.
assert A2.rank()==3 and B2.rank()==2 and (A2-B2).rank()==2
assert A3.rank()==3 and B3.rank()==2

# Roman type: the six singleton pinch preimages lie on no nonzero conic.
qR=[y*z,z*x,x*y,x*x+y*y+z*z]
FR=a*a*b*b+a*a*c*c+b*b*c*c-a*b*c*d
assert s.expand(FR.subs(dict(zip((a,b,c,d),qR))))==0
pinches=[(0,1,1),(0,1,-1),(1,0,1),(1,0,-1),(1,1,0),(1,-1,0)]
quadratic_basis=[x*x,y*y,z*z,x*y,x*z,y*z]
evaluation=s.Matrix([[q.subs(dict(zip((x,y,z),point))) for q in quadratic_basis] for point in pinches])
assert evaluation.det()!=0 and evaluation.rank()==6
u,v=s.symbols("u v")
roman_x_axis_chart=[v,v/u,(v*v+1+u*u)/u]
roman_differential=s.Matrix([[s.diff(q,t) for t in (v,u)] for q in roman_x_axis_chart])
for sign in (1,-1):
    JJ=roman_differential.subs({v:0,u:sign})
    assert JJ[:,1]==s.zeros(3,1) and JJ[:,0]!=s.zeros(3,1)

# Jordan two: all finite z=0 fibers are paired by r -> -1-r, except r=-1/2.
r,r_other=s.symbols("r r_other")
assert s.expand((-r-r*r)-(-r_other-r_other*r_other)-(r_other-r)*(r+r_other+1))==0
assert s.expand((-r-r*r).subs(r,-1-r)-(-r-r*r))==0
for point in ((1,0,0),(0,0,1)):
    image=[q.subs(dict(zip((x,y,z),point))) for q in q2]
    assert image[:3]==[0,0,0] and image[3]!=0
jordan2_pinch_chart=[(-s.Rational(1,2)+v)*u,u,u*u+s.Rational(1,4)-v*v]
JJ=s.Matrix([[s.diff(q,t) for t in (u,v)] for q in jordan2_pinch_chart]).subs({u:0,v:0})
assert JJ[:,1]==s.zeros(3,1) and JJ[:,0]!=s.zeros(3,1)

# Jordan three: x=0 fibers are the sign pair in y/z; its two endpoints are
# the singleton fibers, and a smooth embedded image crosses x=0 transversely.
assert [q.subs(x,0) for q in q3]==[0,0,z*z,y*y]
jordan3_p_chart=[x*x,x*y,y*y-x]
JJ=s.Matrix([[s.diff(q,t) for t in (x,y)] for q in jordan3_p_chart]).subs({x:0,y:0})
assert JJ[:,1]==s.zeros(3,1) and JJ[:,0]!=s.zeros(3,1)
jordan3_q_chart=[x*x/(1-x*z),x/(1-x*z),z*z/(1-x*z)]
JJ=s.Matrix([[s.diff(q,t) for t in (x,z)] for q in jordan3_q_chart]).subs({x:0,z:0})
assert JJ[:,1]==s.zeros(3,1) and JJ[:,0]!=s.zeros(3,1)

# The first conductor jet uses the exact ring k(y)[x]/(x^2). An involution
# fixes every target generator. No conic satisfying the full fiber/smoothness
# conditions can have a positive power descending in characteristic zero.
ca,cb,cc,cd=s.symbols("conic_alpha conic_beta conic_gamma conic_delta")
def jet(expr):
    return s.simplify(s.series(expr,x,0,2).removeO())
def iota(expr):
    return jet(expr.subs({x:-x,y:-y+x/y},simultaneous=True))
assert iota(iota(x))==x and iota(iota(y))==y
for generator in (x*x,x*y,y*y-x):
    assert s.simplify(iota(generator)-jet(generator))==0
conic_affine=ca*x*x+cb*x*y+cc*x+cd*y
assert jet(conic_affine)==cd*y+x*(cb*y+cc)
assert s.simplify(iota(conic_affine)-(-cd*y+x*(cd/y+cb*y-cc)))==0

# For an even positive exponent n, the constant terms agree. After dividing
# the x-coefficient difference by n*(delta*y)^(n-1), it is exactly this sum.
# The odd-exponent constant obstruction and n!=0 are mathematical steps,
# explicitly recorded in the note, not a finite sample of exponents here.
normalized_even_difference=s.simplify((cb*y+cc)+(cd/y+cb*y-cc))
assert normalized_even_difference==2*cb*y+cd/y
obstruction=s.Poly(s.expand(y*normalized_even_difference),y)
assert obstruction.coeff_monomial(y*y)==2*cb
assert obstruction.coeff_monomial(1)==cd
assert obstruction.coeff_monomial(y)==0

print("PASS: tensor/dual-quadric convention, all three canonical pencil forms,")
print("quartic/quadric equations, finite-projection basepoint controls in note,")
print("birational inverse identities, nonnodal transverse tangent cones, and")
print("generic conductor branch-separation exponents two and three;")
print("Roman no-conic matrix, Jordan singleton-fiber/transversality controls,")
print("and the exact first-jet involution excluding all Jordan-three conic powers.")
