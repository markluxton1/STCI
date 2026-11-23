---
id: STCI-R-0084
type: result
title: Sign-invariant ACM sources and one sign-eigen equation force zero first moment
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
translated-quartic cycles with positive multiplicities. For the ACM theorem,
actual homogeneous ideals are invariant under
\(\tau=\operatorname{diag}(1,-1,-1,1)\). The coordinate algebra must
be finite flat over \(k[x_0,x_3]\), as holds for an ACM curve avoiding
the fixed projection center. For the additional CI consequence only one
actual generator need be a \(\tau\)-eigenform.

## Statement

Every such curve satisfies \(M_1=\sum_i n_i u_i/v_i=0\). Neither a CI
presentation, a Gorenstein hypothesis nor a specified Hilbert numerator is
required. Full intrinsic-torus invariance implies the required sign symmetry.

The proof constructs the basis-independent differential
\(\operatorname{Tr}(dX\wedge dY)=2M_1\,dx_0\wedge dx_3\) from the
actual commuting multiplication matrices. Homogeneous sign symmetry forces
it to vanish term by term.

For a proper actual CI with the same entire-cycle hypothesis, one
sign-eigen generator \(F\) suffices, including reducible and nonreduced
\(F\): the proper sign-invariant norm pair \((F,G\tau G)\) has twice
the original cycle. Thus nonzero moment forbids a sign-eigen member of
the smallest actual generator space. The
[norm reduction and actual-source comparison](../arguments/torus/sign_symmetry_and_actual_sources.md)
also give sign-breaking controls with zero moment and a canonical
source-saturation description of the symmetrized union's section defect.

In characteristic zero, both opposite invariant pure hulls of a hypothetical
sole-supported CI must therefore be non-ACM. An ACM invariant pure hull of
any Hilbert numerator already suffices to force vanishing.

The [section-defect refinement](../arguments/torus/chow_section_parity_defect.md)
shows more: nonzero moment on an invariant pure curve requires opposite
signs among equal-degree free section generators and a nonstandard-parity
class in the head of its finite section/Rao defect. This necessary condition
occurs for the single reduced quartic; no exclusion of it in CI limits is known.

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
The norm reduction was independently reconstructed in the current
contribution, including properness and cycle additivity for nonreduced
generators. This extends the actual-source coverage; it is not a review
of arbitrary non-invariant CI ideals.
