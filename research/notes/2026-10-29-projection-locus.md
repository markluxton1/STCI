# Marked quadric projection: two completed empty loci and the remaining incidence

October 29, 2026. Status: **provisional exact exclusions of the two literal
families below**. This note does not claim to have computed the full
sixteen-parameter admissible locus. Independent review is required before
using these as accepted results.

## Source and authority

Work over an algebraically closed field of characteristic zero. Write
\(S=\mathbf P^1\times\mathbf P^1\) in Segre coordinates
\([a:b:c:d]\), with \(ad=bc\), and put \(\Delta=b-c\).
The diagonal is \(c_\Delta=V(\Delta)\). The complete marked source is

\[
 U=(a^2,ab,dc,d^2)+\Delta(A_0,A_1,A_2,A_3),
 \qquad A_i\in\langle a,b,c,d\rangle.
\]

Every restriction to the diagonal is
\([s^4:s^3t:st^3:t^4]\). The admissibility requirements are basepoint
freedom, finiteness, birationality onto the image, and full reduced inverse
support of the fixed quartic equal to the diagonal, including the absence
of isolated extra inverse points. These are the literal requirements of
[R-0004](../results/projection_phase_reduction.md); the listed model in
[R-0002](../results/cartier_singleton_lift.md) does not establish their
existence. This is a continuation of the complete source in
[the candidate note](2026-10-28-stci-search-candidates.md), not a repetition
of its two tested points.

## 1. The eight-parameter two-fixed-coordinate locus is empty

Keep \(U_0=a^2\), \(U_1=ab\), and allow **all** eight scalar coefficients
of \(A_2,A_3\). Then no parameter is admissible, even if birationality is
omitted.

Write \(A_2=e_0a+e_1b+e_2c+e_3d\). On the two ruling fibers meeting the
diagonal endpoint \([0:0:0:1]\), the third coordinate is

\[
\begin{aligned}
 a=b=0:&\quad U_2=c((1-e_3)d-e_2c),\\
 a=c=0:&\quad U_2=b(e_1b+e_3d).
\end{aligned}
\]

On either fiber \(U_0=U_1=0\). A zero of \(U_2\) away from the diagonal
is therefore either a basepoint (if \(U_3=0\)) or an extra inverse point
of the endpoint of the quartic (if \(U_3\ne0\)). To avoid both, the zero
divisor of the first quadratic must be supported at \(c=0\), which forces
\(e_3=1\) and \(e_2\ne0\). The second must have zero divisor supported
at \(b=0\), which forces \(e_3=0\) and \(e_1\ne0\). These conditions
contradict each other. If either quadratic vanishes identically, a whole
off-diagonal subset maps to the endpoint or consists of basepoints, so
that case does not evade the argument. The fourth coordinate was arbitrary
throughout.

There are no surviving admissible strata in this eight-parameter slice,
and therefore no descent test is required on it. This does not exclude
parameters with moving \(U_0\) or \(U_1\).

## 2. An empty slice moving all four coordinates

For arbitrary \(A,D,p\in k\), set

\[
 L=pb+(1-p)c,\qquad
 U=(a^2+A\Delta^2,\ aL,\ dL,\ d^2+D\Delta^2).
 \tag{1}
\]

This three-parameter family belongs to the complete marked source. Its
admissible locus is empty. The proof treats every parameter stratum,
including \(A=0\), \(D=0\), and \(p=1/2\).

If \(A=D=0\), the two Segre coordinate points with \(a=d=0\) are
basepoints. If exactly one of \(A,D\) vanishes, these off-diagonal points
map to one of the two endpoints of the quartic. Hence assume \(AD\ne0\).
Choose \(r\ne0\) with \(r^4=D/A\). For an auxiliary \(z\), take

\[
\begin{aligned}
 a&=z^2,& d&=z^2r^2,\\
 b&=r(z^2+A)+z(1-p),&
 c&=r(z^2+A)-zp.
\end{aligned}
\]

Then \(\Delta=z\) and

\[
 bc-ad=F_r(z):=(1-2p)rz^3+
 (2Ar^2-p(1-p))z^2+(1-2p)rAz+A^2r^2.
 \tag{2}
\]

Moreover, without imposing any further equation,

\[
 U=z^2(z^2+A)(1,r,r^3,r^4).
 \tag{3}
\]

If \(p\ne1/2\), (2) is a nonconstant cubic with nonzero constant term,
so it has a nonzero root \(z\) over \(k\). If \(p=1/2\), it becomes

\[
 (2Ar^2-1/4)z^2+A^2r^2.
\]

Among the fourth roots of \(D/A\), the values of \(r^2\) include two
opposites. Since the characteristic is zero, at least one has
\(2Ar^2\ne1/4\). For that choice, the polynomial is nonconstant and again
has a nonzero root. Consequently the constructed source point lies on
the Segre quadric and off its diagonal. Equation (3) shows that it is
either a basepoint, if \(z^2+A=0\), or an extra inverse point of the fixed
quartic otherwise. Both alternatives violate admissibility.

No rank-open choice, genericity assumption, or saturation discards the
boundary cases in this proof. Again there is no surviving descent stratum
within (1).

## 3. A complete nonzero determinant stratum inside the nine-parameter source

Put \(Y=(b+c)/2\) and \(z=\Delta\), so
\(z^2=4(Y^2-ad)\). The full affine source satisfying
\(\operatorname{ord}_{c_\Delta}q(U)\ge2\) has the following nine parameters:

\[
\begin{aligned}
 V_0&=l_0a+m_0Y,&
 V_1&=l_1a+l_0Y+m_0d,\\
 V_2&=l_2a+m_2Y-l_1d,&
 V_3&=l_2Y+m_2d,\\
 U&=(a^2,aY,Yd,d^2)+z(V_0,V_1,V_2,V_3)
                       +z^2(h_0,h_1,h_2,h_3).
\end{aligned}
\tag{4}
\]

The normal-order condition imposes seven independent linear constraints
on the full sixteen-parameter source. Formula (4) follows by making the
first derivative of the determinant vanish on the conic \(ad=Y^2\);
its five antisymmetric parameters and four \(z^2\) parameters are all
independent. Thus the calculation below retains the entire determinant
stratum it states, rather than a selected point of that stratum.

Specify the residual determinant divisor to be the four coordinate
ruling fibers:

\[
 q(U)=\kappa z^2ad,\qquad \kappa\ne0.
 \tag{5}
\]

The complete coefficient locus for (5), obtained by coefficient comparison
in \(k[a,Y,d,z]/(z^2-4(Y^2-ad))\) and saturation by \(\kappa\), is

\[
\begin{gathered}
 l_0=m_2=h_1=h_2=0,\qquad
 h_0=-m_0l_1,\qquad h_3=l_1l_2,\\
 \kappa=l_1^2-1/4\ne0,\qquad m_0l_2=0.
\end{gathered}
\tag{6}
\]

The saved exact rational saturation certificate verifies equality of the
two ideals, retaining both branches of \(m_0l_2=0\). Its closure has
dimension two. The admissible locus on it is **empty**:

- If \(l_2=0\), then \(U_3=d^2\), \(U_2=d(Y-l_1z)\). At either Segre
  point with \(a=d=0\), \(Y=\pm z/2\), \(z\ne0\), the tuple is
  \((m_0z^2(\pm1/2-l_1),0,0,0)\). If \(m_0=0\), these are basepoints;
  otherwise they map to the endpoint \([1:0:0:0]\). The coefficient is
  nonzero because \(l_1^2\ne1/4\).
- If \(m_0=0\), the same two points give
  \((0,0,0,l_2z^2(\pm1/2+l_1))\). They are basepoints when \(l_2=0\)
  and otherwise extra inverse points of \([0:0:0:1]\).

Consequently (5) has no surviving full-inverse-support stratum, and no
descent candidate. This is a completed calculation on one reducible
residual-divisor stratum of the full order-two source. Other residual
divisors of type \((2,2)\), and the order-one source, remain outside it.

The exact script and output are
[stci_projection_m2_endpoint_2026_10_29.m2](../computations/stci_projection_m2_endpoint_2026_10_29.m2)
and
[stci_projection_m2_endpoint_2026_10_29.txt](../computations/stci_projection_m2_endpoint_2026_10_29.txt).

## 4. A rational residual component of first ruling degree one is impossible

Let \(T\) be the normalization of a rational irreducible residual
component, and suppose its two target-quadric ruling maps \(A,B:T\to
\mathbf P^1\) have degrees one and \(b>0\), respectively. Then the
equation \(A=B^3\) holds at **at least \(b+1\) distinct points** of
\(T\). Values zero and infinity are included in this statement.

To prove it, use the rational function \(f=B^3/A\). It is nonconstant:
constant equality would imply that the nonconstant maps \(A\) and
\(B^3\) have the same degree, whereas their degrees are one and \(3b\).
The divisor of \(A\) has one simple zero and one simple pole. Let
\(s\) count its same-sign overlaps with the zero and pole divisors of
\(B\), and let \(r\) count all overlaps of these supports. Thus
\(0\le s\le r\le2\). The degree of \(f\) is
\(d=3b+1-s\): at a same-sign overlap the simple zero or pole of \(A\)
cancels exactly one order. The number \(n_0+n_\infty\) of distinct
zeros and poles of \(f\) is at most \(2b+2-r\). Opposite-sign overlaps
merge points without cancelling their orders and only strengthen this
bound. The same-sign cancellation cannot remove the point entirely,
since a nonzero order of \(B^3\) is at least three.

If \(q\) is the number of distinct points of the fiber \(f=1\), the
ramification contribution of the three fibers zero, infinity and one is
\(3d-n_0-n_\infty-q\). Riemann--Hurwitz in characteristic zero bounds
this by \(2d-2\), and therefore

\[
q\ge d-(n_0+n_\infty)+2
 \ge b+1+r-s\ge b+1.
\]

Every point in \(f^{-1}(1)\) satisfies the equation of the target curve
with neither coordinate zero nor infinite, so these are distinct points
of the required inverse curve. Possible additional endpoint solutions
are not needed for this lower bound.

For a residual component of class \((r_0,s_0)\), put \(n=r_0+s_0\).
The pullback of the ambient hyperplane has degree \(2n\); hence when its
first ruling map has degree one its second has degree \(b=2n-1\).
The preceding bound gives at least \(2n\) distinct inverse points on its
normalization. The preimage there of its intersection with the diagonal
has at most \(n\) distinct points, since the pulled-back diagonal divisor
has degree \(c_\Delta\cdot T=n\). As \(n>0\), some inverse point is
off the diagonal. This rules out full inverse support, including when the
residual component is singular. It applies to a component of the reduced
support of a nonreduced residual divisor as well.

This excludes a specific component-degree pattern. It does not prove that
every reducible residual divisor has such a component. A first ruling map
of degree zero or at least two requires its own argument.

## 5. Evidence and exact remaining endpoint

The verifier
[stci_projection_locus_2026_10_29.m2](../computations/stci_projection_locus_2026_10_29.m2)
checks the polynomial identities used above over \(\mathbf Q\). Its saved
output is
[stci_projection_locus_2026_10_29.txt](../computations/stci_projection_locus_2026_10_29.txt).
The existence of nonzero roots in (2) is the algebraic argument above,
not a finite numerical sample.

The full sixteen-parameter source remains larger than the union of these
two slices. The necessary \(m=1,2\) determinant strata and their geometric
degree constraints are recorded separately in
[the projection geometry note](2026-10-29-projection-residual-geometry.md).
Their remaining task is to solve the residual inverse incidence in
parameter space with every boundary retained, then test
\(\Delta^{2b}\in\langle U^\alpha:|\alpha|=b\rangle\) on an actual
admissible stratum. **Neither that full incidence nor its surviving
descent loci is computed here.** No conclusion about the plane or cone
normalization model, or unrestricted characteristic-zero STCI, follows.
