#!/usr/bin/env python3
"""Exact identities for the October 24 P4/ruled-surfaces research proposal.

Run with a Python having SymPy installed, for example
  /tmp/stci-z4-env/bin/python research/computations/verify_p4_ruled_surfaces_2026_10_24.py

This checks coordinate identities and finite ideal computations. Normality,
finiteness, completeness of singular loci, and independent mathematical
review are supplied by the accompanying notes, not certified by this file.
It does not replay inherited STCI proofs or promote a canonical result.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


CHECKS: list[dict] = []


def record(name: str, condition: bool, **evidence) -> None:
    assert condition, name
    CHECKS.append({"name": name, "pass": True, **evidence})


def equal_ideals(left, right, variables, **options) -> bool:
    gl = sp.groebner(left, *variables, **options)
    gr = sp.groebner(right, *variables, **options)
    return all(gr.reduce(p.as_expr())[1] == 0 for p in gl.polys) and all(
        gl.reduce(p.as_expr())[1] == 0 for p in gr.polys
    )


def intersection(n: int, left: tuple[int, int], right: tuple[int, int]) -> int:
    """On F_n with E^2=-n, E.f=1, f^2=0."""
    a, b = left
    c, d = right
    return -n * a * c + a * d + b * c


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "p4_ruled_surfaces_2026_10_24.json"))
    args = parser.parse_args()

    s, t, a, b = sp.symbols("s t a b")
    x0, x1, x2, x3, x4 = sp.symbols("x0 x1 x2 x3 x4")
    scroll = [x0*x4-x2**2, x0*x3-x1*x2, x2*x3-x1*x4]
    bundle = {x0: a*s**2, x1: b*s, x2: a*s*t, x3: b*t, x4: a*t**2}
    quartic = {x0: s**4, x1: s**3*t, x2: s**2*t**2,
               x3: s*t**3, x4: t**4}
    record("S(1,2) parametrization satisfies its three minors",
           all(sp.expand(p.subs(bundle)) == 0 for p in scroll))
    record("the complete rational normal quartic lies on that same scroll",
           all(sp.expand(p.subs(quartic)) == 0 for p in scroll))
    elim = sp.groebner(scroll, x2, x0, x1, x3, x4, order="lex")
    eliminated = [p.as_expr() for p in elim.polys if not p.as_expr().has(x2)]
    cubic = x0*x3**2-x1**2*x4
    record("dropping the middle quartic coordinate eliminates to R",
           equal_ideals(eliminated, [cubic], [x0, x1, x3, x4]),
           eliminated_generators=[str(p) for p in eliminated])

    c, d = sp.symbols("c d")
    segre_restriction = (x0*x3**2-x1**2*x4).subs(
        {x0: a*c, x1: a*d, x3: b*c, x4: b*d})
    record("cubic restriction to Q factors as curve plus two ruling fibers",
           sp.expand(segre_restriction-a*b*(b*c**3-a*d**3)) == 0,
           identity="R|Q=a*b*(b*c^3-a*d^3)",
           divisor="C+L0+Linfty")

    r, w = sp.symbols("r w")
    delta = w-r**2
    pulled = [r*w-r**3, w**2-r**4]
    desired = [delta*r, delta*w]
    record("scheme inverse of C on normalization of R has endpoint defect",
           equal_ideals(pulled, desired, [w, r]),
           source_ideal=["x2-x1^3", "x3-x1^4"],
           substitution={"x1": "r", "x2": "r*w", "x3": "w^2"},
           pullback="(w-r^2)*(r,w)",
           divisorial_hull="(w-r^2)", defect_length=1)
    u = sp.symbols("u")
    missing = s**2*t**2
    retained = [s**4, s**3*t, s*t**3, t**4]
    products = [retained[1]**2, retained[0]*retained[2],
                retained[1]*retained[3], retained[2]**2]
    record("missing middle cone generator multiplies into the image ring",
           all(sp.expand(missing*x-y) == 0 for x, y in zip(retained, products)),
           identities=["h*x0=x1^2", "h*x1=x0*x2", "h*x2=x1*x3", "h*x3=x2^2"])
    record("middle cone generator integral relation",
           sp.expand(missing**2-retained[0]*retained[3]) == 0,
           identity="h^2=x0*x3")
    exponents = {0, 1, 3, 4}
    sums2 = {i+j for i in exponents for j in exponents}
    record("projection-cone degree-two semigroup base case",
           sums2 == set(range(9)), degree_one_missing=[2],
           degree_two_exponents=sorted(sums2),
           induction="If degree n contains [0,4n], multiplying by exponents 0 and4 covers [0,4n+4] for n>=1.")
    semigroup34 = {3*i+4*j for i in range(15) for j in range(15)}
    record("cuspidal plane quartic chart semigroup conductor base cases",
           [i for i in range(6) if i not in semigroup34] == [1, 2, 5]
           and all(i in semigroup34 for i in [6, 7, 8]),
           gaps=[1, 2, 5], conductor=6,
           induction="6,7,8 are present; add3 to obtain every integer>=6.",
           local_ring="k[v^3,v^4,q] inside k[v,q]")
    record("quartic-cone further projection integral relation",
           sp.expand((s*t**3)**4-s**4*(t**4)**3) == 0,
           identity="(st^3)^4=s^4*(t^4)^3")

    # On F4 a graph difference is a degree-four section. Orders are read
    # directly in the two parameter charts, with p0=[1:0], pinfty=[0:1].
    q_middle = s**2*t**2
    q_sheet = s*t**3
    record("C4 and its chosen zero graph intersect 2p0+2pinfty",
           sp.degree(q_middle.subs(s, 1), t) == 2
           and sp.degree(q_middle.subs(t, 1), s) == 2,
           divisor={"p0": 2, "pinfty": 2})
    record("distinct four-sheet graphs intersect 3p0+pinfty on F4",
           sp.degree(q_sheet.subs(s, 1), t) == 3
           and sp.degree(q_sheet.subs(t, 1), s) == 1,
           divisor={"p0": 3, "pinfty": 1})

    alpha, beta, y, z = sp.symbols("alpha beta y z")
    coeff = sp.QQ.frac_field(alpha, beta)
    near0 = [y-alpha*u**3, z-u**4, y-beta*u**3]
    gb0 = sp.groebner(near0, y, z, u, domain=coeff)
    record("distinct component images intersect with length3 at p0",
           equal_ideals(near0, [y, z, u**3], [y, z, u], domain=coeff),
           coefficient_condition="alpha-beta invertible; characteristic zero distinct fourth roots",
           groebner_basis=[str(p.as_expr()) for p in gb0.polys], length=3)
    # In x3=1 and coordinate z=x2, C_alpha has x0=z^4,
    # x1=alpha*z^3 because alpha^4=1.
    nearinf = [x0-z**4, x1-alpha*z**3, x1-beta*z**3]
    gbi = sp.groebner(nearinf, x0, x1, z, domain=coeff)
    record("distinct component images intersect with length3 at pinfty",
           equal_ideals(nearinf, [x0, x1, z**3], [x0, x1, z], domain=coeff),
           root_condition="alpha^4=beta^4=1 and alpha!=beta",
           groebner_basis=[str(p.as_expr()) for p in gbi.polys], length=3)

    table = []
    # Q uses ruling over the degree-one parameter; C=E+3f.
    for label, n, hyperplane, curve in [
        ("Q", 0, (1, 1), (1, 3)),
        ("projection cone smooth model", 4, (1, 4), (1, 4)),
        ("R normalization", 1, (1, 2), (2, 2)),
        ("F smooth model", 4, (1, 4), (1, 4)),
    ]:
        row = {"model": label, "n": n, "H": list(hyperplane), "C": list(curve),
               "H_square": intersection(n, hyperplane, hyperplane),
               "C_square": intersection(n, curve, curve),
               "degree_C": intersection(n, hyperplane, curve),
               "ruling_degree_on_C": curve[0]}
        table.append(row)
    record("intersection table gives degree4 for all distinguished quartics",
           [row["degree_C"] for row in table] == [4, 4, 4, 4]
           and [row["C_square"] for row in table] == [6, 4, 4, 4]
           and [row["H_square"] for row in table] == [2, 4, 3, 4], table=table)
    record("cubic ruling degree-two base change splits into F2 sections",
           intersection(2, (1, 2), (1, 2)) == 2,
           model="F2", sections="E2+2f", self_intersection=2,
           intersection_divisor="p0+pinfty")

    lam, q = sp.symbols("lambda q")
    bitangent = lam**2+4*lam+1
    cube_linear = sp.rem(lam**3-(15*lam+4), bitangent, lam)
    image_relation = sp.rem(lam**6+52*lam**3+1, bitangent, lam)
    record("cube identifies the rank-two bitangent multiplier family near2",
           cube_linear == 0 and image_relation == 0,
           identities=["lambda^3=15*lambda+4", "(lambda^3)^2+52*lambda^3+1=0"],
           inverse="lambda=(q-4)/15; 15 is invertible in Z_(2)",
           special_fiber="(q-1)^2=0")
    orbit_special = sp.Poly((q-u**3)**4-(q**4-u**12), q, u, modulus=2)
    record("four-sheet special fiber is fourth-power graph on affine ruled chart",
           orbit_special.is_zero,
           total_equation="q^4-u^12", special_equation="(q-u^3)^4")
    bitangent_special = sp.Poly(bitangent-(lam-1)**2, lam, modulus=2)
    record("bitangent multiplier family specializes to mu2 inside mu4",
           bitangent_special.is_zero,
           special_equation="(lambda-1)^2",
           inclusion="(lambda-1)^4 lies in ((lambda-1)^2)")

    report = {
        "status": "PASS",
        "scope": "new coordinate identities and finite ideal checks; provisional research evidence only",
        "sympy_version": sp.__version__,
        "check_count": len(CHECKS),
        "checks": CHECKS,
        "limitations": [
            "The script is not a proof of normalization, finiteness, global smoothness, or novelty.",
            "Endpoint multiplicities for distinct components assume the difference of roots is invertible; they do not assert mixed-characteristic transversality.",
            "No inherited STCI proof is rerun and no STCI claim is made.",
        ],
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"PASS: {len(CHECKS)} exact checks; SymPy {sp.__version__}")
    print(args.output)


if __name__ == "__main__":
    main()
