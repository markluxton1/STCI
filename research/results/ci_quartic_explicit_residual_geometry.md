---
id: STCI-R-0023
title: "Explicit quartic residual geometry"
kind: theorem
status: proved
scope:
  characteristic: "0"
  curve: "fixed C0"
  hypotheses:
    - "The explicit quartic pairs in the cited audits"
statement: "The (2,3) pair has a smooth degree-12 genus-16 residual; the (1,1) pair has a line and smooth degree-11 genus-12 residual."
dependencies:
  - STCI-R-0021
evidence:
  - "research/notes/2026-10-25-ci-cycle-smooth-residual-audit.md"
  - "research/notes/2026-10-25-ci-cycle-line-degeneration-audit.md"
independent_audits:
  - "research/notes/2026-10-25-ci-cycle-smooth-residual-audit.md"
  - "research/notes/2026-10-25-ci-cycle-line-degeneration-audit.md"
accepted_in: "research/PROMOTION_ADJUDICATION_CR06-08_CR12-14_2026-10-26.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Specific examples only"
---
# Explicit quartic residual geometry

## Statement
For the exact pair f_a=F+QH0+a*x0*A and g_b=G+QH1+b*x3*D3 defined in the linked audits, the (2,3) complete intersection is the scheme union of the fixed rational quartic C and a smooth geometrically integral degree-12 genus-16 residual D. Their intersection is 18 distinct transverse points avoiding both marked endpoints.

At (1,1), the residual is L union E, with L a line and E smooth geometrically integral of degree 11 and genus 12. There are five reduced transverse L-E attachments, seventeen C-E attachments and one C-L attachment, with no triple intersections.

## Hypotheses and quantifiers
Only the displayed rational equations and their algebraically closed characteristic-zero extensions.

## Proof outline
The independent audits verify exact ideal unions, saturation, Hilbert polynomials, Jacobian smoothness, geometric connectedness, and transverse attachments using rational Macaulay2 computations. Along the local moving-ruling divisor ab=1, each of the five residual-node smoothing parameters is a unit multiple of ab-1.

## Dependencies
The reference quartic forms appear in R-0021.

## Evidence and verification
See linked independent audits and their exact verifier scripts. No new replay was performed in this promotion turn.

## Consequences
Provides a concrete smooth residual and a five-node line degeneration.

## Limitations
No universal statement about quartic pairs or STCI.
