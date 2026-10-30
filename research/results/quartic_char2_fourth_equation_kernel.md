---
id: STCI-R-0031
title: "Characteristic-two fourth normal equation and canonical kernel identification"
kind: theorem
status: proved
scope:
  characteristic: "2"
  curve: "fixed rational quartic C0"
  hypotheses:
    - "The prescribed quartic pair F=x1^4-x0^3*x3 and G=x2^4-x0*x3^3"
statement: "For the prescribed characteristic-two complete intersection, the filtered equation-module kernel and the fourth minimal initial-equation bundle are canonically isomorphic to O_C(-24), with comparison defect zero."
dependencies:
  - STCI-R-0020
  - STCI-R-0021
  - STCI-R-0030
evidence:
  - "research/notes/2026-10-23-ideal-filtrations-independent-investigation.md"
  - "research/validation/ideal-filtrations-2026-10-23/README.md"
independent_audits:
  - "research/notes/2026-10-23-ideal-filtrations-independent-review.md"
accepted_in: "research/notes/2026-10-23-ideal-filtrations-independent-review.md"
legacy_ids: []
supersedes: []
superseded_by: []
limitations:
  - "Only the prescribed characteristic-two pair"
  - "Inherited exact script validation, not freshly replayed"
  - "Does not assert a characteristic-zero lifting or STCI obstruction"
---
# Fourth normal equation in characteristic two

## Statement
For C0=[s^4:s^3t:st^3:t^4] in characteristic two and the prescribed quartics F=x1^4-x0^3*x3 and G=x2^4-x0*x3^3, put I=I_C, J=(F,G), D=J/IJ and H=in_I(J). The first conormal map phi:D -> I/I^2 has image O(-8), cokernel O(-6), and kernel O(-24). The full initial ideal has a single additional minimal generator in normal degree four: Q_4=H_4/(S_+H)_4=O(-24). All other Q_n for n at least two vanish. The comparison defect Delta is zero and the canonical filtration identifies ker(phi) with Q_4.

## Hypotheses and quantifiers
Only the specified embedded complete intersection over characteristic two, with the marked two-chart trivializations.

## Proof outline
On the first chart the full ideal is (v,u^4), with initial ideal (V,U^4); on the second chart the corresponding frames are (A,B^4). Hence Q_4 has transition B^4=a^(-24)U^4 and is O(-24). In the quartic equation-module frames r0=a^8 eF0+eG0 and rInfinity=eFInfinity+b^8 eGInfinity, the transition is rInfinity=a^(-24)r0, so ker(phi)=O(-24). More than matching degrees is needed: the corrected lift (a^8+a^4v+v^2,1) maps to u^4, while its infinity-chart counterpart (1,b^8+b^4A+A^2) maps to B^4, compatibly on overlap. Locally IJ=(v^2,vu,u^5), so in_I(IJ)=S_+H, and F^2D=F^3D=F^4D=ker(phi), F^5D=0. The canonical exact comparison of R-0030 is therefore an isomorphism Q_4 -> F^4D/F^5D.

## Dependencies
R-0020 supplies the characteristic-dependent conormal geometry, R-0021 the fixed degeneration, and R-0030 the exact comparison.

## Evidence and verification
The October 23 independent quartic audit explicitly checked both chart expansions, kernel frames, corrected lifts, fourth-order identification and transition compatibility. Its Python validation is saved. This promotion re-inspected the stated chart identities and audit but did not execute the scripts again.

## Consequences
The order-four initial generator is intrinsic to the filtered equation module in this special characteristic-two pair.

## Limitations
No general theorem for arbitrary characteristic-two pairs or characteristic-zero lifts. Nonlinear overlap terms still matter for reconstructing the full embedded intersection.

## Permanent evidence navigation

The `research/notes/` metadata above preserves historical provenance identifiers, not live paths on this branch. For the retained mathematical argument, hypotheses, and links into detailed supplements, follow [the consolidated subject chapter](../synthesis/03-infinitesimal-geometry.md). The original source identifiers are retained for audit provenance; this navigation link does not change the theorem's scope or status.
