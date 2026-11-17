# Historical recovery coverage — 2026-11-17

This is a **temporary audit tracker**, not a new mathematical authority or corpus inventory. Source is GitHub comparison of `main` against 18 `recovery/*` branches. Of these, `recovery/gemini-audit` has no unique commits; `recovery/historical-retirement` has its own 894-file disposition ledger (857 retained, 28 consolidated-and-retired, 9 retired). The remaining 16 branches produce **208 distinct changed paths** after deduplication: **189 added** and **19 modified** relative to main. These are *path comparisons*, not 208 missing results. The 208-path list is reproducible from the branch comparisons; a full path-level reconciliation is not yet recorded here.

## Review standard

- **Covered (subject):** historical source and current destination both inspected, mathematical content clearly represented; no requirement to preserve dated duplicate prose or scripts.
- **Pending exact check:** a likely current destination exists but a potentially distinct theorem, proof qualification, or computation has not been checked.
- **Gap:** substantive historical claim demonstrably absent from current corpus. No gap established below.
- Do not confuse current-corpus review (352/352) or historical-retirement dispositions (894/894) with this 208-path branch comparison. Do not count historical notes and scripts independently when they are evidence for one result.

## First cross-branch adjudications

| Historical source / branch | Current home on main | Disposition |
| --- | --- | --- |
| `ribbon-triple-audit`: intrinsic independent audit | `research/arguments/arithmetic/z4_intrinsic_arithmetic_mechanism.md`, pinned proof source | Covered (subject); exact extension and fixed-ambient qualification present |
| `z4-relative-ext`: persistent marked relative class | `research/arguments/arithmetic/z4_intrinsic_arithmetic_mechanism.md`; `z4_lifting_and_deformation.md` | Covered (subject); marked relative scope and no unqualified divided-Frobenius claim |
| `leading-ideal-lifting`: GHK and global normal lifting | `research/arguments/normal-geometry/actual_equation_filtration.md` | Covered (subject); GHK hypotheses and local/global realization gates explicit |
| `delta-geometry`: conormal annihilator proposal | `research/results/conormal_entry_annihilator.md` | Covered (subject); exact entry-ideal annihilator theorem and scope present |
| `quartic-bitangents`: symmetric-square bitangents | `research/arguments/curve/quartic_dual_flags_and_bitangents.md` | Covered (subject); divisor flag and nonreduced boundary treatment present |
| `special-lines`: lines/planes STCI audit | `research/arguments/curve/special_plane_and_line_sections.md` | Covered (subject); residual and local-length caveats retained |
| `z4-integral-obstruction`: quartic obstruction | `research/arguments/arithmetic/z4_lifting_and_deformation.md` | Covered (subject); integral cocycle and deformation reduction present |
| `local-cohomology-generator`: dx1 p044 | `research/arguments/normal-geometry/e2_primitive_quartic_incidence.md` | Covered (subject); separate historical certificates not byte-checked |
| `frontier-assessment`: octic slice kernel verifier | `research/arguments/spectral/actual_octic_root_lift_comparison.md` | Pending exact check: 24-root kernel and basepoint-freeness certificate |
| `history-2026-10-06`: localcoh incidence | `research/arguments/normal-geometry/e2_primitive_quartic_incidence.md` and local-cohomology Arguments | Pending exact check: finite rank certificates |
| `gemini-audit-worktree`: VGIT full limits | `research/arguments/torus_hilbert_boundary.md` | Pending exact check: VGIT graph and weight-discrepancy specifics |
| `torus-homogeneous-descent`: homogeneous descent | `research/arguments/torus_hilbert_boundary.md` | Pending exact check: specific counterexamples and limitations |
| `torus-attracting-strata`: translate incidence | `research/arguments/torus_hilbert_boundary.md` and torus-supported framework | Pending exact check: conditional Chow-polytope rigidity; historical note itself labels converse unproved |
| `gemini-toric-integration`: toric ranking report | torus-supported framework and torus Hilbert Argument | Covered as historical synthesis, not independently a new theorem |
| `quartic-bitangents`: automorphisms/projections | `research/arguments/curve/quartic_projection_and_special_geometry.md` | Covered (subject); no new STCI claim |
| `gemini-toric-integration`: conductor endpoint verifier | `research/arguments/torus/toric_torsion_and_endpoint_contacts.md` | Pending exact check: certificate, not subject |

## Remaining work

1. Record all 208 unique paths, grouped by topic, with one disposition per path. Avoid a second permanent corpus inventory.
2. Compare the **pending exact checks** above; use existing main arguments/results to close most cases without redoing computations.
3. Reconcile the historical-retirement ledger with main only if evidence of unmerged substantive content appears.
4. Retire this temporary tracker when the audit is complete, retaining only any genuine mathematical correction.

**Current audit metric:** 16/16 non-retirement divergent recovery branches compared, 208/208 changed paths enumerated in comparison output, 16 subject-level decisions above, **0 confirmed content gaps**, **208/208 paths not yet individually dispositioned**. Subject decisions do not decrement path count.
