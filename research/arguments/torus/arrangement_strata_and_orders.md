# Arrangement strata, endpoint planarity, and separate vanishing orders

**Scoped review (November 23, 2026):** the generalizations branch supplied
the three extensions below; distinct technical and generalizations reviewers
independently reconstructed the arguments and this written account, including
the four-component corollary. [R-0082](../../results/arrangement_strata_and_orders.md)
records scope and limits.

Work over an algebraically closed field of arbitrary characteristic. Let
\(Z=\{(u_i,v_i)\}_{i=1}^m\subset T=(\mathbf G_m)^2\), \(m\ge1\),
have distinct points, and give \(A_Z=\bigcup_i C_i\) its reduced union
structure, where
\[
 C_i=[s^4:s^3t:u_i st^3:v_i t^4],\qquad
 (\alpha_i,\beta_i)=(v_i^2/u_i^3,v_i^3/u_i^4).
\]
The opposite-coordinate map is a torus automorphism. These statements
extend the [endpoint defect calculation](arrangement_endpoint_delta.md)
and the [relative arrangement construction](relative_arrangement_blowup_family.md).
They concern distinct reduced arrangements; collisions and nonreduced
fundamental cycles require separate arguments.

## 1. Constant Hilbert polynomial already gives flat re-formed unions

Let \(B_m=\operatorname{Conf}_m(T)\) be the ordered configuration space,
and put \(M=4(m-1)\). For \(0\le n<M\), let \(E_{0,n}\) have columns
\((u_i^av_i^b)_i\) for \(3a+4b\le n\), and define \(E_{\infty,n}\)
using \((\alpha_i,\beta_i)\). For \(n\ge M\), both evaluation ranks
are \(m\): ordinary degree at most \(m-1\) interpolates \(m\) distinct
points, and has weighted degree at most \(M\).

**Proposition.** Let \(S\subset B_m\) be reduced and locally closed.
If the Hilbert polynomial of the geometric reduced union \(A_Z\) is
constant on \(S\), the full finite endpoint-rank vector is locally
constant on \(S\). The union formed anew over \(S\), with ideal
\[
 I_S=\bigcap_i I_{C_{i,S}}\subset\mathcal O_{\mathbf P^3\times S},
\]
is flat over \(S\), and its ideal intersection commutes with every
further base change from \(S\).

**Proof.** The exact endpoint formula gives
\[
 P_{A_Z}(d)=4md+m-\delta_0-\delta_\infty,\qquad
 \delta_0+\delta_\infty
 =2mM-\sum_{n<M}(\operatorname{rank}E_{0,n}
                     +\operatorname{rank}E_{\infty,n}).
\]
Thus the finite sum of ranks is constant. Each rank is lower
semicontinuous. Around any \(s\in S\), take the intersection of the
finitely many open neighborhoods where each rank is at least its value
at \(s\). Constancy of their sum forces equality for every rank there.
For \(m=1\) the vector is empty and the conclusion is immediate.

Locally invert a nonzero minor of each prescribed rank. All larger
minors vanish at every point, hence vanish as functions because \(S\)
is reduced. Row and column operations give an identity block and a
zero block, so each evaluation cokernel is locally free. The
coefficient calculation at the two endpoints identifies the
normalization-discrepancy module of the union formed over \(S\) with
\[
 Q_S\cong\bigoplus_{n<M}
       (\operatorname{coker}E_{0,n}\oplus
        \operatorname{coker}E_{\infty,n})
\]
as an \(\mathcal O_S\)-module. Away from the endpoints the branches
are disjoint. Consequently, in
\[
 0\longrightarrow\mathcal O_{A_S}
 \longrightarrow\bigoplus_i\mathcal O_{C_{i,S}}
 \longrightarrow Q_S\longrightarrow0,
\]
the last two terms are \(S\)-flat. The first is therefore flat, and
the sequence stays exact after every base change. Tensoring also
preserves the defining ideal sequence because \(\mathcal O_{A_S}\)
is flat. Its pulled-back ideal is exactly the kernel of restriction
to the pulled-back branches, hence their ideal intersection. \(\square\)

A Hilbert polynomial need not determine one rank vector globally:
different clopen pieces of its locus can have different vectors.
For example, two-curve defect pairs \((4,3)\) and \((3,4)\) have the
same sum. The local constancy above is all that the flat-family proof
needs; no finer rank stratum is necessary. Reducedness is used to
turn pointwise vanishing of minors into vanishing of functions, not
in the semicontinuity argument itself.

This does not identify \(I_S\) with the restriction of the universal
union ideal from \(B_m\). It also says nothing about flatness of
\(\mathcal O/I_S^n\) for \(n>1\), or specialization of the Rees
algebra. The distinction and the sufficient normal-flatness condition
remain those in the [relative construction](relative_arrangement_blowup_family.md).

## 2. Intrinsic endpoint planarity and the four-component threshold

Call an endpoint germ **planar** when the reduced union is contained
in a smooth formal surface in the completed ambient threefold.

**Lemma.** The germ at \(p_0\) is planar if and only if either all
\(u_i=U\), or \(v_i=A+Bu_i\) for all \(i\). At \(p_\infty\) the
same alternatives hold for \((\alpha_i,\beta_i)\).

**Proof.** At \(p_0\), put \((r,y,z)=(x_1/x_0,x_2/x_0,x_3/x_0)\).
A smooth formal equation \(F\) vanishing on every
\((r,u_i r^3,v_i r^4)\) has zero \(r\)-linear coefficient. Write
its remaining linear part as \(by+cz\), where \((b,c)\ne(0,0)\).
If \(b\ne0\), the coefficient of \(r^3\) in each restriction is
\(bu_i+q\), with one common scalar \(q\); all \(u_i\) agree.
If \(b=0\), then \(c\ne0\), and the coefficient of \(r^4\) is
\(cv_i+eu_i+f\); this is the asserted affine relation. Conversely,
the equations \(y-Ur^3\) and \(z-Ar^4-Bry\) are smooth common
surface equations in the respective cases. At infinity the branch
coordinates are \((w,\alpha_i w^3,\beta_i w^4)\), giving the same
proof. \(\square\)

**Proposition.** If \(m\ge5\) and both endpoint germs are planar,
then \(v_i=Bu_i\) for one \(B\ne0\). Thus all components lie on
the common smooth quadric \(x_0x_3-Bx_1x_2=0\). In particular, every
reduced scheme-theoretic complete-intersection arrangement with
\(m\ge5\) is nonplanar at at least one endpoint.

**Proof.** If both alternatives in the lemma are vertical, then
\(u_i=U\), \(\alpha_i=K\) force \(v_i^2=KU^3\), allowing at most
two distinct points. If the first is vertical and the second affine,
then
\[
 v_i^3-DUv_i^2-CU^4=0,
\]
allowing at most three. In the reverse mixed case,
\((A+Bu_i)^2-Ku_i^3=0\), again a nonzero cubic, since \(K\ne0\).
Thus for \(m\ge5\) both relations must be affine:
\(v_i=A+Bu_i\), \(\beta_i=C+D\alpha_i\). The \(u_i\) are
distinct, and each is a root of
\[
 P(u)=(A+Bu)^3-Du(A+Bu)^2-Cu^4.
\]
Five distinct roots force \(P=0\). Its constant and degree-four
coefficients give \(A=C=0\); the remaining coefficient gives
\(B^2(B-D)=0\). Nonzero \(v_i=Bu_i\) implies \(B\ne0\), so
\(D=B\). This works in every characteristic.

Each \(C_i\) has the unique quadric
\(x_0x_3-(v_i/u_i)x_1x_2\): among the ten quadratic monomials,
only \(x_0x_3\) and \(x_1x_2\) have the same binary exponent on
the parametrization. This quadric is smooth, so any common quadric
is of the form just obtained.
No reduced CI union of these curves lies on a common smooth quadric.
Indeed, every component is nondegenerate, so the ideal has no linear
equation. The quadric in a two-generated homogeneous CI ideal can
therefore replace a degree-two minimal generator. On the quadric a
degree-\(N\) second generator cuts class \((N,N)\), whereas the
union has class \((m,3m)\), up to swapping rulings. These cannot
agree for \(m>0\); see the [fixed-quadric comparison](fixed_carrier_chow_arrangements.md#comparison-with-the-fixed-smooth-quadric).
\(\square\)

**Corollary (four components).**
For \(m=4\), the reduced union is a \((4,4)\) CI if and only if
both endpoint germs are planar and there is no common quadric.

**Proof.** For sufficiency, the vertical and mixed cases above cannot
contain four points, so both relations are affine. If \(P=0\), the
same coefficient comparison gives a common quadric. Otherwise its
four distinct nonzero roots force \(C\ne0\), since \(C=0\) would
give degree at most three. They also force \(A\ne0\): for \(A=0\),
\(P=u^3(B^2(B-D)-Cu)\) has at most one nonzero root. Thus the two
affine relations have nonzero intercepts, and the established
[two-endpoint line criterion](arrangement_endpoint_delta.md)
gives the reduced \((4,4)\) CI. Conversely, that criterion supplies
the two smooth formal surfaces for a reduced \((4,4)\) CI, while
the quadric argument just proved excludes a common quadric. \(\square\)

The local planarity criterion needs no global CI assumption. Its
five-component consequence is a necessary geometric condition for
reduced CIs, not an exclusion of all such CIs or of arbitrary
set-theoretic pairs. For a repeated fundamental cycle, support on a
quadric need not put that quadric in the CI ideal; the generator
bridge used here is then unavailable.

## 3. The separated model retains every separate vanishing order

Use the [smooth separated model](relative_arrangement_blowup_family.md):
\(\psi:W'\to\mathbf P^3\) is the resolved quotient-graph morphism,
the lifted \(\widetilde C_i\) are disjoint smooth curves, and
\[
 b:\widehat W_Z=\operatorname{Bl}_{\coprod_i\widetilde C_i}W'
 \longrightarrow W'
\]
has exceptional divisors \(\widetilde E_i\). Put
\(g=\psi b\), \(H=g^*\mathcal O_{\mathbf P^3}(1)\).

**Proposition.** For arbitrary integers \(n_i\ge0\),
\[
 g_*\mathcal O_{\widehat W_Z}(-\sum_i n_i\widetilde E_i)
 =\bigcap_i I_{C_i}^{\,n_i}.
\]
Consequently, for every \(d\ge0\),
\[
 H^0(\widehat W_Z,\mathcal O(dH-\sum_i n_i\widetilde E_i))
 \cong H^0(\mathbf P^3,(\bigcap_i I_{C_i}^{\,n_i})(d)).
\]
The powers on the right are ordinary ideal-sheaf powers, with
\(I^0=\mathcal O\).

**Proof.** Proper birationality onto normal \(\mathbf P^3\) gives
\(g_*\mathcal O_{\widehat W_Z}=\mathcal O_{\mathbf P^3}\), so
the left side is a sheaf of regular functions on the target. For
the blow-up of a smooth codimension-two center, the order along
its exceptional divisor is the generic ideal order at that center:
in regular normal coordinates it is the lowest total normal degree.
The graph map is an isomorphism at the generic point of each \(C_i\)
in the dense projective torus. Thus a regular function belongs to
the left side exactly when it belongs to every symbolic power
\(I_{C_i}^{(n_i)}\).

Here symbolic and ordinary ideal-sheaf powers agree; order zero is
tautological. For \(n\ge1\), at any point of
the smooth integral curve \(C_i\), its regular prime ideal \(I\)
satisfies
\[
 \operatorname{gr}_I\mathcal O
 \cong\operatorname{Sym}_{\mathcal O/I}(I/I^2),
\]
a polynomial algebra over a domain after a local trivialization.
If \(a\notin I\), multiplication by its nonzero degree-zero class
is injective on every graded piece. Hence \(ab\in I^n\) forces
\(b\in I^n\): otherwise take the first nonzero initial class of
\(b\) below degree \(n\). Thus \(I^n\) is \(I\)-primary and
\(I^{(n)}=I^n\). This proves the sheaf identity; the projection
formula and global sections prove the stated dictionary. \(\square\)

The mechanism is generic isomorphism plus primary powers of the
smooth individual curves. It does not require the pulled-back
singular arrangement ideal to be invertible. The dictionary records
arbitrary separate orders along the components, strengthening the
order-one containment dictionary; it does not identify
\(\bigcap_i I_{C_i}^n\) with \((\bigcap_i I_{C_i})^n\), establish
Rees base change for the singular union, or control the residual
support of an equation pair. No nonflat relative specialization
claim for these higher powers is made.
