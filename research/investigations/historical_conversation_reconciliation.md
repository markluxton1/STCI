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
| Two-stage normal/endpoint initial filtrations | Does the noncommutation of normal-order and endpoint-valuative initials yield an intrinsic lemma or obstruction beyond the existing filtered-Koszul, source-image, and vertical-order-jump results? | Compare an exact formulation and counterexample with [global equation jets](../arguments/equations/global_equation_jets.md) and [mixed-degree poles](../arguments/carriers/mixed_degree_normal_forms_and_poles.md); retain only a demonstrably stronger statement. |\n| Early cubic contact ranks | Do the old cubic rank-14 calculation, special reducible \(Lq\) rank drops, or characteristic-three behavior establish any independent geometric statement not subsumed by the current cubic carrier exclusion? | Retain only a verified, reusable geometric mechanism or example; otherwise discard. |
| Fixed-quadric residual degeneration | Is there a *specific*, correct flat-family construction of a \((2,4)\) CI with limit \(C\cup Z\), \(Z\sim(3,1)\), which adds useful information to the current residual-absorption framework? | Compare exact equations and flatness with canonical residual framework. Retain only if new and consequential. |
| Old primitive-conormal/pole stratification | Does any verified calculation survive the arbitrary-mate quartic-carrier theorem as a useful general method for higher-degree carriers? | Identify an explicit independent lemma and applicable higher-degree hypotheses; otherwise discard. |
| Quintic conductor descent | Is there an older quintic-specific construction beyond the expanded normalization, conductor, full-inverse-support and descent arguments? | No new result yet identified; compare only an explicit candidate. |

## Resolved comparison: cuspidal cubic conductor mechanism

The August 21 historical source computes the non-torsion additive conductor defect \\(-3z^{-2}\\) for the cuspidal cubic cone \\(y^3-x^2z=0\\), despite proportionality on normalization. This **is already preserved** in [projection pairings and conductor failures](../frameworks/carrier-normalization/projection_pairings_and_conductor_failures.md), which also distinguishes the ruled-cubic failure on the normalization. **Discard the historical duplicate.** This is a cubic mechanism, not evidence of an unresolved quintic descent case.

The August 22 primitive/quasiprimitive \\((4,5)\\) artifacts (\\(p_1=8,9\\), conditional \\(p_2\\) bounds) were also recovered. They are necessary filters for a degree pair now excluded by R-0001, not an independent higher-degree obstruction. **Do not retain as a new Result** unless a specific generalization beyond quartic carriers is verified.

## Further duplicates screened out

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
