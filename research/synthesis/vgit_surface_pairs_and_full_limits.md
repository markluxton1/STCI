# VGIT of surface pairs, residual cycles, and full intersection limits

**Status:** reviewed provisional geometric framework, all-degree deductions
and bounded controls; independent review is recorded below. No canonical
result is promoted. Fix
\(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), ordinarily in
characteristic zero, and \(S=k[x_0,x_1,x_2,x_3]\), \(I=I_C\).
The power-containment lemma below works in every characteristic. The question
includes **all proper containing intersections**, with cycle
\([Y]=m[C]+R\), before imposing sole support.

The general organizing objects are the [closed residual-degree filtration
and exact generator incidence](residual_cycles_and_chow_incidence.md) and
the [invariant residual arrangements](torus_residual_arrangements_and_absorption.md).
The all-degree semistability argument below restricts every actual supported
pair to a single natural torus linearization. The intrinsic boundedness proof
and the graph then retain its full embedded limits. The sextic weight counts
and residual examples are bounded controls; they do not select the scope of
the problem or introduce a canonical theorem. The
[opposite-limit framework](torus_attracting_strata_and_generator_incidence.md)
still owns the general moving-ideal generator question.

## 1. Choose the group and the parameter space

Put \(V_d=H^0(\mathbf P^3,\mathcal I_C(d))=I_d\). The fixed curve is
preserved by the one-dimensional torus with ring action
\[
\lambda(t)x_i=t^{w_i}x_i,\qquad (w_0,w_1,w_2,w_3)=(0,1,3,4).
\]
We apply this action to ideals. Centered weights \((-2,-1,1,2)\) give the
same action on homogeneous projective objects. In degree d the centered
weight is the uncentered weight minus 2d. This fixes both the sign and which
limit is called positive: t tending to zero selects minimum ring weights.

For equal degrees use
\[
X_d=\operatorname{Gr}(2,V_d),\qquad
U_d=\{W\in X_d:\operatorname{ht}(W)=2\}.
\]
A point is a pencil, independent of its chosen basis. For W in U_d, its
ideal (W) is a proper saturated complete intersection. Reducible carriers
and residual curves are allowed. Smoothness is not part of U_d. An ordered
product of projective equation spaces repeats the same ideal under basis
changes and supplies presentation-dependent linearizations.

For a<b the analogous presentation space is the projective bundle of lines
in E over \(\mathbf P(V_a)\), where
\[
0\longrightarrow\mathcal O(-1)\otimes S_{b-a}
 \xrightarrow{\ F\cdot\ }V_b\otimes\mathcal O
 \longrightarrow E\longrightarrow0.
\]
Its fiber is \(\mathbf P(V_b/(F S_{b-a}))\). Multiplication by a nonzero
polynomial is injective, so E is locally free. **All ambient multipliers**
\(S_{b-a}\) must be divided out, not just equations vanishing on C. Take
the open subset where a representative pair is a regular sequence.

The full group SL4 does not preserve V_d for this fixed C. There are two
useful VGIT versions, with different meanings:

* On X_d, use the preserving torus T and vary the character of the Plucker
  linearization. This gives a complete finite coarse numerical decomposition
  for a fixed d. Equal-degree pencils have one Plucker polarization; a
  separate weighting of the two chosen basis vectors does not descend.
* To use SL4 and a slope between a curve and a pair, let K be the projective
  orbit closure of [C] in \(\operatorname{Hilb}^{4n+1}(\mathbf P^3)\).
  Use the marked incidence of \((C',W)\in K\times\operatorname{Gr}(2,S_d)\)
  with \(C'\subset V(W)\). Positive tensor products of a Hilbert
  polarization on K and the Plucker polarization are ample linearizations.
  This is an SL4 problem with a moving marked curve; intersect its invariant
  loci with the fiber C'=C to investigate this embedding. Its walls and
  instability strata have not been computed here.

In either version keep the **unquotiented loci** when subsequently applying
T to embedded intersections. The same T acts trivially on its GIT quotient;
likewise a subgroup of SL4 acts trivially on the SL4 quotient. A quotient
alone cannot retain the orbit degeneration we want to study. VGIT chamber
membership, optimal-destabilization strata, and attracting sets for one
chosen T are distinct decompositions.

## 2. A uniform neighborhood for actual supported complete intersections

**Intrinsic lemma.** More generally, let C be any integral curve of degree
delta in projective three-space, and suppose \(J=(F_a,G_b)\) is a proper
homogeneous complete intersection with reduced projective support exactly C.
Then delta divides ab. Set m=ab/delta. In every characteristic,
\[
 I^{(m)}\subset J,\qquad\text{hence}\qquad I^m\subset J\subset I.       \tag{1}
\]
Here \(I^{(m)}=I^mS_I\cap S\) is the symbolic power.

**Proof.** The graded quotient S/J is Cohen--Macaulay of dimension two.
Thus J is saturated and unmixed. Sole reduced projective support, together
with saturation, gives \(\sqrt J=I\) for the affine homogeneous ideals as
well. Its only associated prime is I, so J is I-primary. The degree formula
for the fundamental cycle is
\[
 ab=\deg(S/J)=\delta\operatorname{length}_{S_I}(S_I/J_I)=\delta m.
\]
In an Artin local ring of length m, the m-th power of its maximal ideal is
zero: any equality of two successive powers forces that power to vanish by
Nakayama, and every nonzero successive quotient consumes positive length.
Consequently \(I^mS_I\subset J_I\). Primary contraction gives
\(J_I\cap S=J\), proving (1). No claim about singularity or normality of
the surfaces, separability, or a transverse normal form was used.

Whenever T preserves C, as for our fixed quartic, for each fixed (a,b)
every actual supported complete intersection and all its full T-limits
therefore lie in the **single closed supported locus**
\[
H_m=\{[Z]\in\operatorname{Hilb}^{P_{a,b}}:
       \mathcal I_C^m\subset\mathcal I_Z\subset\mathcal I_C\}.
\]
These are closed flag/Quot incidence conditions, so H_m is projective and
T-stable. The two containments persist in its flat limits. For the fixed
quartic delta=4; in particular, for (6,6),
\[
m=9,\qquad P_{6,6}(n)=36n-144.
\]
Thus an unspecified exponent N is **not** an additional coverage problem
for actual supported sextic CIs: H_9 covers them. This does not classify H_9,
its fixed components, or its attracting loci. It gives no single N for all
degree pairs, and makes no assertion that every ideal with the same Hilbert
polynomial is primary or lies in this neighborhood. The general bounded
framework permits other ideals and should retain that distinction.

## The Chow linearization covers supported pairs in every degree

**Theorem.** Use the centered SL4 lift with ring weights (-2,-1,1,2)
and its natural linearizations. In every characteristic, every proper
degree-(a,b) pair with reduced support C_0 is T-semistable at character
zero on \(\mathbf P(I_a)\times\mathbf P(I_b)\) for
\(\mathcal O(b,a)\). For a=b=d, every such pencil is semistable for the
Plucker polarization. In the extremal-weight convention of section 3,
\[
 \ell(W)\le 0\le u(W).                                             \tag{B}
\]

**Proof.** Write \(E_e=H^0(\operatorname{Gr}(2,4),O(e))\) and
\(Q=\operatorname{Ch}_{C_0}\in E_4\). Its line is T-invariant.
Coordinate reversal \(\iota=(03)(12)\) preserves C_0 by interchanging
s and t, belongs to SL4, and conjugates the centered torus to its inverse.
It also preserves the Q-line. Thus the character q of Q satisfies
q=-q in \(X^*(T)=\mathbf Z\), so q=0. This remains true in characteristic
two: the character lattice, rather than the ground field, is being used.

The [universal-line resultant](residual_cycles_and_chow_incidence.md#1-the-proper-pair-chow-morphism)
is an equivariant polynomial map
\(R:I_a\times I_b\to E_{ab}\), homogeneous of degrees (b,a).
The natural determinant target has no extra ambient character: the identity
\(\det\operatorname{Sym}^n\mathcal S^\vee
=(\det\mathcal S^\vee)^{n(n+1)/2}\) gives exponent ab for the Sylvester
target minus its sources. For a supported pair, 4 divides ab and
\(R_{F,G}=cQ^{ab/4}\), with c nonzero. Choose a weight-zero functional
\(L:E_{ab}\to k\) nonzero on this Chow power. The section L(R) of
\(\mathcal O(b,a)\) is invariant and nonzero at the pair. It proves
semistability for that ample linearization.

For equal degrees, a change of pencil basis by a matrix A gives
\(R_{A(F,G)}=\det(A)^dR_{F,G}\). This polynomial identity follows from
diagonal changes, shears and interchange of the two binary forms, so holds
over every field. Consequently R descends on the whole Grassmannian as a
section of \(E_{d^2}\otimes(\det\mathcal W^\vee)^d
=E_{d^2}\otimes O_{X_d}(d)\), where \(\mathcal W\) is its tautological
two-plane bundle. L(R) is an invariant section of that positive Plucker
power. The torus criterion gives (B). QED.

This covers **all degrees and all actual supported pairs**, with no
eigenform, carrier or transverse-quotient hypothesis. It removes wholly
one-sided centered weight blocks from the supported proper-pair search.
Semistability is not a sufficient support condition; residual pairs can be
semistable too. The character-zero locus already covers the supported
search, so a sweep of every VGIT chamber is unnecessary for that coverage.
Other characters can still organize residual intersections. Character zero
refers to the specified centered lift; an uncentered lift translates the
linearization character.

The assertion concerns the moving proper pair. Its limiting equation pencil
can be improper and unstable: the resultant section vanishes at the
common-factor boundary even when the full Hilbert limit stays supported.
Thus (B) does not require each fixed endpoint pencil to have weight zero.
Graph limits remain essential.

**Strictness using the reviewed eigenform theorem.** In characteristic
zero, every actual supported ordered pair is T-stable for O(b,a), and
every actual supported equal-degree pencil satisfies
\[
 \ell(W)<0<u(W).                                                   \tag{B'}
\]
The same conclusions hold in characteristic p when p does not divide ab
(d squared for equal-degree pencils). These strengthened statements use
the independently reviewed provisional
[eigenform obstruction](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md#the-bound-and-its-exact-large-prime-minimum)
in addition to the intrinsic Chow argument.

To prove the ordered-pair statement, let alpha and beta be the minimum
centered weights of F and G. The minimum O(b,a) state weight is
b alpha+a beta. If it is zero, the rescaled equation vectors
\(t^{-\alpha}\lambda(t)F\) and \(t^{-\beta}\lambda(t)G\) have nonzero
limits F_min and G_min, each an eigenform. Their **full** resultant is
\[
 t^{-(b\alpha+a\beta)}\lambda(t)R_{F,G}=R_{F,G}=cQ^{ab/4}.
\]
It remains nonzero at the limit, so the limiting eigenform pair is
proper and supported on C_0. This contradicts the cited theorem in
characteristic zero or p not dividing ab. The maximum-weight equality
is excluded by the inverse torus. Thus both inequalities are strict;
the stabilizer is finite, giving stability for the one-dimensional torus.
For pencils, if ell=0 the affine Plucker cone has a nonzero weight-zero
limit. The degree-d resultant section on that cone keeps its same nonzero
invariant value, giving the same contradiction; u=0 is handled oppositely.
No extension of the section to the whole exterior-power vector space is
needed. When p divides ab, the eigenform theorem does not yield this
strictness claim.

There is also a useful global simplification for a fixed degree pair:
the entire supported proper-pair locus, or supported proper-pencil locus
in equal degree, is [closed in one affine resultant chart](residual_cycles_and_chow_incidence.md#a-single-affine-chart-for-the-whole-supported-pair-locus).
For C_0 that chart is T-invariant. This removes improper pairs from the
working chart; it does not compactify the locus or decide nonemptiness.
The arbitrary-degree invariant boundary still belongs to the full graph.

## 3. Complete coarse VGIT data for sextic pencils

For W in X_d, write its Plucker vector as
\(p(W)=\sum p_r\) in the weight decomposition of \(\bigwedge^2 V_d\).
Define
\[
\ell(W)=\min\{r:p_r\ne0\},\qquad
u(W)=\max\{r:p_r\ne0\}.
\]
Define the character parameter theta so that the shifted Plucker-vector
weights for \(\mathcal O(q)\) are qr-k, with theta=k/q. This specifies the
linearization convention without a dual-line sign ambiguity. The torus
criterion gives exactly
\[
 W\text{ is theta-semistable}\iff\ell(W)\le\theta\le u(W),             \tag{2}
\]
and stability is the strict-inequality case. A nondegenerate interval gives
a finite stabilizer; a one-weight point is fixed and strictly semistable at
that weight. This is the projective ample criterion, not an assertion for
arbitrary nonample bundles on other compactifications.

The loci \(X_{\ell,u}\) are locally closed: all weight blocks outside
[ell,u] vanish, and the two extreme blocks are nonzero. They form a finite
partition of **all** X_d, including the points unstable at theta=0.
Restricting to U_d retains a partition of all proper pencils. It does not
assert that an invariant open U_d is a saturated open for every good
quotient, or that its restricted quotient has already been constructed.

For d=6, the restriction of a monomial of uncentered weight r is the same
binary monomial \(s^{24-r}t^r\). If n_r counts degree-six monomials of
weight r, then \(\dim V_{6,r}=n_r-1\). All weights 0,...,24 occur in S_6.
The nonzero kernel dimensions are:

| Uncentered weights | Dimensions, in order |
| --- | --- |
| 3,...,12 | 1,2,2,3,3,4,4,4,4,5 |
| 13,...,21 | 4,4,4,4,3,3,2,2,1 |

Hence \(\dim V_6=59\) and \(\dim X_6=114\). The actual Plucker weights
fill 7,...,41, or **-17,...,17 in centered coordinates**. This follows
by taking sums of two weights, allowing repetition only when that weight
space has dimension at least two. Every such weight is realized by an
eigenvector two-plane, so these are the ambient candidate character walls, with 34
open chambers between successive weights. Properness and support may remove
wall loci. Outside [-17,17] the ambient semistable locus is empty.
There are at most \(35\cdot36/2=630\) extremal-weight blocks,
including potentially empty blocks; they are not 630 classified geometric
families of intersections. One representative theta per chamber and wall
covers the effective character interval, and their semistable loci together
cover X_6. For actual supported pencils, the all-degree theorem above
already restricts the search to blocks with ell<=0<=u. The remaining
characters need not be swept to obtain supported-pair coverage.

The [exact certificate](../computations/verify_vgit_surface_pairs.py)
enumerates these weights. The geometric reason for the kernel calculation
is restriction to the marked curve, rather than an unrelated monomial count.

## 4. Retain the intersection: the graph and its two polarizations

There is a T-equivariant morphism
\[
f:U_d\longrightarrow\operatorname{Hilb}^{P_{d,d}}(\mathbf P^3),
\qquad W\longmapsto V(W).
\]
The universal regular sequence has constant complete-intersection Hilbert
function and defines a flat family. Set
\[
\Gamma_d=\overline{\operatorname{graph}(f)}
 \subset X_d\times\operatorname{Hilb}^{P_{d,d}}.
\]
This is a projective equivariant graph closure, not an asserted smooth
resolution. A point (W_0,J_0) keeps both the limiting pencil and the full
saturated ideal of the intersection limit. Universal equation incidence is
closed, so \((W_0)\subset J_0\).

**Proper-limit lemma.** If W_0 is proper, then J_0=(W_0). Indeed both
schemes have P_{d,d}; their inclusion gives a coherent quotient of Hilbert
polynomial zero, which must be zero. Saturation turns equality of sheaves
into equality of these homogeneous ideals. Therefore an extra-generator
limit lies over the common-factor boundary of X_d. The gcd degree is a
useful first refinement, but it does not determine J_0 or its support.

The same argument gives a stronger intrinsic test on the whole Hilbert
scheme with the exact polynomial P_{a,b}: a proper prescribed-degree pair
inside a saturated J already generates J. Equivalently, for a<=b it is
enough that J_a be nonzero and the degree-b equation system have no fixed
hypersurface component. The [general proof](residual_cycles_and_chow_incidence.md#3-exact-generator-incidence-at-the-complete-intersection-polynomial)
replaces a separate higher-degree generator calculation on this locus.
Existence of two independent equations with a common factor is insufficient.

For the sole-support sector take the closure of the graph over
\(U_d\cap f^{-1}(H_{d^2/4})\) inside \(X_d\times H_{d^2/4}\), when
4 divides d^2. Call this \(\Gamma_d^{\mathrm{supp}}\). This choice keeps
the approximating intersections supported; merely intersecting the closure
of *all* CIs with the supported Hilbert locus is a potentially larger space.
All supported pencils and both their full limits occur here. In
characteristic zero the existing reviewed provisional
[eigenform theorem](../supplements/EQUIVARIANT_DEGREE_BOUNDS.md) implies
that neither limiting pencil can remain proper: otherwise its supported
full limit would itself be an invariant CI with eigenform generators.
This observation inherits that theorem's authority and does not exclude
the moving pencil.

Fix one sufficiently high Hilbert embedding degree n for the entire
projective graph, and let L_n be its Hilbert Plucker polarization. On Gamma use
\[
A=\pi_X^*\mathcal O_{X_d}(1),\qquad B=\pi_H^*L_n,
\qquad A^r\otimes B^s\quad(r,s>0),
\]
with a character twist. These products are ample by the product embedding.
The pullback A alone need not be ample on graph fibers. If the degree-n
ideal Plucker weights of J have extrema ell_H,u_H, then the product state
interval is exactly
\[
[r\ell(W)+s\ell_H(J),\;ru(W)+su_H(J)].                              \tag{3}
\]
This follows from the Segre--Veronese state support being the Minkowski sum.
Thus the graph supplies a slope between **pair data and full intersection
data even in equal degrees**. Its actual wall fan and graph fibers remain
to be determined. Formula (3) is a valid finite numerical organizing test,
not a precomputed list of the graph's nonempty strata.

Refine a numerical block upstairs by both full fixed limits, endpoint gcds,
graded minimal-generator modules, and normal/endpoint structures. Fixed
components can have positive dimension. No affine-cell structure or finite
list of fixed ideals is claimed. The two torus limits in the Hilbert scheme
remain different from the two geometric endpoints of a finite transverse
modification.

## 5. A residual control detects the difference between the two polarizations

Reuse the independently reviewed provisional
[degree-ten-generator example](toric_sextic_residuals_and_limits.md):
\[
q=x_0x_3-x_1x_2,\quad A_3=x_0^2x_2-x_1^3,\quad
a_6=x_0^2x_3A_3,\quad b_4=x_0^3x_2,
\qquad W=\langle q^3+a_6,b_4q\rangle.                               \tag{4}
\]
It is proper because q does not divide a_6, and neither x0 nor x2 divides
q^3+a_6. The centered weights of q,a_6,b_4 are 0,-5,-5. Thus its two
Plucker blocks have weights -10 and -5, and (2) says
\[
W\text{ is theta-semistable exactly for }-10\le\theta\le-5.
\]
In particular theta=0 instability does not invalidate this actual containing
intersection. The two limiting pencils are
\[
 W_+=\langle a_6,b_4q\rangle\quad(t\to0),\qquad
 W_-=\langle q^3,b_4q\rangle\quad(t\to\infty).
\]
Their gcds are x0^2 and q respectively. At the negative-direction endpoint,
the full ideal is
\[
J_-=(q^3,b_4q,a_6b_4),
\]
as proved by the flat Hilbert--Burch family
\((q^3+h^5a_6,b_4q,a_6b_4)\). The degree-ten generator retains the
cancellation relation lost by just taking W_-. The total Hilbert polynomial
is 36n-144. The original and limiting cycles have generic multiplicity one
along C and residual degree 32. This is outside H_9 and outside the
sole-supported graph. Its role is to verify how the construction handles
actual residual intersections and generator jumps.

One can measure the lost information intrinsically by the character of
\(\det(J_-)_n\). Put \(N_j=\binom{j+3}{3}\) for j>=0 and zero otherwise.
The generators have (degree,centered weight)
\((6,0),(6,-5),(10,-10)\); the two Hilbert--Burch syzygies have
\((10,-5),(12,-10)\). Since the total centered weight of S_j is zero,
\[
\operatorname{wt}\det(J_-)_n
=-5N_{n-6}-5N_{n-10}+10N_{n-12}.                                    \tag{5}
\]
The Koszul sequence over the proper-pencil locus gives the pair coefficient
\(D_n=N_{n-6}-N_{n-12}\): up to weight-zero constant lines,
\(\det J_n\simeq(\det W)^{D_n}\). Evaluating that *pair-side extension*
at W_- would give -5D_n. The actual difference is
\[
\operatorname{wt}\det(J_-)_n-(-5D_n)
=-5(N_{n-10}-N_{n-12}).                                             \tag{6}
\]
At n=12 these values are **-460 versus -415**, a correction of -45.
The correction records the failure of the multiplication map at the
common-factor pencil, equivalently the generator/syzygy data in the full
limit. Equal Hilbert polynomials do not identify these linearizations across
the graph boundary.

There is an independent finite check: build the actual spaces
\(J_n=(q^3+a_6)S_{n-6}+(b_4q)S_{n-6}\). Minimum and maximum weight bases
of their monomial column matroids give their extreme Plucker weights:

| n | dim J_n | Minimum | Maximum |
| --- | --- | --- | --- |
| 6 | 2 | -10 | -5 |
| 10 | 70 | -345 | -180 |
| 12 | 167 | -780 | -460 |
| 13 | 236 | -1065 | -660 |

Exact rational row reduction verifies (5) at the maximum endpoint and gives
these opposite-direction degreewise invariants. This does **not** claim
that these four graded pieces reconstruct the full positive limit, determine
its embedded points, or furnish a global Hilbert embedding for the entire
Hilbert scheme at n=12. For n sufficiently high the same determinant formula
is a Hilbert-point weight. A large uniform Hilbert embedding must be chosen
before using (3) on the whole graph.

### One coarse block already contains different intersection strata

There is an actual one-parameter pilot, rather than just one isolated control.
Keep q,A_3,a_6,b_4 from (4), and put
\[
a_\tau=a_6+\tau qx_0A_3
 =x_0A_3\big((1+\tau)x_0x_3-\tau x_1x_2\big),\qquad
W_\tau=\langle q^3+a_\tau,b_4q\rangle.                              \tag{7}
\]
Every finite tau gives a proper CI: q does not divide a_tau because its
class modulo q equals a_6, and neither x0 nor x2 divides q^3+a_tau. These
regular sequences give a flat family of actual intersections. At the generic
point of C, b_4 and x0^2*x3 are units, so its localized ideal is (q,A_3).
Thus every member has generic multiplicity one along C and residual degree
32. This is a family of containing intersections, not supported candidates.

All pencils have the same Plucker interval [-10,-5]. All their full
negative-direction ideals are also the **same** ideal J_-, since
\[
(a_\tau-a_6)b_4=\tau x_0A_3(b_4q).
\]
The Hilbert--Burch proof applies to each member. Nevertheless the positive
limiting pencils \(\langle a_\tau,b_4q\rangle\) have gcd
\[
\begin{cases}
x_0^2,&\tau=0,\\
x_0x_2,&\tau=-1,\\
x_0,&\tau\ne0,-1.
\end{cases}                                                        \tag{8}
\]
This follows from the displayed factorization and the coprimality of A_3
with x0,x2,q. Hence even within one coarse VGIT block and one specified
negative full-limit attracting set, the opposite pencil geometry changes.

In characteristic zero, the full degree-12 state distinguishes two of these
members as well:
\[
\tau=0:\ [-780,-460],\qquad \tau=1:\ [-810,-460].                    \tag{9}
\]
These are exact rational computations on actual equation spaces, not a
generic-rank extrapolation. In characteristic two, tau=1 equals -1 and this
particular numerical contrast is not asserted. No formula for every tau or
full positive ideal is inferred. At degree 12, (3) consequently has lower endpoint
-10r-780s for tau=0 and -10r-810s for tau=1, with the same upper endpoint
-5r-460s. This is a numerical distinction for the two-factor degree-12
Grassmannian model on this family. Its extension to the whole projective
graph uses a sufficiently high uniform Hilbert degree as above. The pilot
shows concretely why the desired geometric analysis requires refinements
after the initial surface-pair VGIT partition.

## 6. Literature guidance and the next geometric strata

[Dolgachev--Hu, section 1.1.5](https://www.numdam.org/item/PMIHES_1998__87__5_0.pdf)
gives the torus state-polytope criterion behind (2). Their general variation
results, and [Thaddeus](https://arxiv.org/abs/alg-geom/9405004), guide quotient
changes; flip descriptions need their own hypotheses. Neither classifies
our support or generator incidence. The explicit weight-block argument
above establishes the asserted finite coarse partition without importing
smooth attracting-cell conclusions.

The closest worked surface-pair model is
[Casalaina-Martin--Jensen--Laza](https://www.ms.uky.edu/~dhje223/Published_Papers/Genus4.pdf),
sections 1.1--1.4 and 6. They compare quadric--cubic parameter spaces with
Hilbert models using a resolution and distinguish nonample numerical tests
from GIT until justified. The transferable method is the **comparison of
polarizations on a common modification**; their genus-four SL4 stability
classification supplies no sextic or fixed-C theorem here.

[Benoist's 2026 paper](https://arxiv.org/html/2601.11474v1), sections 1.3,
1.6, and 4, supplies a second model: quotient higher equations by lower
multiples, stratify the common-factor boundary, and compare with a
multigraded Hilbert compactification. Its completed MMP concerns two
variables. The higher-dimensional questions are explicitly separated.
It supersedes [the 2012 preprint](https://arxiv.org/abs/1212.4862); do not
silently import the old preprint's broad framing as a completed P3 program.

A continuation aimed at the general problem can use the following objects
for **any degree pair**, keeping sextics as controls rather than a reduction:

1. Organize all proper containing pairs by the closed Chow-divisibility
   filtration \(m_C\ge r\). For supported pairs use the single affine
   resultant chart and the centered character-zero locus, stable in
   characteristic zero; other characters may help study
   residual geometry without being needed for supported coverage.
2. Retain equations, full Hilbert ideals and Chow cycles on the
   [triple graph](residual_cycles_and_chow_incidence.md#4-full-graph-limits-and-the-top-cycle-fiber).
   Both full T-limits exist. Their reduced curve components have the
   [orbit-closure classification](torus_residual_arrangements_and_absorption.md#2-all-invariant-irreducible-curves-are-explicit-orbit-closures),
   including the possible middle coordinate line linked through residual
   chains. Classify nonreduced structures only with their full relations.
3. In the top Chow fiber, connectedness forces the Hilbert coordinate
   to have reduced support C in characteristic zero. The decisive
   incidence is whether it meets the open type-(a,b) CI locus. Test a
   degree-a section and absence of a fixed surface in degree b; the full
   prescribed Hilbert polynomial then supplies ideal equality.
4. Distinguish residual-cycle motion from embedded, fixed-polynomial
   deformation and actual equations. Invariant full-support quartics
   move to C at cycle level, but that does not lift the whole intersection.
   A stratum exclusion requires coverage of its moving ideals; an
   unrestricted exclusion still needs coverage over unbounded degrees.

Completed here and in the two linked proof homes: an all-degree centered
semistability condition, a closed residual-degree filtration, exact
two-degree generator incidence, a general invariant-support classification
and its attachment counterexample, an intrinsic fixed-degree bound, a complete
coarse torus-VGIT partition of the pencil space, a graph comparison, an
exact nonzero boundary-character correction, and a one-parameter residual
family requiring opposite-limit refinements within one coarse block.
Not completed: the nonempty
supported graph strata, their full fixed-ideal classification or fibers, the
refined wall fan, or any supported CI existence/exclusion. The unrestricted
characteristic-zero STCI question remains open.

## Evidence and independent review

The written arguments prove the primary-power and proper-limit lemmas.
The finite certificate
`python3 research/computations/verify_vgit_surface_pairs.py` checks the
restriction-weight count, ambient Plucker weights, exact degreewise state
extrema of (4), and comparison with its equivariant Hilbert--Burch character.
The existing
`python3 research/computations/verify_toric_quotients_and_residual_limits.py`
checks the inherited polynomial/minor identities. Neither script certifies
an exhaustive supported-stratum computation. Flatness, saturation, and the
residual cycles of (4) use the written proof in the linked existing chapter.

Independent reconstruction on 2026-11-01 accepted the primary-power lemma,
proper-limit lemma, coarse weight partition, graph polarizations, and
character comparison with their literal scopes. It separately checked the
one-parameter pilot's properness, generic length, constant negative full
ideal and varying positive gcds. The review required the explicit
characteristic-zero qualification for (9). A separate certificate review
reconstructed the greedy column-matroid argument and the degree-12 character
from the syzygies, and reran both verifiers. The mathematical reviewer also
recomputed (9) independently. Neither review asserts literature priority,
canonical promotion, or supported-stratum classification. No canonical
result or question record is changed by this proposal.

A further independent reconstruction on 2026-11-01 accepted the centered
semistability theorem in every characteristic, including the integral
GL2 covariance, the specified SL4 lift, and the weight-zero Chow line.
It also reviewed the general-degree primary-power statement and the two
new linked geometric proof homes. The character-zero assertion concerns
proper moving pairs, not their potentially improper equation endpoints.
A bounded independent reconstruction additionally accepted the affine
resultant chart and the strict-stability corollary in characteristic zero
or p not dividing ab. The strict corollary uses the full resultant at
the endpoint and inherits the eigenform theorem's reviewed provisional
authority; no sufficient support criterion is asserted. These contributions
remain reviewed provisional deductions without canonical promotion.
