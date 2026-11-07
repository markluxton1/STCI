# Four research objects and their proof reviews

## Mathematical content

A **Result** is an independently reusable statement, construction, counterexample,
or reduction. Its own document contains the exact statement, hypotheses,
quantifiers, and limitations. Its complete proof is in that document or a
precisely identified Argument section containing the actual reasoning.
Existing mathematical expositions can supply such proof sections while the
repository is reconstructed; re-encoding a file is not a mathematical step.

An **Argument** gives a coherent complete development combining Results and
explaining their geometry. A **Framework** describes a strategy, actual inputs,
missing bridges, controls, and coverage obligations for an STCI or related
geometric question. An **Investigation** is a concrete motivated activity with
a question, method, findings, and unresolved work. Completing an activity does
not imply answering its motivating question.

Preserve independently useful lemmas, complete proofs, alternative arguments,
constructions, counterexamples, and exact hypotheses. Prefer intrinsic geometry;
when calculation remains necessary, explain its invariant assertion and coverage.
Exploratory code belongs to its Investigation. A Result keeps only the smallest
essential exact support in an optional `<claim>.support/` directory. Computations
and attachments are not additional research object types.

## Evidence and review

Results have no overall status or authority classification. The information
that matters is the statement, actual proof routes, their prerequisites, and
what each review checked. Record accepted, pending, or disputed review on the
precise route. No extra acceptance step follows an accepted proof review.
Repository integration approval is a separate project decision.

An accepted route needs an actual decision passage describing its checked
scope, what was read or executed, and qualifications. Source review and
independent reconstruction may be recorded factually; neither introduces a
second rank among Results. A reviewed conditional theorem stays conditional.
An unperformed calculation or a missing realization remains an explicit gap.
Do not infer acceptance from a file's name, identifier, location, or history.

Metadata checks declared structure, not mathematical truth, completeness of
premises, review sufficiency, reviewer independence, or exhaustive coverage.
Consequential arguments need substantive independent reconstruction, with
counterexamples and omitted hypotheses actively tested. Use the
[evidence rules](AUTHORITY.md) and [contribution instructions](CONTRIBUTING_AGENT.md).

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
Investigations; existing question records retain their exact formulations until
reviewed relocation. A claimed answer requires its precise mathematical scope.

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

Each accepted route must have noncircular accepted prerequisites. The checker
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
External literature citations are not fetched by deterministic validation.

Discover objects independently of the generated catalog. Malformed metadata
must fail rather than silently remove a record from discovery. README and INDEX
files are navigation, not objects. Untyped topic prose is recognized from
non-ID entries in the existing result index. The single pre-existing untyped
framework is a temporary serialization exception; adding metadata ends it.
Neither exception gives mathematical precedence. No migration manifest is kept.

Untyped Results retain exact statements, kinds, scope, evidence, review source
paths, aliases, references, corrections, and limitations. Their removed
classification fields are not retained elsewhere. Both compatibility validator
commands invoke the shared engine. The same route, identity, and path rules
apply to every serialization, without a fixed-size special collection.

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
review and explicit integration approval. Continue wider mathematical migration
only at the agreed user decision point. These project approvals are not
additional mathematical acceptance states.
