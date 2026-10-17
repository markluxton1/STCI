#!/usr/bin/env python3
"""Independent exact certificate for the explicit P-044 survivor cubic.

Checks:
  1. Bezout identity for A,B.
  2. H_x vanishes on the canonical primitive triple modulo eps^3.
  3. The displayed coefficient vector reconstructs H_x.

This deliberately does not recompute the full P-044 obstruction.
"""
import sympy as sp

x,z,e=sp.symbols("x z e", nonzero=True)
X0,X1,X2,X3=sp.symbols("x0 x1 x2 x3")

Aq=z**2-sp.Rational(1,2)*z+x
Bq=1-2*z+z**2/x
s=2*(2*x-z)/(x*(4*x-1))
t=(2*z-1)/(4*x-1)
assert sp.cancel(s*Aq+t*Bq-1)==0

gamma=-(8*x**3+16*x**2*z**2-18*x**2*z+4*x**2
        -12*x*z**3+8*x*z**2+3*z**4)/(8*x**3)

u=Aq*e-t*gamma*e**2
v=Bq*e+s*gamma*e**2
subs={
 X0:1,
 X1:z,
 X2:z**3+v,
 X3:z**4+u+sp.Rational(3,2)*z*v,
}

q=X0*X3-X1*X2
A3=X0**2*X2-X1**3
B3=X0*X2**2-X1**2*X3
D3=X2**3-X1*X3**2
L=-4*x**3*X0+8*x**3*X1-2*x*X2+4*x*X3
H=sp.expand(D3+4*x**2*B3+4*x**4*A3+L*q)

He=sp.series(H.subs(subs),e,0,3).removeO()
assert sp.cancel(sp.expand(He))==0

alpha,beta,gam=4*x**4,4*x**2,sp.Integer(1)
lam=[-4*x**3,8*x**3,-2*x,4*x]
H2=sp.expand(alpha*A3+beta*B3+gam*D3
             +q*(lam[0]*X0+lam[1]*X1+lam[2]*X2+lam[3]*X3))
assert sp.expand(H-H2)==0

print("PASS: Bezout identity")
print("PASS: H_x vanishes on canonical C3 modulo epsilon^3")
print("PASS: coefficient vector reconstructs H_x")
