---
id: STCI-R-0036
title: "Pointwise conductor contact and top-socle defect"
kind: theorem
scope:
  characteristic: "characteristic zero"
  curve: "smooth curve in a smooth threefold"
  hypotheses:
    - "Actual complete intersection supported on C and integral carrier generically regular on C"
    - "Finite normalization with full inverse support a single smooth Cartier curve c isomorphic to C"
    - "Normalization smooth along c; invertible conductor O(-B) with no c component"
statement: "With A the transverse differential zero divisor and J^(n-1)=Soc(Y)(-D_n), equality of actual divisors holds: D_n=(n-1)A-B|c."
dependencies: []
evidence:
  - "research/arguments/carriers/carrier_conductor_differential_comparison.md#conductor-transverse-differential-and-the-actual-top-socle"
independent_audits:
  - "research/arguments/carriers/carrier_conductor_differential_comparison.md#conductor-transverse-differential-and-the-actual-top-socle"
  - "research/arguments/carriers/normal_index_socle_and_torsion.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Not established for multiple branches, non-Cartier lift, singular normalization along c, or generically singular carrier"
  - "Jacobian argument cannot be transferred to characteristic dividing n"
---

# Pointwise conductor contact and top-socle defect

## Statement and hypotheses

With A the transverse differential zero divisor and J^(n-1)=Soc(Y)(-D_n), equality of actual divisors holds: D_n=(n-1)A-B|c.

Required hypotheses:
- Actual complete intersection supported on C and integral carrier generically regular on C
- Finite normalization with full inverse support a single smooth Cartier curve c isomorphic to C
- Normalization smooth along c; invertible conductor O(-B) with no c component

## Proof and verification

- [Source proof](../arguments/carriers/carrier_conductor_differential_comparison.md#the-actual-differential-has-a-smaller-zero-divisor)
- [Source proof](../arguments/carriers/carrier_conductor_differential_comparison.md#divisor-and-conductor-degrees)
- [Independent audit](../arguments/carriers/carrier_conductor_differential_comparison.md#the-actual-differential-has-a-smaller-zero-divisor)
- [Independent audit](../arguments/carriers/normal_index_socle_and_torsion.md#2026-10-14-generalization-transverse-socle-independent-audit)
- [Claim-level acceptance](../arguments/carriers/carrier_conductor_differential_comparison.md#characteristic-applications-and-review)

## Dependencies and limitations

Inherited premises are described in the proof and audit.
- Not established for multiple branches, non-Cartier lift, singular normalization along c, or generically singular carrier
- Jacobian argument cannot be transferred to characteristic dividing n

## Current mathematical evidence

The metadata identifies the live proof owners. Their statements retain the original theorem hypotheses and recorded independent reconstructions; consolidation does not imply an unrestricted conclusion. The full proof, unique corrections and necessary mathematical support are retained in those homes.
