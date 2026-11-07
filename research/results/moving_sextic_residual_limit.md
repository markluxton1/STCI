---
id: STCI-R-0048
type: result
title: Endpoint-avoiding residual curves with a full boundary limit
scope: "#scope"
statement: "#statement"
proofs:
  - name: quadric divisors and flat complete-intersection family
    at: "research/arguments/torus_sextic_residuals.md#moving-residual-curves-and-their-full-limit"
    using: [STCI-R-0044]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Endpoint-avoiding residual curves with a full boundary limit

## Scope

Let \(k\) be algebraically closed of any characteristic and
\(C=[s^4:s^3t:st^3:t^4]\). Set \(q=x_0x_3-x_1x_2\), and identify the
smooth quadric \(Q=V(q)\) with \(\mathbf P^1\times\mathbf P^1\) by
\(x=(ac,ad,bc,bd)\). Put \(D=bc^3-ad^3\), so \(C=V_Q(D)\). Use
integer weights \((0,1,3,4)\) and the maximal-weight initial convention.
Write \(L_{ij}\) for coordinate lines and \(p_0,p_\infty\) for the
two endpoints of \(C\).

## Statement

Define

\[
r_{\mathrm{lo}}=x_0^3x_2-x_0x_1^3,\quad
r_{\mathrm{hi}}=x_2^3x_3-x_1x_3^3,\quad
G=(x_0+x_3)^2(r_{\mathrm{lo}}+r_{\mathrm{hi}}),\quad F=q^3+G.
\]

The pair is proper, with ideal \((F,G)=(q^3,G)\) and cycle

\[
3[C]+3[H]+6[K],\qquad
H=V_Q(a^3c+b^3d),\quad K=V_Q(ac+bd).
\]

The curves \(H,K\) are smooth rational curves of degrees four and two,
and both avoid \(p_0,p_\infty\). In characteristic zero their attachments
to \(C\) are the reduced, disjoint divisors \(s^{10}+t^{10}=0\) and
\(s^4+t^4=0\). At either endpoint the intersection is locally a pure
triple structure on \(C\), with local normal-coordinate presentation
\((q^3,D)\).

Its full saturated torus family is

\[
\bigl(q^3,(x_3+h^4x_0)^2
(r_{\mathrm{hi}}+h^{10}r_{\mathrm{lo}})\bigr).
\]

All fibers are proper sextic complete intersections; the family is
flat and \(h\)-saturated. The special ideal is exactly

\[
(q^3,x_3^3(x_2^3-x_1x_3^2))
\]

and its cycle is \(3[C]+15[L_{01}]+9[L_{02}]\). The Hilbert series is
\((1-z^6)^2/(1-z)^4\) throughout. The maximal-weight forms of the
original chosen \(F,G\) coincide; their difference supplies the
additional degree-six initial generator \(q^3\).

## Proof

The [complete divisor and family proof](../arguments/torus_sextic_residuals.md#moving-residual-curves-and-their-full-limit)
proves smoothness by graph projections, computes divisors on \(Q\), uses
R-0044 for scheme multiplicities, and proves flatness and both parameter
and irrelevant saturation by the regular-sequence argument.

## Evidence

Reconstructed from §§3–3.1 of
[sextic residuals](../synthesis/toric_sextic_residuals_and_limits.md).
Explicit substitutions certify the divisor factorizations.

## Limitations

Reduced disjoint attachment is asserted only in characteristic zero.
These are residual intersections, not sole-supported schemes.
Point attraction does not compute the displayed curve limit, and the
example gives no classification of moving residual curves.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
accepted this route on November 4, 2026. The reviewer reconstructed smoothness of the graphs, divisor
multiplicities, endpoint behavior, attachment qualification, and full-family
flatness and saturation. A separate sparse-polynomial implementation over
the integers checked the moving and special divisor factorizations.
The argument is a geometric reduction with necessary exact identities,
and its characteristic-zero attachment qualification remains explicit.
Acceptance concerns this residual family, not sole-supported intersections.

Independent reconstruction review accepts this route within its stated scope.
