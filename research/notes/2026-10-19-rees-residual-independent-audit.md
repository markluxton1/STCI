# Independent audit: intrinsic Rees divisors and an unbounded first-relation defect

Date: 2026-10-19.

Reviewer: independent `audit_contact_budget` research agent.
Status: **independently reconstructed structural statements on the hypotheses below; not a promoted result**. No canonical result or question record is modified. The conclusions are limitations on proposed invariants, not an STCI exclusion.

## 1. Exact scope, dependencies, and outcome

The blowup statements concern a smooth integral threefold of finite type over a field, and a codimension-two complete-intersection subscheme whose reduced support is one integral curve. The Segre calculation specializes to two homogeneous surfaces in projective three-space with no common surface component. The degeneration family is an affine local model over the affine line; it makes no existence claim for a global homogeneous presentation of the fixed rational quartic.

The companion proposal audited here is [the full-ideal Rees investigation](2026-10-19-rees-residual-investigation.md). The relevant prior evidence is the [exceptional-cycle and vertical-family proposal](2026-10-19-exceptional-cycle-balance-and-vertical-counterexamples.md), especially its local family, and its [independent audit](2026-10-19-exceptional-cycle-and-vertical-family-independent-audit.md). Those records already establish the chosen-pair vertical degeneration. This audit does not repeat that multiplicity calculation or reopen the inherited entirely-thick numerical inequality. It reconstructs the intrinsic full-ideal blowup claims and adds the exact first-relation defect calculation.

The audit outcomes are:

1. Every exceptional prime divisor of the normalized blowup of the full complete-intersection ideal dominates the support curve. Localization at the generic point identifies these divisors with the divisorial Rees valuations of the generic transverse ideal.
2. The coefficients and finite degrees of these divisors satisfy an exact multiplicity identity, proved below.
3. The ordinary Segre class pushed to projective three-space is fixed by the two surface degrees.
4. In the displayed local family, the actual first degree-\(p\) relation has saturation defect of length \(N\). On the subsequence \(N=aL\), this grows without bound while the complete generic ideal, and hence its divisorial Rees data, is fixed up to an explicit filtration-preserving coordinate isomorphism.

The fourth item concerns the degree-\(p\) relation; it does not assume saturated first relations. No assertion is made that valuations are identical in an ambient ring with its coordinates fixed.

## 2. Normalized full-ideal blowup: no exceptional divisors over closed points

Let \(X\) be a smooth integral threefold of finite type over a field. Let \(I\subset\mathcal O_X\) define a codimension-two complete intersection \(Y\), and suppose \(Y_{\mathrm{red}}=C\) is one integral curve. Put

\[
b:B=\operatorname{Bl}_I X\longrightarrow X.
\]

The ideal \(I\mathcal O_B\) is invertible. Write \(I\mathcal O_B=\mathcal O_B(-E)\); its effective Cartier divisor is the scheme-theoretic inverse image of \(Y\). Since the immersion is regular,

\[
\operatorname{gr}_I\mathcal O_X
\simeq\operatorname{Sym}_{\mathcal O_Y}(I/I^2),
\qquad
E\simeq\operatorname{Proj}_Y
\operatorname{Sym}_{\mathcal O_Y}(I/I^2).
\tag{R1}
\]

The conormal bundle \(I/I^2\) has rank two over \(Y\). Thus \(E\to Y\) is a projective-line bundle, including its nonreduced base structure. Its reduction \(E_{\mathrm{red}}\to C\) is an irreducible ruled surface. In particular, the fiber of \(b\) over a closed point of \(C\) has dimension one. This assertion does not require the scheme \(Y\) to be reduced or normally flat relative to \(C\).

The scheme \(B\) is integral: locally its Rees algebra is a subring of the polynomial ring over the integral coordinate ring of \(X\). Its normalization

\[
\nu:\overline B\longrightarrow B
\]

is finite, because schemes of finite type over a field are excellent. Outside \(Y\), the map \(b\) is an isomorphism onto a smooth open subscheme, so normalization is an isomorphism there as well. Every prime divisor exceptional for \(b\nu\) is consequently contained in \(\nu^{-1}(E)\).

Let \(D\) be such a prime divisor. Since \(\nu\) is finite, its image has the same dimension as \(D\), namely two. Its image is contained in the irreducible surface \(E_{\mathrm{red}}\), so that image is all of \(E_{\mathrm{red}}\). Therefore

\[
\boxed{\text{every exceptional prime divisor of }\overline B\to X
\text{ dominates }C.}
\tag{R2}
\]

Equivalently, the inverse image of a closed point of \(C\), being finite over a one-dimensional fiber of \(B\), cannot contain a divisor of \(\overline B\). This conclusion concerns divisors of the normalized blowup of the full ideal. It does not forbid vertical curves in \(B\), singularities over special points, or vertical components in intersections of two individually transformed equations on another blowup.

If a proper complete intersection has several reduced curve components, the same reasoning component by component shows that each exceptional prime divisor dominates a curve component of the reduced center. There is still no exceptional prime divisor mapping to an isolated closed point.

## 3. Localization and the generic Rees valuations

Let \(\eta\) be the generic point of \(C\), let

\[
R=\mathcal O_{X,\eta},\qquad J=I R,\qquad
m=\operatorname{length}_R(R/J).
\]

The ring \(R\) is a two-dimensional regular local ring, and \(J\) is a parameter ideal primary to its maximal ideal. Formation of the Rees algebra and blowup commutes with localization. Normalization of a domain also commutes with localization. Consequently

\[
\overline B\times_X\operatorname{Spec}R
\simeq\operatorname{Nor}\bigl(\operatorname{Bl}_J\operatorname{Spec}R\bigr).
\tag{R3}
\]

Every global exceptional divisor from (R2) survives this localization, because its generic point maps to \(\eta\). Conversely, every exceptional prime divisor of the localized normalized blowup has a unique closure among the global exceptional prime divisors. One may see this directly as the localization bijection on primes above the generic point of \(E_{\mathrm{red}}\). Hence the exceptional prime divisors in (R2) are in bijection with the divisorial Rees valuations of \(J\).

This proves that their valuation-theoretic data come from the generic transverse ideal. It does not say that their global exceptional surfaces or the degeneration of those surfaces over closed points are determined by generic data.

## 4. Exact coefficient identity

Write

\[
\nu^*E=\sum_i a_iD_i,
\qquad
f_i=[k(D_i):k(E_{\mathrm{red}})].
\]

The integers \(a_i>0\) are the orders of the full ideal along the corresponding normalized exceptional divisors. By (R2), each map \(D_i\to E_{\mathrm{red}}\) is finite and dominant, so \(f_i\) is a positive finite integer.

The coefficient of the fundamental cycle of \(E\) along \(E_{\mathrm{red}}\) is exactly \(m\): by its projective-bundle description (R1), the local ring at the generic point is a polynomial-localization extension of the Artinian ring \(\mathcal O_{Y,\eta}\) with the same length. Thus

\[
[E]=m[E_{\mathrm{red}}].
\tag{R4}
\]

Since \(\nu\) is finite birational, \(\nu_*[\overline B]=[B]\). Applying the projection formula for the effective Cartier divisor \(E\) gives

\[
\nu_*\bigl(\nu^*E\cap[\overline B]\bigr)
=E\cap[B]=[E].
\]

Comparison of the coefficient of \(E_{\mathrm{red}}\) proves

\[
\boxed{\sum_i a_if_i=m.}
\tag{R5}
\]

For example, over an algebraically closed field, the parameter ideal \((u^a,v^b)\) has one primitive monomial Rees valuation with

\[
v(u)=b/g,\qquad v(v)=a/g,\qquad
a_1=ab/g,\qquad f_1=g,\quad g=\gcd(a,b).
\]

Its exceptional map has degree \(g\), given on the torus by a constant multiple of the \(g\)-th power map. Formula (R5) gives \(a_1f_1=ab\), its transverse complete-intersection length. This example illustrates why the coefficient identity alone permits arbitrarily large multiplicity.

## 5. Segre pushforward for two projective surfaces

Specialize to \(X=\mathbf P^3\), and let \(Y=V(F_d,G_e)\) be the proper scheme intersection of surfaces with no common surface component. It is a regular immersion, with

\[
N_{Y/\mathbf P^3}
\simeq\mathcal O_Y(d)\oplus\mathcal O_Y(e).
\]

For the inclusion \(i:Y\hookrightarrow\mathbf P^3\), the regular-immersion Segre formula gives

\[
s(Y,\mathbf P^3)
=c(N_{Y/\mathbf P^3})^{-1}\cap[Y].
\]

With \(H\) the hyperplane class and \(i_*[Y]=deH^2\), its pushforward is

\[
\boxed{i_*s(Y,\mathbf P^3)
=deH^2-de(d+e)H^3.}
\tag{R6}
\]

Higher terms vanish for dimension reasons. Thus the ordinary Segre numbers pushed to projective three-space are determined by \(d,e\). This computation does not provide a new numerical distinction among thickenings of fixed complete-intersection type. It makes no claim that all finer Segre constructions relative to the smooth reduced support, or normalization and conductor data, are redundant.

## 6. Exact first-relation kernel in the degeneration family

Let \(A=k[t]\), let \(S=A[u,v]\), and put \(\mathfrak q=(u,v)\). Fix

\[
p\ge2,\qquad a>p,\qquad b>p,\qquad N\ge1,
\]

and define

\[
J_N=(u^b,v^a+t^Nu^p),\qquad
B_N=S/J_N,\qquad M_N=\mathfrak q B_N.
\tag{R7}
\]

The original family is a complete intersection with radical \(\mathfrak q\). Indeed \(u^b\) is a nonzerodivisor in \(S\), and the second equation is monic in \(v\), hence is a nonzerodivisor modulo \(u^b\). Successive monic division gives the free \(A\)-basis

\[
u^iv^j,\qquad 0\le i<b,\quad0\le j<a.
\tag{R8}
\]

Thus the original family is finite flat of rank \(ab\). Nilpotence of \(u\), followed by the displayed relation for \(v^a\), gives its stated radical.

There are no relations below degree \(p\), because \(J_N\subset\mathfrak q^p\). The actual degree-\(p\) relation module is

\[
\mathcal R_p
=\ker\left(
\operatorname{Sym}_A^p(\mathfrak q/\mathfrak q^2)
\longrightarrow M_N^p/M_N^{p+1}
\right).
\tag{R9}
\]

Identify the source with \(\mathfrak q^p/\mathfrak q^{p+1}\). Since \(J_N\subset\mathfrak q^p\), its kernel is the image of \(J_N\) in this module. Both \(u^b\) and \(v^a\) vanish modulo \(\mathfrak q^{p+1}\), because \(a,b>p\). For an arbitrary coefficient \(h(t,u,v)\), only its degree-zero term \(h(t,0,0)\) can contribute to the degree-\(p\) image of \(h(t,u,v)t^Nu^p\); every other term belongs to \(\mathfrak q^{p+1}\). Consequently the whole image of the ideal, with all possible coefficient combinations included, is exactly

\[
\boxed{\mathcal R_p=A\,t^Nu^p.}
\tag{R10}
\]

In particular there is no additional degree-\(p\) relation arising from cancellation between higher-order terms. The computation is the image of the entire ideal in the quotient, not just the leading term of a selected generator.

Its saturation in the free module \(\operatorname{Sym}_A^p(A^2)\), with respect to the generic point of \(\operatorname{Spec}A\), is \(A u^p\). Therefore

\[
\boxed{\mathcal R_p^{\mathrm{sat}}/\mathcal R_p
\simeq A/(t^N),\qquad
\operatorname{length}_A(
\mathcal R_p^{\mathrm{sat}}/\mathcal R_p)=N.}
\tag{R11}
\]

Equivalently, \(M_N^p/M_N^{p+1}\) has a torsion summand \((A/(t^N))u^p\), while its other degree-\(p\) monomials form a free summand. Thus flatness of the original algebra (R8) does not imply flatness of its normal associated graded algebra.

## 7. Fixed generic filtered ideal, with the exact coordinate qualification

Let \(K=k(t)\) and restrict to \(N=aL\), \(L\ge1\). The invertible \(K\)-linear coordinate substitution

\[
u\longmapsto u,\qquad v\longmapsto t^L v'
\]

preserves \((u,v)\) and all of its powers. It takes the generic ideal in (R7) to

\[
(u^b,t^{aL}(v'^a+u^p))
=(u^b,v'^a+u^p),
\tag{R12}
\]

since \(t\) is a unit in \(K\). Hence the complete generic ideals, not just their quotient lengths, are identified by this filtration-preserving coordinate isomorphism. Their Rees algebras, normalized blowups, divisorial Rees valuations, orders \(a_i\), and finite degrees \(f_i\) correspond under that isomorphism. Nevertheless (R11) has length \(aL\), which is unbounded.

This proves the precise limitation:

\[
\boxed{\begin{gathered}
\text{The generic filtered ideal, up to a filtration-preserving}\
\text{coordinate isomorphism, and its corresponding divisorial}\
\text{Rees data do not bound the first-relation saturation defect}\
\text{in this affine local family.}
\end{gathered}}
\tag{R13}
\]

One must not strengthen (R12) to equality in a fixed ambient coordinate ring. For example, take \(p=2,a=b=3\). In \(K[[s]]\), the arc

\[
u=s^3,\qquad v=-t^Ls^2
\]

has order nine on \(J_{3L}=(u^3,v^3+t^{3L}u^2)\), while \(v^3+u^2\) has order six, since \(1-t^{3L}\ne0\). The valuative criterion for integral dependence therefore shows

\[
v^3+u^2\notin\overline{J_{3L}},
\]

although it belongs to \((u^3,v^3+u^2)\). Thus even the integral closures of these ideals need not agree in the fixed ambient coordinates. The comparison made in (R12)--(R13) is explicitly up to the coordinate isomorphism; no identical-ambient-valuations claim is needed.

## 8. Additional audit: fixed full generic initial ideals

The companion proposal's Corollaries 4b and 4c both pass independent reconstruction. In this section, the initial ideal means the full ordinary initial ideal for the maximal-ideal filtration over \(K=k(t)\), using lowest total normal degree. It does not mean a chosen monomial-order initial ideal.

Write \(c=t^{-N}\in K^\times\) and \(F=u^p+cv^a\), so that the generic ideal is \((u^b,F)\).

For \(b=2p\), the identity

\[
(u^p-cv^a)F=u^{2p}-c^2v^{2a}
\]

shows that

\[
(u^{2p},F)=(F,v^{2a}).
\]

The two latter generators have initial forms \(u^p\) and \(v^{2a}\), so

\[
(u^p,v^{2a})\subseteq\operatorname{in}_{\mathfrak q}(J_NK[u,v]).
\]

The left ideal has colength \(2pa\), and the original quotient has exactly that length by (R8). Passage to the full associated graded algebra preserves the length of an Artinian local algebra. A strict additional initial relation would reduce this length. Therefore

\[
\boxed{\operatorname{in}_{\mathfrak q}(J_NK[u,v])
=(u^p,v^{2a})\quad\text{when }b=2p.}
\tag{R14}
\]

This is a coprime binary complete-intersection initial type \((p,2a)\). In particular \(p=2,a=3,b=4,N=3L\) has fixed generic full initial type \((2,6)\), length twelve, and unbounded degree-two relation defect \(3L\).

For \(b=p+1\), the exact cancellations

\[
uF-u^{p+1}=cuv^a,
\qquad
v^aF-u^{p-1}(uv^a)=cv^{2a}
\]

give \(uv^a,v^{2a}\in J_NK[u,v]\). Together with the initial form \(u^p\) of \(F\), they give inclusion of

\[
L=(u^p,uv^a,v^{2a})
\]

in the full initial ideal. Its standard monomials are \(v^j\), \(0\le j<2a\), and \(u^iv^j\), \(1\le i<p\), \(0\le j<a\). Hence

\[
\operatorname{length}(K[u,v]/L)
=2a+(p-1)a=(p+1)a,
\]

equal to the original length. The same length argument proves

\[
\boxed{\operatorname{in}_{\mathfrak q}(J_NK[u,v])
=(u^p,uv^a,v^{2a})\quad\text{when }b=p+1.}
\tag{R15}
\]

All three monomials are minimal generators since \(p\ge2\). This second initial algebra is not a complete intersection. For \(p=2,a=3,b=3,N=3L\), it is \(K[u,v]/(u^2,uv^3,v^6)\), of length nine, again with unbounded first-relation defect \(3L\).

The additional socle observation also passes. In the quotient of (R15), its socle has exactly the monomial basis

\[
u^{p-1}v^{a-1},\qquad v^{2a-1},
\]

in degrees \(p+a-2\) and \(2a-1\). Indeed a standard monomial with positive \(u\)-exponent is killed by both variables precisely when its \(u\)-exponent is \(p-1\) and its \(v\)-exponent is \(a-1\). Among the standard monomials having zero \(u\)-exponent, only \(v^{2a-1}\) is killed by both variables. Since multiplication by each variable sends distinct surviving monomials to distinct monomials, cancellation supplies no additional socle elements. Thus this associated graded algebra has socle dimension two, whereas the original generic local algebra is a complete intersection and hence Gorenstein. A one-dimensional graded-socle pairing therefore cannot be transferred from the original algebra to its full ordinary associated graded algebra in this example.

These two subfamilies show that the limitation (R13) persists both with a fixed coprime-CI full generic initial type and with a fixed three-generator full generic initial ideal. They do not weaken the saturated-actual-first-relation hypothesis of [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md): by (R11), that hypothesis fails for every \(N>0\). No proof of that promoted theorem is repeated here.

## 9. Frontier impact and unresolved dependencies

The full-ideal normalized blowup removes the dependence on a chosen pair of generators, but its divisorial valuations over a pure curve-supported complete intersection all come from the generic transverse ideal. The example proves that those generic data do not control even the first-relation saturation defect along the base. The ordinary Segre pushforward supplies only the degree expression (R6).

These conclusions leave open invariants retaining global variation: the exceptional surfaces as finite covers of the reduced exceptional ruled surface, their degeneration, ramification or conductor data, and the full filtration relative to the reduced support. No inequality for those finer data is proved here. The affine family does not establish their realizability for the fixed rational quartic or a global two-hypersurface STCI presentation. The unrestricted characteristic-zero quartic question remains open.

The evidence in this audit is the exact arguments above. No computational reduction is being reported as a completed calculation, and no promoted theorem or closed quartic-carrier case is reopened.
