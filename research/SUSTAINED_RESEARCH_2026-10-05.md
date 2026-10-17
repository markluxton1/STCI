# Sustained STCI research: resumed 2026-10-05

This is the entry point for the resumed goal-directed research after commit
`a454b3b`. It supplements the earlier same-day update rather than replacing
the historical record. The universal integral-curve question and the
unrestricted characteristic-zero C0 question remain **OPEN**.

## Target and verified baseline

For every algebraically closed field k and every integral curve
C in P3_k, decide whether two homogeneous forms have saturated radical I_C.
The characteristic-zero laboratory is

    C0=[s^4:s^3t:st^3:t^4], I=(q,A,B,D),
    q=x0*x3-x1*x2,
    A=x0^2*x2-x1^3, B=x0*x2^2-x1^2*x3,
    D=x2^3-x1*x3^2.

The current checkout was reconstructed from README, RESEARCH_RECORD,
RESEARCH_REPORT, SUCCESSOR_HANDOFF, the earlier dated update, the literature
ledger, and their notes and exact companions. Older work in another checkout
was used only for the methodological higher-jet guardrail; its state files or
results were not substituted for this checkout's evidence.

All 22 existing Python verification executions passed again, as did the two
Macaulay2 companions. The full Python outputs and timings are preserved in
`computations/validation_2026-10-05_resumed.json`. The existing temporary
SymPy environment and Homebrew M2 were available; no environment installation
was required. These checks corroborate their encoded exact systems and do
not independently establish unencoded geometric exhaustion hypotheses.

## Independently verified results in the resumed phase

### R-001: foundational reductions and source boundary

Status: **AUDITED**. The complement-morphism criterion P-029, the
height-two homogeneous Gorenstein-primary criterion P-035, the uniform
ordinary/symbolic power equality on smooth quadrics, and the existing
positive-characteristic quartic constructions survive independent audit.
The audit is `notes/2026-10-05-foundational-frontier-audit.md`.

The broad assertion about arbitrary ACM space curves must carry a source
qualification: the modern D'Cruz survey states it, whereas the inspected
original Robbiano--Valla proof fixes a monomial curve. This is a source-scope
gap, not a proof that the broad assertion is false. None of the resumed
mathematical arguments uses that broader assertion.

### R-002: exact mate degrees on a fixed quartic cone

Status: **PROVED and independently audited**. On
F=x0*x3^3-x2^4, arbitrary homogeneous mates of degree N exist exactly when

| Characteristic | Allowed degree set | Minimum |
| --- | --- | --- |
| 0 | empty | none |
| 2 | 4 divides N | 4 |
| 3 | 3 divides N | 3 |
| 5 | 25 divides N | 25 |
| prime p>=7 | p divides N | p |

Normalization forces the pullback of any mate to be a scalar multiple of
(z-s^3*t)^N; semigroup descent is equivalent to
p^(v_p(N)) in <3,4>. This is a fixed-carrier optimum, not a global minimum.
Proof: `notes/2026-10-05-positive-quartic-carrier-optimality.md`.
Exact finite controls: `computations/verify_fixed_quartic_mate_degrees.py`.

### R-003: pointwise residual-cycle formula

Status: **PROVED under the explicit quasiprimitive hypotheses, independently
audited**. The formula previously marked a proof candidate is a valid
identity of length cycles, including special-point defects:

    [rho intersect sigma_b]=(b-1)T+D_(b-1).

It follows by taking the determinant of multiplication by the auxiliary
quadric in a saturated BF basis and identifying its torsion cokernel with
the residual finite intersection. An extra copy of C in the mate restriction
is retained in sigma_b; no order-one assumption on that restriction is needed.
The first-normal bound A<=D_(b-1) is coefficientwise. Neither formula asserts
equality of schemes or determines higher jets.
Audit: `notes/2026-10-05-residual-cycle-audit.md`.

### R-004: the finite quartic ancestor has generic length four

Status: **PROVED in the accompanying note; independent audit in progress**.
A surviving quartic common ancestor of the fixed socle targets has principal
order four. Its generic cyclic annihilator algebra is curvilinear of length
four, while (F_4,G_4) has multiplicity three along C0 and residual cycle of
degree four. The order-three global section is already excluded by the
verified finite principal-part computation.
Note: `notes/2026-10-05-localcoh-generic-length.md`.

A local inverse-system example proves that the cyclic algebra need not have
Gorenstein special fibers. Consequently the generic length-four result cannot
be promoted to a globally primitive quadruple without further hypotheses.
This failed shortcut is preserved with its exact algebra in the note and
`computations/verify_localcoh_generic_length_model.py`.

## Active research branches and integration policy

The agents pursue finite quartic local-cohomology incidence, multiplicity-six
Fitting/pole data, split-sextic higher jets, primitive e=2 quadruple contact,
normal quartic singularities, and independent source/proof audits. Results
are integrated here only with their exact proof and parameter-space scope.
Exploration scripts and symbolic outputs remain inspectable but carry no
theorem status merely because a finite calculation terminated.

Pending integration includes the all-direction defect-degree-one/two quartic
exclusion, the primitive quadruple zero locus and its ambient quartic factors,
the normal quartic carrier classification, and the full both-ramified-root
split-sextic family. Each has a specific independent audit or exact chart
completion underway. The strongest continuation should use the resulting
finite systems and source exclusions, retaining poles and higher normal jets.

## Explicit unresolved boundary

No universal STCI theorem, characteristic-zero counterexample, unrestricted
two-form presentation of C0, or all-degree obstruction is established.
The local-cohomology degree-four problem remains nonlinear and finite;
higher multiplier degrees remain unbounded. A primitive local construction
must still pass ambient homogeneous generation and global ACM/Gorenstein
conditions. Thick pairs require full higher-jet/valuation information, not
only tangent roots or first-normal line bundles.

The goal remains active. This document is a continuation checkpoint, and
its pending-integration entries will be updated as the audits conclude.
