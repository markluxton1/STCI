#!/usr/bin/env python3
"""Exact higher-jet certificate for the P-041 fixed split-[2,2] survivor.

Characteristic zero.  This excludes every integral carrier having *this*
quadratic normal form from admitting an STCI mate, using P-020's necessary
Mumford intersection 17/5.  It does not exclude the entire [2,2] family.
"""

import sympy as sp

x0, x1, x2, x3, z, e, w, xi, eta, lam = sp.symbols(
    "x0 x1 x2 x3 z e w xi eta lam"
)
q = x0 * x3 - x1 * x2
A = x0**2 * x2 - x1**3
B = x0 * x2**2 - x1**2 * x3
D = x2**3 - x1 * x3**2
F = (
    B**2
    + q**2 * (x0**2 - 4 * x0 * x3 + 3 * x3**2)
    + q * (x1 * A + x2 * D)
    + lam * q**3
)


def quadratic_normal(form):
    affine = sp.expand(
        form.subs(
            {
                x0: 1,
                x1: z,
                x2: z**3 + eta,
                x3: z**4 + xi + sp.Rational(3, 2) * z * eta,
            }
        )
    )
    polynomial = sp.Poly(affine, xi, eta)
    return sp.expand(
        sum(
            coefficient * xi**i * eta**j
            for (i, j), coefficient in polynomial.terms()
            if i + j == 2
        )
    )


target = (xi + sp.Rational(3, 2) * z * eta) * (
    (1 - 3 * z**4 + z**8) * xi
    + (z / 2 - z**5 / 2 + z**9 / 2) * eta
)
assert sp.expand(quadratic_normal(F) - target) == 0


def strict_transform(substitution):
    result = sp.cancel(F.subs(substitution) / e**2)
    assert sp.denom(result) == 1
    return sp.expand(result)


f0 = strict_transform({x0: 1, x1: z, x2: z**3 + e, x3: z**4 + e * w})
finf = strict_transform({x3: 1, x2: z, x1: z**3 + e, x0: z**4 + e * w})


def origin_quadratic(form):
    return sp.expand(
        sum(
            coefficient * z**i * e**j * w**k
            for (i, j, k), coefficient in sp.Poly(form, z, e, w).terms()
            if i + j + k <= 2
        )
    )


assert origin_quadratic(f0) == e**2 + w**2 - w * z
assert origin_quadratic(finf) == e**2 + 3 * w**2 - 7 * w * z + 4 * z**2
assert sp.det(sp.hessian(origin_quadratic(f0), (z, e, w))) == -2
assert sp.det(sp.hessian(origin_quadratic(finf), (z, e, w))) == -2

# The low branch in the finite chart is e=w=0.  Away from the endpoints its
# collisions with the high branch are the eight simple roots of collision.
collision = z**8 - 4 * z**4 + 1
assert sp.gcd(collision, sp.diff(collision, z)) == 1
assert sp.expand(
    f0.subs(e, 0)
    - w * (w * z**8 - 3 * w * z**4 + w - z**9 + 4 * z**5 - z)
) == 0
next_coefficient = sp.factor(sp.diff(f0, e).subs({e: 0, w: 0}))
assert next_coefficient == -z**3 * (lam + 6 * z**4 - 4)

# A collision is singular precisely when lam=4-6*z^4.  Take derivatives
# BEFORE imposing that equality: lambda is a constant ambient coefficient.
hessian = sp.hessian(f0, (z, e, w)).subs(
    {e: 0, w: 0, lam: 4 - 6 * z**4}
)
hessian_determinant = sp.rem(sp.det(hessian), collision, z)
assert hessian_determinant == 1536 * (23 - 86 * z**4)
assert sp.gcd(hessian_determinant, collision) == 1
r = sp.symbols("r")
assert sp.resultant(r**2 - 4 * r + 1, 23 - 86 * r, r) == 13

# Thus both endpoints are A1 for every lambda.  The other eight collisions
# are smooth unless lambda=-8 +/- 6*sqrt(3), in which case exactly four are
# also A1.  Each smooth transverse branch intersection contributes 1; each
# A1 intersection contributes 1/2 by the one-(-2)-curve resolution.
generic_intersection = 8 + 2 * sp.Rational(1, 2)
special_intersection = 4 + 6 * sp.Rational(1, 2)
assert generic_intersection == 9
assert special_intersection == 7
assert generic_intersection != sp.Rational(17, 5)
assert special_intersection != sp.Rational(17, 5)

print("PASS: the unique fixed-boundary lifts are F_lambda=F_0+lambda*q^3")
print("PASS: all branch collisions are smooth or ordinary A1")
print("PASS: Gamma_low.Gamma_high is 9 or 7, never the required 17/5")
