#!/usr/bin/env python3
"""Independent global-source and boundary calculation for the smooth residual.

Only the standard library is used. The QQ Macaulay2 companion verifies the
projective residual geometry; this file verifies the actual polynomial
restriction, first symbols, and squarefree degree-eighteen determinant.
"""
import json
from fractions import Fraction
from pathlib import Path


def add(*polys):
    out = {}
    for p in polys:
        for m, c in p.items():
            out[m] = out.get(m, 0) + c
    return {m: c for m, c in out.items() if c}


def scale(p, c):
    return {m: c * a for m, a in p.items() if c * a}


def mul(p, q):
    out = {}
    for m, a in p.items():
        for n, b in q.items():
            key = tuple(x + y for x, y in zip(m, n))
            out[key] = out.get(key, 0) + a * b
    return {m: c for m, c in out.items() if c}


def monomial(*powers):
    return {powers: 1}


x0, x1, x2, x3 = (monomial(*(int(i == j) for i in range(4))) for j in range(4))
power = lambda x, n: monomial(*(n * a for a in next(iter(x))))
q = add(mul(x0, x3), scale(mul(x1, x2), -1))
cubic_a = add(power(x1, 3), scale(mul(power(x0, 2), x2), -1))
cubic_d = add(power(x2, 3), scale(mul(x1, power(x3, 2)), -1))
f0 = add(power(x1, 4), scale(mul(power(x0, 3), x3), -1))
g0 = add(power(x2, 4), scale(mul(x0, power(x3, 3)), -1))
h0 = add(*(power(x, 2) for x in (x0, x1, x2, x3)),
         mul(x0, x2), scale(mul(x1, x3), 2))
h1 = add(scale(power(x0, 2), 2), scale(power(x1, 2), 3),
         scale(power(x2, 2), 5), scale(power(x3, 2), 7),
         mul(x0, x1), mul(x0, x3), mul(x1, x2),
         scale(mul(x2, x3), 3))
f = add(f0, mul(q, h0), scale(mul(x0, cubic_a), 2))
g = add(g0, mul(q, h1), scale(mul(x3, cubic_d), 3))


def restriction(p):
    out = {}
    for m, c in p.items():
        w = m[1] + 3 * m[2] + 4 * m[3]
        out[(w,)] = out.get((w,), 0) + c
    return {m: c for m, c in out.items() if c}


def first_symbol(p):
    """Coefficients of X,Y at x0=1,x1=u,x2=u^3+Y,x3=u^4+X."""
    a, b = {}, {}
    for m, c in p.items():
        w = m[1] + 3 * m[2] + 4 * m[3]
        if m[3]:
            a[(w - 4,)] = a.get((w - 4,), 0) + c * m[3]
        if m[2]:
            b[(w - 3,)] = b.get((w - 3,), 0) + c * m[2]
    return add(a), add(b)


af, bf = first_symbol(f)
ag, bg = first_symbol(g)
det = add(mul(af, bg), scale(mul(bf, ag), -1))
u = {(1,): 1}
one = {(0,): 1}
expected = add(
    mul(add(u, scale(one, 2)), restriction(h1)),
    mul({(9,): 1}, mul(add(one, scale(u, 3)), restriction(h0))),
    {(8,): -6, (9,): -16, (10,): -9},
)
assert restriction(f) == restriction(g) == {}
assert det == expected and all(sum(m) == 4 for p in (f, g) for m in p)
coeffs = [det.get((i,), 0) for i in range(19)]
assert coeffs[0] == 4 and coeffs[-1] == 3


def trim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p


def remainder(p, q):
    p = trim(p)
    while len(p) >= len(q):
        c = p[-1] / q[-1]
        shift = len(p) - len(q)
        for i, a in enumerate(q):
            p[i + shift] -= c * a
        p = trim(p)
    return p


def gcd(p, q):
    while q:
        p, q = q, remainder(p, q)
        if q:
            q = [a / q[-1] for a in q]
    return [a / p[-1] for a in p]


derivative = [Fraction(i * coeffs[i]) for i in range(1, 19)]
divisor_gcd = gcd([Fraction(c) for c in coeffs], derivative)
assert divisor_gcd == [Fraction(1)]

result = {
    "scope": "Actual QQ quartics, generic first-normal independence, squarefree boundary only.",
    "checks": {
        "homogeneous_quartics": True,
        "actual_global_vanishing_on_C": True,
        "independent_determinant_formula": True,
        "degree_18": True,
        "squarefree_over_QQ": True,
        "neither_endpoint_is_an_attachment": True,
    },
    "determinant_coefficients_in_ascending_u_degree": coeffs,
    "gcd_with_derivative": [1],
    "generic_component_multiplicity_from_nonzero_determinant": 1,
    "number_of_simple_geometric_attachment_points": 18,
    "projective_residual_geometry": "Certified separately by the Macaulay2 companion.",
}
destination = Path(__file__).with_name("ci_smooth_residual_boundary_2026_10_25.json")
destination.write_text(json.dumps(result, indent=2) + "\n")
print("Actual homogeneous source and independent boundary formula: PASS")
print("Boundary degree 18, squarefree, both distinguished endpoints avoided: PASS")
print("Wrote", destination.name)
