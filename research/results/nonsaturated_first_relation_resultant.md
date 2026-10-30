---
id: STCI-R-0016
title: "Effective resultant budget for nonsaturated actual first relations"
kind: theorem
status: proved
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "smooth connected projective curve in smooth threefold"
  hypotheses:
    - "Actual lci thickening Y with unique reduced support C"
    - "Full generic ordinary initial algebra a coprime binary CI of degrees 2<=r<s"
    - "First actual kernel K_r=R(-D), R its line-subbundle saturation, D effective; saturated filtration and generation lengths c_j as in source"
statement: "The quotient-relation resultant defines an effective divisor Delta supported on first-relation saturation defects, with deg Delta=(r-1)c_(s-1)-r*c_s and 0<=deg Delta<=(r-1)*binom(s-r,2)*length(D). For gaps s-r<=2 normal flatness follows, without assuming the first kernel is saturated."
dependencies:
  - STCI-R-0010
  - STCI-R-0011
evidence:
  - "research/notes/2026-10-19-first-relation-defect-investigation.md"
  - "research/notes/2026-10-19-filtered-generic-ci-normal-flatness.md"
  - "research/notes/2026-10-19-filtered-saturated-duality-moving-purepower-bridge.md"
independent_audits:
  - "research/notes/2026-10-19-first-relation-defect-independent-audit.md"
  - "research/notes/2026-10-19-filtered-local-normal-flatness-independent-audit.md"
  - "research/notes/2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-21.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "The formula is conditional on full generic binary CI and actual lci with unique support; it is not a general STCI obstruction."
  - "Nonsaturated roots may pay an effective degeneration divisor, rather than being excluded."
  - "Local gap-three counterexamples do not establish global homogeneous examples."
  - "R0010 is a comparison/special case, not an input establishing the nonsaturated resultant formula; R0011 is used only for the optional repeated-root strengthening."
---

# Effective resultant budget for nonsaturated actual first relations

## Statement and hypotheses

The quotient-relation resultant defines an effective divisor Delta supported on first-relation saturation defects, with deg Delta=(r-1)c_(s-1)-r*c_s and 0<=deg Delta<=(r-1)*binom(s-r,2)*length(D). For gaps s-r<=2 normal flatness follows, without assuming the first kernel is saturated.

- Actual lci thickening Y with unique reduced support C
- Full generic ordinary initial algebra a coprime binary CI of degrees 2<=r<s
- First actual kernel K_r=R(-D), R its line-subbundle saturation, D effective; saturated filtration and generation lengths c_j as in source

## Proof, verification, and acceptance

The principal formula uses the separately proved saturated Gorenstein-duality and local exact-order normal-flatness lemmas listed as evidence, not R0010 applied to a nonsaturated first relation. R0010 is a comparison theorem for the zero-defect saturated case; R0011 enters only the additional repeated-root payment argument. Saturated Gorenstein duality computes the quotient relation line and the degree of its resultant section; the independent audit reconstructs the defect sheaves, signs, support and gap-two local classification. The source separately supplies the stronger pure-power defect payment with the denominator restriction s-r>=2. R0010 covers the zero-defect saturated special case; this record does not weaken its assumptions.

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above. Scope acceptance for this promotion is documented in [the reconciliation decision](../RECONCILIATION_2026-10-21.md); that decision does not replace the source proof.

## Limitations

- The formula is conditional on full generic binary CI and actual lci with unique support; it is not a general STCI obstruction.
- Nonsaturated roots may pay an effective degeneration divisor, rather than being excluded.
- Local gap-three counterexamples do not establish global homogeneous examples.

## Permanent evidence navigation

The `research/notes/` metadata preserves original provenance identifiers rather than live branch paths. The [consolidated subject chapter](../synthesis/03-infinitesimal-geometry.md) provides a current entry point to the mathematical argument and its retained detailed supplements. This route does not alter the record's hypotheses, proof status, or historical audit identity.
