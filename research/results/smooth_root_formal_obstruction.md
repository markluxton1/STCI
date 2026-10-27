---
id: STCI-R-0005
title: Smooth movement-two roots do not lift to all exceptional neighborhoods
kind: theorem
status: proved
scope:
  characteristic: "any algebraically closed field, with the balanced normal-bundle hypothesis"
  curve: "smooth rational degree-e curve in P3, e>=4, with normal bundle O(2e-1)^2"
  hypotheses:
    - "r>=2"
    - "Z is a smooth divisor in the class O_E(2,r) on E=P1 x P1"
    - "Lifting means compatible embedded effective Cartier divisors on all exceptional neighborhoods in the actual blowup"
statement: "No such smooth movement-two root Z has an all-orders embedded Cartier lift in the exceptional formal completion."
dependencies: []
evidence:
  - "research/notes/2026-10-15-generalization-smooth-root-formal-nonexistence.md"
  - "research/notes/2026-10-15-generalization-smooth-root-characteristic-scope-addendum.md"
independent_audits:
  - "research/notes/2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md"
accepted_in: "research/notes/2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not exclude all actual complete intersections with smooth roots."
  - "No explicit universal finite jet stage is computed."
  - "Actual-CI consequences require the separate blowup-bridge hypotheses."
---

# Smooth movement-two formal-root obstruction

## Statement

Let C be a smooth rational degree-e curve in projective three-space over an algebraically closed field, e>=4, with the explicit balanced normal bundle N_C = O_C(2e-1) direct sum O_C(2e-1). Let B be the blowup of C and E its exceptional divisor, identified with P1 x P1.

For every r>=2 and every smooth divisor Z in the linear system O_E(2,r), **Z cannot extend to compatible embedded effective Cartier divisors on all infinitesimal neighborhoods of E in B**. Smoothness refers to the actual divisor, not just its reduced support. The smooth (2,r) divisor is connected and integral and maps finitely to C.

The original characteristic-zero proof was independently audited. The subsequent characteristic-scope addendum extends this **formal geometric theorem** to arbitrary algebraically closed characteristic under the same explicit normal-bundle hypothesis. It does not assume that the fixed monomial C0 has that splitting in every characteristic.

## Proof outline

An all-orders embedded Cartier lift would define a smooth formal surface along the full Z. Its normal degree is positive enough to algebraize it as a branch. The algebraic closure would then have a degree bounded above by a normal-degree intersection inequality and bounded below by a plane-section/genus inequality. The two bounds are incompatible for movement degree two and r>=2. The proof retains all other algebraic branches and does not assume that a formal line bundle extends globally on B.

A general numerical version appears in the source: for a smooth connected root of class (epsilon,r), with genus g=(epsilon-1)(r-1), normal degree nu=(2e-1)r-epsilon, and h=e*r, if nu>4g+5 then any algebraized surface degree d must satisfy

    d <= max_{a positive integer} (2*a*h - nu*a*a)
    (d-1)(d-2) >= e*r*(r-1).

The contradiction in the (2,r) case proves the theorem.

## Consequences and limits

For the fixed characteristic-zero C0, this excludes an **infinite compatible formal lift** of every smooth movement-two root, uniformly over first normal orders r>=2. The accepted finite-tower argument implies that, for each fixed r, some finite stage already has no such smooth lifts; it does **not** provide an explicit stage.

This does **not** by itself exclude an actual STCI with that initial root. To transfer it to actual intersections requires the independently audited actual-CI blowup bridge, including its saturated first relation, joint generation of leading sections, full generic initial regular sequence, a gap of at least two, and a smooth full root. See [bridge proof](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-inseparable-root-blowup-bridge.md) and [independent bridge audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit.md).

## Evidence

- [Formal-root theorem and general numerical criterion](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-smooth-root-formal-nonexistence.md)
- [Independent formal-root audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md)
- [Characteristic-scope addendum](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-15-generalization-smooth-root-characteristic-scope-addendum.md)

No component proof is rerun in this promotion; the theorem and audit are preserved on the Ultra branch.
