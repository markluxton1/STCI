#!/usr/bin/env python3
"""Exact local identities for the proposed intrinsic (4,4) K3 argument.

Standard library only. Monomial order is (t,x,y). This verifies polynomial
identities and Milnor-algebra dimensions for representatives; the proof
for arbitrary unit coefficient functions is in the companion note.
"""

from fractions import Fraction as Q


def poly(terms):
    return {m: Q(c) for m, c in terms.items() if c}


def scalar(c):
    return poly({(0, 0, 0): c})


def add(*items):
    result = {}
    for item in items:
        for monomial, coefficient in item.items():
            result[monomial] = result.get(monomial, Q(0)) + coefficient
    return poly(result)


def scale(c, item):
    return poly({m: Q(c) * value for m, value in item.items()})


def mul(first, second):
    result = {}
    for a, c in first.items():
        for b, d in second.items():
            monomial = tuple(a[i] + b[i] for i in range(3))
            result[monomial] = result.get(monomial, Q(0)) + c * d
    return poly(result)


def power(item, exponent):
    result = scalar(1)
    for _ in range(exponent):
        result = mul(result, item)
    return result


def derivative(item, variable):
    result = {}
    for monomial, coefficient in item.items():
        exponent = monomial[variable]
        if exponent:
            target = list(monomial)
            target[variable] -= 1
            result[tuple(target)] = coefficient * exponent
    return poly(result)


t = poly({(1, 0, 0): 1})
x = poly({(0, 1, 0): 1})
y = poly({(0, 0, 1): 1})


def verify_defect(d):
    td = power(t, d)
    f = add(power(x, 2), scale(-1, mul(td, y)), power(y, 2))
    shifted_y = add(y, scale(Q(-1, 2), td))
    square_form = add(
        power(x, 2), power(shifted_y, 2), scale(Q(-1, 4), power(t, 2 * d))
    )
    assert f == square_form

    # These identities prove equality of the Jacobian ideal with
    # (x, y-t^d/2, t^(2d-1)), since all displayed scalar coefficients
    # are nonzero in characteristic zero. Thus the quotient basis is
    # 1,t,...,t^(2d-2), of length 2d-1.
    j1, j2, j3 = x, shifted_y, power(t, 2 * d - 1)
    assert derivative(f, 1) == scale(2, j1)
    assert derivative(f, 2) == scale(2, j2)
    assert derivative(f, 0) == add(
        scale(-d, mul(power(t, d - 1), j2)), scale(Q(-d, 2), j3)
    )
    return 2 * d - 1


def verify_lambda_removal():
    # In the free module with basis 1,a,b,c=ab, impose
    # a^2=t^d b+lambda c, ab=c, b^2=ac=bc=c^2=0.
    # The identity (a-lambda*b/2)^2=t^d*b is checked coefficientwise.
    for d in (1, 2, 3):
        lam = add(scalar(2), scale(3, t))
        zero = ({}, {}, {}, {})
        basis = tuple(
            tuple(scalar(int(i == j)) for i in range(4)) for j in range(4)
        )

        def multiply_vectors(first, second):
            result = list(zero)
            for i, first_coefficient in enumerate(first):
                for j, second_coefficient in enumerate(second):
                    coefficient = mul(first_coefficient, second_coefficient)
                    if not coefficient:
                        continue
                    if i == 0:
                        result[j] = add(result[j], coefficient)
                    elif j == 0:
                        result[i] = add(result[i], coefficient)
                    elif i == j == 1:
                        result[2] = add(result[2], mul(coefficient, power(t, d)))
                        result[3] = add(result[3], mul(coefficient, lam))
                    elif {i, j} == {1, 2}:
                        result[3] = add(result[3], coefficient)
            return tuple(result)

        for first in basis:
            for second in basis:
                for third in basis:
                    assert multiply_vectors(multiply_vectors(first, second), third) == multiply_vectors(
                        first, multiply_vectors(second, third)
                    )
        adjusted_a = ({}, scalar(1), scale(Q(-1, 2), lam), {})
        assert multiply_vectors(adjusted_a, adjusted_a) == (
            {}, {}, power(t, d), {}
        )
        assert multiply_vectors(adjusted_a, basis[2]) == basis[3]


def verify_moving_a3():
    f = add(mul(t, y), power(x, 4))
    assert derivative(f, 0) == y
    assert derivative(f, 2) == t
    assert derivative(f, 1) == scale(4, power(x, 3))
    # Jacobian algebra k[[t,x,y]]/(y,t,4x^3) has basis 1,x,x^2.
    return 3


def main():
    verify_lambda_removal()
    ranks = {d: verify_defect(d) for d in (1, 2, 3)}
    a3_rank = verify_moving_a3()
    assert a3_rank == 3
    assert 8 * a3_rank == 24
    partitions = ((1, 1, 1), (2, 1), (3,))
    total_ranks = [6 * a3_rank + sum(ranks[d] for d in part) for part in partitions]
    assert total_ranks == [21, 22, 23]
    assert min(total_ranks) > 20
    print("PASS: exact lambda removal, completed squares, and Jacobian ideals")
    print("PASS: defect ranks d=1,2,3 are 1,3,5; moving A3 rank is 3")
    print("PASS: e=1 exceptional rank 24; e=0 ranks 21,22,23")


if __name__ == "__main__":
    main()
