#!/usr/bin/env python3
"""Exact first-conormal root collision for the rational quartic C4.

This companion to c4_conormal.py constructs an M8-chart quartic whose first
conormal divisor has a root of multiplicity five.  It verifies the polynomial
and local Taylor data used to identify the collision germ.  The final analytic
A9,5 interpretation uses the characteristic-zero formal Morse lemma and
Jaffe's A_{n,k} type formula; the script reports the exact hypotheses for that
interpretation rather than pretending to mechanize formal analytic equivalence.
"""

from collections import defaultdict
from fractions import Fraction

from c4_conormal import (
    affine_conormal_pair,
    gradient_restriction,
    passes_q_multiple_gradient_test,
    restriction,
)


def add(a, b):
    result = defaultdict(int)
    for polynomial in (a, b):
        for exponent, coefficient in polynomial.items():
            result[exponent] += coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def multiply(a, b):
    result = defaultdict(int)
    for exponent_a, coefficient_a in a.items():
        for exponent_b, coefficient_b in b.items():
            result[exponent_a + exponent_b] += coefficient_a * coefficient_b
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def power(a, exponent):
    result = {0: 1}
    for _ in range(exponent):
        result = multiply(result, a)
    return result


def derivative(a):
    return {exponent - 1: exponent * coefficient for exponent, coefficient in a.items() if exponent}


def trim(coefficients):
    coefficients = list(coefficients)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def divmod_polynomials(dividend, divisor):
    """Exact division for low-to-high coefficient lists."""
    dividend = trim([Fraction(coefficient) for coefficient in dividend])
    divisor = trim([Fraction(coefficient) for coefficient in divisor])
    quotient = [Fraction(0)] * max(1, len(dividend) - len(divisor) + 1)
    while dividend != [0] and len(dividend) >= len(divisor):
        coefficient = dividend[-1] / divisor[-1]
        shift = len(dividend) - len(divisor)
        quotient[shift] = coefficient
        for index, divisor_coefficient in enumerate(divisor):
            dividend[index + shift] -= coefficient * divisor_coefficient
        dividend = trim(dividend)
    return trim(quotient), dividend


def gcd_polynomials(a, b):
    a = trim(a)
    b = trim(b)
    while b != [0]:
        _, remainder = divmod_polynomials(a, b)
        a, b = b, remainder
    return [coefficient / a[-1] for coefficient in a]


def multivariate_add(a, b):
    result = defaultdict(int)
    for polynomial in (a, b):
        for exponent, coefficient in polynomial.items():
            result[exponent] += coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def multivariate_multiply(a, b):
    result = defaultdict(int)
    for (t_a, r_a, q_a), coefficient_a in a.items():
        for (t_b, r_b, q_b), coefficient_b in b.items():
            result[(t_a + t_b, r_a + r_b, q_a + q_b)] += coefficient_a * coefficient_b
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def multivariate_power(a, exponent):
    result = {(0, 0, 0): 1}
    for _ in range(exponent):
        result = multivariate_multiply(result, a)
    return result


def local_expansion(polynomial):
    """Substitute x=1, y=t, z=t^3+r, w=t^4+tr+q."""
    t = {(1, 0, 0): 1}
    y = t
    z = multivariate_add({(3, 0, 0): 1}, {(0, 1, 0): 1})
    w = multivariate_add(
        multivariate_add({(4, 0, 0): 1}, {(1, 1, 0): 1}),
        {(0, 0, 1): 1},
    )
    result = {}
    for (x_exponent, y_exponent, z_exponent, w_exponent), coefficient in polynomial:
        term = multivariate_power(y, y_exponent)
        term = multivariate_multiply(term, multivariate_power(z, z_exponent))
        term = multivariate_multiply(term, multivariate_power(w, w_exponent))
        result = multivariate_add(result, {exponent: coefficient * value for exponent, value in term.items()})
    return result


def first_blowup_chart(expansion):
    """Substitute q=r(t+v) and divide by r for the strict transform chart.

    The chart contains the section selected by the generic conormal direction:
    q/r=t, equivalently v=0.  Coordinates are again ordered (t,r,v).
    """
    t = {(1, 0, 0): 1}
    r = {(0, 1, 0): 1}
    q = {(1, 1, 0): 1, (0, 1, 1): 1}
    substituted = {}
    for (t_exponent, r_exponent, q_exponent), coefficient in expansion.items():
        term = multivariate_power(t, t_exponent)
        term = multivariate_multiply(term, multivariate_power(r, r_exponent))
        term = multivariate_multiply(term, multivariate_power(q, q_exponent))
        substituted = multivariate_add(substituted, {exponent: coefficient * value for exponent, value in term.items()})
    assert all(r_exponent >= 1 for _, r_exponent, _ in substituted)
    return {
        (t_exponent, r_exponent - 1, v_exponent): coefficient
        for (t_exponent, r_exponent, v_exponent), coefficient in substituted.items()
        if coefficient
    }


def a_type(n, k):
    """Jaffe's recursion phi(n,k) for an A_{n,k} surface--curve pair."""
    if 2 * k > n + 1:
        return a_type(n, n - k + 1)
    if 2 * k == n + 1:
        return (k,)
    return (k,) + a_type(n - k, k)


def main():
    q = [((1, 0, 0, 1), 1), ((0, 1, 1, 0), -1)]
    h = {0: -1, 2: 10, 3: -16, 5: 16, 6: -10, 8: 1}
    residual_factor = {0: 1, 1: 5, 2: 5, 3: 1}

    collision_quartic = [
        ((3, 0, 0, 1), 1),
        ((2, 1, 1, 0), -2),
        ((2, 0, 2, 0), 10),
        ((1, 2, 0, 1), -10),
        ((1, 1, 2, 0), -16),
        ((1, 0, 3, 0), 16),
        ((1, 0, 2, 1), -10),
        ((1, 0, 0, 3), 1),
        ((0, 4, 0, 0), 1),
        ((0, 3, 0, 1), 16),
        ((0, 2, 1, 1), -16),
        ((0, 2, 0, 2), 10),
        ((0, 1, 1, 2), -2),
        ((0, 0, 4, 0), 1),
    ]

    assert h == multiply(power({0: -1, 1: 1}, 5), residual_factor)
    assert restriction(collision_quartic) == {}
    assert affine_conormal_pair(collision_quartic) == ({}, {exponent + 1: coefficient for exponent, coefficient in h.items()})
    expected_gradient = [
        {4: -1, 6: 10, 7: -16, 9: 16, 10: -10, 12: 1},
        {3: 2, 5: -20, 6: 32, 8: -32, 9: 20, 11: -2},
        {1: -2, 3: 20, 4: -32, 6: 32, 7: -20, 9: 2},
        {0: 1, 2: -10, 3: 16, 5: -16, 6: 10, 8: -1},
    ]
    assert gradient_restriction(collision_quartic) == expected_gradient
    assert not passes_q_multiple_gradient_test(collision_quartic, q)

    expansion = local_expansion(collision_quartic)
    normal_linear = {exponent: coefficient for exponent, coefficient in expansion.items() if exponent[1] + exponent[2] == 1}
    expected_linear = {}
    for exponent, coefficient in h.items():
        expected_linear[(exponent + 1, 1, 0)] = coefficient
        expected_linear[(exponent, 0, 1)] = -coefficient
    assert normal_linear == expected_linear

    normal_quadratic = {exponent: coefficient for exponent, coefficient in expansion.items() if exponent[1] + exponent[2] == 2}
    a_rr = [10, -16, 0, 32, -20, 0, 3]
    a_rq = [0, 0, -16, 0, 0, -2]
    a_qq = [0, 0, 10, 0, 1]
    expected_quadratic = {}
    for exponent, coefficient in enumerate(a_rr):
        if coefficient:
            expected_quadratic[(exponent, 2, 0)] = coefficient
    for exponent, coefficient in enumerate(a_rq):
        if coefficient:
            expected_quadratic[(exponent, 1, 1)] = coefficient
    for exponent, coefficient in enumerate(a_qq):
        if coefficient:
            expected_quadratic[(exponent, 0, 2)] = coefficient
    assert normal_quadratic == expected_quadratic

    # At t=1, Q(r,q)=9r^2-18rq+11q^2.  The first nonzero linear normal
    # term is 12 tau^5(r-q), since H=(t-1)^5 residual_factor and residual_factor(1)=12.
    normal_quadratic_at_one = (9, -18, 11)
    normal_quadratic_determinant = 9 * 11 - (-18 // 2) ** 2
    assert normal_quadratic_determinant == 18
    linear_vector = (12, -12)
    inverse_quadratic_numerator = (
        linear_vector[0] * (11 * linear_vector[0] + 9 * linear_vector[1])
        + linear_vector[1] * (9 * linear_vector[0] + 9 * linear_vector[1])
    )
    assert inverse_quadratic_numerator == 288
    completed_square_coefficient = Fraction(-inverse_quadratic_numerator, 4 * normal_quadratic_determinant)
    assert completed_square_coefficient == -4

    strict_transform = first_blowup_chart(expansion)
    exceptional_restriction = {
        (t_exponent, v_exponent): coefficient
        for (t_exponent, r_exponent, v_exponent), coefficient in strict_transform.items()
        if r_exponent == 0
    }
    assert exceptional_restriction == {(exponent, 1): -coefficient for exponent, coefficient in h.items()}
    strict_transform_r_coefficient_at_collision = sum(
        coefficient
        for (t_exponent, r_exponent, v_exponent), coefficient in strict_transform.items()
        if r_exponent == 1 and v_exponent == 0
    )
    assert strict_transform_r_coefficient_at_collision == 2

    # At a simple root alpha of residual_factor, the tangent-cone determinant is
    # a nonzero scalar times H'(alpha)^2 D(alpha), where D is below.
    d_polynomial = [10, -16, 0, 16, -10, 0, 2]
    assert gcd_polynomials([Fraction(coefficient) for coefficient in residual_factor.values()], [Fraction(coefficient) for coefficient in derivative(residual_factor).values()]) == [Fraction(1)]
    assert gcd_polynomials(d_polynomial, [Fraction(coefficient) for coefficient in residual_factor.values()]) == [Fraction(1)]

    assert a_type(9, 5) == (5,)
    assert a_type(1, 1) == (1,)
    print("collision_H=(t-1)^5*(1+5t+5t^2+t^3)")
    print("collision_quartic: in_I=True q_factor_excluded_by_gradient=True conormal_pair=(0,tH)")
    print("collision_t=1: normal_quadratic=9r^2-18rq+11q^2 determinant=18")
    print("collision_t=1: leading_normal_linear=12*tau^5*(r-q) completed_square_tau10_coefficient=-4")
    print("collision_first_blowup: exceptional_restriction=-H(t)*v, so p1_local_at_t=1=5")
    print("collision_first_blowup_at_t=1: strict_transform_r_coefficient=2, so p2_local=0")
    print("collision_simple_roots: gcd(residual,residual_prime)=1 gcd(residual,D)=1")
    print("collision_local_types: A_9,5=(5); three A_1,1=(1); total_type=(8)")


if __name__ == "__main__":
    main()
