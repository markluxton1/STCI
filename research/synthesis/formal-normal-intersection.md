# Formal normal geometry and residual intersections: provisional research interface

**Status:** exploratory synthesis, not a theorem or a change to canonical authority. This note supplements [Chapter 2](02-two-surfaces.md), [Chapter 3](03-infinitesimal-geometry.md), and the [dependency map](DEPENDENCIES.md). For precise claims use [canonical results](../results/INDEX.md) and [authority rules](../AUTHORITY.md).

## 1. Setup and objects (see the primary treatments)

For the fixed characteristic-zero rational quartic, begin with a proper intersection containing C, **without** requiring sole reduced support. The cycle identity, the distinction between generic length and the STCI specialization, and the warning against interpreting vertical exceptional curves as residual components are developed in [Chapter 2](02-two-surfaces.md) and [Residual intersections and jets](residual_intersections_and_jets.md).

The normal cone, the full I-initial ideal (including cancellation-generated equations), and the strict-transform intersection on the blowup are **three different constructions**. Their precise definitions and the limitations on comparing them are in [Chapter 2](02-two-surfaces.md), [Chapter 3](03-infinitesimal-geometry.md), and [Normal-filtration defects](normal_filtration_boundary_obstructions.md). No identification between these objects is assumed here.

This note's distinct purpose is to develop the **valuation and specialization research interface**, which is still provisional.

## 2. Generic formal algebra and specialization

At \(\eta=\eta_{C_0}\), the completed transverse regular local ring is (noncanonically) \(K[[u,v]]\), \(K=k(C_0)\simeq k(t)\). The ideal \(J_\eta\) is \((f,g)\), and, since the surfaces have no common component, its colength is \(m\). If \(r=\operatorname{ord}_\eta(f)\), \(s=\operatorname{ord}_\eta(g)\), then \(m\ge rs\), with equality precisely when their initial binary forms are coprime over \(\overline K\); see [Chapter 2](02-two-surfaces.md). Common first factors encode generic normal directions, not global factors of \(F,G\).

Working over \(\overline K\) separates geometric generic directions. Choosing a point \(p\in C_0\) and completing \(K\) at its discrete valuation gives \(k((t_p))\) after choosing a local parameter (with residue field \(k\)); this is **not** the algebraic closure of \(K\). In characteristic zero, Puiseux extensions describe an algebraic closure of \(k((t_p))\). These valued extensions can organize branching and specialization of generic directions, but a valuation at \(p\) does not by itself prove the existence of a residual global curve.

The global sheaf of normal jets, its saturation defects, and the behavior over special points retain information absent from \(K[[u,v]]\). The full root scheme of a saturated first relation, including repeated and nonreduced fibers, is essential; see [Chapter 3](03-infinitesimal-geometry.md).

## 3. Exceptional directions, cancellation, and valuations

The common zero scheme of the two leading normal forms on \(E\) can have components dominating \(C_0\) (not necessarily sections), special-fiber components, and embedded or nonreduced features. Successive blowups can separate some persistent contacts, but no general finite-step classification or implication \(\text{vertical exceptional component}\Rightarrow R\ne0\) is asserted.

The appropriate structural question is how the **full filtered ideal**, rather than a chosen pair of initial forms, controls the transforms and their exceptional intersection. Cancellation is a geometric source of higher initial relations; it should be understood through initial ideals, Rees constructions, and valuations, **not** treated as an invitation to enumerate polynomial examples. Weighted initial ideals and tropical/Gröbner methods may help organize valuations and changes of normal direction. Tropicalizations of the individual generators need not determine the initial ideal or tropicalization of \(J\); generator-independent statements require the whole ideal. Seek intrinsic invariants and global constraints first; use examples only to distinguish precise competing assertions.

The valuation tree of persistent horizontal directions and their specializations is a **possible organizing picture**, not an established classification or a canonical tree. It requires a precise choice of valuations and a proof that any proposed invariant is independent of coordinates, generators, and blowup sequence.

## 3A. Initial equations, punctual defects, and integral boundary data

Three distinct operations must be kept separate. Taking the leading normal forms of F and G can miss generators of the full initial ideal H. Passing from the minimal generators of H to the associated graded of the actual equation module J/IJ can then lose further information. Finally, passing to the generic point removes punctual torsion in these sheaves. The canonical exact comparison and its local counterexample are integrated in [Normal-filtration defects](normal_filtration_boundary_obstructions.md#full-initial-ideals-and-the-filtered-equation-module), with the scoped result [R-0030](../results/local_filtration_comparison_defect.md).

The support of the comparison defect lies where both carriers are singular along C. That necessary condition does not prove a punctual defect exists for an intersection with sole reduced support C. Nor does cancellation imply such a defect: the characteristic-two quartic has a higher initial equation but vanishing comparison defect [R-0031](../results/quartic_char2_fourth_equation_kernel.md).

Weighted valuations require the integral coefficient lattice at each point, not only the generic algebra. In the family (x²,y²+t^r x), the integral weighted initial ideals distinguish the boundary exponent r; after inverting t, the generic length remains four. The Smith-form determinant index of a normal-degree relation matrix records torsion missed by entry valuations alone. The calculation and frame-change limitations are in [Weighted initials and normal boundary](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md#weighted-initials-normal-boundary). These invariants can constrain special-point behavior but do not alone imply a global residual curve.

## 4. Where this fits among established results

For the scoped root, graded-relation and actual-CI bridge theorems R-0005–R-0009, use [Chapter 3](03-infinitesimal-geometry.md). For local initial-ideal comparison and saturation, use [Normal-filtration defects](normal_filtration_boundary_obstructions.md). For proper residual cycles, examples and global jet obstructions, use [Residual intersections and jets](residual_intersections_and_jets.md). For fixed-carrier normalization and conductor descent, use [Chapter 4](04-carriers.md) and [Carrier/socle interfaces](carrier_conductor_socle_interfaces.md). The quartic-carrier exclusion [R-0001](../results/quartic_carrier_exclusion.md) remains closed.

**None of these references proves the valuation-theoretic classification proposed below.** In particular, moving from generic formal data to an actual supported pair requires hypotheses not provided by the valuation picture.

## 5. Focused theorem-level questions (all open)

1. **Generic-to-global interface.** What hypotheses on the full initial ideal and its saturation make a horizontal common-direction scheme extend to a controlled global root relation, including special-point defects? Can those defects be related to global normal-jet restrictions?
2. **Residual detection.** Can a generator-independent invariant of successive transforms or the normal filtration distinguish a pure \(C_0\)-supported intersection from one with \(R\ne0\)? Prove a direction of implication before attempting numerical bounds; exceptional vertical curves alone do not suffice.
3. **Valuation-theoretic structure.** Is there a finite intrinsic invariant of persistent generic normal directions, their specialization, and higher cancellation that constrains \(m\), \(R\), or the realizability of \(J\) by global homogeneous equations?
4. **Connection to established obstructions.** Can one verify the precise extra hypotheses that transfer the graded/root-scheme criteria or carrier-conductor restrictions to an actual pair in a nontrivial family of degrees \(d,e\ge5\)?

A productive next round should choose one or two of these interfaces **only after** assessing leverage against the current [frontier](../FRONTIER.md). Generalize beyond \(C_0\) only when doing so is cheap or clarifies a proof. Prefer a structural lemma, counterexample to a proposed implication, or a sharply isolated missing implication over computational casework. This note imposes no mandatory method or priority order.

## 6. Entirely-thick source-preserved cluster and ideal-power facts

The [generic cluster analysis](../notes/2026-10-07-entirely-thick-rees-valuation-framework.md) identifies the higher-contact budget for a supported pair of degrees a,b and generic normal orders p,q. At the generic point of C, the two-dimensional regular local ring has complete-intersection length ab/4. Noether's intersection formula expresses the excess ab/4-pq as the sum of the products of multiplicities over common infinitely-near points, weighted by residue degrees. This bounds the number of generic common centers for fixed a,b,p,q, but not uniformly for fixed ratios a/p and b/q. First normal forms alone do not control length: the pairs (y^2+x^N, y^2+2x^N) have constant first forms and length 2N.

The [relative blowup recursion](../notes/2026-10-07-entirely-thick-relative-blowup-budget.md) says that blowing up a smooth horizontal common center Z with orders r,s subtracts rs[Z] from the pushed-forward intersection cycle of the strict transforms. A later center of covering degree d contributes drs. For the (3,4) boundary, the first exceptional intersection has total coefficient 2pq; **for terminating horizontal trees** this bounds the degree-weighted total common-center budget. It does not imply that the first exceptional bidegree's zero horizontal coordinate prevents later twisting. Persistent formal centers are not thereby shown to algebraize to extra projective common curves.

The [power-saturation theorem](../notes/2026-10-07-rational-quartic-power-saturation.md) settles an earlier open homogeneous-colon question. For the fixed rational quartic and every m>=0,d>=3m, global sections of the mth ideal sheaf in degree d equal the degree-d component of the ordinary homogeneous power, and first sheaf cohomology vanishes. The proof uses the unique smooth quadric Q, the exact sequence from multiplication by Q with quotient O_Q(d-m,d-3m), induction, and products of cubic generators. Thus the degree-3p intersection of the pth power with (Q) is Q times the degree-(3p-2) part of the (p-1)st power, and the quotient is H0(Q,O_Q(2p,0)). This is an exact carrier-space recursion, not a mate exclusion. The earlier [sheaf-colon source](../notes/2026-10-07-thick-sheaf-colon-recursion.md) should not be quoted as leaving this saturation step open.

Finally, the [local thickened-fiber countermodel](../notes/2026-10-07-thickened-fiber-local-countermodel.md) shows that reduced support of a pair along a repeated ruling component constrains only the zeroth-order restriction of the mate, not its higher transverse coefficients. Consequently the thickened-fiber interpolation cokernel is not, by itself, an STCI obstruction. This is a substantive failed mechanism to retain in the research record.

These are source-preservation statements, not a new independent audit of the proofs.

## 7. Entirely-thick marked roots: distinct-root bound and failure of coefficient coupling

The [Segre ruling audit](../notes/2026-10-07-thick-segre-root-audit.md) fixes an essential incidence distinction. On the unique quadric, the two projections of C have degrees one and three. A generic trisecant ruling fiber L meets C in **three distinct points**. A root of the residual F factor on the quadric-direction section makes F vanish at all three, but the residual mate factor restricts to a degree-q section on L and may place all its zeros at only one of them. Thus each distinct root guarantees **at least one**, not three, common first-normal points. The bound `number of distinct roots <= number of horizontal sections <= min(p,q)` survives; a stronger three-points-per-root count does not. At ramified fibers use the scheme-theoretic degree-three intersection, not an invented three-distinct-points assertion.

The [marked-jet separation](../notes/2026-10-07-thick-marked-point-jets.md) distinguishes root multiplicity M_T of the residual F factor from divisorial coefficient r_T of the first exceptional divisor along the corresponding section. Locally `A=z+x^M` has restriction order M on z=0 without containing the transverse section x=0. Hence no general inequality `r_T>=M_T`, and no monotone lower bound on the sectionwise Noether contribution follows from the marked root order alone. In particular `sum M_T=2p` cannot be substituted into the separate budget `sum c_T=2pq` without a coupling theorem.

For a trisecant L meeting C in the degree-three divisor P1+P2+P3, the support-only requirement on a nonzero residual mate restriction `R_G|L` of degree q says its zero divisor is supported on those **up to three points**. It therefore has the form `lambda*ell_1^e1*ell_2^e2*ell_3^e3` with nonnegative exponents summing to q, rather than necessarily a pure qth power at a single distinguished point. The single-point pure-power statement in the marked-point note is valid only with the additional assumption that the allowed support is one point. The open global problem is to couple these exponent allocations, their exceptional clusters, and the restrictions of one global `O_Q(3q,q)` section. This retains the counterexample and the actual discrete incidence data without importing an unjustified stronger assertion.

## 8. Exact ruling interpolation, thickened-fiber discrepancy and smoothing

The [ruling interpolation audit](../notes/2026-10-07-thick-ruling-interpolation-audit.md) proves that for r distinct fibers L_i, restriction `H0(Q,O(3q,q)) -> direct_sum H0(L_i,O(q))` is surjective whenever `r<=3q+1`, by evaluation in the first P1 factor. For each fixed allocation of the degree-q zero divisor among the up to three points of `C intersect L_i`, the allowed nonzero restriction is a one-dimensional subspace of the `(q+1)`-dimensional fiber space. Thus r specified allocations impose **exactly rq linear conditions**; their finite union is still far from empty when `r<=min(p,q)`. A reduced-fiber interpolation count alone cannot exclude the boundary. Multiplicity M_i of a fiber does not add independent conditions on its reduced restriction.

For the [thickened-fiber jet calculation](../notes/2026-10-07-thickened-fiber-jets.md), set `Z=sum_i M_i L_i`, `sum M_i=2p`. The exact sequence `0 -> O_Q(3q-2p,q) -> O_Q(3q,q) -> O_Z(3q,q) -> 0` gives `h0(O_Z(3q,q))=2p(q+1)`. The restriction map is surjective for `2p<=3q+1`; for `2p>3q+1` its cokernel has dimension `(2p-3q-1)(q+1)`. This is a **linear interpolation discrepancy**, not an STCI obstruction: reduced common support does not force the higher mate jets to belong to a specified proper incidence locus. The leading `2pq` term agrees numerically with the first exceptional intersection budget, but the two quantities are not identified.

The [repeated-fiber smoothability note](../notes/2026-10-07-thick-repeated-fiber-smoothability.md) supplies another negative result. Along a repeated residual ruling fiber away from C, the local carrier may have form `F=x^M u+z A`, where `z=0` cuts out Q. Even if `M>=2`, the transverse derivative `A|L` may be nonzero. The degree-3p recursion `F=F_cub+Q K` with `K in (I_C^(p-1))_(3p-2)` permits such a smoothing term because I_C is the unit ideal away from C. Thus repeated residual multiplicity does **not** force generic singularity along L. This does not assert existence of a globally smooth supported STCI pair. Any genuine obstruction must couple the transverse smoothing, mate restrictions, and marked divisor `C intersect L`.

## 9. Exceptional marked section versus trisecant base: unresolved coordinate bridge

The [quadric-section divisor calculation](../notes/2026-10-07-thick-quadric-section-divisor.md) uses `H|E=(4,0)` and `E|E=(7,-1)` to obtain `S_Q=(2H-E)|E=(1,1)`. At the (3,4) boundary, each horizontal exceptional component T_j has class `(0,1)`, hence `T_j.S_Q=1`; if `W=sum c_j T_j` as a cycle, its intersection divisor on S_Q is `sum c_j P_j` of degree `2pq`. The first-normal divisor degrees on S_Q are `6p` and `10q`, not the residual quadric degrees `2p` and `q`. The necessary fixed-factor and coordinate identifications must not be skipped.

**Important unresolved identification:** a trisecant ruling root of `R_F in H0(Q,O(2p,0))` pulls back under the degree-three ruling projection `C -> P1` to a degree-three divisor, whereas an exceptional horizontal T_j of class `(0,1)` meets the graph S_Q at just one point. Therefore no canonical one-to-one matching of ruling roots with exceptional sections has been established by these class calculations. In particular, the previously quoted `#roots <= #horizontal sections` must be treated as **conditional on a correct root-to-section correspondence**, rather than a free consequence of the Segre computation. The class computation and this unresolved comparison should be kept separate from the proven interpolation statements for ruling fibers.

The [first-blowup coupling audit](../notes/2026-10-07-thick-first-blowup-marked-coupling.md) and [root-budget separation](../notes/2026-10-07-thick-root-budget-separation.md) distinguish generic-along-section intersection coefficient c_T from vanishing order M_T at a marked point on S_Q; semicontinuity of finite-flat fiber length cannot compare them because these are not fibers of one such length function. The [marked-trisecant local pair](../notes/2026-10-07-thick-local-pair-marked-trisecant.md) retains the full exponent allocation across `C intersect L` and ambient transverse smoothing, but reduced support still leaves higher local mate coefficients free. An obstruction would need the actual CI cluster, a global divisor/proximity relation, or a justified coordinate bridge between these strata.

## 10. Exact power saturation and degree-3p carrier recursion

The [October 7 rational-quartic power theorem](../notes/2026-10-07-rational-quartic-power-saturation.md) proves for every `m>=0`, `d>=3m` both `H0(P3,I_C^m(d))=(I_C^m)_d` and `H1(P3,I_C^m(d))=0`. The key sheaf exact sequence, using C Cartier of class `(1,3)` on Q, is `0 -> I_C^(m-1)(d-2) --Q--> I_C^m(d) -> O_Q(d-m,d-3m) -> 0`. The cubic generators, after factoring C on Q, span `H0(O_Q(2,0))`; their m-fold products and ambient degree `d-3m` factors surject onto the quadric quotient. Induction proves both vanishing and **ordinary-power** saturation in this range; there is no extra symbolic section at degree at least `3m`.

In particular `(I^p:Q)_(3p-2)=(I^(p-1))_(3p-2)` and `(I^p)_(3p) intersect (Q)=Q (I^(p-1))_(3p-2)`. The [degree-3p quotient note](../notes/2026-10-07-thick-degree-3p-quotient.md) and the power theorem identify `(I^p)_(3p)/Q(I^(p-1))_(3p-2)` with `H0(Q,O_Q(2p,0))`. Thus every degree-3p order-at-least-p carrier is `F=F_cub+QK`, with `F_cub` a combination of products of p cubic generators and `K in (I^(p-1))_(3p-2)`. This describes the full ambient vector space but does **not** control its singularities, normalization, or mate support. It also justifies the transverse smoothing freedom discussed above without asserting that every such smoothing occurs globally.

## 11. Valuation data with coordinate and integral-model discipline

The weighted-initial investigation starts with K=k(C), a rational normal frame X,Y, a closed point p, and the discrete valuation v_p on K. For polynomial expressions and integer weights (alpha,beta), define

    v_(p,alpha,beta)(sum a_ij X^i Y^j)
      = min {v_p(a_ij)+i*alpha+j*beta : a_ij nonzero}.

In this chosen frame the construction is a Gauss valuation on K(X,Y). Its initial polynomial retains all terms attaining the minimum; its *initial ideal* must be formed from every element of the ideal, not merely from the initials of F and G. The [weighted-initial source](../notes/2026-10-26-weighted-initials-normal-boundary.md) studies the resulting Newton and Groebner chambers and records its restrictions on formal series. This is a coordinate-dependent calculation, not yet an intrinsic invariant of the embedded pair.

Two distinctions are essential. First, multiplying a generator by a rational coefficient changes its scalar value, so taking the infimum of v_(p,w) over every nonzero element of a K-ideal is meaningless: powers of a local parameter in the denominator drive that infimum to minus infinity. The integral model over O_(C,p), its saturation, and the associated graded coefficient ring retain the boundary information that would otherwise disappear. Second, the rational frame changes at p; the individual coefficient valuations and Newton polygons can change. The intrinsic leading symbols instead live in symmetric conormal powers, and their divisors require the correct transition functions.

For a research test, retain the chosen frame, integral lattice, full initial ideal, and transformation rule. Only after proving frame invariance may a chamber boundary or valuation defect be called a geometric obstruction. Monomial-containing initials must be included; restricting to the tropical (monomial-free) locus would discard relevant specializations.

## 12. What the exact ideal-power theorem contributes

The [October 7 power-saturation theorem](../notes/2026-10-07-rational-quartic-power-saturation.md) gives, for the fixed rational quartic and every m>=0, d>=3m,

    H^0(P3, I_C^m(d)) = (I_C^m)_d,
    H^1(P3, I_C^m(d)) = 0.

This is a source-level proved theorem retained here without a new promotion decision. Its proof uses the exact sequence through the unique quadric Q, on which C has class (1,3):

    0 -> I_C^(m-1)(d-2) --Q--> I_C^m(d)
      -> O_Q(d-m,d-3m) -> 0.

The H1 vanishing follows by induction in the stated range, and products of the three cubic generators span the quadric quotient after factoring C. The theorem says that ordinary homogeneous powers already supply all global sections of the ideal-sheaf power in degrees at least 3m; no additional symbolic section appears in that range.

At d=3p it gives a recursive description of *all* order-at-least-p carriers: the quotient of (I^p)_(3p) by Q*(I^(p-1))_(3p-2) is H^0(Q,O_Q(2p,0)), represented by products of p cubic generators. Thus every such carrier can be written as a cubic-product combination plus Q*K with K in (I^(p-1))_(3p-2).

This closes an ambient-source completeness question for these degrees, but not the STCI problem. It does not constrain singularities of an arbitrary carrier in the space, the generic initial ideal of a mate, or the absence of residual support. The distinction is important: a complete parameterization of a vector space is not a classification of the geometry of its members.

## 12A. The difference between source completeness and symbol surjectivity

The ideal-power theorem identifies every actual ambient section of \(I_C^m(d)\) with an ordinary degree-\(d\) product expression for \(d\ge3m\). Its next restriction map
\[
H^0(I_C^m(d))\longrightarrow H^0(C,\operatorname{Sym}^m(I_C/I_C^2)(d))
\]
can nevertheless have a proper image. The source theorem controls its **domain**, not its rank or cokernel. A higher-order jet from the same global equation must also satisfy compatibility with the lower orders; arbitrary choices in distinct graded pieces need not glue.

This explains why a complete degree-\(3m\) recursion is useful for finite experiments but is not a global STCI obstruction. It supplies a finite ambient parameter space; one still needs a uniform transverse-length or conductor argument on the proper-pair locus. The [global-source section](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md) records the exact image-as-kernel formulation using the connecting map to \(H^1(I_C^{m+1}(d))\).

## 13. A single local-to-global test protocol

For an actual proper pair F,G, begin with its generic colength and full I-initial ideal over K, then compute the horizontal exceptional directions. At each special point, record the conormal frame transition and the *integral* weighted-initial lattice, including cancellation-generated relations and any torsion. If a curvilinear saturated flag is available, apply the scoped residual-zero-cycle formulas; otherwise record precisely why the hypotheses fail. Next test whether the candidate local jets lie in the image of the global degree-d and degree-e equation spaces, using the exact power theorem when its degree range applies. Finally compute the projective residual cycle, not just the exceptional support.

A negative computation should identify which step fails and whether the failure is stable across a whole parameter family. This protocol is provisional: it does not assert that passing every finite test yields global equations or that failure of an isolated test excludes all STCI pairs.

## 14. Why marked trisecant and ruling tests did not force a contradiction

The [marked-trisecant local calculation](../notes/2026-10-07-thick-local-pair-marked-trisecant.md) is an informative negative result. On Q near a transverse point of a trisecant ruling L meeting C, choose parameters with L=(u) and C=(y). If a carrier restricts as F|Q=y^p*u^M times a unit and the mate as G|Q=y^q*R_G, the reduced-support condition along L only fixes R_G(0,y)=y^e times a unit. It does not fix the u-dependent coefficients of R_G or the coefficient transverse to Q. Even retaining the multiplicity M and all three marked intersections of L with C does not produce the desired local coupling without extra global hypotheses.

This explains why imposing a contact budget on the ruling alone is insufficient: the ambient normal direction remains free. To turn this into an obstruction, one must identify a global divisor relation, a proximity constraint on an actual complete-intersection cluster, or a justified compatibility map between the ruling and ambient transverse data. The negative result is about the insufficiency of a method, not evidence that an STCI exists.

## 15. Intrinsic flags versus scalar valuation lists

The [coefficient-valuation study](../notes/2026-10-23-intrinsic-coefficient-valuations.md) distinguishes the intrinsic normal blowup and subsequent valuation flags from the noncanonical choice of a coefficient field and transverse coordinates. On the full formal ring K[[U,V]], weights that assign positive order to U,V support normal-first valuations under their stated domain conditions; coefficient-first Gauss expressions for arbitrary real weights require separate convergence/domain control. Their associated initial ideals and residue polynomials carry more information than a collection of scalar values of elements.

The same study gives a warning from the prescribed mu4 family: even knowing scalar values of an ideal for all selected weights does not in general recover transverse length. Cancellation, residue classes, and higher initials matter. Consequently the useful object is a filtered ideal or an initial algebra together with its integral model and frame transitions, not a numerical valuation score.

This is a provisional methodological distinction, not an assertion that a canonical valuation invariant already decides residual support.

## 16. Family-level failure analysis

The entirely-thick investigations have produced both exact positive tools and instructive dead ends. The degree-3p quotient and power-saturation theorem determine global equation spaces in a stable degree range. The marked-trisecant and ruling interpolation tests show that a reduced-support condition does not automatically constrain all transverse coefficients. The weighted-initial framework tracks degeneration but does not, without a comparison theorem, force residual support.

A next experiment should therefore state the invariant class it tests, the specific global source image it uses, and the exact step where the proposed local-to-global implication fails. Do not restart an unbounded search through isolated equations after each failure; ask whether the failure persists for the entire family and what additional hypothesis would make the implication valid.

## 17. Arithmetic support and normal specialization

R-0021 supplies a flat integral pair whose characteristic-zero intersection has four reduced quartic components, while the characteristic-two intersection has sole reduced support C and transverse length four. R-0020 describes the associated change in conormal splitting. These facts demonstrate that flatness preserves neither the number of reduced components nor the form of the normal initial ideal.

R-0012 excludes a lift of precisely this special embedded scheme over Z_(2) or Z_2 only when the generic reduced support must be C. The displayed integral family does not satisfy that extra generic-support requirement. Consequently a valuation or blowup argument using specialization must keep the embedded model, base, full initial ideal, and support condition separate.
