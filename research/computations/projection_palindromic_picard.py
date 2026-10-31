"""Exact replay and first construction gate for the fixed palindromic target.

Requires SymPy 1.14.0. This independently rebuilds the relevant fixed-target
identities from the balanced target in projection_and_elliptic_gluing.md.
It does not replay that file's preliminary variable-parameter exploration.
The Picard gate is interpreted geometrically in the accompanying proof note.
No numerical roots, other candidates, residue tests, or mate searches occur.

Run: python projection_palindromic_picard.py [--output PATH]
"""

import argparse
import json
import platform
from pathlib import Path

import sympy as sp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    t, a, eta = sp.symbols("t A eta")
    eta_value = 2 * sp.sqrt(5) * sp.I / 5
    field = sp.QQ.algebraic_field(eta_value)
    checks = []

    def poly(expression, variable):
        return sp.Poly(expression, variable, domain=field)

    def require(label, condition):
        if not condition:
            raise AssertionError(label)
        checks.append(label)

    def coprime(first, second):
        return first.gcd(second).degree() == 0

    def display_scalar(value):
        coefficients = sp.to_number_field(value, eta_value).coeffs()
        return str(sp.Poly.from_list(coefficients, eta).as_expr())

    def display_polynomial(value):
        variable = value.gen
        return str(sum(
            sp.sympify(display_scalar(value.nth(i))) * variable**i
            for i in range(value.degree() + 1)
        ))

    r = poly(t**4 + eta_value*t**3 + eta_value*t + 1, t)
    p = r**5
    coefficients = [poly(sum(p.nth(3*i+j)*a**i for i in range(7)), a)
                    for j in range(3)]
    e0, e1, e2 = coefficients
    square_factor = poly((eta_value*a+1)*(a+eta_value)
                         * (a**2-7*eta_value*a+1), a)
    elliptic_quartic = poly(5*a**4 + sp.Rational(28, 5)*eta_value*a**3
                           + sp.Rational(102, 25)*a**2
                           + sp.Rational(28, 5)*eta_value*a + 5, a)
    discriminant = e1**2 - 4*e0*e2

    require("four distinct nonendpoint marks", coprime(r, r.diff())
            and r.nth(0) != 0 and r.degree() == 4)
    require("primitive target equation of full bidegree (6,2)",
            e0.gcd(e1).gcd(e2).degree() == 0
            and e0.degree() == e2.degree() == 6)
    require("discriminant = -3 S^2 D", (discriminant
            + 3*square_factor**2*elliptic_quartic).is_zero)
    require("smooth elliptic normalization from separable quartic D",
            elliptic_quartic.degree() == 4
            and coprime(elliptic_quartic, elliptic_quartic.diff()))

    def at_cube(value):
        return poly(value.as_expr().subs(a, t**3), t)

    require("restriction to the target quartic equals R(t)^5",
            (at_cube(e0) + poly(t, t)*at_cube(e1)
             + poly(t**2, t)*at_cube(e2) - p).is_zero)
    require("exactly four smooth normalized inverse points",
            coprime(r, at_cube(discriminant)))

    q0 = poly(10*a**4 + (eta_value**3+30*eta_value)*a**3
              + 33*eta_value**2*a**2
              + (10*eta_value**3+3*eta_value)*a + 1, a)
    qinf = poly(a**4 + (10*eta_value**3+3*eta_value)*a**3
                + 33*eta_value**2*a**2
                + (eta_value**3+30*eta_value)*a + 10, a)
    require("B-boundary factorizations",
            (e0-poly((eta_value*a+1)**2, a)*q0).is_zero
            and (e2-poly((a+eta_value)**2, a)*qinf).is_zero)
    require("ordinary B-boundary points are simple",
            coprime(q0, q0.diff()) and coprime(qinf, qinf.diff())
            and coprime(q0, e1) and coprime(qinf, e1))
    zero_node, pole_node = 5*eta_value/4, -eta_value
    extra = poly(a**2-7*eta_value*a+1, a)
    require("two branches at each doubled B-boundary root are simple",
            q0.eval(zero_node) != 0 and qinf.eval(pole_node) != 0
            and e2.eval(zero_node) != 0 and e0.eval(pole_node) != 0
            and elliptic_quartic.eval(zero_node) != 0
            and elliptic_quartic.eval(pole_node) != 0
            and extra.eval(zero_node) != 0 and extra.eval(pole_node) != 0
            and zero_node != pole_node)
    require("A-boundary is simple and disjoint from B-boundary",
            elliptic_quartic.nth(0) != 0
            and e0.nth(0) != 0 and e2.nth(0) != 0
            and e0.LC() != 0 and e2.LC() != 0)

    # Riemann--Hurwitz on the smooth elliptic normalization then identifies
    # the whole passport: degrees 20, fibers (3^6,1^2), (5^4), (3^6,1^2).
    # The above assertions plus the proof note establish this, not a count.

    marked_numerator = (2*poly(t, t)*at_cube(e2) + at_cube(e1)).rem(r)
    marked_denominator = at_cube(square_factor).rem(r)
    require("marked normalization denominator is invertible",
            coprime(marked_denominator, r))
    marked_y = (marked_numerator * marked_denominator.invert(r)).rem(r)
    expected_y = poly(sp.Rational(27, 5)*t**2*(1-t**2), t).rem(r)
    require("marked Y coordinate has the stated exact modular formula",
            (marked_y-expected_y).is_zero)
    require("marked points lie on the elliptic normalization",
            (marked_y**2+3*at_cube(elliptic_quartic)).rem(r).is_zero)

    basis_values = [poly(1, t), poly(t**3, t), poly(t**6, t).rem(r), marked_y]
    evaluation = sp.Matrix([[value.nth(i) for value in basis_values]
                            for i in range(4)])
    determinant = sp.simplify(evaluation.det())
    require("Picard evaluation determinant equals 486 eta / 25",
            sp.simplify(determinant-sp.Rational(486, 25)*eta_value) == 0)
    require("Picard evaluation determinant is nonzero", determinant != 0)

    report = {
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "field": "Q(eta), eta^2=-4/5; either conjugate gives the same verdict",
        "target_replay": "PASS for the fixed target and normalized boundary/support facts",
        "component_picard_gate": "FAIL: H^0(E,L^2(-Z))=0",
        "marked_y_mod_R": display_polynomial(marked_y),
        "basis": ["1", "A", "A^2", "Y"],
        "quotient_basis": ["1", "t", "t^2", "t^3"],
        "evaluation_matrix": [[display_scalar(value) for value in row]
                              for row in evaluation.tolist()],
        "determinant": display_scalar(determinant),
        "later_gates": "NOT RUN: residue gluing, section extension, contact, mate descent",
        "exact_checks_passed": checks,
    }
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
