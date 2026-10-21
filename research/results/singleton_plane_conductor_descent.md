---
id: STCI-R-0017
title: "Degree-sixteen singleton plane projection family without mates"
kind: theorem
status: proved
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "fixed C0 in P3"
  hypotheses:
    - "Basepoint-free plane map [s^4:s^3t:st^3+alpha*z^4:t^4+zP_3(s,t,z)], alpha nonzero"
    - "For normalization statement, A_3 or C_1 coefficient of P_3 is nonzero, ensuring birationality"
statement: "The specified birational open family gives finite normalizations P2 -> integral degree-sixteen carrier surfaces with full reduced inverse support of C0 equal to z=0, but none admits an ambient homogeneous mate of positive degree. A broader two-fixed-coordinate full-singleton sublane has the same no-mate property."
dependencies: ["STCI-R-0002","STCI-R-0003"]
evidence:
  - "research/notes/2026-10-19-singleton-projection-investigation.md"
independent_audits:
  - "research/notes/2026-10-19-singleton-plane-projection-independent-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-21.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not exclude every degree-sixteen plane-normalization projection or every Cartier singleton model."
  - "For nonbirational parameter values the image does not give an additional degree-sixteen normalization."
  - "Reduced inverse support alone does not imply conductor descent."
---

# Degree-sixteen singleton plane projection family without mates

## Statement and hypotheses

The specified birational open family gives finite normalizations P2 -> integral degree-sixteen carrier surfaces with full reduced inverse support of C0 equal to z=0, but none admits an ambient homogeneous mate of positive degree. A broader two-fixed-coordinate full-singleton sublane has the same no-mate property.

- Basepoint-free plane map [s^4:s^3t:st^3+alpha*z^4:t^4+zP_3(s,t,z)], alpha nonzero
- For normalization statement, A_3 or C_1 coefficient of P_3 is nonzero, ensuring birationality

## Proof, verification, and acceptance

The audit reconstructs basepoint freedom, finiteness, birationality, exact inverse support, the all-degree derivative contradiction, and the broader two-fixed-coordinate boundary case. The obstruction detects a first-order nilpotent conductor term invisible in reduced residue data. The general question STCI-Q-0001 remains open.

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above. Scope acceptance for this promotion is documented in [the reconciliation decision](../RECONCILIATION_2026-10-21.md); that decision does not replace the source proof.

## Limitations

- Does not exclude every degree-sixteen plane-normalization projection or every Cartier singleton model.
- For nonbirational parameter values the image does not give an additional degree-sixteen normalization.
- Reduced inverse support alone does not imply conductor descent.
