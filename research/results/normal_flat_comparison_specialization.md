---
id: STCI-R-0063
type: result
title: Normal flatness specializes the full equation comparison for a rank-two complete intersection
scope: "#scope"
statement: "#statement"
proofs:
  - name: two normal cones and the two lowest equation degrees
    at: "research/arguments/transverse_specialization.md#comparison-under-normal-flatness"
    using: [STCI-R-0030, STCI-R-0062]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# The equation comparison under normal flatness

## Scope

Work in formal equicharacteristic coordinates along a smooth marked curve
in a smooth threefold. Let \(B=k[[t]]\) for a field \(k\) of arbitrary
characteristic, \(R=B[[x,y]]\), \(I=(x,y)\), and let \(J=(f,g)\subset I\)
be a regular-sequence ideal. Fix the parameter lift specifying \(B\to R\).
Write \(M=R/J\), \(K=IM\), \(S=\operatorname{gr}_I R=B[X,Y]\),
\(H=\operatorname{in}_I J\), \(T=\operatorname{in}_I(IJ)\). Use the full
initial ideals. Write \(D=J/IJ\) with
\(F^n D=((J\cap I^n)+IJ)/IJ\), and put
\[
A=S/H,\qquad A'=S/T,\qquad
G=\operatorname{gr}_F D=H/T,\qquad Q=H/S_+H,\qquad \Delta=T/S_+H .
\]
There is no initial sole-support assumption.

## Statement

Assume first that \(M\) is \(B\)-flat. Degreewise \(B\)-flatness of \(A\)
and \(A'\) is equivalent to degreewise \(B\)-flatness of \(A\) and \(G\).
Under either condition the normal algebras of \(R/J\) and \(R/IJ\) commute
with the specified slice. The sliced equations form a regular sequence.
The natural maps from \(H\otimes_B k\) and \(T\otimes_B k\) identify them
as the full initial ideals of \(\bar J\) and \(\bar I\bar J\) in
\(k[X,Y]\), respectively. The resulting maps identify
\[
(Q,G,\Delta)\otimes_B k
\simeq (Q_{\mathrm{slice}},G_{\mathrm{slice}},\Delta_{\mathrm{slice}})
\]
and preserve the exact equation comparison.

In this formal rank-two setting, degreewise flatness of \(A\) alone
implies \(B\)-flatness of \(M\) and \(G\), and hence gives all the preceding
identifications. It also gives \(K^N=0\) for some \(N\), so
\(\sqrt{J}=I\) locally.

The [two-cone proof](../arguments/transverse_specialization.md#comparison-under-normal-flatness)
uses the [first two equation degrees](../arguments/transverse_specialization.md#the-two-lowest-initial-equation-degrees)
to pass from ordinary normal flatness to flatness of \(G\).

## Limitations

The flatness hypotheses suffice for compatibility of the defect and
are stronger than necessary for that compatibility. The supported
family \(J=(x^2,y^2+tx)\) has length four and has \(\Delta=0\) both
relatively and on the slice. Its normal-cone comparison nevertheless has
one-dimensional kernels in degrees two and three.
[Length-four calculation](../arguments/transverse_specialization.md#the-supported-length-four-control)

Actual flatness and sole support alone allow the defect to change.
The [supported length-five family](supported_length_five_defect_specialization.md)
has \(\Delta=0\) relatively and a nonzero degree-four defect on the actual
closed slice. The specialization maps on \(H,T,\Delta\) still exist
outside normal flatness. The map from \(H\otimes_B k\) to \(k[X,Y]\)
can have a kernel, and its image can be strictly smaller than the full
slice initial ideal. The same distinction applies to \(T\).

The theorem gives no flatness or vanishing claim for \(Q\) or \(\Delta\).
If \(G\) is flat, every torsion class of \(Q\) lies in \(\Delta\).
Whether such punctual torsion occurs on the normal-flat locus remains
open here. The broader question whether a sole-support complete
intersection with \(\Delta_\eta=0\) can have nonzero punctual relative
\(\Delta\) also remains open. No identification of the full filtered
scheme from its cone or defect and no global quartic realization follows.

## Review

The Phase 5 nonauthor reviewer `review_specialization` accepted the
two-cone route with R-0030 and R-0062 as joint premises. The reviewer
reconstructed the strict sequence for \(D\subset R/IJ\), the maps from the
two relative initial ideals to the full slice ideals, and exactness of the
specialized comparison under flatness of \(G\). They checked strict
reduction of the equation filtration, localization and completion at the
generic marked point, the two-lowest-degrees lemma, and the saturation
and support conclusions. The reviewer separately reconstructed the
supported length-four control in arbitrary characteristic. The decision
applies to the chosen transverse slice in the formal two-equation setting.

The October 24 source records independent reconstruction of its local
specialization development. It uses the earlier local equation comparison
and the inherited supported quadruple calculation.
[Specialization source](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#delta-transverse-specialization-and-normal-flatness) ·
[Supported quadruple](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#7-a-supported-quadruple-torsion-in-q-is-not-enough)
