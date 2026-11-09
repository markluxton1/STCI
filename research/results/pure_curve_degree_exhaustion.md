---
id: STCI-R-0056
type: result
title: A closed subscheme exhausting the degree of a pure curve equals that curve
scope: "#scope"
statement: "#statement"
proofs:
  - name: generic lengths and absence of finite-support submodules
    at: "research/arguments/torus_embedded_quotients.md#pure-curve-degree-exhaustion"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# A closed subscheme exhausting the degree of a pure curve equals that curve

## Scope

Let \(k\) be any field and let \(X\subset\mathbf P^N_k\) be a projective
scheme of pure dimension one whose structure sheaf is pure: every nonzero
coherent subsheaf of \(\mathcal O_X\) has one-dimensional support.
Equivalently here, \(X\) has no embedded associated points of dimension
zero. This holds in particular for a pure Cohen--Macaulay curve. Let
\(Y\hookrightarrow X\) be an actual closed subscheme of dimension at most
one, and compute both degrees with the same projective polarization.
No reducedness or irreducibility is assumed.

## Statement

If \(\deg Y=\deg X\), then the inclusion \(Y\hookrightarrow X\) is an
equality of schemes. More precisely, additivity of generic lengths and
degree first makes the kernel of \(\mathcal O_X\twoheadrightarrow
\mathcal O_Y\) supported at finitely many closed points; purity then
forces this kernel to vanish. If the two projective schemes are given by
saturated homogeneous ideals, those ideals are equal.

In particular, if positive-degree homogeneous forms \(F,G\in
k[x_0,x_1,x_2,x_3]\) have no common factor, and their complete-intersection
curve contains a closed subscheme \(Y\) of degree \((\deg F)(\deg G)\),
then \(Y=V(F,G)\).

## Evidence

[The proof](../arguments/torus_embedded_quotients.md#pure-curve-degree-exhaustion)
supplies both steps, including the elimination of a possible finite-support
kernel. This independently reusable lemma is extracted from the
[source's proper-pair criterion](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_quotients_and_endpoint_descent.md#when-does-the-compactified-family-have-two-global-equations).

## Limitations

Equal degrees without an actual closed inclusion do not imply equality.
Purity of the containing curve cannot be omitted: an embedded point can
be removed without changing degree. Generic equality alone is therefore
insufficient. The statement does not infer properness of a pair from the
existence of two independent sections.

## Review

The source review addressed its specific use of degree exhaustion. Extracting the general lemma required a separate reconstruction review.

Independent reconstruction review, 2026-11-04: reviewer
pilot_review_hilbert accepted the exact R-0056 route after reconstructing
generic-length degree additivity, the finite-support remainder and its
elimination by purity, and the regular-sequence and saturation application
to a gcd-one homogeneous pair. Actual containment and purity are retained
as essential hypotheses. No blocker was found. The reconstruction review accepts this independently reusable lemma within its stated scope.
