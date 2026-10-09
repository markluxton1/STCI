#!/usr/bin/env python3
"""Exact arithmetic certificate for the session normal-quartic reduction.

The companion note supplies the geometric passage, classification, Picard,
and normal-sheaf arguments. This script verifies their finite numerical
consequences and does not establish existence of a surface or an STCI.

Run with the repository's existing SymPy environment; stdout is JSON.
"""

from collections import defaultdict
from fractions import Fraction as Q
from math import gcd, lcm
import json

import sympy as sp


def matrix_index(column):
    """Denominator of the entire correction, not just of its square."""
    return lcm(*(int(value.q) for value in column))


def chain(rank):
    result = 2 * sp.eye(rank)
    for i in range(rank - 1):
        result[i, i + 1] = result[i + 1, i] = -1
    return result


def root_matrix(kind, rank):
    if kind == "A":
        return chain(rank)
    if kind == "D":
        result = 2 * sp.eye(rank)
        edges = [(i, i + 1) for i in range(rank - 3)]
        edges += [(rank - 3, rank - 2), (rank - 3, rank - 1)]
    elif kind == "E" and rank in (6, 7):
        result = 2 * sp.eye(rank)
        edges = [(i, i + 1) for i in range(rank - 2)]
        edges.append((2, rank - 1))
    else:
        raise ValueError((kind, rank))
    for i, j in edges:
        result[i, j] = result[j, i] = -1
    assert all(result[:i, :i].det() > 0 for i in range(1, rank + 1))
    return result


# Build the permitted smooth curve--ADE rows independently from root
# matrices, verifying both correction and complete denominator.
ade = []
ade_checks = []


def add_row(kind, rank, vertex, order, expected_q, expected_index, name):
    inverse = root_matrix(kind, rank).inv()
    column = inverse[:, vertex]
    correction = Q(inverse[vertex, vertex])
    index = matrix_index(column)
    assert correction == expected_q
    assert index == expected_index
    assert correction <= Q(rank * order, rank + order)
    ade.append((rank, order, correction, index, name))
    ade_checks.append({"pair": name, "rank": rank,
                       "first_normal_order": order,
                       "correction": str(correction), "index": index})


for rank in range(1, 12):
    for k in range(1, (rank + 1) // 2 + 1):
        add_row("A", rank, k - 1, k,
                Q(k * (rank + 1 - k), rank + 1),
                (rank + 1) // gcd(k, rank + 1), f"A{rank}^{k}")
    if rank >= 4:
        add_row("D", rank, 0, 2, Q(1), 2, f"D{rank}^1")
        add_row("D", rank, rank - 1, rank // 2, Q(rank, 4),
                2 if rank % 2 == 0 else 4, f"D{rank}^n")
add_row("E", 6, 0, 2, Q(4, 3), 3, "E6")
add_row("E", 7, 5, 3, Q(3, 2), 2, "E7")


# The positive integer passage bounds, and integral equality corrections.
passage_bounds = []
for d in (1, 2, 3):
    allowed = [t for t in range(1, 7) if t * t <= d * (6 - t)]
    equality = [t for t in allowed if t * t == d * (6 - t)]
    assert all(Q(t, d).denominator == 1 for t in equality)
    surviving = [t for t in allowed if t not in equality]
    assert surviving == ([1] if d == 1 else [1, 2])
    passage_bounds.append({"d": d, "Cauchy_allowed_t": allowed,
                           "integral_equality_excluded_t": equality,
                           "remaining_t": surviving})


# Irreducible E: the argument needs only nonrational order >= 2.
irreducible_gaps = []
for d in (1, 2, 3):
    rank = 8 + d
    order = 7
    required = Q(5) - Q(1, d)
    upper = Q(rank * order, rank + order)
    gap = required - upper
    assert gap > 0
    irreducible_gaps.append({"d": d, "ADE_rank_upper": rank,
                             "ADE_order_upper": order,
                             "required_correction": str(required),
                             "harmonic_upper": str(upper),
                             "positive_gap": str(gap)})
assert [row["positive_gap"] for row in irreducible_gaps] == [
    "1/16", "13/34", "7/18"]


def compositions(total, length):
    """All weak compositions, including zeros and a single positive part."""
    if length == 1:
        yield (total,)
    else:
        for value in range(total + 1):
            for tail in compositions(total - value, length - 1):
                yield (value,) + tail


def dihedral_representative(weights):
    size = len(weights)
    reversed_weights = tuple(reversed(weights))
    orbit = [weights[i:] + weights[:i] for i in range(size)]
    orbit += [reversed_weights[i:] + reversed_weights[:i]
              for i in range(size)]
    return min(orbit)


def cycle_matrix(weights):
    size = len(weights)
    result = sp.diag(*(2 + value for value in weights))
    # For two vertices the cycle has two edges, hence off-diagonal -2.
    for i in range(size):
        j = (i + 1) % size
        result[i, j] -= 1
        result[j, i] -= 1
    ones = sp.ones(size, 1)
    assert result * ones == sp.Matrix(weights)
    assert (ones.T * result * ones)[0] == sum(weights)
    # Connected cycle energy plus a nonzero nonnegative diagonal term is
    # positive definite. Verify leading minors as an independent check.
    assert all(result[:i, :i].det() > 0 for i in range(1, size + 1))
    return result


# Every allowed multiset of ADE rows is generated by unbounded knapsack.
# A representative suffices for equal (rank,order,correction,index), since
# the later cycle constraints depend only on these four invariants.
states = {(0, 0, Q(0), 1): ()}
for rank, order, correction, index, name in ade:
    previous = list(states.items())
    for (rank0, order0, correction0, index0), configuration in previous:
        repeat = 1
        while rank0 + repeat * rank <= 11 and order0 + repeat * order <= 7:
            key = (rank0 + repeat * rank, order0 + repeat * order,
                   correction0 + repeat * correction, lcm(index0, index))
            states.setdefault(key, configuration + (name,) * repeat)
            repeat += 1
by_rank = defaultdict(list)
for (rank, order, correction, index), configuration in states.items():
    by_rank[rank].append((order, correction, index, configuration))

cycle_count = 0
column_count = 0
seen_data = set()
matches = []
for d in (1, 2, 3):
    for size in range(2, 10 + d):  # 2 <= size <= 9+d, including the bound.
        for weights in compositions(d, size):
            if weights != dihedral_representative(weights):
                continue
            matrix = cycle_matrix(weights)
            inverse = matrix.inv()
            cycle_count += 1
            for vertex in range(size):
                correction = Q(inverse[vertex, vertex])
                index = matrix_index(inverse[:, vertex])
                data = (d, size, correction, index)
                if data in seen_data:
                    continue
                seen_data.add(data)
                column_count += 1
                required = Q(5) - correction
                if required < 0:
                    continue
                for rank in range(10 + d - size):
                    for order, ade_q, ade_index, configuration in by_rank[rank]:
                        if ade_q != required:
                            continue
                        full_index = lcm(index, ade_index)
                        matches.append({
                            "d": d, "cycle_rank": size,
                            "cycle_diagonal": [2 + value for value in weights],
                            "selected_vertex_zero_based": vertex,
                            "nonrational_correction": str(correction),
                            "nonrational_index": index,
                            "ADE_rank": rank, "ADE_order": order,
                            "ADE_correction": str(ade_q),
                            "ADE_index": ade_index,
                            "ADE_configuration": list(configuration),
                            "compressed_mate_degree": full_index})

matches.sort(key=lambda row: (row["d"], row["cycle_rank"], row["ADE_rank"]))
expected = [
    (1, 2, "3/2", 7, 7, 2),
    (1, 2, "3/2", 8, 7, 2),
    (1, 4, "2", 6, 6, 2),
    (2, 4, "3/2", 7, 7, 2),
    (3, 4, "4/3", 8, 7, 6),
]
assert [(row["d"], row["cycle_rank"], row["nonrational_correction"],
         row["ADE_rank"], row["ADE_order"], row["compressed_mate_degree"])
        for row in matches] == expected
denominator_killed = [row for row in matches
                      if row["compressed_mate_degree"] <= 5]
survivors = [row for row in matches if row["compressed_mate_degree"] >= 6]
assert len(denominator_killed) == 4
assert {row["compressed_mate_degree"] for row in denominator_killed} == {2}
assert len(survivors) == 1
assert survivors[0]["ADE_configuration"] == ["A1^1"] * 6 + ["A2^1"]


# Explicitly check the full denominator of the final cusp column.
final_matrix = cycle_matrix((0, 0, 0, 3))
final_column = final_matrix.inv()[:, 1]
assert list(final_column) == [sp.Rational(5, 6), sp.Rational(4, 3),
                             sp.Rational(5, 6), sp.Rational(1, 3)]
assert matrix_index(final_column) == 6
assert Q(final_column[1]) == Q(4, 3)
assert Q(6, 2) + Q(2, 3) + Q(4, 3) == 5


# Normal-sheaf defects: the ideal correction at the met A1/A2 prime is one.
node_numerical = chain(1).inv()[0, 0]
a2_numerical = chain(2).inv()[0, 0]
node_gap = Q(1) - Q(node_numerical)
a2_gap = Q(1) - Q(a2_numerical)
assert node_gap == Q(1, 2)
assert a2_gap == Q(1, 3)
required_defect = 6 * node_gap + a2_gap
available_defect = Q(7) - Q(4)  # The final row forces e=0.
assert required_defect == Q(10, 3)
assert required_defect > available_defect

print(json.dumps({
    "status": "PASS",
    "scope": "conditional numerical reduction for normal quartic C0 carriers",
    "passage_bounds": passage_bounds,
    "irreducible_anticanonical_gaps": irreducible_gaps,
    "ADE_rows_checked_from_full_root_matrices": len(ade_checks),
    "ADE_data": ade_checks,
    "ADE_knapsack_states": len(states),
    "dihedral_cycle_matrices_checked": cycle_count,
    "distinct_cycle_correction_index_data": column_count,
    "exact_correction_matches": matches,
    "quadric_compression_exclusions": len(denominator_killed),
    "last_cycle_correction_column": list(map(str, final_column)),
    "last_cycle_denominator": matrix_index(final_column),
    "last_candidate_ADE_defect": str(required_defect),
    "last_candidate_global_available_defect": str(available_defect),
    "last_candidate_positive_defect_gap": str(required_defect - available_defect),
    "reduced_anticanonical_numerical_survivors_after_all_tests": 0,
    "remaining_geometric_lane": "reducible nonreduced anticanonical divisor",
}, indent=2))
