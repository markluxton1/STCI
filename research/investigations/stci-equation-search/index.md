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
  admit a homogeneous mate of any positive degree. [Proof and characteristic-zero replay](#characteristic-zero-center-line).
- In the reduction at \(i=2\) over \(\mathbf F_5\), each of the 1,250
  tested rational parameter tuples fails the combined basepoint-free
  and full inverse support requirement. [Finite-field scope and replay](#finite-field-candidate-search).

The broader characteristic-zero question is whether the support-unit locus
meets the smooth, basepoint-free, birational locus in the full five-parameter
family. A survivor would require the pure-power identity (8), including
the actual conductor descent. The unrestricted characteristic-zero STCI
question remains open. [Remaining constructive question](../../arguments/carriers/elliptic_double_inverse_construction.md#6-low-degree-filters-and-the-constructive-question-that-remains) ·
[Degree bounds and literature status](../../literature/README.md#current-status-and-general-bounds).

## Characteristic-zero center line

On the stated line the source \(S_2=V(Q_1+2Q_0)\) is smooth. For a
basepoint-free fiber, the two sections \(g_0,g_\infty\) cut out the
length-twelve zero scheme \(Z\) on \(D=V(d)\), since the two pulled-back
ruling coordinates have no common zero. If the fiber has full inverse
support, then \(|Z|\subset E\) and the positive length forces
\(Z\cap E\ne\varnothing\). Thus \(d,g_0,g_\infty\) must have a common
point on \(E\). [Geometric support criterion](../../results/elliptic_inverse_support.md#statement).

The script works over \(K=\mathbf Q(i)\). It divides the three numerators
by \(Q_0\) modulo \(Q_1+2Q_0\), verifying the identities for the quotients
\(d,g_0,g_\infty\). Let \(I_j\) be the ideal imposing these three divided
equations and \(Q_0=Q_1=0\) on the chart \(Z_j=1\). The four charts cover
\(E\), so the projection of their disjoint union to the \(p\)-line records every
geometric parameter at which the common point exists. The script
computes
\[
 \bigcap_{j=0}^3 (I_j\cap K[p])=(P(p)),
\]
where \(P\) has degree six and is squarefree. Each contraction is the
kernel of the corresponding map from \(K[p]\) to the chart coordinate
ring. These kernels, and their finite intersection, commute with field
extension by flatness. Over any algebraically closed extension of \(K\),
the zero set of each contraction is the closure of the corresponding
chart image, and the union of those four closures consists of the six
roots of \(P\). Each chart image is therefore contained in a finite set of
closed points, so it is already closed. The union of the actual chart
images is exactly those six geometric parameters. The resulting
parameter scheme \(V(P)\) is geometrically reduced.

For the off-\(E\) test the script imposes \(P=0\), \(Q_0=1\),
the source quadric, and all four undivided inverse equations (7).
Every geometric projective point off \(E\) on \(S_2\) has a representative
with \(Q_0=1\), by rescaling with a square root of \(Q_0^{-1}\).
The contraction of the off-\(E\) ideal to \(K[p]\) again equals \((P)\).
It defines the scheme-theoretic image in the parameter line. The
geometric image lies inside the six closed points of \(V(P)\), so it is
closed and equals that entire set. Reducedness here concerns the
parameter image. This computation determines existence in each of the
six off-\(E\) fibers, with no calculation of their lengths or
multiplicities.

On \(Q_0=1\) with \(P=0\), the source equation and the four section rows
generate the unit ideal. This separate test rules out basepoints there.
On \(E\) the rows give the marked morphism (2), which has no basepoint.
All six candidates are consequently basepoint-free and have a
geometric inverse point outside \(E\). At every other parameter, a
basepoint-free fiber fails the necessary condition \(Z\cap E\ne\varnothing\).
For a birational member, the failure of full inverse support rules out a
homogeneous mate of every positive degree for its implicit octic.
[Equations (7) and (8)](../../arguments/carriers/elliptic_double_inverse_construction.md#5-fiberwise-support-and-actual-descending-equations).

The [characteristic-zero script](elliptic_center_line.m2) checks the
division identities, both elimination ideals, squarefreeness and the
basepoint ideal. Run it from the repository root.

```sh
M2 --script research/investigations/stci-equation-search/elliptic_center_line.m2
```

## Finite-field candidate search

The separate reduction uses \(i=2\) and the smooth rational
\(\mu=2,3\) over \(\mathbf F_5\), with all \(5^4\) rational lifts for
each. Every ideal on \(Q_0=1\) generated by the full undivided inverse
equations (7) is proper in its source fiber ring. Faithful flatness
preserves properness over \(\overline{\mathbf F}_5\), where a geometric
point of the ideal is either a basepoint or an off-\(E\) inverse point.
The conclusion covers the combined test for these rational parameter
tuples at this reduction. The characteristic-zero conclusion follows
independently from the elimination above.
[Finite-field evidence and replay](../../computations/README.md#elliptic-double-inverse-candidate-search-over-f5).
