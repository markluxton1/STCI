# Latest-pause rundown: October 11, after the all-quartic seal

This is a status snapshot for the user's request for a rundown. It is not a
new mathematical verifier or a replacement for a proof acceptance. The
universal integral-projective-curve STCI problem and the unrestricted
characteristic-zero question for
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN** in this investigation.

## Accepted and sealed milestone

The [all-quartic acceptance](2026-10-11-session-all-quartic-results-acceptance.md)
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

The frozen [quintic frontier](2026-10-11-session-quintic-structural-frontier.md)
and its [independent audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
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

The [multiplicity-ten filtration](2026-10-11-session-multiplicity-ten-filtration-audit.md)
leaves 308 necessary numerical profiles for (5,8). They are not realized
structures, a classification of all embedded structures, or an exclusion.

## New work after the seal

1. The [intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
   and [explicit-model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md)
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
3. The [power-descent algebra audit](2026-10-11-session-power-descent-algebra-audit.md)
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
   The [a=0,b!=0 proof](2026-10-11-session-quintic-endpoint-a0-support-exclusion.md)
   now has a completed [independent full audit](2026-10-11-session-quintic-endpoint-a0-polynomial-support-independent-audit.md).
   It proves that every displayed parameter choice has an actual off-c
   inverse point over C0. Thus every admissible projection in this subfamily
   is excluded in every mate degree. The owner's historical pending header
   is superseded, for this bounded claim, by the completed audit.
5. For endpoint a!=0, the [quadric-factor reduction](2026-10-11-session-quintic-endpoint-quadric-factor-reduction.md)
   has a completed [independent audit](2026-10-11-session-quintic-endpoint-factor-independent-audit.md)
   and separate [contact-length audit](2026-10-11-session-quintic-endpoint-factor-contact-independent-audit.md).
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
