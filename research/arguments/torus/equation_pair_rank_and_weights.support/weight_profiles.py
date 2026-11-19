#!/usr/bin/env python3
"""Finite support for equation_pair_rank_and_weights.md; standard library only.

Checks the displayed C0 weight tables and quotient fibers. Independent first-jet
matrices over Q, F2 and F3 check the order-two character in degrees 5..8.
Monomial boundary ideals check the rank formula in a bounded unequal-degree set.
The written flag and syzygy proofs, not these cases, supply all-degree coverage.
"""

from collections import Counter
from fractions import Fraction
from math import comb


def monomials(d):
    if d < 0:
        return []
    return [(i, j, k, d - i - j - k)
            for i in range(d + 1)
            for j in range(d - i + 1)
            for k in range(d - i - j + 1)]


def weight(mon):
    return sum(a * b for a, b in zip(mon, (-2, -1, 1, 2)))


def ambient(d):
    return Counter(weight(mon) for mon in monomials(d))


def containing(d):
    assert d >= 2
    return +Counter({w: c - 1 for w, c in ambient(d).items()})


def double(d):
    assert d >= 5
    return +Counter({w: c - 3 for w, c in ambient(d).items()})


def exterior(profile):
    basis_weights = list(profile.elements())
    return Counter(a + b for i, a in enumerate(basis_weights)
                   for b in basis_weights[i + 1:])


def rank(rows, prime=None):
    """Exact elimination over Q or a prime field; input is a small integer matrix."""
    a = [[x % prime if prime else Fraction(x) for x in row] for row in rows]
    pivot = 0
    for j in range(len(a[0])):
        found = next((i for i in range(pivot, len(a)) if a[i][j]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        inverse = pow(a[pivot][j], -1, prime) if prime else 1 / a[pivot][j]
        a[pivot] = [(x * inverse) % prime if prime else x * inverse for x in a[pivot]]
        for i in range(pivot + 1, len(a)):
            coefficient = a[i][j]
            a[i] = [((x - coefficient * y) % prime if prime else x - coefficient * y)
                    for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def check_first_jets():
    # x0=1, x1=z, x2=z^3+y, x3=z^4+m. In one weight block,
    # the constant/y/m coefficients are 1,k,l times fixed powers of z.
    for d in range(5, 9):
        blocks = {}
        for mon in monomials(d):
            blocks.setdefault(weight(mon), []).append(mon)
        for prime in (None, 2, 3):
            actual = Counter()
            for w, mons in blocks.items():
                matrix = [[1 for _ in mons], [m[2] for m in mons], [m[3] for m in mons]]
                actual[w] = len(mons) - rank(matrix, prime)
            assert +actual == double(d), (d, prime, actual)


def check_profiles_and_bundles():
    expected = {
        2: (0, [1]),
        3: (-3, [1] * 7),
        4: (-5, [1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1]),
        5: (-7, [1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]),
    }
    for d, (start, counts) in expected.items():
        assert containing(d) == Counter(dict(zip(range(start, start + len(counts)), counts)))
    profile = [1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1]
    assert double(6) == Counter(dict(zip(range(-6, 7), profile)))
    for space, low, high, dimension in (
            (ambient(4), -15, 15, 35),
            (containing(6), -17, 17, 59),
            (double(6), -11, 11, 23),
            (containing(8), -25, 25, 132),
            (double(8), -19, 19, 80)):
        ext = exterior(space)
        assert sum(space.values()) == dimension
        assert set(ext) == set(range(low, high + 1))
        assert sum(ext.values()) == comb(dimension, 2)
    assert 23 * 24 // 2 == 276
    for a, b, fiber_rank, total_dim in ((5, 8, 112, 145), (6, 16, 618, 675)):
        va, vb, multipliers = containing(a), containing(b), ambient(b - a)
        assert sum(vb.values()) - sum(multipliers.values()) == fiber_rank
        assert sum(va.values()) - 1 + fiber_rank - 1 == total_dim
        for wa in va:
            shifted = {w + wa: c for w, c in multipliers.items()}
            fiber = {w: vb[w] - shifted.get(w, 0) for w in set(vb) | set(shifted)}
            assert min(fiber.values()) >= 0
            assert sum(fiber.values()) == fiber_rank


def check_rank_drop():
    def dim_s(n):
        return comb(n + 3, 3) if n >= 0 else 0

    for a, b in ((6, 6), (5, 8), (6, 16)):
        for e in range(1, a):
            f, g = (e, a - e, 0, 0), (e, 0, b - e, 0)
            for n in range(a, a + b + 2):
                image = {tuple(x + y for x, y in zip(generator, multiplier))
                         for generator, degree in ((f, a), (g, b))
                         for multiplier in monomials(n - degree)}
                assert len(image) == dim_s(n - a) + dim_s(n - b) - dim_s(n - a - b + e)


if __name__ == "__main__":
    check_profiles_and_bundles()
    check_first_jets()
    check_rank_drop()
    print("C0 source/fiber/exterior characters; Q,F2,F3 first jets d=5..8; bounded rank drops: passed.")
