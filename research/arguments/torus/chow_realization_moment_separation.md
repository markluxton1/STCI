# Chow realization and first-moment separation

**Status:** proposed argument, pending independent review. Characteristic zero
unless otherwise stated. This develops the existing
[first-moment theorem](chow_arrangement_moments.md), not a new unrestricted
STCI exclusion. The classical cubic-carrier theorem of Craighero–Gattazzo
([1989](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf)) and
[R-0022](../../results/quartic_44_filtered_exclusion.md) are independent
benchmarks; neither is used in the moment proof for (3,4) or the
multiple-support proof for (4,4).

## 1. Primary cycle space, not a moduli space of thickenings

Put \(C_{u,v}=[s^4:s^3t:ust^3:vt^4]\), \(T=(\mathbf G_m)^2\),
\(q=u/v\), and \(H\) the intrinsic torus of weights \((0,1,3,4)\).
For \(ab=4m\) use the unordered space \(A_m=\operatorname{Sym}^m T\).
No component is distinguished, and no ambient automorphism quotient is
taken. [R-0074](../../results/chow_polytope_rigidity.md) identifies its
geometric points, via \(\mu_m(\sigma)=[\prod_i R_{z_i}^{n_i}]\), with
the full Chow-polytope fiber \(P_Z=mP_C\). Here \(R_z\) denotes the
degree-four Chow form, viewed as a section of \(\mathcal O(4)\) on
\(\operatorname{Gr}(2,4)\). This is a cycle statement, not a scheme-level
isomorphism assertion for an unspecified Chow locus.

For proper pairs in \(\mathbf P(S_a)\times\mathbf P(S_b)\), let
\(\rho_{a,b}(F,G)\) be their binary resultant on the universal line,
a Chow form of degree \(ab\). Define the actual realization locus
\(R_{a,b}\) as the geometric-point image in \(A_m\) of the fiber product
of the proper-pair space and \(A_m\) over the Chow-form projective space.
Its constructibility follows from Chevalley's theorem. Do not replace
the proper-pair image by an image of arbitrary pairs with common factors.
The small diagonal is \(D_m=\{m[z]:z\in T\}\), with Chow image
\([R_z^m]\). All multiplicity partitions are present from the outset.

The projective product locus is the image of \(\operatorname{Sym}^m S\)
under multiplication, where \(S\) is the single-orbit Chow closure.
This map is finite: a fixed effective cycle admits finitely many
decompositions into degree-four effective cycles. It is generically
one-to-one by unique decomposition into integral curves; in characteristic
zero it is birational. Consequently the normalization of the product
locus is \(\operatorname{Sym}^m\widetilde S\), where \(\widetilde S\) is
the normalized toric Chow surface
[computed here](chow_quotient_fan_and_blowup_comparison.md).
Normality follows from the normal product and finite symmetric quotient.
Boundary decompositions may be nonunique, so no global isomorphism is
claimed for the unnormalized spaces.

The Hilbert lift is secondary: for \(\sigma=\sum n_i[z_i]\), a pure
embedded scheme with that cycle restricts to a finite flat degree-\(m\)
family over the orbit coordinate \(r\in\mathbf G_m\) in
\(\mathbf G_m\times T\). Purity gives torsion-freeness, and the family lies
in a fixed fat-point neighborhood of its support. Its map to
\(\operatorname{Hilb}^m(T)\) has constant Hilbert–Chow value \(\sigma\),
hence extends uniquely over \(\mathbf P^1\) by projectivity of the
Hilbert–Chow fiber. Conversely such a map determines a pure embedded
scheme by scheme-theoretic closure of the dense-torus family (contraction
introduces no associated points supported on the complement).
This is a correspondence on geometric points, not a family-level
equivalence. The sole-support version and its stronger bundle and
conductor constraints are already in
[full tropical thickenings](tropical_thickenings_and_endpoint_duality.md)
and [R-0072](../../results/torus_quotient_movement_bounds.md).
A constant map corresponds to an invariant ideal. There is no need to
force forgetful maps or a compactification of these Hilbert lifts to
study the primary cycle separation.

## 2. The universal separator and its exact target

The regular function
\[
M_1(\sigma)=\sum_i n_i q(z_i)
\]
defines a closed locus in every \(A_m\). On \(D_m\) it takes the value
\(m q(z)\ne0\) in characteristic zero; this same affine disjointness
holds when the characteristic does not divide \(m\). The existing
linear Chow coefficient \(A_{yz}\) satisfies
\(A_{yz}/A_0=-4M_1\) on the arrangement locus, with \(A_0\ne0\)
([proof](chow_arrangement_moments.md#A-regular-function-on-the-Chow-space)).
Thus when \(4m\) is invertible, a covered realization locus and its
projective closure miss the *interior* deepest collision locus.
The projective closures of the two loci can meet on the toric boundary:
the diagonal scaling \(\operatorname{diag}(1,t,t,1)\) sends every
translated quartic cycle to \(4[L_{03}]\) as \(t\to0\).

A smaller faithful cycle coordinate model in characteristic zero is the
hyperplane section \(x_3=x_0\) followed by normalization \(x_0=1\).
Set \(p=1/v=q/u\). Its normalized zero-cycle Chow form for one translate is
\[
f_{p,q}(y,z)=1-4qyz+2q^2y^2z^2-py^4-(q^4/p)z^4.
\]
Indeed it is the product of \(1+yt+zut^3\) over \(t^4=p\).
The arrangement is the product of these forms with multiplicities.
Its factors as a zero-cycle recover \(p=x_1^4\) and \(q=x_1x_2\);
the power locus consists of \(f_{p,q}^m\).
The coefficient of \(yz\) is \(-4M_1\).
The classical multisymmetric coordinates on \(A_m\) (Vaccarino,
*The ring of multisymmetric functions*, Ann. Inst. Fourier 55 (2005))
are another description of the same invariant functions. The
unrestricted missing theorem is \(R_{a,b}\subset V(M_1)\) for every
\(ab=4m\), not a further proof of disjointness of \(V(M_1)\) and \(D_m\).

## 3. Cycle-preserving regular initial sequences

**Lemma.** Suppose a Chow-matched proper pair of degrees \(a\le b\)
has a degree-\(a\) generator \(F\) with an irreducible extreme weight
component \(F_0\) (either orientation). Then its cycle admits an
invariant proper CI realization of the same degree type, hence
\(M_1=0\) in characteristic zero.

Choose the weight orientation making \(F_0\) initial. For \(a<b\),
repeatedly subtract from \(G\) a homogeneous multiple of \(F\) whenever
its current initial form is divisible by \(F_0\). The initial weight
strictly increases; the process terminates and cannot give zero
because the pair is proper. For \(a=b\) this is just adapting the
second pencil member by scalar subtraction. The resulting \(G_0\)
is not divisible by \(F_0\), so the two initial equations are coprime.
The normalized orbit equations over the degeneration parameter
are a regular sequence modulo the parameter. The parameter is
regular in their quotient, giving the flat CI degeneration with
special fiber \(V(F_0,G_0)\). This is the usual regular-initial-sequence
criterion and the end-adaptation of
[canonical extreme sources](chow_matched_equation_layers.md).
The intrinsic torus fixes the entire Chow cycle, and flat
specialization preserves its Chow point. The invariant CI at the
special fiber therefore realizes exactly the same cycle. Apply the
existing eigenform moment theorem.

More generally any proper invariant initial CI is sufficient.
The general question is whether a fiber of the proper-CI-to-Chow
map contains such a realization. The fiber need not be proper:
initial equations may have common surface factors and the full
flat limit may have extra generators or embedded points. No
general fixed-point theorem on these open fibers is available.

## 4. The cubic–quartic case

For \(ab=12\), write \(B(h)\subset A_3\) for configurations all of whose
support points have the same value of the indicated character \(h\).
The four cubic containment families are \(B(u),B(q),B(uq),B(uq^2)\).
Indeed the seven possible multimonial cubic weight spaces have
weights \(3,4,5,6,7,8,9\); their coefficient-kernel conditions are
respectively \(u,q,q,uq,q,q,uq^2\) constant on the support.
This decomposes the entire containing cubic space, without assuming
the actual cubic is an eigenform. Each \(B(h)\simeq
\mathbf G_m\times\operatorname{Sym}^3\mathbf G_m\) has dimension four
and contains \(D_3\).

If a proper pair has multiple distinct supports, no two can have
the same \(q\). In that case both lie on the same smooth quadric with
ruling class \((1,3)\); a cubic through them contains that quadric,
and the quartic does too by the same restriction calculation.
For distinct \(q\)'s only the weight-3, 6 and 9 cubic components can
be present. Weights 3 and 6, or 6 and 9, cannot coexist. Weight 6 alone
contains \(V(x_0,x_3)\), which the arrangement misses, and every
positive-degree mate meets that line. Therefore some extreme component
is one of the irreducible binomials of weight 3 or 9. The lemma gives
an invariant realization of the cycle, so also handles mixed
weight-3/9 cubics without the transverse Jacobian case split.

For the small diagonal, translate the support to \(C_{1,1}\) for
the proof only. A length-three local Gorenstein algebra of embedding
dimension at most two is curvilinear (the alternative \((1,2)\)
Hilbert function has a two-dimensional socle). Every local parameter
slice of the sole-support CI is finite free of rank three and lci.
Thus the triple is primitive everywhere. By the classical primitive
filtration and adjunction its type line is \(L=\mathcal O(-7)\):
\(\omega_C\otimes L^{-2}=\mathcal O(12)\).
The balanced conormal \(E=\mathcal O(-7)^2\) then forces a constant
kernel in a split frame. This uses only the first layer, not the
known second-order triple-extension obstruction.

Use the split frame from
[formal normal geometry](../normal-geometry/formal-normal-intersection.md#primitive-triples-on-smooth-rational-quartics):
on \(x_0=1\), \(r=x_1\), \(V=x_2-r^3\), \(U=x_3-r^4-3rV/2\).
With \(Q=x_0x_3-x_1x_2\), the cubic basis in increasing weight is
\(x_0^2x_2-x_1^3,\ x_0Q,\ x_1Q,\ x_0x_2^2-x_1^2x_3,\
x_2Q,\ x_3Q,\ x_2^3-x_1x_3^2\).
Writing coefficients \(c_3,\ldots,c_9\), the first jet is \(PU+SV\) with
\[
P=c_4+c_5r-c_6r^2+c_7r^3+c_8r^4-2c_9r^5,\quad
S=c_3+\tfrac12(c_4r+c_5r^2+c_6r^3+c_7r^4+c_8r^5).
\]
For a finite kernel direction \(U+\theta V\), \(S=\theta P\).
If \(c_9=0\), descending coefficient comparison gives
\(c_8=c_7=c_6=c_5=c_4=c_3=0\), impossible. Thus the highest
weight component is the irreducible weight-nine binomial.
For kernel \(V\), \(P=0\) forces the nonzero cubic to be the
weight-three binomial. In either case the lemma gives \(M_1=0\),
contradicting \(M_1(3[z])=3q(z)\). This is a first-jet plus
cycle-preserving degeneration proof of diagonal separation.

In particular the full cycle realization locus is
\[
R_{3,4}=(B(u)\cup B(uq^2))\cap V(M_1).
\]
To verify sufficiency and the exact invariant image, for \(u=\lambda\)
take \(F=x_0^2x_2-\lambda x_1^3\) and
\(G=x_2^4+B x_1x_2x_3^2+D x_0x_3^3\).
The quotient equation is \(\lambda q^3+Bq+D=0\).
Every multiset of three nonzero roots with sum zero occurs:
choose the corresponding monic depressed cubic, then \(D\ne0\).
On \(x_0=0\) the cubic forces \(x_1=0\), the quartic forces
\(x_2=0\); on \(x_3=0\) the quartic forces \(x_2=0\), the
cubic forces \(x_1=0\). The middle coordinate hyperplanes give
only these endpoints as well. Thus there is no boundary curve,
and root multiplicities give the exact cycle. Conversely
invariant generators must have weights \((3,12)\) or \((9,4)\)
by the two excluded middle vertices. Coordinate reversal
sends \(u\) to \(v^2/u^3=1/(uq^2)\) and preserves \(q\),
giving the second family. These two families are disjoint since
on their intersection all \(q_i\) are in \(\{r,-r\}\) and the
sum of three entries cannot vanish. Each is isomorphic as a
reduced parameter variety to \(\mathbf G_m\times\mathbf A^1
\times\mathbf G_m\) via carrier and depressed-cubic coefficients.
The double-root locus is the discriminant of the depressed cubic;
the triple-root cusp is outside the nonzero-constant-term open.
The projected containment conditions alone never exclude \(D_3\).

## 5. Quartic pencils with at least two distinct supports

For \(m=4\) the following proves
\[
R_{4,4}\setminus D_4\subset V(M_1)
\]
without assuming invariance or smoothability through reduced arrangements.

Again, distinct support points must have distinct \(q\): two
translates on one smooth quadric force both quartics to contain it,
since \((4,4)-2(1,3)=(2,-2)\) is not effective.

Suppose \(u\) is not constant on the support. Every containing quartic
has zero components below weight 4: weights 0,1,2 each have one
monomial, and the weight-3 system is \(x_0(x_1^3,x_0^2x_2)\),
whose kernel requires constant \(u\). Choose an actual pencil member
nonzero at the \(x_1\) vertex. Its weight-4 component is
\(A x_1^4+B x_0^2x_1x_2+C x_0^3x_3\) with \(A\ne0\).
If \(C=0\), vanishing on the support forces constant \(u\), impossible.
The component is irreducible: viewed as linear in \(x_3\) its
coefficient \(Cx_0^3\) is coprime to its constant term (as \(A\ne0\)).
It is initial. Section 3 supplies an invariant realization of the
same cycle. By reversal the same conclusion holds if \(uq^2\)
is not constant.

The sole remaining multiple-support locus is \(B(u)\cap B(uq^2)\)
(now defined on \(A_4\)). There are exactly two support points,
\((u,q)=(\lambda,r),(\lambda,-r)\). The balanced distribution
\((2,2)\) satisfies \(M_1=0\) automatically; we do not claim
it admits an invariant lift or even a proper realization at
these specified support points.

For the unbalanced distribution \((3,1)\), link the reduced union
\(X=C_+\cup C_-\) in the actual CI of type (4,4).
The two local intersection lengths are both four: on \(x_0=1\)
the coefficients of \(x_2\) agree and those of \(x_3\) differ,
giving the ideal \((r^4)\) on either branch; in the opposite
chart \(\alpha=v^2/u^3\) agrees and \(\beta=v^3/u^4\) differs,
giving the same length. Thus \(p_a(X)=4+4-1=7\).
The reduced union is locally Cohen–Macaulay and eligible for
ordinary CI linkage. The residual is locally Cohen–Macaulay
by liaison duality, has degree eight, and has cycle \(2[C_+]\).
The standard liaison genus formula
\(p_a(X')-p_a(X)=(a+b-4)(\deg X'-\deg X)/2\) forces genus seven.
But Ferrand doubling classifies every pure CM double on the smooth
quartic by a surjective conormal quotient
\(\mathcal O(-7)^2\twoheadrightarrow L\) (see the
[existing linkage account](../linkage/supported_linkage_operations.md)).
Its genus is \(-1-\deg L\le6\), contradiction.
Thus the unbalanced collision cannot occur.

This proves the desired moment vanishing for every multiple-support
quartic–quartic realization and separates their full Chow closure
from the interior power locus. Away from the exceptional opposite
two-support locus the proof actually gives an invariant lift of
the same cycle. No assertion of invariant lifts throughout that
exceptional locus is made. The invariant locus itself is classified in
[the quartic root-polynomial description](../equations/chow_polytope_rigidity.md#quartics-including-invariant-collision-lifts).

## 6. Boundaries and next decision

The pairs (1,4), (2,2), (2,4) have empty realization locus by
nonplanarity, the unique quadric, and the common-quadric ruling-class
argument respectively. For (3,4) the above moment proof is
unrestricted. For (4,4) it covers every cycle except the small diagonal;
[R-0022](../../results/quartic_44_filtered_exclusion.md) independently
excludes that diagonal, so the full moment inclusion follows using
the existing exclusion. A new direct moment proof on the fourth-power
locus remains missing. In higher degrees the moment separator is
already available; the problem is coverage by invariant degeneration,
linkage or other cycle-level mechanisms. Do not infer that the
existence of a cycle-preserving flat Hilbert limit guarantees a proper
CI at the limit. The desired generalization is an unrestricted moment
identity, not an enumeration of normal algebra types or a new numerical
bound. No independent review or unrestricted all-degree theorem is
claimed by this draft.


## 7. Beyond coprime initials: basic double linkage and ACM full limits

**Proposed statements, pending independent review.** Use the full graded
initial ideal \(J\), before irrelevant saturation, for one weight end.
The result is characteristic-free as a decomposition of cycles; moment
vanishing here is in characteristic zero. The classical inputs are
Hilbert–Burch (e.g. Hartshorne, *Deformation Theory*, Theorem 8.1)
and basic double linkage (Migliore–Nagel,
[*Numerical Macaulification*, Lemma 3.1](https://academicweb.nd.edu/~jmiglior/MN11-NumMac.pdf)).
The latter applies in the form \(DI+(K)\) for \(K\in I\) and
\(\gcd(D,K)=1\); the colon exact sequence below verifies the required
cycle identity directly. Neither classical input asserts that arbitrary
non-ACM full CI limits have such a decomposition.

### 7.1 One effective cancellation

For an end-adapted pair, let \(F_0=DA,\ G_0=DB\), \(\deg D=e>0\),
\(\gcd(A,B)=1\). Adaptation ensures \(e<a\).
The [common-factor rank calculation](equation_pair_rank_and_weights.md#common-factor-rank-drop-in-arbitrary-degrees)
gives one extra class in degree \(d=a+b-e\) and none below it.
Choose a weight-homogeneous representative \(K\in J_d\) of that class.
If \(\gcd(D,K)=1\), let \(J'=(DA,DB,K)\subset J\).
The colon by \(D\) is \((A,B,K)\); indeed
\(Dh\in D(A,B)+(K)\) implies the coefficient of \(K\) is divisible by
\(D\). Thus
\[
0\to S/(A,B,K)(-e)\xrightarrow{\cdot D}S/J'
\to S/(D,K)\to0.
\]
The ideal \(J'\) has height two and
\[
ab\le\deg S/J'\le (a-e)(b-e)+ed=ab.
\]
Here the degrees refer to the projective curve cycles, with a
lower-dimensional residual term contributing zero. The second
inequality is degree exhaustion in the CI \((A,B)\).
Consequently \(K\in(A,B)\), since the latter ideal is unmixed and
the quotient by \(K\) has lost no generic length. Equality of degree
and containment give the cycle identity
\[
[V(J)]=[V(A,B)]+[V(D,K)].
\]
Both summands are invariant proper CIs. As the entire cycle of the
flat limit is the original Chow-matched cycle, both summands
separately have only translated-quartic support. Their moments vanish
by the existing theorem; additivity proves \(M_1=0\) for the original
pair. This includes the three-generator full initial ideal case:
if there are exactly three minimal generators, \(K\) is the third,
and height two forces \(\gcd(D,K)=1\). The two-generator case is
already Section 3. For (4,4) no nontrivial such splitting exists,
by the plane/quadric arrangement exclusions.

### 7.2 Arbitrarily many cancellations: the ACM limit theorem

**Theorem candidate.** If either full graded intrinsic torus limit
of a Chow-matched proper pair of degrees \(a\le b\) is ACM, then
its cycle has an effective decomposition into invariant proper
complete-intersection cycles, and \(M_1=0\).

The full graded quotient retains Hilbert series
\((1-t^a)(1-t^b)/(1-t)^4\).
In the coprime-initial case the result is Section 3.
Otherwise the ideal has minimal initial generators of degrees \(a,b\),
and the first extra generator occurs in degree \(c_1=a+b-e>b\)
by the rank calculation. List all extra generator degrees
\(c_1\le\cdots\le c_r\). Since \(S/J\) is ACM of height two, a
minimal homogeneous Hilbert–Burch resolution and comparison of its
Hilbert numerator show that the syzygy shifts are precisely
\(c_1,\ldots,c_r,a+b\), as multisets. The original \(a,b\) shift terms
cancel from this comparison even when \(a=b\).

Choose the resolution equivariant for both ordinary and intrinsic
torus gradings (choose homogeneous bases of the minimal generator
space and then the syzygy space). Its matrix has row degrees
\(a,b,c_1,\ldots,c_r\), and column degrees \(c_1,\ldots,c_r,a+b\).
An entry can be nonzero only if its column degree is strictly larger
than its row degree: equal-degree scalar entries vanish by ordinary
graded minimality. The maximal minors are all nonzero because they
are the minimal generators. This forces \(c_r<a+b\): otherwise the
last row is zero and a minor deleting a first row vanishes.
It also forces strict inequalities between the \(c_j\).
Indeed, in the minor deleting the first row, the last \(r\) rows
must match distinct columns of strictly greater degree. If
\(c_i=c_{i+1}\), the rows with indices \(i,\ldots,r\) have at most
\(r-i\) eligible columns, impossible. Put \(c_{r+1}=a+b\).

The resulting matrix has two unrestricted top rows and an
upper-triangular bottom \(r\times r\) block after its first column.
The last row contains only its final entry \(D_r\), which is nonzero
and has degree \(c_{r+1}-c_r\). Delete last row and last column;
write \(J_{r-1}\) for the maximal-minor ideal of the smaller matrix.
Laplace expansion gives
\[
J=D_rJ_{r-1}+(K_r),\qquad K_r\in J_{r-1},
\]
where \(K_r\) is the minor deleting the last row of the original
matrix. No irreducible factor can divide every generator of
\(J_{r-1}\), since it would divide every generator of \(J\).
The ideal \(J_{r-1}\) is proper (all entries of the smaller matrix
are in the homogeneous maximal ideal); the determinantal height
bound therefore gives height two. Likewise \(\gcd(D_r,K_r)=1\).
The basic double link exact sequence now yields
\[
[V(J)]=[V(J_{r-1})]+[V(D_r,K_r)].
\]
Apply the same argument to the smaller matrix: its last row again
has only the one last-column entry. Iteration reaches a two-row,
one-column matrix whose two nonzero entries are coprime by the
height argument. Hence
\[
[V(J)]=[V(A,B)]+\sum_{j=1}^{r}[V(D_j,K_j)].
\]
The degrees of the stripped pair are \(a-e,b-e\), since the
product \(\prod_jD_j\) is exactly the gcd of the first two minors;
it has degree \(\sum_j(c_{j+1}-c_j)=a+b-c_1=e\).
For the intermediate steps \(K_j\) denotes the last-row-deleted
minor of the matrix truncated to its first \(j+2\) rows and \(j+1\)
columns, with degree \(c_j+c_{j+1}-(a+b)\).
The weight-equivariant resolution makes all minors and staircase
entries eigenforms. Every summand is an effective CI cycle and
therefore has only translated-quartic support by the exact
Chow-matched cycle condition. Each summand has zero moment, so
the sum does as well.

Theorem candidate implies a hypothetical characteristic-zero
sole-supported CI has non-ACM full graded intrinsic limits in
**both** orientations, improving the three-generator bound.
If a Chow-matched ACM limit has extras, each nonempty summand has
both defining degrees at least three by the elementary arrangement
plane/quadric exclusions. Thus \(a-e\ge3\), all
\(c_{j+1}-c_j\ge3\), and \(a\ge3(r+1)\). These inequalities
are consequences of the cycle decomposition, not an independent
numerical method. They also explain uniformly why a non-CI ACM
limit of a Chow-matched quartic pair is impossible.

### 7.3 Pure cycles rather than special-fiber ACMness

Passing to the pure hull preserves the fundamental cycle, as do
all zero-dimensional embedded or saturation corrections. Thus
even non-ACM limits are covered whenever the pure hull has an
effective invariant-CI cycle decomposition. In particular the
[actual (16,16) Chow-matched control](chow_matched_equation_layers.md#opposite-full-limits-can-retain-a-large-embedded-hilbert-correction)
has non-ACM limits at both ends but invariant CI pure hulls
\((U,V^{16})\) of type \((4,64)\); their endpoint corrections have
length 4608. Independently the original pencil of this control
contains the eigenform \(U^4\), so this is not a new exclusion.
It shows why neither ACM preservation nor preservation of CI degrees
under taking pure hulls is the right general hypothesis.

The recursive last-row argument applies to any invariant
Hilbert–Burch matrix having the requisite successive one-entry
rows, regardless of the Hilbert series. But an arbitrary ACM pure
hull need not retain the CI numerator and need not have that
staircase; no general claim about its moment follows from ACMness alone.
Likewise the full non-ACM limit has a longer free resolution,
whose alternating Hilbert numerator does not give the matrix above.
The next question is whether the non-ACM boundary can always
be reduced, at the cycle level, to these decomposable pure hulls,
or whether there are invariant pure-hull cores escaping this
mechanism. Do not assume such a reduction. In particular a
degree-independent bound on the number of missing line layers
is not supplied by this argument. The existing non-ACM controls
and the [homogeneous ACM-thickening question](../../frameworks/global-equation-realization/projection_and_liaison.md)
must guide that next investigation.
