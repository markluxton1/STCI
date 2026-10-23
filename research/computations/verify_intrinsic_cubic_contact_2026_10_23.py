#!/usr/bin/env python3
"""Exact checks for the provisional intrinsic cubic-contact construction.

Requires SymPy. Run, for example:
    /tmp/stci-z4-env/bin/python research/computations/verify_intrinsic_cubic_contact_2026_10_23.py

This checks the displayed identities, module presentation, and local blowup
formulas. It does not prove global quartic-source nonvanishing or an STCI
exclusion. The mathematical argument for the module presentation uses the
Hilbert--Burch theorem after checking its minors and height-two hypothesis.
"""

import sympy as s


def equal(left, right=0):
    residual = s.cancel(s.expand(left - right))
    if residual != 0:
        raise AssertionError(residual)


def check_defect_module():
    a, x, y = s.symbols("a x y")
    f, g, h = x**2 - a*y, x*y, y**2
    syzygy_matrix = s.Matrix([[y, 0], [-x, y], [a, -x]])
    generators = s.Matrix([[f, g, h]])
    for entry in generators * syzygy_matrix:
        equal(entry)
    equal(syzygy_matrix.extract([0, 1], [0, 1]).det(), h)
    equal(syzygy_matrix.extract([0, 2], [0, 1]).det(), -g)
    equal(syzygy_matrix.extract([1, 2], [0, 1]).det(), f)

    # Modulo I=(x,y), the presentation leaves precisely the relation a*h=0.
    reduced_matrix = syzygy_matrix.subs({x: 0, y: 0})
    assert reduced_matrix == s.Matrix([[0, 0], [0, 0], [a, 0]])

    # Independent ideal reduction checks that a*h belongs to I*J, while
    # f,g,h themselves survive; the presentation above proves no further
    # O_C-linear relations beyond the displayed torsion relation.
    products = [x*f, y*f, x*g, y*g, x*h, y*h]
    groebner = s.groebner(products, x, y, a, order="lex")
    equal(groebner.reduce(a*h)[1])
    assert groebner.reduce(f)[1] != 0
    assert groebner.reduce(g)[1] != 0
    assert groebner.reduce(h)[1] != 0
    print("PASS: defect Hilbert--Burch identities and torsion presentation")


def check_contact_and_blowups():
    m, n, t, u = s.symbols("m n t u")
    f2, h, e, c, b20, b12, b21, b30 = s.symbols(
        "f2 h e c b20 b12 b21 b30"
    )
    k = -h*f2
    H = (h*m + k*t**2 + e*m*t + c*t**3 + b20*m**2
         + b12*m*t**2 + b21*m**2*t + b30*m**3)

    # A general cubic Taylor polynomial includes m^2 and m*t^2 terms.
    # In M=(n,t^3)/(n^2,n*t,t^4) they do not affect cubic contact.
    expanded = s.Poly(s.expand(H.subs(m, n + f2*t**2)), n, t)
    reduced = 0
    for (n_degree, t_degree), coefficient in expanded.terms():
        if n_degree >= 2 or (n_degree >= 1 and t_degree >= 1) or t_degree >= 4:
            continue
        reduced += coefficient*n**n_degree*t**t_degree
    equal(reduced, h*n + (c + e*f2)*t**3)

    # Two successive blowup charts m=t*m1 and m1=t*m2, then m2=f2+u.
    transformed = s.Poly(s.expand(H.subs(m, t**2*(u + f2))/t**2), u, t)
    tangent = sum(coefficient*u**i*t**j
                  for (i, j), coefficient in transformed.terms() if i+j <= 1)
    equal(tangent, h*u + (c + e*f2)*t)
    print("PASS: cubic contact reduction and twice-blown-up tangent matrix")


def check_determinant_transformations():
    h0, h1, tau0, tau1, a, b, d, r = s.symbols(
        "h0 h1 tau0 tau1 a b d r"
    )
    delta = h0*tau1 - h1*tau0
    hp0, hp1 = h0/a, h1/a
    tp0, tp1 = (tau0 - b*h0/a)/d**3, (tau1 - b*h1/a)/d**3
    equal(hp0*tp1 - hp1*tp0, delta/(a*d**3))
    equal(h0*(tau1+r*h1) - h1*(tau0+r*h0), delta)

    p, q, r0, v = s.symbols("p q r0 v")
    generator_change = s.Matrix([[p, q], [r0, v]])
    contact = s.Matrix([[h0, tau0], [h1, tau1]])
    equal((generator_change*contact).det(), generator_change.det()*delta)
    print("PASS: adapted-coordinate, fourth-lift, and generator transformations")


if __name__ == "__main__":
    check_defect_module()
    check_contact_and_blowups()
    check_determinant_transformations()
    print("PASS: intrinsic cubic-contact identities (no global nonvanishing claim)")
