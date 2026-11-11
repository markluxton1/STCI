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
Extending it to moving transverse quotients requires additional geometry. The reconstruction reviews accept the exact scopes stated in the Result records.

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
[R-0021](../results/quartic_mu4_degeneration.md) retains its own stated
scope. Its flat integral model has three residual quartics on the geometric
generic fiber. The [normal filtration calculation](../results/quartic_normal_initial_base_change.md)
exhibits failure of associated-graded base change, a different operation from
base change of the projective image. The [finite specialization checks](../investigations/quartic-specialization-controls/index.md)
replay identities for this pair and the fixed quartic's degree-four symbols.
Actual equation recovery after projective contraction still requires the
embedded quotient and the homogeneous source test.

## Bridges

The [comparison investigation](../investigations/quotient-hilbert-comparison/index.md)
connects this lens to [full supported Hilbert boundaries](torus_supported_boundaries.md).
For a proper degree-\((a,b)\) pair with sole reduced support \(C_0\), the
investigation points to the separate finite-modification and strict-movement
proofs. In characteristic zero or characteristic \(p>0\) with \(p\nmid ab\),
the embedded quotient has positive degree. Its endpoint budget constrains
one moving object. [R-0070](../results/intrinsic_limits_endpoint_fibers.md)
determines the pure parts of both intrinsic limits and their two embedded
lengths from the corresponding endpoint fibers. The full opposite-endpoint
algebras and moving generator incidence remain open.

Use the relative image map in R-0070 when comparing an embedded quotient
and an intrinsic limit. Recovering the full special equation module
requires further data. Any finite prescribed-degree test must retain
the actual source image and establish properness.

## Research decisions

Use constant quotients for explicit constructions, tests, and counterexamples
where the embedded data and endpoint contraction can be computed. Move to a
declared nonconstant family when the construction needs movement. Do not impose
curvilinearity or a fixed abstract quotient type without a coverage argument.
The [finite controls](../investigations/torus-residual-controls/index.md) can
detect arithmetic errors; their successful execution does not establish
unexamined image descent or projective realization.
