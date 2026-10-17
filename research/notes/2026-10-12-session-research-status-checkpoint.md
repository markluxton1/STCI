# Research status checkpoint, October 12

Recorded by root at 2026-10-12 15:09 UTC (11:09 EDT), in response to the
user's request for a rundown at the latest pause. This is a current
root-reviewed routing snapshot, not a new full-record seal. Work continues;
the research goal has not been marked complete, blocked or paused.

## Global scope

The universal integral projective-curve STCI problem and the unrestricted
characteristic-zero problem for the literal curve
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. No positive universal theorem,
counterexample, unrestricted two-form presentation or upper bound on
hypothetical defining degrees has been established. No novelty claim is
certified. The new exclusions below concern this fixed curve and its
projective equivalents in characteristic zero, not every rational quartic
or every algebraically closed field.

## Sealed, accepted frontier

1. **PROVED HERE / independently audited:** every integral quartic carrier
   of fixed C0 has no mate in any positive degree. The normal and all
   nonnormal normalization-genus cases are exhausted. The degree-factor
   argument and checked lower-degree exclusions imply that every
   irreducible factor of either defining form has degree at least five.
   See the [all-quartic root acceptance](2026-10-11-session-all-quartic-results-acceptance.md).
2. **PROVED HERE / independently audited:** the entire admissible endpoint
   projection family in the sectional-genus-one quintic A4 normalization
   lane has no mate in any positive degree, for all four lift parameters.
   See the [endpoint root acceptance](2026-10-11-session-quintic-continuation-results-acceptance.md).
   The intrinsic pair is unique, but the nonendpoint projection family
   retains a nonzero separation parameter and is a separate problem.

The latest sealed checkpoint is the
[quintic continuation seal](../validation/2026-10-11-quintic-continuation-seal/result.json),
completed at 2026-10-12 14:22:11 UTC: PASS, 8,387 record checks, 868 local
links and 1,203 bound files. Root freshly recomputed all 1,203 stored
file digests for this rundown: no changed or missing binding was found.
That check certifies the recorded bytes and routing, not mathematical
truth. It reran no mathematical verifier. New October 12 research below
postdates that seal and is not covered by it.

## New independently audited nonendpoint progress

All statements here inherit the accepted actual degree-five A4 pair and
require an admissible center-avoiding projection when interpreted as an
integral quintic normalization. Parameters are `delta!=0,a,b,g,d`.

* **PROVED HERE / independently audited, every mate degree:** let Ph,Jh
  be the corrected homogeneous conormal cubics and put
  `Jbar=d-2g+2b-a`. A hypothetical mate requires
  `Jbar*Res_h(Ph,Jh)=0`. Thus a proper dense open part of this
  five-parameter family is excluded in all mate degrees. The proof
  converts cotangent surjectivity and the necessary single-point fibers
  over C0 into exact local normalization isomorphisms. The actual
  conductor divisor in `|2H|` would then miss the lifted curve, contrary
  to its required restriction degree eight. This is not a first-normal
  bound on higher contact lengths. See the [owner proof](2026-10-12-session-nonendpoint-conormal-cubic-reduction.md)
  and [independent all-mate audit](2026-10-12-session-nonendpoint-all-mate-conormal-conductor-independent-audit.md).
* **PROVED HERE / independently audited, every mate degree:** the
  entire-line rank-one subfamily has an actual downstairs-frame
  differential obstruction to every positive power of Q. See the
  [pole and line-jet audit](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet-independent-audit.md).
* **PROVED HERE / independently audited, structural reductions:** the
  residual Weil divisor has degree partitions `6,2+4,3+3,2+2+2`.
  The full `2+2+2` partition is excluded. The conic-plus-quartic case
  reduces to eight necessary one-parameter families, retaining every
  nonzero delta. Off the two factor hyperplanes the actual integral
  residual has arithmetic genus one, maps birationally to a target
  residual of arithmetic genus three, and needs exactly eight additional
  scheme lengths of contact beyond its intrinsic intersection with c.
  No upper bound on those lengths is asserted. See the
  [residual-factor/genus audit](2026-10-12-session-nonendpoint-residual-factor-and-genus-independent-audit.md).
* **PROVED HERE / independently audited, every mate degree:** every
  equal-lift projection `a=b=g=d` is excluded for all `delta!=0`.
  Complete source-boundary and exceptional-target equations also give
  additional exact bounded exclusions; they do not exhaust the family.
  See the [target-fiber proof audit](2026-10-12-session-nonendpoint-target-fiber-independent-proof-audit.md).

Root has read the new written audits and the corresponding proof scopes.
The corrected conormal coefficient identities are supported by root's
seven-condition M2 checker and an independent twelve-check implementation;
the target-fiber checker has seventeen identities and its independent
gap checker eleven. These support the displayed algebra. The written
geometric arguments provide the scope of each theorem. Failed mathematical
expansions, protected-name failures and checker-operation failures are
preserved separately from successful runs. Replays are not independent
mathematical sources.

## Work in progress, not accepted as completed theorems

* **COMPUTATIONALLY CERTIFIED / geometric audit pending:** for
  `G=g-3b+2a=0`, `Jbar=0`, `B=b-a!=0`, the owner reports exact polynomial
  Bezout certificates for all 21 degree-five root-multiplicity profiles
  supported at target p=0 and the two roots of `p^2-6p+6`. Each coefficient
  ideal generates one even before saturation. A new proof/evidence record
  and a separate audit of the complete root cover, forced parameter
  values, degree drops and every exceptional fiber are being completed.
  The already accepted B=0 equal-lift result does not substitute for this
  audit. See the [new supporting source](../computations/verify_session_nonendpoint_GJ_zero_profile_exclusion_2026_10_12.m2).
* **PROPOSED STRUCTURAL PROOF / audit pending:** a conductor-geometry
  argument proposes excluding the remaining `Jbar=0` coprime-cubic stratum
  in all degrees, which would sharpen the necessary locus to
  `Res_h(Ph,Jh)=0`. Its local fiber-length, global conductor-prime
  accounting and reduction to a square power require independent
  reconstruction. It is not part of the accepted frontier above.
* **ACTIVE COMPUTATION / incomplete:** the eight conic-plus-quartic
  families are being tested with actual contact and conductor data.
  Some necessary finite delta exceptions have been derived in one type;
  no whole eight-family exclusion is accepted yet.

## Continuation priorities and open boundary

First complete the two new audits and preserve their full failed/successful
execution histories. Then resolve the retained common-root and A4
cotangent loci using the denominator-free target-fiber equations, the
eight conic families, the cubic-pair cases and actual higher contact or
conductor membership. Do not infer later contact bounds from tangent data,
nor infer conductor rank two from total degrees ten and five. Split
root-of-unity phases and nonreduced generic conductor algebras require
actual algebra, even when a particular stratum eventually excludes them.

Normal quintics, other nonnormal quintic normalization genera, higher
minimum carrier degrees, entirely thick presentations, the retained
split-sextic boundary and distinct common-ancestor incidence remain open.
The 308 necessary numerical profiles for `(5,8)` are not 308 realized
geometries and are not a degree-pair exclusion. Closing this genus-one
quintic lane would still leave the unrestricted fixed-C0 and universal
questions unresolved.

At this observation HEAD is `0adab2bd188351a77d961d7f2251c21545aaebcc` on
`research/ultra-resume-2026-10-06`. New work is retained in the working
tree. Root has made no Git mutation for this rundown. The older canonical
files still describe the sealed checkpoint; this note explicitly records
the post-seal extension pending the next consolidated acceptance and seal.
