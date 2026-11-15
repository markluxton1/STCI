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

## Contribution workflow

1. Retrieve the exact statement, proof, and dependencies before reusing a
   claim. For an approach start with the [framework map](MAP.md); read the
   [source record](literature/README.md) and the theorem where the application
   depends on its hypotheses.
2. Extend an existing mathematical owner when refining its proof, example,
   or interpretation. Give a reusable result a stable identifier and an
   exact statement; place its proof where the reasoning reads naturally.
   Keep exploratory findings in their investigation until their durable
   role is understood.
3. After a finding, check nearby proofs and approaches, including other
   Frameworks that use the same mechanism. Update interpretations, open
   steps and bounded work where the mathematical consequence changes. State
   whether the connection is proved, conditional, or still missing a map.
   Link the authoritative argument instead of copying it. Update the
   [map](MAP.md) when the route between approaches changes.
4. Create, merge, split or retire Frameworks as the mathematics changes. A
   completed Investigation can leave its question open. Move the exact
   result, proof, informative negative finding, or remaining question to
   its durable home; retain a completed Investigation only for independently
   useful material that would lose context there.

Give parallel agents disjoint questions or editable paths, shared proof inputs,
and stopping conditions. Integrate by mathematical owner and retire the agents
after their findings are used. Preserve stable IDs, proof addresses and review
scope when moving material; repair internal links and regenerate the catalog.

## Choosing bounded work

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
