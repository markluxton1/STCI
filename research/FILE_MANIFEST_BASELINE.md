# Current-tree file inventory — manifest baseline

Source: user-provided `git ls-tree -r -l HEAD` manifest, 27 October 2026. These counts describe the local commit where the manifest was generated; branch-tip identity has not been independently verified. **This is a path-and-blob census, not a mathematical-content audit.**

## Totals

- 3,840 tracked files; 223,868,590 bytes (223.9 MB, decimal).
- 2,954 distinct Git blob hashes.
- 483 duplicate-blob clusters, representing 886 extra identical-file paths and 14,027,806 bytes beyond one copy per distinct blob.
- 3,822 tracked files live under `research/`.

## Principal file families

| Directory | Files | Bytes | Share |
|---|---:|---:|---:|
| `research/validation/` | 2,253 | 176,398,454 | 78.8% |
| `research/computations/` | 629 | 36,137,079 | 16.1% |
| `research/notes/` | 545 | 5,872,919 | 2.6% |
| `research/archive/` | 146 | 2,217,451 | 1.0% |
| `research/scratch/` | 112 | 1,762,730 | 0.8% |
| `research/results/` | 44 | 137,978 | 0.1% |
| `research/synthesis/` | 15 | 89,754 | <0.1% |

The 44 result-directory files should not be equated with 44 canonical results; existing navigation identifies 36 canonical result records. The current file tree has more notes and computations than the older historical indexes.

## Largest tracked files

- 50,074,842 bytes: `research/validation/2026-10-13-generalization-quintic-h3/support32-subset-witness.txt.gz`
- 50,074,835 bytes: `research/validation/2026-10-13-generalization-quintic-h3/support32-witness.txt.gz`
- 22,978,614 bytes: `research/computations/conditional_2_12_cubic_reduction_2026_10_21_family_lifts.m2`
- 22,448,188 bytes: `research/validation/2026-10-13-generalization-quintic-h3/multiplicity4-witness.txt`

## Inventory classification protocol

For each tracked path, record its blob SHA, size, source family, mathematical contribution (if any), linked claims, dependency or reproducibility role, epistemic status, and proposed disposition. Distinguish filename-based preliminary role from **content-read** and **independently validated** classifications. Preserve meaningful failure mechanisms and independent alternative proofs, not chronology for its own sake.

No file is deletable merely because it is old, duplicated, generated, or large. Validate the actual mathematical or reproducibility need before recommending removal.

## Review order

1. Read the canonical results and supporting proof sources; map claims to files.
2. Review thematic, provisional and exploratory notes for unique mathematics and failed approaches.
3. Inspect the large validation witnesses and exact-duplicate clusters for reproducibility requirements.
4. Consolidate only after the mathematical contribution and dependencies of each candidate source are understood.

Companion machine-readable register generated from the supplied manifest: `STCI_file_register.csv` (3,840 rows; currently retained as a chat attachment rather than committed to the repository). No mathematical claims have been promoted and no files have been deleted.
