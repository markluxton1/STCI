# Mixed-degree Fitting strata and thickening realization

[Formal normal Framework](index.md) · [Original section addresses](normal_filtration_boundaries.md)

## Mixed (4,6): Fitting divisor and pole strata

The formulas below retain structural information from the historical
degree-\((4,6)\) tests. The characteristic-zero quartic-mate cases are
closed by the [quartic-carrier theorem R-0001](../../results/quartic_carrier_exclusion.md).
References to strata remaining outside an individual calculation describe
that calculation's scope, not open quartic-mate or \((4,6)\) STCI cases.
The saturated-filtration and Fitting identities remain useful comparisons
for higher-degree work under their stated hypotheses.

The [October 5 mixed-six calculation](../../arguments/residuals/quasiprimitive_residual_cycles.md#mixed-46-the-first-normal-fitting-divisor-and-the-multiplicity-six-defects) assumes a finite-flat quasiprimitive length-six Gorenstein algebra, locally free Banica–Forster pieces, and perfect multiplication pairings. For defect divisors `0<=D2<=D3`, the graded pieces are `O,L,L^2(D2),L^3(D3),L^4(D2+D3),L^5(D2+D3)`. The coordinate-independent first-normal cokernel Fitting divisor satisfies `A=D3+min(D2,D3-D2)`, with the minimum taken pointwise. The proof computes torsion `T=N/yB`: its length is `ord(D2+D3)`, while `length(T^2)=max(ord D2-ord(D3-D2),0)`, and `length(T/T^2)=ord A`. In particular `D3<=A<=D2+D3`; neither extreme equality is universal.

For degree pair `(4,6)`, the seven necessary numerical types are `e=0: (d2,d3)=(1,8),(2,7),(3,6),(4,5)` and `e=1: (0,4),(1,3),(2,2)`. Their coarse nonregular pole lengths reduce to `e=0: p=1,2,3,4` and `e=1: p=4,5,6`. This is a restriction on possible strata, not a realization or an STCI exclusion. The [regular-ratio proof](../../arguments/residuals/quasiprimitive_residual_cycles.md#regular-ratio-degree-46-pairs-a-pure-horizontal-direction-is-impossible) separately excludes only the two pure constant horizontal directions when `e=0` and the quotient ratio is globally regular. Its quadric-residual and cubic-jet argument does not treat mixed directions, e=1, or nonregular pairs. The [earlier rank-six audit](../../arguments/residuals/quasiprimitive_residual_cycles.md#mf6-audit-and-higher-jet-exclusions-for-the-mixed-46-pole-branch) records the saturated-lattice hypotheses and the remaining `(4,5)` defect case.


## The geometric realization problem for successive thickenings

The characteristic-zero conormal bundle of the fixed quartic is balanced, whereas the characteristic-two splitting changes [R-0020](../../results/quartic_conormal_characteristic_jump.md). The prescribed characteristic-two fourth-equation kernel [R-0031](../../results/quartic_char2_fourth_equation_kernel.md) makes a key distinction concrete: cancellation-generated higher initials cannot be discarded merely because two low-order symbols appear dependent. The prescribed \(\mu_4\) degeneration [R-0021](../../results/quartic_mu4_degeneration.md) likewise warns that flat arithmetic specialization need not preserve reduced support. Neither example proves a universal characteristic-zero obstruction.

The [weighted-initial note](../../arguments/normal-geometry/normal_boundary_weighted_initials.md#normal-boundary-strata-weighted-initials-and-lifting) uses valuations of coefficient functions over \(k(C)\) to track special-point Newton changes. Those coefficients depend on chosen normal coordinates; intrinsically their leading terms are sections of symmetric powers of the conormal bundle. This is a *methodological proposal*, not an established coordinate-independent tropical obstruction. The [normal torsion/genus note](../../arguments/normal-geometry/curvilinear_genus_and_defects.md#normal-torsion-spectral-genus-budget) further distinguishes ordinary torsion from saturation divisors: counting both as independent genus contributions double-counts the same phenomenon in its stated curvilinear setting.

### A finite, checkable continuation

Choose a specific surviving pair of degrees at least five, or a specified lower embedded thickening. Record (i) its generic transverse algebra and **full** initial ideal; (ii) the saturation and exceptional-point defect of each conormal layer; (iii) the exact obstruction class and allowed boundary divisor for the next lift; and (iv) the image of actual global homogeneous sections in the required jets. At each step distinguish failure of a necessary condition from failure to construct a solution. Finally check properness and actual residual support independently. The [boundary repair](../../arguments/normal-geometry/normal_boundary_weighted_initials.md#normal-boundary-strata-weighted-initials-and-lifting) and [one-step completion](../../arguments/one_step_boundary_repair.md#2026-10-27-one-step-boundary-obstruction) analyses provide scoped tools, not a theorem that this procedure always decides STCI.

**Remaining mathematical gap:** there is no established general implication from a generic or graded root configuration and its local repair data to a pair of global equations with sole reduced support. Conversely, there is no established theorem excluding all such configurations when first relations are nonsaturated or the comparison defect is punctual.


## Local comparison, saturation, and the unresolved singularity interface

[R-0030](../../results/local_filtration_comparison_defect.md#statement) compares
minimal equations of the full initial ideal with the filtration of the actual
equation module. Its [proof](../../arguments/filtered_equation_comparison.md#local-comparison-and-the-punctual-defect)
gives the generic generator count, DVR length formula, and smooth-carrier
criterion under their respective hypotheses. See the
[sole-support question and controls](open_normal_geometry.md#punctual-relative-defect-under-sole-support).

### Three distinct exceptional phenomena

1. **Unsaturated first relation.** The coefficient section vanishes at a point of C, so the first-relation line and its quotient acquire a base-point or torsion issue. The [nonsaturated resultant result R-0016](../../results/nonsaturated_first_relation_resultant.md) supplies a scoped numerical test, not a blanket exclusion.
2. **Singular but nonvanishing root divisor.** The coefficient section remains nonzero, while roots collide or become nonreduced. Saturation alone does not prevent this. The formal-root and Picard-descent restrictions must be applied with their own hypotheses.
3. **Punctual comparison defect.** Even if the generic initial ideal has the expected two generators, special fibers can acquire cancellation-generated initials. R-0030 measures this separately from first-relation saturation and from residual components.

These alternatives need not be mutually exclusive. A proof eliminating one does not eliminate the others. In particular, do not infer properness or sole support from a vanishing graded obstruction.

