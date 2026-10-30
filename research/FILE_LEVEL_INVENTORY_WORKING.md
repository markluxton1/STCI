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


## Migration continuation — third group (2026-10-30)

**15 additional sources read or sampled by section and content**, of which seven were integrated into Sections 16–19 of the permanent technical chapter and eight were compared against existing Sections 2–15 and retained for their detailed proofs, certificates, or dependency boundaries. No source from this group was deleted: the complete fiber-history enumeration, independent ideal equalities, two-chart conormal calculations, and marked proximity arguments remain substantially more detailed than the chapter synopsis. This is a deliberate *retain pending further extraction* decision, not a completed retirement.

Newly integrated:
- \`2026-10-10-session-genus-two-bisection-even-fiber-exclusion.md\`: whole exceptional graph, rational-singularity line-bundle descent, all positive even fiber counts excluded.
- \`2026-10-10-session-genus-two-bisection-three-blowup-fiber-exclusion.md\`: three entire fiber types, forced three-center histories, and the nonreduced \(D_5\) numerical near-counterexample defeated by an integral anti-nef uniformizer cycle. Source's conditional/awaiting-audit status preserved.
- \`2026-10-10-session-genus-two-trisecant-quartic-carriers.md\`: entire cubic ideal, 11-dimensional quartic space, contact discriminant and its identically-zero boundary.
- \`2026-10-09-session-ribbon-211-projection-independent-audit.md\`: fixed-center \([2,1,1]\) partition argument.
- \`2026-10-09-session-genus-one-uniform-projection-adversarial.md\`: isolated-ramification countershield and toric-family nonexhaustiveness.
- \`2026-10-10-session-genus-two-marking-and-section-pause-audit.md\`: \(D_8\) marking and internal-chain satellite caution.
- \`2026-10-10-session-genus-two-lambda1-horizontal-line-budget.md\` together with \`2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md\`: integral contact test, one/two-line budget, accepted \(B\)-absent exclusion and surviving \(B\)-present boundary.

Also compared and retained: \`2026-10-09-session-ribbon-repeated-partitions-complete.md\`, \`2026-10-10-session-ribbon-repeated-partitions-independent-audit.md\`, \`2026-10-09-session-genus-one-ribbon-net-independent-audit.md\`, \`2026-10-09-session-normalization-sectional-genus-zero.md\`, \`2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md\`, \`2026-10-09-session-nonrational-normalization-independent-audit.md\`, and \`2026-10-10-session-genus-two-entire-conductor-independent-audit.md\`. These provide deeper proof or independent verification of material already in the chapter. (The two horizontal-line sources above are counted together as one thematic unit; individual file tally is 15.)

**Cumulative:** eight historical sources retired in earlier passes. This pass made mathematical integration rather than deletions. Do not infer completeness of historical source coverage or an exhaustive inbound-reference scan.

## Repair pass — 2026-10-30

Correction to third-group dispositions: historical sources retained only because the chapter summarized rather than fully reproduced their mathematics are **incomplete migration**, not independently retained artifacts. Three source retirements have now been completed: `2026-10-10-session-genus-two-entire-conductor-independent-audit.md` (complete mathematical argument in `research/supplements/GENUS_TWO_ENTIRE_CONDUCTOR_PROOF.md`), `2026-10-09-session-nonrational-normalization-independent-audit.md` (complete mathematical argument in `research/supplements/NONRATIONAL_QUARTIC_NORMALIZATION_PROOF.md`), and `2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md` (full one- and two-line arguments added to Section 19 of `research/chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md`). The other twelve third-group sources remain **incomplete migration pending extraction**, not justified permanent retentions. Earlier two retained sources also remain incomplete. Cumulative historical sources retired: **11**. Historical full-population remaining count remains unverified. Some inbound links still require updating.

## Full-content migration continuation — 2026-10-30

GitHub write operations resumed. Nine additional historical sources were migrated with their full mathematical text (including proofs, calculations, caveats, and open boundaries) into permanent subject supplements and the historical source files were deleted. The nine are: genus-two even-fiber, genus-two three-center, genus-two trisecant carrier; genus-one [2,1,1] projection, uniform projection, ribbon partition casework, ribbon conormal net; genus-two marking/section and lambda-one horizontal-line budget. Their permanent paths are indexed in `research/INDEX.md`. The technical carrier chapter's links were redirected for these sources. **Cumulative historical source retirements: 20.**

This supersedes the earlier 'incomplete migration' disposition for those nine files, but not for the other unretired notes. The historical total remains unverified; repository-wide inbound-reference cleanup remains outstanding. Permanent supplements retain the complete original mathematical expositions pending subject-level editorial harmonization; duplicated headings and audit chronology should eventually be cleaned without deleting mathematical content.

## Full-content migration — quintic geometry batch (2026-10-30)

Seventeen historical `2026-10-11-session-*.md` mathematical sources were read and consolidated into four permanent subject-organized supplements: `QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md` (five source files), `DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md` (two), `QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md` (six), and `QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md` (four). All seventeen original source files were deleted after complete text preservation. The material includes quintic carrier/conormal geometry, low-pole spaces, degree-five del Pezzo A4 models, endpoint residual-support and contact calculations, and transverse jet/power descent. Conditional statements remain conditional; no correctness audit or canonical result promotion occurred. Research index updated. **Cumulative historical source retirements: 40.** Earlier inventory entries describing these notes as retained or candidates are superseded. Full historical population count and repository-wide inbound-reference cleanup remain outstanding.

## Full-content migration — nonendpoint quintic batch (2026-10-30)

Twenty-two historical `2026-10-12-session-*.md` mathematical sources were read, preserved in full and retired. Permanent destinations: `research/supplements/NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md` (seven), `NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md` (four), `NONENDPOINT_CUBIC_CONTACT_AND_FAMILIES.md` (six), and `NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md` (five). Their mathematical content includes conormal and conductor module calculations, center-rank cases, socle and all-mate restrictions, phase constraints, residual factorization and genus, pole filtrations, cubic-pair contact classifications, and exact target-fiber/full-support obstructions. Conditional scope and counterexamples remain preserved. All 22 original source files were deleted after permanent content was committed; no canonical promotion or new correctness audit was performed. The research index links the new supplements. **Cumulative historical source retirements: 62.** Remaining historical population and repository-wide inbound-link cleanup are unverified.

## Full-content migration — October 13 nonendpoint continuation (2026-10-30)

Seven complete historical mathematical sources were preserved in `research/supplements/NONENDPOINT_CUBIC_PAIR_COMPLETION.md` (four) and `research/supplements/NONENDPOINT_SINGLE_ROOT_INCIDENCE.md` (three) and their originals were retired. Material includes cubic-pair independent proof, coefficient checks, homogeneous gcd/rank classification, theorem-scope qualification, regular double-root analysis, quotient fibers, and Taylor incidence. Index updated. The separate `2026-10-13-generalization-quintic-l2.md` was read but remains unmigrated after a blocked write; no source deletion attempted. **Cumulative retired historical sources: 69.** No canonical promotion or new mathematical audit.

## Full-content migration — October 13–14 generalization batch (2026-10-30)

Twenty-five historical mathematical sources were preserved in full and retired after committing four subject-grouped supplements: `NORMAL_INDEX_SOCLE_AND_TORSION.md` (six), `NORMAL_CARRIER_SYMBOLIC_TORSION.md` (five), `PROJECTION_CONDUCTOR_CONTACT_AND_PHASE.md` (six), and `QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md` (eight, including the October 13 quintic L2 generalization). Topics include normal-index and socle bounds, conductor and symbolic triple calculations, torsion and index-12 compatibility, projection contact budgets and phase restrictions, intrinsic A4 contact, quintic conductor quotients, logarithmic support, and sextic incidence. Conditional claims and unresolved cases were retained; no new audit or promotion occurred. Index updated. **Cumulative historical sources retired: 94.** Editorial deduplication and repository-wide inbound reference cleanup remain outstanding.

## Full-content migration — root towers and cyclic covers (2026-10-30)

Twenty-eight historical mathematical sources were preserved in full in six subject-grouped supplements: `MOVING_POWER_SECOND_RELATION.md` (one), `MOVING_POWER_AND_SPECTRAL_ROOTS.md` (five), `QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md` (six), `CYCLIC_COVER_AND_MOVING_LINEAR_RIGIDITY.md` (seven), `LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md` (three), and `FINITE_ROOT_FAMILIES_AND_SMOOTH_OBSTRUCTIONS.md` (six). All 28 historical originals were subsequently retired. Scope includes moving-power relation obstructions, spectral-root curves, quadratic-root incidence, blowup and Cartier lifts, cyclic-cover counterexamples, moving-linear rigidity, degree-15 local cohomology, and finite/smooth-root formal obstructions. Complete mathematical calculations, counterexamples, hypotheses and limitations are retained, without new theorem promotion or correctness audit. The index links the six supplements. **Cumulative historical source retirements: 122.** Editorial deduplication and repo-wide inbound reference cleanup remain outstanding.

## Full-content migration — October 15 root and quintic H2 mathematics (2026-10-30)

Twenty-six historical mathematical sources were preserved in full and their originals retired. Permanent supplements: `UNIFORM_ROOT_TOWERS_AND_INSEPARABLE_BRIDGES.md` (six), `QUADRATIC_ROOT_SECOND_ZERO_AND_DUAL_COMPRESSION.md` (four), `QUINTIC_H2_SPECTRAL_AND_GENERATOR_SYSTEM.md` (seven), `QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md` (three), and `PROJECTION_TORSION_AND_RATIONAL_PHASE_BOUNDS.md` (six). Topics include finite determinacy and cohomology of root towers, inseparable blowup algebra, quadratic-root torsion and second-zero geometry, H2 spectral generators and ODE incidence, projection torsion cosets, rational phase bounds, and nef formal branches. All hypotheses, counterexamples, corrections and conditional limitations were retained without theorem promotion. Research index updated. **Cumulative historical source retirements: 148.** Editorial deduplication and repo-wide inbound reference cleanup remain outstanding.

## Full-content migration — October 16–19 structural geometry (2026-10-30)

Twenty-six historical mathematical sources were preserved in full in six subject-grouped supplements and all 26 originals retired: `NORMAL_FLATNESS_AND_FILTERED_CI.md` (five), `FIRST_RELATION_AND_SPECTRAL_ROOTS.md` (six), `REES_RESIDUAL_AND_EXCEPTIONAL_CYCLES.md` (four), `SATURATED_DUALITY_AND_MOVING_POWERS.md` (three), `PROJECTION_SINGLETON_AND_ANTIDIAGONAL.md` (four), and `STRUCTURAL_CONTINUATION_AND_INDEPENDENT_INVESTIGATIONS.md` (four). Subjects include normal-flatness and generic CI filtrations, first-relation defects, nonreduced spectral roots, Rees residual cycles, vertical-family counterexamples, filtered duality, singleton projection, quadric antidiagonal fourfold-line proposals, and October 16 quintic H2 continuation. Mathematical calculations, conditional hypotheses, failures and open cases are retained; no new theorem promotion or independent correctness audit. Research index updated. **Cumulative historical source retirements: 174.** Editorial deduplication and repository-wide inbound reference cleanup remain outstanding.

## Full-content migration — October 20–21 arithmetic and conditional geometry (2026-10-30)

Twenty-eight historical mathematical sources were preserved in full and their originals retired. Permanent supplements: `Z4_LIFTING_AND_DEFORMATION.md` (five), `Z4_INTRINSIC_ARITHMETIC_MECHANISM.md` (six), `CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md` (six), `CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md` (five), `CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md` (four), and `HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md` (two). These preserve Z4 lifting and divided-power obstruction calculations, characteristic-zero consequences with precise limitations, conditional (2,12) incidence and surface bounds, singular conductor ramification, exceptional-locus and sextic exclusions, and higher initial ideals and ribbon/triple thickening obstructions. No new theorem promotion or correctness audit. Research index updated. **Cumulative historical source retirements: 202.** Editorial deduplication and repository-wide inbound-reference cleanup remain outstanding.

## Full-content migration — October 23–25 intrinsic geometry and CI cycles (2026-10-30)

Twenty-eight historical mathematical notes have their full contents preserved in seven permanent subject supplements: `CI_CYCLE_DEFORMATIONS_AND_RESIDUAL_GEOMETRY.md`, `CI_CYCLE_VALUATIONS_AND_CONTACT.md`, `CI_CYCLE_AUDITS_AND_BOUNDARY_SMOOTHING.md`, `CI_CYCLE_PENCILS_AND_SPECIALIZATION.md`, `CI_CYCLE_ADAPTIVE_FRONTIER.md`, `INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md`, `IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md`. Subjects include intrinsic coefficient and blowup-flag valuations, filtered (4,4) contact obstructions, complete-intersection cycle deformations, smooth and nodal residual examples, genus and conductor ledgers, root-pencil specializations, endpoint valuations, and adaptive residual witnesses. Original source sections are identified within the supplements; epistemic status remains as in each source. This migration does not promote new results. **Target cumulative retirements after deleting all 28 originals: 230.**

## Full-content migration — October 24 quartic geometry (2026-10-30)

Thirty October 24 historical mathematical notes were preserved in full in three subject supplements: `QUARTIC_DUAL_FLAGS_AND_BITANGENTS.md` (10), `CUBIC_SCROLL_AND_RULED_SURFACES.md` (11), and `QUARTIC_PROJECTION_AND_SPECIAL_GEOMETRY.md` (9). These retain detailed mathematics of duality, flags, symmetric squares, bitangents, cubic scrolls, ruled surfaces, projection models, conormal geometry, special lines and planes, and independent reviews. No theorem promotion. **Target cumulative retirements after all 30 original deletions: 260.** Inbound reference cleanup remains outstanding.

## Full-content migration — October 23–26 delta, (4,4) and normal boundary (2026-10-30)

Twenty-five historical mathematical sources were preserved in full in four subject supplements: `DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md` (nine), `INTRINSIC_44_MULTIPLICITY_AND_GENUS_BUDGETS.md` (eight), `NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md` (four), and `INTRINSIC_44_APPROACHES_AND_CHARACTERISTIC_CONORMAL.md` (four). Delta embedding, singular loci, conormal annihilators, Rees specialization, characteristic conormal, intrinsic (4,4) proposals and critical audits, multiplicity constraints, degeneration genus budgets, normal torsion, weighted initials and global lifting are preserved without theorem promotion. **Target cumulative retirements after deleting all 25 originals: 285.** Inbound-reference cleanup remains outstanding.

## Full-content migration — October 25–27 endpoint and boundary (2026-10-30)

Five historical mathematical notes preserved in full in `BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md` (four) and `ENDPOINT_FOUR_ACTUAL_SEXTICS.md` (one). Topics include one-step boundary obstructions and their audit, endpoint-four nonsplit node scope, fixed-boundary node smoothing, and actual sextic jet certificates. No theorem promotion. **Target cumulative retirements after deleting five originals: 290.** Inbound reference cleanup remains outstanding.
