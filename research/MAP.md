# Mechanisms and mathematical interfaces

The [approach index](INDEX.md) organizes questions. This page connects their
mechanisms. A shared idea is not a theorem dependency: each application must
satisfy the hypotheses of its full statement. The complete promoted claim
locator is [results/INDEX.md](results/INDEX.md).

## Reusable mechanisms and their owners

| Mechanism | Full mathematical home | What crosses topics, and what does not |
| --- | --- | --- |
| Actual lifting through a fixed symbol | [Global lifting interfaces](synthesis/global_lifting_interfaces.md), [rank strata and unique sextic lifts](synthesis/rank_strata_and_sextic_lifts.md) | All allowed higher lifts enter the obstruction quotient; a successful linear lift still needs properness and support |
| Saturation and perfect multiplication | [Normal filtrations](synthesis/normal_filtration_boundary_obstructions.md), [comparison and specialization](synthesis/comparison_defect_specialization.md), [quartic-pair local algebra](synthesis/quartic_pair_obstruction.md), [intrinsic fourth extensions](synthesis/intrinsic_fourth_extension.md) | Generic algebra plus integral lattices yields special-point divisors; distinct module defects are not identified without a map |
| Full conductor descent | [Conductor algebra](supplements/CONDUCTOR_DESCENT_ALGEBRA.md), [fixed carriers](supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md), [graded quadratic boundary](synthesis/quadratic_covers_and_conductor_descent.md) | Normalized sections must glue through the full finite algebra; nilpotent and residue-phase conditions have different characteristic behavior |
| Polarization and gluing | [Elliptic projection](synthesis/projection_and_elliptic_gluing.md), [finite pullbacks](synthesis/finite_pullback_and_matrix_obstructions.md) | Component line-bundle restrictions, node identifications and actual ambient sections are separate tests |
| Local singularities versus global surface geometry | [Quartic pair](synthesis/quartic_pair_obstruction.md), [quintic–octic constraints](synthesis/quintic_octic_surface_constraints.md) | Moving-symbol germs produce exceptional curves; the quintic argument additionally needs an integral Picard relation and an even-node cover |
| Numerical versus ideal pullback | [Numerical surface pullback](synthesis/numerical_surface_pullback.md), [ruled-surface degree criterion](synthesis/ruled_surface_degree_criterion.md), [normal-carrier Hodge criterion](supplements/NORMAL_CARRIER_DIVISOR_GEOMETRY.md) | The effective difference measures exceptional ideal vanishing; the normal hypersurface equality criterion has its own Q-Cartier and characteristic hypotheses; Cartier index alone does not bound the correction |
| Degree exhaustion and residual attachment | [Residual geometry](synthesis/residual_intersections_and_jets.md), [finite normal jets](synthesis/finite_normal_jets.md) | Properness and generic length turn a local bound into a projective residual degree; vertical exceptional support alone is insufficient |
| Deformation and realization | [Marked absorption](synthesis/marked_deformation_and_absorption.md) | Lifting a quotient, a marked embedding and actual equation coefficients are distinct tasks; partial residual transfer need not iterate |
| Duality and global presentation | [Contact and descent](synthesis/contact_duality_and_global_descent.md), [endpoint algebras](synthesis/fixed_surface_and_endpoint_algebras.md) | The full algebra/dualizing module retains data absent from reduced support or traces; two affine presentations need not glue homogeneously |
| Frobenius versus characteristic-zero rigidity | [Positive-characteristic equations](supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md), [arithmetic gaps](supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md) | Frobenius can remove nilpotent descent obstructions; flat arithmetic deformation does not preserve sole reduced support |
| Integral embedded obstruction classes | [Arithmetic lifting and defect twists](supplements/Z4_INTRINSIC_ARITHMETIC_MECHANISM.md) | Primitive-stage, defect-twisted and derivation-gluing classes distinguish prescribed embedded lifts from arbitrary characteristic-zero equations |

## Additional comparisons with actual realization

- [Complement section classes](synthesis/complement_section_obstructions.md) distinguish complete continuous solvability and vanishing primary algebraic classes from actual homogeneous sections on the nonaffine complement.
- [Punctual lifts and actual columns](synthesis/punctual_quadric_extensions.md) distinguish finite-order sheaf existence from the normal-action quotient of a specified homogeneous ideal embedding. A rank-zero transition can change the ruling invariant.
- [Supported linkage](synthesis/supported_linkage_operations.md) isolates the generic Gorenstein test. Its type-two local algebra cannot be repaired by changing only endpoint attachment; the Rao dimensions are the same canonical boundary budget, not a second independent obstruction.

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

## Proved arrows and proposed bridges

The [short dependency map](synthesis/DEPENDENCIES.md) identifies proved arrows
and their premises. The [frontier](FRONTIER.md) owns the remaining questions.
Do not silently turn a conceptual resemblance into a dependency—for example,
no general theorem identifies an initial-module defect with a conductor defect,
a node-gluing class, or a residual projective curve.
