#!/usr/bin/env python3
"""Exact, standard-library verification of the normalized parity-family dual.

The saved tensors use actual quartic forms. This verifier independently
contracts them with the polynomial ancestor alpha(c,lambda), checks its top
symbol, and proves n(c,lambda)^T L(alpha)=0 with n^T u=1. It therefore
excludes every common u,v ancestor in this normalized family, for all c and
lambda over an algebraic closure of QQ. No Gröbner calculation is needed.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
from math import comb

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
D = json.loads((HERE/'localcoh-incidence-parity-dual-2026-10-06.json').read_text())
for name, expected in D['coordinate_file_sha256'].items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected, name

def decoded(terms):
    out = {}
    for i, j, value in terms:
        assert (i, j) not in out and i >= 0 and j >= 0
        if Q(value):
            out[i, j] = Q(value)
    return out

def scale(a, value):
    value = Q(value)
    return {m: value*v for m, v in a.items() if value*v}

def add(a, b):
    out = dict(a)
    for m, value in b.items():
        out[m] = out.get(m, Q(0)) + value
        if not out[m]:
            del out[m]
    return out

def multiply(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            m = (i+k, j+l)
            out[m] = out.get(m, Q(0)) + x*y
            if not out[m]:
                del out[m]
    return out

def linear_sum(coefficients, polynomials):
    result = {}
    for value, polynomial in zip(coefficients, polynomials):
        if value:
            result = add(result, scale(polynomial, value))
    return result

alpha = list(map(decoded, D['alpha_polynomials']))
dual = list(map(decoded, D['dual_polynomials']))
assert len(alpha) == 30 and len(dual) == 74
lines = (HERE/'localcoh-incidence-tensor.txt').read_text().splitlines()
assert lines[0] == '30 18 74 542'
rows = [[Q(0)]*542 for _ in range(74)]
seen = set()
for line in lines[1:]:
    r, c, value = line.split()
    r, c = int(r), int(c)
    assert 0 <= r < 74 and 0 <= c < 542 and (r, c) not in seen
    seen.add((r, c))
    rows[r][c] = Q(value)
assert [row[540] for row in rows] == [Q(r == 72) for r in range(74)]
assert [row[541] for row in rows] == [Q(r == 73) for r in range(74)]
base_lines = (HERE/'localcoh-incidence-bases.txt').read_text().splitlines()
assert base_lines[1:31] == (HERE/'localcoh-symbol-numerators.txt').read_text().splitlines()

TOP = json.loads((HERE/'localcoh-symbol-top.json').read_text())
M = [[Q(value) for value in row] for row in TOP['matrix']]
assert len(M) == 32 and all(len(row) == 30 for row in M)
expected = [{} for _ in range(32)]
for i in range(4):
    for k in range(i+1):
        j = 2*k + 3-i
        expected[8*i+j] = {(3-i, 0): Q(comb(i, k))}
assert [linear_sum(row, alpha) for row in M] == expected
# This also verifies that the freely varying lambda term lies in the kernel.
shifted = []
for i in range(4):
    shifted.extend([{}] + expected[8*i:8*i+7])
obstructions = [linear_sum(row, shifted) for row in TOP['annihilator']]
assert any(len(p) == 1 and (0, 0) in p and p[0, 0] for p in obstructions)
print('PASS: alpha(c,lambda) has exactly the intended pure cubic top; h=t cannot lift for any c.')

for j in range(18):
    result = {}
    for r in range(74):
        entry = linear_sum([rows[r][18*i+j] for i in range(30)], alpha)
        result = add(result, multiply(dual[r], entry))
    assert not result, (j, result)
assert dual[72] == {(0, 0): Q(1)}
assert decoded(D['dual_on_u']) == dual[72]
assert decoded(D['dual_on_v']) == dual[73]
print('PASS: n(c,lambda)^T L(alpha(c,lambda)) vanishes identically in QQ[c,lambda].')
print('PASS: n(c,lambda)^T u=1 identically; no quartic produces u anywhere in the family.')
print('PROVED: normalized parity direction (1+t²,c*t), h=1, has no common quartic u,v ancestor.')
print('Scope includes every lower-order T3 coefficient and all characteristic-zero field extensions.')
