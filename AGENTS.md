# STCI agent retrieval protocol

Read [research/INDEX.md](research/INDEX.md) first; for mathematical orientation
use [research/MAP.md](research/MAP.md) before dated notes. This file governs
retrieval and assessment; it establishes no mathematical conclusion.

1. Identify the exact curve, characteristic, hypotheses, and question. When
   studying intersections consider containment and residual components before
   imposing sole support. A vertical exceptional component need not be an
   additional curve downstairs.
2. Use the index and map to find the smallest relevant statement, proof, or
   question. Read its actual dependencies; do not ingest the whole record.
3. Check hypotheses, quantifiers, characteristic, proof scope, limitations,
   and what a review actually checked. Distinguish necessary conditions,
   fixed-carrier conclusions, finite reductions, and unrestricted theorems.
4. A Result states its exact mathematics in its own document. Its complete
   proof may be in a precisely addressed Argument section, which must contain
   the actual reasoning. Follow evidence when a claim or review is missing;
   do not invent an acceptance decision.
5. On conflict, compare both scopes and proofs, consult the
   [evidence rules](research/AUTHORITY.md), and report unresolved issues.
   Recency, branch names, identifiers, and file location do not settle them.
6. STATE, FRONTIER, indexes, and graph relationships guide retrieval. They
   supply neither extra proofs nor a separate rank among Results.
7. Preserve useful intermediate lemmas, complete arguments, corrections,
   counterexamples, exact scope, and necessary support. Remove redundant
   wrappers only after checking the surviving mathematical homes. Git keeps
   history; no administrative classification or queue is needed.
8. Record accepted, pending, or disputed review on precise proof routes.
   Separate alternatives and their joint premises. An accepted route needs
   noncircular accepted prerequisites; metadata consistency is not a proof.

For substantial work report the exact claim, assumptions, proof/evidence paths,
review scope, and remaining dependencies. Use the
[contribution instructions](research/CONTRIBUTING_AGENT.md) and
[object model](research/MODEL.md). There is no overall Result status field.

## Navigation and integration

Coordinate INDEX, MAP, STATE, FRONTIER, and the decision guide when reading
routes or research direction change. Preserve informative negative findings
and independent constructive approaches. The decision guide is not a
compulsory agenda. Review consequential proof rewrites and scope changes
independently; editorial organization supplies no new implication.

Prefer intrinsic geometric reasoning. When calculation remains necessary,
state its invariant assertion, exact source and coverage, and smallest
checkable support. Distinguish an intrinsic replacement proof, a geometric
reduction requiring algebra, and a computation still needing explanation.

Use full torus limits: retain Hilbert polynomial, support, embedded and endpoint
structure, and additional generators. Separate the full ideal from two initial
forms, normal-cone ideals, and cycles. For a bounded supported locus, consider
both opposite limits and attracting families where useful; impose actual
generation on moving ideals. Do not require fixed limits to be two-generated
or infer coverage from selected fixed points. State degree, power, regularity,
and characteristic bounds. Independent geometric arguments remain available.

## Working commands and branches

Run `python3 -m unittest discover -s tests -v`,
`python3 scripts/research.py validate`, and
`python3 scripts/research.py catalog --check` after structural changes.
`catalog` explicitly regenerates the view. Every enforced mechanical rule needs
positive and deliberately invalid examples. Exploratory code belongs to its
Investigation; essential exact proof support stays with its Result.

Keep the reconstruction PRs stacked and unmerged into main until the requested
mathematical review, retrieval/reuse evaluation, and explicit integration
approval. Integration approval is separate from a scoped proof-review decision.
