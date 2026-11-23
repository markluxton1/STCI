# Socle budgets, source modules, and arithmetic comparisons

[Formal normal Framework](index.md) · [Original section addresses](normal_filtration_boundaries.md)

## What the socle budget does and does not exclude

For an actual supported complete intersection, [R-0032](../../results/full_conormal_socle_budget.md) records the corrected identity

    n(lambda*d-L)=lambda*(n*d-2*M)+2*Delta,

where n is generic length, d the Loewy index, M the weighted layer-rank sum, L the canonical degree parameter, lambda a valid conormal quotient degree bound, and Delta the corrected degree/torsion defect. The intermediate layers matter: computing only the first normal form and final socle omits terms in M and Delta. The conclusion lambda*d>=L is necessary under the theorem's hypotheses. Equality gives graded self-duality; a constant algebra needs additional balanced-rational assumptions.

The [constant-first-relation obstruction R-0033](../../results/constant_first_relation_lifting.md) requires an actual embedded thickening, a constant first form f, and next initial relation space exactly fV. For a factor direction m of multiplicity nonzero in the field, the quadratic obstruction h_m must vanish. For the fixed characteristic-zero quartic, the inherited nonvanishing of the direction classes excludes the corresponding zero-defect constant-graded-CI equality models. It does not exclude a moving f, an extra next-order relation, or a positive-defect model.


## Interfaces required for a complete comparison

A candidate with explicit generic transverse algebra must be compared at the exceptional points of \(C\) using the full initial ideal, first-relation saturation divisor, local comparison module \(\Delta\), torsion-corrected conormal layers, next extension class and image of global homogeneous sections. Distinguish failures of generic algebra, saturation, punctual comparison, embedded lifting, global source and residual support, including whether failure is invariant under coordinate changes. A single failed pair is not a class-wide obstruction. Characteristic-two split conormal and characteristic-zero balanced extension examples can be compared, but arithmetic specialization does not transfer sole reduced support.

## Ordinary ideal powers and filtered equation modules are different source questions

In degrees \(d\ge3m\), the fixed quartic's ordinary ideal-power theorem identifies the complete ambient source \(H^0(I_C^m(d))\) with \((I_C^m)_d\), and gives \(H^1(I_C^m(d))=0\). This is a statement about ambient sections vanishing to a prescribed order. The comparison defect \(\Delta_n\) instead compares minimal generators of the **full initial ideal of an actual pair** with the filtered equation module \(J/I_CJ\). Neither assertion implies the other.

To pass from an ambient source to a specific normal symbol, the map to \(H^0(\operatorname{Sym}^m N_C^\vee(d))\) must be computed. To pass from compatible symbols to an actual supported complete intersection, one must also impose a common global lift, properness and degree exhaustion. See [the ideal-power proof](../../arguments/normal-geometry/formal-normal-intersection.md#12-ordinary-ideal-powers-on-a-smooth-quadric-complete-proof) and [the global-source treatment](../../arguments/normal-geometry/normal_boundary_weighted_initials.md#normal-boundary-strata-weighted-initials-and-lifting).


## Characteristic-two comparison and arithmetic scope

The fixed quartic pair in R-0021 is flat over the integers. Its characteristic-zero fiber contains four reduced quartics, whereas its characteristic-two fiber has sole reduced support C and generic transverse length four. The conormal extension changes splitting type (R-0020). In the special fiber, R-0031 identifies the cancellation-generated fourth initial equation with the filtered equation-module kernel O(-24); its comparison defect is zero.

R-0012 rules out a constrained flat embedded lift of this prescribed special scheme over Z_(2) or Z_2 with generic reduced support C. It does not contradict the integral family with four generic components or address arbitrary ramified bases. These are separate tests of normal structure, full initial equations, and global support.


## The shared duality mechanism and its limit

The boundary-repair catalecticant and the local-cohomology polynomial left dual are two concrete uses of duality on an actual source map. In the first, Serre duality changes a pole-repair problem into annihilation of a multiplication subspace; in the second, a row annihilating the complete tensor image separates a target class from the image. Both mechanisms work over any coefficient field where the displayed objects and maps are defined. They do not identify their obstruction spaces, and no theorem transfers a repair divisor from one problem to the other. The same global homogeneous source must remain fixed when several conditions are stacked. A separate divisor for each component or independently chosen normal jets would change the existence question.

The [complete endpoint owner](../../arguments/local-cohomology/degree_fifteen_obstruction.md#the-degree-fifteen-boundary-and-exact-duals) now assembles both rational target-u family exclusions with parameter coverage, all affine corrections, exact factor closure and actual tensor reconstruction. Its rational certificate scope is characteristic zero. The [positive-characteristic construction](../../arguments/arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) remains the global control: these duality mechanisms constrain specified sources; they do not exclude STCI in every characteristic.

A cross-topic comparison must first name the objects being compared.
R-0016 assumes a full generic initial CI of degrees \(2\le r<s\),
so the generic transverse algebra has embedding dimension two. R-0019
assumes a generically curvilinear algebra, of embedding dimension one.
These are disjoint hypotheses on the same quotient; asking for a direct
divisor inequality without changing the object has no common input.

A meaningful bridge must specify an operation transporting the actual
equation source between these regimes. On the covered mixed
\((6,4q;2,q)\) edge, the
[first-graph recovery SC6](../../arguments/residuals/first_graph_finite_transfer.md#recovering-generic-curvilinearity-in-all-orders-on-a-subset-of-the-edge)
provides such a change of object; the
[actual finite-modification formulas](../../arguments/normal-geometry/curvilinear_genus_and_defects.md#cartier-cuts-and-finite-modifications-of-the-saturated-filtration)
then compare stated curvilinear presentations where their hypotheses
hold. Neither operation is asserted for arbitrary R-0016 data. A new
comparison should retain the transported global equations, the full
generic algebra, changed conormal data, saturation, attachment and proper
auxiliary cuts, and derive its correction terms there. A vertical
exceptional cycle alone still does not give a residual curve downstairs.



The [attachment-corrected layer and cutting formulas](../../arguments/residuals/layerwise_attachment_and_triples.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component) give an actual comparison with residual support: the signed top class subtracts the marked attachment, and positive complementary-layer failure bounds that attachment below. This is not an identification of R-0016 and R-0019 or arbitrary initial-relation defects. The [actual equation quotient](../../arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers) is the local duality target for the proper pair. The scoped correctness reconstruction of November 23, 2026 is recorded at the linked proof owners.
