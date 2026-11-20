# Conversation-to-repository mathematical gap audit

**Purpose:** recover substantive mathematics from prior discussions that is absent from the canonical repository. This is a **temporary triage file**, not a history of conversations, proof archive, new framework, or competing investigation queue.

**Repository baseline:** main at `928053ea99b209fd02faa4b89a0d37ef3f11b02d` (2026-11-19). Recheck current main before acting: canonical content changes rapidly.

## Retention rule

- If a claim and its useful proof/construction are already preserved, **drop it from this audit**.
- Retain a second viewpoint only when it yields a materially different proof, stronger generality, counterexample, useful construction, or a consequential bridge between existing frameworks.
- For an apparently missing claim, verify hypotheses, proof, precedence and consequences before placing it in the canonical Result/Argument/Framework/Investigation.
- Discard false, superseded, low-value and purely chronological material. Do not copy chats into the repo.

## Open mathematical comparisons

| Candidate | Concrete question | Closure criterion |
|---|---|---|
| Early cubic contact ranks | Do the old cubic rank-14 calculation, special reducible \(Lq\) rank drops, or characteristic-three behavior establish any independent geometric statement not subsumed by the current cubic carrier exclusion? | Retain only a verified, reusable geometric mechanism or example; otherwise discard. |
| Fixed-quadric residual degeneration | Is there a *specific*, correct flat-family construction of a \((2,4)\) CI with limit \(C\cup Z\), \(Z\sim(3,1)\), which adds useful information to the current residual-absorption framework? | Compare exact equations and flatness with canonical residual framework. Retain only if new and consequential. |
| Old primitive-conormal/pole stratification | Does any verified calculation survive the arbitrary-mate quartic-carrier theorem as a useful general method for higher-degree carriers? | Identify an explicit independent lemma and applicable higher-degree hypotheses; otherwise discard. |
| Quintic conductor descent | Is there an older quintic-specific construction beyond the expanded normalization, conductor, full-inverse-support and descent arguments? | No new result yet identified; compare only an explicit candidate. |

## Resolved comparison: cuspidal cubic conductor mechanism

The August 21 historical source computes the non-torsion additive conductor defect \\(-3z^{-2}\\) for the cuspidal cubic cone \\(y^3-x^2z=0\\), despite proportionality on normalization. This **is already preserved** in [projection pairings and conductor failures](../frameworks/carrier-normalization/projection_pairings_and_conductor_failures.md), which also distinguishes the ruled-cubic failure on the normalization. **Discard the historical duplicate.** This is a cubic mechanism, not evidence of an unresolved quintic descent case.

The August 22 primitive/quasiprimitive \\((4,5)\\) artifacts (\\(p_1=8,9\\), conditional \\(p_2\\) bounds) were also recovered. They are necessary filters for a degree pair now excluded by R-0001, not an independent higher-degree obstruction. **Do not retain as a new Result** unless a specific generalization beyond quartic carriers is verified.

## Promoted open question

- The higher-degree analogue of the quartic K3 exceptional-rank budget was **not explicitly formulated** as a unified research question. It is now recorded, without claiming a universal conservation identity, in [carrier degree exclusions](../frameworks/carrier-normalization/degree_exclusions.md#open-question-higher-degree-surface-singularity-budgets). This is a substantive question rather than a missing proved result; the quintic–octic ADE/even-node budget is cited as an existing partial comparison.

## Newly recovered candidate: common-quadric Chow boundary

- A November 3 discussion studies a quartic pencil degenerating to \\(W_0=\\langle QA,QB\\rangle\\), with quadrics \\(A,B\\), and first-order deformations \\(F_t=QA+tF_1+\\cdots, G_t=QB+tG_1+\\cdots\\). The combination \\(BF_t-AG_t=tK+\\cdots\\), \\(K=BF_1-AG_1\\), gives a proposed limiting cycle \\([V(A,B)]+[V(Q,K)]\\) of degree \\(4+12=16\\). Since \\(F_1,G_1\\) vanish on \\(C\\), \\(K|_Q\\) contains \\(C\\), leaving residual divisor class \\((5,3)\\) on \\(Q\\). The source further identifies a Koszul quotient \\(H^0(Q,\\mathcal I_{Z/Q}(5,3))\\) for \\(Z=V_Q(A,B)\\), using the vanishing \\(H^1(Q,\\mathcal O_Q(1,-1))=0\\), and proposes an exceptional projective bundle of boundary cycles. **Status:** the scoped first-order cycle and Koszul residual-system calculation has now been recovered into [Chow bundle maps](../arguments/equations/chow_bundle_maps.md#common-quadric-boundary-of-the-quartic-pencil-chow-map-recovered-first-order-calculation), with properness assumptions and an explicit P^15 dimension check. The full exceptional-fibre/blowup identification and higher-order arcs remain open; no unrestricted STCI implication. Compare [torus Hilbert boundary](../arguments/torus_hilbert_boundary.md), [Chow bundle maps](../arguments/equations/chow_bundle_maps.md), and [residual geometry](../frameworks/residual-construction/residual_geometry.md). Avoid conflating this quartic–quartic common-factor degeneration with the unrelated proposed \\((2,4)\\) flat family.

## Additional source comparisons

- **November 3 relative common-quadric boundary:** the source also contains a projective bundle over the regular-sequence locus and a key warning about rank-jumping when the two restricted quadrics acquire a common divisor. Both have now been preserved with the first-order calculation in [Chow bundle maps](../arguments/equations/chow_bundle_maps.md#relative-boundary-family-and-the-rank-jump-caveat). The closure of that bundle, specialized multiplication images, and higher-order arcs remain a genuine geometric question, not a claimed result.
- **November 5 universal translate incidence:** the historical \\(T/T_C\\) quotient, horizontal/vertical incidence, finite embedded translate schemes, and the positive-characteristic coalescence model are now substantially covered by [embedded torus quotients](../frameworks/embedded-torus-quotients/index.md), [constant quotient equation criterion](../results/constant_quotient_equation_criterion.md), and [Chow polytope rigidity](../arguments/equations/chow_polytope_rigidity.md). No separate reconstruction is warranted without a sharper new implication.


- **Historical cubic rank-drop heuristic:** [equation-pair rank and weights](../arguments/torus/equation_pair_rank_and_weights.md) already treats common-factor rank drop in arbitrary degrees and distinguishes degreewise rank loss from flatness and supported limits. The recovered bare rank-14 numerical claim has not been linked to an independent invariant statement. Do not promote it without an exact rank map and geometric interpretation.
- **Unbounded endpoint poles despite flat transverse length:** the historical local family \\(F=t^\\alpha u+v^n,\\ G=u\\) defines the flat algebra \\(k[[t,v]]/(v^n)\\) while its displayed first-normal ratio has pole order \\(\\alpha\\). This is a valid caution about non-invariant generator ratios, not a pole bound; existing [mixed-degree poles](../arguments/carriers/mixed_degree_normal_forms_and_poles.md) and [weighted initials](../arguments/normal-geometry/normal_boundary_weighted_initials.md) explicitly separate actual generator changes, principal parts, and flatness. No new result.
- **Fixed-quadric \\((2,4)\\) degeneration:** [explicit quartic residuals](../arguments/residuals/explicit_quartic_residuals.md) provides other reduced residual intersections but not a verified family realizing the historical proposed \\(C+(3,1)\\) split. The divisor-class equality \\((1,3)+(3,1)=(4,4)\\) makes a \\((2,4)\\) CI divisor on \\(Q\\) numerically possible, but does not establish flatness of a particular family. Keep conditional until equations and fibers are recovered.

## Further duplicates screened out

- **Two-stage normal/endpoint valuations:** [endpoint valuation fans and cancellation](../arguments/torus/endpoint_valuations.md) already distinguishes the generic normal valuation, endpoint valuation on the function field of C, and ambient flag valuations; computes the weighted wall and the lexicographic flag value \\((1,9)\\) in the quartic-binomial model; and explains why residue polynomials are needed beyond tropical weights. Together with [actual equation filtrations](../arguments/normal-geometry/actual_equation_filtration.md), this **closes the earlier apparent gap**. Do not create a second formulation without a stronger precise theorem.
- **K3 singularity-budget/conservation observation:** the October 23 prompt asks whether the exceptional rank \\(24-r\\) is a general conservation law. The established characteristic-zero quartic-pair result already contains the rank formula, local \\(A_3\\)/defect singularities and Picard-rank contradiction in [R-0022](../results/quartic_44_filtered_exclusion.md), with geometric comparison in [multiplicity and genus budgets](../arguments/normal-geometry/extracted_intrinsic_44_multiplicity_and_genus_budgets.md). Generalizing it to arbitrary degree is a question, not a missing established theorem. No new file.


- The affine-versus-projective STCI and homogenization/closure distinction is already treated in [extracted affine/projective and literature limits](../arguments/equations/extracted_affine_projective_and_literature_limits.md). The cone-vertex lci obstruction is explicit. No new standalone result.
- The proposed higher-degree exceptional-ruling heuristic is not itself a theorem. Existing carrier arguments already treat exceptional ruling and residual contact under specified hypotheses; retain only if a new general statement with proof emerges.

## Already covered — do not re-audit without new evidence

- Full Chow-polytope rigidity and its set-theoretic translate locus: [R-0074](../results/chow_polytope_rigidity.md) and [proof](../arguments/equations/chow_polytope_rigidity.md).
- General-coordinate tropical boundary, sixteen generic punctures, resultant edge loci and toric model: [argument](../arguments/torus/general_coordinate_boundary.md).
- Enriched boundary reconstruction and its finite-order limitations: [argument](../arguments/torus/boundary_reconstruction_and_defects.md).
- Fixed quartic and normal-carrier exclusions: [R-0001](../results/quartic_carrier_exclusion.md).
- Entirely-thick inequalities and the \((3,4)\) equality case: [result](../results/entirely_thick.md).
- Supported Hilbert limits, torus quotients and the distinction between cycles and actual equation realization: existing torus boundary framework and arguments.

## Audit outcome to date

**No verified missing theorem or construction yet.** One historical conductor example and the old (4,5) filters have been screened out as already preserved or superseded. The items above are questions for targeted comparison, not proposed research projects. Do not generate a historical summary for a closed item. Once all items are resolved, integrate any retained mathematics into its canonical home and **delete this temporary file**.

## November 18 coregularity comparison recovered

A literature handoff distinguishes Hartshorne–Polini's exact homogeneous coregularity criterion from the project's finite conormal and actual-equation filtration tests. The theorem and individually-coregular counterexample were already represented in [literature](../literature/README.md) and [global equations](../arguments/equations/global_equations_and_constructions.md), but the proposed **bridge question** was not formulated precisely. It is now recorded in [global equation realization](../frameworks/global-equation-realization/index.md#open-interface-simultaneous-coregularity-versus-actual-equation-filtrations): for \(fM=M\), can the geometric filtration detect \(K_f/gK_f\ne0\)? This is an open comparison, not a proved theorem, and cannot be inferred from missing sextic symbols alone.

## Earlier normalization/conductor proposal screened

An October degree-independent divisor/conductor proposal suggested combining fractional inverse-curve classes (heuristic \(c^2=16/d\)) with power descent through the conductor. Its principal mechanisms are already owned by [carrier descent](../frameworks/carrier-normalization/carrier_descent.md), the [normalization index and power-descent account](../arguments/carriers/normalization_indices_and_power_descent.md), and the [fixed-carrier criterion](../results/fixed_carrier_conductor_criterion.md). In particular, the rational self-intersection identity is conditional on the normal/\(\mathbf Q\)-Cartier setup, and class-group index and conductor power descent are separate invariants. **Disposition:** covered, not a new universal obstruction. No additional framework or theorem warranted.

## Toric group-scheme handoff screened

The toric handoff describes the two inversion-conjugate quartic carriers, the transverse character \(z^N-1\), the \(\mu_4\) collision in characteristic two, and the semigroup \(\langle3,4\rangle\) governing the displayed binomial descent. These are substantially present in [quartic mu4 degeneration](../results/quartic_mu4_degeneration.md), [toric torsion and endpoint contacts](../arguments/torus/toric_torsion_and_endpoint_contacts.md), and [positive characteristic constructions](../arguments/arithmetic/positive_characteristic_constructions.md). The handoff also notes \(\operatorname{Aut}_{\mathbf P^3}(C)\cong\mathbf G_m\rtimes C_2\) in characteristic zero and the 14-dimensional projective orbit; these are elementary consequences of the omitted middle monomial and are not, by themselves, an independent STCI obstruction. **Disposition:** no new result or framework; preserve the distinction between the torus-level character equation and its projective descent and boundary support.
