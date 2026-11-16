---
id: STCI-R-0051
type: result
title: Finite embedded transverse quotients give pure orbit-image curves
scope: "#scope"
statement: "#statement"
proofs:
  - name: scheme image and finite charts
    at: "research/arguments/torus_embedded_quotients.md#finite-image-and-purity"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Finite embedded transverse quotients give pure orbit-image curves

## Scope

Let \(k\) be any algebraically closed field, of arbitrary characteristic,

\[
B=k[u^{\pm1},v^{\pm1}]/J,\qquad 0<n=\dim_k B<\infty,
\quad S=k[x_0,x_1,x_2,x_3].
\]

The specified quotient map, including the units \(u,v\in B\), is part of
the data. No reducedness, separability, Gorenstein or complete-intersection
hypothesis on \(B\) is imposed. Give \(s,t\) degree one and read target
degrees in multiples of four. All images below are scheme-theoretic.

## Statement

For the homogeneous kernel

\[
K=\ker\bigl(S\longrightarrow B[s,t]\bigr),\qquad
(x_0,x_1,x_2,x_3)\longmapsto(s^4,s^3t,ust^3,vt^4),
\]

\(K\) is irrelevant-saturated. The curve \(Z_B=\operatorname{Proj}(S/K)\)
is the scheme-theoretic projective closure of

\[
\operatorname{Spec}B\times\mathbf G_m\longrightarrow\mathbf P^3,
\quad (u,v,r)\longmapsto[1:r:ur^3:vr^4].
\]

The induced morphism \(\nu:\mathbf P^1_B\to Z_B\) is finite and is an
isomorphism away from the two endpoint supports
\(p_0=[1:0:0:0]\), \(p_\infty=[0:0:0:1]\). Its affine image charts are

\[
k[r,r^3u,r^4v]\subset B[r],\qquad
k[z,z^3\alpha,z^4\beta]\subset B[z],
\]

where \(z=(u/v)(s/t)\), \(\alpha=v^2/u^3\), \(\beta=v^3/u^4\).
Both image charts are finite torsion-free modules over their parameter
polynomial rings. In particular \(Z_B\) is a pure Cohen--Macaulay curve;
it has neither embedded endpoint points nor boundary curve components.

For every \((c,d)\in\operatorname{Supp}B\subset\mathbf G_m^2(k)\), one
reduced component is the smooth quartic
\([s^4:s^3t:cst^3:dt^4]\). These are all its reduced components; distinct
ones meet only at the endpoints. For \(C_0=[s^4:s^3t:st^3:t^4]\),

\[
C_0\subset (Z_B)_{\mathrm{red}}\iff(1,1)\in\operatorname{Supp}B,
\qquad (Z_B)_{\mathrm{red}}=C_0\iff\operatorname{Supp}B=\{(1,1)\}.
\]

## Evidence

The complete proof is [the finite-image and purity section](../arguments/torus_embedded_quotients.md#finite-image-and-purity).
The historical source is [the original orbit-family construction](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_quotients_and_endpoint_descent.md#geometry-of-a-finite-family-of-orbit-closures).
No finite computation is required for this claim.

## Limitations

An abstract finite algebra without its chosen \(u,v\) does not determine
this image. This construction concerns a constant embedded transverse
quotient; it is not a parametrization of arbitrary moving supported
complete intersections. The finite map is not called a normalization when
\(B\) is nonreduced. Purity does not assert that \(Z_B\) is arithmetically
Cohen--Macaulay or a complete intersection.

## Review

The historical source records a separate review of its image and endpoint arguments.

Independent reconstruction review, 2026-11-04: reviewer
pilot_review_hilbert accepted the exact R-0051 route after independently
reconstructing the scheme image, saturation, finite charts, support and
Cohen--Macaulay purity arguments. No blocker was found within the stated
constant embedded-quotient scope. The reconstruction review accepts this route within its stated scope.
