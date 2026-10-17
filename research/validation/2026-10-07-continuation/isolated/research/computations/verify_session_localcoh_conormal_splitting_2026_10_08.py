#!/usr/bin/env python3
"""Independent standard-library check of the intrinsic splitting rank record.

The theorem's sheaf map is proved in the companion note. This checks the
exact degree arithmetic, Laurent cup matrices and determinant expressions;
it does not evaluate any actual ambient extension class or exclude a stratum.
"""
from pathlib import Path
from fractions import Fraction as Q
import ast
import hashlib
import itertools
import json

HERE = Path(__file__).resolve().parent
RECORD = HERE/'session_localcoh_conormal_hankel_2026_10_07.json'
NOTE = HERE.parent/'notes/2026-10-07-session-localcoh-conormal-splitting.md'


def add(a, b):
    result = dict(a)
    for power, coefficient in b.items():
        result[power] = result.get(power, Q(0))+coefficient
        if not result[power]:
            del result[power]
    return result


def scale(a, c):
    return {power: coefficient*c for power, coefficient in a.items() if coefficient*c}


def multiply(a, b):
    result = {}
    for left, x in a.items():
        for right, y in b.items():
            result = add(result, {tuple(sorted(left+right)): x*y})
    return result


def polynomial(node):
    if isinstance(node, ast.Expression):
        return polynomial(node.body)
    if isinstance(node, ast.Constant):
        assert isinstance(node.value, int)
        return {(): Q(node.value)} if node.value else {}
    if isinstance(node, ast.Name):
        assert node.id.startswith('c') and node.id[1:].isdecimal()
        return {(int(node.id[1:]),): Q(1)}
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return scale(polynomial(node.operand), Q(-1))
    assert isinstance(node, ast.BinOp)
    a, b = polynomial(node.left), polynomial(node.right)
    if isinstance(node.op, ast.Add):
        return add(a, b)
    if isinstance(node.op, ast.Sub):
        return add(a, scale(b, Q(-1)))
    if isinstance(node.op, ast.Mult):
        return multiply(a, b)
    if isinstance(node.op, ast.Pow):
        assert set(b).issubset({()}) and b.get((), Q(0)).denominator == 1
        n = int(b.get((), Q(0)))
        assert n >= 0
        result = {(): Q(1)}
        for _ in range(n):
            result = multiply(result, a)
        return result
    raise AssertionError(type(node.op))


def determinant(matrix):
    n = len(matrix)
    result = {}
    for permutation in itertools.permutations(range(n)):
        sign = (-1)**sum(permutation[i] > permutation[j]
                         for i in range(n) for j in range(i+1, n))
        monomial = tuple(sorted(int(matrix[i][j][1:]) for i, j in enumerate(permutation)))
        result = add(result, {monomial: Q(sign)})
    return result


data = json.loads(RECORD.read_text())
assert len(data['rows']) == 13
checked = []
for row in data['rows']:
    e, d2, d3 = row['e'], row['d2'], row['d3']
    assert e in (0, 1, 2) and d3 == 7-3*e and 0 <= d2 <= d3
    P, Qline = 3*e-5+d2, 9-e-d2
    assert P+Qline == 2*e+4
    assert row['extension_line_degree'] == P-Qline
    assert row['extension_dimension'] == max(0, Qline-P-1)
    twist = 3 if e == 0 else 2*e+2
    domain, target = Qline-twist, P-twist
    assert domain >= 0 and target <= -2
    matrix = row['connecting_matrix']
    assert len(matrix) == -target-1
    assert all(len(values) == domain+1 for values in matrix)
    # Multiplying z^j into c_l*z^-l contributes to the i-th H1
    # coordinate exactly when l=i+j+1, with no discarded endpoints.
    for i, values in enumerate(matrix):
        for j, coefficient in enumerate(values):
            contributions = [ell for ell in range(1, row['extension_dimension']+1)
                             if j-ell == -i-1]
            assert contributions == [i+j+1]
            assert coefficient == 'c'+str(i+j+1)
    required = domain+1 if e == 0 else domain
    assert row['required_rank'] == required
    if e == 1:
        assert domain+1 == 5-d2 and len(matrix) == domain+1
        assert determinant(matrix) == polynomial(ast.parse(row['determinant_equation'], mode='eval'))
    checked.append({'e': e, 'd2': d2, 'matrix_shape': [len(matrix), domain+1],
                    'required_rank': required})

# Exact split equivalences: write the larger summand as O(a).
# For e>=1, a>=e+2, and h0 after twist -(2e+2) equals
# max(a-2e-1,0); it is one iff a=2e+2.
# For e=0, a>=2 and h0 after twist -3 equals a-2;
# it is zero iff a=2. These closed formulas prove the equivalence.
for e in (1, 2):
    total, target_larger = 2*e+4, 2*e+2
    for a in range(e+2, target_larger+6):
        h0 = max(a-target_larger+1, 0)+max(total-a-target_larger+1, 0)
        assert h0 == max(a-2*e-1, 0)
        assert (h0 == 1) == (a == target_larger)
for a in range(2, 12):
    assert max(a-2, 0)+max(2-a, 0) == a-2
    assert (a-2 == 0) == (a == 2)

checks = {
    'status': 'PASS: necessary splitting degrees, all Laurent cup matrices and e1 symbolic determinants',
    'scope': 'No actual ambient extension class is evaluated; no positive-D2 stratum is excluded',
    'record_sha256': hashlib.sha256(RECORD.read_bytes()).hexdigest(),
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'proof_sha256': hashlib.sha256(NOTE.read_bytes()).hexdigest(),
    'rank_rows': checked,
    'retained': 'e1,d2=4 zero-extension and Gorenstein boundary remains open'
}
(HERE/'session_localcoh_conormal_splitting_audit_2026_10_08.json').write_text(json.dumps(checks, indent=2)+'\n')
print('PASS: complete necessary degree data and every Laurent cup-product coefficient.')
print('PASS: all four e1 determinant expressions independently reconstructed; exact required ranks3,2,1,0.')
print('PASS: e2 ranks1,0 and e0 full-rank criteria, with their distinct twists.')
print('OPEN: actual ambient extension classes, unique-quotient quartic image and remaining positive-D2 strata.')
