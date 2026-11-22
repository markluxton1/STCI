---
id: STCI-F-0003
type: framework
title: Formal normal geometry of intersections containing the rational quartic
status: in_use
scope: "#fixed-setup"
bridges: "#simultaneous-realization-and-compatibility-problems"
relations:
  - kind: uses
    from: [STCI-R-0077]
    to: [STCI-F-0003]
    at: "#exceptional-geometry-and-components-downstairs"
---
# Formal normal geometry of intersections containing the rational quartic

## Fixed setup

Let k be algebraically closed of characteristic zero and
\[
C=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3_k.
\]
Use the [characteristic-zero conormal splitting](../../results/quartic_conormal_characteristic_jump.md)
to obtain \(N_{C/\mathbf P^3}\simeq\mathcal O_{\mathbf P^1}(7)^{\oplus2}\).

Let \(F,G\) define distinct integral surfaces containing \(C\), and set \(Z=V(F,G)\). **Do not assume** \(Z_{\mathrm{red}}=C\). The eventual STCI condition is a constraint to detect, not a standing hypothesis. In particular, a component of \(Z\) different from \(C\) may meet \(C\) at finitely many points, and the formal completion along \(C\) need not record its full global geometry.

## Simultaneous realization and compatibility problems

For any homogeneous form nonzero on a characteristic-zero CI supported on
the fixed quartic, its degree gives a lower bound on the generic length of
its multiplication image. The proof maps the last conormal layer of the
colon curve into the socle of the original CI. Applied to a differentiated
defining equation, this tests how many directions of the entire embedded
quotient move at first order. The bound concerns this intrinsic torus family
and uses no smooth-root or saturated first-relation hypothesis.
[Multiplier rank and its application](../../results/torus_quotient_movement_bounds.md#proof).

The problem is simultaneous realization of a generic local ideal, its embeddings in two carriers, and the ambient intersection.

At the generic point of C, choose a finite-colength ideal \(J_\eta\subset K[[X,Y]]\), where \(K=k(C)\), representing a candidate generic thickening \(T_\eta=\operatorname{Spec}(K[[X,Y]]/J_\eta)\). For the actual intersection, \(J_\eta=(F,G)K[[X,Y]]\) when this quotient has finite length. More generally, ask whether a candidate \(J_\eta\) can arise from a coherent ideal sheaf \(\mathcal J\subset\mathcal O_{\mathbf P^3}\) with \(\mathcal J\subset I_C\), whose generic completion is \(J_\eta\). Such a global realization can have extra components or special-point structure; no purity or STCI hypothesis is implicit.

There are **four interdependent tests**, not a sequential list of independent classifications:

1. **Abstract/generic thickening:** what finite-length \(K[[X,Y]]\)-algebras (with specified embedding in the formal normal plane) can occur, and what intrinsic invariants and deformations do they possess?
2. **Realization inside each carrier:** for integral surfaces \(X_F=V(F)\) and \(X_G=V(G)\) containing C, can the same thickening be embedded as a closed subscheme of each? In ideals, this requires \((F)\subset\mathcal J\) and \((G)\subset\mathcal J\) (and the corresponding containments after completion). Separate embeddings into unrelated abstract surfaces do not suffice.
3. **Ambient realization:** does the candidate thickening and its chosen normal embedding extend to a coherent closed subscheme of \(\mathbf P^3\) with the prescribed restrictions along C? This imposes global section, gluing, degree and normal-bundle constraints not visible over K alone.
4. **Joint compatibility and actual intersection:** can the *same ambient embedding* and the *same pair of global integral surface equations* realize all of the preceding data with \(\mathcal J=(F,G)\)? Merely having \((F,G)\subset\mathcal J\) shows the candidate thickening lies in the intersection; equality is stronger. To obtain an STCI, one must additionally prove \(V(F,G)_{\mathrm{red}}=C\), excluding extra components globally.

Thus the question is not only whether \(T\) lies in \(X_F\), in \(X_G\), and in \(\mathbf P^3\) separately, but whether these are **the same closed immersion and compatible factorisations**
\[
T\hookrightarrow X_F\hookrightarrow\mathbf P^3,
\qquad
T\hookrightarrow X_G\hookrightarrow\mathbf P^3,
\]
with the additional equality \(I_T=(F,G)\) when T is meant to be the full intersection scheme.

## Three distinct constructions

Write \(J=I_C\subset\mathcal O_{\mathbf P^3}\) and \(I=(F,G)\subset J\). Distinguish:

1. The \(J\)-adic completion of \(\mathcal O_Z=\mathcal O_{\mathbf P^3}/I\), with its induced filtration.
2. The normal cone \(\operatorname{Spec}_C\operatorname{gr}_{J\mathcal O_Z}\mathcal O_Z\), and its projectivization (which can lose information).
3. The scheme-theoretic intersection of the **strict transforms** of the two surfaces on \(E=\mathbf P(N_{C/\mathbf P^3})\subset\operatorname{Bl}_C\mathbf P^3\).

These are related, but generally not identical. In particular, the intersection on E is described by the leading normal forms of the individual surfaces, while the initial ideal of (F,G) may contain additional initial forms arising from combinations of generators. Saturation and higher relations matter.

Their comparison requires exact ideals and saturations, distinguishing
intrinsic data from dependence on chosen generators. For proved local comparisons
of full initial ideals and actual equations, see
[R-0030](../../results/local_filtration_comparison_defect.md).

At the generic point \(\eta_C\), after a choice of formal parameters, study \(I\subset K[[X,Y]]\), \(K=k(C)\simeq k(t)\). Orders \(r=\operatorname{ord}_C F\), \(s=\operatorname{ord}_C G\) and the leading forms provide the first layer, not a complete invariant. When \(C\) is an isolated generic component of the intersection, the length \(\ell_{K[[X,Y]]}(K[[X,Y]]/I)\) measures its generic multiplicity. The identity \(de/4\) for this length requires that C be the only one-dimensional component of the global complete intersection; it must not be imposed in the broader setup.

<a id="which-mixed-degree-pairs-truly-need-an-entirely-thick-analysis"></a>
### Which actual pairs truly need an entirely-thick analysis?

The [all-degree normal-replacement theorem](../../arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier) (pending independent audit) characterizes precisely when the larger-degree generator system of a sole-supported CI admits a normal integral member: the generic transverse Artin algebra has embedding dimension at most one. Equivalently at least one first normal symbol is nonzero. Equal degrees are included. This is a property of the actual CI ideal, independent of its degree-compatible generators; two generic order-at-least-two generators cannot be changed into an order-one member of that system. A different thickening on the same reduced support is not excluded by this observation. The quadric bound gives this reduction for every hypothetical \((5,b)\) pair, and the graph bound for \((6,6)\). The Hodge equality and exact-index criterion then decide mate existence on a fixed normal carrier.

The [almost-Cartier power–socle extension](../../arguments/carriers/normal_carrier_symbolic_torsion.md#normality-is-unnecessary-the-actual-almost-cartier-power-theorem) applies the same top-defect, symbolic-power, and first-layer arguments to any integral hypersurface carrier which is generically regular along the support: the DVR at its generic point and the surface's S2 property suffice for the necessary divisions. The [normalized Hodge/APic test](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) then identifies precisely when that local geometry can give a sole-support mate on the fixed carrier. Normality away from the curve is not a premise of these extensions. Generic embedding dimension two for the actual pair remains a separate case. Independent audit is pending.

The [branch valuation dictionary and exact marked-ideal Hodge gap](../../arguments/carriers/numerical_surface_pullback.md#branch-valuations-and-the-actual-first-blowup) now work also in the entirely-thick regime on a specified integral carrier. They identify the actual first-blowup coefficients with \(n_i-qe_i\) and put componentwise restrictions on the special exceptional contributions. Even without generic regularity, a no-vertical single-root carrier cannot admit a mate, and for two no-vertical branches the necessary rational intersection matrix and [Cartier cluster partition](../../arguments/carriers/numerical_surface_pullback.md#cartier-test-divisors-and-the-degree-three-per-order-boundary) are explicit. This is a bridge from generic transverse excess to normalized special-point geometry, not a classification of the filtered pair or its Rees valuations. Independent review is pending.

The first mixed pair where
**both** equations can have
normal order two is \((6,8)\):
the universal [graph residual
bound](../../arguments/residuals/blowup_residual_geometry.md#5-integer-strengthening-usefulness-region-and-exact-limitations)
specializes to \(K=80-10b\)
for \((6,b)\) with orders
\((2,2)\). It is positive at
\(b=6\), giving the established
\((6,6)\) exclusion of that
order pattern, but vanishes
at \(b=8\). This is a
**failure of the available
necessary bound**, not a
construction or a claim that
the higher-order algebra is
noncurvilinear everywhere.
It identifies a precise
interface where the full
initial ideal, higher normal
coefficients and actual
homogeneous sources cannot
be replaced by the normal
Hodge criterion. Neither
case's special geometry
has been silently promoted
to an all-degree result.

The [ample strict-carrier compression](../../arguments/residuals/blowup_residual_geometry.md#lefschetz-compression-on-ample-strict-carriers) transfers the actual-index method to a smooth sole-support strict intersection on the first blowup. If its multiplicity is \(c\) and the ample strict carrier is generically regular along it, then its index lcm \(R\) satisfies \(c/R\mid\gcd(a,p)\). Under the stated section-lifting inequalities, a nontrivial quotient gives a lower-degree ambient mate. On the \((3p,4q)\) edge with \(p\le q\) those inequalities hold. In particular the entirely-thick \((6,8;2,2)\) case has a generically curvilinear first strict intersection, a normal general strict octic and an actual index-eight point (LC4). This uses R-0077 and the characteristic-zero low-degree exclusion; it neither proves normality of the original octic nor excludes the pair. Review pending.

The [pointwise graph resultant and finite modification formulas](../../arguments/residuals/blowup_residual_geometry.md#socle-defects-on-the-two-presentations-of-the-first-graph) identify the divided exceptional resultant with \((c-1)\Theta+D_{\rm top}\) for a generically curvilinear sole-support strict CI, where \(\Theta\) is tangency of its normal line to the exceptional surface. This is the specialization of [CF1--CF4](../../arguments/normal-geometry/curvilinear_genus_and_defects.md#cartier-cuts-and-finite-modifications-of-the-saturated-filtration), valid for actual Cartier cuts and finite modifications of curvilinear thickenings in arbitrary smooth ambient threefolds. On the \((3p,4q)\) edge, the finite map to the image quintic CI in \(V_5\) has length defect \(pq(q-1)\) at the marked point, with pointwise top-defect change \((c-1)\xi-(q-1)\), \(\xi=0,1\) from the actual conormal modification. The [marked-line obstruction ML9](../../arguments/residuals/blowup_residual_geometry.md#all-orders-the-marked-line-comparison-by-interpolation) eliminates primitivity at the prescribed marked point for every mixed \((3p,4q)\) edge pair with \(2\le p\le q\), without ADE or normality assumptions. Thus the globally primitive mixed \((6,8)\) row is excluded, not merely conditionally: only the mixed slope-four and endpoint slope-five rows remain there, with positive marked defect in the mixed row. Of the five necessary global primitive order pairs on the full edge, mixed directions survive this test only at \((10,4),(21,3)\); endpoint directions remain subject to their separate splitting and line contact. The [full marked finite-modification lattice](../../arguments/residuals/blowup_residual_geometry.md#full-marked-finite-modification-lattice-in-the-primitive-at-the-point-stratum) identifies the completed image ideal for \(q=2\) in the primitive graph stratum as \((y^2-x^2t,t^{2p})\), with multiplication defects \(D_j=2\lfloor j/2\rfloor\); for a generically regular image carrier the local index is two (marked \(D_{2p+1}\)) or \(4p\) (multiplicity at least three). The opposite [smooth marked image-carrier lane](../../arguments/residuals/blowup_residual_geometry.md#the-opposite-marked-stratum-a-smooth-image-carrier-and-a-forced-graph-defect) gives strict equations \(xv=t^{2p},v^q=0\), defects \(D_j=\lfloor j/(2p)\rfloor\) and marked index \(2p\) on the strict carrier. A degree-two image mate there would descend to an original degree-four mate by exact conic trace cancellation, so is excluded. For \(q=2\) and an integral smaller image carrier its minimal image mate degree is therefore four; for \(p=2\) an actual index-eight point away from the smooth marked point is forced. These deductions await independent review.

The [edge recovery theorem SC6](../../arguments/residuals/blowup_residual_geometry.md#recovering-generic-curvilinearity-in-all-orders-on-a-subset-of-the-edge) shows that on the mixed \((6,4q;2,q)\) edge the strict sextic always has order one, and for \(q\ge2\) a general strict carrier of the other equation is normal with at least \(9q-10\) distinct moving index-\(4q\) points. The first strict CI must be nonprimitive somewhere for \(q>2\). Across the full \((3p,4q)\) edge, global primitivity on the graph has only the five necessary order pairs \((2,2),(5,19),(6,8),(10,4),(21,3)\), by the [primitive edge arithmetic](../../arguments/residuals/blowup_residual_geometry.md#primitive-graph-structures-on-the-full-degree-threefour-slope-edge). This is not the classical primitive list on \(C_0\); it applies to the first strict intersection. The [normal K3 torsion theorem](../../arguments/carriers/normal_carrier_symbolic_torsion.md#a-uniform-torsion-bound-on-normal-k3-carriers) also gives an all-mate-degree bound \(R\le16\) on globally ADE degree-two image carriers in \(V_5\), with a mate there in degree at most eight; conic vanishing for an actual lift to the original problem is separate. The results are pending review.

### Classical primitive exclusion and the fixed nonprimitive defect

[Ellia's primitive CI theorem](../../literature/README.md#ellia)
is a **stronger existing
starting point** than a
generic normal-form
enumeration: a primitive
STCI on a smooth rational
quartic must occur among
ten explicit degree pairs,
none with degree five or
equal pair \((6,6)\).
Therefore every hypothetical
\((5,b)\) or \((6,6)\)
sole-support pair has a
point of \(C\) where
**both defining surfaces
are singular**. For a
quintic generator the
other equation's generic
curvilinear intersection
can still be primitive
away from finitely many
such points; the
nonprimitive locus is
not an optional special
case. The unrestricted
common-singular-point
statement in all defining
degrees remains **unproved**.

For every generically curvilinear actual pair, the [unified first-symbol and defect analysis](../../arguments/carriers/normal_carrier_divisor_geometry.md#the-global-moving-root-theorem-the-larger-normal-carrier-has-index-m) decomposes the general larger carrier's first-symbol divisor into the fixed common gcd \(B_{\rm np}\) and disjoint reduced moving zeros. There may be no moving zeros. Each moving zero has local Cartier index \(m\), but zero top defect. Even without any moving zeros, the actual top defect has support exactly \(B_{\rm np}\), by the pointwise Frobenius and monomial-lattice equalities. This connects the normal-carrier index theorem to the full saturated filtration of the same CI. The [uniform reduced-gcd test](../../arguments/carriers/normal_carrier_divisor_geometry.md#reduced-common-first-normal-divisor-a-uniform-marked-ade-and-rank-test) gives actual filtration coefficients \(\lfloor i/r_P\rfloor\) at a simple fixed point; it is not an identification of arbitrary nonreduced defects by their lengths. In particular, the all-degree congruence for \(m\) with prime factors \(1\bmod4\) shows why even very high index strata can require multiple common roots. These extensions require independent audit.

It does **not** identify
the actual special-point
defect structures from
their support alone:
their higher jets,
homogeneous source maps,
and conormal gluing
remain necessary.

For actual curvilinear full primaries inside a Gorenstein intersection, [linkage replaces the sole-support socle identity](../../arguments/residuals/residual_capacity_and_constructions.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component) with a signed top class and complementary attachment layers. [Finite modification](../../arguments/residuals/blowup_residual_geometry.md#signed-finite-transfer-throughout-the-interior-equality-boundary) extends the graph comparison to a residual center. The [attachment equation quotient](../../arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers) has its own exact duality, not yet an identity with arbitrary filtered comparison defects.

## Exceptional geometry and components downstairs

The joint zeros of the two actual leading forms on the first exceptional
divisor give a projective residual test. On the boundary of zero
direction degree, sole support forces one constant section. Its normal
bundle on the blowup has splitting \((2,5)\) at the endpoint directions
and \((3,4)\) elsewhere in characteristic zero. This turns the embedded
quadratic transition into a bound on the next two equation orders.
[Normal directions and the second blowup](../../results/connected_normal_directions.md#statement).

Separate horizontal components over C (dominating C) from vertical components over special points of C. Study their scheme structures and behavior under successive blowups. An exceptional component does **not** by itself prove that Z has another component downstairs: it may encode higher contact, a special fiber, or excess intersection. Conversely, if another global component meets C, its formal trace can influence the exceptional scheme. Establish precise implications rather than equating these phenomena.

Generic completion over \(K\) misses distinct residual curves, including
those meeting \(C\) at special points. An additional curve downstairs requires a criterion involving exceptional schemes over all
points. See the [cycle and visibility analysis](../residual-construction/two_surfaces.md#25-actual-sources-finite-jets-and-formal-visibility).

The normal cone, strict-transform intersection, and scheme-theoretic total transform should be compared through their defining graded/Rees constructions. Keep track of whether a claimed direction or component is intrinsic to the ideal or depends on the chosen pair of surfaces.

## Valuations and tropical perspective

The function field K is not itself a Laurent-series field. A chosen point of C gives a completion \(k((t))\) after a local parameter choice; in characteristic zero, Puiseux-type extensions can be used in an algebraic closure of that completion. Passing instead to \(\overline K\) is a different operation. State which field and valuation are being used.

Weighted initial ideals, valuations and tropical geometry organize successive normal directions, degenerations and cancellation. Cancellation involves intrinsic initial ideals and relations. In particular, the tropicalizations of two principal equations need not determine the tropicalization of their ideal.

The key question is whether these methods yield structural criteria for allowable formal thickenings and their global realizations, and whether specializations along C force additional components or obstructions.
The [valuation and specialization questions](../../arguments/normal-geometry/formal-normal-intersection.md#5-focused-theorem-level-questions-all-open)
give more specific comparisons.

## Multiplicity two as a test

For generic intersection length two, describe the possible local
complete-intersection structures and their behavior under blowup, allowing
residual components in the global intersection. Check compatibility of the
two generic normal orders with length two. Separate the local conclusions
from the conditions for an ambient realization and for sole reduced support.

The assertion that two STCI defining surfaces share a singular point on C
is unproved and cannot be used as an obstruction. The fixed integral
quartic-carrier exclusion is [R-0001](../../results/quartic_carrier_exclusion.md).

## Filtrations and comparisons

In characteristic zero, the generic transverse Hilbert function determines the **maximum**
length of the separated quadratic conductor as the missing linear
section and its quadric lift vary. Four general simple zeros attain
it. An osculating quadric concentrates the boundary at one point and
gives a smaller upper bound there. The lengths allowed by this
filtration bound already exceed the required scalar minimum; the
embedded coefficient map retains a further test.
[Local lattice and global comparison](../../results/moving_quadratic_conductors.md).

For the fixed osculating conormal quotient, the
[primitive-triple class](../../arguments/normal-geometry/osculating_ribbon_obstruction.md)
is \(2[u^{-2}]\ne0\). A finite-flat quasiprimitive flag extending that
ribbon needs defect degree at least two, and an actual generically regular
osculating CI supplies this flag. All embedded triples containing the
fixed ribbon are classified: minimum defects form a \(\mathbf P^1\),
cubic defects satisfy a determinant condition, and every divisor of
degree at least four occurs. Their non-Gorenstein defect points do not
exclude a later Gorenstein thickening. The carrier's first symbol has
degree \(4a-8\) and contains the actual defect divisor. The next gate
is therefore a higher embedded flag and its actual source fixed surfaces,
not another unrestricted defect-placement test. The fixed quotient's
algebra extends to odd characteristic; in characteristic three its plane
family is no longer singled out by osculation.

The [quadric-flag character formula](../../arguments/torus/equation_pair_rank_and_weights.md#characters-of-all-double-surface-equation-spaces)
computes every weight of the actual degree-\(d\) equations vanishing to
second order along \(C\). For \(d\ge5\) this source character is unchanged
in characteristic two, even though the conormal bundle's splitting changes.
The proof uses the flag and its induced linearizations, rather than
transporting the characteristic-zero splitting. This identifies an actual
source-space comparison across characteristics; it does not identify
higher-jet maps or transport a characteristic-zero STCI obstruction.

[From symbols to actual equations](from_symbols_to_equations.md) follows the
first saturated relation, the next quotient relation, and the remaining
global source condition. [Normal filtration boundaries](normal_filtration_boundaries.md)
explains why taking the full initial ideal and identifying the associated
graded equation module are separate operations. The
[open comparisons](open_normal_geometry.md) give exact local and global
questions, including the punctual relative defect and the length-five stratum.
The [arithmetic framework](../arithmetic-supported-lifts/index.md) gives a
flat projective family where normal associated-graded base change fails.
The [residual construction framework](../residual-construction/index.md)
compares marked deformations and cycle transfer; a map from the full normal
cone to its marked incidence problem is still needed.


### From normal symbols to global equations

- [Generic normal forms and saturation of relations](generic_normal_forms_and_relation_saturation.md)
- [Actual equation modules and complete-intersection bridges](actual_equation_module_and_ci_bridge.md)
- [Thickening hierarchy, jet budgets, and socle movement](thickening_hierarchy_and_jet_budgets.md)
- [Characteristic-two tests and sextic lifting](characteristic_two_and_sextic_lifts.md)
- [Embedded one-step lifts and arithmetic boundaries](embedded_one_step_lifts_and_arithmetic_boundaries.md)

The first saturated normal relation, subsequent quotient relations, actual homogeneous equation sources, and embedded arithmetic lifting are distinct requirements. The [original section addresses](from_symbols_to_equations.md) remain navigable.


### Normal filtrations and exceptional boundaries

- [Normal neighborhoods and boundary repair mechanisms](normal_neighborhoods_and_boundary_repairs.md)
- [Filtered equation modules and sextic source obstructions](filtered_equation_module_and_sextic_obstruction.md)
- [Quartic ancestor restrictions and endpoint exclusions](quartic_ancestor_and_endpoint_exclusions.md)
- [Mixed-degree Fitting strata and thickening realization](mixed_degree_fitting_and_realization.md)
- [Socle budgets, source modules, and arithmetic comparisons](socle_budgets_and_arithmetic_comparisons.md)
- [Filtration calculations and exact computational sources](filtration_computational_sources.md)

These developments distinguish successive neighborhoods, the full filtered equation module, fixed ancestor and endpoint restrictions, and actual global realization. [Original section addresses](normal_filtration_boundaries.md) remain available.

### Actual source coverage on the equality boundary

The [marked correspondence](../../arguments/residuals/blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary)
now covers both endpoint and interior slopes on the equality boundary
and reduces the test to irreducible factors. The conic resultant tests
common normal roots but not the absence of a contracted marked ruling
or the off-conic intersection. The next missing input is a bound on
what the actual source sections can realize there, or a realizing pair.
This does not cover positive direction degree.
