#!/usr/bin/env python3
"""Exact checks accompanying the 2026-10-21 characteristic-zero report.

Standard library only. These checks verify the displayed identities and small
linear-algebra calculations; they do not prove a global STCI exclusion.
"""

from fractions import Fraction
from itertools import permutations


def obstruction(a, b, d, h):
    return (
        h * (a * h + 3 * b**2 - 5 * b * d + 3 * d**2),
        (b - d) * (4 * a * h + 3 * b**2 - 8 * b * d + 6 * d**2),
        a * (a * h + 9 * b**2 - 23 * b * d + 15 * d**2),
    )


def determinant(matrix):
    n = len(matrix)
    total = Fraction(0)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = Fraction((-1) ** inversions)
        for i in range(n):
            term *= matrix[i][perm[i]]
        total += term
    return total


def add(p, q, multiplier=1):
    out = dict(p)
    for monomial, coefficient in q.items():
        out[monomial] = out.get(monomial, 0) + multiplier * coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def multiply(p, q):
    out = {}
    for (i, j, k), a in p.items():
        for (l, m, n), b in q.items():
            key = (i + l, j + m, k + n)
            out[key] = out.get(key, 0) + a * b
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def normal_form(p):
    """Reduce in Z[t,x,y]/(x^2,y^2+t*x), using its monic basis."""
    out = {}
    for (x_power, y_power, t_power), coefficient in p.items():
        pairs, y_power = divmod(y_power, 2)
        x_power += pairs
        t_power += pairs
        coefficient *= (-1) ** pairs
        if x_power >= 2:
            continue
        key = (x_power, y_power, t_power)
        out[key] = out.get(key, 0) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def main():
    # Same quotient degree, different intrinsic obstruction classes.
    distinguished = obstruction(0, 0, 1, 0)
    unobstructed = obstruction(0, 1, 1, 0)
    assert distinguished == (0, -6, 0)
    assert unobstructed == (0, 0, 0)
    # The nonzero middle functional is outside the evaluation Veronese conic.
    c1, c2, c3 = distinguished
    assert c2**2 - c1 * c3 == 36
    print("PASS: q0=(0,-6,0), q1=0; q0 dual functional lies off the evaluation conic")

    # H^1(O(3*epsilon-7)) can be nonzero only for epsilon=0 or 1.
    assert [max(0, 6 - 3 * epsilon) for epsilon in range(5)] == [6, 3, 0, 0, 0]
    print("PASS: first obstruction dimensions for epsilon=0,...,4 are 6,3,0,0,0")

    x2 = {(2, 0, 0): 1}
    y2_tx = {(0, 2, 0): 1, (1, 0, 1): 1}
    f = add(x2, y2_tx)
    g = add(x2, y2_tx, 2)
    assert add(add(f, f), g, -1) == x2
    assert add(g, f, -1) == y2_tx
    assert normal_form(x2) == {}
    assert normal_form(y2_tx) == {}
    assert normal_form({(0, 4, 0): 1}) == {}
    # The two chosen homogeneous quadrics have rank three, hence are integral
    # over every algebraically closed characteristic-zero field.
    half = Fraction(1, 2)
    assert determinant([[1, 0, half], [0, 1, 0], [half, 0, 0]]) == Fraction(-1, 4)
    assert determinant([[1, 0, 1], [0, 2, 0], [1, 0, 0]]) == -2
    print("PASS: integral quadric pair generates (x^2,y^2+t*x); y^4=0; both ranks are three")

    # Flat specialization to Z4 must have the same CI Hilbert polynomial.
    pairs = [(d, e) for d in range(1, 17) for e in range(d, 17) if d * e == 16 and d + e == 8]
    assert pairs == [(4, 4)]
    surviving = [(d * e, d, e) for d in range(5, 37) for e in range(d, 37) if d * e % 4 == 0]
    assert min(surviving) == (36, 6, 6)
    print("PASS: Z4 Hilbert polynomial forces (4,4); accepted d,e>=5 imply m>=9")

    print("All exact checks passed. Global arguments and their hypotheses are in the accompanying report.")


if __name__ == "__main__":
    main()
