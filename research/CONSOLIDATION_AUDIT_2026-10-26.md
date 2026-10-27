# Consolidation audit — 2026-10-26

Status: **review intake; no mathematical promotion**.

## Git ancestry and scope

Integration branch starts at `codex/ci-cycle-valuations-2026-10-25`, which was four commits ahead of `codex/quartic-flag-duality-2026-10-24` at comparison. Thus the latter is an ancestor of the former; no second wholesale merge is needed. Main's earlier PR #75 work is incorporated in the ancestry. This preserves the complete recent branch history and avoids duplicate imports.

## Rules

Follow [AUTHORITY.md](AUTHORITY.md), [AGENTS.md](../AGENTS.md), and [RESULT_SCHEMA.md](RESULT_SCHEMA.md). No theorem follows from a PASS label alone. Do not promote any claim without its exact hypotheses, independent proof review, and reproducible certificate where applicable.

## Immediate review packets

1. October 25–26 CI-cycle valuations: distinguish local valuation multiplicity formulas, global fixed-carrier bounds, and unconditional STCI claims.
2. Fixed sextic degree-sixteen mate: audit the kernel identity, exact computer certificates, nonsplit-node hypothesis, and the inference `m_C <= 22`; retain **fixed-carrier only**.
3. Fixed-boundary deformation: distinguish first-order rank calculations, formal smoothing, and global algebraic families.
4. Smooth degree-twelve residual: check ideal identity, smoothness, genus, transversality, and characteristic; record as an **example**, not universal endpoint behavior.
5. Quartic flag/duality and ruled surfaces: independently check scheme structures, singular/embedded contributions, and precise scope; keep exploratory geometry separate from STCI obstruction claims.
6. Older unpromoted notes and reconciliation files: systematically inventory against canonical results index, checking duplicates, supersessions, missing proof links, and unresolved contradictory claims.

## Completion criteria

Every provisional claim has an owner/source path, exact statement, status, dependencies, evidence, and disposition. Canonical records and indexes change only through subsequent reviewed promotion. No unrestricted characteristic-zero STCI conclusion is asserted by this intake.
