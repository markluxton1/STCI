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

## Universal translate incidence (recovered geometric interface)

Let \(T\subset\operatorname{PGL}_4\) be the diagonal torus, \(H=T_C\), and \(B=T/H\cong(\mathbf G_m)^2\). The dense coordinate torus \(T_X\subset\mathbf P^3\) is an \(H\)-torsor over \(B\), in fact split as a torus (choose a splitting of the character-lattice sequence). Its fibers are the dense parts of the translates \(C_\beta\). This uses the genuine quotient torus; the auxiliary normalization \([s^4:us^3t:vst^3:t^4]\) has a residual \(\mu_4\) identification, including a nonreduced group scheme in characteristic two.

For fixed degrees \(a,b\), let \(W_d=H^0(\mathbf P^3,\mathcal O(d))\) and \(S_{a,b}=\mathbf P(W_a)\times\mathbf P(W_b)\). The universal dense-torus incidence
\[
\mathscr I_{a,b}=\{([F],[G],x)\in S_{a,b}\times T_X:F(x)=G(x)=0\}
\]
projects to \(S_{a,b}\times B\) via the torus quotient. For a proper intersection, a curve component meeting \(T_X\) is *vertical* precisely when it is a full translate \(C_\beta\); otherwise its image is a curve (generically finite over its image). This distinction concerns the **image dimension**, not the dimension of the original intersection fiber. Coordinate-boundary components remain invisible here.

The incidence of *entire translates* is a relative projective-bundle construction. The restriction maps \(W_d\otimes\mathcal O_B\to\mathcal E_d\), where \(\mathcal E_d\) has fiber \(H^0(C_\beta,\mathcal O_{C_\beta}(d))\), have constant rank because the translates are projectively equivalent. Their kernels \(\mathcal K_d\) are vector bundles, and
\[
\mathscr V_{a,b}=\mathbf P_B(\mathcal K_a)\times_B\mathbf P_B(\mathcal K_b)
\]
parametrizes surface pairs containing at least one entire translate, whenever the projective bundles are nonempty. This follows from the standard relative evaluation/constant-rank construction; it is not a new existence theorem. The harder locus is the subset of **proper pairs whose full intersection cycle** consists of translates, equivalently (by [R-0074](../../results/chow_polytope_rigidity.md)) whose Chow polytope is \(mP_C\), with \(ab=4m\). Its scheme structure, boundary, degenerations, and realizable configurations are not determined by the relative projective bundle alone.

This recovers the November 5 universal-incidence viewpoint as an interface to the existing constant-quotient and moving-quotient theories, without assuming that arbitrary pairs are eigenforms, that torus-fiber lengths equal intersection multiplicities, or that nonproper incidence projections satisfy proper semicontinuity statements.
