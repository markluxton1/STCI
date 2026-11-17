# Working on the mathematics

| Home | What belongs there |
| --- | --- |
| [Results](results/INDEX.md) | Reusable statements, constructions, exclusions, counterexamples and reductions, with exact scope and proof routes |
| [Arguments](arguments/) | Complete proofs and coherent developments; Results can point to a section and retain distinct proof routes |
| [Literature](literature/README.md) | External statements, source references, checked hypotheses and applicability, and outstanding source checks |
| [Frameworks](MAP.md) | Evolving mathematical accounts of approaches: ideas, applicable results and literature, links to other approaches, missing implications, and active work |
| [Investigations](MAP.md#questions-and-active-work) | Active or planned bounded activities: the question, actual inputs, method, findings, and a clear stopping point |

[Computations](computations/README.md) and figures support this mathematics.
Keep small evidence with its proof when practical; share reusable code by
linking one copy. An open implication can live in a Framework until there is
bounded work to undertake.

## Research roles and delegation

The repository owns durable mathematics; agents are temporary workers, not
nodes in the mathematical file hierarchy. Responsibilities can be combined
when a single worker is sufficient, and delegation can recur at any depth:

- **Research coordinator:** maintain the overall mathematical picture, select
  priorities, and synthesize implications between Frameworks.
- **Framework or topic lead:** understand an approach, select bounded questions,
  delegate when useful, and interpret findings in that approach.
- **Bounded investigator:** work from a precise question, characteristic,
  hypotheses, source inputs, and stopping condition; use the lightest adequate
  model where selection is available. Report findings, supporting evidence,
  limitations, unresolved points, and potential consequences to the parent.
- **Reviewer and integrator:** temporary responsibilities, not standing ranks.
  Reviewers independently check consequential claims; integrators place reviewed
  mathematics with its owners and examine affected parallel Frameworks.

Give subagents narrow assignments without unnecessary inherited conversation
or whole-Framework context. Their reports flow to the delegating parent, who
may investigate further, escalate a consequential finding, do both, or stop.
Retire agents once their contributions have been incorporated. Avoid delegation
that adds more coordination than mathematical value.

## Progressive mathematical retrieval

When selecting an approach, start at the [Framework map](MAP.md) or
`python3 scripts/research.py frameworks`. Read the relevant Framework
`index.md` for substantive mathematical orientation, then retrieve only
coherent topic sections or companion documents pertinent to the question.
Follow exact Results, Arguments, literature, computations, and proof
dependencies as needed, including connections to other Frameworks. Use
`show ID`, `route LANE --compact`, and `section ADDRESS` (with line ranges
when helpful) instead of loading an entire Framework by default.

Minimize irrelevant context, never essential hypotheses or proof support.
Framework indexes should explain the approach and its mathematical interfaces;
topic documents should be independently retrievable where practical. Create
relationship documents only when substantive synthesis needs them. Existing
links, catalog records, and retrieval commands suffice unless a concrete
limitation requires additional infrastructure.

## Contribution workflow

1. **Open bounded work.** Specify the curve, characteristic, question,
   hypotheses, actual mathematical sources, stopping condition, and what
   either outcome changes. Use a dedicated branch and
   `investigations/<activity>/` workspace when persistent exploratory work
   is needed; temporary calculations, notes and provisional claims stay
   there. A small question need not create an Investigation.
2. **Investigate.** A lead may decompose the question into narrow tasks.
   Investigators return findings and limitations upward; the parent judges
   significance and decides whether to continue, report upward, or stop.
   Retrieve established statements and strongest applicable literature
   before attempting a new proof or computation.
3. **Review.** Apply [evidence and review](#evidence-and-review) to exact
   statements, hypotheses, proof routes, coverage, and consequential
   interpretations. An agent report is not a verified proof. Independent
   review is required for consequential new or modified mathematical claims;
   review depth follows mathematical significance.
4. **Integrate.** Put reviewed statements, proofs, negative findings,
   counterexamples, necessary evidence, and unresolved implications in
   their durable Results, Arguments, Frameworks, literature or computational
   owners. Reuse stable identifiers and proof addresses; link the authoritative
   argument instead of duplicating it. Do not retain the investigation report
   as a second permanent mathematical account.
5. **Propagate.** Check direct consumers, references and dependencies,
   including the originating Framework. Also scan the global map and other
   Framework indexes for plausible *conceptual* connections not already
   declared. Read detailed documents only for concrete connections; mark
   consequences as established, conditional or speculative. Update affected
   interpretations and the map where justified, without a blanket audit of
   every Framework for minor changes.
6. **Finish.** Review the integrated diff and consequential cross-Framework
   claims, run relevant structural and mathematical checks, then merge the
   durable work. Retire temporary branch-local notes with no independent
   mathematical value. Git history can preserve the research process.
   An Investigation may end with its main question unresolved.

One investigation PR may contain investigation, integration and final review.
Do not require scoring, promotion queues, review certificates, or administrative
records. Preserve existing review scope and mathematical evidence when moving
material. Frameworks may be created, combined, split or retired as the
mathematics warrants, independently of the agent hierarchy.

## Choosing bounded work

The central characteristic-zero objective for the fixed rational quartic is to construct or obstruct **actual proper homogeneous equation pairs** with sole support, equivalently maximal generic multiplicity. This equivalence follows from intersection-cycle degree exhaustion; it is a problem formulation, not a mechanism for bounding multiplicity. Before opening work, check the strongest applicable literature and existing repository proofs, then state explicitly:

- **Coverage:** which actual equation pairs, degrees, characteristics, singularity classes, or moving ideals are controlled, and what remains outside the scope;
- **Decision:** the exact theorem, construction, exclusion, or missing implication that either outcome could establish;
- **Consequence:** the logical bridge from that decision to unrestricted STCI, if any; and
- **Novel gap:** why established theory and the repository's existing Results do not already answer the question.

A bounded calculation can be useful without an unrestricted consequence, but label it bounded and do not infer general coverage. Prefer tests that create a new structural constraint or a concrete realization/coverage bridge over accumulating cases within an unchanged obstruction. The full-ideal torus, residual, and formal-normal methods are investigative tools, not presumed solutions; local cohomology and fixed-carrier criteria remain available when they offer a consequential new bridge. Do not launch a new classification solely because a neighboring family is unresolved.

State the curve, characteristic, actual source or candidate family, question,
and what either outcome changes. Constructing an example, closing a covered
sector, finding a counterexample, or identifying a missing comparison can
each be worthwhile. Declare the degree, power and regularity bounds needed
for any coverage claim. For a proposed computation isolate the real
mathematical input, its special strata, and a stopping outcome.

Ask whether two tests just express the same numerical budget. A useful next
test adds actual source, multiplication, embedding, support, or coverage
information. Revisit a closed family when the source, hypotheses, boundary
calculation or coverage genuinely changes. Read the Framework's open steps
and compare related approaches before choosing a bounded Investigation.

### Claim propagation at integration

When a finding changes the research state, give its **exact hypotheses and
characteristic**, the **owning proof or reproducible calculation**, its
**verification status** (proved, independently checked computation, or
conditional interpretation), and the **precise question it resolves**.
Identify the existing Result or Argument rather than creating a duplicate
account. When carrying it into Frameworks, Investigations or navigation,
retain its scope: a linear rank is not a nonempty incidence locus, a
weight-module match is not a canonical geometric isomorphism, and a
necessary boundary condition is not a sole-support realization. Check
nearby consumers and remove superseded open questions. This is a
lightweight review convention, not a new record or certificate.

## Evidence and review

Assess the literal statement, proof, jointly required premises, and scope of
review. Keep the distinctions among characteristic restrictions, necessary
conditions, fixed family conclusions, actual constructions and conjectures.
In the fixed quartic problem a formal thickening, projected model, generic
length or Chow cycle does not alone realize a proper pair with sole support.

A consequential new or changed proof route needs independent mathematical
review. Record what was read, checked or reproduced and its limitations on
that route. Results have no overall authority classification. Separate
independent arguments stay separately addressable.

### Corrections and conflicting claims

Compare the exact hypotheses and proof steps. State any unresolved difference
and preserve the counterexample or correction. Explain the mathematical scope
bridge before replacing a result or reusing it in another setting.

## Exact proof support and retention

Keep the smallest adequate exact support for a proof, including a reusable
script, necessary data, or a commit-pinned archived source. Explain the
mathematical domain, invariant assertion, coverage, and replay command at
the point of use. Record whether the supporting output was inspected or
replayed. A successful rank check does not identify its source space or
prove that it covers the relevant cases.

Retire duplicate accounts, output dumps, and execution records only after
checking for unique hypotheses, proof steps, correction or evidence and
their consumers. Replace essential certificates only with reviewed support
covering the same claim. Cite removed evidence by full Git commit and path.
Preserve useful counterexamples and genuinely different arguments.

## Files and fields

[Templates](../scripts/templates/) give the supported typed fields. Use
`STCI-R-####`, `STCI-A-####`, `STCI-F-####` and `STCI-I-####` for
cataloged records. An Argument may also be an ordinary Markdown development
in a topical subdirectory. Use `frameworks/<strategy>/index.md` for typed
Framework entries, with ordinary companion Markdown where helpful, and
`investigations/<activity>/index.md` for Investigation entries. Use ordinary
links for mathematical connections and the existing `relations` fields when
recording declared Result consumers or Investigation motivations. An
Investigation can have several motivating Frameworks. The catalog and
`frameworks` command derive navigation from these records and links.

Record each Result proof route's address, joint premises, and precise review
address. Alternative proof routes are separate entries; legacy evidence and
dependencies remain citations and do not imply a proof review. Metadata
addresses are repository-relative; `#fragment` is local to the current file.
Normal Markdown links are relative to the current file. Use `aliases` to point
a retired identifier to its exact surviving section. Preserve the Result
IDs and legacy locators in [results/INDEX.md](results/INDEX.md).

## Commands and integration

Install the [pinned requirements](../scripts/requirements-research.txt) in
Python 3.12 or later. From the repository root:

```sh
python3 scripts/research.py frameworks
python3 scripts/research.py show STCI-R-0022
python3 scripts/research.py route normal-orders --compact
python3 scripts/research.py section research/frameworks/formal-normal-geometry/index.md#fixed-setup
python3 scripts/research.py validate
python3 scripts/research.py catalog
python3 scripts/research.py catalog --check
python3 scripts/check_markdown_links.py --anchors
python3 -m unittest discover -s tests -v
```

Use `section ... --lines FIRST LAST` to inspect part of a large section.
Regenerate [CATALOG.md](CATALOG.md) after changing records or their addresses.
Run [the exact replays](computations/README.md) that support changed proofs or
moved scripts. Structural checks establish that links, records and declared
dependencies are usable; mathematical correctness and coverage still require
reading the proofs and checking their inputs.
