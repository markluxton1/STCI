#!/usr/bin/env python3
"""Exact small-degree BF defect profile enumeration; no lci inference.

Uses only d0=d1=0, nonnegativity, superadditivity, complementary
self-duality, and d2<=1,d3<=2.  Supports are unlabeled: the global output
lists multisets of nonzero local profiles of total top defect b-7.

Proof of exhaustiveness.  Write n=b-1 and D=d_n.  Superadditivity with
d1=0 gives monotonicity, hence 0<=d_i<=D.  Complementary self-duality
determines the second half from the first; at an even n it also forces
2*d_(n/2)=D.  The loop exhausts the finite box for the first half,
checks that identity, and checks EVERY superadditivity inequality.
Every nonzero support point has D>=1, so a global configuration of
total top defect b-7 has at most b-7 points.  combinations_with_replacement
exhausts every unordered configuration in that bound, and the explicit
global d2/d3 checks retain exactly the requested configurations.

An independent short classification follows directly.  In all three
degrees, floor(n/2)*d2<=D<=b-7 gives d2=0.  For b9, central pairing forces
D even; at D2, d4=1 and d3=0 or1.  For b10, write a=d3,c=d4.  At D1 or2,
a=0 and 0<=c<=floor(D/2); at D3, (a,c)=(0,0),(0,1),(1,1).  For b11,
D is even and (a,c) satisfies 0<=a<=c<=D/2 and 2*a+c<=D.  At D2 this
gives (0,0),(0,1); at D4 it gives (0,0),(0,1),(0,2),(1,1),(1,2).
Complementary symmetry determines all remaining entries in each case.

The printed monomial embedding dimensions refer EXCLUSIVELY to
A_d=R-span(t^-d_i*x^i) in K[x]/(x^b), R=k[[t]].  Its reduction has
basis X_i and product X_i*X_j=t^(d_(i+j)-d_i-d_j)*X_(i+j).
An index i>0 contributes to embedding dimension exactly when every
split i=j+(i-j) has a strictly positive t-exponent.  Its socle is exactly
X_(b-1), by complementary symmetry, so the special fiber is Gorenstein.
Embedding dimension >=3 excludes a planar presentation only for A_d.
It DOES NOT exclude a nonmonomial filtered deformation with this same
profile: a filtered algebra can have embedding dimension smaller than
its associated graded algebra.
"""

from itertools import combinations_with_replacement, product
import json


def profiles(b, top):
    n = b - 1
    answers = []
    # Monotonicity follows from superadditivity with d1=0.  Every value
    # is therefore between zero and top, and symmetry determines the
    # second half.  This finite loop is exhaustive.
    for half in product(range(top + 1), repeat=n // 2 + 1):
        if half[:2] != (0, 0):
            continue
        d = [None] * b
        for i, value in enumerate(half):
            d[i] = value
            d[n-i] = top-value
        if any(d[i] + d[n-i] != top for i in range(b)):
            continue
        if d[2] > 1 or d[3] > 2:
            continue
        if any(d[i]+d[j] > d[i+j]
               for i in range(b) for j in range(b-i)):
            continue
        generators = [i for i in range(1, b)
                      if all(d[j]+d[i-j] < d[i] for j in range(1, i))]
        socle = [i for i in range(b)
                 if all(i+j >= b or d[i]+d[j] < d[i+j]
                        for j in range(1, b))]
        # Self-duality supplies the nonzero top product X_i*X_(n-i)
        # for every i<n.  Thus only X_n lies in the special-fiber socle.
        assert socle == [n]
        answers.append({
            "profile": d,
            "top": top,
            "first_nonzero": next((i for i, a in enumerate(d) if a), None),
            "monomial_generators": generators,
            "monomial_embedding_dimension": len(generators),
            "monomial_socle_indices": socle,
            "monomial_gorenstein": True,
        })
    return answers


def global_configurations(b, local):
    total = b-7
    nonzero = [p for p in local if p["top"]]
    configurations = []
    for size in range(1, total+1):
        for indices in combinations_with_replacement(range(len(nonzero)), size):
            parts = [nonzero[i] for i in indices]
            if sum(p["top"] for p in parts) != total:
                continue
            aggregate = [sum(p["profile"][i] for p in parts) for i in range(b)]
            if aggregate[2] > 1 or aggregate[3] > 2:
                continue
            configurations.append({
                "local_profiles": [p["profile"] for p in parts],
                "aggregate": aggregate,
                "first_nonzero": next((i for i,a in enumerate(aggregate) if a), None),
            })
    return configurations


def main():
    result = {}
    for b in (9, 10, 11):
        local = [p for top in range(b-6) for p in profiles(b, top)]
        configurations = global_configurations(b, local)
        result[b] = {"local": local, "global": configurations}
        assert all(p["profile"][2] == 0 for p in local)
        assert all(p["aggregate"][3] <= 1 for p in configurations)
        assert all(len(p["local_profiles"]) == 1
                   for p in configurations if p["aggregate"][3])
    # Exact local tables, listed by top and then lexicographic profile.
    expected = {
        9: {
            0: [(0,0,0,0,0,0,0,0,0)],
            1: [],
            2: [(0,0,0,0,1,2,2,2,2), (0,0,0,1,1,1,2,2,2)],
        },
        10: {
            0: [(0,0,0,0,0,0,0,0,0,0)],
            1: [(0,0,0,0,0,1,1,1,1,1)],
            2: [(0,0,0,0,0,2,2,2,2,2), (0,0,0,0,1,1,2,2,2,2)],
            3: [(0,0,0,0,0,3,3,3,3,3), (0,0,0,0,1,2,3,3,3,3),
                (0,0,0,1,1,2,2,3,3,3)],
        },
        11: {
            0: [(0,0,0,0,0,0,0,0,0,0,0)],
            1: [],
            2: [(0,0,0,0,0,1,2,2,2,2,2), (0,0,0,0,1,1,1,2,2,2,2)],
            3: [],
            4: [(0,0,0,0,0,2,4,4,4,4,4), (0,0,0,0,1,2,3,4,4,4,4),
                (0,0,0,0,2,2,2,4,4,4,4), (0,0,0,1,1,2,3,3,4,4,4),
                (0,0,0,1,2,2,2,3,4,4,4)],
        },
    }
    for b, by_top in expected.items():
        for top, table in by_top.items():
            actual = [tuple(p["profile"]) for p in result[b]["local"]
                      if p["top"] == top]
            assert actual == table, (b, top, actual)
    assert [len(result[b]["global"]) for b in (9,10,11)] == [2,6,8]
    assert [sum(p["first_nonzero"] <= 3 for p in result[b]["global"])
            for b in (9,10,11)] == [1,1,2]
    assert [sum(p["first_nonzero"] <= 4 for p in result[b]["global"])
            for b in (9,10,11)] == [2,3,6]
    expected_early3 = {
        9: [(0,0,0,1,1,1,2,2,2)],
        10: [(0,0,0,1,1,2,2,3,3,3)],
        11: [(0,0,0,1,1,2,3,3,4,4,4), (0,0,0,1,2,2,2,3,4,4,4)],
    }
    for b, table in expected_early3.items():
        actual = [tuple(p["aggregate"]) for p in result[b]["global"]
                  if p["aggregate"][3]]
        assert actual == table, (b, actual)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
