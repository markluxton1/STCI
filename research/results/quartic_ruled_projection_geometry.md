---
id: STCI-R-0028
title: "Ruled projection and normalization models"
kind: theorem
status: proved
scope:
  characteristic: "0"
  curve: "fixed marked rational quartic"
  hypotheses:
    - "The specific projection center, scroll and ordered endpoints"
statement: "The prescribed cone and projected cubic have the finite normalizations, smooth resolutions, conductors and endpoint corrections recorded below."
dependencies: []
evidence:
  - "research/notes/2026-10-24-p4-ruled-surfaces-synthesis.md"
  - "research/computations/p4_ruled_surfaces_2026_10_24.json"
independent_audits:
  - "research/PROMOTION_ADJUDICATION_CR21-26_2026-10-26.md"
  - "research/notes/2026-10-24-ruled-comparison-independent-audit.md"
accepted_in: "research/PROMOTION_ADJUDICATION_CR21-26_2026-10-26.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Only the specified marked projections"
  - "Saved computations not freshly rerun"
---
# Ruled projection and normalization models

## Statement
For the specified projection center in P4, the blowup is P_H(O plus O(-1)) under the lines convention, and the inverse image of C is F4. Two sections of E+4f intersect in twice each marked endpoint. The cone has finite normalization P(1,1,4) and smooth resolution F4, which are not the same. The projected cubic has finite normalization F1 and doubled conductor line branched at the endpoints. The same-center scroll projection has a nonnormal cubic whose intersection with the cone has reduced support C and two embedded length-one endpoint corrections. Ordered-endpoint elementary transformations from Q to F4 change the self-intersection of C through 6,5,4,3,4; the first three centers lie on C and the fourth does not.

## Hypotheses and quantifiers
The specific center, scroll and ordered endpoint marking in the cited audits.

## Proof outline
Projective bundle formulas, finite normalization and conductor calculations, local intersection rings, and tracked elementary transforms establish the statements.

## Dependencies
No other canonical theorem is required; marked setup agrees with R-0026.

## Evidence and verification
Documentary independent audits and saved exact symbolic evidence. No fresh script execution.

## Consequences
Separates projection, finite normalization, smooth resolution and birational elementary transformation.

## Limitations
No universal projected-scroll classification or STCI exclusion.

## Permanent evidence navigation

The `research/notes/` metadata retains original provenance identifiers, not current-tree paths. For mathematical exposition and the linked detailed source supplements, consult [the consolidated subject chapter](../synthesis/04-carriers.md). Historical identifiers remain unchanged; the theorem's hypotheses and status are not expanded.
