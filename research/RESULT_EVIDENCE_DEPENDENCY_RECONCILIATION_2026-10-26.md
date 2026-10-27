# Result dependency and evidence provenance reconciliation — October 26, 2026

## Scope and verification

GitHub connector read of all 36 indexed canonical result records. All metadata dependency IDs resolve among R-0001 through R-0036, and the directed dependency graph has no cycle. The metadata index has 36 unique targets and matching IDs. **95 source/audit/acceptance paths** appearing in the extracted record references were successfully retrieved from the present adjudication branch (some references are repeated across records). This is a path-presence check, not an independent mathematical audit, and not a byte-for-byte verification of the original historical Git blobs.

## Historical branch provenance issue

Some metadata references use `https://github.com/markluxton1/STCI/blob/research/ultra-resume-2026-10-06/...` or `.../blob/codex/normal-cone-rigidity-2026-10-19/...`. GitHub branch search returned no branches for either name, and a direct fetch on the Ultra ref returned missing-ref errors. The corresponding cited `research/...` source files **do exist on the current adjudication branch**. Accordingly, the source files are available, but the historical branch URLs should be stabilized (prefer immutable commit-pinned URLs, or current canonical relative paths with an archival provenance note). Do not claim that the old branch links themselves have been validated.

## R-0003 — independent audit provenance

`research/results/fixed_carrier_conductor_criterion.md` has `independent_audits: []`. Its cited `research/notes/2026-10-13-generalization-conductor-theorem.md` explicitly identifies two independent reviewers (`split_unit_audit` and `cartier_lattice_audit`) and contains an `Audit record` section describing their checks. This supports the statement that independent reviews were **reported within the proof note**, but does not identify separate independently retrievable audit files. Retain the empty field pending either a separately preserved audit artifact or a schema convention allowing an explicitly labeled embedded audit record. No mathematical demotion is inferred.

## R-0025 — saved computation

The fixed-sextic result cites `CR09_CERTIFICATE_INSPECTION_2026-10-26.md` as evidence, audit and acceptance. Its finite-rank 683 certificate is corroborated by saved independent implementations and outputs, but the October 26 review did not rerun them. An independent replay should record exact source revision, environment, modulus, sample points, rank, nullity, kernel inclusion and output hashes; any rerun result should be attached as a new audit artifact. Scope remains the selected sextic and degree-16 mates.

## Validator

`research/computations/validate_result_records.py` is now a reusable Python/PyYAML validator for metadata, index completeness, local source availability, dependency IDs, and cycles. **It has been committed but not executed** in this GitHub-only review. Its historical-URL check resolves the referenced source path locally and emits a warning; it does not verify that the old URL is live.

## Outstanding

- Run the validator in CI or an approved execution environment, then fix any issues it reports.
- Stabilize old branch URLs in result metadata, preserving provenance.
- Verify supersession relations and external evidence semantics as the schema evolves.
- Independent mathematical and computational review is separate from these checks.

## Closure disposition

The October 26 structural/provenance audit is **closed with disclosed verification debt**, not certified as an independently reproduced proof of all 36 results. No theorem status is changed by this documentary review. Follow-up work is limited to running the committed validator, stabilizing historical branch URLs, locating a separately preserved R-0003 audit if available, and independently replaying R-0025 when computational certification is required. PR #77 remains subject to its normal review and merge process.

## Final execution update — October 26

- The repository's pre-existing `research/computations/validate_records.py` and the additional `research/computations/validate_result_records.py` were both **executed successfully** by the existing `Canonical research records` GitHub Actions workflow, [run 40434021004](https://github.com/markluxton1/STCI/actions/runs/40434021004), job `validate`.
- The same run's `replay-r0025` job completed successfully: fresh Python/C++ construction of the 690-by-969 matrix, rank 683, nullity 286, annihilation of all 286 known multiples, and exact match to saved matrix SHA-256 `a3e546424d11200e1d8075c7f9d5d342787bd925a303901bd2b33b2661f56445`. Output was uploaded as a workflow artifact. This is an independent implementation replay, not a fresh Macaulay2 execution.
- The older historical-branch references in canonical result **front matter** R-0001 through R-0011 were replaced with current local `research/...` evidence paths where applicable; narrative historical links remain as provenance. This avoids relying on absent branch refs for metadata resolution.
- R-0003's independent reviewers are explicitly described in its source proof note. No separate audit file has been identified, so `independent_audits: []` is intentionally retained and the distinction is recorded as a limitation.
- The new standalone workflow was removed in favor of extending the existing `.github/workflows/research-records.yml`. Both validators and the replay now belong to the established PR CI path.

**Disposition:** the targeted record-schema, dependency, evidence-availability, and R-0025 replay gates are closed. Full independent mathematical re-proving of all 36 results and exhaustive historical source-tree inventory are not claimed. The normal PR review and merge decision remain separate.
