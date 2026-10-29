# Phase 2 Step 1C — destination comparison, batch 1 (provisional)

Scope: direct comparison against research/chapters/CARRIER_AND_CONDUCTOR_GEOMETRY.md, research/synthesis/normalization_conductor_projection.md, and the original sources below. Other permanent owners must still be searched; absence here is not global absence. This is preservation analysis, not independent correctness certification.

| Source | Claim | Checked destinations | Status | Action / owner |
|---|---|---|---|---|
| research/notes/2026-10-07-session-veronese-pencil-classification.md | All-degree exclusion for finite birational quartic projections of (P2,O(2)), including regular Jordan sizes 2 and 3; full inverse support and conductor-jet descent | CARRIER_AND_CONDUCTOR_GEOMETRY.md §3.1; normalization_conductor_projection.md | Partial in inspected destinations: classification mentions Veronese but detailed pencil/conductor/all-degree proof remains in historical note | Primary owner carrier/conductor geometry, genus-zero Veronese subsection. Compare other permanent chapters before integrating. |
| research/notes/2026-10-07-session-veronese-singular-pencil.md | Rank-two symmetric pencil with identically zero determinant has linear kernel; projected image quadric, generic degree two, including char 2 caveat | Same | Partial in inspected destinations: singular-pencil argument not located | Owner carrier/conductor geometry, Veronese subsection; keep characteristic scope distinct |
| research/notes/2026-10-05-mumford-normal-bound.md | For S generically regular along smooth C, (C^#)^2 <= deg N_C/S, with exact defect (Z-R).C, A1 contribution 1/2, conditional split-sextic delta>=8 | Same | Not found in inspected destinations; global status pending | Primary owner carrier/conductor numerical geometry; cross-reference split-sextic and low-degree chapter. Independent audit remains required before promotion. |

## Explicit boundaries
- These three comparisons are **not** an exhaustive search of all permanent destinations.
- The Veronese note asserts a proof, but an earlier PASS is not a new correctness verification.
- The Mumford note explicitly requests an independent proof audit; do not silently promote it.
- A quartic fixed-carrier exclusion must not be represented as general STCI exclusion.
- The source-intake process remains incomplete; this is not a coverage certificate.

## Next actions
1. Search every permanent chapter for the three claims and reclassify globally.
2. Read the Veronese conductor-jet endpoint argument and compare at proof level.
3. Read the nonimmersion-prime and nonnormal MF6 source notes; compare against their actual owners.
4. Integrate only verified omissions and record commit SHA per change.

## Subsequent integration status

Veronese classification and singular-pencil reduction are now recorded in `phase2_step1c_veronese_integration.md` (2b4aaac), linked from the technical carrier chapter (b8af1a1), with the explicit length-three conductor-jet argument added in d275c95. These claims are integrated for preservation, not independently re-certified. The Mumford numerical bound is preserved provisionally in `phase2_step1c_mumford_numerical_bound_review.md` (19d3a57; expanded db7f90a) and linked from the carrier chapter (2436f49). Its correctness audit remains open.
