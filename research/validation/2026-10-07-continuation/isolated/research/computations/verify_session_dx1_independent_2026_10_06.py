#!/usr/bin/env python3
"""Independent rational audit of the dx=1 residual calculation.

Two complementary checks:
* expand the persisted Macaulay2 membership certificate with SymPy over QQ;
* certify a real algebraic zero of the insufficient three-equation subsystem
  using exact rational interval arithmetic and a contraction/Brouwer argument.

No floating point arithmetic is used for assertions. Displayed decimals are
only summaries of proved rational inequalities.
"""
from fractions import Fraction as F
from pathlib import Path
import re
import sympy as sp

HERE = Path(__file__).resolve().parent
a, b, x, u = sp.symbols("a b x u")
symbols = {str(v): v for v in (a, b, x, u)}


def read_definitions():
    """Read the polynomials, not the CAS instructions or output."""
    source = (HERE / "session_dx1_saturation_2026_10_06.m2").read_text()
    result = {}
    for name, expression in re.findall(r"^(R2|R4|Q[1-5])=(.*);$", source, re.M):
        result[name] = sp.Poly(
            sp.sympify(expression.replace("^", "**"), locals=symbols),
            a, b, x, domain=sp.QQ,
        )
    assert set(result) == {"R2", "R4", "Q1", "Q2", "Q3", "Q4", "Q5"}
    return result


def verify_membership(polys):
    """Parse the external matrix and multiply it in an independent engine."""
    raw = (HERE / "session_dx1_saturation_certificate_2026_10_06.txt").read_text()
    raw = raw.split("R^{{-10}},", 1)[1].strip()
    assert raw.startswith("{{") and raw.endswith("}})")
    entries = re.split(r"\}\s*,\s*\{", raw[2:-3])
    assert len(entries) == 5
    coefficients = [
        sp.Poly(sp.sympify(v.replace("^", "**"), locals=symbols), a, b, x, domain=sp.QQ)
        for v in entries
    ]
    s = sp.Poly(x * (b*x-a) * (2*a+1) * (b+2), a, b, x, domain=sp.QQ)
    difference = sum(
        (polys[f"Q{i+1}"] * coefficients[i] for i in range(5)),
        sp.Poly(0, a, b, x, domain=sp.QQ),
    ) - s**2
    assert difference.is_zero
    assert (polys["Q2"] - sp.Poly((2*a+1), a,b,x)*polys["R2"]).is_zero
    assert (polys["Q4"] - sp.Poly(2*(b+2), a,b,x)*polys["R4"]).is_zero
    print("PASS: exact independent QQ expansion of sum(Q_i C_i)=s^2.")
    print("Certificate coefficient term counts:", [len(c.terms()) for c in coefficients])


def rational(q):
    q = sp.Rational(q)
    return F(int(q.p), int(q.q))


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def neg(z):
    return (-z[1], -z[0])


def mul(z, w):
    values = [z[i]*w[j] for i in range(2) for j in range(2)]
    return (min(values), max(values))


def power(z, n):
    answer = (F(1), F(1))
    for _ in range(n):
        answer = mul(answer, z)
    return answer


def polynomial_interval(poly, box):
    answer = (F(0), F(0))
    for exponents, coefficient in poly.terms():
        c = rational(coefficient)
        term = (c, c)
        for coordinate, exponent in zip(box, exponents):
            term = mul(term, power(coordinate, exponent))
        answer = add(answer, term)
    return answer


def magnitude(z):
    return max(abs(z[0]), abs(z[1]))


def transform(poly):
    numerator, denominator = sp.fraction(sp.cancel(poly.as_expr().subs(b, (a+u)/x)))
    assert sp.Poly(denominator, x).terms() == [((sp.degree(denominator,x),), sp.LC(sp.Poly(denominator,x)))]
    return sp.Poly(numerator, a, u, x, domain=sp.QQ)


def verify_subsystem_survivor(polys):
    # Exact decimal rationals. The initial guess was obtained with nsolve;
    # existence/uniqueness below depends only on these rational data.
    center = [
        F("-0.199499192681611878608445711923"),
        F("0.190901045508013354512168855298"),
        F("-0.366729879371914138346593229175"),
    ]
    radius = F(1, 10**10)
    box = [(c-radius, c+radius) for c in center]
    subsystem = [transform(polys[n]) for n in ("R2", "R4", "Q5")]
    expressions = sp.Matrix([p.as_expr() for p in subsystem])
    jacobian = expressions.jacobian((a,u,x))
    point = dict(zip((a,u,x), map(sp.Rational, center)))
    inverse = jacobian.subs(point).inv()
    assert inverse.det() != 0
    inverse = [[rational(inverse[i,j]) for j in range(3)] for i in range(3)]
    fcenter = [rational(f.subs(point)) for f in expressions]
    hcenter = [-sum(inverse[i][j]*fcenter[j] for j in range(3)) for i in range(3)]
    jbox = [
        [polynomial_interval(sp.Poly(jacobian[i,j], a,u,x), box) for j in range(3)]
        for i in range(3)
    ]
    error = []
    for i in range(3):
        row = []
        for j in range(3):
            v = (F(int(i==j)), F(int(i==j)))
            for k in range(3):
                v = add(v, neg(mul((inverse[i][k],inverse[i][k]), jbox[k][j])))
            row.append(v)
        error.append(row)
    contraction = max(sum(magnitude(v) for v in row) for row in error)
    image_bounds = [abs(hcenter[i]) + sum(magnitude(v)*radius for v in error[i]) for i in range(3)]
    assert contraction < 1
    assert all(v < radius for v in image_bounds)
    # T(y)=y-C f(y) maps this closed cube to its interior and contracts it.
    # Its unique fixed point is a zero because C is invertible.
    open_factors = [x, u, 2*a+1, a+u+2*x]
    bounds = [polynomial_interval(sp.Poly(f,a,u,x),box) for f in open_factors]
    assert all(lo > 0 or hi < 0 for lo,hi in bounds)
    omitted_bounds = [polynomial_interval(transform(polys[n]), box) for n in ("Q1", "Q3")]
    assert all(lo > 0 or hi < 0 for lo,hi in omitted_bounds)
    # A conservative report using exact comparisons, with convenient bounds.
    assert contraction < F(1,10**4)
    assert max(image_bounds) < F(1,10**14)
    print("PASS: exact rational cube gives a unique real zero of R2,R4,Q5.")
    print("Center (a,u,x):", [str(c) for c in center])
    print("Cube radius: 1e-10; derivative contraction < 1e-4; image radius < 1e-14.")
    print("Open-factor intervals:", [(float(lo),float(hi)) for lo,hi in bounds])
    print("Omitted Q1,Q3 numerator intervals:", [(float(lo),float(hi)) for lo,hi in omitted_bounds])
    print("These displayed decimals summarize exact rational interval checks.")


if __name__ == "__main__":
    polynomials = read_definitions()
    verify_membership(polynomials)
    verify_subsystem_survivor(polynomials)
