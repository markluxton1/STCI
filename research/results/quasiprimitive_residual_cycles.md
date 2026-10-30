---
id: STCI-R-0019
title: "Saturated quasiprimitive residual intersection cycle and first-normal defect bound"
kind: theorem
status: proved
scope:
  characteristic: "arbitrary for the local determinant and first-normal bound; quartic application characteristic zero"
  curve: "smooth reduced support curve; arbitrary smooth ambient threefold locally"
  hypotheses:
    - "Finite-flat curvilinear generic algebra K[y]/(y^m) with saturated order flag and invertible quotients E_i=L^i(D_i), D0=D1=0"
    - "For cycle identity: smooth auxiliary surface Q containing C, nonzero generic first class of its local equation, and proper residual intersection of restrictions"
    - "For A<=D_(m-1): the first-normal image and primitive horizontal kernel as defined in source"
statement: "For q with nonzero generic first class, length tors(B/qB)=(m-1)ord(q_1)+ord(D_(m-1)); globally the proper residual zero-cycle satisfies [rho cap sigma]=(m-1)T+D_(m-1), and the first-normal divisor satisfies A<=D_(m-1) coefficientwise."
dependencies: []
evidence:
  - "research/notes/2026-10-05-residual-cycle.md"
independent_audits:
  - "research/notes/2026-10-05-residual-cycle-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-21.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "All identities are length cycles or divisor inequalities, not scheme or ideal equalities."
  - "Unsaturated ordinary associated gradeds and improper residual intersections are outside the claim."
  - "Historical quartic (4,b) applications remain illustrations, not open mate cases after STCI-R-0001."
  - "Vertical exceptional cycles are not residual curves downstairs."
---

# Saturated quasiprimitive residual intersection cycle and first-normal defect bound

## Statement and hypotheses

For q with nonzero generic first class, length tors(B/qB)=(m-1)ord(q_1)+ord(D_(m-1)); globally the proper residual zero-cycle satisfies [rho cap sigma]=(m-1)T+D_(m-1), and the first-normal divisor satisfies A<=D_(m-1) coefficientwise.

- Finite-flat curvilinear generic algebra K[y]/(y^m) with saturated order flag and invertible quotients E_i=L^i(D_i), D0=D1=0
- For cycle identity: smooth auxiliary surface Q containing C, nonzero generic first class of its local equation, and proper residual intersection of restrictions
- For A<=D_(m-1): the first-normal image and primitive horizontal kernel as defined in source

## Proof, verification, and acceptance

The independent determinant audit chooses a saturated DVR-adapted basis, computes a triangular nonzero minor for multiplication by q and telescopes valuations. Cancellation on Q and finite flatness identify the torsion quotient with the proper residual intersection, yielding the pointwise cycle formula. A conormal quotient argument bounds A. The local determinant and bound generalize beyond quartic carriers; the explicit classes, bidegrees, and historical numerical consequences on the unique quadric do not.

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above. Scope acceptance for this promotion is documented in [the reconciliation decision](../RECONCILIATION_2026-10-21.md); that decision does not replace the source proof.

## Limitations

- All identities are length cycles or divisor inequalities, not scheme or ideal equalities.
- Unsaturated ordinary associated gradeds and improper residual intersections are outside the claim.
- Historical quartic (4,b) applications remain illustrations, not open mate cases after STCI-R-0001.
- Vertical exceptional cycles are not residual curves downstairs.

## Permanent evidence navigation

Historical `research/notes/` identifiers in the metadata are preserved for provenance. The permanent [subject synthesis](../synthesis/05-exclusions.md) provides navigation to the mathematical arguments and their detailed supplements. This addition does not change any theorem or audit claim.
