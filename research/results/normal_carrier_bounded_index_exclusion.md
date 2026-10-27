---
id: STCI-R-0035
title: "Bounded-index normal-carrier exclusion for C0"
kind: theorem
status: proved
scope:
  characteristic: "characteristic zero"
  curve: "fixed rational quartic C0 in P3"
  hypotheses:
    - "Normal integral hypersurface carrier with a mate supported on C0"
    - "Every actual on-curve local Cartier index is at most four"
    - "Inherited normal-carrier torsion reduction and quadratic direction obstruction"
statement: "No such normal integral carrier of C0 admits a mate in any degree."
dependencies: 
  - STCI-R-0034
  - STCI-R-0001
evidence:
  - research/notes/2026-10-14-generalization-normal-index-socle-theorem.md
  - research/notes/2026-10-14-generalization-normal-carrier-torsion.md
independent_audits:
  - research/notes/2026-10-14-generalization-index12-filtered-compatibility.md
accepted_in: research/HISTORICAL_STRUCTURAL_ADJUDICATION_2026-10-26.md
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Indices six, twelve and higher are not excluded"
  - "No conclusion for nonnormal or entirely-thick presentations"
---

# Bounded-index normal-carrier exclusion for C0

## Statement and hypotheses

No such normal integral carrier of C0 admits a mate in any degree.

Required hypotheses:
- Normal integral hypersurface carrier with a mate supported on C0
- Every actual on-curve local Cartier index is at most four
- Inherited normal-carrier torsion reduction and quadratic direction obstruction

## Proof and verification

- [Source proof](../notes/2026-10-14-generalization-normal-index-socle-theorem.md)
- [Source proof](../notes/2026-10-14-generalization-normal-carrier-torsion.md)
- [Independent audit](../notes/2026-10-14-generalization-index12-filtered-compatibility.md)
- [Claim-level acceptance](../HISTORICAL_STRUCTURAL_ADJUDICATION_2026-10-26.md)

## Dependencies and limitations

Canonical dependencies: STCI-R-0034, STCI-R-0001. Additional inherited premises are in the proof and audit.
- Indices six, twelve and higher are not excluded
- No conclusion for nonnormal or entirely-thick presentations
