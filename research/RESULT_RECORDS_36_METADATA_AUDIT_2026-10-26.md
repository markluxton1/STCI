# Canonical 36-result metadata and presentation audit — 2026-10-26

Scope: GitHub-only review of all 36 files linked in `research/results/INDEX.md`, against `research/RESULT_SCHEMA.md`. This checks the visible record metadata and body structure, not mathematical correctness or a fresh computational rerun.

## Verified across all 36

- Exactly 36 indexed R IDs, R-0001 through R-0036, with no gaps or duplicates.
- Each index target resolves to a file on the adjudication branch; each YAML `id` agrees with the index.
- All records have the thirteen schema fields: `title`, `kind`, `status`, `scope`, `statement`, `dependencies`, `evidence`, `independent_audits`, `accepted_in`, `legacy_ids`, `supersedes`, `superseded_by`, `limitations` (plus `id`).
- All observed `kind` and `status` values are within the declared schema vocabularies. R-0014 and R-0015 are exact reductions; the remaining records use `proved` status, including reductions R-0004 and R-0007.
- All records have substantive body text, but headings differ across generations. Schema-prescribed seven headings appear verbatim in R-0020 through R-0031 and R-0001; many older records and R-0032 through R-0036 use consolidated headings or unheaded prose. This is a **presentation discrepancy**, not evidence of an invalid theorem.

## Findings requiring separate verification

1. **R-0003:** `independent_audits: []`. Acceptance points to a dated audited state, but no independent audit is listed in the record. Determine whether independent proof review exists before claiming the record has that evidence.
2. **R-0025:** evidence, audit and acceptance all point to the CR-09 certificate-inspection report. That report expressly did not rerun the finite-rank calculation. The index correctly marks the saved-certificate qualification; an independent replay remains a distinct gate.
3. **R-0032:** the body is unheaded despite the seven-heading schema recommendation. R-0033–R-0036 have compressed three-heading bodies. Normalize presentation only if useful; preserve precise hypotheses and accepted proof scopes.
4. **Older records:** R-0002–R-0019 use heterogeneous headings and several source URLs on historical branches. The schema explicitly permits historical branch URLs with disclosure; those URLs require a separate live-target verification rather than being treated as local-path failures.
5. **Dependencies:** this pass observed declared dependency IDs but did not yet complete an independently checked graph/cycle and every evidence-target validation. Do not describe those as passing.
6. **R-0004 and R-0007:** `kind: reduction` with `status: proved` is allowed by the schema; reviewers should confirm the index descriptions do not imply a broader theorem than the actual reductions.

## Disposition

**Metadata presence and index/ID consistency pass.** Independent mathematical proofs, computational reruns, complete source-link validation, and a full dependency graph check remain distinct gates. No result is demoted or silently broadened by this audit.
