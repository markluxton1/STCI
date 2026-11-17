#!/usr/bin/env python3
"""Uniform fourth-coefficient test on the quartic pencils through T3.

The full sextic source is computed in characteristic zero. Two minors of
its restriction matrix along a varying quartic branch certify rank 17 on
the geometric parameter line by reduction at a split prime.
"""

from audit_sextic_triple_spaces_2026_10_31 import (
    ONE, ZERO, monomials, orbit, padd, pmul, q, rank_columns,
    rref_kernel, scale, source_matrix,
)


PRIME = 107
ROOT = next(a for a in range(PRIME) if (a * a + 2) % PRIME == 0)


def truncated_product(left, right):
    """Multiply in q', y with weights 3, 1, discarding weight above four."""
    out = {}
    for (i, j), a in left.items():
        for (k, power), b in right.items():
            key = (i + k, j + power)
            if 3 * key[0] + key[1] <= 4:
                out[key] = padd(out.get(key, {}), pmul(a, b))
    return out


def source_jets(degree, data, expected_dimension):
    """Return (h, Theta, e, d) for each vector of the full equation basis."""
    columns, _, matrix = source_matrix(degree, data)
    _, basis = rref_kernel(matrix, len(columns))
    assert len(basis) == expected_dimension

    _, _, s0, t0, _, z, x2, x3 = data
    # The y axis is the triple substitution, with m = q' - gamma*y^2.
    x2q = scale({0: s0}, q(-1))
    x3q = padd({0: t0}, scale(pmul(z, {0: s0}), q(-3, 2)))
    coordinates = (
        {(0, 0): z},
        {(0, j): term for j, term in enumerate(x2)} | {(1, 0): x2q},
        {(0, j): term for j, term in enumerate(x3)} | {(1, 0): x3q},
    )
    powers = []
    for coordinate in coordinates:
        terms = [{(0, 0): {0: ONE}}]
        for _ in range(degree):
            terms.append(truncated_product(terms[-1], coordinate))
        powers.append(terms)
    jets = []
    for _, j, k, l in monomials(degree):
        jet = truncated_product(truncated_product(powers[0][j], powers[1][k]), powers[2][l])
        jets.append((jet.get((1, 0), {}), scale(jet.get((0, 3), {}), q(-1)),
                     jet.get((1, 1), {}), jet.get((0, 4), {})))

    out = []
    for vector in basis:
        h, theta, e, d = {}, {}, {}, {}
        for coefficient, (hj, tj, ej, dj) in zip(vector, jets):
            h = padd(h, scale(hj, coefficient))
            theta = padd(theta, scale(tj, coefficient))
            e = padd(e, scale(ej, coefficient))
            d = padd(d, scale(dj, coefficient))
        out.append((h, theta, e, d))
    return out


def restriction_columns(carrier, source):
    h, theta, e, d = carrier
    h_squared = pmul(h, h)
    theta_h = pmul(theta, h)
    fourth = padd(pmul(h, d), pmul(e, theta))
    cubic_rows, quartic_rows = [], []
    for hf, tf, ef, df in source:
        cubic_rows.append(padd(pmul(theta, hf), scale(pmul(h, tf), q(-1))))
        quartic_rows.append(padd(padd(pmul(h_squared, df), pmul(theta_h, ef)),
                                  scale(pmul(fourth, hf), q(-1))))
    return cubic_rows, quartic_rows


def reduce_coefficient(value):
    rational, radical = value
    return (rational.numerator * pow(rational.denominator, -1, PRIME)
            + ROOT * radical.numerator * pow(radical.denominator, -1, PRIME)) % PRIME


def parameter_matrix(quartics, sextics):
    first, second = quartics
    at_zero = restriction_columns(first, sextics)
    at_one = restriction_columns(tuple(padd(a, b) for a, b in zip(first, second)), sextics)
    at_infinity = restriction_columns(second, sextics)
    rows = []
    for degree, zero, one, infinity in zip((1, 2), at_zero, at_one, at_infinity):
        for exponent in sorted(set().union(*zero, *one, *infinity)):
            row = []
            for a, b, c in zip(zero, one, infinity):
                constant, middle, lead = (reduce_coefficient(poly.get(exponent, ZERO))
                                          for poly in (a, b, c))
                if degree == 1:
                    assert (constant + lead - middle) % PRIME == 0
                    row.append((constant, lead))
                else:
                    row.append((constant, (middle - constant - lead) % PRIME, lead))
            rows.append(row)
    return rows


def pivot_minor(matrix):
    """Find row and column indices of a nonzero minor at a parameter point."""
    entries = [row.copy() for row in matrix]
    row_indices = list(range(len(entries)))
    pivots = []
    for column in range(len(entries[0])):
        i = len(pivots)
        pivot = next((j for j in range(i, len(entries)) if entries[j][column]), None)
        if pivot is None:
            continue
        entries[i], entries[pivot] = entries[pivot], entries[i]
        row_indices[i], row_indices[pivot] = row_indices[pivot], row_indices[i]
        pivots.append((row_indices[i], column))
        inverse = pow(entries[i][column], -1, PRIME)
        for row in entries[i + 1:]:
            factor = row[column] * inverse % PRIME
            if factor:
                for j in range(column, len(row)):
                    row[j] = (row[j] - factor * entries[i][j]) % PRIME
    assert len(pivots) == 17
    return tuple(zip(*pivots))


def determinant(matrix):
    value = 1
    for i, row in enumerate(matrix):
        pivot = next((j for j in range(i, len(matrix)) if matrix[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
            row = matrix[i]
            value = -value
        value = value * row[i] % PRIME
        inverse = pow(row[i], -1, PRIME)
        for lower in matrix[i + 1:]:
            factor = lower[i] * inverse % PRIME
            if factor:
                for j in range(i + 1, len(row)):
                    lower[j] = (lower[j] - factor * row[j]) % PRIME
    return value


def trim(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def interpolate(values):
    """Interpolate at consecutive integers via the Newton binomial basis."""
    answer = [0] * len(values)
    basis = [1]
    for i in range(len(values)):
        for j, coefficient in enumerate(basis):
            answer[j] = (answer[j] + values[0] * coefficient) % PRIME
        values = [(b - a) % PRIME for a, b in zip(values, values[1:])]
        inverse = pow(i + 1, -1, PRIME)
        basis = [(b - i * a) * inverse % PRIME for a, b in zip(basis + [0], [0] + basis)]
    return trim(answer)


def polynomial_gcd(left, right):
    while right:
        remainder = left.copy()
        inverse = pow(right[-1], -1, PRIME)
        while len(remainder) >= len(right):
            offset = len(remainder) - len(right)
            factor = remainder[-1] * inverse % PRIME
            for j, coefficient in enumerate(right):
                remainder[offset + j] = (remainder[offset + j] - factor * coefficient) % PRIME
            trim(remainder)
        left, right = right, remainder
    return [coefficient * pow(left[-1], -1, PRIME) % PRIME for coefficient in left]


def affine_minor(matrix, indices):
    rows, columns = indices
    degree_bound = sum(len(matrix[i][0]) - 1 for i in rows)
    values = []
    for t in range(degree_bound + 1):
        values.append(determinant([
            [sum(c * t**i for i, c in enumerate(matrix[row][col])) % PRIME for col in columns]
            for row in rows
        ]))
    return interpolate(values)


def verify(name):
    data = orbit(name)
    quartics = source_jets(4, data, 2)
    sextics = source_jets(6, data, 27)
    h0, theta0, _, _ = quartics[0]
    h1, theta1, _, _ = quartics[1]
    degrees = sorted(h0.keys() | h1.keys())
    assert rank_columns([[h.get(i, ZERO) for i in degrees] for h in (h0, h1)]) == 2
    assert padd(pmul(h0, theta1), scale(pmul(h1, theta0), q(-1)))

    matrix = parameter_matrix(quartics, sextics)
    zero = [[entry[0] for entry in row] for row in matrix]
    infinity = [[entry[-1] for entry in row] for row in matrix]
    at_infinity = pivot_minor(infinity)
    rows, columns = at_infinity
    assert determinant([[infinity[i][j] for j in columns] for i in rows])
    minors = [affine_minor(matrix, indices) for indices in (at_infinity, pivot_minor(zero))]
    assert polynomial_gcd(*minors) == [1]
    print(f"{name}: rank 17 at infinity, affine minor degrees "
          f"{[len(poly) - 1 for poly in minors]}, gcd 1 modulo {PRIME}")


if __name__ == "__main__":
    verify("principal")
    verify("algebraic")
