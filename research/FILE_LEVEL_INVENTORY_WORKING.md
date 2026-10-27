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
