# Global equation jets and their intrinsic source filtration

Fix an embedded curve, its polarization and its actual ideal sheaf. Compatible
jets on that embedded neighborhood are different from independently chosen
sections of its normal graded pieces. The finite filtered-cohomology argument
below measures their difference, gives global realization cutoffs, and computes
the fixed quartic's sextic source deficit. All powers are ideal **sheaf** powers;
homogeneous representatives require sheafification and saturation.

These are independently source-reviewed deductions from frozen
commit `aad349d1c413e0de511dd6b62c2194faf706fda9`, consolidated without a new
computation. General lemmas retain their stated fields
and hypotheses. The application is the characteristic-zero embedding
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), with exact rational computation
and geometric existence over \(\overline{\mathbf Q}\). The split-quadric cutoff
is characteristic free. Neither finite compatible jets nor their dimensions
supply a proper sole-support pair without its additional conditions.

## Intrinsic to which data?

STCI is a question about an embedding, so removing all embedding data would
remove part of the problem. The useful levels are:

| Retained data | Invariant information | Information not thereby determined |
| --- | --- | --- |
| Abstract curve \(C\) | Genus and abstract line bundles | Its homogeneous equations or normal neighborhood |
| \(C\), its polarization, and conormal bundle \(E\) | Normal graded pieces and their cohomology | Higher extension maps and obstruction differentials |
| Polarized embedded neighborhood \((C\subset X,L)\) through order \(N\) | Finite jet spaces, their restriction maps, and filtered-cohomology differentials | Global realization without an extension theorem |
| A flag \(C\subset S\subset X\) | Divisibility and recursive source constraints relative to that surface | A canonical choice of \(S\) when several surfaces are available |
| Spectral curve with two degree-two line bundles \((\Sigma,A,B)\) | The class \(BA^{-1}\), its torsion, and the pushforward splitting | The actual ambient lifting operator |
| Specified equations or elimination map | Its transverse algebra and degeneracy strata | Minimum complexity among all presentations of the same curve |

For an actual pair in an ambient projective space \(P\), a common input is
the labelled sheaf morphism
\[
\Phi:\mathcal O_P(-a)\oplus\mathcal O_P(-b)\longrightarrow I_C.
\]
Its two components are the homogeneous equations. Their images give the
carrier ideals \(I_X,I_Y\), and the total image gives \(I_Z\). The actual
source spaces constrain \(\Phi\); its filtered Koszul complex organizes
the intersection. Passing to a root on the blowup is a further construction
with its own hypotheses. This common input organizes the maps without
asserting that their obstruction theories are identical.

Charts and frames can be changed while transporting all these data.
Replacing a nonlinear transition by its linear part changes the object.
For example, extensions with graded pieces \(\mathcal O\) and
\(\mathcal O(-2)\) on \(\mathbf P^1\) can have connecting map
\(H^0(\mathcal O)\to H^1(\mathcal O(-2))\) of rank zero or one.
The split and nontrivial extension have identical graded pieces. This is
a filtered-sheaf control, not an assertion that every such extension is
realized by a prescribed projective embedding.

## Keep the actual diagram and distinguish its spectral sequences

Put \(P=\mathbf P^3\) and \(I=\mathcal I_C\). For two actual hypersurfaces
\(X=V(F_a)\), \(Y=V(G_b)\) with \(C\subset X\cap Y\), put
\(A=\mathcal I_X\), \(B=\mathcal I_Y\), and
\(J=A+B=\mathcal I_Z\), where \(Z=X\cap Y\) is the scheme intersection.
The input is the diagram of inclusions

\[
\begin{array}{ccccc}
&&I&&\\
&&\uparrow&&\\
A&\longrightarrow&J&\longleftarrow&B,
\end{array}
\qquad A,B\subset J\subset I\subset\mathcal O_P.
\]

Its ideal powers, restriction maps, and multiplication maps retain the
embedding. The [nine-embedding diagram](../normal-geometry/ideal_filtrations_quartic_exclusion.md#intrinsic-local-algebra-and-characteristic-zero-quartic-geometry)
section 2 already specifies the conormal maps and their bases. In particular,
for a proper hypersurface pair the central map is

\[
D=J/IJ\simeq\mathcal O_C(-a)\oplus\mathcal O_C(-b)
\longrightarrow E=I/I^2,
\]

with kernel \((J\cap I^2)/IJ\) and cokernel \(I/(I^2+J)\).
This map need not be injective. The whole diagram is not one long exact
sequence, and different embeddings have different ideal-power filtrations.

| Construction | What it computes | Information it must retain |
| --- | --- | --- |
| Carrier Koszul complex \(K(F,G)\), filtered along \(C\) | Cancellations that create full initial equations of \(J\) | Actual equations and filtration shifts; displayed first symbols need not generate the initial ideal |
| Koszul complex on local normal parameters, filtered on \(\mathcal O_P/J\) | Normal Tor pages and the comparison defect \(\Delta\) | Full initial algebra and induced filtration on \(J/IJ\) |
| Cech complex of \((I^r/I^{N+1})(d)\), filtered by normal order | Compatibility of global equation jets of fixed degree | Actual chart transitions, including their higher terms and the degree-\(d\) line-bundle transition |
| Successive Cartier-root lifting on the blowup | The root obstructions \(K_1,K_2,\ldots\) | Root equation, nonlinear base motion, units, corrections, and the relevant quotient sheaves |

The [carrier equation filtration](../normal-geometry/ideal_filtrations_quartic_exclusion.md#82-filtered-koszul-complexes)
and the [normal Koszul comparison](../normal_koszul_cancellation.md#normal-koszul-comparison-and-degree-bounds)
use different complexes. The exact comparison and its scoped review are
in [R-0030](../../results/local_filtration_comparison_defect.md).

For a regular hypersurface pair, \(\mathcal O_X\otimes^L\mathcal O_Y\)
already has no higher homology and equals \(\mathcal O_Z\). Its derived
restriction to \(C\) is a different operation. Neither operation alone
supplies the missing higher embedded gluing maps.

## The finite Cech filtration gives actual source-image obstructions

Let
\[
T_{r,N}(d)=(I^r/I^{N+1})(d),\qquad 0\le r\le N+1.
\]
Filter its Cech complex by
\(F^pT_{r,N}=(I^p/I^{N+1})(d)\) for \(r\le p\le N+1\).
Because \(C\subset P\) is a regular embedding, the graded pieces are
\(\operatorname{Sym}^pE\otimes\mathcal O_C(d)\). The finite filtration gives

\[
E_1^{p,q}=H^{p+q}\!\left(C,\operatorname{Sym}^pE(d)\right)
\Longrightarrow H^{p+q}\!\left(P,T_{r,N}(d)\right),
\qquad
d_s:(p,q)\longmapsto(p+s,q-s+1).
\tag{1}
\]

This is the usual [spectral sequence of a filtered complex](https://stacks.math.columbia.edu/tag/012K),
applied to the actual finite Cech complex. Only total cohomological degrees
zero and one occur on its first page. A proposed normal symbol survives
precisely when its successive gluing obstructions can be removed, with
choices of intervening corrections retained. Higher differentials depend on
the actual extensions, which the split conormal bundle by itself does not
determine. The spectral sequence retains the associated graded of the
answer; reconstructing an actual section also requires its compatible lifts.

More concretely, the short exact sequences
\[
0\to\operatorname{Sym}^nE(d)\to T_{r,n}(d)
\to T_{r,n-1}(d)\to0
\tag{2}
\]
give linear connecting maps
\[
\partial_n:H^0(T_{r,n-1}(d))
\to H^1(\operatorname{Sym}^nE(d)).
\tag{3}
\]
A compatible jet extends exactly when it lies in \(\ker\partial_n\).
The set of extensions is an affine space under
\(H^0(\operatorname{Sym}^nE(d))\). These are successive maps on already
compatible jets; they are not unrelated tests on independently chosen
graded symbols. Equation (1) repackages (2), including the ambiguity of
intermediate lifts.

## The source deficit is a canonical filtration, not a matrix size

Let \(C\subset X\) be a regular embedding of a proper curve, with ideal
\(I\), conormal bundle \(E=I/I^2\), and a specified line bundle \(L\) on
\(X\). Fix \(d\) and \(N\ge r\). Write
\[
T_{r,N}(d)=(I^r/I^{N+1})\otimes L^d,
\quad
S_{r,N}(d)=\operatorname{im}\left[H^0(T_{r,N}(d))
\to H^0(C,\operatorname{Sym}^rE\otimes L^d|_C)\right].
\]
Truncation gives canonical nested subspaces
\[
S_{r,r}(d)\supseteq S_{r,r+1}(d)\supseteq\cdots.
\tag{1}
\]
The actual homogeneous source image, denoted \(S_{d,r}^{\rm act}\), lies
in every one. These subspaces express how long a symbol can survive global
lifting, without choosing a particular sequence of corrections.

The filtered complex above is intrinsic to this polarized ideal-adic neighborhood.
There are no incoming differentials to total cohomological degree zero.
Thus the source at \((r,-r)\) shrinks by kernels and ends at
\(S_{r,N}(d)\). In particular,
\[
\operatorname{codim}S_{r,N}(d)
=\sum_{s=1}^{N-r}\operatorname{rank}
\left(d_s:E_s^{r,-r}\to E_s^{r+s,1-r-s}\right).
\tag{2}
\]
The targets are the targets on their respective pages, with previous
quotients already taken. They are not independent copies of first-page
\(H^1\) spaces. Isomorphisms of the polarized filtered neighborhoods
preserve these spaces and ranks.

If \(H^0(I^rL^d)\to H^0(T_{r,N}(d))\) is onto, the terminal space is
\(S_{d,r}^{\rm act}\). Vanishing of \(H^1(I^{N+1}L^d)\) suffices.
Vanishing of \(H^0(I^{N+1}L^d)\) is needed for unique realization,
not for equality of symbol images. The quartic sextic deficit of eleven,
concentrated in \(d_3\) from normal degree two to five, is an instance of
(2); its page and rank are invariant for that polarized embedding.

The first page has only two cohomological rows because the support is a
curve. This bounds cohomological width, not the index of the last nonzero
differential.

## Finite realization: existence versus an effective bound

For a smooth connected curve \(C\subset\mathbf P^3\) over an algebraically
closed field and \(d\ge0\), let \(C_N=V(I^{N+1})\). There exists a finite
\(N_0(C,d)\) such that
\[
H^0(\mathbf P^3,\mathcal O(d))\xrightarrow{\sim}
H^0(C_N,\mathcal O_{C_N}(d))\quad\text{for every }N\ge N_0(C,d).
\tag{3}
\]
This statement is characteristic free. It supplies no numerical bound on
\(N_0\).

**Proof.** The conormal and Euler sequences give subbundle injections
\(E\hookrightarrow\Omega_{\mathbf P^3}|_C\hookrightarrow
\mathcal O_C(-1)^4\). Consequently
\(H^0(C,\operatorname{Sym}^nE(d))=0\) for \(n>d\): the symmetric power
embeds in a sum of copies of the negative-degree line bundle
\(\mathcal O_C(d-n)\). Restriction
\(H^0(C_{N+1},\mathcal O(d))\to H^0(C_N,\mathcal O(d))\) is therefore
injective for \(N\ge d\). Identify these spaces with a descending sequence
of subspaces of the finite-dimensional \(H^0(C_d,\mathcal O(d))\).
There are finitely many strict drops, hence a last drop. Its stable value
is the inverse limit, the space of global formal sections.

The classical G3/Lefschetz section-extension theorem identifies that formal
space with \(H^0(\mathbf P^3,\mathcal O(d))\). The precise input and its
section-extension argument are retained in
[formal geometry, section 5](../residuals/formal_residual_visibility.md).
[Hartshorne, section 1](https://www.numdam.org/article/CM_1971__23_3_257_0.pdf)
states the projective-space G3 theorem and its Lefschetz consequence; the
absence of a divisor disjoint from \(C\) extends neighborhood sections
globally. This proves (3).

The proof bounds the **number** of strict drops, not their **positions**.
A plateau followed by a later drop is compatible with the argument.
Checking equality of two consecutive spaces is therefore not a stopping
certificate. It becomes one, for unique realization at all later orders,
when \(N\ge d\) and restriction from the known ambient source is already
an isomorphism: later spaces inject and must contain that same source.
At these depths the ambient restriction is injective, so the computable
equality \(h^0(C_N,\mathcal O(d))=\binom{d+3}{3}\) is such a certificate.

For comparison, a point in \(\mathbf P^1\) has arbitrarily long local jets
which do not extend as a fixed-degree global polynomial. The global
extension hypothesis cannot be discarded from the abstract formulation.

### An explicit family bound from a quadric flag

Let \(C\) be an effective Cartier divisor of bidegree \((\alpha,\beta)\),
\(\alpha,\beta\ge1\), on a smooth split quadric \(Q\subset\mathbf P^3\).
Smoothness of \(C\) is not needed for the following cohomology calculation.
Put \(c=\min(2,\alpha,\beta)\). Then
\[
mc>d\ge0\quad\Longrightarrow\quad
H^0(I^m(d))=H^1(I^m(d))=0.
\tag{4}
\]
Indeed, the flag sequence iterates to the base \(\mathcal O(d-2m)\)
and quotients
\[
\mathcal O_Q\bigl(d-2m+(2-\alpha)j,
                  d-2m+(2-\beta)j\bigr),\qquad 1\le j\le m.
\]
Under \(mc>d\), both bidegrees are negative for every \(j\).
Their \(H^0,H^1\) vanish by
[Kunneth](https://stacks.math.columbia.edu/tag/0BEC), and the base vanishes
in these degrees by [projective-space cohomology](https://stacks.math.columbia.edu/tag/01XS).
The long exact sequences prove (4). Thus
\[
N\ge\left\lfloor d/c\right\rfloor
\tag{5}
\]
is an explicit sufficient bound in (3), also for the ideal quotients
\(I^r/I^{N+1}\). All powers here are ideal sheaf powers.

This extends the \((1,3)\) quartic calculation to a family, with an improved
bound \(\lfloor d/2\rfloor\) when both bidegrees are at least two.
The zero-bidegree cases are outside this proof, not counterexamples to its
conclusion. Nor is (5) asserted minimal: the quartic sextic minimum is five,
while (5) gives six.

A useful contrasting control is a smooth \((2,2)\) curve. It is a complete
intersection of two quadrics. Its ideal powers have a resolution
\[
0\to\mathcal O(-2m-2)^m\to
\mathcal O(-2m)^{m+1}\to I^m\to0.
\]
Hence \(H^1(I^m(d))=0\) for every \(d\), and the exact minimum cutoff is
\(\lfloor d/2\rfloor\). Smaller depths fail injectivity, while all jet
sections lift. In this example all the differentials obstructing global
section lifting vanish; the \(H^1\) groups themselves need not vanish.
The mere existence of a two-row spectral sequence does not prescribe the
quartic's obstruction pattern.

For the fixed quartic on its split quadric, the bidegree is (1,3), so c=1:
for d≥0 and m>d, both H0(I^m(d)) and H1(I^m(d)) vanish. Thus N≥d
recovers all degree-d homogeneous sections, and for 0≤r≤N+1 also gives
H0(I^r(d))≅H0((I^r/I^(N+1))(d)). The latter follows directly from
0→I^(N+1)(d)→I^r(d)→(I^r/I^(N+1))(d)→0. This is actual compatible
neighborhood data, not the direct sum of graded pieces. The balanced
conormal splitting used next retains its characteristic-zero hypothesis.


## Sextic equation jets: where the source deficit is detected

The characteristic-zero calculation uses
\[
\operatorname{Sym}^nE(6)=
\mathcal O_{\mathbf P^1}(24-7n)^{\oplus(n+1)}.
\]
The accepted [actual source calculation](#exact-homogeneous-equation-spaces-and-fixed-quadric-restrictions) gives
\(h^0(I^2(6))=23\), while its quadratic symbol has image dimension 22
inside a 33-dimensional target, and the kernel is \(\mathbf Q q^3\).
The exact rational Cech calculation gives:

| Maximum normal order \(n\) | \(h^0(T_{2,n}(6))\) | Quadratic-symbol image dimension | Rank of the new connecting map \(\partial_n\) |
| --- | ---: | ---: | ---: |
| 2 | 33 | 33 | — |
| 3 | 49 | 33 | 0 |
| 4 | 34 | 33 | 15 |
| 5 | 23 | 22 | 11 |
| 6 | 23 | 22 | 0 |

The new layers at orders 3, 4, 5, 6 have respectively
\((h^0,h^1)=(16,0),(0,15),(0,60),(0,119)\).
The zero-obstruction stage at order three adds 16 freedoms; subsequent
stages only impose conditions. The full computation is retained in
[sextic_global_jet_cech.py](../../computations/sextic_global_jet_cech.py).

It uses the accepted exact embedded transition, not just its linear part:
\[
\begin{aligned}
T&=z^4+u+\tfrac32zv,&
w&=(z^3+v)/T,\\
a'&=z/T-w^3,&b'&=1/T-w^4,\\
u'&=a'/2,&v'&=-3wa'+2b'.
\end{aligned}
\]
The two affine charts \(x_0\ne0\) and \(x_3\ne0\) cover \(C\) and its
nilpotent neighborhoods. A degree-six section is a pair of polynomial jets
\((P_0(z,u,v),P_\infty(w,u',v'))\) satisfying
\[
P_0=T^6P_\infty\pmod{I^{n+1}}.
\tag{9}
\]
The factor \(T^6\), higher normal terms, and nonlinear change of base are
all retained. At new order \(n\), the leading transformation is
\(z^{24-7n}\) on each normal monomial. Put \(L=24-7n\).
In the Laurent mismatch, exponents \(k\ge0\) can be removed on the first
chart and \(k\le L\) on the second. The remaining coefficients
\(L<k<0\) are precisely the connecting obstruction. Their rational
matrix kernel gives all liftable old jets; if \(L\ge0\), the overlaps
\(0\le k\le L\) supply all new global-section freedoms. This constructs
the whole space at each stage, including its projection to quadratic symbols.

### The first nonlinear gluing map by torus weight

The pure cubic-to-quartic connecting map can be checked without reducing
an entire 15-by-16 matrix. Give \(z,u,v\) weights \(1,4,3\). The source
basis is \(z^k u^i v^j\) with \(i+j=3\), \(0\le k\le3\).
The quartic target has the standard Čech gap basis
\(z^k u^i v^j\) with \(i+j=4\), \(-3\le k\le-1\).
Exactly the weights \(9,\ldots,15\) occur in both. The respective source
and target multiplicities are
\[
(1,2,3,4,3,2,1),\qquad (1,2,3,3,3,2,1).
\]

Here is the whole calculation for these small blocks. On the second
chart the matching pure-cubic term is \(w^{3-k}(u')^i(v')^j\).
Put \(X=u/z^4,\ Y=v/z^3\). The transition in (9) gives
\(T=z^4(1+X+3Y/2)\), \(w=z^{-1}(1-X-Y/2+O(I^2))\), and
\[
\begin{aligned}
 z^7 u'&=u-\tfrac52z^{-4}u^2-3z^{-3}uv-\tfrac38z^{-2}v^2+O(I^3),\\
 z^7 v'&=v+3z^{-5}u^2-z^{-4}uv-\tfrac94z^{-3}v^2+O(I^3).
\end{aligned}
\]
Before projecting to the gap, the normal-degree-four part of
\(T^6 w^{3-k}(u')^i(v')^j\) has just the following four terms (a term
with a negative monomial exponent and zero coefficient is omitted).
The connecting map uses the negative of this degree-four part.
\[
\begin{array}{c|c}
 \text{monomial} & \text{coefficient}\\ \hline
 z^{k-5}u^{i+2}v^{j-1} & 3j\\
 z^{k-4}u^{i+1}v^j     & 3+k-\frac52 i-j\\
 z^{k-3}u^iv^{j+1}     & \frac{15+k}{2}-3i-\frac94 j\\
 z^{k-2}u^{i-1}v^{j+2} & -\frac38 i
\end{array}
\]
This gives the following determinants, with rows and columns ordered
first by \(i\), then by \(k\), keeping the first three columns at weight 12.
\[
\begin{array}{c|rrrrrrr}
 \text{weight} &9&10&11&12&13&14&15\\\hline
 \det\text{ or maximal minor}&-3/4&3/8&-21/32&21&21/4&3/2&3/2
\end{array}
\]
Thus all seven maps are onto in characteristic zero. Their only kernel
is in weight 12 and is the symbol of \(q^3\), a genuine global sextic.
The argument separates the equivariant geometry and the first nonlinear
transition from the remaining elementary determinants. It is a small
coordinate proof, not a coordinate-free theorem for arbitrary embeddings.

### A genuine third differential detects the eleven missing symbols

The order-four obstruction has rank 15 already on the 16-dimensional
subspace of **pure cubic corrections**. Thus every quadratic symbol has
an order-four lift, and the cubic ambiguity is one-dimensional. The actual
sextic \(q^3\), with \(q=u+zv/2\) on the first chart, spans that ambiguity.
Its order-five obstruction is zero because it is an actual global equation.
The remaining order-five map therefore descends to a rank-11 map on the
33-dimensional quadratic-symbol space.

In the filtered Čech sequence, this means
\[
\operatorname{rank}\bigl(d_1:H^0(\operatorname{Sym}^3E(6))
\to H^1(\operatorname{Sym}^4E(6))\bigr)=15.
\tag{10}
\]
It exhausts the degree-four target. Hence the potential \(d_2\) from
normal degree two to four has zero target. The surviving cubic class
\(q^3\) is permanent, so its \(d_2\) into degree five also vanishes.
Consequently the surviving quadratic symbols form the kernel of an actual
\[
d_3:E_3^{2,-2}\longrightarrow E_3^{5,-4},
\qquad \operatorname{rank}d_3=11.
\tag{11}
\]
This identifies the obstruction **page and source-image kernel**. It does
not assert a preferred basis of the 60-dimensional target or identify its
coordinates with a different obstruction theory. The kernel is the accepted
22-dimensional image described by the
[eleven sextic symbol equations](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-global-realization-incidence).
Thus a leading symbol can be globally compatible through quartic normal
order and still fail to be the symbol of any global sextic. This is a
specific higher-gluing obstruction, not merely a count of extra parameters.

### Verified characters and the quadric-flag cohomology

Let \(T\) act on coordinates with weights \((0,1,3,4)\), and use the
induced (unshifted) linearization on \(\mathcal O_{\mathbf P^3}(6)\).
The equivariant quadratic-symbol sequence is
\[
0\to I^3(6)\to I^2(6)\to\operatorname{Sym}^2E(6)\to0.
\]
The established vanishing \(H^1(I^2(6))=0\) therefore identifies,
**canonically and \(T\)-equivariantly**,
\[
\operatorname{coker}(\sigma_{6,2})\simeq H^1(\mathbf P^3,I^3(6)).
\tag{13}
\]
Here \(H^0(I^3(6))=kq^3\) has weight \(12\).

A weight-by-weight check needs no new rank calculation. The three
quadratic normal monomial families have weights \(6+j,7+j,8+j\)
for \(0\le j\le10\). The already established actual source
\(H^0(I^2(6))\) has weight multiplicities
\((1,1,2,2,2,2,3,2,2,2,2,1,1)\) for weights \(6,\ldots,18\).
Subtract the one-dimensional kernel in weight \(12\):

| Weight | Target | Source | Kernel | Image | Cokernel |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 6 | 1 | 1 | 0 | 1 | 0 |
| 7 | 2 | 1 | 0 | 1 | 1 |
| 8 | 3 | 2 | 0 | 2 | 1 |
| 9 | 3 | 2 | 0 | 2 | 1 |
| 10 | 3 | 2 | 0 | 2 | 1 |
| 11 | 3 | 2 | 0 | 2 | 1 |
| 12 | 3 | 3 | 1 | 2 | 1 |
| 13 | 3 | 2 | 0 | 2 | 1 |
| 14 | 3 | 2 | 0 | 2 | 1 |
| 15 | 3 | 2 | 0 | 2 | 1 |
| 16 | 3 | 2 | 0 | 2 | 1 |
| 17 | 2 | 1 | 0 | 1 | 1 |
| 18 | 1 | 1 | 0 | 1 | 0 |
| **Total** | **33** | **23** | **1** | **22** | **11** |

There is also a geometric explanation. Write
\(Q=\mathbf P^1_{a,b}\times\mathbf P^1_{c,d}\), with
\((x_0,x_1,x_2,x_3)=(ac,ad,bc,bd)\). Then
\(\mathrm{wt}(b)=3,\mathrm{wt}(d)=1\), with \(a,c\) of weight zero.
The quadric equation \(q=x_0x_3-x_1x_2\) has weight \(4\);
the divisor \(C\subset Q\) is cut out by
\(f=bc^3-ad^3\), of bidegree \((1,3)\) and weight \(3\).
The standard Cartier-divisor/quadric flag for \(I^3(6)\)
has successive quotients
\[
\mathcal O_Q(3,-3)\,[f^3],\quad
\mathcal O_Q(2,-2)\,[qf^2],\quad
\mathcal O_Q(1,-1)\,[q^2f],\quad
\mathcal O_{\mathbf P^3}\,[q^3].
\tag{14}
\]
The brackets indicate the **equivariant generator weight**,
respectively \(9,10,11,12\); they must not be discarded when
computing characters. The last two terms have zero \(H^1\),
and the relevant \(H^0,H^2\) terms vanish, so the filtration
induces an exact sequence (the subobject comes from multiplication by \(q\))
\[
0\to H^1(Q,\mathcal O_Q(2,-2))[10]
\to H^1(\mathbf P^3,I^3(6))
\to H^1(Q,\mathcal O_Q(3,-3))[9]\to0.
\tag{15}
\]
By Künneth and the standard equivariant Čech basis
\(d^{-1}c^{-2},d^{-2}c^{-1}\) for \(H^1(\mathcal O(-3))\)
(and \(d^{-1}c^{-1}\) for \(H^1(\mathcal O(-2))\)),
the two pieces have characters
\[
\begin{aligned}
H^1(Q,\mathcal O_Q(3,-3))[9]&:
  &&7,8,10,11,13,14,16,17,\\
H^1(Q,\mathcal O_Q(2,-2))[10]&:
  &&9,12,15.
\end{aligned}
\tag{16}
\]
Their weights are disjoint. In characteristic zero, torus
representations are semisimple, so the cokernel is multiplicity-free:
\[
\operatorname{coker}(\sigma_{6,2})
 \cong_T\bigoplus_{w=7}^{17}k_w
 \cong_T\left(\bigoplus_{j=-5}^{5}k_j\right)\otimes k_{12}.
\tag{17}
\]
The centered \(-5,\ldots,5\) list is therefore a **character
normalization**, not the unshifted representation. The cohomology
identification (13) and quadric filtration (15) are canonical for
the embedded curve and its unique quadric. For this specified torus,
the disjoint weight supports canonically split (15) equivariantly.
This does not pick an unmarked coordinate splitting of the full
order-five target. The intrinsic 8-plus-3 criterion for the eleven
individual coordinate rows is in the
[actual sextic symbol calculation](../spectral/conditional_2_12_surface_and_symbol_geometry.md#2-the-exact-global-k-linear-symbol-map).
The natural map from (13) to the order-five image is described below.
No supported sextic pair or characteristic-zero exclusion follows.

### Natural comparison with the actual symbol defect

The order-five calculation proves \(H^1(I^6(6))=0\) as in the cutoff
argument below (restriction of sextics is onto, and
\(H^1(\mathcal O_{\mathbf P^3}(6))=0\)).
Consequently \(H^1(I^3(6))\) injects into \(H^1((I^3/I^6)(6))\).
The order-four surjectivity above gives
\(H^1((I^3/I^5)(6))=0\) and \(H^0((I^3/I^5)(6))=kq^3\).
The class \(q^3\) lifts through order five, so the exact sequence
for \(I^3/I^6\) gives the natural isomorphism
\[
 H^1(\operatorname{Sym}^5E(6))\ \xrightarrow{\sim}\
 H^1((I^3/I^6)(6)).
\]
By naturality between the actual symbol sequence and its quotient
by \(I^6(6)\), the order-five connecting map is the actual connecting
map to \(H^1(I^3(6))\) followed by this injection, expressed in the
order-five target using the isomorphism. It is the \(d_3\) here:
the quartic target was exhausted by \(d_1\), the only cubic global
class survives, and \(H^0(\operatorname{Sym}^4E(6))=0\).
This identifies the quadric-flag filtration on the actual symbol
defect with a filtration of the **image** of \(d_3\), not with a
filtration of the whole 60-dimensional target. It does not replace
the retained order-five calculation establishing the cutoff or give
a formula for the position of each image line in the full target.

### The exact minimum sextic cutoff is order five

The map \(H^0(I^2(6))\to H^0(T_{2,5}(6))\) is injective, since
\(H^0(I^6(6))=0\) by the existing equation-space formula. Both dimensions
are 23, so it is an isomorphism. Also \(H^1(I^2(6))=0\) by the established
high-degree vanishing. Given any global section of \((\mathcal O/I^6)(6)\),
its reduction modulo \(I^2\) therefore lifts to a homogeneous sextic.
Subtract that lift. The remainder lies in \(H^0(T_{2,5}(6))\) and so
also lifts. Uniqueness again uses \(H^0(I^6(6))=0\). Hence
\[
H^0(\mathcal O_P(6))\xrightarrow{\sim}
H^0((\mathcal O_P/I^6)(6)).
\tag{12}
\]
Order four fails: \(H^0(T_{2,4}(6))\) has dimension 34, exceeding the
23-dimensional actual source. If one of these jets came from a sextic,
vanishing modulo \(I^2\) would put that sextic in \(H^0(I^2(6))\), a
contradiction for jets outside its image. Orders two and three fail by
the same comparison; at order one the restriction is not injective because
\(H^0(I^2(6))\ne0\), and at order zero it is not injective either.
Thus five is the least order giving an isomorphism for all sextic sections.

## The correction recursion is an exact sequence of obstruction spaces

Let \(C\subset S=V(q)\subset\mathbf P^3\), where \(q\) has degree \(e\),
\(S\) is smooth along \(C\), and \(C\) is Cartier on \(S\). The flag gives
\[
0\to I^{m-1}(d-e)\xrightarrow{q}I^m(d)
\to\mathcal O_S(d)(-mC)\to0.
\]
If the last sheaf has no global sections, then
\(V_{d,m}=qV_{d-e,m-1}\). No \(H^1\) hypothesis is required for this equality.

Set \(A=\mathcal O_C(-e)\subset E\), \(M=E/A\), and denote its first
symbol by \(\ell\). There is an exact symmetric-power sequence
\[
0\to\operatorname{Sym}^{m-1}E(d-e)\xrightarrow{\ell}
\operatorname{Sym}^mE(d)\to M^m(d)\to0.
\]
Let \(K\) and \(B\) be the global-section spaces of the first and middle
terms; let \(U=S_{d-e,m-1}^{\rm act}\subset K\) and
\(J=\operatorname{im}[B\to H^0(M^m(d))]\). The actual image is
\(W=\ell U\), and the quotient obstruction spaces fit into
\[
0\to K/U\to B/W\to J\to0.
\tag{6}
\]
Thus \(\operatorname{codim}_B W=\dim J+\operatorname{codim}_K U\).
If \(H^1(\operatorname{Sym}^{m-1}E(d-e))=0\), then \(J=H^0(M^m(d))\).
Without an established surjectivity statement, only the actual image \(J\)
counts; replacing it by the full target can overcount the divisibility
constraints. A nonzero \(H^1\) alone does not imply that surjectivity fails.

The octic \(15+11\) is exactly (6): \(\dim B=48\), \(\dim K=33\),
\(\dim J=15\), \(\dim U=22\). It is a filtration of obstruction spaces,
not a preferred splitting. This recursion transports the lower-degree
source calculation to higher-degree corrections, retaining all affine
lift freedoms. It does not transport a root obstruction without a
comparison map.

### The two degree rows use the source filter at different orders

Under the precise saturated, full generic initial-CI, order-two,
movement-two hypotheses retained in the
[torsion-two continuation](../spectral/quadratic_root_torsion_two_lifting.md),
the remaining degree rows are \((6,16)\) and \((8,8)\). The sextic row
already has the 11 quadratic-symbol conditions above. An octic has no
quadratic-symbol restriction: the actual source has dimension 80 and
surjects onto the full 57-dimensional symbol space. Nevertheless its
higher corrections are constrained in an especially simple way.

Write \(V_{d,r}=H^0(I^r(d))\), and let \(\sigma_{d,r}\) be the leading
symbol map. The existing quadric-factor formula gives exact global identities
\[
V_{8,3}=qV_{6,2},\qquad V_{8,4}=kq^4.
\tag{13}
\]
Thus, after fixing the quadratic symbol and choosing one actual octic
\(F_0\) with that symbol, **every** other actual lift is
\(F_0+qH\), \(H\in V_{6,2}\). Its cubic symbol difference from \(F_0\)
lies precisely in
\[
\ell\,\operatorname{im}\sigma_{6,2}
\subset H^0(\operatorname{Sym}^3E(8)),
\qquad \ell=\sigma_{2,1}(q)=u+\tfrac12zv.
\tag{14}
\]
The image has dimension 22 inside a 48-dimensional space, and the remaining
equation freedom after fixing it is \(kq^4\). These statements concern
differences of octics with the **same** quadratic symbol. The absolute cubic
term of an arbitrary octic is not required to be divisible by \(\ell\).

The 26 missing directions have a geometric two-stage description. The
conormal flag of the smooth quadric is
\[
0\to L=\mathcal O_{\mathbf P^1}(-8)\to
E=\mathcal O_{\mathbf P^1}(-7)^{\oplus2}
\to\mathcal O_{\mathbf P^1}(-6)\to0.
\]
Multiplying by \(\ell\) and taking the quotient gives
\[
0\to\operatorname{Sym}^2E(6)
\xrightarrow{\ell}\operatorname{Sym}^3E(8)
\to\mathcal O_{\mathbf P^1}(14)\to0.
\tag{15}
\]
Because the first term has no \(H^1\), the sequence on global sections
is exact with dimensions \(33\to48\to15\). First impose these 15
linear conditions for **global divisibility** by \(\ell\); then the unique
quadratic quotient must satisfy the 11 sextic-symbol conditions. This is a
canonical nested filtration of the constraints, not a preferred direct-sum
decomposition of their targets. It gives exactly the image in (14), with
all global correction freedom retained.

Consequently the same 11-condition source calculation can be reused for
both rows: directly on sextic quadratic symbols, and after 15 divisibility
conditions on differences of octic cubic lifts. When comparing a proposed
compatible cubic jet with \(F_0\), use this affine image instead of 48
independent cubic coefficients. This is a linear reduction; no new
emptiness calculation for the root incidence follows from it. Nor does
(13) alone give an order-six global cutoff for arbitrary octic jets:
divisibility of actual equations and divisibility of truncated jets are
different requirements.

## One finite neighborhood for a fixed-degree pair

The full [generic finite-normal-jet criterion](../residuals/finite_normal_jets.md) already
proves, for the fixed quartic and nonzero degree-(a,b) forms in its ideal,
that sole support is equivalent to truncated generic length M=ab/4 at
exponent M+1 when M is integral; it also detects failure of properness.
The proof and sharpness examples remain in that single owner. Combined with
the cutoff above, N≥max(a,b,M) suffices for both global-source compatibility
and this generic support test on one actual neighborhood. If4∤ab, no such
pair exists. Actual coefficients remain constant-field scalars.

This is a finite organization, not a claim that jet coordinates are smaller
than homogeneous forms. Actual source dimensions grow as O(d³). Linear
compatibility can be imposed before nonlinear root/contact conditions, but
no solver, uniform witness-degree bound or hardness theorem follows.
The [finite certificate account](bounded_equation_certificates.md) distinguishes
these verification and search quantifiers.


For the movement-two laboratory, [R-0007](../../results/quadratic_root_obstruction_model.md)
concerns a root divisor on the exceptional ruled surface. Call that divisor
\(\Sigma\) here to avoid confusing it with \(Z=X\cap Y\). Its first and
second obstructions are nonlinear Cech lifting classes on the blowup.
[R-0006](../../results/actual_ci_smooth_root_bridge.md) supplies a one-way
necessity bridge from actual CI data only under its stated saturation,
full initial-CI, smooth-root, and relation-gap hypotheses. No comparison
identifying these root classes with the filtered-Čech differentials, or with
either Koszul spectral sequence, has been established. The finite-source
calculation instead supplies a rigorously separate compatibility filter.

## Exact sextic source-image certificate

The [rational Čech calculator](../../computations/sextic_global_jet_cech.py) checks both normal frames, signs, and Laurent gaps. It gives source dimensions \(33,49,34,23,23\), quadratic-symbol ranks \(33,33,33,22,22\), and connecting ranks \(0,0,15,11,0\). Pure cubics have connecting rank \(15\), while the surviving \(q^3\) direction has zero fifth-order obstruction. An independent 28-generator two-chart span has source rank \(23\), quadratic rank \(22\), and combined rank \(23\) with the Čech basis, establishing equality of the computed source subspaces.

The filtered recursion measures the **actual image** \(J\): nonzero \(H^1\) alone does not establish failure of lifting. These calculations establish neither a finite-field extension nor a supported pair. The uniform arguments are [finite normal jets](../residuals/finite_normal_jets.md) and [global lifting interfaces](global_lifting_interfaces.md).

## Consolidated order-one carrier and defect bounds

The following results are retained from the historical order-one jet analysis. They are necessary conditions, not a characteristic-zero STCI exclusion in unrestricted degrees. The cited numerical normal-sheaf and primitive obstruction inputs retain their original hypotheses.

## Additional lower bound for the order-one carrier

Suppose F_a is the equation whose generic normal order is one, and set
S=V(F_a). It is integral: any irreducible factor of a defining equation
must contain C, by intersecting with the mate, so more than one factor
would give normal order at least two. It is regular at the generic point
of C. Its torsion-free conormal along C is L, hence

    deg N_(C/S)=7-e.

On the normalization the unique lift C^nu of C is smooth and isomorphic
to C. The mate's pullback Cartier divisor is m C^nu, with m=ab/4;
finiteness of normalization creates no additional curve supported over
a closed point. Thus its numerical pullback satisfies

    (C^nu)^# == (4/a)H,  ((C^nu)^#)^2=16/a.

The audited numerical-normal-sheaf inequality in
[the numerical surface-pullback proof](../carriers/numerical_surface_pullback.md) applies even if S is nonnormal at
finitely many points of C. It gives

    16/a <= 7-e,
    a >= ceil(16/(7-e)).                             (U4)

Combined with a>=4, the order-one carrier's necessary lower degree for
e=0,...,6 is respectively 4,4,4,4,6,8,16. This bound is on the degree
of the generically regular carrier; if the mate is thick along C it does
not transfer to that mate. The finite-order defect bounds above are
independently audited; this additional geometric deduction is recorded
with its explicit reliance on the proved normal-sheaf inequality.

## Companion bound for local-cohomology ancestors

For the fixed C0 let u,v be the recorded first-socle targets of degree -3.
If equal-degree homogeneous multipliers F_d,G_d and an ancestor alpha obey
F_d alpha=u, G_d alpha=v, then alpha has degree -(d+3). Suppose at least
one multiplier has nonzero first conormal symbol and alpha has top
principal-part order n>=3. Its top quotient is

    O_P1(7n-4d-5) tensor Sym^(n-1)(k^2).

Contraction by the nonzero linear symbol kills that top section. In
characteristic zero it is a pure (n-1)-st power in the perpendicular
primitive degree-e direction, multiplied by a nonzero binary section.
Consequently

    7n-4d-5-(n-1)e >= 0,
    (7-e)(n-1) >= 4d-2.                              (U3)

For d>=1 this again forces e<=6. If d>=4, the quotient of order two has
no global sections, so n>=3 is automatic for a nonzero ancestor. Coprimality
and the fixed-degree principal-part bound provide a finite maximum n for
each d, but do not bound d. If both multiplier first symbols vanish, the
linear contraction argument does not apply and no e-bound is asserted.


## 3. A uniform degree strengthening beyond the retained bounds

Assume a,b>=4, generic normal order one for at least one equation, and
N*=O(-7)^2. The conormal epimorphism onto L has

    L=O(e-7),     e>=0,     c=7-e,     m=ab/4, s=m-1.

Here ab must be divisible by 4. Adjunction gives

    deg D_s = c*(ab/4-1)+14-4(a+b).                   (1)

Effectivity first gives c>0, hence e<=6. Multiplying (1) by 4c and
completing the product gives the stronger necessary degree condition

    (c*a-16)(c*b-16) >= 256-56*c+4*c^2.               (2)

This is equivalent to top-defect effectivity, rather than an additional
geometric hypothesis. It displays degree restrictions missed by listing
only e<=6 or 16/a<=c. For the four highest direction degrees it becomes

| e | Exact necessary inequality | Each defining degree must be at least |
|---|---|---:|
| 3 | (a-4)(b-4)>=6 | 5 |
| 4 | (3a-16)(3b-16)>=124 | 6 |
| 5 | (a-8)(b-8)>=40 | 9 |
| 6 | (a-16)(b-16)>=204 | 17 |

For e=3 both factors are nonnegative because a,b>=4, and the right
side is positive. For e=4, if both factors were negative their product
would be at most 16; for e=5 the corresponding bound is 64 after
multiplying by four; for e=6 it is 144. Each is smaller than the
required right side. A mixed-sign product is also impossible, so both
factors must be strictly positive. This proves both degree lower bounds,
including for a mate that may be thick generically. It does not transfer
the geometric normal-sheaf inequality to a thick mate.

For completeness, (2) has right sides 60,64,76 for c=7,6,5
(e=0,1,2). None is negative. The exact constraints for e=1,2 are
(6a-16)(6b-16)>=64 and (5a-16)(5b-16)>=76.
At e=2,a=4 the latter is precisely b>=7. These conditions give no
upper bound on either degree and do not exclude the high-degree
order-one branch.

## 4. Why the primitive factorization stops at its stated hypotheses

For a quartic carrier m=b and the top formula is

    deg D_(b-1)=(3-e)*b+e-9.

At e=2 this is b-7. For b=7 the entire defect divisor vanishes.
For b=8, superadditivity forces D2=D3=0 because twice either one
is bounded by a divisor of degree one. The canonical primitive fourth
then exists, so its quotient lies on the audited fourth-obstruction
zero locus. On that locus the defining quartic lies in

    H0(I_(C3)(4))=T*H0(O_(P3)(1)).

Its nonzero plane factor forces an extra curve when intersected with
any mate, proving the two exclusions. The same argument works at
any larger b when D2=D3=0. It does not force these equalities once
b-7 permits nonzero early defects. The existing parity theorem does
give an all-b exclusion on its explicit parity quotient family with
D2=0, but it does not cover every quadratic quotient or D2=1.

## 5. Exact local CI controls against a numerical overclaim

Let R=k[[t]] and take integers r,h>=2. The local algebra

    B_(r,h)=R[x,y]/(t*x-y^r, x^h)

is finite free with basis x^i*y^j, 0<=i<h, 0<=j<r. One can see
this by first taking R[x]/(x^h) and adjoining the monic relation
y^r-t*x. It is a complete intersection supported on (x,y).
After inverting t it is K[y]/(y^(r*h)) with x=t^(-1)y^r.
Writing k=r*i+j shows that the saturated layer E_k has generator
t^(-i)y^k, whereas the image of E1^k has generator y^k. Hence

    d_k=ord_t D_k=floor(k/r),       0<=k<r*h.         (3)

This formula satisfies superadditivity and complement duality exactly:

    floor(i/r)+floor((r*h-1-i)/r)=h-1.

Two controls are directly compatible with the e=2 top degree:

| b=r*h | Local equations | (d2,d3,d_(b-1)) |
|---:|---|---|
| 9 | t*x-y^3, x^3 | (0,1,2) |
| 12 | t*x-y^2, x^6 | (1,1,5) |

In each case d_(b-1)=b-7 and the uniform early bounds are satisfied.
Thus even finite-flat, two-normal-generator, local CI and Gorenstein
duality do not extend the primitive exclusion to every b. These are
local numerical controls, not projectively embedded multiple curves
on C0 and not STCI counterexamples or constructions. They establish
the insufficiency of the proposed numerical inference.

## 6. A sharper small-degree surviving frontier

For e=2, repeated multiplication gives

    deg D2 <= floor((b-7)/floor((b-1)/2)),
    deg D3 <= floor((b-7)/floor((b-1)/3)).              (4)

In particular b=9,10,11 have D2=0 and deg D3<=1. A survivor must
have deg D3=1; otherwise the primitive factorization applies. Write
D3=p. At p, superadditivity and complement duality force every
top defect to lie at p:

* b=9: D3+D5=D8 and D5>=D3, so the top degree two is spent at p.
* b=10: 3D3<=D9, so the top degree three is spent at p.
* b=11: 3D3<=D9=D10. Moreover D10=2D5, so its coefficient
  at each point is even. Its coefficient at p is therefore at least
  four, exhausting the total degree four.

Consequently the complete divisor sequence is an integer profile
d_i*p. Exhausting the finitely many integers allowed by (BF) gives

| b | Complete permissible profiles (d0,...,d_(b-1)) |
|---:|---|
| 9 | (0,0,0,1,1,1,2,2,2) |
| 10 | (0,0,0,1,1,2,2,3,3,3) |
| 11 | (0,0,0,1,1,2,3,3,4,4,4); (0,0,0,1,2,2,2,3,4,4,4) |

The companion `verify_session_uniform_bf_profiles.py` independently
enumerates every complementary profile, imposes effectivity,
monotonicity (the i=1 multiplication case), all superadditivity
inequalities, and d2=0,d3=1. It checks exactly these lists.
The b=9 profile has the genuine local CI control above. The other
profiles remain necessary numerical possibilities; the verifier does
not assert their embedded or local nonmonomial existence.

## 7. Intrinsic fourth-layer annihilation for fixed C0

The universal moving-coordinate generator and exact P16/Delta formulas in this subsection concern the fixed embedded C0, with its stated quotient frames; they are not a universal formula for all smooth rational quartics.

When D2=0 the primitive triple has ideal-generator bundle fitting in

    0 -> L^3 -> V=I_(C3)/(I_C*I_(C3)) -> M -> 0,
    L=O(-5), M=O(-9).

Its class c lies in H1(O(-6)). A fourth layer with
E3=L^3(D3) induces a quotient V->E3 whose restriction to L^3
is the canonical multiplication section. Applying Hom(-,E3) gives
the necessary annihilation

    c maps to zero in H1(O(-6+D3)).                   (5)

If c is represented by coefficients c1,...,c5 of z^-1,...,z^-5,
a quadratic annihilator exists exactly when

    det [[c1,c2,c3],[c2,c3,c4],[c3,c4,c5]]=0.           (6)

This is multiplication of Laurent cocycles, so it includes the moving
infinity point when sections are treated homogeneously. For b=9..11
the stronger degree-one annihilator is necessary: the four-by-two
matrix with rows (c1,c2),(c2,c3),(c3,c4),(c4,c5) must have nonzero
kernel. The condition is rank at most one, not merely (6).

The [Hankel exporter](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/session_uniform_e2_hankel.py) imports
the exact moving-coordinate generator. From the repository root, run
`python3 research/computations/session_uniform_e2_hankel.py` with SymPy
to produce `research/scratch/session_uniform_e2_hankel.json`. SymPy
1.14.0 reproduced the [historical export](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/scratch/session_uniform_e2_hankel.json) byte for byte from
absent output. The calculation gives c_j with a single
homogeneous-resultant denominator Delta. Then the Hankel determinant
reduces to P16/Delta, with P16 homogeneous of degree sixteen and
1112 monomials. The numerator vanishes to order at least six in
(2a1+b0,2a2+b1). Its parity specialization is

    - (beta+2)^6*(beta^2+8beta+36)
       *(beta^4+8beta^3-24beta^2-256beta-432)/1024.

Division by the specialized Delta=beta^2 gives the actual determinant.
At beta=-6,-2,6 the fourth vectors are respectively
(64,0,-8,0,0), (0,0,0,0,0), and (-128,0,160,0,-192);
the determinants are 512,0,-163840, matching the independent retained
parity certificate. There was no useful general polynomial
factorization, and no universal incidence exclusion was completed.

This export is exact derived data from the established generator,
not an independent audit of that generator. The open primitive-triple
problem combines actual quartic contact, the resultant-open condition,
and (5). For D2=1 a defective-triple gluing state is needed before
using any fourth class. The primitive calculation does not apply there.

The exporter also saves all six exact minors of the four-by-two
degree-one annihilator matrix, with their resultant denominator powers.
Their reduced numerator term counts are 392,412,447,416,412,392.
Thus the sharper b=9..11 necessary condition has a reproducible complete
polynomial specification. No saturation or emptiness certificate for its
intersection with the full ambient quartic-contact incidence is claimed.



## Exact scope of the tests

The local \(B_{r,h}\) examples show that saturation symmetry and a top divisor do not force early primitivity. The Hankel model tests the **specified primitive triple and the same allowable divisor**, not all embedded incidence. The [profile verifier](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_uniform_bf_profiles.py) exhausts the displayed integer profiles; the [Hankel exporter](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/session_uniform_e2_hankel.py) gives necessary polynomial equations and denominators, **not** an emptiness proof. The full quartic-source and arbitrary-mate results are [the quartic-pair argument](../normal-geometry/quartic_pair_obstruction.md) and [R-0001](../../results/quartic_carrier_exclusion.md).

Local saturated duality is characteristic-free. The degree table needs the characteristic-zero normal bundle and lower-carrier exclusions; ancestor contraction uses the characteristic-zero symmetric pairing. [Odd-characteristic generator arithmetic](../normal-geometry/normal_flatness_and_filtered_ci.md) is a different initial-algebra class.

## Independent balanced-normal proof excluding thick–thick sextic pairs

This argument is separate from the universal effective-cycle inequality. Its characteristic-zero balanced-normal hypothesis is essential.

## the first thick carriers, in degree six

<a id="p-017"></a>

Let \(q\) define the unique quadric \(Q\), with
\(C\sim(1,3)\).  Reduction modulo \(q\) gives an exact sequence

\[
 0\longrightarrow \mathcal I_C(4)
 \xrightarrow{\cdot q}\mathcal I_C^{(2)}(6)
 \longrightarrow\mathcal O_Q(4,0)\longrightarrow0.
\]

Indeed, the restriction of a double sextic is \(h^2R\), where \(h\) defines
\(C\) on \(Q\) and

\[
 R\in H^0(Q,\mathcal O_Q((6,6)-2(1,3)))
 =H^0(Q,\mathcal O_Q(4,0)).
\]

The kernel consists of \(qH\) with \(H\in I_C(4)\), and
\(H^1(I_C(4))=0\).  Since

\[
 h^0(I_C(4))=h^0(\mathcal O_{\mathbf P^3}(2))
 +h^0(\mathcal O_Q(3,1))=10+8=18,
\]

one obtains

\[
 \boxed{h^0(I_C^{(2)}(6))=23,\qquad
 H^0(I_C^{(2)}(6))/qH^0(I_C(4))\simeq H^0(O_Q(4,0)).}
\]

Every non-\(q\)-divisible member has exact normal order two, because
\(H^0(I_C^{(3)}(6))=kq^3\).  Its quadric section is

\[
 X\cap Q=2C+D_R,
\]

where \(D_R\) is the union, with multiplicities, of the four ruling lines
selected by the binary quartic \(R\).

For \(C_0\), with

\[
 q=x_0x_3-x_1x_2,\quad
 A=x_0^2x_2-x_1^3,\quad
 B=x_0x_2^2-x_1^2x_3,\quad
 D=x_2^3-x_1x_3^2,
\]

the five classes

\[
 A^2,\ AB,\ B^2,\ BD,\ D^2
\]

give a complement to \(qH^0(I_C(4))\).  The missing-looking class satisfies

\[
 AD-B^2=-x_1x_2q^2.
\]

The exact verifier proves that \(I_C^{(2)}=I_C^2\) here and constructs

\[
 F_*=A^2+B^2+D^2+q^2(x_0^2+x_1^2+x_2^2+x_3^2)
\]

with reduced Jacobian locus exactly \(C_0\).  This also forces absolute
irreducibility: a nontrivial factorization would put the curve of intersection
of two factors in the singular locus. If their entire intersection were supported on C0, one factor would have degree at most three and would be a lower-degree carrier of C0. A plane cannot contain C0, cubic carriers have no mate, and the unique quadric cannot have a mate by its unequal ruling classes; these [low-degree carrier obstructions](../../frameworks/residual-construction/two_surfaces.md) exclude that possibility. Thus integral sextics singular along
the whole quartic genuinely exist; the problem is finding a mate, not finding
the first carrier.

## two thick sextics cannot be the pair

<a id="p-018"></a>

Assume characteristic zero, so
\(N_C\simeq\mathcal O(7)^2\), and suppose two non-\(q\)-divisible double
sextics \(F,G\) cut out only \(C\).  Their complete intersection has degree
36, hence generic transverse length nine along the degree-four support.  In
the transverse ring \(k(C)[[x,y]]\), both equations have order two.  Relatively
prime quadratic initial forms would have intersection length four, so the two
quadratics have a common nonconstant factor.

On the exceptional divisor

\[
 E=\mathbf P(N_C)\simeq\mathbf P^1\times\mathbf P^1,
\]

each quadratic normal divisor has class \((10,2)\).  The generic common factor
closes to a horizontal common component
\(T\sim(a,e)\), where \(a\ge0\) and \(e=1\) or \(2\); vertical factors caused
by closed-point order jumps do not remove this horizontal component.

The first normal form of \(q\) vanishes on the section

\[
 S_q=\mathbf P(N_{C/Q})\sim(1,1).
\]

The class is not \((0,1)\): after twisting the normal inclusion
\(N_{C/Q}=\mathcal O(6)\hookrightarrow\mathcal O(7)^2\) by
\(\mathcal O(-7)\), it is given by two independent linear forms, so its graph
has base degree one.

On \(Q\), write

\[
 F|_Q=h^2R_F,\qquad G|_Q=h^2R_G,\qquad
 R_F,R_G\in H^0(O_Q(4,0)).
\]

Restriction of the quadratic normal divisors to \(S_q\) is exactly the pullback
of the zero divisors of \(R_F,R_G\).  If \(T=S_q\), both residual quartics
vanish identically, so both sextics are divisible by \(q\), contrary to the
hypothesis.  Otherwise

\[
 T\cdot S_q=a+e>0.
\]

At an intersection point the two residual binary quartics have a common root.
The corresponding ruling line of \(Q\) is then contained in both \(F\) and
\(G\), giving an extra curve outside \(C\).  This contradiction proves

\[
 \boxed{\text{no thick--thick \((6,6)\) defining pair exists in
 characteristic zero}.}
\]

The balanced-normal hypothesis is essential to this proof.  In characteristic
two, \(N_{C_0}=\mathcal O(6)\oplus\mathcal O(8)\), so
\(E\simeq\mathbb F_2\) has a negative section disjoint from \(S_q\).  Exact
examples show that two tangent quadratics can share that section while their
residual quartics are coprime; those examples have other extra curves and are
not STCI pairs, but they prevent an invalid characteristic-two extension of
the argument.

## Characteristic boundary

The 23-dimensional double-sextic source and five-dimensional quadric quotient use characteristic-free smooth-quadric sheaf powers and binary monomial multiplication, without factorial division. The \(F_*\) Jacobian/radical example is certified only in characteristic zero. The thick–thick proof uses the balanced-normal exceptional product and quadric-direction graph, **not** available for this \(C_0\) in characteristic two; a negative Hirzebruch section blocks the same argument. The [positive-characteristic quartic-carrier construction](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) is independent.

## Exact homogeneous equation spaces and fixed-quadric restrictions

The following characteristic-free dimension and fixed-factor results, global row-operation restrictions, fixed-residual family, and broader characteristic-dependent monomial-curve controls are preserved from the retired equation-space supplement. Balanced conormal-symbol formulas and characteristic-zero conclusions retain their original hypotheses.

## Exact global freedom

Set
\[
D(u)=\frac{5u^3+15u^2+16u+6}{6}\qquad(u\ge0).
\]
For every integer \(m\ge1\) and \(d\ge0\),
\[
A_m(d)=
\begin{cases}
0,&d<2m,\\[2mm]
D(d-2m),&2m\le d\le3m,\\[2mm]
\displaystyle\binom{d+3}{3}
-\frac{m(m+1)(4d+1)}2
+\frac{7m(m^2-1)}3,&d\ge3m.
\end{cases} \tag{1}
\]
The two formulas at \(d=3m\) agree. The final polynomial already holds at \(d=3m-1\).

There is more information than the dimension alone. For \(2m\le d\le3m\),
\[
V_{d,m}=Q^{\,3m-d}
V_{3(d-2m),\,d-2m}. \tag{2}
\]
Thus every section has the displayed fixed quadric factor. For example,
\(V_{2m,m}=kQ^m\), and at \(d=2m+2\) the space has dimension 23 for every \(m\ge2\), but consists of \(Q^{m-2}\) times the degree-six, order-two space. This apparent freedom cannot be used as an integral degree-\(2m+2\) carrier when \(m>2\).

Here is the geometric reason. The smooth quadric \(Q\simeq\mathbf P^1\times\mathbf P^1\) contains \(C\) as a Cartier divisor of class \((1,3)\), up to swapping the rulings. The local regular-sequence identity
\((Q)\cap\mathcal I^m=Q\mathcal I^{m-1}\)
gives the flag sequence
\[
0\longrightarrow\mathcal I^{m-1}(d-2)
\xrightarrow{Q}\mathcal I^m(d)
\longrightarrow\mathcal O_Q(d-m,d-3m)\longrightarrow0. \tag{3}
\]
If \(d<3m\), the right-hand term has no sections, proving the forced factor and its iteration. Induction in (3) gives
\(H^1(\mathcal I^m(d))=0\) for \(d\ge3m-1\).
In the range \(d\ge3m\), taking sections yields
\[
A_m(d)=A_{m-1}(d-2)+(d-m+1)(d-3m+1),
\]
which sums to (1). This proves the all-degree formula; finite computations below only check its implementation and boundary values.

## Asymptotic interpretation

For fixed \(m\) and \(d\to\infty\), the number of independent linear conditions is exactly
\[
\operatorname{codim}V_{d,m}
=\frac{m(m+1)(4d+1)}2-\frac{7m(m^2-1)}3
\qquad(d\ge3m-1). \tag{4}
\]
It grows linearly in \(d\), while the ambient form space grows cubically. Vanishing to a fixed normal order therefore becomes inexpensive in large degree.

The more relevant scaling for high multiplicity is \(m/d\to\theta\). For \(0\le\theta\le1/3\),
\[
\frac{A_m(d)}{\binom{d+3}{3}}
\longrightarrow 1-12\theta^2+14\theta^3. \tag{5}
\]
At the boundary \(d=3m\), the limiting fraction is \(5/27\), so the global equation space is still large: \(A_m(3m)\sim5m^3/6\). For \(1/3\le\theta\le1/2\), the fraction is instead
\(5(1-2\theta)^3\), but this entire region has the forced quadric factor in (2). Above \(\theta=1/2\), there are no sections. These are dimensions of equation spaces, not expected dimensions of a STCI locus.

## Actual leading symbols: a small degree margin removes the first obstruction

For an equation of exact order \(r\), its leading normal symbol lies in
\[
H^0(C,\operatorname{Sym}^rE\otimes\mathcal O_C(d))
=H^0\bigl(\mathbf P^1,\mathcal O(4d-7r)\bigr)^{\oplus(r+1)}.
\]
Its actual source image has dimension
\[
\dim\operatorname{im}\sigma_{d,r}=A_r(d)-A_{r+1}(d), \tag{6}
\]
because the kernel is exactly \(V_{d,r+1}\). At the first degrees without a forced quadric factor, the comparison is

| Degree | Actual symbol image dimension | Full symbol target dimension | Codimension |
|---|---:|---:|---:|
| \(d=3r\) | \(5r^2+2\) | \((r+1)(5r+1)\) | \(6r-1\) |
| \(d=3r+1\) | \(5r^2+8r+4\) | \(5(r+1)^2\) | \(2r+1\) |
| \(d\ge3r+2\) | \((r+1)(4d-7r+1)\) | same | 0 |

The last row follows from \(H^1(\mathcal I^{r+1}(d))=0\). It is a surjectivity statement for the first nonzero normal symbol, and does not say that an arbitrary compatible tower of higher symbols comes from a pair of the required fixed degrees.

The small exact examples are useful controls:

| \((d,r)\) | Equation space \(A_r(d)\) | Symbol image | Full target |
|---|---:|---:|---:|
| \((3,1)\) | 7 | 7 | 12 |
| \((4,1)\) | 18 | 17 | 20 |
| \((5,1)\) | 35 | 28 | 28 |
| \((6,2)\) | 23 | 22 | 33 |
| \((7,2)\) | 47 | 40 | 45 |
| \((8,2)\) | 80 | 57 | 57 |
| \((9,3)\) | 54 | 47 | 64 |
| \((10,3)\) | 96 | 73 | 80 |
| \((11,3)\) | 150 | 96 | 96 |

The degree-three and degree-four rows are controls of the source spaces, not reopened STCI cases. At degree \(3r\), most equation freedom lies in higher-order terms: the equation space has cubic growth in \(r\), while its symbol image has quadratic growth. A search should keep these higher terms as adjustable contact data after selecting the leading root pattern.

## What a STCI candidate must do with this freedom

Suppose an actual proper pair \((F_a,G_b)\) has generic normal orders \(r,s\). At the generic point of \(C\), the transverse ambient local ring is regular of dimension two over \(k(C)\). If the two initial binary forms are coprime, their local intersection length is exactly \(rs\). A complete intersection with sole reduced support \(C\) would instead need length
\[
M=ab/4. \tag{7}
\]

For the integral degree-at-least-five representatives supplied by the accepted low-degree/factor reduction, (2) forces
\[
r\le a/3,\qquad s\le b/3.
\]
Consequently a coprime-leading-symbol pair has
\[
M=rs\le ab/9,
\qquad
\deg R=ab-4M\ge5ab/9. \tag{8}
\]
The lower bound in (8) is conditional on coprime leading symbols. It is **not** a residual lower bound on arbitrary pairs: shared leading roots can raise the local intersection length above \(rs\).

This proves a useful necessary search condition: a hypothetical integral STCI pair must have a nontrivial common factor between its leading normal forms over \(k(C)\). It must acquire at least \(ab/4-rs\) additional generic contact units, and the ratio of its required length to the ordinary product is at least \(9/4\). These are exact necessities, not an argument that the extra contact is unavailable.

The resulting candidate generator is concrete:

1. Choose degrees and exact equation orders with \(a,b\ge5\), \(4\mid ab\), \(r\le a/3\), and \(s\le b/3\).
2. Choose a shared-root pattern for the leading symbols, retaining its movement, branching and marked boundary behavior. At \(a=3r\) or \(3r+1\), impose the actual image in (6); at \(a\ge3r+2\), every leading symbol is available. Apply the analogous rule to \(G\).
3. Lift using actual coefficients in \(V_{a,r}\) and \(V_{b,s}\). Compute the full generic local intersection length, allowing cancellations and extra initial generators. Do not substitute the product \(rs\) once the symbols share a root.
4. Retain only proper pairs, compute \(ab-4M\), and test full global support and boundary attachment when the generic length reaches \(ab/4\). Record whether a failure came from a forced surface, inaccessible global symbol, insufficient higher contact, or residual/global boundary behavior.

This workflow uses freedom where it exists and makes each failure update a specific part of the next candidate choice. It does not make any one shared-root type compulsory; the accepted root, conductor and filtration records can test patterns within their exact hypotheses.

## Fixed residuals in a large actual lifting family

### A family with a fixed curve

Work over an algebraically closed field of characteristic zero. Fix
\[
C=C_0=[s^4:s^3t:st^3:t^4],\qquad Q=(q=0),\quad
q=x_0x_3-x_1x_2.
\]
Choose any cubic \(H\in H^0(\mathcal I_C(3))\) not divisible by \(q\).
For \(m\ge1\), put \(d=3m+2\) and take the entire actual source
\[
\mathcal W_H=
H^m\,k[x_0,x_1,x_2,x_3]_2+
H^0(\mathcal I_C^{m+1}(d)).
\tag{1}
\]
The powers are sheaf powers, or saturated homogeneous powers.
For \(m\) even and at least two, \(d\) is an even degree at least eight,
so the pair \((d,d)\) passes the low-degree and degree-divisibility filters.
No claim is made that a generic member is integral or a pair is proper.

The constructive motivation is literal: take
\[
F=f_2H^m+K,\qquad G=g_2H^m+L,
\]
with different quadratic coefficients \(f_2,g_2\) and all available
higher-normal-order corrections \(K,L\). The leading normal forms
have a common factor; their coefficient ratio may be nonconstant on
\(C\), so a constant row subtraction need not cancel them.

Nevertheless, **no two members of (1) can define \(C\) set-theoretically**.
The reviewed [freedom formula](#exact-homogeneous-equation-spaces-and-fixed-quadric-restrictions) gives
\[
H^0(\mathcal I_C^{m+1}(3m+2))
\subset q\,k[x_0,x_1,x_2,x_3]_{3m}.
\]
Indeed \(3m+2<3(m+1)\), so the next-order source has a forced quadric factor.
Thus every member of \(\mathcal W_H\) belongs to \((q,H^m)\), and
\[
V(q,H)\subset V(F,G).
\]
On \(Q\simeq\mathbf P^1\times\mathbf P^1\), the cubic cuts a divisor
of class \((3,3)\), while \(C\) has class \((1,3)\). It contains \(C\)
exactly once: two copies would leave a negative second ruling degree.
Its residual divisor therefore has class \((2,0)\). This is a nonzero
degree-two cycle of ruling lines, possibly a doubled line, and is
genuine support outside \(C\).

There is a stronger scheme-theoretic consequence for every proper pair:
\[
V(q,H^m)\subset V(F,G),\qquad
[V(q,H^m)]=m[C]+mR_H.
\]
At the generic point of each residual ruling, the quotient by \((F,G)\)
surjects onto the quotient by \((q,H^m)\); both lengths are finite.
Consequently the genuine residual cycle of the proper pair satisfies
\[
\boxed{R\ge mR_H,\qquad \deg R\ge2m.}
\]
If \(R_H\) is a doubled line, its multiplicity is retained in this
inequality. Attainment of the floor is not asserted.

The freedom in \(K,L\) cannot alter this residual because all such
corrections vanish identically on \(Q\). This is an all-parameter
global restriction, not the failure of one sampled equation.

### Equation freedom and boundary movement

Write
\[
D(m)=\frac{5m^3+15m^2+16m+6}{6}.
\]
The same reviewed source calculation gives
\[
\dim H^0(\mathcal I_C^{m+1}(3m+2))=D(m).
\]
Multiplication by \(H^m\) injects the ten-dimensional space of quadrics.
Its intersection with the next-order source consists exactly of
\(qH^m\): the cubic has generic normal order one, so the order increases
precisely when the quadratic vanishes on \(C\), and its only quadratic
equation is \(q\). Consequently
\[
\dim\mathcal W_H=D(m)+9.
\]
The full individual equation source has
\[
\dim H^0(\mathcal I_C^m(3m+2))
=D(m)+(m+1)(5m+9).
\]
Hence the excluded fixed-\(H\) family occupies a fraction of vector-space
dimension tending to one, while remaining a proper subspace of positive
codimension for every \(m\). This does not mean that it contains a
generic form or is exhaustive.

The family is not excluded merely because it has no proper pairs.
It has no fixed surface: it contains \(H^mS_2\) and
\(q^{m+1}S_m\), whose common fixed factor is one because \(q\nmid H\).
Over the infinite ground field, a generic second member avoids all
surface factors of a fixed nonzero first member. The proper-pair
locus is therefore nonempty. The quadratic leading coefficients can
also be chosen independent modulo \(q\), so every nonzero scalar
pencil member can retain exact normal order \(m\).

The floor \(2m\) grows with degree, but its ratio to
\((3m+2)^2\) tends to zero. It is not a uniform positive gap in contact
score, and it does not imply a floor for arbitrary sources.

There is a complementary warning for non-existence. The source excluded
by the [weighted-subalgebra line theorem](../curve/carrier_test_curves.md)
at degree \(3m\) has dimension asymptotic to \(m^2/4\), whereas the
full \(H^0(\mathcal I_C^m(3m))\) has dimension \(D(m)\sim5m^3/6\).
Its relative dimension is asymptotic to \(3/(10m)\), tending to zero.

Thus an all-degree family theorem need not asymptotically exhaust the
actual source, and a very large actual lifting space need not be able
to repair a fixed global boundary. Neither team may use a raw dimension
count as a substitute for the paired equations and full support test.

### Actual global row operations

Suppose actual homogeneous \(F_a,G_b\) define \(C\) set-theoretically
in characteristic zero, with \(a\le b\).
For every actual polynomial \(A\) of degree \(b-a\), the nonzero form
\[
G_b+A F_a
\tag{2}
\]
cannot have generic normal order greater than \(b/3\).
Otherwise the reviewed fixed-factor formula forces a factor \(q\)
(or forces the form to be zero when its order is too high even for a
nonzero section). A zero form in (2) makes the pair improper.
In the nonzero case
\[
V(F_a,q)\subset V(F_a,G_b+A F_a)=V(F_a,G_b).
\]
The accepted quadric-carrier exclusion and factor reduction say that
\(V(F_a,q)\) cannot have reduced support just \(C\) in characteristic zero.
This contradicts sole support. The corresponding restriction applies
after any mate-preserving homogeneous triangular row operation.

In particular, for equal-degree pairs, no nonzero scalar pencil member
may cross this normal-order threshold. This is a necessary condition
on all actual hypothetical pairs, not only (1).

The missing universal implication is substantial: large generic contact
does not automatically produce such a representative by **actual global
polynomial** row operations. Formal standard-basis cancellation can use
coefficients in \(k(C)\) with poles. No such globalization is proved here.

## Constructive interface on the quadric

For actual forms not divisible by \(q\), factor their restrictions on
the smooth quadric as divisors
\[
F_a|_Q=C^{u}A_Q,\qquad G_b|_Q=C^{v}B_Q,
\]
where \(u,v\) are their exact vanishing orders on \(C\) **inside \(Q\)**,
and
\[
[A_Q]=(a-u,a-3u),\qquad [B_Q]=(b-v,b-3v).
\]
These orders need not equal the ambient normal orders.
Sole support forces the entire common zero support of \(A_Q,B_Q\)
to lie on \(C\), with no common residual curve outside \(C\).
When the two residual divisors have no common component their total
intersection degree is
\[
(a-u)(b-3v)+(a-3u)(b-v).
\]
The problem is to concentrate that full intersection on \(C\), then solve
the remaining ambient contact and support conditions.

This is the constructive response to the fixed-\(H\) failure: choose
global restrictions whose residual factors do not share the fixed
ruling divisor, or move to degrees where next-order lifts can change
the quadric restriction. The obstruction program can independently
seek uniform bounds on this concentration or classify more residual
configurations. Neither response is yet an existence or non-existence
proof for arbitrary pairs.

## Exact scope of the source-image tests

The flag-sequence argument proves the uniform symbol formulas. The [finite Macaulay2 check](../../computations/stci_search_freedom_2026_10_28.m2) covers \(1\le m\le6\), \(0\le d\le3m+2\); it is not the uniform proof. The fixed-cubic residual-cycle floor is separate. These source-image results can locate degrees admitting higher restriction movement or obstruct movement for a specified source, but formal row operations over \(k(C)\) do **not** imply that homogeneous triangular operations cross the fixed-factor threshold.

## Broader curve controls: global coefficients and Frobenius

These exact controls concern the whole family below, not only the fixed quartic. The scalar-coefficient counterexample received independent source review. The twisted-cubic containment is checked by the retained exact script; it is a positive characteristic-zero control.

Throughout let
\[
 C_n=(s^{n+1}:s^nt:st^n:t^{n+1}),\qquad n\ge2.
\]
It is a smooth rational curve of degree n+1 and class (1,n) on the
smooth quadric \(Q=xw-yz\), up to swapping the two rulings.

## 1. Scalar extension can manufacture a false global witness

Let \(S_n=yw^{n-1}-z^n\). Consider the degree-(n+1) forms
\[
 G_1=yS_n,\qquad G_2=wS_n.
\]
In the chart w=1 take the genuine generic coordinate T=z, and the
normal coordinates
\[
 u=y-T^n,\qquad v=x-yT.
\]
Thus \(Q=v\), \(S_n=u\), and \(K=k(C_n)=k(T)\). The jets satisfy
\[
 G_1=(T^n+u)u,\quad G_2=u,\quad G_1-T^nG_2=u^2.
\]
Consequently the relaxed K-linear combination with Q has local ideal
(v,\(u^2\)), of length two. This matches the proposed global degree
budget \(2(n+1)/(n+1)=2\), even at the sufficient cutoff.

But \(T^n\) is not a constant global surface coefficient. For every
nonzero pair \((\alpha,\beta)\in k^2\), the actual global combination
has
\[
 \alpha G_1+\beta G_2
 =u(\alpha u+\alpha T^n+\beta).
\]
Since T is transcendental, \(\alpha T^n+\beta\ne0\).
The second factor is a unit in the generic local ring, so the actual
intersection with Q has length one. No member of this global pencil
passes the degree-two target.

There is a stronger, pencil-independent exclusion on this Q. A
degree-(n+1) surface meeting Q properly and with generic multiplicity
two along C_n would require
\[
 (n+1)H-2C_n=(n-1,1-n)
\]
effective on \(\mathbf P^1\times\mathbf P^1\), impossible for n>=2.
Indeed C_n is not STCI on this smooth Q in any second degree because
its class is not proportional to H.

This does not contradict the finite normal-jet criterion. The formal expression with
coefficient \(T^n\) is not a global degree-(n+1) form. Treating T as
the ambient coordinate z after dehomogenization would instead change
the polynomial to \(S_n^2\), of homogeneous degree 2n. Its degree
budget is different, and its intersection with Q has a residual ruling.
The generic formal coefficient field and homogeneous polynomial degree
must be retained together.

**Coefficient contract:** the local matrix is computed over K, but the unknown
surface coefficients must remain in k. Existence of a K-point in a
relaxed coefficient problem is insufficient. The missing datum is liftability from the actual scalar-coefficient global equation space.

## 2. The binomial pair: exact characteristic dependence

Now use the singular first surface S_n and the degree-(n+1) form
\[
 T_n=x^nw-y^{n+1}.
\]
Use normal coordinates \(u=y-T^n\), \(v=x-T^{n+1}\) in the same chart.
The target generic multiplicity is n. Modulo \(S_n=u\), the other
equation becomes
\[
 (T^{n+1}+v)^n-T^{n(n+1)}.
\]

In characteristic zero its linear term is
\(nT^{n^2-1}v\), with nonzero coefficient in K, so the length is one.
The pair therefore fails for every n>=2.

In characteristic p, write \(n=p^e r\), with \(p\nmid r\). Frobenius gives
\[
 (T^{n+1}+v)^n-T^{n(n+1)}
 =\left((T^{n+1}+v)^r-T^{r(n+1)}\right)^{p^e}.
\]
The inner expression has nonzero linear coefficient, so the generic
length is exactly \(p^e\). The direct support calculation below proves
\[
 \boxed{\quad
 V_+(S_n,T_n)_{\mathrm{red}}=C_n
 \quad\Longleftrightarrow\quad n\text{ is a power of }p.
 \quad}
\]
This is an if-and-only-if for this particular binomial pair.
It is not an exclusion of other pairs when n is not a p-power; Moh's
broader projective monomial theorem supplies positive results in those
other cases by different equations.

There is a direct geometric check. Let r=n in characteristic zero and
r=n/p^e in characteristic p. On w=1 the support consists of the r
distinct curves
\[
 x=\zeta z^{n+1},\quad y=z^n,\qquad \zeta^r=1.
\]
Their closures each have degree n+1 and generic multiplicity p^e
(multiplicity one in characteristic zero). They account for the whole
degree \(n(n+1)\). At w=0 the equations force z=y=0 and leave just
(1:0:0:0), already on their closures. Thus no component at infinity
has been silently omitted.

Frobenius merges these distinct components scheme-theoretically into
one support exactly when r=1. It is a genuine global positive mechanism.
In characteristic zero the deficit relative to C_n alone is
\((n-1)(n+1)\); it is residual degree, not an abstract local defect.

## 3. A positive characteristic-zero control

For n=2 the twisted cubic is an STCI, but its second equation on S_2
needs the mixed term:
\[
 F=yw-z^2,\qquad G=x^2w-2xyz+y^3.
\]
For
\[
 I=(xz-y^2,\ xw-yz,\ yw-z^2),
\]
the exact computation gives
\[
 (F,G)\subset I,\qquad I^2\subset(F,G),
 \qquad\deg S/I=3,\quad\deg S/(F,G)=6.
\]
The generic finite jet length is two, exactly the target. These
containments independently certify the radical equality over QQ.
This keeps failure of the simpler binomial pair separate from failure
of the curve to be an STCI.


The retained [finite normal-jet verifier](https://github.com/markluxton1/STCI/blob/65f5122ff816052fc76e5876d501e7b9ef86253b/research/computations/finite_normal_jet_certificate.m2) supplies the exact twisted-cubic containments and finite characteristic controls; the uniform family statements have the proofs above.


## A terminal hyperplane-jet defect in every degree

**Scoped correctness review (2026-11-23, combined integration):** the terminal hyperplane-jet calculation HJ1–HJ7 and fixed determinant-truncation image equality HJ8–HJ9 were independently reconstructed, using the classical Rao module and inherited finite source-depth theorem. This does not assert pure-target nonemptiness or unrestricted STCI nonexistence.
The fixed rational quartic has Hartshorne--Rao module
\[
 M_C=\bigoplus_nH^1(\mathbf P^3,\mathcal I_C(n))
 \simeq k
\]
concentrated in degree \(1\).  This standard fact is recorded explicitly,
for example, in Zhang's *The SpaceCurves package in Macaulay2*, J. Software
for Algebra and Geometry 8 (2018), 31--48.  The following does not claim a
new Rao-module computation.  Its point is that, for one canonical
hyperplane, the single Rao class becomes an explicit all-degree transverse
source obstruction.

Put
\[
 L=x_3-x_0,\qquad \Pi=V(L).
\]
In characteristic zero the section \(D=C\cap\Pi\) consists of the four
points \(t^4=s^4\).  In the plane \(\Pi\), with \(x_3=x_0\), its ideal is
the complete intersection
\[
 I_{D/\Pi}=(q,r),\qquad
 q=x_0^2-x_1x_2,\qquad r=x_1^2-x_2^2.                 \tag{HJ1}
\]
The first quadric is the restriction of the unique ambient quadric
\(Q=x_0x_3-x_1x_2\); the second is the missing quadratic direction.

For \(e\ge1\), let
\[
 \Pi_e=V(L^e),\qquad D_e=C\cap\Pi_e.
\]
Since \(L\) is a nonzerodivisor on the integral curve \(C\),
\[
 I_C\cap(L^e)=L^eI_C.
\]
Therefore for every \(d,e\) there is an exact restriction sequence
\[
 0\longrightarrow\mathcal I_C(d-e)
 \xrightarrow{\ L^e\ }
 \mathcal I_C(d)
 \longrightarrow
 \mathcal I_{D_e/\Pi_e}(d)
 \longrightarrow0.                                   \tag{HJ2}
\]

The Rao module gives the exact source behavior.  For \(d\ge2\),
\[
 H^1(\mathcal I_C(n))=
 \begin{cases}
  k,&n=1,\\
  0,&n\ge2.
 \end{cases}
\]
Hence
\[
 H^0(\mathcal I_C(d))
 \longrightarrow
 H^0(\mathcal I_{D_e/\Pi_e}(d))                       \tag{HJ3}
\]
is surjective for every
\[
 1\le e\le d-2,
\]
while at the next thickness \(e=d-1\) its cokernel is exactly one
dimensional:
\[
 \boxed{\quad
 \operatorname{coker}\!\left[
 H^0(\mathcal I_C(d))\to
 H^0(\mathcal I_{D_{d-1}/\Pi_{d-1}}(d))
 \right]\simeq k.
 \quad}                                                \tag{HJ4}
\]
Thus all compatible transverse hyperplane jets through normal order
\(d-3\) lift; the first failure occurs at normal order \(d-2\), and it has
dimension one.

Nothing in this cohomological statement depends on the special symmetric
hyperplane.  If \(\ell\) is **any** linear form nonzero on \(C\), put
\(H_e=V(\ell^e)\).  The same nonzerodivisor argument and the same Rao module
give
\[
 H^0(\mathcal I_C(d))\to
 H^0(\mathcal I_{C\cap H_e/H_e}(d))
\]
surjective for \(e\le d-2\), with one-dimensional cokernel at
\(e=d-1\).  Thus the terminal order \(d-2\) is intrinsic to the embedded
quartic; the choice \(L=x_3-x_0\) is used only to exhibit a particularly
simple generator of the missing class.

The missing class is explicit.  On \(C=[s^4:s^3t:st^3:t^4]\),
\[
 r|_C=s^6t^2-s^2t^6
     =-s^2t^2\,L|_C.                                  \tag{HJ5}
\]
Consequently
\[
 L^{d-2}r
 \in H^0(\mathcal I_{D_{d-1}/\Pi_{d-1}}(d))
\]
because its restriction to \(C\) is divisible by \(L^{d-1}\).
It does not lift to an element of \(H^0(\mathcal I_C(d))\): such a lift
would have the form
\[
 F=L^{d-2}r+L^{d-1}\ell
\]
modulo \(L^{d-1}\), with \(\ell\) linear, and restriction to \(C\) would
force
\[
 \ell|_C=s^2t^2.
\]
But the restrictions of ambient linear forms span
\[
 \langle s^4,s^3t,st^3,t^4\rangle
 \subset H^0(\mathbf P^1,\mathcal O(4)),
\]
whose unique missing direction is \(s^2t^2\).  Therefore
\(L^{d-2}r\) spans the cokernel in (HJ4).

Equivalently, (HJ4) has an intrinsic obstruction functional.  If
\([P]\in H^0(\mathcal I_{D_{d-1}/\Pi_{d-1}}(d))\), then
\(P|_C\) is divisible by \(L_C^{d-1}\), and
\[
 \rho_d([P])
 =
 \left[
 {P|_C\over L_C^{\,d-1}}
 \right]
 \in
 {H^0(C,\mathcal O_C(1))
  \over
  \operatorname{im}H^0(\mathbf P^3,\mathcal O(1))}
 \simeq k.                                             \tag{HJ6}
\]
The section lifts to a degree-\(d\) equation through \(C\) exactly when
\(\rho_d([P])=0\).  Formula (HJ5) gives
\(\rho_d(L^{d-2}r)=-[s^2t^2]\ne0\).

### Consequence for the fixed-plane Chow and trace tests

The preceding transverse Chow norm and five-row trace gate use only the
reduced plane section \(D=D_1\).  For every degree \(d\ge3\), (HJ3) with
\(e=1\) says that **every** plane equation of degree \(d\) through \(D\)
already lifts individually to a homogeneous degree-\(d\) equation through
\(C\).  Therefore no obstruction based solely on membership in the
one-plane restriction image can distinguish the desired global source in
the degree range relevant to STCI.

The first genuinely global source information on this hyperplane flag is
instead the terminal scalar \(\rho_d\), at normal order \(d-2\).  A useful
resultant/Chow obstruction must therefore couple the fixed-plane norm to
transverse variation through this order (or use a different genuinely
global compatibility condition).  This does not say that arbitrary
restricted **pairs** lift to proper ambient pairs: common factors,
properness, and simultaneous residual support remain separate conditions.
It only removes the individual one-plane restriction map as a source of
higher-degree obstruction.


### The moving-depth principle

The terminal Rao defect should be compared with the independently proved
[fixed-depth center-jet surjectivity](../torus/chow_matched_equation_layers.md#a-fixed-depth-center-jet-limitation).
For the disjoint center line \(P\), that theorem gives
\[
 H^0(\mathcal I_C(d))\longrightarrow(S/P^N)_d
 \quad\text{surjective whenever}\quad d\ge N+2.        \tag{HJ7}
\]
Thus restrictions coming solely from membership in the individual source
space \(H^0(\mathcal I_C(d))\), at a **fixed** center depth, eventually
disappear as the equation degree grows.  An obstruction using further
joint CI or global support conditions need not be a source-membership
restriction; those conditions are not removed by (HJ7).

The hyperplane calculation attains exactly the first possible moving scale:
its first failure is at thickness
\[
 e=d-1,
\]
equivalently normal order \(d-2\).  In that sense (HJ4) is a sharp model for
what an all-degree source-membership obstruction must look like: counting
bounded first, second, or other fixed jets cannot suffice.  This does not
assert that the
single Rao residue itself obstructs an STCI; actual equations through \(C\)
satisfy it by definition.  Its role is to locate the first global source
information that survives uniformly in degree and to rule out fixed-depth
jet counting as a scalable strategy.

### Fixed determinant truncations forget containment of the quartic in large degrees

**Source-image consequence (independently reviewed, 2026-11-23).**  Work in
characteristic zero with \(S=k[x_0,x_1,x_2,x_3]\),
\(P=(x_0,x_3)\), and \(M=V_+(P)\), the line disjoint from \(C\).
Fix \(r\ge1\) and degrees
\[
 a,b\ge4r+3.
 \tag{HJ8}
\]
Let \(\mathcal U_{a,b}\) be the set of pairs of homogeneous forms of
degrees \((a,b)\) whose binary restrictions to \(M\) have nonzero
resultant, and put
\[
 \mathcal U^C_{a,b}
 =\mathcal U_{a,b}\cap
   \bigl(H^0(\mathcal I_C(a))\times
         H^0(\mathcal I_C(b))\bigr).
\]
Every pair in \(\mathcal U_{a,b}\) is proper and has the finite-flat
plane-pencil cover used in the
[paired determinant](../torus/chow_arrangement_moments.md#a-two-operator-determinant-recovers-the-full-transverse-chow-polynomial).
Use its fixed test sections
\[
 D=x_0^3x_3,\qquad P_4=x_0^2(x_0x_3-x_1x_2),\qquad
 R_4=x_1^4-x_0^3x_3,
\]
with \(P_4\) distinguished from the center ideal \(P\), to define
\[
 \Delta_Y(S_0,T,Z)
   =\sum_{j=0}^{ab}S_0^{ab-j}\Delta_j(T,Z).
\]
Then the following sets of attainable coefficient tuples are equal:
\[
 \boxed{\quad
 \{(\Delta_1,\ldots,\Delta_r):(F,G)\in\mathcal U^C_{a,b}\}
 =
 \{(\Delta_1,\ldots,\Delta_r):(F,G)\in\mathcal U_{a,b}\}.
 \quad}                                                   \tag{HJ9}
\]

To prove this, take any pair in \(\mathcal U_{a,b}\) and set
\(N=4r+1\).  By (HJ7) and (HJ8), its two arbitrary classes modulo
\(P^N\) lift independently to forms through \(C\) of the same degrees.
Their binary leading forms are unchanged.  Nonzero binary resultant
means that the resulting intersection misses \(M\).  It also proves
properness: a common positive-degree surface factor would meet the
projective line \(M\), giving a common binary zero.  Projection from
\(M\) is finite on this projective CI, since a curve in a fiber plane
would meet its line \(M\); Cohen--Macaulayness then gives flatness over
the smooth base curve.  The finite source-depth statement (CHD8) uses
only base-degree layers through \(4j\) for \(\Delta_j\).  These layers
agree for every \(j\le r\), so the tuples agree.  The reverse inclusion
in (HJ9) is immediate.

The same argument for the
[quadric/cubic characteristic towers](../torus/fixed_surface_and_endpoint_algebras.md#two-fixed-test-surfaces-give-an-exact-support-criterion)
uses only \(a,b\ge3r+3\) when retaining both towers through order \(r\).
No assertion about equality of full cycles or full characteristic towers
is involved.

This is stronger than a cycle-level cancellation control but is not a
nonexistence theorem or a construction of pure-target jets.  It does
**not** prove that \(\Delta_1=\cdots=\Delta_r=0\) has any solution on
either side of (HJ9).  It says that, in the degree range (HJ8), a fixed
determinant truncation cannot distinguish equations containing \(C\)
from arbitrary proper equations avoiding \(M\).  A contradiction in
that truncation would already have to come from the general finite-CI
source algebra; any further use of the marked curve must enter through
deeper source data or an additional joint global condition.  In particular,
the marked-containment condition adds no restriction to this tuple for
\(r\le\lfloor(\min(a,b)-3)/4\rfloor\).  The
roots-of-unity cycle construction remains a distinct warning, since it
does not realize its cycles by actual equation pairs.
