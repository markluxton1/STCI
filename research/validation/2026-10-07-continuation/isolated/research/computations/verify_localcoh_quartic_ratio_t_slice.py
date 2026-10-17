#!/usr/bin/env python3
"""Exact linear classification of the quartic first-symbol ratio-t slice.

The entire slice consists of F=xH+zD, G=yH+wD with H,D in I(C0)_3.
This computation verifies the classification and its 14-dimensional size.
It does not by itself prove the all-stage ancestor exclusion; that proof uses
the finite-principal-part argument recorded in the companion research note.
Run with a Python interpreter containing SymPy.
"""

import sympy as sp

x, y, z, w, t, a, b = sp.symbols("x y z w t a b")
ambient = (x, y, z, w)
q = x * w - y * z
A = x**2 * z - y**3
B = x * z**2 - y**2 * w
C = y * w**2 - z**3
cubic_basis = [q * x, q * y, q * z, q * w, A, B, C]


def exponents(degree):
    return [
        (i, j, k, degree - i - j - k)
        for i in range(degree + 1)
        for j in range(degree - i + 1)
        for k in range(degree - i - j + 1)
    ]


def vector(polynomial, degree):
    polynomial = sp.Poly(sp.expand(polynomial), *ambient)
    return sp.Matrix([polynomial.coeff_monomial(e) for e in exponents(degree)])


quartic_candidates = [q * sp.prod(v**e for v, e in zip(ambient, mon))
                      for mon in exponents(2)]
quartic_candidates += [c * v for c in (A, B, C) for v in ambient]
quartic_vectors = sp.Matrix.hstack(*(vector(f, 4) for f in quartic_candidates))
_, pivots = quartic_vectors.rref()
quartic_basis = [quartic_candidates[i] for i in pivots]
assert len(quartic_basis) == 18

chart = {x: 1, y: t, z: t**3 + a, w: t**4 + t * a + b}


def normal_row(polynomial):
    expression = sp.expand(polynomial.subs(chart))
    return tuple(sp.expand(sp.diff(expression, v).subs({a: 0, b: 0}))
                 for v in (a, b))


def tvector(polynomial):
    return sp.Matrix([sp.expand(polynomial).coeff(t, i) for i in range(14)])


rows = [normal_row(f) for f in quartic_basis]
for ratio in (t, t**3):
    constraints = sp.Matrix.hstack(*(
        sp.Matrix.vstack(tvector(-ratio * r), tvector(-ratio * k))
        for r, k in rows
    ), *(
        sp.Matrix.vstack(tvector(r), tvector(k)) for r, k in rows
    ))
    assert len(constraints.nullspace()) == 14

classified_columns = []
for cubic in cubic_basis:
    classified_columns.append(sp.Matrix.vstack(vector(x * cubic, 4),
                                               vector(y * cubic, 4)))
for cubic in cubic_basis:
    classified_columns.append(sp.Matrix.vstack(vector(z * cubic, 4),
                                               vector(w * cubic, 4)))
classified = sp.Matrix.hstack(*classified_columns)
assert classified.rank() == 14

for cubic in cubic_basis:
    for F, G in ((x * cubic, y * cubic), (z * cubic, w * cubic)):
        rf, kf = normal_row(F)
        rg, kg = normal_row(G)
        assert sp.expand(rg - t * rf) == 0
        assert sp.expand(kg - t * kf) == 0

h_coeffs = sp.symbols("h0:7")
d_coeffs = sp.symbols("d0:7")
H = sum(c * v for c, v in zip(h_coeffs, cubic_basis))
D = sum(c * v for c, v in zip(d_coeffs, cubic_basis))
F = x * H + z * D
G = y * H + w * D
assert sp.expand(x * G - y * F - q * D) == 0
assert sp.expand(w * F - z * G - q * H) == 0
F_other = x * H + y * D
G_other = z * H + w * D
assert sp.expand(x * G_other - z * F_other - q * D) == 0
assert sp.expand(w * F_other - y * G_other - q * H) == 0
rf, kf = normal_row(F_other)
rg, kg = normal_row(G_other)
assert sp.expand(rg - t**3 * rf) == 0
assert sp.expand(kg - t**3 * kf) == 0

# The P-039 pair is H=A-lambda*B, D=lambda*A in this full slice.
lam = sp.symbols("lambda")
assert sp.expand(x * (A - lam * B) + z * lam * A
                 - (x * A + lam * y**2 * q)) == 0
assert sp.expand(y * (A - lam * B) + w * lam * A
                 - (y * A + lam * x * z * q)) == 0

print("PASS: entire ratio-t quartic slice has dimension 14")
print("PASS: unique representation F=xH+zD, G=yH+wD, H,D in I_3")
print("PASS: both determinant identities and P-039 specialization")
print("PASS: transposed ruling slice ratio-t^3 also has dimension 14")
