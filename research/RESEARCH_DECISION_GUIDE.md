# What matters now: STCI research decision guide

This is a **navigation and prioritization guide**, not a new theorem, proof audit, or change to the accepted frontier. Consult [STATE.md](STATE.md) and the [canonical results](results/INDEX.md) for authoritative statements. The unrestricted fixed rational quartic STCI question remains open.

## Essential conclusions: read first

| Importance | What is established | Authority | Consequence |
|---|---|---|---|
| Decisive for low degrees | No integral quartic carrier of the fixed C0 admits a mate; with lower-degree exclusions, both defining degrees are at least five | [STCI-R-0001](results/quartic_carrier_exclusion.md) | Do not reopen quartic mate cases |
| General structural tool, not classification | Exact fixed-carrier full-conductor criterion | [STCI-R-0003](results/fixed_carrier_conductor_criterion.md) | Apply when a specific higher-degree carrier is available |
| Restricted higher-degree models | Three necessary Cartier-singleton normalization models | [STCI-R-0002](results/cartier_singleton_lift.md) | Investigate actual projections and conductor descent; do not infer existence or exhaustiveness |
| Restricted reduction | Projection phase/torsion-coset criterion | [STCI-R-0004](results/projection_phase_reduction.md) | Computation of actual phase images is still missing |
| Conditional infinitesimal toolkit | Smooth-root formal obstruction, actual-CI bridge, quadratic obstruction, spectral Picard criterion, pure-power degeneration | [STCI-R-0005 through 0009](results/INDEX.md) | Powerful only with exact hypotheses; not an arbitrary-STCI exclusion |

## Recommended research order (editorial judgment, not theorem)

**A. Primary: jet dependence and discrepancy geometry.** See [FRONTIER Priority 1](FRONTIER.md) and [synthesis Chapter 3](synthesis/03-infinitesimal-geometry.md). Why: seeks a geometric explanation for failures of independent containment conditions rather than another bounded computation. **Deliverable:** an intrinsic description of first jet restriction-map rank defects on the unique quadric, with hypotheses and examples. **Stop condition:** if the formulation reproduces only the already-closed quartic-mate cases, reframe as an ancestor/jet problem rather than claiming progress on actual mates.

**B. Primary alternative: entirely-thick successive-transform geometry.** See [FRONTIER Priority 2](FRONTIER.md), [two-surface synthesis](synthesis/02-two-surfaces.md), and [legacy thick topic](results/entirely_thick.md). Why: first symbols miss higher transverse contact. **Deliverable:** a valuation or exceptional-cycle invariant giving a nontrivial obstruction in a surviving higher-degree region. **Stop condition:** numerical inequalities alone or restated generic common factors do not count as progress.

**C. Targeted computational lane: Cartier singleton projection/conductor families.** See [STCI-Q-0001](questions/cartier_projection_models.md), [STCI-R-0002](results/cartier_singleton_lift.md), [STCI-R-0003](results/fixed_carrier_conductor_criterion.md), [STCI-R-0004](results/projection_phase_reduction.md). **Deliverable:** an actual admissible phase image and full-conductor torsion test for at least one model, not another formal reduction.

**D. Conditional root lane: actual equations versus full root relations.** See [STCI-R-0006](results/actual_ci_smooth_root_bridge.md), [synthesis Chapter 3](synthesis/03-infinitesimal-geometry.md), and [common-factor audit](synthesis/COMMON_FACTOR_SOURCE_AUDIT.md). **Deliverable:** a new implication valid beyond the bridge's saturation/smoothness/equal-order hypotheses, or a concrete defect obstruction. **Stop condition:** no more repackaging of existing restricted results as progress toward unrestricted STCI.

## What to ignore by default

- Historical handoffs and dated state snapshots when determining *current* theorem status.
- Legacy quartic B1/B2/B3/D mate cases as open cases: [STCI-R-0001](results/quartic_carrier_exclusion.md) closed them for the fixed curve.
- Individual validation logs or scratch outputs unless a canonical result, a reproducibility question, or an active computation points to them.
- New synthesis/audit notes as proof authority. They can clarify interfaces but cannot promote results.
- Generalization notes for other curves/characteristics when the immediate goal is the fixed characteristic-zero C0, unless a specific theorem transfer is justified.

## How to find evidence efficiently

**Question -> canonical record -> exact cited proof/acceptance -> independent audit -> certificate/computation (only if necessary).**

1. Find the ID in [results/INDEX.md](results/INDEX.md) or the tracked [question STCI-Q-0001](questions/cartier_projection_models.md).
2. Read the result's YAML scope, hypotheses, evidence, audits, and limitations *before* the exposition.
3. Follow the evidence links in that record; many point to preserved historical notes. Consult [source-note inventory](archive/ULTRA_SOURCE_NOTES_INDEX.md) only when the record lacks a direct path.
4. For exact computations use the [certificate map](certificates/README.md), [computation guide](computations/README.md), and [validation inventory](archive/ULTRA_VALIDATION_RECURSIVE_INVENTORY.md). Do not infer a certificate from an output filename.
5. If a note conflicts with a canonical result, apply [AUTHORITY.md](AUTHORITY.md); record the discrepancy rather than silently broadening the theorem.

## Completion test for future work

A new research contribution should answer at least one of: **(i)** exclude a genuinely surviving class of actual STCI presentations; **(ii)** establish a new general geometric constraint with explicit hypotheses and proof; **(iii)** compute a previously unresolved necessary/sufficient test for an actual candidate family; **(iv)** repair a substantive gap in an accepted proof. A restatement, inventory, or new notation alone does not meet this bar.

This guide ranks relevance and directs reading; it does not claim exhaustive dependency tracing across every historical file.
