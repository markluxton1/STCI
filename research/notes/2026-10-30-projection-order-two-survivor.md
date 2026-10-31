# The remaining order-two projection incidence

October 30, 2026. This consolidates the reviewed provisional order-two
boundary and involution deductions from October 29. The line-bundle
identity in Section 3 is independently reconstructed in the
[October 30 support audit](2026-10-30-projection-elliptic-target-incidence-audit.md).
No canonical result or question is changed, and the full
admissible projection locus is not computed.

## 1. Every surviving residual is a primitive elliptic image

Work over an algebraically closed characteristic-zero field. The source
is \(S=\mathbf P^1\times\mathbf P^1\), with diagonal \(c\), and the four
basepoint-free \((2,2)\) sections have fixed diagonal restriction
\((s^4,s^3t,st^3,t^4)\). Assume the surface map is birational and has
full reduced inverse support \(c\). On its order-two determinant stratum
write
\[
f^*Q=2c+D,\qquad D\in|\mathcal O_S(2,2)|,\quad c\not\subset D.
\]
The [complete boundary theorem](2026-10-29-projection-m2-boundary.md)
and its [independent audit](2026-10-29-projection-m2-boundary-audit.md)
force \(D\) to be smooth and irreducible. Thus \(D\) is elliptic.

Let \(A,B:D\to\mathbf P^1\) be the target ruling maps, of degrees two
and six. The target curve has equation \(A=B^3\). The
[independent smooth-residual reconstruction](2026-10-29-projection-m2-doublecover-audit.md)
proves two further uniform conclusions:

1. All zero and pole divisors of \(A,B\) are reduced and pairwise disjoint.
   These are necessary conditions on the entire surviving smooth
   stratum, rather than genericity hypotheses.
2. \(D\to f(D)\subset Q\) cannot have generic degree two: that case
   forces every global coordinate section to be symmetric under source
   factor interchange, contradicting surface birationality.

The degree of \(D\to f(D)\) divides \(\gcd(2,6)=2\). Consequently the
remaining restriction is birational onto an integral target curve
\(C'\) of class \((6,2)\), with normalization \(D\).

The four points \(Z=D\cap c\) are distinct. They map to four distinct
points of \(C_0\), none at either parameter endpoint, since endpoint
equality would give a common zero or pole of \(A,B\).

## 2. The degree-twenty cover condition is now uniform

For clarity, the overlap bookkeeping proving the first conclusion is
recorded here. Let
\[
\delta_A=4-\#\operatorname{Supp}\operatorname{div}(A),\qquad
\delta_B=12-\#\operatorname{Supp}\operatorname{div}(B).
\]
Let \(S_0,O_0\) count same-sign and opposite-sign boundary overlaps, and
let \(C=\sum_{\mathrm{same}}|\operatorname{ord}_P A|\). Each order in
this sum is at most two. No overlapping boundary point disappears
from the divisor of \(F=B^3/A\), because \(B^3\) has order at least three.
Thus
\[
\deg F=20-C,\qquad
n_0(F)+n_\infty(F)=16-\delta_A-\delta_B-S_0-O_0.
\]
Riemann--Hurwitz gives
\[
\#F^{-1}(1)\ge4+\delta_A+\delta_B+S_0+O_0-C.
\]
The projective equation \(A=B^3\) holds additionally at each same-sign
overlap. These points are disjoint from \(F^{-1}(1)\), so its actual
inverse support has at least
\[
4+\delta_A+\delta_B+O_0+
\sum_{\mathrm{same}}\left(2-|\operatorname{ord}_P A|\right)
\]
points. Full inverse support allows at most four. It first forces
\(\delta_A=\delta_B=O_0=0\); every order of \(A\) is then one, so it
also forces \(S_0=0\).

It follows that \(F\) has degree twenty, zero and infinity passports
\((3^6,1^2)\), and four points over one. Equality holds in
Riemann--Hurwitz: it is branched only over \(0,1,\infty\).
The partition over one consists of four positive parts summing to twenty.
This is a necessary finite cover problem, not a completed cover
enumeration or proof that a cover extends to the global source.

## 3. An additional line-bundle constraint

The following deduction has the independent reconstruction linked above. Put
\[
L=A^*\mathcal O_{\mathbf P^1}(1),\qquad
M=B^*\mathcal O_{\mathbf P^1}(1),\qquad
\mathcal Z=\mathcal O_D(Z).
\]
The actual source hyperplane bundle restricts as
\[
H|_D=L\otimes M=\mathcal Z^2,
\]
because \(H=\mathcal O_S(2,2)\) and \(Z\) is cut by a \((1,1)\) section.
Let \(T=F^*(1)\), as an effective divisor including its multiplicities.
It has support \(Z\), and \(\mathcal O_D(T)=L\otimes M^3\).
Since all boundary divisors are reduced and disjoint, ramification over
zero and infinity has line-bundle class \(M^4\). Ramification over one
is \(T-Z\), and there is no other ramification. The elliptic canonical
bundle is trivial. Riemann--Hurwitz therefore gives the identity in
\(\operatorname{Pic}(D)\)
\[
M^4\otimes (L\otimes M^3\otimes\mathcal Z^{-1})
=(L\otimes M^3)^2.
\]
Consequently \(M=L\otimes\mathcal Z\). Combining with
\(L\otimes M=\mathcal Z^2\) gives
\[
\boxed{\mathcal Z=L^2,\qquad M=L^3.}
\]
These are line-bundle equalities, not merely numerical degrees.
In particular \(L\) is one of the four degree-two square roots of
\(\mathcal Z\) on this elliptic curve.

The identity does **not** identify \(Z\) with the actual ramification
divisor of \(A\). That stronger divisor equality was proved in the
degree-two image case using its four branch fibers; it cannot be
inferred here from linear equivalence.

The [global source-extension obstruction](2026-10-30-projection-elliptic-target-incidence.md)
uses this Picard identity to exclude the entire four-point support locus
whose binary quartic has zero middle coefficient. It retains all contact
multiplicities and both the invertible and degenerate Möbius cases.
In the complete nine-parameter normal form in the residual-geometry note,
that middle coefficient is \(C^2-1/4\), up to the nonzero scalar
normalizing the quartic. Thus an admissible order-two tuple must in
particular have \(C^2\ne1/4\).

This condition has a direct geometric meaning: the four marked image
points on \(C_0\) must **span \(\mathbf P^3\)**. A hyperplane restricts
to a binary quartic in
\(\langle s^4,s^3t,st^3,t^4\rangle\), exactly the quartics with zero
\(s^2t^2\) coefficient. For four distinct points, such a section vanishes
on all of them precisely when their images are coplanar.
On the target quadric this plane cuts a \((1,1)\) conic; in the
irreducible case it identifies the two ruling parameters by a Möbius
map. The extension proof says that this correspondence would make the
two degree-two source pencils coincide on the elliptic residual,
destroying its actual \((2,2)\) embedding. The
[geometric review](2026-10-30-stci-game-geometry-review.md) reconstructs
the intrinsic interpretation and its exact scope.

## 4. A literal target equation for the remaining incidence

An equation of \(C'\) is
\[
e_0(A)+B e_1(A)+B^2e_2(A)=0,\qquad \deg e_i\le6.
\]
Restriction to \(C_0\), \(A=t^3,B=t\), is an isomorphism from this
21-dimensional global coefficient space onto binary forms of degree
twenty: grouping exponents modulo three uniquely recovers \(e_0,e_1,e_2\).

Thus the target image is determined, up to scalar, by
\[
P(t)=\prod_{i=1}^{4}(t-t_i)^{n_i},\qquad
t_i\in k^*,\quad t_i\ne t_j,\quad
n_i>0,\quad \sum n_i=20.
\]
The curve-preserving torus normalizes one \(t_i\) to one. There are
three remaining support parameters and a finite list of multiplicity
partitions. The quadratic discriminant
\[
\Delta(A)=e_1(A)^2-4e_0(A)e_2(A)
\]
must have odd squarefree part of degree three or four, so that the
normalization has genus one. The equation must be primitive of actual
bidegree \((6,2)\), and its normalization must have exactly four
points over \(C'\cap C_0\). Counting only four target intersection
points would miss possible splitting into extra inverse points.

Even after this target incidence, one must construct the marked
\((2,2)\) embedding and the four global source sections, check
basepoint freedom and surface birationality, and test
\[
\Delta_{\mathrm{source}}^{\,2b}
\in\operatorname{span}_k\{U^\alpha:|\alpha|=b\}
\]
on an actual admissible stratum. None of these remaining tests is
claimed completed here. The general order-one source is a separate
unresolved incidence.
