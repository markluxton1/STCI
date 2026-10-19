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

## Research viewpoints and agent discretion (editorial guidance, not theorem)

The broader question can start from \(C_0\subset V(F,G)_{\mathrm{red}}\) with no common surface component, without imposing STCI in advance. Write \([V(F,G)]=m[C_0]+R\) and \(de=4m+\deg R\). An STCI has \(R=0\); conversely, forcing \(R\ne0\) excludes an STCI presentation for the chosen pair. Exceptional vertical curves do not automatically imply residual components downstairs.

Possible complementary viewpoints are: (a) generic filtered transverse algebras and full initial ideals; (b) global realization by normal jets and homogeneous equations; (c) Rees algebras, successive blowups, exceptional and residual intersection cycles; (d) carrier geometry, normalization, and conductor descent. None is a required first step. Work on one level can be valuable even before it forces a residual component.

The existing frontier offers several **nonexclusive** entry points: [jet dependence/discrepancy](FRONTIER.md), [entirely-thick successive transforms](results/entirely_thick.md), [root and formal-lifting questions](results/INDEX.md), and [fixed-carrier projection/conductor questions](questions/cartier_projection_models.md). Agents should choose or combine them based on potential mathematical leverage, not the number of existing records, convenience of case-splitting, or a mandated strategy. The possible Hilbert-function approach is one hypothesis to evaluate, not an adopted priority. New ideas outside these lanes are welcome if their assumptions and relationship to the original problem are explicit.

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
