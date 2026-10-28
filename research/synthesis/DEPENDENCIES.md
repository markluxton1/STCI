# Dependency and interface map

This map records **logical dependence** separately from **conceptual contact**. For exact hypotheses and audit links, consult the individual result records.

## Established dependencies

The historical jet rank-defect calculation in [order-one structure](../results/order_one.md) is a concrete example of global-section restriction failure. It is conceptually related to, but not proved equivalent to, the R-0030 local equation-module comparison defect or the saturated-layer divisors in R-0016/R-0019. These are **conceptual contacts**, not established implication arrows.

- **Low-degree and quartic carrier exclusions** -> [STCI-R-0001](../results/quartic_carrier_exclusion.md) plus audited factor reduction -> hypothetical defining degrees at least five.
- [STCI-R-0002](../results/cartier_singleton_lift.md) -> [STCI-Q-0001](../questions/cartier_projection_models.md) (restricted candidate normalization models -> unresolved actual projections and conductor descent).
- [STCI-R-0003](../results/fixed_carrier_conductor_criterion.md) -> [STCI-R-0004](../results/projection_phase_reduction.md) (full-conductor descent framework -> fixed-family phase/torsion reduction).
- [STCI-R-0005](../results/smooth_root_formal_obstruction.md) + [STCI-R-0006](../results/actual_ci_smooth_root_bridge.md) -> conditional consequences for actual complete intersections. The bridge hypotheses are essential.
- [STCI-R-0007](../results/quadratic_root_obstruction_model.md) + [STCI-R-0006](../results/actual_ci_smooth_root_bridge.md) -> conditional actual-CI application of the computed obstruction classes.
- [STCI-R-0008](../results/spectral_root_picard_criterion.md) -> existence criterion for graded second relations, **not** automatic ambient lifting.
- [STCI-R-0009](../results/moving_purepower_boundary.md) -> forced second-relation degeneration, **not** unrestricted impossibility.

## Conceptual connections, not proved implications

- Common normal factor / exceptional curve <-> spectral root scheme / graded relations.
- Successive blowups and Rees valuations <-> excess intersection and jet-discrepancy data.
- Carrier normalization and conductor <-> global constraints on the same pair of equations.
- Local cohomology and primitive thickenings <-> ambient jet-condition dependence.

These arrows are **research interfaces**, not established theorem dependencies. In particular, the common-factor and blowup material needs source-by-source audit before promotion.

## Epistemic guardrails

- Do not replace exact hypotheses by a generic phrase such as “smooth root” or “normal carrier.”
- Do not conflate a formal lifting obstruction with an obstruction to every actual pair.
- Do not treat quartic ancestor-incidence problems as surviving quartic-mate cases.
- Do not infer global STCI nonexistence from a finite-dimensional conditional model.
