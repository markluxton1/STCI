---
id: STCI-R-0050
type: result
title: Primitive orbit degrees and finite transverse quotient multiplicities
scope: "#scope"
statement: "#statement"
proofs:
  - name: primitive monomial parametrization and generic localization
    at: "research/arguments/torus_sextic_residuals.md#orbit-curves-and-finite-quotient-degree"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Primitive orbit degrees and finite transverse quotient multiplicities

## Scope

Let \(k\) be algebraically closed of any characteristic, with the torus
action on \(\mathbf P^3_k\) having integer weights \(w=(0,1,3,4)\).
For an orbit with at least two nonzero coordinates let \(J\) be its
nonzero index set. For the second assertion take any proper pair of
positive-degree homogeneous eigenforms and use dense coordinate torus
coordinates \(x=(1,t,t^3u,t^4v)\).

## Statement

An orbit with nonzero index set \(J\) has irreducible rational closure
of projective degree

\[
\frac{\max_{j\in J}w_j-\min_{j\in J}w_j}
{\gcd\{w_i-w_j:i,j\in J\}}.
\]

The gcd is taken in the integers before passing to the image. In positive
characteristic it removes the inseparable part of the orbit parameter
map as well as any separable degree. Every reduced irreducible invariant
curve meeting the dense coordinate torus is such an orbit closure.

If the proper eigenpair restricts to \(t^rf(u,v),t^sg(u,v)\), then

\[
V(F,G)\cap T_{\mathrm{dense}}
=\operatorname{Spec}B\times\mathbf G_m,\qquad
B=k[u^{\pm1},v^{\pm1}]/(f,g)
\]

with \(B\) finite dimensional, possibly zero. For a quotient point
\((\epsilon,\zeta)\), the orbit closure is the smooth quartic

\[
C_{\epsilon,\zeta}=[s^4:s^3t:\epsilon st^3:\zeta t^4].
\]

Its generic scheme multiplicity equals the length of the local factor
of \(B\). Thus the fundamental-cycle degree of all components meeting
the dense torus is \(4\dim_kB\), counting multiplicities. Each such
quartic has only \(p_0=[1:0:0:0]\), \(p_\infty=[0:0:0:1]\) on the
coordinate boundary.

## Proof

The [complete orbit proof](../arguments/torus_sextic_residuals.md#orbit-curves-and-finite-quotient-degree)
divides the monomial exponents by their gcd to obtain a birational
primitive parametrization. It computes the pullback hyperplane degree,
proves finiteness from properness, and localizes the product scheme to
obtain generic multiplicities.

## Evidence

Reconstructed from §§1 and 5 of
[sextic residuals](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_sextic_residuals_and_limits.md).
The dense quotient calculation is the elementary product calculation,
not a claim of global endpoint descent.

## Limitations

Invariant curves lying on coordinate hyperplanes can have different
degrees, including lines and cubics. Noninvariant residual curves are
not classified here. A finite quotient does not record boundary cycles,
attachment, or endpoint schemes, and quotient flatness does not on its
own establish projective-image flatness.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
accepted this route on November 4, 2026. The reviewer reconstructed the primitive monomial degree formula,
its inseparable-degree qualification, the dense-torus product, finiteness
from properness, and generic local multiplicities. Acceptance makes no
inference from quotient data alone to boundary or endpoint geometry.

Independent reconstruction review accepts this route within its stated scope.
