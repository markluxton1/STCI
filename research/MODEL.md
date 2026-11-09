# Four research objects and their proof reviews

## Mathematical content

A **Result** is an independently reusable statement, construction, counterexample,
or reduction. Its own document contains the exact statement, hypotheses,
quantifiers, and limitations. Its complete proof is in that document or a
precisely identified Argument section containing the actual reasoning.
Existing mathematical expositions can supply such proof sections while the
repository is reconstructed. Expository applications and restatements must
respect the literal scope of the Result.

An **Argument** gives a coherent complete development combining Results and
explaining their geometry. A **Framework** describes a strategy, actual inputs,
missing bridges, controls, and coverage obligations for an STCI or related
geometric question. An **Investigation** is a concrete motivated activity with
a question, method, findings, and unresolved work. Completing an activity does
not imply answering its motivating question.

Prefer intrinsic geometry. Distinguish a replacement proof from a geometric
reduction that still requires algebra or a computation whose mathematical
role or coverage still needs explanation.

## Evidence and review

Assess each claim by its exact statement, assumptions, proof, and review scope.
Branch, recency, path, identifier, catalog inclusion, and merge approval
supply no mathematical justification. STATE, FRONTIER, indexes, and research
relationships guide retrieval. Their claims depend on the mathematical homes.
Keep the antecedents of a conditional statement explicit. Distinguish a
necessary condition, a fixed-carrier conclusion, a finite reduction, an actual
construction, and an unrestricted theorem.

Record accepted, pending, or disputed review on the precise proof route.
An accepted route needs an actual decision passage giving its checked scope,
the assumptions used, what was read or executed, and the qualifications.
Acceptance covers the checked route and requires no further mathematical
approval. Results have no overall status or authority classification. Describe
source review and independent reconstruction factually and recover decisions
from the review passages themselves.

Independently reconstruct consequential arguments and changes in scope. Test
omitted cases, hidden hypotheses, counterexamples, dependency scope, and
characteristic restrictions. Distinguish generic claims from all-point
assertions, and formal or local existence from realization by global equations.
The checker verifies declared structure. Mathematical correctness, completeness
of premises, reviewer independence, review sufficiency, and exhaustive
coverage require substantive review.

For substantial contributions report the exact claim or question, curve,
characteristic, hypotheses and quantifiers, proof and evidence paths, review
scope, remaining dependencies, and any affected Framework or Investigation.
Keep unperformed calculations and missing realizations explicit. The
unrestricted characteristic-zero STCI question remains open until resolved by
an independently reviewed proof.

### Corrections and conflicting claims

Compare the exact scopes, proofs, and reviews of both claims. Report any
unresolved discrepancy, identify the precise disputed step, and preserve
useful corrections or counterexamples. Explain the scope bridge before
replacing one statement with another.

## Exact proof support and retention

Preserve independently useful lemmas, complete proofs, alternative arguments,
constructions, counterexamples, exact questions, and the smallest adequate
support. The Result owns its necessary exact support in an optional
`<claim>.support/` directory. Exploratory code and data belong to the owning
Investigation. Computations and attachments are support for the four
research objects.

For an essential computation, link its support from the proof's Evidence
section. Record the exact inputs, characteristic and source domain, invariant
assertion and geometric interpretation, coverage argument, usable command and
environment, and whether the result was inspected or replayed. A saved rank
still needs a proof of source identification and coverage. Keep a second
implementation only when it supplies distinct verification or an additional
argument.
Keep large generated artifacts out of ordinary Git. An essential external
artifact needs an accessible location, an integrity identifier, and an exact
account of the claim that depends on it. A checker, checksum, or regeneration
recipe requires separate evidence of completed execution.

Before retiring a necessary exact certificate, replace it with a reviewed
argument or compact exact certificate covering the same surviving claim.
Review the replacement and removal together. Check content and consumers for
unique corrections, proof steps, and exact inputs before dropping duplicate
certificates, logs, diagnostics, repeated PASS output, regenerable bulk
dumps, chronological handoffs, or migration manifests.

### Historical citations

Keep citations to historical proof and review sources, with their precise
scope. Cite a retired source at its full Git commit and path. If a source is
unavailable, check the surviving proof and its necessary evidence before
reusing the claim. Keep shared Git history and source branches intact during
working-tree consolidation.

## Files and fields

| Object | Location | Required mathematical section pointers | Work-state field |
| --- | --- | --- | --- |
| Result | `research/results/<claim>.md` | `scope`, `statement`; nonempty Limitations section | None |
| Argument | `research/arguments/<development>.md` | `scope`, `conclusion` | `draft` or `complete` |
| Framework | `research/frameworks/<strategy>.md` | `scope`, `bridges` | `proposed`, `in_use`, or `retired` |
| Investigation | `research/investigations/<activity>/index.md` | `scope`, `question`, `findings` | `planned`, `active`, `complete`, or `inactive` |

Typed objects have `id`, `type`, `title`, and `scope`. Results additionally have
`statement` and `proofs`; the other objects have a `status` describing only the
work state shown above. Unknown fields are rejected. Section pointers such as
`scope: "#scope"` address nonempty sections of the owning document. Put the
actual mathematics in those sections; a link elsewhere is not the statement.

Use stable `STCI-R-####`, `STCI-A-####`, `STCI-F-####`, and `STCI-I-####` IDs.
Keep identifiers when files move; resolve branch collisions before integration.
No allocation registry is needed. Optional `aliases` map former identifiers to
local sections, for example `STCI-Q-0001: "#question"`. Aliases must be unique
against all live IDs and other aliases. Questions live in Frameworks or
Investigations in the target structure. During reconstruction, FRONTIER can
hold unresolved interfaces awaiting a typed owner. Existing question records
retain their exact formulations until reviewed relocation. A claimed answer
requires its precise mathematical scope.

Templates: [Result](../scripts/templates/result.md),
[Argument](../scripts/templates/argument.md),
[Framework](../scripts/templates/framework.md), and
[Investigation](../scripts/templates/investigation.md). Template prose is not a
project claim.

## Proof routes

Each Result route has `name`, `at`, `using`, and `review`:

```yaml
proofs:
  - name: direct
    at: "#proof"
    using: []
    review:
      state: pending
      at: "#review"
```

`at` identifies an actual complete proof in the Result, an Argument, or an
existing mathematical exposition. It must be a local Markdown path and section,
not an external URL or a chain of proof outlines. Known Framework or Investigation
objects cannot substitute for a proof home. `using` lists the jointly required
Result premises; separate route entries are alternatives. Standard external
mathematics is stated and cited in the proof without mandatory local records.

`review.state` is `pending`, `accepted`, or `disputed`. An accepted review also
has `basis: inherited` or `basis: reconstructed`, describing whether the recorded
review comes from the actual source proof or the current independent
reconstruction. Both require a precise decision passage and its literal scope.
The basis field records what was reviewed; it confers no separate authority.
An empty `proofs` list means no proof route has yet been recorded.

Each accepted route must have noncircular accepted prerequisites. Only
accepted routes can ground those premises. The checker
starts with accepted routes having no cataloged premises and repeatedly adds
conclusions whose accepted routes have every premise in that set. It checks
every accepted route's premises against the final set. An independent accepted
alternative can ground a premise that would otherwise depend on a cycle.
A direct self-premise is invalid. Catalog and lookup display each route's review.

An existing untyped Result may document routes with exactly this structure;
its explicit accepted routes can ground other Results. Evidence lists alone
do not synthesize review decisions. Older administrative fields are removed,
not copied into source-information fields. Older flat dependency lists remain
references, not newly inferred joint proof routes; navigation cycles do not
establish circular mathematical reasoning.

Optional `supersedes` records a precise correction or replacement. State the
scope bridge or corrected assertion in a Supersession section. Its graph must
have no replacement cycles. A valid proof is assessed on its own mathematics;
replacement information is not a rank or automatic rejection of its conclusion.

## Research relationships

A relationship is stored once in an incident object, with an explanatory local
section and nonempty, nonduplicated endpoint groups:

```yaml
relations:
  - kind: motivates
    from: [STCI-F-0001, STCI-F-0002]
    to: [STCI-I-0001]
    at: "#purpose"
```

| Kind | Source types to target types | Meaning |
| --- | --- | --- |
| `uses` | Results/Arguments to Arguments/Frameworks/Investigations | Inputs or applications |
| `motivates` | Frameworks to Investigations | Why the activity is useful |
| `produces` | Investigations to Results/Arguments | Actual mathematical outputs |
| `informs` | Investigations/Results/Arguments to Frameworks | Findings that change strategy |
| `limits` | Results to Frameworks/Investigations | Exact restrictions from a failure or counterexample |

Every Investigation has at least one Framework motivation. A grouped edge is
one joint relationship, not all pairwise implications. Research cycles are
legitimate. The derived graph helps retrieval; actual proofs establish the
mathematical implications. Proof ownership is not itself a premise.

## Discovery, paths, and compatibility

Metadata paths are repository-root-relative; `#fragment` addresses the current
document. Reject external schemes, absolute paths, queries, missing files or
sections, `..` metadata segments, and escaping symlinks. Ordinary body links
can use parent-relative paths inside the repository. Explicit support files
and images are checked for availability; existence does not verify their content.
Legacy evidence and audit fields allow external citations. Deterministic
validation does not fetch them or external literature.

Discover objects independently of the generated catalog. Malformed metadata
must fail rather than silently remove a record from discovery. README and INDEX
files are navigation, not objects. Untyped topic prose is recognized from
non-ID entries in the existing result index. The single pre-existing untyped
framework is a temporary serialization exception; adding metadata ends it.
Neither exception gives mathematical precedence. Discovery has no fixed record
count or migration manifest.

Untyped Results retain exact statements, kinds, scope, evidence, review source
paths, aliases, references, corrections, and limitations. Keep their ID
entries and the untyped topic links in [results/INDEX.md](results/INDEX.md)
for discovery and validation. Preserve the exact formulation of each untyped
question, including [STCI-Q-0001](questions/cartier_projection_models.md).
Question and activity states describe open work. The same route, identity, and
path rules apply to every serialization. The two compatibility commands,
`research/computations/validate_records.py` and
`research/computations/validate_result_records.py`, invoke the shared engine.

## Commands and integration

Use Python 3.12 or later and the pinned dependency:

```sh
python3 -m pip install -r scripts/requirements-research.txt
python3 -m unittest discover -s tests -v
python3 scripts/research.py validate
python3 scripts/research.py catalog
python3 scripts/research.py catalog --check
python3 scripts/research.py show STCI-R-0022
python3 scripts/check_markdown_links.py --anchors
```

`catalog` rebuilds [CATALOG.md](CATALOG.md); validation, lookup, and freshness
checking do not write files. `--root /path/to/repository` before the subcommand
selects another checkout or a temporary fixture. The generated view contains
no timestamps and displays actual route reviews and activity states. It is the
only generated research artifact.

Every enforced mechanical rule needs a positive and deliberately invalid test.
Temporary miniature repositories exercise malformed fields, accepted and
unreviewed premises, alternative routes, circular justification, identities,
aliases, paths, compatibility, research cycles, and deterministic generation.
Scientific controls belong to their owning Investigation or Result support;
a passing execution supplies no coverage theorem.

Independent infrastructure review checks parsing, validation, tests, determinism,
and authoring burden. Independent mathematical review reconstructs consequential
proofs and checks preservation of hypotheses, intermediate results, counterexamples,
and necessary support. Retrieval/reuse evaluation is separate from both.
Keep the reconstruction PRs stacked and unmerged into main until the requested
mathematical review, retrieval/reuse evaluation, and explicit integration
approval. Continue wider mathematical migration only at the agreed user
decision point. Integration approval is a project decision separate from
scoped proof review.
