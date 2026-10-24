# Independent audit: projection, automorphisms, moduli, and characteristic two

Date: 2026-10-24. Reviewer: independent agent `audit_projection`.
Status: **independent reconstruction completed; reviewed exploratory
research, not canonical promotion**.

The principal object is the fixed smooth rational quartic
$[s:t]\mapsto[s^4:s^3t:st^3:t^4]$ over an algebraically closed field of
characteristic zero. Characteristic two is considered only in Section 6.
The reviewer read [INDEX](../INDEX.md), the authority and contribution
instructions, and the earlier [special-lines geometry audit](2026-10-24-special-lines-planes-geometry-audit.md),
then reconstructed the arguments before reading the new full drafts.
No normal-bundle calculation, carrier exclusion, or STCI obstruction was
used or rerun.

Reviewed sources are the [projection note](2026-10-24-quartic-projection-automorphisms.md),
the [literature/outlook note](2026-10-24-quartic-invariant-literature-outlook.md),
and Sections 2, 3, and 6 of the [synthesis](2026-10-24-quartic-automorphisms-bitangents-synthesis.md).
The symmetric-square and correspondence claims have a
[separate independent audit](2026-10-24-quartic-symmetric-independent-audit.md).

**Outcome:** no substantive mathematical discrepancy was found in the
reviewed final arguments. Two distinctions checked especially carefully
are the closed orbit *inside the semistable locus*, and the difference in
characteristic two between the reduced diagonal image and the double-line
discriminant divisor. Both are correctly maintained. The endpoint
reconstruction formula suggested during this audit was added to the
projection note; it strengthens the intrinsic explanation without changing
the claimed group.

## 1. Projection center and exceptional osculating spaces

With $W=H^0(\mathcal O_{\mathbf P^1}(4))$ in its monomial basis, the
annihilator of the four-dimensional subsystem is the functional
$z=e_2\in W^\vee$. Thus the projection comes from the quotient
$W^\vee\to V^\vee$. It is not a projection between the projective spaces
of sections. At the center the middle Hankel matrix is

\[
\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},
\qquad \det=-1.
\]

Every secant or limiting tangent point of the rational normal quartic
has Hankel rank at most two. This gives a direct proof that the center
lies outside the closed secant variety; no classification of binary
forms is needed for this step. Separation of every length-two subscheme
of $\mathbf P^1$ then proves that projection is a closed immersion.

Independently, on the finite chart set
$v(u)=(1,u,u^2,u^3,u^4)$. Membership of $e_2$ in the span of
$v,v',v''$ forces the coefficient of $v$ to be zero from its first
coordinate and that of $v'$ to be zero from the second. The coefficient
of $v''$ is $1/2$, and the fourth coordinate is then $3u$. Thus only
$u=0$ works. For the span through $v'''$, the added coefficient is
$-u/2$ and the fifth coordinate becomes $-6u^2$, again forcing $u=0$.
The reversed chart gives precisely the other endpoint. This checks the
claim about both second- and third-osculating spaces, including infinity.
No tangent span contains the center.

The endpoint osculating planes are
$\mathbf P\langle e_0,e_1,e_2\rangle$ and
$\mathbf P\langle e_2,e_3,e_4\rangle$, with intersection exactly $z$.
Their projection drops to a line. The vanishing sequence is
$(0,1,3,4)$ there, while the Wronskian on the finite chart is $72u^2$.
Consequently the distinction between an endpoint second jet and the
limiting contact-four plane is necessary and correctly made.

## 2. Duality conventions and the complete automorphism group

For $m_i=s^{4-i}t^i$, the asserted apolar form pairs $m_i,m_{4-i}$
with $(-1)^i/\binom4i$. Substitution of

\[
F_Z=\sum_i(-1)^i\binom4i Z_i s^i t^{4-i}
\]

gives $\langle m_i,F_Z\rangle=Z_i$ term by term. In particular an
evaluation functional at $[s_0:t_0]$ becomes
$(s_0t-t_0s)^4$, and $e_2$ becomes $6s^2t^2$. The normalization and
alternating reversal are correct. Only the projective identification
is independent of the chosen volume form, as the note states.

The kernel of ambient restriction is trivial: any linear representative
fixing $C$ pointwise has every curve point as an eigenline. An irreducible
nondegenerate curve cannot lie in a finite union of proper eigenspaces.
Thus the representative is scalar. This also covers a nonsemisimple
representative, since its eigenvectors still form the union of its
ordinary eigenspaces.

The image of restriction is exactly the subgroup preserving $V$:
necessity follows by pulling back ambient linear forms, and sufficiency
by the induced projectivity of $V^\vee$. Under apolarity the stabilizer
of $V$ is the stabilizer of the double-double root divisor. It is precisely
the subgroup preserving its unordered support, namely
$u\mapsto au$ or $u\mapsto a/u$. This proves completeness of the
torus-normalizer answer and excludes an unexamined larger finite extension.
The matrices $D_a$ and coordinate reversal $J$ act as stated, and
$JD_aJ=a^4D_{a^{-1}}$ verifies the inversion action projectively.

There is also an independent coefficient check. For substitution
$(s,t)\mapsto(as+bt,cs+dt)$, the middle coefficients of the four
sections are

\[
6a^2b^2,\quad3ab(ad+bc),\quad3cd(ad+bc),\quad6c^2d^2.
\]

Over a field of characteristic zero their vanishing and invertibility
force a diagonal or antidiagonal matrix. This check supports, but is
not a substitute for, the intrinsic stabilizer proof.

## 3. Reconstructing the system, quadric, and trisecant ruling

The endpoint pair recovers the subsystem by the intrinsic direct sum

\[
V=H^0(\mathcal O(4)(-3p_0))\oplus
H^0(\mathcal O(4)(-3p_\infty)).
\]

Each summand has dimension two and their intersection has negative degree.
This confirms that reconstructing the center from the two complete
osculating planes does reconstruct the entire embedded linear system.

The quadratic multiplication map has exactly one monomial repetition,
at weight four. Its kernel is therefore one-dimensional and gives the
smooth quadric $x_0x_3-x_1x_2=0$. The Segre parametrization makes the
curve the graph of $u\mapsto u^3$, so the ruling degrees are one and
three. They cannot be interchanged by an automorphism preserving $C$.
The diagonal and antidiagonal actions on the two factors agree with
the displayed ambient matrices. The cubic map is the quotient by
$\mu_3\subset T$ and its two ramification points agree with the
projection-theoretic endpoint pair.

The additional classification of center-containing planes of degree-three
divisors was also independently checked. If
$g=a s^3+b s^2t+c st^2+d t^3$ cuts out such a divisor $D$, its span
is annihilated by $gH^0(\mathcal O(1))$. Thus $z$ lies in that span
if and only if the two middle coefficients of $sg$ and $tg$, namely
$c$ and $b$, vanish. The full pencil is consequently
$\langle s^3,t^3\rangle$. In characteristic zero it has reduced
three-point fibers except at its two triple endpoints. Projection
contracts these planes to exactly the cubic-ruling trisecants.

For $u_i^3=\kappa\ne0$, the sum in projection-note equation (5.4)
has coordinates $(\sum u_i,\sum u_i^2,\sum u_i^3,\sum u_i^4,
\sum u_i^5)=(0,0,3\kappa,0,0)$. This verifies the explicit rank-three
decomposition and its relation to the entire ruling pencil.

## 4. Central involution, osculation, and dual action

In $N(T)=T\rtimes\mathbf Z/2$, central torus elements satisfy $a=a^{-1}$;
no endpoint-exchanging element commutes with every torus element. Hence
the unique nonidentity central element is $a=-1$. This characterization
is intrinsic to the group acting on $C$, and is stronger than merely
saying that the element fixes the projection center.

The residual osculating map still requires a geometric calculation.
The coefficient of $v^2$ in $(v-u)^3(v-r)$ is $3u(u+r)$, so for
nonendpoint $u$ the allowed residual point is $r=-u$. The endpoint
limits are the unique contact-four members, not all planes through
the endpoint tangent. Thus the group characterization and the contact
characterization do coincide.

The dual action is $h\mapsto M^{-\mathsf T}h$. Applying it to
$[-u^4:2u^3:-2u:1]$ gives the parameters $au$ and $1/u$ for $D_a$
and $J$, respectively. The same pushforward of contact divisors gives
$g(B_{p,q})=B_{g(p),g(q)}$. A generic bitangent pair is not exchanged
by $-1$: that would force $v=-u$ and violate the bitangent equation.
The two contact-family fixed members are precisely the endpoint members.
Finally $(-u)^3=-u^3$ verifies descent of the involution to the cubic
quotient, and also shows it is not a deck transformation.

## 5. Moduli statement and literature boundary

The reviewer independently inspected
[Isaev, Section 3, printed pp. 476–477](https://imar.ro/journals/Revue_Mathematique/pdfs/2015/4/5.pdf#page=6).
It explicitly distinguishes the two strictly semistable root types,
their dimensions and closure relation, and the classical invariants
of degrees two and three. The source is over $\mathbf C$; the root
arguments and invariant formulas here have the stated characteristic-zero
scope. Its associated-form involution is not used as an identification
of our osculating involution.

The geometric argument identifying the secant hypersurface with the
irreducible Hankel determinant is sound: the secant variety is an
irreducible threefold, lies in the determinant cubic, and that cubic is
irreducible by the relatively-prime linear coefficient and constant
coefficient argument in the literature note. Thus the embedding locus
is exactly $J\ne0$.

Using the classical invariant ring $k[I,J]$, localization followed by
degree zero gives $k[I^3/J^2]$, so the asserted coarse invariant
quotient is an affine line. Independently substituting both
$s^2t^2$ and $s^2(s^2+t^2)$ gives
$I=1/12$, $J=-1/216$, and $I^3/J^2=27$ in the chosen normalization.
Both are in the embedding locus, although their root types and orbits
differ. The coarse quotient therefore fails to distinguish them.
The double-double orbit is closed in the semistable locus, not in the
whole projective space. The synthesis correctly retains this qualifier.

These moduli conclusions rely on the stated classical invariant-ring
input. Finite symbolic substitutions alone would not establish that
input or a good-quotient theorem.

The subsequently added characterization by positive-dimensional
automorphisms was independently re-read and is sound. A smooth integral
rational quartic in $\mathbf P^3$ is nondegenerate: containment in a
plane would make it a smooth plane quartic of genus three, and containment
in a line is incompatible with degree four. Its four-dimensional
hyperplane subsystem therefore lies in the five-dimensional complete
system $H^0(\mathbf P^1,\mathcal O(4))$ and defines a point projection
of $C_4$. The restriction-kernel and subsystem-stabilizer proofs above
apply to every such embedding. A binary root divisor with at least
three distinct support points has finite stabilizer, by its faithful
action on that finite set. Of the remaining types, $(4)$ and $(3,1)$
have zero catalecticant and cannot give embeddings, while $(2,2)$ is
the single orbit already studied and has a one-dimensional stabilizer.
This proves the asserted uniqueness among smooth embedded rational
quartics in characteristic zero. The corresponding synthesis paragraph
has the same scope. This is an elementary consequence of the preceding
projection and stabilizer classification, not an extra novelty claim.

## 6. Characteristic-two checks and scheme distinctions

This section explicitly changes the characteristic. The ordinary
characteristic-zero apolar identification cannot simply be reduced;
the literature note correctly returns to the actual section space and
its dual. The two affine charts still exhibit the map as a closed
immersion, and $u^3$ remains separable.

Reducing the independently computed middle coefficients gives
$0,ab\det(g),cd\det(g),0$. On the open invertible-matrix locus,
$ab=cd=0$ is the disjoint union of diagonal and antidiagonal tori:
the opens where $ad$ or $bc$ is invertible cover it and force the
other two entries to vanish. Thus the stabilizer is the smooth
normalizer scheme, not a newly nonreduced enlargement. Its central
$\mu_2$ is nonreduced, while $-1$ is the identity geometric point.

For $h=\alpha s^2+\beta st+\gamma t^2$, the missing coefficient of
$h^2$ is $\beta^2$. The bitangent incidence scheme is a double line.
The actual scheme-theoretic image of $p\mapsto2p$ is the reduced line
$\beta=0$, parametrized by Frobenius; the specialized discriminant
polynomial defines its double. These are distinct schemes, and the
final outlook correctly says so.

Hasse derivatives of $(1,u,u^3,u^4)$ of orders one and two are
$(0,1,u^2,0)$ and $(0,0,u,0)$. At nonzero finite $u$ they give
the plane $x_3+u^4x_0=0$, with restricted section $(v+u)^4$.
The endpoint rank drops have the indicated limiting contact-four
planes. The resulting map is the degree-four purely inseparable map
onto a line in the dual projective space. No inference about a
characteristic-two orbit classification or a full nonreduced
correspondence is warranted or claimed.

## 7. Reproduction, corrections, and remaining scope

The reviewer used an independent SymPy 1.14.0 calculation, separate from
the submitted verifier, for the substitution coefficients, maximal-minor
gcds of $[v,v',\ldots,v^{(r)},e_2]$ for $r=1,2,3$, and the two
invariant evaluations. The nonzero-minor gcds on the finite chart were
$1$, $6u$, and $72u^2$, respectively. The reversed chart was checked
by the endpoint symmetry. These are checks of explicit identities;
the completeness, scheme, and quotient arguments are supplied above.

No incorrect mathematical assertion was retained after this review.
The reviewer requested the explicit endpoint reconstruction formula
and emphasized the reduced-diagonal/double-discriminant distinction;
both are present. The final cubic-plane pencil addition was rechecked.
No unresolved mathematical defect was identified within this audit's
scope. This does not certify the unreviewed parts by association, and
does not constitute canonical promotion, a novelty claim, or any STCI
conclusion.
