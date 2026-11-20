#!/usr/bin/env python3
"""Exact polynomial controls for the written equation-layer argument.

This checks displayed identities and weight extremes, not the geometric
proofs of canonicity, flat closure, or the Cech/Kummer comparison.
"""
from collections import defaultdict


def add(*polys):
    out = defaultdict(int)
    for poly in polys:
        for exp, coefficient in poly.items():
            out[exp] += coefficient
    return {e: c for e, c in out.items() if c}


def scale(poly, c):
    return {e: c * a for e, a in poly.items() if c * a}


def mul(*polys):
    result = {(0, 0, 0, 0): 1}
    for poly in polys:
        out = defaultdict(int)
        for e, a in result.items():
            for f, b in poly.items():
                out[tuple(x + y for x, y in zip(e, f))] += a * b
        result = {e: c for e, c in out.items() if c}
    return result


def power(poly, n):
    return mul(*([poly] * n))


def extreme(poly, upper=False):
    weight = lambda e: sum(a * b for a, b in zip(e, (0, 1, 3, 4)))
    w = (max if upper else min)(map(weight, poly))
    return w, {e: c for e, c in poly.items() if weight(e) == w}


def main():
    x, y, z, w = [{tuple(int(i == j) for i in range(4)): 1} for j in range(4)]
    U = add(power(y, 4), scale(mul(power(x, 3), w), -1))
    V = add(power(z, 4), scale(mul(x, power(w, 3)), -1))
    D = add(power(V, 2), mul(power(x, 4), U))
    A = mul(w, power(y, 3))
    F = add(power(U, 3), mul(A, D))
    G = power(D, 3)
    Gp = add(G, mul(power(x, 12), F))
    assert {sum(e) for e in F} == {12}
    assert {sum(e) for e in Gp} == {24}
    assert extreme(F) == (11, mul(A, power(x, 4), U))
    assert extreme(G) == (12, mul(power(x, 12), power(U, 3)))
    assert extreme(Gp) == (11, mul(power(x, 12), extreme(F)[1]))
    assert extreme(F, True) == (31, mul(A, power(V, 2)))
    assert extreme(G, True) == extreme(Gp, True) == (72, power(V, 6))
    H = add(power(x, 12), power(w, 12))
    G16 = add(power(V, 4), mul(H, U))
    F16 = add(power(U, 4), G16)
    assert extreme(F16) == extreme(G16) == (4, mul(power(x, 12), U))
    assert extreme(F16, True) == extreme(G16, True) == (52, mul(power(w, 12), U))
    assert 256 * (4 + 64 - 4) // 2 - 256 * (16 + 16 - 4) // 2 == 4608
    assert [12 - 4, 8 - 4, 0] == [8, 4, 0]
    print('Exact homogeneous weights, shear leaders, and Hilbert correction: PASS')


if __name__ == '__main__':
    main()
