# VGIT of surface pencils and full intersection limits

**Status:** proposed geometric framework and exact bounded deductions, with
independent review recorded below; not promoted to canonical results. Fix
\(C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k\), ordinarily in
characteristic zero, and \(S=k[x_0,x_1,x_2,x_3]\), \(I=I_C\).
The power-containment lemma below works in every characteristic. The question
includes **all proper containing intersections**, with cycle
\([Y]=m[C]+R\), before imposing sole support.

The contribution is an intrinsic boundedness proof, a geometric graph
construction relating equation VGIT to full ideals, and a necessary exact
weight calculation on an existing residual example. It replaces no existing
calculation or canonical theorem. The
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

**Intrinsic lemma.** Suppose \(J=(F_a,G_b)\) is a proper homogeneous complete
intersection with reduced projective support exactly the integral quartic C.
Then 4 divides ab. Set m=ab/4. In every characteristic,
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
 ab=\deg(S/J)=4\operatorname{length}_{S_I}(S_I/J_I)=4m.
\]
In an Artin local ring of length m, the m-th power of its maximal ideal is
zero: any equality of two successive powers forces that power to vanish by
Nakayama, and every nonzero successive quotient consumes positive length.
Consequently \(I^mS_I\subset J_I\). Primary contraction gives
\(J_I\cap S=J\), proving (1). No claim about singularity or normality of
the surfaces, separability, or a transverse normal form was used.

For each fixed (a,b), every actual supported complete intersection and all
its full T-limits therefore lie in the **single closed supported locus**
\[
H_m=\{[Z]\in\operatorname{Hilb}^{P_{a,b}}:
       \mathcal I_C^m\subset\mathcal I_Z\subset\mathcal I_C\}.
\]
These are closed flag/Quot incidence conditions, so H_m is projective and
T-stable. The two containments persist in its flat limits. For (6,6),
\[
m=9,\qquad P_{6,6}(n)=36n-144.
\]
Thus an unspecified exponent N is **not** an additional coverage problem
for actual supported sextic CIs: H_9 covers them. This does not classify H_9,
its fixed components, or its attracting loci. It gives no single N for all
degree pairs, and makes no assertion that every ideal with the same Hilbert
polynomial is primary or lies in this neighborhood. The general bounded
framework permits other ideals and should retain that distinction.

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
eigenvector two-plane, so these are the ambient character walls, with 34
open chambers between successive weights. Properness and support may remove
wall loci. Outside [-17,17] the ambient semistable locus is empty.
There are at most \(35\cdot36/2=630\) extremal-weight blocks,
including potentially empty blocks; they are not 630 classified geometric
families of intersections. One representative theta per chamber and wall
covers the effective character interval, and their semistable loci together
cover X_6.

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

Let L_n be a sufficiently high Hilbert Plucker polarization. On Gamma use
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

A next bounded study can now start from geometric strata rather than
selected smoothings:

1. On X_6 use the complete extremal-weight partition, then refine by the
   gcds of **both** limiting pencils. For the supported characteristic-zero
   sector these gcds must be nonconstant by the scoped eigenform theorem.
2. Above a chosen boundary locus, describe the graph fiber using the
   multiplication maps \(W\otimes S_{n-6}\to S_n\), their rank drops,
   cancellation relations, and the full saturated limiting ideal. The
   degree-ten example supplies an exact residual control for this step.
3. Intersect with the supported graph in X_6 times H_9, retaining both
   endpoints and full relations. Determine actual graph-fiber incidence;
   a formal determinantal rank condition without its realizations does not
   finish this calculation.
4. On the resulting loci test the moving ideal's generator module
   \(J/S_+J\). An actual sole-supported proper sextic pencil would already
   generate a CI; an abstract supported Hilbert point still needs that
   generation incidence. Compare normal and endpoint invariants only through
   stated maps, and retain embedded structure instead of taking a pure hull.

Completed here: an intrinsic fixed-degree neighborhood bound, a complete
coarse torus-VGIT partition of the pencil space, a graph comparison, an
exact nonzero boundary-character correction, and a one-parameter residual
family requiring opposite-limit refinements within one coarse block.
Not completed: the nonempty
supported graph strata, their full fixed-ideal classification or fibers, the
refined wall fan, or any supported CI existence/exclusion. The unrestricted
characteristic-zero STCI question remains open.

## 7. Common-factor rank-drop law, prime-ideal boundary dichotomy, and the double-sextic sub-Grassmannian

*(Authored by Gemini on `evaluate_toric_integration_stci`; independently reviewed by Gemini subagent and verified in `verify_vgit_surface_pairs.py`.)*

We now execute steps 1 and 2 of the bounded program above by establishing the exact multiplication-map rank drop across the common-factor boundary \(\Delta_d^{\mathrm{cf}} = X_d \setminus U_d\), classifying the boundary dichotomy forced by \(J_0 \subset I_C\) on \(\Gamma_6^{\mathrm{supp}}\), and determining the intrinsic \(T\)-weight structure of the double-surface spaces \(V_{d,2} = H^0(\mathcal I_C^2(d))\) and the double-sextic sub-Grassmannian \(\operatorname{Gr}(2, V_{6,2}) \subset X_6\).

### 7.1 Universal rank-drop and degreewise cancellation-degree lemma on \(\Gamma_d\)

Stratify the non-proper boundary \(\Delta_d^{\mathrm{cf}} = X_d \setminus U_d\) by the common-factor degree \(e = \deg \gcd(W_0) \in \{1, \dots, d-1\}\):
\[
  \Delta_d^{\mathrm{cf}}(e) := \bigl\{[W_0] \in X_d : \deg \gcd(W_0) = e\bigr\}.
\]
Every \(W_0 \in \Delta_d^{\mathrm{cf}}(e)\) factors uniquely up to scalars as \(W_0 = D_e \cdot W'_{d-e}\), where \(D_e = \gcd(W_0) \in S_e\) and \(W'_{d-e} = \langle A_{d-e}, B_{d-e} \rangle \in \operatorname{Gr}(2, S_{d-e})\) is a coprime pencil (\(\gcd(A_{d-e}, B_{d-e}) = 1\)).

**Lemma (Common-factor rank drop and first degreewise cancellation degree).** Let \([W_0] \in \Delta_d^{\mathrm{cf}}(e)\) with \(1 \le e \le d-1\), and let \(H_{\mathrm{CI}(d,d)}(n) = 2 N_{n-d} - N_{n-2d}\) be the Hilbert function of a proper \((d,d)\) complete intersection in \(\mathbf P^3\).
1. *(Exact syzygy and rank drop in all characteristics:)* Because \(A_{d-e}, B_{d-e}\) form a regular sequence in \(S\), the kernel of the multiplication map \(\mu_n(W_0): W_0 \otimes S_{n-d} \to S_n\) is a free \(S\)-module of rank \(1\) generated in degree \(2d - e\) by the cancelled Koszul syzygy \((B_{d-e}, -A_{d-e})\). Hence for every \(n \ge 0\),
   \[
     \dim(W_0)_n = 2 N_{n-d} - N_{n - 2d + e}, \qquad
     \Delta\operatorname{rank}_n(e) := H_{\mathrm{CI}(d,d)}(n) - \dim(W_0)_n = N_{n - 2d + e} - N_{n - 2d}. \tag{10}
   \]
2. *(Degreewise Grassmannian limit and cancellation class:)* For any one-parameter family \(W_\tau \in U_d\) converging to \((W_0, J_0) \in \Gamma_d\), let \(L_n := \lim_{\tau\to 0} (W_\tau)_n \in \operatorname{Gr}(H_{\mathrm{CI}(d,d)}(n), S_n)\) be the degreewise limit subspace. Since \((W_0)_n \subset L_n \subset (J_0)_n\):
   - For all \(n < 2d - e\), \(\dim(W_0)_n = 2 N_{n-d} = \dim L_n\), so \(L_n = (W_0)_n\).
   - At \(n = 2d - e\), \(\dim L_{2d-e} - \dim(W_0)_{2d-e} = N_0 - N_{-e} = 1\), so \(L_{2d-e}\) contains a unique projective cancellation line \([G_{2d-e}] \in \mathbf P\bigl(S_{2d-e}/(W_0)_{2d-e}\bigr)\). If \(W_\tau = \langle D_e A_{d-e} + \tau^k \tilde F_d + O(\tau^{k+1}),\, D_e B_{d-e} + \tau^k \tilde G_d + O(\tau^{k+1})\rangle\) with \(B_{d-e}\tilde F_d - A_{d-e}\tilde G_d \notin (W_0)_{2d-e}\), then \(G_{2d-e} = B_{d-e}\tilde F_d - A_{d-e}\tilde G_d\) spans \(L_{2d-e}/(W_0)_{2d-e}\).
   - Because \(J_0\) is the saturation of \(L = \bigoplus_{n\ge 0} L_n\), \(\dim\bigl((J_0)_n/(W_0)_n\bigr) \ge N_{n-2d+e} - N_{n-2d}\) for all \(n \ge 0\), with equality for all \(n \gg 0\) (and equality for all \(n \ge 0\) whenever \(J_0\) is arithmetically Cohen–Macaulay, in which case the first extra minimal generator of \(J_0\) modulo \((W_0)\) occurs in degree **\(2d - e\)**).

Formula (10) explains conceptually why the residual control (4) (where \(W_- = \langle q^3, b_4 q\rangle\) has \(\gcd(W_-) = q\) of degree \(e = 2\)) acquires its extra minimal generator in degree \(2\cdot 6 - 2 = 10\) with character discrepancy proportional to \(N_{n-10} - N_{n-12}\) in (6).

### 7.2 Prime-ideal dichotomy on the supported graph boundary \(\Gamma_6^{\mathrm{supp}}\)

Suppose \((W_0, J_0) \in \Gamma_6^{\mathrm{supp}} \subset X_6 \times H_9\) lies over \(\Delta_6^{\mathrm{cf}}(e)\) (\(1 \le e \le 5\)), and write \(W_0 = D_e \cdot \langle A_{6-e}, B_{6-e}\rangle\) with \(\gcd(A_{6-e}, B_{6-e}) = 1\). Because \(D_e \cdot (A_{6-e}, B_{6-e}) = (W_0) \subset J_0 \subset I_C\) and \(I_C\) is a **prime ideal**, every such boundary pencil falls into one of two geometric types:

1. **Carrier-factor boundary (\(D_e \in V_e = H^0(\mathcal I_C(e))\), \(e \in \{2, 3, 4, 5\}\)):**
   Since \(V_1 = 0\), a common factor vanishing on \(C\) must have degree \(e \in \{2, 3, 4, 5\}\), with first degreewise cancellation degree \(12 - e \in \{10, 9, 8, 7\}\). The centered \(T\)-weight profiles of the carrier-factor spaces \(V_e\) (\(e = 2, 3, 4, 5\)) are:

   | Degree \(e\) | \(\dim V_e\) | Centered weight range | Centered weight profile of \(V_e\) | First cancellation degree \(12 - e\) |
   | :---: | :---: | :---: | :--- | :---: |
   | \(2\) | \(1\) | \(0 \dots 0\) | \([1]\) (spanned by \(q\)) | \(10\) |
   | \(3\) | \(7\) | \(-3 \dots 3\) | \([1, 1, 1, 1, 1, 1, 1]\) | \(9\) |
   | \(4\) | \(18\) | \(-5 \dots 5\) | \([1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1]\) | \(8\) |
   | \(5\) | \(35\) | \(-7 \dots 7\) | \([1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]\) | \(7\) |

   In particular, for \(e = 2\), \(D_2 = q\) has centered weight \(0\), so the carrier-factor stratum \(q \cdot \operatorname{Gr}(2, S_4)_{\mathrm{prop}} \subset \Delta_6^{\mathrm{cf}}(2)\) has dimension \(2(35 - 2) = 66\) and centered Plücker weights in \([-15, 15]\) (since \(S_4[\pm 8]\) are \(1\)-dimensional).

2. **Coprime-carrier-pencil boundary (\(D_e \notin I_C\) and \(\langle A_{6-e}, B_{6-e}\rangle \in U_{6-e} \subset \operatorname{Gr}(2, V_{6-e})\), \(e \in \{1, 2, 3\}\)):**
   If \(D_e \notin I_C\), primality of \(I_C\) forces both \(A_{6-e}\) and \(B_{6-e}\) into \(V_{6-e} = H^0(\mathcal I_C(6-e))\), so \(\langle A_{6-e}, B_{6-e}\rangle \in U_{6-e}\) is a proper complete-intersection pencil of degree \((6-e, 6-e)\) containing \(C\). Because \(V_1 = 0\) and \(\dim V_2 = 1\) (\(\operatorname{Gr}(2, V_2) = \emptyset\)), this type is **impossible for \(e \in \{4, 5\}\)**: it can occur only for \(e \in \{1, 2, 3\}\) (\(6 - e \in \{5, 4, 3\}\)). Furthermore, at any \(T\)-fixed point \((W_0, J_0)\) of this type in characteristic zero, \(\langle A_{6-e}, B_{6-e}\rangle \in U_{6-e}^T\) is a \(T\)-invariant proper complete intersection containing \(C\); by the eigenform theorem ([R-0001](../results/R-0001-global-splitting-obstruction-for-the-model-rational-quartic.md)), \(V(A_{6-e}, B_{6-e})\) cannot be sole-supported on \(C\), so it has a non-empty residual curve \(R' \not\subset C\) of degree \((6-e)^2 - 4m'\), and the extra generators of \(J_0\) modulo \((W_0)\) must vanish on \(C\) while cutting out \(I_C\)-primary support by eliminating \(R'\).

### 7.3 Intrinsic quadric-restriction sequence for \(V_{d,2}\) and the double-sextic sub-Grassmannian \(\operatorname{Gr}(2, V_{6,2})\)

Let \(V_{d,2} = H^0(\mathbf P^3, \mathcal I_C^2(d))\) be the space of degree-\(d\) surfaces singular along \(C\). Because \(C \subset Q = V(q)\) is a smooth divisor of bidegree \((1, 3)\) on the smooth quadric \(Q \cong \mathbf P^1 \times \mathbf P^1\) and \(q\) is part of a regular system of parameters along \(C\), \(\mathcal I_C^2 / (q \cdot \mathcal I_C) \cong \mathcal I_{C/Q}^2 \cong \mathcal O_Q(-2, -6)\). Twisting by \(\mathcal O_{\mathbf P^3}(d)\) gives the exact sequence of sheaves
\[
  0 \longrightarrow \mathcal I_C(d-2) \xrightarrow{\;\cdot q\;} \mathcal I_C^2(d) \longrightarrow \mathcal O_Q(d-2,\, d-6) \longrightarrow 0. \tag{11}
\]

**Proposition (Intrinsic structure and \(T\)-weight profile of \(V_{d,2}\) for \(d \ge 4\)).** In every characteristic, \(H^1(\mathbf P^3, \mathcal I_C(d-2)) = 0\) for all \(d \ge 4\), so (11) induces a \(T\)-equivariant short exact sequence of global sections:
\[
  0 \longrightarrow V_{d-2} \xrightarrow{\;\cdot q\;} V_{d,2} \longrightarrow H^0\bigl(Q,\, \mathcal O_Q(d-2,\, d-6)\bigr) \longrightarrow 0 \qquad (\forall\, d \ge 4). \tag{12}
\]
Consequently:
1. For \(d = 4\) and \(d = 5\), \(H^0(Q, \mathcal O_Q(d-2, d-6)) = 0\), so \(V_{4,2} = q \cdot V_2 = k \cdot q^2\) (\(\dim = 1\), centered weight \(0\)) and \(V_{5,2} = q \cdot V_3\) (\(\dim = 7\), centered weights \(-3 \dots 3\) of multiplicity \(1\)): **every quartic or quintic singular along \(C\) is divisible by \(q\)**.
2. For all \(d \ge 5\), \(H^1(Q, \mathcal O_Q(d-2, d-6)) = 0\) as well, so \(H^1(\mathbf P^3, \mathcal I_C^2(d)) = 0\), the conormal evaluation \(V_d \to H^0((\mathcal I_C/\mathcal I_C^2)(d))\) is surjective in every weight, and for each centered weight \(w \in [-2d, 2d]\):
   \[
     \dim V_{d,2}[w] = \max\bigl(0,\, \dim S_d[w] - 3\bigr) \qquad (\forall\, d \ge 5). \tag{13}
   \]
3. For **\(d = 6\)**, \(\dim V_{6,2} = \dim V_4 + \dim H^0(\mathcal O_Q(4, 0)) = 18 + 5 = 23\), supported on the \(13\) centered weights \(-6 \dots 6\) with symmetric profile
   \[
     \dim V_{6,2}[w] = (1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 1) \qquad (w = -6, \dots, 6).
   \]
   On the double-sextic sub-Grassmannian \(X_{6,2} := \operatorname{Gr}(2, V_{6,2}) \subset X_6\) (\(\dim X_{6,2} = 42\)), the exterior square \(\bigwedge^2 V_{6,2}\) has dimension \(\binom{23}{2} = 253\) and its centered Plücker weights fill the \(23\) integers **\(-11, \dots, 11\)** (with \(22\) open chambers and at most \(23 \cdot 24 / 2 = 276\) extremal-weight blocks).
4. For **\(d = 8\)**, \(\dim V_{8,2} = \dim V_6 + \dim H^0(\mathcal O_Q(6, 2)) = 59 + 21 = 80\), supported on the \(21\) centered weights \(-10 \dots 10\) with \(\dim V_{8,2}[w] = \dim S_8[w] - 3\).

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
