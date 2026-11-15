# Why a degree-four carrier cannot have a mate

Work over an algebraically closed field of characteristic zero and fix
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]
The accepted theorem [R-0001](../../results/quartic_carrier_exclusion.md) is:
for every **integral quartic** \(X\supset C\) and every homogeneous form
\(G\) of positive degree, \(V(X,G)_{\rm red}\ne C\).
There is no restriction on the mate degree, the normal order of its
equation, the singularities of the normalization, or the conductor scheme.
The unrestricted existence question for two degrees at least five remains
open. The [quartic-pair proof](../normal-geometry/quartic_pair_obstruction.md) is a separate,
narrower argument and is not used to assert this all-degree theorem.

The characteristic boundary is substantive: **in every characteristic
\(p>0\), this same embedded curve is an STCI using a quartic carrier**.
The [characteristic construction and exact fixed-carrier mate degrees](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier)
give the equations and their semigroup proof. Section 8 explains which
parts of the exclusion survive and which do not.

The proof has three common operations: turn sole support into a divisor
relation; compare numerical correction with actual embedded vanishing;
and test whether a normalization section descends through the **entire**
conductor. The sectional genus determines which operation finishes the
argument. This account owns the common lemmas, the normal-carrier proof,
and the exhaustive assembly. The linked specialized proofs own the long
projection and local-attachment calculations.

## 1. Sole support, smooth passage, and the common correction identity

Let \(\nu:S\to X\) be the finite normalization,
\(\sigma:M\to S\) a smooth resolution, and put
\(H=\nu^*\mathcal O_X(1)\), \(L=\sigma^*H\).
The genus \(\pi\) of a general normalized plane section satisfies
\[
L^2=4,\qquad K_ML=2\pi-6.
\]
For a normal carrier \(\pi=3\); for a nonnormal one \(0\le\pi\le2\).
Indeed, a general plane quartic has arithmetic genus three, and a
nonnormal hypersurface has a codimension-one nonnormal locus, giving
positive defect on that section. A Cohen--Macaulay hypersurface cannot
have only an isolated failure of normality.

**Generic regularity.** Every integral quartic containing a smooth
degree-four curve is regular at its generic point. Otherwise its partial
derivatives vanish along the curve. A general integral plane section then
has four distinct singular points, requiring normalization defect at least
four, greater than its arithmetic genus three. More generally this same
argument applies to a degree-\(d\) carrier containing a smooth curve of
degree \(\delta>(d-1)(d-2)/2\). The inequality is essential to this
argument; it gives no automatic generic regularity for quintics containing
\(C\).

**Full inverse support.** Assume a mate of degree \(b\) exists. Generic
regularity gives a unique curve \(c\subset S\) above \(C\), finite
birational and thus isomorphic to the normal curve \(C\). The nonzero
Cartier section \(\nu^*G\) has pure one-dimensional zero scheme on the
normal surface. Its zero set is the whole \(\nu^{-1}(C)\). There can
therefore be no isolated extra inverse point outside \(c\), and
\[
(\nu^{-1}C)_{\rm red}=c,\qquad
\operatorname{div}_S(\nu^*G)=bc\sim bH.                 \tag{1}
\]
The coefficient is \(b\) because \(Hc=H^2=4\). On a different-degree
carrier it would be \(b\deg X/\deg C\). Equation (1) does not make
\(c\) Cartier: it makes its specified multiple Cartier.

**Smooth passage.** The strict transform \(\widetilde c\subset M\)
is isomorphic to \(C\): the rational lift from the smooth proper curve
extends by the valuative criterion and is a section over \(C\).
At a singular point of the normal surface \(S\), every function in its
maximal ideal pulls back with positive integral order along every
exceptional prime in that fiber. At the lifted point on the smooth
surface their distinct local equations divide the pullback. Some such
function restricts to a uniformizer on the embedded smooth \(c\).
Consequently the sum of its intersections with the reduced exceptional
fiber is one. Thus \(\widetilde c\) meets exactly one exceptional prime,
transversely at a smooth point away from all other primes. The argument
also allows singular exceptional primes and nontransverse exceptional
intersections; the actual curve cannot pass through those bad points.

Pulling back (1) and dividing by \(b\) gives
\[
\widetilde c+Z\equiv L,\quad Z\ge0\text{ exceptional},\quad
Z E_i=-\widetilde cE_i.
\]
Set \(q=-Z^2=\widetilde cZ\ge0\). Adjunction gives the shared identity
\[
\boxed{\widetilde c^2=4-q,\qquad q+K_MZ=2\pi.}          \tag{2}
\]
This is the common genus budget. It uses a divisor of an **actual** mate,
not just a proposed numerical configuration. The separate
[normal-line comparison](numerical_surface_pullback.md) measures the
additional exceptional vanishing of the curve ideal; a numerical
correction alone does not measure that vanishing.

## 2. Why a nonnormal normalization is rational

The following intrinsic criterion is independent of a mate or special projection, and holds over an algebraically closed field of **any characteristic**.

**Ruled-surface degree criterion.** Let \(M\) be smooth projective, \(L\) nef Cartier, \(d=L^2>0\), and \(A=-K_ML>0\). If an integral rational curve has positive \(L\)-degree \(\delta\) and \(A\delta>d\), then \(M\) is rational. More precisely, on a nonrational surface the ruled base has genus \(g\ge1\), and
\[
 d\ge A\delta+(2g-2)\delta^2.
\]
The [complete intrinsic proof and sharpness examples](ruled_surface_degree_criterion.md) use smooth minimal ruledness and actual ruling fibers on a common resolution. They justify the bound at infinitely near centers and exclude inseparable maps from a rational curve to a positive-genus base. They do not require Kawamata--Viehweg vanishing or classification of the nonnegative Kodaira-dimension cases.

Here \(A=d+2-2\pi\). For a nonnormal quartic, \(d=\delta=4\) and \(\pi\le2\), so \(A\delta>d\). The normalization is rational **before** a mate is assumed. For a normal quartic \(\pi=3\), the key coefficient is zero and this criterion does not apply. The intrinsic criterion extends in characteristic; the rest of the carrier exclusion retains its own hypotheses.

Two cohomological refinements of the original special-case proof are
also useful. Kawamata--Viehweg vanishing and duality give
\(H^1(M,\mathcal O_M(-L))=0\). Restriction to a smooth general
hyperplane curve \(Y\) therefore injects
\(H^1(\mathcal O_M)\hookrightarrow H^1(\mathcal O_Y)\), so the
irregularity of a hypothetical nonrational ruling satisfies \(g\le\pi\).
The stronger intersection criterion above does not need this bound,
but it explains the cohomological meaning of the sectional genus.

After rationality is proved, Leray injects \(H^1(S,\mathcal O_S)\)
into \(H^1(M,\mathcal O_M)=0\), without a rational-singularity
assumption on \(S\). The degree-four line bundle \(H|_Y\) is
nonspecial for \(\pi\le2\), so the Cartier restriction sequence gives
\(h^0(S,H)=1+(5-\pi)=6-\pi\). Thus the complete systems have six,
five or four sections in genus zero, one or two respectively; these
dimensions alone do not prove an embedding or classify a polarization.
These two refinements retain their unchanged accepted source proofs.

## 3. Normal quartics: exceptional correction and actual ideal vanishing

There are two external surface inputs. Jaffe's
[Theorem B / 11.11](https://arxiv.org/pdf/alg-geom/9410008) says a smooth
STCI curve on a quartic with only rational singularities in characteristic
zero must be linearly normal. A smooth rational quartic in \(\mathbf P^3\)
is not linearly normal, so this excludes that case. His smooth
curve--ADE pair data supply the correction and first-normal orders below.
Ishii--Nakayama's
[Main Theorem and \S2.4](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf)
classify the remaining normal quartics. The positive-genus ruled cases
have hyperplane degree at most three on a ruling fiber, so cannot contain
our degree-four rational curve. The rational minimal resolutions satisfy
\[
K_M=-E,\qquad d=-E^2\in\{1,2,3\},\qquad\rho(M)=10+d,
\]
where \(E\) is effective exceptional and may be singular or nonreduced.
The irrationality classification is over \(\mathbf C\); the field-transfer
argument at the end of this section retains the full characteristic-zero
scope.

### 3.1 Compression and the passage budget

Put \(A=(-E_iE_j)\), let \(a\) be the coefficient vector of \(E\),
and \(m_i=\widetilde cE_i\). Then
\[
z=A^{-1}m,\quad t=a^tm=\widetilde cE,\quad
q=m^tA^{-1}m,\qquad t+q=6,\quad t^2\le dq.             \tag{4}
\]
The last inequality is Cauchy--Schwarz in the full positive-definite
matrix \(A\), including all separate ADE blocks.

Let \(n\) be the least positive common denominator of the **whole**
vector \(z\). The [general global compression theorem](normal_carrier_compression.md#1-global-denominator-compression)
uses numerical-to-linear equivalence on the whole rational resolution,
pushforward of principal divisors, and ambient section lifting to give
an actual mate of degree \(n\), with \(n\mid b\). Its full arbitrary-
carrier-degree proof, singular/nonreduced determinant bound and cusp
illustration have that single owner. This is a global implication under
existence, not cancellation in an arbitrary local class group.

Minimality and adjunction show that any exceptional prime of coefficient
zero in \(E\) is a \((-2)\)-curve disjoint from its support. Connectedness
of \(E\) and of resolution fibers separates one irrational fiber from
the ADE fibers. The curve must meet the irrational fiber. If it avoided
it, (2) would require ADE correction six, while rank at most twelve and
total first-normal order at most nine give at most \(36/7<6\) by the
inequality below.

Thus \(t>0\). Equation (4) and denominator-one compression in its equality
cases leave
\[
d=1:\ t=1;\qquad d=2,3:\ t\in\{1,2\}.                \tag{5}
\]
Here \(t\) is the coefficient of the sole prime met in the irrational
fiber, by smooth passage. At an irrational hypersurface point the two
first-normal coefficients have common order at least two: order one
would give a rank-at-least-two quadratic term, hence a formal \(A_n\)
rational singularity by splitting. A quartic gives a pair of binary
degree-nine first-normal coefficients, so at most seven orders remain
for the ADE points.

### 3.2 A single inequality excludes irreducible anticanonical support

For a smooth-curve ADE pair, write \(r_i\) for root rank, \(s_i\) for
first-normal order, and \(\gamma_i\) for correction. Jaffe's
Propositions 5.2 and 5.7 give
\[
\gamma_i\le\frac{r_is_i}{r_i+s_i},\qquad
\sum\gamma_i\le\frac{RP}{R+P},\quad R=\sum r_i, P=\sum s_i.       \tag{6}
\]
The second inequality follows by writing each summand as
\(r_i-r_i^2/(r_i+s_i)\) and applying Cauchy--Schwarz. Its first
inequality is checked on the permitted ADE pairs, not on arbitrary
Cartier-index data. This is a reusable rank/order budget; the
[index-two family](numerical_surface_pullback.md#cartier-index-does-not-bound-the-numerical-correction)
shows why index alone cannot replace the root matrix.

If \(E=aP\), then \(a^2(-P^2)\le3\) forces \(a=1\). Smooth
passage gives \(t=1\), even for singular arithmetic-genus-one \(P\).
Its correction is \(1/d\), so the ADE correction must equal
\(5-1/d\). With \(R\le8+d\), \(P\le7\), (6) gives strict gaps
\(1/16,13/34,7/18\), for \(d=1,2,3\). This treats the smooth elliptic,
nodal, and cuspidal irreducible cases at once; their separate local
classifications are unnecessary for this exclusion.

### 3.3 Reduced reducible support: the exact finite calculation

If \(E\) is reduced and reducible, component adjunction forces smooth
rational primes and a connected degree-two intersection multigraph.
It is a cycle, including the two-prime intersection-two case. With
\(k\) primes and \(b_i=-E_i^2\),
\[
2\le k\le9+d,\quad b_i\ge2,\quad\sum(b_i-2)=d.
\]
The matrix permits tangencies or coincident exceptional intersections;
the smooth curve avoids them. For every cycle, mark one passage vertex
\(j\), compute \((A^{-1})_{jj}\) and its full inverse-column denominator,
and compare all ADE multisets with rank at most \(9+d-k\), order at
most seven, and correction \(5-(A^{-1})_{jj}\). The exact complete
calculation leaves:

| \(d\) | cycle diagonals, starting at the marked prime | irrational correction | ADE pairs | denominator |
|---:|---|---:|---|---:|
| 1 | \((2,3)\) | \(3/2\) | seven \(A_1\) | 2 |
| 1 | \((2,3)\) | \(3/2\) | five \(A_1\), middle \(A_3\) | 2 |
| 1 | \((2,2,3,2)\) | 2 | six \(A_1\) | 2 |
| 2 | \((2,2,4,2)\) | \(3/2\) | seven \(A_1\) | 2 |
| 3 | \((2,2,5,2)\) | \(4/3\) | six \(A_1\), end \(A_2\) | 6 |

The first four compress to the impossible quadric mate. The final row
spends all nine first-normal zeros, so the normal line has degree seven
and its numerical square is four. The
[ideal-versus-numerical defect formula](numerical_surface_pullback.md)
allows total defect three. Its six nodes each cost \(1/2\). The end
\(A_2\) costs \(1/3\): on \(xy=z^3\), \(c=(x,z)\), the blowup chart
\(y=u,z=uv,x=u^2v^3\) principalizes its ideal as \((uv)\); both
exceptional ideal coefficients are one, while the contacted numerical
coefficient is \(2/3\). Hence the row requires
\(3\ge6/2+1/3=10/3\), a contradiction.

The necessary exact support is
[the cycle checker](../../computations/verify_session_normal_carrier_progress.py)
and [its independently reconstructed checker](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_normal_independent_audit.py).
They build the ADE inverse columns and budgeted multisets and enumerate
the finite cycles just specified. The recorded executions establish these
unchanged exact calculations; no fresh execution is claimed here. A
reported rank or row count alone would not replace their exhaustive inputs.

### 3.4 Nonreduced support: trees and the actual maximal ideal

For every proper nonzero effective subdivisor \(D<E\), rationality and
duality give
\[
H^1(\mathcal O_D)=H^2(\mathcal O_M(-D))
=H^0(\mathcal O_M(D-E))^*=0.
\]
Taking primes and then the connected reduced support proves that the
support is a rational SNC tree with simple edges. For its positive
coefficient vector \(a\),
\[
A a=b-2,\quad 1\le d=\sum a_i(b_i-2)\le3,
\quad k\le9+d\le12,\quad\sum(b_i-2)\le3.               \tag{7}
\]
Some coefficient exceeds one. The marked coefficient is constrained by
(5). Together with ADE rank/order/correction budgets and compression,
(7) defines a finite **necessary superset** of geometric configurations.

[The exact tree checker](../../computations/verify_session_normal_nonreduced_trees.py)
generates free trees by leaf addition, weak diagonal excesses of total at
most three, and exact rational solutions of (7). Its
[independent reconstruction](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_nonreduced_independent_audit.py)
uses rooted-multiset tree codes and determinant-by-matchings rather than
Schur elimination. All correction-column denominators are retained.
For clarity, its distinct exact matrix argument is as follows. A
determinant permutation of a tree has only fixed points and edge
transpositions, so
\[
\det(A+xI)=\sum_{\text{matchings }\mathcal M}(-1)^{|\mathcal M|}
\prod_{i\text{ unmatched}}(b_i+x).
\]
All roots of this polynomial are real because \(A\) is symmetric.
Positive definiteness implies all coefficients are positive; conversely
positive coefficients forbid a root at \(x\ge0\), so forbid any
nonpositive eigenvalue. If \(P_{ij}\) is the unique path from \(i\)
to \(j\), its inverse entries are
\[
(A^{-1})_{ij}=\frac{\det(A\text{ with }P_{ij}\text{ deleted})}{\det A}.
\]
For \(i=j\) this is the principal cofactor. For a mixed cofactor the
unique path is forced; its off-diagonal \(-1\) factors cancel the
cofactor sign, and the remaining permutations are matchings on the
complementary forest. This proves the formula and explains why the
second implementation supplies a genuinely different exact check.
After the independently proved mate-degree exclusions through five,
every surviving row has \(d=3,t=2\). The computations eliminate a
superset; they do not claim that its weighted trees are realizable.
The low-degree inputs are the plane/quadric and classical cubic and
\((4,4)\) exclusions, and the independent
[\((4,5)\) proof P-040](../residuals/quasiprimitive_multiplicity_five.md#p-040).
Thus this step does not invoke R-0001 circularly.

The classification identifies \(d=3\) with Type D. Its hyperplane
sections are
\[
\xi_0=\phi_4,\quad
(\xi_1,\xi_2,\xi_3)=\phi_3\rho^*(x,y,z),
\]
where \(\phi_3\) cuts out the **whole** \(E\), \(\phi_4\) is a unit
along it, and the three plane coordinate sections have no common zero.
At its image \(p=(1:0:0:0)\), the pulled maximal ideal is therefore
exactly \(\mathfrak m_p\mathcal O_M=\mathcal O_M(-E)\), including
multiplicities. Restriction to the embedded smooth curve has order one,
so \(t=\widetilde cE=1\). This contradicts the only remaining numerical
rows. An ideal identity, rather than one more graph enumeration, closes
the normal case.

For all algebraically closed characteristic-zero fields, descend a
hypothetical pair and finite radical-equality witnesses to a finitely
generated field. Geometric integrality and normality descend faithfully
from its algebraic closure in the given field; an embedding into
\(\mathbf C\) then preserves them and all radical-equality identities.
The forbidden complex pair would result. This supplies the field
transfer for the complex classification without any uncountability
assumption.

## 4. Sectional genus zero: finite normalization and descent

Here \(K_ML=-6\). Nefness makes \(H^0(K_M+L)=0\), while
Kawamata--Viehweg vanishing and Riemann--Roch give \(\chi(\mathcal O_M)=1\).
Restriction to a general rational hyperplane section gives \(h^0(S,H)=6\).
The complete map is finite (\(H\) is ample) and birational (the original
normalization map factors through it). Its degree-four image in
\(\mathbf P^5\) is a minimal-degree surface. The classical
[minimal-degree classification, Theorem 0.1](https://www.math.stonybrook.edu/~sorin/eprints/2-regular.pdf)
therefore gives precisely
\[
(\mathbf F_0,C_0+2f),\quad(\mathbf F_2,C_{\min}+3f),\quad
(\mathbf P^2,\mathcal O(2)),\quad S(0,4).
\]
All are normal, so the finite birational complete map is an isomorphism.
The proof and the singular-cone argument are in
[the genus-zero proof](sectional_genus_zero_normalization_proof.md).

The two scrolls use the actual conductor, an ACM cubic scheme, and its
generic Artin algebras. Reduced conic-plus-line and three-line cases,
Gorenstein thick lines, fat triple lines, and nongorenstein doubled-line
crossings require different local algebra, all covered in the
[entire-scroll proof](quartic_scroll_nonreduced_conductors.md).
The common mechanism is to compress a descended power to a square on
the full conductor and obtain a forbidden quadric mate, or to contradict
an immersion by generic differential vanishing. The full conductor
scheme is essential to that compression.

For the Veronese, a projection center is a pencil of symmetric quadratic
forms. The regular-pencil Jordan types give the Roman, size-two Jordan,
and size-three Jordan cases. Every-member-singular pencils have
degree-two projection and quadric image, so are not quartic
normalizations. Roman singleton fibers cannot lie on the required conic;
the size-two case leaves only one allowable conductor point; and the
size-three case has a nonzero first conductor jet for every conic power.
The [classification and exact conductor-jet proof](../curve/veronese_quartic_projections.md)
retain these three distinct obstructions.

For the cone \(S(0,4)\), \(\operatorname{Cl}(S)=\mathbf Z[f]\) and
\(H=4f\), so (1) forces \(c\sim H\), hence \(c\) Cartier and disjoint
from the vertex. On its \(\mathbf F_4\) resolution it is a ruling
section. The original projection is a cone over a rational plane quartic.
A multibranch base point violates full inverse support; a singleton
singular branch has vanishing base derivative. Differentiating the actual
unit-times-power mate identity along this kernel makes the section tangent
to the kernel, contradicting immersion of \(c\to C\). The
[complete cone calculation](sectional_genus_zero_normalization_proof.md#3-the-singular-minimal-degree-cone-is-excluded-in-every-mate-degree)
also shows why a numerical class calculation alone is insufficient.

## 5. Sectional genus one: a permitted ribbon with incompatible projection

Adjunction and minimality force \(K_M=-L\); the normalization is the
degree-four ADE del Pezzo anticanonical model in \(\mathbf P^4\).
The \(D_5\) exceptional-lattice saturation argument gives actual
\(2c\sim2H\), not merely \(2[c]=2[H]\) numerically. The
[root-lattice proof](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-torsion-filtermd)
and [del Pezzo reduction](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
own these classification steps.

Restriction of the five anticanonical sections to \(c\) is an
isomorphism onto \(H^0(\mathbf P^1,\mathcal O(4))\). A kernel section
would have divisor \(c\) by degree, making it Cartier contrary to its
nonzero exceptional correction. Thus the complete coordinates are
\((s^4,s^3t,s^2t^2,st^3,t^4)\), and the original map necessarily deletes
the middle coordinate. Its center misses \(S\). This derives the fixed
center for every carrier in the lane; a convenient toric example would
not establish that coverage.

The Cartier double is a CM ribbon with nilideal \(\mathcal O(-6)\).
Writing the six rational-normal-quartic quadrics in their natural order,
its quadratic net consists exactly of vectors \(d\) with
\[
\begin{pmatrix}d_0&d_1&d_2\\d_1&d_2+d_3&d_4\\d_2&d_4&d_5\end{pmatrix}
\begin{pmatrix}\eta_0\\\eta_1\\\eta_2\end{pmatrix}=0,
\qquad\eta_1^2-\eta_0\eta_2\ne0.                       \tag{8}
\]
The conic of excluded directions has a cubic surface as net base locus;
the open directions give actual \((2,2,2)\) ribbons. See the
[complete conormal-net proof](genus_one_ribbon_conormal_net_proof.md).

The actual two-quadric normalization can be written
\(z^2-Az-R_1=Lz+R=0\). Elimination gives
\(R^2+ALR-R_1L^2=0\), and the entire conductor is \((L,R)\), including
nonreduced conics. Its full algebra is derived by the
[graded-module conductor proof](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-entire-conductor-algebra-independent-auditmd).
For quadrics \(Q_1,Q_2\) normalized to have middle-square coefficients
one and zero, respectively, the omitted-coordinate derivatives satisfy
\[
\operatorname{rad}(D_{Q_2})\mid D_{Q_1},\qquad
D_d=d_0s^4-d_1s^3t-2d_3s^2t^2-d_4st^3+d_5t^4.         \tag{9}
\]
This is support divisibility, not a multiplicity assertion.

The five root partitions of the nonzero binary quartic \(D_{Q_2}\)
are exhaustive. The squarefree case is excluded by (8)--(9) and the
[actual projection fiber test](genus_one_uniform_projection_analysis.md).
The [proof for partition 2,1,1](genus_one_211_projection_proof.md)
uses the exact double fiber and the forced extra derivative zero.
For \([4]\) and \([3,1]\), the full net forces a line of singularities,
contrary to normality. The \([2,2]\) case reduces to one pencil whose
quadratic conductor trace and norm forbid **every** descended positive
power. The [complete repeated-partition proof](genus_one_ribbon_partition_proofs.md)
retains the invisible coefficient \(d_2\), all determinant roots, and
the direction boundary. Its
[independent ideal certificates](genus_one_ribbon_partition_proofs.md#genus-one-ribbon-repeated-partition-independent-certificates)
remain necessary exact support. General \(\mathrm{PGL}_2\) moves the
projection center and cannot be substituted for its center-preserving
orbit calculation.

The genus-one projection interface remains **conditional** on separate exclusions of the \([4]\), \([3,1]\), and \([2,2]\) contact partitions; no mate-degree bound, normal order, or reduced-conductor assumption is used. The full mathematical dependencies are retained in the focused genus-one Arguments.

## 6. Sectional genus two: conic geometry and the two correction strata

The [adjoint proof](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-two-adjoint-conic-modelmd)
gives \(K_M^2=0\), \(f=K_M+L\), and a complete connected basepoint-free
rational pencil \(|f|\) of plane conics. Exceptional primes are vertical
\((-2)\)-curves or horizontal \((-3)\)-sections, at most two of the
latter. Put \(\lambda=K_MZ\). Equation (2) and Hodge give
\[
q+\lambda=4,\qquad\lambda\in\mathbf Z_{\ge0},\qquad
\lambda^2\le q,
\quad(\lambda,q)=(0,4)\text{ or }(1,3).               \tag{10}
\]
Dropping the horizontal canonical correction would incorrectly force
\(q=4\) in both cases.

The [entire-conductor theorem](genus_two_entire_conductor_proof.md)
identifies the actual downstairs conductor as a reduced line \(\Gamma\)
and its upstairs quadratic algebra, including split and nonreduced
covers. The
[ambient blowup proof](genus_two_ambient_conic_model_proof.md)
identifies the two line equations naturally with the complete adjoint
pencil. Their common factor generates the whole pulled line ideal; this
gives the actual lift into \(\operatorname{Bl}_\Gamma\mathbf P^3\).
Its strict transform \(T\) is normal Gorenstein ADE by the proper-duality
trace argument and is crepant from \(M\). This assertion concerns \(T\),
not the potentially non-Gorenstein normalization \(S\). The actual line
intersection length is
\[
\operatorname{length}(C\cap\Gamma)=4-f\widetilde c.
\]
These lift and normality steps are accepted inputs with complete proofs;
their earlier proposal labels do not represent a current gap in R-0001.
An arbitrary abstract conic bundle with the same lattice data would not
supply this ambient realization.

### 6.1 Bisection: the global nilideal obstruction

For \(\lambda=0\), \(f\widetilde c=2\), and \(|\widetilde c|\) is a
second connected rational pencil. The pair of pencils has degree two
onto \(\mathbf P^1\times\mathbf P^1\); its normal Stein cover has branch
class \((2,2)\). Its crepant resolution has \(K^2=4\), so \(M\) is
obtained by four point blowups. If \(R\) is the actual relative canonical
divisor and \(k_t\) counts all blowups over a fiber, including infinitely
near centers, the second-pencil proof gives the equality of actual cycles
\[
2Z=\sum k_tF_t-2R,\qquad\sum k_t=4.
\]
Thus \(2Z\) is integral and compression gives a Cartier double
\(2c\sim2H\) on \(S\). It need not be an ambient quadric section.

The Cartier double is CM of generic length two with smooth reduction,
hence a ribbon: the square of its nilideal vanishes generically and
purity forbids a finite-support square; its torsion-free rank-one
nilideal is a line bundle. Rational singularities give
\(\chi(\mathcal O_S(mH))=2m^2+m+1\); the Cartier sequence at \(-2H\)
then gives nilideal \(J=\mathcal O_{\mathbf P^1}(-8)\).
The normalization morphism on the entire ribbon induces
\(N^*_{C/\mathbf P^3}\to J\), nonzero on the open where normalization
is an isomorphism. But
\(N^*_{C/\mathbf P^3}=\mathcal O(-7)^2\) has no nonzero map to
\(\mathcal O(-8)\), a contradiction. The
[complete bisection proof](genus_two_bisection_proof.md)
includes the exact two-pencil, Cartier-double and characteristic-zero
normal-bundle arguments. It replaces the longer fiber-by-fiber closure;
the even/three-center proofs remain useful distinct descent mechanisms.
The same global ribbon contradiction excludes a section-stratum candidate
if its own independently established integral \(2Z\) gives actual
\(2c\sim2H\). No assertion makes every section correction half-integral.

**Reusable boundary.** A ribbon over \(\mathbf P^1\) with nilideal
\(\mathcal O(j)\), mapped to an ambient embedding with conormal
\(\mathcal O(-a)\oplus\mathcal O(-b)\), can have a generically nonzero
normal map only if \(j\ge-\max(a,b)\). Its genus is \(-j-1\).
This immediate Hom calculation explains both cases: the genus-two
double violates the degree bound, while the genus-one ribbon's
\(\mathcal O(-6)\) is permitted and needs the finer projection test.
Smooth reduction and generic multiplicity alone do not make a ribbon:
\(k[[t,e]]/(te^2,e^3)\) has an embedded point and nonzero nilideal square.

### 6.2 Section: genuine trisecants and an all-length graph inequality

For \(\lambda=1\), \(f\widetilde c=1\) and \(C\cap\Gamma\) has
length three. Thus \(\Gamma\) lies on the unique smooth quadric
\(q=x_0x_3-x_1x_2\). Its degree-three ruling has lines
\[
\Gamma_a=(x_2-ax_0,x_3-ax_1),\qquad
C\cap\Gamma_a:\ t^3-as^3=0.
\]
There are exactly two contact types: three distinct points for
\(a\ne0,\infty\), and one triple point for \(a=0,\infty\), exchanged
by reversal. There is no missing \([2,1]\) case for this fixed embedding.
This contact split uses \(3\ne0\): in characteristic three the map
\([s:t]\mapsto[s^3:t^3]\) is inseparable and every such fiber is a
triple contact, so the three-distinct-contact argument does not carry over.
The [exact carrier-ideal proof](genus_two_trisecant_carrier_proof.md)
gives the whole eleven-dimensional quartic space, rather than a sampled
family. The marked-plane analysis forces a special horizontal prime
\(B^2=-3\) disjoint from \(\widetilde c\); the
[free-chain argument](../../frameworks/carrier-normalization/quartic_proof_interfaces.md#19-genus-two-marked-section-case)
proves that a configuration without this prime is impossible.

For three distinct contacts, write the conductor section of the actual
ambient exceptional surface as \(D_T\) of bidegree \((2,2)\), containing
the fiber \(B_T\). Every reducible residual and repeated-fiber divisor
is excluded by the singleton-fiber test, including the case when the
coefficient of \(B\) in \(Z\) is zero. For integral residual
\((1,2)\), its other two singleton fibers consume both branch values of
its degree-two map to \(\Gamma\). It meets \(B_T\) in two transverse
points. Relative formal Morse splitting, preserving the actual conductor
branches, gives endpoint \(A_n\)-chains of arbitrary length.

If the contacted chain has length \(n\), contact position \(k\), and
the other chain length \(m\ge0\), elimination gives
\[
\operatorname{coeff}_B Z=
\frac{(n+1-k)/(n+1)}{3-n/(n+1)-m/(m+1)}<1.
\]
Its numerator is below one and denominator above one, contradicting
\(K_MZ=1\). This is an all-length statement, not a finite chain search.
The [nonendpoint proof](genus_two_nonendpoint_proof.md)
contains the entire divisor exhaustion and exact inverse-chain formulas.

### 6.3 Triple contact: actual normal coefficients replace an abstract graph

At the endpoint the exact lift is \((a,b,y)=(r,r,r^3)\). The full
quartic equation after its required horizontal factor has exceptional
restriction
\[
P=a\bigl[(b-a)(a_1+b_1b)-b^2(c_0+c_1a)\bigr].
\]
All regimes are needed. If \(c_0\ne0\), smooth contact and the exact
second-horizontal possibilities force coefficient \(1/3\), contradicting
one; this includes a coefficient-zero special \(B\), a second fiber at
infinity, and repeated fixed fibers. For \(c_0=0,a_1\ne0\), there are
two transverse residual crossings and the preceding all-length inequality
applies, including a crossing at infinity. For
\(c_0=a_1=0,b_1\ne0\), the complete local equation forces an endpoint
\(A_n\), an internal \(A_n\) with coefficient \(2/(n+5)\), or a
\(D_4\) with coefficient \(1/4\); a multiplicity-three germ is
incompatible with the accepted ADE model.

The remaining doubled-horizontal divisor is \(2B_T+2F_0\). Its actual
normal coefficient along \(B_T\) is a degree-three section
\(h(b)=b(A+B_1b+Cb^2)\). For an ADE block with positive Cartan matrix
\(Q\), attachment vector \(v\), and contact vector \(e_j\), the
correction equation requires
\[
\sum v^tQ^{-1}v+v^tQ^{-1}e_j=3.
\]
Crepancy and the complete equation give
\(2v^tQ^{-1}v=\operatorname{ord}(h)\) at every root away from contact,
including infinity and repeated roots. At contact, exact factorization
forces \(A_3,A_5,A_7\) with specified attachment positions; their
contribution plus all other roots is at most \(5/2\), a contradiction.
The [endpoint proof](genus_two_endpoint_proof.md) and
its linked local calculations retain the actual equations proving these
positions. An abstract ADE graph with the right square is insufficient.

## 7. Exhaustion, useful alternatives, and what remains unproved

Normal quartics and nonnormal quartics of sectional genera zero, one, and two exhaust the integral degree-four carriers. The genus-two correction identity and actual line positions cover the section stratum; genus-one partition completeness requires the fixed projection center. Hence the accepted R-0001 argument excludes every integral quartic carrier in characteristic zero.

The proof mechanisms are **not interchangeable**: numerical pullback belongs to a normal resolution; full-conductor descent governs nonnormal gluing; the ribbon Hom obstruction is global and embedded; trisecant exclusions use actual ambient blowup attachments. The doubled-horizontal case requires its cubic normal coefficient rather than a reduced two-crossing formula.

Two counterexamples prevent shortcuts: a smooth lifted curve can pass through an \(A_1\) normalization point while retaining a local mate ([local model](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-singular-local-liftmd)); full inverse support does not imply containment in the nonreduced ramification scheme ([Fitting model](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-ramification-scheme-counterexamplemd)). Numerical conic-bundle data likewise cannot replace invertibility of the pulled center ideal and its section ratios. The independent \((4,4)\), primitive \(e=2\), MF6, and even/three-center mechanisms remain distinct; their obsolete quartic-mate open labels do not. R-0001 does not settle sextic mates, ancestor incidence, or global realization of formal normal models.

## 8. What changes in positive characteristic

The [positive-characteristic construction](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) gives an actual quartic carrier in **every** positive characteristic. The characteristic-zero exclusion cannot be transported wholesale:

| Mechanism | Characteristic scope and missing input |
|---|---|
| Smooth passage, full inverse support, plane-section genus | Valid under the stated integral/smooth hypotheses in any characteristic, but not contradictory alone. |
| Ruled degree criterion | [Intrinsic criterion](ruled_surface_degree_criterion.md) is characteristic-free; each carrier still needs its numerical hypotheses. |
| Normal resolution and compression | Negative intersection and rational-surface linear equivalence retain their meaning on available resolutions; classification, actual ideal budgets, and low-degree exclusions do not automatically transfer. |
| Ribbon and global Hom obstruction | Pure CM doubles are ribbons in any characteristic. Here \(N_C^\vee=\mathcal O(-7)^2\) for \(p\ne2\), but \(\mathcal O(-6)\oplus\mathcal O(-8)\) for \(p=2\). Neither splitting guarantees the requisite genus-two Cartier double for arbitrary carriers. |
| Conductor differentiation and power descent | The factor \(b\) in \(d(uf^b)\) can vanish for \(p\mid b\); Frobenius can annihilate nilpotent descent obstructions. |
| Quadratic trace and local Morse splitting | Require \(2\) invertible, separability, and the relevant ambient hypotheses. |
| Fixed trisecant geometry | The three distinct contacts of \(t^3-as^3\) require \(p\ne3\); characteristic three gives inseparable triple contact. |
| Global \((4,4)\) bound | The characteristic-zero Hodge/Picard bound is not a positive-characteristic exclusion. |

Even in odd characteristic, the balanced conormal splitting does not exclude the known STCI: the missing implication is that an arbitrary supported pair supplies the **particular** genus-two Cartier double with a nonzero global normal map. The positive-characteristic construction instead uses conductor descent powers divisible by the characteristic.

## 9. Verification boundaries

Independent normal-graph and weighted simple-elliptic checks support the **necessary** numerical cases in §3, not an unrestricted classification. The repaired \(a=-1/2\) checker requires \(x\ne0\); quartic-incidence membership is over \(\mathbf Q\) with rational constants. The repeated-partition M2 certificate was recovered byte-identically, **not rerun**. The normal route retains passage/correction budgets, integral compression, reduced-cycle pullback defect, and the Type D maximal-ideal bound. The [two-arm Green-function comparison](../normal-geometry/saturation_rees_and_carrier_cases.md#q-two-arm-coefficient-one-tails-exact-comparison) requires its terminal diagonal condition. The [ruled criterion](ruled_surface_degree_criterion.md) is characteristic-free, but the carrier conclusion here is characteristic zero.

## Consolidated historical supplement: `research/supplements/QUARTIC_PROJECTION_MODULI.md`

# Projection-center moduli and the exact characteristic-two comparison

The projection center and its binary-form avatar are distinct in small characteristic. The catalecticant tests embedded smoothness, whereas the discriminant tests collisions of the auxiliary center roots. The full calculation below retains two inequivalent smooth projected curves with the same coarse quotient value and gives the literal characteristic-two stabilizer and Hasse contact maps. It is independently reviewed exploratory geometry, not an unrestricted STCI statement.

## 1. Literature checked and the boundary of the comparison

The classical inputs are [Bernardi, *Normal bundle of rational curves and Waring decomposition*, J. Algebra 400 (2014), §2.1, Remark 2.7 and Proposition 2.8](https://arxiv.org/pdf/1203.4955#page=3), for apolarity, catalecticant secant rank, and smooth projection-center criteria; and [Isaev, *Duality for binary quartics and ternary cubics arising from their Milnor algebras*, Rev. Roumaine Math. Pures Appl. 60 (2015), §3](https://imar.ro/journals/Revue_Mathematique/pdfs/2015/4/5.pdf#page=6), for the strictly semistable orbit quotient and invariants (3.3)–(3.5). Neither Bernardi's normal-bundle results nor Isaev's associated-form duality is being imported as an osculating-involution theorem. Isaev works over \(\mathbf C\); the elementary root-orbit arguments below apply over algebraically closed characteristic-zero fields. No priority claim is made for these classical constructions.

## 2. Smooth projection centers and their invariant quotient

Let $W=H^0(\mathbf P^1,\mathcal O(4))$. Use the monomial basis
$s^4,s^3t,s^2t^2,st^3,t^4$ of $W$, and its dual coordinates
$[a_0:a_1:a_2:a_3:a_4]$ on $\mathbf P(W^\vee)$. The complete embedding is

\[
\nu_4([s:t])=[s^4:s^3t:s^2t^2:st^3:t^4].
\]

The closed secant variety $\sigma_2(C_4)$ includes tangent lines. Its equation
is the catalecticant cubic

\[
J=\det\begin{pmatrix}
a_0&a_1&a_2\\a_1&a_2&a_3\\a_2&a_3&a_4
\end{pmatrix}=0.
\tag{2.1}
\]

For completeness, the rank-one matrix of a point of $C_4$ shows that every
secant has rank at most two; the closed secant variety is therefore contained
in this cubic. The secant variety is irreducible of dimension three: at the
two endpoints its two tangent lines span a projective three-space, and the
same rank condition persists on an open set of pairs. The determinant is
irreducible. Indeed, as a polynomial in $a_4$ it has coefficient
$a_0a_2-a_1^2$ and constant term
$-a_0a_3^2+2a_1a_2a_3-a_2^3$; these are relatively prime. To see this,
the first is irreducible, while on $a_0=1,a_2=a_1^2$ the second becomes
$-(a_3-a_1^3)^2$, which is not identically zero. The irreducible cubic
hypersurface consequently equals $\sigma_2(C_4)$.

A center outside this variety identifies no two points and kills no tangent
direction. The induced linear system separates every length-two subscheme
of $\mathbf P^1$, which is precisely the very-ampleness criterion for the
map to its projective target to be a closed immersion. Conversely, a
center on a secant or tangent prevents that separation. Hence

\[
U=\mathbf P(W^\vee)\setminus\sigma_2(C_4)=\{J\ne0\}
\tag{2.2}
\]

is the parameter space of point centers yielding embedded smooth rational
quartics. The same projection criterion is Bernardi's Proposition 2.8.

In characteristic zero the alternating form on a two-dimensional vector
space identifies its fourth symmetric power projectively with the dual
fourth symmetric power, with the appropriate binomial factors. Under this
identification a dual-coordinate point can be written as the binary form

\[
f=a s^4+4b s^3t+6c s^2t^2+4d st^3+e t^4.
\]

Reversal and alternating signs in an equivariant self-duality do not change
the following invariant values. Set

\[
I=ae-4bd+3c^2,\qquad
J=ace-ad^2-b^2e-c^3+2bcd.
\tag{2.3}
\]

Thus $J$ is the catalecticant determinant, and the discriminant has the
normalization

\[
\Delta=I^3-27J^2.
\tag{2.4}
\]

The invariant ring in characteristic zero is $k[I,J]$, of generator degrees
two and three; this standard fact and the normalization are recorded in
Isaev, Section 3. Localizing at $J$, its degree-zero subring is

\[
(k[I,J,J^{-1}])_0=k[z],\qquad z=I^3/J^2.
\tag{2.5}
\]

Consequently the good GIT quotient of $U$ is $\mathbf A^1_z$. The statement
is about the coarse invariant quotient. The quotient stack
$[U/\operatorname{PGL}_2]$ retains stabilizers and distinct nonclosed orbits;
it is a more faithful moduli object for the projected embeddings up to
ambient projectivity. That interpretation follows because a projective
equivalence between two embedded quartics restricts to an automorphism of
their parameter lines and hence identifies their four-dimensional
hyperplane systems, and conversely such an identification induces the
ambient projectivity.

## 3. Our center is a special orbit, not a singular projected curve

The subsystem

\[
V=\langle s^4,s^3t,st^3,t^4\rangle\subset W
\]

has annihilator $[0:0:1:0:0]$. Under the characteristic-zero self-duality
its binary form has two double roots, so it belongs to the orbit of
$s^2t^2$. For $f=s^2t^2$, one has $c=1/6$, $I=1/12$, $J=-1/216$,
and therefore

\[
J\ne0,\qquad \Delta=0,\qquad z=27.
\tag{3.1}
\]

The double-double orbit has dimension two and stabilizer the normalizer of
the torus fixing the two root points. It is closed **inside the semistable
locus**, not inside the full projective space: coalescing its two root
points tends to a quadruple-root, unstable form. There is one other strictly
semistable orbit, represented by $s^2(s^2+t^2)$. It has a unique double
root and two simple roots; its dimension is three and its closure contains
the double-double orbit. These are exactly the two orbits specified in
Isaev, printed p. 476. This is the precise meaning of the unique closed
strictly semistable orbit here.

Both representatives have nonzero catalecticant: in the one-double-root
example, $a=1,c=1/6,e=b=d=0$ still gives $J=-1/216$. Thus both yield
smooth embedded projected quartics and both have $z=27$, although their
centers are inequivalent. The coarse quotient is not an orbit
classification at that value. Four distinct roots are stable and are
classified by their unordered root cross-ratios; in $U$ their quotient
values satisfy $z\ne27$. Squarefree centers with $J=0$ are excluded from
$U$ because they lie on the secant hypersurface.

This distinction is the useful moduli lesson: **a multiple root of the
binary form representing a projection center does not imply a singular
projected quartic**. The discriminant detects collisions in the auxiliary
root divisor of the center; the catalecticant detects failed secant and
tangent separation. Our curve lies on a special orbit for the first
notion while remaining in the open embedding locus for the second.

There is also a concise moduli characterization of this orbit. **Our
quartic is the unique projective-equivalence class of smooth embedded
rational quartics in $\mathbf P^3$ with positive-dimensional projective
automorphism group.** Such a curve is nondegenerate: a smooth plane quartic
has genus three. Every such embedding is therefore a point projection of
$C_4$, because its complete degree-four system has dimension five. A binary
quartic with at least three distinct roots has finite stabilizer: its
stabilizer acts on a finite root set, with kernel fixing three points of
$\mathbf P^1$ and hence trivial. With at most two distinct roots, the
possible multiplicity types are $(4)$, $(3,1)$, and $(2,2)$. The first
two have $J=0$ (substitute $s^4$ or $s^3t$ into the catalecticant), so
cannot give an embedding. The remaining type is exactly our orbit.
Restriction of ambient automorphisms to the curve has trivial kernel
and image the center stabilizer, as proved in the projection note, so
this root argument establishes both directions of the characterization.

## 4. Brief characteristic-two outlook

Now let $k$ be algebraically closed of characteristic two. Keep the actual
subsystem $V\subset W$ and its dual center, rather than reducing the
characteristic-zero binary-form identification. The natural identification
$(\operatorname{Sym}^4 E^\vee)^\vee\cong\operatorname{Sym}^4 E$ uses
binomial/factorial normalizations in characteristic zero; in characteristic
two it must be replaced by divided-power language. In particular, a
fourth power $(as+bt)^4$ has only its two endpoint monomials. The literal
binary form $s^2t^2$ is therefore not a valid substitute for the dual center
without a new representation-theoretic argument.

The map $[s:t]\mapsto[s^4:s^3t:st^3:t^4]$ remains a closed immersion:
on $s\ne0$, the coordinate $u=t/s$ itself occurs among the affine image
coordinates, and the reverse chart gives $s/t$. It remains the graph of
$u\mapsto u^3$ on the same smooth Segre quadric. The latter map is separable
in characteristic two, with its two totally ramified endpoints.

Even its subgroup preserving $V$ does not automatically become larger or
nonreduced. For an invertible matrix
$g=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ acting by substitution on $s,t$,
the middle coefficients of the four basis sections are

\[
0,\quad ab\det(g),\quad cd\det(g),\quad0.
\tag{4.1}
\]

Since $\det(g)$ is invertible, the stabilizer in $\operatorname{GL}_2$ is
cut out by $ab=cd=0$. On the open set $ad\ne0$ this means $b=c=0$;
on $bc\ne0$ it means $a=d=0$. These two opens cover the stabilizer,
because $ad+bc$ is invertible. It is therefore the disjoint union of the
diagonal and antidiagonal tori, scheme-theoretically. Passing to scalars
gives the same smooth torus normalizer in $\operatorname{PGL}_2$.

The order-two subgroup $\mu_2$ inside the torus is, however, nonreduced;
its only geometric point is the identity. The characteristic-zero central
element $u\mapsto-u$ specializes to the identity. This collapse is not an
enlargement of the reduced automorphism group.

For the symmetric square, the divisor represented by
$h=\alpha s^2+\beta st+\gamma t^2$ doubles to $h^2$. Its missing middle
coefficient is $\beta^2$. Hence the incidence condition becomes the
nonreduced double line

\[
\mathcal B=V(\beta^2)\subset\mathbf P^2.
\tag{4.2}
\]

The reduced diagonal is $V(\beta)$: over $k$, every quadratic with zero
mixed coefficient is a square. Its parametrization
$[s:t]\mapsto[t^2:0:s^2]$ is inseparable. Thus the polynomial expression
$\beta^2-4\alpha\gamma$ now cuts out a double line, whereas the actual
reduced image of the diagonal in $\operatorname{Sym}^2\mathbf P^1$ is a
line. One must distinguish that image from the characteristic-zero conic
and its scheme-theoretic flat specialization.

For finite $u\ne0$, Hasse derivatives of
$c(u)=(1,u,u^3,u^4)$ span its ordinary order-two jet plane. The latter is

\[
H_u=V(x_3+u^4x_0),\qquad H_u|_C=4c(u).
\tag{4.3}
\]

Indeed, the section is $(z+u)^4$. At either endpoint, the second Hasse jet
drops rank, but the unique contact-four plane still has this limiting
formula. The osculating-plane map has reduced image the line of planes
$Ax_0+Dx_3=0$ and is purely inseparable of degree four onto it. Every point
has contact four, and there are no two distinct double-contact points in
one hyperplane section. These direct identities explain why reducing
$\rho+\rho^{-1}=-4$ cannot preserve the characteristic-zero two-partner
picture. No classification of the nonreduced correspondence or of
positive-characteristic projection moduli is claimed here.


The positive-characteristic STCI constructions for the fixed curve are proved [separately](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier); no binary-form orbit classification is substituted for that construction.



## Consolidated historical supplement: `research/supplements/QUARTIC_SINGULAR_SUPPORT_AND_SINGLETON_FIBERS.md`

# Reduced singular support and singleton normalization fibers

Let k be algebraically closed of characteristic zero. A quartic here means
a geometrically integral X in P3, and Sigma denotes the **reduced curve
support** of Sing(X), not its Jacobian or conductor scheme. The first
three propositions apply to any such quartic. The singleton-Hessian
argument applies to an integral hypersurface surface at its stated local
hypotheses; the conductor-contact consequence applies to a smooth integral
curve along which the carrier is generically regular. Only the final MF6
application specializes to fixed C0. These independently accepted bounded
statements distinguish reduced support from thick schemes; they do not
establish a general residual component or an unrestricted STCI obstruction.

## 1. The reduced curve support has degree at most three

**Proposition.** For an integral quartic X, deg(Sigma) <= 3. If X is
nonnormal, Sigma is nonempty, so 1 <= deg(Sigma) <= 3.

Choose a general plane H. Bertini irreducibility makes Y=X intersect H
geometrically irreducible; Bertini smoothness on X_reg makes Y smooth
at its generic point. The plane hypersurface Y is Cohen--Macaulay, so
irreducibility plus generic reducedness makes it integral. The plane
can simultaneously avoid the isolated singular points of X, the
finitely many singular points and component intersections of Sigma,
and be transverse to every component at each point of H intersect
Sigma. Consequently H intersect Sigma consists of exactly deg(Sigma)
distinct geometric points. For the Bertini inputs, see the primary
[Stacks irreducibility theorem](https://stacks.math.columbia.edu/tag/0G4C)
and [smoothness theorem](https://stacks.math.columbia.edu/tag/0FD4).

Every one of those points is singular on Y: all ambient first
derivatives of its quartic equation vanish there, hence the two plane
derivatives vanish. Let nu_Y:Y_tilde -> Y be the finite normalization.
The exact sequence

    0 -> O_Y -> (nu_Y)_* O_Y_tilde -> T -> 0

has T of finite length, with length at each singular point at least
one. (An integral curve over this perfect field is regular exactly
where it is normal.) Both proper integral curves have H0=k. Taking
Euler characteristics gives

    p_a(Y) = g(Y_tilde) + length(T).

The arithmetic genus of a plane quartic is three, directly from
0 -> O_P2(-4) -> O_P2 -> O_Y -> 0. Hence

    deg(Sigma) <= length(T) <= 3.

An integral hypersurface is S2. If it were regular in codimension one,
Serre's criterion would make it normal. Thus a nonnormal quartic has a
singular curve component. This proves the lower bound.

If deg(Sigma)=3, the same proof gives g(Y_tilde)=0 and exactly delta=1
at each of the three general singular section points. It does not
identify the global normalization, classify special fibers, or bound
the degree of the Jacobian scheme.

**Irreducible-support corollary.** If Sigma is irreducible of degree
three, it is a smooth twisted cubic. Section 2 excludes the planar
case. For a nonplanar integral degree-three curve, pull O(1) to the
smooth normalization Z. The resulting line bundle L has degree three
and at least four independent sections, since the four ambient
coordinates are linearly independent on a nondegenerate curve. If Z
had positive genus, every effective divisor of degree d>0 would have
h0 at most d: h0(O_Z(p))=1 for any point p (a second section would give
a degree-one map to P1), and adding the other d-1 points increases h0
by at most one each. A nonzero section of L supplies such a divisor,
contradicting h0(L)>=4. Hence Z=P1, L=O(3), and the four coordinates
give the complete degree-three embedding. The image is consequently
a smooth twisted cubic. Reducible degree-three support is not covered
by this irreducible corollary.

## 2. Every reduced planar cubic singular support is impossible

**Proposition.** If a quartic form F has all its first derivatives
vanishing on a reduced planar cubic C, then its plane equation divides
F. More precisely, after writing the plane as z=0 and its squarefree
cubic equation as g(x0,x1,x2)=0, one has

    F = z (lambda*g + z*Q2).

In particular an integral quartic cannot have such a cubic in its
singular support.

Write

    F = A4(x0,x1,x2) + z*B3(x0,x1,x2) + z^2*Q2(x0,x1,x2,z).

Support containment gives g|A4, g|partial_i(A4) for i=0,1,2,
and g|B3 from the normal derivative partial_z F. If an irreducible
factor q of g occurs only once in a nonzero A4=q*a, choose a nonzero
partial_i q. Its degree is smaller than deg(q), so q does not divide
partial_i q. Reducing partial_i A4 modulo q gives

    partial_i A4 = (partial_i q)*a mod q,

which is nonzero in the domain k[x0,x1,x2]/(q), a contradiction. Each
factor of the squarefree g therefore occurs at least twice in A4.
Thus g^2|A4; degree six exceeds degree four, so A4=0. Since g and B3
have the same degree, B3=lambda*g, giving the displayed formula.

This treats irreducible cubics (including singular cubics), a conic
and line, and three distinct lines with any planar arrangement. It
also gives the ordinary-ideal certificate

    F in (z^2,z*g)_4 = (I_C^2)_4.

No symbolic-power equality or unproved absence of embedded primes is
needed. A repeated or embedded thickening of the Jacobian scheme does
not affect the support-based proof. A **nonreduced degree-three plane
scheme whose reduced support has degree one or two** is outside this
cubic assertion. In particular, a Jacobian scheme of degree three is
not itself evidence of a reduced planar cubic.

The subagent planar_cubic_audit supplied a separate complete factor
argument and reached the same exact formula. Agreement supplements
the written proof; it is not substituted for it.

### Complete reduced degree-three support list

**Corollary.** If the reduced singular curve support Sigma has degree
three, it is connected and nonplanar. Its underlying reduced curve
has one of exactly four forms:

1. A smooth twisted cubic.
2. A smooth plane conic together with a line outside its plane,
   meeting the conic.
3. A chain of three lines, with the two endpoint lines skew.
4. Three concurrent lines spanning P3.

This is a list of possible reduced supports, not an existence claim
for quartics realizing every entry, and not a conductor-scheme
classification.

Nonplanarity follows from the proposition above. The irreducible case
is the corollary in section 1. An irreducible degree-two component is
a smooth plane conic: normalization and the degree-two line-bundle
section bound exclude a nondegenerate embedding in P3, and a reduced
integral plane conic is smooth over this field. Thus the only other
degree partitions are a conic plus a line, or three distinct lines.

Suppose a line L is disjoint from a conic K in its plane P. Double
vanishing of F on the reduced conic gives

    F|P = lambda*q2^2,

by the same irreducible-factor derivative proof used above. The line
cannot lie in P, and its intersection p with P is off K. Since
F(p)=0, lambda=0 and P divides F, contradicting integrality. Therefore
the conic-plus-line case is connected. If the line also lay in the
conic's plane, their union would be the forbidden planar cubic.

For three lines, if one pair intersects and the third is disjoint
from that pair, let P be the plane of the intersecting pair and let
q2 be their squarefree degree-two product. Again F|P=lambda*q2^2.
The third line meets P at a point off the pair, forcing lambda=0 and
a plane factor. Thus this disconnected case is impossible.

If the three lines are pairwise skew, put them by a projective change
of coordinates into

    L1: x2=x3=0,
    L2: x0=x1=0,
    L3: x2=x0, x3=x1.

They lie on the smooth quadric Q: x0*x3-x1*x2=0, and they are in the
same ruling. The restriction of the quartic to Q has class (4,4).
Because F and all its first derivatives vanish on each line, its
restriction vanishes to order at least two along each line. If this
restriction were nonzero, subtracting those three doubled ruling
lines would give a section of O_Q(-2,4), which has no sections.
Therefore Q divides F, another contradiction. This removes the last
disconnected three-line case.

Connected nonplanar three-line arrangements are precisely a chain
with skew endpoints or three concurrent lines spanning P3. Three
pairwise intersecting lines with three distinct intersection points
are a planar triangle and were already excluded. This exhausts the
list. The independent planar_cubic_audit subagent checked the
disconnected cases, the smooth-quadric restriction, and the line
incidence exhaustion without finding a gap.

## 3. The Jacobian scheme can have larger degree

For a concrete distinction, take

    F = x^2*z^2 + y^3*w.

This quartic is integral: viewed as a polynomial in w it is primitive
and linear over k[x,y,z], with coprime coefficients y^3 and x^2*z^2;
Gauss's lemma gives irreducibility. Its derivatives give the Jacobian
ideal, up to nonzero constants,

    (x*z^2, y^2*w, x^2*z, y^3).

The reduced singular support is the union of the two lines
(x,y)=0 and (y,z)=0, of degree two. At the first line's generic point,
z and w are units and the Jacobian ideal is (x,y^2), of length two.
At the second, x and w are units and it is (z,y^2), also of length two.
Thus the one-dimensional Jacobian scheme has degree four. Embedded
points, if present, do not change this leading degree computation.
The degree-at-most-three theorem must not be applied to that scheme.

## 4. A nonnormal singleton-fiber surface point has Hessian rank at most one

**Local proposition.** Let x be a closed point of an integral
hypersurface surface X over k, and let nu:S -> X be its finite
normalization. If X is nonnormal at x and nu^{-1}(x) has exactly one
point, the rank of the local hypersurface Hessian at x is at most one.

Suppose instead that the rank is at least two. Formal splitting in
characteristic zero puts the completed local equation into the form

    u*v + g(w),  g in k[[w]].

One can obtain this with the formal implicit function theorem for two
variables with invertible quadratic Hessian block, followed by the
formal Morse lemma with parameter w. This uses a formal coordinate
change and multiplication by a unit; it does not require convergent
or analytic coordinates. A primary precise statement allowing
non-isolated singularities is [Greuel--Pfister, The Splitting Lemma in
any Characteristic, Theorem 2.1(2)](https://arxiv.org/html/2507.17078v2).
If g is nonzero, its derivative is also
nonzero. The hypersurface is Cohen--Macaulay and its singular support
is isolated (the derivatives are v,u,g'(w)). It is therefore normal
by S2+R1. Normality of the completion descends along the faithfully
flat map to the completion, so X is normal at x, a contradiction.

If g=0, the completed ring is

    A_hat = k[[u,v,w]]/(u*v),

with two nonzero zero divisors u and v. Set A=O_X,x and let B be its
finite normalization algebra. The singleton fiber means B has just
one maximal ideal, so it is a local normal ring. Rings essentially
of finite type over a field, their localizations, and finite algebras
over them are excellent. Exact completion of the finite injection
A -> B gives an injection

    A_hat -> B tensor_A A_hat = B_hat.

Here completion at the maximal ideal of B agrees with completion at
m_A*B because the two adic topologies are equivalent for a finite
local algebra. The completed local ring B_hat is normal, hence a
domain. A ring with the displayed nonzero zero divisors cannot inject
into a domain. This is the required contradiction. The exact
excellence inputs are [Stacks Proposition 15.53.3 and Lemmas
15.53.2](https://stacks.math.columbia.edu/tag/07QS) and the precise
[normal-completion Lemma 15.53.6](https://stacks.math.columbia.edu/tag/0C23).

This argument avoids treating formal branch counting as automatically
equal to normalization fiber counting, and avoids any unqualified
claim that normalization commutes with arbitrary completion.

At a singular point, Hessian rank is invariant under regular or
formal coordinate changes and multiplication of the equation by a
unit. For a homogeneous equation, Euler's identity places the radial
vector in the Hessian kernel once all first derivatives vanish.
Thus the rank of the homogeneous four-variable Hessian at a
projective representative equals the rank of the three-variable
Hessian in any affine chart.

## 5. A mate forces a conductor intersection with Hessian rank at most one

**Global proposition.** Let X be an integral nonnormal hypersurface
surface in P3 and C a smooth integral projective curve in X, with X
regular at the generic point of C. If a hypersurface mate cuts out C
set-theoretically on X, then some point x in C where X is nonnormal
has Hessian rank at most one.

Let G be a mate and b its degree, with nu:S -> X the finite
normalization and H=nu^*O_X(1), an ample Cartier divisor. The full
inverse support of C is the support of the nonzero effective Cartier
divisor defined by nu^*G. Because nu is an isomorphism at the generic
point of C, there is just one curve c above C. Its finite birational
map to the smooth curve C is an isomorphism. The zero support of a
nonzero section of a line bundle on a normal surface is pure of
codimension one, so no isolated inverse-image point can remain.
Hence

    (nu^{-1}(C))_red = c,  nu|c:c -> C is an isomorphism,
    div(nu^*G) = m*c linearly equivalent to b*H

for a positive integer m. In particular every fiber over C is a
singleton. When deg(X)=deg(C)=4, intersecting with H gives m=b.

Since X is an S2 nonnormal hypersurface, its nonnormal locus contains
a curve. Choose a prime curve D on S in the inverse image of that
locus. It is distinct from c, since X is regular at the generic point
of C. Restrict the section defining m*c to D. It is a nonzero section
of O_D(b*H), which has positive degree by ampleness. It must have a
zero: pull the restricted section to the smooth normalization of
the integral curve D, where this is the ordinary positive divisor
degree statement. Therefore c intersects D, even if S is singular at that
intersection and even if c is only a Weil divisor: m*c is Cartier,
which is all the restriction argument uses.

The image x of such an intersection is nonnormal on X and has a
singleton normalization fiber. Section 4 now gives Hessian rank at
most one. No smoothness hypothesis on the normalization, no ADE
assumption, and no reducedness hypothesis on the conductor is used.
Here singleton means a singleton underlying set; no assertion that
the finite scheme fiber is reduced is needed. The independent
planar_cubic_audit subagent also audited sections 4--6, including the
finite-algebra completion topologies and the Cartier restriction,
and found no substantive gap.

Consequently, an exact computation showing that C has **no** singular
point of X at which all two-by-two Hessian minors vanish excludes a
mate in every degree. The condition is necessary; the existence of
a rank-at-most-one point does not establish a mate.

## 6. First-normal consequences and the defect-chart boundary

At a point of \(C=(y,m)\) with local curve parameter \(z\), suppose the first normal equation is \(h(z)m\). Then
\[
F=h(z)m+a(z)y^2+b(z)ym+c(z)m^2+O((y,m)^3).
\]
The carrier is singular there precisely when \(h=0\). Its Hessian at a zero of \(h\), in coordinates \((z,y,m)\), is
\[
\begin{pmatrix}0&0&h'\\0&2a&b\\h'&b&2c\end{pmatrix}.
\]
A simple zero gives the nonzero minor \(-(h')^2\), contradicting the rank-at-most-one condition from §5 for a nonnormal carrier with a mate. Thus **\(h\) must have a repeated zero**, invariant under regular normal-frame changes. At such a zero the additional rank condition is \(4ac-b^2=0\). It reduces to \(b=0\) only when an independently established contact identity gives \(a=0\). In particular \(a=\Gamma h/\delta\) cannot be specialized at a zero of \(\delta\) without a completed two-chart identity. A proposed \(\gcd(h,h',b)\) filter must therefore retain all defect points; the homogeneous Hessian-minor test has no such denominator restriction.

These are necessary singularity/contact conditions, not a finite-locus theorem or an exclusion of surviving quartic fibers. The reduced plane-section degree bound does not bound a thick Jacobian scheme. The singleton-fiber Hessian argument uses characteristic-zero formal splitting and actual finite normalization; in positive characteristic its separability and coefficient hypotheses require fresh verification. The [positive-characteristic construction](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) remains valid.

