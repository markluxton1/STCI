---
id: STCI-R-0013
title: "Saturated actual-generator rigidity and movement-one exclusion"
kind: theorem
status: proved
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "fixed C0 in P3"
  hypotheses:
    - "Actual homogeneous complete intersection Y=V(F_a,G_b) with Y_red=C0"
    - "Full generic ordinary initial ideal a coprime binary complete intersection of degrees 2<=r<s"
    - "Actual first degree-r kernel R is a line subbundle (saturated); write R=O(-7r-epsilon), epsilon>=0"
statement: "The actual-generator sequence 0 -> T -> O(-4a)⊕O(-4b) -> R -> 0, where deg T=-7s+s*epsilon/r, is nonsplit; both original equations have exact generic normal order r, and no such STCI has epsilon=1. Necessary identities: ab=4rs, 4(a+b)=7(r+s)-epsilon(s-r)/r, r divides epsilon*s."
dependencies:
  - STCI-R-0001
  - STCI-R-0010
evidence:
  - "research/supplements/NORMAL_FLATNESS_AND_FILTERED_CI.md"
independent_audits:
  - "research/supplements/NORMAL_FLATNESS_AND_FILTERED_CI.md"
accepted_in: "research/supplements/NORMAL_FLATNESS_AND_FILTERED_CI.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not apply without saturation, a full generic binary-CI initial ideal, or actual two-equation global STCI."
  - "Movement zero and movement at least two are not excluded."
  - "An abstract bundle sequence does not establish global embedded realizability."
---

# Saturated actual-generator rigidity and movement-one exclusion

## Statement and hypotheses

The actual-generator sequence 0 -> T -> O(-4a)⊕O(-4b) -> R -> 0, where deg T=-7s+s*epsilon/r, is nonsplit; both original equations have exact generic normal order r, and no such STCI has epsilon=1. Necessary identities: ab=4rs, 4(a+b)=7(r+s)-epsilon(s-r)/r, r divides epsilon*s.

- Actual homogeneous complete intersection Y=V(F_a,G_b) with Y_red=C0
- Full generic ordinary initial ideal a coprime binary complete intersection of degrees 2<=r<s
- Actual first degree-r kernel R is a line subbundle (saturated); write R=O(-7r-epsilon), epsilon>=0

## Proof, verification, and acceptance

The generator-filtration quotient identifies the two original homogeneous equations with generators of the first-relation line, and R0010 provides the second quotient line. The independent audit verifies the nonsplitting argument, exact-order and joint-generation consequence, no-quadric-factor degree lower bound, and integral contradiction at epsilon one. The underlying graded-generator interface is preserved in the source and audited dependency note; its use here is reconstructed in the cited audit.

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above.

## Limitations

- Does not apply without saturation, a full generic binary-CI initial ideal, or actual two-equation global STCI.
- Movement zero and movement at least two are not excluded.
- An abstract bundle sequence does not establish global embedded realizability.

## Current proof navigation

The evidence paths above point directly to the retained mathematical proofs. Consolidation changes their location and incorporates reviewed corrections; the canonical statement and limitations remain unchanged. The [filtration chapter](../synthesis/03-infinitesimal-geometry.md) explains how these hypotheses differ from arbitrary STCI equations.
