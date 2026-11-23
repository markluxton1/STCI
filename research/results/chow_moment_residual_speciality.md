---
id: STCI-R-0083
type: result
title: Residual-cohomology vanishing forces first-moment vanishing on repeated arrangements
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
More precisely its dimension is \(\dim(I_Y)_a-\dim J_a\), so the
criterion is exactly exhaustion of the lowest equation space of the
reduced support.
Consequently the smaller generator is an eigenform if \(a<b\), and
the ideal is invariant if \(a=b\). This symmetry criterion is valid in
every characteristic.

For an entire translated-quartic cycle, the criterion implies
\(M_1=\sum_i n_i u_i/v_i=0\). If exactly one component has multiplicity
\(n\ge2\) and all other components are simple, the sufficient bound is
\(4b\ge7n+1\). In particular, exactly one double component and any
number of simple components satisfy the moment relation in every degree;
one triple component and simple companions satisfy it for \(b\ge6\).
In characteristic zero the one-triple class is covered in every degree:
the remaining \((4,5)\) case follows from residual genus, endpoint ranks
and an irreducible extreme component of the actual quartic generator.

If every multiplicity is at most two, the residual is the reduced union
\(D\) of doubled components. Explicit endpoint conductor orders
\(\alpha_i,\beta_i\) give the sufficient condition
\(4(b-4)\ge\max_i(\alpha_i+\beta_i)-1\). For two doubled components,
\[
 h^1(\mathcal O_D(1))
 =[u_1=u_2]+[v_1^2/u_1^3=v_2^2/u_2^3]
              +[u_1^2/v_1=u_2^2/v_2].
\]
The proof states the configuration-sensitive orders and uniform degree
consequences; this is a sufficient source criterion, not a converse.

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
layers on November 23, 2026. The source-algebra lead supplied the conductor
bound and exact two-component cohomology formula; the same distinct reviewer
reconstructed those proofs and their written formulations. The existing moment theorem and R-0020 are
inherited inputs. That reviewer also checked the written argument and its
characteristic qualifications. Full contribution synthesis and integration
review is in progress.
The characteristic-zero one-triple closure and the exact source-space
dimension identity were independently reconstructed by the separate
algebraic-geometry reviewer; the latter also received a generalizations
check. The proof retains inherited low-degree and regular-initial inputs.
