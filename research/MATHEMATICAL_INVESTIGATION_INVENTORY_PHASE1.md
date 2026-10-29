# Phase 1 — Mathematical investigation inventory (working)

Status: preliminary mathematical classification based on the working-branch MAP, INDEX, FRONTIER, PROVISIONAL_INVENTORY, claim reviews and historical manifest. **Not a complete current-tree enumeration or claim-level audit.** No theorem promotion or source deletion is authorized.

## Investigation families and consolidation destinations

| Family / destination dossier | Main scope | Canonical anchors | Provisional / historical intake | Remaining bridge |
|---|---|---|---|---|
| Intrinsic quartic geometry | Quadric, flags, osculation, bitangents, dual schemes, automorphisms, ruled and P4 models | R-0026–0029 | 2026-10-24 flag, special-lines, automorphism, P4 and Delta notes | Separate intrinsic geometry from STCI applications; extract unpromoted incidence calculations |
| Normalization, conductor, projection | Cartier singleton lifts, projection phases, conductor descent | R-0002–0004, R-0017, R-0036; Q-0001 | legacy normalization_conductor, open topics, historical donor notes | Realizable higher-degree phase images; non-Cartier and multibranch cases |
| Complete-intersection cycles | Residual degree, local clusters, attachments, smoothing | R-0019, R-0023–0025 | 2026-10-25 CI-cycle and valuative notebooks | Compare exceptional contact with actual residual support |
| Normal/conormal filtrations | Normal splitting, graded initial ideals, comparison defect, socle | R-0010, R-0020, R-0030–0033 | 2026-10-24 ideal filtration reconciliation; 2026-10-26 torsion, weighted initials, boundary repair | Global actual equations; punctual defect under sole support |
| Entirely-thick and moving roots | First and second relations, root schemes, movement and resultants | R-0005–0011, R-0013–0016, R-0018 | entirely_thick legacy topic; root and formal notes | Nonsaturation, extra generators, singular roots, global realization |
| Valuations and boundary | Complete clusters, cancellations, Gauss weights, principal parts | R-0019, R-0030 (limited overlap) | 2026-10-23 valuations reconciliation; 2026-10-26 weighted initials; 2026-10-27 one-step obstruction | Intrinsic and global boundary invariants |
| Low-degree exclusions | Quartic carriers, (4,4), fixed sextics | R-0001, R-0022, R-0025 | K3 alternative proof, multiplicity-three and quartic degeneration notes | Higher-degree carrier families; retain examples without reopening closed cases |
| Positive characteristic/arithmetic | Frobenius constructions, mu4, conormal splitting, mixed-characteristic lifting | R-0012, R-0020–0021, R-0031 | Space Curves VI binomial examples, arithmetic ruled models | Which phenomena require Frobenius versus splitting? |
| Singular carrier geometry | Cartier index, normality, conductor, socle and resolutions | R-0034–0036 | normal_carriers legacy topic, normalization notes | Higher indices, nonnormal and multiple-branch models |
| Computational mathematics | Finite jet certificates, symbolic and lattice computations | R-0025, R-0027 (certificate-qualified) | Space Curves VI-011/012, scripts, historical Ultra inventories | Link every unique input/script to mathematical claim and exact scope |

## Critical overlap rules

- R-0002–0004 are conditional carrier tests/reductions, not existence proofs. R-0017 shows singleton inverse support alone does not supply a mate.
- R-0019 conditional residual zero-cycle statement differs from elementary proper-CI cycle identity `de=4m+deg R`.
- Higher initial equations can arise by cancellation: dependent first symbols do not determine a thickening.
- Exceptional vertical cycles and wedge vanishing do not by themselves imply a residual curve downstairs.
- R-0012 prescribed Z4 nonlifting is not a universal mixed-characteristic or characteristic-zero obstruction.
- R-0023–0025 are fixed examples/fixed carriers, not uniform exclusions.
- R-0030 punctual support inclusion does not prove simultaneous singularities or existence of a punctual defect under sole support.

## Preservation priorities

1. Space Curves VI-011 finite normal-jet test, its multiplication-map formulation, and script; VI-012 global coefficient counterexample and characteristic-specific binomial pair.
2. Entirely-thick higher initial ideals, root degenerations, cancellation examples and nonsaturated boundary calculations.
3. Normalization/conductor failed realizations and negative results, including singleton inverse-support obstruction.
4. Valuative complete clusters, principal-parts boundary repair, and residual-attachment constructions.
5. Imported rational-quintic smooth and A1 cubic-carrier calculations, independent of the fixed quartic question.
6. Unique scripts, exact input forms, finite-rank certificates, and relevant computational witnesses.
7. Unpromoted intrinsic geometry, including incidence cycles and arithmetic ruled models.

## Large-batch consolidation order

1. **Pilot:** normalization / conductor / projection / Cartier lifting, including R-0002–0004, R-0017, R-0034–0036 and Q-0001. Preserve hypotheses and failed realizations. No source deletion during pilot.
2. Intrinsic quartic geometry and ruled/dual/flag packages.
3. CI cycles, residual configurations, deformation and jet rigidity.
4. Normal filtrations, entirely-thick structures, moving roots, valuations and boundary repair (coordinate shared definitions before parallel edits).
5. Characteristic-dependent constructions, arithmetic lifting and general space-curve donor mathematics.
6. Computational certificates and cross-family deduplication after mathematical ownership is assigned.

## Coverage and gaps

Verified in this pass: working-branch AGENTS, INDEX, MAP, STATE, FRONTIER, results/INDEX, PROVISIONAL_INVENTORY, historical manifest, first claim review, and Space Curves intake excerpts. Existing claim reviews collectively register CR-01–46; 36 promoted records are indexed. **Not verified:** exhaustive current-tree file enumeration, all 36 full proofs, individual historical scratch/archived files, all scripts, or all side-branch differences. The dated manifest explicitly disclaims completeness. No current file count or exhaustive preservation certificate is asserted.

Next: enumerate current tree with nontruncated tree SHA; compare side branches and historical manifests; extract claims per dossier, preserving unique mathematics and eliminating mere correction chronology only after comparison.

## Phase 1B — historical donor mathematical extraction (October 29)

**Scope:** source-specific extraction from the Space Curves intake README, donor artifact manifest, historical source manifest, mathematical map, and frontier. This is not a new proof audit or an exhaustive scratch/tree scan. Paths below are relative to `research/archive/space-curves-2026-10-19/` unless otherwise stated.

| Contribution and precise scope | Source path(s) | Proposed permanent home | Status / relationship |
|---|---|---|---|
| Finite normal-jet criterion for supplied global homogeneous pair on integral degree-d curve: if d divides ab and M=ab/d, sole reduced support iff generic truncated length at I_C^(M+1) equals M; weighted componentwise version for reduced unions. Full truncated ideal multiplication map, not two-vector rank. | `space-curves-vi/state/artifacts/integrated/ARTIFACT-20260906-011-finite-normal-jet-certificate.md`; `space-curves-vi/scripts/finite_normal_jet_certificate.m2`; `space-curves-vi/state/artifacts/provisional/WORKER-20260906-finite-jet-audit.md` | Global equation realization / finite normal jets (cross-link computational mathematics) | Imported source proof and donor audit, **not promoted**. Complements but does not follow from R-0005–0011; no uniform degree bound. |
| Global coefficient-field counterexample: for C_n=(s^(n+1):s^nt:st^n:t^(n+1)), n>=2, pencil generated by yS_n,wS_n, S_n=yw^(n-1)-z^n: k(C_n)-linear combination has generic length 2 but every nonzero constant combination has length 1. | `space-curves-vi/state/artifacts/integrated/ARTIFACT-20260906-012-global-coefficients-and-frobenius.md` | Global equation realization, with valuation cross-reference | Imported audited formulation control; cannot replace global k-coefficients with k(C). |
| For specific binomial pair (S_n,x^n w-y^(n+1)), support equals C_n iff characteristic p>0 and n is a p-power; characteristic-zero failure of **this pair** does not exclude other pairs. | Same VI-012 | Positive characteristic / explicit constructions | Imported example, **not universal**. Keep twisted-cubic positive control as well. |
| Contact-depth estimate m<=(h+1)pq and h>=ceil(ab/(dpq))-1 for generic normal orders p,q and common infinitely-near depth h; surface-effective threshold tau yields h>=ceil(tau^2/d)-1; smooth (1,n) on quadric forces h>=n-1 under carrier exclusion. | `space-curves-vi/state/artifacts/integrated/ARTIFACT-20260823-003-surface-threshold-second-resultant.md`; `space-curves-vi/state/artifacts/integrated/ARTIFACT-20260823-005-contact-depth-and-quadric-families.md`; `space-curves-vi/state/artifacts/integrated/WORKER-20260823-jaffe-contact-depth-audit.md` | Entirely thick / valuations | Source argument and scope audit, **provisional**. Not an all-degree obstruction; distinguish generic horizontal contact from closed-point exceptional type. |
| Same leading tangent form need not determine next multiplicities: local y^p+x^(p+r) examples. | `space-curves-vi/state/artifacts/integrated/ARTIFACT-20260823-010-horizontal-recurrence-boundary.md` | Entirely thick / valuations | Negative example; finite cutoff exists for fixed supplied pair by VI-011, not uniformly over degrees. |
| Smooth rational degree-five curve on smooth cubic surface: class 2L-E1 in suitable marking; exactly five disjoint lines, hence carrier complement nonaffine. One-A1 normal cubic, curve avoiding node: disjoint line via weak-del-Pezzo lattice, 120 eligible classes and 15 specified line classes. | `space-curves-i/research-state/artifacts/ARTIFACT-20260821-014.yaml`, `ARTIFACT-20260821-015.yaml`, `ARTIFACT-20260821-019.yaml`, `ARTIFACT-20260821-020.yaml`; `space-curves-i/research-state/scripts/nodal_cubic_quintic_lattice.py` | **General space curves / rational quintic cubic carriers** (separate from C0) | Imported source-reviewed claims, **not target-promoted**; nodal independent-review evidence weaker; script not rerun; nonaffine specified carrier does not imply universal quintic non-STCI. |
| Corrected explicit rational-quintic benchmark forced line V(3U2-5U0,3U3-5U0-5U1); partial resultant and singular-incidence data, not full discriminant. | `space-curves-i/research-state/artifacts/ARTIFACT-20260821-012.yaml`, `ARTIFACT-20260821-013.yaml`, `ARTIFACT-20260821-023.yaml`; `space-curves-i/research-state/scripts/vahlen_quintic_exact.py`, `vahlen_base_locus_discriminant.py` | General space curves / quintic computational benchmarks | Corrected coordinate input; discard superseded erroneous line display, retain exact scripts. |
| Two distinct fixed-carrier failures: cuspidal cubic divisor proportionality but nonzero additive polar conductor part -3z^(-2); ruled cubic pinch torsion compatible but normalized H=(2,1), Ctilde=(2,0) not proportional. | `space-curves-iii/research-state/artifacts/ARTIFACT-20260821-012.json`, `ARTIFACT-20260821-013.json`; `space-curves-iii/research-state/experiments/2026-08-21-explicit-examples.md`, `explicit_examples.py` | Normalization / conductor / failed realizations | Historical examples of distinct R-0003 stages; source interpretation not independently reaudited. |
| Fivefold conormal root on explicit quartic C0 carrier with first-transform normal derivative coefficient 2 and p1=5,p2=0; repeated root does not imply persistent contact after blowup. | `space-curves-iv/research-state/artifacts/ARTIFACT-20260822-031.yaml`, `ARTIFACT-20260822-032.yaml`; `space-curves-iv/experiments/c4_root_collision.py`, `c4_conormal.py` | Intrinsic quartic / conormal collision examples | Computation with **provisional** ADE/type interpretation; no proved global irreducibility/normality; quartic mate cases already closed R-0001. |
| Historical Space Curves II generator-span finite checks and Space Curves V (4,7) formal contact/finite-field probes | `research/archive/space-curves-2026-10-19/README.md` (decisions II and V; donor source inventory for unimported paths) | Computational methods / closed low-degree investigations | Do not preserve finite scans as characteristic-zero exclusions; retain only distinct structured contact-module method or exact useful inputs after source check. |

### Phase 1B gaps and Phase 2 implications

- **Still unexamined individually:** `research/scratch/` paths, most historical notes and scripts, post-October-17 additions, and complete differences of research branches. Existing historical manifest explicitly says no nontruncated current-head recursive tree enumeration exists. Do not certify completeness or delete sources on this basis.
- **Branch comparison outstanding:** enumerate named side branches and compare their mathematical content, not merely changed-file counts; distinguish already integrated claims from branch-only mathematics.
- **Computational intake outstanding:** map each exact script/input to its claimed proposition, characteristic, outputs and limitations; the Space Curves donor inventory is an acceleration index, not evidence that all scripts were checked.
- **New conceptual dossier recommendation:** separate *general space curves and rational quintics* from C0-specific geometry, and treat *global homogeneous equation realization* as an explicit interface connecting finite jets, k versus k(C) coefficients, and boundary repair.
- **No new promotions, source deletions or dossier restructuring** in this phase. Ordinary corrected mistakes should not become permanent research history; substantive counterexamples and failed realizations should.

### Reconciled unique scratch calculation

| Contribution and hypotheses | Exact source | Destination | Status |
|---|---|---|---|
| Corrected type-B (4,5) second-neighborhood Cech obstruction, rank-one determinant c1*c3-c2², killing section c2-c1*z on c1 !=0 and remaining coefficient c1². | `research/scratch/explore_quasi45_type_b.py` | Normal/conormal filtrations and low-degree historical methods | Exploratory script, not theorem. Preserve corrected formulas and hypotheses; do not preserve obsolete frozen-frame calculation as mathematics. |

The source script defines α=a0+a1z, β=b0+b1z and restricts to Δ=a0b1−a1b0 ≠ 0. Its corrected Čech coordinates c1,c2,c3 satisfy the rank-one killing condition c1c3−c2²=0; on c1≠0 the killing section is c2−c1z and the remaining coefficient is c1². These are symbolic calculations, **not a proved global (4,5) obstruction theorem**. Retain the coefficient corrections under changes of embedded charts; do not use the obsolete frozen-frame formulas.

### Additional preservation cautions from the parallel pass

- The VI-011 finite-jet criterion uses the sharp truncation I_C^(M+1), the full multiplication matrix, and restricted global scalar parameters, not merely two coefficient vectors.
- The VI-012 example distinguishes k-constant linear combinations from k(C)-linear combinations; the latter cannot be substituted in a global homogeneous-equation search.
- Scratch discovery leads not individually reviewed: `research/scratch/explore_split4_lift.py`, `research/scratch/explore_split4_local.py`, `research/scratch/explore_split22_nonramified.py`, and `research/scratch/mf6_type4_resultant.m2` (verify the final path before use).
- The branch `codex/intersections-containing-quartic-2026-10-27` still needs a substantive mathematical comparison; no complete branch or scratch census is claimed.

