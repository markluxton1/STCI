# Independent ideal-filtrations investigation: validation

Date: 2026-10-23.

Report: [independent investigation](../../notes/2026-10-23-ideal-filtrations-independent-investigation.md).

Review: [independent review record](../../notes/2026-10-23-ideal-filtrations-independent-review.md).

All new computations use the Python standard library and exact arithmetic. Run from the repository root:

~~~sh
python3 -B research/computations/verify_ideal_filtration_counterexamples_2026_10_23.py
python3 -B research/computations/verify_ideal_filtration_completeness_2026_10_23.py
python3 -B research/computations/verify_ideal_filtration_quartic_lifting_2026_10_23.py
python3 -B research/computations/validate_records.py
git diff --check
~~~

| Output | What it establishes |
|---|---|
| [counterexamples.log](counterexamples.log) | Exact cancellation/localization identities, associative dimension-five algebra, I-adic dimensions and higher-generator defect example |
| [completeness.log](completeness.log) | Exact unit identities, associative dimension-eight algebras, equal Hilbert functions, distinct square-zero invariants |
| [quartic-lifting.log](quartic-lifting.log) | Twenty-seven exact chart, overlap, conormal, lift, and gluing identity checks |
| [canonical-records.log](canonical-records.log) | Canonical metadata validation only |

All commands completed with exit code zero. Local links in the report, review, and this directory were checked. No inherited mathematical exclusion scripts were rerun.

These are finite arithmetic certificates supporting the accompanying proofs. They do not establish irreducibility, the general quotient identities, the full sheaf diagrams, the formal reconstruction statements, or any global STCI conclusion without the report's separate arguments. The smooth-carrier support proposition has a first-principles proof and two independent mathematical reviews; no finite replay is substituted for that proof.
