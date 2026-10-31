# Marked embeddings through absorption deformations

Date: 2026-10-31. **Independently reviewed provisional deductions; not
canonically promoted.** See the [separate audit](2026-10-31-marked-absorption-deformations-audit.md).
Work over the complex numbers in the ribbon
application, followed by explicit spreading to algebraically closed
characteristic-zero fields. The marked embedding lemma itself works over
an algebraically closed field, with the finite-presentation hypotheses below.

This corrects an overly broad stopping inference in the literature selection:
an abstract deformation theorem need not prescribe the projective embedding
for that embedding to extend. A separate vanishing argument can supply the
extension, including a fixed embedded component. At sufficiently high fixed
degrees, actual proper pairs can then be carried along this family. The
result is partial absorption with a prescribed embedded ribbon, not STCI.

## 1. Sources, inherited interfaces, and exact question

Retrieval began with [INDEX](../INDEX.md) and [MAP](../MAP.md), followed by
the [October 27 absorption synthesis](2026-10-27-arbitrary-degree-absorption-synthesis.md)
and [October 28 liaison construction](2026-10-28-residual-liaison-construction.md).
The existing [equation-lifting interface](2026-10-27-absorption-formal-lifting-interface.md),
especially §§3–4, remains necessary when chosen homogeneous equations are
also to move. Extending an embedding is a different problem.

The primary deformation inputs checked are:

- [Stacks, 08U8](https://stacks.math.columbia.edu/tag/08U8): obstruction and
  difference groups for morphisms through square-zero thickenings.
- [Stacks, 0D1C](https://stacks.math.columbia.edu/tag/0D1C): relative morphisms
  from a proper flat finitely presented source to a separated finitely
  presented target form an algebraic space locally of finite presentation.
- [Stacks, 0APN](https://stacks.math.columbia.edu/tag/0APN),
  [055U](https://stacks.math.columbia.edu/tag/055U), and
  [05XA](https://stacks.math.columbia.edu/tag/05XA): the pointwise infinitesimal
  smoothness criterion, étale local sections, and openness of the locus
  where a proper relative morphism is a closed immersion.

Drézet, [*Reducible deformations and smoothing of primitive multiple
curves*, full text](https://arxiv.org/html/1409.4175v3), Proposition 3.2.6
and Theorem 3.2.7(ii), gives a global maximal reducible deformation of a
given complex ribbon when its conormal is \(O_C(-\Delta)\) for a reduced
effective divisor. Definition 2.3.1 makes each total-space component a flat
family with scheme-theoretic special fiber the reduced \(C\). The two
general components meet in \(-\deg L\) transverse points. These are the
source conclusions used here. The landing-page abstract's broader global
“if and only if” formulation is not needed; the full-text theorem suffices
on \(C=\mathbf P^1\). Its higher-multiplicity discussion is not used as an
existence theorem.

## 2. A marked embedding lemma, with algebraization

Let \(k\) be algebraically closed, \(S\) a locally Noetherian \(k\)-scheme,
and \(s\in S(k)\). Let \(\mathcal X\to S\) be proper, flat and of finite
presentation. Suppose there is a closed immersion

\[
\mathcal C=C\times S\hookrightarrow\mathcal X
\]

with \(C\) a proper finitely presented \(k\)-scheme. Write

\[
W=\mathcal X_s,\qquad J=\mathcal I_{C/W}.
\]

Fix closed immersions \(j:C\hookrightarrow\mathbf P^3_k\) and

\[
i:W\hookrightarrow\mathbf P^3_k,\qquad i|_C=j.
\]

**Marked embedding lemma.** If

\[
H^1\bigl(W,i^*T_{\mathbf P^3}\otimes J\bigr)=0,                 \tag{1}
\]

then, after an étale neighborhood \(S'\to S\) of \(s\), the embedding \(i\)
extends to a closed immersion

\[
\mathcal X_{S'}\hookrightarrow\mathbf P^3\times S'
\]

whose restriction to \(C\times S'\) is exactly \(j\times\mathrm{id}\).
No smoothness, local complete-intersection condition, or reducedness of
\(W\) is required.

**Proof of the lifting assertion.** The ideal
\(\mathcal J=\mathcal I_{\mathcal C/\mathcal X}\) is flat over \(S\): both
the middle and quotient terms in
\(0\to\mathcal J\to O_{\mathcal X}\to O_{\mathcal C}\to0\) are flat.
For a small extension of local Artinian \(k\)-algebras \(A'\to A\), with
kernel \(K\) annihilated by the maximal ideal, consider an \(S\)-map
\(\operatorname{Spec}A'\to S\) centered at \(s\). Suppose a marked map
\(f_A:\mathcal X_A\to\mathbf P^3_A\), reducing to \(i\), is given.

Inside \(\mathcal X_{A'}\), the closed union

\[
D=\mathcal X_A\cup\mathcal C_{A'}
\]

has square-zero ideal \(K\otimes_k J\). Indeed its ideal is
\((K O_{\mathcal X_{A'}})\cap\mathcal J_{A'}=K\mathcal J_{A'}\);
flatness of \(O_{\mathcal C_{A'}}\) and \(\mathcal J_{A'}\) gives this
intersection and identifies it with \(K\otimes_k J\). The two maps
\(f_A\) and \(j\times\mathrm{id}_{A'}\) agree on \(\mathcal C_A\), so
they glue to a map from \(D\).

Smoothness of \(\mathbf P^3_{A'}\to\operatorname{Spec}A'\) supplies local
lifts from \(D\) to \(\mathcal X_{A'}\). On overlaps, their differences
form a Čech cocycle in

\[
i^*T_{\mathbf P^3}\otimes J\otimes_k K.
\]

Its cohomology class vanishes by (1), so the lifts can be corrected and
glued. This proves lifting for every small Artin extension, not merely
for first-order tangent vectors.

**From lifts to an algebraic family.** Form the fiber over the fixed map
\(j_S\) of the restriction morphism

\[
\operatorname{Mor}_S(\mathcal X,\mathbf P^3_S)
\longrightarrow\operatorname{Mor}_S(C\times S,\mathbf P^3_S).
\]

Both relative morphism functors are algebraic spaces locally of finite
presentation by 0D1C. Their fiber, the space of marked maps, has the same
property over \(S\). The local Artin lifting criterion over a locally
Noetherian base (0APN) shows it is smooth at \([i]\). For residue-field
extensions the identical argument uses flat base change of (1).
Take an étale scheme chart through this point and a local section of its
smooth map to \(S\), after
an étale neighborhood of \(s\). The section can pass through the specified
\(k\)-point: in smooth local coordinates, take the constant coordinate
section through that point and pull back along the étale coordinate map.
This gives an actual algebraic relative morphism extending \(i\).
By 05XA, its closed-immersion locus is open and contains \(s\). Shrinking
the neighborhood proves the assertion. This step uses representability
and smoothness, rather than asserting convergence of a formal series.

The same proof works with any fixed smooth separated finite-type target
in place of \(\mathbf P^3\). The hypothesis is a sufficient vanishing
criterion; nonvanishing is not an obstruction class.

## 3. Embedded ribbon absorption with the quartic fixed

Now fix

\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_{\mathbf C}.
\]

The syzygies of the four displayed sections of \(O_{\mathbf P^1}(4)\) are
the columns

\[
(t,-s,0,0),\quad(0,t^2,-s^2,0),\quad(0,0,t,-s).
\]

They have degrees \(1,2,1\), are independent at every point, and generate
the kernel of \(O^4\to O(4)\). Pulling back and dualizing the Euler
sequence therefore gives

\[
T_{\mathbf P^3}|_C\simeq O_{\mathbf P^1}(5)^{\oplus2}
                         \oplus O_{\mathbf P^1}(6).             \tag{2}
\]

Let \(W\subset\mathbf P^3\) be **any given embedded ribbon** with
reduction exactly this \(C\), and conormal ideal

\[
J=\mathcal I_{C/W}\simeq O_{\mathbf P^1}(-d),\qquad 0\le d\le6.
\]

Since \(J^2=0\), the obstruction sheaf in (1) is the pushforward from
\(C\) of \(T_{\mathbf P^3}|_C\otimes O(-d)\). Formula (2) yields

\[
h^1(W,T_{\mathbf P^3}|_W\otimes J)
 =2\max(d-6,0)+\max(d-7,0)=0.                                  \tag{3}
\]

For \(1\le d\le6\), choose a reduced divisor of degree \(d\) on
\(\mathbf P^1\), and apply Drézet's global theorem to the abstract ribbon
\(W\). Write its two total-space components as
\(\mathcal X_1,\mathcal X_2\subset\mathcal X\). Each is closed and flat
over the smooth parameter curve, and has special fiber \(C\) as a scheme.
Thus the restriction of \(\mathcal X_1\hookrightarrow\mathcal X\) to the
special fiber is the reduced inclusion \(C\hookrightarrow W\), not a
thickened mark.

After an étale neighborhood of the base point,
\(\mathcal X_1\simeq\mathbf P^1\times S\), with its central
identification prescribed. One direct justification uses the relative
isomorphism functor: \(H^1(\mathbf P^1,T_{\mathbf P^1})=0\) lifts an
isomorphism through every small extension; representability, the open
isomorphism locus, and a section through the identity then give the
trivialization. We consequently have exactly the flat closed distinguished
family required in §2. Applying (3) extends the existing embedding \(W\)
while keeping the first component equal to the fixed embedded \(C\).

For \(d=0\), the ribbon on \(\mathbf P^1\) is split, since its extension
class lies in \(H^1(\mathbf P^1,T_{\mathbf P^1})=0\). Use the explicit
abstract flat family

\[
\mathbf P^1\times
\operatorname{Spec}\mathbf C[z,t]/(z(z-t))\longrightarrow\mathbf A^1_t,
\]

marked by \(z=0\), and apply the same lemma. This avoids interpreting an
empty divisor in the cited existence theorem.

**Conclusion.** Every such given embedded ribbon is the special fiber of
an algebraic flat embedded family whose noncentral fibers are

\[
C\cup C_t,
\]

where \(C_t\subset\mathbf P^3\) is a smooth rational quartic distinct
from \(C\), and the two curves meet transversally in \(d\) distinct points
and are disjoint when \(d=0\). The degree of \(C_t\) is four because the
restriction of the extended \(O(1)\) to the flat second component has
degree four on its special fiber. A closed immersion preserves the
scheme-theoretic intersections and the transverse nodal geometry supplied
by the abstract family. The total degree is eight; its arithmetic genus
is \(d-1\), agreeing with \(0\to O(-d)\to O_W\to O_C\to0\).

This is a geometric realization theorem for an entire specified class of
embedded ribbons. It fixes \(C\) pointwise in the ambient projective space
and transfers the other quartic into its nilpotent structure. It does not
choose two equations or claim that the union or ribbon is a complete
intersection. In particular, degree eight cannot be the sole-support
intersection of two forms of degrees at least five. The construction
removes the blanket embedding objection. The following corollary supplies
proper pairs containing this family, while allowing residual curves.

### 3.1. Actual pairs retaining the prescribed ribbon

After shrinking the smooth pointed base \(S\), choose sufficiently large
fixed integers \(a,b\). Relative Serre vanishing and generation make
\(\mathcal I_{\mathcal X}(a)\) and \(\mathcal I_{\mathcal X}(b)\) generated
by relative global sections, with their direct images locally free and
commuting with base change. Thus chosen sections on \(W\) lift to
actual homogeneous forms over a neighborhood of the base point.
This is the same large-twist section-lifting operation already used in
the October 27 construction; no numerical threshold is asserted here.

Choose \(F_0\in H^0(I_W(a))\), \(G_0\in H^0(I_W(b))\) generally enough
that they have no common surface component and generate \(I_W\) at the
generic point of \(C\). Both conditions are nonempty open conditions.
For the latter, the ribbon is a codimension-two local complete
intersection, and generation gives two independent conormal classes at
the generic point. For the former, the generated ideal has no surface
base component, so a second general section avoids the finitely many
surface factors of a chosen first section.

Lift \(F_0,G_0\) to forms \(F,G\) over \(S\) vanishing on \(\mathcal X\).
The central ribbon is lci. The openness and fiberwise criterion for lci
morphisms, followed by properness and a base shrink, make
\(\mathcal X\hookrightarrow\mathbf P^3_S\) a regular immersion of
codimension two. This standard criterion is recorded in
[Stacks, §37.62](https://stacks.math.columbia.edu/tag/068E).
The determinant of the two equation classes in the rank-two conormal
bundle \(\mathcal I_{\mathcal X}/\mathcal I_{\mathcal X}^2\) is nonzero
on a nonempty open of the central reduced \(C\).

Restrict this determinant to each of the smooth component families
\(\mathcal X_i\to S\). Its nonvanishing locus meets the central fiber;
its image in \(S\) is open. Shrinking once more ensures that on each
nearby component fiber the determinant is not identically zero.
Consequently \(F_s,G_s\) generate the ideal of \(\mathcal X_s\) at the
generic points of both reduced components for \(s\ne0\), and generate
the ideal of \(W\) generically at \(s=0\).

Properness of the pair persists after a base shrink by upper
semicontinuity of fiber dimension for the projective family \(V(F,G)\).
The fiberwise regular sequences then give a flat family of actual
complete intersections \(Y_s=V(F_s,G_s)\). Its cycles are

\[
[Y_0]=2[C]+R_0,\qquad [Y_s]=[C]+[C_s]+R_s\quad(s\ne0),
\qquad\deg R_0=\deg R_s=ab-8.                                  \tag{4}
\]

Neither \(R_0\) nor \(R_s\) contains \(C\); \(R_s\) does not contain
\(C_s\). In fact the full \(C\)-primary component of \(Y_0\) is precisely
the prescribed embedded \(W\): the two ideals agree at the generic
point of \(C\), and the pure ribbon ideal is the contraction of that
primary localization. Generic agreement therefore identifies the
entire primary component, including its behavior at closed points.

The degree of the genuine residual after removing the full \(C\)-primary
component is \(ab-4\) off the special fiber and \(ab-8\) at the special
fiber. Exactly four units of residual degree have become ribbon
thickness. There is no claim that full-primary extraction is flat.
The once-linked family by the fixed reduced \(C\) is flat by the
existing [relative liaison result, §2.1](2026-10-28-residual-liaison-construction.md).
The integer \(d\) describes only \(C\cap C_s\), not attachment to the
entire residual, which also contains \(R_s\). No residual smoothness or
optimal degree bound is asserted.

### 3.2. Characteristic-zero field scope

The cited existence theorem is stated over \(\mathbf C\). To obtain the
same conclusion for a given embedded ribbon over an arbitrary
algebraically closed characteristic-zero field \(k\), descend its finite
equations, embedding, and ribbon data to a finitely generated subfield
\(k_0\subset k\). This field admits an embedding in \(\mathbf C\); the
whole field \(k\) need not do so. Apply the complex construction after
this base change.

The resulting smooth pointed parameter curve, its two component
families, closed embeddings, central identifications, and, when used,
the forms \(F,G\), involve finitely many coefficients. Spread them to a
finitely generated \(k_0\)-subalgebra of \(\mathbf C\), using
[finite-presentation descent, Stacks 01ZM](https://stacks.math.columbia.edu/tag/01ZM).
Shrinking its
spectrum preserves the specified identifications and the flatness,
properness, smoothness, closed-immersion, and transverse-intersection
conditions; descent of the displayed properties is supplied by
[Stacks §32.8](https://stacks.math.columbia.edu/tag/081C), including
[properness, 081F](https://stacks.math.columbia.edu/tag/081F).
The noncentral locus remains nonempty after shrinking. A
closed point of this nonempty parameter open has residue field finite
over \(k_0\), which embeds in \(k\) over \(k_0\). Specializing there and
base-changing to \(k\) gives the desired family with the original ribbon
as its marked special fiber. This is an existence transfer by spreading,
not an identification of an arbitrary characteristic-zero field with
a subfield of \(\mathbf C\).

## 4. The sufficient vanishing fails at every supported-CI endpoint

Suppose, conditionally, that \(Z=V(F_a,G_b)\subset\mathbf P^3\) is a
proper complete intersection with \(Z_{\mathrm{red}}=C\), \(a,b\ge5\).
Set

\[
c=a+b-4,\quad E=T_{\mathbf P^3}|_Z,\quad
J=\mathcal I_{C/Z},\quad R=\mathbf C[x_0,x_1,x_2,x_3]/(F_a,G_b),
\]

and write \(H_R(n)=\dim R_n=h^0(O_Z(n))\) for \(n\ge0\). The equality
follows from the Koszul resolution. Adjunction gives
\(\omega_Z=O_Z(c)\).

The restricted Euler sequence is

\[
0\longrightarrow O_Z\longrightarrow O_Z(1)^{\oplus4}
 \longrightarrow E\longrightarrow0.                            \tag{5}
\]

By Serre duality, the dual of the map
\(H^1(O_Z)\to H^1(O_Z(1))^{\oplus4}\) is multiplication by the coordinates,

\[
R_{c-1}^{\oplus4}\longrightarrow R_c.
\]

It is surjective because \(R\) is standard graded and \(c\ge1\). Since
\(h^0(O_Z)=1\) and \(h^0(O_Z(1))=4\), (5) consequently gives

\[
h^0(E)=15,\qquad h^1(E)=4H_R(c-1)-H_R(c).                       \tag{6}
\]

All these fifteen sections are restrictions of ambient projective vector
fields. Their restriction to \(C\) is injective: if a matrix-induced
projective vector field vanishes pointwise on \(C\), every vector over
\(C\) is an eigenvector of that matrix. Irreducibility puts \(C\) in one
eigenspace, and nondegeneracy forces that eigenspace to be the whole
four-dimensional vector space. The matrix is scalar and its projective
vector field is zero.

By (2), \(h^0(T_{\mathbf P^3}|_C)=19\) and
\(h^1(T_{\mathbf P^3}|_C)=0\). The exact sequence

\[
0\to E\otimes J\to E\to T_{\mathbf P^3}|_C\to0
\]

therefore gives

\[
\boxed{h^1(E\otimes J)=4+4H_R(c-1)-H_R(c)
       =19+ab\left(\frac{3c}{2}-4\right)>0.}                   \tag{7}
\]

For the second equality, the complete-intersection Hilbert polynomial is
\(\chi(O_Z(n))=abn-ab c/2\). Thus (5) gives
\(\chi(E)=ab(4-3c/2)\), and (6) gives the stated expression. Positivity
holds in particular because \(c\ge6\).

Formula (7) concerns the **space that can contain marked map-lifting
obstructions**. It does not exhibit a nonzero obstruction for any particular
deformation and does not prove that the marked Hom space is singular.
It shows that the sufficient criterion (1) never automatically extends
the ribbon construction to a hypothetical complete-intersection endpoint.
No iteration to higher thickness or unrestricted exclusion follows.

For comparison, the identical argument for a nondegenerate smooth rational
curve of degree \(e\) inside such a complete intersection replaces the
constant 19 in (7) by \(4e+3\): the Euler sequence on
\(\mathbf P^1\) gives \(h^0(T_{\mathbf P^3}|_C)=4e+3\) and \(h^1=0\).
This extension needs no classification of multiple structures.

## 5. Review boundary and geometric gain

The proof supplies a general marked embedding method and actual proper
pairs realizing quartic-into-ribbon absorption with any prescribed
embedded ribbon in the stated conormal range. Actual partial absorption
already existed in the October 27 work; the gain here is control of this
given embedded ribbon and its normal direction. High twists let two
forms contain the whole family and be generically exact on it. They do
not make those two forms generate its ideal everywhere or eliminate
the residual of degree \(ab-8\).

The independent audit reconstructs the ideal of the closed union in the
Artin lifting step; algebraization through the marked relative Hom space;
the scheme-theoretic distinguished component; the \(d=6\) cohomology
threshold; the actual-pair and primary-component corollary; and the
distinction between (7) and an actual obstruction. It also checks the
field transfer and the strategy assessment's ambient Hilbert-scheme
nef-class calculation. No material finding remains unresolved within
those reviewed scopes.
No numerical campaign, new local-model classification, or canonical
promotion accompanies this proposal.

## 6. Supported semiregularity also has zero target for smooth projective curves

This continuation tests an actual proposed way to control the obstruction
classes left open in §4. The recommendation and bounded test were reported
before verification. The conclusion is a uniform limitation of a specified
detector, not an obstruction to STCI and not a new classification.

**Claim.** Let \(C\subset X=\mathbf P^n_k\), \(n\ge2\), be a smooth
projective curve over an algebraically closed field. It need not be
rational or nondegenerate. Then

\[
\boxed{H_C^n(X,\Omega_X^{n-2})=0,\qquad
\mathbb H_C^{2n-2}(X,\Omega_X^{<n-1})=0.}                     \tag{8}
\]

The truncated de Rham complex in (8) has terms \(\Omega_X^p\) in degrees
\(0\le p\le n-2\). The vanishing itself is valid in every
characteristic. Its application to the cited semiregularity theorem
uses that theorem's characteristic-zero hypotheses.

**Proof.** Put \(I=I_C\) and \(C_m=V(I^m)\). For a locally free E,
the supported-cohomology formula and coherent Serre duality give

\[
H_C^q(X,E)=\varinjlim_m\operatorname{Ext}_X^q(O_{C_m},E),
\qquad
\operatorname{Ext}_X^q(O_{C_m},E)
\simeq H^{n-q}(C_m,E^\vee\otimes\omega_X|_{C_m})^\vee.
\tag{9}
\]

These are **global** Ext groups. The first equality is the coherent
supported-cohomology formula on the noetherian scheme X, obtained from
quasi-coherent resolutions for the I-power-torsion functor and global
sections. This is not an assertion about arbitrary O-module sheaves.
The second equality uses coherent Serre
duality and a locally free twist, not local freeness of \(O_{C_m}\).
See [supported cohomology](https://stacks.math.columbia.edu/tag/0A39)
and [coherent Serre duality](https://stacks.math.columbia.edu/tag/0FVZ).
In particular the groups in (9) vanish for \(q>n\).

For \(E=\Omega_X^{n-2}\), exterior-power duality identifies
\(E^\vee\otimes\omega_X\) with \(\Omega_X^2\). The possible top
Ext group is therefore dual to \(H^0(C_m,\Omega_X^2|_{C_m})\).
The regular embedding C supplies the filtration

\[
I^r/I^{r+1}=\operatorname{Sym}^r N_{C/X}^\vee.
\]

Conormal and Euler sequences give locally split bundle injections

\[
N_{C/X}^\vee\hookrightarrow\Omega_X^1|_C
\hookrightarrow O_C(-1)^{\oplus(n+1)}.
\]

Taking symmetric and exterior powers, and tensoring, consequently yields

\[
\Omega_X^2|_C\otimes\operatorname{Sym}^rN_{C/X}^\vee
\hookrightarrow O_C(-r-2)^{\oplus M_r}
\tag{10}
\]

for some finite \(M_r\). Local splitting justifies these injections in
all characteristics. Each line bundle on the right has negative degree
on every component of C. Hence every graded layer has no global sections.
The finite filtration of \(O_{C_m}\) gives

\[
H^0(C_m,\Omega_X^2|_{C_m})=0
\quad\text{for every }m.
\]

Equation (9) now proves the first vanishing in (8). For the second, use
the supported hypercohomology spectral sequence

\[
E_1^{p,q}=H_C^q(X,\Omega_X^p)
\Longrightarrow\mathbb H_C^{p+q}(X,\Omega_X^{<n-1}).
\]

On the diagonal \(p+q=2n-2\), every term has \(q>n\), except
\(p=n-2,q=n\). All vanish by the preceding argument. The spectral
sequence is taken for sheaves of k-vector spaces: the de Rham differential
is k-linear and need not be O-linear. At \(n=2\) the truncated complex
is just O, and the same proof applies.

**The detector actually considered.** For a codimension-\(p\) lci
subscheme realized as the regular zero locus of a section of a rank-p
vector bundle on a Zariski open neighborhood, [Iacono–Manetti, Theorem 11.1 and its proof, pp. 27–28](https://arxiv.org/pdf/1112.0425)
annihilate embedded Hilbert obstructions already in
\(\mathbb H_Z^{2p}(X,\Omega_X^{<p})\), before mapping to ordinary
ambient cohomology. For a thickening Z of C, \(p=n-1\), and support
cohomology depends only on the closed topological support. Thus both
that target and its untruncated precursor
\(H_Z^{p+1}(X,\Omega_X^{p-1})\) are precisely the zero groups in (8).
In P3 this includes \(\mathbb H_C^4(P^3,[O\to\Omega^1])\).

The initial literature selection correctly noted the stronger supported
map but left its target unresolved. Formula (8) closes that particular
remaining possibility. It does not claim that every relative or marked
obstruction complex has a zero target. Ordinary ambient trace targets
in [Pridham's extension, Corollary 2.22 and Remarks 2.27–2.29](https://webhomes.maths.ed.ac.uk/~jpridham/semireg2.pdf)
also vanish on P3: \(H^{q+2}(P^3,\Omega^q)=0\) for the relevant q.

**Geometric content and strategy.** Every finite normal neighborhood of
any smooth projective curve has no sections of the restricted ambient
two-form bundle: the candidate sections in each normal order inject into
negative line bundles. Duality therefore removes this supported
semiregularity detector independently of thickness, genus and equation
degrees. The calculation cannot distinguish a successful supported pair
from an unsuccessful one. In particular it supplies neither cancellation
nor nonvanishing of the actual marked map-lifting classes in §4.

Stop this semiregularity application, including this specific supported
refinement. A different marked comparison would need a different target
or additional pair data; its existence is not established here. The
prescribed-ribbon construction in §3 and the open unrestricted STCI
status are unchanged. This is an application of standard duality and
normal-filtration methods, with no claim of publication novelty. The
[audit continuation](2026-10-31-marked-absorption-deformations-audit.md)
records independent reconstruction of this generalization.
