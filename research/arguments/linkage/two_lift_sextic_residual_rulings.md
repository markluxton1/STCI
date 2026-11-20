# Residual-ruling calculations for two-lift sextics

**Scope and role.** These are the repeated-fiber and marked-endpoint
lemmas in the [two-lift sextic theorem](two_lift_sextic_exclusion.md#supported-exclusion-and-proof-map).
Work over an algebraically closed field of characteristic zero, with
\(C=[s^4:s^3t:st^3:t^4]\), \(q=x_0x_3-x_1x_2\),
\(r=2x_1x_2-x_0x_3\), and \(X=V(z^2-r)\).
Use the actual integral norm source
\(F=P^2-rQ^2\), \(\deg P=3\), \(\deg Q=2\),
\(P|_C=Q|_C=0\). On the fixed covering quadric \(X\), the signed
cubic contains the two lifted quartics \(D,D'\). The residual divisor of
\(P\) on \(V(q)\) is two ruling fibers, allowing repetition.

**Conclusions and dependencies.** The doubled unmarked and distinct marked
patterns have no mate under the normality hypothesis of their lemmas;
[actual inverse support and normalization](two_lift_sextic_exclusion.md#removing-normality-inverse-support-and-the-actual-normalization)
remove that hypothesis. The doubled marked pattern is first excluded
for normal cubics, then by the explicit normalized calculation at the end
of this file without normality. These four computations exhaust the
patterns remaining after the [transverse unmarked case](two_lift_sextic_exclusion.md#transverse-residual-sextics-higher-a_n-do-not-suffice).
The [shared-node and numerical-correction setup](two_lift_sextic_exclusion.md#nodal-signed-cubics-the-correction-is-insufficient)
and the [K3 smoothing rank bound](two_lift_sextic_exclusion.md#transverse-residual-sextics-higher-a_n-do-not-suffice)
are used below with their stated local hypotheses. Each limitation to a
normal case is the scope of that intermediate lemma.

**Review provenance.** The relocated proofs retain the scopes assessed in the
[consolidated review of PR #167](https://github.com/markluxton1/STCI/pull/167#issuecomment-7043663699),
reviewed head `4d1b03cdf4671a7b1e987cb641a3509de23e9a5c`. The present
organization separates those existing arguments; it does not extend their
source hypotheses or claim a fresh rerun of historical computations.

## Doubled unmarked ruling: a conic bounds the correction

For the two-lift split sextic, the degree-three ruling map of
\(C\) on \(V(q)\) is \([s^3:t^3]\), so a reduced unmarked
ruling meets \(C\) at three distinct points in characteristic
zero. The only possibility not covered by the transverse
result when the residual divisor avoids the endpoints is
a doubled unmarked ruling \(2L\). In this case too there is
no mate in any degree if the signed cubic is normal.
No Du Val hypothesis is needed, including along the lifts.

Write \(T\subset X\) for the pullback of \(V(q)\). On a ruling
\(L\) away from the endpoints, Segre coordinates have the form
\((\alpha u,\alpha v,\beta u,\beta v)\) with \(\alpha\beta\ne0\).
The branch section restricts to \(\alpha\beta uv\). Thus the
pullback \(R\) of \(L\) is a smooth conic, and \(T\) is smooth
along it: at its two branch points the branch equation has
a simple zero on \(L\), so it cuts the downstairs quadric
transversely there, and elsewhere the cover is étale.
The signed cubic cuts \(D+D'+2R\) on \(T\) near \(R\).
Its derivative along \(R\) is therefore zero in the
cotangent bundle of \(T\), and its derivative normal to \(T\)
defines a section of
\[
N^*_{T/X}|_R\otimes\mathcal O_R(3)=\mathcal O_R(1).
\]
This line bundle has degree two on the conic. The zeros
are exactly the singular points of the signed cubic along
\(R\); the section is nonzero by normality. All singularities
along the lifts must lie among these zeros, since away from
\(R\) the signed cubic cuts each lift simply on \(T\) at
unmarked points, and the marked endpoints are smooth by
the [transverse-slice tangent-plane argument](two_lift_sextic_exclusion.md#transverse-residual-sextics-higher-a_n-do-not-suffice).

At a singular point of a lift use \(w=q\) and choose
coordinates \(x,y\) on \(w=0\) in which the lift is \(x=0\)
and the conic is \(y=0\). They meet transversely since
the ruling is unmarked. The cubic has local equation
\(xy^2+wA(x,y,w)\) after multiplication by a unit, and the
conormal section on the conic is represented by \(A(x,0,0)\).
At a simple zero, \(A_x(0)\ne0\); the Hessian has rank two
and the tangent of \(R\) is outside its radical. The point
is therefore of type \(A_{d-1}\), and \(R\) meets an end of the
exceptional chain. Indeed in a rank-two normal form
\(uv=\xi^d\) a smooth curve with tangent outside the radical
has either \(u\) or \(v\) of order one, which gives the end
intersection in the toric resolution. A smooth marked lift
through this point meets exactly one exceptional curve,
transversely: choose a local function restricting to order
one on it; every exceptional component has order at least
one in the pullback of that function. In the chain
discriminant group \(\mathbf Z/d\), incidence at vertex
\(j\) has class \(j\) up to simultaneous sign (the relations
are \(2e_j=e_{j-1}+e_{j+1}\) with zero boundary values).
The Cartier divisor \(w=0\) gives the local relation
\([D]+2[R]=0\), with \(D\) denoting the lift present there.
Thus the marked lift meets vertex \(2\) or \(d-2\), and
its diagonal correction is \(2(d-2)/d<2\).

Let \(A_0,B_0\) denote the correction sums for the two
lifts. Their endpoints are smooth, so the same separate
intersection calculation gives
\(1/(6-A_0)+1/(6-B_0)=3/4\).
Two simple zeros of the conormal section yield total
correction strictly below four. For nonnegative sums
with that budget the left side is at most
\(1/(6-4)+1/6=2/3\), by convexity. If the section
instead has a double zero, it can contribute at only one
marked point, and the required correction there is
\(30/7\). At that zero \(A_x(0)=0\). If \(A_y(0)\ne0\),
the tangent of the marked lift itself is outside the
Hessian radical, so its end correction is below one.
The double-zero case can in fact be closed without the local
Du Val assumption. If \(A_x(0)=A_y(0)=0\) but \(A_w(0)\ne0\),
the singularity is necessarily \(D_5\). Indeed the conormal
section has a zero of order exactly two, so the coefficient
of \(x^2\) in \(A(x,0,0)\) is nonzero. With weights
\((2,3,4)\) on \((x,y,w)\), the initial equation is
\(a w^2+c x^2w+xy^2\), with \(ac\ne0\). Completing the
square gives \(w'^2+xy^2+c'x^4\), \(c'\ne0\). This weighted
initial form determines the formal type: its Jacobian
quotient has basis \(1,x,x^2,x^3,y\), all of weight at
most six, so terms of weight above eight can be removed
successively by coordinate changes of strictly increasing
weight. The \(D_5\) Cartan determinant is four; the required
fraction \(30/7\) is impossible.

If \(A_x(0)=A_y(0)=A_w(0)=0\), the surface has
multiplicity three. In the blowup chart along the marked
lift, write \(x=yX_1,w=yW_1\). The strict equation is
\[
X_1+W_1\,A(yX_1,y,yW_1)/y^2=0.
\]
It is smooth where the strict lift hits the exceptional
divisor and there \(W_1=0\) cuts out the strict lift,
transversely to the exceptional divisor \(y=0\). The
strict conic lies in a different tangent direction. A
resolution elsewhere on this blowup need not modify this
neighborhood. The discrepancy at the exceptional component
met by the lift is \(-1\): the ambient volume form gains
\(y^2\) in the blowup, while its defining equation loses
\(y^3\), giving the factor \(y^{-1}\) in the residue.
Since the signed cubic has trivial canonical class and
this is the only possible singular point of either lift,
adjunction gives self-intersection \(-1\) for the strict
lift through the point rather than \(-2\).

There is also an upper bound on its numerical-pullback
correction. Locally \(\operatorname{div}(w)=D+2R\).
On a resolution of the normal surface the numerical
pullbacks of these two effective curves have nonnegative
exceptional coefficients: their coefficient vectors solve
the negative definite intersection systems with
nonnegative incidence vectors, and the inverse of the
negative exceptional matrix is nonnegative. The
exceptional part of the actual pullback of \(w\) is their
weighted sum. It meets the strict marked lift with
multiplicity exactly one, since \(w=yW_1\) in the chart
and the strict conic is disjoint there. Thus the marked
curve's own numerical correction is at most one. Together
with the change in adjunction, this gives an effective
self-correction of at most two relative to the smooth
self-intersection \(-2\). The same two separate mate
intersections, using this effective correction on the
singular side and zero on the other, would require
\(30/7\), again impossible.

A residual ruling through a marked endpoint lies in the branch
quadric; the conic derivative argument does not apply. The
[distinct marked rulings](#distinct-residual-rulings-through-marked-points)
instead use the shared endpoint geometry.

## Distinct residual rulings through marked points

For a two-lift split sextic with normal signed cubic in
characteristic zero, suppose the residual ruling divisor
has two distinct fibers. At a marked point belonging to
one such fiber, use coordinates
\(t=x_1/x_0,\ v=x_2/x_0,\ q=x_3/x_0-tv=tv-z^2\) on the
first chart, and reversed coordinates at the other point.
The signed cubic has equation
\[
v(v-t^3)a(v)+(tv-z^2)\bigl(L(t,v,tv-z^2)+cz\bigr),
\qquad a(0)c\ne0.
\]
Indeed its restriction to the downstairs quadric consists
of \(C\) and the two residual rulings, with just a simple
residual fiber \(v=0\) at this point. The two lifts are
\(v=t^3,\ z=\pm t^2\). If \(L(0)\ne0\), the quadratic
part has rank three, giving the [shared node](two_lift_sextic_exclusion.md#nodal-signed-cubics-the-correction-is-insufficient).

If \(L(0)=0\) but \(\ell=L_t(0)\ne0\), the following local
resolution gives both the type and the actual incidences.
In the first blowup chart put \(V=v/t,\ Z=z/t\). The
strict equation is
\[
 V(V-t^2)a(tV)+t(V-Z^2)
    \bigl(\ell+cZ+L_v(0)V+O(t)\bigr).
\]
The reduced exceptional line is \(t=V=0\); its singular
points are \(Z=0\) and \(Z=-\ell/c\), from the derivative
\(-Z^2(\ell+cZ)\). There is no singularity at infinity,
where in the \(z\)-chart the remaining derivative is
\(-c\). The simple root is a node, by its nonzero
\(t,Z\) pairing and squared \(V\) term. At zero the
Hessian in \((V,t)\) is nondegenerate. Splitting over
\(k[[Z]]\) gives critical coordinates starting
\(V=Z^2,t=-2a(0)Z^2/\ell\) and critical value starting
\(a(0)Z^4\), so the point is \(A_3\). The old exceptional
line has both split coordinates of order at least two;
their product has order four, so their orders are exactly
\((2,2)\) and the line meets the middle exceptional curve.
The two marked lifts \((V,t,Z)=(t^2,t,\pm t)\) point to the
same nonkernel isotropic axis. Their order-one split
coordinate divided by \(Z\) has opposite nonzero values,
so they meet the same end of the chain at distinct points.
The first blowup is crepant by multiplicity two, and the
resulting graph is \(D_5\): the old line joins the middle
of the \(A_3\) chain to the additional node exceptional.
The two lifts meet the same short tip. The inverse Cartan
diagonal at that tip is \(5/4\).

In the numerical intersection matrix of the two original
lifts, relative to a smooth marked endpoint, a shared node
adds \(1/2\) to each self-intersection and subtracts
\(1/2\) from their mutual intersection. The shared
\(D_5\) just computed adds \(5/4\) to each self-intersection
and subtracts \(3/4\) from the mutual intersection: their
strict transforms no longer meet over the point, and the
common tip contributes \(5/4\) to their numerical product.

The remaining simple endpoint case, \(L(0)=L_t(0)=0\),
has a different resolution but a controlled numerical
correction. Blow up with weights \((1,2,3)\) on \((t,z,v)\).
The weight-six initial equation, in the weight-one chart
\(z=t^2Z,\ v=t^3V\), is
\[
a(0)V(V-1)+(\gamma+cZ)(V-Z^2)=0.
\]
Here \(\gamma\) is the coefficient of \(t^2\) in \(L(t,0,0)\).
The exceptional curve \(E\) is integral: the quadratic in
\(V\) has discriminant a cubic in \(Z\) with nonzero
cubic coefficient, not a square, and the homogeneous form
has no component in \(t=0\). The partial strict surface is
normal locally over the point: the weighted chart covers
are hypersurfaces, smooth at the generic point of
their reduced exceptional curve, and possible singularities
there are isolated; taking finite chart quotients preserves
normality. The tautological restriction is
\(\mathcal O_E(E)=\mathcal O_E(-1)\) in the rational divisor
sense. The degree of \(\mathcal O_E(1)\) is one: the
weight-one coordinate vanishes at the single point
\(a(0)v^2=cz^3\) of \(\mathbf P(2,3)\), where both
coordinates are nonzero, the stabilizer is trivial,
and the intersection is transverse. Thus \(E^2=-1\).

Both lifts meet \(E\) transversely at distinct smooth
points \((V,Z)=(1,\pm1)\): the \(V,Z\) derivatives are \(a(0)+\gamma\pm c\)
and \(\mp2(\gamma\pm c)\), which cannot both vanish,
and \(t\) is a parameter
on either lift. Resolve any other points without modifying
these neighborhoods. The discrepancy on the component
met by the lifts is \(-1\), since the ambient volume
form in this chart acquires \(t^5\) and the defining
equation contributes \(t^6\) in the residue. Adjunction
therefore adds one to each strict self-intersection.
The numerical pullback over this endpoint adds \(E\) to
either strict lift on the partial surface, since each
meets \(E\) once and \(E^2=-1\); further resolution
does not change the numerical pairing. Thus the
numerical corrections from the initial endpoint,
relative to a smooth endpoint, are **\(+2\) on both
self-intersections and \(-1\) on the mutual intersection**:
the strict transforms do not meet, and the contracted
curve contributes one to their numerical product.

These three local cases suffice for all distinct residual
rulings. If both rulings are marked, the sum of one
numerical self-intersection and the mutual intersection
is at most four: its smooth baseline is two and each
marked contribution adds at most one to that row sum.
The mate would require \(8b\le4(3b/2)\), a contradiction.
If one ruling is marked and one is unmarked, the three
unmarked transverse hits contribute extra self-corrections
\(A,B\ge0\) with \(A+B<3\). Denote by \(u\) the common
numerical self-intersection before those extra corrections
and by \(v_0\) the numerical mutual intersection; the
separate intersections with the mate give
\[
(v_0-u-A)\lambda=(v_0-u-B)\mu=(3v_0/2-4)b.
\]
For a shared node, \((u,v_0)=(-3/2,7/2)\), and this
requires \(1/(5-A)+1/(5-B)=6/5\), whereas the left side
is below \(1/2+1/5\). For the shared \(D_5\),
\((u,v_0)=(-3/4,13/4)\), so the required value of
\(1/(4-A)+1/(4-B)\) is \(12/7\), but the left side is
below \(1+1/4\). Both bounds use convexity and the
total budget three.

In the weight-six case \((u,v_0)=(0,3)\), the reciprocal
sum \(1/(3-A)+1/(3-B)\) would have to be three.
If at most two unmarked singular hits belong to either
lift, the largest allocation is \((2,1)\) and the sum
is below \(1+1/2\). Otherwise all three lie on one
lift and the other has no correction. Writing
\(d_i=n_i+1\) for the three end incidences, the equality
requires \(\sum 1/d_i=3/8\). The K3 smoothing bound
on the three isolated unmarked \(A_{n_i}\) points
alone gives \(\sum d_i\le22\), irrespective of the
marked singularity. Hence \(\sum 1/d_i\ge9/22>3/8\),
again impossible. A [doubled marked ruling](#doubled-marked-ruling-closure-for-normal-signed-cubics)
requires the separate argument below, not a degenerate simple endpoint.

## Doubled marked ruling: closure for normal signed cubics

The remaining residual divisor is a doubled marked ruling.
In this case too, an integral two-lift split sextic with
normal signed cubic in characteristic zero has no mate
in any degree.

For the marked ruling in the first affine chart, write the
downstairs quadric in Segre form
\[
(x_0,x_1,x_2,x_3)=(A u,A v_0,B u,B v_0).
\]
The quartic is \(B u^3-A v_0^3=0\), and the ruling in
question is \(B=0\). The cubic
\(x_2^3-x_1x_3^2=B^2(Bu^3-Av_0^3)\) restricts to the exact
divisor \(C+2L\) on the quadric. Thus the actual \(P\)
in the norm representation is a nonzero multiple of this
cubic plus \(q\) times a linear form. In cover coordinates
\(t=x_1/x_0,\ v=x_2/x_0,\ q=tv-z^2\), the signed cubic
has equation
\[
a v^2(v-t^3)+(tv-z^2)\bigl(L(t,v,tv-z^2)+cz\bigr),
\qquad ac\ne0,
\]
and along the reduced inverse image of the marked ruling,
\(L(t,0,0)=L_0+\ell t\). Indeed
\(v^3-t(x_3/x_0)^2=v^2(v-t^3)-tq(2tv+q)\);
the added \(q\)-coefficient vanishes on that line.

If \(L_0=\ell=0\), all first derivatives of the signed
equation vanish along \(v=z=0\), a curve, contradicting
normality of the surface. If \(L_0\ne0\), the marked point
is a shared node, since the quadratic is
\(L_0(tv-z^2)\). It adds zero to each numerical row sum
(self plus mutual intersection), by the [shared-node calculation](two_lift_sextic_exclusion.md#nodal-signed-cubics-the-correction-is-insufficient). It remains to
treat \(L_0=0,\ell\ne0\).

At this point the surface has multiplicity three. In the
ordinary blowup chart \(v=tV,\ z=tZ\), its strict equation is
\[
aV^2(V-t^2)+(V-Z^2)
       \bigl(\ell+L_v(0)V+cZ+O(t)\bigr).
\]
The surface is smooth at the common marked point of the
strict lifts, by the \(V\)-derivative \(\ell\). The two
strict lifts are \(V=t^2, Z=\pm t\); in the local surface
coordinates \(t,Z\) they meet with length one, and each
meets the same exceptional component \(t=0\) transversely
once. Resolve elsewhere without modifying this
neighborhood. The discrepancy at the component met
by the lifts is \(-1\), since the ambient volume in the
ordinary threefold blowup gains \(t^2\) and the equation
contributes \(t^3\) in the residue. Adjunction therefore
adds one to each strict self-intersection, while the
strict mutual intersection loses one at this endpoint.

Let \(e\) be their common exceptional incidence vector
on a resolution over this point. If \(M\) is the negative
of the exceptional intersection matrix, all three
numerical corrections (two self and one mutual) at
this point are \(s=e^{\mathsf T}M^{-1}e\). To bound
\(s\), use the actual Cartier divisor \(q=0\) on the
signed surface, which has \(D,D'\) each with
multiplicity one and an effective residual divisor.
In fact the reduced inverse ruling occurs with
multiplicity four: off the endpoint, \(q=0\) gives
\(v=z^2/t\), and the factor \(v^2\) has order four.
The exceptional part of the pullback of \(q\) is the
sum of the numerical exceptional parts for these
effective curves. All their exceptional coefficients
are nonnegative by inverse-matrix positivity. In
the blowup chart \(q=t^2(V-Z^2)\), and \(V-Z^2\) does
not vanish identically on the local exceptional component:
setting \(V=Z^2\) at \(t=0\) leaves \(aZ^6\) in the strict
equation. Thus the exceptional part of the pullback
meets either strict lift with multiplicity exactly two
there. The two marked curves alone contribute \(2s\)
to that intersection, so \(s\le1\).

The other endpoint is smooth and there are no unmarked
residual hits. Each numerical row sum is therefore
at most its smooth value two plus
\((1+s)+(-1+s)\le2\), hence at most four. Intersecting
the mate with the sum of the two lifts would give
\(8b\le4(3b/2)\), a contradiction. This also covers the
shared node case, whose correction is smaller. The other
marked ruling is the reversed chart.

Combining the two distinct and two doubled patterns proves the
normal-signed-cubic intermediate case in all mate degrees. The
[inverse-support argument](two_lift_sextic_exclusion.md#removing-normality-inverse-support-and-the-actual-normalization)
and the normalized doubled marked calculation below remove normality.
One-lift norms and higher-degree two-lift carriers retain their separate scopes.

## Normalizing the doubled marked ruling

The last case without normality is a doubled marked
residual ruling with \(L_0=\ell=0\) in the actual cubic
representative above. The two-lift support makes its
nonnormality tractable: after the ordinary blowup, both
lifted quartics belong to the same local sheet of the
normalization, although the other sheet is also present.

Keep the ordinary \(t\)-chart \(v=tV,z=tZ\) of the blowup,
and write the strict equation as
\[
aV^2(V-t^2)+(V-Z^2)B(t,V,Z)=0 .
\]
The actual cubic representative gives \(B(t,0,0)=0\)
identically, with transverse linear part at \(t=0\)
equal to \(dV+cZ\), \(c\ne0\). In particular the strict
equation and all its first derivatives vanish all along
\(V=Z=0\). Its transverse Hessian there is nondegenerate,
with quadratic part at \(t=0\) equal to \(V(dV+cZ)\).
Apply the parametric formal splitting lemma over
\(k[[t]]\), retaining that line as the critical section.
The critical value is identically zero; the resulting
equation is a product \(XY\) up to a unit, with
\[
X=V+O((t,V,Z)^2),\qquad
Y=dV+cZ+O((t,V,Z)^2).
\]
The two marked arcs \(V=t^2, Z=\pm t\) have
\(Y=\pm ct+O(t^2)\), nonzero on either arc. Both must
therefore lie in the sheet \(X=0\). Normalization
commutes with completion here (the local rings are
excellent), splitting the two formal sheets into
smooth planes. In the marked sheet with coordinates
\(t,Y\), the two lifts meet each other with length
one, since the slopes of their \(Y\) coordinates
are opposite and nonzero. Each meets the same
exceptional curve \(t=0\) transversely once. Normalize
the blown-up surface and resolve any remaining
points away from this smooth marked neighborhood;
this is a smooth model of the original normalization.

The rational canonical generator of the original
signed cubic pulls back in this sheet, up to a unit, as
\[
\frac{dt\wedge dY}{tY}.
\]
The factor \(t^{-1}\) is the same blowup residue factor
\(t^2/t^3\) as before, from the ordinary ambient blowup
and multiplicity three. The factor \(Y^{-1}\) is the
residue along the sheet \(X=0\) of the product
equation \(XY=0\). Both pole divisors meet each
strict lift once, because \(t\) and \(Y\) have order
one along those lifts. Elsewhere the original surface
is smooth along the lifted quartics. Thus the
canonical intersection with either strict lift is
\(-2\), and its self-intersection by adjunction is
zero, an increase of two from the smooth marked
baseline. The mutual strict intersection has
decreased by one.

Finally, \(q=t^2(V-Z^2)\). The second factor does not
vanish identically on the exceptional component
met by the lifts: at \(t=0,V=Z^2\) the strict equation
would force \(aZ^6=0\), inconsistent with a curve
on that chart. Hence the exceptional multiplicity
of \(q\) along that component is exactly two. The
actual divisor of \(q\) on the original normalization
contains both lifted curves with multiplicity one
and has effective residual support. Their exceptional
incidence vectors agree, so positivity of the
numerical pullback bounds their common self and
mutual correction \(s\) by \(2s\le2\), as in the
normal triple-point case. The total numerical row
sum is at most
\[
2+(2+s)+(-1+s)\le5 .
\]
The other endpoint is smooth, and there are no
unmarked residual hits. Thus \(8b\le5(3b/2)\),
a contradiction.

Combining the residual patterns, **no integral
two-lift split sextic has a mate of any degree in
characteristic zero**, with no normality assumption
on its signed surface. The scope is the two-lift
degree-six norm case. Endpoint-concentrated one-lift
norms, higher degree, and nonsplit carriers are not
excluded by this classification.
