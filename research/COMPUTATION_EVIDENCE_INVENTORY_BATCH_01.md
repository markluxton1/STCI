# Computation evidence inventory: batch 1

Inspected four source scripts, one validation README and one recorded output log. This was source inspection, not execution.

| Artifact | Role | Preliminary disposition |
|---|---|---|
| computations/verify_intrinsic_quadruple_local_algebra_2026_10_23.py | Exact representative local identities and exceptional-rank arithmetic; not arbitrary-coefficient proof | Keep checker |
| computations/audit_mf6_e1_primitive_2026_10_07.py | Independent SymPy 35-column ambient quartic checks, orbit, infinity and normalization tests; writes JSON | Keep checker; inspect sidecar |
| computations/verify_44_quartic_symbol_comparison_2026_10_23.py | Standard-library rational and mod-two quartic symbol ranks, q-squared kernel | Keep checker |
| computations/verify_z4_local_structure_2026_10_20.m2 | Exact Macaulay2 kernel, saturation, local charts, transition and integral expansions | Keep checker |
| validation/44-conormal-2026-10-23/README.md | Maps four executed scripts to logs, dependencies and runtime; limits PASS claims | Preserve evidence mapping |
| validation/z4-lift-2026-10-20/local-structure.log | Recorded M2 checks and Hilbert polynomials for Z1 through Z4 | Keep pending reproducibility check |

The logs were not regenerated in this pass. Script assertions support finite computations but do not replace global geometric proofs. No sampled artifact is presently established to be redundant.

Next: inspect JSON sidecars, contact logs, and large witness generation and references. No deletion or promotion.


## Repository-wide evidence structure (theme 7 continuation)

A recursive Git tree enumeration on the consolidation branch identified **629 files** under research/computations (207 .py, 209 .m2, 109 .json, 59 .txt, 20 .out, 19 .log, 5 .c, 1 .md) and **2,253 files** under research/validation, across **120 immediate validation subdirectories** (17 README.md). This is a structural inventory, not 2,882 individually inspected proofs or an execution rerun. The figures are counts for the enumerated tree, and may change as the branch changes.

The results/INDEX.md gives **36 promoted scoped results** and six legacy topic syntheses. The computation README already has a substantial script-to-claim map, with explicit limits on what PASS means, and validation directories preserve independent audit/execution context. We should **reuse and reconcile** these maps rather than create one duplicate row per generated artifact.

### Evidence retention rules

1. For each of the 36 promoted records, retain a **claim -> proof -> exact witness (if needed) -> independent audit -> runtime/reproduction instructions** path. A theorem supported by conceptual proof does not need every exploratory scratch run; an exact computational certificate must not be retired merely because a prose result exists.
2. Keep small explicit **counterexamples** even if they invalidate abandoned conjectures: they explain which hypothesis is missing.
3. For unpromoted but interesting intrinsic geometry and conditional research, keep at least one readable mathematical derivation and the minimal essential exact checks, clearly marked as unpromoted.
4. Keep large generated data only where it is a nontrivial certificate or where regeneration cannot presently be assured. Distinguish source generators, exact output, audit hashes, interrupted attempts, and exploratory probes.
5. **Do not delete from filename or byte-count similarity alone.** Prior large-witness inventory identifies two gzip archives with reported equal uncompressed hashes; independent verification and reference tracing are still required.
6. Treat PASS logs as evidence of a specific historical run, not proof that the script was rerun in this review or that a global mathematical conclusion follows.

### Gaps before retirement

The 36-by-evidence claim matrix is **not yet constructed**. This pass checks the tree, README, canonical index, and prior sample inventory, not the completeness of every proof dependency. Next review should prioritize missing evidence links in canonical front matter, unsupported large witness files, and the distinction between required exact certificates and exploratory outputs. Theme 8 must also reconcile false historical claims and conditional branches before any removal.

No deletions or theorem promotions are authorized by this inventory.
