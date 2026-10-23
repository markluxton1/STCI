---
id: STCI-R-0020
title: "Characteristic-dependent conormal splitting of the fixed rational quartic"
kind: theorem
status: proved
scope:
  characteristic: "0 and 2 (more generally characteristic not 2 versus 2)"
  curve: "fixed C0=[s^4:s^3t:st^3:t^4]"
  hypotheses:
    - "Base field; conormal sheaf on the smooth embedded curve"
statement: "N^*_{C0/P3} is O(-7)^2 when 2 is invertible, and O(-8) direct sum O(-6) in characteristic 2."
dependencies: []
evidence:
  - "research/notes/2026-10-23-quartic-characteristic-conormal.md"
  - "research/computations/verify_normal_bundle.py"
independent_audits:
  - "research/notes/2026-10-23-quartic-geometry-symbol-independent-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-23-44.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not alone obstruct an arbitrary pair of quartic STCI equations."
---
# Characteristic-dependent conormal splitting

## Statement
For the fixed smooth rational quartic C0, E=I/I² fits into 0→O(-8)→E→O(-6)→0. Its extension class is a nonzero scalar multiple of 2 in H¹(O(-2)). Hence E=O(-7)² in characteristic different from 2 and E=O(-8)⊕O(-6) in characteristic 2.

## Hypotheses and quantifiers
All statements concern the specified embedded curve, not every rational quartic embedding.

## Proof outline
The unique quadric yields the conormal extension. Its explicit two-chart transition has off-diagonal coefficient proportional to 2u⁻¹. A nonzero class yields the balanced extension; in characteristic two it splits.

## Dependencies
None of the project’s higher-degree STCI exclusions is used.

## Evidence and verification
See the source note, independent geometry audit, and normal-bundle transition verifier. Clean GitHub Actions verification of the October 23 related symbol comparison is [run 39972680627](https://github.com/markluxton1/STCI/actions/runs/39972680627).

## Consequences
The symmetric-power splitting in characteristic two differs from the balanced characteristic-zero formula.

## Limitations
This conormal statement does not establish the global (4,4) exclusion.
