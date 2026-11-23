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

## Mathematical scope and interfaces

This approach studies **embedded finite torus quotient images**, their
projective endpoint contractions, contact geometry, and comparisons with
moving torus degenerations. The [complete quotient proof](../../arguments/torus_embedded_quotients.md)
and [endpoint image theorem](../../results/orbit_image_endpoint_polynomial.md)
give constant-image controls. The [intrinsic endpoint-fiber comparison](../../results/intrinsic_limits_endpoint_fibers.md)
determines pure parts and embedded lengths under its hypotheses, but does not
resolve the full moving-family comparison in the
[Investigation](../../investigations/quotient-hilbert-comparison/index.md).
The [supported-boundary approach](../torus-supported-boundaries/index.md)
provides complementary full-ideal and opposite-limit techniques; neither
approach excludes studying the other's degenerations. Contact, polarization,
and conductor constraints meet in [contact and global descent](contact_and_global_descent.md#the-approaches-and-their-exact-reach).

## Available results

[R-0072](../../results/torus_quotient_movement_bounds.md) bounds the
splitting degrees and the generic secant and tangent ranks of the entire
moving quotient of a characteristic-zero defining pair. Its endpoint
inequality compares the two kernels in the same transverse coordinates.
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
algebras and moving generator incidence remain open.

Use the relative image map in R-0070 when comparing an embedded quotient
and an intrinsic limit. Recovering the full special equation module
requires further data. Even the two completed endpoint presentations of
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
testing actual generators. It does not do so on the partial diagonals.
The invariant quartic collision examples give embedded quotient
controls; a general repeated cycle may instead lift to a non-invariant
ideal. Test one partial diagonal in actual pencils, and compare its
local finite quotients with both full flat limits while retaining the
equation source. A cycle or canonical endpoint index alone cannot
make that comparison.

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
criterion of [R-0074](../../results/chow_polytope_rigidity.md); its scheme
structure and non-invariant repeated-cycle lifts require further work.

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
