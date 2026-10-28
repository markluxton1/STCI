# All-branch frontier and provenance inventory — 2026-10-13 evening

**Scope:** repository coverage and routing, with accepted mathematics taken as correct. No inherited verifier or proof was rerun. This note records the branches actually observed locally and through the connected GitHub reader. **Historical snapshot:** branch inventories and statuses here are dated October 13, not current branch or theorem status. The present [authority policy](../AUTHORITY.md) and [canonical results](../results/INDEX.md) control. Preserve the historical manifest as evidence. It does not change checkout, branches, remote refs, canonical files, or the status of any mathematical claim.

## 1. Observed checkout and complete ref coverage

At the first inspection, the working tree was clean. Current checkout:

- branch `research/ultra-resume-2026-10-06`;
- HEAD `b16e4322c7b955147ce2ed241a1a0316a8e1a67a`;
- commit title `2026-10-13 morning limit reached`;
- one local worktree, no tags, and no stashes.

The initial clean observation predates other agents' evening writes. It is not a claim that the subsequent shared working tree is clean.

| Local or cached ref | Exact SHA | Coverage / relationship to current HEAD |
|---|---|---|
| local `research/ultra-resume-2026-10-06`, cached `origin/research/ultra-resume-2026-10-06` | b16e4322c7b955147ce2ed241a1a0316a8e1a67a | Current checkout; live remote agrees. |
| local `main`, cached `origin/main`, cached symbolic `origin/HEAD` | 98d71ddf8f8cceaad01bec43e94298699dcb5560 | Ancestor, current checkout has 30 later commits. Cached main is stale relative to live remote main. |
| local `archive/codex-5hr-interrupted`, local `ultra_mode`, cached `origin/ultra_mode` | 2e53a7b5e9d4c96b5741ee4a4746a4a9ff0ad647 | Historical interrupted branch; current HEAD has 62 unique commits, this branch has 1. Live ultra_mode agrees. |
| cached `origin/research/consolidate-2026-10-06` | 3f7b7fec652a0175ef7a7c5353f198f03649281a | Historical consolidation; 31 current-only / 55 cached-branch-only commits. No added path absent from HEAD. This branch name is absent from live enumeration. |
| cached `origin/research/local-audit-e2` | a0a5a67e2d5b01c83832041b578efe9d478f5c8c | Historical local audit; 31 current-only / 18 cached-branch-only commits. Only path absent from HEAD is `research/computations/branch_dx1_p044.out`. This branch name is absent from live enumeration. |

Two `refs/codex/turn-diffs/...` application snapshot refs also exist, at
`4f4cd1a7ce8836cdb51871ac01d2914b2fe95a05` and
`4190b258bac07e2d248a880a3102a457d59ff808`.
They are application captures, not research branches. They are recorded in the local inventory without promoting their contents to mathematical evidence.

Live GitHub enumeration returned exactly these seven branches:

| Live GitHub branch | Exact head SHA | Unique head commits / current commits from common base |
|---|---|---:|
| main | 7662a2ebb1dd561c1fb5e3c8958799b37d962c41 | 51 / 30 |
| research/e1-jet-rebuild-2026-10-07 | d5bed93e8c1ea09c2e11f0e096085da641819080 | 68 / 30 |
| research/entirely-thick-rees-valuation | a843888ce15b06247c576f8f717bec6b7ef5a352 | 70 / 30 |
| research/jet-discrepancy-order-one-2026-10-06 | f512d4d28da1fd6700aa4e6d2396229712d133d0 | 8 / 30 |
| research/normal-rational-carrier-classification | 4b936074f68038cfaa7ec51f5a960f23289627cd | 65 / 30 |
| research/ultra-resume-2026-10-06 | b16e4322c7b955147ce2ed241a1a0316a8e1a67a | same |
| ultra_mode | 2e53a7b5e9d4c96b5741ee4a4746a4a9ff0ad647 | local graph inspected |

All five divergent live branches above have common base
`98d71ddf8f8cceaad01bec43e94298699dcb5560`.
GitHub compare lists the changes from the merge base to the requested head,
not a direct tree diff against current HEAD. Missing local paths and overlap
were assessed separately, so a three-dot “added” path does not automatically
mean missing mathematics.

Network shell `git ls-remote` failed with DNS resolution failure; the connected
GitHub reader provided a successful live branch inventory. No Git fetch or
merge was performed.

## 2. Authority conflict and mathematical frontier

The current checkout README, `AUDITED_STATE_2026-10-07.md`,
`SUCCESSOR_HANDOFF_2026-10-07.md`, and newest acceptance records are the
continuation authority for this research line. They accept the all-quartic
carrier theorem for fixed C0 in characteristic zero, so every actual
quartic mate lane is closed and any hypothetical pair has both degrees
at least five.

Live remote main has a separate `research/STATE.md` and
`research/FRONTIER.md` described as canonical there. Their content is
mathematically older: they still list the MF6 (4,5) and normal quartic
remainder as open. Their generic “durable authority” wording must not
supersede the later acceptance record in this checkout. Wholesale merging
main would mix the two authority schemes and reopen already closed lanes.

The latest inherited quintic record accepts the coprime homogeneous
conormal exclusion, the G=Jbar=0 exclusion, the 2+4 residual exclusion,
and the complete actual conductor octic. At inherited HEAD, 3+3 has a frozen
all-mate proof under review, and the integral residual remains open.
This note leaves the evening team's subsequent reconciliations to its new
acceptance record.

Other live obligations survive separately:

1. normal quintics and other quintic normalization genera;
2. higher minimum carrier degrees and no general upper degree bound;
3. entirely thick pairs with both generic normal orders at least two;
4. the degree-six totally ramified split [2,2] carrier, whose mate scale is 8k;
5. common-quartic-ancestor incidence, including 22 family-two exceptional
   geometric points with their complete lower lift fibers, remaining
   nonendpoint top zeros, and the recorded positive-D2 directions;
6. a general theorem forcing a bounded minimum carrier, or excluding all
   carrier degrees, has not been established.

## 3. Recovered remote-only mathematical content

The four live remote-only research branches were missing from the cached
origin refs. Their newly recovered source contents are preserved as remote
snapshots rather than copied into active canonical note paths.

### Entirely-thick branch: 18 absent notes, still relevant

The branch `a843888...` contains 18 Oct 7 notes absent from the current
checkout. It retains the generic labelled transverse cluster, Rees
valuations, relative blowup cycle recursion, saturation and colon
recursion, equality-boundary quadric restriction, marked trisecant
coupling, and normalization/APic reformulation. These are new coverage
leads for the current session; their author labels are retained, without
a new independent proof audit.

The generic Noether excess budget is `ab/4-pq`. The notes explicitly
retain the limitation that normalized ratios do not bound cluster size
independently of p,q.

The strongest useful failure shields recovered are:

- `thick-root-budget-separation`: generic section coefficient c_i and
  special ruling-root multiplicity M_i live at different strata; no
  increasing lower bound c_i >= Phi(M_i) follows just from first
  exceptional geometry.
- `thick-segre-root-audit`: a trisecant root forces at least one selected
  common point, not all three. The established distinct-root bound
  survives, but stronger counting requires an actual coupling.
- `thick-boundary-carrier-rigidity`: at a=3p,
  F|Q=h^p R_F has exact h-order p and R_F is a repeated ruling divisor.
  Ambient lifting remains open; no power, factorization, or normalization
  is forced by this alone.
- `thick-apic-conductor-bridge` and
  `thick-generic-normalization-filter`: full inverse support and a
  positive Cartier/hyperplane relation are the correct normalization
  conditions. Clean conductor descent becomes automatic after a power;
  the global divisor class remains the obstruction.

The recovered sources were sent to the higher-carrier and thick-Rees
workers for degree-free synthesis.

### Order-one jet branch and e1 rebuild: geometry survives, mate searches superseded

The `f512d4d...` branch contains the 686-line order-one jet framework
and two old exact e1 companions. The main structural supplement recasts
ambient first symbols using the quadric comparison divisor R, the source
H0(I_R/Q(1,3)), and a finite target supported on 2R.

The `d5bed93...` branch contains a 490-line e1 rebuild plus three exact
sources. It preserves an explicit correction of the invalid implication
“a fixed residual ruling line itself excludes every possible mate.”
Its repaired argument uses the actual quartic carrier. Positive-defect
d2=1 sampling and elimination remained unfinished on that branch.

All of their actual quartic mate questions are superseded by the later
accepted all-quartic theorem. Their intrinsic R/2R description,
ambient-contact maps, and failed-shortcut record remain useful for
common-ancestor and degree-free programs. They were routed to the
local-cohomology worker without old verifier reruns.

### Normal-carrier branch: detailed failure history, no surviving quartic lane

The `4b936074...` branch contains a roughly 950-line Type-D classification
and resolution analysis, absent at its original local path. It records
endpoint and interior-point analyses, false attachment monotonicity,
corrected anticanonical coefficients, (-2)-tail Schur effects, and an
unfinished exact separation audit.

Its open normal-quartic status is superseded by the accepted complete
normal and all-quartic theorems. It is preserved as provenance and a source
of general resolution warnings, not a reason to restart normal quartics.

### Historical interrupted branch

The historical `2e53a7b...` tree has 37 paths absent from HEAD, mostly
old local-cohomology parity/seed scripts, validation snapshots, interrupted
scratch resultant sources, and dated notes. The exact names are retained
in the local inventory. The current canonical record already documents
the generator-coordinate/form confusion and corrected tensor. Neither an
old output nor an input script is promoted over the later accepted record.

## 4. Evidence files and continuation use

Directory:
`research/validation/2026-10-13-evening-branch-inventory/`.

- `remote-heads.json`: all seven live branch heads.
- `local-git-inventory.json`: exact local refs, graph counts, absent historical
  paths, worktree, tag and stash commands.
- `comparisons/*.json`: five successful GitHub merge-base comparisons.
  The ultra_mode comparison response records a transport failure;
  its exact live SHA and local graph remain available.
- `snapshot-manifest.json`: 25 recovered source snapshots with branch,
  head, original path, Git blob SHA and source URL.
- `snapshot-byte-checks.json`: all 25 saved sources match their returned
  Git blob SHA byte-for-byte, with SHA256 and byte lengths.
- `remote-snapshots/`: 18 thick notes, e1 rebuild, full jet framework,
  normal-carrier history, quadric-jet supplement, and three main synthesis
  files.

The byte checks validate archival identity only. They do not reverify
mathematics or count as new mathematical certificates.

A successor should use the new acceptance record for mathematical
status, this note for all-branch coverage, and exact snapshots for
previously untracked structural leads. No branch merge is needed for
research continuation.

