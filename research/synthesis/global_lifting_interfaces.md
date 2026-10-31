# Actual equation spaces and compatible lifts

The existence problem asks for two homogeneous equations, with proper
intersection and sole reduced support on the fixed embedded curve. Several
useful models first prescribe lower normal data or a section upstairs. The
remaining question is then an image, compatibility, or descent problem. This
note states one elementary lifting lemma and distinguishes its applications
from comparisons that have no proved connecting map.

## A fixed-symbol lifting lemma

Let \(V,S,T\) be finite-dimensional vector spaces over a field, let
\(\sigma:V\to S\) and \(\tau:V\to T\) be linear, and fix a subspace
\(A\subset T\). For \(s\in\operatorname{im}\sigma\), choose any
\(v\in V\) with \(\sigma(v)=s\). Then
\[
\operatorname{ob}(s)=[\tau(v)]\in T/(A+\tau(\ker\sigma))
\]
is well-defined and vanishes if and only if some \(v'\in V\) satisfies
\(\sigma(v')=s\) and \(\tau(v')\in A\). When nonempty, the set of such
lifts is an affine space under \(\ker\sigma\cap\tau^{-1}(A)\).

**Proof.** All lifts of \(s\) are \(v+K\), where \(K=\ker\sigma\).
Their \(\tau\)-values are \(\tau(v)+\tau(K)\). This affine space meets
\(A\) exactly when \(\tau(v)\in A+\tau(K)\). Replacing \(v\) by another
lift does not change the quotient class. The difference of any two successful
lifts belongs to \(K\cap\tau^{-1}(A)\), and adding any member of that
subspace preserves success. \(\square\)

The lemma is about a **fixed** linear source and a **fixed** permissible
correction subspace. If the root, embedding, or correction subspace varies,
one must impose the corresponding incidence and handle rank changes; this
lemma supplies neither flatness nor a uniform quotient bundle automatically.
It also supplies no properness or residual-support test for a pair of forms.

A failed chosen lift gives an obstruction only modulo \(A\). To exclude
**every** lift, one must work modulo \(A+\tau(K)\). A nonzero functional
on \(T/A\) is an all-lifts obstruction only when it annihilates
\(\tau(K)\) as well. This distinction can produce constructions by finding
a correction, or exclusions by proving the larger quotient class nonzero.

## The sextic illustration

In the conditional moving-quadratic-root calculation, the actual degree-six,
normal-order-two source has dimension 23 and its symbol map has rank 22.
The kernel is \(kq^3\). At a fixed nonzero root \(f\), the permissible cubic
corrections form the rank-16 image of multiplication by \(f\) in the
40-dimensional cubic-jet space. The correct varying-lift obstruction therefore
is the affine-target class
\[
[F_{c,3}-\alpha G_0]\in T/(\operatorname{im}\mu_f+k\tau(q^3)).
\]
Here \(\alpha G_0\) is the prescribed cubic target; subtracting it
turns the lifting equation into the linear membership test of the lemma.
Its dimension is 24 or 23 according as the extra direction is contained in the
multiplication image or not. These are the actual maps of the
[conditional sextic calculation](normalization_conductor_phase2_addendum.md),
not dimensions inferred from an abstract conormal bundle.

A nonzero fixed-lift pairing is insufficient unless it kills the \(q^3\)
direction. For the specified seed, that check is completed: the exact row
giving \(-384\) pairs with \((q^3)_3=(u+zv/2)^3\) as
\(3-2(3/2)=0\). It therefore excludes every lift of that fixed seed.
The separate exact free-orbit certificate also includes the free parameter
and excludes its specified chart. The remaining strata, actual mate,
and full support conditions stay separate. This general lemma packages an
existing correction; it is not a new exclusion theorem.

## A constructed source with a global correction obstruction

The [quadric elementary modification](quadric_modification_and_global_corrections.md)
supplies an actual rank-two bundle and the complete affine space of lifts of
a specified divisor section. For its nonzero first-cancellation branch, the
required next correction is \(4s^{11}t^{11}\). The image of every allowed
ambient correction is contained in
\[
s^{12}H^0(\mathcal O_{\mathbf P^1}(10))+
t^{12}H^0(\mathcal O_{\mathbf P^1}(10))
\subset H^0(\mathcal O_{\mathbf P^1}(22)).
\]
The middle monomial is absent from this subspace, so the quotient class is
nonzero in characteristic different from two. This is a concrete realization
of an obstruction in an actual source quotient. The complete proof separately
handles failed first cancellation and the zero-cancellation branch to obtain
positive residual degree throughout this source. The construction does not
exhaust all sextic pairs, or all sections of the bundle.

## How the realization problems differ

| Mathematical object already supplied | Remaining actual question | Current mathematical home |
| --- | --- | --- |
| A normal symbol or finite jet | Is it in the image of the prescribed-degree homogeneous source, with all allowable higher lifts? | [Actual equation spaces](../supplements/ACTUAL_EQUATION_SPACES.md), [normal filtrations](normal_filtration_boundary_obstructions.md) |
| An abstract lower multiple structure | Does the extension exist for this embedding, and do actual forms generate the required quotient? | [Infinitesimal geometry](03-infinitesimal-geometry.md), [marked deformation](marked_deformation_and_absorption.md) |
| A section/divisor on the normalized carrier | Does the section glue through the full conductor, including nilpotents and all inverse branches? | [Carrier descent](04-carriers.md), [conductor algebra](../supplements/CONDUCTOR_DESCENT_ALGEBRA.md) |
| Componentwise polarized elliptic covers | Do the chosen line-bundle identifications agree at the actual nodes and yield the prescribed projection? | [Elliptic gluing](projection_and_elliptic_gluing.md) |
| Affine equations at both ends | Do they define a single compatible homogeneous presentation of the chosen projective thickening? | [Global equations](global_equations_and_constructions.md), [contact and descent](contact_duality_and_global_descent.md) |
| A full local transverse algebra | Is the pair globally proper and does its degree exhaust the intersection cycle? | [Two surfaces](02-two-surfaces.md), [Chow and complement criteria](global_equations_and_constructions.md) |

These rows share a pattern of compatibility, but are different mathematical
problems. No theorem here identifies a conductor obstruction with a
normal-filtration defect, a node-gluing class, or an obstruction to lifting
coefficients. An asserted identification would need a map and a proof.

## What calculations measure

An exact matrix rank can measure the image of an actual global linear system;
it is useful only after its domain and specialization argument are established.
A determinant can measure the wedge of actual contact directions, or the Chow
cycle of a proper intersection; these are different determinants. A conductor
unit-power computation measures descent of a particular normalized section,
not existence of the carrier. An exceptional intersection matrix measures
numerical pullback or independent contracted curves; its entries are not
controlled by Cartier index alone.

The [quartic-pair proof](quartic_pair_obstruction.md) is a complete example of
calculation becoming geometry: the exact first-symbol fixed divisor determines
local surface equations, direct blowups produce independent exceptional
classes, and the global Hodge/Noether bound gives a contradiction. The
[numerical pullback lemma](numerical_surface_pullback.md) explains a different
matrix: integral ideal vanishing versus rational numerical orthogonality.
The shared use of exceptional curves does not make these the same obstruction.

## Review status

The elementary fixed-symbol lemma, its fixed-data restrictions, the actual
sextic source/kernel application and the seed witness annihilation were
independently reconstructed and accepted in this consolidation (GPT-6.1 Sol,
high effort). The vector-space lemma is characteristic-free; the stated sextic
computation uses its characteristic-zero coefficients and hypotheses. Applications use the hypotheses
and evidence of their linked owners. The compatibility comparisons are an
organizational synthesis, not additional theorem dependencies or a resolution
of the characteristic-zero STCI problem.
