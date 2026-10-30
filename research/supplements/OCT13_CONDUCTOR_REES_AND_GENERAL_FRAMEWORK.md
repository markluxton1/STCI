# Historical mathematical investigations

Complete source text preserved below, including explicit hypotheses, calculations, counterexamples and unresolved issues. Compilation is not independent correctness audit or theorem promotion.

---

## Source: 2026-10-13-evening-branch-frontier-audit.md

# All-branch frontier and provenance inventory — 2026-10-13 evening

**Scope:** repository coverage and routing, with accepted mathematics taken as correct. No inherited verifier or proof was rerun. This note records the branches actually observed locally and through the connected GitHub reader. **Historical snapshot:** branch inventories and statuses here are dated October 13, not current branch or theorem status. The present [authority policy](../AUTHORITY.md) and [canonical results](../results/INDEX.md) control. Preserve the historical manifest as evidence. It does not change checkout, branches, remote refs, canonical files, or the status of any mathematical claim.

## 1. Observed checkout and complete ref coverage

At the first inspection, the working tree was clean. Current checkout:

- branch `research/ultra-resume-2026-10-06`;
- HEAD `b16e4322c7b955147ce2ed241a1a0316a8e1a67a`;
- commit title `2026-10-13 morning limit reached`;
- one local worktree, no tags, and no stashes.

The initial clean observation predates other agents' evening writes. It is not a claim that the subsequent shared working tree is clean.

| Local or cached ref | Exact SHA | Coverage / relationship to current HEAD |
|---|---|---|
| local `research/ultra-resume-2026-10-06`, cached `origin/research/ultra-resume-2026-10-06` | b16e4322c7b955147ce2ed241a1a0316a8e1a67a | Current checkout; live remote agrees. |
| local `main`, cached `origin/main`, cached symbolic `origin/HEAD` | 98d71ddf8f8cceaad01bec43e94298699dcb5560 | Ancestor, current checkout has 30 later commits. Cached main is stale relative to live remote main. |
| local `archive/codex-5hr-interrupted`, local `ultra_mode`, cached `origin/ultra_mode` | 2e53a7b5e9d4c96b5741ee4a4746a4a9ff0ad647 | Historical interrupted branch; current HEAD has 62 unique commits, this branch has 1. Live ultra_mode agrees. |
| cached `origin/research/consolidate-2026-10-06` | 3f7b7fec652a0175ef7a7c5353f198f03649281a | Historical consolidation; 31 current-only / 55 cached-branch-only commits. No added path absent from HEAD. This branch name is absent from live enumeration. |
| cached `origin/research/local-audit-e2` | a0a5a67e2d5b01c83832041b578efe9d478f5c8c | Historical local audit; 31 current-only / 18 cached-branch-only commits. Only path absent from HEAD is `research/computations/branch_dx1_p044.out`. This branch name is absent from live enumeration. |

Two `refs/codex/turn-diffs/...` application snapshot refs also exist, at
`4f4cd1a7ce8836cdb51871ac01d2914b2fe95a05` and
`4190b258bac07e2d248a880a3102a457d59ff808`.
They are application captures, not research branches. They are recorded in the local inventory without promoting their contents to mathematical evidence.

Live GitHub enumeration returned exactly these seven branches:

| Live GitHub branch | Exact head SHA | Unique head commits / current commits from common base |
|---|---|---:|
| main | 7662a2ebb1dd561c1fb5e3c8958799b37d962c41 | 51 / 30 |
| research/e1-jet-rebuild-2026-10-07 | d5bed93e8c1ea09c2e11f0e096085da641819080 | 68 / 30 |
| research/entirely-thick-rees-valuation | a843888ce15b06247c576f8f717bec6b7ef5a352 | 70 / 30 |
| research/jet-discrepancy-order-one-2026-10-06 | f512d4d28da1fd6700aa4e6d2396229712d133d0 | 8 / 30 |
| research/normal-rational-carrier-classification | 4b936074f68038cfaa7ec51f5a960f23289627cd | 65 / 30 |
| research/ultra-resume-2026-10-06 | b16e4322c7b955147ce2ed241a1a0316a8e1a67a | same |
| ultra_mode | 2e53a7b5e9d4c96b5741ee4a4746a4a9ff0ad647 | local graph inspected |

All five divergent live branches above have common base
`98d71ddf8f8cceaad01bec43e94298699dcb5560`.
GitHub compare lists the changes from the merge base to the requested head,
not a direct tree diff against current HEAD. Missing local paths and overlap
were assessed separately, so a three-dot “added” path does not automatically
mean missing mathematics.

Network shell `git ls-remote` failed with DNS resolution failure; the connected
GitHub reader provided a successful live branch inventory. No Git fetch or
merge was performed.

## 2. Authority conflict and mathematical frontier

The current checkout README, `AUDITED_STATE_2026-10-07.md`,
`SUCCESSOR_HANDOFF_2026-10-07.md`, and newest acceptance records are the
continuation authority for this research line. They accept the all-quartic
carrier theorem for fixed C0 in characteristic zero, so every actual
quartic mate lane is closed and any hypothetical pair has both degrees
at least five.

Live remote main has a separate `research/STATE.md` and
`research/FRONTIER.md` described as canonical there. Their content is
mathematically older: they still list the MF6 (4,5) and normal quartic
remainder as open. Their generic “durable authority” wording must not
supersede the later acceptance record in this checkout. Wholesale merging
main would mix the two authority schemes and reopen already closed lanes.

The latest inherited quintic record accepts the coprime homogeneous
conormal exclusion, the G=Jbar=0 exclusion, the 2+4 residual exclusion,
and the complete actual conductor octic. At inherited HEAD, 3+3 has a frozen
all-mate proof under review, and the integral residual remains open.
This note leaves the evening team's subsequent reconciliations to its new
acceptance record.

Other live obligations survive separately:

1. normal quintics and other quintic normalization genera;
2. higher minimum carrier degrees and no general upper degree bound;
3. entirely thick pairs with both generic normal orders at least two;
4. the degree-six totally ramified split [2,2] carrier, whose mate scale is 8k;
5. common-quartic-ancestor incidence, including 22 family-two exceptional
   geometric points with their complete lower lift fibers, remaining
   nonendpoint top zeros, and the recorded positive-D2 directions;
6. a general theorem forcing a bounded minimum carrier, or excluding all
   carrier degrees, has not been established.

## 3. Recovered remote-only mathematical content

The four live remote-only research branches were missing from the cached
origin refs. Their newly recovered source contents are preserved as remote
snapshots rather than copied into active canonical note paths.

### Entirely-thick branch: 18 absent notes, still relevant

The branch `a843888...` contains 18 Oct 7 notes absent from the current
checkout. It retains the generic labelled transverse cluster, Rees
valuations, relative blowup cycle recursion, saturation and colon
recursion, equality-boundary quadric restriction, marked trisecant
coupling, and normalization/APic reformulation. These are new coverage
leads for the current session; their author labels are retained, without
a new independent proof audit.

The generic Noether excess budget is `ab/4-pq`. The notes explicitly
retain the limitation that normalized ratios do not bound cluster size
independently of p,q.

The strongest useful failure shields recovered are:

- `thick-root-budget-separation`: generic section coefficient c_i and
  special ruling-root multiplicity M_i live at different strata; no
  increasing lower bound c_i >= Phi(M_i) follows just from first
  exceptional geometry.
- `thick-segre-root-audit`: a trisecant root forces at least one selected
  common point, not all three. The established distinct-root bound
  survives, but stronger counting requires an actual coupling.
- `thick-boundary-carrier-rigidity`: at a=3p,
  F|Q=h^p R_F has exact h-order p and R_F is a repeated ruling divisor.
  Ambient lifting remains open; no power, factorization, or normalization
  is forced by this alone.
- `thick-apic-conductor-bridge` and
  `thick-generic-normalization-filter`: full inverse support and a
  positive Cartier/hyperplane relation are the correct normalization
  conditions. Clean conductor descent becomes automatic after a power;
  the global divisor class remains the obstruction.

The recovered sources were sent to the higher-carrier and thick-Rees
workers for degree-free synthesis.

### Order-one jet branch and e1 rebuild: geometry survives, mate searches superseded

The `f512d4d...` branch contains the 686-line order-one jet framework
and two old exact e1 companions. The main structural supplement recasts
ambient first symbols using the quadric comparison divisor R, the source
H0(I_R/Q(1,3)), and a finite target supported on 2R.

The `d5bed93...` branch contains a 490-line e1 rebuild plus three exact
sources. It preserves an explicit correction of the invalid implication
“a fixed residual ruling line itself excludes every possible mate.”
Its repaired argument uses the actual quartic carrier. Positive-defect
d2=1 sampling and elimination remained unfinished on that branch.

All of their actual quartic mate questions are superseded by the later
accepted all-quartic theorem. Their intrinsic R/2R description,
ambient-contact maps, and failed-shortcut record remain useful for
common-ancestor and degree-free programs. They were routed to the
local-cohomology worker without old verifier reruns.

### Normal-carrier branch: detailed failure history, no surviving quartic lane

The `4b936074...` branch contains a roughly 950-line Type-D classification
and resolution analysis, absent at its original local path. It records
endpoint and interior-point analyses, false attachment monotonicity,
corrected anticanonical coefficients, (-2)-tail Schur effects, and an
unfinished exact separation audit.

Its open normal-quartic status is superseded by the accepted complete
normal and all-quartic theorems. It is preserved as provenance and a source
of general resolution warnings, not a reason to restart normal quartics.

### Historical interrupted branch

The historical `2e53a7b...` tree has 37 paths absent from HEAD, mostly
old local-cohomology parity/seed scripts, validation snapshots, interrupted
scratch resultant sources, and dated notes. The exact names are retained
in the local inventory. The current canonical record already documents
the generator-coordinate/form confusion and corrected tensor. Neither an
old output nor an input script is promoted over the later accepted record.

## 4. Evidence files and continuation use

Directory:
`research/validation/2026-10-13-evening-branch-inventory/`.

- `remote-heads.json`: all seven live branch heads.
- `local-git-inventory.json`: exact local refs, graph counts, absent historical
  paths, worktree, tag and stash commands.
- `comparisons/*.json`: five successful GitHub merge-base comparisons.
  The ultra_mode comparison response records a transport failure;
  its exact live SHA and local graph remain available.
- `snapshot-manifest.json`: 25 recovered source snapshots with branch,
  head, original path, Git blob SHA and source URL.
- `snapshot-byte-checks.json`: all 25 saved sources match their returned
  Git blob SHA byte-for-byte, with SHA256 and byte lengths.
- `remote-snapshots/`: 18 thick notes, e1 rebuild, full jet framework,
  normal-carrier history, quadric-jet supplement, and three main synthesis
  files.

The byte checks validate archival identity only. They do not reverify
mathematics or count as new mathematical certificates.

A successor should use the new acceptance record for mathematical
status, this note for all-branch coverage, and exact snapshots for
previously untracked structural leads. No branch merge is needed for
research continuation.



---

## Source: 2026-10-13-evening-entirely-thick-rees-progress.md

# Entirely thick presentations: full conormal filtration and socle budget

Date: 2026-10-13. Status: **PROVED necessary structure, pending independent
audit**. This note gives a theorem about the entire complete-intersection
thickening, at every normal order. It does not exclude all entirely thick
presentations and does not resolve the STCI problem. No novelty claim is made.

## 1. Reconstructed frontier and retained boundaries

The current audited record is `research/AUDITED_STATE_2026-10-07.md`, updated
through October 12. The characteristic-zero curve

    C0 = [s^4:s^3 t:s t^3:t^4]

has normal bundle `O_P1(7)^2`. Every integral quartic carrier is now excluded
in characteristic zero, with arbitrary mate degree. The unresolved global
branches include higher-degree order-one carriers and entirely thick pairs.

The October 6 independent thick audit proves, for degrees `a,b` and exact
generic normal orders `p,q`, the first blowup restriction

    W = (u,v),
    u = 7ab/4 + 7pq - 4(aq+bp),
    v = ab/4 - pq,
    u >= 0, v >= 0, a >= 3p, b >= 3q.

At `a=3p,b=4q`, its support consists of constant sections and the quadric
residual binary form has at most `min(p,q)` distinct ruling roots. The
entire `a=3p,b=3q` boundary is already excluded by `u<0`.

The branch inventory recovered the live remote branch
`research/entirely-thick-rees-valuation`, commit
`a843888ce15b06247c576f8f717bec6b7ef5a352`, into
`research/validation/2026-10-13-evening-branch-inventory/remote-snapshots/`.
Its October 7 notes contain the generic Noether cluster reformulation,
the relative blowup budget, marked-root countershields, and the proof of
power saturation in degrees `d>=3m`. Direct inspection verified the
quadric exact sequence and the saturation proof in
`2026-10-07-rational-quartic-power-saturation.md`: there is no hidden
ordinary-power correction at or above degree `3m`.

The recovered notes deliberately reject a comparison between generic
exceptional-cycle coefficient and special repeated-root multiplicity.
This note retains that rejection. The higher data used below is the full
`I_C`-adic algebra of the complete intersection, together with its global
dualizing sheaf. It requires neither constant tangent roots nor clean
normalization/conductor hypotheses.

## 2. A theorem for any smooth support curve

Let `C` be a smooth integral projective curve in `P3` over an algebraically
closed field. Write its degree as `e` and genus as `g`. Let

    Y = V(F_a,G_b),  Y_red = C.

The two surfaces have no common surface component. Thus `Y` is a pure
one-dimensional Cohen--Macaulay Gorenstein complete intersection. Put

    J = I_C O_Y,
    A = O_(Y,eta),
    n = length A = ab/e,
    d = max { j : (J_eta)^j != 0 }.

Here `eta` is the generic point of `C`. The integer `d` is the actual
generic Loewy index of the full thickening; it is not the order of either
chosen equation. Write

    h_j = dim_(k(C)) (J_eta)^j/(J_eta)^(j+1),
    M = sum_(j=0)^d j h_j,
    L_j = J^j/J^(j+1).

Let `T_j` be the torsion subsheaf of `L_j` as an `O_C`-module, and
`B_j=L_j/T_j`. Then `B_j` is a vector bundle of rank `h_j`. Torsion in
these quotients is allowed and must be retained.

Choose a positive real number `lambda` such that every torsion-free
quotient `V` of `Sym^j N_(C/P3)^*` satisfies

    deg V >= -j lambda rank V                    (S)

for every `j>=0`. One elementary sufficient choice is `lambda=deg A0`
for a positive-degree line bundle `A0` with `N_C^* tensor A0` globally
generated: all symmetric powers after twisting by `A0^j` are then
globally generated. Thus the theorem has a choice of `lambda` for every
smooth support curve. In characteristic zero the standard slope theorem
also permits `lambda=mu_max(N_C)`; for semistable `N_C`, this is
`deg N_C/2`. The quartic application below uses its explicit split
normal bundle and does not depend on the slope theorem.

Define

    L = e(a+b-4) - (2g-2),
    Delta_j = deg B_j + j lambda h_j + length T_j,
    Delta = sum Delta_j,
    Asym = nd - 2M.

Then all the following hold:

1. `J^(d+1)=0` on all of `Y`.
2. The global socle along the support is the line bundle

       S_C(Y) = Ann_(O_Y)(J)
              = Hom_(O_Y)(O_C,O_Y)
              = omega_C tensor O_C(4-a-b).

3. `J^d` is a line bundle on `C` and there is an effective divisor `D`
   with

       J^d = S_C(Y)(-D).

4. `Sym^j N_C^*` surjects onto `L_j` for every `j`; hence
   `Delta_j>=0`.
5. The generic Gorenstein algebra satisfies `Asym>=0`.
6. The exact global budget is

       n(lambda d - L) = lambda Asym + 2 Delta.   (B)

In particular

       lambda d >= e(a+b-4) - (2g-2).            (N)

The effective top-socle defect is visible more precisely as

       deg D <= lambda d - L.

These assertions are independent of any upper bound on the degrees,
normal orders, or higher contact lengths. They apply equally to thick
and order-one presentations of a smooth support curve.

## 3. Proof: purity and the actual socle

Since `Y` is Cohen--Macaulay of pure dimension one and has only the
irreducible support `C`, the only associated point of `O_Y` is `eta`.
Every subsheaf of `O_Y` supported on finitely many closed points is zero.
The sheaf `J^(d+1)` is generically zero, so it is zero everywhere. This
does not assert that the quotients `L_j` are torsion free: a quotient of
a pure sheaf may have zero-dimensional torsion.

For the finite closed immersion `i:C->Y`, duality gives

    Hom_Y(O_C,omega_Y) = omega_C.

Since `omega_Y=O_Y(a+b-4)` is invertible, tensoring this identity by its
inverse gives the stated socle isomorphism. One can obtain the same
identity by the change-of-rings computation of
`Ext^2_(P3)(O_C,omega_(P3))` through the regular sequence `(F,G)`.
Its degree is

    deg S_C(Y) = 2g-2-e(a+b-4) = -L.

The ideal `J^d` is annihilated by `J`, and thus is a subsheaf of this
socle. The generic Artin algebra `A` is Gorenstein and has a
one-dimensional socle; its nonzero highest power `(J_eta)^d` lies in
that socle and therefore equals it. Consequently `J^d` is a rank-one
subsheaf of the socle line bundle. On the smooth curve it is locally
free and has the form `S_C(Y)(-D)` for an effective divisor `D`.

In particular the Loewy index at the generic point is a global
nilpotency bound, but special points can still contribute precisely
through the torsion of intermediate quotients and through `D`.

## 4. Proof: conormal quotients and Euler characteristic

The regular embedding `C->P3` gives

    I_C^j/I_C^(j+1) = Sym^j N_C^*.

Passing to `O_Y` therefore yields a surjection onto `L_j`. Composing
with `L_j->B_j` and applying (S) shows that

    deg B_j + j lambda h_j >= 0.

This proves `Delta_j>=0`, including the torsion length. For `j=d`,
`L_d=J^d` is torsion free and rank one, so

    -L - deg D = deg J^d >= -lambda d,

which gives the top-socle inequality directly.

Riemann--Roch on the support curve and additivity for the filtration
give

    chi(O_Y)
       = sum_j [deg B_j + length T_j + (1-g)h_j]
       = Delta - lambda M + n(1-g).

The complete-intersection genus formula gives

    chi(O_Y) = -ab(a+b-4)/2 = -ne(a+b-4)/2.

Combining them yields the exact relation

    2 Delta = 2 lambda M - n L.                  (E)

## 5. Proof: a Frobenius inequality retaining all higher jets

Choose a coefficient field in the completed generic Artin algebra; this
has residue field `K=k(C)`. Since `A` is Artin Gorenstein, choose a
`K`-linear functional nonzero on its socle. The multiplication pairing
defined by that functional is perfect. For every ideal `U` of `A`,

    dim_K Ann_A(U) = n - dim_K U.

With `m=J_eta`, the identity `m^(d+1)=0` gives

    m^(d-i+1) subset Ann_A(m^i),

and hence

    dim m^i + dim m^(d-i+1) <= n,  1<=i<=d.

Summing over `i` and using

    sum_(i=1)^d dim m^i = sum_j j h_j = M

gives `2M<=nd`. No symmetry of the Hilbert function was assumed:
the associated graded algebra of an Artin Gorenstein algebra can fail
to be Gorenstein. Formula (B) now follows from (E), with
`Asym=nd-2M>=0`.

This is the first-moment consequence of the classical symmetric
decomposition of a local Artin Gorenstein Hilbert function, but the
short pairing proof above avoids assuming that its individual layers
are symmetric.

## 6. Specialization to C0: an integral defect identity

For `C0`, take `lambda=7`, `e=4`, `g=0`. Then

    n=ab/4,
    mu=7d+14-4(a+b),
    Delta_j=deg B_j+7j h_j+length T_j.

The theorem becomes

    n mu = 7 Asym + 2 Delta,
    mu >= 0,
    0 <= deg D <= mu.                           (C0)

Every `Delta_j` is a nonnegative integer. This couples three genuinely
different measurements of the full thickening:

- its generic nonhomogeneous Gorenstein Hilbert function (`Asym`);
- global degree/torsion defects of all normal layers (`Delta`);
- the actual top socle line and its special-point divisor (`D`).

This is more information than the first blowup cycle. It is still a
necessary condition: large Loewy index is permitted, and the local
families already showing unbounded higher contact remain consistent
with it.

## 7. Equality rigidity: a constant graded Artin algebra

Suppose `mu=0`. The identity forces `Asym=0` and every `Delta_j=0`.
Consequently `T_j=0` and `deg B_j=-7j h_j` for all `j`. The bundle
`L_j(7j)` is a globally generated vector bundle of degree zero on `P1`,
so it is trivial. Thus

    L_j = O_P1(-7j) tensor B_j^0

for constant vector spaces `B_j^0` of dimension `h_j`.

After these twists, every multiplication map has constant coefficients:
it is a map between trivial bundles on the complete connected curve
`P1`. The surjections from `Sym^j N_C^*` also have constant matrices.
Therefore there is a graded Artin quotient `B` of `k[x,y]` with

    gr_J(O_Y) = direct_sum_j O_P1(-7j) tensor B_j.

At the generic point, equality in the summed Frobenius inequalities
forces equality in each individual inequality:

    m^(d-i+1) = Ann_A(m^i),  1<=i<=d.

The resulting pairings

    (m^i/m^(i+1)) x (m^(d-i)/m^(d-i+1)) -> m^d

are perfect. This proves that the associated graded algebra, and hence
the constant algebra `B`, is Gorenstein. In the entirely thick branch,
its embedding dimension is two. A graded Artin Gorenstein quotient of
`k[x,y]` is a homogeneous complete intersection, say of degrees `r,s`.
Thus equality imposes the exact relations

    ab = 4rs,
    d = r+s-2,
    4(a+b) = 7(r+s).                            (R)

The degrees `r,s` are the degrees of generators of the full initial
ideal, not necessarily the normal orders `p,q` of the chosen pair.
For example, a cancellation between chosen equations can expose the
second generator at a higher normal order. Identifying `(r,s)` with
`(p,q)` would discard the very higher-jet phenomenon this theorem
retains.

Equality is therefore a rigid boundary with a constant Gorenstein
normal algebra. This does not imply that the filtered algebra itself
is constant, or that its embedded formal neighborhood splits. Those
would require further extension/embedding arguments.

## 8. Explicit remaining equality data and limitations

The smallest thick degree pair surviving the old scalar inequalities is
`(a,b,p,q)=(6,8,2,2)`. Here `n=12` and the new theorem requires `d>=6`.
If `d=6`, equality forces a constant graded complete intersection of
degrees `(r,s)=(2,6)` and no normal-layer torsion or degree defects.
The alternative factorization `(3,4)` has socle degree five and is
incompatible with `d=6`.

This is an exact dichotomy for the full `(6,8)` thickening:

1. a very rigid constant graded `(2,6)` algebra at Loewy index six; or
2. a higher Loewy index with the defect budget in (C0).

Neither branch is excluded here. At equality the original two quadratic
symbols can be scalar multiples of the same constant quadratic
direction; their scalar coefficients can have complementary zero
divisors. Their cancellation produces the degree-six initial generator.
One must not assume that a global regular change of the original
homogeneous generators realizes that cancellation.

The result supplies no uniform bound on `d` or on `a,b`. It introduces
no tangent-only multiplicity cap, no generic-to-special root comparison,
and no assumption that the graded algebra is Gorenstein away from the
equality boundary.

## 9. Continuation targets

The useful next step is to analyze the full filtered deformation of the
constant graded complete intersection on the equality boundary, or to
bound the allowable global defect `Delta` using actual homogeneous
generation. This is a structural theorem before any computation.

For `(6,8)`, compare the global exact generator filtration

    0 -> O(-42) -> O(-24) + O(-32) -> O(-14) -> 0

suggested by a graded `(2,6)` model, with the actual sextic normal-image
constraints and the global embedded filtered deformation. The exact
sequence is a proposed next bridge, not established in this note.

For larger degrees, retain the entire nonnegative budget rather than
enumerating first symbols: every candidate generic Hilbert function
must satisfy its exact arithmetic, and every special-point repair must
pay the corresponding degree/torsion defect. There is no finite generic
Hilbert-function classification claimed uniformly in the degrees.

## 10. Provenance and standard inputs

The proof above derives the numerical budget and equality statement
directly. Standard inputs were checked against primary sources:

- Stacks Project, [regular immersions, Lemma 31.22.5](https://stacks.math.columbia.edu/tag/0638),
  for the symmetric conormal associated graded of a regular embedding.
- Stacks Project, [Duality for curves](https://stacks.math.columbia.edu/tag/0E31),
  and [finite-morphism duality, Remark 48.20.12](https://stacks.math.columbia.edu/tag/0AX4),
  for the actual socle line via the finite closed immersion.
- Iarrobino and Macias Marques,
  [Symmetric Decomposition of the Associated Graded Algebra of an Artinian
  Gorenstein Algebra](https://arxiv.org/abs/1812.03586), for the literature
  context behind nonhomogeneous Gorenstein Hilbert functions. Its
  symmetric-decomposition theorem is not needed for the elementary
  pairing proof in Section 5.

Memory was used only to route the higher-jet failure shield and the
existing first-normal-transverse boundary, then replaced by current
repository inspection: `/Users/markluxton/.codex/memories/MEMORY.md`,
lines 164--171. The older checkout-specific canonical state was not
transferred here. The memory rollout id is
`01a02fb1-2af7-7fa3-897c-9d6527951ac9`.


---

## Source: 2026-10-13-evening-general-conductor-power-compression.md

# A degree-independent conductor power-compression theorem

Date: 2026-10-13. Root continuation. Status: **NEW WRITTEN THEOREM;
independent mathematical review pending**. Existing audited conductor and
quartic results are accepted as premises at the user's direction. This
note generalizes the single-field phase mechanism used in the quintic
Jbar-zero lane. It is not an assertion that its hypotheses hold on all
carriers, and no novelty claim is made.

## 1. Full Artinian descent, without bounding nilpotent length

Let A -> B be an injective finite map of commutative Artinian local rings
of characteristic zero. Put K=A_red and E=B_red. Assume K is a field
containing every root of unity and E is a field of finite degree r over K.
If u is a unit of B and u^n belongs to A for some n>0, then

    u^m belongs to A, where m=[K(bar u):K] <= r.

Moreover m divides n. Consequently u^N belongs to A for
N=lcm(1,2,...,r). There is no bound on the lengths of A and B, and the
conclusion is membership in the actual nonreduced ring A.

Proof. Write alpha=bar u. Since alpha^n belongs to K and K contains all
n-th roots of unity, K(alpha)/K is the splitting field of the minimal
polynomial of alpha: all its roots lie among zeta*alpha and hence in
K(alpha). In characteristic zero it is a cyclic Galois extension, with
Galois group a subgroup of mu_n. Its order m divides n and alpha^m
belongs to K. Set s=n/m and w=u^n in A. The polynomial V^s-w over A
has the simple nonzero residual root beta=alpha^m in K; its derivative
s*beta^(s-1) is nonzero. The Artinian local ring A is Henselian, so it
has a unique root v in A with residue beta. Its image in B and u^m
have that same residual root and satisfy the same equation. Uniqueness
in B gives v=u^m. This proves membership in A, including every
nilpotent layer.

This proof can also be given by finite Newton iteration along the
nilradical. The only general reference consulted here is the simple-root
lifting property in [Stacks, Henselian local rings, tag 04GE](https://stacks.math.columbia.edu/tag/04GE).

## 2. Global surface theorem

Let X be an integral Cohen--Macaulay projective surface over an
algebraically closed characteristic-zero field, with finite normalization
nu:S->X. Let L be a line bundle on X and Q a nonzero section of nu^*L.
Assume:

1. The zero divisor of Q contains no prime of the upstairs conductor.
   Thus Q is a unit at every generic conductor point in a local frame
   pulled back from X.
2. At every generic prime eta of the downstairs conductor, the reduced
   upstairs conductor algebra is a single field E_eta over k(eta), of
   degree at most a fixed r. All full nilpotent conductor structures
   are retained.
3. Q^n descends to a section of L^n for some n>0.

Then Q^N descends to a section of L^N, where N=lcm(1,...,r).

Proof. Let I be the full conductor. At eta the actual quotients
A_eta=O_X,eta/I_eta and B_eta=(nu_*O_S)_eta/I_eta are Artinian, and
the second hypothesis makes B_eta local. The first hypothesis makes
the local representative of Q a unit; apply section 1, since k(eta)
contains all roots of unity. The image of Q^N lies in A_eta for every
eta. Membership modulo I is equivalent to actual membership in
O_X,eta, because I is the same ideal on both sides of the conductor
square.

The sheaf T=nu_*O_S/O_X has no associated closed points. At a closed
point x of X, both O_X,x and (nu_*O_S)_x have depth at least two: the
first by Cohen--Macaulayness, the second by normality at the finitely
many points of S over x and finiteness. The depth lemma gives depth
T_x>=1 whenever T_x is nonzero. Therefore a section of T tensor L^N
that vanishes at every generic support point vanishes everywhere.
Apply this to the image of Q^N. This argument preserves pointwise
noninvertibility of the conductor; it does not discard it or assume
that the downstairs conductor is Cartier.

The depth facts can be expressed using [Stacks, Depth, tag 00LE](https://stacks.math.columbia.edu/tag/00LE)
and [coherent depth and associated points, tag 0340](https://stacks.math.columbia.edu/tag/0340).

## 3. All-mate-degree consequence on a hypersurface

Suppose X is an integral degree-a surface in P3, L=O_X(d) with d>0,
and the reduced zero support of Q is precisely nu^(-1)(C). If any
power Q^n is an actual mate section, the theorem gives one of degree

    b <= d*lcm(1,...,r).

Indeed Q^N descends, has exactly the same zero support, and lifts to
an ambient homogeneous form of degree Nd by the hypersurface sequence
and H1(P3,O(Nd-a))=0. Thus this entire class of unbounded mate degrees
reduces to one bounded degree. For r=1 it descends already; for r=2
it suffices to test Q squared; for r=3, exponent six suffices.

The section Q and its divisor ray are part of the hypotheses. A mate
with several independently varying lifted multiplicities does not
automatically supply a fixed Q of bounded degree. Producing such a Q
uses a separate Cartier/Picard or exceptional-lattice argument.

## 4. Essential failure shields and the general research target

The single-field hypothesis is essential. For the diagonal subring
A=k in B=k x k and u=(1,zeta), with zeta of arbitrarily large finite
order n, u^n descends and no smaller positive power does. The sum of
residual field degrees is always two. Consequently neither the total
conductor degree nor a bound on Artinian length yields a uniform
phase exponent on split conductor algebras. The geometric exclusion
of split branches in existing proofs is doing real work.

In characteristic p, the derivative used above can vanish; nilpotent
depth can then require further p-powers. This is consistent with the
repository's Frobenius constructions. The characteristic-zero
hypothesis cannot be removed from this argument.

The useful degree-independent program is therefore:

* compress the lifted divisor ray to a primitive Cartier section Q;
* prove a geometric bound on residual field degrees on the actual
  conductor, and rule out uncontrolled split phases;
* apply full-ring power compression, then a ribbon/socle obstruction
  at the resulting bounded degree.

This avoids treating each mate exponent independently. The remaining
global bottlenecks are the primitive section degree, split conductor
phases, and coverage of entirely thick or generically nonregular
minimum carriers. None is assumed solved here.


---

## Source: 2026-10-13-evening-literature-refresh.md

# Literature refresh through October 13, 2026

Date: 2026-10-13, America/New_York. Lane: literature_refresh.
Status: **PRIMARY SOURCE SCOPES REFRESHED; bounded search; no universal resolution found.**
No canonical file was edited by this lane. This note does not independently
audit the new repository carrier proofs or certify their novelty.

The controlling records inspected were [the literature ledger](../LITERATURE_LEDGER.md),
[the current audited state](../AUDITED_STATE_2026-10-07.md),
[the October 10 primary refresh](OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-primary-literature-frontier-refreshmd),
[the October 6 positive-characteristic proof audit](2026-10-06-positive-characteristic-literature-audit.md),
and [the October 10 positive-characteristic primary refresh](OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-positive-characteristic-primary-refreshmd).
The current repository claims concern fixed
`C0=[s^4:s^3t:s t^3:t^4]` in characteristic zero, including all integral quartic
carriers and specified quintic normalization/projection families. Those
quantifiers remain distinct from all rational quartic embeddings and from the
universal integral-projective-curve question.

## 1. Current status: exactly what was found

No inspected primary source gives an unrestricted affirmative theorem for
every integral projective curve in `P^3`, a valid algebraically closed
characteristic-zero counterexample, or two arbitrary homogeneous defining
forms for fixed C0 in characteristic zero. This is a **bounded negative search
result**, not a proof that no unindexed resolution exists.

- David Eisenbud and Joe Harris, *The Practice of Algebraic Curves*, AMS,
  GSM 250 (2024), Example 3.13, printed pp.64–65,
  [official preview](https://www.ams.org/bookstore/pspdf/gsm-250-prev.pdf).
  The indexed publisher text again describes the two-equation question for
  the literal displayed C0 as “one of the most famous open problems in the
  theory of curves” (12 words). It also records a one-parameter family of
  projective orbits of smooth rational quartics. Direct PDF access failed;
  the indexed primary text was inspected. The 2024 date is bibliographic,
  not the search engine's crawl/publication label.
- Takumi Murayama, *MA665 Algebraic Geometry II*, Spring 2026,
  [author notes](https://www.math.purdue.edu/~murayama/ma665.pdf),
  Question 2.6.40 and Remark 2.6.41, printed p.199.
  The question asks whether irreducible projective curves are STCI, and the
  historical remark explicitly retains its open status after Perron's
  correction of Vahlen. Direct PDF opening failed; the indexed author text
  at the numbered question was refreshed. The April 28 compilation date is
  from the earlier checked primary note; it was not independently extracted
  anew in this refresh.
- Robin Hartshorne and Claudia Polini,
  [*Quasi-cyclic modules and coregular sequences*](https://arxiv.org/html/1907.05472),
  abstract, Setting 5.1, and Example 7.10(1), directly refreshed. The paper
  treats coregularity/codepth criteria and necessary conditions. Its
  characteristic-zero C0 problem remains undecided in Example 7.10(1), while
  the positive-characteristic example is affirmative. Their explicit
  wording includes “the still open problem” (4 words), referring in the
  abstract to connected curves in P3. Neither the criteria nor the
  vanishing of higher local cohomology constructs the required sequence.

The [Murayama companion notes](https://www.math.purdue.edu/~murayama/LocalCohomology.pdf),
section 5, Open Question and Example 11, were independently found again in
indexed author text. They retain the irreducible P3 question and literal
smooth rational quartic example. This is corroborating dated evidence, not
a contemporary resolution search by the notes' author.

## 2. Quartic-carrier overlap and the novelty boundary

The following actual theorem scopes were refreshed in primary full text.

| Source and exact location | Established scope | Boundary relevant here |
|---|---|---|
| Craighero–Gattazzo, [1986 original PDF](https://www.numdam.org/item/RSMUP_1986__76__177_0.pdf), introduction pp.177–178 and Proposition 4, p.187, PDF zero-based page 11 | Fixed Cremona/Macaulay quartic is not the intersection of two quartic surfaces over an algebraically closed field with characteristic different from 2 and 3 | Excludes `(4,4)`, not `(4,b)` for every b. The preceding trisecant argument prevents an integral quartic carrier from being double along C0. |
| Craighero–Gattazzo, [1989 original PDF](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf), abstract and introduction pp.171–173 | Every smooth rational quartic over an algebraically closed characteristic-zero field is excluded on every cubic surface with arbitrary mate degree | Gives all `(3,b)`, not all `(4,b)`. |
| David B. Jaffe, [*Applications of iterated curve blow-up to set theoretic complete intersections in P3*](https://arxiv.org/html/alg-geom/9410008v1), Theorem 11.11, printed p.45 | A quartic surface with rational singularities whose intersection with another surface is set-theoretically a smooth curve forces that curve to be linearly normal; displayed statement is over C | Does not cover every nonnormal quartic carrier. The proof's replacement `g -> g+fh` removes a mate singular generically along C; it does not require the original mate to be smooth there. |
| Philippe Ellia, [*Complete intersections primitive structures on space curves*](https://arxiv.org/html/1409.3801), introduction, Corollary 16 and Remarks 17–18 | Characteristic-zero primitive STCI numerical restrictions for smooth rational quartics leave ten degree pairs, including `(4,7)` | Primitive requires local containment in a smooth surface. Quasiprimitive with simultaneous isolated singularities and thick structures have separate scope. A surviving numerical pair is not an existence theorem. |

Jaffe's finite degree list and Theorem 13.1 retain the **no common singular
points** hypothesis; the introduction explicitly places that hypothesis
before its bounds. Ellia's retained higher pairs are
`(6,26),(12,18),(10,28),(9,48),(22,50),(20,67),(19,84),(18,118),(17,220)`.

Hartshorne–Polini,
[*Divisor class groups of singular surfaces*](https://arxiv.org/html/1301.3222),
Proposition 7.1, characterizes STCI on a chosen surface by `r C=m H` in
APic when C meets its singular locus in finitely many points. Corollaries
7.9–7.10 exclude a smooth rational quartic on characteristic-zero surfaces
with at most ordinary singularities and ordinary nodes, with C outside the
singular locus. Example 7.16 treats a particular rational quartic surface
with elliptic conductor, not every degeneration. These interfaces preserve
the necessity of full Cartier/conductor data. Example 7.13 and Remark 7.14
also prevent replacing arbitrary mate orders by a presumed uniformly
bounded order from an open/closed-locus argument.

**Bounded novelty assessment.** None of these checked sources states the
repository's all-integral-quartic-carrier exclusion for fixed C0 with an
arbitrary positive mate degree, or its newest specified quintic exclusions.
The repository has extended the checked source scopes if its assembled
proofs hold. This is not a priority or novelty certificate. It supplies no
claim that an arbitrary STCI presentation must have a quartic carrier.

## 3. Positive characteristic: the verified family and the remaining gap

T. T. Moh, *Set-theoretic complete intersections*, Proc. AMS 94 (1985),
217–220, DOI 10.1090/S0002-9939-1985-0784166-1,
[official AMS abstract](https://www.ams.org/proc/1985-094-02/S0002-9939-1985-0784166-1/),
was refreshed through indexed publisher text. The monomial result concerns
every projective monomial curve in characteristic p>0. The other result
requires an algebraically closed field of positive characteristic and a
linear plane projection whose center misses the curve, is birational on
the curve, and has a plane image with only cusps. All those hypotheses are
present. Direct article/PDF access returned errors, including 403, so this
is abstract verification, not a new inspection of the original proof.

Consequently **fixed C0 is an STCI in every positive characteristic** by
the monomial-family theorem. This does not establish the universal
projective statement. The repository's separate all-smooth-rational-quartic
construction has its own proof scope and is not a direct application of
Moh's disjoint-center projection clause.

The inherited Cowsik–Nori theorem concerns affine curves. The cone over a
projective space curve is a surface in A4, so it is outside that curve
theorem. The established Das finite-field-closure affine-surface result
requires lci at every point. The cone of a projective curve that is not
already a scheme-theoretic CI fails lci at the vertex: the two local
generators at the irrelevant maximal ideal would imply two minimal
homogeneous generators globally. This is the exact repository cone
obstruction, not a negative theorem about positive-characteristic
projective STCI.

No checked theorem from the refreshed searches proves every integral
projective curve in P3 is STCI over Fpbar or over every algebraically
closed field of characteristic p. Even an affirmative theorem over
Fpbar would not by itself cover curves whose coefficients generate a
transcendental extension of Fp. Degree-zero Picard torsion also does not
eliminate Neron–Severi or full conductor obstructions on a chosen carrier.

## 4. Modern toric input is especially explicit about its restricted rank

Anargyros Katsabekis and Apostolos Thoma,
[*Radical splittings of toric ideals*](https://link.springer.com/article/10.1007/s10801-026-01593-w),
J. Algebraic Combinatorics 64 (2026), article 42,
**published September 28, 2026**, DOI 10.1007/s10801-026-01593-w.
Publisher full text was accessible and inspected.

The abstract identifies radical splitting with **binomial** arithmetic
rank for height-two toric ideals. Section 4, Remarks 4.7, gives radical
splitting number 2 in positive characteristic and 3 in characteristic
zero for symmetric projective monomial curves
`[u^d:u^(d-a)v^a:u^(d-b)v^b:v^d]`, where `a+b=d` and
`gcd(a,b,d)=1`. Fixed C0 has `(a,b,d)=(1,3,4)`, so this directly
confirms its binomial rank is 3 in characteristic zero. It does not
exclude two arbitrary forms. This is a sharper source-specific scope
than describing the paper merely as recent toric work.

## 5. Mandal–Zinna: published conditional results and a still-unrepaired v1

The primary publisher abstract and introductory theorem extract were
refreshed for *Set-theoretic complete intersection for curves in affine
three-folds*, J. Algebra 690 (15 March 2026), 101–113,
[publisher page](https://www.sciencedirect.com/science/article/abs/pii/S0021869325006295),
DOI 10.1016/j.jalgebra.2025.10.042. Theorem 1.2 concerns a dimension-three
affine algebra over a characteristic-zero C1-field, a height-two lci
ideal with free conormal of rank two, and torsion Grothendieck-group
class. The ring-level variant adds the condition that every stably free
rank-three module is free. This gives an affine conditional theorem;
it has no compatibility condition at projective infinity.

The separately published *Set-theoretic complete intersection for smooth
surfaces in a smooth affine algebra*, J. Algebra 693 (1 May 2026), 36–53,
[publisher page](https://www.sciencedirect.com/science/article/abs/pii/S0021869326000165),
DOI 10.1016/j.jalgebra.2025.12.026, still has the smooth affine Fpbar
ambient, trivial conormal and torsion Grothendieck-class hypotheses in
its abstract. Missing rendered dimension formulas were not silently
filled in. It gives no universal projective theorem.

[arXiv:2511.07589](https://arxiv.org/abs/2511.07589) still shows only
v1, submitted **November 10, 2025**. Native arXiv metadata was also
independently retrieved through the connected Sider Scholar tool.
The abstract claims arbitrary dimension-three affine lci curves are
STCI and gives analogous four-dimensional Fpbar claims. The broad v1
must be labeled **CLAIM WITH AN INVALID DISPLAYED PROOF**, not a verified
general theorem: the October 6 exact audit applies unchanged. This
qualifies the ledger's abstract-only “verified abstract theorem” wording.
Refreshing an unchanged abstract does not repair the proof.

The faulty Step 3 was directly inspected again in
[v1 full text](https://arxiv.org/html/2511.07589v1), following equation (1).
It substitutes `J/(c)` for the tensor quotient `J/cJ`. To independently
reconstruct the exact countercheck, take

```
A=k[x,y,z], J=(x,y), c=x,
0 -> A -> A^2 -> J -> 0,
t |-> (-yt,xt), (a,b) |-> ax+by.
```

With `B=A/(x)`, the displayed last term `J/(x)` gives a complex
`B -> B^2 -> (y)` whose middle kernel is `B(1,0)` but whose preceding
image is `yB(1,0)`. Its middle homology is `B/(y)`, nonzero. If the
notation instead means the actual tensor quotient `J/xJ`, the class of
x in `(x,y)/(x^2,xy)` is nonzero and killed by y, so the assertion of
local rank-one freeness fails. This exact computation invalidates the
splitting step. The separate real-sphere example in the October 6 audit
refutes the unrestricted arbitrary-Noetherian-ring CI claim; it is not
a projective counterexample over an algebraically closed field.

No revised arXiv version or primary correction to that step was found.
The newer peer-reviewed titles were not conflated with this v1.

### Two additional 2026 affine papers discovered

Lisa Mandal, *Set theoretic complete intersection of ideals in a Laurent
polynomial ring*, Communications in Algebra 54(11) (2026), 3565–3573,
[publisher abstract](https://www.tandfonline.com/doi/abs/10.1080/00927872.2025.2604611),
DOI 10.1080/00927872.2025.2604611, published online January 13, 2026.
The abstract requires a dimension-n affine algebra over Fpbar with n>=3,
an lci ideal of height n in `A[T,T^-1]`, free rank-n conormal and torsion
Grothendieck class. It proves STCI under those assumptions. It does not
close the homogeneous-projective gap.

**DISCOVERY LEAD ONLY:** Lisa Mandal and Md. Ali Zinna,
*On the minimal number of generators of local complete intersection
ideals in affine four-folds*, J. Pure Appl. Algebra 230(11) (2026),
article 108384, DOI
[10.1016/j.jpaa.2026.108384](https://doi.org/10.1016/j.jpaa.2026.108384).
The title/authors/DOI were returned by connected OpenAlex metadata
record W7204541041; the journal issue and article number also appear
in MathNet citation indexing. Secondary discovery text describes a
three-generator bound over Fpbar under reduced-K0 vanishing.
The primary publisher text and proof were inaccessible in this lane,
so that formulation is **not used as a verified theorem**. A successor
should retrieve its primary abstract and actual hypotheses before
comparing it with the audited v1. In particular, a smooth affine
surface that is not a scheme CI need not be a non-STCI, and supplies
no projective counterexample by itself.

## 6. Another tempting negative claim still has no repaired source

Vahap Erdoğdu,
[*Radically finite rings and space curves*](https://arxiv.org/abs/2209.04489),
still shows only v1, submitted **September 9, 2022**. Its abstract
claims a negative conclusion about space curves. The exact October 6
[unique-maximal/unique-prime countercheck](2026-10-06-session-literature-refresh.md)
remains controlling; no revised version or primary corrected proof was
located. The invalid argument is not an established resolution of the
user's projective algebraically closed problem.

## 7. One bibliographic correction to the inherited ledger

S. Hamid Hassanzadeh,
[*Set-theoretically perfect ideals and residual intersections*](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms.70108),
was published in **J. London Math. Soc. 111(3) (2025), e70108**,
first published **March 6, 2025**, DOI 10.1112/jlms.70108.
The publisher's indexed primary abstract and bibliographic block
were inspected; direct Wiley opening failed. The ledger's “to appear”
wording is outdated even though arXiv metadata remains v2 of February
12, 2025. Its residual-intersection perfectness and cohomological-CI
claims retain Serre-condition hypotheses. Neither perfectness nor
cohomological complete-intersection behavior says that a same-support
ideal has two generators.

## 8. Search and access provenance

Search date throughout: October 13, 2026. Primary theorem statements,
not search-engine crawl ages or secondary summary labels, control all
verified scope assertions above. Queries included:

1. `"set-theoretic complete intersection" "projective" "curves" "2026"`;
   `"set-theoretic complete intersections" "integral projective"`;
   `"set-theoretic complete" "projective curves" "2025" "2026"`.
   Returned dated author sources, affine papers and many irrelevant hits;
   no accepted unrestricted projective resolution was identified.
2. `"rational quartic" "set-theoretic" "quartic"`;
   `"rational quartic" "quartic surfaces" "set-theoretic"`;
   `"Cremona quartic" "set-theoretic complete"`;
   `"quartic" "set-theoretic complete intersections" "Jaffe" "2026"`;
   `"rational quartic" "set-theoretic" "2025" "2026"`.
   Actual Craighero–Gattazzo, Jaffe and Ellia theorem locations were
   inspected after discovery; no checked all-integral-quartic theorem
   emerged.
3. `site:ams.org/bookstore/pspdf/gsm-250-prev.pdf "famous" "quartic"`;
   `site:math.purdue.edu/~murayama/ma665.pdf "Question 2.6.40"`;
   `site:ams.org "0784166" "monomial"` and the corresponding `"cusps"`
   query. These returned the indexed publisher/author originals and
   allowed exact primary scope checks despite direct PDF/403 failures.
4. `"projective curves" "set-theoretic complete" "positive characteristic"`;
   `"quintic" "set-theoretic" "nonnormal" "curve"`.
   Restricted toric/cuspidal families and conductor papers were found.
   The first query supplies no universal positive-char theorem.
5. `"Mandal" "Zinna" "set-theoretic" "2026"`;
   exact-title and `"four-folds"`, `"108384"`, DOI queries.
   The two conditional J. Algebra papers and the Laurent paper were
   checked on primary publisher text. The affine-fourfold paper remained
   a metadata/discovery lead after DOI and issue-page access failures.
6. `"Set-Theoretically Perfect Ideals and Residual Intersections" "2026"`;
   publisher-domain exact-title query; `"Radical splittings of toric ideals"
   "2026"`. These supplied the actual JLMS publication correction and
   the September 28 toric primary article.
7. Direct current arXiv abstract/version records for `2511.07589`,
   `2209.04489`, `1907.05472`, `2409.05705`, `1312.7661`, plus actual
   HTML theorem locations for Jaffe, Ellia and Hartshorne–Polini.
   No later versions repairing the two audited v1 arguments appeared.

Connected-tool provenance: a Sider Scholar OpenAlex search for
`set-theoretic complete intersection curves`, filtered from 2024 and
sorted by newest, returned numerous irrelevant results. A second
concise author/title search also missed the affine-fourfold target.
These outputs are search limitations, **not absence evidence**. Native
arXiv lookup for `2511.07589` succeeded and agreed with the primary
record. Exact-DOI OpenAlex retrieval for the affine-fourfold paper
succeeded, but supplied no inspected primary theorem text. No external
messages were sent, and no items were imported to a scholarly library.

## 9. Continuation consequences

- Keep the universal statement and unrestricted characteristic-zero C0
  problem unresolved. The inherited strongest carrier results have their
  repository proof/audit provenance, not external-resolution status.
- Correct the ledger's broad Mandal–Zinna v1 framing using the existing
  exact audit; do not downgrade the distinct conditional published papers.
- Update Hassanzadeh's publication status and the recent toric entry's
  exact symmetric-monomial/binomial-rank scope.
- Retrieve the new JPAA paper's primary theorem before using it. Its
  indexed affine dimension/field/K-theory restrictions must not be
  dropped even if the abstract eventually confirms the discovery text.
- For a serious novelty assessment of the all-quartic and quintic proofs,
  continue citation-chain and nonnormal-degeneration comparison. The
  bounded search here does not settle priority.


---

## Source: 2026-10-13-evening-localcoh-exception-fields.md

# Second endpoint family: exact cubic and quartic exception closure

Date: 2026-10-13. Scope: characteristic zero, the fixed smooth rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, the audited actual quartic-ancestor multiplication
tensor, primitive degree-two normal-dual directions, pure cubic top `h=t`,
and the second rational endpoint family. This does not address boundary
families with `p(0)=0`, nonendpoint cubic top zeros, or higher ancestor degrees.

## Exact result currently completed

**PROVED under the audited actual multiplication tensor and coordinate bases:**
every root of both factors

```text
f3=3*k^3+4*k^2+9*k-4
f4=13*k^4+10*k^3+2*k^2-42*k-7
```

is excluded for **every** affine lower-lift parameter `lambda`. These account
for seven of the 22 geometric parameter points still retained after the
accepted generic and quadratic calculations. The degree-15 factor remains
OPEN pending the separate exact field calculation discussed below.

The Macaulay2 computations returned target evaluation ideal `(1)` over each
number-field polynomial ring `K[lambda]` and a polynomial left dual `n` with

```text
n^T L(a*(k)+lambda*k0)=0,
n^T u=1.
```

The cubic dual has 26 nonzero entries and degree at most two in `lambda`.
The quartic dual has 26 nonzero entries and degree at most one in `lambda`.
Consequently these certificates exclude the entire affine lower-lift fibers;
they are not ranks or point samples.

## Full-fiber verification and logical scope

The new standard-library verifier
[`evening_localcoh_family2_exception_fields_2026_10_13.py`](../computations/evening_localcoh_family2_exception_fields_2026_10_13.py)
uses `Fraction`, exact polynomial division, and a restricted AST expression
parser. It works in the quotient `QQ[k]/(f)` represented by coefficient
vectors and separately in its polynomial variable `lambda`. Its certificate
verification rederives every source denominator inverse, all rational
direction expressions, all 30 seed coefficients, the affine slope vector,
and both primitive homogeneous directions. It checks:

1. The actual 32-by-30 top matrix has rank 29 over `QQ`.
2. The specified slope vector is nonzero and every seed plus `lambda*k0`
   satisfies all 32 pure-top identities. Since the top map has one-dimensional
   kernel, this gives every possible affine lift of the specified top.
3. The factor is square-free, so its degree counts distinct geometric roots.
4. The homogeneous Sylvester determinant matches the rational source
   resultant and is a **unit** modulo the factor, so every root has a
   primitive direction and no omitted nonprimitive stratum.
5. The actual tensor target columns are `e72,e73`, the dual coordinate
   `n72` is the constant one, and all eighteen entries of `n^T L` vanish
   identically as polynomials in `lambda` modulo the full factor.

The last identities imply exclusion after every homomorphism from the
quotient into an algebraically closed field of characteristic zero. Thus
coverage of all roots does not depend on accepting a numerical embedding,
a sampled rank, or even the Macaulay2 factorization result. The exact
Macaulay2 `factor` output also reports both factors as irreducible, but the
independent verification only needs square-freeness and the explicitly
checked unit inversions.

The actual tensor and coordinate sources are unchanged and SHA-256-bound
inside each certificate. They are the same tensor sources accepted in the
[previous independent quadratic audit](OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#source-2026-10-08-session-localcoh-family2-quadratic-independent-auditmd).
This certificate inherits that audited coordinate interpretation; it does
not reconstruct the ambient quotient basis from fresh geometric generators.

## Reproduction and retained evidence

Generate the exact matrix inputs:

```sh
python3 research/computations/evening_localcoh_family2_exception_fields_2026_10_13.py --generate cubic quartic
```

Generate the full polynomial left kernels and duals:

```sh
/opt/homebrew/bin/M2 --script research/computations/evening-localcoh-family2-cubic-2026-10-13.m2
/opt/homebrew/bin/M2 --script research/computations/evening-localcoh-family2-quartic-2026-10-13.m2
```

Regenerate the two exact JSON certificates and verify all identities:

```sh
python3 research/computations/evening_localcoh_family2_exception_fields_2026_10_13.py --regenerate cubic quartic
```

Thereafter default verification uses only the saved certificate and an
ordinary Python 3 runtime:

```sh
python3 research/computations/evening_localcoh_family2_exception_fields_2026_10_13.py cubic quartic
```

Evidence, including the raw complete duals, target ideal outputs, terminal
logs, and JSON certificates, is retained under the respective stems
`research/computations/evening-localcoh-family2-cubic-2026-10-13` and
`research/computations/evening-localcoh-family2-quartic-2026-10-13`.
The final full-kernel processes returned exit code zero; the cubic process
finished directly and the quartic process was collected from tool session
`90236`. The strengthened independent regeneration/verification returned
exit code zero for both cases.

## Failed attempts and runtime details

The first generated M2 source used `assert #factor f==1`, which is invalid
for this Macaulay2 version because `factor` returns a `Product`. Both runs
stopped at that parser/type check before constructing any matrix. The failed
logs are preserved as `...-attempt01.log`; no mathematical result is taken
from those runs. The corrected source prints `factor f`, and the all-roots
logic is instead independently checked by exact quotient identities.

The historical SymPy interpreter path currently exists but lacks the SymPy
package (`ModuleNotFoundError`). No package installation was required. A
`--script /dev/stdin` factor probe also failed because M2 could not reopen
the shell-generated descriptor path; a saved ordinary `.m2` file succeeded.

## Continuation at the degree-15 factor

The exact generalized arithmetic includes the remaining degree-15 modulus.
A separate agent is attempting a polynomial dual of degree at most two via
ordinary field linear algebra. Writing `L=L0+lambda*L1` and
`n=n0+lambda*n1+lambda^2*n2` reduces the full polynomial identity to

```text
L0^T n0=0
L0^T n1+L1^T n0=0
L0^T n2+L1^T n1=0
L1^T n2=0
(n0)72=1, (n1)72=(n2)72=0.
```

This is a 75-by-222 exact linear system over `QQ[k]/(f15)`. A successful
solution will be independently checked against all source expressions by
the same generalized verifier. Existence has not yet been asserted here.


---

## Source: 2026-10-13-generalization-conductor-theorem.md

# Conductor torsion, primitive Cartier rays, and a finite carrier criterion

Started 2026-10-13; completed in the 2026-10-14 continuation.
Author: `conductor_general`, with independent new-proof audits by
`split_unit_audit` and `cartier_lattice_audit`.

Status: **NEW STRUCTURAL THEOREMS WITH WRITTEN PROOFS; independent audits
recorded below.** Previously accepted repository claims were used as
context and were not recomputed. This note audits and substantially
extends the new
[power-compression proposal](#source-2026-10-13-evening-general-conductor-power-compressionmd).
No novelty claim is made. These results give a degree-independent
framework on a **fixed carrier**; they do not classify all carriers or
resolve the global projective-curve STCI question.

## 1. Exact characteristic-zero local theorem

Let `A -> B` be a finite injective unital map of commutative Artinian
rings containing `Q`. Assume `A` is local, but allow `B` to be semilocal.
Write

```
N_A = nil(A),  N_B = nil(B),  K = A/N_A,
E = B/N_B = product_i E_i,
G = B^*/A^*,  R = E^*/K^*.
```

Here `K^*` maps diagonally to the finite field extensions `E_i`.
Since the map is injective, `N_A = A intersect N_B`.

**Theorem 1.** Reduction gives an exact sequence of abelian groups

```
0 -> N_B/N_A -> G -> R -> 0,
```

where the left-hand map is induced by the finite exponential series.
The kernel is a uniquely divisible `Q`-vector group. In particular,
reduction induces a **canonical isomorphism**

```
Tor(G)  ->  Tor(R).
```

Consequently, if a given unit `u` has any positive power in `A`, then
the **smallest** such exponent is precisely the order of its residual
class in `R`. Nilpotent layers add no exponent once eventual descent
has been established.

Proof. Units lift across nilpotent ideals. A unit whose residual class
is diagonal can be divided by a unit of `A` having the same residue,
leaving an element of `1+N_B`. The finite series

```
log(1+x) = x - x^2/2 + x^3/3 - ...,
exp(x)   = 1 + x + x^2/2! + ...
```

are mutually inverse group isomorphisms between `1+N_B` and the
additive group of `N_B`, and restrict to the corresponding groups for
`A`. This proves the exact sequence.

For a torsion residual class `r` of order `e`, choose any lift `g` in
`G`. Then `e g` belongs to the kernel. Subtract its uniquely defined
`e`-th part in that kernel from `g`; the result is an `e`-torsion lift
of `r`. A torsion lift is unique because the kernel is torsion-free.
If an actual class `g` is torsion, its order therefore equals the order
of its residue. This is a group-theoretic proof retaining every
nilpotent layer. Alternatively, the simple-root lifting argument in
the proposal proves the same exponent statement directly.

### A necessary distinction: residual torsion is not enough

A specific unit can have torsion residue but no power in `A`. For
example,

```
A=k,  B=k[epsilon]/(epsilon^2),  u=1+epsilon
```

in characteristic zero has trivial residual class, whereas
`u^n=1+n epsilon` never belongs to `A` for positive `n`.
Thus the torsion isomorphism does **not** assert that every lift of a
torsion residual class is torsion.

The missing condition has an exact logarithmic certificate. Suppose
the residual class of `u` has order `e`, so all residues `alpha_i^e`
equal a common `beta in K^*`. Choose `a in A^*` with residue `beta`.
Define

```
delta(u) = (1/e) log(u^e/a) mod N_A  in N_B/N_A.
```

This is independent of `a`, because replacing `a` changes the
logarithm by an element of `N_A`. It is also independent of replacing
`e` by a positive multiple and is a homomorphism on the preimage of
`Tor(R)`. The following are equivalent:

```
delta(u)=0;
u^e belongs to A;
some positive power of u belongs to A.
```

Indeed `log(u^e/a) in N_A` is equivalent, after exponentiating, to
`u^e/a in 1+N_A`. Conversely, if a power descends, Theorem 1 forces
the nilpotent kernel component to vanish. On the preimage of residual
torsion there is therefore a canonical decomposition into the
nilpotent defect and the unique torsion lift.

## 2. Split fields: a shared Kummer extension plus finite phases

Assume now that `K` has characteristic zero and contains all roots of
unity. Let `alpha=(alpha_i) in product E_i^*` have torsion class in
`R`, meaning that `alpha_i^n` are all the same element of `K^*` for
some `n>0`.

Fix embeddings of the `E_i` into one algebraic closure of `K`. Then

```
alpha_i = zeta_i alpha_1,  zeta_i in mu_infinity(K),  zeta_1=1.
```

It follows that all fields `K(alpha_i)` are the **same cyclic Kummer
extension** in this algebraic closure. Put

```
m = [K(alpha_i):K].
```

Then `m` divides every `[E_i:K]`. Also `alpha_i^m in K^*` for every
`i`. If

```
beta_i = alpha_i^m,
t = lcm_i order(beta_i/beta_1),
```

the exact residual order is

```
e = m t = lcm(m, order(zeta_2), ..., order(zeta_s)).
```

Proof. The polynomial `T^n-alpha_1^n` splits over `K(alpha_1)` because
`mu_n subset K`; thus `K(alpha_1)/K` is cyclic Galois. Its group embeds
in `mu_n` by `sigma -> sigma(alpha_1)/alpha_1`. Its order is `m`,
and `alpha_1^m in K`. Any exponent putting `alpha_1` in `K` is
divisible by `m`; conversely each multiple of `m` does so.
The same statements hold for each `alpha_i`. After writing an exponent
as `m h`, equality of all branch values is equivalent to
`(beta_i/beta_1)^h=1` for every `i`, giving `e=m t`.

The formula using `beta_i` is intrinsic. The formula using `zeta_i`
uses chosen embeddings, but its value is unchanged when those
embeddings change: the resulting changes are roots of unity of order
dividing `m`.

For a single field `E`, the phase factor is absent:

```
e=m divides [E:K].
```

This sharpens the original proposal. If actual residual extension
degrees at the finitely many generic conductor components are known,
the common exponent is their least common multiple. The proposal's
`lcm(1,...,r)` remains valid when only the numerical bound
`[E:K]<=r` is known. In particular, an actual degree-three field needs
exponent three, rather than the conservative exponent six obtained
from the bound alone.

For several fields, the bounded Kummer factor satisfies

```
m divides gcd_i [E_i:K],
```

but the relative phase factor can have arbitrarily large order.
The example `A=k`, `B=k x k`, `u=(1,zeta)` exhibits arbitrary exact
order with total residual degree two. This obstruction persists with
fixed ring lengths. A degree or length bound alone cannot control
split phases.

One optional description of the residual torsion is useful. With
the chosen embeddings, put `F=intersection_i E_i` inside the algebraic
closure. The preceding argument gives

```
Tor((product E_i^*)/K^*)
    ~= Tor(F^*/K^*) x mu_infinity(K)^(s-1),
```

by taking the common radical class represented by `alpha_1` and the
ratios `alpha_i/alpha_1`. The displayed splitting uses embeddings;
the intrinsic exponent and the torsion reduction theorem do not.

## 3. Audit of the proposed global compression theorem

The proposal's global theorem is correct under its stated hypotheses:
finite normalization, integral Cohen--Macaulay projective surface,
characteristic zero, a section `Q` which is a unit at every generic
upstairs conductor point, a single residual field over each generic
downstairs conductor point, and existence of an actually descending
power. The unit hypothesis and the existence of some descending
power are essential.

The local theorem proves membership in the **full** conductor
quotient, not only its reduction. At a closed point of a surface,
both `O_X` and `nu_*O_S` have depth at least two: the first by
Cohen--Macaulayness and the second by normality and finiteness.
Hence the depth lemma gives

```
depth_x(nu_*O_S/O_X) >= 1
```

when the quotient is nonzero. This quotient has no associated closed
points. Its only possible associated points are generic points of
the conductor curves. A section of this quotient vanishing at all
those points is zero. This justifies passing from generic conductor
membership to global descent; no Cartier hypothesis on the
downstairs conductor is needed.

A sharper choice in that theorem is

```
N = lcm_eta [E_eta:k(eta)]
```

when the actual single-field degrees are known. No Artinian length
bound enters this exponent.

## 4. An exact fixed-carrier criterion, including thick support

This section does **not** need characteristic zero. Work over any
algebraically closed field. Let `X` be an integral Cohen--Macaulay
projective surface with finite normalization `nu:S->X`, let `L` be an
ample line bundle on `X`, and put `H=nu^*L`. Let `C` be an integral
curve on `X`. Write the full reduced inverse image as `W`.

If `W` contains an isolated point not lying on its curve components,
there is no section cutting `C` set-theoretically: the pullback of
such a section is an effective Cartier divisor on the normal surface
`S`, whose support has pure codimension one. Hence suppose

```
W = Gamma_1 union ... union Gamma_s
```

has no isolated points. Let `I` be the **full** conductor ideal.

Define the Cartier relation lattice

```
Lambda = ker[ Z^(s+1) -> Cl(S) ],
(n_1,...,n_s,d) -> sum n_j[Gamma_j] - d[H].
```

A vector in `Lambda` gives a rational section `Q_v` of `O_S(dH)`
with divisor `sum n_j Gamma_j`. It is unique up to `k^*`, since `S`
is integral, normal and projective. If all `n_j>=0`, normality makes
the rational section regular. A nonzero such effective divisor
forces `d>0`, by intersecting with the ample divisor `H`.

For each generic conductor point `eta` whose curve is different from
`C`, set

```
A_eta = O_X,eta/I_eta,
B_eta = (nu_*O_S)_eta/I_eta,
G_eta = B_eta^*/A_eta^*.
```

These are the actual Artinian conductor rings. The rational section
`Q_v`, in a frame pulled back from `X`, is a unit at every branch
above this `eta`, since its divisor is supported on `W`. Its class
in `G_eta` is independent of the frame and of its global scalar.
Multiplication of sections gives a homomorphism

```
phi: Lambda -> G = product_{eta off C} G_eta.
```

Define the descent lattice

```
Lambda_desc = ker[ Lambda -> G/Tor(G) ].
```

**Theorem 2.** A positive power of a section of a positive tensor power
of `L` cuts out `C` set-theoretically if and only if

```
Lambda_desc contains v=(n,d) with every n_j>0.
```

Equivalently, `C` has a mate on this carrier precisely when the
normalization Cartier relation lattice has a fully positive vector
whose off-`C` conductor unit class is torsion.

Proof of necessity. A descending section cutting `C` has a pullback
divisor with full support `W`; its coefficient vector lies in
`Lambda`, is positive on every `Gamma_j`, and has zero conductor
class. Therefore it lies in `Lambda_desc`.

Proof of sufficiency. Let `v` be such a vector. At every generic
conductor curve off `C`, some common positive power of `Q_v` lies
in `A_eta`, because `phi(v)` is torsion. At the generic point of `C`,
if it is itself a conductor curve, `Q_v` vanishes on **all** branches
above `C`. In the semilocal normalization, which is a product of
DVR localizations at those branches, a sufficiently large power
therefore belongs to the actual conductor ideal. Such a power
automatically belongs to `O_X,eta`. Take a common multiple large
enough for both requirements. The purity/depth argument in section
3 gives global descent to `L^(Nd)`. Its pullback still has full
support `W`; surjectivity of `nu` gives zero support exactly `C`.

If `X` is a degree-`a` hypersurface in `P^3` and `L=O_X(1)`, every
descending section of `O_X(b)` lifts to an ambient degree-`b` form,
since `H^1(P^3,O(b-a))=0`. Thus this criterion is exactly a criterion
for an ambient STCI mate **on the chosen carrier**.

The theorem retains both kinds of conductor behavior. On components
lying over `C`, vanishing enters the conductor after a large power.
On components away from `C`, unit descent is precisely a torsion
condition. For characteristic zero, Theorem 1 separates the latter
condition into residual finite phases and the vanishing of the
nilpotent logarithmic defect. No local class at a closed point is
silently discarded: the original section already exists everywhere
on `S`, and Cohen--Macaulayness forces generic actual membership to
extend everywhere on `X`.

## 5. Finite lattice reduction, rather than separate mate degrees

The group `Lambda` is a subgroup of a finite-rank free abelian group,
so it is a finite-rank lattice. Since `G/Tor(G)` is torsion-free,
`Lambda_desc` is a **saturated sublattice of Lambda**. Saturation here
is relative to `Lambda`, not necessarily to the ambient
`Z^(s+1)`; torsion divisor classes can make the latter distinction
substantive.

The semigroup

```
M = Lambda_desc intersect N^(s+1)
```

has a finite Hilbert basis. To see finiteness directly, its cone is
the intersection of a rational linear subspace with the nonnegative
orthant. Triangulate that rational polyhedral cone into finitely many
cones with integral ray generators. In each cone, remove integer
multiples of those generators from a lattice point. What remains is
a lattice point in a bounded fundamental parallelepiped, of which
there are finitely many. These points and the ray generators generate
`M`. Passing to a minimal generating set gives a finite Hilbert basis.

Let its nonzero members be `h_1,...,h_q`. Then Theorem 2 has the
finite equivalent test:

```
for each Gamma_j, some h_i has positive j-th coefficient.
```

Indeed a fully positive vector decomposes into Hilbert basis members,
so the supports of those members cover all `Gamma_j`. Conversely the
sum of a support-covering subset of the basis is fully positive.

For **existence alone**, a full Hilbert basis is unnecessary. The
rational cone
`(Lambda_desc tensor R) intersect R_>=0^(s+1)` has finitely many
extreme rays. Choose an integral lattice vector on each ray. A
full-support vector exists exactly when the union of their curve
supports covers all branches; a support-covering sum constructs it.
Thus computation of the rational cone and its extreme rays can be
the first finite target, reserving a Hilbert basis for finer degree
or multiplicity questions.

**Do not claim that each Hilbert basis member is itself a mate.** A
member can omit some branches above `C`; at the generic point of `C`
it may then have a mixture of zero and nonzero branch residues, which
no power can descend. The support-covering sum removes that problem.

There is also a fixed-data power bound. The torsion group
`phi(Lambda_desc)` is finitely generated, hence finite. Denote its
exponent by `E_{X,C,L}`. For every normalization branch above `C`
on which the conductor has positive valuation, write

```
c_j = ord_{Gamma_j}(I O_S),
c_max = max(1, all these c_j).
```

Any fully positive vector has `n_j>=1`, so every power exponent
divisible by `E_{X,C,L}` and at least `c_max` descends. In particular
the single common choice

```
N_{X,C,L} = E_{X,C,L} ceil(c_max/E_{X,C,L})
```

works for every fully supported vector in `Lambda_desc`. For a
particular vector one can improve `c_max` to
`max(1, ceil(c_j/n_j))`.

If `v_0` is a support-covering sum of Hilbert basis members, this
constructs a mate of degree at most `N_{X,C,L} d(v_0)` in the
hypersurface case. This bound depends on the fixed carrier, curve
and polarization. Split phases can have unbounded orders as these
data vary. Moreover **abstract finite generation is not an effective
algorithm**: computing `Cl(S)`, the relation lattice, and the integer
relations among the conductor-unit images remains substantial work.

The conceptual gain is exact: all mate degrees on a fixed carrier
are governed by one lattice and one homomorphism, rather than by a
new calculation for each degree. Non-torsion conductor classes cut
the lattice; finite conductor phases determine only the final power.

## 6. Primitive Cartier rays and a carrier-degree-independent bound

Let `v=(n_1,...,n_s,d)` be a primitive positive integer vector in the
ambient lattice, so `gcd(n_1,...,n_s,d)=1`. Put

```
Delta_v = sum n_j[Gamma_j] - d[H] in Cl(S).
```

The ray generated by `v` contains a Cartier relation if and only if
`Delta_v` is torsion. If its order is `t`, then `t v` is the first
Cartier relation on that ray. The associated primitive Cartier
section has degree `t d`. A mate along this ray exists if and only if
`phi(t v)` is torsion; its actual descending power is then governed
by sections 1--5.

This separates two different torsion orders: the class-group order
needed to **produce** an upstairs section, and the conductor-unit
order needed to **descend** it. An existing mate does not justify
dividing its divisor by the gcd without keeping the first order.

There is a useful uniform upstairs consequence when there is only
one curve `Gamma` in `W`. Write

```
a = H^2,  c = H.Gamma,  g = gcd(a,c).
```

Any mate has divisor `n Gamma` linearly equivalent to `d H`, so
intersection with `H` forces `n c=d a`. The primitive ray is therefore

```
(n_0,d_0) = (a/g,c/g).
```

If `Cl(S)` is torsion-free, existence of any mate implies

```
(a/g)[Gamma] = (c/g)[H]
```

already. It supplies a base section `Q` of degree

```
d_0 = c/g <= c,
```

**independent of the carrier degree**. The full mate problem along
this unique ray is then one conductor torsion problem for `Q`.

For a hypersurface carrier generically regular along a degree-`e`
curve `C`, the unique branch maps birationally to `C`, so `c=e` and
`a=deg(X)`. Thus, assuming the full inverse image has only this branch
and `Cl(S)` is torsion-free, an upstairs base section has degree

```
e/gcd(deg(X),e) <= e.
```

A smooth rational normalization has torsion-free Picard group and
`Cl(S)=Pic(S)`, so belongs to this scope. For `C0` of degree four,
the possible base degrees on **all** such carriers are `1,2,4`.
This does not bound the carrier degree or the descending mate degree,
and it does not cover multiple normalization branches or torsion
class groups. It nevertheless replaces separate upstairs mate-degree
searches across an entire normalization class by finitely many base
degrees.

There is an **exact minimum-degree formula** in the same one-branch
situation when `X` is generically regular along `C`. Let `t` be the
order of the primitive class

```
Delta_0 = (a/g)[Gamma] - (c/g)[H],
```

with `t=infinity` if it is not torsion. If `t` is finite, let `Q`
be the section associated to `t(a/g,c/g)` and put

```
E = order(phi(t(a/g,c/g))),
```

again allowing infinity. There is no generic conductor component
equal to `C`, so there is no additional vanishing threshold there.
A mate exists if and only if **both `t` and `E` are finite**. If so,
the possible mate degrees on this carrier are exactly

```
k t E (c/g),   k=1,2,3,... .
```

To prove exactness, every relation lies on the intersection-determined
ray. The class order forces its ray coefficient to be divisible by
`t`; its upstairs section is then a scalar multiple of a power of
`Q`. Actual conductor descent forces that power to be divisible by
`E`, and sufficiency follows from generic-to-global descent.
For torsion-free `Cl(S)`, `t=1`; for a hypersurface and `c=deg(C)`,
the minimum degree is exactly

```
E deg(C)/gcd(deg(X),deg(C)).
```

This identifies the full sequence of mate degrees with two torsion
orders rather than with a sequence of independent degree problems.

## 7. APic interface and the thick-carrier boundary

The conductor unit quotient used here is the generic-point version
of the standard quotient sheaf
`nu_*O_S^*/O_X^*`. Its identification with the quotient of the full
conductor unit sheaves is precisely the interface developed in
Hartshorne--Polini, Proposition 2.6; their Sections 3--4 relate these
data to Picard and almost-Picard groups. Their Proposition 7.1
expresses the chosen-carrier STCI condition by a relation between
`C` and the hyperplane class in APic when `C` meets the singular locus
only finitely. See the primary source
[*Divisors class groups of singular surfaces*](https://arxiv.org/html/1301.3222).

An almost-Cartier divisor is locally principal outside codimension
two. When `C` lies in the codimension-one singular locus, its reduced
ideal need not be almost Cartier. Writing `[C] in APic(X)` in that
case requires a separate proof. The normalization relation lattice
and full conductor-unit map in Theorem 2 make no such assumption.
They retain the multiplicities of all branches and apply directly
to the section of a hypothetical Cartier mate.

Accordingly the class-group ray and conductor torsion tests are a
precise replacement for an unjustified single reduced-curve APic
class in the entirely thick situation. Computing them remains the
central task.

## 8. Positive characteristic comparison

The local nilpotent distinction changes in characteristic `p>0`.
If `N_B^(p^h)=0` and the residual class of a unit `u` has order `e`,
choose `a in A^*` lifting its common residual `e`-th power. Then

```
(u^e/a)^(p^h)=1,
u^(e p^h)=a^(p^h) in A.
```

Hence in positive characteristic a given unit eventually descends
**if and only if its residual class is torsion**. Nilpotents can add
`p`-powers but cannot supply the characteristic-zero infinite-order
logarithmic obstruction. The lattice criterion of Theorem 2 still
holds; this observation simplifies its local unit map. It does not
make nonconstant residual ratios automatically torsion over function
fields, and it does not prove the universal STCI statement.

## 9. Audit record and next mathematical target

The independent `split_unit_audit` checked Theorem 1, the residual
torsion versus a given lift distinction, the logarithmic defect, the
common Kummer extension, and the exact split exponent. Its useful
messages were received before a transport interruption; the root
proofs above preserve their content. The independent
`cartier_lattice_audit` checked generic-to-global sufficiency and
flagged two scope improvements adopted here: the lattice theorem
works in arbitrary characteristic, and its finite Hilbert-basis
existence is not an effective algorithm. Its primitive-ray check is
complete: it independently confirmed the torsion-free class-group
bound and the exact one-branch arithmetic progression of mate
degrees. A separate combinatorial/APic check through that auditor
also confirmed the finite support-covering argument and the APic
scope. These audits concern the new theorem rather than a rerun of
accepted repository computations.

The highest-value next target is to compute one **carrier-class
relation/descent map**, using the accepted normalization and full
conductor data already in the repository. For smooth rational
normalizations generically regular along `C0`, start with base degrees
`1,2,4`, rather than arbitrary mate degrees. For thick carriers,
compute all branch classes and the map `phi`; then determine whether
the descent cone has full support. The irreducible global gaps are:

* classification or degree control of all possible integral carriers;
* class-group and branch-lattice control when the normalization is
  nonrational, singular, or has multiple branches over `C`;
* actual non-torsion conductor-unit relations, especially for split
  components off `C`;
* simultaneous compatibility with the separately developed thick
  valuation/Rees constraints.

No fixed-carrier finite reduction is a theorem that every possible
carrier has been covered. No field-degree bound eliminates split
phases, and no reduced conductor computation certifies the
characteristic-zero nilpotent defect.


---

## Source: 2026-10-13-generalization-frontier-map.md

# Frontier reconciliation and mechanisms beyond individual degrees

Date: 2026-10-13, continued 2026-10-14, America/New_York. Lane: `frontier_reconcile`.
Status: **HISTORICAL REPOSITORY RECONCILIATION AND RESEARCH ROUTING**. The branch tips and active-frontier descriptions below are October 13 snapshots; use [current state](../STATE.md), [current frontier](../FRONTIER.md), and [canonical results](../results/INDEX.md) for present claims. This note remains provenance, not independent theorem authority. Accepted mathematics
is taken as correct at the user's direction. No inherited verifier was run,
no remote source was fetched again, and no canonical or frozen proof was
edited. The current team's subsequent acceptance record controls promotion
of the new evening results listed below.

The universal integral-projective-curve STCI problem and the unrestricted
characteristic-zero problem for
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. The accepted all-quartic theorem
forces both defining degrees for this literal C0 to be at least five. The
newest completed independent cubic-pair audit closes one additional entire
quintic lane. None of these results bounds the minimum carrier degree of an
arbitrary hypothetical presentation.

## 1. Authority and complete branch coverage

The existing [evening branch inventory](#source-2026-10-13-evening-branch-frontier-auditmd)
already provides complete local/cached/live coverage and exact SHAs. Its
saved [manifest](../validation/2026-10-13-evening-branch-inventory/snapshot-manifest.json)
binds 25 recovered sources to their branches and Git blobs. That inventory
was reused; this lane did not repeat enumeration or mathematical checks.

| Branch or record | Current mathematical use | Treatment of older open labels |
|---|---|---|
| `research/ultra-resume-2026-10-06`, HEAD `b16e4322c7b955147ce2ed241a1a0316a8e1a67a` | Current checkout; October 11 all-quartic and October 12 nonendpoint acceptances, plus October 13 completed/new work | Latest acceptance and completed independent audits control |
| Live `main`, `7662a2ebb1dd561c1fb5e3c8958799b37d962c41` | Recovered jet supplement and synthesis sources | Its STATE/FRONTIER still list MF6 `(4,5)` and normal-quartic remainder as open; superseded here |
| `research/e1-jet-rebuild-2026-10-07`, `d5bed93e8c1ea09c2e11f0e096085da641819080` | Intrinsic residual `R/2R` maps and actual ambient lifting restrictions; corrected failed shortcut | Actual quartic mate searches superseded by all-quartic theorem; ancestor questions remain distinct |
| `research/jet-discrepancy-order-one-2026-10-06`, `f512d4d28da1fd6700aa4e6d2396229712d133d0` | General discrepancy/jet framework and conormal comparison geometry | Its old quartic mate obligations are closed; structural maps remain usable |
| `research/normal-rational-carrier-classification`, `4b936074f68038cfaa7ec51f5a960f23289627cd` | Resolution warnings, actual branch positions and corrected lattice calculations | No surviving normal-quartic mate lane; no reason to repeat Type-D quartic classification |
| `research/entirely-thick-rees-valuation`, `a843888ce15b06247c576f8f717bec6b7ef5a352` | Eighteen recovered notes on full clusters, Rees valuations, saturation, marked roots and normalization | Still structurally relevant; recovered owner claims are not silently upgraded to independent audits |
| `ultra_mode` / local archive, `2e53a7b5e9d4c96b5741ee4a4746a4a9ff0ad647` | Failure history and historical source preservation | Invalid generator-coordinate parity/seed certificates remain invalid; interrupted scratch is not a new frontier |
| Cached `research/consolidate-2026-10-06`, `research/local-audit-e2` | Historical branches assessed in inventory; latter has one missing output path | They are absent from live enumeration; no mathematical coverage gap justifies rereading all old work |

One local worktree, no tags and no stashes were observed by the saved
inventory. Its initially clean working tree observation predates evening
writes. Live remote-main authority wording does not supersede this
checkout's later mathematical acceptance record. No merge is needed to use
the preserved structural leads.

## 2. Compact mathematical evidence matrix

`ACCEPTED` below means the existing proof and its independent audit are
already authoritative premises. `NEW EXACT / REVIEW PENDING` means a new
calculation or owner proof has evidence but still needs the current review;
it never asks for inherited mathematics to be reverified.

| Lane | Strongest current result and precise scope | Live obligation |
|---|---|---|
| Universal question; unrestricted fixed C0 in characteristic zero | **OPEN**. The [October 13 literature refresh](#source-2026-10-13-evening-literature-refreshmd) found no accepted unrestricted resolution in its inspected primary sources | No general positive theorem, characteristic-zero counterexample or all-carrier obstruction |
| Positive characteristic | **ACCEPTED** restricted constructions, including this monomial C0 and the audited cuspidal-projection hypotheses; literature scopes remain as recorded | Do not infer a theorem for every integral projective curve from monomial/cuspidal families |
| Actual carriers of degree at most four | **ACCEPTED** [all-quartic assembly](OCT11_QUARTIC_DEPENDENCIES_AND_DP5_ENDPOINTS.md#source-2026-10-11-session-all-quartic-results-acceptancemd), with the earlier cubic/quadric exclusions and factor reduction | Closed as STCI mate lanes, including MF6, early defects, normal quartics, every nonnormal normalization genus and full conductor degenerations |
| Quintic structural frontier | **ACCEPTED** rationality through sectional genus three; genus zero excluded; Gorenstein nonnormal mate lane forced to degree-five ADE del Pezzo normalization with one A4 point | Normal quintics and other nonnormal genera remain open; Cartier index divisible by five is a necessary restriction, not exclusion |
| Genus-one quintic intrinsic endpoint projection | **ACCEPTED** all lift parameters and every positive mate power excluded | Closed; do not transfer its endpoint factorization into the genuine nonendpoint separation modulus |
| Genus-one quintic nonendpoint, homogeneous gcd degree zero | **ACCEPTED** all-mate exclusion for every admissible coprime corrected conormal pair | Closed. Both `Jbar!=0` local-isomorphism and `Jbar=0` full conductor-phase alternatives are accepted |
| Nonendpoint `G=Jbar=0`; entire-line rank-one; equal lifts | **ACCEPTED** stated entire subfamilies have no mate in any degree | Closed within exact scopes; entire-line power exclusion need not prove SUP failure |
| Nonendpoint residual partitions `2+2+2`, `2+4` | **ACCEPTED** exhaustive no-mate results, retaining repeated primes, all target endpoint/degree-drop strata and actual higher jets | Closed |
| Nonendpoint residual partition `3+3` | **COMPLETED INDEPENDENT AUDIT** [full October 13 audit](2026-10-13-session-nonendpoint-cubic-pair-full-independent-audit.md): entire all-mate exclusion, including a doubled residual cubic | Closed after root acceptance. SUP fails by the contact argument only when `Jbar!=0`; at `Jbar=0`, use separate all-power obstruction |
| Nonendpoint integral residual | **ACCEPTED REDUCTION**: arithmetic genus one source, birational target arithmetic genus three, exact excess contact length eight, including affine singular source cases | Complete support/higher-contact/conductor incidence remains open; exact total excess does not bound individual contact |
| Actual conductor quadric and binary octic | **ACCEPTED** whole conductor ideal upstairs, nonzero homogeneous degree-eight restriction, all pivot/rank alternatives; mate requires `Fdet | (H P^epsilon)^8` | This is necessary, not sufficient for full inverse support or actual power descent |
| Nonendpoint homogeneous gcd degree two/three | **COMPLETED INDEPENDENT ALGEBRA AUDIT** [rank and complete cover](2026-10-13-session-nonendpoint-homogeneous-gcd-rank-and-cover-independent-audit.md) | Cover classifies corrected first symbols only. Actual centers, higher contacts and conductor descent remain separate |
| Nonendpoint sole-common-root Taylor incidence | **NEW EXACT / REVIEW PENDING** eight Taylor coefficients; target-zero simple conductor zero; actual quotient-fiber L1/L2 separation | Review only the new incidence/branch proof and its connection to sole-root support; singular denominator charts and L2 remain active |
| Regular L1 rational branch | **NEW EXACT / REVIEW PENDING** [exact double-root identity](NONENDPOINT_SINGLE_ROOT_INCIDENCE.md) with retained factors `q(q-1)(q-2)(q^2-6q+6)!=0` | Its all-mate consequence also needs the quotient-fiber necessity of the rational family and a sole-common-root hypothesis |
| Nonendpoint h3 zero-P/zero-J charts | **NEW EXACT / REVIEW PENDING** actual cubic-times-quintic conductor factorization, original remainder-coefficient Bezout product one and homogeneous chart reversal | New written geometric proof/review required; recorded exact package is under `2026-10-13-h3-zero-chart-conductor-new/` |
| Nonendpoint h3 proportional ratio `lambda=1` | **NEW EXACT / REVIEW PENDING** compact actual-conductor support Bezout, including leading drop and the added A4 support root | New written homogeneous support proof/review required; generic-gcd evidence alone is not the proof |
| Remaining main h3 | **OPEN** two-parameter proportional family with `lambda!=0,1` and `Jbar!=0` | Solve homogeneous `S5 | H3^5`, retaining leading drops. The other `Jbar=0` factors imply the already excluded `G=Jbar=0` locus |
| Common-quartic-ancestor incidence | **ACCEPTED** actual 74-by-18 multiplication tensor, accepted principal/degree-one and stated other exclusions | Ancestor identities are distinct from actual quartic STCI mates; full incidence remains open |
| Second endpoint ancestor family | **ACCEPTED** generic and quadratic exception exclusions; **NEW EXACT / REVIEW PENDING** cubic/quartic factors exclude seven further geometric points with every affine lower lift | Degree-15 factor remains open. If new f3/f4 results are accepted, retained finite locus changes from 22 to 15 points |
| Ancestor boundary families `p(0)=0` | **NEW EXACT OUTPUTS / REVIEW PENDING** generic cleared-dual files and boundary-four field outputs | No accepted boundary closure yet; boundary-three degree-103 cleared target still needs exceptional analysis; boundary-four needs full primitive/excluded-root accounting and saved independent identity verification |
| Nonendpoint ancestor top zeros and positive-D2 directions | **OPEN** within recorded scope | Retain full tensor target incidence, every rank jump and denominators/infinity; no blanket closure from adjacent endpoint family |
| Totally ramified split-sextic `[2,2]` | **ACCEPTED REDUCTION**, actual carrier degree six and mate scale `8k` | Actual full conductor and filtered higher jets remain open; all-quartic theorem does not close this lane |
| Entirely thick pairs | **ACCEPTED** first blowup cycle/Noether budget and failure shields; **NEW OWNER THEOREM / REVIEW PENDING** all-normal-layer socle budget | No uniform degree/Loewy bound or entirely-thick exclusion; equality filtered deformation and positive-defect generation remain active |
| General single-field conductor power compression | **NEW OWNER THEOREM / REVIEW PENDING** characteristic-zero full Artinian membership compresses to field degree, then global surface descent | Primitive Cartier section degree and uncontrolled split phases are not supplied by this theorem |
| Smooth-normalization singleton rational lane, every carrier degree | **NEW THEOREM / COMPLETED INDEPENDENT AUDIT** [all-degree classification](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-smooth-normalization-independent-auditmd) forces a minimal-degree polarized `(S,c)`; fixed C0 has only higher models `a=8,P1xP1,H=(2,2),c=(1,1)` and `a=16,P2,H=4h,c=line` | Actual projections and full conductor descent remain open. Smooth normalization and singleton isomorphic lift are hypotheses, not guaranteed properties of a minimum carrier |
| Cartier-normalization-lift singleton rational lane, every carrier degree | **NEW EXTENSION / COMPLETED INDEPENDENT AUDIT** [singular extension](2026-10-14-generalization-cartier-lift-independent-audit.md) permits exactly one extra fixed-C0 model: degree-eight quadric-cone normalization, c a Cartier conic, H=2c | Three actual projection targets remain; non-Cartier lifts and several or nonisomorphic inverse curves remain outside |
| Cartier curve downstairs on an integral carrier, every characteristic | **NEW COROLLARY / INDEPENDENTLY DERIVED IN THE EXTENSION AUDIT** forces normal X, `a divides d^2`, `2g-2=d^2/a+(a-4)d`, and `a<4+(2g-2)/d` | Every smooth rational d>=3 is non-Cartier downstairs on every mate-admitting integral carrier; this does not exclude Cartier lifts upstairs on nonnormal X |

The h3 current-work status above incorporates the owning continuation lane's
report; it is not an independent mathematical judgment by this reconciliation
lane. Likewise raw boundary-four M2 outputs `|1|` do not by themselves
establish complete geometric coverage or acceptance.

## 3. Outdated canonical labels requiring a root integration

The following changes are status reconciliation, not new proof obligations:

1. README, the latest-frontier paragraph of
   `AUDITED_STATE_2026-10-07.md`, the opening and priorities of
   `SUCCESSOR_HANDOFF_2026-10-07.md`, and section 5 of the October 12
   acceptance still call the frozen `3+3` proof under review. The completed
   October 13 full independent audit supersedes that label.
2. The standalone [scope qualification](2026-10-13-session-cubic-pair-theorem-scope-qualification.md)
   still says its independent audit is pending. Its correction was explicitly
   incorporated in the full audit. Preserve frozen owner/proof bytes and
   retain the qualified theorem; only continuation labels should change.
3. A later paragraph in the canonical audited state still calls the
   pole/line mathematical audit outstanding. Section 2 of the October 12
   acceptance already accepts that independent audit.
4. Canonical ancestor summaries still retain 22 second-family points. This
   is the last **accepted** number. The evening exact f3/f4 results reduce
   the candidate count to 15 only after their new review/acceptance. No
   inherited generic/quadratic calculation needs rerunning.
5. Canonical handoff priority 1 still asks to audit the direct nonendpoint
   pole/line proof. That task is completed. The remaining work concerns the
   actual common-root/octic incidence, integral residual, h1/h2 and main h3.

Older body sections preserve historical open labels after explicit
superseding paragraphs. Do not silently reinterpret those historical labels
as present obligations or rewrite seal-bound historical notes.

## 4. General mechanisms already suggested by the proofs

These mechanisms identify reusable mathematics and the precise missing
bridge. They do not claim that every carrier satisfies the necessary
hypotheses.

| General mechanism | Accepted inputs or new theorem to review | What would advance the unrestricted problem |
|---|---|---|
| Full inverse support + conormal surjectivity forces local ring equality | Accepted finite Nakayama arguments in coprime quintic lane; full fibers retain isolated extra points | A degree-free way to prove surjectivity or quantify its actual exceptional scheme, then a positive conductor restriction contradiction |
| Ample rational Cartier lift forces a minimal-degree polarization | New smooth-normalization classification has completed independent audit, including all Picard divisibilities | On fixed C0 analyze two remaining smooth normalization models across all mate degrees; singular normalizations and multiple lift primes need a separate reduction |
| Cartierness downstairs bounds carrier degree independently of mate | New arbitrary-characteristic normality and adjunction corollary | Focus unbounded carrier work on actual non-Cartier singularities; upstairs Cartier-lift projections still require full conductor analysis |
| Restricted conductor support converts all mate degrees to finite contact geometry | Accepted homogeneous octic and full cubic/heptic contact proofs | Build the actual conductor restriction on broader normalization classes and prove a uniform support obstruction; first symbols locate exceptional support but never cap its contact multiplicity |
| Primitive Cartier divisor ray + complete conductor descent compresses mate powers | Accepted Picard/lattice compression in closed lanes; new general single-field Artinian theorem | Bound primitive upstairs section degree and reduced field degrees geometrically, and exclude or control split phase groups |
| Socle line + every conormal layer records the whole thickening | New [socle budget](#source-2026-10-13-evening-entirely-thick-rees-progressmd): `n(lambda*d-L)=lambda*Asym+2*Delta` | Derive an upper bound on actual Loewy index or positive global defect from ambient homogeneous generation, or contradict the constant Gorenstein graded algebra at equality |
| Global ribbon/conormal obstruction after compression | Accepted balanced `O(-7)^2` normal bundle and global Cartier-double/ribbon argument | Generalize to support curves with controlled normal slopes and actual low-degree Cartier multiples; do not assume normalization sections already descend |
| Polynomial left duals exclude whole parameter/lift fibers | Accepted actual tensor and affine lift coverage; new f3/f4 polynomial duals | Turn families into a projective parameter/module theorem that includes every denominator/rank stratum and scales to higher ancestors |
| Full Rees/colon/cluster data couples generic and special behavior | Recovered relative-blowup and saturation framework, with accepted higher-jet failure shields | Supply actual marked-point coupling beyond distinct-root counts; generic exceptional coefficient is not special root multiplicity |

The shared structure is a global-to-local obstruction chain: a hypothetical
complete intersection gives a positive Cartier/hyperplane relation and full
inverse support; the complete conductor or complete normal filtration then
measures the obstruction to realizing that relation. The accepted proofs
have progressed by making those measurements exact. Their reuse is more
promising than asserting that a low-degree carrier must exist without a
reduction theorem.

There are two distinct unbounded quantities to control: the primitive
upstairs divisor/section degree and the filtered nilpotent/Loewy complexity.
Single-field power compression addresses mate exponent only after fixing
the first; the socle budget constrains the second without bounding it.
A general theorem joining the divisor ray, actual conductor and global
normal algebra would address a broader class of degrees at once.

## 5. New-review queue and continuation order

Do not redo accepted all-quartic, endpoint, coprime, pole/line, residual
factor/genus, 2+4, actual conductor-module or homogeneous gcd-cover audits.
Read the completed full cubic-pair audit once for root acceptance; its
source scopes and qualification are already written.

The actual new review queue is:

1. General Artinian/surface conductor power-compression theorem, including
   its CM/purity transfer and the essential single-field hypothesis.
2. Full conormal-filtration socle theorem, nonhomogeneous Gorenstein
   first-moment inequality and equality rigidity; filtered equality
   extension arguments remain separate proposed work.
3. New exact ancestor f3/f4 certificates and stated all-lift/primitive
   coverage. A degree-15 certificate, if obtained, is a new task rather
   than a replay of quadratic exceptions.
4. New h3 zero-chart and `lambda=1` all-support proofs, plus the sole-root
   Taylor/quotient/L1 branch linkage. Retain L2, singular rank charts,
   homogeneous infinity roots and leading-degree drops.
5. Boundary-three/four ancestor certificates with complete exceptional
   coverage; saved outputs alone do not close these families.

While those reviews proceed, independent research can target the general
compression/socle interface, primitive degree and split-conductor phases;
the actual main h3/h1/h2 incidence; and equality filtered deformations.
This preserves the ongoing quintic and finite-incidence work while making
the main research direction increasingly independent of individual degree
pairs.

## 6. Provenance

This map uses current accepted notes, completed October 13 audit and
preserved evening source files as records, not as material to rerun. The
all-branch evidence is reused from the saved inventory. Direct owner-lane
reports clarified active h3 and localcohomology statuses; they are disclosed
above and require the new mathematical reviews before promotion.

Memory was used only for routing and the distinction between proofs,
certificates and unresolved strata: `MEMORY.md`, lines 65--68 and 80--82.
Current repository acceptances replaced its October 6 degree-specific
frontier. Corresponding memory rollout id:
`01a1125c-059b-78a0-a6d5-4bd27bfa1684`.


---

## Source: 2026-10-13-generalization-global-carrier-framework.md

# Degree-free carrier framework and the smooth-normalization classification

Date: 2026-10-13 evening, continued 2026-10-14. Owner:
`global_structure`. Status: **NEW WRITTEN PROOFS; independent review
requested**. Accepted repository results are premises; no inherited
proof or computation was rerun. This note makes no novelty claim and
does not resolve either unrestricted STCI question.

## 1. Accepted inputs and the reason to change the organization

The controlling inputs are the [all-quartic acceptance](OCT11_QUARTIC_DEPENDENCIES_AND_DP5_ENDPOINTS.md#source-2026-10-11-session-all-quartic-results-acceptancemd),
[quintic structural frontier](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-quintic-structural-frontiermd),
and the current [all-branch inventory](#source-2026-10-13-evening-branch-frontier-auditmd).
The all-quartic theorem excludes every integral quartic carrier of the
literal fixed `C0=[s^4:s^3t:st^3:t^4]` in characteristic zero, with
arbitrary mate degree. It does not force an arbitrary STCI presentation
to have a quartic carrier.

The reusable content of the accepted proofs is stronger than a collection
of degree exclusions. It is the combination of full inverse-image
support, a positive Cartier divisor on a ray in the normalization class
group, and descent through the entire conductor. The recovered thick
notes [normalization/APic bridge](../validation/2026-10-13-evening-branch-inventory/remote-snapshots/research_entirely-thick-rees-valuation/research/notes/2026-10-07-thick-apic-conductor-bridge.md)
and [generic normalization filter](../validation/2026-10-13-evening-branch-inventory/remote-snapshots/research_entirely-thick-rees-valuation/research/notes/2026-10-07-thick-generic-normalization-filter.md)
already preserve this organization and its unproved coverage boundary.
The new theorem below classifies an entire normalization lane in every
carrier degree.

## 2. The exact divisor ray on a singleton lift

Let `C` be a smooth integral curve of degree `d` and genus `g` in `P3`.
Let `X` be an integral degree-`a` hypersurface containing `C`, with finite
normalization `nu:S->X`, and put `H=nu*O_X(1)`; `H` is ample and
`H^2=a`. Assume

    (nu^{-1}(C))_red=c,  and  nu|c:c -> C is an isomorphism.       (2.1)

This is an explicit support and degree-one hypothesis. If `X` is
generically regular along `C` and has a mate, the accepted full-support
theorem implies (2.1): there is one dominating prime because normalization
is an isomorphism at the generic point, isolated inverse-image points
are prohibited by the mate, and a finite birational map to the normal
curve `C` is an isomorphism. Some nonregular unibranch carriers also
satisfy (2.1).

If a mate of degree `b` exists, its pullback has divisor `m c`, with

    m d=a b,   m c~b H,   c_num=(d/a)H,   c_num^2=d^2/a.          (2.2)

Here `c` is Q-Cartier because an actual positive multiple is Cartier;
the intersection numbers are therefore defined without any assumption
on the normalization singularity type.

Set `h=gcd(a,d)`, `u=a/h`, `v=d/h`, and

    D=u c-v H in Cl(S).                                        (2.3)

Every normalized mate has `m=u k,b=v k`. Its existence therefore forces
`D` to be torsion. Conversely, if `k D=0`, linear equivalence gives a
section of `O_S(v k H)` whose divisor is exactly `u k c`. This supplies
the required positive Cartier support upstairs. It supplies an ambient
mate exactly when this section descends through the full conductor.

For a normal carrier `X=S`, descent is automatic, so (under (2.1)) the
criterion `D is torsion` is necessary and sufficient. It is also necessary
and sufficient if all normalization defect is supported on `C`, by the
accepted [asymptotic conductor theorem](OCT6_SESSION_FRONTIERS_AND_VALIDATION.md#2026-10-06-session-conductor-support).
On a general nonnormal carrier, torsion upstairs leaves a real additional
descent obstruction. This exact distinction survives arbitrary degrees.

If `t c` is Cartier, restriction of its line bundle to the smooth `c`
gives the stronger elementary index condition

    a divides t d^2.                                          (2.4)

Indeed its restriction has integer degree `t c_num^2=t d^2/a`.
Using only the Cartier square would give the weaker condition
`a divides t^2 d^2`. If `z K_S` is Cartier, and `pi` is the sectional
genus of `(S,H)`, intersection with `c` similarly gives

    a divides z d(2 pi-a-2).                                  (2.5)

The sectional genus here is that of a general hyperplane pullback,
chosen to avoid the finitely many singular points of the normal surface.
Adjunction gives `K_S.H=2pi-a-2`; this numerical identity is defined
even if `K_S` itself is not Q-Cartier, by intersection with the Cartier
hyperplane divisor. Condition (2.5) is used only when the stated global
Cartier canonical multiple exists.

## 3. Smooth normalization of a rational curve: all degrees at once

**Theorem.** Work over an algebraically closed field of characteristic
zero. Let `C` be a smooth rational curve of degree `d`, and assume (2.1),
that `S` is smooth, and that `X` has a mate. Then the polarized pair
`(S,c)` is a smooth surface of minimal degree with `c` its hyperplane
section. More precisely, the complete possibilities are:

| Normalization and lifted curve | Hyperplane pullback `H` | Carrier degree `a` |
|---|---|---|
| `S=P2`, `c` a line | `O_P2(d)` | `d^2` |
| `S=P2`, `c` a smooth conic; `d` even | `O_P2(d/2)` | `d^2/4` |
| A smooth rational normal scroll of degree `n>=2`, `c` its hyperplane section; `n` divides `d` | `(d/n)c` | `d^2/n` |

The scroll entry means `S=F_e`, `c=E+t f`, with `E^2=-e`,
`t>e>=0`, `n=2t-e`, and the usual equality of the two rulings when
`e=0`. The scroll degree `n` is finite: it is a positive divisor of
`d`, not an independently unbounded carrier parameter.

**Proof.** Smoothness makes `c` Cartier. Equation (2.2) implies

    n=c^2=d^2/a is a positive integer.

It also makes `c` ample, since its numerical class is a positive multiple
of the ample `H`. Adjunction on the smooth rational `c` gives

    K_S.c=-n-2<0.

Thus `K_S.H<0`. No positive multiple of `K_S` is effective, and the
characteristic-zero classification makes `S` rational or birationally
ruled over a curve of positive genus. In the latter case the ruling
extends to a morphism from `S` after the point blowups from its minimal
ruled model. Any map `P1` to the positive-genus base is constant, so
`c` is contained in a fiber. A fiber component has self-intersection
at most zero: for the full effective fiber `F`, `F.c=0`, while the
other components meet `c` nonnegatively. This contradicts `c^2=n>0`.
Consequently `S` is rational, and `H^1(S,O_S)=0`.

The exact sequence

    0 -> O_S -> O_S(c) -> O_P1(n) -> 0

shows `h0(S,O_S(c))=n+2` and that restriction to `c` is surjective.
The canonical section is nonzero away from `c`, and the restricted
sections generate `O_P1(n)`, so `|c|` has no base point. Its morphism
`phi:S->P^(n+1)` is finite because `c` is ample. If `Y` is its image
and `e_phi` its generic degree, then

    n=e_phi deg(Y),   deg(Y)>=codim(Y)+1=n.

The image is nondegenerate because the complete system is used.
Therefore `e_phi=1` and `deg(Y)=n`. The Del Pezzo--Bertini classification
makes `Y` a minimal-degree surface: a plane, a rational normal scroll
(including cones), or the Veronese surface. These surfaces are normal.
Hence the finite birational map from normal `S` is an isomorphism.
Since `S` is smooth, the singular cones are excluded; the smooth
classification in the table follows.

On a smooth rational surface numerical and linear equivalence of
divisors agree. Thus `H=(d/n)c` in `Pic(S) tensor Q`. On a scroll the
coefficient of `E` in `c` is one, so integrality forces `n|d`. On `P2`
with a line this gives `H=d h`; with a conic it gives `H=(d/2)h` and
requires `d` even. The displayed carrier degrees follow by squaring.

The only newly consulted primary classification interface is
[Eisenbud--Green--Hulek--Popescu, *Small schemes and varieties of minimal degree*, introduction](https://arxiv.org/html/math/0404517v5),
which states the degree bound and Del Pezzo--Bertini classification.
The surface-classification and rational-surface Picard facts are the
same standard inputs already used in the accepted quartic/quintic
arguments. This proof does not use an unverified classification of
projections of these surfaces.

## 4. Fixed C0: only two higher smooth-normalization models remain

For `d=4`, the scroll divisors are `n=2,4`; the plane-conic entry also
has `n=4`. Thus all smooth-normalization carriers satisfying (2.1)
have degree `4,8,16`. The accepted degree-four theorem removes the
entire first degree, leaving exactly:

    a=8:  S=P1 x P1, c=(1,1), H=(2,2), pi=1;
    a=16: S=P2,       c=line,  H=4h,    pi=3.                  (4.1)

For the degree-two scroll, smoothness and ampleness force the smooth
quadric: `2t-e=2,t>e>=0` leaves `t=1,e=0`. The sectional genera in
(4.1) follow either from the polarization or from adjunction:

    2g-2=d(d+2pi-a-2)/a,
    for d=4,g=0: pi=(a-4)/4.                                (4.2)

These are necessary normalization/projection targets, not constructed
mate carriers. The original four ambient coordinates must be a
four-dimensional generating subspace of `H0(S,H)`, finite birational
onto its degree-8 or degree-16 image, restricting to the prescribed
deleted-middle-monomial quartic on `c`. Full inverse-image equality,
the actual conductor, and its entire power-descent equation remain
required. The dimensions of the complete systems are respectively
9 and 15. The finite target does not by itself bound all projections
or remove their split conductor phases.

Both entries have `H~q c` with `q=2,4`. Consequently the primitive
normalized section `Q` has degree one and divisor `q c`, and every
normalized mate of degree `b` is a scalar multiple of `Q^b`.
Under the separately audited [single-field conductor power-compression theorem](#source-2026-10-13-evening-general-conductor-power-compressionmd),
if no conductor prime is contained in `c` and every generic reduced
upstairs conductor algebra is one field of degree at most two, any
mate compresses to ambient degree two. This is excluded by the accepted
quadric theorem. More generally, residual degrees at most three
compress to degree six, a bounded remaining target; residual degrees
at most four compress to degree twelve. The exponent is the least
common multiple across field degrees, so one must not replace this
by their maximum.

If all actual generic residue degrees are exactly one, two, or four,
without a degree-three point, exponent four suffices; the accepted
all-quartic theorem then excludes the carrier. This is a conditional
coverage statement. Split residual products, conductor components
inside `c`, and larger degrees remain outside it. In particular,
ordinary projection heuristics are not a proof that every projection
has an integral double-cover conductor.

## 5. Normal carriers and the actual source of unboundedness

On a normal hypersurface, the exact criterion is torsion of (2.3).
The canonical index filter imposes no new restriction there:
`K_X=(a-4)H`, so `K_X.c=d(a-4)` is already integral. If a mate exists,
the curve's Cartier index is at least `a/gcd(a,d^2)` by (2.4).
This lower bound grows with `a`; it is not an upper degree bound.

For a rational singleton lift on a normal carrier whose singularities
along `c` are ADE, let `sigma:M->S` be its crepant resolution and
write the Mumford pullback `c_num=c# +Z`. The smooth strict transform
is rational and adjunction gives the uniform exact correction equation

    -Z^2=2+d(a-4)+d^2/a.                                    (5.1)

Indeed `c#^2=c_num^2+Z^2`, and `K_M.c#=K_S.c=d(a-4)`.
This is a necessary equation in the entire exceptional lattice.
It organizes every carrier degree by a local correction budget. The
exceptional lattice can itself grow with the carrier and is not
bounded by the accepted quartic proof. Without a new global bound or
geometric realization theorem, (5.1) does not exclude all `a`.
For noncrepant resolutions the discrepancy intersection must also
be retained; replacing it by zero would be invalid.

## 6. Minimum-carrier choice: what is justified

For an actual STCI pair with no common surface component, each
irreducible factor of either form is itself a carrier with the other
form as mate; this is the accepted positive-degree factor argument.
It is therefore legitimate to select an integral carrier of minimum
degree among all carriers that admit a mate for `C`.

This choice supplies neither generic regularity along `C` nor smooth
normalization nor the singleton degree-one lift (2.1). The fact that
there are smooth general surfaces containing `C` in sufficiently
large degree also supplies no mate on such a surface. Linear
combinations `G+F T` preserve a given pair when the degrees permit,
but can stay singular along `C` when both generators have generic
normal order at least two. Thus there is no presently justified
degree-lowering or smooth-normalization lemma for a minimum carrier.

The theorem in section 3 consequently reduces every smooth-normalization,
singleton degree-one rational lane at once, including thick carriers
when they satisfy those stated hypotheses. It leaves singular
normalizations, several inverse-image primes, and finite lifts of
degree greater than one as distinct global tasks. The accepted
quartic/quintic exclusions do not remove those tasks.

## 7. Continuation-ready program

The fastest general continuation now has specific targets:

1. Independently audit the proof of section 3 and route it as an all-degree
   normalization theorem if accepted. No old verifier rerun is needed.
2. On the two models (4.1), derive the entire conductor from the actual
   four-coordinate projection and either exclude split phase descent
   geometrically or apply a justified residual-field bound. This is a
   finite normalization-type problem across all mate degrees.
3. For singular normalizations, work with the primitive ray (2.3), the
   stronger Cartier index (2.4), and the full exceptional correction
   equation, rather than extrapolating a quartic first-jet proof.
4. For thick carriers with multiple primes above `C`, retain a positive
   coefficient vector on every prime and its Cartier/Picard compatibility.
   A singleton divisor-ray theorem cannot be substituted for that vector.
5. Seek a structural theorem about minimum mate-admitting carriers. The
   missing theorem must actually force bounded Cartier index, bounded
   normalization type, or a divisor-class obstruction across every
   allowed inverse-image vector. None of these is assumed established.

The companion [symbolic-ribbon generalization](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-ribbon-numerical-criterionmd)
develops a different reusable obstruction from the accepted ribbon
arguments. Its audit status must be checked before using it as a
premise. The root's new conductor power theorem is also a separate
dependency, not proved by this note.

No claim here proves that every integral projective curve is STCI,
or supplies a universal counterexample. The new content is a written
classification of an entire rational-curve normalization lane and an
exact framework that identifies why the remaining global degrees are
still unbounded.
