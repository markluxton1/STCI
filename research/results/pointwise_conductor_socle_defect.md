---
id: STCI-R-0036
title: "Pointwise conductor contact and top-socle defect"
kind: theorem
status: proved
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
  - "research/supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md"
independent_audits:
  - "research/supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md"
  - "research/supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md"
accepted_in: "research/supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md"
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

- [Source proof](../supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md#exact-top-socle-divisor-for-an-actual-pair)
- [Source proof](../supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md#local-residue-identity-and-global-contact)
- [Independent audit](../supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md#exact-top-socle-divisor-for-an-actual-pair)
- [Independent audit](../supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-transverse-socle-independent-audit)
- [Claim-level acceptance](../supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md#consolidation-review)

## Dependencies and limitations

Inherited premises are described in the proof and audit.
- Not established for multiple branches, non-Cartier lift, singular normalization along c, or generically singular carrier
- Jacobian argument cannot be transferred to characteristic dividing n

## Current mathematical evidence

The metadata identifies the live proof owners. Their statements retain the original theorem hypotheses and recorded independent reconstructions; consolidation does not promote an unrestricted conclusion. The full proof, unique corrections and necessary mathematical support are retained in those homes.
