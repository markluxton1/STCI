# Session normal-carrier progress: exceptional passage and reduced cycles

Started 2026-10-06; persisted and extended 2026-10-07 after interruption.
Scope: characteristic zero, the fixed smooth monomial rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, an integral **normal quartic carrier**, and an
arbitrary ambient mate. This is a new session note, not a replacement for
the canonical audited state. On 2026-10-07 `frontier_audit` independently
accepted sections 2--6, including a separately rebuilt exact enumeration;
the root also audited the passage, Cauchy and local `A2` arguments. The
nonreduced tree enumeration in section 9 was then independently rebuilt
and accepted; the root separately checked the cohomology/tree proof and
the Type-D passage argument against the primary source. Verification
also reran the stabilized sources live with matching output hashes.
The complete normal-quartic exclusion below is accepted under the
explicitly recorded classification, compression, ADE-classification and
normal-sheaf inputs.

## Checkpoint and claimed progress

1. **PROVED / independently audited:** a smooth embedded curve
   passes through an isolated surface singularity by meeting exactly one
   exceptional prime transversely at a smooth point of the reduced
   exceptional divisor on its resolution.
2. **PROVED / independently audited:** the anticanonical
   intersection and numerical correction satisfy `t+q=6`; Cauchy's
   inequality and denominator compression leave `t=1` for `d=1`, and
   `t in {1,2}` for `d=2,3`.
3. **PROVED / independently audited:** every irreducible
   anticanonical exceptional divisor is excluded, including a singular
   irreducible genus-one divisor.
4. **PROVED through an independently audited exact reduction:** for reduced reducible
   anticanonical divisors, an exhaustive cycle/ADE numerical scan leaves
   five configurations. Four compress to a forbidden quadric mate. The
   fifth has compressed mate degree six and is then excluded by the
   independently proved normal-sheaf defect formula, using its six `A1`
   points and one `A2` point.
5. **PROVED / independently audited:** the nonreduced divisor has a rational
   SNC tree support; the complete bounded graph enumeration leaves only
   Type-D coefficient-two passages, which the Type-D coordinate basis
   excludes. Thus every normal quartic carrier is excluded.
6. **OPEN:** nonnormal quartic carriers, higher-degree minimum carriers,
   and the entirely-thick branch. No conclusion that `C0` is not STCI is
   asserted.

The normal quartic lane for `C0` is now closed, whatever the mate degree.

## 1. Inputs reconstructed and checked

The controlling state is `research/AUDITED_STATE_2026-10-06.md`. Its normal
lane already excludes rational-singularity quartics, positive-genus ruled
quartics, avoidance of the nonrational locus, and smooth simple-elliptic
exceptional divisors. The remaining rational-resolution types of
Ishii--Nakayama have

| `d=-E^2` | types | `rho(M)` |
|---:|---|---:|
| 1 | B2/B3 | 11 |
| 2 | B1 | 12 |
| 3 | D | 13 |

Here `sigma:M -> S` is the **minimal** smooth resolution, `H` is the
hyperplane pullback, and `K_M=-E` with integral effective exceptional `E`.
The minimality, effective discrepancy divisor, Picard numbers and
exhaustiveness are explicit in [Ishii--Nakayama's author
preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1370.pdf),
pp.7, 14, 17, 19 and 23, and in the
[published paper](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf).
The saved convenience extraction `/private/tmp/stci-normalquartic-rims1370.txt`
was inspected in this session. The classification is geometric, not an
inference from an ADE table or examples.

The proof of `2026-10-06-normal-rational-carrier-compression.md` was
rechecked: a mate gives `c+Z == H`; clearing the denominators produces an
integral numerically trivial divisor on the rational surface `M`, hence a
principal divisor. Pushforward and ambient section lifting produce a
mate of exactly the numerical denominator `n`. Every actual mate degree
is divisible by `n`. The argument requires normality, a rational **whole
resolution**, and existence of a mate. In particular one cannot use
numerical coincidence on an arbitrary nonrational resolution to discard
local Picard torsion.

The determinant proof also remains applicable: all exceptional classes
have rank at most `9+d`, and minimality gives
`sum (b_i-2)_+ <= d` for `b_i=-E_i^2`. Thus its bounds 1536, 4608, 13824
are valid even for nonreduced or singular `E`.

The normal-sheaf inequality in `2026-10-05-mumford-normal-bound.md` was
read through its ideal-principalization proof. For a generically regular
carrier it supplies the exact nonnegative defect

`deg N_(C/S) - (C#)^2 = (Z_ideal-Z_num).c >= 0`.

It applies here since a normal surface is regular at the generic point
of the curve. Contributions over different singular points are additive.
The global first-normal symbol of a quartic is a nonzero pair of binary
forms of degree nine, so its total common order is `9-e <= 9` and
`deg N_(C/S)=7-e`. These identities use the audited balanced normal bundle
`N_C=O(7)^2` of the fixed `C0`. We retain the audited stronger `e<=2`,
although only `e>=0` is needed in the new exclusions.

## 2. Smooth passage lemma, including singular primes and crossings

Let `p` be an isolated singular point of an integral normal surface
`S` containing a smooth curve `C`, and let `sigma:M -> S` be any smooth
proper resolution. Its strict transform `c` maps isomorphically to `C`:
the rational lift from the smooth proper curve extends by the valuative
criterion, giving a section and hence a closed immersion.

At its point `x` over `p`, let `E_i` run through the exceptional prime
curves. For every local function `f in m_(S,p)`, its pullback vanishes on
every exceptional prime above `p` with integer order at least one. Since
`M` is smooth, each prime divisor is locally principal, and the product
of their distinct local equations divides `sigma^*f`. This remains true
when an exceptional prime is singular or several exceptional primes
cross: smoothness of `M`, not smoothness of these divisors, supplies the
local divisor factorization. Restriction to `c` gives

`ord_x(f|c) >= sum_(E_i over p) (c.E_i)_x`.

The maximal ideal of `S` maps onto the maximal ideal of `C`; some `f`
therefore restricts to a uniformizer of the smooth curve, of order one.
The strict transform must meet the exceptional fiber. Thus

`sum_(E_i over p) c.E_i = 1`.

Every nonzero term is a positive integral scheme intersection length.
Consequently `c` meets exactly one exceptional prime, with intersection
length one. That point is smooth on the prime and outside all other
exceptional primes; otherwise the relevant local intersection length or
the sum would be at least two. The intersection is transverse. In the
matrix notation, the passage vector at each singular point is a single
standard basis vector, not an arbitrary nonnegative vector.

For the rational normal quartics at hand, `E` is connected: Proposition
1.1 of Ishii--Nakayama gives `h^0(E,O_E)=1`. An exceptional prime with
coefficient zero in `E` is disjoint from its support, as follows from
minimality and adjunction in the preceding compression note. Connected
exceptional fibers therefore show that the support of `E` is the entire
fiber of the unique nonrational singular point. All other singular fibers
are ADE. The already proved avoidance exclusion forces `C` through this
nonrational point. Its anticanonical passage `t=c.E` is thus precisely the
coefficient of the exceptional prime selected by the passage lemma.

## 3. A small anticanonical passage bound

Write all exceptional primes as `E_i`, put `A_ij=-E_i.E_j`,
`E=sum a_i E_i`, `m_i=c.E_i`, and `Z=sum z_i E_i` with
`z=A^(-1)m`. Set

`t=a^T m=c.E > 0`, `q=m^T A^(-1)m=-Z^2`, `d=a^T A a=-E^2`.

Adjunction on the smooth rational strict transform gives `c^2=t-2`.
The mate relation gives `c+Z == H`, whose square is four. Orthogonality
to exceptionals gives `(c+Z)^2=c^2+q`, so

`t+q=6`.

Cauchy--Schwarz in the positive definite form `A` gives

`t^2 <= d q = d(6-t)`.

Hence the positive integer possibilities are `t<=2` for `d=1,2`, and
`t<=3` for `d=3`. Equality occurs at `(d,t)=(1,2)` or `(3,3)` and forces
`z=(t/d)a`, respectively `2a` or `a`. In both cases `Z` is integral and
the numerical denominator is one. Compression would produce a plane
mate, impossible for a nondegenerate degree-four curve. Thus

| `d` | remaining `t` |
|---:|---|
| 1 | 1 |
| 2 | 1 or 2 |
| 3 | 1 or 2 |

In particular a nonreduced surviving exceptional divisor must have a
prime with coefficient one or two available to the smooth passage; for
`d=1` the selected prime has coefficient one.

## 4. Irreducible anticanonical divisors are excluded

If `E=aP` is irreducible as a support, then `d=a^2(-P^2)<=3` forces
`a=1`. Thus every irreducible `E` here is reduced. Its arithmetic genus
is one by adjunction. The passage lemma gives `c.E=1`, including when
`E` is a nodal or cuspidal rational curve: a smooth embedded `C` cannot
meet its singular point on `M`.

Orthogonality gives local correction `Z_irr=E/d`, with contribution
`q_irr=1/d`. The whole correction is `q=5`, so the ADE points on `C`
would have to contribute `5-1/d`. Their total root rank is at most
`N=8+d`, because `H`, the irreducible `E`, and the ADE roots are independent.

Every **nonrational isolated hypersurface** singular point on a smooth
curve has first-normal common order at least two. To verify this without
a local irrational-singularity classification, straighten the smooth
support to the `x` axis. Order one would give a quadratic term
`x(ay+bz)+Q(y,z)` with `(a,b)!=(0,0)`. Its quadratic rank is at least two.
The characteristic-zero analytic/formal splitting lemma then writes
the isolated hypersurface germ as `uv+h(w)`, or as a nondegenerate
quadratic germ. Isolation makes `h` a nonzero one-variable power series;
the result is an `A_n` rational double point. This contradicts
nonrationality. The argument transfers from complex coefficients in the
same way as the classification inputs in the earlier note.

At most seven of the nine first-normal zeros remain for ADE points.
Jaffe's smooth curve--ADE classification, recorded and checked in
`2026-10-05-normal-quartic-carriers.md`, gives the harmonic inequality

`q_ADE <= N P/(N+P)` with `P=sum s_i <=7`.

It now contradicts the required correction in every row:

| `d` | required `q_ADE` | harmonic maximum | positive gap |
|---:|---:|---:|---:|
| 1 | 4 | `63/16` | `1/16` |
| 2 | `9/2` | `70/17` | `13/34` |
| 3 | `14/3` | `77/18` | `7/18` |

This excludes all irreducible exceptional anticanonical divisors, without
assuming smooth ellipticity or any upper bound on the mate degree.

## 5. Reduced reducible divisors: exact cycle reduction

Suppose `E` is reduced and reducible, with `k` primes. Connectedness was
proved above. Adjunction on each prime gives

`sum_(j!=i) E_i.E_j = 2-2p_a(E_i)`.

A prime of arithmetic genus one would have no neighbors and contradict
connectedness. Every prime therefore has arithmetic genus zero and is a
smooth rational curve, with total intersection two with the others.
The connected weighted multigraph is a cycle. For `k=2` the two primes
have intersection two; for `k>=3` its edges have intersection one. It
may have coincident intersection points or tangent intersection schemes;
the matrix reduction does not assume simple normal crossings. The smooth
passage avoids all such points by section 2.

Minimality gives `b_i=-E_i^2>=2`. Since the coefficient vector is all
ones,

`sum_i (b_i-2)=d`, `2<=k<=9+d`.

These are a genuinely finite set of cycle matrices: choose a weak
composition of `d` into `k` entries and set the diagonals to two plus
those entries. The matrix for the two-prime cycle has off-diagonal `-2`;
larger cycles have adjacent off-diagonal `-1`. Its negative definiteness
is equivalently the positive definiteness of this matrix; all the listed
matrices are positive definite because at least one diagonal exceeds two.

The passage lemma makes `m_irr` a unit vector. Thus each numerical
candidate is determined by the selected diagonal entry
`q_irr=(A^(-1))_(jj)` and the common denominator of column `j`.
The ADE points must satisfy

`N_ADE<=9+d-k`, `P_ADE<=7`, `q_ADE=5-q_irr`.

The exact companion enumerates every allowed ADE pair row, every multiset
of them under these rank and order budgets, and every cycle column. It
uses the entire correction-column denominator, not merely the denominator
of its square. Rotations/reflections and identical `(d,k,q,index)` data
are deduplicated, which does not affect existence in these numerical tests.

Exactly five configurations remain after the correction equality:

| `d` | cycle weights | selected prime | `q_irr` | ADE pairs | compressed degree |
|---:|---|---|---:|---|---:|
| 1 | `(-2,-3)` | `-2` | `3/2` | seven `A1` | 2 |
| 1 | `(-2,-3)` | `-2` | `3/2` | five `A1`, one `A3^2` | 2 |
| 1 | `(-3,-2,-2,-2)` | opposite `-3` | 2 | six `A1` | 2 |
| 2 | `(-4,-2,-2,-2)` | opposite `-4` | `3/2` | seven `A1` | 2 |
| 3 | `(-5,-2,-2,-2)` | opposite `-5` | `4/3` | six `A1`, one `A2^1` | 6 |

The four denominator-two rows are impossible: the conditional
compression theorem produces a quadric mate. For `C0` the unique-quadric
obstruction rules it out. This is an actual compressed mate conclusion
under the hypothetical original mate, not a cancellation of a local
torsion scalar without its global hypothesis.

## 6. The degree-six numerical survivor is excluded by normal-sheaf defect

The final row uses all seven allowed ADE first-normal orders. The
nonrational point uses at least two. Hence the whole first-normal common
order is exactly nine and `e=0`. The available global normal-sheaf defect
is therefore

`deg N_(C/S)-(C#)^2 = 7-4=3`.

Each of the six `A1` passages contributes `1/2` to this nonnegative
defect, by the exact local model already proved in
`2026-10-05-mumford-normal-bound.md`. The `A2^1` passage contributes
`1/3`. To check the latter directly, use

`S: xy=z^3`, `C: x=z=0`.

The ordinary point blowup resolves this `A2` surface with two `(-2)`
curves. On the `y` chart, put `y=t,z=tu,x=t^2u^3`; the strict support is
`u=0`, and its ideal is `(x,z)=(tu)`. On the `x` chart the ideal is
generated by `x`. On the `z` chart put `x=zX,y=zY`, so `z=XY` and
`(x,z)=(XY)`. The ideal exceptional coefficient is one on each of the
two exceptional curves. The numerical coefficient at the prime met by
the support is `2/3`, from the inverse of `[[2,-1],[-1,2]]`. The defect
is thus `1-2/3=1/3`.

The `A2^1` smooth pair is the unique `A2` passage from Jaffe's
classification (the two symmetric ends are equivalent), so this model
applies to the surviving row. Contributions over all other points are
nonnegative by the proved ideal-principalization comparison. Therefore

`3 >= 6*(1/2)+1/3=10/3`,

a contradiction. Equivalently the surviving nonrational passage would
need too little ideal correction for its numerical correction `4/3`.
This eliminates the final reduced-cycle numerical configuration.

## 7. First checkpoint boundary and evidence (superseded by sections 8--11)

The independently audited new conclusion is: **a normal quartic carrier for
`C0` in characteristic zero, if it has any mate, must have a reducible
nonreduced exceptional anticanonical divisor.** Its smooth nonrational
passage selects a coefficient-one prime for `d=1`, or a coefficient-one
or coefficient-two prime for `d=2,3`. The exact identities `t+q=6` and
the existing denominator bounds remain necessary.

At this first checkpoint it was not a normal-quartic global exclusion:
the nonreduced case was retained. The next step was a classification or an exact graph audit
of the nonreduced anticanonical cycles under `a^T A a=d<=3`, relative
nefness, rank at most `9+d`, and the selected coefficient at most two.
One must preserve the local smooth-passage condition and the full
correction denominators, and must not identify these configurations with
reduced cusp cycles.

Exact companion and saved output:

- `research/computations/verify_session_normal_carrier_progress.py`;
- `research/computations/session_normal_carrier_progress_2026-10-07.json`.

The companion checks the rational gaps, passage-bound arithmetic, exact
cycle enumeration, all ADE correction/index data used in the scan, the
five remaining numerical rows, and the final defect contradiction.
Its output checks numerical implications, not existence of the surfaces,
the source classification, or the geometric passage lemma. Those are
separate proof obligations explicitly supplied above.

## 8. New checkpoint: the nonreduced support is a rational SNC tree

Status: proof supplied and independently accepted by the root on 2026-10-07.
This supplies the smaller exact graph problem for the nonreduced lane;
its complete enumeration is recorded in section 9.

On the smooth projective rational surface `M`, both `H^1(O_M)` and
`H^2(O_M)` vanish. For any nonzero **proper** effective subdivisor
`0<D<E`, the sequence

`0 -> O_M(-D) -> O_M -> O_D -> 0`

and Serre duality give

`H^1(O_D) = H^2(O_M(-D)) = H^0(O_M(K_M+D))^*`

`=H^0(O_M(D-E))^*=0`.

The last vanishing follows because `E-D` is a nonzero effective divisor:
a global section of its negative ideal would be a global regular
function on the proper connected surface vanishing there, hence zero.
This is an actual cohomology statement, not an inference from arithmetic
genus alone.

Every prime of the now retained reducible `E` is a proper subdivisor, so
it has arithmetic genus zero and is a smooth rational curve. If `E` is
nonreduced, its reduced support `R=E_red` is also a proper subdivisor.
It is connected, has `h^0(O_R)=1`, and the above argument gives
`h^1(O_R)=0`; therefore `p_a(R)=0`. Adjunction, adding the individual
prime adjunction formulas, gives

`sum_(i<j) E_i.E_j = k-1`.

Connectedness forces at least `k-1` graph edges, each carrying a positive
integer intersection length. Equality forces a tree with simple edges of
intersection length one. There are no tangent intersections, and no
three primes can pass through the same point, since that would produce
a cycle of three pairwise edges. Consequently the support is a simple
normal crossing tree of smooth rational curves.

The residual matrix equations are thus exactly

`A_ii=b_i>=2`, `A_ij=-1` on tree edges and zero elsewhere,

`A a = b-2`, `a_i in Z_(>0)`, `a^T A a = sum a_i(b_i-2)=d`,

`1<=d<=3`, `2<=k<=9+d`, `some a_i>1`.

Positive definiteness remains mandatory. At the nonrational point the
selected smooth-passage prime has `a_j=1` if `d=1`, or `a_j in {1,2}`
if `d=2,3`; its correction is the selected diagonal of `A^(-1)` and its
full numerical denominator is that inverse column's denominator.
Every other point on `C` is ADE with the same rank and first-normal
budgets as above, but now the required correction is

`q_ADE = 6-a_j-(A^(-1))_(jj)`.

Since `a_i>=1`, the diagonal excess satisfies
`sum(b_i-2)<=d<=3`, so these are a finite set of nonisomorphic trees of
at most twelve vertices with at most three total units of diagonal
excess. This finite numerical graph problem is a **necessary** condition
for the classified surfaces. Passing it will not establish realizability
or a smooth local passage, and failing it would supply an exclusion only
after all its equations and admissible rows are independently audited.

The root supplied a further coefficient-one simplification. At a prime
with `a_i=1`, the equation `Aa=b-2` says that the sum of neighboring
coefficients is two. It is therefore either a leaf attached to a
coefficient-two prime or a valency-two vertex with two coefficient-one
neighbors. The latter situation propagates along coefficient-one
vertices and cannot reach a larger coefficient without encountering a
coefficient-one leaf; connectedness of a finite tree with some coefficient
greater than one forces the first case. Thus every coefficient-one prime
of this nonreduced tree is a leaf attached to a coefficient-two prime.

## 9. Exact nonreduced tree enumeration

Status: exact source completed and `PASS` in the live checkout on
2026-10-07; `frontier_audit` independently rebuilt the graph enumeration
and obtained the same 381802 trials, 195 cycles and twelve post-compression
rows. Sections 8 and 10 have separate root proof audits. Verification
independently reran the stabilized source in 22.899 seconds with a saved
JSON hash matching this checkout's output.

The source `verify_session_normal_nonreduced_trees.py` enumerates every
unweighted nonisomorphic tree of sizes two through twelve by adding a
leaf at every vertex of every tree at the previous size, then comparing
exact rooted tuple codes over all possible roots. Induction is exhaustive
because every tree has a leaf. The counts by size are

`1,1,2,3,6,11,23,47,106,235,551`.

For each tree it enumerates every nonnegative excess vector `v=b-2` of
total one, two or three. There is no missing zero-excess case: positive
definite `A` and `Aa=0` would imply `a=0`, contrary to effective nonzero
`E`. Every necessary positive excess vector has sum at most three, by
section 8. Leaf Schur elimination checks positive definiteness with exact
fractions and solves `Aa=v`; every resulting solution is independently
substituted into the full original equations. The filter retains exactly
positive integral coefficients and `d=a.v in {1,2,3}`, with `k<=9+d`.
Weighted tree isomorphisms are then deduplicated by exact tuple codes.

The 381802 diagonal modifications leave 195 numerical canonical cycles:
nine for `d=1`, 59 for `d=2`, and 127 for `d=3`. These are a finite
**superset** of the classified geometric configurations. No analytic
realizability or proper-subcycle cohomology conditions are imposed, so
discarding all of them is legitimate; retaining one would not establish
existence on a quartic.

At every possible selected coefficient one or two allowed by section 3,
the source solves the unit-column correction exactly, takes the least
common denominator of **every** entry in that column, and compares
`6-t-q_irr` with every ADE multiset under the rank and order budgets.
There are 236 exact correction matches. The known compressed mate-degree
exclusions up through degree five eliminate 224. Twelve rows remain:

| nonrational rank | `q_irr` | `t` | number of rows | ADE data |
|---:|---:|---:|---:|---|
| 5 | 2 | 2 | 5 | correction 2, rank 4--7, order 3 or 4 |
| 7 | 2 | 2 | 2 | correction 2, rank 4 or 5, order 4 |
| 8 | 2 | 2 | 1 | four `A1` points |
| 8 | `17/6` | 2 | 4 | one `A1` and one `A2^1` |

**Every remaining row has `d=3` and `t=2`.** Their compressed degrees are
six or twelve. The saved JSON includes the full 195 graph/diagonal/
coefficient data and each surviving full correction column, so this
assertion can be reconstructed rather than inferred from a total count.

Exact source:
`research/computations/verify_session_normal_nonreduced_trees.py`.
Saved output:
`research/computations/session_normal_nonreduced_trees_2026-10-07.json`.
The source emits JSON on stdout and makes no internal file writes. Its
only dependency is the earlier reduced-cycle companion, whose exact
ADE root matrices and multiset states are revalidated through `runpy`.

## 10. Type D has anticanonical passage one on every smooth embedded curve

Status: source and geometric proof independently accepted by the root on
2026-10-07. This proof does not depend on the tree enumeration or a mate.

Ishii--Nakayama §2.4, author preprint p.23 (published p.955), supplies the
following exact description for **all** Type-D surfaces, by the exhaustive
Main Theorem. There is a separation `rho:M -> P^2` of a smooth plane
quartic `B` and an effective cubic divisor `G`. It satisfies

`K_M+H ~ rho^*(K_(P^2)+B) ~ rho^*O_(P^2)(1)`.

Thus `H-E ~ rho^*O_(P^2)(1)`. More precisely, the four basis sections
of `H` are

`xi0=phi4`, `xi1=phi3 rho^*x`, `xi2=phi3 rho^*y`,
`xi3=phi3 rho^*z`,

where `phi3` cuts out the **entire** exceptional divisor `E`, including
its multiplicities, and `phi4` cuts out the pulled-back smooth hyperplane
section `D`, which is disjoint from `E`. The three pulled-back coordinate
sections have no common zero on `M`. The image of `E` is
`p=(1:0:0:0)`, and projection from `p` is the map induced by `rho`.
The explicit basis and the image assertion are in the source; they are
not reconstructed from a generic cubic example.

Near the exceptional fiber `E`, `xi0` is a unit in a local trivialization.
The three affine ambient coordinates `xi1/xi0`, `xi2/xi0`, `xi3/xi0`
generate the maximal ideal of `p` on `S`. Their pullback ideal is exactly
`O_M(-E)`: each has the factor `phi3`, and the three remaining coordinate
sections are basepoint-free. On any smooth curve `C` through `p`, the
maximal ideal of `S` maps onto the maximal ideal of `C`, whose order is
one. Restricting the pulled-back ideal to its isomorphic strict transform
therefore gives

`c.E = 1`.

This holds even when `E` is nonreduced. It forbids the selected
coefficient-two passage in every row remaining in section 9. In
particular the elimination is geometric, rather than a prediction of an
unverified lower bound for the local Jacobian common order.

## 11. Complete normal-quartic exclusion and its boundary

Sections 1--10 and their independent audits establish:

> For `C0=[s^4:s^3t:st^3:t^4]` in characteristic zero, no integral normal
> quartic surface can be a carrier in a set-theoretic complete
> intersection presentation, whatever the mate degree or common singular
> points.

The older rational-singularity, ruled-resolution and avoidance exclusions
dispose of the earlier classes. The reduced-`E` case is independently
accepted in sections 2--6. Rational-surface cohomology reduces nonreduced
`E` to the finite tree problem; the exact numerical scan leaves only
Type-D coefficient-two passages, which section 10 excludes.

The primary classification and analytic ADE inputs are stated over the
complex numbers. The theorem applies over **every algebraically closed
characteristic-zero field** as follows. A hypothetical finite-degree
pair has finitely many coefficients. Radical equality with the homogeneous
prime ideal of the fixed `C0` has finite witnesses: both carrier equations
belong to that prime, and a positive power of each of its finitely many
generators belongs to the two-equation ideal. Descend those coefficients
and witnesses to a finitely generated subfield `k0` of characteristic zero.
Its algebraic closure can be taken inside the original algebraically
closed field. Faithfully flat descent from the original field shows that
the carrier over that algebraic closure is integral and normal; thus the
model over `k0` is geometrically integral and geometrically normal. These
properties persist after field extension. Embed `k0`, and then its
algebraic closure, in the complex numbers. The finite polynomial witnesses
still express the same radical equality after this extension, and `C0`
remains its fixed smooth nondegenerate quartic. The resulting complex
hypothetical pair contradicts the complex proof above. This transfer
uses neither uncountability of the original field nor specialization of
singularity types at an uncontrolled parameter value.

Independent audit:
`research/notes/2026-10-07-session-normal-carrier-independent-audit.md`,
and `research/notes/2026-10-07-session-normal-nonreduced-independent-audit.md`,
with separately built reduced-cycle and nonreduced-tree numerical data.
The certificate sources stabilized at SHA-256
`57c73e7fc597d892dde3628dc0a7c0da2e6e61514af7890118e057f29b5cef13`
(reduced-cycle companion) and
`fca8eb7c177d88d00adcf5c60f664f8bbf9926abaf586762f22bfedf4199a2a7`
(nonreduced-tree companion). Numerical verification and geometric proof
audits remain distinct; the Type-D coordinate factorization is a primary-
source geometric input, not an output discovered by the enumeration.

The result is explicitly about **normal quartic carriers for the fixed
curve `C0`**. It does not exclude nonnormal quartic carriers, pairs whose
minimum carrier degree exceeds four, or the entirely-thick branch, and
does not prove `C0` is not STCI. The universal integral-curve problem
therefore remains open in this repository.
