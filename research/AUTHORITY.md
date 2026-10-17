# Canonical research authority policy

This policy defines the intended **post-migration** authority model. It does not retroactively certify or change any mathematical statement.

## Levels

1. **Canonical result records:** one addressable statement per accepted result, with explicit quantifiers, hypotheses, evidence, limitations, dependencies, and review status. Records live under `research/results/` after promotion.
2. **Canonical question records:** open questions and precise missing implications, linked to applicable results. They live under `research/questions/` when introduced.
3. **Navigation:** `research/INDEX.md`, `research/STATE.md`, `research/FRONTIER.md`, and topic indexes route readers; summaries are not independent proofs or competing sources of mathematical authority.
4. **Evidence:** immutable or historically preserved proof notes, independent audits, computations, literature records, and acceptance records establish provenance and support review. An accepted note is not automatically a promoted canonical result.
5. **Provisional work:** active branches, scratch notes, and ChatGPT submissions are not canonical by default.

**Transition:** `STATE.md` and `FRONTIER.md` are navigation summaries, not independent theorem authority. Some legacy passages remain unreconciled with promoted records. Use the canonical record and its evidence for exact claims; when a genuine conflict remains, state the uncertainty and cite both sources.

## Promotion and supersession

- Promote **claims**, not entire branches or documents. Check scope against the exact source proof and independent audit; preserve the characteristic, curve, degrees, normality, Cartier, genericity, and other hypotheses.
- Give each result a stable ID. Prefer one statement per record, or separate independently usable lemmas into distinct records. Keep legacy IDs as aliases rather than silently renumbering them.
- Require a recorded review decision, explicit evidence paths, dependencies, and limitations. A newer timestamp, broader title, or stronger-looking summary does not establish a stronger theorem.
- Supersede an older claim only when a documented implication or correction justifies it. Preserve its historical path and record `supersedes` / `superseded_by` references. Do not overwrite proofs to erase earlier errors.
- Where two records conflict without a verified scope bridge, mark the dispute and do not use either stronger formulation as an unconditional premise.
- Never promote a conditional result to an unconditional one; never promote a necessary condition or decision procedure into existence/nonexistence of a mate without its remaining computation.
- Keep the unrestricted characteristic-zero STCI question open unless a separately reviewed proof actually resolves it.

## Agent-friendly indexing

Indexes should contain IDs, concise scopes, statuses, and relative links, not copied proofs. Result metadata should be machine-parseable using the schema in [RESULT_SCHEMA.md](RESULT_SCHEMA.md). Indexes may eventually be generated from that metadata; generation is not implemented in this PR.

## Review checklist

A promotion PR must state the old and new claims verbatim or by precise references, show the scope bridge, list evidence and audit paths, identify affected frontier questions and supersession links, and verify local links. No wholesale merging of diverged research branches.
