---
id: STCI-R-0045
type: result
title: Colon exact sequence for a surface-supported divisor cycle
status: provisional
scope: "#scope"
statement: "#statement"
proofs:
  - name: prime cancellation and generic lengths
    at: "research/arguments/torus_sextic_residuals.md#a-colon-formula-for-divisor-cycles"
    using: [STCI-R-0044]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Colon exact sequence for a surface-supported divisor cycle

## Scope

Let \(S=k[x_0,x_1,x_2,x_3]\) over any field, let \(q\in S\) be
irreducible homogeneous, let \(a,b\in S\) be homogeneous with
\(q\nmid ab\), and let \(r\ge1\). Set \(I=(q^r,bq,ab)\).
The cycle assertion additionally assumes that
\(Q=V(q)\subset\mathbf P^3_k\) is a smooth surface.

## Statement

There are exact identities

\[
I:q=(q^{r-1},b),\qquad I+(q)=(q,ab),
\]

and the multiplication-by-\(q\) sequence is

\[
0\longrightarrow S/(q^{r-1},b)(-\deg q)
\xrightarrow{\ q\ }S/I\longrightarrow S/(q,ab)\longrightarrow0.
\]

For \(r=1\) the first module is zero. Under the smoothness hypothesis
the fundamental cycle of \(\operatorname{Proj}(S/I)\) is

\[
\operatorname{div}_Q(a|_Q)+r\,\operatorname{div}_Q(b|_Q).
\]

Equivalently, at each irreducible divisor \(E\) in that support its
generic length is
\(\operatorname{ord}_E(a|_Q)+r\operatorname{ord}_E(b|_Q)\).

## Proof

The [complete colon proof](../arguments/torus_sextic_residuals.md#a-colon-formula-for-divisor-cycles)
uses primality of \(q\) to cancel the coefficient of \(ab\); localization
of the exact sequence and R-0044 then compute the cycle.

## Evidence

This abstracts the explicit colon calculation in §4.1 of
[sextic residuals](../synthesis/toric_sextic_residuals_and_limits.md).
The general prime and smoothness hypotheses are stated explicitly here;
no symbolic colon routine is used as the proof.

## Limitations

For the prime-cancellation identity without a grading hypothesis, use
[R-0041](prime_element_colon_identity.md). Its exact sequence applies directly
to formal local domains under its stated assumptions; the projective cycle
formula here retains its homogeneous and geometric hypotheses.

The conclusion is a fundamental-cycle formula. Saturation, absence of
embedded points, endpoint schemes, and equality of ideals are additional
questions for general \(I\). Smoothness can be replaced by regularity at
the generic divisor points, but no singular-surface extension is claimed.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
accepted this route on November 4, 2026. The reviewer reconstructed prime cancellation, the multiplication
exact sequence, and its localized length calculation under the stated
smoothness hypothesis, including the specialization used in R-0046.
Acceptance concerns a cycle formula, without inferring saturation or
endpoint structure for arbitrary such ideals.

The Result remains provisional; independent acceptance of this
reconstructed route does not promote its status or the source's labels.
