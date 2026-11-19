---
id: STCI-R-0075
type: result
title: Toric quintic normalizations exclude every mate degree
scope: "#scope"
statement: "#statement"
proofs:
  - name: marked normalization and full inverse support at every projection center
    at: "research/arguments/carriers/quintic_toric_center_incidence.md#1-geometric-object-and-scope"
    using: [STCI-R-0003]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Toric quintic normalizations exclude every mate degree

## Scope

Fix \(C_0=[s^4:s^3t:st^3:t^4]\) in \(\mathbf P^3\) over an
algebraically closed field of characteristic zero. Let \(S\) be an
integral quintic hypersurface containing \(C_0\) whose normalization is
a toric surface. The projection and the mate may be arbitrary within
these hypotheses.

## Statement

For every positive-degree homogeneous form \(G\) meeting \(S\) properly
and containing \(C_0\), the intersection has a curve component distinct
from \(C_0\).

Under a hypothetical mate the marked-source classification gives a
unique curve \(c\) above \(C_0\) and an upstairs section \(q\) with
divisor \(5c\). The projection calculation finds a point outside \(c\)
above \(C_0\) for every admissible center. Every power of \(q\) is
nonzero at that point, whereas the pullback of a mate must vanish there.
[Source classification](../arguments/carriers/quintic_non_gorenstein_toric_sources.md#41-this-is-the-only-remaining-polarized-toric-normalization) ·
[Complete center proof](../arguments/carriers/quintic_toric_center_incidence.md)

## Limitations

Among nonnormal quintics the open cases include non-toric,
non-Gorenstein normalizations. The argument gives no exclusion for
arbitrary higher-degree carriers. [Degree-five bounds](../frameworks/carrier-normalization/degree_exclusions.md)

## Review

The marked-source classification, finite and one-infinity charts, and
the three previously settled exceptional curves retain their recorded
reviews. For the last exceptional curve an independent replay checked
the coefficient equations, all four factors of the projected resultant
gcd, their specialized fibers and the nonvanishing conditions. Combined
with the preceding cases, this exhausts the centers that could yield a
mate. [Last elimination and exact evidence](../arguments/carriers/quintic_toric_center_incidence.md#exact-elimination-on-m0)
