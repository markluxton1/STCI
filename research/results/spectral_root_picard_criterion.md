---
id: STCI-R-0008
title: Spectral root-curve Picard criterion for a graded second relation
kind: theorem
status: proved
scope:
  characteristic: "algebraically closed field"
  curve: "smooth projective curve with split rank-two conormal E=H^-1 tensor V"
  hypotheses:
    - "Saturated first relation R=H^-r tensor M in Sym^r(E), with M a line subbundle of Sym^r(V)"
    - "Second relation is a line in the quotient by the first relation, not necessarily a global polynomial line"
    - "Fiberwise coprimality of first and second graded relations"
statement: "A degree-s second quotient relation coprime in every fiber exists iff the direction line bundle O_Z(s) descends from the base along the full finite flat root scheme Z, including nilpotents."
dependencies: []
evidence:
  - "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-spectral-root-curve-relations.md"
independent_audits:
  - "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-spectral-root-curve-independent-audit.md"
accepted_in: "https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-spectral-root-curve-independent-audit.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Constructs abstract graded families, not actual formal neighborhoods or ambient complete intersections."
  - "Root scheme may be singular or nonreduced; the full Picard group is essential."
  - "Numerical divisibility is not sufficient without torsion in Pic(Z)."
---

# Spectral root-curve criterion for a graded second relation

## Statement

Let C be a smooth integral projective curve over an algebraically closed field, E=H^-1 tensor V its conormal bundle with V a constant two-dimensional vector space. Suppose the first saturated normal relation is a line subbundle R=H^-r tensor M in Sym^r(E), r>=2, where M is a line subbundle of Sym^r(V).

The corresponding binary form defines a divisor Z in C x P(V*), finite flat of degree r over C. This includes repeated roots and nonreduced Z. Write pi:Z->C and let O_Z(1) denote the direction-ruling line bundle.

For s>r, a **second relation in the quotient by the first relation** exists and is coprime to the first in every fiber if and only if there is a line bundle N on C such that

    O_Z(s) is isomorphic to pi^*N.

Equivalently, the class of O_Z(1) in Pic(Z)/pi^*Pic(C) is killed by s. This is a necessary and sufficient condition for the corresponding abstract graded Artin complete-intersection family with regular-sequence fiber ideals (f_r,g_s). It is **not** a criterion for lifting that family to the actual formal neighborhood or for a projective STCI.

## Rational base and torsion arithmetic

For C=P1 and M=O(-epsilon), the root Z has bidegree (epsilon,r). Put d=gcd(r,epsilon), r0=r/d, epsilon0=epsilon/d. The descent condition is equivalent to

    r0 divides s, and
    [O_Z(r0) tensor pi^*O(-epsilon0)]^(s/r0) is trivial in Pic(Z).

If the displayed line bundle has order t, the possible second degrees are precisely positive multiples of r0*t that exceed r. If it has infinite order, no fiberwise coprime graded second relation exists. This retains the full Picard group of nonreduced root schemes.

For epsilon>0, the second quotient relation **cannot generally be represented by a global second polynomial line**: the relevant generator extension is nonsplit. Assuming such a lift would incorrectly discard valid abstract graded families.

## Relationship to the ambient obstruction model

This is a graded/spectral criterion, logically separate from the actual exceptional-neighborhood obstruction. In particular, the smooth torsion-two seed in [STCI-R-0007](quadratic_root_obstruction_model.md) satisfies the first ambient compatibility and spectral torsion conditions but has a nonzero second ambient obstruction. Thus graded torsion does not imply ambient liftability.

The spectral criterion covers singular and nonreduced root schemes; [STCI-R-0005](smooth_root_formal_obstruction.md) concerns smooth roots only. Their hypotheses should not be conflated.

## Evidence

- [Original spectral root-curve proof](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-spectral-root-curve-relations.md).
- [Independent spectral audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-spectral-root-curve-independent-audit.md).

The proofs and audit remain preserved on the Ultra branch; no new proof or ambient existence claim is asserted.
