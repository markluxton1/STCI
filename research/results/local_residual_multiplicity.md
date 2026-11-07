---
id: STCI-R-0044
type: result
title: Surface-power multiplicities and two local binomial certificates
scope: "#scope"
statement: "#statement"
proofs:
  - name: parameter filtration and exact local reductions
    at: "research/arguments/torus_sextic_residuals.md#local-multiplicity-and-binomial-certificates"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Surface-power multiplicities and two local binomial certificates

## Scope

For the first assertion, \(R\) is a regular local ring of dimension two,
\(R/(q)\) is a discrete valuation ring, and \(f\in R\) has nonzero image
of finite positive order \(d\) in that DVR. For the binomial assertions,
\(K\) is any field, \(\gamma,\delta\in K^\times\), and the ring is
\(K[a,b]_{(a,b)}\). All characteristics are allowed.

## Statement

For every integer \(r\ge1\),

\[
\ell_R R/(f,q^r)=r\,d.
\]

In the specified binomial local ring one has the exact ideal equalities
and lengths

\[
(a^6-b^2,b^6-\gamma a^2)=(a^2,b^2),\qquad\ell=4,
\]

\[
(\delta a^3-b^3,b^6-a^4)=(a^4,b^3-\delta a^3),
\qquad\ell=12.
\]

In particular the lengths four and twelve used for the boundary lines
in the eigenpair controls hold in every characteristic.

## Proof

The [complete local proof](../arguments/torus_sextic_residuals.md#local-multiplicity-and-binomial-certificates)
uses the parameter filtration of the one-dimensional Cohen–Macaulay
ring \(R/(f)\). The binomial proofs reduce one equation modulo the other
and divide a factor which is a unit at \((a,b)\); a displayed finite
free basis gives the remaining length.

## Evidence

The first rule is the multiplicity rule (20) of
[sextic residuals](../synthesis/toric_sextic_residuals_and_limits.md).
The two binomial assertions preserve the local calculations in §§1.1–1.2.
The length-twelve proof here replaces the source's coprime lowest-form
calculation by an exact binomial reduction; independent review must
cover that replacement.

## Limitations

These are local multiplicity statements. They neither identify global
primary components without a contraction argument nor specify complete
endpoint schemes. The unit coefficient hypotheses in the binomial
identities are required as stated; no classification of general
binomial pairs is asserted.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
accepted this route on November 4, 2026. The reviewer reconstructed the parameter-filtration proof and both
exact local binomial reductions, including the replacement length-twelve
unit-factor argument and finite free basis. The proof is a geometric
reduction with necessary exact local algebra, not a blanket intrinsic
replacement. Acceptance is within the stated local hypotheses.

Independent reconstruction review accepts this route within its stated scope.
