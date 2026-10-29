---
id: STCI-R-0014
title: "Six necessary movement-two numerical rows"
kind: reduction
status: exact_reduction
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "fixed C0 in P3"
  hypotheses:
    - "All hypotheses of STCI-R-0013"
    - "Movement epsilon=2"
statement: "The unordered necessary numerical quadruples (r,s;a,b) are exactly (2,8;8,8), (2,12;6,16), (6,21;18,28), (14,42;48,49), (15,45;50,54), (20,60;64,75). These are necessary arithmetic candidates, not geometric STCI realizations."
dependencies:
  - STCI-R-0001
  - STCI-R-0008
  - STCI-R-0010
  - STCI-R-0011
  - STCI-R-0013
evidence:
  - "research/notes/2026-10-19-global-ci-filtration-investigation.md"
independent_audits:
  - "research/notes/2026-10-19-numerical-first-root-independent-audit.md"
  - "research/notes/2026-10-19-global-ci-filtration-independent-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-21.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not exhaust arbitrary characteristic-zero STCI pairs."
  - "Picard descent, singular full roots, formal lifting, and actual homogeneous equations remain untested for the rows."
  - "STCI-R-0011 ensures reduction of moving full roots only under its own Picard-descent interface."
---

# Six necessary movement-two numerical rows

## Statement and hypotheses

The unordered necessary numerical quadruples (r,s;a,b) are exactly (2,8;8,8), (2,12;6,16), (6,21;18,28), (14,42;48,49), (15,45;50,54), (20,60;64,75). These are necessary arithmetic candidates, not geometric STCI realizations.

- All hypotheses of STCI-R-0013
- Movement epsilon=2

## Geometric interpretation of movement and saturation

The integer `epsilon` is not an arbitrary search parameter. Since
`N_C^* = O_{P^1}(-7)^{\oplus 2}`, a saturated first-relation line
`R = O_{P^1}(-7r-epsilon) -> Sym^r N_C^*`
defines a basepoint-free coefficient morphism
`phi: C = P^1 -> P(Sym^r k^2) = P^r` with
`phi^* O_{P^r}(1) = O_{P^1}(epsilon)`.
Equivalently, the first normal-root divisor in the projectivized normal-direction
bundle `P^1_base x P^1_direction` has bidegree `(epsilon,r)`,
where the first entry denotes degree over the base coordinate and the
second denotes degree in the normal-direction coordinate. Thus
`epsilon=2` means **quadratic variation of the first normal-root
divisor along C**; it is not a bound on the number of singular roots.

Distinguish two independent conditions. A full *generic* binary-CI
initial ideal over `k(C)` only ensures coprimality at the generic point;
it does not prevent the first relation's coefficient vector from
vanishing at special points. Saturation excludes those base points
(and corresponding torsion in the quotient of the first-relation
line inside `Sym^r N_C^*`). It does **not** exclude collisions or
multiple roots of the nonzero binary form, nor does it by itself ensure
that two specialized initial forms remain coprime at every point.
The latter is a separate resultant/specialization issue.

The six rows classify necessary numerical possibilities only for
actual homogeneous STCI pairs with the full generic coprime binary-CI
initial ideal, saturated first relation, `2 <= r < s`, and a
bidegree-`(2,r)` first normal-root divisor. No reduction from an
arbitrary STCI presentation to this class is known here.

## Proof, verification, and acceptance

The audit verifies global degree and first-blowup inequalities and a complete signed-divisor/discriminant argument; the exact Python arithmetic verifier cross-checks the finite candidate list but is not used in place of an exhaustion proof.

Full proofs and their recorded independent reconstruction reside in the linked evidence and audits above. Scope acceptance for this promotion is documented in [the reconciliation decision](../RECONCILIATION_2026-10-21.md); that decision does not replace the source proof.

## Limitations

- Does not exhaust arbitrary characteristic-zero STCI pairs.
- Picard descent, singular full roots, formal lifting, and actual homogeneous equations remain untested for the rows.
- STCI-R-0011 ensures reduction of moving full roots only under its own Picard-descent interface.
