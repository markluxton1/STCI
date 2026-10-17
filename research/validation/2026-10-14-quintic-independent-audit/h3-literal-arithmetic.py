"""Independent multiplication audit of NEW literal quintic support captures.

Only Python standard library exact arithmetic is used. No accepted verifier is
imported or executed. The polynomial evaluator below reads mathematical text
as a restricted AST; it does not call eval. This is an arithmetic identity
audit, not a normalization/conductor or geometric coverage proof.
"""
from fractions import Fraction
from pathlib import Path
import ast
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
H3 = ROOT / "research/validation/2026-10-13-h3-zero-chart-conductor-new/new-exact-support-incidence.json"
L1 = ROOT / "research/validation/2026-10-13-evening-h3-proportional"
AUDIT = Path(__file__).resolve().parent
inputs = [H3, L1 / "lambda1-compact-numerators.txt", L1 / "lambda1-compact-denominators.txt", L1 / "lambda1-bezout.txt"]
checks = []


def scalar(c):
    c = Fraction(c)
    return {(0, 0): c} if c else {}


def plus(a, b, sign=1):
    result = a.copy()
    for exponent, coefficient in b.items():
        value = result.get(exponent, Fraction(0)) + sign * coefficient
        if value:
            result[exponent] = value
        else:
            result.pop(exponent, None)
    return result


def product(a, b):
    result = {}
    for (i, j), c in a.items():
        for (u, v), d in b.items():
            exponent = (i + u, j + v)
            result[exponent] = result.get(exponent, Fraction(0)) + c * d
    return {e: c for e, c in result.items() if c}


def times(c, p):
    return {e: c * v for e, v in p.items() if c * v}


def exponentiate(p, n):
    assert type(n) is int and n >= 0
    result = scalar(1)
    while n:
        if n & 1:
            result = product(result, p)
        p = product(p, p)
        n >>= 1
    return result


def parse(text, names):
    node = ast.parse(text.replace("^", "**").replace("{", "[").replace("}", "]"), mode="eval").body

    def walk(n):
        if isinstance(n, ast.Constant) and type(n.value) is int:
            return scalar(n.value)
        if isinstance(n, ast.Name):
            return names[n.id]
        if isinstance(n, (ast.List, ast.Tuple)):
            return [walk(x) for x in n.elts]
        if isinstance(n, ast.UnaryOp):
            assert isinstance(n.op, (ast.USub, ast.UAdd))
            return times(-1 if isinstance(n.op, ast.USub) else 1, walk(n.operand))
        if isinstance(n, ast.BinOp):
            if isinstance(n.op, ast.Pow):
                assert isinstance(n.right, ast.Constant)
                return exponentiate(walk(n.left), n.right.value)
            left, right = walk(n.left), walk(n.right)
            if isinstance(n.op, ast.Add):
                return plus(left, right)
            if isinstance(n.op, ast.Sub):
                return plus(left, right, -1)
            if isinstance(n.op, ast.Mult):
                return product(left, right)
            if isinstance(n.op, ast.Div):
                assert len(right) == 1 and (0, 0) in right, "only rational scalar division is accepted"
                return times(1 / right[(0, 0)], left)
        raise ValueError(ast.dump(n))

    return walk(node)


def check(name, assertion, detail):
    assert assertion, name
    checks.append({"name": name, "passed": True, "detail": detail})
    print("PASS", name, "::", detail, flush=True)


def encoded_poly(rows):
    result = {}
    for row in rows:
        i, j = row["j"], row["p"]
        assert type(i) is int and type(j) is int and i >= 0 and j >= 0
        assert (i, j) not in result
        c = Fraction(row["coefficient"])
        assert c
        result[(i, j)] = c
    return result


def ascending_poly(coefficients):
    return {(i, 0): Fraction(c) for i, c in enumerate(coefficients) if Fraction(c)}


def degree(p, variable):
    return max((e[variable] for e in p), default=-1)


def coefficient(p, variable, n):
    result = {}
    for e, c in p.items():
        if e[variable] == n:
            rest = list(e)
            rest[variable] = 0
            result[tuple(rest)] = c
    return result


def q_shift(p, n):
    return {(i, j + n): c for (i, j), c in p.items()}


def pseudo_remainder(p, divisor):
    """Division in second variable, fraction free over first-variable ring.

    Each step replaces R by lc(divisor)*R - lc(R)*q^gap*divisor.
    A zero result proves divisibility over the fraction field. No GCD or
    newly generated Bezout coefficients are used.
    """
    d = degree(divisor, 1)
    lead = coefficient(divisor, 1, d)
    steps = 0
    r = p
    while r and degree(r, 1) >= d:
        n = degree(r, 1)
        r = plus(product(lead, r), product(coefficient(r, 1, n), q_shift(divisor, n - d)), -1)
        assert not r or degree(r, 1) < n
        steps += 1
    return r, steps


record = json.loads(H3.read_text())
fp = encoded_poly(record["zero_P_F"])
fj = encoded_poly(record["zero_J_F"])
s = encoded_poly(record["S"])
q5 = encoded_poly(record["Q5_monic"])
quotient = encoded_poly(record["S5_division_quotient"])
remainder = encoded_poly(record["S5_division_remainder"])
check("h3-Q5-monic-degree-five", degree(q5, 1) == 5 and coefficient(q5, 1, 5) == scalar(1), "Q5 is monic of degree 5 in p")
check("h3-original-octic-factor-binding", product(s, q5) == times(Fraction(9, 2), fp), "S*Q5 = (9/2)*captured zero_P_F")
check("h3-original-support-division-product", plus(product(q5, quotient), remainder) == exponentiate(s, 5), "Q5*captured quotient + captured remainder = S^5")
check("h3-remainder-degree", degree(remainder, 1) < 5, "captured remainder has p-degree below 5")
original_coefficients = [ascending_poly(cs) for cs in record["remainder_coefficients_ascending_j"]]
check("h3-original-generator-list-binding", len(original_coefficients) == 5 and all(coefficient(remainder, 1, i) == p for i, p in enumerate(original_coefficients)), "five original coefficient lists equal the captured bivariate remainder")
bezout = [ascending_poly(cs) for cs in record["bezout_coefficients_ascending_j"]]
check("h3-bezout-list-length", len(bezout) == len(original_coefficients), "one captured witness per original generator")
total = {}
for c, b in zip(original_coefficients, bezout):
    total = plus(total, product(c, b))
check("h3-original-generator-bezout-product", total == scalar(1) == ascending_poly(record["bezout_gcd_ascending_j"]), "sum of five captured coefficient/witness products is exactly 1")
one_minus = {(0, 1): Fraction(1), (0, 0): Fraction(-1)}
transformed = {}
for (jj, pp), c in fp.items():
    assert pp <= 8
    transformed = plus(transformed, product({(jj, pp): (-1) ** jj * c}, exponentiate(one_minus, 8 - pp)))
check("h3-captured-binary-octic-coordinate-swap", transformed == fj, "FJ(p,j) = (p-1)^8*FP(p/(p-1),-j)")
transformed_s = {}
for (jj, pp), c in s.items():
    assert pp <= 3
    transformed_s = plus(transformed_s, product({(jj, pp): Fraction(-2, 3) * (-1) ** jj * c}, exponentiate(one_minus, 3 - pp)))
literal_ptj = parse("-2*j+(6*j-4)*p+(4-6*j)*p^2+(2*j-2/3)*p^3", {"j": {(1, 0): Fraction(1)}, "p": {(0, 1): Fraction(1)}})
check("h3-conormal-coordinate-swap", transformed_s == literal_ptj, "(-2/3)*(p-1)^3*S(p/(p-1),-j) equals displayed zero-J conormal")

dl = {(1, 0): Fraction(1)}
q = {(0, 1): Fraction(1)}
names = {"dl": dl, "q": q}
numerators = parse((L1 / "lambda1-compact-numerators.txt").read_text(), names)
denominators = parse((L1 / "lambda1-compact-denominators.txt").read_text(), names)
matrix_text = (L1 / "lambda1-bezout.txt").read_text()
assert matrix_text.startswith("matrix ")
matrix = parse(matrix_text[len("matrix "):], names)
check("lambda1-original-generator-and-matrix-shape", len(numerators) == len(denominators) == len(matrix) == 4 and all(len(row) == 1 for row in matrix), "four numerators, four denominators, and a 4 by 1 captured witness matrix")
total = {}
for n, row in zip(numerators, matrix):
    total = plus(total, product(n, row[0]))
check("lambda1-original-generator-bezout-product", total == scalar(1), "sum of four captured numerator/witness products is exactly 1")
h = parse("(dl+1)*q^3-6*q^2+(6-6*dl)*q+4*dl", names)
q4 = parse("(90*dl^2-76*dl-58)*q^4+(-405*dl^2+458*dl+203)*q^3+(675*dl^2-858*dl-261)*q^2+(-450*dl^2+800*dl+174)*q-400*dl", names)
t = parse("45*dl^2-38*dl-29", names)
common = exponentiate(t, 9)
scales = [32, 256, 512, 512]
check("lambda1-captured-denominator-factors", all(d == times(k, common) for d, k in zip(denominators, scales)), "denominators are respectively 32,256,512,512 times (45*dl^2-38*dl-29)^9")
# Clearing the common denominator, rather than generating the remainder anew.
cleared_remainder = {}
for i, (n, k) in enumerate(zip(numerators, scales)):
    cleared_remainder = plus(cleared_remainder, q_shift(times(Fraction(1, k), n), i))
dividend = plus(product(common, exponentiate(h, 4)), cleared_remainder, -1)
residual, steps = pseudo_remainder(dividend, q4)
check("lambda1-original-numerator-denominator-remainder-binding", residual == {} and degree(cleared_remainder, 1) < 4, f"cleared H^4 minus captured remainder is divisible by Q4; {steps} fraction-free division steps")
check("lambda1-leading-coefficient-binding", coefficient(q4, 1, 4) == times(2, t), "Q4 leading q coefficient equals 2*(45*dl^2-38*dl-29)")
infinity_witness = parse("(dl+1)*(45*dl-83)+54", names)
check("lambda1-leading-drop-infinity-separation", infinity_witness == t and coefficient(h, 1, 3) == parse("dl+1", names), "T=(dl+1)*(45*dl-83)+54; H infinity coefficient is dl+1")
check("lambda1-extra-A4-root-separation", coefficient(q4, 1, 0) == times(-400, dl), "Q4(0)=-400*dl, hence no residual A4 root on dl nonzero")

report = {
    "scope": "Independent literal exact arithmetic identity audit; no accepted script reruns and no geometric acceptance claim",
    "arithmetic": "Python standard library fractions.Fraction; restricted AST parsing; sparse polynomial convolution; fraction-free division",
    "input_files": [{"path": str(p.relative_to(ROOT)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs],
    "checks": checks,
    "check_count": len(checks),
    "h3_original_remainder_generator_degrees": [degree(p, 0) for p in original_coefficients],
    "h3_captured_witness_degrees": [degree(p, 0) for p in bezout],
    "lambda1_original_numerator_degrees": [degree(p, 0) for p in numerators],
    "lambda1_captured_witness_degrees": [degree(row[0], 0) for row in matrix],
    "lambda1_denominator_open_chart": "45*dl^2-38*dl-29 != 0",
    "remaining_scope": "The arithmetic verifies the captured original generator certificates and their remainder binding. Normalization/conductor geometry, admissibility, and the proportional-stratum coverage are outside this audit.",
}
(AUDIT / "h3-literal-arithmetic-report.json").write_text(json.dumps(report, indent=2) + "\n")
print("ALL", len(checks), "LITERAL ARITHMETIC CHECKS PASSED")
