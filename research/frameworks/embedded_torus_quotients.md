---
id: STCI-F-0002
type: framework
title: Embedded torus quotients and projective endpoint descent
status: in_use
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0051, STCI-R-0052, STCI-R-0053, STCI-R-0056]
    to: [STCI-F-0002]
    at: "#available-results"
  - kind: limits
    from: [STCI-R-0054]
    to: [STCI-F-0002]
    at: "#embedded-controls"
---
# Embedded torus quotients and projective endpoint descent

## Scope

Work over an algebraically closed field and the fixed quartic torus action.
On the dense coordinate torus use
\(x=(1,t,t^3u,t^4v)\). A finite *embedded* quotient
\(B=k[u^{\pm1},v^{\pm1}]/K\), of length \(0<n<\infty\), determines a constant
family of orbit closures and its projective scheme image. The full maps from
the Laurent ring are data: an abstract isomorphism class of Artin algebras
does not determine this image. Keep every characteristic restriction of an
example or descent assertion.

This strategy gives exact tests and counterexamples for specified images.
Extending it to moving transverse quotients requires additional geometry. The
new Result records remain provisional, even when their reconstructions have
independent acceptance.

## Available results

[R-0051](../results/constant_embedded_orbit_image.md) constructs the finite
image and its pure Cohen–Macaulay structure.
[R-0052](../results/orbit_image_endpoint_polynomial.md) measures its two
endpoint image lattices and gives
\[
P_{Z_B}(d)=4nd+n-\delta_0-\delta_\infty.
\]
[R-0053](../results/constant_quotient_equation_criterion.md) uses the actual
homogeneous equation spaces: a degree-\((a,b)\) realization requires a
gcd-one pair in those spaces and degree exhaustion \(ab=4n\).
[R-0056](../results/pure_curve_degree_exhaustion.md) supplies the separate
purity argument that turns inclusion and degree exhaustion into scheme
equality. Equal degrees of unrelated schemes would supply no such conclusion.
The [complete quotient argument](../arguments/torus_embedded_quotients.md)
retains the construction, proofs, examples, and characteristic comparisons.

## Embedded controls

[R-0054](../results/embedded_quotient_endpoint_counterexamples.md) preserves
distinct embeddings with isomorphic abstract algebra and their different
endpoint images, including characteristic-dependent behavior and non-Gorenstein
local structure. Defect lengths alone do not determine the full gluing algebra.
[R-0055](../results/flat_collision_of_orbit_images.md) gives a controlled
collision with verified relative image lattices; constancy of one numerical
defect is not its flatness proof.

The positive-characteristic prescribed quartic control
[R-0021](../results/quartic_mu4_degeneration.md) retains its own canonical
scope. Its characteristic-two sole support is not a characteristic-zero
supported deformation. Neither an abstract quotient nor its reduced support
provides actual global equations after projective contraction.

## Bridges

The [comparison investigation](../investigations/quotient-hilbert-comparison/index.md)
connects this lens to [full supported Hilbert boundaries](torus_supported_boundaries.md).
A hypothetical characteristic-zero supported CI need not have a constant
embedded quotient; the whole moving finite modification is the relevant
comparison object. The existing
[finite-modification proof](../synthesis/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification)
and [strict-movement argument](../synthesis/tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier)
remain reviewed provisional sources outside the reconstructed constant-family
proof closure. Their endpoint budget is a constraint on one moving object,
not a formula for the difference of its two Hilbert limits.

Useful next work would identify an actual specialization map for embedded
quotients, endpoint lattices, and equation modules. A numerical resemblance
between defects does not supply this map. Any finite prescribed-degree test
must retain the actual source image and establish properness.

## Research decisions

Use constant quotients for explicit constructions, tests, and counterexamples
where the embedded data and endpoint contraction can be computed. Move to a
declared nonconstant family when the construction needs movement. Do not impose
curvilinearity or a fixed abstract quotient type without a coverage argument.
The [finite controls](../investigations/torus-residual-controls/index.md) can
detect arithmetic errors; their successful execution does not establish
unexamined image descent or projective realization.
