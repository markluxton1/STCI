---
id: STCI-R-0043
type: result
title: Sharp quotient length eight for proper sextic eigenpairs
status: provisional
scope: "#scope"
statement: "#statement"
proofs:
  - name: fixed-point incidence and degree exhaustion
    at: "research/arguments/torus_sextic_residuals.md#the-sharp-sextic-eigenpair-bound"
    using: [STCI-R-0047, STCI-R-0050]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Sharp quotient length eight for proper sextic eigenpairs

## Scope

Let \(k\) be algebraically closed of any characteristic. Let \(F,G\) be
ordinary homogeneous sextics in \(k[x_0,x_1,x_2,x_3]\), each an eigenform
for the integer weights \((0,1,3,4)\), with no common factor.
Containing \(C=[s^4:s^3t:st^3:t^4]\) is not required. On the dense
coordinate torus write \(x=(1,t,t^3u,t^4v)\), \(F=t^rf(u,v)\),
\(G=t^sg(u,v)\), and

\[
B=k[u^{\pm1},v^{\pm1}]/(f,g),\qquad n=\dim_kB.
\]

## Statement

The algebra \(B\) is finite dimensional, possibly zero, and

\[
n\le8.
\]

The fundamental cycle of components meeting the dense torus has degree
\(4n\), and the cycle lying entirely in the coordinate boundary has degree

\[
36-4n\ge4.
\]

The bound is sharp in every characteristic, attained by

\[
(x_1^6-x_0^4x_2^2,\ x_2^6-x_1^2x_3^4),
\]

whose finite quotient is
\(k[u^{\pm1},v^{\pm1}]/(u^2-1,v^4-1)\) of length eight.

## Proof

The [complete incidence proof](../arguments/torus_sextic_residuals.md#the-sharp-sextic-eigenpair-bound)
uses the quartic orbit-degree and multiplicity statement R-0050.
If nine quotient lengths exhausted all degree, purity would force the
intersection to miss \(e_1,e_2\). The resulting pure-power terms force
weights six and eighteen, which force the additional line \(L_{03}\).
R-0047 and the same Argument's eigenpair controls verify attainment.

## Evidence

Reconstructed from §2 and the explicit §1.1 example in
[sextic residuals](../synthesis/toric_sextic_residuals_and_limits.md).
The proof is an all-characteristic incidence argument.

## Limitations

This is a bound for actual pairs of eigenforms, not arbitrary
mixed-weight sextics, all invariant ideals, or full limits with more than
two generators. It does not classify boundary schemes or exclude all
sole-supported sextic complete intersections.

## Review

Independent reconstruction by the nonauthor reviewer pilot_review_sextic
accepted this route on November 4, 2026. The reviewer checked orbit multiplicities, purity in the
degree-exhaustion case, fixed-point incidence, integer-character reasoning
in every characteristic, and sharp attainment. The sharp-example premise
R-0047 is explicitly declared following review. Acceptance concerns proper
eigenpairs only, without extending to arbitrary mixed-weight pairs.

The Result remains provisional; independent acceptance of this
reconstructed route does not promote its status or the source's labels.
