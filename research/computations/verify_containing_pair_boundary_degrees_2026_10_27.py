#!/usr/bin/env python3
"""Exact higher-degree attachment-map differentials for the fixed quartic.

All columns come from differences of actual homogeneous monomials of the
same restriction weight. The selected pair is
  x0^(a-4)*(x1^4-x0^3*x3), x3^(b-4)*(x2^4-x0*x3^3).
This verifies only the stated finite coordinate calculations. The all-degree
proof and geometric scope are in the companion research note.
Standard library only; no inherited (4,4) verifier is replayed.
"""

import json
from math import comb


def monomials(degree):
    for e0 in range(degree + 1):
        for e1 in range(degree - e0 + 1):
            for e2 in range(degree - e0 - e1 + 1):
                yield (e0, e1, e2, degree - e0 - e1 - e2)


def basis(degree):
    groups = {}
    for exponents in monomials(degree):
        weight = exponents[1] + 3 * exponents[2] + 4 * exponents[3]
        groups.setdefault(weight, []).append(exponents)
    assert set(groups) == set(range(4 * degree + 1))
    columns = [
        (weight, m, block[0])
        for weight, block in sorted(groups.items())
        for m in block[1:]
    ]
    assert len(columns) == comb(degree + 3, 3) - (4 * degree + 1)
    return columns


def interval(values):
    result = sorted(values)
    assert result == list(range(result[0], result[-1] + 1))
    return [result[0], result[-1]]


def calculation(a, b):
    # A monomial difference of weight w has symbol
    # (delta(e3)*u^(w-4), delta(e2)*u^(w-3)).
    # At the displayed pair every derivative column has one monomial.
    left = {}
    for weight, m, reference in basis(a):
        coefficient = 4 * (m[3] - reference[3]) + 3 * (m[2] - reference[2])
        if coefficient:
            exponent = weight + 4 * b - 11
            left.setdefault(exponent, [coefficient, m, reference])
    right = {}
    for weight, m, reference in basis(b):
        coefficient = -(m[2] - reference[2])
        if coefficient:
            right.setdefault(weight - 3, [coefficient, m, reference])
    target_degree = 4 * (a + b) - 14
    assert set(left) | set(right) == set(range(target_degree + 1))
    assert interval(left) == [4 * b - 8, target_degree]
    assert interval(right) == [0, 4 * b - 6]
    expected_genus_twice = (a + b - 4) * (a * b - 8)
    assert expected_genus_twice % 2 == 0
    result = {
        "degrees": [a, b],
        "source_dimensions": [len(basis(a)), len(basis(b))],
        "vary_first_support": interval(left),
        "vary_second_support": interval(right),
        "affine_differential_rank": target_degree + 1,
        "projective_boundary_dimension": target_degree,
        "general_residual_degree": a * b - 4,
        "general_residual_genus": expected_genus_twice // 2,
        "general_attachment_length": target_degree,
        "residual_Rao_degree": a + b - 5,
    }
    if a == b:
        pencil_dimension = 2 * (len(basis(a)) - 2)
        result["pencil_dimension"] = pencil_dimension
        result["generic_boundary_fiber_dimension"] = pencil_dimension - target_degree
    return result


if __name__ == "__main__":
    pairs = [(4, 5), (5, 4)] + [(a, b) for a in range(5, 10) for b in range(5, 10)]
    data = [calculation(a, b) for a, b in pairs]
    print(json.dumps({"scope": "27 new higher/mixed-degree coordinate checks over Q", "results": data}, indent=2))
