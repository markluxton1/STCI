# Mixed-degree normal forms and their pole divisors

For fixed C0 in characteristic zero, this owner separates an allowed global generator subtraction from an uncontrolled rational ratio of first-normal symbols. The actual homogeneous restriction map determines the quotient of possible normal coefficients. Its principal-part class is finite-dimensional even when the ratio has poles; the positions, multiplicities and common vertical divisor remain part of the data.

The original degree (4,5)/(4,6) existence questions are closed by the fixed quartic-carrier theorem. These arguments retain independent structural value: the regular-ratio reduction, exact rational-pole parameterization, countermodels and first-blowup incidence examples explain why local source compatibility does not produce global supported equations. Neither a regular ratio nor a first-blowup common factor is automatic.


The low-degree normal-order bound and persistence argument used below are proved in [formal normal intersection geometry](../synthesis/formal-normal-intersection.md), in the retained P-011 and P-006 proofs.

## corrected first-normal reduction for the mixed \((4,6)\) pair

<a id="p-021"></a>

Let \(F,G\) have degrees four and six.  The quartic cannot have normal order
two by P-011.  If both equations initially have order one, P-006 makes their
normal linear forms proportional over \(k(C)\).  Write them on the exceptional
surface as

\[
 f_1=H_F L,\qquad g_1=H_G L,
\]

where \(L\) is the primitive horizontal factor.  The quotient \(H_G/H_F\)
is a **rational**, not automatically regular, section of
\(O_C(2)=O_{\mathbf P^1}(8)\).  A global subtraction is available only on the
regular-ratio branch
\(\operatorname{div}(H_G)\ge\operatorname{div}(H_F)\).  On that branch,

\[
 H^0(\mathbf P^3,O(2))\longrightarrow H^0(C,O_C(2))
\]

is surjective.  Subtracting a quadratic multiple of \(F\) from \(G\) therefore
puts the pair, without changing its ideal, in normal orders \((1,2)\).

The regularity condition cannot be omitted.  In the complete local ring
\(k[[t,u,v]]\),

\[
 F=tu+v^6,\qquad G=u
\]

generate \((u,v^6)\), whose radical is \((u,v)\) and whose quotient is finite
free of transverse length six over \(k[[t]]\), but the first-normal ratio is
\(1/t\).  This disproves the formerly stated universal subtraction.

After the permitted subtraction, write G for the transformed sextic of generic normal order two. On

\[
 E=\mathbf P(N_C^*)\simeq\mathbf P^1\times\mathbf P^1,
\]

the first normal divisors have classes

\[
 D_F\sim(9,1),\qquad D_G\sim(10,2).
\]

Write the saturated horizontal component common to them as
\(R\sim(e,1)\), retaining every closed-point order jump as a vertical divisor:

\[
 D_F=V_B+R,\qquad V_B\sim(9-e,0),
\]

\[
 D_G=R+V_W+T,\qquad
 V_W\sim(w,0),\quad T\sim(10-e-w,1).
\]

Let \(S_q\sim(1,1)\) be the section defined by the normal direction of the
unique quadric.  On that quadric, with \(C\sim(1,3)\), neither equation can be
\(q\)-divisible, and

\[
 F|_Q=C+\rho,\qquad \rho\sim(3,1),
\]

\[
 G|_Q=2C+\sigma,\qquad \sigma\sim(4,0).
\]

The common horizontal section cuts

\[
 D_0=R\cap S_q,\qquad \deg D_0=e+1,
\]

and the exceptional-divisor identities show scheme-theoretically that

\[
 D_0\subset\rho\cap\sigma.
\]

If \(\rho\) and \(\sigma\) have no common component, their proper intersection
on \(Q\) has length

\[
 (3,1)\cdot(4,0)=4.
\]

Hence \(e+1\le4\).  If \(e\ge4\), the two residuals share a component; since
\(\sigma\) is a sum of four ruling fibers, that component is an extra ruling
line contained in both ambient equations.  Therefore every pair in the
regular-ratio branch must
satisfy

\[
 \boxed{e\in\{0,1,2,3\}},
\]

so the vertical singularity divisor of the quartic has degree
\(9-e\ge6\).

For the omitted nonregular order-\((1,1)\) branch, the original divisors have
classes \((9,1)\) and \((17,1)\).  A primitive common horizontal factor may
have \(e\le8\); the endpoint \(e=9\) has constant \(H_F\) and is therefore
regular.  These pole/vertical-divisor strata are not covered by the finite
list below and form a separate necessary incidence stratum; they do not reopen the closed actual mate question.

This bound is sharp at first-normal order.  For \(C_0\), exact linear algebra
identifies the quartic normal image as a rank-17 subspace of
\(H^0(O(9))^2\), and the sextic quadratic-normal image as a rank-22 subspace
of \(H^0(O(10))^3\).  For each \(e=0,1,2,3\), their common-factor incidence
has a nonempty full-rank locus, even after imposing non-\(q\)-divisibility and
the absence of a common residual ruling on \(Q\).  One explicit \(e=0\)
example is

\[
\begin{aligned}
F={}&A(x_0+x_1+x_2+x_3)+B(x_2+x_3)+Dx_2\\
 &+q(x_1x_3+x_2^2+2x_3^2)+2q^2,\\
G={}&A^2+4q^3.
\end{aligned}
\]

Its normal forms are \(H_9a\) and \(a^2\); neither equation is
\(q\)-divisible and the residual divisors on \(Q\) share no ruling.  Yet its
generic transverse length is three rather than six, leaving residual degree
twelve.  Within the regular-ratio branch, the next decisive conditions are
the vanishing,
after formal elimination by the quartic, of the cubic, quartic, and quintic
transverse coefficients, followed by nonvanishing of the sextic coefficient.
The first blowup cannot replace those higher-jet equations.

## finite pole-divisor strata for the nonregular mixed pairs

<a id="p-031"></a>

The ratio gap in P-021 and P-026 is not an arbitrary infinite-dimensional
phenomenon.  It has an exact divisor parameterization.  Let \(b=5\) or \(6\)
and put \(\delta=4(b-4)\), so \(\delta=4\) or \(8\).  On
\(E=\mathbf P(N_{C_0}^*)\), an order-one degree-\(d\) normal divisor has
class \((4d-7,1)\).  Write the primitive common horizontal factor and its
vertical coefficients as

\[
 f_1=hL,\qquad g_1=kL,\qquad L\sim(e,1),
\]

\[
 \deg h=m=9-e,\qquad \deg k=m+\delta.
\]

For the zero divisors \(H=(h)_0\) and \(K=(k)_0\), define their coefficientwise
common part and the remaining pole and zero divisors by

\[
 A=H\wedge K,\qquad P=H-A,\qquad Z=K-A.
\]

Then

\[
 H=A+P,\qquad K=A+Z,\qquad P\wedge Z=0,
\]

\[
 c=\deg A,\qquad p=\deg P,\qquad
 c+p=9-e,\qquad \deg Z=p+\delta.
\]

The quotient \(k/h\) is a rational section of \(O_{\mathbf P^1}(\delta)\)
with divisor \(Z-P\).  It is regular exactly when \(p=0\).  Thus \(A\) records
the common vertical order jumps and \(P\) records precisely the poles omitted
by the former reductions.

Generator changes give finite principal-part quotients.  For \((4,6)\),
restriction of ambient quadrics to \(C_0\) is all of \(H^0(O(8))\), and

\[
 H^0(O(m+8))/hH^0(O(8))\simeq H^0(O_H(m+8))
\]

has dimension \(m\).  On an affine chart whose point at infinity avoids
\(H\), polynomial division and subtraction of a quadratic multiple of \(F\)
give the representative

\[
 \boxed{k=r,\qquad \deg r<m.}
\]

and \(c=\deg\gcd(h,r)\), \(p=m-c\).  This polynomial remainder is a chartwise
description of the intrinsic principal part, not a preferred global
coordinate.  For \((4,5)\), the restrictions of ambient linear forms in the
standard monomial coordinate are

\[
 W_5=\langle1,z,z^3,z^4\rangle\subset H^0(O(4)),
\]

with missing section \(z^2\).  Intrinsically there is an exact sequence

\[
 0\longrightarrow H^0(O(4))/W_5
 \longrightarrow H^0(O(m+4))/hW_5
 \longrightarrow H^0(O_H(m+4))
 \longrightarrow0.
\]

Thus the quotient has dimension \(m+1\): one missing-restriction coordinate
and an \(m\)-dimensional principal part on \(H\).  After choosing a lift \(r\)
of that principal part, it has the representative

\[
 \boxed{k=\lambda z^2h+r,\qquad \deg r<m.}
\]

Here vanishing of the principal part, equivalently \(r=0\) in any such
splitting, is exactly the regular-ratio slice used in P-026; a nonzero
principal part is the full nonregular locus.  On a chart avoiding \(H\), the
lift can be taken with \(\deg r<m\).  The invariant data are its class on
\(H\) and the pole divisor \(P\), not the chosen polynomial remainder.

For \((4,5)\), P-016 leaves gcd types \(e=0,m=9\) and \(e=1,m=8\), and P-025
eliminates the first type without any regular-ratio assumption.  Jaffe's
checked no-common-singularity theorem forces a genuine \((4,5)\) pair to
have a point where both carriers are singular.  Since \(L\) is primitive,
this is exactly \(A\ne0\), or \(c\ge1\).  Hence every remaining nonregular
candidate satisfies

\[
 \boxed{e=1,\qquad 1\le p\le7,\qquad c=8-p,\qquad
 \deg Z=p+4.}
\]

There are seven numerical pole-length strata.

For \((4,6)\), nonregularity first gives \(0\le e\le8\) and \(p\ge1\).
The pair \((4,6)\) is likewise absent from Jaffe's list for carriers with no
common singular point, so again \(c\ge1\).  Before using the global
multiplicity-six filtration, the exact first-normal reduction is

\[
 \boxed{0\le e\le7,\qquad 1\le p\le8-e,\qquad
 c=9-e-p,\qquad \deg Z=p+8.}
\]

This is a triangle of \(8+7+\cdots+1=36\) preliminary numerical strata, while
the regular branch has P-021's preliminary list \(p=0,\ e=0,1,2,3\).  P-042
later imposes the global lci condition \(e\in\{0,1\}\), leaving only 15 of the
nonregular strata and only the first two regular values.

Finite flatness controls special transverse orders but not pole length.  At a
common singular point a length-five fiber forces orders \((2,2)\); a
length-six fiber permits \((2,2),(2,3),(3,2)\).  Nevertheless, for every
\(\alpha\ge1\),

\[
 F=t^\alpha u+v^n,\qquad G=u
\]

defines \((u,v^n)\), which is free of rank \(n\) over \(k[[t]]\), while its
first-normal ratio is \(t^{-\alpha}\).  No bound on \(p\) can therefore follow
from flat transverse length alone.

The unique quadric gives useful exact tangency budgets.  If
\(D_0=L\cap S_q\), then

\[
 R_4|_{C_0}=D_0+H,\qquad R_b|_{C_0}=D_0+K,
\]

and their common restriction has degree
\(\deg(D_0+A)=10-p\).  The residual intersections on the quadric have total
length ten for \((4,5)\) and fourteen for \((4,6)\).  If

\[
 \epsilon_x=i_x(R_4,R_b)-\operatorname{ord}_x(D_0+A),
\]

then \(\epsilon_x\ge0\) and

\[
 \boxed{\sum_x\epsilon_x=p\quad\text{for }(4,5),}
\]

\[
 \boxed{\sum_x\epsilon_x=4+p\quad\text{for }(4,6).}
\]

These are exact constraints, not contradictions.  They show that every unit
of pole length must reappear as residual excess tangency.  P-038 completes the
formerly conjectural defect comparison in the opposite direction:
\(A=2D\) scheme-theoretically.  Hence the type-B \((4,5)\) list collapses to
the single stratum \((c,p,\deg Z)=(2,6,10)\).  P-042 subsequently restricts
every hypothetical \((4,6)\) lci to horizontal degree \(e=0\) or \(1\), so
only15 of the36 preliminary nonregular strata satisfy that additional necessary filtration restriction. They are not current open quartic-mate existence cases after R-0001.

## Characteristic boundary

The decomposition H=A+P,K=A+Z and the principal-part quotient by the **actual** ambient restriction image are algebraic constructions over any field with the stated source and line-bundle data. The numerical e-strata here additionally use their characteristic-zero balanced conormal and no-common-singularity inputs; they must not be imported wholesale to a prime. In characteristic2 the fixed-quartic normal bundle changes. The [every-positive-characteristic quartic-carrier construction](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) is the separate positive control. A pole-divisor parameter space and correct local finite-flatness do not by themselves construct a global supported pair.
