# Post-consolidation link and duplication checks

The first manual pass checked 108 local Markdown links across 12 principal navigation files on 2026-10-17 and found no missing destinations. This is a scoped result, **not** a claim that all repository links work.

Run `python3 research/computations/check_markdown_links.py --core` for those entry points, or omit `--core` to scan all tracked Markdown files. The checker uses the Python standard library, reports missing local destinations, and returns nonzero on failure. It does not validate external URLs, Markdown fragment anchors, dynamically generated links, or every complex Markdown syntax; review reported exceptions before editing historical evidence.

The October 17 branch reconciliation preserved 69 previously absent source paths and 53 alternative versions under `research/archive/branch-reconciliation/`. An initial exact-blob inventory found 14 redundant copies *within that archive*, but these copies also record branch membership. **Do not remove them without a provenance map.** Validation snapshots and isolated verifier trees may intentionally repeat files for reproducibility.

The current canonical reading path remains [STATE](../STATE.md), [FRONTIER](../FRONTIER.md), and [AUTHORITY](../AUTHORITY.md). Historical versions are evidence, not automatically accepted results.

## Expanded navigation check (2026-10-17)

A second API-based destination check covered the 26 Markdown files in `research/results/`, `research/open/`, `research/questions/`, and `research/certificates/`: 39 additional relative links resolved to repository paths. Combined with the first 12-document check, 147 relative links across 38 documents had no missing path destinations. These checks did not validate fragment anchors or external URLs.

The `Markdown navigation links` GitHub Actions workflow now runs the **12-document core checker** on relevant PRs and pushes to main. This scoped check is intentionally blocking; the full archive checker remains available as an explicit manual command pending review of historical exceptions. The CI workflow is not evidence that the full archive has been checked.
