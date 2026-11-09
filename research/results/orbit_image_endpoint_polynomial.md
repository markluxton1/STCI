---
id: STCI-R-0052
type: result
title: Endpoint lattices determine the Hilbert polynomial of a constant orbit image
scope: "#scope"
statement: "#statement"
proofs:
  - name: finite modification exact sequence
    at: "research/arguments/torus_embedded_quotients.md#endpoint-defects-and-hilbert-polynomial"
    using: [STCI-R-0051]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Endpoint lattices determine the Hilbert polynomial of a constant orbit image

## Scope

For every algebraically closed field \(k\) of arbitrary characteristic,
let \(B=k[u^{\pm1},v^{\pm1}]/J\) have finite positive length \(n\), with
its specified transverse coordinate embedding. Let \(Z_B\subset\mathbf
P^3\) and \(\nu:\mathbf P^1_B\to Z_B\) be the image and finite map
of [R-0051](constant_embedded_orbit_image.md). Put
\(\alpha=v^2/u^3\), \(\beta=v^3/u^4\). No reducedness assumption is made.

## Statement

The completed endpoint images are the finite module algebras

\[
A_0=k[[r]][r^3u,r^4v]\subset B[[r]],\qquad
A_\infty=k[[z]][z^3\alpha,z^4\beta]\subset B[[z]].
\]

Their quotients have finite lengths
\(\delta_0=\dim_k(B[[r]]/A_0)\) and
\(\delta_\infty=\dim_k(B[[z]]/A_\infty)\). There is an exact sequence

\[
0\longrightarrow\mathcal O_{Z_B}\longrightarrow
\nu_*\mathcal O_{\mathbf P^1_B}\longrightarrow Q_0\oplus Q_\infty
\longrightarrow0,
\qquad \ell(Q_i)=\delta_i,
\]

with \(Q_i\) supported at the corresponding endpoint, and
\(\nu^*\mathcal O_{Z_B}(1)=\mathcal O_{\mathbf P^1_B}(4)\). Consequently

\[
P_{Z_B}(d)=4nd+n-\delta_0-\delta_\infty,
\quad \deg Z_B=4n,
\quad p_a(Z_B)=1-n+\delta_0+\delta_\infty.
\]

## Evidence

[The complete proof](../arguments/torus_embedded_quotients.md#endpoint-defects-and-hilbert-polynomial)
constructs conductor tails using positive monomials in the units; it does
not require a reduced finite scheme or a separable power map. The source
is [the original endpoint gluing calculation](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_quotients_and_endpoint_descent.md#the-two-endpoints-as-a-finite-gluing-defect).

## Limitations

These defects are cokernel lengths for a finite modification. They are
not automatically conductor colengths, reduced normalization defects or
residual curve degrees. The two geometric endpoints here are distinct from
the two opposite directions of a full torus Hilbert limit; no comparison
or specialization map between these constructions is asserted. A Hilbert
polynomial identity does not supply global generators.

## Review

The historical source records independent review of its endpoint arguments.

Independent reconstruction review, 2026-11-04: reviewer
pilot_review_hilbert accepted the exact R-0052 route after independently
reconstructing the endpoint image algebras, finite-cokernel exact sequence,
polarization pullback and Hilbert polynomial calculation in the stated
characteristics. No blocker was found. The reconstruction review accepts this route within its stated scope. No comparison with opposite Hilbert-limit directions was included or inferred.
