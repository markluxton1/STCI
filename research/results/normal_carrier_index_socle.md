---
id: STCI-R-0034
title: "Normal-carrier local Cartier-index and socle compatibility"
kind: theorem
status: proved
scope:
  characteristic: "characteristic zero"
  curve: "smooth curve on a normal integral carrier surface"
  hypotheses:
    - "Actual mate with divisor nC on the carrier"
    - "Actual local Cartier index r divides n, with k=n/r"
    - "Generic transverse complete intersection curvilinear"
statement: "At P, the actual top ordinary-power socle defects satisfy D_n,P=(k-1)A_F,P+k D_r,P. The ordinary curvilinear filtration satisfies 2 sum_i length(T_i)_P=n D_n,P."
dependencies: []
evidence:
  - research/supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md
independent_audits:
  - research/supplements/NORMAL_CARRIER_SYMBOLIC_TORSION.md
accepted_in: "research/supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Actual local Cartier index cannot be replaced by surface multiplicity"
  - "No unconditional carrier exclusion follows"
---

# Normal-carrier local Cartier-index and socle compatibility

## Statement and hypotheses

At P, the actual top ordinary-power socle defects satisfy D_n,P=(k-1)A_F,P+k D_r,P. The ordinary curvilinear filtration satisfies 2 sum_i length(T_i)_P=n D_n,P.

Required hypotheses:
- Actual mate with divisor nC on the carrier
- Actual local Cartier index r divides n, with k=n/r
- Generic transverse complete intersection curvilinear

## Proof and verification

- [Source proof](../supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-normal-index-socle-theorem)
- [Independent audit](../supplements/NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-index12-filtered-compatibility)

## Dependencies and limitations

Inherited premises are described in the proof and audit.
- Actual local Cartier index cannot be replaced by surface multiplicity
- No unconditional carrier exclusion follows

## Current proof navigation

The evidence paths above point directly to the retained mathematical proofs. Consolidation changes their location and incorporates reviewed corrections; the canonical statement and limitations remain unchanged. The [filtration chapter](../synthesis/03-infinitesimal-geometry.md) explains how these hypotheses differ from arbitrary STCI equations.
