#!/usr/bin/env python3
"""Independent exact controls for all-mate Veronese carrier exclusion.

Global classification, full inverse support, degree and descent reasoning
are in the accompanying Oct8 audit; this checks the small identities used
there, including the nonreduced first-jet involution for arbitrary degree.
"""
import sympy as s

x,y,z,A,B,C,D = s.symbols("x y z A B C D")
a,b,c,d,N = s.symbols("a b c d N")

q2=s.Matrix([y*y,x*z,y*z,z*z-x*y-x*x])
pinf=dict(zip((x,y,z),(1,0,0)))
pextra=dict(zip((x,y,z),(0,0,1)))
assert q2.subs(pinf)+q2.subs(pextra)==s.zeros(4,1)
r=s.symbols("r")
qline=q2.subs({y:1,z:0,x:r})
assert s.expand(qline[3].subs(r,-1-r)-qline[3])==0
fixed=s.solve(s.Eq(r,-1-r),r)
assert fixed==[s.Rational(-1,2)]
affine2=s.Matrix([x*z,z,z*z-x-x*x])
j2=affine2.jacobian([x,z]).subs({x:s.Rational(-1,2),z:0})
assert j2[:,0]==s.zeros(3,1)
assert j2[:,1]==s.Matrix([-s.Rational(1,2),1,0])

q3=s.Matrix([x*x,x*y,z*z,y*y-x*z])
affine_at_z1=s.Matrix([x*x,x*y,y*y-x])
j3z=affine_at_z1.jacobian([x,y]).subs({x:0,y:0})
assert j3z[:,0]==s.Matrix([0,0,-1]) and j3z[:,1]==s.zeros(3,1)
affine_at_y1=s.Matrix([x*x/(1-x*z),x/(1-x*z),z*z/(1-x*z)])
j3y=affine_at_y1.jacobian([x,z]).subs({x:0,z:0})
assert j3y[:,0]==s.Matrix([0,1,0]) and j3y[:,1]==s.zeros(3,1)

def red(expr):
    return s.cancel(s.series(s.cancel(expr),x,0,2).removeO())

def involution(expr):
    return red(expr.xreplace({x:-x,y:-y+x/y}))

assert red(involution(involution(x))-x)==0
assert red(involution(involution(y))-y)==0
for generator in (x*x,x*y,y*y-x):
    assert red(involution(generator)-generator)==0

f=a*x*x+b*x*y+c*x+d*y
assert s.cancel(red(f)-(d*y+x*(b*y+c)))==0
if_=involution(f)
assert s.expand(if_-(-d*y+x*(d/y+b*y-c)))==0

# For every even positive N, divide first-jet coefficient equality by the
# common nonzero scalar N*d^(N-1)*y^(N-1). This is an exact identity,
# rather than checking a finite list of powers.
normalized_difference=s.expand((b*y+c)+(d/y+b*y-c))
assert normalized_difference==2*b*y+d/y
assert s.expand(y*normalized_difference)==2*b*y*y+d
assert s.Poly(2*b*y*y+d,y).coeff_monomial(1)==d

# The whole singular supports cannot contain an integral degree-four C:
# Jordan3: dF/dC=-A^3 then F|A=0=B^4.
F3=(B*B-A*D)**2-A**3*C
assert s.diff(F3,C)==-A**3 and F3.subs(A,0)==B**4
# Jordan2: dF/dD=-A*C^2, and the two alternatives give two lines.
F2=C**4-A*D*C*C-A*A*B*C-A*A*B*B
assert s.diff(F2,D)==-A*C*C
assert F2.subs(A,0)==C**4
assert F2.subs(C,0)==-A*A*B*B
print("PASS: Jordan2 full exceptional fiber, sole allowed singleton and")
print("transverse differential; Jordan3 endpoint differentials, actual")
print("first-jet involution fixing the image ring, and arbitrary-even-degree")
print("coefficient contradiction. Global hypotheses remain in the audit note.")
