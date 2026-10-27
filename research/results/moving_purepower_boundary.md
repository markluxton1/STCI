---
id: STCI-R-0009
title: Moving pure-power relation tower and unavoidable second-relation degeneration
kind: theorem
status: proved
scope:
  characteristic: "zero"
  curve: "smooth curve in a smooth threefold with balanced split conormal"
  hypotheses:
    - "Conormal E=H^-1 tensor V with V constant of dimension two"
    - "Moving line subbundle M in V tensor O_C, degree(M)=-epsilon<0"
    - "Saturated first relation W^r with W=H^-1 tensor M and r>=2"
    - "For second-relation conclusion, next independent generic relation at s>r is unique modulo prior multiples and coprime to m"
statement: "Finite principal-relation lifting can persist for many orders, but a moving pure-power first relation cannot admit an everywhere-coprime second graded generator of fixed degree; its actual evaluation divisor has degree at least (r-1)epsilon."
dependencies:
  - STCI-R-0008
evidence:
  - "research/notes/2026-10-14-generalization-moving-power-obstruction-tower.md"
  - "research/notes/2026-10-14-generalization-moving-power-second-relation.md"
independent_audits:
  - "research/notes/2026-10-14-generalization-moving-purepower-tower-independent-audit.md"
  - "research/notes/2026-10-14-generalization-moving-purepower-second-relation-independent-audit.md"
accepted_in: "research/notes/2026-10-14-generalization-moving-purepower-second-relation-independent-audit.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Does not exclude special-fiber degeneration, noncoprime next relations, or nonsaturated first relations."
  - "Finite Cohen-Macaulay thickenings are not global carrier surfaces or STCI pairs."
  - "Characteristic-zero apolar formula is not claimed in arbitrary characteristic."
---

# Moving pure-power first relation: two complementary conclusions

Let E=N_C^*=H^-1 tensor V with V a constant two-dimensional vector space, and let M be a moving line subbundle of V tensor O_C with degree -epsilon<0. Set W=H^-1 tensor M. Suppose the saturated first relation is the pure power W^r, r>=2, over characteristic zero.

## The finite-order tower is not an exclusion

If no independent relation has appeared by degree r+k, the obstruction bundle for correcting the first relation is

    Q_k = H^-k tensor M^-(r+k+1) tensor Sym^(r-1)V.

Vanishing of H^1(C,Q_k) through k<g allows a compatible embedded finite-order ideal locally of the form (P,I_C^(r+g)). The resulting finite thickening is Cohen-Macaulay. This explains why testing finitely many first-relation orders cannot by itself uniformly exclude moving powers. These ideals do not construct STCI pairs.

## The next coprime relation must degenerate

Suppose the next independent generic relation occurs at s>r, is unique modulo multiples of the first, and is generically coprime to m. Write L=E/W and let T be the actual second relation line in the quotient by prior multiples. The evaluation map T->L^s is nonzero generically; its zero divisor D is effective. The apolar quotient and negative degree of M give

    deg D >= (r-1)*epsilon.

In particular D cannot vanish. A binary complete-intersection initial ideal with the same degrees (r,s), and first generator m^r, **cannot remain coprime in every fiber** when the first direction moves and r>=2.

The divisor D records actual special-point degeneration, including failures of saturation of the second relation. It cannot be dropped. The theorem does not exclude an actual STCI whose next relation degenerates at special points, is not coprime, or has a different initial-ideal pattern.

## Relation to the spectral criterion

[STCI-R-0008](spectral_root_picard_criterion.md) tests whether an everywhere-coprime second **abstract graded** relation exists on the full root scheme. This theorem proves that for moving pure powers r>=2 the required everywhere-coprime graded relation is impossible, while finite first-relation thickenings can still exist. It does not convert the graded obstruction into unrestricted ambient nonexistence.

## Original evidence and independent audits

- [Moving-power tower](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-moving-power-obstruction-tower.md) and [independent audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-moving-purepower-tower-independent-audit.md).
- [Second-relation payment](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-moving-power-second-relation.md) and [independent audit](https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/research/notes/2026-10-14-generalization-moving-purepower-second-relation-independent-audit.md).
