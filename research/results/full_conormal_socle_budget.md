---
id: STCI-R-0032
title: Full conormal filtration and socle budget
kind: theorem
status: proved
scope:
  characteristic: "any characteristic with valid conormal quotient degree bounds"
  curve: "smooth integral curve C in P3"
  hypotheses:
    - "Actual complete intersection Y with reduced support C"
    - "Valid degree bound for torsion-free symmetric conormal quotients"
statement: "The full socle and conormal filtration identity n(lambda*d-L)=lambda*(n*d-2*M)+2*Delta holds, including intermediate torsion."
dependencies: []
evidence:
  - research/notes/2026-10-13-evening-entirely-thick-rees-progress.md
independent_audits:
  - research/notes/2026-10-13-generalization-socle-independent-audit.md
accepted_in: research/HISTORICAL_STRUCTURAL_ADJUDICATION_2026-10-26.md
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Necessary condition only; does not resolve unrestricted STCI"
---

# Full conormal filtration and socle budget

Let C have degree e and genus g, and let Y=V(F_a,G_b) be an actual complete intersection with reduced support C. Write J=I_C O_Y, n=ab/e, d for the generic Loewy index, h_j for the ranks of J^j/J^(j+1), M=sum(j*h_j), and L=e(a+b-4)-(2g-2). Let lambda be a valid conormal quotient degree bound and Delta the total corrected normal-layer degree and torsion defect. Then

    n(lambda*d-L)=lambda*(n*d-2*M)+2*Delta.

The actual socle is omega_C tensor O_C(4-a-b). In particular lambda*d>=L. Equality gives globally Gorenstein graded self-duality; identifying a constant algebra requires the additional balanced rational hypothesis.

The [original proof](../notes/2026-10-13-evening-entirely-thick-rees-progress.md), [independent audit](../notes/2026-10-13-generalization-socle-independent-audit.md), and [acceptance decision](../HISTORICAL_STRUCTURAL_ADJUDICATION_2026-10-26.md) delimit the claim. No general STCI exclusion follows.