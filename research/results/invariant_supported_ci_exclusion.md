---
id: STCI-R-0040
type: result
title: Trace restriction on invariant supported complete-intersection ideals
status: provisional
scope: "#scope"
statement: "#statement"
proofs:
  - name: invariant-generator-lifting-and-trace
    at: "research/arguments/torus_hilbert_boundary.md#invariant-supported-complete-intersections"
    using: [STCI-R-0038, STCI-R-0042]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Trace restriction on invariant supported complete-intersection ideals

## Scope

Let \(k\) be algebraically closed,
\(S=k[x_0,x_1,x_2,x_3]\), and
\(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), with
homogeneous prime ideal \(P=I_C\). Let \(J\subset S\) be a
homogeneous height-two complete-intersection ideal with
\(\sqrt J=P\). Assume that the ideal \(J\) itself is invariant
under the torus of integer weights \((0,1,3,4)\). Let
\(\{a,b\}\), with \(a,b>0\), be the ordinary-degree multiset of
its two minimal homogeneous generators.

These are actual homogeneous ideals in \(S\) and global equations
in \(\mathbf P^3\). Invariance of \(\sqrt J\), which is automatic
for sole support \(C\), is a strictly weaker hypothesis than the
assumed invariance of \(J\).

## Statement

Such an invariant supported complete-intersection ideal cannot exist
in characteristic zero. In characteristic \(p>0\), its generator
degrees necessarily satisfy
\[
p\mid ab,\qquad \max(a,b)\ge p.
\]

More precisely, invariance of \(J\) gives two weight-eigenform
generators \(F,G\) with the same ordinary degrees \(\{a,b\}\).
The trace obstruction for their actual sole-supported pair gives
\(ab=0\) in \(k\).

## Evidence

The complete composite proof is in
[STCI-A-0001](../arguments/torus_hilbert_boundary.md#invariant-supported-complete-intersections).
It jointly uses
[equivariant generator lifting](torus_eigenvector_generator_lifting.md)
and the
[supported eigenform trace obstruction](eigenform_trace_obstruction.md),
checking the actual equations, positive ordinary degrees, integer
weight condition, and sole support before applying the latter.

The source implication appears in the
[supported Hilbert-boundary account](../synthesis/global_equations_and_constructions.md#invariant-support-and-the-full-torus-limit)
and in
[positive movement and the global presentation barrier](../synthesis/tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier).
No new computation is needed for this corollary.

## Limitations

No arbitrary supported pair is made invariant by this argument.
Invariant reduced support alone gives no eigenform generators.
A full torus-fixed limit of a supported CI can have additional minimal
generators, so excluding an invariant supported CI does not exclude a
moving supported CI with such a boundary. There is no all-pair STCI
exclusion here and no uniform degree or support-power bound.

The positive-characteristic assertion is necessary, not sufficient for
existence. In characteristic two it gives no parity conclusion for the
generic multiplicity along \(C\); the factor-only variant of the trace
theorem is not being used.

## Review

Independent reconstruction review accepted this composite route, separately
from the earlier direct Hilbert proofs. It checked preservation of the ordinary
degrees under character lifting, generation of the same height-two ideal,
actual sole support, and the precise characteristic conclusion of R-0042.
No computation was needed. The decision supplies no reduction from radical
invariance or an arbitrary pair to an invariant ideal. The source retains its
own review scope, and this Result remains provisional.
