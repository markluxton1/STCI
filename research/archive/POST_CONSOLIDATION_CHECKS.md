# Post-consolidation link and duplication checks

The first manual pass checked 108 local Markdown links across 12 principal navigation files on 2026-10-17 and found no missing destinations. This is a scoped result, **not** a claim that all repository links work.

Run `python3 research/computations/check_markdown_links.py --core` for those entry points, or omit `--core` to scan all tracked Markdown files. The checker uses the Python standard library, reports missing local destinations, and returns nonzero on failure. It does not validate external URLs, Markdown fragment anchors, dynamically generated links, or every complex Markdown syntax; review reported exceptions before editing historical evidence.

The October 17 branch reconciliation preserved 69 previously absent source paths and 53 alternative versions under `research/archive/branch-reconciliation/`. An initial exact-blob inventory found 14 redundant copies *within that archive*, but these copies also record branch membership. **Do not remove them without a provenance map.** Validation snapshots and isolated verifier trees may intentionally repeat files for reproducibility.

The current canonical reading path remains [STATE](../STATE.md), [FRONTIER](../FRONTIER.md), and [AUTHORITY](../AUTHORITY.md). Historical versions are evidence, not automatically accepted results.
