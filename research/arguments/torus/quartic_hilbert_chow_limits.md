# Exceptional quartic Hilbert-over-Chow limits

This file owns the Chow-closure, flat-limit and characteristic-two consequences
of the exceptional quartic pencils classified in
[Quartic pencils with the fixed Chow polytope](quartic_chow_pencils.md).
Put
\[
A=x_1^3-x_0^2x_2,\qquad B=x_2^3-x_1x_3^2,\qquad
D=x_1^2x_2^2-x_0^2x_3^2,
\]
and
\[
F_\lambda=\lambda x_2A+x_1B,\qquad
G_\lambda=D+\lambda x_1A+\lambda^{-1}x_2B. \tag{1}
\]
The classification and uniqueness of the family remain in the canonical
[liaison/canonical-module proof](quartic_chow_pencils.md#two-translates-with-coinciding-cubic-jets).

## Chow closure and full opposite limits

The first moment vanishes on (1) by cancellation of the two opposite
ratios. On the invariant family, write \(v=\alpha+\beta u\) and the second
equation as \(u^4+\gamma u v^2+\eta v^3=0\). The root coordinate
\(\rho=u/v\) gives
\(\alpha\rho^4+(\gamma\rho+\eta)(1-\beta\rho)=0\).
The roots and their multiplicities correspond, since \(1-\beta\rho\)
is nonzero at each root. The missing cubic term gives the first moment
by Viète's formula, including in characteristic two. In that characteristic
the first moment also vanishes at a single support since its multiplicity
is four.

The exceptional cycles lie outside the Chow closure of invariant quartic
realizations. Specialize any proposed family along a trait and extend
the two generator lines by projectivity. The projective closure of the
single-translate orbit gives a proper labeling space via its four-fold
product. After finite base change the four labels specialize, and each
degree-four label in the target sum is one of the two prescribed quartics
by positivity and degree. Thus the labeled traits stay in the open
orbit, and polynomial incidence forces both limiting quartics to
contain both translates. For the normalized supports, the limiting
weight-four and weight-twelve lines are necessarily \(k x_1 A\) and
\(k x_2 B\). These forms are coprime, so their intersection is the flat
CI limit. Its cycle contains the line \(x_1=x_2=0\), a contradiction.

The \(H\) action on the exceptional fiber sends \(\lambda\) to
\(h^{-4}\lambda\) when acting on equations by weight substitution.
At \(\lambda=0\), the pencil itself tends to \(\langle x_1B,x_2B\rangle\).
Put \(D_0=x_0^2 D-x_1^2x_2 A\). The **saturated flat limit ideal** is
\[
J_0=(x_1 B,\ x_2 B,\ x_0^2 B,\ A^2,\ D_0). \tag{4}
\]
Indeed use \(G'=\lambda G_\lambda\) and the cancellation
\(x_2F_\lambda-x_1G'=-\lambda(x_0^2B+\lambda x_1^2 A)\).
Writing \(K_0=x_0^2B+\lambda x_1^2 A\), the next cancellations are
\(x_0^2F_\lambda-x_1 K_0=-\lambda A^2\) and
\(x_0^2G'-x_2 K_0=\lambda(D_0+\lambda x_0^2x_1 A)\).
All five generators of (4) therefore specialize from the parameter
saturation.

The identification of the entire special ideal and its Hilbert
function can be proved by **Hilbert--Burch and an exact sequence**,
without a Gröbner order or monomial count. Put
\[
 I'=(B,A^2,D_0),\qquad T=(x_1,x_2,x_0^2),\qquad
 H_5=2x_0^2x_1^2x_2-x_1^5.
\]
The two relations
\[
 x_0^4B-x_2A^2-x_1D_0=0,\qquad
 H_5B-x_3^2A^2-x_2^2D_0=0
\]
are the columns of the Hilbert--Burch matrix
\[
 \Phi=
 \begin{pmatrix}
 x_0^4&H_5\\
 -x_2&-x_3^2\\
 -x_1&-x_2^2
 \end{pmatrix}. \tag{FL1}
\]
Its signed maximal minors are precisely \(B,A^2,D_0\).
Since \(A\) and \(B\) are coprime, \(I'\) has height two.
Hilbert--Burch gives
\[
 0\longrightarrow S(-7)\oplus S(-8)
 \xrightarrow{\Phi}S(-3)\oplus S(-6)^2
 \longrightarrow I'\longrightarrow0. \tag{FL2}
\]
In particular, \(S/I'\) is arithmetically Cohen--Macaulay,
and its Hilbert series is
\[
 H_{S/I'}(q)=
 \frac{1-q^3-2q^6+q^7+q^8}{(1-q)^4}. \tag{FL3}
\]
Geometrically, this is the **pure doubled divisor** supported on
\(C_+\cup C_-\) inside the cubic carrier \(B=0\):
away from the endpoints, the relation
\(x_1D_0+x_2A^2=x_0^4B\) makes \(I'=(B,A^2)\);
the two curves are regular and \((A,B)\) give transverse parameters.
Their multiplicities are two, accounting for all sixteen degrees
of the Cohen--Macaulay determinantal curve. The Hilbert polynomial
of this pure quotient is \(16n-34\).

The five-generator ideal (4) is \(J_0=(A^2,D_0)+BT\).
The Hilbert--Burch relations in (FL2) identify
\[
 (A^2,D_0):B=(x_0^4,H_5)\subset T,\qquad
 J_0:B=T.
\]
Consequently multiplication by \(B\) gives a short exact
sequence of graded modules
\[
 0\longrightarrow (S/T)(-3)
 \xrightarrow{\ \cdot B\ } S/J_0
 \longrightarrow S/I'\longrightarrow0. \tag{FL4}
\]
Here \(S/T\simeq k[x_0,x_3]/(x_0^2)\) is the structure
module of a length-two scheme at \(p_\infty\).
Thus (FL4) geometrically exhibits the embedded
endpoint correction and gives
\[
 \begin{aligned}
 H_{S/J_0}(q)
 &=\frac{1-q^3-2q^6+q^7+q^8}{(1-q)^4}
   +\frac{q^3(1+q)}{1-q}\\
 &=\frac{(1-q^4)^2}{(1-q)^4},
 \end{aligned} \tag{FL5}
\]
the Hilbert series of a \((4,4)\) complete intersection.
The first and last terms of (FL4) are Cohen--Macaulay of
dimensions one and two, respectively. The depth lemma
gives \(\operatorname{depth}(S/J_0)\ge1\); hence \(J_0\)
is already saturated.

The generators in (4) come from the parameter-saturated
family, so \(J_0\) is contained in its special ideal.
The generic fiber is a proper \((4,4)\) complete intersection,
and each degree of the parameter-saturated family is a
torsion-free finite module over the parameter DVR, hence free.
Its special fiber therefore has the same Hilbert function as
the generic fiber. Equation (FL5) forces equality of the
special ideal with \(J_0\). This proves the **full scheme**
limit, not only its cycle or pure hull.

Reversal sends
\(\lambda\) to \(\lambda^{-1}\), giving the other full limit and embedded
length two at \(p_0\). The cycles agree throughout this family.
For a separate invariant of the original pairs, see the
[endpoint different](chow_endpoint_different.md#colength-and-finite-detection).

## Hilbert over Chow, and the characteristic-two collision

For a fixed exceptional cycle, the ideals \((F_\lambda,G_\lambda)\)
give a nonconstant \(H\simeq\mathbf G_m\)-orbit in the Hilbert
fiber over a **single Chow point**. The two saturated opposite limits
are fixed Hilbert points above that same cycle. The original pairs
are proper complete intersections; their limiting ideals have extra
generators and embedded endpoint length two, despite having the
unchanged fundamental cycle. Thus the Chow polytope (indeed the
entire Chow point) cannot recover the vertical Hilbert orbit.
The appropriate classical comparison is the Hilbert-state-polytope
and Gröbner-degeneration theory of
[Bayer--Morrison, *Standard bases and geometric invariant theory I*](https://doi.org/10.1016/S0747-7171(88)80043-9).
No explicit projected state polytope or general conservation law
equating different jumps to embedded length is asserted.

There is also a **single-support** phenomenon in characteristic two,
which must not be confused with the multi-support classification.
Specialize (1) at \(\lambda=1\) and reduce modulo two:
\(F=x_2A+x_1B,\ G=D+x_1A+x_2B\).
Direct expansion gives
\[
 A^2=(x_0^2+x_1x_2)F+x_1^2G,\qquad
 B^2=(x_1x_2+x_3^2)F+x_2^2G
 \quad(\operatorname{char}k=2).
\]
The reduced support of \(V(A,B)\) is \(C_0\) together with
\(L=V(x_1,x_2)\). On \(L\), \(G=x_0^2x_3^2\),
so the only points of \(L\) retained by the pair are
\(p_0,p_\infty\in C_0\). Thus \(\sqrt{(F,G)}=I_{C_0}\).
The pair is proper since a common surface factor of \(F,G\)
would divide both \(A^2,B^2\), whereas \(A,B\) are coprime.
Its ideal is non-invariant, as the distinct intrinsic weights of
both generators show. This is a characteristic-two
\((4,4)\) STCI presentation with a \((2,2)\) generic-characteristic
support splitting; it is different from the familiar four-distinct-
translate binomial splitting \((1,1,1,1)\).
This explicit characteristic-two construction makes
**no claim** to classify all multi-support quartic pencils
in that characteristic. The full uniqueness theorem
above is stated and proved in characteristic zero.
