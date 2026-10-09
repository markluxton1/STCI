#!/usr/bin/env python3
"""Check the sparse all-stage certificate from P-043 exactly.

The written proof is uniform in N.  This script corroborates its coefficient
identities for N=2,...,8, including the transition-map pullback of the two
functionals.  It does not classify any other degree-four multiplier pairs and
does not prove non-quasi-cyclicity.
"""

from functools import lru_cache

import sympy as sp


x, y, z, w, lam = sp.symbols("x y z w lambda")
variables = (x, y, z, w)

q = x * w - y * z
A = x**2 * z - y**3
B = x * z**2 - y**2 * w
F = sp.expand(x * A + lam * y**2 * q)
G = sp.expand(y * A + lam * x * z * q)


@lru_cache(maxsize=None)
def monomial_exponents(degree):
    return tuple(
        (a, b, c, degree - a - b - c)
        for a in range(degree + 1)
        for b in range(degree - a + 1)
        for c in range(degree - a - b + 1)
    )


def term_dict(expression):
    return dict(sp.Poly(sp.expand(expression), *variables).terms())


def clean_weights(weights):
    return {
        exponent: sp.expand(coefficient)
        for exponent, coefficient in weights.items()
        if sp.expand(coefficient) != 0
    }


def phi_weights(N):
    return clean_weights(
        {
            (2 * N, 0, 2 * N - 2, N - 1): -(N - 1) * lam,
            (2 * N - 1, 1, 2 * N - 1, N - 2): -lam,
            (2 * N - 1, 0, 2 * N - 1, N - 1): -1,
        }
    )


def psi_weights(N):
    return clean_weights(
        {
            (2 * N - 1, 0, 2 * N - 2, N): N,
            (2 * N - 2, 1, 2 * N - 1, N - 1): 1,
        }
    )


def functional_on_shifted_product(base_terms, shift, weights):
    """Apply a coefficient functional to base_polynomial * monomial(shift)."""

    total = 0
    for target, weight in weights.items():
        needed = tuple(target[index] - shift[index] for index in range(4))
        if min(needed) >= 0:
            total += weight * base_terms.get(needed, 0)
    return sp.expand(total)


def pull_back_weights(weights, multiplier_terms):
    """Pull a coefficient functional back along P -> multiplier * P."""

    pulled = {}
    for target, weight in weights.items():
        for exponent, coefficient in multiplier_terms.items():
            source = tuple(target[index] - exponent[index] for index in range(4))
            if min(source) >= 0:
                pulled[source] = pulled.get(source, 0) + weight * coefficient
    return clean_weights(pulled)


F_terms = term_dict(F)
G_terms = term_dict(G)
qB_terms = term_dict(q * B)

assert 5 * 1 - 7 == -2

for N in range(2, 9):
    phi = phi_weights(N)
    psi = psi_weights(N)
    qN_terms = term_dict(q**N)
    BN_terms = term_dict(B**N)

    # Phi and Psi descend to the relevant graded piece of S/(q^N,B^N).
    for exponent in monomial_exponents(3 * N - 3):
        assert functional_on_shifted_product(qN_terms, exponent, phi) == 0
        assert functional_on_shifted_product(qN_terms, exponent, psi) == 0
    for exponent in monomial_exponents(2 * N - 3):
        assert functional_on_shifted_product(BN_terms, exponent, phi) == 0
        assert functional_on_shifted_product(BN_terms, exponent, psi) == 0

    # The combined functional kills every possible boundary (Fh,Gh).
    for exponent in monomial_exponents(5 * N - 7):
        value = functional_on_shifted_product(F_terms, exponent, phi)
        value += functional_on_shifted_product(G_terms, exponent, psi)
        assert sp.expand(value) == 0

    # It detects the target pair with the constant value -1.
    R_terms = term_dict(q ** (N - 1) * B ** (N - 1))
    target_value = functional_on_shifted_product(R_terms, (1, 0, 1, 0), phi)
    target_value += functional_on_shifted_product(R_terms, (0, 1, 0, 1), psi)
    assert sp.expand(target_value) == -1

    # The detecting functionals themselves respect P -> qBP.
    assert pull_back_weights(phi_weights(N + 1), qB_terms) == phi
    assert pull_back_weights(psi_weights(N + 1), qB_terms) == psi

print("PASS: P-043 all-stage coefficient certificate checked for N=2,...,8")
