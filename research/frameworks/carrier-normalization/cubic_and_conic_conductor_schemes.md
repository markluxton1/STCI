# Cubic and conic conductor schemes

[Carrier Framework](index.md) · [Original section addresses](normalization_conductor_projection.md)

## Entire cubic conductor schemes on smooth quartic scrolls

The October 8 scroll-conductor investigation extends beyond the smooth twisted-cubic downstairs conductor treated above. For an integral quartic carrier whose **finite normalization is a smooth rational quartic scroll** (F0 or F2 with its quartic hyperplane class), the source program classifies actual cubic conductor schemes using the entire conductor, including nonreduced and nongorenstein structures. The combined result excludes a mate supported on the fixed smooth quartic in characteristic zero under these hypotheses, in any mate degree. The proof uses the conductor duality sequence, Hilbert–Burch classification of the cubic conductor, generic Artin-module constraints, and full inverse-fiber conditions; it does not replace actual conductor schemes by reduced support. The independent Artin audit explicitly accepts the nonreduced reductions and supplies a direct completion of the double-line-plus-line case.

Source proof: [current proof](../../arguments/carriers/quartic_scroll_nonreduced_conductors.md) and [current proof](../../arguments/carriers/quartic_scroll_conductor_structure.md). Independent audit: [current proof](../../arguments/carriers/quartic_scroll_nonreduced_conductors.md). The alternate differential/slice proof in the first source has a separate conditional geometric passage and is **not** needed for this source-level synthesis. This is an audited historical claim, not a new result. It says nothing about singular scroll normalizations or arbitrary nonnormal quartic carriers.

A separate October 12 conductor-phase investigation for the admissible genus-one quintic A4 normalization, with Jbar=0 and coprime conormal cubics, derives an actual phase bound and all-mate exclusion within that restricted Jbar-zero, coprime-cubic stratum. Although the owner note's header says audit pending, the companion independent audit explicitly reports PASS for the all-mate exclusion under its precise geometric hypotheses, including the separately treated ramified-line locus. This does **not** exclude all genus-one quintic carriers, the common-root stratum, or other quintic normalizations. Sources: [current proof](../../arguments/carriers/nonendpoint_conormal_and_conductor_modules.md#6-jbar-zero-coprime-conductor-phase-bound) and [current proof](../../arguments/carriers/nonendpoint_conormal_and_conductor_modules.md#7-jbar-zero-conductor-phase-independent-audit). This belongs primarily to the low-degree carrier family and is cross-referenced here for coverage.



## Entire-conic quadratic conductor: exact power criterion

This is a reusable *actual-conductor algebra* theorem, not a classification of which conic conductor data occur for the fixed curve. For a characteristic-zero degree-four ADE del Pezzo normalization with a two-quadric anticanonical embedding, choose a projection from a point outside the surface. The graded equations can be arranged as
\[
Q_1=z^2-Az-R_1,\qquad Q_2=Lz+R,
\]
where (A,L) are linear and (R_1,R) quadratic in the four target coordinates. Elimination gives the quartic
\[
F=R^2+ALR-R_1L^2.
\]
Under the complete-intersection, finite-birational projection hypotheses, the **entire downstairs conductor scheme** is the plane conic (\Gamma=V(L,R)), not its reduction. It may be smooth, reducible, or a double line. The algebra audit accepts this exact calculation conditionally on the geometric setup; it does not independently establish every claimed anticanonical embedding or fixed-\(C_0\) spanning application. Sources: `research/notes/2026-10-09-session-genus-one-entire-conductor.md` and [current proof](../../arguments/carriers/genus_one_two_adjoint_and_conductor.md#source-2026-10-09-session-genus-one-entire-conductor-algebra-independent-auditmd).

Let \(M=\mathcal O_\Gamma(1)\) and suppose the *entire* finite flat quadratic algebra is
\[
p_*\mathcal O_D=\mathcal O_\Gamma\oplus M^{-1},\qquad w^2=\delta,
\]
with trace involution (\sigma\(w\)=-w). For a nonzerodivisor section \(q=m+w\ell\), where (m\in H^0\(\Gamma,M^2\)), (\ell\in H^0\(\Gamma,M\)), (\delta\in H^0\(\Gamma,M^2\)), put
\[
\mathcal C_{\rm cyc}=\left\{\left\(\frac{1+\zeta}{1-\zeta}\right\)^2:\ \zeta\text{ a root of unity},\ \zeta\ne\pm1\right\}.
\]
For a smooth conic or the **entire plane double line**, a positive power of \(q\) is invariant under \(\sigma\) if and only if
\[
m\ell=0\quad\text{on the entire }\Gamma,
\qquad\text{or}\qquad
m^2=\rho\delta\ell^2\quad\text{on the entire }\Gamma
\quad\text{for some }\rho\in\mathcal C_{\rm cyc}.
\]
For two distinct lines, impose the corresponding criterion **separately on both components**, with possibly different cyclotomic constants and a common multiple of the resulting power orders. These are equalities of entire schemes, including nilpotents, not equations only on reduced supports. The proof uses (\sigma\(q\)/q) in generic Artin rings, separability of (T^n-1) in characteristic zero, and injectivity of sections into generic total quotient rings. A split quadratic conductor permits unbounded phase order; this algebraic criterion alone does **not** bound mate degree or exclude the remaining genus-one carrier models. Sources: [current proof](../../arguments/linkage/quadratic_conductor_power_descent.md) and its `2026-10-09-session-quadratic-conductor-power-descent-independent-audit.md`.

The quadratic-algebra proof uses2 invertible to split trace and define the involution. That splitting persists in characteristic p≠2, but the all-positive-power criterion above uses characteristic zero: powers divisible by p can remove nilpotent terms that survive every characteristic-zero power. In characteristic2 even the trace splitting and involution require replacement. No unrestricted positive-characteristic version of this entire-scheme power criterion is asserted.

The companion genus-one weak del Pezzo reduction and D5 root-saturation filter concern which actual normalizations and primitive sections can occur. They are **separate geometric hypotheses**, not consequences of the quadratic-algebra criterion. The explicit four-A1 projections are negative full-inverse-support examples, not an exhaustion of the lattice stratum. See [current proof](../../arguments/carriers/genus_one_two_adjoint_and_conductor.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd), [current proof](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-torsion-filtermd), and [current proof](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-singular-delpezzo-four-a1-familymd).



