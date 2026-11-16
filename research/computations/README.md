# Exact mathematical computations

Begin with the [mathematical approaches](../INDEX.md) and the
[cataloged Result](../CATALOG.md) or focused proof named below.
The proof explains the object being computed, the hypotheses, and the
implication supplied by its output. A script name, successful run, or recorded
rank does not by itself establish those bridges.

Run the commands from the repository root. Python programs use either the
standard library or SymPy; the explicit SymPy requirement is **1.14.0** for the
checks that specify it. Macaulay2 programs use `M2 --script`. The independent
R-0025 matrix builder also requires a C++ compiler. Read a program's header
before running it. Some programs regenerate saved mathematical data, and
some are bounded exploratory models rather than certificate checkers.

## Mathematical entry points

| Mathematical question | Proof and computation | Exact scope |
|---|---|---|
| The curve, conormal geometry, and positive-characteristic constructions | [Curve geometry](../arguments/curve/fixed_quartic_geometry.md), [positive-characteristic proofs](../arguments/arithmetic/positive_characteristic_constructions.md); `verify_c0.py` and the [quartic specialization checks](../arguments/quartic_specialization_and_symbols.md#finite-quartic-replay-evidence) | The stated parametrizations and transitions. The positive-characteristic construction and optimality arguments are proved directly in the mathematical home. |
| Quartic carrier mechanisms | [Quartic carrier proof](../arguments/carriers/quartic_carrier_proof.md); primitive obstruction/factor programs, normal-carrier programs and genus-one/genus-two exact checks linked there | Complete arguments require the classification/coverage and descent steps in their proof homes. A determinant or denominator compression alone is not a carrier exclusion. |
| The separate filtered quartic-pair calculation | [Quartic-pair account](../arguments/normal-geometry/quartic_pair_obstruction.md), [R-0022 and its evidence](../results/quartic_44_filtered_exclusion.md#evidence-and-verification); [filtered-contact verifier](verify_44_filtered_contact_2026_10_23.py) | The stated filtered-contact cases; inherited primitive-direction coverage remains a separate mathematical input. The [actual quartic source spaces](../results/quartic_actual_symbols.md) have a separate proof. |
| Filtrations, cancellation, and marked embedding | [Filtration account](../frameworks/formal-normal-geometry/normal_filtration_boundaries.md); `verify_ideal_filtration_*.py`, `verify_delta_conormal_annihilator_2026_10_24.m2`, `verify_delta_rees_equation_module_2026_10_24.m2`, `verify_delta_singular_families_2026_10_24.m2` | Explicit identities, counterexamples and displayed Rees/initial ideals. Finite samples do not establish global equation realization or a general STCI consequence. |
| Prescribed characteristic-two arithmetic lifting | [Arithmetic lifting and exact support](../arguments/arithmetic/z4_lifting_and_deformation.md#exact-computational-support-and-scope), [R-0012](../results/prescribed_z4_arithmetic_nonlifting.md) | The prescribed embedded structure and its integral congruence. The raw-source decomposition checks the corrected residues. |
| Local-cohomology tensor and actual family certificates | [Local-cohomology proof homes](../arguments/local-cohomology/local_cohomology_conormal_geometry.md), [full tensor and finite direction replays](../results/quartic_ancestor_direction_reduction.md#evidence) | The named actual top and seed families, complete affine lower-lift fibers and full tensor identities. A zero of an older denominator is not an existence witness. |
| Degree-fifteen exceptional factor | [Exact dual proof and archived replay](../arguments/local-cohomology/degree_fifteen_obstruction.md#direct-original-tensor-verification) | The saved normalized dual annihilates all 18 original-tensor columns modulo the entire degree-15 polynomial and has target coordinate 72 equal to one for every affine lower lift. |
| Explicit residual curves and fixed-boundary smoothing | [Residual examples](../arguments/residuals/explicit_quartic_residuals.md), [smoothing proof](../arguments/residuals/fixed_boundary_smoothing.md); exact residual/line M2 programs and `verify_ci_fixed_boundary_node_smoothing_2026_10_25.py` | The displayed quartic pairs, geometric smoothness/connectedness, and five independent node parameters in the specified fixed-boundary family. |
| Fixed sextic, degree-sixteen mates | [R-0025 full proof](../results/ci_fixed_sextic_jet_rigidity.md); [maintained verifier](../results/ci_fixed_sextic_jet_rigidity.support/verify.py) | One carrier and one mate degree. The 23-dimensional normal quotient, 969 constant coefficients, 286 carrier multiples, good samples and rank 683 are all needed. |
| Finite generic jets at fixed degrees | [Finite-jet theorem and controls](../arguments/residuals/finite_normal_jets.md) | The Nakayama and degree proof applies to singular integral curves and weighted reducible curves in arbitrary characteristic. The archived program supplies examples and source-coefficient controls. |
| Residual constructions and equation spaces | [Actual global models](../arguments/residuals/residual_global_models.md), [reverse liaison](../arguments/residuals/residual_liaison.md) | The proofs give the sheaf cohomology, attachment maps and stated linkage resolution. |
| Projection and elliptic gluing | [Projection proof and evidence](../arguments/carriers/projection_and_elliptic_gluing.md) | Exact incidence, local contact, inverse-image and Picard gates for the stated targets. |
| Mixed contact and additional sextic ranks | [Mixed-sextic contact](../arguments/residuals/residual_contact_cycles.md#consolidated-historical-source-researchsupplementsmixed_sextic_contactmd); archived [Macaulay2 contact checker](https://github.com/markluxton1/STCI/blob/0a35730b2f5e046705b8a7570ebc52c2a726da52/research/computations/stci_mixed_contact_2026_10_29.m2) and [sextic jet calculations](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/stci_search_sextic_jets_2026_10_28.py) | Uniform polynomial matrix arguments and named finite sextic-source ranks are distinct. The archived Python program imported the historical R-0025 arithmetic implementation. |
| Root pencils and collision scales | [Geometric pencil](../arguments/torus/root_pencil_geometry.md), [arithmetic collision](../arguments/arithmetic/arithmetic_root_collision.md); root-pencil, eight-component and root-collision verifiers | Displayed actual families, contact/conductor controls and residue-sensitive valuation calculations; no invariant of every containing pair is asserted. |
| Embedded quotient descent and full sextic toric limits | [Quotient image proof](../arguments/torus_embedded_quotients.md), [sextic configurations](../arguments/torus_sextic_residuals.md); [Argument-owned verifier](../arguments/torus-sextic-controls.support/verify.py) | Standard-library exact endpoint ranks in the stated characteristics, homogeneous source ranks, polynomial identities and cycle/HP checks. The general image, purity, flatness and full-initial-ideal arguments are proved in the mathematical homes. |

The focused proof homes identify further companion programs where they supply
an independent construction, a separate argument, or necessary exact support.
This table is an entry route, not a proposed all-program execution suite.

## Checking important saved certificates

The fixed-sextic independent builder reconstructs its finite matrix and
checks every known carrier multiple:

```sh
python3 -B research/results/ci_fixed_sextic_jet_rigidity.support/verify.py
```

The verifier prints the prime, good samples, rank, kernel dimension and
matrix hash. The [Result's evidence section](../results/ci_fixed_sextic_jet_rigidity.md#exact-evidence-and-independent-verification)
records the proof linkage and the historical and consolidation replays.

The fixed-boundary smoothing check reconstructs the actual quartic source,
its gradient node functional and all five tangent witnesses:

```sh
python3 -B research/computations/verify_ci_fixed_boundary_node_smoothing_2026_10_25.py
```

The [saved witness JSON](ci_fixed_boundary_node_smoothing_2026_10_25.json)
contains the global monomial basis, exact rational perturbations, pivots and
ranks. The formal/étale-local smoothing interpretation additionally uses the
node-family argument in its proof home.

## Historical computation artifacts and current scope

Some proof homes cite exact data or certificates at pinned commits rather
than carrying a second copy. A pinned reference preserves the source, but
does not supply a replay environment in the current tree. A reference to a saved witness, dual coefficient,
Taylor array, or other validation export in an older research note is historical
unless its current availability is separately confirmed.

The [H2 monic ODE account](../arguments/carriers/extracted_quintic_h2_monic_ode_and_open_incidence.md)
records the export construction. Replaying it requires the historical
coefficient inputs, including the seventeen-equation and domain-polynomial
exports, or their regeneration.

The distinct H3 multiplicity-four and support32 coefficient certificates were
also retired. Their identities, hypotheses, and qualifications remain described
in the [H3 argument](../arguments/carriers/quintic_h3_support_exclusion.md), but the large saved columns and the former
multiplicity/support32 generator program paths are not available in the current
tree. Treat computer-certified identities as historically verified claims, not
as newly established independent symbolic proofs.

Retained mathematical methods and statements should be distinguished from
historical execution evidence. The project does not require retaining every
saved coefficient or certificate to preserve the mathematical research.

## Structural checks

The repository's existing validators check records and navigation, not
mathematical correctness:

```sh
python3 -B research/computations/validate_records.py
python3 -B research/computations/validate_result_records.py
python3 -B scripts/check_markdown_links.py --anchors
```

Both record commands require the pinned PyYAML dependency in
`scripts/requirements-research.txt`; `validate_records.py` is the compatibility
entry point for the shared legacy/new-schema engine. Verification status belongs
with the mathematical statement: distinguish a proof, a saved exact witness,
a source inspection and an actual rerun. None implies an unrestricted STCI
answer or an unperformed computation.
