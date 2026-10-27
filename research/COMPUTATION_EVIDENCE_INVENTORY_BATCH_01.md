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
