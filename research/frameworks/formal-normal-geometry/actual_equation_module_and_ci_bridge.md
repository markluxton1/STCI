# Actual equation modules and complete-intersection bridges

[Formal normal Framework](index.md) · [Original section addresses](from_symbols_to_equations.md)

## 3.4 Why the Picard criterion is not enough

The Picard condition on a full root scheme is a statement about **abstract graded relations**; it does not ensure that the relation lifts through the nonlinear formal neighborhoods or to global equations. Under balanced-normal hypotheses, [R-0005](../../results/smooth_root_formal_obstruction.md) excludes compatible all-order embedded Cartier lifting of a smooth movement-two root of class \((2,r)\), \(r\ge2\). It does not exclude finite lifting, singular or nonreduced roots, or other classes. [R-0007](../../results/quadratic_root_obstruction_model.md) gives the first two ambient tests and a smooth torsion seed that passes the first but fails the second; its full second zero locus remains unknown.

A further distinction concerns the **actual equation module**: cancellation can create full-initial-ideal generators beyond the displayed normal symbols, and the associated graded of \(J/IJ\) need not equal the minimal initial-generator module. [R-0030](../../results/local_filtration_comparison_defect.md) identifies the comparison kernel and its support; nonzero defect for a proper sole-support pair remains unresolved. Consequently, neither a graded second relation nor a finite formal lift is by itself a global STCI construction.

## 3.5 The actual complete-intersection bridge

[R-0006](../../results/actual_ci_smooth_root_bridge.md) starts from an **actual** sole-support complete intersection whose two displayed equations both have order \(r\), whose degree-\(r\) relation is saturated and everywhere jointly generated, and whose **full** generic initial ideal is \((f_r,g_s)\) with coprime generators, \(s>r\), gap \(\ell=s-r\ge2\), and a smooth full Cartier root. The strict-transform intersection is then locally a primitive \(\ell\)-fold structure \((h,u^\ell)\), yielding compatible finite embedded Cartier lifts through orders below \(\ell\). Combined with [R-0005](../../results/smooth_root_formal_obstruction.md), this gives a conditional finite-gap obstruction, not a universal degree bound. Here \(s\) is the order of the second generator of the **full initial ideal**, not necessarily the original order of the second displayed equation.

## 3.6 Moving pure powers and degeneration

[R-0009](../../results/moving_purepower_boundary.md) proves, in characteristic zero, that a saturated first relation equal to the \(r\)-th power of a moving normal direction (\(r\ge2\)) cannot admit an everywhere-coprime next graded relation: its evaluation divisor has degree at least \((r-1)\varepsilon\) for direction-map degree \(\varepsilon>0\). Finite first-relation lifting may nevertheless persist. This forces a **degeneration divisor** under the stated assumptions, not universal failure of actual complete intersections; nonsaturation, noncoprimality, special-point defects, or a different full initial ideal remain outside that conclusion.

## 3.7 The other multiple-structure calculations

The [order-one](../../results/order_one.md) and [jet geometry](../../results/jet_geometry.md) analyses study how ambient sections lift through successive thickenings and how the restriction maps can fall short. When both normal orders are at least two, the [entirely-thick numerical restrictions](../../results/entirely_thick.md) use the exceptional cycle of a proper sole-support pair with balanced normal bundle. The historical quartic-carrier cases are covered by [STCI-R-0001](../../results/quartic_carrier_exclusion.md).


The [finite marked-index equation gate](../../arguments/residuals/marked_line_local_geometry.md#finite-index-rigidity-of-higher-marked-jets)
makes one formerly scalar boundary condition into an
actual multiplication-closure test on \(q+h\)
border products of a local image algebra.
The first nontrivial jet forbids \(xv^i\),
\(2\le i<q\), in the smooth marked graph
model, modulo the permitted linear \(xv\)
coordinate correction. This is not the same
as the intrinsic relation-lifting obstruction:
it presupposes a genuine finite map of the
actual strict and image CIs, and still needs
a homogeneous section lift.

## 3.8 The unresolved interface

The missing theorem would give checkable hypotheses under which an actual pair's common-direction scheme determines a saturated global root relation and a controlled second quotient relation, including special-point defects. The distinctions between generic factors, global saturation, full initial ideals, fiberwise coprimality and embedded lifting remain essential.

The valuation and specialization program is maintained in [Formal normal geometry](../../arguments/normal-geometry/formal-normal-intersection.md); residual detection in [Residual intersections and jets](../residual-construction/residual_geometry.md); and punctual comparison defects and boundary lifting in [Normal-filtration defects](normal_filtration_boundaries.md). The root-source implications described here remain open. For a different actual-pair interface, the [full-primary attachment quotient](../../arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers) now has a local-cohomological dual, and [attachment duality](../../arguments/residuals/layerwise_attachment_and_triples.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component) measures complementary-layer failure. Neither identifies the intrinsic comparison module R-0030 with that quotient without a further theorem.

