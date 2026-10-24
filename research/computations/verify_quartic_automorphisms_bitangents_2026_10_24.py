#!/usr/bin/env python3
"""Exact identity checks for the fixed rational quartic geometry package.

Requires SymPy 1.14.0 (the existing /tmp/stci-z4-env/bin/python runtime works).
Run from any directory; --output optionally chooses the JSON report path.

This checks polynomial and linear-algebra identities used in the accompanying
research notes. It is not a proof of classification, of a group-scheme claim,
or of any STCI assertion. No normal-bundle or carrier exclusion is rerun.
"""

from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path

import sympy as S


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name(
            "quartic_automorphisms_bitangents_2026_10_24.json"
        ),
    )
    args = parser.parse_args()
    checks: list[dict[str, object]] = []

    def check(name: str, condition: object, evidence: object = None) -> None:
        if not bool(condition):
            raise AssertionError(name)
        item: dict[str, object] = {"name": name, "status": "PASS"}
        if evidence is not None:
            item["evidence"] = evidence
        checks.append(item)

    def zero(expr: object) -> bool:
        if isinstance(expr, S.MatrixBase):
            return all(S.cancel(e) == 0 for e in expr)
        return S.cancel(expr) == 0

    s, t, u, v, w, a, b, c, d = S.symbols("s t u v w a b c d")
    alpha, beta, gamma, lam, z = S.symbols("alpha beta gamma lambda z")
    x = S.symbols("x0:4")
    center = S.Matrix([0, 0, 1, 0, 0])
    complete = S.Matrix([1, u, u**2, u**3, u**4])
    curve = S.Matrix([1, u, u**3, u**4])

    # Coordinates in W^vee are evaluation coordinates, without binomial factors.
    cat = S.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    check("center_catalecticant_rank_three", cat.det() == -1 and cat.rank() == 3,
          {"determinant": "-1", "rank": 3})
    eval_cat = S.Matrix([[1, u, u**2], [u, u**2, u**3],
                         [u**2, u**3, u**4]])
    check("evaluation_catalecticant_rank_one", eval_cat.rank() == 1)
    check("sum_of_two_evaluations_catalecticant_rank_at_most_two",
          zero((eval_cat + eval_cat.subs(u, v)).det()))
    apolar_center = sum((-1)**i * S.binomial(4, i) * center[i]
                        * s**i * t**(4-i) for i in range(5))
    check("apolar_center_double_double", apolar_center == 6*s**2*t**2,
          "6*s^2*t^2, using the determinant-twisted SL2 self-duality")
    osculating_matrix = S.Matrix.hstack(
        complete, complete.diff(u), complete.diff(u, 2), complete.diff(u, 3)
    )
    check("center_in_osculating_hyperplane_only_at_finite_zero",
          S.factor(S.Matrix.hstack(osculating_matrix, center).det()) == 72*u**2,
          "det[c,c',c'',c''',e2]=72*u^2; reverse chart gives infinity")
    endpoint_plane = S.Matrix.hstack(complete, complete.diff(u), complete.diff(u,2)).subs(u,0)
    reverse = S.Matrix(list(reversed(complete)))
    reverse_plane = S.Matrix.hstack(reverse,reverse.diff(u),reverse.diff(u,2)).subs(u,0)
    check("endpoint_osculating_planes_meet_at_center",
          endpoint_plane.rank()==3 and reverse_plane.rank()==3
          and S.Matrix.hstack(endpoint_plane,reverse_plane).rank()==5
          and S.Matrix.hstack(endpoint_plane,center).rank()==3
          and S.Matrix.hstack(reverse_plane,center).rank()==3,
          "two 3-dimensional vector spans in a 5-dimensional sum, each containing e2")
    wronskian = S.Matrix([[S.diff(f, u, i) for f in curve]
                         for i in range(4)]).det()
    check("hyperplane_system_wronskian", S.expand(wronskian) == 72*u**2,
          "72*u^2 on finite chart, order two at infinity in the reversed chart")
    cubic_divisor = a*s**3+b*s*s*t+c*s*t*t+d*t**3
    check("center_incident_degree_three_divisor_pencil",
          S.Poly(S.expand(s*cubic_divisor),s,t).coeff_monomial(s*s*t*t)==c
          and S.Poly(S.expand(t*cubic_divisor),s,t).coeff_monomial(s*s*t*t)==b,
          "the two sections s*g,t*g vanish under the center iff g=a*s^3+d*t^3")
    r, zeta = S.symbols("r zeta")
    weighted_vector = sum(((r*zeta**i)*complete.subs(u,r*zeta**i)
                           for i in range(3)), S.zeros(5,1))
    check("center_rank_three_ruling_decomposition",
          all(S.rem(S.expand(e),zeta*zeta+zeta+1,zeta)==0
              for e in weighted_vector-3*r**3*center),
          "sum_{i=0}^2 u_i*c4(u_i)=3*kappa*e2, with u_i=r*zeta^i and kappa=r^3")

    basis = [s**4, s**3*t, s*t**3, t**4]
    transformed = [S.expand(f.subs({s: a*s+b*t, t: c*s+d*t}, simultaneous=True))
                   for f in basis]
    omitted = [S.Poly(f, s, t).coeff_monomial(s**2*t**2) for f in transformed]
    expected = [6*a*a*b*b, 3*a*b*(a*d+b*c), 3*c*d*(a*d+b*c), 6*c*c*d*d]
    check("stabilizer_omitted_middle_coefficients",
          all(zero(f-g) for f, g in zip(omitted, expected)),
          [str(S.factor(e)) for e in expected])
    check("diagonal_and_antidiagonal_preserve_system",
          all(zero(f.subs({b: 0, c: 0})) for f in omitted)
          and all(zero(f.subs({a: 0, d: 0})) for f in omitted))
    determinant, middle = a*d-b*c, a*d+b*c
    check("stabilizer_ideal_localization_identity",
          zero(a*b*determinant**2-middle*(a*b*middle)+4*c*d*(a*a*b*b))
          and zero(c*d*determinant**2-middle*(c*d*middle)+4*a*b*(c*c*d*d)),
          "after inverting det and 6, omitted coefficients generate the ideal (ab,cd)")

    Da = S.diag(1, a, a**3, a**4)
    J = S.zeros(4)
    for i in range(4):
        J[i, 3-i] = 1
    sigma = S.diag(1, -1, -1, 1)
    full_sigma = S.diag(1, -1, 1, -1, 1)
    check("ambient_torus_and_reversal_action",
          zero(Da*curve - curve.subs(u, a*u))
          and zero(J*curve - u**4*curve.subs(u, 1/u)))
    check("normalizer_relation", zero(J*Da*J - a**4*Da.subs(a, 1/a)))
    check("involution_is_central_projectively",
          zero(sigma*Da-Da*sigma) and zero(sigma*J-J*sigma)
          and zero(full_sigma*center-center))
    q = x[0]*x[3]-x[1]*x[2]
    check("quadric_relative_invariance",
          zero(q.subs(dict(zip(x, Da*S.Matrix(x))), simultaneous=True)-a**4*q)
          and zero(q.subs(dict(zip(x, J*S.Matrix(x))), simultaneous=True)-q))
    monomials = [x[i]*x[j] for i in range(4) for j in range(i, 4)]
    restrictions = [S.expand(f.subs(dict(zip(x, curve)), simultaneous=True))
                    for f in monomials]
    restriction_matrix = S.Matrix(
        [[f.coeff(u, i) for f in restrictions] for i in range(9)]
    )
    check("unique_quadric_restriction_kernel", restriction_matrix.rank() == 9
          and len(restriction_matrix.nullspace()) == 1
          and zero(q.subs(dict(zip(x,curve)),simultaneous=True)),
          {"rank": 9, "kernel_dimension": 1})

    H = S.Matrix([-u**4, 2*u**3, -2*u, 1])
    check("osculating_section_factorization",
          zero((H.T*curve.subs(u, z))[0]-(z-u)**3*(z+u)))
    check("dual_osculating_involution_action", zero(sigma*H-H.subs(u, -u)))
    check("dual_torus_osculating_equivariance",
          zero(Da.inv().T*H-a**-4*H.subs(u, a*u)))

    # The secant map is globally cubic on Sym^2, including diagonal divisors.
    plucker = S.Matrix([
        gamma**3,
        gamma*(beta**2-alpha*gamma),
        -beta*(beta**2-2*alpha*gamma),
        -alpha*beta*gamma,
        alpha*(beta**2-alpha*gamma),
        alpha**3,
    ])
    wedge = S.Matrix([
        S.cancel((curve[i]*curve[j].subs(u, v)
                  -curve[j]*curve[i].subs(u, v))/(v-u))
        for i in range(4) for j in range(i+1, 4)
    ])
    check("secant_plucker_divided_difference",
          zero(wedge-plucker.subs({alpha: u*v, beta: -(u+v), gamma: 1})),
          [str(e) for e in plucker])
    p01, p02, p03, p12, p13, p23 = plucker
    check("secant_plucker_relation", zero(p01*p23-p02*p13+p03*p12))
    check("secant_map_has_no_basepoints",
          S.groebner(list(plucker.subs(beta, 1)), alpha, gamma).contains(S.Integer(1)),
          "alpha=gamma=0 forced by p23=p01=0; beta=1 chart has unit ideal")
    check("diagonal_divisors_map_to_tangent_lines",
          zero(plucker.subs({alpha: u*u, beta: -2*u, gamma: 1})-wedge.subs(v, u)))
    check("endpoint_tangent_lines",
          plucker.subs({alpha: 0, beta: 0, gamma: 1}) == S.Matrix([1,0,0,0,0,0])
          and plucker.subs({alpha: 1, beta: 0, gamma: 0}) == S.Matrix([0,0,0,0,0,1]))
    trisecant_restriction = plucker.subs({alpha: z*z, beta: z, gamma: 1})
    check("trisecant_pair_conic_cubic_ruling_map",
          trisecant_restriction == S.Matrix([1,0,z**3,-z**3,0,z**6]),
          "beta^2=alpha*gamma parametrized by [z^2:z:1] maps to ruling kappa=z^3")
    chart_map = plucker.subs(gamma, 1)[1:, 0]
    jac = chart_map.jacobian([alpha, beta])
    minors = [jac.extract([i,j], [0,1]).det()
              for i in range(5) for j in range(i+1, 5)]
    ramification_ideal = S.groebner(minors, alpha, beta)
    check("secant_differential_rank_drop_scheme",
          [p.as_expr() for p in ramification_ideal.polys] == [alpha, beta**2],
          "gamma=1 chart: ideal (alpha,beta^2), supported at tangent trisecant 2p0")
    endpoint_fiber = S.groebner(list(chart_map),alpha,beta)
    check("secant_endpoint_fiber_length_three",
          [p.as_expr() for p in endpoint_fiber.polys] == [alpha-beta**2,beta**3],
          "gamma=1 fiber over T0 has ideal (alpha-beta^2,beta^3); length three")

    h = alpha*s*s+beta*s*t+gamma*t*t
    h_square = S.expand(h*h)
    Dform = beta**2-4*alpha*gamma
    Bform = beta**2+2*alpha*gamma
    Dmat = S.Matrix([[0,0,-2], [0,1,0], [-2,0,0]])
    Bmat = S.Matrix([[0,0,1], [0,1,0], [1,0,0]])
    check("bitangent_doubling_coefficient",
          S.Poly(h_square,s,t).coeff_monomial(s*s*t*t) == Bform)
    check("diagonal_and_bitangent_conics_smooth", Dmat.det() == -4 and Bmat.det() == -1)
    intersection = S.groebner([Dform.subs(gamma,1), Bform.subs(gamma,1)],alpha,beta)
    check("conic_intersection_length_two_each_endpoint",
          [p.as_expr() for p in intersection.polys] == [alpha,beta**2],
          "gamma=1 local ideal (alpha,beta^2); swapping alpha,gamma gives other length two")
    B_lambda = S.Matrix([[0,0,lam/2], [0,1,0], [lam/2,0,0]])
    check("conic_pair_generalized_eigenspectrum",
          Dmat.inv()*B_lambda == S.diag(-lam/4,1,-lam/4),
          "generalized eigenvalues: simple 1, repeated -lambda/4")
    zc = S.symbols("z0:5")
    Qz = S.Matrix([[zc[0],zc[1],zc[2]], [zc[1],zc[2],zc[3]],
                    [zc[2],zc[3],zc[4]]])
    check("multiplication_dual_conics_are_apolar_to_diagonal",
          zero(S.trace(Dmat.inv()*Qz)),
          "trace(D^-1 Q_z)=0 for every quartic-coefficient functional z")
    check("torus_invariant_apolar_conic_unique_in_pencil",
          S.solve(S.trace(Dmat.inv()*B_lambda),lam) == [2],
          "trace=1-lambda/2, hence lambda=2")

    R = u*u+4*u*v+v*v
    check("affine_bitangent_relation_from_conic",
          zero(Bform.subs({alpha:u*v,beta:-(u+v),gamma:1})-R))
    rho = -2+S.sqrt(3)
    check("rho_equation_and_reciprocal_sum",
          zero(rho*rho+4*rho+1) and zero(rho+1/rho+4),
          {"minimal_polynomial": "T^2+4*T+1", "reciprocal_sum": "-4"})
    check("rho_square_reciprocal_sum", zero(rho**2+rho**-2-14))
    check("rho_real_embedding_excludes_root_of_unity", -1 < rho < 0,
          "rho=-2+sqrt(3) is real and strictly between -1 and 0")
    contact_ratio_polynomial = v*v+(2+lam)*u*v+u*u
    check("general_conic_contact_ratio",
          zero((beta**2+lam*alpha*gamma).subs(
              {alpha:u*v,beta:-(u+v),gamma:1})-contact_ratio_polynomial),
          "rho+rho^-1=-(2+lambda); lambda=2 gives -4")
    check("ordered_bitangent_graphs",
          zero(R.subs(v,rho*u)) and zero(R.subs(v,u/rho)))
    check("bitangent_graphs_meet_transversely_at_endpoint",
          not zero(rho-1/rho), "distinct slopes rho,rho^-1 at zero; reverse chart likewise")
    check("bitangent_diagonal_intersection_double_endpoints",
          R.subs(v,u) == 6*u*u,
          "finite chart ideal (v-u,u^2), and reverse chart gives infinity")
    check("bitangent_osculating_graph_intersection_double_endpoints",
          R.subs(v,-u) == -2*u*u)
    composite_ideal = S.groebner([R,w*w+4*v*w+v*v],v,w,u)
    eliminated = [p.as_expr() for p in composite_ideal.polys
                  if not p.as_expr().has(v)]
    reduced_composite = (w-u)*(w*w-14*u*w+u*u)
    check("scheme_composition_elimination_has_simple_diagonal",
          len(eliminated)==1 and zero(eliminated[0]-reduced_composite),
          "elimination ideal ((w-u)*(w^2-14*u*w+u^2)); reverse chart covers infinity")
    check("composition_resultant_counts_diagonal_twice",
          zero(S.resultant(R,w*w+4*v*w+v*v,v)
               -(w-u)**2*(w*w-14*u*w+u*u)),
          "resultant and correspondence cycle have diagonal multiplicity two; scheme image does not")
    check("osculating_unordered_pairs_form_line",
          (-(u+v)).subs(v,-u) == 0 and (u*v).subs(v,-u) == -u*u
          and zero(plucker.subs({alpha:-u*u,beta:0,gamma:1})
                   - S.Matrix([1,u*u,0,0,-u**4,-u**6])))

    # Only literal reductions are asserted here; no self-duality in char 2.
    def mod2(expr: object, *gens: S.Symbol) -> S.Expr:
        return S.Poly(S.expand(expr),*gens,modulus=2).as_expr()

    check("characteristic_two_bitangent_and_discriminant_reductions",
          mod2(Bform,alpha,beta,gamma) == beta**2
          and mod2(Dform,alpha,beta,gamma) == beta**2,
          "both equations reduce to beta^2; their reduced support is a line")
    check("characteristic_two_stabilizer_reduction",
          mod2(omitted[1],a,b,c,d) == mod2(a*b*(a*d+b*c),a,b,c,d)
          and mod2(omitted[2],a,b,c,d) == mod2(c*d*(a*d+b*c),a,b,c,d))
    check("characteristic_two_osculating_section_fourth_power",
          mod2((H.T*curve.subs(u,z))[0]-(z-u)**4,u,z) == 0,
          "H_u=[u^4:0:0:1], ordinary -1 involution becomes identity")

    report = {
        "status": "PASS",
        "date": "2026-10-24",
        "scope": "Exact polynomial and linear-algebra checks for the fixed rational quartic in characteristic zero, with three explicitly labelled characteristic-two reductions.",
        "limitations": [
            "The notes supply the geometric classification and completeness proofs.",
            "A passing identity verifier does not certify mathematical novelty, canonical promotion, or an STCI exclusion.",
            "No inherited normal-bundle or carrier-exclusion computation is rerun.",
            "The rank-three catalecticant tests the supplied center; the proof that every secant has rank at most two is in the note.",
            "The stabilizer identities are checked; the full stabilizer identification requires the characteristic-zero argument in the note.",
            "The composition elimination computes the actual affine scheme image; inversion covers the remaining projective endpoint.",
        ],
        "python_version": platform.python_version(),
        "sympy_version": S.__version__,
        "check_count": len(checks),
        "checks": checks,
    }
    args.output.write_text(json.dumps(report,indent=2)+"\n")
    print(f"PASS: {len(checks)} exact checks; report {args.output}")


if __name__ == "__main__":
    main()
