# Normal filtrations and boundary obstructions

**Status:** thematic synthesis, not theorem authority or a new audit. This document connects accepted local results with provisional global-lifting arguments. Exact hypotheses and proofs remain in the linked sources.

## Distinguish three levels

For a smooth curve C with ideal I and an actual two-equation regular-sequence ideal J=(F,G) contained in I:

1. **Normal structure:** normal layers, their torsion, saturation, and socle of a supported multiple curve.
2. **Initial equations:** the full I-initial ideal of J, including cancellation-generated initials, and the filtered actual equation module J/IJ.
3. **Global realization:** actual homogeneous forms, compatible jets, properness, common factors, and residual support.

These are not interchangeable. In particular, a punctual initial-ideal defect does not by itself prove residual support; a vertical exceptional cycle need not descend to a residual curve.

## Accepted anchors

- [R-0010](../results/saturated_first_relation_normal_flatness.md): normal flatness under saturated first-relation and full generic binary-CI assumptions.
- [R-0016](../results/nonsaturated_first_relation_resultant.md): nonsaturated resultant and defect budget under stated conditions.
- [R-0019](../results/quasiprimitive_residual_cycles.md): conditional saturated residual-cycle and first-normal restrictions.
- [R-0030](../results/local_filtration_comparison_defect.md): canonical local exact comparison between initial-equation generators and the filtered actual equation module. With generic defect zero, punctual defect can occur only at simultaneous carrier singularities along C. Its existence under sole support is unresolved.
- [R-0032](../results/full_conormal_socle_budget.md): conormal and socle budget for actual supported complete intersections, with its degree-bound assumptions.
- [R-0033](../results/constant_first_relation_lifting.md): lifting obstruction for particular constant-first-relation models, not all moving relations.

The [normal torsion and genus note](../notes/2026-10-26-normal-torsion-spectral-genus-budget.md) compares ordinary graded torsion and saturated-layer divisors in the generically curvilinear supported setting. They measure the same genus contribution and must not be counted twice. Further spectral claims in that note remain provisional beyond promoted record scopes.

## Provisional boundary-repair and one-step arguments

The [boundary-repair note](../notes/2026-10-26-boundary-repair-global-lifting.md) supplies a principal-parts test for an identified linear obstruction in H^1(C,V): the class dies under V to V(D) exactly when its image in H^1(C,V(D)) is zero. On P1 this admits a common-divisor multiplication-kernel test. Repair by an arbitrary divisor of a given degree does not imply a prescribed geometric repair or actual homogeneous realization.

The [one-step note](../notes/2026-10-27-one-step-boundary-obstruction.md), with [independent audit](../notes/2026-10-27-one-step-boundary-obstruction-audit.md), constructs an extension class for a fixed lower embedded Cohen-Macaulay thickening with generically curvilinear normal algebra. The existing power-relation divisor consumes part of the next permitted divisor; the remaining allowance, together with vanishing of the pushed-forward extension class and surjectivity, governs its specified one-step extension.

For the final Gorenstein step (generic length at least three), that note argues that no additional divisor allowance remains: the relevant extension class must vanish, and perfect top-layer multiplication is also required. **These claims remain provisional and scoped.** They do not give a general ambient obstruction comparison, a global STCI exclusion, or a converse from splitting to two global equations.

## The global-source gap

The actual degree-d normal-jet source is the image of global sections of I(d) in sections of the finite normal neighborhood. Rational coefficients and independently chosen symbols need not arise from the same global homogeneous form. The one-step note develops further fixed-degree source tests, but does not exclude an entire surviving degree-at-least-five family.

## Open interfaces

- Decide whether an actual supported pair with generically zero comparison defect can have nonzero punctual defect (R-0030).
- Vary lower embeddings, their boundary divisors and extension classes **together**; determine the full vanishing locus rather than only a generic obstruction.
- Apply global-source and properness tests to a surviving family of actual homogeneous pairs.
- Construct a justified comparison among the R-0016, R-0019 and R-0030 defects, with all finite-flatness and curvilinearity hypotheses explicit.

This document is a reading route, not a replacement for proof evidence. No source note is retired by this first consolidation.


## Relation to the historical jet-discrepancy calculation

The [order-one result](../results/order_one.md) distinguishes the maximal-rank defect of successive global-section maps from the divisor D_j in a quasiprimitive saturated layer. The local comparison defect of R-0030 concerns the actual filtered equation module versus its initial generators, and is not automatically equal to either invariant. The quadric comparison divisor R and doubled divisor 2R are concrete finite-jet test cases, not a general identification of these three defects. Any proposed equality or implication needs an explicit comparison theorem and hypotheses.

## Source-preserved quartic-ancestor conormal and endpoint restrictions

These statements concern **quartic inverse-system ancestors**, not arbitrary STCI pairs or arbitrary-degree mates. Their proofs depend on the finite-flat quadruple, socle-pencil and complete quartic-fiber antecedents cited in the original notes.

The [intrinsic conormal splitting criterion](../notes/2026-10-07-session-localcoh-conormal-splitting.md) constructs V from the canonical triple ideal J by taking the torsion-free quotient of J/(I_C J). Its intrinsic extension has a line subbundle L cubed, twisted by the second defect, and a complementary conormal quotient. The actual two quartic targets map V surjectively onto the socle line O(-14), since their images form a basepoint-free pencil. The kernel has degree 2e-14, and the extension splits because H1(O(2e)) vanishes for e>=0. Therefore a common quartic ancestor necessarily has V=O(2e-14) direct sum O(-14). The criterion is necessary, not sufficient. For e=1, the remaining d2=1,2,3,4 strata require respective Hankel connecting-matrix ranks 3,2,1,0; in particular the d2=4 zero-extension/Gorenstein case remains possible at this stage. These are not STCI BF bounds.

The [corrected simultaneous-target bridge](../notes/2026-10-07-session-socle-bridge-adversarial-audit.md) excludes primitive e=1,d2=0 common quartic ancestors under the accepted finite-flat and socle antecedents, using both target equations together. The actual image of a multiplier in the quadruple is a nonzero socle target; it must not be set to zero. The valid local equation retains that target, and elimination between the two multipliers yields the contradiction. The older single-multiplier pole argument is invalid for ancestors.

The [six defective e=1,d2=1 endpoints](../notes/2026-10-08-session-localcoh-e1-d1-endpoint-ancestors.md) are excluded as *ancestors*: four have a one-dimensional complete ambient quartic space, incompatible with two independent target images; two have a common cubic factor and reduce to degree-one multipliers, excluded by P-037. This does not rule out an arbitrary higher-degree mate for a remaining unique quartic carrier. Likewise the [principal open-chart rank result](../notes/2026-10-08-session-mf6-principal-rank-open-independent-audit.md) gives dimension one for the complete quartic space on its specified open, not an all-mate carrier exclusion; boundary charts require their separate proofs.

The remaining defective ancestor strata and other directions must be checked with their actual extension classes and target images. None of these conditional exclusions should be promoted to a universal STCI theorem by dropping their antecedents.

## Two additional October 8 ancestor exclusions

**Quadric first-quotient direction.** For the fixed rational quartic C of class (1,3) on the smooth quadric Q, the conormal direction A=-z/2, B=1 is precisely the direction inside Q. Its canonical double is 2C on Q. Any containing quartic F restricts to a section of O_Q(4,4)(-2C)=O_Q(2,-2), which has no sections. Thus both quartic ancestor equations would be divisible by Q, reducing to the prohibited common quadratic ancestor P-037. This excludes that **direction for every second-defect divisor**, conditional on the canonical-triple reduction and P-037; it does not exclude every positive-defect or Gorenstein stratum. [Source and complete 35-monomial rank check](../notes/2026-10-08-session-localcoh-quadric-direction.md).

**Two algebraic defect-four directions.** For A=r*z, B=1 with 12r²+4r+3=0 and second-defect degree four, a genuine corrected triple has relation delta*m+theta*y²=0 with theta a nonzero constant, normalized to one. The complete seven-dimensional ambient double-quartic space has two primitive members and five coefficients (h,E)=(a_i*z^(i+2),z^i), i=0,...,4, with pairwise distinct a_i. Quartic containment is h=delta*E. Eliminating the two primitive coefficients leaves a seven-by-five matrix. For delta=d0+...+d4*z^4, its low and high minors are d0^4 and d4^4; when both vanish, the next minors are d1^5 and d3^5. For the remaining delta=d2*z², a diagonal minor has entries d2-a_i, at most one zero. Thus the kernel always has dimension at most one: no two independent quartics contain the triple. This excludes common quartic ancestors for **these two directions and every defect section**, not all defect-four directions or arbitrary-degree mates. [Exact source](../notes/2026-10-08-session-localcoh-e1-d4-algebraic.md).

## Rational endpoint-family comparison

The [Step 1C endpoint-family synthesis](phase2_step1c_endpoint_families.md) preserves the complete first-family target-u exclusion and the incomplete second-family certificate. For the latter, 22 primitive geometric parameter points remain unresolved after the two quadratic exceptional factors are closed. These are exceptions to a certificate, not constructed ancestors. Both results concern specified pure-top endpoint directions, not all quartic ancestors or arbitrary mates.
