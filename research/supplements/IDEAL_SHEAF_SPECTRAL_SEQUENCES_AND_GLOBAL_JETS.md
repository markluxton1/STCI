# Ideal-sheaf spectral sequences and finite global equation jets

Exploratory continuation, 2026-10-31, from commit
`38f5f00563c9bb2f5c87769a619bf474854fa9c2` in `9cf8/STCI`.
The new claims are independently reviewed source-level deductions; the exact
review scope is recorded below. No canonical result or research status changes here.

Fix the actual embedding
\(C=C_0=[s^4:s^3t:st^3:t^4]\subset P=\mathbf P^3\), and write
\(I=\mathcal I_C\). Use characteristic zero and coefficients over
\(\mathbf Q\), with geometric existence over \(\overline{\mathbf Q}\),
except that the finite global-extension bound in section 3 is characteristic
free. All powers are **ideal sheaf powers**. In homogeneous computations
they correspond to sheafification and saturation, not an automatic
identification with unsaturated polynomial ideal powers.

The useful new point is a finite, linear global-source calculation. The
actual ideal-adic filtration has a Cech spectral sequence whose surviving
sections recover actual homogeneous equations at an explicit depth. This
organizes one compatibility problem without identifying it with either
Koszul spectral sequence or the nonlinear lifting of a root divisor.
The subsequent [intrinsic review and generalization](INTRINSIC_GEOMETRY_AND_STCI_COMPLEXITY.md)
formulates the source deficit without coordinates, proves an existential
cutoff for smooth connected curves in projective space and an explicit
quadric-family bound, and generalizes the octic correction recursion.

## 1. Keep the actual diagram and distinguish its spectral sequences

For two actual hypersurfaces \(X=V(F_a)\), \(Y=V(G_b)\), put
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
embedding. The [nine-embedding diagram](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md)
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
[ideal filtrations, section 8](IDEAL_FILTRATIONS_AND_44_FILTERED_EXCLUSION.md)
and [the normal Tor comparison, section 3](DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md).
The comparison \(0\to\Delta\to Q\to\operatorname{gr}D\to0\) is promoted as
[R-0030](../results/local_filtration_comparison_defect.md); that does not
promote every continuation in those supplements.

For a regular hypersurface pair, \(\mathcal O_X\otimes^L\mathcal O_Y\)
already has no higher homology and equals \(\mathcal O_Z\). Its derived
restriction to \(C\) is a different operation. Neither operation alone
supplies the missing higher embedded gluing maps.

## 2. The finite Cech filtration gives actual source-image obstructions

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

## 3. A characteristic-free global-extension cutoff for this quartic

**Claim.** For \(d\ge0\) and \(m>d\),
\[
H^0(P,I^m(d))=H^1(P,I^m(d))=0.
\tag{4}
\]
Consequently, for every \(N\ge d\), restriction is an isomorphism
\[
H^0(P,\mathcal O_P(d))
\xrightarrow{\sim}
H^0\!\left(P,(\mathcal O_P/I^{N+1})(d)\right).
\tag{5}
\]
For \(0\le r\le N+1\), it also gives
\[
H^0(P,I^r(d))\xrightarrow{\sim}H^0(P,T_{r,N}(d)).
\tag{6}
\]

**Proof.** The [quadric flag sequence](ACTUAL_EQUATION_SPACES.md), equation (3),
uses \(C\) of class \((1,3)\) on the smooth quadric \(Q\):
\[
0\to I^{j-1}(e-2)\xrightarrow{q}I^j(e)
\to\mathcal O_Q(e-j,e-3j)\to0.
\]
Apply this for \(j=1,\ldots,m\), with \(e=d-2m+2j\).
The starting term is \(\mathcal O_P(d-2m)\), and every successive
quotient is
\[
\mathcal O_Q(d-2m+j,d-2m-j).
\]
If \(m>d\), both bidegrees are negative. Such a line bundle on
\(\mathbf P^1\times\mathbf P^1\) has zero \(H^0\) and \(H^1\): each
summand of its \(H^1\) in the Kunneth formula has a negative-degree
\(H^0(\mathbf P^1,\mathcal O(t))\) factor. The starting term has zero
\(H^0\) and \(H^1\) as well. The long exact sequences prove (4).
Here the only external cohomology facts are
[projective-space line-bundle cohomology](https://stacks.math.columbia.edu/tag/01XS)
and [Kunneth over a field](https://stacks.math.columbia.edu/tag/0BEC).
Finally use \(m=N+1>d\) in
\(0\to I^{N+1}(d)\to I^r(d)\to T_{r,N}(d)\to0\), including \(r=0\).
This proves (5) and (6).

The word **compatible** is essential: (5) concerns global sections on the
actual embedded neighborhood \(V(I^{N+1})\), not arbitrary sections of the
direct sum of its normal graded pieces. This finite-depth statement is
stronger than saying that each leading symbol is available. It is still a
bound depending on the prescribed degree, not a bound on possible witness
degrees for an arbitrary STCI problem.

The proof works over any field for this split quadric flag. The balanced
conormal splitting \(E=\mathcal O_{\mathbf P^1}(-7)^{\oplus2}\), used in the
next section, requires the characteristic-zero hypothesis retained in
[R-0020](../results/quartic_conormal_characteristic_jump.md).

## 4. Sextic equation jets: where the source deficit is detected

The characteristic-zero calculation uses
\[
\operatorname{Sym}^nE(6)=
\mathcal O_{\mathbf P^1}(24-7n)^{\oplus(n+1)}.
\]
The accepted [actual source calculation](ACTUAL_EQUATION_SPACES.md) gives
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

In (1), this means
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
[eleven sextic symbol equations](CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-global-realization-incidence).
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

## 5. What this contributes to bounded STCI compatibility

For prescribed degrees \(a,b\), the sections representing \(F_a,G_b\)
on any actual neighborhood of order \(N\ge\max(a,b)\) come from unique
homogeneous forms. Requiring them to vanish on \(C\) amounts to using
\(T_{1,N}(a)\) and \(T_{1,N}(b)\). This gives an exact finite global-source
description before imposing intersection conditions.

Combine it with the independently reviewed
[generic finite-jet support criterion](../synthesis/finite_normal_jets.md).
For nonzero forms of positive degrees, if \(M=ab/4\) is an integer, sole
reduced support on \(C\) is equivalent to
\[
\operatorname{length}_{R}
R/\bigl((F,G)+\mathfrak m^{M+1}\bigr)=M,
\quad R=\mathcal O_{P,\eta_C}.
\tag{7}
\]
Hence
\[
N\ge\max(a,b,M)
\tag{8}
\]
is sufficient to place both the global-source condition and the generic
support test on one finite actual neighborhood. The extra layer in (7)
also detects failure of properness. If \(4\nmid ab\), degree exhaustion
already rules out such a pair. All coefficients remain constants over the
ground field, with geometric existence over its algebraic closure.

This is an exact organization of the bounded problem, not a claim that the
jet representation is computationally smaller than directly parameterizing
homogeneous forms. In particular, the actual source dimensions are
\(O(d^3)\); one should impose these linear compatibility conditions before
nonlinear root or contact conditions whenever possible. Keeping extra
independent normal coefficients would enlarge the search with candidates
that no global surface can realize.

### The two degree rows use the source filter at different orders

Under the precise saturated, full generic initial-CI, order-two,
movement-two hypotheses retained in the
[torsion-two continuation](QUADRATIC_ROOT_TORSION_TWO_REDUCTION.md#7-connection-to-the-already-bounded-actual-degree-rows),
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

For the movement-two laboratory, [R-0007](../results/quadratic_root_obstruction_model.md)
concerns a root divisor on the exceptional ruled surface. Call that divisor
\(\Sigma\) here to avoid confusing it with \(Z=X\cap Y\). Its first and
second obstructions are nonlinear Cech lifting classes on the blowup.
[R-0006](../results/actual_ci_smooth_root_bridge.md) supplies a one-way
necessity bridge from actual CI data only under its stated saturation,
full initial-CI, smooth-root, and relation-gap hypotheses. No comparison
identifying these root classes with the differentials in (1), or with
either Koszul spectral sequence, has been established. The finite-source
calculation instead supplies a rigorously separate compatibility filter.

## Evidence and review

- Existing diagram, Koszul distinctions, actual source dimensions, and the
  fixed-pair support test are reused from the proof homes linked above;
  their exact promoted or source-level status is retained.
- The `global_jet_bound_review` reviewer independently reconstructed the
  new cutoff (4)–(6), its application (8), the filtered Cech indexing, and
  the implications of the computed ranks, including (10)–(12). The reviewer
  explicitly treated the numerical ranks as a dependency on the separate
  implementation review. Its wording correction distinguishes the 11
  conditions from their 22-dimensional kernel. No mathematical finding
  remains unresolved within these claims.
- The same reviewer independently reconstructed the subsequent octic
  application (13)–(15), including the subbundle property, global
  divisibility, exact dimensions, and residual \(q^4\) freedom. The
  accepted qualification is that the 15 and 11 constraints are nested;
  no preferred splitting or identification with root obstructions is used.
- The `sextic_cech_review` reviewer independently checked coverage by the two
  affine charts, both coordinate frames, the degree-six transition, Laurent
  gap obstruction, correction signs, and completeness of all lift freedoms.
  It then ran the retained script over the rationals and confirmed every
  table entry, the rank-15 restriction to pure cubics, and rank zero on the
  remaining cubic direction at order five.
- As an independent endpoint check, that reviewer expanded 28 actual
  sextics generated by \(q^2S_2\), \(q\) times the three cubic ideal
  generators times \(S_1\), and the six quadratic products of the cubic
  generators. Their **two-chart** jet span has rank 23, the computed Cech
  basis has rank 23, and their combined span has rank 23. Both quadratic
  projections have rank 22. Thus the check compared the actual subspaces,
  rather than only matching dimensions. This separately constructed check
  was diagnostic review evidence; the retained calculator and the proof of
  its exhaustive recursion above reproduce the claimed ranks.
- Reviewed calculator SHA-256:
  `2f2b84549cb7dbc8cd8a6c402a2795730fd08986dc2fc51a50c3445ee4ccf00d`.
  Execution used Python with SymPy 1.14.0. Reproduction, from the repository
  root in an environment containing SymPy:

      python3 research/computations/sextic_global_jet_cech.py

  The JSON reports dimensions `33,49,34,23,23`, quadratic projection ranks
  `33,33,33,22,22`, connecting ranks `0,0,15,11,0`, the restricted ranks,
  and the identification of the remaining cubic direction with `q^3`.
  All arithmetic is rational; no finite-field extrapolation is used.
- Local links and whitespace were checked. Canonical records were unchanged;
  their metadata validator was not rerun. No full root-incidence elimination
  or new search for actual surface pairs was performed in this continuation.
- No unrestricted STCI exclusion, uniform witness-degree bound, complexity
  lower bound, or identification of root obstruction classes is claimed.
