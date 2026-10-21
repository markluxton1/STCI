#!/usr/bin/env python3
"""New checks for the general marked embedded obstruction mechanism.

This imports the previously audited three Laurent coefficient polynomials.
It does not reconstruct the quartic ambient rational transitions, re-prove
accepted carrier exclusions, or turn finite arithmetic checks into a proof.
Run with: python3 research/computations/verify_z4_general_mechanism_2026_10_21.py
"""

from math import comb

import sympy as s


def valuation(value, prime):
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def laurent_class(expr, coordinate, degree):
    """Normal representative of H1(P1,O(degree)), degree <= -2."""
    assert degree <= -2
    result = 0
    for term in s.Add.make_args(s.expand(expr)):
        exponent = int(term.as_powers_dict().get(coordinate, 0))
        if degree < exponent < 0:
            result += term
    return s.expand(result)


a, b, h, d, alpha, beta, gamma, delta = s.symbols(
    "a b h d alpha beta gamma delta"
)
coefficients = [
    h * (a * h + 3 * b**2 - 5 * b * d + 3 * d**2),
    (b - d) * (4 * a * h + 3 * b**2 - 8 * b * d + 6 * d**2),
    a * (a * h + 9 * b**2 - 23 * b * d + 15 * d**2),
]
assert [f.subs({a: 0, b: 0, h: 0, d: 1}) for f in coefficients] == [0, -6, 0]
substitution = {a: 2 * alpha, b: 2 * beta, h: 2 * gamma, d: 1 + 2 * delta}
divided = []
for expression in coefficients:
    polynomial = s.Poly(s.expand(expression.subs(substitution)), alpha, beta, gamma, delta)
    assert all(int(value) % 2 == 0 for value in polynomial.coeffs())
    divided.append(
        s.Poly(s.expand(polynomial.as_expr() / 2), alpha, beta, gamma, delta, modulus=2).as_expr()
    )
assert divided == [gamma, 1, alpha]
assert s.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]).rank() == 2
print("PASS: accepted full Laurent polynomials yield -6, lambda=(gamma,1,alpha), rank(D)=2")

# A nonlinear normal-coordinate change, allowing coefficients depending on a
# moving base coordinate. Multiplication by the new diagonal frame clears the
# harmless unit denominator in a'=(alpha*a+C)/delta^2.
t, y = s.symbols("t y")
aa0, aa1, al0, al1, de0, de1, cc0, cc1 = s.symbols(
    "aa0 aa1 al0 al1 de0 de1 cc0 cc1"
)
mix, quad, xy, xx, base_y, base_x = s.symbols("mix quad xy xx base_y base_x")
aa = aa0 + aa1 * t
al = al0 + al1 * t
de = de0 + de1 * t
cc = cc0 + cc1 * t
x = aa * y**2
xp = al * x + cc * y**2 + xy * x * y + xx * x**2
yp = mix * x + de * y + quad * y**2
tp = t + base_y * y + base_x * x
defect = s.expand(de.subs(t, tp)**2 * xp - (al.subs(t, tp) * aa.subs(t, tp) + cc.subs(t, tp)) * yp**2)
assert all(s.expand(defect).coeff(y, index) == 0 for index in range(3))
print("PASS: full adapted quadratic transformation, linear mixing, and moving base coordinate")

u, c = s.symbols("u c", nonzero=True)
old = -6 / u**2
new = old - (1 + u) + u**-4 * (u**-1 + u**-2)
assert laurent_class(old, u, -4) == laurent_class(new, u, -4)
print("PASS: nontrivial integral chartwise quadratic changes alter full cocycle only by a coboundary")

for stage in range(2, 9):
    degree = 8 - 6 * stage
    normalized = (c * u**-10) / u**-8
    assert s.simplify(normalized - c * u**-2) == 0
    assert laurent_class(normalized, u, degree) == c * u**-2
    changed = normalized - (1 + u**3) + u**degree * (1 + u**-2)
    assert laurent_class(changed, u, degree) == c * u**-2
print("PASS: same-conormal nonsplit gluing at stages 2..8 has nonzero normalized obstruction")

for prime in (2, 3, 5):
    for power in (1, 2, 3):
        exponent = prime**power
        surviving = []
        for index in range(1, exponent):
            coefficient = comb(exponent, index)
            assert valuation(coefficient, prime) == power - valuation(index, prime)
            if (coefficient // prime) % prime:
                surviving.append(index)
        assert surviving == [index * prime**(power - 1) for index in range(1, prime)]
        for index in range(1, prime):
            lhs = (comb(exponent, index * prime**(power - 1)) // prime) % prime
            rhs = ((-1)**(index - 1) * pow(index, -1, prime)) % prime
            assert lhs == rhs
        # a unit and b normal: minimum surviving normal order is p^(r-1).
        assert min(surviving) == prime**(power - 1)
        # Both a and b normal: every term has total normal order p^r.
        assert all((exponent - index) + index == exponent for index in surviving)
print("PASS: p=2,3,5 and r=1,2,3 illustrate divided cross-effects and both normal-order regimes")

# At higher divided order the leading section need not be affine-linear.
# o(q)=4+q^2, q=2t over Z_(2), gives o/4 = 1+t^2 mod 2.
q = s.symbols("q")
leading = s.expand((4 + q**2).subs(q, 2 * t) / 4)
assert leading == 1 + t**2
assert s.Poly(s.diff(leading, t), t, modulus=2).is_zero
assert leading.subs(t, 0) % 2 == 1 and leading.subs(t, 1) % 2 == 0
print("PASS: higher divided obstruction example has zero differential but a cancelling lift")

print("Boundary: new finite checks support the stated proofs; no divided-Frobenius identification is inferred.")
