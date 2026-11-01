#!/usr/bin/env python3
"""Exact certificates for the fixed-frame order-three parity slice.

Run with SymPy 1.14.0 (the existing quartic-geometry requirements).
Reuses the accepted ambient operator and complete 23-dimensional sextic
source. Does not execute their artifact-writing footers or generate files.
The proof and coverage statements live in order_three_roots_and_sextic_lifts.md.
"""
import ast
import json
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
z, u, v, B, C = s.symbols("z u v B C")


def load_prefix(filename, stop_name):
    """Use the same AST-prefix convention as the structured-incidence exporter."""
    path = HERE / filename
    tree = ast.parse(path.read_text())
    stop = next(i for i, node in enumerate(tree.body)
                if isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == stop_name
                        for t in node.targets))
    env = {"__file__": str(path), "__name__": "certificate_input"}
    exec(compile(ast.Module(body=tree.body[:stop], type_ignores=[]),
                 str(path), "exec"), env)
    return env


def zero(expr):
    assert s.expand(expr) == 0, s.factor(expr)


def coefficients(forms, degree):
    return s.Matrix([s.expand(p).coeff(z, j)
                     for p in forms for j in range(degree + 1)])


def multiplier_map(forms, degree, target_degree):
    return s.Matrix.hstack(*(coefficients([z**k*p for p in forms], target_degree)
                             for k in range(degree + 1)))


def correction_map(forms):
    columns = []
    for lin in range(2):
        shifted = ([0] + forms) if lin else (forms + [0])
        columns.extend(coefficients([z**k*p for p in shifted], 9)
                       for k in range(8))
    return s.Matrix.hstack(*columns)


def main():
    first = load_prefix("generalization_quadratic_root_curve_universal_incidence.py", "EXAMPLE")
    full = load_prefix("generalization_quadratic_root_global_second_model.py", "stem")
    forms = [C*z**2-B**2, (B-C)*z, B-z**2]
    a, b, c = forms
    q = s.Matrix([1, z, B, C*z])
    r = s.Matrix([-z**3, B**2-2*B*z**2,
                  B*(C-B)*z-C*z**3, B**3+C*(C-3*B)*z**2])
    T = s.Matrix([[a, b, c, 0], [0, a, b, c]])
    assert (T*q).applyfunc(s.expand) == s.zeros(2, 1)
    assert (T*r).applyfunc(s.expand) == s.zeros(2, 1)
    # Six Plucker coordinates prove q,r are a basis of the dual bundle
    # after the appropriate twists, not just two generic syzygies.
    plucker = [c**2, -b*c, b**2-a*c, a*c, -a*b, a**2]
    for value, (i, j) in zip(plucker, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]):
        zero(q[i]*r[j]-q[j]*r[i]-value)
    fvalues = list(coefficients(forms, 2))
    point = dict(zip(first["VARIABLES"], fvalues))
    evaluate = lambda entry: s.sympify(first["evaluate"](entry, point))
    d = s.Matrix([evaluate(entry) for entry in first["D_VECTOR"]])
    A = s.Matrix([[evaluate(entry) for entry in row] for row in first["A"]])
    duals = [q, z*q, z**2*q, r]
    dual_matrix = s.Matrix([[s.expand(p[iv]).coeff(z, -k-1)
                            for k, iu, iv in first["ROWS"]] for p in duals])
    assert (dual_matrix*A).applyfunc(s.expand) == s.zeros(4, 12)
    P1 = (B-2)*(3*B**2+11*B+C+12)
    E2 = 9*B**4+3*B**3*C-12*B**2*C-60*B**2-16*B*C-72*B+4*C**2+72*C
    R = -9*B**4+9*B**3*C-30*B**3-8*B**2*C+2*B*C**2-24*B*C+72*B+24*C
    expected = s.Matrix([0, P1/4, 0, R/8])
    assert (dual_matrix*d-expected).applyfunc(s.expand) == s.zeros(4, 1)
    zero(R-E2+2*(3*B-C)*P1)
    delta = s.expand(b*b-4*a*c)
    zero(delta-(4*C*z**4+(C**2-6*B*C-3*B**2)*z**2+4*B**3))
    zero((C**2-6*B*C-3*B**2)**2-64*B**3*C-(C-B)**3*(C-9*B))
    P = 3*B**4-22*B**3-92*B**2-88*B+48
    Cbranch = -3*B**2-11*B-12
    zero(E2.subs(B, 2)-4*(C-6)*(C+10))
    zero(E2.subs(C, Cbranch)+3*(B+2)*P)
    assert s.gcd(P, s.diff(P, B)) == 1
    assert s.gcd(P, B*Cbranch*(Cbranch-B)*(Cbranch-9*B)) == 1
    print("PASS: dual basis, first compatibility, and exactly six smooth slice points")

    data = json.loads((HERE / "conditional_2_12_symbol_map_2026_10_20.json").read_text())
    M = s.Matrix(data["symbol_matrix_33_by_23"])
    cubic = s.Matrix(data["cubic_layer_matrix_40_by_23"])
    ann = s.Matrix(data["annihilator_11_by_33"])
    assert M.shape == (33, 23) and cubic.shape == (40, 23)
    assert ann.shape == (11, 33) and ann*M == s.zeros(11, 23)
    symbol = ann*multiplier_map(forms, 8, 10)
    rows = [0, 1, 2, 3, 4, 5, 6, 8, 10]
    minor = s.factor(symbol.subs(C, Cbranch).extract(rows, range(9)).det())
    expected_minor = (32*B**3*(B-2)*(B+2)*(3*B**2+11*B+12)
                      *(49*B**4+348*B**3+1012*B**2+1392*B+784)**2)
    zero(minor-expected_minor)
    assert s.gcd(P, minor) == 1
    print("PASS: all four quartic-parameter points fail the actual sextic symbol map")

    cases = [
        (6, [16, 0, 0, 0, -12, 0, 0, 0, 9],
         [s.Rational(-1, 2), 0, s.Rational(-11, 4), 0, s.Rational(3, 8), 0,
          0, s.Rational(-1, 4), 0, s.Rational(-37, 8), 0, s.Rational(3, 16)],
         [-s.Rational(9, 4), -s.Rational(9, 8)*z, -s.Rational(27, 8), s.Rational(3, 16)*z],
         {4: 108, 8: -36, 10: 24, 16: -108, 20: 108, 33: 81,
          37: -36, 39: -24, 41: -16, 44: -108, 55: 108}, -2916),
        (-10, [16, 0, 64, 0, 276, 0, -80, 0, 25],
         [s.Rational(-9, 2), 0, s.Rational(-11, 4), 0, s.Rational(-5, 8), 0,
          0, s.Rational(-1, 4), 0, s.Rational(-37, 8), 0, s.Rational(-45, 16)],
         [-s.Rational(25, 4), -s.Rational(225, 8)*z, s.Rational(325, 8), -s.Rational(45, 16)*z],
         {2: 625, 6: -125, 8: -50, 10: -20, 14: -625, 18: 125,
          20: 150, 35: 125, 37: -50, 39: 20, 41: -8, 53: 625}, -86250),
    ]
    for cvalue, alphas, h, gforms, sparse, obstruction in cases:
        substitution = {B: 2, C: cvalue}
        evaluated_forms = [p.subs(substitution) for p in forms]
        avals = s.Matrix(alphas)
        numeric_symbol = symbol.subs(substitution)
        assert numeric_symbol*avals == s.zeros(11, 1)
        assert numeric_symbol.rank() == 8
        assert A.subs(substitution)*s.Matrix(h) == d.subs(substitution)
        values = list(coefficients(evaluated_forms, 2)) + h
        assert all(full["ceval"](p, values) == 0 for p in full["FIRST"])
        actual_g = [sum(full["ceval"](p, values)*z**j
                        for (ui, vi, j), p in full["G0"].items() if vi == i)
                    for i in range(4)]
        assert all(s.expand(x-y) == 0 for x, y in zip(actual_g, gforms))
        L = M.row_join(s.zeros(33, 16)).col_join(
            cubic.row_join(-correction_map(evaluated_forms)))
        target = (multiplier_map(evaluated_forms, 8, 10)*avals).col_join(
            multiplier_map(gforms, 8, 9)*avals)
        witness = s.zeros(1, 73)
        for j, value in sparse.items():
            witness[j] = value
        assert witness*L == s.zeros(1, 39)
        assert (witness*target)[0] == obstruction != 0
        print(f"PASS: B=2, C={cvalue}: unique symbol multiplier; all cubic lifts fail ({obstruction})")


if __name__ == "__main__":
    main()
