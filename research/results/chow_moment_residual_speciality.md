---
id: STCI-R-0083
type: result
title: Residual speciality forces first-moment vanishing on repeated arrangements
scope: "#scope"
statement: "#statement"
proofs:
  - name: low-degree linkage symmetry and conormal filtration
    at: "research/arguments/torus/chow_moment_residual_speciality.md#1-a-low-degree-symmetry-criterion-from-linkage"
    using: [STCI-R-0020]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Residual speciality and first-moment vanishing

## Scope

Over an algebraically closed field, let \(J=(F_a,G_b)\), \(a\le b\),
be a homogeneous proper complete intersection with reduced support \(Y\),
preserved by a diagonal torus action. Let \(R\) be residual to \(Y\) in
\(V(J)\). The translated-quartic consequences require characteristic
different from two, with all positive cycle multiplicities interpreted in
the field. The unrestricted target remains characteristic zero.

## Statement

If \(H^1(\mathcal O_R(b-4))=0\), linkage gives \((I_Y)_a=J_a\).
Consequently the smaller generator is an eigenform if \(a<b\), and
the ideal is invariant if \(a=b\). This symmetry criterion is valid in
every characteristic.

For an entire translated-quartic cycle, the criterion implies
\(M_1=\sum_i n_i u_i/v_i=0\). If exactly one component has multiplicity
\(n\ge2\) and all other components are simple, the sufficient bound is
\(4b\ge7n+1\). In particular, exactly one double component and any
number of simple components satisfy the moment relation in every degree;
one triple component and simple companions satisfy it for \(b\ge6\).

[Proof and precise boundaries](../arguments/torus/chow_moment_residual_speciality.md).

## Limitations

Nonzero residual cohomology does not imply a nonzero moment or a realizable
counterexample. Higher residual structures cannot be replaced by their
reduction. The sufficient single-component bound gives no new sole-support
exclusion in smaller-generator degree at least three. UM1 and unrestricted
characteristic-zero STCI remain open.

## Review

A repeated-structure researcher derived the linkage and conormal-filtration
criteria. A distinct Sol/max correctness reviewer independently reconstructed
the residual identification, ideal-sheaf duality, saturation, all-characteristic
torus representation argument, and filtration including possible torsion
layers on November 23, 2026. The existing moment theorem and R-0020 are
inherited inputs. That reviewer also checked the written argument and its
characteristic qualifications. Full contribution synthesis and integration
review is in progress.
