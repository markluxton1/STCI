# Historical mathematical investigations

Full original mathematical text follows. Preserve source-level evidence status, counterexamples, corrections and unresolved boundaries; no independent re-audit or result promotion.

---

## Source: 2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md

# Independent assembly audit: all integral quartic carriers of the fixed C0 are excluded

Date: 2026-10-11. Auditor: `oct11_quartic_assembly_audit`.
Status: **PROVED HERE / independent dependency and coverage audit PASS**,
under the explicitly recorded classical and independently accepted component
inputs. No canonical frontier file is edited by this note. The conclusion
is an all-quartic carrier theorem, not an unrestricted non-STCI theorem.

Work over an algebraically closed field of characteristic zero, with the
literal smooth rational quartic and its projective equivalents

    C0=[s^4:s^3 t:s t^3:t^4] subset P3.

**Audited assembled theorem.** If `F` is an irreducible homogeneous form of
degree four with `C0 subset V(F)`, no homogeneous form `G` of any positive
degree has `V(F,G)=C0` set-theoretically. The carrier can be normal or
nonnormal, its normalization can be singular, and the mate can have arbitrary
normal order or degree. No generic-smoothness, reduced-conductor, first-normal
ratio, clean-conductor, ordinary-singularity or displayed-family restriction
remains in this assembled statement.

## 1. Actual checkout and scope of this audit

The live checkout inspected here had HEAD
`2ba77d1a1177db9390693066c6b185040766c089`. The source notes and working-tree
canonical records were read rather than treating an older pause summary as
current evidence. The October 10 resumed
[acceptance](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-continuation-results-acceptancemd) already
accepts the bisection and nonendpoint section exclusions. Its remaining
endpoint label is its preserved earlier frontier. The subsequently saved
[full endpoint reduction](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-endpoint-full-quartic-reductionmd)
and [binding independent audit](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-endpoint-full-independent-auditmd)
supply the missing component checked in this assembly. Root acceptance and
canonical reconciliation remain distinct actions.

This audit verifies logical interfaces, full case coverage and the exact
degree consequence. It does not claim a fresh literature novelty result,
rerun every historical numerical enumeration, count copied verifier sources
as independent programs, or use parallel-agent agreement as proof. It read
the actual component proofs, including their hypotheses and rejected
shortcuts, and checked the decisive local and divisor calculations below.

## 2. The carrier classification has no omitted case

An integral quartic `X=V(F)` is either normal or nonnormal. In the normal
case a general plane section is a smooth genus-three curve and the separate
normal-carrier theorem applies. In the nonnormal case, finite normalization
`nu:S->X` has a general smooth integral pulled-back hyperplane curve of
genus `pi` in exactly `{0,1,2}`. The plane section has arithmetic genus
three, and the nonnormal codimension-one locus gives positive normalization
defect. A hypersurface is Cohen--Macaulay, so a nonnormal integral quartic
cannot hide only an isolated failure of normality outside this argument.

The normalization sectional genus is not the ambient plane quartic's
arithmetic genus and not the conductor degree. The following table is the
complete split used by the proof.

| Carrier or normalization lane | Complete exclusion used |
|---|---|
| Integral normal quartic | [Normal global audit](OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-normal-global-adversarialmd), including [nonreduced exceptional cycles](OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-normal-nonreduced-independent-auditmd) |
| Nonnormal, `pi=0` | [Minimal-degree classification and cone audit](OCT9_MF6_WEIGHTED_AND_QUADRATIC_DESCENT.md#source-2026-10-09-session-normalization-genus-zero-independent-auditmd), with the accepted entire F0/F2 scroll and Veronese projection proofs |
| Nonnormal, `pi=1` | [All genus-one interfaces](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-genus-one-interface-independent-auditmd) and [all repeated contact partitions](GENUS_ONE_RIBBON_PARTITION_INDEPENDENT_CERTIFICATES.md) |
| Nonnormal, `pi=2`, `lambda=0` | [Full second-pencil/Cartier-double/ribbon audit](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-genus-two-bisection-full-independent-auditmd) |
| Nonnormal, `pi=2`, `lambda=1`, three distinct contacts | [Full nonendpoint trisecant audit](OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-auditmd) |
| Nonnormal, `pi=2`, `lambda=1`, one triple contact | [Full endpoint audit](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-endpoint-full-independent-auditmd), including reversal of the endpoint |

There is no separate nonrational-normalization row: the
[ruled intersection audit](NONRATIONAL_QUARTIC_NORMALIZATION_PROOF.md)
proves that every nonnormal integral quartic containing a smooth rational
degree-four curve has rational normalization, without assuming a mate.
Its nef pushdown identity retains every infinitely near blowup:

    4=(2g-2)a^2+(6-2pi)a+sum m_i(a-m_i),   0<=m_i<=a.

For a nonrational ruling this forces `a<=2`, while the rational lifted
degree-four curve is a fiber component and forces `4<=a`. The contradiction
establishes rationality before either del Pezzo or conic-model reduction.

## 3. Generic regularity and full inverse support remove hidden hypotheses

The generic regularity of an integral quartic along C0 is automatic. If all
ambient partial derivatives vanished generically on C0, they would vanish
on it. A general integral plane quartic would then have its four distinct
transverse C0-intersection points singular. Its normalization defect would
be at least four, greater than arithmetic genus three. The
[genus-zero audit's addendum](OCT9_MF6_WEIGHTED_AND_QUADRATIC_DESCENT.md#source-2026-10-09-session-normalization-genus-zero-independent-auditmd)
proves this without a normality assumption. Consequently there is no extra
integral quartic lane singular at the generic point of C0.

Under a mate, the unique curve component `c` above C0 is a smooth embedded
copy of C0. A proper birational strict-transform map to this normal curve
is quasi-finite, hence finite and an isomorphism. Potential additional
isolated inverse-image points cannot simply be ignored. The actual nonzero
Cartier pullback of G on normal S has a pure one-dimensional zero scheme;
its zero support is the entire inverse image of C0. This rules out isolated
extra points and yields full support exactly c. Intersecting its Weil
divisor with H gives

    div_S(nu*G)=b c ~ bH,   H.c=H^2=4,   b=deg G.

Thus the coefficient is b even when the mate has higher generic normal
order. The smooth curve c need not be Cartier at a singular point of S;
the positive-genus arguments expressly retain that possibility.

The `pi=0` classification includes the singular rational-normal-quartic
cone, in addition to F0, F2 and the Veronese surface. The accepted entire
scroll proofs include nongorenstein and nonreduced conductor schemes. A
smooth-normalization theorem alone is therefore not being used to cover
all quartic normalizations.

## 4. The genus-one theorem is genuinely complete

The actual rational resolution has `K_M=-L`; S is the crepant degree-four
ADE del Pezzo model. The signed D5 saturation proof applies to the actual
exceptional lattice and actual smooth lift and gives genuine `2c~2H`.
The complete anticanonical map identifies this S with a normal integral
two-quadric intersection in P4 before any projection computation is used.
Restriction to c identifies the fifth coordinate with `s^2t^2`, so the
projection deletes precisely the middle coordinate of the complete rational
normal quartic. This establishes the fixed-center hypothesis for every
carrier in this lane; it does not posit that a displayed toric family is
exhaustive.

The actual Cartier double is a global CM ribbon, including all its ADE
points, with nilideal O(-6) and the complete kernel net `M(d) eta=0`.
The entire conductor algebra and singleton test give the necessary support
condition for the nonzero binary quartic L_C. Its five and only five
multiplicity partitions are

    [1,1,1,1], [2,1,1], [2,2], [3,1], [4].

The interface audit covers the first two with every direction and basepoint
chart; the independent repeated-partition audit covers the last three,
including the derivative-invisible quadric coefficient and every determinant
root. Its `[2,2]` final obstruction proves that no positive power of the
actual quadratic section descends, in both split and nonsplit conductor
algebras. No mate-degree bound remains. All reparametrizations used in the
fixed-center classification preserve that center; an arbitrary smooth
rational quartic projection is not substituted for the literal C0.

## 5. Both genus-two mate strata, and all trisecants, are covered

The [adjoint proof](OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-two-adjoint-independent-auditmd)
gives the complete connected basepoint-free conic pencil `f=K_M+L`, with
`K_M^2=0`. The [null-curve and correction proof](OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-two-nullcurve-mate-independent-auditmd)
classifies every exceptional prime as vertical (-2) or horizontal (-3),
with at most two disjoint horizontal sections. For the effective rational
actual correction Z it proves

    q=-Z^2>0,   lambda=K_M.Z in Z>=0,
    q+lambda=4,   lambda^2<=q.

Consequently the only mate strata are `(lambda,q)=(0,4)` and `(1,3)`.
The earlier shortcut `q=4` in every case is not used.

The [entire conductor proof](GENUS_TWO_ENTIRE_CONDUCTOR_PROOF.md)
establishes rational singularities of S and the actual reduced downstairs
conductor line, with no embedded or isolated components. Its upstairs
quadratic algebra retains split, singular and nonreduced covers. The
[normal ambient-model proof](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-blowup-lift-normality-independent-auditmd)
constructs the actual strict transform in the ambient line blowup and proves
its normal ADE property by proper trace, before invoking crepancy. It is T,
not the possibly non-Gorenstein S, which is asserted ADE. The pulled line
ideal is exactly O(-D_M), without a residual zero-dimensional base scheme.

In `lambda=0`, the second rational pencil produces an actual equality
`2Z=sum k_t F_t-2R`, with all entire fiber multiplicities and every one of
the four blowup centers retained. Thus `2Z` is integral exceptional and
`2c~2H` is an actual Cartier equivalence. Its full Cartier double is pure
CM with nilideal O(-8), as follows from `chi(O_S(mH))=2m^2+m+1`.
Normalization gives a nonzero global ambient conormal map to that nilideal.
The verified `N_C0/P3^*=O(-7)^2` forbids such a map. This covers bisecants,
tangents and all local-normalization singularities, without requiring Q to
be an ambient quadratic section.

In `lambda=1`, the actual line intersection has length three, so the line
lies on the unique smooth quadric q and belongs to its degree-three ruling.
The restriction is `t^3-a s^3`. In characteristic zero it has three distinct
roots for finite nonzero a, or one triple root for a=0 or infinity; reversal
exchanges the latter. These are all line positions.

The no-degree-zero-horizontal theorem forces the special prime B with
`c#.B=0`. The complete nonendpoint proof exhausts every (2,2) divisor
containing its Gamma fiber, including double B, reducible residuals, double
fixed fibers, and B with coefficient zero when another horizontal exists.
For integral residual, the two other contacts force its two branch values;
the branches cross B transversely and give actual endpoint A-chains. Their
all-length correction formula is strictly below the required coefficient
one. It never infers disjointness on T merely from disjointness on M.

For the endpoint, the full degree-four ideal identity gives the entire
eleven-dimensional carrier family `F=q Q+D L0`. The unique positive
horizontal correction must lie over the sole triple contact and has
coefficient one. The full endpoint proof then retains and excludes:

* a coefficient-zero special B with a second supporting horizontal prime,
  including the second Gamma fiber at infinity;
* two distinct residual crossings, including a crossing at infinity;
* the entire triple residual family, with its endpoint A-chain, exact
  internal A-chain attachment `2/(n+5)`, D4 distinct outer arms and
  incompatible multiplicity-three case;
* the doubled-horizontal divisor `2B+2F`, with all normal-coefficient roots
  on P1, repeated roots and arbitrary ADE blocks away from the contact.

In the last case the degree-three normal coefficient gives the exact
away-contact contribution `2 v^t Q^(-1) v=ord(h)`. The actual contact
equation gives total contribution at most 5/2, below the required three.
This is the calculation closing the potentially dangerous repeated scheme;
an assumed all-A-chain graph or an abstract D7 numerical example is not used
to assert realizability or exclusion. The [full endpoint binding audit](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-endpoint-full-independent-auditmd)
checks these actual family interfaces and local attachments. Reversal closes
the second endpoint. This exhausts `lambda=1` and hence the genus-two lane.

## 6. No circular small-degree or numerical input is hidden

The inherited normal-quartic proof uses the classical normal-quartic source
classification, Jaffe's rational-singularity and ADE-pair inputs, the audited
normal-bundle and normal-sheaf bounds, exact reduced/nonreduced necessary
graph enumerations, and prior mate exclusions through degree five. Those
prior exclusions were established before the present assembly: the plane
and quadric obstructions, classical cubic and (4,4) theorems, and repository
P-040 for (4,5). P-040 is independently proved from the multiplicity-five
Banică--Forster/Boratyński classification and P-025's complete chart cover;
it does not use this all-quartic conclusion. Thus the assembly has no
dependency loop through its own new theorem.

The two graph enumerations eliminate a necessary superset; they do not
claim every retained graph is geometrically realized. Their counts and
agreement are evidence for their explicitly proved enumeration scope.
The final Type-D step is the actual pulled maximal-ideal identity, forcing
passage coefficient one, contrary to the remaining coefficient-two rows.

For complex primary classification statements, the recorded finitely
generated coefficient-field transfer includes radical-equality witnesses,
geometric integrality and normality, so it applies to every algebraically
closed characteristic-zero field. No uncountability assumption is imported.

## 7. Degree consequence and remaining scope

For any homogeneous pair F,G with projective `V(F,G)=C0`, the forms are
coprime. Otherwise their common irreducible factor supplies a surface in
the intersection. If f is any nonconstant irreducible factor of F, then
`V(f,G)` is a nonempty pure one-dimensional complete intersection, since
f and G are coprime. It lies in the integral curve C0, so its support is
all of C0. Thus f is itself a carrier of a defining pair. The same applies
to every factor of G, or to any pair of factors f,g. Repetition changes
scheme multiplicity, not this support argument.

No degree-one factor can contain this nonplanar C0. Its only quadric is
`q=x0*x3-x1*x2`, and restrictions of ambient degree-b forms to q have class
(b,b), which cannot have full support a positive multiple of its curve
class (1,3). The verified Craighero--Gattazzo 1989 all-cubic theorem removes
every integral degree-three factor. The assembled theorem above removes
every integral degree-four factor. Therefore:

    Every irreducible factor of either defining form has degree at least 5.
    In particular, every STCI presentation of fixed C0 has min(deg F,deg G)>=5.

This conclusion includes reducible and repeated presentations. It does not
assert that degree five is attained or that a higher-degree pair exists.
The delegated [degree-factor microaudit](#source-2026-10-11-session-degree-factor-and-mf6-scope-auditmd)
separately inspected the actual [CG1989 primary PDF](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf),
printed pages 171--173: its base field is already algebraically closed of
characteristic zero, its mate has arbitrary degree, and its cubic carriers
are reduced irreducible. The factor lemma handles reducible or repeated
cubic forms. No extra complex-field descent is needed for this particular
cubic input.

Every actual quartic-plus-mate lane is now excluded, including all (4,6)
MF6 mate types and all early-defect quartic mate strata, whatever the extra
defect divisors, principal parameter roots or mate degree. Earlier finite
candidate loci cease to be open *mate existence* problems with an actual
quartic carrier. The theorem does not calculate their parameter sets.

In particular, all seven necessary MF6 numerical types close as actual
mate presentations:

| e | `(d2,d3)` |
|---:|---|
| 0 | `(1,8), (2,7), (3,6), (4,5)` |
| 1 | `(0,4), (1,3), (2,2)` |

All fifteen retained coarse nonregular pole strata likewise close as
actual (4,6) pairs; no unproved bijection between BF types and pole strata
is needed for that conclusion. The regular-ratio `(0,3,6)` subcase and
principal positive-D2 `(1,1,3)` and `(1,2,2)` cases are included.

Common-quartic-ancestor and local-cohomology incidences ask for containment
or simultaneous annihilation, not a two-form STCI radical equality. Their
22 retained endpoint-family roots, entire lift lines, principal necessary
at-most-630-point locus and other uncomputed incidences are not declared
empty by a no-mate theorem. They remain distinct algebraic questions or
possible information for higher-degree research. Entirely thick higher-degree
presentations and an integral split sextic with arbitrary higher-degree mate
also remain outside the all-quartic theorem. If such a sextic has an actual
quartic mate, that pair is excluded; a quartic ancestor alone does not imply
that hypothesis.

The retained split family `F_tau=-B^2+tau*q*K` has degree six, and its
necessary P-020 mate scale is `8k` with k positive. Thus it does not require
a quartic mate; its remaining totally ramified normalization and conductor
work retains its previous scope.

The unrestricted fixed-C0 STCI question, every general integral projective
curve and the universal question over arbitrary algebraically closed fields
remain **OPEN** in this record. No theorem forcing a quartic carrier in an
arbitrary presentation has been established. This audit finds no blocking
coverage gap in the stated all-quartic assembly, while preserving precisely
that larger unresolved scope.

## 8. Source bindings and verification attribution

At this audit the principal component source SHA-256 values were:

| Source | SHA-256 |
|---|---|
| Normal global audit | `cecccf902bfc8a63b70ebf28c1510c49b590c323c4c95be94fa86759425e2bff` |
| Normal nonreduced audit | `3fefd232c29931319eab3894ddb0f82659624a6b623449f163d5242ce8d80a50` |
| Genus-zero independent audit | `b4cc4bdb803e2bab5a66e4366cce5bb0a48521866ff6860a193d117e92c2ef7d` |
| Nonrational independent audit | `e2e24ac3524ef473f86d71d8465ed18987abc83ac6c20ac2630f85196a3908bb` |
| Genus-one interface audit | `96fa5d1f3d5f3de5ca51866d554039a8a19d8e759198e4fce8453c9358261561` |
| Repeated-partition audit | `a7ee3496fe5b3aaedae9b0a34abdfcbc63e6dfbda1d7993cc301d7cb23fc1cf1` |
| Full bisection audit | `5aa6eeedb31ff2fe316b706c3c0e86ff78d9beca01c9f92dfa5d7fafcc283133` |
| Full nonendpoint audit | `970e41c503d71402df22275308cf024b45191dc3fe1e371319285b9adac70395` |
| Full endpoint owner | `366c8396333118dabcaed6106fbc68fdaf0851d1005bf5c5d3511d46c77cc5c9` |
| Full endpoint independent audit | `d4253e444643c2201e49de9dd20545bb6aff993123d303a75c286f8758d4c37c` |

This audit also inspected the existing isolated root manifests for the
[genus-one 42/29-identity replays](../validation/2026-10-10-genus-one-root-replay/execution-manifest.json),
[8-condition normal-bundle replay](../validation/2026-10-10-normal-bundle-root-replay/execution-manifest.json),
and [16-identity endpoint replay](../validation/2026-10-10-endpoint-root-replay/execution-manifest.json).
All record terminal exit zero, and a fresh standard-library SHA-256 check
confirmed their recorded source hashes match the current original sources.
This is source-binding verification of existing executions, not a new
Macaulay2 execution or a mathematical proof inferred from a green manifest.
The local geometry and exhaustive interfaces remain the written proofs.

Historical 97-source/110-execution counts and frozen integrity seals are
unchanged. No repository memory, Git state or canonical record was mutated
by this audit; only this separate continuation-ready note was added.


---

## Source: 2026-10-11-session-all-quartic-results-acceptance.md

# October 11 root acceptance: every quartic carrier of fixed C0 is excluded

The universal integral projective-curve STCI question and the unrestricted
characteristic-zero question for fixed
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. This record accepts the complete
quartic-carrier theorem assembled from the preserved October 9--10
proofs and the new genus-two arguments. It supersedes the endpoint-open
frontier in the
[October 10 continuation acceptance](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-continuation-results-acceptancemd).
The source notes retain their dated scopes and historical open labels.
No claim of novelty is made without a separate literature assessment.

## 1. Accepted theorem and exact quantifiers

**PROVED HERE / independently audited.** Over every algebraically
closed field of characteristic zero, for every integral quartic surface
`X subset P3` containing the fixed monomial C0 and every homogeneous
form G of positive degree,

    V(X,G) != C0  set-theoretically.

The statement includes every normal and nonnormal integral quartic,
singular finite normalizations, arbitrary positive mate degree, and
reducible or nonreduced conductor schemes. It imposes no ordinary,
semi-log-canonical, first-normal-order or generic-regularity hypothesis
on the mate. It applies to projective equivalents of this fixed curve.
It is not asserted for every smooth rational quartic embedding.

## 2. Exhaustive assembly of the quartic cases

The earlier accepted plane-section argument makes an integral quartic
carrier generically regular along the smooth C0: otherwise a general
plane section would have at least four singular points, exceeding its
arithmetic genus three. This is derived, not an extra carrier hypothesis.
For a nonnormal quartic, the genus of the normalized general plane
section is exactly zero, one or two; genus three would leave no
codimension-one normalization defect. The earlier rationality argument
excludes nonrational normalization for a quartic containing C0, without
assuming a mate.

| Carrier lane | Accepted proof and coverage |
| --- | --- |
| Normal integral quartic | The prior all-degree normal-quartic theorem, routed by the [October 9 acceptance](OCT9_SINGULAR_DELPEZZO_AND_LOCAL_LIFTS.md#source-2026-10-09-session-results-acceptancemd) and canonical state. |
| Nonnormal, sectional genus zero | The [complete genus-zero audit](SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md), including smooth scrolls, the Veronese and the rational cone, with the prior separate applicability and conductor audits. |
| Nonnormal, sectional genus one | The [October 10 acceptance](OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-results-acceptancemd), complete fixed-center ribbon net, all five root partitions, actual conductor and arbitrary-power descent. |
| Nonnormal, sectional genus two, lambda zero | The [full bisection audit](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-genus-two-bisection-full-independent-auditmd) and global Cartier-double/ribbon obstruction accepted in the [resumed October 10 record](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-continuation-results-acceptancemd). |
| Nonnormal, sectional genus two, lambda one, nonendpoint trisecant | The [complete nonendpoint coverage audit](OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-auditmd), including every effective `(2,2)` conductor decomposition and arbitrary endpoint A-chain lengths. |
| Nonnormal, sectional genus two, lambda one, endpoint trisecant | The [full endpoint proof](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-endpoint-full-quartic-reductionmd) and [binding independent audit](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-endpoint-full-independent-auditmd), accepted below. |

The genus-two mate identity has exactly the two alternatives
`(lambda,q)=(0,4),(1,3)`. The actual normal ambient conic model identifies
the conductor-line intersection length as `4-f.c`. In the section lane
this length is three, so the line lies in the degree-three ruling of
the unique smooth quadric containing C0. For this literal curve its
intersection is either three distinct points or a triple endpoint;
there is no missing `[2,1]` contact partition. Coordinate reversal
exchanges the two endpoints.

Root has read the new complete proofs and independently reconstructed
the ribbon Euler calculation, global conormal map, conductor divisor
cases, local factorization identities and correction equations. Root
also accepts the completed
[independent dependency/coverage assembly](#source-2026-10-11-session-all-quartic-dependency-assembly-independent-auditmd)
at SHA-256 `ca4b7e8a174b2cd17536052ae3cae59f535c8674f6e2af732b44a15703522f73`.
It checks every older dependency scope, the noncircular use of prior
P-040, all normalization genera, both mate strata and every conductor
line position. Its separately completed
[degree-factor microaudit](#source-2026-10-11-session-degree-factor-and-mf6-scope-auditmd)
checks the reduced/integral factor argument and the actual primary
characteristic-zero cubic theorem.

## 3. The final endpoint lane is accepted

Root accepts the full endpoint theorem at owner SHA-256
`366c8396333118dabcaed6106fbc68fdaf0851d1005bf5c5d3511d46c77cc5c9`
and binding independent-audit SHA-256
`d4253e444643c2201e49de9dd20545bb6aff993123d303a75c286f8758d4c37c`.
The full eleven-dimensional quartic carrier ideal, rather than an
irreducible-residual subfamily, gives the actual equation on the blowup.
The proof exhausts:

* A nonzero contact normal coefficient, including the special horizontal
  prime having correction coefficient zero, another horizontal at infinity,
  and doubled horizontal components. Smoothness at the contact or the
  exact isolated `(-3)` correction contradicts the necessary coefficient one.
* Two transverse residual intersections, including infinity. The
  branch-preserving relative formal proof gives endpoint A-chains and
  the all-length correction coefficient strictly below one.
* A triple residual intersection. The
  [local ADE audit](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-endpoint-local-ade-correction-auditmd)
  retains the full ambient equation: an endpoint A-chain, an internal
  A-chain with exact coefficient `2/(n+5)`, or the actually realized
  D4 with coefficient `1/4`. The all-quadratic-terms-zero case violates
  ADE multiplicity two. The abstract D7 numerical shield is not a
  realization of this equation.
* The doubled-horizontal divisor `2B_T+2F0`. The
  [complete doubled-horizontal audit](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-endpoint-double-horizontal-independent-auditmd)
  uses the crepant residue to prove the exact identity
  `2 v^t Q^(-1) v=ord(h_B)` at every away-contact normal-derivative
  root. The global normal derivative has degree three, so infinity,
  repeated roots and arbitrary ADE blocks are included. The actual
  contact factorization bounds the entire contribution by `5/2`,
  while the mate equation requires three.

The initial unjustified doubled-horizontal shortcut is explicitly
preserved and repaired in the binding audit. No conclusion relies on
equating disjoint strict transforms with disjoint images after ADE
contraction, or on assuming every graph is an endpoint A-chain.

## 4. Consequences and retained higher-degree scope

Combining the theorem with the checked characteristic-zero cubic
exclusion of Craighero--Gattazzo and the elementary unique-quadric
divisor-class obstruction proves that **both defining forms of any
STCI presentation of fixed C0 must have degree at least five**.

The factor reduction is exact. The two defining forms have no common
surface component. Each irreducible factor of either form cuts a
nonempty positive-degree divisor with the other form. Its intersection
support is contained in the integral C0, hence is all C0. Thus that
factor is itself a carrier with the other form as mate. A degree at
most four factor is impossible by the quadric, cubic and quartic
exclusions. A plane cannot contain C0. This also covers reducible and
nonreduced defining forms of degree at most four.

If the two degrees are a,b, Bézout gives `ab=4m` for the actual generic
intersection multiplicity m. Consequently a quintic carrier would
require mate degree divisible by four, beginning with degree eight.
There is still no upper bound forcing a hypothetical presentation into
these or any other finite degree pairs.

All actual quartic-mate lanes are now closed, including MF6, larger
early-defect `(4,b)` pairs, and the principal at-most-630-point necessary
mate locus. Their earlier case proofs and necessary loci remain evidence,
but are no longer open STCI mate possibilities. Common quartic
local-cohomology ancestor incidence is a different condition: multiplier
equalities alone do not supply set-theoretic equality of two ambient
forms. Its 22 retained points and full lift lines, and other ancestor
directions, remain open unless a separate implication is established.

Higher minimum carrier degrees and entirely thick presentations remain
open. The totally ramified split-sextic boundary remains outside the
quartic theorem. No unrestricted non-STCI theorem for C0, universal
counterexample, or universal positive theorem has been proved.

## 5. Evidence and literature status

The fresh [primary-literature refresh](OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-primary-literature-frontier-refreshmd)
checks exact hypotheses in Craighero--Gattazzo, Jaffe, Ellia and
Hartshorne--Polini. None of the checked primary sources supplies this
full arbitrary-mate quartic theorem. This bounded finding does not
certify novelty. The unrestricted questions retain their stated open
repository status.

The [ribbon/conormal microaudit](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-bisection-ribbon-conormal-microauditmd)
and [independent weighted-ribbon interface audit](OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-weighted-ribbon-conormal-independent-auditmd)
supply separate checks of the full global nilideal and nonzero ambient
conormal map in the bisection theorem. Their agreement is not used in
place of the written sheaf arguments.

Root's isolated [normal-bundle replay](../validation/2026-10-10-normal-bundle-root-replay/execution-manifest.json)
passed eight exact checks and [endpoint local replay](../validation/2026-10-10-endpoint-root-replay/execution-manifest.json)
passed sixteen exact identities, both exit zero with copied source bytes
and raw subprocess streams. The nonendpoint chain and doubled-horizontal
companions have their separately recorded twelve and fourteen conditions.
These finite identity checks support their displayed algebra; the
written geometric proofs supply complete parameter and mate scope.
Copies, repeated passes, diagnostic runs and failed scaffolds are not
inflated into distinct mathematical verifiers.

Live HEAD remains `2ba77d1a1177db9390693066c6b185040766c089`, title
`2026-10-10 afternoon limit reached`, branch
`research/ultra-resume-2026-10-06`, observed on October 11. Root has made
no Git mutation. All new acceptance and canonical edits are working-tree
continuation data. Historical 97/110 and October 9 integrity counts
remain frozen historical records; the forthcoming continuation seal
certifies current bytes and routing, not theorem truth by check count.

## 6. Root-reviewed continuation beyond degree four

Root has read and accepts the bounded structural results in the frozen
[quintic frontier](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-quintic-structural-frontiermd),
SHA-256 `4e84d1183435f8509df48b6b1d02fb4f00f29736ec8670bb09b2577dc991595b`,
and its [independent audit](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit),
SHA-256 `9cf5438894e3fb07f2094b4bcc1280ec0ead01822155d3897aceb73ffc1011fb`.
These do not exclude every quintic carrier.

An integral quintic containing C0 is generically regular along it.
Under a mate its normalization lift satisfies `c_num=(4/5)H`, hence
`c_num^2=16/5`; smooth normalization is impossible. The ruled
intersection proof establishes rational normalization through sectional
genus three without a mate. The full genus-zero lane is excluded by
the degree-five minimal-degree classification, including its cone.
If the normalization is Gorenstein under a mate, sectional genus is
one or six; for a nonnormal carrier only one remains. In other genera,
a global canonical Cartier index, if one exists, is divisible by five.

The genus-one mate lane requires a degree-five ADE del Pezzo
normalization with exactly one A4 point. The lifted c meets an
interior A4 vertex, and `5c~4H` is an actual Cartier relation. A unique
degree-one curve supplies the exact one-dimensional restriction
kernel; the complete restriction embeds c as a rational normal quartic
in P4, and that line is tangent to c at the A4 point. The actual
upstairs conductor is in `|2H|`; the entire downstairs conductor is a
CM curve of degree five and arithmetic genus two. Neither reducedness
nor flatness of its cover is assumed. The unresolved task is whether
any power of the distinguished upstairs quartic section descends
through this entire conductor for an actual projection to P3. The
power remains unbounded; no ambient quartic follows from the
normalization section. Other nonnormal genera and normal quintics
remain open.

Root also accepts the actual finite-flat multiplication-duality proof
and necessary inequalities in the frozen
[multiplicity-ten audit](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-multiplicity-ten-filtration-auditmd),
SHA-256 `90bd87fad8cf0f10fe39b4e8d9c3946fc38a3424d497ce3f5ad969c5047221e3`.
For a hypothetical (5,8) pair, the first saturated line has degree
`-7,-6,-5`, with top defects of degree `25,16,7`. Four actual effective
divisors encode the full necessary filtration; their degree inequalities
leave 198,97,13 profiles respectively, 308 total. The recorded
standard-library enumeration supports this finite numerical statement.
These are not realized structures, an embedded classification, a
parameter-space exhaustion or a (5,8) exclusion. No extra mathematical
execution was performed merely to count or route this evidence.


---

## Source: 2026-10-11-session-degree-factor-and-mf6-scope-audit.md

# Degree factors, cubic scope, and conditional MF6 closure

Date: 2026-10-11. Auditor: `oct11_quartic_assembly_audit/degree_factor_audit`.
Status: **PROVED elementary factor reduction; KNOWN cubic exclusion;
conditional consequences of the full integral-quartic assembly**.
No canonical frontier file is edited by this note. The complete quartic
assembly remains a separate proof obligation and is not certified here.

Throughout, k is algebraically closed of characteristic zero and

    C0 = [s^4:s^3t:st^3:t^4] subset P3_k.

The statements also hold after a projective change of these coordinates.
No assertion about every smooth rational quartic embedding is inferred
from the proposed fixed-C0 quartic theorem.

## 1. Every irreducible factor is itself a carrier with a mate

Suppose nonzero homogeneous forms F,G of positive degree satisfy

    V_P3(F,G) = C0

as sets. Factor them in k[x0,x1,x2,x3] into irreducible homogeneous
factors, with arbitrary positive multiplicities.

First, F and G have no common irreducible factor: any common factor
would put its entire projective surface in their intersection, contrary
to that intersection being the curve C0.

Let f be any irreducible factor of F and g any irreducible factor of G.
They are coprime. Their intersection is nonempty and pure of dimension
one in P3. One algebraic justification is that f,g form a regular
sequence in the four-variable polynomial ring. The quotient is
Cohen--Macaulay of dimension two, so its minimal homogeneous primes have
height two; none is the height-four irrelevant ideal. Equivalently,
the projective dimension theorem and the absence of a common surface
component give a projective curve intersection.

The containment

    V_P3(f,g) subset V_P3(F,G) = C0

now forces equality. A nonempty pure one-dimensional closed subset of
the integral curve C0 must be C0 itself. In particular each factor f
and each factor g vanishes on C0, and **every pair of factors, one from
each form, is itself an STCI presentation of C0**. The same conclusion
holds for f with the entire other form G, and for g with F.

This is stronger than the elementary prime-ideal observation that at
least one factor of F must vanish on C0. That observation alone does
not establish the conclusion for all factors; the projective
intersection argument does. Repeated factors cause no exception, since
they do not change any of these underlying zero sets.

## 2. The precise cubic theorem and the degrees below three

The [literature ledger](../LITERATURE_LEDGER.md), section
Craighero--Gattazzo 1989, agrees with a fresh inspection of the actual
[Numdam PDF](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf).
The abstract and introduction on printed pp.171--172 state the
exclusion for a smooth rational quartic, a cubic surface, and a mate
of arbitrary degree over an algebraically closed characteristic-zero
field. The notations on pp.172--173 explicitly define a cubic surface
to be reduced and irreducible. Thus the theorem directly applies to
every irreducible cubic factor supplied by section 1.

No descent from a complex-only formulation is needed for that primary
statement: its stated base field already has the required scope. A
reducible or nonreduced homogeneous cubic form is nonetheless excluded
as a possible defining form. Section 1 produces either an integral
cubic factor to which the theorem applies, or a factor of degree one
or two, to which the following elementary exclusions apply.

The curve C0 is not contained in a plane, since its four coordinate
binary quartics are linearly independent. Its unique quadric is

    q = x0*x3-x1*x2.

Indeed, restriction of the ten quadratic monomials to P1 gives nine
distinct powers of s,t, and the only repeated weight gives precisely
q. This quadric is smooth. Under its Segre identification with
P1 x P1, C0 has class (1,3), up to exchanging the factors.

If a homogeneous mate of degree b restricted to q cut out only C0,
its effective Cartier divisor would have class (b,b) and support C0.
It would therefore be m*C0 for some positive integer m, requiring

    (b,b) = m*(1,3),

which is impossible. A mate identically zero on q would instead
contain the whole quadric and also fails the required intersection.
Thus no integral carrier of degree one, two, or three can occur.

For completeness, a separate complex-only carrier exclusion could
be transported to this literal C0 by finite-coefficient descent.
Choose a finitely generated subfield K of k containing all coefficients
of a hypothetical pair and the finitely many membership witnesses
for its radical equality with the rational-coefficient ideal of C0.
Embed K into C. The witnesses persist under scalar extension, so the
same pair would be an STCI over C. Smoothness and the displayed
parametrization of C0 persist as well. This is a valid backup argument,
not an additional hypothesis imposed on the 1989 theorem.

## 3. Consequence if the full integral-quartic theorem is accepted

Assume the separately audited assembly proves:

> Every integral quartic surface containing fixed C0 admits no
> homogeneous mate cutting it set-theoretically to C0, in every
> positive mate degree.

Then every irreducible factor of both forms in an arbitrary STCI
presentation has degree at least five. In particular

    deg F >= 5 and deg G >= 5.

This applies to reducible, nonreduced, and entirely thick
presentations. It does not assert that either form is generically
regular along the curve. It also does not supply a theorem forcing
some defining form to have degree at most four.

Therefore a completed all-quartic assembly would be a strict
minimum-carrier-degree reduction, rather than a proof that C0 is not
an STCI in arbitrary degree.

## 4. Which actual MF6 mate branches that would close

The exact P-042 calculation in
[the research record](../RESEARCH_RECORD.md) gives

    5*deg L + deg D2 + deg D3 = -26,
    e = deg L + 7 in {0,1}.

After the already excluded primitive-triple type e=0,(d2,d3)=(0,9),
the seven necessary numerical types of an actual (4,6) presentation
are

| e | (d2,d3) |
|---:|---|
| 0 | (1,8), (2,7), (3,6), (4,5) |
| 1 | (0,4), (1,3), (2,2) |

The proposed full quartic theorem excludes **every one** of these
actual mate presentations at once. It includes the historically
retained regular-ratio e=0,(3,6) member, the principal e=1,(1,3)
carrier locus, and e=1,(2,2). The fifteen coarse nonregular pole
strata surviving the horizontal-degree bound likewise cannot support
an actual (4,6) pair. The BF types and pole strata encode different
necessary data; closure does not require an unproved bijection between
their lists.

The conclusion also covers any reducible quartic defining form by
section 1. It is not limited to generic-rank members, principal
charts, or to the stronger ancestor exclusions already proved in
particular defect strata.

More generally every actual (4,b) mate presentation is excluded,
including the e=2 larger-b early-defect profiles retained in section A
of the audited state. Their abstract local CI countermodels remain
valid models of the numerical constraints; a carrier theorem excludes
their realization by an actual quartic STCI pair rather than proving
those local models impossible. Early-defect problems for carriers of
degree at least five and ancestor incidence are separate.

## 5. What does not follow for common quartic ancestors

The finite local-cohomology problem asks for an ancestor alpha and
actual quartic multipliers satisfying

    F*alpha=u,   G*alpha=v.

Those equations do **not** assert V_P3(F,G)=C0. In the audited
finite-flat quadruple interpretation, F and G have nonzero socle
images; they vanish on its canonical triple, rather than on the
whole quadruple. In particular these equalities do not turn either
quartic into an STCI carrier with a mate supported only on C0.

The [retracted bridge](2026-10-07-session-localcoh-mf6-bridge.md)
records exactly why replacing the nonzero socle images by zero is
invalid. Its corrected simultaneous-target proof excludes particular
ancestor strata by their own target equations. The present carrier
factor reduction supplies no replacement for such a proof.

Consequently the common-quartic-ancestor incidence, the 22 retained
second-family parameter roots with their complete lower lift lines,
and surviving positive-D2 ancestor strata are not declared closed
merely by an all-quartic carrier theorem. A further bridge would have
to establish the missing support or a direct target obstruction.
The totally ramified split-sextic carrier boundary and higher minimum
carrier degrees likewise lie outside a quartic-carrier theorem.

The split boundary is genuinely a sextic-carrier problem. In the
[full ramified reduction](OCT6_SESSION_FRONTIERS_AND_VALIDATION.md#2026-10-06-split22-finite-reduction), the
surviving actual forms are

    F_tau = -B^2 + tau*q*K,  tau!=0,

with deg B=3, deg q=2 and deg K=4, hence deg F_tau=6. Its hypothesis
is the existence of a mate of any degree, retaining the integral
carrier, reduced/content-free split exceptional divisor, and no
vertical component assumptions of P-020. It is not the assumption
that this sextic has a quartic mate. The corresponding
[split-sextic note](2026-10-05-split-sextic.md) records the necessary
degree and branch-order scale k*(11,1,8), with k>0; in particular the
mate degree is 8k in this stratum. Thus an all-quartic theorem does
not close this surviving one-parameter family, its normalization or
conductor obligations, or arbitrary sextic carriers outside those
split hypotheses.

## 6. No circular use of the new assembly in the normal-carrier input

The prior normal-quartic theorem uses excluded compressed mate
degrees through five. Its
[nonreduced independent audit](OCT7_NORMAL_RAMIFICATION_AND_VERONESE.md#source-2026-10-07-session-normal-nonreduced-independent-auditmd),
section 1, lists that dependency explicitly. The degree-five exclusion
is the already independently established P-040 no-(4,5) theorem in
the research record, proved from P-025's multiplicity-five structure
exclusion. It predates the present all-quartic assembly and does not
depend on it. Degrees one through three use the elementary and cubic
inputs above; degree four uses the separate classical CG1986
no-(4,4) theorem. Consequently this aspect of assembling the normal
carrier theorem into an all-quartic theorem introduces no circular
dependency. This observation does not re-audit every premise of the
prior normal-carrier classification or enumerations.

## 7. Audit boundary

This note certifies the factor argument, the elementary degree-one
and degree-two exclusions, and the exact scope of the inspected
1989 primary statement. Its all-quartic and MF6 closure consequences
are explicitly conditional on the separate full quartic assembly.
It gives neither an unrestricted negative theorem nor a novelty
certificate for the quartic assembly.


---

## Source: 2026-10-11-session-dp5-a4-local-chart-independent-audit.md

# Exact A4 chart of the parametric degree-five del Pezzo model

Date: 2026-10-11. Author: independent local-chart child of
`a4_exact_ideal`. This note concerns the stated parametrization and its
actual image closure. It does not assert that every geometric degree-five
A4 model is isomorphic to this parametrized model, nor that this chart
contains every singular point of the global surface.

## 1. Statement and scope

Let k be an algebraically closed field of characteristic zero. Let S be
the reduced projective image closure of the rational map

```
P2 --> P5,
[x:y:z] |--> [y z^2-x^3 : x y z : y^2 z : x^2 y : x y^2 : y^3].
```

Then the actual open subscheme `S intersect {Z0 != 0}` is isomorphic to

```
Spec k[a,u,v]/(u v+a^5).
```

Its only singular point is `[1:0:0:0:0:0]`. At that point its completed
local ring is exactly

```
k[[a,u,v]]/(u v+a^5),
```

the formal A4 surface singularity. The assertion follows from polynomial
coordinate changes; it needs neither a numerical singularity recognizer
nor a presumed global ideal computation.

## 2. Five exact relations

The following five quadrics vanish identically after the parametrization:

```
Z1 Z5-Z2 Z4,
Z3 Z5-Z4^2,
Z1 Z4-Z2 Z3,
Z0 Z5-Z2^2+Z3 Z4,
Z0 Z4-Z1 Z2+Z3^2.
```

On the chart `Z0=1`, put

```
a=Z1/Z0, b=Z2/Z0, c=Z3/Z0, d=Z4/Z0, e=Z5/Z0.
```

The last two relations solve

```
d=a b-c^2,
e=b^2-c d=b^2-a b c+c^3.
```

After this substitution the third relation becomes

```
f=b(a^2-c)-a c^2=0.
```

The first and second relations become `-c f` and `-b f`. Consequently the
chart coordinate ring of the scheme cut out by these five quadrics is
exactly `k[a,b,c]/(f)`, with no extra relation and no lost component.

The polynomial change of coordinates

```
u=c-a^2,
v=b+a c+a^3
```

has the polynomial inverse

```
c=u+a^2,
b=v-a u-2a^3.
```

It sends the single equation to

```
f=-u v-a^5.
```

In particular the five-quadric chart is integral: `u v+a^5` is an
irreducible primitive polynomial, linear in v over `k[a,u]`, since u and
`a^5` are relatively prime. This argument uses no characteristic-zero
division.

## 3. Why this is the actual image-closure chart

The preceding computation could otherwise only describe a proposed
containing scheme. Here density identifies it with the actual image.

On the nonempty open subset `e != 0` of the integral five-quadric chart,
take source coordinates `y=1`, `x=d/e`, `z=b/e`. The first two relations
give `a=b d/e`, `c=d^2/e`. The remaining relations give

```
e^2=b^2 e-d^3,
z^2-x^3=1/e.
```

Therefore the source parametrization, divided by its nonzero Z0, is
exactly `[1:a:b:c:d:e]`. Thus the entire open subset `e != 0` is in the
parametric image. It is nonempty, for example at
`(a,b,c,d,e)=(0,1,0,0,1)`, and hence dense in the integral chart.

All five quadrics vanish on S, so its chart is contained in this
five-quadric chart. Conversely the dense open subset just exhibited lies
in S. Since S is the reduced image closure, its chart is the entire
integral five-quadric chart scheme. This proves the asserted actual
chart identification without appealing to an unverified global kernel.

## 4. Singularity and normality

For `F=u v+a^5`, the characteristic-zero Jacobian ideal is
`(u,v,5a^4)`. Its support is the single point `(a,u,v)=(0,0,0)`.
The surface is a hypersurface, so it is Cohen--Macaulay and satisfies
Serre's S2 condition. It is regular away from that closed point, so it
also satisfies R1 and is normal. The coordinate origin corresponds to
`[1:0:0:0:0:0]`. Completion gives the displayed formal A4 equation
directly; replacing v by `-v` gives the alternative standard form
`u v-a^5=0`.

The Jacobian *scheme* is not asserted to be reduced: its local quotient
has length four in characteristic zero. Only the singular support is
a single reduced point.

## 5. Exact replay and preserved failed attempts

The written algebra above proves the result. The companion Macaulay2
source checks 20 elementary polynomial identities over QQ:

- five pullbacks of the quadrics;
- five chart-substitution identities, checked as one exact list equality;
- the equation under the A4 coordinate change;
- three coordinate identities in each direction of the inverse;
- three identities giving the inverse on the open `e != 0`.

The source is
[verify_session_dp5_a4_local_chart_2026_10_11.m2](../computations/verify_session_dp5_a4_local_chart_2026_10_11.m2),
SHA-256 `9a5672a81ce2cfd23fa0eddf2838a1b9224c9cd25a7a70535e2e5523c6ce222d`.
The observed final execution used `/opt/homebrew/bin/M2 --script`, exited
zero, and printed `PASS: 20 exact identities`; tool chunk `c6e806`.
The execution manifest and raw stdout/stderr are retained in
[2026-10-11-dp5-a4-local-chart](../validation/2026-10-11-dp5-a4-local-chart/execution-record.json).

Earlier failures are retained separately. The initial source used the
protected Macaulay2 variable `dd` (initial console chunk `8ff0c6`); its
exact source and a labeled explicit failed replay are stored as
`protected-dd-failed-source.m2`, `protected-dd-failure.*`. The next
scaffold mistakenly applied `entries` to the list `gens R` (observed
chunk `f79399`); its exact source and contemporaneous raw logs are
stored as `gens-list-failed-source.m2`, `gens-list-failure.*`. Renaming
the variable and scanning the generator list fixed these interface
errors. Neither was a failed mathematical identity.

No global-kernel, projective degree, or global-singular-locus check is
counted in this local verifier; those belong to the parent's separate
exact computation.


---

## Source: 2026-10-11-session-endpoint-two-common-roots-target-contact-independent-audit.md

# Endpoint septic: independent two-common-root contact audit

Status: **PROVED conditional univariate support exclusion, characteristic zero.**
The proof below verifies the target-septic contact calculation directly. Its
geometric application requires the parent's separately audited assertion that
full inverse support forces all roots of this target septic to be common roots
of `U,V`. This note does not assert that global reduction independently.

## 1. Data and precisely stated conclusion

Work over an algebraically closed field of characteristic zero. Put

\[
\begin{aligned}
U&=2az^3-3bz^2-z+g,&V&=3az^4-4bz^3-2z^2-z+d,\\
A&=az-b,&H&=az^3+z-g-1,\\
J&=AV-(Az-1)U,&E&=J^2-(3zA-1)HJ+AUH^2,\\
C_b&=a^2g-ab-b^3.
\end{aligned}
\]

Assume `a C_b != 0`. Exact expansion gives degree seven in `z`, with leading
coefficient `a C_b`. Suppose additionally that the endpoint projection has no
point off the lifted curve mapping into the affine target curve. Then:

* At every common root of `U,V`, the multiplicity as a root of `E` is at most
  four.
* A common root with multiplicity four as a root of `E` is the only common
  root of `U,V`; moreover `U/(z-rho),V/(z-rho)` have no common root, even at
  `rho` itself.
* Consequently, if `U,V` have exactly two distinct common roots, every one of
  them has `E`-multiplicity at most three. Their total multiplicity is at most
  six, so the degree-seven `E` cannot have all its roots supported there.

No squarefreeness assumption is used. In particular, a repeated common root
does not evade the conclusion.

## 2. Common-root parameters and the exceptional H=0 fiber

At a common root `rho` set `w=a rho-b` and `q=w rho`. Solving the two
common-root equations gives

\[
b=a\rho-w,\quad g=a\rho^3-3w\rho^2+\rho,\quad
d=a\rho^4-4w\rho^3+2\rho^2+\rho.
\]

The exact carrier identity is

\[
C_b=w\bigl(a(1-3q)+w^2\bigr).
\]

Thus `w != 0`; this covers, and excludes on the present locus, the possible
exception `k=b-a rho=0` in the opposite sign convention.

Writing `c_j` for the coefficient of `(z-rho)^j` in `E`, exact expansion gives

\[
H(\rho)=3w\rho^2-1,\qquad
c_1=-H(\rho)\bigl(6q^2-6q+1+3wq\bigr).
\]

The factor `H(rho)` must not simply be divided away. At the fixed target
parameter `z=rho`, the two residual affine fiber equations are

\[
\begin{aligned}
F&=wT(-1+3q+w^2T),\\
G&=T\{6q^2-4q-w+1+(4\rho w^3-2w^2)T+w^4T^2\}.
\end{aligned}
\]

If `q != 1/3`, put `T_0=(1-3q)/w^2`. It is nonzero and

\[
F(T_0)=0,\qquad G(T_0)=T_0 wH(\rho),\qquad
1+aT_0=C_b/w^3\ne0.
\]

Thus `H(rho)=0` with `q != 1/3` yields an actual off-curve point in the affine
chart, contrary to the stated no-extra-support hypothesis. This does not
confuse a vanishing affine denominator with an actual fiber.

The remaining exceptional case `H(rho)=0,q=1/3` forces
`rho=1,w=1/3`. Exact expansion then gives `c_2=1/9`, independently of `a`.
Since `c_1=0`, its `E`-multiplicity is exactly two.

## 3. Parameterization of contact order at least two

It remains to consider `H(rho) != 0`. If `c_1 != 0`, the multiplicity is one.
Otherwise put `D=6q^2-6q+1`; the equation `c_1=0` gives

\[
w=-D/(3q),\qquad \rho=q/w.
\]

Both `q` and `D` are nonzero: `q=0` would leave the defining equation equal to
one, while `D=0` would force `w=0`. Further,

\[
H(\rho)=-\frac{(3q-1)(3q^2+3q-1)}D.
\]

Therefore `q != 1/3` and `3q^2+3q-1 != 0` on this branch. The exceptional
zeros of these factors have already been handled in Section 2.

Here `c_2` is affine linear in `a`, with slope

\[
-\frac{3q(3q-1)^2(3q^2+3q-1)}{D^2},
\]

which is nonzero on the branch. Consequently `c_2=0` forces exactly

\[
a=-\frac{D^2(54q^4-72q^3+15q^2-3q+1)}{27q^3(3q-1)^2}.
\]

There is no unexamined zero of the coefficient of `a` in this step.

## 4. Exact coprimality checks and maximum contact order

After substituting this value of `a`, let

\[
\begin{aligned}
N_9={}&8748q^9-20412q^8+18954q^7-8262q^6+1458q^5\\
&-252q^4+180q^3-66q^2+12q-1,\\
N_{11}={}&17496q^{11}-46656q^{10}+39366q^9-16848q^8\\
&+12123q^7-12231q^6+8316q^5-2934q^4+612q^3\\
&-129q^2+25q-2.
\end{aligned}
\]

The actual next coefficients are

\[
c_3=-\frac{(3q^2+3q-1)DN_9}{81q^4(3q-1)^3},\qquad
c_4=-\frac{D^2N_{11}}{81q^4(3q-1)^3}.
\]

The exact gcd of their numerators is a nonzero rational multiple of `D`.
Since `D != 0`, these coefficients cannot both vanish. Every common root
therefore has multiplicity at most four in `E`.

Let

\[
R_{\mathrm{other}}=\operatorname{Res}_z
\bigl(U/(z-\rho),V/(z-\rho)\bigr)
\]

after the same substitutions. A separate exact Sylvester determinant gives
the gcd of the numerator of `R_other` with the numerator of `c_3` as again a
nonzero rational multiple of `D`. All denominators in this calculation are
products of nonzero rational numbers, powers of `q` and powers of `3q-1`.
Thus `c_3=0` forces `R_other != 0`. This includes the possibility that the
quotients both vanish at `rho`: such a repeated common root would also force
the resultant to vanish.

Multiplicity four requires `c_1=c_2=c_3=0`. It therefore forces no second
common root. If there are two distinct common roots, both multiplicities are
at most three, and their sum is less than the degree seven of `E`.

## 5. Scope and captured evidence

The proof is a conditional local-contact and univariate-support exclusion.
The parent's global audit must still justify the target residual equations
and the necessary support condition for `E` across all affine and projective
boundary cases. This note supplies no bound from first-normal degree alone;
the bound follows from the actual higher coefficients `c_1` through `c_4`.

The independent source is
[two-root-contact-target.m2](../validation/2026-10-11-endpoint-support-global-audit/two-root-contact-target.m2).
The final captured execution passed **14 exact assertions**, checking the
septic leading coefficient, common-root substitution, first coefficient,
exceptional fiber, order-two exceptional case, second-coefficient slope,
solved value of `a`, and both polynomial gcd conclusions. See
[the final execution record](../validation/2026-10-11-endpoint-support-global-audit/two-root-contact-attempts/20261012T000753990549Z/execution-record.json)
and its adjacent source snapshot, stdout and stderr.

The same directory preserves an earlier 12-assertion PASS and an intermediate
failed assertion caused by using total polynomial degree in all coefficient
variables instead of degree in `z`. The final source checks the eighth
`z`-derivative and the seventh `z`-coefficient directly. These are development
executions of one audit source, not independent geometric cases.


---

## Source: 2026-10-11-session-latest-pause-rundown.md

# Latest-pause rundown: October 11, after the all-quartic seal

This is a status snapshot for the user's request for a rundown. It is not a
new mathematical verifier or a replacement for a proof acceptance. The
universal integral-projective-curve STCI problem and the unrestricted
characteristic-zero question for
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN** in this investigation.

## Accepted and sealed milestone

The [all-quartic acceptance](#source-2026-10-11-session-all-quartic-results-acceptancemd)
assembles a written, independently audited exclusion of every integral
quartic surface containing fixed C0, with a mate of any positive degree.
It includes normal and nonnormal carriers, singular normalizations and the
full conductor schemes. It applies in characteristic zero and to projective
equivalents of this fixed embedding. Novelty has not been certified.

Together with the recorded plane, quadric and primary cubic exclusions,
the factor argument forces every irreducible factor of either form in any
hypothetical STCI presentation to have degree at least five. In particular,
both form degrees are at least five. There is no upper degree bound and no
theorem forcing an unrestricted presentation to have a quartic factor.
Actual quartic-mate lanes, including MF6, are closed. The distinct common
quartic-ancestor local-cohomology incidence is not closed by this theorem.

The frozen [October 11 seal](../validation/2026-10-11-continuation-seal/result.json)
records PASS at `2026-10-11T14:52:14.681994+00:00`: 5,747 record checks,
773 local links and 921 file bindings. A fresh read-only hash comparison
for this rundown found no mismatch in those 921 bindings. The seal checks
provenance and routing; it executes no mathematical verifier and does not
certify mathematical truth or novelty. Later notes below are outside that
frozen acceptance and seal unless already reached by their recorded scope.

## Accepted quintic structural frontier

The frozen [quintic frontier](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-quintic-structural-frontiermd)
and its [independent audit](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit)
exclude the full sectional-genus-zero normalization lane. Under a mate,
smooth normalization is impossible. Rationality is proved through
sectional genus three; this is not an exclusion of every other genus.
Gorenstein nonnormal normalization under a mate is forced into sectional
genus one, whereas other genera retain possible non-Gorenstein structures.
Normal quintics and those other nonnormal genera remain open.

The genus-one mate lane is forced onto a degree-five del Pezzo surface S
with exactly one A4 singularity, a smooth lifted curve c, and a unique
degree-one line ell. The relations `5c~4H`, `5ell~H`, `c+ell~H` are actual
divisor relations. There is an actual section `Q` of `4H` with divisor
`5c`, and every mate would pull back to `Q^k`. A quintic mate degree is
`4k`, with k at least two; the first remaining degree pair is (5,8).
The upstairs quartic section is not an ambient quartic without descent.

The [multiplicity-ten filtration](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-multiplicity-ten-filtration-auditmd)
leaves 308 necessary numerical profiles for (5,8). They are not realized
structures, a classification of all embedded structures, or an exclusion.

## New work after the seal

1. The [intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
   and [explicit-model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
   give a written exhaustion of the pair (S,c), including its plane
   blowup model and automorphisms. Supporting symbolic identities and their
   failed development attempts are saved. The intrinsic exhaustion is the
   geometric contraction and conic-orbit proof, not a finite check count.
2. The projection-center classification exposes a necessary scope correction.
   The intrinsic pair permits translations of the curve coordinate, but
   no remaining scaling. Endpoint projections have four lift parameters.
   Nonendpoint projections retain a further nonzero separation modulus
   delta, up to sign, as well as four lift parameters. The endpoint family
   alone does not exhaust the entire genus-one quintic lane. Any older
   globally read four-parameter wording must be read with this correction.
3. The [power-descent algebra audit](QUINTIC_ENDPOINT_JETS_AND_POWER_DESCENT.md#4-power-descent-algebra-audit)
   proves that actual membership in the full conductor algebra is required;
   a tensor equalizer can give a false positive. In characteristic zero,
   powering cannot repair a unit nilpotent-jet obstruction after its reduced
   phase is resolved. Purity of the actual normalization quotient means full
   generic conductor membership suffices for global section descent. Reduced
   split-branch phases can still have unbounded root-of-unity periods as the
   projection varies. This is an exact structural criterion within this
   lane, not a solution of its parameter space. The note's final
   four-parameter wording likewise requires the two-lane correction above.
4. The endpoint projection is written
   `X=(1+aT, r+bT, r^3+(g-r)T, r^4+(d-2r^2-r)T+T^2)`, with `c:T=0`.
   The [a=0,b!=0 proof](QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md#4-quintic-endpoint-a0-support-exclusion)
   now has a completed [independent full audit](QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md#3-quintic-endpoint-a0-polynomial-support-independent-audit).
   It proves that every displayed parameter choice has an actual off-c
   inverse point over C0. Thus every admissible projection in this subfamily
   is excluded in every mate degree. The owner's historical pending header
   is superseded, for this bounded claim, by the completed audit.
5. For endpoint a!=0, the [quadric-factor reduction](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#4-quintic-endpoint-quadric-factor-reduction)
   has a completed [independent audit](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#2-quintic-endpoint-factor-independent-audit)
   and separate [contact-length audit](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#3-quintic-endpoint-factor-contact-independent-audit).
   The actual pulled quadric factors as `hK`. Its integral residual curve
   has arithmetic genus one and image of type (3,2) on the quadric. Full
   inverse support requires exactly seven excess contact lengths. Those
   excesses can occur only at common roots of the two first-normal
   polynomials U,V. Coprime U,V therefore exclude a mate. Common-root strata
   remain open; the number of their roots does not bound higher contact
   lengths. The owner's pending header is superseded only for this audited
   reduction and coprime consequence, not for a full endpoint exclusion.

## Provisional and unfinished at this snapshot

The proposed endpoint a=b=0 all-power jet obstruction is not counted as a
completed result here: its final saved proof and independent audit are still
outstanding. The a!=0 common-root strata are under active exact support and
higher-contact investigation. Target-fiber eliminations, including a
degree-seven condition, are research leads until exceptional fibers,
projective boundaries and the full geometric implication have been checked.
No full endpoint or full genus-one quintic exclusion is claimed.

The nonendpoint family, including its modulus, is open. So are the other
quintic normalization genera, normal quintics, higher-degree carriers,
entirely thick presentations, the retained split-sextic boundary and the
separate common-ancestor incidence. A counterexample to the universal
question still requires an unrestricted non-STCI theorem for an actual
curve, not just exclusions of successively more degree pairs.

## Repository and continuation state

Fresh inspection found HEAD
`2ba77d1a1177db9390693066c6b185040766c089`, title
`2026-10-10 afternoon limit reached`, on the recorded research branch.
The current new proofs, audits, sources, raw streams and canonical edits
are saved working-tree data and remain uncommitted. `git diff --check`
passed. No Git mutation or mathematical replay was performed for this
status request.

The [canonical handoff](../SUCCESSOR_HANDOFF_2026-10-07.md) reflects the
sealed all-quartic and first quintic structural frontier. The newer notes
above are a separate post-seal continuation batch. They need a separate
root acceptance, corrected canonical routing and a new integrity seal;
the older seal must remain unchanged. This snapshot supplies a current
entry point without pretending that this integration has already happened.
