# Repository-wide historical source manifest — 2026-10-26

**Scope and status:** reconciled directory and file-level **index of existing GitHub historical inventories**, not a new recursive tree crawl, not an assertion that all present-day paths have been enumerated, and not a mathematical proof audit. No local filesystem or Work mode used. The underlying October 17–19 inventories contain individual file paths and provenance; this document assigns retention, claim extraction and evidence roles. Do not delete files based on this manifest.

## A. Indexed historical path sets

| Set | Existing per-path source | Snapshot size | What is covered | Decision |
|---|---|---:|---|---|
| Ultra historical source notes | [ULTRA_SOURCE_NOTES_INDEX](archive/ULTRA_SOURCE_NOTES_INDEX.md) | **356** individual notes | File paths, GitHub source links, sizes, heuristic keyword buckets | Historical claim sources; review against canonical records before extraction or promotion |
| Ultra computations | [ULTRA_COMPUTATIONS_INDEX](archive/ULTRA_COMPUTATIONS_INDEX.md) | **427** directly contained files | Scripts, outputs, JSON, logs and data with exact paths/sizes | Evidence, not independent theorem authority; distinguish executable source from output |
| Ultra validation | [ULTRA_VALIDATION_RECURSIVE_INVENTORY](archive/ULTRA_VALIDATION_RECURSIVE_INVENTORY.md) and [directory index](archive/ULTRA_VALIDATION_INDEX.md) | **2,168** tracked blobs in 106 top-level directories; 2,542 tree entries | Recursive validation paths, preserved blob sizes, Git tree SHA 48ed7bda55b4faf9606b7959986178b417601e80 | Preserve complete sessions and dependency chains; large witnesses are not disposable duplicates |
| Space Curves I–VI donor records | [source-artifact-inventory.json](archive/space-curves-2026-10-19/source-artifact-inventory.json), [intake manifest](archive/space-curves-2026-10-19/manifest.json), [README](archive/space-curves-2026-10-19/README.md) | **98** donor artifact files, not 98 distinct results | Source project, path, ID, title, original status, SHA-256, imported flag | Imported evidence and unimported donor references must not be conflated |
| Ultra selected handoffs and source-audit copies | [ULTRA_INTAKE](archive/ULTRA_INTAKE.md) | Seven handoff/state snapshots plus selected source notes | Original branch and preserved archival paths | Historical state only; status labels do not override current authority |
| October 17 provenance census | [PROVENANCE_CLASSIFICATION](PROVENANCE_CLASSIFICATION_2026-10-17.md) | Notes 382, computations 461, validation 2,168, scratch 112, archive 95, synthesis 11, results 17, questions 1 | **Directory totals at that date**, not per-path listing for every directory | Baseline for gap detection, not current counts |
| Current authority and indexed active research | [research index](INDEX.md), [canonical results](results/INDEX.md), [provisional inventory](PROVISIONAL_INVENTORY.md) | 31 promoted result IDs on adjudication branch; 46 separately registered provisional/reviewed claims | Navigation and scope; recent October 20–26 packages | Keep separate from historical Ultra snapshot and from theorem authority |

**Do not add these counts together as a count of unique repository files.** The 356/427/2168 inventories are source snapshots and overlap the October 17 directory census; the 98 donor artifacts are an external intake, some imported and some not. In particular the 3,076 preserved Ultra-branch blobs reported by [ULTRA_INTAKE](archive/ULTRA_INTAKE.md) are not a disjoint additional population.

## B. Source-by-source disposition rules

| Path family | Status | Review procedure | Deletion policy |
|---|---|---|---|
| `research/results/` | Canonical only for exact record hypotheses | Read R-0001–R-0031 and source dependencies; identify legacy topic navigation separately | Retain |
| `research/questions/` | Canonical question record, not a proof | Check STCI-Q-0001 and open frontier | Retain |
| `research/notes/` | Mixed historical proof, failed attempt, audit, provisional theorem and later promoted evidence | Match each source path from Ultra index and post-snapshot notes against results and CR-01–CR-46; label promoted evidence, unpromoted claim, correction, or abandoned approach | Retain |
| `research/computations/` | Executable certificate and output mixture | For each script, locate its saved output, assumptions, characteristic, exact inputs, dependency in a note/result and replay status | Retain |
| `research/validation/` | Reproducibility sessions and witnesses | Use recursive inventory to keep entire directory-level provenance; distinguish exact replay, exploratory sampling and known failure | Retain |
| `research/scratch/` | Historical provisional calculations | **No existing complete per-path list identified** in the examined indices; needs fresh GitHub tree enumeration | Retain; never infer obsolete from filename |
| `research/archive/` | Historical source snapshots, handoffs, inventories and imported evidence | Track original branch, path and any duplicated source without collapsing review history | Retain |
| `research/synthesis/` | Exposition and cross-links | Match mathematical claims to canonical records; unsupported syntheses remain explanatory | Retain |
| `research/open/`, `research/certificates/`, `research/figures/` | Frontier, evidence pointers and visualization | Preserve references, replay links and scope | Retain |

## C. Mathematical extraction coverage

| Claim register | IDs | Source area | Coverage status |
|---|---|---|---|
| [First tranche](CLAIM_REVIEW_2026-10-26.md) | CR-01–CR-14 | Residual cycles, valuations, fixed sextic, deformation, filtrations | Selective documentary audit |
| [Second tranche](CLAIM_REVIEW_GEOMETRY_K3_2026-10-26.md) | CR-15–CR-31 | Flag, conormal, duality, ruled surfaces, K3 alternative proof | Selective documentary audit |
| [Third tranche](CLAIM_REVIEW_ARITHMETIC_SCHEMES_2026-10-26.md) | CR-32–CR-46 | Arithmetic four-section model, group schemes, conductors, dual singular scheme | Selective documentary audit |

No assertion that 46 claims exhaust 356 historical notes, 98 donor artifacts or any computation/validation session. Existing promoted result IDs must not be counted as new promotion candidates.

## D. Explicit gaps preventing a complete current-tree manifest

1. **No live recursive tree enumeration in this pass.** The connected GitHub file API supports named-file reads/writes, but the available connector actions do not expose a read-only recursive tree listing. The GitHub website tree/API attempt did not yield an accessible listing. Thus a path-by-path current-head diff against the October 17 census is **not established**.
2. **Scratch and archive path coverage.** The October 17 census records 112 scratch and 95 archive files but the consulted historical indices do not enumerate all their individual paths. A current Git tree manifest is needed.
3. **Post-October-17 additions.** Notes, computations, validation files, promotion records and PR-76 files added later cannot be assumed covered by the dated Ultra indices.
4. **Duplicate content.** October 17 provenance reports 478 identical-content groups with 869 additional copies. A duplicate hash does not certify safe deletion, especially for validation snapshots.
5. **Source dependencies.** The per-path inventories do not map every script to its exact result, saved output, independent audit and characteristic assumptions.
6. **Branch-only material.** The preserved Ultra-branch assertion does not establish that every later side branch was imported or reconciled. Compare named active branches explicitly before completeness certification.

## E. Completion criterion

A *complete current-head path manifest* requires one GitHub tree snapshot with branch/ref and tree SHA, `truncated=false`, all tracked paths and blob SHAs, and a machine-checkable reconciliation against the three Ultra path indexes and Space Curves donor manifest. Each path then receives an explicit role (canonical result, question, historical source, audit, computation, validation, scratch, navigation or generated artifact), claim-ID link if applicable, preservation decision and review state. Only after that can a complete claim-level extraction or safe-removal decision be asserted.

**Current verdict:** the historical Ultra and Space Curves sources have substantial pre-existing **path-level inventories**; the present PR now reconciles them into a single authority-aware manifest. **A verified, exhaustive current-tree path manifest is still outstanding.** No deletions or theorem promotions authorized.

## F. October 26 review-branch promotion overlay

Seven scoped result records, R-0023–R-0029, were added on the adjudication branch after this manifest's initial compilation. The 46 adjudicated CR claims have the following disposition: R-0023 (CR-06–07), R-0024 (CR-08), R-0025 (CR-09–11), R-0026 (CR-15–20 and 42–43), R-0027 (CR-21–22 and 44–46), R-0028 (CR-23–26), and R-0029 (CR-32–41). CR-27–30 is an alternative proof attached to R-0022, CR-31 is covered by existing exclusions, CR-01–05 are supporting local claims, CR-14 is a correction, and CR-12–13 remain on hold.

This overlay updates **claim dispositions only**. It does not supply a fresh recursive current-head tree listing, establish completeness for scratch/archive, or identify every post-snapshot source. The path-level completeness criteria in section E remain unmet. No deletion is authorized.

## G. Filtration claim disposition update

R-0030 promotes the independently reviewed local comparison, generator-excess, torsion and smooth-carrier support statements; R-0031 promotes the fixed characteristic-two pair's global fourth-equation/kernel identification. This raises the review-branch result index to 31. The normal-Koszul spectral-sequence general packaging and supported punctual-defect question remain unpromoted or open. This update does not improve completeness of the historical file-tree inventory.

## H. Subsequent structural promotions (review-branch overlay)

The historical structural adjudication promoted R-0032 through R-0036 after the earlier 31-record census. These five records cover the conormal/socle budget, constant first-relation obstruction, local normal-carrier index/socle identity, bounded-index normal-carrier exclusion and pointwise conductor/socle identity. The canonical index now contains 36 records. This overlay does not imply a new recursive current-head tree inventory, or a resolution of deferred symbolic-ribbon, quintic endpoint, or degree-15 certificate questions.
