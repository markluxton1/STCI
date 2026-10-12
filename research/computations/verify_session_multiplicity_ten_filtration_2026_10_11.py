#!/usr/bin/env python3
"""Enumerate necessary saturated-filtration DEGREE data for CI(5,8).

This is not an embedded-structure classification or an STCI exclusion.
The mathematical input is explained in the associated audit note.
Uses Python's standard library only; performs no file mutations.
"""

from itertools import product
import json


def defect_sequence(a, b, c, top):
    return [0, 0, a, b, c, top - c, top - b, top - a, top, top]


def original_conditions(sequence, top):
    return (
        all(value >= 0 for value in sequence)
        and all(sequence[i] + sequence[9 - i] == top for i in range(10))
        and all(
            sequence[i] + sequence[j] <= sequence[i + j]
            for i in range(10)
            for j in range(10 - i)
        )
    )


def compact_conditions(a, b, c, top):
    return (
        0 <= a <= b <= c
        and 2 * a <= c
        and 2 * c <= top
        and a + b + c <= top
        and 3 * b <= top
    )


def main():
    results = []
    checked = 0
    for line_degree in (-7, -6, -5):
        top = -38 - 9 * line_degree
        retained = []
        raw_count = 0
        for a, b, c in product(range(top + 1), repeat=3):
            sequence = defect_sequence(a, b, c, top)
            original = original_conditions(sequence, top)
            compact = compact_conditions(a, b, c, top)
            if original != compact:
                raise AssertionError((line_degree, a, b, c, original, compact))
            checked += 1
            if not compact:
                continue
            raw_count += 1
            if line_degree == -7 and a == 0:
                continue  # Separate, established P-010 primitive-triple input.
            if 10 + 45 * line_degree + sum(sequence) != -180:
                raise AssertionError("Euler-characteristic inconsistency")
            retained.append([a, b, c])
        results.append(
            {
                "line_degree": line_degree,
                "direction_degree": line_degree + 7,
                "top_defect_degree": top,
                "raw_necessary_degree_count": raw_count,
                "count_after_P010": len(retained),
                "triples_after_P010": retained,
            }
        )
    counts = [row["count_after_P010"] for row in results]
    if counts != [198, 97, 13]:
        raise AssertionError(counts)
    print(
        json.dumps(
            {
                "status": "PASS",
                "scope": "necessary numerical data only; no existence or exclusion",
                "bounded_triples_checked_for_equivalence": checked,
                "total_necessary_degree_triples_after_P010": sum(counts),
                "results": results,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
