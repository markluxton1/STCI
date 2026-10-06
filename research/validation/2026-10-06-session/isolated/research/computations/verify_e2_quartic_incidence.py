#!/usr/bin/env python3
"""Exact quartic-incidence regression for the canonical e=2 primitive triple.

Status: EXACT COMPUTATION / COMPUTATIONAL CROSS-CHECK, not a theorem-level
classification.  The script reconstructs I_C(4) directly from the monomial
parametrization, forms first- and second-order jet matrices, and checks the
generic and P-045 regressions.

Important: the generic six-dimensional C2-kernel chart does NOT cover P-045:
rank M1 is 11 there, not 12.
"""
import sympy as sp

z=sp.symbols("z")
x,a,b,d=sp.symbols("x a b d")
X=sp.symbols("x0:4")
Delta=1-a*b+a*a*d-2*d*x+b*b*x-a*b*d*x+d*d*x*x
A=x+a*z+z**2
B=1+b*z+d*z**2

# Bezout pair s*A+t*B=1 from the audited moving-coordinate construction.
s=(-a*b*d-a*d*d*z+b*b+b*d*z+d*d*x-d)/Delta
t=(a*a*d-a*b+a*d*z-b*z-d*x+1)/Delta
assert sp.cancel(s*A+t*B-1)==0

# gamma_U independently reconstructed from the moving-coordinate quadratic
# mismatch.  Multiplying the second jet by Delta clears the only parameter
# denominator on D(Delta).
gamma=(
 -4*a*a*d-6*a*b*b-8*a*b*d*z-32*a*b-2*a*d*d*z**2-16*a*d*z
 -12*a*d-72*a-3*b**3*z-9*b*b*d*z**2-10*b*b*z-9*b*b
 -9*b*d*d*z**3-16*b*d*z**2-18*b*d*z-20*b*z-24*b
 -3*d**3*z**4+2*d*d*x*z-6*d*d*z**3-9*d*d*z**2-8*d*x
 -12*d*z**2-20*d*z-9*d-24*z-28
)/8

U1=A
V1=B
U2=-t*gamma
V2=s*gamma
W1=U1+sp.Rational(3,2)*z*V1
W2=U2+sp.Rational(3,2)*z*V2

# Direct monomial construction of I_C(4): group degree-four monomials by
# exponent i1+3*i2+4*i3 after (x0,x1,x2,x3)=(1,z,z^3,z^4).
mons=[]
for i0 in range(5):
    for i1 in range(5-i0):
        for i2 in range(5-i0-i1):
            i3=4-i0-i1-i2
            ex=(i0,i1,i2,i3)
            wt=i1+3*i2+4*i3
            mon=sp.prod(X[k]**ex[k] for k in range(4))
            mons.append((wt,ex,mon))
groups={}
for wt,ex,mon in mons:
    groups.setdefault(wt,[]).append((ex,mon))
basis=[]
basis_exponents=[]
for wt in sorted(groups):
    g=groups[wt]
    for ex,mon in g[1:]:
        basis.append(sp.expand(mon-g[0][1]))
        basis_exponents.append((wt,ex,g[0][0]))
assert len(groups)==17
assert len(basis)==18

red={X[0]:1,X[1]:z,X[2]:z**3,X[3]:z**4}
J1=[]
J2=[]
for F in basis:
    f2=sp.diff(F,X[2]).subs(red)
    f3=sp.diff(F,X[3]).subs(red)
    f22=sp.diff(F,X[2],2).subs(red)
    f23=sp.diff(sp.diff(F,X[2]),X[3]).subs(red)
    f33=sp.diff(F,X[3],2).subs(red)
    j1=sp.expand(f2*V1+f3*W1)
    j2=f2*V2+f3*W2+sp.Rational(1,2)*(
        f22*V1**2+2*f23*V1*W1+f33*W1**2)
    J1.append(j1)
    J2.append(sp.factor(sp.cancel(Delta*j2)))
assert all(sp.denom(q)==1 for q in J2)

# Both jet polynomials have degree <=14, so the full matrix is 30 x 18.
M1=sp.Matrix([[q.coeff(z,k) for q in J1] for k in range(15)])
M2=sp.Matrix([[sp.expand(q).coeff(z,k) for q in J2] for k in range(15)])
assert M1.shape==(15,18) and M2.shape==(15,18)

def reduced_ranks(pt):
    m1=M1.subs(pt)
    m2=M2.subs(pt)
    ns=m1.nullspace()
    N=sp.Matrix.hstack(*ns)
    R=m2*N
    return m1.rank(),len(ns),R.rank(),sp.Matrix.vstack(m1,m2).rank()

# Generic point from the handoff plus independent exact rational controls.
tests=[
    {x:2,a:3,b:5,d:7},
    {x:1,a:2,b:-1,d:3},
    {x:3,a:-2,b:4,d:1},
    {x:sp.Rational(2,3),a:1,b:2,d:-1},
]
for pt in tests:
    assert Delta.subs(pt)!=0
    assert reduced_ranks(pt)==(12,6,6,18)

# A concrete rank-12 chart.  The displayed determinant proves this chart is
# valid on D(d*(b+2)*Delta); it is intentionally not a global chart.
pt0=tests[0]
_,pivot_cols=M1.subs(pt0).rref()
_,pivot_rows=M1.subs(pt0).T.rref()
P=M1.extract(list(pivot_rows),list(pivot_cols))
assert sp.factor(P.det()) == d**7*(b+2)*Delta/sp.Integer(128)

# On the recommended dx=1 test bed this chart is especially clean.  Since
# Delta=(b*x-a)^2/x there, basepoint-free implies x*(b*x-a) != 0, so the
# chart covers the entire basepoint-free slice away from the single divisor
# b=-2.
P_dx1=sp.factor(P.det().subs(d,1/x))
assert P_dx1 == (b*x-a)**2*(b+2)/(sp.Integer(128)*x**8)

# P-045: first-order rank drops to 11, so its C2 quartic kernel has dimension
# seven.  The second-order obstruction has rank three on that kernel, leaving
# exactly four quartics.
for xv in map(sp.Rational,[1,2,3,-1]):
    pt={x:xv,a:-sp.Rational(1,2),b:-2,d:1/xv}
    assert Delta.subs(pt)!=0
    assert reduced_ranks(pt)==(11,7,3,14)

# Symbolic P-045 containment of H_x*x_i through order epsilon^2.
q=X[0]*X[3]-X[1]*X[2]
A3=X[0]**2*X[2]-X[1]**3
B3=X[0]*X[2]**2-X[1]**2*X[3]
D3=X[2]**3-X[1]*X[3]**2
Hx=(D3+4*x**2*B3+4*x**4*A3+
    (-4*x**3*X[0]+8*x**3*X[1]-2*x*X[2]+4*x*X[3])*q)
ps={a:-sp.Rational(1,2),b:-2,d:1/x}
for ell in X:
    F=sp.expand(Hx*ell)
    f2=sp.diff(F,X[2]).subs(red)
    f3=sp.diff(F,X[3]).subs(red)
    f22=sp.diff(F,X[2],2).subs(red)
    f23=sp.diff(sp.diff(F,X[2]),X[3]).subs(red)
    f33=sp.diff(F,X[3],2).subs(red)
    jj1=sp.cancel((f2*V1+f3*W1).subs(ps))
    jj2=sp.cancel((f2*V2+f3*W2+sp.Rational(1,2)*(
        f22*V1**2+2*f23*V1*W1+f33*W1**2)).subs(ps))
    assert jj1==0 and jj2==0

print("PASS: dim I_C(4)=18 from direct monomial substitution")
print("PASS: generic ranks M1=12, reduced R=6, full=18 at four exact points")
print("PASS: rank-12 chart determinant = d^7*(b+2)*Delta/128")
print("PASS: on dx=1 it is (b*x-a)^2*(b+2)/(128*x^8)")
print("PASS: P-045 has ranks M1=11, reduced second-order=3, full=14")
print("PASS: H_x*x_i vanish symbolically on P-045 canonical C3")
