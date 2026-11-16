# Intersections and multiple structures through the fixed quartic

Fix an algebraically closed field and the embedding
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). Its unrestricted STCI status in
characteristic zero is **open**. Any defining pair in characteristic zero
would have both degrees at least five by the
[quartic carrier exclusion and factor reduction](results/quartic_carrier_exclusion.md).
The same curve has a [quartic carrier presentation in every positive characteristic](arguments/arithmetic/positive_characteristic_constructions.md).

A proper degree-\((a,b)\) pair through \(C_0\) gives the cycle
\([V(F,G)]=m[C_0]+R\), with \(ab=4m+\deg R\). Generic length,
exceptional contact, and the residual projective cycle play different
roles. Sole support is the case \(R=0\).

To develop or compare approaches, start with the [framework map](MAP.md).
For the embedding itself, see the [fixed curve geometry](arguments/curve/fixed_quartic_geometry.md)
and [special plane and line sections](arguments/curve/special_plane_and_line_sections.md).
Find exact claims in the [catalog](CATALOG.md) and external sources in the
[shared literature](literature/README.md).

## Find a statement, proof, or open question

Use `python3 scripts/research.py show ID` for a known claim, its proof routes
and declared consumers. For a lane, start with the links below or run
`python3 scripts/research.py route <lane> --compact`. Pass selected addresses
to `python3 scripts/research.py section ADDRESS [ADDRESS ...]`. The route
without `--compact` expands the starting sections.

| Lane | Starting sections | Proofs, controls, and open dependencies |
| --- | --- | --- |
| `quartic` | [Status and degree bounds](frameworks/carrier-normalization/degree_exclusions.md#52-factors-and-the-degree-bound), [integral quartic carriers and factor reduction](results/quartic_carrier_exclusion.md#complete-quartic-carrier-exclusion-for-the-fixed-c0) | [Full quartic-carrier proof](arguments/carriers/quartic_carrier_proof.md), [carrier cases](frameworks/carrier-normalization/open_carrier_cases.md) |
| `lifting` | [Equations for every \(p>0\)](arguments/arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-a-quartic-carrier), [prescribed nonlifting hypotheses](results/prescribed_z4_arithmetic_nonlifting.md#statement-and-hypotheses) and [limitations](results/prescribed_z4_arithmetic_nonlifting.md#limitations), [arithmetic lift strategy and open bridge](frameworks/arithmetic-supported-lifts/index.md#bridges), [strong lifts](arguments/arithmetic/frobenius_power_lifting_precision.md#strong-lifts-and-the-exact-unramified-precision-shift) | [Nonlifting proof](results/prescribed_z4_arithmetic_nonlifting.md#current-proof), [prime-to-\(p\) extraction](arguments/arithmetic/prime_to_p_power_extraction.md#extraction-theorem), [exact strong-lift precision](arguments/arithmetic/frobenius_power_lifting_precision.md#exact-obstruction-level-for-the-prescribed-quartic-construction), [endpoint specialization theorem](arguments/arithmetic/frobenius_power_lifting_precision.md#root-specialization-and-the-remaining-endpoint-defects), [prescribed \(\mu_4\) normal base change](results/quartic_normal_initial_base_change.md#statement) |
| `torus` | [Invariant-ideal scope](results/invariant_supported_ci_exclusion.md#scope), [exclusion](results/invariant_supported_ci_exclusion.md#statement) and [limits](results/invariant_supported_ci_exclusion.md#limitations), [sextic eigenpair scope](results/sextic_eigenpair_quotient_bound.md#scope) and [STCI-R-0043 sharp length bound](results/sextic_eigenpair_quotient_bound.md#statement), [STCI-R-0070 intrinsic endpoint statement](results/intrinsic_limits_endpoint_fibers.md#statement), [opposite full limits and generation](frameworks/torus-supported-boundaries/index.md#directional-loci) | [Invariant-ideal proof](arguments/torus_hilbert_boundary.md#invariant-supported-complete-intersections), [sharp sextic bound proof](arguments/torus_sextic_residuals.md#the-sharp-sextic-eigenpair-bound) and [STCI-R-0043 review](results/sextic_eigenpair_quotient_bound.md#review), [endpoint theorem proof](arguments/torus_hilbert_boundary.md#endpoint-fibers-in-the-two-intrinsic-limits) and [STCI-R-0070 review](results/intrinsic_limits_endpoint_fibers.md#review), [moving-ideal generator test](arguments/torus_hilbert_boundary.md#the-moving-ideal-generator-test), [residual and loss-of-generation controls](frameworks/torus-supported-boundaries/index.md#controls) |
| `normal-orders` | [Displayed orders and full initial generators](frameworks/formal-normal-geometry/from_symbols_to_equations.md#31-generic-normal-forms-versus-global-relations), [equal-order smooth-root bridge](results/actual_ci_smooth_root_bridge.md#statement), [integral quartic carriers](results/quartic_carrier_exclusion.md#complete-quartic-carrier-exclusion-for-the-fixed-c0) | [Smooth-root bridge proof](arguments/spectral/uniform_root_towers_and_inseparable_bridges.md#2026-10-15-generalization-inseparable-root-blowup-bridge), [entirely-thick bounds](results/entirely_thick.md), [unequal orders and the quotient relation](frameworks/formal-normal-geometry/from_symbols_to_equations.md#unequal-orders-and-the-quotient-relation) |
| `incidence` | [Generator incidence scope](investigations/supported-generator-incidence/index.md#scope), [question](investigations/supported-generator-incidence/index.md#question) and [method](investigations/supported-generator-incidence/index.md#method), [quotient-to-Hilbert scope](investigations/quotient-hilbert-comparison/index.md#scope) and [question](investigations/quotient-hilbert-comparison/index.md#question) | [Closed incidence and both full limits](arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits), [directional loci](frameworks/torus-supported-boundaries/index.md#directional-loci), [proof of the moving-ideal generator test](arguments/torus_hilbert_boundary.md#the-moving-ideal-generator-test), [quotient comparison inputs](investigations/quotient-hilbert-comparison/index.md#inputs) and [findings](investigations/quotient-hilbert-comparison/index.md#findings), [framework connections](MAP.md#questions-and-active-work) |
| `realization` | [Simultaneous realization](frameworks/formal-normal-geometry/index.md#simultaneous-realization-and-compatibility-problems), [embedded ribbon-to-triple statement](arguments/normal-geometry/formal-normal-intersection.md#the-canonical-embedded-extension) | [Canonical extension proof](arguments/normal-geometry/formal-normal-intersection.md#independent-proof), [one-step boundary and Gorenstein repair](arguments/one_step_boundary_repair.md#one-step-boundary-repair-and-the-final-gorenstein-obstruction), [actual global sources](arguments/equations/global_equation_jets.md#exact-homogeneous-equation-spaces-and-fixed-quadric-restrictions) |

For local equation comparison and specialization use [conormal and actual
quartic symbols](arguments/quartic_specialization_and_symbols.md), the
[filtered equation defect](results/local_filtration_comparison_defect.md),
[normal Koszul cancellation](arguments/normal_koszul_cancellation.md),
[transverse specialization](arguments/transverse_specialization.md), and
[punctual defect and support](arguments/punctual_comparison_defects.md#statements-and-proofs).
