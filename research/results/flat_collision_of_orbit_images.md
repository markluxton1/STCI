---
id: STCI-R-0055
type: result
title: A flat genus-twenty-eight collision of compactified orbit families
scope: "#scope"
statement: "#statement"
proofs:
  - name: relative endpoint lattices and image base change
    at: "research/arguments/torus_embedded_quotients.md#a-flat-collision-of-the-genus-twenty-eight-images"
    using: [STCI-R-0051, STCI-R-0052, STCI-R-0054]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# A flat genus-twenty-eight collision of compactified orbit families

## Scope

Let \(k\) be algebraically closed of characteristic zero. Set

\[
B_h=k[h,\epsilon]/\bigl(\epsilon(\epsilon-h)
(\epsilon-2h)(\epsilon-3h)\bigr),\qquad u=1+\epsilon,\ v=1.
\]

Choose an affine open neighborhood \(U\) of \(0\in\mathbf A^1_h\) where
the norm of \(u\) and the coefficient determinant of
\((1,a,b,a^2)\), \(a=u^{-3}-1,b=u^{-4}-1\), are invertible.
Such a \(U\) exists since their values at zero are \(1\) and \(36\).
Put \(R=\mathcal O(U)\), \(B_R=B_h\otimes_{k[h]}R\). Use the actual
scheme image of \(\mathbf P^1_{B_R}\to\mathbf P^3_R\) defined by
\([s^4:s^3t:ust^3:t^4]\).

## Statement

This scheme image is flat over \(U\), and its fiber at every point of
\(U\) is the scheme image formed from the corresponding fiber quotient.
Its zero- and infinity-endpoint lattices have exact free bases

\[
1,\ r^3\epsilon,\ r^6\epsilon^2,\ r^9\epsilon^3;\qquad
1,\ z^3a,\ z^4b,\ z^6a^2.
\]

Their cokernels in the finite source are free \(R\)-modules of ranks
eighteen and thirteen. Every projective fiber has polynomial \(16d-27\).
At each \(h\ne0\) in \(U\) the image consists of four reduced quartic
components. At \(h=0\) it is the sole-support image of
\(k[\epsilon]/(\epsilon^4)\), \(u=1+\epsilon,v=1\), whose infinity
endpoint has type two. The quotient \(\epsilon=0\) retains the fixed
embedded marked curve \(C_0=[s^4:s^3t:st^3:t^4]\) in every fiber.

## Evidence

[The full relative proof](../arguments/torus_embedded_quotients.md#a-flat-collision-of-the-genus-twenty-eight-images)
proves lattice closure, flat cokernels, and fiber image compatibility.
Its infinity closure check is explicit: the unique nonunit product of
total weight below seven is \(a\cdot a=a^2\) at weight six; all remaining
products have sufficient weight to reduce in the displayed basis.
The retained source is [the flat collision section](../synthesis/toric_quotients_and_endpoint_descent.md#colliding-orbit-families-inside-the-hilbert-scheme).

## Limitations

Flatness of a finite quotient family alone would not prove flatness of
its compactified images or image base change. The explicit endpoint
lattices supply those missing assertions for this family. Its Hilbert
polynomial differs from the fourth-root CI's \(16d-32\); this is not a
flat deformation of that CI through these images. It does not produce
a supported complete intersection or a comparison with opposite full
torus Hilbert limits.

## Review

The source has a separate review of its collision argument. The explicit relative closure justification here was also reviewed.

Independent reconstruction review, 2026-11-04: reviewer
pilot_review_hilbert accepted the exact R-0055 route after reconstructing
relative weighted algebra closure, flat endpoint cokernels, image base
change and the constant Hilbert polynomial. The weighted closure argument
was checked also on semisimple fibers; the coefficient determinant was
independently recomputed. No blocker was found within this characteristic-zero family. The reconstruction review accepts this route within its stated scope. It does not assert a deformation of the fourth-root CI.
