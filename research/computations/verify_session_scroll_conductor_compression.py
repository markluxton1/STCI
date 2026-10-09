#!/usr/bin/env python3
"""Exact identity checks for the Oct8 smooth-base rank-two conductor note.

This script does not classify nonnormal quartics or sample mate degrees.
The all-degree conclusions use the structural proof in the companion note.
"""

import sympy as s


def assert_zero(value):
    assert s.cancel(s.expand(value)) == 0, value


a, b, c, d, delta, q, zeta = s.symbols("a b c d delta q zeta")


def multiply(left, right, discriminant=delta):
    """Coefficients of (left0+eta left1)(right0+eta right1), eta²=delta."""
    l0, l1 = left
    r0, r1 = right
    return (l0 * r0 + discriminant * l1 * r1, l0 * r1 + l1 * r0)


def involution(pair):
    return (pair[0], -pair[1])


# Trace involution is multiplicative for arbitrary discriminant.
lhs = involution(multiply((a, b), (c, d)))
rhs = multiply(involution((a, b)), involution((c, d)))
for difference in (lhs[i] - rhs[i] for i in range(2)):
    assert_zero(difference)
assert involution(involution((a, b))) == (a, b)
square = multiply((a, b), (a, b))
assert_zero(square[1] - 2 * a * b)

# For square discriminant the two branch evaluations form algebra maps.
product = multiply((a, b), (c, d), q**2)
for sign in (1, -1):
    evaluated = product[0] + sign * q * product[1]
    assert_zero(evaluated - (a + sign * q * b) * (c + sign * q * d))

# A nontrivial constant branch eigenvalue forces both restrictions q*ell.
a_eigen = q * b * (1 + zeta) / (1 - zeta)
plus = a_eigen + q * b
minus = a_eigen - q * b
assert_zero(minus - zeta * plus)
assert_zero(plus - 2 * q * b / (1 - zeta))
assert_zero(minus - 2 * zeta * q * b / (1 - zeta))

# Exact initial Taylor coefficient at contacts m=1 and m=2. Terms of
# larger ordinary degree have larger t-adic degree after w=t^m, so
# cannot change the coefficient being verified.
t, w = s.symbols("t w")
coefficients = {
    (i, j): s.Symbol(f"f{i}{j}")
    for i in range(5)
    for j in range(5 - i)
}
f = sum(value * t**i * w**j for (i, j), value in coefficients.items())
for contact in (1, 2):
    difference = s.expand(f.subs(w, t**contact) - f.subs(w, 0))
    assert s.Poly(difference, t).coeff_monomial(t**contact) == coefficients[(0, 1)]
    assert all(s.Poly(difference, t).coeff_monomial(t**i) == 0 for i in range(contact))

# The dual-number power coefficient is n*a^(n-1)*b for every positive n;
# this is an exact symbolic differentiation identity, not finite sampling.
n = s.Symbol("n", integer=True, positive=True)
epsilon = s.Symbol("epsilon")
linear_coefficient = s.diff((a + b * epsilon) ** n, epsilon).subs(epsilon, 0)
assert s.simplify(linear_coefficient / (n * a ** (n - 1) * b)) == 1

# Unique ambient quadric through C0=[s^4:s^3t:st^3:t^4].
source_exponents = (4, 3, 1, 0)
quadratic_pairs = [(i, j) for i in range(4) for j in range(i, 4)]
evaluation = s.zeros(9, 10)
for column, (i, j) in enumerate(quadratic_pairs):
    evaluation[source_exponents[i] + source_exponents[j], column] = 1
assert evaluation.rank() == 9
relation = s.zeros(10, 1)
relation[quadratic_pairs.index((0, 3)), 0] = 1
relation[quadratic_pairs.index((1, 2)), 0] = -1
assert evaluation * relation == s.zeros(9, 1)
assert len(evaluation.nullspace()) == 1

# Every quartic singular along the standard smooth twisted cubic is a
# quadratic expression in its three quadratic ideal generators. This
# finite-dimensional algebraic step uses a rank certificate, independent
# of any classification or slc hypothesis.
x0, x1, x2, x3 = s.symbols("x0 x1 x2 x3")
coordinates = (x0, x1, x2, x3)
quartic_exponents = [
    (e0, e1, e2, 4 - e0 - e1 - e2)
    for e0 in range(5)
    for e1 in range(5 - e0)
    for e2 in range(5 - e0 - e1)
]
restriction = s.zeros(40, 35)
weights = (3, 2, 1, 0)
for column, exponents in enumerate(quartic_exponents):
    for derivative in range(4):
        if exponents[derivative]:
            s_degree = sum(weights[i] * exponents[i] for i in range(4)) - weights[derivative]
            restriction[10 * derivative + s_degree, column] = exponents[derivative]
pivot_columns = restriction.rref()[1]
assert len(pivot_columns) == 29
pivot_rows = restriction[:, list(pivot_columns)].T.rref()[1]
rank_minor = restriction.extract(list(pivot_rows), list(pivot_columns))
rank_determinant = rank_minor.det()
assert rank_determinant != 0
xi = (x0 * x2 - x1**2, x0 * x3 - x1 * x2, x1 * x3 - x2**2)
products = [s.Poly(xi[i] * xi[j], *coordinates) for i in range(3) for j in range(i, 3)]
product_coefficients = s.Matrix([
    [form.coeff_monomial(exponents) for form in products]
    for exponents in quartic_exponents
])
assert product_coefficients.rank() == 6
assert restriction * product_coefficients == s.zeros(40, 6)

print("PASS: trace algebra, square-discriminant eigenrelation, contact jets,")
print("      symbolic nilpotent powers, and the unique quadric through C0.")
print("PASS: quartic derivative restriction on the twisted cubic has rank 29;")
print("      its six-dimensional kernel is spanned by the six xi_i*xi_j.")
print(f"      Certified 29x29 minor determinant: {rank_determinant}")
