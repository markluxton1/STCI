---
id: STCI-R-0037
type: result
title: Bounded supported Hilbert loci and both full torus limits
scope: "#scope"
statement: "#statement"
proofs:
  - name: projective-supported-incidence
    at: "research/arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#statement"
---
# Bounded supported Hilbert loci and both full torus limits

## Scope

Let \(k\) be an algebraically closed field of any characteristic,
\(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), and
\(\mathcal I=\mathcal I_C\). Fix positive integers \(a,b,N\), and put
\[
P_{a,b}(n)=abn+\frac{ab(4-a-b)}2.
\]
This is the Hilbert polynomial of a proper complete intersection of
degrees \((a,b)\). The containments below are containments of ideal
sheaves on \(\mathbf P^3\), not assertions about two selected equations
or their initial forms. Write
\[
\lambda(t)[x_0:x_1:x_2:x_3]
 =[x_0:tx_1:t^3x_2:t^4x_3]
\]
for the action of \(T=\mathbf G_m\). No Cohen--Macaulay, Gorenstein,
purity, or two-generator hypothesis is imposed on the boundary ideals.

## Statement

The incidence functor in \(\operatorname{Hilb}^{P_{a,b}}(\mathbf P^3_k)\)
defined by
\[
H_N=\{Y:\mathcal I^N\subset\mathcal I_Y\subset\mathcal I\}
\]
is represented by a closed projective \(T\)-stable subscheme. Every
geometric point has reduced support exactly \(C\).

For every \(Y\in H_N(k)\), its orbit morphism
\(t\mapsto\lambda(t)Y\) extends uniquely to a morphism
\(\overline o_Y:\mathbf P^1\to H_N\). Consequently its two full flat
limits
\[
Y_+=\overline o_Y(0),\qquad Y_-=\overline o_Y(\infty)
\]
exist and are \(T\)-fixed points of \(H_N\). Each has the same Hilbert
polynomial \(P_{a,b}\) and reduced support \(C\); both belong to the same
connected component of \(H_N\) as \(Y\). The family obtained by pulling
back the universal Hilbert family is the full embedded flat family.
Its fibers are retained with all their nilpotent and embedded structure.

Every projective subscheme with reduced support \(C\) satisfies
\(\mathcal I^N\subset\mathcal I_Y\subset\mathcal I\) for some positive
integer \(N\) depending on that subscheme. Thus every actual
sole-supported proper degree-\((a,b)\) complete intersection belongs to
some \(H_N\), together with both of its full torus limits. For arbitrary
supported Hilbert points this nilpotence argument is individual. On the
actual CI sublocus there is the stronger uniform bound
\[
\mathcal I_C^{m}\subset\mathcal I_Y,
\qquad m=ab/4.
\]
The CI ideal is \(I_C\)-primary, and the \(m\)-th power of the maximal
ideal of its generic length-\(m\) algebra is zero. Primary contraction
therefore gives \(I_C^{(m)}\subset I_Y\), hence the displayed ordinary
power containment. Closedness of this incidence preserves it along the
supported orbit. Thus \(H_m\) covers every actual sole-supported CI of
this degree type and both intrinsic limits; for \((6,6)\) one can use
\(H_9\).

For every point of \(H_N\), the generic length along \(C\) is
\(ab/4\). In particular nonemptiness implies \(4\mid ab\). For
\((a,b)=(6,6)\), the polynomial is \(36n-144\), its arithmetic genus
is \(145\), and the generic length is \(9\).

## Evidence

The complete geometric proof, including closedness as an incidence
functor, nilpotence, and the generic-length computation, is in
[Argument STCI-A-0001](../arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits).
No finite computation is required. The standard external inputs are
projectivity and the universal flat family of the projective Hilbert
scheme, sufficiently positive relative generation and cohomology/base
change, and extension over a nonsingular curve into a proper scheme;
their precise uses are explained there.

The uniform actual-CI power containment is proved in the
[supported graph comparison](../arguments/torus_hilbert_boundary.md#equationhilbertchow-graph-and-its-top-fiber).
Its primary-contraction argument is independent of characteristic. It does
not assert the same bound on arbitrary points of a larger top-Chow fiber.

The source is the
[supported Hilbert-boundary section](../arguments/equations/global_equations_and_constructions.md#the-supported-hilbert-locus-and-its-full-torus-boundary),
with the fixed-\(N\) directional formulation in
[F-0001](../frameworks/torus-supported-boundaries/index.md#directional-loci).

## Limitations

This is a bounded support-preservation theorem, not a classification of
fixed points or their attracting loci. It proves neither finiteness nor
local closedness of any proposed point-indexed decomposition. A fixed
\(N\) covers only its declared incidence of arbitrary Hilbert points.
For actual CIs the fixed-degree bound \(N=m\) above supplies coverage;
classification of fixed limits and their attracting families remains
unperformed, and no nonempty supported CI locus is exhibited.

The two full limits need not be the same ideal and need not retain two
generators. Neither the ideal of two equation initials, an
\(\mathcal I\)-adic normal-cone initial ideal, a pure hull, nor the
fundamental cycle is a substitute for the full limit. The separate
[endpoint-fiber theorem](intrinsic_limits_endpoint_fibers.md) identifies
their pure orbit images and embedded lengths from the finite transverse
modification. That comparison does not recover all full endpoint algebras
or prescribed-degree generators. No unrestricted STCI conclusion follows.
