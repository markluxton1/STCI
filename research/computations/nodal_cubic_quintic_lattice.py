#!/usr/bin/env python3
"""Finite E6 check used in ARTIFACT-20260821-019 (standard library only).

For a degree-three weak del Pezzo resolution with one A1 root alpha, enumerate
all numerical classes D having H.D=5, D^2=3, D.alpha=0, and nonnegative
intersection with the 15 simple lines (the -1 curves orthogonal to alpha).
The Cauchy bound restricts the leading coefficient to 2,...,8.  The script
verifies that every such class has exactly three simple lines disjoint from it.
"""
from itertools import product

def dot(x, y):
    return x[0] * y[0] - sum(a * b for a, b in zip(x[1:], y[1:]))

H = (3, 1, 1, 1, 1, 1, 1)
alpha = (0, -1, 1, 0, 0, 0, 0)  # a representative E6 root
lines = []
for i in range(6):
    b = [0] * 6
    b[i] = -1
    lines.append(("E" + str(i + 1), (0, *b)))
for i in range(6):
    for j in range(i + 1, 6):
        b = [0] * 6
        b[i] = b[j] = 1
        lines.append(("L%d%d" % (i + 1, j + 1), (1, *b)))
for i in range(6):
    b = [1] * 6
    b[i] = 0
    lines.append(("Q" + str(i + 1), (2, *b)))

simple = [(name, line) for name, line in lines if dot(alpha, line) == 0]
assert len(simple) == 15
classes = []
for a in range(2, 9):  # Cauchy: (3a-5)^2 <= 6(a^2-3)
    target_sum, target_square = 3 * a - 5, a * a - 3
    bound = int(target_square ** 0.5)
    for b in product(range(-bound, bound + 1), repeat=6):
        if sum(b) != target_sum or sum(x * x for x in b) != target_square:
            continue
        D = (a, *b)
        if dot(D, alpha) != 0 or any(dot(D, line) < 0 for _, line in simple):
            continue
        classes.append(D)

assert len(classes) == 120
zero_counts = [sum(dot(D, line) == 0 for _, line in simple) for D in classes]
assert set(zero_counts) == {3}
print("simple lines:", len(simple))
print("admissible quintic classes:", len(classes))
print("disjoint simple-line count:", sorted(set(zero_counts)))
