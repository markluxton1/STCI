# Context-efficient corpus inventory (structural baseline)

This is a **structural inventory, not a mathematical review or completed proof classification**. It is an agent entry point for the *existing* Results / Arguments / Frameworks / Investigations corpus. Its baseline is the head of `chatgpt/math-content-consolidation` (PR #136) when this inventory branch was created. Do not infer proof equivalence, independence, or correctness from metadata alone.

For a file-by-file index of catalog-linked mathematical sources, see [CORPUS_FILE_INDEX.md](CORPUS_FILE_INDEX.md), extended by [87 verified Framework-linked files](CORPUS_LINK_CANDIDATES.md). The canonical [516-path snapshot inventory](CORPUS_TREE_INVENTORY.md) supersedes these preliminary partial indexes.

## Authoritative routes

- [Research entry and six retrieval lanes](INDEX.md)
- [Generated complete record catalog](CATALOG.md) — do not edit directly
- [Result topic and legacy locators](results/INDEX.md)
- [Framework map and cross-framework interfaces](MAP.md)
- [Mathematical ownership, contribution and validation rules](MODEL.md)
- [External literature ledger](literature/README.md)

The linked-path inventory now covers **220 distinct Markdown files**: 127 catalog-linked files, 87 additional Framework/navigation-linked files, and 5 further verified carrier Arguments discovered by following proof dependencies. All 87 Framework/navigation-linked paths have been fetched successfully on this branch, with per-file character and line counts in [the additional-path inventory](CORPUS_LINK_CANDIDATES.md). This is **not** a complete repository tree listing; unlinked files remain outside coverage. A few very long coherent Arguments warrant targeted retrieval-cost review, notably `arguments/carriers/projection_and_elliptic_gluing.md` (84,503 characters), `arguments/carriers/normalization_conductor_phase2_addendum.md` (38,873), and `arguments/arithmetic/arithmetic_equations_and_jet_gaps.md` (36,663). File length alone does not justify splitting.

The catalog currently indexes **71 typed Results, 9 typed Arguments, 9 Frameworks and 2 Investigations**. Ordinary untyped Argument and topic Markdown files also carry mathematical content: the typed counts are **not** a count of all files, proofs, or coherent topics. The generated catalog currently displays **32 Result rows with “no recorded proof route”**; many also list evidence or independent audits. This means the proof-route metadata must be checked against the actual text, not that the Results are unproved.

## Structural recommendations (in progress)

The [canonical 516-file inventory](CORPUS_TREE_INVENTORY.md) now includes a **structural status** and **proposed action / target** for every file. [Source-inspected transformation proposals](CORPUS_STRUCTURAL_PROPOSALS.md) record mathematical units, methods, dependencies and target decisions for selected Arguments; the [carrier](CORPUS_PROOF_ROUTES_CARRIERS.md) and [torus](CORPUS_PROOF_ROUTES_TORUS.md) route analyses distinguish theorem assemblies from case proofs and upstream lemmas. **The structural review is complete:** all 210 Arguments, 83 Results-directory entries, 55 Frameworks, and 2 Investigations have cleanup dispositions in the canonical inventory. This is not a new mathematical proof audit. No mathematical content has been changed.

## Complete pinned-tree file inventory

The [single canonical repository inventory](CORPUS_TREE_INVENTORY.md) lists **all 516 files** in one table with paths, blob sizes, formats, and provisional path-based roles. This includes **357 research Markdown** and **159 other** files. This completes **file-level metadata inventory**, not mathematical review or code verification. Later inventory commits are outside the pinned snapshot.

## Authoritative repository tree coverage

The [complete repository inventory](CORPUS_TREE_INVENTORY.md) was generated from GitHub's recursive Git Trees API at commit `f6d2751e1c5eddd484d7f854841fa995e75a0ebe` (tree `902ff7719e6e601b40b4d93453a156f61c560b30`, `truncated=false`). The snapshot contains **516 repository files** and **357 research Markdown files**, including navigation and inventory files. The earlier 220-path link crawl missed **137** research Markdown paths, including **128 mathematical or supporting files** and **9 navigation/inventory files**. This closes path enumeration **for the pinned tree snapshot**; it does not complete content or proof review. The inventory file itself was committed afterward and is therefore not counted in its own snapshot.

## Additional dependency-linked files (verified)

The quartic-carrier proof-route review discovered six existing Arguments outside the preceding 214-file union: [entire conductor](arguments/carriers/genus_two_entire_conductor_proof.md) (12,420 characters), [trisecant carrier ideal](arguments/carriers/genus_two_trisecant_carrier_proof.md) (17,529), [projection-center moduli](arguments/carriers/quartic_projection_center_moduli.md) (11,713), [reduced singular support](arguments/carriers/quartic_singular_support_singleton_fibers.md) (16,613), [three-center bisection](arguments/carriers/genus_two_bisection_three_center_proof.md) (11,305), and [marking/section](arguments/carriers/genus_two_marking_and_section_proof.md) (27,830). These six additional files bring the verified linked-path union to **220**. See [carrier proof-route classifications](CORPUS_PROOF_ROUTES_CARRIERS.md). All six were fetched successfully. These examples demonstrate why linked-file crawling is not equivalent to a complete repository tree.

## First-pass topic partitions (navigation, not exclusive ownership)

| Topic / approach | Start here | Related proof or question routes |
| --- | --- | --- |
| Carrier normalization and degree exclusions | [Carrier Framework](frameworks/carrier-normalization/index.md) | [Quartic carrier Result](results/quartic_carrier_exclusion.md), [carrier proof](arguments/carriers/quartic_carrier_proof.md) |
| Formal normal geometry and filtered relations | [Formal-normal Framework](frameworks/formal-normal-geometry/index.md) | [normal flatness argument](arguments/normal-geometry/normal_flatness_and_filtered_ci.md), [open normal questions](frameworks/formal-normal-geometry/open_normal_geometry.md) |
| Global equations and actual lifting | [Global-equation Framework](frameworks/global-equation-realization/index.md) | [global equation jets](arguments/equations/global_equation_jets.md) |
| Residual intersection and absorption | [Residual Framework](frameworks/residual-construction/index.md) | [quasiprimitive residual argument](arguments/residuals/quasiprimitive_residual_cycles.md) |
| Spectral roots and Picard conditions | [Spectral Framework](frameworks/spectral-roots/index.md) | [moving-power roots](arguments/spectral/moving_power_and_spectral_roots.md) |
| Full torus Hilbert boundaries | [Torus-boundary Framework](frameworks/torus-supported-boundaries/index.md) | [torus Hilbert argument](arguments/torus_hilbert_boundary.md) |
| Embedded torus quotients and endpoints | [Embedded quotient Framework](frameworks/embedded-torus-quotients/index.md) | [intrinsic endpoint Result](results/intrinsic_limits_endpoint_fibers.md), [quotient/Hilbert comparison](investigations/quotient-hilbert-comparison/index.md) |
| Arithmetic supported lifts | [Arithmetic Framework](frameworks/arithmetic-supported-lifts/index.md) | [Z4 nonlifting Result](results/prescribed_z4_arithmetic_nonlifting.md), [arithmetic argument](arguments/arithmetic/z4_lifting_and_deformation.md) |
| Local cohomology and ancestor modules | [Local cohomology Framework](frameworks/local-cohomology/index.md) | [quartic ancestors](frameworks/local-cohomology/open_quartic_ancestors.md) |

These partitions are overlapping retrieval routes. A Result may depend on several approaches.

## Completed source-text proof-route classifications (not independent verification)

- [Quartic-carrier proof roles](CORPUS_PROOF_ROUTES_CARRIERS.md): theorem assembly, genus-two case proofs, structural inputs, narrower alternatives, and independent geometry.
- [Torus proof roles](CORPUS_PROOF_ROUTES_TORUS.md): three distinct typed Arguments, composite invariant-ideal exclusion, sextic eigenpair scope, constant quotient versus moving intrinsic limits.

## Per-topic inventory record (fill from complete mathematical text)

For each coherent topic, record:

1. **Canonical Results:** stable IDs and exact statement locations; include characteristic, hypotheses, scope and limitations.
2. **Distinct proof routes:** each Argument path and section; identify its method, hypotheses, dependencies, and what makes it independent. Mark **unclassified** until inspected. Distinguish alternative proofs from complementary lemmas, audits, and duplicate exposition.
3. **Other mathematical content:** examples, counterexamples, conditional statements, calculations, unresolved discrepancies and open interfaces.
4. **Ownership and retrieval:** minimal entrypoint; prerequisite Results; proof addresses; relevant Frameworks and Investigations; necessary evidence and literature.
5. **Refactor plan:** proposed coherent units and relocations; preserve old IDs and anchors, with redirects or aliases where needed.
6. **Verification:** pre/post mathematical-content coverage, link/anchor validation, and representative tokens or bytes fetched for the same retrieval task.

Do not mark a proof duplicate based on shared conclusions or similar titles. Do not rewrite mathematical claims to reconcile discrepancies. Log discrepancies with both exact addresses and leave them unresolved.

## Execution boundary

**Current stage: structural inventory only.** No proof deduplication, topic splitting, new mathematics, or modifications to existing mathematical source files are authorized by this stage.

Next: inspect the complete files and catalog links by topic, identify candidate Result/proof ownership, and populate the inventory before moving text. Prioritize long mixed-topic files and repeated retrieval paths, not arbitrary size thresholds. A coherent long proof is preferable to fragmented short files.

After any subsequent refactor, validate `python3 scripts/research.py validate`, `python3 scripts/research.py catalog --check`, and `python3 scripts/check_markdown_links.py --anchors` where an execution environment is available. Compare the same representative Result-to-proof and Framework-to-question retrieval tasks before and after, counting actual text consumed; do not treat structural checks as mathematical verification.

## Initial measured retrieval slices (character proxies)

These are **section boundaries inspected in full GitHub file reads**, not tokenizer measurements and not proof reviews. They illustrate opportunities for scoped section retrieval without physically splitting a coherent Argument.

| Source | Whole file | Example coherent section | Approximate slice | Relative reduction |
| --- | ---: | --- | ---: | ---: |
| `arguments/carriers/projection_and_elliptic_gluing.md` | 84,503 chars | §6, reconstructing actual source (from heading §6 to heading §7) | 7,404 chars | 91.2% |
| `arguments/carriers/quartic_carrier_proof.md` | 37,654 chars | §6, sectional genus two (from heading §6 to heading §7) | 7,117 chars | 81.1% |
| `arguments/arithmetic/arithmetic_equations_and_jet_gaps.md` | 36,663 chars | §3, binomial equation with arbitrary mate (to next main subsection) | 6,872 chars | 81.3% |

These section boundaries are approximate: headings of different levels occur within the slices. Before using them as stable agent addresses, confirm Markdown anchors and ensure the requested statement's hypotheses and dependencies are included. Full-file context may still be necessary for proof review.
