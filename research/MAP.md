# Mathematical approaches and their interfaces

## Central problem and research selection

For the fixed rational quartic \(C_0\subset\mathbf P^3\) in characteristic zero, the unrestricted question concerns **actual homogeneous pairs** \(F\in I_{C_0}(a)\), \(G\in I_{C_0}(b)\) forming a proper intersection. Its effective cycle is \([V(F,G)]=m_{C_0}[C_0]+R\), where \(ab=4m_{C_0}+\deg R\). Thus maximal generic multiplicity \(m_{C_0}=ab/4\) is equivalent to sole support. This is classical degree exhaustion and a reformulation of STCI, **not** a new obstruction or a reason to assume a degree-independent bound exists.

The principal investigative interfaces are **actual global realization and formal normal geometry**, **full-ideal torus degeneration with its coverage problem**, and **residual construction or absorption**. Each must ultimately constrain or construct actual proper equation pairs. Local cohomology, fixed-carrier normalization, spectral roots, and prescribed arithmetic lifts remain mathematically valid methods and sources of tests, but bounded results in these settings do not acquire unrestricted coverage without a separate bridge. No approach currently proves a degree-independent obstruction.

Before prioritizing new work, state the exact class of equation pairs covered, the theorem or decision obtainable, its implication for unrestricted STCI, and the strongest existing result that leaves the gap open. A bounded question may remain open without being an active priority.

The common zeros of the two leading forms give a residual test in all
possible defining degrees. If a sole-support pair has zero degree
in the normal-direction factor, its strict intersection is supported
on one section. The normal bundle of that section forces deeper contact in
characteristic zero. On the edge \((3p,4q)\) two marked rational
quintics on \(V_5\) give an equivalent equation problem with an explicit
test for the contracted trisecant. [Connected directions](results/connected_normal_directions.md#statement) ·
[Actual equation correspondence](arguments/residuals/blowup_residual_geometry.md#actual-equations-on-the-zero-direction-edge).

Use the [active front door](investigations/proof-audit/open-items.md) for the current research organization. The KG queue owns strategic ranking; this map and its linked frameworks own the mathematical approaches. The cross-framework audit is a comparison aid, not another queue.

Choose an approach by the object it studies and the map it would need to
construct. Use the [index](INDEX.md) for exact proof routes and
`python3 scripts/research.py frameworks` for entry and bridge addresses and
links to connected work. Each Framework owns the mathematical discussion and
open implications relevant to its approach.

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

For every characteristic-zero bidegree, the smaller defining equation and
its weight components bound the splitting of the moving transverse quotient.
At a general point, a single base tangent vector induces a map from the fiber
kernel to the fiber algebra whose rank also has a lower bound. The unresolved
global question is which such families arise as the entire torus modification
of a saturated homogeneous ideal with two generators of the prescribed
degrees. Splitting, generic ranks, the CI Hilbert polynomial, and both endpoint
image algebras give tests for a candidate. The remaining compatibility concerns
relations among its actual homogeneous equations throughout the family.
[Movement bounds](results/torus_quotient_movement_bounds.md) ·
[Moving quotient and equation comparison](investigations/quotient-hilbert-comparison/index.md#completion-and-next-decisions).

For primitive-triple sextic pencils, the current interfaces are (i) higher contact
through the surviving ADE primitive triples with independent restrictions
to the containing quadric, and (ii) comparison of the established canonical
cohomological obstruction and unique-quadric filtration for the eleven
missing sextic symbols with the order-five Čech target filtration.
For pencils with a first-order member and dependent quadric restrictions,
the sharp generic length is five in all three orbits, so the residual
degree is at least sixteen. See
[the ADE contact bound](arguments/carriers/sextic_ade_reduction.md#sharp-length-five-for-pencils-with-a-quadric-divisible-member),
[global symbol cohomology](arguments/equations/global_equation_jets.md#verified-characters-and-the-quadric-flag-cohomology),
and [formal normal questions](frameworks/formal-normal-geometry/filtered_equation_module_and_sextic_obstruction.md#two-precise-sextic-questions).
Existing torus-boundary investigations continue to require a single
realizable moving ideal with both full limits.
For the three fixed characteristic-zero primitive triples, the
[intrinsic source and determinant proof](arguments/carriers/sextic_triple_intrinsic_contact.md)
replaces the degree-four through degree-six source ranks, restricted-contact
ranks and determinant ranks by quadric interpolation and a rank-two bundle
on the curve.
It gives the source dimension in every degree at least four and a full
determinant image for \(a,b\ge5\) with \(a+b\ge11\), including
the mixed quintic-sextic case. The equal-quintic case retains a specific
six-jet interpolation gap in the geometric proof.
The remaining issue in this framework is higher contact of actual proper pencils;
surjectivity of the determinant span does not settle that incidence.
For an actual orbit pair in any bidegree, the two endpoints together
detect raw equation torsion but can miss classes on a parameter layer.
On the first layer the multiplicity of the disjoint coordinate line in
the intersection of the stripped extreme forms bounds the moving residual
degree from below after subtracting the generic length missed there.
A residual sextic pencil exhibits the loss even when the full limit
omits the line. [Endpoint and residual degree theorem](results/endpoint_equation_torsion.md).

## Questions and active work

The [same-radical equation lemma and higher-rank torus control](arguments/torus/equivariant_set_theoretic_descent.md)
separate unbounded set-theoretic equations from generators of a moving ideal.
The [general pair-rank and weight formulas](arguments/torus/equation_pair_rank_and_weights.md)
retain degree and source information across that distinction. The
[finite-group-scheme orbit model](arguments/arithmetic/frobenius_power_lifting_precision.md#torus-eigenforms-and-the-finite-group-scheme-orbit)
explains the splitting and coalescence of one explicit arithmetic family.
These connections sharpen the boundary and realization questions; none
establishes a moving supported pair in characteristic zero or decides
unrestricted STCI.

Fixed-carrier normalization has established exclusions for particular
quintic models and necessary inverse-support conditions for a marked
elliptic octic family. These are bounded results, not a classification
of all possible carriers or a degree-independent obstruction. See the
[carrier framework](frameworks/carrier-normalization/index.md),
[toric quintic exclusion](results/toric_quintic_carrier_exclusion.md),
and [elliptic inverse-support criterion](results/elliptic_inverse_support.md).

The quadratic conductor now compares global postulation with both actual
endpoint capacities on the same object, excluding specified carrier families
in all mate degrees. [Choosing the auxiliary cover](arguments/linkage/quadratic_cover_choice.md)
makes the nonsplit onset available for every integral carrier of degree
greater than two in characteristic different from two. In characteristic
zero the uniform all-minors bound applies, but even one
[smooth-transverse endpoint](arguments/linkage/endpoint_lattice_capacity.md#transverse-endpoints-throughout-the-cover-pencil)
already has capacity exceeding the displayed scalar postulation bound for
every cover. That comparison's remaining target has aligned smooth or
singular behavior at both endpoints. The characteristic-zero fixed-cover
two-lift sextic sector is excluded without normality. Its surviving
one-lift sector is generically regular along the lift, has non-Du-Val
behavior there, and satisfies the symbolic defect strata \(g=5,6,8\)
without a normality assumption. The unique singular-cubic exclusion
also holds in odd characteristic; the Du Val/K3 exclusions do not extend
by this argument. These statements
do not close the separate split-first-normal-cone frontier or improve the
general degree bound. See the [current carrier scope](frameworks/carrier-normalization/index.md#quadratic-cover-exclusions-and-the-remaining-one-lift-sector)
and [local/global interface](frameworks/global-equation-realization/projection_and_liaison.md#embedded-conductor-and-ambient-equations).

Actual [pairs retaining the toric quartic as a defining equation](arguments/torus/fixed_carrier_chow_arrangements.md)
have an exact coefficient description: the carrier's semigroup
gaps force \(c_1=c_2=c_5=0\). In characteristic zero at least three distinct
translates remain, while partial collisions occur; the root-of-unity examples
form a special locus. This does not classify arbitrary CI thickenings whose
support merely lies on that surface. The smooth quadric admits no such section,
by its ruling
classes. More generally, the [Chow trace moment](arguments/torus/chow_arrangement_moments.md)
vanishes for pairs with an eigenform generator or specified polynomial
congruences, including every invariant CI and reduced CI arrangement.
Its linear Chow-coefficient equation separates their entire Chow closure
from \(m[C_{u,v}]\) in characteristic zero. Non-invariant CI lifts over
repeated cycles need not lie in that closure. Their realization geometry is
the [current exploratory priority](investigations/proof-audit/knowledge-gain-priorities.md#current-choice-and-reassessment).
Separately, [simultaneous torus degeneration of the quadratic graph](arguments/linkage/toric_limit_conductor_comparison.md)
compares original and pure-limit conductor lengths using the difference of
the two embedded endpoint corrections. Their control by global equations is
the missing comparison; endpoint concentration alone supplies no inequality.

Two bounded objects in [Investigations](investigations/) currently connect the
torus approaches, at different stages of readiness: [moving quotient and full Hilbert comparison](investigations/quotient-hilbert-comparison/index.md)
is active, and [generator incidence](investigations/supported-generator-incidence/index.md)
describes a **planned, unperformed** test requiring an actual declared supported family. Its existing generator criterion is not evidence that such a family has been constructed. The Frameworks
explain how either outcome would change the approach.

Other usable starting points include
[normal-geometry questions](frameworks/formal-normal-geometry/open_normal_geometry.md),
[carrier and conductor cases](frameworks/carrier-normalization/open_carrier_cases.md),
[actual lifts of spectral roots](frameworks/spectral-roots/open_root_lifts.md),
[projected ACM constructions](frameworks/global-equation-realization/projection_and_liaison.md),
[octic multiplier kernels](frameworks/residual-construction/octic_multiplier_kernels.md), and
[the quartic two-target problem](frameworks/local-cohomology/open_quartic_ancestors.md).
These are mathematical entry points. Use the [bounded work guide](MODEL.md#choosing-bounded-work)
to decide whether a particular question is ready for an Investigation.

A [geometric synthesis of quadric restriction and contact rigidity](frameworks/residual-construction/quadric_restriction_and_contact_rigidity.md) separates the degree-independent Picard-class support obstruction from the computational sharp sextic contact bound. It records the symbolic-power vanishing equivalent to the rank test, the residual quartic cycles, and a bounded uniform proof-replacement question; it does not assert a new exclusion.
