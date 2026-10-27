---
id: STCI-R-0029
title: "Arithmetic ruled four-section family"
kind: theorem
status: proved
scope:
  characteristic: "mixed over Z localized at 2"
  curve: "fixed prescribed quartic family"
  hypotheses:
    - "The explicit arithmetic cone and four-section divisor"
statement: "The prescribed arithmetic ruled model has the normalization, conductor, flat four-section, special-fiber and endpoint behaviors recorded below."
dependencies:
  - STCI-R-0021
evidence:
  - "research/notes/2026-10-24-ruled-surfaces-arithmetic.md"
independent_audits:
  - "research/notes/2026-10-24-four-sheet-arithmetic-independent-audit.md"
accepted_in: "research/PROMOTION_ADJUDICATION_CR32-37_2026-10-26.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "The fixed arithmetic family only"
  - "No general lifting theorem"
---
# Arithmetic ruled four-section family

## Statement
Over A=Z localized at 2, the cone x1^4=x0^3*x3 has finite normalization P_A(1,1,4) and ruled resolution F4. The full homogeneous conductor is (x0,x1)^2, whose extension on F4 is O(-2E-6fInfinity). The prescribed four-section divisor is relative effective Cartier and finite flat of degree four over P1_A, with pushforward module O plus O(-4) plus O(-8) plus O(-12).

The characteristic-zero sections meet pairwise in 3p0+pInfinity; the characteristic-two fiber is a fourth Cartier multiple of one section. The mu4 orbit has this divisor as scheme image, but scheme image fails to commute with restriction to the endpoint. Over A[i], the vertical intersection coefficients for adjacent and opposite roots are one and two.

The ruled-to-projective map is finite; at infinity pairwise intersection lengths are one upstairs and three downstairs. The total normalization of the reduced arithmetic four-section family has two P1 components over A and one over A[i]; its special fiber differs from normalization of the reduced special curve. Three graph-pencil blowups at p0 and one at pInfinity separate characteristic-zero sections while leaving the characteristic-two group-scheme multiplicity. The multiplier scheme lambda^2+4lambda+1=0 is finite flat of degree two over A, not generically a subgroup.

## Hypotheses and quantifiers
Only this explicit arithmetic family, its ruled model and indicated base changes.

## Proof outline
Graded normalization, conductor calculations, Cartier finite flatness, root-valuations, explicit endpoint rings, and graph blowups.

## Dependencies
R-0021 records the related projective complete-intersection degeneration; its flatness is not inferred from the Cartier divisor alone.

## Evidence and verification
Written calculations and independent arithmetic audit, without a fresh execution in this promotion.

## Consequences
Distinguishes specialization of a finite flat divisor, normalization of the total space, and normalization of a special fiber.

## Limitations
No unrestricted characteristic-two lifting or STCI theorem.
