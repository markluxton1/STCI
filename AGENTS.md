# STCI research

The objective is to make consequential progress toward understanding or settling the unrestricted STCI problem. Prioritize mathematical insight and progress on the central question over the production of isolated results, computations, or investigations.

## Research judgment

Research agents have broad discretion to select questions and methods. Exercise independent mathematical judgment rather than following a prescribed research program.

Understand the existing mathematics and strongest applicable literature before investigating. Prefer questions that reveal general structure, connect existing frameworks, eliminate substantial possibilities, or resolve consequential uncertainties. Do not confuse tractability with importance.

Seek geometric, intrinsic, and conceptual understanding, using computation and examples wherever they are productive. Reconsider assumptions, formulations, and research directions as understanding develops. Be willing to abandon a planned investigation when a more consequential direction emerges or diminishing returns become apparent.

**Every new result requires a review of its generality and significance:** the work done by each hypothesis, the weakest justified conditions, the widest justified applicability to STCI, implications and interpretations, connections to previous work, and the obstacles to strengthening it.

Use that understanding to reassess the full body of results, and feed any further deductions back into the review. Follow the [iterative synthesis and stopping rule](research/MODEL.md#extract-implications-and-track-approach-gaps); finish when a full synthesis pass adds no material understanding, not merely when the original claim is verified. Independent proof review still governs new claims.

Choose the next task from the resulting current understanding. Name the next thing the approach needs to understand; do not assign the final theorem as the default task.

## Research context

Start with the [lane routes](research/INDEX.md#find-a-statement-proof-or-open-question) and [framework map](research/MAP.md).

Use `python3 scripts/research.py frameworks` to discover approaches, `show ID` for proofs and declared consumers, and `route LANE --compact` or `section ADDRESS` for scoped reading.

Before pursuing a question, understand what is already established, why the question remains unresolved, and how resolving it could advance the central problem. Use the relevant existing results and frameworks without treating them as restrictions on possible approaches.

## Mathematical standards

State hypotheses and conclusions precisely. Distinguish established results, conditional conclusions, conjectures, and speculation.

Justify the scope of claims, especially exclusions and assertions about all possible equation pairs. Do not promote computations, examples, or bounded investigations into general theorems without adequate justification.

Preserve the distinction between containment, scheme structure, and set-theoretic support. Consult the relevant mathematical frameworks for specialized requirements.

Prefer explanations that reveal why a result holds and how broadly it applies.

## Delegation and execution

Follow the [research workflow](research/MODEL.md#research-roles-and-delegation) and [contribution workflow](research/MODEL.md#contribution-workflow).

Delegate bounded technical tasks with clear scope and stopping conditions. Use the lightest model and reasoning effort sufficient for the task. Retire child agents when their retained context is no longer useful.

Independently review consequential mathematical claims before accepting them.

## Integration

Integrate reviewed mathematics into its appropriate owner. Reassess the significance of new mathematics for the central problem, existing results, and related frameworks. Preserve consequential connections, stronger formulations, and unresolved generalizations for future research.

Every PR must leave the research account consistent with the resulting understanding. Apply the [current-state acceptance requirement](research/MODEL.md#claim-propagation-at-integration) during the existing final review, including relevant unchanged summaries and next steps across the repository. Materially superseded claims or research tasks make the PR incomplete.

Keep files small, focused and independently retrievable. Remove superseded development narrative and split growing accounts at mathematical boundaries before they become costly to load or revise; preserve essential proof and evidence. Apply the [file-size and retrieval review](research/MODEL.md#compact-files-and-agent-retrieval), and run relevant [checks](research/MODEL.md#commands-and-integration).

**Progress is measured by advances in mathematical understanding, not by the volume of work produced.**
