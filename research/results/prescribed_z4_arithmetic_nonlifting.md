---
id: STCI-R-0012
title: "Prescribed characteristic-two Z4 has no flat embedded lift over Z_(2) or Z_2"
kind: theorem
status: proved
scope:
  characteristic: "special fiber F2; bases Z_(2) and Z_2"
  curve: "fixed relative rational quartic [s^4:s^3t:st^3:t^4] in P3_R"
  hypotheses:
    - "Flat embedded subscheme over R=Z_(2) or Z_2"
    - "Special embedded fiber is precisely V(x1^4-x0^3*x3,x2^4-x0*x3^3)"
    - "Generic reduced support is the fixed relative quartic over Frac(R)"
statement: "No such flat embedded family exists; every hypothetical family forces a primitive triple whose obstruction in H^1(P1_R,O(-4)) has middle Laurent coefficient congruent to 2 modulo 4."
dependencies: []
evidence:
  - "research/notes/2026-10-20-z4-characteristic-zero-lifting-report.md"
  - "research/notes/2026-10-20-z4-local-structure.md"
  - "research/notes/2026-10-20-z4-ci-deformation-lemma.md"
  - "research/notes/2026-10-20-z4-quartic-obstruction.md"
independent_audits:
  - "research/notes/2026-10-20-z4-lift-independent-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-21.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not rule out characteristic-zero STCI or arbitrary characteristic-zero multiplicity-four schemes."
  - "Does not cover arbitrary ramified DVRs of residue characteristic two."
  - "Does not imply that the prescribed characteristic-two ribbon itself fails to lift."
---

# Prescribed characteristic-two Z4 has no flat embedded lift over Z_(2) or Z_2

## Statement and hypotheses

No such flat embedded family exists; every hypothetical family forces a primitive triple whose obstruction in H^1(P1_R,O(-4)) has middle Laurent coefficient congruent to 2 modulo 4.

- Flat embedded subscheme over R=Z_(2) or Z_2
- Special embedded fiber is precisely V(x1^4-x0^3*x3,x2^4-x0*x3^3)
- Generic reduced support is the fixed relative quartic over Frac(R)

## Proof, verification, and acceptance

The source proves persistence of the global quartic complete-intersection equations under flat embedded deformation, containment of the fourth ideal power and forced primitive intermediate stages. An integral two-chart calculation then produces the universal middle Laurent coefficient `C2=(b-d)(4ah+3b^2-8bd+6d^2)=2 (mod 4)` for all permitted quotient directions and quadratic corrections. The independent audit reconstructs these reductions and checks the integer and Macaulay2 certificates. This is an arithmetic nonlifting result, logically independent of STCI-R-0001.

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above. Scope acceptance for this promotion is documented in [the reconciliation decision](../RECONCILIATION_2026-10-21.md); that decision does not replace the source proof.

## Limitations

- Does not rule out characteristic-zero STCI or arbitrary characteristic-zero multiplicity-four schemes.
- Does not cover arbitrary ramified DVRs of residue characteristic two.
- Does not imply that the prescribed characteristic-two ribbon itself fails to lift.
