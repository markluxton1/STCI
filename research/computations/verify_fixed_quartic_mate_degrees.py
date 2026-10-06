#!/usr/bin/env python3
"""Exact finite controls for the fixed quartic-cone mate-degree theorem.

This checks binomial descent, semigroup solutions, and the displayed
normalization pullbacks. The all-degree theorem and arbitrary-mate reduction
are proved in notes/2026-10-05-positive-quartic-carrier-optimality.md.
No finite scan is used to prove that theorem.
"""
from math import comb


def semigroup_solution(r):
    for b in range(r // 3 + 1):
        if (r - 3 * b) % 4 == 0:
            c = (r - 3 * b) // 4
            return 2 * b + 3 * c, b, c
    return None


def descends(n, p):
    return all(comb(n, j) % p == 0 or semigroup_solution(j) is not None
               for j in range(n + 1))


def p_primary_part(n, p):
    r = 1
    while n % p == 0:
        n //= p
        r *= p
    return r


assert [r for r in range(30) if semigroup_solution(r) is None] == [1, 2, 5]
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
for p in primes:
    minimum = {2: 4, 3: 3, 5: 25}.get(p, p)
    for n in range(1, 201):
        direct = descends(n, p)
        lucas = semigroup_solution(p_primary_part(n, p)) is not None
        assert direct == lucas == (n % minimum == 0), (p, n)
    a, b, c = semigroup_solution(minimum)
    assert a + b + c == minimum
    # Pull back x0^a*x2^b*x3^c through
    # [s:t:z] -> [s^4:z:s*t^3:t^4].
    assert 4 * a + b == 3 * minimum
    assert 3 * b + 4 * c == minimum
    # At a p-power minimum all intermediate binomial coefficients vanish.
    assert all(comb(minimum, j) % p == 0 for j in range(1, minimum))
    print(f"p={p}: exact finite descent controls agree; minimum={minimum}; "
          f"mate monomial exponents={(a, b, c)}")

assert semigroup_solution(4) == (3, 0, 1)
assert semigroup_solution(3) == (2, 1, 0)
assert semigroup_solution(25) == (18, 3, 4)
for n in range(1, 201):
    # In characteristic zero the nonzero next coefficient has index one.
    assert comb(n, 1) != 0 and semigroup_solution(1) is None

print("PASS: characteristic-zero control and all displayed minimum mates")
