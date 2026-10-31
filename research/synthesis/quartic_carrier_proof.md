# Why a degree-four carrier cannot have a mate

Work over an algebraically closed field of characteristic zero and fix
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]
The accepted theorem [R-0001](../results/quartic_carrier_exclusion.md) is:
for every **integral quartic** \(X\supset C\) and every homogeneous form
\(G\) of positive degree, \(V(X,G)_{\rm red}\ne C\).
There is no restriction on the mate degree, the normal order of its
equation, the singularities of the normalization, or the conductor scheme.
The unrestricted existence question for two degrees at least five remains
open. The [quartic-pair proof](quartic_pair_obstruction.md) is a separate,
narrower argument and is not used to assert this all-degree theorem.

The characteristic boundary is substantive: **in every characteristic
\(p>0\), this same embedded curve is an STCI using a quartic carrier**.
The [characteristic construction and exact fixed-carrier mate degrees](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier)
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

The following useful strengthening isolates the part independent of any
mate or special projection.

**Ruled-surface criterion.** Let \(M\) be a smooth projective surface in
characteristic zero, and \(L\) a nef divisor of positive square \(d\),
with \(K_ML=2\pi-2-d<0\). Suppose \(M\) contains a rational curve of
\(L\)-degree \(\delta\). If
\[
\delta(d+2-2\pi)>d,                                  \tag{3}
\]
then \(M\) is rational.

**Proof.** The negative intersection excludes effective positive powers
of \(K_M\), so the surface classification makes \(M\) rational or
birationally ruled. If the minimal ruling has base genus \(g\ge1\),
write its nef pushdown as \(L_0=aC_0+bf\), with \(C_0^2=-e\), and
use total-transform exceptional classes for all point blowups:
\[
L=\tau^*L_0-\sum m_iE_i,
\quad d=a(2b-ae)-\sum m_i^2,
\quad 2\pi-2-d=a(2g-2+e)-2b+\sum m_i.
\]
Nefness descends at every blowdown. At each center a component of the
actual ruling fiber has \(L\)-degree at most \(a\); its strict transform
remains nef against the next pushdown. Thus \(0\le m_i\le a\), including
infinitely near centers. Eliminating \(b\) gives
\[
d=(2g-2)a^2+(d+2-2\pi)a+\sum m_i(a-m_i).
\]
The last sum is nonnegative. Any rational curve maps constantly to the
positive-genus base, so its degree is at most the degree \(a\) of an
entire fiber. Hence \(d\ge(d+2-2\pi)a\ge(d+2-2\pi)\delta\),
contradicting (3). \(\square\)

For a nonnormal quartic, \(d=\delta=4\) and \(\pi\le2\), so (3)
always holds. The normalization is rational **before** a mate is assumed.
It does not apply to normal quartics: their \(\pi=3\) makes its key
coefficient zero. This explains one necessary boundary in the proof.

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
[the cycle checker](../computations/verify_session_normal_carrier_progress.py)
and [its independently reconstructed checker](../computations/verify_session_normal_independent_audit.py).
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

[The exact tree checker](../computations/verify_session_normal_nonreduced_trees.py)
generates free trees by leaf addition, weak diagonal excesses of total at
most three, and exact rational solutions of (7). Its
[independent reconstruction](../computations/verify_session_nonreduced_independent_audit.py)
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
[\((4,5)\) proof P-040](../supplements/QUASIPRIMITIVE_MULTIPLICITY_FIVE.md#p-040).
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
[the genus-zero proof](../supplements/SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md).

The two scrolls use the actual conductor, an ACM cubic scheme, and its
generic Artin algebras. Reduced conic-plus-line and three-line cases,
Gorenstein thick lines, fat triple lines, and nongorenstein doubled-line
crossings require different local algebra, all covered in the
[entire-scroll proof](../supplements/QUARTIC_SCROLL_NONREDUCED_CONDUCTORS.md).
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
The [classification and exact conductor-jet proof](../supplements/VERONESE_QUARTIC_PROJECTIONS.md)
retain these three distinct obstructions.

For the cone \(S(0,4)\), \(\operatorname{Cl}(S)=\mathbf Z[f]\) and
\(H=4f\), so (1) forces \(c\sim H\), hence \(c\) Cartier and disjoint
from the vertex. On its \(\mathbf F_4\) resolution it is a ruling
section. The original projection is a cone over a rational plane quartic.
A multibranch base point violates full inverse support; a singleton
singular branch has vanishing base derivative. Differentiating the actual
unit-times-power mate identity along this kernel makes the section tangent
to the kernel, contradicting immersion of \(c\to C\). The
[complete cone calculation](../supplements/SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md#3-the-singular-minimal-degree-cone-is-excluded-in-every-mate-degree)
also shows why a numerical class calculation alone is insufficient.

## 5. Sectional genus one: a permitted ribbon with incompatible projection

Adjunction and minimality force \(K_M=-L\); the normalization is the
degree-four ADE del Pezzo anticanonical model in \(\mathbf P^4\).
The \(D_5\) exceptional-lattice saturation argument gives actual
\(2c\sim2H\), not merely \(2[c]=2[H]\) numerically. The
[root-lattice proof](../supplements/OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-delpezzo-d5-torsion-filtermd)
and [del Pezzo reduction](../supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
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
[complete conormal-net proof](../supplements/GENUS_ONE_RIBBON_CONORMAL_NET_PROOF.md).

The actual two-quadric normalization can be written
\(z^2-Az-R_1=Lz+R=0\). Elimination gives
\(R^2+ALR-R_1L^2=0\), and the entire conductor is \((L,R)\), including
nonreduced conics. Its full algebra is derived by the
[graded-module conductor proof](../supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-entire-conductor-algebra-independent-auditmd).
For quadrics \(Q_1,Q_2\) normalized to have middle-square coefficients
one and zero, respectively, the omitted-coordinate derivatives satisfy
\[
\operatorname{rad}(D_{Q_2})\mid D_{Q_1},\qquad
D_d=d_0s^4-d_1s^3t-2d_3s^2t^2-d_4st^3+d_5t^4.         \tag{9}
\]
This is support divisibility, not a multiplicity assertion.

The five root partitions of the nonzero binary quartic \(D_{Q_2}\)
are exhaustive. The squarefree case is excluded by (8)--(9) and the
[actual projection fiber test](../supplements/GENUS_ONE_UNIFORM_PROJECTION_ANALYSIS.md).
The [\([2,1,1]\) proof](../supplements/GENUS_ONE_211_PROJECTION_PROOF.md)
uses the exact double fiber and the forced extra derivative zero.
For \([4]\) and \([3,1]\), the full net forces a line of singularities,
contrary to normality. The \([2,2]\) case reduces to one pencil whose
quadratic conductor trace and norm forbid **every** descended positive
power. The [complete repeated-partition proof](../supplements/GENUS_ONE_RIBBON_PARTITION_PROOFS.md)
retains the invisible coefficient \(d_2\), all determinant roots, and
the direction boundary. Its
[independent ideal certificates](../supplements/GENUS_ONE_RIBBON_PARTITION_INDEPENDENT_CERTIFICATES.md)
remain necessary exact support. General \(\mathrm{PGL}_2\) moves the
projection center and cannot be substituted for its center-preserving
orbit calculation.

## 6. Sectional genus two: conic geometry and the two correction strata

The [adjoint proof](../supplements/OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-two-adjoint-conic-modelmd)
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

The [entire-conductor theorem](../supplements/GENUS_TWO_ENTIRE_CONDUCTOR_PROOF.md)
identifies the actual downstairs conductor as a reduced line \(\Gamma\)
and its upstairs quadratic algebra, including split and nonreduced
covers. The
[ambient blowup proof](../supplements/GENUS_TWO_AMBIENT_CONIC_MODEL_PROOF.md)
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
[complete bisection proof](../supplements/GENUS_TWO_BISECTION_PROOF.md)
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
The [exact carrier-ideal proof](../supplements/GENUS_TWO_TRISECANT_CARRIER_PROOF.md)
gives the whole eleven-dimensional quartic space, rather than a sampled
family. The marked-plane analysis forces a special horizontal prime
\(B^2=-3\) disjoint from \(\widetilde c\); the
[free-chain argument](../chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md#19-genus-two-marked-section-case)
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
The [nonendpoint proof](../supplements/GENUS_TWO_NONENDPOINT_PROOF.md)
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
The [endpoint proof](../supplements/GENUS_TWO_ENDPOINT_PROOF.md) and
its linked local calculations retain the actual equations proving these
positions. An abstract ADE graph with the right square is insufficient.

## 7. Exhaustion, useful alternatives, and what remains unproved

Normality and the three nonnormal sectional genera exhaust all integral
quartics. Equation (10) exhausts genus two, and its actual line positions
exhaust the section stratum. The genus-one five partitions are exhaustive
only after the complete embedding and its fixed projection center are
derived. Thus all mates on every integral quartic are excluded, at exactly
the accepted scope of R-0001.

The necessary case distinctions reflect different objects. Numerical
pullback works on a normal resolution; conductor descent measures gluing
on the nonnormal carrier; the ribbon obstruction measures a **global
embedded** normal map; the trisecant argument measures actual branch
attachments in an ambient blowup. They share (1)--(2) but cannot be
identified by discarding their extra data. The ruled criterion and the
ribbon Hom boundary above generalize the common reductions. The
rank/order inequality unifies irreducible normal exceptional cases, and
the relative inverse-chain formula unifies both ordinary two-crossing
trisecant configurations. The doubled-horizontal case remains distinct
because its cubic normal coefficient, rather than two reduced crossings,
controls its entire exceptional budget.

Two useful negative controls prevent false simplifications. A smooth
lift can pass through an \(A_1\) normalization point with full inverse
support and a local mate; the
[explicit local counterexample](../supplements/OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-singular-local-liftmd)
prevents replacing the singular-normalization analysis by smoothness of
the curve. Full inverse support also does not imply scheme containment
in the nonreduced ramification locus; the
[Fitting counterexample](../supplements/OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-ramification-scheme-counterexamplemd)
retains the exact failed implication. Similarly a blowup lift in another
carrier family requires an invertible pulled center ideal and the actual
ratios of its equation sections; a numerical conic-bundle model alone
does not provide them.

The independent \((4,4)\) proof, the primitive \(e=2\) factorization,
the principal MF6 finite candidate locus, and the even/three-center
bisection proofs remain worthwhile distinct mechanisms. Their old
quartic-*mate* open labels are superseded by R-0001. The theorem does
not compute common-quartic ancestor incidence, rule out arbitrary sextic
mates, or turn a formal/graded normal model into actual homogeneous
equations.

## 8. What changes in positive characteristic

These boundaries concern each argument, not merely its theorem label.
The construction linked at the start supplies an actual quartic-carrier
control in **every** positive characteristic.

| Mechanism | What carries over | What the characteristic-zero proof still needs |
|---|---|---|
| Plane-section defect, full inverse support, smooth passage | The genus inequality, purity, normalization over a smooth curve, uniformizer argument and divisor-degree equality work in any characteristic under the stated integral/smooth hypotheses. | These reductions alone give no contradiction; they hold for positive-characteristic examples too. |
| Ruled intersection identity | Once a smooth ruled model and nef pushdowns are given, the total-transform calculation and \(0\le m_i\le a\) use only intersection theory. | The rationality criterion above invokes the characteristic-zero surface classification; no broader classification theorem is imported silently. |
| Numerical pullback and actual ideal vanishing | On an available smooth resolution of a normal surface, the negative matrix and principalized-ideal argument retain their algebraic meaning. | A Cartier index does not control its correction. The classification, first-normal budgets and small-mate exclusions used to finish the normal-quartic case have separate characteristic hypotheses. |
| Rational-resolution compression | Numerical-to-linear equivalence on smooth rational surfaces and ambient hypersurface section lifting do not require characteristic zero. | Compression can produce an allowed positive-characteristic mate; the normal scan's low-degree exclusion inputs cannot simply be reused there. |
| Ribbon and normal-map bound | A pure CM double with smooth reduction is a ribbon in every characteristic; its nilideal degree and the Hom calculation remain valid whenever their global inputs hold. | The fixed conormal computation uses determinant eight. It yields \(\mathcal O(-7)^2\) for \(p\ne2\); characteristic two has \(\mathcal O(-6)\oplus\mathcal O(-8)\), so the \(\mathcal O(-8)\) contradiction fails there. Neither splitting proves that the genus-two Cartier double exists for an arbitrary carrier. |
| Generic differential and conductor-power descent | Differentiating \(u f^b\) gives the same formula when \(b\) is nonzero in the field. | Cancellation at a conductor meeting uses that scalar. In characteristic \(p\mid b\) it vanishes. Frobenius also kills nilpotent conductor obstructions, whereas in characteristic zero the nilpotent unit group is additive and has no nonzero finite-order element. |
| Degree-two trace, involution and local Morse splitting | The quadratic trace decompositions, formal square roots of units, and parameter-preserving splitting work with the required invertibility of two and separability. | They are not proofs in characteristic two. Rationality, cohomology, actual ambient-model and branch hypotheses also need proof in a new characteristic. |
| Fixed-embedding trisecants | The equation \(t^3-as^3\) and the carrier-ideal calculation retain their algebraic meaning. | The three-distinct-contact case needs \(3\ne0\). In characteristic three the ruling map on \(C\) is inseparable and every fiber is a triple contact; the nonendpoint support/branch-value proof cannot be imported there. |
| Global quartic surface bound | Direct blowup charts can often be read whenever their coefficients and two remain invertible. | The characteristic-zero \(h^{1,1}\)/Picard bound in the separate \((4,4)\) surface proof is not a positive-characteristic bound; local equations alone do not transport that global contradiction. |

In particular the odd-characteristic balanced conormal bundle does not
exclude the known positive-characteristic STCI. The missing implication
would be that every such pair produces the particular genus-two Cartier
double with its nonzero global normal map; the proof never establishes
that. The quartic-carrier construction instead uses a conductor descent
power divisible by the characteristic.

## 9. Review state

The case proofs and exact finite calculations reuse accepted independent
reviews of the same mathematical inputs. Independent consolidation review
reconstructed the new ruled criterion, common correction and compression,
normal proof, actual ambient lift, global ribbon and Hom obstruction, and
the complete nonendpoint/endpoint transfers; the replacement and precise
duplicate-source removals were accepted. It corrected the Jaffe citation
to Theorem B/11.11, specified the least common denominator in compression,
retained the independent matching/path-cofactor proof, and made the
characteristic-three trisecant boundary explicit.

The four unchanged normal graph computations were not rerun. Two repaired
primitive/incidence checkers received independent code/mathematical review
before targeted execution and both passed: the \(a=-1/2\) boundary proof
now states its \(x\ne0\) localization, and the quartic-incidence proof
correctly tests polynomial membership over \(\mathbf Q\) while allowing
rational constants. Neither generic rank controls nor these bounded
checks are promoted to a larger classification. The final successful
genus-one repeated-partition Macaulay2 proof source was restored from its
exact replay snapshot with identical SHA-256 bytes; no fresh execution
of that inherited certificate is claimed. No theorem promotion or
unrestricted STCI conclusion is made by the consolidation.
