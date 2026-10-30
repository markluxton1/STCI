# 6. The surviving frontier: geometric questions and next theorems

The unrestricted characteristic-zero question for the fixed rational quartic \(C_0\subset\mathbf P^3\) remains **open**. The completed quartic-carrier exclusion [STCI-R-0001](../results/quartic_carrier_exclusion.md) forces both defining degrees to be at least five; it does not settle higher-degree pairs.

This chapter collects **candidate mathematical deliverables**, not a current priority ranking. The [canonical frontier](../FRONTIER.md) currently emphasizes general proper intersections, residual cycles, full initial ideals, and their global realization; the older jet, root, and carrier tasks below remain available alternatives. The ordering of sections is expository, not a research directive.

## 6.1 Jet-condition dependence

**Problem.** For a chain of primitive or quasiprimitive structures
\[
C=C_1\subset C_2\subset\cdots\subset C_m,
\]
when are the successive conditions imposed on ambient hypersurfaces dependent? Why does the naive count of independent jet conditions sometimes fail?

**Established inputs.** The [order-one result](../results/order_one.md) now records the rank-defect definitions and first finite evaluation maps; the [jet-geometry lemmas](../results/jet_geometry.md) identify a comparison divisor between the primitive conormal direction and the conormal direction of the unique quadric. Earlier [order-one](../results/order_one.md), [primitive e=2](../results/quartic_e2.md), local-cohomology, and MF6 calculations give controlled test cases. The historical quartic-mate cases are closed, but their *jet mechanisms* are not thereby erased.

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


## 6.9 Residual-intersection deliverables

Two research routes remain distinct. First, extend the fixed-sextic jet-kernel theorem R-0025 to a geometrically defined family of carriers and mates, including the exceptional rank-drop strata. A uniform upper bound on generic multiplicity strictly below de/4 would imply positive residual degree via the projective cycle formula. One selected sextic does not establish such a uniform bound.

Second, extend the saturated residual zero-cycle formula R-0019 to a detector for a residual one-cycle in projective space. This requires an explicit bridge from auxiliary-surface intersections and horizontal exceptional data to the actual global equations; vertical exceptional cycles alone do not suffice. The explicit residual quartics of R-0023 and fixed-boundary deformation of R-0024 are useful laboratories, not general existence or nonexistence theorems.

A new case computation should identify an invariant class excluded, an exceptional stratum left unresolved, or a structural implication that fails. Otherwise it remains exploratory evidence, not a promoted result.

## 6.10 Formal-normal and valuation research targets

A next theorem should seek a coordinate-independent invariant of the full normal initial ideal, including integral specialization at exceptional points, and connect it to an actual projective residual cycle. Weighted valuations in a rational normal frame do not yet provide that implication; residue and cancellation data matter.

The exact ideal-power theorem gives complete global equation spaces in degrees d at least 3m. Their geometric singularity and jet-rank strata remain to be classified. The marked-trisecant negative calculation shows that ruling-contact conditions alone leave ambient transverse coefficients free. A successful obstruction needs a proved global compatibility condition rather than another isolated calculation.

## 6.11 Arithmetic specialization research target

The prescribed characteristic-two quartic complete intersection has a proved nonlifting obstruction over the two specified unramified mixed-characteristic bases. This does not exclude unrelated characteristic-zero equations. A meaningful extension would classify which invariants of a supported thickening persist under flat specialization, with the exact special embedded scheme and generic reduced support specified. The characteristic-dependent conormal extension, cancellation-generated initial equations, and arithmetic obstruction must be checked separately. See Chapter 3 and canonical results R-0012, R-0020, R-0021, and R-0031.

## 6.12 Global source and embedded lifting tests

The reviewed October 27 one-step source separates the extension class of a fixed embedded lower thickening from the actual homogeneous equations. A proposed next saturated layer must first satisfy its power-relation divisor inequality and the pushed-forward extension-class vanishing test; surjectivity of the extension map is a separate condition. At the final Gorenstein step the source requires the lower equation-module extension to split, with the socle divisor already fully allocated.

For a fixed lower thickening Y of generic length n, an actual proper degree-(a,b) pair with ab=(n+1)deg(C) has sole reduced support C exactly when its determinant in the rank-two torsion-free equation module vanishes. This converts the fixed-Y existence problem to a decomposable-kernel problem in the actual homogeneous source spaces, after removing improper pairs. The next theorem should classify the zero locus across a geometrically controlled family of lower embedded thickenings, including rank-drop strata, rather than assume generic source rank settles all cases. See Chapter 3 and the October 27 one-step boundary investigation.

## 6.13 Intrinsic contact, duality and conductor bridges

The marked flag, dual discriminant, ruled projection and arithmetic four-section results (R-0026 through R-0029) provide controlled models of endpoint contact, nonreduced fibers, embedded dual singularities, conductor gluing, and specialization. Their natural role is to formulate *invariant bridge questions*, not to add an unrestricted STCI exclusion.

One bridge asks whether the intrinsic horizontal common-direction scheme of two actual equations can be mapped to a marked contact or conormal flag in a way compatible with the full initial ideal at the endpoints. The finite-flat degree-six divisor-addition map and its nonreduced fibers show why replacing the flag by its reduced points would lose information. A second bridge asks whether endpoint contact imposes a conductor-descent obstruction on a specified normalized carrier; this requires the full conductor and actual pullback section, not only a divisor class on a smooth resolution.

The arithmetic ruled four-section warns that normalization, scheme image and specialization cannot be silently interchanged. A proposed theorem should state which operation is compatible with base change and prove the relevant comparison map. The embedded endpoint terms in the dual Jacobian and projected scroll/cone intersection are concrete tests for such a comparison.

A useful deliverable would be one intrinsic map with a proved compatibility or a counterexample identifying its failure. Repeating dual discriminant computations without a link to actual global equation spaces would not advance the STCI question.
