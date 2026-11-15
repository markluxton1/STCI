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
- [Integral equation incidence](../../arguments/arithmetic/arithmetic_root_collision.md#the-full-simultaneous-equation-incidence)
  and [effective degree transfer](../../arguments/arithmetic/effective_characteristic_transfer.md)
  address the separate question of varying the equation pairs. A prescribed
  lift obstruction has no coverage over those pairs.

## Bridges

For one prescribed powered source, compare the actual specialization kernel
with the corresponding annihilator, linkage, or duality data. A conductor
approach needs a map to or from the full conductor for a specified normalized
carrier and a check that the map retains the endpoint algebra. A comparison
that supplies only the genus identity leaves the compatibility open.

## Bounded work and selection

No activity has been selected here. A bounded test should fix a powered source
and the target algebra or sheaf, then stop at a proved comparison, a control
invalidating it on its declared domain, or the first missing map or descent
condition. A positive compatibility result gives a test on that source. An
obstruction closes only the covered traits. Revise the approach when the
comparison requires changing its carrier or its source. Retire the strategy
for a source once its supported lifting question is decided under the stated
trait hypotheses.

## Comparisons with other approaches

The [prescribed flat family](../../results/quartic_mu4_degeneration.md) is a
control for [embedded torus quotient descent](../embedded-torus-quotients/index.md).
At the two endpoints the full embedded fiber is needed; in characteristic two
the new order-four relation in the [normal initial ideal](../../results/quartic_normal_initial_base_change.md)
appears only after reduction. This is also a control for
[formal normal geometry](../formal-normal-geometry/index.md). The lower-root
specialization defect, the spectral Picard class, and the Weil class of a
normalized carrier belong to different objects. A bridge would have to produce
an actual comparison map with its specialization hypotheses.

The shared [positive-characteristic references](../../literature/README.md#positive-characteristic)
distinguish the quartic constructions from affine theorems and from
hypotheses needed for degree transfer.
