# Formal normal geometry and residual intersections: research interface

This exploratory synthesis supplements [Chapter 2](02-two-surfaces.md),
[Chapter 3](03-infinitesimal-geometry.md), and the [mechanism map](../MAP.md).
For precise claims use the [research catalog](../CATALOG.md) and the
[evidence and review rules](../MODEL.md#evidence-and-review).

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

The support of the comparison defect lies where both carriers are singular along C. The characteristic-two quartic has a higher initial equation from cancellation and vanishing comparison defect [R-0031](../results/quartic_char2_fourth_equation_kernel.md). See the [open sole-support question](../FRONTIER.md#punctual-relative-defect-under-sole-support).

Weighted valuations require the integral coefficient lattice at each point, not only the generic algebra. In the family (x²,y²+t^r x), the integral weighted initial ideals distinguish the boundary exponent r; after inverting t, the generic length remains four. The Smith-form determinant index of a normal-degree relation matrix records torsion missed by entry valuations alone. The calculation and frame-change limitations are in [Weighted initials and normal boundary](normal_filtration_boundary_obstructions.md#weighted-initials-normal-boundary). These invariants can constrain special-point behavior but do not alone imply a global residual curve.

## 4. How the comparison lemmas fit together

For the scoped root, graded-relation and actual-CI bridge theorems R-0005–R-0009, use [Chapter 3](03-infinitesimal-geometry.md). For local initial-ideal comparison and saturation, use [Normal-filtration defects](normal_filtration_boundary_obstructions.md). For proper residual cycles, examples and global jet obstructions, use [Residual intersections and jets](residual_intersections_and_jets.md). For fixed-carrier normalization and conductor descent, use [Chapter 4](04-carriers.md). The quartic-carrier exclusion [R-0001](../results/quartic_carrier_exclusion.md) remains closed.

**None of these references proves the valuation-theoretic classification proposed below.** In particular, moving from generic formal data to an actual supported pair requires hypotheses not provided by the valuation picture.

## 5. Focused theorem-level questions (all open)

1. **Generic-to-global interface.** What hypotheses on the full initial ideal and its saturation make a horizontal common-direction scheme extend to a controlled global root relation, including special-point defects? Can those defects be related to global normal-jet restrictions?
2. **Residual detection.** Can a generator-independent invariant of successive transforms or the normal filtration distinguish a pure \(C_0\)-supported intersection from one with \(R\ne0\)? Prove a direction of implication before attempting numerical bounds; exceptional vertical curves alone do not suffice.
3. **Valuation-theoretic structure.** Is there a finite intrinsic invariant of persistent generic normal directions, their specialization, and higher cancellation that constrains \(m\), \(R\), or the realizability of \(J\) by global homogeneous equations?
4. **Connection to established obstructions.** Can one verify the precise extra hypotheses that transfer the graded/root-scheme criteria or carrier-conductor restrictions to an actual pair in a nontrivial family of degrees \(d,e\ge5\)?

A productive next round should choose one or two of these interfaces **only after** assessing leverage against the current [frontier](../FRONTIER.md). Generalize beyond \(C_0\) only when doing so is cheap or clarifies a proof. Prefer a structural lemma, counterexample to a proposed implication, or a sharply isolated missing implication over computational casework. This note imposes no mandatory method or priority order.

## 6. Entirely-thick source-preserved cluster and ideal-power facts

The [generic cluster analysis](rees_and_vertical_controls.md#2026-10-07-entirely-thick-rees-valuation-framework) identifies the higher-contact budget for a supported pair of degrees a,b and generic normal orders p,q. At the generic point of C, the two-dimensional regular local ring has complete-intersection length ab/4. Noether's intersection formula expresses the excess ab/4-pq as the sum of the products of multiplicities over common infinitely-near points, weighted by residue degrees. This bounds the number of generic common centers for fixed a,b,p,q, but not uniformly for fixed ratios a/p and b/q. First normal forms alone do not control length: the pairs (y^2+x^N, y^2+2x^N) have constant first forms and length 2N.

The [relative blowup recursion](rees_and_vertical_controls.md#2026-10-07-entirely-thick-relative-blowup-budget) says that blowing up a smooth horizontal common center Z with orders r,s subtracts rs[Z] from the pushed-forward intersection cycle of the strict transforms. A later center of covering degree d contributes drs. For the (3,4) boundary, the first exceptional intersection has total coefficient 2pq; **for terminating horizontal trees** this bounds the degree-weighted total common-center budget. It does not imply that the first exceptional bidegree's zero horizontal coordinate prevents later twisting. Persistent formal centers are not thereby shown to algebraize to extra projective common curves.

The [local thickened-fiber countermodel](#the-local-thickened-fiber-countermodel) shows that reduced support along a repeated ruling component constrains the zeroth-order restriction of the mate and leaves its higher transverse coefficients free.

These are source-preservation statements, not a new independent audit of the proofs.

## 7. Entirely-thick marked roots: distinct-root bound and failure of coefficient coupling

Use the ruling convention in which C has class (1,3) on the unique quadric. In Segre coordinates the parametrization is `[s³:t³] x [s:t]`, with the middle ambient coordinates ordered accordingly. The first ruling projection has degree three and the second has degree one. In characteristic zero, or characteristic different from three, a generic fiber L of the first projection meets C in **three distinct points**. A root of the residual F factor on the quadric-direction section makes F vanish at all three, but the residual mate factor restricts to a degree-q section on L and may place all its zeros at only one of them. Thus each distinct root guarantees **at least one**, not three, common first-normal points. In the exact sole-support balanced boundary a=3p,b=4q, the actual strict-intersection purity argument in section9 gives a choice-dependent injection into the constant exceptional sections, proving `number of roots <= number of sections <= min(p,q)`. A stronger three-points-per-root count still fails. At ramified fibers use the scheme-theoretic degree-three intersection, not an invented three-distinct-points assertion.

The [marked-jet separation](https://github.com/markluxton1/STCI/blob/ffe78df0f9d4378255d1a2cdcf64b2e8a80a4655/research/supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-marked-point-jetsmd) distinguishes root multiplicity M_T of the residual F factor from divisorial coefficient r_T of the first exceptional divisor along the corresponding section. Locally `A=z+x^M` has restriction order M on z=0 without containing the transverse section x=0. Hence no general inequality `r_T>=M_T`, and no monotone lower bound on the sectionwise Noether contribution follows from the marked root order alone. In particular `sum M_T=2p` cannot be substituted into the separate budget `sum c_T=2pq` without a coupling theorem.

For a trisecant L meeting C in the degree-three divisor P1+P2+P3, the support-only requirement on a nonzero residual mate restriction `R_G|L` of degree q says its zero divisor is supported on those **up to three points**. It therefore has the form `lambda*ell_1^e1*ell_2^e2*ell_3^e3` with nonnegative exponents summing to q, rather than necessarily a pure qth power at a single distinguished point. The single-point pure-power statement in the marked-point note is valid only with the additional assumption that the allowed support is one point. The open global problem is to couple these exponent allocations, their exceptional clusters, and the restrictions of one global `O_Q(3q,q)` section. This retains the counterexample and the actual discrete incidence data without importing an unjustified stronger assertion.

## 8. Exact ruling interpolation, thickened-fiber discrepancy and smoothing

For r distinct ruling fibers L_i, restriction `H0(Q,O(3q,q)) -> direct_sum H0(L_i,O(q))` is surjective whenever `r<=3q+1`, by evaluation in the first P1 factor. For each fixed allocation of the degree-q zero divisor among the up to three points of `C intersect L_i`, the allowed nonzero restriction is a one-dimensional subspace of the `(q+1)`-dimensional fiber space. Thus r specified allocations impose **exactly rq linear conditions**; their finite union is still far from empty when `r<=min(p,q)`. A reduced-fiber interpolation count alone cannot exclude the boundary. Multiplicity M_i of a fiber does not add independent conditions on its reduced restriction.

For higher transverse jets set `Z=sum_i M_i L_i`, `sum M_i=2p`. The exact sequence `0 -> O_Q(3q-2p,q) -> O_Q(3q,q) -> O_Z(3q,q) -> 0` gives `h0(O_Z(3q,q))=2p(q+1)`. The restriction map is surjective for `2p<=3q+1`; for `2p>3q+1` its cokernel has dimension `(2p-3q-1)(q+1)`. This is a **linear interpolation discrepancy**, not an STCI obstruction: reduced common support does not force the higher mate jets to belong to a specified proper incidence locus. The leading `2pq` term agrees numerically with the first exceptional intersection budget, but the two quantities are not identified.

### The local thickened-fiber countermodel

Let `h=0` cut out C on Q and take regular coordinates x,y near a point
of a ruling fiber `L=(x=0)` in Q. Locally the quadric restrictions can be
written
```text
F|Q = h^p x^M u,
G|Q = h^q (A_0(y) + x A_1(y) + ... + x^(M-1) A_(M-1)(y) + x^M B(x,y))
```
with u a unit. Off C, their reduced common set on Q is given by
`x=A_0(y)=0`. Fix any nonzero A_0 whose zeros on L are supported on
`C intersect L`. All choices of the higher transverse coefficients then have
the same reduced common set there. The countermodel is local on Q. An
obstruction to actual global pairs would require a further compatibility
between transverse coefficients, contact at the marked divisor, and the
intersection of the strict transforms.

Away from C the ambient carrier can have local equation `F=x^M u+z A`,
where `z=0` cuts out Q. For `M>=2` the derivative in x vanishes on L and
the transverse derivative is `A|L`. The degree-3p recursion
`F=F_cub+Q K` allows K in the degree-(3p-2) order-(p-1) source. The local
ideal sheaf of C is the unit ideal away from C. A chosen global K giving
a nonzero restriction makes the carrier smooth at the generic point of L.
Repeated residual multiplicity alone supplies no local singularity
condition. The mate and simultaneous support still require their own
analysis.

The October 7 sources give the full local countermodel, marked ruling
correction, and interpolation calculation. [Historical source compilation](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md).

<a id="9-exceptional-marked-section-versus-trisecant-base-unresolved-coordinate-bridge"></a>

## 9. Actual strict restrictions and the residual-root count

The [quadric-section divisor calculation](https://github.com/markluxton1/STCI/blob/ffe78df0f9d4378255d1a2cdcf64b2e8a80a4655/research/supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-quadric-section-divisormd) uses `H|E=(4,0)` and `E|E=(7,-1)` to obtain `S_Q=(2H-E)|E=(1,1)`. At the (3,4) boundary, each horizontal exceptional component T_j has class `(0,1)`, hence `T_j.S_Q=1`; if `W=sum c_j T_j` as a cycle, its intersection divisor on S_Q is `sum c_j P_j` of degree `2pq`. The first-normal divisor degrees on S_Q are `6p` and `10q`, not the residual quadric degrees `2p` and `q`. The necessary fixed-factor and coordinate identifications must not be skipped.

**The count bridge on the exact boundary is proved.** The blowup restricted to Q is the blowup of its Cartier divisor C, hence the strict transform Qtilde is Q itself and E|Qtilde=C. Consequently the actual strict divisor restrictions are exactly R_F and R_G, including their local equations and multiplicities. For each residual ruling root ℓ of R_F, R_G|ℓ is a nonzero section of O_ℓ(q); otherwise ℓ would be an extra common curve. Choose a zero P. Sole support forces P∈C, so its lift lies in the actual proper strict-transform intersection W and on S_Q. On a=3p,b=4q, W is pure with effective cycle of class(0,2pq); its support consists of constant sections T_j. Each T_j meets S_Q in one point, and distinct ruling fibers are disjoint, so the chosen points give an injection of distinct ruling roots into distinct T_j. This proves the count bound without a canonical bijection. The [complete supported-cycle and root-count proof](rees_and_vertical_controls.md) retains its exact hypotheses and the additional no-vertical refinement.

The degree-three pullback of a ruling root need not map pointwise to three different sections: only the selected mate zero is used. This resolves the earlier overly broad statement that a count correspondence was missing. It does **not** identify the root multiplicity M_i with the cycle coefficient c_j, compare their local Noether contributions, or supply this bound outside the exact supported balanced boundary.

The [first-blowup coupling audit](https://github.com/markluxton1/STCI/blob/ffe78df0f9d4378255d1a2cdcf64b2e8a80a4655/research/supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-first-blowup-marked-couplingmd) distinguishes generic-along-section intersection coefficient c_T from vanishing order M_T at a marked point on S_Q; semicontinuity of finite-flat fiber length cannot compare them because these are not fibers of one such length function. The [marked-trisecant local pair](https://github.com/markluxton1/STCI/blob/ffe78df0f9d4378255d1a2cdcf64b2e8a80a4655/research/supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-local-pair-marked-trisecantmd) retains the full exponent allocation across `C intersect L` and ambient transverse smoothing, but reduced support still leaves higher local mate coefficients free. An obstruction would need the actual CI cluster, a global divisor/proximity relation, or a justified coordinate bridge between these strata.

## 11. Valuation data with coordinate and integral-model discipline

The weighted-initial investigation starts with K=k(C), a rational normal frame X,Y, a closed point p, and the discrete valuation v_p on K. For polynomial expressions and integer weights (alpha,beta), define

    v_(p,alpha,beta)(sum a_ij X^i Y^j)
      = min {v_p(a_ij)+i*alpha+j*beta : a_ij nonzero}.

In this chosen frame the construction is a Gauss valuation on K(X,Y). Its initial polynomial retains all terms attaining the minimum; its *initial ideal* must be formed from every element of the ideal, not merely from the initials of F and G. The [weighted-initial source](normal_filtration_boundary_obstructions.md#weighted-initials-normal-boundary) studies the resulting Newton and Groebner chambers and records its restrictions on formal series. This is a coordinate-dependent calculation, not yet an intrinsic invariant of the embedded pair.

Two distinctions are essential. First, multiplying a generator by a rational coefficient changes its scalar value, so taking the infimum of v_(p,w) over every nonzero element of a K-ideal is meaningless: powers of a local parameter in the denominator drive that infimum to minus infinity. The integral model over O_(C,p), its saturation, and the associated graded coefficient ring retain the boundary information that would otherwise disappear. Second, the rational frame changes at p; the individual coefficient valuations and Newton polygons can change. The intrinsic leading symbols instead live in symmetric conormal powers, and their divisors require the correct transition functions.

For a research test, retain the chosen frame, integral lattice, full initial ideal, and transformation rule. Only after proving frame invariance may a chamber boundary or valuation defect be called a geometric obstruction. Monomial-containing initials must be included; restricting to the tropical (monomial-free) locus would discard relevant specializations.

## 12. Ordinary ideal powers on a smooth quadric: complete proof

Let Q≅P1×P1 be a split smooth quadric over a field and C an integral Cartier divisor of class (a,b), with 1<=a<=b. Let I be its saturated homogeneous prime ideal in P3. The inherited independently reviewed theorem is stronger than a high-degree saturation bound: for every m>=0 and every integer d,

    H^0(P3,I_C^m(d))=(I^m)_d,   I^m=(I^m)^sat=I^(m).   (P)

For b>=2, one additionally has H^1(P3,I_C^m(d))=0 whenever d>=bm. For the rational quartic (a,b)=(1,3), this gives H1 vanishing from d=3m but ordinary/symbolic equality in every degree. Smoothness of C is not needed for this integral Cartier-divisor theorem. The complete inherited proof and classical monomial overlap are in [the uniform quadric proof](global_equations_and_constructions.md#2-uniform-theorem-for-integral-curves-on-a-smooth-quadric). This consolidation recovers that stronger existing scope; it does not claim a new theorem or novelty.

Locally C is cut out by Q and a local Cartier equation h on Q, so these
two classes form a basis of the conormal module. The associated graded of
this regular immersion is its symmetric algebra. Multiplication by the
class of Q is multiplication by one polynomial variable, hence injective.
For `m>=1` a class of order `j<m-1` then has product with Q of order
`j+1<m`. This proves the sheaf colon
`(I_C^m:Q)=I_C^(m-1)` without a linear-type assumption. The homogeneous
equality follows separately from the all-degree argument below.
[Original sheaf calculation](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/supplements/OCT7_THICK_FIBRES_AND_OCT8_CONTINUATION.md#source-2026-10-07-thick-sheaf-colon-recursionmd).
Restriction gives

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

This explains why a complete degree-\(3m\) recursion is useful for finite experiments but is not a global STCI obstruction. It supplies a finite ambient parameter space; one still needs a uniform transverse-length or conductor argument on the proper-pair locus. The [global-source section](normal_filtration_boundary_obstructions.md#normal-boundary-weighted-initials-and-lifting) records the exact image-as-kernel formulation using the connecting map to \(H^1(I_C^{m+1}(d))\).

## 13. A single local-to-global test protocol

For an actual proper pair F,G, begin with its generic colength and full I-initial ideal over K, then compute the horizontal exceptional directions. At each special point, record the conormal frame transition and the *integral* weighted-initial lattice, including cancellation-generated relations and any torsion. If a curvilinear saturated flag is available, apply the scoped residual-zero-cycle formulas; otherwise record precisely why the hypotheses fail. Next test whether the candidate local jets lie in the image of the global degree-d and degree-e equation spaces, using the exact power theorem when its degree range applies. Finally compute the projective residual cycle, not just the exceptional support.

A negative computation should identify which step fails and whether the failure is stable across a whole parameter family. This protocol does not assert that passing every finite test yields global equations or that failure of an isolated test excludes all STCI pairs.

## 14. Why marked trisecant and ruling tests did not force a contradiction

The [marked-trisecant local calculation](https://github.com/markluxton1/STCI/blob/ffe78df0f9d4378255d1a2cdcf64b2e8a80a4655/research/supplements/OCT7_THICK_CARRIERS_AND_MARKED_GEOMETRY.md#source-2026-10-07-thick-local-pair-marked-trisecantmd) is an informative negative result. On Q near a transverse point of a trisecant ruling L meeting C, choose parameters with L=(u) and C=(y). If a carrier restricts as F|Q=y^p*u^M times a unit and the mate as G|Q=y^q*R_G, the reduced-support condition along L only fixes R_G(0,y)=y^e times a unit. It does not fix the u-dependent coefficients of R_G or the coefficient transverse to Q. Even retaining the multiplicity M and all three marked intersections of L with C does not produce the desired local coupling without extra global hypotheses.

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


## Consolidated historical supplement: `research/supplements/HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md`

# higher initial ideals and embedded thickenings

## Integration guide: cancellations and higher embedded data

The [higher-initial investigation](#2026-10-21-higher-initial-ideals-valuations) records how cancellations between leading normal forms create higher initial generators; the explicit examples must be retained because they rule out replacing the full initial ideal with just the first symbols. The [embedded ribbon/triple obstruction](#2026-10-21-intrinsic-embedded-ribbon-triple-obstruction) concerns a different global extension and gluing problem, with its own Čech and coordinate-invariance hypotheses.

Compare the [full ideal-filtration diagram](https://github.com/markluxton1/STCI/blob/ca33958696fdc4f06a1c39b160aa13d097f24146/research/supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md#2026-10-23-ideal-filtrations-independent-investigationmd), the [valuation length counterexample](../synthesis/coefficient_valuations.md), and the [boundary equation-module test](toric_torsion_and_endpoint_contacts.md#2026-10-27-one-step-boundary-obstruction). The common obstruction to an overly simple approach is loss of higher-order or gluing information, **not** a theorem that any given local thickening fails globally.

The original coprime theorem, examples, and unreviewed status remain intact below.

---


Complete mathematical arguments and exploratory boundaries preserved. Conditional conclusions remain conditional; computational and geometric obstructions are not asserted beyond their original hypotheses.

---

## 2026-10-21-higher-initial-ideals-valuations

# Higher initial ideals and transverse valuations — research note (2026-10-21)

Status: PROPOSAL; no independent review. Branch only.

## Setup
Let I be the homogeneous ideal of C0 in S and J=(F,G). The global gr_I(S)=⊕ I^n/I^{n+1} has two gradings: homogeneous polynomial degree and filtration degree. Its sheafification along C0 is Sym(I_C/I_C²), but global sections of the latter need not be obtained from individual global graded pieces without saturation. At η_C, completion gives K[[x,y]] with K=k(C0), and gr_m=K[X,Y]. The full initial ideal in_m(JR) includes leading forms of every combination AF+BG; it is generally larger than (in F,in G). Generic localization can lose special-point torsion/degeneration.

## Coprime theorem
If in(F)=F_r and in(G)=G_s are relatively prime, they are a homogeneous regular sequence; the filtered Koszul argument gives gr(R/J)=K[X,Y]/(F_r,G_s), and length(R/J)=rs. In an STCI with no residual components, Bézout gives de=4 length(R/J), hence de=4rs in this case.

## Explicit cancellation examples
(1,1): F=x, G=x+y^n, n>=2. The full initial ideal is (X,Y^n), length n, whereas the individual initials generate only (X).
(2,2): F=x², G=x²+y³. Cancellation gives J=(x²,y³), initial ideal (X²,Y³), length 6, rather than 4.
(2,3): F=x², G=x³+y^5. Cancellation by xF gives J=(x²,y^5), initial ideal (X²,Y^5), length 10 rather than 6.
These are local transverse models, not global STCI constructions.

## Quartic benchmark, local chart x0=1
Put t=x1, u=x2-t³, v=x3-t⁴. Then C is u=v=0. For F=x1⁴-x0³x3, G=x2⁴-x0 x3³:
F=-v.
G=(t³+u)^4-(t⁴+v)^3.
Modulo F, G reduces to (t³+u)^4-t¹².
At generic t ≠0, characteristic 0: initial G modulo F is 4t^9 u, so J=(v,u) and length 1. Characteristic 2: (t³+u)^4-t¹²=u⁴, so J=(v,u⁴), full initial ideal (V,U⁴), length 4. The individual initial forms in characteristic 2 are F_1=-V and G_1=-t^8 V (since (t⁴+v)^3 has linear term t⁸v), so cancellation is essential. In characteristic zero, G_1=4t⁹U-3t⁸V, and initial forms are coprime. Over algebraic closure of K in characteristic zero the transverse scheme is generically reduced of length one at C; other components of the (4,4) intersection must occur elsewhere, so the pair is not STCI in characteristic zero. In characteristic two it is a length-four curvilinear thickening along C at the generic point. Global radical equality requires separate projective chart/boundary verification.

## Valuations
The m-adic order is total transverse degree and is not a valuation on K itself. For each closed p in C, ord_p on K gives a discrete base valuation. Weight vectors (w_x,w_y)>0 give monomial valuations on K(x,y) with trivial base valuation; after choosing p, Gauss-type extensions v(Σ a_ij x^i y^j)=min(ord_p(a_ij)+i w_x+j w_y) give base-sensitive information, subject to coordinate choice and suitable completion. Composite lexicographic valuations retain transverse order and then coefficient order. Newton polygons/infinitely near points resolve common tangent factors and distinguish transverse branches; a single m-adic initial ideal generally does not encode their Puiseux exponents. Weighted initial ideals of the full ideal, not just two generators, are required. Rees valuations of J describe normalized blowup data but need not recover all infinitely near branches.

## Globalization and limitations
The degree-d normal symbol of F of I-order r is a section of Sym^r(N_C^∨)⊗O_C(d), which for the characteristic-zero balanced splitting is O_{P¹}(4d-7r)^{⊕(r+1)} (O_C(1)=O_{P¹}(4)). Thus a nonzero symbol requires 4d-7r>=0; similarly 4e-7s>=0. This is a necessary degree constraint, not a new STCI exclusion. The local (x,y) coordinates are only rational frames of the conormal bundle: rational cancellation coefficients generally have poles at closed points and do not produce ambient global polynomial combinations. Clear denominators only after tracking the induced twists and possible extra zero divisors. In characteristic two do not use the characteristic-zero normal-bundle splitting.

Related notes: [residual-cycle and wedge distinctions](../synthesis/residual_contact_cycles.md#wedge-degeneracy-distinguishes-neither-thickness-nor-residual-contact); [special-fiber length and standard bases](../synthesis/valuations_and_residual_contact.md#valuative-standard-bases-and-special-length-jumps); [orders, Hilbert filtration, and duality](normal_filtration_boundary_obstructions.md#source-2026-10-21-equality-orders-filtration-dualitymd).

## Conormal splitting and quartic family references

- [STCI-R-0020](../results/quartic_conormal_characteristic_jump.md): audited characteristic-dependent conormal splitting; the balanced formula above applies when the characteristic is not two.
- [STCI-R-0021](../results/quartic_mu4_degeneration.md): audited global behavior of the prescribed quartic pair, including its four characteristic-zero components and characteristic-two support.
- [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md) and [STCI-R-0016](../results/nonsaturated_first_relation_resultant.md): conditional normal-flatness and first-relation-defect results; neither applies to arbitrary full initial ideals without its hypotheses.

## Priorities
1. Compute a standard basis of the actual generic ideal for arbitrary candidate F,G and retain each cancellation certificate.
2. Track denominators of certificates at closed points and formulate sheaf-valued graded relations with saturation.
3. Compare base-sensitive weighted valuations at each exceptional point with global degree constraints.
4. Seek a numerical exclusion for nonsaturated relations and both orders >=2; no such exclusion is proved here.

This note does not claim the generic local data determine global radical equality or that the example proves a characteristic-zero impossibility theorem.


---

## 2026-10-21-intrinsic-embedded-ribbon-triple-obstruction

# The embedded ribbon-to-triple obstruction

The characteristic-free ideal-sheaf construction fixes the embedded
ribbon and its conormal quotient. The [October 21 audit](#independent-audit-and-arithmetic-provenance)
independently reconstructed this correction of the difference-of-lifts
argument. The quartic Laurent coefficients come from the separate
[arithmetic calculation](#quartic-consistency).

## The canonical embedded extension

Let `i:C -> X` be a regular immersion of codimension two of schemes, with ideal `I`, and `E=I/I²`. Fix a surjective homomorphism of locally free sheaves `q:E -> L` with `L` invertible and kernel `M` invertible. Put `J₂=ker(I -> E -> L)`, and define the **canonical ideal** `K=I J₂+I³` (indeed `I³ ⊂ I J₂`).

There is a canonical exact sequence of **O_C-modules**
```
0 -> L^⊗2 -> J₂/K -> M -> 0.                    (*)
```
The sheaf of embedded ideals `J₃` satisfying `I³ ⊂ J₃ ⊂ J₂`, with local primitive-triple normal form `(x-a y²,I³)` for generators adapted to `q`, is canonically identified with the sheaf of O_C-linear splittings of (*). It is a locally nonempty torsor under `H=Hom_O_C(M,L²)`. Its class is exactly the Yoneda extension class
```
o_X(q) = [J₂/K] ∈ Ext¹_O_C(M,L²) = H¹(C,H).
```
It vanishes exactly when a global embedded primitive triple exists. If one exists, the set of global embedded triples is a torsor under `H⁰(C,H)`.

This holds in arbitrary characteristic, including mixed-characteristic DVRs; smoothness over a DVR is sufficient but not required beyond the stated regular immersion and locally free quotient. The claim is about embedded ideals in the fixed X and the fixed quotient q, not about abstract multiple curves.

## Independent proof

1. Regular immersion gives `I²/I³ ≅ Sym²(E)`. Since `J₂` is the inverse image of `M`, `I² ⊂ J₂`, and the image of `I J₂` in `I²/I³` is precisely the image `ME` of `M ⊗ E -> Sym²(E)`. Consequently
```
(I²+K)/K = I²/(I J₂+I³) ≅ Sym²(E)/(ME) ≅ Sym²(L)=L².
```
The last isomorphism is canonical for a line quotient, with no need to invert 2. The quotient `J₂/I²=M`. These identify the kernel and cokernel of (*).

2. Since `I J₂ ⊂ K`, multiplication by `I` kills `J₂/K`. Thus (*) is genuinely an exact sequence of O_C-modules, not a spurious O_C-module structure on `I/I³`. This repairs the central gap in the earlier proof.

3. For any admissible `J₃`, `I J₃ ⊂ J₃`, `I³ ⊂ J₃`, and the local normal form implies that the image of `J₃` in `E` is `M` and its intersection with `I²` modulo `I³` is `ME`. Therefore `K ⊂ J₃` and `J₃/K -> M` is an isomorphism: its inverse is a splitting of (*).

4. Conversely, a splitting `s:M -> J₂/K` has image an O_C-submodule. Its inverse image `J₃` in `J₂` is an O_X-ideal because the action modulo `K` factors through `O_C`. It contains `K` and hence `I³`, and maps onto `M` with quadratic intersection `ME`. Locally choose adapted generators `x,y` of `I`, with `x` mapping to a frame of `M` in `E` and `y` to a frame of `L`. The splitting is generated modulo `K` by `w=x-a y²` for some local coefficient `a`. Since `J₂=(x,y²)=(w,y²)`, the product `I J₂` lies in `(w,I³)`. Thus `J₃=(w,K)=(w,I³)=(w,y³)`, using `I=(w,y)` in the last equality. The quotient has graded pieces `O_C,L,L²` by the linear image `M` and quadratic intersection `ME`. This construction uses no division.

5. Splittings of an exact sequence with locally free quotient M exist locally. The difference of two splittings is a unique O_C-linear map M -> L². This action is free, transitive, additive and restriction-compatible. The construction uses only intrinsic ideals and module operations.

6. On a trivializing cover choose splittings s_i and set h_ij=s_j-s_i. Then h_ij+h_jk=h_ik. Replacing s_i by s_i+t_i adds the Čech coboundary t_j-t_i. Vanishing means the splittings can be adjusted to agree and glue, and inverse images in J₂ give a global *embedded ideal*. Conversely a global ideal yields a global splitting. Standard sheaf Ext gives Ext¹(M,L²)=H¹(Hom(M,L²)) because M is locally free. There is no nonabelian obstruction at this fixed embedded stage.

## Arbitrary adapted coordinate transformations

Locally choose generators x,y of I with q(x)=0 and q(y) a frame of L. Any other adapted generators, modulo I³, have the form
```
x' = α x + A x² + B xy + C y²,
y' = β x + δ y + D x² + E xy + F y²,
```
where α and δ restrict to units on C; coefficients may be ambient functions, including dependence on moving base coordinates. Terms from nilpotent variations of these coefficients are already included in their quadratic jets. In the quotient by `(x-a y²,I³)`, x=a y², y'=δ y + O(y²), and x'=(α a+C)y². Hence
```
a' = (α a+C)/δ²
```
with all coefficients restricted to C (and the appropriate local frames). For two choices a,b in the *same original frame*,
```
a' - b' = (α/δ²)(a-b).
```
This is exactly the transition for Hom(M,L²): x' has M-frame αx, y' has L-frame δy. The affine translation C/δ² may depend on the full quadratic neighborhood and base-coordinate movement; it cancels in differences. Arbitrary linear mixing β, all x²/xy terms, and quadratic corrections to y' do not change this result. No chosen retraction of the quadratic neighborhood is used. Equality is equality of ideals, not of preferred generators.

## Functoriality, base change and dependence

Isomorphisms of the data `(X,C,q)` carry `I,J₂,K` and (*) to their counterparts. Under flat ambient base change, the defining ideals, conormal quotient and (*) pull back to the corresponding geometric construction, and so does the Yoneda class. For nonflat ambient base change, the pullback of (*) as a module sequence on the new curve remains exact because `M` is locally free. Identifying that sequence with the new geometric extension still requires a compatible regular immersion and conormal quotient, with the relevant ideal, product and graded identifications commuting with pullback. When these identifications hold, the Yoneda class pulls back naturally. An isomorphism on cohomology under base change is a separate question.

The class is determined by the embedded quadratic neighborhood `O_X/I³` and `q`, since that truncation determines `J₂/K`. The associated graded algebra `Sym(E)` and the abstract ribbon can lose this information.

## Quartic consistency

For the specified relative rational quartic and distinguished quotient `L=O(-6), M=O(-8)`,
```
H = M^∨ ⊗ L² = O(-4).
```
On the two standard affine charts, H¹(O(-4)) has Laurent representatives u^-1,u^-2,u^-3. The earlier independently audited raw ambient calculation yields the transition defect `K(u)` and for the distinguished quotient `[-6u^-2]`. Each local kernel equation defines a splitting of (*), and their normalized differences give its Čech cocycle. The general theorem identifies this inherited cocycle with the Yoneda extension class. For the specified admissible quotients over Z_(2) and Z_2, the middle coefficient is 2 mod 4. [Full Čech reduction](../supplements/Z4_LIFTING_AND_DEFORMATION.md#full-cech-reduction), [coefficient verifiers and arithmetic scope](../supplements/Z4_LIFTING_AND_DEFORMATION.md#exact-computational-support-and-scope).

## Why the common comparison object matters

The statement that one can subtract arbitrary lifts of M *inside I/I³* as O_C-linear maps is not justified: I/I³ has no canonical O_C-module structure. Also the expression I²/(I³+IJ) is circular unless J is fixed and it does not by itself define a common comparison object for varying J. The common object is instead **J₂/(I J₂+I³)**. It is annihilated by I, so the difference construction and its additive law are literal O_C-module statements. The original numerical calculation survives; the original general proof contains the gap described above.

## Independent audit and arithmetic provenance

The October 21 independent reviewer gave **verdict B** after replacing
the difference-of-lifts argument by (*). The audit read the original
proposal, the literature report and the five October 20 lifting
reports. It reconstructed the general fixed-ambient, fixed-quotient
torsor, descent and coordinate invariance by ideal and module operations.
It inherited the Laurent coefficient, sign conventions and mod-four
reduction from the earlier quartic audits. Those calculations have the
arithmetic scope stated above. The audit’s handoff permits using the
corrected class with the fixed-quotient and base-change hypotheses.
Identification with a divided-Frobenius operation remains open.
[Original independent audit](https://github.com/markluxton1/STCI/blob/a5ed68f7f11d3b51e5e972a9a4b90e0a3bd7ce5b/research/notes/2026-10-21-intrinsic-ribbon-triple-independent-audit.md).

## A coordinate change as an explicit control

The complete quadratic transition, including movement of the base coordinate, yields for the distinguished relative-quartic quotient the contributions K_A=18u^-2, K_B=-12u^-2, K_move=-12u^-2, and total K=-6u^-2. Under A'=A+B, B'=B the first contributions become K_A'=18u^-2+9u^-1 and K_B'=-12u^-2-9u^-1; the base term stays unchanged. Only the total represents the intrinsic class. These are the inherited exact chart calculations from [the arithmetic lifting proof](../supplements/Z4_LIFTING_AND_DEFORMATION.md), with the failure of individual-summand invariance isolated in [the coordinate control](arithmetic_root_collision.md#a-coordinate-summand-really-changes). The corrected extension proof explains the invariance; it does not independently recompute these Laurent coefficients.

## Relation to arithmetic operations

No identification of this Yoneda class with a divided-Frobenius or cotangent-complex operation has been established. Such a comparison requires a morphism of the relevant embedded deformation complexes and proof that it takes the actual extension class to the proposed operation. The existence of a formal arithmetic operation alone does not establish a nonzero geometric obstruction.

## Primitive triples on smooth rational quartics

This result is independent of, and stronger in the formal-neighborhood
direction than, the already known exclusion of cubic carriers for \(C_0\): it
excludes every embedded primitive triple of the type forced by a \((3,4)\)
complete intersection, whether or not that triple is generated by global
equations of degrees three and four.

First, any \((3,4)\) complete intersection \(X\) supported on a smooth rational
quartic would be primitive everywhere.  At a point of the curve, complete the
ambient local ring as

\[
k[[t,x,y]],\qquad I_C=(x,y).
\]

The quotient by the two equations is finite over \(k[[t]]\), is a
one-dimensional Cohen--Macaulay ring with a unique associated prime, and is
therefore torsion-free and finite free over the DVR.  Its rank is
\(3\cdot4/4=3\).  Every transverse fiber is consequently a length-three Artin
complete intersection and hence Gorenstein.  Such a local algebra cannot have
embedding dimension two: then its Hilbert function would be \((1,2)\), its
square of the maximal ideal would vanish, and its socle would have dimension
two.  It is therefore \(k[\epsilon]/(\epsilon^3)\).  A local linear combination
\(H\) of the two equations has nonzero normal differential.  The surface
\(S=(H=0)\) is regular, and \(C\) is the Cartier divisor \((v=0)\) in the
two-dimensional regular local UFD \(\mathcal O_{S,p}\).  The other local
generator \(K\) has radical \((v)\), so unique factorization gives
\(K=\text{unit}\cdot v^n\).  The transverse length is three, hence \(n=3\),
and after changing coordinates

\[
 I_X=(u,v^3)
\]

inside that smooth surface.  Thus the triple is primitive at every point, with
no finite exceptional defects.

If \(L\) is its type line bundle, then

\[
\operatorname{gr}\mathcal O_X
=\mathcal O_C\oplus L\oplus L^2.
\]

Complete-intersection adjunction gives

\[
\omega_X|_C=\mathcal O_C(3)=\mathcal O_{\mathbf P^1}(12),
\]

while the primitive-triple formula gives
\(\omega_C\otimes L^{-2}\).  Thus

\[
 \mathcal O_{\mathbf P^1}(12)
 =\mathcal O_{\mathbf P^1}(-2)\otimes L^{-2}.
\]

Since \(\operatorname{Pic}(\mathbf P^1)\simeq\mathbf Z\) has no two-torsion,
\(L=\mathcal O(-7)\).  In characteristic zero every smooth rational quartic
has \(N_C^*=\mathcal O(-7)^2\), by the normal-bundle theorem of
Eisenbud--Van de Ven, so quotients to \(L\) exist and first-order data alone
do not obstruct the triple.

For \(C_0\), make the calculation intrinsic to the two standard embedded
charts.  On \(x_0\ne0\), put \(z=x_1/x_0\) and

\[
 a=x_2/x_0-z^3,\qquad b=x_3/x_0-z^4.
\]

On \(x_3\ne0\), put \(w=x_2/x_3\) and

\[
 a'=x_1/x_3-w^3,\qquad b'=x_0/x_3-w^4.
\]

On the overlap the exact coordinate changes include

\[
 w=\frac{z^3+a}{z^4+b},\qquad
 a'=\frac{z}{z^4+b}-w^3,\qquad
 b'=\frac1{z^4+b}-w^4.
\]

Choose the split conormal frames

\[
 u=b-\frac32za,\quad v=a,\qquad
 u'=\frac12a',\quad v'=-3wa'+2b'.
\]

Direct expansion of the exact changes through order two gives

\[
\begin{aligned}
u'={}&z^{-7}u-\frac52z^{-11}u^2-3z^{-10}uv-\frac38z^{-9}v^2,\\
v'={}&z^{-7}v+3z^{-12}u^2-z^{-11}uv-\frac94z^{-10}v^2
\end{aligned}
\pmod{I_C^3}.
\]

Every quotient \(N_C^*\twoheadrightarrow\mathcal O(-7)\) is parametrized by
a kernel line in \(\mathbf P^1\).  For the finite chart take
\(m=u+\theta v\), \(\ell=v\); the corresponding Ferrand double has ideal
\((m,\ell^2)\).  The embedded extension theorem proved above (also the Bănică--Forster criterion in this setting) says it extends to a primitive
triple exactly when

\[
0\longrightarrow L^2\longrightarrow
J_2/(I J_2+I^3)\longrightarrow M\longrightarrow0
\]

splits.  The Čech class of this extension is

\[
h_\theta=3\left(
\theta^3z^{-5}-\frac12\theta^2z^{-4}
+\frac14\theta z^{-3}-\frac18z^{-2}
\right)
\in H^1(\mathcal O(-7)).
\]

In the standard basis \(z^{-1},\ldots,z^{-6}\), its \(z^{-2}\) coefficient
is \(-3/8\), so it is nonzero for every finite \(\theta\) in characteristic
zero.  The missing kernel line, represented by \(m=v,\ell=u\), has class
\(3z^{-5}\ne0\).  These cases exhaust the quotient projective line.  Hence no
Ferrand double extends to a primitive triple of type \(\mathcal O(-7)\), and
there can be no \((3,4)\) complete intersection supported on \(C_0\).

The class is intrinsic in \(\operatorname{Ext}^1(M,L^2)\): changes of local
lifts add a Čech coboundary, frame changes act on the parameter projective
line, and changes of parameter transport cohomology.  Its overall factor of
three explains, at the level of the second formal neighborhood, why the
obstruction disappears in characteristic three, where P-008 supplies an actual
primitive \((3,4)\) complete intersection.

The obstruction in fact never vanishes for *any* characteristic-zero smooth
rational quartic.  By the [smooth-quadric graph description](../synthesis/01-problem-and-curve.md), the curve is the graph, on
\(Q\simeq\mathbf P^1\times\mathbf P^1\), of a separable degree-three map
\(f:\mathbf P^1\to\mathbf P^1\).  Pre- and postcomposition by
\(\operatorname{PGL}_2\) come from automorphisms of the Segre quadric and do
not change the existence of a primitive triple.  Riemann--Hurwitz gives total
ramification four.  If there is no simple ramification, there are exactly two
totally ramified points and the map is equivalent to \(z^3\), the case just
computed.  Otherwise choose two simple ramification points.  Their branch
values are distinct, and source and target normalizations put the map in the
marked form

\[
 f_\lambda(z)=\frac{z^2(z-1)}{z-\lambda},\qquad \lambda\ne0,1.
\]

This parameter is a surjective marked cover of the remaining left--right
orbits; it is not asserted to be a unique coarse-moduli coordinate.

For this graph, explicit split conormal frames again identify
\(N_C^*=\mathcal O(-7)^2\).  Use the Čech cover

\[
 U=\mathbf P^1\setminus\{\infty,\lambda\},\qquad
 V=\mathbf P^1\setminus\{0,1\}.
\]

Reducing the exact quadratic chart transition by subtracting the principal
parts at \(\lambda\) and \(1\) gives the Bănică--Forster class in the standard
basis of \(H^1(\mathcal O(-7))\).  For a quotient point \([A:B]\in\mathbf
P^1\), multiply its six coordinates by the common unit
\(4\lambda^4(\lambda-1)^2\).  Four of the resulting homogeneous cubics are

\[
\begin{aligned}
G_1={}&(A\lambda+B)\bigl((5\lambda^3-3\lambda^2)A^2
 +(6\lambda^2-2\lambda)AB+(3\lambda-1)B^2\bigr),\\
G_2={}&\lambda(A\lambda+B)\bigl((3\lambda^3-\lambda^2)A^2
 +4\lambda^2AB+(3\lambda-1)B^2\bigr),\\
G_5={}&\lambda^4(A+B)\bigl((3\lambda-1)A^2
 +4\lambda AB+(3\lambda-1)B^2\bigr),\\
G_6={}&\lambda^4(A+B)\bigl((3\lambda-1)A^2
 +2(3\lambda-1)AB+(5\lambda-3)B^2\bigr).
\end{aligned}
\]

On \(A=1\), write \(T=B\), and divide \(G_2\) by \(\lambda\) and
\(G_5,G_6\) by \(\lambda^4\).  Exact subtraction gives

\[
 G_1-G_2/\lambda=2\lambda(\lambda-1)(\lambda+T)^2,
\]

and

\[
 G_5/\lambda^4-G_6/\lambda^4
 =-2T(\lambda-1)(T+1)^2.
\]

If all six obstruction coordinates vanished, the first identity would force
\(T=-\lambda\); the second difference would then be
\(2\lambda(\lambda-1)^3\ne0\), a contradiction.  At the missing point
\(A=0\), a direct calculation gives, up to the same unit,

\[
 (G_1,\ldots,G_6)=
 (3\lambda-1,\lambda(3\lambda-1),\lambda^2(3\lambda-1),
 \lambda^3(3\lambda-1),\lambda^4(3\lambda-1),
 \lambda^4(5\lambda-3)).
\]

Simultaneous vanishing would require both \(3\lambda-1=0\) and
\(5\lambda-3=0\), impossible in characteristic zero.  Hence the obstruction
has no zero on any quotient line for any degree-three map, proving P-010 for
all smooth rational quartics.  The marked-transition reduction, including the
discard of a \(z^{-7}\) Čech coboundary, is checked exactly in
[the exact marked-transition verifier](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_all_quartic_primitive_obstruction.py).


## Characteristic reach of the two mechanisms

The filtered-Koszul coprime theorem and the corrected embedded extension 0→L²→J₂/(IJ₂+I³)→M→0 require no division by an integer, so their stated regular-immersion/line-quotient constructions apply in every characteristic, including relative mixed characteristic. Their obstruction classes need not remain nonzero after specialization. In the fixed-quartic P010 calculation the balanced frames use 1/2 and the final obstruction has a factor 3: the fixed-C0 displayed nonvanishing proof also applies for every p>3 (only powers of2 are inverted and3 stays nonzero), disappears at3, and cannot simply be read in characteristic2, where the conormal splits differently. The explicit characteristic3 primitive presentation in [positive-characteristic constructions](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md) is the control. The higher-initial example itself works in characteristic2 and shows why cancellation, rather than two selected symbols, is essential. These local/embedded mechanisms are compatible with [the every-positive-characteristic quartic-carrier construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) for the fixed C0.

### The fixed-quartic primitive-triple boundary in characteristic2

The invalidity of the balanced coordinate formulas at2 does not leave this particular type undecided. R0020 gives N_C0^*=O(-8)⊕O(-6). There is no surjection to O(-7): a homomorphism from O(-6) vanishes because H0(O(-1))=0, while every homomorphism O(-8)→O(-7) is a section of O(1) and vanishes somewhere. Thus no embedded primitive triple of typeO(-7) exists on fixedC0 in characteristic2 already at the conormal quotient stage. The length-three lci/adjunction argument above works in every characteristic and would force this type for a supported(3,4) pair, so that pair is excluded in characteristic2. Together with the displayed nonzero P010 class for p>3 and the characteristic-zero calculation, the fixed-C0(3,4) obstruction has exactly characteristic3 as its positive-characteristic escape; there the explicit primitive presentation exists. This is an independently reconstructed source-level extension. No assertion about every smooth rational quartic in characteristic2 follows from the fixedC0 splitting alone.
