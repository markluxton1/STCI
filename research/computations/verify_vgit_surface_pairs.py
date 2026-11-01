#!/usr/bin/env python3
"""Exact finite certificates for VGIT of surface pencils and full limits.

Run from any directory with Python's standard library. This checks restriction
weights, ambient exterior-square weights, and degreewise ideal state extrema
for one actual residual CI. It compares those with its existing equivariant
Hilbert--Burch resolution. It does not classify graph fibers, prove flatness
or saturation, compute a full opposite initial ideal, or decide sole support.
The geometric proofs and scope are in
../synthesis/vgit_surface_pairs_and_full_limits.md.
"""

from collections import Counter
from fractions import Fraction
from math import comb

from verify_toric_quotients_and_residual_limits import add, mul, power, scale


WEIGHTS = (-2, -1, 1, 2)


def monomials(degree):
    if degree < 0:
        return []
    return [(i, j, k, degree - i - j - k)
            for i in range(degree + 1)
            for j in range(degree - i + 1)
            for k in range(degree - i - j + 1)]


def weight(exponent):
    return sum(a * b for a, b in zip(exponent, WEIGHTS))


def dim_s(degree):
    return comb(degree + 3, 3) if degree >= 0 else 0


def shift(polynomial, exponent):
    return {tuple(a + b for a, b in zip(term, exponent)): coefficient
            for term, coefficient in polynomial.items()}


def extreme_state(rows, maximum=False):
    """Rank and extreme Plucker weight of a polynomial row span over Q.

    Greedy pivot columns in weight order give a minimum/maximum-weight basis
    of the column matroid. Its nonzero maximal minor is a Plucker coordinate.
    Ties can be broken arbitrarily without changing the extremal weight.
    Sparse rational elimination retains dependencies, including the Koszul
    relation in degrees >= 12; merely summing generator weights would not.
    """
    columns = sorted({e for row in rows for e in row},
                     key=lambda e: (weight(e), e), reverse=maximum)
    order = {e: i for i, e in enumerate(columns)}
    basis = {}
    for source in rows:
        row = {order[e]: Fraction(c) for e, c in source.items() if c}
        while row:
            pivot = min(row)
            value = row[pivot]
            if pivot not in basis:
                basis[pivot] = {j: c / value for j, c in row.items()}
                break
            for j, coefficient in basis[pivot].items():
                updated = row.get(j, 0) - value * coefficient
                if updated:
                    row[j] = updated
                else:
                    row.pop(j, None)
    return len(basis), sum(weight(columns[j]) for j in basis)


def representation_checks():
    ambient = Counter(weight(e) for e in monomials(6))
    assert sum(ambient.values()) == 84
    assert set(ambient) == set(range(-12, 13))
    # Restriction sends every monomial in a weight block to the same nonzero
    # binary monomial, so its kernel is the coefficient-sum-zero hyperplane.
    equation = {w: count - 1 for w, count in ambient.items() if count > 1}
    expected = [1, 2, 2, 3, 3, 4, 4, 4, 4, 5,
                4, 4, 4, 4, 3, 3, 2, 2, 1]
    assert [equation[w] for w in range(-9, 10)] == expected
    assert sum(equation.values()) == 59
    exterior = Counter()
    for w, dimension in equation.items():
        exterior[2 * w] += dimension * (dimension - 1) // 2
        for v, other_dimension in equation.items():
            if v > w:
                exterior[w + v] += dimension * other_dimension
    exterior = +exterior  # Discard zero-multiplicity weights.
    assert set(exterior) == set(range(-17, 18))
    assert sum(exterior.values()) == comb(59, 2) == 1711
    assert exterior[-17] == exterior[17] == 2
    assert 35 * 36 // 2 == 630
    print("V6: dimension 59; centered weights -9..9; profile", expected)
    print("exterior square: dimension 1711; weights -17..17; <=630 blocks")


def residual_control():
    x0, x1, x2, x3 = (
        {tuple(int(i == j) for i in range(4)): 1} for j in range(4))
    q = add(mul(x0, x3), scale(-1, mul(x1, x2)))
    cubic = add(mul(power(x0, 2), x2), scale(-1, power(x1, 3)))
    a6 = mul(mul(power(x0, 2), x3), cubic)
    b4 = mul(power(x0, 3), x2)
    f = add(power(q, 3), a6)
    g = mul(b4, q)
    full_negative = [power(q, 3), g, mul(a6, b4)]
    # Generator and syzygy characters in the written Hilbert--Burch proof.
    assert [{weight(e) for e in p} for p in full_negative] == [{0}, {-5}, {-10}]
    assert mul(b4, full_negative[0]) == mul(power(q, 2), full_negative[1])
    assert mul(a6, full_negative[1]) == mul(q, full_negative[2])
    assert {weight(e) for e in mul(b4, full_negative[0])} == {-5}
    assert {weight(e) for e in mul(a6, full_negative[1])} == {-10}

    expected = {6: (2, -10, -5), 10: (70, -345, -180),
                12: (167, -780, -460), 13: (236, -1065, -660)}
    print("control: n, ideal dimension, minimum state, maximum state")
    for n, values in expected.items():
        rows = [shift(generator, e) for generator in (f, g)
                for e in monomials(n - 6)]
        rank_min, lower = extreme_state(rows)
        rank_max, upper = extreme_state(rows, maximum=True)
        ci_dimension = 2 * dim_s(n - 6) - dim_s(n - 12)
        assert rank_min == rank_max == ci_dimension
        assert (rank_min, lower, upper) == values
        # Independent span calculation on the full negative limit, without
        # assuming that its displayed resolution is exact in the computation.
        limit_rows = [shift(generator, e) for generator, degree in
                      zip(full_negative, (6, 6, 10))
                      for e in monomials(n - degree)]
        limit_rank, limit_character = extreme_state(limit_rows)
        limit_rank_max, limit_character_max = extreme_state(limit_rows, maximum=True)
        character = (-5 * dim_s(n - 6) - 5 * dim_s(n - 10)
                     + 10 * dim_s(n - 12))
        assert limit_rank == limit_rank_max == ci_dimension
        assert limit_character == limit_character_max == upper == character
        print(n, rank_min, lower, upper)
    pair_extension = -5 * (dim_s(6) - dim_s(0))
    actual = -5 * dim_s(6) - 5 * dim_s(2) + 10 * dim_s(0)
    assert (actual, pair_extension, actual - pair_extension) == (-460, -415, -45)
    print("n=12: full-limit character -460; pair extension -415; correction -45")
    return x0, q, cubic, a6, b4


def same_block_family(x0, q, cubic, a6, b4):
    correction = mul(mul(q, x0), cubic)
    g = mul(b4, q)
    # A polynomial identity, not just equality of endpoint Hilbert series:
    # the additional full-limit generator changes by a multiple of b4*q.
    assert mul(correction, b4) == mul(mul(x0, cubic), g)
    a1 = add(a6, correction)
    assert {weight(e) for e in a1} == {-5}
    f1 = add(power(q, 3), a1)
    pencil_rows = [f1, g]
    assert extreme_state(pencil_rows) == (2, -10)
    assert extreme_state(pencil_rows, maximum=True) == (2, -5)
    rows = [shift(generator, e) for generator in (f1, g)
            for e in monomials(6)]
    assert extreme_state(rows) == (167, -810)
    assert extreme_state(rows, maximum=True) == (167, -460)
    print("same pair block, same negative full ideal: tau=1 degree-12 state [-810,-460]")
    print("tau=0 degree-12 state [-780,-460]; no all-parameter rank extrapolation")


def main():
    representation_checks()
    control = residual_control()
    same_block_family(*control)
    print("Exact finite checks passed; supported graph incidence remains open.")


if __name__ == "__main__":
    main()
