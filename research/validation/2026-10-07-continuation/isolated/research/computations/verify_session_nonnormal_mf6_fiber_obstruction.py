#!/usr/bin/env python3
"""Exact identities for the four MF6 boundary-carrier fiber obstruction.

This verifies algebraic identities, not an exhaustive classification of
nonnormal quartics.  The proof of finite normalization and arbitrary-degree
mate exclusion is in the companion independent audit note.
"""

import sympy as s

b, u, v = s.symbols("b u v")
a = b + 1
p = 3 * b**2 - 2 * b + 1
x0, x1, x2, x3, S, T = s.symbols("x0 x1 x2 x3 S T")


def zero(expression):
    assert s.expand(expression) == 0, s.factor(expression)


def modulo_p(expression):
    num, den = s.cancel(expression).as_numer_denom()
    assert s.rem(s.Poly(num, b), s.Poly(p, b)).as_expr() == 0
    assert s.gcd(s.Poly(den, b), s.Poly(p, b)).degree() == 0


F0 = x0**3 * x3 - a * x0**2 * x1 * x2 + b * x1**4
X1 = u**2 * (a * v - u) / b
X0 = u * X1
monic = u**3 - a * v * u**2 + b * x1
zero(monic.subs(x1, X1))
zero(F0.subs({x0: X0, x1: X1, x2: v, x3: 1}))
zero(F0.subs({x0: S**4, x1: S**3*T, x2: S*T**3, x3: T**4}))
assert s.gcd(x0**2*x1, x0**3+b*x1**4) == 1

# Exact elementary generator operations; the residual cofactor has support
# only at u=v=0, which is already on the diagonal.
K = u**2 - b*u*v - b*v**2
g1, g2 = X1-v**3, X0-v**4
zero(g1 + (u-v)*K/b)
zero(g2-u*g1-(u-v)*v**3)
zero(K.subs(v, 0)-u**2)

# Same original double-line point, for all v, with distinct preimages if v!=0.
for coordinate in (X0, X1, v):
    zero(coordinate.subs(u, 0)-coordinate.subs(u, a*v))
zero((v-u).subs(u, a*v)+b*v)

# Quadratic-field involution and norm.  If (-b)^n=1, conjugation and
# multiplication force (1/3)^n=1 for a positive integer n in characteristic 0.
b_star = s.Rational(2, 3)-b
zero(p.subs(b, b_star)-p)
modulo_p(b*b_star-s.Rational(1, 3))
assert p.subs(b, 0) != 0 and p.subs(b, -1) != 0
assert s.discriminant(p, b) == -8
assert s.Poly(p, b).is_irreducible

# The second displayed pencil member is coordinate reversal of the conjugate.
F1 = x0*x3**3+(b-s.Rational(5, 3))*x1*x2*x3**2+(s.Rational(2, 3)-b)*x2**4
reversed_F0 = F0.subs(b, b_star).xreplace({x0:x3, x1:x2, x2:x1, x3:x0})
zero(F1-reversed_F0)
print("PASS: monic normalization equation, birational coordinate, kernel gcd,")
print("full inverse-image ideal identities, duplicate-fiber ratio, quadratic norm,")
print("and exact coordinate-reversal/conjugation identity.")
