# Independent audit: resolved projection and the ruled models in four-space

Date: 2026-10-24. Reviewer: independent agent `audit_models`.
Status: **independent mathematical reconstruction; provisional research evidence,
not canonical promotion**. Final draft comparison is recorded below when complete.

The field is algebraically closed of characteristic zero unless a specific
arithmetic observation is explicitly made. The fixed curve is
\(c(u)=[1:u:u^3:u^4]\), its complete lift is
\(c_4(u)=[1:u:u^2:u^3:u^4]\), and the projection center is
\(z=[0:0:1:0:0]\). The reviewer read the navigation and contribution
instructions, then made the following calculations before reading the new
author drafts. None uses a carrier exclusion or an STCI obstruction.

## 1. Blowup conventions and the two sections

Use projectivizations of **lines**. Write \(W^\vee=kz\oplus U\), with
\(H=\mathbf P(U)\), and put

\[
B=\mathbf P_H(\mathcal O\oplus\mathcal O(-1)),\qquad
h=p^*\mathcal O_H(1),\quad \xi=\mathcal O_B(1).
\]

The tautological subline maps into \((kz\oplus U)\otimes\mathcal O_B\)
and defines \(b:B\to\mathbf P^4\). Its fiber over a point of \(H\)
is precisely the line joining that point to \(z\). On the chart where
one of the four coordinates on \(U\) is nonzero, this is the usual
graph chart of the ideal of the origin in affine four-space. Hence it
is the blowup, rather than merely a birational incidence candidate.

The section from the summand \(\mathcal O\) is the exceptional divisor
\(E=\xi-h\); its normal bundle is \(\mathcal O_H(-1)\), and \(b\)
contracts it to \(z\). The section from \(\mathcal O(-1)\) is
\(\widetilde H=\xi\); its normal is \(\mathcal O_H(1)\), and both
\(p\) and \(b\) restrict to its natural identification with \(H\).
The equality \(p\circ j=\operatorname{id}_H\) is the precise retraction
statement. Also \(b^*\mathcal O_{\mathbf P^4}(1)=\xi\) and
\(p^*\mathcal O_H(1)=\xi-E\). These checks fix the otherwise easily
reversed signs in the bundle presentation.

Restricting to \(C\subset H\) gives
\(\mathbf P_{\mathbf P^1}(\mathcal O\oplus\mathcal O(-4))=\mathbb F_4\).
Write its negative section as \(e\) and a fiber as \(f\).
Then \(\xi=e+4f\). Both \(C\) and \(C_4\) are sections disjoint
from \(e\), of class \(\xi\), so their normal bundles in this smooth
surface are \(\mathcal O_{\mathbf P^1}(4)\). Their graph functions differ
by \(s^2t^2\); consequently their intersection divisor is exactly
\(2p_0+2p_\infty\), including its scheme structure.

## 2. The cone is not normal

At the vertex of the projective cone, its affine coordinate ring and
normalization are

\[
A=k[s^4,s^3t,st^3,t^4]\subset
T=\bigoplus_{n\geq0}k[s,t]_{4n}.
\]

The missing element \(q=s^2t^2\) is integral since
\(q^2=s^4t^4\). The exponent sums from \(\{0,1,3,4\}\) already cover
\(0,\ldots,8\) in degree two; induction by adding 0 or 4 covers all
subsequent degrees. Thus \(T/A=kq\), and the fraction fields agree.
The Veronese ring is normal, proving that it is the normalization.
This establishes an actual authority gap in any argument that calls the
original cone normal merely because its projective base curve is smooth.

The conductor in \(A\) is its homogeneous maximal ideal \(\mathfrak m\).
In \(T\) the same ideal has degree-one part
\(\langle s^4,s^3t,st^3,t^4\rangle\) and all degrees at least two.
The two conductor quotients are therefore

\[
A/\mathfrak m=k,\qquad T/\mathfrak mT=k[\epsilon]/(\epsilon^2).
\]

Pulling the conductor to \(\mathbb F_4\) gives the invertible ideal
\(\mathcal O(-e)\): the four coefficient sections have no common zero
on the parameter line. The correct factorization of the ruled map is

\[
\mathbb F_4\longrightarrow\overline S
\xrightarrow{\text{finite}}S,
\]

where the first map contracts the \((-4)\)-section and the second is
the normalization. Here \(\overline S\) is the normal cone over the
complete rational normal quartic in \(\mathbf P^5\). Its only
singularity is the contracted vertex, resolved minimally by \(e\).
In particular \(\mathbb F_4\to S\) is a resolution map, not a finite
normalization.

The conductor unit square also gives a useful check on line equivalence:
the kernel of \(\operatorname{Pic}(S)\to\operatorname{Pic}(\overline S)\)
is \((k[\epsilon]/\epsilon^2)^\times/k^\times\cong(k,+)\). The
two marked sections are linearly equivalent on the smooth ruled model
and on \(\overline S\), but not on \(S\). Indeed \(C\) is a hyperplane
section of \(S\), whereas \(C_4\) lies in no hyperplane of \(\mathbf P^4\).
Here \(H^0(S,\mathcal O_S(1))\) is the original five-dimensional
coordinate space: the missing integral element is not regular at the
vertex. This distinguishes equality of pullback classes from descent of
linear equivalence through a nonnormal map.

## 3. The cubic scroll: bundle, conductor, and the same complete quartic

Put \(v=u^2\). The ruling line has the parametrization

\[
[a:b:vb:v^2a].
\]

Homogeneously over \([S:T]\in\mathbf P^1_v\), its two generating
vectors are \((S^2,0,0,T^2)\) and \((0,S,T,0)\). They never become
dependent. Thus its incidence surface is exactly

\[
\mathbf P(\mathcal O(-2)\oplus\mathcal O(-1))\cong\mathbb F_1,
\]

which is smooth and normal. Its hyperplane class is \(H_R=e+2f\),
where \(e^2=-1\). It is ample: its intersections with both generators
of the effective cone are positive. Consequently the map to the cubic
surface is finite; on \(x_1\ne0\) the inverse parameter is
\(v=x_2/x_1\), proving birationality. The smooth incidence surface is
therefore the **finite normalization**, with no contracted curve.

The negative section \(a=0\) maps isomorphically to the nonsingular
line \([0:S:T:0]\). It is not the conductor. The other section
\(D=\{b=0\}\), of class \(e+f\), maps to the singular line
\(L=\{x_1=x_2=0\}\) by \([S:T]\mapsto[S^2:T^2]\).
In the chart \(x_0=1\), the local rings are

\[
k[b,bv,v^2]\subset k[b,v].
\]

Their conductor is \((b,bv)\) downstairs and \((b)\) upstairs.
The chart \(x_3=1\) gives the same description at infinity. Hence the
entire conductor is the reduced singular line and the reduced section
\(D\); no hidden thickening is needed at the two branch points.
Generically there are two inverse points on \(D\); at either branch
point the local image equation is the pinch point
\(y^2=x^2z\). The singular line is therefore a double curve with two
pinch points, rather than a line of uniformly split nodes.

Restoring the omitted coordinate \(aST\) gives the complete system

\[
[aS^2:aST:aT^2:bS:bT]\in\mathbf P^4,
\]

the smooth cubic rational normal scroll \(S(1,2)\). The projection center
is \([0:1:0:0:0]\), which is off the scroll and in the plane of its
conic directrix. It merges the pairs on that directrix and ramifies at
its two endpoint tangent lines. The inverse image of \(C\) is
\(\widetilde C\sim2e+2f=2D\), of degree four, self-intersection four,
and genus zero. Taking \([S:T]=[s^2:t^2]\) and the compatible fiber
coordinates gives

\[
[s^4:s^2t^2:t^4:s^3t:st^3].
\]

After permuting ambient coordinates this is the original \(C_4\), and
the omitted coordinate is precisely its middle monomial. Thus the
coexistence of the two four-space constructions is meaningful: **the
same complete quartic and the same center lie in the smooth scroll whose
projection is \(R\)**. The center lies on secants of the scroll's conic
directrix, although it lies on no secant or tangent of \(C_4\).

## 4. Normal bundles checked without a carrier theorem

For the projected curve the quadric normal sequence is
\(0\to\mathcal O(6)\to N_{C/\mathbf P^3}\to\mathcal O(8)\to0\).
Its extension is nonzero in characteristic zero. One independent test,
using the dual Euler and tangent sequences twisted by \(-8\), reduces
\(H^0(N(-8))\) to the kernel of the map from quadratic syzygies of
\((1,u,u^3,u^4)\) to quartics, \((a_i)\mapsto\sum a_i c_i'\).
A basis maps as follows:

\[
\begin{array}{c|c}
(-u,1,0,0)&1\\
(-u^2,u,0,0)&u\\
(0,-u^2,1,0)&2u^2\\
(0,0,-u,1)&u^3\\
(0,0,-u^2,u)&u^4.
\end{array}
\]

The determinant is 2, so \(H^0(N(-8))=0\); equivalently the extension
is the nontrivial one and \(N=\mathcal O(7)^{\oplus2}\). For the
complete quartic, the same argument twisted by \(-7\) uses the four
adjacent linear syzygies of \((1,u,u^2,u^3,u^4)\), which map to
\(1,u,u^2,u^3\). Hence \(H^0(N_{C_4/\mathbf P^4}(-7))=0\).
Its rank is three and degree eighteen, giving
\(N_{C_4/\mathbf P^4}=\mathcal O(6)^{\oplus3}\). Finally the
linear-hyperplane normal sequence splits on \(C\), since
\(H^1(\mathcal O(3))=0\), giving
\(N_{C/\mathbf P^4}=\mathcal O(7)^{\oplus2}\oplus\mathcal O(4)\).
These are statements about different embedded curves in the same space.

The displayed syzygy matrix was checked separately with SymPy 1.14.0
using `/tmp/stci-z4-env/bin/python`; its diagonal entries are
\((1,1,2,1,1)\). This finite identity supports, rather than replaces,
the cohomological proof.

## 5. Additional comparison bridges checked independently

The normal cone \(\overline S\) has homogeneous coordinates
\([r:s^4:s^3t:s^2t^2:st^3:t^4]\). Dropping \(s^2t^2\) gives \(S\);
dropping also \(st^3\) gives
\(F:x_1^4=x_0^3x_3\), with \(r\) as \(x_2\).
The second projection center is off \(S\), so \(S\to F\) is finite.
The semigroup generated by \((4,0),(3,1),(0,4)\) has the same group
completion as the fourth Veronese and saturates to it. Thus \(F\) has
the same normal cone \(\overline S\), and the same minimal smooth
model \(\mathbb F_4\). This assertion does not identify the two marked
sections: the complete quartic in \(S\) is graph \(r=s^2t^2\), while
the four components over \(F\) are graphs \(r=\zeta st^3\).

There is also a verified, choice-dependent elementary transformation
chain from \(Q=\mathbf P^1_u\times\mathbf P^1_v\) to the latter
\(\mathbb F_4\), preserving the marked curve \(v=u^3\) and its ruling
over \(u\). Choose the endpoint \(u=\infty\), put \(w=1/u\),
\(r_0=1/v\), and successively blow up \((w,r_i)=(0,0)\) on the
negative section, contracting the strict transform of that fiber.
The new coordinate is \(r_{i+1}=r_i/w\). Since on \(C\)
\(r_0=w^3\), the curve passes through the first three centers and
misses the fourth. Its self-intersections are

\[
6\longrightarrow5\longrightarrow4\longrightarrow3\longrightarrow4.
\]

For the first three models its class is \(e_i+3f\); on the fourth it
is \(e_4+4f\). This checks the divisor bookkeeping and explains why
an arbitrary birational equivalence is unnecessary. The construction
requires the endpoint choice and the fiber coordinate supplied by the
quadric presentation. It must not be described as a canonical map
preserving the unordered endpoint pair without that extra choice.

## 6. Draft comparison, issues, and review boundary

Draft comparison pending at the time this independent reconstruction was
first written. The author agents were informed of the cone's conductor
calculation, the normal-bundle syzygy proof, the common scroll containing
the same \(C_4\), and the elementary-transformation bookkeeping.

The review concerns intrinsic geometry of these fixed models. It neither
reopens excluded STCI cases nor promotes any canonical result. Arithmetic
orbit and characteristic-two claims require their separate independent
audit; characteristic-zero pinch-point descriptions are not implicitly
asserted in characteristic two.
