# Normalization, conductor descent, and projection geometry

For the fixed embedded characteristic-zero quartic, a proposed normalization model, an actual projection, and a descending hypersurface section are three different objects. This account separates their tests and the related quintic and conditional sextic applications. [result records](../results/INDEX.md) determine theorem scope; the detailed proof homes below retain conditional mathematics with its stated proof and review scopes.

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

The [explicit projection proofs](../supplements/PROJECTION_SUPPORT_AND_DIFFERENTIAL_OBSTRUCTIONS.md) expose different failures. The plane map [s⁴:s³t:st³+z⁴:t⁴+s³z] is an actual finite degree-sixteen normalization with full inverse support z=0, but every positive mate degree is excluded by a polynomial derivative identity. The general two-fixed-coordinate sublane has the same obstruction. Its generic conductor residue is already trivial, while a nonzero first nilpotent jet survives every power. By contrast, the two actual smooth-quadric families have isolated inverse points, so fail before unit descent. The corrected quadric audit retains seven forced endpoint extras in the kappa family and the exact four-or-five extra points in the companion family. Neither argument exhausts the complete projection space.

The [twisted-cubic corrected-square benchmark](../supplements/TORSION_CONSTRUCTIONS_AND_PINCHING_LIMITS.md) shows that characteristic-zero singular-carrier torsion can produce an actual homogeneous pair for a different curve. The abstract nodal pinching counterexample shows why local phase torsion alone can destroy the marked full-support requirement. These constructive and negative controls explain the missing geometry rather than presuming nonexistence for the quartic.

## Projection phases, effective scope, and geometric scaling

[R-0004](../results/projection_phase_reduction.md) works in a specified finite-type family of admissible Cartier-singleton projections. After stratification and a finite cover, full conductor descent is a torus torsion-phase test. Its proof keeps nilpotent equations, generic conductor components and excluded specialization boundaries. The actual phase images of the three quartic models remain uncomputed. Their on-C thresholds are 5,5,13; with phase order E, every positive multiple of E at least the relevant threshold is a mate degree, with any additional degrees confined to smaller multiples.

The [torsion and rational-phase proofs](../supplements/PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md) distinguish a finite torsion-coset envelope from a constructible mate locus. For an explicitly presented rational constructible phase image W=⋃(Y_i−B_i), the effective method partitions supports into vanishing blocks, applies Mann's ratio bound P\(S\)=∏_{prime≤S}prime, and solves binomial systems by Smith normal form. With maximal translated support degree d and support size S in dimension D, isolated torsion orders are at most P\(S\)d^D; this is a bound, not a divisibility assertion. A common annihilating exponent may use P\(S\)lcm(1,...,d^D). Each coset must still be tested against the removed boundaries B_i. Positive-dimensional retained torsion cosets have unbounded orders. The [raw-input corollary](../supplements/EFFECTIVE_PROJECTION_PHASE_DECISION.md) first constructs actual admissible conductor/phase data; its termination theorem is not an executed fixed-model calculation.


## Five-coordinate geometry of the phase

For an admissible fixed-\(C_0\) Cartier-singleton projection \(S\to X\subset\mathbf P^3\), adjoining the primitive section \(Q\) to the four projection sections gives a finite image \(Y\subset\mathbf P^4\), with coordinates \([U_0:U_1:U_2:U_3:Q]\). Projection from the last-coordinate point is finite birational onto \(X\). The hyperplane \(Q=0\) pulls back to \(2c\) or \(4c\) in the three normalized models and has reduced support \(C_0\).

For \(\zeta\in k^\times\), let \(T_\zeta\) scale only the fifth coordinate. If two conductor branches have identical \(U_i\) coordinates and primitive-section ratio \(\zeta\), their images lie in \(Y\cap T_\zeta\(Y\)\). A descending mate power requires the relevant constant ratios to be roots of unity **and** requires full nilpotent conductor descent. This is a geometric reformulation of the phase obstruction, not an exclusion. The hyperplane curve \(Q=0\) is common to these intersections for every \(\zeta\); a naive intersection-degree argument must first remove this forced component before counting additional branch curves. The fixed-degree affine split-conductor example below shows why phase orders cannot be bounded from finite presentation or smooth singleton inverse support alone. Any useful global bound must invoke the actual projective polarization, contact divisor, or differential/conductor budget. [Original five-coordinate formulation](../supplements/PROJECTION_CONDUCTOR_CONTACT_AND_PHASE.md#2026-10-14-generalization-projection-ray-and-split-phase-model).


## Actual projection coefficient spaces

For the three primitive Cartier singleton models (smooth quadric, quadric cone, plane), the restriction kernels of the full section spaces to the fixed quartic have dimensions 4, 4, 10. Choosing lifts of the four fixed coordinate sections is an affine graph space of dimensions **16, 16, 40**, respectively, before equivalences. Basepoint freeness gives finiteness by ampleness, but birationality and **full inverse support** are additional conditions. For the graded section ring (B=\bigoplus_{b\ge0}H^0(S,bH)) and the four-section subring \(R\), the primitive ray section \(Q\) has a degree-\(b\) mate precisely when \(Q^b\in R_b\), with the prescribed normalization/support hypotheses. Source: [current proof](../supplements/PROJECTION_CONDUCTOR_CONTACT_AND_PHASE.md#2026-10-14-generalization-projection-ray-and-split-phase-model).


## Fixed-degree affine control with unbounded phase

Let \(B=k[u,v]\), \(\lambda=\alpha+\beta\), \(\mu=\alpha\beta\), \(y=v^2-\lambda uv\), (h=y+\mu u^2=\(v-\alpha u\)\(v-\beta u\)), \(z=vh\), and \(A=k[u,y,z]=k[u,y]\oplus h k[u,y]v\). The carrier relation is \(z^2-\lambda uhz-yh^2=0\); the **entire conductor** is (hB). The quotients are \(A/hB=k[u]\) and (B/hB=k[u,v]/(\(v-\alpha u\)\(v-\beta u\))). For \(Q=v^q\), \(Q^n\in A\) exactly when \(\alpha^{qn}=\beta^{qn}\). Choosing \(\alpha/\beta\) of order \(N\) coprime to \(q\) forces least descent exponent \(N\). The inverse support of the indicated affine downstairs line is the smooth line \(v=0\). This disproves any algebra-only universal bound on phase order, **not** a projective fixed-\(C_0\) bound. Same source.


## Opposite-ruling pairing and the sparse-family boundary

On the smooth quadric with diagonal \(c\), the specified pairing ((x,0)\leftrightarrow(0,ax)), \(a\ne0,-1\), forces phase (a^{-2}) and permits the **full form within this pairing**
\[
U(x,y)=W_0+\frac{ax+y}{a+1}W_1+
(a^2x^2+y^2-(a^2+1)xy)D+
xy\bigl(xE+y(W_2-E)\bigr)+x^2y^2W_3,
\]
where \(D,E\in k^4\) are arbitrary. The sparse choice \(D=W_2,E=uW_2\) is finite but has extra inverse points mapping to ([0:0:0:1]): (\(\infty,-a^2/u\)) when \(u\ne0\), and ((-1/(1-u),\infty)) when \(u\ne1\). The boundary coefficient pairs of the full form are (a^2D+yE+y^2W_3) and (D+x(W_2-E)+x^2W_3), which can avoid these particular sparse-family defects. Thus only the **sparse family** is excluded. Sources: [current proof](../supplements/PROJECTION_SUPPORT_AND_DIFFERENTIAL_OBSTRUCTIONS.md#the-opposite-ruling-pairing-and-its-complete-coefficient-freedom), [current proof](../supplements/CYCLIC_COVER_AND_MOVING_LINEAR_RIGIDITY.md#2026-10-14-quadric-opposite-ruling-phase-family-failure).


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

Source: [current proof](../supplements/OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-ramification-scheme-counterexamplemd), with its exact symbolic verifier. These local distinctions should be preserved in future conductor/ramification arguments.


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
Under the complete-intersection, finite-birational projection hypotheses, the **entire downstairs conductor scheme** is the plane conic (\Gamma=V(L,R)), not its reduction. It may be smooth, reducible, or a double line. The algebra audit accepts this exact calculation conditionally on the geometric setup; it does not independently establish every claimed anticanonical embedding or fixed-\(C_0\) spanning application. Sources: `research/notes/2026-10-09-session-genus-one-entire-conductor.md` and [current proof](../supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-entire-conductor-algebra-independent-auditmd).

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

The companion genus-one weak del Pezzo reduction and D5 root-saturation filter concern which actual normalizations and primitive sections can occur. They are **separate geometric hypotheses**, not consequences of the quadratic-algebra criterion. The explicit four-A1 projections are negative full-inverse-support examples, not an exhaustion of the lattice stratum. See [current proof](../supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd), [current proof](../supplements/OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-torsion-filtermd), and [current proof](../supplements/OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-singular-delpezzo-four-a1-familymd).



## Quintic geometry before the final support incidence

The [quintic structural proof](../supplements/QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md) first isolates its hypotheses: in the specified nonnormal Gorenstein genus-one lane, the normal degree-five anticanonical model has one A4 singularity, a smooth lifted quartic c and a unique line ell with `H=c+ell=5ell` and `5c=4H`. This is not a classification of all quintic carriers. The [intrinsic pair proof](../supplements/DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md) contracts the marked A4 chain to the full plane cluster `(y−x³,x⁴)`, classifies every admissible smooth conic through it, and computes the residual automorphism group as translations. Its proof explains why the extra nonendpoint projection parameter cannot be discarded by scaling.

| Actual projection stratum | Retained mechanism and precise remaining boundary |
| --- | --- |
| Endpoint a=0 | [Support and excess proof](../supplements/QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md) plus [the actual fourth-blowup unit jet](../supplements/QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md) exclude every positive mate power in this stratum. The unit jet is an actual-ring obstruction, not only equalizer matching. |
| Endpoint a≠0 | The residual anticanonical divisor gives target contact11, intrinsic contact4 and excess7. The completed [global inverse-support proof](../supplements/QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md#2-endpoint-a-nonzero-global-independent-audit) then excludes every such endpoint projection: its actual target septic must be supported at common roots of U,V; each has order≤4, order4 allows no second root, and the three-root family is separately excluded. A degree7 septic cannot have the resulting support. |
| Nonendpoint reducible residual | The [exhaustive pole filtration](../supplements/NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md) preserves cancellation and repeated-prime strata. The specified partitions 2+2+2, 2+4 and 3+3 are excluded through [actual higher contacts](../supplements/NONENDPOINT_CUBIC_CONTACT_AND_FAMILIES.md) and [complete cubic-pair scope](../supplements/NONENDPOINT_CUBIC_PAIR_COMPLETION.md), not a generic-root count. |
| Nonendpoint integral residual | The actual source has arithmetic genus one, including singular affine cubics, and is smooth at its A4 point. Full inverse support excludes a degree-two map, so its image is birational of class (4,2), arithmetic genus three. Its intrinsic c-ideal has length6, including length2 at A4; target contact14 forces excess8. The curve-model quotient length2 cancels in the local contact comparison and gives no upper bound on that excess. This incidence remains open. |
| Nonendpoint target fibers | The [actual fiber equations](../supplements/NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md) keep finite denominator/rank boundaries, A4 target, infinity and primitive cube-root compatibility. Their equal-lift exclusion does not exhaust every projection. The [single-root incidence](../supplements/NONENDPOINT_SINGLE_ROOT_INCIDENCE.md) preserves separate quotient fibers and singular denominator charts. |

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
valid also on the repeated-root boundary. With the allowed \(A_4\) point \(s=0\), retain the homogeneous system \(D_{sH_2}Q_6=L_1Q_6,\ jD_{H_2}Q_6=\mu Q_6\), \(j=\bar J\), rather than discarding \(j=0\). For \(j\ne0\) the support condition is equivalently the covariant identity \(J(\operatorname{Hess}\(F_{\rm cond}\),Q_6)=0\). These are necessary incidence reductions, **not an \(h=2\) exclusion or conductor-power descent**. The original source flags its later quadratic-algebra norm computation as pending independent review. [Differential proof and incidence](../supplements/QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-h2-conductor-quotient).


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
Then \((d-5)P_6\(\eta\)+(6-d)P_5\(\eta\)\) belongs to the same ODE ideal. The proof uses the two complementary idempotents \(d-5\) and \(6-d\) and Cayley–Hamilton on the sixth and fifth symmetric powers, without radicalizing, inverting a discriminant, or choosing roots. This is a computational compression, **not a unit-ideal certificate**. The subsequent whole-\(h=2\) global saturation prospect stopped at its memory guard and supplied no mathematical emptiness result; that resource-limit history is not part of the theorem. [Twelve generators](../supplements/QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-twelve-generator-independent-audit), [ODE equivalence](../supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-automatic-open-ode-independent-audit), [spectral identity](../supplements/QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md#2026-10-15-generalization-quintic-h2-eta-spectral-independent-audit).


The **global** monic necessary incidence has seventeen equations in nine variables on the original-parameter open `delta E Delta1!=0`. It retains the inverse-map boundary `Delta K=0`. Saturating by `Delta K` treats only a smaller chart and cannot settle the global incidence. The [global monic proof](../supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence) states this boundary exactly. The [degree-five j=0 reduction](../supplements/QUINTIC_H2_INCIDENCE_AND_LOCALCOH_FRONTIER.md) remains unresolved: both proposed exclusions mistake a fixed simple A4 zero at source infinity for one at source zero, so they do not justify their pure-power specialization. The later verifier additionally divides the unreversed determinant polynomial instead of the actual source conductor. Replaying its resultants cannot repair this reduction gap. The degree-six j!=0 branch and full conductor-power descent remain open. Neither the ODE reduction nor the spectral accelerator resolves them.

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

For the homogeneous \(h=2\) factorization \(F_{\rm src}=H_2Q_6\), the first-symbol factor \(H_2\) cannot contain the \(A_4\) point on a surviving candidate. If \(\operatorname{Res}(H_2,Q_6)\ne0\) when \(j=0\), all sextic roots would have to lie at the \(A_4\) point, forcing conductor contact six and contradicting the bound. Therefore **every remaining \(h=2\) mate candidate**, for either value of \(j\), satisfies \(\operatorname{Res}(H_2,Q_6)=0\). This is a necessary homogeneous norm equation, not an emptiness proof; the repeated-root and infinity charts remain included. [Intrinsic coefficient and support proof](../supplements/QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-14-generalization-quintic-intrinsic-a4-contact-bound).


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
Writing \(B=\sum m_iD_i\), ampleness of \(c\) gives \(\sum m_i\(D_i\cdot c\)=N\), bounding prime conductor components, multiplicities and total branch contact. For each downstairs conductor curve, let \(d_\Delta\le a\) be the total generic reduced normalization degree. The **ordered off-diagonal pair correspondence**, including conjugate pairs on one prime, has total weighted first-projection contact bounded by \((a-1)N\). The three fixed-\(C_0\) singleton models give \((a,N,(a-1)N)=(8,20,140)\) for both quadric normalizations and \((16,51,765)\) for the plane normalization. These are finite integer-contact budgets, **not** bounds on scalar phase orders or nilpotent logarithmic defects. The global conductor need not be Cartier, only Cartier near \(c\); singular or non-Cartier lifts and generically nonregular carriers are outside the stated bridge. An independent review **passed under the stated Gorenstein, smooth Cartier-lift, full-support and generic-regularity hypotheses**; applications to a globally non-Gorenstein normalization require retaining the original local-versus-global distinction. [Independent review](../supplements/PROJECTION_CONDUCTOR_CONTACT_AND_PHASE.md#2026-10-14-generalization-projection-conductor-budget-independent-review). [Jacobian identity](../supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md#local-residue-identity-and-global-contact), [contact and pair budgets](../supplements/PROJECTION_CONDUCTOR_CONTACT_AND_PHASE.md#2026-10-14-generalization-projection-conductor-contact-budget).


## Minimum actual carriers and Cartier-index compression

The [canonical compression proof](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md#canonical-compression-on-a-minimum-actual-carrier) chooses a carrier of minimum degree **among carriers that occur in an actual defining pair**. In characteristic zero, for a generically regular carrier and local Cartier exponent e, Picard torsion-freeness compresses its mate to eC~nH. For the fixed quartic, n=4e/a≥a and e≥a²/4; a genuinely minimum sextic carrier would require 3|e and e≥9. Choosing instead a minimum-degree surface merely containing C would invalidate the argument: the smooth quadric contains C but is not a possible sole-support carrier in characteristic zero.

This mechanism can be used constructively as a lower-complexity target or obstructively as a local-index constraint. The proof uses no genus calculation; its degree-d formulation is in the same mathematical home. Generic singularity along C and characteristic-p Picard behavior remain separate boundaries.

## Normal indices and the exact socle bridge

[R-0034](../results/normal_carrier_index_socle.md) uses actual local Cartier index r, not surface multiplicity. For an actual mate multiplicity n=kr, the pointwise socle relation is D_n=(k−1)A_F+kD_r, with ordinary normal-layer torsion satisfying 2Σlength\(T_i\)=nD_n. [R-0035](../results/normal_carrier_bounded_index_exclusion.md) uses its inherited normal-carrier and quadratic-direction hypotheses to exclude the regime where all actual on-curve indices are at most four; it does not treat arbitrary higher indices or nonnormal carriers.

[R-0036](../results/pointwise_conductor_socle_defect.md), for an already existing supported pair with its smooth singleton Cartier lift and invertible conductor, gives D_n=(n−1)A−B|c as an equality of actual divisors. It implies coefficientwise inequalities, not just a degree bound. It is not a substitute for full conductor-unit membership, and it has no established branchwise extension by summing over multiple inverse curves. See [the exact interface](carrier_conductor_socle_interfaces.md).

A separate [normal-carrier divisor reformulation](../supplements/NORMAL_CARRIER_DIVISOR_GEOMETRY.md) preserves the source's proposed equivalence between a Q-Cartier Hodge equality and an actual positive divisor relation, together with its suggested local-socle certificate. That source strengthening remains explicitly pending independent mathematical audit; relocating its full proof does not replace the stated inputs of R-0034/R-0035.

## Conditional sextic applications and the remaining implication

The [conditional sextic treatment](normalization_conductor_phase2_addendum.md) retains the actual rank-22 global source, all q³ lift freedom, constant-rank cubic correction map, the quadric-cycle norm proof including collision and branch multiplicities, free-orbit unit certificate, remaining two-node conic and zero-defect pencils, degree-52 exceptional locus, and the singular-trisecant/nonnormal alternative. [Endpoint-four actual sextics](../supplements/ENDPOINT_FOUR_ACTUAL_SEXTICS.md) provide complete second-symbol lifts and a single-carrier necessary jet exclusion, not a construction or exhaustion of the family.

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
