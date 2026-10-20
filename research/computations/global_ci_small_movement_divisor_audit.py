#!/usr/bin/env python3
"""Exact finite enumeration for the conditional global-CI arithmetic system.

This enumerates integer solutions of (A) in the companion independent audit.
It does not test root Picard descent, ambient lifting, or geometric existence.
Exhaustion uses the proved small-r factorization and t=3 tail, rather than
an arbitrarily chosen search cutoff. Only 1 <= epsilon <= 8 is supported.
"""

import argparse
import json
from math import isqrt


def positive_divisors(n):
    small = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return sorted(set(small + [n // d for d in small]))


def valid(epsilon, r, s, a, b):
    return (
        r >= 2
        and s > r
        and 3 * r <= a <= b
        and a * b == 4 * r * s
        and (epsilon * s) % r == 0
        and 4 * r * (a + b)
        == 7 * r * (r + s) - epsilon * (s - r)
    )


def enumerate_candidates(epsilon):
    if not 1 <= epsilon <= 8:
        raise ValueError("The proved lattice reduction applies to epsilon=1,...,8.")
    cutoff_numerator = 3 * epsilon * (2 * epsilon + 1)
    small_r_max = cutoff_numerator // 5
    candidates = set()

    # Small orders: retain signed divisor pairs even if 5r-3epsilon <= 0.
    for r in range(2, small_r_max + 1):
        c = 7 * r - epsilon
        assert c > 0
        constant = 4 * r * r * (15 * r * r + epsilon * epsilon)
        for positive in positive_divisors(constant):
            for first in (positive, -positive):
                second = constant // first
                if (first + 16 * r * r) % c:
                    continue
                if (second + 16 * r * r) % c:
                    continue
                a = (first + 16 * r * r) // c
                b = (second + 16 * r * r) // c
                if a > b or a * b % (4 * r):
                    continue
                s = a * b // (4 * r)
                if valid(epsilon, r, s, a, b):
                    candidates.add((r, s, a, b))

    # Larger orders force s=3r. Odd epsilon gives a half-integral sum.
    if epsilon % 2 == 0:
        h = epsilon // 2
        constant = 48 * h * h
        for positive in positive_divisors(constant):
            for first in (positive, -positive):
                second = constant // first
                if first > second or (first + second) % 2:
                    continue
                r = (first + second) // 2 + 7 * h
                if 5 * r <= cutoff_numerator or (second - first) % 2:
                    continue
                difference = (second - first) // 2
                total = 7 * r - h
                if (total - difference) % 2 or (total + difference) % 2:
                    continue
                a = (total - difference) // 2
                b = (total + difference) // 2
                s = 3 * r
                if valid(epsilon, r, s, a, b):
                    candidates.add((r, s, a, b))

    return sorted(candidates)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("epsilon", nargs="*", type=int, default=list(range(1, 9)))
    parser.add_argument("--show-tuples", action="store_true")
    args = parser.parse_args()
    for epsilon in args.epsilon:
        candidates = enumerate_candidates(epsilon)
        record = {
            "epsilon": epsilon,
            "candidate_count": len(candidates),
            "maximum_surviving_r": max((row[0] for row in candidates), default=None),
        }
        if args.show_tuples:
            record["candidates_r_s_a_b"] = candidates
        print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
