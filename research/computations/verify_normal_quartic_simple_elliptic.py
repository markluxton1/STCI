#!/usr/bin/env python3
"""Exact checks for the bounded simple-elliptic normal-quartic exclusion.

This checks formulas and inequalities, not the cited classification theorems
or the existence of an STCI. Source hypotheses and geometric deductions are
in research/notes/2026-10-05-normal-quartic-carriers.md.
"""

from fractions import Fraction as Q
import json

import sympy as sp


x, y, z, X, Y, Z = sp.symbols("x y z X Y Z")
a0, a1, a2, a3, a4, b, c, d0, nu, gamma, delta, alpha = sp.symbols(
    "a0 a1 a2 a3 a4 b c d0 nu gamma delta alpha"
)
forms = [
    ("E6_2", (1, 1, 1), 3, 2,
     x*x*y+a0*x*z*z+a1*y**3+a2*y*y*z+a3*y*z*z+a4*z**3),
    ("E7_2", (1, 1, 2), 4, 2,
     x*x*z+x**3*y+b*x*x*y*y+c*x*y**3+d0*y**4+z*z),
    ("E7_3", (1, 1, 2), 4, 3,
     x*y*(x-y)*(x-nu*y)+z*z),
    ("E8_3", (1, 2, 3), 6, 3,
     x**3*z+gamma*x*x*y*y+delta*x**4*y+y**3+z*z),
    ("E8_4", (1, 2, 3), 6, 4,
     alpha*x**4*y+x*x*y*y+y**3+z*z),
]


def nonzero_order(poly):
    p = sp.Poly(poly, x)
    return min(k[0] for k, coeff in p.terms() if coeff != 0)


local_checks = []
for name, weights, degree, expected_order, f in forms:
    assert f.subs({y: 0, z: 0}) == 0
    monomials = sp.Poly(f, x, y, z).monoms()
    assert all(sum(a*w for a, w in zip(m, weights)) == degree
               for m in monomials)
    fy = sp.diff(f, y).subs({y: 0, z: 0})
    fz = sp.diff(f, z).subs({y: 0, z: 0})
    order = min(nonzero_order(q) for q in (fy, fz) if q != 0)
    assert order == expected_order
    chart = sp.expand(f.subs({y: x**weights[1]*Y,
                             z: x**weights[2]*Z}) / x**degree)
    assert not chart.has(x)
    derivatives = [sp.diff(chart, u).subs({Y: 0, Z: 0}) for u in (Y, Z)]
    assert any(q != 0 for q in derivatives)
    elliptic_degree = Q(degree, weights[0]*weights[1]*weights[2])
    assert elliptic_degree in (1, 2, 3)
    local_checks.append({"pair": name, "weights": weights,
                         "first_normal_order": order,
                         "chart_derivatives": list(map(str, derivatives)),
                         "elliptic_degree": str(elliptic_degree)})

# Every ADE rank which can occur in the bounded argument is checked exactly.
# The proof in the note also gives the symbolic, unbounded inequalities.
ade_checks = 0
for n in range(1, 12):
    for k in range(1, (n+1)//2+1):
        value = Q(k*(n+1-k), n+1)
        assert value <= Q(n*k, n+k)
        assert value <= Q(n, 2)
        ade_checks += 1
    if n >= 4:
        assert Q(1) <= Q(2*n, n+2)
        assert Q(1) <= Q(n, 2)
        ade_checks += 1
    if n >= 5:
        s = n//2
        assert Q(n, 4) <= Q(n*s, n+s)
        assert Q(n, 4) <= Q(n, 2)
        ade_checks += 1
for n, s, value in [(6, 2, Q(4, 3)), (7, 3, Q(3, 2))]:
    assert value <= Q(n*s, n+s)
    assert value <= Q(n, 2)
    ade_checks += 1

gaps = []
for d, N, P in [(1, 9, 6), (2, 10, 7), (3, 11, 7)]:
    required = Q(5)-Q(1, d)
    upper = Q(N*P, N+P)
    gap = required-upper
    assert gap > 0
    gaps.append({"elliptic_degree": d, "ADE_rank_upper": N,
                 "ADE_order_upper": P, "required": str(required),
                 "upper": str(upper), "positive_gap": str(gap)})

print(json.dumps({"status": "PASS", "local_forms": local_checks,
                  "bounded_ADE_rows_checked": ade_checks,
                  "strict_gaps": gaps}, indent=2))
