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

## Complete first-level path-existence check (2026-10-27)

**Branch:** `restructure/mathematical-consolidation`, HEAD `c9082e8c7a6a5fd7ed765d0977a298c252a3f4d5`; recursive Git tree `7d0b34b1d409fe9c9b876ebfc6b6e9b07ed4e225` (**4,339 entries; not truncated**).

I re-read all 36 canonical YAML front matters and transcribed the `evidence`, `independent_audits`, and `accepted_in` paths into a deduplicated existence check against the recursive Git tree. **Result: 115 distinct cited paths checked, zero missing.** The check includes notes, adjudications/reconciliations, computation scripts and saved JSON/text outputs, and the ideal-filtrations validation README. Duplicated paths were counted once.

This is **first-level reference closure**, not full transitive proof closure. In particular, an evidence note may itself refer to a source script, external branch/blob, inherited theorem, or historical proof not named in the canonical YAML. Those second-level references have not all been checked. The check was based on manually transcribed canonical path lists; an automated YAML parser should independently repeat it before destructive cleanup.

### Practical consequences

- **No immediate broken canonical evidence link** was detected in the 36-record front matter. This removes one straightforward reason to retain old branches, but **does not** establish that all historical proof dependencies have been preserved.
- **Do not delete proof notes, scripts or saved outputs on this basis alone.** Path existence does not verify content, mathematical correctness, reproducibility, or whether a different file contains unique supporting arguments.
- For R-0003, an empty `independent_audits` list is compatible with the embedded reviewer record in its existing proof note; preserve this distinction.
- For R-0023 and R-0036, the same file may occupy multiple evidence roles; count unique objects once while retaining the distinct relationships.

### Remaining gates, in order

1. **Transitive proof closure:** inspect links and named inherited lemmas inside proof/audit/adjudication files, beginning with R-0001, R-0022 and R-0035. Verify stable retained locations for historical-branch blobs.
2. **Computational replay closure:** record which scripts actually ran, with commands, outputs, environment and source SHA; keep saved-certificate-only status where appropriate.
3. **Unique-content review:** compare legacy and exploratory mathematical arguments with the proposed permanent chapters; preserve failed implications and their counterexamples without a chronological archive.
4. **Deletion eligibility:** mark a file redundant only when its unique mathematical content and evidence role have both been captured elsewhere with traceable references.

**Audit state:** canonical metadata 36/36; first-level cited path existence 115/115; transitive proof/evidence closure **incomplete**.

## Transitive proof dependencies: first layer

Checked R-0001, R-0022 and R-0035 and their main proof notes. Against the complete Git tree at commit `5485c43`, **30 selected second-level source paths were present, zero missing**. This checks availability, not proof validity.

**R-0001.** The October 11 acceptance organizes the integral quartic exclusion into six cases: normal carriers; nonnormal sectional genus 0; genus 1; genus 2 bisection; genus 2 nonendpoint trisecant; genus 2 endpoint trisecant. The last case invokes local ADE corrections and doubled-horizontal arguments. Preserve this case structure and its coverage audit. The two primary accepted proof/audit blobs also exist on the current branch, although canonical body links still target an older research branch.

**R-0022.** The filtered (4,4) argument distinguishes the degree-three-defect case from the primitive-triple case and uses nonzero cubic-contact determinants of actual quartic pencils. The proof note records an incorrect earlier quadratic-contact sign and an overgeneralized fixed-ruling-line shortcut; preserve the corrected reasoning. The canonical **body** additionally cites an alternative K3/lattice proof and its audit, not included in the YAML evidence fields. This is a body-level preservation dependency, not a newly checked proof.

**R-0035.** The normal-carrier source develops local detection of class-group torsion by Cartier indices along the ample rational curve, via a connected cyclic-cover argument. It distinguishes necessary local-index constraints from actual global torsion. The index/socle compatibility audit and inherited quadratic-direction argument are part of the proof chain. Preserve the mechanism, not just the bounded-index numerical conclusion.

**Conclusion.** Canonical YAML alone does not encode all proof dependencies. Source-body links and inherited inputs must be traced before any deletion. This first-layer check is not exhaustive; no files have been removed or canonical theorem statuses changed.
