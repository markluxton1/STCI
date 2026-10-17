"""Exact coefficient extraction from the frozen degree-eight polynomial.

Standard-library polynomial arithmetic; no eval, SymPy, or replay of M2.
This checks the coefficient identity, not the conductor's geometric status.
"""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "research/validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt"
EXPECTED_INPUT_SHA256 = "d5701314fdf45a60b66d4763159ac383a7fed5eb51d9821115455ab968e0ea84"
VARIABLES = ("delta", "a", "B", "G", "J", "p")
ZERO_EXP = (0,) * len(VARIABLES)


def add(left, right, scale=1):
    answer = dict(left)
    for exponent, coefficient in right.items():
        answer[exponent] = answer.get(exponent, 0) + scale * coefficient
        if not answer[exponent]:
            del answer[exponent]
    return answer


def multiply(left, right):
    answer = {}
    for le, lc in left.items():
        for re, rc in right.items():
            exponent = tuple(x + y for x, y in zip(le, re))
            answer[exponent] = answer.get(exponent, 0) + lc * rc
    return {e: c for e, c in answer.items() if c}


def polynomial(node):
    if isinstance(node, ast.Constant) and type(node.value) is int:
        return {ZERO_EXP: node.value} if node.value else {}
    if isinstance(node, ast.Name) and node.id in VARIABLES:
        exponent = list(ZERO_EXP)
        exponent[VARIABLES.index(node.id)] = 1
        return {tuple(exponent): 1}
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        scale = -1 if isinstance(node.op, ast.USub) else 1
        return {e: scale * c for e, c in polynomial(node.operand).items()}
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Add):
            return add(polynomial(node.left), polynomial(node.right))
        if isinstance(node.op, ast.Sub):
            return add(polynomial(node.left), polynomial(node.right), -1)
        if isinstance(node.op, ast.Mult):
            return multiply(polynomial(node.left), polynomial(node.right))
        if isinstance(node.op, ast.Pow):
            if not (isinstance(node.right, ast.Constant) and type(node.right.value) is int and node.right.value >= 0):
                raise ValueError("Expected a nonnegative integer exponent")
            answer = {ZERO_EXP: 1}
            base = polynomial(node.left)
            for _ in range(node.right.value):
                answer = multiply(answer, base)
            return answer
    raise ValueError(f"Unsupported syntax: {ast.dump(node)}")


raw = INPUT.read_bytes()
input_hash = hashlib.sha256(raw).hexdigest()
assert input_hash == EXPECTED_INPUT_SHA256
tree = ast.parse(raw.decode().replace("^", "**"), mode="eval")
full = polynomial(tree.body)
assert len(full) == 344
specialized = {e: c for e, c in full.items() if not e[1] and not e[2]}
coefficient_8 = {e[:-1]: c for e, c in specialized.items() if e[-1] == 8}
coefficient_7 = {e[:-1]: c for e, c in specialized.items() if e[-1] == 7}
assert coefficient_8 == {}
assert coefficient_7 == {(7, 0, 0, 0, 0): 1}
assert max(e[-1] for e in specialized) == 7
print(json.dumps({
    "status": "PASS",
    "input": str(INPUT.relative_to(ROOT)),
    "input_sha256": input_hash,
    "full_monomial_count": len(full),
    "specialized_monomial_count": len(specialized),
    "specialization": "a=B=0",
    "coefficient_p8": "0",
    "coefficient_p7": "delta^7",
    "specialized_p_degree": 7,
    "scope": "Exact coefficient identity from frozen F; no geometric conductor assertion",
}, indent=2))
