#!/usr/bin/env python3
"""Integral double-to-triple obstruction for the prescribed quartic Z4.

Requires SymPy, and uses exact integer polynomial arithmetic only.  The proof
that an admissible Z4 lift supplies a primitive triple is separate from this
identity certificate; see the accompanying research note.
"""

import sympy as sp

u, e = sp.symbols("u e")
a, b, d, h, r, s = sp.symbols("a b d h r s")


def trunc(expr, order=3):
    poly = sp.Poly(sp.expand(expr), e)
    return sp.expand(sum(poly.nth(i) * e**i for i in range(order)))


# The complete quotient N_C^* -> O_C(-6), in the integral raw frame.
p = a + b*u + 3*h*u**2
q = d + 2*h*u
P = 3*a/u**2 + (3*b-4*d)/u + h
Q = 2*a/u + 2*b-3*d
assert sp.expand(P - (3*p/u**2-4*q/u)) == 0
assert sp.expand(Q - (2*p/u-3*q)) == 0

# Reconstruct the actual ambient change of coordinates to order two, allowing
# arbitrary local second-order corrections r(u),s(u) (represented by symbols).
X = p*e + r*e**2
Y = q*e + s*e**2
inv = trunc(u**-4 * (1-X/u**4+X**2/u**8))
c = trunc((u**3+Y)*inv)
A = trunc(inv-trunc(c**4))
B = trunc(u*inv-trunc(c**3))
Pv = trunc(3*a*c**2+(3*b-4*d)*c+h)
Qv = trunc(2*a*c+2*b-3*d)
mV = trunc(Qv*A-Pv*B)
mU = trunc(q*X-p*Y)
Kfull = sp.expand(mV+u**-8*mU).coeff(e,2)
assert not Kfull.has(r, s), "All local quadratic corrections must cancel."

# Directly reconstruct the homogeneous linear normal transformation as well.
x, y = sp.symbols("x y")
T = sp.Matrix([[3*u**-8,-4*u**-7],[2*u**-7,-3*u**-6]])
assert sp.factor(T.det()) == -u**-14
assert sp.expand((Q*(T*sp.Matrix([x,y]))[0]
                 -P*(T*sp.Matrix([x,y]))[1])
                 +u**-8*(q*x-p*y)) == 0

K = sp.expand(u**8*Kfull)
expected = [
    h*(a*h+3*b**2-5*b*d+3*d**2),
    (b-d)*(4*a*h+3*b**2-8*b*d+6*d**2),
    a*(a*h+9*b**2-23*b*d+15*d**2),
]
actual = [sp.factor(K.coeff(u,-j)) for j in (1,2,3)]
assert all(sp.expand(x-y) == 0 for x,y in zip(actual,expected))

# The two-chart coboundary space is R[u] + u^-4 R[u^-1].  Therefore the
# following are the exact three obstruction coordinates, with no omitted
# Laurent terms.  A full cocycle decomposition is also verified.
nonnegative = 3*b*h**2+3*h**3*u
negative = 3*a**3/u**5+(9*a**2*b-12*a**2*d)/u**4
assert sp.expand(K-nonnegative-negative
                 -sum(expected[j-1]/u**j for j in (1,2,3))) == 0

# Prescribed reduction: a,b,h are even and d is odd.  Uniformly substitute
# the complete coefficient freedom and certify C2 = 2 modulo 4 coefficientwise.
aa, bb, hh, dd = sp.symbols("aa bb hh dd")
middle = sp.expand(expected[1].subs({a:2*aa,b:2*bb,h:2*hh,d:1+2*dd}))
assert all(int(v) % 4 == 0
           for v in sp.Poly(middle-2,aa,bb,hh,dd).coeffs())

print("PASS: exact integral raw normal transition and all quotient parameters")
print("PASS: arbitrary local quadratic embedding corrections cancel")
print("PASS: complete cocycle and H^1(O(-4)) coordinates")
for j, expr in enumerate(expected,1):
    print(f"C{j} = {sp.factor(expr)}")
print("PASS: prescribed reduction forces C2 = 2 (mod 4), for all corrections")
