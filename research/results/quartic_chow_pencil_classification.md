---
id: STCI-R-0079
type: result
title: Quartic pencils with the fixed Chow polytope
scope: "#scope"
statement: "#statement"
proofs:
  - name: endpoint contact, liaison residual genus, and canonical-module rigidity
    at: "research/arguments/torus/quartic_chow_pencils.md#classification"
    using: [STCI-R-0074]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Quartic pencils with the fixed Chow polytope

## Scope

For the **classification**, let \(k\) be an algebraically
closed field of **characteristic zero**. Take a proper
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
Every pair in this **characteristic-zero** scope satisfies
\(\sum n_i u_i/v_i=0\).

**Separate characteristic-two construction (not part of the
classification).** Reduction of the normalized exceptional
formulas at \(\lambda=1\) gives a non-invariant
single-support \((4,4)\) STCI presentation of \(C_0\).
This is proved directly by polynomial identities and a
boundary support check; it does **not** establish a complete
multi-support classification in characteristic two.

## Limitations

The separate [quartic-pair exclusion](quartic_44_filtered_exclusion.md)
rules out single support in characteristic zero, completing
the classification **only in characteristic zero**.
The revised liaison proof uses the characteristic-zero
balanced normal splitting
\(N_{C/\mathbf P^3}\simeq\mathcal O(7)^{\oplus2}\);
it does not prove the full uniqueness statement in
odd positive characteristic. The invariant line-and-quartic
model has its own separately stated characteristic scope.
No positive-characteristic classification is asserted here. The [Hilbert--Burch first-normal formulation](../arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
gives an intrinsic degeneracy locus for doubled support.
Every proper \((4,4)\) member of that locus
[self-links the locally complete-intersection union](../arguments/torus/quartic_chow_pencils.md#self-linkage-and-the-canonical-conormal-quotient):
the nilpotent sheaf is canonically \(\omega_Y(-4)\), and
the degree-three and degree-four equation maps satisfy
the stated Serre-duality tests. These are established
liaison/Ferrand mechanisms, not new classification theorems.
The [geometric uniqueness proof](../arguments/torus/quartic_chow_pencils.md#two-translates-with-coinciding-cubic-jets)
**does replace** the former coefficient-based uniqueness
and triple-branch exclusions. Linkage makes the residual
to \(Y\) an eight-degree Cohen--Macaulay curve of genus seven;
a hypothetical \((3,1)\) or \((1,3)\) partition would require
a forbidden \(\mathcal O(-8)\) quotient of the balanced
conormal \(\mathcal O(-7)^{\oplus2}\).
For \((2,2)\), self-linkage identifies
\(I_Y/I_Z\simeq\omega_Y(-4)\).
Dualizing Hilbert--Burch and restricting the resulting
quadratic identity to \(V(x_1,x_2)\) forces the unique
\(\lambda\)-orbit. The canonical-module calculation
retains actual quartic generators rather than replacing
them with an abstract doubling.
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

The original coefficient-based classification was accepted for
its mathematical scope. The replacement
[linkage/canonical-module argument](../arguments/torus/quartic_chow_pencils.md#two-translates-with-coinciding-cubic-jets)
now closes the remaining uniqueness and triple-branch gates
without coefficient elimination: residual genus excludes
the asymmetric multiplicities, and the canonical module of
the Hilbert--Burch union plus the residual-line restriction
classifies all proper doubled pencils.
The argument relies on established Peskine--Szpiro linkage,
Ferrand doubling and the accepted balanced normal splitting
of the fixed rational quartic.
The Hilbert--Burch proof also replaces the earlier
weight/parity monomial enumeration, while a second
Hilbert--Burch resolution and exact sequence replace the
full-flat-limit Gröbner calculation. The sextic conormal
rank table is replaced at its canonical argument owner.
A subsequent **independent mathematical review of
the updated geometric proof (PR #171, head \`f323856\`)**
reconstructed the residual genus/Ferrand obstruction,
the canonical-module relations, the residual-line
restriction and its signs, and the full flat-limit
and sextic syzygy arguments. It found no substantive gap
in the **characteristic-zero quartic uniqueness proof**,
but correctly identified the previously overstated
characteristic scope and the separate degree-independent
involution--Bézout regularity hypothesis; both
statements have now been restricted at their owners.
This is a scoped independent correctness reconstruction,
not a claim that all six independent review perspectives
have been completed.
The earlier separate reviews of the characteristic-two
specialization, opposite full limits, and retained-carrier
theorem preserve their stated scopes. No unrestricted
higher-degree STCI claim follows.
