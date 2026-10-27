---
id: STCI-R-0011
title: Moving nonreduced spectral roots obstruct Picard descent
kind: theorem
status: proved
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "rational base P1 with full finite-flat root divisor in P1 x P1"
  hypotheses:
    - "Root divisor Z has class (epsilon,r), epsilon>0 and r>=2"
    - "For some s>0, O_Z(0,s) descends from the base: O_Z(0,s) is isomorphic to pi^*O(n)"
statement: "The full root divisor Z is reduced; each irreducible component has bidegree t_i(epsilon/g,r/g), where g=gcd(epsilon,r), t_i>0 and sum t_i=g."
dependencies:
  - STCI-R-0008
evidence:
  - "research/notes/2026-10-19-spectral-nonreduced-root-obstruction.md"
independent_audits:
  - "research/notes/2026-10-19-spectral-nonreduced-root-independent-audit.md"
accepted_in: "research/notes/2026-10-19-spectral-nonreduced-root-independent-audit.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Moving means epsilon>0; constant repeated roots are not excluded."
  - "Special fibers can have nonreduced fibers even when the total divisor is reduced."
  - "Reduced singular roots and gluing of multiple components remain possible."
  - "Does not by itself establish ambient liftability or unrestricted STCI nonexistence."
---

# Moving nonreduced spectral-root obstruction

Let Z be a full finite-flat effective Cartier root divisor of class (epsilon,r) in P1_base x P1_direction, with epsilon>0. If O_Z(0,s) is pulled back from the base for some s>0, then Z is reduced.

The geometric lemma is injectivity of Pic(P1 x P1) -> Pic(2D) for any effective divisor D of strictly positive bidegrees. A trivialization modulo I_D^2 kills the ambient restricted logarithmic Chern class; H^1(Omega^1(-D))=0 gives injectivity on H^1(Omega^1), which detects both ruling degrees in characteristic zero. A repeated moving component would contain 2D and contradict this lemma.

Writing g=gcd(epsilon,r), each irreducible component has class t_i(epsilon/g,r/g), with positive t_i summing to g. For epsilon=2, the only possibilities are an integral reduced (2,r) divisor, or (if r is even) two distinct smooth rational (1,r/2) components. This is a necessary restriction, not a sufficient criterion for descent.

STCI-R-0008 provides the abstract graded Picard-descent interface. STCI-R-0010 supplies the bridge for **actual** lci thickenings under its separate saturated-first-relation and full generic-CI hypotheses. Neither theorem implies that every actual STCI has those hypotheses.
