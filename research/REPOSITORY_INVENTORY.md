# Repository inventory and consolidation staging

Organization audit dated 2026-10-17. **No mathematics was re-audited and no evidence files were deleted.**

## Verified GitHub tree observations

- `main` recursive Git tree: **149 tracked blobs**, not truncated; no blob over 50 MB. Largest tracked file is `research/RESEARCH_RECORD.md` (~161 KB).
- `main` has 55 tracked files under `research/computations/`, 43 under `research/notes/`, and 17 under `research/results/` (counts include README/index files).
- Ultra branch `research/ultra-resume-2026-10-06` has a **different top-level layout**: `computations/`, `validation/`, and `research/`. Its `research/` directory includes dated `AUDITED_STATE`, `RESEARCH_UPDATE`, `SUCCESSOR_HANDOFF`, `CODEX_RESUME` files, and `research/validation/`.
- GitHub comparison of `main` against Ultra reports the branches **diverged** (Ultra 38 commits ahead, 118 behind); its file list reaches **300 entries** and may be capped. This is **not** a complete file-by-file inventory of Ultra.
- Prior failed GitHub push reported `research/validation/2026-10-13-generalization-quintic-h3/support32-witness.txt` as 102.67 MB, above GitHub's 100 MB per-blob limit. This is a reported push failure, **not evidence that the oversized file is tracked in current `main` or the remote Ultra tree**.

## Verified navigation link spot-check

On `main`, inspected local Markdown links in `README.md`, `AGENTS.md`, `research/INDEX.md`, `research/MAINTENANCE.md`, `research/results/INDEX.md`, `research/certificates/README.md`, and `research/open/README.md` against the recursive Git tree. **No missing local target was found in these seven files.** This is not a full link-checker run; anchor links and other Markdown files were not validated.

## Duplicate entry points and history

The branch layouts contain multiple dated state snapshots, handoffs, and updates. These are **overlapping genres of documentation**, not verified byte-identical duplicates. Treat them as historical provenance, not competing current homepages.

- Canonical reading route: root README -> `research/INDEX.md` -> relevant result/question -> source proof and audit.
- `research/STATE.md` and `research/FRONTIER.md` remain working summaries with acknowledged reconciliation debt.
- `research/RESEARCH_RECORD.md`, dated snapshots, and successor handoffs are historical records. Do not delete or rename them until inbound references and preservation needs are checked.

## Coherent Ultra intake batches (proposed, not yet imported)

1. **History and provenance:** dated audited states, updates, handoffs, and literature changes. Preserve original path mapping; prefer archive copies/manifest rather than overwriting main summaries.
2. **Source notes and audits:** move or copy as a coherent provenance-preserving batch; check path collisions and relative links before committing.
3. **Computations and validation:** import source scripts, small exact certificates, and manifests; review output size and regeneration procedures first.
4. **Final canonical reconciliation:** only after the source material is available and independently reviewed. This is deferred, not implied by importing files.

Never merge the Ultra branch wholesale. Avoid replacing existing main files solely because Ultra has newer timestamps. Record any path moves in a mapping file and preserve historical Git references.

## Outstanding verification

- Run `python3 scripts/check_markdown_links.py` in full local checkouts of both branches.
- Complete Ultra recursive tree inventory (including blob sizes), not just the 300-file comparison.
- Resolve relative links after any actual imports.
- Check large-file history and whether the previously rejected 102.67 MB witness is still present in **local** unpushed commits.

## 2026-10-17 inventory continuation

The Ultra source-note index covers 356 direct files. The [computation index](archive/ULTRA_COMPUTATIONS_INDEX.md) enumerates 427 direct files in Ultra `research/computations/` with byte sizes and extensions; the [validation index](archive/ULTRA_VALIDATION_INDEX.md) enumerates 106 immediate validation subdirectories, **not their recursive contents**. Five additional scripts exist at top-level Ultra `computations/`, and a separate top-level `validation/` tree exists. These are not yet in the detailed file index. No large remote Ultra computation file in the 427-file directory listing exceeds 1 MB; this says nothing about nested validation outputs or unpushed Git history.

## Recursive Ultra validation audit

The [complete recursive validation tree inventory](archive/ULTRA_VALIDATION_RECURSIVE_INVENTORY.md) enumerates **2,168 tracked files** across **106 top-level directories**, with total Git blob sizes of **175,927,123 bytes** (compressed artifacts measured compressed). The largest are two approximately 50 MB gzip witness files and one 22.4 MB uncompressed witness. The tree response was not truncated. This does **not** establish the status of locally rejected, unpushed 102.67 MB files. See the artifact policy before importing.
