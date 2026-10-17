#!/usr/bin/env python3
"""Exact quartic symbol image and primitive direction ranks for C0.

Uses the balanced frame U=w-t^4-(3/2)t(z-t^3), V=z-t^3.
This verifies first-conormal statements, not higher ancestor equations.
Run with a Python interpreter containing SymPy.
"""

import sympy as sp

x, y, z, w, t, s = sp.symbols("x y z w t s")
ambient = (x, y, z, w)
chart = {x: 1, y: t, z: t**3, w: t**4}
q = x * w - y * z
A = x**2 * z - y**3
B = x * z**2 - y**2 * w
C = y * w**2 - z**3


def exponents(degree):
    return [
        (i, j, k, degree - i - j - k)
        for i in range(degree + 1)
        for j in range(degree - i + 1)
        for k in range(degree - i - j + 1)
    ]


def ambient_vector(polynomial, degree):
    polynomial = sp.Poly(sp.expand(polynomial), *ambient)
    return sp.Matrix([polynomial.coeff_monomial(m) for m in exponents(degree)])


def first_symbol(polynomial):
    P = sp.expand(sp.diff(polynomial, w).subs(chart))
    Q = sp.expand(
        (sp.diff(polynomial, z) + sp.Rational(3, 2) * y * sp.diff(polynomial, w))
        .subs(chart)
    )
    return P, Q


def symbol_vector(polynomial):
    P, Q = first_symbol(polynomial)
    assert sp.degree(P, t) <= 9 or P == 0
    assert sp.degree(Q, t) <= 9 or Q == 0
    return sp.Matrix([P.coeff(t, i) for i in range(10)]
                     + [Q.coeff(t, i) for i in range(10)])


quartic_monomials = [sp.prod(v**e for v, e in zip(ambient, m))
                    for m in exponents(4)]
restrictions = [sp.expand(m.subs(chart)) for m in quartic_monomials]
restriction_matrix = sp.Matrix(
    [[f.coeff(t, i) for f in restrictions] for i in range(17)]
)
assert restriction_matrix.shape == (17, 35)
assert restriction_matrix.rank() == 17
assert len(restriction_matrix.nullspace()) == 18

quadratic_lifts = [x**2, x * y, y**2, x * z, x * w,
                   y * w, z**2, z * w, w**2]
assert [sp.expand(H.subs(chart)) for H in quadratic_lifts] == [t**i for i in range(9)]
R_lifts = [x * A, y * A, z * A, w * A, z * B, w * B, -z * C, -w * C]
R_weights = [0, 1, 3, 4, 6, 7, 9, 10]
quartic_basis = [q * H for H in quadratic_lifts] + R_lifts + [q**2]
assert len(quartic_basis) == 18
assert all(sp.expand(F.subs(chart)) == 0 for F in quartic_basis)
assert sp.Matrix.hstack(*(ambient_vector(F, 4) for F in quartic_basis)).rank() == 18

image_matrix = sp.Matrix.hstack(*(symbol_vector(F) for F in quartic_basis))
assert image_matrix.rank() == 17
assert image_matrix.nullspace() == [sp.eye(18)[:, 17]]
constraints = sp.zeros(3, 20)
for row, k in enumerate((1, 4, 7)):
    constraints[row, k] = -sp.Rational(1, 2)
    constraints[row, 10 + k + 1] = 1
assert constraints.rank() == 3
assert constraints * image_matrix == sp.zeros(3, 18)
assert image_matrix.T.nullspace() == list(constraints.T.columnspace())

# The exceptional degree-one preimage is exactly q*S2: its nine-dimensional
# symbol image and the kernel q² account for all ten quartic dimensions.
q_quartic_basis = [q * sp.prod(v**e for v, e in zip(ambient, m))
                   for m in exponents(2)]
assert len(q_quartic_basis) == 10
assert sp.Matrix.hstack(*(ambient_vector(F, 4) for F in q_quartic_basis)).rank() == 10
assert sp.Matrix.hstack(*(symbol_vector(F) for F in q_quartic_basis)).rank() == 9
for F in q_quartic_basis:
    P_q, Q_q = first_symbol(F)
    assert sp.expand(2 * Q_q - t * P_q) == 0

assert first_symbol(A) == (0, 1)
assert first_symbol(B) == (-t**2, t**3 / 2)
assert first_symbol(C) == (2 * t**5, 0)
for F, weight in zip(R_lifts, R_weights):
    P, Q = first_symbol(F)
    assert sp.expand(Q - t * P / 2) == t**weight

# Universal exact inverse for a symbol satisfying the three constraints.
P_coeff = sp.symbols("P0:10")
Q_coeff = sp.symbols("Q0:10")
P = sum(P_coeff[i] * t**i for i in range(10))
Q = sum(Q_coeff[i] * t**i for i in range(10)).subs(
    {Q_coeff[2]: P_coeff[1] / 2,
     Q_coeff[5]: P_coeff[4] / 2,
     Q_coeff[8]: P_coeff[7] / 2}
)
R = sp.Poly(sp.expand(Q - t * P / 2), t)
J = sum(R.coeff_monomial(t**i) * F for i, F in zip(R_weights, R_lifts))
P_J, Q_J = first_symbol(J)
p = sp.expand(P - P_J)
assert p.coeff(t, 9) == 0
H = sum(p.coeff(t, i) * quadratic_lifts[i] for i in range(9))
F_lift = q * H + J
actual_P, actual_Q = first_symbol(F_lift)
assert sp.expand(actual_P - P) == 0
assert sp.expand(actual_Q - Q) == 0


def direction_matrix(degree):
    """Three constraints on h for arbitrary binary pair r of degree e."""
    a = sp.symbols(f"a0:{degree + 1}")
    b = sp.symbols(f"b0:{degree + 1}")
    matrix = sp.zeros(3, 10 - degree)
    for k in range(3):
        for i in range(degree + 1):
            j = 3 * k + 1 - i
            if 0 <= j < 10 - degree:
                matrix[k, j] += a[i]
            j = 3 * k + 2 - i
            if 0 <= j < 10 - degree:
                matrix[k, j] -= 2 * b[i]
    return a, b, matrix


a0, b0, M0 = direction_matrix(0)
assert M0[:, [1, 4, 7]].det() == a0[0]**3
assert M0[:, [2, 5, 8]].det() == -8 * b0[0]**3

a1, b1, M1 = direction_matrix(1)
assert M1[:, [0, 3, 6]].det() == a1[1]**3
assert sp.expand(M1[:, [1, 4, 7]].det() - (a1[0] - 2 * b1[1])**3) == 0
assert M1[:, [2, 5, 8]].det() == -8 * b1[0]**3
assert M1.subs({a1[1]: 0, a1[0]: 2 * b1[1], b1[0]: 0}) == sp.zeros(3, 9)

a2, b2, M2 = direction_matrix(2)
D, E, T, K = sp.symbols("D E T K")
expected = sp.Matrix([
    [D, E, K, 0, 0, 0, 0, 0],
    [0, 0, T, D, E, K, 0, 0],
    [0, 0, 0, 0, 0, T, D, E],
])
changed = M2.subs({a2[0]: E + 2 * b2[1], a2[1]: D + 2 * b2[2],
                   a2[2]: T, b2[0]: -K / 2})
assert changed == expected
assert expected[:, [0, 3, 6]].det() == D**3
assert expected[:, [1, 4, 7]].det() == E**3
exceptional = expected.subs({D: 0, E: 0})
assert exceptional[:, [2, 5]] == sp.Matrix([[K, 0], [T, K], [0, T]])
assert exceptional[:2, [2, 5]].det() == K**2
assert exceptional[1:, [2, 5]].det() == T**2
assert exceptional.subs({T: 0, K: 0}) == sp.zeros(3, 8)
r1 = a2[0] * s**2 + a2[1] * s * t + a2[2] * t**2
r2 = b2[0] * s**2 + b2[1] * s * t + b2[2] * t**2
rank_zero = {a2[0]: 2 * b2[1], a2[1]: 2 * b2[2], a2[2]: 0, b2[0]: 0}
assert sp.expand(r1.subs(rank_zero) - 2 * s * (b2[1] * s + b2[2] * t)) == 0
assert sp.expand(r2.subs(rank_zero) - t * (b2[1] * s + b2[2] * t)) == 0

# All primitive rank-two directions have kernel h2=h5=0, and the
# homogeneous resultant explicitly cuts out the basepoint-free open subset.
assert len(exceptional.nullspace()) == 6
assert exceptional.nullspace() == [sp.eye(8)[:, j] for j in (0, 1, 3, 4, 6, 7)]
resultant = sp.resultant(a2[0] + a2[1] * t + a2[2] * t**2,
                         2 * b2[0] + a2[0] * t + a2[1] * t**2, t)
assert sp.expand(resultant - (
    a2[0]**3 * a2[2] - 6 * a2[0] * a2[1] * a2[2] * b2[0]
    + 2 * a2[1]**3 * b2[0] + 4 * a2[2]**2 * b2[0]**2
)) == 0

# Primitive witnesses verify both degree-two ranks, including infinity.
assert M2.subs({a2[0]: 0, a2[1]: 0, a2[2]: 1,
                b2[0]: 1, b2[1]: 0, b2[2]: 0}).rank() == 2
assert M2.subs({a2[0]: 1, a2[1]: 0, a2[2]: 0,
                b2[0]: 0, b2[1]: 0, b2[2]: 1}).rank() == 3

print("PASS: dim I4=18; balanced symbol image rank17; kernel kq²")
print("PASS: image equations P1=2Q2, P4=2Q5, P7=2Q8")
print("PASS: universal exact quartic lift F=qH(P-P_J)+J+cq²")
print("PASS: e0 intersection dimension7 for every direction")
print("PASS: e1 dimension9 at r~(2s,t), dimension6 elsewhere")
print("PASS: e2 dimension6 at a0=2b1,a1=2b2, dimension5 elsewhere")
print("PASS: excluded e2 rank0 directions have a common linear factor")
print("PASS: all primitive e2 rank2 scalar kernels are h2=h5=0")
print("PASS: exact homogeneous resultant on exceptional e2 directions")
print("PASS: exceptional e1 quartic preimage is exactly q*S2")
