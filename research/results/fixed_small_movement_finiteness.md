---
id: STCI-R-0015
title: "Finite arithmetic possibilities for each movement one through eight"
kind: reduction
status: exact_reduction
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "fixed C0 in P3"
  hypotheses:
    - "All hypotheses of STCI-R-0013"
    - "Fixed integer movement 1<=epsilon<=8"
statement: "For each fixed epsilon in 1,...,8 only finitely many numerical tuples (r,s;a,b) satisfy the necessary actual-generator identities and degree bounds; the exact unordered arithmetic counts are respectively 0,6,4,11,9,19,9,19."
dependencies:
  - STCI-R-0013
evidence:
  - "research/notes/2026-10-19-global-ci-filtration-investigation.md"
independent_audits:
  - "research/notes/2026-10-19-global-ci-filtration-independent-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-21.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "No finiteness conclusion is claimed for epsilon>=9."
  - "Finite arithmetic lists are not realizability lists or STCI classifications."
---

# Finite arithmetic possibilities for each movement one through eight

## Statement and hypotheses

For each fixed epsilon in 1,...,8 only finitely many numerical tuples (r,s;a,b) satisfy the necessary actual-generator identities and degree bounds; the exact unordered arithmetic counts are respectively 0,6,4,11,9,19,9,19.

- All hypotheses of STCI-R-0013
- Fixed integer movement 1<=epsilon<=8

## Proof, verification, and acceptance

The independent arithmetic proof treats small-order exceptional denominators using signed divisor pairs and obtains a strict large-order cutoff and integral factorization. The verifier `research/computations/global_ci_small_movement_divisor_audit.py` reproduces the counts.

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above. Scope acceptance for this promotion is documented in [the reconciliation decision](../RECONCILIATION_2026-10-21.md); that decision does not replace the source proof.

## Limitations

- No finiteness conclusion is claimed for epsilon>=9.
- Finite arithmetic lists are not realizability lists or STCI classifications.

## Permanent evidence navigation

The `research/notes/` metadata preserves original provenance identifiers rather than live branch paths. The [consolidated subject chapter](../synthesis/03-infinitesimal-geometry.md) provides a current entry point to the mathematical argument and its retained detailed supplements. This route does not alter the record's hypotheses, proof status, or historical audit identity.
