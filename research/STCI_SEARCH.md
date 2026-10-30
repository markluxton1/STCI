# If C were a STCI, how would we find its equations?

Search record, begun October 28 and continued through October 30, 2026.
The curve throughout is
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]
The target is an actual homogeneous pair over an algebraically closed
characteristic-zero field with reduced projective intersection exactly C.
Existence and nonexistence remain open. This document selects and records
searches; it is not a new canonical result. New deductions below are
independently reviewed provisional work, with their source proofs and
computations linked explicitly.
The [baseline integration review](notes/2026-10-29-stci-search-integration-audit.md)
checks the earlier synthesis, its scope boundaries and navigation changes.
The [subsequent continuation](notes/2026-10-29-search-continuation.md)
links the new family calculations and their separate independent audits;
its full projection-locus endpoint remains unfinished.

The [adversarial research game](STCI_GAME.md) is the current strategy
ledger. The existence side develops constructions and the non-existence
side independently seeks the largest exclusions and general principles;
both may pursue side research using the full record. New results must
change that shared understanding, not merely accumulate as isolated
family calculations.

## 1. The question and the search cycle

Generate actual global equations or a parametrized carrier with an exact
global section test. Test properness, contact and support. Record the
first reason for failure, change the source or constraints in response,
and repeat. A successful local model, large parameter space, or residual
bound is useful when it changes this search; it is not itself the target.

For every proper pair retain
\[
[V(F_a,G_b)]=\ell_C[C]+R,\qquad \deg R=ab-4\ell_C.
\]
Thus the contact score is \(4\ell_C/(ab)\), with score one the sole-support
target. Record actual residual support when available. Exceptional vertical
curves, generic symbols and full residual schemes are distinct data.

Every substantial search entry should specify:

1. The coefficient field, degrees, literal family and why it might work.
2. Which prior exclusion hypotheses it avoids and which remain untested.
3. The actual global coefficient space, with common factors removed.
4. The exact test, completed output, and scope of any modular certificate.
5. What the outcome changes in the next search. A timeout is an unfinished
   computation; a finite empty family is not a general exclusion.

## 2. What the accumulated record tells us to search

The following are inputs, not new re-verifications of accepted proofs.

| Input and authority | Consequence for generating candidates |
| --- | --- |
| [R-0001](results/quartic_carrier_exclusion.md), promoted | Factor reduction permits searching integral equations; both defining degrees must be at least five. Do not reopen quartic mates. |
| Thoma's one-binomial exclusion and Hellus–Hübl's extremal-weight theorem, [source review](notes/2026-10-28-stci-search-candidates.md) | Characteristic-zero witnesses must escape binomial and torus-homogeneous carriers. Use mixed weights and test both extremal gcds and their membership in I_C. |
| [R-0002](results/cartier_singleton_lift.md), promoted, conditional | A constructive source is the degree-eight smooth-quadric or cone normalization, or degree-sixteen plane normalization. Actual projections and full inverse support still have to be constructed. These models do not exhaust arbitrary carriers. |
| [R-0003](results/fixed_carrier_conductor_criterion.md), promoted | Once a carrier is specified, use its full normalization/divisor/conductor criterion; a rational normal symbol is insufficient. |
| [R-0014](results/movement_two_six_rows.md), promoted, conditional | The (6,16) and other five rows guide a saturated/full generic binary-CI search only. They are not all possible STCI degree pairs. |
| [R-0035](results/normal_carrier_bounded_index_exclusion.md), promoted, conditional | Avoid normal carriers satisfying its bounded-index hypotheses. Higher actual indices and nonnormal carriers remain separate sources. |

The two searches with the most direct routes to equations are therefore:
mixed-weight global forms with deliberately correlated normal roots, and
actual normalization maps whose coordinate rings contain a pure power of
the marked inverse curve. Keep a broader all-pairs parameter space as the
exhaustion benchmark; neither source above is claimed exhaustive.

## 3. Characteristic p: the correct minimum-degree target

Define the geometric minimum over **all** presentations
\[
\delta(p)=\min\{\max(a,b):V(F_a,G_b)_{\mathrm{red}}=C_{
\overline{\mathbf F}_p}\}.
\]
Then
\[
C_{\overline{\mathbf Q}}\text{ is not STCI}
\quad\Longleftrightarrow\quad
\delta(p)\longrightarrow\infty\quad(p\text{ through primes}).
\tag{A}
\]
This is an independently checked exact reduction, not a lower-bound
theorem. At each fixed degree bound the actual solution locus is
constructible over the integers. Chevalley's theorem makes existence at
that bound either finite in p, or cofinite in p with a characteristic-zero
solution. Equivalently, a fixed bound working in infinitely many
characteristics already implies characteristic-zero existence. Allow
algebraic-closure points; failure over F_p itself does not prove emptiness.
The full finite-matrix and independent incidence proofs are in the
[search-logic audit](notes/2026-10-28-stci-search-logic-audit.md).

The reviewed fixed-quartic calculation already determines mate degrees on
\(S=x_0x_3^3-x_2^4\): a positive degree N works in characteristic p exactly
when \(p^{v_p(N)}\in\langle3,4\rangle\). Its minima are 4, 3, 25, p for
p=2, 3, 5, and p>=7, respectively. This is a fixed-carrier statement;
it does not bound delta(p) below across other carriers. The
[arithmetic source note](notes/2026-10-28-stci-search-arithmetic.md)
preserves the inherited evidence, alternative constructions, the scoped
one-binomial lower bound, and the precise remaining all-pairs implication.

There is a useful extension beyond that fixed quartic: for any presentation
with at least one binomial equation and an arbitrary homogeneous mate,
\(p\mid ab/4\). Hence max(a,b)>=p. For p>=7 the known (4,p) pair attains
this, so the one-binomial geometric minimum is exactly p. The
[arithmetic audit](notes/2026-10-28-stci-search-arithmetic-audit.md)
independently checks the carrier reduction and finite-cover argument.
This covers every binomial carrier, but leaves the two-non-binomial class.
The exact restricted minima at p=2,3,5 are 4,4,20. In particular the
audited characteristic-five (3,20) pair improves on the fixed quartic's
minimum mate degree 25, illustrating why carrier-specific optimality
cannot be substituted for the all-pairs minimum.

The practical arithmetic task is to find a mechanism forcing growing
degrees for pairs with **two non-binomial equations**, or a valid reduction
of all pairs to a controlled source. Degenerating equations to binomials
without preserving properness does not supply that reduction. On the
positive side, fixed-degree geometric solutions across many primes are
candidates for reconstruction over number fields; numerical samples alone
do not establish the infinitely-many-primes hypothesis in (A).

## 4. Freedom versus constraints gives exact source filters

Write Q=x_0x_3-x_1x_2 and
\(A_m(d)=h^0(\mathbf P^3,\mathcal I_C^m(d))\), using sheaf powers,
equivalently saturated homogeneous powers. For
\(2m\le d\le3m\), put u=d-2m. Then
\[
A_m(d)=\begin{cases}
0,&d<2m,\\
\displaystyle(5u^3+15u^2+16u+6)/6,&2m\le d\le3m,\\
\displaystyle\binom{d+3}{3}-\frac{m(m+1)(4d+1)}2
+\frac{7m(m^2-1)}3,&d\ge3m.
\end{cases}\tag{B}
\]
The formulas agree at the overlap. Below degree 3m every such form has
the fixed factor Q^(3m-d). Consequently an integral equation of degree
at least five and exact order m requires d>=3m. This is stronger than a
count of coefficients. It follows from the quadric flag sequence
\[
0\to\mathcal I_C^{m-1}(d-2)\xrightarrow{Q}\mathcal I_C^m(d)
\to\mathcal O_Q(d-m,d-3m)\to0.
\]
The source proof and asymptotic calculation are in the
[freedom note](notes/2026-10-28-stci-search-freedom.md), with an
[independent proof audit](notes/2026-10-28-stci-search-freedom-independent-audit.md)
and [exact finite controls](computations/stci_search_freedom_2026_10_28.json).

In characteristic zero the order-r symbol map has codimension 6r-1 at
d=3r, codimension 2r+1 at d=3r+1, and is surjective at d>=3r+2.
For example:

| Degree, order | Global equation space | Actual symbol image | Abstract target |
| --- | ---: | ---: | ---: |
| (6,2) | 23 | 22 | 33 |
| (7,2) | 47 | 40 | 45 |
| (8,2) | 80 | 57 | 57 |

If integral F_a,G_b have orders r,s and coprime leading binary normal
forms, their generic length is rs<=ab/9. The target is ab/4. Thus a
minimal integral witness must have shared leading roots and higher
contact. Search that correlated locus; generic independent leading forms
cannot work. This necessity permits excess contact and makes no universal
upper bound on it.
Here r,s are the normal orders of the two actual global equations.
They are not the orders of new relations obtained after subtracting
formal or rational multiples of F. In particular the order twelve in
the conditional (6,16) standard-basis test below does not assert that a
degree-sixteen global form itself lies in I_C^12.

For m/d tending to theta<=1/3, the fraction of all degree-d forms that
remain tends to 1-12theta^2+14theta^3, still 5/27 at theta=1/3. There is
substantial freedom, but it is individual-equation freedom. The missing
conditions correlate the two equations through higher contact and global
support; their independence is not established by this dimension formula.

## 5. Completed attempts and the resulting changes to the search

### Actual degree-eight projections

On P1 x P1 use Segre coordinates (a,b,c,d) with ad=bc, Delta=b-c,
and the diagonal Delta=0 as the marked curve. The tested pencil is
\[
U=(a^2+\Delta^2,\ ab,\ dc,\ d^2+\lambda\Delta^2).
\]
It has the correct restriction to C, but fails for every lambda in
characteristic zero. On the affine chart (u_0,v_0)=(1,1), at v_1=0,
u_1^2=-1, Delta is nonzero. For lambda nonzero these are isolated extra
inverse points over [0:0:0:1] in C; for lambda zero they are basepoints.
The [exact rejection](notes/2026-10-28-stci-search-quadric-test.md) and
the independent addendum to the [logic audit](notes/2026-10-28-stci-search-logic-audit.md)
check the literal family. It does not eliminate the full projection source.

**Update:** vary the middle coordinates as well. The complete marked source
is U_i=B_i+Delta A_i with sixteen scalar parameters, where
B=(a^2,ab,dc,d^2) and each A_i has bidegree (1,1). Screen basepoints
and isolated extra inverse support first. For an admissible finite
birational map with singleton lift, a mate G_b is equivalent to the
exact global membership
\[
\Delta^{2b}\in\operatorname{span}_k\{U^\alpha:|\alpha|=b\}.
\tag{C}
\]
A successful identity gives the actual equation G and handles descent.
For unknown parameters retain all rank strata; inversion of one convenient
minor can discard the candidates we seek.

The first correction was also tested: add Delta^2 and 2Delta^2 to the two
middle coordinates and take lambda=3 in the last coordinate. This actual
map is basepoint-free, but the off-diagonal inverse image of C is a
nonempty zero-dimensional scheme of length sixteen in the chart Delta=1
on the Segre quadric. The exact rational computation is in the same
[projection test note](notes/2026-10-28-stci-search-quadric-test.md).
Thus the elementary endpoint defect can be removed while isolated inverse
support still prevents a mate. **Second update:** solve the full inverse
support condition in parameter space; unrestricted middle-coordinate
perturbation by itself does not solve it.
In fact this particular finite image has no mate in any positive degree:
the pullback of a mate would be a Cartier divisor on the smooth quadric
and cannot have isolated zero points. This conclusion needs no unproved
birationality assertion. It remains a statement about this image alone.

### Actual sextics and all global degree-sixteen mates

The [experiment note](notes/2026-10-28-stci-search-experiments.md) records
new members of an actual sextic family, the complete 969-dimensional
degree-sixteen equation source, exact modular necessary-jet ranks, a
separate nodal audit, and the resulting contact bounds. The previously
accepted fixed carrier was not replayed. The
[saved output](computations/stci_search_sextic_jets_2026_10_28.json)
records each input and every tested cutoff.

Writing q=x_0x_3-x_1x_2 and D=x_2^3-x_1x_3^2, the tested family was
\[
F_{t,\kappa}=-q^2x_3^2-qDx_2-tqDx_3+D^2/4+\kappa q^3.
\]
All seven selected inputs fail against every proper degree-sixteen mate.
For (t,kappa)=(0,0),(1,0),(2,0), the computed bound is ell_C<=18,
so deg R>=24. For (1,1),(1,-1),(2,1),(0,-1), the exact maximum is
ell_C=16 and the sharp residual floor is 32. Every maximal-contact mate
at the latter four inputs defines the same full scheme (F,q^8), with
cycle
\[
16[C]+32[L_0],\qquad L_0=V(x_2,x_3).
\]
Thus these selected carriers' apparent perturbation freedom cannot
improve even the known quadric-power residual at maximal contact. The
[independent experiment audit](notes/2026-10-28-stci-search-experiments-audit.md)
uses separate Macaulay2 quotient coordinates at representative inputs.

The principle being tested is whether extra global equation freedom can
remove the residual of a known proper intersection while retaining the
carrier. Kernel equality with F times all degree-ten forms proves failure
for every mate at the specified degree on that carrier, rather than just
failure of one guessed G. The nodal nonsplitting argument is essential
when converting the jet cutoff to a bound on all mate contact lengths.

**Update:** investigate loci where the global jet rank drops. A smaller
rank is only a possible direction: reconstruct an actual G, remove common
factors and compute its full contact before calling it a candidate. Sampling
more generic coefficients after the kernel stabilizes supplies little new
information. No finite set of carriers exhausts all sextics or all degrees.
The zero-kappa boundary has a larger remaining cutoff-nine kernel and
changes the rank of an auxiliary quadric from five to three. It is a
specific place to investigate exceptional contact; its surviving kernel
has not been identified with actual normalization sections or a mate.

## 6. The next iteration

1. Use the exact freedom formula to build genuine global sources, eliminate
   forced quadric factors, and impose shared normal roots or extremal-weight
   constraints before expensive higher-jet calculations.
2. In the actual projection source, screen full inverse support and search
   the pure-power membership locus (C). In the sextic source, use the
   completed ranks to seek special contact loci rather than new generic
   samples. These are complementary constructive tests with explicit
   success certificates.
3. Extend the higher-jet arithmetic obstruction beyond its now-tested
   larger plane source. Keep the all-pairs delta(p) target visible; do not
   identify restricted-source optimality with this target.
   For a degree bound B, primes p>B automatically remove all one-binomial
   presentations from that bounded search; allow extension-field
   coefficient solutions in the remaining two-non-binomial locus.

The next deliverable should be an actual defining pair, an exact empty
specified parameter locus, or a smaller surviving locus with the first
unresolved equation identified. A new geometric invariant earns further
work here by helping produce or reject those equations.

## 7. First continuation and its remaining projection endpoint

The [October 29 continuation](notes/2026-10-29-search-continuation.md)
records three distinct outcomes, with proofs, exact computations and
independent audits:

- For \(F=q^3+\alpha c_0^2+\beta c_2^2\), \(\alpha\beta\ne0\), every
  member is integral and every proper actual sextic mate has
  \(\ell_C\le8\). The entire \((6,6)\) contact-nine incidence is empty;
  \(\deg R\ge4\). The calculation treats the split branches separately
  and retains every parameter. Higher mate degrees remain uncomputed.
- On a specified twenty-three-parameter plane source, every mate degree
  satisfies \(p\mid b\), by a higher-jet descent gap. An explicit
  non-binomial degree-sixteen carrier has non-binomial degree-\(p\)
  mates for every prime \(p\ge43\), with literal pullback \(z^{4p}\).
  The restricted-source minimum is exactly \(p\); this does not bound
  the all-pairs minimum below.
- For the complete marked smooth-quadric source, only determinant orders
  one and two can be basepoint free. Several complete parameter slices
  and residual-divisor strata are excluded. The remaining full-inverse
  incidence and descent on surviving admissible strata are **not**
  computed. The source notes specify those remaining equations.

These are reviewed provisional contributions, without canonical promotion.
They do not settle the unrestricted characteristic-zero question or the
other normalization models.

## 8. October 30: all-degree line obstructions and the adversarial update

The [four-line theorem](notes/2026-10-30-mixed-weight-line-obstruction.md)
now excludes **every positive mate degree** on the entire mixed-weight
seed \(q^3+\alpha c_0^2+\beta c_2^2\), \(\alpha\beta\ne0\). Its
independent audit reconstructs actual branch attachment and the
incompatible divisor-degree identities. This supersedes the earlier
research limitation that higher mate degrees on this seed were untested;
the earlier \((6,6)\) certificate remains a separately scoped control.

The [uniform subalgebra theorem](notes/2026-10-30-weighted-subalgebra-line-obstruction.md)
extends this to every actual
\[
F=\sum_{i=0}^{\lfloor m/2\rfloor}q^{3i}B_{m-2i}(c_0,c_2)
\]
with squarefree axis-free \(B_m\), for every \(m\ge1\) and every mate
degree, without assuming carrier irreducibility. The next construction
must enter its binary boundary or leave this subalgebra. Its relative
dimension in the full degree-\(3m\), order-\(m\) source tends to zero;
there is no exhaustion of arbitrary equations.

The [order-two projection survivor](notes/2026-10-30-projection-order-two-survivor.md)
is now a primitive smooth elliptic residual with precise degree-twenty
three-branch-value data. All singular/reducible/nonreduced boundaries
and the double-image case are excluded. The
[support and global extension theorem](notes/2026-10-30-projection-elliptic-target-incidence.md)
excludes the zero-middle-coefficient support quartic for every contact
distribution. An explicit elliptic target incidence survives the target
tests but fails this source-extension test. The general primitive
elliptic and order-one loci, followed by descent on actual surviving
strata, remain uncomputed.

These results and their next challenges are tracked in
[STCI_GAME.md](STCI_GAME.md). In particular the obstruction side must
continue to enlarge coverage and extract reusable mechanisms, rather
than wait for the next construction to refute. The current
[quadric-boundary investigation](notes/2026-10-30-stci-game-quadric-boundary.md)
tests why large global higher-order lifting freedom can preserve a fixed
residual, and identifies a global row-operation restriction to compare
with formal cancellation.
