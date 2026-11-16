# Context-efficient corpus inventory (structural baseline)

This is a **structural inventory, not a mathematical review or completed proof classification**. It is an agent entry point for the *existing* Results / Arguments / Frameworks / Investigations corpus. Its baseline is the head of `chatgpt/math-content-consolidation` (PR #136) when this inventory branch was created. Do not infer proof equivalence, independence, or correctness from metadata alone.

For a file-by-file index of catalog-linked mathematical sources, see [CORPUS_FILE_INDEX.md](CORPUS_FILE_INDEX.md), extended by [87 verified Framework-linked files](CORPUS_LINK_CANDIDATES.md). Its coverage is explicitly partial until repository-wide paths are enumerated.

## Authoritative routes

- [Research entry and six retrieval lanes](INDEX.md)
- [Generated complete record catalog](CATALOG.md) — do not edit directly
- [Result topic and legacy locators](results/INDEX.md)
- [Framework map and cross-framework interfaces](MAP.md)
- [Mathematical ownership, contribution and validation rules](MODEL.md)
- [External literature ledger](literature/README.md)

The linked-path inventory now covers **214 distinct Markdown files**: 127 catalog-linked files and 87 additional files discovered through the Framework and central navigation links. All 87 additional paths have been fetched successfully on this branch, with per-file character and line counts in [the additional-path inventory](CORPUS_LINK_CANDIDATES.md). This is **not** a complete repository tree listing; unlinked files remain outside coverage. A few very long coherent Arguments warrant targeted retrieval-cost review, notably `arguments/carriers/projection_and_elliptic_gluing.md` (84,503 characters), `arguments/carriers/normalization_conductor_phase2_addendum.md` (38,873), and `arguments/arithmetic/arithmetic_equations_and_jet_gaps.md` (36,663). File length alone does not justify splitting.

The catalog currently indexes **71 typed Results, 9 typed Arguments, 9 Frameworks and 2 Investigations**. Ordinary untyped Argument and topic Markdown files also carry mathematical content: the typed counts are **not** a count of all files, proofs, or coherent topics. The generated catalog currently displays **32 Result rows with “no recorded proof route”**; many also list evidence or independent audits. This means the proof-route metadata must be checked against the actual text, not that the Results are unproved.

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
