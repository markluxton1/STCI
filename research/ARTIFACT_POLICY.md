# Research artifact and large-file policy

The repository preserves reproducible mathematics and computations. The policy separates **source and evidence** from **reproducible bulk output**.

## Track in ordinary Git

- Human-authored proofs, notes, independent audits, and provenance manifests.
- Reproducible scripts (`.py`, `.m2`, etc.), input data needed to rerun them, and small exact certificates.
- Selected compact outputs required to verify a stated result, with their generating command and scope.

## Do not commit bulk output by default

- Large regenerated witness dumps, temporary caches, scratch exports, and tool logs.
- Artifacts over 50 MB without explicit review. GitHub rejects ordinary blobs over 100 MB.
- Files whose content cannot be independently regenerated or whose provenance is unknown should **not** be silently discarded; record their source and retention plan.

For an essential large artifact, use Git LFS **only after** confirming repository access, quotas, clone requirements, and long-term availability. Alternatives are a regeneration script plus a SHA-256 checksum and a separately archived output. LFS tracking alone does not rewrite existing commits or solve a rejected push containing an oversized ordinary Git blob.

## Handling the known support32 witness incident

A previous push was rejected for `research/validation/2026-10-13-generalization-quintic-h3/support32-witness.txt` (102.67 MB). Before another push, inspect **local history**, not just the working tree. Decide whether to keep it outside Git with a manifest/checksum, use LFS, or regenerate it. If the large blob is in an unpushed commit, remove it from that branch's history using a reviewed history-rewrite procedure; adding `.gitignore` after the fact is insufficient.

## Intake checklist

For each imported computation or certificate, record: source branch and commit, script/input paths, expected outputs, run instructions, checksum if externalized, and whether verification was rerun. Preserve source evidence and never claim a verification merely because the file was copied.
