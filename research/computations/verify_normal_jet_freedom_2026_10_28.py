#!/usr/bin/env python3
"""Exact new normal-layer checks for C0; no inherited certificate is replayed.

On x0=1 substitute x1=u, x2=u^3+Y, x3=u^4+X.  Taylor
coefficients of normal order <=r split into blocks by the original u-weight.
Ranks use Fraction arithmetic over Q.  A kernel of the coefficients of
order <r is H^0(I_C^r(d)): the lci normal layers have no punctual torsion.
The image in order r therefore has dimension rank(T_<=r)-rank(T_<r).
These finite checks corroborate, but do not replace, the all-order proof.
"""

from fractions import Fraction
from math import comb
from pathlib import Path
import json


def rank(rows):
    if not rows:
        return 0
    matrix = [[Fraction(x) for x in row] for row in rows]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((j for j in range(pivot_row, len(matrix))
                      if matrix[j][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        leading = matrix[pivot_row][column]
        matrix[pivot_row] = [x / leading for x in matrix[pivot_row]]
        for j in range(pivot_row + 1, len(matrix)):
            factor = matrix[j][column]
            if factor:
                matrix[j] = [x - factor * y for x, y in
                             zip(matrix[j], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def taylor_rank(degree, order):
    if order < 0:
        return 0
    blocks = {}
    for i0 in range(degree + 1):
        for i1 in range(degree - i0 + 1):
            for i2 in range(degree - i0 - i1 + 1):
                i3 = degree - i0 - i1 - i2
                weight = i1 + 3 * i2 + 4 * i3
                blocks.setdefault(weight, []).append((i2, i3))
    total = 0
    for weight, columns in blocks.items():
        rows = []
        for x_order in range(order + 1):
            for y_order in range(order - x_order + 1):
                if weight < 4 * x_order + 3 * y_order:
                    continue
                rows.append([
                    comb(i3, x_order) * comb(i2, y_order)
                    if i3 >= x_order and i2 >= y_order else 0
                    for i2, i3 in columns
                ])
        total += rank(rows)
    return total


def run():
    checks = []
    for normal_order in range(1, 6):
        for offset in (1, 2, 3):
            degree = 3 * normal_order + offset
            previous = taylor_rank(degree, normal_order - 1)
            current = taylor_rank(degree, normal_order)
            target = (normal_order + 1) * (4 * degree - 7 * normal_order + 1)
            expected_cokernel = 2 * normal_order + 1 if offset == 1 else 0
            check = {
                "normal_order": normal_order,
                "ambient_degree": degree,
                "source_h0_I_power": comb(degree + 3, 3) - previous,
                "kernel_h0_next_power": comb(degree + 3, 3) - current,
                "image_rank": current - previous,
                "target_dimension": target,
                "cokernel_dimension": target - current + previous,
                "expected_cokernel_dimension": expected_cokernel,
            }
            assert check["cokernel_dimension"] == expected_cokernel, check
            checks.append(check)
    output = {
        "field": "Q",
        "method": "exact Taylor matrices with Fraction Gaussian elimination",
        "scope": "15 finite normal-layer checks; theorem proved separately",
        "checks": checks,
        "passed": len(checks),
    }
    destination = Path(__file__).with_name("normal_jet_freedom_2026_10_28.json")
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(f"PASS: {len(checks)} exact normal-layer ranks; {destination.name}")


if __name__ == "__main__":
    run()
