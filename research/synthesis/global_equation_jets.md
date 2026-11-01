# Global equation jets and their intrinsic source filtration

Fix an embedded curve, its polarization and its actual ideal sheaf. Compatible
jets on that embedded neighborhood are different from independently chosen
sections of its normal graded pieces. The finite filtered-cohomology argument
below measures their difference, gives global realization cutoffs, and computes
the fixed quartic's sextic source deficit. All powers are ideal **sheaf** powers;
homogeneous representatives require sheafification and saturation.

These are independently source-reviewed provisional deductions from frozen
commit `aad349d1c413e0de511dd6b62c2194faf706fda9`, consolidated without a new
computation or canonical promotion. General lemmas retain their stated fields
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
embedding. The [nine-embedding diagram](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md)
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

The first two constructions and their distinction are retained in
[ideal filtrations, section 8](../supplements/IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md)
and [the normal Tor comparison, section 3](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md).
The comparison \(0\to\Delta\to Q\to\operatorname{gr}D\to0\) is promoted as
[R-0030](../results/local_filtration_comparison_defect.md); that does not
promote every continuation in those supplements.

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
[formal geometry, section 5](formal_residual_visibility.md).
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
The accepted [actual source calculation](../supplements/ACTUAL_EQUATION_SPACES.md) gives
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
[sextic_global_jet_cech.py](../computations/sextic_global_jet_cech.py).

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
[eleven sextic symbol equations](../supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-global-realization-incidence).
Thus a leading symbol can be globally compatible through quartic normal
order and still fail to be the symbol of any global sextic. This is a
specific higher-gluing obstruction, not merely a count of extra parameters.

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
[torsion-two continuation](quadratic_root_torsion_two_lifting.md),
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

The full [generic finite-normal-jet criterion](finite_normal_jets.md) already
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


For the movement-two laboratory, [R-0007](../results/quadratic_root_obstruction_model.md)
concerns a root divisor on the exceptional ruled surface. Call that divisor
\(\Sigma\) here to avoid confusing it with \(Z=X\cap Y\). Its first and
second obstructions are nonlinear Cech lifting classes on the blowup.
[R-0006](../results/actual_ci_smooth_root_bridge.md) supplies a one-way
necessity bridge from actual CI data only under its stated saturation,
full initial-CI, smooth-root, and relation-gap hypotheses. No comparison
identifying these root classes with the filtered-Čech differentials, or with
either Koszul spectral sequence, has been established. The finite-source
calculation instead supplies a rigorously separate compatibility filter.

## Intrinsic Künneth and torus-weight decomposition of the sextic and octic deficits

*(Authored by Gemini on `evaluate_toric_integration_stci`; independently reviewed by Gemini subagent and verified in [`verify_toric_jet_deficits_and_unequal_vgit.py`](../computations/verify_toric_jet_deficits_and_unequal_vgit.py).)*

The \(11\)-dimensional sextic quadratic-symbol deficit \(\operatorname{coker}(\sigma_{6,2})\) and the \(26\)-dimensional octic cubic-symbol deficit admit an intrinsic, characteristic-free geometric proof via the quadric conormal flag \(C_0 \subset Q = V(q) \subset \mathbf P^3\) and decompose into multiplicity-free (or multiplicity-\(\le 2\)) weight blocks under the curve's preserving \(\mathbf G_m\)-action \(T\) (centered weights \((-2,-1,1,2)\)).

### 1. Intrinsic Künneth splitting \(\operatorname{coker}(\sigma_{6,2}) \cong H^1(Q, \mathcal O_Q(2,-2)) \oplus H^1(Q, \mathcal O_Q(3,-3))\)

Let \(L = (\mathcal I_Q/\mathcal I_Q^2)|_{C_0} \cong \mathcal O_{\mathbf P^1}(-8)\) (trivialized in degree \(2\) by \(\ell = \sigma_{2,1}(q)\) of centered weight \(0\)) and \(M_Q = \mathcal I_{C_0/Q}/\mathcal I_{C_0/Q}^2 \cong \mathcal O_Q(-1,-3)|_{C_0} \cong \mathcal O_{\mathbf P^1}(-6)\). Since \(H^1(C_0, E(4)) = 0\) and \(H^1(\mathbf P^3, \mathcal I_{C_0}(4)) = 0\) in every characteristic, the actual equation filtration \(0 \to V_4 \xrightarrow{\cdot q} V_{6,2} \to H^0(Q, \mathcal O_Q(4,0)) \to 0\) (after quotienting out \(\ker \sigma_{4,1} = V_{4,2} = k\cdot q^2\) and \(\ker \sigma_{6,2} = V_{6,3} = k\cdot q^3\)) maps injectively into the symbol filtration:
\[
\begin{array}{ccccccccc}
0 & \longrightarrow & V_4 / (k \cdot q^2) & \xrightarrow{\;\cdot q\;} & V_{6,2} / (k \cdot q^3) & \longrightarrow & H^0\bigl(Q, \mathcal O_Q(4, 0)\bigr) & \longrightarrow & 0 \\
& & \downarrow \sigma_{4,1} \;(17\hookrightarrow 20) & & \downarrow \sigma_{6,2} \;(22\hookrightarrow 33) & & \downarrow \mathrm{res}_{C_0} \;(5\hookrightarrow 13) & & \\
0 & \longrightarrow & H^0(C_0, E(4)) & \xrightarrow{\;\cdot \ell\;} & H^0(C_0, \operatorname{Sym}^2 E(6)) & \longrightarrow & H^0(C_0, M_Q^{\otimes 2}(6)) & \longrightarrow & 0
\end{array}
\tag{16}
\]
By the snake lemma:
- From \(0 \to \mathcal I_{C_0}^2(4) \to \mathcal I_{C_0}(4) \to E(4) \to 0\) and \(0 \to \mathcal I_{C_0}(2) \xrightarrow{\cdot q} \mathcal I_{C_0}^2(4) \to \mathcal O_Q(2,-2) \to 0\), we have \(\operatorname{coker}(\sigma_{4,1}) \cong H^1(\mathbf P^3, \mathcal I_{C_0}^2(4)) \cong H^1(Q, \mathcal O_Q(2,-2))\), which by Künneth has dimension \(3 \cdot 1 = 3\) and centered \(T\)-weights **\(\{-3, 0, +3\}\)** (multiplicity \(1\) each).
- From \(0 \to \mathcal O_Q(3,-3) \to \mathcal O_Q(4,0) \xrightarrow{\mathrm{res}_{C_0}} M_Q^{\otimes 2}(6) \cong \mathcal O_{\mathbf P^1}(12) \to 0\) on \(Q\), we have \(\operatorname{coker}(\mathrm{res}_{C_0}) \cong H^1(Q, \mathcal O_Q(3,-3))\), which by Künneth has dimension \(4 \cdot 2 = 8\) and centered \(T\)-weights **\(\{-5, -4, -2, -1, +1, +2, +4, +5\}\)** (the \(8\) non-multiples of \(3\) in \([-6, 6]\), multiplicity \(1\) each).

Because the centered weight supports \(\{-3, 0, +3\}\) and \(\{-5, -4, -2, -1, +1, +2, +4, +5\}\) are disjoint, the snake-lemma exact sequence splits canonically as a \(T\)-module in every characteristic:
\[
  \operatorname{coker}(\sigma_{6,2}) \cong H^1\bigl(Q, \mathcal O_Q(2, -2)\bigr) \oplus H^1\bigl(Q, \mathcal O_Q(3, -3)\bigr) \cong \bigoplus_{w=-5}^{5} k_{[w]}. \tag{17}
\]
Thus the \(11\) missing sextic quadratic-symbol equations are **multiplicity-free under \(T\)**, with exact dimension \(1\) in each of the \(11\) centered weights \(w \in [-5, 5]\):
- \(H^0(C_0, \operatorname{Sym}^2 E(6))\) (\(\dim = 33\)) is supported on \(w \in [-6, 6]\) with profile \((1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1)\),
- \(\operatorname{im}(\sigma_{6,2}) \cong V_{6,2}/(k\cdot q^3)\) (\(\dim = 22\)) is supported on \(w \in [-6, 6]\) with profile \((1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1)\).

Similarly, in the octic cubic-symbol sequence (15), the \(15\)-dimensional quotient \(H^0(C_0, M_Q^{\otimes 3}(8)) = H^0(C_0, \mathcal O_{\mathbf P^1}(14))\) is multiplicity-free on centered weights \(w \in [-7, 7]\). Combining this with (17) shows that the \(26\)-dimensional octic cubic-symbol deficit \(H^0(\operatorname{Sym}^3 E(8)) / (\ell \cdot \operatorname{im}\sigma_{6,2})\) is supported on centered weights \(w \in [-7, 7]\) with profile \((1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1)\) (\(\dim = 2\) for \(|w| \le 5\) and \(\dim = 1\) for \(|w| \in \{6, 7\}\)).

### 2. Unequal-degree and octic VGIT parameter spaces for \((5, 8)\), \((6, 16)\), and \((8, 8)\)

Combining the [surface-pair VGIT framework](vgit_surface_pairs_and_full_limits.md) with the intrinsic primary-power containment \(I_{C_0}^{ab/4} \subset J \subset I_{C_0}\) gives exact parameter-space dimensions, fiber ranks, and \(T\)-weight ranges for the remaining unequal-degree and octic frontier rows:

| Degree pair \((a, b)\) | Intrinsic Hilbert locus \(H_{ab/4}\) | Surface-pair parameter space | Base / fiber dimensions | Centered \(T\)-weight / Plücker range |
| :---: | :---: | :--- | :--- | :--- |
| \((5, 8)\) | \(H_{10}\) (\(m = 10\)) | Projective bundle \(\mathbf P(E) \to \mathbf P(V_5)\), fiber \(\mathbf P(V_8 / F_5 S_3)\) | \(\dim V_5 = 35\), \(\operatorname{rk} E = 132 - 20 = 112\), \(\dim \mathbf P(E) = 145\) | Base \(V_5\): \([-7, 7]\); \(V_8\): \([-13, 13]\) |
| \((6, 16)\) | \(H_{24}\) (\(m = 24\)) | Projective bundle \(\mathbf P(E) \to \mathbf P(V_6)\), fiber \(\mathbf P(V_{16} / F_6 S_{10})\) | \(\dim V_6 = 59\), \(\operatorname{rk} E = 904 - 286 = 618\), \(\dim \mathbf P(E) = 675\) | Base \(V_6\): \([-9, 9]\); \(V_{16}\): \([-29, 29]\) |
| \((8, 8)\) | \(H_{16}\) (\(m = 16\)) | Equal-degree \(X_8 = \operatorname{Gr}(2, V_8)\) and double-octic \(X_{8,2} = \operatorname{Gr}(2, V_{8,2})\) | \(\dim V_8 = 132\) (\(\dim X_8 = 260\)); \(\dim V_{8,2} = 80\) (\(\dim X_{8,2} = 156\)) | \(X_8\): \(51\) Plücker weights \([-25, 25]\); \(X_{8,2}\): \(39\) Plücker weights \([-19, 19]\) |

Over any \(T\)-eigenform \(F_a \in V_a[w_a]\), the quotient fiber \(E_{[F_a]} = V_b / (F_a S_{b-a})\) is \(T\)-graded with \(\dim E_{[F_a]}[w] = \dim V_b[w] - \dim S_{b-a}[w - w_a] \ge 0\).

## Evidence and computation boundary

The frozen source's `global_jet_bound_review` independently reconstructed the
filtered-Čech indexing, quartic cutoff, exact minimum-sextic-cutoff deductions
and octic application. `generalize_quadric_cutoff` checked the split-quadric
family bound and balanced control; `intrinsic_filtration_review` checked the
intrinsic deficit, G3 section-extension input and general flag recursion.
The recursion uses no unnecessary H1 assumption: only the actual image J
counts unless surjectivity is established, and nonzero H1 does not imply failure.

The separate `sextic_cech_review` checked both chart frames, coverage, degree-six
transition, Laurent gap, correction signs and all lift freedoms, then ran the
[retained calculator](../computations/sextic_global_jet_cech.py) over Q with
SymPy1.14.0. Its reviewed SHA256 is
`2f2b84549cb7dbc8cd8a6c402a2795730fd08986dc2fc51a50c3445ee4ccf00d`.
It confirmed dimensions33,49,34,23,23; quadratic ranks33,33,33,22,22;
connecting ranks0,0,15,11,0; rank15 on pure cubics; and zero order-five
obstruction on their remaining q³ direction. A separately constructed
two-chart span of28 actual sextic generators had rank23, quadratic rank22,
and combined rank23 with the Čech basis. Thus source-subspace equality was
checked beyond matching dimensions. That diagnostic is review evidence;
the retained exhaustive recursion is the reproducible support.

The calculator is copied unchanged from the frozen source and was not rerun
for consolidation. It uses rational arithmetic and SymPy; no finite-field
extrapolation, full root-incidence elimination or actual pair construction
is claimed. Reproduction is `python3 research/computations/sextic_global_jet_cech.py`.
The source review treats its numerical ranks as a separate implementation
and executed-evidence dependency. Existing full finite-length and fixed-symbol
lifting proofs remain in [finite normal jets](finite_normal_jets.md) and
[global lifting interfaces](global_lifting_interfaces.md).
