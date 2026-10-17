# Repository maintenance plan

This is a **repository-organization checklist**, not a mathematical research agenda. The immediate goal is a readable, auditable working repository. Final mathematical exposition and exhaustive theorem reconciliation are deferred.

## Current conventions

- `README.md`: short project overview and first entry points.
- `research/INDEX.md`: compact directory; no theorem descriptions appended here.
- `research/results/`: individually reviewed, scope-limited result records.
- `research/questions/` and `research/open/`: precise questions and broader topic navigation.
- `research/STATE.md` and `research/FRONTIER.md`: working summaries; not independent proof authority.
- `research/notes/`: source proofs and independent reviews, preserved with provenance.
- `research/computations/` and `research/certificates/`: executable checks and their stated scope.
- `research/archive/`, dated handoffs, and chronological records: historical provenance, not default starting points.

## Practical cleanup queue

- [ ] Inventory top-level and research directories, including the Ultra branch; identify duplicate entry points, stale handoffs, and orphaned files **without deleting evidence**.
- [ ] Check links from README, research indexes, result/question records, and certificate maps. Record broken links before moving any files.
- [ ] Audit overlapping summaries and mark superseded navigation. Keep source proofs and audit notes intact.
- [x] Add a reproducible **read-only** local Markdown link checker: `python3 scripts/check_markdown_links.py` from the repository root (Python 3.9+). It checks paths in tracked Markdown files, reports missing local targets, and exits nonzero on issues. It deliberately does not validate remote URLs, fragment anchors, or dynamically generated pages. **The checker has been added but a full repository run has not yet been verified.**
- [ ] Run the checker on `main` and Ultra, triage false positives, and repair confirmed broken links in a separate reviewed PR.
- [ ] Check computation directories for large generated outputs and establish a Git/LFS/ignore policy that preserves reproducibility without blocking pushes.
- [ ] Decide how reviewed Ultra material enters main in **coherent organizational batches**, not one theorem per PR.
- [ ] Only after structure stabilizes: reconcile all claims, notation, and final exposition.

## Change discipline

Prefer small, reversible organization-only changes. Do not rename or delete source files casually: existing links and provenance depend on them. Do not merge the Ultra branch wholesale. For each organizational PR, state which paths changed, which links were checked, and which mathematical claims were deliberately left untouched.

**PR #12**, if still open, is a theorem-promotion PR from the previous workflow. Review or merge it independently; do not treat it as part of this maintenance cleanup.
