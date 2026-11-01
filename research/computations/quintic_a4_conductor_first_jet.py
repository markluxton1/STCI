"""Uniform conductor jets at the marked A4 point.

Uses the reviewed universal conductor determinant. The output is an exact
first-jet identity on J=0, delta!=0 and a quadratic contact coefficient
on J=0, 2*B+G+delta**2=0. It does not assert projection admissibility,
conductor smoothness, or mate descent. Run with Python 3 and SymPy.
"""

import json
import sympy as sp

from quintic_conductor_cone_identity import conductor_quadric


def first_jet():
    coordinates, quadric = conductor_quadric()
    parameters = {str(p): p for p in quadric.as_expr().free_symbols
                  if p not in coordinates}
    delta, a, b, g, j = [parameters[name]
                         for name in ("delta", "a", "B", "G", "J")]
    x, y, z = sp.symbols("a_local b_local c_local")

    # Exact source chart Z0=1. Its remaining equation is
    # b_local*(c_local-a_local**2)+a_local*c_local**2=0.
    z4 = x*y-z*z
    z5 = y*y-x*y*z+z**3
    symbol = y+z
    target = [
        1-x+a*symbol,
        1-x+delta*x+(a+b)*symbol,
        1-x+3*delta*x+3*delta**2*z-delta**3*z4+(a+3*b+g)*symbol,
        1-x+4*delta*x+6*delta**2*z-4*delta**3*z4+delta**4*z5
        +(a+4*b+2*g)*symbol,
    ]
    q = quadric.as_expr().subs(j, 0)
    image_point = dict.fromkeys(coordinates, 1)
    origin = dict.fromkeys((x, y, z), 0)
    constant = sp.factor(q.subs(image_point))
    gradient = [sp.diff(q, coord).subs(image_point) for coord in coordinates]
    actual = [sp.factor(sum(gradient[i]*sp.diff(target[i], variable).subs(origin)
                            for i in range(4))) for variable in (x, y, z)]

    ell = 2*b+g+delta**2
    r = delta*(g+3*delta**2)**2-2*g**2
    denominator = 81*delta**9
    expected = [2*g*(g+3*delta**2)**2*ell/denominator,
                -g*ell*r/denominator,
                -(g+3*delta**2)*ell*(r+6*b*delta*(g+3*delta**2))/denominator]
    if constant != 0 or any(sp.cancel(u-v) != 0 for u, v in zip(actual, expected)):
        raise RuntimeError("The stated uniform first-jet identity failed")

    # On ell=0, admissibility requires the following parameter factor to
    # be nonzero, because it divides every actual quadric coefficient.
    restricted = sp.Poly(q.subs(b, -(g+delta**2)/2).expand(), *coordinates)
    kappa = -g**2+4*g*a-2*g*delta**2-2*g*delta-delta**4
    for _, coefficient in restricted.terms():
        sp.Poly(sp.cancel(648*delta**10*coefficient/kappa), delta, a, g,
                domain=sp.QQ)
    # The source line b_local=c_local=0 is tangent to marked c, whose
    # exact equations are b_local=-x**2/(1-x), c_local=x**2/(1-x).
    # The full first jet is zero here, so both curves have the same
    # coefficient of x**2 in the restricted conductor.
    line_target = {coordinates[i]: target[i].subs({y: 0, z: 0}) for i in range(4)}
    along_line = sp.Poly(restricted.as_expr().subs(line_target, simultaneous=True), x)
    second_coefficient = sp.factor(along_line.coeff_monomial(x**2))
    expected_second = -(g+3*delta**2)**2*kappa/(81*delta**8)
    if sp.cancel(second_coefficient-expected_second) != 0:
        raise RuntimeError("The stated A4 contact coefficient failed")
    return {"sympy_version": sp.__version__,
            "parameter_domain": "J=0, delta!=0",
            "constant": str(constant),
            "linear_coefficients_a_local_b_local_c_local": [str(u) for u in actual],
            "common_factor": str(ell),
            "restricted_family": "J=0, B=-(G+delta**2)/2",
            "factor_of_every_restricted_quadric_coefficient": str(kappa),
            "coefficient_factor_clearing_scalar": "648*delta**10",
            "quadratic_coefficient_on_marked_curve": str(second_coefficient),
            "scope": "actual conductor jets; admissibility and local consequences are separate"}


if __name__ == "__main__":
    print(json.dumps(first_jet(), indent=2))
