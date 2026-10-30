---
id: STCI-R-0033
title: "Constant first-relation quadratic lifting obstruction"
kind: theorem
status: proved
scope:
  characteristic: "characteristic zero; factor multiplicity nonzero in arbitrary characteristic"
  curve: "smooth rational curve with balanced conormal bundle"
  hypotheses:
    - "Actual embedded thickening with constant first relation f"
    - "Next initial relation space consists only of fV"
statement: "Every linear factor direction m of f with multiplicity nonzero in the field has vanishing quadratic obstruction h_m. For fixed C0 in characteristic zero, inherited nonvanishing of all h_m excludes zero-defect constant-graded-CI equality models."
dependencies: 
  - STCI-R-0032
evidence:
  - research/notes/2026-10-13-generalization-thick-equality-geometry.md
independent_audits:
  - research/notes/2026-10-13-generalization-thick-relation-obstruction-independent-audit.md
accepted_in: research/HISTORICAL_STRUCTURAL_ADJUDICATION_2026-10-26.md
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Uses inherited P-010 direction classes for the C0 consequence"
  - "Does not exclude moving first relations, extra next-order relations, or positive-defect models"
---

# Constant first-relation quadratic lifting obstruction

## Statement and hypotheses

Every linear factor direction m of f with multiplicity nonzero in the field has vanishing quadratic obstruction h_m. For fixed C0 in characteristic zero, inherited nonvanishing of all h_m excludes zero-defect constant-graded-CI equality models.

Required hypotheses:
- Actual embedded thickening with constant first relation f
- Next initial relation space consists only of fV

## Proof and verification

- [Source proof](../notes/2026-10-13-generalization-thick-equality-geometry.md)
- [Independent audit](../notes/2026-10-13-generalization-thick-relation-obstruction-independent-audit.md)
- [Claim-level acceptance](../HISTORICAL_STRUCTURAL_ADJUDICATION_2026-10-26.md)

## Dependencies and limitations

Canonical dependencies: STCI-R-0032. Additional inherited premises are in the proof and audit.
- Uses inherited P-010 direction classes for the C0 consequence
- Does not exclude moving first relations, extra next-order relations, or positive-defect models

## Permanent evidence navigation

The `research/notes/` metadata above preserves historical provenance identifiers, not live paths on this branch. For the retained mathematical argument, hypotheses, and links into detailed supplements, follow [the consolidated subject chapter](../synthesis/03-infinitesimal-geometry.md). The original source identifiers are retained for audit provenance; this navigation link does not change the theorem's scope or status.
