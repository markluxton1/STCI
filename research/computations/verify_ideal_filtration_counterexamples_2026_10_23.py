#!/usr/bin/env python3
"""Finite exact checks for the October 23 independent filtration audit.

Example over Q:
    R = Q[x,y]_(x,y), I = (x,y),
    f = x^2+y^3, g = xy+x^3+y^3, J = (f,g).

This script checks polynomial identities, a five-dimensional quotient algebra,
its associativity and I-adic Hilbert function, and the explicit monomial
comparison showing in_I(IJ) != S_+ in_I(J).  Its calculations support the
accompanying first-principles proof; they do not establish a general theorem,
global realization, irreducibility, or any STCI assertion.

The localization argument uses two explicit polynomials with constant term 1.
No approximate arithmetic, external packages, or computer-algebra installation
is used.  Run with: python3 <this file>
"""

from fractions import Fraction
from itertools import product


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def scale(coefficient, polynomial):
    return {exponent: coefficient * value
            for exponent, value in polynomial.items() if coefficient * value}


def mul(left, right):
    result = {}
    for (a, b), first in left.items():
        for (c, d), second in right.items():
            exponent = (a + c, b + d)
            result[exponent] = result.get(exponent, 0) + first * second
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def power(polynomial, exponent):
    result = {(0, 0): 1}
    for _ in range(exponent):
        result = mul(result, polynomial)
    return result


def initial(polynomial):
    order = min(sum(exponent) for exponent in polynomial)
    return {exponent: coefficient for exponent, coefficient in polynomial.items()
            if sum(exponent) == order}


ONE = {(0, 0): 1}
X = {(1, 0): 1}
Y = {(0, 1): 1}
F = add(power(X, 2), power(Y, 3))
G = add(mul(X, Y), power(X, 3), power(Y, 3))
U = add(ONE, scale(-1, power(Y, 2)))
V = add(power(U, 2), Y)
P = add(mul(X, Y), power(Y, 3))


def check_identities():
    """Check exact ideal identities used in the local colength proof."""
    first_coefficient = add(Y, power(X, 2))
    second_coefficient = add(scale(-1, X), power(Y, 2))
    cancellation = add(mul(first_coefficient, F),
                       mul(second_coefficient, G))
    expected = add(power(Y, 4), mul(power(X, 2), power(Y, 3)),
                   mul(power(X, 3), power(Y, 2)), power(Y, 5))
    assert cancellation == expected
    assert initial(cancellation) == power(Y, 4)
    assert min(map(sum, first_coefficient)) >= 1
    assert min(map(sum, second_coefficient)) >= 1

    # v*y^4 = A*f + B*g, with v(0)=1, proves y^4 in J locally.
    coefficient_a = add(mul(power(U, 2), Y),
                        scale(-1, mul(X, power(Y, 2))),
                        mul(U, power(X, 2)))
    coefficient_b = add(power(Y, 2), scale(-1, mul(U, X)))
    assert mul(V, power(Y, 4)) == add(mul(coefficient_a, F),
                                      mul(coefficient_b, G))
    assert U[(0, 0)] == V[(0, 0)] == 1

    # u*p = g-x*f-y^5, hence p in J after y^4 is known.
    assert mul(U, P) == add(G, scale(-1, mul(X, F)),
                            scale(-1, power(Y, 5)))
    # Conversely g is in (f,p,y^4), so the local ideals agree.
    assert G == add(mul(U, P), mul(X, F), power(Y, 5))


BASIS = ((0, 0), (1, 0), (0, 1), (0, 2), (0, 3))
BASIS_INDEX = {exponent: index for index, exponent in enumerate(BASIS)}
ZERO_VECTOR = (Fraction(0),) * len(BASIS)


def reduce_monomial(a, b):
    """Use x^2=-y^3, xy=-y^3, y^4=0; x exponent decreases."""
    coefficient = 1
    while True:
        if b >= 4:
            return ZERO_VECTOR
        if a >= 2:
            a, b, coefficient = a - 2, b + 3, -coefficient
        elif a >= 1 and b >= 1:
            a, b, coefficient = a - 1, b + 2, -coefficient
        else:
            result = list(ZERO_VECTOR)
            result[BASIS_INDEX[(a, b)]] = Fraction(coefficient)
            return tuple(result)


def vector_add(*vectors):
    return tuple(sum(entries) for entries in zip(*vectors))


def vector_scale(coefficient, vector):
    return tuple(coefficient * entry for entry in vector)


def algebra_mul(left, right):
    result = ZERO_VECTOR
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            if first and second:
                a, b = BASIS[i]
                c, d = BASIS[j]
                result = vector_add(
                    result, vector_scale(first * second,
                                         reduce_monomial(a + c, b + d)))
    return result


def evaluate(polynomial):
    result = ZERO_VECTOR
    for (a, b), coefficient in polynomial.items():
        result = vector_add(result, vector_scale(coefficient,
                                                 reduce_monomial(a, b)))
    return result


def row_basis(vectors):
    """Exact rational row reduction, returning a basis for the row span."""
    rows = [list(map(Fraction, vector)) for vector in vectors if any(vector)]
    pivot_row = 0
    for column in range(len(BASIS)):
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


def check_finite_algebra():
    """A generated associative algebra gives the lower colength bound 5."""
    basis_vectors = [reduce_monomial(*exponent) for exponent in BASIS]
    assert len(row_basis(basis_vectors)) == 5
    unit = basis_vectors[0]
    for left, right in product(basis_vectors, repeat=2):
        assert algebra_mul(left, right) == algebra_mul(right, left)
        assert algebra_mul(unit, left) == left
    for first, second, third in product(basis_vectors, repeat=3):
        assert algebra_mul(algebra_mul(first, second), third) == \
               algebra_mul(first, algebra_mul(second, third))
    assert evaluate(F) == evaluate(G) == evaluate(P) == ZERO_VECTOR
    assert evaluate(power(Y, 4)) == ZERO_VECTOR

    # Each listed basis vector is a monomial in x,y, so the algebra is generated.
    assert [evaluate({exponent: 1}) for exponent in BASIS] == basis_vectors

    maximal_ideal = basis_vectors[1:]
    powers = [basis_vectors, row_basis(maximal_ideal)]
    while powers[-1]:
        powers.append(row_basis(algebra_mul(left, right)
                                for left in powers[-1]
                                for right in maximal_ideal))
    dimensions = [len(space) for space in powers]
    assert dimensions == [5, 4, 2, 1, 0]
    hilbert_function = [left - right
                        for left, right in zip(dimensions, dimensions[1:])]
    assert hilbert_function == [1, 2, 1, 1]
    return dimensions, hilbert_function


def check_generator_comparison():
    """Y^4 is new in H and in in(IJ), while its lifting quotient vanishes."""
    assert initial(F) == power(X, 2)
    assert initial(G) == mul(X, Y)
    # Independent degree-two initial forms force constant coefficients to vanish
    # in every combination af+bg of order at least three.
    degree_two_monomials = ((2, 0), (1, 1), (0, 2))
    initial_coefficient_vectors = [
        tuple(initial(polynomial).get(exponent, 0)
              for exponent in degree_two_monomials) + (0, 0)
        for polynomial in (F, G)
    ]
    assert len(row_basis(initial_coefficient_vectors)) == 2

    # H=(X^2,XY,Y^4); its quotient has the independently checked length five.
    generators = ((2, 0), (1, 1), (0, 4))
    quotient_monomials = []
    for total_degree in range(5):
        for a in range(total_degree + 1):
            b = total_degree - a
            if not any(a >= c and b >= d for c, d in generators):
                quotient_monomials.append((a, b))
    assert set(quotient_monomials) == set(BASIS)

    # Membership in S_+H requires a positive-degree multiplier.
    def in_positive_product(a, b):
        return any(a >= c and b >= d and (a - c) + (b - d) >= 1
                   for c, d in generators)

    assert not in_positive_product(0, 4)
    assert all(in_positive_product(a, 4 - a) for a in range(1, 5))
    # Thus Q_4 has basis [Y^4], but the explicit IJ identity kills it in gr_4 D.


def main():
    check_identities()
    dimensions, hilbert_function = check_finite_algebra()
    check_generator_comparison()
    print("PASS: exact polynomial cancellation and localization identities")
    print("PASS: associative quotient algebra with basis 1,x,y,y^2,y^3")
    print(f"PASS: dimensions of I-adic powers = {dimensions}")
    print(f"PASS: associated-graded Hilbert function = {hilbert_function}")
    print("PASS: H=(X^2,XY,Y^4), Q_4=Q, but gr_4(J/IJ)=0")
    print("PASS: Y^4 lies in in_I(IJ) and not in S_+ in_I(J)")
    print("Boundary: finite exact checks support the accompanying local proof;")
    print("they do not certify a general theorem or a global STCI conclusion.")


if __name__ == "__main__":
    main()
