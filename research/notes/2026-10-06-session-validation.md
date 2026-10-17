# Session exact validation and reproducibility record

Started 2026-10-06; continued and completed 2026-10-07.
Status: **EXACT LIVE VALIDATION / REPRODUCIBILITY**, with two documented verifier repairs.
The dated filename is retained across the continuation. This note does not by itself prove any global STCI claim.

## Counts and environment

There are **55 distinct source checks with a successful latest execution**. The initial executions gave 53 passes and 2 failures. Both failures were investigated before changing their sources; the two repaired-source reruns passed. Three additional compatibility-copy diagnostic runs are retained separately: one pass and two failures. The MF6 owner subsequently completed the universal verifier with self-contained incidence reconstruction, explicit minor-membership witnesses, and the full exceptional fiber. That changed source was rerun once and passed; its earlier successful output is retained. Thus there were 61 complete top-level verifier/exporter executions: 55 initial distinct-source checks, 2 repaired-source reruns, 3 diagnostic copies, and 1 meaningful source-completion rerun. Prefix evaluations used to diagnose failures and imported subsidiary modules are not inflated into additional source-check counts.

The 41-source baseline suite consists of 38 Python files named in the computation README, the historical mixed-(4,5) Python verifier, and two Macaulay2 verifiers. Its initial result was 40 passes and 1 failure; the repaired boundary verifier makes its latest result 41 passes. The remaining fourteen distinct checks are one tensor exporter, two incidence verifiers, two supplementary retained checks, five fresh MF6/dx1 checks, three new normal-carrier arithmetic checks, and one source-reconstructed dx1 saturation audit.

The baseline was run on branch `research/ultra-resume-2026-10-06`, starting from HEAD `4103561f3e271e03d8069e7f09def3889b4eb4da`. The continuation started from the clean retained snapshot at HEAD `3ffda7548a863387429adab61eefe02575e86297`. These are observation points, not asserted final commit IDs. No branch was switched or reset by this validation lane.

- Python: `/private/tmp/stci-cas-venv/bin/python`, version 3.14.8.
- SymPy: 1.14.0.
- Macaulay2: `/opt/homebrew/bin/M2`, version 1.26.06.
- Python executions used `PYTHONDONTWRITEBYTECODE=1`.
- The baseline passed checks were not rerun merely because the user resumed on the following day.

Exact commands, elapsed times, exit statuses, source hashes, and logs are stored in [`validation-index.json`](../validation/2026-10-06-session/validation-index.json). Environment observation files are [`environment.json`](../validation/2026-10-06-session/environment.json) and [`environment-2026-10-07.json`](../validation/2026-10-06-session/environment-2026-10-07.json). The replay drivers are [`run_suite.py`](../validation/2026-10-06-session/run_suite.py) and [`run_fresh_2026_10_07.py`](../validation/2026-10-06-session/run_fresh_2026_10_07.py). They expect the recorded runtime paths, so a successor must adjust those paths if the temporary Python environment disappears.

## Baseline per-source results

| Source | Initial result | Latest result | Exact run log |
|---|---|---|---|
| `computations/verify_all_quartic_primitive_obstruction.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_all_quartic_primitive_obstruction.log) |
| `computations/verify_c0.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_c0.log) |
| `computations/verify_chow_form.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_chow_form.log) |
| `computations/verify_chow_pencil_45.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_chow_pencil_45.log) |
| `computations/verify_degree6.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_degree6.log) |
| `computations/verify_dx1_a_half_boundary.py` | FAILED | PASS | [log](../validation/2026-10-06-session/verify_dx1_a_half_boundary_repaired.log) |
| `computations/verify_dx1_p044_residual.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_dx1_p044_residual.log) |
| `computations/verify_general_conductor_power.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_general_conductor_power.log) |
| `computations/verify_localcoh_constant_direction_apolar.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_constant_direction_apolar.log) |
| `computations/verify_localcoh_degree4_allstage_certificate.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_degree4_allstage_certificate.log) |
| `computations/verify_localcoh_degree4_counterexample.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_degree4_counterexample.log) |
| `computations/verify_localcoh_direction_image.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_direction_image.log) |
| `computations/verify_localcoh_finite_principal_parts.m2` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_finite_principal_parts.log) |
| `computations/verify_localcoh_generic_length_model.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_generic_length_model.log) |
| `computations/verify_localcoh_pure_direction_audit.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_pure_direction_audit.log) |
| `computations/verify_localcoh_quartic_ratio_t_slice.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_quartic_ratio_t_slice.log) |
| `computations/verify_mf6_defect12.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mf6_defect12.log) |
| `computations/verify_mf6_type3.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mf6_type3.log) |
| `computations/verify_mixed46_regular.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mixed46_regular.log) |
| `computations/verify_normal_bundle.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_normal_bundle.log) |
| `computations/verify_normal_quartic_simple_elliptic.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_normal_quartic_simple_elliptic.log) |
| `computations/verify_normal_rational_carrier_compression.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_normal_rational_carrier_compression.log) |
| `computations/verify_p044_survivor_cubic.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_p044_survivor_cubic.log) |
| `computations/verify_positive_quartic_descent.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_positive_quartic_descent.log) |
| `computations/verify_primitive_obstruction.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_primitive_obstruction.log) |
| `computations/verify_primitive_quadruple_universal.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_primitive_quadruple_universal.log) |
| `computations/verify_primitive_quartic_factor_audit.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_primitive_quartic_factor_audit.log) |
| `computations/verify_primitive_triple_parity.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_primitive_triple_parity.log) |
| `computations/verify_quadric_powers.m2` | PASS | PASS | [log](../validation/2026-10-06-session/verify_quadric_powers.log) |
| `computations/verify_residual_cycle.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_residual_cycle.log) |
| `computations/verify_split22_boundary_lift.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split22_boundary_lift.log) |
| `computations/verify_split22_boundary_survivor.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split22_boundary_survivor.log) |
| `computations/verify_split22_chart_audit.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split22_chart_audit.log) |
| `computations/verify_split22_finite_reduction.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split22_finite_reduction.log) |
| `computations/verify_split4_nonramified.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split4_nonramified.log) |
| `computations/verify_typea45.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typea45.log) |
| `computations/verify_typeb45_boundary.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typeb45_boundary.log) |
| `computations/verify_typeb45_corner.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typeb45_corner.log) |
| `computations/verify_typeb45_dense.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typeb45_dense.log) |
| `computations/verify_typeb45_endpoint_certificate.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typeb45_endpoint_certificate.log) |
| `scratch/degree6/verify_mixed45_reduction.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mixed45_reduction.log) |

The three primitive generator-driving checks ran sequentially in the retained `validation/2026-10-06-session/isolated` snapshot. Their generators rewrite formula JSON and Macaulay2 sources, so the snapshot preserves all generated data while leaving the existing research formulas unchanged. The universal primitive verifier invokes both its exact M2 membership companions with checked subprocess exits. The source and generated-output hashes are in [`isolated-source-output-hashes.json`](../validation/2026-10-06-session/isolated-source-output-hashes.json).

Known faulty historical `localcoh-symbol-paritycheck.m2` and `localcoh-symbol-seedcheck.m2` were not executed or used as proof inputs. The older resultants-only dx1 diagnostic is retained as a diagnostic; its passing gcd assertion does not certify residual emptiness.

## Missing local-cohomology coordinates restored

The unchanged retained exporter `computations/localcoh-incidence-tensor.m2` regenerated its two absent files. Its exact assertions checked 30 ancestors, 18 actual quartic forms of degree four, target dimension 74, and preservation of the combined product/target row space. The source SHA-256 was

    c81ff40cd8a83cdbe527401b038d75a9748f2b2b10c09214fb0520e3ecb69377

The output hashes were:

| Coordinate file | SHA-256 |
|---|---|
| `localcoh-incidence-tensor.txt` | `05702619ef67a6fed4420e24a5530eccb18e4700d8e1f1ba5cae89b7899cc60b` |
| `localcoh-incidence-bases.txt` | `ee3e320f240b77c370ad21704c97aeec12b619f55c6ad8aff829aef9235d8dcc` |
| `localcoh-symbol-numerators.txt` | `4989e3ed86a06221b828b1ede99085325fb9740ad02dd1c542e547c8f5809406` |

The tensor and basis hashes agree **exactly** with both previously retained JSON certificates. The retained `localcoh-symbol-top.json` hash also agrees with both certificates. The formerly absent symbol-numerators file was extracted as the 30 ancestor lines `bases[1:31]`, in the same order and with a trailing newline. Its equality with those lines is checked by both incidence verifiers. No coordinate convention or stored certificate was edited.

| Source | Initial result | Latest result | Exact run log |
|---|---|---|---|
| `computations/localcoh-incidence-2026-10-06.py` | PASS | PASS | [log](../validation/2026-10-06-session/localcoh-incidence-2026-10-06.log) |
| `computations/localcoh-incidence-parity-dual-2026-10-06.py` | PASS | PASS | [log](../validation/2026-10-06-session/localcoh-incidence-parity-dual-2026-10-06.log) |

The fixed-direction certificate proves the exclusion only for normalized direction `(1+t^2,-2t)`, including all lower-order coefficients. The polynomial parity dual proves its stated normalized family exclusion over all characteristic-zero extensions. These exact reruns do not establish emptiness of the full quartic incidence. See [`regenerated-coordinate-hashes.json`](../validation/2026-10-06-session/regenerated-coordinate-hashes.json) and the [exporter log](../validation/2026-10-06-session/localcoh-incidence-tensor.log).

## Boundary verifier failure and chart repair

The initial `verify_dx1_a_half_boundary.py` failed at `G.reduce(u)` because SymPy inferred the integer coefficient domain from the residual polynomials but `u=bx+1/2` has a rational coefficient. An isolated one-line `domain=QQ` compatibility change exposed a second issue: ordinary ideal membership was false in the undivided residual ideal.

After dividing the four displayed numerators by `(b+2)^2`, every residual still contains a factor `x`. The exact QQ Gröbner basis was

    [b*x-8*x^2-4*x, x^3+x^2/2+x/16],

with remainder

    rem(u)=8*x^2+4*x+1/2.

At `x=0` this residual system vanishes while `u=1/2`, so the literal unsaturated membership statement cannot hold. The intended `dx=1` chart requires `x!=0`. Removing the verified common factor `x` on that chart gives

    [b-8*x-4, x^2+x/2+1/16],

and `rem(u)=0`.

The repaired source explicitly states the chart, verifies divisibility by `x`, divides the residuals by `x`, and computes over QQ. Its conclusion is now scoped to `a=-1/2` and `x!=0`. The calculation does not claim ordinary membership in the earlier undivided ideal or make any assertion at `x=0`.

- Original source hash: `871f5f68e0a179a77e0626e904e2841e786ffa189bd093017cf5233ffa122d87`.
- Repaired source hash: `296eeefc0496b390d3b230d08fc8330ef3170ee4a5e1ad19a9a556715f10bf2e`.
- [Original failing log](../validation/2026-10-06-session/verify_dx1_a_half_boundary.log), [QQ-only failing log](../validation/2026-10-06-session/compat_verify_dx1_a_half_boundary_QQ.log), [membership diagnostic](../validation/2026-10-06-session/dx1-boundary-membership-diagnostic.txt), [chart diagnostic](../validation/2026-10-06-session/dx1-boundary-saturation-diagnostic.txt), and [successful repaired log](../validation/2026-10-06-session/verify_dx1_a_half_boundary_repaired.log) preserve the correction rather than hiding the failed premises.

The separately regenerated five-equation Macaulay2 boundary audit agrees with the reduced geometric implication; its exact boundary radicals are recorded in the fresh checks below.

## Supplementary retained checks and polynomiality repair

| Source | Initial result | Latest result | Exact run log |
|---|---|---|---|
| `computations/verify_e2_quartic_incidence.py` | FAILED | PASS | [log](../validation/2026-10-06-session/verify_e2_quartic_incidence_repaired.log) |
| `computations/verify_localcoh_direction_contact_survivor.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_direction_contact_survivor.log) |

The unlisted `verify_e2_quartic_incidence.py` initially failed its assertion that every entry of `J2` has literal denominator one. Exact inspection found only rational constant denominators `4,8,16`, no parameter denominators, and all 18 entries polynomial over QQ. The scoped repair asserts polynomiality over QQ in `x,a,b,d,z` and exact equality after expansion; it does not change the entries or promote the script beyond its own **exact regression / computational cross-check** scope.

An initial diagnostic copy compared `Poly(...).as_expr()` to the unexpanded expression with structural equality and failed. That diagnostic failure concerns expression representation, not a changed polynomial. A second diagnostic copy that permits constant denominators passed. The final repaired source uses explicit QQ construction and expanded equality, and its complete rerun passed.

- Original source hash: `66a725a4fa44038f183319a2c77e3fa64ca42dccf9d9a4d06e5b1f4d1a17dad3`.
- Repaired source hash: `cb210f61e9a154c8a9d1c1a388e75e1a02a3c89b13bfd8157c1bce942c6e8559`.
- [Initial failure](../validation/2026-10-06-session/verify_e2_quartic_incidence.log), [exact denominator diagnostic](../validation/2026-10-06-session/e2-j2-denominator-diagnostic.json), and [successful repaired log](../validation/2026-10-06-session/verify_e2_quartic_incidence_repaired.log).

The contact-survivor script proves only that its explicit coprime ambient pair has second transverse contact but its forced highest inverse coefficient has uncancelled poles, so it has no global quartic ancestor. It does not classify the full contact chart.

## Fresh checks on the 2026-10-07 continuation

| Source | Initial result | Latest result | Exact run log |
|---|---|---|---|
| `computations/session_dx1_boundary_2026_10_06.m2` | PASS | PASS | [log](../validation/2026-10-06-session/session_dx1_boundary_2026_10_06_2026_10_07.log) |
| `computations/session_dx1_compact_certificate_2026_10_06.m2` | PASS | PASS | [log](../validation/2026-10-06-session/session_dx1_compact_certificate_2026_10_06_2026_10_07.log) |
| `computations/verify_mf6_infinity_universal.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mf6_infinity_universal_completed_2026_10_07.log) |
| `computations/verify_session_dx1_independent_2026_10_06.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_session_dx1_independent_2026_10_06_2026_10_07.log) |
| `scratch/session-mf6-special-fiber.py` | PASS | PASS | [log](../validation/2026-10-06-session/session-mf6-special-fiber_2026_10_07.log) |

The universal MF6 infinity script independently derives the nonlinear support/frame transition through cubic order, checks the generic chart as an additional regression, and computes the universal annihilation boundary-minor ideal

    ((A-12)^2,(A-12)(B-4),(B-4)^2).

Its reduction forces `(A,B)=(12,4)` under the recorded annihilation/one-excess-defect hypotheses; the generic kernel is not used to extrapolate the universal boundary rank condition. The completed universal source also reconstructs the full incidence matrix without a generated JSON proof input, checks explicit polynomial combinations witnessing each generator of the boundary-minor ideal, and derives its complete exceptional quartic fiber. Its source SHA-256 is `75bd764fadce1dbd538ac9f23c2039164cbac4e49fd597de7bd46c8e03b42b9e`. The earlier successful source SHA-256 was `3037a2203977e7812ce5d7769667f8a1ab010ba57786ff971e28598f00835bfe`; both run logs remain inspectable. The separate complete special-fiber script cross-checks that its four-dimensional quartic space is exactly `C*H0(O(1))`. This generated JSON was retained in an isolated fresh snapshot; its SHA-256

    059a5188dd40a69ceb921c88fc2830d9a7ffc07eae6678adf6eec72df327fcf3

agrees exactly with the prior repository JSON. The shared MF6 incidence fixture hash is in the special-fiber result record, so the direct fiber check can be rerun with its precise matrix input. The finite matrix calculation and the surrounding geometric argument have distinct roles; this validation note does not replace the proof of the pole/annihilation reduction.

The dx1 compact M2 run computes the common colon exponent and prints `colon equality: true` for the supplied six-generator ideal. The boundary M2 run prints true for the full basepoint-free radical `(2a+1,b+2)` and both boundary radical implications. These boolean outputs were checked explicitly in [`semantic-output-checks.json`](../validation/2026-10-06-session/semantic-output-checks.json), in addition to the process exits.

The independent dx1 Python companion verifies the full polynomial identity `sum(Q_i*C_i)=s^2` by expansion over QQ in a different engine. It also uses exact rational interval arithmetic to certify a real zero of the insufficient three-equation subsystem on its open set, while the two omitted numerators stay nonzero. The displayed decimal intervals summarize exact rational inequalities. The strict inequalities certify the contraction argument; floating point arithmetic is not used for its assertions.

The retained historical resultant-gcd check therefore remains useful evidence for why a full five-equation certificate was necessary. The independent expansion verifies the supplied ideal-membership identity directly rather than treating CAS agreement as an audit.

## Hash integrity and remaining reproducibility limits

The [before hash manifest](../validation/2026-10-06-session/source-hashes-before.json), [after hash manifest](../validation/2026-10-06-session/source-hashes-after.json), [fresh input hashes](../validation/2026-10-06-session/fresh-input-hashes-2026-10-07.json), and individual repair/result JSONs preserve the executed source boundary. The original baseline sources changed only in the explicitly documented boundary and supplementary polynomiality repairs. The neighboring `session_dx1_saturation_2026_10_06.m2` was still being completed by its owning research lane when the first broad manifest was taken; its final source and witness are hashed as fresh independent-check inputs. That neighboring source change is recorded, not silently attributed to the earlier baseline.

The tensor/basis/numerator reproducibility gap is repaired. The MF6 type-4 incidence fixture is present and hashed. Missing general `localcoh-e2-incidence-2026-10-06.py` exporter/chart systems and the historical parity discovery M2 file remain unavailable in this checkout. They were not claimed as live reruns. The retained corrected parity dual is self-contained once the regenerated tensor coordinates and stored top map are present.

No unavailable-runtime or missing-fixture failure remains in the executed set. The temporary Python runtime is a future reproducibility dependency, while the persisted exact formulas, snapshots, hashes, and output logs provide a continuation-ready evidence record independent of its continued availability. Passing a verifier establishes only its recorded finite identities, ranks, memberships, or scoped family calculation; it does not settle the unrestricted STCI question for C0 or for every integral curve.

## Additional stabilized normal-carrier and dx1 audits

Four further sources were copied with their dependencies into `validation/2026-10-06-session/isolated-additional-2026-10-07` and rerun after owner coordination. The previous 51 passing latest checks were not repeated.

| Source | Live result | Exact run log |
|---|---|---|
| `computations/audit_dx1_saturation_2026_10_07.py` | PASS | [log](../validation/2026-10-06-session/audit_dx1_saturation_2026_10_07_validation_2026_10_07.log) |
| `computations/verify_session_normal_carrier_progress.py` | PASS | [log](../validation/2026-10-06-session/verify_session_normal_carrier_progress_validation_2026_10_07.log) |
| `computations/verify_session_normal_independent_audit.py` | PASS | [log](../validation/2026-10-06-session/verify_session_normal_independent_audit_validation_2026_10_07.log) |
| `computations/verify_session_normal_nonreduced_trees.py` | PASS | [log](../validation/2026-10-06-session/verify_session_normal_nonreduced_trees_validation_2026_10_07.log) |

The reduced normal-carrier companion reconstructs the complete inverse ADE columns, enumerates the reduced cycle/ADE numerical constraints, and verifies the numerical normal-sheaf contradiction in its last row. The separately implemented independent scan imports no primary normal companion and finds the same five correction configurations, with full denominators `2,2,2,2,6`. Both regenerated reports agree byte-for-byte with their prior retained JSON outputs. This validates the arithmetic; the geometric passage, classification, compression, and local defect arguments are separately audited inputs.

The stabilized nonreduced tree source has SHA-256 `fca8eb7c177d88d00adcf5c60f664f8bbf9926abaf586762f22bfedf4199a2a7`; its reduced-source dependency has SHA-256 `57c73e7fc597d892dde3628dc0a7c0da2e6e61514af7890118e057f29b5cef13`. The independent live run took 22.899 seconds and its JSON output hash `52c5633b19828017636f1a88e74d8989129edb9d4a6abbfefb850ce893402c36` agrees exactly with the owner's retained report. It verifies:

- 381802 tree diagonal modifications under the stated rank/excess budgets;
- 195 admissible positive integral anticanonical cycles;
- 236 exact correction matches, of which 12 remain after degree-at-most-five compression;
- all 12 remaining rows have `d=3,t=2`;
- zero rows remain after applying the **external geometric Type-D passage input `t=1`**.

The source checks every successful leaf-elimination solve against its original linear equations and uses full inverse-column denominators. Its last filter is an arithmetic application of a geometric premise; the computation does not itself prove that premise or the classification's exhaustion of surfaces. The stronger normal-quartic conclusion requires the separately audited geometric argument in the normal-carrier/frontier notes.

The new dx1 audit has SHA-256 `6c2fcf9747814a6dff5f06af9043c2dc2d6fa2123a39fda23715c2f09393fc63`. It independently regenerates all five `Q_i` from the dated obstruction dump, proves their specialization denominators and equivalence on the basepoint-free chart, checks equality with the legacy source inputs, and expands the saved shifted 5-by-6 witness over QQ. It also establishes the exact comparison with the retained universal coordinate implementation: reversed obstruction coordinates differ by the stated factor 32, and the resultants agree. Its generated standalone M2 source, metadata, and output all agree byte-for-byte with the prior retained files; the generated M2 assertions check both ideal containments, the colon/saturation equality, the radical, and the two boundary square ideals.

The [additional input manifest](../validation/2026-10-06-session/additional-input-hashes-2026-10-07.json), [three-source results](../validation/2026-10-06-session/additional-results-2026-10-07.json), and [nonreduced result](../validation/2026-10-06-session/additional-nonreduced-result-2026-10-07.json) retain exact replay boundaries. These four new checks add to the existing record; they do not turn arithmetic agreement into a global STCI theorem.
