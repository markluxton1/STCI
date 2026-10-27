# Mathematical consolidation: claim-to-evidence preservation manifest

**Status:** working source-retention audit on `restructure/mathematical-consolidation`. This file records *verified source existence and provenance*, not a new mathematical theorem or independent proof validation. The canonical claim-to-subject map is [MATHEMATICAL_CONSOLIDATION_CLAIM_HOME_MATRIX.md](MATHEMATICAL_CONSOLIDATION_CLAIM_HOME_MATRIX.md).

## Verification basis

- Branch HEAD when checked: `105771ffd1fddb68ea979a672b53918773197376`.
- Recursive Git tree `96e15e8e33b955ebdd27686837ccdc32e5815391` was **not truncated** (4,338 entries). Its presence confirms repository paths at that commit, but not content validity.
- The eight files below were additionally fetched directly on the working branch and their blob hashes recorded.
- No source has been deleted or moved. Do not interpret this partial manifest as deletion authorization.

## Verified evidence objects (first tranche)

| Canonical claim | Evidence role | Verified branch path | Git blob SHA | Note |
|---|---|---|---|---|
| R-0001 | Accepted assembled proof | `research/notes/2026-10-11-session-all-quartic-results-acceptance.md` | `d7d8580131e3e69c611e307a4e0d3b16d75d69b1` | Matches blob ID preserved in canonical record; source available on working branch |
| R-0001 | Independent dependency/coverage audit | `research/notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md` | `5d3d2aa936f74195a569063ca21395ee582131dd` | Also matches canonical recorded blob ID |
| R-0003 | Proof with embedded independent reviews | `research/notes/2026-10-13-generalization-conductor-theorem.md` | `4f002fa599d6ce658e2276851831bc34b4aebb98` | Intro names `split_unit_audit` and `cartier_lattice_audit`; canonical `independent_audits: []` reflects lack of *separate* audit file |
| R-0023 | Independent smooth-residual example audit, also listed as evidence | `research/notes/2026-10-25-ci-cycle-smooth-residual-audit.md` | `76f4117ba42483606cd1673aa90783ca438a818d` | File explicitly identifies independent audit agent |
| R-0023 | Independent line-degeneration example audit, also listed as evidence | `research/notes/2026-10-25-ci-cycle-line-degeneration-audit.md` | `d3ba0762fdde89928e7e860a3b174c53a48d5443` | File explicitly identifies independent cycle-notebook reviewer |
| R-0036 | Proof and review combined | `research/notes/2026-10-14-generalization-pointwise-conductor-socle-independent-audit.md` | `6a515e23dcd1c43b1acdac06b419e46e9a0724f4` | Intro describes new proof plus independent review; evidence/audit dual role |
| R-0036 | Additional independent review | `research/notes/2026-10-14-generalization-transverse-socle-independent-audit.md` | `9b4c19aff090d42a2f364297c7490e98d8c913f4` | Related transverse-socle input, not automatically independent replication of entire R-0036 |
| R-0025 | Macaulay2 input | `research/computations/endpoint4_fixed_m2_2026_10_25.m2` | `84d988eb8cc1f413c4d461b31fa27f76dbdc4807` | Saved source present; no execution performed in this check |

### What this resolves

1. **R-0001 branch-retention concern partially resolved.** Its two principal cited historical-branch blobs exist on the working branch at the **same exact blob IDs**. Before branch deletion, also check its third factor audit and the deeper component proof graph; these two files alone do not certify full proof closure.
2. **R-0003 independent-review provenance clarified.** The proof note itself says it contains independently reviewed material, even though no separate audit path is in canonical front matter. Preserve the note; do not invent a separate audit artifact or silently change status.
3. **R-0023 audit-role overlap clarified.** Both dual-role files present themselves as independent audits of exact examples. The duplicate role in metadata is real, but is not evidence that the work lacked independent review. Each file should count once in a deduplicated evidence inventory.
4. **R-0036 review roles need separation.** The pointwise note combines proof and review; the transverse note verifies a related input. Their roles must not be flattened into two independent full-theorem replications.
5. **R-0025 saved Macaulay2 input survives.** Source existence is not a fresh replay or a verification of saved output.

## Preservation contract

For each of the 36 canonical results, retain a directed chain:

`R-ID -> exact theorem scope -> source proof(s) -> inherited inputs -> independent review(s) -> accepted-in decision -> reproducible computational inputs and outputs (where applicable)`.

Represent shared files once and link them from every dependent claim. Record whether a source is a proof, independent review, review embedded in proof, adjudication, script, saved output, or inherited premise. Record actual replay separately. Do not confuse an existing file with an independently validated theorem.

## Remaining verification tasks

1. Parse all 36 canonical YAML evidence/dependency/audit/acceptance fields and check **every referenced path** against a nontruncated branch tree; investigate missing paths or refs rather than assuming they are lost.
2. Traverse inherited proof notes and branch/blob references (especially R-0001, R-0022, R-0035); determine whether each essential component is retained on a stable ref.
3. Verify paired script/output/README paths for computational claims and preserve exact source/command/output provenance.
4. Identify unique mathematical content in unpromoted and legacy files before any deletions.
5. Only then replace provisional thematic syntheses with permanent subject chapters and retire duplicates.

**Completion status:** 36/36 canonical records have metadata/scope review in the matrix; this manifest has **8 directly fetched evidence objects**, not an exhaustive claim-to-evidence closure audit.
