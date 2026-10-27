# Mathematical map of the STCI project

This is a **conceptual navigation map**, not a new proof, a chronological record, or a machine-verified theorem-dependency graph. Follow each [canonical result record](results/INDEX.md) for exact hypotheses, characteristic, evidence, and formal dependencies. Grouping records here means they address related questions, **not** that one theorem logically implies another. See [AUTHORITY.md](AUTHORITY.md).

## The central question and boundary

For the fixed rational quartic \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), is \(C_0\) a set-theoretic complete intersection of two surfaces in characteristic zero? **Open.** For a proper intersection \(Y=V(F_a,G_b)\) containing \(C_0\), the cycle can be studied as \([Y]=m[C_0]+R\), with \(ab=4m+\deg R\). The STCI case requires \(R=0\), but studying intersections with residual components can illuminate obstructions. Do not infer a residual curve downstairs from exceptional vertical cycles.

**Closed low-degree boundary:** [R-0001](results/quartic_carrier_exclusion.md) excludes every integral quartic carrier with a mate; together with its accepted lower-degree/factor reduction, both defining degrees in any hypothetical characteristic-zero STCI are at least five. [R-0022](results/quartic_44_filtered_exclusion.md) gives a separate, narrower proof for a quartic pair. Neither resolves higher-degree pairs.

For a compact list of specific unresolved implications, see the [open-question locator](questions/README.md). It is navigation, not an additional authority layer.

## Approaches and their missing bridges

| Approach | What the records provide | Main unresolved bridge |
|---|---|---|
| Carrier normalization, conductors, projection | Fixed-carrier tests, conditional singleton models, projection-phase reduction, pointwise conductor formula | Compute admissible actual higher-degree families, full inverse support and conductor descent; address non-Cartier/multiple branches |
| Normal filtrations, roots, initial ideals | Normal-flatness, moving-root and actual-generator obstructions, resultant and socle budgets, local comparison | Pass from conditional generic/graded structure to arbitrary **actual global** supported pairs; handle nonsaturation, punctual defects and extra generators |
| Blowups and residual intersection | Conditional effective residual-cycle and first-normal restrictions; explicit examples | Relate local defects to genuine residual support and global intersection inequalities without assuming properness or finite flatness |
| Jets and equation modules | Fixed-jet rigidity and explicit boundary examples; provisional boundary-repair tests | Prove global homogeneous realizability or exclusion for a surviving degree-\(\ge5\) family |
| Characteristic and intrinsic geometry | Conormal splitting jump, prescribed arithmetic nonlifting, dual/ruled/flag models | Determine which characteristic-specific mechanisms transfer to characteristic zero and constrain STCI |
| Deformations and degenerations | Explicit degeneration/smoothing and residual configurations | Turn examples and parameter-space observations into general constraints on supported intersections |

These are **research interfaces**, not an ordered program. [FRONTIER.md](FRONTIER.md) tracks present activity; [RESEARCH_DECISION_GUIDE.md](RESEARCH_DECISION_GUIDE.md) gives selection criteria.

## Complete canonical result locator (R-0001–R-0036)

Each ID below links to the authoritative record. Descriptions are deliberately short; **scoped/conditional** does not mean unrestricted exclusion.

### A. Carrier geometry, normalization, conductor and projection

- [R-0001](results/quartic_carrier_exclusion.md) — all integral quartic carriers excluded for fixed \(C_0\), characteristic zero.
- [R-0002](results/cartier_singleton_lift.md) — necessary Cartier singleton-lift models, conditional.
- [R-0003](results/fixed_carrier_conductor_criterion.md) — fixed-carrier full-conductor criterion.
- [R-0004](results/projection_phase_reduction.md) — restricted projection-family phase reduction; images not generally computed.
- [R-0017](results/singleton_plane_conductor_descent.md) — exclusion of one degree-sixteen plane subfamily.
- [R-0034](results/normal_carrier_index_socle.md) — local Cartier-index/socle compatibility, conditional.
- [R-0035](results/normal_carrier_bounded_index_exclusion.md) — normal integral carriers excluded under bounded local index (at most four) and inherited hypotheses; higher indices and nonnormal carriers not covered.
- [R-0036](results/pointwise_conductor_socle_defect.md) — pointwise contact/top-socle divisor identity for smooth singleton Cartier normalization with invertible conductor.

### B. Normal roots, first relations, filtrations and thickening obstructions

- [R-0005](results/smooth_root_formal_obstruction.md) — smooth movement-two formal-root exclusion in balanced setup.
- [R-0006](results/actual_ci_smooth_root_bridge.md) — actual-CI bridge under restrictive hypotheses.
- [R-0007](results/quadratic_root_obstruction_model.md) — universal quadratic-root obstruction model with conditional CI interface.
- [R-0008](results/spectral_root_picard_criterion.md) — Picard criterion for graded second relations.
- [R-0009](results/moving_purepower_boundary.md) — moving pure-power and second-relation degeneration.
- [R-0010](results/saturated_first_relation_normal_flatness.md) — normal-flatness under saturated actual first relation and full generic CI conditions.
- [R-0011](results/moving_nonreduced_spectral_root_obstruction.md) — moving nonreduced root obstruction, scoped to rational base.
- [R-0013](results/saturated_actual_generator_movement.md) — actual-generator rigidity and movement-one exclusion, conditional.
- [R-0014](results/movement_two_six_rows.md) — six necessary movement-two rows, not all STCI cases.
- [R-0015](results/fixed_small_movement_finiteness.md) — fixed movement 1–8 arithmetic finiteness reduction.
- [R-0016](results/nonsaturated_first_relation_resultant.md) — nonsaturated resultant/defect budget, conditional.
- [R-0018](results/regular_singular_root_formal_obstruction.md) — reduced singular movement-two root obstruction with regular lifted formal surface.
- [R-0030](results/local_filtration_comparison_defect.md) — local exact comparison, generic generator excess, and punctual-defect support criterion; existence under sole support remains open.
- [R-0032](results/full_conormal_socle_budget.md) — full conormal filtration/socle identity, conditional actual supported CI.
- [R-0033](results/constant_first_relation_lifting.md) — quadratic lifting obstruction for constant first relation; does not cover moving or positive-defect models.

### C. Residual geometry, jets and explicit intersections

- [R-0019](results/quasiprimitive_residual_cycles.md) — saturated quasiprimitive residual cycles and first-normal bound, conditional.
- [R-0023](results/ci_quartic_explicit_residual_geometry.md) — explicit residual geometry for fixed quartic examples.
- [R-0024](results/ci_quartic_fixed_boundary_smoothing.md) — independent residual-node smoothing for an explicit pencil.
- [R-0025](results/ci_fixed_sextic_jet_rigidity.md) — fixed sextic jet rigidity, certificate-qualified.

### D. Characteristic, conormal, dual and ruled geometry

- [R-0012](results/prescribed_z4_arithmetic_nonlifting.md) — prescribed characteristic-two Z4 arithmetic nonlifting; not a universal characteristic-zero obstruction.
- [R-0020](results/quartic_conormal_characteristic_jump.md) — characteristic-dependent conormal splitting.
- [R-0021](results/quartic_mu4_degeneration.md) — explicit \(\mu_4\) degeneration.
- [R-0022](results/quartic_44_filtered_exclusion.md) — independent scoped (4,4) exclusion in characteristic zero (also referenced above).
- [R-0026](results/quartic_flag_conormal_geometry.md) — marked flag incidence/conormal geometry.
- [R-0027](results/quartic_dual_singular_scheme.md) — dual discriminant singular scheme, certificate-qualified.
- [R-0028](results/quartic_ruled_projection_geometry.md) — marked ruled projection and normalization models.
- [R-0029](results/quartic_arithmetic_ruled_models.md) — prescribed arithmetic ruled four-section family.
 
**Coverage:** R-0001–R-0036 appear above exactly once except R-0022, which is cross-referenced in the low-degree boundary and listed in D. All statements remain subject to their record-level qualifications.

## Open interfaces: where a new result would matter

1. **Punctual comparison defect under sole support.** [R-0030](results/local_filtration_comparison_defect.md) restricts support of defect but does not decide existence/nonexistence with \(\sqrt{(F,G)}=I_{C_0}\) and generically vanishing comparison defect. A residual-support example does not settle this.
2. **Actual higher-degree carrier families.** [Q-0001](questions/cartier_projection_models.md), [R-0002](results/cartier_singleton_lift.md), [R-0004](results/projection_phase_reduction.md), [R-0017](results/singleton_plane_conductor_descent.md): determine an actual admissible projection phase locus and full conductor descent for a surviving family.
3. **Global equation realization.** Connect [R-0016](results/nonsaturated_first_relation_resultant.md), [R-0019](results/quasiprimitive_residual_cycles.md), [R-0030](results/local_filtration_comparison_defect.md), and [R-0032](results/full_conormal_socle_budget.md) to actual homogeneous pairs. The [one-step boundary obstruction note](notes/2026-10-27-one-step-boundary-obstruction.md) is **provisional**, not an accepted general realization theorem.
4. **Surviving normal-carrier regimes.** [R-0034](results/normal_carrier_index_socle.md)–[R-0036](results/pointwise_conductor_socle_defect.md) leave higher local indices, nonnormal/multiple-branch settings and various non-Cartier cases outside their scopes.
5. **General initial ideals and residual support.** [R-0010](results/saturated_first_relation_normal_flatness.md)–[R-0019](results/quasiprimitive_residual_cycles.md) leave nonsaturated, extra-generator and certain singular-root cases; a vertical exceptional cycle is not automatically a residual curve.

This list is selective and not a new canonical question inventory. See [open-problem topics](open/README.md) and [FRONTIER.md](FRONTIER.md).

## Reading and maintenance

- For an assertion: **map → result record → exact evidence/audit**. A blank YAML `dependencies` field does not prove that a theorem has no inherited proof inputs; inspect the record's evidence.
- For a question: **map → question or frontier → relevant result limitations**.
- For a new result: update the canonical record and this map only after review; never infer authority from a topical grouping.
- Prefer consolidating useful mathematical content over preserving chronological narratives. Keep verification evidence, counterexamples and meaningful failed approaches; Git retains edit history. Do not delete supporting material merely because it is dated.
