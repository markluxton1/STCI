# Containing-intersections research validation

Date: 2026-10-27. Branch: codex/intersections-containing-quartic-2026-10-27.
Base main commit: 9d734e1b03dc2de1faf3d2497ce2916cec5c4dac.

This records validation of the [integrated vision](../../notes/2026-10-27-containing-intersections-research-vision.md).
New mathematical deductions are independently reviewed provisional work, not canonical promotions.

## Mathematical reviews

- [Global containing-intersections audit](../../notes/2026-10-27-global-containing-intersections-audit.md): PASS for all-degree attachment dominance, generic residual geometry and classical Rao-module calculation, retaining inherited reviewed-provisional premises.
- [Formal visibility audit](../../notes/2026-10-27-formal-residual-visibility-audit.md): PASS for fixed-twist extension, power-containment equivalence and finite-jet injectivity, with no existence assertion.
- [Characteristic interface audit](../../notes/2026-10-27-positive-characteristic-interface-audit.md): PASS for integral flatness, group-scheme cycle, endpoint completeness and characteristic-coprime attachment divisor.
- [Integration audit](../../notes/2026-10-27-intersections-integration-audit.md): PASS for fixed-degree rank strata, actual coefficient constraints, sextic Plücker locus and final synthesis. A residual-arithmetic-genus wording correction was incorporated; once-linked and whole-primary residuals remain distinct.

## Exact new computations

- The standard-library higher-degree boundary verifier passed 27 cases: (4,5), (5,4), and every 5<=a,b<=9. Generated JSON agrees with the saved output. The all-degree proof does not rely on extrapolating from these samples.
- The standard-library mu-q verifier passed 47 two-chart/lattice identities and corroborated 11 inherited fixed-carrier minima. Those corroborations are not new theorems.
- The new Macaulay2 mu-q verifier passed global colon, scheme-union, residual-degree and attachment-divisor checks for q=3,4,7. It verifies those exact examples.
- The bounded additional rational sextic attempt verified properness and residual degree32/genus112, then was interrupted during the scheme-union comparison. Its preserved partial log is explicitly not a smoothness or reduced-attachment certificate. The general geometric proof has separate independent review.

No inherited computation was replayed as a substitute for retrieving accepted evidence.

## Repository checks

- python3 research/computations/validate_records.py: **Checked 37 canonical records; 0 error(s)**.
- Local Markdown targets in the six modified navigation files and the ten new research/audit notes: **320 checked; 0 missing**.
- git diff --check: passed before staging. Staged whitespace validation is checked separately before the local commit.
- Canonical result and question files were not modified. No mathematical status was promoted.
- The pre-existing unrelated untracked file-manifest.txt was left outside the research change.

Source access, bounded search coverage and inaccessible originals are recorded in the [literature refresh](../../notes/2026-10-27-containing-intersections-literature-refresh.md).
