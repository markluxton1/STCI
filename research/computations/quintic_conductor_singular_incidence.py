"""Exact specialized Sing(Gamma) intersection C for the inherited A4 projection.

Usage: python3 research/computations/quintic_conductor_singular_incidence.py
       delta a B G J

Inputs are rational numbers and delta must be nonzero. Source: the inverse
linear substitution and five quadrics in the October 12 restricted-conductor
note, and its independent (2,3,3) ideal audit. This script computes that ideal
by row reduction, then restricts its equations and 2x2 Jacobian minors to
C=[s^4:s^3*t:s*t^3:t^4]. The homogeneous gcd on P1 retains t/s=infinity.
It does not certify conductor integrality or any STCI/section descent.

Only Python's standard library is used. Polynomials have six variables
(X0,X1,X2,X3,h,z); coefficient arithmetic is over Q throughout.
"""

from fractions import Fraction as Q
from itertools import combinations
import json
import sys


def add(*polys):
    out = {}
    for poly in polys:
        for exp, coeff in poly.items():
            out[exp] = out.get(exp, Q(0)) + coeff
    return {exp: coeff for exp, coeff in out.items() if coeff}


def scale(coeff, poly):
    return {exp: coeff * value for exp, value in poly.items() if coeff * value}


def mul(left, right):
    out = {}
    for exp, coeff in left.items():
        for other_exp, other_coeff in right.items():
            key = tuple(a + b for a, b in zip(exp, other_exp))
            out[key] = out.get(key, Q(0)) + coeff * other_coeff
    return {exp: coeff for exp, coeff in out.items() if coeff}


def variable(index):
    exp = [0] * 6
    exp[index] = 1
    return {tuple(exp): Q(1)}


def derivative(poly, index):
    out = {}
    for exp, coeff in poly.items():
        if exp[index]:
            key = list(exp)
            key[index] -= 1
            out[tuple(key)] = coeff * exp[index]
    return out


def omitted_coefficient(poly, h_degree, z_degree):
    return {exp[:4] + (0, 0): coeff for exp, coeff in poly.items()
            if exp[4:] == (h_degree, z_degree)}


def conductor_equations(params):
    delta, a, b, g, j = params
    if not delta:
        raise ValueError("The inherited nonendpoint coordinates require delta != 0")
    x0, x1, x2, x3, h, z = [variable(i) for i in range(6)]
    u3 = scale(1 / delta, add(x0, scale(-1, x1), scale(b, h)))
    u2 = scale(1 / (3 * delta**2),
               add(x2, scale(-3, x1), scale(2, x0), scale(-g, h), scale(delta**3, z)))
    u0 = scale(1 / delta**4,
               add(x3, scale(-2, x2), scale(2, x1), scale(-1, x0),
                   scale(-j, h), scale(2 * delta**3, z)))
    z0, z1, z2, z3, z4, z5 = (
        add(x0, scale(-a, h), scale(-1, u3)), scale(-1, u3),
        add(h, scale(-1, u2)), u2, z, u0)
    rows = [
        add(mul(z4, z4), scale(-1, mul(z3, z5))),
        add(mul(z2, z4), scale(-1, mul(z1, z5))),
        add(mul(z2, z3), scale(-1, mul(z1, z4))),
        add(mul(z2, z2), scale(-1, mul(z3, z4)), scale(-1, mul(z0, z5))),
        add(mul(z1, z2), scale(-1, mul(z3, z3)), scale(-1, mul(z0, z4))),
    ]
    center_monomials = [(0, 0, 0, 0, 2, 0), (0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 0, 2)]
    rank = 0
    for exp in center_monomials:
        pivot = next((i for i in range(rank, 5) if rows[i].get(exp)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        rows[rank] = scale(1 / rows[rank][exp], rows[rank])
        for i in range(5):
            if i != rank and rows[i].get(exp):
                rows[i] = add(rows[i], scale(-rows[i][exp], rows[rank]))
        rank += 1
    if rank != 3:
        return rank, None
    a1, a2 = [omitted_coefficient(row, 0, 0) for row in rows[3:]]
    b1, b2 = [omitted_coefficient(row, 1, 0) for row in rows[3:]]
    c1, c2 = [omitted_coefficient(row, 0, 1) for row in rows[3:]]
    quadric = add(mul(b1, c2), scale(-1, mul(b2, c1)))
    cubic_h = add(mul(c1, a2), scale(-1, mul(c2, a1)))
    cubic_z = add(mul(b2, a1), scale(-1, mul(b1, a2)))
    return rank, [quadric, cubic_h, cubic_z]


def curve_restriction(poly):
    """Return coefficients in t on the s=1 chart, with homogeneous degree."""
    degrees = {sum(exp) for exp in poly}
    if not degrees:
        return [], None
    if len(degrees) != 1 or any(exp[4] or exp[5] for exp in poly):
        raise ValueError("Expected a homogeneous polynomial in X0,...,X3")
    degree = 4 * degrees.pop()
    out = [Q(0)] * (degree + 1)
    for exp, coeff in poly.items():
        out[exp[1] + 3 * exp[2] + 4 * exp[3]] += coeff
    return trim(out), degree


def trim(poly):
    while poly and not poly[-1]:
        poly.pop()
    return poly


def remainder(left, right):
    left = list(left)
    while left and len(left) >= len(right):
        shift = len(left) - len(right)
        coeff = left[-1] / right[-1]
        for i, value in enumerate(right):
            left[i + shift] -= coeff * value
        trim(left)
    return left


def gcd(left, right):
    while right:
        left, right = right, remainder(left, right)
    return [value / left[-1] for value in left] if left else []


def projective_common_zeros(polys):
    common, infinity_order = [], None
    for poly in polys:
        affine, degree = curve_restriction(poly)
        if not affine:
            continue
        common = gcd(common, affine)
        vanishing = degree - (len(affine) - 1)
        infinity_order = vanishing if infinity_order is None else min(infinity_order, vanishing)
    if infinity_order is None:
        return {"whole_curve": True}
    return {"whole_curve": False, "degree": len(common) - 1 + infinity_order,
            "infinity_order": infinity_order,
            "affine_monic_coefficients_low_to_high": [str(value) for value in common]}


def incidence(params):
    rank, equations = conductor_equations(params)
    result = {"parameters_delta_a_B_G_J": [str(x) for x in params], "center_rank": rank}
    if equations is None:
        result["status"] = "No conductor claim: center rank is not three"
        return result
    jacobian = [[derivative(poly, i) for i in range(4)] for poly in equations]
    minors = [add(mul(jacobian[r][i], jacobian[s][j]),
                  scale(-1, mul(jacobian[r][j], jacobian[s][i])))
              for r, s in combinations(range(3), 2) for i, j in combinations(range(4), 2)]
    result["conductor_intersection_C"] = projective_common_zeros(equations)
    result["singular_conductor_intersection_C"] = projective_common_zeros(equations + minors)
    result["conductor_integrality"] = "not tested"
    result["mate_descent"] = "not tested"
    return result


if __name__ == "__main__":
    if len(sys.argv) != 6:
        raise SystemExit(__doc__)
    print(json.dumps(incidence(tuple(Q(x) for x in sys.argv[1:])), indent=2))
