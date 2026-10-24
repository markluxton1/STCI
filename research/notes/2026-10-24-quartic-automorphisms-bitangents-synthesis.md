# One endpoint pair, two conics, and the geometry of the rational quartic

Date: 2026-10-24. Status: **exploratory research with proofs and independent
audits; no canonical promotion**. Throughout the main discussion, the field
is algebraically closed of characteristic zero and

\[
C=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3.
\]

This investigation concerns the embedding, its automorphisms, projection,
and contact correspondences. No STCI assertion is proposed. The accepted
normal-bundle splitting and carrier exclusions are neither reproved nor
used in the proofs here.

## 1. Evidence and reading route

The repository route was [INDEX](../INDEX.md),
[STATE](../STATE.md), [FRONTIER](../FRONTIER.md), and
[AUTHORITY](../AUTHORITY.md). These navigation files do not establish new
mathematics. The starting evidence was the
[special-lines research note](2026-10-24-special-lines-planes-research-note.md)
and its [independent geometry audit](2026-10-24-special-lines-planes-geometry-audit.md)
on `codex/special-lines-planes-2026-10-24`, base commit
`51dc4772e6a2b028a1d9559a4bcfbd69be9bd0d6`.
The contact identities needed for the new arguments were reconstructed;
the endpoint jet drops and the earlier audit's correction of the reduced
dual singular locus remain relevant cautions.

The self-contained proof notes are:

- [Projection, linear system, and full automorphism group](2026-10-24-quartic-projection-automorphisms.md).
- [Symmetric square, bitangent conic, and correspondences](2026-10-24-quartic-symmetric-square-bitangents.md).
- [Literature, projection moduli, and characteristic-two outlook](2026-10-24-quartic-invariant-literature-outlook.md).

Independent reconstruction is recorded in the
[projection/group audit](2026-10-24-quartic-projection-independent-audit.md)
and [symmetric-square audit](2026-10-24-quartic-symmetric-independent-audit.md).
These are reviews of research evidence; none is a numbered canonical result.

## 2. The smallest common datum

Let $W=H^0(\mathbf P^1,\mathcal O(4))$ and
$V=\langle s^4,s^3t,st^3,t^4\rangle$. The center of the linear projection
is the annihilator point $z=\mathbf P(V^\perp)$ in $\mathbf P(W^\vee)$.
The relevant map is the quotient $W^\vee\to V^\vee$; its targets must not
be confused with projective spaces of sections.

The center lies outside the secant variety of the complete rational normal
quartic $C_4$. Its middle catalecticant has determinant $-1$, so projection
separates every length-two subscheme and gives a closed immersion. Under
the characteristic-zero equivariant binary-form duality, $z$ is represented
by a scalar multiple of $s^2t^2$, a form with two double roots. This is a
special orbit of smooth projection centers, not a generic center.

There is a description that avoids choosing a binary-form identification:

\[
z=\operatorname{Osc}^2_{p_0}(C_4)
   \cap\operatorname{Osc}^2_{p_\infty}(C_4).
\tag{2.1}
\]

These are exactly the two osculating planes of $C_4$ containing the center.
Thus the complete embedding together with the unordered pair
$E=\{p_0,p_\infty\}$ reconstructs the center and hence $V$. Conversely the
center recovers this pair. The same points are recovered downstairs as the
two hyperosculating points, or as the two totally ramified points of the
degree-three ruling map. These descriptions are proved to agree in the
projection note.

![Projection and reconstruction diagram](../figures/quartic-geometry-2026-10-24/projection-center.png)

The figure is schematic: a projective four-space is not being drawn as a
metric three-space. Its arrows record the actual quotient and embedding
maps. [Vector version](../figures/quartic-geometry-2026-10-24/projection-center.svg).

## 3. Why the symmetry and the quadric are inevitable

An ambient projectivity preserving $C$ restricts faithfully to its parameter
line. Its image consists exactly of automorphisms preserving $V$, hence
stabilizing $z$. The two double roots of the dual center imply

\[
\operatorname{Aut}(\mathbf P^3,C)
\cong N(T)=\mathbf G_m\rtimes\mathbf Z/2,
\qquad T=\operatorname{Aut}(\mathbf P^1;p_0,p_\infty).
\tag{3.1}
\]

Here $u\mapsto au$ gives
$\operatorname{diag}(1,a,a^3,a^4)$ and endpoint interchange is the coordinate
reversal. The latter conjugates $a$ to $a^{-1}$. The restriction kernel is
trivial, not merely finite.

The quadric follows from the factorization

\[
V=H^0(\mathcal O(1))\cdot\langle s^3,t^3\rangle.
\tag{3.2}
\]

The four coordinates form a rank-one $2\times2$ matrix. Its determinant is
$x_0x_3-x_1x_2$, and the quadratic multiplication map has a one-dimensional
kernel. Consequently $Q$ is the unique containing quadric and is preserved
by every automorphism of the embedded curve. On $Q$ the curve is the graph
of $[s:t]\mapsto[s^3:t^3]$. The ruling degrees on $C$ are one and three;
an automorphism preserving $C$ cannot exchange the rulings.

There is an explanation of that cubic pencil directly upstairs. A degree-three
divisor with equation $g=a s^3+b s^2t+c st^2+d t^3$ spans a plane containing
$z$ precisely when $z(sg)=z(tg)=0$, or $b=c=0$. Thus the entire pencil
$\langle s^3,t^3\rangle$ consists of exactly the three-point spans containing
the center, including the nonreduced endpoint members. Projection sends
these planes to the trisecant ruling lines. The cubic ruling is already
encoded by the rank-three decompositions of the projection center.

The osculating involution has a particularly short intrinsic description:
it is the unique nonidentity central element of $N(T)$, equivalently the
unique nonidentity involution fixing both points of $E$ individually.
Its coordinate expression is $u\mapsto-u$. Proving that this element is
the osculating residual map still requires contact geometry; the identity
$H_p|_C=3p+\iota(p)$ supplies that proof. It descends through the cubic
quotient $C\to C/\mu_3$, but is not a deck transformation of that quotient.

## 4. Why the bitangent multiplier has trace minus four

Set $U=H^0(\mathbf P^1,\mathcal O(2))$, so that
$\operatorname{Sym}^2(C)=\mathbf P(U)$ by taking the zero divisor of a
quadratic. There are two natural conics in this plane:

\[
\mathcal D:\ \beta^2-4\alpha\gamma=0,
\qquad
\mathcal B:\ z(h^2)=\beta^2+2\alpha\gamma=0,
\quad h=\alpha s^2+\beta st+\gamma t^2.
\tag{4.1}
\]

The first is the diagonal of double points. The second is the locus whose
doubling is a hyperplane section of $C$. Their scheme intersection is
$2[2p_0]+2[2p_\infty]$: the conics are tangent at those two points.
Invariance and tangency alone leave a pencil of conics
$\beta^2+\lambda\alpha\gamma=0$ and do not determine $\lambda$.

The decisive additional **condition** is intrinsic to the already given
diagonal. Write $D$ for its nonsingular polar form and $B$ for a candidate
conic form. Multiplication

\[
m:\operatorname{Sym}^2U\longrightarrow H^0(\mathcal O(4))
\]

has one-dimensional kernel spanned by the inverse discriminant tensor.
Its dual image is therefore exactly the hyperplane
$\operatorname{tr}(D^{-1}B)=0$. For an invariant candidate, the eigenvalues
of $D^{-1}B$ are

\[
1,\ -\lambda/4,\ -\lambda/4.
\]

The trace-free condition forces $\lambda=2$. Equivalently the ratio of
the simple eigenvalue to the repeated eigenvalue is $-2$. This constructs
$\mathcal B$ uniquely from the polar geometry of $\mathcal D$ and the
endpoint-preserving group. It requires no extra independent embedding
datum, although it requires more than an assertion of invariance.

![The diagonal and bitangent conics](../figures/quartic-geometry-2026-10-24/symmetric-square-conics.png)

This real affine slice uses $\alpha+\gamma=1$, $x=\alpha-\gamma$,
$y=\beta$. The equations become $x^2+y^2=1$ and $x^2-2y^2=1$.
It illustrates the two tangent intersections; the proofs concern the
whole projective plane over the specified algebraically closed field.
[Vector version](../figures/quartic-geometry-2026-10-24/symmetric-square-conics.svg).

For a nonendpoint bitangent pair $p,q$, choose any parameter with endpoints
$0,\infty$ and put $r=u(q)/u(p)$. Rescaling the parameter does not change
$r$; interchanging either the endpoints or the contacts replaces it by
$r^{-1}$. This unordered cross-ratio is thus intrinsic. Substitution in
the conic gives

\[
r+r^{-1}=-(2+\lambda)=-4,
\qquad \{r,r^{-1}\}=\{-2+\sqrt3,-2-\sqrt3\}.
\tag{4.2}
\]

The representation-theoretic multiplication and the polar trace explain
the value; the ratio equation alone merely expresses it in coordinates.
The intersection numbers of the two conics, which remain the same through
the invariant pencil, cannot explain it. For comparison, the osculating
pair has cross-ratio $-1$, the harmonic involution of the endpoint pair.

## 5. Two cautions about parameter spaces

The secant-line map from $\operatorname{Sym}^2 C$ to the Grassmannian
extends to tangent lines along the diagonal. It retains the unordered pair
on an ordinary secant, but a general trisecant has three different inverse
pairs. At either endpoint tangent trisecant the inverse fiber is one
nonreduced point of length three; locally its ideal can be written
$(\alpha-\beta^2,\beta^3)$. Thus this finite birational map is not an
embedding. This loss of information matters even though $C$ itself is
smoothly embedded.

The ordered bitangent correspondence is the reduced union
$\mathcal R=\Gamma_\rho\cup\Gamma_{\rho^{-1}}\subset C\times C$, not an involution.
Each component maps isomorphically to the unordered conic $\mathcal B$;
the two components meet transversely at the endpoint diagonal points.
By contrast, the osculating graph maps with degree two to the line of
unordered pairs $\{p,\iota(p)\}$. As correspondence cycles,

\[
\mathcal R\circ\mathcal R
=\Gamma_{\rho^2}+2\Delta_C+\Gamma_{\rho^{-2}}.
\tag{5.1}
\]

The multiplicity two counts the two return paths. The scheme-theoretic
image of the fiber-product composition is already reduced and has each
of these three graphs with multiplicity one. The subgroup
$\langle\rho,-1\rangle\subset T(k)$ is
isomorphic to $\mathbf Z\times\mathbf Z/2$ and is Zariski dense in $T$;
it gives an infinite contact orbit on the open torus orbit.
Its common fixed points and all the indicated contact coalescences are
exactly the two distinguished endpoints.

## 6. Moduli and the characteristic-two boundary

The surrounding geometry is classical. The
[literature/outlook note](2026-10-24-quartic-invariant-literature-outlook.md)
records the sources actually inspected and their precise use: Bernardi's
projection criterion and apolarity, and Isaev's binary-quartic invariants
and strictly semistable orbit description. No novelty claim is made.

For normalized binary quartic invariants $I,J$, the embedding locus of
centers is $J\ne0$. Its coarse invariant quotient is the affine line with
coordinate $I^3/J^2$. Our center has value $27$ and is the closed
double-double orbit in the semistable locus. A distinct, nonclosed orbit
with one double root has the same coarse value and also gives a smooth
projected quartic. The quotient stack retains this distinction and the
positive-dimensional stabilizer. Collision of roots of the auxiliary
binary center must therefore be distinguished from singularity of the
projected curve.

In fact this is the unique projective-equivalence class of smooth embedded
rational quartics in $\mathbf P^3$ with a positive-dimensional projective
automorphism group. A center with at least three distinct binary roots has
finite stabilizer; root types $(4)$ and $(3,1)$ lie on the secant cubic;
only the double-double orbit remains. The literature/outlook note gives
the complete short argument, including why all these quartic embeddings
arise as point projections of $C_4$.

In characteristic two the actual subsystem still embeds the curve, the
Segre quadric and separable cubic ruling survive, and the stabilizer of
$V$ remains the smooth torus normalizer. The central subgroup $\mu_2$ is
nonreduced and its nonidentity characteristic-zero point collapses.
The bitangent incidence conic becomes $\beta^2=0$, while the reduced
diagonal is a line. The limiting osculating-plane map is purely
inseparable of degree four onto a line, with section $4p$ at every point.
The characteristic-zero self-duality and trace-free argument cannot be
transported unchanged. These observations are a brief outlook, not a
classification in positive characteristic.

## 7. Reproduction and review boundary

The exact checker and its recorded output are
[the verifier](../computations/verify_quartic_automorphisms_bitangents_2026_10_24.py)
and [the JSON evidence](../computations/quartic_automorphisms_bitangents_2026_10_24.json).
It verifies the explicit algebra supporting the proofs; it does not turn
finite identity checks into a proof of a group or moduli classification.
The figures are regenerated by
[the drawing script](../computations/draw_quartic_geometry_2026_10_24.py).
The audit notes record reviewer reconstruction and any corrections.

All conclusions here are restricted to this fixed characteristic-zero
embedding unless a section explicitly says otherwise. No canonical result
or question record is changed; no existing STCI case is reopened or closed.
