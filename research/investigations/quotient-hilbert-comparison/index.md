---
id: STCI-I-0002
type: investigation
title: Specialization between moving transverse quotients and full Hilbert limits
status: active
scope: "#scope"
question: "#question"
findings: "#findings"
relations:
  - kind: motivates
    from: [STCI-F-0001, STCI-F-0002]
    to: [STCI-I-0002]
    at: "#purpose"
  - kind: uses
    from: [STCI-R-0037, STCI-R-0039, STCI-R-0051, STCI-R-0052, STCI-R-0053, STCI-R-0070, STCI-R-0072, STCI-R-0073]
    to: [STCI-I-0002]
    at: "#inputs"
---
# Specialization between moving transverse quotients and full Hilbert limits

## Scope

Fix \(C_0\), its integer-weight torus, a degree type \((a,b)\), and a
declared bounded supported family if one is being tested. A sole-supported
proper pair would have generic transverse length \(m=ab/4\). The general
comparison permits a moving embedded quotient and noncurvilinear algebras.
It is not restricted to a constant quotient or its abstract isomorphism class.
Any concrete calculation must state its characteristic, polynomial, family,
power bound, and finite cutoff where one is used.

## Question

Starting from one actual moving embedded family, which transverse algebra,
endpoint image-lattice, and actual homogeneous equation-module data specialize
to its two full torus limits? Which section-hull profiles and parity classes
can arise through the canonical relative-image and cohomological
specialization maps of the same two equations? Can these constraints decide
generator incidence on a declared opposite-limit intersection, beyond the
individual Hilbert-polynomial and endpoint-length budgets?

## Purpose

[F-0001](../../frameworks/torus-supported-boundaries/index.md) organizes full
supported limits and moving equations.
[F-0002](../../frameworks/embedded-torus-quotients/index.md) retains embedded
quotients and projective contraction. Their relative-image and
[actual-family cohomological maps](../../arguments/normal-geometry/source_specialization_and_linkage.md)
are now inputs, rather than an unspecified missing bridge. This joint
investigation asks which actual homogeneous source data can induce the
required pure section hull and full endpoint correction simultaneously.

## Inputs

[R-0073](../../results/endpoint_equation_torsion.md) compares the raw
equation presentation with its two completed endpoint presentations in
each single degeneration. Its first-layer bound applies to proper pairs
with residual curves as well as to a hypothetical defining pair.

For characteristic-zero candidates, [R-0072](../../results/torus_quotient_movement_bounds.md)
supplies the rank and splitting bounds on the entire moving quotient used
in the [findings](#findings).

The [section-cohomology comparison](../../arguments/torus/boundary_section_cohomology.md)
computes the pure image's \(H^1\) from one two-lattice interpolation map
and imposes the whole splitting-profile inequality for CI origin. The
[sign-symmetrized source theorem](../../results/sign_symmetrized_source_defect.md)
computes the invariant union's section defect from the actual source
\(J+\tau J\), with its equivariant sign twist. Its
[one-equation norm reduction](../../arguments/torus/sign_symmetry_and_actual_sources.md#1-one-sign-eigen-equation-is-sufficient)
also restricts the actual minimal-degree source space. The union defect
is not automatically the pure torus limit's defect.

[R-0037](../../results/supported_hilbert_full_limits.md) preserves the whole
supported Hilbert object; [R-0039](../../results/moving_ideal_generator_criterion.md)
tests its actual generators. The constant-quotient construction,
[R-0051](../../results/constant_embedded_orbit_image.md), endpoint formula
[R-0052](../../results/orbit_image_endpoint_polynomial.md), and source test
[R-0053](../../results/constant_quotient_equation_criterion.md) give controlled
comparisons, not coverage of every moving family.

The broader [entire finite-modification argument](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification)
has its own scoped review. Starting with a proper homogeneous pair of
degrees \((a,b)\) with sole reduced support \(C_0\), it takes the full
closure of the torus restriction. It gives a rank-\(m\) quotient bundle
\(\mathcal B\), with \(m=ab/4\), degree \(e\ge0\), and endpoint defects
satisfying
\[
\delta_0+\delta_\infty=e+m(2a+2b-7).
\]
Its [strict-movement proof](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#positive-movement-and-the-global-presentation-barrier)
requires characteristic zero or characteristic \(p>0\) with \(p\nmid ab\).
For \((6,6)\), the rank is nine and \(\delta_0+\delta_\infty=e+153\),
with \(e>0\) in that range. A constant quotient has \(e=0\). Conversely,
if \(e=0\), global generation makes \(\mathcal B\) trivial and its
multiplication and coordinate sections constant. Movement refers to variation
of the embedded quotient and allows the abstract algebra to stay isomorphic.
The finite-modification theorem has a separate proof and review from the
constant-quotient Results.

## Method

Retain the entire scheme-theoretic closure of the torus restriction and both
endpoint image algebras, including torsion removal and saturation. Compute the
full ideal limits of the same moving scheme in both directions. Use the
[relative image sequence](../../arguments/torus_hilbert_boundary.md#endpoint-fibers-in-the-two-intrinsic-limits)
on the chart whose parameter is multiplied by the degeneration parameter.
Comparing full algebras and equation modules requires the corresponding
maps at the opposite endpoint.

The geometric points \(p_0,p_\infty\) on an orbit closure and the two limits
\(t\to0,\infty\) in a Hilbert scheme play different roles. The displayed
endpoint budget is neither their difference nor a formula determining a full
limit ideal. Constant total defect does not identify the algebras or guarantee
flatness of a relative image lattice.

An explicit residual family can test the proposed maps first. Label it as a
control outside the supported incidence whenever residual curves remain.
Positive-characteristic collisions can test characteristic dependence, but do
not supply a characteristic-zero supported deformation.

## Impact of the residual and full-limit comparison

The [invariant residual analysis](../../arguments/torus_hilbert_boundary.md#invariant-residual-supports-and-absorption-limits)
rules out the simplifying assumption that every invariant
residual component meets the marked curve directly: a
disjoint \(L_{12}\) can be connected through other residual
curves in an actual proper intersection. This is a
**control outside the sole-supported family**, not a new
candidate quotient in the present Investigation.

The [four-generator full-limit control](../../arguments/torus_hilbert_boundary.md#a-four-generator-full-limit-with-an-embedded-point)
shows that a flat full ideal can acquire embedded punctual
structure while its pure hull has a different Hilbert
polynomial. It reinforces the existing requirement to
compare **the same moving embedded family**, including
its equation modules and both endpoint images. A cycle-level absorption
argument does not determine those maps or their images. A decisive outcome
can be a compatibility obstruction or a realization on one declared family;
classifying all invariant residual arrangements is not required.

## Findings

The [actual-equation movement theorem](../../results/torus_quotient_movement_bounds.md)
gives necessary compatibility bounds on the ranks and splitting degrees of
the moving quotient. Its [paired inequality](../../results/torus_quotient_movement_bounds.md#consequence-for-opposite-full-limits)
uses the common embedded quotient of the two endpoint fibers and the
matched embedded lengths. At a general point \(x\), the larger equation degree \(b\) gives the lower bound \(\lceil(4b-7)/7\rceil\) on the rank of the
linear map \(K_x\to B_x\) induced by a single base tangent vector. That rank
can exceed the dimension of the classifying image, which is a curve.
Its fixed-involution refinement also bounds the common quotient at
\(r,-r\) by \(m-\lceil(4b-7)/7\rceil\) for general \(r\), so the
embedded family cannot factor through \(r\mapsto r^2\).
Specialization to the two endpoint fibers can lower the secant rank. These conclusions
need neither an endpoint classification nor a specified type of transverse
algebra. The missing step for a family passing the bounds is the comparison
with its full projective equation module and two-generator incidence.

[R-0070](../../results/intrinsic_limits_endpoint_fibers.md) now compares each
full intrinsic limit with the constant image of the corresponding embedded
endpoint fiber of the moving family. It determines the pure quotient and
the embedded lengths individually. On the matched endpoint chart the
embedded module is the parameter-annihilated part of a relative image
cokernel, giving an exact image-base-change criterion.

For a characteristic-zero sole-support \((6,6)\) CI, each endpoint fiber
must have total constant-image defect at least \(153\). The
[weighted-basis and sextic-source proof](../../arguments/torus_hilbert_boundary.md#necessary-endpoint-conditions-for-a-sextic-pair)
excludes fibers with fourth power of the maximal ideal zero. For
curvilinear fibers it imposes high affine-line contact in the transverse
frames and excludes exact order-eight contact in a frame whose slow
coordinate is a parameter unless the direction is the containing
quadric. The latter exclusion uses the actual dimension of the
degree-six source, beyond the defect inequality.

The cohomology profile adds an independent restriction: the diagonal
length-nine algebra \(u=v=1+\epsilon\), \(\epsilon^9=0\), cannot be
either endpoint fiber, even after the endpoint correction of length 63
repairs its polynomial. More generally the
[diagonal exclusion](../../arguments/torus/boundary_section_cohomology.md#3-diagonal-endpoint-algebras-can-fail-despite-finite-correction)
applies when \(n=ab/4\le a+b-3\), including the length-ten diagonal
algebra for \((5,8)\), whose required correction would be 80. The
two-lattice map and full section-hull profile can test other surviving
embedded algebras; total endpoint length alone cannot do so.
The cohomology exclusion itself is characteristic free. The complete
diagonal splitting calculation also shows that all twist inequalities
pass when \(n\ge a+b-2\); more twists of that model give no further test.

For each pure hull \(Y\), distinguish its vertex section defect
\(D=\bigoplus_d H^1(I_Y(d))\) from the projective endpoint correction
\(T=I_Y/I_L\). There is a canonical surjection
\(H^1(I_L(d))\twoheadrightarrow D_d\), and the actual flat family
supplies cohomological specialization sources for the former. The
nonstandard-sign head class in \(D\) is automatic for every sole-support
constant image in characteristic zero, without any CI-origin assumption.
It is not an additional endpoint filter. Restrictions must concern the
actual source inducing that class and its extended multiplication; contact separately
requires the finite conormal map into \(T(-2)\) to vanish. The remaining
question concerns their simultaneous images and actual equation sources.

The full algebra at the opposite endpoint of a limit, its additional
generators, and the incidence of compatible moving equations remain
unresolved. Transverse one-parameter subgroups move the marked support
off the coordinate torus. Their
[length-two sextic control](../../arguments/torus_sextic_residuals.md#a-transverse-limit-with-generic-length-two)
has a full CI limit on coordinate lines and residual degree \(28\)
before specialization.

The provisional [moving neighborhood/conormal comparison](../../arguments/torus/transverse_neighborhood_motion_and_conormal.md) identifies the derivative of the embedded quotient with the longitudinal conormal component; the exterior square can lose this motion. Its extension to the two weighted endpoint cotangent lattices does not identify the separated closure's conormal with the pulled-back projective equation bundle. The [plane-family criterion](../../arguments/torus/plane_pencil_equation_bundles.md) gives a separate full fixed-type plane-CI completion and generator-triviality test; this is not a construction of the required opposite full Hilbert limits. The sole-support hypotheses of R-0072 are unchanged.

## Completion and next decisions

For a fully specified embedded moving family, the kernels of homogeneous
restriction to the schematically dense torus recover the saturated ideal
of its pure projective image. Over an infinite field, once that ideal
\(J\) has the whole CI polynomial \(P_{a,b}\), it suffices to check
\(J_a\ne0\) and that the degree-\(b\) forms have no common irreducible
factor. The open question is what restrictions two global generators impose
on a *family* passing the movement, involutive-secant, pure-cohomology
and full endpoint-contact conditions, while inducing the required actual
section-algebra presentation.
[Proper-pencil criterion](../../arguments/torus_hilbert_boundary.md#complete-intersection-polynomial-and-a-proper-pencil).

One bounded alternative is to construct or exclude an actual
full-translated-cycle CI boundary with nonzero pure section defect \(D\),
including moment-zero cases. The known exceptional quartic limits have
ACM pure hulls, while the \((16,16)\) equation-layer control has a CI pure
hull, despite their nonzero \(T\). Noninvariance of actual CIs and the
appearance of endpoint corrections are already realized; the proposed
test concerns section-hull data and its compatible source. It sits beside
the interpolation and actual-family source problems, without claiming
priority over a carrier-based section lift or modulus-compatible relation.

### What the presentation theorems already give

Given a regular sequence \(F,G\) in \(S=k[x_0,x_1,x_2,x_3]\), the ideal
\(J=(F,G)\) is of linear type. Its symmetric and Rees algebras both have
the presentation \(S[T_1,T_2]/(GT_1-FT_2)\) with \(T_1,T_2\) mapping to
\(Ft,Gt\) in the Rees algebra. For a supplied generating sequence in a
Noetherian ring, the cycle approximation complex has zeroth homology
\(\operatorname{Sym}_S(J)\). Vanishing of the first homology of the
homology approximation complex \(\mathcal M\) implies linear type. These
statements take the generators and their relations as input. They do not
recover two homogeneous generators of prescribed degrees from the moving
quotient or its two endpoint images. This is where the projective
equation-module comparison is still needed.
[Micali, Chapter I, Theorem 1 and Lemma 2](https://www.numdam.org/item/10.5802/aif.173.pdf#page=10) ·
[Busé–Jouanolou, §4.1](https://arxiv.org/pdf/math/0210096#page=25) and [Proposition 4.5](https://arxiv.org/pdf/math/0210096#page=28) ·
[Existing graph-blowup application](../../arguments/equations/global_equations_and_constructions.md#the-complement-morphism-and-its-graph-blowup).

## Relation-persistence control and remaining bridge

The degree-12 decision for the positive degeneration of the rational
residual pencils is settled by \(W_0\). Its first layer contains two
independent classes whose images vanish even at both endpoints together.
They are the degree-12 part of a graded submodule whose sheaf is \(\mathcal O_{L_{12}}(-11)\) on the line disjoint
from the marked quartic. The [identities and localization proof](../../results/endpoint_equation_torsion.md#a-relation-missed-at-both-endpoints)
give the witnesses for the specified map before parameter saturation.

In every bidegree, both completed endpoints detect unfiltered parameter
torsion degree by degree. The common kernel on a layer consists exactly
of the classes killed by powers of \((x_0,x_3)\). The [residual degree
bound](../../results/endpoint_equation_torsion.md#statement) describes
the cost of first-layer detection when the stripped extreme forms both
contain that line. The Smith exponents counted source classes. The explicit witnesses
exhibit classes that become locally divisible by the parameter.

The broader realization question remains active. For a proposed supported
family whose stripped extreme forms meet with multiplicity \(e_L>0\) on
the line, its global first equation layer must supply precisely that
generic length in the joint kernel. An independent upper bound below
\(e_L\) on the same presentation would force a residual curve. A family
passing this comparison still needs its full moving ideal and two
homogeneous generators. The local comparison alone gives neither an
upper bound on that kernel for all pairs nor a supported family to test.


## Canonical equation sources and delayed hidden layers

The [Chow-matched equation-layer comparison](../../arguments/torus/chow_matched_equation_layers.md) now identifies canonical end-adapted raw ideals and proves an exact shift of all line-supported layers for unequal generator degrees. A same-ideal shear changes the first missed length from eight to zero by moving it to the next layer; it does not remove cancellation. Opposite optimal representatives need not coincide, so compare both filtrations of the same homogeneous equation source, not one supposedly simultaneously optimized pair.

The [global Cech/Kummer comparison](../../arguments/torus/chow_matched_equation_layers.md#the-global-cech-kernel-and-the-scope-of-kummer-comparisons) separates endpoint conductor data from the extension condition on raw equation relations. The [full-limit control](../../arguments/torus/chow_matched_equation_layers.md#opposite-full-limits-can-retain-a-large-embedded-hilbert-correction) retains the CI polynomial by an embedded endpoint correction of length 4608 at either orientation. The live gate is an independent bound or compatibility condition on the **canonical** filtered sources/layers, not a new calculation of first length for an arbitrary generating pair. No such strict bound or unrestricted exclusion is proved here.
