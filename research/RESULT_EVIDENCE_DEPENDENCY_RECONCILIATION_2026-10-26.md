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
