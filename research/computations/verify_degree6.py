#!/usr/bin/env python3
"""Exact degree-six symbolic-square calculations for the monomial quartic C0.

This is the durable certificate for the degree-six classification recorded in
the research record.
"""

import sympy as sp

x0, x1, x2, x3, zeta = sp.symbols("x0 x1 x2 x3 zeta")
xs = (x0, x1, x2, x3)

q = x0 * x3 - x1 * x2
A = x0**2 * x2 - x1**3
B = x0 * x2**2 - x1**2 * x3
D = x2**3 - x1 * x3**2
IGENS = (q, A, B, D)


def monomials_of_degree(degree):
    return [
        x0**a * x1**b * x2**c * x3 ** (degree - a - b - c)
        for a in range(degree, -1, -1)
        for b in range(degree - a, -1, -1)
        for c in range(degree - a - b, -1, -1)
    ]


def coefficient_row(poly, degree, modulus=None):
    P = sp.Poly(poly, *xs, modulus=modulus)
    return [P.coeff_monomial(monomial) for monomial in monomials_of_degree(degree)]


def independent_basis(polys, degree, modulus=None):
    rows = []
    basis = []
    rank = 0
    for poly in polys:
        row = coefficient_row(poly, degree, modulus)
        if modulus is None:
            new_rank = sp.Matrix(rows + [row]).rank()
        else:
            new_rank = rank_mod(sp.Matrix(rows + [row]), modulus)
        if new_rank > rank:
            rows.append(row)
            basis.append(sp.expand(poly))
            rank = new_rank
    return basis


def rank_mod(matrix, p):
    rows = [[int(value) % p for value in row] for row in matrix.tolist()]
    rank = 0
    if not rows:
        return 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column] % p),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, p)
        rows[rank] = [(entry * inverse) % p for entry in rows[rank]]
        for row in range(len(rows)):
            if row != rank and rows[row][column] % p:
                factor = rows[row][column] % p
                rows[row] = [
                    (rows[row][j] - factor * rows[rank][j]) % p
                    for j in range(len(rows[row]))
                ]
        rank += 1
    return rank


def groebner(gens, modulus=None, variables=xs, order="grevlex"):
    kwargs = {"order": order}
    if modulus is not None:
        kwargs["modulus"] = modulus
    return sp.groebner(gens, *variables, **kwargs)


def same_ideal(left, right, modulus=None):
    gl = groebner(left, modulus)
    gr = groebner(right, modulus)
    return all(gl.reduce(f)[1] == 0 for f in right) and all(
        gr.reduce(f)[1] == 0 for f in left
    )


def saturate_by_one(gens, variable, modulus=None):
    kwargs = {"order": "lex"}
    if modulus is not None:
        kwargs["modulus"] = modulus
    big = sp.groebner([*gens, 1 - zeta * variable], zeta, *xs, **kwargs)
    eliminated = [
        polynomial.as_expr()
        for polynomial in big.polys
        if not polynomial.as_expr().has(zeta)
    ]
    return [polynomial.as_expr() for polynomial in groebner(eliminated, modulus).polys]


print("1. SYMBOLIC SQUARE AND DEGREE-SIX SPACE")

ordinary_square_generators = [
    sp.expand(IGENS[i] * IGENS[j])
    for i in range(len(IGENS))
    for j in range(i, len(IGENS))
]

for modulus in (None, 2, 3, 5):
    label = "QQ" if modulus is None else f"GF({modulus})"
    saturated_each_chart = [
        same_ideal(
            ordinary_square_generators,
            saturate_by_one(ordinary_square_generators, variable, modulus),
            modulus,
        )
        for variable in xs
    ]
    assert all(saturated_each_chart)
    print(f"  {label}: I^2:x_i^infinity=I^2 on all four charts")

# Thus I^(2)=I^2 for C0.  Compute the relevant graded pieces exactly.
I4_candidates = [q * monomial for monomial in monomials_of_degree(2)] + [
    cubic * variable for cubic in (A, B, D) for variable in xs
]
I4_basis = independent_basis(I4_candidates, 4)
assert len(I4_basis) == 18

qI4_basis = [sp.expand(q * form) for form in I4_basis]
assert len(independent_basis(qI4_basis, 6)) == 18

residual_basis = [A**2, A * B, B**2, B * D, D**2]
degree6_basis = independent_basis(qI4_basis + residual_basis, 6)
assert len(degree6_basis) == 23
assert same_ideal(ordinary_square_generators, groebner(ordinary_square_generators).polys)

print(f"  dim H^0(I_C(4)) = {len(I4_basis)}")
print(f"  dim q*H^0(I_C(4)) = {len(qI4_basis)}")
print(f"  dim H^0(I_C^(2)(6)) = {len(degree6_basis)}")
print("  quotient basis: A^2, A*B, B^2, B*D, D^2")

# The complete degree-six ideal has dimension 84-(24+1)=59: every binary
# monomial of degree 24 occurs under the parametrization.
s, t = sp.symbols("s t")
parameter_substitution = {
    x0: s**4,
    x1: s**3 * t,
    x2: s * t**3,
    x3: t**4,
}
parameter_images = [
    sp.expand(monomial.subs(parameter_substitution))
    for monomial in monomials_of_degree(6)
]
image_matrix = sp.Matrix(
    [
        [
            sp.Poly(image, s, t).coeff_monomial(s**power * t ** (24 - power))
            for image in parameter_images
        ]
        for power in range(25)
    ]
)
assert image_matrix.rank() == 25
print("  dim H^0(I_C(6)) = 84-25 = 59")

relation = sp.factor(A * D - B**2)
assert sp.expand(relation + x1 * x2 * q**2) == 0
print("  relation modulo q*I_C(4): A*D = B^2")
print("  exact relation: A*D-B^2 = -x1*x2*q^2")

# Saturating the ordinary cube produces no new sextic beyond q^3.
ordinary_cube_generators = [
    sp.expand(IGENS[i] * IGENS[j] * IGENS[k])
    for i in range(len(IGENS))
    for j in range(i, len(IGENS))
    for k in range(j, len(IGENS))
]
cube_saturation = saturate_by_one(ordinary_cube_generators, x0)
degree6_cube = [
    polynomial
    for polynomial in cube_saturation
    if sp.Poly(polynomial, *xs).total_degree() == 6
]
assert len(degree6_cube) == 1
assert sp.factor(degree6_cube[0]) in (sp.factor(q**3), -sp.factor(q**3))
print("  H^0(I_C^(3)(6)) is one-dimensional, spanned by q^3")


print("\n2. RESTRICTION TO THE QUADRIC")

a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1")
segre = {x0: a0 * b0, x1: a0 * b1, x2: a1 * b0, x3: a1 * b1}
h = a1 * b0**3 - a0 * b1**3
assert sp.expand(q.subs(segre)) == 0
assert sp.expand(A.subs(segre) - a0**2 * h) == 0
assert sp.expand(B.subs(segre) - a0 * a1 * h) == 0
assert sp.expand(D.subs(segre) - a1**2 * h) == 0
print("  A|Q=a0^2*h, B|Q=a0*a1*h, D|Q=a1^2*h")
print("  Therefore every non-q class restricts as h^2*R(a0,a1),")
print("  where R is an arbitrary binary quartic (dimension 5).")


print("\n3. AN IRREDUCIBLE SEXTIC WITH REDUCED SINGULAR LOCUS C0")

S2 = x0**2 + x1**2 + x2**2 + x3**2
Fstar = sp.expand(A**2 + B**2 + D**2 + q**2 * S2)
factorization = sp.factor_list(Fstar, *xs)
assert len(factorization[1]) == 1 and factorization[1][0][1] == 1

gradient = [sp.diff(Fstar, variable) for variable in xs]
curve_gb = groebner(IGENS)
assert all(curve_gb.reduce(partial)[1] == 0 for partial in gradient)
gradient_gb = groebner(gradient)
power_certificates = {}
for name, generator in zip(("q", "A", "B", "D"), IGENS):
    for exponent in range(1, 9):
        if gradient_gb.reduce(generator**exponent)[1] == 0:
            power_certificates[name] = exponent
            break
assert power_certificates == {"q": 6, "A": 4, "B": 4, "D": 4}

print("  F*=A^2+B^2+D^2+q^2*(x0^2+x1^2+x2^2+x3^2) is irreducible over QQ")
print(f"  radical Jacobian certificate: {power_certificates}")
print("  Hence sqrt(Jac(F*))=I_C0: its reduced singular locus is exactly C0.")


print("\n4. FIRST QUADRATIC NORMAL FORM AND DISCRIMINANT")

u, normal_a, normal_b = sp.symbols("u normal_a normal_b")
y = u
z = u**3 + normal_a
w = u**4 + normal_b
affine_substitution = {x0: 1, x1: y, x2: z, x3: w}
Fstar_affine = sp.expand(Fstar.subs(affine_substitution))
normal_polynomial = sp.Poly(Fstar_affine, normal_a, normal_b)
first_normal_form = sp.expand(
    sum(
        coefficient * normal_a**i * normal_b**j
        for (i, j), coefficient in normal_polynomial.terms()
        if i + j == 2
    )
)
coefficient_aa = first_normal_form.coeff(normal_a, 2).coeff(normal_b, 0)
coefficient_ab = first_normal_form.coeff(normal_a, 1).coeff(normal_b, 1)
coefficient_bb = first_normal_form.coeff(normal_b, 2).coeff(normal_a, 0)
discriminant = sp.factor(coefficient_ab**2 - 4 * coefficient_aa * coefficient_bb)
expected_discriminant = -4 * (u**2 - u + 1) * (u**2 + u + 1) * (
    u**16 + 2 * u**10 + 2 * u**6 + 1
)
assert sp.expand(discriminant - expected_discriminant) == 0
assert sp.Poly(discriminant, u).degree() == 20
print(f"  discriminant = {discriminant}")
print("  It is a nonzero degree-20 section, so the generic transverse type is nodal")
print("  and it degenerates in a divisor of total degree 20 on C0.")


print("\n5. RESULTANT TEST FOR PAIRS OF THICK SEXTICS")

S2_second = 1 + 2 * y**2 + 3 * z**2 + 5 * w**2 + y * z
Fsecond_affine = sp.expand(
    (A**2 + 2 * B**2 + 3 * D**2).subs(affine_substitution)
    + (q**2).subs(affine_substitution) * S2_second
)


def quadratic_coefficients(expression):
    polynomial = sp.Poly(expression, normal_a, normal_b)
    quadratic = sp.expand(
        sum(
            coefficient * normal_a**i * normal_b**j
            for (i, j), coefficient in polynomial.terms()
            if i + j == 2
        )
    )
    return (
        quadratic.coeff(normal_a, 2).coeff(normal_b, 0),
        quadratic.coeff(normal_a, 1).coeff(normal_b, 1),
        quadratic.coeff(normal_b, 2).coeff(normal_a, 0),
    )


c1 = quadratic_coefficients(Fstar_affine)
c2 = quadratic_coefficients(Fsecond_affine)
sylvester = sp.Matrix(
    [
        [c1[0], c1[1], c1[2], 0],
        [0, c1[0], c1[1], c1[2]],
        [c2[0], c2[1], c2[2], 0],
        [0, c2[0], c2[1], c2[2]],
    ]
)
pair_resultant = sp.factor(sylvester.det())
assert pair_resultant != 0
assert sp.Poly(pair_resultant, u).degree() == 40
print("  an explicit pair has nonzero normal resultant of degree 40")
print(f"  resultant = {pair_resultant}")
print("  Therefore the resultant-identically-zero condition is a proper closed")
print("  condition on pairs; a generic pair cannot have radical C0.")

print("\nALL ASSERTIONS PASSED")
