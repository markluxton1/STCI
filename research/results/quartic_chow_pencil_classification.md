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
\((4,4)\) realizations. Both full opposite limits of the exceptional
orbit preserve the cycle, with embedded length two at opposite endpoints.
Every pair in scope satisfies \(\sum n_i u_i/v_i=0\). In characteristic
two only the invariant case occurs.

## Limitations

The separate [quartic-pair exclusion](quartic_44_filtered_exclusion.md)
rules out single support in characteristic zero, completing the
classification in that characteristic. A further
[fixed-carrier deduction](../arguments/torus/quartic_chow_pencils.md#all-mate-degrees-on-a-retained-exceptional-carrier)
uses the [quartic-carrier exclusion](quartic_carrier_exclusion.md) to
classify all translated mates on a retained exceptional carrier in
characteristic zero. The unrestricted higher-degree realization locus
and its possible single-support pencils remain open.

## Review

Independent reconstruction checked the endpoint evaluation kernels,
smooth graph argument, and two-branch transverse determinant through
first normal order. The invariant moment was rederived by change of
root coordinate. A separate proof review checked the specialization of
the labeled supports and actual pencils, the parameter saturations,
their Hilbert functions and the pure quotients at both ends. The
retained-carrier proof was separately checked using generic regularity,
extension across codimension two and the full quartic-carrier exclusion.
