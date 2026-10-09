# Continuation handoff — 2026-10-07, reconciled through 2026-10-09

Read [AUDITED_STATE_2026-10-07.md](AUDITED_STATE_2026-10-07.md) first, then
[RESEARCH_UPDATE_2026-10-07.md](RESEARCH_UPDATE_2026-10-07.md), the relevant
proof note and its independent audit. Older handoffs are historical.
The universal STCI problem and unrestricted characteristic-zero C0
problem remain unresolved.

## Live checkpoint

The current branch is `research/ultra-resume-2026-10-06`. The retained
October 6 interruption commit is `3ffda7548a863387429adab61eefe02575e86297`.
Inspect `git status` and current sources before trusting any older hash.
No changes were reset or wholesale research branches merged in this
continuation. The current notes and exact outputs are continuation data.

Accepted major results: every normal quartic carrier for fixed C0 is
excluded in characteristic zero, with any mate degree; MF6 e=0 type
(4,5) is excluded completely; the entire primitive e=1,D2=0 quartic
lane is excluded in every mate degree; the dx=1 full five-coordinate saturation
gap is closed; the e=2 local-cohomology corner is excluded and its
endpoint direction classification is complete; the primitive e=1,D2=0
common-quartic-ancestor lane is separately excluded. Each statement has a
linked proof with a specified source/dependency scope.
The complete `(P2,O(2))` nonnormal quartic-carrier lane is now excluded,
including its non-slc Jordan forms. The first rational e=2,h=t ancestor
endpoint family is fully excluded; the second has a generic dual with
22 retained parameter points of degrees 3,4,15 after the two quadratic
exceptions were independently excluded for every lower lift. The exact ancestor-generator splitting
criterion and six positive-second-defect endpoint exclusions are also
accepted with their separate carrier and ancestor arguments.
Every integral quartic singular along a smooth twisted cubic is now
excluded for fixed C0 in every characteristic-zero mate degree, including
non-slc cases. The entire conductor and smooth-scroll normalization
hypotheses are proved for this class. Both algebraic e=1,d2=4 ancestor
directions are also excluded for all homogeneous defect sections.
The entire e=1,d2=1 common-quartic-ancestor lane is now excluded,
including the principal curve, genuine infinity defect and projective
b0=0 chart. The node's dimension-four fixed-cubic space is explicitly
retained; other valid fibres have dimension one.
Every integral quartic with smooth rational quartic-scroll normalization
is now excluded for fixed C0 in every characteristic-zero mate degree,
with no reducedness or Gorenstein assumption on either conductor. The
exact Artin and differential arguments exhaust the nongorenstein cubic
schemes as well. See the
[late root acceptance](notes/2026-10-08-session-late-results-acceptance.md)
and [full independent scroll audit](notes/2026-10-08-session-scroll-nongorenstein-independent-audit.md).

The normal theorem does not imply that arbitrary quartic carriers are
excluded. The historical broad e=2 theorem does not imply that larger
early-defect quartic pairs are excluded. A local CM or CI control model
does not imply an embedded global STCI pair.

## Priorities and open proof obligations

1. The primitive e=1 audit is accepted. The complete quartic pencils
   and finite/infinity pole computations reduce every mate degree to
   four pure pencil members; the affine normalization gluing obstruction
   excludes them. Extend the method to positive D2 directions,
   particularly MF6 types (1,3),(2,2), while retaining their extra
   defect-killing sections. Do not reuse the primitive triple frame
   without reconstructing these sections.
   The principal d2=1 ancestor contact theorem and all exceptional
   frames are already closed. Its direction curve has elliptic equation
   `YE^2=XE^3+96XE-448`; the unique-carrier family has a finite proper
   closed nonnormal subset. Determine that exact finite carrier locus,
   keeping ancestor rank conditions distinct from all-mate exclusions.
   The new weighted polynomial kernel has saved degree9,9,10 generator
   leads; verify its current source/output status before using it.
   All complement carriers, including p=8,r=1/2, are excluded in every
   mate degree. The generic principal carrier problem remains open.
2. Continue the local-cohomology endpoint families using the saved
   polynomial duals, rational seeds and .m2 sources. A dual over Q(k)
   does not exclude its denominator roots. The first-family exception
   factors Q2,Q1,Q3,Q13 are now all excluded for
   every lower lift, with an independent completeness and rational-source
   audit. The second family's two quadratic factors are now excluded
   at all four geometric roots and for every lower lift. It retains 22
   primitive geometric parameter points in the degree3,4,15 factors,
   each with its entire lower lift line. The two
   boundary families and non-endpoint top zeros remain open. The accepted
   simultaneous-target e=1 proof must retain the nonzero target terms;
   its retracted single-multiplier predecessor is not a valid premise.
   Both algebraic e=1,d2=4 directions are excluded for all defect
   sections. The principal obstruction-zero direction's extension
   derivation is only an exploratory source, with no completed output
   or independently identified cocycle yet. Do not use it as a theorem.
3. For nonnormal quartic carriers, exploit full inverse-image purity
   and fiber gluing. If the smooth curve lift avoids singularities of
   the normalization, adjunction gives a useful sectional-genus test.
   Verify the precise normalization hypotheses; do not transfer a
   semi-log-canonical classification to every degeneration. The
   [conditional nonnormal reductions](notes/2026-10-07-session-nonnormal-structural-progress.md)
   exclude the stated ordinary scroll and Veronese subclasses.
   Degenerate-pinching countermodels prevent an unrestricted
   ramification-support or ordinary-pinch-count argument.
   The stronger [all-Veronese proof](notes/2026-10-07-session-veronese-pencil-classification.md)
   closes `(P2,O(2))` without slc, using actual first conductor jets.
   The [smooth twisted-cubic applicability theorem](notes/2026-10-08-session-scroll-conductor-applicability.md)
   is now part of the complete smooth rational quartic-scroll exclusion.
   Reduced and nonreduced actual conductors, including nongorenstein
   schemes, are all covered by the
   [classification and exact Artin proof](notes/2026-10-08-session-scroll-nongorenstein-cubic-classification.md),
   [independent Artin audit](notes/2026-10-08-session-scroll-artin-independent-audit.md)
   and [differential lemma](notes/2026-10-08-session-normalization-differential-independent-audit.md).
   Focus on other smooth polarized normalizations and singular
   normalizations. A smooth lift passing through a singular normalization
   point is not excluded by adjunction for a lift avoiding singularities.
   Do not treat the ACM cubic classification as a classification of all
   nonnormal quartic surfaces.
4. The uniform e=2 b=9,10,11 defect profiles require an actual quartic
   contact incidence and a degree-one obstruction annihilator. The
   six Hankel minors and degree-sixteen determinant are saved in
   `scratch/session_uniform_e2_hankel.json`; no universal rank-one
   saturation was completed.
5. The entirely-thick branch, higher minimum carrier degrees and
   split-sextic totally ramified boundary remain open. Use higher
   jets, filtered structures or valuations. First tangent forms do
   not bound later horizontal multiplicities.

## Reproduction and evidence

Use `PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python`
for SymPy and `/opt/homebrew/bin/M2 --script` for Macaulay2 while those
paths exist. The temporary Python environment is not guaranteed to
survive a future machine session; inspect the environment record.
The corner and generic sparse polynomial-dual verifiers use Python's
standard library for checking their stored identities.

[Validation note](notes/2026-10-06-session-validation.md) and
[validation index](validation/2026-10-06-session/validation-index.json)
retain command, source hash, runtime, exit status and output evidence.
The initial baseline and successful repairs should not be rerun just
because the date changes. Run changed or newly completed sources;
preserve failure logs and distinguish an identity check from a geometric
proof or full parameter exhaustion.

Use the newer [validation index](validation/2026-10-08-continuation-index/index.json)
and [October 8 checkpoint](notes/2026-10-08-session-checkpoint.md) for the
complete continuation counts (91 latest-PASS sources and 103 indexed
executions), retained failures, interrupted-agent state,
and the explicit superseded Veronese-source retention limitation. All
agents have stopped at usage limits and subsequently resumed after
verified resets. At 2026-10-09 11:25:38 UTC the next reset had passed;
live usage allowed ordinary work and the finite-carrier and singular
normalization agents resumed. Assignments without completed evidence
are not results. Root did not mark the global goal complete.

If a tool or agent stops, inspect its current process/session handle
and final artifact status. An .m2 input file or an intended run is not
evidence of a live process or a successful result. Do not promote an
unfinished module calculation or launch overlapping copies blindly.
