# Common normal factors and the actual-CI root bridge: source audit

Date: 2026-10-17. **Status: scoped source comparison; no new theorem.**

## Source identification

The prior synthesis audit referred to a historical “P-006 common-normal-factor argument.” A repository filename or canonical result with that identifier was **not located** in this pass. Do **not** attribute a general theorem to P-006 without recovering the exact source. The verifiable source for the *conditional* bridge is [STCI-R-0006](../results/actual_ci_smooth_root_bridge.md), supported by the [October 14 bridge](../notes/2026-10-14-generalization-blowup-root-curve-primitive-bridge.md), its [independent audit](../notes/2026-10-14-generalization-blowup-root-curve-bridge-independent-audit.md), and the [October 15 local-algebra review](../notes/2026-10-15-generalization-inseparable-root-blowup-local-algebra-review.md).

## 1. Generic shared factors: exact scope

Let \(A=\mathcal O_{\mathbf P^3,\eta_C}\), a two-dimensional regular local ring, and \(I=(F,G)A\) be primary to its maximal ideal. If the original equations have orders \(r_F,r_G\) and leading forms \(f,g\), then the local intersection length satisfies \(\ell(A/I)\ge r_F r_G\). Equality holds for coprime homogeneous forms; strict inequality forces a common factor over an algebraic closure of the residue field. This is **generic local algebra**; it does not imply that the common factor extends as a saturated line subbundle along all of \(C\).

In particular, a shared factor is not necessarily the **entire first relation** of the full initial ideal. The latter is obtained only after accounting for cancellations and possible additional generators.

## 2. What the audited bridge actually requires

The actual-CI bridge [STCI-R-0006](../results/actual_ci_smooth_root_bridge.md) assumes:

- both original equations have generic order \(\rho\);
- their degree-\(\rho\) symbols jointly generate an everywhere saturated line relation;
- the **full** generic initial ideal is \((f_\rho,g_\sigma)\), a coprime binary complete intersection with \(\sigma>\rho\) and gap \(\sigma-\rho\ge2\);
- the full root divisor of \(f_\rho\) on the exceptional surface is smooth.

Then the intersection of the **two original strict-transform divisors** has local ideal \((h,u^{\sigma-\rho})\) along the root, and the specified finite Cartier lifts follow. The local-algebra review verifies the key subtlety: although an alternative ideal generator has order \(\sigma\), both *original* equations are divided by the common order \(\rho\). Dividing the replacement generator by \(u^\sigma\), or saturating by \(u\), would erase the exceptional multiplicity.

The strict-transform **intersection of the original divisors** is not the strict transform of the supported scheme \(V(F,G)\); the latter has no points outside the center and has empty strict transform in the closure-from-complement sense.

## 3. Defects that block an unrestricted application

| Defect | Why it matters |
| --- | --- |
| Different original orders \(r_F\ne r_G\) | The bridge assumes equal original order \(\rho\). |
| First symbols share only a proper factor | Their common factor need not define the whole saturated first relation of the full initial ideal. |
| Base points of the coefficient pair | Vertical exceptional fibers may appear in the strict intersection. |
| Nonsaturated relation | The relative root form may degenerate or acquire torsion at special points. |
| Extra full-initial-ideal generators | The prescribed binary complete-intersection standard basis is unavailable. |
| Gap \(\sigma-\rho=1\) | The primitive-multiple/obstruction consequence with gap at least two does not apply. |
| Singular or nonreduced full root | The smooth-root conormal and Cartier-lifting argument cannot be applied unchanged. |

None of these defects is ruled out by the mere existence of a generic common normal factor.

## 4. Source-supported local algebra

The October 15 review confirms that under the **full initial-ideal** assumption one may choose actual elements \(P,H\in I\) with initial forms \(f_\rho,g_\sigma\) and obtain \((P,H)=I\) **before completion**, via filtered division and Krull intersection. The generator change is invertible in the actual generic local ring. On the blowup, the original strict-intersection ideal is
\[
(P/u^\rho,H/u^\rho)
=(P/u^\rho,u^{\sigma-\rho}(H/u^\sigma)).
\]
At a reduced generic root prime the second parenthesis is a unit, giving transverse length \(\sigma-\rho\). The independent October 14 audit then uses the smooth full root and everywhere generation to extend the local normal form along every point of the root.

This is a genuinely geometric statement, but only **after** the global hypotheses have been checked.

## 5. Recommended next lemma, explicitly OPEN

Find a canonical defect construction attached to an arbitrary actual pair \((F,G)\) whose generic leading forms have a common factor. It should compare the closure of the common-direction scheme on \(E\) with the saturation of the first full-initial-ideal relation and record the vertical exceptional components at defective points. A second stage should compare the quotient second relation and its special-fiber evaluation divisor.

**First test:** unequal original orders and a proper common factor, not only the equal-order proportional case covered by the bridge. A correct comparison should recover STCI-R-0006 when its defects vanish.

No such general comparison theorem is claimed here.

## 6. Audit conclusion

**Verified against cited source records:** the bridge's hypotheses, generic standard-basis generator change, retained exceptional factor, and support/vertical-component argument under everywhere generation.

**Not verified:** an independently identified P-006 source theorem, a general passage from shared generic factors to saturated root relations, or a new unrestricted STCI obstruction.

The immediate improvement is epistemic: stop treating “common normal factor” and “smooth global first root” as interchangeable.
