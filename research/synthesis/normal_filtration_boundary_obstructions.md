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

The [boundary-repair note](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md) supplies a principal-parts test for an identified linear obstruction in H^1(C,V): the class dies under V to V(D) exactly when its image in H^1(C,V(D)) is zero. On P1 this admits a common-divisor multiplication-kernel test. Repair by an arbitrary divisor of a given degree does not imply a prescribed geometric repair or actual homogeneous realization.

The [one-step note](../supplements/BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md), with [independent audit](../notes/2026-10-27-one-step-boundary-obstruction-audit.md), constructs an extension class for a fixed lower embedded Cohen-Macaulay thickening with generically curvilinear normal algebra. The existing power-relation divisor consumes part of the next permitted divisor; the remaining allowance, together with vanishing of the pushed-forward extension class and surjectivity, governs its specified one-step extension.

For the final Gorenstein step (generic length at least three), that note argues that no additional divisor allowance remains: the relevant extension class must vanish, and perfect top-layer multiplication is also required. **These claims remain provisional and scoped.** They do not give a general ambient obstruction comparison, a global STCI exclusion, or a converse from splitting to two global equations.

## Full initial ideals and the filtered equation module

For a regular codimension-two embedding C in a smooth threefold, let I be its ideal and J=(F,G) a proper complete-intersection ideal contained in I. Set S=gr_I(O_X)=Sym(I/I²), H=in_I(J), and Q_n=H_n/(S_+ H)_n. The actual equation module J/IJ carries its induced I-filtration. The canonical comparison has an exact sequence

    0 -> Delta_n -> Q_n -> gr^n(J/IJ) -> 0,

where Delta_n=in_n(IJ)/(S_+ H)_n. In particular, minimal generators of the full initial ideal need not survive as independent generators of the filtered equation module. This is the comparison in [R-0030](../results/local_filtration_comparison_defect.md), with its full construction and counterexample in [the ideal-filtration supplement](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd).

The full initial ideal is itself not determined by the two displayed leading forms. In the regular transverse local ring, J=(x²,x²+y³)=(x²,y³), so the displayed order-two symbols generate only (X²), whereas the full initial ideal is (X²,Y³), of colength six. The [higher-initial investigation](../supplements/HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#explicit-cancellation-examples) gives further local examples and the prescribed characteristic-two quartic computation. None of these local models by itself constructs a global STCI.

The comparison defect Delta_n is supported only where both carrier hypersurfaces are singular along C. Thus smoothness of either carrier along C forces its vanishing there; simultaneous singularity is necessary, not sufficient, for a nonzero punctual defect. Whether a nonzero punctual comparison defect occurs for an actual proper pair with sole reduced support C remains open. The characteristic-two quartic example illustrates the distinction: its fourth initial equation arises by cancellation, but its comparison defect vanishes [R-0031](../results/quartic_char2_fourth_equation_kernel.md).

Neither Delta_n nor cancellation is the saturated first-relation resultant defect of [R-0016](../results/nonsaturated_first_relation_resultant.md), the quasiprimitive residual-cycle divisor of [R-0019](../results/quasiprimitive_residual_cycles.md), or the rank shortfall of a global jet map. Identifying any two requires an additional comparison argument.

## A common-divisor test for cohomological boundary repair

For a fixed obstruction \(o\in H^1(\mathbf P^1,\mathcal O(-r))\), \(r\ge2\), and an effective divisor of degree \(B\), write \(n=r-2\). Serre duality identifies the obstruction with a functional on \(H^0(\mathcal O(n))\). If the divisor is cut out by \(h\in H^0(\mathcal O(B))\), then the obstruction dies after twisting by that divisor precisely when
\[
\langle o,hq\rangle=0\quad\text{for all }q\in H^0(\mathcal O(n-B)).
\]
Thus allowing the divisor to vary asks for a nonzero kernel of a catalecticant multiplication map. A dimension argument supplies such a divisor for every scalar obstruction when \(B\ge\lfloor r/2\rfloor\); for a vector-valued obstruction the **same divisor** must lie in the kernels of all component maps. A prescribed socle boundary is still more restrictive.

This is a precise *cohomological* criterion, not a proof that the allowed socle divisor modifies the ambient embedded-lifting obstruction in this way. The missing comparison of obstruction complexes and the actual global homogeneous source are separate requirements. The detailed derivation and limits are in [the boundary supplement](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md), with the fixed-lower embedded criterion in [the one-step supplement](../supplements/BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md).

## A computed rank-drop interface in degree six

The movement-two (6,16) lane provides an exact model of the global-source obstruction. Its degree-six quadratic-normal-symbol map has domain dimension 23, kernel generated by the cube of the unique quadric, and rank 22 inside a 33-dimensional target. Hence eleven independent linear symbol constraints survive even though the entire ambient source is known. The [conditional source computation](normalization_conductor_phase2_addendum.md) records a basis and the equations explicitly.

A putative quadratic root f and multiplier alpha must satisfy those equations **together**; arbitrary choices of f and alpha need not lift to a sextic. At the next normal order, a further cubic-jet equation must be imposed on a lift, and changing the sextic by the kernel generator does not change its quadratic symbol. This is an actual rank calculation, not a general theorem about every degree or a proof of a (6,16) STCI. It also does not determine the punctual equation-module comparison defect, which belongs to a different filtration.

## A witnessed failure of successive-jet realization

The conditional movement-two (6,16) calculation supplies a particularly sharp negative example. A specified smooth torsion-two quadratic root has a unique projective multiplier meeting all eleven equations of the actual sextic quadratic-symbol image. Its next cubic comparison has exact nonzero annihilating pairing \(-384\), and the seed separately fails the second obstruction. Thus even **membership in the true global leading-symbol image** need not extend to a compatible next jet. See [the computed seed](normalization_conductor_phase2_addendum.md#exact-failed-seed-and-the-remaining-incidence).

This failure is not the local comparison defect \(\Delta_n\) of R-0030, not a nonsaturated first relation, and not a residual curve. It is an obstruction at the next global-source compatibility stage for a specified seed. A uniform theorem would need to handle the whole root/multiplier incidence, including singular roots and multiplier zeros.

## Rank-stratified realization rather than generic elimination

The global sextic quadratic-symbol image is an exact linear subspace, but its next cubic compatibility equation depends on the chosen root and multiplier. Solving that equation on the generic full-rank open and dividing by a parameter cannot decide the exceptional rank-drop or multiplier-zero strata. The correct incidence retains the full coefficient scheme, imposes augmented-minor solvability on each rank stratum, and then intersects with the independently necessary second-obstruction and full-root torsion conditions. See [the finite incidence formulation](normalization_conductor_phase2_addendum.md#a-scheme-level-incidence-formulation).

This procedure does not identify the local comparison module \(\Delta_n\), nor does it assert that the necessary incidence has a point. It specifies how to avoid losing legitimate exceptional candidates while testing **actual** homogeneous source realization.

## The constant-rank cubic correction

The cubic correction is multiplication by the nonzero root \(f\), applied to a linear normal form with two degree-at-most-seven coefficients. This is injective over the polynomial ring, so the correction image has rank sixteen and codimension twenty-four in the forty-dimensional target. The correct test is vanishing of the cubic difference in this quotient, not a search for correction-matrix rank drops. The exceptional geometry remains in the root, multiplier, second obstruction and mate equations.

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

**Later endpoint closure:** The earlier October 8 count of 22 unresolved second-family exception points was eliminated by the October 13 cubic/quartic field duals and the October 14 degree-fifteen fraction-free certificate. Both specified rational endpoint families are excluded under their actual tensor and pure-top assumptions. See [the updated endpoint synthesis](phase2_step1c_endpoint_families.md). Do not interpret the earlier count as the current frontier.

## P-044 dx=1 slice: exact five-coordinate saturation (October 7)

The [dx=1 saturation audit](../notes/2026-10-07-dx1-saturation-audit.md) proves a **slice-level** classification for P-044's normalized primitive-fourth obstruction, not a universal STCI theorem. Write `A=z²+az+x`, `B=1+bz+dz²`, impose `d=1/x`, and put `u=bx-a`, `t=xu`, `alpha=2a+1`, `beta=b+2`. The basepoint-free slice is precisely `D(t)`. Reconstructing all five original obstruction coordinates gives an ideal `L=(Q1,...,Q5)` whose saturation is the six-generator ideal

`L:t^infinity = J = (x beta²+alpha beta-2alpha², (4x+2)alpha beta-3alpha², beta³, alpha beta², alpha² beta, alpha³)`.

The exact certificates are `tJ subset L subset J` and `J:t=J`. The latter also follows from the free rank-four `Q[x]` quotient `R/J` with basis `1,alpha,beta,gamma`, `gamma=beta²-(8/3)alpha beta`: multiplication by t has determinant `[x(1/2-2x)]^4`, hence is injective. The radical is `(alpha,beta)`, so the basepoint-free zero locus is `a=-1/2`, `b=-2`, `x!=0,1/4`. The scheme is **nonreduced**; its underlying support alone does not preserve the four-dimensional quotient structure. The formerly proposed three-coordinate saturation is false: all five coordinates are necessary. The note checks agreement with P-045 on this slice, without claiming that the slice exhausts P-044's full parameter space. Preserve this exact ideal as a distinct boundary calculation rather than treating its previous audit gap as current.

## Primitive e=1 triples versus defective d2=4 ancestor directions

The [October 7 primitive-triple audit](../notes/2026-10-07-session-mf6-e1-independent-audit.md) distinguishes a stronger quartic-carrier statement from the weaker quartic-ancestor rank tests. In characteristic zero, for first quotient `O(-6)` and `D2=0`, the basepoint-free primitive directions comprise one principal torus orbit and three boundary orbits. The principal and two algebraic boundary orbits have complete two-dimensional quartic pencils with forced ruling-line base components; the comparison-zero boundary has quartics divisible by the unique quadric. The fixed-line observation alone does **not** exclude arbitrary mates, since a line can meet C at its forced intersection points. The subsequent normalizations and full inverse-support analysis in the independent audit exclude the pure quartic carriers for mates of any positive degree under the stated MF6 hypotheses. Do not preserve the earlier fixed-line-only argument as a complete all-degree proof. The defective `D2>0` cases remain outside this primitive result.

By contrast, the [October 8 algebraic d2=4 audit](../notes/2026-10-08-session-localcoh-e1-d4-independent-audit.md) is a **common-quartic-ancestor** exclusion for precisely the two directions `A=r z, B=1`, `12r²+4r+3=0`, uniform in every genuine quartic defect section. The correction coefficient theta must be nonzero: theta zero would produce torsion `(R/(delta))*m` at a zero of delta and violate finite flatness. Normalizing theta=1 gives `y²=-delta*m` and quartic containment `h=delta E`. The complete quartic source has dimension seven; a seven-by-five matrix has rank at least four for every delta, including repeated and infinity zeros, leaving at most one containing quartic. Two independent target classes are therefore impossible **conditional on the canonical-triple ancestor reduction**. This does not exclude all d2=4 directions or arbitrary-degree mates.

## Six degree-one defective endpoints: fixed-carrier exclusion stronger than ancestor rank

The [October 7 endpoint audit](../notes/2026-10-07-session-mf6-e1-d1-endpoints.md) treats all six `e=1,d2=1` boundary directions (`a0=0` or `b1=0`), **not** the principal `a0*b1!=0` locus or the `d2=2` stratum. For each endpoint the complete ambient quartic space is computed from all 35 monomials. At the rational root `r=-1/2`, the quartics are a fixed cubic times linear forms; at either algebraic root of `12r²+4r+3=0`, the space is one-dimensional and generated by an explicit irreducible quartic. The latter has third-layer defect `d3=4`, incompatible with MF6 `(d2,d3)=(1,3)`, but that numerical contradiction alone is not an arbitrary-mate exclusion.

The stronger fixed-carrier result uses an explicit dominant birational parametrization of an affine chart of each algebraic quartic by `k[u,v,(u+kappa)^(-1)]`, where `3kappa²-2kappa+1=0`, with full inverse support of C equal to the diagonal `v=u`. A hypothetical mate pullback must be `c(v-u)^n(u+kappa)^k`. Comparing the two branches over the singular line forces `k=-n` and `(-kappa)^n=1`; conjugation and `Norm(kappa)=1/3` contradict `n>0`. Coordinate reversal and torus symmetry transfer the argument to the other endpoints. This proves an **all-degree mate exclusion for these six fixed endpoint carrier directions**. The open principal `d2=1` locus and the `d2=2` stratum are not covered by this scoped argument. This strengthens, without contradicting, the earlier ancestor-only quartic-space statement above; the general R-0001 theorem subsequently excludes all integral quartic carriers by a different global route.

## Defective e=1 MF6 structural conditions

The [October 7 defective structural note](../notes/2026-10-07-session-mf6-e1-defective-structural.md) gives a local Hilbert–Burch presentation for a positive-second-defect canonical triple: `J=(delta*m-gamma*y^2,m*y,m^2,y^3)`, with gamma invertible at zeros of delta. Its torsion-free generator bundle has extension `0 -> L^3(D2) -> V -> M(-D2) -> 0`, where `L=O(-6), M=O(-8)`. The `-D2` twist in the quotient is essential. The normalized cubic residue uses `delta^2*f3`, yielding a class in `H1(O(-10+2*d2))` that must vanish after mapping to `H1(O(-10+d2+d3))`.

For `(d2,d3)=(1,3)` the necessary condition is a nonzero kernel of the five-by-three Hankel matrix on seven Laurent coefficients (all ten maximal minors vanish). For `(2,2)` the class in `H1(O(-6))` must vanish in all five coordinates. These conditions are not sufficient for a quartic carrier or mate. The first quadratic-cocycle killing test gives a sextic direction locus `c1*c3-c2^2=0` for `d2=1`; for `d2=2`, a defect quadratic `delta0+delta1*z+delta2*z^2` must satisfy `delta0*c1+delta1*c2+delta2*c3=0`. In each case finite flatness imposes an additional no-common-zero condition on delta and the corrected coefficient gamma. Primitive obstruction-zero directions cannot acquire a genuine positive defect of degree at most three by multiplying their unique correction by delta.

The [primitive progress note](../notes/2026-10-07-session-mf6-e1-progress.md) records the exact `H1(O(-4))` quadratic cocycle, three Laurent obstruction coordinates, and classification into one principal and three boundary torus orbits. Its incomplete conjugate-orbit checkpoint was superseded by the later [independent audit](../notes/2026-10-07-session-mf6-e1-independent-audit.md). The six degree-one boundary directions have the stronger all-degree exclusions recorded above. The principal `d2=1` sextic and `(2,2)` conditions remain open within this structural method, without contradicting the separate global quartic-carrier exclusion R-0001.

## Mixed (4,6): Fitting divisor and pole strata

The [October 5 mixed-six calculation](../notes/2026-10-05-mixed46-poles.md) assumes a finite-flat quasiprimitive length-six Gorenstein algebra, locally free Banica–Forster pieces, and perfect multiplication pairings. For defect divisors `0<=D2<=D3`, the graded pieces are `O,L,L^2(D2),L^3(D3),L^4(D2+D3),L^5(D2+D3)`. The coordinate-independent first-normal cokernel Fitting divisor satisfies `A=D3+min(D2,D3-D2)`, with the minimum taken pointwise. The proof computes torsion `T=N/yB`: its length is `ord(D2+D3)`, while `length(T^2)=max(ord D2-ord(D3-D2),0)`, and `length(T/T^2)=ord A`. In particular `D3<=A<=D2+D3`; neither extreme equality is universal.

For degree pair `(4,6)`, the seven necessary numerical types are `e=0: (d2,d3)=(1,8),(2,7),(3,6),(4,5)` and `e=1: (0,4),(1,3),(2,2)`. Their coarse nonregular pole lengths reduce to `e=0: p=1,2,3,4` and `e=1: p=4,5,6`. This is a restriction on possible strata, not a realization or an STCI exclusion. The [regular-ratio proof](../notes/2026-10-05-mixed46-regular.md) separately excludes only the two pure constant horizontal directions when `e=0` and the quotient ratio is globally regular. Its quadric-residual and cubic-jet argument does not treat mixed directions, e=1, or nonregular pairs. The [earlier rank-six audit](../notes/2026-10-05-mf6-further-audit.md) records the saturated-lattice hypotheses and the remaining `(4,5)` defect case.

## Integrated thickening and realization problem

The characteristic-zero conormal bundle of the fixed quartic is balanced, whereas the characteristic-two splitting changes [R-0020](../results/quartic_conormal_characteristic_jump.md). The prescribed characteristic-two fourth-equation kernel [R-0031](../results/quartic_char2_fourth_equation_kernel.md) makes a key distinction concrete: cancellation-generated higher initials cannot be discarded merely because two low-order symbols appear dependent. The prescribed \(\mu_4\) degeneration [R-0021](../results/quartic_mu4_degeneration.md) likewise warns that flat arithmetic specialization need not preserve reduced support. Neither example proves a universal characteristic-zero obstruction.

The [weighted-initial note](../notes/2026-10-26-weighted-initials-normal-boundary.md) uses valuations of coefficient functions over \(k(C)\) to track special-point Newton changes. Those coefficients depend on chosen normal coordinates; intrinsically their leading terms are sections of symmetric powers of the conormal bundle. This is a *methodological proposal*, not an established coordinate-independent tropical obstruction. The [normal torsion/genus note](../notes/2026-10-26-normal-torsion-spectral-genus-budget.md) further distinguishes ordinary torsion from saturation divisors: counting both as independent genus contributions double-counts the same phenomenon in its stated curvilinear setting.

### A finite, checkable continuation

Choose a specific surviving pair of degrees at least five, or a specified lower embedded thickening. Record (i) its generic transverse algebra and **full** initial ideal; (ii) the saturation and exceptional-point defect of each conormal layer; (iii) the exact obstruction class and allowed boundary divisor for the next lift; and (iv) the image of actual global homogeneous sections in the required jets. At each step distinguish failure of a necessary condition from failure to construct a solution. Finally check properness and actual residual support independently. The provisional [boundary repair](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md) and [one-step completion](../supplements/BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md) analyses provide scoped tools, not a theorem that this procedure always decides STCI.

**Remaining mathematical gap:** there is no established general implication from a generic or graded root configuration and its local repair data to a pair of global equations with sole reduced support. Conversely, there is no established theorem excluding all such configurations when first relations are nonsaturated or the comparison defect is punctual.

## Local comparison, saturation, and the unresolved singularity interface

The canonical comparison in [R-0030](../results/local_filtration_comparison_defect.md) can be stated without choosing normal coordinates. In a regular local ring along a smooth codimension-two curve, put I=I_C, J=(f,g), S=gr_I(R), H=in_I(J), B=in_I(IJ), and S_+=the positive-degree ideal. Filter the *actual* equation module D=J/IJ by its intersections with powers of I. In each degree n there is an exact sequence

    0 -> Delta_n -> Q_n -> gr_F^n(D) -> 0,
    Delta_n=B_n/(S_+H)_n,  Q_n=H_n/(S_+H)_n.

This compares three objects that are often conflated: minimal generators of the full initial ideal H, the initial ideal B of IJ, and the filtered images of the two actual equations. At a generic transverse field where J is a parameter ideal, dim Delta=mu(H)-2; hence a two-generator original ideal can have more than two *initial* generators. If Delta vanishes generically, the DVR formula reads

    length(Delta_n)=length(tors Q_n)-length(tors gr_F^n(D)).

Under the stated local hypotheses, Delta vanishes wherever either carrier is smooth on C. Therefore nonzero punctual Delta requires a simultaneous singular point of both carriers; the converse is not asserted, nor is existence under radical(J)=I. This criterion does **not** prove that every supported complete intersection has a common singular point. It only locates a defect *if* that defect exists.

### Three distinct exceptional phenomena

1. **Unsaturated first relation.** The coefficient section vanishes at a point of C, so the first-relation line and its quotient acquire a base-point or torsion issue. The [nonsaturated resultant result R-0016](../results/nonsaturated_first_relation_resultant.md) supplies a scoped numerical test, not a blanket exclusion.
2. **Singular but nonvanishing root divisor.** The coefficient section remains nonzero, while roots collide or become nonreduced. Saturation alone does not prevent this. The formal-root and Picard-descent restrictions must be applied with their own hypotheses.
3. **Punctual comparison defect.** Even if the generic initial ideal has the expected two generators, special fibers can acquire cancellation-generated initials. R-0030 measures this separately from first-relation saturation and from residual components.

These alternatives need not be mutually exclusive. A proof eliminating one does not eliminate the others. In particular, do not infer properness or sole support from a vanishing graded obstruction.

## What the socle budget does and does not exclude

For an actual supported complete intersection, [R-0032](../results/full_conormal_socle_budget.md) records the corrected identity

    n(lambda*d-L)=lambda*(n*d-2*M)+2*Delta,

where n is generic length, d the Loewy index, M the weighted layer-rank sum, L the canonical degree parameter, lambda a valid conormal quotient degree bound, and Delta the corrected degree/torsion defect. The intermediate layers matter: computing only the first normal form and final socle omits terms in M and Delta. The conclusion lambda*d>=L is necessary under the theorem's hypotheses. Equality gives graded self-duality; a constant algebra needs additional balanced-rational assumptions.

The [constant-first-relation obstruction R-0033](../results/constant_first_relation_lifting.md) requires an actual embedded thickening, a constant first form f, and next initial relation space exactly fV. For a factor direction m of multiplicity nonzero in the field, the quadratic obstruction h_m must vanish. For the fixed characteristic-zero quartic, the inherited nonvanishing of the direction classes excludes the corresponding zero-defect constant-graded-CI equality models. It does not exclude a moving f, an extra next-order relation, or a positive-defect model.

## A bounded next experiment, not another case catalogue

The most informative single test is to choose one candidate whose generic transverse algebra is explicit and carry it across the exceptional points of C. Record in one place the full initial ideal, the first-relation saturation divisor, the local comparison module Delta, the torsion-corrected conormal layers, the next extension class, and the image of global homogeneous sections. A failed candidate should be classified by the *first failed interface*: generic algebra, saturation, punctual comparison, embedded lifting, global source, or residual support. State whether the failure survives coordinate changes or is specific to the chosen family.

A useful negative outcome is a mechanism that excludes an entire invariant class; a failed isolated pair without that explanation is not a general obstruction. The characteristic-two split conormal example and the characteristic-zero balanced extension provide a controlled comparison, but arithmetic specialization by itself does not transfer sole reduced support.

## Ordinary ideal powers and filtered equation modules are different source questions

In degrees \(d\ge3m\), the fixed quartic's ordinary ideal-power theorem identifies the complete ambient source \(H^0(I_C^m(d))\) with \((I_C^m)_d\), and gives \(H^1(I_C^m(d))=0\). This is a statement about ambient sections vanishing to a prescribed order. The comparison defect \(\Delta_n\) instead compares minimal generators of the **full initial ideal of an actual pair** with the filtered equation module \(J/I_CJ\). Neither assertion implies the other.

To pass from an ambient source to a specific normal symbol, the map to \(H^0(\operatorname{Sym}^m N_C^\vee(d))\) must be computed. To pass from compatible symbols to an actual supported complete intersection, one must also impose a common global lift, properness and degree exhaustion. See [the ideal-power proof](formal-normal-intersection.md#12-what-the-exact-ideal-power-theorem-contributes) and [the global-source treatment](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md).

## Characteristic-two comparison and arithmetic scope

The fixed quartic pair in R-0021 is flat over the integers. Its characteristic-zero fiber contains four reduced quartics, whereas its characteristic-two fiber has sole reduced support C and generic transverse length four. The conormal extension changes splitting type (R-0020). In the special fiber, R-0031 identifies the cancellation-generated fourth initial equation with the filtered equation-module kernel O(-24); its comparison defect is zero.

R-0012 rules out a constrained flat embedded lift of this prescribed special scheme over Z_(2) or Z_2 with generic reduced support C. It does not contradict the integral family with four generic components or address arbitrary ramified bases. These are separate tests of normal structure, full initial equations, and global support.
