# The cubic scroll: Gauss resolution, dual normalization, and common planes

Date: 2026-10-24. Author role: `scroll_duality`.

**Status: proposed intrinsic geometry with proofs, independently reviewed in the
[companion audit](2026-10-24-cubic-scroll-dual-independent-audit.md); not a canonical
result record.** Throughout, \(k\) is algebraically closed of characteristic zero,

\[
C=[s^4:s^3t:st^3:t^4],\qquad
R=V(x_0x_2^2-x_1^2x_3),\qquad Q=V(x_0x_3-x_1x_2).
\]

The claim concerns this fixed marked embedding. It is not a statement about all
rational quartics or all cubic scroll projections. It has no STCI conclusion.

## 1. Retained input and conventions

We retain the independently reviewed construction of the smooth finite
normalization from the [merged cubic-scroll note](2026-10-24-cubic-scroll-normalization.md),
Sections 2–5, and its
[independent audit](2026-10-24-p4-ruled-models-independent-audit.md), Section 3.
We do not rerun that normalization proof. In its notation,

\[
T=\mathbb F_1=\mathbf P_{\mathrm{lines}}(\mathcal O(-2)\oplus\mathcal O(-1)),
\quad H=E+2f,
\]

\[
\nu([v_0:v_1;A:B])=[A v_0^2:Bv_0:Bv_1:A v_1^2].
\tag{1}
\]

Here \(E^2=-1, Ef=1, f^2=0\), and Cox degrees are

\[
\deg A=E,\qquad \deg B=E+f,\qquad \deg v_i=f.
\]

The conductor section is \(D=V(B)\), class \(E+f\), square (1), and

\[
\widehat C=V(B^2-A^2v_0v_1),\qquad [\widehat C]=2E+2f.
\]

The negative section \(E=V(A)\) maps to the simple directrix

\[
M=V(x_0,x_3),
\]

whereas \(D\) maps two to one to the double directrix \(V(x_1,x_2)\).
The two conductor branch points are

\[
q_0=(B=v_1=0),\qquad q_\infty=(B=v_0=0).
\]

Use dual coordinates \([a:b:c:d]\), so that the covector represents the plane

\[
a x_0+b x_1+c x_2+d x_3=0.
\]

The letters \(c\) in a dual coordinate and \(C\) for the curve have different
roles. A Gauss value below is a conormal covector, not an ambient normal vector.

## 2. The Gauss map on the actual normalization

The hypersurface Gauss system consists of the four first partial derivatives of

\[
F=x_0x_2^2-x_1^2x_3.
\]

Pulling that system to \(T\) gives

\[
[B^2v_1^2:-2ABv_0v_1^2:2ABv_0^2v_1:-B^2v_0^2].
\]

Its common divisorial factor is precisely the conductor equation \(B\).
Consequently the rational map extending the Gauss map from \(R_{\rm sm}\) is

\[
\gamma_T:T\dashrightarrow(\mathbf P^3)^\vee,\qquad
[Bv_1^2:-2Av_0v_1^2:2Av_0^2v_1:-Bv_0^2].
\tag{2}
\]

Every entry is a section of

\[
L=2H-D=E+3f.
\tag{3}
\]

This line-bundle description explains the conductor correction to the usual
gradient system; it is more informative than merely cancelling a factor on the
smooth locus.

The base scheme of (2) is exactly the reduced pair \(q_0\sqcup q_\infty\).
For example on \(A=v_0=1\), with \(r=B/A, w=v_1/v_0\),

\[
\nu=[1:r:rw:w^2],\qquad
\gamma_T=[rw^2:-2w^2:2w:-r],
\tag{4}
\]

whose base ideal at \(q_0\) is \((r,w)\). The reversed chart gives the other
reduced base point. Everywhere else either \(B\ne0\), or \(A v_0v_1\ne0\)
on \(D\setminus\{q_0,q_\infty\}\), so there are no further base points or
base divisors.

Let

\[
\pi:S=\operatorname{Bl}_{q_0,q_\infty}T\longrightarrow T
\]

have exceptional curves \(e_0,e_\infty\). The resolved Gauss map is the morphism
given by

\[
\mathcal M=\pi^*(E+3f)-e_0-e_\infty,\qquad \mathcal M^2=3.
\tag{5}
\]

One ordinary blowup at each point suffices: the local generators \((r,w)\)
become invertible, so no infinitely near base point remains.

## 3. The cubic dual and its normalization

The complete dual surface is

\[
\boxed{R^\vee=V(a c^2+b^2d)\subset(\mathbf P^3)^\vee.}
\tag{6}
\]

Indeed (2) satisfies this equation. The equation is irreducible: regarded as a
polynomial in \(a\), it is primitive over \(k[b,c,d]\), and \(c^2\) and \(b^2d\)
have no common factor. On the dense open \(w\ne0,\infty\), the ratio

\[
w=-b/c
\]

recovers the ruling, and (4) then recovers \(r\). Thus the Gauss image has
dimension two and is dense in (6); its closure is that cubic surface. The
surface is not developable in characteristic zero. Its Gauss map is birational
but is neither finite nor everywhere defined on its normalization before the
two blowups.

There is a projective linear isomorphism \(R^\vee\simeq R\), for example

\[
[a:b:c:d]\longmapsto[a:b:c:-d].
\]

This is a statement about these two projective cubic surfaces. It is not a
polarity construction identifying the conormal normalization of the quartic
with its quadric.

For clarity the finite normalization of \(R^\vee\) can be written in the
same ruling convention:

\[
\nu^\vee:T^\vee=\mathbb F_1\longrightarrow R^\vee,
\quad
[v_0:v_1;A':B']\longmapsto
[A'v_1^2:-B'v_1:B'v_0:-A'v_0^2].
\tag{7}
\]

It is obtained from (1) by projective coordinate changes in the source base
and target, so the retained finite-normalization result applies. Its negative
section is \(E^\vee=V(A')\); its conductor is \(D^\vee=V(B')\).

The Gauss map lifts birationally to \(T^\vee\), over the *same* base

\[
[v_0:v_1;A:B]\dashrightarrow
[v_0:v_1;A':B']=[v_0:v_1;B:2A v_0v_1].
\tag{8}
\]

This formula is interpreted in local trivializations; it is not a claim that
the two displayed fiber coordinates have the same Cox degree on \(T\).
The corresponding intrinsic factorization is

\[
T\ \xleftarrow{\ \pi\ }\ S\ \xrightarrow{\ \rho\ }\ T^\vee
\ \xrightarrow{\ \nu^\vee\ }\ R^\vee.
\tag{9}
\]

Here \(\rho\) contracts exactly the strict transforms of the two endpoint
fibers \(f_0,f_\infty\). This follows locally from (8): near \(q_0\) the
fiber transformation is \([A':B']=[r:2w]\), resolved by the blowup of

\[
(r,w),
\]

and the strict transform of \(w=0\) is contracted to \([A':B']=[1:0]\).
The exceptional curve maps isomorphically to the new ruling fiber.
The reversed chart is identical. Away from those two fibers (8) is an
isomorphism. Thus these are precisely two elementary transformations.

Their effect on the marked sections is especially simple:

\[
D\longmapsto E^\vee,\qquad E\longmapsto D^\vee.
\tag{10}
\]

The first section has square \(1-2=-1\) after the blowups; it does not meet
the strict fibers being contracted. The second has square \(-1+2=1\)
after contracting those two fibers. These intersection computations also
identify the resulting ruled surface as \(\mathbb F_1\). The Gauss comparison
therefore exchanges the two directing sections with their marked roles
retained; it is not an isomorphism of the original marked ruled surfaces.

The singular support and Jacobian singular scheme of the dual are

\[
\operatorname{Sing}(R^\vee)_{\rm red}=V(b,c),
\]

\[
I_{\operatorname{Sing}(R^\vee)}=(c^2,bd,ac,b^2).
\tag{11}
\]

In (11) we give generators of the Jacobian ideal **sheaf**. The saturated
homogeneous ideal defining that sheaf is

\[
(b^2,bc,c^2,ac,bd)
=(b,c)\cap(c,d,b^2)\cap(a,b,c^2).
\tag{11a}
\]

Indeed the product of \(bc\) with every homogeneous coordinate lies in
(11); the displayed primary decomposition proves saturation and equality
of the resulting sheaf. Thus this is a reduced double-directrix line
with an embedded length-one addition at each pinch endpoint, rather
than a generically doubled singular line. On \(a=1\), for example, the
local ideal is \((c,b^2,bd)\); the nilpotent class of \(b\) is supported
only at \(d=0\).

The conductor section \(D^\vee\to V(b,c)\) has degree two, ramified at

\[
[1:0:0:0],\qquad[0:0:0:1].
\]

The corresponding two image points are pinch points. At a general point of
the double line the two completed branches meet transversely. These are the
same local types as for \(R\), transported by the displayed projective
isomorphism, with their scheme structures explicitly supplied by (11).

## 4. Ordinary and limiting Gauss values are different

For a general ruling \(w\), the Gauss map varies along the ruling and maps it
birationally to a ruling of \(R^\vee\). The endpoint fibers are exceptional:
all smooth points of \(f_0\setminus D\) have tangent plane \(x_3=0\), and all
smooth points of \(f_\infty\setminus D\) have tangent plane \(x_0=0\).
These are the two contracted fibers in (9).

On the source negative section \(E\), which lies over smooth points of \(R\),
the Gauss map is

\[
[v_0:v_1]\longmapsto[v_1^2:0:0:-v_0^2].
\]

It is degree two onto the dual double line. Thus a general point of the
singular line in \(R^\vee\) has two actual smooth contact points on the
simple directrix of \(R\).

On the source conductor \(D\setminus\{q_0,q_\infty\}\), the extension (2)
has value

\[
[0:-v_1:v_0:0],
\]

the dual simple directrix. These are limiting tangent planes along a branch
over the source double line; the source points themselves are singular in
 \(R\).

Finally the exceptional curve over \(q_0\) fills the dual line

\[
\ell_0=V(a,b),
\]

and that over \(q_\infty\) fills

\[
\ell_\infty=V(c,d).
\tag{12}
\]

Apart from \([0:0:0:1]\in\ell_0\) and \([1:0:0:0]\in\ell_\infty\),
these endpoint-pencil planes are not Gauss values at any smooth point of
 \(R\).

They belong to the dual because the dual is the *closure* of the Gauss image.
For example in (4), a Gauss value with \(a=b=0\) requires \(w=0\) away from
the conductor, and then also \(c=0\). This difference matters in any
interpretation of intersections of dual varieties.

## 5. The osculating curve and the residual flag

There is an intrinsic residual interpretation of the **whole** dual
normalization, not just the osculating curve. Let

\[
L_\iota=\{p+\iota(p):p\in C\}\subset\operatorname{Sym}^2C
\]

be the projective line of even binary quadratics, with its endpoint
divisors \(2p_0,2p_\infty\) included. Let

\[
J=\operatorname{pr}_1^{-1}(L_\iota)\subset\mathcal I.
\tag{12a}
\]

By the universal residual construction of the flag, a fiber of \(J\)
parametrizes the planes containing the secant line of its degree-two
divisor. Those are exactly the ruling lines of \(R\), including its
two endpoint tangent trisecants. For a ruling parameter
\([v_0:v_1]\) and divisor \(D=V(v_0t^2-v_1s^2)\), the plane
covectors form the rank-two kernel of restriction of the marked linear
system \(V\) to \(D\). As a subbundle of
\(V\otimes\mathcal O_{\mathbf P^1}\), it is generated by

\[
(v_1^2,0,0,-v_0^2),\qquad(0,-v_1,v_0,0),
\]

with respective summands \(\mathcal O(-2)\) and \(\mathcal O(-1)\).
Thus \(J\cong\mathbb F_1\), and its plane map is exactly (7). In
particular

\[
\boxed{T^\vee=J=\mathcal I|_{L_\iota}}
\tag{12b}
\]

is a natural identification for the marked embedding and involution.
This proof includes nonreduced endpoint divisors: restriction to \(2p_0\)
means containing the limiting tangent line, so the whole endpoint pencil
is retained, not just its generic osculating limit.

The primal surface \(T\) is the corresponding **point-on-ruling** bundle;
the dual normalization \(J\) is the **plane-through-ruling** bundle. A
tangent plane to a ruled surface contains its ruling, so its Gauss map
is naturally a rational map from the first bundle to the second over
the same base. Equations (8)–(10) describe the two special fibers at
which this fiberwise projectivity degenerates. This is the geometric
source of the two elementary transformations.

On \(\widehat C\), put \(w=u^2, r=u\). Equation (4) becomes

\[
[u^5:-2u^4:2u^2:-u]
=[-u^4:2u^3:-2u:1],
\tag{13}
\]

away from the endpoints. The right side extends regularly to both endpoints
and is the osculating-plane quartic. Hence the Gauss map of the cubic
restricts along the marked quartic to its osculating-plane map, with precisely
the limiting endpoint planes required by the global extension. This explains
the relation through the scroll, rather than equating arbitrary tangent and
osculating planes.

There is a particularly small residual construction behind (13). Let

\[
\jmath:C\longrightarrow\mathcal I,\qquad
p\longmapsto(2p,p+\iota(p)),\quad\iota(u)=-u.
\tag{14}
\]

The total divisor is \(3p+\iota(p)\), so it belongs to the marked hyperplane
system and its image in dual space is (13). The second divisor in (14)
parametrizes precisely the ruling lines of the cubic. Residual swapping gives

\[
\tau\jmath(p)=(p+\iota(p),2p),
\]

which has the *same plane* but a different first secant divisor. Thus the
osculating residual involution on points, the paired-secant ruling, and
residual swap on the flag arise from one residual divisor identity, while
remaining genuinely different maps. At the two endpoints these pairs
coincide on the swap fixed locus; generically they do not.

Under the two elementary transformations the strict osculating bisection

\[
\widehat C\subset T
\]

has image of class \(2E^\vee+2f\) on \(T^\vee\), again a smooth bisection.
For direct verification, (8) sends \(B^2=A^2v_0v_1\) to

\[
(B')^2=4(A')^2v_0v_1.
\tag{15}
\]

Its endpoint behavior is resolved by (9). The divisor-class assertion follows
also by using its ruling degree two and degree four under (7).

## 6. The full scheme intersection with the dual quadric

The dual quadric is

\[
Q^\vee=V(ad-bc).
\]

On its Segre model

\[
[a:b:c:d]=[p r:p s:q r:q s],
\]

the cubic equation (6) restricts exactly to

\[
p q(qr^3+ps^3).
\tag{16}
\]

Therefore the **scheme-theoretic** intersection, viewed as a Cartier divisor
on the smooth quadric, is

\[
\boxed{R^\vee\cap Q^\vee=\ell_0+\ell_\infty+K,}
\tag{17}
\]

where each component occurs once and

\[
K=V(qr^3+ps^3)\subset Q^\vee
\]

is a smooth rational quartic of class \((1,3)\). The equation is linear in

\[
[p:q]
\]

with coefficients \(s^3,r^3\) that do not vanish simultaneously, so it is
the graph of a degree-three morphism and is smooth. A convenient
parametrization is

\[
K:[s:t]\longmapsto[-t^4:s t^3:-s^3t:s^4].
\tag{18}
\]

The two lines are disjoint and belong to the same ruling of the quadric.
Each meets \(K\) in a length-three divisor concentrated at an endpoint.
Consequently (17) is reduced but has nontransverse intersections there.
Factorization (16), not a support count, proves that no embedded
zero-dimensional correction is present in this complete intersection on the
quadric.

The Cartier pullback to the dual normalization has the parallel form

\[
(\nu^\vee)^*Q^\vee=f_0+f_\infty+\widehat K,\qquad
\widehat K=V((B')^2-(A')^2v_0v_1).
\tag{17a}
\]

Indeed substituting (7) into \(ad-bc\) gives
\(v_0v_1((B')^2-(A')^2v_0v_1)\).
The osculating bisection (15) instead has coefficient \(4\).
Thus the dual operation exchanges which of these marked bisections has the
same incidence with its quadric as the primal quartic: the source quartic
has coefficient \(1\) and maps to the osculating bisection with coefficient
\(4\), whereas the source bisection \(B^2=4A^2v_0v_1\) maps to
\(\widehat K\) with coefficient \(1\). This is an equality of explicit
marked constructions; equality of their divisor classes alone would not
identify them.

The curve \(K\) is different from both the osculating quartic and the curve

\[
\sigma_Q(C):u\longmapsto[u^4:-u^3:-u:1]
\]

of quadric-tangent planes along \(C\). These are different marked curves and are not interchangeable traces.

For a general plane on \(K\), there are actual contacts on both surfaces,
at *different* points. Taking \(r=2u, w=u^2\) in (4) gives

\[
x_R=[1:2u:2u^3:u^4]\in R_{\rm sm},
\quad H=[-u^4:u^3:-u:1]\in K.
\]

The pole of that plane under the quadric polarity is

\[
x_Q=[1:u:-u^3:-u^4]\in Q.
\tag{19}
\]

For \(u\ne0,\infty\), these points are different and neither lies on
the common quartic \(C\). In particular (17) is not the locus of common
Gauss planes at the same point of \(R\cap Q\).

In fact there is **no** point at which both \(R\) and \(Q\) are smooth and
have the same tangent plane. To see this, the retained Cartier identity

\[
R|_Q=C+L_0+L_\infty
\]

exhausts their common support. At \(c(u)\), \(u\ne0,\infty\), the planes

\[
[-u^4:2u^3:-2u:1],\qquad[u^4:-u^3:-u:1]
\]

cannot coincide in characteristic zero. At a smooth point

\[
[A:B:0:0]\in L_0,
\]

one has \(B\ne0\); the tangent planes are respectively \([0:0:0:1]\)
and \([0:0:-B:A]\), again different. The reversed argument applies on

\[
L_\infty.
\]

The remaining endpoints are singular on \(R\), so they cannot supply a
common smooth contact point. A general plane of either line in (12) is
therefore a true tangent plane to \(Q\) and only a limiting tangent plane
to \(R\) at a pinch point, exactly as Section 4 describes.

## 7. Evidence and review boundary

The [scoped verifier](../computations/verify_cubic_scroll_gauss_dual_2026_10_24.py)
checks the gradient pullback, conductor factor, dual equation, bidual
identity, local reduced base ideals, Segre factorization, three marked
quartic substitutions, and their distinct contact-point example. Its
[JSON output](../computations/cubic_scroll_gauss_dual_2026_10_24.json)
records these exact identities. Run

```
/tmp/stci-z4-env/bin/python research/computations/verify_cubic_scroll_gauss_dual_2026_10_24.py
```

from the repository root. Computation verifies the displayed identities;
the global resolution, completeness of the dual, normalization, and
scheme-divisor conclusions use the proofs above.

The companion independent audit reconstructs the new Gauss and dual
claims and checks endpoint, section-class, and common-contact distinctions.
Retained inputs are the exact fixed-scroll normalization and divisor
calculations already reviewed in the merged October 24 package. No
accepted STCI result, conormal-splitting proof, or arbitrary-curve
classification is invoked or rerun. These conclusions remain provisional
research evidence, without canonical promotion.

The behavior in characteristic two is **not** covered: division by two,
the nonzero middle gradient coordinates, the two elementary-transform
formula, and the ordinary separable Gauss interpretation require the
stated characteristic-zero hypothesis. The monomial surface still
exists there. In fact its characteristic-two gradient is

\[
[x_2^2:0:0:x_1^2],
\]

so its actual dual is the line \(V\(b,c\)\). This is not the cubic
\(V\(ac^2+b^2d\)\) obtained by specializing the characteristic-zero dual
equation. Taking the reduced Gauss image closure does not commute with
that specialization. No characteristic-two version of (6)–(10) is
asserted.
