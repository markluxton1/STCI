# Independent audit of the October 9 frozen continuation record

**PASS — record integrity and scope routing.** This audit received the
root's explicit canonical-file freeze on October 9 and checked those
bytes without editing the canonical documents. It did not execute any
mathematical verifier or independently reprove the accepted theorems.
The [result](result.json) seals the exact canonical/input hashes and UTC
interval. The [terminal log](check_record.log) retains the successful
execution summary; the [execution manifest](execution-manifest.json)
binds its command, source, output and exit status.

The independent [checker](check_record.py) passed 1,645 recorded
integrity checks. All 212 local file links in the stated routing scope
resolve, `git diff --check` passed, and the seven frozen canonical
documents remained byte-identical throughout the check. No unexplained
latest-source, log, manifest or declared current-snapshot hash drift was
found. These are timestamped observations, not claims about later edits.

## Counts reconstructed from constituent records

| Record group | Distinct top-level source paths | Explicit executions |
|---|---:|---:|
| Retained October 6/7 baseline | 55 | 61 |
| Central continuation | 28 | 30 |
| Separately frozen strengthened Veronese revision | 0 additional | 1 |
| Independent first-endpoint completeness companion | 1 | 1 |
| Independent principal completeness companions | 4 | 4 |
| Independent second-family quadratic audit | 3 | 6 |
| **Combined** | **91** | **103** |

All 91 distinct paths have a latest PASS record. The central records plus
the strengthened Veronese execution represent 30 distinct source-byte
revisions of 28 paths. A source path, a source revision and an execution
are different counting units. Imported helpers, agent discovery work,
unindexed runs and this integrity auditor are excluded from the
mathematical-verifier total. The baseline was retained, not rerun.

The six explicit second-family audit executions consist of its isolated
field-verifier replay, its independently implemented countercheck, and
four tensor-reconstruction versions: two preparatory failures followed
by two passing versions. The copied source-owner principal transcript
does not count as another independent auditor execution.

## Frontier and continuation distinctions preserved

The reviewed documents consistently retain the following scopes:

- The universal STCI problem and the unrestricted characteristic-zero
  rational-quartic `C0` problem remain OPEN.
- The entire `e=1,d2=1` common-quartic-ancestor lane is excluded. The
  complete principal contact and projective boundary arguments retain
  the node's four-dimensional fixed-cubic space; they do not assert
  uniform quartic dimension one there. The ancestor result alone does
  not exclude higher-degree mates for a unique quartic carrier. The
  remaining nonnormal principal-carrier locus is a finite proper
  closed subset whose exact list remains OPEN.
- Every integral quartic with finite smooth normalization
  `F0,H=C+2f` or `F2,H=C+3f` is excluded as a carrier of fixed `C0` in
  characteristic zero, in every mate degree. The final accepted
  theorem has no reducedness or Gorenstein assumption on either
  actual conductor scheme. The intermediate reduced/Gorenstein
  theorem and former nongorenstein boundary are explicitly superseded.
  This does not classify all nonnormal quartic normalizations.
- The first rational `e=2,h=t` endpoint ancestor family is fully
  excluded, including its exceptional direction points and every
  affine lower lift. The second family's generic certificate initially
  retained 26 points; the two quadratic-field exclusions remove four.
  Its current unresolved locus is **22 geometric points** from factors
  of degrees **3,4,15**, each with its entire lower-lift fibre OPEN.
  Exception to an older dual certificate does not assert existence of
  an ancestor or incidence point.
- Singular normalizations, other smooth polarized normalization types,
  surviving `e=1` ancestor defects `d2=2,3,4`, other endpoint families,
  nonendpoint top zeros, higher carrier degrees and the entirely thick
  branch retain their separate stated proof obligations. Assignment of
  new research work does not add an accepted result.

The exact frontier is in
[the audited state](../../AUDITED_STATE_2026-10-07.md),
[the late root acceptance](../../notes/2026-10-08-session-late-results-acceptance.md)
and [the successor handoff](../../SUCCESSOR_HANDOFF_2026-10-07.md).
The principal, full-scroll and second-family independent proof audits
are directly linked there. This integrity note verifies their current
routing and consistent stated scopes, not their mathematics afresh.

## Historical failures and reproducibility limits

Both failed central continuation records survive. The conormal verifier
first failed because its proof-note provenance input was absent; it
then passed with the completed input closure and unchanged source
bytes. The initial elliptic verifier used the false boundary factor
`8(p+2)^3`; the corrected literal factor `8p(p+2)^2` passed in its own
source snapshot. The repair does not erase the failed record.

The original October 7 Veronese-classifier source bytes were overwritten
by the earlier addition copier. Its original digest, log and recorded
manifest transition survive; the original source bytes do not. The
current stronger revision has a separate exact source snapshot and PASS
execution. The auditor confirms this is exactly the one declared
historical byte loss, not an unexplained latest-source change. Baseline
logs that lacked original digests are checked against the later
observed seal; no original historical log digest is invented.

The older `continuation-index/editorial-integrity.json` seals a former
index digest and has no timestamp. It is outside the current index's
metadata binding. This dated audit supplies the current routing/count
seal; the former editorial result should be read as historical. The
separate [routing observation](routing-observation.json) binds the old
record and current index bytes without rewriting either.

This audit's own first preparatory attempt misread an explanatory
manifest field, four logical certificate labels and a field-extension
degree multiplied by `(a-k)` as file paths. Its source, detailed result and
[failure history](attempt01-schema-parser-history.json) are preserved.
The corrected parser passes. This was an auditor-code failure and
executed no mathematical verifier.

The check is reproducible from the repository root with

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python \
  research/validation/2026-10-09-continuation-freeze-audit/check_record.py
```

Reproduction writes only this audit folder's result. Future canonical
edits should be sealed in a new dated audit instead of being attributed
to the frozen observation recorded here.
