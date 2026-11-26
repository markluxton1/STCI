# Chow realization and first-moment separation

**Scoped correctness review (2026-11-23, combined integration):** independently reconstructed the stated low-degree realization arguments, ACM Hilbert–Burch/basic-double-link decomposition, exceptional quartic construction, reciprocity and universal depressed-quartic spectrum construction. Inherited inputs are the accepted quartic diagonal exclusion and balanced normal splitting; arbitrary non-ACM limits and unrestricted moment vanishing are not covered.

**Status:** proposed argument, covered by the scoped correctness review above. Characteristic zero
unless otherwise stated. This develops the existing
[first-moment theorem](chow_arrangement_moments.md), not a new unrestricted
STCI exclusion. The classical cubic-carrier theorem of Craighero–Gattazzo
([1989](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf)) and
[R-0022](../../results/quartic_44_filtered_exclusion.md) are independent
benchmarks; neither is used in the moment proof for (3,4) or the
multiple-support proof for (4,4).

**Coefficient-only realization interface.** The focused [transverse Chow / mixed-moment criterion](transverse_chow_moment_realization.md) records the homogeneous full transverse Chow polynomial, its quadric-spectrum specialization, the characteristic-zero coefficient-to-power-sum dictionary, and the determinantal reformulation of the existing *reduced-cycle* CI criterion. It deliberately avoids fixing a carrier and explicitly separates necessary rank vanishings from properness and the unresolved repeated-cycle case.

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
([proof](chow_arrangement_moments.md#a-regular-function-on-the-chow-space)).
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

### Source parameter space and equal-degree Chow fibers

The [focused source-parameter argument](chow_source_parameter_geometry.md#source-parameter-space-and-equal-degree-chow-fibers) records a provisional deduction from the resultant linear system: the Chow morphism from the proper equal-degree pencil locus is affine. In particular a nonconstant fixed-cycle orbit cannot have both limiting pencils proper. This explains the need for non-CI boundary points without proving moment vanishing. The unequal-degree source geometry is different.

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
bound. The scoped correctness review above covers these proof routes; no unrestricted all-degree theorem is claimed.


## 7. Beyond coprime initials: basic double linkage and ACM full limits

**Proposed statements, covered by the scoped correctness review above.** Use the full graded
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
staircase. The subsequent [sign-symmetry theorem](chow_acm_parity_vanishing.md)
nevertheless proves moment vanishing for **every invariant ACM pure hull**
with the entire translated cycle, in characteristic different from two,
without a prescribed numerator or CI-cycle decomposition. Thus in
characteristic zero both invariant pure hulls of a hypothetical
sole-supported CI must be non-ACM. The decomposition question retains its
independent structural meaning but is no longer needed for this vanishing.
The full non-ACM limit has a longer free resolution,
whose alternating Hilbert numerator does not give the matrix above.
The next question is whether the non-ACM boundary can always
be reduced, at the cycle level, to moment-zero pieces,
or whether genuinely non-ACM invariant pure-hull cores escape this
mechanism. Do not assume such a reduction. In particular a
degree-independent bound on the number of missing line layers
is not supplied by this argument. The existing non-ACM controls
and the [homogeneous ACM-thickening question](../../frameworks/global-equation-realization/projection_and_liaison.md)
must guide that next investigation.


## 8. Signed cycle decompositions for non-ACM limits

**Proposed argument, covered by the scoped correctness review above.** The adjacent literature is
Goto--Heinzer--Kim, *The leading ideal of a complete intersection of height
two, Part II*, J. Algebra 312 (2007), 709--732
([DOI](https://doi.org/10.1016/j.jalgebra.2007.02.025)), on leading ideals
and successive gcds for the local maximal-ideal filtration; the filtration
and grading here are different. The basic-double-link identity of Section 7
does not require the residual scheme to be ACM for its cycle calculation.

Let \(J=(f_1,\ldots,f_s)\) be any invariant ordinary-homogeneous height-two
ideal, with weight-homogeneous generators. Put \(g_i=\gcd(f_1,\ldots,f_i)\),
\(h_i=g_{i-1}/g_i\), \(K_i=f_i/g_i\), and
\(J_i=(f_1/g_i,\ldots,f_i/g_i)\). Then \(J_1=S,\ J_s=J\),
\(J_i=h_i J_{i-1}+(K_i)\), and \(\gcd(h_i,K_i)=1\).
The colon exact sequence yields
\[
[Z_i]=[V(h_i,K_i)]+[V(J_{i-1}+(K_i))],
\]
where \(Z_i\) means the one-cycle of \(V(J_i)\), including zero when
there is no curve. A unit factor contributes the zero cycle. There are
no height-one components of \(J_i\) since its generators have gcd one.
At each height-two prime the quotient by \(K_i\) can only decrease length.
Consequently the effective loss
\(\Delta_i=[Z_{i-1}]-[V(J_{i-1}+(K_i))]\) gives the exact signed
decomposition
\[
[V(J)]=\sum_{i=2}^s[V(h_i,K_i)]-\sum_{i=2}^s\Delta_i.
\]
In particular the degree inequality
\(\deg Z_s\le\sum_i(\deg g_{i-1}-\deg g_i)(\deg f_i-\deg g_i)\)
is an equality precisely when all loss cycles vanish. It then supplies
an effective CI decomposition without requiring ACMness. This is a
cycle statement, not an assertion about removal of embedded points.

The existing trace proof extends to all invariant proper CIs disjoint
from \(\ell=V(x_0,x_3)\), whether or not all components are full-support
quartics: the two missing middle vertices force the same weight
assignments and congruences, and the same rectangular finite-free basis
gives trace zero. Projection to \([x_0:x_3]\) is finite on every curve
disjoint from \(\ell\), hence neither endpoint coordinate is identically
zero on such a curve. Any invariant boundary curve then has \(x_1=0\)
or \(x_2=0\) and its trace contribution is zero. Extend \(M_1\) by zero
on these boundary curves. Thus if every nontrivial CI term in the signed
decomposition misses \(\ell\), then
\(M_1(Z_s)=-\sum_i M_1(\Delta_i)\). The moment vanishes if all losses
are in the coordinate boundary, equivalently if the sum of the
full-support degrees on the positive side equals the full-support
degree of \(Z_s\). Total-degree equality is unnecessary. Avoidance of
\(\ell\) by the individual CI terms, and absence of full-support loss,
are substantive additional hypotheses, not consequences of the final
limit missing \(\ell\). No unrestricted proof of either is given.

A small control is the invariant cubic pair
\[
(x_0^2x_2-x_1^3,\ x_2^3-x_1x_3^2).
\]
Its dense quotient is \(u=1,\ v^2=1\); the only boundary curve is
\(L_{03}\) (check \(x_0=0,x_3=0\) give the endpoints, and either
middle coordinate zero forces the other zero). The two cubics have
independent normal differentials at the generic point of \(L_{03}\).
Thus its cycle is \([C_{1,1}]+[C_{1,-1}]+[L_{03}]\), with
degree nine and disjoint from \(\ell\). The degree-eight union is the
residual to \(L_{03}\) under ordinary CI linkage: its generic
multiplicities are one and the link is unmixed, hence reduced. In
particular it is ACM. Its moment is zero, but it cannot be an
effective sum of nonempty translated-arrangement CIs, since each such
CI has degree at least twelve. This is a counterexample to demanding
such a decomposition for all invariant ACM pure schemes, not an
example of a Chow-matched CI full limit. The sign-symmetry theorem now
explains its zero moment without such a decomposition. Boundary-compatible
signed decomposition remains a sufficient condition for non-ACM cores.

## 9. Uniqueness of the regular additive first-moment candidate

In characteristic zero let \(h\in k[u^{\pm1},q^{\pm1}]\) and define
\(M_h(\sum n_i[z_i])=\sum n_i h(z_i)\). If \(M_h\) vanishes on just
the two constructed invariant (3,4) families in Section 4, then
\(h=cq\) for some \(c\in k\). Indeed for each fixed \(u=\lambda\),
the depressed-cubic family gives the Laurent polynomial identity
\[
h(\lambda,x)+h(\lambda,y)+h(\lambda,-x-y)=0
\]
on the dense open where \(xy(x+y)\ne0\). Differentiating once in
each variable gives \(h_{qq}(\lambda,-x-y)=0\); hence
\(h(\lambda,q)=A(\lambda)q+B(\lambda)\), and substitution gives
\(3B(\lambda)=0\). This is the elementary Laurent version of the
characteristic-zero additive-polynomial calculation (Milne,
*Algebraic Groups*, §2, 2.21). Repeating on every fiber of \(uq^2\)
gives \(h(u,q)=q\,B'(uq^2)\). Thus \(h/q\) is both in
\(k[u^{\pm1}]\) and \(k[(uq^2)^{\pm1}]\), whose intersection is \(k\)
by distinct Laurent characters. Conversely \(q\) vanishes on both
families as a summed moment. This identifies the unique candidate
among degree-independent **regular additive** functions on the
arrangement monoid. It makes no assertion about nonlinear functions,
arbitrary nonregular additive maps, or higher-degree Chow equations.
The unrestricted vanishing on actual CI pairs remains open.


## 10. Density of reduced arrangements fails already for (4,4)

**Proposed proof, covered by the scoped correctness review above.** In characteristic zero
every invariant CI arrangement is in the closure of reduced ones in its
own bidegree: vary its two weight-homogeneous generators in their weight
spaces. The pure powers of the middle variables make these systems
basepoint-free on the dense coordinate torus. General members meet
smoothly there by Bertini; properness and the absence of boundary curves
are open and hold at the given pair. This proves density within the
invariant realization locus, not in the unrestricted Chow-matched
incidence.

The following exact control shows that allowing arbitrary embedded
realizations produces an additional cycle component. It uses the
opposite-parameter exceptional locus identified in Section 5, and the
cubics of Section 8. Set
\[
 A=x_0^2x_2-x_1^3,\quad B=x_2^3-x_1x_3^2,\quad
 D=x_0^2x_3^2-x_1^2x_2^2,
\qquad F=x_1A-x_2B+D,\quad G=x_1B-x_2A.
\]
Both quartics contain \(C_{1,1}\) and \(C_{1,-1}\).
In \((1,r,ur^3,vr^4)\) coordinates the three source equations
are \(r^3(u-1),r^9(u^3-v^2),r^8(v^2-u^2)\).
At either \((1,\pm1)\) put \(\eta=du,\xi=d(u^3-v^2)\);
then \(d(v^2-u^2)=\eta-\xi\), so
\[
 d_\perp F=r^4(1+r^4)(\eta-r^4\xi),\qquad
 d_\perp G=-r^6(\eta-r^4\xi).
\]
Both generic local lengths are at least two. On \(x_0=0\)
their restrictions are
\[
 -x_1^4-x_2^4+x_1x_2x_3^2-x_1^2x_2^2,\qquad
 x_1(x_2^3+x_1^2x_2-x_1x_3^2).
\]
If \(x_1\ne0\) the second equation substituted into the first
gives \(-x_1^4=0\). Otherwise the first forces \(x_2=0\).
The common support in that plane is just \(p_\infty\).
A common projective surface factor would meet the plane in a curve.
Hence the pair is proper and degree exhaustion gives exactly
\[
 [V(F,G)]=2[C_{1,1}]+2[C_{1,-1}].
\]
Diagonal translates realize every cycle with support
\((u,q)=(\lambda,r),(\lambda,-r)\) and multiplicities \((2,2)\).

### 10.1 Closedness of the invariant quartic cycle locus in the interior

The [invariant quartic classification](../equations/chow_polytope_rigidity.md#quartics-including-invariant-collision-lifts)
gives \(v_i=\alpha+\beta u_i\), \(\alpha\ne0\), and the weight-twelve
mate \(u^4+B'uv^2+C'v^3=0\), \(C'\ne0\).
In \(q=u/v\) this latter equation becomes
\(\alpha q^4+(B'q+C')(1-\beta q)=0\). Thus its root multiset
has \(e_1=0,\ e_2-\beta e_3+\beta^2e_4=0\), where \(e_j\)
are the elementary symmetric functions of the four q's, with repetition.
Conversely these conditions and the line relation give the invariant
realization, taking \(C'=\alpha e_4\) and
\(B'=-\alpha e_3+\beta C'\).
The slope \(\beta\) is integral since \(e_4\) is invertible.
On the ordered cover \(T^4\) the incidence
\[
 e_1=0,\quad \beta^2-(e_3/e_4)\beta+e_2/e_4=0,\quad
 v_i-v_j=\beta(u_i-u_j)
\]
is finite over \(T^4\); its image is closed (Stacks Project,
Tag 01WM, finite/integral morphisms are closed). Any point in this
image has \(\alpha=v_i-\beta u_i\ne0\): otherwise all \(q_i\)
would equal \(1/\beta\), contradicting \(e_1=0\) in characteristic zero.
It therefore lifts invariantly by the converse just described.
The symmetric quotient is finite and closed, so the invariant
realization locus is closed in \(A_4\); Bertini gives equality with
the relative closure of the reduced realization locus.
This relative topology agrees with the interior Chow topology:
the multiplication map from \(\operatorname{Sym}^4 S\) is finite
(Section 1), and the inverse image of an interior arrangement cannot
contain any boundary degree-four summand by positivity of cycles.

The opposite doubled configuration cannot satisfy the finite-slope
line condition: its \(u_i\)'s agree but its \(v_i\)'s differ.
Hence it is not in the interior closure of the reduced realization
locus, even as a Chow cycle. Since no nonempty CI arrangement
has degree below twelve, degree sixteen cannot be a sum of two
nonempty CI arrangement cycles, so it also refutes the proposed
same-total-degree additive reduced density statement.

### 10.2 Entire (4,4) cycle locus and implications

Combine Section 5 with the new realization. Off \(B(u)\cap B(uq^2)\)
the extreme-component lemma supplies an invariant lift. On that
intersection Section 5 excludes the unbalanced two-support distribution;
the balanced one is the explicit construction above up to diagonal
translation. The small diagonal is excluded independently by R-0022.
Thus as reduced cycle loci
\[
 R_{4,4}=R_{4,4}^{\mathrm{inv}}\ \sqcup\
 E,\qquad
 E=\{2[(u,v)]+2[(u,-v)]:(u,v)\in T\}.
\]
The first locus is irreducible of dimension four by the invariant
classification, and closed in \(A_4\) by the slope argument.
The second is closed in \(A_4\): on \(T^4\) it is the finite union
of the closed equations for a constant \(u\), two equal \(v\)'s and
the other two equal to their negatives, and the quotient is finite.
It is irreducible of dimension two, parametrized by \(u,v^2\).
Thus there are exactly two irreducible components, and the second
is entirely nonreduced. This classification uses R-0022 only to
remove the small diagonal, not to establish the new exceptional
component or its lack of reduced density. Both components lie in
\(V(M_1)\).

The original density proposal must consequently allow more than
sums of reduced full-support CI arrangements. The new component is
twice the full-support part of the invariant (3,3) cycle in Section 8,
after deleting \(L_{03}\). That is already compatible with the
boundary-discarding, zero-moment monoid from Section 8. It gives
a concrete reason to enlarge the known closure to such cycles,
rather than assume all repeated CI cycles are smoothable through
reduced Chow-matched CIs. No density theorem for that enlarged
monoid is proved. Nor does the example refute density in the
closure of all currently moment-covered realizations (it is itself
covered). The unrestricted moment question remains open.


## 11. The two extreme mixed coefficients of the quadric-spectrum equation

**Exact comparison (characteristic zero; no invariance required for the
spectral equation).** For a proper CI \(Y=V(F_a,G_b)\) with whole cycle
\(\sum_i n_i[C_{u_i,v_i}]\), put
\[
 A=x_1x_2,\quad B=x_0x_3,\quad q_i=u_i/v_i,\quad
 m=\sum_i n_i=ab/4,\qquad
 H_Z(A,B)=\prod_i(A-q_iB)^{n_i}.
\]
This polynomial is **an actual member of \((F,G)\)**, not just of its
radical. At the generic point of each \(C_i\), \(S/(F,G)\) is Artinian
local of length \(n_i\), so its maximal ideal has \(n_i\)-th power
zero. In particular \((A-q_iB)^{n_i}=0\) there. The product vanishes
at every minimal associated prime, and \(S/(F,G)\) is Cohen--Macaulay
with no embedded associated primes. Therefore \(H_Z\in(F,G)\).
The standard inputs are complete-intersection Cohen--Macaulayness
([Stacks, Tag 00S8](https://stacks.math.columbia.edu/tag/00S8)) and
unmixedness ([Stacks, Tag 00N2](https://stacks.math.columbia.edu/tag/00N2)).
This already appears as an implication in the quadric-pencil
discussion; it is recorded here to make its exact scope explicit.

Write \(e_j=e_j(q_1,\ldots,q_m)\), with the roots repeated according
to multiplicity. Vieta's formulas give
\[
 H_Z=A^m-e_1A^{m-1}B+\cdots+
 (-1)^{m-1}e_{m-1}AB^{m-1}+(-1)^me_mB^m,
\quad
 e_1=\sum n_iq_i,\quad
 e_{m-1}=e_m\sum n_iq_i^{-1},\quad e_m\ne0.
\]
Thus the two mixed coefficients encode traces of **inverse** operators:
\[
 -[A^{m-1}B]H_Z=\operatorname{Tr}(\xi),\qquad
 -\frac{[AB^{m-1}]H_Z}{[B^m]H_Z}
 =\operatorname{Tr}(\xi^{-1}),\qquad \xi=A/B,
\]
on a generic length-\(m\) transverse algebra. The reciprocal is
well-defined on each full-support component. The usual
trace--norm/characteristic-polynomial identities (e.g.
[Stacks, Tag 0BIE](https://stacks.math.columbia.edu/tag/0BIE))
supply this pairing; Gorenstein duality by itself does not equate
the two traces. Under the quotient torus scaling \(q\mapsto\lambda q\),
the two traces have weights \(+1\) and \(-1\), respectively.
Consequently there is no canonical same-weight linear identification
without additional geometric structure.

**Why the two ends of the quadric pencil are asymmetric.** Its two
reducible members are
\[
 Q_0=V(A)=V(x_1)\cup V(x_2),\qquad
 Q_\infty=V(B)=V(x_0)\cup V(x_3).
\]
On each translated quartic the coordinate hyperplane divisors are
\[
\begin{array}{c|c}
x_0 &4p_\infty\\
x_3 &4p_0\\
x_1 &3p_\infty+p_0\\
x_2 &p_\infty+3p_0 .
\end{array}
\]
Hence the two planes of \(Q_\infty\) have quadruple endpoint contact,
while those of \(Q_0\) have \(3+1\) contact. No ambient automorphism
preserving the curve can exchange these two pairs of planes, since
their intersection divisors on the curve have different multiplicity
partitions. The apparent algebraic exchange \(A\leftrightarrow B\)
does not preserve the fixed embedded rational-quartic problem.

**An entire \((4,4)\) CI family with one coefficient free.** Fix
\[
 F=x_1^4-x_0^3x_3,\quad
 G_{\alpha,\beta}
 =x_2^4+\alpha x_1x_2x_3^2+\beta x_0x_3^3,\quad
 \beta\ne0.
\]
The restrictions to the disjoint line \(L_{12}=V(x_0,x_3)\) are
\(x_1^4,x_2^4\), so this is a proper CI. On the dense torus,
using \([1:r:ur^3:vr^4]\), its equations are
\(v=1\) and \(u^4+\alpha u+\beta=0\).
The roots are all nonzero; their quartic components exhaust its
degree \(16\), with the correct root multiplicities. Therefore
\[
 H_Z(A,B)=A^4+\alpha AB^3+\beta B^4.
\]
In particular \([A^3B]H_Z=0\) for every \(\alpha\), while
\([AB^3]H_Z=\alpha\) is free. Choosing \((\alpha,\beta)=(-1,1)\)
gives the squarefree polynomial \(q^4-q+1\), an explicit reduced
proper CI with a nonzero opposite mixed coefficient.
For this example \(\sum q_i^{-1}=-\alpha/\beta\).
This conclusively disproves the proposed general pairing as
simultaneous vanishing, even within invariant actual CI arrangements.

**Why special degrees can nevertheless have both coefficients zero.**
Coordinate reversal identifies the fixed carrier \(F\) above with
the already-classified quartic carrier in
[fixed-carrier Chow arrangements](fixed_carrier_chow_arrangements.md).
The normalization semigroup is \(\langle3,4\rangle\), whose positive
gaps are exactly \(\{1,2,5\}\). The descent theorem says that in
a fixed-carrier \((4,m)\) arrangement
\[
 e_j(q)=0\quad\text{precisely for the obligatory missing indices }
 j\in\{1,2,5\}\cap[1,m],
\]
with no implication that other coefficients must be nonzero.
The opposite mixed term has \(j=m-1\). Hence **both extreme mixed
coefficients are forced zero on this carrier for \(m=3\) and \(m=6\)**:
\(m-1=2,5\), respectively. In degree \((4,4)\), \(m-1=3\)
is allowed and the explicit family shows it varies. The case \(m=2\)
has no proper fixed-carrier realization (its nonzero constant
coefficient would itself occupy a forbidden gap); \(m=5\) is also
empty. The simultaneous vanishing for \(m=3,6\) is a
**degree-specific conductor/semigroup phenomenon**, not a symmetry
of the general quadric pencil.

**Consequence for the universal obstruction.** It is legitimate to
compare both ends as the trace and reciprocal trace, or as the
first polar coefficients at the reducible pencil members. It is not
legitimate to infer the vanishing of the reciprocal trace from \(M_1=0\),
nor to argue by an involution exchanging the pencil ends.
A more plausible global argument must explain why the *particular*
trace \(\operatorname{Tr}(A/B)\), but not its reciprocal, has a
missing coefficient for all actual Chow-matched CIs. The
low-fiber-layer trace formula in
[fixed surfaces and endpoint algebras](fixed_surface_and_endpoint_algebras.md#7-the-first-trace-depends-only-on-two-lower-fiber-degree-layers)
provides an exact test of this proposed one-sided mechanism.


### 11.1 Opposite Chow charts pair the coefficients exactly

This is a direct consequence of the classical Chow resultant
interpretation and homogeneity; it creates **no new CI constraint**.
It makes precise how the two coefficients are geometrically paired.

Use the two coordinate charts of the **same** family of lines:
\[
\begin{array}{ll}
 \ell^+_{s,t}:&x_0=sx_1,\quad x_3=tx_2,\\
 \ell^-_{s,t}:&x_1=sx_0,\quad x_2=tx_3.
\end{array}
\]
On the common \(s,t\ne0\) torus, \(\ell^-_{1/s,1/t}=\ell^+_{s,t}\).
The origin of the plus chart is the disjoint line
\(L_{12}=V(x_0,x_3)\); the origin of the minus chart is the secant
\(L_{03}=V(x_1,x_2)\), through both endpoints.

For a *single* \(C_{u,v}\), with homogeneous parameters \(S,T\),
substitute into the two equations defining each line and take their
degree-four binary resultant. With the displayed equation order and
standard Sylvester convention, writing \(z=st\), these are
\[
\begin{aligned}
 R^+_{u,v}(s,t)
 &=\operatorname{Res}_{S,T}
   \big(S^3(S-sT),\ T^3(vT-tuS)\big)
   =v^4(1-qz),\\
 R^-_{u,v}(s,t)
 &=\operatorname{Res}_{S,T}
   \big(S^3(T-sS),\ T^3(uS-tvT)\big)
   =v^4z^3(z-q),
 \qquad q=u/v .
\end{aligned}
\]
Both formulas follow by multiplicativity of the resultant for the
factored forms; no genericity or reducedness is required. They have
also been checked by the \(8\times8\) Sylvester determinant.
The \(s^3t^3\) factor in the second formula records the \(3+1\)
endpoint-contact partitions, not a new divisor of the arrangement.

For an arbitrary effective arrangement
\(Z=\sum_i n_i[C_{u_i,v_i}]\), multiply the single-curve forms.
With \(K=\prod_i v_i^{4n_i}\ne0\),
\[
 \boxed{R_Z^+(s,t)=K\,H_Z(1,st),\qquad
        R_Z^-(s,t)=K\,(st)^{3m}H_Z(st,1).}
\]
Thus
\[
 \boxed{R_Z^-(z)=z^{4m}R_Z^+(1/z)}
\]
in the one-variable notation, where the reciprocal has degree
\(4m\) with \(3m\) leading zero coefficients in the plus chart
(or a factor \(z^{3m}\) in the minus chart).
Equivalently,
\[
\begin{aligned}
 R_Z^+(z)/R_Z^+(0)
   &=1-M_1z+\cdots,\\
 \frac{R_Z^-(z)/z^{3m}}{[z^{3m}]R_Z^-(z)}
   &=1-\Big(\sum_i n_iq_i^{-1}\Big)z+\cdots .
\end{aligned}
\]
The second normalization is legitimate because all \(q_i\ne0\).

**Important non-implication.** The reciprocal relation follows
formally from multihomogeneity of *any* curve's Chow form: if
\(d=\deg Z\), the two hyperplanes in the minus chart at
\((1/s,1/t)\) are respectively \(-1/s\) and \(-1/t\) times those in
the plus chart. Thus for any degree-\(d\) curve
\[
 R^-(s,t)=(st)^d R^+(1/s,1/t)
\]
on the common torus, irrespective of whether the curve is a CI.
The support-on-translates hypothesis is what specializes both
restrictions to a single variable \(st\) and forces the
\(3m\) endpoint factor. Neither property forces its next coefficient
to vanish: §11's quartic family has \([AB^3]H\ne0\).

There is also the classical apolar pairing on binary forms
\(\operatorname{Sym}^m\langle A,B\rangle\), where the basis vectors
\(A^{m-1}B\) and \(AB^{m-1}\) pair nontrivially. This is the top
transvectant (see [Borcea--Brändén representation account,
§3](https://link.springer.com/article/10.1007/s00209-021-02825-4)).
A bilinear pairing of basis vectors is not an equation equating
their coefficients in one form \(H_Z\), absent an additional
self-duality constraint. No such constraint follows from the CI
condition; the quartic example rules out the suggested equality or
simultaneous zero statement.

**Geometric source of asymmetry.** Projection from \(L_{12}\), which
misses every translated quartic, gives the finite-free cover used
for the global trace of \(x_1x_2\) over \(k[x_0,x_3]\); on the
arrangement its trace is \(4M_1x_0x_3\). The opposite center
\(L_{03}\) contains \(p_0,p_\infty\), so it is *not* a basepoint-free
projection of the curve. This obstructs copying the first trace
proof verbatim for the reciprocal operator. The \(z^{3m}\) factor
is the Chow manifestation of the endpoint defect.

A bounded next test is therefore one-sided: study whether the **actual
resultant image of a complete-intersection pair**, when constrained to
\(R^+(s,t)=K P(st)\) with \(\deg P=m=ab/4\), necessarily has
\([st]R^+=0\). The reciprocal chart imposes no independent equation;
it only repackages the same resultants. Existing §7 of
[fixed surfaces and endpoint algebras](fixed_surface_and_endpoint_algebras.md#7-the-first-trace-depends-only-on-two-lower-fiber-degree-layers)
gives an exact low-layer formula for that coefficient, and its
§8 gives a residual-curve control showing that weaker endpoint
conditions do not suffice.


### 11.2 The degree-six coincidence is actually realized

The fixed-carrier prediction that both opposite mixed coefficients
vanish for \(m=6\) is witnessed by an explicit \((4,6)\) CI:
\[
 F=x_1^4-x_0^3x_3,\qquad
 G=x_2^6+x_1x_2^3x_3^2+x_1^2x_3^4.
\]
The restrictions to \(L_{12}\) are \(x_1^4,x_2^6\), hence the
pair is proper. On the dense torus \(v=1\), and the mate equation
is \(u^6+u^3+1=0\). In characteristic zero this is squarefree,
with all six roots nonzero. Those degree-four components exhaust
the Bézout degree \(24\), and their spectral polynomial is
\[
 H_Z(A,B)=A^6+A^3B^3+B^6.
\]
Both \(A^5B\) and \(AB^5\) have zero coefficients. This is the
specific semigroup-gap phenomenon \(1,5\notin\langle3,4\rangle\);
it does not generalize to the \((4,4)\) example in §11, where
\(3\in\langle3,4\rangle\).

The comparison isolates what may still be useful: a fixed-carrier
*descent* restriction can annihilate both opposite polar
coefficients in exceptional degrees, but the bare reciprocity of
opposite Chow charts cannot do so. A general CI theorem would
need a new descent/gluing statement that applies without an
actual fixed carrier.


## 12. The integral (4,4) binomial pair: four translates versus a Frobenius thickening

**Previously established scheme theorem:** [R-0021](../../results/quartic_mu4_degeneration.md),
with proof in [quartic specialization](../quartic_specialization_and_symbols.md#1-what-actually-coalesces),
gives the flat family over \(\mathbb Z\), reduced four-curve characteristic-zero
fiber, and sole-support characteristic-two fiber with generic
\(k(C)[\varepsilon]/(\varepsilon^4)\) transverse algebra. This section
only translates that accepted result into the quadric-spectrum and
opposite-coefficient language of §11. No new STCI or lifting claim
is made.

Fix the homogeneous quartic equations over \(\mathbb Z\)
\[
 F=x_1^4-x_0^3x_3,\qquad G=x_2^4-x_0x_3^3.
\]
On the dense projective torus use
\([1:r:ur^3:vr^4]\). There
\[
 F=r^4(1-v),\qquad G=r^{12}(u^4-v^3),
\]
so the complete intersection is
\(\mathbb G_{m,r}\times\mu_4\), with \(v=1,\ u^4=1\).
The quadric-pencil parameter \(\xi=x_1x_2/(x_0x_3)\) is
\(\xi=u/v=u\).

Set \(A=x_1x_2\), \(B=x_0x_3\). The exact spectral polynomial
over \(\mathbb Z\) is
\[
 \boxed{H(A,B)=A^4-B^4}
\]
and its actual ideal membership has the *integral* Koszul expression
\[
 \boxed{A^4-B^4=x_2^4F+x_0^3x_3G
             =x_1^4G+x_0x_3^3F.}
\]
This is not merely membership in a radical. Its middle coefficients
\([A^3B]H=[A^2B^2]H=[AB^3]H=0\) vanish integrally,
not only after reduction modulo two.

Over an algebraically closed field of characteristic zero,
\(u^4-1=\prod_{\zeta\in\mu_4}(u-\zeta)\) has four distinct
roots. Its cycle is
\[
 Z_0=[C_{1,1}]+[C_{-1,1}]+[C_{i,1}]+[C_{-i,1}],
 \qquad H_{Z_0}(A,B)=\prod_{\zeta^4=1}(A-\zeta B)=A^4-B^4.
\]
All four curves are generically reduced, each of degree four;
the full intersection has degree \(16\), so there is no other curve.
Both extreme mixed coefficients vanish. In characteristic two,
\(u^4-1=(u-1)^4\) by Frobenius, and hence
\[
 Z_2=4[C_{1,1}],\qquad
 H_{Z_2}(A,B)=(A-B)^4=A^4-B^4=A^4+B^4
 \quad\text{in characteristic }2.
\]
On the dense torus the algebra is
\(k[r^{\pm1},\varepsilon]/(\varepsilon^4)\)
with \(\varepsilon=u-1\), as in R-0021. This is a fourfold
generic thickening of one curve, *not* a union of four distinct
translates. There is no extra projective residual curve:
the two chart normal forms in R-0021 cover the fiber.

The characteristic polynomial of multiplication by \(\xi=u\) on
the rank-four transverse algebra has the **same integral
presentation** over \(\mathbb Z\):
\[
 K=\mathbb Z[u]/(u^4-1),\qquad
 M_\xi=
 \begin{pmatrix}
 0&0&0&1\\1&0&0&0\\0&1&0&0\\0&0&1&0
 \end{pmatrix}
 \text{ in the basis }(1,u,u^2,u^3),\qquad
 \det(T-M_\xi)=T^4-1 .
\]
In characteristic zero this operator is semisimple with eigenvalues
\(\{1,-1,i,-i\}\); in characteristic two it is a single unipotent
Jordan block, since \((M_\xi-I)^4=0\) but
\((M_\xi-I)^3\ne0\). Both
\(\operatorname{Tr}(\xi)\) and
\(\operatorname{Tr}(\xi^{-1})\) vanish over \(\mathbb Z\);
the first trace is the coefficient of \(A^3B\), the reciprocal trace
controls that of \(AB^3\). In characteristic zero this is
cancellation across four distinct roots; in characteristic two
the weighted moments are \(4\cdot1=0\), because the scalar \(4\)
vanishes. The equality of traces across characteristics is not
evidence for a characteristic-zero sole-support STCI.

The opposite line-chart restrictions of §11.1 specialize to
\[
 R^+(z)=H(1,z)=1-z^4,\qquad
 R^-(z)=z^{12}H(z,1)=z^{12}(z^4-1).
\]
Modulo two, these become
\(R^+(z)=(1-z)^4\) and
\(R^-(z)=z^{12}(z-1)^4\).
The reciprocal relation is still automatic and does not prevent
the four spectral points from coalescing.

Two qualifications clarify the meaning of the comparison:

1. For the **characteristic-zero** fixed quartic carrier of §11,
   the semigroup gaps force \(e_1=e_2=0\) for \(m=4\),
   but *do not* force \(e_3=0\). The vanishing of both
   extreme mixed coefficients in this binomial pair is the
   extra special equation \(u^4=1\); §11's proper
   \(q^4+\alpha q+\beta=0\) family exhibits freely varying
   \([AB^3]H=\alpha\).
2. The \(\mathbb Z\)-family is flat as a family of complete
   intersections, while its **generic-fiber support changes**:
   four translates in characteristic zero collapse to
   one support in characteristic two. It is *not* a
   mixed-characteristic lift with sole support \(C\) in
   characteristic zero. This distinguishes R-0021 from the
   separate no-flat-sole-support-lift result for the intrinsic
   characteristic-two triple structure.

**Implication for the unrestricted moment program.** This
example cannot establish a general vanishing of the reciprocal
moment, since it has an exceptional binomial symmetry; nor can
moment vanishing in characteristic two exclude the deepest diagonal
when its multiplicity is divisible by the characteristic.
It does show that \(H_Z\) is a natural integral spectral object
whose same coefficient vector can encode either split eigenvalues
or a nilpotent thickening after reduction.


## 13. Complete quadric-spectrum projections in degrees (3,4) and (4,4)

**New calculation; covered by the scoped correctness review above.** This is a
statement about projection to the unordered multiset of *quadric parameters*
\(q=u/v\), not the full parameter pairs \((u,v)\). It uses the already
proved invariant quartic-pair classification in
[Chow-polytope rigidity](../equations/chow_polytope_rigidity.md#quartics-including-invariant-collision-lifts)
and the established fixed cubic carrier of §4. The classical
algebraic inputs are Vieta's formulas, root multiplicity via
squarefree factorization and the resultant/discriminant. No claim
that the full arrangement realization locus is a depressed-polynomial
space is intended.

Let \(\mathcal P_m=\{T^m+\sum_{j=2}^m c_jT^{m-j}:c_m\ne0\}\),
the space of monic degree-\(m\) polynomials with nonzero constant
term and zero next-to-leading coefficient. The map from an
arrangement cycle to \(\prod_i(T-q_i)^{n_i}\) forgets the separate
\(u_i,v_i\) and retains the multiplicity-weighted quadric divisor.

For \(m=3\) in characteristic zero, the fixed cubic carrier of §4
gives every \(T^3+c_2T+c_3\) with \(c_3\ne0\) as the spectrum of
an actual invariant proper (3,4) CI. The root partitions in
characteristic zero are \((1,1,1)\) and \((2,1)\), with (3)
excluded by \(3q\ne0\). This is a surjection to \(\mathcal P_3\)
and does not identify the higher-dimensional full arrangement space.

**An exact universal (4,4) construction.** Work over any algebraically
closed field \(k\). Given
\[
 P(T)=T^4+c_2T^2+c_3T+c_4,\qquad c_4\in k^\times,
\]
choose any root \(\beta\in k\) of
\[
 c_4\beta^2+c_3\beta+c_2=0
\]
and set \(\gamma=c_3+c_4\beta\). Define
\[
\begin{aligned}
 F&=x_1^4+\beta x_0^2x_1x_2-x_0^3x_3,\\
 G&=x_2^4+\gamma x_1x_2x_3^2+c_4x_0x_3^3.
\end{aligned}
\]
These are homogeneous quartic intrinsic-torus eigenforms, of
weights 4 and 12. For \(A=x_1x_2\) and \(B=x_0x_3\),
\[
\begin{aligned}
 H_P(A,B)
 &=A^4+B^2(B-\beta A)(\gamma A+c_4B)\\
 &=A^4+c_2A^2B^2+c_3AB^3+c_4B^4\\
 &=x_2^4F+x_0^2(B-\beta A)G .
\end{aligned}
\]
The first expansion uses
\(-\beta\gamma=c_2\) and \(\gamma-\beta c_4=c_3\).
The final equation is an **actual Koszul membership identity**.

On the dense torus \([1:r:ur^3:vr^4]\), the two equations give
\(v=1+\beta u\) and \(u^4+\gamma u v^2+c_4v^3=0\).
With \(q=u/v\), these are equivalent to
\[
 v=\frac1{1-\beta q},\qquad
 u=\frac q{1-\beta q},\qquad P(q)=0 .
\]
Every root of \(P\) is nonzero by \(c_4\ne0\), and no root
satisfies \(1-\beta q=0\), because the displayed expansion then
gives \(P(q)=q^4\ne0\). Thus every root corresponds to exactly
one legitimate translated quartic, with local transverse length
equal to its root multiplicity. The pair misses
\(L_{12}=V(x_0,x_3)\), since its restrictions are
\(x_1^4,x_2^4\); hence it is a proper CI. Its four full-support
quartics counted with multiplicity already have degree 16,
exhausting Bézout and excluding residual components. Therefore
\[
 \pi_q(R_{4,4}^{\rm inv})=\mathcal P_4
\]
for **every algebraically closed characteristic**, where
\(\pi_q\) is the quadric-spectrum projection. In characteristic
zero, the previously proved full (4,4) moment theorem also gives
\(\pi_q(R_{4,4})=\mathcal P_4\).

**Multiplicity strata in characteristic zero.** All partitions of
four except (4) occur. Examples are
\[
\begin{array}{c|c}
(1,1,1,1)&T^4-1\\
(2,1,1)&(T-1)^2(T^2+2T+3)\\
(2,2)&(T^2-1)^2\\
(3,1)&(T-1)^3(T+3).
\end{array}
\]
The excluded (4) would have \(M_1=4q\ne0\).
The dimensions of the corresponding root loci in
\(\mathcal P_4\simeq\mathbb A^2\times\mathbb G_m\)
are respectively \(3,2,1,1\).

**Multiplicity strata in characteristic two.** Here
\(P'(T)=c_3\). If \(c_3\ne0\), all four roots are distinct.
If \(c_3=0\), then
\[
 P=(T^2+\sqrt{c_2}T+\sqrt{c_4})^2.
\]
For \(c_2\ne0\) there are two distinct double roots, while
\(c_2=0\) gives one quadruple root. Thus precisely
\((1,1,1,1),(2,2),(4)\) occur among centered quartics,
all actually realizable by the same invariant CI construction.
They have strata dimensions \(3,2,1\), respectively.
Examples are \(T^4+T+1,\ (T^2+T+1)^2,\ (T-1)^4\).
The characteristic-two discriminant is \(c_3^4\), so the
nonreduced discriminant divisor has support \(c_3=0\).
This differs substantially from the characteristic-zero
collision stratification; the quadruple-root locus occurs because
\(4q=0\) in characteristic two.

**Why the projection loses geometry.** The exceptional non-invariant
cycle from §10 has two doubled q-values \(1,-1\), giving
\(P=(T^2-1)^2\). The universal invariant construction also realizes
that same spectral polynomial: \(c_2=-2,c_3=0,c_4=1\),
so choose \(\beta^2=2\) in characteristic zero. Its corresponding
curve parameters are
\[
 (u_q,v_q)=
 \big(q/(1-\beta q),\,1/(1-\beta q)\big),\quad q=\pm1,
\]
and have *different* \(u_q\), whereas the exceptional cycle has
both \(u=1\). The equal quadric-spectrum polynomials conceal
genuinely different realization components. Consequently the
quadric spectrum and its discriminant alone cannot detect all
CI restrictions, even though they classify the possible
numbers of distinct q-roots at (3,4) and (4,4).

**Higher degrees are different.** Fixing the quartic carrier of
[fixed-carrier arrangements](fixed_carrier_chow_arrangements.md)
imposes gaps \(e_1=e_2=e_5=0\) when the indices occur; varying the
(4,4) carrier above removes the extra \(e_2\) obstruction via
the quadratic equation for \(\beta\). No corresponding
surjectivity theorem is claimed for general \(m\) or general
bidegree (a,b). Investigate whether the available carrier
parameters suffice to eliminate higher missing-coefficient
conditions before adding general low-degree casework.
