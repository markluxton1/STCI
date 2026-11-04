---
id: STCI-R-0037
type: result
title: Bounded supported Hilbert loci and both full torus limits
status: provisional
scope: "#scope"
statement: "#statement"
proofs:
  - name: projective-supported-incidence
    at: "research/arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits"
    using: []
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
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
some \(H_N\), together with both of its full torus limits. This assertion
does not supply a uniform value of \(N\).

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

The source is the
[supported Hilbert-boundary section](../synthesis/global_equations_and_constructions.md#the-supported-hilbert-locus-and-its-full-torus-boundary),
supplemented by the fixed-\(N\) incidence in
[attracting strata and generator incidence](../synthesis/torus_attracting_strata_and_generator_incidence.md#invariant-limits-stratify-moving-ideals).

## Limitations

This is a bounded support-preservation theorem, not a classification of
fixed points or their attracting loci. It proves neither finiteness nor
local closedness of any proposed point-indexed decomposition. A fixed
\(N\) covers only its declared incidence, and no nonempty supported
complete-intersection locus is exhibited.

The two full limits need not be the same ideal and need not retain two
generators. Neither the ideal of two equation initials, an
\(\mathcal I\)-adic normal-cone initial ideal, a pure hull, nor the
fundamental cycle is a substitute for the full limit. This result gives
no map identifying endpoint data of a finite transverse modification
with these opposite Hilbert limits, and no unrestricted STCI conclusion.

## Review

Independent reconstruction review accepted this route and its exact
scope: scheme-theoretic closed incidence via relative generation and
base change, both proper full limits in every characteristic, individual
nilpotence bounds, and generic length including embedded boundary
structure. The reviewer reconstructed the proof, compared the declared
sources, and found no blocking mathematical correction or lost
contribution. No mathematical computation was needed. Acceptance gives
no uniform \(N\), classification, nonempty incidence, numerical
generator cutoff, or quotient-comparison theorem. The Result remains
provisional; review acceptance is not promotion.

Separately, the source's October 31, 2026 scope review accepted the
distinctions between support invariance and ideal invariance, full limits
and extreme forms, embedded data, and fixed-family coverage; it did not
certify a deformation-existence theorem. That inherited decision is
distinct from the independent reconstruction decision above. The
source's surrounding trace discussion is framed in characteristic zero;
the geometric incidence, nilpotence and properness proof here uses no
characteristic restriction. The characteristic-free statement was
explicitly included in the reconstruction review. This acceptance
does not cover the composite trace corollary STCI-R-0040, whose separate
reconstruction decision is recorded in its own Result.
