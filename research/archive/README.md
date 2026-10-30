# Research archive

This directory preserves dated handoffs, reports, branch alternatives, and other provenance. **Archived content is not automatically an accepted mathematical result.**

For current claims read [the canonical state](../STATE.md), [current frontier](../FRONTIER.md), and [authority rules](../AUTHORITY.md).

## Post-consolidation layout

- [Space Curves I–VI intake](space-curves-2026-10-19/README.md): selective external-project evidence, provenance hashes, proposed uses and review boundaries; no canonical promotions.
- [research notes](../notes/): original mathematical notes; the obsolete filename-keyword index was retired.
- Ultra computations index (historical file not present on this branch); original scripts remain at [research/computations](../computations/).
- Ultra validation inventory (historical file not present on this branch); original evidence remains in [research/validation](../validation/).
- [Ultra intake](ULTRA_INTAKE.md) and [dated reports](reports/): older handoffs and snapshots.
- Ultra conflicting versions: consult the [branch reconciliation archive](branch-reconciliation/) for preserved alternatives; the former `ultra-conflicts/` directory is not present on this branch.
- [Other branch reconciliation](branch-reconciliation/): original branch-specific alternatives, organized by source branch. Paths within these directories are historical source paths, **not live canonical paths**.

## Duplication and provenance

Some archived files are byte-identical across multiple branch directories, and validation directories may contain intentionally repeated verifier snapshots. Their separate paths record provenance, execution context, or historical branch membership. Do not delete or deduplicate them without recording a replacement provenance map and checking incoming links. A matching blob does not establish that two mathematical claims have the same status.

The branch reconciliation imported missing research files at their original paths and preserved conflicting versions without overwriting main. It did **not** merge all branch commit histories or validate every historical result. The [repository inventory](../REPOSITORY_INVENTORY.md) and Ultra indexes were produced before consolidation and should be read as dated snapshots, not live counts.
