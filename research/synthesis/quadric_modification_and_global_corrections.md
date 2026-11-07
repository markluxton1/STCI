# A quadric elementary modification and its full global correction space

This is a concrete positive rank-two bundle construction followed by a
complete exclusion of the supported-section target in one prescribed lift
space. The characteristic-zero
source and audit are reviewed mathematics at `c1339ed`; the
proof below incorporates the audit’s full Chern/cycle and endpoint-quotient
arguments. Its bounded odd-characteristic extension uses the already
reviewed odd-characteristic residual inequality. Independent consolidation
review accepted the complete proof, source preservation and that extension.
No unrestricted STCI conclusion is claimed.

## 1. The actual construction source and its purpose

Work over an algebraically closed field of characteristic different from
two. The bundle construction itself works in every characteristic. Put

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
70-parameter affine source, restricted to its proper-pair open locus,
with a geometric construction behind it. It is not an exhaustive source of
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

Write \(\mathsf h=c_1(O_{\mathbf P^3}(1))\). For reference, \(c_1(E)=10\mathsf h\), \(c_2(E)=28\mathsf h^2\). Here is the full
Chern-character calculation. Write \(a,b\) for the ruling classes on
\(Q\), so \(i_*a=i_*b=\mathsf h^2\). For \(L=O_Q(10,6)\), the
codimension-one Riemann–Roch formula gives
\[
\operatorname{ch}_1(i_*L)=2\mathsf h,\qquad
\operatorname{ch}_2(i_*L)=i_*((10a+6b)-(a+b))=14\mathsf h^2.
\]
Subtracting from \(\operatorname{ch}(O(6)^2)\) yields
\(\operatorname{ch}_1(E)=10\mathsf h\), \(\operatorname{ch}_2(E)=22\mathsf h^2\),
and hence \(c_2(E)=(100-44)\mathsf h^2/2=28\mathsf h^2\). These are integer
intersection classes, not coefficients reduced modulo the field
characteristic. The Cartier divisor \(D^2\) has degree eight, and
\(c_2(O(6)^2)=36\mathsf h^2\), consistently with the following cycle identity.
Locally a section \((u,v)\) of \(E\) maps to \((qu,v)\). If its
image zero scheme is proper, multiplication by \(qu\) is regular modulo
\(v\), and hence so are the separate factors. Its codimension-two cycle
is the sum of the cycles of \((u,v)\) and \((q,v)\). The latter
restricts on \(Q\) to the zero divisor of \(D^2\), exactly \(2C\).
Thus, when the zero schemes are proper,

\[
[Z(F,G)]=[Z(\sigma)]+2[C]. \tag{4}
\]

Thus a lift \(\sigma\) of the prescribed \(D^2\) with zero support
exactly \(C\) would have cycle \(7C\) and construct the CI with cycle
\(9C\). This concerns that full affine fiber of the quotient-section map,
not every section of \(E\). The test has a direct existence consequence.
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
literal hypotheses; it is not a new blowup theorem. A pair outside the
proper locus already has a common surface in its support and cannot cut
out only \(C\), so no STCI case is omitted by that restriction.

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

The subspace V+t^12 V has no t^11 term. Since \(4\ne0\) in characteristic different from two, (7) cannot
vanish identically in \(k(t)\). Therefore R3≠0, proving
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

## 5. The zero-T branch and the uniform residual floor

If T=0, then H,K vanish along C. Both equations have exact generic normal
order two: modulo q their nonzero quadratic terms are c0² and c2², so
terms divisible by q cannot raise those orders. Apply the inherited
[actual-pair blowup inequality](blowup_residual_geometry.md#supporting-nef-bounds-exact-slack-and-equality-controls),
with a=b=6 and r=s=2:

\[
5\delta\ge16(as+br)-7ab-28rs=20.
\]

Thus δ≥4. This inequality assumes a proper pair. Its
[reviewed characteristic scope](blowup_residual_geometry.md#characteristic-reach-and-limitation)
includes every characteristic different from two, using generated
\(I_C(3)\) and the balanced normal bundle; the \(V_5\) model is not
needed for this inequality. It does not require integral carriers or
saturated initial symbols. This branch is not empty: H=K=0
gives generic length four and residual support. No classification of its
higher contact is needed for the conclusion.

## 6. Scope, prior exclusions, and stopping decision

The [mixed-weight contact calculation](../supplements/MIXED_SEXTIC_CONTACT.md)
fixes a carrier \(q^3+\alpha c_0^2+\beta c_2^2\),
\(\alpha\beta\ne0\). Its [test-curve and weighted-subalgebra
extensions](../supplements/CARRIER_TEST_CURVES.md) retain their actual
carrier and boundary hypotheses. Arbitrary quartic corrections in (1)
are not covered by fixing those sources. The
[quadric common-boundary construction](../supplements/ACTUAL_EQUATION_SPACES.md#constructive-interface-on-the-quadric)
also has different hypotheses: (2) leaves different endpoint rulings for
the two equations. None of these scoped exclusions is being rerun or
expanded to justify the present full correction calculation.

The new result closes this whole explicit elementary-modification source
and gives its uniform positive residual floor. It supplies no exclusion
of all sextic pairs, all elementary modifications, or unrestricted STCI.
One successful source would have settled existence; failure of this
source has no exhaustive implication. The reusable calculation is to
compare the required normal correction with the restriction image of the
actual global linear system, retaining every correction allowed by the
construction. It generalizes as a method, not as an already proved
all-degree theorem. No larger-m or higher-degree sequence is selected.

## 7. Characteristic boundary and connection with absorption

The elementary-transform bundle, its complete affine lift space, the
Chern/cycle identities, and the first cancellation gate are characteristic-
free. The nonzero-\(T\) obstruction uses exactly \(4\ne0\), with no
separability or division-by-three assumption. The zero-\(T\) branch uses
the balanced-normal blowup bound, already proved in every odd
characteristic. Thus this whole explicit source has residual degree at
least four over every algebraically closed field of characteristic
other than two.

In characteristic two, \(4s^{11}t^{11}=0\), and the conormal splitting
also changes. These two proofs do not exclude that source there. No
characteristic-two source classification is supplied. The
[quartic-carrier STCI in every positive characteristic](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
uses a different source, so the odd-characteristic exclusion here is
compatible with those actual endpoints.

The [marked deformation and absorption account](marked_deformation_and_absorption.md)
distinguishes partial transfer from an endpoint. This modification supplies
an actual bundle and all actual correction equations, rather than only an
abstract normal model. The global endpoint gap in (7) shows exactly why
those plentiful corrections cannot realize a supported lift of the
prescribed \(D^2\) in this specified bundle. It is a restriction of a full construction source,
not a statement that all partial absorption or all bundle approaches fail.
