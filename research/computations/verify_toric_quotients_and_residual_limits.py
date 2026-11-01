#!/usr/bin/env python3
"""Verify finite algebra and explicit polynomial certificates used in the toric quotient and residual-limit notes.

This checks only the displayed finite computations and identities. It is not a
general classification, a Groebner-basis exhaustion, or a proof of any geometric
descent, flatness, or primary-decomposition assertion. Geometric arguments are
in ../synthesis/toric_quotients_and_endpoint_descent.md and
../synthesis/toric_sextic_residuals_and_limits.md.
"""

from fractions import Fraction
from math import comb


def rank(rows, mod=None):
    """Exact row rank over Q or F_mod."""
    a = [list(map(Fraction, row)) if mod is None else [x % mod for x in row]
         for row in rows]
    if not a:
        return 0
    nr, nc, r = len(a), len(a[0]), 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = 1 / a[r][c] if mod is None else pow(a[r][c], -1, mod)
        a[r] = [v * inv if mod is None else v * inv % mod for v in a[r]]
        for i in range(nr):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [u - q * v if mod is None else (u - q * v) % mod
                        for u, v in zip(a[i], a[r])]
        r += 1
        if r == nr:
            break
    return r


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def add(f, g):
    h = dict(f)
    for e, c in g.items():
        h[e] = h.get(e, 0) + c
        if not h[e]:
            del h[e]
    return h


def scale(c, f):
    return {e: c * v for e, v in f.items() if c * v}


def mul(f, g):
    h = {}
    for e, a in f.items():
        for d, b in g.items():
            k = tuple(x + y for x, y in zip(e, d))
            h[k] = h.get(k, 0) + a * b
    return {e: c for e, c in h.items() if c}


def power(f, n):
    one = {(0,) * len(next(iter(f))): 1}
    while n:
        if n & 1:
            one = mul(one, f)
        f = mul(f, f)
        n //= 2
    return one


def assert_zero(f):
    assert not f, f


def quotient_checks():
    a, b = [0, -3, 6, -10], [0, -4, 10, -20]
    expected = {None: 13, 2: 18, 3: 15, 5: 13, 7: 13, 11: 13}
    for p, delta in expected.items():
        total = 0
        for n in range(13):
            cols = []
            for i in range(n // 3 + 1):
                for j in range(n // 4 + 1):
                    if 3 * i + 4 * j <= n:
                        v = [1, 0, 0, 0]
                        for _ in range(i):
                            v = [sum(v[k] * a[d - k] for k in range(d + 1))
                                 for d in range(4)]
                        for _ in range(j):
                            v = [sum(v[k] * b[d - k] for k in range(d + 1))
                                 for d in range(4)]
                        cols.append(v)
            total += 4 - rank(list(map(list, zip(*cols))), p)
        assert total == delta, (p, total)
    e_delta = sum(4 - min(4, n // 3 + 1) for n in range(13))
    assert e_delta == 18
    assert det3([[a[1], b[1], 0], [a[2], b[2], a[1] ** 2],
                 [a[3], b[3], 2 * a[1] * a[2]]]) == 36
    # b=(4/3)a+(2/9)a^2-(4/81)a^3 in Q[e]/(e^4).
    aa = [Fraction(0), Fraction(-3), Fraction(6), Fraction(-10)]
    bb = [Fraction(0), Fraction(-4), Fraction(10), Fraction(-20)]
    prod = [Fraction(0)] * 4
    cur = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    for c in (Fraction(4, 3), Fraction(2, 9), Fraction(-4, 81)):
        cur = [sum(cur[k] * aa[d - k] for k in range(d + 1)) for d in range(4)]
        prod = [x + c * y for x, y in zip(prod, cur)]
    assert prod == bb
    rows = [[Fraction(1), Fraction(1, u ** 3), Fraction(1, u ** 4),
             Fraction(1, u ** 6)] for u in (1, 2, 3, 4)]
    assert det4(rows) == Fraction(1505, 7962624)


def det4(m):
    if len(m) == 1:
        return m[0][0]
    return sum((-1) ** j * m[0][j] * det4(
        [row[:j] + row[j + 1:] for row in m[1:]]) for j in range(len(m[0])))


def jet_checks():
    profile = [1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1]
    primes = (None, 2, 3, 5, 7)
    by_weight = {w: [] for w in range(25)}
    for k in range(7):
        for l in range(7 - k):
            for j in range(7 - k - l):
                e0 = 6 - k - l - j
                if e0 >= 0:
                    by_weight[j + 3 * k + 4 * l].append((1, k, l))
    assert sum(map(len, by_weight.values())) == comb(9, 3) == 84
    for p in primes:
        dims = {}
        for w in range(25):
            columns = by_weight[w]
            # Three jet rows, columns are (1,k,l).
            mat = [[c[r] for c in columns] for r in range(3)]
            dims[w] = len(columns) - rank(mat, p)
        assert [dims[w] for w in range(6, 19)] == profile, (p, dims)
        assert all(dims[w] == 0 for w in range(25) if not 6 <= w <= 18)
        assert sum(dims.values()) == 23
    assert sum(profile) == 23
    assert sum(bool(v) for v in by_weight.values()) == 25
    assert 84 - 25 == 59
    for degree, source_dimension, grassmannian_dimension in ((4, 18, 32), (6, 59, 114)):
        weights = {
            j + 3 * k + 4 * l
            for k in range(degree + 1)
            for l in range(degree - k + 1)
            for j in range(degree - k - l + 1)
        }
        assert weights == set(range(4 * degree + 1))
        assert comb(degree + 3, 3) - len(weights) == source_dimension
        assert 2 * (source_dimension - 2) == grassmannian_dimension
    assert 2 * (23 - 2) == 42 and 114 - 42 == 72


def residual_checks():
    # First verify the identity in independent ambient variables x0,...,x3.
    x = [{tuple(int(i == j) for i in range(4)): 1} for j in range(4)]
    x0, x1, x2, x3 = x
    qx = add(mul(x0, x3), scale(-1, mul(x1, x2)))
    Ax = add(mul(power(x0, 2), x2), scale(-1, power(x1, 3)))
    Bx = add(mul(x0, power(x2, 2)), scale(-1, mul(power(x1, 2), x3)))
    assert_zero(add(add(mul(mul(power(x0, 2), x1), Bx),
                         scale(-1, mul(mul(power(x0, 2), x3), Ax))),
                    mul(mul(power(x0, 3), x2), qx)))

    # Now substitute the Segre parametrization x=(ac,ad,bc,bd), so
    # q=0, A=a^2 D, B3=abD, rlo=a^3cD, rhi=b^3dD, D=bc^3-ad^3.
    a, b, c, d = ({tuple(int(i == j) for i in range(4)): 1}
                  for j in range(4))
    q = add(mul(mul(a, c), mul(b, d)),
            scale(-1, mul(mul(a, d), mul(b, c))))
    D = add(mul(b, power(c, 3)), scale(-1, mul(a, power(d, 3))))
    A, B3 = mul(power(a, 2), D), mul(mul(a, b), D)
    rlo, rhi = mul(mul(power(a, 3), c), D), mul(mul(power(b, 3), d), D)
    x0, x1, x2, x3 = mul(a, c), mul(a, d), mul(b, c), mul(b, d)
    assert not q
    assert A == add(mul(power(x0, 2), x2), scale(-1, power(x1, 3)))
    assert B3 == add(mul(x0, power(x2, 2)),
                     scale(-1, mul(power(x1, 2), x3)))
    assert rlo == add(mul(power(x0, 3), x2),
                      scale(-1, mul(x0, power(x1, 3))))
    assert rhi == add(mul(power(x2, 3), x3),
                      scale(-1, mul(x1, power(x3, 3))))
    a6_segre = mul(mul(power(x0, 2), x3), A)
    b4_segre = mul(power(x0, 3), x2)
    assert a6_segre == mul(mul(mul(mul(power(a, 4), b), power(c, 2)), d), D)
    assert b4_segre == mul(mul(power(a, 3), b), power(c, 4))
    split_section = mul(power(add(x0, x3), 2), add(rlo, rhi))
    assert split_section == mul(
        mul(power(add(mul(a, c), mul(b, d)), 2), D),
        add(mul(power(a, 3), c), mul(power(b, 3), d)))
    absorbed = mul(A, add(A, power(x0, 3)))
    assert absorbed == mul(
        mul(power(a, 4), D), add(D, mul(a, power(c, 3))))
    assert_zero(add(mul(mul(power(x0, 2), x1), B3),
                    scale(-1, mul(mul(power(x0, 2), x3), A))))
    # Check the Hilbert--Burch minors with the actual ambient polynomials;
    # the fifth independent variable is the degeneration parameter h.
    x0, x1, x2, x3, h = (
        {tuple(int(i == j) for i in range(5)): 1} for j in range(5))
    qvar = add(mul(x0, x3), scale(-1, mul(x1, x2)))
    ambient_A = add(mul(power(x0, 2), x2), scale(-1, power(x1, 3)))
    a6 = mul(mul(power(x0, 2), x3), ambient_A)
    b4 = mul(power(x0, 3), x2)
    f = add(power(qvar, 3), mul(power(h, 5), a6))
    matrix = [
        [b4, {}],
        [scale(-1, power(qvar, 2)), a6],
        [scale(-1, power(h, 5)), scale(-1, qvar)],
    ]
    minors = []
    for i, j in ((1, 2), (0, 2), (0, 1)):
        minors.append(add(mul(matrix[i][0], matrix[j][1]),
                          scale(-1, mul(matrix[i][1], matrix[j][0]))))
    assert minors == [f, scale(-1, mul(b4, qvar)), mul(a6, b4)]
    assert_zero(add(add(mul(b4, f), scale(-1, mul(power(qvar, 2), mul(b4, qvar)))),
                    scale(-1, mul(mul(power(h, 5), a6), b4))))


def hilbert_checks():
    def c3(n):
        return comb(n + 3, 3) if n >= 0 else 0
    for n in range(12, 31):
        assert c3(n) - 2 * c3(n - 6) + c3(n - 12) == 36 * n - 144
    # The 10-degree generator and 10-degree syzygy cancel in the numerator;
    # the remaining numerator is that of the (6,6) complete intersection.
    terms = [(0, 1), (6, -2), (10, -1), (10, 1), (12, 1)]
    coeff = {}
    for degree, value in terms:
        coeff[degree] = coeff.get(degree, 0) + value
    assert {d: c for d, c in coeff.items() if c} == {0: 1, 6: -2, 12: 1}
    degree_sums = [8 * 4 + 4, 6 * 4 + 12, 6 * 4 + 12,
                   3 * 4 + 3 * 4 + 6 * 2, 3 * 4 + 15 + 9,
                   3 * 4 + 3 * 4 + 12, 6 * 4 + 12,
                   4 + 13 + 13 + 2 + 1 + 3, 4 + 13 + 14 + 4 + 1]
    assert degree_sums == [36] * 9


def main():
    quotient_checks()
    print("quotients: exact ranks, determinants, and truncated-algebra identities OK")
    jet_checks()
    print("equation spaces: 84 sextic monomials, double source dimension 23, profile OK")
    residual_checks()
    print("residual limits: explicit substitution and minor identity OK")
    hilbert_checks()
    print("Hilbert and degree checks: all OK")


if __name__ == "__main__":
    main()
