# The conormal surface as an ordered residual-root construction

Date: 2026-10-24. Author role: `conormal_geometry`.

**Status: new provisional intrinsic geometry, with a separate independent
audit; no canonical promotion.** The main statements concern precisely
the marked embedding

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3
\]

over an algebraically closed field of characteristic zero. No carrier
classification, STCI obstruction, or higher-filtration result is used.

The construction gives a useful common source for three objects: the
quadric-tangent section is a ramification divisor, the osculating section
is a graph, and the bitangent locus is the inverse image of the diagonal
conic under one residual-divisor map. These descriptions include the
endpoint schemes.

## 1. Inputs and conventions

Retrieval began with [INDEX](../INDEX.md), the requested navigation
summaries, the [authority policy](../AUTHORITY.md), and the
[contribution checklist](../CONTRIBUTING_AGENT.md). Relevant retained
evidence is the [discussion reconciliation](2026-10-24-discussion-reconciliation.md),
[dual-incidence derivation](2026-10-24-special-dual-incidence-derivation.md),
[geometry audit](2026-10-24-special-lines-planes-geometry-audit.md), and
[symmetric-square note](2026-10-24-quartic-symmetric-square-bitangents.md).
Their status remains provisional. The promoted input
[STCI-R-0020](../results/quartic_conormal_characteristic_jump.md) is used
only for its stated splitting
\(E=N^*_{C/\mathbf P^3}=\mathcal O(-7)^2\) when 2 is invertible,
and \(\mathcal O(-8)\oplus\mathcal O(-6)\) in characteristic two.
Its accepted proof is not rerun.

Projectivization \(\mathbf P_{\rm lines}(A)\) parametrizes sublines
of a vector bundle \(A\). Put

\[
U=H^0(C,\mathcal O(2)),\quad P=\mathbf P_{\rm lines}(U),\quad
W=H^0(C,\mathcal O(4)),\quad
V=\langle s^4,s^3t,st^3,t^4\rangle.
\]

A quadratic divisor is represented by
\(r=\alpha s^2+\beta st+\gamma t^2\); thus in the affine root
coordinate \(z=t/s\) it is \(\alpha+\beta z+\gamma z^2\).
The diagonal of double divisors is the Veronese conic

\[
\Delta=\{\beta^2-4\alpha\gamma=0\}\subset P,
\qquad j(p)=2p.
\]

Multiplication followed by the quotient \(W\to W/V\) is the symmetric
pairing, valued in the one-dimensional space \(W/V\),

\[
\mathsf B(r,r')=\alpha\gamma'+\beta\beta'+\gamma\alpha'.
\tag{1.1}
\]

Its matrix has determinant \(-1\). Rescaling a generator of \(W/V\)
rescales the pairing without changing its projective polarity. It
depends on the marked linear system \(V\); it is not attached to an
unmarked abstract rational curve.

## 2. The conormal incidence is a surface inside the flag threefold

Let

\[
\mathcal I=\{(D,R)\in P\times P:\mathsf B(D,R)=0\},\qquad
\mu(D,R)=D+R\in\mathbf P(V).
\]

The conormal incidence is the base change

\[
N=\mathcal I\times_{P,j}C
=\{(p,R):2p+R\in\mathbf P(V)\}.
\tag{2.1}
\]

The isomorphism with \(\{(p,H):T_pC\subset H\}\) is functorial:
restrict a tangent plane to \(C\), then remove its relative effective
Cartier divisor \(2p\). Conversely multiply the sections representing
\(2p\) and \(R\). On a smooth curve this construction works in
families and includes \(R=2p\) and all other nonreduced cases.
Accordingly \(N=\operatorname{pr}_1^{-1}(\Delta)\) as a closed
surface in \(\mathcal I\); the flag threefold itself is not the
conormal normalization.

In jet-bundle terms let

\[
K=\ker\bigl(V\otimes\mathcal O_C\longrightarrow
J^1\mathcal O_C(4)\bigr).
\]

The map is surjective because the embedding separates length-two
subschemes. The Euler and conormal sequences identify
\(K=E\otimes\mathcal O_C(1)=E(4)\), so

\[
N=\mathbf P_{\rm lines}(K),\qquad K\simeq\mathcal O(-3)^2.
\tag{2.2}
\]

This convention parametrizes **conormal covectors**. The exceptional
divisor of the blowup of \(\mathbf P^3\) along \(C\), in the normal-line
convention, parametrizes lines in \(E^\vee\). There is a canonical
rank-two projective identification sending a normal line to its
annihilator covector line. It is not an identification of the two vector
bundles; the rank-two duality carries a determinant twist.

## 3. A canonical product attached to the marked linear system

There is more structure than an unspecified balanced splitting:

\[
\boxed{\quad N\ \simeq\ C\times C.\quad}
\tag{3.1}
\]

The first factor records the contact point. To define the second, take
\((p,R)\in N\). The polar line
\(\mathsf B(-,R)=0\) in \(P\) meets \(\Delta\) in a relative divisor
of degree two containing \(j(p)\). Its residual degree-one divisor
is \(j(p')\). This defines the **companion point** \(p'\), including
the tangency case \(p'=p\).

For the inverse construction, the pair \(p,p'\) determines the chord
of \(\Delta\), or its tangent if the points coincide. Apply the
inverse polarity of \(\mathsf B\) to that line to obtain \(R\).
These are inverse morphisms: restriction of linear forms to a smooth
plane conic is the complete degree-two system, and the universal
incidence of a root in a degree-two divisor is \(C\times C\), with
the second root obtained by Cartier residual. Thus no division by a
generic coordinate, or extension only at geometric points, is involved.

The product is canonical **relative to the embedded linear system**.
It uses both \(\Delta\) and the marked polarity \(\mathsf B\).
Every automorphism of \((\mathbf P^3,C)\) acts diagonally on the
two copies of \(C\) in (3.1).

Write \(\mathcal O(a,b)\) for the two product classes, with the first
factor the contact point. The residual map

\[
r:N\longrightarrow P,\qquad(p,p')\longmapsto R
\]

is the symmetric-square quotient by
\(\delta(p,p')=(p',p)\), followed by the projective isomorphism
induced by the chord construction and \(\mathsf B^{-1}\).
Consequently it is finite flat of degree two, and

\[
r^*\mathcal O_P(1)=\mathcal O(1,1).
\tag{3.2}
\]

With finite affine points \(p=u,p'=v\), one can choose the residual
quadratic as

\[
R(z)=z^2+\frac{u+v}{2}z+uv.
\tag{3.3}
\]

For fixed \(R=\alpha+\beta z+\gamma z^2\), the two companion
points satisfy
\(\gamma u^2-2\beta u+\alpha=0\). The branch conic is therefore

\[
\mathcal A=\{\beta^2-\alpha\gamma=0\}\subset P.
\tag{3.4}
\]

It differs from both the diagonal conic \(\Delta\) and the bitangent
conic \(\mathcal B=\{\beta^2+2\alpha\gamma=0\}\).

## 4. The dual normalization and its hyperplane bundle

The map \(\nu:N\to\mathbf P(V)\) sends \((p,R)\) to the section
with divisor \(2p+R\). Since \(j^*\mathcal O_P(1)=\mathcal O_C(2)\),
and multiplication on \(P\times P\) has bundle \(\mathcal O(1,1)\),

\[
\nu^*\mathcal O_{\mathbf P(V)}(1)=\mathcal O(3,1).
\tag{4.1}
\]

Every nonzero quartic has finitely many multiple roots, so \(\nu\)
is proper and quasi-finite, hence finite. A general member of its image
has one double root and two other simple roots. For example
\((z-1)^2(z^2+z/2)\) has precisely that root pattern. Thus \(\nu\)
is birational in characteristic zero. Its image is the dual variety
\(C^\vee\), and the smooth surface \(N\) is its normalization.
The degree follows without expanding a discriminant:

\[
\deg C^\vee=c_1(\mathcal O(3,1))^2=6.
\]

For checking signs, if \(p=[s:t]\) and \(p'=[a:b]\), the plane
coefficients are

\[
\nu(p,p')=
[2t^3b:\ t^2(ta-3sb):\ s^2(sb-3ta):\ 2s^3a].
\tag{4.2}
\]

These forms have bidegree \((3,1)\) and no common zero. In the affine
chart they represent
\((z-u)^2(z^2+(u+v)z/2+uv)\). Formula (4.2) is a verification of
the global construction, not its definition.

## 5. The two marked sections and their different meanings

The ramification divisor of \(r\) is the diagonal \(p'=p\).
It is exactly the quadric-tangent section \(\sigma_Q\). Indeed
(3.3) gives \(R=z^2+uz+u^2\) there, and

\[
(z-u)^2R=z^4-uz^3-u^3z+u^4,
\qquad
T_{c(u)}Q=[u^4:-u^3:-u:1].
\tag{5.1}
\]

Equivalently, the quadric-tangent section is characterized intrinsically
as the locus where the companion contact point coalesces with the given
one. Its residual image is the branch conic \(\mathcal A\), mapped
isomorphically onto that conic.

This ramification concerns \(r\), not the normalization map \(\nu\).
Away from the endpoints, the quadric-tangent plane section has exactly
one double root and two simple roots, so its point on \(C^\vee\) is
smooth. A branch point for one incidence projection need not be a
singular point of the dual image under another projection.

Let \(\iota(u)=-u\), the osculating residual involution retained
from the audited special-lines work. The limiting osculating section
is the graph

\[
\sigma_O=\{p'=\iota(p)\}\subset C\times C.
\tag{5.2}
\]

Its residual quadratic is \(z^2-u^2\), giving the divisor
\(3p+\iota(p)\), including \(4p\) at the two endpoints.
The residual image is the line \(\beta=0\), and
\(r|_{\sigma_O}\) is its degree-two cover branched at the endpoints.
In fact \(r^{-1}(\beta=0)=\sigma_O\) as Cartier divisors.
The involution \(\delta\) preserves this graph and restricts to
\(p\mapsto\iota(p)\).

Both sections have class \(\mathcal O(1,1)\), square two, and dual
hyperplane degree four:

| Section | Product description | Square | Image under \(r\) | Image under \(\nu\) |
| --- | --- | --- | --- | --- |
| \(\sigma_Q\) | diagonal | 2 | branch conic \(\mathcal A\), degree 1 | quadric-tangent rational quartic in \(Q^\vee\) |
| \(\sigma_O\) | graph of \(\iota\) | 2 | line \(\beta=0\), degree 2 | osculating rational quartic |

They intersect as reduced points exactly at
\((p_0,p_0),(p_\infty,p_\infty)\). The local graph equations
\(v=u\) and \(v=-u\) show that each intersection is simple in
characteristic zero.

Their images in \(\mathbf P(V)\) have a different intersection
scheme: each endpoint intersection has length three. Near the first
endpoint compare
\([u^4:-u^3:-u:1]\) with
\([-v^4:2v^3:-2v:1]\). Equality gives \(u=2v\) and an ideal
\((v^3)\); reversal gives the same at infinity. Thus intersection
on the normalization cannot be substituted for intersection of the
image curves.

Under the ruling \(Q\to C\) meeting \(C\) once, the curve
\(C\subset Q\) has square six. Since \(\sigma_Q^2=2\), there is
**no isomorphism over \(C\)** carrying \(\sigma_Q\) to that marked
curve on \(Q\). The canonical product (3.1) does not supply such an
isomorphism. Polarity sends tangent-plane covectors to poles in ambient
space; the polar line of a tangent line is generally not a ruling of
\(Q\).

## 6. Bitangency and the distinction among the involutions

The locus with residual divisor another double point is

\[
N\cap\tau(N)=r^{-1}(\Delta)\subset\mathcal I,
\qquad \tau(D,R)=(R,D).
\tag{6.1}
\]

It is the ordered bitangent contact curve. If the residual double
point is \(q\), then the missing coefficient condition is
\(p^2+4pq+q^2=0\), giving partner ratios
\(\rho,\rho^{-1}\), where \(\rho=-2+\sqrt3\). Thus it has two
section components, each of class \((1,1)\). In companion coordinates
these are the graphs of multiplication by \(\rho^2\) and
\(\rho^{-2}\), up to interchanging their labels. They meet simply
at each endpoint; their union is the full Cartier inverse image of
\(\Delta\), including the two crossing points.

The three operations have different domains and fixed loci:

- \(\tau\) is residual swap on the flag threefold. It fixes
  \((D,D)\) with \(D\) on the bitangent conic \(\mathcal B\).
- \(\delta\) is the deck involution of \(r:N\to P\). It fixes
  the entire quadric-tangent section \(\sigma_Q\).
- \(\iota\) is an involution of the original curve. It is the
  restriction of \(\delta\) to the invariant osculating graph.

On the bitangent curve, both \(\delta\) and \(\tau\) exchange the
two components, but they do not do the same thing: \(\delta\) keeps
the residual divisor \(2q\) fixed and replaces the contact \(p\)
by its other compatible companion; \(\tau\) exchanges contact and
residual divisors. The ratios \(\rho^{\pm1}\) encode a two-valued
bitangent correspondence, rather than an involution of \(C\).

## 7. Higher contact as jet incidence, including endpoint schemes

Inside \(N\), the condition of contact at least three at the recorded
point is the vanishing of the residual quadratic evaluated there.
In (4.2) coordinates its global equation is

\[
3st(sb+ta)=0.
\]

Therefore the full third-contact Cartier divisor is

\[
T_3=F_0+F_\infty+\sigma_O\sim\mathcal O(3,1),
\tag{7.1}
\]

where \(F_0,F_\infty\) are the fibers of \(N\to C\) over the
endpoints. Their images are exactly the two endpoint pencil lines.
This explains why closing only the generic osculating section misses
two components of the triple-contact locus. The intersections of
\(\sigma_O\) with those fibers are ordinary crossings on \(N\).

The natural fourth-contact **jet scheme** retains more than its two
geometric points. Near \((u,v)=(0,0)\), write

\[
f(z)=(z-u)^2R(z),\qquad
R(z)=z^2+\frac{u+v}{2}z+uv.
\]

Its ideal is obtained by requiring \(R(u)=R'(u)=0\):

\[
\bigl(3u(u+v),\ 5u+v\bigr)
=\bigl(u^2,\ v+5u\bigr).
\tag{7.2}
\]

It has length two. Reversal gives the same length at infinity, and
there are no other fourth-contact points. Its total length is four,
in agreement with the ramification weight of the degree-four
four-dimensional linear system on \(\mathbf P^1\). One must
distinguish this jet incidence scheme from the reduced two-point
intersection \(\sigma_Q\cap\sigma_O\). Restricting the fourth-jet
ideal to the osculating section gives a reduced endpoint; the full
jet scheme has an additional first-order direction in \(N\).

There is a direct flag interpretation of this entire scheme:

\[
\boxed{\quad T_4=N\cap\operatorname{Fix}(\tau)\quad}
\tag{7.3}
\]

scheme-theoretically inside \(\mathcal I\). Indeed \(N\) has
\(D=2p\), and contact four means exactly \(R=2p\), which is the
swap-fixed equation. Pulling the fixed-conic equation back to \(C\)
gives \(\mathsf B(2p,2p)=6s^2t^2\). Thus projection to the contact
point identifies \(T_4\) with the doubled divisor
\(2p_0+2p_\infty\). The fixed conic on the threefold and the
Wronskian scheme on the curve are related by this nontransverse
intersection, rather than by identifying their dimensions or supports.

The full Jacobian singular subscheme of \(C^\vee\) is a separate
construction on the image. Formula (7.1), or the contact-four scheme,
does not by itself identify its nilpotent structure.

There is nevertheless an exact contact link to the threefold map
\(\mu:\mathcal I\to\mathbf P(V)\). Its ramification divisor is
the quadratic resultant \(\operatorname{Res}(D,R)=0\): the
differential of multiplication has a kernel precisely where the two
quadratics share a root. The determinant and resultant both have
bidegree \((2,2)\), and at a general common simple root the
ramification is simple. On the conormal surface \(D=\ell_p^2\),

\[
\operatorname{Res}(\ell_p^2,R)=R(p)^2,
\qquad
\operatorname{Ram}(\mu)|_N=2T_3.
\tag{7.4}
\]

This is an equality of Cartier divisors, not just an equality of
supports. Its class on \(C\times C\) is \((6,2)\), twice the
class in (7.1). It does not assert that the conormal surface itself is
the ramification divisor of the threefold map.

## 8. Characteristic boundary and limits

The polarity \(\mathsf B\) remains nondegenerate in characteristic
two, and its flag threefold remains smooth. The smooth-Veronese-conic
construction does not specialize: \(p\mapsto2p\) becomes purely
inseparable onto the line \(\beta=0\). By R0020 the conormal
incidence is then \(\mathbb F_2\), not a product over \(C\).
In particular (3.1), its deck involution, and the section intersection
arguments cannot be imported unchanged.

More explicitly, for
\(f(z)=A+Bz+Cz^3+Dz^4\) in characteristic two, conormal incidence
satisfies

\[
B=Cu^2,\qquad A=Du^4.
\]

The reduced dual is the cubic
\(AC^2+B^2D=0\). The conormal map to it is generically purely
inseparable of degree two, so **it is not its normalization**. The
restricted characteristic-zero discriminant specializes to the square
\((AC^2+B^2D)^2\), with multiplicity retained. In characteristic
three the triple-contact equation (7.1) also changes, so the main
normalization and osculating conclusions are asserted here in
characteristic zero only.

The new arguments close the marked-product, section-class,
residual-double-cover, and higher-jet questions for the fixed embedding
in characteristic zero. They do not classify other projection centers,
identify \(N\) with the marked quadric, determine the entire image
singular scheme by themselves, or establish an STCI consequence.
Independent reconstruction is recorded in
[the conormal audit](2026-10-24-quartic-conormal-independent-audit.md).
