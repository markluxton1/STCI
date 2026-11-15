# Normalization, conductor descent, and projection geometry

For the fixed embedded characteristic-zero quartic, a proposed normalization model, an actual projection, and a descending hypersurface section are three different objects. This account separates their tests and the related quintic and conditional sextic applications. The [cataloged Results](../CATALOG.md) and their proofs retain the exact theorem and review scopes.

## Fixed-carrier existence and the shared descent mechanism

Let X be an integral Cohen–Macaulay projective surface, nu:S→X its finite normalization, L ample, and H=nu*L. Use the **entire** reduced inverse support W of C. Isolated points outside its curve components already forbid a mate. Otherwise, with W=⋃Gamma_i, the class relations form

    Lambda=ker[Z^(s+1)→Cl\(S\)], (n_i,b)↦Σn_i[Gamma_i]-b[H].

The [full proof of R-0003](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md#4-an-exact-fixed-carrier-criterion-including-thick-support) associates to each relation its actual unit class at every generic conductor curve away from C. A mate exists exactly when a relation with every n_i>0 has torsion full-conductor class. Positivity enters the conductor over C after a sufficiently large power; purity of nu_*O_S/O_X extends **full** generic membership globally. An ambient hypersurface equation then lifts from the hypersurface sequence. This works in arbitrary characteristic and does not assume that reduced C defines an APic class in a generically singular carrier.

The [local algebra](../supplements/CONDUCTOR_DESCENT_ALGEBRA.md) proves the underlying mechanism and its limitations. Membership is in the fiber-product conductor ring, not merely a tensor equalizer. In characteristic zero, nilpotent logarithmic defects must vanish; the reduced phase can then have finite order. If each reduced upstairs algebra is a single field, its extension degree bounds a sufficient exponent. Split phases such as (1,zeta) have unbounded least orders even with two branches. A nonunit can behave differently; powers of t on a cusp enter its conductor. None of these statements computes an actual phase image.

The relation cone offers both obstruction and construction. Its Hilbert basis has a full-support member sum exactly when the union of basis supports covers all inverse curves; an individual basis member can miss branches. Products from distinct global divisor directions can cancel opposite logarithmic defects, whereas powers along one fixed divisor ray cannot. See [the constructive cone application](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md#constructive-use-of-the-descent-lattice).

## Necessary Cartier singleton models and actual projection tests

The [complete proof of R-0002](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md#cartier-singleton-models-the-complete-proof) assumes an **actual mate**, full singleton inverse support c≅C, and Cartier c on normal S. Smooth Cartier c forces S regular along c; the mate makes c ample. Surface classification, adjunction and the Cartier restriction sequence make |c| a minimal-degree embedding. For rational C of degree d, c²=d²/deg X; the possibilities are plane, smooth scroll, or rational-normal cone models with the integral polarizations in R-0002.

For the fixed quartic, after [R-0001](../results/quartic_carrier_exclusion.md), the higher-degree necessary models are

| Carrier degree | S | c and H |
| --- | --- | --- |
| 8 | smooth quadric | c=(1,1), H=(2,2) |
| 8 | quadric cone | smooth Cartier hyperplane conic c, H=2c |
| 16 | plane | line c, H=O(4) |

A listed model is not an actual carrier or a mate. Four sections must define a basepoint-free finite birational map to an integral hypersurface, have **full** inverse support c without isolated extras, and pass full conductor descent. Non-Cartier, multiple, and nonisomorphic inverse lifts are outside this classification.

The [explicit projection proofs](carrier_conductor_differential_comparison.md#projection-support-and-differential-obstructions) expose different failures. The plane map [s⁴:s³t:st³+z⁴:t⁴+s³z] is an actual finite degree-sixteen normalization with full inverse support z=0, but every positive mate degree is excluded by a polynomial derivative identity. The general two-fixed-coordinate sublane has the same obstruction. Its generic conductor residue is already trivial, while a nonzero first nilpotent jet survives every power. By contrast, the two actual smooth-quadric families have isolated inverse points, so fail before unit descent. The corrected quadric audit retains seven forced endpoint extras in the kappa family and the exact four-or-five extra points in the companion family. Neither argument exhausts the complete projection space.

The [twisted-cubic corrected-square benchmark](square_descent_and_singular_gluing.md#torsion-constructions-and-the-limits-of-pinching) shows that characteristic-zero singular-carrier torsion can produce an actual homogeneous pair for a different curve. The abstract nodal pinching counterexample shows why local phase torsion alone can destroy the marked full-support requirement. These constructive and negative controls explain the missing geometry rather than presuming nonexistence for the quartic.

## Projection phases, effective scope, and geometric scaling

[R-0004](../results/projection_phase_reduction.md) works in a specified finite-type family of admissible Cartier-singleton projections. After stratification and a finite cover, full conductor descent is a torus torsion-phase test. Its proof keeps nilpotent equations, generic conductor components and excluded specialization boundaries. The actual phase images of the three quartic models remain uncomputed. Their on-C thresholds are 5,5,13; with phase order E, every positive multiple of E at least the relevant threshold is a mate degree, with any additional degrees confined to smaller multiples.

The [torsion and rational-phase proofs](../supplements/PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md) distinguish a finite torsion-coset envelope from a constructible mate locus. For an explicitly presented rational constructible phase image W=⋃(Y_i−B_i), the effective method partitions supports into vanishing blocks, applies Mann's ratio bound P\(S\)=∏_{prime≤S}prime, and solves binomial systems by Smith normal form. With maximal translated support degree d and support size S in dimension D, isolated torsion orders are at most P\(S\)d^D; this is a bound, not a divisibility assertion. A common annihilating exponent may use P\(S\)lcm(1,...,d^D). Each coset must still be tested against the removed boundaries B_i. Positive-dimensional retained torsion cosets have unbounded orders. The [raw-input corollary](../supplements/PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md#from-explicit-projection-input-to-a-decision-procedure) first constructs actual admissible conductor/phase data; its termination theorem is not an executed fixed-model calculation.


## Five-coordinate geometry of the phase

For an admissible fixed-\(C_0\) Cartier-singleton projection \(S\to X\subset\mathbf P^3\), adjoining the primitive section \(Q\) to the four projection sections gives a finite image \(Y\subset\mathbf P^4\), with coordinates \([U_0:U_1:U_2:U_3:Q]\). Projection from the last-coordinate point is finite birational onto \(X\). The hyperplane \(Q=0\) pulls back to \(2c\) or \(4c\) in the three normalized models and has reduced support \(C_0\).

For \(\zeta\in k^\times\), let \(T_\zeta\) scale only the fifth coordinate. If two conductor branches have identical \(U_i\) coordinates and primitive-section ratio \(\zeta\), their images lie in \(Y\cap T_\zeta\(Y\)\). A descending mate power requires the relevant constant ratios to be roots of unity **and** requires full nilpotent conductor descent. This is a geometric reformulation of the phase obstruction, not an exclusion. The hyperplane curve \(Q=0\) is common to these intersections for every \(\zeta\); a naive intersection-degree argument must first remove this forced component before counting additional branch curves. The fixed-degree affine split-conductor example below shows why phase orders cannot be bounded from finite presentation or smooth singleton inverse support alone. Any useful global bound must invoke the actual projective polarization, contact divisor, or differential/conductor budget. [Original five-coordinate formulation](#consolidated-historical-supplement-researchsupplementsprojection_conductor_contact_and_phasemd).


## Actual projection coefficient spaces

For the three primitive Cartier singleton models (smooth quadric, quadric cone, plane), the restriction kernels of the full section spaces to the fixed quartic have dimensions 4, 4, 10. Choosing lifts of the four fixed coordinate sections is an affine graph space of dimensions **16, 16, 40**, respectively, before equivalences. Basepoint freeness gives finiteness by ampleness, but birationality and **full inverse support** are additional conditions. For the graded section ring (B=\bigoplus_{b\ge0}H^0(S,bH)) and the four-section subring \(R\), the primitive ray section \(Q\) has a degree-\(b\) mate precisely when \(Q^b\in R_b\), with the prescribed normalization/support hypotheses. Source: [current proof](#consolidated-historical-supplement-researchsupplementsprojection_conductor_contact_and_phasemd).


## Fixed-degree affine control with unbounded phase

Let \(B=k[u,v]\), \(\lambda=\alpha+\beta\), \(\mu=\alpha\beta\), \(y=v^2-\lambda uv\), (h=y+\mu u^2=\(v-\alpha u\)\(v-\beta u\)), \(z=vh\), and \(A=k[u,y,z]=k[u,y]\oplus h k[u,y]v\). The carrier relation is \(z^2-\lambda uhz-yh^2=0\); the **entire conductor** is (hB). The quotients are \(A/hB=k[u]\) and (B/hB=k[u,v]/(\(v-\alpha u\)\(v-\beta u\))). For \(Q=v^q\), \(Q^n\in A\) exactly when \(\alpha^{qn}=\beta^{qn}\). Choosing \(\alpha/\beta\) of order \(N\) coprime to \(q\) forces least descent exponent \(N\). The inverse support of the indicated affine downstairs line is the smooth line \(v=0\). This disproves any algebra-only universal bound on phase order, **not** a projective fixed-\(C_0\) bound. Same source.


## Opposite-ruling pairing and the sparse-family boundary

On the smooth quadric with diagonal \(c\), the specified pairing ((x,0)\leftrightarrow(0,ax)), \(a\ne0,-1\), forces phase (a^{-2}) and permits the **full form within this pairing**
\[
U(x,y)=W_0+\frac{ax+y}{a+1}W_1+
(a^2x^2+y^2-(a^2+1)xy)D+
xy\bigl(xE+y(W_2-E)\bigr)+x^2y^2W_3,
\]
where \(D,E\in k^4\) are arbitrary. The sparse choice \(D=W_2,E=uW_2\) is finite but has extra inverse points mapping to ([0:0:0:1]): (\(\infty,-a^2/u\)) when \(u\ne0\), and ((-1/(1-u),\infty)) when \(u\ne1\). The boundary coefficient pairs of the full form are (a^2D+yE+y^2W_3) and (D+x(W_2-E)+x^2W_3), which can avoid these particular sparse-family defects. Thus only the **sparse family** is excluded. Sources: [current proof](carrier_conductor_differential_comparison.md#the-opposite-ruling-pairing-and-its-complete-coefficient-freedom), [current proof](spectral_pushforward_powers.md#2026-10-14-quadric-opposite-ruling-phase-family-failure).


## Divisor-lattice failure and additive conductor failure

The imported Space Curves III examples illustrate distinct obstructions within the fixed-carrier criterion, and should not be conflated.

* Cuspidal cubic: on the carrier y^3-x^2 z=0, the necessary divisor proportionality holds on normalization, but the nonreduced conductor quotient has a nonzero additive polar term -3 z^(-2). This prevents descent of every positive power in characteristic zero. The symbolic companion checks an explicit Cartier identity and a conductor restriction, but does not independently prove the global conductor identification.
* Ruled cubic: on x z^2-y^2 w=0, local pinch-point torsion is compatible with descent of a power, but normalization classes H=(2,1) and lifted C=(2,0) are not positively proportional. Here the obstruction is already in the normalization divisor lattice, not in the local conductor unit group.

These are historical examples, not new exclusions of unaddressed carrier degrees. Source: research/archive/space-curves-2026-10-19/README.md, section 4, and its linked Space Curves III artifacts and symbolic companion. The imported status is historical/source-reviewed, with its stated review scope.


## A rank-two scroll conductor: three distinct algebras

The October 8 adversarial source proves a conditional result for an integral quartic carrier normalized by a smooth rational quartic scroll, generically regular along C0. If the actual conductor center is a smooth twisted cubic Gamma and its upstairs conductor D maps finite flat of rank two to Gamma, there is no mate in any degree. Crucially D need not be reduced.

Finite duality gives the actual upstairs conductor divisor D linearly equivalent to -K_S. The rank-two algebra on Gamma=P1 splits by trace as O + O(-2) eta, with eta^2=Delta, Delta a quartic section. The proof separates:

* Integral reduced D: invariance of a descending power forces the square of the upstairs primitive section to descend. This produces a quadric cutting C0 on the quartic carrier, contradicting the unique smooth quadric's bidegree (1,3) against the carrier intersection class (4,4).
* Reducible reduced D: Delta=q2^2. The two branches glue modulo q2, including tangencies. Their section restrictions differ by a root of unity. Nontrivial phase forces simultaneous branch contact exceeding their mutual intersection multiplicity, impossible for a third smooth branch by a local Taylor expansion.
* Nonreduced D: Delta=0, eta^2=0. If f=a+b eta, descent of f^n forces n a^(n-1)b=0; characteristic zero and a nonzero force b=0, so f itself descends, producing an impossible hyperplane.

The source also proves that assuming the *entire nonnormal support* is a smooth twisted cubic suffices to recover the conductor hypotheses: the actual conductor center has Hilbert polynomial 3m+1, is pure Cohen-Macaulay and therefore reduced on its smooth degree-three support; upstairs D is finite flat of rank two by torsion-freeness over Gamma and H.D=6. A further applicability argument proves every integral quartic singular along a smooth twisted cubic has this scroll normalization: the space of quartics singular along the cubic is the six-dimensional span of products of its three quadratic generators, and integrality gives a smooth conic in the associated quadratic-map target. The incidence blowup identifies its normalization as a smooth quartic scroll. The source reports independent exact symbolic checks of the derivative matrix and rank. These statements remain scoped to a smooth twisted-cubic singular support; singular or reducible degenerations are not covered. Moreover quartic carriers are already excluded for C0 by R-0001, so this is valuable mechanism and geometry rather than a newly open quartic case.

Source: [current proof](../supplements/QUARTIC_SCROLL_REDUCED_CONDUCTORS.md) and its cited applicability and computation companions. The argument is retained without generalizing its rank-two conductor hypotheses to arbitrary scroll projections.


## Nonreduced ramification is not determined by full support

The exact local model X: X^2+Y^2(Y+Z^2)=0 has normalization k[w,z] via X=-w^3-wz^2, Y=-w^2-z^2, Z=z. Its actual conductor is YB and its relative differential Fitting ideal is (w,z^2), a length-two ramification scheme. The smooth image curve X=-2Z^3, Y=-2Z^2 has lift c=(w-z), and the full pulled-back curve ideal is (w-z)(w+z,z^2), so the *full reduced inverse support* is c. Nevertheless the ramification scheme is not contained scheme-theoretically in c, since w-z maps to -z modulo (w,z^2).

More generally for c_f=(w-f\(z\)), h=ord\(f\) and r=ord(f^2+z^2), the source computes length(R intersect c_f)=min(h,2), with scheme containment exactly when h>=2. Choosing f=iz+z^k gives unbounded conductor contact r=k+1 but ramification intersection length one. The local Jacobian factorization J_X B=\(Y\) I_R yields first-normal vanishing order s=r+min(h,2). This blocks the unsupported inference from smooth image plus full inverse support to containment of nonreduced ramification. It is a local counterexample, **not** an STCI presentation or a global normalization classification.

Source: the historical [ramification counterexample proof](#source-2026-10-07-session-ramification-scheme-counterexamplemd). Its symbolic checker was retired after the explicit model and scheme-theoretic distinctions were preserved. These local distinctions should be preserved in future conductor/ramification arguments.


## Entire cubic conductor schemes on smooth quartic scrolls

The October 8 scroll-conductor investigation extends beyond the smooth twisted-cubic downstairs conductor treated above. For an integral quartic carrier whose **finite normalization is a smooth rational quartic scroll** (F0 or F2 with its quartic hyperplane class), the source program classifies actual cubic conductor schemes using the entire conductor, including nonreduced and nongorenstein structures. The combined result excludes a mate supported on the fixed smooth quartic in characteristic zero under these hypotheses, in any mate degree. The proof uses the conductor duality sequence, Hilbert–Burch classification of the cubic conductor, generic Artin-module constraints, and full inverse-fiber conditions; it does not replace actual conductor schemes by reduced support. The independent Artin audit explicitly accepts the nonreduced reductions and supplies a direct completion of the double-line-plus-line case.

Source proof: [current proof](../supplements/QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md) and [current proof](../supplements/QUARTIC_SCROLL_CONDUCTOR_STRUCTURE.md). Independent audit: [current proof](../supplements/QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md). The alternate differential/slice proof in the first source has a separate conditional geometric passage and is **not** needed for this source-level synthesis. This is an audited historical claim, not a new result. It says nothing about singular scroll normalizations or arbitrary nonnormal quartic carriers.

A separate October 12 conductor-phase investigation for the admissible genus-one quintic A4 normalization, with Jbar=0 and coprime conormal cubics, derives an actual phase bound and all-mate exclusion within that restricted Jbar-zero, coprime-cubic stratum. Although the owner note's header says audit pending, the companion independent audit explicitly reports PASS for the all-mate exclusion under its precise geometric hypotheses, including the separately treated ramified-line locus. This does **not** exclude all genus-one quintic carriers, the common-root stratum, or other quintic normalizations. Sources: [current proof](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#6-jbar-zero-coprime-conductor-phase-bound) and [current proof](../supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#7-jbar-zero-conductor-phase-independent-audit). This belongs primarily to the low-degree carrier family and is cross-referenced here for coverage.


## Entire-conic quadratic conductor: exact power criterion

This is a reusable *actual-conductor algebra* theorem, not a classification of which conic conductor data occur for the fixed curve. For a characteristic-zero degree-four ADE del Pezzo normalization with a two-quadric anticanonical embedding, choose a projection from a point outside the surface. The graded equations can be arranged as
\[
Q_1=z^2-Az-R_1,\qquad Q_2=Lz+R,
\]
where (A,L) are linear and (R_1,R) quadratic in the four target coordinates. Elimination gives the quartic
\[
F=R^2+ALR-R_1L^2.
\]
Under the complete-intersection, finite-birational projection hypotheses, the **entire downstairs conductor scheme** is the plane conic (\Gamma=V(L,R)), not its reduction. It may be smooth, reducible, or a double line. The algebra audit accepts this exact calculation conditionally on the geometric setup; it does not independently establish every claimed anticanonical embedding or fixed-\(C_0\) spanning application. Sources: `research/notes/2026-10-09-session-genus-one-entire-conductor.md` and [current proof](#source-2026-10-09-session-genus-one-entire-conductor-algebra-independent-auditmd).

Let \(M=\mathcal O_\Gamma(1)\) and suppose the *entire* finite flat quadratic algebra is
\[
p_*\mathcal O_D=\mathcal O_\Gamma\oplus M^{-1},\qquad w^2=\delta,
\]
with trace involution (\sigma\(w\)=-w). For a nonzerodivisor section \(q=m+w\ell\), where (m\in H^0\(\Gamma,M^2\)), (\ell\in H^0\(\Gamma,M\)), (\delta\in H^0\(\Gamma,M^2\)), put
\[
\mathcal C_{\rm cyc}=\left\{\left\(\frac{1+\zeta}{1-\zeta}\right\)^2:\ \zeta\text{ a root of unity},\ \zeta\ne\pm1\right\}.
\]
For a smooth conic or the **entire plane double line**, a positive power of \(q\) is invariant under \(\sigma\) if and only if
\[
m\ell=0\quad\text{on the entire }\Gamma,
\qquad\text{or}\qquad
m^2=\rho\delta\ell^2\quad\text{on the entire }\Gamma
\quad\text{for some }\rho\in\mathcal C_{\rm cyc}.
\]
For two distinct lines, impose the corresponding criterion **separately on both components**, with possibly different cyclotomic constants and a common multiple of the resulting power orders. These are equalities of entire schemes, including nilpotents, not equations only on reduced supports. The proof uses (\sigma\(q\)/q) in generic Artin rings, separability of (T^n-1) in characteristic zero, and injectivity of sections into generic total quotient rings. A split quadratic conductor permits unbounded phase order; this algebraic criterion alone does **not** bound mate degree or exclude the remaining genus-one carrier models. Sources: [current proof](../supplements/QUADRATIC_CONDUCTOR_POWER_DESCENT.md) and its `2026-10-09-session-quadratic-conductor-power-descent-independent-audit.md`.

The quadratic-algebra proof uses2 invertible to split trace and define the involution. That splitting persists in characteristic p≠2, but the all-positive-power criterion above uses characteristic zero: powers divisible by p can remove nilpotent terms that survive every characteristic-zero power. In characteristic2 even the trace splitting and involution require replacement. No unrestricted positive-characteristic version of this entire-scheme power criterion is asserted.

The companion genus-one weak del Pezzo reduction and D5 root-saturation filter concern which actual normalizations and primitive sections can occur. They are **separate geometric hypotheses**, not consequences of the quadratic-algebra criterion. The explicit four-A1 projections are negative full-inverse-support examples, not an exhaustion of the lattice stratum. See [current proof](#source-2026-10-09-session-genus-one-delpezzo-reductionmd), [current proof](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-torsion-filtermd), and [current proof](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-singular-delpezzo-four-a1-familymd).



## Quintic geometry before the final support incidence

The [quintic structural proof](quintic_conductor_geometry.md#quintic-carriers-conormal-factorization-residual-divisors-and-low-pole-spaces) first isolates its hypotheses: in the specified nonnormal Gorenstein genus-one lane, the normal degree-five anticanonical model has one A4 singularity, a smooth lifted quartic c and a unique line ell with `H=c+ell=5ell` and `5c=4H`. This is not a classification of all quintic carriers. The [intrinsic pair proof](quintic_octic_ade_cover_and_triple.md#degree-five-del-pezzo-a4-model-intrinsic-classification-and-explicit-equations) contracts the marked A4 chain to the full plane cluster `(y−x³,x⁴)`, classifies every admissible smooth conic through it, and computes the residual automorphism group as translations. Its proof explains why the extra nonendpoint projection parameter cannot be discarded by scaling.

| Actual projection stratum | Retained mechanism and precise remaining boundary |
| --- | --- |
| Endpoint a=0 | [Support and excess proof](../supplements/QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md) plus [the actual fourth-blowup unit jet](../supplements/QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md) exclude every positive mate power in this stratum. The unit jet is an actual-ring obstruction, not only equalizer matching. |
| Endpoint a≠0 | The residual anticanonical divisor gives target contact11, intrinsic contact4 and excess7. The completed [global inverse-support proof](../supplements/QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md#2-endpoint-a-nonzero-global-independent-audit) then excludes every such endpoint projection: its actual target septic must be supported at common roots of U,V; each has order≤4, order4 allows no second root, and the three-root family is separately excluded. A degree7 septic cannot have the resulting support. |
| Nonendpoint reducible residual | The [exhaustive pole filtration](../supplements/NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md) preserves cancellation and repeated-prime strata. The specified partitions 2+2+2, 2+4 and 3+3 are excluded through [actual higher contacts](quintic_conductor_geometry.md#nonendpoint-conic-plus-quartic-residuals-all-eight-families) and [complete cubic-pair scope](quintic_conductor_geometry.md#nonendpoint-residual-cubic-pairs-complete-contact-and-coefficient-proof), not a generic-root count. |
| Nonendpoint integral residual | The actual source has arithmetic genus one, including singular affine cubics, and is smooth at its A4 point. Full inverse support excludes a degree-two map, so its image is birational of class (4,2), arithmetic genus three. Its intrinsic c-ideal has length6, including length2 at A4; target contact14 forces excess8. The curve-model quotient length2 cancels in the local contact comparison and gives no upper bound on that excess. This incidence remains open. |
| Nonendpoint target fibers | The [actual fiber equations](quintic_conductor_geometry.md#4-nonendpoint-target-fiber-reduction-and-bounded-exclusions) keep finite denominator/rank boundaries, A4 target, infinity and primitive cube-root compatibility. Their equal-lift exclusion does not exhaust every projection. The [single-root incidence](quintic_toric_center_incidence.md#nonendpoint-single-root-incidence-and-actual-quotient-fibers) preserves separate quotient fibers and singular denominator charts. |

The recurring mechanism is **scheme-theoretic pullback of the marked curve ideal**, followed by exact lengths in actual integral curve rings. Finite birational curve-model defect, conductor contact, differential degeneracy and excess contact are different quantities. Smooth source or image branches can have high mutual contact. The seven- and eight-length budgets by themselves are necessary constraints. The endpoint case has a completed additional actual-fiber and higher-jet exclusion; the integral nonendpoint eight-excess incidence remains open. The entire intrinsic endpoint family is therefore excluded in every mate degree, while the separate nonendpoint modulus is retained. These are the characteristic-zero source results; their A4/del Pezzo classification and coefficient separability have not been asserted in arbitrary characteristic.

## Quintic support: closed h=3 and the remaining h=2 problem

These statements concern **admissible nonendpoint genus-one quintic \(A_4\) projections in characteristic zero**, not all quintic carriers. Let \(H_j\) be the homogeneous gcd of the corrected first conormal cubics, and let \(F_{\rm cond}\) be the **actual homogeneous conductor octic**.

**Complete \(h=3\) lane.** Under the accepted homogeneous gcd-three classification, every admissible projection with \(\deg H_3=3\) is excluded for **all positive mate degrees**. Zero-cubic and proportional boundary charts are included. In the remaining proportional family \(F_{\rm cond}=\mathrm{const}\cdot H_3S_5\). Full inverse support restricts the roots of \(S_5\) to those of \(H_3\). The homogeneous leading-drop analysis excludes infinity support, and the complete alternatives are: three distinct roots, or multiplicity patterns \(5\), \(4+1\), \(3+2\). The last pattern uses the **original six-generator** polynomial row \(M_6\) and an exact identity \(M_6W=(Vc_5)^2\), where the admissible parameter product \(Vc_5\) is nonzero; thus the six equations cannot vanish simultaneously. This closes the entire \(h=3\) lane, not merely a generic chart. [Accepted scoped result](../supplements/QUINTIC_H3_SUPPORT_EXCLUSION.md).

**Differential content of \(h=2\).** For every finite birational ring extension \(A\subset B\) with conductor \(I\), the identity \(I\Omega_{B/A}=0\) follows from \(c\,db=d(cb)-b\,dc\) for \(c\in I\). Along the smooth lifted curve, the relative differentials have the local form \(\Omega_{S/X}\otimes\mathcal O_c\cong\mathcal O_c/(u_1,v_1)\,dT\), where \(u_1,v_1\) are the corrected conormal symbols. Hence their complete homogeneous gcd \(H_2\) divides \(F_{\rm cond}\), including multiplicities and the permitted simple \(A_4\) infinity factor. Write \(F_{\rm cond}=H_2Q_6\), with \(Q_6\) homogeneous sextic. This is **divisibility**, not equality of conductor and first-symbol divisors.

When no extra \(A_4\) support is allowed, the remaining support condition becomes the eigenvector equation
\[
D_{H_2}Q_6=\mu Q_6,\qquad D_K=\(\partial_tK\)\partial_s-\(\partial_sK\)\partial_t.
\]
For quadratic \(H_2=as^2+bst+ct^2\), with \(\Delta=b^2-4ac\), the degree-six action has characteristic polynomial
\[
\mu\(\mu^2-4\Delta\)\(\mu^2-16\Delta\)\(\mu^2-36\Delta\),
\]
valid also on the repeated-root boundary. With the allowed \(A_4\) point \(s=0\), retain the homogeneous system \(D_{sH_2}Q_6=L_1Q_6,\ jD_{H_2}Q_6=\mu Q_6\), \(j=\bar J\), rather than discarding \(j=0\). For \(j\ne0\) the support condition is equivalently the covariant identity \(J(\operatorname{Hess}\(F_{\rm cond}\),Q_6)=0\). These are necessary incidence reductions, **not an \(h=2\) exclusion or conductor-power descent**. The original source flags its later quadratic-algebra norm computation as pending independent review. [Differential proof and incidence](quintic_octic_ade_cover_and_triple.md#2026-10-14-generalization-quintic-h2-conductor-quotient).


## Actual h=2 incidence and its linear-system meaning

On the justified remaining nonendpoint \(A_4\) quintic \(h=2\) parameter open, write \(H=t^2+vst+ws^2\), \(Q=\sum_{i=0}^6q_is^{6-i}t^i\), \(j=\bar J\), and \(R=D_HQ\). The accepted closed-lane and intrinsic-contact results give the **unit ideal** \((q_5,q_6)=A\) on the localized candidate ring; this is not permission to invert either coefficient separately. The full quadratic and cubic rank incidence has 77 minors. Its saturation by \((q_5,q_6)\) equals the saturation of **twelve fixed generators**: eleven selected cubic minors and \(jM_{56}\), where \(M_{56}=q_5r_6-q_6r_5\). The identity uses pivot covers, works with nonreduced parameter rings, and does not divide by \(j\). The actual conductor norm product can be appended as a single necessary equation without splitting its factors.

On the same localized scheme, the cubic rank condition is equivalently the existence of uniquely determined, locally gluing witnesses \(d,u\) for
\[
h\(z\)q'\(z\)=(dz+u)q\(z\),\quad
E_i=w(i+1)q_{i+1}+(vi-u)q_i+(i-1-d)q_{i-1}=0
\quad\(0\le i\le7\).
\]
The equations imply **as ideal memberships**, not just at closed points, \((d-5)(d-6)=0\) and \(j(d-6)=0\). The \(d=5\) branch retains simple intrinsic-\(A_4\) infinity contact; \(d=6\) has no infinity root. Neither is discarded.

Geometrically, the ODE measures invariance of the zero divisor of q under the polynomial vector field `h\(z\) d/dz`, with the right-hand affine factor recording the chosen line-bundle lift and infinity weight. At a root x of q of multiplicity m, write `q=(z-x)^m r`, r\(x\)≠0. The leading term of hq′ is `m h\(x\) r\(x\)(z-x)^(m-1)`, whereas `(dz+u)q` has order at least m. In characteristic zero this forces h\(x\)=0. Thus the derivative equation encodes support at the actual root directions, rather than an unrelated coefficient rank. Repeated roots of h and the prescribed infinity support still need their exact coefficient equations; this interpretation does not replace them. In characteristic p a multiplicity divisible by p makes the displayed leading coefficient vanish, so this support argument does not extend without a separability or multiplicity hypothesis.

There is a single derived spectral polynomial on this entire scheme. Put \(\Delta=v^2-4w\), \(\eta=dv-2u\),
\[
P_6\(X\)=X\(X^2-4\Delta\)\(X^2-16\Delta\)\(X^2-36\Delta\),\qquad
P_5\(X\)=\(X^2-\Delta\)\(X^2-9\Delta\)\(X^2-25\Delta\).
\]
Then \((d-5)P_6\(\eta\)+(6-d)P_5\(\eta\)\) belongs to the same ODE ideal. The proof uses the two complementary idempotents \(d-5\) and \(6-d\) and Cayley–Hamilton on the sixth and fifth symmetric powers, without radicalizing, inverting a discriminant, or choosing roots. This is a computational compression, **not a unit-ideal certificate**. The subsequent whole-\(h=2\) global saturation prospect stopped at its memory guard and supplied no mathematical emptiness result; that resource-limit history is not part of the theorem. [Twelve generators](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-twelve-generator-independent-audit), [ODE equivalence](https://github.com/markluxton1/STCI/blob/63b401a4b399c435fe292820dcbf630470e01ff6/research/supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-automatic-open-ode-independent-audit), [spectral identity](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-eta-spectral-independent-audit).


The **global** monic necessary incidence has seventeen equations in nine variables on the original-parameter open `delta E Delta1!=0`. It retains the inverse-map boundary `Delta K=0`. Saturating by `Delta K` treats only a smaller chart and cannot settle the global incidence. The [global monic proof](https://github.com/markluxton1/STCI/blob/63b401a4b399c435fe292820dcbf630470e01ff6/research/supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence) states this boundary exactly. The [degree-five j=0 reduction](quintic_toric_center_incidence.md#quintic-h2-the-degree-five-necessary-incidence-and-its-open-boundary) remains unresolved: both proposed exclusions mistake a fixed simple A4 zero at source infinity for one at source zero, so they do not justify their pure-power specialization. The later verifier additionally divides the unreversed determinant polynomial instead of the actual source conductor. Replaying its resultants cannot repair this reduction gap. The degree-six j!=0 branch and full conductor-power descent remain open. Neither the ODE reduction nor the spectral accelerator resolves them.

## Intrinsic A4 contact and the necessary homogeneous norm

In the admissible nonendpoint genus-one quintic \(A_4\) model, write \(j=\bar J\), \(\delta\ne0\), and \(F\) for the **actual primitive conductor octic** in the target coordinate \(p=\delta/r\). On \(j=0\), the exact coefficient identities are
\[
F(0)=0,\quad [p]F=-2G\(\delta^2+2B+G\)\(3\delta^2+G\)^2,
\]
and, when \(G=-3\delta^2\),
\[
[p^2]F=-108\delta^5\(\delta^2-B\).
\]
The accepted \(G=j=0\) mate exclusion and full target-fiber criterion show that any remaining \(j=0\) mate candidate has \(G\ne0\) and \(\delta^2+2B+G\ne0\). Thus its intrinsic \(A_4\) conductor contact is **exactly one or two**, not arbitrarily large. The contact-two case occurs on \(G=-3\delta^2\) with \(B\ne\delta^2\).

For the homogeneous \(h=2\) factorization \(F_{\rm src}=H_2Q_6\), the first-symbol factor \(H_2\) cannot contain the \(A_4\) point on a surviving candidate. If \(\operatorname{Res}(H_2,Q_6)\ne0\) when \(j=0\), all sextic roots would have to lie at the \(A_4\) point, forcing conductor contact six and contradicting the bound. Therefore **every remaining \(h=2\) mate candidate**, for either value of \(j\), satisfies \(\operatorname{Res}(H_2,Q_6)=0\). This is a necessary homogeneous norm equation, not an emptiness proof; the repeated-root and infinity charts remain included. [Intrinsic coefficient and support proof](quintic_octic_ade_cover_and_triple.md#2026-10-14-generalization-quintic-intrinsic-a4-contact-bound).


## Full conductor contact, its differential, and its weighted budget

For a finite normalization \(\nu:S\to X=\(F=0\)\subset\mathbf P^3\) with \(X\) integral, a smooth curve \(C\) whose **full reduced inverse image** is one smooth Cartier \(c\cong C\), \(S\) regular along \(c\), and \(X\) regular at the generic point of \(C\), finite duality identifies the actual upstairs conductor as \(\mathcal O_S(-B)=\omega_S\otimes\nu^*\omega_X^{-1}\) near \(c\). Let \(A\) be the full common-zero divisor of the normal differential of \(\nu\) along \(c\), and \(D_F\) the common-zero divisor of the **actual first normal symbol** of \(F\). The residue/Jacobian identity yields the equality of effective divisors, with multiplicities,
\[
D_F=B|_c+A.
\]
In particular \(A\) is **not** itself the conductor contact divisor; equality \(D_F=B|_c\) requires transverse immersion all along \(c\).

If \(X\) has degree \(a\), \(C\) degree \(d\) and genus \(g\), and \(k=c^2\), adjunction gives the weighted conductor budget
\[
N=B\cdot c=d(a-4)+k-(2g-2).
\]
Writing \(B=\sum m_iD_i\), ampleness of \(c\) gives \(\sum m_i\(D_i\cdot c\)=N\), bounding prime conductor components, multiplicities and total branch contact. For each downstairs conductor curve, let \(d_\Delta\le a\) be the total generic reduced normalization degree. The **ordered off-diagonal pair correspondence**, including conjugate pairs on one prime, has total weighted first-projection contact bounded by \((a-1)N\). The three fixed-\(C_0\) singleton models give \((a,N,(a-1)N)=(8,20,140)\) for both quadric normalizations and \((16,51,765)\) for the plane normalization. These are finite integer-contact budgets, **not** bounds on scalar phase orders or nilpotent logarithmic defects. The global conductor need not be Cartier, only Cartier near \(c\); singular or non-Cartier lifts and generically nonregular carriers are outside the stated bridge. An independent review **passed under the stated Gorenstein, smooth Cartier-lift, full-support and generic-regularity hypotheses**; applications to a globally non-Gorenstein normalization require retaining the original local-versus-global distinction. [Independent review](#consolidated-historical-supplement-researchsupplementsprojection_conductor_contact_and_phasemd). [Jacobian identity](carrier_conductor_differential_comparison.md#local-residue-identity-and-global-contact), [contact and pair budgets](#consolidated-historical-supplement-researchsupplementsprojection_conductor_contact_and_phasemd).


## Minimum actual carriers and Cartier-index compression

The [canonical compression proof](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md#canonical-compression-on-a-minimum-actual-carrier) chooses a carrier of minimum degree **among carriers that occur in an actual defining pair**. In characteristic zero, for a generically regular carrier and local Cartier exponent e, Picard torsion-freeness compresses its mate to eC~nH. For the fixed quartic, n=4e/a≥a and e≥a²/4; a genuinely minimum sextic carrier would require 3|e and e≥9. Choosing instead a minimum-degree surface merely containing C would invalidate the argument: the smooth quadric contains C but is not a possible sole-support carrier in characteristic zero.

This mechanism can be used constructively as a lower-complexity target or obstructively as a local-index constraint. The proof uses no genus calculation; its degree-d formulation is in the same mathematical home. Generic singularity along C and characteristic-p Picard behavior remain separate boundaries.

## Normal indices and the exact socle bridge

[R-0034](../results/normal_carrier_index_socle.md) uses actual local Cartier index r, not surface multiplicity. For an actual mate multiplicity n=kr, the pointwise socle relation is D_n=(k−1)A_F+kD_r, with ordinary normal-layer torsion satisfying 2Σlength\(T_i\)=nD_n. [R-0035](../results/normal_carrier_bounded_index_exclusion.md) uses its inherited normal-carrier and quadratic-direction hypotheses to exclude the regime where all actual on-curve indices are at most four; it does not treat arbitrary higher indices or nonnormal carriers.

[R-0036](../results/pointwise_conductor_socle_defect.md), for an already existing supported pair with its smooth singleton Cartier lift and invertible conductor, gives D_n=(n−1)A−B|c as an equality of actual divisors. It implies coefficientwise inequalities, not just a degree bound. It is not a substitute for full conductor-unit membership, and it has no established branchwise extension by summing over multiple inverse curves. See [the exact interface](04-carriers.md#47a-conductor-gluing-versus-the-top-socle-divisor).

A separate [normal-carrier divisor reformulation](../supplements/NORMAL_CARRIER_DIVISOR_GEOMETRY.md) preserves the source's proposed equivalence between a Q-Cartier Hodge equality and an actual positive divisor relation, together with its suggested local-socle certificate. That source strengthening remains explicitly pending independent mathematical audit; relocating its full proof does not replace the stated inputs of R-0034/R-0035.

## Conditional sextic applications and the remaining implication

The [conditional sextic treatment](normalization_conductor_phase2_addendum.md) retains the actual rank-22 global source, all q³ lift freedom, constant-rank cubic correction map, the quadric-cycle norm proof including collision and branch multiplicities, free-orbit unit certificate, remaining two-node conic and zero-defect pencils, degree-52 exceptional locus, and the singular-trisecant/nonnormal alternative. [Endpoint-four actual sextics](toric_sextic_residuals_and_limits.md#endpoint-four-sextic-constructions) provide complete second-symbol lifts and a single-carrier necessary jet exclusion, not a construction or exhaustion of the family.

The common mechanism is a global section whose admissible local class must lift through an actual source module and then descend through an actual conductor. Divisor classes, reduced phases, first symbols and formal roots each forget different information. Their comparison can guide constructions and exclusions only after establishing a common actual carrier or pair. No all-carrier coverage theorem, full h=2 incidence solution, or unrestricted characteristic-zero STCI conclusion follows.

## Characteristic range of the mechanisms

| Mechanism | What extends, and what fails |
| --- | --- |
| Full conductor fiber product, pure generic-to-global descent, fixed-carrier relation cone | Characteristic independent under the stated finiteness, depth and support hypotheses. |
| Nilpotent unit-power rigidity | In characteristic zero, a nonzero logarithmic defect survives every power. In characteristic p, a sufficiently large p-power kills a finite nilpotent defect; it leaves non-torsion residue phases untouched. |
| Single-field extension-degree compression | The proved form uses characteristic zero and all roots of unity in the residue field. It is not a theorem for arbitrary Q-algebras or arbitrary inseparable residue extensions. |
| Plane differential exclusion | The identity forces b=0 in the field. It excludes every b>0 in characteristic zero; in characteristic p it only excludes b not divisible by p. A p-power can evade the differential test. |
| Minimal-degree Cartier singleton classification | The retained proof uses characteristic-zero surface classification. No unrestricted positive-characteristic extension is asserted. |
| Conductor–socle Jacobian comparison | The pointwise proof extends when the Jacobian factor n is invertible, with the same geometric hypotheses and actual socle input; in characteristic dividing n the Jacobian may vanish although the socle does not. |
| Conditional sextic global-symbol algebra | An exact rational calculation extends only after its denominators and necessary rank minors remain invertible. The characteristic-zero Milnor/Hodge surface contradiction is a separate input and cannot be transported just from a matrix rank. |

For this fixed embedding, every positive characteristic admits an actual STCI with a quartic carrier; the [complete characteristic-specific construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) proves this directly. Thus the characteristic-zero quartic-carrier exclusion and the nilpotent power obstruction must not be stated without their characteristic range. Positive-characteristic witnesses at each finite level do not supply one characteristic-zero or infinite-formal descending power.

For a prescribed degree rather than eventual powers, [sections and modules through normalization](../supplements/NORMALIZATION_SECTION_AND_MODULE_DESCENT.md) proves the exact fiber-product and module-factorization criterion, including full inverse support, all branch degrees, integral singular curves and the normalized-blowup support test. The supported-conductor power argument there is a distinct direct proof.


## Consolidated historical supplement: `research/supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md`

The historical sections retain their hypotheses, qualifications, and proof status. Where an argument is repeated, links point to the full proof.

# conditional 2 12 singular and conductor

## Proof-dependency map: node gluing and conductor constraints

The [two-node torsion calculation](#2026-10-20-conditional-2-12-singular-continuation) and [subsequent singular continuation](#2026-10-21-conditional-2-12-singular-continuation2) analyze branch identifications. The [cubic-image/conductor interface](#2026-10-21-conditional-2-12-cubic-image-and-conductor-interface) and [conductor ramification](#2026-10-21-conditional-2-12-conductor-ramification) add global compatibility conditions, with an [independent chart review](#2026-10-21-conditional-2-12-conductor-and-chart-independent-review).

The [symbol-map and sextic realization dossier](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-elimination) supplies the equation-level inputs; the [strict-surface continuation](rank_strata_and_sextic_lifts.md#nonnormal-conductor-budget-and-local-escape-models) imposes further conditions. The torsion and conductor tests are necessary compatibility constraints in the stated conditional geometry; they are not an unconditional exclusion of the (2,12) degree pair.

Preserve the exact two-node factors, torsion scheme, diagonal-slice countercheck, and chart-independence qualifications below.

---


Permanent mathematical dossier. The (2,12) setting and every other hypothesis remain conditional as in the original arguments; full calculations, exceptional cases and failures are retained.

---

## 2026-10-20-conditional-2-12-singular-continuation

# Conditional (2,12;6,16;2): exact two-node torsion and a diagonal exclusion

Date: 2026-10-20. Author: `singular_gluing` continuation worker.
Status: **new proposal; exact reduction and scoped exclusion**. No
record or inherited proof is changed. The factor-matrix and
torsion-scheme calculation below was independently reconstructed by
`two_node_torsion_audit`, with an additional factorization check by its
`factor_check` worker. The diagonal ambient exclusion, its exact
contraction ideal, its source substitution in the actual chart,
and its arithmetic were independently reviewed by the same auditor
and its `diagonal_arithmetic` worker, with verdict PASS.

## Scope and existing interface

Retain precisely the characteristic-zero curve, actual-CI, full generic
coprime `(2,12)` initial ideal and saturated movement-two relation
hypotheses in
[the singular-root bridge note](../supplements/SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md).
The current task investigates the necessary structured incidence, not
unrestricted homogeneous equations. The inherited universal first
incidence and complete second test are stated in [STCI-R-0007](../results/quadratic_root_obstruction_model.md), and the
finite singular bridge remains a reviewed proposal in the linked note.

The source generator for these new calculations is
`../computations/conditional_2_12_singular_continuation_2026_10_20.py`.
It imports the inherited universal equation constructor without its
artifact-writing footer and substitutes into the existing exact
operators. It does not rerun an inherited proof or seed certificate.

## 1. Full two-node factors in the original coordinates

Write the two actual `(1,1)` factors as

    li=(Ai+Ci*z)u+(Bi+Di*z)v,       i=1,2,
    Delta_i=Ai*Di-Bi*Ci.

No change of base or direction ruling is performed. In homogeneous
base coordinates `z=[z0:z1]`, put

    Mi=[[-Bi,-Di],[Ai,Ci]].

The component `Di=(li)` is the graph `[u:v]=[Mi*z]`, and it is a
smooth `(1,1)` component exactly when `Delta_i !=0`. Set

    N=adj(M1)*M2,
    tau=tr(N)=A1*D2+A2*D1-B1*C2-B2*C1,
    delta=det(N)=Delta_1*Delta_2.

The nodes are the eigenlines of `N`. More precisely
`det(M1*z,M2*z)=det(z,N*z)`, with binary discriminant

    D=tau^2-4*delta.

Thus the full two-node open, with neither node discarded, is

    delta*D != 0.                                                (1)

This parameterization covers all ordered pairs of smooth `(1,1)`
components with two transverse intersections, up to the independent
nonzero scales of the two factors. The finite swap of the factors
does not change any condition below.

## 2. Exact torsion scheme of the actual node identifications

For `L=O_Z(1,-1)`, the fiber at `(z,w)` is
`Hom(ell_z,ell_w)`. The matrix `Mi` supplies a nowhere-zero section
`sigma_i` of `L|Di`. At a node represented by an eigenvector `v_j`,

    M2*v_j=mu_j*M1*v_j,
    g_j=sigma_1(z_j)/sigma_2(z_j)=mu_j^(-1).

Consequently the actual two-node gluing modulus is

    lambda=g_1/g_2=mu_2/mu_1,

up to inversion. Rescaling either factor changes both eigenvalues
together and leaves this ratio unchanged. This proves directly in
the original coefficients that

    L^12=O_Z  iff  N^12 is scalar.                               (2)

It does not replace the original coefficients in the ambient first
or second operator by an arbitrary ruling normal form.

Cayley-Hamilton gives the exact equation

    Q12=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)
              *((tau^2-2*delta)^2-3*delta^2)=0.                  (3)

The polynomial has degree twenty-two in the eight factor
coefficients. Equivalently,

    Q12=tau^11-10*delta*tau^9+36*delta^2*tau^7
        -56*delta^3*tau^5+35*delta^4*tau^3-6*delta^5*tau.

This is an exact scheme equation on (1), not just a closed-point
test. Indeed `N^12=Q12*N-delta*U10*I`. If
`N=[[a,b],[c,d]]`, its scalar-matrix ideal is

    Q12*(b,c,a-d).

But `D=(a-d)^2+4*b*c` is invertible on (1), so
`(b,c,a-d)` is the unit ideal and the scalar-matrix ideal is exactly
`(Q12)`. Thus the full two-node torsion parameter scheme is

    Spec k[Ai,Bi,Ci,Di]_[delta*(tau^2-4delta)] / (Q12).           (4)

This includes orders two, three, four, six and twelve, as required
by divisibility by twelve. The factor `tau` must occur only once:
replacing it by `tau^2` gives the correct geometric support but
doubles the involution stratum. At `tau=0`, the quotient
`Q12/tau=-6*delta^5` is a unit. The independent audit specifically
caught and corrected this possible scheme error.

The [original-coordinate generator](../computations/conditional_2_12_singular_continuation_2026_10_20.py)
constructs the exact first/second incidence with (3) and open (1).
This replaces a 143-component torsion-kernel witness by one
polynomial on this stratum. It is still a low-order necessary
incidence; the actual global sextic cubic matching condition and
all subsequent certificates remain additional requirements.

## 3. A proper diagonal slice is exactly excluded already at first order

Consider only

    l1=t1*u+z*v,          l2=t2*u+z*v,
    t1*t2*(t1-t2) !=0.                                         (5)

This is a proper two-parameter slice in the original ambient
coordinates. It is not a normal form for every two-node root under
automorphisms of `C0`. Separate arbitrary PGL2 transformations of
the two rulings would change the ambient obstruction operator and
are not used.

Substituting

    a0=t1*t2, b1=t1+t2, c2=1,
    all other root coefficients zero

in the universal sixteen first equations and eliminating the twelve
first-unit coefficients gives the exact ideal with generators

    P(t1)+P(t2),             (t1-t2)*P(t2),
    P(T)=3*T^3-10*T^2+20*T-24
        =(T-2)*(3*T^2-4*T+12).                                (6)

The complete QQ elimination in
`../computations/conditional_2_12_singular_continuation_2026_10_20_diagonal.m2`
returned these two generators. Thus on (5), first compatibility
forces `P(t1)=P(t2)=0` with distinct roots.

There is also an exact elimination proof without relying on a
Groebner-basis transcript. Put `S=t1+t2`, `T=t1*t2`. In the inherited
first-unit variable ordering the equations force

    h9=-7/2-3*S/8,
    h2=(3*S^2-10*S-6*T)/8.

Rows one and six, using zero-based row indices, then reduce to
`-C/8,-A/8`, where

    A=P(t1)+P(t2),
    C=t2*P(t1)+t1*P(t2).

All other first-unit variables may be set to zero; direct
substitution makes every first equation vanish when `A=C=0`.
Consequently their exact contraction is
`(A,C)=(A,(t1-t2)*P(t2))`, with no radical taken. On (5) this is
`(P(t1),P(t2))`, consisting of the six reduced ordered pairs of
distinct roots. The first unit is unique on that open.

There is a short exact arithmetic exclusion. If one selected root
is `2` and the other is a root `r` of `3*T^2-4*T+12`, then

    t1/t2+t2/t1 = r/2+2/r = 2/3.

If the two selected roots are the two roots of that quadratic, their
sum is `4/3` and their product is `4`, whence

    t1/t2+t2/t1 = ((4/3)^2-8)/4 = -14/9.

Neither rational number is an algebraic integer. A root of unity
and its inverse have algebraic-integer sum. Therefore no ratio of
two distinct roots in (6) is any root of unity, and in particular
it cannot satisfy the required twelfth-power condition. This
excludes every point of the diagonal slice (5), before the second
ambient obstruction or global cubic matching is considered.

For a direct rational nonvanishing certificate specific to twelve,
put `x=(t1+t2)^2/(t1*t2)`. The two cases give `x=8/3` and `x=4/9`.
After dividing (3) by the nonzero factor
`(t1+t2)*(t1*t2)^5`, its values are respectively

    (x-1)*(x-2)*(x-3)*((x-2)^2-3)
        =230/243,                  x=8/3,
        =75670/59049,               x=4/9.

Both are nonzero in every characteristic-zero field. This supplies
an exact torsion nonvanishing check without choosing complex
embeddings or approximating eigenvalue ratios.

For an independent exact computation check, the same M2 input adds

    sum_(j=0..11) t1^(11-j)*t2^j,
    iv*t1*t2*(t1-t2)-1

to the sixteen first equations. Its QQ Groebner basis is `{1}`.
Adding the complete twenty-five second equations again gives `{1}`.
The latter repetition is recorded only as an output already produced
by the same script; the first-order argument is sufficient.

The independent auditor expanded the accepted actual transition
through normal degree three with a separate stdlib rational-Laurent
implementation and compared all sixteen substituted first equations;
every entry matched exactly. Its continuation-ready source is
`../computations/conditional_2_12_singular_continuation_2026_10_20_independent_diagonal_audit.py`.
The independent output was
`INDEPENDENT_DIRECT_TRANSITION_FIRST_EXPORT_MATCH: True`.

## 4. Retained coverage and first unresolved global condition

The diagonal exclusion does not eliminate the full two-node scheme
(4), nor the integral nodal or smooth-root loci. Cuspidal and tangent
strata are excluded by the reviewed torsion-free Picard argument
in the previous note. On retained roots, symbol membership and
universal root compatibility still have to be compared with the
actual jets of a global sextic. Their first matching condition is

    [F3-alpha*G0] mod(f)=0,
    F=F0(alpha*f)+lambda*q^3,

with actual `k` coefficients and with every zero of `alpha`
retained. The next abstract Cartier obstruction at `E3` is a
separate condition. Nothing here asserts a nonempty low-order
incidence, a global pair, a full degree-twelve standard basis, or
the global gcd/Bezout support certificate.

The general-factor first-incidence/torsion computation, if attempted,
must report its exact chart, resources and returned ideal. An
interrupted computation is neither an emptiness nor a survival
certificate. This note preserves the full original-coordinate
parameter scheme (4) regardless of the outcome on any individual
computational chart.


---

## 2026-10-21-conditional-2-12-singular-continuation2

# Conditional (2,12;6,16;2): forced-norm two-node reductions and exclusions

Date: 2026-10-21. Author: `singular_gluing` continuation worker.
Status: **new exact reductions and scoped exact exclusions**. The cubic-defect identities, generic line/conic
decomposition and original-coordinate normalizations were independently
reviewed by `two_node_torsion_audit`. The new completed line-component and boundary
CAS exclusions are submitted to `certificate_audit` for independent
review. An interrupted conic computation gives no exclusion or survival
certificate.

## 1. Literal actual-pair scope and dependencies

Retain characteristic zero, the fixed
`C0=[s^4:s^3t:st^3:t^4]`, an actual homogeneous pair of degrees
`6,16` with sole reduced support `C0`, FULL generic ordinary initial
ideal a coprime binary CI `(2,12)`, and the ACTUAL saturated first
relation of movement two. The inputs are
[R-0010](../results/saturated_first_relation_normal_flatness.md),
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md),
and the universal first/second operators in
[R-0007](../results/quadratic_root_obstruction_model.md).
The finite singular-root bridge remains the reviewed proposal in
[the singular-root note](../supplements/SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md).

This continuation additionally uses the independently reviewed
**actual-pair** norm identity from
[the actual-pair norm proof](../synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge):
if `q1=u+zv/2`, `tau=f|_(q1=0)`, then `tau!=0` and

    alpha proportional tau(omega*z)*tau(omega^2*z), omega^3=1.

That identity retains collisions and endpoint ramification. It must
not be inferred on arbitrary low-order points just from the generic
orbit factorization. The sextic symbol image and its exact
one-dimensional kernel are the reviewed new computation in
[the exact sextic symbol map](rank_strata_and_sextic_lifts.md#2-the-exact-global-k-linear-symbol-map).

Only the two-node reducible root stratum is considered below. The
previously excluded cuspidal and tangent strata stay excluded;
integral nodal and smooth roots remain outside these reductions.

## 2. An exact cubic defect makes the forced-norm equations small

Write the two factors in the **original** accepted normal coordinates:

    li=(Ai+Ci*z)u+(Bi+Di*z)v,       Delta_i=Ai*Di-Bi*Ci !=0.

The two-node open additionally inverts
`T^2-4*Delta_1*Delta_2`, where

    T=A1*D2+A2*D1-B1*C2-B2*C1.

For a single factor suppress its index and put

    d=D-A/2, e=-C/2, tau_l=B+d*z+e*z^2,
    alpha_l=B^2-B*d*z+(d^2-B*e)z^2-d*e*z^3+e^2*z^4,
    kappa=(A+2D)*(d^2+BC/2),
    beta=-A*d^2+BC*(D-A).

Then `alpha_l=tau_l(omega*z)*tau_l(omega^2*z)` and the degree-one
normal symbol `p_l=alpha_l*l` differs from an ACTUAL global cubic
symbol by exactly

    p_l = c_l + (kappa/2)*z^3*v.                              (1)

The cubic-symbol image is spanned by

    q1, z*q1, z^3*q1, z^4*q1,
    v, -z^2*u+z^3*v/2, -2*z^5*u.

The coefficients of the last three generators in `c_l` are,
respectively,

    B^3,              beta,              -C^3/8.

The four `q1` coefficients, if `p_l=P(z)u+R(z)v`, are precisely
the coefficients of `P` at degrees `0,1,3,4`. Identity (1) follows
by direct multiplication, and does not assume first compatibility
of the single linear factor.

For `f=l1*l2` the forced multiplier is `alpha=alpha_1*alpha_2`.
Products of two actual cubic symbols lie in the global sextic
symbol image `V_(6,2)`. Applying its eleven exact quotient rows to
`p_1*p_2` leaves only zero-based rows `3,6,9`:

    row3 = -2*(kappa_1*B2^3+kappa_2*B1^3),
    row6 = -(kappa_1*beta_2+kappa_2*beta_1+kappa_1*kappa_2),
    row9 = (kappa_1*C2^3+kappa_2*C1^3)/4.                      (2)

Every other quotient row is identically zero. Thus setting the
three right sides of (2) to zero gives the **exact pullback
scheme** of forced-norm global symbol membership in the original
factor coefficients.

The independent verifier
`../computations/conditional_2_12_singular_continuation2_2026_10_21_independent_symbol_audit.py`
checks both identities (1) and all eleven rows with sparse rational
polynomial arithmetic. Its recorded output is
`FACTOR_CANONICAL_CUBIC_DEFECT_IDENTITIES: PASS` and
`ALL_ELEVEN_GLOBAL_SYMBOL_ROWS: PASS`, with row multipliers
`-2,-1,1/4` as above.

## 3. Mixed zero/nonzero defects are empty on the actual-pair open

Suppose `kappa_1=0` and `kappa_2` is invertible. Equations (2) give

    B1^3=C1^3=beta_1=0.

As raw ideals these do not say `B1=C1=0`; they make these two
coefficients nilpotent. Since `Delta_1` is invertible, `A1,D1`
are units. The equation `beta_1=0` makes `d1^2`, and hence `d1`,
nilpotent. All coefficients of

    tau_1=B1+d1*z-C1*z^2/2

are nilpotent. Consequently the required open `tau_1*tau_2 !=0`
is empty as a scheme. At closed points the only possible first
factor is the already excluded quadric direction `q1`. The
symmetric mixed stratum is identical. It is therefore enough to
retain both defects zero, or both defects nonzero.

## 4. Generic nonzero defects: a disjoint line/conic decomposition

On

    B1*B2*C1*C2*kappa_1*kappa_2 !=0,

independent factor scaling sets `B1=B2=1`. The actual
`C0`-preserving torus, after dividing each factor by its common
scale, acts by

    (A,B,C,D) -> (t*A,B,t^2*C,t*D).

Thus `C1=1` is permitted on a square-root finite etale cover,
with residual `mu2`. Equations (2) then give exactly

    C2=w, w^3=1,
    kappa_2=-kappa_1,
    beta_2-beta_1=kappa_1.                                  (3)

All three cube roots, including one, must be retained. This is a
gauge slice using only the actual torus; no arbitrary ruling PGL2
transformation is applied to the ambient obstruction operator.

Put

    x=d1, y=w*d2, a=A1+x,
    U1=2*x^2+1, U2=2*y^2+1.

Then

    kappa_1=a*U1,
    kappa_2=(w*A2+y)*U2,
    kappa+2*beta=2*d^3+3*BC*d.

Consequently (3) is equivalent as an ideal to

    kappa_1+kappa_2=0,
    (x-y)*(2*(x^2+x*y+y^2)+3)=0.                              (4)

Since both defects are units, `U2` is already a unit and one can
eliminate `A2` without losing any additional stratum:

    w*A2=-y-a*(2*x^2+1)/(2*y^2+1).                           (5)

The line and conic in (4) are disjoint **on this open**. Indeed
if `ell=x-y` and `Q=2*(x^2+x*y+y^2)+3`, then

    Q=3*U1-2*ell*(y+2*x).

Thus `(ell,Q)=(1)` after `U1` is inverted, and their product
equation is an exact disjoint scheme union. Before localization
their intersection lies at `x=y,2*x^2+1=0`, which belongs to
the separate zero-defect strata and has not been discarded.

The compact generic model, including eight remaining first
equations and all forty-eight actual global cubic matching
equations, is
`../computations/conditional_2_12_singular_continuation_2026_10_21.m2`.
It loaded successfully and reported the stated equation counts.
Loading is not an elimination result. A metadata-label correction
is recorded in section 9.

## 5. The entire generic line component is exactly excluded

On `y=x`, equations (5) give

    A1=a-x,           D1=(a+x)/2,
    A2=-w^2*(a+x),    D2=w^2*(x-a)/2.

Writing `J=(a^2-x^2-2)/2`, the trace/determinant of the actual
two-node gluing matrix are

    T=-w^2*(a^2+x^2)-1-w,
    delta=w*J^2.

Use the exact spectral equation from the previous continuation,

    Q12=T*(T^2-delta)*(T^2-2delta)*(T^2-3delta)
                    *((T^2-2delta)^2-3delta^2)=0.             (6)

The endpoint coefficients are `a2=w,c0=1`, so eight first-unit
variables can be eliminated by the triangular recurrences, with
no new denominator besides the already invertible `w`. Four
variables `h4,h5,h6,h7` remain.

For `w=1`, the root coefficients depend on `a` only through
`p=a^2`. Eliminating those four first-unit variables gives the
following four exact necessary polynomials in `p,x`:

    48p^3+1130px^2+292p^2+8400x^2+1072p-615,
    4x^4+2px^2-14x^2-2p+1,
    22px^3+8p^2x+60x^3-28px-15x,
    6p^2x^2-38px^2-22p^2-390x^2-49p+30.                      (7)

Here `T=-(p+x^2+2)`, `delta=((p-x^2-2)/2)^2`, and the precise
generic two-node open is

    p*(2*x^2+1)*(p-x^2-2)*(x^2+2) !=0.

The saturation of (7) plus (6) by this open is the unit ideal
over `QQ`. The historical calculation returned zero in 0.407 seconds with maximum
RSS 122,503,168 bytes. The [exact rational input](https://github.com/markluxton1/STCI/blob/934b6bafd7b255f58e3f9b3e93507afb57cb6266/research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_w1.m2) reproduces
(7) and the unit saturation. [Historical run output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_w1.log).

For a primitive cube root, use the exact number field
`QQ[w]/(w^2+w+1)` and keep `a,x`. The actual open is

    a*(2*x^2+1)*(a^2-x^2-2)*(2*a^2-3) !=0.

The same first-unit elimination followed by adding (6) and
saturating this open again returns the unit ideal. It completed
with return code zero in 1.242 seconds with maximum RSS 283,295,744
bytes. The [exact number-field input](https://github.com/markluxton1/STCI/blob/934b6bafd7b255f58e3f9b3e93507afb57cb6266/research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_primitive.m2) covers both
conjugate primitive roots. [Historical run output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_primitive.log).

Thus all three `w` branches of the generic line component are
excluded, before the complete second obstruction or global cubic
matching is needed. These are exact characteristic-zero
computations on specified coefficient schemes, not finite samples.

## 6. The full nonzero-defect B/C boundary is exactly excluded

With both defects units, `B1=0` forces `B2^3=0`. On closed points
both `B` coefficients vanish; the same statement holds for the
two `C` coefficients. If both `B` and both `C` vanish, the old
diagonal exclusion in
[the preceding continuation](#2026-10-20-conditional-2-12-singular-continuation)
applies. The remaining `B=0` boundary has both `C_i` invertible.
Set `C1=C2=1` by factor scaling. Here `Delta_i=Ai*Di` and
`d_i, Ai+2Di` are units. Equations (2) give

    A2*d2^2+2*D1*d1^2=0,
    2*D2*d2^2+A1*d1^2=0.

Let `rho=d1/d2`. It follows that

    A2=-2*D1*rho^2,
    D2=-A1*rho^2/2,
    d2=rho^2*d1,
    rho^3=1.

After `C_i=1`, the actual torus sends `Ai,Di` to
`Ai/t,Di/t`, so set the unit `D1=1`. Rename `A1=t`, `rho=w`:

    A1=t, D1=1, A2=-2*w^2, D2=-w^2*t/2,
    B1=B2=0, C1=C2=1, w^3=1,
    t*(t^2-4) !=0.                                          (8)

The last open is exactly the nonzero-defect, finite two-component,
two-node open. The universal sixteen first equations are now
linear in twelve unit coefficients and polynomial in one parameter.
Their contraction is `(t-2)` for `w=1`, and `(1)` over
`QQ[w]/(w^2+w+1)` for primitive `w`. Thus (8) is already empty at
first compatibility. The two complete runs returned zero; their
artifact stems are

    ../computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_w1
    ../computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_primitive.

The [rational input](https://github.com/markluxton1/STCI/blob/6bb084487daafca4af85489949a00ce0ef193ece/research/computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_w1.m2) gives `(t-2)` and the
[number-field input](https://github.com/markluxton1/STCI/blob/959d131f7ce23401aa7fbd437739b734d0462fa6/research/computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_primitive.m2) gives `(1)` before torsion.
The first-order contraction proves the exclusion on (8). The
[rational run output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_w1.log) and
[number-field run output](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_singular_continuation2_2026_10_21_boundary_B0_primitive.log) also record the
redundant first-plus-torsion unit calculation.

The historical outputs of the two line and two boundary calculations
were reproduced with `M2 --script` on the four linked inputs from the
repository root.

The `C=0` boundary is covered by the **actual** coordinate reversal
`x0<->x3,x1<->x2` preserving `C0`. Its first normal action in the
accepted balanced frame is

    (u,v) -> z^(-7)*(v/2,2u),
    (A,B,C,D) -> (2D,C/2,2B,A/2).

It exchanges the `B=0` and `C=0` boundaries, preserving `Delta`
and `kappa`. This is not an arbitrary ruling normalization.
Nilpotent structures in the unnormalized boundary equations
cannot hide a nonempty scheme with empty closed-point support;
all schemes here have finite type over the algebraically closed
field. Thus the closed-point cover and exact unit computations
exclude the entire nonzero-defect boundary scheme.

## 7. Precise retained two-node strata

After these exclusions, the nonzero-defect two-node root can only
lie on the generic **conic** component

    B1=B2=C1=1, C2=w, w^3=1,
    Q=2*(x^2+x*y+y^2)+3=0,
    a*(2*x^2+1)*(2*y^2+1) !=0,
    w*A2=-y-a*(2*x^2+1)/(2*y^2+1),

with the original `Delta_1*Delta_2*(T^2-4delta)` also inverted.
The identity on this conic

    (2*x^2+1)/(2*y^2+1)=(x*y-1)/(x^2+2)

is useful: `x^2+2` is already a unit there. Indeed
`(2*y^2+1)*(2*(-x-y)^2+1)=2*(2*x^2+1)*(x^2+2)`.

A bounded `w=1` trial eliminated four first-unit variables and
`A2` before imposing torsion, with all clearing factors retained.
It stopped at its sixty-second cap with exit `-15` and maximum RSS
714,358,784 bytes, before returning an elimination ideal. Its
artifacts have stem
`../computations/conditional_2_12_singular_continuation2_2026_10_21_conic_w1`.
This supplies **no** emptiness, dimension or survival certificate.
The other cube-root branches remain equally unresolved. No
unchanged rerun or larger resource limit is proposed here.

The other surviving two-node stratum is

    kappa_1=kappa_2=0,

including all its B/C and endpoint boundaries, with the quadric
direction component removed. Each factor satisfies

    (Ai+2Di)*((Di-Ai/2)^2+Bi*Ci/2)=0.

By (1), there is then a unique actual global cubic `Hi` with
symbol `alpha_i*li`; the cubic symbol map is injective. Thus the
ENTIRE allowed global sextic family on this stratum has the form

    F6=H1*H2+eta*q^3.                                       (9)

This uses the exact kernel `k*q^3` of the sextic symbol map.
An actual supported pair requires `eta!=0`: if `eta=0`, its
degree-six equation has cubic factors, contradicting the
factor-reduction and lower-carrier consequences explicitly stated
in [R-0001](../results/quartic_carrier_exclusion.md). Formula (9)
does not establish normality, global realization, or emptiness
when `eta!=0`. It gives a concrete cubic-product pencil for the
remaining global cubic-jet condition.

## 8. First unresolved lifting conditions and actual-pair boundary

On the conic and zero-defect strata, impose the first incidence,
the complete twenty-five second pairings and the actual spectral
equation (6), along with the forced multiplier. The first
unresolved global lifting test is still

    [F3-alpha*G0] mod(f)=0

with ACTUAL global sextic coefficients. The compact exported
forty-eight syzygy equations implement it without dividing by any
coefficient of `f` or by `alpha`; on (9) its only remaining
sextic freedom is the nonzero scalar `eta`. Later root or sextic
lifts, actual degree-sixteen coefficients, the full degree-twelve
standard-basis certificate and its coprimality, and the global
gcd/Bezout argument remain necessary. None of the reduced schemes
in this note is asserted nonempty or realized.

## 9. Metadata correction and evidence boundaries

Independent review found a naming defect in an earlier generic two-node
metadata export: its
`norm_symbol_equations` strings were formatted after the exporter
mutated its display-name array for the later line exports. The
original-coordinate `.m2` equations were formatted BEFORE that
mutation and are correct; all completed calculations use those
mathematical input files. The old JSON strings are not equation
authority. The [exporter](../computations/conditional_2_12_singular_continuation_2026_10_21.py)
now captures the original-coordinate equation strings before renaming the
display variables, so its metadata agrees with the actual equation source. This metadata repair leaves every generated
M2 mathematical input unchanged and does not repair or resolve the separate
FIRST-residual discrepancy in the reconciliation dossier.

The old generic mixed-cube-root line trial returned a large first
Groebner basis but was stopped before a torsion result; it is not
used as an exclusion. Splitting `w=1` and the primitive quadratic
field, suppressing large intermediate output and eliminating
linear unit variables first produced the completed certificates
in section 5. The proof depends on their exact inputs and returned
unit ideals, not on the interrupted trial or an equation count.


---

## 2026-10-21-conditional-2-12-cubic-image-and-conductor-interface

# The cubic image and the anticanonical conductor interface

Status: **independently reviewed conditional proof in the actual-pair scope**. The fixed curve is C0, and the antecedent is an actual sole-support degree-(6,16) pair with full generic initial CI (2,12) and actual saturated movement-two first relation. The proof does not assert that this antecedent is realized, nor emptiness of the remaining incidence.

## 1. Explicit cubic image

Put q=x0*x3-x1*x2, A=x0^2*x2-x1^3,
B0=x0*x2^2-x1^2*x3, D0=x2^3-x1*x3^2. The seven cubics

    q*x0,q*x1,q*x2,q*x3,A,B0,D0

generate I_C0(3). They define the line bundle L=3H-E on
B=Bl_C0(P3), and a morphism phi:B->P6. The pair of maps given by
H and L is the graph closed immersion B->P3 x P6: the seven cubics
give the usual relative Proj embedding of the Rees algebra, after
twisting by O(3). In particular H+L is ample.

In P6 with coordinates y0,...,y6, the image is cut out by

    y0*y5-y2*y4+y1^2,
    y0*y6-y2*y5+y1*y3,
    y1*y5-y3*y4+y0*y2,
    y1*y6-y3*y5+y2^2,
    y4*y6-y5^2+y1*y2.                                  (1)

The new exact M2 calculation
[cubic-image verifier](https://github.com/markluxton1/STCI/blob/934b6bafd7b255f58e3f9b3e93507afb57cb6266/research/computations/conditional_2_12_cubic_image_2026_10_21.m2)
checks the following over QQ:

* substituting the seven displayed cubics makes all five equations zero;
* their quotient ring has dimension four and degree five;
* the affine singular locus is zero-dimensional (only the cone vertex),
  so their projective threefold V is smooth;
* the quotient has free resolution with ranks (1,5,5,1) and shifts
  (0,2,3,5).

The resolution proves arithmetically Cohen--Macaulay, type one, with
canonical sheaf omega_V=O_V(-2). It also gives H0(O_V)=k, so V is
connected. A smooth connected projective scheme here is integral.
The cubic map is birational onto its image because off q=0 the first
four cubics recover [x0:x1:x2:x3]. Its image is closed, dimension
three, and contained in integral V of dimension three, hence equals V.
The same statements base-change to every characteristic-zero field.

## 2. An explicit blowup identification

Let Gamma be the conic cut out on V by y0=y1=y2=y3=0; equation (1)
leaves y4*y6-y5^2=0 in P2, so Gamma is smooth. The inverse rational
map V-->P3 is the projection [y0:y1:y2:y3]. Its graph closure is
Bl_Gamma(V), since its base ideal on V is exactly the ideal generated
by these four sections, whose scheme of zeros is Gamma.

Under the graph closed immersion B->P3 x V, the image is exactly this
graph closure: on the dense open q!=0 it is the graph of the inverse
birational maps, and B is integral and the graph embedding is closed.
Thus

    B = Bl_Gamma(V).                                    (2)

The exceptional divisor of (2) is Q'=2H-E=L-H, the strict transform
of the original smooth quadric. Indeed the common zero divisor of
the four pullback sections y0,...,y3 is Q': each section is the strict
q factor times x_i, and the four x_i have no common zero. The map
Q'->Gamma is the contraction of one ruling, with degree-two image
polarization. This proof needs no classification theorem for V5.

## 3. The actual sextic descends to an anticanonical surface

The exact 23-element source basis in
[the symbol computation](rank_strata_and_sextic_lifts.md#2-the-exact-global-k-linear-symbol-map)
consists of products of the seven cubics. Consequently every actual
sextic in H0(I_C0^2(6)) gives a quadric section T of V with

    D=phi^* T,              O_V(T)=O_V(2),
    omega_T=O_T.                                     (3)

For an actual supported pair, F6 cannot have Q as a component, by
the quadric Picard argument in
[the quadric-factor exclusion](../synthesis/normalization_conductor_phase2_addendum.md#the-quadric-direction-is-not-a-root-component).
Thus D has no Q' component, T does not contain Gamma, and D is the
strict transform as well as total pullback of T. Off Q', phi is an
isomorphism, so local normalizations and conductors there transfer
between D and T unchanged.

For the remaining conductor discussion one needs T integral. This
follows within the actual supported-pair scope from the accepted
exclusion of all carriers of degree at most four. Every irreducible
factor of F must contain C: otherwise its positive-degree intersection
with G gives a curve outside C. Each such factor is itself a supported
carrier for C with mate G. Hence each has degree at least five. A
sextic can have only one such factor and no higher power, so F, D,
and T are integral. This use of the lower-carrier exclusion must be
checked against its literal canonical hypotheses before applying the
conductor claim; it is not needed for (1)-(2).

## 4. Full conductor of a Gorenstein anticanonical surface

The [conductor-duality proof](rank_strata_and_sextic_lifts.md#3-full-conductor-duality-and-component-genus-independent-review-pass) applies to the integral
Gorenstein anticanonical surface with trivial dualizing sheaf. It identifies
the full upstairs conductor ideal with the canonical module of the
normalization. If nonempty, its conductor scheme Delta is a pure
Cohen--Macaulay curve with trivial dualizing sheaf, hence
`chi(O_Delta)=0` by Serre duality. Each integral component of generic
multiplicity one has arithmetic genus at most one, including when other
components are nonreduced. The proof allows a non-Gorenstein normalization
and a non-Cartier conductor.

A local model forcing a generically reduced conductor branch with delta
invariant at least two therefore needs a separate analysis of whether that
branch maps onto a conductor component after the contraction. The
[ramified-simple-zero argument](#5-the-contracted-ruling-fiber-case) checks
this issue in its stated setting.

## Reviewed actual-pair scope

The seven cubic coordinates, five quadrics, graph/base-ideal blowup construction and full conductor duality above were independently reconstructed in the actual sole-support (6,16), full generic (2,12), saturated movement-two setting. The [stronger conductor continuation](rank_strata_and_sextic_lifts.md#2026-10-21-conditional-2-12-surface-audit-cont2) retains the critical-value unit argument, monic local normalization, component-genus refinement and explicit rejection of the nonfinite nodal model. The argument does not assert that an abstract low-order incidence point supplies an actual global pair, nor does it close the remaining exceptional strata.

## 2026-10-21-conditional-2-12-conductor-ramification

# Conditional (2,12;6,16;2): conductor control at a ramified simple multiplier zero

Date: 2026-10-21. Author: `conductor_budget` worker.

Status: **reviewed conditional conductor and ramification argument**. The anticanonical contraction hypothesis used below is established for the actual-pair scope in the preceding cubic-model proof and the stronger continuation. The local monic normalization and critical-value argument retain their explicit hypotheses. The nodal nonfinite attempted normalization is rejected as explained in section7. No global pair, full incidence-emptiness certificate or general nonnormal-surface bound is claimed.

## 1. Exact scope and source boundary

Use the same actual-pair hypotheses as the reviewed
[surface-bound proposal](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus): an actual
homogeneous supported pair of degrees `(6,16)`, full generic coprime initial CI
of degrees `(2,12)`, and actual saturated movement-two first relation, over an
algebraically closed field of characteristic zero. The inputs are
[R-0010](../results/saturated_first_relation_normal_flatness.md) and
[R-0011](../results/moving_nonreduced_spectral_root_obstruction.md); the finite
singular-root bridge remains the reviewed dependency in
[the singular-gluing proposal](../supplements/SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md).

Put `B=Bl_C0(P3)`, `L=3H-E`, and `Q'=2H-E=L-H`. The strict sextic is
`D in |2L|`, and `K_D=Q'|D`. In this note **D is assumed integral**. At a root
point above a zero of the base multiplier `alpha`, the actual finite bridge
and invertible generator change give

    F'=A*p+t^10*U,       U a unit,       p=G16/t^2 up to a unit,       (1)

where `t=0` cuts out `E`. On `E`, the coefficient of `p` is `alpha/beta`;
`beta` is a unit at a zero of `alpha`. Thus a simple zero of `alpha` on the
BASE gives `A|E=z` up to a unit, with `z` a local base parameter. This does
not assert that the pullback divisor on the double root cover is reduced.

The reduced root `Z` has bidegree `(2,2)`. The full spectral condition removes
the cuspidal and tangent-component strata, retaining smooth integral,
integral nodal, and two-node reducible roots, with their actual gluing data.
No earlier first or second obstruction computation is repeated here.

The global canonical-ideal facts used below are specializations of finite
duality and codimension-one adjunction. A primary reference is Miles Reid,
[Nonnormal del Pezzo Surfaces, section 2](https://ems.press/content/serial-article-files/40537).
Only those general duality facts are used; the del Pezzo classification and
its antiample hypotheses are not transferred to the present situation.

## 2. The conductor of a Gorenstein surface with trivial dualizing sheaf

The [full proof](rank_strata_and_sextic_lifts.md#3-full-conductor-duality-and-component-genus-independent-review-pass) shows that the nonempty conductor
of the normalization of an integral projective Gorenstein surface with
trivial dualizing sheaf is a pure Cohen--Macaulay curve with trivial
dualizing sheaf. It also proves that an integral component of generic
multiplicity one has arithmetic genus at most one. An intrinsically
unibranch point of delta invariant two on such a component is therefore
impossible. This holds when other conductor components are nonreduced.

## 3. Explicit global contraction hypothesis

For the application below, assume a morphism

    psi:B -> Y0

with ALL the following properties:

* `Y0` is a smooth projective threefold, with an ample class `M`;
* `psi` is birational and is an isomorphism off `Q'`;
* `Q'=P1 x P1`, with normal bundle `O(1,-1)`, is its exceptional divisor;
  `psi` contracts exactly the ruling fibers on which `L|Q'=O(2,0)` has
  degree zero;
* `psi^*M=L`, `K_Y0=-2M`, and the integral `D in |2L|` is the pullback of
  an integral `T in |2M|`.

Then `T` is Gorenstein with trivial dualizing sheaf. The expected target is
the degree-five del Pezzo threefold in `P6`. **This note does not establish
that contraction or the descent of every section of `2L`. They are required
bridges, not consequences of the numerical identities alone.**

Let `Y_D` and `Y_T` be the normalizations of `D` and `T`. The morphism
`Y_D->T` factors through a proper birational map `Y_D->Y_T`. A conductor
component `R_D` whose image curve in `B` is not contracted by `psi` maps
finite birationally onto a conductor component `R_T`: away from `Q'` the
ambient morphism is an isomorphism. Generic conductor multiplicity one is
preserved. For proper integral curves a finite birational map gives

    p_a(R_T) >= p_a(R_D).                                    (6)

Consequently the genus bound of section 2 applies to every such
NONCONTRACTED component. Contracted exceptional ruling fibers require a
separate argument; section 5 supplies one for the particular local germ
arising below.

## 4. Exact local normal form at a ramified simple base zero

Assume `Z` is smooth at `x`, its degree-two map to the base is ramified
there, and `alpha` has a simple zero on the base. In completed local
coordinates one may arrange

    A|t=0 = z times a unit,       p|t=0 = (z-w^2) times a unit.

Both `A` and `p` are regular in `z`. By formal Weierstrass division,

    A=a*(z-a0(w,t)),       p=b*(z-p0(w,t)),

where `a,b` are units, `a0(w,0)=0`, and `p0(w,0)=w^2` after the allowed
coordinate choices. Divide (1) by `ab`, center the `z` coordinate, and put
`s=(p0-a0)/2`. This gives

    F'=z_c^2-s(w,t)^2+t^10*V(z_c,w,t),       V a unit.

Its `z_c`-critical section `c(w,t)` lies in `(t^10)`. Parameter-dependent
formal completion of the square gives an actual formal coordinate `x` and
unit `u(w,t)` with

    F'=x^2-B(w,t),
    B=s(w,t)^2-t^10*u(w,t),       s(w,0)=w^2/2.              (7)

Indeed the critical value differs from `-s^2` by `t^10` times a unit;
`c^2/t^10` is divisible by `t^10`, so the unit remains a unit. Formal square
roots of units exist in characteristic zero over the algebraically closed
field. Hence

    B=B_-*B_+,       B_-=s-t^5*sqrt(u),   B_+=s+t^5*sqrt(u). (8)

Each factor is Weierstrass of degree TWO in `w`. They have no common
irreducible factor: any common factor would divide `t^5`, but neither
factor is divisible by `t`.

A double-cover hypersurface `x^2=B` in characteristic zero is normal
exactly when `B` is squarefree. Thus nonnormality at this germ forces one
factor, say `B_-`, to have the form

    B_-=e*d^2,       d=w-phi(t),       e a unit.              (9)

The other factor cannot also be a square. If `B_+=e2*d2^2`, restriction to
`d=0` would make `t^5` times a unit a square in `k[[t]]`, impossible because
its valuation is odd. It follows that `B_+` is reduced, and

    B_+|d=0 = t^5 times a unit.                              (10)

After absorbing `sqrt(e)`, the normalization is

    Y_local: y^2=B_+(w,t),       x=d*sqrt(e)*y.

This is normal, because `B_+` is reduced. Write `R=k[[w,t]]`; the original
ring and its normalization have presentations

    R + d*R*y  subset  R + R*y.

Their conductor is EXACTLY `d*(R+R*y)`: multiplication by `y` forces both
coefficients of a conductor element to be divisible by `d`. Consequently
the conductor curve germ is

    d=0,       y^2=t^5 times a unit.                         (11)

It is reduced, irreducible, of generic multiplicity ONE, and has
`delta=2`. Thus its global reduced conductor component has arithmetic
genus at least two.

Under the contraction hypothesis of section 3, if the corresponding
nonnormal curve is not contracted, (6) and the genus-one bound contradict
(11). This argument includes the case where the particular point lies on
`Q'`; a noncontracted conductor curve still maps finite birationally.

## 5. The contracted ruling-fiber case

Suppose the nonnormal curve in section 4 is a ruling fiber `W` contracted
by `psi`. On `B` one has

    N_(W/Q')=O_W,       N_(Q'/B)|W=O_W(-1).

The normal sequence splits since `H^1(P1,O(1))=0`, so

    N_(W/B)=O_W + O_W(-1),       O_B(D)|W=O_W.                (12)

The equation of `D` vanishes to order at least two along `W`. Its quadratic
normal cone is a global section of
`Sym^2(N_(W/B)^*) tensor O_B(D)|W`. Its discriminant is therefore a section

    disc(q2) in H^0(W,(det N_(W/B)^*)^2 tensor O_B(2D)|W)
             = H^0(P1,O(2)).                               (13)

The local normal form (9)--(10) is an ordinary transverse double crossing at
the generic point of `W`, so this discriminant is nonzero. In the local
coordinates `(x,d)` normal to `W`, its quadratic form is

    q2=x^2-t^5*unit*d^2.

Here `t` is a uniformizer on `W`, since `W=(x,d)` and `d=w-phi(t)`. The
discriminant thus vanishes to order FIVE at the point. That contradicts
(13), whose total zero degree is two. This excludes the contracted case
without applying the anticanonical conductor genus bound to a contracted
curve.

Combining sections 4 and 5 gives the following conditional conclusion:

> Subject to the contraction bridge in section 3, no nonnormal curve of
> the integral strict sextic can pass through a smooth ramification
> point of the root where alpha has a simple zero on the base.

At a smooth UNRAMIFIED root over a simple base zero, `(A,p,t)` are regular
coordinates; the germ is an isolated `A9` singularity. It contributes no
nonnormal curve. Thus the word "ramified" is now removed from the generic
simple-base-zero exception, but repeated base zeros and root nodes remain.

## 6. Conditional residual locus with squarefree alpha

The following consequence uses only the actual finite bridge, the local
conclusion above, the ampleness of `G'=16H-2E=10H+2L`, and the preceding
normal-strict-sextic exclusion. Ampleness follows if `H` and `L` give the
closed graph embedding into `P3 x P6`; that graph property is part of the
same geometric bridge and must be checked separately.

Suppose `alpha` is squarefree on the BASE and is nonzero at every singular
point of `Z`. Along `E` away from `Z`, the equation `F'|E=alpha*f` has
nonzero derivative in the base direction whenever it vanishes; hence `D`
is smooth there. At smooth root points over `alpha=0`, sections 4--5 and
the unramified `A9` calculation exclude any nonnormal curve. At smooth
root points where `alpha` is a unit, `D` is smooth.

A nonnormal curve `Sigma` would therefore meet `E` only at root nodes where
`alpha` is a unit. It cannot be contained in `E`, since the preceding
singular points in `E` are finite. At such a node one may take `p=F'`, and
parameter-dependent Morse coordinates give

    p=X*Y+h(t).

A singular curve exists there only if `h=0` identically, and its local
parameter is then `t`. Thus every such intersection with `E` is transverse.
There are at most two root nodes in the retained spectral strata. Put

    d=H.Sigma,       n=E.Sigma,       1<=n<=2.

The strict second equation restricts to `t^10` times a unit at each node,
and its intersection with `D` has sole support `Z`; hence

    (16H-2E).Sigma=10*n.

It follows that `16d=12n`, or `4d=3n`, impossible for integral `d>=1` and
`n=1,2`. A curve with `H.Sigma=0` would lie in an exceptional `E`-fiber,
already excluded. Thus `D` has no nonnormal curve, so its integral
hypersurface is normal. The existing normal-strict-sextic exclusion then
applies.

Accordingly, conditional on the geometric bridges and the normal-surface
proposal, an actual pair with integral strict sextic must satisfy at least
one of

    alpha has a repeated zero on the base;
    alpha vanishes at a root node.                           (14)

This is an exact exceptional-locus restriction, not a proof that its
remaining locus is empty. In particular it does not replace the actual
nodal or two-node gluing conditions by normalization data.

## 7. Exact local escape at a root node

**Correction flagged by independent reviewer `surface_bound` on 2026-10-21:**
the displayed map below obtained by adjoining `y=w/(z-t^3)` is NOT finite
at the origin: its fiber there contains the affine `y`-line. Consequently
it is not the finite normalization, and the ensuing assertions about its
conductor and normalization singularities must not be used. The equation
`F=z*p+t^10` and the existence of its nonnormal curve remain correct local
countermodels. The correction and a genuinely integral normalization
candidate are recorded in
[the continuation audit](rank_strata_and_sextic_lifts.md#2026-10-21-conditional-2-12-surface-audit-cont2).
This defect is confined to the nodal example; sections 2--6 use the monic
`x^2` normalization calculation and do not divide by a nonunit coefficient.

The local calculations do not remove the second stratum in (14). For
example

    F=z*w^2-(z-t^3)^2*(z-t^4)
      = z*p+t^10,

where

    p=w^2-z^2+z*t^4+2*z*t^3-2*t^7-t^6.

On `t=0`, the full root is the ordinary node `p=w^2-z^2`, and the base
multiplier is the simple zero `alpha=z`. The surface is nonnormal along

    W: w=0, z=t^3,

which leaves E. The attempted parametrization

    y=w/(z-t^3), z*(y²−1)=−t^4

is not finite at the origin: its fiber there contains the affine y-line. It therefore supplies neither the finite normalization nor a conductor or normalization-singularity calculation. The valid content is the displayed local surface equation and its nonnormal curve; it is not an actual globally allowed sextic or a supported pair. A monic integral extension candidate, whose normality and exact conductor are still to be verified, is retained in the stronger continuation.

Repeated zeros of `alpha` are likewise genuinely unresolved. A gap-ten
term alone does not force transverse singularity `z^m+t^10` along a
nonnormal curve. For example `p*(z^2+t^2)+t^10` has a generic ordinary
double transverse singularity along `z=t=0`, with conductor cost two,
rather than the cost ten of `p*z^2+t^10`. A conductor-degree budget by
itself does not exclude these strata.

## Remaining actual-equation incidence

The actual anticanonical contraction and reviewed monic ramification exclusion do not settle the multiple-base-zero or nodal-contact strata. Retain the forced norm multiplier, all first and second ambient equations, full spectral gluing and actual homogeneous coefficient lifting. None of the local escape models constructs a point of that full incidence, a degree-twelve standard basis, or a proper degree-sixteen mate.

## 2026-10-21-conditional-2-12-conductor-and-chart-independent-review

# Independent review: cubic contraction, conductor and realization charts

Date: 2026-10-21. Reviewer: `incidence_audit` worker.

Status: **PASS for the scoped bridges and chart exclusions described
below; no full conditional emptiness claim.**
This review uses saved source notes and executable certificates, not
unsaved worker conclusions. All actual-pair implications retain the
fixed `C0`, characteristic zero, degrees `(6,16)`, FULL generic coprime
ordinary initial CI `(2,12)`, ACTUAL saturated movement-two first
relation, and sole reduced support `C0`.

## 4. Tiny free-orbit unit certificate and its exact coverage

The persisted new audit

The archived command uses [conditional_2_12_cont2_independent_unit_audit_2026_10_21.py](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.py) from the pinned repository snapshot.

    python3 research/computations/conditional_2_12_cont2_independent_unit_audit_2026_10_21.py

was run successfully. It compares the full-cubic residuals from
the saved 48-equation source with the candidate residual set
after exact specialization and polynomial reduction; it also
checks the following identity without a Groebner basis. Put

    P=648h^4+45h^2-4,
    E4=3eta/4+369h/16-891h^3/2,
    E8=eta/8+27h/32-81h^3/4.

Then `E4-6E8=18h-324h^3`, and identically over QQ,

    1=((162h^2-1)/4)*P
        +(81h^3+77h/8)*(E4-6E8).

Thus the exact candidate family cannot satisfy the full global
sextic cubic lift, independently of the second ambient or Picard
tests. This is a polynomial unit identity, not just exclusion of
four numerical approximations.

The [lightweight exact family verifier](https://github.com/markluxton1/STCI/blob/8775cf615047b7a878c436eab7bd9b0a0f039190/research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.m2)
was also run successfully, as recorded in its
[historical successful run record](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_free_orbit_certificate.json).
It checks both exact ideal containments by rational normal forms,
with dimension zero and degree four, between the saved
first/quadric-cubic family ideal and the triangular ideal defining `P=0`. This bridges the tiny identity
back to the entire displayed family, rather than just checking
that the four candidate points solve necessary equations.

Coverage was audited separately:

* The normalization `d0=d4=1` uses projective root scaling and
  the actual `C0`-preserving torus. Choosing a fourth root of a
  nonzero ratio gives a finite faithfully flat cover of the
  nonzero-endpoint chart. It covers no endpoint-zero root.
* On that chart, multiplication by the norm complement in
  `k[z]/(D)` has determinant `81*detJ^2`. Thus `detJ!=0` is
  exactly the absence of collisions between roots in different
  rotated cubic-ruling positions. It need not make `D`
  squarefree: repeated roots of `D` with no rotated collision
  are INCLUDED in this exclusion.
* The smaller differentiated quadric test is equivalent to the
  all-strata test precisely on this open: both `z` and the
  multiplier are units in `k[z]/(D)`. No inverse of `D'` is
  used, so repeated roots are not accidentally lost.
* The eight-variable family keeps all four first-correction
  variables. Its ideal-equality and tiny unit certificates do
  not require the separate four-row Schur pivot determinant.
  Hence pivot-rank-drop points on this free-orbit chart are
  included.

An old October 20 printed Schur matrix omitted the
term `-d1*d3` in its middle diagonal entry. The October 21
exporters used for these certificates contain that term. The
old printed formula must not be used to redefine this chart.

**PASS on `d0*d4*detJ!=0`; no endpoint or orbit-collision
emptiness follows from this certificate.**

## 5. Endpoint multiplicity lemma and two exact normal forms

Here is an additional actual-pair reduction, independently checked
at the root agent's request. Write `tau=f(-z/2,1)` and assume
`m=ord_0(tau)>0`. The norm lemma gives residual divisor
`R=b^m*unit` on the quadric chart `(z,b)`, where
`C0:b=z^3`. The residual mate divisor `T` has restriction of
degree ten to the ruling `b=0`. It cannot contain that ruling;
actual sole support forces its zero divisor on the ruling to
be precisely ten times its sole intersection point with `C0`.
Thus `T(z,0)=z^10*unit`.

The actual ideal equality on the strict quadric is

    (R,T)=(p,t^10),             t=b-z^3.

Reduce it modulo `b`. The left side becomes `(z^10)`, while
the right side is `(p(z,0),z^30)`. Hence

    ord_z p(z,0)=10.

Substitution `b=z^3` changes a regular power series by an
element of `(z^3)`, so `p(z,z^3)` is divisible by `z^3`.
Its order is exactly `m`, since the exceptional restriction of
`p` is a unit multiple of the saturated root equation. Therefore

    ord_0(tau)>=3.

The same argument in the opposite homogeneous chart gives
`ord_infinity(tau)>=3` whenever that order is positive. A
nonzero binary quartic cannot satisfy both inequalities. Thus,
up to the actual projective/torus scaling and inversion of
`C0`, every remaining endpoint root has one of the two forms

    tau=z^3*(1+z),       or       tau=z^4.

The multiplicity-three case has a nonzero remaining finite
root; a remaining root at infinity would violate the second
endpoint inequality. Torus scaling moves that finite nonzero
root to `-1`. These reductions do not assume the endpoint
multiplier is nonzero and do not divide by it.

**Review outcome:** PASS for the endpoint lemma within the
actual supported-pair scope. It is a finite chart reduction,
not exclusion of either resulting chart. Together with section
4 it leaves the nonzero-endpoint orbit-collision chart and the
two endpoint normal forms for the structured computation.

## 6. Fourth-order endpoint: the retained root and exact nodal modulus

On the endpoint chart `D=4tau=z^4`, the symbol equations give

    a=a0+2b2*z+z^2,
    b=b1*z+b2*z^2,
    c=(b1/2-a0/4)*z^2,
    a0!=0.

The root meets the smooth quadric-direction diagonal only at
`p=(z,w)=(0,0)`, with total intersection length four, where
`w=-2u/v`. It cannot be a reduced two-component survivor: each
`(1,1)` component would meet that diagonal with total degree two,
all at `p`, and would consequently be tangent to the diagonal.
The two smooth components would be tangent to each other, the
already excluded additive Picard stratum. A diagonal component
itself is forbidden by `tau!=0`.

Hence any retained endpoint-four root is integral nodal. Its
tangent quadratic is

    (u+z*v/2)*(a0*u+(b1-a0/2)*z*v).

The two slopes `dw/dz` are therefore

    1,       rho=2*b1/a0-1.

They are nonzero and distinct on the retained open. Distinctness
is the nodal condition. If `rho=0`, the displayed coefficient
`c` is zero identically and the binary root has a constant
direction component, violating finiteness in both rulings.

To check that the modulus is the actual Picard gluing, let the
normalization ruling maps be `z=X1/X0` and `w=Y1/Y0`, each of
degree two. Their degree-two numerators vanish at both node
preimages, so `Y1=c*X1`. Their local slope ratios are
`r_i=c*X0(i)/Y0(i)`. On the other hand the actual identification
of `O_Z(1,-1)` at the two preimages gives

    lambda=Y0(p)*X0(q)/(X0(p)*Y0(q))=r_q/r_p.

Thus `lambda=rho` up to inversion, with no normalization-degree
substitution for the conductor identification. The exact spectral
condition on this chart is

    (2*b1/a0-1)^12=1,           2*b1/a0-1 !=1.

After clearing the unit denominator this is
`(2*b1-a0)^12-a0^12=0` on the stated open. This is a necessary
torsion equation, not an exclusion of its intersection with K1
or higher global lifts. The argument was independently
reconstructed from the root agent's proposed endpoint reduction.


### Retired source certificate: `research/computations/conditional_2_12_cubic_image_2026_10_21.m2`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```macaulay2
-- New exact cubic-image calculation. No actual pair is constructed.
R=QQ[y0,y1,y2,y3,y4,y5,y6];
I=ideal(y0*y5-y2*y4+y1^2,
        y0*y6-y2*y5+y1*y3,
        y1*y5-y3*y4+y0*y2,
        y1*y6-y3*y5+y2^2,
        y4*y6-y5^2+y1*y2);
assert(dim(R/I)==4);
assert(degree(R/I)==5);
singIdeal=I+minors(3,jacobian gens I);
assert(dim(R/singIdeal)==0);
F=res(coker gens I);
assert(length F==3);
assert(degrees F_1==toList(5:{2}));
assert(degrees F_2==toList(5:{3}));
assert(degrees F_3=={{5}});
S=QQ[x0,x1,x2,x3];
q=x0*x3-x1*x2;
A=x0^2*x2-x1^3;
B=x0*x2^2-x1^2*x3;
D=x2^3-x1*x3^2;
phi=map(S,R,{q*x0,q*x1,q*x2,q*x3,A,B,D});
assert(phi(I)==ideal(0_S));
print("CUBIC_IMAGE_EXACT: projectively smooth threefold, degree5, resolution(1,5,5,1) shifts(0,2,3,5)");
print("CUBIC_SYZYGIES_ZERO: canonical sheaf O(-2), by the codimension3 selfdual resolution");
print betti F;
print("NO_GLOBAL_PAIR_OR_EMPTINESS_CERTIFICATE_CLAIMED");
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_cubic_reduction_2026_10_21_cont2_collision.py`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```python
#!/usr/bin/env python3
"""One-pair mu3 collision chart, retaining its explicit rank-drop boundary.

D=(z-1)(z-omega)(z^2+e*z+ff), monic. On ff*S!=0, norm-symbol
compatibility is the displayed four-parameter family; no arbitrary root
coefficient chart or global sextic search is introduced.
"""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
accepted=HERE/'generalization_quadratic_root_curve_universal_incidence.json'
data=json.loads(accepted.read_text())
first=[]
for row,rhs in zip(data['A_f'],data['d_f']):
    terms=[f'({p})*h{j}' for j,p in enumerate(row) if p!='0']
    first.append('+'.join(terms)+f'-({rhs})')
stem=Path(__file__).with_suffix('')
lines=[
 '-- Generic one-pair collision chart; rank-drop factors explicitly retained.',
 'K=QQ[omega]/ideal(omega^2+omega+1);',
 'R=K[ee,ff,lambda,tt,H4,H5,H6,H7,fi,MonomialOrder=>GRevLex];',
 'd0=omega*ff; d1=omega^2*ff+omega*ee; d2=ff+omega^2*ee+omega; d3=ee+omega^2;',
 'a0=4*tt+2*ee*lambda; a1=d3/2+2*lambda; a2=1;',
 'b0=-d1/4-ff*lambda; b1=4*tt-d2/2+ee*lambda; b2=-d3/4+lambda;',
 'c0=d0/4; c1=d1/8-ff*lambda/2; c2=tt;',
 'h4=H4; h5=H5; h6=H6; h7=H7;',
 'h3=-a0*h5-a1*h4;',
 'h2=-3-a0*h4-a1*h3;',
 'h1=-4*a1+3*b2-a0*h3-a1*h2;',
 'h0=-5*a0+3*b1-a0*h2-a1*h1;',
 'c0Inverse=4*omega^2*fi;',
 'h8=-c0Inverse*(c2*h6+c1*h7);',
 'h9=-9/2-c0Inverse*(c2*h7+c1*h8);',
 'h10=c0Inverse*(-4*c1-3/8*b0-c2*h8-c1*h9);',
 'h11=c0Inverse*(-7/2*c2-3/8*b1-c2*h9-c1*h10);',
 'firstEquations={'+','.join(first)+'};',
 'endpointUnit=ff*fi-1;',
 'S=R[zz];',
 'aa=a0+a1*zz+zz^2; bb=b0+b1*zz+b2*zz^2; cc=c0+c1*zz+c2*zz^2;',
 'DD=(zz-1)*(zz-omega)*(zz^2+ee*zz+ff);',
 'U=d0+d3*zz^3; V=d1*zz+zz^4; W=d2*zz^2;',
 'alphaCanonical=U^2+V^2+W^2-U*V-U*W-V*W;',
 'coeffR=(p,j)->sub(coefficient(zz^j,p),R);',
 'normSymbol=apply(3,j->coeffR(alphaCanonical*aa,3*j+1)-coeffR(alphaCanonical*bb,3*j+2)-(j+1)*coeffR(alphaCanonical*DD,3*j+3)/4);',
 'assert(all(normSymbol,p->p==0));',
 'g30=-(a1*h5+a2*h4)-a2*h5*zz;',
 'g21=-(b1*h5+b2*h4+a1*h11+a2*h10)-(b2*h5+a2*h11)*zz;',
 'g12=-(3/4*a2+c1*h5+c2*h4+b1*h11+b2*h10)-(c2*h5+b2*h11)*zz;',
 'g03=-(3/8*b2+c1*h11+c2*h10)-c2*h11*zz;',
 'GG=g30*(-zz/2)^3+g21*(-zz/2)^2+g12*(-zz/2)+g03;',
 'LL=diff(zz,DD)-12*zz^2*GG;',
 'qlCoefficients=new MutableList from apply(7,j->coeffR(LL,j));',
 'scan(reverse toList(2..6),j->(v:=qlCoefficients#j;qlCoefficients#(j-2)=qlCoefficients#(j-2)-ff*v;qlCoefficients#(j-1)=qlCoefficients#(j-1)-ee*v;qlCoefficients#j=0));',
 'qlineEquations={qlCoefficients#0,qlCoefficients#1};',
 'collisionBoundary=((omega+1)*ee-ff-omega)*(ee^2-ff);',
 'collisionIdeal=ideal join(firstEquations,qlineEquations,{endpointUnit});',
 'print "ONE_PAIR_COLLISION_9VAR_MODEL_READY";',
 '-- Necessity on ff*collisionBoundary !=0. The boundary needs separate charts.',
 '-- No Groebner basis is run by this exporter.',
]
stem.with_suffix('.m2').write_text('\n'.join(lines)+'\n')
out={'status':'new exact collision chart; no emptiness assertion',
     'accepted_first_input_sha256':hashlib.sha256(accepted.read_bytes()).hexdigest(),
     'D':'(z-1)(z-omega)(z^2+e*z+f)',
     'normalization':'torus fixes one collision root to1; projective f scale makesDmonic',
     'symbol_kernel':'(v0,v1,v2)=lambda*(-f,e,1)',
     'deviation_coordinates':'v0=y0+d1/4,v1=y1-4t+d2/2,v2=y2+d3/4',
     'rank_drop_boundary':'S=((omega+1)*e-f-omega)*(e^2-f)',
     'boundary_meanings':['first factor: complete orbit {1,omega,omega^2}',
                          'second factor: residual quadratic itself is a mu3 pair'],
     'qline_condition':'On f*S!=0, exact norm-alpha qline condition is rem_(z^2+e*z+f)(Dprime-12*z^2*G)=0, two equations',
     'variables':['e','f','lambda','t','H4','H5','H6','H7','fInverse'],
     'h_elimination':'Eight accepted first equations solve h0..3,h8..11 usinga2=1,c0=omega*f/4. f*fInverse=1 retains all endpoint-nonzero points.',
     'limitations':'Endpointzero, completeorbit and two-pair boundary separately retained; no globalpair claim.'}
stem.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'model':str(stem.with_suffix('.m2')),'variables':9,'qline_equations':2},indent=2))
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_nodal_normalization_2026_10_21.m2`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```macaulay2
-- New finite-normalization audit of the LOCAL nodal caution family only.
-- It does not construct homogeneous global coefficients or a supported pair.
R=QQ[t,z,w,v];
scan(1..4,n->(
    m:=10-2*n;
    d:=z-t^n;
    e:=z-t^m;
    f:=z*w^2-d^2*e;
    J:=ideal(v^2-z*e,z*w-d*v,v*w-d*e);
    assert(dim(R/J)==2);
    -- Hilbert--Burch: these are all 2x2 minors of a 2x3 matrix,
    -- and height two gives CM. Do not use the length of M2's
    -- nonminimal inhomogeneous resolution as a CM test.
    assert(J==minors(2,matrix{{z,v,d},{v,e,w}}));
    assert(dim(R/(J+ideal(z)))==1);
    -- On z!=0 this is the integral double cover v^2=z(z-t^m).
    -- Hence CM + dimension drop gives an integral ring.
    assert(dim(R/(J+minors(2,jacobian gens J)))==0);
    -- R1 + CM gives normality. v is monic-integral over the original ring.
    assert(eliminate(J,{v})==ideal(f));
    conductor:=J+ideal(d,w);
    expected:=ideal(z-t^n,w,v^2-t^n*(t^n-t^m));
    assert(conductor==expected);
    print("LOCAL_NODAL_FINITE_NORMALIZATION n="|toString n|", m="|toString m|": PASS");
    print("CONDUCTOR_EQUATION: "|toString(v^2-t^n*(t^n-t^m)));
    ));
print("NO_GLOBAL_SEXTIC_OR_PAIR_ASSERTED");
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_primitive.m2`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```macaulay2
-- Exact primitive-cube-root line component over QQ(w), w^2+w+1=0.
K=toField(QQ[ww]/ideal(ww^2+ww+1));
R=K[h4,h5,h6,h7,a,x,MonomialOrder=>Eliminate 4];
w=sub(K_0,R);
firstEquations={1/2*a-1/2*x-8*w*x-w*h6-1/2*w*w*a-1/2*w*w*x-w*a*h7+w*x*h7-1/4*a*a*a+7/4*a*a*x-11/4*a*x*x+5/4*x*x*x+w*w*a*h7+w*w*x*h7+5/2*w*a*a*x-5/2*w*x*x*x-a*a*a*h4-3*a*a*x*h4-3*a*x*x*h4-x*x*x*h4+1/4*w*w*a*a*a+7/4*w*w*a*a*x+11/4*w*w*a*x*x+5/4*w*w*x*x*x+w*a*a*a*h4+1/2*w*a*a*a*h7-3*w*a*a*x*h4-1/2*w*a*a*x*h7+3*w*a*x*x*h4-1/2*w*a*x*x*h7-w*x*x*x*h4+1/2*w*x*x*x*h7-a*a*a*a*h5-2*a*a*a*x*h5+2*a*x*x*x*h5+x*x*x*x*h5-1/2*w*w*a*a*a*h7-1/2*w*w*a*a*x*h7+1/2*w*w*a*x*x*h7+1/2*w*w*x*x*x*h7+1/4*w*a*a*a*a*h6-1/2*w*a*a*x*x*h6+1/4*w*x*x*x*x*h6+1/2*a*a*a*a*a*h4+3/2*a*a*a*a*x*h4+a*a*a*x*x*h4-a*a*x*x*x*h4-3/2*a*x*x*x*x*h4-1/2*x*x*x*x*x*h4-w*w*a*a*a*a*h5+2*w*w*a*a*a*x*h5-2*w*w*a*x*x*x*h5+w*w*x*x*x*x*h5-1/2*w*a*a*a*a*a*h4+3/2*w*a*a*a*a*x*h4-w*a*a*a*x*x*h4-w*a*a*x*x*x*h4+3/2*w*a*x*x*x*x*h4-1/2*w*x*x*x*x*x*h4+1/2*a*a*a*a*a*a*h5+a*a*a*a*a*x*h5-1/2*a*a*a*a*x*x*h5-2*a*a*a*x*x*x*h5-1/2*a*a*x*x*x*x*h5+a*x*x*x*x*x*h5+1/2*x*x*x*x*x*x*h5+1/2*w*w*a*a*a*a*a*a*h5-w*w*a*a*a*a*a*x*h5-1/2*w*w*a*a*a*a*x*x*h5+2*w*w*a*a*a*x*x*x*h5-1/2*w*w*a*a*x*x*x*x*h5-w*w*a*x*x*x*x*x*h5+1/2*w*w*x*x*x*x*x*x*h5,1/2+1/2*w-w*h7-1/4*a*a+3/2*a*x-5/4*x*x-1/4*w*a*a-3/2*w*a*x-5/4*w*x*x-1/2*a*a*h7+a*x*h7-1/2*x*x*h7-3*w*w*x*x-w*a*a*h4+w*a*a*h7+2*w*a*x*h4-w*x*x*h4-w*x*x*h7-1/4*a*a*a*h6+1/4*a*a*x*h6+1/4*a*x*x*h6-1/4*x*x*x*h6-w*w*a*a*h4-1/2*w*w*a*a*h7-2*w*w*a*x*h4-w*w*a*x*h7-w*w*x*x*h4-1/2*w*w*x*x*h7+1/4*w*a*a*a*h6+1/4*w*a*a*x*h6-1/4*w*a*x*x*h6-1/4*w*x*x*x*h6+1/4*a*a*a*a*h7-1/2*a*a*a*x*h7+1/2*a*x*x*x*h7-1/4*x*x*x*x*h7-2*w*w*a*a*x*h5+2*w*w*x*x*x*h5+1/2*w*a*a*a*a*h4-1/4*w*a*a*a*a*h7-w*a*a*a*x*h4+1/2*w*a*a*x*x*h7+w*a*x*x*x*h4-1/2*w*x*x*x*x*h4-1/4*w*x*x*x*x*h7+1/8*a*a*a*a*a*h6-1/8*a*a*a*a*x*h6-1/4*a*a*a*x*x*h6+1/4*a*a*x*x*x*h6+1/8*a*x*x*x*x*h6-1/8*x*x*x*x*x*h6+1/2*w*w*a*a*a*a*h4+1/4*w*w*a*a*a*a*h7+w*w*a*a*a*x*h4+1/2*w*w*a*a*a*x*h7-w*w*a*x*x*x*h4-1/2*w*w*a*x*x*x*h7-1/2*w*w*x*x*x*x*h4-1/4*w*w*x*x*x*x*h7-1/8*w*a*a*a*a*a*h6-1/8*w*a*a*a*a*x*h6+1/4*w*a*a*a*x*x*h6+1/4*w*a*a*x*x*x*h6-1/8*w*a*x*x*x*x*h6-1/8*w*x*x*x*x*x*h6+w*w*a*a*a*a*x*h5-2*w*w*a*a*x*x*x*h5+w*w*x*x*x*x*x*h5,-1/4*w*a+7/4*w*x-1/2*a*h7+1/2*x*h7+1/4*w*w*a+7/4*w*w*x+1/2*w*a*h7-2*w*x*h4+1/2*w*x*h7-1/4*a*a*h6+1/4*x*x*h6+1/8*w*a*a*a+5/8*w*a*a*x-w*a*a*h5-1/8*w*a*x*x-5/8*w*x*x*x+w*x*x*h5+1/2*a*a*a*h7-1/2*a*a*x*h7-1/2*a*x*x*h7+1/2*x*x*x*h7-1/8*w*w*a*a*a+5/8*w*w*a*a*x-w*w*a*a*h5+1/8*w*w*a*x*x-5/8*w*w*x*x*x+w*w*x*x*h5-1/2*w*a*a*a*h7+w*a*a*x*h4-1/2*w*a*a*x*h7+1/2*w*a*x*x*h7-w*x*x*x*h4+1/2*w*x*x*x*h7+1/4*a*a*a*a*h6-1/2*a*a*x*x*h6+1/4*x*x*x*x*h6+3/2*w*w*a*a*x*h7+1/2*w*w*x*x*x*h7+1/2*w*a*a*a*a*h5-1/8*w*a*a*a*a*h6-1/4*w*a*a*a*x*h6-w*a*a*x*x*h5+1/4*w*a*x*x*x*h6+1/2*w*x*x*x*x*h5+1/8*w*x*x*x*x*h6-1/8*a*a*a*a*a*h7+1/8*a*a*a*a*x*h7+1/4*a*a*a*x*x*h7-1/4*a*a*x*x*x*h7-1/8*a*x*x*x*x*h7+1/8*x*x*x*x*x*h7+1/2*w*w*a*a*a*a*h5-1/8*w*w*a*a*a*a*h6+1/4*w*w*a*a*a*x*h6-w*w*a*a*x*x*h5-1/4*w*w*a*x*x*x*h6+1/2*w*w*x*x*x*x*h5+1/8*w*w*x*x*x*x*h6+1/8*w*a*a*a*a*a*h7+1/8*w*a*a*a*a*x*h7-1/4*w*a*a*a*x*x*h7-1/4*w*a*a*x*x*x*h7+1/8*w*a*x*x*x*x*h7+1/8*w*x*x*x*x*x*h7-1/16*a*a*a*a*a*a*h6+3/16*a*a*a*a*x*x*h6-3/16*a*a*x*x*x*x*h6+1/16*x*x*x*x*x*x*h6-3/4*w*w*a*a*a*a*x*h7+1/2*w*w*a*a*x*x*x*h7+1/4*w*w*x*x*x*x*x*h7+1/16*w*a*a*a*a*a*a*h6+1/8*w*a*a*a*a*a*x*h6-1/16*w*a*a*a*a*x*x*h6-1/4*w*a*a*a*x*x*x*h6-1/16*w*a*a*x*x*x*x*h6+1/8*w*a*x*x*x*x*x*h6+1/16*w*x*x*x*x*x*x*h6+1/16*w*w*a*a*a*a*a*a*h6-1/8*w*w*a*a*a*a*a*x*h6-1/16*w*w*a*a*a*a*x*x*h6+1/4*w*w*a*a*a*x*x*x*h6-1/16*w*w*a*a*x*x*x*x*h6-1/8*w*w*a*x*x*x*x*x*h6+1/16*w*w*x*x*x*x*x*x*h6,-1/2*w-h4-w*h4-1/2*a*a-1/2*a*x-a*h5+x*x+x*h5+1/4*w*a*a+5/4*w*x*x+1/2*a*a*h4+1/4*a*a*h7-1/2*x*x*h4-1/4*x*x*h7-1/2*w*w*a*a+1/2*w*w*a*x+w*w*a*h5+w*w*x*x+w*w*x*h5+1/2*w*a*a*h4-1/4*w*a*a*h7-1/2*w*a*x*h7-1/2*w*x*x*h4-1/4*w*x*x*h7+1/16*a*a*a*a+1/4*a*a*a*x+1/2*a*a*a*h5+1/8*a*a*a*h6-3/8*a*a*x*x-1/2*a*a*x*h5+1/8*a*a*x*h6-1/4*a*x*x*x-1/2*a*x*x*h5-1/8*a*x*x*h6+5/16*x*x*x*x+1/2*x*x*x*h5-1/8*x*x*x*h6-1/4*w*w*a*a*h7+1/2*w*w*a*x*h7-1/4*w*w*x*x*h7-1/4*a*a*a*a*h7+1/2*a*a*x*x*h7-1/4*x*x*x*x*h7+1/16*w*w*a*a*a*a-1/4*w*w*a*a*a*x-1/2*w*w*a*a*a*h5-1/8*w*w*a*a*a*h6-3/8*w*w*a*a*x*x-1/2*w*w*a*a*x*h5+1/8*w*w*a*a*x*h6+1/4*w*w*a*x*x*x+1/2*w*w*a*x*x*h5+1/8*w*w*a*x*x*h6+5/16*w*w*x*x*x*x+1/2*w*w*x*x*x*h5-1/8*w*w*x*x*x*h6+1/8*w*a*a*a*a*h7+w*a*a*a*x*h7-3/4*w*a*a*x*x*h7-3/8*w*x*x*x*x*h7-1/8*a*a*a*a*a*h6-1/8*a*a*a*a*x*h6+1/4*a*a*a*x*x*h6+1/4*a*a*x*x*x*h6-1/8*a*x*x*x*x*h6-1/8*x*x*x*x*x*h6+1/8*w*w*a*a*a*a*h7-w*w*a*a*a*x*h7-3/4*w*w*a*a*x*x*h7-3/8*w*w*x*x*x*x*h7+3/8*w*a*a*a*a*x*h6-1/4*w*a*a*x*x*x*h6-1/8*w*x*x*x*x*x*h6+1/16*a*a*a*a*a*a*h7-3/16*a*a*a*a*x*x*h7+3/16*a*a*x*x*x*x*h7-1/16*x*x*x*x*x*x*h7+1/8*w*w*a*a*a*a*a*h6-1/8*w*w*a*a*a*a*x*h6-1/4*w*w*a*a*a*x*x*h6+1/4*w*w*a*a*x*x*x*h6+1/8*w*w*a*x*x*x*x*h6-1/8*w*w*x*x*x*x*x*h6-3/8*w*a*a*a*a*a*x*h7+3/8*w*a*a*a*a*x*x*h7+1/4*w*a*a*a*x*x*x*h7-1/4*w*a*a*x*x*x*x*h7+1/8*w*a*x*x*x*x*x*h7-1/8*w*x*x*x*x*x*x*h7+1/32*a*a*a*a*a*a*a*h6+1/32*a*a*a*a*a*a*x*h6-3/32*a*a*a*a*a*x*x*h6-3/32*a*a*a*a*x*x*x*h6+3/32*a*a*a*x*x*x*x*h6+3/32*a*a*x*x*x*x*x*h6-1/32*a*x*x*x*x*x*x*h6-1/32*x*x*x*x*x*x*x*h6+3/8*w*w*a*a*a*a*a*x*h7+3/8*w*w*a*a*a*a*x*x*h7-1/4*w*w*a*a*a*x*x*x*h7-1/4*w*w*a*a*x*x*x*x*h7-1/8*w*w*a*x*x*x*x*x*h7-1/8*w*w*x*x*x*x*x*x*h7-3/16*w*a*a*a*a*a*a*x*h6+5/16*w*a*a*a*a*x*x*x*h6-1/16*w*a*a*x*x*x*x*x*h6-1/16*w*x*x*x*x*x*x*x*h6-1/32*w*w*a*a*a*a*a*a*a*h6+1/32*w*w*a*a*a*a*a*a*x*h6+3/32*w*w*a*a*a*a*a*x*x*h6-3/32*w*w*a*a*a*a*x*x*x*h6-3/32*w*w*a*a*a*x*x*x*x*h6+3/32*w*w*a*a*x*x*x*x*x*h6+1/32*w*w*a*x*x*x*x*x*x*h6-1/32*w*w*x*x*x*x*x*x*x*h6,1-h7-w*h7-1/2*a*a-5/2*x*x+w*a*a-w*a*x-1/2*w*a*h6-2*w*x*x-1/2*w*x*h6-a*a*h4+1/2*a*a*h7+2*a*x*h4-x*x*h4-1/2*x*x*h7+w*w*a*a+w*w*a*x+1/2*w*w*a*h6-2*w*w*x*x-1/2*w*w*x*h6+w*a*a*h4+1/2*w*a*a*h7-w*x*x*h4-1/2*w*x*x*h7-w*w*a*a*h4-2*w*w*a*x*h4-w*w*x*x*h4-1/8*w*a*a*a*a+1/2*w*a*a*a*x+w*a*a*a*h5+1/4*w*a*a*a*h6+3/4*w*a*a*x*x-w*a*a*x*h5+1/4*w*a*a*x*h6-1/2*w*a*x*x*x-w*a*x*x*h5-1/4*w*a*x*x*h6-5/8*w*x*x*x*x+w*x*x*x*h5-1/4*w*x*x*x*h6+1/2*a*a*a*a*h4-4*a*a*a*x*h4-3*a*a*x*x*h4-3/2*x*x*x*x*h4-1/8*w*w*a*a*a*a-1/2*w*w*a*a*a*x-w*w*a*a*a*h5-1/4*w*w*a*a*a*h6+3/4*w*w*a*a*x*x-w*w*a*a*x*h5+1/4*w*w*a*a*x*h6+1/2*w*w*a*x*x*x+w*w*a*x*x*h5+1/4*w*w*a*x*x*h6-5/8*w*w*x*x*x*x+w*w*x*x*x*h5-1/4*w*w*x*x*x*h6-w*a*a*a*a*h4+2*w*a*a*x*x*h4-w*x*x*x*x*h4-3*a*a*a*a*x*h5+2*a*a*x*x*x*h5+x*x*x*x*x*h5+1/2*w*w*a*a*a*a*h4+4*w*w*a*a*a*x*h4-3*w*w*a*a*x*x*h4-3/2*w*w*x*x*x*x*h4-w*a*a*a*a*a*h5+w*a*a*a*a*x*h5+2*w*a*a*a*x*x*h5-2*w*a*a*x*x*x*h5-w*a*x*x*x*x*h5+w*x*x*x*x*x*h5+3/2*a*a*a*a*a*x*h4+3/2*a*a*a*a*x*x*h4-a*a*a*x*x*x*h4-a*a*x*x*x*x*h4-1/2*a*x*x*x*x*x*h4-1/2*x*x*x*x*x*x*h4+w*w*a*a*a*a*a*h5+w*w*a*a*a*a*x*h5-2*w*w*a*a*a*x*x*h5-2*w*w*a*a*x*x*x*h5+w*w*a*x*x*x*x*h5+w*w*x*x*x*x*x*h5+1/4*w*a*a*a*a*a*a*h4-3/4*w*a*a*a*a*x*x*h4+3/4*w*a*a*x*x*x*x*h4-1/4*w*x*x*x*x*x*x*h4+3/2*a*a*a*a*a*a*x*h5-5/2*a*a*a*a*x*x*x*h5+1/2*a*a*x*x*x*x*x*h5+1/2*x*x*x*x*x*x*x*h5-3/2*w*w*a*a*a*a*a*x*h4+3/2*w*w*a*a*a*a*x*x*h4+w*w*a*a*a*x*x*x*h4-w*w*a*a*x*x*x*x*h4+1/2*w*w*a*x*x*x*x*x*h4-1/2*w*w*x*x*x*x*x*x*h4+1/4*w*a*a*a*a*a*a*a*h5-1/4*w*a*a*a*a*a*a*x*h5-3/4*w*a*a*a*a*a*x*x*h5+3/4*w*a*a*a*a*x*x*x*h5+3/4*w*a*a*a*x*x*x*x*h5-3/4*w*a*a*x*x*x*x*x*h5-1/4*w*a*x*x*x*x*x*x*h5+1/4*w*x*x*x*x*x*x*x*h5-1/4*w*w*a*a*a*a*a*a*a*h5-1/4*w*w*a*a*a*a*a*a*x*h5+3/4*w*w*a*a*a*a*a*x*x*h5+3/4*w*w*a*a*a*a*x*x*x*h5-3/4*w*w*a*a*a*x*x*x*x*h5-3/4*w*w*a*a*x*x*x*x*x*h5+1/4*w*w*a*x*x*x*x*x*x*h5+1/4*w*w*x*x*x*x*x*x*x*h5,1/4*a+7/4*x+a*h4-x*h4+x*h7-1/4*w*w*a+7/4*w*w*x-w*a*h4-w*x*h4-1/8*a*a*a+5/8*a*a*x-1/4*a*a*h6+1/8*a*x*x-5/8*x*x*x+1/4*x*x*h6-w*a*a*h5+w*x*x*h5-a*a*a*h4+a*a*x*h4-1/2*a*a*x*h7+a*x*x*h4-x*x*x*h4+1/2*x*x*x*h7+1/8*w*w*a*a*a+5/8*w*w*a*a*x-1/4*w*w*a*a*h6-1/8*w*w*a*x*x-5/8*w*w*x*x*x+1/4*w*w*x*x*h6+w*a*a*a*h4+w*a*a*x*h4-w*a*x*x*h4-w*x*x*x*h4-1/2*a*a*a*a*h5+1/8*a*a*a*a*h6+a*a*a*x*h5-1/4*a*a*x*x*h6-a*x*x*x*h5+1/2*x*x*x*x*h5+1/8*x*x*x*x*h6-3*w*w*a*a*x*h4-w*w*x*x*x*h4+w*a*a*a*a*h5-2*w*a*a*x*x*h5+w*x*x*x*x*h5+1/4*a*a*a*a*a*h4-1/4*a*a*a*a*x*h4-1/2*a*a*a*x*x*h4+1/2*a*a*x*x*x*h4+1/4*a*x*x*x*x*h4-1/4*x*x*x*x*x*h4-1/2*w*w*a*a*a*a*h5+1/8*w*w*a*a*a*a*h6-w*w*a*a*a*x*h5-1/4*w*w*a*a*x*x*h6+w*w*a*x*x*x*h5+1/2*w*w*x*x*x*x*h5+1/8*w*w*x*x*x*x*h6-1/4*w*a*a*a*a*a*h4-1/4*w*a*a*a*a*x*h4+1/2*w*a*a*a*x*x*h4+1/2*w*a*a*x*x*x*h4-1/4*w*a*x*x*x*x*h4-1/4*w*x*x*x*x*x*h4+1/4*a*a*a*a*a*a*h5-1/2*a*a*a*a*a*x*h5-1/4*a*a*a*a*x*x*h5+a*a*a*x*x*x*h5-1/4*a*a*x*x*x*x*h5-1/2*a*x*x*x*x*x*h5+1/4*x*x*x*x*x*x*h5+3/2*w*w*a*a*a*a*x*h4-w*w*a*a*x*x*x*h4-1/2*w*w*x*x*x*x*x*h4-1/4*w*a*a*a*a*a*a*h5+3/4*w*a*a*a*a*x*x*h5-3/4*w*a*a*x*x*x*x*h5+1/4*w*x*x*x*x*x*x*h5+1/4*w*w*a*a*a*a*a*a*h5+1/2*w*w*a*a*a*a*a*x*h5-1/4*w*w*a*a*a*a*x*x*h5-w*w*a*a*a*x*x*x*h5-1/4*w*w*a*a*x*x*x*x*h5+1/2*w*w*a*x*x*x*x*x*h5+1/4*w*w*x*x*x*x*x*x*h5,-1/4-1/4*w-h4+1/8*a*a-3/4*a*x+5/8*x*x+1/8*w*a*a+3/4*w*a*x+5/8*w*x*x+a*a*h4-1/4*a*a*h7-1/2*a*x*h7-x*x*h4-1/4*x*x*h7+3/2*w*w*x*x-1/2*w*a*a*h4-w*a*x*h4-1/2*w*x*x*h4+1/2*a*a*a*h5-1/2*a*a*x*h5-1/2*a*x*x*h5+1/2*x*x*x*h5-1/2*w*w*a*a*h4-1/4*w*w*a*a*h7+w*w*a*x*h4+1/2*w*w*a*x*h7-1/2*w*w*x*x*h4-1/4*w*w*x*x*h7-1/2*w*a*a*a*h5-1/2*w*a*a*x*h5+1/2*w*a*x*x*h5+1/2*w*x*x*x*h5-1/4*a*a*a*a*h4+1/8*a*a*a*a*h7+1/4*a*a*a*x*h7+1/2*a*a*x*x*h4-1/4*a*x*x*x*h7-1/4*x*x*x*x*h4-1/8*x*x*x*x*h7+1/4*w*w*a*a*x*h6-1/4*w*w*x*x*x*h6+1/4*w*a*a*a*a*h4+1/2*w*a*a*a*x*h4-1/2*w*a*x*x*x*h4-1/4*w*x*x*x*x*h4-1/4*a*a*a*a*a*h5+1/4*a*a*a*a*x*h5+1/2*a*a*a*x*x*h5-1/2*a*a*x*x*x*h5-1/4*a*x*x*x*x*h5+1/4*x*x*x*x*x*h5+1/4*w*w*a*a*a*a*h4+1/8*w*w*a*a*a*a*h7-1/2*w*w*a*a*a*x*h4-1/4*w*w*a*a*a*x*h7+1/2*w*w*a*x*x*x*h4+1/4*w*w*a*x*x*x*h7-1/4*w*w*x*x*x*x*h4-1/8*w*w*x*x*x*x*h7+1/4*w*a*a*a*a*a*h5+1/4*w*a*a*a*a*x*h5-1/2*w*a*a*a*x*x*h5-1/2*w*a*a*x*x*x*h5+1/4*w*a*x*x*x*x*h5+1/4*w*x*x*x*x*x*h5-1/8*w*w*a*a*a*a*x*h6+1/4*w*w*a*a*x*x*x*h6-1/8*w*w*x*x*x*x*x*h6,-2*x-h5-1/8*w*a-1/8*w*x-1/2*a*h4-1/2*x*h4+1/8*w*w*a-1/8*w*w*x+5/8*a*a*x-5/8*x*x*x+1/2*w*w*a*h4-1/2*w*w*x*h4+1/16*w*a*a*a+7/16*w*a*a*x+11/16*w*a*x*x+5/16*w*x*x*x+1/4*a*a*a*h4+1/8*a*a*a*h7+1/4*a*a*x*h4+3/8*a*a*x*h7-1/4*a*x*x*h4+3/8*a*x*x*h7-1/4*x*x*x*h4+1/8*x*x*x*h7-1/16*w*w*a*a*a+7/16*w*w*a*a*x-11/16*w*w*a*x*x+5/16*w*w*x*x*x-1/8*w*a*a*a*h7+3/8*w*a*a*x*h7-3/8*w*a*x*x*h7+1/8*w*x*x*x*h7+1/4*a*a*a*a*h5-1/2*a*a*x*x*h5+1/4*x*x*x*x*h5-1/4*w*w*a*a*a*h4+1/4*w*w*a*a*x*h4+1/4*w*w*a*x*x*h4-1/4*w*w*x*x*x*h4-1/16*w*a*a*a*a*h6+1/8*w*a*a*a*x*h6-1/8*w*a*x*x*x*h6+1/16*w*x*x*x*x*h6-1/16*a*a*a*a*a*h7-3/16*a*a*a*a*x*h7-1/8*a*a*a*x*x*h7+1/8*a*a*x*x*x*h7+3/16*a*x*x*x*x*h7+1/16*x*x*x*x*x*h7-1/16*w*w*a*a*a*a*h6-1/8*w*w*a*a*a*x*h6+1/8*w*w*a*x*x*x*h6+1/16*w*w*x*x*x*x*h6+1/16*w*a*a*a*a*a*h7-3/16*w*a*a*a*a*x*h7+1/8*w*a*a*a*x*x*h7+1/8*w*a*a*x*x*x*h7-3/16*w*a*x*x*x*x*h7+1/16*w*x*x*x*x*x*h7+1/32*w*a*a*a*a*a*a*h6-1/16*w*a*a*a*a*a*x*h6-1/32*w*a*a*a*a*x*x*h6+1/8*w*a*a*a*x*x*x*h6-1/32*w*a*a*x*x*x*x*h6-1/16*w*a*x*x*x*x*x*h6+1/32*w*x*x*x*x*x*x*h6+1/32*w*w*a*a*a*a*a*a*h6+1/16*w*w*a*a*a*a*a*x*h6-1/32*w*w*a*a*a*a*x*x*h6-1/8*w*w*a*a*a*x*x*x*h6-1/32*w*w*a*a*x*x*x*x*h6+1/16*w*w*a*x*x*x*x*x*h6+1/32*w*w*x*x*x*x*x*x*h6};
I=ideal firstEquations;
print("PRIMITIVE_LINE_FIRST_ELIMINATION_START");
E=eliminate({h4,h5,h6,h7},I);
print("PRIMITIVE_LINE_FIRST_ELIMINATION_READY");print gens E;
S=K[a,x];phi=map(S,R,{0,0,0,0,a,x});
ES=ideal phi(gens E);w=sub(K_0,S);
tau=w^2*(1-a^2-x^2);delta=w*((a^2-x^2-2)/2)^2;
q=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);
op=a*(2*x^2+1)*(a^2-x^2-2)*(2*a^2-3);
J=saturate(ES+ideal(q),ideal(op));
print("PRIMITIVE_LINE_FIRST_TORSION_RESULT");print gens gb J;
```
</details>


### Retired source certificate: `research/computations/conditional_2_12_singular_continuation_2026_10_21_line_component_w1.m2`

Historical source retained verbatim, including limitations and external dependencies. Relative file paths in archived code refer to the original repository location.

<details><summary>Original source</summary>

```macaulay2
-- Exact w=1,y=x generic norm component, p=a^2; p nonzero.
R=QQ[h4,h5,h6,h7,p,x,MonomialOrder=>Eliminate 4];
firstEquations={-h6-9*x+2*h7*x+6*p*x-6*h4*p*x-2*h5*p*p+1/4*h6*p*p-h7*p*x+3*h4*p*p*x-2*h4*x*x*x+h5*p*p*p-1/2*h6*p*x*x+h7*x*x*x-2*h4*p*x*x*x-h5*p*p*x*x+2*h5*x*x*x*x+1/4*h6*x*x*x*x-h4*x*x*x*x*x-h5*p*x*x*x*x+h5*x*x*x*x*x*x,1-h7-1/2*p-2*h4*p-11/2*x*x+h4*p*p-2*h4*x*x-2*h5*p*x+1/2*h6*p*x+1/4*h7*p*p-2*h7*x*x+h5*p*p*x+2*h5*x*x*x-1/4*h6*p*p*x-1/2*h6*x*x*x+1/2*h7*p*x*x-h4*x*x*x*x-2*h5*p*x*x*x+1/2*h6*p*x*x*x-3/4*h7*x*x*x*x+h5*x*x*x*x*x-1/4*h6*x*x*x*x*x,7/2*x-2*h4*x-2*h5*p-1/4*h6*p+h7*x+5/4*p*x+h4*p*x+h5*p*p+2*h5*x*x+1/4*h6*x*x+1/2*h7*p*x-5/4*x*x*x-h4*x*x*x-2*h5*p*x*x+1/16*h6*p*p*p-1/2*h6*p*x*x-1/2*h7*p*p*x+3/2*h7*x*x*x+h5*x*x*x*x+1/16*h6*p*p*x*x+1/2*h6*x*x*x*x-5/16*h6*p*x*x*x*x+1/2*h7*x*x*x*x*x+3/16*h6*x*x*x*x*x*x,-1/2-2*h4-3/4*p+h4*p+2*h5*x-1/4*h7*p+1/8*p*p+13/4*x*x-h4*x*x-h5*p*x+1/4*h6*p*x-3/4*h7*x*x-3/4*p*x*x+h5*x*x*x+1/8*h6*p*p*x-1/4*h6*x*x*x+1/16*h7*p*p*p-h7*p*x*x+5/8*x*x*x*x-1/8*h6*p*p*p*x+1/4*h6*p*x*x*x+9/16*h7*p*p*x*x-h7*x*x*x*x+1/8*h6*p*p*x*x*x-3/8*h6*x*x*x*x*x-5/16*h7*p*x*x*x*x+1/8*h6*p*x*x*x*x*x-5/16*h7*x*x*x*x*x*x-1/8*h6*x*x*x*x*x*x*x,1-2*h7+3/2*p-h4*p-h6*x+h7*p-1/4*p*p-13/2*x*x-3*h4*x*x-2*h5*p*x+1/2*h6*p*x-h7*x*x+3/2*p*x*x+1/4*h4*p*p*p-4*h4*p*x*x-h5*p*p*x+2*h5*x*x*x-1/2*h6*x*x*x-5/4*x*x*x*x+9/4*h4*p*p*x*x-4*h4*x*x*x*x+h5*p*p*p*x-2*h5*p*x*x*x-5/4*h4*p*x*x*x*x-h5*p*p*x*x*x+3*h5*x*x*x*x*x-5/4*h4*x*x*x*x*x*x-h5*p*x*x*x*x*x+h5*x*x*x*x*x*x*x,7/2*x-2*h4*x-h5*p-1/2*h6*p+h7*x+5/4*p*x-h4*p*x+h5*x*x+1/4*h6*p*p+1/2*h6*x*x-1/2*h7*p*x-5/4*x*x*x+h4*p*p*x-3*h4*x*x*x+1/4*h5*p*p*p-2*h5*p*x*x-1/2*h6*p*x*x+1/2*h7*x*x*x+1/4*h5*p*p*x*x+2*h5*x*x*x*x+1/4*h6*x*x*x*x-h4*x*x*x*x*x-5/4*h5*p*x*x*x*x+3/4*h5*x*x*x*x*x*x,-1/2-h4+1/4*p-1/2*h7*p+11/4*x*x+1/4*h4*p*p-2*h4*x*x-h5*p*x+1/4*h6*p*x+1/4*h7*p*p-1/2*h7*x*x+1/2*h4*p*x*x+1/2*h5*p*p*x+h5*x*x*x-1/8*h6*p*p*x-1/4*h6*x*x*x-3/4*h4*x*x*x*x-h5*p*x*x*x+1/4*h6*p*x*x*x-1/4*h7*x*x*x*x+1/2*h5*x*x*x*x*x-1/8*h6*x*x*x*x*x,-h5-9/4*x-h4*x+3/2*p*x+1/2*h4*p*x+1/4*h5*p*p-1/8*h6*p*p+3/4*h7*p*x-1/2*h4*x*x*x-1/2*h5*p*x*x+1/16*h6*p*p*p-3/8*h7*p*p*x+1/4*h7*x*x*x+1/4*h5*x*x*x*x-1/16*h6*p*p*x*x+1/8*h6*x*x*x*x+1/4*h7*p*x*x*x-1/16*h6*p*x*x*x*x+1/8*h7*x*x*x*x*x+1/16*h6*x*x*x*x*x*x};
I=ideal firstEquations;
print("W1_LINE_FIRST_ELIMINATION_START");
E=eliminate({h4,h5,h6,h7},I);
print("W1_LINE_FIRST_ELIMINATION_READY");print gens E;
S=QQ[p,x];phi=map(S,R,{0,0,0,0,p,x});
ES=ideal phi(gens E);
tau=-(p+x^2+2);delta=((p-x^2-2)/2)^2;
q=tau*(tau^2-delta)*(tau^2-2*delta)*(tau^2-3*delta)*((tau^2-2*delta)^2-3*delta^2);
op=p*(2*x^2+1)*(p-x^2-2)*(x^2+2);
J=saturate(ES+ideal(q),ideal(op));
print("W1_LINE_FIRST_TORSION_RESULT");print gens gb J;
```
</details>



## Consolidated historical supplement: `research/supplements/OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md`

# Ramification schemes and marked socle frames

These two full mathematical controls distinguish support from nonreduced ramification containment and actual source frames from a target-pencil scalar. Their hypotheses remain explicit.

## Source: 2026-10-07-session-ramification-scheme-counterexample.md

# Full inverse support does not force containment of nonreduced ramification

Date: 2026-10-07. Status: **PROVED exact local counterexample**. This
blocks a proposed local extension of the ordinary projected-Veronese
argument. It does not exhibit an STCI presentation of C0, nor assert
that this germ occurs on a semi-log-canonical Veronese projection.

Let k be algebraically closed of characteristic zero and consider

    X: X^2+Y^2(Y+Z^2)=0,
    B=k[w,z],
    nu(w,z)=(X,Y,Z)=(-w^3-wz^2,-w^2-z^2,z).

The map is finite and birational: w satisfies w^2+Y+Z^2=0, and
w=X/Y in the common function field. B is the normalization. Its
conductor is YB, the reduced nodal divisor w^2+z^2=0. Indeed with
A0=k[Y,Z] one has B=A0+ A0 w and A=A0+Y A0 w. Modulo YB the inclusion
is k[z] in k[z,w]/(w^2+z^2). A conductor element must belong to k[z],
and multiplying it by w must again belong to k[z]; freeness over k[z]
forces that element to be zero. Thus the upstairs conductor is exactly
YB, rather than an inferred reduced support.

The coordinate change P=X+iYZ, Q=Y, R=2iZ gives

    P^2+Q^3-PQR=X^2+Y^3+Y^2Z^2.

This is the T_(2,3,infinity) degenerate cusp. It occurs in the strictly
semi-log-canonical list in
[Ducat, Table 1, p.9](https://d-nb.info/1317691679/34).
Equivalently the normalized pair consists of a smooth surface and a
reduced nodal conductor, and the original hypersurface is nodal in
codimension one. The example is not excluded by an slc hypothesis.

## 1. Smooth image and the complete pulled-back curve ideal

Let C be the smooth curve

    X=-2Z^3, Y=-2Z^2,

with parameter Z. Its lift c is w=z. Exact substitution gives

    nu*I_C=(w-z)(w+z,z^2).

The cofactor's support is the origin, already lying on c. Therefore
the entire reduced inverse image is exactly c, with no additional
isolated point and no additional curve. The map c->C is an isomorphism.
This example satisfies both smooth embedded image and full inverse
support, the two hypotheses under examination.

## 2. The actual differential/Fitting ramification scheme

Because dZ=dz, the relative cotangent module is generated by dw with
relations

    (-3w^2-z^2)dw=0, -2w dw=0.

Hence

    Omega_(B/A)=B/(w,z^2) dw,
    I_R=Fitt_0(Omega_(B/A))=(w,z^2).

The same ideal is generated by the two-by-two minors of the three-by-two
derivative matrix of nu. It is a length-two scheme at the singleton
normalization fiber. Its support lies on c, but its full scheme does
not: the equation w-z of c maps to -z, a nonzero element of B/I_R.
Thus **R is not a subscheme of c**.

Scheme-theoretic containment of R cannot be deduced from smoothness of
the image and full inverse support. The no-conic Hilbert-Burch argument
for reduced ordinary pinches therefore does not automatically extend
to nonreduced ramification by replacing support with scheme containment.

## 3. Correct valuation information in this germ

More generally take a lift c_f:w=f(z), with f in z k[[z]] and
f^2+z^2 nonzero. Its image is smooth because Z=z remains a parameter.
Its complete pulled-back ideal is

    (w-f)(w+f,Y_f), Y_f=-(f^2+z^2),

and again its full reduced support is c_f. Write h=ord_z(f), with
h=infinity if f=0, and r=ord_z(f^2+z^2). Then

    length(R intersect c_f)=min(h,2),
    R subset c_f iff h>=2.

The containment condition is an additional tangent condition. Smooth
image and full support permit h=1. Taking f=iz+z^k gives arbitrarily
large r=k+1 while the ramification intersection length remains one.

There is useful information without the false inclusion. Exact
Jacobian substitution gives

    J_X B=(Y) I_R.

For this embedded smooth image, the tangential derivative is a
combination of the two transverse derivatives. Their common vanishing
order is therefore

    s=r+min(h,2).

This valuation identity keeps conductor contact and ramification
intersection separate. It is proved for this local model; it is not
asserted as a general normalization formula without further hypotheses.

The [exact verifier](https://github.com/markluxton1/STCI/blob/4bd00d02c56ca39dc4b238048f44c113c6e1e363/research/computations/verify_session_ramification_counterexample.py)
reconstructs the Fitting ideal from the derivative matrix, the complete
curve preimage, the failed containment, the Jacobian product and the
explicit degenerate-cusp coordinate transformation.


---

## Source: 2026-10-07-session-socle-bridge-adversarial-audit.md

# Independent frame audit of the corrected primitive-e=1 ancestor bridge

Date: 2026-10-07. Scope: the fixed characteristic-zero curve
`C0=[s^4:s^3t:st^3:t^4]`, quartic multipliers, and the stratum
`e=1,D2=0`. Status: **PROVED CONDITIONAL ON THE ACCEPTED ANTECEDENTS**
listed below. The corrected two-target argument passes an independent
geometric audit. The old single-multiplier pole argument does not pass.
This note makes no assertion that C0 is not a set-theoretic complete
intersection or that the whole quartic ancestor incidence is empty.

## 1. Verdict, dependencies, and the rejected implication

Assume the accepted quartic-ancestor finite bound and generic-length
theorem: an ancestor with `F*alpha=u,G*alpha=v` defines a pure finite-flat
CM quadruple `Z`, generically curvilinear, with saturated pieces

```text
E1=L=O(e-7), E2=L^2(D2), E3=L^3(D3).
```

Assume also the audited socle-pencil theorem in Section 2 of
[`2026-10-06-session-localcoh-progress.md`](../supplements/LOCAL_COHOMOLOGY_CONORMAL_GEOMETRY.md#2026-10-06-session-localcoh-progress),
the complete primitive-e=1 triple directions and quartic fibres in
[`2026-10-07-session-mf6-e1-independent-audit.md`](normal_filtration_boundary_obstructions.md#source-2026-10-07-session-mf6-e1-independent-auditmd),
and P-037's all-stage exclusion of multiplier degrees at most three.
The socle theorem gives `E3=O(-14)`. Thus `e=1` means
`L=O(-6),degD3=4`.

Under these antecedents, **there is no common quartic ancestor with
`e=1,D2=0`**. The proof below uses both target equations together.

The earlier proposed bridge used the false implication that a multiplier
containing the canonical triple also vanishes in `OZ`. In fact its image
is a nonzero socle element, because its alpha-image is one of the targets.
Consequently `h*a=T*tau` cannot be used for one multiplier. The valid
equation is `h*a-T*tau=f`, retaining its actual target image `f`.
The single-multiplier cubic pole bound is therefore not an ancestor
obstruction. Its use in an actual complete-intersection quotient is a
different argument, with a different vanishing hypothesis.

## 2. The canonical triple and its actual quotient frame

Since the two targets lie in the first inverse-system socle, the images
of `F,G` in `OZ` lie in the saturated socle `E3`. One may first verify
this generically and then use the torsion-free lower filtration quotients
to extend it to every curve point. Hence both quartics contain

```text
Z3=Spec(OZ/E3).
```

When `D2=0`, multiplication `L^2 -> E2` is an isomorphism. Locally
over a completed smooth support DVR, a normal lift `ell` of a generator
of `L` has square generating `E2`. Nakayama on the three successive
rank-one pieces shows that `1,ell,ell^2` generate the canonical triple.
Its embedded transverse algebra is primitive. No curvilinear assertion
about the quadruple's special fibre is needed.

On `x0=1` the actual ambient normal coordinates are

```text
z=x1, x2=z^3+V, x3=z^4+U+3zV/2.
```

The balanced conormal coordinates satisfy to first order on the opposite
ambient chart

```text
U'=z^-7 U, V'=z^-7 V.
```

For `L=O(-6)`, write its quotient direction `U=A(z)*ell,V=B(z)*ell`
with the classified linear polynomials `A,B`. This is the actual
balanced quotient frame: a linear coefficient multiplies an `O(-6)`
frame to give the `O(-7)` normal coordinate. It is not an arbitrary
formal transverse variable.

For the principal orbit, `A=1+z,B=-2-8z`, use

```text
ell=4U/3+V/6, m=B*U-A*V.
```

On the other chart the Bezout lift is `ell'=-U'/3-V'/6`. Substituting
the quotient values gives `ell'=z^-6*ell` to first order. Likewise
`m'=(-8-2/z)U'-(1+1/z)V'=z^-8*m` to first order.
For either algebraic orbit, `A=r*z,B=1`, use `ell=V,m=U-r*z*V`.
The opposite-chart lift is `ell'=U'/r`, whose quotient value is again
`z^-6*ell`; and `m'=U'/z-r*V'=z^-8*m` to first order.
These identities are checked directly in the independent verifier.

Higher-order changes of a lift of `L` differ by saturated degree at
least two. Cubing them changes `ell^3` only in saturated degree at least
four, which is zero on the quadruple. The moving support coordinate
has its first difference from `1/z` in normal degree one; multiplying
that difference by `ell^3` is again degree at least four. Thus these
nonlinear transitions do not change the global cubic multiplication
map `L^3 -> E3`.

## 3. The target normalization and the global degree-four coefficient

The ancestor induces the isomorphism

```text
E3 -> omega_C(-3)=O(-14).
```

The isomorphism is the accepted socle-pencil theorem, rather than a
choice of a possibly meromorphic socle generator. Choose the regular
finite-chart socle frame `w` by pulling back the standard frame of
`omega_C(-3)` through this isomorphism. After twisting by the ambient
quartic, its target space is

```text
E3(4) -> omega_C(1)=O(2).
```

To verify its scalar coordinates, in the balanced normal frame

```text
q=U+zV/2, B=-z^2U+z^3V/2+V^2.
```

Their first-normal determinant is `z^3`. The restrictions of the raw
target numerators `x0*x2,x1*x3` are `z^3,z^5`; the normalized residue
coefficients are therefore exactly `1,z^2`. The same regular sections
extend at `z=0`: one computes the equality on the dense chart where the
determinant is nonzero, then uses the regular balanced residue frame
and torsion-freeness. The homogeneous pencil is `(s^2,t^2)` and has no
common zero. The raw numerators alone would give an incorrect endpoint
frame.

Multiplication gives a global line-bundle map

```text
L^3=O(-18) -> E3=O(-14).
```

Write `ell^3=tau(z)*w` on the finite chart. Then `tau` is a polynomial
of degree at most four. Explicitly, `ell'=z^-6*ell` modulo irrelevant
higher terms and `w'=z^-14*w`, so
`tau'(1/z)=z^-4*tau(z)`. Regularity at both endpoints gives the degree
bound. This is the crucial geometric constraint on the coefficient;
it cannot be assumed for an arbitrary chosen formal socle frame.

If `F0,F1` are a basis of the complete two-dimensional quartic fibre,
their alpha-images `f0,f1` lie in `span(1,z^2)` and form a basis of that
pencil: the given `F,G` are independent and their images are `u,v`.
Consequently the two images have no common projective zero.
Actual ambient torus normalization preserves this property and this
pencil, since the targets are two torus eigenvectors. Only those actual
torus transformations are used in the orbit classification.

## 4. Correct multiplier identities

In a primitive triple chart choose its regular quadratic correction
`gamma` so that `m+gamma*ell^2=0` in `OZ3`. In the quadruple write

```text
m+gamma*ell^2=a(z)*w, ell^3=tau(z)*w.
```

Both coefficients are regular on that chart. If a quartic's jet is

```text
F=h*m+gamma*h*ell^2+E*m*ell+K*ell^3+higher terms,
T=gamma*E-K,
```

then `m*ell=-gamma*ell^3`: the extra term `a*w*ell` is zero because
`E3` is annihilated by the curve ideal. Terms of saturated degree four
also vanish. Hence its actual image in `E3(4)` is

```text
f=h*a-T*tau.
```

For a basis `F0,F1`, eliminate the unrestricted local coefficient `a`:

```text
h1*f0-h0*f1=(h0*T1-h1*T0)*tau.
```

There is no assumption that either quartic annihilates `OZ`.

## 5. Principal orbit: two finite points contradict the target pencil

Put `P=4z^2+2z+1`. The accepted quartic jets give

```text
h0=P*z^3/16,
h1=P*(64z^6+8z^3+1)/1024,
h0*T1-h1*T0=(2z-1)^3*(2z+1)*P/256.
```

The determinant identity is independently recomputed from the explicit
`T0,T1`. Cancelling the nonzero polynomial `P` from the identity of
regular functions gives

```text
(64z^6+8z^3+1)*f0-64z^3*f1
    =4*(2z-1)^3*(2z+1)*tau.
```

At `z=1/2` it says `3*f0-8*f1=0`; at `z=-1/2` it says
`f0+8*f1=0`. Every section in `span(1,z^2)` has the same value at
these two points in the fixed finite-chart frame. The two linear
equations therefore force both `f0,f1` to vanish at both points.
This contradicts the basepoint-free pencil. Both points are finite,
and `P` is nonzero at them, so no endpoint or denominator issue occurs.

As a redundant stronger algebra check, the complete polynomial
coefficient system with `deg(tau)<=4` has a one-dimensional solution
space. Its target part is

```text
f0=c*(z^2-1/4), f1=(3/8)*f0.
```

It has rank one and cannot be the required target basis. The two-point
proof already supplies the contradiction without this stronger check.

## 6. Algebraic orbits: the global degrees contradict either target basis

For either root `12r^2+4r+3=0`, the accepted complete pencil has

```text
h0=1,T0=0, h1=(2r+2/3)*z^8,T1=(8r/9)*z^3.
```

Both displayed constants are nonzero. The first equation gives
`a=f0`; the second therefore reads

```text
f1=(2r+2/3)*z^8*f0-(8r/9)*z^3*tau.
```

If `f0` is nonzero its first term has degree at least eight, whereas
the second term has degree at most seven and `f1` has degree at most
two. Thus `f0=0`, already contradicting independence of the two target
images. In fact the remaining equation, with a right side divisible
by `z^3` and left side of degree at most two, forces `tau=f1=0` too.
The exact coefficient matrix has rank nine over `Q(sqrt(-2))`, confirming
the zero solution for both geometric conjugates. The degree argument
itself proves the contradiction.

## 7. Quadric-factor orbit and reproducibility

In the fourth orbit `A=-z/2,B=1`, the complete quartic fibre is
`q*H0(P3,O(2))`. Both multiplier equations then make `q*alpha` a common
ancestor with degree-two multipliers. P-037 excludes it. This is the
correct ancestor obstruction for this fibre; the STCI divisor-class
argument on the quadric is not being substituted for it.

The four primitive triple orbits are exhausted, proving the stated
conditional quartic-ancestor exclusion. Positive `D2` makes the
canonical triple defective and remains outside this argument. Other
values of `e`, multiplier degrees beyond four, and the universal STCI
question also remain outside it.

Run the independent exact frame and coefficient checks with

```sh
PYTHONDONTWRITEBYTECODE=1 python3 \
  research/computations/audit_session_socle_bridge_frames_2026_10_07.py
```

Its source imports no other research verifier or generated JSON. It
checks the determinant-normalized targets, actual first-order quotient
frames, principal cubic determinant, two-point equations, full principal
coefficient rank and both-conjugate algebraic coefficient rank. The
durable JSON carries the source hash. These exact identities support the
geometric proof above; they do not prove the listed antecedents.


---



## Consolidated historical supplement: `research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md`

The historical sections retain their hypotheses, qualifications, and proof status. Where an argument is repeated, links point to the full proof.

# October 9 historical mathematics

This compilation retains the mathematical hypotheses, counterexamples, unsuccessful arguments, and open questions. This compilation supplies no new independent audit.

---

## Source: 2026-10-09-session-elliptic-conductor-quadratic-descent-independent-audit.md

# Independent audit: quadratic descent across an elliptic conductor

**PROVED conditional exclusion, in characteristic zero.** The argument below
excludes every mate for a carrier satisfying all the listed hypotheses. It
does not assert that these hypotheses cover every singular normalization, or
that the requisite section `Q` always exists.

Let `nu:S -> X` be the finite normalization of an integral quartic surface
`X` in `P3`, with `S` normal and `H=nu^*O_X(1)`. Assume:

1. A smooth rational curve `c` maps isomorphically to the fixed smooth rational
   quartic `C0`.
2. A global section `Q` of `O_S(2H)` has Weil divisor exactly `2c`.
3. The **actual** downstairs conductor scheme `Gamma` is a smooth conic.
4. The **actual** upstairs conductor scheme `D` is a smooth integral elliptic
   curve, avoids `Sing(S)`, and maps finite flat of degree two to `Gamma`.

The conductor scheme hypotheses, not merely equality of conductor supports,
are needed for the fiber-product descent step.

## A hypothetical mate has the required divisor

The [divisor and power proof](#2-a-mate-gives-the-divisor-and-the-squared-power-identity)
derives the Weil divisor `b*c` from the mate and conductor hypotheses.
It retains possible isolated off-curve inverse points as a support
obstruction and works for every positive degree `b`.

## Even valuations exclude the anti-invariant case

The [global sign](#3-power-invariance-gives-a-global-sign-on-the-conductor)
and [ramification parity](#4-the-minus-sign-contradicts-even-ramification-valuations)
proofs give invariance of the primitive section on the entire elliptic
conductor. The parity argument covers tangency to the marked curve by
using twice the local intersection multiplicity.

## The actual conductor square gives global descent

The [conductor-square proof](#5-descent-through-the-entire-conductor-square)
glues the compatible pair on the full schemes and lifts the resulting
section to an ambient quadric.

## The fixed-curve quadric obstruction

The [quadric divisor-class proof](#6-the-fixed-c0-quadric-contradiction)
completes the exclusion. The independent audit accepts all four steps
under the listed hypotheses. Existence of the global section and the
actual smooth conductor schemes remain separate obligations in each
application.

---

## Source: 2026-10-09-session-elliptic-conductor-quadratic-descent.md

# Quadratic descent across a smooth elliptic double conductor

Date: 2026-10-09. Author: `singular_local_lift`, for
`singular_normalization_next_frontier`.

Status: **PROVED HERE, independently audited**, under the exact
hypotheses below. This is a conditional geometric exclusion, not a
classification of singular quartic normalizations. The universal
STCI problem and the unrestricted fixed-C0 problem remain open.

## 1. Theorem with actual conductor schemes retained

Let k be an algebraically closed field of characteristic zero. Let
X be an integral quartic surface in P3, let nu:S->X be its finite
normalization, and set H=nu^*O_X(1). Suppose the following hold.

1. There is a smooth integral curve c on S whose image is the fixed
   rational quartic C0=[s^4:s^3t:st^3:t^4], and nu|c is an
   isomorphism onto C0.
2. There is a nonzero global section Q of O_S(2H) whose Weil divisor
   is exactly 2c.
3. The actual downstairs conductor scheme Gamma is a smooth conic.
   The actual upstairs conductor scheme D is a smooth integral
   projective curve of genus one, and D avoids Sing(S).
4. The induced map p:D->Gamma is finite flat of degree two.

Then X has no homogeneous set-theoretic mate for C0, in any positive
degree.

Here “actual conductor” means the closed schemes defined by the
conductor ideal I=Ann_OX(nu_*O_S/O_X), respectively I O_S. Smoothness
of their supports alone does not satisfy hypotheses 3 and 4. The
theorem permits c to pass through singularities of S away from D.
It imposes no parity condition on the degree of a hypothetical mate.

## 2. A mate gives the divisor and the squared power identity

Assume G is a homogeneous mate of degree b>0, so the zero support
of G on X is exactly C0. It is not identically zero on X. Thus
h=nu^*G is a nonzero section of O_S(bH).

The curve C0 is distinct from the conic Gamma. At its generic point
the normalization is therefore an isomorphism: off the conductor
the finite ring extension is an equality. Every curve component of
nu^{-1}(C0) dominates C0 because nu is finite. Hence c is the only
curve component above C0. Consequently the Weil divisor of h is
m c for an integer m>0. Any isolated off-c inverse-image point would
already contradict the zero support of this Cartier section; that
obstruction need not be assumed absent in advance.

The intersection degree with H gives

    b H^2 = m (H.c).

The finite birational quartic normalization has H^2=4, and
H.c=deg(C0)=4. Therefore m=b and

    div_S(h)=b c.

Both h^2 and Q^b are nonzero sections of the same line bundle
O_S(2bH), with identical Weil divisor 2b c. Their quotient is a
rational function with neither zeros nor poles in codimension one.
Normality makes it an invertible regular function on S, and
projectivity and integrality make it a constant. Thus

    h^2=lambda Q^b,        lambda in k^*.

This is why an assumption that b is even is unnecessary. Squaring
the mate gives a descended power of Q for every positive integer b.

## 3. Power invariance gives a global sign on the conductor

Put M=O_Gamma(1). Since H is pulled back from X,

    O_D(H)=p^*M,
    q=Q|D is a section of p^*(M^2).

The section q is nonzero: D is integral of genus one and is distinct
from the rational curve c, while div_S(Q)=2c. Let sigma be the
nontrivial involution of the finite flat double cover p. Its action
on p^*M^2 is the canonical action on a pulled-back line bundle.

The section h|D is pulled back from G|Gamma. Restricting the power
identity to D shows that q^b is invariant under sigma. In the
function field k(D), the ratio r=(sigma q)/q therefore satisfies
r^b=1. The polynomial T^b-1 splits into linear factors over k, and
k(D) is a field. Hence r is a constant root of unity zeta in k.
Applying sigma twice gives zeta^2=1, so

    sigma q=+q       or       sigma q=-q.

These are global equalities of sections, because they hold
generically on the integral curve D. There is no independent sign
choice at different points, and no unexamined pole stratum in this
step. Only the ratio in the function field is used; the equality of
regular sections extends over their zero sets automatically.

## 4. The minus sign contradicts even ramification valuations

The conic Gamma is isomorphic to P1. Riemann--Hurwitz for the smooth
genus-one degree-two cover gives

    0 = 2(-2)+deg(R),       deg(R)=4.

In characteristic zero a degree-two ramification index is two and
its different exponent is one. Thus there are four distinct simple
ramification points. In particular there is at least one such
point P.

At P choose a local frame of M^2 downstairs, and pull it back. This
frame is sigma invariant. In the completed local ring of the smooth
curve D choose a uniformizer w such that sigma(w)=-w. For example,
the trace-zero coordinate of a quadratic algebra is a uniformizer
at a simple ramification point; its square is a base uniformizer
times a unit. Write q=a(w) in the chosen pulled-back frame.

If sigma q=-q, then a(-w)=-a(w). Since a is a nonzero regular power
series and the characteristic is not two, its first nonzero term
has odd degree. Therefore ord_P(q) is odd.

On the other hand S is regular along D. At every P in D, the prime
curve c is locally Cartier, even if it is not Cartier at some point
outside D. Let f be a local equation of c where P lies on it. The
equality div_S(Q)=2c gives locally Q=u f^2 with u a unit, after a
local frame for O_S(2H). Restricting to D makes its vanishing order
twice the local intersection multiplicity of c and D. If P does not
lie on c, its vanishing order is zero. Thus every valuation of q
on D is even:

    div_D(q)=2(c.D).

Changing to the pulled-back frame multiplies the representing
function by a unit and does not change this valuation. The odd
valuation forced by anti-invariance is impossible. Consequently

    sigma q=q.

The argument needs regularity of S along the actual D. It does not
discard non-Cartier behavior of c at singular points away from D.

## 5. Descent through the entire conductor square

For a finite flat double cover in characteristic not two, the trace
splitting gives

    (p_*O_D)^sigma=O_Gamma.

This also follows locally by choosing a trace-zero basis element
z with z^2 in the base ring and sigma(z)=-z. The projection formula
therefore identifies invariant sections of p^*M^2 with sections of
M^2. Hence q=p^*qbar for a global section qbar of O_Gamma(2).

The actual conductor square is a fiber-product square, not merely
a generic gluing prescription. Locally, if A is the ring of X, B
its normalization and I their conductor, then

    A = B x_(B/I) (A/I).

Indeed an element of B whose residue belongs to A/I differs from
an element of A by an element of I, and I is contained in A.
Globally this gives the exact sequence

    0 -> O_X -> nu_*O_S direct_sum O_Gamma -> nu_*O_D -> 0,

where the last map subtracts the two restrictions. Tensoring with
the invertible sheaf O_X(2) preserves exactness. The compatible pair
(Q,qbar) therefore comes from a global section Q_X of O_X(2), with

    nu^*Q_X=Q.

There is no H^1 obstruction to this descent: exactness identifies
the kernel already on global sections. Compatibility has been proved
on all of the smooth actual conductor D, including the ramification
points, rather than only at its generic point.

Finally the hypersurface exact sequence

    0 -> O_P3(-2) -> O_P3(2) -> O_X(2) -> 0

and H^1(P3,O(-2))=0 lift Q_X to a homogeneous ambient quadric q_X.
The lift is nonzero since Q is nonzero.

## 6. The fixed-C0 quadric contradiction

The fixed curve C0 lies on exactly one quadric, up to scalar:

    Q0 = V(x0 x3-x1 x2).

This is immediate by restricting the ten degree-two monomials to
`[s^4:s^3t:st^3:t^4]`: nine resulting monomials are independent and
the only repeated monomial is x0x3=x1x2=s^4t^4. Thus q_X is a
nonzero scalar multiple of this smooth quadric's equation.

The pullback of q_X has divisor 2c, so its zero support on S is
exactly c. Finite surjectivity then makes its zero support on X
exactly C0. Therefore the quartic equation of X, restricted to the
smooth quadric Q0, has an effective divisor supported only on C0.
Its degree is eight, so that divisor must be 2C0.

Under Q0=P1xP1 the fixed C0 has divisor class (1,3), up to swapping
the rulings. One Segre parametrization is

    [s^3:t^3] x [s:t]
        |-> [s^4:s^3t:st^3:t^4].

The divisor cut by a quartic has class (4,4). But 2C0 has class
(2,6), so it cannot be that divisor. Equivalently a residual divisor
after subtracting 2C0 would have class (2,-2), which is not
effective. This contradiction excludes the hypothetical mate G.

## 7. Applicability and boundaries

The [explicit four-A1 degree-four del Pezzo projection](quintic_octic_ade_cover_and_triple.md#source-2026-10-09-session-dp4-projection-local-liftmd)
satisfies all four hypotheses: its actual downstairs conductor is
a smooth conic, upstairs it has a smooth elliptic double cover
avoiding the four A1 vertices, and the displayed global quadric has
divisor 2c. That carrier was already excluded by its explicit
nonsingleton fibers. This theorem supplies a second exclusion and
extends to every carrier for which the same hypotheses are proved.

The theorem does not prove that every singular-normalization
quartic has this conductor or the global section Q. It does not
cover nonreduced actual conductor schemes, a singular upstairs
conductor, an upstairs conductor passing through Sing(S), or the
absence of a global doubled-curve quadric. Those hypotheses must
not be inferred solely from the reduced support, a local divisor
class, or a model family containing the explicit example.

## 8. Independent audit and primary inputs

The [independent audit summary](#source-2026-10-09-session-elliptic-conductor-quadratic-descent-independent-auditmd)
records the scope of the review. [Historical audit source](https://github.com/markluxton1/STCI/blob/8d4ea1ad5af2b26955571bb668ef1cc4a582fa3d/research/notes/2026-10-09-session-elliptic-conductor-quadratic-descent-independent-audit.md).
It accepts the power reduction without a degree parity assumption,
the odd/even valuation contradiction, complete conductor-square
descent, and the final smooth-quadric divisor-class contradiction.
Independent agreement is audit evidence; the proof is the argument
above. No finite symbolic calculation is substituted for this
conditional theorem.

The primary general inputs used here are the
[Stacks Project Riemann--Hurwitz formula](https://stacks.math.columbia.edu/tag/0C1B)
for the four simple ramification points, and
[Stacks Project cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS)
for the ambient quadratic lift. The conductor fiber-product equality,
sign reduction and parity obstruction are proved explicitly above.
No literature novelty claim is made.


---

## Source: 2026-10-09-session-genus-one-delpezzo-reduction.md

# Every genus-one quartic normalization containing C0 is a degree-four weak del Pezzo model

Date: 2026-10-09. Owner: root. Status: **PROVED HERE, independently
accepted in the bounded audit below**. This establishes the hypotheses
of the del Pezzo root-lattice reduction. It does not exclude every
genus-one normalization or supply a mate on any of them.

Let k be algebraically closed of characteristic zero. Let X in P3 be
an integral nonnormal quartic containing the smooth rational quartic
C0, let nu:S->X be its finite normalization, and let
H=nu*O_X(1). Suppose its normalization sectional genus is pi=1.
The proof does not require a mate.

The accepted [nonrational-normalization theorem](../synthesis/quartic_carrier_proof.md#2-why-a-nonnormal-normalization-is-rational)
shows that S is rational. Let sigma:M->S be its minimal smooth
resolution and L=sigma*H. Then L is a nef and big Cartier divisor,
L^2=4, and a general smooth hyperplane curve of class L has genus
one. Adjunction gives

    K_M.L=-4,       (K_M+L).L=0.

## 1. The adjoint has a unique effective representative

The smooth projective surface M is rational, so chi(O_M)=1.
Characteristic-zero Kawamata--Viehweg vanishing for the nef and big
L gives Hi(M,K_M+L)=0 for i>0. Surface Riemann--Roch therefore gives

    h0(M,K_M+L)=chi(K_M+L)
      =1+(K_M+L).L/2=1.

Choose the effective divisor D of that nonzero section. Thus
D~K_M+L and L.D=0. Since L is the pullback of an ample divisor
under sigma, any prime curve not contracted by sigma has positive
L-degree. Consequently every prime component of D is exceptional.
No rational-singularity or Gorenstein assumption on S was used here.

## 2. Minimality and negative definiteness force D=0

The exceptional intersection matrix of a resolution of a normal
surface is negative definite. Every exceptional integral prime E
therefore has E^2<0. Minimality excludes an exceptional smooth
rational curve of self-intersection -1, since it could be contracted
to give a smaller smooth resolution over S. Adjunction consequently
gives

    K_M.E=2 p_a(E)-2-E^2 >= 0.

Indeed, if p_a(E)=0 then E is a smooth rational curve, so E^2<=-2;
if p_a(E)>=1 then the displayed intersection is positive. Since
L.E=0, one also has D.E=K_M.E>=0 for every exceptional prime.
Writing the effective divisor as D=sum d_i E_i now gives

    D^2=sum d_i (D.E_i) >= 0.

This contradicts negative definiteness unless D=0. Hence the unique
adjoint section has no zeros and

    K_M~ -L,       K_M^2=4.

In particular M is a rational weak del Pezzo surface of degree four:
its anticanonical line bundle is nef and big. The curves contracted
by sigma have anticanonical degree zero.

## 3. The normalization is Gorenstein del Pezzo with ADE singularities

To make the crepant conclusion precise, choose an actual hyperplane
divisor H0 in |H|, whose pullback is L0 in |L|. The linear equivalence
K_M~ -L lets us choose a rational two-form omega on M with

    div_M(omega)=-L0.

Use the same rational two-form on S, which has the same function
field. Pushing its divisor forward gives the canonical Weil divisor

    K_S=div_S(omega)=-H0.

It is Cartier, and its negative is ample. Moreover these choices give
the actual equality of divisors

    K_M=sigma* K_S.

Thus sigma is crepant. The standard surface characterization of
Du Val singularities by a crepant resolution applies. The primary
author-hosted statement is [Miles Reid, The Du Val singularities,
Theorem 2.1(2)](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).
Accordingly S has only ADE singularities and is a normal Gorenstein
del Pezzo surface of degree four. This conclusion comes from the
adjoint argument; it is not an assumed classification hypothesis.
The usual characteristic-zero form of this surface result applies;
equivalently the finite coefficients and resolution data descend to
a finitely generated field that embeds in C, where Reid's stated
characterization applies, and the resulting intersection and crepant
properties transfer back.

## 4. Relation to a hypothetical mate and the root-lattice task

Under a mate of degree b, the accepted full-support theorem gives a
smooth lifted curve c isomorphic to C0 and b c~bH on S. Its strict
transform c# on M is also smooth. The Cartier pullback supplies an
effective rational exceptional correction Z with

    c#+Z numerically equivalent to L,       -Z^2=2 pi=2.

The previous [sectional-genus proof](../supplements/SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md)
establishes this identity without assuming that c is Cartier. On the
rational weak del Pezzo M, the integral class L-c# realizes Z in
the saturation of the exceptional root lattice inside the
anticanonical orthogonal lattice D5. Thus the forthcoming D5 torsion
filter is applicable to every remaining genus-one normalization,
once its own lattice proof is accepted. The classification of that
lattice filter and the exclusion of any surviving conductor types
are separate obligations.

The displayed [four-A1 family](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-singular-delpezzo-four-a1-familymd)
already realizes the order-two correction in an actual normalization,
then fails the full-fiber condition. It does not represent every
possible projection of a four-A1 surface. Genus-two rational
normalizations, higher carrier degrees, and entirely thick
presentations are outside this theorem.

## 5. Audit and source scope

The independent auditor `normal_global_adversarial` accepted the
KV/Riemann--Roch calculation, exceptional support, all exceptional
prime adjunction inequalities on the minimal resolution, negative
definiteness, and the chosen-canonical-form crepant equality before
this owner note was written. Its standalone audit is recorded in
the October 9 acceptance record once frozen. No new computational
test is needed for these divisor arguments. The source inputs are
the standard characteristic-zero nef-big vanishing theorem, surface
Riemann--Roch, negative definiteness on a normal-surface resolution,
and the explicitly linked Du Val characterization.


---

## Source: 2026-10-09-session-genus-one-entire-conductor-algebra-independent-audit.md

# Independent audit of the two-quadric Hilbert-series conductor proof

Date: 2026-10-09. Auditor: `singular_local_lift`.
Status: **CONDITIONAL ALGEBRA ACCEPTED**. This audits root's
`research/notes/2026-10-09-session-genus-one-entire-conductor.md`
through its actual coordinate-ring and conductor route. It does not
rederive the result from finite duality, and does not certify the
separately assigned anticanonical embedding or lifted-curve spanning
application to the full genus-one lane. The universal STCI problem
and unrestricted C0 problem remain open.

## 1. Hypotheses used in the audit

The algebra acceptance requires the stated normal integral
nondegenerate complete intersection S of two quadrics in P4, a
projection from a center outside S, and a finite birational integral
quartic image X. Its equations are exactly

    Q1=z^2-Az-R1,       Q2=Lz+R,
    F=R^2+ALR-R1 L^2,
    T=k[x0,x1,x2,x3],       A_X=T/(F),
    B=T[z]/(Q1,Q2),       C=T/(L,R).

Here A,L have degree one, R1,R degree two, and L is nonzero.
The characteristic-zero hypothesis permits the trace-zero
coordinate z-A/2. The argument up to that change of coordinate
uses no characteristic-specific cancellation.

The normalization of the pencil is justified conditionally from
these geometric assumptions: a center outside S supplies a nonzero
z^2 coefficient in one quadric; cancel it from the other. If the
remaining z coefficient were zero, the quartic image would lie in
a nonzero quadric, which is impossible for an integral quartic
surface. Thus L is nonzero. This statement does not establish the
geometric assumptions in the first place.

## 2. The injection and the complete-intersection Hilbert series

On L!=0, the equation Q2 gives z=-R/L. Substitution into Q1 gives
the displayed F. This open is nonempty because S is nondegenerate
and L is a nonzero linear form. If F were the zero polynomial, the
equations on that open would leave a three-dimensional image,
contrary to S being a surface. F is therefore nonzero.

Since X is assumed to be an integral degree-four hypersurface, the
degree-four equation F vanishing on it is its irreducible equation
up to scalar. This proves the graded injection A_X->B. It must be
established before taking HS(B)-HS(A_X); root's proof does so.

B is the actual complete-intersection coordinate ring under the
hypotheses, so its Hilbert series is the two-quadric series. The
normality and complete-intersection assumptions also justify using
this ring for normalization: its affine cone is Cohen--Macaulay,
and regular in codimension one away from the vertex by normality
of S. The vertex has codimension three. Thus the coordinate ring
is normal; monic Q1 makes B finite over A_X and z=-R/L makes their
fraction fields equal.

## 3. L,R are a regular sequence and retain all conic schemes

If R=L T1 for a linear form T1, then Q2=L(z+T1). B is a domain,
so either L or z+T1 would vanish in B. Either outcome puts S in a
hyperplane, violating nondegeneracy. Hence R is nonzero modulo L.

T/(L) is a polynomial domain in three variables. Thus the nonzero
quadratic R mod L is a nonzerodivisor, and L,R are a regular
sequence. C is consequently the entire homogeneous coordinate
ring of a plane conic complete intersection. It may be reducible
or nonreduced, but it has no additional embedded component. F lies
in (L,R), so C=A_X/J for J=(L,R) in A_X.

## 4. The signs and the exact quotient module

The identities in B are

    Lz=-R,       Rz=AR-LR1.

For the second identity, multiply Q2 by z, replace z^2 by Az+R1,
and replace Lz by -R. The minus sign before LR1 is essential.
These identities show that J kills B/A_X. Monic Q1 makes B
generated by 1,z over A_X. Thus there is a surjection

    C(-1) -> B/A_X,       a |-> az mod A_X.

With the injection from Section 2 already established, the actual
complete-intersection Hilbert series give

    HS(B)=(1+t)^2/(1-t)^3,
    HS(A_X)=(1+t+t^2+t^3)/(1-t)^3,
    HS(C)=(1+t)/(1-t)^2,
    HS(B)-HS(A_X)=t HS(C).

The surjection has zero kernel in every graded degree, not merely
an eventually vanishing kernel. Therefore

    B/A_X isomorphic to C(-1).

As a supplementary literal sign check, reduce modulo the monic
Q1 in the free T-basis 1,z. The ideal generated by Q2 has relation
columns (R,L) and (LR1,AL+R), with determinant F. Subtracting A
times the first column from the second gives (LR1-AR,R), exactly
the second identity above. This is consistent with the Hilbert-series
quotient proof and does not change its scope.

## 5. Actual conductor, upstairs scheme, and trace

The conductor is Ann_A_X(B/A_X). The annihilator of C(-1) is
exactly J, since C=A_X/J. Hence the actual entire conductor ideal
is (L,R). Equality of Hilbert series before sheafification leaves
no hidden finite-length module at the affine cone vertex and no
discarded conductor scheme structure. Sheafification gives

    nu_*O_S/O_X=O_Gamma(-1).

In B, R=-Lz, so JB=(L). L is a nonzero element of the domain B;
the upstairs scheme D=V_S(L) is therefore the actual Cartier
hyperplane conductor, including through singular points of S.
Its coordinate ring is exactly

    B/JB=C[z]/(z^2-Az-R1).

This is free of rank two over C, with basis 1,z and graded shifts
zero and one. It therefore gives

    p_*O_D=O_Gamma direct_sum O_Gamma(-1)

as modules, and proves finite flat degree two on every point of
the actual conic, including the double line. The equation determines
the entire multiplication, not just a generic extension.

The trace is A on the generator z. The involution z->A-z preserves
the monic equation. In the coordinate w=z-A/2 it is w->-w, with
w^2=A^2/4+R1. This remains valid over nonreduced C. Root explicitly
does not infer a single global sign from powers on a reducible or
nonreduced D; that retained boundary is correct.

## 6. Fixed-C0 signs and the squarefree subcase

Under the separately stated RNC coordinate hypothesis, all six
displayed quadrics vanish on
[U^4:U^3V:UV^3:V^4:U^2V^2]. The normalized coefficient formulas
give the exact restrictions

    R_C=-z_c L_C,
    R1_C=z_c^2-A_C z_c,       z_c=U^2V^2.

The second restriction has the minus sign before A_C z_c. Thus
at L_C=0 the roots are z_c and A_C-z_c, as root states.

The assertion that a mate forces them to coincide is justified
conditionally: Gamma is a conic distinct from degree-four C0,
so normalization is an isomorphism at the generic point of C0.
c is the sole curve component above C0. A second isolated point
in a fiber off c cannot belong to the zero support of a nonzero
Cartier mate without another curve component. Hence such a point
prevents a mate.

L_C is a nonzero binary quartic with middle coefficient zero.
A_C-2z_c has middle coefficient -2. If L_C has four distinct
projective roots, the forced coincidence requires the latter
quartic to vanish at all four, making the two quartics proportional.
Their middle coefficients rule that out in characteristic zero.
This accepts only the squarefree subcase. Repeated-root strata and
the global power-descent problem remain unresolved by this audit.

## 7. Exact algebra and geometric hypotheses

The symbolic identities corroborate the displayed algebra. They do not
verify the geometric hypotheses or supply parameter coverage for the
application; those requirements remain as stated in the proof and
acceptance boundary below.

## 8. Acceptance boundary

Accepted: the conditional CI-projection algebra, regular-sequence
argument, exact quotient and actual conductor ideal, full upstairs
quadratic algebra, trace involution, and fixed-C0 restriction signs.
The squarefree-L necessary-condition exclusion is also accepted
under its stated RNC coordinate hypothesis.

Not audited here: the anticanonical CI embedding of every surface
in the proposed genus-one lane, projective spanning of every lifted
c needed to choose these RNC coordinates, the entire repeated-root
parameter space, or the doubled-curve power-descent obstruction.
Those separate application claims must not be certified by this
conditional algebra acceptance.


---

## Source: 2026-10-09-session-genus-two-adjoint-conic-model.md

# The genus-two adjoint conic model and its bounded exceptional locus

Date: 2026-10-09. Owner: `delpezzo_d5_torsion_filter`.
Status: **PROVED HERE**. Sections 1--2 are independently accepted in
the [adjoint audit](#source-2026-10-09-session-genus-two-adjoint-independent-auditmd)
and its [degree-one counteraudit](#source-2026-10-09-session-genus-two-degree-one-counterauditmd).
Sections 4--5 and 7 are independently accepted in the
[null-curve and mate-strata audit](#source-2026-10-09-session-genus-two-nullcurve-mate-independent-auditmd).
Sections 3, 6 and 8 are supplied for a final bounded audit. This is a
structural reduction; neither the genus-two mate lane nor the
unrestricted STCI problem is excluded here.

Work over an algebraically closed field of characteristic zero. Let
X in P3 be an integral nonnormal quartic containing a smooth rational
degree-four curve C0. Let nu:S->X be its finite normalization,
sigma:M->S its minimal smooth resolution, H=nu*O_X(1), and L=sigma*H.
Assume normalization sectional genus pi=2.

The accepted [rationality theorem](../synthesis/quartic_carrier_proof.md#2-why-a-nonnormal-normalization-is-rational)
gives rational M, without a mate hypothesis. The basic data are

    L nef, big and globally generated,
    L^2=4,       K_M.L=-2,       chi(O_M)=1,
    h0(M,L)=h0(S,H)=4.

The four actual ambient sections span this complete space; the
complete |L| morphism has the actual quartic X as its image and is
birational. An integral prime E has L.E=0 exactly when it is
sigma-exceptional. Minimality forbids an exceptional smooth rational
(-1) curve, but does not forbid (-1) curves with positive L-degree.
No conductor classification or ADE hypothesis is assumed.

## 1. The adjoint is nef and has square zero

Set A=K_M+L. Nef-big Kawamata--Viehweg vanishing and Riemann--Roch give

    h0(M,A)=1+(A.L)/2=2,       A.L=2.

If A.E<0 for an integral prime E, effectiveness makes E a fixed
component and forces E^2<0. Adjunction gives

    K_M.E=2p_a(E)-2-E^2.

This is nonnegative for p_a(E)>=1 or E^2<=-2. The remaining case is
a smooth rational (-1) curve, and minimality then gives L.E>=1,
so A.E=-1+L.E>=0. Hence A is nef. Its square is

    A^2=K_M^2,

and Hodge index against L gives 0<=A^2<=1.

If A^2=1, the class T=L+2K_M is numerically zero: T.L=0 and T^2=0,
and L-perp is negative definite. A numerically trivial divisor N
on this rational M is linearly trivial by the following useful
direct argument. Riemann--Roch gives chi(N)=1; Serre duality gives
h2(N)=h0(K_M-N)=0 because (K_M-N).L=-2. Thus N has a nonzero section.
Its zero divisor is effective and numerically zero, hence zero by
intersection with an ample class. In particular T~0 and L~2A.

Two independent sections u,v of A give three independent square
sections u^2,uv,v^2 of L. Independence follows from the nonconstant
rational function u/v. Completing them to a basis of h0(L)=4 puts
the |L| image in the nonzero quadric X0 X2-X1^2=0, contrary to its
being an integral quartic hypersurface. Therefore

    A^2=K_M^2=0.

The independent degree-one counteraudit verifies this exact
contradiction. An anticanonical classification theorem is not needed.

## 2. The entire adjoint system is a rational pencil without base points

Write |A|=|P|+D, where D is fixed and |P| has no fixed curve.
Then h0(P)=2. Nefness of A gives A.P=A.D=0. Two general members of
|P| have no common curve, hence P^2>=0. Subtracting the appropriate
rational multiple of A makes P orthogonal to L; Hodge index then
gives P^2<=0. Thus P^2=0 and P is numerically proportional to A.
Any base point would give a positive local intersection multiplicity
between two general members, so |P| has no base points.

The associated map to P1 has connected fibers. Its Stein base is P1
because M is rational. If its finite map to the original target had
degree d, then h0(P)=h0(P1,O(d))=d+1, so d=1. A general fiber F is
smooth and integral. Since K_M=A-L and A.P=0,

    2g(F)-2=K_M.P=-L.P<0.

Therefore F is P1 and L.P=2. Comparing with L.A=2 shows P is
numerically equivalent to A; the effective fixed part D is
numerically zero and is therefore zero. Consequently

    f:=K_M+L,       |f| is a basepoint-free connected rational pencil,
    f^2=0,         L.f=2,       K_M.f=-2.

The general fiber is mapped by the actual complete |L| isomorphically
onto a smooth plane conic in X. Its degree-two line bundle uses at
most three independent sections. A two-dimensional subspace would
give a degree-two map onto a line, contradicting birationality on
the general fiber. Thus all three sections of O_P1(2) occur.

This fibration is on M. It need not descend as a morphism to S,
because some curves contracted by sigma can be horizontal for it.

## 3. A marked eight-blowup ruled model

Contract vertical (-1) curves until the smooth rational fibration
is a relatively minimal ruled surface F_n. A smooth relatively
minimal P1 fibration over P1 is a P1 bundle, so this is a Hirzebruch
surface. The resulting factorization M->F_n consists of point
blowups, including possibly infinitely near centers. Since K_M^2=0
and K_Fn^2=8, there are exactly eight point blowups.

Write C_min^2=-n and C_min.f=1 on F_n, and use total transforms
e1,...,e8 for the blowup classes. Every contracted vertical (-1)
curve E has f.E=0, K.E=-1, and therefore

    L.E=(f-K).E=1.

At each contraction the pushed-down L remains nef; intersecting
strict transforms proves this directly, as in the rationality note.
The canonical blowup formula therefore gives the actual marked class

    L=2C_min+(n+3)f-sum_{i=1}^8 e_i.

On F_n the pushed-down L has intersection 3-n with C_min. Nefness
forces

    0<=n<=3.

All multiplicities are one in this total-transform marking. This
does not mean that all eight centers are distinct points of F_n.
For a direct numerical control, the pushed-down class has square
twelve and canonical intersection minus ten; subtracting the eight
blowup classes gives L^2=4 and K_M.L=-2 as required.

This model uses only the adjoint fibration. It does not assert that
the normalization is itself the strict transform of X in a blowup
of an ambient line, or that the original conductor is a reduced line.

## 4. All contracted prime curves have tightly bounded types

Let E be any integral sigma-exceptional prime. Put

    d=f.E=K_M.E>=0,
    Q=K_M+L/2.

The inequality d>=0 follows from nefness of f. The projection Q
lies in L-perp and has square -1. Since L-perp is negative definite,
Cauchy--Schwarz there gives

    d^2=(Q.E)^2<=-E^2.

Adjunction gives

    -E^2=d+2-2p_a(E),
    d^2<=d+2-2p_a(E).

If d=0, the negative square forces p_a(E)=0 and E^2=-2. Thus every
vertical contracted prime is a smooth rational (-2) curve.

If d>0, the inequality leaves only d=1 or d=2. For d=1 the map
E->P1 induced by f has degree one. It is finite birational, and the
target P1 is normal, so it is an isomorphism. Hence E is a smooth
rational section and E^2=-3.

For d=2 the inequality forces p_a(E)=0 and E^2=-4. Equality in
Cauchy--Schwarz gives E numerically equivalent to -2Q=-2K_M-L.
The numerical-to-linear argument of section 1 gives

    E~ -2K_M-L,       L~2f+E.

Multiplying three independent sections u^2,uv,v^2 of 2f by the
nonzero section of E gives three independent sections of L with
the same quadric relation. This contradicts the actual quartic
image. Thus the (-4) bisection cannot occur.

**Conclusion.** Every contracted prime is either a vertical smooth
(-2) curve or a horizontal smooth (-3) section. No positive-genus
exceptional prime has been omitted by an ADE assumption.

## 5. There are at most two horizontal curves, and they are disjoint

For two distinct horizontal (-3) sections E1,E2 put t=E1.E2>=0.
For T=E1+E2, one has K_M.T=2 and T^2=-6+2t. Cauchy--Schwarz on
L-perp gives 4<=6-2t, so t<=1.

If t=1, equality gives T numerically equivalent to -2Q, hence
T~-2K_M-L and L~2f+T. The effective divisor T gives the same
three-section quadric contradiction as section 4. Therefore t=0:
two such sections are disjoint.

Suppose three such curves existed. For their sum T, pairwise
disjointness gives T^2=-9 and K_M.T=3. Cauchy equality gives

    T equivalent to -3Q,       2T~-6K_M-3L.

The upgrade to the displayed linear equivalence uses the same
numerically-trivial-divisor argument. It implies L=2B in Pic(M),
with the explicit integral class B=-3K_M-T-L. Then

    B^2=1,       K_M.B=-1.

Riemann--Roch gives chi(B)=2. Also h2(B)=h0(K_M-B)=0 because its
L-degree is negative. Hence h0(B)>=2, and the square sections of
two independent sections of B again put the |L| image in a quadric.
This contradiction proves that there are at most two horizontal
(-3) sections.

They can still meet vertical (-2) curves in their exceptional fiber.
No claim that all singularities of S are ADE is made.

## 6. The vertical root lattice is the explicit D8 lattice

In the marked ruled model of section 3, a Picard class orthogonal
to both f and L has the form

    v=b f-sum_i d_i e_i,       2b=sum_i d_i.

Its square is -sum_i d_i^2. Thus the integral lattice

    f-perp intersect L-perp

is the negative D8 lattice: integer vectors (d1,...,d8) with even
coordinate sum. Its roots are the 112 vectors +/-u_i+/-u_j, bound
geometrically to

    +/- (e_i-e_j),       +/- (f-e_i-e_j).

Every vertical contracted (-2) curve is one of these roots. The
negative definite lattice of all vertical exceptional primes is
therefore an embedded root subsystem of D8, and its total rank is
at most eight. The signed-coordinate argument from the
[D5 filter](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-torsion-filtermd) applies
to root sublattices here as well: coordinate-connected components
are A or D, including D2=2A1 and D3=A3. This is an exact lattice
identification, not a claim that every embedded D8 configuration
is geometrically realized in the given conic model.

If there are no horizontal exceptional curves, every exceptional
prime is (-2) and the canonical divisor is crepant on the minimal
resolution; the standard Du Val criterion then gives ADE singularities
of S. With horizontal sections present that inference is unavailable.

## 7. A mate retains two correction strata, not just the ADE one

Now add a hypothetical mate. Its full support supplies a smooth
embedded c=P1 on S and an effective rational exceptional correction Z,

    c# + Z equivalent to L,       Z=sum_i a_i E_i,       a_i>=0.

The class Z=L-c# is integral, although its coefficients in the
exceptional basis may be fractional. Put

    q=-Z^2>0,       lambda=K_M.Z.

The general adjunction identity from the sectional-genus record is

    q+lambda=2pi=4.

Since K_M.E is zero on every vertical prime and one on each
horizontal (-3) section,

    lambda=sum of the horizontal correction coefficients.

It is a nonnegative integer, because K_M and Z are integral classes.
Cauchy--Schwarz with Q in section 4 gives

    lambda^2<=q=4-lambda.

Therefore exactly two necessary numerical strata remain:

| lambda | q | c#^2 | f.c# | Type of lifted rational curve on M |
| --- | --- | --- | --- | --- |
| 0 | 4 | 0 | 2 | Bisection |
| 1 | 3 | 1 | 1 | Section |

The lambda=1 stratum must not be discarded by setting Z^2=-4 in
advance. That equality presupposes K_M.Z=0, which is automatic in
the ADE lane but has not been established in the non-ADE lane.
An attempted audit shortcut making that substitution was corrected
before acceptance. Effectiveness alone permits lambda=1.

In the lambda=0 stratum, Z has zero coefficient on all horizontal
sections. It is supported on vertical (-2) components and belongs
to D8. For a horizontal section E, positivity gives Z.E>=0 while
the mate gives Z.E=-c#.E<=0. Consequently Z.E=c#.E=0. Thus both
the correction support and c# avoid the horizontal sections in this
stratum. This avoidance is conditional on lambda=0.

As in the D5 proof, Z is not in the integral exceptional lattice R:
otherwise c~H downstairs would be Cartier, so embedded smoothness
forces c to avoid Sing(S), and negative definiteness then forces
Z=0. Under a degree-b mate, bZ belongs to R. Determining which
D8 root sublattices and exceptional configurations can contain the
required missing norm-four or norm-three class remains open here.

## 8. The two strata have concrete moving systems

In the lambda=0 stratum, the smooth P1 c# has square zero. The
restriction sequence

    0 -> O_M -> O_M(c#) -> O_c#(c#) -> 0

and H1(O_M)=0 give h0(c#)=2. The system is basepoint free: its
restriction to c# is O_P1, and the canonical section is nonzero
away from c#. Thus c# is a fiber of a second rational pencil.
The two rational pencils have fiber intersection f.c#=2.

In the lambda=1 stratum, c#^2=1. The same sequence restricts to
O_P1(1), gives h0(c#)=3, and proves basepoint freeness. The complete
|c#| map has two-dimensional image in P2 and generic degree one,
because c#^2=1. It is therefore a birational morphism M->P2.
As K_M^2=0, it consists of nine point blowups.

Mark c# by the pullback h of a line and the nine total exceptional
classes e0,...,e8. The nef class L has the form

    L=4h-sum_{i=0}^8 m_i e_i,       m_i>=0.

Nefness of its successive pushdowns ensures these nonnegative
integer multiplicities, including infinitely near centers. The
two intersection identities give

    sum_i m_i=10,       sum_i m_i^2=12,
    sum_i m_i(m_i-1)=2.

Exactly one m_i is two and the other eight are one. Renaming the
double center e0, the actual marked classes are

    L=4h-2e0-sum_{i=1}^8 e_i,
    f=K_M+L=h-e0,
    c#=h,
    Z=L-c#=3h-2e0-sum_{i=1}^8 e_i.

This is a stronger marked reduction for the retained lambda=1
mate stratum. It does not show that the effective rational
exceptional representative of Z has integral coefficients, nor
that it descends to a mate on X. In particular the smooth lifted
curve and its singleton normalization fibers remain necessary
conditions in addition to these marked identities.

## 9. Relationship with a double-line blowup, retaining its hypotheses

For comparison only, if an actual carrier X has a line ell of
generic multiplicity two, put B=Bl_ell(P3), with pulled-back
hyperplane H_B and exceptional divisor E_B. Its strict transform is

    T~4H_B-2E_B=2H_B+2f_B,       f_B=H_B-E_B.

When T is normal, adjunction gives K_T=-E_B|T. The exceptional
intersection is a (2,2) scheme in E_B=P1 times P1, with arithmetic
genus one. The numerical identities are H_B^2|T=4,
H_B.E_B|T=2, and (E_B|T)^2=0. This is consistent with the adjoint
model, but it is a conditional ambient realization.

[Dolgachev, Monoidal and submonoidal surfaces, and Cremona transformations](https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/monoidal.pdf),
section 3, explicitly imposes conditions before identifying the
normalization with this strict transform. Definition 3.6 retains
that identification, discriminant multiplicity bounds and smoothness
of the small discriminant; Proposition 3.7 gives the resulting
normalization geometry. Its nondegenerate model must not be used
as coverage of arbitrary genus-two normalizations. Sections 1--8
above do not use those extra hypotheses or an asserted reduced
downstairs conductor line.

## 10. Continuation-ready boundary

The intrinsic adjoint argument produces a connected rational conic
fibration, K_M^2=0, an explicit eight-blowup ruled marking, and a
bounded exceptional locus: vertical D8 roots and at most two
disjoint horizontal (-3) sections. For a mate it retains exactly
the two numerical correction strata of section 7, and section 8
gives a concrete marked plane model in the non-ADE stratum.

The next finite task is to classify smooth-lift correction vectors
in these exceptional configurations. Downstairs smoothness is stronger
than smoothness of c# alone; for example meeting multiple exceptional
branches or tangency to an exceptional prime may prevent a uniformizer
of c from descending. A necessary local condition must be proved
before it is used as a lattice exhaustion. The actual conductor,
full inverse-image support, and descent of sections to the original
quartic remain separate obligations.

No exhaustive genus-two mate exclusion, no conductor purity theorem,
and no universal STCI conclusion is claimed. No frontier
file has been edited by this owner.


---

## Source: 2026-10-09-session-genus-two-adjoint-independent-audit.md

# Independent audit: the genus-two adjoint pencil is a rational conic fibration

Date: 2026-10-09. Auditor: `genus_two_adjoint_audit`. Status:
**PROVED HERE / independently accepted as a structural reduction**.
This note audits the proposed genus-two reduction of
`delpezzo_d5_torsion_filter`. It does not classify every singular
normalization or exclude mates in this lane. No frontier
file was edited.

Work over an algebraically closed field of characteristic zero. Let
X in P3 be an integral nonnormal quartic containing a smooth rational
degree-four curve C. Let nu:S->X be its finite normalization,
sigma:M->S its minimal smooth resolution, H=nu^*O_X(1), and
L=sigma^*H. Assume that a general curve of class L has genus two.
Then the entire complete adjoint system

    |K_M+L|

is a basepoint-free pencil with connected general fiber a smooth
rational curve F and L.F=2. The complete |L| morphism maps its general
fiber isomorphically to a plane conic in the actual quartic X. The
assertion is about the smooth resolution M; it does not assert that
the fibration descends to S or that S has rational or ADE
singularities.

## 1. Inputs and the exact scope of minimality

The accepted [nonrational-normalization audit](../synthesis/quartic_carrier_proof.md#2-why-a-nonnormal-normalization-is-rational)
establishes that M is rational without requiring a mate. The general
plane-section and pullback calculations give

    L nef, big, and globally generated,
    L^2=4,     K_M.L=-2,     chi(O_M)=1,     h0(M,L)=4.

The four pulled-back ambient sections span all of H0(M,L), so the
complete |L| map is sigma followed by the actual finite birational
normalization map nu. Its image is the given integral quartic X,
not a projection chosen after the calculation.

For an integral prime E on M,

    L.E=0  if and only if E is sigma-exceptional.

Indeed H is ample on S. Minimality of sigma excludes an exceptional
smooth rational (-1)-curve. It does not exclude (-1)-curves with
positive L-degree, which will be treated explicitly below. No
assumption about rational singularities of S is used.

## 2. The adjoint is effective and nef

Put A=K_M+L. Characteristic-zero Kawamata--Viehweg vanishing for the
nef and big L gives H^i(M,A)=0 for i>0. Surface Riemann--Roch yields

    h0(M,A)=1+(A.L)/2=2,     A.L=2.

Suppose that A.E<0 for an integral prime E. Since A is effective,
E occurs in every effective member of |A|. Choose one such member
and write it nE+B, with n>0 and E not a component of B. Distinct
effective curves have nonnegative intersection, so

    0>A.E=nE^2+B.E

forces E^2<0. Adjunction, valid also for an integral possibly
singular curve on the smooth M, gives

    K_M.E=2p_a(E)-2-E^2.

If p_a(E)>=1 this is positive. If p_a(E)=0, E is a smooth rational
curve, and E^2<=-2 gives K_M.E>=0. The only remaining possibility
is a smooth rational (-1)-curve. If its L-degree were zero it would
be exceptional, contradicting minimality. Therefore L.E>=1 and

    A.E=K_M.E+L.E=-1+L.E>=0.

Every case contradicts A.E<0. Thus A is nef. In particular

    A^2=K_M^2+2K_M.L+L^2=K_M^2>=0.

Hodge index applied to L gives

    (A.L)^2 >= A^2 L^2,

so 0<=A^2<=1. Its square is an integer, hence A^2 is zero or one.

## 3. Square one would put the image in a quadric

Assume A^2=1. Set N=L-2A=-L-2K_M. Then

    N.L=0,     N^2=0.

Since L^2>0, Hodge index is negative definite on its numerical
orthogonal complement. Thus N is numerically zero. We upgrade this
to linear equivalence directly, avoiding any shorthand inference
from torsion-freeness of the Picard group.

Let T=L+2K_M=-N. Riemann--Roch gives chi(T)=1 because T is
numerically trivial and chi(O_M)=1. Serre duality gives

    h2(T)=h0(K_M-T)=0:

an effective representative of K_M-T would have negative
L-intersection -2, impossible for nef L. Hence
h0(T)=1+h1(T)>=1. A nonzero section has an effective divisor
numerically equivalent to zero; intersection with any ample
divisor forces that divisor to be zero. Therefore T~0 and

    L~ -2K_M,     A~ -K_M.

There are two independent sections u,v of A since h0(A)=2. The
three sections u^2,uv,v^2 of 2A=L are linearly independent: on the
open where v is nonzero, a dependence would make u/v algebraic
over the algebraically closed field k, hence constant, contradicting
the independence of u and v. Complete these sections to a basis
of the four-dimensional H0(L). In the resulting coordinates the
complete |L| image satisfies the nonzero equation

    X0 X2-X1^2=0.

An integral two-dimensional quartic in P3 cannot be contained in
a quadric: its homogeneous prime ideal is generated by its
irreducible degree-four hypersurface equation. This contradicts
the actual image being X. The square-one case is excluded.

This bounded argument was counteraudited independently by
`degree_one_anticanonical_counteraudit`; its
[separate note](#source-2026-10-09-session-genus-two-degree-one-counterauditmd)
also checks the numerical-to-linear upgrade and the independence
of the square sections. Consequently

    A^2=K_M^2=0.

## 4. The adjoint has no fixed divisor and no base points

Write the complete system as |A|=|P|+D, with D its fixed effective
divisor and |P| having no fixed curve. Multiplication by the fixed
section gives h0(P)=h0(A)=2. Nefness of A and A^2=0 give

    A.P=A.D=0.

Two general distinct members of |P| have no common curve, so P^2
is the sum of their nonnegative local intersection multiplicities.
Thus P^2>=0. Put lambda=(P.L)/(A.L) and N0=P-lambda A.
Then N0.L=0 and, since A.P=A^2=0,

    N0^2=P^2.

Hodge index for the positive-square L gives P^2<=0. Therefore
P^2=0 and N0 is numerically zero; in particular P is numerically
proportional to A. Every base point of |P| would give a positive
intersection multiplicity to the two general members. Hence
|P| has no base points and defines a morphism g:M->P1.

Take its Stein factorization M->B->P1. The normal projective curve
B is smooth, and H1(O_B) injects into H1(O_M)=0 because the first
map has connected fibers and direct image O_B. Thus B is P1. If
the finite map B->P1 has degree d, then P is the pullback of
O_B(d). Connected fibers and the projection formula give

    h0(P)=h0(P1,O(d))=d+1.

As h0(P)=2, d=1. The original g therefore has connected fibers,
and P is the class of one fiber, not a multiple fiber class used
as a composite pencil. A general fiber F is smooth and integral
in characteristic zero; generic smoothness and connectedness
suffice here.

Since A.P=0 and K_M=A-L, adjunction gives

    2g(F)-2=K_M.P=-L.P<0.

The strict inequality holds because P is a nonzero effective
moving class: it cannot have zero degree against the nef and big
L, as Hodge index and P^2=0 would make P numerically zero. Thus
g(F)=0 and L.P=2. Since A.L=2, the numerical proportionality is
P equivalent to A, and D is numerically zero. An effective
numerically-zero divisor is zero by ample intersection. Hence

    D=0,     A~P,     |K_M+L|=|F|.

This handles fixed exceptional components and infinitely near
points without selecting a particular blowup model.

## 5. The general fiber is an actual plane conic

The restriction of L to F=P1 has degree two and is globally
generated. Its induced map into P3 comes from a subspace of
H0(P1,O(2)), of dimension at most three. It cannot have dimension
one, because L.F>0 and the |L| morphism does not contract F.
If its dimension were two, F would map with degree two onto a
line. The surface morphism is birational and is an isomorphism
on a dense open of M, so its restriction to the general fiber
is generically one-to-one. The degree-two line map is impossible.
The restriction therefore uses all three sections of O(2) and
embeds the general F as a smooth plane conic in the actual X.

## 6. Accepted reduction and unresolved obligations

The proposed adjoint reduction passes independently, including
all fixed-part, relative-minimality, and numerical-to-linear
issues. No smoothness or ADE conclusion for S was inferred.
In particular a sigma-exceptional curve may be horizontal for
the adjoint ruling, so this proof does not by itself descend
the ruling to S. Identifying exceptional configurations, the
entire conductor, full normalization fibers above C, and descent
of a hypothetical mate remain separate obligations.

The argument applies to every rational genus-two normalized
quartic model satisfying the stated complete birational |L|
hypotheses, with no mate required. The prior accepted rationality
theorem establishes these hypotheses for an integral nonnormal
quartic containing any smooth rational degree-four curve. The
unrestricted C0 and universal STCI problems remain open.

Source scope: the vanishing input is the same primary
[Hacon characteristic-zero nef-big vanishing account](https://www.math.utah.edu/~hacon/Kyoto2016talks.pdf)
already checked in the rational and genus-one audits. The
remaining tools are surface Riemann--Roch, Serre duality,
adjunction, Hodge index, intersection positivity on a smooth
surface, Stein factorization, and generic smoothness. The
degree-one and fixed-part conclusions above are proved here
rather than imported from an ample-polarization classification.
[Lanteri and Mallavibarrena, Rational conic fibrations of sectional genus two](https://arxiv.org/abs/2005.11415)
is a relevant primary classification reference, but its ample
polarization hypotheses are not substituted for the nef
pullback hypothesis needed here.


---

## Source: 2026-10-09-session-genus-two-degree-one-counteraudit.md

# Bounded counteraudit: the genus-two adjoint square-one case is impossible

Date: 2026-10-09. Owner: degree-one-anticanonical counteraudit agent.
Status: **PROVED HERE; accepted bounded argument**. This note excludes
only the square-one adjoint configuration specified below. It does not
establish the nefness of an adjoint in any broader normalization problem.

Let k be algebraically closed of characteristic zero, let M be a smooth
rational projective surface, and write K=K_M. Let L be a nef, globally
generated, big Cartier divisor satisfying

    L^2=4,       K.L=-2,       h0(M,L)=4.

Assume that the complete morphism phi_|L|:M->P3 is birational onto an
integral degree-four surface. Put A=K+L. The configuration A^2=1 is
impossible. The stated additional assumption that A is nef is allowed
but is not needed for this bounded exclusion.

## 1. Hodge equality gives L numerically equivalent to -2K

We have A.L=K.L+L^2=2. Set D=L-2A. Then

    D.L=4-2(2)=0,
    D^2=4-4(2)+4(1)=0.

The Hodge index theorem says that the orthogonal complement of the
positive-square class L in the real numerical divisor space is negative
definite. Thus D is numerically zero. Consequently

    L numerically equivalent to -2K,
    A numerically equivalent to -K,
    K^2=A^2-2K.L-L^2=1.

The first displayed conclusion uses L=2(K+L) numerically, rearranged
to L numerically equivalent to -2K.

## 2. Riemann--Roch upgrades the numerical equality to linear equivalence

The usual rational-surface facts imply that numerical and linear
equivalence coincide. However, the bare statement that Pic(M) is
torsionfree does not by itself prove this: the numerical kernel must
also be addressed. The following direct proof avoids that shortcut.

Put N=L+2K, which is numerically trivial by Step 1. Rationality gives
chi(O_M)=1. Surface Riemann--Roch and Serre duality give

    chi(O_M(N))=1+N.(N-K)/2=1,
    h2(M,N)=h0(M,K-N).

An effective divisor in the class K-N would have intersection
(K-N).L=K.L=-2 with the nef divisor L, which is impossible. Hence
h2(M,N)=0 and h0(M,N)=1+h1(M,N)>=1. Choose a nonzero section of
O_M(N), with effective zero divisor E. Since E is numerically trivial,
E.H=0 for any ample divisor H. A nonzero effective divisor has strictly
positive intersection with an ample divisor, so E=0. This nowhere-zero
section trivializes O_M(N). Therefore

    L linearly equivalent to -2K,
    A linearly equivalent to -K.

In particular -K is nef and big with (-K)^2=1. These conclusions follow
from numerical equivalence to L/2; no anticanonical classification is
being assumed.

## 3. The anticanonical system has exactly two sections

Apply characteristic-zero Kawamata--Viehweg vanishing to the nef and
big Cartier divisor L. It gives

    Hi(M,K+L)=0 for every i>0.

The precise primary-source statement used here is [Osamu Fujino,
Kawamata--Viehweg vanishing theorem, Theorem 0.1](https://www.math.kyoto-u.ac.jp/~fujino/kawamata--viehweg2.pdf), applied
with the morphism to a point and integral D=L. Its fractional part is
zero, so the normal-crossings condition is automatic.

Since K+L is linearly equivalent to -K, Riemann--Roch gives

    h0(M,-K)=chi(O_M(-K))
      =1+(-K).(-2K)/2=1+K^2=2.

This is the only vanishing-theorem use in the argument. It makes no
assumption that |-K| is free of base points or fixed divisors.

## 4. Two independent sections force a quadratic equation for the image

Let s,t be a basis of H0(M,-K). At the generic point, the ratio f=s/t
is an element of k(M). It is nonconstant: otherwise s and t would be
linearly dependent. Because k is algebraically closed, every element
of k(M) algebraic over k lies in k. Therefore f is transcendental over
k.

If a s^2+b st+c t^2=0 as a section of O_M(-2K), division by t^2 at
the generic point gives

    a f^2+b f+c=0.

Transcendence forces a=b=c=0. Thus s^2,st,t^2 are linearly independent
sections of O_M(-2K). Choose the isomorphism O_M(-2K)=O_M(L) supplied
by Step 2 and extend these three sections to a basis

    (s^2, st, t^2, u)

of H0(M,L), which has dimension four by hypothesis. In the corresponding
coordinates of P3, the complete morphism satisfies

    X0 X2-X1^2=0,

because (s^2)(t^2)=(st)^2 as sections of O_M(2L). This is a nonzero
homogeneous polynomial of degree two.

The calculation at the generic point is valid even if s and t have
a common fixed divisor or base points. At a common zero of s and t,
the three product coordinates vanish; global generation of L makes
u nonzero there, and the morphism sends the point to the quadric
vertex [0:0:0:1]. There is therefore no undefined evaluation or
fixed-component exception to the quadratic equation.

An integral degree-four surface in P3 has a principal homogeneous
ideal generated by an irreducible polynomial of degree four. It cannot
be contained in the zero set of a nonzero quadratic polynomial. This
contradicts the assumed image. Equivalently, the image is the quadric
cone and the degree formula L^2=deg(phi) deg(image) forces deg(phi)=2,
contradicting birationality.

## 5. Audit boundaries and characteristic

All steps above are accepted under the stated characteristic-zero
hypotheses. Rationality was used for chi(O_M)=1, and the direct
Riemann--Roch argument gives the required numerical-to-linear upgrade.
Neither a weak del Pezzo classification nor a base-point-free
anticanonical pencil is required.

The square-product independence and the quadratic identity work over
an algebraically closed field in every characteristic. The exact
equality h0(-K)=2 above uses characteristic-zero vanishing. For the
contradiction itself, even that equality can be weakened: Riemann--Roch
and h2(-K)=h0(2K)=0, since 2K.L=-4, already give h0(-K)>=2. Together
with h0(L)=4, any independent pair supplies the same quadratic
equation. Thus no positive-characteristic conclusion about exact
anticanonical cohomology is being inferred from Kawamata--Viehweg.

The square-product lemma was also checked independently by a separate
bounded algebraic audit. That agreement is an audit record; the proof
is the explicit generic-point argument in Step 4.


---

## Source: 2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md

# Independent audit: exceptional curves and the two genus-two mate strata

Date: 2026-10-09. Auditor: `genus_two_adjoint_audit`. Status:
**PROVED HERE / independently accepted as bounded structural
reductions**. This extends the [independent adjoint audit](#source-2026-10-09-session-genus-two-adjoint-independent-auditmd).
No frontier file was edited. The genus-two mate problem
remains open.

Keep the characteristic-zero hypotheses and notation of that audit.
Thus M is a smooth rational minimal resolution of the normal
quartic normalization S, L is the pulled-back ample hyperplane,
L^2=4, K.L=-2, K^2=0, h0(L)=4, and

    f=K+L

is the class of a connected rational conic-fibration fiber. Its
complete |L| map is birational onto the actual integral quartic X.

## 1. A useful numerical-to-linear and quadratic-product lemma

If N is a numerically trivial integral divisor class on M, then
chi(N)=1 and h2(N)=h0(K-N)=0: (K-N).L=-2 excludes an effective
representative. Thus h0(N)>=1. Its effective representative is
numerically zero, so ample intersection forces it to be zero.
Consequently N~0. This direct argument establishes every
numerical-to-linear upgrade below without relying on an incomplete
Picard torsion-freeness assertion.

If L~2B+T for an integral divisor class B with h0(B)>=2 and an
effective divisor T, two independent sections u,v of B give three
independent sections s_T u^2,s_T uv,s_T v^2 of L. Independence
follows by dividing at the generic point by s_T v^2 and using that
u/v is nonconstant and transcendental over the algebraically closed
ground field. Extending them to a basis of H0(L) imposes the
nonzero relation X0X2-X1^2=0 on the actual quartic image. This is
impossible. Fixed components of B or T and common zeros of u,v
do not invalidate a global identity of sections.

In particular L is not divisible by two in Pic(M). If L~2B, then
B^2=1, K.B=-1, and

    chi(B)=1+(B^2-K.B)/2=2,
    h2(B)=h0(K-B)=0

because (K-B).L=-4. Hence h0(B)>=2 and the preceding contradiction
applies.

## 2. Exceptional primes are vertical (-2)-curves or horizontal (-3)-sections

Let E be an integral sigma-exceptional prime. Then L.E=0 and
E^2<0. Relative minimality and adjunction give K.E>=0 as in the
genus-one audit. Put

    d=f.E=K.E>=0,     Q=K+L/2.

The rational numerical class Q belongs to L-perpendicular and has
Q^2=-1. The Hodge pairing is negative definite on this
perpendicular space. Cauchy--Schwarz for its negative gives

    d^2=(Q.E)^2 <= -E^2.

Adjunction gives -E^2=d+2-2p_a(E), so

    d^2 <= d+2-2p_a(E).

For d=0, negative self-intersection and adjunction force p_a(E)=0
and E^2=-2. Thus E is a smooth rational vertical (-2)-curve.

For d>0 the inequality gives d<=2. If d=1, the restriction of the
adjoint ruling to E is a finite degree-one map E->P1. It is an
isomorphism since the target is normal and both curves are
integral. Thus E is a smooth rational section and E^2=-3.

If d=2, the inequality forces p_a(E)=0, E^2=-4, and equality in
Cauchy--Schwarz. Consequently E is numerically -2Q=-2K-L.
The numerical-to-linear lemma upgrades this to E~-2K-L, or

    L~2f+E.

Here E is effective and h0(f)=2, so the quadratic-product lemma
excludes this case. Therefore every exceptional prime is either
a vertical smooth rational (-2)-curve or a horizontal smooth
rational (-3)-section.

## 3. There are at most two horizontal exceptional sections, and they are disjoint

Let E1,E2 be distinct horizontal exceptional sections and t=E1.E2.
Distinct curves on smooth M give t>=0. Their sum T satisfies

    Q.T=2,     T^2=-6+2t.

Cauchy--Schwarz gives 4<=6-2t, so t<=1. If t=1, equality gives
T numerically -2Q. The same numerical-to-linear upgrade yields

    L~2f+T,

contradicting the quadratic-product lemma. Thus t=0: all
horizontal exceptional sections are pairwise disjoint. This is
stronger than the preliminary bound t<=1.

Suppose that three such sections E1,E2,E3 exist. Their disjoint
sum T has T^2=-9 and Q.T=3. Equality in Cauchy--Schwarz gives

    T numerically -3Q,
    2T numerically -6K-3L.

The integral divisor 2T+6K+3L is numerically trivial and therefore
linearly trivial. Rearranging gives

    L~2(-3K-T-L).

This contradicts the nondivisibility of L proved in section 1.
There are consequently at most two horizontal exceptional
(-3)-sections, and they are disjoint.

## 4. The correct mate identity retains two different strata

Assume now that an ambient mate of degree b exists. The accepted
[full-support and smooth-lift identities](../supplements/SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md)
give a smooth embedded curve c in S isomorphic to the degree-four
rational C and an effective pullback divisor on M

    div_M((nu sigma)^*G)=b c# + W ~ bL,

where W is supported on the sigma-exceptional locus and c# is the
smooth strict transform. Put Z=W/b, an effective rational
exceptional divisor, so c# is numerically L-Z and L.Z=0. Define

    q=-Z^2,     lambda=K.Z.

Here q>0 by negative definiteness. Also lambda>=0 by section 2,
and lambda is an integer since it equals K.(L-c#). Adjunction
to c# gives the actual general relation

    -2=c#^2+K.c#=(4-q)+(-2-lambda),
    q+lambda=4.

In particular one must not assert q=4 before proving lambda=0.
The noncrepant horizontal (-3)-curves make the distinction
material. As Q.Z=lambda, Cauchy--Schwarz gives lambda^2<=q.
Together with q+lambda=4 and integral lambda>=0 this leaves
exactly

    lambda=0, q=4, c#^2=0, f.c#=2;
    lambda=1, q=3, c#^2=1, f.c#=1.

The first stratum has a rational bisection c# and Z supported
only on vertical (-2)-curves. For any horizontal exceptional
section E, effectivity gives Z.E>=0, while

    Z.E=(L-c#).E=-c#.E<=0.

Thus c#.E=Z.E=0 in the first stratum: the bisection and the
support of its correction avoid the horizontal exceptional
sections.

The second stratum has a rational section c#. The sum of the
coefficients of horizontal exceptional sections in Z equals one;
vertical correction components can still occur. Section 3 shows
there are at most two such horizontal primes. No argument here
excludes this section stratum.

The auditor initially sent an unsaved informal proposal that
started from Z^2=-4 in all genus-two cases. The owner and root
immediately identified the omitted K.Z term. That proposal was
retracted. The two-stratum identity
above is the corrected accepted assertion; this audit preserves
the surviving noncrepant section case explicitly.

## 5. A smooth embedded lift meets an exceptional fiber transversely at one prime

The curve c is smooth and the proper birational map c#->c is
finite and hence an isomorphism. Therefore above each point p of
c, the strict transform has one point P.

If p is singular on S, choose a local function a in m_(S,p)
whose restriction to c is a uniformizer. Such a function exists
because O_(S,p)->O_(c,p) is surjective. Its pullback to M vanishes
with positive integral coefficient along every exceptional prime
above p. The smooth local ring O_(M,P) is factorial. Restriction
of the pullback to c# has order exactly one at P, whereas its
order is at least the sum of the local intersection
multiplicities of c# with all exceptional local branches through
P. Every such multiplicity is positive. It follows that:

* exactly one exceptional prime passes through P;
* that prime is smooth at P and meets c# transversely;
* c# meets no other point of the same exceptional fiber.

In particular c#.E is zero or one for every exceptional prime E,
and there is at most one positive intersection in each connected
exceptional fiber. This constraint uses the smooth embedded lift,
not a Cartier assumption on c. It can be applied to both mate
strata, but alone it is not a classification of the exceptional
intersection graph or a proof that lambda=1 is impossible.

## 6. Accepted boundary

Sections 1--5 are exact divisor and local-ring arguments. They do
not assume that S has ADE singularities or that the adjoint
ruling descends to S. They do not identify the conductor or prove
that every possible normalization fiber has been exhausted. The
vertical (-2) exceptional configurations and their integral
saturation, the noncrepant section stratum, and descent of a
hypothetical mate all remain separate obligations. No numerical
or computational enumeration is asserted here.



## Consolidated historical supplement: `research/supplements/PROJECTION_CONDUCTOR_CONTACT_AND_PHASE.md`

# Projection contact, conductor budgets, and actual phase tests

Fix characteristic zero. A primitive upstairs Cartier ray is not a mate until
its powers descend through the **entire** conductor. This chapter owns the
projective contact test, its canonical weighted bounds, actual projection
coordinates, and controls showing why scalar phases remain a separate problem.
The [full family theorem](../supplements/PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md#actual-families-and-their-finite-phase-image)
owns specialization, logarithmic equations, and the finite phase cover; its
proof retains every admissibility and nilpotent condition. The
[universal unit-descent algebra](../supplements/CONDUCTOR_DESCENT_ALGEBRA.md) owns the full
Artinian logarithm/Kummer proof. These links are theorem dependencies, not an
assertion that either phase image has been computed for the fixed quartic.

**Review.** The scoped contact, budget and split-control arguments have
inherited independent source review. The later audited family theorem replaces
the preliminary finite-phase construction, including its specialization repair.
Independent replacement review accepted the corrected proof preservation,
controls, constants, and scope. No material finding remains.

<a id="2026-10-14-generalization-projection-ray-and-split-phase-model"></a>

## Actual projection spaces and the one-ray membership problem

### 1. The finite-dimensional projection spaces

The [Cartier-lift theorem](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md)
leaves three fixed-C0 models after accepted quartic exclusion:

    smooth quadric, H=(2,2), c=(1,1);
    quadric cone, H=2c, c smooth Cartier conic;
    plane, H=4h, c a line.

All have a primitive normalized section `Q in H0(S,H)` with divisor
`2c` or `4c`, respectively. The normal mate ray is precisely `Q^b`.
This is already a reduction of all mate degrees to one distinguished
section, but descent of its powers remains a global problem.

Fix the isomorphism of `c` with the literal C0 parametrization, and
write `W=span(s^4,s^3t,st^3,t^4)` in `H0(c,O(4))`. For a smooth
quadric, restriction

    H0(S,O(2,2)) -> H0(c,O(4))

is surjective and has kernel `H0(O(1,1))`, of dimension four. For
the plane with `H=4h`, its kernel is `ell H0(O(3))`, of dimension
ten, where `ell=0` is `c`. The same cone dimension is four, obtained
from its Cartier sequence. Once a splitting of restriction is fixed,
every four-coordinate subspace mapping isomorphically to `W` is the
graph of a linear map from `W` to this kernel. Thus the parameter
spaces before quotienting surface symmetries have affine dimensions
16 for either degree-eight model and 40 for the degree-sixteen model.

Four sections must have no base point. Since `H` is ample, their
resulting morphism is automatically finite: a positive-dimensional
fiber would have zero `H` degree. Birationality onto the image is an
additional condition. On that locus the model is the actual finite
normalization, and the image degrees are eight or sixteen.

The full support condition is exact and finite-dimensional: pull back
the actual generators of `I_C0` through the four sections and require
the radical of their sheaf ideal on `S` to be `I_c`. This retains every
extra isolated inverse point and every extra prime. It is not implied
by the fixed restriction to `c`.

### 2. Exact section-ring condition and what it does not bound

Let

    B=direct_sum_(b>=0) H0(S,bH),
    R=k[U0,U1,U2,U3] subset B,

where the four actual projection sections generate `R`. The carrier
is a hypersurface in P3, so its ambient degree-`b` forms supply all
sections of `O_X(b)`, by `H1(P3,O(b-a))=0`. Consequently

    a mate of degree b exists iff Q^b belongs to R_b.        (1)

When the projection is finite birational, `B` is a finite graded
module over `R` (it is the section module of the finite coherent
normalization algebra), and `Q` lies in the common fraction field.
The intermediate algebra `R[Q]` is finite birational. Thus (1) is an
actual power-membership condition in one finite ambient module,
equivalently the full conductor descent of one primitive ray.

The conductor theorem compresses single-field residual algebras.
Split residual products instead retain scalar root-of-unity phases.
Finite-dimensional parameter spaces or a finite normalization module
do not by themselves bound the orders of those phases. The exact
example below preserves full support and a smooth degree-one lift,
so these hypotheses cannot silently remove the phase problem.

<a id="2026-10-14-generalization-projection-contact-phase-criterion"></a>
<a id="2026-10-14-generalization-projection-contact-phase-independent-review"></a>

## Entire contact divisors and residual phases

### 1. Exact contact criterion

Let `nu:S->X` be a finite birational normalization of an integral
projective surface over an algebraically closed characteristic-zero
field `k`. Assume `X` is Cohen--Macaulay for the global descent
conclusions in Section 5; the residual contact criterion itself does
not require this extra hypothesis. Let `C subset X` be integral, with full reduced inverse
image a single smooth Cartier curve `c` mapped isomorphically to `C`.
Let `H=nu*L`, where `L` is ample on `X`, and assume that an upstairs
section `Q of H` has divisor

    div(Q)=m c,    m>0.                                    (1)

In particular `c` is ample. Let `eta` be a generic conductor point
whose curve is different from `C`. Write the actual reduced
normalization conductor algebra there as

    E=product_i E_i,    K=k(eta),

where each `E_i/K` is finite and separable. `Q` is a unit in the
entire conductor algebra at `eta`, because its zero divisor is
supported only on `c`.

For every component of the reduced geometric-pair correspondence
above `eta` whose two geometric entries differ, take its projective
closure in `S x_X S` and its normalization `T`. The projections
`p_1,p_2:T->S` are finite onto curves. There is a canonical
identification

    p_1*H=p_2*H,

because `nu p_1=nu p_2`. Thus the ratio

    rho_T=p_1*Q/p_2*Q

is a nonzero rational function on the proper integral normal curve
`T`, with exact divisor

    div(rho_T)=m(p_1*c-p_2*c).                             (2)

**Theorem.** The residual class of `Q` in `E*/K*` is torsion if and
only if, on all these finitely many correspondences:

    p_1*c=p_2*c as entire effective divisors;               (3)
    the resulting constant rho_T belongs to mu_infinity(k). (4)

Diagonal pair components have ratio one and require no test. An
off-C unibranch conductor with residual field `E=K` therefore has no
residual obstruction; its full nilpotent obstruction can still be
nonzero. Components dominating `C` are deliberately excluded from
this unit criterion. The accepted conductor theorem handles their
vanishing by a sufficiently large positive power. Consequently this
part of the theorem allows the carrier to be generically singular
along `C`; generic regularity is needed only in Section 3 below.

Proof. The divisor formula follows from (1) and the canonical
line-bundle identification. A rational function on a proper normal
integral curve over `k` has zero divisor exactly when it is a
nonzero constant: it and its inverse are then regular, and proper
integrality gives `H0(T,O_T)=k`. This proves the equivalence between
constant ratios and (3).

Choose a rational frame of `L` at `eta`, and write the residues of
`Q` as `alpha=(alpha_i) in E*`. A power `alpha^N` belongs to the
diagonal `K*` if and only if all its geometric values agree. In
characteristic zero, base change to a separable algebraic closure
of `K` identifies these values with the factors of `E tensor_K
Kbar`; the equality test consists exactly of the geometric-pair
ratios above. Hence residual torsion implies every `rho_T^N=1`.
Conversely, if all ratios are roots of unity, their finitely many
orders have a common multiple `N`. All geometric values of
`alpha^N` agree; faithful scalar descent then puts `alpha^N` in
`K*`. This is the desired residual torsion. No reduced test is used
to claim full conductor descent.

### A sharper single-field consequence

If `E` is one field, condition (3) on every conjugate-pair
correspondence already implies (4). To see this, pass to a finite
Galois closure `K'/K` and a representative `alpha in K'`. Constant
conjugate ratios give

    sigma(alpha)/alpha=chi(sigma) in k*.

Galois automorphisms fix `k`, so `chi` is a homomorphism from a finite
group to `k*`; its values are roots of unity. Thus the single-field
residual test is just equality of contact divisors. For several
fields, the constants comparing different field factors need not
be roots of unity. These relative split phases remain a real
condition and can have unbounded finite orders.

### 2. All residual information is read at contact points

Every `T` above meets `c` under either projection, since its image
is a curve and `c` is ample. Full inverse support implies

    supp(p_1*c)=supp(p_2*c).                               (5)

Indeed `p_1(t) in c` implies `nu p_2(t) in C`, so `p_2(t) in c`;
the reverse implication is identical. As `nu|c` is an isomorphism,
each such pair equals `(P,P)` for one point `P in c`.

Equality of supports (5) does not imply equality of multiplicities
in (3). An unequal contact order is an immediate all-power
exclusion: `rho_T` has a zero or pole, and no positive power can
become a constant. If the orders agree, one contact point suffices
to evaluate the constant ratio.

More precisely, choose a local equation `q` of `c` at `P`, a
uniformizer `z` on `T` at `t`, and write

    q(p_1(z))=beta_1 z^r+...,   q(p_2(z))=beta_2 z^r+...,
    beta_1 beta_2 != 0.

Using the same local frame of `O_S(c)` at the common point `P`,
equation (1) and the canonical `H` frame show

    rho_T(t)=(beta_1/beta_2)^m.                            (6)

The unit multiplying `q^m` has the same value at `p_1(t)=p_2(t)=P`
and cancels. Formula (6) is coordinate independent as a ratio. Thus
one computes the correspondence and its contact orders once, then
reads a residual phase from local leading terms; one does not
solve a separate power-membership problem for every mate degree.

For a component joining branch curves `D_i,D_j` with projection
degrees `e_1,e_2`, a useful necessary numerical test from (3) is

    e_1(c.D_i)=e_2(c.D_j).                                (7)

This total-degree equality is weaker than the required pointwise
contact-divisor equality and must not replace it.

### 3. Every contact lies at transverse degeneracy

Now also assume `X subset P3` and that `X` is regular at the generic
point of `C`. The accepted
transverse theorem supplies the generically nonzero map

    alpha:O_c(c)->N_C/P3

and its entire effective common-zero divisor `A`. Every contact
point of an off-C conductor correspondence lies in `supp(A)`.

Here is a local proof of the new assertion. If `alpha(P)!=0`, the
map `S->P3` is immersive at `P`: its tangent on `c` is injective,
and its transverse normal image is nonzero. The fibre of `nu` over
`nu(P)` is a singleton, by full inverse support and the isomorphism
on `c`. Let `R=O_X,nu(P)` and let `B` be the finite local
normalization algebra above it. Cotangent surjectivity from the
immersion gives `m_R B=m_B` by Nakayama. Thus `B/m_R B=k`; another
application of Nakayama to the finite `R`-module `B` says that `1`
generates `B`, so `R->B` is surjective. It is also injective, hence
an isomorphism. There is therefore no conductor curve through `P`
upstairs. Any contact with an off-C conductor curve forces
`alpha(P)=0`.

For the three accepted fixed-C0 Cartier-lift models this puts all
residual correspondence contacts at at most five or six points:

| Normalization and polarization | `m` | Maximum `deg(A)` |
|---|---:|---:|
| `P1 x P1`, `H=(2,2)`, `c=(1,1)` | 2 | 5 |
| Quadric cone, `H=2c`, `c` a Cartier conic | 2 | 5 |
| `P2`, `H=4h`, `c` a line | 4 | 6 |

These are numbers of possible distinct contact sites, bounded by
the degree of the **entire** degeneracy divisor. They do not bound
the number of correspondence branches, their contact orders, or
the orders of their constant phases. At a cone vertex the lift
curve does not pass through the singularity, because a smooth
Cartier curve forces the surface smooth along it; the proof above
is consequently valid in all three models.

### 4. A literal sixteen-parameter quadric correspondence

On `S=P1_(s:t) x P1_(u:v)`, put

    q=sv-tu,    c=(q=0),    Q=q^2,
    P0=s^2 u^2,
    P1=su(sv+tu)/2,
    P2=tv(sv+tu)/2,
    P3=t^2 v^2.

These restrictions to `c` are the prescribed literal quartic
coordinates `(s^4,s^3t,st^3,t^4)`. Every four-coordinate lift with
these fixed restrictions is uniquely

    U_i=P_i+q L_i,  0<=i<=3,
    L_i=a_i su+b_i sv+c_i tu+d_i tv.                       (8)

The sixteen coefficients are the entire projection family before
quotienting automorphisms. On the basepointfree finite birational
locus the image is an integral degree-eight hypersurface. This
parameterization uses the accepted restriction-sequence reduction;
the symmetric `P_i` make the two projections in the fibre product
particularly explicit.

### The first jets are precisely an arbitrary pair of quintics

The universal family has an explicit linear first-jet quotient. On
the chart `s=u=1`, write `t=x,v=x+n`, so `q=n`, and put

    f_i(x)=L_i|c=a_i+l_i x+d_i x^2,    l_i=b_i+c_i.

Normalize the image coordinates by `U0`. Their transverse derivative
at `n=0` is

    v1=1/2+f1-x f0,
    v2=(3/2)x^2+f2-x^3 f0,
    v3=2x^3+f3-x^4 f0.

Taking the derivatives of the two local normal equations
`X2-X1^3` and `X3-X1^4` gives

    a=f2-3x^2 f1+2x^3 f0,
    b=f3-4x^3 f1+3x^4 f0.

The balanced pair is

    A=a=f2-3x^2 f1+2x^3 f0,
    B=2b-3x a=2f3-3x f2+x^3 f1.                          (8a)

Both have degree at most five. This is an actual balanced normal
frame, including infinity. On the reciprocal source chart take
`x'=1/x` and `n'=1/(x+n)-1/x`; the reciprocal target curve
coordinate is `X2/X3`. Direct differentiation of the analogous
normal equations gives

    A_infinity=-x^(-5) B,    B_infinity=-x^(-5) A.          (8b)

The constant interchange of the frame does not change the common
zero divisor. Thus the homogenizations

    A_h(s,t)=s^5 A(t/s),    B_h(s,t)=s^5 B(t/s)

represent the entire normal map `O(2)->O(7)^2`, and its degeneracy
divisor is exactly the homogeneous gcd divisor of `A_h,B_h`, with
full multiplicity and infinity retained. When they are not both
zero its degree is at most five. When both vanish the projection
is generically nonimmersive along `c` and belongs to the separate
thick-carrier boundary.

The twelve coefficients `(a_i,l_i,d_i)` map **isomorphically** to
the twelve coefficients of the arbitrary pair `(A,B)`. In fact,
if `A=sum A_j x^j` and `B=sum B_j x^j`, the explicit inverse is

    d0=A5/2,         l0=(A4+3B5)/2,   a0=(A3+3B4)/2,
    d1=B5,           l1=B4,           a1=-(B3+3A2)/8,
    d2=-(A2+3B3)/8,  l2=A1,           a2=A0,
    d3=(B2+3A1)/2,   l3=(B1+3A0)/2,   a3=B0/2.             (8c)

Direct coefficient extraction also checks the inverse without a rank heuristic:

    A=(a2,l2,d2-3a1,2a0-3l1,2l0-3d1,2d0),
    B=(2a3,2l3-3a2,2d3-3l2,a1-3d2,l1,d1).

On the reciprocal source chart, n'=-n/x²+O(n²). The two unbalanced target
normal derivatives against the old n are x^-7(2b-3xa), x^-8(3b-4xa).
Multiplying by -x² and balancing gives precisely (8b). Thus the source
normal factor and target-coordinate scale are both retained.

The other four parameters `b_i-c_i` vary the coefficients of
`q^2` in the four `U_i`; they affect second and later jets while
leaving (8a) unchanged. This surjectivity is a statement about the
entire lift vector space. It does not say that every quintic pair
has a basepointfree, birational, full-support admissible projection,
or that a first-jet pair determines its conductor. Equations
(8a)--(8c) make the degree-one-through-five gcd strata and their
four independent higher-jet parameters explicit for further work.

The actual equality-of-image locus in `S x S` is defined by all six
minors

    U_i(P)U_j(P')-U_j(P)U_i(P'),    0<=i<j<=3.             (9)

For the residual test, remove the diagonal locus and take the
projective closure, then normalize each curve component dominating
an off-C conductor curve. Its contact divisors are obtained by
pulling back `q(P)=0` and `q(P')=0`. Under the canonical matching
of `H`, the ratio is

    rho_T=q(P)^2/q(P')^2,                                 (10)

with the equality-of-image scale included through that line-bundle
identification. If homogeneous representatives are used with
`U_i(P')=lambda U_i(P)`, the scalar version of (10) is
`lambda q(P)^2/q(P')^2`; omitting this factor would give the wrong
invariant. In a common target-coordinate frame, the formula is the
ratio of `q^2/U_i` on the two branches. At a contact point, the
scalar factor tends to one in the common source frame, yielding
the square of the contact leading-coefficient ratio in (6).

Taking the closure retains all contact points on the diagonal.
Reducing and normalizing (9) is used only for the residual-field
test; it does **not** compute the full conductor or its nilpotent
logarithmic defect. Full support is separately imposed by the
pullback ideal of literal `C0`, retaining every possible isolated
inverse point. The basepoint, finite-birational, full-support, and
entire conductor conditions remain mandatory throughout (8).

### 5. Exact integration with full conductor descent

For a fixed projection satisfying these hypotheses, with `X`
Cohen--Macaulay as in every hypersurface model here:

1. Compare the finitely many full contact divisors on the actual
   residual correspondences. Any mismatch excludes every mate.
2. Evaluate the resulting constant phases by (6). A non-root-of-
   unity split phase excludes every mate. Single-field components
   require no additional root-of-unity test after all conjugate
   contacts match.
3. If all residual classes are torsion, compute the full Artinian
   conductor logarithmic defects from the accepted conductor
   theorem. Each must vanish. A reduced correspondence cannot
   replace this step.
4. If the defects vanish, the conductor theorem gives eventual
   descent. When `X` is an integral hypersurface in `P3`,
   `L=O_X(1)`, and the carrier is generically regular along `C`, the
   minimum ambient mate degree is the exact residual order of `Q`.
   For the general polarized surface, the statement concerns the
   least descending tensor exponent rather than an ambient degree.

This is a finite geometric criterion on a **chosen** projection,
not an effective algorithm over arbitrary unspecified coefficient
fields, and not a proof that every parameter stratum is covered.
Root-of-unity membership still depends on the coefficient field;
its orders can be unbounded in a family. The accepted affine split
phase example is consistent with (6): arbitrary ratios of branch
slopes give arbitrary finite phases after squaring or taking fourth
powers. The new projective gain is that every residual component
must meet the ample lift and its entire function-field ratio is
controlled by its contact divisor and a leading coefficient at one
of at most five or six degeneracy points. This is a structural
target across all mate degrees, rather than a mate-degree search.

### 7. A uniform mate bound in the single-field sublane

There is a quantitative consequence for all projections in each
fixed model, rather than only one carrier. If `nu:S->X subset P3`
is finite with `nu*O_X(1)=H` and `H^2=a`, then at any point with
residue field `K` its normalization residue degrees obey

    sum_i [E_i:K] <= a.                                  (11)

Indeed, over `K`, choose a line through the corresponding `K`-point
of `X_K` that is not contained in `X_K`. Two target hyperplanes
cutting that line pull back to a proper zero-dimensional
intersection of two `H_K` divisors, of total length `H^2=a`.
The entire scheme fibre is a closed subscheme of that intersection,
so its length is at most `a`; its reduced residue degrees have at
most that sum. The infinite field `K` ensures such a line can be
chosen. This proof does not assume that the finite normalization
is flat.

Suppose now the carrier is generically regular along `C`, every
off-C generic conductor residual algebra consists of a **single**
field, and a mate exists. The accepted characteristic-zero theorem
then makes each exact local descent order divide its field degree.
Vanishing of the full logarithmic defects follows from actual mate
existence. The minimum mate degree is their least common multiple,
so (11) gives the uniform divisibility bounds

    degree-eight models:     b_min divides lcm(1,...,8)=840;
    degree-sixteen model:    b_min divides lcm(1,...,16)=720720. (12)

These are conservative uniform bounds, not assertions that those
large degrees are necessary or that checking them is a practical
computation. In particular, in this sublane it is enough to test
one fixed power `Q^840` or `Q^720720` on the **full** conductor,
rather than arbitrary powers: an existing mate forces that power
to descend, and descent of that power constructs a mate. This
last equivalence retains the nilpotent defect. A single reduced
test still cannot decide it.

The hypothesis that the carrier is generically regular along `C`
removes the separate conductor vanishing threshold on `C`. No
bound in (12) is asserted here for the thick-on-C boundary. No
split-conductor phase is bounded by (11): even two degree-one
residual fields can have an arbitrary-order relative root of
unity. The contact criterion in Sections 1--3 remains the exact
replacement for that false inference.

### 8. A deliberately preserved failed global phase construction

The [opposite-ruling normal form](carrier_conductor_differential_comparison.md#the-opposite-ruling-pairing-and-its-complete-coefficient-freedom)
gives the entire coefficient family for the specified pairing
`(x,0)<->(0,a x)` through one diagonal point. It retains arbitrary
four-vectors `D,E`; its branchwise phase is `a^(-2)`. This is a
new exact incidence subfamily and imposes no phase-order bound.

The especially sparse coefficient choice `D=W2,E=u W2` yields a
basepointfree finite projection, but the [full-support failure
shield](spectral_pushforward_powers.md#2026-10-14-quadric-opposite-ruling-phase-family-failure)
shows that it always has an extra off-diagonal inverse point above
the infinite endpoint of literal C0. The two boundary obstructions
would require simultaneously `u=0` and `u=1` to disappear.
Consequently it supplies no admissible fixed-C0 carrier. This
failure does not exclude the full `D,E` normal form: linearly
independent projected coefficient pairs can remove that particular
boundary obstruction. The entire full-support and nilpotent
descent problem remains for that broader family.

<a id="2026-10-14-generalization-projection-conductor-contact-budget"></a>
<a id="2026-10-14-generalization-projection-conductor-budget-independent-review"></a>

## Canonical conductor and ordered contact budgets

### 1. General theorem

Let `nu:S->X subset P3` be a finite birational normalization of an
integral degree-`a` hypersurface over an algebraically closed field of
characteristic zero. Let `C subset X` be a smooth degree-`d`, genus-`g`
curve with full reduced inverse image a
single smooth ample Cartier curve `c`, mapped isomorphically to `C`.
Assume `X` is regular at the generic point of `C`. The Cartier-lift
lemma makes `S` regular along `c`. Put `H=nu*O_X(1)` and `k=c^2`.

Finite duality identifies the **actual** upstairs conductor ideal with
`omega_S tensor nu*omega_X^(-1)`. A normal surface is Cohen--Macaulay,
and its canonical sheaf is rank-one reflexive. Thus the conductor is
the divisorial ideal of an effective Weil divisor `B`:

    conductor O_S = O_S(-B),
    B ~ (a-4)H-K_S,
    N := B.c = d(a-4)+k-(2g-2).                    (1)

This statement identifies the actual ideal, not only its double dual;
there is no discarded zero-dimensional ideal defect. Globally `B`
need not be Cartier. It is Cartier near `c`, because `S` is regular
there, and this is enough to define `B|c` and its degree. Adjunction
near `c` proves the formula for `N`. If `S` is Gorenstein, `B` is
Cartier globally.

Write its effective Weil divisor as `B=sum_i m_i D_i`, with the `D_i`
distinct prime curves and `m_i>=1`. No `D_i` equals `c`, because the
normalization is an isomorphism at the generic point of `C`. Then

    sum_i m_i (D_i.c) = N.                          (2)

Every `D_i.c` is a strictly positive integer since `c` is ample.
Consequently:

* There are at most `N` prime conductor curves, and each generic
  conductor multiplicity `m_i` is at most `N`.
* If `D_i^nor` is the normalization of `D_i`, the sum of the vanishing
  orders of `c` on all its branches is `D_i.c`. Thus every such branch
  contact order, and the number of branches meeting `c`, is at most
  `N`; their sum with weights `m_i` is exactly `N`.
* The exact first-symbol bridge is

      Z(F_1) = B|c + A,                             (3)

  where `A` is the entire zero divisor of the normalization normal
  differential. In particular (2) concerns the full conductor contact,
  including multiplicities, rather than only its reduced support.

Here `F_1` is the actual first normal symbol of the carrier equation.
The local proof below establishes (3). The contact graph bounds (1)--(2)
use finite duality directly and do not depend on that differential identity.

### Proof of the actual conductor and first-symbol identity

For a finite birational extension `A subset B` with common fraction field,
every `A`-linear map `B->A` is multiplication by a fraction. Consequently
`Hom_A(B,A)` is the actual conductor `{q:q B subset A}`, not merely its
reflexive hull or its divisorial support. Since `A` is Gorenstein and `B`
is Cohen--Macaulay, finite canonical duality gives

    omega_B = Hom_A(B,A) tensor_A omega_A.

On a Gorenstein normalization the conductor is invertible globally. On a
normal normalization it is the actual rank-one reflexive canonical ideal;
smoothness near c still makes it invertible there. The local argument below
therefore applies near c without assuming global Gorensteinness.

The new local bridge was independently reconstructed in completed regular
coordinates. Take source coordinates `(t,u)`, with `c=(u=0)`, and ambient
coordinates `(x,y,z)` with `C=(y=z=0)` and `nu*x=t`. Write `nu=(t,Y,Z)`.
If `h` generates the actual conductor and `eta=dx wedge dy/F_z` generates
the hypersurface dualizing module, then `h nu*eta` is a generator of
`omega_S`. Hence there is one common unit `epsilon` satisfying

    F_z composed with nu=epsilon h Y_u,
    F_y composed with nu=-epsilon h Z_u.

At least one of these rational residue expressions is available generically:
the map is birational and is an isomorphism at the generic point of the
hypersurface. The equalities extend in the regular local ring. Restriction
to `u=0` gives the exact DVR-ideal equality

    (F_y|C,F_z|C)=(h|c)(Y_u|c,Z_u|c).

Taking orders proves the entire divisor identity

    Z(F_1)=B|c+A.

This argument uses the actual invertible conductor before restricting to
`c`; it avoids the possible codimension-two error in restricting only a
Weil-divisor or reflexive-hull identity. It also keeps isolated zeros of
the transverse differential. Smoothness along `c` follows from the accepted
smooth Cartier-curve lemma. The quadric cone is Gorenstein and its smooth
Cartier conic avoids the vertex, so that model satisfies the hypotheses.

### 2. A bound on the entire off-diagonal pair correspondence

For every image conductor curve `Delta subset X`, let

    K=k(Delta),    E=product_(i over Delta) E_i,
    E_i=k(D_i),   d_Delta=sum_i [E_i:K].

The accepted fiber-degree argument gives `d_Delta<=a`. Characteristic
zero makes each extension separable. Fix a prime `D_i` over `Delta`.
The reduced generic algebra of all pairs with first entry on `D_i` is

    E_i tensor_K E,

of rank `d_Delta` over `E_i`. Its diagonal component is one factor
`E_i`, of rank one. Removing it leaves total rank `d_Delta-1`.
Normalizing and taking projective closures therefore gives finitely
many integral off-diagonal pair curves `T`, with finite first projection
`p_1:T->D_i`, satisfying the exact equality

    sum_(T with first image D_i) deg(p_1) = d_Delta-1 <= a-1. (4)

This includes conjugate pairs on one irreducible conductor curve as
well as pairs between different conductor curves. When `E=K` there
are no off-diagonal curves, consistent with (4). Generic nilpotents
are deliberately absent from this pair construction, but are retained
in the conductor divisor `B` and in the final full descent condition.

Pullback of the Cartier divisor `c` to each proper normal curve `T`
has total degree `deg(p_1)(D_i.c)`. Summing (4) over all first images
and then using (2) gives the uniform bound

    sum_T deg(p_1*c)
      = sum_i (d_(image D_i)-1)(D_i.c)
      <= (a-1) sum_i D_i.c
      <= (a-1)N.                                    (5)

The index `T` in (5) means the integral components of the **ordered**
off-diagonal pair correspondence. In particular a component invariant
under exchange is counted once as an integral component, rather than
being artificially doubled. The equality is the decomposition of
the finite algebra over each fixed first image, so there is no missing
conjugate-pair degree or extra factor of two.

Because `c` is ample, every `p_1*c` is a nonzero effective divisor.
Hence (5) bounds all of the following by `(a-1)N`: the number of pair
components, the number of their contact branches counted with
multiplicity, and any single contact order on their normalizations.
These quantities were not bounded by the size of the degeneracy
support alone.

### 3. The three surviving fixed-C0 models

The accepted normal splitting `N_C0/P3=O(7)^2` and transverse theorem
place every conductor contact in the support of `A`, whose degree
is at most five or six. Equations (1)--(5) supply the additional
global weighted bounds:

| Normalization and polarization | `B` class | `N=B.c` | `deg A` bound | Ordered pair contact budget |
| --- | --- | ---: | ---: | ---: |
| `P1 x P1`, `H=(2,2)`, `c=(1,1)` | `(10,10)` | 20 | 5 | 140 |
| Quadric cone, `H=2c`, `c` a smooth conic | `10c` | 20 | 5 | 140 |
| `P2`, `H=4h`, `c=h` | `51h` | 51 | 6 | 765 |

The quadric cone is Gorenstein, and `c` avoids its vertex. Thus its
global conductor class is Cartier and its local contact calculation
occurs entirely in the smooth locus. No resolution at the vertex is
being silently inserted.

These inequalities put the incidence into finitely many **combinatorial
weighted contact graph types**. Vertices can record the at most five or
six sites on `c`, the prime conductor branches and their positive
integer weights. Edges record ordered pair branches and their positive
contact orders, with total edge weight bounded by 140 or 765. The
actual curves, contact locations, correspondence maps and leading
coefficients still vary in families. Finitely many graph types do not
mean finitely many projection parameters or finitely many phase values.

### 4. Consequence for the general strategy and retained boundaries

The accepted projective criterion requires, on every pair curve `T`,
equality of the entire divisors `p_1*c` and `p_2*c`, followed by a
root-of-unity test on the resulting constant ratio. The new theorem
bounds the amount of integer contact data needed to formulate these
tests uniformly on each normalization model. It does not require
enumerating possible mate powers.

There is still no bound here on the order of a split scalar phase.
Even one edge with contact order one can carry an arbitrary-order
root of unity in the local split model. Canonical conductor duality
constrains that edge's integer contact data, not its scalar label.
The entire nilpotent logarithmic conductor defect must also vanish;
the reduced correspondence and (1)--(5) do not prove this vanishing.

The theorem applies more generally to any smooth ample Cartier lift
on a normal projective-hypersurface normalization, with the uniform
quantity `N` in (1). Global Gorensteinness is unnecessary: the actual
reflexive conductor ideal and smoothness along `c` suffice. For
non-Cartier lifts the contact divisor needs replacement; for a lift
through singular points of the normalization the local bridge needs
replacement; and for carriers generically
singular along `C`, the conductor can contain `c`, so its restriction
in (2) is not defined as an effective finite divisor. Those strata
are not covered by this theorem. It does not resolve the universal
integral-curve STCI problem or the unrestricted fixed-C0 problem.



## Split-phase controls and a five-coordinate construction interface

### 3. An entire split-conductor affine example with unbounded phase order

Choose nonzero distinct `alpha,beta` in an algebraically closed
characteristic-zero field. Set `lambda=alpha+beta`, `mu=alpha beta`,

    B=k[u,v],
    y=v^2-lambda u v,
    h=y+mu u^2=(v-alpha u)(v-beta u),
    z=v h,
    A=k[u,y,z] subset B.

Put `R0=k[u,y]`. The equation `v^2-lambda u v-y=0` makes `B`
finite free of rank two over `R0`, and

    B=R0 direct_sum R0 v,
    A=R0 direct_sum h R0 v.

The latter is closed under multiplication because
`(hv)^2=yh^2+lambda u h(hv)`. Away from `h=0`, `v=z/h`, so the
extension `A subset B` is finite birational; normal `B` is its
normalization. The actual integral affine carrier is the hypersurface

    z^2-lambda u h z-y h^2=0,    h=y+mu u^2.                 (2)

Its conductor is exactly `hB`. To see this, an element `a+bv` belongs
to `A` exactly when `b in hR0`; requiring its product with `v` to
belong to `A` then forces `a+b lambda u in hR0`, hence `a in hR0`.
Thus the entire conductor square is

    A/hB=k[u],
    B/hB=k[u,v]/((v-alpha u)(v-beta u)),

with downstairs ideal `(h,z)` and upstairs divisor the two actual
lines `v=alpha u` and `v=beta u`. The upstairs curve is reducible,
with the two lines meeting at `(0,0)`; no nilpotent or intersection
data is dropped. Their maps to the downstairs line agree in the
coordinate `u`.

Let `C` downstairs be `y=z=0`. Its full reduced inverse image is
exactly the smooth line `c:v=0`, mapped isomorphically by `u`.
Indeed if `v!=0`, the first equation forces `v=lambda u`, and the
second then forces `mu u^2=0`, contradicting `mu!=0` and `v!=0`.
At `u=0` the only inverse point is still `v=0`; no isolated extra
normalization point appears.

For any fixed positive integer `q`, put `Q=v^q`. Modulo the entire
conductor its two restrictions are

    alpha^q u^q,   beta^q u^q.

Therefore the exact full-ring criterion is

    Q^n in A iff alpha^(q n)=beta^(q n).                      (3)

For sufficiency, if the two constants agree, the conductor residue
is the diagonal polynomial `alpha^(qn)u^(qn)` in `k[u]`; subtracting
it leaves an element of `hB subset A`. Necessity is immediate from
the two generic restrictions. Thus (3) includes the intersection
point and the entire conductor, not just a generic unit test.

Choose `alpha/beta` to be a root of unity of order `N`, with
`gcd(N,q)=1`. Then the smallest descending positive power is exactly
`n=N`, which is unbounded while the formulas (2) have fixed degrees
and the smooth singleton lift is unchanged. The primitive-like
orders `q=2` or four therefore do not bound split phases locally.

This is an affine example with a line support. It is **not** a
projective fixed-C0 carrier or a counterexample to any accepted
projective theorem. It proves that a proposed global argument must
use global projectivity, polarization or the actual fixed-C0
projection geometry in addition to these local support conditions.

### 4. Five-coordinate viewpoint: a concrete global lead

Adjoin `Q` to the four projection sections. Since the original four
generate `H`, the five also do, and their map has a finite image

    Y subset P4,  coordinates [U0:U1:U2:U3:Q].

Projection from the fifth-coordinate point is finite birational
`Y->X`. The hyperplane `Q=0` has scheme pullback `2c` or `4c`, and
the reduced curve there is the prescribed fixed C0.

For any scalar `zeta`, let `T_zeta` scale just the fifth coordinate.
At a split conductor identification where the `U_i` agree and the
two `Q` values have ratio `zeta`, the corresponding branch curves
are contained in `Y intersect T_zeta(Y)`. A mate requires these
phase ratios to be constant roots of unity and requires full
Artinian conductor membership as well.

This is a geometric reformulation, **not a proved exclusion**.
The shared hyperplane curve occurs for every `zeta`, so a naive
intersection-degree count must first separate that forced common
component from the additional branch curve. The local example above
shows why neither low coordinate degree nor isolated ramification
alone makes all `zeta` have bounded order. A useful new theorem
would have to couple the extra common curves to the actual
hyperplane multiplicity, global canonical/conductor divisor, or
prescribed C0 parametrization.

The separately written [transverse differential/socle theorem](../supplements/NORMAL_INDEX_SOCLE_AND_TORSION.md#2026-10-14-generalization-transverse-differential-socle-bound)
already supplies one global coupling: on a generically regular
carrier, every surviving projection requires a nonzero common-zero
divisor of the transverse differential, with bounded degree five
or six and a quantitative conductor-contact budget. Classifying
those root strata while preserving the split phase model is the
next structural target. No mate-power search has been started.

<a id="2026-10-14-generalization-projection-finite-phase-space"></a>

## Finite phase covers and their remaining arithmetic

For a finite-type family of actual admissible projections, the corrected
[family theorem](../supplements/PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md#actual-families-and-their-finite-phase-image)
constructs a finite surjective phase cover Z->T0 and a map Z->G_m^D.
T0 imposes full nilpotent logarithmic equations and constancy of all geometric
pair ratios. Ordered roots of the characteristic polynomial of multiplication
by rho in E tensor_K E give the phase coordinates, including conjugate and
split comparisons; repeated roots are permitted. Eventual descent holds exactly
when the resulting tuple is torsion. The corrected proof uses monic finiteness
of the entire conductor quotient before rational localization, so specialized
conductor curves are not lost. Common ideals need not be the largest conductor.

The finite-algebra criterion is u=v exp(w), with u^n in A exactly when
w is in nil(A) and rho^n=1. Characteristic zero is essential to remove the
factor n from the logarithmic membership test. The theorem's full algebraic
proof is owned by [unit descent](../supplements/CONDUCTOR_DESCENT_ALGEBRA.md); the family
construction and its specialization proof are owned by the linked family
theorem. No finite normalization module alone bounds split phase orders.

The mate locus
need not itself be constructible: even the finite algebra family
`A=F` diagonally in `B=F times F`, `u=(1,t)`, over `t in G_m`, has eventual
descent exactly for `t in mu_infinity(k)`. In characteristic zero this is
infinite and has infinite complement, whereas constructible subsets of
`G_m` are finite or cofinite.

There is a useful exact one-phase dichotomy. Suppose, after a finite
refinement, the phase image lies in a fixed torsion translate of a
one-dimensional subtorus, parameterized as

    z_i=xi_i lambda^(m_i), xi_i fixed roots of unity,
    m_i integers, gcd(m_1,...,m_d)=1.                      (11)

The admissible `lambda` image is constructible in `G_m`. If it is finite,
only finitely many phase tuples can occur. If it is infinite, it is
cofinite. It consequently contains roots of unity of arbitrarily large
orders; every such value is realized by an admissible parameter and gives
a mate. Phase orders are unbounded: if `M` kills all `xi_i` and the phase
tuple has order `e`, Bezout on the `m_i` gives `lambda^(M e)=1`, hence
`e >= order(lambda)/M`.

The hypothesis (11) must be proved for the actual phase image. It cannot
be replaced by positive dimension. The curve

    {(lambda,2 lambda): lambda in G_m} subset G_m^2

is positive dimensional and contains no torsion point in characteristic
zero. Thus a multiphase image retains a substantive torsion-intersection
problem even after every contact and logarithmic condition has been made
algebraic.

For the fixed-C0 projective families this yields a concrete structural
target: construct the finite phase image after imposing the entire
nilpotent equations, and determine its torus relations. A surviving
one-phase torsion translate with infinite image would prove existence,
whereas a phase image with no torsion point would exclude the full family
at every mate degree. Neither alternative has yet been established.

## Characteristic boundary

The equalizer, entire contact-divisor formula and finite-module geometry need
no characteristic-zero logarithm; residual-field arguments require separable
extensions. Characteristic zero supplies separability here, the derivative
constancy test, finite logarithms with invertible integer coefficients, and the
single-field Kummer order theorem. Frobenius can kill a nilpotent obstruction in
positive characteristic, so the exponent-free logarithmic criterion is not
imported there. The first-jet formulas use 2 invertible; the three normalization
models and low-degree pruning are inherited characteristic-zero hypotheses.
For the fixed quartic, the [every-positive-characteristic quartic-carrier
construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
remains the separate existence control. No uniform positive-characteristic
extension of these phase bounds is asserted.
