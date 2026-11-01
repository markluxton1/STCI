"""Exact universal rank bound for the inherited nonendpoint conductor quadric.

Run with Python 3 and SymPy (validated with 1.14.0). The source substitution
is equation (5) of the October 12 nonendpoint restricted-conductor note.
The five source quadrics and the universal determinant are independently
audited there. This checks a polynomial identity with delta nonzero; it
does not check conductor integrality, singleton fibers, or mate descent.
"""

from itertools import combinations
import json
import sympy as sp


def conductor_quadric():
    x = sp.symbols("X0:4")
    h, z = sp.symbols("h z")
    delta = sp.Symbol("delta", nonzero=True)
    a, b, g, j = sp.symbols("a B G J")
    u3 = (x[0] - x[1] + b*h) / delta
    u2 = (x[2] - 3*x[1] + 2*x[0] - g*h + delta**3*z) / (3*delta**2)
    u0 = (x[3] - 2*x[2] + 2*x[1] - x[0] - j*h + 2*delta**3*z) / delta**4
    z0, z1, z2, z3, z4, z5 = x[0] - a*h - u3, -u3, h - u2, u2, z, u0
    quadrics = [z4*z4 - z3*z5, z2*z4 - z1*z5, z2*z3 - z1*z4,
                z2*z2 - z3*z4 - z0*z5, z1*z2 - z3*z3 - z0*z4]
    rows = [sp.Poly(sp.expand(q), h, z) for q in quadrics]
    center = sp.Matrix([[q.coeff_monomial(m) for m in (h*h, h*z, z*z)] for q in rows])
    linear = sp.Matrix([[q.coeff_monomial(m) for m in (h, z)] for q in rows])
    terms = []
    # Laplace expansion in the last two columns of [center | linear].
    # The zero-based row pair i,k has sign (-1)^(i+k+1).
    for i, k in combinations(range(5), 2):
        other_rows = [r for r in range(5) if r not in (i, k)]
        minor = sp.factor(center[other_rows, :].det(method="domain-ge"))
        terms.append((-1)**(i+k+1) * minor *
                     (linear[i, 0]*linear[k, 1] - linear[i, 1]*linear[k, 0]))
    poly = sp.Poly(sp.expand(sum(terms)), *x)
    return x, sp.Poly.from_dict({m: sp.factor(c) for m, c in poly.terms()}, *x)


if __name__ == "__main__":
    coordinates, quadric = conductor_quadric()
    if quadric.is_zero or any(sum(m) != 2 for m, _ in quadric.terms()):
        raise RuntimeError("Expected a nonzero homogeneous universal quadric")
    determinant = sp.factor(sp.hessian(quadric.as_expr(), coordinates).det(method="domain-ge"))
    if determinant != 0:
        raise RuntimeError("The universal conductor Hessian determinant is nonzero")
    print(json.dumps({"sympy_version": sp.__version__,
                      "parameter_field": "QQ(delta,a,B,G,J)",
                      "coordinate_domain": "delta != 0",
                      "quadric_monomials": len(quadric.terms()),
                      "hessian_determinant": str(determinant),
                      "scope": "rank at most three; no integrality or descent claim"}, indent=2))
