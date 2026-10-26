# Provisional inventory — intake register

**Status:** initial topic-level intake, **not yet exhaustive at claim level**. No item here is canonical theorem authority.

| Topic | Evidence location | Current status | Next adjudication |
|---|---|---|---|
| CI-cycle valuations, local clusters and cancellations | October 25–26 notes on `codex/ci-cycle-valuations-2026-10-25` | Provisional, scoped local claims | PQ-04 |
| Fixed-sextic jet kernel and residual bound | October 26 continuation/checkpoint notes on valuation branch | Computationally supported, fixed-carrier only | PQ-01 |
| Fixed-boundary deformations and node smoothing | October 25 fixed-boundary notes | Audited calculations; globalization scope to separate | PQ-02 |
| Smooth residual quartic CI example | October 25 smooth-residual audit | Explicit computational example, not general theorem | PQ-03 |
| Quartic flag, cubic Gauss and duality schemes | [flag synthesis](notes/2026-10-24-quartic-flag-duality-synthesis.md) | Provisional intrinsic geometry | PQ-05 |
| P4 quartic and ruled surfaces | [ruled synthesis](notes/2026-10-24-p4-ruled-surfaces-synthesis.md) | Provisional geometry | PQ-06 |
| Intrinsic (4,4) K3 proof | [research report](notes/2026-10-23-intrinsic-44-research-report.md) | Independently reviewed note, authority gap | PQ-07 |
| Ideal filtrations and spectral sequences | [reconciliation](RECONCILIATION_2026-10-24-IDEAL-FILTRATIONS.md) | Provisional | PQ-08 |
| Higher initial ideals and valuations | [reconciliation](RECONCILIATION_2026-10-23-VALUATIONS.md) | Provisional, mixed scopes | PQ-08 |
| Delta marked-embedding geometry | [report](notes/2026-10-24-delta-embedding-geometry-report.md) | Provisional, inactive lane | PQ-08 |
| Historical unpromoted claims and open topics | [provenance classification](PROVENANCE_CLASSIFICATION_2026-10-17.md), [open topics](open/README.md), [research record](RESEARCH_RECORD.md) | Requires claim-level sweep | PQ-08 |

Promoted records remain authoritative only within their stated scopes. Unrestricted characteristic-zero STCI remains open. Do not infer exhaustive coverage from this initial register.

## Authority reconciliation and disposition register

The [canonical results index](results/INDEX.md) currently enumerates **22 promoted result IDs (R-0001 through R-0022)** and six legacy topic syntheses. These are **not** unpromoted simply because earlier notes describe them as provisional. The sole indexed canonical question is [STCI-Q-0001](questions/cartier_projection_models.md). Promotion review must compare against these records before proposing any new IDs.

| Existing scope | Authority or evidence | Disposition |
|---|---|---|
| All integral quartic carrier exclusion, fixed C0, char 0 | [R-0001](results/quartic_carrier_exclusion.md) | Promoted; closed, do not reopen |
| Cartier singleton inverse-lift and three normalization models | [R-0002](results/cartier_singleton_lift.md), [Q-0001](questions/cartier_projection_models.md) | Promoted conditional reduction; realizability open |
| Fixed-carrier conductor and phase reductions | [R-0003](results/fixed_carrier_conductor_criterion.md), [R-0004](results/projection_phase_reduction.md) | Promoted conditional reductions; actual phase computations open |
| Smooth movement-two root, actual-CI bridge, quadratic-root model | [R-0005](results/smooth_root_formal_obstruction.md), [R-0006](results/actual_ci_smooth_root_bridge.md), [R-0007](results/quadratic_root_obstruction_model.md) | Promoted scoped claims; second zero scheme / general bridge open |
| Spectral roots and pure-power degeneration | [R-0008](results/spectral_root_picard_criterion.md), [R-0009](results/moving_purepower_boundary.md) | Promoted; degeneration not global contradiction |
| Saturated first relation and moving nonreduced roots | [R-0010](results/saturated_first_relation_normal_flatness.md), [R-0011](results/moving_nonreduced_spectral_root_obstruction.md) | Promoted within hypotheses; nonsaturated and extra-generator cases open |
| Prescribed Z4 nonlifting | [R-0012](results/prescribed_z4_arithmetic_nonlifting.md) | Promoted for specified model/DVRs, not general characteristic-zero theorem |
| Movement, resultants, singleton degree-16, singular roots | [R-0013](results/saturated_actual_generator_movement.md)–[R-0018](results/regular_singular_root_formal_obstruction.md) | Six promoted scope-limited records; inspect individually for dependencies |
| Quasiprimitive residual zero cycles | [R-0019](results/quasiprimitive_residual_cycles.md) | Promoted conditional surface theorem; distinct from elementary Bézout residual 1-cycle |
| Conormal splitting, mu4 degeneration, filtered (4,4) | [R-0020](results/quartic_conormal_characteristic_jump.md)–[R-0022](results/quartic_44_filtered_exclusion.md) | Promoted; assess October 23 K3 note only for independent additional content |
| Higher initial ideals / valuation reconciliation | [October 23 reconciliation](RECONCILIATION_2026-10-23-VALUATIONS.md) | Reviewed intake, no promotions; distinguish generic multiplicity and residual length |
| Comparison defect and filtered Koszul | [October 24 reconciliation](RECONCILIATION_2026-10-24-IDEAL-FILTRATIONS.md) | Reviewed provisional; spectral-sequence conventions, sheafification and punctual defect open |
| Intrinsic geometry interlude and special lines/planes | [interlude](INTRINSIC_GEOMETRY_INTERLUDE_2026-10-24.md), [special lines](notes/2026-10-24-special-lines-planes-research-note.md) | Provisional geometry, not STCI obstruction |
| Automorphisms, bitangents and marked embedding | [synthesis](notes/2026-10-24-quartic-automorphisms-bitangents-synthesis.md), [Delta report](notes/2026-10-24-delta-embedding-geometry-report.md) | Provisional, preserve evidence and correction history |
| Older jet, thick, normalization, conductor and tropical explorations | [frontier](FRONTIER.md), [open topics](open/README.md), [legacy topic index](results/INDEX.md) | Mixed historical and open; no unscoped promotion |

### Conflict and duplication checks

- The October 23 local valuation identity `de=4m_C+deg R` is an elementary proper-CI cycle identity, **not** R-0019's conditional residual zero-cycle theorem.
- The characteristic-zero four-component quartic example and characteristic-two single-support degeneration are already addressed by R-0021; do not treat a new example as an unrestricted quartic theorem.
- The fixed-sextic bound, quartic residual example and node smoothing have different quantifiers; none establishes universal endpoint concentration.
- The comparison defect's support inclusion does **not** imply simultaneous carrier singularities exist.
- The provenance classification dated October 17 is a historical file-count snapshot (then 17 files under results), not an accurate current promoted-result count.

### Remaining coverage gaps

This register covers the canonical result families, named reconciliation packets, active branch research, and indexed frontier lanes. It does **not** certify that every assertion in the hundreds of archived notes, scratch files, scripts and validation logs has been individually examined. Those require a path-level claim extraction pass with exact source lines, dependencies and a disposition. Preserve these sources until that pass is complete.
