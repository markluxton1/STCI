#!/usr/bin/env python3
"""Exact identity checks for the fixed characteristic-zero cubic Gauss package.

Run from the repository root:
  python3 research/computations/verify_cubic_scroll_gauss_dual_2026_10_24.py
Requires SymPy 1.14.0 in the selected Python environment.
An optional first argument selects a JSON destination. The global geometry is
proved in the companion note; this verifier checks only its new identities.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import sympy as sp


checks: dict[str, bool] = {}


def zero(name: str, expression: sp.Expr) -> None:
    checks[name] = sp.expand(expression) == 0
    assert checks[name], name


def same_ideal(name: str, generators, expected, variables) -> None:
    actual_basis = sp.groebner(generators, *variables).polys
    expected_basis = sp.groebner(expected, *variables).polys
    checks[name] = actual_basis == expected_basis
    assert checks[name], name


def intersection(generators_1, generators_2, variables):
    auxiliary = sp.Dummy("intersection")
    basis = sp.groebner(
        [auxiliary * g for g in generators_1]
        + [(1 - auxiliary) * g for g in generators_2],
        auxiliary,
        *variables,
    )
    return [
        item.as_expr()
        for item in basis.polys
        if not item.as_expr().has(auxiliary)
    ]


x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")
a, b, c, d = sp.symbols("a b c d")
A, B, v0, v1 = sp.symbols("A B v0 v1")
r, w, u = sp.symbols("r w u")
p, q, h, j = sp.symbols("p q h j")

F = x0 * x2**2 - x1**2 * x3
K = a * c**2 + b**2 * d
Q = a * d - b * c
primal = [A * v0**2, B * v0, B * v1, A * v1**2]
gauss = [B * v1**2, -2 * A * v0 * v1**2,
         2 * A * v0**2 * v1, -B * v0**2]
primal_substitution = dict(zip((x0, x1, x2, x3), primal))
dual_substitution = dict(zip((a, b, c, d), gauss))

for index, variable in enumerate((x0, x1, x2, x3)):
    zero(f"gradient_pullback_{index}",
         sp.diff(F, variable).subs(primal_substitution) - B * gauss[index])
zero("dual_cubic_on_gauss", K.subs(dual_substitution))
for index, variable in enumerate((a, b, c, d)):
    zero(f"bidual_gradient_{index}",
         sp.diff(K, variable).subs(dual_substitution)
         - 4 * A * v0**2 * v1**2 * primal[index])

chart_zero = [r * w**2, -2 * w**2, 2 * w, -r]
chart_infinity = [r, -2 * w, 2 * w**2, -r * w**2]
same_ideal("reduced_base_ideal_zero", chart_zero, [r, w], (r, w))
same_ideal("reduced_base_ideal_infinity", chart_infinity, [r, w], (r, w))

seg = {a: p * h, b: p * j, c: q * h, d: q * j}
zero("quadric_segre_factor",
     K.subs(seg) - p * q * (q * h**3 + p * j**3))
dual_normalization = {
    a: A * v1**2, b: -B * v1, c: B * v0, d: -A * v0**2,
}
zero("dual_normalization_quadric_pullback",
     Q.subs(dual_normalization)
     - v0 * v1 * (B**2 - A**2 * v0 * v1))
param_K = {a: -u**4, b: u**3, c: -u, d: 1}
zero("quartic_K_in_dual_cubic", K.subs(param_K))
zero("quartic_K_in_dual_quadric", Q.subs(param_K))

osc = {a: -u**4, b: 2 * u**3, c: -2 * u, d: 1}
zero("osculating_quartic_in_dual_cubic", K.subs(osc))
zero("quadric_tangent_trace_distinct",
     K.subs({a: u**4, b: -u**3, c: -u, d: 1}) - 2 * u**6)

z = sp.symbols("z")
plane_from_pencil = A * w**2 - B * w * z + B * z**3 - A * z**4
zero("residual_factorization_for_ruling",
     plane_from_pencil - (z**2 - w) * (-A * z**2 + B * z - A * w))

contact_R = {x0: 1, x1: 2 * u, x2: 2 * u**3, x3: u**4}
contact_Q = {x0: 1, x1: u, x2: -u**3, x3: -u**4}
zero("different_point_R_contact_on_R", F.subs(contact_R))
zero("different_point_Q_contact_on_Q",
     (x0 * x3 - x1 * x2).subs(contact_Q))
for index, variable in enumerate((x0, x1, x2, x3)):
    zero(f"R_contact_plane_{index}",
         sp.diff(F, variable).subs(contact_R)
         + 4 * u**2 * list(param_K.values())[index])
quadric_gradient = [x3, -x2, -x1, x0]
for index, expression in enumerate(quadric_gradient):
    zero(f"Q_contact_plane_{index}",
         expression.subs(contact_Q) - list(param_K.values())[index])

jacobian = [c**2, b * d, a * c, b**2]
saturated = [b**2, b * c, c**2, a * c, b * d]
variables = (a, b, c, d)
for variable in variables:
    zero(f"bc_in_saturation_{variable}",
         sp.groebner(jacobian, *variables).reduce(variable * b * c)[1])
decomposition = intersection(
    intersection([b, c], [c, d, b**2], variables),
    [a, b, c**2],
    variables,
)
same_ideal("singular_scheme_primary_decomposition",
           decomposition, saturated, variables)

output = {
    "date": "2026-10-24",
    "scope": "Fixed R=x0*x2^2-x1^2*x3, characteristic zero; exact new identities",
    "status": "identity evidence, not a substitute for global proofs",
    "checks": checks,
    "passed": len(checks),
    "failed": 0,
}
destination = (
    Path(sys.argv[1]) if len(sys.argv) > 1
    else Path(__file__).with_name("cubic_scroll_gauss_dual_2026_10_24.json")
)
destination.write_text(json.dumps(output, indent=2) + "\n")
print(f"PASS: {len(checks)} exact checks; output {destination}")
