---
id: STCI-R-0084
type: result
title: Sign-invariant ACM translated arrangements have zero first moment
scope: "#scope"
statement: "#statement"
proofs:
  - name: commuting-matrix differential and homogeneous parity
    at: "research/arguments/torus/chow_acm_parity_vanishing.md#1-the-finite-flat-sign-symmetry-theorem"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Sign-invariant ACM arrangements and the first moment

## Scope

Algebraically closed fields of characteristic different from two; entire
translated-quartic cycles with positive multiplicities. Actual homogeneous
ideals are invariant under \(\tau=\operatorname{diag}(1,-1,-1,1)\).
The coordinate algebra must be finite flat over \(k[x_0,x_3]\), as holds
for an ACM curve avoiding the fixed projection center.

## Statement

Every such curve satisfies \(M_1=\sum_i n_i u_i/v_i=0\). Neither a CI
presentation, a Gorenstein hypothesis nor a specified Hilbert numerator is
required. Full intrinsic-torus invariance implies the required sign symmetry.

The proof constructs the basis-independent differential
\(\operatorname{Tr}(dX\wedge dY)=2M_1\,dx_0\wedge dx_3\) from the
actual commuting multiplication matrices. Homogeneous sign symmetry forces
it to vanish term by term.

In characteristic zero, both opposite invariant pure hulls of a hypothetical
sole-supported CI must therefore be non-ACM. An ACM invariant pure hull of
any Hilbert numerator already suffices to force vanishing.

## Limitations

Invariant cycles do not establish invariant ideals. Non-ACM finite projections
need not be flat, and replacing their algebras by free models does not preserve
the required actual embedding. No arbitrary CI can presently be reduced to
the invariant ACM case. In odd positive characteristic, multiplicities may
vanish in the field, so the characteristic-zero nonclosure consequence does
not follow when the total multiplicity is zero in the field.

## Review

The generalizations reviewer derived the theorem during synthesis. A distinct
repeated-structure investigator independently reconstructed the finite-flat
basis, gauge-invariant differential, separable splitting with nilpotents and
graded parity argument. The algebraic-geometry reviewer independently checked
the same mechanism, including the odd-characteristic extension.
