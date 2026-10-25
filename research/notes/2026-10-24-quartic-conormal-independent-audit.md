# Independent audit: residual conormal product and higher contact

Date: 2026-10-24. Reviewer: independent agent `conormal_check`.

**Status: independent reconstruction of new provisional research evidence;
no canonical promotion.** The field is algebraically closed of characteristic
zero, and the curve is exactly
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\).
The reviewer read the research index and the discussion reconciliation before
reconstructing the proposed residual construction. No STCI exclusion or
normal-bundle calculation is used or rerun.

## 1. Global construction, including coincident points

Write quadratic divisors as
\(D=\alpha z^2+\beta z+\gamma\) and
\(R=Az^2+Bz+C_0\). The coefficient of \(z^2\) in their product is

\[
\mathsf B(D,R)=\alpha C_0+\beta B+\gamma A.
\]

Its matrix is invertible. The diagonal double-divisor locus
\(\Delta\subset\operatorname{Sym}^2C\) is a smooth Veronese conic in
characteristic zero. For a conormal pair \((p,H)\), write its plane section
as \(2p+R\). The polar line \(\mathsf B(-,R)=0\) cuts \(\Delta\) in
a degree-two effective Cartier divisor containing \(2p\). Taking the
residual degree-one divisor gives another point \(2p'\).

This construction extends through tangent polar lines: the residual point
then equals the first point, rather than becoming undefined. Conversely,
the chord or tangent of \(\Delta\) through \(2p,2p'\), followed by
\(\mathsf B^{-1}\), gives the unique residual quadratic. The two operations
are inverse morphisms, using the universal degree-two divisor on the smooth
conic. Thus they prove a global isomorphism

\[
N\simeq C\times C,
\]

canonical relative to the marked linear system. The first coordinate is
the contact point and the second is its companion. The residual projection
is the symmetric quotient of these factors followed by a projective linear
isomorphism of its target. It is finite flat of degree two.

In affine coordinates \(p=u,p'=v\), the residual quadratic is

\[
R(z)=z^2+\frac{u+v}{2}z+uv,
\qquad
f_{u,v}(z)=(z-u)^2R(z).
\]

The residual projection has branch conic \(B^2-AC_0=0\); its ramification
curve is the product diagonal. This also proves that the product construction
does not depend on selecting distinct points or dividing by \(u-v\).

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

## 7. Characteristic boundary and audit outcome

The smooth-conic construction requires characteristic different from two;
the stated higher-contact equations and ordinary derivative interpretation
are here asserted in characteristic zero. In characteristic two, the
double-divisor map becomes purely inseparable onto a line, even though the
ambient pairing remains nondegenerate. The companion product, branch conic,
and these jet formulas must not be specialized unchanged. Characteristics
three and five also require separate treatment of the displayed constants
and contact calculations.

**Outcome:** the reviewer found no discrepancy in the global product,
ramification identification, distinguished sections, plane-map line bundle,
third-contact divisor, length-four fourth-contact scheme, fixed-scheme
intersection, resultant restriction, or image intersection lengths under the stated
characteristic-zero hypotheses. The arguments above reconstruct the claims
independently and include the coincident-point and endpoint cases. They are
review evidence for the [conormal residual note](2026-10-24-quartic-conormal-residual-geometry.md),
not a promoted result record or an STCI conclusion.
