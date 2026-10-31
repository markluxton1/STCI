# Independent audit: the full quadric-modification sextic lift space

Date: October 31, 2026. Reviewer: `quadric_modification_gate_review`,
independent of the proposing agent. Status: **PASS for the exact
characteristic-zero source below; reviewed provisional exclusion, no
canonical promotion**. The reviewer independently reconstructed the
normal-coordinate expansion, global correction space, all branches of
the first gate, and the applicability of the inherited residual bound.
No new computation campaign or inherited verifier was run.

## Exact claim and dependencies

Over an algebraically closed field of characteristic zero, fix
\[
C=[s^4:s^3t:st^3:t^4],\quad q=x_0x_3-x_1x_2,\quad
c_0=x_1^3-x_0^2x_2,\quad c_2=x_2^3-x_1x_3^2.
\]
For **arbitrary actual homogeneous quartics** \(H,K\), put
\[
F=c_0^2+qH,\qquad G=c_2^2+qK.
\]
No such pair has reduced intersection support exactly \(C\). For a
proper pair, write its actual cycle as \(m[C]+R\), with
\(\delta=\deg R=36-4m\). The audit establishes these exhaustive cases:

1. If the first cancellation gate fails, then \(m=2\).
2. If the gate holds with its binary quartic \(T\ne0\), then \(m=3\).
3. If the gate holds with \(T=0\), the exact normal orders of both
   equations are two; the inherited graph bound gives \(\delta\ge4\).

The third case uses the reviewed provisional inequality in
[the residual-degree note, §§1–2](2026-10-28-residual-degree-blowup-bounds.md)
and [its independent audit](2026-10-28-residual-degree-blowup-audit.md).
Its original proof and independent reconstruction are
[the exceptional-cycle note, §2](2026-10-19-exceptional-cycle-balance-and-vertical-counterexamples.md)
and [the corresponding audit](2026-10-19-exceptional-cycle-and-vertical-family-independent-audit.md).
That inequality applies to every actual proper pair with the specified
exact normal orders; it requires neither integral carriers nor ordinary
normal roots. No new general graph inequality is claimed here.

## 1. Quadric restrictions and the complete first gate

On the Segre quadric use
\[
x_0=A_0B_0,\quad x_1=A_0B_1,\quad
x_2=A_1B_0,\quad x_3=A_1B_1.
\]
Then \(D=A_0B_1^3-A_1B_0^3\) defines \(C\), of class \((1,3)\), and
\[
c_0|_Q=A_0^2D,\qquad c_2|_Q=-A_1^2D.
\]
The two cubic restrictions therefore include different doubled endpoint
rulings. Their squares have coefficients \(A_0^4,A_1^4\), with no
relative minus sign.

At the generic point of \(C\), choose local normal coordinates given
by an equation of \(Q\) and an equation of \(C\) inside \(Q\).
Elimination of the linear quadric-normal term shows that \(m>2\)
requires
\[
t^{12}(H|_C)=s^{12}(K|_C).
\]
If either restriction is nonzero and this equality fails, the remaining
equation has a nonzero quadratic term, so the local length is exactly
two. Coprimality of \(s^{12},t^{12}\) gives the complete global gate
\[
H|_C=s^{12}T(s,t),\qquad K|_C=t^{12}T(s,t),
\tag{1}
\]
where \(T\) is a binary quartic, including zero. If both restrictions
vanish, (1) holds with \(T=0\); no ordinary-first-symbol hypothesis has
been inserted.

## 2. The nonzero-T branch: independent third-order reconstruction

Work over \(k(t)\) on \(x_0=1\), with actual local normal coordinates
\[
t=x_1,\quad v=x_2-t^3,\quad u=q=x_3-tx_2.
\]
Thus \(x_2=t^3+v\), \(x_3=t^4+tv+u\), and direct expansion gives
\[
c_0=-v,\quad
c_2=t^6v+2t^3v^2+v^3-2t^5u-2t^2vu-tu^2.
\tag{2}
\]
These coordinates are used only on this chart and at the generic point;
the homogeneous polynomial \(q\) is not treated as a global scalar
normal coordinate.

Write \(T(t)=T(1,t)\). If \(T\ne0\), then \(H|_C=T(t)\) is a unit
in \(k(t)\). The formal implicit function theorem solves
\(F=v^2+uH=0\) uniquely as
\[
u=-\frac{v^2}{T}+\frac{H_v}{T^2}v^3+O(v^4),
\tag{3}
\]
where the subscript denotes the partial derivative with respect to
\(v\), evaluated at \(u=v=0\). Terms involving \(H_u\) contribute
only from degree four onward. Substitution of (2)–(3) into \(G\)
cancels its quadratic coefficient by (1). Its cubic coefficient is
\[
R_3=4t^9+\frac{4t^{11}+t^{12}H_v-K_v}{T}.
\tag{4}
\]

For every binary quartic \(T\), the actual homogeneous quartics
\(T(x_0,x_1)\) and \(T(x_2,x_3)\) have precisely the restrictions
specified in (1). Therefore write, without loss of any correction,
\[
H=T(x_0,x_1)+h,\qquad K=T(x_2,x_3)+k,
\quad h,k\in H^0(\mathcal I_C(4)).
\]
The first baseline has zero \(v\)-derivative. The second has derivative
\[
T_X(t^3,t^4)+tT_Y(t^3,t^4)=4t^9T(1,t),
\]
by homogeneity and Euler's identity. Hence (4) becomes
\[
TR_3=4t^{11}+t^{12}h_v-k_v.
\tag{5}
\]

Every quartic \(h\) vanishing on \(C\) restricts on \(Q\) as
\(D\) times a section of \(\mathcal O_Q(3,1)\): this follows from
\(C=(D=0)\), with no claim about unsaturated homogeneous ideal powers.
On this chart \(D=-v\). Restriction of that section to \(C\), where
\((A_0,A_1)=(1,t^3)\) and \((B_0,B_1)=(1,t)\), gives
\[
h_v,k_v\in V=
\langle1,t,t^3,t^4,t^6,t^7,t^9,t^{10}\rangle_k.
\tag{6}
\]
Quartics divisible by \(q\) contribute zero to these derivatives,
because \(u\) is held fixed. Thus (6) includes every allowed quartic,
not merely a chosen subalgebra or a subset of global corrections.

Every exponent of \(V\) is at most ten; every exponent of
\(t^{12}V\) is at least twelve. Consequently their sum has no
\(t^{11}\) coefficient. In characteristic zero, (5) is nonzero for
every allowed \(h,k\). Therefore \(R_3\ne0\). Since \(F\) is smooth
transversely at the generic point, the local intersection length is
exactly three. Roots of \(T\), including either endpoint, do not affect
this argument over \(k(t)\); no pointwise classification or inversion of
a parameter minor is used.

## 3. The zero-T branch and properness

When \(T=0\), both \(H,K\) vanish on \(C\). Hence \(F,G\) lie in
the square of the local ideal of \(C\). Their exact generic orders
are two: reduction modulo \(u\) retains respectively \(v^2\) and
\(t^{12}v^2+O(v^3)\). A term divisible by \(u\) cannot cancel those
nonzero quadratic terms.

For a proper pair substitute \(a=b=6\), \(r=s=2\) into the inherited
bound
\[
5\delta\ge16(as+br)-7ab-28rs=20.
\]
Thus \(\delta\ge4\), which excludes sole support and implies \(m\le8\).
No claim of attainment of this upper bound is made. A pair with a
common surface factor already has surface support and cannot define
\(C\) set-theoretically. This disposes of the nonproper locus without
an integrality assumption on either sextic.

## Geometric content and stopping boundary

The first gate makes the lifted elementary-transform section vanish
generically along \(C\); the image section's unavoidable double curve
alone does not accomplish that. The next obstruction is global: its
normal correction belongs to the quotient of binary degree-22 sections
by the two actual correction images \(s^{12}V_{\mathrm{hom}}\) and
\(t^{12}V_{\mathrm{hom}}\), where \(V_{\mathrm{hom}}\) is the image
of \(H^0(Q,\mathcal O_Q(3,1))\) in binary degree-ten sections on
\(C\). In the displayed coordinates,
the fixed class is \(4s^{11}t^{11}\), which is absent from their sum.
This obstructs the third-order cancellation needed for higher contact
in the nonzero-T branch. It is an incompatibility of global normal
corrections, not an interpretation of exceptional fibers as residual
curves.

The zero-T branch is excluded by the inherited actual-cycle inequality.
Together these arguments exhaust this full sextic lift source and
finish the bounded experiment. They do not exhaust arbitrary sextic
carriers, higher powers of the section, other elementary modifications,
or arbitrary defining pairs. The unrestricted characteristic-zero STCI
question remains open. No higher-jet or higher-degree campaign follows
from this audit.

## Final-state source coverage

The reviewer subsequently read the complete final source
[quadric-modification note](2026-10-31-quadric-modification.md), including
its bundle construction and the larger correction-space quotient.
**PASS for that source state**, with no material correction required.

In §1 the two nowhere-simultaneously-zero fourth powers indeed embed
\(S=\mathcal O_Q(2,6)\) in \(\mathcal O_Q(6,6)^2\); the determinant
gives quotient \(L=\mathcal O_Q(10,6)\). The elementary-transform
kernel is locally free, and the local diagonal form gives the displayed
sequence with kernel \(\mathcal O_{\mathbf P^3}(4)^2\). Its vanishing
\(H^1\) makes the full lift space precisely the stated arbitrary
quartic corrections. Independently, write \(a,b\) for the ruling
classes on \(Q\). The codimension-one Chern-character formula gives
\[
\operatorname{ch}_1(i_*L)=2H,\qquad
\operatorname{ch}_2(i_*L)=i_*((10a+6b)-(a+b))=14H^2.
\]
Subtracting from \(\operatorname{ch}(\mathcal O(6)^2)\) gives
\(c_1(E)=10H\), \(\operatorname{ch}_2(E)=22H^2\), hence
\(c_2(E)=28H^2\). Locally the image ideal is \((qu,v)\), whose
proper intersection cycle is the sum of those of \((u,v)\) and
\((q,v)\). The latter restricts on \(Q\) to the divisor of \(D^2\),
namely \(2C\). This verifies the source's cycle identity and the
conditional supported cycles \(7C\) for the section and \(9C\) for
its image.

The end of §4 correctly strengthens the interpretation: the two
degree-22 subspaces \(s^{12}H^0(\mathcal O(10))\) and
\(t^{12}H^0(\mathcal O(10))\) have monomial exponent intervals
\(0,\ldots,10\) and \(12,\ldots,22\) on the displayed chart.
Their sum has dimension 22 in the 23-dimensional ambient space.
Thus even this enlarged correction space misses exactly the middle
class \(s^{11}t^{11}\). The asserted one-dimensional quotient and
two-endpoint interpretation hold. The remaining final-source proof
and its stated limitations match the cases reconstructed above.
