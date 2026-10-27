# 6. The surviving frontier: geometric questions and next theorems

The unrestricted characteristic-zero question for the fixed rational quartic \(C_0\subset\mathbf P^3\) remains **open**. The completed quartic-carrier exclusion [STCI-R-0001](../results/quartic_carrier_exclusion.md) forces both defining degrees to be at least five; it does not settle higher-degree pairs.

This chapter collects **candidate mathematical deliverables**, not a current priority ranking. The [canonical frontier](../FRONTIER.md) currently emphasizes general proper intersections, residual cycles, full initial ideals, and their global realization; the older jet, root, and carrier tasks below remain available alternatives. The ordering of sections is expository, not a research directive.

## 6.1 Jet-condition dependence

**Problem.** For a chain of primitive or quasiprimitive structures
\[
C=C_1\subset C_2\subset\cdots\subset C_m,
\]
when are the successive conditions imposed on ambient hypersurfaces dependent? Why does the naive count of independent jet conditions sometimes fail?

**Established inputs.** The [jet-geometry lemmas](../results/jet_geometry.md) identify a comparison divisor between the primitive conormal direction and the conormal direction of the unique quadric. Earlier [order-one](../results/order_one.md), [primitive e=2](../results/quartic_e2.md), local-cohomology, and MF6 calculations give controlled test cases. The historical quartic-mate cases are closed, but their *jet mechanisms* are not thereby erased.

**Next mathematical deliverable.** On the unique quadric \(Q\), write the first two or three containment maps intrinsically, identify the comparison divisor, and prove an exact rank formula (or a finite geometric incidence criterion) for failure of independence. Separate the part that holds for any smooth rational quartic from the part depending on this embedding.

**What would count as progress?** A proved geometric criterion predicting a rank defect before running elimination, and an audited example where it recovers a known exceptional locus.

**What would not count?** Another unexplained list of polynomial equations, or reclassifying an already excluded quartic mate case.

## 6.2 Entirely-thick and excess-contact problem

**Problem.** When both original equations have generic normal orders \(r,s\ge2\), their first symbols can hide arbitrarily high intersection multiplicity. Which *finite* geometric data control that excess in the global STCI setting?

**Established inputs.** [Entirely-thick restrictions](../results/entirely_thick.md) give
\[
de\ge4rs,\qquad 7de+28rs\ge16(ds+er),\qquad d\ge3r,\quad e\ge3s.
\]
The first-symbol analysis in [Chapter 2](02-two-surfaces.md) describes common directions but does not compute the excess.

**Next mathematical deliverable.** Define a valuation- or successive-transform invariant of the pair \((F,G)\) that is invariant under changes of generators, and prove a formula relating it to generic intersection length \(de/4\) and the horizontal exceptional common-direction scheme. Start with the equality/near-equality boundary, where the numerical restrictions force special root behavior.

**Potential obstruction target.** Show that a specified nontrivial family of excess-contact patterns necessarily creates an extra projective intersection curve or forbidden inverse support on a carrier normalization.

**Critical caveat.** There is no justified *uniform* bound on transverse contact from the first symbols alone. A finite invariant must genuinely incorporate higher terms or valuations.

## 6.3 Bridge the actual equations to root schemes without discarding degenerations

**Problem.** How does a common factor of generic normal forms become a global saturated first relation? What happens when its extension fails at finitely many points of \(C\)?

**Established inputs.** [STCI-R-0008](../results/spectral_root_picard_criterion.md) treats fiberwise coprime graded second relations on the full root scheme. [STCI-R-0006](../results/actual_ci_smooth_root_bridge.md) reaches actual complete intersections only with saturated everywhere-generated first relation, full coprime generic initial ideal, gap at least two, and smooth full root. [STCI-R-0009](../results/moving_purepower_boundary.md) forces a degeneration divisor for moving pure powers.

**Next mathematical deliverable.** Formulate an exact **defect sheaf or divisor** for failure of saturation and joint generation, and prove a comparison between:
- the generic common-direction scheme of \(F,G\);
- the saturated first-relation root scheme;
- the special-point degeneration of the second quotient relation;
- the full generic initial ideal after cancellations.

**What would count as progress?** A theorem with a precise defect term, including singular or nonreduced fibers, which reduces to STCI-R-0006 when all defects vanish. It need not exclude an STCI immediately.

**What would not count?** Treating the first two displayed normal symbols as the full initial ideal, or silently replacing a nonreduced root by its reduction.

## 6.4 Compute the quadratic-root obstruction locus

**Problem.** Determine whether the first-compatible quadratic movement-two roots that also satisfy the spectral torsion condition can survive the complete second ambient obstruction.

**Established inputs.** [STCI-R-0007](../results/quadratic_root_obstruction_model.md) supplies sixteen first equations, twenty-five second pairings, and a smoothness discriminant. A particular smooth torsion-two seed and its four-dimensional first-compatible component are obstructed at second order, but other components have not been excluded.

**Next mathematical deliverable.** Compute the **full second zero scheme**, its components and saturation by the relevant discriminant, then intersect with the full spectral torsion condition. Record the defining ideal, exact computational certificate, and independent verification.

**Scope.** Even an empty smooth torsion intersection would be a result about this root family. Any implication for actual STCI equations still requires the bridge hypotheses of STCI-R-0006. Do not equate a finite-stage computation with unrestricted nonexistence.

## 6.5 Test the surviving higher-degree carrier models

**Problem.** Do any of the three Cartier singleton normalization models for \(C_0\) admit an actual finite birational projection into \(\mathbf P^3\) with full singleton inverse support and a mate?

**Established inputs.** [STCI-R-0002](../results/cartier_singleton_lift.md) leaves the degree-eight smooth quadric, degree-eight quadric cone, and degree-sixteen plane normalizations under its restricted hypotheses. [STCI-R-0003](../results/fixed_carrier_conductor_criterion.md) gives fixed-carrier conductor descent; [STCI-R-0004](../results/projection_phase_reduction.md) gives the phase/torsion-coset reduction for admissible families.

**Next mathematical deliverable.** For **one** model, compute in order:
1. the admissible four-section projection locus with the fixed \(C_0\) restriction;
2. the entire inverse image of \(C_0\), including isolated points;
3. the full conductor algebra and phase map, retaining nilpotents;
4. the actual torsion-coset intersection.

A failed projection or an unavoidable extra inverse point is already a useful geometric exclusion; there is no need to calculate phase torsion if admissibility fails.

**Scope.** Excluding all three models would close the **Cartier singleton degree-one inverse-lift** branch only. It would not classify non-Cartier, multiple-branch, or higher-degree inverse lifts.

## 6.6 What would connect the two main approaches?

The common-normal-factor program and the carrier-conductor program both arise from an actual pair \((F,G)\), but they retain different information. The following is a **proposed comparison problem**, not an established theorem.

Fix an integral carrier \(X=V(F)\) with normalization \(\nu:S\to X\). Can the horizontal common-direction cycle on \(\operatorname{Bl}_C\mathbf P^3\), together with its valuation data, determine any part of the inverse-support divisor \((\nu^{-1}C)_{\mathrm{red}}\) or its conductor gluing defect?

A productive first case would be a carrier with one generically degree-one inverse branch, allowing singularities or non-Cartier behavior at finitely many points. One should seek a **precise morphism or correspondence of local models** before claiming a global equality of obstruction classes.

The possible payoff is conceptual: a special-point defect visible in normal-form geometry might force failure of global descent, or conversely a conductor defect might impose a concrete degeneration of the second graded relation. Neither implication has yet been established.

## 6.7 Decision rules for new work

| If a proposed argument produces… | Record it as… | Before using it globally… |
| --- | --- | --- |
| A numerical inequality | Necessary condition | Check sharpness and whether high-order contact evades it |
| A common initial factor | Generic exceptional direction | Check saturation, special fibers, and the full initial ideal |
| A graded Picard obstruction | Graded-family obstruction | Check whether actual-CI bridge hypotheses hold |
| A finite-order lifting obstruction | Restricted ambient obstruction | Identify the relevant actual equation/root family |
| A normalization model | Necessary carrier geometry | Check actual projection, full inverse support, and conductor |
| A torsion-coset reduction | Structured finite-type problem | Compute admissible phase image and surviving torsion |
| A case exclusion | Conditional or scoped theorem | Audit quantifiers, missing strata, and factor reduction |

## 6.8 Selecting the next problem

The [current frontier](../FRONTIER.md) takes precedence over the ordering of this chapter. In particular, general proper intersections may have a residual cycle, and the STCI multiplicity formula applies only when that residual cycle vanishes. A generator-independent comparison of the full normal initial ideal, special-point defects, and actual residual support is an active **research question**, not a theorem; see [residual intersections and jets](residual_intersections_and_jets.md) and [normal-filtration defects](normal_filtration_boundary_obstructions.md).

The jet-dependence, root-obstruction, and Cartier-projection problems in Sections 6.1–6.6 remain bounded alternative projects. Choose them by mathematical leverage and check whether later scoped results already settle the proposed subcase. Promote claims only under the [authority policy](../AUTHORITY.md), with exact hypotheses and independent audit.

