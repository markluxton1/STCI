# October 11 root acceptance: every quartic carrier of fixed C0 is excluded

The universal integral projective-curve STCI question and the unrestricted
characteristic-zero question for fixed
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. This record accepts the complete
quartic-carrier theorem assembled from the preserved October 9--10
proofs and the new genus-two arguments. It supersedes the endpoint-open
frontier in the
[October 10 continuation acceptance](2026-10-10-session-continuation-results-acceptance.md).
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
| Normal integral quartic | The prior all-degree normal-quartic theorem, routed by the [October 9 acceptance](2026-10-09-session-results-acceptance.md) and canonical state. |
| Nonnormal, sectional genus zero | The [complete genus-zero audit](2026-10-09-session-normalization-sectional-genus-zero.md), including smooth scrolls, the Veronese and the rational cone, with the prior separate applicability and conductor audits. |
| Nonnormal, sectional genus one | The [October 10 acceptance](2026-10-10-session-results-acceptance.md), complete fixed-center ribbon net, all five root partitions, actual conductor and arbitrary-power descent. |
| Nonnormal, sectional genus two, lambda zero | The [full bisection audit](2026-10-10-session-genus-two-bisection-full-independent-audit.md) and global Cartier-double/ribbon obstruction accepted in the [resumed October 10 record](2026-10-10-session-continuation-results-acceptance.md). |
| Nonnormal, sectional genus two, lambda one, nonendpoint trisecant | The [complete nonendpoint coverage audit](2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md), including every effective `(2,2)` conductor decomposition and arbitrary endpoint A-chain lengths. |
| Nonnormal, sectional genus two, lambda one, endpoint trisecant | The [full endpoint proof](2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md) and [binding independent audit](2026-10-10-session-genus-two-endpoint-full-independent-audit.md), accepted below. |

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
[independent dependency/coverage assembly](2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md)
at SHA-256 `ca4b7e8a174b2cd17536052ae3cae59f535c8674f6e2af732b44a15703522f73`.
It checks every older dependency scope, the noncircular use of prior
P-040, all normalization genera, both mate strata and every conductor
line position. Its separately completed
[degree-factor microaudit](2026-10-11-session-degree-factor-and-mf6-scope-audit.md)
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
  [local ADE audit](2026-10-10-session-endpoint-local-ade-correction-audit.md)
  retains the full ambient equation: an endpoint A-chain, an internal
  A-chain with exact coefficient `2/(n+5)`, or the actually realized
  D4 with coefficient `1/4`. The all-quadratic-terms-zero case violates
  ADE multiplicity two. The abstract D7 numerical shield is not a
  realization of this equation.
* The doubled-horizontal divisor `2B_T+2F0`. The
  [complete doubled-horizontal audit](2026-10-10-session-genus-two-endpoint-double-horizontal-independent-audit.md)
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

The fresh [primary-literature refresh](2026-10-10-session-primary-literature-frontier-refresh.md)
checks exact hypotheses in Craighero--Gattazzo, Jaffe, Ellia and
Hartshorne--Polini. None of the checked primary sources supplies this
full arbitrary-mate quartic theorem. This bounded finding does not
certify novelty. The unrestricted questions retain their stated open
repository status.

The [ribbon/conormal microaudit](2026-10-10-session-bisection-ribbon-conormal-microaudit.md)
and [independent weighted-ribbon interface audit](2026-10-10-session-weighted-ribbon-conormal-independent-audit.md)
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
[quintic frontier](2026-10-11-session-quintic-structural-frontier.md),
SHA-256 `4e84d1183435f8509df48b6b1d02fb4f00f29736ec8670bb09b2577dc991595b`,
and its [independent audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md),
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
[multiplicity-ten audit](2026-10-11-session-multiplicity-ten-filtration-audit.md),
SHA-256 `90bd87fad8cf0f10fe39b4e8d9c3946fc38a3424d497ce3f5ad969c5047221e3`.
For a hypothetical (5,8) pair, the first saturated line has degree
`-7,-6,-5`, with top defects of degree `25,16,7`. Four actual effective
divisors encode the full necessary filtration; their degree inequalities
leave 198,97,13 profiles respectively, 308 total. The recorded
standard-library enumeration supports this finite numerical statement.
These are not realized structures, an embedded classification, a
parameter-space exhaustion or a (5,8) exclusion. No extra mathematical
execution was performed merely to count or route this evidence.
