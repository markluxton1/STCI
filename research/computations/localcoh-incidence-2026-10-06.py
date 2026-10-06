#!/usr/bin/env python3
"""Verify the Oct6 exact finite incidence coordinates and a polynomial dual.

Only Python's standard library is required. For exact coordinate regeneration,
first run localcoh-incidence-tensor.m2 from the repository root. This script
proves the fixed direction (1+t²,-2t), h=1 has no quartic multiplier to either
of the two target classes, for any lower-order T3 coefficient. It does not
claim that the full 30-dimensional quartic incidence is empty.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
D = json.loads((HERE / 'localcoh-incidence-2026-10-06-certificate.json').read_text())
for name, expected in D['coordinate_file_sha256'].items():
    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    assert actual == expected, (name, actual, expected)

lines = (HERE / 'localcoh-incidence-tensor.txt').read_text().splitlines()
assert tuple(map(int, lines[0].split())) == (30, 18, 74, 542)
rows = [[Q(0)] * 542 for _ in range(74)]
seen = set()
for line in lines[1:]:
    i, j, value = line.split()
    i, j = int(i), int(j)
    assert 0 <= i < 74 and 0 <= j < 542 and (i, j) not in seen
    seen.add((i, j))
    rows[i][j] = Q(value)
assert [row[540] for row in rows] == [Q(int(i == 72)) for i in range(74)]
assert [row[541] for row in rows] == [Q(int(i == 73)) for i in range(74)]

# Confirm the 30 coordinate columns agree with the source of the top map.
bases = (HERE / 'localcoh-incidence-bases.txt').read_text().splitlines()
assert bases[0] == 'ancestor stage4 numerators' and bases[31] == 'quartic multipliers'
assert bases[1:31] == (HERE / 'localcoh-symbol-numerators.txt').read_text().splitlines()
assert len(bases[32:]) == 18
M = [[Q(v) for v in row] for row in json.loads((HERE / 'localcoh-symbol-top.json').read_text())['matrix']]
assert len(M) == 32 and all(len(row) == 30 for row in M)

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))

def rank(matrix):
    a = [row[:] for row in matrix]
    pivot = 0
    for col in range(len(a[0])):
        candidate = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if candidate is None:
            continue
        a[pivot], a[candidate] = a[candidate], a[pivot]
        factor = a[pivot][col]
        a[pivot] = [v/factor for v in a[pivot]]
        for i in range(pivot + 1, len(a)):
            factor = a[i][col]
            if factor:
                a[i] = [v - factor*w for v, w in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot

def product(a, b):
    result = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result

def power(a, n):
    result = [Q(1)]
    for _ in range(n):
        result = product(result, a)
    return result

seed = list(map(Q, D['alpha_seed']))
kernel = list(map(Q, D['alpha_kernel']))
assert len(seed) == len(kernel) == 30 and any(kernel)
top = []
for i in range(4):
    coefficients = product(power([Q(1), Q(0), Q(1)], i), power([Q(0), Q(-2)], 3-i))
    top.extend(coefficients + [Q(0)] * (8-len(coefficients)))
assert [dot(row, seed) for row in M] == top
assert [dot(row, kernel) for row in M] == [Q(0)] * 32
assert rank(M) == 29
shifted = []
for i in range(4):
    shifted.extend([Q(0)] + top[8*i:8*i+7])
assert rank([row + [value] for row, value in zip(M, shifted)]) == 30
print('PASS: this primitive direction admits exactly the h=constant top line.')
print('PASS: every lift of this normalized top symbol is seed+c*kernel.')

A0 = [[sum((rows[r][18*i+j]*seed[i] for i in range(30)), Q(0)) for j in range(18)] for r in range(74)]
A1 = [[sum((rows[r][18*i+j]*kernel[i] for i in range(30)), Q(0)) for j in range(18)] for r in range(74)]
n0 = list(map(Q, D['dual_constant']))
n1 = list(map(Q, D['dual_parameter']))
assert len(n0) == len(n1) == 74
for j in range(18):
    c0 = [A0[r][j] for r in range(74)]
    c1 = [A1[r][j] for r in range(74)]
    assert dot(n0, c0) == 0
    assert dot(n0, c1) + dot(n1, c0) == 0
    assert dot(n1, c1) == 0
assert n0[72] == 1 and n1[72] == 0
assert n0[73] == Q(8,11) and n1[73] == 0
print('PASS: n(c)^T A(seed+c*kernel)=0 identically as a degree-two polynomial.')
print('PASS: n(c)^T u=1 and n(c)^T v=8/11; neither target can be produced.')
print('PASS: exact sparse tensor has standard target columns e72,e73.')
print('Scope: fixed normalized top direction (1+t²,-2t), all quartics, all c.')
