# Cross-branch assessment: actual equations and residual support

Date: 2026-10-31. Scope: the fixed
C0=[s^4:s^3t:st^3:t^4] in P3, characteristic zero, with arbitrary
homogeneous defining degrees. **Unrestricted STCI remains open.**
This is a closeout and research recommendation, not a new research round,
branch merge or canonical promotion.

## 1. Source states and closeout

Remote references were refreshed before comparison. Local research heads
include work not yet present in their remote tracking branches. The
following fixed commits, rather than branch names alone, delimit this
assessment. Proof paths below can be read with git show COMMIT:PATH.

| Stream | Fixed commit | Evidence used and authority |
| --- | --- | --- |
| This global-geometric stream | 7530d05 | Strategy assessment §§35–38; pencil Milnor note; reviewed provisional proofs and the subsequently completed §38 audit |
| Parallel carrier closeout, completed during this assessment | 61290bd | notes/2026-10-31-quintic-toric-center-incidence.md and its independent review; reviewed partial exclusions with the M incidence still open |
| Mathematical consolidation | fd50fb6 | INDEX, MAP, STATE, FRONTIER; synthesis/global_lifting_interfaces.md, intrinsic_fourth_extension.md and quadratic_covers_and_conductor_descent.md; maintained mathematical synthesis with explicit review boundaries |
| Containing intersections and elliptic construction | b271fc5, remote head; local branch remains 317d5bc | notes/2026-10-31-stci-package-closeout.md and its existence/projection audits; reviewed fixed-member constructions and explicitly unfinished family tests |
| Spectral realization | 0046bec | synthesis/order_three_roots_and_sextic_lifts.md and the linked spectral proof homes; reviewed provisional parameterization and bounded actual-source tests |
| Octic root comparison / torsion two | 2875622 | supplements/ACTUAL_OCTIC_ROOT_LIFT_COMPARISON.md and QUADRATIC_ROOT_TORSION_TWO_REDUCTION.md; reviewed provisional source comparison and actual proper pairs |
| Positive characteristic and lifting | 563fa53 | supplements/FROBENIUS_POWER_LIFTING_PRECISION.md, PRIME_TO_P_POWER_EXTRACTION.md, ARITHMETIC_EQUATIONS_AND_JET_GAPS.md and EFFECTIVE_CHARACTERISTIC_TRANSFER.md; reviewed provisional arithmetic results |
| Main | 9d734e1 | Older canonical/navigation baseline; later branch findings are not silently promoted into it |

The consolidation head is a selected integration checkpoint, not a
guarantee that the later research heads have all been incorporated.
The two detached worktree heads at the opening inventory were existing
main/consolidation checkpoints, not additional mathematical sources.

The previously unaudited Chow Hom lemma and source-applicability findings
are now independently reconstructed: see the follow-up audit in
[assessment §38](2026-10-31-unrestricted-strategy-assessment.md#follow-up-independent-review-after-usage-reset).
No material correction was required. Every map with the exact P-033
symmetric-power source and target bundles already comes from two global
forms. Existence of a map with the desired determinant remains open.
The result is reviewed provisional mathematics, not a new STCI theorem.

At the opening inventory, four untracked toric-center artifacts in
the shared checkout belonged to the separate carrier continuation.
A read-only preservation check flagged their remaining M=0 incidence,
coverage limitations and missing written support for an “accompanying
message” referenced by the saved JSON. These were preliminary flags
on that artifact state, not findings against the owner's later
reconciled partial-exclusion record. Static inspection is not
execution or family-theorem review. A separate
codex/quintic-octic-closeout-2026-10-31 worktree appeared during this
assessment; these artifacts and its final adjudication are left to that
owner. That continuation subsequently committed its
[reviewed partial closeout](2026-10-31-quintic-toric-center-incidence.md)
as 61290bd. Its written proof and independent specialization review
close the one-infinity boundary and three exceptional finite curves,
while retaining the explicit M incidence. This supersedes the preliminary
preservation flags for its covered claims, not the open full-center
question. No competing calculation or edits were made.

The spectral branch's larger eighteen-point slice remains unaudited.
The mixed torsion-two characteristic-zero chart remains unresolved:
a unit ideal over F_32003 does not settle its rational version.
These unfinished cases are preserved in their owning branches and
are not converted into a new queue here.

## 2. What has genuinely been added

The comparison distinguishes three levels: geometric data for a
multiple structure, realization by actual homogeneous equations,
and exhaustion of the intersection cycle. Progress at each level
is useful; it does not automatically pass to the next.

**This stream has found strong limits on coarse obstructions.**
For an equal-degree supported pencil, m=D^2/4 and
T=m+1-mu. The exact cluster interpretation gives
T=sum epsilon_i A_i and m=sum epsilon_i rho_i.
The universal local inequality T>=2 sqrt(m)=D already implies the
polar inequality T>=7D/8. The latter is valid but adds no quartic
restriction. Likewise, the checked complement classes, ordinary
genus estimates, finite-map equivalents and arbitrary Chow-power
determinants do not supply global equations or a contradiction.
These findings retire specific shortcuts, not topology, valuations,
conductor geometry or global constructions as subjects.

**The consolidation adds an intrinsic embedded mechanism.**
Its fourth-extension proof computes the actual contact-extension class
of every triple in the two allowed saturated quartic-pair types.
Only the quadric direction extends as required. This is an alternative
embedded-neighborhood proof of the (4,4) exclusion, not a new exclusion
in higher degrees. Its value for this lane is methodological: a
specific extension class can retain ambient compatibility that a
scalar genus or multiplicity budget forgets.

**Spectral geometry now includes a whole family, not only samples.**
At 0046bec, all smooth order-three roots in fixed ruling frames are
parameterized by an open of P7, with spectral trivializations and
graded CI families. A complete selected slice has six first-compatible
roots: four fail the actual sextic-symbol image, and the remaining two
fail full cubic lifting, including the free q^3 correction. The
parameterization is a positive geometric result. The exclusions concern
the selected slice and conditional smooth-root setting.

**The octic comparison reaches actual global intersections.**
At 2875622, restriction to the uniquely lifted first root gives
rho_f; quotienting by the complete actual correction image gives
kappa_f. Its target dimension is 6–9 for 17 multiplier coefficients.
This proves actual normal-order-two octic lifts passing first membership
for every smooth first-compatible root, while retaining possible fixed
divisors in the multiplier space. A certified seed has joint generation
and a proper (8,8) pair with
\[
[V(F,G)]=8[C_0]+R,\qquad \deg R=32.
\]
Thus there is genuine global realization, with a measured residual
cycle. The seed fails the second root obstruction; its q^4 perturbation
generically keeps multiplicity eight. It is not a surviving STCI
candidate or a demonstrated residual-absorption operation.

**Arithmetic lifting now identifies an actual specialization defect.**
For the prescribed powered-quartic pairs with p>=7, the largest strong
unramified Witt precision is 1+v_p(n), with both equations allowed
to deform. Prime-to-p power extraction excludes supported traits
of that prescribed type at every ramification index. A surviving
pure-p-power trait needs E>=p-1 and a positive endpoint defect
in the lower root:
\[
0\longrightarrow T_{\rm sp}\longrightarrow O_{D_0}
 \longrightarrow O_{Z_0}\longrightarrow0.
\]
If T_sp=0, relative Cartier extension and ambient lifting would
produce a forbidden characteristic-zero quartic mate. This is an
actual geometric implication, but neither a contradiction to
T_sp>0 nor a trait realizing it is known. It does not identify
T_sp with this stream's conductor boundary or Milnor defects.
Finite precision obtained by increasing degrees is not a compatible
fixed-degree lift.

The arithmetic branch also retains actual non-binomial (16,p)
supported pairs for p>=43. Frobenius supplies successful ambient
descent in that source; unrelated characteristic-zero pairs remain
possible. The all-quartic-carrier degree bound is not an all-carrier
degree bound.

## 3. What crosses branches, and what does not

There is one exact shared lifting operation. For a fixed actual
source V, symbol map sigma, next restriction tau and allowable
target subspace A, every lift must be tested in
\[
T/(A+\tau(\ker\sigma)).
\]
The consolidation's fixed-symbol lemma, the spectral sextic system
and the octic restriction-to-the-lifted-root map instantiate it.
A failed chosen lift is not an all-lifts obstruction unless its
functional annihilates every actual correction. This comparison
can construct corrections as well as rule them out.

There is no established identification of the normal-root classes
K1,K2 with global-source spectral-sequence differentials, arithmetic
endpoint torsion, or either conductor module. Nor is there an
arbitrary-pair reduction to the smooth, saturated, movement-two
root setting. The conditional (8,8) and (6,16) rows must retain
their bridge hypotheses. More root classifications cannot remove
those hypotheses by accumulation.

The positive proper octic pair and positive-characteristic solutions
also change how this lane should read its negative results:
substantial local and global compatibility is realizable. A new
nonexistence argument needs an additional actual ambient constraint.
Our locally automatic Milnor inequality and permissive exceptional
covers supply no reason to forbid the arithmetic endpoint defect.

Conversely, this lane prevents the other streams from treating
root moduli, finite lifts or a determinant as homogeneous sole-support
equations. The exact P-033 bundle types retain those equations;
arbitrary determinants do not. The checked
[Chow-complex literature](https://arxiv.org/pdf/math/0111040) and
[potential-good-reduction theorem](https://arxiv.org/pdf/0806.1364)
provide the structures in their hypotheses, without the missing
ambient construction.

## 4. Recommendation for this lane

Recommend one bounded continuation of the **existing five-parameter
elliptic normalization construction**, directed at full inverse
support. This is a deliberate return to an already recorded candidate,
not a new reduction or a claim that it is uniquely best.
The toric quintic projection problem is another actual global source;
its separately owned closeout should not be duplicated.

The elliptic family has genuine quadratic sections and a verified
finite birational octic member. That member has an extra inverse
scheme of projective length twelve, not twelve asserted distinct
points. Raising the mate degree cannot repair that fixed map.
Changing its actual projection parameters can change the map,
so the entire family is not excluded by the fixed-member failure.

Use precisely the source in b271fc5's existence audit §6:
B=Q(i)[mu,rho_0,rho_1,rho_3,rho_4],
S_mu=V(Q1+mu Q0), and U_j=V_j+rho_j Q0.
Retain source smoothness, basepoint freedom and finite birationality.
The next question is:

> Does any admissible geometric parameter fiber have no inverse
> support outside Gamma=V(Q0), or does every admissible member
> necessarily retain some extra inverse support?

Describe the inverse scheme and relevant specialization behavior
for the argument used; one exact positive fiber does not require
a classification of the whole family. When using a relative-family
argument, retain what happens when off-Gamma points approach Gamma.
On Q0=1 the test is
the fiberwise unit condition for Q1+mu Q0, Q0-1 and the substituted
quadric and three cubic generators of I_C0. Generic flatness may
help organize a dense open, but supplies no conclusion about all
boundary fibers: [Stacks, generic flatness](https://stacks.math.columbia.edu/tag/0529).
Saturation in the total parameter ring followed by specialization
cannot replace the required fiberwise support test.

This is a construction test with actual global input, not another
abstract compatibility criterion. One admissible positive fiber
would produce a carrier passing a necessary gate, still requiring
full conductor/power descent. For that fiber the later question is
whether Q0^b lies in the actual degree-b coordinate image.
No mate-degree search should precede the support gate. A negative
result for the whole family would exclude this source only.

**Stopping conditions:** stop at one exact admissible fiber with
full inverse support, a coverage-certified exclusion of the entire
admissible family, or a precisely identified missing geometric
comparison/representation that prevents deciding it. If only generic
failure is proved, preserve it with the exceptional locus and stop
for reassessment; do not automatically enumerate successive strata.
Set a resource cap before any later execution; reaching it closes
that attempt as unfinished rather than authorizing an automatic sequel.
Do not expand to neighboring elliptic targets, mate degrees or
local types without a new construction operation or coverage argument.

For nonexistence, retain the arbitrary-pair conductor/attachment
constraints and actual normal forms as the comparison target.
No new all-pair inequality or upper defect capacity is presently
available. The arithmetic non-eigen trait is a meaningful alternative
existence target, but currently lacks a specific fixed-degree
support-preserving lifting operation. Its absence of the known
trace obstruction is not positive construction evidence.

## 5. Review and disposition

The branch comparisons used fresh gpt-6.1-sol/high readers with
fixed source commits. They reused the owning proof/audit evidence;
they did not rerun all branch computations or re-certify every theorem.
The toric preservation check was read-only and unexecuted.
The separate §38 proof/source reconstruction passes as recorded above.

The fresh gpt-6-astra/xhigh strategy challenge required two changes
to the recommendation: acknowledge that the elliptic test was already
a leading candidate, and acknowledge the competing toric global
source. Both are incorporated. It also required keeping the
support-to-descent gap, whole-family versus generic coverage, and
fixed length-twelve scheme versus twelve distinct points explicit.
These qualifications are part of the recommendation, not afterthoughts.
The same reviewer checked the written report and assessment §39:
preservation passes. The separate Sol reviewer likewise checked
the written §38 audit and literature-ledger correction. Both
bounded contexts are complete and retired.

No new technical round is started by this assessment. All new findings
remain within their stated provisional or strategic scope; no result
or question record is promoted. The general goal remains paused
while this requested closeout and recommendation are committed.
