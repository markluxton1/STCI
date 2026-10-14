#!/usr/bin/env python3
"""Independent literal coefficient binding, using only Python's standard library.

This does not run Macaulay2 or any accepted verifier.  It treats the captured
coefficient lists as polynomials, parses the compact source assignments, and
compares their expansions over Q by a small sparse-polynomial implementation.
"""
from __future__ import annotations

import ast
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
CAPTURE = ROOT / "research/validation/2026-10-13-evening-h3-proportional"
OUT = Path(__file__).resolve().parent
ZERO = (0, 0, 0)  # delta, lambda, q


def constant(c):
    c = Fraction(c)
    return {ZERO: c} if c else {}


def add(a, b):
    result = dict(a)
    for m, c in b.items():
        result[m] = result.get(m, Fraction(0)) + c
        if not result[m]:
            del result[m]
    return result


def scale(a, c):
    return {m: t * c for m, t in a.items() if t * c}


def multiply(a, b):
    result = {}
    for m, c in a.items():
        for n, d in b.items():
            p = tuple(x + y for x, y in zip(m, n))
            result[p] = result.get(p, Fraction(0)) + c * d
    return {m: c for m, c in result.items() if c}


def power(a, n):
    assert isinstance(n, int) and n >= 0
    result = constant(1)
    while n:
        if n & 1:
            result = multiply(result, a)
        a = multiply(a, a)
        n >>= 1
    return result


def parse_poly(text):
    text = re.sub(r"\blambda\b", "lam", " ".join(text.split())).replace("^", "**")
    tree = ast.parse(text, mode="eval")
    names = {"delta": 0, "dl": 0, "lam": 1, "q": 2}

    def visit(node):
        if isinstance(node, ast.Constant):
            assert type(node.value) is int, ast.dump(node)
            return constant(node.value)
        if isinstance(node, ast.Name):
            idx = names[node.id]
            m = [0, 0, 0]
            m[idx] = 1
            return {tuple(m): Fraction(1)}
        if isinstance(node, ast.UnaryOp):
            value = visit(node.operand)
            if isinstance(node.op, ast.USub):
                return scale(value, -1)
            assert isinstance(node.op, ast.UAdd)
            return value
        assert isinstance(node, ast.BinOp), ast.dump(node)
        left = visit(node.left)
        if isinstance(node.op, ast.Pow):
            assert isinstance(node.right, ast.Constant)
            assert type(node.right.value) is int
            return power(left, node.right.value)
        right = visit(node.right)
        if isinstance(node.op, ast.Add):
            return add(left, right)
        if isinstance(node.op, ast.Sub):
            return add(left, scale(right, -1))
        if isinstance(node.op, ast.Mult):
            return multiply(left, right)
        if isinstance(node.op, ast.Div):
            assert set(right) == {ZERO}
            return scale(left, 1 / right[ZERO])
        raise AssertionError(ast.dump(node))

    return visit(tree.body)


def parse_list(path, expected_length):
    data = path.read_text().strip()
    assert data.startswith("{") and data.endswith("}")
    parts = data[1:-1].split(",")
    assert len(parts) == expected_length
    return [parse_poly(p) for p in parts]


def assignment(source, name):
    match = re.search(r"\b" + re.escape(name) + r"\s*=\s*(.*?);", source, re.S)
    assert match, name
    return match.group(1)


def lam_one(poly):
    result = {}
    for (d, l, q), c in poly.items():
        m = (d, 0, q)
        result[m] = result.get(m, Fraction(0)) + c
    return {m: c for m, c in result.items() if c}


def from_coefficient_list(coefficients):
    result = {}
    for i, coefficient in enumerate(coefficients):
        assert all(m[2] == 0 for m in coefficient)
        result = add(result, {(d, l, i): c for (d, l, _), c in coefficient.items()})
    return result


def q_coefficient(poly, degree):
    return {(d, l, 0): c for (d, l, q), c in poly.items() if q == degree}


def display(poly):
    if not poly:
        return "0"
    terms = []
    for m in sorted(poly, reverse=True):
        c = poly[m]
        factors = []
        for name, exponent in zip(("delta", "lambda", "q"), m):
            if exponent:
                factors.append(name if exponent == 1 else f"{name}^{exponent}")
        monomial = "*".join(factors)
        if monomial and abs(c) == 1:
            unsigned = monomial
        else:
            unsigned = str(abs(c)) + ("*" + monomial if monomial else "")
        if not terms:
            terms.append(("-" if c < 0 else "") + unsigned)
        else:
            terms.append((" - " if c < 0 else " + ") + unsigned)
    return "".join(terms)


def evaluate_delta(poly, value):
    assert all(l == 0 and q == 0 for d, l, q in poly)
    return sum(c * value**d for (d, l, q), c in poly.items())


def exact_divide_delta(dividend, divisor):
    assert divisor
    assert all(l == 0 and q == 0 for d, l, q in dividend)
    assert all(l == 0 and q == 0 for d, l, q in divisor)
    quotient, remainder = {}, dict(dividend)
    leading = max(divisor)
    while remainder and max(remainder)[0] >= leading[0]:
        top = max(remainder)
        term = {(top[0] - leading[0], 0, 0): remainder[top] / divisor[leading]}
        quotient = add(quotient, term)
        remainder = add(remainder, scale(multiply(term, divisor), -1))
    assert not remainder, display(remainder)
    return quotient


paths = {
    "main_H": CAPTURE / "main-H-coefficients.txt",
    "main_S": CAPTURE / "main-S-coefficients.txt",
    "main_source": CAPTURE / "probe_main.m2",
    "lambda_source": CAPTURE / "probe_lambda1.m2",
    "compact_source": CAPTURE / "probe_lambda1_compact.m2",
    "compact_denominators": CAPTURE / "lambda1-compact-denominators.txt",
}
source = paths["compact_source"].read_text()
main_h = from_coefficient_list(parse_list(paths["main_H"], 4))
main_s = from_coefficient_list(parse_list(paths["main_S"], 6))
compact_h = parse_poly(assignment(source, "h3lcH"))
compact_q4 = parse_poly(assignment(source, "h3lcQ"))
h1, s1 = lam_one(main_h), lam_one(main_s)
assert h1 == compact_h, display(add(h1, scale(compact_h, -1)))
assert not q_coefficient(s1, 0)
s1_div_q = {(d, l, q - 1): c for (d, l, q), c in s1.items()}
ratio = exact_divide_delta(q_coefficient(s1_div_q, 4), q_coefficient(compact_q4, 4))
assert ratio
assert s1_div_q == multiply(compact_q4, ratio)

# Homogeneous infinity values: the leading coefficients at the stated degrees.
h_infinity = q_coefficient(h1, 3)
q4_infinity = q_coefficient(compact_q4, 4)
t = scale(q4_infinity, Fraction(1, 2))
assert h_infinity == parse_poly("dl+1")
assert t == parse_poly("45*dl^2-38*dl-29")
assert t == add(multiply(parse_poly("45*dl-83"), h_infinity), constant(54))
assert evaluate_delta(t, Fraction(-1)) == 54
assert q_coefficient(compact_q4, 0) == parse_poly("-400*dl")

# The displayed compact remainder denominators are captured artifacts; their
# exact dependence is bound here, without computing the accepted remainders.
denominators = parse_list(paths["compact_denominators"], 4)
t9 = power(t, 9)
denominator_scalars = []
for denominator in denominators:
    m = max(t9)
    scalar = denominator[m] / t9[m]
    assert denominator == scale(t9, scalar)
    denominator_scalars.append(str(scalar))

main_source = paths["main_source"].read_text()
lambda_source = paths["lambda_source"].read_text()
assert "h3eHC=-3*lambda^2/delta*h3eH;" in main_source
assert "h3eSC=432*lambda^4/delta^3*h3eS;" in main_source
assert "h3lMap=map(h3lField,h3lBase,{dl,1_h3lField});" in lambda_source

report = {
    "audit_kind": "independent standard-library sparse-polynomial arithmetic",
    "accepted_scripts_rerun": False,
    "input_sha256": {k: hashlib.sha256(p.read_bytes()).hexdigest() for k, p in paths.items()},
    "main_H_coefficient_count": 4,
    "main_S_coefficient_count": 6,
    "H_at_lambda_1_equals_compact_H": True,
    "H_at_lambda_1": display(h1),
    "S_at_lambda_1_divisible_by_q": True,
    "S_at_lambda_1_equals_scalar_times_q_times_Q4": True,
    "scalar_in_QQ_delta": display(ratio),
    "S_div_q_coefficients_by_ascending_q_power": [display(q_coefficient(s1_div_q, i)) for i in range(5)],
    "compact_Q4": display(compact_q4),
    "infinity_H": display(h_infinity),
    "infinity_Q4": display(q4_infinity),
    "infinity_disjointness_identity": "(45*delta^2-38*delta-29) - (45*delta-83)*(delta+1) = 54",
    "T_at_delta_minus_1": "54",
    "Q4_at_q_0": display(q_coefficient(compact_q4, 0)),
    "captured_compact_denominators": [f"{c}*(45*delta^2-38*delta-29)^9" for c in denominator_scalars],
    "coefficient_identity_scope": "Polynomial identities over QQ[delta,q], with no parameter denominator after lambda=1.",
    "main_source_normalization_scope": "Original rational normalizations divide by delta and by delta^3; underlying proportional parameterization divides by lambda and lambda^2. The literal lambda=1 coefficient identities themselves extend polynomially to delta=0; intended original chart is delta nonzero.",
    "compact_remainder_denominator_chart": "T=45*delta^2-38*delta-29 nonzero. The separate leading-drop arithmetic identity does not use those denominators.",
    "characteristic_scope": "QQ/characteristic zero only. No claim for reduction in arbitrary positive characteristic.",
    "geometry_claims": "None. This audit only binds captured coefficient lists to displayed polynomials, denominator factors, and the stated leading coefficient arithmetic.",
}
result_path = OUT / "lambda-binding-result.json"
result_path.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
print("PASS all literal coefficient bindings")
