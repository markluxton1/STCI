#!/usr/bin/env python3
"""Exact finite checks accompanying the conic power-descent proof.

These checks do not prove the generic-Artin classification or classify
actual surface carriers. They check the universal odd coefficient,
cyclotomic specialization, and two nilpotent counterexamples to weaker
coefficient conditions over characteristic zero.
"""

import json
import sympy as sp

m, ell, delta, b, zeta, eps = sp.symbols("m ell delta b zeta eps")


def pair_mul(left, right, square):
    a, u = left
    c, v = right
    return (sp.expand(a*c + u*v*square), sp.expand(a*v + u*c))


def pair_pow(pair, n, square):
    answer = (sp.Integer(1), sp.Integer(0))
    for _ in range(n):
        answer = pair_mul(answer, pair, square)
    return answer


def reduce_eps(expr):
    return sp.rem(sp.Poly(sp.expand(expr), eps), sp.Poly(eps**2, eps)).as_expr()


def nilpotent_pair_pow(pair, n, square):
    answer = (sp.Integer(1), sp.Integer(0))
    for _ in range(n):
        answer = tuple(reduce_eps(x) for x in pair_mul(answer, pair, square))
    return answer


odd_checks = []
cyclotomic_checks = []
nilpotent_checks = []
for n in range(1, 25):
    actual_odd = pair_pow((m, ell), n, delta)[1]
    formula = ell * sum(
        sp.binomial(n, 2*j+1) * m**(n-2*j-1) * (delta*ell**2)**j
        for j in range((n-1)//2+1)
    )
    assert sp.expand(actual_odd-formula) == 0
    odd_checks.append(n)

    if n >= 3:
        # lambda=(1+zeta)/(1-zeta) has
        # (lambda-1)/(lambda+1)=zeta. Its two power values coincide.
        lam = (1+zeta)/(1-zeta)
        numerator = sp.together((lam+1)**n-(lam-1)**n).as_numer_denom()[0]
        cyclotomic = sp.cyclotomic_poly(n, zeta)
        assert sp.rem(sp.Poly(numerator, zeta), sp.Poly(cyclotomic, zeta)).is_zero
        cyclotomic_checks.append(n)

    # m=epsilon, ell=1, delta=1: m²=0, but anti correction survives
    # every even power. Thus rho=0 proportionality is not sufficient.
    first_odd = nilpotent_pair_pow((eps, 1), n, 1)[1]
    assert first_odd == (n*eps if n % 2 == 0 else 1)
    # m=1, ell=epsilon, delta=epsilon: reduced ell=0 does not suffice.
    second_odd = nilpotent_pair_pow((1, eps), n, eps)[1]
    assert second_odd == n*eps
    nilpotent_checks.append(n)

# Exact factor checks at the first three nontrivial constants.
d = sp.symbols("d")
s3 = 3*m**2+d
s4 = 4*m*(m**2+d)
s6 = 6*m**5+20*m**3*d+6*m*d**2
assert sp.expand(s6 - 2*m*(3*m**2+d)*(m**2+3*d)) == 0
assert sp.rem(sp.Poly(s3, m), sp.Poly(m**2+d/3, m)).is_zero
assert sp.rem(sp.Poly(s4, m), sp.Poly(m**2+d, m)).is_zero

print(json.dumps({
    "status": "PASS",
    "sympy_version": sp.__version__,
    "universal_odd_coefficients_checked": odd_checks,
    "cyclotomic_power_specializations_checked": cyclotomic_checks,
    "nilpotent_counterexample_powers_checked": nilpotent_checks,
    "smooth_or_double_conic_degree_four_section_dimension": 9,
    "smooth_or_double_conic_required_rank_minors": 36,
    "separate_reduced_line_degree_four_section_dimension": 5,
    "separate_reduced_line_required_rank_minors": 10,
    "scope": "Finite exact identity checks; generic-Artin proof and actual surface geometry are separate."
}, indent=2))
