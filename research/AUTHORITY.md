# Canonical research authority policy

**Consolidated hierarchy:** [Canonical results](results/INDEX.md) and their evidence govern theorem scope; [synthesis chapters](synthesis/README.md) provide exposition; [dependency navigation](synthesis/DEPENDENCIES.md) identifies proved arrows and missing bridges; [state](STATE.md), [frontier](FRONTIER.md), and [topic map](MAP.md) guide readers but do not promote claims. A chapter must not broaden the hypotheses of a result record.

This policy defines the current consolidated authority model. It does not retroactively certify or change any mathematical statement.

## Levels

1. **Canonical result records:** one addressable statement per accepted result, with explicit quantifiers, hypotheses, evidence, limitations, dependencies, and review status. Records live under `research/results/` after promotion.
2. **Canonical question records:** open questions and precise missing implications, linked to applicable results. They live under `research/questions/` when introduced.
3. **Navigation:** `research/INDEX.md`, `research/STATE.md`, `research/FRONTIER.md`, and topic indexes route readers; summaries are not independent proofs or competing sources of mathematical authority.
4. **Evidence:** current proofs, essential exact computations, checked literature applications, and concise independent review decisions support mathematical claims. Historical wrappers and original paths are not independently required. An accepted note is not automatically a promoted canonical result.
5. **Provisional work:** active branches, scratch notes, and ChatGPT submissions are not canonical by default.

**Transition:** `STATE.md` and `FRONTIER.md` are navigation summaries, not independent theorem authority. Some legacy passages remain unreconciled with promoted records. Use the canonical record and its evidence for exact claims; when a genuine conflict remains, state the uncertainty and cite both sources.

## Promotion and supersession

- Promote **claims**, not entire branches or documents. Check scope against the exact source proof and independent audit; preserve the characteristic, curve, degrees, normality, Cartier, genericity, and other hypotheses.
- Give each result a stable ID. Prefer one statement per record, or separate independently usable lemmas into distinct records. Keep legacy IDs as aliases rather than silently renumbering them.
- Require a recorded review decision, explicit evidence paths, dependencies, and limitations. A newer timestamp, broader title, or stronger-looking summary does not establish a stronger theorem.
- Supersede an older claim only when a documented implication or correction justifies it. Retain any mathematically useful counterexample or limitation and record a precise corrected statement. Consolidated proofs may replace obsolete versions after review; Git retains development history.
- Where two records conflict without a verified scope bridge, mark the dispute and do not use either stronger formulation as an unconditional premise.
- Never promote a conditional result to an unconditional one; never promote a necessary condition or decision procedure into existence/nonexistence of a mate without its remaining computation.
- Keep the unrestricted characteristic-zero STCI question open unless a separately reviewed proof actually resolves it.

## Agent-friendly indexing

Indexes should contain IDs, concise scopes, statuses, and relative links, not copied proofs. Result metadata should be machine-parseable using the schema in [RESULT_SCHEMA.md](RESULT_SCHEMA.md). Indexes may eventually be generated from that metadata; generation is not implemented in this PR.

## Review checklist

A promotion PR must state the old and new claims verbatim or by precise references, show the scope bridge, list evidence and audit paths, identify affected frontier questions and supersession links, and verify local links. No wholesale merging of diverged research branches.

## Mathematical retention and review

A source earns retention through useful mathematical content not adequately
represented elsewhere. This includes conditional statements, alternative proofs,
constructions, counterexamples, intermediate lemmas, precise unresolved questions,
and exact computational support. Promotion status is not a retention test.

Review replacements together with proposed removals. Preserve the actual
hypotheses, quantifiers, characteristic, embedding, and distinction between formal,
local, graded, and global objects. A recorded rank or successful run alone does
not establish a theorem. Supply the mathematical meaning and necessary exact
support of a computation before removing its certificate.

Remove redundant exposition, execution logs, repeated verification records,
chronological handoffs, migration inventories, and obsolete formulations after
unique mathematics and necessary support have surviving reviewed homes. Original
evidence paths may be updated to those homes. Independent review can be recorded
concisely with the claim it covers; a separate audit hierarchy is not required.

These rules govern consolidation as well as new work. They do not authorize
stronger claims, removal of essential evidence, or relabeling provisional work as
proved. The unrestricted characteristic-zero existence question remains open.
