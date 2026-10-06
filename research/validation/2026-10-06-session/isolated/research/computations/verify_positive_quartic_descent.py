#!/usr/bin/env python3
"""Exact checks for the descent identities used in P-012.

This is not a substitute for the geometric proof. It checks the semigroup
membership step for representative primes and the exceptional characteristic-3
identity in the cuspidal normalization ring.
"""

import sympy as sp


s, t, z, alpha = sp.symbols("s t z alpha")


def in_standard_cusp_semigroup(i: int, j: int) -> bool:
    """Whether s^i t^j is in k[s^3,s^2 t,t^3]."""
    for a in range(i // 3 + 1):
        for b in range(min(i // 2, j) + 1):
            rem_i = i - 3 * a - 2 * b
            rem_j = j - b
            if rem_i == 0 and rem_j >= 0 and rem_j % 3 == 0:
                return True
    return False


def check_semigroup_lemma(max_total: int = 120) -> None:
    """For total degree 0 mod 3, exponent 1 is the unique obstruction."""
    for n in range(0, max_total + 1, 3):
        for i in range(n + 1):
            j = n - i
            expected = i != 1
            actual = in_standard_cusp_semigroup(i, j)
            assert actual == expected, (i, j, expected, actual)


def check_descent_support(p: int) -> None:
    """Check support of (l^p z^p-h^p)^3 for a dense sample l,h."""
    assert p in (2, 5, 7)
    l = s + 2 * t
    h = s**4 + 2 * s**3 * t + 3 * s**2 * t**2 + 4 * s * t**3 + 5 * t**4
    expr = sp.Poly((sp.expand(l**p) * z**p - sp.expand(h**p)) ** 3, s, t, z)

    # Reduce integer coefficients modulo p and inspect every surviving monomial.
    surviving = 0
    for (i, j, k), coeff in expr.terms():
        if int(coeff) % p == 0:
            continue
        surviving += 1
        assert i + j + 3 * k == 12 * p
        assert (i + j) % 3 == 0
        assert i % p == 0 and j % p == 0
        assert in_standard_cusp_semigroup(i, j), (p, i, j, k)
    assert surviving > 0


def check_characteristic_three_identity() -> None:
    """Verify the exceptional R_alpha identities coefficientwise mod 3."""
    X = s**3
    Y = s**2 * t
    Z = t**3 + alpha * s * t**2

    rhs = X * Z**2 + alpha * Y**2 * Z + alpha**2 * X * Y * Z - alpha**3 * Y**3
    first = sp.Poly(sp.expand(rhs - s**3 * t**6), s, t, alpha)
    assert all(int(c) % 3 == 0 for c in first.coeffs())

    second = sp.Poly(sp.expand(Z**3 - t**9 - alpha**3 * s**3 * t**6), s, t, alpha)
    assert all(int(c) % 3 == 0 for c in second.coeffs())

    # Ninth powers of arbitrary binary forms are polynomials in s^9,t^9.
    a, b, c, d, e = sp.symbols("a b c d e")
    h = a * s**4 + b * s**3 * t + c * s**2 * t**2 + d * s * t**3 + e * t**4
    ninth = sp.Poly(sp.expand(h**9), s, t, a, b, c, d, e)
    for monomial, coeff in ninth.terms():
        if int(coeff) % 3 == 0:
            continue
        i, j = monomial[0], monomial[1]
        assert i % 9 == 0 and j % 9 == 0


def main() -> None:
    check_semigroup_lemma()
    for p in (2, 5, 7):
        check_descent_support(p)
        print(f"PASS: standard-cusp descent support in characteristic {p}")
    check_characteristic_three_identity()
    print("PASS: characteristic-3 cusp-ring identities")
    print("PASS: all positive-quartic descent assertions")


if __name__ == "__main__":
    main()
