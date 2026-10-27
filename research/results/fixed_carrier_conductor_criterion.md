---
id: STCI-R-0003
title: Fixed-carrier conductor descent criterion
kind: theorem
status: proved
scope:
  characteristic: "any algebraically closed field"
  curve: "integral curve on a fixed integral Cohen-Macaulay projective surface"
  hypotheses:
    - "Finite normalization and ample polarization"
    - "Full inverse support consists of curves, without isolated points"
statement: "An STCI mate on a fixed hypersurface exists exactly when the full conductor descent lattice contains a fully positive vector."
dependencies: []
evidence:
  - "research/notes/2026-10-13-generalization-conductor-theorem.md"
independent_audits:
  - research/notes/2026-10-13-generalization-conductor-theorem.md
accepted_in: "research/AUDITED_STATE_2026-10-14.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Only a fixed-carrier theorem; not a global carrier classification."
  - "Abstract finite reduction is not an effective algorithm for arbitrary surfaces."
---

# Fixed-carrier conductor descent

## Statement and hypotheses

Let X be an integral Cohen-Macaulay projective surface over an algebraically closed field of any characteristic, with finite normalization nu:S->X and ample line bundle L, and let C be an integral curve. Put H=nu*L and W=(nu^-1 C)_red.

An isolated point of W outside its curve components excludes a section cutting C set-theoretically. Otherwise write W as the union of curves Gamma_1,...,Gamma_s. Define the relation lattice

    Lambda = ker[Z^(s+1) -> Cl(S)]
    (n_1,...,n_s,d) |-> sum n_j[Gamma_j] - d[H].

A lattice vector determines an upstairs rational section with divisor sum n_j Gamma_j. At generic conductor curves away from C, its full-conductor unit classes define a homomorphism phi from Lambda to the product G of the actual unit quotients B_eta^*/A_eta^*. Define Lambda_desc as the kernel of the induced map Lambda -> G/Tor(G).

**Theorem:** A positive power of L has a section cutting out exactly C set-theoretically if and only if Lambda_desc contains a vector whose coefficient n_j is strictly positive for every inverse branch. For a hypersurface in projective three-space, sections lift to ambient homogeneous forms, giving exactly the fixed-carrier mate criterion.

## Proof outline

Necessity comes from pulling back the mate divisor. For sufficiency, torsion of the off-C conductor classes permits a common descending power. Positivity on every branch over C forces a further power into the actual conductor ideal there. Cohen-Macaulay depth and normality upstairs turn generic conductor membership into global descent. The resulting zero support is C.

## Consequences and limitations

The descending lattice is saturated relative to Lambda and has a finite support-covering test using its nonnegative cone. This is not a general effective algorithm: class groups and conductor unit maps remain to be computed. In characteristic zero, residual torsion alone does not ensure that a particular unit descends; the nilpotent logarithmic defect must vanish. Split residual phases may have unbounded orders.

For a singleton branch when X is generically regular along C, set a=H^2, c=H.Gamma, g=gcd(a,c). Let t be the order of (a/g)[Gamma]-(c/g)[H], and E the full-conductor unit order of the resulting primitive upstairs section. A mate exists exactly when both are finite; possible mate degrees are k*t*E*c/g for positive integers k. This formula requires all the singleton and generic-regularity assumptions.

## Evidence

[Original theorem and recorded independent audits](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-13-generalization-conductor-theorem.md).

[Accepted October 14 state, Section 2](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/AUDITED_STATE_2026-10-14.md).

The source proof is preserved on the Ultra branch; no new independent proof or unrestricted STCI conclusion is asserted here.
