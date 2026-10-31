# Mechanisms and mathematical interfaces

The [approach index](INDEX.md) organizes questions. This page connects their
mechanisms. A shared idea is not a theorem dependency: each application must
satisfy the hypotheses of its full statement. The complete promoted claim
locator is [results/INDEX.md](results/INDEX.md).

Read a mechanism both as a constraint and as information about realization:
which multiple structures, projections, residual cycles or other geometric
objects it describes. The fixed STCI problem is one application. A source's
failure can identify a feature to change without deciding other sources.

## Reusable mechanisms and their owners

| Mechanism | Full mathematical home | What crosses topics, and what does not |
| --- | --- | --- |
| Actual lifting through a fixed symbol | [Global lifting interfaces](synthesis/global_lifting_interfaces.md), [rank strata and unique sextic lifts](synthesis/rank_strata_and_sextic_lifts.md) | All allowed higher lifts enter the obstruction quotient; a successful linear lift still needs properness and support |
| Saturation and perfect multiplication | [Normal filtrations](synthesis/normal_filtration_boundary_obstructions.md), [comparison and specialization](synthesis/comparison_defect_specialization.md), [quartic-pair local algebra](synthesis/quartic_pair_obstruction.md), [intrinsic fourth extensions](synthesis/intrinsic_fourth_extension.md) | Generic algebra plus integral lattices yields special-point divisors; distinct module defects are not identified without a map |
| Full conductor descent | [Conductor algebra](supplements/CONDUCTOR_DESCENT_ALGEBRA.md), [fixed carriers](supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md), [graded quadratic boundary](synthesis/quadratic_covers_and_conductor_descent.md) | Normalized sections must glue through the full finite algebra; actual norms constrain boundary postulation, while canonical endomorphisms retain section completion and embedded action as separate data |
| Polarization and gluing | [Elliptic projection](synthesis/projection_and_elliptic_gluing.md), [finite pullbacks](synthesis/finite_pullback_and_matrix_obstructions.md) | Component line-bundle restrictions, node identifications and actual ambient sections are separate tests |
| Local singularities versus global surface geometry | [Quartic pair](synthesis/quartic_pair_obstruction.md), [quintic–octic constraints](synthesis/quintic_octic_surface_constraints.md) | Moving-symbol germs produce exceptional curves; the quintic argument additionally needs an integral Picard relation and an even-node cover |
| Numerical versus ideal pullback | [Numerical surface pullback](synthesis/numerical_surface_pullback.md), [ruled-surface degree criterion](synthesis/ruled_surface_degree_criterion.md), [normal-carrier Hodge criterion](supplements/NORMAL_CARRIER_DIVISOR_GEOMETRY.md) | The effective difference measures exceptional ideal vanishing; the normal hypersurface equality criterion has its own Q-Cartier and characteristic hypotheses; Cartier index alone does not bound the correction |
| Degree exhaustion and residual attachment | [Residual geometry](synthesis/residual_intersections_and_jets.md), [finite normal jets](synthesis/finite_normal_jets.md) | Properness and generic length turn a local bound into a projective residual degree; vertical exceptional support alone is insufficient |
| Deformation and realization | [Marked absorption](synthesis/marked_deformation_and_absorption.md) | Lifting a quotient, a marked embedding and actual equation coefficients are distinct tasks; partial residual transfer need not iterate |
| Duality and global presentation | [Contact and descent](synthesis/contact_duality_and_global_descent.md), [endpoint algebras](synthesis/fixed_surface_and_endpoint_algebras.md) | The full algebra/dualizing module retains data absent from reduced support or traces; two affine presentations need not glue homogeneously |
| Frobenius versus characteristic-zero rigidity | [Positive-characteristic equations](supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md), [arithmetic gaps](supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md) | Frobenius can remove nilpotent descent obstructions; flat arithmetic deformation does not preserve sole reduced support |
| Integral embedded obstruction classes | [Arithmetic lifting and defect twists](supplements/Z4_INTRINSIC_ARITHMETIC_MECHANISM.md) | Primitive-stage, defect-twisted and derivation-gluing classes distinguish prescribed embedded lifts from arbitrary characteristic-zero equations |
| Torsion classes and geometric constructions | [Elliptic double inverse](synthesis/elliptic_double_inverse_construction.md), [sextic cyclic cover](supplements/SEXTIC_PAIR_REDUCTION.md) | Torsion supplies actual sections or a normalized cover in the stated settings; full inverse support, polarization and local class compatibility remain separate realization conditions |

## Additional comparisons with actual realization

- [Complement section classes](synthesis/complement_section_obstructions.md) distinguish complete continuous solvability and vanishing primary algebraic classes from actual homogeneous sections on the nonaffine complement.
- [Punctual lifts and actual columns](synthesis/punctual_quadric_extensions.md) distinguish finite-order sheaf existence from the normal-action quotient of a specified homogeneous ideal embedding. A rank-zero transition can change the ruling invariant.
- [Supported linkage](synthesis/supported_linkage_operations.md) isolates the generic Gorenstein test. Its type-two local algebra cannot be repaired by changing only endpoint attachment; the Rao dimensions are the same canonical boundary budget, not a second independent obstruction.
- [Pencil-compatible retraction](synthesis/contact_jacobians_and_hamiltonian_actions.md#a-pencil-compatible-polarized-retraction-cannot-extend-globally) detects the omitted hyperplane section through a general polarized linear-normality criterion. It leaves the actual nonretracted multiple structures available; it does not exclude arbitrary retractions or supported pairs.

The [ruled integral gap](synthesis/ruled_surface_degree_criterion.md#the-first-positive-integral-gap) and [embedded conductor refinement](synthesis/quadratic_covers_and_conductor_descent.md#12-embedded-curve-exclusion-of-the-minimal-boundary) share a useful method: analyze equality or the first integral gaps in a budget, then use the actual fiber or ambient equation scheme to exclude a numerical survivor. Their correction terms and obstruction modules remain different objects.

The [projected-source calculation](synthesis/projected_thickening_section_defects.md) makes another comparison explicit: a missing ambient section corresponds to irrelevant torsion in the source/image quotient and nonzero Rao classes downstairs, using ACMness of that source. Those high-degree classes can die under reduction with the same support. This section-ring defect is neither the R-0030 relative comparison defect nor a residual curve, and no all-pair persistence map is proved.

## General lemmas and uses beyond the fixed embedding

| Reusable result | Its general mathematical content and the application boundary |
| --- | --- |
| [Fixed-symbol lifting quotient](synthesis/global_lifting_interfaces.md) | Determines both obstructions and possible corrections in an entire affine lift fiber; vanishing still needs the nonlinear realization and support conditions |
| [One extra homogeneous module generator](synthesis/quadratic_covers_and_conductor_descent.md#11-a-common-graded-mechanism-one-extra-homogeneous-module-generator) | Canonical-module inequalities for finite birational graded extensions of Gorenstein curve rings; a module-generator hypothesis is stronger than algebra generation |
| [Quadratic norm and postulation](synthesis/quadratic_covers_and_conductor_descent.md#81-ambient-quadratic-norms-force-conductor-postulation) | Converts actual conductor membership into an ambient polynomial relation, then a Hilbert-function bound; the separated-cover application has additional characteristic hypotheses |
| [Projection section defects](synthesis/projected_thickening_section_defects.md) | A parameter-sequence and Jacobian-socle mechanism for finite projection of nonreduced schemes; the generalized version may change the reduced curve |
| [Spectral four-torsion and syzygy splitting](synthesis/spectral_torsion_and_syzygy_splitting.md) | On a smooth (2,2) root, the ruling-difference line bundle determines the splitting of the fourth-power pushforward and the minimal syzygy degrees; it does not make the actual embedded operator invariant under arbitrary changes of direction |
| [Ruled-surface criterion](synthesis/ruled_surface_degree_criterion.md) and [numerical pullback](synthesis/numerical_surface_pullback.md) | Degree/genus and ideal-versus-numerical pullback comparisons under their own geometric hypotheses; the quartic and quintic uses are applications |

Conductor–differential comparisons, extending the [fourth-power pushforward](synthesis/spectral_torsion_and_syzygy_splitting.md)
to other powers, and more general tame covers are additional directions. Only a statement
with its governing proof is an available lemma; a promising extension is still a
proposed bridge. In particular the surface-normalization conductor is not the
conductor of the quadratic separation of a nonreduced intersection.

## Compatibility as an optional viewpoint

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

## Proved arrows and proposed bridges

The [short dependency map](synthesis/DEPENDENCIES.md) identifies proved arrows
and their premises. The [frontier](FRONTIER.md) owns the remaining questions.
Do not silently turn a conceptual resemblance into a dependency—for example,
no general theorem identifies an initial-module defect with a conductor defect,
a node-gluing class, or a residual projective curve.
