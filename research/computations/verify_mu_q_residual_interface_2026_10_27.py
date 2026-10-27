#!/usr/bin/env python3
"""Exact finite corroboration of the mu_q residual-family chart calculations.

No third-party dependencies. The general proof is in the accompanying note;
these computations establish only the displayed sparse polynomial identities.
"""

from collections import defaultdict
from math import comb, gcd


def mul(left, right):
    out = defaultdict(int)
    for (i, j, k), a in left.items():
        for (l, m, n), b in right.items():
            if j + k + m + n <= 1:
                out[i + l, j + m, k + n] += a * b
    return {key: value for key, value in out.items() if value}


def power(poly, n):
    out = {(0, 0, 0): 1}
    for _ in range(n):
        out = mul(out, poly)
    return out


def sub(left, right):
    out = defaultdict(int, left)
    for key, value in right.items():
        out[key] -= value
    return {key: value for key, value in out.items() if value}


def belongs(q):
    return any(3 * b + 4 * c == q for b in range(q // 3 + 1)
               for c in range(q // 4 + 1))


def chart_checks(q, b, c):
    a = 2 * b + 3 * c
    assert q == 3 * b + 4 * c == a + b + c
    assert (4 * a + b, 3 * b + 4 * c) == (3 * q, q)
    # x0=1, x1=u, x2=u^3+y, x3=u^4+z; normal degree <=1.
    x2 = {(3, 0, 0): 1, (0, 1, 0): 1}
    x3 = {(4, 0, 0): 1, (0, 0, 1): 1}
    first = sub(power(x3, 3), power(x2, 4))
    second = sub({(q, 0, 0): 1}, mul(power(x2, b), power(x3, c)))
    assert first == {(9, 1, 0): -4, (8, 0, 1): 3}
    expected_second = {}
    if b:
        expected_second[q - 3, 1, 0] = -b
    if c:
        expected_second[q - 4, 0, 1] = -c
    assert second == expected_second
    # Extract the determinant independently as a sparse polynomial.
    f_y = { (i, 0, 0): v for (i, j, k), v in first.items() if j == 1 }
    f_z = { (i, 0, 0): v for (i, j, k), v in first.items() if k == 1 }
    g_y = { (i, 0, 0): v for (i, j, k), v in second.items() if j == 1 }
    g_z = { (i, 0, 0): v for (i, j, k), v in second.items() if k == 1 }
    assert sub(mul(f_y, g_z), mul(f_z, g_y)) == {(q + 5, 0, 0): q}
    # x3=1: S=X, G=(v^3+Y)^q-(v^4+X)^a v^b.
    # Its determinant is the Y coefficient q*v^(3q-3).
    v_y = {(3, 0, 0): 1, (0, 0, 1): 1}
    v_x = {(4, 0, 0): 1, (0, 1, 0): 1}
    infinity_g = sub(power(v_y, q), mul(power(v_x, a), {(b, 0, 0): 1}))
    assert infinity_g.get((3 * q - 3, 0, 1)) == q
    assert (q + 5) + (3 * q - 3) == 4 * q + 2
    # Relation-lattice index: primitive cross product is (1,3,4).
    cross = (4 * c + 3 * b, 3 * q, 4 * q)
    assert cross == (q, 3 * q, 4 * q)
    assert gcd(gcd(*cross[:2]), cross[2]) == q


count = 0
for q in range(3, 51):
    for b in range(4):
        if q >= 3 * b and (q - 3 * b) % 4 == 0:
            chart_checks(q, b, (q - 3 * b) // 4)
            count += 1

for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
    expected = {2: 4, 3: 3, 5: 25}.get(p, p)
    # This corroborates an inherited semigroup theorem; it is not its proof.
    actual = next(n for n in range(1, expected + 1)
                  if all(comb(n, j) % p == 0 or belongs(j)
                         for j in range(n + 1)))
    assert actual == expected

print(f"PASS: {count} exact two-chart determinants and relation-lattice indices")
print("PASS: 11 inherited fixed-carrier prime minima corroborated")
print("Scope: finite sparse identities; no unrestricted STCI or global novelty claim")
