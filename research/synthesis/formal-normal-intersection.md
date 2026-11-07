# Formal normal geometry and residual intersections: research interface

**Status:** exploratory synthesis, not a theorem or a change to authority. This note supplements [Chapter 2](02-two-surfaces.md), [Chapter 3](03-infinitesimal-geometry.md), and the [dependency map](DEPENDENCIES.md). For precise claims use [results](../results/INDEX.md) and [authority rules](../AUTHORITY.md).

## 1. Setup and objects (see the primary treatments)

For the fixed characteristic-zero rational quartic, begin with a proper intersection containing C, **without** requiring sole reduced support. The cycle identity, the distinction between generic length and the STCI specialization, and the warning against interpreting vertical exceptional curves as residual components are developed in [Chapter 2](02-two-surfaces.md) and [Residual intersections and jets](residual_intersections_and_jets.md).

The normal cone, the full I-initial ideal (including cancellation-generated equations), and the strict-transform intersection on the blowup are **three different constructions**. Their precise definitions and the limitations on comparing them are in [Chapter 2](02-two-surfaces.md), [Chapter 3](03-infinitesimal-geometry.md), and [Normal-filtration defects](normal_filtration_boundary_obstructions.md). No identification between these objects is assumed here.

This note's distinct purpose is to develop the **valuation and specialization research interface**, whose open questions are stated below.

The global numerical filter is independent of the formal initial ideal: if the pair is proper with sole reduced support \(C\), then \(4/\gcd(4,d)\mid e\) by Bézout. If residual degree is nonzero, this divisibility need not hold. Neither the formal local length nor the valuation polygon by itself proves the residual degree is zero.

## 2. Generic formal algebra and specialization

At \(\eta=\eta_{C_0}\), the completed transverse regular local ring is (noncanonically) \(K[[u,v]]\), \(K=k(C_0)\simeq k(t)\). The ideal \(J_\eta\) is \((f,g)\), and, since the surfaces have no common component, its colength is \(m\). If \(r=\operatorname{ord}_\eta(f)\), \(s=\operatorname{ord}_\eta(g)\), then \(m\ge rs\), with equality precisely when their initial binary forms are coprime over \(\overline K\); see [Chapter 2](02-two-surfaces.md). Common first factors encode generic normal directions, not global factors of \(F,G\).

Working over \(\overline K\) separates geometric generic directions. Choosing a point \(p\in C_0\) and completing \(K\) at its discrete valuation gives \(k((t_p))\) after choosing a local parameter (with residue field \(k\)); this is **not** the algebraic closure of \(K\). In characteristic zero, Puiseux extensions describe an algebraic closure of \(k((t_p))\). These valued extensions can organize branching and specialization of generic directions, but a valuation at \(p\) does not by itself prove the existence of a residual global curve.

The global sheaf of normal jets, its saturation defects, and the behavior over special points retain information absent from \(K[[u,v]]\). The full root scheme of a saturated first relation, including repeated and nonreduced fibers, is essential; see [Chapter 3](03-infinitesimal-geometry.md).

## 3. Exceptional directions, cancellation, and valuations

The common zero scheme of the two leading normal forms on \(E\) can have components dominating \(C_0\) (not necessarily sections), special-fiber components, and embedded or nonreduced features. Successive blowups can separate some persistent contacts, but no general finite-step classification or implication \(\text{vertical exceptional component}\Rightarrow R\ne0\) is asserted.

The appropriate structural question is how the **full filtered ideal**, rather than a chosen pair of initial forms, controls the transforms and their exceptional intersection. Cancellation is a geometric source of higher initial relations; it should be understood through initial ideals, Rees constructions, and valuations, **not** treated as an invitation to enumerate polynomial examples. Weighted initial ideals and tropical/Gröbner methods may help organize valuations and changes of normal direction. Tropicalizations of the individual generators need not determine the initial ideal or tropicalization of \(J\); generator-independent statements require the whole ideal. Seek intrinsic invariants and global constraints first; use examples only to distinguish precise competing assertions.

The valuation tree of persistent horizontal directions and their specializations is a **possible organizing picture**, not an established classification or a canonical tree. It requires a precise choice of valuations and a proof that any proposed invariant is independent of coordinates, generators, and blowup sequence.

## 3A. Initial equations, punctual defects, and integral boundary data

Three distinct operations must be kept separate. Taking the leading normal forms of F and G can miss generators of the full initial ideal H. Passing from the minimal generators of H to the associated graded of the actual equation module J/IJ can then lose further information. Finally, passing to the generic point removes punctual torsion in these sheaves. The canonical exact comparison and its local counterexample are integrated in [Normal-filtration defects](normal_filtration_boundary_obstructions.md#from-exceptional-normal-divisors-to-the-full-filtered-equation-module), with the scoped result [R-0030](../results/local_filtration_comparison_defect.md).

The support of the comparison defect lies where both carriers are singular along C. That necessary condition does not prove a punctual defect exists for an intersection with sole reduced support C. Nor does cancellation imply such a defect: the characteristic-two quartic has a higher initial equation but vanishing comparison defect [R-0031](../results/quartic_char2_fourth_equation_kernel.md).

Weighted valuations require the integral coefficient lattice at each point, not only the generic algebra. In the family (x²,y²+t^r x), the integral weighted initial ideals distinguish the boundary exponent r; after inverting t, the generic length remains four. The Smith-form determinant index of a normal-degree relation matrix records torsion missed by entry valuations alone. The calculation and frame-change limitations are in [Weighted initials and normal boundary](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md#weighted-initials-normal-boundary). These invariants can constrain special-point behavior but do not alone imply a global residual curve.

## 4. How the comparison lemmas fit together

For the scoped root, graded-relation and actual-CI bridge theorems R-0005–R-0009, use [Chapter 3](03-infinitesimal-geometry.md). For local initial-ideal comparison and saturation, use [Normal-filtration defects](normal_filtration_boundary_obstructions.md). For proper residual cycles, examples and global jet obstructions, use [Residual intersections and jets](residual_intersections_and_jets.md). For fixed-carrier normalization and conductor descent, use [Chapter 4](04-carriers.md) and [Carrier/socle interfaces](carrier_conductor_socle_interfaces.md). The quartic-carrier exclusion [R-0001](../results/quartic_carrier_exclusion.md) remains closed.

**None of these references proves the valuation-theoretic classification proposed below.** In particular, moving from generic formal data to an actual supported pair requires hypotheses not provided by the valuation picture.

## 5. Focused theorem-level questions (all open)

1. **Generic-to-global interface.** What hypotheses on the full initial ideal and its saturation make a horizontal common-direction scheme extend to a controlled global root relation, including special-point defects? Can those defects be related to global normal-jet restrictions?
2. **Residual detection.** Can a generator-independent invariant of successive transforms or the normal filtration distinguish a pure \(C_0\)-supported intersection from one with \(R\ne0\)? Prove a direction of implication before attempting numerical bounds; exceptional vertical curves alone do not suffice.
3. **Valuation-theoretic structure.** Is there a finite intrinsic invariant of persistent generic normal directions, their specialization, and higher cancellation that constrains \(m\), \(R\), or the realizability of \(J\) by global homogeneous equations?
4. **Connection to established obstructions.** Can one verify the precise extra hypotheses that transfer the graded/root-scheme criteria or carrier-conductor restrictions to an actual pair in a nontrivial family of degrees \(d,e\ge5\)?

A productive next round should choose one or two of these interfaces **only after** assessing leverage against the current [frontier](../FRONTIER.md). Generalize beyond \(C_0\) only when doing so is cheap or clarifies a proof. Prefer a structural lemma, counterexample to a proposed implication, or a sharply isolated missing implication over computational casework. This note imposes no mandatory method or priority order.

## 6. Entirely-thick source-preserved cluster and ideal-power facts

The [generic cluster analysis](../supplements/OCT7_SATURATION_REES_AND_CARRIER_CLASSIFICATION.md#2026-10-07-entirely-thick-rees-valuation-framework) identifies the higher-contact budget for a supported pair of degrees a,b and generic normal orders p,q. At the generic point of C, the two-dimensional regular local ring has complete-intersection length ab/4. Noether's intersection formula expresses the excess ab/4-pq as the sum of the products of multiplicities over common infinitely-near points, weighted by residue degrees. This bounds the number of generic common centers for fixed a,b,p,q, but not uniformly for fixed ratios a/p and b/q. First normal forms alone do not control length: the pairs (y^2+x^N, y^2+2x^N) have constant first forms and length 2N.

The [relative blowup recursion](../supplements/OCT7_SATURATION_REES_AND_CARRIER_CLASSIFICATION.md#2026-10-07-entirely-thick-relative-blowup-budget) says that blowing up a smooth horizontal common center Z with orders r,s subtracts rs[Z] from the pushed-forward intersection cycle of the strict transforms. A later center of covering degree d contributes drs. For the (3,4) boundary, the first exceptional intersection has total coefficient 2pq; **for terminating horizontal trees** this bounds the degree-weighted total common-center budget. It does not imply that the first exceptional bidegree's zero horizontal coordinate prevents later twisting. Persistent formal centers are not thereby shown to algebraize to extra projective common curves.

Finally, the [local thickened-fiber countermodel](../supplements/OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md#source-2026-10-07-thickened-fiber-local-countermodelmd) shows that reduced support of a pair along a repeated ruling component constrains only the zeroth-order restriction of the mate, not its higher transverse coefficients. Consequently the thickened-fiber interpolation cokernel is not, by itself, an STCI obstruction. This is a substantive failed mechanism to retain in the research record.

These are source-preservation statements, not a new independent audit of the proofs.

## 7. Entirely-thick marked roots: distinct-root bound and failure of coefficient coupling

The [Segre ruling audit](../supplements/OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md#source-2026-10-07-thick-segre-root-auditmd) fixes an essential incidence distinction. On the unique quadric, the two projections of C have degrees one and three. A generic trisecant ruling fiber L meets C in **three distinct points**. A root of the residual F factor on the quadric-direction section makes F vanish at all three, but the residual mate factor restricts to a degree-q section on L and may place all its zeros at only one of them. Thus each distinct root guarantees **at least one**, not three, common first-normal points. In the exact sole-support balanced boundary a=3p,b=4q, the actual strict-intersection purity argument in section9 gives a choice-dependent injection into the constant exceptional sections, proving `number of roots <= number of sections <= min(p,q)`. A stronger three-points-per-root count still fails. At ramified fibers use the scheme-theoretic degree-three intersection, not an invented three-distinct-points assertion.

The [marked-jet separation](../supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-marked-point-jetsmd) distinguishes root multiplicity M_T of the residual F factor from divisorial coefficient r_T of the first exceptional divisor along the corresponding section. Locally `A=z+x^M` has restriction order M on z=0 without containing the transverse section x=0. Hence no general inequality `r_T>=M_T`, and no monotone lower bound on the sectionwise Noether contribution follows from the marked root order alone. In particular `sum M_T=2p` cannot be substituted into the separate budget `sum c_T=2pq` without a coupling theorem.

For a trisecant L meeting C in the degree-three divisor P1+P2+P3, the support-only requirement on a nonzero residual mate restriction `R_G|L` of degree q says its zero divisor is supported on those **up to three points**. It therefore has the form `lambda*ell_1^e1*ell_2^e2*ell_3^e3` with nonnegative exponents summing to q, rather than necessarily a pure qth power at a single distinguished point. The single-point pure-power statement in the marked-point note is valid only with the additional assumption that the allowed support is one point. The open global problem is to couple these exponent allocations, their exceptional clusters, and the restrictions of one global `O_Q(3q,q)` section. This retains the counterexample and the actual discrete incidence data without importing an unjustified stronger assertion.

## 8. Exact ruling interpolation, thickened-fiber discrepancy and smoothing

The [ruling interpolation audit](../supplements/OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md#source-2026-10-07-thick-ruling-interpolation-auditmd) proves that for r distinct fibers L_i, restriction `H0(Q,O(3q,q)) -> direct_sum H0(L_i,O(q))` is surjective whenever `r<=3q+1`, by evaluation in the first P1 factor. For each fixed allocation of the degree-q zero divisor among the up to three points of `C intersect L_i`, the allowed nonzero restriction is a one-dimensional subspace of the `(q+1)`-dimensional fiber space. Thus r specified allocations impose **exactly rq linear conditions**; their finite union is still far from empty when `r<=min(p,q)`. A reduced-fiber interpolation count alone cannot exclude the boundary. Multiplicity M_i of a fiber does not add independent conditions on its reduced restriction.

For the [thickened-fiber jet calculation](../supplements/OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md#source-2026-10-07-thickened-fiber-jetsmd), set `Z=sum_i M_i L_i`, `sum M_i=2p`. The exact sequence `0 -> O_Q(3q-2p,q) -> O_Q(3q,q) -> O_Z(3q,q) -> 0` gives `h0(O_Z(3q,q))=2p(q+1)`. The restriction map is surjective for `2p<=3q+1`; for `2p>3q+1` its cokernel has dimension `(2p-3q-1)(q+1)`. This is a **linear interpolation discrepancy**, not an STCI obstruction: reduced common support does not force the higher mate jets to belong to a specified proper incidence locus. The leading `2pq` term agrees numerically with the first exceptional intersection budget, but the two quantities are not identified.

The [repeated-fiber smoothability note](../supplements/OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md#source-2026-10-07-thick-repeated-fiber-smoothabilitymd) supplies another negative result. Along a repeated residual ruling fiber away from C, the local carrier may have form `F=x^M u+z A`, where `z=0` cuts out Q. Even if `M>=2`, the transverse derivative `A|L` may be nonzero. The degree-3p recursion `F=F_cub+Q K` with `K in (I_C^(p-1))_(3p-2)` permits such a smoothing term because I_C is the unit ideal away from C. Thus repeated residual multiplicity does **not** force generic singularity along L. This does not assert existence of a globally smooth supported STCI pair. Any genuine obstruction must couple the transverse smoothing, mate restrictions, and marked divisor `C intersect L`.

<a id="9-exceptional-marked-section-versus-trisecant-base-unresolved-coordinate-bridge"></a>

## 9. Actual strict restrictions and the residual-root count

The [quadric-section divisor calculation](../supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-quadric-section-divisormd) uses `H|E=(4,0)` and `E|E=(7,-1)` to obtain `S_Q=(2H-E)|E=(1,1)`. At the (3,4) boundary, each horizontal exceptional component T_j has class `(0,1)`, hence `T_j.S_Q=1`; if `W=sum c_j T_j` as a cycle, its intersection divisor on S_Q is `sum c_j P_j` of degree `2pq`. The first-normal divisor degrees on S_Q are `6p` and `10q`, not the residual quadric degrees `2p` and `q`. The necessary fixed-factor and coordinate identifications must not be skipped.

**The count bridge on the exact boundary is proved.** The blowup restricted to Q is the blowup of its Cartier divisor C, hence the strict transform Qtilde is Q itself and E|Qtilde=C. Consequently the actual strict divisor restrictions are exactly R_F and R_G, including their local equations and multiplicities. For each residual ruling root ℓ of R_F, R_G|ℓ is a nonzero section of O_ℓ(q); otherwise ℓ would be an extra common curve. Choose a zero P. Sole support forces P∈C, so its lift lies in the actual proper strict-transform intersection W and on S_Q. On a=3p,b=4q, W is pure with effective cycle of class(0,2pq); its support consists of constant sections T_j. Each T_j meets S_Q in one point, and distinct ruling fibers are disjoint, so the chosen points give an injection of distinct ruling roots into distinct T_j. This proves the count bound without a canonical bijection. The [complete supported-cycle and root-count proof](rees_and_vertical_controls.md) retains its exact hypotheses and the additional no-vertical refinement.

The degree-three pullback of a ruling root need not map pointwise to three different sections: only the selected mate zero is used. This resolves the earlier overly broad statement that a count correspondence was missing. It does **not** identify the root multiplicity M_i with the cycle coefficient c_j, compare their local Noether contributions, or supply this bound outside the exact supported balanced boundary.

The [first-blowup coupling audit](../supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-first-blowup-marked-couplingmd) and [root-budget separation](../supplements/OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md#source-2026-10-07-thick-root-budget-separationmd) distinguish generic-along-section intersection coefficient c_T from vanishing order M_T at a marked point on S_Q; semicontinuity of finite-flat fiber length cannot compare them because these are not fibers of one such length function. The [marked-trisecant local pair](../supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-local-pair-marked-trisecantmd) retains the full exponent allocation across `C intersect L` and ambient transverse smoothing, but reduced support still leaves higher local mate coefficients free. An obstruction would need the actual CI cluster, a global divisor/proximity relation, or a justified coordinate bridge between these strata.

## 11. Valuation data with coordinate and integral-model discipline

The weighted-initial investigation starts with K=k(C), a rational normal frame X,Y, a closed point p, and the discrete valuation v_p on K. For polynomial expressions and integer weights (alpha,beta), define

    v_(p,alpha,beta)(sum a_ij X^i Y^j)
      = min {v_p(a_ij)+i*alpha+j*beta : a_ij nonzero}.

In this chosen frame the construction is a Gauss valuation on K(X,Y). Its initial polynomial retains all terms attaining the minimum; its *initial ideal* must be formed from every element of the ideal, not merely from the initials of F and G. The [weighted-initial source](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md#weighted-initials-normal-boundary) studies the resulting Newton and Groebner chambers and records its restrictions on formal series. This is a coordinate-dependent calculation, not yet an intrinsic invariant of the embedded pair.

Two distinctions are essential. First, multiplying a generator by a rational coefficient changes its scalar value, so taking the infimum of v_(p,w) over every nonzero element of a K-ideal is meaningless: powers of a local parameter in the denominator drive that infimum to minus infinity. The integral model over O_(C,p), its saturation, and the associated graded coefficient ring retain the boundary information that would otherwise disappear. Second, the rational frame changes at p; the individual coefficient valuations and Newton polygons can change. The intrinsic leading symbols instead live in symmetric conormal powers, and their divisors require the correct transition functions.

For a research test, retain the chosen frame, integral lattice, full initial ideal, and transformation rule. Only after proving frame invariance may a chamber boundary or valuation defect be called a geometric obstruction. Monomial-containing initials must be included; restricting to the tropical (monomial-free) locus would discard relevant specializations.

## 12. Ordinary ideal powers on a smooth quadric: complete proof

Let Q≅P1×P1 be a split smooth quadric over a field and C an integral Cartier divisor of class (a,b), with 1<=a<=b. Let I be its saturated homogeneous prime ideal in P3. The inherited independently reviewed theorem is stronger than a high-degree saturation bound: for every m>=0 and every integer d,

    H^0(P3,I_C^m(d))=(I^m)_d,   I^m=(I^m)^sat=I^(m).   (P)

For b>=2, one additionally has H^1(P3,I_C^m(d))=0 whenever d>=bm. For the rational quartic (a,b)=(1,3), this gives H1 vanishing from d=3m but ordinary/symbolic equality in every degree. Smoothness of C is not needed for this integral Cartier-divisor theorem. The complete inherited proof and classical monomial overlap are in [the uniform quadric proof](../supplements/FOUNDATIONAL_FRONTIER_AND_INCIDENCE.md#2-uniform-theorem-for-integral-curves-on-a-smooth-quadric). This consolidation recovers that stronger existing scope; it does not claim a new theorem or novelty.

Locally C is cut out by Q and a local Cartier equation h on Q. Consequently the sheaf colon is (I_C^m:Q)=I_C^(m-1), and restriction gives

    0 -> I_C^(m-1)(d-2) --Q--> I_C^m(d)
      -> O_Q(d-ma,d-mb) -> 0.                            (1)

For d>=bm, both right-hand bidegrees are nonnegative. Also d-2>=b(m-1), since b>=2. Starting at m=0, induction and the vanishing of H^1 of those nonnegative quadric line bundles give H^1(I_C^m(d))=0 and surjectivity on H^0 of the last map in (1).

The remaining step is **ordinary homogeneous source completeness**, which does not follow from this sheaf vanishing alone. Choose degree-b equations of C whose restrictions after factoring h form a basis of H^0(Q,O_Q(b-a,0)). Such lifts exist: restriction of ambient degree-b forms to Q is surjective, and multiplying by h identifies that space with H^0(Q,I_(C/Q)(b)). Products of m such equations span H^0(O_Q(m(b-a),0)), because multiplication of binary forms is surjective. Put e=d-bm>=0. Ambient degree-e forms restrict surjectively to H^0(O_Q(e,e)); multiplication gives the full H^0(O_Q(m(b-a)+e,e)), exactly the quotient in (1). Thus (I^m)_d already maps onto that quotient.

When d<bm, the second bidegree of the quotient in (1) is negative, so that quotient has no global sections; take F_0=0. When d>=bm, the multiplication construction provides F_0 in (I^m)_d with the same quotient restriction as any given F. Thus for every degree and any section F of I_C^m(d), choose such an F_0. Then F-F_0=QK for K in H^0(I_C^(m-1)(d-2)). By induction K lies in (I^(m-1))_(d-2), so F lies in (I^m)_d. This proves the sheaf-power and saturation assertion in (P) in every degree: the induction is now on m for all d simultaneously, so no degree inequality is needed for K. The argument uses the split smooth quadric and its line-bundle multiplication, without a monomial parameterization, characteristic zero, or a mate.

For symbolic equality, away from the affine-cone vertex I is a prime regular-sequence ideal: C is Cartier on the smooth Q. There its associated graded algebra is polynomial over the domain quotient, so the powers are I-primary. An embedded prime could therefore occur only at the vertex; saturation excludes it. Thus I^m is I-primary and equals I^(m). The equalities do not imply that S/I^m is Cohen–Macaulay or that I is two-generated. In particular, a dimension-three local Cowsik criterion must not be applied to the dimension-four homogeneous coordinate ring. The ruling-line case outside a,b>0 is separately a complete intersection.

For (a,b)=(1,3), it gives the exact homogeneous colon and quotient

    (I^p:Q)_(3p-2)=(I^(p-1))_(3p-2),
    (I^p)_(3p) ∩ (Q)=Q(I^(p-1))_(3p-2),
    (I^p)_(3p)/Q(I^(p-1))_(3p-2)=H^0(Q,O_Q(2p,0)).       (2)

The three cubic generators of the fixed quartic supply the degree-three lifts above. Every degree-3p carrier of order at least p is therefore F=F_cub+QK, with F_cub a linear combination of products of p cubics and K in (I^(p-1))_(3p-2). This parameterizes the actual source space, without restricting its singularities, normalization, or mates.

The inherited full proof is [the ordinary-power calculation](formal-normal-intersection.md#12-ordinary-ideal-powers-on-a-smooth-quadric-complete-proof). The distinct-root bound has the separate actual-intersection proof in section9; it does not follow from the source-space calculation alone and does not identify root multiplicities with exceptional-cycle coefficients.

## 12A. The difference between source completeness and symbol surjectivity

The ideal-power theorem identifies every actual ambient section of \(I_C^m(d)\) with an ordinary degree-\(d\) product expression for \(d\ge3m\). Its next restriction map
\[
H^0(I_C^m(d))\longrightarrow H^0(C,\operatorname{Sym}^m(I_C/I_C^2)(d))
\]
can nevertheless have a proper image. The source theorem controls its **domain**, not its rank or cokernel. A higher-order jet from the same global equation must also satisfy compatibility with the lower orders; arbitrary choices in distinct graded pieces need not glue.

This explains why a complete degree-\(3m\) recursion is useful for finite experiments but is not a global STCI obstruction. It supplies a finite ambient parameter space; one still needs a uniform transverse-length or conductor argument on the proper-pair locus. The [global-source section](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md) records the exact image-as-kernel formulation using the connecting map to \(H^1(I_C^{m+1}(d))\).

## 13. A single local-to-global test protocol

For an actual proper pair F,G, begin with its generic colength and full I-initial ideal over K, then compute the horizontal exceptional directions. At each special point, record the conormal frame transition and the *integral* weighted-initial lattice, including cancellation-generated relations and any torsion. If a curvilinear saturated flag is available, apply the scoped residual-zero-cycle formulas; otherwise record precisely why the hypotheses fail. Next test whether the candidate local jets lie in the image of the global degree-d and degree-e equation spaces, using the exact power theorem when its degree range applies. Finally compute the projective residual cycle, not just the exceptional support.

A negative computation should identify which step fails and whether the failure is stable across a whole parameter family. This protocol does not assert that passing every finite test yields global equations or that failure of an isolated test excludes all STCI pairs.

## 14. Why marked trisecant and ruling tests did not force a contradiction

The [marked-trisecant local calculation](../supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-local-pair-marked-trisecantmd) is an informative negative result. On Q near a transverse point of a trisecant ruling L meeting C, choose parameters with L=(u) and C=(y). If a carrier restricts as F|Q=y^p*u^M times a unit and the mate as G|Q=y^q*R_G, the reduced-support condition along L only fixes R_G(0,y)=y^e times a unit. It does not fix the u-dependent coefficients of R_G or the coefficient transverse to Q. Even retaining the multiplicity M and all three marked intersections of L with C does not produce the desired local coupling without extra global hypotheses.

This explains why imposing a contact budget on the ruling alone is insufficient: the ambient normal direction remains free. To turn this into an obstruction, one must identify a global divisor relation, a proximity constraint on an actual complete-intersection cluster, or a justified compatibility map between the ruling and ambient transverse data. The negative result is about the insufficiency of a method, not evidence that an STCI exists.

## 15. Intrinsic flags versus scalar valuation lists

The [coefficient-valuation study](coefficient_valuations.md) distinguishes the intrinsic normal blowup and subsequent valuation flags from the noncanonical choice of a coefficient field and transverse coordinates. On the full formal ring K[[U,V]], weights that assign positive order to U,V support normal-first valuations under their stated domain conditions; coefficient-first Gauss expressions for arbitrary real weights require separate convergence/domain control. Their associated initial ideals and residue polynomials carry more information than a collection of scalar values of elements.

The same study gives a warning from the prescribed mu4 family: even knowing scalar values of an ideal for all selected weights does not in general recover transverse length. Cancellation, residue classes, and higher initials matter. Consequently the useful object is a filtered ideal or an initial algebra together with its integral model and frame transitions, not a numerical valuation score.

This is a methodological distinction, not an assertion that a canonical valuation invariant already decides residual support.

## 16. Family-level failure analysis

The entirely-thick investigations have produced both exact positive tools and instructive dead ends. The degree-3p quotient and power-saturation theorem determine global equation spaces in a stable degree range. The marked-trisecant and ruling interpolation tests show that a reduced-support condition does not automatically constrain all transverse coefficients. The weighted-initial framework tracks degeneration but does not, without a comparison theorem, force residual support.

A next experiment should therefore state the invariant class it tests, the specific global source image it uses, and the exact step where the proposed local-to-global implication fails. Do not restart an unbounded search through isolated equations after each failure; ask whether the failure persists for the entire family and what additional hypothesis would make the implication valid.

## 17. Arithmetic support and normal specialization

R-0021 supplies a flat integral pair whose characteristic-zero intersection has four reduced quartic components, while the characteristic-two intersection has sole reduced support C and transverse length four. R-0020 describes the associated change in conormal splitting. These facts demonstrate that flatness preserves neither the number of reduced components nor the form of the normal initial ideal.

R-0012 excludes a lift of precisely this special embedded scheme over Z_(2) or Z_2 only when the generic reduced support must be C. The displayed integral family does not satisfy that extra generic-support requirement. Consequently a valuation or blowup argument using specialization must keep the embedded model, base, full initial ideal, and support condition separate.

## Successive ruled exceptional surfaces: a concrete open comparison

After blowing up a chosen horizontal section or multisection Z_i in an exceptional ruled surface E_i=P(N_i), determine the actual normal bundle of Z_i in the transformed threefold and the splitting/extension class of the next ruled exceptional surface. Even when the first E_i is abstractly P1×P1, a chosen product identification need not be canonical, and later E_(i+1) is not automatically a product. A useful result would give exact hypotheses under which the transition is an elementary transformation of a ruled bundle, together with its effect on degree, marked attachment and common-center multiplicity. This is a concrete open geometry question in any characteristic where the chosen smooth centers and bundle maps exist, not an asserted recursion or an STCI obstruction.

## Coprime first normal forms and the global resultant

<a id="p-006"></a>

The following argument applies more generally. Let \(C\subset\mathbf P^3\)
be a smooth curve of degree \(d\) and genus \(g\). Suppose degree-\(a\) and
degree-\(b\) forms cut it out set-theoretically. At the generic point of
\(C\), let their orders in the normal ideal be \(r,s>0\). Their first normal
forms are binary forms

\[
f_r\in H^0\!\left(C,\operatorname{Sym}^rN_C^*\otimes
\mathcal O_C(a)\right),
\quad
g_s\in H^0\!\left(C,\operatorname{Sym}^sN_C^*\otimes
\mathcal O_C(b)\right).
\]

These are genuinely global sections.  Indeed, because \(C\) is a regular
embedding,
\(\mathcal I_C^j/\mathcal I_C^{j+1}\simeq
\operatorname{Sym}^jN_C^*\) is locally free.  If any lower normal class of
one of the equations vanishes at the generic point, it vanishes globally;
induction puts that equation in the corresponding sheaf power.  At a special
point its order may therefore increase, but it cannot decrease.

Assume for contradiction that \(f_r,g_s\) are relatively prime over
\(k(C)\).  Fix \(p\in C\) and choose completed coordinates

\[
 \widehat{\mathcal O}_{\mathbf P^3,p}=k[[t,u,v]],\qquad
 \mathcal I_{C,p}=(u,v),\qquad \widehat{\mathcal O}_{C,p}=k[[t]].
\]

For the completed local equations \(A_p,B_p\), the hypothesis that the
set-theoretic intersection is \(C\) says
\(\sqrt{(A_p,B_p)}=(u,v)\).  Hence
\(k[[t,u,v]]/(A_p,B_p)\) is finite over \(k[[t]]\).  The two equations have
height two in the regular local ring, so they form a regular sequence; the
quotient is one-dimensional Cohen--Macaulay with the unique minimal prime
\((u,v)\).  Thus \(t\) is a nonzerodivisor.  The quotient is a finite
torsion-free, hence free, module over the DVR \(k[[t]]\), and its transverse
fiber length is constant.

Over \(k((t))\), coprimality of the initial binary forms makes that length
exactly \(rs\).  At the special point, plane intersection multiplicity is at
least the product of the two orders, hence at least \(rs\); equality holds
only when both orders remain \(r,s\) and their initial forms are relatively
prime.  Constancy forces equality at every point.  The resultant is therefore
nowhere zero on \(C\).

That resultant is a nowhere-vanishing section of

\[
(\det N_C^*)^{rs}\otimes\mathcal O_C(a)^s
\otimes\mathcal O_C(b)^r.
\]

Consequently its degree is zero. Bézout and the resultant degree give

\[
ab=drs,
\qquad
d(as+br)=(4d+2g-2)rs.
\]

Writing \(x=a/r\) and \(y=b/s\), one obtains

\[
xy=d,
\qquad
x+y=4+\frac{2g-2}{d}.
\]

The arithmetic--geometric mean inequality now shows that generic relative
primality is impossible whenever

\[
4+\frac{2g-2}{d}<2\sqrt d.
\]

In that range the strict transforms of the two defining surfaces must still
share a curve dominating \(C\) inside \(\mathbf P(N_C)\) after the first
blowup. For a rational quartic the two sides are \(7/2\) and \(4\), so the
obstruction applies. More generally it applies to every smooth rational curve
of degree at least three. The twisted cubic provides a useful sanity check:
its known quadric--cubic presentation indeed has excess tangency and generic
intersection multiplicity two. An elliptic quartic is the boundary equality
case and its transverse \((2,2)\) complete-intersection presentation realizes
\(x=y=2\).

This is a structural restriction, not a disproof: the horizontal common curve
or multisection in the exceptional ruled surface may persist through further
blowups, and positive-characteristic Frobenius constructions show that such
persistence can end in a valid presentation.

## Low-degree surfaces singular along the whole quartic

<a id="p-011"></a>

Let \(C\sim(1,3)\) on its unique smooth quadric \(Q=(q=0)\), and let
\(F\) be a degree-\(a\) hypersurface containing \(C\) and singular at every
point of \(C\). Since \(C\subset\mathbf P^3\) is a regular embedding,
singularity along \(C\) is equivalent to

\[
 F\in H^0(\mathbf P^3,\mathcal I_C^2(a)).
\]

In homogeneous coordinates this is membership in the saturated sheaf square
\((I_C^2)^{\mathrm{sat}}=I_C^{(2)}\), not necessarily in the unsaturated
ordinary ideal square.  Locally on the smooth quadric one may write
\(I_C=(q,h)\).  Reducing an element of \(I_C^{(2)}\) modulo \(q\) gives a
multiple of \(h^2\), so if \(q\nmid F\), the divisor \(F|_Q\) contains the
doubled Cartier divisor \(2C\).

The divisor \(F|_Q\) has class \((a,a)\), while \(2C\) has class \((2,6)\).
Its residual divisor
would have class

\[
 (a-2,a-6),
\]

which is not effective when \(a<6\). Hence every degree-\(<6\) hypersurface
singular along all of \(C\) is divisible by \(q\). Write \(F=qH\). Along
\(C\), the quadric is smooth and

\[
 dF|_C=H|_C\,dq|_C;
\]

therefore \(F\) is singular along \(C\) exactly when \(H\) also contains
\(C\).

This gives the complete low-degree list:

- there is no cubic singular along the entire curve;
- a quartic singular along the entire curve is a scalar multiple of \(q^2\);
- a quintic singular along the entire curve is \(qH_3\), where the cubic
  \(H_3\) contains \(C\).

In fact no \(q\)-divisible hypersurface can be a member of a successful pair.
For every second form \(G\),

\[
 V(q,G)\subseteq V(qH,G).
\]

P-004 says that \(V(q,G)\) strictly contains \(C\), so the extra locus survives
in \(V(qH,G)\).  This excludes the quintics as well as \(q^2\).  Thus a valid
quartic or quintic carrier has normal order one at the generic point of \(C\),
although P-005 forces every carrier to be singular at at least one closed point
of \(C\). In particular, the genuinely thick-carrier escape route cannot begin
below degree six.
