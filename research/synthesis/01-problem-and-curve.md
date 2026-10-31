# 1. The problem and fixed curve

Let \(k\) be algebraically closed of characteristic zero and let
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3_k.
\]
We seek homogeneous forms \(F,G\) such that \(V_+(F,G)_{\mathrm{red}}=C_0\). We may study integral factors separately, but must preserve the factor-reduction hypotheses when doing so.

The curve has degree four, genus zero, and unique smooth containing quadric \(Q=V(x_0x_3-x_1x_2)\). Its normal bundle is \(\mathcal O_{\mathbf P^1}(7)^{\oplus2}\). These are fixed inputs, not calculations to redo.

For a proper intersection of degrees \(d,e\) supported set-theoretically on \(C_0\), Bézout gives generic intersection length \(de/4\). More generally, when other curves occur, the cycle is \([V(F,G)]=m[C_0]+R\) and \(de=4m+\deg R\); thus \(m\) need not equal \(de/4\). If \(r,s\) are generic normal orders, their initial forms govern the first blowup but **do not in general determine** the full intersection multiplicity. See [Chapter 2](02-two-surfaces.md) and [residual intersections](residual_intersections_and_jets.md).

**Established boundary:** integral quartic carriers have no mate in characteristic zero, [STCI-R-0001](../results/quartic_carrier_exclusion.md). Together with separately audited lower-degree and factor arguments, hypothetical defining degrees are at least five. The unrestricted STCI question is still open.


## 1.1 Intrinsic contact geometry and marked duality

The curve's special parametrization supplies more than its degree, quadric and normal bundle. The two endpoints are distinguished by fourth-order contact. The osculating-plane correspondence and its paired secants organize how the curve meets the ruled cubic and its dual. These geometric structures provide possible loci where global equations acquire exceptional jets, but do not by themselves constrain the full defining ideal of a pair.

The canonical [flag-incidence theorem R-0026](../results/quartic_flag_conormal_geometry.md) identifies a smooth complete flag surface for the marked pairing. Addition of effective degree-two divisors is finite flat of degree six, including a single length-six fiber at a quadruple root. Its swap fixed locus is a smooth conic in characteristic zero and a doubled line in characteristic two; the ambient flag remains smooth. The conormal normalization is C times C, while the degree-three unordered partition quotient is a *different* construction. The diagonal and involution graph meet at the two endpoints; third- and fourth-contact schemes carry additional endpoint multiplicities.

The [dual singular-scheme theorem R-0027](../results/quartic_dual_singular_scheme.md) refines the familiar osculating and bitangent strata. For the specified dual discriminant, its saturated Jacobian scheme has degree sixteen, four minimal associated primes, and two embedded endpoint primes of length one each. The distinction between the unmixed singular cycle and the endpoint corrections matters: reduced singular support alone loses scheme-theoretic information.

The [ruled projection theorem R-0028](../results/quartic_ruled_projection_geometry.md) compares a cone's finite normalization with its F4 resolution and a projected cubic's F1 normalization with its doubled conductor line. These are distinct geometric operations, and the prescribed scroll/cone intersection has two embedded endpoint corrections. The [arithmetic ruled model R-0029](../results/quartic_arithmetic_ruled_models.md) further shows that finite-flat four-section specialization and normalization of the special fiber need not commute.

All these results concern specified marked constructions. They form a coherent geometric toolkit, not an unrestricted classification of quartic carriers or an STCI obstruction. In particular, one cannot infer that a candidate defining pair has a singular point on C merely because the dual or projected model has marked singular strata.


## 1.2 Three different incidence spaces and their markings

The following distinctions prevent recurring false identifications in the historical geometry discussions. Work in characteristic zero unless stated otherwise.

**The containing quadric.** The smooth quadric \(Q=V(x_0x_3-x_1x_2)\) is abstractly \(\mathbf P^1\times\mathbf P^1\), and \(C\) has bidegree \((1,3)\) (up to swapping rulings). For the ruling in which \(C\) is a section, \(C^2=6\).

**The conormal incidence surface.** Let \(\mathcal N=\{(p,H):p\in C,\ T_pC\subset H\}\). This is a \(\mathbf P^1\)-bundle over \(C\), abstractly \(\mathbf P^1\times\mathbf P^1\) in characteristic zero because the normal bundle is balanced. It parametrizes tangent planes *with a marked contact point*, not points of \(Q\). The section \(p\mapsto(p,T_pQ)\) has self-intersection \(2\), not \(6\). Consequently there is no isomorphism over \(C\) taking this distinguished section to the section \(C\subset Q\). Abstract isomorphism of the underlying products is not an identification of marked ruled surfaces.

**The secant-plane flag space.** A length-two divisor \(D\in\operatorname{Sym}^2 C\simeq\mathbf P^2\), together with a plane containing its secant (or tangent) line, gives a three-dimensional incidence space. The residual degree-two divisor in the plane section yields a second symmetric-square coordinate. The residual-swap involution and its fixed conic belong to this threefold, not to the two-dimensional conormal incidence surface. The precise flag and finite-flat assertions are in [R-0026](../results/quartic_flag_conormal_geometry.md).

These distinctions also explain why polarity on \(Q\) does not provide a canonical marked identification \(\mathcal N\simeq Q\): the polar line of a tangent line is not generally a ruling of \(Q\). See the preserved calculations in [quartic projection and special geometry](../supplements/QUARTIC_PROJECTION_AND_SPECIAL_GEOMETRY.md) and [quartic duality and flags](../supplements/QUARTIC_DUAL_FLAGS_AND_BITANGENTS.md). The comparison is geometric background, **not** a theorem about arbitrary defining surface pairs.

## 1.2A Marked contact cycles and what they count

The osculating-plane family has contact divisor \(3\Delta+\Gamma_\iota\) on \(C\times C\), where \(\iota(u)=-u\). The bitangent family has contact divisor \(2\Gamma_{c_+}+2\Gamma_{c_-}\), with the two ratio correspondences given in characteristic zero by \(c_\pm=-2\pm\sqrt3\). These are universal **marked plane-section cycles**, not zero schemes of arbitrary defining equations. At the two fixed points of \(\iota\), the osculating plane has fourth-order rather than separated triple-plus-simple contact.

The distinction matters for global intersection arguments: multiplying the universal plane contact divisor by the degree of a chosen plane family is legitimate only after that family and its pullback multiplicities have been specified. It does not turn the two marked endpoints into compulsory singularities of both carriers. The flag and dual records [R-0026](../results/quartic_flag_conormal_geometry.md) and [R-0027](../results/quartic_dual_singular_scheme.md) retain the nonreduced contact and embedded endpoint structure; [Chapter 4](04-carriers.md) explains the additional conductor conditions required to descend a divisor from a carrier normalization.

## 1.3 Dual invariants and the scheme-theoretic intersection

Write dual coordinates \([A:B:C:D]\) for the plane whose restriction to the parametrized curve is \(As^4+Bs^3t+Cst^3+Dt^4\). Put
\[
M=AD-BC,\qquad L=BC-4AD,\qquad K=AC^2+B^2D.
\]
The dual quadric is \(Q^\vee=V(M)\), while the dual of the ruled cubic \(R=V(x_0x_2^2-x_1^2x_3)\) is \(R^\vee=V(K)\). For the binary-quartic discriminant \(\Delta\) of this restricted four-term system, the exact identity is
\[
\Delta=-4L^3-27K^2.
\]
Thus the **scheme-theoretic** intersection is
\[
C^\vee\cap R^\vee=V(K,L^3),
\]
not merely the support \(V(K,L)\) and not the ambient ideal cube \((K,L)^3\). The reduced support \(V(K,L)\) consists of the osculating quartic and the two endpoint pencil lines; the triple Cartier structure retains endpoint contact information. This identity alone does not determine the full singular scheme of the dual discriminant: see [R-0027](../results/quartic_dual_singular_scheme.md).

