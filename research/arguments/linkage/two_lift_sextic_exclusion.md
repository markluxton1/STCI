# Two-lift sextics in the fixed quadratic cover

## Supported exclusion and proof map

**Theorem.** Work over an algebraically closed field of characteristic zero.
Let \(C=[s^4:s^3t:st^3:t^4]\), \(r=2x_1x_2-x_0x_3\), and let
\[
 F=P^2-rQ^2
\]
be integral of degree six, with \(\deg P=3\), \(\deg Q=2\) and
\(P|_C=Q|_C=0\). There is no homogeneous form \(G\) of any positive
degree such that \(V(F,G)\) is a proper complete intersection with sole
reduced support \(C\). No normality assumption on the signed cubic is needed.
Here “two-lift” refers to the two lifted quartics on each signed cubic in
the fixed quadratic cover \(X=V(z^2-r)\). It does not refer to a split first
normal cone.

**Proof map.** [Smooth signed surfaces](#two-lift-split-carriers-intersection-on-the-signed-surface)
explain the polarized intersection obstruction in every degree \(2m\).
[Du Val corrections](#required-correction-at-du-val-points) retain the
actual marked incidence. For sextics, \(Q\) is a nonzero multiple of the
unique quadric \(q=x_0x_3-x_1x_2\) through \(C\), and the cubic
restriction to \(V(q)\) consists of \(C\) and a degree-two ruling divisor.
Its exhaustive patterns are two distinct fibers or one doubled fiber,
with each marked or unmarked. The [transverse distinct unmarked case](#transverse-residual-sextics-higher-a_n-do-not-suffice)
is below. The [residual-ruling calculations](two_lift_sextic_residual_rulings.md)
handle doubled unmarked, distinct marked and doubled marked patterns.
[Actual inverse support](#removing-normality-inverse-support-and-the-actual-normalization)
removes normality in the first three patterns, and
[the normalized doubled marked calculation](two_lift_sextic_residual_rulings.md#normalizing-the-doubled-marked-ruling)
finishes the last one. The intermediate normality and ADE hypotheses
below belong to individual lemmas, not to the final theorem.

The [fixed-cover norm theorem](split_carrier_norm_and_conductor.md)
supplies the factorization and distinguishes its one-lift case. The
[one-lift conormal exclusion](one_lift_sextic_conormal_exclusion.md)
has a separate smooth/Du Val hypothesis along its single lift.

**Review provenance.** The relocated proofs retain the scopes assessed in the
[consolidated review of PR #167](https://github.com/markluxton1/STCI/pull/167#issuecomment-7043663699),
reviewed head `4d1b03cdf4671a7b1e987cb641a3509de23e9a5c`. The present
organization separates those existing arguments; it does not extend their
source hypotheses or claim a fresh rerun of historical computations.

## Two-lift split carriers: intersection on the signed surface

The two-lift case also has a global exclusion that does not require
estimating the endpoint conductor. Let \(S_+=V_X(P+zQ)\) be one
integral signed surface of degree \(m\) on the covering quadric,
with \(P|_C=Q|_C=0\). If either signed surface is smooth along
\(D\cup D'\), there is **no mate in any degree**. This is smoothness
of the surface upstairs; the original norm carrier downstairs
is singular along \(C\) in this two-lift case.

Indeed, a hypothetical mate of degree \(b\) would cut on
\(S_+\) an effective Cartier divisor with cycle
\(\lambda D+\mu D'\), with \(\lambda,\mu>0\). Its intersection
with the hyperplane class gives
\(4(\lambda+\mu)=2mb\). Along the two curves adjunction
on \(S_+\) gives \(K_{S_+}=(m-3)H\) and
\[
D^2=(D')^2=10-4m.
\]
The scheme intersection of the two lifts has length two at each
marked point and is empty elsewhere: on the pullback of \(C\)
the local equation is \(z^2=t^4\), and the two ideals
\((z-t^2)\) and \((z+t^2)\) sum to \((z,t^2)\).
Their common scheme does not change when computed inside a
surface containing both curves. Since the curves are Cartier
on the smooth neighborhood of their support, \(D\cdot D'=4\).
Intersecting the mate with \(D+D'\) would therefore give
\[
8b=(\lambda+\mu)(14-4m),\qquad
8-\tfrac m2(14-4m)=2m^2-7m+8>0,
\]
a contradiction. The same argument applies to the other signed
surface by conjugation. Singularities away from the two curves
play no role.

There are actual integral split carriers in this locus in every
even degree \(2m\ge6\), in characteristic zero. The flat
pullback of \(C\) is the reduced union \(D\cup D'\): its algebra
is free over \(C\) locally and generically reduced, so any
nilpotent would be torsion and hence zero. The quartic ideal is
generated in degrees two and three. Thus the system of degree-\(m\)
sections vanishing on the union generates the union's ideal
sheaf for \(m\ge3\), by pulling back those generators and padding
degrees with forms that are nonzero at the point. At a smooth
point of the union, the condition that the section be singular
there imposes two independent linear conditions. As the point
varies in a curve, their incidence cannot dominate the parameter
space. At either of the two marked points the union has a
two-dimensional tangent space in the smooth threefold: locally
the union is cut by a transverse coordinate and \(z^2-t^4\).
So singularity imposes one nontrivial linear condition at each
of these fixed points, also avoidable. Off the union the system
has no base points, and its image has dimension three: multiplying
the fixed containing quadric of \(C\) by all degree-\((m-2)\)
forms downstairs gives a subsystem with three-dimensional image.
Bertini gives an integral general surface. The conditions
\(P\ne0\) and \(Q\ne0\) define a nonempty open since both
\(I_C(m)\) and \(I_C(m-1)\) are nonzero. The signed surfaces
are then distinct, with the same integral image; their norm
is an integral carrier, since over its generic point the cover
is étale and the two factors have multiplicity one.

### Required correction at Du Val points

For a normal signed surface with at worst Du Val singularities
along the two lifts, the same argument quantifies the exact
correction a mate would need. On a resolution crepant near the
lifts, let \(\widetilde D,\widetilde D'\) be their strict
transforms. Each is isomorphic to the corresponding smooth
quartic: the restricted map is proper, birational and has
finite fibers, hence is an isomorphism over a normal curve.
Their self-intersections are still \(10-4m\) by crepancy.
Put \(k=\widetilde D\cdot\widetilde D'\). At a point of the
second strict transform the pullback of the ideal of \(D\)
is contained in the ideal of \(\widetilde D\); restricting
to \(\widetilde D'\cong D'\) therefore gives \(k\le4\).
Write the total pullback of the actual mate divisor as
\(\lambda\widetilde D+\mu\widetilde D'+E_G\).
Intersecting with \(\widetilde D+\widetilde D'\) gives the
required budget
\[
E_G\cdot(\widetilde D+\widetilde D')
=8b-(\lambda+\mu)(10-4m+k)
\ \ge\ b(2m^2-7m+8).
\]
For a signed cubic this is at least \(5b\).
More precisely, at each resolved point let \(A_p\) be the
negative of the exceptional intersection matrix and let
\(x_p,y_p\) be the actual intersection vectors of the two
strict transforms with the exceptional curves. The contribution
is
\[
(x_p+y_p)^\mathsf{T}A_p^{-1}(\lambda x_p+\mu y_p);
\]
this follows by intersecting the total pullback with the
exceptional curves, on which it has degree zero. It is the
[numerical pullback mechanism](../carriers/numerical_surface_pullback.md)
on the actual signed surface, with the local incidence of both
lifts retained. The ADE type alone does not determine these vectors. This
numerical-pullback lemma specifies the required correction; the
subsequent residual-ruling lemmas constrain the actual incidences
and give the incompatible upper bounds used in the final theorem.

### Nodal signed cubics: the correction is insufficient

In degree six downstairs (\(m=3\)), suppose the signed cubic
is normal and all its singularities along \(D\cup D'\)
are ordinary double points. Then there is no mate in any degree.
This follows by evaluating the correction on the actual nodal
incidence, not by assuming the two curves avoid the singularities.

At a node the resolution is the blowup and each smooth curve
through it meets its unique exceptional \((-2)\)-curve with
multiplicity one: the maximal ideal has order one on the
smooth curve. If both lifts pass through that node, it is a
marked endpoint. Their local intersection on the resolution
has length one, rather than two downstairs. Indeed around
such an endpoint take smooth ambient coordinates \(t,z,w\),
with the lifts \(w=0,\ z=\pm t^2\). In the blowup chart
containing both strict transforms the coordinates are
\(t,z/t,w/t\), and the common ideal of their strict transforms
is \((t,z/t,w/t)\). The strict transform of the surface
contains both, so it has the same common scheme. If there
are \(s\) shared nodes, this gives \(k=4-s\). The matrix
correction from each shared node is \(\lambda+\mu\) and
exactly offsets the loss of one mutual intersection.
Let \(u,v\) count nodes belonging only to \(D\) or only to
\(D'\), respectively. The correction equation reduces to
\[
\frac{u\lambda+v\mu}{2}=5b .
\]

To count unshared nodes, use the unique containing quadric
\(q=0\) of \(C\) downstairs. In a two-lift sextic norm the
coefficient \(Q\) is a nonzero scalar multiple of \(q\).
The restriction of \(P\) to the smooth quadric is nonzero
(otherwise \(F\) would have the factor \(q^2\)). It cuts
\(C\) plus a residual divisor of ruling class \((2,0)\),
up to exchange of the rulings, since \(C\) has class
\((1,3)\) up to the same exchange. This residual divisor
meets \(C\) in length six. Off the two marked points the
cover is étale over \(C\), and the pulled-back containing
quadric is smooth there. Away from the residual intersection
the signed cubic is smooth along the marked lift, because its
restriction to the pulled-back quadric cuts the lift simply.
At a residual point the two first derivatives on the two
sheets differ, after transport to the base, by a nonzero
multiple of \(2z\,dq\). Thus at most one lift over each such
point can be singular on a given signed cubic. It follows
that \(u+v\le6\), even for coincident residual rulings.
Consequently the left-hand side of the correction equation
is at most \(3(\lambda+\mu)=9b/2<5b\), a contradiction.

The cancellation at shared nodes does not classify other Du
Val singularities. For them the incidences of the strict
transforms and the change in their mutual intersection must
still be tracked together.

### Transverse residual sextics: higher \(A_n\) do not suffice

Work in characteristic zero with a two-lift split sextic, so
\(m=3\) and \(Q\) is a nonzero scalar multiple of the fixed
containing quadric equation \(q\). Suppose the signed cubic is
normal, and the residual ruling divisor in \(P|_{V(q)}\) meets \(C\) in six
distinct unmarked points. Then there is no mate in any degree.

The two marked endpoints are smooth on the signed surface in
this sector. At either endpoint the image of the differential
of the quadratic cover is the tangent plane of its branch
quadric; there that plane is also the tangent plane to
\(V(q)\). This follows from the linear terms of \(r\) and
\(q\) in the endpoint affine charts. Since \(P|_{V(q)}\)
cuts \(C\) simply there, \(dP\) is nonzero on that tangent
plane. Along the lift \(d(P+zQ)=dP\) at the endpoint,
with \(dP\) understood as pulled back, so the signed
surface is smooth there.

Off the endpoints the cover is étale along \(C\); the only
possible marked singularities lie over the six residual hits,
with at most one singular lift over any hit by the signed
derivative comparison above. At a singular hit the fixed
slice \(q=0\) has two transverse branches, one the marked
quartic and the other the residual ruling. Choose local
coordinates so this slice equation is \(uv=0\). The formal
splitting lemma over \(k[[q]]\) puts the signed equation in
the form \(xy+f(q)\). After normalizing the equation on the slice,
the subsequent changes preserve \(q\) and are the identity on the slice. The
transverse Hessian is invertible, so one first solves for
the critical point in \(u,v\) over \(k[[q]]\), shifts by
multiples of \(q\), and removes the remaining higher
transverse terms by formal changes. In particular the marked
axis remains one of the two axes on \(q=0\). Normality
excludes \(f=0\), and the point is an \(A_n\) with
\(\operatorname{ord}_q f=n+1\). On the toric resolution of
\(xy=q^{n+1}\) the marked axis meets the end of the exceptional
chain transversely (it is the strict transform of a boundary
divisor of the defining cone). The end diagonal of the inverse
chain matrix is \(n/(n+1)\), as follows by solving the linear
recurrence on the chain with zero boundary values. This is its
self-correction in the numerical pullback.

Let \(A,B\) be the sums of these end corrections on \(D,D'\),
respectively. The two lifts meet only at their smooth marked
endpoints, hence their strict transforms still meet in length
four. With \(\lambda+\mu=3b/2\), intersecting the pulled-back
mate separately with the two strict transforms gives
\[
(6-A)\lambda=(6-B)\mu=2b,
\qquad
\frac1{6-A}+\frac1{6-B}=\frac34.
\]
To bound the rank needed at the marked hits, spread the finite
equation data to a subfield of \(\mathbf C\) and smooth the
signed cubic in its full linear system on \(X\). Choose a
general perturbing section nonzero at all marked singular
points, so its pencil has smooth general member. Inside
disjoint analytic Milnor balls around those points, the
nearby fibers are the Milnor fibers of the \(A_n\) germs:
locally the pencil is a level set of the signed equation
divided by the nonvanishing perturbing section. The local
2-cycles have the negative definite \(A_n\) intersection
matrices. Their pairings are unchanged in the global fiber,
and cycles in different balls have zero mutual pairing.
Thus the direct sum of their rational spans injects into
the homology of the smooth fiber: a kernel vector would
pair to zero with the entire local sum, which is nondegenerate.
The smooth \((2,3)\) complete intersection is a K3 surface
with intersection signature \((3,19)\). Hence the sum of the
\(n\) at the marked hits is at most 19. This use of a smoothing
requires no Du Val assumption away from the two lifts;
the resolution used to intersect the mate needs to be crepant
only along the two lifts.

The equality is incompatible with that rank bound. Count only
singular hits and exchange the lifts so their counts are
\(i\ge j\) with \(i+j\le6\). If \(i\le4\), each correction
is strictly below one. The left-hand side is strictly less
than \(3/4\): the largest candidate bounds are at allocations
\((4,2)\) and \((3,3)\), where they are \(1/2+1/4\) and
\(2/3\), respectively. If \(i=5\), then \(j\le1\), and
Cauchy–Schwarz gives
\[
6-A=1+\sum_{s=1}^5\frac1{n_s+1}
\ \ge\ 1+\frac{25}{19+5}=\frac{49}{24}.
\]
The left-hand side is at most \(24/49+1/5<3/4\).
Finally if \(i=6\) then \(B=0\), forcing
\(\sum_{s=1}^6 1/d_s=12/7\), where \(d_s=n_s+1\ge2\)
and \(\sum d_s\le25\). Among the denominators divisible by
seven the only possibilities are one seven, two sevens,
or one fourteen (or none). After multiplying by seven,
reduce in \(\mathbf Z_{(7)}\) modulo seven. The corresponding
left residues are \(1,2,1/2,0\), none equal to
\(12\equiv5\). Thus no allocation is possible.

This uses the transverse unmarked slice to fix the exceptional
incidence, not just the Du Val type. The transverse-slice lemma has no repeated or tangent residual
intersections, marked residual hits, or nonnormal signed surfaces in
its hypotheses. Those cases are handled by the residual-ruling
and inverse-support arguments linked in the proof map.

### Removing normality: inverse support and the actual normalization

In the [transverse unmarked argument](#transverse-residual-sextics-higher-a_n-do-not-suffice)
and the [marked and doubled residual-ruling calculations](two_lift_sextic_residual_rulings.md),
the normality assumption can be removed for both distinct residual
rulings and for a doubled unmarked ruling. The substitute is the
presence of an **actual** mate: every relevant local
branch must carry the inverse support of that equation.

Specifically, at an unmarked point the local support of
the mate on the signed surface is the one lifted quartic
there. A power of its ideal is contained in the principal
mate ideal, and the mate ideal is contained in the curve
ideal. These inclusions persist after completion and
restriction to any formal branch. If a formal plane
branch meets the lifted quartic only at the point, the
restriction of the mate has maximal radical on that
plane, impossible for one equation in a two-dimensional
regular local ring. In the transverse fixed-slice
normal form \(xy+f(w)\), the case \(f=0\) has just such
an extra plane, since the marked curve is one of the
axes at \(w=0\). Thus all unmarked transverse singularities
of a hypothetical mate are isolated \(A_n\), without
assuming global normality. In the two-distinct-unmarked
case this already forces global normality: an integral
hypersurface that is not normal has a singular curve,
which must meet the ample divisor \(T\). In this case
\(S\cap T\) consists of two lifts and two residual conics
each with multiplicity one; its sole possible singular
points on \(T\) are the transverse hits, since the
endpoints are smooth. No singular curve can meet those
isolated singularities.

More generally we can perform the intersection comparison
on the **normalization** of the integral signed cubic,
which is smooth along each lift generically. The pullback
of a hypothetical mate is an effective Cartier divisor.
Above each generic lift there is a unique strict inverse
curve, which maps isomorphically to the smooth original
lift by finite birationality. No extra isolated inverse
point can occur in the support: the pullback of a nonzero
single equation on the normal integral surface has
support of pure codimension one. Thus its cycle is the
same combination \(\lambda D+\mu D'\) on these inverse
curves. The hyperplane degree and \(\lambda+\mu=3b/2\)
are unchanged. On any smooth model of this normalization,
the numerical pullback computes their intersections.
For adjunction one may pull back the original rational
canonical generator, which exists globally because
the signed cubic is a \((2,3)\) complete intersection.
The needed discrepancies are determined in the actual
charts along the strict inverse curves, not by
normality elsewhere.

In particular the simple marked-endpoint node and
\(D_5\) calculations remain unchanged. In the weight-six
case of the simple marked endpoint, normalize the
weighted strict surface before resolving. Its integral
exceptional curve \(E\) is generically smooth in the
strict surface, and is Cartier there near its entire
support (the weight-one chart and the free chart at
weighted infinity). Its finite pullback still has
one exceptional prime with multiplicity one, and
preserves \(E^2=-1\) by the projection formula. The
normalization is an isomorphism at the two smooth
marked points on \(E\), so both incidence vectors are
unchanged. The normalized exceptional curve contracts
to one point on the original normalization because
it is connected and that normalization is finite.
The same numerical self and mutual corrections follow.
The K3 smoothing rank estimate for any unmarked hits
also remains valid, since those isolated Milnor balls
only use the original signed equation and a smoothing
in the full linear system. Thus every distinct residual
ruling configuration is excluded without normality.

For the doubled unmarked ruling, first the conormal
derivative on the lifted conic \(R\) must be nonzero
under a hypothetical mate. Otherwise the signed cubic
is singular along \(R\), and its quadratic normal part
is a binary form on \(N_{R/X}=\mathcal O_R(1)^2\)
valued in \(\mathcal O_R(3)\); the conic is the section
of \(X\) by the two hyperplanes defining its plane.
Each entry of the form is therefore a section of
\(\mathcal O_R(1)\), of degree two, and its determinant
has degree four. At any of the six distinct marked
hits a nonzero determinant gives a formal product
of two planes along \(R\), by splitting the two
nondegenerate normal directions over the parameter
of \(R\). The lift is transverse to \(R\), so belongs
to only one of the two sheets. The other sheet is
forbidden by inverse support. The determinant thus
vanishes at all six hits and is identically zero.
At each hit the coefficient obtained by restricting
the normal form to the direction normal to \(R\) in
\(T\) has a simple zero, by the local \(xy^2\) slice.
A rank-one binary form over the local DVR with
any unit coefficient and determinant zero is a unit
times a square (complete a square after choosing a
unit diagonal entry). Its value on that direction
cannot have odd order. Therefore all entries vanish
at all six hits, impossible for their degree unless
the form is zero, contradicting the nonzero generic
slice coefficient. This proves the derivative
section is nonzero and still has just two zeros
counted with multiplicity.

At a rank-two hit of the doubled conic, the (A_n)
calculation applies again: the only alternative is a
formal product, and the lifted quartic cannot be in
the intersection of its two sheets, because it is
generically smooth on the signed surface (in the
slice coordinates the derivative in the \(x\) direction
restricts to \(y^2\) on the lift). Thus one sheet would
again be forbidden. The rank-one \(D_5\) case is already
isolated. In the rank-zero case the ordinary blowup
[chart in the doubled-conic lemma](two_lift_sextic_residual_rulings.md#doubled-unmarked-ruling-a-conic-bounds-the-correction)
is smooth at the point of the strict
marked lift even without normality of the original.
Normalize the blowup and resolve elsewhere, retaining
this chart. It factors through the original
normalization. Along the lift the local pole of the
original canonical form is exactly the factor
\(y^{-1}\) computed in the smooth chart; elsewhere on
that lift the original surface is smooth. The
Cartier divisor \(q=0\) has the same generic
multiplicities on the original normalization, since
the derivative section is generically nonzero on
\(R\). Its exceptional part still meets the marked
strict lift with multiplicity one. The effective
self-correction is therefore still at most two,
rather than \(30/7\). This finishes the doubled
unmarked ruling with no normality assumption.
