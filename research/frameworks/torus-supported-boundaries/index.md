---
id: STCI-F-0001
type: framework
title: Full torus boundaries and equations of moving supported ideals
status: in_use
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0037, STCI-R-0039, STCI-R-0040]
    to: [STCI-F-0001]
    at: "#available-results"
  - kind: limits
    from: [STCI-R-0043, STCI-R-0046]
    to: [STCI-F-0001]
    at: "#controls"
---
# Full torus boundaries and equations of moving supported ideals

## Scope

Fix an algebraically closed field, the embedded quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), and its torus of integer
weights \((0,1,3,4)\). For a bounded test fix ordinary degrees \((a,b)\),
the complete-intersection polynomial
\(P_{a,b}(n)=abn+ab(4-a-b)/2\), and an integer \(N>0\).
The closed incidence \(H_N\) consists of ideal sheaves with
\(\mathcal I_C^N\subset\mathcal J\subset\mathcal I_C\) and this polynomial.
The characteristic is part of each application; the geometric boundary and
generator criteria work in every characteristic, while the invariant-CI
obstruction has a different characteristic boundary.

The boundary results constrain actual supported intersections but do not
resolve unrestricted STCI.

## Available results

[R-0037](../../results/supported_hilbert_full_limits.md) supplies both full torus
limits in the same supported incidence, retaining the Hilbert polynomial and
the full limit schemes, including any embedded structure. Its exponent bound
is individual, not uniform.
[R-0038](../../results/torus_eigenvector_generator_lifting.md) lifts minimal
generators only when the whole homogeneous ideal is invariant.
[R-0040](../../results/invariant_supported_ci_exclusion.md) applies the trace
obstruction to such an invariant CI: characteristic zero excludes it, and in
characteristic \(p>0\) the degree product must be divisible by \(p\).
Invariance of the radical alone supplies no eigenform presentation.

The complete [Hilbert-boundary argument](../../arguments/torus_hilbert_boundary.md)
explains why the useful object is the whole fixed boundary ideal, with its
possible additional generators. The equation condition belongs on the moving
ideal. [R-0039](../../results/moving_ideal_generator_criterion.md) tests its entire
minimal-generator module \(J/S_+J\). A finite multiplication-map test requires
an actual regularity bound on the declared family.

## Directional loci

For a fixed ideal \(J_0\), let \(A_+(J_0)\) and \(A_-(J_0)\) mean the
sets of points whose full limits at zero and infinity are respectively
\(J_0\). For a pair of fixed ideals, study
\(A_+(J_+)\cap A_-(J_-)\). These are definitions of organizing sets.
The orbit extension in [A-0001](../../arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits)
puts both limits in the same connected component of \(H_N\) as the moving
ideal. Common Hilbert data and connected component are necessary for a pair.
Realizability requires a single ideal in the intersection, even if both
one-sided sets are nonempty. The opposite limits can have different normal
and endpoint structures. Fixed components may have positive dimension, so
one can also ask for incidence over pairs of fixed components. Finiteness,
local closedness, smoothness, and exhaustive coverage remain open here.

## Controls

[R-0043](../../results/sextic_eigenpair_quotient_bound.md) bounds proper sextic
eigenpairs, not arbitrary mixed-weight pairs. In
[R-0046](../../results/sextic_three_generator_full_limit.md), a proper sextic CI
has a full saturated ACM limit requiring generators of degrees \(6,6,10\).
Both fibers have residual degree 32 and generic multiplicity one on \(C\).
Their polynomial is \(36n-144\), but they are outside every sole-supported
\(H_N\). They test full-ideal bookkeeping, not supported-CI nonemptiness.

The Hilbert-limit scheme, the two extreme equation forms, the normal-cone
initial ideal, and the fundamental cycle are different objects. Keeping only
a cycle or a pure hull can discard data necessary for deformation. Likewise,
following individual points in a residual divisor does not compute its flat
divisor limit; [R-0048](../../results/moving_sextic_residual_limit.md) supplies a
concrete control. [R-0049](../../results/sextic_residual_absorption.md) transfers
some residual multiplicity to \(C\) while retaining a residual line; it does
not prove that transfer can be iterated to sole support.

## Bridges

The [supported generator investigation](../../investigations/supported-generator-incidence/index.md)
asks for an actual specified supported family and its two-generator locus.
The [quotient comparison investigation](../../investigations/quotient-hilbert-comparison/index.md)
asks which transverse and endpoint data specialize through an actual map.
Both must preserve the full embedded object.
Its [endpoint comparison](../../results/intrinsic_limits_endpoint_fibers.md)
now gives the pure limit and embedded lengths. Use the
[sextic endpoint conditions](../../arguments/torus_hilbert_boundary.md#necessary-endpoint-conditions-for-a-sextic-pair)
before assigning a curvilinear or noncurvilinear endpoint fiber to a
proposed sole-support family.

A construction must verify support, polynomial, and actual homogeneous ideal
generation. An obstruction must cover its declared family. Extending it to all
supported pairs of a fixed degree requires coverage of the relevant fixed
limits and power bounds; extending it to all degrees is a further problem.
Finding an arbitrary supported flat deformation to a CI is already useful;
realizing a prescribed torus boundary as an orbit limit is a stronger task.

## Cycle incidence versus actual equations

For a proper pair of degrees \((a,b)\) containing \(C\), its fundamental
cycle has the form \([Y]=m[C]+R\) with \(ab=4m+\deg R\).
This provides a **cycle-level** stratification of the proper equation
space; it is not a stratification of the full saturated ideals.
In particular, a pure Chow cycle \((ab/4)[C]\) is a necessary condition
for sole support (when \(4\mid ab\)), but does not recover embedded
structure, the complete-intersection Hilbert polynomial, or the
two-generator property of a limiting ideal.

There are therefore two complementary parameterizations, not interchangeable
tests. The proper-pair locus in
\(\mathbf P(I_C(a))\times\mathbf P(I_C(b))\) (or the pencil Grassmannian
when \(a=b\)) retains **actual equations**; its cycle map records
multiplicity and residual degree. The bounded supported Hilbert incidence
\(H_N\) retains **full flat ideals**, including the two opposite limits.
A graph of the equation-to-ideal map can relate their closures, but
points on its boundary need not be generated by the limiting pair.
Use the full generator criterion [R-0039](../../results/moving_ideal_generator_criterion.md)
on the moving fiber, not a Chow equality or an extreme-weight pencil.

The older torus/VGIT investigations also distinguish the GIT weight of a
pencil from the Hilbert limit of its ideal. A semistability or weight
calculation alone does not give a supported intersection, and the
existence of a cycle-level residual absorption does not supply a flat
supported CI deformation. The [marked absorption argument](../../arguments/residuals/marked_deformation_and_absorption.md)
already provides closed multiplicity conditions on actual proper pairs
and partial-absorption controls. Any further Chow or VGIT construction
must improve those existing conditions, rather than repackage them.

## Coverage boundaries

Failure of eigenform equations does not exclude other moving equations or
attracting families; failure at one fixed ideal does not exclude other
components. The [finite residual controls](../../arguments/torus_sextic_residuals.md#finite-replay-evidence)
check calculations but do not prove realization or coverage.

## Weight geometry and moving families

[Weights and full limits](weights_and_limits.md) gives the normal-coordinate
and endpoint geometry behind the directional loci. The
[supported deformation test](supported_deformation_questions.md) explains
what a represented family can establish. The same approach can organize a
[downstairs ACM construction](../global-equation-realization/projection_and_liaison.md)
if the moving ideal is tested at that threshold. Explicit
[residual constructions](../residual-construction/index.md) explain how
generation or cycle support can change without providing supported limits.


### Focused mathematical developments

- [Torus actions, endpoint frames, and transport](torus_actions_and_endpoint_frames.md)
- [Weight components and normal filtrations](weight_symbols_and_normal_filtrations.md)
- [Extreme weights and saturated Hilbert limits](extreme_weights_and_hilbert_limits.md)
- [Generic transverse algebras and endpoint contact](generic_algebras_and_endpoint_contact.md)
- [Global postulation and residual support](global_postulation_and_residual_support.md)
- [Sextic filtration and source comparisons](sextic_filtration_and_source_comparisons.md)

The original [section-address compatibility page](weights_and_limits.md) retains old headings for existing references. The developments distinguish individual equation symbols from the saturated full initial ideal, and generic normal algebra from endpoint extension and global support.
