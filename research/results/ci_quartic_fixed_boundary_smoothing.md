---
id: STCI-R-0024
title: "Independent residual-node smoothing at fixed boundary"
kind: theorem
status: proved
scope:
  characteristic: "0"
  curve: "fixed C0"
  hypotheses:
    - "The (1,1) quartic pencil and five residual nodes of R-0023"
statement: "The fixed-boundary Grassmannian fiber is smooth of dimension 14 and admits five independent formal and etale-local residual-node smoothing parameters."
dependencies:
  - STCI-R-0023
evidence:
  - "research/synthesis/fixed_boundary_smoothing.md"
  - "research/computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py"
  - "research/computations/ci_fixed_boundary_node_smoothing_2026_10_25.json"
independent_audits:
  - "research/synthesis/fixed_boundary_smoothing.md"
accepted_in: "research/results/ci_quartic_fixed_boundary_smoothing.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "No explicit polynomial coefficient arc"
  - "Local statement for the specified pencil"
---
# Fixed-boundary smoothing of five residual nodes

## Statement
At the (1,1) pencil in R-0023, the affine boundary, node, and joint tangent maps on the 36-dimensional ordered quartic source have respective ranks 19, 5, and 24. After passing to the Grassmannian of pencils, the projective boundary rank is 18, so the fixed-boundary fiber is smooth of dimension 14. After splitting and labeling the five nodes, its completed local ring is k[[tau1,tau2,tau3,tau4,tau5,z1,...,z9]], with tau_i independent node-smoothing parameters.

## Hypotheses and quantifiers
The specified characteristic-zero pencil, after splitting the geometric nodes and etale localization.

## Proof outline
Exact rational matrices from global quartic equations yield ranks (19,5,24) and five explicit tangent witnesses. The GL2 quotient removes one scalar boundary direction without affecting node smoothing. Standard flat nodal-family charts and formal inverse-function theory lift these independent tangent classes to formal and etale-local smoothing coordinates.

## Dependencies
R-0023 supplies the residual geometry and five nodes.

## Evidence and verification
The independent audit reconstructs the matrices and checks the formal-local interpretation. Saved Python verifier and JSON give reproducible witnesses. The inherited exact verifier was not rerun in this consolidation.

## Consequences
Residual nodes can be smoothed independently with the attachment divisor exactly fixed, locally.

## Limitations
No explicit polynomial or rational coefficient arc, nor universal theorem for all quartic pairs.

## Current proof home

The complete consolidated proof and its exact qualifications are in [the mathematical account](../synthesis/fixed_boundary_smoothing.md). Inherited review covers unchanged proofs. Independent consolidation review reconstructed the replacement, checked scope and dependencies, and accepted the replacement and bounded source removals; no new inherited CAS execution was required.
