# Contact, spectral gluing, and asymmetry in the elliptic octic family

**Scope and review.** Work over an algebraically closed field of
characteristic zero, on the smooth, basepoint-free, birational octic
locus of the fixed [five-parameter elliptic construction](elliptic_double_inverse_construction.md#2-the-complete-five-parameter-lifting-family-and-its-symmetry).
The November 23, 2026 carrier/spectral reassessment derived the
comparisons below. A distinct reviewer independently reconstructed the
contact and Picard formulas, the conditional four degree rows, and the
branch-asymmetry argument. The full inverse-support and actual
homogeneous-source problems remain open on this locus.

## 1. Contact moves defect between the vertical and horizontal curves

Let \(f:S\to X\) be the normalization map from the smooth source
quadric to its octic image. Retain the marked elliptic curve \(E\),
the degree-two map \(\pi=f|_E:E\to C_0\simeq\mathbf P^1\),
and the length-twelve residual inverse scheme \(Z\). Put
\[
 A=\pi^*\mathcal O_{\mathbf P^1}(1),\qquad
 G=Z\cap E,\qquad g=\operatorname{length}G.
\]
Here \(G\) is an effective divisor on the smooth curve \(E\).
The construction proves the [actual inverse-ideal identity](elliptic_double_inverse_construction.md#an-intersection-bound-and-the-missing-descent-step)
\[
 \mathcal I_{C_0}\mathcal O_S=\mathcal I_E\mathcal I_Z,
 \qquad \mathcal O_E(E)=A^4.
\]
Dividing the two pulled-back normal generators by an equation of \(E\)
and restricting to \(E\) gives the conormal map
\[
 (A^{-7})^{\oplus2}\longrightarrow A^{-4}.
\]
Its entries are two sections of \(A^3\), whose common divisor is
exactly \(G\). Removing that divisor gives a basepoint-free direction
pencil \(\Theta:E\to\mathbf P^1\), with
\[
 B=\Theta^*\mathcal O(1)=A^3(-G),\qquad
 d=\deg B=6-g.                                          \tag{EC1}
\]

The [generic-node proof](elliptic_double_inverse_construction.md#the-generic-double-branch-has-conductor-coefficient-one)
shows that the directions of the two generic deck conjugates are
distinct. Thus \((\pi,\Theta)\) is the normalization of its horizontal
symbol image \(\Sigma\subset\mathbf P^1\times\mathbf P^1\),
an integral curve of type \((d,2)\). Both \(E\) and \(\Sigma\)
are finite flat double covers of the base line. Their trace-zero
summands are \(\mathcal O(-2)\) and \(\mathcal O(-d)\), respectively,
so the inclusion is multiplication by a nonzero binary form \(j\)
of degree \(d-2\). In a local trace frame it is
\[
 R\oplus jRw\ \subset\ R\oplus Rw,\qquad w^2\in R.
\]
An element and its product by \(w\) lie in the smaller algebra
exactly when both its coefficients are divisible by \(j\). The
relative conductor on \(E\) is therefore \(j\mathcal O_E\), and
the discriminant is multiplied by \(j^2\). Consequently
\[
 0\le g\le4,\qquad
 \delta(\Sigma)=p_a(\Sigma)-p_a(E)=d-2=4-g.              \tag{EC2}
\]
The binary divisor \(J=\operatorname{div}(j)\) is the same
direction-coincidence excess as in the [actual conductor identity](elliptic_double_inverse_construction.md#the-vertical-divisor-counts-the-residual-inverse-scheme).
Together with the vertical first-symbol divisor \(V\), that identity
gives
\[
 \deg V=12+g,\qquad \deg J=4-g,\qquad
 (B_{\rm cond}-E)|_E=\pi^*(V+J).                        \tag{EC3}
\]
Thus the restriction of the remaining ambient conductor always has
degree \(32\). Contact transfers degree between the vertical
inverse-support divisor and the horizontal trace conductor. These are
restrictions to \(E\), not a description of the full off-\(E\)
surface conductor.

Full inverse support is equivalent to nilpotence of the equation
\(e=Q_0\) on \(Z\). After trivializing its line bundle on this Artin
scheme, multiplication by \(e\) has cokernel of length \(g\).
On a full-support fiber it is a nilpotent endomorphism of a
twelve-dimensional vector space with exactly \(g\) Jordan blocks.
If its nilpotence index is \(n\), then \(12\le ng\). The inverse
ideal identity forces \(e^{b-1}|_Z=0\) for an actual degree-\(b\)
mate. Hence
\[
 1\le g\le4,\qquad
 b\ge1+\left\lceil\frac{12}{g}\right\rceil.             \tag{EC4}
\]
The separate [low-degree argument](elliptic_double_inverse_construction.md#descent-and-the-remaining-degrees)
excludes \(b\le5\) throughout the family. Neither bound proves the
existence of a full-support fiber or of a descending power.

## 2. The full root Picard class retains the conductor gluing

Let \(\pi_\Sigma:\Sigma\to\mathbf P^1\) be the root projection.
For a fiberwise coprime quotient second relation in degree \(s>2\),
[R-0008](../../results/spectral_root_picard_criterion.md) requires
\[
 \mathcal O_\Sigma(0,s)
   \simeq\pi_\Sigma^*\mathcal O(sd/2).                  \tag{EC5}
\]
In particular \(sd\) must be even. If \(d\) is even, the primitive
degree-zero class is
\(\xi=\mathcal O_\Sigma(0,1)\otimes\pi_\Sigma^*\mathcal O(-d/2)\),
and \(\xi^s\) must be trivial. If \(d\) is odd, \(s\) is even,
and the corresponding class is
\(\xi=\mathcal O_\Sigma(0,2)\otimes\pi_\Sigma^*\mathcal O(-d)\),
killed by \(s/2\). Pullback along \(E\to\Sigma\) and (EC1) give:

| \(g\) | Root type and total delta | Pullback of \(\xi\) to \(E\) |
| --- | --- | --- |
| 0 | \((6,2)\), \(\delta=4\) | \(BA^{-3}\simeq\mathcal O_E\) |
| 1 | \((5,2)\), \(\delta=3\) | \(B^2A^{-5}=A(-2G)\) |
| 2 | \((4,2)\), \(\delta=2\) | \(BA^{-2}=A(-G)\) |
| 3 | \((3,2)\), \(\delta=1\) | \(B^2A^{-3}=A^3(-2G)\) |
| 4 | smooth \((2,2)\) | \(BA^{-1}=A^2(-G)\) |

For \(g<4\), triviality or torsion of this pullback does not settle
(EC5). The line bundle must also have the required gluing on the
full conductor of \(E\to\Sigma\), including its nilpotent structure.
The actual failed member has \(g=0\): its normalized class is already
trivial, while its horizontal root has delta four and its residual
inverse scheme lies off \(E\). It supplies a concrete control against
using ordinary elliptic torsion as a support or full-root criterion.

For \(g=4\), \(j\) is a unit and \(\Sigma\simeq E\) is a smooth
\((2,2)\) curve. In that case \(G\) cannot be the pullback of a
degree-two divisor on the base: this would give \(B\simeq A\),
whose complete degree-two pencils agree up to an automorphism, contrary
to the \((2,2)\) embedding. No unconditional mate hypothesis here
places the horizontal root in the saturated graded setting of R-0008.

## 3. Four necessary rows when the actual first kernel is saturated

Suppose an actual degree-\(b\) mate exists, and put
\(Y=V(F_8,G_b)\), \(\mathcal J=\mathcal I_{C_0}\mathcal O_Y\).
Assume additionally that the **actual kernel**
\[
 R=\ker\bigl(\operatorname{Sym}^2N^*_{C_0/\mathbf P^3}
                     \longrightarrow\mathcal J^2/\mathcal J^3\bigr)
                                                               \tag{EC6}
\]
is a line subbundle, equal to the primitive horizontal relation.
Merely taking the saturation of a possibly nonsaturated kernel does
not satisfy this hypothesis.

The full generic ordinary initial algebra has CI degrees \((2,b)\).
Indeed the transverse carrier is a node after the separable residue
extension. In formal coordinates it has equation \(uv=0\). The
mate pulls back with divisor \(bE\), so it has order \(b\) on
each split branch. Modulo \(uv\) its first term is therefore
\(\alpha u^b+\beta v^b\), with \(\alpha\beta\ne0\).
This coprime initial CI has length \(2b\), already the full generic
intersection length. Thus it is the full initial algebra.

This reduction uses local formal multiples of the carrier equation.
It does not replace \(G_b\) by a global homogeneous form of normal
order \(b\). Its lower-order symbols can be proportional to those
of \(F_8\), and the actual homogeneous source must still supply
the required global corrections.

[R-0010](../../results/saturated_first_relation_normal_flatness.md)
now supplies ordinary normal flatness and a coprime quotient second
relation in every fiber. With
\(N^*_{C_0/\mathbf P^3}=\mathcal O(-7)^{\oplus2}\), (EC5) gives
\[
 R=\mathcal O(-14-d),\qquad
 T=\mathcal O(-7b+bd/2).
\]
The [graded CI socle formula](../spectral/moving_power_and_spectral_roots.md#5-exact-c0-numerical-boundary-for-these-abstract-families)
then gives
\[
 \operatorname{Soc}=R\otimes T\otimes\det(N_C^*)^{-1}
                   =\mathcal O(-d-7b+bd/2).
\]
For the actual \((8,b)\) complete intersection the socle line on
\(C_0\) is \(\mathcal O(14-4(8+b))=\mathcal O(-18-4b)\).
Equating degrees and substituting \(d=6-g\) yields
\[
 \boxed{\quad g(b-2)=24.\quad}                          \tag{EC7}
\]
Together with (EC2), this leaves exactly the following necessary rows:

| \(g\) | Mate degree \(b\) | Necessary normalized Picard condition |
| --- | --- | --- |
| 1 | 26 | \(A(-2G)\) killed by \(13\) |
| 2 | 14 | \(A(-G)\) killed by \(14\) |
| 3 | 10 | \(A^3(-2G)\) killed by \(5\) |
| 4 | 8 | \(A^2(-G)\) killed by \(8\) |

The full-root conductor gluing remains necessary in the first three
rows. These are additional tests of the saturated sector, not an
exhaustive list of all mates in this family. Failure of (EC6) remains
a separate possibility. Passing a row still does not establish full
inverse support, higher ambient compatibility, or membership of
\(Q_0^b\) in the actual homogeneous coordinate subalgebra.

The [actual equation-source extension](elliptic_conjugate_sources.md#3-saturated-first-symbols-force-a-nontrivial-source-extension)
has coefficient degrees \(12+g\) and \(4b-20+g\). The first
local cancellation has pole divisor exactly \(V\), explaining why
it is not a permitted homogeneous row operation. The same account
distinguishes vanishing of the equation-comparison defect from the
positive full normal-layer degree defect. Neither supplies a new
exclusion of the four rows.

## 4. The fixed marking prevents target sign symmetry

The sign involution on the target is
\(\tau[z:x:y:w]=[z:-x:-y:w]\); on \(C_0\) it sends \(t\) to
\(-t\). In the fixed elliptic marking
\[
 E:y^2=x^3-x,\qquad t=(y+1-i)/(x-i),
\]
substitution and removal of the extraneous factor \(x-i\) give
\[
 -x^2+(t^2-i)x-it^2-2(1-i)t+2=0.
\]
Its discriminant is
\[
 D(t)=t^4-6it^2-8(1-i)t+7.                              \tag{EC8}
\]
The smooth genus-one double cover has four branch points. Its
degree-four discriminant has square leading coefficient and no branch
at infinity, so it is squarefree. Since
\(D(-t)-D(t)=16(1-i)t\ne0\), this monic branch polynomial is not
even and its branch divisor is not preserved by \(t\mapsto-t\).

If an octic image \(X\) in this locus were \(\tau\)-preserved,
\(\tau\) would lift to its normalization \(S\). It would preserve
\(E\), the unique inverse curve over \(C_0\) by the ruling-degree
argument. Isolated inverse points do not affect that uniqueness.
The resulting automorphism of \(E\) would lift \(t\mapsto-t\),
forcing its branch divisor to be preserved, a contradiction. Thus no
birational octic in this fixed family is target-sign invariant,
without requiring full inverse support.

More strongly, the [two conjugate quadratic residue fields](elliptic_conjugate_sources.md#1-the-octic-and-its-sign-transform-have-generic-contact-four)
have disjoint branch divisors. The actual pair \((F_8,\tau F_8)\)
therefore has generic normal CI type \((2,2)\), multiplicity four
on \(C_0\), and residual degree \(48\). This provides a concrete
conjugate-source comparison while retaining its residual attachments.

This explains why the [one-sign-eigen-generator consequence](../torus/sign_symmetry_and_actual_sources.md)
does not directly exclude this constructive family. Its support
nilpotence problem, root-conductor gluing, and actual-source descent
remain distinct questions.
