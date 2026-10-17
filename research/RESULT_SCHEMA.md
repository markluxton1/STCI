# Result and question record specification (v1 proposal)

This specification applies to **future promoted records**. Existing topic syntheses and proof notes are not required to conform until individually migrated. No records are promoted by this specification.

## Result format

One Markdown file per independently retrievable claim, with YAML front matter:

```yaml
---
id: STCI-R-0001
title: Short descriptive theorem name
kind: theorem                  # theorem | lemma | reduction | certificate
status: proved                # proved | exact_reduction | conditional | needs_audit | disputed | superseded
scope:
  characteristic: "0"
  curve: "fixed C0 only"
  hypotheses:
    - "List all additional assumptions explicitly"
statement: "Exact statement, or a precise pointer to the statement below"
dependencies: []              # stable result IDs; empty if none
evidence:
  - "research/notes/path-to-proof.md"
independent_audits: []
accepted_in: null              # evidence path, if formally accepted
legacy_ids: []                 # e.g. P-044; never silently reuse
supersedes: []
superseded_by: []
limitations:
  - "What this does not establish"
---
```

The body should contain **Statement**, **Hypotheses and quantifiers**, **Proof outline**, **Dependencies**, **Evidence and verification**, **Consequences**, and **Limitations**. Paths in metadata are repository-root-relative when the evidence exists on the canonical branch. Evidence preserved only on another branch may instead use a full GitHub source URL, ideally a commit-pinned permalink; the record must disclose that location and any remaining source-migration work. Stable IDs must be unique; filenames may change while IDs persist. A `needs_audit` or `disputed` record must never be indexed as an accepted theorem.

## Question format

Question records use `STCI-Q-####` IDs, `status: open | conditional | resolved | superseded`, an exact question, links to applicable result IDs, missing implications, and supporting evidence. Distinguish an unresolved calculation within a proved decision procedure from an unresolved theorem.

## Validation contract (not yet automated)

Before promotion, verify: unique IDs; valid statuses and kinds; every dependency ID exists; every referenced path exists; no supersession cycles; every `proved` claim has evidence and recorded acceptance/review; no contradiction between a question's resolved status and its linked results. An index entry must link to a real file. A sample record is illustrative, **not** a project claim.
