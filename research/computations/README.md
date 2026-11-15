# Exact mathematical computations

Begin with the [mathematical approaches](../synthesis/README.md) and the
[cataloged Result](../CATALOG.md) or focused proof named below.
The proof explains the object being computed, the hypotheses, and the
implication supplied by its output. A script name, successful run, or recorded
rank does not by itself establish those bridges.

Run the commands from the repository root. Python programs use either the
standard library or SymPy; the explicit SymPy requirement is **1.14.0** for the
checks that specify it. Macaulay2 programs use `M2 --script`. The independent
R-0025 matrix builder also requires a C++ compiler. Read a program's header
before running it: some programs regenerate saved mathematical data, and
some are bounded exploratory models rather than certificate checkers.

## Mathematical entry points

| Mathematical question | Proof and computation | Exact scope |
|---|---|---|
| The curve, conormal geometry, and positive-characteristic constructions | [Curve geometry](../synthesis/01-problem-and-curve.md), [positive-characteristic proofs](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md); `verify_c0.py` and the [quartic specialization checks](../investigations/quartic-specialization-controls/index.md) | The stated parametrizations and transitions. The positive-characteristic construction and optimality arguments are proved directly in the mathematical home. |
| Quartic carrier mechanisms | [Quartic carrier proof](../synthesis/quartic_carrier_proof.md); primitive obstruction/factor programs, normal-carrier programs and genus-one/genus-two exact checks linked there | Complete arguments require the classification/coverage and descent steps in their proof homes. A determinant or denominator compression alone is not a carrier exclusion. |
| The separate filtered quartic-pair calculation | [Quartic-pair account](../synthesis/quartic_pair_obstruction.md), [R-0022](../results/quartic_44_filtered_exclusion.md); `verify_44_filtered_contact_2026_10_23.py`, `audit_44_filtered_contact_2026_10_23.py` | The stated filtered-contact cases; inherited primitive-direction coverage remains a separate mathematical input. The [actual quartic source spaces](../results/quartic_actual_symbols.md) have a separate proof. |
| Filtrations, cancellation, and marked embedding | [Filtration account](../synthesis/normal_filtration_boundary_obstructions.md); `verify_ideal_filtration_*.py`, `verify_delta_conormal_annihilator_2026_10_24.m2`, `verify_delta_rees_equation_module_2026_10_24.m2`, `verify_delta_singular_families_2026_10_24.m2` | Explicit identities, counterexamples and displayed Rees/initial ideals. Finite samples do not establish global equation realization or a general STCI consequence. |
| Prescribed characteristic-two arithmetic lifting | [Arithmetic lifting](../supplements/Z4_LIFTING_AND_DEFORMATION.md), [R-0012](../results/prescribed_z4_arithmetic_nonlifting.md); four Z4 primary/audit programs and `verify_z4_raw_source_decomposition.py` | The prescribed embedded structure and its integral congruence. Raw-source decomposition checks the corrected residues; it is not universal characteristic-zero nonlifting. |
| Local-cohomology tensor and actual family certificates | [Local-cohomology proof homes](../supplements/LOCAL_COHOMOLOGY_CONORMAL_GEOMETRY.md); `session-localcoh-origin-generic-dual.py`, `verify_session_localcoh_q*_dual_2026_10_07.py`, `evening_localcoh_family2_exception_fields_2026_10_13.py`, boundary certificate programs | The named actual top/seed families, complete affine lower-lift fibers and full tensor identities. A zero of an older denominator is not an existence witness. |
| Degree-fifteen exceptional factor | [Exact dual proof](../supplements/LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md); `general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py` | The saved normalized dual annihilates all 18 original-tensor columns modulo the entire degree-15 polynomial and has target coordinate 72 equal to1, for every affine lower lift. |
| Explicit residual curves and fixed-boundary smoothing | [Residual examples](../synthesis/explicit_quartic_residuals.md), [smoothing proof](../synthesis/fixed_boundary_smoothing.md); exact residual/line M2 programs and `verify_ci_fixed_boundary_node_smoothing_2026_10_25.py` | The displayed quartic pairs, geometric smoothness/connectedness, and five independent node parameters in the specified fixed-boundary family. |
| Fixed sextic, degree-sixteen mates | [R-0025 full proof](../results/ci_fixed_sextic_jet_rigidity.md); `endpoint4_fixed_m2_2026_10_25.m2`, `endpoint4_fixed_jet_independent_2026_10_26.py` | One carrier and one mate degree. The 23-dimensional normal quotient, 969 constant coefficients, 286 carrier multiples, good samples and rank 683 are all needed. |
| Finite generic jets at fixed degrees | [Finite-jet theorem](../synthesis/finite_normal_jets.md); `finite_normal_jet_certificate.m2` | The general iff criterion has a mathematical Nakayama/degree proof, valid for singular integral curves and weighted reducible curves in arbitrary characteristic. The program supplies examples and source-coefficient controls, not that general proof or an all-degree solver. |
| Residual constructions and equation spaces | [Actual global models](../synthesis/residual_global_models.md), [reverse liaison](../synthesis/residual_liaison.md); `verify_residual_liaison_resolution_2026_10_28.m2` | The sheaf/cohomology and attachment-map arguments are proved in the mathematical homes; the program checks the stated linkage resolution. Exporting an incidence system is not solving it. |
| Projection and elliptic gluing | [Projection proof](../synthesis/projection_and_elliptic_gluing.md); focused `projection_*.m2` programs and `projection_palindromic_picard.py` | Exact incidence, local contact, inverse-image and Picard gates for the stated targets. The compact programs have no dependency on historical validation snapshots. |
| Mixed contact and additional sextic ranks | [Mixed-sextic contact](../supplements/MIXED_SEXTIC_CONTACT.md); primary/independent `stci_mixed_contact_2026_10_29.m2`, `stci_search_sextic_jets_2026_10_28.py` | Uniform polynomial matrix arguments and named finite sextic-source ranks are distinct. The latter imports the retained R-0025 arithmetic implementation. |
| Root pencils and collision scales | [Geometric pencil](../synthesis/root_pencil_geometry.md), [arithmetic collision](../synthesis/arithmetic_root_collision.md); root-pencil, eight-component and root-collision verifiers | Displayed actual families, contact/conductor controls and residue-sensitive valuation calculations; no invariant of every containing pair is asserted. |
| Embedded quotient descent and full sextic toric limits | [Quotient image proof](../arguments/torus_embedded_quotients.md), [sextic configurations](../arguments/torus_sextic_residuals.md); [Investigation-owned verifier](../investigations/torus-residual-controls/verify.py) | Standard-library exact endpoint ranks in the stated characteristics, homogeneous source ranks, polynomial identities and cycle/HP checks. The general image, purity, flatness and full-initial-ideal arguments are proved in the mathematical homes. |

The focused proof homes identify further companion programs where they supply
an independent construction, a separate argument, or necessary exact support.
This table is an entry route, not a proposed all-program execution suite.

## Checking important saved certificates

The degree-15 check uses only standard Python for the exact saved certificate:

```sh
python3 -B research/computations/general_localcoh_family2_degree15_corank_one_certificate_2026_10_14.py --verify --stem general-localcoh-family2-degree15-corank-one-2026-10-14-attempt06
```

Its default stem is an earlier construction attempt, so the explicit
`--stem` matters. `--verify` checks the saved polynomial dual and its actual
tensor identities; omit it only when intentionally regenerating a certificate.

The fixed-sextic independent builder reconstructs its finite matrix and
checks every known carrier multiple:

```sh
python3 -B research/computations/endpoint4_fixed_jet_independent_2026_10_26.py
```

Its [saved output](endpoint4_fixed_jet_independent_2026_10_26.json) records the
prime, good samples, rank, kernel dimension and matrix hash. The full result
record explains the rank sandwich and nonsplit-node argument and identifies
the actual inherited CI replay. The command here does not assert a new run.

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

Exact computational inputs and certificates used in earlier investigations were
retired under the Phase 3A retention policy. Git history retains the historical
versions; the current tree does **not** provide a complete replay environment
for those computations. A reference to a saved witness, dual coefficient,
Taylor array, or other validation export in an older research note is historical
unless its current availability is separately confirmed.

The retained `generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2`
describes the H2 export construction but itself reads historical coefficient
inputs, some now retired. The former seventeen-equation and domain-polynomial
exports are no longer present. Do not claim this model is immediately rerunnable
without restoring inputs from Git history or regenerating them.

The distinct H3 multiplicity-four and support32 coefficient certificates were
also retired. Their identities, hypotheses, and qualifications remain described
in the H3 mathematical supplement, but the large saved columns and the former
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
