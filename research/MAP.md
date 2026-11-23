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

The [quartic-pencil classification](results/quartic_chow_pencil_classification.md)
classifies proper \((4,4)\) pencils in characteristic zero, including a
non-invariant exceptional orbit. Liaison and the canonical module explain
its rigidity. Its [K3/even-eight carrier](arguments/torus/quartic_exceptional_carrier_geometry.md)
and [opposite full Hilbert limits](arguments/torus/quartic_hilbert_chow_limits.md)
have different information from the Chow cycle. The characteristic-two
sole-support construction is separate from that classification.

The [trace-moment theorem](arguments/torus/chow_arrangement_moments.md)
forces \(M_1=\sum n_i u_i/v_i=0\) on its proved invariant/eigenform/congruence
loci, including reduced CI arrangements. The same vanishing for arbitrary
non-invariant repeated-cycle pairs is an open conjecture. The
[spectral–Jacobian residue bridge](arguments/torus/spectral_jacobian_first_jet_bridge.md)
expresses \(2M_1\) as the first-jet residue pairing on the full translated
realization locus; it does not force isotropy there.

The [full residue criterion](arguments/torus/sole_support_first_jet_gate.md#full-exact-stci-jet-criterion-ideal-powers-and-the-perfect-residue-pairing)
is a finite exact sole-support system in each bidegree. Explicit actual pairs
with residual curves pass its two leading tests. The full
[opposite Chow envelopes](arguments/torus/full_transverse_chow_pullback_envelope.md)
and [quadric/cubic polarizations](arguments/torus/weighted_chow_quadric_cubic_polarizations.md)
give exact same-generator incidences. Their norm gate is required to recover
exact component multiplicities. The [saturation and interpolation theorem](arguments/torus/spectral_interpolation_and_polar_saturation.md)
shows that the opposite coefficient chains impose equivalent membership on
coordinate-saturated ideals, including full-translated-support CIs. A second
polarization adds boundary coverage, not an independent cofactor obstruction.
On the stratum of distinct spectral values, \((H,K)\) recovers all paired
torus parameters, even with repeated multiplicities; collisions need higher
polars. This parameter compression does not replace full-chain membership or
the norm condition by the two first polars.

The [paired source determinant](arguments/torus/chow_arrangement_moments.md#a-two-operator-determinant-recovers-the-full-transverse-chow-polynomial)
recovers the full transverse Chow polynomial on the translated locus and
detects sole support under its finite-pencil hypotheses. Its coefficient of
order \(j\) uses only source depth \(4j\). With varying binary leading
forms these coefficients are regular on the resultant-nonzero source open;
polynomial dependence requires fixing leading forms or clearing denominators.
Roots-of-unity cycles can cancel arbitrarily many initial coefficients while
retaining residual translates; those controls do not assert actual CI
realizability. The [actual jet-source theorem](arguments/equations/global_equation_jets.md)
likewise shows eventual freedom at every fixed center-jet depth. In particular,
for \(a,b\ge4r+3\), the attainable tuples \(\Delta_1,\ldots,\Delta_r\)
are unchanged by imposing containment of \(C\). This does not prove the
truncated pure target is attainable; joint global conditions remain. A useful
all-degree obstruction must add actual simultaneous source compatibility,
rather than another scalar support detector.

This determinant-image equality, and the analogous degree-\((2,3)\)
characteristic-coefficient tower statement, hold over any field; their proofs
use linear lifting and characteristic-polynomial scaling without Newton
division. The characteristic-zero moment/trace assertions retain their scope.

The [sharp center-jet calculation](arguments/torus/chow_matched_equation_layers.md#sharpness-and-the-last-missing-center-layer)
has cokernel dimension \(N+1\) at degree \(N+1\), and vanishes in degrees
at least \(N+2\). Sharpness of that source map does not establish sharpness
of the determinant-image threshold. The [canonical projection order](arguments/carriers/tame_projection_sections.md#the-canonical-projection-order)
packages both endpoint failures in one rank-four algebra with rational
normalization and genus \(1\le\delta\le6(m-1)\), under its tame
sole-support hypotheses. It has no proved comparison forcing residual support.

### Arrangement families and their boundaries

The [arrangement investigation](investigations/chow-quotient-arrangement-bridge/index.md)
connects the quotient fan, endpoint Hilbert data, equation incidence and blowups.
The [endpoint evaluation ranks](arguments/torus/arrangement_endpoint_delta.md)
compute reduced-union Hilbert polynomials. In the
[relative construction](arguments/torus/relative_arrangement_blowup_family.md),
the union must be formed anew on a rank stratum: restriction of the universal
scheme union can acquire an embedded nilpotent. Correct Rees specialization
requires control of ideal powers as well as the reduced union. The separate
smooth model blows up disjoint lifted curves and recovers containing-section
spaces; it is not an identification with the direct singular blowup.
Collision strata, general two-equation realization and complementary
contractions retain their separate missing steps.

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
