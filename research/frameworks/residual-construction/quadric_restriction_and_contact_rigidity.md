# Quadric restriction, residual geometry, and contact rigidity

**Status:** geometric synthesis and bounded proof-replacement question; not a new STCI exclusion beyond the cited Arguments.

## A support obstruction independent of the ADE reduction

Let \(C=C_0\subset\mathbf P^3\) be the fixed rational quartic and \(Q=V\(q\)\simeq\mathbf P^1\times\mathbf P^1\) its unique containing quadric. Fix the ruling convention \(C\sim(1,3)\). If \(F\in I_C(d)\) is not divisible by \(q\), then the effective divisor \(F|_Q\) has class \((d,d)\). Writing
\[
\operatorname{div}_Q(F)=aC+R_Q,\qquad R_Q\sim(d-a,d-3a),
\]
gives \(a\ge1\), \(3a\le d\), and \(R_Q\ne0\). Indeed, the class \((d,d)\) is never a positive multiple of \((1,3)\).

Thus if a **proper** pair \(F,G\) has a member \(G=qP\), the nonzero residual divisor (R_Q\subset V\(F,G\)) lies outside \(C\). This excludes sole support for **any degrees** and requires neither ADE singularities nor a primitive-triple classification. It does **not** bound the generic transverse intersection length sharply. It is the standard divisor-class argument on the smooth quadric, not a new theorem of intersection theory.

For a pencil of equal-degree equations, the condition that their restrictions to \(Q\) are dependent is equivalent to the existence of a nonzero quadric-divisible member. Therefore independent restrictions to \(Q\) are necessary for any proper sole-support pencil. This necessary condition is not sufficient.

## What the ADE sextic computation adds

Under the hypotheses of the [ADE sextic argument](../../arguments/carriers/sextic_ade_reduction.md#sharp-length-five-for-pencils-with-a-quadric-divisible-member), fix one of the three surviving primitive triples \(T_3\). Put
\[
W=H^0\(mathbf P^3,\mathcal I_{T_3}(4)),\qquad
V=H^0\(mathbf P^3,\mathcal I_{T_3}(6)).
\]
The verified source calculation gives \(dim W=2) and \(dim V=27). Each nonzero \(P\in W\) is integral and generically smooth along \(C\). The exact fourth-coefficient computation proves the **uniform kernel statement**
\[
\{F\in V:\operatorname{ord}_{C}(F|_{P})\ge5\}
=P\,H^0\(mathbf P^3,\mathcal O(2)).
\tag{*}
\]
Here order is taken at the generic point of \(C\) on \(P\). The right side has dimension ten. This is the geometric meaning of the rank-17 calculation: excessive contact forces the quartic carrier to be a component of the sextic. The existing finite-field/minor certificate remains the proof of (*); the present note does not replace it.

For a proper pencil with a first-order member and a quadric-divisible member (qP), the local intersection identity
\[
m_C(F,qP)=1+\operatorname{ord}_{C}(F|_P)
\]
then gives \(m_C\le5\), sharply, hence residual degree at least (36-4\cdot5=16). The ADE hypothesis is needed to reduce a hypothetical supported sextic pair to these triples, **not** for the general support obstruction above.

## Intrinsic proof target

For an integral quartic (P\in\mathbf P(W)), define \(mathcal I_{C/P}^{(5)}) by order at least five along the generic point of \(C\) (symbolic power of its height-one prime ideal). The intrinsic version of (*) is
\[
H^0\bigl(P,\mathcal I_{C/P}^{(5)}(6)\bigr)=0.\tag{**}
\]
The standard hypersurface restriction sequence
\[
0\to\mathcal O_{\mathbf P^3}(2)\xrightarrow{\cdot P}
\mathcal O_{\mathbf P^3}(6)\to\mathcal O_P(6)\to0
\]
and (H^1\(mathbf P^3,\mathcal O(2))=0) identify (**) with (*): every restricted section lifts, and a lift with order-five vanishing on \(P\) contains the generically defined triple (T_3\subset P), hence globally by purity. This equivalence uses the specific embedded triple and its generic local description. The **vanishing itself is still computationally proved**.

Do not silently replace the symbolic power by an ordinary invertible ideal \(mathcal O_P(-5C)): \(P\) may be singular along points of \(C\), and \(C\) need not be Cartier everywhere on \(P\). Normalization, conductor, or a resolution may be necessary to make a divisor-class proof rigorous.

## Residual quartics and the proposed geometric mechanism

For independent (P,P'\in W), the established generic contact order three gives
\[
[P\cap P']=3[C]+[D],\qquad\deg D=16-12=4.
\]
Likewise, since \(q\) meets \(P\) with generic multiplicity one along \(C\),
\[
[P\cap Q]=[C]+[E],\qquad\deg E=8-4=4.
\]
These are cycle equalities, not assertions that (D,E) are reduced, integral, or disjoint from \(C\). Their divisor classes on a suitable model of \(P\) are candidates for explaining (**) without matrices. The sharpness construction \(F=x_0^2P+qP'\), \(G=qP\) realizes \(m_C=5\), but does not itself prove the upper bound.

**Bounded replacement test:** identify the base-locus residual \(D\), the quadric residual \(E\), and a suitable normalization/resolution for the *whole quartic pencil*; then decide whether divisor theory or the conormal filtration proves (**) uniformly over \(mathbf P(W)), including exceptional members. If it does not, isolate the exact global-section lifting obstruction rather than enumerating additional quartic parameter cases. The universal pencil offers a second formulation: after quotienting the contact-kernel bundle by the obvious ten-dimensional subbundle of quadratic multiples of the universal quartic, prove the induced map is fiberwise injective. Expected codimension alone does not prove emptiness of its degeneracy locus.

## Reusable lessons and boundaries

- Separate **residual support** (often a Picard-class obstruction) from **generic multiplicity** (a transverse-length problem).
- Interpret a computed matrix kernel geometrically before promoting its rank as a framework principle.
- Distinguish formal/symbolic contact along a carrier from sections lifted from **actual homogeneous equations**.
- Preserve uniformity over the carrier parameter space; generic calculations alone cannot exclude special members.
- For higher degrees, first test restrictions to geometrically controlled auxiliary surfaces. This is a method, **not** an established degree-independent obstruction.
- The independent-restriction sextic locus and all non-ADE carriers remain open. No new Investigation is warranted without a uniform geometric test and stopping criterion.

**Proof owner:** [ADE sextic reduction](../../arguments/carriers/sextic_ade_reduction.md#sharp-length-five-for-pencils-with-a-quadric-divisible-member). **Related interfaces:** [formal equation-source gap](../formal-normal-geometry/filtered_equation_module_and_sextic_obstruction.md#the-gap-between-embedded-multiple-curves-and-global-hypersurfaces), [carrier cases](../carrier-normalization/open_carrier_cases.md#higher-contact-in-the-ade-66-triple-orbits), [residual framework](index.md).
