#!/usr/bin/env python3
"""Exact symbolic controls for the four-A1 projected del Pezzo family.

The written proof supplies irreducibility, normality, finite birational
projection, and the full-fiber obstruction. The identities below bind that
proof to the actual C0 coordinates, uniformly on alpha*beta*gamma*delta*
(alpha*delta-beta*gamma) != 0. No sampled rank claim replaces that coverage.
"""

import hashlib
import json
from pathlib import Path

import sympy as sp


def assert_zero(expr):
    assert sp.expand(expr) == 0


def main():
    alpha, beta, gamma, delta = sp.symbols("alpha beta gamma delta")
    x0, x1, x2, x3, z = sp.symbols("x0 x1 x2 x3 z")
    U, V = sp.symbols("U V")
    u0, u1, v0, v1 = sp.symbols("u0 u1 v0 v1")
    Delta = alpha * delta - beta * gamma
    M = alpha * delta + beta * gamma
    transform = sp.Matrix([
        [0, gamma**2, 2 * gamma * delta, delta**2, 0],
        [-alpha * gamma, -M, -beta * delta, 0, 0],
        [0, -alpha * gamma, -M, -beta * delta, 0],
        [0, 0, -alpha * gamma, -M, -beta * delta],
        [0, alpha**2, 2 * alpha * beta, beta**2, 0],
    ])
    determinant = sp.factor(transform.det())
    assert_zero(determinant - alpha * beta * gamma * delta * Delta**3)
    a, b, c, d, e = transform * sp.Matrix([x0, x1, z, x2, x3])
    Q1 = sp.expand(a * e - c**2)
    Q2 = sp.expand(b * d - c**2)
    basic = x1 * x2 - z**2
    assert_zero(Q1 - Delta**2 * basic)
    L = (alpha**2 * gamma**2 * x0 - alpha * gamma * M * x1
         - beta * delta * M * x2 + beta**2 * delta**2 * x3)
    R = (alpha * gamma * M * x0 * x2 + alpha * beta * gamma * delta * x0 * x3
         - alpha**2 * gamma**2 * x1**2 - alpha * beta * gamma * delta * x1 * x2
         + beta * delta * M * x1 * x3 - beta**2 * delta**2 * x2**2)
    A2 = -(alpha**2 * delta**2 + alpha * beta * gamma * delta
           + beta**2 * gamma**2)
    assert_zero(Q2 + A2 * basic - L * z - R)
    # In particular the center (0,0,1,0,0) lies outside S uniformly.
    assert_zero(Q1.subs({x0: 0, x1: 0, x2: 0, x3: 0, z: 1}) + Delta**2)
    assert_zero(L.coeff(x0) - alpha**2 * gamma**2)
    F = sp.expand(R**2 - x1 * x2 * L**2)
    # A4-degree resultant and its exact normalization scalar.
    assert_zero(sp.resultant(Q1, Q2, z) - Delta**4 * F)
    assert sp.Poly(F, x0, x1, x2, x3).total_degree() == 4
    assert_zero(sp.Poly(F, x0).coeff_monomial(x0**2)
                - ((alpha * gamma * M * x2 + alpha * beta * gamma * delta * x3)**2
                   - alpha**4 * gamma**4 * x1 * x2))
    c0 = {x0: U**4, x1: U**3 * V, x2: U * V**3, x3: V**4, z: U**2 * V**2}
    assert_zero(Q1.subs(c0))
    assert_zero(Q2.subs(c0))
    assert_zero(F.subs(c0))
    Lc = sp.expand(L.subs(c0))
    assert_zero(Lc.subs(V, 0) - alpha**2 * gamma**2 * U**4)
    assert_zero(Lc.subs(U, 0) - beta**2 * delta**2 * V**4)
    assert_zero(R.subs(c0) + U**2 * V**2 * Lc)
    # The other normalization point over every Lc=0 point is exact:
    # Q1 vanishes on both signs, Q2 at the negative sign is -2*z*Lc.
    minus = dict(c0)
    minus[z] = -U**2 * V**2
    assert_zero(Q1.subs(minus))
    assert_zero(Q2.subs(minus) + 2 * U**2 * V**2 * Lc)
    # Exact involution-cover binding for the divisor 2c ~ 2H.
    aa, bb, cc, dd, ee = sp.symbols("a b c d e")
    cover = {aa: u0**2 * v0**2, bb: u0**2 * v1**2,
             cc: u0 * u1 * v0 * v1, dd: u1**2 * v0**2,
             ee: u1**2 * v1**2}
    odd = (alpha * u0**2 * v0 * v1 + beta * u0 * u1 * v0**2
           + gamma * u0 * u1 * v1**2 + delta * u1**2 * v0 * v1)
    Q = (alpha**2 * aa * bb + beta**2 * aa * dd
         + gamma**2 * bb * ee + delta**2 * dd * ee
         + 2 * cc * (alpha * beta * aa + alpha * gamma * bb
                     + beta * delta * dd + gamma * delta * ee)
         + 2 * (alpha * delta + beta * gamma) * cc**2)
    assert_zero(Q.subs(cover) - odd**2)
    assert_zero(Q.subs(dict(zip([aa, bb, cc, dd, ee], [a, b, c, d, e]))).subs(c0))
    sample = {alpha: 1, beta: 1, gamma: 1, delta: 2}
    assert_zero(L.subs(sample) - (x0 - 3 * x1 - 6 * x2 + 4 * x3))
    assert_zero(Lc.subs(sample)
                - (U**2 - 4 * U * V + 2 * V**2) * (U**2 + U * V + 2 * V**2))
    source = Path(__file__).resolve()
    root = source.parent.parent
    report = {
        "status": "PASS",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "scope": "Uniform exact identities; geometry and full-fiber proof are in the companion note.",
        "parameter_open": "alpha*beta*gamma*delta*(alpha*delta-beta*gamma) != 0",
        "transform_determinant": str(determinant),
        "projection_center_Q1": str(-Delta**2),
        "projection_linear_coefficient": str(L),
        "projection_constant_coefficient": str(R),
        "quartic_equation": "R^2 - x1*x2*L^2",
        "resultant_scalar": str(Delta**4),
        "C0_conductor_pullback": str(Lc),
        "endpoint_values_nonzero_on_parameter_open": True,
        "two_distinct_lifts_at_every_Lc_root": "z=+/-U^2*V^2, with U*V!=0",
        "other_point_Q2": "-2*U^2*V^2*Lc",
        "double_curve_section_cover_identity": "q^*Q=odd^2",
        "sample_conductor_pullback_factorization": str(sp.factor(Lc.subs(sample))),
        "global_unrestricted_STCI_claim": False,
    }
    target = root / "research/scratch/session-singular-delpezzo-four-A1-family-2026-10-09.json"
    target.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PASS: uniform four-A1 family coordinates, quartic elimination, and full-fiber identities")
    print(f"source sha256: {report['source_sha256']}")
    print(f"report: {target}")


if __name__ == "__main__":
    main()
