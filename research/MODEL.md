# Four research objects: authoring and structural rules

## Coexistence and authority

This specification implements the approved reconstruction architecture. The
existing [authority policy](AUTHORITY.md), [result records](results/INDEX.md),
and their evidence remain authoritative during the pilot. This infrastructure
does not migrate mathematics, establish claims, or change inherited statuses.
The temporary [architecture proposal](RECONSTRUCTION_PROPOSAL.md) remains on the
stacked branches until integration is approved; it is not a permanent archive.

A **Result** is an independently reusable statement, construction, counterexample,
or reduction. Its own document must state the exact mathematics, hypotheses,
quantifiers, and limitations. A complete proof may be in a precisely identified
Argument section. That section must contain the actual proof; a chain of
references or proof outlines is insufficient.

An **Argument** is a coherent exposition combining results and explaining their
geometry, with complete reasoning and a precise stopping point. A **Framework**
explains how mathematics could advance an STCI question or a substantive related
geometric question, including missing bridges, known failures, and coverage
obligations. An **Investigation** is a concrete activity motivated by one or more
Frameworks, with a precise question, method, findings, and unresolved work.
Finishing an activity does not imply answering its question.

Preserve independently useful intermediate lemmas, alternative proofs, negative
findings, and counterexamples. Prefer intrinsic geometric proofs; when a
calculation remains necessary, explain its invariant assertion and why its
source and cases cover the claim. Exploratory code and useful data belong to
their Investigation. Only the smallest essential exact proof support belongs
beside a Result in an optional `<claim>.support/` directory. Attachments and
computations are not additional research object types.

Statements and proofs govern mathematical meaning. Metadata checks structural
consistency, not mathematical truth, exhaustive coverage, completeness of
premises, or correctness of a review decision. Do not promote a claim merely
because an old document says `proved` or `established`. Preserve inherited
conclusions and review scope while distinguishing them from independently
reconstructed proofs. A reviewed provisional claim can remain provisional.

## Files and minimal metadata

Use these locations; filenames describe mathematics rather than chronology:

| Type | Location | Status values | Required local section pointers |
| --- | --- | --- | --- |
| `result` | `research/results/<claim>.md` | `provisional`, `established`, `disputed`, `superseded` | `scope`, `statement`; a nonempty Limitations section |
| `argument` | `research/arguments/<development>.md` | `draft`, `complete` | `scope`, `conclusion` |
| `framework` | `research/frameworks/<strategy>.md` | `proposed`, `in_use`, `retired` | `scope`, `bridges` |
| `investigation` | `research/investigations/<activity>/index.md` | `planned`, `active`, `complete`, `inactive` | `scope`, `question`, `findings` |

All objects have YAML front matter with `id`, `type`, `title`, `status`, and
`scope`. Section pointers such as `scope: "#scope"` refer to nonempty sections
in that same document. Put the full hypotheses and quantifiers in Scope and
the full claim in Statement; a pointer is not permission to move those elsewhere.
Optional `aliases` and `relations` are omitted when unnecessary. Unknown fields
are rejected to catch misspellings. Authoring templates are available for
[Results](../scripts/templates/result.md),
[Arguments](../scripts/templates/argument.md),
[Frameworks](../scripts/templates/framework.md), and
[Investigations](../scripts/templates/investigation.md). Templates are not claims.

Use stable `STCI-R-####`, `STCI-A-####`, `STCI-F-####`, and `STCI-I-####` IDs.
Keep existing R IDs when their statements are reconstructed. Allocate IDs on
the working branch and resolve collisions before merge; no registry is needed.
An optional alias map preserves former identifiers as precise local sections:

```yaml
aliases:
  STCI-Q-0001: "#question"
```

Questions are sections of Frameworks or Investigations. Existing legacy Q
records remain intact until a reviewed migration preserves their exact question
and assigns an alias. An alias cannot collide with a live ID or another alias.
An answering Result and a scope explanation are needed to claim resolution;
an Investigation's `complete` status does not make that claim.

## Proof routes and establishment

Results also have `statement` and `proofs`. Each proof route contains `name`,
`at`, `using`, and `review`. `using` lists jointly required cataloged Results;
separate routes are alternatives. Standard external mathematics is stated and
cited in the proof; it need not be cataloged simply to enlarge the graph.

```yaml
proofs:
  - name: direct
    at: "#proof"
    using: []
    review:
      state: pending
      at: "#review"
```

`at` identifies the complete proof in this Result or a new-schema Argument,
using a local fragment or a repository-root-relative Markdown path and fragment.
External links, including branch URLs, cannot satisfy this requirement. Review
passages may be in local Markdown and must identify the actual scope reviewed,
what was read or executed, and qualifications. `review.state` is `pending`,
`accepted`, or `disputed`. An accepted review must explicitly declare
`basis: inherited` or `basis: reconstructed`; either value requires the actual
decision passage. This extra field distinguishes preservation of source review
from independent reconstruction without an audit registry. Neither value proves
that the reviewer was independent: that is checked in substantive review.

An established Result must have an accepted noncircular route grounded in
established premises. The structural rule admits only new-schema Results with
`status: established`: begin with accepted routes having no cataloged premises,
then admit a Result if one accepted route has every premise already admitted.
Provisional, disputed, and superseded Results cannot enter this set even if
their retained review is accepted. A direct self-premise is invalid. An accepted
acyclic alternative may ground a Result even when a different route participates
in a cycle. Empty `proofs` is allowed only for provisional or disputed proposals.

The legacy adapter preserves original statuses; it does not synthesize accepted
proof routes or convert old `proved` labels into new-schema establishment.
Legacy IDs resolve for research relationships and provisional proof work.
An established new-schema route cannot be grounded solely through an unmigrated
legacy record. Such a premise needs an explicitly reconstructed Result and
accepted route, preserving its inherited conclusion and actual review scope.
This is a structural coexistence boundary, not a withdrawal of legacy authority.

A conditional theorem states its assumptions literally. An unproved antecedent
is not an established premise in `using`. A reduction retains its unfinished
calculation or realization task; it does not become existence or nonexistence.
An optional Result `supersedes` list requires an explicit Supersession section
explaining the corrected statement or scope bridge. Inverse links are derived;
supersession cycles are invalid.

## Research relationships

Store a relationship once, in an incident object, with an explanatory section:

```yaml
relations:
  - kind: motivates
    from: [STCI-F-0001, STCI-F-0002]
    to: [STCI-I-0001]
    at: "#purpose"
```

`from` and `to` are nonempty lists without repeated endpoints. A grouped edge
describes one joint relationship, not pairwise mathematical implications.
`at` is a nonempty section of the owning document. Every Investigation must be
motivated by at least one Framework; the relation may be owned by either endpoint.

| Kind | Source types → target types | Meaning |
| --- | --- | --- |
| `uses` | Results/Arguments → Arguments/Frameworks/Investigations | Mathematical inputs or applications |
| `motivates` | Frameworks → Investigations | Why the activity is worth undertaking |
| `produces` | Investigations → Results/Arguments | Actual outputs, with their own status |
| `informs` | Investigations/Results/Arguments → Frameworks | Findings that change or clarify strategy |
| `limits` | Results → Frameworks/Investigations | Exact scope ruled out by a failure or counterexample |

The graph is derived from these local declarations and each proof route's joint
premises, conclusion, and proof location. It is a navigational model, not an
additional authority. Research cycles are legitimate: a Framework can motivate
an Investigation which informs it. A Result's reference to its proof in an
Argument is ownership, not a mathematical self-premise. Keep these relationships
separate from proof grounding.

## Paths, discovery, and legacy coexistence

Metadata paths are repository-root-relative; `#fragment` means the current
document. Reject external schemes, absolute paths, queries, missing files or
fragments, `..` path segments, and symlinks escaping the repository. Ordinary
body links can use parent-relative paths that stay inside the repository.
Required sections must contain text. Explicit proof-support links and images in
new-schema documents are checked for local availability; presence of a linked
certificate or diagram does not validate it.
Literature URLs remain citations and are not fetched by deterministic checks.

The tool discovers object files independently of the generated catalog. Any
metadata-bearing file in an object location must parse; a missing or malformed
header cannot silently drop an object from the catalog. New Argument files and
Investigation entrypoints require metadata. README and INDEX navigation files
are not objects. Legacy topic prose is recognized from non-ID entries in the
existing result index. The one untyped pre-existing framework,
`research/frameworks/formal-normal-geometry.md`, is a temporary explicit prose
exception, not an automatic Framework record; adding metadata ends the exception.
Other untyped Framework files must supply metadata. No migration manifest is
maintained. Remove the exception when that prose is reconstructed.

Legacy R/Q records retain their IDs, statements, status vocabulary, and source
fields. The adapter validates their original schema and result-index consistency
without hardcoding the present record count, resolves references against the
legacy/new union, and labels their authority as inherited. Historical external
evidence remains disclosed and is not certified remotely. A new alias cannot
mask a still-live legacy ID or an inherited `legacy_ids` alias. Legacy aliases
resolve to their owning documents without fabricated section pointers. Preserve
the original dependency-cycle rejection on the legacy-only subgraph; it does
not impose ordinary acyclicity on new alternative proof routes. Untyped
expositions stay reachable through existing navigation; being in a directory
does not promote them.

The old validators and scientific CI jobs remain unchanged during this phase.
Remove duplicate schema engines only after equivalent compatibility coverage
has been demonstrated and the transition is reviewed. Scientific verifier
controls belong to the pilot or migration batch taking ownership of each
verifier; a substantial scientific change is separately reviewed. Do not claim
new negative-control coverage for an inherited check before it exists and passes.
Every retained check needs such coverage before final reconstruction completion.

## Commands, tests, and review

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

`catalog` explicitly rebuilds [CATALOG.md](CATALOG.md). Validation, `show`, and
`catalog --check` do not write files. `--root /path/to/repository` before the
subcommand selects a repository for temporary fixtures or another checkout.
The catalog contains no timestamps; sorting and grouped relationships are
deterministic. It is the only generated research view. Human reading routes and
the mechanism map continue to explain the mathematics.

Every enforced mechanical rule needs positive and deliberately invalid tests.
Temporary miniature repositories exercise malformed metadata, joint and
alternative proof routes, forbidden grounding, identities and aliases, path
containment, legacy compatibility, research cycles, and catalog determinism.
These fixtures are synthetic examples, never fabricated project results.

Before presenting infrastructure, an independent nonauthor reviews the code,
tests, parsing and grounding behavior, coexistence, determinism, and authoring
overhead. Consequential mathematical reconstruction additionally requires a
reviewer who reconstructs the underlying proofs and checks preservation of
intermediate results, counterexamples, hypotheses, and exact support. Automated
checks cannot replace that work or the separate retrieval/reuse evaluation.

Keep this infrastructure and the torus pilot in separate, reviewable stacked
PRs. Do not merge either into `main` before the pilot's independent mathematical
review, retrieval/reuse evaluation, and explicit user approval. Phase 2 changes
no mathematics or computation ownership. Record unresolved pilot tasks precisely;
solving them is not a prerequisite for reconstructing the existing cluster.
