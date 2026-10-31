# A global normal-correction obstruction for a quadric elementary modification

Date: 2026-10-31. Status: **independently reviewed provisional result**;
see the [independent audit](2026-10-31-quadric-modification-audit.md).
This closes one explicit construction source, not the unrestricted STCI
question for the smooth rational quartic in characteristic zero.

## 1. The actual construction source and its purpose

Work over an algebraically closed field of characteristic zero. Put

\[
C=[s^4:s^3t:st^3:t^4],\quad q=x_0x_3-x_1x_2,\quad Q=V(q),
\]
\[
c_0=x_1^3-x_0^2x_2,\qquad c_2=x_2^3-x_1x_3^2.
\]

Consider **all** pairs

\[
F=c_0^2+qH,\qquad G=c_2^2+qK,
\qquad H,K\in H^0(\mathbf P^3,\mathcal O(4)). \tag{1}
\]

Retain pairs with no common surface component. This is an explicit
70-parameter affine source of proper containing intersections, with a
geometric construction behind it. It is not an exhaustive source of
degree-(6,6) pairs or arbitrary STCI presentations.

On the Segre quadric use

\[
(x_0,x_1,x_2,x_3)=(A_0B_0,A_0B_1,A_1B_0,A_1B_1),
\quad D=A_0B_1^3-A_1B_0^3.
\]

Then C is the divisor of D, of type (1,3), while

\[
c_0|_Q=A_0^2D,\qquad c_2|_Q=-A_1^2D. \tag{2}
\]

The two sections A_0^4,A_1^4 have no common zero, so there is an exact
sequence of bundles on Q

\[
0\to\mathcal O_Q(2,6)\to\mathcal O_Q(6,6)^2
\to\mathcal O_Q(10,6)\to0.
\]

With i:Q→P3, define the rank-two bundle

\[
E=\ker[\mathcal O_{\mathbf P^3}(6)^2\to
i_*\mathcal O_Q(10,6)].
\]

Local freeness follows from the elementary-transform local form
diag(q,1). The same local form gives

\[
0\to\mathcal O_{\mathbf P^3}(4)^2\to E
\to i_*\mathcal O_Q(2,6)\to0. \tag{3}
\]

H1(O_P3(4))=0, so the section D² defining 2C lifts to E. Its full
affine space of lifts maps into O(6)² precisely as (1). This is an actual
split-middle elementary modification; the supported zero scheme of its
lift is the unresolved construction condition being tested.

For reference, c1(E)=10 and c2(E)=28. The latter follows either from the
Chern character of the displayed surface quotient or from the cycle
identity below: the Cartier divisor D² has degree eight, and c2(O(6)²)=36.
Locally a section (u,v) of E maps to (qu,v); when both zero schemes are
proper, this gives

\[
[Z(F,G)]=[Z(\sigma)]+2[C]. \tag{4}
\]

Thus a supported section of E would have cycle 7C and would construct
the desired CI with cycle 9C. The test has a direct existence consequence.
The construction of E and the lifting in (3) are standard bundle
operations, not claimed as new theorems.

## 2. Result

For every proper pair (1), write

\[
[V(F,G)]=m[C]+R,\qquad \delta=\deg R=36-4m.
\]

**Proposition.** Every such pair has \(\delta\ge4\), hence is not an
STCI presentation of C. More precisely:

* If H|C and K|C do not satisfy the common-quartic condition (5) below,
  then m=2.
* If (5) holds with T nonzero, then m=3 and δ=24.
* If (5) holds with T=0, both exact generic normal orders are two;
  the inherited all-pair blowup bound gives δ≥4.

The first two statements are the global normal-correction calculation
proved here. The third applies an already reviewed inequality with its
literal hypotheses; it is not a new blowup theorem.

## 3. The first cancellation is the start of vanishing of the lifted section

At the generic point of C, q and a local equation of C inside Q are
regular normal parameters. From (2), eliminating the linear q term
shows that generic intersection length greater than two requires

\[
t^{12}(H|_C)=s^{12}(K|_C).
\]

If both restrictions vanish, this equality still holds. Coprimality of
s and t and their degree-sixteen restrictions therefore give a unique
binary quartic T with

\[
H|_C=s^{12}T(s,t),\qquad K|_C=t^{12}T(s,t). \tag{5}
\]

When (5) fails, at least one restriction is nonzero and elimination
leaves a nonzero quadratic normal term, proving m=2.

In the elementary-transform frame, (5) says that the section σ of E
itself vanishes along C. Without it only its image in O(6)² has the
unavoidable multiplicity two. This is a geometric entry condition, not
evidence of the required multiplicity seven for σ.

The condition is globally feasible: all its solutions can be written

\[
H=T(x_0,x_1)+h,\qquad K=T(x_2,x_3)+k,
\qquad h,k\in H^0(\mathcal I_C(4)). \tag{6}
\]

Indeed (x0,x1)=s³(s,t) and (x2,x3)=t³(s,t) on C. No particular roots
or coefficients of T are assumed.

## 4. The next normal coefficient cannot be corrected globally

Assume T≠0. Work on x0=1 and put

\[
t=x_1,\quad v=x_2-t^3,\quad u=q,
\qquad x_2=t^3+v,\quad x_3=t^4+tv+u.
\]

These are coordinates near the generic point of C, where u=v=0.
Here c0=−v and the exact identity is

\[
c_2=t^6v+2t^3v^2+v^3-2t^5u-2t^2vu-tu^2.
\]

Write T(t)=T(1,t), and let H_v,K_v denote derivatives in v at u=v=0,
with t fixed. Since T(t) is nonzero in k(t), the equation F=0 solves
formally as

\[
u=-\frac{v^2}{T}+\frac{H_v}{T^2}v^3+O(v^4).
\]

Substitution in G cancels the v² term by (5). Its v³ coefficient R3 is

\[
R_3=4t^9+\frac{4t^{11}+t^{12}H_v-K_v}{T}.
\]

For the baseline terms in (6), the first v derivative is zero for
T(x0,x1). On u=0, T(x2,x3)=(t³+v)^4T(1,t), so its derivative is
4t^9T. Thus

\[
T R_3=4t^{11}+t^{12}h_v-k_v. \tag{7}
\]

The derivatives of the corrections are controlled by their global
geometry on Q. Since h vanishes on C, its restriction to Q is D times
a section of O_Q(3,1). In this chart D=−v, whence h_v is minus the
restriction of that section to C. The same holds for k. Consequently

\[
h_v,k_v\in V=
\langle1,t,t^3,t^4,t^6,t^7,t^9,t^{10}\rangle. \tag{8}
\]

This follows directly from (A0,A1)=(1,t³), (B0,B1)=(1,t) on C:
the exponents are 3i+j, 0≤i≤3 and 0≤j≤1. Corrections divisible by q
contribute zero to this derivative, so none are omitted.

The subspace V+t^12 V has no t^11 term. Since 4≠0 in characteristic
zero, (7) cannot vanish identically in k(t). Therefore R3≠0, proving
that the complete generic transverse intersection has length exactly
three. This proves the second case of the proposition without examining
any local singularity types or particular T.

**Geometric content.** The required correction is a nonzero class in

\[
H^0(\mathbf P^1,\mathcal O(22))\big/
\big(s^{12}\operatorname{im}H^0(Q,\mathcal O_Q(3,1))
+t^{12}\operatorname{im}H^0(Q,\mathcal O_Q(3,1))\big).
\]

Here the restriction images have degree ten, and the nonzero class is
represented by 4s^11t^11. It measures the impossibility of extending the
needed next normal correction from C to an actual quartic on Q. The
missing coefficient is a global linear-system obstruction, not a count
of residual points or a proxy for their degree. The degree δ=24 follows
separately from the actual generic intersection length and Bézout.

In fact the internal gaps in the eight-dimensional restriction image
are unnecessary: even allowing every section of O_P1(10) leaves the
middle coefficient missing. The obstruction survives in the
one-dimensional quotient

\[
H^0(\mathcal O(22))\big/
\big(s^{12}H^0(\mathcal O(10))+t^{12}H^0(\mathcal O(10))\big).
\]

Geometrically, corrections vanishing to order at least twelve at either
marked endpoint cannot supply the required section with order eleven at
both. This is a two-endpoint degree constraint on actual normal
corrections, with no need to classify zeros of T.

The subsequent [Picard-lifting note, §5](2026-10-31-punctual-quadric-lifting.md#5-an-explicit-comparison-with-the-sextic-normal-correction)
constructs a Koszul-and-adjunction comparison carrying this class to
the nonzero Picard obstruction of O_Q(2,6), up to a fixed sign.
It identifies these displayed classes without equating their two
realization problems or changing the scope of the proposition here.

## 5. The zero-T branch and the uniform residual floor

If T=0, then H,K vanish along C. Both equations have exact generic normal
order two: modulo q their nonzero quadratic terms are c0² and c2², so
terms divisible by q cannot raise those orders. Apply the inherited
[all-pair inequality, §1](2026-10-28-residual-degree-blowup-bounds.md#1-exact-question-and-the-earlier-result-that-already-answers-part-of-it),
with a=b=6 and r=s=2:

\[
5\delta\ge16(as+br)-7ab-28rs=20.
\]

Thus δ≥4. This inequality assumes a proper pair and uses the fixed
characteristic-zero normal geometry of C; it does not require integral
carriers or saturated initial symbols. This branch is not empty: H=K=0
gives generic length four and residual support. No classification of its
higher contact is needed for the conclusion.

## 6. Scope, prior exclusions, and stopping decision

The earlier [mixed-weight exclusion](2026-10-29-mixed-weight-contact.md)
fixes a carrier q³+αc0²+βc2² with αβ≠0. Its
[all-mate-degree continuation](2026-10-30-mixed-weight-line-obstruction.md)
and the [weighted-subalgebra exclusion](2026-10-30-weighted-subalgebra-line-obstruction.md)
retain their respective carrier/boundary hypotheses. Arbitrary corrections
in (1) are not contained in those sources. The
[common-boundary obstruction](2026-10-30-stci-game-quadric-boundary.md)
also does not apply: (2) leaves different endpoint rulings for the two
equations. These scoped exclusions were retrieved rather than rerun.

The new result closes this whole explicit elementary-modification source
and gives its uniform positive residual floor. It supplies no exclusion
of all sextic pairs, all elementary modifications, or unrestricted STCI.
One successful source would have settled existence; failure of this
source has no exhaustive implication. The reusable calculation is to
compare the required normal correction with the restriction image of the
actual global linear system, retaining every correction allowed by the
construction. It generalizes as a method, not as an already proved
all-degree theorem. No larger-m or higher-degree sequence is selected.
