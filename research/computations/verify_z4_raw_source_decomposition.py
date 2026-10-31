#!/usr/bin/env python3
"""Exact Laurent-polynomial support for the raw-frame Z4 decomposition.

Variables are (u,a,b,h,d); only u permits negative exponents. This verifies
identities in a fixed frame, not invariance of any individual summand.
"""
from collections import defaultdict


def mon(*powers, coefficient=1):
    return {powers: coefficient}


def add(*polynomials):
    result = defaultdict(int)
    for polynomial in polynomials:
        for powers, coefficient in polynomial.items():
            result[powers] += coefficient
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def mul(*polynomials):
    result = mon(0, 0, 0, 0, 0)
    for polynomial in polynomials:
        product = defaultdict(int)
        for p, c in result.items():
            for q, d in polynomial.items():
                product[tuple(x+y for x, y in zip(p, q))] += c*d
        result = {p: c for p, c in product.items() if c}
    return result


def scale(coefficient, polynomial):
    return {p: coefficient*c for p, c in polynomial.items() if coefficient*c}


def upower(power):
    return mon(power, 0, 0, 0, 0)


a, b, h, d = (mon(0, *(int(i == j) for i in range(4))) for j in range(4))
p = add(a, mul(b, upower(1)), scale(3, mul(h, upower(2))))
q = add(d, scale(2, mul(h, upower(1))))
P = add(scale(3, mul(a, upower(-2))), mul(add(scale(3, b), scale(-4, d)), upower(-1)), h)
Q = add(scale(2, mul(a, upower(-1))), scale(2, b), scale(-3, d))
c1 = add(mul(upower(-4), q), scale(-1, mul(upower(-5), p)))
A1 = add(scale(3, mul(upower(-8), p)), scale(-4, mul(upower(-7), q)))
B1 = add(scale(2, mul(upower(-7), p)), scale(-3, mul(upower(-6), q)))
A2 = add(scale(-9, mul(upower(-12), p, p)), scale(16, mul(upower(-11), p, q)), scale(-6, mul(upower(-10), q, q)))
B2 = add(scale(-5, mul(upower(-11), p, p)), scale(9, mul(upower(-10), p, q)), scale(-3, mul(upower(-9), q, q)))
KA = mul(upower(8), Q, A2)
KB = scale(-1, mul(upower(8), P, B2))
Kmove = mul(upower(8), c1, add(mul(scale(2, a), A1), scale(-1, mul(add(scale(6, mul(a, upower(-1))), scale(3, b), scale(-4, d)), B1))))


def middle(polynomial):
    return {p: c for p, c in polynomial.items() if p[0] == -2}


expected = [
    add(scale(-88, mul(a,b,h)), scale(114, mul(a,d,h)), scale(-18, mul(b,b,b)), scale(59, mul(b,b,d)), scale(-60, mul(b,d,d)), scale(18, mul(d,d,d))),
    add(scale(82, mul(a,b,h)), scale(-102, mul(a,d,h)), scale(15, mul(b,b,b)), scale(-47, mul(b,b,d)), scale(45, mul(b,d,d)), scale(-12, mul(d,d,d))),
    add(scale(10, mul(a,b,h)), scale(-16, mul(a,d,h)), scale(6, mul(b,b,b)), scale(-23, mul(b,b,d)), scale(29, mul(b,d,d)), scale(-12, mul(d,d,d))),
]
for calculated, target in zip((KA, KB, Kmove), expected):
    assert middle(calculated) == mul(upower(-2), target)
C2 = mul(add(b, scale(-1, d)), add(scale(4, mul(a,h)), scale(3, mul(b,b)), scale(-8, mul(b,d)), scale(6, mul(d,d))))
assert add(*expected) == C2
# Formal substitution a=2alpha,b=2beta,h=2gamma,d=1+2delta modulo4.
substitutions = (upower(1), scale(2,a), scale(2,b), scale(2,h), add(mon(0,0,0,0,0),scale(2,d)))
def substitute(polynomial):
    terms=[]
    for powers, coefficient in polynomial.items():
        factors=[mon(0,0,0,0,0,coefficient=coefficient)]
        for variable, exponent in zip(substitutions,powers):
            factors.extend([variable]*exponent)
        terms.append(mul(*factors))
    return {powers: coefficient % 4 for powers,coefficient in add(*terms).items() if coefficient % 4}
for polynomial,target in zip(expected,(mon(0,0,0,0,0,coefficient=2),scale(2,b),scale(2,b))):
    assert substitute(polynomial)==target
assert substitute(C2)==mon(0,0,0,0,0,coefficient=2)
print('PASS: exact middle polynomials, sum C2, raw residues 2,2beta,2beta modulo4')
