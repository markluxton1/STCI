---
id: STCI-F-0002
type: framework
title: Embedded torus quotients and projective endpoint descent
status: in_use
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0051, STCI-R-0052, STCI-R-0053, STCI-R-0056, STCI-R-0072]
    to: [STCI-F-0002]
    at: "#available-results"
  - kind: limits
    from: [STCI-R-0054]
    to: [STCI-F-0002]
    at: "#embedded-controls"
---
# Embedded torus quotients and projective endpoint descent

## Scope

Work over an algebraically closed field and the fixed quartic torus action.
On the dense coordinate torus use
\(x=(1,t,t^3u,t^4v)\). A finite *embedded* quotient
\(B=k[u^{\pm1},v^{\pm1}]/K\), of length \(0<n<\infty\), determines a constant
family of orbit closures and its projective scheme image. The full maps from
the Laurent ring are data: an abstract isomorphism class of Artin algebras
does not determine this image. Keep every characteristic restriction of an
example or descent assertion.

The constant-image results do not by themselves cover moving transverse quotients.

### Universal full-Chow envelope above every moving quotient

The [full two-dimensional Chow pullback](../../arguments/torus/full_transverse_chow_pullback_envelope.md)
supplies a canonical constant **fat-point**
algebra above *every* actual translated-cycle
CI, with no invariant-ideal hypothesis.
For \(\sigma=\sum_i n_i[(u_i,v_i)]\),
\[
 B_\sigma=
 k[u^{\pm1},v^{\pm1}]/
       \bigcap_i\mathfrak m_i^{n_i},
 \quad
 \dim B_\sigma=\sum_i\binom{n_i+1}{2}.
\]
The full Chow form, pulled through
the first degree-four three-monomial
torus quotient and its opposite
chart, gives \(2(m+1)\) explicit
homogeneous ideal-membership conditions
for any realizing CI.
The resulting actual finite-flat algebra
over the intrinsic orbit coordinate
\(t\in\mathbf G_m\) is a **rank-\(m\)
moving quotient** of
\(B_\sigma\otimes k[t^{\pm1}]\),
with kernel rank
\(\sum_i\binom{n_i}{2}\).
Its norm of \(X+uY+vZ\) is the
**complete transverse Chow form**;
its trace of \(u/v\) is \(M_1\).
The quotient is forced constant for
reduced cycles, while each double
component adds a moving \(\mathbf P^1\)
normal-direction choice.
Unlike R-0051–R-0056, this is a
**necessary constant envelope for an
arbitrary moving CI quotient**,
not a claim that every moving quotient
comes from a constant embedded image.
Both endpoint descent and generation
by **two actual homogeneous equations**
remain essential. The all-degree
universal \(M_1=0\) theorem is not proved.

The [opposite quadric–cubic Chow polarization](../../arguments/torus/weighted_chow_quadric_cubic_polarizations.md) sharpens the constant fat-envelope source below: two degree-\((2m,\ldots,3m)\) coefficient chains, sharing the quadric-spectrum term, generate **the same dense-torus ordinary-power envelope** and have combined radical exactly the translated support. Their first opposite polars satisfy a homogeneous syzygy with coefficient \(M_1\). This gives lower-degree input for comparing the **same actual global two-generator quotient** with the moving-quotient and two-endpoint descent theorems. It does **not** extend the sole-supported movement bounds R-0072 to multiple supports, nor prove first-moment vanishing.

**Saturation correction.**
The [spectral-interpolation review](../../arguments/torus/spectral_interpolation_and_polar_saturation.md)
proves that the *two*
opposite polarized fat-point
envelopes are the **same**
after restriction to the
dense ambient torus.
An actual full-support CI
is saturated by the
coordinate product, so
opposite-polar membership
is automatic from one
chain; the syzygy containing
\(M_1\) is not an
independent obstruction.
What remains is a
**moving finite quotient
of the single canonical
fat-point source**, with
the correct norm and
two-endpoint global descent.
When the quadric parameters
are distinct, the
entire paired configuration
is compactly encoded by
the spectral polynomial
\(H\) and an interpolation
polynomial \(K\), with
\(K/H\) residues
\(n_i/u_i\), even for
nonreduced multiplicities.

## Mathematical scope and interfaces

This approach studies **embedded finite torus quotient images**, their
projective endpoint contractions, contact geometry, and comparisons with
moving torus degenerations. The [complete quotient proof](../../arguments/torus_embedded_quotients.md)
and [endpoint image theorem](../../results/orbit_image_endpoint_polynomial.md)
give constant-image controls. The [intrinsic endpoint-fiber comparison](../../results/intrinsic_limits_endpoint_fibers.md)
determines pure parts and embedded lengths under its hypotheses, but does not
resolve the full source-realization question in the
[Investigation](../../investigations/quotient-hilbert-comparison/index.md).
For CI origin, retain the pure image's free section hull and finite vertex
defect separately from the full limit's finite endpoint correction. The
[section-cohomology comparison](../../arguments/torus/boundary_section_cohomology.md)
constrains the whole splitting profile and computes its cohomology by one
two-endpoint interpolation map on the actual embedded algebra. The
[actual-family specialization account](../../arguments/normal-geometry/source_specialization_and_linkage.md)
provides canonical cohomological sources for the pure section defect;
their allowed images under a two-equation presentation remain the issue.
Independently, [symmetrizing the actual ACM source](../../results/sign_symmetrized_source_defect.md)
identifies its invariant union's section defect with the torsion of
\(S/(J+\tau J)\), including its equivariant sign twist. This is an
explicit source comparison before degeneration, distinct from the
endpoint correction and the pure torus limit's section defect.
The [supported-boundary approach](../torus-supported-boundaries/index.md)
provides complementary full-ideal and opposite-limit techniques; neither
approach excludes studying the other's degenerations. Contact, polarization,
and conductor constraints meet in [contact and global descent](contact_and_global_descent.md#the-approaches-and-their-exact-reach).

## Available results

[R-0072](../../results/torus_quotient_movement_bounds.md) bounds the
splitting degrees and the generic secant and tangent ranks of the entire
moving quotient of a characteristic-zero defining pair. Its endpoint
inequality compares the two kernels in the same transverse coordinates.
The fixed-involution refinement bounds the common quotient at \(r,-r\)
by \(m-\lceil(4b-7)/7\rceil\) for general \(r\); in particular the
embedded quotient cannot factor through \(r\mapsto r^2\).
The [one-summand control](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#one-moving-summand-with-the-complete-intersection-polynomial)
has the CI Hilbert polynomial in arbitrarily high degree and fails the
splitting bound.

[R-0051](../../results/constant_embedded_orbit_image.md) constructs the finite
image and its pure Cohen–Macaulay structure.
[R-0052](../../results/orbit_image_endpoint_polynomial.md) measures its two
endpoint image lattices and gives
\[
P_{Z_B}(d)=4nd+n-\delta_0-\delta_\infty.
\]
[R-0053](../../results/constant_quotient_equation_criterion.md) uses the actual
homogeneous equation spaces: a degree-\((a,b)\) realization requires a
gcd-one pair in those spaces and degree exhaustion \(ab=4n\).
[R-0056](../../results/pure_curve_degree_exhaustion.md) supplies the separate
purity argument that turns inclusion and degree exhaustion into scheme
equality. Equal degrees of unrelated schemes would supply no such conclusion.
The [complete quotient argument](../../arguments/torus_embedded_quotients.md)
retains the construction, proofs, examples, and characteristic comparisons.

## Embedded controls

[R-0054](../../results/embedded_quotient_endpoint_counterexamples.md) preserves
distinct embeddings with isomorphic abstract algebra and their different
endpoint images, including characteristic-dependent behavior and non-Gorenstein
local structure. Defect lengths alone do not determine the full gluing algebra.
They also do not determine the two-lattice interpolation ranks. The
[diagonal-algebra exclusion](../../arguments/torus/boundary_section_cohomology.md#3-diagonal-endpoint-algebras-can-fail-despite-finite-correction)
rules out \(u=v=1+\epsilon\), \(\epsilon^n=0\), as either endpoint of a
sole-supported CI\((a,b)\) when \(n=ab/4\le a+b-3\). In the surviving
degree range this excludes \((a,b,n)=(6,6,9),(5,8,10)\), up to degree
exchange, even when finite corrections repair the Hilbert polynomial.
This cohomological statement is characteristic free; when
\(n\ge a+b-2\), the full diagonal profile passes every twist test.
[R-0055](../../results/flat_collision_of_orbit_images.md) gives a controlled
collision with verified relative image lattices; constancy of one numerical
defect is not its flatness proof.

The positive-characteristic prescribed quartic control
[R-0021](../../results/quartic_mu4_degeneration.md) retains its own stated
scope. Its flat integral model has three residual quartics on the geometric
generic fiber. The [normal filtration calculation](../../results/quartic_normal_initial_base_change.md)
exhibits failure of associated-graded base change, a different operation from
base change of the projective image. The [finite specialization checks](../../arguments/quartic_specialization_and_symbols.md#finite-quartic-replay-evidence)
replay identities for this pair and the fixed quartic's degree-four symbols.
Actual equation recovery after projective contraction still requires the
embedded quotient and the homogeneous source test.

### Quadrics and cubics as the two quotient characters (PR #173)

The [intrinsic spectral–Jacobian bridge](../../arguments/torus/spectral_jacobian_first_jet_bridge.md)
replaces arbitrary affine quotient coordinates by the two homogeneous
characters
\(\xi=x_1x_2/(x_0x_3)\) and
\(\eta=x_0x_2^2/(x_1^2x_3)\). They determine the
unique containing quadric and a cubic scroll respectively, and
\(Q_\xi\cap R_\eta\) is exactly the translated quartic plus
two fixed endpoint ruling lines. Thus the full arrangement records
paired points in these two character coordinates; a quadric spectral
polynomial alone loses the cubic parameter and the pairing.
The companion Jacobian identity is valid in the actual nonreduced
CI ring, but does not reconstruct all nilpotent multiplication from
its cycle. The new first-jet residue pairing is a necessary
algebraic test conditional on whole translated-cycle support.

## Bridges

The [comparison investigation](../../investigations/quotient-hilbert-comparison/index.md)
connects this lens to [full supported Hilbert boundaries](../torus-supported-boundaries/index.md).
For a proper degree-\((a,b)\) pair with sole reduced support \(C_0\), the
investigation points to the separate finite-modification and strict-movement
proofs. In characteristic zero or characteristic \(p>0\) with \(p\nmid ab\),
the embedded quotient has positive degree. Its endpoint budget constrains
one moving object. [R-0070](../../results/intrinsic_limits_endpoint_fibers.md)
determines the pure parts of both intrinsic limits and their two embedded
lengths from the corresponding endpoint fibers. The full opposite-endpoint
algebras and moving generator incidence remain open. The pure section hull
must pass cohomological semicontinuity. By contrast, the
[nonstandard-parity condition](../../arguments/torus/chow_section_parity_defect.md)
is automatic for every sole-support constant image in characteristic zero,
with no CI-origin premise. It describes the multiplication and extra
sections that an actual source would have to induce, rather than filtering
the endpoint algebras independently. Endpoint \(T\), vertex defect \(D\),
and the finite contact map on \(T\) are separate retained data.

Use the relative image map in R-0070 when comparing an embedded quotient
and an intrinsic limit, together with the actual-family cohomological
specialization maps when comparing section defects. Recovering the full
special equation module requires further data. Even the two completed endpoint presentations of
one raw equation family can lose first-layer classes along the disjoint
coordinate line. The [endpoint kernel formula](../../results/endpoint_equation_torsion.md#statement)
specifies what that restriction detects. Applying it to a proposed
transverse quotient first requires actual homogeneous equations for the
same family. Any finite prescribed-degree test must retain
the actual source image and establish properness.

## Coverage boundaries

Constant quotients do not cover nonconstant moving families; curvilinearity
or a fixed abstract quotient type requires a coverage argument. The
[finite controls](../../arguments/torus_sextic_residuals.md#finite-replay-evidence)
check identities but do not establish image descent or projective realization.

The [finite primary canonical colon identity](../../arguments/residuals/first_graph_finite_transfer.md#local-canonical-ideal-version-and-several-marked-points) supplies an actual curve-conductor comparison in transverse charts with identical generic algebras. With an image residual it uses the attachment ideal, not the conductor of the ambient surface. The [semigroup primary computation](../../arguments/torus/fixed_carrier_chow_arrangements.md#all-order-primary-structure-and-attachment-on-the-classified-carrier) gives explicit layer indices on the classified carrier.

## From contact to descent

[Contact and global descent](contact_and_global_descent.md) compares the
Jacobian, polarization root, and the full endpoint conductor. The rank of
the moving family, its multiplication, and the contracted endpoint
subalgebras constrain the image together. Comparing with an
[arithmetic collision](../arithmetic-supported-lifts/index.md) requires
checking normal specialization separately from the projective family.

### Reduced cycles and the first nonreduced gap

For [specified reduced Chow cycles](../../arguments/equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle),
purity forces a reduced scheme and closes the invariance gap in
testing actual generators. On the partial diagonals, the
[exceptional \((4,4)\) orbit](../../arguments/torus/quartic_chow_pencils.md#classification)
has generic length two on each of two translates and full opposite
limits gaining embedded length two at opposite endpoints. Its
[relative different](../../arguments/torus/chow_endpoint_different.md)
recovers the reduced support count and the endpoint normalization
colength from the actual finite pencil algebra. Extending the equation
comparison to higher-degree repeated cycles requires the moving
generators and their parameter relations.

The [exceptional quartic](../../arguments/torus/quartic_hilbert_chow_limits.md#hilbert-over-chow-and-the-characteristic-two-collision)
is an exact control: a nontrivial \(\mathbf G_m\)-orbit of Hilbert
points has a **constant Chow point**, but its two full flat limits
acquire different embedded endpoint corrections. The
[Hilbert--Burch normal-map model](../../arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
retains first-normal data invisible to Chow. The
[geometric classification](../../arguments/torus/quartic_chow_pencils.md#proof-route)
is now complete: linkage excludes asymmetric multiplicities,
and the canonical module of the Hilbert--Burch resolution
with restriction to the residual line forces the
\(\lambda\)-orbit. This applies to actual proper quartic
pencils over the fixed two-support cycle, not arbitrary
embedded torus-quotient families. In
characteristic two, the same formulas give a non-invariant quartic
single-support complete intersection, a \((2,2)\) splitting that
contrasts with the binomial \((1,1,1,1)\) split in characteristic
zero. The [relative different](../../arguments/torus/chow_endpoint_different.md#classical-discriminant-and-index-interpretation)
measures the reduced endpoint normalization lattice, not the
complete Hilbert lift or its limit corrections.


### From endpoint contacts to local divisor classes

The [orbit-lattice/contact theorem](../../arguments/torus/fixed_surface_restriction_lifts.md#local-index-lattice-and-contact-capacity-of-symmetric-arrangements) supplies an intersection-theoretic use of the two-branch endpoint length: actual mate relations bound local index orders, and at odd-index smooth or Du Val common endpoints the first-symbol vanishing cannot exceed the contact length (for the stated involution). For the exchanged sextic translates the two contact lengths are four. Together with the mixed Hodge pairing this excludes both endpoints being smooth or Du Val, independently reconstructed on November 23, 2026 at the scope recorded in the linked proof owners. It does not identify the completed nonreduced endpoint algebra or reconstruct a pair from its cycle.

## Universal translate incidence

Let \(T\) be the diagonal torus, \(H=T_C\), and
\(B=T/H\cong(\mathbf G_m)^2\), the genuine quotient torus. Its
universal translated curve has restriction maps
\(W_d\otimes\mathcal O_B\to\mathcal E_d\), where
\(W_d=H^0(\mathbf P^3,\mathcal O(d))\) and
\((\mathcal E_d)_\beta=H^0(C_\beta,\mathcal O_{C_\beta}(d))\).
These maps have constant rank because the translates are projectively
equivalent. Their kernels \(\mathcal K_d\) are vector bundles, and
\[
 \mathbf P_B(\mathcal K_a)\times_B\mathbf P_B(\mathcal K_b)
\]
parametrizes pairs together with a chosen entire translate they contain,
where the projective bundles are nonempty. Choose a splitting
\(B\to T\) and its diagonal linear lift. Transporting forms
trivializes each kernel as
\(\mathcal K_d\simeq H^0(\mathcal I_C(d))\otimes\mathcal O_B\).
Thus this incidence is noncanonically
\(B\times\mathbf P H^0(\mathcal I_C(a))\times
\mathbf P H^0(\mathcal I_C(b))\), empty if an equation space is zero.
A scalar change of the lift acts trivially on the projectivization.

This standard, trivial incidence construction packages the
[actual coefficient restriction kernels](../../arguments/torus/fixed_surface_restriction_lifts.md#translate-coordinates-constrain-actual-coefficients).
It does not impose properness, exclude coordinate-boundary components,
or compute transverse multiplicities. The smaller locus of proper pairs
whose **entire** cycle consists of translates has the Chow-polytope
criterion of [R-0074](../../results/chow_polytope_rigidity.md).
[R-0079](../../results/quartic_chow_pencil_classification.md) gives its
geometric pencils in \((4,4)\) **in characteristic zero**.
The characteristic-two single-support example is a separate
construction, not a positive-characteristic classification.
Its incidence scheme structure and
higher-degree repeated-cycle lifts require further work.

For a fixed translate, the [common-quadric boundary](../../arguments/equations/common_quadric_chow_boundary.md)
describes the full special scheme when ambient cofactors are coprime and
first cancellation is nonzero on its containing quadric. With nonzero
cofactor restrictions of gcd class \((h_1,h_2)\), its exact normal image
is known and its kernel has dimension \((h_1+2)h_2\). For \(h_2=0\),
the resultant ideal is the squared center ideal and the graph is the
ordinary blowup; these centers are outside the closure of fixed-degree
sole-support pairs. For \(h_2>0\), the squared-ideal model fails and
the graph and deeper cancellation remain open. The special-cycle
exclusion from the exact Chow-polytope fibre does not exclude the closure
of varying translate arrangements or determine moving transverse quotients.
