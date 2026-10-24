#!/usr/bin/env python3
"""Exact identities supporting the provisional special-lines/planes note.

Requires SymPy; e.g. /tmp/stci-z4-env/bin/python <this file>.
These checks supplement the geometric proofs. They neither construct an STCI
pair nor prove a universal obstruction. All coefficient extraction follows
full expansion. Output is deterministic JSON; no files are written here.
"""
import json
import sympy as S


def equal(a, b=0):
    assert S.cancel(S.expand(a - b)) == 0, S.factor(a - b)


x = S.symbols("x0:4")
x0, x1, x2, x3 = x
s, t, a, b, u, v, w, z, A, B, c, d = S.symbols(
    "s t a b u v w z A B c d")
nu = S.Matrix([s**4, s**3*t, s*t**3, t**4])
paired = nu.subs(t, -t)
q = x0*x3-x1*x2
R = x0*x2**2-x1**2*x3
f1 = x0**2*x2-x1**3
f3 = x1*x3**2-x2**3
F = f1+f3
checks = []


def record(name):
    checks.append({"name": name, "status": "PASS"})


# Uniqueness of Q: nine distinct exponent vectors, kernel exactly q.
mons = [x[i]*x[j] for i in range(4) for j in range(i, 4)]
coeff = S.Matrix([[S.expand(m.subs(dict(zip(x, nu)), simultaneous=True))
                   .coeff(t, k).coeff(s, 8-k) for m in mons]
                 for k in range(9)])
assert coeff.rank() == 9
equal(q.subs(dict(zip(x, nu)), simultaneous=True))
record("unique smooth containing quadric (rank nine)")

H = S.Matrix([-b**4, 2*a*b**3, -2*a**3*b, a**4])
equal(H.dot(nu), (a*t-b*s)**3*(a*t+b*s))
equal(H.dot(nu.subs(t, -t)), (a*t+b*s)**3*(a*t-b*s))
record("homogeneous osculating factorization and residual involution")

bit = S.Matrix([b**4/4, a*b**3, -2*a**3*b, a**4])
equal(bit.dot(nu), (a**2*t**2-a*b*s*t-b**2*s**2/2)**2)
quartic = S.Poly(S.expand((v-a)**2*(v-b)**2), v)
equal(quartic.coeff_monomial(v**2), a*a+4*a*b+b*b)
assert S.expand((a*a+4*a*b+b*b).subs(b, -a)) != 0
record("bitangent square family and non-involution partner equation")

# The dual discriminant: degree six, its four displayed singular components, and a
# simple-double-root smooth test. Exhaustiveness is proved geometrically in
# the note, not inferred from finitely many tests.
A0, B0, C0, D0 = S.symbols("A0 B0 C0 D0")
disc = S.discriminant(D0*z**4+C0*z**3+B0*z+A0, z)
assert S.Poly(disc, A0, B0, C0, D0).total_degree() == 6
for family in [(-u**4, 2*u**3, -2*u, 1), (u**4/4, u**3, -2*u, 1),
               (0, 0, a, b), (a, b, 0, 0)]:
    subs = dict(zip((A0, B0, C0, D0), family))
    equal(disc.subs(subs, simultaneous=True))
    for var in (A0, B0, C0, D0):
        equal(S.diff(disc, var).subs(subs, simultaneous=True))
smooth_subs = {A0:3, B0:-4, C0:0, D0:1}
equal(disc.subs(smooth_subs))
assert any(S.diff(disc, var).subs(smooth_subs) != 0
           for var in (A0, B0, C0, D0))
endpoint = S.groebner([u-w, 2*u**3-w**3, -u**4-w**4/4], u, w)
assert endpoint.reduce(w**3)[1] == 0
assert endpoint.reduce(w**2)[1] != 0
record("dual sextic: four singular components; osculating-bitangent endpoint length three")

P = S.Matrix([1, u, u**3, u**4])
Qp = S.Matrix([1, v, v**3, v**4])
lam, mu = S.symbols("lam mu")
equal(q.subs(dict(zip(x, lam*P+mu*Qp)), simultaneous=True),
      lam*mu*(u-v)**2*(u*u+u*v+v*v))
equal(q.subs(dict(zip(x, lam*P+mu*P.diff(u))), simultaneous=True),
      -3*u*u*mu*mu)
det = S.Matrix.hstack(P, P.diff(u), Qp, Qp.diff(v)).det()
equal(det, (u-v)**4*(u*u+4*u*v+v*v))
record("secant, tangent, and bitangent tangent-line determinant identities")

PairedLine = S.Matrix([A, B, z*B, z*z*A])
equal(R.subs(dict(zip(x, PairedLine)), simultaneous=True))
ha = S.Matrix([-u**4, 2*u**3, -2*u, 1])
for row in [P, P.subs(u, -u)]:
    equal(ha.dot(row))
gradient = S.Matrix([S.diff(R, xx) for xx in x])
for lhs, rhs in zip(gradient.subs(dict(zip(x, P)), simultaneous=True), -u*u*ha):
    equal(lhs, rhs)
equal(R.subs({x0:a*c, x1:a*d, x2:b*c, x3:b*d}, simultaneous=True),
      a*b*(b*c**3-a*d**3))
equal(R.subs({x0:1, x1:u, x2:u**3+v, x3:u**4+w}, simultaneous=True),
      u*u*(2*u*v-w)+v*v)
record("paired-secant cubic, osculating tangent planes, endpoint first symbols")
record("cubic-quadric residual divisor C plus endpoint trisecants")

pole = S.Matrix([1, 2*u, -2*u**3, -u**4])
equal(q.subs(dict(zip(x, pole)), simultaneous=True), 3*u**4)
equal(4*pole[0]*pole[3]-pole[1]*pole[2])
record("quadric polarity and distinct polar quartic")

# First-normal coincidence numerator: full homogeneous derivative expansion.
def D(poly):
    return S.expand(sum(S.diff(poly, xx).subs(dict(zip(x, nu)), simultaneous=True)
                        * yy for xx, yy in zip(x, paired)))

equal(D(q), 4*s**4*t**4)
equal(D(f1), 4*s**9*t**3)
equal(D(f3), 4*s**3*t**9)
equal(D(R))
equal(D(F), 4*s**3*t**3*(s**6+t**6))
gradF = S.Matrix([S.diff(F, xx) for xx in x]).subs(dict(zip(x, P)), simultaneous=True)
assert gradF[0] == 2*u**3 and gradF[2].subs(u, 0) == 1
assert S.diff(F, x1).subs({x0:0, x1:0, x2:0, x3:1}) == 1
assert S.gcd(S.Poly(u**6+1, u), S.Poly(6*u**5, u)).degree() == 0
equal(F.subs({x0:a*c, x1:a*d, x2:b*c, x3:b*d}, simultaneous=True),
      (a*a-b*b)*(b*c**3-a*d**3))
record("smooth-along-C cubic with six simple osculating coincidences")
record("proper common-normal pair (F,x0F+q^2) has explicit residual rulings")

# Two plane CIs of the same length need not have the same tangent scheme.
X, T = S.symbols("X T")
for r in (2, 3, 4):
    for m in (1, 2, 3, 5):
        GB = S.groebner([X, X+(-T**r)**m], X, T)
        equal(GB.reduce(T**(r*m))[1])
        assert GB.reduce(T**(r*m-1))[1] != 0
record("local smooth-surface models realize lengths rm for r=2,3,4")

print(json.dumps({
    "status": "PASS", "sympy_version": S.__version__,
    "scope": "displayed exact identities only; no STCI existence or exclusion",
    "checks": checks,
    "osculating_normal_test": {
        "surface": str(F), "coincidences": "s^6+t^6=0 (six simple points)",
        "pair": "(F, x0*F+q^2)",
        "residual": "two trisecant ruling lines a=b and a=-b on Q",
        "sole_support": False
    }
}, indent=2))
