# October 9 root acceptance and continuation frontier

Date: 2026-10-09. This record supersedes the open-normalization
language in the October 8 acceptance/checkpoint where stated below.
The universal integral-curve STCI problem and the unrestricted
characteristic-zero problem for fixed C0 remain **OPEN**. No novelty
claim is made without a separate literature assessment.

All mathematical statements in sections 1--5 are over an algebraically
closed field of characteristic zero and concern the fixed smooth
rational quartic C0=[s^4:s^3t:st^3:t^4], unless explicitly broadened.
The new results concern integral quartic carriers. They do not impose
an upper bound on the carrier degrees of an unrestricted presentation.

## 1. The entire sectional-genus-zero and smooth-normalization lanes close

**PROVED HERE / independently accepted.** Every integral quartic
whose normalization has sectional genus zero is excluded as a mate
carrier for C0 in every mate degree. Consequently every integral
quartic with smooth normalization is excluded in every mate degree.

The [owner proof](2026-10-09-session-normalization-sectional-genus-zero.md)
and [independent audit](2026-10-09-session-normalization-genus-zero-independent-audit.md)
give an exhaustive classification from nef-big vanishing and
Riemann--Roch: h0(H)=6, so the complete polarized normalization is a
degree-four minimal-degree surface in P5. The possibilities are
F0, F2, the Veronese surface, and the rational-normal-quartic cone.
The earlier entire-scroll and Veronese proofs exclude the first
three; the newly proved cone argument excludes the fourth using
torsion-free class group, full normalization fibers, and the
unit-factor differential lemma.

There is no remaining "other smooth polarization" quartic lane
under a mate: a lift avoiding the singular locus forces sectional
genus zero, and this classification is exhaustive. The cone argument
uses no reducedness hypothesis on a conductor.

Root also proved, and the independent audit accepted, that an
integral quartic containing this smooth degree-four curve is
automatically regular at its generic point. Otherwise a general
integral plane quartic would have four distinct singular points,
contrary to arithmetic genus three. Thus no order-one qualifier
remains in the new integral-quartic conclusions.

## 2. All nonnormal quartics containing C0 have rational normalization

**PROVED HERE / independently accepted, without a mate hypothesis.**
Every integral nonnormal quartic containing C0 has a rational
normalization. Extra isolated points over C0 need not be excluded
for this theorem. The same argument applies to any smooth rational
degree-four curve in a nonnormal integral quartic.

See the [owner proof](2026-10-09-session-nonrational-quartic-normalizations.md)
and [independent audit](2026-10-09-session-nonrational-normalization-independent-audit.md).
For a smooth resolution M and L the pulled-back hyperplane,
L^2=4, K_M.L=2pi-6<0, and 0<=pi<=2. A nonrational resolution is
ruled over a curve of positive genus. Pushing the nef L through
point blowdowns gives actual multiplicities 0<=m_i<=a, including
infinitely near centers, where a is its ruling-fiber degree. The
exact total-transform intersection identity is

    4=(2g-2)a^2+(6-2pi)a+sum m_i(a-m_i).

It forces a<=2. The strict lifted P1 of C0 must be a fiber
component and has degree four, giving 4<=a<=2. This contradiction
uses only the existence of C0, not a mate or full inverse support.
The nonnormal hypothesis is material: normal quartics have pi=3
and are covered by the earlier separate normal-carrier exclusion.

## 3. The genus-one lane reduces to two singularity patterns

**PROVED HERE / independently accepted.** Every genus-one
normalization of an integral nonnormal quartic containing C0 is a
normal Gorenstein del Pezzo surface of degree four with only ADE
singularities. Its minimal resolution is a weak del Pezzo surface
with L=-K_M. No mate hypothesis is needed for this classification
reduction.

The [root proof](2026-10-09-session-genus-one-delpezzo-reduction.md)
and [independent audit](2026-10-09-session-rational-genus-one-ADE-independent-audit.md)
derive h0(K_M+L)=1. Its unique effective divisor is exceptional;
minimality gives nonnegative canonical intersection with every
exceptional prime. Negative definiteness then forces that divisor
to be zero. Compatible canonical differentials give an actual
crepant equality and K_S=-H. The primary crepant/Du Val and weak
del Pezzo marking inputs are explicitly checked in the notes.

**PROVED necessary filter, with root's separate proof reconstruction.**
If such a genus-one carrier has a mate, its complete exceptional
type is exactly one of 4A1 or A3+2A1, and its mate degree is even.
All other ADE types in this lane are excluded. See the
[owner D5 proof](2026-10-09-session-delpezzo-D5-torsion-filter.md)
and [root independent audit](2026-10-09-session-delpezzo-D5-root-independent-audit.md).

The missing integral root Z=L-c# has square -2 and belongs to
sat(R) minus R. Downstairs smoothness is needed to exclude Z in R.
In the signed-coordinate D5 model, a missing root can join only
two full D blocks. Five coordinates allow only block sizes (2,2)
or (2,3), giving the two types above and index two. The effective
corrections are

| Type | Effective exceptional correction Z | Strict curve intersections |
|---|---|---|
| 4A1 | Half the sum of the four exceptional curves | One with each |
| A3+2A1 | Middle A3 curve plus half its ends and the two A1 curves | One with the middle and each A1; zero with the ends |

The owner reflection/HNF checker and root's different signed-partition
checker both completed isolated terminal PASS. They check all 428
embedded root subsystems; precisely fifteen 4A1 embeddings and ten
A3+2A1 embeddings are nonprimitive. The written signed-component
argument proves completeness; program agreement alone is not the
proof. A further worker audit was interrupted at the weekly quota
before a final written record and is not counted as completed.

## 4. A uniform four-A1 family is excluded in every mate degree

**PROVED HERE / independently accepted.** On the parameter open

    alpha beta gamma delta (alpha delta-beta gamma) != 0,

the [displayed family](2026-10-09-session-singular-delpezzo-four-A1-family.md)
has normalization S=V(ae-c^2,bd-c^2) in P4, a smooth lifted rational
normal quartic with 2c~2H, and projection to the exact fixed C0.
Nevertheless every carrier in that family is excluded in every
mate degree. The [independent audit](2026-10-09-session-singular-delpezzo-four-A1-family-independent-audit.md)
proves the actual finite birational normalization and entire parameter
coverage, including repeated roots and the special cancellation loci.

Every zero of the nonzero binary quartic L_C lies away from the
two endpoints. It gives both z=+U^2V^2 and z=-U^2V^2 above the
same C0 point; the negative lift is not on the rational normal
quartic. A pulled-back mate cannot vanish at an isolated extra
point without a height-one zero component through it. Full inverse
support therefore fails. The root's fresh isolated owner replay
passed in 0.603 seconds, in addition to the independent auditor's
owner and countercheck replays. The final
[audit manifest](../validation/2026-10-09-four-A1-family-audit/audit-manifest.json)
preserves the actual source and proof hashes.

This is not the entire four-A1 projection class. In particular this
construction places two of its singularity passages at the fixed
C0 parameter endpoints. Other positions and the singular coordinate
transformation boundary are not silently included.

## 5. Principal MF6 carriers have an explicit finite necessary locus

**PROVED necessary finite reduction / separately accepted algebra
and geometry.** On the declared principal contact open, every
nonnormal carrier having a mate lies in a fixed binary-gradient
Sylvester determinant's zero locus. It contains at most **630 distinct
principal weighted parameter points**. The exact zero list remains
uncomputed, and this locus is not asserted to equal the nonnormal
parameter locus or the locus of actual mates.

The [owner proof](2026-10-09-session-mf6-principal-weighted-candidate.md),
[independent geometry audit](2026-10-09-session-mf6-weighted-candidate-geometric-audit.md)
and [independent algebra audit](2026-10-09-session-mf6-weighted-candidate-algebra-independent-audit.md)
bind eighteen actual quartic forms, three polynomial syzygies of
weighted degrees 9,9,10, and the actual first-normal binary octic.
The fixed 14-by-14 determinant has weighted degree 210 and retains
zero-generator fibers and infinity multiple roots. At a good point
modulo 101 its determinant is 22, proving characteristic-zero
nonvanishing by the primitive integer sextic and powers-of-two
denominator/Gauss argument. The finite ordinary-plane cover gives
Bezout bound 1260, with two distinct lifts per principal point,
and hence 630.

Root's full isolated source replay passed in 25.463 seconds; a
new bounded independent coefficient/matrix/infinity countercheck
passed in 7.909 seconds. The input closure and final
[audit manifest](../validation/2026-10-09-mf6-weighted-candidate-audit/audit-manifest.json)
are retained. Completeness of the whole kernel module at every
exceptional fiber is not needed: one checked syzygy and the accepted
pointwise rank-one theorem suffice, while zero syzygy fibers remain
in the determinant's zero locus.

The r=0 lead from modulo-13/23 multiple-root samples was false in
characteristic zero. Exact cubic-field computation gives squarefree
normal coefficients and a zero-dimensional projective Jacobian
locus, so all three r=0 conjugates are normal and excluded by the
normal theorem. The owner note retains those bad-reduction leads;
they must not be promoted as nonnormal examples.

## 6. Current surviving frontier and evidence record

For an integral quartic mate carrier for fixed C0, the normal lane,
sectional-genus-zero lane, every smooth normalization and every
nonrational normalization are now excluded. A survivor requires a
rational singular normalization and a smooth non-Cartier lift through
its singular locus. In genus one, only 4A1 and A3+2A1 remain and the
mate degree is even. Genus-two rational normalizations remain OPEN.

Other four-A1 projections, A3+2A1 conductor descent, and genus-two
geometry are the next structural targets. The finite principal MF6
candidate list still needs its actual carriers and conductor jets
classified. The remaining 22 second endpoint-family points of
degrees 3,4,15, their full lower lift lines, e=1 ancestor degrees
2,3,4, early e=2 defects, higher minimum carrier degrees, entirely
thick presentations and the split-sextic totally ramified boundary
also remain OPEN.

The reconciled [execution index](../validation/2026-10-08-continuation-index/index.json)
now contains **97 distinct top-level sources with latest PASS records
and 110 explicitly indexed executions**. The original 55-source/61-run
baseline was retained. The earlier 91/103 and 95/108 index bytes are
preserved separately. Imported helpers and unindexed discovery runs
are not inflated into independent checks. Old failure logs and the
disclosed lost bytes of one superseded Veronese revision remain.

Live Git inspection found branch research/ultra-resume-2026-10-06
at HEAD e7c9c9594795271ff2c1b0a9026955523975e7d7, with commit title
"2026-10-09 morning limit reached". The inherited October 6 snapshot
3ffda7548a863387429adab61eefe02575e86297 is historical. Root did not
perform this Git mutation; the newly observed checkout is authoritative.

Several workers subsequently terminated at the weekly account limit
with reset message October 14, 8:24 AM local. Their saved completed
proofs and exact runs remain evidence; unfinished assignments, the
conditional smooth-conic conductor proposal, and absent final worker
audits remain leads. Root completed the separate D5 audit and
record reconciliation. No account reset credit was used. No process
is claimed live from a saved input alone, and the global goal is
not marked complete or narrowed to this batch.
