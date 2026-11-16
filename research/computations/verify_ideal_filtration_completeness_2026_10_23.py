#!/usr/bin/env python3
"""Exact finite checks for section 6.2 of the independent filtration audit.

Over a characteristic-zero field, localize R=k[t,u,v] at (t,u,v) and put
I=(u,v).  The integral hypersurface equations in the report are

    f_0=u^2+v^5, f_1=u^2+v^3, g=v^4+u^5.

This script checks the localization identities and the transverse algebras

    A_0=Q[u,v]/(u^2,v^4), A_1=Q[u,v]/(u^2+v^3,v^4).

It constructs both eight-dimensional associative algebras, verifies their
defining relations and generation, and computes their identical I-adic
Hilbert functions.  Exact quadratic coefficient matrices verify the distinct
square-zero behavior used in the report.  In A_1, for h in its nilradical,
the v^2 coefficient of h^2 is beta^2; once beta=0, its v^3 coefficient is
-alpha^2, where h=alpha*u+beta*v modulo I^2.  Over a reduced coefficient
ring these identities imply beta=alpha=0.  The report uses the reduced
domain k[t]_(t), not an arbitrary nonreduced coefficient ring.

The independent-basis construction and the elementary rewriting upper bound
together establish the dimensions of these finite models.  The script does
not check irreducibility, all nine sheaf-level graded maps, formal uniqueness,
or any general completeness theorem or global projective/STCI assertion.
It uses only the Python standard library and exact rational/integer arithmetic.
Run with: python3 research/computations/verify_ideal_filtration_completeness_2026_10_23.py
"""

from fractions import Fraction
from itertools import product


def poly_add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def poly_scale(coefficient, polynomial):
    return {exponent: coefficient * value
            for exponent, value in polynomial.items() if coefficient * value}


def poly_mul(left, right):
    result = {}
    for (a, b), first in left.items():
        for (c, d), second in right.items():
            exponent = (a + c, b + d)
            result[exponent] = result.get(exponent, 0) + first * second
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def poly_power(polynomial, exponent):
    result = {(0, 0): 1}
    for _ in range(exponent):
        result = poly_mul(result, polynomial)
    return result


ONE = {(0, 0): 1}
U = {(1, 0): 1}
V = {(0, 1): 1}
G = poly_add(poly_power(V, 4), poly_power(U, 5))


def check_unit_identities():
    """Verify the exact identity giving a unit times v^4 modulo f_r."""
    for r in (5, 3):
        f = poly_add(poly_power(U, 2), poly_power(V, r))
        coefficient = poly_add(poly_mul(U, f),
                               poly_scale(-2, poly_mul(U, poly_power(V, r))))
        unit = poly_add(ONE, poly_mul(U, poly_power(V, 2 * r - 4)))
        assert G == poly_add(poly_mul(f, coefficient),
                             poly_mul(poly_power(V, 4), unit))
        assert unit[(0, 0)] == 1
        assert all(a + b > 0 for (a, b) in unit if (a, b) != (0, 0))


# First exponent is the u exponent; this order matches the report's basis.
BASIS = ((0, 0), (0, 1), (0, 2), (0, 3),
         (1, 0), (1, 1), (1, 2), (1, 3))
BASIS_INDEX = {exponent: index for index, exponent in enumerate(BASIS)}
DIMENSION = len(BASIS)
ZERO = (Fraction(0),) * DIMENSION
UNIT_VECTORS = tuple(tuple(Fraction(i == j) for i in range(DIMENSION))
                     for j in range(DIMENSION))


def vector_add(*vectors):
    return tuple(sum(entries) for entries in zip(*vectors))


def vector_scale(coefficient, vector):
    return tuple(coefficient * entry for entry in vector)


def row_basis(vectors):
    """Exact rational row reduction; return an independent spanning set."""
    rows = [list(map(Fraction, vector)) for vector in vectors if any(vector)]
    pivot_row = 0
    for column in range(DIMENSION):
        pivot = next((index for index in range(pivot_row, len(rows))
                      if rows[index][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        leading = rows[pivot_row][column]
        rows[pivot_row] = [entry / leading for entry in rows[pivot_row]]
        for index, row in enumerate(rows):
            if index != pivot_row and row[column]:
                factor = row[column]
                rows[index] = [entry - factor * base for entry, base
                               in zip(row, rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return [tuple(row) for row in rows[:pivot_row]]


class TransverseAlgebra:
    """Model with u^2=0 (deformed=False) or u^2=-v^3 (True), v^4=0."""

    def __init__(self, deformed):
        self.deformed = deformed
        self.table = tuple(tuple(self.reduce_monomial(a + c, b + d)
                                 for c, d in BASIS) for a, b in BASIS)

    def reduce_monomial(self, a, b):
        # This rewriting terminates by lowering a.  It supplies the upper
        # bound of eight on the dimension of the stated quotient algebra.
        coefficient = 1
        if a >= 2:
            if not self.deformed:
                return ZERO
            pairs, a = divmod(a, 2)
            b += 3 * pairs
            coefficient = (-1) ** pairs
        if b >= 4:
            return ZERO
        return vector_scale(Fraction(coefficient),
                            UNIT_VECTORS[BASIS_INDEX[(a, b)]])

    def multiply(self, left, right):
        result = list(ZERO)
        for i, first in enumerate(left):
            if first:
                for j, second in enumerate(right):
                    if second:
                        for index, coefficient in enumerate(self.table[i][j]):
                            if coefficient:
                                result[index] += first * second * coefficient
        return tuple(result)

    def evaluate(self, polynomial):
        result = ZERO
        for (a, b), coefficient in polynomial.items():
            result = vector_add(result,
                                vector_scale(coefficient,
                                             self.reduce_monomial(a, b)))
        return result

    def multiply_power(self, vector, exponent):
        result = UNIT_VECTORS[0]
        for _ in range(exponent):
            result = self.multiply(result, vector)
        return result

    def square_coefficient_matrix(self, target):
        """Quadratic coefficients for h=sum(h_i*e_i), 1<=i<=7.

        Each (i,j) entry is the coefficient of h_i*h_j in the target basis
        coefficient of h^2.  Off-diagonal terms include both orders.
        """
        result = {}
        for i in range(1, DIMENSION):
            for j in range(i, DIMENSION):
                coefficient = self.table[i][j][target] * (1 if i == j else 2)
                if coefficient:
                    result[(i, j)] = coefficient
        return result


def check_algebra(model):
    """Check construction, relations, generation and the I-adic filtration."""
    assert len(row_basis(UNIT_VECTORS)) == 8
    for first, second in product(UNIT_VECTORS, repeat=2):
        assert model.multiply(first, second) == model.multiply(second, first)
        assert model.multiply(UNIT_VECTORS[0], first) == first
    for first, second, third in product(UNIT_VECTORS, repeat=3):
        assert model.multiply(model.multiply(first, second), third) == \
               model.multiply(first, model.multiply(second, third))

    relation = poly_add(poly_power(U, 2), poly_power(V, 3)) \
        if model.deformed else poly_power(U, 2)
    assert model.evaluate(relation) == ZERO
    assert model.evaluate(poly_power(V, 4)) == ZERO
    assert model.evaluate(G) == ZERO
    original_f = poly_add(poly_power(U, 2),
                          poly_power(V, 3 if model.deformed else 5))
    assert model.evaluate(original_f) == ZERO

    # The independent vectors are actually generated by the two variables,
    # so this eight-dimensional model is a quotient of the stated algebra.
    # With the rewriting upper bound, its dimension is exactly eight.
    u_vector = UNIT_VECTORS[BASIS_INDEX[(1, 0)]]
    v_vector = UNIT_VECTORS[BASIS_INDEX[(0, 1)]]
    for exponent, expected in zip(BASIS, UNIT_VECTORS):
        a, b = exponent
        actual = model.multiply(model.multiply_power(u_vector, a),
                                model.multiply_power(v_vector, b))
        assert actual == expected

    ideal = row_basis(UNIT_VECTORS[1:])
    powers = [list(UNIT_VECTORS), ideal]
    while powers[-1]:
        powers.append(row_basis(model.multiply(left, right)
                                for left in powers[-1] for right in ideal))
        assert len(powers) <= 7
    dimensions = [len(space) for space in powers]
    hilbert_function = [left - right
                        for left, right in zip(dimensions, dimensions[1:])]
    assert dimensions == [8, 7, 5, 3, 1, 0]
    assert hilbert_function == [1, 2, 2, 2, 1]
    return dimensions, hilbert_function, powers


def check_square_zero_invariant(undeformed, deformed, powers):
    """Check the exact quadratic coefficients behind the intrinsic argument."""
    u_index = BASIS_INDEX[(1, 0)]
    v_index = BASIS_INDEX[(0, 1)]
    v2_index = BASIS_INDEX[(0, 2)]
    v3_index = BASIS_INDEX[(0, 3)]
    u_vector = UNIT_VECTORS[u_index]
    assert undeformed.multiply(u_vector, u_vector) == ZERO
    assert len(row_basis(powers[2] + [u_vector])) == len(powers[2]) + 1

    # beta is the v coefficient and alpha is the u coefficient of h.
    assert deformed.square_coefficient_matrix(v2_index) == {
        (v_index, v_index): Fraction(1)}
    v3_matrix = deformed.square_coefficient_matrix(v3_index)
    assert v3_matrix == {(v_index, v2_index): Fraction(2),
                         (u_index, u_index): Fraction(-1)}
    after_beta_zero = {indices: coefficient
                       for indices, coefficient in v3_matrix.items()
                       if v_index not in indices}
    assert after_beta_zero == {(u_index, u_index): Fraction(-1)}


def main():
    check_unit_identities()
    undeformed = TransverseAlgebra(deformed=False)
    deformed = TransverseAlgebra(deformed=True)
    dimensions_0, hilbert_0, powers_0 = check_algebra(undeformed)
    dimensions_1, hilbert_1, _ = check_algebra(deformed)
    assert dimensions_0 == dimensions_1
    assert hilbert_0 == hilbert_1
    check_square_zero_invariant(undeformed, deformed, powers_0)

    print("PASS: exact unit identities for f_0=u^2+v^5, f_1=u^2+v^3, g=v^4+u^5")
    print("PASS: both finite quotient models are associative, commutative and generated by u,v")
    print("PASS: both quotient models have basis 1,v,v^2,v^3,u,uv,uv^2,uv^3 (dimension 8)")
    print(f"PASS: dimensions of I-adic powers in each model = {dimensions_0}")
    print(f"PASS: associated-graded Hilbert function in each model = {hilbert_0}")
    print("PASS: A_0 has square-zero u outside I^2")
    print("PASS: A_1 square coefficients: [v^2](h^2)=beta^2; [v^3](h^2)|beta=0=-alpha^2")
    print("Boundary: these exact finite models support the local proof over a characteristic-zero")
    print("field or its reduced parameter base; no full sheaf diagram or global STCI assertion is checked.")


if __name__ == "__main__":
    main()
