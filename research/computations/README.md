# Exact computation checks

## Accepted sources through October 9 and their scope

The [current audited state](../AUDITED_STATE_2026-10-07.md) and
[integrated update](../RESEARCH_UPDATE_2026-10-07.md) control the
mathematical frontier. Run only changed or relevant sources; a successful
identity check is not a replacement for the linked geometric proof.

- `verify_mf6_infinity_universal.py` reconstructs the full e=0 type
  (d2,d3)=(4,5) incidence, moving cubic transition, annihilator minors
  with direct membership witnesses, and exceptional quartic fiber.
- `audit_mf6_e1_primitive_2026_10_07.py` independently reconstructs every
  primitive e=1 direction and complete quartic fiber in 35 ambient
  monomial columns, including both infinity boundaries and the
  remaining-carrier normalization identities. Its companion proof
  excludes e=1,D2=0 quartic STCI pairs in every mate degree.
- `verify_session_nonnormal_mf6_fiber_obstruction.py` independently checks
  the four surviving carriers' finite normalization, full C0 inverse
  support, duplicate-fiber gluing ratio and quadratic-field norm.
  Arbitrary powers are excluded by the written norm argument, not by
  checking finitely many powers.
- `verify_session_normal_carrier_progress.py` and
  `verify_session_normal_independent_audit.py` independently reconstruct
  the reduced-cycle/ADE numerical exclusions. The nonreduced sources
  `verify_session_normal_nonreduced_trees.py` and
  `verify_session_nonreduced_independent_audit.py` exhaust the necessary
  tree matrices by different representations. Their final Type-D
  geometric input is proved from the published hyperplane section basis.
- `audit_dx1_saturation_2026_10_07.py` reconstructs the original five
  obstruction coordinates, verifies the localized ideal witnesses and
  checks the universal coordinate bridge. Three-coordinate subsystem
  resultants do not supply this saturation.
- `session-localcoh-corners.py` verifies all polynomial-dual identities
  for three complete corner lift lines. `session-localcoh-origin-generic-dual.py`
  checks the stored rational-family dual after denominators are cleared.
  Both default identity checks use only Python's standard library.
  The generic dual retains its finite exceptional parameter locus.
- `audit_session_localcoh_endpoint_2026_10_07.py` reconstructs the
  complete four-family endpoint classification and first generic dual.
  `verify_session_localcoh_q2_dual_2026_10_07.py` and
  `verify_session_localcoh_q1_dual_2026_10_07.py` check the complete
  quadratic and first quartic exceptional fibers for every lower lift.
  These two coefficient verifiers use only the standard library.
  The Q3 and Q13 field-dual sources complete every exceptional root of
  this first rational family. Its independent rational-source and
  denominator-partition countercheck is preserved in
  `../validation/2026-10-08-first-endpoint-audit/countercheck.py`.
  The separate `verify_session_localcoh_family2_generic_2026_10_08.py`
  checks the second family's complete generic dual, retaining 26 points
  in its original factors of degrees 2,2,3,4,15. The new standard-library
  `verify_session_localcoh_family2_quadratics_2026_10_08.py` excludes both
  quadratic factors at all four geometric roots and every lower lift,
  rederiving the exact seeds and directions. A separate field
  countercheck and literal full actual tensor reconstruction are in
  `../validation/2026-10-08-family2-quadratic-audit/`. The remaining
  22 points have degrees 3,4,15 and retain each full lower lift line.
- `verify_session_localcoh_e1_simultaneous_2026_10_07.py` and
  `audit_session_socle_bridge_frames_2026_10_07.py` check the corrected
  two-target e=1,D2=0 ancestor obstruction and actual frame identities.
  The retracted single-target argument is not a dependency.
- `verify_mf6_e1_defective_structural.py` checks the intrinsic ideal
  module, cubic-class twists and bounded necessary matrices for the
  surviving positive-second-defect MF6 types. It is a reduction, not
  a complete exclusion of those types.
- `verify_session_nonnormal_structural.py` checks the genus arithmetic,
  Roman no-conic control and degenerate-pinch countermodel behind the
  explicitly conditional nonnormal carrier lemmas.
- `verify_session_uniform_bf_profiles.py` checks the exact necessary
  e=2 b=9,10,11 profiles. It does not certify their ambient existence
  or nonexistence.
- `verify_mf6_e1_d1_endpoints.py` checks the complete quartic spaces and
  localized birational maps of all six positive-defect endpoint orbits.
  The global mate argument retains the localized units and does not
  assume these open maps are finite normalizations.
- `verify_session_localcoh_conormal_splitting_2026_10_08.py` checks the
  necessary generator-bundle split and exact Hankel ranks. Its proof-note
  provenance input is required; the missing-input failure is retained.
- `verify_session_localcoh_e1_d4_algebraic_2026_10_08.py` reconstructs
  all 35 monomials and the complete seven-dimensional double-quartic
  space in both quadratic-field directions. Four covering minors and
  a distinct-diagonal last case prove every defect-four quartic fiber
  has dimension at most one, retaining all defect sections.
- `verify_session_veronese_pencils.py`,
  `verify_session_veronese_allmate_independent.py` and
  `verify_session_veronese_singular_pencil.py` check the exhaustive
  symmetric-pencil classification, full fibers and Jordan conductor jet
  for the all-degree `(P2,O(2))` carrier theorem. Its structural proof
  does not follow from a finite sample of powers.
- `verify_session_scroll_conductor_compression.py` checks trace algebras,
  branch contact, symbolic nilpotent powers, the unique C0 quadric and
  the entire quartic equation space singular along a smooth twisted
  cubic. `audit_scroll_twisted_cubic_equation_space_2026_10_08.py`
  independently rebuilds the literal rank-29 minor by differentiation
  and Fraction elimination. The all-degree exclusion additionally uses
  the supplied smooth-normalization and whole-conductor proof.
- `verify_session_mf6_principal_elliptic_2026_10_08.py` checks exact
  birational identities compressing the saved principal defect-one
  direction curve to `YE^2=XE^3+96XE-448`. The full ancestor contact
  theorem is now supplied by
  `verify_session_mf6_principal_rank_open_2026_10_08.py`, the all-35-column
  `verify_mf6_e1_d1_principal_boundaries_2026_10_08.py`, and the literal
  two-chart residue companion. The independent completeness audit is in
  `../validation/2026-10-08-principal-e1-d1-audit/`. These close all
  e=1,d2=1 common quartic ancestors, including the node's dimension-four
  fixed-cubic space. They do not alone exclude the unique carriers'
  higher-degree mates; that carrier locus is separately finite.
- `verify_session_mf6_rhalf_scroll_2026_10_08.py` binds the actual
  exceptional p=8,r=1/2 quartic to its finite F0 normalization, complete
  normalization ring and entire nonreduced conductor ideal. Its all-mate
  argument is in the separate structural proof.
- `verify_session_scroll_nongorenstein_cubic_2026_10_08.py` checks the
  literal Hilbert--Burch ideals, generic Artin rings, exact nil-image
  constraints and realizable cusp projection. The complete smooth
  rational quartic-scroll all-mate theorem additionally uses the
  independently audited differential lemma and full divisor/fibre
  arguments. It retains nongorenstein actual conductors and makes no
  classification claim for other normalization types.
- `verify_session_mf6_principal_weighted_candidate_2026_10_09.py`
  checks all eighteen actual ambient forms, weighted polynomial syzygies,
  the actual first-normal octic and fixed degree-210 determinant matrix.
  `audit_session_mf6_weighted_candidate_2026_10_09.py` independently
  reconstructs coefficients, matrix, sample determinant 22 modulo 101,
  and simple/multiple infinity controls. The separate geometry and
  Bezout proof give at most 630 necessary principal mate parameters,
  not their exact list or an exclusion at every zero.
- The root-level `../../computations/verify_singular_delpezzo_four_A1_family_2026_10_09.py`
  checks universal four-parameter normalization and full-fiber identities.
  Its separate countercheck and frozen audit are in
  `../validation/2026-10-09-four-A1-family-audit/`. The all-degree
  geometric exclusion applies to the displayed open family and does
  not exhaust all four-A1 projections.
- The root-level `../../computations/verify_delpezzo_D5_torsion_filter_2026_10_09.py`
  enumerates all 428 embedded reflection-closed root subsystems and
  checks their integer saturation with HNF. The independent signed
  set-partition countercheck in `../validation/2026-10-09-D5-root-audit/`
  uses no reflection search or HNF. The missing-root proof leaves
  only 4A1 or A3+2A1 and even mate degree. Its weak-del-Pezzo/ADE
  geometric hypotheses follow from separately audited genus-one
  divisor arguments; the lattice checker alone does not prove them.

The genus-zero cone, nonrational ruled-surface and genus-one adjoint
proofs are structural divisor arguments, recorded in the
[October 9 acceptance](../notes/2026-10-09-session-results-acceptance.md).
They do not acquire their validity from these finite source counts.

The [validation record](../notes/2026-10-06-session-validation.md)
preserves source hashes, isolated generated outputs, meaningful repairs
and failed diagnostics. Additional accepted sources from this continuation
have separate dated logs; counts are not inflated by imported modules.
The [October 7 continuation replay](../validation/2026-10-07-continuation/results.json)
adds isolated checks of newly completed sources while preserving the
earlier baseline and its failed diagnostic records.
The [October 8 reconciled index](../validation/2026-10-08-continuation-index/index.json)
binds 97 distinct top-level sources to latest PASS evidence and counts
110 explicitly indexed executions. Nested/imported checks are not counted
as extra sources. It records the two central continuation failures and
repairs and the unavailable bytes of one superseded Veronese source
revision; the current strengthened revision has a separate passing
snapshot. See the [checkpoint](../notes/2026-10-08-session-checkpoint.md)
for the limits of those records and unfinished computations.

Current runtime paths, when available:

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/audit_mf6_e1_primitive_2026_10_07.py
python3 research/computations/session-localcoh-origin-generic-dual.py
/opt/homebrew/bin/M2 --script research/computations/session_dx1_compact_certificate_2026_10_06.m2
```

## Earlier retained sources

The original verification scripts in this directory, together with the dated
2026-10-05 companions and the preserved mixed-degree script under
`../scratch/degree6`, use exact symbolic arithmetic in SymPy or Macaulay2;
the Python checks do not use floating point calculations.

- `verify_c0.py` checks the parametrization ideal, the characteristic 2 and 3
  radical pairs, the uniform positive-characteristic family in characteristics
  2, 3, 5, and 7, coordinate saturations, and wrong-characteristic controls.
- `verify_normal_bundle.py` checks the two-chart conormal transition, its
  extension class, an independent Jacobian-syzygy determinant, and the local
  characteristic-3 primitive triple.
- `verify_primitive_obstruction.py` checks the quadratic transition jet used
  in the Banica--Forster obstruction calculation.
- `verify_all_quartic_primitive_obstruction.py` checks the marked
  degree-three-map normal form, the six homogeneous obstruction coordinates,
  and the non-incidence identities that eliminate primitive triples for every
  characteristic-zero smooth rational quartic.
- `verify_positive_quartic_descent.py` checks the cusp semigroup lemma,
  representative Frobenius-descent supports, and the exceptional
  characteristic-3 normalization identities used in P-012.
- `verify_degree6.py` checks the degree-six symbolic square, its five
  residual classes on the quadric, the cubic symbolic-power boundary, an
  integral sextic singular exactly along the curve, and the first-normal
  discriminant/resultant calculations.
- `verify_chow_form.py` checks a compact 10-term Pluecker-coordinate formula
  for the Chow form of \(C_0\) against the exact 64-term binary resultant of
  two hyperplane pullbacks. It also verifies Pluecker degree four and
  coefficient bidegree \((4,4)\).
- `verify_typeb45_endpoint_certificate.py` checks the terminal rational
  identity at the proposed dense type-B survivor and the exact Bezout
  certificate excluding the proposed boundary survivor.  Its scope is
  intentionally narrower than the mathematical proof: it does not derive the
  transition recursion, justify Cech reductions, or prove chart exhaustion.
- `verify_chow_pencil_45.py` checks the exact dimensions and bases of the
  restricted carrier spaces excluded by one Schubert-line pencil, including
  the stronger 13-dimensional quartic and 28-dimensional quintic spaces.  It
  also checks the Chow restriction, coefficientwise resultant orders, and an
  explicit irreducible-quartic pair that passes this pencil but fails the
  reversed pencil.  It does not certify the full Grassmannian identity.
- `verify_typeb45_boundary.py` independently reproduces the full moving-frame
  obstruction on the \(b_0=0\) type-B boundary, including all six Cech
  coordinates and the characteristic-zero unit certificate.  It takes the
  lower Bănică--Forster delta/gamma chart data as input and does not cover the
  distinct rank-zero corner \(a_0=b_1=0\).
- `verify_typeb45_corner.py` checks the full moving-coordinate
  second-order coefficient, the three rank-zero parameters, and a bounded
  gamma-gluing calculation at the formerly missed corner.  Its final
  length-four statement counts a displayed monomial basis rather than
  deriving a Gröbner basis; the exhaustive proof uses
  \(H^0(O_{\mathbf P^1}(-3))=0\) and the elementary quotient
  \(k[m,\ell]/(m^2,m\ell,\ell^3)\).
- `verify_localcoh_degree4_counterexample.py` checks membership in
  \(I_{C_0}\), the nonconstant proportional first-symbol rows, the two exact
  polynomial identities, and generic coprimality over \(\mathbb Q(\lambda)\).
  It does not construct or assert a common local-cohomology ancestor.
- `verify_localcoh_degree4_allstage_certificate.py` checks P-043's two sparse
  coefficient functionals for stages \(N=2,\ldots,8\): annihilation of all
  correction and boundary spaces, target value \(-1\), and exact compatibility
  with multiplication by \(qB\).  The written proof is uniform in \(N\); this
  finite exact check does not classify other degree-four pairs.
- `verify_split22_boundary_survivor.py` checks the content-free
  \(d=1,[2,2]\) two-ramified-root first-normal survivor, including both factor
  evaluations and all eleven sextic normal-image equations.  It does not
  construct an ambient integral sextic or a mate.
- `verify_general_conductor_power.py` checks the exact normalization,
  conductor, pinch, and ordinary-power identities used in the literature
  refresh. It is an algebraic example, not an STCI theorem.
- `verify_localcoh_finite_principal_parts.m2` computes the first five
  principal-part dimensions for the quartic and checks the stage-4 injection
  and socle-multiplier statement in Macaulay2.
- `verify_localcoh_quartic_ratio_t_slice.py` checks the all-stage coefficient
  functionals excluding the ratio-t and ratio-t^3 slices, including their
  boundary specializations.
- `verify_mixed46_regular.py` checks the exact regular degree-(4,6) local
  equations used to exclude the pure constant directions.
- `verify_quadric_powers.m2` checks symbolic-power equals ordinary-power
  formulas for the monomial and nonmonomial integral divisors used as a
  special-case laboratory.
- `verify_residual_cycle.py` checks 81 exact residual-cycle lattice instances
  and the A <= D_{m-1} bound used in the mixed-(4,6) analysis.
- `verify_split22_boundary_lift.py` checks the fixed split-[2,2] ambient
  lift, node/A1 collisions, and the Mumford branch-intersection counts.
- `verify_typea45.py` independently reconstructs the type-A (4,5) parameter
  charts and terminal obstruction.
- `verify_typeb45_dense.py` independently rederives the dense type-B
  elimination boundaries and terminal obstruction.

- `../scratch/degree6/verify_mixed45_reduction.py` checks the quartic and
  quintic first-normal maps for the \((4,5)\) problem, the two allowed gcd
  strata, and, after assuming the regular-ratio missing-section normalization,
  exact augmented-minor exclusions for three carrier families. It does not
  prove that the ratio is regular or cover the newly separated pole strata.
  Its SHA-256 at handoff is
  `862ec150664459fc94187164bcaa1d25e87c5f815e589fff1608a28efc6a89d5`.

The dated exploratory sources under `../scratch` are retained separately:
`explore_mixed46_e0.py`, `mixed46/local_lattice.py`, and
`primitive47/obstruction.py` support the corresponding notes but are not
standalone theorem certificates.

Run them with a Python environment containing SymPy:

```sh
python3 research/computations/verify_c0.py
python3 research/computations/verify_normal_bundle.py
python3 research/computations/verify_primitive_obstruction.py
python3 research/computations/verify_all_quartic_primitive_obstruction.py
python3 research/computations/verify_positive_quartic_descent.py
python3 research/computations/verify_degree6.py
python3 research/computations/verify_chow_form.py
python3 research/computations/verify_typeb45_endpoint_certificate.py
python3 research/computations/verify_chow_pencil_45.py
python3 research/computations/verify_typeb45_boundary.py
python3 research/computations/verify_typeb45_corner.py
python3 research/computations/verify_localcoh_degree4_counterexample.py
python3 research/computations/verify_localcoh_degree4_allstage_certificate.py
python3 research/computations/verify_split22_boundary_survivor.py
python3 research/scratch/degree6/verify_mixed45_reduction.py

# Dated 2026-10-05 companions
python3 research/computations/verify_general_conductor_power.py
python3 research/computations/verify_localcoh_quartic_ratio_t_slice.py
python3 research/computations/verify_mixed46_regular.py
python3 research/computations/verify_residual_cycle.py
python3 research/computations/verify_split22_boundary_lift.py
python3 research/computations/verify_typea45.py
python3 research/computations/verify_typeb45_dense.py
# The two .m2 files use Macaulay2 rather than Python.
/opt/homebrew/bin/M2 --script research/computations/verify_localcoh_finite_principal_parts.m2
/opt/homebrew/bin/M2 --script research/computations/verify_quadric_powers.m2
```

On 2026-09-30 all 15 original script executions passed sequentially under the temporary environment
`/private/tmp/stci-cas-venv/bin/python`. On 2026-10-05 the original suite and
the dated Python companions passed with `PYTHONDONTWRITEBYTECODE=1`; the dated
Macaulay2 companions passed with `/opt/homebrew/bin/M2 --script`. Both the system Python and the bundled
workspace Python failed before running any assertion because SymPy was not
installed. The proofs recorded in `../RESEARCH_RECORD.md` do not rely on the
continued existence of that temporary environment.

## Full four-parameter e=2 obstruction data (2026-10-05)

- `e2_full4_obstruction_2026-10-05.txt` is the durable exact computation dump for
  the four-parameter (e=2) cubic obstruction, with strong cross-checks.
  It records the resultant (Delta), all five exact obstruction numerators
  (G_1,ldots,G_5), the raw mismatch denominator
  (32z^{25}Delta^3), exact divisibility of the five raw numerators by
  (Delta^2), and the exact (b=0) specialization check against the
  independently audited three-parameter calculation. It is formula data, not
  by itself a proof that the parameter cross-section exhausts the geometric
  problem; that symmetry argument and the scope warnings are in
  `../notes/2026-10-05-e2-full-obstruction.md`.


### P-044 survivor cubic certificate (2026-10-05)

- \`verify_p044_survivor_cubic.py\` is a compact independent certificate for
  P-045. It checks the displayed Bezout identity, reconstructs the canonical
  moving-coordinate primitive triple for the explicit P-044 survivor, verifies
  exactly that \(H_x\) vanishes modulo \(\epsilon^3\), and checks that the
  seven displayed cubic coefficients reconstruct \(H_x\). It deliberately
  does not recompute or classify the full P-044 obstruction zero locus.

Run with:

\`\`\`sh
python3 research/computations/verify_p044_survivor_cubic.py
\`\`\`


## 2026-10-06 audited consolidation certificates

This is the historical October 6 consolidation status; current results
are routed by `../AUDITED_STATE_2026-10-07.md`. The consolidation branch
intentionally omitted exploratory scratch and known-faulty historical
certificates. The following promoted checks accompanied its audited results:

- `verify_primitive_quadruple_universal.py` — universal fourth-obstruction zero-locus certificates for the primitive e=2 analysis.
- `verify_primitive_quartic_factor_audit.py` — independent reconstruction of the quartic symbol/contact calculation and factorization theorem.
- `verify_primitive_triple_parity.py` — exact parity-family triple/fourth-layer checks; scoped only to that family.
- `verify_normal_quartic_simple_elliptic.py` — numerical verification for the simple-elliptic normal-quartic exclusion.
- `verify_normal_rational_carrier_compression.py` — determinant/denominator bounds for the remaining rational-resolution normal quartics.
- `verify_mf6_defect12.py` and `verify_mf6_type3.py` — audited multiplicity-six defect and type-3 calculations.
- `verify_localcoh_direction_image.py`, `verify_localcoh_pure_direction_audit.py`, `verify_localcoh_constant_direction_apolar.py`, and `verify_localcoh_generic_length_model.py` — retained local-cohomology direction/subfamily checks.
- `localcoh-incidence-2026-10-06.py` with its JSON certificate and `localcoh-incidence-parity-dual-2026-10-06.py` with its JSON certificate — exact tensor/dual incidence data.
- `verify_split4_nonramified.py`, `verify_split22_chart_audit.py`, and `verify_split22_finite_reduction.py` — split-carrier reductions; these do not assert a global exclusion.
- `verify_dx1_a_half_boundary.py` and `verify_dx1_p044_residual.py` — dx=1 boundary/residual calculations. The residual saturation problem remains OPEN; these scripts do not certify emptiness of the residual locus.

Do **not** use `localcoh-symbol-paritycheck.m2` or `localcoh-symbol-seedcheck.m2` as theorem certificates; their quartic-basis construction was faulty and they are intentionally absent from the consolidation diff.

The older scratch references below are historical instructions from earlier research phases. They are not part of the 2026-10-06 promoted certificate set.
