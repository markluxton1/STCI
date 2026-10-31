#!/usr/bin/env python3
"""Exact first-root compatibility slice inside actual octic sources.

Diagnostic at the accepted smooth seed in the movement-two root model.
Expands every homogeneous octic in the balanced x0=1 chart, imposes
vanishing through normal order one, then imposes the seed first-lift
equation through normal order three. Rational linear algebra only.
This is a one-chart necessary filter; no global root-lifting equivalence
or STCI conclusion is asserted by this script.
"""
from fractions import Fraction as F
import json
import sympy as sp

# Sparse normal polynomial (u exponent, v exponent, z exponent) -> Q.
Poly = dict[tuple[int, int, int], F]


def clean(p):
    return {m: c for m, c in p.items() if c}


def add(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, F(0)) + c
    return clean(out)


def scale(p, c):
    return clean({m: c * v for m, v in p.items()})


def mul(p, q, max_normal=3):
    out = {}
    for (i, j, k), a in p.items():
        for (r, s, t), b in q.items():
            if i + j + r + s <= max_normal:
                key = (i + r, j + s, k + t)
                out[key] = out.get(key, F(0)) + a * b
    return clean(out)


def power(p, e, max_normal=3):
    out = {(0, 0, 0): F(1)}
    for _ in range(e):
        out = mul(out, p, max_normal=max_normal)
    return out


def monomials(total):
    """Exponent tuples (x0,x1,x2,x3) of total homogeneous degree."""
    return [(total-b-c-d, b, c, d)
            for b in range(total + 1)
            for c in range(total - b + 1)
            for d in range(total - b - c + 1)]


def expand_octic(mono, max_normal=3):
    _, b, c, d = mono
    z = {(0, 0, 1): F(1)}
    u = {(1, 0, 0): F(1)}
    v = {(0, 1, 0): F(1)}
    x1 = z
    x2 = add(power(z, 3, max_normal), v)
    x3 = add(power(z, 4, max_normal), u,
             scale(mul(z, v, max_normal), F(3, 2)))
    return mul(mul(power(x1, b, max_normal),
                   power(x2, c, max_normal), max_normal=max_normal),
               power(x3, d, max_normal), max_normal=max_normal)


def normal_keys(poly, order):
    return sorted({(i, j, k) for i, j, k in poly if i + j == order})


def matrix_for(keys, columns):
    return sp.Matrix([[col.get(key, F(0)) for col in columns]
                      for key in keys])


def as_poly(coeffs, start=0):
    return sp.Poly.from_dict({(i + start,): c for i, c in enumerate(coeffs)
                              if c}, sp.Symbol("z"), domain=sp.QQ)


def gcd_with_infinity(polys, degree):
    """Homogeneous gcd degree on P1, including the point at infinity."""
    z = sp.Symbol("z")
    gcd = None
    infinity_order = degree
    for coefficients in polys:
        p = as_poly(coefficients)
        gcd = p if gcd is None else sp.gcd(gcd, p)
        deg = p.degree() if not p.is_zero else -1
        infinity_order = min(infinity_order, degree - deg)
    if gcd is None:
        return {"all_zero": True, "finite_gcd": "0", "infinity_order": degree}
    return {"all_zero": gcd.is_zero,
            "finite_gcd": str(gcd.as_expr()),
            "finite_gcd_degree": max(0, gcd.degree()) if not gcd.is_zero else None,
            "infinity_order": infinity_order,
            "homogeneous_common_divisor_degree":
                (max(0, gcd.degree()) if not gcd.is_zero else 0) + infinity_order}


def basepoint_free_pair(alpha_basis, degree):
    """Find two multipliers with no common zero on P1, if present."""
    candidates = list(alpha_basis)
    for i in range(min(12, len(alpha_basis))):
        for j in range(i + 1, min(12, len(alpha_basis))):
            candidates.append([a + b for a, b in zip(alpha_basis[i], alpha_basis[j])])
    for i, first in enumerate(candidates):
        for second in candidates[i + 1:]:
            common = gcd_with_infinity([first, second], degree)
            if common["homogeneous_common_divisor_degree"] == 0:
                return [str(as_poly(first).as_expr()), str(as_poly(second).as_expr())]
    return None


def normal_component(poly, order):
    u, v = sp.symbols("u v")
    return sp.expand(sum(sp.Rational(c.numerator, c.denominator) * u**i * v**j
                         for (i, j, k), c in poly.items()
                         if i + j == order and k == 0))


def chart_expansion_from_homogeneous(coefficients, expansions):
    result = {}
    for coefficient, expansion in zip(coefficients, expansions):
        if coefficient:
            result = add(result, scale(expansion, F(coefficient)))
    return result


def pair_certificate(pair_coefficients, source_monomials):
    """Recompute ambient gcd and the seed's quartic relation at z=0."""
    x0, x1, x2, x3, u, v = sp.symbols("x0 x1 x2 x3 u v")
    homogeneous = []
    for coefficients in pair_coefficients:
        form = sum(sp.Rational(coefficient.numerator, coefficient.denominator) *
                   x0**a * x1**b * x2**c * x3**d
                   for (a, b, c, d), coefficient
                   in zip(source_monomials, coefficients))
        homogeneous.append(sp.Poly(form, x0, x1, x2, x3, domain=sp.QQ))
    ambient_gcd = sp.gcd(*homogeneous)

    # At z=0, f0=4u^2-8v^2 and G0=-3/4*u*v^2. Divide the residual
    # cubic exactly to recover the correction linear forms l_F,l_G.
    chart_four = [expand_octic(m, max_normal=4) for m in source_monomials]
    charts = [chart_expansion_from_homogeneous(coeffs, chart_four)
              for coeffs in pair_coefficients]
    f0 = 4*u**2 - 8*v**2
    g00 = -sp.Rational(3, 4) * u * v**2
    alpha, beta = [normal_component(p, 2).coeff(u, 2) / 4 for p in charts]
    # Directly derive both multipliers from the u^2 coefficient of F2,G2;
    # checking the full binary quadratics below guards the proportionality.
    quadratic_matches = [sp.expand(normal_component(p, 2) - a*f0) == 0
                         for p, a in zip(charts, (alpha, beta))]
    f3, g3 = [normal_component(p, 3) for p in charts]
    f4, g4 = [normal_component(p, 4) for p in charts]
    quotients, remainders = [], []
    for cubic, a in zip((f3, g3), (alpha, beta)):
        quotient, remainder = sp.div(sp.Poly(cubic - a*g00, u, v),
                                      sp.Poly(f0, u, v))
        quotients.append(quotient.as_expr())
        remainders.append(remainder.as_expr())
    lf, lg = quotients
    r4 = sp.expand(alpha**2*g4 - alpha*beta*f4
                   - (alpha*lg - beta*lf)*f3)
    r4_poly = sp.Poly(r4, u, v, domain=sp.QQ)
    content, primitive = r4_poly.primitive()
    f0_poly = sp.Poly(f0, u, v, domain=sp.QQ)
    primitive_gcd = sp.gcd(f0_poly, primitive)
    return {
        "ambient_gcd_degree": ambient_gcd.total_degree(),
        "proper_complete_intersection": ambient_gcd.total_degree() == 0,
        "quadratic_matches_seed_root": all(quadratic_matches),
        "first_cubic_division_exact": all(r == 0 for r in remainders),
        "alpha_z0": str(alpha),
        "beta_z0": str(beta),
        "lF_z0": str(lf),
        "lG_z0": str(lg),
        "quartic_primitive_content": str(content),
        "quartic_primitive_terms": {
            "u^%d*v^%d" % exponent: str(coefficient)
            for exponent, coefficient in primitive.terms()},
        "quartic_coprime_with_seed_f0": primitive_gcd.total_degree() == 0,
        "quartic_common_factor_degree": primitive_gcd.total_degree(),
    }


def compute():
    source_monomials = monomials(8)
    expanded = [expand_octic(m) for m in source_monomials]

    # Vanishing to order >= 2: every constant and linear normal coefficient
    # in the affine chart must vanish identically as a polynomial in z.
    base_keys = sorted({key for p in expanded for key in p
                        if key[0] + key[1] <= 1})
    base_matrix = matrix_for(base_keys, expanded)
    source_kernel = base_matrix.nullspace()
    source = []
    for vector in source_kernel:
        p = {}
        for coefficient, expansion in zip(vector, expanded):
            if coefficient:
                p = add(p, scale(expansion, F(coefficient)))
        source.append(p)

    quad_rows = sorted({(i, j, k) for p in source for i, j, k in p
                        if i + j == 2})
    quad_matrix = matrix_for(quad_rows, source)
    cubic_rows = sorted({(i, j, k) for p in source for i, j, k in p
                         if i + j == 3})
    cubic_matrix = matrix_for(cubic_rows, source)
    # The kernel of the quadratic projection is the actual order-three
    # octic source. Its cubic-symbol rank is an intrinsic source dimension.
    order_three_source = []
    for vector in quad_matrix.nullspace():
        p = {}
        for coefficient, expansion in zip(vector, source):
            if coefficient:
                p = add(p, scale(expansion, F(coefficient)))
        order_three_source.append(p)
    order_three_cubic_rows = sorted({key for p in order_three_source for key in p
                                    if key[0] + key[1] == 3})
    order_three_cubic_matrix = matrix_for(order_three_cubic_rows, order_three_source)

    # Seed root f and its accepted first cubic correction G0.
    z = sp.Symbol("z")
    f = [sp.Poly(z**2 + 4, z, domain=sp.QQ),
         sp.Poly(0, z, domain=sp.QQ),
         sp.Poly(z**2 - 8, z, domain=sp.QQ)]
    G0 = [sp.Poly(0, z, domain=sp.QQ),
          sp.Poly(z/8, z, domain=sp.QQ),
          sp.Poly(-sp.Rational(3, 4), z, domain=sp.QQ),
          sp.Poly(z/8, z, domain=sp.QQ)]

    # Coefficient rows for all source cubics and alpha*G0.
    max_cubic_degree = max(k for _, _, k in cubic_rows)
    alpha_degree = 16
    l_degree = m_degree = max(max_cubic_degree, alpha_degree + 1) - 2
    # Variables: source-section coefficients, alpha_0..alpha_16,
    # l_0..l_L, m_0..m_L.
    nsource, nalpha = len(source), alpha_degree + 1
    nl, nm = l_degree + 1, m_degree + 1
    total_vars = nsource + nalpha + nl + nm
    row_dict = {}
    # Source cubic terms.
    for col, p in enumerate(source):
        for key in normal_keys(p, 3):
            row_dict.setdefault(key, {})[col] = p[key]
    # - alpha * G0.
    for ai in range(nalpha):
        for (u_exp, v_exp), gp in zip([(3, 0), (2, 1), (1, 2), (0, 3)], G0):
            for (k,), coeff in gp.terms():
                row_dict.setdefault((u_exp, v_exp, k + ai), {})[nsource + ai] = -F(coeff)
    # F2 = alpha*f: these order-two equations keep the multiplier tied to
    # the actual source symbol, rather than imposing only the cubic match.
    for col, p in enumerate(source):
        for key in normal_keys(p, 2):
            row_dict.setdefault(key, {})[col] = p[key]
    for ai in range(nalpha):
        for (u_exp, v_exp), fp in zip([(2, 0), (1, 1), (0, 2)], f):
            for (k,), coeff in fp.terms():
                row_dict.setdefault((u_exp, v_exp, k + ai), {})[nsource + ai] = -F(coeff)
    # - f*(l*u + m*v).
    lstart, mstart = nsource + nalpha, nsource + nalpha + nl
    for i in range(nl):
        for (k,), coeff in f[0].terms():
            row_dict.setdefault((3, 0, k + i), {})[lstart + i] = -F(coeff)
        for (k,), coeff in f[2].terms():
            row_dict.setdefault((1, 2, k + i), {})[lstart + i] = -F(coeff)
    for i in range(nm):
        for (k,), coeff in f[0].terms():
            row_dict.setdefault((2, 1, k + i), {})[mstart + i] = -F(coeff)
        for (k,), coeff in f[2].terms():
            row_dict.setdefault((0, 3, k + i), {})[mstart + i] = -F(coeff)

    cubic_equation_keys = sorted(row_dict)
    cubic_equation_matrix = sp.Matrix(
        [[row_dict[key].get(j, F(0)) for j in range(total_vars)]
         for key in cubic_equation_keys])
    cubic_kernel = cubic_equation_matrix.nullspace()
    projected_forms = []
    projected_alphas = []
    for vector in cubic_kernel:
        projected_forms.append(sp.Matrix(vector[:nsource, :]))
        projected_alphas.append(sp.Matrix(vector[nsource:nsource+nalpha, :]))
    alpha_projection = (sp.Matrix.hstack(*projected_alphas)
                        if projected_alphas else sp.zeros(nalpha, 0))
    form_projection = (sp.Matrix.hstack(*projected_forms)
                       if projected_forms else sp.zeros(nsource, 0))
    source_coefficient_matrix = sp.Matrix.hstack(*source_kernel)
    homogeneous_root_forms = source_coefficient_matrix * form_projection

    alpha_image_basis = alpha_projection.columnspace()
    alpha_basis = [[F(vector[i]) for i in range(nalpha)]
                   for vector in alpha_image_basis]
    alpha_gcd = gcd_with_infinity(alpha_basis, alpha_degree)
    free_pair = basepoint_free_pair(alpha_basis, alpha_degree)

    def vector_poly(values):
        return sp.Poly(sum(value * z**i for i, value in enumerate(values)), z,
                       domain=sp.QQ)

    def lift_alpha(alpha_values):
        """Select the first exact lift of an alpha vector to full solutions."""
        solution, parameters = alpha_projection.gauss_jordan_solve(
            sp.Matrix(alpha_values))
        if parameters.rows:
            solution = solution.subs({parameter: 0 for parameter in parameters})
        return solution

    def homogeneous_form_dict(coefficients):
        return {"x0^%d*x1^%d*x2^%d*x3^%d" % monomial: str(value)
                for monomial, value in zip(source_monomials, coefficients) if value}

    root_basis = []
    for j in range(len(cubic_kernel)):
        alpha_values = [F(projected_alphas[j][i]) for i in range(nalpha)]
        form_values = homogeneous_root_forms[:, j]
        root_basis.append({
            "alpha": str(vector_poly(alpha_values).as_expr()),
            "octic": homogeneous_form_dict(form_values),
        })

    free_pair_lifts = None
    pair_coefficients = None
    if free_pair is not None:
        free_pair_lifts = []
        pair_coefficients = []
        for expression in free_pair:
            poly = sp.Poly(expression, z, domain=sp.QQ)
            alpha_values = [F(poly.nth(i)) for i in range(nalpha)]
            coordinates = lift_alpha(alpha_values)
            form_values = homogeneous_root_forms * coordinates
            pair_coefficients.append(form_values)
            free_pair_lifts.append({
                "alpha": expression,
                "octic": homogeneous_form_dict(form_values),
            })
    certificate = (pair_certificate(pair_coefficients, source_monomials)
                   if pair_coefficients is not None else None)

    return {
        "source_dimension": len(source),
        "source_quadratic_projection_rank": quad_matrix.rank(),
        "source_quadratic_kernel_dimension": len(source) - quad_matrix.rank(),
        "order_three_source_dimension": len(order_three_source),
        "order_three_symbol_rank": order_three_cubic_matrix.rank(),
        "all_source_local_cubic_coefficient_rank": cubic_matrix.rank(),
        "source_cubic_max_z_degree": max_cubic_degree,
        "base_equation_rows": len(base_keys),
        "base_equation_rank": base_matrix.rank(),
        "seed_first_lift_equation_rows": len(cubic_equation_keys),
        "seed_first_lift_equation_rank": cubic_equation_matrix.rank(),
        "full_variable_kernel_dimension": len(cubic_kernel),
        "projected_actual_octic_basis_dimension": len(form_projection.columnspace()),
        "projected_actual_octic_dimension": form_projection.rank(),
        "projected_alpha_dimension": alpha_projection.rank(),
        "alpha_degree_bound": alpha_degree,
        "l_m_degree_bound": l_degree,
        "alpha_gcd": alpha_gcd,
        "basepoint_free_alpha_pair": free_pair,
        "basepoint_free_actual_octic_pair": free_pair_lifts,
        "coprime_pair_certificate": certificate,
        "alpha_basis": [[str(x) for x in row] for row in alpha_basis],
        "root_compatible_actual_basis": root_basis,
        "source_kernel_basis": source,
    }


if __name__ == "__main__":
    result = compute()
    # Keep the command-line report compact; reviewers can import compute()
    # to inspect all 12 actual homogeneous vectors and their multipliers.
    result.pop("source_kernel_basis")
    root_basis = result.pop("root_compatible_actual_basis")
    alpha_basis = result.pop("alpha_basis")
    actual_pair = result.pop("basepoint_free_actual_octic_pair")
    result["root_basis_dimension"] = len(root_basis)
    result["alpha_basis_vectors"] = len(alpha_basis)
    result["coprime_multiplier_pair"] = result["basepoint_free_alpha_pair"]
    result["coprime_pair_octic_term_counts"] = [len(x["octic"]) for x in actual_pair]
    result.pop("basepoint_free_alpha_pair")
    print(json.dumps(result, indent=2))
