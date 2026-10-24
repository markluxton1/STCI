# The rational quartic: projection center, automorphisms, and osculation

Date: 2026-10-24. Status: **proved arguments in a provisional research
proposal; independent audit recorded separately; no canonical promotion**.

The field is algebraically closed of characteristic zero. The object is the
fixed embedded curve

\[
\nu([s:t])=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

This note concerns its intrinsic projective geometry. It uses no
normal-bundle splitting, quartic-carrier exclusion, or STCI obstruction.
The prior [special-lines note](2026-10-24-special-lines-planes-research-note.md),
Sections 2–4, and its [independent geometry audit](2026-10-24-special-lines-planes-geometry-audit.md)
supply the calculations to be explained. The arguments needed for the new
conclusions are reconstructed below, including the endpoint jet drops.
The [symmetric-square companion](2026-10-24-quartic-symmetric-square-bitangents.md)
and [synthesis](2026-10-24-quartic-automorphisms-bitangents-synthesis.md)
explain how the same center controls the bitangent conic. No novelty claim
is intended.

## 1. Projective spaces and the center

Put

\[
W=H^0(\mathbf P^1,\mathcal O(4)),\qquad
V=\langle s^4,s^3t,st^3,t^4\rangle\subset W.
\]

Here $\mathbf P(U)$ denotes the lines in $U$. Evaluation defines the
rational normal quartic

\[
\nu_4:\mathbf P^1\hookrightarrow\mathbf P(W^\vee),\qquad
[s:t]\longmapsto[s^4:s^3t:s^2t^2:st^3:t^4].
\]

The inclusion $V\subset W$ induces the quotient $W^\vee\twoheadrightarrow
V^\vee$, hence a linear projection

\[
\pi_z:\mathbf P(W^\vee)\dashrightarrow\mathbf P(V^\vee),
\quad z=\mathbf P(V^\perp)=[0:0:1:0:0].
\tag{1.1}
\]

Thus $z$ is the middle-coefficient **functional**, not the omitted section
viewed as a point of $\mathbf P(W)$. The latter interpretation requires a
specified self-duality, given in Section 3. Hyperplanes of the target are
points of $\mathbf P(V)$; the osculating and bitangent plane maps take
values there, rather than in $\mathbf P(V^\vee)$.

## 2. Secants, tangents, and osculating spaces before projection

For $Z=[Z_0:\ldots:Z_4]\in\mathbf P(W^\vee)$ form the middle
catalecticant

\[
K(Z)=\begin{pmatrix}Z_0&Z_1&Z_2\\Z_1&Z_2&Z_3\\Z_2&Z_3&Z_4\end{pmatrix}.
\tag{2.1}
\]

At an evaluation point this has rank one. On a secant line, including a
limiting tangent line, it has rank at most two. At $z$ its determinant is
$-1$. Consequently $z$ lies outside the closed secant variety
$\sigma_2(C_4)$, and in particular outside both $C_4$ and its tangent
developable. This argument only needs the rank bound; it does not assume
a classification of secant-variety points.

Every degree-two subscheme of $C_4\cong\mathbf P^1$ spans a secant or
tangent line. Since none contains $z$, projection retains separation of
all length-two subschemes. It has no base point, and it separates both
points and tangent vectors. The associated linear system therefore gives
a closed immersion. This explains smooth embeddedness of $C$ without
checking affine charts one by one.

Write $\operatorname{Osc}^r_p(C_4)$ for the projective span of jets of
orders at most $r$. After the usual symmetric-tensor identification, the
rational normal curve consists of fourth powers $L^4$, and

\[
\operatorname{Osc}^r_{[L]}(C_4)=\mathbf P(L^{4-r}\operatorname{Sym}^r k^2).
\tag{2.2}
\]

In these polynomial coordinates $z$ is proportional to $X^2Y^2$. Hence:

- $z$ belongs to no tangent line ($r=1$).
- It belongs to exactly two osculating planes ($r=2$), at
  $p_0=[1:0]$ and $p_\infty=[0:1]$.
- It belongs to exactly the osculating hyperplanes ($r=3$) at those same
  two points.

In evaluation coordinates the two planes are

\[
\operatorname{Osc}^2_{p_0}=\mathbf P\langle e_0,e_1,e_2\rangle,
\quad
\operatorname{Osc}^2_{p_\infty}=\mathbf P\langle e_2,e_3,e_4\rangle,
\quad
\operatorname{Osc}^2_{p_0}\cap\operatorname{Osc}^2_{p_\infty}=\{z\}.
\tag{2.3}
\]

Here $e_i$ are the coordinate vectors dual to $s^{4-i}t^i$. The projection
of either exceptional second-osculating plane is only a line. The
vanishing sequence of $V$ at either endpoint is $(0,1,3,4)$, of
ramification weight two. Away from the endpoints it is $(0,1,2,3)$:
on $s\ne0$, the Wronskian of $(1,u,u^3,u^4)$ is $72u^2$.
Thus there is a unique limiting osculating plane at each endpoint, with
contact order four, although its ordinary second jet spans a line.

Equations (2.2)–(2.3) give a coordinate-free reconstruction: an unordered
pair of distinct points of the complete rational normal quartic specifies
$z$ by intersecting their second-osculating planes. Conversely this $z$
recovers the pair as the only osculating planes containing it.

## 3. Apolarity and the distinguished orbit

To compare $W^\vee$ with binary quartics, choose a volume form on the
two-dimensional parameter space. Changing that choice multiplies the
resulting self-duality by a scalar, so the projective identification is
canonical. With $m_i=s^{4-i}t^i$, use the apolar pairing

\[
\langle m_i,m_j\rangle=
\begin{cases}(-1)^i/\binom4i&i+j=4,\\0&i+j\ne4.\end{cases}
\tag{3.1}
\]

The functional $Z=(Z_i)$ corresponds to

\[
F_Z(s,t)=\sum_{i=0}^4(-1)^i\binom4i Z_i s^i t^{4-i},
\qquad \langle f,F_Z\rangle=Z(f).
\tag{3.2}
\]

The binomial coefficients are necessary. Evaluation at $[s_0:t_0]$
corresponds to $(s_0t-t_0s)^4$, whereas

\[
F_z=6s^2t^2,\qquad V=(s^2t^2)^\perp.
\tag{3.3}
\]

Thus the omitted coefficient expresses an apolar hyperplane associated
with the doubled endpoint divisor $2p_0+2p_\infty$.

The projection center belongs to the binary-quartic orbit of root type
$(2,2)$, rather than the orbit of a general quartic with four simple
roots. Its points are the squares of quadratics with two distinct roots,
and its stabilizer preserves the unordered root pair. The orbit has
dimension two. In the usual binary-quartic GIT terminology it is the
closed strictly semistable orbit: quartics with a root of multiplicity
more than two are unstable, and the other semistable double-root types
degenerate to this orbit. This terminology is supplementary; the group
and projection proofs use only the explicit root divisor. The orbit is
not closed in the whole projective space, since coalescing the two roots
gives a fourth power, which lies on $C_4$.

## 4. Full projective automorphism group

Restriction gives

\[
r:\operatorname{Aut}(\mathbf P(V^\vee),C)\longrightarrow
\operatorname{Aut}(C)=\operatorname{PGL}_2.
\]

Its kernel is trivial. Indeed a lift of an ambient automorphism fixing
$C$ pointwise has every vector representing a point of $C$ as an
eigenvector. The irreducible curve lies in the finite union of projective
eigenspaces, hence in one of them. Since $C$ spans $\mathbf P^3$, that
eigenspace is the entire vector space and the lift is scalar.

Every automorphism $a$ of $\mathbf P^1$ preserves $\mathcal O(4)$ and
acts projectively on $W$. If it extends to the given embedding, pulling
back ambient linear forms shows $a^*V=V$. Conversely $a^*V=V$ gives a
projective transformation of $\mathbf P(V^\vee)$ carrying $\nu(p)$ to
$\nu(a(p))$. Therefore

\[
\operatorname{im}(r)=\operatorname{Stab}_{\operatorname{PGL}_2}(V)
=\operatorname{Stab}_{\operatorname{PGL}_2}(z).
\tag{4.1}
\]

By (3.3), this is exactly the stabilizer of the unordered pair
$\{p_0,p_\infty\}$. Its elements are

\[
u\longmapsto au\quad\text{or}\quad u\longmapsto a/u,\qquad a\in k^*.
\tag{4.2}
\]

It is the normalizer $N(T)$ of the maximal torus fixing both endpoints
individually, with inversion as the nontrivial Weyl action. Thus

\[
\boxed{\operatorname{Aut}(\mathbf P^3,C)\cong
\mathbf G_m\rtimes\mathbf Z/2.}
\tag{4.3}
\]

Concretely, put

\[
D_a=\operatorname{diag}(1,a,a^3,a^4),\qquad
J=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
\tag{4.4}
\]

Then $D_ac(u)=c(au)$, $Jc(u)=c(1/u)$ projectively,
$J^2=1$, and $JD_aJ=a^4D_{a^{-1}}$ as matrices. These are all ambient
automorphisms. The torus has weights $0,1,3,4$ because it is the inherited
quartic representation with its weight-two line omitted.

The two distinguished points have several equivalent intrinsic
descriptions: the torus fixed points on $C$; the hyperosculating points;
the points whose second-osculating planes upstairs contain $z$; and the
two ramification points of the cubic ruling map described next.

## 5. Why the quadric and both ruling actions are forced

The multiplication map

\[
\operatorname{Sym}^2V\longrightarrow H^0(\mathbf P^1,\mathcal O(8))
\]

has monomial exponents $0,1,2,3,4,4,5,6,7,8$. Its kernel is one-dimensional,
spanned by $x_0x_3-x_1x_2$. Hence every projective automorphism preserving
$C$ preserves its unique containing quadric

\[
Q=V(x_0x_3-x_1x_2),
\]

which is smooth. Its equation is the unique equality of weight-four
products in the multiplication of actual sections. In this sense the
quadric is forced by the linear system, not an extra incidence assumption.

Under the Segre coordinates

\[
(x_0,x_1,x_2,x_3)=(A_0B_0,A_0B_1,A_1B_0,A_1B_1),
\]

our curve is the graph of

\[
[B_0:B_1]=[s:t]\longmapsto[A_0:A_1]=[s^3:t^3].
\tag{5.1}
\]

The two projections have degrees one and three on $C$. No automorphism of
the pair $(Q,C)$ can exchange the rulings, because those degrees differ.
The explicit action is

\[
D_a:([A_0:A_1],[B_0:B_1])\mapsto
([A_0:a^3A_1],[B_0:aB_1]),\qquad
J:([A_0:A_1],[B_0:B_1])\mapsto
([A_1:A_0],[B_1:B_0]).
\tag{5.2}
\]

The degree-three ruling is, up to identifying its target, the quotient by
the unique order-three subgroup $\mu_3\subset T$. Its only ramification
points are $p_0,p_\infty$, each with ramification index three. This gives
a second geometric route to the same pair, independently of apolar
coordinates.

The ruling also has a direct interpretation upstairs. Let $D$ be any
effective divisor of degree three on $C_4$, with cubic equation
$g=a s^3+b s^2t+c st^2+d t^3$. Its span is a plane, annihilated by
$H^0(\mathcal O(4)(-D))=gH^0(\mathcal O(1))$. Therefore

\[
z\in\langle D\rangle
\quad\Longleftrightarrow\quad z(sg)=z(tg)=0
\quad\Longleftrightarrow\quad b=c=0.
\tag{5.3}
\]

Thus **all** degree-three divisors whose planes contain the center form
the cubic pencil $\langle s^3,t^3\rangle$. Its reduced members are exactly
the cubic ruling fibers on $C$, and its two nonreduced members are
$3p_0,3p_\infty$. Projection contracts each such plane to its trisecant
line. For a reduced member with $u_i^3=\kappa\ne0$, a concrete
decomposition of the center is

\[
\sum_{i=1}^3u_i(1,u_i,u_i^2,u_i^3,u_i^4)=3\kappa e_2.
\tag{5.4}
\]

This is the elementary form of the degree-three apolar-decomposition
pencil of the binary quartic $X^2Y^2$. In particular the three-point
fibers and their endpoint degenerations are already encoded by the
projection center; they are not additional choices on the quadric.

There are two useful reconstruction formulas from the endpoint pair.
First, intrinsically on $\mathbf P^1$,

\[
V=H^0(\mathcal O(4)(-3p_0))+
  H^0(\mathcal O(4)(-3p_\infty)).
\tag{5.5}
\]

The summands have dimension two and zero intersection; in endpoint
coordinates they are $\langle st^3,t^4\rangle$ and
$\langle s^4,s^3t\rangle$. Second, any four-dimensional $T$-stable subspace
of $H^0(\mathcal O(4))$ is a sum of four of its five distinct weight
lines. Basepoint freedom at the two endpoints forces weights $0,4$;
immersion there forces weights $1,3$. Therefore the only such subspace
giving an embedding is $V$. An arbitrary invariant subspace is not being
assumed: basepoint freedom and immersion force the omitted middle weight.

## 6. The osculating involution is the central involution

The center of $N(T)=T\rtimes\mathbf Z/2$ is precisely
$\{1,-1\}\subset T$. An element of $T$ is central exactly when it equals
its inverse, and no endpoint-exchanging element commutes with all of
$T$. Thus there is a coordinate-free distinguished automorphism

\[
\iota=\text{the unique nonidentity central element of }
\operatorname{Aut}(\mathbf P^3,C).
\tag{6.1}
\]

Equivalently it is the unique nonidentity involution of $\mathbf P^1$
fixing $p_0,p_\infty$ individually. In endpoint coordinates it is
$u\mapsto-u$, with ambient representative
$D_{-1}=\operatorname{diag}(1,-1,-1,1)$.

This group-theoretic characterization alone would not prove that osculation
selects it. For that, the section of a plane with a triple zero at finite
$u\ne0$ has the form $(v-u)^3(v-r)$. Its middle coefficient is
$3u(u+r)$, and the apolar condition $z(f)=0$ forces $r=-u$. Hence

\[
H_u=[-u^4:2u^3:-2u:1]\in\mathbf P(V),\qquad
H_u|_C=3c(u)+c(\iota(u)).
\tag{6.2}
\]

The limiting members are $H_0=V(x_3)$ and $H_\infty=V(x_0)$, with
sections $4p_0,4p_\infty$. At an endpoint other planes through its
tangent line have contact at least three, so the limiting plane in (6.2)
is distinguished by contact four. The residual correspondence here is
that of the limiting osculating family, not all endpoint triple-contact
planes.

Upstairs $\iota$ acts by
$\operatorname{diag}(1,-1,1,-1,1)$ in evaluation coordinates. It fixes
$z$, and projection gives $D_{-1}$. Merely fixing $z$ does not characterize
$\iota$, since every element of $N(T)$ fixes $z$; the characterization is
its unique nontrivial central element. On the cubic ruling quotient,
$u^3\mapsto-u^3$. Consequently $\iota$ descends to the corresponding
central involution of the target endpoint pair, and it is not a deck
transformation of that degree-three map.

## 7. The dual action and the contact families

For an ambient point transformation $M$, a plane coefficient column
$h\in V$ transforms by $M^{-\mathsf T}h$. Thus

\[
D_a^{-\mathsf T}[h_0:h_1:h_2:h_3]
=[h_0:a^{-1}h_1:a^{-3}h_2:a^{-4}h_3],
\]

and $J$ reverses the four coordinates. Formula (6.2) gives

\[
D_a(H_u)=H_{au},\qquad J(H_u)=H_{1/u},\qquad
\iota(H_u)=H_{-u}.
\tag{7.1}
\]

The same conclusion has an intrinsic proof: an automorphism carries
contact divisors to their images and commutes with limiting osculation.
Because $\iota$ is central, the residual map remains $\iota$ under every
automorphism, including those interchanging endpoints.

For a bitangent plane $B_{p,q}$ with contact divisor $2p+2q$, the dual
action gives $g(B_{p,q})=B_{g(p),g(q)}$. In particular
$\iota(B_{u,v})=B_{-u,-v}$. It preserves the bitangent family but does not
interchange the two contacts of a general bitangent plane. The osculating
and bitangent plane families each have exactly the two endpoint members
fixed by $\iota$. For the bitangent assertion, a nonendpoint invariant
unordered contact pair would have $v=-u$; its middle-coefficient condition
would be $-2u^2=0$, impossible in characteristic zero.

## 8. Evidence and precise boundaries

The [exact verifier](../computations/verify_quartic_automorphisms_bitangents_2026_10_24.py)
checks the catalecticant, apolar normalization, Wronskian, group matrices,
and osculating formulas; its [report](../computations/quartic_automorphisms_bitangents_2026_10_24.json)
records the finite checks. The
[independent audit](2026-10-24-quartic-projection-independent-audit.md)
reconstructs the group and projection proofs separately.
Computational identities do not replace the arguments establishing
completeness of the stabilizer or the projective embedding.

The group identification, reconstruction from an unordered endpoint pair,
and explanation of the central involution are proved here for this fixed
characteristic-zero embedding. The principal invariant datum can be
recorded as either $(C_4,z)$ with $z$ of binary-quartic type $(2,2)$, or as
$C_4$ with an unordered pair of distinct points. Each recovers the other
by (2.3). The full hyperplane system, rather than abstract group action
alone, determines the bitangent conic; the companion note makes that
distinction precise.

No normal-bundle theorem or carrier exclusion was used. No STCI case is
closed or reopened, and no canonical result record is introduced.
Characteristic two requires separate treatment: the apolar self-duality
and binomial normalizations in Section 3 are not valid there, and the
principal results are not asserted by reduction of these formulas.
