#!/usr/bin/env python3
"""Independent literal-minor audit of the smooth twisted-cubic equation space.

The derivative matrix is rebuilt by actual symbolic differentiation and
substitution, rather than importing the coefficient formula or any prior
matrix. Rank/determinant calculations use Fraction elimination. This
checks the finite equation-space step, not the geometric normalization
or the arbitrary-mate-degree theorem.
"""

from fractions import Fraction
import json
from pathlib import Path
import sympy as sp


def rank(matrix):
    a = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        lead = a[pivot_row][column]
        for i in range(pivot_row + 1, len(a)):
            ratio = a[i][column] / lead
            for j in range(column, len(a[0])):
                a[i][j] -= ratio * a[pivot_row][j]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def determinant(matrix):
    a = [[Fraction(value) for value in row] for row in matrix]
    answer = Fraction(1)
    for column in range(len(a)):
        pivot = next((i for i in range(column, len(a)) if a[i][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            a[column], a[pivot] = a[pivot], a[column]
            answer = -answer
        lead = a[column][column]
        answer *= lead
        for i in range(column + 1, len(a)):
            ratio = a[i][column] / lead
            for j in range(column, len(a)):
                a[i][j] -= ratio * a[column][j]
    return answer


x = sp.symbols("x0:4")
s, t = sp.symbols("s t")
exponents = [
    (a, b, c, 4 - a - b - c)
    for a in range(5)
    for b in range(5 - a)
    for c in range(5 - a - b)
]
forms = [sp.prod(x[i] ** e[i] for i in range(4)) for e in exponents]
substitution = dict(zip(x, (s**3, s**2 * t, s * t**2, t**3)))
matrix = []
for variable in x:
    restrictions = [sp.Poly(sp.diff(form, variable).subs(substitution), s, t) for form in forms]
    for degree in range(10):
        matrix.append([poly.coeff_monomial(s**degree * t ** (9 - degree)) for poly in restrictions])

rows = list(range(19)) + list(range(20, 29)) + [30]
columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18,
           21, 22, 23, 24, 28, 29, 30, 31, 32, 33, 34]
minor = [[matrix[i][j] for j in columns] for i in rows]
literal_determinant = determinant(minor)
assert literal_determinant == 104509440

q1 = x[0] * x[2] - x[1] ** 2
q2 = x[0] * x[3] - x[1] * x[2]
q3 = x[1] * x[3] - x[2] ** 2
quadrics = (q1, q2, q3)
products = [sp.Poly(quadrics[i] * quadrics[j], *x) for i in range(3) for j in range(i, 3)]
coefficients = [[form.coeff_monomial(e) for form in products] for e in exponents]
assert rank(coefficients) == 6
for row in matrix:
    for j in range(6):
        assert sum(row[i] * coefficients[i][j] for i in range(35)) == 0
assert rank(matrix) == 29
assert sp.expand(x[2] * q1 - x[1] * q2 + x[0] * q3) == 0
assert sp.expand(x[3] * q1 - x[2] * q2 + x[1] * q3) == 0
for form in forms:
    assert sp.expand(sum(x[i] * sp.diff(form, x[i]) for i in range(4)) - 4 * form) == 0

report = {
    "status": "PASS",
    "scope": "Quartics singular along the standard smooth twisted cubic only; geometry proved separately",
    "matrix_shape": [40, 35],
    "matrix_rank": 29,
    "kernel_dimension": 6,
    "six_product_rank": 6,
    "literal_minor_rows_zero_based": rows,
    "literal_minor_columns_zero_based": columns,
    "literal_minor_determinant": int(literal_determinant),
    "derivatives_rebuilt_by_symbolic_substitution": True,
    "rank_and_determinant_arithmetic": "Fraction Gaussian elimination",
    "syzygies_and_euler_identity": "PASS",
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
