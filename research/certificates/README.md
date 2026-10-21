# Certificate map

Exact computations support specific statements; they do not enlarge theorem scope. Source files remain in ../computations/ during this cleanup pass so existing scripts and historical references keep working.

## dx=1 / P-044 slice

Current closure uses session_dx1_saturation_2026_10_06.m2 and its recorded output, the compact colon certificate, verify_session_dx1_independent_2026_10_06.py, and the boundary/residual companion checks.

Scope: basepoint-free P-044 classification on the dx=1 slice, not global P-044.

## Primitive e=2 quartic

Promoted checks:
- verify_primitive_quadruple_universal.py
- verify_primitive_quartic_factor_audit.py
- verify_primitive_triple_parity.py

Scope: the audited primitive-fourth zero locus and quartic factorization used for the e=2 (4,7) and (4,8) branches. Do not extrapolate to arbitrary mate degree.

## Local cohomology

Promoted checks include verify_localcoh_finite_principal_parts.m2, the direction/pure-direction/constant-direction/generic-length verifiers, and the two 2026-10-06 incidence computations with their JSON data.

Scope: finite reduction, tensors, and named subfamilies. The full bilinear incidence problem remains open.

## MF6

verify_mf6_defect12.py and verify_mf6_type3.py support the audited defect/type-3 calculations. They are not a complete multiplicity-six exclusion.

## Normal carriers

verify_normal_quartic_simple_elliptic.py supports the simple-elliptic exclusion. verify_normal_rational_carrier_compression.py supports finite denominator compression; it is not an exclusion of the remaining rational-resolution cases.

## Split carriers

The split4 and split22 promoted verifiers support exact reductions and named strata, not a global split-carrier exclusion.

## Excluded historical checks

The historical localcoh symbol parity/seed Macaulay2 checks with the faulty quartic-basis construction are not theorem certificates and were not promoted.


## October 20–21 Z4 arithmetic lift — STCI-R-0012

[Canonical scope](../results/prescribed_z4_arithmetic_nonlifting.md), [source proof](../notes/2026-10-20-z4-characteristic-zero-lifting-report.md), [independent Macaulay2 audit](../notes/2026-10-20-z4-lift-independent-audit.md). Exact scripts: `verify_z4_local_structure_2026_10_20.m2`, `verify_z4_global_quartics_2026_10_20.m2`, `verify_z4_quartic_obstruction_2026_10_20.py`, `audit_z4_lift_2026_10_20.m2`. Check `validation/z4-lift-2026-10-20/` logs for prior recorded runs. These certify exact identities and the mod-four polynomial congruence, not the deformation reduction by themselves. No expensive computation was rerun during this promotion.

## Actual-generator movement — STCI-R-0014 and R0015

`global_ci_small_movement_divisor_audit.py` checks the **necessary arithmetic system**, including the six movement-two rows and counts for epsilon 1–8. The exhaustive mathematical proof is in [the generator investigation](../notes/2026-10-19-global-ci-filtration-investigation.md) and [fixed-movement audit](../notes/2026-10-19-global-ci-filtration-independent-audit.md). Neither a Picard-descent test nor a witness for an actual STCI is certified.
