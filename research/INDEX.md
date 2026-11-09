# Intersections and multiple structures through the fixed quartic

Fix an algebraically closed field and the embedding
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). In characteristic zero,
its STCI status is **open**. In every characteristic \(p>0\), a quartic
carrier has a mate defining this same curve. Exact characteristic hypotheses
are stated with each proof; the characteristic-zero quartic exclusion does
not extend unchanged to positive characteristic.

The account asks which proper intersections contain this curve, which embedded
multiple structures actual homogeneous equations realize, and what normalization,
projection and deformation constructions produce. For a proper degree-\((a,b)\)
pair, write \([V(F,G)]=m[C_0]+R\), where \(R\) is the effective residual cycle;
then \(ab=4m+\deg R\). Sole support is the case \(R=0\). Describing attainable
multiplicities, residual cycles, ACM or AG structures, and useful geometry of
other curves is worthwhile even when it does not decide STCI.

This index offers approaches before selecting a program. For connections use
the [mechanism map](MAP.md); for exact current claims use the
[research catalog](CATALOG.md); for concrete unresolved implications use
[the frontier](FRONTIER.md). None of these navigation pages is an extra theorem.

## Choose by the mathematical question

For the four-object torus pilot, enter through
[full supported boundaries](frameworks/torus_supported_boundaries.md) or
[embedded quotient descent](frameworks/embedded_torus_quotients.md).
Their linked Results have independently reconstructed proofs with scoped
reviews. The [catalog](CATALOG.md) exposes reusable lemmas and their actual
proof routes; every statement is assessed through its mathematics and evidence.
Concrete next questions are
[moving-ideal generator incidence](investigations/supported-generator-incidence/index.md)
and [quotient-to-Hilbert comparison](investigations/quotient-hilbert-comparison/index.md).

For characteristic-sensitive normal geometry of the fixed quartic, start with
the [conormal splitting](results/quartic_conormal_characteristic_jump.md), the
[flat prescribed \(\mu_4\) family](results/quartic_mu4_degeneration.md), or the
[actual degree-four symbols](results/quartic_actual_symbols.md).
The full argument separates flatness of the intersection, specialization of
its normal associated graded, and realization by global quartic equations.

For the comparison between full initial equations and actual filtered
equations, start with [R-0030](results/local_filtration_comparison_defect.md)
and the [comparison argument](arguments/filtered_equation_comparison.md).
The local controls separate a [lost minimal equation](results/initial_equation_cancellation_counterexample.md)
from [loss of the embedded algebra](results/restricted_normal_diagram_counterexample.md).
The [prescribed characteristic-two pair](results/quartic_char2_fourth_equation_kernel.md)
gives an exact chartwise lift that survives the comparison.

To recover the defect by normal degree and cancellation page, use the
[normal Koszul filtration](results/normal_koszul_comparison_defect.md).
The [recursive transverse complete intersections](results/recursive_normal_koszul_cancellation.md)
realize all cancellations on page \(q-2\) for \(q\ge3\). Their integral
carrier realization concerns the affine part of a marked line.

For coefficient torsion in the comparison, use the
[punctual-defect reading route](arguments/punctual_comparison_defects.md#statements-and-proofs)
to find the annihilator theorem, the residual family, and the supported
quadruple. For existence under sole support, see the
[open question](FRONTIER.md#punctual-relative-defect-under-sole-support).

For a specified transverse slice, use the
[normal-cone specialization test](results/normal_cone_slice_specialization.md)
to check the power quotients over the DVR. For a formal two-equation complete
intersection, [normal flatness and comparison](results/normal_flat_comparison_specialization.md)
gives the hypotheses for specializing the full equation comparison. The
[supported length-five family](results/supported_length_five_defect_specialization.md)
has a free intersection algebra and zero relative defect, but its actual
closed slice has a degree-four defect.

| Question or approach | Mathematical entry | Reach and missing step |
| --- | --- | --- |
| Which multiplicities and residual cycles occur? | [Two surfaces and actual cycles](synthesis/02-two-surfaces.md), [residual geometry and jets](synthesis/residual_intersections_and_jets.md) | Actual constructions and bounds on specified families; no universal residual floor or monotonicity in the equation degrees is assumed |
| What would two global equations amount to? | [Global equations, Chow forms, complements and bundles](synthesis/global_equations_and_constructions.md), [exact Chow bundle maps](synthesis/chow_bundle_maps.md), [section obstructions](synthesis/complement_section_obstructions.md) | Exact equivalents and constructions; an equivalent test still needs a pair or an obstruction covering every pair |
| Can the curve's torus symmetry organize the search? | [Full flat limits and supported deformations](synthesis/global_equations_and_constructions.md#the-supported-hilbert-locus-and-its-full-torus-boundary), [explicit sextic residuals and limits](arguments/torus_sextic_residuals.md), [weight restrictions](supplements/EQUIVARIANT_DEGREE_BOUNDS.md) | Full limits retain Hilbert data but can need extra generators. The sharp quotient-length bound is eight for eigenform sextics, in every characteristic; mixed-weight and supported deformation questions remain distinct |
| What does a finite torus quotient descend to? | [Constant-quotient equation criterion](results/constant_quotient_equation_criterion.md#statement), [moving-quotient comparison](investigations/quotient-hilbert-comparison/index.md#inputs), [toric torsion and endpoint contacts](synthesis/toric_torsion_and_endpoint_contacts.md) | The constant case gives exact homogeneous source spaces for a specified embedding. For a characteristic-zero sole-support CI, the entire finite modification gives a positive-degree embedded family. Its comparison with full torus Hilbert limits remains open |
| Can an ACM thickening be constructed downstairs? | [Projected section defects](synthesis/projected_thickening_section_defects.md), [supported sources upstairs](synthesis/supported_linkage_operations.md) | ACM on the quadric threefold need not survive projection to P3; the stated power and binary-mixture images fail when the degree product is nonzero, while other actual sources remain open |
| Which low-degree carriers cannot admit sole-support mates? | [Quartic carriers](synthesis/quartic_carrier_proof.md), [Gorenstein-normalized nonnormal quintics](synthesis/quintic_gorenstein_normalizations.md), [quintic–octic ADE constraint](synthesis/quintic_octic_surface_constraints.md) | Fixed embedding, characteristic zero; the quintic carrier theorem excludes every mate degree under its normalization hypothesis, while the ADE theorem concerns degree (5,8) |
| What constrains a conditional (6,16) pair? | [Actual quadric-cycle norm](synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge), [sextic symbol map](supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2-the-exact-global-k-linear-symbol-map), [actual cubic jet](supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#7-first-unresolved-global-lift-the-actual-sextic-cubic-jet) | The norm assumes an actual proper sole-support pair with the full generic coprime (2,12) initial ideal and a saturated movement-two first relation. The symbol test leaves an affine line of sextics whose cubic jets still need matching |
| Why does positive characteristic allow quartic carriers? | [Positive-characteristic constructions](supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md), [arithmetic jet gaps](supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md), [lifting precision](supplements/FROBENIUS_POWER_LIFTING_PRECISION.md), [toric torsion and endpoint contacts](synthesis/toric_torsion_and_endpoint_contacts.md) | Explicit equations in every p>0; degree transfer, prescribed embedded lifts and ramification have separate quantifiers, and all-pair growth remains conditional |
| How do full torus limits organize supported ideals and two-generation? | [Opposite attracting loci](frameworks/torus_supported_boundaries.md#directional-loci), [full-limit proof](arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits), [generator incidence](investigations/supported-generator-incidence/index.md#question) | One moving ideal realizes both full limits. Test generation on that moving ideal. The [comparison with the two geometric endpoints of its quotient modification](investigations/quotient-hilbert-comparison/index.md#question) remains open |
| What do normalization and projection construct? | [Carriers and conductor](synthesis/04-carriers.md), [elliptic projection and gluing](synthesis/projection_and_elliptic_gluing.md), [quadratic conductor boundary](synthesis/quadratic_covers_and_conductor_descent.md) | Actual sections and normalized carriers must also pass full inverse support, polarization and conductor gluing; an abstract or local model can retain independent geometric value |
| Which split sextic strata need a conductor test? | [Split sextic carriers](FRONTIER.md#split-sextic-carriers) | The fixed ramified specimen is excluded. A separate one-parameter line still needs normalization and conductor analysis |
| Can local multiple structures come from actual equations? | [Embedded infinitesimal geometry](synthesis/03-infinitesimal-geometry.md), [actual source spaces](supplements/ACTUAL_EQUATION_SPACES.md), [punctual extensions and columns](synthesis/punctual_quadric_extensions.md) | Saturation, duality, roots, finite jets and source images; formal or graded existence does not supply a proper global pair |
| Can two surfaces realize the same formal generic thickening? | [Formal-normal realization problem](frameworks/formal-normal-geometry.md#simultaneous-realization-and-compatibility-problems) | One ambient embedding, containment in both carriers, equality with their intersection, and sole support impose distinct requirements |
| When does a fixed embedded ribbon extend to a primitive triple? | [Canonical ideal-sheaf extension](supplements/HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#the-canonical-embedded-extension), [independent audit](supplements/HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#independent-audit-and-arithmetic-provenance) | For a codimension-two regular immersion with a fixed line quotient of the conormal, splittings classify the embedded triples. The quartic Laurent calculation is a separate application |
| What if both equations have normal order at least two? | [Entirely-thick numerical restrictions](results/entirely_thick.md), [higher-order Rees question](FRONTIER.md#higher-order-rees-data-for-entirely-thick-pairs) | For a proper sole-support pair with balanced normal bundle, the exceptional cycle constrains the degrees and normal orders. An obstruction from higher-order contact remains open |
| What does a syzygy rank jump measure geometrically? | [Spectral pushforward powers](synthesis/spectral_pushforward_powers.md), [determinant schemes and graded families](synthesis/spectral_determinant_schemes.md), [order-three roots and actual sextics](synthesis/order_three_roots_and_sextic_lifts.md) | Picard torsion determines splitting and supplies graded families, including nonreduced parameter schemes; the actual embedded equation operator remains an additional condition |
| How much infinitesimal data determines actual equations? | [Global equation jets](synthesis/global_equation_jets.md), [actual octic and sextic comparison](synthesis/actual_octic_root_lift_comparison.md), [bounded equation certificates](synthesis/bounded_equation_certificates.md) | Intrinsic source filtrations and small lifting quotients; an actual proper octic pair has length eight along C0 and residual degree 32, while fixed-degree verification and all-degree search remain separate |
| When do successive jet conditions become dependent? | [Jet discrepancies](FRONTIER.md#successive-jet-discrepancies-in-actual-equation-spaces), [multiplicity-six incidence](FRONTIER.md#multiplicity-six-incidence-in-actual-jets) | Compare actual section ranks, saturated layer divisors and punctual equation-module defects |
| Can local cohomology obstruct two equations? | [Surviving finite ancestor incidence](FRONTIER.md#quartic-common-ancestors-in-local-cohomology), [all-stage obstructions](supplements/LOCAL_COHOMOLOGY_ANCESTOR_OBSTRUCTIONS.md), [first rational endpoint exclusion and replay](supplements/LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md#first-rational-family-full-parameter-and-exceptional-field-coverage) | Exact exclusions for specified multiplier families leave the finite quartic incidence and the full-module question distinct |
| What forces or permits residual support? | [Residual geometry and jets](synthesis/residual_intersections_and_jets.md), [two surfaces](synthesis/02-two-surfaces.md), [supported linkage operations](synthesis/supported_linkage_operations.md) | Exact cycles, attachment, capacity, blowups and liaison; uniform bounds need actual family coverage |
| Can residual curves be absorbed? | [Marked deformation and absorption](synthesis/marked_deformation_and_absorption.md) | Actual partial constructions and lifting criteria; iteration to sole support is missing |
| What do contact and tropical models retain? | [Contact duality and global descent](synthesis/contact_duality_and_global_descent.md), [root-of-unity endpoint contact proof](synthesis/toric_torsion_and_endpoint_contacts.md#4-pairwise-endpoint-contact) | Jacobians, full transverse families, endpoint algebras and global-presentation controls. Contact and jet-stabilizer formulas concern the specified arrangements, with projective and ruled-model contact computed separately. |
| What other intrinsic geometry is useful? | [Fixed geometry](synthesis/01-problem-and-curve.md), [marked flags and duality](supplements/QUARTIC_DUAL_FLAGS_AND_BITANGENTS.md), [projection-center moduli](supplements/QUARTIC_PROJECTION_MODULI.md) | Conormal, ruled and dual models are valuable in their own right; varying an actual equation obstruction with the embedding needs a relative source, not just the existing center classification |

## Short retrieval paths

- **An exact claim:** result record → current proof → necessary computation only
  if that argument uses one. A script's successful rank is not its coverage proof.
- **A proposed extension:** inspect the proof's characteristic, embedding,
  normality, saturation, properness and global-source assumptions.
- **A missing implication:** frontier → owning mathematical home and controls.
- **A shared mechanism:** map → full lemma owner; other topics link its application.

The [short orientation chapters](synthesis/README.md) introduce the account.
The proof homes they link contain full arguments, including informative failed
constructions and generalizations. [State](STATE.md) summarizes mathematical statements, their review scopes,
and open questions. [Literature](LITERATURE_LEDGER.md)
records checked external statements and application limits; the relevant
literature also appears in the mathematics itself.

For applications beyond the original example, start with the [general lifting
quotient](synthesis/global_lifting_interfaces.md), [graded conductor mechanism](synthesis/quadratic_covers_and_conductor_descent.md#11-a-common-graded-mechanism-one-extra-homogeneous-module-generator),
[projection section defects](synthesis/projected_thickening_section_defects.md),
[carrier conductor–differential comparison](synthesis/carrier_conductor_differential_comparison.md),
[spectral powers](synthesis/spectral_pushforward_powers.md),
[global equation jets](synthesis/global_equation_jets.md),
or [ruled-surface degree criterion](synthesis/ruled_surface_degree_criterion.md).
Their hypotheses, rather than the fixed-quartic motivation, determine their reach.
