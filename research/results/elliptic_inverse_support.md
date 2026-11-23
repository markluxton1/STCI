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

**Residual scheme.** The pullback of the unique target quadric through
\(C_0\) is \(E+D\). The divided equation of \(C_0\) defines a Cartier
zero scheme \(Z\) of length twelve on \(D\), including when \(D\) is
reducible or nonreduced.

**Full inverse support.** Off \(E\), the scheme \(Z\) agrees with
\(f^{-1}(C_0)\). Since \(f(E)=C_0\), the full reduced inverse is
\(E\) exactly when \(|Z|\subset E\). [Geometric proof](../arguments/carriers/elliptic_double_inverse_construction.md#a-length-twelve-scheme-testing-every-basepoint-free-fiber)

**Matrix formulation.** The unaugmented matrix in (9) spans the
degree-24 forms on the source quadric vanishing on \(Z\) and has rank
613. Adjoining the column \(Q_0^{12}\) preserves that rank exactly
when \(|Z|\subset E\). [Column-span proof](../arguments/carriers/elliptic_double_inverse_construction.md#matrix-formulation)

## Limitations

For a birational fiber with full inverse support, a mate of degree \(b\)
requires \(Q_0^b\) to be a degree-\(b\) polynomial in the four actual
sections. Such an identity would give a defining pair with the implicit
octic. The completed parameter-line search found no eligible fiber.
[Descent identity (8)](../arguments/carriers/elliptic_double_inverse_construction.md#5-fiberwise-support-and-actual-descending-equations) ·
[Bounded investigation](../investigations/stci-equation-search/index.md#findings)

## Review

The revised geometric and full column-span proof route was independently
reconstructed on November 23, 2026, against commit
`9ee976fe28f4e496230d9b2e22523d4fa5eabe9d`. The review checked the
componentwise ruling-degree estimates, regularity of the divided section
on repeated components, both cohomology vanishings on nonreduced divisors,
the complete degree-24 column span and rank 613, and the length-twelve
nilpotence criterion. Reducible and nonreduced residual fibers are included;
birationality onto the image is not required. The criterion is accepted at
the hypotheses in Scope. This review did not establish a surviving support
fiber, ambient power descent, or the later relative norm-divisor and
dimension-bound arguments. The investigation records the separate
parameter-line and finite-field computations; none was rerun for this proof
review. [Earlier review request](https://github.com/markluxton1/STCI/pull/154#pullrequestreview-5977922254) · [Bounded computations](../investigations/stci-equation-search/index.md#findings)
