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

**Current audit metric:** 16/16 non-retirement divergent recovery branches compared, 208/208 changed paths enumerated in comparison output, 16 subject-level decisions above, **0 confirmed losses of canonical Results or Arguments**, **208/208 paths assigned individual dispositions; see register**. Subject decisions do not decrement path count.

## Complete deduplicated path register (16 recovery branches)

All 208 paths are recorded below. **Closed** means no separate recovery is needed (historical source remains accessible in Git history). **Covered** means the main corpus has a canonical subject owner, not that all historical computations were rerun. **Pending** means a specific mathematical construction still needs comparison. Branch lists and statuses come from live GitHub comparisons against `main`; `added` means absent at the same path on main, not lost content. Subject classification is filename-based triage, not a mathematical judgment.

| Historical path | Diff | Topic triage | Branches | Path verdict | Canonical home / reason |
| --- | --- | --- | --- | --- | --- |
| `research/AUDITED_STATE_2026-10-06.md` | added | navigation / miscellaneous | local-cohomology-generator | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/computations/audit_z4_lift_2026_10_20.m2` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/branch_dx1_p044.out` | added | local cohomology / primitive | residual-verifier-fix | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/branch_dx1_p044.py` | added | local cohomology / primitive | local-cohomology-generator, residual-verifier-fix | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/branch_dx1_quartic_reduce.py` | added | local cohomology / primitive | local-cohomology-generator, residual-verifier-fix | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/draw_quartic_geometry_2026_10_24.py` | added | quartic geometry | quartic-bitangents | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_chart45_details.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_chart45.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_chart46.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_chart47_details.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_chart47.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_chart56.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_chart57.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_chart67.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_lambda0.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_lambda1.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact_lambda2.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/explore_localcoh_direction_contact.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-e2-incidence-2026-10-06.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-e2-p-constant-both-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-e2-p-constant-u-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-e2-p-t-both-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-e2-p-t-u-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-e2-r-constant-both-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-e2-r-constant-u-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-e2-r-t-both-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-e2-r-t-u-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-incidence-2026-10-06-certificate.json` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/localcoh-incidence-2026-10-06.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-incidence-bases.txt` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/localcoh-incidence-parity-dual-2026-10-06.json` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/localcoh-incidence-parity-dual-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-incidence-parity-dual-2026-10-06.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-incidence-parity-dual-2026-10-06.txt` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/localcoh-incidence-tensor.m2` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-incidence-tensor.txt` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/localcoh-parity-incidence-2026-10-06.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-parity-incidence-u-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-parity-incidence-v-2026-10-06.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-symbol-directions.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-symbol-export.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-symbol-numerators.txt` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/localcoh-symbol-parity-coordinates.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-symbol-parity.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-symbol-paritycheck.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-symbol-seed-products.txt` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/localcoh-symbol-seed.json` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/localcoh-symbol-seedcheck.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/localcoh-symbol-top.json` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/localcoh-symbol-top.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/normal_quartic_simple_elliptic_2026-10-06.json` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/normal_rational_carrier_compression_2026-10-06.json` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/octic_order_three_slice_kernels.py` | added | octic roots | frontier-assessment | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/quartic_automorphisms_bitangents_2026_10_24.json` | added | quartic geometry | quartic-bitangents | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/README.md` | modified | navigation / miscellaneous | delta-geometry, local-cohomology-generator, quartic-bitangents, special-lines, z4-integral-obstruction | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/computations/requirements-quartic-geometry-2026-10-24.txt` | added | quartic geometry | quartic-bitangents | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/requirements-z4-2026-10-20.txt` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/translate_incidence_checks_2026_11_05.m2` | added | torus / VGIT | torus-attracting-strata | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/validation_2026-10-05_resumed.json` | added | navigation / miscellaneous | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/validation_2026-10-06_checkpoint.json` | added | navigation / miscellaneous | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/computations/verify_delta_conormal_annihilator_2026_10_24.m2` | added | navigation / miscellaneous | delta-geometry, quartic-bitangents, special-lines | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_delta_rees_equation_module_2026_10_24.m2` | added | navigation / miscellaneous | delta-geometry, quartic-bitangents, special-lines | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_dx1_a_half_boundary.py` | added | local cohomology / primitive | local-cohomology-generator, residual-verifier-fix | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_dx1_p044_residual.py` | added | local cohomology / primitive | local-cohomology-generator, residual-verifier-fix | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_fixed_quartic_mate_degrees.py` | added | quartic geometry | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_localcoh_constant_direction_apolar.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_localcoh_direction_contact_survivor.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_localcoh_direction_image.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_localcoh_generic_length_model.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_localcoh_pure_direction_audit.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_mf6_defect12.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_mf6_type3.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_normal_quartic_simple_elliptic.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_normal_rational_carrier_compression.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_primitive_quadruple_universal.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_primitive_quartic_factor_audit.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_primitive_triple_parity.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_quartic_automorphisms_bitangents_2026_10_24.py` | added | quartic geometry | quartic-bitangents | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_sextic_triple_toric_vgit.py` | added | torus / VGIT | gemini-audit-worktree, gemini-toric-integration | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_special_lines_planes_2026_10_24.py` | added | quartic geometry | quartic-bitangents, special-lines | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_split22_chart_audit.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_split22_finite_reduction.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_split4_nonramified.py` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_toric_conductor_and_endpoint_defects.py` | added | torus / VGIT | gemini-toric-integration | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_toric_jet_deficits_and_unequal_vgit.py` | added | torus / VGIT | gemini-audit-worktree, gemini-toric-integration | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_torus_homogeneous_descent.m2` | added | torus / VGIT | torus-homogeneous-descent | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_vgit_surface_pairs.py` | added | torus / VGIT | gemini-audit-worktree, gemini-toric-integration, torus-homogeneous-descent, vgit-surface-pairs | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_z4_global_quartics_2026_10_20.m2` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_z4_local_structure_2026_10_20.m2` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/computations/verify_z4_quartic_obstruction_2026_10_20.py` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical computation/source, branch retained | source recovery branch; main argument/result governs claims |
| `research/figures/quartic-geometry-2026-10-24/projection-center.png` | added | quartic geometry | quartic-bitangents | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/figures/quartic-geometry-2026-10-24/projection-center.svg` | added | quartic geometry | quartic-bitangents | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/figures/quartic-geometry-2026-10-24/README.md` | added | quartic geometry | quartic-bitangents | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/figures/quartic-geometry-2026-10-24/symmetric-square-conics.png` | added | quartic geometry | quartic-bitangents | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/figures/quartic-geometry-2026-10-24/symmetric-square-conics.svg` | added | quartic geometry | quartic-bitangents | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/FRONTIER.md` | modified | navigation / miscellaneous | delta-geometry, frontier-assessment, gemini-audit-worktree, gemini-toric-integration, quartic-bitangents, special-lines, torus-attracting-strata, torus-homogeneous-descent, vgit-surface-pairs | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/INDEX.md` | modified | navigation / miscellaneous | delta-geometry, gemini-audit-worktree, gemini-toric-integration, quartic-bitangents, special-lines, torus-attracting-strata, torus-homogeneous-descent, vgit-surface-pairs, z4-integral-obstruction | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/LITERATURE_LEDGER.md` | modified | navigation / miscellaneous | gemini-audit-worktree, gemini-toric-integration, history-2026-10-06, leading-ideal-lifting, torus-homogeneous-descent, vgit-surface-pairs | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/MAP.md` | modified | navigation / miscellaneous | gemini-audit-worktree, gemini-toric-integration, torus-homogeneous-descent, vgit-surface-pairs | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/notes/2026-10-05-foundational-frontier-audit.md` | added | navigation / miscellaneous | history-2026-10-06 | Verified — mathematical statement mapped to canonical Argument | research/results/ and arguments/carriers/normal_primitive_carriers_and_bounds.md |
| `research/notes/2026-10-05-localcoh-direction-image.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — mathematical statement mapped to canonical Argument | research/arguments/local-cohomology/direction_and_apolarity.md |
| `research/notes/2026-10-05-localcoh-generic-length.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — mathematical statement mapped to canonical Argument | research/arguments/local-cohomology/direction_and_apolarity.md |
| `research/notes/2026-10-05-localcoh-pure-direction-audit.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — mathematical statement mapped to canonical Argument | research/arguments/residuals/extracted_multiplicity_mixed46_and_mf6.md |
| `research/notes/2026-10-05-mf6-further-audit.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — mathematical statement mapped to canonical Argument | research/arguments/residuals/extracted_multiplicity_mixed46_and_mf6.md |
| `research/notes/2026-10-05-mf6-pairing-audit.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — mathematical statement mapped to canonical Argument | research/arguments/residuals/extracted_multiplicity_mixed46_and_mf6.md |
| `research/notes/2026-10-05-mumford-normal-bound.md` | added | navigation / miscellaneous | history-2026-10-06, local-cohomology-generator | Verified — mathematical statement mapped to canonical Argument | research/arguments/carriers/normal_primitive_carriers_and_bounds.md |
| `research/notes/2026-10-05-normal-quartic-carriers.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — mathematical statement mapped to canonical Argument | research/arguments/carriers/normal_primitive_carriers_and_bounds.md |
| `research/notes/2026-10-05-positive-quartic-carrier-optimality.md` | added | local cohomology / primitive | history-2026-10-06 | Verified — substantive claim and scope mapped | research/arguments/arithmetic/rational_quartics_in_positive_characteristic.md |
| `research/notes/2026-10-05-primitive-carrier-theory.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — mathematical statement mapped to canonical Argument | research/arguments/carriers/normal_primitive_carriers_and_bounds.md |
| `research/notes/2026-10-05-residual-cycle-audit.md` | added | navigation / miscellaneous | history-2026-10-06 | Verified — mathematical statement mapped to canonical Argument | research/arguments/residuals/quasiprimitive_residual_cycles.md |
| `research/notes/2026-10-05-residual-cycle.md` | modified | navigation / miscellaneous | history-2026-10-06 | Verified — mathematical statement mapped to canonical Argument | research/arguments/residuals/quasiprimitive_residual_cycles.md |
| `research/notes/2026-10-05-split4-nonramified.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/residuals/extracted_residual_cycles_and_split_configurations.md |
| `research/notes/2026-10-05-uniform-multiplicity.md` | modified | local cohomology / primitive | local-cohomology-generator | Verified — mathematical statement mapped to canonical Argument | research/arguments/residuals/quasiprimitive_residual_cycles.md |
| `research/notes/2026-10-06-dx1-p044-classification.md` | added | local cohomology / primitive | local-cohomology-generator, residual-verifier-fix | Verified — substantive claim and scope mapped | research/arguments/normal-geometry/e2_primitive_quartic_incidence.md |
| `research/notes/2026-10-06-localcoh-constant-direction-apolar.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/local-cohomology/direction_and_apolarity.md |
| `research/notes/2026-10-06-localcoh-e2-incidence-charts.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/carriers/normal_primitive_carriers_and_bounds.md |
| `research/notes/2026-10-06-localcoh-incidence.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/equations/extracted_foundational_frontier_and_incidence.md |
| `research/notes/2026-10-06-localcoh-mixed-contact-pole.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/local-cohomology/contact_parity_and_mf6.md |
| `research/notes/2026-10-06-localcoh-parity-dual.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/local-cohomology/contact_parity_and_mf6.md |
| `research/notes/2026-10-06-mf6-type3-independent-audit.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/local-cohomology/contact_parity_and_mf6.md |
| `research/notes/2026-10-06-mf6-type4-incidence.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/local-cohomology/contact_parity_and_mf6.md |
| `research/notes/2026-10-06-normal-bound-independent-audit.md` | added | navigation / miscellaneous | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/carriers/normal_carrier_compression.md |
| `research/notes/2026-10-06-normal-rational-carrier-compression.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/carriers/normal_carrier_compression.md |
| `research/notes/2026-10-06-primitive-quadruple-audit.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/carriers/normal_carriers_primitive_jets_and_characteristic.md |
| `research/notes/2026-10-06-primitive-quadruple-universal.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/carriers/normal_carriers_primitive_jets_and_characteristic.md |
| `research/notes/2026-10-06-primitive-triple-parity.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/carriers/normal_carriers_primitive_jets_and_characteristic.md |
| `research/notes/2026-10-06-split22-finite-reduction.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/carriers/split_sextic_two_ramified_roots.md |
| `research/notes/2026-10-06-uniform-order-one-frontier.md` | added | local cohomology / primitive | history-2026-10-06, local-cohomology-generator | Verified — substantive claim and scope mapped | research/arguments/equations/global_equation_jets.md; research/arguments/carriers/normal_carrier_compression.md |
| `research/notes/2026-10-20-z4-characteristic-zero-lifting-report.md` | added | arithmetic Z4 | z4-integral-obstruction | Verified — substantive claims mapped to canonical proofs | research/arguments/arithmetic/z4_lifting_and_deformation.md; z4_intrinsic_arithmetic_mechanism.md |
| `research/notes/2026-10-20-z4-ci-deformation-lemma.md` | added | arithmetic Z4 | z4-integral-obstruction | Verified — substantive claims mapped to canonical proofs | research/arguments/arithmetic/z4_lifting_and_deformation.md; z4_intrinsic_arithmetic_mechanism.md |
| `research/notes/2026-10-20-z4-lift-independent-audit.md` | added | arithmetic Z4 | z4-integral-obstruction | Verified — substantive claims mapped to canonical proofs | research/arguments/arithmetic/z4_lifting_and_deformation.md; z4_intrinsic_arithmetic_mechanism.md |
| `research/notes/2026-10-20-z4-local-structure.md` | added | arithmetic Z4 | z4-integral-obstruction | Verified — substantive claims mapped to canonical proofs | research/arguments/arithmetic/z4_lifting_and_deformation.md; z4_intrinsic_arithmetic_mechanism.md |
| `research/notes/2026-10-20-z4-quartic-obstruction.md` | added | arithmetic Z4 | z4-integral-obstruction | Verified — substantive claims mapped to canonical proofs | research/arguments/arithmetic/z4_lifting_and_deformation.md; z4_intrinsic_arithmetic_mechanism.md |
| `research/notes/2026-10-21-intrinsic-ribbon-triple-independent-audit.md` | added | arithmetic Z4 | ribbon-triple-audit | Verified — substantive claims mapped to canonical proofs | research/arguments/arithmetic/z4_lifting_and_deformation.md; z4_intrinsic_arithmetic_mechanism.md |
| `research/notes/2026-10-21-z4-persistent-independent-audit.md` | added | arithmetic Z4 | z4-relative-ext | Verified — substantive claims mapped to canonical proofs | research/arguments/arithmetic/z4_lifting_and_deformation.md; z4_intrinsic_arithmetic_mechanism.md |
| `research/notes/2026-10-24-delta-annihilator-review.md` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Verified — substantive claims mapped to canonical proofs | research/arguments/normal-geometry/rees_equation_persistence.md; research/results/conormal_entry_annihilator.md; transverse_specialization.md; normal_flat_comparison_specialization.md |
| `research/notes/2026-10-24-delta-base-change-proposal.md` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Verified — substantive claims mapped to canonical proofs | research/arguments/normal-geometry/rees_equation_persistence.md; research/results/conormal_entry_annihilator.md; transverse_specialization.md; normal_flat_comparison_specialization.md |
| `research/notes/2026-10-24-delta-conormal-annihilator-proposal.md` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Verified — substantive claims mapped to canonical proofs | research/arguments/normal-geometry/rees_equation_persistence.md; research/results/conormal_entry_annihilator.md; transverse_specialization.md; normal_flat_comparison_specialization.md |
| `research/notes/2026-10-24-delta-embedding-geometry-report.md` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Verified — substantive claims mapped to canonical proofs | research/arguments/normal-geometry/rees_equation_persistence.md; research/results/conormal_entry_annihilator.md; transverse_specialization.md; normal_flat_comparison_specialization.md |
| `research/notes/2026-10-24-delta-normal-geometry-proposal.md` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Verified — substantive claims mapped to canonical proofs | research/arguments/normal-geometry/rees_equation_persistence.md; research/results/conormal_entry_annihilator.md; transverse_specialization.md; normal_flat_comparison_specialization.md |
| `research/notes/2026-10-24-delta-rees-specialization-proposal.md` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Verified — substantive claims mapped to canonical proofs | research/arguments/normal-geometry/rees_equation_persistence.md; research/results/conormal_entry_annihilator.md; transverse_specialization.md; normal_flat_comparison_specialization.md |
| `research/notes/2026-10-24-delta-rees-specialization-review.md` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Verified — substantive claims mapped to canonical proofs | research/arguments/normal-geometry/rees_equation_persistence.md; research/results/conormal_entry_annihilator.md; transverse_specialization.md; normal_flat_comparison_specialization.md |
| `research/notes/2026-10-24-osculating-normal-count-review.md` | added | quartic geometry | quartic-bitangents, special-lines | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-quartic-automorphisms-bitangents-synthesis.md` | added | quartic geometry | quartic-bitangents | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-quartic-invariant-literature-outlook.md` | added | quartic geometry | quartic-bitangents | Verified — substantive mathematical claims mapped | research/arguments/carriers/quartic_projection_center_moduli.md |
| `research/notes/2026-10-24-quartic-projection-automorphisms.md` | added | quartic geometry | quartic-bitangents | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-quartic-projection-independent-audit.md` | added | quartic geometry | quartic-bitangents | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-quartic-symmetric-independent-audit.md` | added | quartic geometry | quartic-bitangents | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-quartic-symmetric-square-bitangents.md` | added | quartic geometry | quartic-bitangents | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-special-dual-incidence-derivation.md` | added | navigation / miscellaneous | quartic-bitangents, special-lines | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-special-lines-geometry-derivation.md` | added | quartic geometry | quartic-bitangents, special-lines | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-special-lines-planes-geometry-audit.md` | added | quartic geometry | quartic-bitangents, special-lines | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-special-lines-planes-research-note.md` | added | quartic geometry | quartic-bitangents, special-lines | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-special-lines-planes-stci-audit.md` | added | quartic geometry | quartic-bitangents, special-lines | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/notes/2026-10-24-special-sections-stci-derivation.md` | added | navigation / miscellaneous | quartic-bitangents, special-lines | Verified — substantive geometry mapped to canonical arguments | research/arguments/curve/quartic_dual_flags_and_bitangents.md; quartic_projection_and_special_geometry.md; special_plane_and_line_sections.md |
| `research/RESEARCH_DECISION_GUIDE.md` | modified | navigation / miscellaneous | frontier-assessment, gemini-audit-worktree, gemini-toric-integration, torus-homogeneous-descent, vgit-surface-pairs | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/RESEARCH_RECORD.md` | modified | navigation / miscellaneous | local-cohomology-generator | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/RESEARCH_REPORT.md` | modified | navigation / miscellaneous | history-2026-10-06, local-cohomology-generator | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/RESEARCH_UPDATE_2026-10-05.md` | modified | navigation / miscellaneous | history-2026-10-06, local-cohomology-generator | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/scratch/explore_mf6_type4.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/explore_split22_nonramified.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/explore_split4_lift.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/explore_split4_local.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/explore_split4_nonramified.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/mf6_type4_incidence.json` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/mf6_type4_resultant.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/classify.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/equations.json` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/general_triple_contact.json` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/general_triple_contact.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/general_triple_contact.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/generate.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/parity_triple_certificate.json` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/quartic_contact.json` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/quartic_contact.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/quartic_contact.py` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/triple_contact_p_chart.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/scratch/primitive47universal/triple_contact_p_factors.m2` | added | local cohomology / primitive | history-2026-10-06 | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/STATE.md` | modified | navigation / miscellaneous | delta-geometry, frontier-assessment, gemini-audit-worktree, gemini-toric-integration, quartic-bitangents, special-lines, torus-homogeneous-descent, vgit-surface-pairs | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/SUCCESSOR_HANDOFF.md` | modified | navigation / miscellaneous | history-2026-10-06, local-cohomology-generator | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/supplements/FROBENIUS_POWER_LIFTING_PRECISION.md` | modified | navigation / miscellaneous | gemini-toric-integration | Resolved — missing torus section integrated with equivariance qualification | research/arguments/arithmetic/frobenius_power_lifting_precision.md (commit 89dbc97) |
| `research/supplements/LOCAL_LEADING_IDEALS_AND_GLOBAL_NORMAL_LIFTING.md` | added | navigation / miscellaneous | leading-ideal-lifting | Verified — substantive mathematical claims mapped | research/arguments/normal-geometry/actual_equation_filtration.md; research/arguments/equations/global_equation_jets.md |
| `research/supplements/SEXTIC_ADE_REDUCTION.md` | modified | navigation / miscellaneous | gemini-audit-worktree, gemini-toric-integration | Rejected after verification triage — no further integration | Historical Git history only |
| `research/SUSTAINED_RESEARCH_2026-10-05.md` | added | navigation / miscellaneous | history-2026-10-06 | Closed — superseded navigation/history | main research/INDEX.md, MAP.md, MODEL.md and corpus catalog |
| `research/synthesis/actual_octic_root_lift_comparison.md` | modified | octic roots | frontier-assessment | Verified — substantive mathematical claims mapped | research/arguments/spectral/actual_octic_root_lift_comparison.md |
| `research/synthesis/global_equation_jets.md` | modified | navigation / miscellaneous | gemini-audit-worktree, gemini-toric-integration | Verified — substantive mathematical claims mapped | research/arguments/equations/global_equation_jets.md |
| `research/synthesis/projected_thickening_section_defects.md` | modified | navigation / miscellaneous | gemini-audit-worktree, gemini-toric-integration | Verified — substantive mathematical claims mapped | research/arguments/linkage/projected_thickening_section_defects.md |
| `research/synthesis/residual_cycles_and_chow_incidence.md` | added | torus / VGIT | torus-homogeneous-descent, vgit-surface-pairs | Resolved — exact theorems, examples, and scope in canonical torus Argument | research/arguments/torus_hilbert_boundary.md |
| `research/synthesis/toric_integration_evaluation_and_ranking.md` | added | torus / VGIT | gemini-toric-integration | Resolved as synthesis/index — claims assigned to canonical and remaining source reviews | research/arguments/arithmetic/frobenius_power_lifting_precision.md; research/arguments/carriers/sextic_ade_reduction.md; research/arguments/torus_hilbert_boundary.md; outstanding original sextic/VGIT supplements |
| `research/synthesis/torus_attracting_strata_and_generator_incidence.md` | modified | torus / VGIT | gemini-audit-worktree, gemini-toric-integration, torus-homogeneous-descent, vgit-surface-pairs | Resolved — preserved opposite-limit refinement and caveats | research/investigations/supported-generator-incidence/index.md (commit 9ce6f76); research/arguments/torus_hilbert_boundary.md |
| `research/synthesis/torus_homogeneous_descent.md` | added | torus / VGIT | torus-homogeneous-descent | Resolved — descent statements mapped; equivariant rank and counterexample restored | research/arguments/torus_hilbert_boundary.md (commit 8a00b63) |
| `research/synthesis/torus_residual_arrangements_and_absorption.md` | added | torus / VGIT | torus-homogeneous-descent, vgit-surface-pairs | Resolved — exact theorems, examples, and scope in canonical torus Argument | research/arguments/torus_hilbert_boundary.md |
| `research/synthesis/translate_incidence_and_attracting_strata.md` | added | torus / VGIT | torus-attracting-strata | Resolved — weight-slice incidence preserved; conditional claims not promoted | research/investigations/supported-generator-incidence/index.md (commit 574e851); research/arguments/torus_hilbert_boundary.md |
| `research/synthesis/vgit_surface_pairs_and_full_limits.md` | added | torus / VGIT | gemini-audit-worktree, gemini-toric-integration, torus-homogeneous-descent, vgit-surface-pairs | Rejected after verification triage — no further integration | Historical Git history only |
| `research/validation/2026-10-24-special-lines-planes/checks.json` | added | quartic geometry | quartic-bitangents, special-lines | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/2026-10-24-special-lines-planes/manifest.json` | added | quartic geometry | quartic-bitangents, special-lines | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/2026-10-24-special-lines-planes/README.md` | added | quartic geometry | quartic-bitangents, special-lines | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/delta-embedding-2026-10-24/canonical-records.log` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/delta-embedding-2026-10-24/conormal-annihilator-m2.log` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/delta-embedding-2026-10-24/integration.log` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/delta-embedding-2026-10-24/README.md` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/delta-embedding-2026-10-24/rees-equation-module-m2.log` | added | conormal / Rees | delta-geometry, quartic-bitangents, special-lines | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/quartic-geometry-2026-10-24/README.md` | added | quartic geometry | quartic-bitangents | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/z4-lift-2026-10-20/audit.log` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/z4-lift-2026-10-20/global-quartics.log` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/z4-lift-2026-10-20/local-structure.log` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/z4-lift-2026-10-20/obstruction.log` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |
| `research/validation/z4-lift-2026-10-20/records.log` | added | arithmetic Z4 | z4-integral-obstruction | Closed — historical evidence/output, branch retained | source recovery branch; canonical mathematics on main |


## Bulk disposition checkpoint (2026-11-17)

All 208 paths received a reproducible first-pass decision. Historical executable and output artifacts remain accessible in their recovery branches and are not treated as missing mathematics simply because they were retired from main. These dispositions do not assert byte-equivalence or rerun scripts. Classification counts: {"Closed — superseded navigation/history":13,"Closed — historical computation/source, branch retained":71,"Closed — historical evidence/output, branch retained":55,"Pending — distinct content not yet checked":12,"Covered — canonical primitive / local cohomology":22,"Covered — canonical quartic geometry":13,"Covered — canonical arithmetic argument":7,"Covered — canonical conormal / comparison result":7,"Covered — canonical octic comparison":1,"Pending — compare distinctive torus construction":7}. The only pending paths require distinctive mathematical content comparison, not a blanket re-review of historical scripts.


## Second batch: inspected pending mathematical documents

Inspected all 19 previously pending historical documents (their scope and principal claims). Twelve were matched to existing canonical subject owners or recognized as historical comparative material; seven torus/VGIT constructions remain flagged for a more specific equivalence check. These are conservative *content-difference* flags, not suspected missing STCI theorems. The earlier bulk categories are archival/recovery dispositions, not claims of independent proof verification. No file was imported or deleted.


## Superseded administrative close — 2026-11-17

**208/208 paths assigned a disposition; 0 pending recovery decisions.** The final six were inspected in full by section and scoped against the current torus Hilbert Argument, torus-supported Framework and quasiprimitive residual Argument. One is covered at the level of the principal full-limit and generator criterion; five contain additional *provisional*, noncanonical constructions or examples not demonstrated to be fully incorporated into main. These five are deliberately classified **archived**, not **identical** or **proved redundant**. Their exact text remains available in the named recovery branches. In particular, the VGIT report's coarse weight partition, graph polarizations, common-factor blowups and rank-drop strata should not be represented as fully present in the main torus Argument. The translate-incidence note explicitly relies on unproved Chow-polytope rigidity and an additional provisional homogeneous bound; neither becomes a theorem by this audit.

**Audit closed as a recovery/accounting task, not a proof-equivalence certification.** No demonstrated loss of a canonical theorem requiring restoration; no historical file deletion or mathematical rewrite. Future research may selectively retrieve archived provisional constructions by branch/path. The historical-retirement ledger (894 decisions) is a separate prior audit and is not reverified here. Do not delete recovery branches merely because this tracker is complete. This temporary tracker can be retired after its summary is included in the eventual merge/PR record.


## Reopened substantive comparison — 2026-11-17

**69 mathematical Markdown documents reopened.** Previous 208-path accounting was archival only and did not prove all mathematical claims preserved. Historical scripts, logs and navigation remain in the administrative bucket (139). Every reopened document requires claim-level mapping to main or an explicit decision not to integrate; do not close merely because the subject appears in main. Earlier 'final recovery decision' is superseded. PR #146 must not be merged as a completed mathematical audit.


## Claim-level review batch 1 — arithmetic and conormal (14 sources)

**Seven delta documents:** Compared the historical annihilator proof, conormal-entry/Fitting interpretation, Rees equation-module torsion, duration family, labelled carrier-square, normal-cone regularity, transverse specialization and normal-flatness distinctions with the canonical `rees_equation_persistence.md`, `conormal_entry_annihilator.md`, `transverse_specialization.md` and `normal_flat_comparison_specialization.md`. Canonical headings and substantive mathematical qualifications match, including k[u]- versus O_C[u]-flatness, preservation of source-line labels, and the unproved spectral-page/duration identification. Historical independent reviews add provenance, not distinct unincorporated mathematical conclusions.

**Seven Z4 documents:** Compared prescribed quadruple local algebra, forced complete-intersection reduction, 35-monomial coefficient coverage, integral triple cocycle with quadratic corrections, fixed marked relative Ext, coordinate-invariance caveats, and the absence of a canonical divided-Frobenius operation with `z4_lifting_and_deformation.md` and `z4_intrinsic_arithmetic_mechanism.md`. The canonical Arguments retain the precise mixed-characteristic scope and fixed-embedding hypotheses. Historical independent audits remain source provenance, not separate claims requiring import.

**Disposition:** 14 mathematical documents closed at claim-level; no missing mathematical statement identified in these two clusters. This is source-to-canonical preservation review, not a new independent proof verification or rerun of historical computation scripts.


## Claim-level review batch 2 — quartic geometry (12 sources)

Compared historical projection-center and automorphism constructions, symmetric-square secant and bitangent correspondences (including trace-free multiplier, diagonal and exceptional fibers), osculating involution and coincidence divisor, special-line/plane incidences, cubic scroll and dual singularities, normal-direction coincidence and its counterexample, and sole-support qualifications against `quartic_dual_flags_and_bitangents.md`, `quartic_projection_and_special_geometry.md`, and `special_plane_and_line_sections.md`. These canonical Arguments contain the substantive developments and explicit qualifications. Independent audits are retained as provenance in history. **12 documents closed**; the invariant-theory literature outlook remains open for a specific check of GIT quotient and characteristic-two observations. No new STCI theorem inferred.


## Claim-level review batch 3 — five additional sources

The quartic invariant-theory literature note is incorporated in `quartic_projection_center_moduli.md` (including its characteristic-two boundary); the leading-ideal/global lifting supplement is represented in `actual_equation_filtration.md` and `global_equation_jets.md`; the octic actual-root comparison is in `actual_octic_root_lift_comparison.md`; the full Cech source filtration and sextic order-five cutoff are in `global_equation_jets.md`; the projected-thickening Rao/ACM defects and the quotient caveat are in `projected_thickening_section_defects.md`. Five sources closed by mathematical section and claim matching. **Do not yet close** the Frobenius-power supplement (additional torus-eigenform section), sextic ADE supplement (additional weight/contact tower), or toric synthesis: their tails include constructions not demonstrated in the primary canonical Arguments.


## Claim-level review batch 4 — early October carrier, residual and MF6 (12 sources)

Reviewed the 5 October source headings, conclusions, and canonical Argument sections. Exact mathematical section correspondence was found for the quartic direction image and generic-length consequence; pure constant-direction audit; MF6 Gorenstein perfect pairing and mixed (4,6) higher-jet exclusions; numerical self-intersection versus normal line; normal quartic carrier rational-singularity exclusion; primitive-fourth cubic carrier; quasiprimitive determinant/residual-cycle statements and the uniform first-normal bound. The foundational audit is corroborating review of existing results rather than a distinct theorem. **12 sources closed**. The positive-characteristic cuspidal-carrier optimality and nonramified split-sextic chart remain pending specific canonical comparison. No historical computation was rerun.


## Claim-level review batch 5 — remaining early-October mathematical notes (17 sources)

Compared the historical headings, scope conclusions and mathematical claims against current canonical Arguments. The exact cuspidal-carrier prime/degree minima appear in `rational_quartics_in_positive_characteristic.md`; the nonramified split-sextic ordinary A3 and [2,2] chart in `extracted_residual_cycles_and_split_configurations.md`; dx=1 P-044 boundaries in `e2_primitive_quartic_incidence.md`; local-cohomology scalar divisor, finite pure-top charts, recovered polynomial dual, mixed contact counterexample and parity exclusions in `direction_and_apolarity.md`, `normal_primitive_carriers_and_bounds.md`, `extracted_foundational_frontier_and_incidence.md`, and `contact_parity_and_mf6.md`. The MF6 type-three/type-four incidence and caveats appear in `contact_parity_and_mf6.md`. The rational-resolution denominator compression and order-one bounds appear in `normal_carrier_compression.md`; universal primitive-fourth and parity-triple arguments in `normal_carriers_primitive_jets_and_characteristic.md`; two-ramified-root higher-jet reduction in `split_sextic_two_ramified_roots.md`. **17 source notes closed by claim-level canonical mapping**. The remaining 9 sources are the Frobenius/sextic supplements and torus/VGIT syntheses, which may contain genuinely unincorporated mathematics.


## Substantive comparison checkpoint — nine extended sources

Compared full section inventories of the nine remaining sources with canonical torus, sextic, and Frobenius Arguments/Frameworks. **Do not close by topic equivalence.** Concrete preservation gaps:

1. `research/supplements/FROBENIUS_POWER_LIFTING_PRECISION.md`: the canonical `arguments/arithmetic/frobenius_power_lifting_precision.md` matches the first seven substantive sections but **does not contain** the additional section on torus eigenforms, `mu_p^{(1)}` orbit splitting in characteristic zero, and endpoint grading. Requires either integration into an arithmetic/torus Argument or explicit evidence of a different canonical home.
2. `research/supplements/SEXTIC_ADE_REDUCTION.md`: the canonical `arguments/carriers/sextic_ade_reduction.md` matches the first five mathematical sections but **does not contain** the extended double-sextic kernel, 23-vs-24 rank split, torus grading, bilinear contact tower through order six, nonproper quintic hull, and classification of T-fixed pencils. These are distinct candidate contributions; must verify proofs and integrate or reject individually.
3. `research/synthesis/vgit_surface_pairs_and_full_limits.md`: `arguments/torus_hilbert_boundary.md` contains a Chow/weight/VGIT summary but **does not reproduce** the detailed common-factor rank-drop law, prime-ideal graph-boundary dichotomy, Pluecker weight range, factorization stratification and Hilbert–Burch blowup analysis. These require proof-level review before promotion.
4. `research/synthesis/torus_homogeneous_descent.md`: canonical torus Argument covers generator lifting, supported example and clean residual descent, but the historical document additionally presents equivariant set-theoretic rank and higher-rank torus failure. Verify whether those statements have an alternate canonical home.
5. `research/synthesis/translate_incidence_and_attracting_strata.md`: distinguish established translate-incidence statements from **conditional** Chow-polytope rigidity. Do not promote the latter as a theorem.
6. `research/synthesis/residual_cycles_and_chow_incidence.md`, `torus_attracting_strata_and_generator_incidence.md`, and `torus_residual_arrangements_and_absorption.md`: major themes are reflected in `arguments/torus_hilbert_boundary.md` and `frameworks/torus-supported-boundaries/index.md`; exact proof coverage and counterexample details remain to check.
7. `research/synthesis/toric_integration_evaluation_and_ranking.md`: primarily a historical integration roadmap, but its closing torus-eigenform and orbit-splitting assertions must be checked against the Frobenius supplement above.

**Status:** 60/69 sources fully dispositioned; 9 remain under substantive investigation. At least three definite section-level preservation gaps are identified, not yet validated as correct mathematical claims. The prior conclusion 'no confirmed missing canonical result' is compatible with these gaps: a historically asserted claim is not automatically a proved canonical Result. Do not merge PR #146 as a complete recovery audit.


## Claim-level review batch 6 — Frobenius torus restoration

Restored the extra torus-eigenform, \(\mu_p^{(1)}\)-splitting, and endpoint-defect section to `arguments/arithmetic/frobenius_power_lifting_precision.md` in commit `89dbc97`. The characteristic-zero identity is asserted as a **cycle** decomposition (not a reduced scheme equality at endpoints); characteristic-\(p\) support and generic multiplicity are distinguished. Corrected an equivariance scope hazard: only genuinely torus-equivariant DVR traits carry a graded defect, whereas every trait retains the endpoint-supported sheaf decomposition and length formula. One supplement resolved; the overlapping historical toric integration roadmap remains open until its remaining independent content is checked.


## Claim-level review batch 7 — opposite-limit generator incidence

The historical attracting-strata source contains established full-limit and two-generation machinery already in `arguments/torus_hilbert_boundary.md`, plus a distinct **research formulation** using the intersection of opposite-limit attracting loci and a warning against identifying Hilbert torus limits with geometric endpoints of the transverse quotient. Restored that formulation and its necessary/sufficient caveats to `investigations/supported-generator-incidence/index.md` in commit `9ce6f76`. This is not a new theorem, a finite-strata classification, or an STCI exclusion. One source closed.


## Claim-level review batch 8 — Chow incidence and residual arrangements (2 sources)

Compared the historical proper-pair Chow morphism, the closed multiplicity filtration `U_ge_r = chi^{-1}(P(Q^r E_{D-r delta}))`, saturation across the improper boundary, single affine chart, complete-intersection minimal-generator criterion and Hilbert polynomial, and the top Chow graph with the corresponding full statements and qualifications in `arguments/torus_hilbert_boundary.md`. The latter explicitly distinguishes the top Chow fiber from the closure of supported pairs, and preserves the relative-to-U closedness and nonreduced-incidence caveat. The historical `residual_cycles_and_chow_incidence.md` is therefore closed.

Compared invariant-orbit degree formula, endpoint attachment and sole disjoint line `L_12`, explicit invariant proper (3,4) pair `(x_0q,x_3A)` with its full cycle `[C]+5[L_23]+[L_02]+[L_01]+[L_12]`, upper semicontinuity of marked cycle multiplicity, and cycle-level versus actual ideal absorption against the section `Invariant residual supports and absorption limits` of the same canonical Argument. The historical `torus_residual_arrangements_and_absorption.md` is therefore closed. These are preservation decisions, not new proof certificates.


## Claim-level review batch 9 — torus homogeneous descent

The full-initial-ideal/naive-leading-pair distinction, minimal-resolution and generator caveats, supported four-generator embedded-point example, clean-cancellation proposition, vertical excess and degree descent are already in `arguments/torus_hilbert_boundary.md`. The historical source also contains a distinct **equivariant set-theoretic rank three** observation for the quartic and a counterexample to descent for a higher-rank torus. Restored the power lemma, explicit `(q,A,D)` radical calculation on the Segre quadric, and the three-concurrent-lines counterexample with its one-parameter exception in commit `8a00b63`. The rank-three conclusion uses the previously established characteristic-zero eigenform-pair obstruction (R-0042), not a new global STCI exclusion. One source closed.


## Claim-level review batch 10 — translate incidence

The historical translate-incidence source supplies a weight-slice coefficient formula, finite translate-count bound for proper pairs, and a diagonalizable group-scheme interpretation of binomial translate incidence. Preserved those precise statements in `investigations/supported-generator-incidence/index.md` (commit `574e851`). Its clean-cancellation theorem is already proved in the torus Argument. Its first-step universal splitting/degree-bound extrapolation explicitly depends on provisional hypotheses; it was **not** promoted as a theorem or used to infer a characteristic-zero exclusion. One source closed.


## Claim-level review batch 11 — toric synthesis and partial sextic/VGIT recovery

The historical `toric_integration_evaluation_and_ranking.md` is a ranked integration memorandum rather than an independent proof: its five streams point to the original sextic ADE and VGIT developments, global-equation jets, projected-thickening defects, and Frobenius torus material. Its Frobenius orbit-splitting contribution was restored in commit `89dbc97`; global jets and projected-thickening primary sources were mapped earlier. Its remaining claims are **not silently accepted**: they remain assigned to the two open primary historical sources, with explicit unverified computational claims. The roadmap is closed as a separate review item, not as verification of its underlying claims.

For the sextic supplement, restored the intrinsic identification `ker(h)=H^0((I_triple intersect I_C^2)(6))`, its dimension 10, and the cubic-contact quotient and rank decomposition to `arguments/carriers/sextic_ade_reduction.md` in commit `df344e1`. The proposed 153-case torus-fixed pencil classification and order-six exclusion remain unverified and are **not** promoted as a canonical Result. Its original Python verifier exists on `recovery/gemini-audit-worktree` but not `main`.

For the VGIT synthesis, restored the exact degreewise common-factor rank-loss formula and prime-ideal carrier/coprime-pencil dichotomy to `arguments/torus_hilbert_boundary.md` in commit `456db66`. Its detailed Pluecker partition and Hilbert–Burch blowup resolution remain unverified, and its original verifier likewise exists only on the recovery branch. The two primary historical sources remain open pending proof-level adjudication and a decision on retaining the exact certificates.


## Proof-level issue in historical VGIT §8.3 — modular intersection identity

The claimed first-blowup Hilbert–Burch theorem in
\`research/synthesis/vgit_surface_pairs_and_full_limits.md\`
(§8.3) asserts that \(\gcd(A,B)=\gcd(D,G)=1\),
with \(G=B\widetilde F-A\widetilde G\in(A,B)\),
forces \((D,A,B)\) to be a regular sequence and hence
\[
 (DA,DB,G)=(D,G)\cap(A,B).
\]
**That implication is false without a further hypothesis.**
For an elementary homogeneous example in \(k[x,y,z,w]\),
take \(A=x\), \(B=y\), \(D=x+y\),
\(\widetilde F=xz\), \(\widetilde G=yw\).
Then \(G=xy(z-w)\), so
\(\gcd(A,B)=\gcd(D,G)=1\), but
\(D\in(A,B)\) and \((D,A,B)\) has height two,
not three. Thus
\((D,G)\cap(A,B)=(D,G)\) while
\((DA,DB,G)\ne(D,G)\).
This counterexample is to the stated *general algebraic implication*;
it is not by itself a counterexample in the restricted
quartic-containing pencil locus \(X_d\). The source must prove the
missing height-three hypothesis in that locus or explicitly impose it.
The canonical restoration in commit \`456db66\` intentionally
excluded the §8.3 blowup theorem. Do not promote its modular
intersection identity or its asserted exhaustive secondary
indeterminacy classification without repair.

The Hilbert–Burch **three-minor construction** and
degreewise rank-drop formula may still be valid under their
appropriate codimension hypotheses. This defect does not invalidate
those narrower statements.


## Certificate scope check — last two mathematical sources

Read the historical verifier structures on
\`recovery/gemini-audit-worktree\`.
\`verify_sextic_triple_toric_vgit.py\` (26,061 characters)
contains exact symbolic functions for weight decompositions,
contact towers, nonproper quintic hull, and torus-fixed pencils.
Its \`main()\` invokes all of those checks, but the script
was **not executed in this audit**; neither its complete
153-weight-pair coverage nor the order-six colength-six
classification has been independently validated here.
The historical source is therefore **partially integrated**,
with the geometric kernel argument preserved and the
computational classification still open.

\`verify_vgit_surface_pairs.py\` (13,480 characters)
contains representation, residual-control, and blowup
examples. Its Hilbert–Burch verification explicitly checks
two chosen \(e=4,5\) examples only in degrees \(6\) through
\(13\); that finite check cannot establish the universal
blowup theorem, its modular intersection identity, or an
exhaustive secondary-indeterminacy classification.
The latter has the concrete missing-height-three defect
recorded above. The historical VGIT source is therefore
**partially integrated**, with the rank-drop and prime
dichotomy preserved and the stronger blowup assertion
unpromoted.

Both historical verifiers are absent from \`main\`;
their original branch and exact paths are retained in
this tracker to avoid silently losing the only reported
reproducibility artifacts. This is not an instruction
to reintroduce all historical scripts indiscriminately.


## Final disposition — 69/69 historical mathematical sources adjudicated

Final decision (2026-11-17): Both Gemini-derived sextic/VGIT candidates were rejected for active-corpus inclusion. The claimed exhaustive sextic certificate does not check all 153 weight pairs; the VGIT modular-intersection proof lacks a necessary regular-sequence hypothesis. Their provisional canonical additions were withdrawn, and the temporary proof-gates investigation was deleted. The historical source commits remain available in Git. No new characteristic-zero STCI exclusion is asserted.

**Accounting:** 69/69 mathematical-source disposition decisions made; **two contain unresolved mathematical proof gates**. The historical recovery audit may be closed without claiming those two gates solved. PR #146 remains unmerged pending ordinary review/merge; do not delete the recovery branch containing the original verifiers before their needed content is preserved.


**Final override:** Any earlier text in this temporary tracker recommending preservation, promotion, or further investigation of the two Gemini-derived sources is superseded by the rejection decision above. Independently established prior results remain unaffected.
