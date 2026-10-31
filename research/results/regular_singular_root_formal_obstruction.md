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
  - "research/supplements/SATURATED_DUALITY_AND_MOVING_POWERS.md"
independent_audits:
  - "research/supplements/SATURATED_DUALITY_AND_MOVING_POWERS.md"
  - "research/supplements/SATURATED_DUALITY_AND_MOVING_POWERS.md"
accepted_in: "research/supplements/SATURATED_DUALITY_AND_MOVING_POWERS.md"
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

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above.

## Limitations

- Regularity of the entire formal lifted surface is essential, not automatic from Cartier lifting.
- No exclusion of singular formal surfaces, finite lifts, or arbitrary actual STCI equations is obtained.
- The suggested degree-e generalization is not part of this promotion.

## Current proof navigation

The evidence paths above point directly to the retained mathematical proofs. Consolidation changes their location and incorporates reviewed corrections; the canonical statement and limitations remain unchanged. The [filtration chapter](../synthesis/03-infinitesimal-geometry.md) explains how these hypotheses differ from arbitrary STCI equations.
