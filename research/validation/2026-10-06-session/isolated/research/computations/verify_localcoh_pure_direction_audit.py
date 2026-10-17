#!/usr/bin/env python3
"""Independent exact audit of pure constant quartic direction contact.

Verifies the ambient basis, curvature coefficient, exhaustive pivot
elimination identities, and reversal action. The global ancestor
implication uses the proven sheaf propagation and primitive-triple inputs.
"""

import sympy as sp

x, y, z, w, t, U, V = sp.symbols("x y z w t U V")
q = x * w - y * z
A = x**2 * z - y**3
B = x * z**2 - y**2 * w
C = y * w**2 - z**3
weights = (0, 1, 3, 4, 6, 7, 9)
cf = dict(zip(weights, sp.symbols("f0 f1 f3 f4 f6 f7 f9")))
cg = dict(zip(weights, sp.symbols("g0 g1 g3 g4 g6 g7 g9")))
kf, kg = sp.symbols("kf kg")
basis = [x * A, y * A, z * A, w * A,
         z * B + q * y * w, w * B + q * z**2,
         -z * C + 2 * q * w**2, q**2]
F = sum(cf[i] * b for i, b in zip(weights, basis)) + kf * basis[-1]
G = sum(cg[i] * b for i, b in zip(weights, basis)) + kg * basis[-1]
hF = sum(cf[i] * t**i for i in weights)
hG = sum(cg[i] * t**i for i in weights)
RF = kf + cf[6] * t - cf[7] * t**2 + 3 * cf[9] * t**4
RG = kg + cg[6] * t - cg[7] * t**2 + 3 * cg[9] * t**4
chart = {x: 1, y: t, z: t**3 + V,
         w: t**4 + U + sp.Rational(3, 2) * t * V}
F_normal = sp.expand(F.subs(chart))
assert sp.expand(sp.diff(F_normal, U).subs({U: 0, V: 0})) == 0
assert sp.expand(sp.diff(F_normal, V).subs({U: 0, V: 0}) - hF) == 0
assert sp.expand(F_normal.subs(V, 0) - RF * U**2 - 2 * cf[9] * U**3) == 0
delta = sp.Poly(sp.expand(hF * RG - hG * RF), t)

# Pivot f9!=0 after subtracting a scalar multiple to kill g9.
case9 = delta.as_expr().subs(cg[9], 0)
assert sp.expand(case9).coeff(t, 11) == -4 * cf[9] * cg[7]
case9 = case9.subs(cg[7], 0)
assert sp.expand(case9).coeff(t, 10) == -2 * cf[9] * cg[6]
case9 = case9.subs(cg[6], 0)
assert sp.expand(case9).coeff(t, 9) == cf[9] * kg

# Pivot f7!=0, with f9=g9=0 and the scalar adjustment killing g7.
case7 = delta.as_expr().subs({cf[9]: 0, cg[9]: 0, cg[7]: 0})
assert sp.expand(case7).coeff(t, 8) == 2 * cf[7] * cg[6]
case7 = case7.subs(cg[6], 0)
assert sp.expand(case7).coeff(t, 7) == cf[7] * kg

# Pivot f6!=0, with both higher coefficients zero and g6 killed.
case6 = delta.as_expr().subs({cf[9]: 0, cg[9]: 0, cf[7]: 0,
                             cg[7]: 0, cg[6]: 0})
assert sp.expand(case6).coeff(t, 6) == cf[6] * kg

# Last pivot kf!=0: all f6,f7,f9,g6,g7,g9 vanish and kg is killed.
R_zero_g = {cg[9]: 0, cg[7]: 0, cg[6]: 0, kg: 0}
assert RG.subs(R_zero_g) == 0
assert sp.expand(delta.as_expr().subs(R_zero_g) + hG.subs(R_zero_g) * RF) == 0
R_zero_f = {cf[9]: 0, cf[7]: 0, cf[6]: 0, kf: 0}
assert sp.expand(F.subs(R_zero_f) - A * (cf[0] * x + cf[1] * y
                                       + cf[3] * z + cf[4] * w)) == 0

# Exact implicit-function quadratic coefficient, without dividing any
# coefficient in the ambient parametrization.
G_normal = sp.expand(G.subs(chart))
restricted_G = sp.expand(G_normal.subs(V, -RF / hF * U**2))
assert sp.simplify(restricted_G.coeff(U, 2) - (hF * RG - hG * RF) / hF) == 0


def first_symbol(polynomial):
    restriction = {x: 1, y: t, z: t**3, w: t**4}
    P = sp.expand(sp.diff(polynomial, w).subs(restriction))
    Q = sp.expand((sp.diff(polynomial, z)
                   + sp.Rational(3, 2) * y * sp.diff(polynomial, w))
                  .subs(restriction))
    return P, Q


def reverse(polynomial):
    return polynomial.xreplace({x: w, y: z, z: y, w: x})


quadratic_lifts = [x**2, x * y, y**2, x * z, x * w,
                   y * w, z**2, z * w, w**2]
full_basis = [q * H for H in quadratic_lifts] + [x * A, y * A, z * A, w * A,
                                               z * B, w * B, -z * C, -w * C, q**2]
assert len(full_basis) == 18
for polynomial in full_basis:
    P, Q = first_symbol(polynomial)
    Pr, Qr = first_symbol(reverse(polynomial))
    assert sp.expand(Pr - 2 * t**9 * Q.subs(t, 1 / t)) == 0
    assert sp.expand(Qr - t**9 * P.subs(t, 1 / t) / 2) == 0
assert sp.expand(reverse(q) - q) == 0
assert sp.expand(reverse(B) + B) == 0
assert sp.expand(reverse(x * z) - y * w) == 0
assert sp.expand(reverse(y * w) - x * z) == 0

print("PASS: full pure-V space and exact transverse expansion")
print("PASS: exhaustive c9,c7,c6,kappa pivot contact identities")
print("PASS: R=0 forms lie in A*S1; zero-symbol boundary included")
print("PASS: generic quadratic quotient coefficient is delta/hF")
print("PASS: reversal exchanges pure constant directions and target classes")
