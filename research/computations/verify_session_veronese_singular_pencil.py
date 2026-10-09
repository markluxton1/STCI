#!/usr/bin/env python3
"""Exact identities for the singular-pencil Veronese projection note.

This verifier does not claim to replace the primitive-adjugate classification
or function-field degree proof in the accompanying note.
"""

import sympy as sp

s, t, alpha, beta, x, y, z, zz = sp.symbols("s t alpha beta x y z zz")
matrix = sp.Matrix([[0, 0, t], [0, 0, s], [t, s, alpha*s+beta*t]])
kernel = sp.Matrix([s, -t, 0])
assert matrix.det() == 0
assert matrix * kernel == sp.zeros(3, 1)
assert sp.simplify(matrix.adjugate() + kernel * kernel.T) == sp.zeros(3)
assert matrix.extract([0, 2], [0, 2]).det() == -t**2
assert matrix.extract([1, 2], [1, 2]).det() == -s**2

center = sp.Matrix([0, 0, 0, t, s, alpha*s+beta*t])
annihilator = sp.Matrix([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, -beta, -alpha, 1],
])
assert annihilator * center == sp.zeros(4, 1)
veronese = sp.Matrix([x*x, x*y, y*y, x*z, y*z, z*z])
image = annihilator * veronese
assert sp.expand(image[0] * image[2] - image[1]**2) == 0
linear = beta*x + alpha*y
completed = sp.expand(image[3].subs(z, zz+linear/2) + linear**2/4)
assert completed == zz**2

print("PASS: determinant, primitive linear kernel, adjugate, rank-two minors,")
print("      center annihilator, quadric image, and square completion identities.")
print("Scope: symbolic identities over ZZ; square completion requires char != 2.")
