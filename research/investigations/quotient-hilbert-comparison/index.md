---
id: STCI-I-0002
type: investigation
title: Specialization between moving transverse quotients and full Hilbert limits
status: planned
scope: "#scope"
question: "#question"
findings: "#findings"
relations:
  - kind: motivates
    from: [STCI-F-0001, STCI-F-0002]
    to: [STCI-I-0002]
    at: "#purpose"
  - kind: uses
    from: [STCI-R-0037, STCI-R-0039, STCI-R-0051, STCI-R-0052, STCI-R-0053]
    to: [STCI-I-0002]
    at: "#inputs"
---
# Specialization between moving transverse quotients and full Hilbert limits

## Scope

Fix \(C_0\), its integer-weight torus, a degree type \((a,b)\), and a
declared bounded supported family if one is being tested. A sole-supported
proper pair would have generic transverse length \(m=ab/4\). The general
comparison permits a moving embedded quotient and noncurvilinear algebras.
It is not restricted to a constant quotient or its abstract isomorphism class.
Any concrete calculation must state its characteristic, polynomial, family,
power bound, and finite cutoff where one is used.

## Question

Starting from one actual moving embedded family, which transverse algebra,
endpoint image-lattice, and actual homogeneous equation-module data specialize
to its two full torus limits? Can a proved comparison morphism or specialization
statement constrain generator incidence on an opposite-limit intersection?
In particular, can the paired endpoint profiles give a compatibility
restriction beyond the individual Hilbert-polynomial and defect budgets?

## Purpose

[F-0001](../../frameworks/torus_supported_boundaries.md) organizes full
supported limits and moving equations.
[F-0002](../../frameworks/embedded_torus_quotients.md) retains embedded
quotients and projective contraction. This joint investigation asks for the
missing mathematical bridge between those objects. It does not identify them
because they share a defect length or resemble one another geometrically.

## Inputs

[R-0037](../../results/supported_hilbert_full_limits.md) preserves the whole
supported Hilbert object; [R-0039](../../results/moving_ideal_generator_criterion.md)
tests its actual generators. The constant-quotient construction,
[R-0051](../../results/constant_embedded_orbit_image.md), endpoint formula
[R-0052](../../results/orbit_image_endpoint_polynomial.md), and source test
[R-0053](../../results/constant_quotient_equation_criterion.md) give controlled
comparisons, not coverage of every moving family.

The broader [entire finite-modification argument](../../synthesis/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification)
has its own scoped review. Starting with a proper homogeneous pair of
degrees \((a,b)\) with sole reduced support \(C_0\), it takes the full
closure of the torus restriction. It gives a rank-\(m\) quotient bundle
\(\mathcal B\), with \(m=ab/4\), degree \(e\ge0\), and endpoint defects
satisfying
\[
\delta_0+\delta_\infty=e+m(2a+2b-7).
\]
Its [strict-movement proof](../../synthesis/tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier)
requires characteristic zero or characteristic \(p>0\) with \(p\nmid ab\).
For \((6,6)\), the rank is nine and \(\delta_0+\delta_\infty=e+153\),
with \(e>0\) in that range. A constant quotient has \(e=0\). Conversely,
if \(e=0\), global generation makes \(\mathcal B\) trivial and its
multiplication and coordinate sections constant. Movement refers to variation
of the embedded quotient and allows the abstract algebra to stay isomorphic.
The finite-modification theorem has a separate proof and review from the
constant-quotient Results.

## Method

Retain the entire scheme-theoretic closure of the torus restriction and both
endpoint image algebras, including torsion removal and saturation. Compute the
full ideal limits of the same moving scheme in both directions. Then construct
the actual maps relating the data and prove what commutes with specialization.
Only after this can defects or rank changes be compared.

The geometric points \(p_0,p_\infty\) on an orbit closure and the two limits
\(t\to0,\infty\) in a Hilbert scheme play different roles. The displayed
endpoint budget is neither their difference nor a formula determining a full
limit ideal. Constant total defect does not identify the algebras or guarantee
flatness of a relative image lattice.

An explicit residual family can test the proposed maps first. Label it as a
control outside the supported incidence whenever residual curves remain.
Positive-characteristic collisions can test characteristic dependence, but do
not supply a characteristic-zero supported deformation.

## Findings

No general comparison morphism, specialization theorem, or new generator
obstruction has been established here. The finite constant-family criteria and
explicit flat collision are preserved, while the moving-family bridge remains
open. No identification with a reduced normalization conductor, normal-cone
defect, or residual curve is assumed.

## Completion and next decisions

A specified constant quotient has an exact prescribed-degree test in R-0053.
Classifying embedded quotients with prescribed endpoint image algebras is
a separate problem. For the positive-degree family, recovering two global
homogeneous generators of its image is a further realization question.
The [sextic residual configurations](../../arguments/torus_sextic_residuals.md)
supply quotient calculations on residual curves and a full saturated limit
as controls outside the sole-support locus.

A useful first completion is a proved comparison on one fully specified family,
with verified special fibers and actual equation maps, or a counterexample to
an explicitly proposed comparison. Record whether it changes generator
incidence or merely repeats an existing numerical budget. Extending such an
answer requires its own family coverage and characteristic argument.
