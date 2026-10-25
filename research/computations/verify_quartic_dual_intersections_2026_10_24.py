#!/usr/bin/env python3
"""Exact identities for the fixed-quartic dual intersections (char. zero).

Requires SymPy. Default output is the adjacent JSON evidence file; pass
--output to use another destination. This verifies explicit polynomial
and ideal identities only. Global reducedness, normalization, completeness,
and geometric interpretation are proved in the accompanying note.
No inherited STCI result is rerun or promoted.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "quartic_dual_intersections_2026_10_24.json"))
    args = parser.parse_args()
    checks = []

    def record(name, condition, **evidence):
        assert condition, name
        checks.append({"name": name, "pass": True, **evidence})

    def equal_ideals(left, right, variables):
        gl = sp.groebner(left, *variables, domain=sp.QQ)
        gr = sp.groebner(right, *variables, domain=sp.QQ)
        return all(gr.reduce(p.as_expr())[1] == 0 for p in gl.polys) and all(
            gl.reduce(p.as_expr())[1] == 0 for p in gr.polys)

    A, B, C, D, u = sp.symbols("A B C D u")
    M = A*D-B*C
    L = B*C-4*A*D
    K = A*C**2+B**2*D
    N = A*C**2-B**2*D
    f = A+B*u+C*u**3+D*u**4
    delta = sp.discriminant(f, u)
    I = 12*D*A-3*C*B
    J = -27*D*B**2-27*C**2*A
    record("binary_quartic_invariants", sp.expand(I+3*L) == 0 and
           sp.expand(J+27*K) == 0 and sp.expand(27*delta-4*I**3+J**2) == 0)
    record("cubic_dual_discriminant_identity", sp.expand(delta+4*L**3+27*K**2) == 0,
           identity="Delta=-4(BC-4AD)^3-27(AC^2+B^2D)^2")
    record("quadric_dual_discriminant_identity",
           sp.expand(delta-4*M*(8*A*D+B*C)**2+27*N**2) == 0,
           identity="Delta=4(AD-BC)(8AD+BC)^2-27(AC^2-B^2D)^2")
    record("full_cubic_intersection_ideal",
           equal_ideals([K, delta], [K, L**3], (A, B, C, D)))
    record("full_quadric_intersection_ideal",
           equal_ideals([M, delta], [M, N**2], (A, B, C, D)))

    a, b, c, d, z = sp.symbols("a b c d z")
    segre = {A:a*c, B:a*d, C:b*c, D:b*d}
    record("segre_hyperplane_factorization", sp.expand(
        f.subs(segre)-(a+b*u**3)*(c+d*u)) == 0)
    record("segre_discriminant_factorization", sp.expand(
        delta.subs(segre)+27*a**2*b**2*(a*d**3-b*c**3)**2) == 0,
        divisor="2ell_0+2ell_infinity+2Gamma_Q")
    record("segre_two_cubic_restrictions", sp.expand(
        N.subs(segre)-a*b*(b*c**3-a*d**3)) == 0 and sp.expand(
        K.subs(segre)-a*b*(b*c**3+a*d**3)) == 0)

    normalization = {A:z**2, B:-z*a, C:a, D:-1}
    record("dual_normalization_equation", sp.expand(K.subs(normalization)) == 0)
    record("residual_quadratic_factorization", sp.expand(f.subs(normalization)+
           (u**2-z)*(u**2-a*u+z)) == 0)
    record("dual_normalization_discriminant", sp.expand(delta.subs(normalization)-
           4*z**3*(a**2-4*z)**3) == 0,
           divisor="3O_tilde+3f_0+3f_infinity")
    record("dual_normalization_cartier_divisor", sp.expand(L.subs(normalization)-
           z*(4*z-a**2)) == 0)
    record("osculating_full_inverse_ideal_endpoint_correction", equal_ideals(
        [z**2-a**4/16, -z*a+a**3/4],
        [(z-a**2/4)*z, (z-a**2/4)*a], (z, a)),
        ideal="(z-a^2/4)(z,a)")

    local = sp.expand(K.subs({D:1, A:B*C/4}))
    record("endpoint_reduced_divisor", sp.expand(local-B*(B+C**3/4)) == 0)
    contact = sp.groebner([B, B+C**3/4], B, C, domain=sp.QQ)
    record("endpoint_branch_contact_length_three",
           [sp.expand(p.as_expr()) for p in contact.polys] == [B, C**3],
           quotient_basis=["1", "C", "C^2"])

    osc = {A:-u**4, B:2*u**3, C:-2*u, D:1}
    quadric_trace = {A:u**4, B:-u**3, C:-u, D:1}
    record("distinguished_curve_substitutions", all(sp.expand(x.subs(osc)) == 0
           for x in (K, L, delta)) and all(sp.expand(x.subs(quadric_trace)) == 0
           for x in (M, N, delta)))
    record("distinguished_traces_are_distinct", sp.factor(M.subs(osc)) == 3*u**4 and
           sp.factor(K.subs(quadric_trace)) == 2*u**6)

    result = {"scope": "fixed marked rational quartic, characteristic zero",
              "status": "exact symbolic evidence for provisional research",
              "sympy_version": sp.__version__, "checks": checks,
              "count": len(checks), "all_pass": True}
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"PASS: {len(checks)} exact checks; evidence: {args.output}")


if __name__ == "__main__":
    main()
