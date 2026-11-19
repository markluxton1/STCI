---
id: STCI-I-0005
type: investigation
title: Bounded equation search through the elliptic double inverse
status: complete
scope: "#scope"
question: "#question"
findings: "#findings"
relations:
  - kind: motivates
    from: [STCI-F-0005, STCI-F-0006]
    to: [STCI-I-0005]
    at: "#purpose"
  - kind: uses
    from: [STCI-R-0076]
    to: [STCI-I-0005]
    at: "#inputs"
---
# Bounded equation search through the elliptic double inverse

## Scope

Over an algebraically closed field of characteristic zero, fix
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). In the marked elliptic
double-inverse construction, test the line
\(\mu=2,\ \rho_0=\rho_1=\rho_3=0,\ \rho_4=p\) for every geometric
parameter \(p\). The candidate equation pairs consist of the implicit
octic of a basepoint-free birational member and a homogeneous mate of
any positive degree. A separate search exhausts the smooth
\(\mathbf F_5\)-rational parameter tuples of the reduction at \(i=2\)
and tests inverse points over \(\overline{\mathbf F}_5\).
[Construction and actual equation conditions](../../arguments/carriers/elliptic_double_inverse_construction.md#5-fiberwise-support-and-actual-descending-equations).

## Question

Does any basepoint-free member of the characteristic-zero line have
full inverse support on the marked elliptic curve? For the separate
finite-field candidate search, does any of the specified rational tuples
give the unit inverse ideal (7)? The bounded investigation ends when
both parameter tests are exhausted. Any support survivor would still
need the octic image and a descending identity (8) to give a defining pair.

## Purpose

The carrier-normalization strategy supplies actual quadratic sections and
requires absence of isolated inverse support. The global realization
strategy asks whether the pure power of the marked divisor descends as a
homogeneous polynomial in those sections. The two computations test the
support requirement first. The [classified toric quintic search](../../arguments/carriers/quintic_toric_center_incidence.md#exact-elimination-on-m0)
uses a different source and does not decide this elliptic family.
[Carrier normalization](../../frameworks/carrier-normalization/index.md) ·
[Global equation realization](../../frameworks/global-equation-realization/index.md).

## Inputs

The length-twelve support criterion supplies the scheme whose intersection
with \(E\) is necessary for full inverse support on a basepoint-free fiber.
[STCI-R-0076 and its proof](../../results/elliptic_inverse_support.md).

## Findings

- The characteristic-zero line has no basepoint-free fiber with full
  inverse support. Every octic from the tested line therefore fails to
  admit a homogeneous mate of any degree. [Proof and characteristic-zero replay](../../arguments/carriers/elliptic_double_inverse_construction.md#the-characteristic-zero-center-line).
- The search over the 1,250 smooth rational parameter tuples at \(i=2\)
  in \(\mathbf F_5\) yielded no unit inverse ideal. [Finite-field evidence and replay](../../computations/README.md#elliptic-double-inverse-candidate-search-over-f5).

The broader characteristic-zero question is whether the support-unit locus
meets the smooth, basepoint-free, birational locus in the full five-parameter
family. A survivor would require the pure-power identity (8), including
the actual conductor descent. The unrestricted characteristic-zero STCI
question remains open. [Remaining constructive question](../../arguments/carriers/elliptic_double_inverse_construction.md#6-low-degree-filters-and-the-constructive-question-that-remains) ·
[Degree bounds and literature status](../../literature/README.md#current-status-and-general-bounds).
