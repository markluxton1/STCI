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
