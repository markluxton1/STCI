# Historical conversation recovery — current-main reconciliation

**Audit snapshot:** 2026-11-19, main `928053ea99b209fd02faa4b89a0d37ef3f11b02d`.
**Status:** provisional historical coverage ledger; **not** a canonical mathematical Result or a competing research priority list. This replaces the stale classification in the previous, now-unavailable `chatgpt/cross-conversation-recovery-audit` branch. Historical source retrieval was selective, not exhaustive.

## Reconciled high-priority candidates

| Historical cluster | Current canonical home | Disposition |
|---|---|---|
| H15 (Nov 5): full Chow-polytope rigidity for the quartic | [R-0074](../results/chow_polytope_rigidity.md), [proof](../arguments/equations/chow_polytope_rigidity.md) | **Preserved and accepted**. Proof now uses endpoint-support test, exact separating-face resultant identities and degree exhaustion. Do not retain the earlier claim that the distinguished-vertex lemma was still open. |
| H16 (Nov 5): translate parameterization, set-level symmetric-power description | [Chow proof](../arguments/equations/chow_polytope_rigidity.md), [global equation framework](../frameworks/global-equation-realization/index.md) | **Set-level geometry preserved**; no scheme-theoretic Chow-locus isomorphism or two-equation realization theorem. |
| H07 (Oct 7): general-coordinate tetrahedron, 16 punctures, four weight-four rays, edge collisions | [general-coordinate boundary](../arguments/torus/general_coordinate_boundary.md) | **Preserved with stronger generality**: arbitrary realized contact vectors, gcd weights, proper ray-only tropical model, smoothness criterion, six resultant edge loci and a simple collision/blowup example. A global polyhedral wall fan over frame moduli is explicitly **not defined**. |
| H17 (Nov 13): enriched tetrahedral boundary diagrams and reconstruction | [boundary reconstruction and defects](../arguments/torus/boundary_reconstruction_and_defects.md) | **Substantially recovered** with bounded-degree uniqueness, characteristic-two counterexamples to finite-order reconstruction, labeled-facet gluing and exact fixed-degree feasibility. No general reconstruction functor or unrestricted STCI conclusion. |
| Nov 1: both supported Hilbert limits and distinction from actual generators | [full Hilbert limits](../results/supported_hilbert_full_limits.md), [argument](../arguments/torus_hilbert_boundary.md) | Preserved; no automatic CI realization at a limit. |
| Nov 5: constant embedded torus quotients, endpoint algebras | [argument](../arguments/torus_embedded_quotients.md) | Preserved, but not a classification of arbitrary moving quotients. |

## Earlier discussions to reconcile at proof level

These are **search matches**, not closure certificates. For each, compare the precise historical statement, hypotheses, characteristic, degree bounds, and whether the original reasoning was later retracted.

| Historical period / theme | Likely owner | Remaining audit check |
|---|---|---|
| August: unique quadric, proposed (2,4) absorption and fixed-ruling residual | [quartic geometry](../arguments/curve/fixed_quartic_geometry.md) and normal geometry | Distinguish proved no-absorption from failed proposed construction |
| September: (4,5), primitive conormal structures, pole corrections and (4,6) strata | [normal carrier](../results/normal_carriers.md), [ideal filtrations](../arguments/normal-geometry/ideal_filtrations_quartic_exclusion.md) | Compare exact low-degree exclusion, avoid retaining abandoned case counts as theorems |
| October: normal quartic carrier exceptional cases | [primitive carrier arguments](../arguments/carriers/normal_primitive_carriers_and_bounds.md) | Identify precise exceptions and later corrections |
| October: entirely-thick inequalities | [entirely-thick result](../results/entirely_thick.md) | Check the hypotheses and whether every historical inequality is included |
| October: special two-ray tropical compactification | [tropical endpoint argument](../arguments/torus/tropical_thickenings_and_endpoint_duality.md) | Already distinct from the general-coordinate H07 model |
| October: quintic conductor and descent | [quintic conductor](../arguments/carriers/quintic_conductor_geometry.md), [root descent](../arguments/carriers/root_descent_and_conductor_defects.md) | Keep normalization identities separate from unresolved descent |
| October: char-2 ribbon/triple obstruction and arithmetic lifting | [arithmetic argument](../arguments/arithmetic/z4_intrinsic_arithmetic_mechanism.md) | Compare integral obstruction versus mod-2 existence |
| October–November: sextic filtered jets, actual sources, conditional (6,16) gate | [filtered jets](../arguments/equations/global_equation_jets.md), [spectral framework](../frameworks/spectral-roots/index.md) | Distinguish source calculations from unresolved existence |

## Explicitly rejected historical claims

- Proposed generic projective (2,2) CI construction for the fixed quartic: false or a different curve.
- Proposed automatic descent from Laurent/global toric CI to two projective equations: not established.
- Scheme-theoretic identification of the Chow fiber with a symmetric product: not established.
- Any implication that general-coordinate tropical rays determine the intersection scheme of hypothetical defining surfaces: not established.

## Audit discipline

1. Check current `main` before classifying any historical claim as missing; the repository changes rapidly.
2. Preserve **source question, exact statement, proof status, current owner, and remaining gap**, not chat chronology.
3. Close an item only after content-level comparison. A keyword match is not enough.
4. Use canonical Result/Argument/Framework homes for mathematics. This ledger records *historical coverage only*, not an alternative KG queue.
5. Do not interpret the 17 historical clusters in the previous ledger as a complete count of all conversations.
6. After reconciliation, consolidate this ledger into existing documentation and retire it if redundant.

**Current finding:** H07, H15, H16 and H17 are no longer defensible as missing topics on the latest main. The next useful audit effort is the older August–October conversations, not a new proof of Chow rigidity.
