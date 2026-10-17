#!/usr/bin/env python3
"""Exact audit of the primitive-triple obstruction for all rational quartics.

The marked normal form is the graph of

    f_lambda(z) = z^2 (z - 1) / (z - lambda),  lambda != 0,1.

Together with the separately checked z^3 orbit, these marked maps cover every
left-right PGL(2) orbit of separable degree-three maps in characteristic zero.
All calculations below are over QQ(lambda).
"""

import sympy as sp

z, lam, u, v, T, A, B = sp.symbols("z lam u v T A B")
D = z - lam
N = z**2 * (z - 1)
f = N / D

# Inverse of the U-side split-frame change.
Y = (u - z * v) / 2
X = ((2 * lam - z) * v - u) / (2 * D)
a = X / D**2
b = Y / D**2

# Taylor coefficients of the raw x0-to-x3 chart transition.
fp = sp.diff(f, z)
fpp = sp.diff(f, z, 2)
A1 = -f**-2
B1 = (z * fp - f) / (z * f**3)
C1 = 1 / (z**2 * f**2)
A2 = f**-3
B2 = (2 * f - z * fp) / (z * f**4)
C2 = 1 / (z**2 * f**3) + fpp / (2 * f**4) - fp**2 / f**5
D2 = -2 / (z**2 * f**3)
E2 = -2 / (z**3 * f**3)

S0 = (z - 1) ** 2 / z**2
dW1 = -b / (z**2 * f)
S1 = 2 * (z - 1) * b / (z**3 * f)

Xp_lin = S0 * (A1 * a + B1 * b)
Xp_quad = S0 * (A2 * a**2 + B2 * a * b + C2 * b**2) + S1 * (
    A1 * a + B1 * b
)
Yp_lin = S0 * C1 * b
Yp_quad = S0 * (D2 * a * b + E2 * b**2) + S1 * C1 * b

# V-side gauge Xbar'=X'-Y'/(1-W), followed by the split frame
# u'=Xbar', v'=W Xbar'-2Y'.
p0 = -z / (z - 1)
p1 = b / ((z - 1) ** 2 * f)
ubar_lin = sp.factor(Xp_lin + p0 * Yp_lin)
ubar_quad = sp.factor(Xp_quad + p0 * Yp_quad + p1 * Yp_lin)
vbar_lin = sp.factor(ubar_lin / z - 2 * Yp_lin)
vbar_quad = sp.factor(ubar_quad / z + dW1 * ubar_lin - 2 * Yp_quad)
assert sp.simplify(ubar_lin - z**-7 * u) == 0
assert sp.simplify(vbar_lin - z**-7 * v) == 0

# BF cocycle on the finite kernel chart m=u+T*v, ell=v.
h = sp.factor(z**7 * (ubar_quad + T * vbar_quad).subs(u, -T * v) / v**2)
h_expected = -(
    (T + z)
    * (
        z**4
        - (3 * lam + 2 * T + 1) * z**3
        + (3 * lam + 3 * T**2 + 4 * T) * z**2
        - (3 * lam * T**2 + 2 * lam * T + T**2) * z
        + lam * T**2
    )
    / (4 * z**4 * (z - lam) ** 2 * (z - 1) ** 2)
)
assert sp.simplify(h - h_expected) == 0


def principal_part_order_two(expr, point):
    """Return the order-at-most-two principal part at a finite point."""

    regularized = sp.cancel((z - point) ** 2 * expr)
    c2 = sp.simplify(sp.limit(regularized, z, point))
    c1 = sp.simplify(sp.limit(sp.diff(regularized, z), z, point))
    return sp.cancel(c2 / (z - point) ** 2 + c1 / (z - point))


# Reduce the Cech cocycle for U=P1-{infinity,lambda}, V=P1-{0,1}.
# Principal parts at lambda are U-coboundaries, principal parts at 1 are
# V-coboundaries, and the quotient term below is also a V-coboundary.  The
# residual coefficients of z^-1,...,z^-6 are the standard H^1(O(-7)) class.
P_lam = principal_part_order_two(h, lam)
h1 = sp.cancel(h - P_lam)
P_1 = principal_part_order_two(h1, 1)
num, den = sp.fraction(sp.cancel(z**7 * P_1))
quot, _rem = sp.div(sp.Poly(num, z), sp.Poly(den, z))
h_reduced = sp.cancel(h1 - P_1 + z**-7 * quot.as_expr())
poly = sp.Poly(sp.cancel(z**7 * h_reduced), z)
c = [sp.factor(poly.coeff_monomial(z ** (7 - j))) for j in range(1, 7)]

# Multiply by a common unit on lambda != 0,1 and homogenize T=B/A.
common_unit = 4 * lam**4 * (lam - 1) ** 2
G = [sp.factor(A**3 * (common_unit * cj).subs(T, B / A)) for cj in c]
expected = [
    (A * lam + B)
    * (
        (5 * lam**3 - 3 * lam**2) * A**2
        + (6 * lam**2 - 2 * lam) * A * B
        + (3 * lam - 1) * B**2
    ),
    lam
    * (A * lam + B)
    * (
        (3 * lam**3 - lam**2) * A**2
        + 4 * lam**2 * A * B
        + (3 * lam - 1) * B**2
    ),
    lam**2
    * (
        (3 * lam**3 - lam**2) * A**3
        + (3 * lam**3 + 3 * lam**2) * A**2 * B
        + (5 * lam**2 + lam) * A * B**2
        + (3 * lam - 1) * B**3
    ),
    lam**3
    * (
        (3 * lam**2 - lam) * A**3
        + (5 * lam**2 + lam) * A**2 * B
        + (3 * lam**2 + 3 * lam) * A * B**2
        + (3 * lam - 1) * B**3
    ),
    lam**4
    * (A + B)
    * ((3 * lam - 1) * A**2 + 4 * lam * A * B + (3 * lam - 1) * B**2),
    lam**4
    * (A + B)
    * (
        (3 * lam - 1) * A**2
        + 2 * (3 * lam - 1) * A * B
        + (5 * lam - 3) * B**2
    ),
]
assert all(sp.expand(actual - wanted) == 0 for actual, wanted in zip(G, expected))

# Non-incidence on A != 0.  If all six coordinates vanished, the first
# difference would force T=-lambda.  Substitution in the second difference is
# 2*lambda*(lambda-1)^3, which is nonzero on the marked parameter space.
finite = [sp.factor(g.subs({A: 1, B: T})) for g in G]
f1 = finite[0]
f2 = finite[1] / lam
f5 = finite[4] / lam**4
f6 = finite[5] / lam**4
assert sp.factor(f1 - f2) == 2 * lam * (lam - 1) * (lam + T) ** 2
assert sp.factor(f5 - f6) == -2 * T * (lam - 1) * (T + 1) ** 2
assert sp.factor((f5 - f6).subs(T, -lam)) == 2 * lam * (lam - 1) ** 3

# Direct check of A=0, represented by the kernel m=v, ell=u.  Simultaneous
# vanishing would require both 3*lambda-1=0 and 5*lambda-3=0.
h_inf = sp.factor(z**7 * vbar_quad.subs(v, 0) / u**2)
P_lam_inf = principal_part_order_two(h_inf, lam)
h1_inf = sp.cancel(h_inf - P_lam_inf)
P_1_inf = principal_part_order_two(h1_inf, 1)
num_inf, den_inf = sp.fraction(sp.cancel(z**7 * P_1_inf))
quot_inf, _rem_inf = sp.div(sp.Poly(num_inf, z), sp.Poly(den_inf, z))
h_reduced_inf = sp.cancel(h1_inf - P_1_inf + z**-7 * quot_inf.as_expr())
poly_inf = sp.Poly(sp.cancel(z**7 * h_reduced_inf), z)
G_inf = [
    sp.factor(common_unit * poly_inf.coeff_monomial(z ** (7 - j)))
    for j in range(1, 7)
]
assert G_inf == [
    3 * lam - 1,
    lam * (3 * lam - 1),
    lam**2 * (3 * lam - 1),
    lam**3 * (3 * lam - 1),
    lam**4 * (3 * lam - 1),
    lam**4 * (5 * lam - 3),
]
assert sp.solve([3 * lam - 1, 5 * lam - 3], [lam], dict=True) == []

print("ALL-RATIONAL-QUARTIC PRIMITIVE OBSTRUCTION VERIFIED")
for j, coordinate in enumerate(G, 1):
    print(f"G{j} = {sp.factor(coordinate)}")
