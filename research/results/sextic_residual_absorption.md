---
id: STCI-R-0049
type: result
title: Residual multiplicity transfers onto the marked quartic in a flat family
scope: "#scope"
statement: "#statement"
proofs:
  - name: graph divisor specialization on the smooth quadric
    at: "research/arguments/torus_sextic_residuals.md#residual-absorption-in-a-proper-flat-family"
    using: [STCI-R-0044]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Residual multiplicity transfers onto the marked quartic in a flat family

## Scope

Let \(k\) be algebraically closed of any characteristic,
\(C=[s^4:s^3t:st^3:t^4]\),
\(q=x_0x_3-x_1x_2\), \(A=x_0^2x_2-x_1^3\), and
\(Q=V(q)\). In Segre coordinates \(x=(ac,ad,bc,bd)\), set
\(D=bc^3-ad^3\), so \(C=V_Q(D)\). The parameter is \(h\in\mathbf A^1_k\).

## Statement

The homogeneous family

\[
\mathcal K_h=(q^3,A(A+h^3x_0^3))
\]

is flat, \(h\)-saturated, and consists of saturated proper sextic complete
intersections. It is the full maximal-weight torus family of its fiber
at \(h=1\), for weights \((0,1,3,4)\). For every \(h\ne0\),
\(H_h=V_Q(D+h^3ac^3)\) is a smooth curve of type \((1,3)\), distinct
from \(C\), and

\[
[Z_h]=3[C]+3[H_h]+12[L_{23}],\qquad
[Z_0]=6[C]+12[L_{23}].
\]

The special ideal is exactly \((q^3,A^2)\). Hence the residual cycle
relative to \(C\) is \(3[H_h]+12[L_{23}]\) before specialization and
\(12[L_{23}]\) after specialization. Its specialization as a cycle
contains the additional \(3[C]\); extracting the residual cycle does
not commute with specialization.

## Proof

The [complete graph and flatness proof](../arguments/torus_sextic_residuals.md#residual-absorption-in-a-proper-flat-family)
uses \(A(A+h^3x_0^3)|_Q=a^4D(D+h^3ac^3)\), the graph's coefficient
pair with no common zero, and R-0044. Nonvanishing on \(Q\) proves
properness in every fiber, and the regular-sequence family proves flatness
and saturation.

## Evidence

Reconstructed from §3.2 of
[sextic residuals](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_sextic_residuals_and_limits.md).
No characteristic restriction is needed for the graph or multiplicities.

## Limitations

The twelvefold residual line remains. This gives neither an iteration
absorbing all residual support nor a supported complete intersection.
The assertion concerns this actual family, not all residual deformation
directions.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
accepted this route on November 4, 2026. The reviewer reconstructed properness and flatness of the full family,
smoothness of the moving graph, the generic and special divisor
multiplicities, and the precise failure of residual extraction to commute
with specialization. A separate sparse-polynomial implementation over
the integers checked the absorption factorization. The surviving
twelvefold line and lack of an iteration to sole support remain limitations.

Independent reconstruction review accepts this route within its stated scope.
