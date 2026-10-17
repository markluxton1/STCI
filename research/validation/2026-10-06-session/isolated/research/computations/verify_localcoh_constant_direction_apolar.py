#!/usr/bin/env python3
"""Exact minimum pole-divisor bound for a constant-direction triple contact.

P-010's class is h_theta in H1(O(-7)). A common quartic scalar divisor D
must kill this class after allowing meromorphic quadratic correction with
poles bounded by D. This checks all divisors of degrees one, two, three.
"""
import sympy as sp

z, theta = sp.symbols("z theta")
h = theta**3*z**-5 - theta**2*sp.Rational(1, 2)*z**-4
h += theta*sp.Rational(1, 4)*z**-3 - sp.Rational(1, 8)*z**-2

def multiplication_matrix(class_expression, degree):
    return sp.Matrix([
        [sp.expand(z**i*class_expression).coeff(z, -j) for i in range(degree+1)]
        for j in range(1, 7-degree)
    ])

m1 = multiplication_matrix(h, 1)
m2 = multiplication_matrix(h, 2)
m3 = multiplication_matrix(h, 3)
assert m1.rank() == 2
assert m2.rank() == 3
assert m3.rank() == 3
expected = sp.Matrix([0, 2*theta, 1, 0])
assert m3*expected == sp.zeros(3, 1)
assert len(m3.nullspace()) == 1

# The symbolic degree-two rank requires theta!=0. Its fixed 3x3 minor
# below gives that precise boundary, without relying on generic rank alone.
minor = sp.factor(m2.extract([0, 1, 3], [0, 1, 2]).det())
assert minor == -theta**4 / 32
assert m1.extract([0, 1], [0, 1]).det() == -sp.Rational(1, 64)
assert len(m2.subs(theta, 0).nullspace()) == 1
assert m2.subs(theta, 0).nullspace()[0] == sp.Matrix([0, 0, 1])

# The missing direction m=v has class z^-5. Its minimum pole divisor
# has degree two, supported twice at infinity (homogeneous polynomial s^2).
infinity = z**-5
assert multiplication_matrix(infinity, 1).rank() == 2
assert multiplication_matrix(infinity, 2).nullspace() == [sp.Matrix([1, 0, 0])]

example_D = z**4-z**3-3*z**2-z+1
assert all(sp.expand(example_D*h.subs(theta, sp.Rational(1,2))).coeff(z,-j) == 0
           for j in (1,2))
print("PASS: mixed constant directions require common scalar divisor degree at least three")
print("PASS: degree-three divisor is exactly s*t*(t+2*theta*s), up to scale")
print("PASS: axis directions require degree-two pole divisors t^2 or s^2")
print("PASS: explicit mixed-contact pair's degree-four divisor kills h_(1/2)")
