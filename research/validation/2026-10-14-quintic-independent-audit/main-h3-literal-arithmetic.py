"""Independent exact product audit of the NEW main H|S witness capture.

This reads the saved original remainder generators and witness matrix only.
It imports no repository CAS/verifier code and uses no computer algebra
system. Expanded monomials are parsed with a strict, separate text parser;
rational witness denominators are cleared before integer convolution.
"""
from fractions import Fraction
from math import lcm
from pathlib import Path
import hashlib
import json
import re
import time

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CAPTURE = ROOT / "research/validation/2026-10-13-generalization-quintic-h3"
MAIN = ROOT / "research/validation/2026-10-13-evening-h3-proportional/main-S-coefficients.txt"
paths = {
    "original_remainder": CAPTURE / "h-divides-s-remainder.txt",
    "original_witness": CAPTURE / "h-divides-s-witness.txt",
    "captured_exponent": CAPTURE / "h-divides-s-witness-exponent.txt",
    "main_S_coefficients": MAIN,
    "witness_schema_source": ROOT / "research/computations/generalization_quintic_h3_divisibility_certificate.m2",
}
started = time.monotonic()


def add(a, b):
    out = a.copy()
    for e, c in b.items():
        out[e] = out.get(e, 0) + c
        if out[e] == 0:
            del out[e]
    return out


def scale(a, c):
    return {e: x * c for e, x in a.items() if x * c}


def multiply(a, b):
    out = {}
    for (i, j), c in a.items():
        for (u, v), d in b.items():
            e = i + u, j + v
            out[e] = out.get(e, 0) + c * d
    return {e: c for e, c in out.items() if c}


def terms(text):
    """Split sums outside parentheses; the entire input must be consumed."""
    text = re.sub(r"\s+", "", text)
    text = re.sub(r"\bdelta\b", "dl", text)
    text = re.sub(r"\blambda\b", "ll", text)
    pieces = []
    depth = 0
    start = 0
    for i, char in enumerate(text):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            assert depth >= 0
        elif char in "+-" and depth == 0 and i > start:
            pieces.append(text[start:i])
            start = i
    assert depth == 0
    pieces.append(text[start:])
    assert all(pieces)
    return pieces


def expanded_poly(text):
    """Parse a sum of coefficient*dl^a*ll^b monomials, without eval/AST."""
    out = {}
    variable = re.compile(r"(dl|ll)(?:\^([0-9]+))?\Z")
    number = re.compile(r"[+-]?[0-9]+(?:/[0-9]+)?\Z")
    for term in terms(text):
        sign = -1 if term[0] == "-" else 1
        if term[0] in "+-":
            term = term[1:]
        assert term
        coefficient = Fraction(sign)
        exponent = [0, 0]
        for factor in term.split("*"):
            assert factor
            matched = variable.fullmatch(factor)
            if matched:
                exponent[0 if matched[1] == "dl" else 1] += int(matched[2] or 1)
            else:
                if factor.startswith("(") and factor.endswith(")"):
                    factor = factor[1:-1]
                assert number.fullmatch(factor), f"Unexpected nonexpanded factor: {factor[:100]}"
                coefficient *= Fraction(factor)
        e = tuple(exponent)
        out[e] = out.get(e, Fraction(0)) + coefficient
    return {e: c for e, c in out.items() if c}


def coefficient_list(text):
    text = text.strip()
    assert text.startswith("{") and text.endswith("}")
    return [expanded_poly(p) for p in text[1:-1].split(",")]


def integer_poly(p):
    assert all(c.denominator == 1 for c in p.values())
    return {e: c.numerator for e, c in p.items()}


original = coefficient_list(paths["original_remainder"].read_text())
assert len(original) == 3
assert all(j >= 2 for p in original for i, j in p)
generators = [{(i, j - 2): c for (i, j), c in integer_poly(p).items()} for p in original]
print("PASS exact original coefficient division by ll^2", flush=True)
witness_text = paths["original_witness"].read_text().strip()
assert witness_text.startswith("matrix {") and witness_text.endswith("}")
row_texts = re.findall(r"\{([^{}]*)\}", witness_text[len("matrix "):])
assert len(row_texts) == 3 and all("," not in row for row in row_texts)
witnesses = [expanded_poly(row) for row in row_texts]
denominators = [lcm(*(c.denominator for c in w.values())) for w in witnesses]
global_denominator = lcm(*denominators)
integer_witnesses = [integer_poly(scale(w, denominator)) for w, denominator in zip(witnesses, denominators)]
print("PASS captured matrix parsed as three rational polynomials", flush=True)
print("original generator term counts:", [len(p) for p in generators], flush=True)
print("captured witness term counts:", [len(p) for p in witnesses], flush=True)
captured_exponent = int(paths["captured_exponent"].read_text())
assert captured_exponent == 2
s_coefficients = coefficient_list(paths["main_S_coefficients"].read_text())
assert len(s_coefficients) == 6
s5 = integer_poly(s_coefficients[5])
u = s5
for factor in ["dl", "ll", "ll-1", "ll^2-4*ll+1", "dl*ll+dl+ll-1", "dl+2*ll-1"]:
    u = multiply(u, integer_poly(expanded_poly(factor)))
target = multiply(u, u)
lhs_numerator = {}
for i, (g, w, denominator) in enumerate(zip(generators, integer_witnesses, denominators)):
    lhs_numerator = add(lhs_numerator, scale(multiply(g, w), global_denominator // denominator))
    print(f"multiplied original witness entry {i + 1} of 3", flush=True)
residual = add(lhs_numerator, scale(target, -global_denominator))
assert residual == {}, "captured original-generator matrix product differs from U^2"
print("PASS exact captured original-generator witness product equals U^2", flush=True)
elapsed = time.monotonic() - started
report = {
    "audit_kind": "Supporting independent literal arithmetic identity audit",
    "accepted_scripts_rerun": False,
    "arithmetic": "Python standard library fractions, strict expanded-monomial text parser, denominator-cleared integer convolution",
    "input_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in paths.items()},
    "input_paths": {name: str(path.relative_to(ROOT)) for name, path in paths.items()},
    "original_coefficient_division": "each captured h-divides-s-remainder entry is exactly divisible by ll^2",
    "original_generator_term_counts": [len(p) for p in generators],
    "captured_witness_term_counts": [len(p) for p in witnesses],
    "original_generator_bidegrees": [[max(e[0] for e in p), max(e[1] for e in p)] for p in generators],
    "captured_witness_bidegrees": [[max(e[0] for e in p), max(e[1] for e in p)] for p in witnesses],
    "witness_matrix_shape": [3, 1],
    "captured_exponent": captured_exponent,
    "target": "(S_coeff5*dl*ll*(ll-1)*(ll^2-4*ll+1)*((ll+1)*dl+ll-1)*(dl+2*ll-1))^2",
    "target_term_count": len(target),
    "literal_original_generator_product_equals_target": True,
    "exact_residual_term_count": len(residual),
    "global_witness_denominator_decimal_digits": len(str(global_denominator)),
    "elapsed_seconds": elapsed,
    "scope": "The saved original three generators divided by ll^2 times the saved 3 by 1 witness equal the stated U^2 in QQ[dl,ll]. No newly generated ideal/Groebner witness, no exponent minimality assertion, and no conductor geometry or stratum-coverage acceptance is claimed.",
}
(HERE / "main-h3-literal-arithmetic-report.json").write_text(json.dumps(report, indent=2) + "\n")
print(f"ALL MAIN H3 LITERAL PRODUCT CHECKS PASSED; elapsed {elapsed:.3f} seconds")
