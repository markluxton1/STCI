# Adjudication: CR-44–46 — dual sextic singular scheme
Date: 2026-10-26. Final three claims, inspected written proof, exact M2 source assertions, saved M2 output, and independent audit; no fresh Macaulay2 execution. No canonical promotion.

Setup: k algebraically closed characteristic zero, fixed marked quartic. S=k[A,B,C,D], L=BC-4AD, K=AC²+B²D, Delta=-4L³-27K², J=Jac(Delta), h=(BC+8AD)K, U=J+(h).

- **CR-44 VERIFIED.** J is saturated, J:h=(B,C,AD), U/J≅(S/(B,C,AD))(-5). U is unmixed, and J has exactly two embedded endpoint contributions of length one each. Three syzygies and local weighted nonmembership establish nonzero endpoint socles; local Hilbert–Burch minors establish unmixedness. Saved M2 asserts global saturation and colon identities.
- **CR-45 VERIFIED with exact saved certificate.** U=(A,B²)∩(D,C²)∩T_O∩P_B, with T_O primary to osculating quartic P_O and P_B reduced bitangent quartic prime. J has six associated primes, four minimal and two embedded. Degree 16; Hilbert polynomials HP(S/J)=16n-43, HP(S/U)=16n-45, HP(U/J)=2.
- **CR-46 VERIFIED geometrically.** Away from hyperosculating endpoints, ordinary cusp transverse models along osculating quartic and endpoint pencil lines give curvilinear double Jacobian structure (x²,y), while ordinary node model along bitangent quartic gives reduced Jacobian (x,y). Generic transverse analysis alone does not prove endpoint corrections.

Sources: notes/2026-10-24-quartic-dual-singular-scheme.md; computations/verify_quartic_dual_singular_scheme_2026_10_24.m2; computations/quartic_dual_singular_scheme_2026_10_24_m2.txt; computations/quartic_flag_duality_independent_audit_2026_10_24_m2.txt; notes/2026-10-24-quartic-flag-duality-independent-audit.md.

Disposition: one singular-scheme package cross-referenced to CR-22, not a duplicate. All 46 inventory claims now adjudicated; this is not an exhaustive historical manifest or canonical promotion.
