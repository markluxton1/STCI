# Singular-locus Delta continuation: exact validation

Date: 2026-10-24.

Report: [continuation](../../notes/2026-10-24-delta-singular-locus-continuation.md).

Review: [mathematical review and scope](../../notes/2026-10-24-delta-singular-locus-review.md).

Commands, from the repository root:

~~~sh
python3 -B research/computations/verify_delta_singular_identities_2026_10_24.py
/opt/homebrew/bin/M2 --script research/computations/verify_delta_singular_families_2026_10_24.m2
python3 -B research/computations/validate_records.py
git diff --check
~~~

Verified runtime: Python 3.15.0, Macaulay2 1.26.06. Python uses only the standard library. The M2 executable path is host-specific; a compatible Macaulay2 can run the same script.

| Output | Boundary |
|---|---|
| [polynomial-identities.log](polynomial-identities.log) | Independent full-product expansions: 24 punctual cases and 35 recursive cases, their exact syzygies, initials, weights, and staircase counts |
| [rees-families.log](rees-families.log) | Full Rees initial ideals in 12 punctual and 12 recursive samples, lifted Hilbert–Burch matrices, plus one supported quadruple |
| [canonical-records.log](canonical-records.log) | Canonical metadata validation only |

All three commands completed with exit code zero. Local report/review links and staged whitespace were checked. These finite samples support the proofs; no fixed finite grid proves an arbitrary-parameter theorem.

No inherited mathematical exclusion scripts were rerun. No canonical promotion, global support exhaustion for the projective carrier upgrades, or unrestricted STCI conclusion is claimed.
