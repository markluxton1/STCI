#!/usr/bin/env python3
"""Exact arithmetic for the primitive curvilinear C0 degree budget.

Scope: characteristic zero, C0 the fixed rational quartic, sole-support
proper CI of degrees 2 <= a <= b, primitive transverse length m=ab/4>1.
This enumerates necessary numerical data; it certifies no global pair.

With L=O(-q), conormal quotients and primitive adjunction give
1 <= q <= 7 and (q*a-16)*(q*b-16)=4*((q-7)**2+15).
Both factors are positive: if both were negative their product would be
at most (16-2*q)**2, strictly smaller than the right side by 8*q.
Positive divisor pairs therefore give an exhaustive finite enumeration.
"""

import json
from math import isqrt


def enumerate_rows():
    rows = []
    for q in range(1, 8):
        target = 4 * ((q - 7) ** 2 + 15)
        for left in range(1, isqrt(target) + 1):
            if target % left:
                continue
            right = target // left
            if (left + 16) % q or (right + 16) % q:
                continue
            a, b = (left + 16) // q, (right + 16) // q
            if a < 2 or a * b % 4:
                continue
            m = a * b // 4
            if m <= 1:
                continue
            if q * (m - 1) != 4 * (a + b) - 14:
                raise ArithmeticError("Factorization and adjunction disagree")
            rows.append({"q": q, "a": a, "b": b, "m": m})
    return sorted(rows, key=lambda row: (row["q"], row["a"], row["b"]))


if __name__ == "__main__":
    rows = enumerate_rows()
    print(json.dumps({
        "status": "necessary numerical data only",
        "primitive_curvilinear_only": True,
        "row_count": len(rows),
        "maximum_degree": max(row["b"] for row in rows),
        "rows": rows,
    }, indent=2))
