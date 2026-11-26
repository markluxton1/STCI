# Working on the mathematics

| Home | What belongs there |
| --- | --- |
| [Results](results/INDEX.md) | Reusable statements, constructions, exclusions, counterexamples and reductions, with exact scope and proof routes |
| [Arguments](arguments/) | Complete proofs and coherent developments; Results can point to a section and retain distinct proof routes |
| [Literature](literature/README.md) | External statements, source references, checked hypotheses and applicability, and outstanding source checks |
| [Frameworks](MAP.md) | Current mathematical accounts of approaches: ideas, applicable results and literature, coverage, connections, and missing implications |
| [Investigations](MAP.md#questions-and-active-work) | Bounded activities: the current question, actual inputs, method, supported findings, and remaining work or completion |
| [Strategic queue](investigations/proof-audit/knowledge-gain-priorities.md) | Which question or phenomenon to investigate next, the expected understanding and reassessment point; link the mathematical account |

[Computations](computations/README.md) and figures support this mathematics.
Keep small evidence with its proof when practical; share reusable code by
linking one copy. An open implication can live in a Framework until there is
bounded work to undertake.

## Research roles and delegation

The repository owns durable mathematics; agents are temporary workers, not
nodes in the mathematical file hierarchy. Ordinary responsibilities can be
combined when a single worker is sufficient; the distinct reviewers required
for a substantive research PR are specified [below](#six-independent-review-perspectives).
Delegation can recur at any depth when authorized by the parent:

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

1. **Open bounded work.** Specify the curve, characteristic, question or
   phenomenon, known inputs and material unknowns, expected understanding,
   initial probe and reassessment point. A theorem or solution bridge need
   not be known in advance. Use a dedicated branch and
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
   substantive research PRs use the [six perspectives](#six-independent-review-perspectives).
   Review depth follows mathematical significance. Review every new result for
   generality, implications, connections and gaps, and [iterate the synthesis](#extract-implications-and-track-approach-gaps)
   with the full body of results until another pass adds no material understanding.
4. **Integrate.** Put reviewed statements, proofs, negative findings,
   counterexamples, necessary evidence, and unresolved implications in
   their durable Results, Arguments, Frameworks, literature or computational
   owners. Reuse stable identifiers and proof addresses; link the authoritative
   argument instead of duplicating it. Do not retain the investigation report
   as a second permanent mathematical account.
5. **Propagate.** Reconcile the resulting understanding across proof owners,
   Frameworks, questions, navigation and priorities, including conceptual
   connections beyond declared dependencies. Mark consequences as established,
   conditional or speculative. If integration exposes a further implication or
   changes an assumption, return to synthesis and the required proof review.
   Maintenance-only changes need no artificial mathematical synthesis.
6. **Finish.** Review the integrated mathematical state, including relevant
   unchanged consumers, under the [current-state acceptance requirement](#claim-propagation-at-integration).
   Resolve material inconsistencies before declaring the PR ready. Run relevant
   structural and mathematical checks and [review file size and retrieval](#compact-files-and-agent-retrieval),
   then merge the durable work. Retire temporary branch-local notes with no
   independent mathematical value.
   Git history preserves the research process. An Investigation may end with
   its main question unresolved.

One investigation PR may contain investigation, integration and final review.
Do not require scoring, promotion queues, review certificates, or administrative
records. Preserve existing review scope and mathematical evidence when moving
material. Frameworks may be created, combined, split or retired as the
mathematics warrants, independently of the agent hierarchy.

## Choosing bounded work

The central characteristic-zero objective for the fixed rational quartic is to construct or obstruct **actual proper homogeneous equation pairs** with sole support, equivalently maximal generic multiplicity. This equivalence follows from intersection-cycle degree exhaustion; it is a problem formulation, not a mechanism for bounding multiplicity. Understanding the relevant geometry can advance this objective before a construction or obstruction is visible. Check the strongest applicable literature and repository proofs, then state:

- **Question and scope:** the phenomenon or uncertainty, relevant objects and hypotheses, and the scope of any proposed coverage;
- **Expected understanding:** what examples, counterexamples, a landscape, a comparison or a new formulation could teach;
- **Relation to STCI:** why that understanding matters, distinguishing established implications from possible connections; and
- **Novel gap:** why established theory and the repository's existing Results do not already answer the question.

A known route to a theorem or unrestricted consequence is not an admission condition. A supported account of a moduli space, its strata or what a comparison forgets can change the research direction. Prefer new understanding over accumulating cases within an unchanged obstruction. The full-ideal torus, residual, formal-normal, local-cohomology and fixed-carrier methods are tools, not presumed solutions. An unresolved neighboring family alone does not justify a classification.

Bound the initial commitment rather than predetermining the outcome. At the
reassessment point, state what was learned, what remains unknown, and whether
a consequential next question warrants continuation, redirection or stopping.
The question may evolve; an unresolved main question need not keep the present
contribution open. Declare degree, power and regularity bounds for coverage
claims. For computation isolate the mathematical input and its special strata.

Ask whether two tests just express the same numerical budget. A useful next
test adds actual source, multiplication, embedding, support, or coverage
information. Revisit a closed family when the source, hypotheses, boundary
calculation or coverage genuinely changes. Read the Framework's open steps
and compare related approaches before choosing a bounded Investigation.

### Extract implications and track approach gaps

For every new or materially changed result, review the following as part of
mathematical acceptance, not only when choosing a new investigation:

- **Generality and hypotheses.** Explain what each hypothesis does and where
  it enters. Seek the weakest sufficient conditions the argument supports and
  the widest justified applicability to our problem. Test whether existing
  results remove a restriction or give a stronger conclusion. Distinguish a
  necessary hypothesis, a limitation of this proof, and an untested extension;
  do not claim minimality without evidence. State what prevents a stronger
  result and what would need to change to obtain it.
- **Implications and interpretation.** Determine what follows alone and in
  combination with existing results, what the result explains, and what other
  formulations reveal about the problem. Give exact deductions and hypotheses,
  including consequences that close or redirect an existing question.
- **Connections with previous work.** Reconsider the full body of results,
  including older work and approaches outside the originating Framework.
  Identify actual maps, common mechanisms, obstructions or comparisons. Explain
  what structure survives and what is lost; similar terminology or numerical
  bounds alone do not establish a connection.
- **Remaining gaps.** State the revised coverage and what still prevents
  further progress: a missing proof, source or realization condition, comparison,
  or bridge beyond the covered class. Identify what resolving it would change
  and a bounded informative test when one is known. Preserve genuine unknowns
  rather than inventing a next task or requiring a solution of unrestricted STCI.

This is an iterative synthesis. Begin with the new result and existing accepted
mathematics. Use the changed understanding to reassess that whole body of work;
feed further implications, stronger formulations, connections and revised gaps
back into the next pass. Independently review consequential new or modified
claims before treating them as established inputs. A correctness check of the
original result or a single pass through its direct dependencies is insufficient.

Cover the full suite conceptually using the map, catalog and Framework accounts;
follow authoritative statements and proofs wherever a comparison depends on
their exact scope. These aids locate mathematics and are not proof authority.
Use bounded workers for coherent clusters when useful. Reuse valid review and
carry forward unaffected conclusions, but reopen them when a new insight changes
their interpretation. Full-suite coverage does not require loading every proof
at once or reproving every theorem on each pass.

Continue while another pass yields material mathematical understanding. Stop the
synthesis loop after a full pass finds no material change to justified generality,
implications, connections, remaining gaps or research decisions. This is a stable
assessment of the available evidence, not proof that no further insight exists. Do not use a
fixed round count, cosmetic rewriting or reviewer agreement as the stopping
test. If progress needs unavailable evidence or genuinely new research, preserve
the precise gap and consequence for use; do not claim it resolved or stable by
repetition. Report the scope and reason for stopping in the existing review,
without a pass-by-pass ledger.

Meeting that stopping condition does not complete the PR or waive repository
maintenance. Finish all resulting integration, propagation, consolidation,
navigation/catalog updates and required verification before declaring completion.
The final repository must consistently reflect the resulting understanding;
do not defer these updates as low-value cleanup or leave known stale accounts
for a later PR. Lack of further mathematical insight does not excuse unfinished
maintenance. Apply the [current-state acceptance requirement](#claim-propagation-at-integration)
to the actual updated files.

Keep current gaps with their canonical Framework or Investigation. Place
proved deductions with their proof owners and link across frameworks rather
than duplicating them. Update the existing ranked list only when a decision
changes. Replace superseded gaps; do not create another queue or require a
per-result checklist or historical ledger.

For a repository-wide sweep, use the framework map to cover each
mechanism, then commit reviewed batches as they are ready. Each batch
updates the canonical approach gap and any existing open question it
materially changes, including negative controls and the precise limits
of a bridge. Keep the current ranked list as the only queue; postpone
reranking until the sweep has compared mechanisms across the repository.

At that decision point, compare the actual next tasks by expected understanding,
transfer to other approaches, or a credible way across a realization or coverage
barrier. A narrow test does not inherit its framework's priority or coverage.
Explain the choice against the strongest relevant alternative, including a
neglected exploratory question when one is apparent. Momentum and the existing
rank are not comparative evidence; preserve uncertainty if the order is not
supported. Nearness to an STCI solution matters only with a specific reason it
is close. Pursue the chosen question with focused, reviewed commits, and
reassess when findings change its promise or scope.

### Claim propagation at integration

Every PR must leave its affected research account describing the current
mathematical state. The task lead owns this reconciliation in the same PR;
it is part of completion, including for deductions established during review.
Maintenance-only changes need no unrelated mathematical edits.

When a finding changes the research state, give its **exact hypotheses and
characteristic**, the **owning proof or reproducible calculation**, its
**verification status** (proved, independently checked computation, or
conditional interpretation), and the **precise question it resolves**.
Identify the existing Result or Argument rather than creating a duplicate
account. When carrying it into Frameworks, Investigations or navigation,
retain its scope: a linear rank is not a nonempty incidence locus, a
weight-module match is not a canonical geometric isomorphism, and a
necessary boundary condition is not a sole-support realization.

Trace the affected claims through their proof owners, Frameworks, active
Investigations, navigation and strategic queue. Use claim identifiers,
terminology, links and the actual mathematical implications to find consumers;
declared dependencies and changed lines alone do not establish coverage.
Rewrite superseded conclusions, limitations and next steps in place. Retain
useful intermediate lemmas, counterexamples, distinct proof routes and essential
evidence, with their precise scope; retire the obsolete tasks and chronological
checkpoints around them. Keep the current mechanism and gap in the Framework,
and the next research decision and its rationale in the existing queue.

The existing final reviewer must check this integrated account as well as the
new proof, including the [synthesis coverage and stopping judgment](#extract-implications-and-track-approach-gaps).
Proof acceptance, synthesis completion and endorsement of next work are distinct
judgments. To endorse a proposed or retained priority, review its comparison of
actual tasks and current coverage. If that comparison was outside review scope,
report the priority as unassessed rather than validated by the proof review.
Starting from an affected ordinary entry point, verify that a reader
can recover what is established, its scope, what remains unresolved and the
reason for the proposed next work without reconstructing the discovery history.
Read relevant unchanged summaries, conclusions and open questions against the
final claims. A materially false scope summary, superseded active task or missing
propagation that misdirects subsequent research blocks completion even when the
new proof and structural checks pass. Recheck affected conclusions after review
revisions; a review of an earlier state does not cover changed implications.

In the existing PR description, state the resulting mathematical understanding
and link the affected owners, or state that mathematical scope and priorities
are unchanged. The review reports synthesis and integration coverage, the
stopping judgment, file-retrieval limitations and any material unresolved
condition. Use those existing surfaces and the assigned reviewers; no separate
reviewer for each synthesis pass, per-result checklist, approval registry or
historical ledger is required.
Structural checks validate records and links; they do not establish semantic
agreement between a theorem, its summaries and the next research task.

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

### Six independent review perspectives

For a substantive research PR, assign a distinct independent reviewer to each
perspective below. Reviewers challenge the actual mathematics and its meaning;
prior acceptance prose and the producer's preferred strategy are not premises.

| Perspective | Required contribution |
| --- | --- |
| Correctness | Reconstruct consequential statements and proofs, including quantifiers, jointly required hypotheses, computations and scope. |
| Journal editorial review | Judge contribution, explanation, notation, proof organization and mathematical economy; identify changes that improve understanding rather than cosmetic preferences. |
| Seasoned algebraic geometer | Examine the intrinsic geometry, conceptual mechanisms, hidden assumptions and stronger geometric interpretations. |
| Generalizations, implications and connections | Seek weakest justified conditions, widest applicability, alternative interpretations and deductions using the full body of prior work; distinguish proofs from missing bridges. |
| Relevant literature | Discover and evaluate transferable mathematics: stronger results, new maps, constructions, invariants, interpretations, counterexamples and consequential questions. Verify primary-source hypotheses and limits, compare existing proofs, and pursue open preprints or related work if access fails. Feed concrete connections into the synthesis; citation checking alone is insufficient. |
| General research picture | Reassess established coverage, remaining gaps and actual next tasks, including neglected alternatives; identify stale conclusions and unsupported priority claims. |

Choose each reviewer's model and reasoning depth for the depth of judgment
required, using the strongest supported route when warranted. Mathematical
understanding is the objective. Cost awareness should reduce irrelevant context,
duplicated work and unnecessary artifacts; it must not justify shallow review,
an insufficient route or premature stopping. Explicit user routes remain binding.

The lead adjudicates findings against the proofs and sources, obtains independent
review of consequential new deductions, and feeds the resulting understanding
through the [full-suite synthesis](#extract-implications-and-track-approach-gaps).
Reuse reviewers for coherent follow-up and final integration; do not rerun six
unchanged reviews merely to count another pass. Cover changed conclusions and
their dependencies, and preserve material unknowns. Agreement is not the stopping
criterion, and proof acceptance does not endorse the research ranking.

Report the six perspectives' substantive dispositions and limits in the existing
PR/review surfaces, without six new reports or a review ledger. The final review
must verify compact proof ownership and [current-state consistency](#claim-propagation-at-integration),
including relevant unchanged consumers. Reaching the synthesis stopping condition
still requires all resulting propagation, consolidation, navigation, catalog and
verification work. Maintenance-only PRs need the affected checks, not an artificial
six-perspective mathematical review.

### Literature as mathematical discovery

The purpose of the literature perspective is to improve understanding and
research choices, not simply check attribution. Begin with the exact question
and known results; search adjacent geometries and generalizations, references
and later work. Follow promising sources far enough to identify the mechanism,
not merely the theorem's title. Prefer accessible primary texts, including
arXiv preprints and author copies. If one is inaccessible, seek related papers,
earlier results or a stronger generalization; state the remaining access gap.

For each consequential connection, explain what the external result supplies,
which actual objects and maps in our problem match its hypotheses, what it
changes relative to existing repository work, and where the transfer stops.
A useful finding may be a reusable construction, a new interpretation, an
exact negative control, a simplification, or a concrete unexplored question.
Develop a bounded application or test when the connection supports one; do
not generate speculative research directions merely to fill a list. Give
the mathematical findings to the lead for the full synthesis, revise proof
owners and existing questions when warranted, and preserve the distinction
between proved external inputs, independently reviewed deductions and
provisional transfers. Do not assume that matching hypotheses of a related
theorem settle a different realization problem. Citation and novelty checks
remain necessary safeguards, but are not the principal deliverable.

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

### Compact files and agent retrieval

Minimize the context needed to understand and safely revise a mathematical
contribution. Each file should have a coherent mathematical purpose that can be
read and reviewed comfortably. Before expanding a large account, remove repeated
summaries and superseded development narrative; split independent mechanisms,
proofs or source computations into focused owners with a short overview and exact
links. Put bulky executable support in linked support files. A section-address
tool does not excuse an account that keeps accumulating unrelated developments.

Preserve all necessary hypotheses, dependencies, proof steps, distinct arguments
and reproducible evidence. Avoid fragments that force an agent to reconstruct one
argument from many tiny files. Line counts and growth are warning signals, not
substitutes for mathematical judgment or arbitrary acceptance thresholds.

The final review must examine new or substantially expanded files for this cost.
Walk through locating a principal claim, reading its necessary proof and sources,
and making a bounded revision: unrelated material should not dominate the load.
If avoidable size, duplication or fragmentation materially impedes that task,
refactor before completion and verify the moved proof addresses and consumers.
Apply the same standard to guidance and Frameworks; keep one owning account and
short pointers elsewhere.

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
