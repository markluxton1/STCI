# Documentation and maintenance review — 2026-10-24

**Status:** documentation maintenance, not a mathematical promotion or an independent proof audit. Review baseline: `main` at `46a0ff3`; relevant pending work: `codex/quartic-p4-ruled-surfaces-2026-10-24` (two commits ahead of that baseline) and discussion-reconciliation PR #71.

## Checked for content and authority

- `AGENTS.md`: retrieval instructions, navigation, status discipline. Fixed a stray literal newline escape at EOF.
- `research/INDEX.md`: entry-point navigation, provisional October 24 notes, pending branch/PR visibility. Added direct pointers to unmerged work without treating it as merged or promoted.
- `research/STATE.md`: retained all existing STCI result scopes; added an explicit unmerged ruled-surface evidence notice. No change to R-0001–R-0022 or to the open unrestricted characteristic-zero question.
- `research/FRONTIER.md`: made historical priority headings unambiguous under the voluntary intrinsic-geometry pause.
- `research/INTRINSIC_GEOMETRY_INTERLUDE_2026-10-24.md`: removed an obsolete 'not pushed' retrieval warning; corrected the misleading suggestion that the four characteristic-zero curves all lie on the same smooth quadric; linked the branch synthesis and discussion PR.
- `research/AUTHORITY.md` and `research/results/INDEX.md`: inspected; no result promotion, renumbering, or authority-policy change justified by these documentation updates.

## Reconciliation findings

1. The unmerged ruled-surface branch includes a same-center smooth cubic-scroll lift in `P^4`, normalization and conductor work, a common `F_4` model for the four characteristic-zero curves, explicit elementary transformations, and arithmetic group-scheme treatment. Its synthesis reports independent audits and scripts; **this maintenance PR does not independently rerun those scripts**.
2. The original quadric `Q`, the common four-section ruled model, and the conormal normalization must not be conflated merely because some are abstractly products. The four curves have individual containing quadrics; the common carrier is not one smooth quadric.
3. PR #71 preserves discussion-only incidence/duality questions and the failed polarity identification. Keep it separate from this navigation/maintenance PR; avoid duplicating its proposed note until it merges.
4. The branch's `research/INDEX.md` adds its own synthesis link. After merging that branch, replace the external branch pointer in `research/INDEX.md` with a relative link, remove the 'unmerged' notices in `STATE.md` and the interlude, and reconcile overlapping navigation edits. Likewise update PR #71 links when it merges.

## Validation boundaries and follow-up

This was a focused inspection of the canonical entry points and the new branch's synthesis/independent-comparison report, **not a full repository-wide link crawl or complete line-by-line proof review**. No claims are made about every historical archive file, every citation target, or the correctness of all computations. A subsequent integration pass should (a) run the canonical record validator, (b) check relative Markdown links across the merged tree, (c) execute the branch's exact Python and Macaulay2 checks in a suitable environment, (d) resolve branch overlap with PR #71, and (e) inspect the full conductor/arithmetic arguments before any promotion decision.

No STCI theorem or frontier question was closed by this maintenance review.
