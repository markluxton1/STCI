#!/usr/bin/env python3
"""Exhaustive exact root-subsystem controls for the scoped dP4 torsion filter.

This is a finite lattice calculation, not a classification of all quartic
normalizations and not an STCI certificate.  Reflection closure enumerates
every embedded root subsystem of the forty-root D5 system.  Integer lattice
membership is checked independently using Hermite normal form and rational
projection, and compared with the signed-coordinate proof in the note.
"""

import hashlib
import json
from collections import Counter
from functools import reduce
from itertools import combinations, product
from math import gcd
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def vector(i, a, j, b):
    result = [0] * 5
    result[i], result[j] = a, b
    return tuple(result)


ROOTS = tuple(vector(i, a, j, b)
              for i, j in combinations(range(5), 2)
              for a, b in product((-1, 1), repeat=2))
INDEX = {root: i for i, root in enumerate(ROOTS)}
NEG = tuple(INDEX[tuple(-x for x in root)] for root in ROOTS)
REFLECT = tuple(tuple(INDEX[tuple(y - dot(alpha, beta) * x
                                    for x, y in zip(alpha, beta))]
                      for beta in ROOTS) for alpha in ROOTS)


def reflection_closure(subsystem, additional):
    found = set(subsystem)
    pending = [additional, NEG[additional]]
    while pending:
        a = pending.pop()
        if a in found:
            continue
        for b in tuple(found):
            for reflected in (REFLECT[a][b], REFLECT[b][a]):
                if reflected not in found:
                    pending.append(reflected)
        found.add(a)
    return tuple(sorted(found))


def all_subsystems():
    found = {()}
    queue = [()]
    for subsystem in queue:
        for additional in range(len(ROOTS)):
            if additional in subsystem:
                continue
            enlarged = reflection_closure(subsystem, additional)
            if enlarged not in found:
                found.add(enlarged)
                queue.append(enlarged)
    return queue


def coordinate_blocks(subsystem):
    adjacency = {i: [] for i in range(5)}
    for a in subsystem:
        root = ROOTS[a]
        i, j = [k for k, value in enumerate(root) if value]
        # epsilon_i*root_i = -epsilon_j*root_j makes this a difference.
        constraint = -root[i] * root[j]
        adjacency[i].append((j, constraint))
        adjacency[j].append((i, constraint))
    visited = set()
    blocks = []
    for first in range(5):
        if first in visited or not adjacency[first]:
            continue
        signs = {first: 1}
        pending = [first]
        balanced = True
        while pending:
            i = pending.pop()
            visited.add(i)
            for j, constraint in adjacency[i]:
                required = constraint * signs[i]
                if j in signs:
                    balanced = balanced and signs[j] == required
                else:
                    signs[j] = required
                    pending.append(j)
        coordinates = tuple(sorted(signs))
        # Check reflection closure gives the entire asserted A or D block.
        actual = {a for a in subsystem
                  if all(ROOTS[a][i] == 0 for i in range(5)
                         if i not in coordinates)}
        expected = {a for a, root in enumerate(ROOTS)
                    if all(root[i] == 0 for i in range(5)
                           if i not in coordinates)
                    and (not balanced or sum(signs[i] * root[i]
                                             for i in coordinates) == 0)}
        assert actual == expected
        blocks.append((coordinates, balanced, signs))
    return blocks


def abstract_type(blocks):
    components = []
    for coordinates, balanced, signs in blocks:
        size = len(coordinates)
        if balanced:
            components.append(f"A{size-1}")
        elif size == 2:
            components.extend(["A1", "A1"])
        elif size == 3:
            components.append("A3")
        else:
            components.append(f"D{size}")
    counts = Counter(components)
    return "+".join((str(count) if count > 1 else "") + name
                    for name, count in sorted(counts.items())) or "empty"


def exact_lattice_membership(subsystem):
    if not subsystem:
        return set(), set(), 1
    columns = sp.Matrix.hstack(*(sp.Matrix(ROOTS[a]) for a in subsystem))
    basis = hermite_normal_form(columns)
    rank = basis.cols
    inverse_gram = (basis.T * basis).inv()
    spanning, belonging = set(), set()
    for a, root in enumerate(ROOTS):
        v = sp.Matrix(root)
        coordinates = inverse_gram * basis.T * v
        if basis * coordinates == v:
            spanning.add(a)
            if all(value.q == 1 for value in coordinates):
                belonging.add(a)
    # gcd of maximal minors is [saturation in Z5 : R].
    minors = [abs(int(basis[list(rows), :].det()))
              for rows in combinations(range(5), rank)]
    z5_index = reduce(gcd, minors)
    return spanning, belonging, z5_index


def chamber_example(simple, expected, intersections, coefficients):
    subsystem = ()
    for root in simple:
        subsystem = reflection_closure(subsystem, INDEX[root])
    span_roots, lattice_roots, z5_index = exact_lattice_membership(subsystem)
    missing = span_roots - lattice_roots
    dominant = [ROOTS[a] for a in missing
                if all(dot(ROOTS[a], alpha) >= 0 for alpha in simple)]
    assert dominant == [expected]
    assert [dot(expected, alpha) for alpha in simple] == intersections
    basis = sp.Matrix.hstack(*(sp.Matrix(alpha) for alpha in simple))
    actual_coefficients = (basis.T * basis).inv() * basis.T * sp.Matrix(expected)
    assert list(actual_coefficients) == coefficients
    assert basis * actual_coefficients == sp.Matrix(expected)
    assert all(value >= 0 for value in actual_coefficients)
    assert any(value.q == 2 for value in actual_coefficients)
    assert dot(expected, expected) == 2
    return {
        "simple_roots": [list(root) for root in simple],
        "unique_dominant_missing_root": list(expected),
        "correction_coefficients": [str(value) for value in actual_coefficients],
        "strict_transform_intersections": intersections,
        "missing_root_count": len(missing),
        "saturation_index": z5_index // 2,
    }


def picard_binding():
    standard_simple = [vector(0, 1, 1, -1), vector(1, 1, 2, -1),
                       vector(2, 1, 3, -1), vector(3, 1, 4, -1),
                       vector(3, 1, 4, 1)]
    B = sp.Matrix.hstack(*(sp.Matrix(root) for root in standard_simple))
    # Pic basis is (h,e1,...,e5), with intersection diag(1,-1,...,-1).
    P = sp.Matrix([
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, -1],
        [-1, 1, 0, 0, -1],
        [0, -1, 1, 0, -1],
        [0, 0, -1, 1, 0],
        [0, 0, 0, -1, 0],
    ])
    form = sp.diag(1, -1, -1, -1, -1, -1)
    L = sp.Matrix([3, -1, -1, -1, -1, -1])
    assert P.T * form * P == -B.T * B
    assert L.T * form * P == sp.zeros(1, 5)
    assert int((P.T * form * P).det()) == -4
    pic_roots = set()
    for root in ROOTS:
        image = P * B.inv() * sp.Matrix(root)
        assert all(value.q == 1 for value in image)
        assert (image.T * form * image)[0] == -2
        assert (L.T * form * image)[0] == 0
        pic_roots.add(tuple(map(int, image)))
    expected = set()
    for i, j in combinations(range(1, 6), 2):
        root = [0] * 6
        root[i], root[j] = 1, -1
        expected.add(tuple(root))
        expected.add(tuple(-value for value in root))
    for triple in combinations(range(1, 6), 3):
        root = [1] + [0] * 5
        for i in triple:
            root[i] = -1
        expected.add(tuple(root))
        expected.add(tuple(-value for value in root))
    assert pic_roots == expected
    assert len(pic_roots) == 40


def main():
    picard_binding()
    subsystems = all_subsystems()
    assert len(subsystems) == 428
    type_counts, type_profiles = Counter(), {}
    exceptional = Counter()
    for subsystem in subsystems:
        blocks = coordinate_blocks(subsystem)
        typename = abstract_type(blocks)
        type_counts[typename] += 1
        span_roots, lattice_roots, z5_index = exact_lattice_membership(subsystem)
        # An ADE root lattice contains precisely its own norm-two roots.
        assert lattice_roots == set(subsystem)
        unbalanced = [block for block in blocks if not block[1]]
        # Balanced blocks have even total coordinate sum; D blocks impose
        # separate parities. Ambient D5 imposes only their total parity.
        sat_index = z5_index // 2 if unbalanced else z5_index
        assert sat_index == 2 ** max(0, len(unbalanced) - 1)
        missing = span_roots - lattice_roots
        predicted = set()
        for first, second in combinations(unbalanced, 2):
            for i, j in product(first[0], second[0]):
                for a, b in product((-1, 1), repeat=2):
                    predicted.add(INDEX[vector(i, a, j, b)])
        assert missing == predicted
        profile = (len(subsystem), len(missing), sat_index)
        type_profiles.setdefault(typename, set()).add(profile)
        if missing:
            assert typename in {"4A1", "2A1+A3"}
            assert sat_index == 2
            exceptional[typename] += 1
    assert exceptional == {"4A1": 15, "2A1+A3": 10}
    four_A1 = chamber_example(
        [vector(0, 1, 1, -1), vector(0, 1, 1, 1),
         vector(2, 1, 3, -1), vector(2, 1, 3, 1)],
        vector(0, 1, 2, 1), [1, 1, 1, 1], [sp.Rational(1, 2)] * 4)
    A3_two_A1 = chamber_example(
        [vector(0, 1, 1, -1), vector(1, 1, 2, -1),
         vector(1, 1, 2, 1), vector(3, 1, 4, -1),
         vector(3, 1, 4, 1)],
        vector(0, 1, 3, 1), [1, 0, 0, 1, 1],
        [sp.Integer(1)] + [sp.Rational(1, 2)] * 4)
    source = Path(__file__).resolve()
    report = {
        "status": "PASS",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "root_count": 40,
        "embedded_reflection_closed_subsystems": len(subsystems),
        "scope": "Necessary lattice obstruction on a weak degree-four del Pezzo resolution with L=-K and ADE exceptional locus.",
        "classifies_all_sectional_genus_one_normalizations": False,
        "STCI_resolution_claim": False,
        "type_counts": dict(sorted(type_counts.items())),
        "type_profiles_root_count_missing_roots_index": {
            name: [list(profile) for profile in sorted(profiles)]
            for name, profiles in sorted(type_profiles.items())},
        "only_nonprimitive_types": dict(sorted(exceptional.items())),
        "four_A1_chamber": four_A1,
        "A3_plus_two_A1_chamber": A3_two_A1,
        "necessary_mate_degree": "even",
    }
    target = source.parent.parent / "research/scratch/session-delpezzo-D5-torsion-filter-2026-10-09.json"
    target.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PASS: all 428 embedded D5 root subsystems, integer saturation, and both effective chambers")
    print(f"source sha256: {report['source_sha256']}")
    print(f"report: {target}")


if __name__ == "__main__":
    main()
