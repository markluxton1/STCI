---
id: STCI-R-0014
title: "Six necessary movement-two numerical rows"
kind: reduction
status: exact_reduction
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "fixed C0 in P3"
  hypotheses:
    - "All hypotheses of STCI-R-0013"
    - "Movement epsilon=2"
statement: "The unordered necessary numerical quadruples (r,s;a,b) are exactly (2,8;8,8), (2,12;6,16), (6,21;18,28), (14,42;48,49), (15,45;50,54), (20,60;64,75). These are necessary arithmetic candidates, not geometric STCI realizations."
dependencies:
  - STCI-R-0001
  - STCI-R-0008
  - STCI-R-0010
  - STCI-R-0011
  - STCI-R-0013
evidence:
  - "research/notes/2026-10-19-global-ci-filtration-investigation.md"
independent_audits:
  - "research/notes/2026-10-19-numerical-first-root-independent-audit.md"
  - "research/notes/2026-10-19-global-ci-filtration-independent-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-21.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not exhaust arbitrary characteristic-zero STCI pairs."
  - "Picard descent, singular full roots, formal lifting, and actual homogeneous equations remain untested for the rows."
  - "STCI-R-0011 ensures reduction of moving full roots only under its own Picard-descent interface."
---

# Six necessary movement-two numerical rows

## Statement and hypotheses

The unordered necessary numerical quadruples (r,s;a,b) are exactly (2,8;8,8), (2,12;6,16), (6,21;18,28), (14,42;48,49), (15,45;50,54), (20,60;64,75). These are necessary arithmetic candidates, not geometric STCI realizations.

- All hypotheses of STCI-R-0013
- Movement epsilon=2

## Proof, verification, and acceptance

The audit verifies global degree and first-blowup inequalities and a complete signed-divisor/discriminant argument; the exact Python arithmetic verifier cross-checks the finite candidate list but is not used in place of an exhaustion proof.

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above. Scope acceptance for this promotion is documented in [the reconciliation decision](../RECONCILIATION_2026-10-21.md); that decision does not replace the source proof.

## Limitations

- Does not exhaust arbitrary characteristic-zero STCI pairs.
- Picard descent, singular full roots, formal lifting, and actual homogeneous equations remain untested for the rows.
- STCI-R-0011 ensures reduction of moving full roots only under its own Picard-descent interface.
