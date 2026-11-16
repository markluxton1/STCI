# Normal quartic carriers

Over an algebraically closed field of characteristic zero, every normal
integral quartic carrier of the fixed \(C_0\) or a projective equivalent
is excluded against mates of arbitrary positive degree by
[R-0001](quartic_carrier_exclusion.md).
The [current full normal proof](../arguments/carriers/quartic_carrier_proof.md#3-normal-quartics-exceptional-correction-and-actual-ideal-vanishing)
contains the exceptional passage and correction argument, denominator
compression, irreducible harmonic bound, exact reduced/tree reductions,
and TypeD pulled-maximal-ideal contradiction. The exact computations
remain explicit dependencies; they eliminate necessary supersets rather
than classify realized surfaces.

Some earlier reductions had broader curve hypotheses: Jaffe's rational-
singularity quartic theorem concerns smooth curves on such carriers;
positive-genus ruled carriers cannot contain **any** rational degree-four
curve; the denominator theorem applies conditionally on a whole rational
resolution. Their proofs and limits are retained in
[NORMAL_PRIMITIVE_CARRIERS_AND_BOUNDS](../arguments/carriers/normal_carrier_compression.md#exact-sources-and-scope)
and [normal compression and jets](../arguments/carriers/normal_carrier_compression.md#related-distinct-developments).
Those broader preliminary statements do not generalize the final fixed-
\(C_0\) exclusion to every rational quartic embedding.

The lattice program for B1/B2/B3/D has a finite necessary reduction using
the passage and first-normal budgets, followed by the reduced-cycle and
nonreduced-tree calculations. See the [normal proof starting at §3.1](../arguments/carriers/quartic_carrier_proof.md#31-compression-and-the-passage-budget)
and the [historical note at commit 2e29ee4](https://github.com/markluxton1/STCI/blob/2e29ee4f45cd7e177c4fef59673f1d05622b41a4/research/open/normal_quartic_remaining.md).
For reuse on other carriers, see the hypotheses of [global denominator compression](../arguments/carriers/normal_carrier_compression.md#1-global-denominator-compression)
and the [index-two counterexample to a bound on numerical correction](../arguments/carriers/numerical_surface_pullback.md#cartier-index-does-not-bound-the-numerical-correction).

The [normal-quartic proof's exceptional-correction analysis](../arguments/carriers/quartic_carrier_proof.md#3-normal-quartics-exceptional-correction-and-actual-ideal-vanishing)
covers the smooth elliptic exceptional curve separately. The [Type D Green-function argument](../arguments/normal-geometry/saturation_rees_and_carrier_cases.md#q-two-arm-coefficient-one-tails-exact-comparison)
requires the terminal effective diagonal bound \(d_{\mathrm{eff}}\ge3\)
in its two-arm reduction (D25). The full normal proof
closes Type D via the pulled maximal ideal, with its [preservation review](../arguments/carriers/quartic_carrier_proof.md#normal-route-preservation-review)
recorded separately. The unrestricted higher-degree STCI question remains
open. Positive-characteristic quartic-carrier examples and the limits of
each proof mechanism are described in the [characteristic boundary](../arguments/carriers/quartic_carrier_proof.md#8-what-changes-in-positive-characteristic).
