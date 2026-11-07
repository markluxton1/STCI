---
id: STCI-R-0054
type: result
title: Embedded quotient coordinates change endpoint genus and local Gorensteinness
scope: "#scope"
statement: "#statement"
proofs:
  - name: exact endpoint lattices and coefficient identities
    at: "research/arguments/torus_embedded_quotients.md#endpoint-examples"
    using: [STCI-R-0051, STCI-R-0052, STCI-R-0053]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Embedded quotient coordinates change endpoint genus and local Gorensteinness

## Scope

For an algebraically closed field \(k\), form the image of
\([s^4:s^3t:ust^3:vt^4]\) for each specified finite quotient \(B\).
Here \(v=1\) in every case. The fourth-root benchmark is defined in
every characteristic; the separated four-point comparison is in
characteristic zero. The nilpotent comparison is formed separately
over each indicated field, with no assertion about arithmetic base
change of images.

## Statement

For \(B=k[u]/(u^4-1)\), the image is the scheme CI

\[
V(x_1^4-x_0^3x_3,\ x_2^4-x_0x_3^3).
\]

At each endpoint its exact finite-modification lattice has weights
\(0,3,6,9\) in the coefficient basis \(1,u,u^2,u^3\), defect eighteen,
and conductor \(r^9B[[r]]\), with \(z\) replacing \(r\) at infinity.
Its Hilbert polynomial is \(16d-32\), and its genus is thirty-three.
In characteristic two this is the image of
\(B=k[\epsilon]/(\epsilon^4)\), \(u=1+\epsilon\), with sole reduced
support \(C_0\). Its nonreduced finite-modification conductor differs
from the full normalization conductor of the smooth reduced curve.

In characteristic zero, the abstract algebra \(k^4\) has another
embedding with \(u\) taking values \(1,2,3,4\). Its zero defect is
eighteen, its infinity defect thirteen, its polynomial \(16d-27\) and
its genus twenty-eight. Thus isomorphic abstract finite algebras with
the same length can give different embedded projective images. This
second image is not a \((4,4)\) CI.

For \(B=k[\epsilon]/(\epsilon^4)\), \(u=1+\epsilon\), the exact defects
and genera, with the image formed over that field, are

| Characteristic | \(\delta_0\) | \(\delta_\infty\) | \(p_a\) |
| --- | ---: | ---: | ---: |
| \(0\), or \(p>3\) | 18 | 13 | 28 |
| \(2\) | 18 | 18 | 33 |
| \(3\) | 18 | 15 | 30 |

In characteristic zero put
\(a=u^{-3}-1\), \(b=u^{-4}-1\). The infinity lattice has basis
\(1,z^3a,z^4b,z^6a^2\), and

\[
A_\infty/zA_\infty\simeq k[x,y]/(x^3,xy,y^2).
\]

It has socle dimension two, so that endpoint is not Gorenstein and is
not a local complete intersection, despite sole reduced support \(C_0\).
The same lattice and algebra assertion holds for \(p>3\).
The displayed genera rule out type \((4,4)\) in all rows except
characteristic two, where the image is the benchmark CI.

## Evidence

The complete proof starts with [the benchmark and conductor](../arguments/torus_embedded_quotients.md#the-fourth-root-image-and-its-conductor)
and continues through [the endpoint counterexamples](../arguments/torus_embedded_quotients.md#embedded-quotients-and-characteristic-dependent-endpoints).
It gives exact coefficient matrices, truncated-polynomial identities,
and weighted algebra-closure proofs. The source is
[the retained quotient chapter](../synthesis/toric_quotients_and_endpoint_descent.md).
The quotient_checks function in the
[existing finite verifier](../investigations/torus-residual-controls/verify.py)
checks the rational determinants and endpoint indices, without proving
the geometry or any general classification.
The separate integral-flatness statement for the prescribed quartic
pair remains [legacy R-0021](quartic_mu4_degeneration.md).

## Limitations

These are specified embedded quotients, not all finite algebras or all
supported intersections. Genus and endpoint type obstruct the displayed
images; they do not exclude other moving families. The conductor of a
nonreduced modification cannot be substituted for the normalization
conductor of its reduction. Arithmetic reduction and fixed-field image
formation have separate quantifiers.

## Review

The source has a separate review, including its characteristic-three calculation; finite arithmetic was checked separately. The legacy R-0021 keeps its own scope and review.

Independent reconstruction review, 2026-11-04: reviewer
pilot_review_hilbert accepted the exact R-0054 route after reconstructing
the endpoint lattices, conductor proof, type-two local algebra and
fixed-field characteristic distinctions. The reviewer independently
recomputed the evaluation determinant 1505/7962624, coefficient determinant
36, truncated nilpotent identity, and characteristic-two and
characteristic-three reductions. No blocker was found. Reconstruction acceptance is limited to the stated characteristic cases. Integral flatness and the separate legacy R-0021 proof were outside this review.
