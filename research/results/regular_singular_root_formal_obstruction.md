---
id: STCI-R-0018
title: "Regular formal surfaces cannot lift reduced movement-two singular roots"
kind: theorem
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
  - "research/arguments/spectral/spectral_pushforward_powers.md#saturated-duality-root-descent-and-embedded-formal-surfaces"
independent_audits:
  - "research/arguments/spectral/spectral_pushforward_powers.md#saturated-duality-root-descent-and-embedded-formal-surfaces"
  - "research/arguments/spectral/spectral_pushforward_powers.md#saturated-duality-root-descent-and-embedded-formal-surfaces"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Regularity of the entire formal lifted surface is essential, not automatic from Cartier lifting."
  - "No exclusion of singular formal surfaces, finite lifts, or arbitrary actual STCI equations is obtained."
  - "The suggested degree-e generalization is not included in this result."
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
- The suggested degree-e generalization is not included in this result.
