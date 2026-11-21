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
every cover. For a smaller carrier smooth at both endpoints, the two
conormal slopes leave at most one candidate for a scalar deficit in
degrees at least six, and at most two in degree five. Singular endpoints
still require their full lattices. An osculating cover instead puts the
full conductor at one general point and tests actual homogeneous kernels
there. [Moving conductor theorem](results/moving_quadratic_conductors.md).
Its exact length cannot give a scalar deficit on any generically regular
smaller carrier, including every integral quintic. The fixed osculating quotient
has a [primitive-triple obstruction and a classification of all pure CM triple extensions](arguments/normal-geometry/osculating_ribbon_obstruction.md):
defect degree two gives a projective line, degree three has a determinant
condition, and every divisor of degree at least four occurs. The algebraic
classification holds in every odd characteristic, but in characteristic three
the fixed quotient is not the unique osculating direction; this does not extend
the characteristic-zero moving-cover theorem. The
[flat graph at the endpoint](arguments/linkage/moving_quadratic_covers.md#the-flat-graph-at-the-endpoint)
retains the entire generic conductor as punctual torsion. These identify
information lost by scalar lengths and pure specialization.
The characteristic-zero fixed-cover
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
from \(m[C_{u,v}]\) in characteristic zero. The
[full quartic-pencil classification](results/quartic_chow_pencil_classification.md)
finds **in characteristic zero** one exceptional non-invariant
orbit over each
\(2[C_{u,v}]+2[C_{u,-v}]\), outside the invariant \((4,4)\) Chow closure.
Every **characteristic-zero** \((4,4)\) realization in this
fiber still satisfies the moment. The exceptional
orbit gives full flat limits with a fixed cycle and an embedded point of
length two at opposite ends. On the exceptional carrier, the
[even-eight identity](arguments/torus/quartic_exceptional_carrier_geometry.md#two-sided-contact-and-the-nodal-even-eight-carrier)
gives genuine two-torsion in the class group of a ten-nodal quartic K3
model, while a
[Hilbert--Burch normal-map degeneracy](arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
describes doubled support. The
[canonical-module and residual-genus proof](arguments/torus/quartic_chow_pencils.md#two-translates-with-coinciding-cubic-jets)
completes **geometric uniqueness for the exceptional
proper quartic pencils**, after a support reduction in
torus coordinates. The \((3,1)\) residual contradicts
the balanced normal bundle, and self-linkage plus
the Hilbert--Burch canonical module forces the
\(\lambda\)-orbit.
The even-eight class remains a complementary
fixed-carrier explanation, not the uniqueness proof. In characteristic two the exceptional formula
[collapses to a non-invariant quartic STCI](arguments/torus/quartic_hilbert_chow_limits.md#hilbert-over-chow-and-the-characteristic-two-collision).
In arbitrary degrees the [one-carrier trace tests](arguments/torus/chow_trace_cone_jets.md)
extend the moment to new presentations and exclude cone jets at disjoint
projection lines for sole support. The
[relative endpoint different](arguments/torus/chow_endpoint_different.md)
detects the number of distinct supports after Chow matching. The
unrestricted obstruction would need a bound on these tests from
higher-degree equations. Separately, a
[fixed-carrier construction criterion](arguments/torus/fixed_surface_restriction_lifts.md#a-two-translate-sextic-construction-criterion)
would convert any proper pair on two exchanged translates with
unequal multiplicities into a sole-support mate. The
[involution--Bézout inequality](arguments/torus/fixed_surface_restriction_lifts.md#involution--bezout-bound-and-the-remaining-sextic-locus)
excludes the previously proposed sextic \((5,4)\) partition
**after generic regularity at both curves**, proved for this
integral symmetric sextic by first-normal geometry; all
remaining unequal two-support sextic partitions are excluded on
nodal carriers. For normal Du Val sextics the
[global exceptional-correction budget](arguments/torus/fixed_surface_restriction_lifts.md#ade-local-classes-and-the-global-sextic-correction-budget)
\(-Z_\pm^2=38/3\) must be reconciled with the local anti-invariant
classes. This is the
[revised scoped investigation](investigations/proof-audit/knowledge-gain-priorities.md#current-choice-and-reassessment),
not a completed higher-degree obstruction.
The [coordinate-to-equation interface](arguments/torus/fixed_surface_restriction_lifts.md)
gives linear coefficient constraints for arbitrary surfaces containing the
chosen translates, then retains joint transverse lengths and normal lifts.
Fixed-surface syzygies recover a first annihilator, not the full embedded
pair. For a sole-support \(C_0\) candidate, a sufficiently low-degree
carrier-power certificate would force a forbidden fixed-carrier mate in
characteristic zero.
For pairs tending to a common smooth quadric, the
[clean boundary theorem](arguments/equations/common_quadric_chow_boundary.md)
computes the full special scheme for all degrees \(a,b\ge3\), under
coprime ambient cofactors and nonzero first cancellation on the quadric,
in every characteristic. For nonzero cofactor restrictions with common
divisor of class \((h_1,h_2)\), the normal source has kernel dimension
\((h_1+2)h_2\) and a known exact image. When \(h_2=0\), the
resultant base ideal is the square of the center ideal and its graph is
the ordinary blowup; these center points are outside the closure of the
fixed-degree sole-support locus, including higher-contact arcs. When
\(h_2>0\), that square-ideal model fails and the graph and deeper
cancellation remain unresolved, as do zero restrictions, common ambient
cofactors and other global strata. The balanced quadric subcycle excludes
constant sole support throughout the special-scheme theorem's scope; for
the fixed monomial quartic it also excludes the exact Chow-polytope fibre.
Closure of varying translate arrangements remains a separate question.
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
