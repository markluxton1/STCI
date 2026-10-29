#!/usr/bin/env python3
"""Exact sparse controls for the explicit non-binomial degree-p mates.

No dependencies. The uniform proof, including every prime >=43, is in
the companion research note; this script checks displayed identities at
selected primes, not the universal theorem by finite sampling.
"""

import json
from math import comb


def add_term(poly, exponent, coefficient, prime):
    value = (poly.get(exponent, 0) + coefficient) % prime
    if value:
        poly[exponent] = value
    else:
        poly.pop(exponent, None)


def verify(prime):
    r = (3 * prime) % 4
    n = (3 * prime - r) // 4
    E = (prime - 3 * r) // 4
    image = {}
    smallest_x0_exponent = prime
    for j in range(n + 1):
        h, ell = divmod(j, 4)
        x0_exponent = E + h - 3 * ell
        assert x0_exponent >= 0
        assert r + x0_exponent + n - j + 3 * h + 4 * ell == prime
        smallest_x0_exponent = min(smallest_x0_exponent, x0_exponent)
        # U0=s^4, U1=s^3 t, U3=t^4+s^3 z;
        # B(U)=s^8 z^4 and A(U)=s^15 z.
        for k in range(n - j + 1):
            exponent = (
                3 * r + 4 * x0_exponent + 8 * h + 15 * ell + 3 * k,
                r + 4 * (n - j - k),
                4 * h + ell + k,
            )
            coefficient = (-1) ** j * comb(n, j) * comb(n - j, k)
            add_term(image, exponent, coefficient, prime)
    assert image == {(prime, 3 * prime, 0): 1}
    # G_p(U) = U2^p - P_p(U); Frobenius leaves exactly z^(4p).
    pulled_mate = {exponent: -coefficient % prime
                   for exponent, coefficient in image.items()}
    add_term(pulled_mate, (prime, 3 * prime, 0), 1, prime)
    add_term(pulled_mate, (0, 0, 4 * prime), 1, prime)
    assert pulled_mate == {(0, 0, 4 * prime): 1}
    return {
        "prime": prime,
        "r": r,
        "n": n,
        "E": E,
        "summands_before_expansion": n + 1,
        "minimum_x0_exponent": smallest_x0_exponent,
        "homogeneous_degree": prime,
        "P_pullback": f"s^{prime}*t^{3 * prime}",
        "G_pullback": f"z^{4 * prime}",
        "status": "PASS",
    }


if __name__ == "__main__":
    print(json.dumps({
        "scope": "selected-prime exact controls; uniform proof in companion note",
        "family": "F=(x0^3*x3-x1^4)^4-x0^13*(x0^2*x2-x1^3)",
        "checks": [verify(p) for p in (43, 47, 53, 59, 61, 101)],
    }, indent=2))
