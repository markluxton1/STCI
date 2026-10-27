# STCI agent retrieval protocol

Read [research/INDEX.md](research/INDEX.md) first. This file governs **how to retrieve and assess** research; it does not establish new mathematical conclusions.

1. Identify the exact curve, characteristic, carrier hypotheses, and question before retrieving claims. When exploring intersections, consider the broader formulation \(C\subset V(F,G)_{\\mathrm{red}}\) and possible residual components rather than assuming STCI at the outset; do not mistake vertical exceptional degeneration for an additional component downstairs.
2. Use the short navigation index to find the smallest relevant topic/result/question. Read only the relevant files and their stated dependencies. Do not ingest the entire research record by default.
3. Check the **exact hypotheses, quantifiers, epistemic status, limitations, and evidence** of every claim before relying on it. Distinguish a necessary condition, a fixed-carrier theorem, a completed exclusion, and an unrestricted STCI theorem.
4. If an indexed result is absent or not yet promoted, follow its evidence links and explicitly report the authority gap. Never manufacture a canonical result file or treat an acceptance note as a promoted result.
5. On conflicting statements, do not resolve by timestamp or branch name alone. Record both scopes and evidence, consult [authority rules](research/AUTHORITY.md), and flag unresolved conflicts.
6. Treat `research/STATE.md` and `research/FRONTIER.md` as current navigation summaries, not independent theorem authority. For mathematical claims consult promoted result records and their evidence; flag any unreconciled legacy passages.
7. Preserve existing proof, audit, certificate, and historical paths. Do not edit accepted mathematics, re-run inherited proofs, or silently reopen closed cases merely to reorganize files.
8. New results enter as proposals with evidence and independent review status; promote them only through a reviewed change to canonical result/question records.

For substantial work, report: precise claim used, assumptions, supporting path(s), unresolved dependencies, and whether the claim is promoted or provisional. Do not equate a computational reduction with a completed computation.
New research contributions should follow [the proposal and audit checklist](research/CONTRIBUTING_AGENT.md). Canonical metadata can be checked with `python3 research/computations/validate_records.py`.

## Navigation maintenance contract

- `research/STATE.md` summarizes established knowledge and open mathematical status; only change mathematical status when supported by canonical evidence and the applicable review process.
- `research/FRONTIER.md` describes current investigations, alternative open interfaces, and next tests; update it when research direction changes, without rewriting historical evidence.
- `research/RESEARCH_DECISION_GUIDE.md` describes selection criteria and comparative strategy, not a compulsory agenda or theorem authority.
- When changing any of these, check the others for stale 'active/current/leading' language. Keep dated priorities explicitly historical and retain paths to negative results and discontinued approaches.
- Never infer proof authority from recency, prominence, or inclusion in the frontier. Do not promote provisional findings during a navigation-only change.
