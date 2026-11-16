---
id: STCI-R-0047
type: result
title: Eigenpair controls with inseparable quotients and boundary lines
scope: "#scope"
statement: "#statement"
proofs:
  - name: torus quotient and local boundary multiplicities
    at: "research/arguments/torus_sextic_residuals.md#eigenpair-residual-controls"
    using: [STCI-R-0044, STCI-R-0050]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Eigenpair controls with inseparable quotients and boundary lines

## Scope

Let \(k\) be algebraically closed of any characteristic,
\(C=[s^4:s^3t:st^3:t^4]\), and \(L_{ij}\) the coordinate lines.
Use \(x=(1,t,t^3u,t^4v)\) on the dense coordinate torus and the integer
weights \((0,1,3,4)\). Let
\(C_{\epsilon,\zeta}=[s^4:s^3t:\epsilon st^3:\zeta t^4]\),
\(q=x_0x_3-x_1x_2\), \(A=x_0^2x_2-x_1^3\).
Every ideal below is an actual proper sextic complete intersection.

## Statement

For

\[
I_8=(x_1^6-x_0^4x_2^2,\ x_2^6-x_1^2x_3^4),
\]

the finite quotient is \(B_8=k[u^{\pm1},v^{\pm1}]/(u^2-1,v^4-1)\)
of length eight. Its only boundary curve is \(L_{03}\), with primary
component exactly \((x_1^2,x_2^2)\) and multiplicity four. Outside
characteristic two, its cycle consists of the eight simple quartics
\(C_{\epsilon,\zeta}\), \(\epsilon^2=1,\zeta^4=1\), plus \(4[L_{03}]\).
In characteristic two its quotient is the noncurvilinear algebra
\(k[\alpha,\beta]/(\alpha^2,\beta^4)\), supported at \((1,1)\), and its
cycle is \(8[C]+4[L_{03}]\).

For

\[
I_6=((x_0x_3)^3-(x_1x_2)^3,\ x_1^6-x_0^4x_2^2),
\]

the finite quotient is
\(B_6=k[u^{\pm1},v^{\pm1}]/(u^2-1,v^3-u^3)\), of length six.
Its only boundary curve is \(L_{23}\), with multiplicity twelve.
The torus cycle is six simple quartics
\(C_{\epsilon,\epsilon\omega}\) if the characteristic is neither two
nor three; two triple quartics \(C_{1,1},C_{-1,-1}\) in characteristic
three; or three double quartics \(C_{1,\omega}\), \(\omega^3=1\),
in characteristic two. In each case add \(12[L_{23}]\).

Exact endpoint chart ideals, using \(x_0=1,(t,y,z)=(x_1,x_2,x_3)\)
and \(x_3=1,(a,b,c)=(x_0,x_1,x_2)\), are respectively

\[
I_8:\quad (y^2-t^6,t^2(t^{16}-z^4)),\qquad
(b^2-c^6,c^2(c^{16}-a^4)),
\]

\[
I_6:\quad (z^3-t^3y^3,t^6-y^2),\qquad
(a^3-b^3c^3,b^6-a^4c^2).
\]

Finally \(I_{\mathrm{th}}=(q^3,A^2)\) has finite quotient

\[
k[u^{\pm1},v^{\pm1}]/((v-u)^3,(u-1)^2),
\]

which is local of length six and embedding dimension two in every
characteristic; its projective cycle is \(6[C]+12[L_{23}]\).
None of these complete intersections has an embedded associated
component. As invariant ideals their full torus limits are themselves.

## Proof

The [complete control proofs](../arguments/torus_sextic_residuals.md#eigenpair-residual-controls)
give every quotient, the coordinate-boundary support, the exact local
lengths and primary contraction, the characteristic-dependent Artin
factors, and the endpoint equations. For \(I_{\mathrm{th}}\), a divisor
calculation on the smooth Segre quadric and R-0044 prove the cycle.

## Evidence

These are the three examples in §§1.1–1.3 of
[sextic residuals](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_sextic_residuals_and_limits.md).
The global equations and local algebra proofs specify their full scope.

## Limitations

The examples demonstrate collisions, noncurvilinearity and residual
boundary support. They do not classify invariant ideals, finite algebras,
or arbitrary sextic pairs. The length-six local quotient has residual
support and contradicts no sole-support curvilinearity theorem. Equal
quotient lengths or fundamental cycles do not identify endpoint schemes.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
accepted this route on November 4, 2026. The reviewer reconstructed the finite quotient factors and
characteristic collisions, boundary support, local lengths four and
twelve, primary contraction, endpoint equations, and noncurvilinear
quadric-divisor control. The source's distinct examples and qualifications
are preserved. Acceptance does not classify all finite algebras or
invariant ideals.

Independent reconstruction review accepts this route within its stated scope.
