#!/usr/bin/env python3
"""Exact checks for the monomial rational quartic STCI constructions."""

from math import comb
import sympy as sp

s, t = sp.symbols("s t")
x0, x1, x2, x3, u = sp.symbols("x0 x1 x2 x3 u")
xs = (x0, x1, x2, x3)

A = x0**2 * x2 - x1**3
B = x0 * x2**2 - x1**2 * x3
Q = x0 * x3 - x1 * x2
C = x1 * x3**2 - x2**3
IGENS = (A, B, Q, C)


def poly_mod(expr, p, variables=xs):
    return sp.Poly(sp.expand(expr), *variables, modulus=p).as_expr()


def gb(gens, p, order="grevlex"):
    return sp.groebner(gens, *xs, modulus=p, order=order)


def same_ideal(left, right, p):
    gl = gb(left, p)
    gr = gb(right, p)
    return all(gl.reduce(f)[1] == 0 for f in right) and all(
        gr.reduce(f)[1] == 0 for f in left
    )


def saturate_by_one(gens, f, p):
    """Return I:f^infinity by elimination of 1-u*f."""
    big = sp.groebner([*gens, 1 - u * f], u, *xs, modulus=p, order="lex")
    eliminated = [g.as_expr() for g in big.polys if not g.as_expr().has(u)]
    return [g.as_expr() for g in gb(eliminated, p).polys]


def homogeneous_degree(expr):
    degrees = {sum(monomial) for monomial, _ in sp.Poly(expr, *xs).terms()}
    assert len(degrees) == 1
    return degrees.pop()


def vanishes_on_parametrization(expr, p):
    image = sp.expand(
        expr.subs({x0: s**4, x1: s**3 * t, x2: s * t**3, x3: t**4})
    )
    return sp.Poly(image, s, t, modulus=p).is_zero


def min_power_in_ideal(expr, ideal_gb, bound):
    for exponent in range(1, bound + 1):
        if ideal_gb.reduce(expr**exponent)[1] == 0:
            return exponent
    return None


def uniform_g(p, e):
    """Construct G_e; e must be divisible by both 3 and p."""
    assert e % 3 == 0 and e % p == 0
    degree = 4 * e // 3
    result = 0
    for j in range(e + 1):
        n = 4 * (e - j)
        b = n % 3
        c = (n - b) // 3
        a = degree - b - c - j
        coefficient = (-1) ** (e - j) * comb(e, j)
        if a < 0:
            assert j == 1 and coefficient % p == 0
            continue
        result += coefficient * x0**a * x1**b * x2**c * x3**j
    return poly_mod(result, p)


print("1. ELIMINATION IDEAL")
elimination_qq = sp.groebner(
    [x0 - s**4, x1 - s**3 * t, x2 - s * t**3, x3 - t**4],
    s,
    t,
    *xs,
    order="lex",
)
kernel_qq = [
    g.as_expr()
    for g in elimination_qq.polys
    if not (g.as_expr().has(s) or g.as_expr().has(t))
]
ideal_qq = sp.groebner(IGENS, *xs, order="grevlex")
kernel_gb_qq = sp.groebner(kernel_qq, *xs, order="grevlex")
assert all(ideal_qq.reduce(f)[1] == 0 for f in kernel_qq)
assert all(kernel_gb_qq.reduce(f)[1] == 0 for f in IGENS)
for p in (2, 3, 5):
    elimination = sp.groebner(
        [x0 - s**4, x1 - s**3 * t, x2 - s * t**3, x3 - t**4],
        s,
        t,
        *xs,
        modulus=p,
        order="lex",
    )
    kernel = [
        g.as_expr()
        for g in elimination.polys
        if not (g.as_expr().has(s) or g.as_expr().has(t))
    ]
    assert same_ideal(kernel, IGENS, p)
print("  parametrization kernel verified over QQ and GF(2), GF(3), GF(5)")


print("2. SPECIAL PAIRS")
special_pairs = {
    2: (x1**4 - x0**3 * x3, x2**4 - x0 * x3**3),
    3: (x1**3 - x0**2 * x2, x0 * x3**3 - x2**4),
}
for p, raw_pair in special_pairs.items():
    pair = tuple(poly_mod(f, p) for f in raw_pair)
    pair_gb = gb(pair, p)
    ideal_gb = gb(IGENS, p)
    assert all(vanishes_on_parametrization(f, p) for f in pair)
    assert all(ideal_gb.reduce(f)[1] == 0 for f in pair)
    powers = {
        name: min_power_in_ideal(f, pair_gb, 24)
        for name, f in zip(("A", "B", "Q", "C"), IGENS)
    }
    assert all(power is not None for power in powers.values())
    assert pair_gb.reduce(Q)[1] != 0
    coordinate_saturations = {
        str(variable): same_ideal(pair, saturate_by_one(pair, variable, p), p)
        for variable in xs
    }
    assert all(coordinate_saturations.values())
    print(f"  characteristic {p}: radical power certificates {powers}")


print("3. UNIFORM FROBENIUS FAMILY")
for p in (2, 3, 5, 7):
    e = 3 if p == 3 else 3 * p
    degree = 4 * e // 3
    ge = uniform_g(p, e)
    assert homogeneous_degree(ge) == degree
    assert vanishes_on_parametrization(ge, p)
    principal_gb = gb((A,), p)
    assert principal_gb.reduce(Q**e - x0 ** (2 * e // 3) * ge)[1] == 0
    boundary = poly_mod(ge.subs({x0: 0, x1: 0}), p, (x2, x3))
    expected = poly_mod((-1) ** e * x2**degree, p, (x2, x3))
    assert boundary == expected and boundary != 0

    pair = (poly_mod(A, p), ge)
    pair_gb = gb(pair, p)
    assert all(pair_gb.reduce(f**e)[1] == 0 for f in IGENS)
    assert all(
        same_ideal(pair, saturate_by_one(pair, variable, p), p)
        for variable in xs
    )
    print(
        f"  characteristic {p}: e={e}, degree={degree}, "
        f"terms={len(sp.Poly(ge, *xs).terms())}"
    )


print("4. WRONG-CHARACTERISTIC SANITY CHECKS")
point_3 = {x0: 1, x1: 1, x2: 1, x3: 2}
assert all(int(f.subs(point_3)) % 7 == 0 for f in special_pairs[3])
assert int(Q.subs(point_3)) % 7 != 0
point_2 = {x0: 1, x1: 1, x2: 4, x3: 1}
assert all(int(f.subs(point_2)) % 5 == 0 for f in special_pairs[2])
assert int(A.subs(point_2)) % 5 != 0
print("  special equations fail outside their intended characteristics")

print("ALL ASSERTIONS PASSED")
