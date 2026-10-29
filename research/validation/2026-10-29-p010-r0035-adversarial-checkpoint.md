# Adversarial review checkpoint — P-010 and R-0035 (2026-10-29)

**Status: INCOMPLETE for P-010; INCOMPLETE for R-0035. Not a certification.**

## Scope and independent checks

The curve is the image of [s:t] -> [s^4:s^3t:st^3:t^4]. The quadric xw-yz vanishes identically. On this smooth rational quartic, deg T_{P3}|C = 16 and deg T_C = 2, so deg N = 14. This alone does **not** prove balanced splitting O(7)^2: an independent splitting computation is still required.

A primitive triple with first conormal line B=O(-7) is locally an embedded algebra R[z]/(z^3), with a second ambient normal equation of the form y-a(t)z^2 modulo cubic terms. Its quadratic correction transforms affinely under changes of normal frames. A genuine obstruction must be computed in the torsor of these corrections; merely displaying a nonzero representative before allowing changes of splittings is insufficient.

For B=O(-7), the natural quadratic correction has homomorphism type Hom(B,B^2)=B=O(-7), hence a potential obstruction in H^1(P1,O(-7)), dimension 6. This identifies a *candidate obstruction group*, not the actual class. The class for all P1 constant directions has **not** been independently derived or shown nonzero. In particular pure directions and projective endpoints remain unverified.

## Historical claims inspected after preliminary reconstruction

- research/notes/2026-10-05-localcoh-degree4.md uses P-010 to exclude an order-three inverse-system ancestor and asserts a primitive triple from its annihilator.
- research/notes/2026-10-05-localcoh-pure-direction-audit.md explicitly depends on P-010 and treats the two pure directions by a contact calculation and symmetry.
- research/notes/2026-10-06-localcoh-constant-direction-apolar.md reports the class 3(theta^3 t^-5 - theta^2 t^-4/2 + theta t^-3/4 - t^-2/8). **This expression has not been independently reconstructed**, and its status as a nonzero class for all directions is not certified here.
- research/notes/2026-10-14-generalization-index12-filtered-compatibility.md expressly says P-010, normal-carrier torsion/index reduction, and socle budget were accepted inputs, not independently reverified.
- research/results/normal_carrier_bounded_index_exclusion.md records R-0035 as proved, but also lists inherited torsion reduction and quadratic direction obstruction among required hypotheses.

## Downstream logical audit

The R-0035 source gives D_n,P=(k-1)A_F,P+kD_r,P for k=n/r, a pointwise torsion identity 2 sum length(T_i)=n D_n,P, and a numerical reduction to (a,b)=(6,8), n=12. These are **claims requiring independent validation**, not established by this checkpoint.

Conditional arithmetic check: with n=12 and r<=4, k>=3, so if A_F,P and D_r,P are nonnegative and the displayed identity holds, D_n,P>=2A_F,P. For a normal sextic, the claimed global formulas give deg(D_n-2A_F)=9ell-62; for ell<=7, nonnegativity forces ell=7, yielding slack 1. This conditional arithmetic is correct, but does not validate the local identities, the reduction to n=12, or the construction of the global primitive triple.

The asserted exclusion of indices 6 and 12 from the *scope of the proof* is not a proof that those indices occur, nor that the boundary is sharp. The stated k>=3 argument fails for r=6,12, but other obstructions may still apply.

## Counterexample search and unfulfilled obligations

No counterexample has been established. Nor has a complete search been performed. Outstanding independent work includes: derive balanced normal transition frames from the embedding; calculate the quadratic correction cocycle from scratch for every constant direction; quotient by all allowed gauge changes; verify nonvanishing in H^1; classify torsion-free primitive triples versus boundary-pole models; independently prove the socle/Jacobian and normal-index formulas with exact hypotheses; independently justify the global class-group/minimal-mate reduction; and check symbolic saturation at every index stratum.

## Verdicts and Phase 2 recommendation

**P-010: INCOMPLETE.** Nonzero obstruction for every direction is not independently established here.

**R-0035: INCOMPLETE.** The final implication remains conditional on several substantial unverified inputs, notably P-010 and the reduction to the primitive triple. No invalid inference or counterexample has yet been established; FAIL would overstate the evidence.

**Phase 2:** Do not treat this checkpoint as an independent proof or promote it. Preserve historical records without silently correcting their status; require a subsequent full adversarial reconstruction before certification. This checkpoint documents precisely what was and was not checked.
