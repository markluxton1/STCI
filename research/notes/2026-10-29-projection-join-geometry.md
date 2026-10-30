# A failed local multiplicity bound for the marked quadric projection

October 29, 2026. Investigator: join_geometry. Status: **provisional
explicit counterexample and exact calculation; independent review pending**.
This note does not compute the full admissible projection locus.

## The proposed comparison and its defect

The marked source is
\(S=\mathbf P^1\times\mathbf P^1\), \(H=\mathcal O_S(2,2)\), with
diagonal \(c\). One possible route to the full-inverse condition is to
intersect a projection center with the join of the embedded surface and
the marked curve, and to compare the intersection multiplicity at the
tangent boundary with first-normal ramification.

The following explicit calculation rules out a tempting local estimate:
the residual inverse contact need **not** be bounded by four times the
vanishing order of the first-normal derivative pair. A basepoint-free
finite birational member of the literal marked source has residual
contact five at a simple normal-ramification point. Its image still has
isolated extra inverse points, so it is not an admissible singleton
projection. The counterexample refutes the local estimate for arbitrary
members; it does not refute a comparison that additionally uses a global
sole-support hypothesis.

The source and the already established determinant strata are described
in [the projection record](2026-10-29-projection-locus.md) and
[the residual geometry](2026-10-29-projection-residual-geometry.md).
No claim from those notes is reopened here.

## Literal global equations

Work over an algebraically closed characteristic-zero field, choose
\(i^2=-1\), and use symmetric Segre coordinates
\[
ad=y^2-z^2/4,\qquad c=(z=0).
\]
Here \(a=u_0v_0\), \(y=(u_0v_1+u_1v_0)/2\),
\(d=u_1v_1\), \(z=u_0v_1-u_1v_0\). Take
\[
\begin{aligned}
U_0&=a^2,&U_1&=ay,\\
U_2&=yd+zy+(i/4)z^2,&
U_3&=d^2+z(-10iy-2d)+(5/2)z^2.
\end{aligned}\tag{1}
\]
All four are actual sections of \(H\), and their restriction to \(c\) is
\((s^4,s^3t,st^3,t^4)\). Thus (1) belongs to the full sixteen-parameter
marked family, with the required literal target curve.

These sections are basepoint free. A common zero has \(a=0\), and then
\(y=\pm z/2\). If \(z=0\), the source point has \(d\ne0\) and
\(U_3=d^2\ne0\). If \(z\ne0\), rescale \(z=1\). The equation
\(U_2=0\) gives \(d=-1\mp i/2\), where
\[
U_3=21/4\mp3i\ne0.
\]
Their product is \(585/16\). Since \(H\) is ample, the resulting
morphism is finite onto its integral image.

It is also birational. On \(a\ne0\), put \(x=y/a\), \(v=z/a\), so
\(d/a=x^2-v^2/4\), and normalize by \(U_0\). The first target ratio is
\(x\), and the second is
\[
U_2/U_0=x^3+xv+(i-x)v^2/4.
\]
Over \(k(x)\), this is a quadratic polynomial in \(v\), with nonzero
quadratic coefficient. Its degree-two extension has involution
\[
v\longmapsto-\frac{4x}{i-x}-v.
\]
The third target ratio is not fixed by that involution. It suffices to
check the regular specialization \(x=1\): the ratio becomes
\[
G(v)=1-(10i+2)v+2v^2+v^3/2+v^4/16,
\]
and the coefficient of \(v^3\) in
\(G(v)-G(-4/(i-1)-v)\) is \((3+i)/2\ne0\). Hence the two ratios
generate \(k(x,v)\), proving generic degree one. In particular the
image has degree \(H^2=8\).

## Residual inverse contact five at simple normal ramification

Near the diagonal point \(a=1,y=d=z=0\), put
\[
y=x,\qquad d=x^2-z^2/4.
\]
The target curve is a graph on \(X_0=1\), with ideal generated locally
by \(X_2-X_1^3\) and \(X_3-X_1^4\). Both pullbacks are divisible by
the diagonal equation \(z\). After removing that factor, they are
\[
\begin{aligned}
H_2&=x(1-z/4)+(i/4)z,\\
H_3&=-10ix-2x^2-(x^2/2)z+z^3/16+z^2/2+(5/2)z.
\end{aligned}\tag{2}
\]
On the diagonal,
\(H_2(x,0)=x\) and \(H_3(x,0)=-10ix-2x^2\), so their common
vanishing order at \(x=0\) is exactly one. This is a simple zero of the
first-normal derivative pair; changes of regular normal frame preserve
that order.

The first equation of (2) is smooth and solves
\[
x=-\frac{iz}{4(1-z/4)}.
\]
Writing \(f=1-z/4\), exact substitution gives
\[
f^2H_3\!\left(-\frac{iz}{4f},z\right)=z^5/256.
\tag{3}
\]
The denominator is a unit at the point. Therefore the residual inverse
scheme has local ring \(k[[z]]/(z^5)\), of length five, supported at
that diagonal point. In particular it has no other nearby inverse
point; its multiplicity five is a genuine concentrated residual contact.

The determinant has diagonal order one: in this chart the coefficient
of \(z\) in \(U_0U_3-U_1U_2\) is
\(-10ix-3x^2\), which is not identically zero. Thus the example belongs
to the order-one determinant stratum, not the order-two boundary.

## Full inverse support still fails

On the affine off-diagonal chart \(z=1\), substitution of all four ideal
generators of \(C_0\) gives a nonempty zero-dimensional scheme of length
eight. The computation retains its nilpotents; eight is not asserted
to be a count of distinct geometric points. Its reduced support is on
\(a=0\). This agrees with the endpoint calculations above.

The finite image therefore has no mate of any positive degree. Indeed a
mate section would pull back to a Cartier zero divisor on smooth \(S\)
whose zero support was the full inverse image of \(C_0\). A Cartier
divisor cannot have isolated support points away from its curve
components. This is a rejection of this particular carrier and a
negative finding about the proposed local estimate, not a classification
of order-one projections.

## Exact verification

The [Macaulay2 script](../computations/stci_projection_join_local_2026_10_29.m2)
works over \(\mathbf Q(i)\). It checks basepoint freedom, identity (3),
the simple normal root, the order-one determinant, the nontrivial
involution action, and the full off-diagonal inverse scheme. Its
[saved output](../computations/stci_projection_join_local_2026_10_29.txt)
records each endpoint.

The join-intersection strategy would need an additional global
comparison or a sharper invariant. The unproved factor-four estimate
cannot supply the missing implication.

## Stronger finite contact six, with the same simple normal root

There is also a basepoint-free finite birational order-one example with
local residual contact **six**, refuting the analogous factor-five
estimate. Let \(\rho^2=5\), and put
\[
A=5\rho/16,\quad L=\rho/10,\quad
B=-8\rho/15,\quad C=-1/2,\quad M=-4/15.
\]
Take
\[
\begin{aligned}
U_0&=a^2,&U_1&=ay,\\
U_2&=yd+z(y+Ad)+Lz^2,&
U_3&=d^2+z(By+Cd)+Mz^2.
\end{aligned}\tag{4}
\]
In the same \(a=1\) chart, the two residual equations are
\[
\begin{aligned}
K_2&=Ax^2+x(1-z/4)+Lz-Az^2/4,\\
K_3&=Bx+Cx^2-(x^2/2)z+z^3/16-Cz^2/4+Mz.
\end{aligned}\tag{5}
\]
The first is smooth at the origin. Its unique solution \(x=x(z)\) has
\[
K_3(x(z),z)=-\frac9{65536}z^6+O(z^7).
\tag{6}
\]
The exact quotient by (5) has dimension six as a vector space, and both
\(x^6\) and \(z^6\) vanish in it. Thus it is supported only at the
origin, with local length six. On the diagonal the residual normal
pair is \(x+Ax^2,\ Bx+Cx^2\); its common root at the origin remains
simple.

The verifier checks basepoint freedom by saturated homogeneous ideal
membership. Birationality has a short field argument: over \(k(x)\),
the ratios \(U_2/U_0\) and \(U_3/U_0\) are polynomials of degrees three
and four in \(z\), respectively, with leading coefficients \(-A/4\)
and \(1/16\). The degree of their common generated function field inside
\(k(x,z)\) divides both three and four, hence is one. The determinant
has order one since its linear normal coefficient is
\[
Bx+(C-1)x^2-Ax^3\ne0.
\]
The off-diagonal inverse scheme again has dimension zero and length
eight, so this example also fails full inverse support and has no mate.
No claim is made that six is a maximal possible local contact.
