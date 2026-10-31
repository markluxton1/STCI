# The full tropical thickening must move

Date: 2026-10-31. Status: **independently reviewed provisional deductions**;
see the [bounded audit](2026-10-31-tropical-descent-audit.md).
No canonical result is promoted. The result applies to every
hypothetical homogeneous defining pair for the fixed characteristic-zero
quartic. It supplies a necessary geometric condition and a presentation
barrier, not an unrestricted STCI exclusion.

## 1. Objects and claim

Let k be algebraically closed and

\[
C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3,
\qquad Z=V(F_a,G_b),\qquad Z_{\rm red}=C.
\]

The pair is proper. Put m=ab/4. Use the actual morphism from the
[reviewed tropical model](2026-10-31-tropical-model-characteristic.md),

\[
Y=\mathbf P^1\times\mathbf G_m^2\xrightarrow{\phi}\mathbf P^3,
\quad [1:t:ut^3:vt^4],
\quad[\tau^4/v:\tau^3/v:(u/v)\tau:1].
\]

Write U=u−1, V=v−1 and let W be the **scheme-theoretic closure in Y of
Z restricted to the dense torus**. Thus the entire pulled-back ideal is
saturated at t=0 and at τ=0. W is not the intersection of two individually
divided pullback equations. Let π:W→P1 be the product projection.

This projection uses the parameter t of the reduced curve and has rank m.
It is distinct from the earlier plane-pencil map [x0:x3], whose coordinate
ratio pulls back to vt^4 on W and whose degree on Z is ab.

The proposed uniform conclusions are:

1. W is finite flat of degree m over P1, with reduction P1×{(1,1)}.
   Its algebra B=π_*O_W is globally generated. The induced map ρ:W→Z
   is finite and injects O_Z into ρ_*O_W, with cokernel supported at the
   two endpoints.
2. If e=deg B and δ0,δ∞ are the two cokernel lengths, then
   \[
   \delta_0+\delta_\infty=e+m(2a+2b−7).                 \tag{1}
   \]
3. In characteristic zero, **e>0**. Equivalently the full embedded
   transverse scheme traces a nonconstant curve in the punctual Hilbert
   scheme. This is not a claim that its abstract generic Artin algebra
   varies, or a claim only about its first normal direction.
4. In characteristic zero, W cannot be the scheme-theoretic intersection
   of any two global effective Cartier divisors on Y. This quantifies over
   all such presentations of W, not just the two original pullbacks.

The reduced curve P1×{(1,1)} remains the scheme CI (U,V). Losing a global
two-divisor presentation for its full thickening is compatible with that
fact and does not contradict the assumed presentation of Z downstairs.

## 2. Constructing the finite modification

On the torus, Z is a Cohen–Macaulay curve with sole support U=V=0.
Its generic transverse algebra has length m, so (U,V)^m vanishes at its
generic point. Purity makes it vanish on the entire torus restriction:
a generically zero subsheaf of this pure curve is zero.

Consequently W lies in the fixed finite scheme

\[
\mathbf P^1\times\operatorname{Spec} k[U,V]/(U,V)^m.
\]

Here 1+U and 1+V are already units. Closure is therefore finite over P1.
On the interior its algebra is torsion free over the parameter curve by
Cohen–Macaulayness. At an endpoint scheme-theoretic closure is contraction
from the punctured chart; it removes parameter torsion. Thus B is torsion
free, hence locally free on P1, of rank m. Moreover

\[
\mathcal O_{\mathbf P^1}\otimes_k k[U,V]/(U,V)^m\twoheadrightarrow B
                                                               \tag{2}
\]

proves global generation and e≥0. This also shows H1(W,O_W)=0.

The equations of Z vanish on W by its definition as closure, so φ factors
through ρ:W→Z. W is proper over k and ρ has one-point topological fibers;
hence ρ is finite. It is an isomorphism over the torus. Its sheaf kernel
is supported at the endpoints and is a subsheaf of the pure sheaf O_Z,
so it is zero. Therefore

\[
0\longrightarrow O_Z\longrightarrow\rho_*O_W
 \longrightarrow Q_0\oplus Q_\infty\longrightarrow0.           \tag{3}
\]

Riemann–Roch on P1 and the ordinary CI genus formula give

\[
\chi(O_W)=m+e,\qquad
\chi(O_Z)=−ab(a+b−4)/2,
\]

which prove (1). This is a finite modification of a nonreduced curve,
not its normalization. The two numbers δ measure the functions gained
by undoing the endpoint contractions, not residual components.

The Hilbert-scheme interpretation is literal: (2) gives a map from P1
to the scheme of length-m quotients of the fixed Artin algebra
k[U,V]/(U,V)^m. It is a closed subscheme of the corresponding Grassmannian,
and B is the pullback of its universal quotient bundle. Thus e is its
Plücker degree. The Hilbert functor used here is the finite-flat functor
in [Stacks, Section 44.2](https://stacks.math.columbia.edu/tag/0B94).

## 3. Why the entire embedded family must move

If e=0, a globally generated vector bundle of degree zero on P1 is
trivial. Under B≅O^m its unit, multiplication and the coordinate sections
U,V are constant, since all their matrix entries are global functions
on P1. Therefore the kernel of (2) is constant and

\[
W=\mathbf P^1\times\operatorname{Spec} A
\]

as an embedded family, for one fixed length-m quotient A. Conversely a
constant embedded family has e=0.

Such W is invariant under scaling t while fixing u,v. Equivariance of φ
makes its scheme-theoretic image Z invariant under the original torus
weights (0,1,3,4). The image really is Z by the injection in (3).

Let J=(F,G)⊂k[x0,x1,x2,x3]. A proper homogeneous codimension-two CI ideal
is saturated, so torus invariance of Z implies invariance of J. The
two-dimensional graded minimal-generator space J/R_+J is a representation
of Gm. Choose a basis of weight eigenvectors and lift each to a polynomial
of the same ordinary degree and torus weight by taking its weight
component. Graded Nakayama shows that the two resulting weight-homogeneous
polynomials generate J. They have no common factor because J has height
two.

In characteristic zero this contradicts
[Hellus–Hübl, Theorem 1.2](https://arxiv.org/pdf/1312.7661):
the lowest-weight components of any
hypothetical defining pair have a nonunit common divisor in I_C. For
weight-homogeneous generators those components are the generators
themselves. Hence e>0.

The external obstruction to a weight-homogeneous defining pair is reused,
not claimed as new. The additional deduction identifies its consequence
for the full finite transverse family of **every** defining pair.

The characteristic qualification has an actual geometric control. For the
inherited characteristic-seven pair
\[
F=x_1^4-x_0^3x_3,\qquad G=x_2^7-x_0x_1x_3^5,
\]
the torus equations are t^4(1-v) and t^21(u^7-v^5). Its full closure
in Y is therefore (v-1,u^7-1). In characteristic seven this is the
constant length-seven family
\(\mathbf P^1\times\operatorname{Spec}k[U]/(U^7)\), with e=0.
In characteristic zero the same closure has seven distinct constant
sections; their projective images are seven distinct quartics, so the
sole-support hypothesis fails. This is the construction reviewed in the
[characteristic comparison](2026-10-31-tropical-model-characteristic.md),
interpreted on Y rather than offered as a new equation family.

## 4. A barrier to every two-divisor presentation upstairs

The following elementary statement works in every characteristic.

**Lemma.** Suppose W⊂P1×Gm² is finite flat of positive degree m over P1,
supported on P1×{(1,1)}. If W is the scheme-theoretic intersection of two
global effective Cartier divisors on this ambient, its embedded family
is constant.

**Proof.** The Picard group of P1×Gm² is Z, generated by the pullback of
O_P1(1). One can see this from the two affine factorial charts: their
overlap units are c t^r u^i v^j, and the chart units remove u^i v^j.
Write the two divisor line bundles as O(d1), O(d2). A nonzero global
section requires di≥0, because its Laurent coefficients in u,v are
sections of O_P1(di).

The two sections have codimension-two zero scheme, hence form a regular
sequence locally. Since ω_Y=π^*O(−2), adjunction gives

\[
\omega_W=\pi^*O(d1+d2−2).
\]

Finite-flat duality and projection formula then give, respectively,

\[
\pi_*\omega_W=B^\vee\otimes O(−2)
             =B\otimes O(d1+d2−2).
\]

Taking determinant degrees yields

\[
2\deg B=−m(d1+d2).
\]

Global generation gives deg B≥0, while di≥0. Thus d1=d2=deg B=0,
and the preceding constant-family argument applies. ∎

The duality input is the usual finite-flat dual module
Hom_O(B,O), as in
[Stacks, quasi-finite Gorenstein morphisms](https://stacks.math.columbia.edu/tag/0C14);
the displayed adjunction is also obtained directly from the Koszul
resolution for the two sections.

Applied to Section 3, the lemma proves conclusion 4. It does not assert
that W fails to be locally a complete intersection, and it does not
exclude equations given as a section of a nonsplit rank-two bundle.
It says that full boundary saturation necessarily leaves the class of
global intersections of two Cartier divisors for any characteristic-zero
STCI downstairs. Replacing the two displayed tropical equations by
another such presentation cannot avoid this particular loss of structure.

## 5. Endpoint lattices and a uniform, deliberately coarse bound

The full algebra also gives concrete local bounds. Complete at p0 and
write R=k[[t]]. The image of the completed local ring of Z in B0 is
exactly

\[
A_0=R[t^3U,t^4V]\subset B_0.                              \tag{4}
\]

Choose standard monomials U^iV^j for the length-m special fiber B0/tB0.
Their exponent set E0 is an order ideal of cardinality m; these monomials
lift to an R-basis of B0. The subalgebra A0 contains each
t^(3i+4j)U^iV^j. Consequently

\[
\delta_0\le\sum_{(i,j)\in E_0}(3i+4j)\le2m(m−1).          \tag{5}
\]

For the last inequality, order the m monomials by total degree. The
monomial in position r, starting with r=0, has degree at most r, since
its divisor chain is in the order ideal. Sum 3i+4j≤4(i+j).

At infinity use the actual local parameter z=x2/x3=τu/v and the torus
coordinates

\[
U'=v^2/u^3−1,\qquad V'=v^3/u^4−1.
\]

Their exponent determinant is −1. The projective coordinates satisfy
x1/x3=z^3(1+U') and x0/x3=z^4(1+V'). Since z is τ times a unit, it is a
nonzerodivisor in B∞ and gives the same special fiber. B∞ is free of
rank m over k[[z]], generated as an algebra by U',V'. Hence

\[
A_\infty=k[[z]][z^3U',z^4V'],\qquad
\delta_\infty\le\sum_{(i,j)\in E_\infty}(3i+4j)
                \le2m(m−1).                              \tag{6}
\]

The local bound is attained by B=R[V]/(V^m), U=0, for which the subalgebra
is R[t^4V] and the index is 4Σ_(j=0)^(m−1)j=2m(m−1). This is a local
control, not an actual projective pair or simultaneous endpoint example.
Higher multiplication and parameter-dependent relations can lower the
index; (5)–(6) are not asserted to be equalities for arbitrary W.

Combining them with (1), in characteristic zero,

\[
0<e\le m(4m−2a−2b+3).                                    \tag{7}
\]

This coarse bound does not contradict the surviving degree range. It is
not presented as stronger than the existing
[full conormal/socle budget R-0032](../results/full_conormal_socle_budget.md).
Its purpose is to connect the movement degree to the actual endpoint
subalgebras and expose exactly where a sharper inequality would be needed.

## 6. Scope, novelty check and missing bridge

The geometric object added here is the entire finite family W, its
positive Plücker degree, and its two finite endpoint contractions. The
normal exponents (3,4) alone did not supply that family. Its construction
uses every relation in the pulled-back ideal and preserves the full
generic transverse length.

The proposed mechanism was checked against the original proof of
[R-0032](2026-10-13-evening-entirely-thick-rees-progress.md), the
[normal-torsion genus account](2026-10-26-normal-torsion-spectral-genus-budget.md),
the [formal-neighborhood equivalence](2026-10-27-formal-neighborhood-residual-visibility.md),
and the [full torus-limit analysis](2026-10-30-four-streams-degeneration.md).
Those establish related genus, socle, extension and saturation facts;
they do not state this punctual-family construction or its strict movement
and global-two-divisor consequence. A focused search of notes, results
and synthesis files for punctual Hilbert schemes and tautological algebras
found no prior version. This is a repository novelty check, not a claim
of literature priority.

[Tevelev](https://arxiv.org/pdf/math/0412329) and
[Luxton–Qu](https://arxiv.org/pdf/0902.2009) were checked for what tropical
compactification guarantees. Their schön/regular-embedding statements
do not preserve global equations for this nonreduced finite family under
the nonproper contraction. The proof above does not infer such preservation.

The remaining existence question is whether a moving full punctual family
can have these two contracted endpoint lattices and be the image of an
actual homogeneous CI. Equation (7) leaves room. Neither positive movement
nor the loss of two global divisors upstairs rules that possibility out.
The previous full fixed-twist formal-pair criterion already resolves
algebraization once its hypotheses hold; no additional algebraization gap
is introduced here.

No computer algebra calculation, inherited certificate rerun, or metadata
promotion was performed. The independent audit reconstructs the main
proofs, characteristic-zero use of Hellus–Hübl, endpoint algebra
identifications, all-presentations lemma, and characteristic-seven control.
No material correction was required. The inherited formal-pair theorem
and novelty observations above are not new inputs proved by that audit.
