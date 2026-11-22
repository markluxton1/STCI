# Thickening hierarchy, jet budgets, and socle movement

[Formal normal Framework](index.md) · [Original section addresses](from_symbols_to_equations.md)

## 3.9 A practical hierarchy for thickening investigations

For an actual pair \(J=(F,G)\subset I_C\), distinguish the generic length of \(\mathcal O_{\mathbf P^3}/J\) along \(C\), the graded conormal layers of its supported Cohen–Macaulay structure, the full \(I_C\)-initial ideal, and the images of **global** degree-bounded homogeneous sections. These four objects can have different generators and different exceptional-point behavior. The cancellation example in §3.1 already shows why the first two displayed symbols need not generate the initial ideal.

The balanced characteristic-zero normal bundle of the fixed quartic and its characteristic-two jump are recorded precisely in [R-0020](../../results/quartic_conormal_characteristic_jump.md). This is a useful test of globalization: a locally chosen normal direction over \(k(C)\) need not extend as a line summand on \(C\). Do not infer that the characteristic-two split model lifts to characteristic zero.

For **saturated, full generic binary complete-intersection** initial data, [R-0010](../../results/saturated_first_relation_normal_flatness.md) supplies a conditional normal-flatness result; [R-0013](../../results/saturated_actual_generator_movement.md) and [R-0014](../../results/movement_two_six_rows.md) further restrict actual generators and movement-two numerical possibilities under their own hypotheses. The six rows are necessary cases within that class, not a classification of arbitrary supported intersections. [R-0015](../../results/fixed_small_movement_finiteness.md) is a fixed-range arithmetic reduction, not a completed all-degree obstruction. Reduced singular roots with a regular lifted formal surface are treated separately in [R-0018](../../results/regular_singular_root_formal_obstruction.md); dropping regularity or saturation is not justified.

When saturation fails, [R-0016](../../results/nonsaturated_first_relation_resultant.md) measures a conditional resultant/defect budget, while [R-0030](../../results/local_filtration_comparison_defect.md) identifies a *different* comparison between the filtered actual equation module and its initial generators. The latter leaves open whether a generically vanishing defect can be punctual under sole reduced support. Neither defect is automatically the jet-map rank shortfall from the historical order-one calculations. [R-0032](../../results/full_conormal_socle_budget.md) imposes a separate socle budget on supported complete intersections; [R-0033](../../results/constant_first_relation_lifting.md) obstructs a specified constant-relation lifting model, not every moving relation.

### Cartier cuts and actual finite modifications retain the defects

The [saturated filtration identities CF1--CF4](../../arguments/normal-geometry/curvilinear_genus_and_defects.md#cartier-cuts-and-finite-modifications-of-the-saturated-filtration) identify the punctual torsion of a Cartier cut of a generically curvilinear thickening with the sum of explicit saturated multiplication divisors. For a generic order-one cut, it is \((c-1)\Theta+D_{\rm top}\). A finite birational modification with unchanged generic algebra has length divisor satisfying \(2B_f/c=(c-1)\Xi+D_{+,\rm top}-D_{-,\rm top}\) in the Gorenstein case. Here \(\Xi\) records the first free normal-layer map, not a symbolic root, and the finite map and actual filtration are required. In the [first-graph application](../../arguments/residuals/blowup_residual_geometry.md#socle-defects-on-the-two-presentations-of-the-first-graph) the first formula is exactly the divided exceptional resultant, while the second computes the marked-point defect created by the other contraction to \(V_5\). These are new pointwise bridges to actual equations and birational geometry, pending independent review; no analogous claim about arbitrary changes of the generic transverse algebra is made.

### Structural lessons from unsuccessful shortcuts

- **First symbols are insufficient.** Higher initial generators may arise through cancellation; the prescribed characteristic-two example has an essential fourth equation [R-0031](../../results/quartic_char2_fourth_equation_kernel.md).
- **A graded model is not an embedded thickening.** The full-root Picard criterion [R-0008](../../results/spectral_root_picard_criterion.md) must be combined with ambient compatibility, not treated as a global construction.
- **Numerical budgets do not realize equations.** Conormal degrees, socle identities, and finite jet ranks constrain candidates but do not establish that a pair of homogeneous forms realizes them.
- **Special-point defects are not residual curves by definition.** Residual support requires a separate actual intersection argument; see [R-0019](../../results/quasiprimitive_residual_cycles.md).

### Concrete remaining tests

1. For a candidate actual pair with \(\sqrt J=I_C\), compute the full local initial ideal and the R-0030 comparison at every exceptional point. See the [punctual relative-defect question](open_normal_geometry.md#punctual-relative-defect-under-sole-support).
2. In a surviving saturated-root family, check full fiberwise coprimality, the actual generator hypotheses, and successive embedded lifting separately; calculate the remaining zero locus rather than extrapolating from one obstructed seed.
3. For a fixed lower thickening, compute the extension class and permitted repair divisor described in [the one-step note](../../arguments/torus/toric_torsion_and_endpoint_contacts.md#boundary-one-step-obstruction-and-endpoint-geometry), then impose the actual global degree-\(d\) source image. A vanishing extension class alone does not supply two defining equations.

These tests are complementary rather than a mandated sequence. For detailed boundary-repair and punctual-defect discussion, continue to [the filtration supplement](normal_filtration_boundaries.md).


### Jet-condition budgets: a precise historical model

In the order-one quartic calculations, the successive restriction map from degree-a ambient sections through a primitive layer to the next conormal layer has two different shortfalls: failure to hit the full target and failure to attain the maximal rank allowed by source and target dimensions. A quasiprimitive defect divisor modifies the target line bundle; it is not the same as either rank shortfall. The [order-one result](../../results/order_one.md) now records the definitions and the concrete quadric-comparison example using R and 2R. This is a model for higher-degree global-source problems, not a universal implication from expected jet counts to residual support. Historical quartic-mate open cases are superseded by R-0001.

### Movement and socle: exact scope

In R-0013 the saturated first-relation line has degree -7r-epsilon. Its coefficient map to P^r has degree epsilon. Saturation prevents coefficient base points, not root collisions or failure of fiberwise coprimality. Under the actual supported-CI and full generic binary-CI assumptions, the necessary equations are ab=4rs, 4(a+b)=7(r+s)-epsilon(s-r)/r, and r divides epsilon*s. Movement epsilon=1 is excluded. R-0014 restricts epsilon=2 to six necessary tuples (r,s;a,b): (2,8;8,8), (2,12;6,16), (6,21;18,28), (14,42;48,49), (15,45;50,54), (20,60;64,75). These are not constructions, and they do not cover nonsaturated relations.

The socle identity in R-0032 is n(lambda*d-L)=lambda*(n*d-2*M)+2*Delta, with n the generic length, d the Loewy index, M the weighted sum of layer ranks, L the canonical degree parameter, lambda a valid conormal degree bound, and Delta the corrected layer defect. Equality gives graded self-duality; a constant algebra requires additional balanced-rational hypotheses. R-0033 then excludes only specified constant-first-relation equality models, assuming the next relation space is exactly fV. Moving relations, extra relations and positive-defect models remain outside its scope.


