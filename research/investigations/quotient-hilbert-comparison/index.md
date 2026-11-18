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
    from: [STCI-R-0037, STCI-R-0039, STCI-R-0051, STCI-R-0052, STCI-R-0053, STCI-R-0070, STCI-R-0072]
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
to its two full torus limits? Can a proved comparison morphism or specialization
statement constrain generator incidence on an opposite-limit intersection?
In particular, can the paired endpoint profiles give a compatibility
restriction beyond the individual Hilbert-polynomial and defect budgets?

## Purpose

[F-0001](../../frameworks/torus-supported-boundaries/index.md) organizes full
supported limits and moving equations.
[F-0002](../../frameworks/embedded-torus-quotients/index.md) retains embedded
quotients and projective contraction. This joint investigation asks for the
missing mathematical bridge between those objects. It does not identify them
because they share a defect length or resemble one another geometrically.

## Inputs

For characteristic-zero candidates, [R-0072](../../results/torus_quotient_movement_bounds.md)
supplies the rank and splitting bounds on the entire moving quotient used
in the [findings](#findings).

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
its equation modules and both endpoint images. Neither
the residual orbit classification nor a cycle-level
absorption argument supplies the missing comparison map.

**Priority consequence:** retain this active bridge as a
prerequisite for interpreting proposed opposite-limit
generator strata, but do not expand its scope to classify
all invariant residual arrangements. A decisive outcome
remains an actual specialization statement or a concrete
compatibility obstruction for one declared family.

## Findings

The [actual-equation movement theorem](../../results/torus_quotient_movement_bounds.md)
gives necessary compatibility bounds on the ranks and splitting degrees of
the moving quotient. Its [paired inequality](../../results/torus_quotient_movement_bounds.md#consequence-for-opposite-full-limits)
uses the common embedded quotient of the two endpoint fibers and the
matched embedded lengths. At a general point \(x\), the larger equation degree \(b\) gives the lower bound \(\lceil(4b-7)/7\rceil\) on the rank of the
linear map \(K_x\to B_x\) induced by a single base tangent vector. That rank
can exceed the dimension of the classifying image, which is a curve.
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

The full algebra at the opposite endpoint of a limit, its additional
generators, and the incidence of compatible moving equations remain
unresolved. Transverse one-parameter subgroups move the marked support
off the coordinate torus. Their
[length-two sextic control](../../arguments/torus_sextic_residuals.md#a-transverse-limit-with-generic-length-two)
has a full CI limit on coordinate lines and residual degree \(28\)
before specialization.

## Completion and next decisions

For a fully specified embedded moving family, the kernels of homogeneous
restriction to the schematically dense torus recover the saturated ideal
of its pure projective image. Over an infinite field, once that ideal
\(J\) has the whole CI polynomial \(P_{a,b}\), it suffices to check
\(J_a\ne0\) and that the degree-\(b\) forms have no common irreducible
factor. The open question is what restrictions two global generators impose
on a *family* beyond its splitting, generic secant and tangent ranks,
Hilbert polynomial and endpoint image algebras.
[Proper-pencil criterion](../../arguments/torus_hilbert_boundary.md#complete-intersection-polynomial-and-a-proper-pencil).

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

Use the two proper residual sextic pencils \(W_\tau\), \(\tau=0,1\), over
\(\mathbf Q\) and the positive degeneration in the
[degree-12 Smith calculation](../../arguments/torus_hilbert_boundary.md#degree-12-relation-persistence-for-the-residual-sextic-pencil).
The pencils share their negative full torus limit. Their degree-12 multiplication
presentations on \(S/(g)\) have different parameter torsion even though the
two moving intersections both have polynomial \(36n-144\).

**Bounded decision.** Do the degree-12 torsion classes of these two
presentations remain detectable, with their filtration by the effective
parameter \(v\), in the family at \(p_\infty=[0:0:0:1]\)?
In the notation of the calculation, let
\(T_\tau=(\operatorname{coker}\mu_\tau)[v^\infty]\).
Dehomogenize at \(x_3=1\) and complete at \((v,x_0,x_1,x_2)\).
With \(I_\tau=(g,a_\tau+v q^3)\) in this local ring, the target torsion
module is \(T_\tau^{\rm loc}=(I_\tau:v^\infty)/I_\tau\).
Restriction of representatives gives a map \(T_\tau\to T_\tau^{\rm loc}\)
commuting with \(v\). Test injectivity on the two layers
\(v^{j-1}T_\tau/v^jT_\tau\to
v^{j-1}T_\tau^{\rm loc}/v^jT_\tau^{\rm loc}\), \(j=1,2\).
The known Smith profiles exhaust the **source** in these two layers.
Stop with a proof of injectivity on both layers for both pencils, or a
nonzero source class whose restriction dies on its layer. Either outcome
decides what this endpoint detects about this fixed presentation. The
completed family is taken before parameter saturation, with all components
through the endpoint retained. Applying the comparison to a sole-supported
family would require its own embedded
quotient, endpoint maps and actual moving equations.
