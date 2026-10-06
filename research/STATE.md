# Canonical research state

This is the durable entry point for claims currently regarded as established in the STCI project. It replaces dated handoffs and reports as the place to determine current status. Git history and the archived dated state preserve provenance.

## Epistemic labels

- **PROVED** — mathematical argument accepted under its stated hypotheses.
- **EXACT REDUCTION / CERTIFICATE** — exact finite reduction or computation whose scope is explicitly limited.
- **CONDITIONAL** — proved assuming the hypotheses named in the statement.
- **OPEN** — a genuine surviving case or missing implication remains.
- **SUPERSEDED / FALSE** — retained only for provenance and must not be used as a current premise.
- **NEEDS RE-AUDIT** — evidence exists but is not yet promoted to the canonical state.

## Global status

The repository does **not** prove that the characteristic-zero smooth rational quartic is not a set-theoretic complete intersection. The present frontier splits into an order-one branch and a separate entirely-thick branch.

The principal characteristic-zero test curve is
[
C_0=[s^4:s^3t:st^3:t^4]subset mathbf P^3.
]

## Order-one structure — PROVED

For a quartic carrier whose generic normal order is one, the BF structure is quasiprimitive. Writing the first quotient as (L=O_{mathbf P^1}(e-7)), one has (0le ele2), with the audited early-defect bounds recorded in `notes/2026-10-06-uniform-order-one-frontier.md`.

For arbitrary carrier degrees (a,bge4), if at least one equation has generic normal order one, then (0le ele6), with the corresponding uniform defect bounds and (16/ale7-e). These statements do not cover pairs for which both equations have generic normal order at least two.

## Primitive e=2 quartic results — PROVED in mate degrees 7 and 8

For (C_0), the universal primitive-fourth obstruction and independent quartic-contact audit classify the reduced basepoint-free fourth-obstruction zero locus used in the argument. On that locus the canonical primitive triple lies on a distinguished cubic (T) and
[
H^0(I_{C_3}(4))=T H^0(O_{mathbf P^3}(1)).
]

Therefore the (e=2) branches of ((4,7)) and ((4,8)) are excluded: every containing quartic factors through (T), and the plane factor forces extra set-theoretic intersection with the mate.

This is **not** an exclusion of arbitrary ((4,b)), (e=2) for all larger (b).

## dx=1 / P-044 slice — EXACTLY CLOSED

The formerly open residual saturation gap is closed by the exact Macaulay2 certificate in `computations/session_dx1_saturation_2026_10_06.m2` and its recorded output. Together with the audited boundary calculation, the basepoint-free P-044 locus on the dx=1 slice is exactly P-045.

This is a slice classification, not a global P-044 classification.

## Local cohomology — EXACT FINITE REDUCTION / OPEN

The quartic common-ancestor problem has a finite principal-part reduction to order four, a 30-dimensional ancestor space, and primitive common conormal degree (ele2). Ruling-ratio, pure constant-direction, and several normalized subfamilies are excluded exactly. The full bilinear quartic incidence problem remains open.

## Multiplicity six / MF6 — PARTIAL STRUCTURAL THEOREMS / OPEN

For saturated quasiprimitive rank-six finite-flat lci/Gorenstein thickenings, the audited Gorenstein pairing and defect identities hold. For (e=0), (deg D_2ge3); the ((d_2,d_3)=(3,6)) nonregular branch is excluded. The regular remainder and the exceptional ((4,5)) defect incidence remain open.

## Normal quartic carriers — LARGE CLASSES EXCLUDED / FINITE REMAINDER OPEN

Excluded are normal quartics with only rational singularities, the positive-genus ruled irrational cases, the case in which (C) avoids the nonrational exceptional anticanonical locus, and the simple-elliptic case.

The remaining rational-resolution Ishii–Nakayama B1/B2/B3/D cases have reducible, singular, or nonreduced exceptional anticanonical divisor. Denominator compression bounds the mate degree but does not exclude these cases.

## Split carriers — EXACT REDUCTIONS / OPEN

The split-[4] and split-[2,2] analyses eliminate several strata but not the entire branch. In particular, the totally ramified [2,2] analysis leaves an explicit one-parameter first-normal survivor. It is not an STCI construction.

## Normalization and conductor — PROVED UNDER STATED HYPOTHESES

For an integral carrier (X) with normalization (
u:S	o X), an STCI mate forces the reduced full inverse image of (C) to support an effective Cartier divisor. An isolated point in that full inverse image therefore excludes every mate on the fixed carrier.

When all nonnormality is supported on (C), the audited conductor argument reduces existence of a mate on the fixed carrier to existence of the required effective Cartier divisor with the appropriate hyperplane linear equivalence; no separate asymptotic conductor obstruction remains after taking a power.

## Entirely-thick branch — NECESSARY NUMERICAL RESTRICTIONS / OPEN

If the two equations have exact generic normal orders (p,qge2) and degrees (a,b), the blowup intersection calculation gives
[
abge4pq,qquad 7ab+28pqge16(aq+bp),
]
together with (age3p), (bge3q).

Thus the simultaneous normalized boundary ((a/p,b/q)=(3,3)) is impossible. On the ((3,4)) boundary the exceptional intersection is forced into a repeated-root configuration. These are necessary restrictions, not an exclusion of the entirely-thick branch. First tangent forms alone do not determine the needed transverse intersection length.

## Structural jet geometry — PROVED LEMMAS / OPEN PROGRAM

The quartic jet analysis identifies the divisor measuring comparison of the primitive and quadric conormal directions, describes the first-order source as sections through that divisor, and localizes the next target on its double. This motivates a condition-budget/discrepancy program for detecting geometric dependencies among successive infinitesimal containment conditions. It is a research framework, not yet a general theorem.

## Provenance

The detailed audited snapshot from the 2026-10-06 consolidation remains in `AUDITED_STATE_2026-10-06.md` until the archive migration is complete. Detailed proofs and exact computations remain in the dated notes and `computations/`; future cleanup will organize those by topic without discarding provenance.
