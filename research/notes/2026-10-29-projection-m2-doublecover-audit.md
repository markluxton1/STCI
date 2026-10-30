# Independent audit: smooth residual boundaries and the degree-two image case

October 29, 2026. Reviewer: m2_elliptic/elliptic_theory.
Status: **PASS for the two precise deductions below**, as provisional
research evidence. Neither deduction computes the remaining primitive
smooth-residual incidence or the full sixteen-parameter projection locus.
No canonical result or question is changed.

The setting is the characteristic-zero marked smooth-quadric source in
[the residual geometry note](2026-10-29-projection-residual-geometry.md).
Let \(S=\mathbf P^1\times\mathbf P^1\), let \(c\) be its diagonal, and
let four basepoint-free sections \(U_i\) of \(H=\mathcal O_S(2,2)\)
restrict to the fixed embedding of \(C_0\) on \(c\).
Assume
\[
V(q(U))=2c+D
\]
with \(D\) smooth and irreducible of type \((2,2)\). Then \(D\) is an
elliptic curve. Its two ruling maps to the target quadric have degrees
\(\deg A=2,\deg B=6\), and the target curve has projective equation
\(A=B^3\). These degrees follow from the already independently reviewed
rank-one matrix calculation in the source note; the deductions here
retain the actual morphism and its projective endpoint values.

## 1. Full inverse support forces reduced, disjoint boundary divisors

Suppose the reduced inverse of \(C_0\) is exactly \(c\). Put
\[
Z=D\cap c,\qquad
N=\#\{P\in D:A(P)=B(P)^3\}.
\]
The count uses equality in \(\mathbf P^1\), so common zeros and common
poles are included. The support of \(Z\) has at most four points, hence
\(N\le4\).

Let \(n_A,n_B\) be the numbers of distinct points in the zero and pole
divisors of \(A,B\), respectively, and set
\[
\delta_A=4-n_A,\qquad\delta_B=12-n_B.
\]
These are nonnegative. Let \(S_0\) count same-sign overlaps (zero/zero or
pole/pole) of these two boundary supports and let \(O_0\) count
opposite-sign overlaps. At a same-sign overlap let \(a_P\) be the
positive order of the zero or pole of \(A\), and put
\[
C=\sum_{\mathrm{same}}a_P.
\]
Since \(A\) has degree two, \(1\le a_P\le2\).

For \(f=B^3/A\), no boundary support point disappears under cancellation:
the absolute order of \(B^3\) at an overlap is at least three, whereas
that of \(A\) is at most two. Therefore
\[
\deg f=20-C,\qquad
n_0(f)+n_\infty(f)
=16-\delta_A-\delta_B-S_0-O_0.
\]
The degree formula counts cancellation at both zero/zero and pole/pole
overlaps; an opposite-sign overlap merges support without cancelling
orders.

Let \(q_1=\#f^{-1}(1)\). Riemann--Hurwitz on the elliptic curve gives
\[
q_1\ge\deg f-(n_0(f)+n_\infty(f))
=4+\delta_A+\delta_B+S_0+O_0-C.
\]
Indeed the ramification contributions of the three fibers \(0,\infty,1\)
sum to \(3\deg f-n_0(f)-n_\infty(f)-q_1\), at most the total
\(2\deg f\).

The projective equation \(A=B^3\) holds precisely at the fiber \(f=1\)
and at all same-sign boundary overlaps. These sets are disjoint:
at a same-sign overlap the order of \(f\) is nonzero because
\(3\operatorname{ord}B\ne\operatorname{ord}A\). Consequently
\[
\begin{aligned}
N=q_1+S_0
&\ge4+\delta_A+\delta_B+O_0+2S_0-C\\
&=4+\delta_A+\delta_B+O_0+
  \sum_{\mathrm{same}}(2-a_P).
\end{aligned}
\]
Every additional term is nonnegative. The bound \(N\le4\) first forces
\(\delta_A=\delta_B=O_0=0\). In particular every \(a_P=1\), so the last
sum equals \(S_0\) and forces \(S_0=0\).

Thus the boundary divisors of \(A,B\) are all reduced and pairwise
disjoint. The former generic-boundary restriction in the source note is
in fact necessary on this entire smooth elliptic residual stratum.
Furthermore \(q_1=N=4\), \(\deg f=20\), and equality holds in
Riemann--Hurwitz. Its zero and infinity passports are
\((3^6,1^2)\), its fiber over one has four points, and there are no other
branch values. The four points of \(Z\) are distinct.

This argument does not apply to singular or reducible \(D\). It does not
enumerate the degree-twenty covers or establish that a cover extends to
the four global sections on \(S\).

## 2. A double image forces the global projection to be symmetric

Assume in addition that the restriction \(D\to Q\) to the target quadric
has generic degree two onto its image. Since its first ruling has degree
two, the image's first ruling has degree one, and
\[
B=R(A)
\]
for a degree-three rational function \(R\) on \(\mathbf P^1\).
The map \(A:D\to\mathbf P^1\) is its double cover.

For completeness, the equation \(t=R(t)^3\) has at least four distinct
solutions in characteristic zero. Apply Riemann--Hurwitz on
\(\mathbf P^1\) to \(R(t)^3/t\): if \(s\) is its number of same-sign
overlaps with the simple zero and pole of \(t\), and \(r\ge s\) counts
all overlaps, its degree is \(10-s\), and its number of distinct zeros
and poles is at most \(8-r\). The fiber over one therefore has at least
\((10-s)-(8-r)+2\ge4\) points. These are already solutions of the
projective equality; endpoint solutions can only add points.

Full inverse support on \(D\), which has at most four points, implies
there are exactly four such values on \(\mathbf P^1\) and each has just
one preimage under \(A\). Hence they are all four branch values of the
degree-two map. If \(\iota\) is its involution, its ramification divisor
is exactly the reduced divisor \(Z\), consisting of the four points
\(D\cap c\).

Write
\[
P=\mathcal O_D(1,0),\quad Q'=\mathcal O_D(0,1),\quad
L=A^*\mathcal O_{\mathbf P^1}(1).
\]
The source diagonal cuts \(Z\), so \(P\otimes Q'=\mathcal O_D(Z)\).
Riemann--Hurwitz gives \(\mathcal O_D(Z)\simeq L^2\).
On an elliptic curve, for every degree-two line bundle \(P\),
\[
\iota^*P\simeq L^2\otimes P^{-1}\simeq Q'.
\]
This identity can be checked directly using the group law: if \(L\)
has degree-two divisor sum \(\ell\), then
\(\iota(x)=\ell-x\); pullback sends a degree-two divisor sum \(p\)
to \(2\ell-p\).

Both source ruling maps \(u,v:D\to\mathbf P^1\) are given by the
complete two-dimensional section spaces of \(P,Q'\). Thus there is
\(g\in\operatorname{PGL}_2\) such that
\[
u\circ\iota=g\circ v,\qquad
v\circ\iota=g^{-1}\circ u.
\]
At each of the four fixed points in \(Z\), the diagonal condition gives
\(u=v\). Their common values are four distinct points of \(\mathbf P^1\),
since the diagonal is embedded and its ruling parameter is an
isomorphism. Consequently \(g\) fixes four points and is the identity.
The involution on \(D\) is therefore the restriction of the source
factor interchange \(\sigma\).

The target map on \(D\) factors through \(A\), hence
\(\phi|_D\circ\sigma=\phi|_D\). The two basepoint-free tuples of sections
\(\sigma^*U_i|_D\) and \(U_i|_D\), compared using the usual interchange
linearization on \(\mathcal O_S(2,2)\), differ by a common scalar
\(\lambda\). The scalar is constant because \(D\) is projective and
connected. On a diagonal fiber this linearization acts as \(+1\);
basepoint freedom at a fixed point of \(D\cap c\) therefore forces
\(\lambda=1\).

It follows that every odd part \(U_i-\sigma^*U_i\) vanishes on \(D\).
Since \(D\) has the same divisor class \((2,2)\) as the section bundle,
each such odd part is a scalar multiple of a defining section \(F_D\).
The divisor \(D\) is invariant under \(\sigma\). Its defining section
is symmetric: an antisymmetric section vanishes on the diagonal and
would make \(c\) a component of the smooth irreducible \(D\). A scalar
multiple of this symmetric section cannot be odd in characteristic
zero. Thus
\[
U_i=\sigma^*U_i\qquad\text{for every }i
\]
on all of \(S\).

The global morphism consequently factors through
\(S\to\operatorname{Sym}^2\mathbf P^1=\mathbf P^2\), a degree-two
quotient. It is not birational. Therefore the smooth residual case
where \(D\to Q\) has degree two is excluded from the admissible
birational projection locus.

The conclusion is failure of birational admissibility. The proof does
not assert that all symmetric systems already fail basepoint freedom or
full inverse support.

## Surviving scope

For a possible admissible tuple with smooth irreducible order-two
residual, the residual map must be birational onto a curve of target
class \((6,2)\). Its boundary divisors must be reduced and disjoint, and
its degree-twenty function has the stated three-branch-value passports.
The remaining global section and marked-embedding incidence is not
computed by this audit.
