# PR #77 cross-family consistency audit — October 26, 2026

## Coverage and method

GitHub comparison of `main` with `research/promotion-adjudication-cr01-05-cr09-11-2026-10-26` returned **93 changed paths and 85 ahead / 0 behind** before the present audit corrections. These counts are snapshot values, not immutable branch totals. The changed-path families include claim/adjudication/manifest documentation, source notes, computation sources and saved outputs, and scoped canonical result files. The comparison is **not** a complete recursive inventory of unchanged historical material. No local execution of Macaulay2, Python certificates or tests was performed.

## Findings and corrections

1. **Canonical index and evidence paths:** R-0032 through R-0036 are linked in `research/results/INDEX.md`; their recorded proof and independent-audit paths all resolve in GitHub. R-0032–R-0036 acceptance is documented in `HISTORICAL_STRUCTURAL_ADJUDICATION_2026-10-26.md`.
2. **Navigation:** `research/STATE.md`, `research/FRONTIER.md`, and `research/INDEX.md` link to `STRUCTURAL_PROMOTION_NAV_2026-10-26.md`, which distinguishes theorem scopes from remaining open cases.
3. **Historical manifest stale count:** its original 31-result census is a dated snapshot. A later overlay now identifies 36 result records; no claim of complete current-tree enumeration is made.
4. **Promotion queue PQ-03 stale status:** the explicit smooth residual example was already promoted as R-0023, despite the older PQ-03 row saying Pending. The row now identifies the fixed-example promotion and explicitly disclaims generality.
5. **CR-12/13 wording:** the earlier broad HOLD is superseded *only* for the local comparison R-0030 and prescribed characteristic-two fourth equation R-0031. The general normal-Koszul spectral-sequence packaging and existence of supported punctual defect remain open or provisional.
6. **Fixed sextic certificate:** CR-09 source/log inspection and two saved implementations agree on rank 683, but this review did not rerun the certificate. R-0025 remains restricted to the selected carrier and degree-16 mate problem, not a general sextic theorem.
7. **Fixed-boundary ranks:** affine boundary rank 19, projective boundary rank 18, node rank 5 and combined rank 24 use different maps/conventions; this is not a numerical contradiction after the recorded reconciliation.
8. **K3 proof and quartic exclusions:** the alternative (4,4) proof is attached to R-0022 without a duplicate ID; R-0001 remains the complete fixed-C0 integral quartic-carrier exclusion.
9. **Open scope boundaries:** symbolic-ribbon root acceptance, quintic endpoint, degree-15 fixed subfamily, higher normal-carrier Cartier indices, moving first relations, positive defects and non-Cartier normalization cases are not silently promoted.
10. **Historical source completeness:** the Ultra and Space Curves path indexes are retained. A fresh nontruncated recursive current-head tree inventory and machine-checkable reconciliation remain outstanding; no deletion is authorized.

## Release gates not represented as complete

- Full automatic YAML/schema and dependency validation across all 36 result records has not been executed.
- Computational evidence has been inspected rather than independently rerun.
- Complete recursive historical file-tree reconciliation remains outstanding.
- This review branch is not merged into main; PR review and CI outcomes must be checked separately.

## Conclusion

The five new structural records are linked to acceptance and source evidence, and the identified stale queue/manifest navigation statements have been corrected. No unrestricted characteristic-zero STCI theorem is claimed. This is a **documentary consistency pass with explicit residual verification gates**, not an unconditional all-files or all-certificates verification.
