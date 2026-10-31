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
  - "research/supplements/NORMAL_FLATNESS_AND_FILTERED_CI.md"
independent_audits:
  - "research/supplements/NORMAL_FLATNESS_AND_FILTERED_CI.md"
accepted_in: "research/supplements/NORMAL_FLATNESS_AND_FILTERED_CI.md"
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

## Current proof navigation

The evidence paths above point directly to the retained mathematical proofs. Consolidation changes their location and incorporates reviewed corrections; the canonical statement and limitations remain unchanged. The [filtration chapter](../synthesis/03-infinitesimal-geometry.md) explains how these hypotheses differ from arbitrary STCI equations.
