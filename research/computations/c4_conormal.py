#!/usr/bin/env python3
"""Dependency-free exact checks for conormal data of C4.

C4 is parametrized on x != 0 by (1,t,t^3,t^4), equivalently by
(s^4:s^3 t:s t^3:t^4).  The script uses only integer/rational linear algebra.
It deliberately reports sample jet conditions rather than treating them as a
classification of all singularity divisors.
"""

from collections import defaultdict
from fractions import Fraction
from math import prod


WEIGHTS = (0, 1, 3, 4)  # x, y, z, w after setting s=1


def monomials(degree):
    """Exponent tuples (x,y,z,w) of homogeneous monomials of the given degree."""
    result = []
    for x in range(degree + 1):
        for y in range(degree - x + 1):
            for z in range(degree - x - y + 1):
                result.append((x, y, z, degree - x - y - z))
    return result


def weight(monomial):
    return sum(exponent * variable_weight for exponent, variable_weight in zip(monomial, WEIGHTS))


def ideal_basis(degree):
    """Exact weight-difference basis for I(C4)_degree.

    A homogeneous monomial restricts to t^weight.  In each same-weight block,
    subtracting the first monomial from all others gives a basis of the kernel.
    A polynomial is represented as a list of (exponent_tuple, coefficient) terms.
    """
    blocks = defaultdict(list)
    for monomial in monomials(degree):
        blocks[weight(monomial)].append(monomial)
    return [
        [(monomial, 1), (block[0], -1)]
        for _, block in sorted(blocks.items())
        for monomial in block[1:]
    ]


def multiply(polynomial_a, polynomial_b):
    terms = defaultdict(int)
    for monomial_a, coefficient_a in polynomial_a:
        for monomial_b, coefficient_b in polynomial_b:
            monomial = tuple(a + b for a, b in zip(monomial_a, monomial_b))
            terms[monomial] += coefficient_a * coefficient_b
    return [(monomial, coefficient) for monomial, coefficient in terms.items() if coefficient]


def gradient_restriction(polynomial):
    """Return the four restricted partial derivatives as exponent-to-coefficient maps."""
    result = [defaultdict(int) for _ in range(4)]
    for monomial, coefficient in polynomial:
        monomial_weight = weight(monomial)
        for index, exponent in enumerate(monomial):
            if exponent:
                result[index][monomial_weight - WEIGHTS[index]] += coefficient * exponent
    return [{exponent: coefficient for exponent, coefficient in component.items() if coefficient} for component in result]


def restriction(polynomial):
    """Restrict a homogeneous polynomial to C4 on the chart x=1."""
    result = defaultdict(int)
    for monomial, coefficient in polynomial:
        result[weight(monomial)] += coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def multiply_restrictions(polynomial_a, polynomial_b):
    """Multiply two polynomials represented by exponent-to-coefficient maps."""
    result = defaultdict(int)
    for exponent_a, coefficient_a in polynomial_a.items():
        for exponent_b, coefficient_b in polynomial_b.items():
            result[exponent_a + exponent_b] += coefficient_a * coefficient_b
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def passes_q_multiple_gradient_test(polynomial, q):
    """Necessary gradient test for whether ``polynomial`` is q times a form.

    On C4, d(q)=(t^4,-t^3,-t,1).  If F=qR, then dF|C4 equals
    R|C4 d(q)|C4, because q vanishes on C4.  Failure therefore certifies that
    q does not divide F.  Passing is intentionally not used as a converse.
    """
    q_gradient = gradient_restriction(q)
    polynomial_gradient = gradient_restriction(polynomial)
    candidate_restriction = polynomial_gradient[3]  # d(q)/dw restricts to 1
    return all(
        component == multiply_restrictions(q_component, candidate_restriction)
        for component, q_component in zip(polynomial_gradient, q_gradient)
    )


def affine_conormal_pair(polynomial):
    """Return the rescaled (q,p)-conormal pair (P,Q) on x != 0, t != 0.

    Let q=xw-yz and p=xz^2-y^2w.  For a monomial of restriction weight r,
    its first normal coefficients are

        (z+2w)t^(r-4) in q, and (z+w)t^(r-6) in p,

    where z,w in this display are the exponents of the monomial.  We rescale
    by P=t*(q coefficient) and Q=t^3*(p coefficient), so both maps are
    polynomials of degree at most ten for quartics.
    """
    p_component = defaultdict(int)
    q_component = defaultdict(int)
    for monomial, coefficient in polynomial:
        restriction_weight = weight(monomial)
        _, _, z_exponent, w_exponent = monomial
        p_component[restriction_weight - 3] += coefficient * (z_exponent + 2 * w_exponent)
        q_component[restriction_weight - 3] += coefficient * (z_exponent + w_exponent)
    return (
        {exponent: coefficient for exponent, coefficient in p_component.items() if coefficient},
        {exponent: coefficient for exponent, coefficient in q_component.items() if coefficient},
    )


def pair_vector(pair):
    """Coefficient vector of (P,Q), each in degrees 0 through 10."""
    p_component, q_component = pair
    return [p_component.get(exponent, 0) for exponent in range(11)] + [
        q_component.get(exponent, 0) for exponent in range(11)
    ]


def quartic_pair_satisfies_image_equations(pair):
    """Five equations cutting out the affine quartic conormal image."""
    p_component, q_component = pair
    return (
        q_component.get(0, 0) == p_component.get(0, 0)
        and q_component.get(2, 0) == 0
        and q_component.get(5, 0) == 0
        and q_component.get(8, 0) == 0
        and q_component.get(10, 0) == -p_component.get(10, 0)
    )


def gaussian_rank(matrix):
    matrix = [[Fraction(entry) for entry in row] for row in matrix if any(row)]
    if not matrix:
        return 0
    row_count, column_count = len(matrix), len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        divisor = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / divisor for entry in matrix[pivot_row]]
        for row in range(row_count):
            if row != pivot_row and matrix[row][column]:
                factor = matrix[row][column]
                matrix[row] = [entry - factor * pivot_entry for entry, pivot_entry in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def gradient_map_rank(degree):
    basis = ideal_basis(degree)
    restrictions = [gradient_restriction(polynomial) for polynomial in basis]
    rows = []
    for component in range(4):
        for exponent in range(4 * (degree - 1) + 1):
            rows.append([restriction[component].get(exponent, 0) for restriction in restrictions])
    return len(basis), gaussian_rank(rows)


def affine_conormal_profile(degree):
    """Ranks in the generic local normal coordinates q,p on x != 0, t != 0.

    With q=xw-yz and p=xz^2-y^2w, the first-order expansion of a monomial of
    weight r has q and p coefficients (z+2w)t^(r-4) and (z+w)t^(r-6).
    The returned ranks are grouped by restriction weight; their sum is the rank
    of the global gradient/conormal map.
    """
    blocks = defaultdict(list)
    for monomial in monomials(degree):
        blocks[weight(monomial)].append(monomial)
    profile = []
    for restriction_weight, block in sorted(blocks.items()):
        if len(block) == 1:
            continue
        representative = block[0]
        vectors = [
            (
                (monomial[2] + 2 * monomial[3]) - (representative[2] + 2 * representative[3]),
                (monomial[2] + monomial[3]) - (representative[2] + representative[3]),
            )
            for monomial in block[1:]
        ]
        nonzero = [vector for vector in vectors if vector != (0, 0)]
        if not nonzero:
            rank = 0
        else:
            first = nonzero[0]
            rank = 1 if all(first[0] * vector[1] == first[1] * vector[0] for vector in nonzero[1:]) else 2
        profile.append((restriction_weight, rank))
    return profile


def derivative_evaluation(component, parameter, derivative_order):
    total = Fraction()
    for exponent, coefficient in component.items():
        if exponent >= derivative_order:
            falling_factorial = prod(range(exponent - derivative_order + 1, exponent + 1)) if derivative_order else 1
            total += coefficient * falling_factorial * parameter ** (exponent - derivative_order)
    return total


def quartic_singularity_condition_rank(divisor):
    """Rank for prescribed gradient-zero jets on the affine parameter line.

    ``divisor`` is a list of (rational_parameter, multiplicity) pairs.  It is a
    sample calculation on this chart, not a claim about every divisor on P1.
    """
    basis = ideal_basis(4)
    restrictions = [gradient_restriction(polynomial) for polynomial in basis]
    rows = []
    for parameter, multiplicity in divisor:
        for derivative_order in range(multiplicity):
            for component in range(4):
                rows.append(
                    [
                        derivative_evaluation(restriction[component], Fraction(parameter), derivative_order)
                        for restriction in restrictions
                    ]
                )
    rank = gaussian_rank(rows)
    return rank, len(basis) - rank


def integer_partitions(number, largest_part=None):
    """Partitions in nonincreasing order, used only for finite jet-pattern checks."""
    if number == 0:
        yield ()
        return
    if largest_part is None or largest_part > number:
        largest_part = number
    for first_part in range(largest_part, 0, -1):
        for tail in integer_partitions(number - first_part, first_part):
            yield (first_part,) + tail


def main():
    q = [((1, 0, 0, 1), 1), ((0, 1, 1, 0), -1)]
    cubic_basis = ideal_basis(3)
    exceptional_quartics = {
        "F8": {
            "polynomial": [
                ((3, 0, 0, 1), -1),
                ((2, 1, 1, 0), 2),
                ((0, 4, 0, 0), -1),
                ((1, 0, 0, 3), 1),
                ((0, 1, 1, 2), -2),
                ((0, 0, 4, 0), 1),
            ],
            "gradient": [
                {4: 1, 12: 1},
                {3: -2, 11: -2},
                {1: 2, 9: 2},
                {0: -1, 8: -1},
            ],
            "common_factor": "1+t^8",
        },
        "F9": {
            "polynomial": [
                ((2, 1, 1, 0), 3),
                ((3, 0, 0, 1), -2),
                ((0, 4, 0, 0), -1),
                ((0, 0, 3, 1), 1),
                ((0, 1, 0, 3), -1),
            ],
            "gradient": [
                {},
                {3: -1, 12: -1},
                {1: 3, 10: 3},
                {0: -2, 9: -2},
            ],
            "common_factor": "1+t^9",
        },
    }

    for degree in (4, 5):
        ideal_dimension, gradient_rank = gradient_map_rank(degree)
        print(
            f"degree={degree} Sdim={len(monomials(degree))} Idim={ideal_dimension} "
            f"gradient_rank={gradient_rank} kernel_dim={ideal_dimension - gradient_rank}"
        )
        print(f"  affine_weight_profile={affine_conormal_profile(degree)}")

    quartic_pairs = [affine_conormal_pair(polynomial) for polynomial in ideal_basis(4)]
    assert all(quartic_pair_satisfies_image_equations(pair) for pair in quartic_pairs)
    pair_matrix = [[pair_vector(pair)[column] for pair in quartic_pairs] for column in range(22)]
    assert gaussian_rank(pair_matrix) == 17
    print(
        "quartic_affine_conormal_image: rank=17; "
        "Q0=P0, Q2=Q5=Q8=0, Q10=-P10"
    )

    q_squared = multiply(q, q)
    assert all(not component for component in gradient_restriction(q_squared))
    assert all(all(not component for component in gradient_restriction(multiply(q, cubic))) for cubic in cubic_basis)
    print("kernel_witnesses: q^2 in ker(rho_4); q*I_3 in ker(rho_5), with dim(I_3)=7")

    for name, example in exceptional_quartics.items():
        polynomial = example["polynomial"]
        assert not restriction(polynomial)
        assert gradient_restriction(polynomial) == example["gradient"]
        assert not passes_q_multiple_gradient_test(polynomial, q)
        pair = affine_conormal_pair(polynomial)
        assert quartic_pair_satisfies_image_equations(pair)
        if name == "F8":
            assert pair == ({}, {1: 1, 9: 1})
        if name == "F9":
            assert pair == ({1: -1, 10: -1}, {1: 1, 10: 1})
        print(
            f"exceptional_{name}: in_I=True q_factor_excluded_by_gradient=True "
            f"restricted_gradient_common_factor={example['common_factor']}"
        )

    samples = {
        "eight_distinct": [(parameter, 1) for parameter in range(1, 9)],
        "eight_at_one_point": [(1, 8)],
        "nine_distinct": [(parameter, 1) for parameter in range(1, 10)],
        "nine_at_one_point": [(1, 9)],
    }
    for name, divisor in samples.items():
        rank, solution_dimension = quartic_singularity_condition_rank(divisor)
        length = sum(multiplicity for _, multiplicity in divisor)
        print(
            f"quartic_gradient_zero_sample={name} length={length} "
            f"condition_rank={rank} solution_vector_dim={solution_dimension}"
        )

    for length in (8, 9):
        profile_results = []
        for partition in integer_partitions(length):
            divisor = [(index + 1, multiplicity) for index, multiplicity in enumerate(partition)]
            rank, solution_dimension = quartic_singularity_condition_rank(divisor)
            profile_results.append((partition, rank, solution_dimension))
        distinct_results = sorted({(rank, solution_dimension) for _, rank, solution_dimension in profile_results})
        print(
            f"all_partition_jet_samples_length={length} partitions={len(profile_results)} "
            f"distinct_(rank,kernel_dim)={distinct_results}"
        )


if __name__ == "__main__":
    main()
