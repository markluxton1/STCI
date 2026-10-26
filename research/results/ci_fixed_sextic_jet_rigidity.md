---
id: STCI-R-0025
title: "Fixed sextic jet rigidity and residual-degree obstruction"
kind: theorem
status: proved
scope:
  characteristic: "0"
  curve: "fixed C0"
  hypotheses:
    - "The selected sextic Fstar and proper degree-sixteen mates"
statement: "For the selected Fstar, the degree-sixteen order-twelve jet kernel is Fstar times degree-ten forms; every proper degree-sixteen mate has generic multiplicity at most 22 and residual cycle degree at least eight."
dependencies: []
evidence:
  - "research/CR09_CERTIFICATE_INSPECTION_2026-10-26.md"
  - "research/notes/2026-10-26-endpoint4-nonsplit-node-scope-audit.md"
  - "research/computations/endpoint4_fixed_m2_2026_10_25.m2"
  - "research/computations/endpoint4_fixed_m2_2026_10_25.json"
  - "research/computations/endpoint4_fixed_jet_independent_2026_10_26.py"
  - "research/computations/endpoint4_fixed_jet_independent_2026_10_26.json"
independent_audits:
  - "research/CR09_CERTIFICATE_INSPECTION_2026-10-26.md"
  - "research/notes/2026-10-26-endpoint4-nonsplit-node-scope-audit.md"
accepted_in: "research/CR09_CERTIFICATE_INSPECTION_2026-10-26.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Only one selected sextic and degree-sixteen mates"
  - "Saved computational certificates source-inspected, not freshly rerun"
  - "Bound not claimed sharp"
---
# Fixed sextic jet rigidity

## Statement
Put q=x0*x3-x1*x2 and D=x2^3-x1*x3^2, and define Fstar=-q^2*x3^2-q*D*x2+D^2/4+q^3. For a degree-sixteen global G, membership of its generic normal jet in (Fstar)+(u,v)^12 forces G=Fstar*H10. For every proper degree-sixteen complete intersection (Fstar,G) containing C0, its generic multiplicity is even and at most 22; its residual fundamental cycle has degree at least eight.

## Hypotheses and quantifiers
Algebraically closed characteristic-zero base field, this particular Fstar, and degree-sixteen mates only.

## Proof outline
The quadratic normal form has nonsquare discriminant class 1+z^2 over k(z). The conjugate branches have equal intersection order n, giving generic multiplicity 2n and jet membership modulo (Fstar)+(u,v)^n. The saved finite-field 690-by-969 jet matrix has rank 683 and annihilates all 286 independent global multiples. Normal division and good-specialization rank lifting prove the characteristic-zero kernel identity. A proper mate cannot have n at least twelve. Thus m_C=2n at most 22, and Bezout gives residual degree 96-4*m_C at least eight.

## Dependencies
The nonsplit-node finite-length lemma and audited global jet certificate, both detailed in the source notes.

## Evidence and verification
Two separately implemented saved computations corroborate rank 683 and annihilation of the multiples. Sources and outputs were inspected, but no fresh execution or independently archived nonzero maximal minor was performed for this promotion.

## Consequences
No proper degree-sixteen mate for this selected sextic has sole reduced support C0.

## Limitations
No general sextic or unrestricted STCI theorem.
