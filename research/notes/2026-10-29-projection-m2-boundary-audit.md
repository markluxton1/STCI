# Independent audit: the order-two residual boundary

October 29, 2026. Reviewer: m2_reducible/rh_audit, independently
reconstructing the argument of m2_reducible.

**Verdict: PASS.** In characteristic zero, a basepoint-free tuple in the
complete marked smooth-quadric source with determinant divisor
\[
V(q(U))=2c+D,\qquad D\in|\mathcal O_S(2,2)|,\quad c\not\subset D,
\]
cannot have full reduced inverse support equal to \(c\) if \(D\) is
reducible, nonreduced, or integral singular. Thus an admissible tuple on
the order-two stratum must have a smooth integral residual elliptic curve.
No surface birationality hypothesis is needed for this exclusion.

This is review evidence for the provisional
[boundary proof](2026-10-29-projection-m2-boundary.md), not canonical
promotion and not a computation of the remaining smooth elliptic
incidence or of the order-one locus. The complete source, determinant
strata and target ruling degrees are described in
[the projection record](2026-10-29-projection-locus.md) and
[the residual geometry calculation](2026-10-29-projection-residual-geometry.md).

## 1. The degree-at-most-two Riemann--Hurwitz bound

Let \(T\) be a smooth projective curve of genus \(g\) over an algebraically
closed characteristic-zero field. Let \(A,B:T\to\mathbf P^1\) have
degrees \(a\in\{1,2\}\) and \(b>0\). Then \(f=B^3/A\) is nonconstant,
because \(3b\ne a\). Write \(q=\#f^{-1}(1)\).

I checked the boundary coincidences explicitly. Let \(n_A,n_B\) be the
numbers of distinct zeros and poles of \(A,B\), respectively. Let \(r\)
count common points of these boundary supports, and let
\[
s=\sum_{\text{same-sign overlap }P}e_P,\qquad
e_P=|\operatorname{ord}_P A|.
\]
Every \(e_P\le2\), whereas a nonzero order of \(B^3\) is at least three.
Consequently cancellation at a same-sign overlap removes exactly \(e_P\)
orders and never removes that point from the boundary of \(f\).
Opposite-sign overlap adds orders. Hence, exactly,
\[
\deg f=3b+a-s,\qquad n_0(f)+n_\infty(f)=n_A+n_B-r.
\]

The fibers over zero, infinity and one contribute
\(3\deg f-n_0(f)-n_\infty(f)-q\) ramification units. Riemann--Hurwitz
therefore yields
\[
\begin{aligned}
q\ \ge\ {}&b-a+2-2g+(2b-n_B)\\
&+\sum_{P\in\operatorname{Supp}\operatorname{div}(A)}(e_P-1)+r-s
\ \ge\ b-a+2-2g.
\end{aligned}
\]
The last correction is nonnegative pointwise: an \(A\)-boundary point
contributes zero at a same-sign overlap, \(e_P\) at an opposite-sign
overlap, and \(e_P-1\) with no overlap. Also \(2b-n_B\ge0\).
This proves the bound without reduced or disjoint boundary hypotheses.
Since no boundary point disappears, \(f^{-1}(1)\) avoids the zeros and
poles of both \(A,B\). Its points genuinely satisfy \(A=B^3\) in
\(\mathbf G_m\); endpoint solutions are not needed for this lower bound.

If \(T\) is the normalization of a rational residual component of class
\((r_0,s_0)\), set \(n=r_0+s_0\). Its hyperplane degree is \(2n\).
When the first ruling degree is one, the bound gives \(2n\) inverse
points, exceeding the at most \(n\) points on the pulled-back diagonal.
When the first ruling degree is two and \(n\ge3\), the second degree is
\(2n-2\), and the bound gives \(2n-2>n\) inverse points.
Pullback of the diagonal to the normalization has degree \(n\), so these
support comparisons remain valid for a singular component.

For integral singular \(D\) of class \((2,2)\), its arithmetic genus is
one and its singularity contribution is positive, so its normalization
has genus zero. The ruling degrees \((2,6)\) then give at least six
inverse points, exceeding the diagonal pullback degree four. This
excludes the entire integral singular stratum.

## 2. All reducible and nonreduced multiplicity patterns

The first ruling line bundle has degree two on the component cycle of
\(D\), and is globally generated. Its degrees on individual reduced
components are nonnegative integers. Every proper integral component
of a \((2,2)\) divisor is smooth rational: its possible positive
bidegrees are bounded by \((2,2)\), its arithmetic genus is zero unless
it has class \((2,2)\), and divisors of classes \((2,0)\) or \((0,2)\)
split into ruling fibers over the algebraically closed field.

The preceding bound excludes every component of first ruling degree
one. Thus exactly one component \(T\) has first ruling degree two,
its multiplicity is one, and every other component \(K\) has first
ruling degree zero. This accounts for nonreduced divisors as well:
a degree-two component of multiplicity at least two would already
exceed the total degree budget, while a degree-one component of
multiplicity two has already been excluded.

If \(c\cdot T\ge3\), Section 1 excludes \(T\). Therefore \(T\) is a
ruling fiber or has class \((1,1)\). When \(T\) is a ruling fiber,
its second ruling degree is zero; this case is kept and is not
incorrectly passed to the positive-\(b\) lemma.

## 3. The constant-first-ruling components

Let \(K\) be another reduced component, with first ruling map constant
and \(n=c\cdot K>0\). Its second ruling map has degree \(2n\), since
the ambient hyperplane pulls back with that degree.

If its first ruling value is in \(\mathbf G_m\), the equation \(A=B^3\)
asks for three distinct values of \(B\). Full inverse support would
place their entire inverse support among at most \(n\) points of
\(K\cap c\). Those three fibers would contribute at least
\[
3(2n)-n=5n
\]
ramification units to \(B:K\simeq\mathbf P^1\to\mathbf P^1\).
Its total ramification is \(4n-2\), a contradiction.
Thus the constant first ruling value is zero or infinity.

Its intersection with the marked diagonal is then supported at the
corresponding unique endpoint \(P\), because the first ruling on \(c\)
is \(t/s\mapsto(t/s)^3\). If \(n\ge2\), the two smooth curves \(K,c\)
are tangent at \(P\). The second ruling coordinate, or its reciprocal
at infinity, is the pullback of an ambient regular coordinate:
\(X_1/X_0\) at \([1:0:0:0]\), or \(X_2/X_3\) at
\([0:0:0:1]\). On \(c\) it has a simple zero. Its derivative along
the common tangent is therefore nonzero, so it also has a simple
zero on \(K\). Full inverse support, however, requires its entire
degree-\(2n\) zero fiber on \(K\) to be supported at \(P\), and hence
to have order \(2n\). This is a contradiction.

Every such \(K\) is consequently a ruling fiber through an endpoint.
Its degree-two second ruling map has the relevant endpoint fiber
supported at that one point, so its derivative there vanishes.

## 4. The final endpoint contradiction

If \(T\) has class \((1,1)\), the complementary component cycle has
class \((1,1)\). Thus it consists of one fiber of each source ruling.
The fibers meet, so continuity of the first ruling map on the
determinant divisor makes their constant values equal. Their marked
diagonal endpoints are therefore the same point \(P\).

If \(T\) has class \((1,0)\), its complement has class \((1,2)\);
the case \((0,1)\) is the transpose. This complement again contains
both ruling types. Its incidence graph is connected, because every
fiber of one ruling meets every fiber of the other. Their first
ruling constants are therefore equal, and all pass through the
same diagonal endpoint \(P\). Repeated fibers are allowed. If two
fibers of the same ruling were distinct, equality of their marked
endpoint would itself be impossible; thus the multiplicity cases
leave the same pair of opposite ruling directions through \(P\).

The ambient regular second-ruling coordinate from Section 3 has
zero derivative along each of these two distinct tangent directions.
They span \(T_PS\), so its whole differential is zero. Its restriction
to the marked diagonal has nonzero derivative, a contradiction.

This excludes every remaining reducible or nonreduced pattern. The
argument uses the actual basepoint-free morphism at the endpoints,
not merely a generic function-field identity. The only surviving
order-two residual type is a smooth integral \((2,2)\) curve; the
admissibility and descent incidence on that type remains open here.

## Evidence and limits

This audit is an independent mathematical reconstruction, not a finite
sample certificate. It checks the zero/pole overlap cases, singular
normalization, weighted component degrees, repeated ruling fibers,
the constant-second-ruling case on \(T\), and regular ambient
coordinates needed for the endpoint differential.
No canonical record is changed. The full sixteen-parameter source,
its order-one stratum, and the smooth elliptic order-two residual
stratum remain outside this exclusion.
