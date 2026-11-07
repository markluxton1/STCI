---
id: STCI-R-0053
type: result
title: Actual coefficient kernels and the exact complete-intersection test for a constant quotient
scope: "#scope"
statement: "#statement"
proofs:
  - name: actual source spaces and degree exhaustion
    at: "research/arguments/torus_embedded_quotients.md#actual-equations-and-the-ci-criterion"
    using: [STCI-R-0051, STCI-R-0052, STCI-R-0056]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Actual coefficient kernels and the exact complete-intersection test for a constant quotient

## Scope

Let \(k\) be algebraically closed of arbitrary characteristic and
\(B=k[u^{\pm1},v^{\pm1}]/J\) be a specified embedded finite quotient of
positive length \(n\). In \(S=k[x_0,x_1,x_2,x_3]\), put

\[
K=\ker\bigl(S\to B[s,t]\bigr),\qquad
x\longmapsto(s^4,s^3t,ust^3,vt^4),\quad Z_B=\operatorname{Proj}(S/K).
\]

Let \(a,b\) be any prescribed positive integers. All equation spaces below
are actual homogeneous spaces in \(S\), without extending coefficients to
\(k(C_0)\) or passing to a finite normal jet.

## Statement

For \(d\ge0\) and integer \(w\), let

\[
E_{d,w}=\{e\in\mathbf Z_{\ge0}^4:|e|=d,
\ e_1+3e_2+4e_3=w\},
\quad \psi_{d,w}:k^{E_{d,w}}\to B,
\quad (c_e)\mapsto\sum_e c_eu^{e_2}v^{e_3}.
\]

Identifying \(k^{E_{d,w}}\) with the span of those monomials in \(S_d\),

\[
K_d=\bigoplus_{w=0}^{4d}\ker\psi_{d,w},\qquad
\dim_k(S/K)_d=\sum_{w=0}^{4d}\dim_k\operatorname{im}\psi_{d,w}.
\]

The exact prescribed-degree criterion is

\[
Z_B\text{ is a scheme CI of type }(a,b)
\iff ab=4n\text{ and }\exists F\in K_a,\ G\in K_b
\text{ with }\gcd(F,G)=1.
\]

In the affirmative case \(K=(F,G)\) as saturated homogeneous ideals, and
the endpoint defects of R-0052 necessarily satisfy

\[
\delta_0+\delta_\infty=n(2a+2b-7).
\]

## Evidence

[The complete proof](../arguments/torus_embedded_quotients.md#actual-equations-and-the-ci-criterion)
uses distinct binary monomials for distinct integer weights and applies
the [pure-curve degree-exhaustion lemma](pure_curve_degree_exhaustion.md).
The source is [the projective equation criterion](../synthesis/toric_quotients_and_endpoint_descent.md#when-does-the-compactified-family-have-two-global-equations).
No finite computation is necessary to establish the criterion.

## Limitations

The finite coefficient construction supplies full source spaces, but does
not itself find a gcd-one pair. Two independent sections, the equality
\(ab=4n\), or the displayed defect budget alone do not imply the criterion's
existence clause. The genus identity is necessary only; it is not a
sufficiency assertion for ACMness, Gorensteinness or two generators.
The test applies to this constant embedded quotient, not to every moving
supported intersection or every full torus-limit ideal.

## Review

The source has a separate review of its proper-pair and equation-space arguments; that review is distinct from the reconstruction decision recorded here.

Independent reconstruction review, 2026-11-04: reviewer
pilot_review_hilbert accepted the exact R-0053 route after reconstructing
the actual coefficient kernels in every characteristic, the gcd-one
regular-sequence condition, and the degree-exhaustion argument with its
finite-support kernel eliminated by purity. The necessary endpoint budget
and its nonsufficiency were checked. No blocker was found within the
specified constant-quotient scope. The reconstruction review accepts this route within its stated scope. The criterion itself does not complete the proper-pair search.
