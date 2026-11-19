---
id: STCI-R-0076
type: result
title: Full inverse support in the marked elliptic double-cover construction
scope: "#scope"
statement: "#statement"
proofs:
  - name: target rulings and a Cartier zero scheme on the residual divisor
    at: "research/arguments/carriers/elliptic_double_inverse_construction.md#a-length-twelve-scheme-testing-every-basepoint-free-fiber"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Full inverse support in the marked elliptic double-cover construction

## Scope

Work over an algebraically closed field of characteristic zero. Take
the source quadric \(S_\mu=V(Q_1+\mu Q_0)\) with \(\mu(\mu^2-1)\ne0\), marked elliptic curve \(E=V(Q_0,Q_1)\) and
four basepoint-free sections \(U_j=V_j+\rho_j Q_0\) of the specified
five-parameter family. Their finite map \(f\) restricts to a double
cover \(E\to C_0=[s^4:s^3t:st^3:t^4]\). The support criterion applies
before testing whether \(f\) is birational onto its image.
[Family and section rows](../arguments/carriers/elliptic_double_inverse_construction.md#2-the-complete-five-parameter-lifting-family-and-its-symmetry)

## Statement

The pullback of the unique target quadric through \(C_0\) is \(E+D\).
The residual divisor \(D\) carries a Cartier zero scheme \(Z\) of length
twelve. Off \(E\), it agrees scheme-theoretically with \(f^{-1}(C_0)\).
Thus the full reduced inverse is \(E\) exactly when \(|Z|\subset E\).
This holds for reducible and nonreduced \(D\) as well. Equivalently,
adjoining the column \(Q_0^{12}\) in equation (9) preserves rank 613.
[Geometric proof and matrix](../arguments/carriers/elliptic_double_inverse_construction.md#a-length-twelve-scheme-testing-every-basepoint-free-fiber)

## Limitations

For a birational fiber with full inverse support, a mate of degree \(b\)
requires \(Q_0^b\) to be a degree-\(b\) polynomial in the four actual
sections. Such an identity would give a defining pair with the implicit
octic. The completed parameter-line search found no eligible fiber.
[Descent identity (8)](../arguments/carriers/elliptic_double_inverse_construction.md#5-fiberwise-support-and-actual-descending-equations) ·
[Bounded investigation](../investigations/stci-equation-search/index.md#findings)

## Review

Independent reconstruction checked the ruling degrees on \(E+D\) and
on \(D\), the Cartier division by \(E\), the length, and the column
span in (9), including its cohomology on repeated components. The
characteristic-zero center line has a separate exact elimination and
replay. [Geometric review](../arguments/carriers/elliptic_double_inverse_construction.md#a-length-twelve-scheme-testing-every-basepoint-free-fiber) ·
[Application to the line](../arguments/carriers/elliptic_double_inverse_construction.md#the-characteristic-zero-center-line)
