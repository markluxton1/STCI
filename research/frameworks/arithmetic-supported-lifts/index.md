---
id: STCI-F-0004
type: framework
title: Arithmetic realization, descent, and supported lifts
status: proposed
scope: "#scope"
bridges: "#bridges"
---
# Arithmetic realization, descent, and supported lifts

## Scope

For the fixed rational quartic, arithmetic geometry connects three distinct
questions: how actual equation degrees vary with the characteristic, how
powers descend through a specified nonnormal carrier, and which special
pairs lie on supported mixed-characteristic traits. The first question has
unrestricted quantifiers: characteristic-zero nonexistence is equivalent
to divergence of the minimum larger defining degree \(\delta(p)\) as
\(p\to\infty\). The known sharp minima and nonlifting theorems cover
specified sources, rather than that full minimum.

Finite Witt lifts, lifts with a strong uniform nilpotence containment,
and actual supported traits retain different hypotheses. The
[root-specialization theorem](../../arguments/arithmetic/frobenius_power_lifting_precision.md#root-specialization-and-the-remaining-endpoint-defects)
concerns the prescribed powered-quartic source and actual traits.

## Available mathematics and controls

- [Integral equation incidence](../../arguments/arithmetic/arithmetic_equations_and_jet_gaps.md#the-full-simultaneous-equation-incidence)
  and [effective degree transfer](../../arguments/arithmetic/effective_characteristic_transfer.md)
  treat all actual pairs at fixed degrees. They make the characteristic
  limit precise without assuming a lifting theorem for chosen special pairs.
- The [explicit equations](../../arguments/arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-a-quartic-carrier)
  give sources in every positive characteristic. On the fixed cuspidal
  quartic, all mate degrees are controlled by the exact semigroup condition
  \(p^{v_p(N)}\in\langle3,4\rangle\). The
  [conductor-unit quotient](../../arguments/torus/fixed_carrier_chow_arrangements.md#the-conductor-unit-quotient-behind-the-characteristic-dependence)
  explains why the additive first moment retains only its first gluing jet.
- The [integral first-jet product](../../results/integral_first_jet_lifting.md)
  gives \(ab/2\in L_F L_G\) on any actual supported trait avoiding the
  fixed projection center. This is a condition on the two actual equation
  sources, independent of special-fiber symmetry. In particular it excludes
  unramified traits through the non-eigen \((16,p)\) points for \(p\ge43\).
- The [prescribed Z/4 embedded nonlift](../../results/prescribed_z4_arithmetic_nonlifting.md#statement-and-hypotheses)
  tests a separate fixed lower neighborhood. [Prime-to-p extraction](../../arguments/arithmetic/prime_to_p_power_extraction.md#extraction-theorem)
  and the [strong precision shift](../../arguments/arithmetic/frobenius_power_lifting_precision.md#strong-lifts-and-the-exact-unramified-precision-shift)
  provide different controls on actual traits or finite lifts.
- In the prescribed powered construction for \(p\ge7\), quartic-carrier
  exclusion forces a nonzero finite-length kernel in specialization of the
  lower root. It is supported at the two marked endpoints, and its length
  is the genus deficit in the root theorem.

## Bridges

The first-jet product and root extraction now place source and specialization
conditions on the same hypothetical trait. For the prescribed powered
source, the maximum unramified strong precision is already exactly
\(1+v_p(n)\); any remaining actual trait has \(p\mid n\), ramification
index at least \(p-1\), and a nonzero endpoint root defect. The open issue
is compatibility of the actual equations with that defect at the remaining
ramification, not another finite-precision test of the same presentation.

An annihilator, linkage, or conductor comparison must retain the actual
root-specialization sequence and the two homogeneous source spaces. A genus
identity or a matching length alone does not determine this compatibility.
The finite section/Rao defect of an invariant pure torus hull has a different
definition from the embedded-point kernel of a specialized arithmetic root;
their relation needs the relevant exact sequence, not an identification by
numerical resemblance.

At two, even the source symmetrization must retain its arithmetic object.
The [flat sign-orbit control](../../arguments/arithmetic/arithmetic_sign_orbit_comparison.md)
has a triple-line schematic \(\mu_2\) orbit, although the reduced pointwise
involution sees only its double line. The correction in its split source
presentation is supported along the curve. This connects the actual
sign-source comparison to the existing \(\mu_4\) arithmetic orbit proof;
it supplies no characteristic-two finite Rao or moment-vanishing theorem.

For the full characteristic-limit strategy, an obstruction must cover all
actual degree-bounded pairs, or a proved reduction must place them in a
controlled source. Neither the fixed-carrier unit quotient nor the
first-jet valuation inequality supplies that reduction. The non-eigen
\((16,p)\) source remains an independent arbitrary-ramification question.

## Bounded comparison

The elliptic double-inverse search tested both smooth \(\mathbf F_5\)-rational
quadric parameters at \(i=2\) and all \(5^4\) lift tuples for each.
Every inverse ideal on the off-curve chart was proper over the geometric
fiber, leaving no candidate among these 1,250 tuples. The
characteristic-zero parameter line was decided by an independent
elimination over \(\mathbf Q(i)\). Existence elsewhere in the
characteristic-zero family remains open. [Search scopes and replays](../../investigations/stci-equation-search/index.md#findings)

For a prescribed powered source and target algebra or sheaf, a positive
compatibility result tests only that source; an obstruction excludes only
the traits covered by its hypotheses. Changing the carrier or source
requires a separate comparison map and descent conditions.

## Comparisons with other approaches

The [finite-group-scheme orbit description](../../arguments/arithmetic/frobenius_power_lifting_precision.md#torus-eigenforms-and-the-finite-group-scheme-orbit)
extends the prescribed prime-exponent example to every represented exponent
\(N=3b+4c>0\). In characteristic \(p\), its prime-to-\(p\) factor counts
distinct quartic translates and its \(p\)-part gives their multiplicity.
This relates the explicit arithmetic construction to invariant residual
cycles without asserting that arbitrary residual cycles can be absorbed.
The [complete fixed-quartic arrangement locus](../../arguments/torus/fixed_carrier_chow_arrangements.md)
places this binomial family inside the larger coefficient space
\(c_1=c_2=c_5=0\). Partial collisions occur in characteristic zero, but
at least three distinct translates must remain on that fixed carrier.
Frobenius explains complete collapse in the prescribed family; it does not
classify all arrangements or all characteristic-zero degenerations. In the
same characteristic \(p\ge7\), the actual flat \((4,p)\) family with
polynomial \(T^p+cT^{p-3}-(1+c)\) connects \(p\) distinct reduced translates
to \(p[C_0]\). All ideals remain invariant ACM ideals and all first moments
vanish. Moment vanishing therefore detects neither inseparability nor
branch coalescence by itself.
The [general arrangement moment](../../arguments/torus/chow_arrangement_moments.md)
separates the Chow closure of invariant CI arrangements from complete collision
in characteristic zero. At \(m[C_{u,v}]\), its normalized Chow coefficient
is \(-4m u/v\); the obstruction vanishes when the characteristic divides
\(4m\), consistently with Frobenius collapse, without proving realizability.
For odd characteristic, the additive generalized-Jacobian target is killed
by \(p\), whereas the fixed cusp's unit quotient can retain higher
\(p\)-power information: characteristic five requires 25 even after its
first moment vanishes at five. This height is still carrier-dependent.
The [standard and nonclassical cubic cusp minima](../../arguments/arithmetic/rational_quartics_in_positive_characteristic.md#exact-cuspidal-carrier-minima-p-014-sharp-degree-on-the-cuspidal-cubic-carriers)
in characteristic three are \(N=3\) and \(N=9\), respectively. The latter's
coefficient condition \(c_{3m-1}=m\alpha c_{3m}\) retains the polarized
section frame after Frobenius removes the cross terms. Local additive
torsion alone cannot replace this graded descent condition.
The [root-defect grading](../../arguments/arithmetic/frobenius_power_lifting_precision.md#equivariant-grading-of-the-root-specialization-defect)
requires an equivariant total trait and the original root theorem's
hypotheses. For the fixed quartic a supported mixed-characteristic trait
with trivial torus action on the base cannot have that equivariance:
its characteristic-zero generic fiber would contradict the invariant-CI
exclusion. The [sign-symmetric ACM theorem](../../results/chow_acm_parity_vanishing.md)
also rules out preservation of that weaker ideal symmetry. Thus any
remaining supported lift must break these symmetries;
the invariant special equations do not grade its root defect. In a
setting where the equivariant specialization lemma applies, the endpoint
modules need not have opposite characters or equal lengths. Comparing
them with conductor or torus-limit modules requires an actual compatible map.

The [prescribed flat family](../../results/quartic_mu4_degeneration.md) is a
control for [embedded torus quotient descent](../embedded-torus-quotients/index.md).
At the two endpoints the full embedded fiber is needed; in characteristic two
the new order-four relation in the [normal initial ideal](../../results/quartic_normal_initial_base_change.md)
appears only after reduction. This is also a control for
[formal normal geometry](../formal-normal-geometry/index.md). The lower-root
specialization defect, the spectral Picard class, and the Weil class of a
normalized carrier belong to different objects. In particular, the
finite-flat four-section on the ruled resolution does not identify its
projective scheme image after endpoint base change: the graph-section
contact divisor is \(3p_0+p_\infty\), while distinct characteristic-zero
projective quartic components of the prescribed \(\mu_4\) family have
intersection length three at **each** endpoint. The special fiber's
fourfold Cartier structure and the total-space normalization must likewise
not be replaced by the normalization of its reduced special fiber
([arithmetic four-section proof](../../arguments/arithmetic/arithmetic_four_section_family.md)). A bridge would have to produce
an actual comparison map with its specialization hypotheses.

The shared [positive-characteristic references](../../literature/README.md#positive-characteristic)
distinguish the quartic constructions from affine theorems and from
hypotheses needed for degree transfer.

The [linkage formulas](../../arguments/residuals/layerwise_attachment_and_triples.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component) and [local duality](../../arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers) use characteristic-free canonical module arguments. The explicit [toric semigroup lattice](../../arguments/torus/fixed_carrier_chow_arrangements.md#all-order-primary-structure-and-attachment-on-the-classified-carrier) uses invertible binomial minors in characteristic zero or the indicated large-characteristic range. Do not specialize this basis when the minors vanish.

### A comparison for compatible quadratic-conductor lattices

The [actual endpoint matrix](../../arguments/linkage/endpoint_lattice_capacity.md#arithmetic-control-and-comparison-of-traits) gives a fixed characteristic-three calibration and lower semicontinuity in the direction \(\delta_{\mathrm{special}}\le\delta_{\mathrm{generic}}\). This uses compatible finite free endpoint lattices on a supported trait. It does not identify the conductor with a Frobenius-root endpoint defect or give the opposite inequality needed for an obstruction by specialization.

The [auxiliary-cover choice](../../arguments/linkage/quadratic_cover_choice.md)
is available in every characteristic different from two: extracting the
finite Frobenius height of \(r/q\) retains an odd moving-divisor valuation.
The [unique singular signed cubic and its normalization exclusion](../../arguments/linkage/signed_cubic_normalization_and_cartier_defect.md)
also extend to odd characteristic. These specific deductions do not
extend the characteristic-zero Du Val/K3 exclusions or exact cyclic
determinant capacity. They remain compatible with the known supported
constructions in every positive characteristic.
