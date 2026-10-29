# Independent audit of the marked smooth-quadric projection continuation

October 29, 2026. Reviewer: `projection_audit`.

**Verdict: PASS for the two stated empty parameter slices, the completed
four-ruling residual stratum, the determinant order restriction, the
residual-degree and first-normal calculations, and the conditional smooth
residual Belyi restriction.**
This is independent review of scoped provisional deductions. The complete
sixteen-parameter admissible locus and descent on any surviving admissible
stratum have **not** been computed. In particular this audit does not mark
the user's full projection endpoint complete, answer
[STCI-Q-0001](../questions/cartier_projection_models.md), or promote a
canonical result.

## Literal scope and accepted premises

Work over an algebraically closed characteristic-zero field. On
\(S=\mathbf P^1\times\mathbf P^1\), use Segre coordinates
\([a:b:c:d]\), \(ad=bc\), and \(\Delta=b-c\). The source is

\[
 U=(a^2,ab,dc,d^2)+\Delta(A_0,A_1,A_2,A_3),
 \qquad A_i\in\langle a,b,c,d\rangle.
\]

The restriction on the diagonal is the fixed embedded curve
\(C_0=[s^4:s^3t:st^3:t^4]\). Admissibility means a basepoint-free
finite birational morphism onto an integral hypersurface, with full reduced
inverse support of \(C_0\) equal to the diagonal. Isolated extra inverse
points violate this condition. These hypotheses are taken literally from
[R-0004](../results/projection_phase_reduction.md); the necessary models
in [R-0002](../results/cartier_singleton_lift.md) do not supply their
existence. The normal-bundle splitting in
[R-0020](../results/quartic_conormal_characteristic_jump.md) is an
accepted premise. No inherited proof was replayed.

The audited sources are
[the two-slice calculation](2026-10-29-projection-locus.md) and
[the residual geometry calculation](2026-10-29-projection-residual-geometry.md).

## The two completed empty loci

For \(U_0=a^2,U_1=ab\), write
\(A_2=e_0a+e_1b+e_2c+e_3d\). On the two distinct ruling fibers
through the diagonal endpoint \([0:0:0:1]\), direct restriction gives

\[
 U_2|_{a=b=0}=c((1-e_3)d-e_2c),\qquad
 U_2|_{a=c=0}=b(e_1b+e_3d).
\]

Each is a binary quadratic whose only allowed zero is the diagonal
endpoint. The first is a nonzero multiple of \(c^2\) only if
\(e_3=1,e_2\ne0\); the second is a nonzero multiple of \(b^2\)
only if \(e_3=0,e_1\ne0\). Otherwise there is an off-diagonal zero,
or the quadratic is identically zero. At such a point the first three
target coordinates vanish. The fourth coordinate either gives an extra
inverse point of the endpoint or is zero as well, giving a basepoint.
Thus arbitrary values of the four coefficients of \(A_3\), and all
boundary values of \(A_2\), are covered. The entire eight-parameter
slice is empty.

For the all-four-moving slice

\[
 U=(a^2+A\Delta^2,aL,dL,d^2+D\Delta^2),\qquad
 L=pb+(1-p)c,
\]

the points \([0:1:0:0]\) and \([0:0:1:0]\) give basepoints when
\(A=D=0\), and unwanted endpoint inverse points when exactly one
of \(A,D\) is zero. When \(AD\ne0\), choose \(r^4=D/A\),
and use the source tuple constructed in the proof note. I independently
expanded its Segre equation and target coordinates. They are

\[
\begin{split}
 bc-ad={}&(1-2p)rz^3+(2Ar^2-p(1-p))z^2\\
 &+(1-2p)rAz+A^2r^2,\\
 U={}&z^2(z^2+A)(1,r,r^3,r^4).
\end{split}
\]

For \(p\ne1/2\), the displayed cubic has nonzero leading and constant
coefficients, so has a nonzero root. For \(p=1/2\), the two opposite
possible values of \(r^2\) cannot both make \(2Ar^2-1/4=0\).
Choosing one for which that coefficient is nonzero gives a quadratic
with nonzero constant coefficient and hence a nonzero root. At that
root the source point has \(\Delta=z\ne0\); the scalar target
factor either vanishes, producing a basepoint, or gives an extra inverse
point of \(C_0\). This checks every parameter stratum, rather than a
rank-open subset. There are no descent survivors in either empty slice.

I ran the new identity verifier directly:

```
M2 --script research/computations/stci_projection_locus_2026_10_29.m2
```

It returned all three expected pass messages and exit status zero. The
algebraically closed root-existence arguments above are necessary in
addition to the polynomial identities checked by that script.

## The completed four-ruling residual stratum

I independently checked completeness of the nine-parameter order-two
source in Section 3 of the projection record. In coordinates
\(Y=(b+c)/2,z=b-c\), every tuple has a symmetric lift
\((a^2,aY,Yd,d^2)\), twelve antisymmetric coefficients \(zV_i\),
and four coefficients \(h_i z^2\). The coefficient of its determinant
at first order in \(z\), restricted to \(ad=Y^2\), is

\[
 a^2V_3+d^2V_0-aYV_2-YdV_1.
\]

Substituting \((a,Y,d)=(s^2,st,t^2)\) shows that its twelve linear
coefficients span every binary monomial of degree six. Thus its kernel
has dimension five. The displayed parameterization

\[
\begin{split}
V_0&=l_0a+m_0Y,&V_1&=l_1a+l_0Y+m_0d,\\
V_2&=l_2a+m_2Y-l_1d,&V_3&=l_2Y+m_2d
\end{split}
\]

is injective in its five parameters, and the first-order determinant
equals \((ad-Y^2)(m_2a+l_0d)\), which vanishes on the conic.
It therefore is the complete kernel, not a chosen subfamily. Together
with the four \(h_i\), this gives the full affine nine-dimensional
order-at-least-two source.

On the stated stratum \(q(U)=\kappa z^2ad\), \(\kappa\ne0\),
I replayed

```
M2 --script research/computations/stci_projection_m2_endpoint_2026_10_29.m2
```

and checked its coefficient construction. Reduction modulo
\(z^2-4(Y^2-ad)\) tests equality in the full source coordinate ring.
Coefficient comparison, saturation by \(\kappa\), and equality with
the displayed expected ideal all passed. The output gives

\[
 l_0=m_2=h_1=h_2=0,\quad h_0=-m_0l_1,\quad h_3=l_1l_2,
 \quad\kappa=l_1^2-1/4,\quad m_0l_2=0.
\]

The ideal is saturated by \(\kappa\), and its closure has dimension
two. In particular neither branch of \(m_0l_2=0\) is discarded.
At the two off-diagonal points \(a=d=0,Y=\pm z/2\), the tuple is

\[
z^2\bigl(m_0(\pm1/2-l_1),0,0,l_2(\pm1/2+l_1)\bigr).
\]

The two possible nonzero scalar factors are nonzero because
\(\kappa\ne0\). The two branches therefore give a basepoint or an
extra endpoint inverse point. This proves the entire stated residual
stratum inadmissible. The residual divisor \(ad=0\) is the union of
the four coordinate ruling fibers; arbitrary residual \((2,2)\)
divisors are outside this calculation.

## Determinant strata and residual contact

Let \(H=(2,2)\), and suppose the tuple is basepoint free and
\(q(U)\ne0\). Write \(E=V(q(U))=mc+D\), with maximal \(m\).
The matrix with rows \((U_0,U_1)\), \((U_2,U_3)\) has rank exactly
one on the full determinant scheme. A locally invertible entry reduces
it to \(\operatorname{diag}(1,q(U))\), including nonreduced
components. Thus its cokernel is a line bundle \(L\) on \(E\),
with resolution

\[
0\to\mathcal O_S(-2,-2)^2\to\mathcal O_S^2\to i_*L\to0.
\]

Riemann--Roch on the quadric gives \(\chi(L)=0\). Since
\(E=(4,4)\) has arithmetic genus nine, \(\deg_E L=8\).
Its restriction to the diagonal is \(\mathcal O(3)\), by the
factorization \(M|_c=(s^3,t^3)^{\mathsf T}(s,t)\). The quotient
presentation makes \(L\) globally generated. Additivity of degree on
the component cycle therefore gives \(\deg_D L=8-3m\ge0\).
The case \(D=0\) would require \(m=4\) and \(8=12\), which is
impossible. Hence \(m=1\) or \(m=2\). This argument retains
nonreduced residual divisors.

The ruling degrees on \(D\) are respectively
\((8-3m,8-m)\), since their sum has degree
\(H\cdot D=16-4m\). The target curve has class \((1,3)\), so
the pullback contact degree on \(D\) is \(32-6m\), namely 26 or
20. Its intersection with the diagonal has length \(8-2m\), namely
six or four. A full-singleton tuple would have to concentrate every
zero of the target-curve section at those diagonal points, while mapping
no residual component into \(C_0\). These are necessary conditions,
not a computation of their parameter incidence. In particular subtracting
six or four is not a universal calculation of off-diagonal scheme length:
diagonal contact need not be transverse.

The proof note's exclusion of the \(q(U)\equiv0\) stratum is valid.
There is also a stronger short check: under basepoint freedom, a map
landing in the target quadric would be finite. Its ruling pullback
\(\mathcal O_S(a,b)\) would have square zero, so \(ab=0\).
Global generation of both ruling pullbacks and their sum \((2,2)\)
give \(0\le a,b\le2\), while the diagonal restriction requires
\(a+b=3\). The only choices \((1,2),(2,1)\) have square four,
a contradiction. Thus no basepoint-free tuple in this marked source
has identically zero determinant.

## First-normal derivative check

The antisymmetric \((2,2)\) sections are \(\Delta\) times symmetric
\((1,1)\) sections. For the four coordinates this gives twelve scalar
first-normal parameters, represented by four binary quadratics. The
target first-normal space has dimension twelve by R-0020. I checked
injectivity without relying on the source note's Euler-class shorthand.

On the chart \(s=1,t=u\), the curve is \((1,u,u^3,u^4)\).
Let \(a_i(u)\) be the four polynomials of degree at most two giving a
first-normal variation. If its normal component vanishes, its projective
variation is tangent to the curve. Eliminating its radial and tangent
coefficients gives

\[
 a_2=3u^2a_1-2u^3a_0,\qquad
 a_3=4u^3a_1-3u^4a_0.
\]

Writing \(a_0=A+Bu+Cu^2\), \(a_1=D+Eu+Fu^2\), the requirement
that both right sides have degree at most two first gives
\(C=0,E=2A/3,F=2B/3\), and then \(D=A=B=0\). Thus every
\(a_i\) is zero. Characteristic zero is used. The map is therefore
an isomorphism. Symmetric lifts have zero first-normal derivative, and
the invariant part of the restriction kernel is the line spanned by
\(\Delta^2\) in each coordinate. Thus the derivative-zero boundary
has dimension four and factors through the interchange quotient
\(S\to\operatorname{Sym}^2\mathbf P^1\). It cannot be birational.

For a prospective birational admissible map, the nonzero normal pair is
a pair of quintics, with common zero divisor of degree at most five.
This does not bound the full conductor contact at those points. The
source note correctly leaves that multiplicity comparison unproved.

## Conditional smooth-residual branch restriction

Section 5 of the residual geometry note is also correct on its explicitly
restricted open stratum. There \(m=2\), the residual \(D\) is smooth
of genus one, its ruling functions \(A,B\) have degrees two and six,
and their four zero and pole divisors are reduced and pairwise disjoint.
Thus \(A/B^3\) has degree twenty. Its zero fiber consists of two
simple zeros of \(A\) and six triple poles of \(B\); its pole fiber
has the symmetric partition. Each contributes twelve to the ramification
divisor. Full inverse support concentrates its fiber over one on at most
four diagonal intersection points, contributing at least sixteen more.
The disjointness assumptions rule out simultaneous zero or pole boundary
cancellation, so this fiber is exactly the target-curve incidence.

Riemann--Hurwitz on the elliptic curve gives total ramification forty.
The three displayed contributions already sum to at least forty.
Equality therefore forces four distinct points in the fiber over one,
four distinct diagonal intersection points, and no ramification outside
\(0,1,\infty\). Its zero and pole passports are \((3^6,1^2)\),
and its remaining passport partitions twenty into four parts. This is a
valid conditional restriction to degree-twenty three-branch-value covers.
It does not enumerate the finite cover possibilities or decide whether
any occurs in the marked projection source. Singular residuals and
colliding or nonreduced boundary divisors remain outside this argument.

## Exact limits

The empty slices are strict subfamilies of the full sixteen-parameter
source. The determinant and differential calculations remove boundaries
and sharpen the residual incidence but do not solve it. There is no
computed surviving admissible projection on which conductor phases or
pure-power descent have been tested. The relevant remaining test is still
the actual inverse-support incidence on the two determinant strata,
followed by global membership
\(\Delta^{2b}\in\langle U^\alpha:|\alpha|=b\rangle\) on an admissible
stratum. Neither a finite reformulation nor the absence of survivors in
the two tested slices is the requested full-family endpoint.
