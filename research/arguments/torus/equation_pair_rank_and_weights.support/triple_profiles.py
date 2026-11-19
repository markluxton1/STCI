#!/usr/bin/env python3
"""Exact characteristic-zero torus refinements of the three O(-6) triples.

Reuses the retained complete-source substitution and Q(sqrt(-2)) arithmetic.
Checks the algebraic orbit weight tables, h/Theta kernel weight profiles,
endpoint coefficient relation and wedge blocks, plus the principal tangency
hyperplane. These are necessary contact data, not the length-nine condition.
"""

from fractions import Fraction
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "computations"))
import audit_sextic_triple_spaces_2026_10_31 as ast


def weight(mon):
    return sum(x * y for x, y in zip(mon, (-2, -1, 1, 2)))


def weighted_source(degree):
    columns, _, matrix = ast.source_matrix(degree, ast.orbit("algebraic"))
    blocks = {}
    for index, mon in enumerate(ast.monomials(degree)):
        blocks.setdefault(weight(mon), []).append(index)
    basis, profile = [], {}
    for w, indices in sorted(blocks.items()):
        _, kernel = ast.rref_kernel([[row[i] for i in indices] for row in matrix], len(indices))
        if kernel:
            profile[w] = len(kernel)
        for vector in kernel:
            full = [ast.ZERO] * len(columns)
            for i, coefficient in zip(indices, vector):
                full[i] = coefficient
            basis.append((w, full))
    _, full_kernel = ast.rref_kernel(matrix, len(columns))
    assert len(basis) == len(full_kernel)  # The homogeneous blocks cover the full source.
    return profile, basis


def combine(coefficients, polynomials):
    result = {}
    for c, p in zip(coefficients, polynomials):
        result = ast.padd(result, ast.scale(p, c))
    return result


def algebraic_checks():
    expected = {
        4: {-4: 1, 4: 1},
        5: {w: 1 for w in (-6, -5, -3, -2, -1, 0, 1, 2, 3, 5, 6)},
        6: dict(zip(range(-8, 9), (1, 1, 1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1))),
    }
    for degree, target in expected.items():
        profile, basis = weighted_source(degree)
        assert profile == target
        print(f"algebraic d={degree}: {profile}")
    data = ast.orbit("algebraic")
    _, _, _, _, _, h, theta = ast.contact_map(6, data, [v for _, v in basis])
    lam = (Fraction(28, 81), Fraction(16, 81))
    kernel_h, kernel_joint = {}, {}
    for w in expected[6]:
        indices = [i for i, (weight_i, _) in enumerate(basis) if weight_i == w]
        for i in indices:
            assert set(h[i]) <= {w + 8}
            assert set(theta[i]) <= {w + 3}
            for d in range(7, 12):
                assert theta[i].get(d, ast.ZERO) == ast.mul(lam, h[i].get(d + 5, ast.ZERO))
        hrank = int(any(h[i] for i in indices))
        pairs = [[h[i].get(w + 8, ast.ZERO), theta[i].get(w + 3, ast.ZERO)] for i in indices]
        jrank = ast.rank_columns(pairs)
        if len(indices) > hrank:
            kernel_h[w] = len(indices) - hrank
        if len(indices) > jrank:
            kernel_joint[w] = len(indices) - jrank
    assert kernel_h == dict(zip(range(-4, 5), (1, 1, 1, 1, 2, 1, 1, 1, 1)))
    assert kernel_joint == {-4: 1, 0: 1, 4: 1}
    blocks = {}
    for i, (wi, _) in enumerate(basis):
        for j, (wj, _) in enumerate(basis[i + 1:], i + 1):
            omega = ast.padd(ast.pmul(h[j], theta[i]), ast.scale(ast.pmul(h[i], theta[j]), ast.q(-1)))
            assert set(omega) <= {wi + wj + 11}
            blocks.setdefault(wi + wj, []).append(bool(omega))
    assert set(blocks) == set(range(-15, 16))
    assert {w for w, values in blocks.items() if any(values)} == set(range(-11, 12))
    print("algebraic ker(h), joint kernel, endpoint relation and 23 nonzero wedge blocks: passed")


def principal_hyperplane():
    data = ast.orbit("principal")
    columns, _, matrix = ast.source_matrix(6, data)
    _, basis = ast.rref_kernel(matrix, len(columns))
    _, _, _, _, _, h, theta = ast.contact_map(6, data, basis)
    hmatrix = [[p.get(d, ast.ZERO) for p in h] for d in range(17)]
    hrank, hkernel = ast.rref_kernel(hmatrix, len(basis))
    assert hrank == 17 and len(hkernel) == 10
    restricted = [combine(v, theta) for v in hkernel]
    for polynomial in restricted:
        assert set(polynomial) <= set(range(7))
        value = ast.ZERO
        for degree, coefficient in polynomial.items():
            value = ast.add(value, ast.mul(coefficient, ast.q(1, 2 ** degree)))
        assert value == ast.ZERO
    assert ast.rank_columns([[p.get(d, ast.ZERO) for d in range(7)] for p in restricted]) == 6
    print("principal Theta(ker h)={p of degree <=6 : p(1/2)=0}, rank 6: passed")


if __name__ == "__main__":
    algebraic_checks()
    principal_hyperplane()
