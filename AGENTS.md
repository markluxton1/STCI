# STCI agent retrieval protocol

Read [research/INDEX.md](research/INDEX.md) first; for mathematical orientation use [research/MAP.md](research/MAP.md) before the dated note directory. This file governs **how to retrieve and assess** research; it does not establish new mathematical conclusions.

1. Identify the exact curve, characteristic, carrier hypotheses, and question before retrieving claims. When exploring intersections, consider the broader formulation \(C\subset V(F,G)_{\\mathrm{red}}\) and possible residual components rather than assuming STCI at the outset; do not mistake vertical exceptional degeneration for an additional component downstairs.
2. Use the thematic map and short navigation index to find the smallest relevant topic/result/question. Read only the relevant files and their stated dependencies. Do not ingest the entire research record by default.
3. Check the **exact hypotheses, quantifiers, epistemic status, limitations, and evidence** of every claim before relying on it. Distinguish a necessary condition, a fixed-carrier theorem, a completed exclusion, and an unrestricted STCI theorem.
4. If an indexed result is absent or not yet promoted, follow its evidence links and explicitly report the authority gap. Never manufacture a canonical result file or treat an acceptance note as a promoted result.
5. On conflicting statements, do not resolve by timestamp or branch name alone. Record both scopes and evidence, consult [authority rules](research/AUTHORITY.md), and flag unresolved conflicts.
6. Treat `research/STATE.md` and `research/FRONTIER.md` as current navigation summaries, not independent theorem authority. For mathematical claims consult promoted result records and their evidence; flag any unreconciled legacy passages.
7. Retain useful mathematical content and the smallest adequate proof or computational support. Historical paths, audit wrappers, logs, inventories, and repeated certificates have no independent retention requirement. Replace or remove them only after checking that distinct arguments, corrections, counterexamples, and necessary support survive in reviewed mathematical homes. Preserve the exact scope of accepted claims; do not reopen closed cases merely to reorganize files.
8. New results enter as proposals with evidence and independent review status; promote them only through a reviewed change to canonical result/question records.

For substantial work, report: precise claim used, assumptions, supporting path(s), unresolved dependencies, and whether the claim is promoted or provisional. Do not equate a computational reduction with a completed computation.
New research contributions should follow [the proposal and audit checklist](research/CONTRIBUTING_AGENT.md). Canonical metadata can be checked with `python3 research/computations/validate_records.py`.

## Navigation maintenance contract

- `research/STATE.md` summarizes established knowledge and open mathematical status; only change mathematical status when supported by canonical evidence and the applicable review process.
- `research/FRONTIER.md` describes current investigations, alternative open interfaces, and next tests; update it when research direction changes, without treating historical wording as immutable.
- `research/RESEARCH_DECISION_GUIDE.md` describes selection criteria and comparative strategy, not a compulsory agenda or theorem authority.
- When changing any of these, check the others for stale 'active/current/leading' language. Retain the mathematical content of informative negative results and concrete unresolved approaches, without preserving chronological priorities or administrative history.
- Never infer proof authority from recency, prominence, or inclusion in the frontier. Do not promote provisional findings during a navigation-only change.

- `research/MAP.md` is a conceptual topic and interface map, not a formal dependency graph or new source of theorem authority. Maintain links to canonical records as new results are promoted; prefer mathematical consolidation to chronological accumulation.

## Standing integration and geometric-proof policy

Integrate only specified, committed mathematical contributions, preserving their exact hypotheses, proof status, counterexamples, and dependencies. Coordinate changes to INDEX, MAP, STATE, FRONTIER, AUTHORITY, and the decision guide when their navigation or status is affected. Do not establish a standing integration branch, intake registry, or compulsory worktree workflow. Independent review is required for consequential new arguments and changes of theorem scope; editorial changes do not promote provisional mathematics.

**Prefer intrinsic and geometric proofs over calculations whenever possible.** Seek arguments through the embedded geometry, normal and conormal structures, intersection theory, finite modifications, deformation theory, or moduli interpretation before presenting a coordinate computation as the proof. A conceptual introduction to a calculation is not a replacement proof. When computation remains necessary, state the invariant geometric assertion it establishes, explain why the computation covers the claimed scope, and retain the smallest independently checkable certificate. Do not weaken a rigorous result to force a geometric narrative.

**Use torus symmetry systematically, but preserve the full object.** For each relevant research lane, ask what the full flat T-limit of an actual intersection, embedded scheme, or carrier retains; distinguish this from initial forms of two equations and from the normal-cone initial ideal. Record the invariant Hilbert polynomial, support, embedded/endpoint structure, and possible new generators. Identify whether the lane's claim covers arbitrary pairs, invariant pairs, constant transverse quotient families, or a specified degeneration. A fixed-point classification cannot exclude general supported complete intersections without a justified supported-deformation or coverage theorem.

For each substantive revision, distinguish (i) an intrinsic proof replacing a calculation, (ii) a geometric reduction with a necessary calculation, and (iii) a computational result awaiting conceptual explanation. Audit the theorem's characteristic and degree hypotheses, and do not promote a new implication solely because a geometric interpretation is available.


**Strongly consider invariant-limit stratification.** For a fixed degree pair and bounded supported Hilbert locus, consider organizing ideals by their full T-invariant flat limit (attracting strata, with any required refinements). Where useful, on each attracting locus ask where the *moving ideal* has two homogeneous generators of the prescribed degrees. Do not require its fixed limit to be two-generated, and do not make tangent-space smoothing of selected fixed points the default research question. Examine graded minimal-generator modules, multiplication maps, and actual equation incidence; verify scheme-theoretic generation, not just two independent sections. State the boundedness, coverage and characteristic qualifications of any resulting stratification. This is a preferred lens, not a prerequisite for independent geometric arguments.
