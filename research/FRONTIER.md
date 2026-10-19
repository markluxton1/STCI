# Current research frontier

This file records the active mathematical frontier. Established claims belong in \`STATE.md\`; detailed historical handoffs and dated reports are provenance, not competing descriptions of current status.

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
