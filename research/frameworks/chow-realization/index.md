---
id: STCI-F-0010
type: framework
title: Chow cycles and realization by two homogeneous equations
status: in_use
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0074, STCI-R-0079, STCI-R-0082, STCI-R-0083, STCI-R-0084, STCI-R-0086]
    to: [STCI-F-0010]
    at: "#scope"
---
# Chow cycles and realization by two homogeneous equations

## Scope

For positive degrees \(a,b\) with \(ab=4m\), study the image of actual
proper homogeneous pairs \((F_a,G_b)\) whose **entire fundamental cycle**
is \(\sum_i n_i[C_{u_i,v_i}]\), where
\(C_{u,v}=[s^4:s^3t:u st^3:v t^4]\), \(u,v\ne0\), and \(\sum_i n_i=m\).
Over an algebraically closed field of any characteristic, the [full
Chow-polytope theorem](../../results/chow_polytope_rigidity.md) identifies
these cycles by equality with \(mP_{C_0}\) in the full, unshifted column-weight
lattice. The cycle points are unordered multisets in \((\mathbf G_m)^2\).
The point \(m[C_0]\) represents the characteristic-zero STCI target.
The realization question also asks which other cycles occur, which embedded
schemes lift them, and what happens to those schemes in flat families.

Keep three maps in view. Actual homogeneous equations define an embedded CI,
which has a fundamental cycle. The full paired transverse Chow polynomial
\(\mathcal C_\sigma(X,Y,Z)=\prod_i(X+u_iY+v_iZ)^{n_i}\) records the cycle.
The normalized specialization
\[
 H_\sigma(A,B)=
 \frac{\mathcal C_\sigma(0,-B,A)}{\prod_i v_i^{n_i}}=
 \prod_i(A-(u_i/v_i)B)^{n_i}
\]
records the weighted divisor in the quadric-pencil coordinate \(q=u/v\). The last
map can forget the pairing of the two coordinates. Above a repeated cycle,
even the full paired polynomial leaves the transverse algebra and its
longitudinal motion undetermined. The [embedded-quotient
framework](../embedded-torus-quotients/index.md) studies those algebras and
their endpoint images. The [global equation
framework](../global-equation-realization/index.md) studies extension to
the same two sections throughout projective space. This spectrum is distinct
from the Picard-torsion roots in [normal
geometry](../spectral-roots/index.md).

## Constructing and recognizing realizations

For a reduced cycle, the CI would be reduced by purity, so its invariant
ideal gives actual weight eigenforms. [Weighted evaluation and the
coprime-pair gate](../../arguments/equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle)
are exact in this case. [Paired coefficient and moment
matrices](../../arguments/torus/transverse_chow_moment_realization.md#3-degreeweight-evaluation-maps-and-coefficient-determinants)
present the same containment spaces. For repeated cycles, evaluating
at the support does not recover the generic lengths.

In characteristic zero, the [full Chow
pullback](../../arguments/torus/full_transverse_chow_pullback_envelope.md)
and the lower-degree [quadric/cubic coefficient
chains](../../arguments/torus/weighted_chow_quadric_cubic_polarizations.md)
give homogeneous ideal memberships for the *same* unknown pair. The
[saturation and interpolation
theorem](../../arguments/torus/spectral_interpolation_and_polar_saturation.md)
explains why one full chain suffices on coordinate-saturated ideals.
Properness, boundary exclusion and the finite norm test are needed to
recognize exact multiplicities. A prescribed coefficient identity, or
membership in the canonical fat-point envelope on the torus, does not
provide homogeneous generators. Conversely, under its finite-pencil
hypotheses the [paired source
determinant](../../arguments/torus/chow_arrangement_moments.md#a-two-operator-determinant-recovers-the-full-transverse-chow-polynomial)
recovers the full paired polynomial of an actual translated CI. Its
order-\(j\) coefficient depends on source depth \(4j\); the coefficients
are regular on the resultant-nonzero source open.

The independent [two-translate sextic
criterion](../../arguments/torus/fixed_surface_restriction_lifts.md#a-two-translate-sextic-construction-criterion)
would construct sole support from an actual symmetric-carrier pair in one
of the surviving unequal multiplicity partitions. Existence of those
pairs remains open.

The [characteristic-zero quartic-pencil
classification](../../results/quartic_chow_pencil_classification.md)
gives a test for the full realization problem in \((4,4)\). Its exceptional
non-invariant orbit over \(2[C_{u,v}]+2[C_{u,-v}]\) lies outside the invariant
Chow closure and has [opposite full Hilbert
limits](../../arguments/torus/quartic_hilbert_chow_limits.md#chow-closure-and-full-opposite-limits)
with the same cycle and different embedded endpoints. In contrast, every
depressed quartic spectral polynomial with nonzero constant term occurs
on the invariant locus. Thus restrictions on the paired configurations can
persist when the spectral coefficients already fill the predicted open
hyperplane. See the [complete low-degree spectral
images](../../arguments/torus/chow_realization_moment_separation.md#13-complete-quadric-spectrum-projections-in-degrees-34-and-44).

## First moment and endpoint tests

The first moment \(M_1=\sum_i n_i u_i/v_i\) is a linear Chow-coefficient
test and is nonzero on every single-support cycle in characteristic zero.
Vanishing on the entire actual CI image in every bidegree would therefore
exclude sole support. The identity with an actual [first-jet
residue](../../arguments/torus/spectral_jacobian_first_jet_bridge.md)
makes the vanishing conjecture a question about homogeneous sources.
The proved cases include [specified one-generator coordinate cone
jets](../../arguments/torus/chow_trace_cone_jets.md), [sign-invariant ACM
ideals or a sign-eigen CI generator](../../results/chow_acm_parity_vanishing.md),
and [linkage criteria covering one double or one triple component with
simple companions in characteristic zero](../../results/chow_moment_residual_speciality.md).
Actual repeated sign-breaking examples can have zero moment.
The [ordinary carrier
norm](../../arguments/torus/spectral_boundary_modulus.md#every-actual-pair-has-such-a-product-of-norms)
exists for every actual translated-cycle pair. Its aggregate first jet
recovers the source residue, and a geometric cancellation criterion
covering all pairs remains open.

[Section parity](../../arguments/torus/chow_section_parity_defect.md)
identifies a necessary defect for nonzero moment on an invariant pure hull.
The [conjugate-pair section hull](../../results/sign_symmetrized_source_defect.md)
expresses a related defect using the actual equations and their sign
transform. [Boundary section
cohomology](../../arguments/torus/boundary_section_cohomology.md)
excludes the exact diagonal endpoint models in types \((6,6)\) and
\((5,8)\). The marked multiplication and source maps remain to be controlled
in general. See the [proof
boundary](../../arguments/torus/universal_first_moment_proof_boundary.md)
and the [cross-framework
comparison](../../arguments/torus/universal_first_moment_corpus_review.md).

For an already given Chow-matched proper CI in characteristic zero, the
[endpoint different](../../arguments/torus/chow_endpoint_different.md)
reads the number of distinct supports from finite jets of the actual
relative Jacobian. This concerns the original pair. A different endpoint
problem concerns the full ideals of torus limits, which can gain embedded
structure and generators. See [full torus
boundaries](../torus-supported-boundaries/index.md). The
[fixed-depth determinant control](../../results/fixed_depth_determinant_incidence.md)
shows why bounded lists of leading source tests have a residual-pair
comparison even for reduced CIs in its large-degree range. Its conclusion
concerns fixed depth and does not negate the exact full support tests.

## Bridges

**Repeated-cycle construction.** Lift the coefficient chain and norm to
one proper homogeneous pair, with control of the embedded structure at
both endpoints and no additional cycle. The [arrangement
investigation](../../investigations/chow-quotient-arrangement-bridge/index.md)
links the quotient fan, endpoint incidence and separated blowups.
[Reduced-union Hilbert strata and the individual-order
dictionary](../../results/arrangement_strata_and_orders.md)
give flat re-formed reduced unions on constant-polynomial strata and
section spaces for prescribed individual vanishing orders. The
[two endpoint evaluation filtrations](../../arguments/torus/arrangement_endpoint_delta.md#the-exact-two-endpoint-rank-formula)
compute the gluing lengths by finite rank tests on distinct markings. In the
[reduced quartic case](../../arguments/torus/arrangement_endpoint_delta.md#the-reduced-44-locus-as-two-affine-line-incidence-conditions),
nonvertical collinearity in both endpoint planes gives gluing lengths
\((18,18)\). Actual \((4,4)\) realization further requires both lines to
avoid the toric vertex \([1:0:0]\) in their respective planes. A reduced CI
arrangement with at least five components must be nonplanar at an endpoint,
so the [dual-planar Rees
models](../../arguments/torus/relative_arrangement_blowup_family.md#8-a-higher-m-planar-locus-and-a-rigidity-threshold)
do not cover those arrangements. General Rees specialization, flat
collision lifts and joint intersection lengths require additional arguments.

**Unrestricted obstruction.** Relate the actual two-generator source to
the moment or endpoint different without imposing a sign or cone-jet
hypothesis. A vanishing theorem would separate the realization locus
from all single-support cycles. The [strategic
queue](../../investigations/proof-audit/knowledge-gain-priorities.md#current-choice-and-reassessment)
compares this question with constructive ones.

The [trace and simultaneous-projection
investigation](../../investigations/trace-residue-projection-geometry/index.md)
compares the Jacobian data of the same two equations in complementary
projections. Its explicit quartic control has nonzero central residue
despite satisfying the tested first-order congruences. The pair lies
outside the full translated-cycle locus, so a vanishing argument still
needs a condition that uses global support beyond those congruences.

The provisional [cycle-first coefficient synthesis](../../arguments/torus/transverse_coefficient_realization_synthesis.md)
compares the same homogeneous source across the product models, quadric
graph and global section maps. The [plane-pencil criterion](../../arguments/torus/plane_pencil_equation_bundles.md)
leaves the full family completion open. The [marked Chow boundary](../../arguments/torus/marked_chow_configuration_boundary.md)
and [endpoint incidence systems](../../arguments/torus/marked_chow_endpoint_incidence.md)
describe distinct-marking models. Their open steps are stable extension
across collisions and comparison with actual nonreduced CI structures.

The [literature discovery comparison](../../literature/chow_realization_connections.md) supplies a toric wonderful model for the character-incidence open, a multigraded reconstruction dimension test, and Benoist's actual CI parameter-space geometry. It also identifies a provisional [affineness comparison](../../arguments/torus/chow_realization_moment_separation.md#source-parameter-space-and-equal-degree-chow-fibers) in equal degrees, and a separate source-sensitive direction through limiting Hurwitz forms. The latter cannot be recovered from a weighted Chow cycle alone; the needed deformation and projection corrections remain open. These are not new universal moment vanishing results.

The [cross-ratio source note](https://chatgpt.com/space/page_d434441dcb688191999bf266b13c4c11)
records a relative-projectivity interpretation of reduced moment balance,
including the two-component harmonicity case.
