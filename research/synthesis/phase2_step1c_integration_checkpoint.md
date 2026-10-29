# Phase 2 Step 1C integration checkpoint

This checkpoint is a mathematical preservation status report, not an exhaustive source-coverage certificate and not an independent correctness review.

## Permanent destination changes

- `827b073`: carrier/conductor chapter preserves nonimmersion-prime obstruction, four explicit nonnormal MF6 carriers and ordinary-versus-nodal conductor distinctions.
- `1e2b8f2`: formal normal synthesis preserves entirely-thick Noether budget, horizontal blowup recursion, power-saturation theorem and thickened-fiber countermodel.
- `46e66bc`: normal-filtration synthesis preserves ancestor conormal splitting, corrected simultaneous-target bridge, six defective endpoint exclusions and principal-rank limitation.
- `2b4aaac`: dedicated Veronese synthesis preserves symmetric-pencil classification, singular-pencil quadric outcome and three all-degree mate obstructions.
- `b8af1a1`: quartic-carrier technical chapter points to the Veronese integration.
- `19d3a57`: provisional Mumford numerical-bound review records exact defect formula and audit obligations.
- `2436f49`: carrier/conductor chapter points to the provisional Mumford review.

## Ownership and remaining obligations

The quartic-carrier technical chapter is the permanent navigation owner for the Veronese proof, while the dedicated synthesis carries the preserved claim-level explanation and the historical note remains the detailed proof owner until a full technical transcription and audit. The carrier/conductor chapter owns the nonimmersion and MF6 conductor summary. The formal-normal synthesis owns the entirely-thick recursion and saturation. The normal-filtration synthesis owns ancestor conormal and MF6 rank restrictions. The Mumford bound is provisionally assigned to carrier numerical geometry and is **not promoted**.

Remaining: independently check the length-three Veronese conductor-jet argument and the Mumford normal-bound proof; compare all other source records against their actual destinations; integrate any still-unique proofs rather than retaining only cross-references; update the unified source-to-claim disposition matrix with final commit references; complete outstanding historical source intake. No claim of full source enumeration, full mathematical accounting, or completion of Step 1C is justified at this checkpoint.

## Subsequent October 8–11 destination reconciliation

- `6641ac9`, `2690fde`: first and second rational endpoint families' target-u incidence exclusions, including the later cubic, quartic and degree-fifteen exceptional-field closures, are preserved in `phase2_step1c_endpoint_families.md`. The 22-point October 8 second-family count is historical, not current.
- `ee87336`, `342aad3`: endpoint source-to-claim dispositions are recorded in `phase2_step1c_endpoint_family_disposition.md`.
- `9417d27`, `56d7a71`, `adba7b8`, `26d2af3`: principal defect-one MF6 complete quartic spaces, boundary fiber, (8,1/2) scroll-conductor all-mate exclusion, independently checked weighted finite candidate reduction, and subsequent R-0001 all-integral-quartic closure are preserved in `phase2_step1c_mf6_principal_boundary.md`.

**Scope warning:** the accepted R-0001 carrier theorem closes the STCI mate question for every integral quartic, but does not automatically close the independent common-quartic-ancestor local-cohomology incidence. The candidate bound of 630 points is historical as an STCI frontier, not a current open carrier problem. These additions are source-preservation comparisons, not fresh independent correctness audits. Exhaustive source coverage and destination completeness remain uncertified.

## Quartic technical proof-level preservation pass

Commits `461c106` and `8c65532` integrated additional mathematical mechanisms directly into `research/chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md`: genus-zero minimal-degree classification and cone nonimmersion, genus-one complete ribbon-net interface and root partitions, genus-two bisection global O(-8) ribbon contradiction and conditional conductor-power algebra, nonrational-normalization exclusion without a mate, and genus-two entire conductor plus normal ADE ambient conic model. The October 10 nonendpoint and endpoint trisecant audits were also checked against the chapter: their universal chain inequality, full endpoint quartic family, coefficient-zero and doubled-horizontal cases, and nonreduced divisor handling are already represented in Sections 3–5. Retain original detailed proofs for verification; do not duplicate them merely to inflate coverage. The genus-two ambient-model conclusion applies to the strict transform T, not automatically to normalization S. This is a **bounded proof-level destination comparison**, not a certification of all historical files.

## October 7 P-044 / P-045 saturation destination

Commit `a520106` integrates the complete five-coordinate `dx=1` saturation result into `normal_filtration_boundary_obstructions.md`. The exact saturated ideal has radical `(2a+1,b+2)` but nonreduced rank-four quotient over `Q[x]`. The historical three-coordinate shortcut is mathematically false (its open subsystem has additional solutions), and must not be used as a proof of emptiness. The source's universal comparison identifies `(a0,a1,a2,b0,b1,b2)=(x,a,1,1,b,d)` and reverses the five numerator indices with scalar `1/32`; it proves agreement with the universal linear locus, not exhaustion of all normalized parameters by `dx=1`. The P-045 cubic-factor exclusion then closes quartic carriers **on this slice only**. Detailed exact multipliers and executable certificates remain with the source. Source owner: `research/notes/2026-10-07-dx1-saturation-audit.md`; permanent thematic owner: normal-filtration synthesis. Independent correctness review was not repeated in Step 1C.

## Entirely-thick October 7 ruling/jet comparison

Commit `bbf4f10` reconciles the Segre three-point trisecant incidence, distinct-root bound, and the false pure-power/marked-multiplicity coupling. Commit `ba381de` preserves exact reduced-fiber interpolation codimension `rq`, thickened-fiber jet surjectivity threshold `2p<=3q+1`, high-p cokernel `(2p-3q-1)(q+1)`, and the transverse smoothing countermodel for repeated ruling fibers. Permanent owner: `formal-normal-intersection.md`; detailed sources: `2026-10-07-thick-segre-root-audit.md`, `2026-10-07-thick-marked-point-jets.md`, `2026-10-07-thick-ruling-interpolation-audit.md`, `2026-10-07-thickened-fiber-jets.md`, and `2026-10-07-thick-repeated-fiber-smoothability.md`. These five source-level contributions are compared and preserved, but no jet-incidence-to-STCI theorem has been established. Do not count a numerical interpolation cokernel as a residual curve or global mate exclusion.

## Further October 7 cross-family dispositions

Commit `161f534` preserves the exceptional quadric section `S_Q=(1,1)`, horizontal class `(0,1)`, marked intersection degree `2pq`, and the **unresolved** coordinate bridge from trisecant ruling roots (degree-three pullback on C) to individual horizontal exceptional sections. It also preserves the absence of a semicontinuity inequality between marked root multiplicity and generic section coefficient, and the local pair countermodel. Source owners: `2026-10-07-thick-quadric-section-divisor.md`, `2026-10-07-thick-first-blowup-marked-coupling.md`, `2026-10-07-thick-root-budget-separation.md`, `2026-10-07-thick-local-pair-marked-trisecant.md`; permanent owner: `formal-normal-intersection.md`. The historical root-count bound requires a justified correspondence, not just the Segre degree count.

Commit `e2a134c` preserves the six defective `e=1,d2=1` endpoint **all-degree fixed-carrier mate exclusions**, including the singular-line branch-value norm argument and the narrower MF6 third-layer defect contradiction. Source: `2026-10-07-session-mf6-e1-d1-endpoints.md`; permanent owner: `normal_filtration_boundary_obstructions.md`. The ancestor-only result is strictly weaker and remains a separate conditional claim. The principal d2=1 and d2=2 lanes are outside this specific proof; global R-0001 has a separate scope.
