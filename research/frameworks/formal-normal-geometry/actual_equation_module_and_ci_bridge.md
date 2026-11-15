# Actual equation modules and complete-intersection bridges

[Formal normal Framework](index.md) · [Original section addresses](from_symbols_to_equations.md)

## 3.4 Why the Picard criterion is not enough

The conormal graded algebra is only the first approximation to the actual infinitesimal neighborhoods. Lifting a root relation requires correcting its equation successively so that it remains compatible with the nonlinear transition functions of the ambient blowup.

[STCI-R-0005](../../results/smooth_root_formal_obstruction.md) proves that, under its balanced-normal-bundle assumptions, a **smooth movement-two root** of class \((2,r)\), \(r\ge2\), has no compatible embedded Cartier lift through *all* exceptional neighborhoods. This does not rule out finite lifts, singular roots, nonreduced roots, or other root classes.

[STCI-R-0007](../../results/quadratic_root_obstruction_model.md) makes the first two ambient stages explicit in a quadratic movement-two family for the fixed quartic: a first rank-incidence test and a second test expressed by 25 scalar pairings. An explicit smooth spectral-torsion seed passes first compatibility but fails the second ambient test. Thus **spectral torsion does not imply embedded liftability**. The full second zero locus remains uncomputed.

The distinction is:
\[
\text{graded second relation}\quad\not\Rightarrow\quad
\text{embedded formal lift}\quad\not\Rightarrow\quad
\text{global STCI pair}.
\]
These arrows express missing implications, not new nonexistence theorems.

### Initial generators versus the actual equation module

The full initial ideal of an actual pair may have cancellation-generated generators beyond the two first normal forms. Its minimal graded generator module can also differ from the associated graded of the actual equation module J/IJ. The canonical comparison and its kernel are established in [R-0030](../../results/local_filtration_comparison_defect.md), with a concrete local example in [the filtration synthesis](normal_filtration_boundaries.md#from-exceptional-normal-divisors-to-the-full-filtered-equation-module).

The comparison defect is supported where both carrier surfaces are singular along C. Whether it can be nonzero for a proper pair with sole reduced support C is unresolved. This distinction does not remove the actual-generator hypotheses of the complete-intersection bridge below.


## 3.5 The actual complete-intersection bridge

[STCI-R-0006](../../results/actual_ci_smooth_root_bridge.md) provides a precise, restrictive passage **from an actual complete intersection back to a controlled root thickening**. Its hypotheses include:

1. An actual complete intersection with reduced support \(C\).
2. A saturated degree-\(r\) first relation, generated **everywhere** by the degree-\(r\) symbols of the two actual equations; both have generic order \(r\).
3. Full generic initial ideal \((f_r,g_s)\), with coprime generators and \(s>r\), gap \(\ell=s-r\ge2\).
4. A **smooth full Cartier root**, not merely a smooth reduction.

Then the intersection of the strict transforms is locally a primitive \(\ell\)-fold structure \((h,u^\ell)\) on the full root and yields compatible finite embedded Cartier lifts through orders below \(\ell\). Combining this bridge with STCI-R-0005 gives a **conditional finite-gap obstruction**, not an explicit universal degree bound.

Notice the indexing subtlety: the two original equations in the bridge have order \(r\), while the independent second generator of the **full initial ideal** has degree \(s\). One must not confuse this \(s\) with the original order of the second equation in Chapter 2.


## 3.6 Moving pure powers and degeneration

[STCI-R-0009](../../results/moving_purepower_boundary.md) treats a saturated first relation that is the \(r\)-th power of a moving normal direction, \(r\ge2\), in characteristic zero. Finite first-relation lifting can persist, but an everywhere-coprime next graded relation cannot: its evaluation divisor has degree at least \((r-1)\varepsilon\), where \(\varepsilon>0\) is the direction-map degree.

This produces a **necessary degeneration divisor**, not a contradiction to every actual complete intersection. A genuine STCI presentation could lie outside the theorem through special-point degeneration, noncoprime relations, nonsaturation, or a different full initial ideal.


## 3.7 The other multiple-structure calculations

The [order-one](../../results/order_one.md) and [jet geometry](../../results/jet_geometry.md) analyses study how ambient sections lift through successive thickenings and how the restriction maps can fall short. When both normal orders are at least two, the [entirely-thick numerical restrictions](../../results/entirely_thick.md) use the exceptional cycle of a proper sole-support pair with balanced normal bundle. The historical quartic-carrier cases are covered by [STCI-R-0001](../../results/quartic_carrier_exclusion.md).


## 3.8 The unresolved interface

The missing theorem would give checkable hypotheses under which an actual pair's common-direction scheme determines a saturated global root relation and a controlled second quotient relation, including special-point defects. The distinctions between generic factors, global saturation, full initial ideals, fiberwise coprimality and embedded lifting remain essential.

The valuation and specialization program is maintained in [Formal normal geometry](../../arguments/normal-geometry/formal-normal-intersection.md); residual detection in [Residual intersections and jets](../residual-construction/residual_geometry.md); and punctual comparison defects and boundary lifting in [Normal-filtration defects](normal_filtration_boundaries.md). None of these interfaces is a proved general implication.

