---
id: STCI-R-0018
title: "Regular formal surfaces cannot lift reduced movement-two singular roots"
kind: theorem
status: proved
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "fixed C0 and exceptional surface of its blowup"
  hypotheses:
    - "Full reduced finite-flat effective Cartier root Z of class (2,r), r>=2"
    - "Compatible all-orders embedded Cartier lifts define a formal surface regular at every point of the full Z"
statement: "No such all-orders formal Cartier lift exists. In particular, any surviving all-orders Cartier lift of a reduced singular movement-two root must have a singular formal surface at some point of that root."
dependencies:
  - STCI-R-0005
evidence:
  - "research/notes/2026-10-19-singular-root-investigation.md"
independent_audits:
  - "research/notes/2026-10-19-regular-singular-root-smoothing-audit.md"
  - "research/notes/2026-10-19-regular-reducible-root-independent-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-21.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Regularity of the entire formal lifted surface is essential, not automatic from Cartier lifting."
  - "No exclusion of singular formal surfaces, finite lifts, or arbitrary actual STCI equations is obtained."
  - "The suggested degree-e generalization is not part of this promotion."
---

# Regular formal surfaces cannot lift reduced movement-two singular roots

## Statement and hypotheses

No such all-orders formal Cartier lift exists. In particular, any surviving all-orders Cartier lift of a reduced singular movement-two root must have a singular formal surface at some point of that root.

- Full reduced finite-flat effective Cartier root Z of class (2,r), r>=2
- Compatible all-orders embedded Cartier lifts define a formal surface regular at every point of the full Z

## Proof, verification, and acceptance

The audit verifies p_*O_Z(7,-1)=O_P1(5)^r, generation and H1 vanishing, algebraization of an lci center, normalization preserving the formal regular branch, smoothing inside a smooth projective surface, and the contradictory ruled-model and plane-section numerical bounds. It explicitly checks use of singular-lci deformation references.

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above. Scope acceptance for this promotion is documented in [the reconciliation decision](../RECONCILIATION_2026-10-21.md); that decision does not replace the source proof.

## Limitations

- Regularity of the entire formal lifted surface is essential, not automatic from Cartier lifting.
- No exclusion of singular formal surfaces, finite lifts, or arbitrary actual STCI equations is obtained.
- The suggested degree-e generalization is not part of this promotion.
