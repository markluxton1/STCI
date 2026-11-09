# Marked conormal normalization and higher contact

The fixed marked system is \(C=[s^4:s^3t:st^3:t^4]\), over an algebraically closed characteristic-zero field unless a characteristic is explicitly changed. The conormal incidence remembers a contact point and a tangent plane. Its canonical product comes from residual intersection on the marked conic, rather than from an arbitrary balanced splitting. Its diagonal, osculating graph and residual swap lie on different spaces; the proof below retains the endpoint contact schemes.

The conormal convention agrees with Tevelev, *Projectively Dual Varieties*, §§1.1–1.2 and Proposition 3.2: tangency is first-jet incidence, with a marked contact point before projection to the dual space. This general framework does not imply that a particular projection is finite birational, especially in positive characteristic; the residual-root proof here establishes that additional assertion for the specified characteristic-zero system. [Primary text](https://arxiv.org/pdf/math/0112028).

<a id="quartic-conormal-residual-geometry"></a>

## Ordered residual roots and the conormal product

## 1. Inputs and conventions

Retrieval began with [INDEX](../INDEX.md), the requested navigation
summaries, and the [evidence and review rules](../MODEL.md#evidence-and-review).
Relevant retained evidence is the [discussion reconciliation](QUARTIC_CONORMAL_AND_CONTACT.md),
[dual-incidence derivation](QUARTIC_DUAL_SCHEMES.md),
[geometry audit](QUARTIC_DUAL_SCHEMES.md), and
[symmetric-square note](QUARTIC_DUAL_FLAGS_AND_BITANGENTS.md#quartic-symmetric-square-bitangents).
Their status retains the review scope stated here. The input
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


## Endpoint schemes and different involutions

## 2. Distinguished sections and plane-map degree

On the diagonal \(v=u\),

\[
f_{u,u}(z)=(z-u)^2(z^2+uz+u^2)
=z^4-uz^3-u^3z+u^4.
\]

The plane coefficient vector is
\([u^4:-u^3:-u:1]\), which equals the gradient of
\(x_0x_3-x_1x_2\) at \([1:u:u^3:u^4]\). Consequently the ramification
section is exactly the quadric-tangent section \(\sigma_Q\), rather than
merely a section with the same numerical class.

For \(v=-u\), the plane section is
\((z-u)^3(z+u)\). This is the osculating section \(\sigma_O\), including
its limiting contact-four planes at the endpoints.

In homogeneous product coordinates \(([s:t],[a:b])\), the plane map is

\[
\Phi([s:t],[a:b])=
[2t^3b:t^2(ta-3sb):s^2(sb-3ta):2s^3a].
\]

The four coordinates have bidegree \((3,1)\), and have no common zero.
For example, at \(s=0\) the first two coordinates cannot both vanish;
at \(t=0\) the last two cannot both vanish; elsewhere the same conclusion
follows from the first and last coordinates. Therefore
\(\Phi^*\mathcal O(1)=\mathcal O(3,1)\).

Both distinguished sections have class \((1,1)\), hence square two. Their
equations are \(sb-ta=0\) and \(sb+ta=0\). Their intersection consists
of the two endpoint pairs, each reduced and of local intersection length
one. In particular this product construction does not identify the marked
section with \(C\subset Q\), whose self-intersection is six.

## 3. The complete third-contact divisor

On the affine chart the universal plane section already has its factor
\((z-u)^2\). Contact at least three is consequently the single equation

\[
R(u)=\frac32u(u+v)=0.
\]

Its global equation, up to a nonzero scalar, is
\(st(sb+ta)=0\), of bidegree \((3,1)\). Hence the natural third-contact
Cartier divisor is exactly

\[
T_3=f_0+f_\infty+\sigma_O.
\]

All three components have multiplicity one. The two endpoint fibers are
essential: third contact does not consist solely of the limiting osculating
section. The affine formula and its reversed-coordinate counterpart cover
every component and their intersections.

## 4. The fourth-contact scheme is not reduced

In characteristic zero, contact at least four is obtained by imposing
\(R(u)=R'(u)=0\). Near the first endpoint this gives

\[
\begin{aligned}
I_{T_4}
&=(3u(u+v),5u+v)\\
&=(u^2,v+5u).
\end{aligned}
\]

Thus the endpoint has a length-two scheme, with nonzero first-order
direction \(v=-5u\). Reversing coordinates gives exactly the same local
description at infinity. Away from the endpoints, the only possible
third-contact locus is \(v=-u\), where \(R'(u)=2u\ne0\), so there are no
other fourth-contact points.

Therefore the underlying hyperosculating set is two points, but the natural
fourth-jet incidence scheme has total length four, with one doubled point
at each endpoint. It is not the scheme-theoretic intersection of the reduced
sections \(\sigma_Q\) and \(\sigma_O\).

The independent ramification check agrees. The vanishing sequence of the
four-dimensional series at each endpoint is \((0,1,3,4)\), of weight two.
The Wronskian is a section of
\(\mathcal O(4)^4\otimes K_C^6\simeq\mathcal O(4)\), and its divisor is
\(2p_0+2p_\infty\). The local fourth-contact scheme maps isomorphically
to this doubled divisor under projection to the contact point. This agreement
checks both the endpoint multiplicity and the total length.

## 5. Fourth contact inside the fixed scheme of residual swap

Let \(\tau(D,R)=(R,D)\) on the flag threefold. Its fixed scheme is
\(R=D\), with \(\mathsf B(D,D)=0\). Restricting to the conormal surface
where \(D=2p\) gives precisely contact four: the plane section is \(4p\).
This equality holds as schemes. In the affine companion coordinates,
\(R=(z-u)^2\) gives the equations

\[
v+5u=0,\qquad uv-u^2=0,
\]

which generate \((v+5u,u^2)\). Thus
\(N\cap\operatorname{Fix}(\tau)=T_4\), including the nonreduced structure.
Equivalently, substituting the double divisor into the fixed-conic equation
gives \(6s^2t^2=0\), confirming the two doubled endpoints.

## 6. Resultant ramification and image intersections

The multiplication map from the full product of quadratic spaces to the
space of quartics has ramification divisor the resultant of the two
quadratics. Its differential sends \((\dot D,\dot R)\) to
\(\dot D R+D\dot R\); it is singular precisely at common-root pairs, and
at a generic simple common root the ramification is simple. The determinant
has bidegree \((2,2)\), equal to that of the resultant. Restricting this
finite map to the marked hyperplane gives the flag multiplication map;
the conormal factors of this base change cancel in the relative canonical
bundle formula. Equivalently, adjunction gives
\(K_{\mathcal I}=\mathcal O(-2,-2)\), whereas the pullback of the canonical
bundle of \(\mathbf P(V)\) is \(\mathcal O(-4,-4)\). Therefore

\[
\operatorname{Ram}(\mu)=\operatorname{div}\operatorname{Res}(D,R).
\]

On \(N\), the identity
\(\operatorname{Res}((z-u)^2,R)=R(u)^2\) proves the exact Cartier-divisor
equality

\[
\operatorname{Ram}(\mu)|_N=2T_3.
\]

This is ramification of the threefold map restricted to the surface; it
must not be relabelled as ramification of the dual normalization map.

The images of \(\sigma_Q\) and \(\sigma_O\) have intersection length three
at each endpoint, unlike the simple intersection of the sections in \(N\).
Near the first endpoint their vectors are
\([u^4:-u^3:-u:1]\) and \([-v^4:2v^3:-2v:1]\).
Equality first gives \(u=2v\), and the other equations then give the ideal
\((v^3)\); the reversed-coordinate calculation is identical at infinity.
The normalization remembers the contact point, so these are different
incidence problems and their different scheme lengths are consistent.


## Characteristic reach and mathematical status

The residual-pair flag equation is defined over the integers and remains a smooth threefold in characteristic two. The characteristic-zero product construction here divides by two; in characteristic two the conormal surface is \(\mathbf F_2\) and its map to the reduced dual is inseparable, so it is not that dual's normalization. Ordinary derivatives in the third/fourth contact calculations must not replace Hasse jets in small characteristic. The exact equalizer of residual swap remains meaningful scheme-theoretically and becomes a double line in characteristic two; [the flag proof](QUARTIC_DUAL_FLAGS_AND_BITANGENTS.md) treats that degeneration. The exact statement is in [R-0026](../results/quartic_flag_conormal_geometry.md); the identities are marked-incidence geometry, not an STCI exclusion.


## Equal endpoint lengths do not identify two contact schemes

Let \(\mathscr S=\operatorname{pr}_1^{-1}(L_\iota)\) in the flag, where \(L_\iota\subset\operatorname{Sym}^2C\) is the line of divisors \(p+\iota(p)\). This is the second flag surface normalizing the dual cubic, as proved in [the Gauss/flag construction](CUBIC_SCROLL_AND_RULED_SURFACES.md#cubic-scroll-gauss-dual). With \(N=N_C\),
\[
\tau(N)\cap\mathscr S=\tau(\sigma_O)
\]
as schemes. Indeed a first factor \(z^2-a^2\) and a doubled second factor \((z-r)^2\) satisfy the missing-middle-coefficient condition precisely when \(a^2=r^2\); using the first-factor coordinate \(a^2\) gives the graph \(a^2=r^2\).

Nevertheless \(N\cap\tau(\sigma_O)\) is not the fourth-contact scheme \(T_4=N\cap\operatorname{Fix}(\tau)\). In the companion coordinates \((u,v)\) near the first endpoint, the residual quadratic is \(R(z)=z^2+(u+v)z/2+uv\). A swapped osculating flag has first factor \(z^2-a^2\) and residual \((z-a)^2\). Requiring the first factor to be \((z-u)^2\) imposes \(u=0,a^2=0\); comparison of the residual linear coefficient gives \(v=-4a\). Consequently
\[
I_{N\cap\tau(\sigma_O)}=(u,v^2),\qquad
I_{T_4}=(u^2,v+5u).
\]
Both schemes have length two at the endpoint, but their tangent directions differ. Reversal gives the other endpoint. This explicit calculation preserves the source audit's correction: equality of support and local lengths cannot identify embedded incidence schemes.
