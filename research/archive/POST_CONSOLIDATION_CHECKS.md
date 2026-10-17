# Post-consolidation link and duplication checks

The first manual pass checked 108 local Markdown links across 12 principal navigation files on 2026-10-17 and found no missing destinations. This is a scoped result, **not** a claim that all repository links work.

Run `python3 research/computations/check_markdown_links.py --core` for those entry points, or omit `--core` to scan all tracked Markdown files. The checker uses the Python standard library, reports missing local destinations, and returns nonzero on failure. It does not validate external URLs, Markdown fragment anchors, dynamically generated links, or every complex Markdown syntax; review reported exceptions before editing historical evidence.

The October 17 branch reconciliation preserved 69 previously absent source paths and 53 alternative versions under `research/archive/branch-reconciliation/`. An initial exact-blob inventory found 14 redundant copies *within that archive*, but these copies also record branch membership. **Do not remove them without a provenance map.** Validation snapshots and isolated verifier trees may intentionally repeat files for reproducibility.

The current canonical reading path remains [STATE](../STATE.md), [FRONTIER](../FRONTIER.md), and [AUTHORITY](../AUTHORITY.md). Historical versions are evidence, not automatically accepted results.

## Expanded navigation check (2026-10-17)

A second API-based destination check covered the 26 Markdown files in `research/results/`, `research/open/`, `research/questions/`, and `research/certificates/`: 39 additional relative links resolved to repository paths. Combined with the first 12-document check, 147 relative links across 38 documents had no missing path destinations. These checks did not validate fragment anchors or external URLs.

The `Markdown navigation links` GitHub Actions workflow now runs the **12-document core checker** on relevant PRs and pushes to main. This scoped check is intentionally blocking; the full archive checker remains available as an explicit manual command pending review of historical exceptions. The CI workflow is not evidence that the full archive has been checked.

## Full historical scan in CI

The `historical-links` workflow job runs the all-tracked-Markdown link checker on each relevant PR and main push, publishes its output as a 30-day artifact, and deliberately does **not** fail the workflow for missing historical destinations. This is an observational audit; its success status alone does not mean that all historical links resolve. Inspect the artifact and classify exceptions before rewriting dated notes or changing relative paths. The `core-links` job remains blocking.

## First full-repository CI result (2026-10-17)

[Main-branch workflow run 39067864521](https://github.com/markluxton1/STCI/actions/runs/39067864521) completed successfully. Its historical job scanned **589 tracked Markdown files** and tested **2,200 local destination candidates**, reporting **361 unresolved**. The job is intentionally informational: green CI does **not** mean zero historical exceptions.

Breakdown by *source file location*, based on the job log:

| Source location | Unresolved candidates |
| --- | ---: |
| `research/archive/branch-reconciliation/` | 224 |
| Other `research/archive/` | 65 |
| `research/validation/` | 63 |
| `research/notes/` | 9 |
| **Total** | **361** |

The nine active-path note candidates are `a-k`, `nine`, `X1-X0`, `X2-X0`, four instances of `lambda-nu`, and `a-e`. These look like mathematical notation parsed as links; inspect source context before classifying them as false positives. Archived paths can be broken **relative to their archival location** while the corresponding original source path exists elsewhere. The report therefore does not support changing 361 links blindly or deleting archived duplicates.

**Recommended follow-up:** improve parser precision with regression tests for mathematical bracket/parenthesis expressions; classify archived paths as relocated, intentionally snapshot-local, or genuinely absent; add non-destructive navigation from archive directories to the original source tree. Do not rewrite the content of proof snapshots or infer mathematical validity from a successful link check.
