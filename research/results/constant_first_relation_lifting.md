---
id: STCI-R-0033
title: "Constant first-relation quadratic lifting obstruction"
kind: theorem
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
  - research/arguments/equations/global_lifting_interfaces.md#quadratic-formal-neighborhood-obstruction-to-zero-defect-thickenings
independent_audits:
  - research/arguments/equations/global_lifting_interfaces.md#quadratic-formal-neighborhood-obstruction-to-zero-defect-thickenings
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

- [Source proof](../arguments/equations/global_lifting_interfaces.md#source-2026-10-13-generalization-thick-equality-geometrymd)
- [Independent audit](../arguments/equations/global_lifting_interfaces.md#source-2026-10-13-generalization-thick-relation-obstruction-independent-auditmd)

## Dependencies and limitations

Dependencies: STCI-R-0032. Additional inherited premises are in the proof and audit.
- Uses inherited P-010 direction classes for the C0 consequence
- Does not exclude moving first relations, extra next-order relations, or positive-defect models
