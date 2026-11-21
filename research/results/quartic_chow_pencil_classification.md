---
id: STCI-R-0079
type: result
title: Quartic pencils with the fixed Chow polytope
scope: "#scope"
statement: "#statement"
proofs:
  - name: weighted endpoint contact and the transverse determinant
    at: "research/arguments/torus/quartic_chow_pencils.md#classification"
    using: [STCI-R-0074]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Quartic pencils with the fixed Chow polytope

## Scope

Over an algebraically closed field, take a proper
\((4,4)\) CI with full Chow polytope \(4P_{C_0}\), where
\(C_0=[s^4:s^3t:st^3:t^4]\), and at least two distinct components.
Write \(H\) for the torus of weights \((0,1,3,4)\), and
\(C_{u,v}=[s^4:s^3t:u st^3:v t^4]\).

## Statement

The \(H\)-invariant pencils are given by the
[line-and-quartic model](../arguments/equations/chow_polytope_rigidity.md#quartics-including-invariant-collision-lifts).
Every other pencil has cycle \(2[C_{u,v}]+2[C_{u,-v}]\).
Over each such cycle the pencils are exactly the explicit
[one-parameter orbit](../arguments/torus/quartic_chow_pencils.md#classification).
The exceptional cycles lie outside the Chow closure of invariant
\((4,4)\) realizations. The non-invariant pencils form a vertical
\(H\)-orbit in the Hilbert fiber over each fixed exceptional Chow point.
Both full opposite limits preserve the cycle, with embedded length two
at opposite endpoints. The normalized exceptional support is
characterized by coincident cubic jets at both endpoints.
On the carrier \(G_1=0\) in characteristic zero, the resolved
ten-nodal K3 surface contains an explicit even eight; its half
maps to a nontrivial class \(C_++C_--2H\) of order two
in the carrier's Weil divisor class group.
Every pair in scope satisfies \(\sum n_i u_i/v_i=0\). In characteristic
two only the **multi-support** invariant case occurs; the
specialized exceptional formulas instead give a non-invariant
single-support \((4,4)\) STCI presentation.

## Limitations

The separate [quartic-pair exclusion](quartic_44_filtered_exclusion.md)
rules out single support in characteristic zero, completing the
classification in that characteristic. The [Hilbert--Burch first-normal formulation](../arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
gives an intrinsic degeneracy locus for doubled support.
Every proper \((4,4)\) member of that locus
[self-links the locally complete-intersection union](../arguments/torus/quartic_chow_pencils.md#self-linkage-and-the-canonical-conormal-quotient):
the nilpotent sheaf is canonically \(\omega_Y(-4)\), and
the degree-three and degree-four equation maps satisfy
the stated Serre-duality tests. These are established
liaison/Ferrand mechanisms, not new classification theorems.
The geometric conditions have **not yet replaced** the
coefficient-based uniqueness and triple-branch exclusions.
The [even-eight divisor calculation](../arguments/torus/quartic_chow_pencils.md#two-sided-contact-and-the-nodal-even-eight-carrier)
explains doubled divisors on one carrier, not uniqueness of
the family. The [characteristic-two specialization](../arguments/torus/quartic_chow_pencils.md#hilbert-over-chow-and-the-characteristic-two-collision)
has sole support and lies outside the characteristic-zero claim.
A further
[fixed-carrier deduction](../arguments/torus/quartic_chow_pencils.md#all-mate-degrees-on-a-retained-exceptional-carrier)
uses the [quartic-carrier exclusion](quartic_carrier_exclusion.md) to
classify all translated mates on a retained exceptional carrier in
characteristic zero. The unrestricted higher-degree realization locus
and its possible single-support pencils remain open.

## Review

The original classification review was accepted for its mathematical scope. The Hilbert--Burch descriptions now replace the original monomial enumeration, the full-limit Gröbner/Hilbert calculation, and the sextic conormal rank table; the self-linkage account uses standard duality. **The core uniqueness of the non-invariant quartic pencil still uses the explicit coefficient and third-order-contact argument**, so a fully intrinsic proof has not been certified. The later geometric and characteristic-two deductions are recorded with their own arguments and have not been promoted to a new completeness certificate. Independent reconstruction checked the endpoint evaluation kernels,
smooth graph argument, and two-branch transverse determinant through
first normal order. The invariant moment was rederived by change of
root coordinate. A separate proof review checked the specialization of
the labeled supports and actual pencils, the parameter saturations,
their Hilbert functions and the pure quotients at both ends. The
retained-carrier proof was separately checked using generic regularity,
extension across codimension two and the full quartic-carrier exclusion.
