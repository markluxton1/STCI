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

The repository does **not** prove that the characteristic-zero smooth rational quartic is not a set-theoretic complete intersection. The remaining work includes order-one and entirely-thick structural questions and higher-degree carrier families. Quartic STCI-mate cases are closed as recorded below.

The principal characteristic-zero test curve is
\[
C_0=[s^4:s^3t:st^3:t^4]\subset \mathbf P^3.
\]

## Integral quartic carriers of the fixed C0 — PROVED EXCLUDED

Canonical theorem: [STCI-R-0001](results/quartic_carrier_exclusion.md). Over an algebraically closed field of characteristic zero, **no integral quartic surface containing this fixed C0 has a mate of any positive degree**. The accepted October 11 assembly and independent audit cover normal and nonnormal carriers and arbitrary mate degree. Together with the plane, quadric, cubic exclusions and the audited factor reduction, **both defining degrees of a hypothetical STCI presentation are at least five**. The unrestricted characteristic-zero STCI question remains open.

The older partial quartic-mate analyses below remain valid **as historical intermediate results**, but any description of a quartic-mate case as still open is superseded by STCI-R-0001. Common-quartic local-cohomology ancestor incidence is a different problem and remains open.

## Cartier singleton lifts on normalizations — PROVED UNDER STATED HYPOTHESES

[STCI-R-0002](results/cartier_singleton_lift.md) classifies the normalization of a mate-admitting integral carrier when the full reduced inverse image of a smooth rational curve is **one Cartier curve mapping isomorphically to it**. For fixed C0, the remaining necessary models in this restricted class have degree 8 (smooth quadric or quadric cone normalization) or 16 (plane normalization). Their actual projections and conductor descent are **open**; see [STCI-Q-0001](questions/cartier_projection_models.md). This is not an all-carrier classification.

## Full-conductor fixed-carrier criterion — PROVED UNDER STATED HYPOTHESES

[STCI-R-0003](results/fixed_carrier_conductor_criterion.md) gives an exact criterion on an integral Cohen–Macaulay projective carrier with finite normalization, in **any characteristic**: the full inverse support must have no isolated points, and the Cartier-relation lattice must contain a vector positive on all inverse branches whose off-curve full-conductor unit classes are torsion. For hypersurface carriers this is equivalent to an ambient mate on that **fixed** carrier. The finite lattice reduction is abstract; it does not compute class groups or conductor descent for all carriers.

## Projection-family torsion-coset reduction — PROVED UNDER STATED HYPOTHESES

[STCI-R-0004](results/projection_phase_reduction.md) reduces the all-mate-degree problem in fixed Cartier singleton projection families to full-conductor phase tuples and torsion in a finite-dimensional torus. It preserves nilpotent defects and admissibility boundaries. The phase images and torsion cosets of the three fixed-C0 models **have not been computed**, so the existence question remains open.

## Order-one structure — PROVED

Topic synthesis: [results/order_one.md](results/order_one.md)

For a quartic carrier whose generic normal order is one, the BF structure is quasiprimitive. Writing the first quotient as \(L=O_{\mathbf P^1}(e-7)\), one has \(0\le e\le2\), with the audited early-defect bounds recorded in \`notes/2026-10-06-uniform-order-one-frontier.md\`.

For arbitrary carrier degrees \(a,b\ge4\), if at least one equation has generic normal order one, then \(0\le e\le6\), with the corresponding uniform defect bounds and \(16/a\le7-e\). These statements do not cover pairs for which both equations have generic normal order at least two.

## Primitive e=2 quartic results — PROVED in mate degrees 7 and 8

Topic synthesis: [results/quartic_e2.md](results/quartic_e2.md)

For \(C_0\), the universal primitive-fourth obstruction and independent quartic-contact audit classify the reduced basepoint-free fourth-obstruction zero locus used in the argument. On that locus the canonical primitive triple lies on a distinguished cubic \(T\) and
\[
H^0(I_{C_3}(4))=T H^0(O_{\mathbf P^3}(1)).
\]

Therefore the \(e=2\) branches of \((4,7)\) and \((4,8)\) are excluded: every containing quartic factors through \(T\), and the plane factor forces extra set-theoretic intersection with the mate.

**Historical scope note:** this partial argument alone did not exclude larger mate degrees; the later complete theorem [STCI-R-0001](results/quartic_carrier_exclusion.md) does.

## dx=1 / P-044 slice — EXACTLY CLOSED

The formerly open residual saturation gap is closed by the exact Macaulay2 certificate in \`computations/session_dx1_saturation_2026_10_06.m2\` and its recorded output. Together with the audited boundary calculation, the basepoint-free P-044 locus on the dx=1 slice is exactly P-045.

This is a slice classification, not a global P-044 classification.

## Local cohomology — EXACT FINITE REDUCTION / OPEN

The quartic common-ancestor problem has a finite principal-part reduction to order four, a 30-dimensional ancestor space, and primitive common conormal degree \(e\le2\). Ruling-ratio, pure constant-direction, and several normalized subfamilies are excluded exactly. The full bilinear quartic incidence problem remains open.

## Multiplicity six / MF6 — PARTIAL STRUCTURAL THEOREMS / OPEN

For saturated quasiprimitive rank-six finite-flat lci/Gorenstein thickenings, the audited Gorenstein pairing and defect identities hold. For \(e=0\), \(\deg D_2\ge3\); the \((d_2,d_3)=(3,6)\) nonregular branch is excluded. The regular remainder and exceptional \((4,5)\) defect incidence remain as structural or ancestor investigations; **they are not open quartic STCI-mate cases** after [STCI-R-0001](results/quartic_carrier_exclusion.md).

## Normal quartic carriers — HISTORICAL PARTIAL CLASSIFICATION; MATE CASES CLOSED

Topic synthesis: [results/normal_carriers.md](results/normal_carriers.md)

Excluded are normal quartics with only rational singularities, the positive-genus ruled irrational cases, the case in which \(C\) avoids the nonrational exceptional anticanonical locus, and the simple-elliptic case.

The remaining rational-resolution Ishii–Nakayama B1/B2/B3/D cases have reducible, singular, or nonreduced exceptional anticanonical divisor. This historical partial argument did not exclude those cases. The subsequent all-integral-quartic theorem [STCI-R-0001](results/quartic_carrier_exclusion.md) excludes every normal quartic **as an STCI carrier with a mate**; the earlier classification and bounds remain evidence.

## Split carriers — EXACT REDUCTIONS / OPEN

The split-[4] and split-[2,2] analyses eliminate several strata but not the entire branch. In particular, the totally ramified [2,2] analysis leaves an explicit one-parameter first-normal survivor. It is not an STCI construction.

## Normalization and conductor — PROVED UNDER STATED HYPOTHESES

Topic synthesis: [results/normalization_conductor.md](results/normalization_conductor.md)

For an integral carrier \(X\) with normalization \(\nu:S\to X\), an STCI mate forces the reduced full inverse image of \(C\) to support an effective Cartier divisor. An isolated point in that full inverse image therefore excludes every mate on the fixed carrier.

When all nonnormality is supported on \(C\), the audited conductor argument reduces existence of a mate on the fixed carrier to existence of the required effective Cartier divisor with the appropriate hyperplane linear equivalence; no separate asymptotic conductor obstruction remains after taking a power.

## Entirely-thick branch — NECESSARY NUMERICAL RESTRICTIONS / OPEN

Topic synthesis: [results/entirely_thick.md](results/entirely_thick.md)

If the two equations have exact generic normal orders \(p,q\ge2\) and degrees \(a,b\), the blowup intersection calculation gives
\[
ab\ge4pq,\qquad 7ab+28pq\ge16(aq+bp),
\]
together with \(a\ge3p\), \(b\ge3q\).

Thus the simultaneous normalized boundary \((a/p,b/q)=(3,3)\) is impossible. On the \((3,4)\) boundary the exceptional intersection is forced into a repeated-root configuration. These are necessary restrictions, not an exclusion of the entirely-thick branch. First tangent forms alone do not determine the needed transverse intersection length.

## Structural jet geometry — PROVED LEMMAS / OPEN PROGRAM

Topic synthesis: [results/jet_geometry.md](results/jet_geometry.md)

The quartic jet analysis identifies the divisor measuring comparison of the primitive and quadric conormal directions, describes the first-order source as sections through that divisor, and localizes the next target on its double. This motivates a condition-budget/discrepancy program for detecting geometric dependencies among successive infinitesimal containment conditions. It is a research framework, not yet a general theorem.

## Provenance

The dated audited snapshot from the 2026-10-06 consolidation is preserved at [archive/reports/AUDITED_STATE_2026-10-06.md](archive/reports/AUDITED_STATE_2026-10-06.md). Detailed proofs and exact computations remain in the dated notes and `computations/`; the durable current authority is this file together with `FRONTIER.md` for active priorities.
