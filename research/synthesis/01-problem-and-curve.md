# 1. The problem and fixed curve

Let \(k\) be algebraically closed of characteristic zero and let
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3_k.
\]
We seek homogeneous forms \(F,G\) such that \(V_+(F,G)_{\mathrm{red}}=C_0\). We may study integral factors separately, but must preserve the factor-reduction hypotheses when doing so.

The curve has degree four, genus zero, and unique smooth containing quadric \(Q=V(x_0x_3-x_1x_2)\). Its normal bundle is \(\mathcal O_{\mathbf P^1}(7)^{\oplus2}\). These are fixed inputs, not calculations to redo.

For a proper intersection of degrees \(d,e\) supported set-theoretically on \(C_0\), Bézout gives generic intersection length \(de/4\). More generally, when other curves occur, the cycle is \([V(F,G)]=m[C_0]+R\) and \(de=4m+\deg R\); thus \(m\) need not equal \(de/4\). If \(r,s\) are generic normal orders, their initial forms govern the first blowup but **do not in general determine** the full intersection multiplicity. See [Chapter 2](02-two-surfaces.md) and [residual intersections](residual_intersections_and_jets.md).

**Established boundary:** integral quartic carriers have no mate in characteristic zero, [STCI-R-0001](../results/quartic_carrier_exclusion.md). Together with separately audited lower-degree and factor arguments, hypothetical defining degrees are at least five. The unrestricted STCI question is still open.


## Intrinsic contact geometry and marked duality

The curve's special parametrization supplies more than its degree, quadric and normal bundle. The two endpoints are distinguished by fourth-order contact. The osculating-plane correspondence and its paired secants organize how the curve meets the ruled cubic and its dual. These geometric structures provide possible loci where global equations acquire exceptional jets, but do not by themselves constrain the full defining ideal of a pair.

The canonical [flag-incidence theorem R-0026](../results/quartic_flag_conormal_geometry.md) identifies a smooth complete flag surface for the marked pairing. Addition of effective degree-two divisors is finite flat of degree six, including a single length-six fiber at a quadruple root. Its swap fixed locus is a smooth conic in characteristic zero and a doubled line in characteristic two; the ambient flag remains smooth. The conormal normalization is C times C, while the degree-three unordered partition quotient is a *different* construction. The diagonal and involution graph meet at the two endpoints; third- and fourth-contact schemes carry additional endpoint multiplicities.

The [dual singular-scheme theorem R-0027](../results/quartic_dual_singular_scheme.md) refines the familiar osculating and bitangent strata. For the specified dual discriminant, its saturated Jacobian scheme has degree sixteen, four minimal associated primes, and two embedded endpoint primes of length one each. The distinction between the unmixed singular cycle and the endpoint corrections matters: reduced singular support alone loses scheme-theoretic information.

The [ruled projection theorem R-0028](../results/quartic_ruled_projection_geometry.md) compares a cone's finite normalization with its F4 resolution and a projected cubic's F1 normalization with its doubled conductor line. These are distinct geometric operations, and the prescribed scroll/cone intersection has two embedded endpoint corrections. The [arithmetic ruled model R-0029](../results/quartic_arithmetic_ruled_models.md) further shows that finite-flat four-section specialization and normalization of the special fiber need not commute.

All these results concern specified marked constructions. They form a coherent geometric toolkit, not an unrestricted classification of quartic carriers or an STCI obstruction. In particular, one cannot infer that a candidate defining pair has a singular point on C merely because the dual or projected model has marked singular strata.

Next: [simultaneous surface geometry](02-two-surfaces.md).
