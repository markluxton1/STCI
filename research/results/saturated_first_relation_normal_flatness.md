---
id: STCI-R-0010
title: Saturated first relation forces ordinary normal flatness
kind: theorem
status: proved
scope:
  characteristic: "algebraically closed field of characteristic zero"
  curve: "smooth connected projective curve regularly embedded in a smooth threefold"
  hypotheses:
    - "Actual lci thickening Y with reduced support C"
    - "Full generic ordinary initial algebra is a coprime binary complete intersection of degrees 2 <= r < s"
    - "Actual degree-r first relation kernel is a line subbundle of Sym^r(N_C^*)"
statement: "All ordinary J-adic layers J^i/J^(i+1) are locally free on C and every graded fiber is a binary complete intersection of degrees (r,s)."
dependencies: []
evidence:
  - "research/supplements/SATURATED_DUALITY_AND_MOVING_POWERS.md"
independent_audits:
  - "research/supplements/NORMAL_FLATNESS_AND_FILTERED_CI.md"
  - "research/supplements/SATURATED_DUALITY_AND_MOVING_POWERS.md"
accepted_in: "research/supplements/NORMAL_FLATNESS_AND_FILTERED_CI.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not cover nonsaturated first relations, non-CI generic initial ideals, or residual curve components."
  - "Does not prove unrestricted STCI nonexistence."
  - "Equal degrees require the separate local theorem and its additional hypotheses."
---

# Saturated-first-relation normal flatness

Let C be a smooth connected projective curve in a smooth threefold X, Y an actual lci thickening supported on C, J=I_C O_Y, and E=N^*_(C/X). Suppose the **full** generic ordinary initial algebra is k(C)[u,v]/(f_r,g_s), where 2<=r<s and gcd(f_r,g_s)=1. Assume the actual kernel R=ker(Sym^r E -> J^r/J^(r+1)) is a line subbundle.

Then every J^i/J^(i+1) is locally free and every ordinary graded fiber is a binary complete intersection of degrees (r,s).

The proof saturates the J-filtration, uses perfect Gorenstein pairings to compute the second quotient relation T, and obtains a generically nonzero resultant in (det E)^(rs) tensor R^(-s) tensor T^(-r) of degree zero. Projectivity makes it nowhere zero. A top-socle pairing identifies the saturated graded algebra with the ordinary one. The second generator is a quotient relation; a global polynomial splitting is **not** assumed.

This strengthens the actual-CI bridge beyond smooth roots and balanced conormal bundles but does not supersede the separately scoped STCI-R-0006. The proof uses the saturated-duality lemma from the linked supporting note, with its independent audit.

## Combined consequence for C0

For the fixed rational quartic C0, when E=O(-7)^2 and the first root is moving, the uniform graded second quotient relation satisfies the hypotheses of STCI-R-0011. Therefore the **full** moving first root is reduced. This is conditional on the hypotheses above and does not constrain arbitrary STCI presentations.

## Current proof navigation

The evidence paths above point directly to the retained mathematical proofs. Consolidation changes their location and incorporates reviewed corrections; the canonical statement and limitations remain unchanged. The [filtration chapter](../synthesis/03-infinitesimal-geometry.md) explains how these hypotheses differ from arbitrary STCI equations.
