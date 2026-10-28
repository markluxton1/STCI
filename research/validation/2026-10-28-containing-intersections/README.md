# Containing intersections: October 28 validation and review

Branch: `codex/intersections-containing-quartic-2026-10-27`.
Starting commit: `7b9397d`. Source synthesis:
[residual families and constructive global models](../../notes/2026-10-28-containing-intersections-synthesis.md).
**All new mathematics remains reviewed provisional work; no canonical
promotion.**

## Independent reconstruction

| Source | Independent reviewer/evidence | Outcome |
|---|---|---|
| [Normal jets and every attachment divisor](../../notes/2026-10-28-prescribed-attachment-and-normal-jets.md) | [Residual-liaison agent audit](../../notes/2026-10-28-prescribed-attachment-audit.md) | Pass; all-field sheaf-power calculation, characteristic-zero smooth construction for every divisor in the sufficient range |
| [Liaison and flat once-link families](../../notes/2026-10-28-residual-liaison-construction.md) | [Root reconstruction](../../notes/2026-10-28-residual-liaison-audit.md) and [integration review](../../notes/2026-10-28-containing-intersections-integration-audit.md) | Pass, including later relative §2.1 and Artinian recovery |
| [Blowup/Fano construction model](../../notes/2026-10-28-blowup-residual-geometry.md) | [Singular-carrier agent audit](../../notes/2026-10-28-blowup-residual-audit.md) | Pass after actual-cycle proof repair |
| [Prescribed-index carriers and residuals](../../notes/2026-10-28-singular-carrier-construction.md) | [Blowup agent audit, with root addendum](../../notes/2026-10-28-singular-carrier-audit.md) | Pass, including local graph control and explicit specialization of the new literature bound |
| [Integrated interpretation](../../notes/2026-10-28-containing-intersections-synthesis.md) | [Separate integration audit](../../notes/2026-10-28-containing-intersections-integration-audit.md) | Pass; authority, characteristic, family and two-projection boundaries retained |

The blowup review found one substantive proof gap: equality of Chow classes
alone did not prove equality of actual effective cycles. The revised source
computes at the generic two-dimensional regular local ring using the blowup
intersection formula and residue-degree weights. The independent reviewer
then reconstructed the cycle assertion. This correction is retained in the
audit; it does not rewrite an accepted proof.

## New exact computations

```sh
python3 research/computations/verify_normal_jet_freedom_2026_10_28.py
/opt/homebrew/bin/M2 --script research/computations/verify_residual_liaison_resolution_2026_10_28.m2
python3 research/computations/validate_records.py
git diff --check
```

- [Normal-layer verifier](../../computations/verify_normal_jet_freedom_2026_10_28.py)
  and [saved JSON](../../computations/normal_jet_freedom_2026_10_28.json):
  **15 exact rational rank checks pass**, normal orders 1–5 and the three
  degrees immediately around the surjectivity threshold. Fraction arithmetic
  and weight-block Taylor matrices are used; the universal theorem relies on
  the written sheaf cohomology proof.
- [Liaison verifier](../../computations/verify_residual_liaison_resolution_2026_10_28.m2)
  and [saved output](../../computations/residual_liaison_resolution_2026_10_28.txt):
  canonical-module matrix rank/grade control passes over Q; **five new
  deterministic finite-field proper links pass** their degree, genus and
  full resolution checks. No smoothness or characteristic-zero lifting of
  those samples is asserted. The all-degree resolution has a separate proof.
- Canonical metadata: **37 records, zero errors** (36 result records plus
  the question record). Canonical result/question files were not modified.
- Whitespace and relative Markdown targets are checked on the final changed
  files; the final delivery check is recorded below.

Inherited accepted certificates and reviewed cubic-model/smooth-residual
computations were not rerun. The new checks target new claims only.

## Source checks and navigation

The [focused literature record](../../notes/2026-10-28-containing-intersections-literature.md)
states exactly what was inspected and how it was used. The October 2026
Noether–Lefschetz paper remains within its Picard-group scope. Existing
Fano geometry, liaison and ideal-power vanishing are identified as such;
no claim of literature originality is established.

INDEX, MAP, STATE, FRONTIER, the decision guide and literature ledger link
the new work. The two October 27 synthesis pages point forward without
rewriting their original proofs or scope. Current direction is general
residual construction and deformation, with no compulsory bidegree and
neither characteristic-zero endpoint answer assumed.

## Final delivery check

The final sweep checked **382 local Markdown targets in 20 changed/new
Markdown files, with zero missing targets**. The new generated JSON and
Macaulay2 log exist at the linked paths. Canonical metadata reports 37
records with zero errors. `git diff --check` passes, and new text files
were also checked explicitly for trailing whitespace and final newlines.
Validation was completed in the local checkout on the requested branch
before publication.
