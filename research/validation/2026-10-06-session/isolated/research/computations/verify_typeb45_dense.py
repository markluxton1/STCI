#!/usr/bin/env python3
"""Rederive the exhaustive dense type-B (4,5) formal-neighborhood audit.

Exact characteristic-zero computation, independently reconstructed on
2026-10-05.  This derives all moving-coordinate jets, killing sections,
Cech corrections, elimination, epimorphism failures, and the terminal class.
It covers b0*b1 != 0, normalized to b0=b1=1.  The other quotient charts are
covered by verify_typeb45_boundary.py, verify_typeb45_corner.py and reversal.
See `research/RESEARCH_RECORD.md` P-025 and
`research/notes/2026-10-05-typea-audit.md` for the geometric proof inputs;
a polynomial identity alone is not a flatness or cohomology theorem.
"""
import sympy as sp
from sympy.polys.fields import field


class Jet:
    def __init__(self, coefficient_field, order):
        self.K, self.order = coefficient_field, order
        self.m = {(1, 0): self.K.one}
        self.ell = {(0, 1): self.K.one}

    def constant(self, value):
        return {(0, 0): self.K(value)}

    def add(self, left, right):
        result = dict(left)
        for ij, coefficient in right.items():
            result[ij] = result.get(ij, self.K.zero) + coefficient
        return {ij: coefficient for ij, coefficient in result.items() if coefficient}

    def scale(self, coefficient, value):
        coefficient = self.K(coefficient)
        return {ij: coefficient * x for ij, x in value.items() if coefficient * x}

    def multiply(self, left, right):
        result = {}
        for (i, j), x in left.items():
            for (k, ell), y in right.items():
                if i + j + k + ell <= self.order:
                    ij = (i + k, j + ell)
                    result[ij] = result.get(ij, self.K.zero) + x * y
        return {ij: coefficient for ij, coefficient in result.items() if coefficient}

    def power(self, value, exponent):
        result = self.constant(1)
        for _ in range(exponent):
            result = self.multiply(result, value)
        return result


def laurent(expression, z):
    numerator, denominator = sp.fraction(sp.cancel(expression))
    numerator = sp.Poly(numerator, z)
    denominator = sp.Poly(denominator, z)
    assert len(denominator.terms()) == 1
    degree, scalar = denominator.degree(), denominator.LC()
    return {
        exponent[0] - degree: sp.cancel(coefficient / scalar)
        for exponent, coefficient in numerator.terms()
    }


def moving_frames(K, r, s, z, order):
    J = Jet(K, order)
    delta = r - s
    alpha, beta = r + s * z, 1 + z
    u = J.add(J.scale(s / delta, J.m), J.scale(alpha, J.ell))
    v = J.add(J.scale(1 / delta, J.m), J.scale(beta, J.ell))
    a = v
    b = J.add(u, J.scale(K(3) / 2 * z, v))
    normalized_b = J.scale(z**-4, b)
    geometric_sum = J.constant(0)
    for exponent in range(order + 1):
        geometric_sum = J.add(
            geometric_sum, J.scale((-1)**exponent, J.power(normalized_b, exponent))
        )
    inverse = J.scale(z**-4, geometric_sum)
    W = J.multiply(J.add(J.constant(z**3), a), inverse)
    a_prime = J.add(J.scale(z, inverse), J.scale(-1, J.power(W, 3)))
    b_prime = J.add(inverse, J.scale(-1, J.power(W, 4)))
    u_prime = J.scale(K(1) / 2, a_prime)
    v_prime = J.add(J.scale(-3, J.multiply(W, a_prime)), J.scale(2, b_prime))
    m_v = J.add(
        J.multiply(J.add(J.scale(r, W), J.constant(s)), v_prime),
        J.scale(-1, J.multiply(J.add(W, J.constant(1)), u_prime)),
    )
    ell_v = J.scale(-1 / delta, J.add(u_prime, J.scale(-r, v_prime)))
    assert m_v[(1, 0)] == z**-8
    assert not m_v.get((0, 1), K.zero)
    assert ell_v[(0, 1)] == z**-6
    return J, W, m_v, ell_v


def third_obstruction(K, r, s, z, killing_chart):
    J, W, m_v, ell_v = moving_frames(K, r, s, z, 3)
    h2 = m_v[(0, 2)] / m_v[(1, 0)]
    h2_laurent = laurent(h2.as_expr(), z.as_expr())
    c1, c2, c3 = [K(h2_laurent.get(-i, 0)) for i in (1, 2, 3)]
    rank = c1 * c3 - c2**2
    if killing_chart == "c1":
        delta_u = 8 * (c2 - c1 * z)
    elif killing_chart == "c3":
        # This branch is used only after c1=c2=0 has been imposed.
        delta_u = 8 * c3
    else:
        raise ValueError(killing_chart)
    product = laurent((delta_u * h2).as_expr(), z.as_expr())
    gamma_u = K(-sum(value * z.as_expr()**i for i, value in product.items() if i >= 0))
    gamma_v = K(sum(value * z.as_expr()**(i + 3) for i, value in product.items() if i <= -3))

    def evaluate_at_moving_w(expression):
        result = {}
        for exponent, coefficient in laurent(expression.as_expr(), z.as_expr()).items():
            assert exponent <= 0
            result = J.add(result, J.scale(K(coefficient), J.power(W, -exponent)))
        return result

    delta_v = evaluate_at_moving_w(delta_u / z)
    gamma_v_jet = evaluate_at_moving_w(gamma_v)
    a_v = J.add(
        J.multiply(delta_v, m_v),
        J.scale(-1, J.multiply(gamma_v_jet, J.power(ell_v, 2))),
    )
    p = a_v[(1, 0)] / delta_u
    assert p == z**-9
    q_b = a_v.get((1, 1), K.zero)
    q_d = a_v.get((0, 3), K.zero)
    h3 = (q_b * gamma_u * delta_u + q_d * delta_u**2) / p
    h3_laurent = laurent(h3.as_expr(), z.as_expr())
    coordinates = [sp.factor(h3_laurent.get(-i, 0)) for i in range(1, 7)]
    return {
        "h2": h2, "c": (c1, c2, c3), "rank": rank,
        "delta": delta_u, "gamma_u": gamma_u, "gamma_v": gamma_v,
        "h3": h3, "coordinates": coordinates,
    }


K, r, s, z = field("r,s,z", sp.QQ)
Z, R, S = z.as_expr(), r.as_expr(), s.as_expr()
result = third_obstruction(K, r, s, z, "c1")
c1, c2, c3 = result["c"]
assert c1 == (2 * r + 12 * s**2 + 16 * s + 9) / 8
assert c2 == (2 * s + 1) * (8 * r + 12 * s**2 + 4 * s + 3) / 8
assert c3 == r * (2 * r + 36 * s**2 + 16 * s + 3) / 4
rank_polynomial = sp.fraction(result["rank"].as_expr())[0]
polynomials = [rank_polynomial] + [sp.fraction(x)[0] for x in result["coordinates"]]
basis = sp.groebner(polynomials, R, S)
eliminant = (2*S - 1)**3 * (2*S + 1)**3 * (12*S**2 + 20*S + 11)**3
assert sp.cancel(basis.polys[-1].as_expr() / eliminant).is_Number
# These ideals make the elimination exhaustive, without taking square roots
# or dropping projective/epimorphism boundaries silently.
expected = [
    (2*S - 1, [R**2 - 4*R + 4, 2*S - 1]),
    (2*S + 1, [R**3 + 4*R**2 + 4*R, 2*S + 1]),
    (12*S**2 + 20*S + 11, [R - 2*S - 1, 12*S**2 + 20*S + 11]),
]
for additional, generators in expected:
    actual = sp.groebner(polynomials + [additional], R, S, domain=sp.QQ)
    target = sp.groebner(generators, R, S, domain=sp.QQ)
    assert actual == target

# c1=0 and rank=0 imply c2=0.  The rank-zero point is (-2,-1/2);
# other points are q(S)=0,R=2S+1 and have c3 != 0.
r_on_c1_zero = -(12*S**2 + 16*S + 9) / 2
assert sp.simplify(
    c2.as_expr().subs(R, r_on_c1_zero)
    + 3 * (2 * S + 1) * (12 * S**2 + 20 * S + 11) / 8
) == 0
zero_point = {R: -2, S: -sp.Rational(1, 2)}
assert all(x.as_expr().subs(zero_point) == 0 for x in (c1, c2, c3))

# For c1 != 0 only two fourth-extension candidates remain.  The candidate
# (2,1/2) has rho=0 at the unique defect point and is not epimorphic.
first = {R: 2, S: sp.Rational(1, 2)}
h3_first = laurent(result["h3"].as_expr().subs(first), Z)
rho_first = -sum(value*Z**i for i, value in h3_first.items() if i >= 0)
assert result["delta"].as_expr().subs(first) == 24*(2-Z)
assert sp.expand(rho_first).subs(Z, 2) == 0

# Check the c3 chart at both quadratic parameter points.  This computation
# does not reuse the invalid zero killing section from the c1 chart.
Kq, sq, zq = field("s,z", sp.QQ)
quadratic = third_obstruction(Kq, 2*sq+1, sq, zq, "c3")
q = 12*sq.as_expr()**2 + 20*sq.as_expr() + 11
coefficient_field = sp.QQ.frac_field(zq.as_expr())
relation = sp.Poly(q, sq.as_expr(), domain=coefficient_field)

def reduce_quadratic(expression):
    numerator, denominator = sp.fraction(sp.cancel(expression))
    numerator = sp.Poly(numerator, sq.as_expr(), domain=coefficient_field).rem(relation)
    denominator = sp.Poly(denominator, sq.as_expr(), domain=coefficient_field).rem(relation)
    return sp.factor((numerator * sp.invert(denominator, relation)).rem(relation).as_expr())

assert reduce_quadratic(quadratic["c"][0].as_expr()) == 0
assert reduce_quadratic(quadratic["c"][1].as_expr()) == 0
h31 = reduce_quadratic(quadratic["coordinates"][0])
assert sp.simplify(h31 - 8192 * (2102 * sq.as_expr() + 3023) / 243) == 0
assert sp.gcd(q, 2102*sq.as_expr()+3023) == 1
assert sp.gcd(q, sp.fraction(reduce_quadratic(quadratic["c"][2].as_expr()))[0]) == 1

# Reconstruct the unique survivor and its moving quartic transition.
survivor = {R: 0, S: -sp.Rational(1, 2)}
assert result["delta"].as_expr().subs(survivor) == -4*Z
assert result["gamma_u"].as_expr().subs(survivor) == (3*Z**2+6*Z+4)/2
assert result["gamma_v"].as_expr().subs(survivor) == 0
h3_survivor = sp.expand(result["h3"].as_expr().subs(survivor))
assert h3_survivor == 36*Z**4+108*Z**3+136*Z**2+72*Z+16

Kf, zf = field("z", sp.QQ)
J, W, m_v, ell_v = moving_frames(Kf, Kf.zero, -Kf.one/2, zf, 4)
delta = -4*zf
gamma = (3*zf**2+6*zf+4)/2
rho = -(36*zf**4+108*zf**3+136*zf**2+72*zf+16)
# Solving E=delta^2*m-delta*gamma*ell^2-(rho/gamma)*m*ell=0
# through ell^4 gives this substitution.  The reference map to E4 sends
# m^2 to gamma^2, delta*m*ell-gamma*ell^3 to rho, ell^4 to delta^2.
substitution = {
    (0, 2): gamma/delta,
    (0, 3): rho/delta**3,
    (0, 4): rho**2/(gamma*delta**5),
}
reduced = {}
for (i, j), coefficient in m_v.items():
    reduced = J.add(reduced, J.scale(coefficient, J.multiply(J.power(substitution, i), J.power(J.ell, j))))
phi = -64*delta**2*reduced.get((0, 4), Kf.zero)
p = -64*m_v[(1, 0)]/delta**2
h4 = phi/p
Q = 3*zf**2+6*zf+4
P = 81*zf**8+486*zf**7+1341*zf**6+2160*zf**5+2204*zf**4+1464*zf**3+656*zf**2+224*zf+64
Rpoly = 81*zf**7+486*zf**6+1341*zf**5+2160*zf**4+2204*zf**3+1464*zf**2+608*zf+128
assert h4 == 2*P/(Q*zf)
assert P-16*Q == zf*Rpoly
assert h4-32/zf == 2*Rpoly/Q

print("PASS: dense type-B chart, all elimination boundaries, epimorphism and terminal obstruction independently rederived")
