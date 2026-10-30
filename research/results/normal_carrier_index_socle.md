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
  - research/notes/2026-10-14-generalization-normal-index-socle-theorem.md
independent_audits:
  - research/notes/2026-10-14-generalization-index12-filtered-compatibility.md
accepted_in: research/HISTORICAL_STRUCTURAL_ADJUDICATION_2026-10-26.md
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

- [Source proof](../notes/2026-10-14-generalization-normal-index-socle-theorem.md)
- [Independent audit](../notes/2026-10-14-generalization-index12-filtered-compatibility.md)
- [Claim-level acceptance](../HISTORICAL_STRUCTURAL_ADJUDICATION_2026-10-26.md)

## Dependencies and limitations

Inherited premises are described in the proof and audit.
- Actual local Cartier index cannot be replaced by surface multiplicity
- No unconditional carrier exclusion follows

## Permanent evidence navigation

The `research/notes/` metadata above preserves historical provenance identifiers, not live paths on this branch. For the retained mathematical argument, hypotheses, and links into detailed supplements, follow [the consolidated subject chapter](../synthesis/04-carriers.md). The original source identifiers are retained for audit provenance; this navigation link does not change the theorem's scope or status.
