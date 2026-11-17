# Quadric restriction, residual geometry, and contact rigidity

**Status:** Framework synthesis and bounded proof-replacement question. The contact vanishing below retains its existing computational proof.

## Degree-independent support obstruction

For the fixed rational quartic \(C\subset\mathbf P^3\), let \(Q=V(q)\simeq\mathbf P^1\times\mathbf P^1\) be its unique smooth quadric, with \(C\sim(1,3)\). If \(F\in I_C(d)\) is not divisible by \(q\), its divisor on \(Q\) satisfies
\[
\operatorname{div}_Q(F)=aC+R_Q,\qquad R_Q\sim(d-a,d-3a).
\]
Here \(a\ge1\), \(3a\le d\), and \(R_Q\ne0\): no positive diagonal class \((d,d)\) is a multiple of \((1,3)\). If a proper pair contains a member \(G=qP\), every component of \(R_Q\) belongs to \(V(F,G)\), so the pair cannot have sole support \(C\). This uses standard divisor theory on \(Q\), with **no ADE hypothesis and no degree restriction**. It does not give a sharp transverse multiplicity bound.

For equal-degree pencils, dependent restrictions of the two equations to \(Q\) mean precisely that some nonzero pencil member is divisible by \(q\). Thus **independent restrictions to \(Q\) are necessary for sole support**, but are not sufficient.

## Geometric meaning of the sharp sextic computation

Fix one of the three surviving primitive triples \(T_3\) in the [ADE sextic argument](../../arguments/carriers/sextic_ade_reduction.md#sharp-length-five-for-pencils-with-a-quadric-divisible-member), and set
\[
W=H^0(\mathbf P^3,\mathcal I_{T_3}(4)),\qquad
V=H^0(\mathbf P^3,\mathcal I_{T_3}(6)).
\]
The established dimensions are \(\dim W=2\) and \(\dim V=27\). Every nonzero \(P\in W\) is integral and generically smooth along \(C\). The verified fourth-coefficient calculation is equivalent to the **uniform kernel description**
\[
\{F\in V:\operatorname{ord}_C(F|_P)\ge5\}
=P\cdot H^0(\mathbf P^3,\mathcal O(2)).\tag{*}
\]
Order means vanishing at the generic point of \(C\) inside \(P\). The right side has dimension ten. Thus excessive contact forces \(P\) to be a component of \(F\); this is the geometric content of the rank-17 certificate, **not yet a calculation-free proof**.

For a proper pencil with first-order member \(F\) and member \(qP\), the established local identity
\[
m_C(F,qP)=1+\operatorname{ord}_C(F|_P)
\]
and (*) give the sharp bound \(m_C\le5\), residual degree at least \(36-4\cdot5=16\). The ADE hypothesis enters the reduction of hypothetical supported sextic pairs to these triples, not the general support obstruction.

## Intrinsic vanishing as a proof-replacement target

For each integral quartic \(P\in\mathbf P(W)\), let \(\mathcal I_{C/P}^{(5)}\) be the symbolic fifth power of the height-one prime of \(C\) on \(P\), defined by generic order-five vanishing. The proposed intrinsic statement is
\[
H^0(P,\mathcal I_{C/P}^{(5)}(6))=0.\tag{**}
\]
The restriction sequence
\[
0\to\mathcal O_{\mathbf P^3}(2)\xrightarrow{\cdot P}
\mathcal O_{\mathbf P^3}(6)\to\mathcal O_P(6)\to0
\]
has surjective global restriction, since \(H^1(\mathbf P^3,\mathcal O(2))=0\). In the specific triple setting, a lift with generic order-five vanishing on \(P\) contains \(T_3\) generically and therefore globally by purity. Hence (**) and (*) are equivalent. This equivalence does not independently prove the vanishing.

Do **not** replace the symbolic power by an invertible ideal \(\mathcal O_P(-5C)\) without checking Cartier and normality hypotheses. Singularities, normalization, conductor and possible exceptional divisors matter.

## Residual quartics as geometric input

For independent \(P,P'\in W\), the established generic order-three contact gives
\[
[P\cap P']=3[C]+[D],\qquad \deg D=16-3\cdot4=4.
\]
Likewise the generic multiplicity of \(P\cap Q\) along \(C\) is one:
\[
[P\cap Q]=[C]+[E],\qquad \deg E=8-4=4.
\]
These are cycle equalities; they do not assert that \(D,E\) are reduced, integral or disjoint from \(C\). The sharpness construction \(F=x_0^2P+qP'\), \(G=qP\) achieves \(m_C=5\), but does not prove the upper bound.

**Bounded geometric test:** describe the residual quartics and a normalization or common resolution of the quartic pencil, then determine whether divisor theory or the conormal filtration proves (**) uniformly, including exceptional parameters. Alternatively formulate the fourth-contact map over \(\mathbf P(W)\), quotient its kernel candidate by quadratic multiples of the universal quartic, and prove fiberwise injectivity. Expected codimension or generic injectivity alone is insufficient. If neither route works, record the precise global lifting obstruction; do not launch a new enumeration of quartic cases.

## General lessons and limits

- Separate Picard-class **support obstructions** from transverse **multiplicity bounds**.
- Prefer a geometric description of a computed kernel to an unexplained rank.
- Keep the distinction between formal contact and sections of **actual homogeneous equations**.
- Check all special carrier parameters before claiming a uniform theorem.
- Auxiliary-surface restriction may generalize, but no degree-independent STCI obstruction follows yet.
- Independent quadric restrictions and non-ADE carriers remain open.

**Proof owner:** [ADE sextic reduction](../../arguments/carriers/sextic_ade_reduction.md#sharp-length-five-for-pencils-with-a-quadric-divisible-member). **Related:** [formal equation-source gap](../formal-normal-geometry/filtered_equation_module_and_sextic_obstruction.md#the-gap-between-embedded-multiple-curves-and-global-hypersurfaces), [carrier cases](../carrier-normalization/open_carrier_cases.md#higher-contact-in-the-ade-66-triple-orbits).
