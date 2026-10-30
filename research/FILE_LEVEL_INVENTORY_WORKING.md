# File-level mathematical inventory — working register

**Branch:** `restructure/mathematical-consolidation`  
**Status:** initial source reconnaissance; **not** an exhaustive current-tree inventory.

## Objective

Identify the unique mathematical contribution, dependencies, and appropriate future home of each tracked file before consolidation. The unit of assessment is the *file*, but one file may contain several independent claims, proofs, corrections, or useful failed approaches.

## Evidence inspected

- `research/INDEX.md`: navigation across canonical, provisional, historical, computational, and reconciliation sources.
- `research/HISTORICAL_SOURCE_MANIFEST_2026-10-26.md`: pre-existing path inventories, their overlap, and explicit coverage gaps.
- `research/PROVENANCE_CLASSIFICATION_2026-10-17.md`: dated directory census and duplicate-blob summary.
- `research/archive/ULTRA_SOURCE_NOTES_INDEX.md`: historical file-level index of 356 notes (filename-keyword buckets, **not** content classification).

These sources are **indexes**, not substitutes for reading each file.

## Current coverage and gaps

| Family | Existing evidence | Inventory state | Required next pass |
|---|---|---|---|
| `research/results/` | 36 canonical records identified by current navigation | Names and authority layer known; individual proof content not yet assessed here | Read each result and link supporting sources |
| `research/notes/` | 356 older notes in Ultra index, plus later additions | Historical partial path list | Enumerate current paths; inspect mathematical content |
| `research/computations/` | 427 older indexed files | Historical partial path list | Map scripts, outputs, exact inputs and claim dependencies |
| `research/validation/` | 2,168 blobs in older recursive snapshot | Historical partial path list | Identify essential reproducibility witnesses vs generated copies |
| `research/scratch/` | 112 files at October 17 census | No complete path list established | Enumerate and read |
| `research/archive/` | Multiple partial indexes and donor manifests | Partial and overlapping | Distinguish unique mathematical sources from session history |
| `research/synthesis/`, `research/open/`, `research/questions/` | Current navigation links | Not yet assessed file by file | Identify unique exposition, conjectures, corrections and open problems |
| Root and other paths | No current exhaustive listing | Unenumerated | Capture full tree |

**Important limitation:** the available connected GitHub actions permit named-file reads but do not expose a read-only recursive Git tree. Existing historical indexes explicitly say they are not complete current-head enumerations. A full inventory cannot be certified until a recursive `git ls-tree -r -l HEAD` manifest (or equivalent, including blob hashes) is supplied or accessible.

## File-register schema

One row per tracked path, with columns:

`path | blob_sha | bytes | family | primary_theme | secondary_themes | file_role | mathematical_content | claim_ids | dependencies | distinct_contribution | status | proposed_destination | disposition | evidence_level | review_notes`

Recommended `file_role`: theorem/proof; alternate proof; failed approach/counterexample; conceptual framework; exploratory calculation; audit; executable certificate; generated output; navigation; agent/session administration.

Recommended `disposition`: retain and consolidate; retain as essential evidence; reference only; candidate redundant **after** extraction; unresolved. No file is automatically marked deletable based on age, filename, or duplicate hash.

Recommended `evidence_level`: filename only; indexed metadata; content read; cross-checked against authority; independently validated.

## Initial mathematical extraction priorities

1. The 36 canonical records and their actual supporting proofs.
2. Provisional notes on generic normal forms, valuations, torsion, boundary repair and the (4,4) case.
3. Intrinsic geometry (special planes/lines, duality, ruled models) and positive-characteristic constructions.
4. Failed exclusions and corrections whose *failure mode* constrains future research.
5. Remaining historical notes, scripts and validation witnesses, checking for otherwise unrepresented mathematics.

## No deletion or promotion

This register is an inventory aid. Neither file disposition nor mathematical authority changes during this phase.

## Quartic-carrier proof-file disposition — 2026-10-27

Permanent mathematics: [carrier chapter](chapters/CARRIER_AND_CONDUCTOR_GEOMETRY.md) and [technical proofs](chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md). Keep source provenance and deletion decisions here, not in the technical appendix.

| Source file (under research/notes/) | Disposition and reason |
| --- | --- |
| 2026-10-09-session-ribbon-4-root-independent-proof.md | Candidate after reference migration; later complete repeated-partition proof covers all endpoints/directions |
| 2026-10-09-session-ribbon-22-bounded-power-obstruction.md | Candidate after reference migration; later full audit proves all-power trace/norm obstruction |
| 2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md | Candidate after reference migration; its unique graph argument is extracted in technical proofs |
| 2026-10-09-session-ribbon-repeated-partitions-complete.md | Retain owner proof and computational provenance |
| 2026-10-10-session-ribbon-repeated-partitions-independent-audit.md | Retain exact ideal-equality certificates |
| 2026-10-09-session-genus-one-ribbon-net-independent-audit.md | Retain two-chart conormal and orbit audit |
| 2026-10-09-session-ribbon-211-projection-independent-audit.md | Retain distinct [2,1,1] case |
| 2026-10-09-session-genus-one-uniform-projection-adversarial.md | Retain full-fiber criterion and ramification failure shield |
| 2026-10-10-session-genus-two-bisection-even-fiber-exclusion.md | Retain integral-correction descent lemma |
| 2026-10-10-session-genus-two-bisection-three-blowup-fiber-exclusion.md | Retain explicit fiber-graph analysis pending extraction |
| 2026-10-09-session-normalization-sectional-genus-zero.md | Retain primary genus-zero proof |
| 2026-10-09-session-quartic-rational-cone-normalization.md | Retain proposal, distinguish from independently accepted proof |
| 2026-10-09-session-nonrational-quartic-normalizations.md | Retain ruled-normalization owner proof |
| 2026-10-09-session-genus-two-degree-one-counteraudit.md | Retain Hodge/Riemann–Roch square-one lemma |
| 2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md | Retain owner derivation alongside independent audit |
| 2026-10-10-session-genus-two-conductor-line-position.md | Retain intersection-length and trisecant geometry |
| 2026-10-10-session-genus-two-marking-and-section-pause-audit.md | Retain D8 marking; separate unfinished section work |
| 2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md | Retain bounded independent audit |
| 2026-10-10-session-genus-two-lambda1-horizontal-line-budget.md | Retain integral pullback cycles and failure modes |
| 2026-10-10-session-genus-two-trisecant-quartic-carriers.md | Retain cubic carrier ideal and geometry; later audits establish exclusions |

**Deletion gate:** The three candidates each had 11 indexed default-branch code-search references, including historical validation scripts and outputs. Do not remove them without a full branch-local inbound-reference scan and deliberate treatment of reproducibility. Never rewrite historical validation outputs merely to clear a deletion check.

## Exact duplicate-blob census — current branch (2026-10-27)

Source: full, untruncated recursive Git tree at commit `c71eb0b70a090479017a80b4ba29b01c2f37ab4f`. Grouping by Git blob SHA gives **3,862 tracked files, 2,976 distinct blobs, 483 duplicate clusters, and 886 additional identical-file paths**. These are exact byte-for-byte duplicates, not semantically redundant proofs.

| Location of duplicate cluster | Extra identical paths |
| --- | ---: |
| Spans more than one top-level research family (or research and root) | 780 |
| Entirely within research/validation | 86 |
| Entirely within research/archive | 14 |
| Entirely within research/computations | 4 |
| Entirely within research/scratch | 2 |
| **Total** | **886** |

The dominant pattern is **cross-family evidence copying**, especially `research/computations/` sources repeated inside `research/validation/.../isolated/research/computations/`, and branch-reconciliation snapshots of `research/STATE.md` and `research/FRONTIER.md`. Another large identical-blob cluster is empty or near-empty stderr/stdout logs across failed and successful runs. These categories should not be conflated: isolated snapshots may be intentionally self-contained and repeated empty logs have low mathematical content, but historical scripts and manifests may refer to their paths.

**Deletion priority:** first assess repeated empty stdout/stderr files, then redundant snapshot copies that are not needed by any independent replay, and only then proof-owner notes. Before any deletion, check branch-local inbound references and execution expectations. This census supplies candidate *families*, not deletion authorization.

## Mathematical migration progress — 2026-10-30

Working branch: `restructure/mathematical-consolidation`. Fixed population: historical research notes and other historical mathematical sources indexed by the existing inventories, plus later branch additions; current exhaustive path population and remaining count are **not yet established**. The October 27 snapshot counted 545 notes, not a verified current remainder. Do not count scripts or canonical results as disposable notes.

| Historical source under `research/notes/` | Disposition | Permanent mathematical destination |
| --- | --- | --- |
| `2026-10-09-session-ribbon-4-root-independent-proof.md` | Retired | `research/chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md`, direct [4] line-singularity proof |
| `2026-10-09-session-ribbon-22-bounded-power-obstruction.md` | Retired | Same chapter, explicit [2,2] trace/norm computation; executable verifier retained |
| `2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md` | Retired | Same chapter, endpoint irreducible graph and all-length chain inequality |

Completed: **3 retired, 0 retained, 0 unresolved** in this processed group. Outstanding: remaining indexed historical sources not yet individually reconciled. Previous 'candidate after reference migration' labels for the first two files and the stale 'retain pending extraction' label for the third are superseded by the above completed dispositions. The complete branch-local inbound-link cleanup remains an organizational follow-up; do not modify historical computational output solely to erase old references.

## Migration continuation — second group (2026-10-30)

Five more historical sources retired after comparison with the permanent technical chapter: `2026-10-09-session-genus-one-entire-conductor.md` (entire conductor and exact coordinate/fiber formulas), `2026-10-10-session-genus-two-conductor-line-position.md` (complete bisecant/trisecant geometry and contact cautions), `2026-10-10-session-genus-two-bisection-quadratic-descent.md` (conditional split conductor/root-of-unity power criterion), `2026-10-09-session-nonrational-quartic-normalizations.md` (nef pushdown and ruled intersection contradiction), and `2026-10-09-session-quartic-rational-cone-normalization.md` (class-group and differential descent contradiction). Their mathematical homes are Sections 2, 5, 9, 10, 12, 14 and 15 of `research/chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md`. Independent audit notes and exact computational scripts remain.

Read but **retained** for further extraction: `2026-10-09-session-normalization-sectional-genus-zero.md` (detailed vanishing/classification and singular-point correction), and `2026-10-09-session-ribbon-repeated-partitions-complete.md` (full exhaustive partition computations; independent audit retained). One named degree-one counteraudit path was absent from this branch and is not counted as processed.

**Cumulative dispositions:** 8 retired; 2 retained pending reconciliation; 0 explicitly unresolved mathematical conflicts. These figures refer only to sources actually reviewed during these migration passes, not the historical full-tree population. Full branch-wide inbound-link reconciliation is not yet complete; references in historical evidence may still name retired files.
