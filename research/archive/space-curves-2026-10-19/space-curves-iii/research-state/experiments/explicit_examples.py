"""Lightweight symbolic checks for the initial space-curve examples.

Dependency: sympy. This script verifies identities only; it does not compute
primary decompositions or prove the general STCI statements.
"""

import sympy as sp


x, y, z, w, s, t = sp.symbols("x y z w s t")

# Rational quartic [s^4:s^3 t:s t^3:t^4].
q = x * w - y * z
g = y**3 - x**2 * z
h = z**3 - y * w**2
r = x * z**2 - y**2 * w
quartic_parametrization = {x: s**4, y: s**3 * t, z: s * t**3, w: t**4}

print(
    "rational quartic substitutions:",
    [sp.expand(form.subs(quartic_parametrization)) for form in (q, g, h, r)],
)
print(
    "q,g on residual line x=y=0:",
    [sp.expand(form.subs({x: 0, y: 0})) for form in (q, g)],
)
print(
    "q,h on residual line z=w=0:",
    [sp.expand(form.subs({z: 0, w: 0})) for form in (q, h)],
)

# Two singular cubic surfaces through the rational quartic.
ruled_cubic = r
ruled_partials = [sp.diff(ruled_cubic, variable) for variable in (x, y, z, w)]
print("ruled cubic partials:", ruled_partials)
print(
    "ruled cubic singular-line check y=z=0:",
    [sp.expand(form.subs({y: 0, z: 0})) for form in ruled_partials],
)

# On the affine chart w=1 of the cuspidal cubic g=0, write
# z=V^3, tau=UV^2, y=U^2V, x=U^3 in the normalization. The lift of
# C is U=V^4. Its third multiple is the invariant Cartier divisor
# cut out by (U-V^4)^3.
U, V, tau = sp.symbols("U V tau")
normalization_substitution = {
    x: U**3,
    y: U**2 * V,
    tau: U * V**2,
    z: V**3,
}
cartier_function = x - 3 * y * z + 3 * tau * z**2 - z**4
print(
    "cuspidal normalization Cartier identity:",
    sp.factor(cartier_function.subs(normalization_substitution)),
)
print(
    "cuspidal conductor restriction modulo x=y=tau^2=0:",
    3 * tau * z**2 - z**4,
)

# Twisted cubic [s^3:s^2 t:s t^2:t^3].
q1 = x * z - y**2
q2 = x * w - y * z
q3 = y * w - z**2
certificate = z * q3 - w * q2
twisted_parametrization = {x: s**3, y: s**2 * t, z: s * t**2, w: t**3}

print(
    "twisted cubic substitutions:",
    [sp.expand(form.subs(twisted_parametrization)) for form in (q1, certificate)],
)

u, v = sp.symbols("u v")
patch_certificate = sp.factor(certificate.subs({x: 1, y: u, z: u**2, w: v}))
print("twisted cubic x=1 patch after q1:", patch_certificate)
