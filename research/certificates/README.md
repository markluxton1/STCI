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
