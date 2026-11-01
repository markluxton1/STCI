# Intrinsic geometry behind the finite compatibility calculations

Review and generalization, 2026-10-31, from source commit
`faaee8a787622db7dab72f9c63fd809c891a7463` in `9cf8/STCI`.
New deductions here are independently reviewed source-level results, with the
review scope recorded below. They do not promote canonical results or change the
unrestricted characteristic-zero STCI status.

The purpose is to extract reusable geometry from the
[root and certificate calculations](STCI_COMPLEXITY_AND_QUADRATIC_ROOTS.md)
and [finite global jets](IDEAL_SHEAF_SPECTRAL_SEQUENCES_AND_GLOBAL_JETS.md).
The numerical quartic results remain useful examples; their coordinate
presentations are not the intended general objects.

The [cross-branch synthesis](COMPLEXITY_LANE_SYNTHESIS.md) places these results
against the committed spectral, arithmetic, carrier and projection work and
records the recommended actual-source continuation.

## 1. Intrinsic to which data?

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

## 2. The source deficit is a canonical filtration, not a matrix size

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

The intrinsic construction is the ideal-adic filtration on derived global
sections of \(T_{r,N}(d)\). A Cech complex computes it. The standard
[filtered-complex spectral sequence](https://stacks.math.columbia.edu/tag/012K)
has
\[
E_1^{p,q}=H^{p+q}(C,\operatorname{Sym}^pE\otimes L^d|_C),
\qquad d_s:(p,q)\mapsto(p+s,q-s+1).
\]
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

## 3. Finite realization: existence versus an effective bound

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
[formal geometry, section 5](../synthesis/formal_residual_visibility.md).
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

## 4. The correction recursion is an exact sequence of obstruction spaces

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

## 5. The spectral torsion calculation extends to every power

Let \(\Sigma\) be a smooth projective genus-one curve over an algebraically
closed field, \(\pi:\Sigma\to\mathbf P^1\) a degree-two map,
\(A=\pi^*\mathcal O(1)\), and \(B\) any degree-two line bundle. Put
\(\eta=BA^{-1}\). For every integer \(n\),
\[
\pi_*B^n\simeq
\begin{cases}
\mathcal O(n-1)^{\oplus2},&\eta^n\not\simeq\mathcal O_\Sigma,\\
\mathcal O(n)\oplus\mathcal O(n-2),&\eta^n\simeq\mathcal O_\Sigma.
\end{cases}
\tag{7}
\]
Finite flatness makes the pushforward a rank-two bundle. Riemann–Roch gives
degree \(2n-2\), while \(h^0(\pi_*B^n(-n))=h^0(\eta^n)\) is zero or one.
Splitting on \(\mathbf P^1\) leaves exactly (7). This reuses the
[degree-four splitting proof](STCI_COMPLEXITY_AND_QUADRATIC_ROOTS.md#4-a-geometric-classification-of-the-minimal-second-syzygies)
for all powers; it needs no chosen elliptic origin and is characteristic free.

For a smooth \((2,2)\) divisor, with \(A,B\) its two ruling bundles and
\(n\ge2\), its divisor sequence gives
\[
0\to\mathcal O(-2)^{n-1}\to\mathcal O^{n+1}
\to\pi_*B^n\to0.
\]
Dualizing and twisting by \(n-2\) gives a square coefficient matrix of
size \(n^2-1\). Its kernel has dimension one exactly when \(\eta^n=1\),
and zero otherwise. The old \(3\times3\) and \(15\times15\) detectors
are its \(n=2,4\) cases. This is a set-theoretic statement on the smooth
locus; no multiplicities or singular-root conclusion are supplied.

This also illustrates a genuine algorithmic choice. If the Jacobian and
the point \(\eta\in\operatorname{Pic}^0(\Sigma)\) are already represented
with usable group operations, the same condition can be checked by binary
doubling and addition in \(O(\log n)\) group operations. Constructing that
representation, field extensions, coefficient growth, and bit costs are
additional tasks. The coefficient-matrix dimension grows quadratically
in \(n\); it can still be preferable for an algebraic family in which
polynomial equations and specialization are the desired output. At fixed
\(n=4\), this is no asymptotic improvement claim for the existing solver.

An arbitrary change of ruling coordinates preserves (7). It simplifies an
actual lifting problem only when the higher ambient transitions and operator
are transported too. Orientation then survives in those data. Keeping the
operator fixed permits only genuine ambient symmetries, such as the proved
torus and reversal. The torsion condition is intrinsic to \((\Sigma,A,B)\),
not to \(\Sigma\) alone and not a complete ambient compatibility test.

## 6. Certificate selection depends on closed support, not total length

Let \(B\) be a nonzero finite commutative unital algebra over an infinite
field \(k\), with \(c\) maximal ideals. If \(s_0,\ldots,s_{m-1}\)
generate its unit ideal, at most \((m-1)c\) values \(t\in k\) make
\(\sum_jt^js_j\) a nonunit. In each residue field the corresponding
polynomial is nonzero and has at most \(m-1\) roots in \(k\). A unit is
exactly an element nonzero in every residue field; nilpotents do not alter
this criterion.

Over \(\mathbf Q\), one of the integers \(0,\ldots,(m-1)c\) therefore
works. The reviewed first-stage algebra in the
[torsion-two boundary](QUADRATIC_ROOT_TORSION_TWO_REDUCTION.md#6-a-bounded-scalar-compression-for-the-finite-first-stage)
is a product of a four-dimensional \(\mathbf Q\)-algebra and a
four-dimensional algebra over the degree-18 number field \(K\).
It has at most eight closed points over \(\mathbf Q\). With sixteen
residues, the earlier sufficient search range \(0,\ldots,1140\) improves to
\[
0\le t\le120.
\tag{8}
\]
This uses the established irreducibility of \(P_{18}\) and the two exact
first-stage dimensions. Conjugate embeddings do not multiply the number of
rational choices: a nonzero residue-field element stays nonzero under every
embedding. No successful \(t\) or inverse is supplied here.

This controls scalar selection, not certificate bit size. Residue-field
degrees still affect arithmetic and storage; the ordered generating list
still affects \(m\). Over a finite field the entire set of choices can be
bad: in \(B=\mathbf F_q^q\), the elements \(s_1=1\) and \(s_0(x)=-x\)
generate the unit ideal, yet \(s_0+ts_1\) has a zero factor for every
\(t\in\mathbf F_q\).

## 7. What to measure in the next calculation

The useful parameters describe different tasks:

| Task | Geometric quantity | Algorithm-dependent quantity or missing bound |
| --- | --- | --- |
| Recover fixed-degree global sources | A depth where restriction is onto; a depth where it is bijective; the ranks in (2) | Constructing the connecting maps and recognizing the final depth |
| Solve linear compatibility | Actual source and correction dimensions; nested quotient (6) | Basis density, denominators, and coefficient growth |
| Solve nonlinear compatibility | The specified root/contact incidence and its rank strata | Elimination order, chosen projection, and coverage of exceptional charts |
| Verify a supplied proper pair | Generic transverse length \(ab/\deg C\) | Constructing its actual normal jets and exact function-field arithmetic |
| Compress a finite exclusion | Closed support, residue fields, and the ideal generated by obstruction sections | Selecting a scalar, producing its inverse, and storing a certificate |
| Decide unrestricted STCI | The least possible witness degrees, if a witness exists | No uniform witness bound is proved here |

For example, the nineteen-point exceptional base is a determinantal locus
of the **specified** elimination map and projection. It is invariant under
compatible changes of bases of that map, but a different projection or
linear subsystem can produce another locus. Its nineteen points and the
length-76 fibers are not invariants of the abstract spectral curve.

Once the finite connecting matrices are supplied, their kernel and image
calculations are ordinary linear algebra. If their dimensions and all
intermediate compatible-section dimensions are bounded by \(D\), processing
\(N\) stages by dense elimination takes at most \(O(ND^3)\) field operations.
This excludes construction of the matrices and growth of exact coefficients;
it is not an end-to-end bit bound. Precomputing the actual homogeneous
source may avoid constructing much larger formal jet spaces altogether.

In families, fixed bundle ranks and base-change compatibility must be checked
before treating the images as vector bundles or transferring fiber ranks.
A flat family of curves alone does not establish the required behavior of
every higher-page differential. Similarly, intrinsic nonlinear parameter
dimension is not itself a runtime bound.

The [actual octic comparison](ACTUAL_OCTIC_ROOT_LIFT_COMPARISON.md) now
carries the flag recursion (6) into first root-lift membership. Restriction
to the embedded lifted divisor gives the actual map, with all correction
freedoms retained. Its target has dimension six to nine, and a seed
calculation produces proper first-compatible pairs with residual degree 32.
Extending that map across the remaining root strata is distinct from
identifying spectral-sequence classes. Replacing it by a larger unified
complex without further comparisons would add notation without improving
the decision problem.

## Review and scope

- Existing exact quartic ranks, exclusions, and field computations are reused
  at the committed states above. This review did not rerun their CAS proofs.
- `generalize_quadric_cutoff` independently derived the family flag bound
  (4)–(5), its hypotheses, and the balanced-quadric control. The formulation
  distinguishes vanishing obstruction maps from possibly nonzero \(H^1\).
- `intrinsic_filtration_review` independently reconstructed (1)–(3), the
  needed G3 section-extension input, and the general flag quotient (6).
  Its correction removes an unnecessary \(H^1\) hypothesis from the general
  recursion, retaining it only as a sufficient surjectivity criterion. Its
  final wording correction also preserves possible surjectivity when that
  \(H^1\) is nonzero. The conditional linear-algebra cost and stopping
  criteria passed its final review.
- `root_complexity_generalization_review` derived (7)–(8) and clarified the
  coordinate, polarization, and elimination-projection dependence.
  `global_jet_bound_review` independently reconstructed both proofs and
  checked that the number-field irreducibility is required for (8). It also
  checked the explicitly conditional group-operation comparison. Matrix
  dimension is distinguished from dense storage size.
- These are reviewed source-level deductions and standard-theorem
  applications, not claims of novelty in the literature. No canonical
  metadata, research priority, or unrestricted STCI status is changed.
