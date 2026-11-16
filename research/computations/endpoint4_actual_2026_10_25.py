#!/usr/bin/env python3
"""Actual endpoint-four sextics, using an accepted symbol map as a premise.

This solves four new right-hand sides in the saved QQ-linear symbol matrix;
it does not recompute the inherited source dimension, matrix rank, or kernel.
An independent ambient-polynomial substitution checks the resulting formulas.
Only Python's standard library is needed. No claim about a global mate follows.
"""

from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "conditional_2_12_symbol_map_2026_10_20.json"
OUT = ROOT / "endpoint4_actual_2026_10_25.json"
M2OUT = ROOT / "endpoint4_actual_2026_10_25.m2"


def add(*polys):
    result = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, Q(0)) + coefficient
    return {e: c for e, c in result.items() if c}


def scale(poly, coefficient):
    return {e: c * coefficient for e, c in poly.items() if c * coefficient}


def mul(poly, other):
    result = {}
    for e, c in poly.items():
        for f, d in other.items():
            exponent = tuple(a + b for a, b in zip(e, f))
            result[exponent] = result.get(exponent, Q(0)) + c * d
    return {e: c for e, c in result.items() if c}


def power(poly, n):
    result = {(0,) * len(next(iter(poly))): Q(1)}
    for _ in range(n):
        result = mul(result, poly)
    return result


def substitute(poly, images):
    result = {}
    for exponent, coefficient in poly.items():
        term = {(0,) * len(next(iter(images[0]))): coefficient}
        for image, n in zip(images, exponent):
            term = mul(term, power(image, n))
        result = add(result, term)
    return result


def encode(poly):
    return [{"exponents": list(e), "coefficient": str(c)}
            for e, c in sorted(poly.items())]


def solve_saved_image(matrix, targets):
    rows = [[Q(x) for x in row] + list(target)
            for row, target in zip(matrix, targets)]
    columns = len(matrix[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(i for i in range(pivot_row, len(rows))
                     if rows[i][column])
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        value = rows[pivot_row][column]
        rows[pivot_row] = [x / value for x in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row and rows[i][column]:
                value = rows[i][column]
                rows[i] = [x - value * y
                           for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
    assert all(not any(row[columns:]) for row in rows[columns:])
    return [row[columns:] for row in rows[:columns]]


def main():
    saved = json.loads(SOURCE.read_text())
    # Right-hand-side order is a0, b1, b2, constant. Rows are P0..P10,
    # Q0..Q10, R0..R10 in the accepted balanced (u,v) frame.
    targets = [[Q(0)] * 4 for _ in range(33)]
    targets[8][0] = Q(1)
    targets[32][0] = Q(-1, 4)
    targets[20][1] = Q(1)
    targets[32][1] = Q(1, 2)
    targets[9][2] = Q(2)
    targets[21][2] = Q(1)
    targets[10][3] = Q(1)
    solution = solve_saved_image(saved["image_matrix_33_by_22"], targets)
    coefficients = {
        parameter: {label: str(solution[i][j])
                    for i, label in enumerate(saved["image_basis_labels"])
                    if solution[i][j]}
        for j, parameter in enumerate(("a0", "b1", "b2", "constant"))
    }

    # Independently construct actual ambient polynomials and substitute.
    xs = [{tuple(int(i == j) for i in range(4)): Q(1)} for j in range(4)]
    x0, x1, x2, x3 = xs
    quadric = add(mul(x0, x3), scale(mul(x1, x2), -1))
    cubic = add(power(x2, 3), scale(mul(x1, power(x3, 2)), -1))
    qqx3 = mul(power(quadric, 2), power(x3, 2))
    qdx2 = mul(mul(quadric, cubic), x2)
    qdx3 = mul(mul(quadric, cubic), x3)
    blocks = {
        "a0": add(scale(qqx3, -1), scale(qdx2, -1)),
        "b1": add(scale(qqx3, 2), qdx2),
        "b2": scale(qdx3, -1),
        "constant": scale(power(cubic, 2), Q(1, 4)),
        "kappa": power(quadric, 3),
    }
    chart = [
        {(0, 0, 0): Q(1)}, {(1, 0, 0): Q(1)},
        {(3, 0, 0): Q(1), (0, 0, 1): Q(1)},
        {(4, 0, 0): Q(1), (0, 1, 0): Q(1), (1, 0, 1): Q(3, 2)},
    ]
    jets = {key: substitute(poly, chart) for key, poly in blocks.items()}
    expected = {
        "a0": {(8, 2, 0): Q(1), (10, 0, 2): Q(-1, 4)},
        "b1": {(9, 1, 1): Q(1), (10, 0, 2): Q(1, 2)},
        "b2": {(9, 2, 0): Q(2), (10, 1, 1): Q(1)},
        "constant": {(10, 2, 0): Q(1)},
        "kappa": {},
    }
    for parameter, expansion in jets.items():
        assert all(e[1] + e[2] >= 2 for e in expansion)
        actual = {e: c for e, c in expansion.items() if e[1] + e[2] == 2}
        assert actual == expected[parameter], (parameter, actual)
        assert all(sum(e) == 6 for e in blocks[parameter])
        # Along L0=(x2,x3), q has order one and D has order two.
        line_order = min(e[2] + e[3] for e in blocks[parameter])
        assert line_order == (3 if parameter == "kappa" else 4)
        torus_weights = {e[1] + 3 * e[2] + 4 * e[3]
                         for e in blocks[parameter]}
        assert torus_weights == {dict(a0=16, b1=16, b2=17,
                                     constant=18, kappa=12)[parameter]}

    # All non-kappa blocks have L0-order four. The kappa block has order
    # three, so it cannot cancel with them when kappa is nonzero.
    report = {
        "status": "actual endpoint-four sextic realization; no mate claim",
        "accepted_input": str(SOURCE.relative_to(ROOT.parent.parent)),
        "accepted_input_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "premises_not_rerun": ["source dimension 23", "symbol rank 22", "kernel k*q^3"],
        "coefficient_ring": "QQ[a0,b1,b2,kappa]; cyclotomic specialization afterward",
        "ambient_generators": {
            "q": "x0*x3-x1*x2", "D": "x2^3-x1*x3^2"
        },
        "frame": "(x0,x1,x2,x3)=(1,z,z^3+v,z^4+u+(3/2)*z*v)",
        "target_root": {
            "a": "a0+2*b2*z+z^2", "b": "b1*z+b2*z^2",
            "c": "(b1/2-a0/4)*z^2", "alpha": "z^8",
        },
        "actual_formula": "(2*b1-a0)*q^2*x3^2+(b1-a0)*q*D*x2-b2*q*D*x3+D^2/4+kappa*q^3",
        "cyclotomic_specialization": "b1=a0*(rho+1)/2; rho^12=1, rho!=1; a0!=0",
        "actual_torus": {
            "ambient": "T_lambda=diag(1,lambda,lambda^3,lambda^4)",
            "equation": "lambda^-18 F(T_lambda*x)",
            "parameter_action": "a0,b1 -> lambda^-2(a0,b1); b2 -> lambda^-1*b2; kappa -> lambda^-6*kappa",
            "normalization": "lambda^2=a0 gives a0=1 on a finite etale square-root cover",
            "residual_action": "mu2 changes sign of b2 and fixes b1,kappa",
        },
        "image_basis_coefficients": coefficients,
        "ambient_exponent_order": ["x0", "x1", "x2", "x3"],
        "ambient_parameter_blocks": {key: encode(poly) for key, poly in blocks.items()},
        "chart_exponent_order": ["z", "u", "v"],
        "full_chart_parameter_blocks": {key: encode(poly) for key, poly in jets.items()},
        "checks": ["four exact target right-hand sides solved",
                   "actual ambient substitution has target second symbol",
                   "zeroth and first normal symbols vanish",
                   "all ambient blocks homogeneous of degree six",
                   "L0-order is three for kappa block and four for all other blocks",
                   "actual torus weights agree with the stated square-root normalization"],
        "limitations": ["a0 remains free in the universal formula; a0=1 requires the recorded torus cover",
                        "root open and nodal torsion condition retained, not solved",
                        "no higher compatible ambient root lift or G16 is asserted"],
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    M2OUT.write_text("""-- Generated by endpoint4_actual_2026_10_25.py.
-- Universal QQ parameter family; no nodal/Picard/saturation opens imposed.
EndpointCoefficients=QQ[a0,b1,b2,kappa];
EndpointAmbient=EndpointCoefficients[x0,x1,x2,x3];
endpointQuadric=x0*x3-x1*x2;
endpointCubicD=x2^3-x1*x3^2;
endpointFactual=((2*b1-a0)*endpointQuadric^2*x3^2
  +(b1-a0)*endpointQuadric*endpointCubicD*x2
  -b2*endpointQuadric*endpointCubicD*x3
  +(1/4)*endpointCubicD^2+kappa*endpointQuadric^3);
-- To specialize, use b1=a0*(rho+1)/2 over an exact cyclotomic field.
EndpointNormal=EndpointCoefficients[z,u,v];
endpointNormalMap=map(EndpointNormal,EndpointAmbient,
  {1,z,z^3+v,z^4+u+(3/2)*z*v});
endpointExpectedSymbol=(z^8*((a0+2*b2*z+z^2)*u^2
  +(b1*z+b2*z^2)*u*v+(b1/2-a0/4)*z^2*v^2));
assert((endpointNormalMap(endpointFactual)-endpointExpectedSymbol)
  %((ideal(u,v))^3)==0);
print("ENDPOINT4_M2_EXPORT_SECOND_SYMBOL: PASS");
use EndpointAmbient;
""")
    print("ENDPOINT4_ACTUAL_LINEAR_REALIZATION: PASS")
    print("ENDPOINT4_DIRECT_AMBIENT_SECOND_SYMBOL: PASS")
    print("ENDPOINT4_SINGULAR_LINE_ORDER: PASS")
    print(f"WROTE {OUT.relative_to(ROOT.parent.parent)}")
    print(f"WROTE {M2OUT.relative_to(ROOT.parent.parent)}")


if __name__ == "__main__":
    main()
