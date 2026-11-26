---
id: STCI-F-0001
type: framework
title: Full torus boundaries and equations of moving supported ideals
status: in_use
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0037, STCI-R-0039, STCI-R-0040, STCI-R-0072, STCI-R-0073]
    to: [STCI-F-0001]
    at: "#available-results"
  - kind: limits
    from: [STCI-R-0043, STCI-R-0046]
    to: [STCI-F-0001]
    at: "#controls"
---
# Full torus boundaries and equations of moving supported ideals

## Scope

Fix an algebraically closed field, the embedded quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), and its torus of integer
weights \((0,1,3,4)\). For a bounded test fix ordinary degrees \((a,b)\),
the complete-intersection polynomial
\(P_{a,b}(n)=abn+ab(4-a-b)/2\), and an integer \(N>0\).
The closed incidence \(H_N\) consists of ideal sheaves with
\(\mathcal I_C^N\subset\mathcal J\subset\mathcal I_C\) and this polynomial.
The characteristic is part of each application; the geometric boundary and
generator criteria work in every characteristic, while the invariant-CI
obstruction has a different characteristic boundary.

The boundary results constrain actual supported intersections but do not
resolve unrestricted STCI. An obstruction for arbitrary pairs needs coverage
of actual moving pairs. Boundary geometry and realization loci are also worth
understanding before such an obstruction is known; examples and collision
strata can reveal the next useful question.

## Two distinct uses of boundary valuations

The [coordinate-contact theorem](../../arguments/torus/general_coordinate_boundary.md) assigns tropical rays and gcd weights to punctures of \(C\) in any realized coordinate-torus embedding and constructs its ray-only tropical compactification. It is a statement about the curve's coordinate contact orders, **not** about the initial ideals of hypothetical defining surfaces. Separately, the [fixed-sextic boundary theorem](../../results/ci_fixed_sextic_jet_rigidity.md) uses divisorial valuations of the **surface normalization** to bound the degree and generic contact of a mate. The former does not imply the latter: identifying a useful map between curve contact rays, surface boundary divisors, and the full equation/Hilbert degeneration data remains an open comparison. Do not treat a shared tropical ray as evidence of a residual component without controlling the actual intersection initial ideal.

**Generically regular arrangement carriers.** The [normalized almost-Cartier matrix theorem](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) extends the exact fixed-carrier monoid to possibly nonnormal integral carriers regular at every marked generic point. The [local orbit-lattice projection and contact theorem](../../arguments/torus/fixed_surface_restriction_lifts.md#local-index-lattice-and-contact-capacity-of-symmetric-arrangements) bounds the local index on an unshared branch by the gcd of its coefficients in all actual mates. For the exchanged sextic translates this now excludes all positive two-support partitions on carriers smooth or Du Val at both common endpoints, even allowing nonnormality elsewhere (independently reconstructed on November 23, 2026 at the scope recorded in the linked proof owner). This constrains actual mates on a specified fixed carrier, not limits reconstructed from cycles alone.

**Normal arrangement carriers.** The [componentwise normal-replacement theorem](../../arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier) covers every proper CI arrangement that is generically of embedding dimension at most one on each component, including reduced arrangements and every quartic translate pencil with more than one component in characteristic zero. The [exact fixed-normal-carrier monoid](../../arguments/torus/fixed_surface_restriction_lifts.md#normal-carriers-a-complete-geometric-description-of-the-arrangement-monoid) then reduces allowable multiplicity vectors to the kernel of a negative-semidefinite Hodge matrix together with Cartierness of the total divisor. This is seed-free on a specified normal surface. It agrees with the existing exceptional pencil's even diagonal lattice on its [nodal distinguished carrier](../../arguments/torus/quartic_exceptional_carrier_geometry.md#the-hodge-matrix-of-the-exceptional-carrier). It does not supply the missing classification of moving or nonnormal carriers or the reconstruction of limits. These deductions were independently reconstructed on November 23, 2026, at the scopes recorded in the linked proof owners.

## Available results

For effective one-cycles in every characteristic, [full Chow-polytope rigidity](../../arguments/equations/chow_polytope_rigidity.md) classifies equality with a multiple of the fixed quartic's full, unshifted column-weight polytope as a sum of diagonal translates. The subgroup fixes the cycle, not necessarily its defining ideal. This cycle statement does not recover Hilbert data, embedded points, moving generators, or a two-equation realization; projected polygons do not suffice.

The [first-moment theorem](../../arguments/torus/chow_arrangement_moments.md)
adds a linear Chow equation for invariant proper CI arrangements, including
every reduced CI arrangement. In characteristic zero their full Chow closure
avoids every complete collision \(m[C_{u,v}]\). In bidegree \((4,4)\) **in characteristic zero**, 
the [classification](../../results/quartic_chow_pencil_classification.md)
finds non-invariant lifts outside the invariant Chow closure. These are
one orbit over each \(2[C_{u,v}]+2[C_{u,-v}]\), and all still satisfy the
moment. A [one-carrier trace argument](../../arguments/torus/chow_trace_cone_jets.md)
reaches further presentation classes in arbitrary degrees. The general
higher-degree realization locus remains open.

The [sign-symmetry theorem](../../results/chow_acm_parity_vanishing.md)
now covers every actual sign-invariant ACM arrangement in characteristic
different from two, without retaining a CI Hilbert numerator or requiring
an effective CI-cycle decomposition. In characteristic zero both opposite
invariant pure hulls of a hypothetical sole-supported CI must therefore
be non-ACM. More precisely their finite section defects must contain a
[nonstandard-parity head class](../../arguments/torus/chow_section_parity_defect.md).
In fact every pure constant-orbit image with sole translated support has
this non-ACMness and parity defect in characteristic zero, without CI
origin. Their presence is automatic on the proposed endpoint algebras;
the source question concerns their compatible realization and multiplication.
This section defect \(D=N/(S/I_Y)\), at the cone vertex of the pure hull
\(Y\), is distinct from the full limit's finite embedded correction
\(T=I_Y/I_L\) at projective endpoints. There is already a canonical
surjection \(H^1(I_L(d))\twoheadrightarrow D_d\); the
[actual-family specialization account](../../arguments/normal-geometry/source_specialization_and_linkage.md)
retains its cohomological source. The question is which classes and
parity pairings the same two equations can induce, rather than whether
an unspecified comparison map exists. The
[section-cohomology profile](../../arguments/torus/boundary_section_cohomology.md)
also constrains every such pure hull, independently of the scalar
endpoint budget.
Before taking a limit, [actual-source sign symmetrization](../../results/sign_symmetrized_source_defect.md)
gives another exact comparison: the pure union \(V(J\cap\tau J)\) has
section defect \(H^0_{(x_0,x_3)}(S/(J+\tau J))\), with the specified
equivariant sign twist. This computes a defect from the actual source;
it is not an identification with the pure limit's \(D\). The issue is
which resulting torsion heads and multiplication data are compatible
with CI origin, rather than nonsaturation alone.
[Residual liaison](../../results/chow_moment_residual_speciality.md) separately
covers one doubled component with simple companions in all degrees and,
in characteristic zero, one tripled component with simple companions.
Neither mechanism establishes symmetry or ACMness of an arbitrary limit.

The [exceptional-pencil interpretation](../../arguments/torus/quartic_exceptional_carrier_geometry.md#two-sided-contact-and-the-nodal-even-eight-carrier)
relates two-sided endpoint cubic contact to an explicit even eight
on a ten-nodal quartic K3 resolution and nontrivial Weil
two-torsion. The [first-normal map](../../arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
describes a doubled-support degeneracy locus inside
\(\operatorname{Gr}(2,9)\). By
[complete-intersection self-linkage](../../arguments/torus/quartic_chow_pencils.md#self-linkage-and-the-canonical-conormal-quotient),
the nilpotent layer of any proper doubled pair is
canonically \(\omega_Y(-4)\); Serre duality controls the
degree-three and degree-four maps.
On the exceptional two-support locus this gives
**geometric uniqueness of proper quartic pencils**:
residual genus and the balanced normal bundle
exclude asymmetric multiplicities; the
[canonical-module rigidity proof](../../arguments/torus/quartic_chow_pencils.md#proof-route)
forces the entire \(\lambda\)-orbit, using the
Hilbert--Burch canonical presentation and restriction
to the residual line. Support reduction to that
locus still uses the distinguished torus coordinates. The [Hilbert-over-Chow orbit](../../arguments/torus/quartic_hilbert_chow_limits.md#hilbert-over-chow-and-the-characteristic-two-collision)
has opposite full embedded limits and specializes in characteristic
two to a non-invariant single-support quartic pair. The exact
Hilbert state-polytope comparison has not been carried out.

For [fixed-carrier mate cycles](../../arguments/torus/fixed_surface_restriction_lifts.md#symmetry-and-the-multiplicity-lattice),
the group orbit of a multiplicity vector generates a lattice of
realizable effective vectors on an integral \(S_2\) carrier regular
at the relevant generic points. The **generically regular** symmetric sextic
construction (generic regularity proved for an integral
symmetric sextic by its first-normal geometry) **excludes \((5,4)\)** by Bézout, and excludes all
remaining unequal two-support partitions on ordinary nodal
carriers. The [Du Val correction budget](../../arguments/torus/fixed_surface_restriction_lifts.md#ade-local-classes-and-the-global-sextic-correction-budget)
is conditional; neither this nor the K3 mechanism is a
general-degree STCI obstruction.

The [fixed-carrier arrangement and simultaneous conductor comparisons](supported_deformation_questions.md)
add actual incidence geometry and an exact endpoint correction. The quartic
carrier permits partial collisions but requires at least three distinct
translates in characteristic zero; the smooth quadric permits no such section.
For full toric limits, the quadratic conductor changes by the difference of
the base and selected graph's embedded endpoint lengths. Moving-carrier
thickenings and control of that difference by global equations remain open.

[R-0073](../../results/endpoint_equation_torsion.md) gives the kernel of
restriction to the two completed endpoints for every layer of the raw
equation torsion, in either torus direction. Unmixedness makes the
unfiltered restriction injective in each degree. For the first layer,
the residual intersection of the two extreme forms after division by
their gcd determines the line multiplicity that a supported limit must
account for.

For an actual characteristic-zero defining pair, the [paired endpoint
inequality](../../results/torus_quotient_movement_bounds.md#consequence-for-opposite-full-limits)
constrains the two full intrinsic limits using both matched embedded
lengths and the relative positions of the endpoint kernels. Its proof
uses surviving weight components of the moving equations. The same
movement theorem bounds the common quotient at \(r,-r\) for general
\(r\), using exclusion of a sign-eigen minimal generator; this is a
restriction on a fixed involutive pair, not just independently general
fibers. Recovering the
full opposite-endpoint algebras and moving generators remains open.

[R-0037](../../results/supported_hilbert_full_limits.md) supplies both full torus
limits in the same supported incidence, retaining the Hilbert polynomial and
the full limit schemes, including any embedded structure. Its exponent bound
for arbitrary supported Hilbert points is individual. For an actual
sole-supported CI of generic length \(m=ab/4\), primary contraction gives
\(I_C^m\subset J\), and this uniform containment persists along its
supported orbit; the triple-graph argument below records the proof.
[R-0038](../../results/torus_eigenvector_generator_lifting.md) lifts minimal
generators only when the whole homogeneous ideal is invariant.
[R-0040](../../results/invariant_supported_ci_exclusion.md) applies the trace
obstruction to such an invariant CI: characteristic zero excludes it, and in
characteristic \(p>0\) the degree product must be divisible by \(p\).
Invariance of the radical alone supplies no eigenform presentation.

The [radical-power lemma and equivariant counterexample](../../arguments/torus/equivariant_set_theoretic_descent.md)
make this distinction independent of the chosen thickening. Any homogeneous
ideal with radical \(I_C\) contains a homogeneous set-theoretic defining
pair if and only if \(I_C\) does; taking powers proves the reverse direction,
with no degree bound. In characteristic zero its minimum number of
eigenforms is exactly three. Thus searching for an arbitrary-degree
set-theoretic pair inside a fixed boundary simply restates the original
existence question. Prescribed degrees, actual ideal generation, or a
proved restriction on moving families must supply the additional information.
The three-line example disproves general eigenform descent for a rank-two
torus, even from a CI with an ACM full limit; its one-parameter subgroup
admits an eigenform pair. This does not decide eigenform descent for the
fixed integral quartic and its rank-one action.

The complete [Hilbert-boundary argument](../../arguments/torus_hilbert_boundary.md)
explains why the useful object is the whole fixed boundary ideal, with its
possible additional generators. The equation condition belongs on the moving
ideal. [R-0039](../../results/moving_ideal_generator_criterion.md) tests its entire
minimal-generator module \(J/S_+J\). A finite multiplication-map test requires
an actual regularity bound on the declared family.

## Directional loci

For a fixed ideal \(J_0\), let \(A_+(J_0)\) and \(A_-(J_0)\) mean the
sets of points whose full limits at zero and infinity are respectively
\(J_0\). For a pair of fixed ideals, study
\(A_+(J_+)\cap A_-(J_-)\). These are definitions of organizing sets.
The orbit extension in [A-0001](../../arguments/torus_hilbert_boundary.md#closed-incidence-and-both-full-limits)
puts both limits in the same connected component of \(H_N\) as the moving
ideal. Common Hilbert data and connected component are necessary for a pair.
Realizability requires a single ideal in the intersection, even if both
one-sided sets are nonempty. The opposite limits can have different normal
and endpoint structures. Fixed components may have positive dimension, so
one can also ask for incidence over pairs of fixed components. Finiteness,
local closedness, smoothness, and exhaustive coverage remain open here.

## Controls

[R-0043](../../results/sextic_eigenpair_quotient_bound.md) bounds proper sextic
eigenpairs, not arbitrary mixed-weight pairs. In
[R-0046](../../results/sextic_three_generator_full_limit.md), a proper sextic CI
has a full saturated ACM limit requiring generators of degrees \(6,6,10\).
Both fibers have residual degree 32 and generic multiplicity one on \(C\).
Their polynomial is \(36n-144\), but they are outside every sole-supported
\(H_N\). They test full-ideal bookkeeping, not supported-CI nonemptiness.

The Hilbert-limit scheme, the two extreme equation forms, the normal-cone
initial ideal, and the fundamental cycle are different objects. Keeping only
a cycle or a pure hull can discard data necessary for deformation. Likewise,
following individual points in a residual divisor does not compute its flat
divisor limit; [R-0048](../../results/moving_sextic_residual_limit.md) supplies a
concrete control. [R-0049](../../results/sextic_residual_absorption.md) transfers
some residual multiplicity to \(C\) while retaining a residual line; it does
not prove that transfer can be iterated to sole support.

## Bridges

The [supported generator investigation](../../investigations/supported-generator-incidence/index.md)
asks for an actual specified supported family and its two-generator locus.
The [quotient comparison investigation](../../investigations/quotient-hilbert-comparison/index.md)
asks which transverse, endpoint, section-hull and source data can arise
together from the same two equations. The relative-image and cohomological
specialization maps are inputs to this question. Both investigations
retain the full embedded object. The
[endpoint comparison](../../results/intrinsic_limits_endpoint_fibers.md)
gives the pure limit and embedded lengths; its
[cohomology refinement](../../arguments/torus/boundary_section_cohomology.md)
tests the whole pure section hull through a two-lattice interpolation map.
Use this and the
[sextic endpoint conditions](../../arguments/torus_hilbert_boundary.md#necessary-endpoint-conditions-for-a-sextic-pair)
before assigning a curvilinear or noncurvilinear endpoint fiber to a
proposed sole-support family.

A construction must verify support, polynomial, and actual homogeneous ideal
generation. An obstruction must cover its declared family. Extending it to all
supported pairs of a fixed degree requires coverage of the relevant fixed
limits and attracting families inside the known uniform incidence
\(H_{ab/4}\); extending it to all degrees is a further problem.
Finding an arbitrary supported flat deformation to a CI is already useful;
realizing a prescribed torus boundary as an orbit limit is a stronger task.

### Jacobian recognition beyond invariant degenerations (PR #173)

The [spectral–Jacobian criterion](../../arguments/torus/spectral_jacobian_first_jet_bridge.md)
recognizes translated reduced support from **two actual ideal
memberships**, assuming a proper CI disjoint from the opposite
fixed line: a product of members of the quadric pencil belongs to
the ideal, and the mixed Jacobian relation
\(A M_{12}-2B M_{03}\) belongs to it. This holds for
non-invariant nonreduced CI arrangements, including the exceptional
quartic component outside the invariant-CI Chow closure. It does
not assert that these two equations generate the CI ideal.
The first moment is half a perfect skew residue of first projection-
line jets. Proving isotropy for all pairs satisfying this entire
support-recognition incidence remains open. Full toric limits can
lose generators, so a fixed invariant limit is still not a substitute
for this actual equation gate.

## Cycle incidence versus actual equations

For actual pairs whose entire cycle consists of translates, see the
[Chow realization framework](../chow-realization/index.md) for the
equation conditions on the prescribed cycle.

For a **proper** pair of degrees \((a,b)\) containing \(C\), its
fundamental cycle is \([Y]=m[C]+R\), with \(ab=4m+\deg R\).
The existing [multiplicity-strata argument](../../arguments/residuals/marked_deformation_and_absorption.md#fixed-degree-multiplicity-strata-of-actual-pairs)
proves that \(m\ge r\) is closed on the proper-pair locus by finite
normal-jet rank conditions. Equivalently, the Chow form of the
intersection is divisible by the \(r\)-th power of the Chow form of
\(C\). This latter description is a **linear subspace condition** in
the projective space of Chow sections; it is not a linear condition on
the original equation coefficients.

When \(4\mid ab\), the terminal condition \(m=ab/4\) for an **actual
proper pair** forces \(R=0\) by degree exhaustion and purity; hence
the pair is sole-supported. This sufficiency does **not** extend to
an arbitrary limiting Chow coordinate, improper pair, or Hilbert
boundary: a cycle alone cannot recover embedded structure or the
generators of the limiting ideal.

The proper-pair locus
\(\mathbf P(I_C(a))\times\mathbf P(I_C(b))\) (or the pencil
Grassmannian when \(a=b\)) retains actual equations and their
cycle map. The supported Hilbert incidence \(H_N\) retains full flat
ideals, including opposite limits. A graph of the equation-to-ideal
map can relate their closures, but its boundary ideals need not be
generated by limiting equation pairs. Use the full moving generator
criterion [R-0039](../../results/moving_ideal_generator_criterion.md),
not merely a Chow equality or an extreme-weight pencil.

The older torus/VGIT investigations distinguish the GIT weight of a
pencil from the Hilbert limit of its ideal. Semistability or weight
data alone do not give a supported intersection. Likewise, cycle-level
residual absorption does not supply a flat supported CI deformation.
The [marked absorption argument](../../arguments/residuals/marked_deformation_and_absorption.md)
already establishes partial-absorption controls. Further Chow or
VGIT machinery should strengthen these existing tests rather than
duplicate them.

For a [prescribed reduced Chow-matched cycle](../../arguments/equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle),
the degree-labeled eigenform evaluation spaces and their common fixed
factors decide actual CI realization; degree exhaustion excludes boundary
residuals after properness. In degree \((4,4)\) the explicit
line-and-quartic model and the exceptional orbit exhaust the actual
pencils. The latter has two [saturated five-generator limits](../../arguments/torus/quartic_hilbert_chow_limits.md#chow-closure-and-full-opposite-limits),
each with an embedded length-two point, whereas its cycle is fixed.
For an original proper Chow-matched pair in any degree, the
[relative different](../../arguments/torus/chow_endpoint_different.md)
detects single support from one finite jet. A global bound on that jet
from unrestricted equation sources remains open.

## Clean-cancellation boundary

The [clean-cancellation theorem](../../arguments/torus_hilbert_boundary.md#clean-cancellation-and-residual-descent)
gives a sharper necessary condition than merely requiring common
extreme factors. For a hypothetical characteristic-zero supported
pair, in **each** torus direction write the extreme forms as
\(Hu,Hv\) with \(\gcd(u,v)=1\), and let \(D_0\) be the first
nonzero normalized cancellation coefficient. Then
\(\gcd(H,D_0)\ne1\): otherwise the full initial ideal is the
three-generator ACM ideal \((Hu,Hv,D_0)\), and its cycle
decomposition forces an excluded eigenform STCI for \(C\).
This restricts the **first correction**, not just the extreme
forms. Further shared factors and higher cancellations remain
unclassified; the statement is not an all-degree exclusion.

The extra initial generators can be measured by
\(H^0_{(t)}(S[t]/(F_t,G_t))/t\), the vertical torsion of the
chosen equation presentation. It is different from the
intrinsic \(I_C\)-adic comparison defect in
[R-0030](../../results/local_filtration_comparison_defect.md).
Keep these two filtrations separate when connecting torus
limits to normal Rees data.

The [classified collision](../../arguments/torus/fixed_carrier_chow_arrangements.md#all-order-primary-structure-and-attachment-on-the-classified-carrier) and [attachment duality](../../arguments/residuals/layerwise_attachment_and_triples.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component) calibrate actual proper pairs. Do not apply linkage to a pure hull of a full limit with embedded points without identifying an actual Gorenstein CI and its full primary. Full attachment is not a monotone proxy for residual degree.

## Embedded-point control for full limits

The [four-generator line control](../../arguments/torus_hilbert_boundary.md#a-four-generator-full-limit-with-an-embedded-point)
shows that even a sole-supported proper complete intersection
can degenerate to a saturated, non-ACM full ideal with an
embedded point. The pure hull has a different Hilbert polynomial,
and the least degree product of a proper pair **inside the limit**
can rise. This complements the existing ACM sextic
three-generator example, which instead retains residual curves.
Neither control is a sole-supported quartic example or an
obstruction to all moving supported pairs. Together they rule
out replacing full-limit incidence by a pure-hull, cycle-only,
or monotone degree-product argument.

## Graph incidence and the centered-weight gate

The [equation–Hilbert–Chow graph](../../arguments/torus_hilbert_boundary.md#equationhilbertchow-graph-and-its-top-fiber)
distinguishes the closure of **supported** proper pairs from
the larger top-cycle fiber reached also by residual pairs.
In characteristic zero, connectedness of complete-intersection
graph limits and cycle specialization imply that the latter
fiber has reduced support \(C\); nevertheless only its
intersection with the actual CI locus solves the prescribed
degree existence problem. The supported-approximant closure
also retains the uniform power containment \(I_C^{ab/4}\subset J\),
which cannot be inferred for an arbitrary top-cycle boundary.

For the centered torus weights \((-2,-1,1,2)\), the Chow
resultant gives a nonvanishing invariant section of the
natural \(\mathcal O(b,a)\) linearization on every actual
sole-supported proper pair. Hence such a pair is
\(T\)-semistable at character zero; for equal degrees its
pencil is semistable for the Plücker polarization.
In characteristic zero, the eigenform obstruction makes
these inequalities **strict** on actual supported pairs.
This removes wholly one-sided centered weight blocks
from the *moving proper-pair search*, but does not impose
stability on the improper equation coordinates of their
full graph limits. Other VGIT chambers need not be
enumerated to cover supported pairs.

### Fixed-degree incidence and VGIT scope

The [equation-pair rank and weight formulas](../../arguments/torus/equation_pair_rank_and_weights.md)
extend the first degreewise cancellation count to unequal degrees and
distinguish the flat graded ideal from its projective saturation. They also
describe the actual quotient by additions of lower-equation multiples for
unequal pairs. These are source and boundary constraints, rather than an
existence test for a supported pair. In particular a common-factor rank
defect does not locate all additional generators of the saturated limit.

The [reconciled Chow filtration and sextic weight partition](../../arguments/torus_hilbert_boundary.md#reconciled-chow-filtration-and-finite-sextic-weight-partition)
make the proper-pair side of this framework more explicit. For each degree
type, the locus of generic multiplicity at least \(r\) is the inverse image
of the linear Chow subspace \(\mathbf P(Q^rE_{ab-4r})\), **relative to
the open proper-pair locus**. When \(4\mid ab\), all actual supported
pairs lie in one affine nonvanishing chart of a Chow-resultant coefficient;
the terminal fiber is cut out by finite coefficient equations there.
This affine incidence is the primary fixed-degree existence target;
projective graph and Hilbert limits are retained to obtain obstructions
and understand degenerations, not to define existence.
Neither the affine chart nor its Chow equations determine the full
Hilbert-boundary ideal.

For sextic pencils the coarse Plücker-weight calculation gives 35 ambient
candidate walls and 34 chambers. The centered Chow semistability gate
already covers every supported proper pencil at character zero; in
characteristic zero the established eigenform obstruction R-0042 makes
these pencils strictly stable for that centered linearization. This
is necessary, not sufficient, and does not apply to improper limiting
pencils. Hence a full VGIT chamber sweep is **not a prerequisite** for the STCI search.
Use other chambers only for a declared residual or graph-boundary
comparison, and always retain the actual generator and endpoint tests.

## Invariant residual incidence and absorption

The [orbit-curve classification and residual counterexample](../../arguments/torus_hilbert_boundary.md#invariant-residual-supports-and-absorption-limits)
show that invariant reduced curves meet the marked quartic
only at its endpoints, except for the unique disjoint
coordinate line \(L_{12}\). The latter can occur in a
connected proper intersection through chains of other
residual components, so direct endpoint attachment is
not a universal constraint. Under flat specialization
the marked multiplicity can rise as residual cycle
specializes onto \(C\), but cycle-level absorption
does not ensure a two-generated full Hilbert limit.
These distinctions refine the geometric incidence
strata without asserting that all residuals can be
removed by further torus translations.

## Coverage boundaries

Failure of eigenform equations does not exclude other moving equations or
attracting families; failure at one fixed ideal does not exclude other
components. The [finite residual controls](../../arguments/torus_sextic_residuals.md#finite-replay-evidence)
check calculations but do not prove realization or coverage.

## Weight geometry and moving families

[Weights and full limits](weights_and_limits.md) gives the normal-coordinate
and endpoint geometry behind the directional loci. The
[supported deformation test](supported_deformation_questions.md) explains
what a represented family can establish. The same approach can organize a
[downstairs ACM construction](../global-equation-realization/projection_and_liaison.md)
if the moving ideal is tested at that threshold. Explicit
[residual constructions](../residual-construction/index.md) explain how
generation or cycle support can change without providing supported limits.


### Focused mathematical developments

- [Torus actions, endpoint frames, and transport](torus_actions_and_endpoint_frames.md)
- [Weight components and normal filtrations](weight_symbols_and_normal_filtrations.md)
- [Extreme weights and saturated Hilbert limits](extreme_weights_and_hilbert_limits.md)
- [Generic transverse algebras and endpoint contact](generic_algebras_and_endpoint_contact.md)
- [Global postulation and residual support](global_postulation_and_residual_support.md)
- [Sextic filtration and source comparisons](sextic_filtration_and_source_comparisons.md)

The original [section-address compatibility page](weights_and_limits.md) retains old headings for existing references. The developments distinguish individual equation symbols from the saturated full initial ideal, and generic normal algebra from endpoint extension and global support.

## Relation persistence as a boundary refinement

The [degree-12 rational sextic control](../../arguments/torus_hilbert_boundary.md#degree-12-relation-persistence-for-the-residual-sextic-pencil)
shows why a common-factor stratum and a coarse Plücker weight
interval do not determine a full Hilbert state. For a moving
section on a fixed hypersurface, the parameter-adic Smith
exponents of multiplication measure successive lifting of
limiting relations. Their sum is the determinantal contact
order (valuation of maximal minors). In the two residual
controls the profiles are \((1^8,2)\) and \((1^2,2)\),
although the coarse Plücker interval and negative full limit
agree. Their degree-12 positive determinant weights are
\(-780\) and \(-810\).

This is a standard filtered-module construction, not a
classification of graph fibers or a new STCI obstruction.
The profile belongs to the specified multiplication presentation and
the uniformizer of the effective orbit trait (here \\(v=t^5\\), rather
than the original torus coordinate \\(t\\)). It is not intrinsic to a
Hilbert boundary point and need not be comparable across different
presentations or fixed hypersurfaces. Use it as an
intermediate check when a common-factor limit makes direct
full-ideal computation expensive. It must not be conflated
with the intrinsic normal filtration along \(C\), nor with
the transverse endpoint image filtration.

In the positive degeneration of the first pencil, two degree-12 classes
vanish on their layer at both geometric endpoints of the same family.
They persist at the generic point of the disjoint coordinate line even
though parameter saturation removes the family there.
[Explicit first-layer classes](../../results/endpoint_equation_torsion.md#a-relation-missed-at-both-endpoints).

The canonical [R-0074](../../results/chow_polytope_rigidity.md) classifies **all** effective cycles in this rigid Chow-polytope fiber; invariance is deduced, not assumed. Its [proper-pair reformulation](../../arguments/equations/chow_polytope_rigidity.md#proper-surface-pairs-and-the-remaining-equation-question) is a classical resultant coefficient condition, not a criterion in the Newton polytopes of the equations alone. The [R-0050 integration](../../arguments/equations/chow_polytope_rigidity.md#eigenpairs-and-transverse-finite-quotients) keeps boundary exclusion and binomial-only subgroup structure explicit.

The [general-coordinate boundary calculation](../../arguments/torus/general_coordinate_boundary.md) is a different compactification from the marked two-ray torus: it proves normalization-order and gcd-weight formulas for all realized coordinate frames, with a proper ray-only tropical compactification and flat multiplication (smooth exactly for primitive contacts), not a global parameter fan. The [H16 parameterization](../../arguments/equations/chow_polytope_rigidity.md#set-level-symmetric-power-fiber-h16) identifies geometric cycle points with a symmetric power, not the Chow fiber scheme; multiple-cycle infinitesimal stabilizers require special care in characteristic p.

[H17 boundary reconstruction](../../arguments/torus/boundary_reconstruction_and_defects.md) distinguishes whole-boundary embedded data from separate face images. It proves bounded-degree CI reconstruction and finite-order nonuniqueness with restricted ordinary Rees data; torus radical support and equation-lifting defects remain distinct.


### Poisson restriction on full supported boundaries

A sole-supported CI is involutive by the reviewed contact theorem.  The
intrinsic torus weight filtration is compatible with the bracket (weight
shift \(-4\)), so initial ideals remain involutive; localization,
contraction and projective saturation preserve self-involutivity.  Hence
[both full torus limits](../../arguments/torus_hilbert_boundary.md#involutivity-persists-through-the-full-torus-boundary)
of any hypothetical supported CI are torus-fixed involutive points of the
same supported Hilbert locus, even when they acquire extra generators.

This does **not** reduce the problem to invariant complete intersections.
For sole transverse support, Scheja--Storch and the explicit quartic
transverse bracket make every pure constant-orbit image automatically
involutive.  If \(L\) is a full limit and \(Y=L^{\rm pure}\), the only
remaining contact datum is the finite endpoint obstruction
\[
 \kappa_L:\wedge^2(I_L/I_L^2)\to (I_Y/I_L)(-2).
\]
The projective twist records bracket degree \(-2\); the ungraded
affine-cone version has target \(I_Y/I_L\).
R-0070 gives the two lengths of the target but not \(\kappa_L\).  A useful
boundary refinement therefore needs the actual endpoint correction algebra
or the weight-graded full ideal; another classification of the pure orbit
quotient cannot exploit contact.


**Diagonal controls and actual CI boundaries.** The diagonal
constant quotient \(B_n=k[\epsilon]/(\epsilon^n)\), \(u=v=1+\epsilon\),
is exactly the Cartier multiple \(nC\subset Q\).  Its symmetric endpoint
defect is \(3n(n-1)/2\) and its polynomial is
\(4nd+4n-3n^2\).  Matching a CI polynomial gives
\((3a-8)(3b-8)=16\): \(4C\) matches \((4,4)\), while \(6C\) matches
\((3,8)\), up to order.  These pure sole-supported curves are torus-fixed
and automatically involutive, but the
[cohomology obstruction](../../arguments/torus/boundary_section_cohomology.md)
excludes them even as pure quotients of flat CIs of the matching types.
More generally it excludes a diagonal endpoint algebra whenever
\(n=ab/4\le a+b-3\). In the degree range \(a,b\ge5\), this removes
\(B_9\) for \((6,6)\) and \(B_{10}\) for \((5,8)\), despite possible
embedded corrections of lengths 63 and 80. These are controls on pure
curves, not examples of CI-compatible acquisition of a section defect.
The cohomology exclusion is characteristic free. For diagonal models with
\(n\ge a+b-2\), their complete splitting profile passes every such
inequality, so testing further twists gives no additional exclusion.

The known exceptional quartic limits have ACM pure hulls, and the
\((16,16)\) equation-layer control has a CI pure hull, despite their
nonzero endpoint corrections. A bounded alternative is to construct or
exclude an actual full-translated-cycle CI boundary with \(D\ne0\),
including moment-zero cases where parity contributions might cancel.
This asks about the section hull's attainability; noninvariance of an
actual CI and nonzero \(T\) are already realized phenomena.
