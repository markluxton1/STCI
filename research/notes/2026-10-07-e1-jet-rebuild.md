# e=1 jet lane rebuild — 2026-10-07

Base: current remote main at `7662a2ebb1dd561c1fb5e3c8958799b37d962c41`.

Purpose: reconstruct the e=1 primitive-triple quartic-carrier calculation on a clean branch. The older branch `research/jet-discrepancy-order-one-2026-10-06` is retained only for provenance.

## Imported theorem-level input

Bănică–Forster gives the standard double-to-triple splitting obstruction in
[
H^1(O_C(-4)).
]
The project-specific exact obstruction coordinates are independently persisted in
`research/computations/verify_e1_triple_obstruction.py`.

Their resultant-open zero locus is:
- main component (b_0=-2a_1, a_0b_1=-8a_1^2);
- boundary (a_0=b_1=0), with (r=b_0/a_1) satisfying
  ((r+2)(3r^2+4r+12)=0).

## Rebuild target

On the main component normalize
[
A=1+tz,qquad B=-2t-8t^2z,qquad t
e0.
]
The new self-contained certificate `verify_e1_jet_rebuild.py` reconstructs:
1. (I_C(4)) from all 35 ambient quartic monomials;
2. the first-symbol condition defining (I_{C_2}(4));
3. the BF quadratic chart correction;
4. the second-contact matrix for (C_3);
5. its kernel as actual ambient quartics (F_0,F_1);
6. the gcd of (F_0,F_1) over (mathbf Q(t)).

## Status discipline

The script contains exact symbolic assertions for the previously obtained dimensions/rank, but this branch has not yet recorded a runtime transcript from an independent Python execution. Therefore:
- the BF obstruction locus is **ported exact certificate / previously audited**;
- the rebuilt quartic assertions are **PENDING RUNTIME VERIFICATION**;
- no new gcd or residual-base-locus conclusion is promoted yet.

After runtime verification, compute/saturate the ideal ((F_0,F_1)) against (I_C), preferably in Macaulay2, and record the residual scheme uniformly over the parameter (t). Only then interpret the geometry and literature-check linkage/contact antecedents.
