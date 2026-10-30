---
id: STCI-R-0021
title: "Four-component mu4 degeneration of the explicit quartic intersection"
kind: theorem
status: proved
scope:
  characteristic: "0 and 2"
  curve: "fixed C0 and the prescribed equations F=x1^4-x0^3*x3, G=x2^4-x0*x3^3"
  hypotheses:
    - "Geometric fibers; characteristic-zero statement after adjoining fourth roots of unity"
statement: "The complete intersection is flat over Z; away from endpoints it is G_m times mu_4. In characteristic zero it is the reduced union of four degree-four curves, whereas in characteristic two its reduced support is C0 with generic transverse length four."
dependencies: []
evidence:
  - "research/notes/2026-10-23-quartic-characteristic-conormal.md"
  - "research/computations/verify_44_mu4_family_2026_10_23.m2"
independent_audits:
  - "research/notes/2026-10-23-quartic-geometry-symbol-independent-audit.md"
accepted_in: "research/RECONCILIATION_2026-10-23-44.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Specific equations only; not a universal classification of characteristic-two STCI equations."
---
# Four-component mu4 degeneration

## Statement
For F=x1⁴−x0³x3 and G=x2⁴−x0x3³, the projective intersection is flat over Z. On the dense torus it is G_m×mu_4. Over an algebraically closed characteristic-zero field its four distinct components are C_zeta=[s⁴:s³t:zeta st³:t⁴], zeta⁴=1, meeting at the two endpoints. In characteristic two the reduced support is exactly C0, and the generic transverse algebra is k(C0)[Y]/(Y⁴).

## Hypotheses and quantifiers
This is the behavior of this prescribed pair, not every (4,4) pair.

## Proof outline
The homogeneous quotient is free over Z[x0,x3] on monomials x1^a x2^b (0≤a,b<4). On x0=1, eliminating X=x3−u⁴ leaves P(Y)=(u³+Y)⁴−u¹². Substitution Y=u³(z−1) gives u¹²(z⁴−1). The second endpoint chart and complete-intersection purity establish the global support claims.

## Dependencies
No quartic-carrier nonexistence theorem is used.

## Evidence and verification
The Macaulay2 certificate and independent audit are linked above. Clean [GitHub Actions run 39972680627](https://github.com/markluxton1/STCI/actions/runs/39972680627) passed the Macaulay2 job.

## Consequences
The four characteristic-zero components coalesce into a single nonreduced support in characteristic two; the full initial ideal acquires the order-four generator.

## Limitations
This does not imply arbitrary characteristic-zero quartic pairs have four components.

## Permanent evidence navigation

The `research/notes/` metadata retains original provenance identifiers, not current-tree paths. For mathematical exposition and the linked detailed source supplements, consult [the consolidated subject chapter](../synthesis/01-marked-quartic.md). Historical identifiers remain unchanged; the theorem's hypotheses and status are not expanded.
