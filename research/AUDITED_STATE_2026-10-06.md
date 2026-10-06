# Canonical audited state — 2026-10-06

This file is the authoritative mathematical status for continuation after the 2026-10-06 branch audit and consolidation. Where an older handoff, research-record entry, scratch calculation, or frontier recommendation conflicts with this file, this file controls. Historical notes remain useful for provenance.

## Epistemic standard

- **PROVED**: argument independently audited and accepted under its stated hypotheses.
- **EXACT REDUCTION / CERTIFICATE**: exact computation or finite reduction, but not by itself a general exclusion.
- **OPEN**: an explicit gap or surviving family remains.
- **SUPERSEDED / FALSE**: do not use as a premise.

## A. Uniform order-one structure — PROVED

For a quartic carrier in a characteristic-zero STCI presentation supported on a smooth rational quartic, the generic normal order is one and the BF structure is quasiprimitive. Writing the first quotient as
\[
L=O_{P^1}(e-7),
\]
effectivity and Gorenstein BF duality force
\[
0\le e\le2.
\]
Uniform early-defect bounds are:
- e=0: 1 <= deg D2 <= 5 and deg D3 <= 8;
- e=1: 0 <= deg D2 <= 3 and deg D3 <= 5;
- e=2: 0 <= deg D2 <= 1 and deg D3 <= 2.

For arbitrary carrier degrees a,b >= 4 with at least one equation of generic normal order one:
\[
0\le e\le6,
\]
with uniform bounds on D2,D3 as recorded in `notes/2026-10-06-uniform-order-one-frontier.md`. The order-one carrier also satisfies
\[
16/a\le7-e.
\]
These results do not cover the entirely-thick branch where both equations have generic normal order at least two.

## B. Primitive e=2 quartic branch — PROVED under stated hypotheses

For the fixed monomial rational quartic C0, the universal fourth-obstruction calculation and independent quartic-contact audit give:
1. the reduced basepoint-free fourth-obstruction zero locus is exactly the stated linear locus in the quadratic quotient parameters;
2. on that locus the canonical primitive triple has a distinguished cubic T;
3.
\[
H^0(I_{C_3}(4))=T\,H^0(O_{P^3}(1)).
\]

Consequently the e=2 branches of (4,7) and (4,8) are excluded: any defining quartic factors as T times a linear form, and the plane factor forces extra set-theoretic intersection with any mate.

This supersedes the older frontier language that treated the full e=2 quartic-carrier branch as still awaiting unrestricted P-044 classification.

Scope: this does not exclude e=0 or e=1, does not prove C0 is not STCI, and does not address the entirely-thick branch.

## C. Local-cohomology quartic route

**PROVED / exact:** finite principal-part reduction to the order-four stage; exact 74x18 multiplier tensor/incidence specification; direction bound e<=2 for a surviving quartic ancestor; exact first-conormal quartic-symbol image; ruling-ratio, pure constant-direction, and normalized parity-family exclusions; conditional generic-length/curvilinear conclusions under the proved finite-bound hypotheses.

**OPEN:** the full bilinear quartic incidence problem, including the general e=2 incidence charts. Retained chart notes are reductions, not exclusions.

Known faulty historical scripts `localcoh-symbol-paritycheck.m2` and `localcoh-symbol-seedcheck.m2` are not part of this consolidation and must not be used as certificates.

## D. Normal quartic carriers

**PROVED exclusions:** normal quartics with only rational singularities; positive-genus ruled irrational normal quartics; the case where C avoids the nonrational exceptional anticanonical locus; simple-elliptic nonrational singularities.

**OPEN but finitely compressed:** rational-resolution Ishii–Nakayama B1/B2/B3/D cases with reducible, singular, or nonreduced exceptional anticanonical divisor. The denominator argument gives a finite mate-degree bound, at most 13824 in the coarsest row. This is a bound, not an exclusion.

The numerical normal-sheaf inequality used here is proved under generic regularity and does not require global normality along C.

## E. Multiplicity-six / MF6 structure

For a saturated quasiprimitive rank-six finite-flat lci/Gorenstein thickening:
\[
D_i+D_{5-i}=D_5,\qquad D_4=D_5=D_2+D_3,qquad 0\le D_2\le D_3,
\]
and the first-normal pole divisor satisfies the audited intrinsic identity recorded in `notes/2026-10-05-mf6-pairing-audit.md`.

For e=0, deg D2 >= 3. The (d2,d3)=(3,6) nonregular branch is excluded; any survivor there has regular first-normal ratio. The (4,5) defect type remains OPEN on an exceptional incidence locus.

## F. Split-carrier reductions

The retained split-[4] and split-[2,2] notes are exact reductions, not complete exclusions. In particular the totally ramified [2,2] analysis reduces the surviving locus to an explicit one-parameter family; that family remains OPEN. Scratch exploration was intentionally not promoted.

## G. dx=1 / P-044 local audit — EXACTLY CLOSED ON THIS SLICE

The previously open residual saturation gap has now been closed by an exact Macaulay2 saturation/unit-ideal certificate. On the basepoint-free residual open set, the full P-044 ideal saturates to the unit ideal; the stored computation reports `full P044 residual unit: true` and verifies an explicit membership certificate with exponent 2. Together with the already-audited boundary calculation, this proves that the basepoint-free P-044 locus on the dx=1 slice is exactly the P-045 family.

This is a slice classification, not a new global exclusion theorem; Section B already excludes the relevant quartic e=2 (4,7)/(4,8) branches by the stronger primitive-triple factorization argument.

Certificates: `computations/session_dx1_saturation_2026_10_06.m2`, its recorded output, the compact colon certificate, and `computations/verify_session_dx1_independent_2026_10_06.py`.

## H. Current global frontier

The repository does **not** prove that the smooth rational quartic is not STCI.

The firm decomposition is:
1. **order-one branch:** uniformly bounded first-direction/early-defect geometry, with the quartic e=2 branch excluded and substantial e=0/e=1/normal/local-cohomology reductions;
2. **entirely-thick branch:** separate and still open; first-symbol/tangent-form data alone are insufficient.

No new research direction is prescribed by this consolidation. The purpose of this file is to give a stable, audited base for future work.

## I. Entirely-thick numerical restriction — PROVED NECESSARY CONDITION

For a smooth rational quartic C on its smooth quadric, let two defining surfaces of degrees a,b have exact generic normal orders p,q. On the blowup of P3 along C, effectivity of the proper intersection cycle on the exceptional P1xP1 gives

\[
ab\ge 4pq,\qquad 7ab+28pq\ge16(aq+bp).
\]

The quadric restriction also gives a>=3p and b>=3q. In normalized variables alpha=a/p, beta=b/q, the second inequality is

\[
7\alpha\beta/4+7\ge4(\alpha+\beta),\qquad \alpha,\beta\ge3.
\]

Hence alpha=3 forces beta>=4 and symmetrically; in particular the simultaneous boundary a=3p,b=3q is excluded for all p,q. On the equality boundary a=3p,b=4q, the intersection cycle is a sum of constant sections and the residual ruling divisor is forced into a repeated-root configuration as detailed in `notes/2026-10-06-session-thick-independent-audit.md`. This is a restriction, not an exclusion of the entirely-thick branch.

## J. Normalization/conductor support criterion — PROVED UNDER STATED HYPOTHESES

For an integral carrier X with finite normalization nu:S->X and W=(nu^{-1}(C))_red, an STCI mate on X forces W to be the support of an effective Cartier divisor; in particular an isolated point in the full inverse image W excludes every mate on that fixed carrier.

If all nonnormality of X is supported on C, then existence of some STCI mate on X is equivalent to existence of an effective Cartier divisor A on S with |A|=W and O_S(A)=O_S(bH) for some b>0. A power of the canonical section descends through the conductor, so no additional asymptotic conductor obstruction remains in this support-contained case. This is carrier-specific and does not produce the required Cartier divisor or linear equivalence.

See `notes/2026-10-06-session-conductor-support.md`.

## K. Structural jet-geometry supplement — RETAINED, NOT A NEW EXCLUSION

The side-thread quartic jet analysis gives useful geometric interpretations of successive primitive restriction maps: the first-normal codimension-three obstruction on the quadric, the divisor R measuring comparison of conormal directions, a description of the first-order source as sections through R, and localization of the second-order target on 2R. It also motivates a general “jet-condition budget” program in which negative expected budget forces degeneracy of successive restriction maps rather than directly proving nonexistence.

These structural observations are retained in `notes/2026-10-06-quartic-jet-geometry-structural-supplement.md`. Any statements in the original side-thread text treating (4,7),e=2 as open are superseded by Section B above.

## Consolidation provenance

Integration branch: `research/consolidate-2026-10-06`, created from main commit `c7551a94a063933784f6b421e1a3fc9682d25874`.

Material was selectively reconstructed from `ultra_mode` and `research/local-audit-e2`; neither branch was merged wholesale. Exploratory scratch, known-faulty certificates, and unsupported stronger conclusions were intentionally omitted.
