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

### From candidate lattices to actual algebras and proper cuts

The [marked border-product theorem](arguments/residuals/blowup_residual_geometry.md#finite-index-rigidity-of-higher-marked-jets)
exposes another exact failure mode of
determinant-only equation tests:
a full-rank lattice of the correct
finite index need not be closed under
multiplication. On the primitive
marked \((3p,4q)\) edge the
first base jet is forced to be
linear modulo the \(q\)-th normal
power. The [R0019 extension](arguments/normal-geometry/actual_equation_filtration.md#residual-corrected-r0019-and-the-actual-equation-source)
shows how the saturated normal-cut
formula changes with real residual
curves, subtracting the marked
attachment. The [actual \((4,6)\) triple](arguments/torus/fixed_carrier_chow_arrangements.md#an-actual-non-lci-curvilinear-triple-the-conormal-torsion-is-visible)
checks the complete interface,
including torsion of the primary
conormal module. These do not
identify the torus-endpoint Sylvester
index with the marked finite-image
index, or automatically convert
a formal defect into \(Q_1\ne0\).

### A shared attachment and finite-transfer interface

The [layerwise attachment duality](arguments/residuals/residual_capacity_and_constructions.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component) relates saturated normal defects of an actual curvilinear full primary to its genuine residual attachment. The [annihilator-layer comparison](arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers) identifies the actual attachment equation quotient, with its adjunction twist, as the local Matlis dual of a layer of the pairwise local-cohomology defect. These give a common obstruction target rather than a universal nonvanishing theorem. The [signed finite-transfer identity](arguments/residuals/blowup_residual_geometry.md#signed-finite-transfer-throughout-the-interior-equality-boundary) extends the graph calculation across the interior equality boundary, allowing an image residual conic; its [canonical ideal version](arguments/residuals/blowup_residual_geometry.md#local-canonical-ideal-version-and-several-marked-points) retains the actual ideal. The [classified toric primary calculation](arguments/torus/fixed_carrier_chow_arrangements.md#all-order-primary-structure-and-attachment-on-the-classified-carrier) shows that full attachment length can rise while residual degree falls. Rank-one layer formulas require generic curvilinearity; the attachment-module comparison does not. Independent review pending.

**Exact triple collapse beyond the sextic program.** The [BF triple and actual-pair attachment TR1--TR4](arguments/residuals/residual_capacity_and_constructions.md#triples-the-full-attachment-has-only-two-independent-divisors) uses the already classified Bănică--Forster local quasiprimitive triple (not a new local classification) to identify \(D_2\) with torsion of the full-primary conormal equation module in every characteristic. On an actual proper CI whose generic marked primary length is three, its three residual-attachment layers collapse to \((\tau+\eta,\eta,\tau+\eta)\), where \(\tau=D_2\) and \(\eta\) is the actual two-equation determinant divisor. Thus full thick attachment is \(2\tau+3\eta\), and the signed socle line is \(\mathcal L^2(-\eta)=\omega_C\omega_Y^{-1}|_C\). This is the strongest clean reconciliation of the normal, residual and local-cohomology approaches in a nontrivial multiplicity. It makes no universal positivity claim and relies on the previously review-pending LA1 for its global attachment conclusion.

### What the degree-four-to-six synthesis actually changes

The [carrier exclusion synthesis](frameworks/carrier-normalization/degree_exclusions.md) distinguishes universal mechanisms, actual-pair reductions, all-mate exclusions for particular carriers, and remaining realizations. The all-mate quartic theorem remains an independent base case, not a consequence of index tests which use it.

**An all-degree division of actual pairs.** The [normal-replacement theorem](arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier) applies to every \(a\le b\): a general degree-\(b\) generator of the same CI ideal is normal integral exactly when some original generator has generic order one. This is the intrinsic embedding-dimension-one branch. Equal-degree pencils need no degree cutoff, and two independent general members are normal there. No member of this generator system can be normal if both symbols vanish generically. The quadric and graph bounds place all hypothetical \((5,b)\) and \((6,6)\) pairs in the first branch; \((6,8)\) is the first numerical pair where an entirely-thick pattern survives those bounds. For arbitrary presentations in either branch, [Ellia's primitive classification](literature/README.md#ellia), together with the quartic theorem, forces a common singular point outside nine surviving primitive-eligible degree pairs; inside those nine the assertion remains unresolved.

**Exact Picard saturation, including arrangement cycles.** The [almost-Cartier Hodge test](arguments/carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) applies to any integral carrier regular at the generic points of the prescribed curves, not just normal carriers. The kernel of the normalized Hodge matrix gives numerical multiplicity directions; actual local almost-Cartier relations downstairs give the integral lattice. In the singleton case, finiteness of the downstairs index \(R_X\) and normalized Hodge equality are necessary and sufficient. The minimal multiplicity is \(R_X\), and the minimal mate degree is \(eR_X/a\). Hartshorne–Polini already provide hyperplane saturation in characteristic zero; flat Lefschetz gives arbitrary characteristic. The [normalization and conductor factorization](arguments/carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) distinguishes this index from the index upstairs. The [almost-Cartier power–socle theorem](arguments/carriers/normal_carrier_symbolic_torsion.md#normality-is-unnecessary-the-actual-almost-cartier-power-theorem) extends the actual local defect formula and the all-mate exclusion of indices at most four to possibly nonnormal generically regular carriers in characteristic zero. Independent review of these extensions is pending.

**Separate fixed defects from moving singularities.** For a generically curvilinear CI, the [actual first-symbol system](arguments/carriers/normal_carrier_divisor_geometry.md#the-global-moving-root-theorem-the-larger-normal-carrier-has-index-m) has fixed common-symbol divisor \(B_{\rm np}\) and a reduced moving divisor on \(C\). Any nonempty moving divisor forces the index lcm \(R=m=ab/4\) and minimal mate degree \(a\), automatically for \(a<b\) with smaller symbol nonzero, and for equal degrees with linearly independent first symbols. Large indices here are consequences of generator movement, not extra impossibilities. The actual top-socle divisor has exactly the support of \(B_{\rm np}\), even when the moving divisor is empty. This localization does not identify the multiplicities or local algebra. [Uniform reduced-gcd test](arguments/carriers/normal_carrier_divisor_geometry.md#reduced-common-first-normal-divisor-a-uniform-marked-ade-and-rank-test): reduced \(B_{\rm np}\) forces end-marked ADE germs, with fixed indices proper divisors of \(m\) and saturated layers \(\lfloor i/r_P\rfloor\). The exact duality and root-rank budgets give a common mechanism for the [proved nonreduced-gcd sextic theorem](arguments/carriers/sextic_pair_reduction.md#the-common-first-normal-divisor-must-be-nonreduced); they also rule out reduced gcd in the entire multiplicity class with prime factors \(1\bmod4\) (e.g. \(m=25\)). The new all-degree extensions require independent audit.

**Distinguish proof thresholds from geometry.** Every-member integrality follows from factor degrees and Bézout in equal degrees \(6,8,10\), but its numerical threshold at degree 12 does not affect general-member normality. At minimal degree product every compatible generator is integral, without a degree bound. Factor descent changes the thick scheme and is not a substitute for ideal-preserving replacement. The resulting normal octic and degree-ten index necessities \(R=16,25\) do not settle the respective pairs.

**The entire-thick branch now has a common carrier/graph obstruction.** The [branch valuation dictionary](arguments/carriers/numerical_surface_pullback.md#branch-valuations-and-the-actual-first-blowup) identifies the actual first strict-intersection coefficients as pushforwards of `n_i-qe_i`, not raw carrier valuations or full-ideal Rees valuations. Principalization gives the exact gap `16p²/a+4a-14p=-e^tQe-V²`, splitting the ambient marked-ideal deficit into the normalized branch Hodge imbalance and exceptional energy. Every exceptional connected component carrying nonzero principalization defect requires a branch with positive actual excess meeting it; the N3 inequalities retain the individual special-point coefficients. A no-vertical singleton inverse or a single horizontal root cannot admit a mate in any degree. Two inverse branches without vertical fibers have a necessary numerical matrix determined by their slopes, degrees and valuations. On the degree-three-per-order boundary, [Cartier ruling clusters](arguments/carriers/numerical_surface_pullback.md#cartier-test-divisors-and-the-degree-three-per-order-boundary) give the all-order root divisibility test and quantitative low-branch Cartier index: for two degree-one branches the low slope is 0 or 1 and its square is respectively `9/(2p)` or `26/(5p)`, never integral. These recover and extend the split-sextic restrictions without requiring an ADE classification. Further branch counts, vertical content, actual conductor descent and higher contact remain genuine gaps. The new deductions await independent review.

The [ample strict-carrier compression](arguments/residuals/blowup_residual_geometry.md#lefschetz-compression-on-ample-strict-carriers) transfers the actual-index method to a smooth sole-support strict intersection on the first blowup. If its multiplicity is \(c\) and the ample strict carrier is generically regular along it, then its index lcm \(R\) satisfies \(c/R\mid\gcd(a,p)\). Under the stated section-lifting inequalities, a nontrivial quotient gives a lower-degree ambient mate. On the \((3p,4q)\) edge with \(p\le q\) those inequalities hold. In particular the entirely-thick \((6,8;2,2)\) case has a generically curvilinear first strict intersection, a normal general strict octic and an actual index-eight point (LC4). This uses R-0077 and the characteristic-zero low-degree exclusion; it neither proves normality of the original octic nor excludes the pair. Review pending.

**Pointwise compatibility on both graph models.** The [pointwise graph resultant and finite modification formulas](arguments/residuals/blowup_residual_geometry.md#socle-defects-on-the-two-presentations-of-the-first-graph) identify the divided exceptional resultant with \((c-1)\Theta+D_{\rm top}\) for a generically curvilinear sole-support strict CI, where \(\Theta\) is tangency of its normal line to the exceptional surface. This is the specialization of [CF1--CF4](arguments/normal-geometry/curvilinear_genus_and_defects.md#cartier-cuts-and-finite-modifications-of-the-saturated-filtration), valid for actual Cartier cuts and finite modifications of curvilinear thickenings in arbitrary smooth ambient threefolds. On the \((3p,4q)\) edge, the finite map to the image quintic CI in \(V_5\) has length defect \(pq(q-1)\) at the marked point, with pointwise top-defect change \((c-1)\xi-(q-1)\), \(\xi=0,1\) from the actual conormal modification. The [marked-line obstruction ML9](arguments/residuals/blowup_residual_geometry.md#all-orders-the-marked-line-comparison-by-interpolation) eliminates primitivity at the prescribed marked point for every mixed \((3p,4q)\) edge pair with \(2\le p\le q\), without ADE or normality assumptions. Thus the globally primitive mixed \((6,8)\) row is excluded, not merely conditionally: only the mixed slope-four and endpoint slope-five rows remain there, with positive marked defect in the mixed row. Of the five necessary global primitive order pairs on the full edge, mixed directions survive this test only at \((10,4),(21,3)\); endpoint directions remain subject to their separate splitting and line contact. The [full marked finite-modification lattice](arguments/residuals/blowup_residual_geometry.md#full-marked-finite-modification-lattice-in-the-primitive-at-the-point-stratum) identifies the completed image ideal for \(q=2\) in the primitive graph stratum as \((y^2-x^2t,t^{2p})\), with multiplication defects \(D_j=2\lfloor j/2\rfloor\); for a generically regular image carrier the local index is two (marked \(D_{2p+1}\)) or \(4p\) (multiplicity at least three). The opposite [smooth marked image-carrier lane](arguments/residuals/blowup_residual_geometry.md#the-opposite-marked-stratum-a-smooth-image-carrier-and-a-forced-graph-defect) gives strict equations \(xv=t^{2p},v^q=0\), defects \(D_j=\lfloor j/(2p)\rfloor\) and marked index \(2p\) on the strict carrier. A degree-two image mate there would descend to an original degree-four mate by exact conic trace cancellation, so is excluded. For \(q=2\) and an integral smaller image carrier its minimal image mate degree is therefore four; for \(p=2\) an actual index-eight point away from the smooth marked point is forced. These deductions await independent review.

The [edge recovery theorem SC6](arguments/residuals/blowup_residual_geometry.md#recovering-generic-curvilinearity-in-all-orders-on-a-subset-of-the-edge) shows that on the mixed \((6,4q;2,q)\) edge the strict sextic always has order one, and for \(q\ge2\) a general strict carrier of the other equation is normal with at least \(9q-10\) distinct moving index-\(4q\) points. The first strict CI must be nonprimitive somewhere for \(q>2\). Across the full \((3p,4q)\) edge, global primitivity on the graph has only the five necessary order pairs \((2,2),(5,19),(6,8),(10,4),(21,3)\), by the [primitive edge arithmetic](arguments/residuals/blowup_residual_geometry.md#primitive-graph-structures-on-the-full-degree-threefour-slope-edge). This is not the classical primitive list on \(C_0\); it applies to the first strict intersection. The [normal K3 torsion theorem](arguments/carriers/normal_carrier_symbolic_torsion.md#a-uniform-torsion-bound-on-normal-k3-carriers) also gives an all-mate-degree bound \(R\le16\) on globally ADE degree-two image carriers in \(V_5\), with a mate there in degree at most eight; conic vanishing for an actual lift to the original problem is separate. The results are pending review.

**Research implication.** For a fixed generically regular carrier, finite downstairs almost-Cartier index plus normalized Hodge equality already gives an actual ambient mate. Conductor computations furnish the first gate, rather than a separate unresolved lifting problem after both gates. In characteristic zero the same local socle budget applies regardless of normality. The entirely-thick branch still requires full-ideal/Rees, residual, and actual equation analysis; the normal replacement theorem does not cover it. The [local attachment test](arguments/residuals/residual_capacity_and_constructions.md#local-index-forces-residual-attachment) also forces residual support through every point where the generic multiplicity fails the local index divisibility test. These mechanisms do not establish unrestricted STCI nonexistence.

A second
[cross-framework consequence](arguments/torus/fixed_surface_restriction_lifts.md#reverse-application-single-curve-exclusions-constrain-multi-curve-chow-cycles)
goes *from* all-mate
single-curve exclusions
*to* Chow realization:
on an integral quartic
carrier, actual supported
mate multiplicity vectors
for two translates have
rank at most one; on
a prime cyclic orbit
they must all be equal.
This is a constraint
on the **actual
equation-to-cycle map**,
not an existence
claim about those
carriers or arrangements.

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
orbit has a [normalized \(\mathbf P^1\) Hilbert
compactification](arguments/torus/quartic_hilbert_chow_limits.md#two-compactifications-of-the-exceptional-orbit)
with two distinct embedded endpoint limits. Its **Grassmannian**
orbit closure in the Plücker embedding is explicitly a smooth
twisted cubic; its two boundary points are instead improper pencils
with a common cubic factor. By
[Chen--Nollet detachment](arguments/torus/quartic_hilbert_chow_limits.md#detaching-the-embedded-endpoint),
each saturated endpoint also lies in the closure of the
six-dimensional family obtained by adjoining two isolated points
to the pure doubled curve. Thus the proper-CI orbit is only a
one-dimensional slice of a substantially larger fixed-one-cycle
Hilbert locus. On the exceptional carrier, the
[even-eight identity](arguments/torus/quartic_exceptional_carrier_geometry.md#two-sided-contact-and-the-nodal-even-eight-carrier)
gives genuine two-torsion in the class group of a ten-nodal
quartic K3 model. Its [Nikulin double cover](arguments/torus/quartic_exceptional_carrier_geometry.md#the-nikulin-double-cover-and-a-square-root-of-the-mate)
makes the actual quartic mate a square, and its
[class-group parity](arguments/torus/quartic_exceptional_carrier_geometry.md#parity-of-mates-from-the-even-eight-class)
forces even equal mate multiplicity on the normal nodal
carriers. Meanwhile a
[Hilbert--Burch normal-map degeneracy](arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
describes doubled support. The
[canonical-module and residual-genus proof](arguments/torus/quartic_chow_pencils.md#proof-route)
completes **geometric uniqueness for the exceptional
proper quartic pencils**, after a support reduction in
torus coordinates. The \((3,1)\) residual contradicts
the balanced normal bundle. The
[direct \((3,3)\) linkage](arguments/torus/quartic_chow_pencils.md#the-residual-line-and-the-canonical-module)
to the residual line **produces** the canonical module;
self-linkage and restriction to the same line then force
the \(\lambda\)-orbit. The first-normal doubled-support
condition is Plücker-linear in \(\operatorname{Gr}(2,9)\).
The even-eight class remains a complementary
fixed-carrier explanation, not the uniqueness proof. In characteristic two the exceptional formula
[collapses to a non-invariant quartic STCI](arguments/torus/quartic_hilbert_chow_limits.md#hilbert-over-chow-and-the-characteristic-two-collision).
In arbitrary degrees the [one-carrier trace tests](arguments/torus/chow_trace_cone_jets.md)
extend the moment to new presentations and exclude cone jets at disjoint
projection lines for sole support. The
[relative endpoint different](arguments/torus/chow_endpoint_different.md)
detects the number of distinct supports after Chow matching. For the
specific monomial endpoint family
(y=u_i x^{d-1}, w=v_i x^d), the same trace/different argument plus
weighted interpolation gives a degree-(d) finite detector already at
depth (N=m+1); this is **not** asserted for arbitrary tame covers.
The unrestricted obstruction would still need a bound on these tests
from higher-degree global equations. Separately, a
[fixed-carrier construction criterion](arguments/torus/fixed_surface_restriction_lifts.md#a-two-translate-sextic-construction-criterion)
would convert any proper pair on two exchanged translates with
unequal multiplicities into a sole-support mate. The primitive
orbit-lattice formula gives mate degree
\(b(m-n)/\gcd(m,n)\); in particular a hypothetical sextic
partition \((6,3)\) would already produce a degree-six
sole-support mate and hence an actual \((6,6)\) STCI. The
[involution--Bézout inequality](arguments/torus/fixed_surface_restriction_lifts.md#involution--bezout-bound-and-the-remaining-sextic-locus)
excludes the previously proposed sextic \((5,4)\) partition
**after generic regularity at both curves**, proved for this
integral symmetric sextic by first-normal geometry; the [local lattice/contact and mixed intersection theorem](arguments/torus/fixed_surface_restriction_lifts.md#the-sextic-symmetric-arrangement-must-escape-ade-at-an-endpoint) now excludes every remaining unequal partition if both common endpoints are smooth or Du Val. Away from these endpoints the actual indices divide the gcd of the two multiplicities, not merely their difference. In particular the coprime partitions force smoothness along both curves away from the endpoints. The (6,3) partition forces incompatible mixed exceptional intersection at two index-nine ADE endpoints. The stronger exclusion does not assume normality away from the endpoints, using the new almost-Cartier extension there. Independent audit is required; the remaining construction locus needs at least one genuinely non-Du-Val endpoint. This narrows the [scoped investigation](investigations/proof-audit/knowledge-gain-priorities.md#current-choice-and-reassessment), not the entire higher-degree realization problem.
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


### Transverse Chow roots, source resultants, and what \(Q_1\) really is

The [homogeneous transverse Chow/norm theorem](arguments/torus/chow_arrangement_moments.md#the-homogeneous-transverse-chow-form-as-a-section-norm)
makes the transverse-root viewpoint exact. For
\(Z=\sum n_i[W_i:U_i:V_i]\), the homogeneous transverse Chow form
\({\cal C}_Z=\prod(W_iX+U_iY+V_iZ_0)^{n_i}\) records the unordered
translate parameters. The explicit bihomogeneous quartic kernel
\(\Psi_{W,U,V}(\alpha,\beta,\gamma)\) sends each root to the Chow form of
its intersection with the symmetric plane \(x_3=x_0\). Their product
\({\cal N}_Z\) is simultaneously the norm/characteristic polynomial of the
finite section algebra and the projective resultant of the **actual**
restricted equations. On the translated-quartic fiber this fixed-plane
section is set-theoretically injective, so no arrangement-cycle information
is lost. The older binary \(H_Z={\cal C}_Z(0,-B,A)\) records the ratios
\(U_i/V_i\); its first Newton trace is exactly the existing Chow moment
\(\sum n_iU_i/V_i\).

This gives the precise content of the Galois-polynomial analogy:
transverse Chow coefficients are symmetric functions of the roots,
multiplication matrices carry the finite algebra, and the source resultant
is their norm. Classical border-basis commutativity is the algebra
consistency condition behind the local MJ1 border-product test. The
Chow/norm polynomial retains joint spectral support but not the complete
nilpotent/Jordan data, which is why Hilbert and attachment questions remain
separate.

There is also a stopping-rule correction. The
[first attachment equation module](arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers)
satisfies \(Q_1=0\) exactly when an actual proper pair has reduced support
\(C\). Thus universal nonvanishing of \(Q_1\) would already be the desired
non-STCI theorem: \(Q_1\) is a **terminal support detector**, not a simpler
intermediate mechanism. The actionable predecessor is to extract necessary
coefficient, rank, tangent or border-algebra conditions on the homogeneous
resultant image \({\cal N}_Z\) and test the perfect-power target against
those conditions. Merely rewriting the target as a norm gives no
nonexistence theorem.


**Constant-row support test.** The
[five-row trace gate](arguments/torus/chow_arrangement_moments.md#a-five-row-trace-rank-gate-for-one-translate-versus-residual-translates)
turns the preceding spectral description into a small source matrix.  On a
proper Chow-matched pair, restrict the trace pairing of the finite symmetric
plane section to
\[
 W_4=\langle x_0^4,x_0^3x_1,x_0^2x_1^2,x_0x_1^3,
 x_1^4+x_0^3x_2\rangle .
\]
After trivialization by \(x_0^4\), the corresponding map
\(W\to B^\vee\) has rank four for exactly one distinct translated quartic
and rank five as soon as a second translate occurs.  Hence for a
Chow-matched pair already containing \(C_0\),
\(Q_1=0\) is equivalent to this five-row matrix having rank four.  The gate
is computable from Macaulay/Bezout trace matrices and avoids factoring the
full resultant.  It is not valid as a global-support criterion before the
Chow-polytope reduction: an arbitrary residual curve could have the same
fixed-plane support.
