#!/usr/bin/env python3
"""Exact mate-independent exclusions of e=0 first defects 1 and 2 on C0.

Derive the moving-chart quadratic cocycle, its divisor-clearing matrices,
and the complete triple-compatible quartic space. Characteristic zero.
See research/notes/2026-10-05-mf6-further-audit.md.
"""
import sympy as s

z, eps, theta = s.symbols("z eps theta", nonzero=True)


def quadratic_cocycle(u, v, quotient):
    a = v
    b = u + s.Rational(3, 2) * z * v
    W = (z**3 + a) / (z**4 + b)
    ap = z / (z**4 + b) - W**3
    bp = 1 / (z**4 + b) - W**4
    up = ap / 2
    vp = -3 * W * ap + 2 * bp
    expr = quotient(up, vp)
    return s.expand(s.series(expr, eps, 0, 3).removeO()).coeff(eps, 2) * z**7


h2 = s.expand(quadratic_cocycle(-theta * eps, eps, lambda up, vp: up + theta * vp))
hinf = s.expand(quadratic_cocycle(eps, 0, lambda up, vp: vp))
assert h2 == 3 * theta**3 / z**5 - s.Rational(3, 2) * theta**2 / z**4 + s.Rational(3, 4) * theta / z**3 - s.Rational(3, 8) / z**2
assert hinf == 3 / z**5


def killing_matrix(cocycle, degree):
    # H^1(O(-7+degree)) has Laurent coordinates z^-1,...,z^(-6+degree).
    return s.Matrix([
        [s.expand(z**j * cocycle).coeff(z, -i) for j in range(degree + 1)]
        for i in range(1, 7 - degree)
    ])


K1 = killing_matrix(h2, 1)
assert s.factor(K1[[0, 1], :].det()) == -s.Rational(9, 64)
assert killing_matrix(hinf, 1).rank() == 2
K2 = killing_matrix(h2, 2)
assert s.factor(K2[[0, 1, 3], :].det()) == -s.Rational(27, 32) * theta**4
assert K2.subs(theta, 0).nullspace() == [s.Matrix([0, 0, 1])]
assert killing_matrix(hinf, 2).nullspace() == [s.Matrix([1, 0, 0])]
# At theta=0: delta_U=z^2, gamma_U=3/8, gamma_V=0.
assert s.expand(z**2 * h2.subs(theta, 0) + s.Rational(3, 8)) == 0
# At infinity: delta_U=1, delta_V=w^2, gamma_U=0, gamma_V=3.
assert hinf == 3 * z**-5

x0, x1, x2, x3, U, V = s.symbols("x0 x1 x2 x3 U V")
xs = (x0, x1, x2, x3)
q = x0*x3-x1*x2
A = x0**2*x2-x1**3
B = x0*x2**2-x1**2*x3
D = x2**3-x1*x3**2


def monomials(degree):
    return [x0**i*x1**j*x2**k*x3**(degree-i-j-k)
            for i in range(degree, -1, -1)
            for j in range(degree-i, -1, -1)
            for k in range(degree-i-j, -1, -1)]


def vectors(forms, degree):
    return s.Matrix.hstack(*[s.Matrix([s.Poly(f, *xs).coeff_monomial(m)
                                      for m in monomials(degree)]) for f in forms])


generators = [q*m for m in monomials(2)] + [f*x for f in (A, B, D) for x in xs]
I4 = [s.expand(generators[i]) for i in vectors(generators, 4).rref()[1]]
assert len(I4) == 18
sub = {x0: 1, x1: z, x2: z**3 + V, x3: z**4 + U + s.Rational(3, 2)*z*V}
jets = [s.Poly(s.expand(f.subs(sub)), U, V) for f in I4]
pure_U_matrix = s.Matrix([[j.coeff_monomial(V).coeff(z, i) for j in jets] for i in range(10)])
pure_U = [s.expand(sum(c*I4[i] for i, c in enumerate(v))) for v in pure_U_matrix.nullspace()]
assert len(pure_U) == 8
pure_jets = [s.Poly(s.expand(f.subs(sub)), U, V) for f in pure_U]
errors = [s.expand(z**2*j.coeff_monomial(V**2) + s.Rational(3, 8)*j.coeff_monomial(U)) for j in pure_jets]
triple_matrix = s.Matrix([[e.coeff(z, i) for e in errors] for i in range(12)])
compatible = [s.expand(sum(c*pure_U[i] for i, c in enumerate(v))) for v in triple_matrix.nullspace()]
assert len(compatible) == 4
expected = [x*D for x in xs]
assert vectors(compatible + expected, 4).rank() == 4
assert vectors(expected, 4).rank() == 4
# Direct second pure direction: m=V, ell=U, delta_U=1,gamma_U=0.
linear_U_matrix = s.Matrix([[j.coeff_monomial(U).coeff(z, i) for j in jets] for i in range(10)])
quadratic_U_matrix = s.Matrix([[j.coeff_monomial(U**2).coeff(z, i) for j in jets] for i in range(12)])
other_compatible = [s.expand(sum(c*I4[i] for i,c in enumerate(v)))
                    for v in linear_U_matrix.col_join(quadratic_U_matrix).nullspace()]
assert len(other_compatible)==4
assert vectors(other_compatible + [x*A for x in xs],4).rank()==4
# Exact degree-five warning: pure-U triples need not have a common zero.
delta5 = 1
gamma5_U = 0
gamma5_V = -s.Rational(3,8)
assert s.expand(delta5*h2.subs(theta,0)+gamma5_U-z**-2*gamma5_V)==0
survivor5 = -2*x0**3*x3+3*x0**2*x1*x2-x1**4
survivor5_jet = s.Poly(s.expand(survivor5.subs(sub)),U,V)
assert survivor5_jet.coeff_monomial(V)==0
assert survivor5_jet.coeff_monomial(V**2)==0

print("PASS: degree-one first defect impossible on all quotient charts")
print("PASS: degree-two first defect forces one of two pure endpoint triples")
print("PASS: every compatible quartic equals D times an ambient linear form")
print("RESULT: every hypothetical characteristic-zero (4,b) pair on C0 with e=0 has deg D2>=3")
