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


def boundary_and_double_surface_checks():
    """Verify Section 7 (authored by Gemini): V_e profiles, V_{d,2} sequence, Gr(2,V_{6,2}), and rank-drop law."""
    expected_ve = {
        2: (1, 0, 0, [1]),
        3: (7, -3, 3, [1, 1, 1, 1, 1, 1, 1]),
        4: (18, -5, 5, [1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1]),
        5: (35, -7, 7, [1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]),
        6: (59, -9, 9, [1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 4, 4, 4, 4, 3, 3, 2, 2, 1]),
    }
    for e, (dim_exp, wmin, wmax, prof_exp) in expected_ve.items():
        ambient = Counter(weight(m) for m in monomials(e))
        ve = {w: c - 1 for w, c in ambient.items() if c > 1}
        assert sum(ve.values()) == dim_exp
        assert min(ve) == wmin and max(ve) == wmax
        assert [ve[w] for w in range(wmin, wmax + 1)] == prof_exp

    # Check intrinsic quadric-restriction dimension and weight formula for V_{d,2} (d=4..8)
    expected_vd2_dims = {4: 1, 5: 7, 6: 23, 7: 47, 8: 80}
    for d, dim_exp in expected_vd2_dims.items():
        ambient_d2 = Counter(weight(m) for m in monomials(d - 2))
        vd_minus_2 = sum(c - 1 for c in ambient_d2.values() if c > 1)
        h0_oq = (d - 1) * max(0, d - 5)
        assert vd_minus_2 + h0_oq == dim_exp
        if d >= 5:
            ambient_d = Counter(weight(m) for m in monomials(d))
            vd2_w = {w: c - 3 for w, c in ambient_d.items() if c > 3}
            assert sum(vd2_w.values()) == dim_exp

    # Detailed check of V_{6,2} and wedge^2 V_{6,2}
    ambient_6 = Counter(weight(m) for m in monomials(6))
    v62 = {w: c - 3 for w, c in ambient_6.items() if c > 3}
    expected_v62 = [1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1]
    assert [v62[w] for w in range(-6, 7)] == expected_v62
    assert sum(v62.values()) == 23
    ext_v62 = Counter()
    for w, d1 in v62.items():
        ext_v62[2 * w] += d1 * (d1 - 1) // 2
        for v, d2 in v62.items():
            if v > w:
                ext_v62[w + v] += d1 * d2
    ext_v62 = +ext_v62
    assert set(ext_v62) == set(range(-11, 12))
    assert sum(ext_v62.values()) == comb(23, 2) == 253

    # Verify universal common-factor rank-drop formula dim(W_0)_n = 2*N_{n-6} - N_{n-12+e}
    # on concrete boundary pencils W_0 = x_0^e * <x_1^{6-e}, x_2^{6-e}> for e = 1..5 and n = 6..13
    x0, x1, x2, _ = ({tuple(int(i == j) for i in range(4)): 1} for j in range(4))
    for e in range(1, 6):
        de = power(x0, e)
        f0 = mul(de, power(x1, 6 - e))
        g0 = mul(de, power(x2, 6 - e))
        for n in range(6, 14):
            rows = [shift(gen, m) for gen in (f0, g0) for m in monomials(n - 6)]
            rk, _ = extreme_state(rows)
            expected_rk = 2 * dim_s(n - 6) - dim_s(n - 12 + e)
            ci_rk = 2 * dim_s(n - 6) - dim_s(n - 12)
            assert rk == expected_rk
            assert ci_rk - rk == dim_s(n - 12 + e) - dim_s(n - 12)
    print("V_{6,2}: dimension 23; centered weights -6..6; profile", expected_v62)
    print("wedge^2 V_{6,2}: dimension 253; weights -11..11; 22 chambers; <=276 blocks")
    print("common-factor rank-drop formula verified for e=1..5 and n=6..13")


def main():
    representation_checks()
    control = residual_control()
    same_block_family(*control)
    boundary_and_double_surface_checks()
    print("Exact finite checks passed; supported graph incidence remains open.")


if __name__ == "__main__":
    main()
