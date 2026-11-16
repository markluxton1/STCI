---
id: STCI-R-0015
title: "Finite arithmetic possibilities for each movement one through eight"
kind: reduction
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
  - "research/arguments/normal-geometry/normal_flatness_and_filtered_ci.md"
independent_audits:
  - "research/arguments/normal-geometry/normal_flatness_and_filtered_ci.md"
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

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above.

## Limitations

- No finiteness conclusion is claimed for epsilon>=9.
- Finite arithmetic lists are not realizability lists or STCI classifications.
