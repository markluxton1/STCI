#!/usr/bin/env python3
"""Check the exact finite normal-quartic bound and a cusp matrix example.

Geometric hypotheses and the compression proof are in the companion note.
This script does not assert existence of a surface with this matrix.
"""

from fractions import Fraction as Q
from functools import reduce
from math import lcm
import json

import sympy as sp


A = sp.Matrix([[3, -1, 0, -1], [-1, 2, -1, 0],
               [0, -1, 2, -1], [-1, 0, -1, 2]])
a = sp.ones(4, 1)
m = sp.Matrix([0, 0, 1, 0])
assert all(A[:i, :i].det() > 0 for i in range(1, 5))
assert A.det() == 4
assert (a.T*A*a)[0] == 1
assert A*a == sp.Matrix([1, 0, 0, 0])
correction = A.inv()*m
assert correction == sp.Matrix([1, sp.Rational(3, 2), 2, sp.Rational(3, 2)])
assert (m.T*correction)[0] == 2

B = sp.diag(A, 2*sp.eye(6))
v = sp.Matrix(list(m)+[1]*6)
full_correction = B.inv()*v
denominator = reduce(lcm, [int(q.q) for q in full_correction], 1)
assert denominator == 2
assert (v.T*full_correction)[0] == 5
assert B.det() == 256
assert B.det() % denominator == 0

# In the proved application d<=3, so every diagonal b_i<=d+2<=5.
for b in range(1, 6):
    assert Q(b, 2) <= Q(3, 2)**max(b-2, 0)

bounds = []
for d in range(1, 4):
    rank_upper = 9+d
    bound = Q(2)**rank_upper*Q(3, 2)**d
    assert bound == 512*3**d
    bounds.append({"anticanonical_square": -d,
                   "exceptional_rank_upper": rank_upper,
                   "compressed_mate_upper": int(bound)})

print(json.dumps({"status": "PASS", "quartic_bounds": bounds,
                  "cusp_cycle_matrix": A.tolist(),
                  "cusp_cycle_determinant": int(A.det()),
                  "opposite_vertex_correction": list(map(str, correction)),
                  "cycle_plus_six_A1_correction": str((v.T*full_correction)[0]),
                  "cycle_plus_six_A1_determinant": int(B.det()),
                  "compressed_mate_denominator": denominator},
                 indent=2, default=int))
