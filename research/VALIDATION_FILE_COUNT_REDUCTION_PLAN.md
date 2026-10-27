# File-count reduction: validation run packaging

Scope: tracked-file register for restructure/mathematical-consolidation, plus source inspection of the genus-two double-horizontal verifier. This is a proposed migration, not a deletion or rerun.

## Counts

- 3,840 tracked paths; 2,253 under research/validation (58.7%).
- 183 execution-record.json, 171 stdout.txt, 171 stderr.txt, 90 source.m2 under validation: **615 files**, totaling about 1.11 MB.
- 161 leaf directories contain the execution-record/stdout/stderr trio; 90 contain all four.
- 96 stderr.txt files are empty; 226 validation files have zero bytes in total.
- 437 extra validation entries repeat an existing Git blob within validation (not all safe to remove).
- Other major file-count families: computations 629, notes 545, archive 146, scratch 112.

## Verified example

research/validation/2026-10-10-genus-two-double-horizontal has execution-record.json, stdout.txt, empty stderr.txt, source.m2, run_verifier.py, and four failed-attempt subdirectories. Its runner copies a canonical computation source to source.m2, executes that copy, writes stdout/stderr and a JSON execution record. The record contains source SHA-256, command, status, exit code, assertion count, and scope. The 14 named PASS checks in stdout are more informative than an undifferentiated PASS marker.

## Proposed migration

For each *completed, independently identified run*, keep one small evidence record containing: canonical source path and SHA-256, tool/version if available, command, exit code, assertion/check identifiers, output digest, and scope. Keep canonical executable source under computations, not an extra source snapshot in each validation run. Do not discard nonempty stderr or detailed stdout until important mathematical diagnostics have been extracted. For failed attempts, preserve a concise failure mechanism and any counterexample, not every failed execution log.

Potential direct reduction: replacing 161 trios with one record each removes up to **322 paths**; where source.m2 is confirmed an exact canonical-source snapshot, another **up to 90**. This is an upper bound, not a measured safe-deletion count. More reduction is possible among empty files, redundant snapshots, and failed attempts, but overlap must be resolved.

## Guardrails

- Migration must update run_verifier.py and any scripts expecting legacy paths; do not delete outputs while existing runners regenerate them.
- Source snapshots may differ from canonical sources; verify hashes before deduplication.
- Distinguish PASS, FAIL, interrupted and exploratory runs; a historical PASS is not a fresh replay.
- Preserve the mathematical meaning and scope of failed approaches without retaining chronology for its own sake.
- Prioritize large run families (2026-10-07-continuation: 301 files; 2026-10-06-session: 193) after validating a small representative migration.

**Recommendation:** implement one representative run migration with runner updates and reproducibility check before mass editing. No files deleted in this pass.
