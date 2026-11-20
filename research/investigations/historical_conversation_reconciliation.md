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

## Batch 5: August–October source-level comparison (2026-11-19)

Conversation-history retrieval recovered August 22–23 exchanges and a September 30 research report. The historical summaries below are **source claims**, not new accepted results. Comparison was against the main snapshot named above; later commits must be checked before reusing the status.

| Source date | Historical content | Current owner / audit decision |
|---|---|---|
| Aug 22 | Cubic order-three contact was reported generically rank 14 over Q with only proportional mates; special reducible cubic \(Lq\) gave rank drops and residual support. A characteristic-three rank drop was suspected to be Frobenius-related. | [Fixed geometry](../arguments/curve/fixed_quartic_geometry.md), [degree exclusions](../frameworks/carrier-normalization/degree_exclusions.md). **Superseded for global exclusion**; the numerical rank assertions are not independently certified by this recovery pass. |
| Aug 23, early | On \(Q\simeq\mathbf P^1\times\mathbf P^1\), \(C\sim(1,3)\), residual \(Z\sim(3,1)\), with \(C\cdot Z=10\); a \((2,4)\) CI can degenerate to \(C\cup Z\). | [Fixed geometry](../arguments/curve/fixed_quartic_geometry.md). **Preserve as geometric background**, but the specific flat-family formula was not rechecked here. The claimed degeneration is not an STCI construction. |
| Aug 23, later | The proposed absorption \(C\cup Z\rightsquigarrow2C\) was ruled out using a ribbon conormal quotient. The historical discussion gave **different proposed degrees** (\(\mathcal O(-10)\) and later \(\mathcal O(-14)\)) depending on the attempted thickening; these are **not interchangeable**. | The definitive fixed-quadric obstruction is \(2C\sim(2,6)\ne(4,4)\). A conormal quotient of a specified ribbon needs its Hilbert polynomial and ideal sequence checked separately. **Do not promote the early ribbon argument as written**. |
| Aug 23 | No plane or quadric carrier; early discussion called \((3,4)\) the first unresolved degree pair, later invoking cubic literature. | [Quartic carrier exclusion R-0001](../results/quartic_carrier_exclusion.md) and [factor/degree reductions](../frameworks/carrier-normalization/degree_exclusions.md) now show hypothetical degrees \(\ge5\) in characteristic zero. Historical “first unresolved” labels are obsolete. |
| Sep 30 | \((4,5)\) and primitive conormal type exclusions; several pole/stratum counts in the old program. | [R-0001](../results/quartic_carrier_exclusion.md), [normal carriers](../results/normal_carriers.md). **Global exclusion superseded**; keep pole/stratum calculations only where they remain independent, correct mathematics. |
| Oct 7 | Entirely-thick numerical inequalities \(ab\ge4pq\), \(7ab+28pq\ge16(aq+bp)\), \(a\ge3p\), \(b\ge3q\); historical \((3,3)\) exclusion and \((3,4)\) equality investigation. | [Entirely-thick result](../results/entirely_thick.md) contains all four inequalities and the sharper constant-section \((3,4)\) boundary. **Closed as preserved** under its balanced-normal, exact-order, proper-pair, sole-support hypotheses. |
| Oct 7 | First normal forms do not determine local intersection multiplicity; illustrative \(f=y^2+x^{2n+1},g=y^2+2x^{2n+1}\). Historical excess-contact heuristics did not prove persistent horizontal centers remain untwisted or produce a projective residual curve. | [Rees/vertical controls](../arguments/normal-geometry/rees_and_vertical_controls.md), [entirely-thick result](../results/entirely_thick.md). **Preserve caution**, not a claimed all-degree obstruction. |
| Oct 11–12 | Normal quartic lattice/correction analysis and quintic conductor descent. | [R-0001](../results/quartic_carrier_exclusion.md), [normal carriers](../results/normal_carriers.md), [quintic conductor](../arguments/carriers/quintic_conductor_geometry.md). **Covered with stronger hypotheses and subsequent specialized proofs**; quintic normalization facts do not automatically descend to a mate. |

**Key mathematical correction:** A quartic surface section on the fixed quadric has class \((4,4)\). Although \(C\sim(1,3)\), a doubled divisor \(2C\sim(2,6)\), so a fixed-quadric \((2,4)\) CI cannot have divisor \(2C\). The old conormal-quotient discussion mixed distinct double-structure Hilbert polynomials; do not copy its line-bundle degree without recomputation.

**Coverage outcome:** No newly missing theorem certified in this batch. Exact August cubic-rank certificates and the \((2,4)\) family remain optional historical checks, not active STCI gates. This is a content-level comparison of named source claims, **not** an exhaustive scan of August–October conversations.
