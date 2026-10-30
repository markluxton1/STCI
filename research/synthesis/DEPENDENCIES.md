# Dependency and interface map

## Principal research routes — explicit missing arrows

The following are **programs**, not chains of proved implications. Each arrow requires an independently established bridge involving actual global homogeneous equations.

| Route | Available starting point | Missing implication | Required deliverable |
| --- | --- | --- | --- |
| Global determinant | Conditional lower-layer/socle and embedded one-step tests | Admissible lower embedding and extension data -> actual equation modules -> **proper decomposable** determinant-zero pair | Prove existence or uniform nonexistence of such a pair in the relevant source spaces; do not infer decomposability from a nonzero kernel |
| Uniform residual jets | R-0019 and R-0023–R-0025, fixed examples and fixed-carrier bounds | Fixed-carrier jet restrictions -> control over all relevant carriers and exceptional strata | A uniform positive residual-degree bound for actual proper homogeneous pairs |
| Conductor descent | R-0002–R-0004, R-0017, R-0034–R-0036 | Necessary normalization models -> actual higher-degree carriers -> full conductor and descent of sections | Computed admissible families and full conductor-unit descent, including non-Cartier/multiple-branch limitations |

A necessary condition is not sufficient; a conditional reduction is not an unconditional theorem; computational certificates cover only their stated inputs. Valuations, characteristic specialization and marked contact geometry supply potential interfaces but no established universal arrow to STCI nonexistence.


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


## Marked geometry: proved results versus missing implications

The flag-incidence theorem [R-0026](../results/quartic_flag_conormal_geometry.md) supplies the marked conormal and contact geometry used by the dual singular-scheme theorem [R-0027](../results/quartic_dual_singular_scheme.md). This is a stated canonical dependency. The ruled projection models [R-0028](../results/quartic_ruled_projection_geometry.md) and arithmetic four-section family [R-0029](../results/quartic_arithmetic_ruled_models.md) are separately scoped constructions; R-0029 uses the prescribed degeneration of R-0021.

There is **no proved implication** from these contact or dual singularity schemes to a common singular point of arbitrary STCI equations on C. Nor does the projected conductor model imply descent for every carrier. The proposed arrows from actual normal initial ideals to contact flags, and from contact flags to global conductor obstructions, remain research questions.

The October 27 one-step source supplies a different conditional bridge: for a fixed embedded lower thickening and actual proper equations of degree product (n+1)deg(C), determinant zero in its torsion-free equation module is equivalent to sole reduced support. This source-level criterion is not a promoted universal existence theorem; it requires a suitable lower thickening and proper decomposable kernel point.

## Cross-family proof obligations

These are the concrete proof obligations at the interfaces. They are **not** additional established arrows.

| Proposed implication | What must be supplied | Failure mode already seen |
| --- | --- | --- |
| Weighted normal data -> residual support | Full cancellation-stable initial ideal, integral specializations, proper global pair, projective cycle comparison | Scalar valuations and vertical exceptional support alone are insufficient |
| Saturated lower layers -> actual embedded thickening | Fixed lower embedding, extension class, allowable repair divisor and surjective equation-module quotient | Abstract graded layers can fail to lift |
| Embedded thickening -> two hypersurfaces | Actual source maps in both degrees, decomposable determinant-zero point, properness and degree exhaustion | A nonempty formal or linear kernel need not contain a proper decomposable pair |
| Characteristic-two construction -> characteristic-zero construction | A specified flat embedded deformation with controlled generic reduced support and base | The mu4 family is flat but has extra generic components |
| Ruled/dual contact -> carrier exclusion | An intrinsic map from actual equations to contact data and a full conductor descent calculation | Reduced endpoint or divisor-class information misses embedded corrections |
| Fixed-carrier jet bound -> unrestricted exclusion | A family covering all carriers under consideration and its exceptional rank-drop strata | A single fixed sextic only excludes its own mate family |

The exact determinant test in the reviewed October 27 one-step source is unusually strong **after** fixing the lower embedding and assuming a proper degree-compatible pair. It does not construct the lower embedding or prove that a proper determinant-zero pair exists. This should be the default separation when moving from local structure to a claimed STCI conclusion.

## Epistemic guardrails

- Do not replace exact hypotheses by a generic phrase such as “smooth root” or “normal carrier.”
- Do not conflate a formal lifting obstruction with an obstruction to every actual pair.
- Do not treat quartic ancestor-incidence problems as surviving quartic-mate cases.
- Do not infer global STCI nonexistence from a finite-dimensional conditional model.
