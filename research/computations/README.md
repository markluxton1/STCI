# Exact mathematical computations

Begin with the [mathematical approaches](../synthesis/README.md) and the
[canonical result](../results/INDEX.md) or focused proof named below.
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
| The curve, conormal geometry, and positive-characteristic constructions | [Curve geometry](../synthesis/01-problem-and-curve.md), [positive-characteristic proofs](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md); `verify_c0.py`, `verify_normal_bundle.py` | The stated parametrizations and transitions. The positive-characteristic construction and optimality arguments are proved directly in the mathematical home. |
| Quartic carrier mechanisms | [Quartic carrier proof](../synthesis/quartic_carrier_proof.md); primitive obstruction/factor programs, normal-carrier programs and genus-one/genus-two exact checks linked there | Complete arguments require the classification/coverage and descent steps in their proof homes. A determinant or denominator compression alone is not a carrier exclusion. |
| The separate filtered quartic-pair calculation | [Quartic-pair account](../synthesis/quartic_pair_obstruction.md), [R-0022](../results/quartic_44_filtered_exclusion.md); `verify_44_quartic_symbol_comparison_2026_10_23.py`, `verify_44_filtered_contact_2026_10_23.py`, `audit_44_filtered_contact_2026_10_23.py` | Actual quartic source maps and the stated filtered-contact cases; inherited primitive-direction coverage remains a separate mathematical input. |
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
| Order-three roots and actual sextic lifts | [Geometric parameterization and covered slice](../synthesis/order_three_roots_and_sextic_lifts.md); `order_three_sextic_slice.py` | Exactly twenty-four smooth first-compatible points on the stated four-parameter slice; twenty-two symbol failures and two all-lifts cubic failures. The extension checker is `order_three_four_parameter_slice.py`. Reuses the accepted full sextic source and does not exclude the entire order-three locus. |

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

## Mathematical inputs are not disposable logs

Keep a check's actual dependency closure. In particular:

- Local-cohomology checks read `localcoh-incidence-tensor.txt`,
  `localcoh-incidence-bases.txt`, `localcoh-symbol-top.json`, actual family
  seed JSONs, dual coefficient files and saved exact certificates. Some
  verifiers also bind small evaluation files by hash. Restore or deliberately
  repair those bindings before removing an input.
- The degree-fifteen certificate stores the complete normalized dual in JSON.
  Its checker reconstructs the actual tensor from the four mathematical inputs
  and checks all polynomial identities directly; construction inverses and
  generation records are unnecessary. The certificate also binds the exact
  arithmetic implementation used by that check.
- Quintic and nonendpoint programs read actual coefficient data under
  `../validation/`: the primitive diagonal polynomial, Taylor coefficient
  arrays, corrected H2 quotient/norm inputs, and H3 coefficient/remainder
  and Bézout data. That directory is not uniformly execution history.
- Preserve the distinct H3 multiplicity-four, support32 and divisibility
  identities with their original generators, exponents and chart units.
  One `support32-witness.txt.gz` archive suffices for the identical support32
  witness; a different Bézout matrix is a different proof step.
- The dx1 exact saturation audit reads its compact polynomial certificate,
  full e2 obstruction formulas and the isolated equation input named in
  its source. A successful status message does not replace these inputs.
- Genus-one repeated-partition identities have their usable M2 source at
  `../validation/2026-10-10-repeated-partitions-independent-audit/countercheck.m2`.
  A nested replay snapshot is unnecessary once its actual source is restored.

The global H2 model loads its seventeen equations and domain polynomial from
`../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-02-name-repair/`.
The retained exact generator source reconstructs the twelve-generator spectral
system from the corrected sextic coefficient inputs; bulk Horner exports add
no separate mathematical assertion.
The two previously absent coefficient captures were recovered from the retained
complete forms: `Q-coefficient-6.txt` is `[x^6]Q`, equal to the saved octic
coefficient `[x^8]Fsrc`, and `F-source-coefficient-0.txt` is
`[x^0]Fsrc=wPar*[x^0]Q`. This restores input paths without a new incidence
calculation; the retained full forms satisfy `Fsrc=(x^2+vPar*x+wPar)*Q`.

A `.txt`, `.json` or compressed file can be the mathematical witness itself.
Conversely, a rank summary, process record, hash inventory or repeated PASS
output may add no argument once the exact proof and adequate checking inputs
survive. Follow the [artifact policy](../ARTIFACT_POLICY.md) and inspect the
content and consumers before changing support.

## Structural checks

The repository's existing validators check records and navigation, not
mathematical correctness:

```sh
python3 -B research/computations/validate_records.py
python3 -B research/computations/validate_result_records.py
python3 -B scripts/check_markdown_links.py --anchors
```

`validate_result_records.py` requires PyYAML. Verification status belongs
with the mathematical statement: distinguish a proof, a saved exact witness,
a source inspection and an actual rerun. None implies an unrestricted STCI
answer or an unperformed computation.
