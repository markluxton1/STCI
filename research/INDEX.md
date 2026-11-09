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
[result records](results/INDEX.md); for concrete unresolved implications use
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

For a specified transverse slice, use the
[normal-cone specialization test](results/normal_cone_slice_specialization.md)
to check the power quotients over the DVR. For a formal two-equation complete
intersection, [normal flatness and comparison](results/normal_flat_comparison_specialization.md)
gives the hypotheses for specializing the full equation comparison. The
[supported length-five family](results/supported_length_five_defect_specialization.md)
has a free intersection algebra and zero relative defect, but its actual
closed slice has a degree-four defect. The
[punctual relative-defect question](FRONTIER.md#broader-interfaces) under sole
support and generic vanishing remains open.

| Question or approach | Mathematical entry | Reach and missing step |
| --- | --- | --- |
| Which multiplicities and residual cycles occur? | [Two surfaces and actual cycles](synthesis/02-two-surfaces.md), [residual geometry and jets](synthesis/residual_intersections_and_jets.md) | Actual constructions and bounds on specified families; no universal residual floor or monotonicity in the equation degrees is assumed |
| What would two global equations amount to? | [Global equations, Chow forms, complements and bundles](synthesis/global_equations_and_constructions.md), [exact Chow bundle maps](synthesis/chow_bundle_maps.md), [section obstructions](synthesis/complement_section_obstructions.md) | Exact equivalents and constructions; an equivalent test still needs a pair or an obstruction covering every pair |
| Can the curve's torus symmetry organize the search? | [Full flat limits and supported deformations](synthesis/global_equations_and_constructions.md#the-supported-hilbert-locus-and-its-full-torus-boundary), [explicit sextic residuals and limits](synthesis/toric_sextic_residuals_and_limits.md), [weight restrictions](supplements/EQUIVARIANT_DEGREE_BOUNDS.md) | Full limits retain Hilbert data but can need extra generators. The sharp quotient-length bound is eight for eigenform sextics, in every characteristic; mixed-weight and supported deformation questions remain distinct |
| What does a finite torus quotient descend to? | [Embedded quotients and endpoint descent](synthesis/toric_quotients_and_endpoint_descent.md), [full finite modification](synthesis/tropical_thickenings_and_endpoint_duality.md), [toric torsion and endpoint contacts](synthesis/toric_torsion_and_endpoint_contacts.md) | A prescribed-degree test recovers actual homogeneous source spaces; isomorphic abstract algebras can have different images. A constant quotient does not replace the moving embedded family required for a characteristic-zero sole-support CI |
| Can an ACM thickening be constructed downstairs? | [Projected section defects](synthesis/projected_thickening_section_defects.md), [supported sources upstairs](synthesis/supported_linkage_operations.md) | ACM on the quadric threefold need not survive projection to P3; the stated power and binary-mixture images fail when the degree product is nonzero, while other actual sources remain open |
| Which low-degree carriers cannot admit sole-support mates? | [Quartic carriers](synthesis/quartic_carrier_proof.md), [Gorenstein-normalized nonnormal quintics](synthesis/quintic_gorenstein_normalizations.md), [quintic–octic ADE constraint](synthesis/quintic_octic_surface_constraints.md) | Fixed embedding, characteristic zero; the quintic carrier theorem excludes every mate degree under its normalization hypothesis, while the ADE theorem concerns degree (5,8) |
| Why does positive characteristic allow quartic carriers? | [Positive-characteristic constructions](supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md), [arithmetic jet gaps](supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md), [lifting precision](supplements/FROBENIUS_POWER_LIFTING_PRECISION.md), [toric torsion and endpoint contacts](synthesis/toric_torsion_and_endpoint_contacts.md) | Explicit equations in every p>0; degree transfer, prescribed embedded lifts and ramification have separate quantifiers, and all-pair growth remains conditional |
| How do full torus limits organize supported ideals and two-generation? | [Attracting strata and generator incidence](synthesis/torus_attracting_strata_and_generator_incidence.md), [geometric Hilbert-boundary synthesis](synthesis/geometric_integration_and_hilbert_boundary.md) | Both opposite full-ideal limits refine the bounded supported Hilbert locus; two-generation concerns moving ideals, not necessarily their fixed limits. No exhaustive stratification or obstruction theorem is claimed |
| What do normalization and projection construct? | [Carriers and conductor](synthesis/04-carriers.md), [elliptic projection and gluing](synthesis/projection_and_elliptic_gluing.md), [quadratic conductor boundary](synthesis/quadratic_covers_and_conductor_descent.md) | Actual sections and normalized carriers must also pass full inverse support, polarization and conductor gluing; an abstract or local model can retain independent geometric value |
| Can local multiple structures come from actual equations? | [Embedded infinitesimal geometry](synthesis/03-infinitesimal-geometry.md), [actual source spaces](supplements/ACTUAL_EQUATION_SPACES.md), [punctual extensions and columns](synthesis/punctual_quadric_extensions.md) | Saturation, duality, roots, finite jets and source images; formal or graded existence does not supply a proper global pair |
| What does a syzygy rank jump measure geometrically? | [Spectral pushforward powers](synthesis/spectral_pushforward_powers.md), [determinant schemes and graded families](synthesis/spectral_determinant_schemes.md), [order-three roots and actual sextics](synthesis/order_three_roots_and_sextic_lifts.md) | Picard torsion determines splitting and supplies graded families, including nonreduced parameter schemes; the actual embedded equation operator remains an additional condition |
| How much infinitesimal data determines actual equations? | [Global equation jets](synthesis/global_equation_jets.md), [actual octic and sextic comparison](synthesis/actual_octic_root_lift_comparison.md), [bounded equation certificates](synthesis/bounded_equation_certificates.md) | Intrinsic source filtrations and small lifting quotients; an actual proper octic pair has length eight along C0 and residual degree 32, while fixed-degree verification and all-degree search remain separate |
| Can local cohomology obstruct two equations? | [Ancestor and all-stage obstructions](supplements/LOCAL_COHOMOLOGY_ANCESTOR_OBSTRUCTIONS.md), [actual tensor certificates](supplements/LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md) | Exact source and multiplier families are excluded; non-quasi-cyclicity of the full module remains unproved |
| What forces or permits residual support? | [Residual geometry and jets](synthesis/residual_intersections_and_jets.md), [two surfaces](synthesis/02-two-surfaces.md), [supported linkage operations](synthesis/supported_linkage_operations.md) | Exact cycles, attachment, capacity, blowups and liaison; uniform bounds need actual family coverage |
| Can residual curves be absorbed? | [Marked deformation and absorption](synthesis/marked_deformation_and_absorption.md) | Actual partial constructions and lifting criteria; iteration to sole support is missing |
| What do contact and tropical models retain? | [Contact duality and global descent](synthesis/contact_duality_and_global_descent.md), [toric torsion and endpoint contacts](synthesis/toric_torsion_and_endpoint_contacts.md) | Jacobians, full transverse families, endpoint algebras and global-presentation controls; explicit root-of-unity arrangements admit endpoint contact and jet-stabilizer descriptions. These do not classify arbitrary invariant arrangements or establish global sole support. |
| What other intrinsic geometry is useful? | [Fixed geometry](synthesis/01-problem-and-curve.md), [marked flags and duality](supplements/QUARTIC_DUAL_FLAGS_AND_BITANGENTS.md), [projection-center moduli](supplements/QUARTIC_PROJECTION_MODULI.md) | Conormal, ruled and dual models are valuable in their own right; varying an actual equation obstruction with the embedding needs a relative source, not just the existing center classification |

## Short retrieval paths

- **An exact claim:** result record → current proof → necessary computation only
  if that argument uses one. A script's successful rank is not its coverage proof.
- **A proposed extension:** inspect the proof's characteristic, embedding,
  normality, saturation, properness and global-source assumptions.
- **A missing implication:** frontier → owning mathematical home and controls.
- **A shared mechanism:** map → full lemma owner; other topics link its application.

The [six short orientation chapters](synthesis/README.md) introduce the account.
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
