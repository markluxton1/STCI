# Sustained research update — 2026-10-06 through 2026-10-09

This record integrates the interrupted session and its continuation.
The authoritative short frontier is
[AUDITED_STATE_2026-10-07.md](AUDITED_STATE_2026-10-07.md). The universal
integral projective-curve problem and the unrestricted characteristic-zero
question for C0 remain unresolved. Results below retain their carrier,
characteristic, direction and defect hypotheses. Agreement of programs
is evidence for their finite arithmetic scope; the geometric arguments
are supplied separately.

## Reconstruction and corrections

The live checkout was reconstructed from the October 6 audited state,
resume reconciliation, research record, handoff and source files. The
continued checkout is on `research/ultra-resume-2026-10-06`; the retained
interruption snapshot is `3ffda7548a863387429adab61eefe02575e86297`.
Working changes and newly created notes are the current evidence.

Three corrections change how the older frontier must be read:

1. The former broad quartic e=2 exclusion was too strong. The accepted
   primitive-fourth argument excludes (4,7), (4,8), and larger pairs
   with D2=D3=0. Larger early-defect cases remain open.
2. The dx=1 boundary verifier required its x!=0 saturation. Ordinary
   ideal membership in the undivided system was false at x=0. The
   full five-coordinate dx=1 saturation is now proved; the suggested
   three-equation subsystem has residual solutions.
3. A normalization criterion must use the full inverse image of C,
   including isolated points. Those points obstruct every mate on the
   specified carrier. Listing only the curve components loses this
   obstruction.

The [validation record](notes/2026-10-06-session-validation.md) retains
failed outputs, repaired claims, exact source hashes and generated data.
The [support theorem](notes/2026-10-06-session-conductor-support.md)
repairs the historical P-032 notation directly.

## Accepted carrier theorem: no normal quartic for C0

For fixed C0=[s^4:s^3t:st^3:t^4] over any algebraically closed field of
characteristic zero, no integral normal quartic surface has a mate
cutting out C0 set-theoretically. The mate degree is unrestricted.

The proof uses the published Ishii–Nakayama classification and the
previously audited ADE, rational-resolution compression, normal-bundle
and low-degree exclusions. A smooth embedded curve meets exactly one
exceptional prime transversely at each singular point. On a rational
resolution, with K=-E, d=-E^2 and t=c.E, the mate relation and adjunction
give t+q=6, q=m^T A^-1 m, and t^2<=d(6-t). Integral equality cases
compress to impossible plane mates.

Irreducible E is excluded by the exact harmonic ADE bound. Reduced
reducible E is an exhausted cycle family: four numerical rows compress
to quadric mates, while the last would require normal-sheaf defect 10/3
when only three is available. For nonreduced E, every proper effective
subdivisor has H1=0. The support is therefore a rational SNC tree, and
the canonical coefficient equations reduce it to a finite graph problem.

Two implementations with different tree and linear-algebra
representations test 381802 diagonal modifications, retain 195 positive
integral canonical cycles, and leave twelve numerical rows after
compressed mate exclusions. Every row has d=3,t=2. In the published
Type-D hyperplane basis, the three sections through the irrational
point factor as the full section of E times basepoint-free plane
coordinates. Hence m_p O_M=O_M(-E); restriction to a smooth curve
forces t=1. All twelve rows are excluded. No realizability claim for
the numerically retained graphs is needed.

Proof and independent evidence:

- [Full normal-carrier proof](notes/2026-10-06-session-normal-carrier-progress.md),
  including characteristic-zero coefficient descent.
- [Independent reduced-cycle audit](notes/2026-10-07-session-normal-carrier-independent-audit.md).
- [Independent nonreduced-tree and Type-D audit](notes/2026-10-07-session-normal-nonreduced-independent-audit.md).
- [First exact tree verifier](computations/verify_session_normal_nonreduced_trees.py)
  and [independent verifier](computations/verify_session_nonreduced_independent_audit.py).

Nonnormal quartics and all higher minimum carrier degrees remain open.
The old bounds 1536,4608,13824 were denominator reductions, not proofs
of nonexistence; the present theorem closes their normal quartic scope.

## Accepted MF6 exclusion and the primitive e=1 audit

The full e=0,(d2,d3)=(4,5) mixed (4,6) type is excluded. The proof uses
the actual moving support coordinate through cubic order. A global
degree-one annihilator of the excess defect imposes four infinity
compatibility coefficients. Their full minor ideal forces the sole
parameter (A,B)=(12,4), including every rank-drop and repeated-root
case. The entire quartic fiber there is a fixed cubic times all linear
forms, so every carrier has an incompatible plane factor.

The [proof](notes/2026-10-06-session-mf6-progress.md) and
[universal verifier](computations/verify_mf6_infinity_universal.py)
include direct polynomial minor-membership witnesses and the full
exceptional fiber. The changed self-contained source passed a fresh
rerun; old generic calculations alone were not used to establish this.

The [primitive e=1 audit](notes/2026-10-07-session-mf6-e1-independent-audit.md)
now proves a stronger all-degree theorem: no quartic STCI carrier with
L=O(-6) and D2=0 exists on C0. The four complete primitive direction
orbits and their full quartic fibers either force a quadric factor or
give cubic pole bounds. The uniform quartic BF bound d3<=5 leaves
four pure pencil carriers. Their finite birational affine normalizations
are planes, with full C0 inverse image a diagonal. Equality of a mate
pullback on two points of one normalization fiber forces
(-kappa)^n=1, but kappa has quadratic-field norm 1/3. The
[separate normalization audit](notes/2026-10-07-session-nonnormal-mf6-independent-audit.md)
and [self-contained 35-column ambient verifier](computations/audit_mf6_e1_primitive_2026_10_07.py)
check the scope independently. This excludes MF6 type (0,4), while
types (1,3),(2,2) and the e=0 (3,6) regular-ratio residual remain open.

## Local-cohomology progress

The actual 74-by-18 multiplication tensor was regenerated and its
coordinate hashes agree byte-for-byte with the retained certificates.
Polynomial duals exclude all lower lifts of the three primitive corner
directions with top coefficient h=t,r(0)=0. The raw xz,yw numerators
are not a basepoint-free pencil; cancellation by the local Jacobian
normalizes the socle targets to (s^2,t^2).

That socle pencil forces E3=O(-14) in a surviving finite-flat CM
quadruple and gives deg D3=7-3e. In particular the e=2 defect types
are exactly (0,1) and (1,1). Explicit flat local CI and non-Gorenstein
models show why a defective triple or a (1,2,1) special fiber cannot
be discarded. They are local controls, not embedded STCI examples.

The h=t endpoint direction classification is complete: after the
excluded corners and reversed parity case, four one-parameter
direction families remain, each with one lower lift parameter. For
the first rational family, a saved polynomial dual excludes every
lower lift away from explicitly recorded finite parameter factors.
The independently checked quadratic and first quartic exception duals
now close all 23 admissible geometric exception points for every lower
lift. The first rational family is therefore completely excluded.
The second rational family now has a complete generic dual, with exactly
26 primitive exceptional points in the original denominator partition.
Both quadratic factors are now excluded at all four geometric roots,
for every lower parameter, by independently checked polynomial duals.
The remaining 22 points have factors of degrees 3,4,15 and retain their
full affine lower lift fibres. The two boundary families
and top zeros outside the endpoints remain open. The
[independent endpoint audit](notes/2026-10-07-session-localcoh-independent-audit.md)
and [Q1 closure](notes/2026-10-07-session-localcoh-q1-exception.md) give
the exact fields, complete lift lines and all-column identities.
The [October 8 completeness audit](notes/2026-10-08-session-first-endpoint-completeness-audit.md)
checks every exceptional field against the original rational sources;
the [second-family note](notes/2026-10-08-session-localcoh-family2-generic.md)
records the original factor partition. The current
[two-quadratic closure](notes/2026-10-08-session-localcoh-family2-quadratics.md)
and [independent audit](notes/2026-10-08-session-localcoh-family2-quadratic-independent-audit.md)
include a separate exact-field implementation and fresh literal
reconstruction of the complete actual multiplication tensor.

A separate [simultaneous-target proof](notes/2026-10-07-session-localcoh-e1-simultaneous.md)
excludes the primitive e=1,D2=0 common-quartic-ancestor lane. It retains
the nonzero socle targets in the equations f_i=h_i*a-T_i*tau. The
principal pencil contradicts the basepoint-free target values at two
points; the algebraic pencils contradict the global degree-four bound
on tau. The prior proposed single-multiplier pole argument is
[retracted and preserved](notes/2026-10-07-session-localcoh-mf6-bridge.md),
because it incorrectly replaced the target equation by annihilation.
The corrected result passed a separate audit of the global normal and
socle frames. The entire e=1,d2=1 ancestor lane is now also excluded:
the exact principal contact rank theorem and complete projective
complement join the six accepted endpoint exclusions. The node has
dimension four with a common cubic and reduces to P-037; the other
fibres have dimension one. The genuine infinity defect and all b0=0
conjugates are retained. See the
[independent completeness audit](notes/2026-10-08-session-principal-e1-d1-independent-completeness-audit.md).
The surviving e=1 ancestor degrees are d2=2,3,4 with their separate
direction exclusions. A unique quartic carrier may still require a
different all-mate argument.
The [intrinsic generator-bundle theorem](notes/2026-10-07-session-localcoh-conormal-splitting.md)
now imposes `V(4)=O(2)+O(2e+2)` on every quartic ancestor, with exact
connecting-matrix ranks for the retained defect strata. The six degree-one
endpoint triples and the quadric direction in every second defect are
also separately excluded in the ancestor problem by their actual
multiplier spaces. No STCI BF bound is imported to discard d2=4.

See the [proof, complete endpoint formulas and exception factors](notes/2026-10-06-session-localcoh-progress.md),
[corner verifier](computations/session-localcoh-corners.py), and
[generic polynomial-dual verifier](computations/session-localcoh-origin-generic-dual.py).
The quartic incidence is not a non-quasi-cyclicity theorem, and there
is no multiplier-degree upper bound for the unrestricted problem.

## Uniform, thick and conductor results

The independent uniform audit verifies the saturated BF Gorenstein
pairings by a direct DVR Frobenius argument, and retains the distinction
between saturated filtration ideals and ordinary powers. It supplies
the degree product inequalities for horizontal e=3,4,5,6 and exact
necessary e=2 profiles at mate degrees 9,10,11. The first possible
fourth obstruction must have a degree-one annihilator in those degrees;
its simultaneous ambient-quartic incidence remains open.

For an entirely-thick pair on a smooth rational quartic, with generic
normal orders p,q, the independently audited curve blowup gives

    a>=3p, b>=3q, ab>=4pq,
    7ab+28pq>=16(aq+bp).

In particular a=3p forces b>=4q. The equality cycle is supported on
constant normal-direction sections and imposes a repeated-root
condition. The proof retains vertical components and arbitrary higher
tangent contact; the high-ratio region remains open.

If all normalization defect of an integral carrier is supported on C,
the existence of a positive Cartier divisor with full inverse-image
support and the required hyperplane linear equivalence is sufficient
for some mate degree. A high canonical-section power enters the
conductor and descends. This works in every characteristic; it removes
only that asymptotic descent obligation, not divisor existence or its
linear equivalence.

Proofs: [uniform audit](notes/2026-10-06-session-uniform-audit.md),
[thick blowup audit](notes/2026-10-06-session-thick-independent-audit.md),
and [conductor criterion](notes/2026-10-06-session-conductor-support.md).

## October 8 nonnormal carrier theorems

Every integral quartic normalized by `(P2,O(2))` is now excluded as a
carrier of any smooth rational quartic in characteristic zero, with any
mate degree. The proof exhausts all projection centers by direct
three-dimensional self-adjoint linear algebra and the primitive adjugate
argument. Roman, Jordan2 and Jordan3 are all excluded. The last case
needs the first conductor jet: reduced normalization fibers alone would
permit a conic, but no positive conic power descends to the original ring.
This includes non-slc degenerations, and supersedes the earlier
ordinary/slc-only exclusion in this precise normalization lane.

Every integral quartic singular along a smooth twisted cubic is also
excluded as a carrier of fixed C0 in characteristic zero, in every
mate degree. The entire equation space is verified to be the six
quadratic products of the cubic's three defining quadrics. Its smooth
conic/blowup model gives a finite smooth-scroll normalization. Finite
duality, CM purity and polynomial 3m+1 identify the actual downstairs
conductor with the reduced smooth cubic and make its upstairs cover
finite flat of rank two. Integral, reducible and nonreduced upstairs
conductors are all covered by the descent/contact argument. See the
[applicability theorem](notes/2026-10-08-session-scroll-conductor-applicability.md)
and [root acceptance](notes/2026-10-08-session-new-results-acceptance.md).
The geometric exclusion now covers **every integral quartic with smooth
rational quartic-scroll normalization**, in every mate degree for fixed
C0 in characteristic zero. It retains both entire conductor schemes,
including nonreduced nongorenstein ACM cubics. The exact generic
canonical modules force divisible-by-three or even conductor
multiplicities for the two triple-line types. The new differential
lemma differentiates the entire mate power equation and rules out
generic rank-one conductor primes meeting the smooth lift. Together
with the F0/F2 anticanonical classes, singleton fibres and ramification,
this exhausts all remaining conductor patterns. No global trace is
assumed at a nongorenstein vertex. See the
[classification](notes/2026-10-08-session-scroll-nongorenstein-cubic-classification.md),
[exact Artin audit](notes/2026-10-08-session-scroll-artin-independent-audit.md),
[full independent audit](notes/2026-10-08-session-scroll-nongorenstein-independent-audit.md)
and [root reconciliation](notes/2026-10-08-session-late-results-acceptance.md).
Other smooth polarization classes, singular normalizations and higher
carrier degrees remain open; the theorem is not a classification of
every nonnormal quartic normalization.

Both algebraic e=1,d2=4 ancestor directions now have complete quartic
fibers of dimension at most one, uniformly over all homogeneous defect
sections. The exact minor cover includes repeated and infinity roots.
The principal obstruction-zero and obstruction-nonzero directions remain
open. The principal e=1,d2=1 candidate direction curve has been
compressed to an elliptic Weierstrass model with j=2048/3. Its complete
quartic rank theorem and omitted charts are now closed for ancestors.
Every complement carrier is also excluded in all mate degrees. The
principal carrier problem reduces to a finite proper closed nonnormal
subset of that integral curve; its exact enumeration remains open.

The [October 8 checkpoint](notes/2026-10-08-session-checkpoint.md)
preserves these proofs, historical interruptions and exact next
boundaries. The [late acceptance record](notes/2026-10-08-session-late-results-acceptance.md)
gives the completed proofs and current scope. The
[reconciled validation index](validation/2026-10-08-continuation-index/index.json)
counts 91 distinct top-level sources with latest PASS records and 103
explicitly indexed executions. It retains both continuation failures
and their repairs, and openly records one superseded source-byte loss
caused by the now-fixed repeated-copy behavior of the snapshot driver.
The [full proof](notes/2026-10-07-session-veronese-pencil-classification.md)
and [independent audit](notes/2026-10-08-session-veronese-allmate-independent-audit.md)
retain every fiber, global-unit and characteristic hypothesis.

## Literature and next actions

The [literature refresh](notes/2026-10-06-session-literature-refresh.md)
found no accepted unrestricted resolution. It records the exact false
prime/maximal step in the preprint claiming a negative resolution and
the failed quotient-module step in a broad affine preprint. These
failures do not prove the opposite theorem. The primary checked
Robbiano–Valla theorem is for ACM monomial curves; the arbitrary ACM
survey assertion remains unverified from its original source chain.

The most valuable remaining directions are structural:

1. Determine the finite remaining principal e=1,d2=1 carrier locus,
   using the saved weighted polynomial kernel and actual higher jets.
   The ancestor problem at d2=1 is closed; the unique-carrier mate
   problem remains. Continue the d2=2 incidence and e=0 (3,6) residual.
   The [intrinsic defective-triple reduction](notes/2026-10-07-session-mf6-e1-defective-structural.md)
   identifies the correct cubic-class twist, a five-by-three quadratic
   annihilator for (1,3), five vanishing coefficients for (2,2), the
   preceding sextic direction locus and six exact endpoint triples.
2. The normal, (P2,O(2)) and smooth rational quartic-scroll carrier
   classes are excluded. Investigate the other smooth polarization
   classes and singular normalizations with full inverse-image support.
   Preserve the semi-log-canonical restriction in modern classification
   summaries; do not import the scroll ACM conductor classification
   as a classification of all quartic surfaces.
3. Exhaust the four endpoint local-cohomology direction families
   using exact module duals plus their full exceptional loci, then
   address top zeros outside the endpoints.
4. Retain the early-defect e=2 fourth obstruction, the entirely-thick
   high-ratio region, higher-degree order-one carriers and the
   ramified split-sextic boundary as genuine open work.

The [dated handoff](SUCCESSOR_HANDOFF_2026-10-07.md) specifies how to
resume these lanes without repeating completed validation or reviving
superseded claims.
