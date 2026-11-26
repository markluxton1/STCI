# Mathematical approaches and their interfaces

## Central problem and research selection

For the fixed rational quartic \(C_0\subset\mathbf P^3\) in characteristic zero, the unrestricted question concerns **actual homogeneous pairs** \(F\in I_{C_0}(a)\), \(G\in I_{C_0}(b)\) forming a proper intersection. Its effective cycle is \([V(F,G)]=m_{C_0}[C_0]+R\), where \(ab=4m_{C_0}+\deg R\). Thus maximal generic multiplicity \(m_{C_0}=ab/4\) is equivalent to sole support. This is classical degree exhaustion and a reformulation of STCI, **not** a new obstruction or a reason to assume a degree-independent bound exists.

The principal investigative interfaces are **actual global realization and formal normal geometry**, **full-ideal torus degeneration with its coverage problem**, and **residual construction or absorption**. Each must ultimately constrain or construct actual proper equation pairs. Local cohomology, fixed-carrier normalization, spectral roots, and prescribed arithmetic lifts remain mathematically valid methods and sources of tests, but bounded results in these settings do not acquire unrestricted coverage without a separate bridge. No approach currently proves a degree-independent obstruction.

Before prioritizing new work, state the exact class of equation pairs covered, the theorem or decision obtainable, its implication for unrestricted STCI, and the strongest existing result that leaves the gap open. A bounded question may remain open without being an active priority.

Use the [research index](INDEX.md) for exact proof routes and the
[active front door](investigations/proof-audit/open-items.md) for current work.
The map routes to mathematical owners; the strategic queue alone ranks tasks.

| Framework | Mechanism and connection to other approaches |
| --- | --- |
| [Carrier normalization](frameworks/carrier-normalization/index.md) | Actual projections, full inverse support and descent through the conductor. Connect local normal geometry to the global divisor problem only after fixing the carrier, polarization and all inverse branches. |
| [Formal normal geometry](frameworks/formal-normal-geometry/index.md) | Saturated layers, full initial ideals, the filtered equation defect and simultaneous realization by two carriers. In families a flat total intersection can have a normal graded jump; see the arithmetic control. |
| [Global equation realization](frameworks/global-equation-realization/index.md) | Actual source spaces, lifting quotients, Sylvester bundles and the complement. Projection and liaison supply constructive sources; missing ambient sections can destroy ACMness after projection. |
| [Residual construction](frameworks/residual-construction/index.md) | Generic length, projective residual cycles, attachment and marked absorption. Local transfer must persist in an actual proper pair before degree exhaustion can be applied. |
| [Spectral roots](frameworks/spectral-roots/index.md) | Genus-one Picard torsion produces graded equations. Actual embedded sextic and octic lifts have different source conditions; a positive octic lift can still leave a residual curve. |
| [Chow realization](frameworks/chow-realization/index.md) | Full coefficient chains and a norm characterize the exact translated cycle of a proper pair under the boundary condition. General repeated-cycle construction and unrestricted first-moment vanishing are open. |
| [Full torus boundaries](frameworks/torus-supported-boundaries/index.md) | Opposite limits of the full ideal preserve Hilbert data and can gain generators. A supported deformation needs a test of the actual moving ideal. |
| [Embedded torus quotients](frameworks/embedded-torus-quotients/index.md) | Embedded finite algebras and endpoint images recover more than the abstract quotient. Pure limit components and embedded lengths are known separately; comparing the full opposite endpoints in one family is further work. |
| [Arithmetic supported lifts](frameworks/arithmetic-supported-lifts/index.md) | Positive-characteristic equations, normal specialization and obstruction to prescribed lifts. Endpoint root defects have no proved identification with spectral Picard torsion or carrier Weil classes. |
| [Local cohomology](frameworks/local-cohomology/index.md) | Simultaneous ancestors in actual homogeneous multiplication spaces. The quartic two-target reduction gives a bounded problem; higher multiplier degrees belong to the full-module question. |

## Current mathematical interfaces

### Carriers, divisor classes, and normal replacement

The [carrier-degree account](frameworks/carrier-normalization/degree_exclusions.md)
separates all-mate exclusions on fixed carriers from pair-specific reductions.
The arbitrary-mate quartic-carrier theorem remains the independent base case;
neither the quintic nor sextic landscape is completely excluded.

For an integral carrier regular at the generic points of the supported curves,
the [normalized Hodge matrix and actual downstairs almost-Cartier relations](arguments/carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices)
give distinct numerical and integral conditions. In the singleton case,
finite downstairs index plus normalized Hodge equality is the exact mate test.
Upstairs normalization index alone omits conductor descent. On a fixed normal
carrier the minimal multiplicity equals the Cartier index; Picard saturation
is a classical input, not a new characteristic-zero theorem.

The [actual normal-replacement argument](arguments/carriers/normal_carrier_divisor_geometry.md#47-all-degree-actual-normal-carrier-replacement)
applies to the generically curvilinear branch of an actual pair, preserving
its CI ideal. It does not replace an entirely-thick pair by a normal one.
Moving high-index points of a general replacement must be distinguished from
the fixed nonprimitive defect divisor. The same owner gives the reduced-gcd
ADE/rank test and its precise scope; large indices alone are not obstructions.
The [branch valuation and principalization comparison](arguments/carriers/numerical_surface_pullback.md)
retains individual inverse branches, exceptional energy and actual first-blowup
coefficients in the entirely-thick branch.

The [branch-energy generality](arguments/carriers/branch_energy_generality.md)
needs only \(4d+2g-2<2d\sqrt d\), covering smooth rational curves of
degree at least three; it excludes the specified no-vertical singleton or
proportional-branch carrier locus, not all carriers. Actual Cartier relations
also localize denominator corrections beyond branch coefficients to shared
points. In the generically curvilinear quartic branch, RG2's stronger
prime-divisor gcd test forces, for example, a hypothetical \((14,14)\)
pair to have nonreduced common first-normal divisor. It leaves that stratum
and the entirely-thick branch open.

### Residual attachment and marked finite transfer

The [two-blowup dictionary](arguments/residuals/blowup_residual_geometry.md)
identifies actual homogeneous sources with sections having prescribed conic
vanishing and compares their residual cycles. Its marked \(V_5\) equation
correspondence, nef bounds and equality strata require the actual lifting and
contact conditions in that proof. They are not arbitrary-carrier exclusions.

The [layerwise attachment theorem](arguments/residuals/layerwise_attachment_and_triples.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component)
and [actual attachment/local-cohomology comparison](arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers)
connect saturated defects, genuine residual attachment and actual equation
quotients. For a proper pair through \(C\), the first quotient \(Q_1\)
vanishes exactly for sole support. Universal nonvanishing would therefore
already be the desired non-STCI theorem; local duality supplies a detector,
not independent positivity. The BF triple calculation is a useful calibration,
while the lci quadruple prevents extrapolating its torsion identity to every
multiplicity. A characteristic-zero candidate has multiplicity at least nine,
so triples are not a direct candidate stratum.

The marked finite-transfer and border-product calculations retain the actual
image algebra beyond its index. Their primitive marked-edge hypotheses are
essential. They do not identify a graph modification index with a torus-endpoint
Sylvester index or resolve the nonprimitive source incidence.

### Chow cycles, actual equations, and finite source depth

The [Chow realization framework](frameworks/chow-realization/index.md)
starts with the full translated-cycle incidence. It routes to exact reduced
and quartic realization, the full coefficient chains and norm, and the
separate first-moment and endpoint tests for repeated cycles. The
[quartic exception](arguments/torus/quartic_hilbert_chow_limits.md)
distinguishes the full Hilbert boundary from the cycle. The
[arrangement strata](results/arrangement_strata_and_orders.md)
and [relative blowup models](arguments/torus/relative_arrangement_blowup_family.md)
describe where marked incidence and individual section orders persist.

The provisional [cycle-first geometric account](arguments/torus/transverse_coefficient_realization_synthesis.md) compares the paired cycle with moving transverse neighborhoods, conormal maps and the same global equations in complementary product models. The [plane-family criterion](arguments/torus/plane_pencil_equation_bundles.md) distinguishes completion to a full fixed-type plane CI from triviality of the minimal generator bundles. The [marked configuration boundary](arguments/torus/marked_chow_configuration_boundary.md) and [opposite endpoint incidence](arguments/torus/marked_chow_endpoint_incidence.md) distinguish stable extension across collisions from actual embedded CI limits. Neither the boundary gluing nor the scalar trace identities prove universal first-moment vanishing.

The [conjugate-pair section hull](results/sign_symmetrized_source_defect.md),
[actual-family specialization maps](arguments/normal-geometry/source_specialization_and_linkage.md)
and [integral first-jet product](results/integral_first_jet_lifting.md)
compare different constraints on actual equation sources. The
[cross-framework synthesis](arguments/torus/universal_first_moment_corpus_review.md)
tracks their implications for moment vanishing. The [elliptic
contact/spectral comparison](arguments/carriers/elliptic_contact_and_spectral_comparison.md)
retains the independent constructive family.

The [Jacobian radical criterion](results/jacobian_radical_support.md)
and [full residue criterion](arguments/torus/sole_support_first_jet_gate.md#full-exact-stci-jet-criterion-ideal-powers-and-the-perfect-residue-pairing)
give exact fixed-degree tests for sole support. The
[fixed-depth determinant theorem](results/fixed_depth_determinant_incidence.md)
gives large-degree residual controls for any fixed number of leading
coefficients, including reduced intersections of normal integral
carriers in its stated range. Compare the [sharp center-jet
range](arguments/torus/chow_matched_equation_layers.md#sharpness-and-the-last-missing-center-layer)
and the [canonical projection
order](arguments/carriers/tame_projection_sections.md#the-canonical-projection-order)
for distinct constraints on the original equations.

## Questions and active work

The [strategic queue](investigations/proof-audit/knowledge-gain-priorities.md#current-choice-and-reassessment)
owns the comparison of actual next tasks. Single-chain Chow realization with
its norm and boundary conditions and
the [whole elliptic inverse-support locus](results/elliptic_inverse_support.md)
are substantial competing questions. Low-order determinant tests are bounded
diagnostics; they acquire no all-degree priority from their small matrices.

The [common-quadric boundary theorem](arguments/equations/common_quadric_chow_boundary.md)
and [resultant blowup calculation](arguments/equations/common_quadric_resultant_blowup.md)
exclude the stated clean strata and the \(h_2=0\) center, including higher
contact arcs in that scope. Positive-\(h_2\) cancellation, zero restrictions
and common ambient cofactors remain distinct open strata.

The [quadratic-conductor account](results/moving_quadratic_conductors.md)
compares global postulation with actual local lattices on one object.
Its scalar length test cannot obstruct a generically regular smaller carrier;
the remaining questions concern actual homogeneous kernels and embedded graph
corrections. The [full toric conductor comparison](arguments/linkage/toric_limit_conductor_comparison.md)
retains both endpoint corrections, with no general sign inequality.

The [full-limit comparison](investigations/quotient-hilbert-comparison/index.md)
remains active. The [supported-generator incidence test](investigations/supported-generator-incidence/index.md)
remains planned and unperformed without a declared supported family.
The [contact-boundary map](arguments/torus_hilbert_boundary.md#involutivity-persists-through-the-full-torus-boundary)
depends on actual embedded endpoint corrections, not just their lengths.
Pure involutive constant-orbit controls can even have the CI Hilbert polynomial
without two homogeneous generators.

The remaining frameworks retain their own exact gaps:
[actual spectral-root lifts](frameworks/spectral-roots/open_root_lifts.md),
[arithmetic specialization](frameworks/arithmetic-supported-lifts/index.md),
[normal realization](frameworks/formal-normal-geometry/open_normal_geometry.md),
[carrier cases](frameworks/carrier-normalization/open_carrier_cases.md),
[marked absorption](frameworks/residual-construction/index.md), and
[actual local-cohomology ancestors](frameworks/local-cohomology/open_quartic_ancestors.md).
No numerical similarity identifies their defect modules or supplies a missing
comparison map. The unrestricted characteristic-zero STCI question remains open.
