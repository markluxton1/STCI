---
id: STCI-R-0085
type: result
title: Integral first equation jets constrain supported mixed-characteristic traits
scope: "#scope"
statement: "#statement"
proofs:
  - name: integral Koszul residue and the two first-jet source ideals
    at: "research/arguments/arithmetic/integral_first_jet_lifting.md#the-integral-source-identity"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Integral first equation jets and arithmetic lifting

## Scope

Homogeneous degree-\((a,b)\) pairs whose binary restrictions to
\(L=V(x_0,x_3)\) have invertible resultant. The source identity is integral
over the universal coefficient open and persists under base change. The
lifting conclusion concerns actual mixed-characteristic DVR traits whose
characteristic-zero generic intersection has sole geometric reduced support
the fixed quartic \(C_0\). No symmetry or generic curvilinearity is required.

## Statement

Write \(z=x_0,w=x_3,x=x_1,y=x_2\) and
\[
 F=f_0+zp+wq\pmod{(z,w)^2},\qquad
 G=g_0+zr+ws\pmod{(z,w)^2}.
\]
For the actual commuting multiplication matrices,
\[
 \operatorname{Tr}(dX\wedge dY)
 =\operatorname{Res}_{f_0,g_0}(ps-qr)\,dz\wedge dw.
\]
The residue coefficient lies in the product of the two ideals of first-jet
coefficients. On a supported DVR trait this gives
\[
 \frac{ab}{2}\in L_F L_G,\qquad
 v_\pi(L_F)+v_\pi(L_G)\le v_\pi(ab/2).
\]
The valuation formula includes residue characteristic two; the proof uses
the characteristic-zero generic fiber and the integral residue, rather than
the sign action on the characteristic-two special fiber.

For the explicit non-eigen degree-\((16,p)\) special pairs, \(p\ge43\),
both first jets vanish. Any supported trait through such a point therefore
has \(v_\pi(p)\ge2\), excluding unramified traits even with arbitrary
simultaneous coefficient variation. The earlier ramified \((7,8)\)
zero-scalar-trace control fails this differential condition: its coefficient
is \(56/3\), whereas sole support would require \(28\).

[Proof and source calculations](../arguments/arithmetic/integral_first_jet_lifting.md).

## Limitations

These are necessary conditions on actual traits. The result does not assert
a strong \(W_2\) extension, exclude arbitrary ramified traits through the
\((16,p)\) points, calculate every horizontal component of the full pair
incidence, or prove unrestricted characteristic-zero nonexistence.

## Review

A distinct correctness reviewer independently reconstructed the universal
integral identity, residue regularity without integer division, the product
of the two source ideals, the all-prime trait valuation statement, the
non-eigen source calculation and the ramified control on November 23, 2026.
The characteristic-zero matrix/residue identity and full translated-cycle
formula are inherited reviewed inputs. The finite-Witt extension was
outside the accepted scope.
