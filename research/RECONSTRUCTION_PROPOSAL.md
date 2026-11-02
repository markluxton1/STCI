# Repository reconstruction proposal

**Decision requested:** approve this information model and bounded pilot before
implementation. This proposal changes no mathematical statement, proof, status,
or existing research path. It is based on the tracked `main` tree at
`e4e10f8d8b525285bed3ec016f0e97adb67a0bdc`. Untracked attachments and unmerged
research branches are outside the migration input.

## 1. What the assessment found

The repository has 988 tracked files, including 317 Markdown files. There are
36 ID-bearing result records, one ID-bearing question record, 95 files in
`research/synthesis/`, 469 in `research/computations/`, and one framework file.
These are counts of the tracked tree, not assessments of mathematical quality.
The current [authority policy](AUTHORITY.md), [schema](RESULT_SCHEMA.md),
[topic map](MAP.md), and [contribution instructions](CONTRIBUTING_AGENT.md)
already make several distinctions this reconstruction should preserve.

Three independent, read-only assessments covered inventory/tooling, the
information model, and the torus pilot's mathematical boundaries. They identified
these design constraints:

- Useful complete proofs already exist in synthesis and supplement files.
  Moving their conclusions into a catalog cannot replace those arguments.
- A result can have alternative proofs with different prerequisites. For
  [R-0022](results/quartic_44_filtered_exclusion.md), exact source computations
  support one route; the surface route does not require those computations.
  The [fourth-extension argument](synthesis/intrinsic_fourth_extension.md)
  also retains a stronger intermediate classification with its own provisional
  status. Retaining only the final exclusion would lose mathematics.
- [R-0025](results/ci_fixed_sextic_jet_rigidity.md) contains a complete proof
  and exact computational support. Its fixed carrier, mate degree, source map,
  rank argument, and different implementation replay histories all matter.
- The two current record validators overlap. One parses metadata with regular
  expressions; the other uses YAML and hardcodes the 36 existing result IDs.
  Neither is a suitable unchanged schema engine for four object types. The
  existing link checker can be reused after adding tests.
- Current scope and review must be read from proofs and evidence. Existing
  `proved` labels and earlier acceptance prose do not independently certify
  the mathematics to be reconstructed.

The design therefore separates reusable claims, coherent explanations, research
strategies, and concrete activities while preserving their mathematical links.
It does not make a larger graph the principal deliverable.

## 2. Four objects, with distinct responsibilities

| Object | Required mathematical content | Boundary |
| --- | --- | --- |
| **Result** | One independently usable exact statement, construction, counterexample, or reduction; literal hypotheses and quantifiers; complete proof or an exact complete-proof location; limitations; review scope | An established conditional theorem remains conditional. A reduction does not supply its unresolved computation or realization. |
| **Argument** | A readable development with its setup, proof steps, geometric explanation, uses of results, and precise conclusion; alternative proofs when useful | It cannot strengthen a referenced result through paraphrase. A missing bridge must be stated where the reasoning stops. |
| **Framework** | A strategy connecting mathematics to an STCI question or a substantive geometric question arising from the account; available inputs, proposed bridges, known controls and failures, coverage obligations, and selection criteria | State the actual STCI relevance or independent geometric value without inventing a bridge. Frameworks can support constructive and obstructive investigations independently. |
| **Investigation** | A precise question or task, framework motivation, declared family and bounds, method, findings, unsuccessful mechanisms, unresolved steps, and owned exploratory code/data | Completing an activity does not mean resolving its motivating question. A negative result on one family does not exclude other families. |

Extract an intermediate result when its statement can be applied independently,
its proof has a definite boundary, or another development can reuse it. Do not
create a record for every paragraph. Preserve useful alternative proofs and
counterexamples even when they reach the same final conclusion.

A short result normally owns its complete proof. A long proof may live in an
Argument, addressed by an exact section. That section must contain the proof,
not another chain of proof-outline links. Arguments can restate a lemma for
readability with its ID and literal scope; they need not become catalogs of
citations. A Result's reference to its owning Argument is an expository link,
not a mathematical premise.

## 3. Target file structure and navigation

```text
AGENTS.md                         concise retrieval and working instructions
README.md                         problem and mathematical entry routes
research/
  INDEX.md                        human reading routes by mathematical question
  MAP.md                          human explanation of mechanisms/connections
  MODEL.md                        object/schema/authority/contribution rules
  CATALOG.md                      generated locator and relationship back-links
  results/
    <claim>.md                    one reusable statement, existing R ID retained
    <claim>.support/               optional essential exact proof support
  arguments/
    <development>.md              complete connected exposition
  frameworks/
    <strategy>.md                 strategy, open bridges, selection criteria
  investigations/
    <activity>/
      index.md                    question, method, findings, outputs, next tests
      <exploratory code/data>      only useful mathematical support
scripts/
  research.py                     parse, validate, build catalog, resolve IDs
  check_markdown_links.py          existing link checker, with tested behavior
  requirements-research.txt        pinned YAML dependency
  templates/                      four small authoring templates
tests/
  test_research.py                 positive and intentionally invalid fixtures
  test_markdown_links.py
.github/workflows/                ordinary CI, no validation-record archive
```

Use descriptive filenames without dates for mathematical owners. Keep stable
IDs when files move. Navigation and attachments are not additional research
object types. No graph database, maintained edge registry, required diagram,
permanent migration inventory, chronological archive, or standalone computation
category is introduced.

The human INDEX and MAP explain the mathematics; the generated CATALOG locates
objects by ID, type, title, status, scope link, and incoming/outgoing relations.
The catalog is the only generated research artifact. A `show ID` command can
resolve aliases and print proof locations and neighboring objects; it reads
the same metadata rather than maintaining another index.

At the end of migration, absorb the useful content of STATE, FRONTIER, and the
decision guide into reading routes, Frameworks, and Investigations. Combine
authority/schema/contribution/artifact rules in MODEL and the short AGENTS entry
point. Remove redundant pages only after their distinct mathematical and
operating content has survived review. During coexistence, current authority
rules remain in force for unmigrated material. Infrastructure must not silently
rewrite the mathematical status pages.

## 4. Metadata and proof routes

Use ordinary Markdown with YAML front matter parsed by a safe YAML loader that
rejects duplicate keys. Do not extend the current regular-expression parser to
simulate nested YAML. Keep one schema implementation and a short documented
specification; do not add a general schema framework.

Common required fields are `id`, `type`, `title`, `status`, and `scope`.
`scope` is a local heading fragment containing the readable exact setting;
it is not a second copy of the hypotheses. Optional `aliases` maps a former
identifier to a local fragment. Optional `relations` records research links.
IDs use `STCI-R-####`, `STCI-A-####`, `STCI-F-####`, and `STCI-I-####`.
Existing R IDs are retained; new IDs are allocated on the branch and duplicate
allocation is resolved before merge. There is no ID allocation service.

| Type | Status values | Additional required fields |
| --- | --- | --- |
| Result | `provisional`, `established`, `disputed`, `superseded` | `statement` fragment; `proofs` list (possibly empty only for provisional/disputed proposals) |
| Argument | `draft`, `complete` | `conclusion` fragment |
| Framework | `proposed`, `in_use`, `retired` | `bridges` fragment |
| Investigation | `planned`, `active`, `complete`, `inactive` | `question` and `findings` fragments; at least one framework motivation |

These statuses describe different things. In particular, an Argument marked
complete does not promote its results, and an Investigation marked complete may
leave an open question. The body's Findings section states the outcome and
remaining scope even for a planned activity. Framework status is not a ranking.

Each Result proof route has `name`, `at`, `using`, and `review`.
`at` is a repository-root-relative Markdown path and fragment, or a local
fragment for a proof in the Result itself. `using` is a list of cataloged
Results actually relied on as mathematical premises in that route. Standard
external mathematics is stated and cited in the proof; it need not become local
records merely to fill the graph. Independently useful local facts should be
cataloged as the pilot and later batches encounter them.

`review` has `state: pending | accepted | disputed` and an `at` location for a
concise decision stating the exact route reviewed, qualifications, and what was
read or executed. Source review and reconstruction review must be distinguished
in that passage. An inherited decision is not a new independent reconstruction.
A checked provisional result may remain provisional: review and promotion are
different decisions. Unchecked alternative proofs can coexist with a checked
proof when their individual states are explicit.

An illustrative fragment, using **existing** IDs without changing their status:

```yaml
id: STCI-R-0022
type: result
title: Quartic-pair exclusion for the fixed characteristic-zero quartic
status: established
scope: "#scope"
statement: "#statement"
proofs:
  - name: surface
    at: "research/arguments/quartic-pair.md#surface-proof"
    using: [STCI-R-0020]
    review:
      state: accepted
      at: "#review-surface"
  - name: filtered-contact
    at: "research/arguments/quartic-pair.md#filtered-contact-proof"
    using: [STCI-R-0020]
    review:
      state: pending
      at: "#review-filtered-contact"
```

The paths above illustrate the proposed syntax and are not existing proof
locations. Actual prerequisites, retained certificates, and review decisions
will be reconstructed before writing such metadata. One route may have several
joint premises; separate `proofs` entries represent alternative routes. They
must not be flattened into one required conjunction.

Exact support attachments are linked from the proof's Evidence section. Their
mathematical role, source domain, coverage argument, environment/command, and
expected invariant assertion belong in that section. The Result owns the
smallest necessary exact certificate; an Investigation owns the wider experiment.
Do not duplicate all exploratory outputs into Result attachments or retain logs
solely to record past execution. Necessary exact outputs and a record that an
implementation was *not* replayed can be mathematically material.

Existing `conditional` and `exact_reduction` labels cannot be translated by a
lookup table alone. Preserve the literal conditional statement or reduction and
its remaining task; determine establishment and review separately from the
actual evidence. Record unresolved disagreements as disputed and do not use a
stronger formulation as an unconditional premise. Preserve existing aliases and
supersession information; a `supersedes` list on a replacement Result requires a
passage proving the scope bridge or stating the correction. No reciprocal field
is maintained: inverse links are derived.

## 5. Relationships and the directed hypergraph

The graph is derived from local documents. There is no second authoritative
graph file. Each proof route contributes one edge from its jointly required
`using` Results to its conclusion Result, with the complete proof location as
witness. This records a declared mathematical dependence; it does not establish
the implication. Proof text and independent review do that work.

Research relationships are a separate small vocabulary:

| `kind` | Source types → target types | Meaning |
| --- | --- | --- |
| `uses` | Results/Arguments → Arguments/Frameworks/Investigations | Explain an application or input; no theorem implication is inferred |
| `motivates` | Frameworks → Investigations | Identify why the concrete activity is worth doing |
| `produces` | Investigations → Results/Arguments | Link actual mathematical outputs, with their own status |
| `informs` | Investigations/Results/Arguments → Frameworks | Explain a revision or improved strategy |
| `limits` | Results → Frameworks/Investigations | State precisely what a counterexample or scoped failure rules out |

Every relation has `kind`, nonempty `from` and `to` ID lists, and an `at` passage
explaining the relationship. It is stored once, in an incident object; its
explanation belongs in that document. A grouped edge describes a joint
relationship, not all pairwise implications and not a Cartesian product of
independent claims. Different edges remain distinct. Every Investigation must
be a target of at least one `motivates` edge, possibly from several Frameworks.

```yaml
relations:
  - kind: motivates
    from: [STCI-F-0001, STCI-F-0002]
    to: [STCI-I-0001]
    at: "#purpose"
```

Navigation cycles are legitimate: a Framework motivates an Investigation which
informs the Framework. A Result can point to its proof in an Argument that also
uses the Result in later sections. Do not impose acyclicity on this graph.

For declared proof dependencies only, reject direct self-premises and require
each established Result to have at least one accepted route grounded in
established Results without circular reliance. Mechanically, admit only Results
whose status is `established`: begin with their accepted routes having no
cataloged premises, then repeatedly admit an established Result with an accepted
route whose every premise is itself established and already admitted. Provisional,
disputed, and superseded Results never enter this admitted set, even if they
retain accepted review decisions. Remaining established Results fail this
structural check. An alternative acyclic route can ground a result even when
another route participates in a cycle. This checks declared structure; it does
not check completeness of premises, truth, or mathematical sufficiency.
Assumptions of a conditional statement belong in its statement and proof, not
in `using` as if an unproved antecedent were an established fact.

Questions remain mathematical content within Frameworks and Investigations,
not a fifth object type. Preserve Q-0001's exact formulation and limitations
when moving it; alias `STCI-Q-0001` to its surviving Question section. More
general open questions belong to Frameworks, finite or family-specific tasks
to Investigations. A claimed resolution needs a precise answering Result and
scope explanation in the body. A completed activity alone is not an answer.

## 6. Infrastructure and its tests

The separate infrastructure PR will add templates and one deterministic tool,
initially without moving research or changing claim status. It will support:

```text
python3 scripts/research.py validate
python3 scripts/research.py catalog --check
python3 scripts/research.py show STCI-R-0022
python3 -m unittest discover -s tests
python3 scripts/check_markdown_links.py --anchors
```

During coexistence, discover migrated records by `type` in the four object
directories, validate legacy records through an explicit read-only adapter, and
resolve IDs against their union. Records referenced by the legacy result index,
front-matter-bearing object files, and files in new object locations must not
silently disappear when parsing fails. Untyped legacy exposition remains
reachable through existing navigation without acquiring new object status.
Existing schema validation and CI remain until the new tool
has tested equivalent legacy coverage; then remove the duplicate engines and
their hardcoded result count. Do not add an evergreen migration manifest.

The tool checks syntax/types, duplicate YAML keys and IDs/aliases, required
fields, allowed statuses, ID/type/location consistency, relation endpoint types
and grouping, local files and fragments, missing explicitly linked proof support, required review
locations, declared proof grounding, and generated-catalog determinism. Resolve
paths inside the repository, including decoded paths and symlinks. External
literature links are disclosed citations, not silently accepted local proofs;
network availability is not a deterministic theorem check. Branch-only source
URLs must not satisfy the migrated complete-proof requirement.

Every enforced rule needs a positive fixture and an intentionally invalid
fixture. Tests run in temporary miniature repositories, never by corrupting
research files. Include these pairs:

| Positive example | Intentionally invalid example |
| --- | --- |
| Each of the four object types, including a conditional established Result | Missing required field, unknown type/status, ID in the wrong directory |
| Unique IDs and an alias to a Question section | Duplicate ID/key/alias or alias colliding with a live ID |
| Existing local proof, section, and exact support | Missing file/fragment/certificate, escaped repository path or escaping symlink |
| Two alternative accepted routes with different joint premises | Scalar/malformed `using`, unresolved premise, direct self-premise, only circular accepted routes |
| An accepted route plus an unchecked alternative | Established Result with no accepted complete-proof route or review passage |
| A reviewed provisional Result retained without grounding an established claim | Established consumer relying solely on provisional, disputed, or superseded premises |
| A valid Framework → Investigation → Framework research cycle | Wrong relation endpoint types, empty group, or relation owned by a nonincident object |
| Complete Investigation with an explicitly open question | Investigation without a framework motivation |
| Byte-identical catalog from repeated runs and shuffled discovery order | Edited/stale generated catalog |
| Valid Markdown heading and escaped/encoded local link | Broken path/anchor; links in fenced code must remain ignored |
| Existing legacy schema accepted without rewriting its mathematics | Malformed legacy record hidden by failed discovery |
| Mixed legacy/migrated references and an alias resolving to the same union | Duplicate cross-schema ID or unresolved migrated-to-legacy reference |

Mechanical tests cannot detect an altered hypothesis, a wrongly merged pair of
proof routes, missing mathematical content, or an unjustified question resolution
from prose alone. Those are explicit human/agent review obligations. Do not
claim otherwise. Existing mathematical checks that remain in CI also need
appropriate positive and deliberately false controls before their enforcement
is carried forward into a migrated mathematical owner; a passing replay alone
is insufficient. Infrastructure owns the schema, catalog, and link-checker
fixtures. Scientific verifier controls belong to the pilot or bounded migration
batch that takes ownership of each verifier. A substantial scientific code
change becomes a separately reviewed prerequisite, not an implicit infrastructure
edit. Unchanged legacy CI jobs may continue during coexistence, with their
existing coverage disclosed. No inherited check is represented as having the
new control coverage until those controls actually exist and pass. Completion
of the repository migration requires such controls for every retained check.

## 7. Torus-limit pilot: scope, outputs, and open boundaries

The pilot's center is **full flat torus limits and generation of moving ideals**
for the fixed embedded quartic. The first bounded application is type (6,6),
with an explicitly specified power bound N and Hilbert polynomial when used.
It does not assume a uniform N or a finite classification of fixed ideals.
Pilot acceptance concerns preservation of existing mathematics, independent
proof review, retrieval/reuse evaluation, and precise Investigation records for
unresolved tasks. It does not require solving those tasks. Any new bounded
computation first declares N, the polynomial, characteristic, and family; an
actual supported ideal or a new comparison theorem is optional research with
its own scope and independent review.

| Current mathematical home | Pilot destination and preservation requirement |
| --- | --- |
| [Global equations: supported Hilbert locus](synthesis/global_equations_and_constructions.md#the-supported-hilbert-locus-and-its-full-torus-boundary) | Reusable support/polynomial preservation statement and complete geometric proof; composite Argument explaining the boundary and missing deformation step |
| [Attracting loci and generator incidence](synthesis/torus_attracting_strata_and_generator_incidence.md) | Framework for directional and opposite-limit loci; Investigations testing actual ideal generation on moving families |
| [Explicit sextic limits](synthesis/toric_sextic_residuals_and_limits.md), especially §§2–4.1 | Separate eigenpair quotient bound, full-limit construction, and useful local/colon lemmas; preserve coherent residual and Hilbert–Burch arguments |
| [Embedded quotients and endpoint descent](synthesis/toric_quotients_and_endpoint_descent.md) | Bounded auxiliary criterion and application, retaining actual source spaces and constant embedded-family hypotheses |
| [Weight restrictions](supplements/EQUIVARIANT_DEGREE_BOUNDS.md) | Required invariant-generator/one-eigenform dependence, with its characteristic and trace hypotheses intact |
| [Entire finite modification and movement](synthesis/tropical_thickenings_and_endpoint_duality.md) | Only the comparison investigation's necessary statements and their proof closure; no wholesale migration of unrelated material |
| [Exact finite identity verifier](computations/verify_toric_quotients_and_residual_limits.py) | Identify precisely which finite identities support which claims; keep exploration in Investigations and essential certificates with their Results |
| [Characteristic controls R-0020](results/quartic_conormal_characteristic_jump.md), [R-0021](results/quartic_mu4_degeneration.md) | Link existing scoped results; follow the required proof dependence without reopening unrelated closed cases |

This is a proposed content boundary, not a predetermined file count. Follow a
lemma's actual dependencies when needed. If closure becomes too large, retain a
clear existing proof location and make the expansion a separate reviewable
batch; do not replace an unexamined dependence with an assertion.

Candidate reusable units include graded eigenvector lifting, the bounded
supported-limit argument, the eigenform sextic quotient-length bound, the
explicit saturated three-generator full limit, the local multiplicity rule and
colon calculation used there, and the constant-quotient equation-space criterion.
The source texts mark newer contributions as reviewed provisional; cataloging
them must not promote them. The attracting-locus account is an explicitly open
research formulation. There is no independent proof certification in Phase 1.

Preserve these distinctions through the pilot:

1. The full saturated Hilbert-limit scheme, the initial forms of two chosen
   equations, the normal-cone initial ideal, and the fundamental cycle retain
   different information. Keep embedded and endpoint structure and extra
   generators wherever they matter.
2. The recorded sextic full-limit control has generator degrees 6,6,10 and
   residual degree 32. It is outside the sole-supported Hilbert incidence. It
   cannot supply a sole-supported boundary point or an exclusion of all sextic
   pairs.
3. The sharp length-eight quotient bound concerns proper eigenform sextic pairs,
   in the source's stated characteristics. It does not cover arbitrary
   mixed-weight pairs. Two independent degree-six sections do not establish
   generation of the entire saturated ideal.
4. Fixed degree, a bounded supported locus, constant transverse quotients,
   prescribed degenerations, and the unbounded STCI question have different
   quantifiers. A finite generator test needs its regularity bound; a broad
   exclusion needs its coverage theorem.
5. The endpoints of a finite modification and the two opposite Hilbert-limit
   directions are different constructions. Comparing their defects requires an
   actual comparison or specialization map. An endpoint budget is not such a map.
6. The unrestricted characteristic-zero STCI question remains open in the
   current account. Positive-characteristic constructions retain their actual
   characteristic and degree qualifications.

Planned pilot Investigations ask for an actual invariant supported ideal or
declared family, which opposite full limits occur, where the moving saturated
ideal has the prescribed two generators, and whether quotient data specialize
through a proved comparison. A bounded construction or exclusion is useful on
its own; it does not become a universal conclusion through a graph edge.

Unmerged all-degree VGIT, residual-cycle-incidence, and homogeneous-descent work
is not part of this main-based pilot. Integration of any such work requires a
specified committed contribution and its own scope review.

## 8. Independent review and migration sequence

The sequence has two explicit user decision points:

1. **Architecture approval now.** This proposal PR contains only this document.
   After approval, implement and test the infrastructure in a separate PR.
   Fold the approved design into MODEL/templates and remove this temporary
   proposal document; do not preserve an administrative design archive.
2. **Pilot approval after reconstruction and independent review.** Submit a
   distinct mathematical pilot PR. Present its mathematical findings,
   preservation decisions, review, and retrieval evaluation before any broader
   migration. Do not merge disputed mathematics or begin repository-wide
   migration merely because tooling passes.

For the pilot and each later batch, the author reconstructs the complete
arguments, identifies independently reusable intermediate results, and explains
proposed deletions alongside their mathematical replacements in the PR. This
temporary PR description can map old passages to surviving owners; no permanent
intake or audit registry is added. Historical wrappers and redundant logs are
removed only after that preservation check. A wholesale rename is insufficient.

The mathematical reviewer must not have authored the reconstruction. They read
the underlying proofs, independently reconstruct the important steps, challenge
characteristic and degree hypotheses, try relevant counterexamples, inspect
necessary exact support, and compare removed material with the replacements.
Review distinguishes (i) an intrinsic proof replacing a calculation, (ii) a
geometric reduction still requiring a necessary calculation, and (iii) a
computational assertion awaiting explanation. Disagreements block the affected
mathematical merge; isolated undisputed work can be split into another PR.

Separately, a reader unfamiliar with the reconstruction performs these tasks
against the old and new organizations:

- Find the exact eigenpair bound, its proof, characteristic scope, and why it
  does not settle arbitrary sextic pairs.
- Recover the degree-ten generator example and determine why it lies outside
  the sole-supported locus.
- Reuse a local multiplicity, colon, or purity lemma in a stated application,
  checking all hypotheses rather than just following a link.
- Identify the moving-ideal generation test and the missing quotient-to-Hilbert
  comparison, including where a regularity or coverage result is needed.
- Decide which concrete investigation can change a framework and what finding
  would justify continuing or abandoning that particular activity.

Judge correct scope, successful proof reconstruction, visibility of reusable
lemmas and connections, and unnecessary reading required. Record a concise
assessment in the PR; timing or link counts alone do not establish improvement.
No permanent benchmark dashboard or verification archive is needed.

After pilot approval, migrate remaining material in dependency-aware bounded
batches: complete one coherent argument and its reusable claims/activities,
review it together with proposed removals, repair paths and CI, and update the
reading routes and strategy descriptions together. Questions, provisional
mathematics, negative findings, and distinct alternative arguments all have
homes. Remove obsolete categories only when no unique mathematical content or
necessary support remains there. Do not establish a standing integration branch
or compulsory worktree workflow.

## 9. Delegation and completion criteria

Use lightweight agents for inventories, typed-link maintenance, metadata
extraction, and routine operations. Use stronger reasoning for architecture,
mathematical exposition, and independent proof review. Escalate an identified
hard or disputed problem rather than starting every task at maximum effort.
Bound tasks by inputs, outputs, and completion criteria; keep authorship separate
from independent review, and end completed assignments. The lead integrates and
checks the work and carries out repository operations.

The reconstruction is complete when an agent can discover a useful statement
with exact scope, reconstruct its proof, reuse intermediate results across
directions, and select worthwhile investigations from the mathematical evidence;
all useful mathematics has reviewed homes; obsolete categories are removed;
and each enforced mechanical check has positive and deliberately invalid tests.
The number of graph edges or moved files is not a completion criterion.
