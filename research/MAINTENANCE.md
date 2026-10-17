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

- [x] Record a **partial, evidence-preserving inventory** of main and Ultra layouts in [REPOSITORY_INVENTORY.md](REPOSITORY_INVENTORY.md); complete Ultra recursive inventory remains open.
- [x] Spot-check seven high-traffic navigation files against the main Git tree; no missing local targets found. See [inventory](REPOSITORY_INVENTORY.md). Full check remains open.
- [x] Reconcile high-level authority and mark the result index's stale migration language. See [authority reconciliation](AUTHORITY_RECONCILIATION_2026-10-17.md). Source proofs and audit notes remain intact; full proof-by-proof re-audit is not claimed.
- [x] Add a reproducible **read-only** local Markdown link checker: `python3 scripts/check_markdown_links.py` from the repository root (Python 3.9+). It checks paths in tracked Markdown files, reports missing local targets, and exits nonzero on issues. It deliberately does not validate remote URLs, fragment anchors, or dynamically generated pages. **The checker has been added but a full repository run has not yet been verified.**
- [ ] Run the checker on a local checkout of `main` and Ultra, triage false positives, and repair confirmed broken links in a separate reviewed PR. This GitHub API pass did not execute the local checker.
- [x] Document [artifact and large-file policy](ARTIFACT_POLICY.md); inspect local rejected-push history and decide retention for the 102.67 MB witness before retrying.
- [x] Document a staged, non-destructive [Ultra intake plan](REPOSITORY_INVENTORY.md). Actual batch imports remain pending.
- [ ] Only after structure stabilizes: reconcile all claims, notation, and final exposition.

## Change discipline

Prefer small, reversible organization-only changes. Do not rename or delete source files casually: existing links and provenance depend on them. Do not merge the Ultra branch wholesale. For each organizational PR, state which paths changed, which links were checked, and which mathematical claims were deliberately left untouched.

**PR #12**, if still open, is a theorem-promotion PR from the previous workflow. Review or merge it independently; do not treat it as part of this maintenance cleanup.

## Historical-file classification

- [x] Inventory the current main Git tree and distinguish canonical navigation, evidence, validation, snapshots, and scratch material; see [provenance classification](PROVENANCE_CLASSIFICATION_2026-10-17.md).
- [ ] Make **no bulk deletions** until individual evidence dependencies and reproducibility have been verified. Identical Git blob hashes alone do not authorize deleting snapshot copies.
