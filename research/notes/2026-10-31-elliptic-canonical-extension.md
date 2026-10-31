# Canonical reconstruction and extension of the elliptic projection data

October 31, 2026. Proposed by `elliptic_extension_selection`.
Status: **independently reviewed provisional general construction criterion**,
with the [scope-specific proof and strategy audit](2026-10-31-elliptic-canonical-extension-audit.md).
This note supplies a sufficient global source-extension mechanism. It does
not supply an admissible carrier, a mate, a new exclusion, or a canonical
promotion.

**Subsequent fixed-target disposition:** the
[palindromic target test](2026-10-31-palindromic-polarization-spin.md) now
passes its exact target replay but fails the first component-polarization
gate. Its proposed cone construction is therefore stopped before residues
or contact. The general conditional criterion below is unchanged.

## 1. Input and the new geometric object

Work over an algebraically closed field of characteristic zero. Keep the
literal target curve
\(C_0=[s^4:s^3t:st^3:t^4]\) in the smooth target quadric
\(Q=(x_0x_3-x_1x_2=0)\). Suppose that the abstract target incidence consists
of a smooth elliptic curve \(E\), four distinct points \(P_i\), and a map
\(h_E:E\to Q\) birational onto an integral curve \(C'\ne C_0\).
Write \(Z=\sum P_i\). Require:

- \(h_E^{-1}(C_0)_{\mathrm{red}}=Z\), including all inverse points;
- \(h_E(P_i)=C_0(t_i)\), with the \(t_i\in k^*\) pairwise distinct;
- \(h_E^*\mathcal O_Q(1,1)\simeq\mathcal O_E(2Z)\).

For application to the surviving order-two incidence, the ruling bundles
have degrees two and six, \(C'\) has class \((6,2)\), and the stronger
reviewed provisional identities are
\(L^2=\mathcal O_E(Z)\), \(M=L^3\). These are inputs from
[the survivor record](2026-10-30-projection-order-two-survivor.md) and
[its Picard-identity audit](2026-10-30-projection-elliptic-target-incidence-audit.md).
The construction below needs the displayed hyperplane identity, not a
passport enumeration.

Glue \(E\) to \(c=\mathbf P^1_t\) by \(P_i\sim t_i\). Denote this nodal
curve by \(Y\). Its arithmetic genus is four. The maps \(h_E\) and the
literal parametrization \(h_c:c\to C_0\) agree at the nodes and give
\(h:Y\to Q\). Set \(\mathcal H=h^*\mathcal O_Q(1,1)\).

The relevant intrinsic source polarization is the dualizing bundle:
\[
\omega_Y|_E=\omega_E(Z)\simeq\mathcal O_E(Z),\qquad
\omega_Y|_c=\omega_c(t_1+\cdots+t_4)\simeq\mathcal O_c(2).
\tag{1}
\]
Consequently \(\mathcal H\) and \(\omega_Y^2\) have isomorphic restrictions
on both components. They need not be isomorphic on their union.

## 2. Canonical reconstruction determines the source quadric

**Proposition.** The complete canonical series embeds \(Y\) in
\(\mathbf P^3\). Its image is the union of an elliptic normal quartic
\(E\) and a smooth plane conic \(c\), meeting transversely at the four
marked points. Exactly one quadric surface \(S_Y\) contains this union.
It is integral, but can be a cone. If it is smooth, then
\[
S_Y\simeq\mathbf P^1\times\mathbf P^1,\qquad
c\in|\mathcal O(1,1)|,\qquad E\in|\mathcal O(2,2)|.
\tag{2}
\]
In either case \(c\) is a Cartier hyperplane section, \(E\) is a Cartier
quadric section, and both avoid the vertex if \(S_Y\) is a cone.
The source ruling pencil(s) on \(E\) are therefore determined by the
marked abstract curve \(Y\), up to interchange in the smooth case;
they are not adjustable extra parameters for removing an obstruction.

**Proof.** \(h^0(Y,\omega_Y)=4\). The kernel of restriction to \(E\)
consists of sections of
\(\omega_Y|_c(-\sum t_i)=\omega_c\), hence is zero. Since
\(h^0(E,\omega_E(Z))=4\), restriction is an isomorphism. A degree-four
line bundle on an elliptic curve is very ample: Riemann--Roch shows that
every subscheme of length two imposes two independent conditions.
Thus \(E\) embeds as a linearly normal quartic.

The kernel of restriction to \(c\) is \(H^0(E,\omega_E)\), of dimension
one. Restriction to \(c\) is consequently the complete degree-two series,
giving a smooth conic in a plane \(\Pi\). The section defining this plane
restricts on \(E\) to the inclusion of a nonzero holomorphic differential
in \(\omega_E(Z)\); its zero divisor is precisely the reduced divisor
\(Z\). Hence \(E\cap\Pi=Z\), and each tangent to \(E\) at \(Z\) is
transverse to \(\Pi\). The two component embeddings therefore glue to a
closed embedding of the nodal union, with no other intersections.

Restriction of quadrics through \(E\) to \(\Pi\) is an isomorphism onto
the pencil of plane conics through \(Z\). Indeed, the restriction sequence
of ideals is
\[
0\longrightarrow\mathcal I_E(1)\longrightarrow\mathcal I_E(2)
\longrightarrow\mathcal I_{Z/\Pi}(2)\longrightarrow0.
\]
Here \(H^0(\mathcal I_E(1))=H^1(\mathcal I_E(1))=0\), by linear
normality. Also no three points of \(Z\) are collinear: restriction of
\(H^0(E,\mathcal O_E(Z))\) to any three has rank three, again by
Riemann--Roch. Thus \(h^0(\mathcal I_{Z/\Pi}(2))=2\).
The equation of the conic \(c\subset\Pi\) selects a unique quadric
\(S_Y\) through \(E\). A reducible or double-plane quadric cannot contain
the integral nonplanar \(E\); hence \(S_Y\) is integral.

If \(S_Y\) is smooth, its plane conic has class \((1,1)\). Write the
class of \(E\) as \((a,b)\). Degree four gives \(a+b=4\), and its genus
one gives \((a-1)(b-1)=1\); thus \((a,b)=(2,2)\). This proves (2).
The two ruling maps restrict isomorphically on the conic, so their target
coordinates can be chosen to equal its specified parameter \(t\).
Then \(c\) is the literal diagonal.

For either integral quadric \(S_Y\), choose another independent quadric
through \(E\). Their proper intersection is \(E\) scheme-theoretically:
it is a Cohen--Macaulay complete intersection of degree four containing
the integral degree-four curve \(E\). Thus \(E\) is a Cartier section of
\(\mathcal O_{S_Y}(2)\). If \(S_Y\) is a cone and its vertex belonged to
\(E\), the Jacobian of these two quadrics would have rank at most one
there, contradicting smoothness of \(E\). The plane of the smooth conic
also avoids the vertex, since a plane through the vertex cuts a singular
conic. This proves the remaining assertions. \(\square\)

This proof treats the reducible nodal curve directly; it does not apply
a smooth genus-four canonical-curve theorem without checking its
hypotheses.

## 3. The precise extension obstruction and a residue formula

Define
\[
\kappa(Y,h)=[\mathcal H\otimes\omega_Y^{-2}].
\tag{3}
\]
Since its component restrictions are trivial, this class belongs to
\[
\ker\bigl(\operatorname{Pic}(Y)\to
\operatorname{Pic}(E)\times\operatorname{Pic}(c)\bigr)
\simeq(k^*)^4/k^*\simeq(k^*)^3.
\tag{4}
\]
The four scalars are the identifications of component fibers at the
nodes. Rescaling the trivializations on the two connected components
changes all four by one common ratio. Formula (4) follows directly from
this gluing description (or the units exact sequence of the normalization).
It is an obstruction at the reduced nodal union, distinct from the later
full conductor descent obstruction on the projected surface.

The class has an intrinsic calculable representative. Put
\(R(t)=\prod_i(t-t_i)\). On \(c\), identify the coordinate section \(x_0\)
with the quadratic differential
\[
\tau_c=\frac{(dt)^2}{R(t)^2}.
\]
As a section of \(\omega_c^2(2\sum t_i)\), its divisor is \(4\infty\),
exactly the divisor of \(x_0|_{C_0}\). Choose any isomorphism
\(h_E^*\mathcal O_Q(1,1)\simeq\omega_E^2(2Z)\), and let \(\tau_E\)
be the quadratic differential corresponding to \(h_E^*x_0\). All its
quadratic residues \(r_i\) at \(P_i\) are nonzero: the image of each node
has finite nonzero parameter, so \(x_0\) is nonzero there. Here the
quadratic residue is the coefficient of \((du/u)^2\); it is independent
of the local parameter \(u\). Indeed, replacing \(u\) by
\(u'=a u+O(u^2)\), \(a\ne0\), changes \(du/u\) by a regular
differential, so it preserves the coefficient of the double-pole term.

At a node the dualizing generator restricts as \(du/u\) and
\(-dv/v\), so its square has matching leading coefficients. The other
three target sections have, at the nodes, the same ratios to \(x_0\)
on both components. Therefore
\[
\boxed{\kappa(Y,h)=1
\quad\Longleftrightarrow\quad
r_1R'(t_1)^2=\cdots=r_4R'(t_4)^2.}
\tag{5}
\]
Changing the isomorphism on \(E\) rescales all four entries equally.
Thus (5) is three actual gluing equations, not merely projective
agreement of the images of the nodes. The elementary local calculation
also makes clear why taking arbitrary square roots of torus coordinates
does not solve this problem: the required square root polarization is
the already determined \(\omega_Y\).

## 4. Unique global sections and the remaining first-normal condition

Assume now that \(\kappa(Y,h)=1\). Allow either normal source quadric,
smooth or a cone. Write \(S=S_Y\), \(D=E\subset S\), and
\(H=\mathcal O_S(2)\), where \(\mathcal O_S(1)\) denotes its hyperplane
bundle. In the smooth case these are \(H=\mathcal O(2,2)\) and
\(\mathcal O_S(1)=\mathcal O(1,1)\). The quadric is Gorenstein with
\(\omega_S=\mathcal O_S(-2)\), while \(Y=c+D\) is Cartier in
\(|\mathcal O_S(3)|\). Adjunction gives
\(\omega_Y=\mathcal O_S(1)|_Y\), and the restriction sequence is
\[
0\longrightarrow\mathcal O_S(-1)\longrightarrow H
\longrightarrow\omega_Y^2\longrightarrow0.
\]
Both \(H^0(\mathcal O_S(-1))\) and \(H^1(\mathcal O_S(-1))\) vanish.
This follows uniformly, including for the cone, from
\(0\to\mathcal O_{\mathbf P^3}(-3)\to
\mathcal O_{\mathbf P^3}(-1)\to\mathcal O_S(-1)\to0\) and
projective-space cohomology. Hence
\[
H^0(S,H)\xrightarrow{\sim}H^0(Y,\omega_Y^2).
\tag{6}
\]
The four target coordinate sections extend **uniquely** to sections
\(U_0,\ldots,U_3\) of \(H\), up to the common scalar in the chosen
isomorphism \(\mathcal H\simeq\omega_Y^2\). Normalize that scalar so
their restrictions to \(c\) are exactly
\((s^4,s^3t,st^3,t^4)\). On the smooth quadric this produces the full source form
\(U_i=B_i+\Delta A_i\), with \(A_i\in H^0(\mathcal O(1,1))\).

There is one further, essential condition. Since the target maps on both
components land in \(Q\),
\[
q(U)=\Delta\,d_D\,r,
\qquad r\in H^0(S,\mathcal O_S(1)).
\tag{7}
\]
Here \(\Delta\) cuts out the conic plane section and \(d_D\) is a
quadric section cutting out \(D\). The required order-two determinant is
equivalent to
\[
\boxed{r=\lambda\Delta\quad\text{for some }\lambda\ne0.}
\tag{8}
\]
Equivalently, \(r|_c=0\) and \(r\ne0\). Restriction to \(c\) is a
binary quadratic, so this is a concrete first-normal condition with
three linear coordinates on the four-dimensional space containing
\(r\). No claim is made that these coordinates vary independently in
the target incidence, or that (5) forces (8).

## 5. Sufficiency for an actual admissible carrier

If \(\kappa=1\) and (8) hold in addition to the input of Section 1, the unique \(U\)
defines a basepoint-free finite birational map
\(f:S\to X\subset\mathbf P^3\), with
\(f^{-1}(C_0)_{\mathrm{red}}=c\).

Indeed, a common zero of the \(U_i\) must lie in
\(V(q(U))=c\cup D\). On that union they restrict to the specified
morphism \(h\), so have no common zero. This also checks the cone vertex,
which lies outside \(c\cup D\). The resulting surface map is
finite, because its pullback of \(\mathcal O(1)\) is ample. It has an
integral surface image \(X\), and \(q(U)\ne0\) means \(X\ne Q\).

Let \(e\) be its generic degree. The projection formula for the target
quadric divisor gives the equality of cycles
\[
e[X\cap Q]=f_*(2c+D)=2[C_0]+[C'].
\]
The coefficient of the distinct curve \(C'\) is one, because
\(h_E\) is birational onto \(C'\). Hence \(e=1\). Finally every inverse
point of \(C_0\) lies in \(c\cup D\), and those on \(D\) are exactly
\(Z\subset c\). This proves full inverse support, including isolated
points. Also \(\deg X=H^2=8\).

Conversely, every admissible smooth-source order-two member with the
reviewed smooth primitive residual gives precisely these data and
passes (3) and (8). The same converse holds for a cone-source member
whose residual is smooth, Cartier, and primitive and meets the conic
transversely in four points. Thus no member of the stated smooth-source
survivor is lost, and the criterion also constructs the specified cone
members. It does not classify other cone residuals, order-one members,
the plane model, or arbitrary STCI equations.

Mate existence remains a separate problem on the actual surface \(X\).
The full-conductor criterion and phase reduction in
[R-0004](../results/projection_phase_reduction.md) apply only after this
construction succeeds. No equality of the reduced-curve gluing class
with the full conductor phase is asserted.

## 6. A concrete cone candidate, rather than another support partition

The [existing palindromic target](2026-10-30-projection-elliptic-target-palindromic.md)
has
\[
R(t)=t^4+\eta t^3+\eta t+1,\qquad \eta^2=-4/5,
\]
four contacts of order five, and the marking
\[
t_i=-\frac{\eta A(P_i)+1}{A(P_i)+\eta}.
\]
Its exact target equations and normalization are recorded there. The
individual computational construction still needs independent replay;
the reviewed interpolation argument excludes its **smooth-quadric**
source extension only. That conclusion is not a cone-source exclusion.
The normal quadric cone remains an allowed degree-eight model in
[R-0002](../results/cartier_singleton_lift.md) and
[Q-0001](../questions/cartier_projection_models.md).

There is a first **unevaluated component-polarization gate** for this
abstract target. Its boundary/Riemann--Hurwitz data give
\(M=L\otimes\mathcal O_E(Z)\). They do not by themselves give
\(L^2=\mathcal O_E(Z)\): the survivor proof obtained the latter using
the actual-source equality \(LM=\mathcal O_E(2Z)\). The palindromic
target note does not independently check this equality. Thus first test
\[
L^2\simeq\mathcal O_E(Z),\quad\text{equivalently here}\quad
h_E^*\mathcal O_Q(1,1)\simeq\mathcal O_E(2Z).
\tag{9}
\]
For example, (9) is equivalent to a nonzero section of the degree-four
bundle \(L^2\) vanishing at all four \(P_i\); if it exists, its divisor
must be exactly \(Z\). This is a four-point elliptic linear-series
calculation, not a new target enumeration.

**If (9) passes**, the canonical quadric \(S_Y\) is necessarily a cone.
A nondegenerate Mobius transform of \(A\) takes the four values
\(t_i\). If \(S_Y\) were smooth, each of its two
degree-two ruling functions \(u,v\) would take these same values on
\(Z\). The reviewed
[degree-two interpolation lemma](2026-10-30-projection-elliptic-target-incidence.md#2-a-degree-two-interpolation-lemma-retains-the-source-embedding)
forces \(u=v\) to be this transform of \(A\), contradicting the embedding
of \(E\) in the smooth quadric. The reconstructed quadric is integral,
so its only alternative is the rank-three cone. This uses the previous
negative evidence to identify the appropriate allowed source geometry;
it does not invalidate or reopen the previous theorem.

There is therefore one concrete construction experiment available:
independently replay this fixed target, check (9), calculate its four
residues in (5), and, if they match, recover its unique cone sections by
(6) and test (8). No new target family or passport enumeration is needed.
Stop this candidate if (9) fails, the residue class is nontrivial, or the
residual linear form fails (8). If all gates pass, the theorem produces an actual admissible
degree-eight cone carrier, and the next genuinely new question is its
full conductor/mate descent. These were unevaluated gates when this
criterion was proposed. The [subsequent test](2026-10-31-palindromic-polarization-spin.md)
finds that (9) fails. Accordingly the conditional cone inference is not
applicable to this target; its residue and determinant gates were not run.

## 7. Primary sources, scope checks, and limits

The closed-node pushout is covered by the Stacks Project,
[Pushouts in the category of schemes, II](https://stacks.math.columbia.edu/tag/0ECH):
the two maps from the finite reduced node scheme are closed immersions.
The restriction sequence and (6) use its
[effective Cartier divisor sequences](https://stacks.math.columbia.edu/tag/0C4S),
[projective-space cohomology](https://stacks.math.columbia.edu/tag/01XS).
The sheaves are invertible and \(Y\) is Cartier on either Gorenstein
quadric, so these hypotheses apply. In the smooth case the same
vanishing also follows from its
[Kunneth formula](https://stacks.math.columbia.edu/tag/0BEC) on the two
projective-line factors.

For the differential interpretation, Scott Wolpert's primary paper
[Infinitesimal deformations of nodal stable curves, Section 2](https://arxiv.org/pdf/1204.3680)
describes opposite residues for the dualizing sheaf and matching quadratic
residues for its square. Its setting is complex analytic. We use it to
check the interpretation, not to transfer an analytic deformation theorem
to arbitrary characteristic-zero fields: the local algebra
\(k[[u,v]]/(uv)\) and the generator \((du/u,-dv/v)\) prove the matching
rule used here algebraically. No smooth-curve theorem is being substituted
for a statement about the reducible \(Y\).

The new input is a reconstruction and sufficiency theorem: the source
quadric and its ruling pencils are intrinsic to a nodal genus-four curve;
the polarization obstruction has the residue formula (5); and after its
vanishing, section extension is automatic and unique. The sole remaining
determinant condition (8) then implies basepoint freedom, finiteness,
birationality and full inverse support without four separate searches.

For a *fixed* marked target incidence, neither the canonical quadric nor
\(\kappa\) can be tuned by choosing different source pencils. Across
different target incidences they can vary, but this note proves no
surjectivity, nonconstancy, or vanishing result for that variation.
The fixed cone candidate of Section 6 is the only proposed next
experiment here. Beyond that candidate, a positive construction would
need genuine control of the quadratic residues, for example constructing
the elliptic target sections directly as matching quadratic differentials
while retaining the rank-one map and full four-point contact support.
No family with such control is proved here. Failure of Section 6 would
not justify proceeding automatically through more supports or partitions.

One successful construction followed by full mate descent could settle
existence for the fixed \(C_0\). Failure on one target only identifies its
polarization or first-normal obstruction; it cannot settle unrestricted
nonexistence. The unrestricted characteristic-zero STCI question remains
open.

## 8. Independent review boundary

A fresh `gpt-6.1-sol/high` reviewer reconstructed Sections 1–7, checked the
critical primary-source applications, and found no material mathematical
defect. The linked audit covers the nodal canonical embedding, the cone,
component/gluing distinction, residue formula, unique extension, and the
full admissibility implication. It also independently supports the proposed
single fixed-target experiment and its stopping conditions.

That criterion review ran no candidate computation and established no
actual carrier or mate. The later fixed-target replay and failed Picard
gate have their own [result and review](2026-10-31-palindromic-polarization-spin.md);
residue matching and the determinant gate remain unperformed. No
literature-priority claim or canonical promotion is made.
