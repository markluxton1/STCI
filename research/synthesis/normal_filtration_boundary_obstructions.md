# Normal filtrations and boundary obstructions

**Status:** thematic synthesis, not theorem authority or a new audit. This document connects accepted local results with global-lifting arguments with the review scopes stated in their sources. Exact hypotheses and proofs remain in the linked sources.

## Geometric orientation: successive neighborhoods of the curve

The primary geometric object is an embedded multiple structure supported on
the fixed rational quartic \(C\), not a list of coefficients in normal
coordinates. Blowing up \(C\) in \(\mathbf P^3\) exposes the normal
directions on the exceptional ruled surface
\(E=\mathbf P(N_{C/\mathbf P^3})\). A surface's first nonzero normal
symbol cuts a divisor on \(E\); common components and special fibers
encode shared normal directions and concentration of contact. This is
the geometric setting for the normal-order and common-factor tests below.

Successive thickening layers ask a different question: whether a specified
embedded multiple curve extends by one more layer. The associated conormal
modules, multiplication maps and extension classes measure compatibility
of those successive neighborhoods. An endpoint divisor may allow a
cohomological obstruction class to be repaired, but this does not by
itself realize the repaired structure by homogeneous equations.

Finally, an actual pair of hypersurfaces imposes **global source
conditions** beyond either exceptional-divisor geometry or abstract
thickening theory. Its full filtered equation module can contain
relations invisible in its initial normal forms. These three levels
(geometric contact, embedded extension, and global equation realization)
organize the results that follow. Their comparison maps, where not
proved, remain research questions rather than implicit identifications.

For torus limits the same objects carry weight decompositions. These
weights can refine the possible normal layers and extension maps, but
the deformation back to a non-invariant complete intersection may use
nonzero-weight directions. Thus a fixed-point calculation is a
necessary boundary test, not a restriction to invariant generators.

## Three levels of the geometric obstruction problem

For a smooth curve C with ideal I and an actual two-equation regular-sequence ideal J=(F,G) contained in I:

1. **Normal structure:** normal layers, their torsion, saturation, and socle of a supported multiple curve.
2. **Initial equations:** the full I-initial ideal of J, including cancellation-generated initials, and the filtered actual equation module J/IJ.
3. **Global realization:** actual homogeneous forms, compatible jets, properness, common factors, and residual support.

These are not interchangeable. In particular, a punctual initial-ideal defect does not by itself prove residual support; a vertical exceptional cycle need not descend to a residual curve.

## Accepted anchors

- [R-0010](../results/saturated_first_relation_normal_flatness.md): normal flatness under saturated first-relation and full generic binary-CI assumptions.
- [R-0016](../results/nonsaturated_first_relation_resultant.md): nonsaturated resultant and defect budget under stated conditions.
- [R-0019](../results/quasiprimitive_residual_cycles.md): conditional saturated residual-cycle and first-normal restrictions.
- [R-0030](../results/local_filtration_comparison_defect.md): canonical local exact comparison between initial-equation generators and the filtered actual equation module. Under its smooth-carrier hypotheses the defect is supported at simultaneous carrier singularities along C.
- [R-0032](../results/full_conormal_socle_budget.md): conormal and socle budget for actual supported complete intersections, with its degree-bound assumptions.
- [R-0033](../results/constant_first_relation_lifting.md): lifting obstruction for particular constant-first-relation models, not all moving relations.

The [normal torsion and genus note](../supplements/CURVILINEAR_GENUS_AND_DEFECTS.md#normal-torsion-spectral-genus-budget) compares ordinary graded torsion and saturated-layer divisors in the generically curvilinear supported setting. They measure the same genus contribution and must not be counted twice. Further spectral claims in that note have the proof and review scopes stated there.

## Boundary-repair and one-step arguments

The [boundary-repair note](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md) supplies a principal-parts test for an identified linear obstruction in H^1(C,V): the class dies under V to V(D) exactly when its image in H^1(C,V(D)) is zero. On P1 this admits a common-divisor multiplication-kernel test. Repair by an arbitrary divisor of a given degree does not imply a prescribed geometric repair or actual homogeneous realization.

The [one-step note](../supplements/BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md), with [independent audit](../supplements/BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md#2026-10-27-one-step-boundary-obstruction-audit), constructs an extension class for a fixed lower embedded Cohen-Macaulay thickening with generically curvilinear normal algebra. The existing power-relation divisor consumes part of the next permitted divisor; the remaining allowance, together with vanishing of the pushed-forward extension class and surjectivity, governs its specified one-step extension.

For the final Gorenstein step (generic length at least three), that note argues that no additional divisor allowance remains: the relevant extension class must vanish, and perfect top-layer multiplication is also required. **These claims retain their stated scopes.** They do not give a general ambient obstruction comparison, a global STCI exclusion, or a converse from splitting to two global equations.

## From exceptional normal divisors to the full filtered equation module

For a regular codimension-two embedding C in a smooth threefold, let I be its ideal and J=(F,G) a proper complete-intersection ideal contained in I. Set S=gr_I(O_X)=Sym(I/I²), H=in_I(J), and Q_n=H_n/(S_+ H)_n. The actual equation module J/IJ carries its induced I-filtration. The canonical comparison has an exact sequence

    0 -> Delta_n -> Q_n -> gr^n(J/IJ) -> 0,

where Delta_n=in_n(IJ)/(S_+ H)_n. In particular, minimal generators of the full initial ideal need not survive as independent generators of the filtered equation module. This is the comparison in [R-0030](../results/local_filtration_comparison_defect.md), with its full construction and counterexample in [the ideal-filtration supplement](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd).

The full initial ideal is itself not determined by the two displayed leading forms. In the regular transverse local ring, J=(x²,x²+y³)=(x²,y³), so the displayed order-two symbols generate only (X²), whereas the full initial ideal is (X²,Y³), of colength six. The [higher-initial investigation](../supplements/HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#explicit-cancellation-examples) gives further local examples and the prescribed characteristic-two quartic computation. None of these local models by itself constructs a global STCI.

Simultaneous carrier singularity is necessary for the comparison defect under the R-0030 hypotheses. The characteristic-two quartic has a fourth initial equation from cancellation and its comparison defect vanishes. [R-0031](../results/quartic_char2_fourth_equation_kernel.md) · [Open sole-support question](../FRONTIER.md#punctual-relative-defect-under-sole-support)

A [finite-flat supported length-five control](../results/supported_length_five_defect_specialization.md) has zero relative comparison defect but a nonzero defect on its actual closed transverse fiber. Its coefficient-specialized relative normal algebra has length eight while the actual closed algebra has length five. An exceptional-slice calculation needs a base-change argument to detect the punctual relative defect. Homogenizing the two equations gives an intersection cycle \(5[L]+2[D]\) with residual conic \(D\). The fixed-quartic sole-support question remains open.

Neither Delta_n nor cancellation is the saturated first-relation resultant defect of [R-0016](../results/nonsaturated_first_relation_resultant.md), the quasiprimitive residual-cycle divisor of [R-0019](../results/quasiprimitive_residual_cycles.md), or the rank shortfall of a global jet map. Identifying any two requires an additional comparison argument.

## Endpoint divisors as geometric repairs of extension classes

For a fixed obstruction \(o\in H^1(\mathbf P^1,\mathcal O(-r))\), \(r\ge2\), and an effective divisor of degree \(B\), write \(n=r-2\). Serre duality identifies the obstruction with a functional on \(H^0(\mathcal O(n))\). If the divisor is cut out by \(h\in H^0(\mathcal O(B))\), then the obstruction dies after twisting by that divisor precisely when
\[
\langle o,hq\rangle=0\quad\text{for all }q\in H^0(\mathcal O(n-B)).
\]
Thus allowing the divisor to vary asks for a nonzero kernel of a catalecticant multiplication map. A dimension argument supplies such a divisor for every scalar obstruction when \(B\ge\lfloor r/2\rfloor\); for a vector-valued obstruction the **same divisor** must lie in the kernels of all component maps. A prescribed socle boundary is still more restrictive.

This is a precise *cohomological* criterion, not a proof that the allowed socle divisor modifies the ambient embedded-lifting obstruction in this way. The missing comparison of obstruction complexes and the actual global homogeneous source are separate requirements. The detailed derivation and limits are in [the boundary supplement](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md), with the fixed-lower embedded criterion in [the one-step supplement](../supplements/BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md).

## A sextic source image and a distinct cubic obstruction

For the conditional movement-two (6,16) lane, the degree-six quadratic-symbol map has source dimension 23, kernel generated by the containing quadric cubed, rank 22 and target dimension 33. Its eleven independent image equations constrain the product of the moving root and its multiplier. A specified smooth torsion-two seed satisfies all eleven; for its selected sextic representative the next cubic comparison has the exact pairing \(-384\), and the seed fails the separate embedded second obstruction. Another sextic with the same quadratic symbol differs by eta*q³. The exact row annihilates this additional cubic direction, so the nonzero pairing excludes all sextic lifts of this specified seed. See [the complete all-lifts calculation](normalization_conductor_phase2_addendum.md#exact-failed-seed-the-row-also-kills-the-free-lift).

For a nonzero quadratic root \(f=au^2+buv+cv^2\), cubic compatibility has the undivided equations \(h_0=a\ell\), \(h_1=b\ell+am\), \(h_2=c\ell+bm\), \(h_3=cm\), where \(\deg\ell,\deg m\le7\). Multiplication by \(f\) is injective, with a sixteen-dimensional correction image in forty cubic coefficients and a twenty-four-dimensional quotient. Singular roots, multiplier zeros, the twenty-five second-obstruction pairings and full-root torsion remain separate constraints. See [the explicit source and coefficient calculation](normalization_conductor_phase2_addendum.md#coefficient-level-cubic-obstruction-without-elimination).

These global realization tests neither compute the punctual filtered equation-module defect nor produce a proper mate. For the specified seed, the kernel-direction check upgrades the cubic failure to an exclusion of every sextic lift with that symbol. The independently established second ambient obstruction excludes that root under its own bridge hypotheses. Neither test excludes the full (6,16) incidence.

## The gap between embedded multiple curves and global hypersurfaces

The actual degree-d normal-jet source is the image of global sections of I(d) in sections of the finite normal neighborhood. Rational coefficients and independently chosen symbols need not arise from the same global homogeneous form. The one-step note develops further fixed-degree source tests, but does not exclude an entire surviving degree-at-least-five family.

## Open interfaces

- [Punctual relative defect under sole support](../FRONTIER.md#punctual-relative-defect-under-sole-support).
- Vary lower embeddings, their boundary divisors and extension classes **together**; determine the full vanishing locus rather than only a generic obstruction.
- Apply global-source and properness tests to a surviving family of actual homogeneous pairs.
- Construct a justified comparison among the R-0016, R-0019 and R-0030 defects, with all finite-flatness and curvilinearity hypotheses explicit.

This document supplies the mechanism view; the linked current proof owners contain the actual arguments and their scope.


## Relation to the historical jet-discrepancy calculation

The [order-one result](../results/order_one.md) distinguishes the maximal-rank defect of successive global-section maps from the divisor D_j in a quasiprimitive saturated layer. The local comparison defect of R-0030 concerns the actual filtered equation module versus its initial generators, and is not automatically equal to either invariant. The quadric comparison divisor R and doubled divisor 2R are concrete finite-jet test cases, not a general identification of these three defects. Any proposed equality or implication needs an explicit comparison theorem and hypotheses.

## Source-preserved quartic-ancestor conormal and endpoint restrictions

These statements concern **quartic inverse-system ancestors**, not arbitrary STCI pairs or arbitrary-degree mates. Their proofs depend on the finite-flat quadruple, socle-pencil and complete quartic-fiber antecedents cited in the original notes.

The [intrinsic conormal splitting criterion](../supplements/LOCAL_COHOMOLOGY_CONORMAL_GEOMETRY.md) constructs V from the canonical triple ideal J by taking the torsion-free quotient of J/(I_C J). Its intrinsic extension has a line subbundle L cubed, twisted by the second defect, and a complementary conormal quotient. The actual two quartic targets map V surjectively onto the socle line O(-14), since their images form a basepoint-free pencil. The kernel has degree 2e-14, and the extension splits because H1(O(2e)) vanishes for e>=0. Therefore a common quartic ancestor necessarily has V=O(2e-14) direct sum O(-14). The criterion is necessary, not sufficient. For e=1, the remaining d2=1,2,3,4 strata require respective Hankel connecting-matrix ranks 3,2,1,0; in particular the d2=4 zero-extension/Gorenstein case remains possible at this stage. These are not STCI BF bounds.

The [corrected simultaneous-target bridge](../supplements/OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-socle-bridge-adversarial-auditmd) excludes primitive e=1,d2=0 common quartic ancestors under the accepted finite-flat and socle antecedents, using both target equations together. The actual image of a multiplier in the quadruple is a nonzero socle target; it must not be set to zero. The valid local equation retains that target, and elimination between the two multipliers yields the contradiction. The older single-multiplier pole argument is invalid for ancestors.

The [six defective e=1,d2=1 endpoints](../supplements/OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-localcoh-e1-d1-endpoint-ancestorsmd) are excluded as *ancestors*: four have a one-dimensional complete ambient quartic space, incompatible with two independent target images; two have a common cubic factor and reduce to degree-one multipliers, excluded by P-037. This does not rule out an arbitrary higher-degree mate for a remaining unique quartic carrier. Likewise the [principal open-chart rank result](../supplements/OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-mf6-principal-rank-open-independent-auditmd) gives dimension one for the complete quartic space on its specified open, not an all-mate carrier exclusion; boundary charts require their separate proofs.

The remaining defective ancestor strata and other directions must be checked with their actual extension classes and target images. None of these conditional exclusions can imply a universal STCI theorem by dropping their antecedents.

## Two additional October 8 ancestor exclusions

**Quadric first-quotient direction.** For the fixed rational quartic C of class (1,3) on the smooth quadric Q, the conormal direction A=-z/2, B=1 is precisely the direction inside Q. Its canonical double is 2C on Q. Any containing quartic F restricts to a section of O_Q(4,4)(-2C)=O_Q(2,-2), which has no sections. Thus both quartic ancestor equations would be divisible by Q, reducing to the prohibited common quadratic ancestor P-037. This excludes that **direction for every second-defect divisor**, conditional on the canonical-triple reduction and P-037; it does not exclude every positive-defect or Gorenstein stratum. [Source and complete 35-monomial rank check](../supplements/OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-localcoh-quadric-directionmd).

**Two algebraic defect-four directions.** For A=r*z, B=1 with 12r²+4r+3=0 and second-defect degree four, a genuine corrected triple has relation delta*m+theta*y²=0 with theta a nonzero constant, normalized to one. The complete seven-dimensional ambient double-quartic space has two primitive members and five coefficients (h,E)=(a_i*z^(i+2),z^i), i=0,...,4, with pairwise distinct a_i. Quartic containment is h=delta*E. Eliminating the two primitive coefficients leaves a seven-by-five matrix. For delta=d0+...+d4*z^4, its low and high minors are d0^4 and d4^4; when both vanish, the next minors are d1^5 and d3^5. For the remaining delta=d2*z², a diagonal minor has entries d2-a_i, at most one zero. Thus the kernel always has dimension at most one: no two independent quartics contain the triple. This excludes common quartic ancestors for **these two directions and every defect section**, not all defect-four directions or arbitrary-degree mates. [Exact source](../supplements/OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-localcoh-e1-d4-algebraicmd).

## Rational endpoint-family comparison

The [Step 1C endpoint-family synthesis](../supplements/LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md) preserves the complete first-family target-u exclusion and the incomplete second-family certificate. For the latter, 22 primitive geometric parameter points remain unresolved after the two quadratic exceptional factors are closed. These are exceptions to a certificate, not constructed ancestors. Both results concern specified pure-top endpoint directions, not all quartic ancestors or arbitrary mates.

**Later endpoint closure:** The earlier October 8 count of 22 unresolved second-family exception points was eliminated by the October 13 cubic/quartic field duals and the October 14 degree-fifteen fraction-free certificate. Both specified rational endpoint families are excluded under their actual tensor and pure-top assumptions. See [the updated endpoint synthesis](../supplements/LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md). Do not interpret the earlier count as the current frontier.

## P-044 dx=1 slice: exact five-coordinate saturation (October 7)

The [dx=1 saturation audit](../supplements/OCT7_SATURATION_REES_AND_CARRIER_CLASSIFICATION.md#2026-10-07-dx1-saturation-audit) proves a **slice-level** classification for P-044's normalized primitive-fourth obstruction, not a universal STCI theorem. Write `A=z²+az+x`, `B=1+bz+dz²`, impose `d=1/x`, and put `u=bx-a`, `t=xu`, `alpha=2a+1`, `beta=b+2`. The basepoint-free slice is precisely `D(t)`. Reconstructing all five original obstruction coordinates gives an ideal `L=(Q1,...,Q5)` whose saturation is the six-generator ideal

`L:t^infinity = J = (x beta²+alpha beta-2alpha², (4x+2)alpha beta-3alpha², beta³, alpha beta², alpha² beta, alpha³)`.

The exact certificates are `tJ subset L subset J` and `J:t=J`. The latter also follows from the free rank-four `Q[x]` quotient `R/J` with basis `1,alpha,beta,gamma`, `gamma=beta²-(8/3)alpha beta`: multiplication by t has determinant `[x(1/2-2x)]^4`, hence is injective. The radical is `(alpha,beta)`, so the basepoint-free zero locus is `a=-1/2`, `b=-2`, `x!=0,1/4`. The scheme is **nonreduced**; its underlying support alone does not preserve the four-dimensional quotient structure. The formerly proposed three-coordinate saturation is false: all five coordinates are necessary. The note checks agreement with P-045 on this slice, without claiming that the slice exhausts P-044's full parameter space. Preserve this exact ideal as a distinct boundary calculation rather than treating its previous audit gap as current.

## Primitive e=1 triples versus defective d2=4 ancestor directions

The [October 7 primitive-triple audit](../supplements/OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-independent-auditmd) distinguishes a stronger quartic-carrier statement from the weaker quartic-ancestor rank tests. In characteristic zero, for first quotient `O(-6)` and `D2=0`, the basepoint-free primitive directions comprise one principal torus orbit and three boundary orbits. The principal and two algebraic boundary orbits have complete two-dimensional quartic pencils with forced ruling-line base components; the comparison-zero boundary has quartics divisible by the unique quadric. The fixed-line observation alone does **not** exclude arbitrary mates, since a line can meet C at its forced intersection points. The subsequent normalizations and full inverse-support analysis in the independent audit exclude the pure quartic carriers for mates of any positive degree under the stated MF6 hypotheses. Do not preserve the earlier fixed-line-only argument as a complete all-degree proof. The defective `D2>0` cases remain outside this primitive result.

By contrast, the [October 8 algebraic d2=4 audit](../supplements/OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-localcoh-e1-d4-independent-auditmd) is a **common-quartic-ancestor** exclusion for precisely the two directions `A=r z, B=1`, `12r²+4r+3=0`, uniform in every genuine quartic defect section. The correction coefficient theta must be nonzero: theta zero would produce torsion `(R/(delta))*m` at a zero of delta and violate finite flatness. Normalizing theta=1 gives `y²=-delta*m` and quartic containment `h=delta E`. The complete quartic source has dimension seven; a seven-by-five matrix has rank at least four for every delta, including repeated and infinity zeros, leaving at most one containing quartic. Two independent target classes are therefore impossible **conditional on the canonical-triple ancestor reduction**. This does not exclude all d2=4 directions or arbitrary-degree mates.

## Six degree-one defective endpoints: fixed-carrier exclusion stronger than ancestor rank

The [October 7 endpoint audit](../supplements/OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-d1-endpointsmd) treats all six `e=1,d2=1` boundary directions (`a0=0` or `b1=0`), **not** the principal `a0*b1!=0` locus or the `d2=2` stratum. For each endpoint the complete ambient quartic space is computed from all 35 monomials. At the rational root `r=-1/2`, the quartics are a fixed cubic times linear forms; at either algebraic root of `12r²+4r+3=0`, the space is one-dimensional and generated by an explicit irreducible quartic. The latter has third-layer defect `d3=4`, incompatible with MF6 `(d2,d3)=(1,3)`, but that numerical contradiction alone is not an arbitrary-mate exclusion.

The stronger fixed-carrier result uses an explicit dominant birational parametrization of an affine chart of each algebraic quartic by `k[u,v,(u+kappa)^(-1)]`, where `3kappa²-2kappa+1=0`, with full inverse support of C equal to the diagonal `v=u`. A hypothetical mate pullback must be `c(v-u)^n(u+kappa)^k`. Comparing the two branches over the singular line forces `k=-n` and `(-kappa)^n=1`; conjugation and `Norm(kappa)=1/3` contradict `n>0`. Coordinate reversal and torus symmetry transfer the argument to the other endpoints. This proves an **all-degree mate exclusion for these six fixed endpoint carrier directions**. The open principal `d2=1` locus and the `d2=2` stratum are not covered by this scoped argument. This strengthens, without contradicting, the earlier ancestor-only quartic-space statement above; the general R-0001 theorem subsequently excludes all integral quartic carriers by a different global route.

## Defective e=1 MF6 structural conditions

The [October 7 defective structural note](../supplements/OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-defective-structuralmd) gives a local Hilbert–Burch presentation for a positive-second-defect canonical triple: `J=(delta*m-gamma*y^2,m*y,m^2,y^3)`, with gamma invertible at zeros of delta. Its torsion-free generator bundle has extension `0 -> L^3(D2) -> V -> M(-D2) -> 0`, where `L=O(-6), M=O(-8)`. The `-D2` twist in the quotient is essential. The normalized cubic residue uses `delta^2*f3`, yielding a class in `H1(O(-10+2*d2))` that must vanish after mapping to `H1(O(-10+d2+d3))`.

For `(d2,d3)=(1,3)` the necessary condition is a nonzero kernel of the five-by-three Hankel matrix on seven Laurent coefficients (all ten maximal minors vanish). For `(2,2)` the class in `H1(O(-6))` must vanish in all five coordinates. These conditions are not sufficient for a quartic carrier or mate. The first quadratic-cocycle killing test gives a sextic direction locus `c1*c3-c2^2=0` for `d2=1`; for `d2=2`, a defect quadratic `delta0+delta1*z+delta2*z^2` must satisfy `delta0*c1+delta1*c2+delta2*c3=0`. In each case finite flatness imposes an additional no-common-zero condition on delta and the corrected coefficient gamma. Primitive obstruction-zero directions cannot acquire a genuine positive defect of degree at most three by multiplying their unique correction by delta.

The [primitive progress note](../supplements/OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-progressmd) records the exact `H1(O(-4))` quadratic cocycle, three Laurent obstruction coordinates, and classification into one principal and three boundary torus orbits. Its incomplete conjugate-orbit checkpoint was superseded by the later [independent audit](../supplements/OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-mf6-e1-independent-auditmd). The six degree-one boundary directions have the stronger all-degree exclusions recorded above. The principal `d2=1` sextic and `(2,2)` conditions remain open within this structural method, without contradicting the separate global quartic-carrier exclusion R-0001.

## Mixed (4,6): Fitting divisor and pole strata

The [October 5 mixed-six calculation](../supplements/MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mixed46-poles) assumes a finite-flat quasiprimitive length-six Gorenstein algebra, locally free Banica–Forster pieces, and perfect multiplication pairings. For defect divisors `0<=D2<=D3`, the graded pieces are `O,L,L^2(D2),L^3(D3),L^4(D2+D3),L^5(D2+D3)`. The coordinate-independent first-normal cokernel Fitting divisor satisfies `A=D3+min(D2,D3-D2)`, with the minimum taken pointwise. The proof computes torsion `T=N/yB`: its length is `ord(D2+D3)`, while `length(T^2)=max(ord D2-ord(D3-D2),0)`, and `length(T/T^2)=ord A`. In particular `D3<=A<=D2+D3`; neither extreme equality is universal.

For degree pair `(4,6)`, the seven necessary numerical types are `e=0: (d2,d3)=(1,8),(2,7),(3,6),(4,5)` and `e=1: (0,4),(1,3),(2,2)`. Their coarse nonregular pole lengths reduce to `e=0: p=1,2,3,4` and `e=1: p=4,5,6`. This is a restriction on possible strata, not a realization or an STCI exclusion. The [regular-ratio proof](../supplements/MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mixed46-regular) separately excludes only the two pure constant horizontal directions when `e=0` and the quotient ratio is globally regular. Its quadric-residual and cubic-jet argument does not treat mixed directions, e=1, or nonregular pairs. The [earlier rank-six audit](../supplements/MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mf6-further-audit) records the saturated-lattice hypotheses and the remaining `(4,5)` defect case.

## The geometric realization problem for successive thickenings

The characteristic-zero conormal bundle of the fixed quartic is balanced, whereas the characteristic-two splitting changes [R-0020](../results/quartic_conormal_characteristic_jump.md). The prescribed characteristic-two fourth-equation kernel [R-0031](../results/quartic_char2_fourth_equation_kernel.md) makes a key distinction concrete: cancellation-generated higher initials cannot be discarded merely because two low-order symbols appear dependent. The prescribed \(\mu_4\) degeneration [R-0021](../results/quartic_mu4_degeneration.md) likewise warns that flat arithmetic specialization need not preserve reduced support. Neither example proves a universal characteristic-zero obstruction.

The [weighted-initial note](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md#weighted-initials-normal-boundary) uses valuations of coefficient functions over \(k(C)\) to track special-point Newton changes. Those coefficients depend on chosen normal coordinates; intrinsically their leading terms are sections of symmetric powers of the conormal bundle. This is a *methodological proposal*, not an established coordinate-independent tropical obstruction. The [normal torsion/genus note](../supplements/CURVILINEAR_GENUS_AND_DEFECTS.md#normal-torsion-spectral-genus-budget) further distinguishes ordinary torsion from saturation divisors: counting both as independent genus contributions double-counts the same phenomenon in its stated curvilinear setting.

### A finite, checkable continuation

Choose a specific surviving pair of degrees at least five, or a specified lower embedded thickening. Record (i) its generic transverse algebra and **full** initial ideal; (ii) the saturation and exceptional-point defect of each conormal layer; (iii) the exact obstruction class and allowed boundary divisor for the next lift; and (iv) the image of actual global homogeneous sections in the required jets. At each step distinguish failure of a necessary condition from failure to construct a solution. Finally check properness and actual residual support independently. The [boundary repair](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md) and [one-step completion](../supplements/BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md) analyses provide scoped tools, not a theorem that this procedure always decides STCI.

**Remaining mathematical gap:** there is no established general implication from a generic or graded root configuration and its local repair data to a pair of global equations with sole reduced support. Conversely, there is no established theorem excluding all such configurations when first relations are nonsaturated or the comparison defect is punctual.

## Local comparison, saturation, and the unresolved singularity interface

[R-0030](../results/local_filtration_comparison_defect.md#statement) compares
minimal equations of the full initial ideal with the filtration of the actual
equation module. Its [proof](../arguments/filtered_equation_comparison.md#local-comparison-and-the-punctual-defect)
gives the generic generator count, DVR length formula, and smooth-carrier
criterion under their respective hypotheses. See the
[sole-support question and controls](../FRONTIER.md#punctual-relative-defect-under-sole-support).

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

To pass from an ambient source to a specific normal symbol, the map to \(H^0(\operatorname{Sym}^m N_C^\vee(d))\) must be computed. To pass from compatible symbols to an actual supported complete intersection, one must also impose a common global lift, properness and degree exhaustion. See [the ideal-power proof](formal-normal-intersection.md#12-ordinary-ideal-powers-on-a-smooth-quadric-complete-proof) and [the global-source treatment](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md).

## Characteristic-two comparison and arithmetic scope

The fixed quartic pair in R-0021 is flat over the integers. Its characteristic-zero fiber contains four reduced quartics, whereas its characteristic-two fiber has sole reduced support C and generic transverse length four. The conormal extension changes splitting type (R-0020). In the special fiber, R-0031 identifies the cancellation-generated fourth initial equation with the filtered equation-module kernel O(-24); its comparison defect is zero.

R-0012 rules out a constrained flat embedded lift of this prescribed special scheme over Z_(2) or Z_2 with generic reduced support C. It does not contradict the integral family with four generic components or address arbitrary ramified bases. These are separate tests of normal structure, full initial equations, and global support.

## The shared duality mechanism and its limit

The boundary-repair catalecticant and the local-cohomology polynomial left dual are two concrete uses of duality on an actual source map. In the first, Serre duality changes a pole-repair problem into annihilation of a multiplication subspace; in the second, a row annihilating the complete tensor image separates a target class from the image. Both mechanisms work over any coefficient field where the displayed objects and maps are defined. They do not identify their obstruction spaces, and no theorem transfers a repair divisor from one problem to the other. The same global homogeneous source must remain fixed when several conditions are stacked. A separate divisor for each component or independently chosen normal jets would change the existence question.

The [complete endpoint owner](../supplements/LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md) now assembles both rational target-u family exclusions with parameter coverage, all affine corrections, exact factor closure and actual tensor reconstruction. Its rational certificate scope is characteristic zero. The [positive-characteristic construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) remains the global control: these duality mechanisms constrain specified sources; they do not exclude STCI in every characteristic.

A precise proposed cross-topic bridge is to compare the nonsaturated-first-relation/resultant defect of R0016 with the saturated quasiprimitive residual zero-cycle of R0019 **using the actual global equations and a proper auxiliary intersection**. The two constructions have different hypotheses and targets. A general divisor inequality has not been established. Any comparison must identify correction terms when ordinary normal flatness, generic curvilinearity, saturation or properness fails, rather than equate the two numerical defects or infer an extra curve from a vertical exceptional cycle.

## Retired exact computational sources: filtration and principal direction

The following preserve the mathematical statements of four historical checkers, **not** claims of actual mates or unconditional STCI exclusions.

### BF e=1, d2=1 annihilator

For `xi=c1 z^-1+c2 z^-2+c3 z^-3` in `H1(O(-4))`, a linear `delta=d0+d1 z` annihilates `xi` after twisting to `H1(O(-3))` exactly when
```
[c1 c2; c2 c3] [d0;d1]=0,  c1*c3-c2^2=0,
c1=-b1(2a0*b1+12a1^2+16a1*b0+9b0^2),
c2=-(2a1+b0)(8a0*b1+12a1^2+4a1*b0+3b0^2),
c3=-2a0(2a0*b1+36a1^2+16a1*b0+3b0^2).
```
For `Delta=a0*b1-a1*b0`, `det=-3Delta^2 Q`. A reduced cover polynomial is `Qred=16x^2+(72+64r+24r^2)x+36+72r+52r^2+16r^3+3r^4`; its discriminant is `64(r+2)^2(6r^2+8r+24)`, with nonsquare last factor over `QQ(r)`. Sample tuples `(a0,a1,b0,b1)` and their annihilators are `(-8,-3,2,-3):(4,-1)`, `(-8,-2,-4,-4):(2,-1)`, `(-8,-1,-2,-4):(2,-1)`. These test the obstruction-side condition, not ambient equations.

### Principal e=1, d2=1 weighted curve

With weights `wt(p,r,b)=(2,1,1)`, the exact weighted equation is
```
H=8p^3-(64r^2+128rb+16b^2)p^2
 +(96r^4+512r^3b+592r^2b^2+128rb^3+6b^4)p
 -(576r^6+960r^5b+880r^4b^2+544r^3b^3
   +220r^2b^4+60rb^5+9b^6).
```
Its discriminant in `p` is `-1728(2r-b)^2(2r+b)^4 S6` with `S6=93b^6+676b^5r+1996b^4r^2+3552b^3r^3+7984br^4+10816r^5b+5952r^6`. On `b=1` the affine singular ideal is `(8p+24r^3+12r^2-38r-3,(2r-1)(2r+1)^3)`, yielding a node at `(2,1/2)` and a tacnode at `(-2,-1/2)`. The historical exact computation finds an absolutely irreducible genus-one normalization with `Y_E^2=X_E^3+96X_E-448`, `j=2048/3`. Its birational chart uses `x=r+1/2, W=(p+2-4x)/x^2, Y=(A(W)x-C(W))/W` with `A(W)=-W^3+8W^2-12W+72`, `C(W)=2(W^2-6W+36)`; inverse `x=(C+WY)/A,r=x-1/2,p=-2+4x+Wx^2`. Exceptional denominators require separate charts.

In the principal frame `A=1+rz,B=1+pz`, the cocycle is `-(2A+zB)(12A^2+3z^2B^2+4z^2(A'B-AB'))/(8z^5)`. Its negative Laurent coefficients satisfy `H=64(c1*c3-c2^2)` on `b=1`. For `delta=-8c2+8c1z` and the corresponding correction `Gamma`, the computed resultant is `Res_z(delta,Gamma)=p^4(2p+12r^2+16r+9)^4/8`. This establishes a flatness test on the stated open, not the remaining ambient quartic/cubic incidence.

### First-normal octic discriminant candidate

The historical principal-weighted construction used 18 independent quartic source forms, a 23-by-18 contact matrix and three polynomial kernel columns of weighted degrees `9,9,10`. For the first generator, `hhat=(p-rb)*coefficient_m(F)` in the actual balanced frame is a binary octic. The candidate equation is the *fixed* 14-by-14 Sylvester determinant `Res(partial_s hhat,partial_t hhat)` for two degree-seven binary gradients, retaining infinity roots. Its weighted degree is 210. A nonzero modular check on `H=0` at `(p,r,b)=(4,2,1)` modulo 101 shows it is not identically zero on the principal curve. The stated double-cover Bézout argument bounds distinct candidate points by 630; this is only a **necessary** candidate set, not mate existence or exclusion.

### CI(5,8) multiplicity-ten necessary filtration degrees

For `l=-7,-6,-5`, put `T=-38-9l` and defect sequence `(0,0,a,b,c,T-c,T-b,T-a,T,T)`. Nonnegativity, symmetry and superadditivity reduce, in the enumerated range, to
`0<=a<=b<=c; 2a<=c; 2c<=T; a+b+c<=T; 3b<=T`.
The Euler check is `10+45l+sum(defects)=-180`. After the separate P-010 primitive-triple exclusion for `l=-7,a=0`, the respective counts are `198,97,13` (total 308). This is a numerical census, not an embedded-structure classification.

These four historical scripts supplied exact polynomial checks; their distinct formulas, hypotheses, limitations and algorithms are retained here without preserving generated artifacts.


## Consolidated historical supplement: `research/supplements/E2_PRIMITIVE_QUARTIC_INCIDENCE.md`

The following historical mathematical content is preserved verbatim with its original hypotheses, limitations, and proof status. Relative links refer to the original supplement location.

# E2 obstruction, primitive structures, and quartic incidence

Consolidated mathematical source material. Sections retain original claims, calculations, hypotheses, and qualifications; their inclusion does not upgrade unverified arguments to theorems.

---

## 2026-10-05-e2-full-obstruction

# e=2 quartic-carrier obstruction: stabilizer, generic cross-section, and surviving family

Date: 2026-10-05

Status: **characteristic-zero continuation**. The ambient-stabilizer statement and the three-parameter exclusion are PROVED; the full four-parameter obstruction formulas are an exact computational result with strong cross-checks, including exact specialization checks. The explicit surviving family and the resulting falsification of the universal cubic exclusion are independently reconstructed and verified. Nothing here constructs a quartic carrier or an STCI presentation.

Throughout,
[
C_0=[s^4:s^3t:st^3:t^4]subsetmathbf P^3.
]

## 1. Ambient stabilizer — PROVED

The embedding linear system is
[
W=langle s^4,s^3t,st^3,t^4anglesubset H^0(O_{mathbf P^1}(4)).
]
In characteristic zero the only (PGL_2) transformations preserving (W) are
[
zmapstolambda z,qquad zmapstolambda/z.
]
The kernel of
[
operatorname{Stab}_{PGL_4}(C_0)	ooperatorname{Aut}(mathbf P^1)
]
is trivial. Hence
[
oxed{operatorname{Stab}_{PGL_4}(C_0)congmathbf G_mtimesmathbf Z/2.}
]
In the formal coordinates used below the torus acts by
[
zmapstolambda z,qquad Umapstolambda^4U,qquad Vmapstolambda^3V.
]
There is no hidden continuous ambient symmetry reducing a general (e=2) quotient to the earlier two-parameter family.

## 2. Generic e=2 symmetry cross-section

On (A_2B_0
e0), projective scaling plus the genuine ambient torus normalize a general (e=2) quotient to
[
oxed{A=x+az+z^2,qquad B=1+bz+dz^2.}
]
This is a generic cross-section to the actual symmetry, **not literally an affine chart of (P^5)**.

The resultant is
[
oxed{Delta=1-ab+a^2d-2dx+b^2x-abdx+d^2x^2.}
]
Basepoint-free is equivalent to (Delta
e0).

On (xd
e0), inversion acts by
[
oxed{(x,a,b,d)mapstoleft(rac{x}{d^2},rac ad,rac bx,rac d{x^2}ight).}
]
Thus the previously studied (x=b=0) family is codimension two in the essential generic moduli.

## 3. Formal-neighborhood audit — independently audited

The nonlinear two-chart transition was independently reconstructed. A crucial point is
[
oxed{w
e1/z}
]
off the reduced curve. Freezing (w=1/z) destroys higher-order information contributing to the obstruction. Calculations using a frozen opposite-chart coordinate must not be reused unless separately corrected.

Several exploratory slice/factorization claims from the research conversation were discarded during this audit and are not used here.

## 4. Three-parameter b=0 family — PROVED

For
[
A=x+az+z^2,qquad B=1+dz^2,
]
put
[
Delta_0=1+a^2d-2dx+d^2x^2.
]
The quadratic graph corrections and all five cubic obstruction numerators (G_i(a,d,x)) were independently regenerated. Exact Gröbner reduction gives
[
oxed{Delta_0in(G_1,ldots,G_5).}
]
Consequently
[
G_1=cdots=G_5=0LongrightarrowDelta_0=0.
]
Hence no basepoint-free member of this entire three-parameter family extends from the relevant primitive triple to a primitive quadruple. This strictly strengthens the earlier (x=b=0) result.

## 5. Full four-parameter cubic obstruction — exact computation with strong cross-checks

For
[
A=x+az+z^2,qquad B=1+bz+dz^2,
]
the cubic mismatch has form
[
M_3=rac{N(z;x,a,b,d)}{32z^{25}Delta^3}.
]
The five relevant coefficients of (N) are each exactly divisible by (Delta^2). Therefore
[
oxed{Omega_i=rac{G_i(x,a,b,d)}{32Delta},qquad i=1,ldots,5.}
]
The exact (G_i) are persisted in
`../computations/e2_full4_obstruction_2026-10-05.txt`.

Exact checks:
- (b=0) reproduces all five independently audited three-parameter obstruction polynomials;
- (x=b=0) reproduces the retained two-parameter obstruction polynomials.

## 6. Universal cubic e=2 exclusion — FALSE

The attempted implication
[
oxed{Omega=0LongrightarrowDelta=0}
]
is **FALSE**.

On (dx=1), write (u=bx-a). Then
[
Delta=rac{u^2}{x}
]
and all five obstruction numerators factor as (G_i=uQ_i). On
[
a=-rac12,
]
all five original (G_i) vanish when
[
u=rac12-2x,
]
equivalently (b=-2). Thus
[
oxed{A=z^2-rac12z+x,qquad B=1-2z+rac1xz^2}
]
satisfies
[
oxed{G_1=cdots=G_5=0.}
]
Its resultant is
[
oxed{Delta=rac{(4x-1)^2}{4x}.}
]
For (x
e0,rac14), the pair is basepoint-free. Therefore the corresponding (e=2) primitive triple extends to a primitive quadruple.

This falsifies the proposed universal **first nontrivial extension-obstruction strategy**. It does not construct a quartic carrier.

## 7. Scope and revised frontier

Do **not** infer:
- existence of an (e=2) quartic carrier;
- existence of an STCI presentation;
- failure of the desired no-quartic-carrier theorem for (C_0);
- failure of the global STCI conjecture.

The surviving family proves only that the first nontrivial extension obstruction is insufficient.

The immediate (e=2) question is:

> Exactly what infinitesimal multiplicity/order does a genuine (e=2) quartic carrier force, and does the explicit surviving primitive quadruple extend through the next required stage?

The sharp test family is
[
A=z^2-rac12z+x,qquad B=1-2z+x^{-1}z^2.
]

Continued higher-order (e=2) computation is not automatically the highest-value global strategy. Other live branches remain:
- equivariance/representation-theoretic interpretation of (Omega);
- (e=1);
- (e=0);
- whether the local-cohomology route can treat (e=0,1,2) uniformly.

All formal calculations in this note currently carry the characteristic-zero caveat.


---

## 2026-10-05-e2-primitive-septuple

# Primitive-septuple theorem for the (4,7), e=2 branch

Date: 2026-10-05

## Status

**PROVED / INDEPENDENTLY AUDITED (characteristic zero).**

This note records the structural consequence of an actual complete-intersection
carrier. It is independent of the classification of the P-044 obstruction
zero locus.

Let
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset \mathbf P^3
\]
and suppose
\[
Y=V(F_4,G_7),\qquad Y_{\mathrm{red}}=C,
\]
is a characteristic-zero complete intersection whose quasiprimitive
Bănică--Forster branch has \(e=2\).

## Theorem

Then \(Y\) is a globally primitive multiplicity-seven structure of type
\[
L=O_{\mathbf P^1}(-5).
\]
If the Bănică--Forster graded pieces are
\[
E_i=L^i(D_i),\qquad i=0,\ldots,6,
\]
then
\[
D_2=D_3=D_4=D_5=D_6=0.
\]

Moreover, writing
\[
M=\ker(N_C^*\twoheadrightarrow L),
\]
one has
\[
M=O_{\mathbf P^1}(-9)
\]
and the primitive complete-intersection conormal sequence is
\[
0\longrightarrow L^7
\longrightarrow O_C(-4)\oplus O_C(-7)
\longrightarrow M\longrightarrow0.
\]
Thus its kernel is naturally
\[
K\simeq L^7=O_{\mathbf P^1}(-35).
\]

Consequently every genuine \((4,7),e=2\) carrier determines a basepoint-free
P-044 zero, and its quartic generator contains the corresponding canonical
primitive triple \(C_3\).

## Proof

For a smooth rational quartic in characteristic zero,
\[
N_C^*\simeq O_{\mathbf P^1}(-7)^2.
\]
The \(e=2\) quotient is therefore
\[
N_C^*\twoheadrightarrow L,\qquad L=O_{\mathbf P^1}(e-7)=O(-5).
\]

The complete intersection has degree \(4\cdot7=28\). Since \(\deg C=4\),
its generic multiplicity along \(C\) is seven. Its arithmetic genus is
\[
p_a(Y)=1+\frac{4\cdot7(4+7-4)}2=99,
\]
hence
\[
\chi(O_Y)=-98.
\]

For a quasiprimitive multiplicity-seven curve, the Bănică--Forster
Cohen--Macaulay filtration has line-bundle quotients
\[
E_i=L^i(D_i),
\]
where \(D_1=0\) and the defect divisors \(D_i\) are effective. Additivity in
the filtration gives
\[
\chi(O_Y)=\sum_{i=0}^6\chi(E_i).
\]
Since \(C\simeq\mathbf P^1\) and \(L=O(-5)\),
\[
\chi(E_i)=1-5i+\deg D_i.
\]
Therefore
\[
-98
=7-5(1+\cdots+6)+\sum_{i=2}^6\deg D_i
=-98+\sum_{i=2}^6\deg D_i.
\]
Thus
\[
\sum_{i=2}^6\deg D_i=0.
\]
Effectivity forces
\[
D_2=\cdots=D_6=0.
\]
In the Bănică--Forster quasiprimitive filtration these defects measure exactly
the isolated failure of primitivity, so their vanishing makes \(Y\) globally
primitive.

The determinant of
\[
0\to M\to O(-7)^2\to O(-5)\to0
\]
gives
\[
M=O(-9).
\]
For a primitive multiplicity-seven extension, the standard primitive conormal
sequence (Bănică--Forster, Proposition 2.3 in the convention audited for this
project) gives
\[
0\to L^7\to \nu_Y|_C\to N_C^*\to L\to0.
\]
Because \(Y=(F_4,G_7)\),
\[
\nu_Y|_C=O_C(-4)\oplus O_C(-7)
       =O_{\mathbf P^1}(-16)\oplus O_{\mathbf P^1}(-28).
\]
Its image in \(N_C^*\) is \(M\), yielding
\[
0\to L^7\to O_C(-4)\oplus O_C(-7)\to M\to0.
\]
Hence
\[
K\simeq L^7=O(-35).
\]

Finally a primitive septuple has canonical primitive truncations
\[
C=C_1\subset C_2\subset C_3\subset C_4\subset\cdots\subset C_7=Y
\]
associated with the same quotient \(N_C^*\twoheadrightarrow L\). Therefore its
canonical triple extends to a primitive quadruple, so its quotient parameters
are a basepoint-free P-044 zero. The actual quartic \(F_4\) contains \(Y\), and
therefore contains \(C_3\).

## First-normal kernel warning

Before global primitivity or first-normal surjectivity is known, one must not
use
\[
\deg K=e-4b-9
\]
unconditionally. If the first-normal pair has common-zero/cokernel divisor
\(A\), the image is \(M(-A)\), and determinant bookkeeping gives
\[
\boxed{\deg K=e-4b-9+\deg A.}
\]
Only after \(A=0\) is established does the simpler formula apply. For the
present primitive \((4,7),e=2\) structure it gives \(\deg K=-35\).

In particular, do not argue that a named septic lies in \(I_C^2\), or that one
named first-normal section is individually nowhere zero. Locally one may have
\[
F=x,\qquad G=ax+y^7.
\]
The pair generates the complementary conormal line.

## Separate audited calculation: cubics through the double

This calculation is useful for stratification but is **not** a consequence of
the primitive-septuple theorem.

On \(x_0=1\), with moving coordinates
\[
x_1=z,\qquad x_2=z^3+v,\qquad
x_3=z^4+u+\frac32zv,
\]
the first jets are
\[
[q]=u+\frac12zv,\qquad [A_3]=v,
\]
\[
[B_3]=-z^2u+\frac12z^3v,\qquad [D_3]=-2z^5u.
\]
For a double defined by
\[
u=A(z)\epsilon,\qquad v=B(z)\epsilon
\]
and a cubic
\[
H=\ell q+\alpha A_3+\beta B_3+\gamma D_3,
\]
the condition that \(H\) contain the double is
\[
A(z)(\ell-\beta z^2-2\gamma z^5)
+B(z)\left(\frac12z\ell+\alpha+\frac12\beta z^3\right)=0.
\]

For
\[
A=z^2+az+x,\qquad B=1+bz+dz^2,
\qquad
\ell=\lambda_0+\lambda_1z+\lambda_2z^3+\lambda_3z^4,
\]
this is the rank-drop condition for
\[
M_2=
\begin{pmatrix}
x&0&0&0&1&0&0\\
a+\frac12&x&0&0&b&0&0\\
1+\frac b2&a+\frac12&0&0&d&-x&0\\
\frac d2&1+\frac b2&x&0&0&\frac12-a&0\\
0&\frac d2&a+\frac12&x&0&\frac b2-1&0\\
0&0&1+\frac b2&a+\frac12&0&\frac d2&-2x\\
0&0&\frac d2&1+\frac b2&0&0&-2a\\
0&0&0&\frac d2&0&0&-2
\end{pmatrix},
\]
with columns
\[
(\lambda_0,\lambda_1,\lambda_2,\lambda_3,\alpha,\beta,\gamma).
\]
Thus
\[
H^0(I_{C_2}(3))\ne0\iff \operatorname{rank}M_2<7.
\]
For the explicit P-044 survivor
\[
a=-\frac12,\qquad b=-2,\qquad d=x^{-1},
\]
the kernel is generated by
\[
(-4x^3,8x^3,-2x,4x,4x^4,4x^2,1),
\]
recovering the P-045 cubic.

**OPEN:** there is no theorem that a genuine \((4,7),e=2\) carrier must satisfy
this cubic rank drop. Do not impose it as a carrier equation without a separate
proof.

## Consequence for the frontier

Every genuine \((4,7),e=2\) carrier must satisfy both
\[
\text{P-044}=0
\]
and
\[
H^0(I_{C_3}(4))\ne0.
\]
These conditions are necessary, not sufficient: quartic containment of
\(C_3\) does not by itself prove compatibility through \(C_4,\ldots,C_7\).

The immediate \(e=2\) task is therefore to derive the general algebraic
incidence condition
\[
H^0(I_{C_3(A,B)}(4))\ne0
\]
in the moving \(e=2\) coordinates and intersect it with the basepoint-free
P-044 obstruction locus before attempting unrestricted P-044 saturation or
higher primitive obstructions.


---

## 2026-10-05-e2-quartic-incidence

# e=2 quartic incidence: first exact compression and chart stratification

Date: 2026-10-05

## Status

**EXACT COMPUTATION / COMPUTATIONAL CROSS-CHECK.** This note does not classify the quartic-incidence locus and does not eliminate the characteristic-zero (4,7), e=2 branch.

## Direct quartic basis

For a degree-four monomial with exponent vector (i0,i1,i2,i3), restriction to (1,z,z^3,z^4) is z^(i1+3i2+4i3). The 35 monomials have 17 distinct weights, hence the kernel has dimension 18.

The verifier chooses differences of equal-weight monomials. In the notation (weight; exponent; reference exponent), the basis is:

    (3;(3,0,1,0);(1,3,0,0))
    (4;(2,1,1,0);(0,4,0,0))
    (4;(3,0,0,1);(0,4,0,0))
    (5;(2,1,0,1);(1,2,1,0))
    (6;(1,2,0,1);(0,3,1,0))
    (6;(2,0,2,0);(0,3,1,0))
    (7;(1,1,2,0);(0,3,0,1))
    (7;(2,0,1,1);(0,3,0,1))
    (8;(1,1,1,1);(0,2,2,0))
    (8;(2,0,0,2);(0,2,2,0))
    (9;(1,0,3,0);(0,2,1,1))
    (9;(1,1,0,2);(0,2,1,1))
    (10;(0,2,0,2);(0,1,3,0))
    (10;(1,0,2,1);(0,1,3,0))
    (11;(1,0,1,2);(0,1,2,1))
    (12;(0,1,1,2);(0,0,4,0))
    (12;(1,0,0,3);(0,0,4,0))
    (13;(0,1,0,3);(0,0,3,1))

Thus h^0(I_C(4))=18 is reproduced directly without using a preselected generating set.

## Canonical triple and matrices

Use A=x+az+z^2, B=1+bz+dz^2 and Delta=1-ab+a^2d-2dx+b^2x-abdx+d^2x^2. With the exact Bezout pair sA+tB=1, the canonical triple is u=A eps-t gamma_U eps^2 and v=B eps+s gamma_U eps^2 in the checked moving coordinates.

The general gamma_U was independently reconstructed from the moving transition. Its specialization to a=-1/2, b=-2, d=x^(-1) agrees identically with the independently audited P-045 formula.

For each basis quartic F_j, write F_j|C3 = J_1j eps + J_2j eps^2 mod eps^3. Both jet polynomials have degree at most 14. Multiplication of the second jet by Delta clears its parameter denominator on D(Delta). Coefficient comparison gives two 15 x 18 exact matrices M^(1) and M^(2), hence a 30 x 18 stacked matrix.

## Generic rank and a concrete six-dimensional chart

At (x,a,b,d)=(2,3,5,7), Delta=57, exact ranks are rank M^(1)=12 and rank stacked=18. The same ranks occur at the exact rational basepoint-free points (1,2,-1,3), (3,-2,4,1), and (2/3,1,2,-1). At all four points the induced second-order map on ker M^(1) has rank 6.

Using generic pivot columns (0,1,2,3,4,5,6,8,10,13,14,16) and coefficient rows 0,...,11, the 12 x 12 first-order pivot minor factors exactly as

    det P = d^7 (b+2) Delta / 128.

Hence on D(d(b+2)Delta) one has the explicit rational kernel parametrization N=(-P^(-1)Q; I_6), after ordering pivot and free columns, and reduced obstruction R=M^(2)N.

The symbolic entries of R have not yet been recorded as durable formulas. The next calculation should fraction-free reduce this R, factor its entries/minors, and seek a small rank certificate.

## P-045 is a lower first-order rank stratum

For P-045, a=-1/2, b=-2, d=x^(-1). The displayed rank-12 chart degenerates because b+2=0, but this is not merely a bad pivot choice. At x=1/2,1,2,3,-1 the verifier obtains rank M^(1)=11. Thus quartics containing C2 form a seven-dimensional space on P-045, not the generic six-dimensional space.

On that seven-dimensional kernel the second-order map has rank 3, so the full stacked rank is 14 and h^0(I_C3(4))=4. As a stronger symbolic regression, the verifier checks over Q(x) that H_x x_0, H_x x_1, H_x x_2, H_x x_3 have zero first and second jets on the canonical triple.

Therefore H^0(I_C3(4)) != 0 iff ker R != 0 for a fixed 18 x 6 kernel matrix is only a chartwise statement on the rank-12 locus. The full incidence locus must also include lower-rank strata of M^(1), beginning with P-045.

## Consequence for P-044 intersection

The target remains V(G_1,...,G_5) intersect quartic incidence intersect D(Delta), but computation should be stratified: (1) on rank M^(1)=12 use six-dimensional kernel charts and reduced R; (2) analyze rank M^(1)<=11 separately. P-045 lies in the second stratum and is already geometrically excluded by P-045.

This prevents saturation by a generic kernel-chart denominator from accidentally deleting the known P-045 component or another genuine lower-rank component.

## Reproducibility and epistemic status

Durable verifier: research/computations/verify_e2_quartic_incidence.py.

- 18-dimensional quartic basis: **EXACT COMPUTATION**.
- Generic/sample ranks: **EXACT COMPUTATION** at the stated fibers.
- Pivot determinant d^7(b+2)Delta/128: **EXACT COMPUTATION**.
- P-045 ranks and symbolic H_x x_i containment: **COMPUTATIONAL CROSS-CHECK** of P-045.
- Global quartic-incidence classification: **OPEN**.
- Elimination of the full e=2 branch: **OPEN**.




## 7. Sharpening on the dx=1 test bed

**EXACT COMPUTATION.** Restricting the same rank-12 pivot minor to (d=x^{-1})
gives
[
det P=rac{(bx-a)^2(b+2)}{128x^8}.
]
On this slice
[
Delta=rac{(bx-a)^2}{x}.
]
Therefore, on the basepoint-free locus, (x
e0) and (bx-a
e0), and this
single six-dimensional kernel chart covers every point with (b
e-2).

Consequently the combined P-044/quartic-incidence problem on (dx=1) has a
particularly clean stratification:

1. (b
e-2): use the single rank-12 chart and its reduced (6)-column
   second-order obstruction;
2. (b=-2): analyze the lower-rank/boundary behavior separately.  The known
   P-045 family lies on this divisor.

This does **not** prove that every point of (b=-2) has first-order rank 11,
nor that P-045 exhausts the P-044 locus there.  Those statements remain
**OPEN** until separately computed.

A direct attempt to symbolically factor a full (6	imes6) reduced minor was
stopped because expression growth became severe even after the (dx=1)
restriction.  No determinant or factorization from that interrupted
calculation is being reported.  The next implementation should use
fraction-free polynomial linear algebra or modular evaluation/reconstruction,
rather than expanding rational SymPy determinants.


---

## 2026-10-05-p044-survivor-cubic

# P-044 survivor family: cubic carrier obstruction

Date: 2026-10-05

## Status

**PROVED / INDEPENDENTLY AUDITED (characteristic zero).**

This note concerns only the explicit basepoint-free P-044 survivor family. It
does **not** classify the full P-044 zero locus and does **not** exclude the
entire \(e=2\) branch.

Let
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3
\]
and write
\[
q=x_0x_3-x_1x_2,\quad
A_3=x_0^2x_2-x_1^3,\quad
B_3=x_0x_2^2-x_1^2x_3,\quad
D_3=x_2^3-x_1x_3^2.
\]
For
\[
A=z^2-\tfrac12z+x,\qquad
B=1-2z+x^{-1}z^2,\qquad x\ne0,\tfrac14,
\]
let \(C_3(x)\) be the canonical primitive triple obtained from the moving
coordinate P-044 construction.

Define
\[
\boxed{
H_x=D_3+4x^2B_3+4x^4A_3+
(-4x^3x_0+8x^3x_1-2xx_2+4xx_3)q.}
\]

## Theorem

For every allowed specialization \(x\ne0,\tfrac14\):

1. \(H_x\in H^0(I_{C_3(x)}(3))\).
2. \(H_x\) is irreducible.
3.
   \[
   H^0(I_{C_3(x)}(4))=H_xH^0(O_{\mathbf P^3}(1)),
   \qquad h^0(I_{C_3(x)}(4))=4.
   \]
4. Consequently this P-044 survivor family cannot be induced by the quartic
   member of a characteristic-zero \((4,7)\) STCI presentation of \(C_0\).

No exhaustion of the full P-044 zero locus is used.

## 1. Exact primitive-triple containment

On \(x_0=1\), the formal coordinates used by P-044 are
\[
x_2=z^3+v,\qquad x_3=z^4+u+\tfrac32zv.
\]
The opposite parameter is
\[
w=\frac{z^3+v}{z^4+u+\tfrac32zv},
\]
so \(w=1/z\) only modulo the normal ideal.

A Bezout identity \(sA+tB=1\) is
\[
s=\frac{2(2x-z)}{x(4x-1)},\qquad
t=\frac{2z-1}{4x-1}.
\]
The audited moving-coordinate calculation gives the canonical triple
\[
u=A\epsilon-t\gamma_U\epsilon^2,\qquad
v=B\epsilon+s\gamma_U\epsilon^2
\pmod{\epsilon^3},
\]
where
\[
\gamma_U=
-\frac{
8x^3+16x^2z^2-18x^2z+4x^2
-12xz^3+8xz^2+3z^4
}{8x^3}.
\]
Thus
\[
\begin{aligned}
x_0&=1,\quad x_1=z,\\
x_2&=z^3+B\epsilon+s\gamma_U\epsilon^2,\\
x_3&=z^4+(A+\tfrac32zB)\epsilon+
(-t+\tfrac32zs)\gamma_U\epsilon^2.
\end{aligned}
\]
Exact substitution gives
\[
[\epsilon^0]H_x=[\epsilon^1]H_x=[\epsilon^2]H_x=0.
\]
The identity is in the localization
\[
\mathbf Q[x,x^{-1},(4x-1)^{-1},z]
\]
(with powers of \(2\) inverted), exactly matching the allowed parameter range.

As an independent linear-algebra check, every cubic through \(C_0\) is
\[
\alpha A_3+\beta B_3+\gamma D_3+
q(\lambda_0x_0+\lambda_1x_1+\lambda_2x_2+\lambda_3x_3).
\]
Imposing vanishing through order \(\epsilon^2\) gives a one-dimensional kernel
generated by
\[
(\alpha,\beta,\gamma,\lambda_0,\lambda_1,\lambda_2,\lambda_3)
=(4x^4,4x^2,1,-4x^3,8x^3,-2x,4x),
\]
which is exactly \(H_x\).

The next coefficient is generically nonzero, so the cubic generically contains
the canonical triple but not the canonical quadruple. This extra fact is not
used in the theorem.

## 2. Irreducibility

The curve \(C_0\) is nonplanar, and direct coefficient comparison after the
parametrization shows
\[
h^0(I_{C_0}(2))=1,
\]
generated by \(q\).

If \(H_x\) were reducible, primality of \(I(C_0)\) would force a proper factor
of degree \(1\) or \(2\) to contain \(C_0\). A linear factor is impossible by
nonplanarity; a quadratic factor must therefore be proportional to \(q\).

But modulo \(q\),
\[
H_x\equiv D_3+4x^2B_3+4x^4A_3.
\]
On the line of \(V(q)\)
\[
[x_0:x_1:x_2:x_3]=[1:0:T:0],
\]
this becomes
\[
T^3+4x^2T^2+4x^4T=T(T+2x^2)^2,
\]
whose leading coefficient is \(1\). Hence it is never identically zero and
\(q\nmid H_x\). Thus \(H_x\) is irreducible for every allowed specialization.
The argument is fiberwise and leaves no exceptional allowed \(x\).

## 3. Hilbert polynomial of the primitive triple

For this \(e=2\) primitive triple,
\[
\operatorname{gr}O_{C_3}=O_C\oplus L\oplus L^2,
\qquad L=O_{\mathbf P^1}(-5),
\]
and \(O_C(1)=O_{\mathbf P^1}(4)\). Hence
\[
\chi(O_C(n))=4n+1,\quad
\chi(L(n))=4n-4,\quad
\chi(L^2(n))=4n-9.
\]
Therefore
\[
P_{C_3}(n)=12n-12,
\]
so
\[
\deg C_3=12,\qquad \chi(O_{C_3})=-12,\qquad p_a(C_3)=13.
\]
The primitive local model is curvilinear, hence \(C_3\) is locally
Cohen--Macaulay and pure of dimension one.

## 4. Divisibility of every containing quartic

Let \(F\in H^0(I_{C_3}(4))\). Suppose \(H_x\nmid F\). Since \(H_x\) is
irreducible, \(H_x,F\) form a proper complete intersection
\[
Y=V(H_x,F)
\]
of type \((3,4)\). Thus
\[
\deg Y=12,\qquad p_a(Y)=19,\qquad \chi(O_Y)=-18.
\]
Scheme containment \(C_3\subseteq Y\) gives
\[
0\to K\to O_Y\to O_{C_3}\to0.
\]
The two schemes have the same degree, so Hilbert-polynomial additivity makes
\(K\) zero-dimensional. Therefore
\[
-18=-12+\operatorname{length}K,
\]
which is impossible. Hence \(H_x\mid F\).

Conversely every \(H_x\ell\), with \(\ell\) linear, vanishes on \(C_3\).
Therefore
\[
H^0(I_{C_3}(4))=H_xH^0(O(1)),
\]
and multiplication by nonzero \(H_x\) is injective, giving dimension \(4\).

## 5. Exclusion from a (4,7) STCI pair

If a hypothetical quartic member inducing this triple were \(F_4\), then
\[
F_4=H_x\ell
\]
for a nonzero linear form \(\ell\). Put \(P=V(\ell)\). Set-theoretically
\[
V(F_4,G_7)=V(H_x,G_7)\cup V(\ell,G_7).
\]
If \(\ell\mid G_7\), the common zero set contains the plane \(P\). Otherwise
\(G_7|_P\) is a nonzero positive-degree homogeneous polynomial and its zero
locus is a nonempty plane curve. Since \(C_0\) is nonplanar,
\(C_0\cap P\) is zero-dimensional, so this plane curve cannot be contained in
\(C_0\). In either case
\[
\sqrt{(F_4,G_7)}\ne I(C_0).
\]

Thus the explicit P-044 survivor family is excluded as the quartic carrier of
a \((4,7)\) STCI presentation.

## Scope / frontier

This theorem kills the **known explicit** basepoint-free P-044 survivor family.
It does not show that this is the full P-044 zero locus. The immediate
remaining \(e=2\) question is therefore classification (or geometric exclusion)
of all other basepoint-free P-044 zeros, not extension of this explicit family
farther up the primitive tower.


---

## 2026-10-06-dx1-p044-classification

> **SUPERSEDED STATUS NOTICE (2026-10-06 cleanup):** The residual saturation calculation requested below was subsequently completed exactly. The Macaulay2 unit-ideal/saturation certificate in `research/computations/session_dx1_saturation_2026_10_06.m2` and its recorded output closes the residual open set. Together with the audited boundary calculation, the basepoint-free P-044 locus on the dx=1 slice is exactly P-045. This note is retained as provenance for the pre-certificate argument and its identified gap; do not use its OPEN conclusion as current status. See `research/AUDITED_STATE_2026-10-06.md`, Section G.

# dx=1 P-044 classification

Date: 2026-10-06

Status: **OPEN pending one residual saturation calculation.** Independent audit found a genuine gap in the previous residual-open argument: coprimality of two multivariate resultant factors does not imply that their common affine zero set is empty.

On the slice
[
d=x^{-1},qquad u=bx-a,
]
the resultant is
[
Delta=u^2/x.
]
Thus the basepoint-free locus is (D(xu)).

The exact P-044 coordinates specialize as (G_i=uQ_i). Two coordinates have
[
Q_2=(2a+1)R_2,qquad Q_4=2(b+2)R_4.
]

## Audited boundary pieces

On (b=-2), the exact residual calculation shows that every extra common zero has (u=0), hence (Delta=0). Therefore on (D(Delta)),
[
b=-2, P	ext{-044}Longrightarrow a=-1/2.
]

On (a=-1/2), the dedicated exact verifier shows
[
P	ext{-044}Longrightarrow b=-2quad	ext{or}quad u=0.
]
The second alternative lies on (Delta=0). Hence the basepoint-free part of this boundary is exactly P-045.

## Residual open set: still open

On
[
D!left(xu(2a+1)(b+2)ight),
]
P-044 implies
[
R_2=R_4=Q_5=0.
]
After (b=(a+u)/x), exact elimination gives
[
operatorname{Res}_u(R_2,R_4)=-36x(2a+1)P_{24}(a,x),
]
[
operatorname{Res}_u(R_2,Q_5)=-36x^2(2a+1)^2P_{25}(a,x),
]
and
[
gcd(P_{24},P_{25})=1quad	ext{in }mathbf Q[a,x].
]

These identities are exact, but the former conclusion that they prove emptiness was invalid: two coprime multivariate polynomials can have isolated common zeros. The independent audit found such resultant intersections, including ((a,x)=(-1,1/4)) and ((-3/2,1/4)); those sampled points lift only to (u=0) and hence are not counterexamples, but they demonstrate the logical gap.

The required repair is an exact certificate that
[
V(R_2,R_4,Q_5)cap D!left(xu(2a+1)(a+u+2x)ight)=arnothing,
]
equivalently that the corresponding saturated ideal is the unit ideal. Direct SymPy Gröbner/Rabinowitsch attempts timed out on 2026-10-06, so no replacement certificate is claimed here.

Therefore the complete classification
[
d=x^{-1},quadDelta
e0,quad P	ext{-044}
iff
a=-rac12,quad b=-2
]
is **not yet proved**.

Consequently the no-carrier statement on the whole (dx=1) slice is also **OPEN pending this residual calculation**. Its final implication remains valid: if the classification is repaired, P-045's cubic-factor theorem excludes a quartic carrier.

Verifier/diagnostic:
`research/computations/verify_dx1_p044_residual.py`.

Boundary verifier:
`research/computations/verify_dx1_a_half_boundary.py`.



## Consolidated historical supplement: `research/supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md`

The following historical mathematical content is preserved verbatim with its original hypotheses, limitations, and proof status. Relative links refer to the original supplement location.

# Intrinsic local algebra and characteristic-zero quartic geometry

## Integration guide: first symbols, complete filtrations, and (4,4) exclusion

The [ideal-filtration investigation](#2026-10-23-ideal-filtrations-independent-investigationmd) records the full marked embedding and an explicit failure of the proposed general first-order-to-higher-generator correspondence. The [filtered (4,4) proposal](#2026-10-23-quartic-44-filtered-proof-proposalmd) and [independent audit](#2026-10-23-quartic-44-filtered-proof-independent-auditmd) instead use additional specific numerical, classification, and global quartic-contact input. These are not contradictory: a special filtered exclusion may hold without the false general correspondence.

The alternative [surface-singularity route](../synthesis/quartic_pair_obstruction.md#4-direct-blowups-and-the-global-contradiction) replaces the global contact determinant with a characteristic-zero exceptional-rank contradiction, while retaining the local defect algebra. [The genus-budget synthesis](INTRINSIC_44_MULTIPLICITY_AND_GENUS_BUDGETS.md#cross-supplement-synthesis-distinct-44-obstruction-routes-editorial-not-a-new-audit) contrasts both approaches with lower-multiplicity residual examples. [Delta embedding](DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#delta-embedding-geometry-report) and [normal flatness](NORMAL_FLATNESS_AND_FILTERED_CI.md#2026-10-19-filtered-generic-ci-normal-flatness) give broader filtration frameworks, each with independent scope restrictions.

Keep the original computational checks, correction freedoms, counterexample, and audit status below. This guide does not extend any (4,4) conclusion to arbitrary degrees.

---


Full mathematical investigations retained by subject. Proposals, independent reviews, limitations and rejected mathematical approaches retain their original epistemic status. This compilation is not a new proof audit.


---

## 2026-10-23-ideal-filtrations-independent-investigation.md

# Independent investigation: ideal filtrations and the nine-embedding diagram

Date: 2026-10-23. Status: **research proposal and independent assessment**.

Scope: distinct integral hypersurfaces \(X,Y\subset P=\mathbf P^3_k\), their scheme intersection \(Z\), and a specified reduced closed subscheme \(C\subset Z\). Distinguish \(C=Z_{\mathrm{red}}\) from a marked component \(C\subsetneq Z_{\mathrm{red}}\). Statements identifying \(\operatorname{Sym}(I/I^2)\) with \(\operatorname{gr}_I\mathcal O_P\) additionally assume \(C\hookrightarrow P\) regular. The explicit marked rational quartic is smooth. Local counterexamples are local examples, not global constructions for that fixed projective quartic.

The original request specified no repository edits. The subsequent instruction, “pls save your work in a branch,” authorizes this report and its evidence on a separate branch. No accepted proof, result, or question is changed.

## 1. Verdict and scope corrections

The framework is useful as a coordinated study of **the actual filtered intersection and its normal degeneration**. Most constructions are standard conormal, normal-cone, standard-basis, Rees, Koszul, and cotangent-complex mathematics. This investigation does not establish novelty.

The strongest completeness formulation is tautological: retaining the actual nine-embedding scheme diagram already retains \(Z\hookrightarrow P\). Even retaining all nine graded algebras with their original bases and ambient quotient maps retains \(\mathcal O_Z\) in degree zero. The substantive question is whether reduced normal data determine the filtered intersection. They do not, even for local intersections of integral hypersurfaces with smooth reduced support.

The lifting filtration is sound after an intrinsic reformulation. Its comparison with minimal initial equations is a canonical surjection, with an explicit defect:
\[
0\longrightarrow\Delta_n\longrightarrow Q_n
\longrightarrow\operatorname{gr}^n_F(J/IJ)\longrightarrow0,
\qquad
\Delta_n=\frac{\operatorname{in}_n(IJ)}{(S_+H)_n}.
\tag{1}
\]
A two-generator complete intersection can have a nonzero \(Q_4\) invisible in this filtered equation module. Section 5 proves this.

For the prescribed characteristic-two quartic pair, the special equality \(\operatorname{in}_I(IJ)=S_+H\) does hold. There is a canonical isomorphism
\[
\ker\phi\simeq Q_4\simeq\mathcal O_{\mathbf P^1}(-24).
\]
The transition calculation verifies compatibility, rather than merely matching degrees.

More generally, section 4.3 proves that the comparison defect is supported only where both carriers are singular along the smooth curve. This explains the favorable behavior of the prescribed pair without treating it as a universal first-order principle.

Three scope corrections are essential:

1. Require \(X\ne Y\). Integral hypersurfaces can coincide. Distinctness makes \(F,G\) a regular sequence; \(Z\) is then a pure one-dimensional Cohen–Macaulay complete intersection. It has no embedded associated components, although it may be nonreduced. Embedded or vertical features in a normal cone are different assertions.
2. The characteristic-zero example uses a marked component. Its smooth quartic \(C\) is one of four geometric components of \(Z_{\mathrm{red}}\). Using the whole reduced union changes \(I\), its conormal sheaf, and its graded algebra.
3. Regularity of \(C\hookrightarrow P\) is additional. A general reduction can be singular or reducible. There is always a surjection \(\operatorname{Sym}(I/I^2)\twoheadrightarrow\operatorname{gr}_I\mathcal O_P\), but it need not be an isomorphism.

The unrestricted characteristic-zero STCI question is outside this investigation. No new proof of it is attempted or implied.

## 2. The complete embedding and conormal diagram

### 2.1 All nine ideals and their bases

Use sheaves throughout; affine expressions denote local realizations. Set
\[
R=\mathcal O_P,\quad A=I_X,\quad B=I_Y,\quad
J=A+B,\quad I=I_C,\quad A,B\subset J\subset I.
\]

The diagram has five immediate arrows and four composites:

~~~mermaid
flowchart TD
    C["C"] --> Z["Z"]
    Z --> X["X"]
    Z --> Y["Y"]
    X --> P["P"]
    Y --> P
    C --> X
    C --> Y
    C --> P
    Z --> P
~~~

The square \(Z\to X,Y\to P\) is Cartesian. Every triangle using a composite arrow commutes. Both length-four routes from \(C\) to \(P\) agree with the direct arrow.

| Embedding | Ideal in its actual ambient ring | Conormal sheaf | Base |
|---|---|---|---|
| \(X\hookrightarrow P\) | \(A\subset R\) | \(A/A^2\) | \(X\) |
| \(Y\hookrightarrow P\) | \(B\subset R\) | \(B/B^2\) | \(Y\) |
| \(Z\hookrightarrow P\) | \(J\subset R\) | \(J/J^2\) | \(Z\) |
| \(C\hookrightarrow P\) | \(I\subset R\) | \(I/I^2\) | \(C\) |
| \(Z\hookrightarrow X\) | \(J/A\subset R/A\) | \(J/(J^2+A)\) | \(Z\) |
| \(Z\hookrightarrow Y\) | \(J/B\subset R/B\) | \(J/(J^2+B)\) | \(Z\) |
| \(C\hookrightarrow X\) | \(I/A\subset R/A\) | \(I/(I^2+A)\) | \(C\) |
| \(C\hookrightarrow Y\) | \(I/B\subset R/B\) | \(I/(I^2+B)\) | \(C\) |
| \(C\hookrightarrow Z\) | \(K=I/J\subset R/J\) | \(I/(I^2+J)\) | \(C\) |

Each row carries its own full ideal-power filtration. For example, degree \(n\) for \(Z\hookrightarrow X\) is \((J^n+A)/(J^{n+1}+A)\), on \(Z\). For \(C\hookrightarrow Z\) it is \((I^n+J)/(I^{n+1}+J)\), on \(C\). These are different filtrations.

### 2.2 Every composable triple and its precise exactness

For ideals \(L\subset M\subset Q\), the chain
\(\operatorname{Spec}(Q/M)\hookrightarrow\operatorname{Spec}(Q/L)\hookrightarrow\operatorname{Spec}Q\)
gives
\[
0\to\frac{L\cap M^2}{LM}
\to\frac{L}{LM}\to\frac{M}{M^2}
\to\frac{M}{M^2+L}\to0.
\tag{2}
\]
This follows by taking the kernel and cokernel of the inclusion-induced map \(L/LM\to M/M^2\). The middle three terms form the usual right-exact conormal sequence. See [Stacks, conormal transitivity](https://stacks.math.columbia.edu/tag/01R1) and [exactness qualifications](https://stacks.math.columbia.edu/tag/06BB).

There are exactly seven strict triples:

| Chain \((U,V,W)\) | Ambient ring \(Q\) | \(L=I_{V/W}\) | \(M=I_{U/W}\) |
|---|---|---|---|
| \((Z,X,P)\) | \(R\) | \(A\) | \(J\) |
| \((Z,Y,P)\) | \(R\) | \(B\) | \(J\) |
| \((C,X,P)\) | \(R\) | \(A\) | \(I\) |
| \((C,Y,P)\) | \(R\) | \(B\) | \(I\) |
| \((C,Z,P)\) | \(R\) | \(J\) | \(I\) |
| \((C,Z,X)\) | \(R/A\) | \(J/A\) | \(I/A\) |
| \((C,Z,Y)\) | \(R/B\) | \(J/B\) | \(I/B\) |

Substituting in (2) determines every first-arrow kernel, image, and cokernel. The two length-four chains give their naturality compatibilities.

For the first two rows regularity of \(F,G\) gives, on \(Z\),
\[
J/J^2\simeq(A/A^2)|_Z\oplus(B/B^2)|_Z.
\tag{3}
\]
For example \(A\cap J^2=AJ\), so the first map for \(Z\to X\to P\) is injective. Analogous maps involving \(C\) need not be injective.

### 2.3 The central first-order diagram

On \(C\), put
\[
M_A=A/IA,\quad M_B=B/IB,\quad
D=J/IJ=(J/J^2)|_C,\quad E=I/I^2.
\]
Then \(D=M_A\oplus M_B\). If \(d=\deg F,e=\deg G\), these source lines are \(\mathcal O_P(-d)|_C,\mathcal O_P(-e)|_C\). Let
\(\alpha:M_A\to E,\ \beta:M_B\to E\). The central map is \(\phi=(\alpha,\beta)\), with exact defects
\[
\ker\phi=\frac{J\cap I^2}{IJ},\qquad
\operatorname{coker}\phi=\frac{I}{I^2+J}=N^*_{C/Z}.
\tag{4}
\]

Write \(E_X=I/(I^2+A)\), \(E_Y=I/(I^2+B)\), \(E_Z=I/(I^2+J)\). Naturality gives
\[
\begin{array}{ccccc}
M_A&\longrightarrow&D&\longrightarrow&M_B\longrightarrow0\\
\Vert&&\downarrow\phi&&\downarrow\bar\beta\\
M_A&\xrightarrow{\alpha}&E&\longrightarrow&E_X\longrightarrow0,
\end{array}
\tag{5}
\]
and the symmetric diagram. The top row is split exact; the bottom is right exact. The sequence \(M_B\to E_X\to E_Z\to0\) is the chain \(C\to Z\to X\); its first kernel is
\[
\frac{A+(J\cap I^2)}{A+IJ}.
\]
The other route is symmetric.

For an exact diagram use the images \(U=\operatorname{im}\alpha\), \(V=\operatorname{im}\beta\). The quotient square
\[
\begin{array}{ccc}
E&\longrightarrow&E/U=E_X\\
\downarrow&&\downarrow\\
E/V=E_Y&\longrightarrow&E/(U+V)=E_Z
\end{array}
\]
is a pushout of modules. Its failure to be a pullback is measured by \(U\cap V\):
\[
0\to U\cap V\to E\to E_X\oplus E_Y\to E_Z\to0,
\tag{6}
\]
where the last arrow is the difference of quotient maps. There is a genuine exact \(3\times3\) diagram whose rows are
\[
(U\cap V,\ U,\ (U+V)/V),\quad
(V,\ E,\ E/V),\quad
(V/(U\cap V),\ E/U,\ E/(U+V)).
\]
Each row and column is short exact. Replacing \(U,V\) by their source lines without retaining \(\ker\alpha,\ker\beta\) invalidates this.

### 2.4 Higher maps and exactness

There is no reason all natural arrows form one complex. The following formulas cover the relevant families.

For \(L\subset M\), the degree-\(n\) map \(\operatorname{gr}_LQ\to\operatorname{gr}_MQ\) has kernel
\((L^n\cap M^{n+1})/L^{n+1}\) and image
\((L^n+M^{n+1})/M^{n+1}\). After restricting the source to \(Q/M\), its source is \(L^n/ML^n\) and kernel
\[
\frac{L^n\cap M^{n+1}}{ML^n}.
\tag{7}
\]
For passage to an ambient quotient \(Q/L\), the induced \(M\)-filtration gives the quotient by the full initial ideal of \(L\), not just by initials of chosen generators.

Multiplication \(M^r/M^{r+1}\otimes M^s/M^{s+1}\to M^{r+s}/M^{r+s+1}\) is canonical; its kernels are relations and no injectivity is automatic. Restriction is tensor product and is right exact. For a short exact sequence its possible new left kernel is the image of a \(\operatorname{Tor}_1\) connecting map. Section 7 exhibits this explicitly.

## 3. The central normal-cone sequence

Set \(S=\operatorname{gr}_IR\) and
\[
H_n=\frac{J\cap I^n}{J\cap I^{n+1}}\hookrightarrow S_n.
\]
Multiplication makes \(H=\bigoplus H_n\) a homogeneous ideal. Since \(K^n=(I^n+J)/J\), taking the kernel of \(I^n/I^{n+1}\to(I^n+J)/(I^{n+1}+J)\) proves
\[
0\to H_n\to S_n\to K^n/K^{n+1}\to0,\qquad
0\to H\to S\to\operatorname{gr}_K(R/J)\to0.
\tag{8}
\]
No regularity assumption on \(I\) is needed.

This is an excellent organizing sequence and also the classical form-ideal sequence. Valabrega–Valla, *Form rings and regular sequences*, §1, pp. 94–95, already gives this kernel description and an intersection criterion for initials of chosen generators to generate the full form ideal ([original paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F91724E40BE6AE7101C7A959AFC3DA05/S0027763000018225a.pdf/form-rings-and-regular-sequences-1.pdf)). The framework should use that established theory.

If \(C\to P\) is regular, \(S=\operatorname{Sym}E\); geometrically (8) embeds \(C_{C/Z}\) in \(N_{C/P}\). See [Stacks, normal cones](https://stacks.math.columbia.edu/tag/062Z).

For \(n\ge1\),
\[
Q_n=H_n/(S_+H)_n,\qquad
(S_+H)_n=\sum_{i=1}^{n-1}S_iH_{n-i}
\tag{9}
\]
is the module of minimal initial equations. It need not be locally free. Over a nonfield base its rank alone does not determine its local generators. It does not retain the syzygies among the equations.

For regular \(J\), the map in the question is
\[
\operatorname{Sym}^nD=J^n/IJ^n\longrightarrow S_n.
\]
Its image is \((\operatorname{im}\phi)^n=(H_1)^n\): products of \(n\) first-order symbols. This is neither all of \(H_n\) nor necessarily \(S_{n-1}H_1\). Its kernel is (7) for \(L=J,M=I\). In characteristic two these maps see powers of \(V\) and miss the new equation \(U^4\).

## 4. Lifting filtration: intrinsic form and exact comparison

### 4.1 The intrinsic filtered equation module

The [intrinsic filtration and the presentation-syzygy proof](../arguments/filtered_equation_comparison.md#full-normal-equations-and-the-actual-equation-module)
use the actual ideal module \(J/IJ\).

### 4.2 The denominator, and the direction of the canonical map

The [denominator and canonical surjection](../arguments/filtered_equation_comparison.md#full-normal-equations-and-the-actual-equation-module)
give the exact comparison (1). [R-0030](../results/local_filtration_comparison_defect.md)
states the local claim and separates its generic count and punctual length formula.

### 4.3 A proved sufficient condition: one smooth carrier

The [smooth-carrier proof](../arguments/filtered_equation_comparison.md#smooth-carrier-vanishing)
straightens one carrier and computes both full initial ideals over the
completed local coefficient domain.

## 5. Counterexample to the general first-order/higher-generator correspondence

The [length-five quotient and filtered Koszul calculation](../arguments/filtered_equation_comparison.md#a-minimal-initial-equation-erased-by-the-comparison)
give the degree-four initial equation erased by passage to \(J/IJ\).
See the exact [counterexample statement](../results/initial_equation_cancellation_counterexample.md).

## 6. Completeness: exactly which data suffice?

### 6.1 Actual ideals and the literal full graded diagram

Actual inclusions \(A,B\subset R\) determine \(J=A+B\) and the embedded \(Z\). A filtered \(\mathcal O_P\)-algebra with its actual underlying algebra, quotient map, and multiplication also retains that algebra.

For “only graded data,” observe
\[
(\operatorname{gr}_JR)_0=R/J.
\tag{16}
\]
If the full nine-graded diagram includes the original bases and \(R\to(\operatorname{gr}_JR)_0\), its kernel is \(J\). If only an abstract graded algebra is retained, degree zero still gives abstract \(Z\), but the embedding needs the ambient map. If the actual scheme diagram is retained, completeness precedes all filtration constructions.

Thus different embedded intersections cannot have isomorphic full nine-graded diagrams over the identity of fixed \(P\), with all degree-zero quotient maps retained. A same-initial-ideal example cannot disprove this stronger assertion.

### 6.2 Different intersections with identical graded diagrams after restriction to \(C\)

The [restricted normal diagram counterexample](../results/restricted_normal_diagram_counterexample.md)
gives both integral hypersurface presentations, the nine graded algebras
and their maps after restriction to \(C\), and the intrinsic square-zero
distinction between the actual intersection rings.

### 6.3 Compatible actual neighborhoods and completions

If \(C=Z_{\mathrm{red}}\), noetherian quasi-compactness gives \(K^N=0\), equivalently \(I^N\subset J\), for some uniform \(N\); see [Stacks, nilpotent ideals](https://stacks.math.columbia.edu/tag/00IM). Thus the actual embedded tower
\[
Z_n=V(J+I^{n+1})\subset P
\tag{19}
\]
stabilizes at \(Z\) for \(n+1\ge N\). The compatible tower with its algebra structures determines \(Z\); its maps to \(P\) determine the embedding. Graded layers do not.

No universal finite truncation exists without a nilpotence bound. Smooth integral hypersurfaces \(X=V(v)\), \(Y_m=V(v+u^m)\) have \(J_m=(v,u^m)\). For fixed \(N<m,m'\), their towers through order \(N\) agree although generic transverse lengths are \(m,m'\).

A formal closed thickening whose ideal contains \(\widehat I^N\) already defines a coherent ideal in the algebraic finite neighborhood \(V(I^N)\), hence a closed subscheme of \(P\). A blanket algebraization warning is therefore wrong for this finite supported case. This reconstruction does not supply global integral hypersurface generators of specified degrees.

If \(C\) is only a marked proper component, completion of \(J\) alone can miss components away from \(C\). For example \((v,u)\) and \((v,u(u-1))\) have equal completions along \((u,v)\); the latter has an extra disjoint line. Each is an intersection of integral smooth affine hypersurfaces, using \((v,u)\) and \((v,v+u(u-1))\).

This does not make the full completed hypersurface-pair diagrams identical. In the stated integral setting, the completed ideals of each hypersurface inside the same fixed completed ambient \(P\) determine the global hypersurfaces uniquely. Faithful completion gives equality of stalks at \(p\in C\); local prime ideals contract to equal primes in an affine neighborhood. The hypersurfaces share an open piece and their scheme-theoretic closures in \(P\) coincide. Apply separately to \(A,B\). The required facts are [faithful flatness of completion](https://stacks.math.columbia.edu/tag/00MC) and [exactness on finite modules](https://stacks.math.columbia.edu/tag/00MB).

This is uniqueness for algebraic pairs with fixed ambient marking. It does not say arbitrary formal hypersurfaces algebraize, or formal ambient automorphisms extend globally.

### 6.4 The missing information and its repair

Passing to the normal graded object loses the compatible algebra extensions assembling the layers: higher equation terms and nonlinear transition functions. The central normal cone along \(C\) alone does not reconstruct the filtered intersection.

The smallest practical repair is to retain actual compatible neighborhood algebras and their embedded gluing. A uniform package is the extended Rees construction
\[
\widetilde{\mathcal R}_I(R)=\sum_{n\in\mathbf Z}I^nt^{-n}
\subset R[t,t^{-1}],\qquad I^n=R\ (n\le0),
\]
with induced ideal \(\widetilde J=\sum(J\cap I^n)t^{-n}\). There is an exact Rees sequence
\[
0\to\widetilde J\to\widetilde{\mathcal R}_I(R)
\to\widetilde{\mathcal R}_K(R/J)\to0.
\tag{20}
\]
Its fiber at \(t=0\) is (8); its fiber at \(t=1\) is \(0\to J\to R\to R/J\to0\). This is the algebra of deformation to the normal cone; see [Vakil, Intersection Theory class 14, §3](https://math.stanford.edu/~vakil/245/245class14.pdf).

Completeness of this package is built in because a nonzero fiber includes the original algebra. Its value is compatible bookkeeping. Retain the labelled subideals \(A,B\) if the carriers matter. Their induced \(I\)-filtrations differ from their own ideal-adic filtrations. Naively homogenizing only displayed generators may require saturation by the deformation parameter to recover cancellation-generated equations.

## 7. Explicit rational quartic audit

Every \(\mathcal O(n)\) here means \(\mathcal O_{\mathbf P^1}(n)\); ambient \(\mathcal O_P(d)|_C=\mathcal O(4d)\). The curve is \([s:t]\mapsto[s^4:s^3t:st^3:t^4]\) and the equations are \(F=x_1^4-x_0^3x_3\), \(G=x_2^4-x_0x_3^3\).

[R0020](../results/quartic_conormal_characteristic_jump.md) and [R0021](../results/quartic_mu4_degeneration.md) cover the splitting and explicit degeneration. The [prescribed family argument](../arguments/quartic_specialization_and_symbols.md#the-prescribed-mu4-intersection-and-actual-quartic-symbols) retains the scope of the geometry/symbol audit consulted here. The chart calculations below independently reconstruct the requested formulas and lifting compatibility; unrelated accepted exclusions are not rerun.

### 7.1 Exact equations and overlap

On \(x_0\ne0\), use \((a,u,v)\) from the request:
\[
F_0=-v,\qquad
G_0=u^4+4a^3u^3+6a^6u^2+4a^9u-3a^8v-3a^4v^2-v^3.
\]
Thus \(J=(v,h)\), \(h=(a^3+u)^4-a^{12}\).

On \(x_3\ne0\), put \(b=x_2/x_3\), \(A=x_0/x_3-b^4\), \(B=x_1/x_3-b^3\). Then \(G_\infty=-A\) and
\[
F_\infty=B^4+4b^3B^3+6b^6B^2+4b^9B-3b^8A-3b^4A^2-A^3.
\]
These charts cover \(Z\): \(x_0=x_3=0\) forces \(x_1=x_2=0\).

Writing \(V,U\) for the conormal classes of \(v,u\), the first-order overlap is
\[
\begin{pmatrix}A\\B\end{pmatrix}
=\begin{pmatrix}3a^{-8}&-4a^{-7}\\2a^{-7}&-3a^{-6}\end{pmatrix}
\begin{pmatrix}V\\U\end{pmatrix}.
\tag{21}
\]
The determinant is \(-a^{-14}\). In characteristic zero choose
\[
w_0=V-\tfrac32aU,\ z_0=U,\quad
w_\infty=B/2,\ z_\infty=2A-3bB.
\]
Then \((w_\infty,z_\infty)=a^{-7}(w_0,z_0)\). In characteristic two (21) is diagonal, \((A,B)=(a^{-8}V,a^{-6}U)\). This recovers \(E=\mathcal O(-7)^2\) in characteristic zero and \(E=\mathcal O(-8)\oplus\mathcal O(-6)\) in characteristic two.

### 7.2 Characteristic zero

The conormal matrices in frames \((V,U)\), respectively \((A,B)\), are
\[
\phi_0=\begin{pmatrix}-1&-3a^8\\0&4a^9\end{pmatrix},
\qquad
\phi_\infty=\begin{pmatrix}-3b^8&-1\\4b^9&0\end{pmatrix}.
\tag{22}
\]
Thus \(\ker\phi=0\), and near the first endpoint
\(\operatorname{coker}\phi=(k[a]/a^9)U\), with length nine also at infinity. Its total length is eighteen, determinant divisor \(9p_0+9p_\infty\).

The full initial ideal and relative algebra are
\[
H|_{U_0}=(V,a^9U),\qquad
\operatorname{gr}_K\mathcal O_Z|_{U_0}=k[a,U]/(a^9U).
\tag{23}
\]
For fullness, eliminate \(v\). In the domain \(k[a]\), the lowest \(u\)-term of any nonzero multiple of \(h\) is the product of the lowest terms. Lifting back adds \(V\). The ideal is generated in degree one, so \(Q_n=0\) for \(n\ge2\).

At generic \(C\), \(a\) is invertible and there is no positive graded part: the generic transverse length is one. Every global positive graded piece is torsion of length nine at each endpoint. The vertical normal-cone directions are not extra curve components downstairs.

Over a splitting field, the actual intersection is the reduced union
\[
C_\zeta=[s^4:s^3t:\zeta st^3:t^4],\qquad\zeta^4=1.
\]
Complete-intersection purity and generic reducedness on these four degree-four components rule out further nilpotent or embedded structure. Each branch has \(v=0,u=(\zeta-1)a^3\); at infinity \(A=0,B=(\zeta-1)b^3\). Each pair meets with length three at each endpoint. The marked curve meets the other three jointly in \(9p_0+9p_\infty\). Four smooth plane branches give \(\delta=6\cdot3=18\) at each endpoint, hence arithmetic genus \(36-4+1=33\). Without fourth roots in \(k\), geometric components are grouped by Galois action.

Although the kernel sheaf in (22) is zero, its endpoint fiber map has a one-dimensional kernel. Tensor product introduces a kernel through the torsion cokernel. Similarly, taking the ambient slice \(a=0\) gives
\[
\operatorname{gr}_K(\mathcal O_Z|_{U_0})\otimes_{k[a]}k=k[U],
\quad
\operatorname{gr}_{(u,v)}(\mathcal O_Z|_{U_0}\otimes_{k[a]}k)=k[U]/(U^4),
\]
where \(k[a]\to k\) sends \(a\) to zero. Normal associated graded formation does not commute with this base change. The tensor product here uses the ambient chart projection to \(\operatorname{Spec}k[a]\); no intrinsic retraction \(Z\to C\) is assumed.

### 7.3 Characteristic two and the canonical fourth-order identification

The [characteristic-two fourth equation proof](../results/quartic_char2_fourth_equation_kernel.md#proof)
gives both exact corrected lifts, the comparison in degree four, and the
nonlinear overlap on the full embedded intersection.

### 7.4 Invariants that distinguish the fibers

| Invariant relative to marked \(C\) | Characteristic zero | Characteristic two |
|---|---|---|
| Geometric reduced support | Four quartics | Fixed quartic |
| Generic transverse length | \(1\) | \(4\) |
| Kernel sheaf of \(\phi\) | \(0\) | \(\mathcal O(-24)\) |
| Cokernel sheaf | Length \(9+9\) torsion | \(\mathcal O(-6)\) |
| Full initial ideal on first chart | \((V,a^9U)\) | \((V,U^4)\) |
| Higher minimal equations | None after degree one | \(Q_4=\mathcal O(-24)\) |
| \(K\)-adic filtration | Not nilpotent | \(K^4=0\) |

These explain the prescribed pair. Characteristic-zero normal data record combined residual contact, not the individual residual equations or their factorization. They do not decide arbitrary other global pairs.

## 8. Organizational alternatives

### 8.1 Ordinary exact diagrams

The nine-object table, master sequence (2), central sequence (8), and [filtered equation module](../arguments/filtered_equation_comparison.md#full-normal-equations-and-the-actual-equation-module) suffice for most immediate calculations. They preserve carrier symmetry, identify noninjective maps, and avoid imposing nonexistent exactness on a large diagram. The invariants are familiar; the contribution is disciplined compatibility and scope.

### 8.2 Filtered Koszul complexes

The global Koszul complex has terms
\[
\mathcal O_P(-d-e)\longrightarrow
\mathcal O_P(-d)\oplus\mathcal O_P(-e)\longrightarrow\mathcal O_P
\]
and resolves \(\mathcal O_Z\). Equip it with compatible \(I\)-filtrations; locally shift generator weights by their normal orders when appropriate. Its associated graded complex can fail to resolve \(\operatorname{gr}_K\mathcal O_Z\). Higher differentials express cancellations and new initial equations.

For a transparent example take \(f=x,g=x+y^m\), \(m\ge2\), along \(I=(x,y)\). The C-restricted first-order and relative cotangent diagrams are independent of \(m\), but intersection length is \(m\). Assign both generators weight one. The graded Koszul complex sees \((X,X)\); its relation has first nonzero higher differential
\[
d_{m-1}(e_g-e_f)=Y^m
\]
using \(E_0=\operatorname{gr}\), \(E_1=H(E_0)\). The limit recovers \(S/(X,Y^m)\). This is a concrete reason to retain the filtered complex.

At a fixed finite truncation the filtrations are finite and convergence is elementary. For an untruncated formal statement require separatedness, completeness, and the relevant convergence hypotheses. A spectral-sequence limit gives the graded target; its pages alone do not solve the remaining extension problem. See [Stacks, filtered complexes](https://stacks.math.columbia.edu/tag/012K).

Standard bases already organize lifting of leading syzygies and correction terms; see Robbiano, *On the theory of graded structures*, introduction and §3 ([original preprint](https://archive.mpim-bonn.mpg.de/2939/1/preprint_1985_17.pdf)). Global calculations must also retain actual homogeneous source spaces and twists. Calculating only over \(k(C)\) can lose special-point torsion and need not produce global equations.

### 8.3 Cotangent complexes and transitivity

For each composable triple there is a triangle
\[
Li^*L_{V/W}\longrightarrow L_{U/W}\longrightarrow L_{U/V}
\longrightarrow Li^*L_{V/W}[1].
\]
The triangles are compatible with both routes through \(X,Y\). These are standard constructions: [Stacks, fundamental triangle](https://stacks.math.columbia.edu/tag/08QR), [lci cotangent complex](https://stacks.math.columbia.edu/tag/08SH).

When \(C\to P\) and \(Z\to P\) are regular,
\[
L_{C/Z}\simeq[D\xrightarrow{\phi}E]
\quad\text{in cohomological degrees }-2,-1.
\tag{26}
\]
Indeed \(L_{Z/P}=(J/J^2)[1]\), \(L_{C/P}=E[1]\); take the transitivity cone. Thus
\(\mathcal H^{-2}=\ker\phi\), \(\mathcal H^{-1}=\operatorname{coker}\phi\).
This retains the lost left defect and supplies obstruction theory. It does not recover higher \(Q_n\) or nonlinear gluing: the family \((x,x+y^m)\) has identical (26).

The whole configuration can be organized in an enhanced derived category with compatible filtrations. The enhancement supplies coherent transitivity, not a completeness theorem for ranks, homology sheaves, or isolated Ext groups. Algebra structure and compatible extension data remain necessary.

### 8.4 Ordinary versus derived intersections

The derived intersection is \(\mathcal O_X\otimes_{\mathcal O_P}^{\mathbf L}\mathcal O_Y\). Here higher Tor vanishes: resolve one hypersurface by its one-equation resolution; its equation remains a nonzerodivisor on the other distinct integral hypersurface. Thus the derived intersection equals ordinary \(Z\), including its multiplicities.

For coincident components, nonproper intersections, or base-change problems, higher Tor can matter. Derived self-intersections also can have higher Tor even though this \(X,Y\) intersection is Tor-independent. These are different questions.

### 8.5 Rees, multigrading, and homotopy diagrams

The Rees package (20) is the simplest uniform comparison of actual intersection with normal degeneration retaining extension data. Attach cotangent triangles to deformation questions and filtered Koszul to cancellation calculations.

Multi-Rees constructions can record products \(I^rA^sB^t\), but do not automatically encode intersection filtrations \(J\cap I^n\); these must be supplied or recovered with the appropriate saturation. Extra gradings are not needed for the findings here.

Homotopy pullbacks or totalizations give no demonstrated additional invariant for this Tor-independent pair. They should be introduced only after specifying which descent, compatibility, or obstruction problem they solve. A single diagram in \(D(\mathcal O_C)\) would discard the original bases explicitly required here; work with the diagram of ringed spaces or with sheaves of derived algebras on \(P\) if such an enhancement is needed.

## 9. Recommendation and the smallest next question

Retain the actual scheme diagram and labelled ideals \(A,B,J,I\). Use the strict filtered sequence \(0\to J\to R\to R/J\to0\), equivalently its Rees form (20), as the main object. Its normal fiber (8) is the calculable degeneration. Attach the intrinsic filtered equation module, comparison (1), and cotangent triangles when needed.

Retain the bases \(X,Y,Z,C\). Replace presentation-based \(T^{(n)}\) by intrinsic \(F^nD\). Abandon the unconditional correspondence of first-order kernels with all higher initial equations. Do not treat the \(C\)-restricted normal graded algebras, spectral-sequence graded limits, or lists of bundle degrees as reconstructions of the embedded intersection.

The smooth-carrier proposition already supplies a geometric vanishing criterion. The most focused remaining question is:

> At the simultaneous singular points of two carriers along a smooth marked curve, what local conditions determine \(\Delta=\operatorname{in}_I(IJ)/(S_+H)\), and can its length and degrees be read from the filtered Koszul cancellations?

This investigation proves vanishing off that locus and failure even for integral local hypersurfaces on it. A useful next result should describe this remaining defect, beyond another isolated degree calculation.

The following precise tasks would establish further usefulness:

1. Refine [smooth-carrier vanishing](../arguments/filtered_equation_comparison.md#smooth-carrier-vanishing) by describing the defect at simultaneous singular points, with precise hypotheses and counterexamples.
2. Construct a global sheaf-level filtered standard-basis or Koszul calculation retaining homogeneous source spaces, and identify its higher differentials with actual symbol corrections across overlaps.
3. For a prescribed normal graded algebra, specify the algebra-extension and nonlinear gluing classes needed to reconstruct an embedded finite thickening, separating that reconstruction from the existence of global integral carrier equations.
4. Show that one of these constructions supplies a new obstruction, completes a finite calculation, or simplifies a proof in a scope not already covered. Notation or a larger diagram alone would not establish that usefulness.

The direction is worthwhile as rigorous organizational and computational language. Its demonstrated value here is the exact distinction between first-order relations, higher initial generators, and filtered extension data, together with the general support bound explaining the favorable quartic case. This does not establish novelty of the construction or a new global STCI consequence.

## 10. Evidence, authority, and review boundary

Retrieval followed [INDEX](../INDEX.md) to the smallest relevant records.
Reuse follows the [rules for evidence and scoped review](../MODEL.md#evidence-and-review).

| input | Exact claim used | Scope retained |
|---|---|---|
| [R0020](../results/quartic_conormal_characteristic_jump.md) | Conormal splitting | Fixed embedding; characteristic not two versus two |
| [R0021](../results/quartic_mu4_degeneration.md) | Explicit reduced/nonreduced degeneration | Prescribed equations; geometric components over splitting field |

Both were reconstructed at the chart level requested by this audit. No broader STCI exclusion or arithmetic nonlifting theorem is inferred. The current result records establish the present scopes.

The general identities, comparison direction, counterexamples, completeness distinctions, and recommendation are the assessment here. Independent workers separately reconstructed the lifting algebra, quartic charts, completeness examples, and derived diagrams. The accompanying review record states what was checked and corrected. Review within this investigation is not external acceptance.

See the [independent proof review](#2026-10-23-ideal-filtrations-independent-reviewmd) and the exact arithmetic programs linked below.

Exact finite arithmetic is supplied by the historical higher-generator counterexample script (retired; available in Git history), [completeness counterexample script](../computations/verify_ideal_filtration_completeness_2026_10_23.py), and [quartic conormal/lifting identity script](../computations/verify_ideal_filtration_quartic_lifting_2026_10_23.py). They check stated polynomial identities, finite algebra models, and transition formulas. They prove no global projective existence or nonexistence statement and do not replace the general arguments.

The [generic count and DVR length argument](../arguments/filtered_equation_comparison.md#generic-count-and-length-over-a-dvr)
continues the local comparison. The
[normal Koszul argument](../arguments/normal_koszul_cancellation.md)
proves that incoming differentials filter the defect and gives the recursive
family that realizes the prescribed page. The
[punctual comparison argument](../arguments/punctual_comparison_defects.md#statements-and-proofs)
gives the residual and supported examples.



---

## 2026-10-23-ideal-filtrations-independent-review.md

# Independent review record: ideal filtrations investigation

Date: 2026-10-23.

Target: [independent investigation](#2026-10-23-ideal-filtrations-independent-investigationmd).

Status: **independent mathematical review completed within the scopes below; proposal only**. The reviewers are independent agents in this investigation, not human referees or external acceptance authorities. A PASS means that the stated derivation was independently checked within its assigned scope. It is not evidence that a computation by itself proves the mathematics.

## Review assignments and findings

| Reviewer task | Scope independently reconstructed | Outcome |
|---|---|---|
| lifting_audit | Initial-ideal exact sequence; intrinsic equation-module filtration; presentation syzygies; quotient denominator; direction of comparison; integral local counterexample; filtered Koszul explanation | PASS after the report explicitly retained the quotient direction \(Q_n\twoheadrightarrow\operatorname{gr}_F^nD\) |
| quartic_audit | Both exact chart expansions; first-order overlap; splitting frames; conormal matrices; characteristic-zero kernel/cokernel and contact; characteristic-two global transitions, corrected lifts, and canonical fourth-order identification | PASS, with endpoint tensor base clarified |
| completeness | Full based nine-graded data versus restricted data; local integral-hypersurface counterexample and intrinsic nonisomorphism; compatible finite towers; completed-pair uniqueness; Rees repair | PASS after removing an unqualified claim that all graded data fail reconstruction |
| diagrams_derived | Nine ideal/conormal bases; seven composable triples; exact kernels; image-sheaf 3×3; higher graded maps; cotangent placement; filtered differential; convergence qualifications; derived intersection | PASS with the indicated regularity and distinctness hypotheses |

The primary agent read all three new arithmetic scripts, checked their stated scope against their calculations, and applied the review corrections. Each script was rerun in the final validation step.

## Specific substantive checks

### Filtered equation module

The reviewers reconstructed
\[
F^nD=\frac{J\cap I^n+IJ}{IJ},\qquad
\operatorname{gr}_F^nD
=\frac{J\cap I^n}
 {J\cap I^{n+1}+IJ\cap I^n}.
\]
In particular the intersection \(IJ\cap I^n\) in the denominator is essential.

Writing \(B=\operatorname{in}_I(IJ)\), multiplication gives \(S_+H\subset B\subset H\), hence
\[
0\to B_n/(S_+H)_n\to Q_n\to H_n/B_n\to0.
\]
This fixes the direction of comparison. It does not canonically split the first-order kernel into the higher pieces.

The regular-sequence presentation has syzygy \((-g,f)\in IP_0\), so the original two-generator \(T\) is intrinsic under the stated hypotheses. Redundant presentations add a fixed constant-syzygy module to every step; the graded quotients still cancel it.

### Higher-generator counterexample

For \(f=x^2+y^3\), \(g=xy+x^3+y^3\), independent checks established:

- Both carriers are integral polynomial hypersurfaces and form a local regular sequence.
- The quotient has basis \(1,x,y,y^2,y^3\), with \(x^2=xy=-y^3\), \(y^4=0\).
- Therefore \(H=(X^2,XY,Y^4)\).
- An explicit combination with both coefficients in \(I\) has initial term \(Y^4\), so \(\Delta_4=Q_4=k\).
- Independence of the quadratic initials gives \(F^3D=0\), hence \(\operatorname{gr}_F^4D=0\).
- The first higher filtered Koszul differential produces this same \(Y^4\).

The exact script checks the polynomial identities, associative five-dimensional model, filtration dimensions, and monomial comparison. Irreducibility and the general filtered-module statements are proved in the text, not inferred from that script.

### Completeness counterexample

The two intersections reduce locally to
\[
J_0=(u^2,v^4),\qquad J_1=(u^2+v^3,v^4),
\]
each originally presented by two integral hypersurfaces. Both have the same normal graded algebra \(D_0[U,V]/(U^2,V^4)\). The review checked every entry of the table after all nine graded objects are restricted to \(C\).

The intrinsic distinction is the existence of a square-zero element outside the square of the nilradical. It holds for \(J_0\) and fails for \(J_1\). The eight-dimensional models and exact square-coefficient identities support that proof.

This example is explicitly not a counterexample to the full nine-graded diagram with original bases and ambient degree-zero quotient maps. Such data already recover \(J\).

### Quartic kernel and global compatibility

The review independently checked the conormal overlap determinant \(-a^{-14}\), the characteristic-zero balanced frames, both conormal matrices, and the torsion cokernel lengths \(9+9\).

In characteristic two, the kernel frames and fourth-generator frames both transform by \(a^{-24}\). The corrected lifts map exactly to \(u^4\), respectively \(B^4\), and the intrinsic filtration has
\[
F^2D=F^3D=F^4D,\qquad F^5D=0.
\]
Thus the canonical comparison is invertible in degree four and supplies the claimed kernel-to-\(Q_4\) isomorphism. Equal line-bundle degrees alone were not used as proof.

### Additional smooth-carrier proposition

The primary agent proposed the general support statement after the initial review. Both lifting_audit and diagrams_derived independently checked it:

> Along a smooth codimension-two curve in a smooth equicharacteristic ambient threefold, for a two-generator regular-sequence ideal, a nonzero fiber conormal symbol of either carrier at \(p\) implies \(\Delta_p=0\). Therefore \(\operatorname{Supp}\Delta\subset C\cap\operatorname{Sing}X\cap\operatorname{Sing}Y\).

Both reviewers reconstructed the completed local calculation. After straightening the smooth equation,
\[
\widehat R=D_0[[x,y]],\quad I=(x,y),\quad
J=(x,h),\quad h=y^m a(t,y),\quad a(t,0)\ne0.
\]
The initial ideals are
\[
H=(X,a_0Y^m),\qquad
\operatorname{in}(IJ)=(X^2,XY,a_0Y^{m+1})=S_+H.
\]
The coefficient \(a_0\) may vanish at the closed point; it only needs to be nonzero in the domain \(D_0\). The proof uses additive \(y\)-order, not invertibility of \(a_0\). Flatness preserves the defining finite intersections and faithful flatness descends each vanishing defect piece.

This is a support containment, not equality. Both carriers being singular does not force a nonzero defect. Generic smoothness only confines the defect to special points; it does not settle those points. The proposition is independently reviewed new material in this proposal .

## Corrections made before saving the final package

1. Required \(m\ge2\) in the family \((x,x+y^m)\) when asserting identical first-order diagrams and a higher differential \(d_{m-1}\).
2. Named \(k[a]\) as the tensor base for the characteristic-zero endpoint slice, avoiding an implicit retraction \(Z\to C\).
3. Qualified the recommendation: the insufficient objects are the \(C\)-restricted normal data and graded spectral-sequence limits. The full based nine-graded diagram remains sufficient through its degree-zero data.
4. Replaced potentially ambiguous “integral closures” language by scheme-theoretic closures of an open piece.
5. Narrowed the next research question to the remaining simultaneous-singular locus after proving the smooth-carrier criterion.

## Evidence and limits

The scripts verify finite local identities and algebra models. The proof audit separately checks the general algebra, gluing, and scope arguments. No unrestricted characteristic-zero STCI theorem, new global pair, or novelty claim is certified. Result and question records remain unchanged.



---

## 2026-10-23-quartic-44-filtered-proof-proposal.md

[Complete filtered-contact proof and exact computational dependencies](../synthesis/quartic_pair_obstruction.md#5-the-distinct-proof-through-filtered-contact).

## 2026-10-23-quartic-44-filtered-proof-independent-audit.md

[Reviewed mathematical replacement: filtered-contact proof](../synthesis/quartic_pair_obstruction.md#5-the-distinct-proof-through-filtered-contact).




## Consolidated historical supplement: `research/supplements/MF6_PRINCIPAL_CANDIDATE_LOCI.md`

The following historical mathematical content is preserved verbatim with its original hypotheses, limitations, and proof status. Relative links refer to the original supplement location.

# Principal MF6 carriers: an exact finite necessary locus

For the fixed C0 in characteristic zero, use principal parameters(p,r,b)
of weights(2,1,1), direction A=1+rz,B=b+pz, and the actual principal
second-defect-one contact locus. Put

    d=p-rb,
    P=2p+12r^2+16rb+9b^2,
    T=2p-4r^2-4rb-b^2,
    U=p*P*d*(2r-b)*T.

On the integral sextic H=0 and U!=0, the
[complete contact-rank theorem](OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-principal-e1-d1-independent-completeness-auditmd)
gives rank 17 and makes the actual ambient quartic space one-dimensional. One checked
polynomial syzygy supplies its binary first-normal octic, with zero-
generator specializations kept. The fixed binary-gradient determinant
has weighted degree210, is nonzero on H, and cuts a necessary locus of
at most630 distinct principal parameters for a hypothetical nonnormal
mate carrier. Its exact zero list is uncomputed and is not the exact
nonnormal locus. The later [all-quartic theorem](../synthesis/quartic_carrier_proof.md)
closes actual mate existence. The separate complete contact-space proof
also closes this principal common-quartic-ancestor branch. The curve and
candidate calculation remain useful independent mechanisms; they do not
compute other common-ancestor incidences.

## 1. Restore the homogeneous direction parameters

Put `A=1+rz`, `B=b+pz`, with parameter weights

```
wt(p)=2, wt(r)=wt(b)=1.
```

Here b is the previously normalized b0. The weighted homogeneous
sextic direction equation is

```
H=8p^3-(64r^2+128rb+16b^2)p^2
  +(96r^4+512r^3b+592r^2b^2+128rb^3+6b^4)p
  -(576r^6+960r^5b+880r^4b^2+544r^3b^3
    +220r^2b^4+60rb^5+9b^6).
```

Its geometric integrality and genus-one normalization follow from the
[complete birational curve calculation](#the-principal-direction-sextic-has-an-elliptic-normalization). The full ambient quartic ideal has the eighteen actual forms
recorded in the accepted contact reconstruction. Their ambient torus
weights are

```
4,3,5,6,7,8,9,4,6,7,8,9,10,10,11,12,12,13.
```

The first normal map has eleven coefficient rows. The quadratic contact
map has twelve. Their combined `23x18` polynomial matrix is homogeneous
with coefficient-column offsets `wi-3` and row offsets

```
1,2,...,11; 10,11,...,21.
```

The actual normal coordinates are

```
x0=1, x1=z, x2=z^3+V, x3=z^4+U+(3/2)zV,
U=-r*m/(p-rb)+(1+rz)y,
V=-p*m/(p-rb)+(b+pz)y.
```

The full matrix specializes at b=1 to the accepted complete contact
matrix. Homogeneity uniquely restores its b powers, so this is an
actual parameter homogenization, not a different conormal frame.

Macaulay2's kernel computation supplied three polynomial generators,
of degrees 9,9,10. Their eighteen coordinates are preserved in
[`mf6-principal-weighted-kernel-2026-10-08.json`](../scratch/mf6-principal-weighted-kernel-2026-10-08.json).
Each generator's coordinate i is homogeneous of degree `D+wi-3`.
The new independent verifier checks every coordinate weight and every
first- and second-contact identity modulo H using SymPy, and checks
that the eighteen forms constitute the complete degree-four ideal
space. Thus **the three actual polynomial syzygies are proved**.
Completeness of the whole kernel module is a separate M2 output; the
candidate theorem needs only the checked first syzygy, not an assertion
that these module generators independently cover every exceptional
fiber.

This avoids the earlier rational normalization by a single ambient
coefficient. That normalization produced denominator divisors of degree
22 in r. The polynomial generators introduce no such denominator
strata. If the chosen polynomial generator vanishes at a parameter,
its entire first-normal octic vanishes and the candidate determinant
vanishes there automatically; that parameter is retained.

The full 23-by-18 contact matrix specializes at b=1 to the accepted eleven first-contact rows and twelve second-contact rows. Its row offsets are exactly 1 through 11, then 10 through 21; its column offsets are exactly 1,0,2,3,4,5,6,1,3,4,5,6,7,7,8,9,9,10. Homogeneous polynomial extension of a fixed offset is uniquely determined by its b=1 specialization: a monomial p^i r^j has the unique possible b-exponent w-2i-j. The owner checks these entry weights, each coordinate of the three degrees 9,9,10 generators, and all sixty-nine contact identities modulo H.

## 2. The geometric multiple-root necessity

### 2.1. A nonnormal mate carrier necessarily meets its conductor

Let X subset P3 be an integral quartic containing the fixed smooth
rational quartic C0. It is automatically regular at the generic point
of C0: a general integral plane quartic would otherwise have four
distinct singular points, contradicting arithmetic genus three.
The full argument is appended to the
[generic-regularity proof](../synthesis/quartic_carrier_proof.md#1-sole-support-smooth-passage-and-the-common-correction-identity).

Suppose a form G of degree b>0 has intersection support exactly C0.
For the finite normalization nu:S->X, the accepted full-support
argument gives a unique reduced smooth curve c isomorphic to C0,
div(nu^*G)=b c, and singleton entire normalization fibers above C0.
Normality of S supplies the purity needed to exclude isolated extra
zero components; no smoothness of the whole S is assumed.

If X is nonnormal, it has a codimension-one normalization defect.
Indeed X is a hypersurface and satisfies S2, so a defect supported
only in codimension two would leave R1 and force normality by Serre's
criterion. The actual conductor consequently has a curve component
upstairs E. It is distinct from c, since X is generically regular
along C0. The section nu^*G restricts generically nonzero to E, and
its line bundle is a positive power of the ample nu^*O_X(1).
On an integral projective curve such a section must have a zero;
otherwise it would trivialize a line bundle of positive degree.
Its zero lies on c by full inverse support. Thus there is a point
P in C0 which is actually nonnormal on X and whose normalization
fiber is nevertheless a singleton.

This argument uses an actual conductor curve, not a curve in a
Jacobian scheme or an arbitrarily chosen inverse-image branch. It
also remains valid if the point of S above P is singular.

### 2.2. A simple first-normal zero gives a nondegenerate quadratic pair

On the stated basepoint-free contact open, use regular ambient
parameters (x,m,y) with C0=(m=y=0) and write the first-normal term
of the actual quartic equation as h(x)m. At a nonnormal point P
the hypersurface is singular, so h(P)=0. Translate x(P) to zero.
If h has a simple zero at P, its quadratic Taylor part has the form

    a x m + A m^2 + B m y + C y^2,       a=h'(P)!=0.

There is no x^2 term because the equation vanishes on C0, and no
x y term because the first-normal y coefficient vanishes identically
in this direction frame. The x,m principal minor of the symmetric
quadratic matrix has determinant -a^2/4. Hence the Hessian rank is
at least two, independently of the other quadratic terms.

The basepoint-free condition on the direction frame is material:
it makes m,y regular normal parameters at every point where this
argument is used. A first-normal coefficient taken in a frame with
a pole or a zero would not justify this calculation. On the second
curve chart the same local argument applies, so an infinity point
is covered by the homogeneous multiple-root test.

### 2.3. Hessian rank at least two contradicts the allowed meeting

In characteristic zero, the formal splitting lemma puts a hypersurface
with a nondegenerate quadratic pair into the form

    Ahat = k[[u,v,w]]/(uv+g(w)).

For completeness, the two formal partial derivatives in the pair
variables have an invertible Jacobian. The formal implicit-function
theorem shifts their critical section to zero, and successive
formal coordinate changes eliminate higher terms involving that
pair. Completeness makes these degreewise changes converge; the
remaining function involves only w. This is the formal Morse argument
used here, not an assertion about an arbitrary tangent-only model.

If g is nonzero, write it as w^r times a unit and absorb the unit by
a formal coordinate change. At the singular point r>=2, the ring
k[[u,v,w]]/(uv+w^r) is a domain with isolated singular locus: its
partials are v,u,r w^(r-1). It is a hypersurface, hence S2, and is
regular in codimension one, hence normal. Normality of the completion
implies normality of the original local ring by faithful-flat descent;
see [Stacks, Lemma 15.44.7](https://stacks.math.columbia.edu/tag/07NU).
This contradicts P being an actual nonnormal conductor point. A
regular formal model would of course give the same contradiction.

If g=0, the completion has precisely two minimal branches, u=0 and
v=0, with normalization

    k[[u,w]] x k[[v,w]].

The algebraic local ring is excellent, since X is of finite type
over k. For an excellent local ring, the number of branches agrees
with that of its completion, and for a domain these branches count
the maximal ideals of its finite integral closure. Thus the actual
normalization fiber at P has two points. This follows directly from
[Stacks, Lemma 15.110.8](https://stacks.math.columbia.edu/tag/0C27).
It contradicts the singleton full fiber required by the mate.

Neither formal alternative is compatible with the conductor meeting
in Section 2.1. Therefore the actual first-normal coefficient has a
multiple zero at some point of C0.

## 3. Actual normal coefficient and determinant

The [independent exact coefficient checker](../computations/audit_session_mf6_weighted_candidate_2026_10_09.py) reconstructs the following data.

It independently differentiates the eighteen actual forms and contracts the first polynomial generator to produce F_U and F_V along C0, in the balanced frame

    U=-r m/d+(1+rz)y,
    V=-p m/d+(b+pz)y.

With A=1+rz and B=b+pz, it verifies the full polynomial identities modulo H

    A F_U+B F_V=0,
    hhat=-r F_U-p F_V,
    d F_U=B hhat, d F_V=-A hhat.

It reconstructs all nine coefficients h_j of hhat, checks their exact equality with the saved vector, and checks that no coefficient of degree greater than eight survives modulo H. The two latter frame identities also explain why hhat is the actual common first-normal binary octic: F_U=B h and F_V=-A h, with hhat=d h and d a unit on the declared open. The homogeneous linear direction A,B is basepoint free when d!=0. This controls both curve charts rather than only an affine derivative chosen in a frame with a zero.

Explicitly, the binary form and candidate determinant are

    hhat(s,t)=sum(h_j*s^(8-j)*t^j, j=0,...,8),
    Delta=det Sylv_7(partial_s hhat, partial_t hhat).

Here Sylv_7 is the fixed 14-by-14 Sylvester matrix of the two
homogeneous degree-seven gradients. On s=1 their coefficient
polynomials are 8*hhat(1,z)-z*hhat'(1,z) and hhat'(1,z), with the
fixed degree-seven padding even when a leading coefficient vanishes.
No h_8 division or smaller-degree resultant is substituted. The
[full symbolic coefficient vector and matrix](../scratch/session-mf6-principal-weighted-candidate-2026-10-09.json)
are literal inputs to the independent reconstruction.

Each h_j is homogeneous of parameter weight 11+j. The independently rebuilt fixed matrix agrees entry by entry with the saved matrix. Its first seven row weights are 18 through 24; its other seven row weights are 19 through 25; its column weights are 0 through 13. Every determinant term therefore has weight

    sum(18,...,24)+sum(19,...,25)-sum(0,...,13)=210.

No leading coefficient is cancelled. A control octic s times the product of seven distinct (t-j s) has a simple infinity root and nonzero gradient determinant. A control octic s^2 times the product of six distinct (t-j s) has a double infinity root and zero determinant. A zero nine-coefficient vector gives the zero fixed matrix and zero determinant. These exact controls confirm the intended behavior of the fixed degree-seven padding.

## 4. Characteristic-zero nonvanishing from the exact modular witness

The independently reconstructed sample at (p,r,b)=(4,2,1) modulo 101 has

    H=0, U=16!=0,
    (h_0,...,h_8)=(26,6,34,38,38,31,17,81,16),
    det(fixed Sylvester matrix)=22!=0.

The sample octic has degree eight and is coprime to its derivative. The modular determinant is exact finite-field arithmetic, and the sample is on H and in the declared contact open.

The audit proves H is a primitive integer polynomial, with leading coefficient 8 in p, and checks that every rational coefficient in the actual determinant matrix has denominator a power of two. Consequently Delta lies in Z[1/2][p,r,b]. If Delta vanished identically on the irreducible characteristic-zero H, H would divide Delta over Q. Clear only a power of two to make an integer polynomial; the primitive polynomial H then divides it in Z[p,r,b] by Gauss's lemma. Reducing that identity modulo 101 is legitimate. Since 101 does not divide the cleared power of two and the sample lies on H, it would force the sample determinant to be zero, contrary to 22. Thus Delta is nonzero on H in characteristic zero.

Geometric integrality of H is an accepted preceding theorem, not inferred from the single modular point. Its explicit certificate in `verify_mf6_e1_d1_principal_curve_2026_10_08.py` rules out a root of the cubic H(p,r,1) over the algebraic closure's rational function field: integrality makes a rational root polynomial in r, leading-degree comparison bounds its degree by two, and the coefficient equations for p=a r^2+c r+d have Groebner ideal (1). A cubic with no such root is absolutely irreducible. Homogenization introduces no b factor, since H contains 8p^3. The prior genus-one model is compatible with this stronger irreducibility argument but is not needed for Bezout.

## 5. Specialization and exceptional-generator qualification

At a point of U!=0 where G0 is nonzero, it lies in the complete contact kernel and hence is a nonzero scalar multiple of the unique actual quartic. That scalar and d do not change first-normal root multiplicities. The geometric necessity proved by the [geometric proof above](#2-the-geometric-multiple-root-necessity) forces a multiple projective root, so Delta vanishes.

If G0 specializes to zero, its first-normal vector specializes to zero, and Delta vanishes automatically. If G0 remains nonzero but its entire first-normal vector is zero, the same conclusion holds. No exceptional parameter was removed by dividing by a coefficient of G0, by a leading coefficient h_8, or by a rational scalar chosen on a smaller chart. The basepoint-free and contact units are the explicit U factors; parameters outside that open are handled separately, not silently added to this candidate theorem.

## 6. Ordinary-plane cover and the 630 bound

The map

    pi:P2 -> P(2,1,1), [a:r:b] -> [a^2:r:b]

is the finite quotient by a -> -a; equivalently its invariant graded ring is k[a^2,r,b], with generator degrees 2,1,1. Pullback gives ordinary homogeneous equations of degrees six and 210. Even if the lifted sextic splits, each of its irreducible curve components maps onto the integral H: finiteness prevents a curve from being contracted, and the only dimension-one closed image in H is H itself. Since Delta is nonzero on H, none of these components is contained in the pulled-back Delta. The two plane curves therefore have no common component.

Bezout bounds their scheme intersection length by 6*210=1260. A principal point has p!=0. On H it cannot have r=b=0 because H would then be 8p^3. It consequently has two distinct plane lifts [a:r:b] and [-a:r:b]: scaling would have to fix a nonzero r or b and hence be one, while a!=0 and characteristic zero forbid identifying the signs. Thus every distinct principal candidate consumes at least two distinct intersection points, proving at most 1260/2=630 candidates. Intersection multiplicities can only strengthen this upper bound; no reducedness of the intersection or irreducibility of its lift is assumed.

The bound concerns distinct weighted parameter points in the necessary locus, not 630 constructed quartics or 630 proven nonnormal fibers. Normal carriers, singularities away from C0, and generator base fibers may all occur among zeros; the exact zero list remains uncomputed here.

## 7. Bad reduction does not prove a characteristic-zero singular curve

Reductions at r=0 modulo 13 and 23 have repeated first-normal roots
and apparent triple-point jets. These are bad-reduction controls;
they do not prove a characteristic-zero nonnormal fiber or a singular
curve, as the exact cubic-field computation below shows.

The corrected r=0 computation is independently self-contained in
[`verify_session_mf6_principal_rzero_normality_2026_10_09.m2`](../computations/verify_session_mf6_principal_rzero_normality_2026_10_09.m2).
Its field polynomial is `8p^3-16p^2+6p-9`, irreducible modulo five
(the values at 0,...,4 are 1,4,3,1,1). Its literal quartic equals the
remainder in `p` of the first degree-nine
[weighted kernel generator](../scratch/mf6-principal-weighted-kernel-2026-10-08.json)
at `(r,b)=(0,1)` modulo that field polynomial. A SymPy replay checked
the equality and the two SHA-256 bindings in the
[historical input record](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/scratch/session-mf6-principal-rzero-normality-input-2026-10-09.json).
A separate Macaulay2 replay gave Jacobian cone dimension one and degree
fifteen. Dimension survives constant-field extension. Reducible or
nonreduced projective quartics have a curve of singular points, so this
also proves geometric integrality. The hypersurface S2 property and
finite singular locus prove geometric normality of all three conjugates.
The accepted normal-carrier theorem excludes their mates in every degree.

## Exact support and characteristic boundaries

The three degrees9,9,10 polynomial syzygies and the full coefficient/matrix
inputs are retained in the linked scratch files. The complete exact
checker is [verify_session_mf6_principal_weighted_candidate_2026_10_09.py](../computations/verify_session_mf6_principal_weighted_candidate_2026_10_09.py),
with the independent coefficient/infinity test linked in Section3. It
preserves the actual nine-coefficient octic and14-by14 matrix; no expanded
resultant or generic sample replaces that support. Existing independently
reviewed executions are reused without a fresh rerun.

The polynomial weight and matrix identities can be reduced where their
rational denominators are invertible. The binary-gradient multiple-root
criterion uses degree8 invertible, and the simple-zero formal splitting
argument requires two invertible. The two-to-one plane cover requires
characteristic different from two. The good prime101 witness proves
characteristic-zero nonvanishing by the primitive-polynomial argument;
it does not certify every other prime. Actual contact-rank and full-support
hypotheses must be checked before applying the same geometric inference
in positive characteristic. The direction curve itself has the explicit
[genus-one model](#the-principal-direction-sextic-has-an-elliptic-normalization) away from characteristics
two and three. None of these statements transports the full quartic-carrier
exclusion to positive characteristic.

## The principal direction sextic has an elliptic normalization

This is the actual parameter curve from the fixed-C0 principal
\(e=1,d_2=1\) contact calculation, not a curve of realized STCI mates.
The contact-space and candidate-determinant applications keep their own
hypotheses. Work first over an algebraically closed field of characteristic
zero. In the affine chart \(b=1\), its equation is
\[
\begin{aligned}
H(p,r)={}&8p^3-(64r^2+128r+16)p^2\\
&+(96r^4+512r^3+592r^2+128r+6)p\\
&-576r^6-960r^5-880r^4-544r^3-220r^2-60r-9.
\end{aligned}
\]
The corresponding weighted homogeneous curve has weights
\(\operatorname{wt}(p,r,b)=(2,1,1)\). All missing projective and contact
charts remain in that original curve; a birational chart is not a claim
that every contact frame is regular.

Put
\[
x=r+\tfrac12,\quad W=(p+2-4x)/x^2,\quad
A=-W^3+8W^2-12W+72,\quad C=2(W^2-6W+36).
\]
Direct substitution gives the exact identity
\[
H(-2+4x+Wx^2,x-\tfrac12)=-8x^4(Ax^2-2Cx+C).
\]
The quadratic in x has discriminant
\(8W^2(W-6)(W^2-6W+36)\). Its cubic factor has three distinct roots,
so this discriminant is not a square even over an algebraic closure of
the constant field. There is also no polynomial content in W:
\(C-A=W^2(W-6)\), while \(C(0)=C(6)=72\), so \(\gcd(A,C)=1\).
Finally \(H(p,-1/2)=8p(p+2)^2\) is not the zero polynomial, so no
component was lost on x=0. These observations prove geometric integrality
of the original direction curve, not merely irreducibility of a sampled
quadratic fiber.

On \(xWA\ne0\), set \(Y=(Ax-C)/W\). Then
\[
Y^2=2(W-6)(W^2-6W+36),\qquad x=(C+WY)/A.
\]
The latter equation recovers \(r=x-1/2\) and \(p=-2+4x+Wx^2\),
so the displayed maps are birational. With
\(X_E=2(W-4),Y_E=2Y\), the normalization has Weierstrass model
\[
\boxed{Y_E^2=X_E^3+96X_E-448},\qquad
\Delta=-143327232=-2^{16}3^7,\quad j=2048/3.
\]
It therefore has genus one. The same explicit birational argument and
nonzero discriminant apply after reduction in characteristic other than
two or three; this does not transport the contact-space or mate-exclusion
arguments without their additional hypotheses.

The [exact identity checker](../computations/verify_session_mf6_principal_elliptic_2026_10_08.py)
retains the literal H, inverse map, nonsquare discriminant, corrected
\(r=-1/2\) fiber and elliptic invariants. The earlier incorrect expression
\(8(p+2)^3\) for that fiber is not retained as a mathematical claim.
The geometric integrality and genus explanation is the proof above;
an existing recorded execution is reused, with no fresh rerun or
assertion that the candidate parameter locus is empty.

Historical source for this relocated section. [Source at the reconstruction baseline](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/MF6_PRINCIPAL_DIRECTION_CURVE.md).



## Consolidated historical supplement: `research/supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md`

The following historical mathematical content is preserved verbatim with its original hypotheses, limitations, and proof status. Relative links refer to the original supplement location.

# NORMAL BOUNDARY WEIGHTED INITIALS AND LIFTING

## Integration guide: boundary repair versus weighted initial data

Two complementary approaches occur below. The [global lifting criterion](#boundary-repair-global-lifting) asks whether a prescribed divisor on the curve can repair a failed global section-lifting condition; the [weighted-initial calculation](#weighted-initials-normal-boundary) studies how initial ideals and chamber decompositions change with normal weights and coefficient valuations. Neither computation may replace the other.

For a genuine surface pair, the allowable sections come from the homogeneous equation space, not the whole space of sections of a normal bundle. The [one-step boundary obstruction](BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md#2026-10-27-one-step-boundary-obstruction) supplies a separate equation-module comparison. The [intrinsic valuation dossier](../synthesis/coefficient_valuations.md) explains why arbitrary coefficient-pole series are outside the naive real-weight minimum and why scalar ideal values fail to determine colength. The [higher-initial dossier](HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#2026-10-21-higher-initial-ideals-valuations) preserves cancellation phenomena that first normal forms can miss.

**Open implication:** translating a locally admissible weighted initial configuration into an actual global pair with no residual support remains unproved here. Boundary repair is a test on a specified equation module, not an existence theorem for STCI pairs. The full chamber calculations and failed shortcuts remain below.

---


Permanent subject consolidation. All source mathematical detail retained with its original conditional and audited status.


---

<a id="boundary-repair-global-lifting"></a>

## Can the boundary repair the actual global lifting obstruction?

Date: 2026-10-26. Status: structural continuation, with
[independent review](#boundary-repair-global-lifting-audit).
No new exclusion or homogeneous realization is claimed.
No isolated example or sampled pair is used.

Continuation, October 27: the
[one-step equation-module comparison](BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md#2026-10-27-one-step-boundary-obstruction)
proves the proposed repair principle for a fixed lower embedded
thickening and identifies exact vanishing at the final Gorenstein step.
It does not settle a comparison for arbitrary ambient obstruction complexes.

### 1. The general question worth answering

The preceding [genus account](INTRINSIC_44_MULTIPLICITY_AND_GENUS_BUDGETS.md)
and [intrinsic initial construction](#weighted-initials-normal-boundary)
make boundary indices measurable, but have not shown that those indices
control the obstruction to realizing two actual homogeneous equations.
The next target is a comparison theorem between an allowed boundary
modification and a genuine global lifting problem.

For the line/socle budget, assume a proper CI Z of degrees (a,b) in P3,
sole smooth reduced support C, and generic transverse algebra K[y]/(y^m).
Then its saturated layers W_i=L^i(D_i) satisfy the inherited pairing
D_i+D_(m-1-i)=D_soc, with D_0=D_1=0. In particular 0<=D_i<=D_soc, and

    O_C(D_soc)=omega_C tensor O_C(4-a-b) tensor L^(-(m-1)).

The degree delta of D_soc is fixed once (a,b,m,L) are fixed. This is a
specific linear system and paired divisor data, not just an arbitrary
collection of punctual lengths. The higher-rank normal-layer account is
needed when the generic transverse algebra has embedding dimension two.

### 2. A precise repair criterion on any smooth projective curve

Let V be a vector bundle on a smooth connected projective curve C over
an algebraically closed field, and let o in H^1(C,V) be an identified
linear lifting obstruction. For effective D put Q_D=V(D)/V. The exact
sequence

    0 -> V -> V(D) -> Q_D -> 0

gives

    o maps to zero in H^1(V(D))
      iff o belongs to image(H^0(Q_D) -> H^1(V)).          (1)

Thus a permitted pole divisor repairs o exactly when its principal parts
can supply o. A cohomology class does not itself have a zero divisor.

By functorial Serre duality, the dual map to H^1(V) -> H^1(V(D)) is

    H^0(V^vee tensor omega_C(-D)) -> H^0(V^vee tensor omega_C).

Consequently (1) is equivalent to

    o annihilates H^0(V^vee tensor omega_C(-D)).          (2)

This is an exact criterion in arbitrary characteristic. The standard
duality input is [Stacks, section 53.4](https://stacks.math.columbia.edu/tag/0E31).
For varying D on a general curve, use the principal-parts incidence
and cohomology/base-change strata; no unqualified closed-locus assertion
across jumping cohomology dimensions is needed.

### 3. On P1, all repair divisors at once give a kernel test

Suppose V=O_P1(-r), r>=2, and n=r-2. Regard o as a linear functional on
H^0(O(n)) by Serre duality. A divisor D of degree B is the zero divisor
of some nonzero h in H^0(O(B)). For B<=n, the subspace in (2) is

    h H^0(O(n-B)) subset H^0(O(n));

for B>n it is zero. Define the multiplication matrix

    C_(B,o): H^0(O(B)) -> H^0(O(n-B))^vee,
    h |-> (g |-> o(hg)),                                (3)

interpreting H^0 of a negative line bundle as zero. Then

    some effective D of degree at most B repairs o
      iff ker C_(B,o) is nonzero.                       (4)

One can pad a divisor to obtain degree exactly B; further twisting
preserves vanishing. Conversely a nonzero kernel element cuts out an
effective degree-B divisor and satisfies (2). Repeated roots of h include
all nonreduced boundary divisors automatically. This is a statement about
an entire divisor family, not a pointwise experiment. It is often called
a catalecticant/multiplication test; its proof here is (1)--(3).

It also gives an immediate limit on the method. If

    B>=floor(r/2),

the source of (3) has dimension B+1 greater than the target dimension
max(r-1-B,0). Every obstruction then has a repair by SOME arbitrary
degree-B divisor. A single line-bundle obstruction cannot exclude using
that relaxed pole allowance. This does not show that an actual boundary
with the required paired divisors and global-source restrictions exists.

For V=direct_sum_i O(-r_i), discard summands with H^1=0, and stack

    C_(B,o): H^0(O(B))
       -> direct_sum_i H^0(O(r_i-2-B))^vee.              (5)

The SAME h must kill every component. Its nonzero kernel is exactly
simultaneous repair by one divisor. Testing each component with its own
divisor discards this common-support and common-multiplicity condition.
Multiple lifting classes can be stacked in the same manner when the
same modification is required to repair them. On fixed splitting-type
strata, (5) is a universal matrix on the actual obstruction parameter
family; full-column-rank and its failure are finite algebraic conditions.

### 4. The unproved comparison needed for our multiple curves

The following is a RESEARCH TARGET, not a consequence of the repair lemma:

    At a specified lifting stage, actual realizations with boundary
    D_soc induce a morphism of obstruction problems in which the
    obstruction o in H^1(V) becomes zero after a controlled modification
    V subset V' subset V(c D_soc), for an explicit integer c.

Proving this requires identifying the lifting complex and how saturation
changes it. There is a reason to try it. For saturated line layers,

    Hom(W_i,W_j)=L^(j-i)(D_j-D_i)
      subset L^(j-i)(D_soc).

Tensor constructions similarly give explicit multiple-divisor bounds.
These inclusions suggest possible correction bundles, but do NOT prove
that an actual realization kills the relevant obstruction in them. The
map between the lifting problems is essential. Depending on the stage,
several correction bundles or different multiples c may be necessary.

After this comparison, (1)--(5) provide necessary tests. Allowing every
divisor of degree c delta is a safe relaxation of allowing only c D_soc
with D_soc in its prescribed linear system. Failure even in the relaxed
test excludes all permitted repairs. Passing it does not prove an actual
correction or a lift: the restricted divisor, paired D_i, nonlinear
equations and actual global source may still fail.

Neither ordinary torsion T_n nor spectral comparison Delta is to be
identified with a pole allowance without proving this bridge. The
existing [R0016](../results/nonsaturated_first_relation_resultant.md)
and [R0019](../results/quasiprimitive_residual_cycles.md) already give
specific conditional divisor comparisons. They are precedents with their
own hypotheses, not authority for the proposed general comparison above.

### 5. Preserve the actual homogeneous source throughout

Let I=I_C and d a carrier degree. The actual finite normal-jet image is

    U_(d,N)=image[H^0(I(d)) -> H^0((I/I^(N+1))(d))].

The ideal-sheaf exact sequence gives the exact description

    U_(d,N)=ker[H^0((I/I^(N+1))(d))
                  -> H^1(P3,I^(N+1)(d))].              (6)

Likewise the possible first nonzero symbols of order n are

    V_(d,n)=image[H^0(I^n(d)) -> H^0(C,Sym^n E(d))]
           =ker[H^0(C,Sym^n E(d))
                  -> H^1(P3,I^(n+1)(d))].              (7)

Separate choices in the V_(d,n) do not imply one compatible finite jet
in U_(d,N). A next-jet lift also has the exact kernel bundle sequence

    0 -> Sym^N E(d) -> (I/I^(N+1))(d)
          -> (I/I^N)(d) -> 0,

whose connecting class lies in H^1(C,Sym^N E(d)). This is one explicit
kind of genuine linear lifting class; other relation/ideal lifting
problems require their own correct targets and maps.

The universal objects should range over admissible lower lifts and
boundary data while imposing (6) for both carrier degrees. Their unknown
coefficients remain constants in k. A generic nonzero obstruction only
excludes a dense open locus; its zero locus must still be studied.
An isolated successful or failed lift does not settle the family.

### 6. An exact finite endpoint for a fixed degree pair

For actual proper global F_a,G_b containing an integral C of degree d,
suppose d divides ab and put M=ab/d. At the generic point of C, let
R=O_(P3,eta_C), with maximal ideal m. Then

    Z_red=C iff length_R R/(F,G,m^(M+1))=M.              (8)

Proof: properness gives a finite generic transverse length m_C, and
Bezout bounds d m_C<=ab. An Artin local algebra of length m_C has
nilpotent maximal ideal of exponent at most m_C. Since m_C<=M, the
truncation in (8) already retains its full length. Equality m_C=M
exhausts degree ab; any residual curve would have positive degree, and
purity of the complete intersection rules out embedded components.
The converse follows in the same way from degree exhaustion.

After a chosen formal coefficient/normal chart, (8) is a finite matrix
rank condition including ALL truncated multiples of F,G. The length
criterion itself is intrinsic. The residue field K=k(C) is not asserted
to be a canonically embedded coefficient field in R/m^(M+1).

Over the universal proper-pair open set in
P H^0(I(a)) times P H^0(I(b)), the finite rank equations concern actual
global coefficients. Fixed coordinate denominators can be cleared and
rational-function identities expanded into finitely many k-equations.
This gives an exact fixed-degree question across all pairs, rather than
a sampled example. It supplies no uniform bound on carrier degrees.

### 7. What the outcomes would teach

- If no permitted boundary repairs any actual-source obstruction on a
  stratum, we obtain an exclusion of that entire stratum.
- If repair occurs only on a proper determinantal locus, it identifies
  precisely which degenerations remain; it is not a universal exclusion.
- If dimensions force repair for every class in the relaxed test, the
  isolated obstruction/pole budget is structurally too weak. Shared
  divisors, actual source images or higher relations must carry the work.
- If abstract repairs exist but (6) fails, the issue is homogeneous
  realization. If (6) passes but the multiplicative lift fails, the
  missing information is filtered ideal/algebra compatibility.
- If the exact final locus (8) is proved nonempty within the proper-pair
  open set, it gives actual fixed-degree existence, unlike survival of
  a lower-order necessary condition.

The first substantive target is the controlled-modification comparison
in section 4, followed by the common-divisor test for its actual
obstruction family. A computation is warranted if it determines a
universal map, proves its rank/zero locus, or exposes a mechanism that
persists on a stated family. No new isolated example is needed here.



---

<a id="weighted-initials-normal-boundary"></a>

## Weighted initial ideals over the coefficient curve

Date: 2026-10-26. Status: continuation, with
[independent review](#weighted-initials-normal-boundary-audit).
No STCI exclusion is claimed.

### Question and inherited scope

The question is about all weighted initial ideals, including those that
contain monomials, rather than only the monomial-free tropical locus.
Let C be smooth over algebraically closed k, K=k(C), and choose rational
normal coordinates X,Y. A point p below means a closed point of C.
Characteristic is arbitrary for the local example.

The [October 23 coefficient-valuation note](../synthesis/coefficient_valuations.md)
and its [review](../synthesis/coefficient_valuations.md)
already establish the Gauss construction, formal-series domain restriction,
coordinate dependence, and scalar-value limitation in their stated scope.
Those reviewed constructions are premises, not replay tasks.
This continuation links them to the
[normal torsion/genus account](INTRINSIC_44_MULTIPLICITY_AND_GENUS_BUDGETS.md).

### 1. The proposed valuations and their initials

With a fixed rational normal frame, for w=(alpha,beta) in Z^2,

    v_(p,w)(sum a_ij X^i Y^j)
      =min_(a_ij nonzero)(ord_p a_ij+i alpha+j beta).

This is a valuation on K[X,Y] and extends to K(X,Y). Multiplicativity
follows because initial polynomials multiply in the domain
gr_(ord_p)(K)[X,Y]. Ties preserve a nonzero residue polynomial.
Thus C_closed times Z^2 is a valid indexing family in that chosen frame.
Rational or real weights also make sense for polynomials; integral
weights alone need not sample every cell of the resulting complex.

After choosing a uniformizer t at p, write a_ij=t^(r_ij) u_ij with u_ij
a unit. The initial form retains the terms of least value, with coefficient
initials over gr_(ord_p)K=k[T,T^-1]. For integer weights one can instead
normalize residue variables and write

    in_(p,w)(f)=residue(t^(-v(f)) f(t^alpha U,t^beta V)).

This lies in k[U,V]. The integral model O_C,p[X,Y] instead has graded
coefficient ring k[T], with T noninvertible. Keeping that model lets
coefficient vanishing remain visible as torsion.

Initial ideals always use ALL elements of an ideal. Taking the two
displayed carrier initials can miss relations created by cancellation.
For a K-ideal, a scalar infimum over its nonzero elements is not useful:
multiplication by t^(-N) drives values to minus infinity. Integral ideals
and full initial ideals avoid that misuse.

For formal series with coefficients regular at p, positive normal weights
give a well-defined valuation centered at (t,X,Y). Arbitrary K[[X,Y]]
does not satisfy the necessary bounded-tail condition: the series
sum_(n>=0) t^(-n^2) X^n has term values unbounded below for each fixed
finite alpha. Finite normal symbols have no such issue. The existing
normal-first lexicographic construction is another option on the full
generic formal ring.

### 2. Newton and Groebner combinatorics

For a polynomial f, lift each exponent to

    (i,j,ord_p a_ij).

Their lower hull gives the support function w -> v_(p,w)(f). Equalities

    ord_p a_ij+i alpha+j beta
      =ord_p a_kl+k alpha+l beta

cut out rational affine walls in the weight plane. Full initial ideals
refine the comparisons for individual polynomials. At fixed coefficient
weight one, use a Groebner complex or local chamber decomposition;
do not automatically call it a fan. Allowing a coefficient weight lambda
homogenizes these equations in (lambda,alpha,beta), with our plane the
slice lambda=1. No global finite-fan assertion is needed here.

In a fixed homogeneous normal degree n, adding (c,c) to w adds nc to
every term value, so only alpha-beta affects term ties. The diagonal
direction matters when comparing different normal orders.

The tropical locus selects weights for which the full initial ideal is
monomial free. We retain every weight and its full initial algebra.
This is essential for nilpotent normal thickenings: their ideals contain
powers of the normal variables, so every initial ideal contains monomials.
The normal-torus tropical locus is empty even when the affine initial
algebras contain substantial multiplicity and boundary information.
Standard terminology and definitions appear in
[Vinzant's initial-ideal/Groebner-complex notes](https://sites.math.washington.edu/~vinzant/teaching/582D/0116.pdf).

### 3. Complete chamber calculation for the supported quadruple

Take D=k[[t]], r>=1, and

    J=(x^2,y^2+t^r x) in D[[x,y]].

Use positive rational weights (1,alpha,beta) on (t,x,y), and put

    delta=2 beta-r-alpha.

In the integral associated graded ring k[T,X,Y], the FULL initials are

| Region | Initial ideal |
| --- | --- |
| delta<0 | (X^2,Y^2) |
| delta=0 | (X^2,Y^2+T^r X) |
| delta>0 | (X^2,T^r X,XY^2,Y^4) |

For delta<0 the two displayed initials are coprime monomials. For delta=0
they are the regular sequence X^2,Y^2+T^r X. In either case the two
equations form a filtered standard basis.

For delta>0, set f=x^2, g=y^2+t^r x, h=xy^2, q=y^4. The latter two
belong to J by the exact identities

    xg-t^r f=h,       y^2g-t^r h=q.

The monomial initials of f,g,h,q are X^2,T^r X,XY^2,Y^4. Their syzygies
are generated by the pairs (f,g),(f,h),(g,h),(h,q). They lift as

    t^r f-xg+h=0,     y^2 f-xh=0,
    y^2 g-t^r h-q=0,  y^2 h-xq=0.

In the first and third identities the correction has higher weight by
delta>0; the others lift exactly. The complete filtered syzygy-lifting
criterion proves the full-initial claim for all the stated weights.
This is a symbolic proof, not an inference from sampled weights.

The wall

    2 beta=alpha+r

retains the boundary exponent r. In the delta>0 chamber, preserving the
normal-degree grading, the T-torsion has length r in each of normal
degrees one and two. The total local torsion is 2r and the socle divisor
is r[p], as in the preceding genus note.

After inverting T, the three normalized residue initial ideals become

    (U^2,V^2),   (U^2,V^2+U),   (U,V^4),

respectively. Each has quotient length four. A single field initial
algebra no longer displays the exponent r in its torsion modules. The
valued-field FAMILY still retains r through the wall location. Thus do
not claim that all valued-field data lose the boundary; the integral
lattice is what identifies its actual torsion/divisor/genus contribution.

### 4. Frame changes and the information to retain

For diagonal changes X'=fX,Y'=gY, the same valuation has weights

    alpha'=alpha+ord_p f, beta'=beta+ord_p g.

The accompanying coefficient transformation makes the value of the
actual normal form unchanged. General GL_2 changes can require residue
relations, rather than a transformation of weight vectors alone. For
example v(X)=1,v(Y)=2 and X'=X,Y'=Y+X give v(X')=v(Y')=1 but
v(Y'-X')=2. A newly chosen monomial Gauss valuation of weights (1,1)
would give value one to that difference. The transported valuation
remembers in(Y')=in(X').

Thus C_closed times Z^2 is a coordinate chart for this family, not an
intrinsic product independent of the normal frame. Integral models and
their transitions must be retained when adding divisor degrees globally.

Scalar ideal minima alone are also insufficient: (X^2,Y^2) and
(X^2,XY,Y^2) have the same value under every centered valuation but
colengths four and three. Valuations belong on the ambient normal
algebra; a valuation on a nonreduced quotient kills its nilpotents.

There is an exact determinant bridge to the preceding genus budget.
In normal degree n, let a matrix M_n over D have columns generating
H_n subset Sym^n E_p, of generic rank h. Smith form writes its nonzero
invariant factors as t^(e_1),...,t^(e_h), and gives

    mult_p B_n=length_D(H_n^sat/H_n)=sum e_i
      =min ord_p(nonzero h-by-h minors of M_n).

For rank zero this contribution is zero. This formula is independent of
integral frame changes. It turns the torsion budget into valuations of
determinants, while preserving cancellations inside those determinants.
For example the matrix with columns (1,1) and (1,1+t^r) has all entry
valuations zero, but determinant valuation r. Entry valuations alone
miss this boundary index; the residue relations and their lifts matter.

The proposed data to retain are the local full initial algebras, their
integral coefficient lattices, their normal grading, and frame-transition
maps. Their combinatorics constrain the boundary divisors from the genus
budget and the initial relation modules entering the normal Koszul
spectral sequence. A weighted wall by itself is not identified with a
spectral-sequence page. Global realization still requires the actual
homogeneous carrier sections and filtered gluing.

### 5. Intrinsic normal symbols and weighted flags

This continuation answers the question about removing normal-coordinate
choices. All constructions here are intrinsic to the indicated embedded
configuration, not to the abstract curve independently of its embedding.

For C regularly embedded in a smooth threefold X, put E=I/I^2. The
canonical algebra is

    S=gr_I O_X=Sym E.

A degree-a hypersurface of normal order n has initial symbol in
Sym^n E tensor O_C(a), without choosing X,Y. For C subset Z subset X,

    H=ker(S -> gr_(I O_Z) O_Z)

is the intrinsic full initial ideal sheaf. These are the normal-cone
constructions in [Stacks, section 31.20](https://stacks.math.columbia.edu/tag/062Z),
with regular-immersion identification in
[section 31.22](https://stacks.math.columbia.edu/tag/0638).

For a rational section s of a vector bundle V on C, its coefficient
order at p is intrinsically

    c_p(s)=max{q in Z : s belongs to m_p^q V_p}.

Negative powers mean fractional lattices. Its coefficient initial lies
in (m_p^q/m_p^(q+1)) tensor V|p. In an integral local frame this is the
minimum of the component orders, but the definition uses no frame or
uniformizer. This applies also to the twisted normal-symbol bundles.

Equal normal weights need only E: for finite graded sums s=sum s_n in
S_K, the valuation

    v_(p,a)(s)=min_n(c_p(s_n)+a n)

is intrinsic. In any integral normal frame it is the previous Gauss
formula with w_X=w_Y=a. The associated graded ring is locally a
polynomial ring over gr_(m_p)O_C,p for the integral model; on S_K the
coefficient ring is localized to gr_(ord_p)K=k[T,T^-1]. Both are domains,
which proves multiplicativity.

For the full integer-weight family there is an especially direct
coordinate-free replacement for a weight pair. Choose an O_C,p-lattice
Lambda subset E_K, meaning a free rank-two module spanning E_K, and set

    c_(Lambda,n)(s)=max{r:s belongs to m_p^r Sym^n Lambda},
    v_Lambda(sum s_n)=min_n c_(Lambda,n)(s_n).

This is a valuation on Sym_K E_K and its fraction field. Any integral
basis of Lambda proves the Gauss property, while its definition uses
only Lambda. The unit ball on degree one recovers Lambda itself.
The old chosen-frame formula corresponds precisely to

    Lambda_w=m_p^(-w_X) O_C,p X + m_p^(-w_Y) O_C,p Y.

Thus the intrinsic indexing set is pairs (p,Lambda), rather than a
canonically fixed C times Z^2. A frame displays diagonal lattices.
For common weight a, Lambda=m_p^(-a) E_p gives the construction above.

Up to homothety these rank-two lattices are the vertices of the
Bruhat--Tits tree; a basis displays one apartment. The actual lattice,
including its scale, is needed here: replacing Lambda by m_p^(-c)Lambda
adds nc to the value in normal degree n. For the general-DVR lattice
and tree construction see Ludwig--Merten,
[section 3](https://afm.episciences.org/18061/pdf). No finite-residue-field
assumption or fixed finite valency is imposed here.

Unequal weights require a weighted flag of E, rather than two named
coordinates. Suppose an intrinsic line subbundle R subset E is given,
with quotient line L. In the generically curvilinear thickening studied
above this flag is supplied by Z itself:

    L=(K/K^2)/torsion, R=ker(E -> L).

Thus R is the saturation of the actual first-symbol image even where
that image degenerates. No splitting of 0 -> R -> E -> L -> 0 is needed.

Assign weight beta to R and alpha to L, with beta>alpha. Use the
intrinsic lattice

    Lambda_(alpha,beta)=m_p^(-beta) R_p+m_p^(-alpha) E_p.

Its symmetric powers give equivalently
the intrinsic filtration

    B_(n,j)=image(R^j tensor Sym^(n-j) E -> Sym^n E),
    B_(n,j)/B_(n,j+1)=R^j tensor L^(n-j).

Its level is n alpha+j(beta-alpha). Combining with coefficient order
at p gives the full basis-free formula, for integer alpha,beta,q,

    F^q(S_n tensor K)
      =sum_(j=0)^n m_p^(q-n alpha-j(beta-alpha)) B_(n,j),p.

For real weights use the ceiling of each exponent. For finite graded
sums take the direct sum over n. In an adapted integral frame X spanning
R and Y lifting L, this is exactly

    min(ord_p a_ij+i beta+j alpha).

To check independence, another adapted frame has X'=uX,
Y'=vY+bX with u,v units and b regular at p. Since beta>alpha, both this
substitution and its inverse preserve the filtration. Consequently the
valuation and its associated initial algebra are independent of the
adapted frame, despite a possibly nonsplit extension. The model lives
on the normal bundle Spec_C Sym E, which has a canonical projection to C.

This is an additional flag if only C subset X is specified. When Z is
generically curvilinear it is intrinsic to C subset Z subset X. For a
candidate-search problem the flag is data to vary, rather than a reason
to choose a global coordinate frame. This does not select a canonical
unequal-weight flag from an arbitrary bare rank-two bundle.

For the fixed rational quartic there is also a distinguished flag before
choosing Z: its unique smooth quadric Q gives the specified sequence
0 -> O(-8) -> E -> O(-6) -> 0 in
[R0020](../results/quartic_conormal_characteristic_jump.md). That flag
defines weighted normal-algebra filtrations in characteristic zero too,
where the extension is nonsplit. A hypothetical thickening's flag R
need not equal this quadric flag; no alignment is assumed.

The actual ambient neighborhood needs a further distinction. A full
Taylor expansion into separate normal degrees requires extra splitting
data; the normal-symbol algebra alone does not supply it. Even an
adapted conormal flag does not determine arbitrary finite weighted
valuations on the full ambient formal ring. For example the lifts
x and x'=x+y^2 have the same class in I/I^2, while a Gauss valuation
with v(x)=beta>2 alpha=2v(y) gives v(x')=2 alpha. Thus the flag
construction on S is an intrinsic refinement of the normal initial
algebra, not an assertion that every ambient weighted initial ideal is
determined by E and R alone. Retain Rees/filtered neighborhood data for
actual equations and cancellations between different normal orders.

For intrinsic valuations directly on the ambient function field there
is the already reviewed geometric route. Let D_exc be the exceptional
divisor of Bl_C X, with fiber D_p over p. The flag

    Bl_C X superset D_exc superset D_p

gives the normal-first, coefficient-second valuation. A point q in D_p
refines it to a full flag and remembers a normal direction. For a
normal symbol s of degree n, first take r=c_p(s), then take the zero
order at q of its residue binary-form section. This yields the local
lexicographic description (n,r,order_q residue(s)); the flag and
section-valued initials provide the intrinsic meaning. Uniformizers
used for numerical labels must be compatible with the flag. Composition
is justified by [Stacks, Lemma 10.50.10](https://stacks.math.columbia.edu/tag/088Z).

Here D_exc=Proj_C Sym E, with points interpreted as one-dimensional
quotients of E. The quotient E -> L supplied by a curvilinear Z picks a
section and hence a distinguished q_p in each D_p. Use the ambient
exceptional divisor: Proj gr_K O_Z is empty for a solely supported
nilpotent thickening. The lexicographic flag valuation and the finite
weighted flag filtrations are distinct constructions; a linear
functional on the lexicographic leading value does not in general
recover the finite weighted minimum of an arbitrary sum.

All boundary divisors B_n=div Fitt_0(H_n^sat/H_n) and the genus budget
already have this intrinsic meaning. Frame polynomials are ways of
calculating their initial objects and maps, not part of their definition.



---

#### Consolidated mathematical status of the boundary-repair calculation

The preceding derivation and its independent reconstruction establish the same exact statement: for a **specified** class \(o\in H^1(C,V)\), allowing poles on an effective divisor \(D\) kills \(o\) precisely when \(o\) annihilates \(H^0(C,V^\vee\otimes\omega_C(-D))\). For \(V=\mathcal O_{\mathbf P^1}(-r)\), all degree-\(B\) repairs are captured simultaneously by the kernel of the catalecticant
\[
H^0(\mathcal O(B))\longrightarrow H^0(\mathcal O(r-2-B))^\vee,\quad h\longmapsto(g\longmapsto o(hg)).
\]
In particular, \(B\ge\lfloor r/2\rfloor\) forces a nonzero kernel for **arbitrary** allowed divisors; it does not force a geometrically admissible boundary. For a split bundle, a **single common** \(h\) must solve all component equations. The original proof of the criterion and the full independent reconstruction remain below, but their repeated statements are consolidated here rather than presented as separate advances.

The exact finite-degree endpoint in the review likewise requires actual proper global forms: if \(C\) has degree \(d\), \(F,G\) have degrees \(a,b\), and \(M=ab/d\) is integral, then the length of the generic transverse algebra truncated at order \(M+1\) is \(M\) exactly when the entire reduced intersection is \(C\). This is a *recognition test*, not a construction. The missing step is still to compare the permitted socle/boundary modifications with the obstruction to lifting an **embedded** lower thickening into actual homogeneous source spaces. Neither the abstract \(H^1\)-test nor the reviewed fixed-lower comparison proves that bridge for arbitrary pairs.

### boundary-repair-global-lifting-audit

#### Independent scope checks

The primary derivation above supplies the cohomological repair theorem, the common-divisor catalecticant test, the actual homogeneous source-image formulas and the fixed-degree endpoint. The remaining verification below records the **distinct** limitations relevant to applying these statements to embedded thickenings. No theorem identifies arbitrary allowed boundary divisors with realizable global lifts.

### 2–3. Independent verification of the repair criterion and common-divisor test

The proof of the principal-parts criterion and its Serre-dual annihilator formulation is given in the primary calculation above, sections 2–3. The independent reconstruction checked the direction of the connecting homomorphism and the \(-D\) twist, including arbitrary characteristic. It also verified that for \(V=\mathcal O_{\mathbf P^1}(-r)\) the kernel of the multiplication map parametrizes **all** effective degree-\(B\) repair divisors, including nonreduced ones; padding a smaller divisor preserves vanishing. The dimension threshold \(B\ge\lfloor r/2\rfloor\) is correct. For a split bundle the *same* section \(h\) must lie in every component kernel; separate componentwise choices would not solve the simultaneous problem. No stronger existence or realization conclusion follows.

### 4. The boundary comparison is not proved by these criteria

The inherited relations D_i+D_(m-1-i)=D_soc and effectivity imply
0<=D_i<=D_soc. Accordingly

    Hom(L^i(D_i),L^j(D_j))
      =L^(j-i)(D_j-D_i) subset L^(j-i)(D_soc)

is correct. These are inclusions of possible coefficient bundles. They
do not prove a morphism of lifting problems or identify the obstruction
for an actual multiple curve with its image under a chosen twist.

The source explicitly marks the needed V -> V' -> V(c D_soc) comparison
as unproved, requires the actual lifting complex, and does not identify
ordinary torsion, spectral Delta, and allowed principal parts. This is
the essential remaining dependency. The relaxation to arbitrary divisors
of degree c delta is logically safe only after the comparison is supplied:
failure of the relaxed test excludes permitted repairs; passing it proves
neither the constrained divisor data nor a genuine lift.

### 5. Actual homogeneous jet and symbol images

The source-image formulas follow directly from the sheaf sequences

    0 -> I^(N+1)(d) -> I(d) -> (I/I^(N+1))(d) -> 0,
    0 -> I^(n+1)(d) -> I^n(d) -> Sym^n E(d) -> 0.

Their H^0 images are precisely the displayed connecting-map kernels.
The second sequence uses the regular embedding of C in the smooth
threefold. These are actual global k-linear source images, not arbitrary
K=k(C) normal symbols.

The next-jet sequence with kernel Sym^N E(d) is likewise exact. Its
connecting class is in H^1(C,Sym^N E(d)), as stated. The note correctly
distinguishes this explicit linear jet obstruction from other relation
or ideal lifting problems, whose targets have not been supplied by that
sequence. Choosing allowable graded symbols separately does not specify
one compatible jet, so retaining the whole source U_(d,N) is necessary.

### 6. Fixed-degree generic length and degree exhaustion

Let F,G be actual global forms of degrees a,b defining a proper complete
intersection containing an integral C of degree d, and suppose M=ab/d
is an integer. At eta_C the two equations have finite transverse length
m_C. The fundamental cycle and Bezout give d m_C<=ab, hence m_C<=M.

For any Artin local algebra of length m_C, every nonzero successive
maximal-ideal power strictly decreases length: equality of adjacent
powers would make that power zero by Nakayama. Therefore its maximal
ideal has exponent at most m_C. The quotient by m^(M+1) already retains
the full local algebra R/(F,G), and its length is m_C.

It follows that the truncated length is M exactly when m_C=M. Then the
contribution of C consumes degree ab. Any additional curve component
would contribute positive degree, while purity of the proper complete
intersection rules out embedded components. Conversely sole reduced
support C gives m_C=M. This proves the intrinsic finite endpoint in
the source, with all its properness and actual-global-form hypotheses.

The matrix interpretation requires all truncated multiples. The note
appropriately states that a coefficient/normal chart is chosen for that
calculation: the residue field is not claimed to be canonically embedded
in R/m^(M+1). Fixed chart denominators can be cleared, with coefficients
of the actual forms remaining constants in k. One must retain the proper
pair open locus. No bound uniform in a,b follows from this fixed-degree
criterion.


---

#### Consolidated mathematical status of the weighted-initial calculation

The source and its independent reconstruction agree on the precise domain: a chosen rational normal frame and a coefficient valuation \(v_p\) give weighted Gauss valuations on \(k(C)[X,Y]\); arbitrary \(k(C)[[X,Y]]\) does **not** admit the same finite real-valued formula without a bounded-tail hypothesis. A normal-first lexicographic valuation is a distinct alternative. The weights give an affine chamber decomposition in a fixed coefficient-weight slice, not automatically a canonical global fan. Full initial **ideals**, including cancellation, are essential; the monomial-free tropical locus alone loses the nilpotent intersection algebra.

For the integral family \(J=(x^2,y^2+t^r x)\subset k[[t,x,y]]\), put \(\delta=2\beta-r-\alpha\), where the weights of \(t,x,y\) are \(1,\alpha,\beta\). The complete chamber computation gives
\[
\operatorname{in}(J)=
\begin{cases}
(X^2,Y^2),&\delta<0,\\
(X^2,Y^2+T^rX),&\delta=0,\\
(X^2,T^rX,XY^2,Y^4),&\delta>0.
\end{cases}
\]
Here \(T\) remains noninvertible in the integral graded coefficient ring. The third chamber requires the cancellation generators \(xy^2\) and \(y^4\); it cannot be read from the two displayed initial generators. The source proof and independent syzygy verification remain below for full detail. The resulting normal-lattice torsion and determinant indices are coordinate-sensitive until their frame-change and residue data are retained. This local example proves neither a global finite-generation theorem nor a characteristic-zero STCI exclusion.

<a id="weighted-initials-normal-boundary-audit"></a>

## Independent audit: weighted initials and normal boundary data

Date: 2026-10-26. Reviewer: independent `valuation_budget` agent.
Status: independent reconstruction of the [companion continuation](#weighted-initials-normal-boundary).
Outcome: **PASS within the stated domains and hypotheses**. This is reviewed
evidence, not a global realization or an
STCI exclusion.

### Scope and method

The reviewer read the retrieval index and the preceding normal-torsion
budget, then independently checked the integral chamber calculation,
coefficient-ring distinctions, frame changes, and determinant-lattice
bridge. The existing reviewed Gauss/domain construction is used in its
stated scope; inherited certificates and accepted exclusions were not
rerun. No finite sample is used to justify the all-weights calculation.

### 1. Verification of domains and frames

The preceding source gives the Gauss valuation on \(k(C)[X,Y]\), the distinction between \(k[T]\) and \(k[T,T^{-1}]\) in the graded coefficient ring, and the divergent series \(\sum t^{-n^2}X^n\) excluding arbitrary formal series. The independent review reconstructed these facts for the stated positive rational weights, including tied residue terms. It also checked that a diagonal frame change \(X'=fX\) shifts the transported weight by \(\operatorname{ord}_p(f)\), whereas a general \(\mathrm{GL}_2\) change requires initial residue relations, not merely the new variable values. At fixed coefficient weight the chambers form an affine complex, not automatically a fan; integer weights may miss rational chambers. These verifications do not establish a canonical global family of weighted valuations.

### 2. Full chamber calculation, all stated weights

Let J=(x^2,y^2+t^r x) in D[[x,y]], r>=1, and give (t,x,y)
positive rational weights (1,alpha,beta). Put delta=2 beta-r-alpha.
The integral associated graded coefficient ring is k[T].

If delta<0, the carrier initials are X^2,Y^2. They form a regular
sequence, so their Koszul syzygy lifts and no extra initial generator
appears. If delta=0, the initials are X^2,Y^2+T^rX. This is again a
regular sequence: modulo X^2, the second polynomial is monic in Y and
is therefore a nonzerodivisor. The standard filtered argument gives the
claimed full initial ideal in both cases.

For delta>0, set f=x^2, g=y^2+t^r x, h=xy^2, q=y^4. Their initials are

    X^2, T^rX, XY^2, Y^4.

All pair syzygies of these four monomials are generated by the pairs
(f,g), (f,h), (g,h), (h,q). The omitted (f,q) and (g,q) pair syzygies
factor through h. The displayed identities

    t^r f-xg+h=0,     y^2 f-xh=0,
    y^2 g-t^r h-q=0,  y^2 h-xq=0

lift those generators. In the first identity, h has weight delta more
than t^r f and x times the initial term of g. In the third, q has weight
delta more than y^2 times that initial term and t^r h. The other two
identities lift without corrections. Positive rational weights may be
scaled to positive integer weights, and completeness permits successive
strict increases of weight. The filtered syzygy criterion therefore
proves the FULL initial ideal, not just inclusion, for every stated
weight. The argument and identities work in arbitrary characteristic.

The three chamber ideals in the source are consequently correct. After
inverting T and normalizing, they become

    (U^2,V^2), (U^2,V^2+U), (U,V^4),

each of colength four. The family still remembers r in the wall
2 beta=alpha+r, even though one normalized field initial does not
display an r-length coefficient-torsion module. The source explicitly
preserves this distinction and does not overstate information loss.

In the delta>0 chamber the ideal is homogeneous for normal degree if
deg X=deg Y=1 and deg T=0. Its coefficient torsion has length r in
normal degrees one and two. Thus tau_p=2r and D_soc=r[p], agreeing
with the prior pointwise budget. On the wall, Y^2+T^rX mixes two normal
degrees. In the delta<0 chamber the initial ideal is normal homogeneous,
but its normal layers are those of this different weighted degeneration,
not the ordinary normal layers of B. Their absence of coefficient torsion
does not contradict the ordinary torsion budget or imply an extra component.

### 3. Determinants recover the normal saturation indices

The additional Smith-minor bridge is correct. Let columns of a matrix M
over D generate H_n inside the free module S_n, and let h be its rank.
Smith form reduces M by invertible row and column operations to its
nonzero entries t^(e_1),...,t^(e_h), up to units. Hence

    length_D(H_n^sat/H_n)=sum e_i
      =min ord_t(nonzero h by h minors of M).

For h=0, the index is zero, with the empty minor interpreted as one.
This is the local multiplicity of the intrinsic divisor B_n. It is
invariant under integral frame changes and depends on the integral
lattice, not merely the generic subspace H_n tensor k((t)).

For M=[[1,1],[1,1+t^r]], every entry has valuation zero but det M=t^r.
Thus entrywise valuations or a tropical determinant lower bound need
not determine the index: tied leading terms can cancel. Actual minor
valuations and residue/initial relations retain this information. This
supports the proposed use of full initial data rather than scalar minima.

### 4. Scope boundaries and outcome

Monomial-containing initials must be retained for the stated problem.
A nilpotent normal ideal contains powers of the normal variables, so
its full initial ideal contains monomials at every weight. Its normal
torus tropical locus can therefore be empty while its affine initial
algebras retain the relevant thickness. The equality of scalar ideal
values for (X^2,Y^2) and (X^2,XY,Y^2) is also correct under every
centered valuation; their different colengths show what those scalar
values omit.

The source does not identify weighted walls with normal-Koszul
spectral-sequence pages. Those pages depend on the specified normal
filtration and its higher differential maps. Weighted initials can
organize initial relations and coefficient defects without independently
supplying the extension data or a global descent theorem. Actual
homogeneous carrier sections, frame transitions, and filtered gluing
remain necessary for global realization.

No substantive correction to the inspected continuation is required.
The all-weights chamber proof and the Smith-minor bridge are independently
reconstructed here.

### 5. Additional independent review of intrinsic symbols and weighted flags

Reviewer: independent `budget_audit` agent, 2026-10-26. This addendum reviews
only the newly appended section 5 of the source. It independently checks
the intrinsic constructions and their coordinate qualifications; no
inherited proof or certificate is replayed.

For a regular immersion C subset X, the identification
gr_I O_X=Sym(I/I^2) and the kernel definition of the full initial ideal H
are intrinsic to the marked embedding. A normal-order-n degree-a equation
has symbol in Sym^n E tensor O_C(a); choosing local normal coordinates is
unnecessary for that assertion. The coefficient order

    c_p(s)=max{q : s belongs to m_p^q V_p}

is likewise invariant under GL(V_p) over the local DVR. Its associated
initial is a section of the stated graded coefficient line tensored with
the fibre of V. The zero section has order infinity, as usual.

One coefficient-ring qualification was requested in the source: on the
integral local algebra Sym(E_p), the equal-weight associated graded is a
polynomial algebra over gr_m O_C,p=k(p)[T]. On S_K=Sym(E) tensor k(C),
the coefficient parameter is invertible, so the coefficient graded ring
is k(p)[T,T^(-1)]. The valuation remains multiplicative in either domain;
the integral statement followed by localization proves the field version.
This is a ring-domain correction, not a change to the valuation formula.

For unequal weights, let R subset E be a line subbundle, L=E/R, and
beta>alpha. In an adapted frame X for R and Y lifting L, the submodule

    B_(n,j)=image(R^j tensor Sym^(n-j) E -> Sym^n E)

has basis X^i Y^(n-i) for i>=j. It follows directly that the proposed
sum

    sum_(j=0)^n m_p^(q-n alpha-j(beta-alpha)) B_(n,j),p

contains a coefficient of X^i Y^(n-i) exactly when its order is at least
q-i beta-(n-i)alpha. For real weights this lower integer bound is the
ceiling of the exponent. Thus the basis-free filtration is exactly the
displayed Gauss minimum, without requiring a splitting E=R direct_sum L.

An adapted change X'=uX, Y'=vY+bX, with u,v units and b integral, preserves
the filtration: the added term bX has weight at least beta>alpha. The
inverse is adapted and has the same property, proving equality rather
than only one-sided containment. On associated graded normal variables,
the off-diagonal term vanishes and the diagonal unit changes remain.
Consequently the filtration and associated initial algebra are independent
of the adapted integral frame. A nonsplit extension is therefore not an
obstruction to this construction. The flag is additional data for a bare
embedding, and is supplied intrinsically by a generically curvilinear
marked thickening through E -> (K/K^2)/torsion. This distinction is stated
correctly.

The ambient warning is necessary and correct. The coordinate lifts x and
x+y^2 have the same class in I/I^2, but under beta>2 alpha their ambient
Gauss values differ. Hence the conormal flag alone does not determine
every finite weighted filtration on the full ambient formal ring. The
construction on Sym E has a canonical projection to C and must retain
its stated separation from actual filtered-neighborhood data.

For the geometric alternative, the exceptional divisor of Bl_C X is
Proj_C Sym E in the quotient-line convention. The fibre over p and a
point q in that fibre give the stated regular flag. For a homogeneous
normal symbol its three-stage value is normal degree, coefficient order,
and zero order of the normalized residue binary-form section at q;
local Cartier equations and coefficient uniformizers must be chosen
compatibly with the flag. The quotient E -> L selects the claimed section
of this exceptional divisor. If K is nilpotent, the irrelevant ideal of
gr_K O_Z is nilpotent as well, so its Proj is empty. Using the ambient
exceptional divisor is therefore essential.

Finally, the lexicographic flag valuation and the finite weighted minimum
are correctly distinguished. Selecting a lexicographic leading term and
then applying a linear weight need not select the least weighted term of
the original sum. The intrinsic determinant/saturation boundary divisors
remain independent of these coordinate presentations.

**Addendum outcome:** PASS after the coefficient-ring qualification above;
no further mathematical correction is required. The findings remain
reviewed evidence, with no new global realization or exclusion.

### 6. Lattice formulation: independent verification and scope

The preceding intrinsic-symbol and weighted-flag calculation is equivalent, for integral weights, to a full \(D=\mathcal O_{C,p}\)-lattice \(\Lambda\subset E_K\), with valuation on \(\operatorname{Sym}_K E_K\) defined by the coefficient orders relative to \(\operatorname{Sym}^n\Lambda\). An integral basis makes this a Gauss valuation, and its degree-one unit ball recovers \(\Lambda\). This was independently checked, including negative integer weights.

The scale matters: replacing \(\Lambda\) by \(\mathfrak m^{-c}\Lambda\) shifts the value of a degree-\(n\) symbol by \(nc\). For a saturated line \(R\subset E\), quotient \(L\), and \(\beta>\alpha\), the nonsplit intrinsic lattice
\[
\Lambda=\mathfrak m^{-\beta}R_p+\mathfrak m^{-\alpha}E_p
\]
reproduces the preceding filtration by the submodules \(B_{n,j}\). Real weights instead use the ceiling filtration; a single \(D\)-lattice is not claimed. This verifies the earlier calculation without repeating its adapted-basis expansion.

The conclusion is confined to the normal-bundle symmetric algebra (or its fraction field), **not** the entire ambient formal neighborhood. In particular, \(x\) and \(x+y^2\) have the same conormal class but can have different weighted ambient values when \(\beta>2\alpha\). No global realization or exclusion follows.




## Consolidated historical supplement: `research/supplements/OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md`

The following historical mathematical content is preserved verbatim with its original hypotheses, limitations, and proof status. Relative links refer to the original supplement location.

# Symbolic ribbons, valuation bounds and normalization controls

Complete source text preserved below, including explicit hypotheses, calculations, counterexamples and unresolved issues. Compilation is not an independent correctness audit.

---

<a id="source-2026-10-13-generalization-quintic-continuationmd"></a>

## Nonendpoint quintics: conductor root support instead of mate-degree searches

Date: 2026-10-13 continuation, written after midnight on October 14. Owner:
`quintic_continuation`. Status: **ZERO-CUBIC AND LAMBDA-ONE FAMILY EXCLUSIONS, THE MAIN
THREE-ROOT/FOURFOLD ALTERNATIVES, AND REGULAR SOLE-ROOT L1/L2 HAVE
PASSED INDEPENDENT AUDIT. THE FINAL MAIN 3+2 ORIGINAL-GENERATOR
WITNESS IS IN PROGRESS.** Accepted older
proofs are premises and were not replayed. The universal problem, higher
carriers, other quintic normalization genera and the full nonendpoint
common-root incidence remain unresolved.

### 1. Authoritative inherited scope

Use the accepted characteristic-zero degree-five genus-one A4 pair `(S,c)`
and actual nonendpoint projection with `delta!=0`, all four lift parameters,
center avoidance and finite birationality. The curve `c` maps isomorphically
to the fixed quartic C0. A mate of any positive degree forces the entire
inverse support `nu^{-1}(C0)_red=c` (SUP). The accepted full conductor is an
effective Cartier divisor on S in `|2H|`; its actual restriction to c is the
nonzero binary octic F, retaining all multiplicities and infinity roots.
The accepted support bridge is

    supp(F) subset supp(H P^epsilon),
    epsilon=1 if Jbar=0, and zero otherwise,

where H is the complete homogeneous gcd of the corrected conormal cubics
and P=0 is the intrinsic A4 target. This concerns the actual conductor
section; no upper contact bound is inferred from first-normal data.

The October 13 full cubic-pair audit accepts the entire residual surface
partition 3+3 as an all-mate exclusion, including doubled cubics. Its
stronger SUP exclusion is qualified to Jbar!=0; the Jbar=0 portion uses the
separate accepted all-power line argument. The residual surface partitions
2+4 and 2+2+2 are already excluded. Thus the surface residual is integral
in any remaining mate lane. The conductor quintic S below is a polynomial
factor of the restricted conductor octic; it is not that degree-six
residual surface divisor.

### 2. Complete h=3 parameters and the conductor factorization

The accepted homogeneous gcd classification says h=3 consists of the two
zero-cubic charts and the proportional main chart. On the main chart write
`J=lambda P`, with lambda nonzero. Its complete parameters are

    a=delta(delta+2lambda-1)/(6lambda^2),
    b=delta(delta+2lambda-1)/(3lambda),
    g=delta((lambda-3)delta+lambda+1)/3,
    d=delta((lambda^2-12)delta+lambda^2-2lambda+6)/6.

The accepted/new evening conductor coefficient artifacts give

    F = -delta^4 H3 S5/(1296lambda^6),

where H3,S5 are fixed-degree binary forms with affine coefficient lists in
`evening-h3-proportional/main-H-coefficients.txt` and
`main-S-coefficients.txt`. Their scalar is nonzero. In particular

    H3=(delta+2lambda-1)p^3
       +(3delta lambda-3delta-9lambda+3)p^2
       +(-3delta lambda^2-6delta lambda-3lambda^2+3delta+12lambda-3)p
       -delta lambda^3+3delta lambda^2-lambda^3+3delta lambda
          +5lambda^2-delta-5lambda+1.

Their original scaling is H3=-3lambda^2 H/delta and
S5=432lambda^4(F/H)/delta^3. Only the scalar being nonzero enters
the support argument.

The exact main Jbar and G factors are

    G=delta(lambda^2-4lambda+1)((lambda+1)delta+lambda-1)/(3lambda^2),
    Jbar=(lambda-1)G/2.

Hence all main Jbar=0 values outside lambda=1 have G=Jbar=0 and are already
excluded by the accepted all-power theorem. Lambda=1 is treated below.
Every other main support candidate has the actual open conditions

    delta lambda (lambda-1)(lambda^2-4lambda+1)
      ((lambda+1)delta+lambda-1) != 0.                 (A)

### 3. Both zero-cubic charts are excluded in every mate degree

Use the final evening standard-library certificate, without replaying it:
`validation/2026-10-13-h3-zero-chart-conductor-new/attempt-01-final/` and
`new-exact-support-incidence.json`. On zero-P, delta=-1, a=0, B=-2/3,G=0,
put j=Jbar. Up to nonzero scalar the complete conormal cubic is

    S3=p^3-6p^2+6p+3j.

The actual octic factors exactly as

    F=(2/9) S3 Q5,
    Q5=p^5+(j/3-13/2)p^4+(27/2)p^3
        +(-12-5j/2)p^2+(9/2-3j/2+j^2)p+9j-3j^2.

Both factors are monic, so neither has an infinity root. For j!=0 SUP
requires all Q5 roots to lie on S3. For j=0 the extra A4 point p=0 is
already a root of S3, so precisely the same necessary support condition
holds. It implies Q5 divides S3^5. Exact polynomial division gives five
remainder coefficients in Q[j]; the certificate records a literal Bezout
combination of the first two equal to 1. They have no common algebraic
zero. Thus no j satisfies SUP. The homogeneous coordinate transformation
`(P,Q,j)->(P,P-Q,-j)` takes this actual octic and conormal cubic to the
zero-J chart, retaining p=0 and target infinity. The certificate contains
both exact homogeneous transform identities. Thus the zero-J chart also
fails SUP in its entirety. No center minor is inverted.

This is a direct all-parameter consequence of the saved exact identities,
and it has passed the separate October 14 independent geometric audit.

### 4. The entire lambda=1 main boundary also fails SUP

On lambda=1, Jbar=0 and G=-4delta^2/3!=0. The conductor factors, up to its
nonzero scalar, as H3*p*Q4, where

    H3=(delta+1)p^3-6p^2+(6-6delta)p+4delta,
    Q4=(90delta^2-76delta-58)p^4
        +(-405delta^2+458delta+203)p^3
        +(675delta^2-858delta-261)p^2
        +(-450delta^2+800delta+174)p-400delta.

Since Q4(0)=-400delta!=0, the allowed additional A4 root p=0 does not
help Q4. When its leading coefficient is nonzero, SUP implies Q4 divides
H3^4. The saved compact evening remainder source records four numerator
polynomials of degree22 in delta and a literal Bezout product equal to 1;
its denominators have only `(45delta^2-38delta-29)^9` and constant factors.
They therefore give a complete contradiction on this chart.

At the leading drop `45delta^2-38delta-29=0`, the fixed-degree Q4 has an
infinity root. H3 has no infinity root there, since delta=-1 gives that
quadratic value54. The added A4 p=0 is finite. This also contradicts SUP.
Thus lambda=1 is entirely excluded, not just a rational sample or a
finite list of mate exponents. Evidence:
`evening-h3-proportional/probe_lambda1_compact.m2`, its passing attempt02,
`lambda1-compact-numerators.txt`, denominators and literal Bezout file.

### 5. A general root-support cover for the remaining main chart

The following elementary lemma replaces an unbounded exponent search.
Let H3,S5 be nonzero binary forms of degrees three and five, with
`supp(S5) subset supp(H3)`.

* If S5 has at least three distinct roots, then H3 has exactly three
  distinct roots, all occur in S5, and H3 divides S5.
* If S5 has at most two distinct roots, then either it has a root of
  multiplicity at least four, or its exact multiplicities are3+2.

Indeed the support inclusion bounds the number of S5 roots by three. In
the first case three roots force H3 to be squarefree and every root must
occur in S5. In the second, partitions of5 into at most two positive parts
are5,4+1,3+2. This lemma concerns the full actual polynomial, including
all nilpotent contact multiplicities. Its scope is independent of mate
degree and of the coefficients of the projection family.

Under (A), Jbar!=0, so SUP imposes this support inclusion. The infinity
chart cannot survive: if LC(S5)=0, the actual fixed-degree S5 has an
infinity root and SUP forces LC(H3)=delta+2lambda-1=0. Substituting
`delta=1-2lambda` gives the exact identity

    LC(S5)=-216lambda^4(2lambda-1)^3
           =216lambda^4 delta^3 != 0,

a contradiction. This new source has a successful captured run in
`generalization-quintic-h3/infinity-attempt-02`. Its first attempt had an
unneeded quotient-ring computation after the candidate ideal was already
unit; that tail interface failure is preserved.

If H3 has an infinity root while S5 has none, it has at most two finite
roots and cannot cover three distinct S5 roots. Otherwise its leading
coefficient is nonzero. The exact three coefficients of the pseudoremainder
of S5 by H3 are saved in `h-divides-s-remainder.txt`. Their common factor
lambda^2 is invertible on (A). For those original divided generators Ri,
put

    U=delta lambda (lambda-1)(lambda^2-4lambda+1)
      ((lambda+1)delta+lambda-1) LC(H3) LC(S5).

The new source constructs and verifies a literal polynomial identity

    sum_i Wi Ri = U^2.

The exact Wi are saved in `h-divides-s-witness.txt`. Thus the H3|S5 case
is empty on the declared chart. The first certificate attempt omitted
LC(S5), found no witness through exponent12 and failed its assertion;
the repaired declared-open witness has exponent2 and succeeds. No claim
is made about that omitted leading condition.

### 6. The high-multiplicity support incidence and current work

Write V for the product of the five nonconstant unit factors in (A).
For a finite root x of S5, put c_i=coefficient_(p^i) S5. A root of
multiplicity at least4 satisfies

    S5(x)=S5'(x)=S5''(x)=S5'''(x)=0.                 (B)

The new exact QQ ideal, saturated only by the units in (A) and c5,
returns the unit ideal. Its source, literal four input polynomials and
captured intermediate ideal are preserved in the new validation package.
The original-generator witness is now complete: for the literal four
generators M4 and the stated unit V*c5, the saved 22 MB vector W4
satisfies `M4 W4=(V*c5)^2`. The source asserts that exact product before
saving it; its completion marker and empty stderr are preserved. The
October 14 independent auditor accepts this arithmetic lineage without
re-expanding the same large product.

For the exact3+2 case choose x to be the triple root. Dividing by
`(p-x)^3` leaves

    c5 p^2+(c4+3x c5)p+(c3+3x c4+6x^2 c5).

Its discriminant is

    c4^2-4c3c5-6x c4c5-15x^2 c5^2.                 (C)

Thus all3+2 cases, including coalescence into a fifth root, lie in the
exact finite polynomial system S5(x)=S5'(x)=S5''(x)=0,(C)=0.
For SUP additionally H3(x)=H3(y)=0, where
`y=-(c4+3x c5)/(2c5)`. The second relation is imposed after multiplying
by `(2c5)^3`, so no undefined root or scalar is introduced. The stronger six-generator full-support incidence has completed with
saturated ideal1. The original six-generator witness is being extracted
in `support32-witness-attempt-01`; complete main-family closure is
withheld until its literal product and captured execution are available.
The earlier unrestricted multiplicity32 computation supplies no claim
and is not needed for this support cover.

The first direct H3^5 modulo S5 source produced exact large coefficients
but was interrupted during ideal processing. A later full Hermite-rank
approach was also interrupted in favor of this much smaller complete root-
multiplicity cover. Those sources, failed setup interfaces and outputs
remain recorded. Neither unfinished computation supplies a theorem.

### 7. Remaining nonendpoint lanes and next action

The companion new note `2026-10-13-generalization-quintic-l2.md` proves
an all-parameter exclusion of the regular sole homogeneous-root lane,
including L2, its discriminant-zero and coefficient-drop boundaries. Its
October 14 independent audit has accepted this explicitly scoped theorem. The quotient/conductor proof and all new
higher Taylor conditions are retained there; no accepted old check is
replayed.

Even if the complete h3 support cover closes, the following remain outside
it: homogeneous gcd degree2 with its full two-root or repeated-root support;
the gcd-degree-one singular target-fiber charts pZ=0 with their denominator-free original
fiber system; other Jbar=0 nonproportional families; actual conductor power
descent on surviving full-support parameters; all other quintic genera;
normal quintics, higher carriers and entirely thick presentations.

The continuation strategy is to exhaust complete support types for the
fixed-degree actual conductor section, then impose full conductor descent.
Its complexity depends on normalization geometry and conductor root
support, not on an unbounded list of mate degrees. A first-symbol root
alone is never treated as a bound on the full conductor multiplicity.


---

<a id="source-2026-10-13-generalization-ribbon-numerical-criterionmd"></a>

## A degree-free symbolic-ribbon and valuation criterion

Date: 2026-10-13. Author: `ribbon_general`, delegated by
`global_structure`. Status: **NEW WRITTEN PROOF / INDEPENDENT REVIEW
PENDING**, as a conditional general theorem. Accepted quartic computations are used as inputs, with no
reruns. This note does not claim a solution of either the fixed `C0`
question or the universal STCI question.

The accepted
[weighted-ribbon proof](GENUS_TWO_BISECTION_PROOF.md)
uses an actual Cartier double on the normalization of a quartic. The
construction below supplies a canonical *symbolic* double even when
`2c` is not Cartier. Its numerical degree is controlled by all symbolic
layers of any actual Cartier multiple. This separates the global
existence of the ribbon from the stronger assertion that its degree can
be read directly from a Cartier-double Euler sequence.

### 1. Hypotheses and notation

Let `k` be an algebraically closed field of arbitrary characteristic.
Let `C subset P3` be a smooth integral projective curve of degree `d`
and genus `g`. Let `S` be a normal integral projective surface with a
finite birational morphism `f` onto an integral surface in `P3`, as
for a normalization of a carrier. Let `c subset S` be a reduced prime curve such
that `f|c:c->C` is an isomorphism. Set

    H=f*O_P3(1),   a=H^2>0,   H.c=d.

Assume there is an actual effective Cartier relation

    r c ~ b H,   r,b positive integers.

Here `r c` means the divisor with that Weil divisor and its divisorial
ideal; the assumption includes Cartierness and actual linear
equivalence. It is stronger than a numerical equivalence. Intersecting
with `H` gives

    r d = b a.

A normalization of an integral carrier with a mate supported exactly
over `C` supplies this relation when there is exactly one inverse prime
and it maps birationally to `C`. Because the normalization is finite,
the latter prime then maps isomorphically to the normal curve `C`.
The absence of extra inverse points is an upstream support condition,
not a conclusion of the present proof.

Let `pi` be the arithmetic genus of a general effective Cartier
member of `|H|`. In the characteristic-zero carrier applications this
is the genus of the smooth general pulled-back hyperplane. Define

    kappa = K_S.H = 2 pi - 2 - a.

No Gorenstein assumption on `S` is needed. The intersection `K_S.H`
is defined using the Cartier divisor `H`; alternatively the right side
can be taken as the definition of `kappa`. The general member avoids
the isolated singularities of the normal surface. Using arithmetic
genus here avoids imposing a positive-characteristic smoothness
assertion on the pulled-back hyperplane linear system.

For each `i>=0` define the reflexive divisorial ideal and its layer

    I_i = O_S(-i c),    E_i = I_i/I_(i+1).

Thus `I_0=O_S` and `E_0=O_c`. Write `ell=deg E_1`.

### 2. The symbolic double is always an entire ribbon

**Lemma.** Under the normality and smoothness hypotheses above,

    R_2 = Spec_S(O_S/I_2)

is a Cohen--Macaulay ribbon on the entire smooth curve `c`, including
every singular point of `S`. Its nilideal is the line bundle `E_1`.
More generally, every `E_i` is a line bundle on `c`.

**Proof.** A divisorial rank-one reflexive sheaf on a normal surface
has depth two at each closed point. The exact sequences

    0 -> I_j -> O_S -> O_S/I_j -> 0,
    0 -> I_(i+1) -> I_i -> E_i -> 0

and the depth lemma therefore give depth at least one to the two
quotients at closed points of their one-dimensional support. Thus
they have no finite-length torsion.

Normality identifies `I_1` with the ideal of the reduced curve `c`:
locally, functions in this ideal are exactly regular functions having
positive valuation at the height-one prime of `c`. Divisorial
valuation inequalities also give

    I_i I_j subset I_(i+j).

In particular `I_1` annihilates `E_i`, so `E_i` is a coherent
`O_c`-module. At the generic point of `c`, the local surface ring is a
DVR; `E_i` has rank one over its residue field. The depth statement
shows it is torsion-free on `c`. A torsion-free rank-one coherent
sheaf on a smooth curve is a line bundle.

The radical of `I_2` is `I_1`, and `I_1^2 subset I_2`. Hence the
nilideal of `O_S/I_2` is exactly `E_1`, its square is zero, and

    0 -> E_1 -> O_R2 -> O_c -> 0

is the ribbon sequence. This proof requires neither `2c` Cartier nor
`S` Gorenstein. QED.

Ordinary ideal squares and ordinary nilradical powers must not replace
the divisorial ideals in this lemma. Their quotients can acquire
finite-support torsion; the reflexive/symbolic construction is what
proves the asserted global Cohen--Macaulay and line-bundle properties.

### 3. Multiplication defects and periodicity

Multiplication induces nonzero, hence injective, maps of line bundles

    E_i tensor E_j -> E_(i+j).

They are isomorphisms at the generic point of `c`. Consequently there
are effective divisors `D_i` on `c` with

    E_i = E_1^i(D_i),    D_0=D_1=0,
    D_i+D_j <= D_(i+j).

All divisor inequalities are coefficientwise. This is symbolic
filtration data, not a proof of primitivity or a determination of
higher normal jets.

Since `r c` is Cartier, the divisorial ideals have actual periodicity

    I_(i+r)=I_i tensor O_S(-r c),
    E_(i+r)=E_i tensor O_c(-bH).

In particular

    E_r=O_c(-bH),    deg E_r=-b d=-r d^2/a.

Applying multiplication to `E_1^r -> E_r` yields the first bound

    ell <= -d^2/a.                                      (1)

More generally, for every positive integer `j`, choose a positive
integer `n` with `r | n j`. The multiplication map
`E_j^n -> E_(nj)`, together with periodicity, gives

    deg E_j <= -j d^2/a.                                (2)

These are inequalities of rational numbers; the left sides are
integers. They do not require generic immersion into `P3`.

### 4. The Euler polynomial gives a sharper first-layer bound

For a normal surface in the carrier setting,

    chi(O_S(mH)) = (a/2)m^2 - (kappa/2)m + chi(O_S).

One can obtain this formula without using a singular-surface
Riemann--Roch correction theorem. The hyperplane exact sequence and
the degree/Euler formula for line bundles on the general Cartier
hyperplane curve give, for every integer
`m`,

    chi(O_S(mH))-chi(O_S((m-1)H)) = ma+1-pi.

The stated polynomial is the unique solution with its given value at
`m=0`.

Set `R_r=Spec_S(O_S/I_r)`. Since `I_r=O_S(-bH)`, its Euler sequence
gives

    chi(O_Rr) = chi(O_S)-chi(O_S(-bH))
               = -(a b^2+b kappa)/2.

Thus the constant `chi(O_S)` cancels. Rationality of the surface, a
prescribed value of its Euler characteristic, and invertibility of
its dualizing sheaf are unnecessary for this numerical step.

Its symbolic filtration has successive quotients `E_0,...,E_(r-1)`.
Riemann--Roch on `c` therefore gives the exact identity

    sum_(i=0)^(r-1) deg E_i
       = -(a b^2+b kappa)/2 - r(1-g).                    (3)

Using `deg E_i >= i ell`, for `r>=2` we obtain

    ell <= -[a b^2+b kappa+2r(1-g)]/[r(r-1)]
         = -[r d^2/a+d kappa/a+2(1-g)]/(r-1).            (4)

Equivalently,

    r(r-1)ell + 2 sum_i deg D_i
       = -a b^2-b kappa-2r(1-g).

When `r=2`, there are only `E_0` and `E_1`, so (4) is an equality:

    ell = -(a b^2+b kappa)/2 - 2(1-g).                  (5)

For `r>2`, (4) need not be an equality. The total Euler characteristic
does not determine the double-ribbon degree without controlling the
multiplication defects. This is precisely where copying a quartic
Cartier-double calculation to an arbitrary Cartier multiple would
lose information.

### 5. The ambient conormal lower bound

Assume first that `f` is an immersion at the generic point of the
symbolic ribbon `R_2`. A sufficient carrier condition is that the
normalization is an isomorphism at the generic point of `C` and the
carrier is regular there. Pullback of the ambient ideal induces

    N_C/P3^* = I_C/I_C^2 -> E_1.

It is generically nonzero: in the sufficient carrier condition it is
even generically surjective, since the ambient ideal generates the
curve ideal in the DVR of the regular carrier. Global immersion of
`R_2`, including along the conductor, is not required.

Let `M` be any upper bound on the degree of a line subbundle of
`N_C/P3`. A nonzero map `N_C^* -> E_1` dualizes to a generically
injective map `E_1^(-1) -> N_C`. Saturation can only increase the
degree of its image, so

    ell >= -M.                                        (6)

For `C=P1` and

    N_C/P3 = O(u) direct_sum O(v),

one can take the exact bound `M=max(u,v)`. For a semistable normal
bundle on a curve of genus `g`, one can take
`M=deg(N_C)/2=2d+g-1`; this bound does not assert semistability.

Combining (1), (4), and (6) gives the degree-free necessary conditions

    d^2 <= a M,

    a b^2+b kappa+2r(1-g) <= r(r-1)M,                  (7)

or, after eliminating `b`,

    r[d^2-aM]+d kappa+a[2(1-g)+M] <= 0.                (8)

Violation of either condition excludes a mate satisfying the stated
normalization, support, and generic-immersion hypotheses.

### 6. Balanced rational curves: a uniform theorem

Suppose `C=P1` and its accepted or separately established normal
splitting is balanced:

    N_C/P3=O(2d-1)^2.

Then every relation above with generic immersion satisfies

    d^2 <= a(2d-1),

    r[d^2-a(2d-1)]+2d(pi-1)+a(d+1) <= 0.              (9)

For equal curve and carrier degrees, `a=d` and `b=r`. Condition (9)
simplifies to

    2 pi <= (r-1)(d-1).                               (10)

In particular, an actual Cartier double `2c~2H` has

    E_1=O_P1(-d-2pi),

and is incompatible with the embedding whenever `2pi>d-1`. This is
a single theorem for every degree `d`, rather than a list of degree
pairs. The accepted quartic bisection input has `d=a=4`, `r=b=2`,
`pi=2`; the theorem gives `E_1=O(-8)` and contradicts the accepted
`N_C0=O(7)^2`. No part of that accepted calculation was rerun here.

For comparison, the accepted quintic genus-one normalization has
`a=5,d=4,r=5,b=4,pi=1`. Bound (4) gives `ell<=-7/2`, hence
`ell<=-4`, while the conormal lower bound is `ell>=-7`. Thus this
general theorem alone does not exclude that remaining quintic lane.
The existence of its symbolic double is proved, but its degree is
not forced to be the prohibited quartic degree `-8`.

### 7. A valuation extension for thick singleton carriers

Generic immersion is exactly the assertion that the first ambient
normal direction survives on `R_2`. There is a useful weaker
version when that direction is killed.

Let `q>=1` be the minimum valuation at the generic point of `c` of
the pulled-back ambient ideal `I_C`. Assume `f|c` remains the given
isomorphism. The pulled-back ideal is globally contained in `I_q`
by the defining divisorial valuation condition. Its square is
contained in `I_(2q) subset I_(q+1)`. Since `I_1` annihilates `E_q`,
pullback therefore defines a global map

    N_C/P3^* -> E_q.

This map is generically nonzero by the definition of `q`. Saturating
its dual gives `deg E_q>=-M`, while (2) gives
`deg E_q<=-q d^2/a`. Hence

    q d^2 <= a M.                                    (11)

For balanced rational curves this is

    q d^2 <= a(2d-1).

It applies to thick singleton normalizations without asserting a
nonzero first-ribbon conormal map. In that setting the Euler
first-layer bound (4) still holds algebraically, but cannot be
combined with (6) unless `q=1`. Multiple inverse branches, inverse
curves mapping with degree greater than one, and non-smooth inverse
curves require a different formulation and are outside this theorem.
Condition (11) is necessary under the stated hypotheses; it does not
prove either singleton inverse support or the isomorphism `c~=C`.

### 8. Preserved limits and next structural use

The symbolic-ribbon construction removes the need for an actual
Cartier double. It does not create a Cartier relation that was not
already supplied by a mate, nor determine its least possible index.
Replacing `(r,b)` by `(nr,nb)` is always permitted and preserves the
relation, but need not preserve sharpness of the Euler bound. More
precisely, put `A=d^2/a` and `B0=d kappa/a+2(1-g)`. The right side
of (4) is `-A-(A+B0)/(r-1)`, so increasing `r` weakens that bound
when `A+B0>=0` and strengthens it when `A+B0<0`. For `a=d`,
`A+B0=2(pi-g)`. In the weakening case one should use the smallest
available actual relation, not infer a new small-index relation.

The most useful structural continuation is to prove a uniform
upper bound on the relevant Cartier index or to control the
effective multiplication defects `D_i` by surface singularities and
conductor descent. That would strengthen (4) without restarting a
degree-pair enumeration. The inequalities themselves do not exclude
all large carrier degrees, and there is no unrestricted non-STCI
conclusion here.


---

<a id="source-2026-10-13-generalization-smooth-normalization-independent-auditmd"></a>

## Independent audit of the all-degree smooth-normalization classification

Date: 2026-10-14, America/New_York. Auditor: `frontier_reconcile`.
Status: **PASS FOR THE NEW THEOREM UNDER ITS EXPLICIT SINGLETON-LIFT AND
SMOOTH-NORMALIZATION HYPOTHESES**. This audit reviews the new derivation;
accepted quartic, conductor and fixed-C0 premises were not rerun. The theorem
does not imply that an arbitrary minimum carrier has these hypotheses.

Owner source read:
[degree-free carrier framework](FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md),
SHA-256 `38bff3c497b1c0f8310a623e36c0fd5d6ded0517fc6903115b4321f5672d5848`.
The acceptance here is for section 3 and the finite fixed-C0 classification
in section 4. The later power-compression consequences have their separate
new-theorem dependency and are not established by this audit.

### 1. The exact accepted theorem

Let `C subset P3` be a smooth rational curve of degree `d` over an
algebraically closed field of characteristic zero. Let `X` be an integral
degree-`a` hypersurface admitting an actual mate for C, with finite
normalization `nu:S->X`. Require:

    S smooth,
    (nu^-1(C))_red=c,
    nu|c:c->C an isomorphism.

Put `H=nu*O_X(1)`. Then `(S,c)` is a smooth surface of minimal degree
with c its complete hyperplane class. The possibilities are exactly:

| Surface and c | H | a |
|---|---|---|
| P2 and a line | `d h` | `d^2` |
| P2 and a smooth conic | `(d/2) h`, requiring d even | `d^2/4` |
| Smooth rational normal scroll of degree n>=2 | `(d/n)c`, requiring n to divide d | `d^2/n` |

The scroll can be written `F_e`, `c=E+t f`, with `E^2=-e`,
`t>e>=0` and `n=2t-e`. These are finitely many normalization/polarization
types for a fixed d. The conclusion is necessary; it neither constructs
the four-coordinate projection nor proves support or conductor descent.

### 2. Independent reconstruction of the proof

The pullback of a degree-b mate is a nonzero section of `O_S(bH)`.
Its complete zero support is c by the stated singleton inverse-image
condition. On the smooth surface its actual divisor is `m c` for a
positive integer m. Since H.c=d and H^2=a, intersecting yields

    m d=a b,
    c_num=(d/a)H,
    n=c^2=d^2/a.

There is no hypothesis that the downstairs C is Cartier on X. Smoothness
of S makes c Cartier upstairs, so n is an integer. It is positive and
c is ample by numerical equivalence with the positive multiple of ample
H. This is the first place the smooth-normalization hypothesis is essential.

Adjunction on the smooth rational c gives `K_S.c=-n-2`. Thus `K_S.H<0`.
An effective positive canonical multiple would have nonnegative
intersection with ample H, so no such multiple is effective. The standard
characteristic-zero surface classification used in the accepted repository
arguments therefore makes S rational or birationally ruled over a
positive-genus curve.

The second alternative is impossible. A smooth ruled minimal model over
the positive-genus base is reached by point contractions, and the ruling
pulls back to a morphism on S. The rational c maps constantly to the base.
Write the fiber containing it as `F=m0*c+sum mi*Di`. Then

    0=F.c=m0*c^2+sum mi*(Di.c).

Every other component has nonnegative intersection with c on the smooth
surface, and m0 is positive. This contradicts c^2>0, including a reducible
or nonreduced fiber. Hence S is rational and `H1(S,O_S)=0`.

Now use the actual Cartier-curve sequence

    0 -> O_S -> O_S(c) -> O_c(c)=O_P1(n) -> 0.

It yields `h0(O_S(c))=n+2` and surjectivity onto all n+1 sections on c.
The canonical section of O_S(c) is nonzero at each point outside c.
At each point of c, some lifted section is nonzero because O_P1(n)
is globally generated. Consequently the complete system |c| is basepoint
free everywhere, not only generically.

Its morphism `phi:S->P^(n+1)` is finite: a positive-dimensional fiber
would contain a curve D with `c.D=0`, contradicting ampleness. The image
Y is an integral nondegenerate surface. Nondegeneracy follows from using
a basis of the complete linear system. If e is the generic map degree,
the intersection-degree formula and the minimal-degree inequality give

    n=c^2=e*deg(Y),
    deg(Y)>=codim(Y)+1=(n+1-2)+1=n.

Thus e=1 and deg(Y)=n. This includes n=1: then the map is finite
birational onto P2; no scroll-only assumption loses that case.

The degree inequality and Del Pezzo--Bertini classification were inspected
in the primary author source [Eisenbud--Green--Hulek--Popescu, *Small Schemes
and Varieties of Minimal Degree*, introduction](https://arxiv.org/html/math/0404517v5).
For integral surfaces, its list is a plane, an integral quadric/rational
normal scroll, or a Veronese surface. These standard surfaces are normal,
including the singular rational normal cones. Therefore the finite
birational map to Y is an isomorphism: on affine opens, the finite integral
algebra inside the common function field equals the integrally closed
target ring. Smoothness of S eliminates singular cones. The complete
polarized classification follows.

On each resulting rational surface numerical equivalence and linear
equivalence agree. For `P2`, c is h or 2h, so H is respectively d h or
(d/2)h; the latter requires d even. On a scroll `Pic(F_e)=ZE+Zf` and
c has E coefficient one. Therefore the rational equality
`H=(d/n)c` forces `d/n` to be an integer. Squaring gives the carrier
degrees in the table. The necessary divisibility n|d gives a uniform
finite list of smooth normalization types at once, rather than a separate
degree-pair search.

### 3. Every fixed-C0 case in the finite list

For d=4, the line model gives a=16. The conic model gives a=4. Smooth
scroll degree n must divide four and satisfy n>=2, so n=2 or n=4:

* n=2 gives a=8. In `n=2t-e` with `t>e>=0`, the only possibility is
  `e=0,t=1`, hence `S=P1xP1`, `c=(1,1)`, `H=(2,2)`.
* n=4 gives a=4. The scroll models are `e=0,t=2` or `e=2,t=3`;
  together with the plane conic, these fall in the already accepted
  all-integral-quartic exclusion. No new check of that theorem is needed.

Thus the only remaining smooth-normalization singleton-lift candidates
for the literal fixed C0 are

    a=8:  (S,c,H)=(P1xP1,(1,1),(2,2)),
    a=16: (S,c,H)=(P2,line,4h).

Their sectional genera are one and three, obtained directly by adjunction
on H. Their complete H systems have dimensions nine and fifteen.
Those dimensions describe parameter spaces for projections, not an
exhaustion of projection centers. Actual finite birational projection,
the prescribed deleted-middle-monomial restriction to c, full inverse
support and every conductor layer remain active conditions.

### 4. Scope audit and retained limitations

The proof needs neither generic regularity of X along C nor a smooth
mate once the full singleton isomorphic lift is explicitly assumed.
Conversely, the theorem does not provide that lift for a general
generically nonregular carrier. Several primes above C and degree-greater-
than-one lifts have a coefficient-vector divisor relation and are outside
this scalar argument.

A singular normalization cannot simply be substituted into the audited
proof. There c may not be Cartier, its self-intersection may be rational,
and the Cartier-curve exact sequence can fail. A proposed extension to
normal S with smooth Cartier c would be a new theorem requiring its own
precise statement, cone/Picard analysis and review. It is not implicitly
accepted here.

The global existence of high-degree smooth surfaces through C does not
yield mates on those surfaces. Nor does choosing a minimum mate-admitting
carrier force smooth normalization. Entirely thick pairs can remain
singular under `G+F*T`. The remaining normalization and filtered-algebra
branches cannot be discarded by this result.

For the two fixed-C0 models, `H=2c` or `H=4c` supplies a primitive
normalized degree-one section, but an upstairs section is still not an
ambient mate. The separate conductor-power theorem may compress it
under its single-field/unit hypotheses. This audit accepts neither a
geometric residue-degree bound for every projection nor the exclusion of
split conductor phases. No unconditional degree-eight or degree-sixteen
carrier exclusion follows.

### 5. Optional proof simplification, not needed for acceptance

One can obtain `H1(O_S)=0` before surface classification. Every morphism
from the rational c to an abelian variety is constant. If the Albanese
morphism of S had positive-dimensional image, pulling back a suitable
ample divisor on that image would give a nonzero effective divisor D
with `c.D=0`, since c is contracted. Ampleness of c contradicts this.
Thus the Albanese variety is trivial; in characteristic zero this gives
`H1(O_S)=0`. The complete-|c| proof then establishes rationality from
the minimal-degree classification itself.

This alternative explains the same geometric rigidity: an ample rational
curve forbids irregularity. It is supplied as an optional simplification;
the audited owner proof already establishes the necessary vanishing by
the standard surface-classification route.

### 6. Evidence and review boundaries

This is a written independent mathematical reconstruction, including
ampleness, reducible fiber signs, n=1 and n=2 cases, finite-map degree,
normality/isomorphism, all Picard divisibilities and the complete fixed-C0
list. There was no symbolic execution and no inherited verifier rerun.
The live primary check was restricted to the new minimal-degree interface.
Parallel agreement is not used as a proof: the argument above supplies the
reviewed implications.

The all-quartic theorem and the normal-bundle/conductor results retain
their earlier audit provenance. No novelty or universal resolution is
claimed. The mathematical advance accepted here is a finite
normalization-type classification for an entire explicitly stated rational
support lane across all carrier and mate degrees.


---

