---
id: STCI-F-0004
type: framework
title: Arithmetic lifting of prescribed supported intersections
status: proposed
scope: "#scope"
bridges: "#bridges"
---
# Arithmetic lifting of prescribed supported intersections

## Scope

For the fixed rational quartic, study which prescribed positive-characteristic
equation pairs can occur as special fibers of supported mixed-characteristic
traits. Keep finite Witt lifts, lifts satisfying a strong nilpotence condition,
and actual supported traits under their respective hypotheses. The open
endpoint test below concerns the powered quartic construction and actual
traits in the [root specialization theorem](../../arguments/arithmetic/frobenius_power_lifting_precision.md#root-specialization-and-the-remaining-endpoint-defects).

## Available mathematics and controls

- The [explicit equations](../../arguments/arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-a-quartic-carrier)
  give sources in every positive characteristic. In the prescribed powered
  construction for \(p\ge7\),
  the lower root closure in the theorem has a special fiber mapping to the
  unpowered intersection, with a finite-length kernel. Quartic-carrier
  exclusion forces this kernel to be nonzero with support contained in the
  two marked endpoints. Its length is the genus deficit in the theorem.
- The [prescribed Z/4 embedded nonlift](../../results/prescribed_z4_arithmetic_nonlifting.md#statement-and-hypotheses)
  tests a separate fixed lower neighborhood. [Prime-to-p extraction](../../arguments/arithmetic/prime_to_p_power_extraction.md#extraction-theorem)
  and the [strong precision shift](../../arguments/arithmetic/frobenius_power_lifting_precision.md#strong-lifts-and-the-exact-unramified-precision-shift)
  provide different controls on actual traits or finite lifts.
- [Integral equation incidence](../../arguments/arithmetic/arithmetic_equations_and_jet_gaps.md#the-full-simultaneous-equation-incidence)
  and [effective degree transfer](../../arguments/arithmetic/effective_characteristic_transfer.md)
  address the separate question of varying the equation pairs. A prescribed
  lift obstruction has no coverage over those pairs.

## Bridges

For one prescribed powered source, compare the actual specialization kernel
with the corresponding annihilator, linkage, or duality data. A conductor
approach needs a map to or from the full conductor for a specified normalized
carrier and a check that the map retains the endpoint algebra. A comparison
that supplies only the genus identity leaves the compatibility open.

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
