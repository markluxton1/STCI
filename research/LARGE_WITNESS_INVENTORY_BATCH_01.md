# Large generated-witness review — batch 1

**Branch:** restructure/mathematical-consolidation. **Evidence:** file-size register plus GitHub reads of archive, execution and lineage manifests. The compressed archives were **not downloaded, decompressed or independently hashed** in this pass.

## First high-confidence candidate

- `validation/2026-10-13-generalization-quintic-h3/support32-witness.txt.gz`: 50,074,835 bytes.
- `validation/2026-10-13-generalization-quintic-h3/support32-subset-witness.txt.gz`: 50,074,842 bytes.
- Their `support32-archive-manifest.json` reports distinct compressed SHA-256 hashes, but the **same** uncompressed SHA-256 `65feb2e88ea19fd28d67512628a28915d05d1c7a44bd657fe7e99ada2910905b` and identical 107,657,203-byte uncompressed lengths.
- **Candidate saving:** 50,074,842 bytes if the subset archive is removed, or 50,074,835 bytes if the other is removed. **Not yet approved:** independently decompress/hash, inspect all references, verify either archive can serve both mathematical witness roles and update references before deletion.

## Evidence chain

- `source-input-lineage-manifest.json` distinguishes completed checks from interrupted attempts and explicitly declines to invent missing historical exit codes.
- `support32-witness-attempt-01/execution-record.json` records an exit-zero Macaulay2 run, source hash and stdout/stderr hashes. This documents historical execution, not a fresh mathematical verification.
- `validation/2026-10-14-localcoh-degree15-attempt06/polynomial-inverse-archive.json` records an 8,068,969-byte compressed archive for a 19,189,736-byte raw inverse and a round-trip hash. No duplicate of this archive was established.
- `validation/2026-10-14-localcoh-degree15-attempt06/acceptance-evidence.json` binds the local-cohomology claim to a named certificate, proof note and arithmetic source. Its scope is the stated family, not universal STCI.

## Next checks

1. Independently compare the two support32 archives after decompression, including the reported hash.
2. Search path references and generator scripts; identify which archive is canonical and whether a single artifact can satisfy both consumers.
3. Investigate the 22.98 MB `computations/conditional_2_12_cubic_reduction_2026_10_21_family_lifts.m2`: source script, generated source, or embedded output?
4. Investigate the 22.45 MB `multiplicity4-witness.txt`: regenerate/check rather than assume redundant.
5. Classify interrupted-attempt snapshots separately from accepted evidence. Failed methods may warrant a short explanation even when their full logs are unnecessary.

**No deletion, source rewrite or mathematical promotion performed.** Removing tracked files from the branch would reduce its current tree, but does not itself erase historical Git objects.
