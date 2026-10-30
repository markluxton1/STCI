# The entire singular and reducible order-two residual boundary is empty

October 29, 2026. Investigator: m2_reducible. Status: **independently
reviewed provisional theorem**. No canonical result or
question is changed. The full order-one and smooth order-two projection
incidences remain separate.

## Exact claim and input

Work over an algebraically closed field of characteristic zero. Let
\(S=\mathbf P^1\times\mathbf P^1\), \(c\) its diagonal, and let four
basepoint-free sections \(U_i\) of \(H=\mathcal O_S(2,2)\) restrict on
\(c\) to
\[
(s^4,s^3t,st^3,t^4).
\]
Let \(f:S\to\mathbf P^3\) be the resulting morphism, and let
\(Q=(x_0x_3-x_1x_2=0)\). Assume its determinant divisor is exactly
\[
f^*Q=2c+D,\qquad D\in|\mathcal O_S(2,2)|,\quad c\not\subset D.
\tag{1}
\]
The source is the full affine nine-parameter order-two source inside the
sixteen-parameter marked quadric system, rather than a coefficient slice.

**Claim.** If the full reduced inverse support of \(C_0\) is \(c\), then
\(D\) is smooth and irreducible. Equivalently, every integral singular,
reducible, or nonreduced residual divisor in (1) has an off-diagonal
inverse point. Birationality is not needed for this exclusion.

The ruling-degree input is established with its exact hypotheses in
[the residual geometry note](2026-10-29-projection-residual-geometry.md),
Sections 1 and 3, and independently reconstructed in
[the projection audit](2026-10-29-projection-locus-audit.md).
On the full scheme \(2c+D\), the rank-one coordinate matrix defines the
two ruling pullbacks from \(Q=\mathbf P^1_A\times\mathbf P^1_B\).
On \(c\) their maps are
\[
A=(s^3:t^3),\qquad B=(s:t).
\]
On the component cycle of \(D\) their total degrees are
\[
\deg_D A=2,\qquad \deg_D B=6.
\tag{2}
\]
The equation of \(C_0\) on \(Q\) is \(A_1B_0^3=A_0B_1^3\).
For affine ruling coordinates it is \(A=B^3\). The two endpoint values
are understood projectively.

For any integral component \(K\) of the reduced support of \(D\), write
\[
n=c\cdot K>0,\qquad
a=\deg(A|_{\widetilde K}),\qquad
b=\deg(B|_{\widetilde K}).
\]
Here \(\widetilde K\) is its normalization. Then
\[
a+b=H\cdot K=2n.
\tag{3}
\]
The pullback of the diagonal divisor to \(\widetilde K\) has degree
\(n\). Full inverse support therefore allows at most \(n\) distinct
points of \(\widetilde K\) mapping to \(C_0\). This statement retains
tangencies and distinct normalization branches at a singular point.

## 1. A Riemann--Hurwitz bound retaining all endpoint coincidences

Let \(T\) be a smooth projective curve of genus \(g\), and let \(A,B\)
be nonconstant ruling functions of degrees \(a\in\{1,2\}\), \(b>0\).
Then
\[
\#\{P\in T:A(P)=B(P)^3\}\ \ge\ b-a+2-2g.
\tag{4}
\]
It suffices to count points where both functions are finite and nonzero;
possible endpoint solutions can only increase the left side.

Set \(F=B^3/A\). It is nonconstant because \(3b\ne a\). Let \(n_A,n_B\)
be the numbers of distinct zeros and poles of \(A,B\), let \(r\) be the
number of points common to these boundary supports, and put
\[
s=\sum_{\text{same-sign overlaps }P} e_P,\qquad
e_P=|\operatorname{ord}_P A|\le2.
\]
At a same-sign overlap the order \(3|\operatorname{ord}_P B|\) is at
least three. Cancellation removes exactly \(e_P\) orders and never
removes the point from the boundary support of \(F\). Opposite-sign
overlaps merge support points without cancellation. Consequently
\[
d=\deg F=3b+a-s,\qquad
n_0(F)+n_\infty(F)=n_A+n_B-r.
\]
If \(q=\#F^{-1}(1)\), ramification in the three distinct fibers
\(0,\infty,1\), together with Riemann--Hurwitz, gives
\[
3d-n_0(F)-n_\infty(F)-q\le 2d+2g-2.
\]
Since \(n_A=2a-\sum_P(e_P-1)\), it follows that
\[
q\ge b-a+2-2g+(2b-n_B)
 +\sum_P(e_P-1)+r-s.
\tag{5}
\]
All correction terms are nonnegative after grouping them by each
boundary point of \(A\). A same-sign overlap contributes
\((e_P-1)+1-e_P=0\); an opposite-sign overlap contributes \(e_P\);
a point not shared with \(B\) contributes \(e_P-1\). Also
\(2b-n_B\ge0\). This proves (4) without assuming reduced or disjoint
zero and pole divisors.

Every point of \(F^{-1}(1)\) lies outside the boundary supports, so it
really satisfies \(A=B^3\). No endpoint point has been counted merely
because a rational quotient had an indeterminate expression.

## 2. Integral singular residual divisors are excluded

An integral divisor \(D\) of class \((2,2)\) has arithmetic genus one.
If it is singular, its normalization has genus zero. By (2) its ruling
degrees are \(a=2,b=6\). Formula (4) gives at least six distinct inverse
points on the normalization, while the pulled-back diagonal divisor has
degree four. At least one inverse point lies off the diagonal.

Thus every integral singular residual divisor in (1) fails full inverse
support, including nodal and cuspidal possibilities. This is a global
support exclusion, not a generic transversality argument.

## 3. Reduction of every reducible or nonreduced component cycle

Suppose \(D\) is reducible or nonreduced. Every integral component
\(K\) is then proper in \(D\), with bidegree \((r_0,s_0)\le(2,2)\).
If one coordinate is zero, integrality forces \(K\) to be a ruling
fiber. Otherwise its possible classes are \((1,1),(1,2),(2,1)\),
all of arithmetic genus zero; an integral curve of arithmetic genus zero
over this field is smooth and rational. In particular every component
of the reduced support of \(D\) is a smooth rational curve.

No component can have first ruling degree one. Indeed (3) would give
\(b=2n-1\), and (4) would give at least \(b+1=2n\) inverse points,
more than the allowed \(n\).

The degrees \(a\) are nonnegative and their sum with component
multiplicities is two by (2). Hence there is exactly one component
\(T\) with first ruling degree two, it has multiplicity one, and every
other component has first ruling degree zero. For \(T\), (3) gives
\(b=2n-2\). If \(n\ge3\), (4) gives at least \(2n-2>n\) inverse
points. Thus
\[
T\ \text{is either a ruling fiber or a curve of class }(1,1).
\tag{6}
\]
The case of a ruling has \(b=0\); it is deliberately not passed through
the nonconstant-\(B\) lemma. It will be excluded by the endpoint argument
below.

## 4. Components of first ruling degree zero must be endpoint fibers

Let \(K\ne T\). The first ruling \(A\) is a constant \(\alpha\), and
\(B\) has degree \(2n\) by (3).

If \(\alpha\) is finite and nonzero, \(C_0\) meets the target ruling
in the three distinct values \(B^3=\alpha\). If their three inverse
fibers on \(K\simeq\mathbf P^1\) are supported on at most \(n\) points,
their total ramification is at least
\[
3(2n)-n=5n.
\]
But the degree-\(2n\) map \(B:\mathbf P^1\to\mathbf P^1\) has total
ramification \(4n-2\), a contradiction. Therefore \(\alpha\) is one of
the endpoint values \(0,\infty\).

Because \(A|_c=(s^3:t^3)\), the entire intersection \(K\cap c\) must
be supported at the corresponding source endpoint \(P\) of \(c\).
The second ruling \(B|_c=(s:t)\) is an isomorphism, so an appropriate
regular endpoint coordinate \(w\) for \(B\) has nonzero derivative along
\(c\) at \(P\).

If \(n\ge2\), the smooth curve \(K\) is tangent to \(c\) at \(P\):
their intersection divisor is \(nP\). Hence \(dw|_K(P)\ne0\).
But full inverse support on \(K\) forces the degree-\(2n\) fiber
\(w=0\) to have sole support \(P\), so its order at \(P\) must be
\(2n\), contrary to the nonzero derivative. It follows that \(n=1\).
Thus every component other than \(T\) is a ruling fiber through one
of the two marked endpoints of \(c\).

## 5. The two transverse endpoint fibers give the final contradiction

If \(T\) has class \((1,1)\), its complement in \(D\) has class
\((1,1)\) and consists of one fiber of each ruling. These fibers meet,
so the constant \(A\)-values on them agree. They must therefore be the
two fibers through the same marked endpoint \(P\).

If \(T\) is a fiber of class \((1,0)\), its complement has class
\((1,2)\). It consists of one \((1,0)\) fiber and two \((0,1)\)
fibers, counted with multiplicity. The first meets the other fibers,
so their constant \(A\)-values again agree. Their diagonal endpoints
are consequently the same point \(P\); in particular the complement
contains the two distinct ruling directions through \(P\). The class
\((0,1)\) case is symmetric. This argument retains doubled fibers and
does not assume that \(D\) is reduced.

Let \(F,G\) be these two transverse ruling fibers through \(P\).
On each, \(B\) has degree two and its inverse of the target curve's
endpoint has sole support \(P\). Thus the endpoint coordinate \(w\)
vanishes to order two on each fiber:
\[
dw|_F(P)=dw|_G(P)=0.
\]
Their tangent directions span \(T_PS\), so \(dw(P)=0\). This
contradicts the nonzero derivative of \(w|_c\), since \(B|_c\) is an
isomorphism.

This exhausts every reducible and nonreduced component cycle of \(D\).
Together with Section 2, it proves the claim.

## Consequence and exact remaining scope

On the entire order-two determinant source, full singleton inverse
support can survive only when \(D\) is a smooth irreducible elliptic
curve of class \((2,2)\). No remaining singular, reducible, doubled,
or endpoint component stratum is discarded by a genericity choice.
This strengthens the earlier exclusions of the square residual locus
and a coordinate four-ruling coefficient locus.

This proof does not compute the smooth elliptic incidence, an admissible
parameter, or its conductor descent. It does not address order-one
determinants, the cone and plane normalization sources, or unrestricted
STCI. Its endpoint is the exact emptiness of the entire order-two
residual boundary.

The independent review is recorded separately in
[the boundary audit](2026-10-29-projection-m2-boundary-audit.md).
