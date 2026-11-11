# Mechanisms and mathematical interfaces

The [approach index](INDEX.md) organizes questions. This page connects their
mechanisms. A shared idea is not a theorem dependency: each application must
satisfy the hypotheses of its full statement. The
[research catalog](CATALOG.md) locates Results and their proof routes.

Read a mechanism both as a constraint and as information about realization:
which multiple structures, projections, residual cycles or other geometric
objects it describes. The fixed STCI problem is one application. A source's
failure can identify a feature to change without deciding other sources.

## Reusable mechanisms and their owners

The [weight, normal, and torus-limit synthesis](synthesis/toric_sextic_residuals_and_limits.md)
follows the equations from their weight and normal symbols through
endpoint extension to Hilbert and support constraints.

The structured torus pilot has complete proof routes in
[Hilbert boundaries](arguments/torus_hilbert_boundary.md),
[sextic residuals and full limits](arguments/torus_sextic_residuals.md), and
[embedded quotient descent](arguments/torus_embedded_quotients.md).
Its Result records identify the exact proof and review scope. In particular, the
[general prime-element colon identity](results/prime_element_colon_identity.md),
[homogeneous divisor-cycle lemma](results/colon_divisor_cycle.md), and
[pure-curve degree-exhaustion lemma](results/pure_curve_degree_exhaustion.md)
can be retrieved independently of the examples in which they are used.
The [supported-boundary framework](frameworks/torus_supported_boundaries.md)
and [embedded-quotient framework](frameworks/embedded_torus_quotients.md)
state which connections are proved applications and which require a new map.

| Mechanism | Full mathematical home | What crosses topics, and what does not |
| --- | --- | --- |
| Actual lifting through a fixed symbol | [Global lifting interfaces](synthesis/global_lifting_interfaces.md), [intrinsic octic/sextic comparison](synthesis/actual_octic_root_lift_comparison.md), [rank strata and unique sextic lifts](synthesis/rank_strata_and_sextic_lifts.md) | Quotient by every allowed ambient correction; the small sextic map and octic flexibility measure actual source images, while root-lift existence, joint generation and support remain separate |
| Quadric contact and the forced multiplier | [Exact contact and norm](synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge) | The actual contact lengths on the quadric force the complementary norm even on branch and collision strata. The proof uses the proper sole-support (6,16) pair and the gap-ten transform ideal |
| Actual quartic symbols through a quadric flag | [Quartic source spaces](results/quartic_actual_symbols.md), [order reduction and the Cartier quadruple](results/quartic_pair_normal_order_reduction.md) | Restriction to the containing quadric determines the first-symbol image. The sole order-two quartic direction is \(q^2\). The Cartier quadruple \(4C_0\) on the quadric has the target graded algebra and genus, while its quadratic equation precludes a \((4,4)\) realization |
| Full normal equations and the filtration of \(J/IJ\) | [Local comparison](results/local_filtration_comparison_defect.md), [two local counterexamples and the quartic application](arguments/filtered_equation_comparison.md) | Cancellations with coefficients in \(I_C\) can produce minimal initial equations that disappear in \(J/I_CJ\). Even all nine graded algebras with their maps after restriction to \(C\) can forget the actual intersection algebra. For the prescribed characteristic-two pair, compatible lifts identify the fourth equation with the first conormal kernel |
| Normal Koszul filtration of the comparison defect | [Incoming differentials](results/normal_koszul_comparison_defect.md), [prescribed-page family](results/recursive_normal_koszul_cancellation.md) | The Koszul complex on the two regular normal parameters uses the full normal algebra. Its incoming images give the successive subquotients of the R-0030 kernel. The recursive transverse family realizes any positive page and unbounded generic defect. The general comparison with extended Rees torsion is open |
| Scheme-theoretic support and punctual comparison defects | [Statements and proofs](arguments/punctual_comparison_defects.md#statements-and-proofs) | The conormal entry ideal bounds the DVR exponents. The relative initial ideals detect loss of torsion, while the actual finite algebra detects residual support |
| Transverse slicing of the normal cone and filtered equations | [DVR power-quotient test](results/normal_cone_slice_specialization.md), [two-equation comparison](results/normal_flat_comparison_specialization.md), [supported length-five family](results/supported_length_five_defect_specialization.md) | For a flat \(B\)-algebra \(M\) with marked quotient \(M/K=B\), the all-degree slice test detects normal flatness over the DVR \(B\). In the formal two-equation setting normal flatness gives base change for the comparison with the full initial ideal of \(IJ\). A free intersection algebra can have zero relative defect and a nonzero defect on the slice |
| Saturation and perfect multiplication | [Normal filtrations](synthesis/normal_filtration_boundary_obstructions.md), [quartic-pair local algebra](synthesis/quartic_pair_obstruction.md), [intrinsic fourth extensions](synthesis/intrinsic_fourth_extension.md) | Generic algebra plus integral lattices yields special-point divisors. The [jet-discrepancy](FRONTIER.md#successive-jet-discrepancies-in-actual-equation-spaces) and [multiplicity-six](FRONTIER.md#multiplicity-six-incidence-in-actual-jets) questions ask for maps to actual jet ranks |
| Full conductor descent | [Conductor algebra](supplements/CONDUCTOR_DESCENT_ALGEBRA.md), [root and component defects](synthesis/root_descent_and_conductor_defects.md), [square descent and singular gluing](synthesis/square_descent_and_singular_gluing.md), [graded quadratic boundary](synthesis/quadratic_covers_and_conductor_descent.md) | Normalized sections must glue through the full finite algebra; smooth-contact differential bounds and singular-gluing controls explain which hypotheses cannot be discarded |
| Polarization and gluing | [Elliptic projection](synthesis/projection_and_elliptic_gluing.md), [finite pullbacks](synthesis/finite_pullback_and_matrix_obstructions.md) | Component line-bundle restrictions, node identifications and actual ambient sections are separate tests |
| Local singularities versus global surface geometry | [Quartic pair](synthesis/quartic_pair_obstruction.md), [quintic–octic constraints](synthesis/quintic_octic_surface_constraints.md), [ADE cover and symbolic triple](synthesis/quintic_octic_ade_cover_and_triple.md) | Integral divisor relations and cover geometry strengthen rank budgets; the globally ADE (5,8) exclusion includes repeated symbols, while non-ADE carriers remain outside |
| Numerical versus ideal pullback | [Numerical surface pullback](synthesis/numerical_surface_pullback.md), [ruled-surface degree criterion](synthesis/ruled_surface_degree_criterion.md), [normal-carrier Hodge criterion](supplements/NORMAL_CARRIER_DIVISOR_GEOMETRY.md) | The effective difference measures exceptional ideal vanishing; the normal hypersurface equality criterion has its own Q-Cartier and characteristic hypotheses; Cartier index alone does not bound the correction |
| Degree exhaustion and residual attachment | [Residual geometry](synthesis/residual_intersections_and_jets.md), [finite normal jets](synthesis/finite_normal_jets.md) | Properness and generic length turn a local bound into a projective residual degree; vertical exceptional support alone is insufficient |
| Deformation and realization | [Marked absorption](synthesis/marked_deformation_and_absorption.md) | Lifting a quotient, a marked embedding and actual equation coefficients are distinct tasks; partial residual transfer need not iterate |
| Opposite torus limits and moving-ideal generators | [Supported-boundary framework](frameworks/torus_supported_boundaries.md#directional-loci), [moving-ideal test](arguments/torus_hilbert_boundary.md#the-moving-ideal-generator-test), [endpoint comparison](results/intrinsic_limits_endpoint_fibers.md#statement) | The embedded endpoint fibers determine the pure limits and individual embedded lengths. The full opposite-endpoint algebras, actual moving generator incidence and coverage of proposed pairs still require proof |
| Torus limits and deformations preserving support | [Full flat limits](synthesis/global_equations_and_constructions.md#the-supported-hilbert-locus-and-its-full-torus-boundary), [explicit residual configurations](arguments/torus_sextic_residuals.md), [weight theorem](supplements/EQUIVARIANT_DEGREE_BOUNDS.md) | The full limit of a supported scheme preserves C0 and Hilbert data. A residual example loses CI while remaining ACM and needing a degree-ten generator; it is not an I_C-primary boundary for a supported deformation |
| Embedded quotient and endpoint image | [Constant quotient descent](arguments/torus_embedded_quotients.md), [moving quotient and full-limit comparison](investigations/quotient-hilbert-comparison/index.md#inputs), [toric torsion and endpoint contacts](synthesis/toric_torsion_and_endpoint_contacts.md) | Actual multiplication and endpoint lattices control embedded descent. Root-of-unity arrangements provide explicit transverse-character and endpoint-contact models, but neither their local filtrations nor abstract quotient types determine arbitrary global homogeneous equations. |
| Duality and global presentation | [Contact and descent](synthesis/contact_duality_and_global_descent.md), [endpoint algebras](synthesis/fixed_surface_and_endpoint_algebras.md), [exact Chow bundle maps](synthesis/chow_bundle_maps.md) | Full algebras retain data absent from reduced support or traces; the prescribed Chow bundle types already encode global equations, while arbitrary determinantal types do not |
| Frobenius and arithmetic coalescence | [Positive-characteristic equations](supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md), [arithmetic gaps](supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md), [normal associated-graded base change](results/quartic_normal_initial_base_change.md), [root-of-unity coalescence](synthesis/toric_torsion_and_endpoint_contacts.md#3-root-of-unity-arrangements) | Nonreduced group schemes explain coalescence in specified binomial arrangements. In the prescribed \(\mu_4\) family the full projective intersection is flat, while the order-four normal relation appears only after reduction mod two |
| Integral embedded obstruction classes | [Arithmetic lifting and defect twists](supplements/Z4_INTRINSIC_ARITHMETIC_MECHANISM.md), [power extraction](supplements/PRIME_TO_P_POWER_EXTRACTION.md), [Frobenius precision](supplements/FROBENIUS_POWER_LIFTING_PRECISION.md) | Prescribed embedded lifting, actual supported traits and finite Witt precision have different hypotheses; none excludes unrelated characteristic-zero presentations |
| Torsion classes and geometric constructions | [Elliptic double inverse](synthesis/elliptic_double_inverse_construction.md), [sextic cyclic cover](supplements/SEXTIC_PAIR_REDUCTION.md), [toric torsion and endpoint contacts](synthesis/toric_torsion_and_endpoint_contacts.md) | Torsion supplies actual sections or a normalized cover in the stated settings; full inverse support, polarization and local class compatibility remain separate realization conditions. |

## Additional comparisons with actual realization

- [Complement section classes](synthesis/complement_section_obstructions.md) distinguish complete continuous solvability and vanishing primary algebraic classes from actual homogeneous sections on the nonaffine complement.
- [Punctual lifts and actual columns](synthesis/punctual_quadric_extensions.md) distinguish finite-order sheaf existence from the normal-action quotient of a specified homogeneous ideal embedding. A rank-zero transition can change the ruling invariant.
- [Supported linkage](synthesis/supported_linkage_operations.md) isolates the generic Gorenstein test. Its type-two local algebra cannot be repaired by changing only endpoint attachment; the Rao dimensions are the same canonical boundary budget, not a second independent obstruction.
- [Pencil-compatible retraction](synthesis/contact_jacobians_and_hamiltonian_actions.md#a-pencil-compatible-polarized-retraction-cannot-extend-globally) detects the omitted hyperplane section through a general polarized linear-normality criterion. It leaves the actual nonretracted multiple structures available; it does not exclude arbitrary retractions or supported pairs.

- The [ruled integral gap](synthesis/ruled_surface_degree_criterion.md#the-first-positive-integral-gap) and [embedded conductor refinement](synthesis/quadratic_covers_and_conductor_descent.md#12-embedded-curve-exclusion-of-the-minimal-boundary) share a useful method: analyze equality or the first integral gaps in a budget, then use the actual fiber or ambient equation scheme to exclude a numerical survivor. Their correction terms and obstruction modules remain different objects.

- The [projected-source calculation](synthesis/projected_thickening_section_defects.md) makes another comparison explicit: a missing ambient section corresponds to irrelevant torsion in the source/image quotient and nonzero Rao classes downstairs, using ACMness of that source. Those high-degree classes can die under reduction with the same support. This section-ring defect is neither the R-0030 relative comparison defect nor a residual curve, and no all-pair persistence map is proved.

- The [opposite-carrier and endpoint-contact proof](synthesis/toric_torsion_and_endpoint_contacts.md#4-pairwise-endpoint-contact) uses the involution to exchange the two explicit carriers and their endpoint lengths. The [local \(\mu_{16}\) graphs](synthesis/toric_torsion_and_endpoint_contacts.md#a-local-graph-with-three-contact-orders) exhibit three distinct contact orders in affine four-space. Realizing further filtrations in global intersections through \(C_0\) remains open.

## General lemmas and uses beyond the fixed embedding

| Reusable result | Its general mathematical content and the application boundary |
| --- | --- |
| [Fixed-symbol lifting quotient](synthesis/global_lifting_interfaces.md) | Determines both obstructions and possible corrections in an entire affine lift fiber; vanishing still needs the nonlinear realization and support conditions |
| [Embedded ribbon-to-triple obstruction](supplements/HIGHER_INITIAL_IDEALS_AND_EMBEDDED_THICKENINGS.md#the-embedded-ribbon-to-triple-obstruction) | A canonical extension of conormal line bundles controls primitive triples in a fixed ambient scheme with fixed ribbon quotient. Flat pullback carries the extension class, with separate compatibility conditions for nonflat pullback |
| [One extra homogeneous module generator](synthesis/quadratic_covers_and_conductor_descent.md#11-a-common-graded-mechanism-one-extra-homogeneous-module-generator) | Canonical-module inequalities for finite birational graded extensions of Gorenstein curve rings; a module-generator hypothesis is stronger than algebra generation |
| [Quadratic norm and postulation](synthesis/quadratic_covers_and_conductor_descent.md#81-ambient-quadratic-norms-force-conductor-postulation) | Converts actual conductor membership into an ambient polynomial relation, then a Hilbert-function bound; the separated-cover application has additional characteristic hypotheses |
| [Projection section defects](synthesis/projected_thickening_section_defects.md) | A parameter-sequence and Jacobian-socle mechanism for finite projection of nonreduced schemes; the generalized version may change the reduced curve |
| [Spectral powers](synthesis/spectral_pushforward_powers.md), [boundary](synthesis/spectral_pushforward_boundary.md) and [determinant schemes](synthesis/spectral_determinant_schemes.md) | General genus-one degree-two pushforwards and smooth (2,2) coefficient determinants detect Picard torsion; singular/nonreduced roots need their own controls, and actual ambient operators retain the fixed embedding |
| [Global equation jets](synthesis/global_equation_jets.md) | An intrinsic filtration records successive source-image deficits; finite realization has a general existential theorem and an explicit quadric-flag bound, not a universal effective stopping rule from a rank plateau |
| [Carrier conductor–differential comparison](synthesis/carrier_conductor_differential_comparison.md) | Full conductor contact versus the actual normal differential constrains smooth normalization/smooth conductor regimes; singular contacts and generically singular carriers require different arguments |
| [Pencil Milnor identity](synthesis/pencil_milnor_budget.md) | A general degree/genus/polar identity retains special-point defects; for C0 its inequality already follows from stronger local geometry, so it is not an independent obstruction |
| [Ruled-surface criterion](synthesis/ruled_surface_degree_criterion.md) and [numerical pullback](synthesis/numerical_surface_pullback.md) | Degree/genus and ideal-versus-numerical pullback comparisons under their own geometric hypotheses; the quartic and quintic uses are applications |

The [tame projection-section result](supplements/TAME_PROJECTION_SECTIONS.md)
retains the actual unramified module and pole bound. Extending it to other covers
needs new hypotheses and proof. Likewise, the surface-normalization conductor
is not the conductor of the quadratic separation of a nonreduced intersection;
their bounds cannot be combined without a map.

## Compatibility as an optional viewpoint

The [formal-normal framework](frameworks/formal-normal-geometry.md#simultaneous-realization-and-compatibility-problems)
states the two-carrier realization question for a prescribed generic ideal.
A useful distinction is between the abstract rational curve, embeddings of it
in surfaces, compatible maps of those surfaces to a common projective space,
and their actual simultaneous intersection there. The abstract \(\mathbf P^1\)
does not encode this embedding problem. Surface polarizations, conormal data,
conductor gluing and the images of global sections progressively retain more
of it.

This is an orientation device, not a required sequence. In particular, local
compatibility along \(C_0\) and global sole support are different conditions.
A divisor or local-algebra model may be realizable while every available pair
has a residual curve. Conversely, useful positive-characteristic constructions
show that some apparently restrictive compatibility conditions can coexist.

## Connections that change the next question

In the stated separated quadratic cover, the [canonical conductor sequence](synthesis/quadratic_covers_and_conductor_descent.md) already determines the [Rao dimensions](synthesis/supported_linkage_operations.md#1-rao-dimensions-repeat-the-canonical-boundary-inequality). Comparing those dimensions repeats one budget. The boundary's embedded multiplication and actual defining-equation restrictions retain additional information; the extremal residual-line argument uses precisely that extra information. An embedded AG conjugate union descends automatically, so constructing the union with its required support and polarization is the unresolved constructive step.

The [intrinsic fourth-extension proof](synthesis/intrinsic_fourth_extension.md) and [unique sextic lift](synthesis/rank_strata_and_sextic_lifts.md) connect embedded data to actual equations in two different covered settings. They explain useful rigidity after the relevant hypotheses are established; neither reduces arbitrary higher-degree thickenings to these settings. The [punctual cohomological comparison](synthesis/punctual_quadric_extensions.md#5-an-explicit-characteristic-zero-comparison-with-the-sextic-normal-correction) is a stated map for the specified source, not an identification of general deformation problems or of the R-0030 comparison defect.

## What the combined realization tests distinguish

The [order-three family](synthesis/order_three_roots_and_sextic_lifts.md)
supplies positive graded and first embedded lifts, while the
[actual equation comparison](synthesis/actual_octic_root_lift_comparison.md)
can eliminate every sextic lift at a point or leave a substantial octic
space. Its proper residual pair demonstrates that first compatibility and
actual equations can coexist with a positive residual cycle. This connects
the local and global questions without identifying them.

The successful [quintic cover argument](synthesis/quintic_octic_ade_cover_and_triple.md)
uses both controlled resolution invariants and the location of an embedded
defect. The [normal sextic cyclic cover](supplements/SEXTIC_PAIR_REDUCTION.md)
retains unresolved singularity corrections, so its normal-cover invariants
cannot simply enter the same smooth-surface inequality. Spectral Picard
torsion, carrier Weil-class torsion and the
[arithmetic endpoint defect](supplements/FROBENIUS_POWER_LIFTING_PRECISION.md)
are different objects; no general comparison map identifies them.

## Proved arrows and proposed bridges

Torus symmetry can organize the (6,6) or downstairs ACM investigation through
invariant boundary ideals and deformations preserving support. It supplies no
finite classification of those ideals or theorem recovering their generators.
The [constant-quotient criterion](results/constant_quotient_equation_criterion.md)
does solve the prescribed-degree test for a specified embedded finite quotient;
it does not cover arbitrary moving transverse families. The
[sextic controls](arguments/torus_sextic_residuals.md) prove the sharp
eigenform quotient-length bound and exhibit splitting, absorption and loss of
two generators with residual support. Their normal-order calculation recovers
the existing 23-dimensional source, rather than a new length-nine obstruction.
The [selection guide](RESEARCH_DECISION_GUIDE.md#torus-symmetry-as-an-organizing-method)
compares this proposed method with the direct actual-equation sources. Varying
the projection-center orbit is a different question: it changes the embedded
reduced curve, whereas these torus limits keep C0 fixed.

Use the [scoped conclusions](STATE.md#exclusions-and-constructions) for
low-degree exclusions and the [frontier](FRONTIER.md) for open comparisons.
Initial-module defects, conductor defects, node-gluing classes, and residual
projective curves require a comparison theorem before one can be used to
compute another.
