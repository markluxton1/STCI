---
id: STCI-F-0006
type: framework
title: Global equation realization for supported intersections
status: proposed
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0076, STCI-R-0077]
    to: [STCI-F-0006]
    at: "#bridges"
---
# Global equation realization for supported intersections

## Scope

For the fixed embedded quartic \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), organize what it takes for two *actual homogeneous forms* to have a prescribed supported intersection. The characteristic-zero STCI question remains open in unrestricted degree. A local multiple structure, normal symbol, cycle, Chow equation, complement pencil, or abstract bundle section retains only part of a global pair. The [global equations account](../../arguments/equations/global_equations_and_constructions.md) gives the geometric mechanisms; the [actual equation-jet filtration](../../arguments/equations/global_equation_jets.md) tracks their source maps.

For a proper pair of degrees \((a,b)\), the cycle identity \(ab=4m_{C_0}+\deg R\) makes \(m_{C_0}=ab/4\) equivalent to sole support. This is an exact existence reformulation, not an independent multiplicity bound. A viable obstruction must supply a structural restriction on **arbitrary actual pairs**, beyond the classical intersection formula or a change of parameter space.

The fundamental object is the labelled map
\(\mathcal O_{\mathbf P^3}(-a)\oplus\mathcal O_{\mathbf P^3}(-b)\to I_{C_0}\)
whose components are the equations. Its image must define a proper complete intersection and have no residual support if the goal is STCI. The [Sylvester Hom identity](../../arguments/equations/chow_bundle_maps.md#the-prescribed-sylvester-bundles-already-retain-the-equations) recovers forms directly from a map of the prescribed bundles; the required nonzero Chow-power determinant is still an existence condition. The [complement calculation](../../arguments/equations/complement_section_obstructions.md) distinguishes the checked continuous and primary algebraic conditions from actual homogeneous section realization. The [Chow/bundle and complement criteria](../../arguments/equations/global_equations_and_constructions.md#geometric-orientation-the-locus-of-globally-presented-multiple-curves) are equivalent formulations or necessary shadows only when their stated hypotheses hold; a cycle identity or a section on the complement does not by itself provide homogeneous lifts with the required base locus.

## Interfaces

[Formal normal geometry](../formal-normal-geometry/index.md) concerns local
compatibility; [carrier normalization](../carrier-normalization/index.md)
requires full inverse support and conductor descent; and
[residual construction](../residual-construction/index.md) tracks residual
cycles. None alone supplies a proper homogeneous pair with sole support.
[Projection and liaison](projection_and_liaison.md) studies supported ACM
sources and section defects.

Two distinct equation questions survive passage to a thickening. The
[radical-power lemma](../../arguments/torus/equivariant_set_theoretic_descent.md)
preserves the least number of set-theoretic homogeneous equations inside
any same-radical ideal, while it gives no bound on their degrees and does
not generate that ideal. For an unequal-degree search, the
[actual pair quotient](../../arguments/torus/equation_pair_rank_and_weights.md)
removes the redundant replacement \(G\mapsto G+HF\). Its bundle dimension
and weight data describe available equations; properness, higher contact
and terminal support remain conditions on those equations.

## Available mathematics and controls

The [full Chow-polytope rigidity theorem](../../arguments/equations/chow_polytope_rigidity.md) classifies effective one-cycles whose full, unshifted column-weight polytope equals a multiple of that of the fixed quartic, in every characteristic: they are sums of diagonal translates of the quartic. This controls cycle support types only. It neither forces those translates to coincide nor constructs a scheme or a pair with the prescribed Sylvester determinant.

- Restriction of an actual orbit presentation to the two completed endpoints preserves the parameter-annihilation order of each homogeneous torsion class. A class can nevertheless become divisible by the parameter there. This explains how endpoint computations can miss global equation relations even with the correct degree and parameter. [Endpoint detection and its first-layer kernel](../../results/endpoint_equation_torsion.md).
- For a characteristic-zero sole-support pair of degrees \(a\le b\), every nonzero weight component of the smaller equation has surviving powers through \(\lfloor b/a\rfloor\). Their multiplication ranks bound the splitting of the moving quotient. This tests the degrees of actual homogeneous generators even when a proposed image has the prescribed CI polynomial. [Power and splitting bounds](../../results/torus_quotient_movement_bounds.md#proof).
- Actual source spaces at fixed degree and normal order and their successive lifting quotients are computed in [global equation jets](../../arguments/equations/global_equation_jets.md). They show why independently selected sections of \(\mathrm{Sym}^r(I/I^2)\) need not come from equations. Finite compatible-jet existence is not an effective bound on all degrees: no general all-degree cutoff is established from a rank plateau or a finite truncation.
- The [octic/root comparison](../../arguments/spectral/actual_octic_root_lift_comparison.md) has an actual source map and a proper pair of transverse length eight with residual degree 32. This illustrates compatibility without sole support, not a solution to the unrestricted question.
- [Projected thickenings](../../arguments/linkage/projected_thickening_section_defects.md) distinguish an ACM source upstairs from its image in \(\mathbf P^3\): the displayed power and binary-mixture images fail ACM when the positive degree product is nonzero. This does not exclude other projected sources or arbitrary supported thickenings.

## Bridges

For degrees \((3p,4q)\) and exact normal orders \((p,q)\), connectedness
reduces the characteristic-zero equation question to either of two
marked rational quintics on \(V_5\). A proper pair of divisors of
classes \(pM,2qM\) must have the prescribed conic orders, meet on the
chosen quintic alone, and retain a nonzero order-\(q\) symbol at its
one conic contact. These conditions, with the exact-order hypotheses
in the proof, also recover a defining pair in \(\mathbf P^3\).
[Section and conic-fiber criterion](../../arguments/residuals/blowup_residual_geometry.md#actual-equations-on-the-zero-direction-edge).

For the explicit elliptic double-cover family, a candidate consists of
a smooth basepoint-free fiber mapping birationally onto an octic.
First, its length-twelve residual zero scheme must be supported on the
marked elliptic curve. Then, for some \(b>0\), one must express
\(Q_0^b\) as a degree-\(b\) polynomial in the four projection sections
in the coordinate ring of that fiber. The polynomial and the implicit
octic would cut out the fixed quartic set-theoretically. The completed
characteristic-zero line fails at the support step. [Support theorem](../../results/elliptic_inverse_support.md) ·
[Descent equation (8)](../../arguments/carriers/elliptic_double_inverse_construction.md#5-fiberwise-support-and-actual-descending-equations) ·
[Tested line](../../investigations/stci-equation-search/index.md#findings)

The unresolved implication is from compatible local/normalized data to two homogeneous sections whose full intersection is supported exactly on \(C_0\). A viable bridge must identify the actual source spaces, lift every required jet through their quotient maps, handle base points and conductor gluing, and then prove properness and eliminate residual components. Conversely, a universal obstruction must cover all equation degrees; the existing fixed-degree calculations and actual jets do not supply an effective all-degree bound.

For witness bounds and fixed-degree tests, see [exact finite certificates](../../arguments/equations/bounded_equation_certificates.md). A separate question asks how an actual equation obstruction changes as the [embedding varies](bounded_equation_search.md). Use [projection and liaison](projection_and_liaison.md) for the companion construction interface. The shared literature records the hypotheses for
[Chow and determinantal representations](../../literature/README.md#chow-forms-and-global-determinant-representations)
and for [affine results and the projective gap](../../literature/README.md#affine-lci-theorems-and-the-projective-gap).

The canonical [R-0074](../../results/chow_polytope_rigidity.md) classifies **all** effective cycles in this rigid Chow-polytope fiber; invariance is deduced, not assumed. Its [proper-pair reformulation](../../arguments/equations/chow_polytope_rigidity.md#proper-surface-pairs-and-the-remaining-equation-question) is a classical resultant coefficient condition, not a criterion in the Newton polytopes of the equations alone. The [R-0050 integration](../../arguments/equations/chow_polytope_rigidity.md#eigenpairs-and-transverse-finite-quotients) keeps boundary exclusion and binomial-only subgroup structure explicit.

The [H16 cycle parameterization](../../arguments/equations/chow_polytope_rigidity.md#set-level-symmetric-power-fiber-h16) is set-theoretic and supplies neither homogeneous equations nor scheme structure. The [proof-dependency inventory](../../investigations/proof-audit/README.md) separates essential computations from evidence, and records the geometric R-0024 rank replacement.

[H17](../../arguments/torus/boundary_reconstruction_and_defects.md) gives a linear obstruction and torsor for lifting labeled boundary equations through C, a separate torus-support defect, and bounded-degree embedded CI reconstruction. Compatibility of lifts is not sole-support realization; the finite-order counterexample does not apply to all marked filtrations or fixed-degree full formal data.

The [H17 fixed-degree realization criterion](../../arguments/torus/boundary_reconstruction_and_defects.md#exact-fixed-degree-realization-of-embedded-facet-schemes) reduces a specified compatible embedded facet diagram to finite homogeneous polynomial feasibility using an ordinary power of I_C. It is an exact criterion, not a proof of automatic existence or an efficient all-degree search.

The [translate and fixed-surface interface](../../arguments/torus/fixed_surface_restriction_lifts.md)
expresses containment by arbitrary forms as coefficient evaluation at the
chosen \((u,v)\), with joint transverse lengths retaining multiplicities.
Restricted syzygies recover the abstract first annihilator of the surface
equation; its embedded normal extensions remain necessary. On the toric
quartic, a hypothetical characteristic-zero sole-support \(C_0\) pair of degrees \(a\le b\)
can contain a power \(A^N\) only with \(4N>b\). No upper bound meeting
that threshold, or automatic extension of scalar semigroup descent to
the relation module, is established.

### What the equality-boundary correspondence leaves to realization

The [actual marked section spaces](../../arguments/residuals/blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary)
on (V_5) give a fixed geometric incidence question in each allowed
bidegree. An appropriate conic resultant is necessary but does not
realize a proper pair: the common support off the conic and absence
of a whole marked fiber must still be tested in the *same* section
spaces. Neither a formal contact lift nor a separate choice of
boundary data supplies that pair. An endpoint and an interior slope
are distinct tests; a result on either should say which realization
condition it actually decides.
