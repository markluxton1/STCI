# Current research frontier

## Current focus — intrinsic geometry interlude (2026-10-24)

**STCI-directed research is voluntarily paused.** The current objective is to explore the intrinsic projective geometry of the fixed rational quartic **for its own mathematical interest**, not to seek an STCI obstruction. Any eventual STCI insight is incidental, not a criterion for success. The unrestricted characteristic-zero STCI problem and all open frontier items below remain open; their former priority labels are historical STCI-work priorities, **not active assignments** during this interlude. See [the geometry agenda](INTRINSIC_GEOMETRY_INTERLUDE_2026-10-24.md). Preserve accepted result scopes and do not promote exploratory geometry without audit.


This file records the mathematical frontier retained for future STCI work. The Priority 1/2 labels below are historical STCI priorities, not active assignments during the intrinsic-geometry interlude. Established claims belong in \`STATE.md\`; detailed historical handoffs and dated reports are provenance, not competing descriptions of current status.

The [Delta marked-embedding continuation](notes/2026-10-24-delta-embedding-geometry-report.md) is preserved as provisional evidence from the earlier STCI-directed phase. Its follow-up questions are **not active priorities** during the intrinsic-geometry interlude.

The [special lines/planes](notes/2026-10-24-special-lines-planes-research-note.md) and [automorphisms/bitangents](notes/2026-10-24-quartic-automorphisms-bitangents-synthesis.md) explorations support the active intrinsic-geometry agenda. These are provisional geometric research records, not new STCI assignments or promoted theorem authority.

## General intersection viewpoint (research framing, not a theorem)

For the fixed curve \(C_0\), it is often useful to begin with two surfaces having no common surface component and
\[
C_0\subset V(F,G)_{\mathrm{red}},
\]
without assuming equality. If \(m\) is the generic intersection multiplicity along \(C_0\), the effective fundamental cycle has the form
\[
[V(F,G)]=m[C_0]+R,\qquad de=4m+\deg R,
\]
where \(R\) has no component equal to \(C_0\). The STCI case is precisely \(R=0\). This cycle-level formulation does not identify special-fiber exceptional curves with residual components downstairs: vertical exceptional geometry may instead encode excess contact or degeneration along \(C_0\).

Useful levels of analysis include the generic filtered transverse complete-intersection algebra, its global normal-jet realization, the full associated graded ideal and Rees/successive-blowup geometry, residual intersection cycles, and (when helpful) carrier normalization and conductor descent. These are complementary viewpoints, **not** a required sequence or a ranking of methods. Agents may choose or combine methods based on mathematical leverage, including approaches not listed here. Do not treat the volume of prior results in any lane as evidence that it is intrinsically preferred. In particular, no Hilbert-function strategy, normalization-first approach, or residual-degree bound is mandated.

## Ideal-filtration comparison defect — OPEN supported-local question

[October 24 reconciliation](RECONCILIATION_2026-10-24-IDEAL-FILTRATIONS.md) records a provisional comparison-defect and filtered-Koszul framework. The evidence indicates that the defect vanishes wherever one carrier is smooth along C, but does **not** establish the existence of simultaneous singularities. Priority test: with radical(J)=I_C and generically zero defect, can a punctual defect occur? Separate residual-support examples from genuine supported intersections. Do not treat these provisional notes as a promoted obstruction or reopen the closed degree-(4,*) carrier cases.

## Priority 1 — jet-condition and discrepancy framework

**Question.** For primitive or quasiprimitive thickenings
\[
C=C_1\subset C_2\subset\cdots\subset C_m,
\]
when do the successive ambient containment conditions on \(H^0(I_{C_j}(a))\) fail to be independent, and can those dependencies be characterized geometrically?

The earlier quartic order-one \(e=0,1\) calculations remain a laboratory for jet dependencies, **not** surviving quartic STCI-mate cases.

**Leverage.** Uniform order-one bounds, the e=2 primitive-fourth classification, quartic factorization, the ruling/comparison divisor, exact first-symbol ranks, finite local-cohomology reduction, and MF6 constraints.

**First attack.** Express the first few restriction maps intrinsically on the unique quadric containing the rational quartic. Compare expected and actual ranks using the divisor measuring the difference between the primitive conormal direction and the quadric conormal direction.

**Intermediate target.** Prove that rank failure through the first few jets is equivalent to a finite list of special divisor/incidence configurations on the quadric.

## Priority 2 — structural invariants for the entirely-thick branch

**Question.** For exact generic normal orders \(p,q\ge2\), what data beyond the first tangent forms controls the exceptional intersection cycle of the proper transforms of the two defining surfaces?

The local examples show that first-symbol data alone can hide arbitrarily large excess contact.

**First attack.** Study successive transforms/Rees valuations along \(C\), initially on the equality and near-equality region of
\[
7(a/p)(b/q)/4+7\ge4(a/p+b/q).
\]

**Intermediate target.** Find a finite valuation-theoretic invariant forcing an extra common curve or forbidden normalization/conductor support in a nontrivial infinite region of normalized degree space.

## Closed quartic-mate frontier — retained for navigation

The former Priority 3 normal-quartic mate question is **closed** by [STCI-R-0001](results/quartic_carrier_exclusion.md), the accepted all-integral-quartic theorem for fixed C0 in characteristic zero. Do not reopen its B1/B2/B3/D cases as possible quartic STCI carriers. The old classification and proofs remain historically useful. This does **not** close separate quartic ancestor-incidence problems or higher-degree carriers.

## Cartier singleton normalization models — OPEN PROJECTION/DESCENT QUESTION

[STCI-R-0002](results/cartier_singleton_lift.md) leaves three higher-degree normalization models for fixed C0 under its **Cartier singleton degree-one inverse-lift** hypotheses. [STCI-Q-0001](questions/cartier_projection_models.md) asks which, if any, admit actual projections with full inverse support and conductor descent. Do not infer that these are the only possible higher-degree carriers; non-Cartier and multiple inverse lifts lie outside the theorem.

## Full-conductor lattice computations — OPEN INSTANCES

The accepted [STCI-R-0003](results/fixed_carrier_conductor_criterion.md) reduces mate existence on a **specified integral carrier** to its normalization class-group relation lattice and full conductor-unit descent. The theorem is proved; computing these objects for the surviving higher-degree carrier families remains open. Residual torsion without characteristic-zero nilpotent-defect control is insufficient, and a fixed-carrier reduction does not bound all carriers.

## Phase images of the three Cartier projection families — OPEN COMPUTATION

[STCI-R-0004](results/projection_phase_reduction.md) gives a reviewed finite-type torsion-coset reduction. The next substantive step is to **compute the actual admissible phase images and surviving torsion cosets** for the three models in [STCI-Q-0001](questions/cartier_projection_models.md), retaining nilpotent conductor equations. Do not mistake the existence of a finite reduction for the completion of these computations.

## Smooth-root bridge boundary — OPEN BEYOND RESTRICTIVE HYPOTHESES

[STCI-R-0005](results/smooth_root_formal_obstruction.md) excludes infinite formal lifts of smooth movement-two roots. [STCI-R-0006](results/actual_ci_smooth_root_bridge.md) supplies a conditional actual-CI bridge, requiring a saturated first relation, everywhere joint generation, full coprime initial ideal, gap at least two, and a smooth full root. The finite-gap conclusion does **not** cover singular or nonreduced roots, defective first relations, or arbitrary actual STCI presentations. An explicit finite obstruction stage remains uncomputed.

## Quadratic-root second zero locus — OPEN COMPUTATION

The accepted [STCI-R-0007](results/quadratic_root_obstruction_model.md) provides a global sixteen-first-equation and twenty-five-second-pairing model, with the homogeneous smoothness discriminant. Compute the **actual second zero scheme and its intersection with the spectral torsion condition**; no completed elimination or global emptiness proof exists. The seed and its four-dimensional component are generically second-order obstructed, but other components may survive. Actual-CI implications remain subject to [STCI-R-0006](results/actual_ci_smooth_root_bridge.md) and s>4.

## Distinct root configurations — GEOMETRIC FRONTIER

The [spectral Picard criterion STCI-R-0008](results/spectral_root_picard_criterion.md) covers abstract graded second relations on full root schemes, including singular and nonreduced roots. The [smooth-root formal obstruction STCI-R-0005](results/smooth_root_formal_obstruction.md) addresses smooth roots and infinite Cartier lifting; [STCI-R-0007](results/quadratic_root_obstruction_model.md) gives actual ambient finite-stage equations in the quadratic movement-two family; [STCI-R-0006](results/actual_ci_smooth_root_bridge.md) transfers them to actual CIs only under restrictive hypotheses. The genuinely unclosed cases include singular/nonreduced full roots, defective or nonsaturated first relation sheaves, missing joint generation, and other initial-ideal patterns. These are **distinct geometric gaps**, not alternate descriptions of one numerical constraint.

## Moving pure powers with special-point degeneration — OPEN

[STCI-R-0009](results/moving_purepower_boundary.md) rules out uniform fiberwise coprimality for moving pure-power first relations of order at least two, but forces an **actual degeneration divisor**, not an unrestricted STCI contradiction. Study its geometry and its compatibility with the full actual initial ideal, including noncoprime next relations and saturation defects. Finite-order principal-relation lifts exist in some ranges and are not STCI constructions.

## Other active lanes

- **Order-one e=0/e=1:** retain the jet/ancestor structural questions, but not as possible quartic STCI-mate cases after STCI-R-0001.
- **Local cohomology:** finite bilinear quartic incidence remains open; use it as a certificate/translation of the jet problem rather than launching unstructured higher-stage scans.
- **MF6:** retain structural and ancestor questions; all actual integral-quartic mate possibilities are closed by STCI-R-0001.
- **Split carriers:** explicit [4]/[2,2] survivors remain; avoid treating first-normal survivors as actual STCI constructions.
- **Normalization/conductor:** use as a carrier-exclusion tool when normalization geometry produces isolated inverse-image points or prevents the required Cartier divisor.

## Current recommendation

Evaluate the available approaches against the broader intersection problem, with attention to structural arguments that work across degrees and normal orders. The jet-condition, entirely-thick, root-scheme, residual-intersection, and carrier approaches remain available; these listed priorities are **options, not instructions to follow in order**. Select or combine approaches according to mathematical leverage and exact hypotheses. Do not reopen quartic STCI-mate cases closed by STCI-R-0001.


## Reviewed October 19 normal-cone results

Promoted [STCI-R-0010](results/saturated_first_relation_normal_flatness.md) proves ordinary normal-flatness for actual lci thickenings with full generic coprime binary CI initial algebra (2 <= r < s) and saturated actual first relation. Promoted [STCI-R-0011](results/moving_nonreduced_spectral_root_obstruction.md) excludes moving nonreduced full spectral roots satisfying Picard descent on the rational base. Together they exclude such roots for actual C0 thickenings **only within** the STCI-R-0010 hypotheses.

Open: nonsaturated first relations, generic initial ideals with additional generators, reduced singular moving roots and equal-slope component gluing, special-fiber defects, and ambient lifting. The unrestricted characteristic-zero STCI question remains open. The exceptional-cycle estimates and degree-eight carrier examples from the same research branch remain unpromoted proposals.

## October 20 source intake — reconciled October 21

The [October 20 normal-filtration report](notes/2026-10-20-normal-filtration-research-report.md) was originally provisional. Its independently reviewed, scope-limited results are now promoted as [STCI-R-0013–0018](results/INDEX.md). The six movement-two tuples in R0014 are necessary only in the specified saturated/full generic binary-CI class, not an exhaustive list of STCI presentations. The nonsaturated resultant formula (R0016), singleton plane-family exclusion (R0017), and regular-formal-surface root obstruction (R0018) retain their distinct hypotheses. Historical proposal labels in source notes record their status *at the time*, not their current authority.

Unpromoted material from this intake includes exceptional-cycle estimates, degree-eight carrier examples, and examples about limitations of generic Rees data; these are not additional canonical theorems. The [Space Curves I–VI archive](archive/space-curves-2026-10-19/README.md) contains the fixed-degree finite normal-jet criterion VI-011 with donor evidence but without a fresh repository audit or promotion. It concerns a supplied global pair and fixed degree budget, not a uniform bound; do not substitute arbitrary k(C) coefficients for global constant coefficients.

## Reconciled October 21 frontier — actual generators and residual geometry

The October 20 source intake above is reconciled: its supported claims are [STCI-R-0013–0018](results/INDEX.md). The residual-cycle proof is [STCI-R-0019](results/quasiprimitive_residual_cycles.md), and the prescribed arithmetic lifting result is [STCI-R-0012](results/prescribed_z4_arithmetic_nonlifting.md). Original note statuses are historical.

**Open actual-STCI cases, both defining degrees at least five:** nonsaturated first-relation loci and their intrinsic defect divisors, full generic initial ideals with more than two generators, reduced singular roots and component gluing with possibly singular formal surfaces, unspecified movement (including epsilon>=9), and positive residual-cycle constraints that can be realized by **actual global homogeneous** generators. The six movement-two rows are a conditional arithmetic list, not a complete frontier for arbitrary presentations. The existing all-integral-quartic exclusion [STCI-R-0001](results/quartic_carrier_exclusion.md) is unchanged.

**Leading next investigation (not a theorem; alternative lanes remain open):** For an actual hypothetical pair `F_a,G_b` with `a,b>=5`, and full generic coprime initial CI of orders `r<s`, compare the defect divisor `D` and resultant vanishing `Delta` from [STCI-R-0016](results/nonsaturated_first_relation_resultant.md) with the pointwise torsion/residual-cycle determinant mechanism of [STCI-R-0019](results/quasiprimitive_residual_cycles.md). First identify a filtration-level specialization map from saturated quotient-generation defects `c_j` to a *geometrically defined* residual cycle on an auxiliary containing surface or successive transform. Prove (rather than assume) finite flatness, the existence of a curvilinear saturated flag, and properness of the residual intersection; where these fail, formulate correction terms. Seek a global inequality by intersecting its effective cycle with sections induced by the **actual** two homogeneous forms, retaining special-point saturation defects. No comparison between `Delta` and `D_(m-1)` is currently known in the general entirely-thick class, and exceptional vertical components need not descend to residual curves.

The claim that the two defining surfaces must share a singular point on C0 remains **OPEN/UNPROVED**: no such general audited proof is recorded. The arithmetic [STCI-R-0012](results/prescribed_z4_arithmetic_nonlifting.md) neither closes this question nor the unrestricted characteristic-zero STCI problem.

## October 21 new evidence: focused next actions (not promoted)

- **Arithmetic mechanism:** audit the [intrinsic divided-power report](notes/2026-10-21-z4-intrinsic-divided-power-mechanism.md) against the [independent structural review](notes/2026-10-21-z4-general-mechanism-independent-audit.md). Separate universal divided-power identities, marked quadratic-neighborhood gluing, and nonvanishing of the actual embedded obstruction. Test any generalization under explicit hypotheses; do not infer an arbitrary characteristic-zero STCI obstruction from R0012.
- **Actual first-normal defects:** the [characteristic-zero consequences](notes/2026-10-21-z4-characteristic-zero-stci-consequences.md) give a reviewed bounded-pole necessary condition for generically curvilinear supported CI with generic length at least three. Compare its *actual* defect divisor with R0016's resultant and R0019's filtration-cycle divisor only after constructing a specialization/comparison map; these divisors are not currently identified.
- **Conditional degree-(6,16) lane:** [independent conductor/chart review](notes/2026-10-21-conditional-2-12-conductor-and-chart-independent-review.md) checks a cubic contraction and several scoped chart exclusions for the full generic (2,12), saturated movement-two case. Remaining endpoint/orbit-collision/repeated-base-zero/node cases must not be declared empty. The newest `computations/conditional_2_12_certificate_audit_cont2_2026_10_21.json` reports a failed M2 assertion (line 23, return code 1): inspect the failing equality and inputs, rerun, and distinguish a verifier defect from a mathematical counterexample. Do not promote this certificate as a pass.
