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

This strategy studies actual intersections and their embedded multiple
structures. It can inform construction or obstruction independently. The
cataloged pilot Results are reviewed provisional mathematics; their review
does not promote them or resolve unrestricted STCI.

## Available results

[R-0037](../results/supported_hilbert_full_limits.md) supplies both full torus
limits in the same supported incidence, retaining the Hilbert polynomial and
all embedded structure. Its exponent bound is individual, not uniform.
[R-0038](../results/torus_eigenvector_generator_lifting.md) lifts minimal
generators only when the whole homogeneous ideal is invariant.
[R-0040](../results/invariant_supported_ci_exclusion.md) applies the trace
obstruction to such an invariant CI: characteristic zero excludes it, and in
characteristic \(p>0\) the degree product must be divisible by \(p\).
Invariance of the radical alone supplies no eigenform presentation.

The complete [Hilbert-boundary argument](../arguments/torus_hilbert_boundary.md)
explains why the useful object is the whole fixed boundary ideal, with its
possible additional generators. The equation condition belongs on the moving
ideal. [R-0039](../results/moving_ideal_generator_criterion.md) tests its entire
minimal-generator module \(J/S_+J\). A finite multiplication-map test requires
an actual regularity bound on the declared family.

## Directional loci

For a fixed ideal \(J_0\), let \(A_+(J_0)\) and \(A_-(J_0)\) mean the
sets of points whose full limits at zero and infinity are respectively
\(J_0\). For a pair of fixed ideals, study
\(A_+(J_+)\cap A_-(J_-)\). These are definitions of organizing sets.
No finite fixed-point list, affine-cell description, local closedness,
smoothness, or exhaustive stratum classification is asserted. Fixed components
may have positive dimension. Two one-sided families do not establish that a
single moving ideal realizes their proposed opposite limits.

## Controls

[R-0043](../results/sextic_eigenpair_quotient_bound.md) bounds proper sextic
eigenpairs, not arbitrary mixed-weight pairs. In
[R-0046](../results/sextic_three_generator_full_limit.md), a proper sextic CI
has a full saturated ACM limit requiring generators of degrees \(6,6,10\).
Both fibers have residual degree 32 and generic multiplicity one on \(C\).
Their polynomial is \(36n-144\), but they are outside every sole-supported
\(H_N\). They test full-ideal bookkeeping, not supported-CI nonemptiness.

The Hilbert-limit scheme, the two extreme equation forms, the normal-cone
initial ideal, and the fundamental cycle are different objects. Keeping only
a cycle or a pure hull can discard data necessary for deformation. Likewise,
following individual points in a residual divisor does not compute its flat
divisor limit; [R-0048](../results/moving_sextic_residual_limit.md) supplies a
concrete control. [R-0049](../results/sextic_residual_absorption.md) transfers
some residual multiplicity to \(C\) while retaining a residual line; it does
not prove that transfer can be iterated to sole support.

## Bridges

The [supported generator investigation](../investigations/supported-generator-incidence/index.md)
asks for an actual specified supported family and its two-generator locus.
The [quotient comparison investigation](../investigations/quotient-hilbert-comparison/index.md)
asks which transverse and endpoint data specialize through an actual map.
Both must preserve the full embedded object.

A construction must verify support, polynomial, and actual homogeneous ideal
generation. An obstruction must cover its declared family. Extending it to all
supported pairs of a fixed degree requires coverage of the relevant fixed
limits and power bounds; extending it to all degrees is a further problem.
Finding an arbitrary supported flat deformation to a CI is already useful;
realizing a prescribed torus boundary as an orbit limit is a stronger task.

## Research decisions

Pursue a family when its full ideals and actual multiplication maps are
accessible. A failure of eigenform equations suggests changing the moving
equations, not rejecting all attracting families. A failure at one fixed ideal
can redirect the family search but cannot close other components. Keep direct
geometric constructions available when they do not need a fixed-point
classification. The finite [residual controls](../investigations/torus-residual-controls/index.md)
check calculations without replacing the realization and coverage arguments.

This consolidates the research formulation in
[the attracting-locus source](../synthesis/torus_attracting_strata_and_generator_incidence.md)
and the [supported-boundary source](../synthesis/global_equations_and_constructions.md#the-supported-hilbert-locus-and-its-full-torus-boundary).
