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
  - research/supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md
  - research/supplements/NORMAL_CARRIER_SYMBOLIC_TORSION.md
independent_audits:
  - research/supplements/NORMAL_CARRIER_SYMBOLIC_TORSION.md
accepted_in: "research/supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md"
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

- [Source proof](../supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-normal-index-socle-theorem)
- [Source proof](../supplements/NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-normal-carrier-torsion)
- [Independent audit](../supplements/NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-index12-filtered-compatibility)

## Dependencies and limitations

Canonical dependencies: STCI-R-0034, STCI-R-0001. Additional inherited premises are in the proof and audit.
- Indices six, twelve and higher are not excluded
- No conclusion for nonnormal or entirely-thick presentations

## Current proof navigation

The evidence paths above point directly to the retained mathematical proofs. Consolidation changes their location and incorporates reviewed corrections; the canonical statement and limitations remain unchanged. The [filtration chapter](../synthesis/03-infinitesimal-geometry.md) explains how these hypotheses differ from arbitrary STCI equations.
