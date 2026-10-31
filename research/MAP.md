# Mechanisms and mathematical interfaces

The [approach index](INDEX.md) organizes questions. This page connects their
mechanisms. A shared idea is not a theorem dependency: each application must
satisfy the hypotheses of its full statement. The complete promoted claim
locator is [results/INDEX.md](results/INDEX.md).

## Reusable mechanisms and their owners

| Mechanism | Full mathematical home | What crosses topics, and what does not |
| --- | --- | --- |
| Actual lifting through a fixed symbol | [Global lifting interfaces](synthesis/global_lifting_interfaces.md) | All allowed higher lifts enter the obstruction quotient; a successful linear lift still needs properness and support |
| Saturation and perfect multiplication | [Normal filtrations](synthesis/normal_filtration_boundary_obstructions.md), [quartic-pair local algebra](synthesis/quartic_pair_obstruction.md) | Generic algebra plus integral lattices yields special-point divisors; distinct module defects are not identified without a map |
| Full conductor descent | [Conductor algebra](supplements/CONDUCTOR_DESCENT_ALGEBRA.md), [fixed carriers](supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md) | Normalized sections must glue through the full finite algebra; nilpotent and residue-phase conditions have different characteristic behavior |
| Polarization and gluing | [Elliptic projection](synthesis/projection_and_elliptic_gluing.md), [finite pullbacks](synthesis/finite_pullback_and_matrix_obstructions.md) | Component line-bundle restrictions, node identifications and actual ambient sections are separate tests |
| Local singularities versus global surface geometry | [Quartic pair](synthesis/quartic_pair_obstruction.md), [quintic–octic constraints](synthesis/quintic_octic_surface_constraints.md) | Moving-symbol germs produce exceptional curves; the quintic argument additionally needs an integral Picard relation and an even-node cover |
| Numerical versus ideal pullback | [Numerical surface pullback](synthesis/numerical_surface_pullback.md), [normal-carrier Hodge criterion](supplements/NORMAL_CARRIER_DIVISOR_GEOMETRY.md) | The effective difference measures exceptional ideal vanishing; the normal hypersurface equality criterion has its own Q-Cartier and characteristic hypotheses; Cartier index alone does not bound the correction |
| Degree exhaustion and residual attachment | [Residual geometry](synthesis/residual_intersections_and_jets.md), [finite normal jets](synthesis/finite_normal_jets.md) | Properness and generic length turn a local bound into a projective residual degree; vertical exceptional support alone is insufficient |
| Deformation and realization | [Marked absorption](synthesis/marked_deformation_and_absorption.md) | Lifting a quotient, a marked embedding and actual equation coefficients are distinct tasks; partial residual transfer need not iterate |
| Duality and global presentation | [Contact and descent](synthesis/contact_duality_and_global_descent.md), [endpoint algebras](synthesis/fixed_surface_and_endpoint_algebras.md) | The full algebra/dualizing module retains data absent from reduced support or traces; two affine presentations need not glue homogeneously |
| Frobenius versus characteristic-zero rigidity | [Positive-characteristic equations](supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md), [arithmetic gaps](supplements/ARITHMETIC_EQUATIONS_AND_JET_GAPS.md), [effective transfer](supplements/EFFECTIVE_CHARACTERISTIC_TRANSFER.md) | Bounded-degree transfer is effective and gives an unconditional growing mate-degree bound over all quartic carriers; unrestricted growth still requires characteristic-zero nonexistence |
| Finite free algebra traces and torus degeneration | [General trace and residual controls](synthesis/fixed_surface_and_endpoint_algebras.md), [torus weight bounds](supplements/EQUIVARIANT_DEGREE_BOUNDS.md) | One weight-homogeneous equation forces p to divide the degree product; degeneration constrains all prime-to-p products and gives the sharp p bound with at most two weights per equation |
| Tame projection and nilpotent lifting | [Canonical section and endpoint poles](supplements/TAME_PROJECTION_SECTIONS.md) | Every supported pair in characteristic zero or odd characteristic has the unique unramified algebra section and an explicit pole bound; tame local complete intersections can attain the full pole order, so extension across ramification needs additional global input |
| Integral embedded obstruction classes | [Arithmetic lifting and defect twists](supplements/Z4_INTRINSIC_ARITHMETIC_MECHANISM.md) | Primitive-stage, defect-twisted and derivation-gluing classes distinguish prescribed embedded lifts from arbitrary characteristic-zero equations |

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
