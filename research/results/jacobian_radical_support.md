---
id: STCI-R-0081
type: result
title: Relative Jacobian radical recovery and two-product quartic support
scope: "#scope"
statement: "#statement"
proofs:
  - name: finite projection and the Artinian Jacobian socle
    at: "research/arguments/equations/jacobian_radical_support.md#radical-recovery-for-any-proper-pair-missing-the-projection-center"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Relative Jacobian radical recovery and two-product quartic support

## Scope

Over any field of characteristic zero, let \(J=(F_a,G_b)\) be a
homogeneous regular sequence in \(k[x_0,x_1,x_2,x_3]\), with projective
intersection disjoint from \(M=V(x_0,x_3)\). No prescribed support,
normality, or reducedness is assumed.

## Statement

For \(D=F_{x_1}G_{x_2}-F_{x_2}G_{x_1}\),
\[
 J:D=\sqrt J.
\]
If the pair contains the fixed quartic \(C=[s^4:s^3t:st^3:t^4]\), then
its sole reduced support is \(C\) exactly when
\[
 (x_0x_3-x_1x_2)D\in J,\qquad (x_0^2x_2-x_1^3)D\in J.
\]
These are homogeneous cofactor identities of degrees \(a+b\) and
\(a+b+1\). [Proof and exact two-product criterion](../arguments/equations/jacobian_radical_support.md).

## Limitations

Finite freeness over the projection base globalizes the classical Artinian
CI Jacobian-socle theorem. This compresses exact support recognition to two
actual polynomial memberships; it supplies no theorem forcing either class
to be nonzero. The Jacobian depends on both full equations and its degree
grows with them. Fixed-depth source controls do not make these identities
automatic. The characteristic-zero hypothesis is substantive; no unrestricted
positive-characteristic version is asserted.

## Review

On November 23, 2026, the geometry reviewer reconstructed the generalization;
a distinct correctness reviewer independently reconstructed the written proof,
including finite freeness, geometric generic Artin factors, torsion-free
contraction, the residual line and purity argument, and the cofactor degrees.
The literature reviewer checked the classical Jacobian-socle input in
Eisenbud–Ulrich, published Appendix A.5. No computational replay is needed
for this algebraic proof. The proof does not establish existence or
nonexistence of a sole-supported pair.
