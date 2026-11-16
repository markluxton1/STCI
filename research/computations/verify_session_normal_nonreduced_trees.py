#!/usr/bin/env python3
"""Enumerate all necessary nonreduced exceptional-tree numerical data.

This checks a finite superset of configurations of classified normal
quartic surfaces. It does not establish realizability of a graph or a
local passage. The geometric Type-D passage bound is proved separately
in the companion note; its only arithmetic use is the last filter t=1.

Dependencies: standard library and SymPy through the earlier companion.
Output: one JSON report to stdout. This source makes no file writes.
"""
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction as Q
from io import StringIO
from itertools import combinations_with_replacement
from math import lcm
from pathlib import Path
import json
import runpy

with redirect_stdout(StringIO()):
    previous = runpy.run_path(str(Path(__file__).with_name(
        "verify_session_normal_carrier_progress.py")))
by_rank = previous["by_rank"]


def rooted_code(adjacency, node, parent=-1, weights=None):
    children = tuple(sorted(rooted_code(adjacency, child, node, weights)
                            for child in adjacency[node] if child != parent))
    return (0 if weights is None else weights[node], children)


def canonical_code(adjacency, weights=None):
    """Exact tree-isomorphism invariant, checking every possible root."""
    return min(rooted_code(adjacency, node, weights=weights)
               for node in range(len(adjacency)))


def next_trees(trees):
    """Every tree has a leaf: add a leaf everywhere and deduplicate."""
    result = {}
    for adjacency in trees:
        size = len(adjacency)
        for vertex in range(size):
            larger = tuple(tuple(list(neighbors) +
                                 ([size] if node == vertex else []))
                           for node, neighbors in enumerate(adjacency))
            larger += ((vertex,),)
            result.setdefault(canonical_code(larger), larger)
    return list(result.values())


def elimination_order(adjacency):
    parents = [-1] * len(adjacency)
    order = [0]
    for node in order:
        for child in adjacency[node]:
            if child != parents[node]:
                parents[child] = node
                order.append(child)
    assert len(order) == len(adjacency)
    return parents, order


def tree_solve(adjacency, diagonal, right_side, prepared):
    """Exact leaf Schur elimination; None iff the matrix is not positive.

    Leaf pivot p subtracts 1/p from its parent and adds rhs/p to the
    parent right side. Positive pivots characterize positive definiteness.
    Back-substitution gives the solution, checked in the original system.
    """
    parents, order = prepared
    pivots = list(map(Q, diagonal))
    right = list(map(Q, right_side))
    for node in reversed(order[1:]):
        if pivots[node] <= 0:
            return None
        parent = parents[node]
        pivots[parent] -= 1 / pivots[node]
        right[parent] += right[node] / pivots[node]
    if pivots[0] <= 0:
        return None
    solution = [Q(0)] * len(adjacency)
    solution[0] = right[0] / pivots[0]
    for node in order[1:]:
        solution[node] = (right[node] + solution[parents[node]]) / pivots[node]
    assert all(diagonal[node] * solution[node] -
               sum(solution[child] for child in adjacency[node]) == right_side[node]
               for node in range(len(adjacency)))
    return solution


def diagonal_excesses(size):
    """All nonnegative vectors of positive sum at most three, once each."""
    for total in (1, 2, 3):
        for positions in combinations_with_replacement(range(size), total):
            excess = [0] * size
            for vertex in positions:
                excess[vertex] += 1
            yield excess


trees = [((1,), (0,))]
cycles = {}
tree_counts = {}
diagonal_trials = 0
all_correction_matches = []
post_compression_candidates = []

for size in range(2, 13):
    if size > 2:
        trees = next_trees(trees)
    tree_counts[size] = len(trees)
    for adjacency in trees:
        prepared = elimination_order(adjacency)
        for excess in diagonal_excesses(size):
            diagonal_trials += 1
            diagonal = [2 + value for value in excess]
            coefficients = tree_solve(adjacency, diagonal, excess, prepared)
            if coefficients is None:
                continue
            if any(value.denominator != 1 or value < 1 for value in coefficients):
                continue
            d = sum(value * amount for value, amount in zip(coefficients, excess))
            if d not in (1, 2, 3) or size > 9 + d:
                continue
            key = canonical_code(adjacency, diagonal)
            if key in cycles:
                continue
            coefficients = list(map(int, coefficients))
            assert max(coefficients) > 1
            assert all(len(adjacency[vertex]) == 1 and
                       coefficients[adjacency[vertex][0]] == 2
                       for vertex, value in enumerate(coefficients) if value == 1)
            cycle_number = len(cycles)
            cycle = {"number": cycle_number, "d": int(d), "rank": size,
                     "adjacency": adjacency, "diagonal": diagonal,
                     "anticanonical_coefficients": coefficients}
            cycles[key] = cycle
            for vertex, passage in enumerate(coefficients):
                if passage not in ([1] if d == 1 else [1, 2]):
                    continue
                unit = [0] * size
                unit[vertex] = 1
                column = tree_solve(adjacency, diagonal, unit, prepared)
                correction = column[vertex]
                index = lcm(*(value.denominator for value in column))
                required = 6 - passage - correction
                if required < 0:
                    continue
                for rank in range(10 + int(d) - size):
                    for order, ade_q, ade_index, configuration in by_rank[rank]:
                        if ade_q != required:
                            continue
                        degree = lcm(index, ade_index)
                        row = {"cycle_number": cycle_number,
                               "d": int(d), "rankE": size,
                               "selected_vertex_zero_based": vertex,
                               "t": passage,
                               "nonrational_correction": str(correction),
                               "nonrational_index": index,
                               "nonrational_full_column": list(map(str, column)),
                               "ADE_rank": rank, "ADE_order": order,
                               "ADE_correction": str(ade_q),
                               "ADE_index": ade_index,
                               "ADE_configuration": list(configuration),
                               "compressed_mate_degree": degree}
                        all_correction_matches.append(row)
                        if degree >= 6:
                            post_compression_candidates.append(row)

assert list(tree_counts.values()) == [1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551]
assert diagonal_trials == 381802
assert len(cycles) == 195
assert len(post_compression_candidates) == 12
assert all(row["d"] == 3 and row["t"] == 2
           for row in post_compression_candidates)
assert Counter(row["nonrational_correction"] for row in post_compression_candidates) == {
    "2": 8, "17/6": 4}
assert {row["compressed_mate_degree"] for row in post_compression_candidates} == {6, 12}

# External geometric input: Type D has t=1 on a smooth embedded curve.
# Its three sections through sigma(E) factor as section(E) times a bpf
# pullback of O_P2(1), so the curve maximal ideal has exactly that divisor.
type_d_survivors = [row for row in post_compression_candidates
                    if row["d"] != 3 or row["t"] == 1]
assert type_d_survivors == []

print(json.dumps({
    "status": "PASS",
    "scope": "necessary finite nonreduced normal-quartic exceptional-tree data",
    "unweighted_nonisomorphic_tree_counts_by_size": tree_counts,
    "diagonal_modifications_tested": diagonal_trials,
    "admissible_positive_integral_canonical_cycles": len(cycles),
    "admissible_cycles_by_d": dict(Counter(row["d"] for row in cycles.values())),
    "all_exact_correction_matches": len(all_correction_matches),
    "mate_degree_at_most_five_compression_exclusions":
        len(all_correction_matches) - len(post_compression_candidates),
    "post_compression_candidate_count": len(post_compression_candidates),
    "post_compression_candidates": post_compression_candidates,
    "Type_D_geometric_passage_input": "t=1 on a smooth embedded curve",
    "survivors_after_Type_D_passage": len(type_d_survivors),
    "all_admissible_cycles": list(cycles.values()),
}, indent=2))
