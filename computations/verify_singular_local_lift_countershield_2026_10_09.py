#!/usr/bin/env python3
"""Exact identities for the singular-normalization local countershield.

Geometric conclusions and their hypotheses are proved in the paired note.
This script checks their literal polynomial certificates, not normality or
the global degree-four C0 problem by symbolic fiat.
"""
import json
import sympy as sp

x, g, v, y, w, t = sp.symbols("x g v y w t")
R = v**2 - 4*x*g
GB = sp.groebner([R], v, g, x, order="lex")

def zero_mod_B(poly):
    assert sp.expand(GB.reduce(sp.expand(poly))[1]) == 0

F = (w + (x-g)**2)**2 - 4*(x+g)**2*w
Fh = (w*t + (x-g)**2)**2 - 4*(x+g)**2*w*t
Y = x+g+v
W = Y**2
zero_mod_B(Y**2 - 2*(x+g)*Y + (x-g)**2)
zero_mod_B(F.subs(w, W))
zero_mod_B(2*(x+g)*Y - W - (x-g)**2)
assert sp.factor(sp.discriminant(F, w)) == 64*x*g*(x+g)**2
assert sp.expand(F.subs(g, 0) - (w-x**2)**2) == 0
assert sp.expand(Fh.subs(t, 1) - F) == 0
assert sp.expand(Fh.subs(g, 0) - (w*t-x**2)**2) == 0
assert sp.Poly(Fh, x, g, w, t).is_homogeneous
assert sp.Poly(Fh, x, g, w, t).total_degree() == 4

gradient_on_C = [sp.factor(sp.diff(F, a).subs({g: 0, w: x**2}))
                 for a in (x, g, w)]
assert gradient_on_C == [0, -16*x**3, 0]
assert [sp.diff(R, a) for a in (x, g, v)] == [-4*g, -4*x, 2*v]

# Full inverse-support certificate: v^2 belongs to (g), and the pulled
# back second curve equation is in (g,v). No elimination saturation is
# used to conceal additional branches.
zero_mod_B(W - x**2 - 2*x*v - g*(6*x+g+2*v))
assert sp.expand(W.subs({g: 0, v: 0}) - x**2) == 0

# A pair of linearly independent degree-one prime-ideal generators
# cannot lie in mP: mP has degree at least two in this graded local model.
assert sp.Poly(R, x, g, v).total_degree() == 2
assert sp.Poly(R, x, g, v).is_homogeneous
assert sp.Poly(g, x, g, v).total_degree() == 1
assert sp.Poly(v, x, g, v).total_degree() == 1

print(json.dumps({
    "status": "PASS",
    "scope": "literal polynomial certificates for a local singular-normalization countershield",
    "affine_hypersurface_degree": sp.Poly(F, x, g, w).total_degree(),
    "projective_hypersurface_degree": sp.Poly(Fh, x, g, w, t).total_degree(),
    "discriminant_in_w": str(sp.factor(sp.discriminant(F, w))),
    "gradient_on_C": [str(a) for a in gradient_on_C],
    "projective_plane_restriction": str(sp.factor(Fh.subs(g, 0))),
    "normalization_equation": str(R),
    "fraction_recovery": "y=(w+(x-g)^2)/(2(x+g)); v=y-x-g",
    "excluded_claims": ["fixed degree-four C0 mate", "universal STCI resolution", "smoothness of all normalizations"]
}, indent=2))
