"""Exact arithmetic companion to the new normal-carrier index theorem.

Input theorems, proved in the accompanying 2026-10-14 note:
  R | L, a | 16 R, g=gcd(a,4), t=R/gcd(R,a/g), b_min=4t/g.
Accepted low-degree carrier exclusions make b_min>4 necessary.
This script checks only NEW finite integer consequences; it does not
replay a normalization, ADE, or carrier exclusion computation.
"""

from math import gcd
import json


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def surviving_index_data(bound):
    rows = []
    for index in divisors(bound):
        for degree in divisors(16 * index):
            if degree <= 4:
                continue
            common = gcd(degree, 4)
            order = index // gcd(index, degree // common)
            mate_degree = (4 // common) * order
            if mate_degree > 4:
                rows.append({
                    "carrier_degree": degree,
                    "curve_cartier_index": index,
                    "primitive_class_order": order,
                    "minimum_mate_degree": mate_degree,
                })
    return rows


if __name__ == "__main__":
    result = {str(bound): surviving_index_data(bound)
              for bound in (2, 3, 4, 6, 12)}
    assert all(result[str(bound)] == [] for bound in (2, 3, 4, 6))
    assert result["12"] == [
        {"carrier_degree": 6, "curve_cartier_index": 12,
         "primitive_class_order": 4, "minimum_mate_degree": 8},
        {"carrier_degree": 8, "curve_cartier_index": 12,
         "primitive_class_order": 6, "minimum_mate_degree": 6},
    ]
    print(json.dumps(result, indent=2, sort_keys=True))
