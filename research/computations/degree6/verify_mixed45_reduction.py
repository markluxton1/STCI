#!/usr/bin/env python3
"""Exact (4,5) normal-jet reduction for the monomial rational quartic.

This is a bounded certificate, not a universal elimination.  It verifies:
  * the degree-4 and degree-5 normal-form dimensions;
  * the three linear equations defining the quartic first-normal image;
  * the seven-variable reduced order-five contact system; and
  * nonzero augmented minors for three explicit one-parameter carrier families.

Run with SymPy 1.14.0.
"""

import sympy as sp

x0, x1, x2, x3, z, a, b, U, V, t = sp.symbols(
    "x0 x1 x2 x3 z a b U V t"
)
LAM = sp.symbols("LAM")
xs = (x0, x1, x2, x3)

q = x0 * x3 - x1 * x2
A = x0**2 * x2 - x1**3
B = x0 * x2**2 - x1**2 * x3
D = x2**3 - x1 * x3**2


def monomials(degree):
    return [
        x0**i * x1**j * x2**k * x3 ** (degree - i - j - k)
        for i in range(degree, -1, -1)
        for j in range(degree - i, -1, -1)
        for k in range(degree - i - j, -1, -1)
    ]


def coefficient_row(form, degree):
    polynomial = sp.Poly(form, *xs)
    return [polynomial.coeff_monomial(monomial) for monomial in monomials(degree)]


def independent_basis(forms, degree):
    rows = []
    basis = []
    rank = 0
    for form in forms:
        row = coefficient_row(form, degree)
        new_rank = sp.Matrix(rows + [row]).rank()
        if new_rank > rank:
            rows.append(row)
            basis.append(sp.expand(form))
            rank = new_rank
    return basis


I3 = independent_basis([q * variable for variable in xs] + [A, B, D], 3)
I4 = independent_basis(
    [q * monomial for monomial in monomials(2)]
    + [cubic * variable for cubic in (A, B, D) for variable in xs],
    4,
)
I5 = independent_basis(
    [q * monomial for monomial in monomials(3)]
    + [cubic * monomial for cubic in (A, B, D) for monomial in monomials(2)],
    5,
)
K5 = [sp.expand(q * cubic) for cubic in I3]
assert (len(I3), len(I4), len(I5), len(K5)) == (7, 18, 35, 7)

normal_substitution = {
    x0: 1,
    x1: z,
    x2: z**3 + a,
    x3: z**4 + b,
}


def normal_polynomial(form):
    return sp.Poly(sp.expand(form.subs(normal_substitution)), a, b)


def balanced_first_normal(polynomial):
    # Balanced conormal frame: U=b-(3/2)za and V=a.
    expression = sp.expand(
        polynomial.as_expr().subs({a: V, b: U + sp.Rational(3, 2) * z * V})
    )
    result = sp.Poly(expression, U, V)
    return (
        sp.expand(result.coeff_monomial(U)),
        sp.expand(result.coeff_monomial(V)),
    )


def coefficient_pair_vector(first, second, maximum_degree):
    return sp.Matrix(
        [sp.Poly(first, z).coeff_monomial(z**i) for i in range(maximum_degree + 1)]
        + [
            sp.Poly(second, z).coeff_monomial(z**i)
            for i in range(maximum_degree + 1)
        ]
    )


W4 = sp.Matrix.hstack(
    *[
        coefficient_pair_vector(*balanced_first_normal(normal_polynomial(form)), 9)
        for form in I4
    ]
)
W5 = sp.Matrix.hstack(
    *[
        coefficient_pair_vector(*balanced_first_normal(normal_polynomial(form)), 13)
        for form in I5
    ]
)
assert W4.rank() == 17
assert W5.rank() == 28

# In coefficient order U_0,...,U_9,V_0,...,V_9, the annihilator of W4 is
# U_1-2V_2, U_4-2V_5, U_7-2V_8.
annihilator = W4.T.nullspace()
expected_annihilator = []
for u_index, v_index in ((1, 2), (4, 5), (7, 8)):
    vector = sp.zeros(20, 1)
    vector[u_index] = 1
    vector[10 + v_index] = -2
    expected_annihilator.append(vector)
assert len(annihilator) == 3
assert all((vector.T * W4).is_zero_matrix for vector in expected_annihilator)


def particular_solution(matrix, target):
    """Choose the solution supported on a fixed independent column set."""
    pivots = matrix.rref()[1]
    pivot_matrix = matrix[:, list(pivots)]
    values = list(next(iter(sp.linsolve((pivot_matrix, target)))))
    result = [sp.Integer(0)] * matrix.cols
    for column, value in zip(pivots, values):
        result[column] = sp.cancel(value)
    return result


def lift_quartic(first_u, first_v, q_square_coefficient):
    coefficients = particular_solution(
        W4, coefficient_pair_vector(first_u, first_v, 9)
    )
    return sp.expand(
        sum(coefficient * form for coefficient, form in zip(coefficients, I4))
        + q_square_coefficient * q**2
    )


def lift_quintic(first_u, first_v):
    coefficients = particular_solution(
        W5, coefficient_pair_vector(first_u, first_v, 13)
    )
    return sp.expand(
        sum(coefficient * form for coefficient, form in zip(coefficients, I5))
    )


def solve_a_series(quartic_normal, maximum_order=5):
    """Solve F(a(t),t)=0 through t^maximum_order over QQ(z)."""
    linear_a = sp.expand(quartic_normal.as_expr()).coeff(a, 1).coeff(b, 0)
    assert linear_a != 0
    coefficients = [sp.Integer(0)] * (maximum_order + 1)

    def multiply(left, right, order):
        return [
            sp.cancel(sum(left[r] * right[j - r] for r in range(j + 1)))
            for j in range(order + 1)
        ]

    for order in range(1, maximum_order + 1):
        powers = [[sp.Integer(0)] * (order + 1) for _ in range(6)]
        powers[0][0] = 1
        base = coefficients[:order] + [0]
        for exponent in range(1, 6):
            powers[exponent] = multiply(powers[exponent - 1], base, order)
        residual = 0
        for (power_a, power_b), scalar in quartic_normal.terms():
            if order >= power_b:
                residual += scalar * powers[power_a][order - power_b]
        coefficients[order] = sp.cancel(-residual / linear_a)
    return coefficients


def restricted_coefficients(polynomial, a_series, maximum_order=5):
    powers = [[sp.Integer(0)] * (maximum_order + 1) for _ in range(6)]
    powers[0][0] = 1
    for exponent in range(1, 6):
        for order in range(maximum_order + 1):
            powers[exponent][order] = sp.cancel(
                sum(
                    powers[exponent - 1][r] * a_series[order - r]
                    for r in range(order + 1)
                )
            )
    result = [sp.Integer(0)] * (maximum_order + 1)
    for (power_a, power_b), scalar in polynomial.terms():
        for order in range(power_b, maximum_order + 1):
            result[order] += scalar * powers[power_a][order - power_b]
    return [sp.cancel(value) for value in result]


def scalar_equations(rational_functions):
    common_denominator = sp.Poly(1, z)
    for value in rational_functions:
        common_denominator = sp.lcm(
            common_denominator, sp.Poly(sp.fraction(sp.cancel(value))[1], z)
        )
    polynomials = []
    for value in rational_functions:
        numerator, denominator = sp.fraction(
            sp.cancel(value * common_denominator.as_expr())
        )
        assert sp.Poly(denominator, z).degree() == 0
        polynomials.append(sp.Poly(sp.expand(numerator / denominator), z))
    maximum_degree = max(polynomial.degree() for polynomial in polynomials)
    return [
        (
            [
                polynomial.coeff_monomial(z**exponent)
                for polynomial in polynomials
            ],
            exponent,
        )
        for exponent in range(maximum_degree + 1)
    ]


def reduced_contact_certificate(first_u, first_v, q_square_coefficient):
    """Test the normalized missing-section multiplier z^2 through order four.

    A quintic with first normal form z^2 times the quartic first normal form is
    unique modulo I_C^(2)(5)=q I_C(3), whose seven basis elements are K5.
    The returned augmented minor certifies inconsistency when nonzero.
    """
    quartic = lift_quartic(first_u, first_v, q_square_coefficient)
    quintic_lift = lift_quintic(z**2 * first_u, z**2 * first_v)
    a_series = solve_a_series(normal_polynomial(quartic))
    candidates = [quintic_lift] + K5
    restrictions = [
        restricted_coefficients(normal_polynomial(candidate), a_series)
        for candidate in candidates
    ]
    assert all(sp.cancel(restriction[1]) == 0 for restriction in restrictions)

    rows = []
    labels = []
    for order in (2, 3, 4):
        block = scalar_equations(
            [restriction[order] for restriction in restrictions]
        )
        rows.extend(row for row, _ in block)
        labels.extend((order, exponent) for _, exponent in block)
    full_matrix = sp.Matrix(rows)
    coefficient_matrix = full_matrix[:, 1:]
    right_hand_side = -full_matrix[:, 0]
    augmented = coefficient_matrix.row_join(right_hand_side)
    augmented_pivot_rows = list(augmented.T.rref()[1])
    certificate_rows = augmented_pivot_rows[:8]
    certificate = sp.factor(augmented[certificate_rows, :].det())
    return {
        "quartic": quartic,
        "coefficient_rank": coefficient_matrix.rank(),
        "augmented_rank": augmented.rank(),
        "certificate_rows": [labels[index] for index in certificate_rows],
        "certificate": certificate,
    }


print("DIMENSIONS AND NORMAL IMAGES")
print("  dim I_C(3), I_C(4), I_C(5) =", len(I3), len(I4), len(I5))
print("  rank W4, rank W5 =", W4.rank(), W5.rank())
print("  kernel of the quintic first-normal map = q*I_C(3), dimension 7")
print("  W4 equations: U_1=2V_2, U_4=2V_5, U_7=2V_8")

families = [
    ("parent family x1*A + lambda*q^2", 0, z, LAM, 2 * LAM**3),
    ("type-A example", z**9 + 1, 0, LAM, -72),
    ("type-B example", z**8 + 1, z * (z**8 + 1), LAM, -48),
]

print("\nEXACT REDUCED-JET CERTIFICATES")
for label, first_u, first_v, coefficient, expected_certificate in families:
    result = reduced_contact_certificate(first_u, first_v, coefficient)
    assert result["coefficient_rank"] == 7
    assert result["augmented_rank"] == 8
    assert sp.expand(result["certificate"] - expected_certificate) == 0
    print(f"  {label}:")
    print("    ranks =", (result["coefficient_rank"], result["augmented_rank"]))
    print("    certificate rows =", result["certificate_rows"])
    print("    augmented 8x8 determinant =", result["certificate"])

print("\nALL ASSERTIONS PASSED")
