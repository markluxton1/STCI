# Projection, liaison, and actual supported ideals

## An actual homogeneous ACM thickening downstairs

This target is weaker than arithmetically Gorenstein (AG): a height-two homogeneous Gorenstein ideal in a polynomial ring is a complete intersection. Generic Cohen–Macaulay type two is allowed at the ACM stage, but cannot be treated as an AG or two-generator certificate. An actual ideal or finite-projection source requires a computation of the
image's section module: ACMness does not transfer from the covering quadric. The existing [section-defect theorem](../../arguments/linkage/projected_thickening_section_defects.md)
and [liaison constructions](../../arguments/linkage/supported_linkage_operations.md) specify
what the covered sources accomplish and where they fail.
[Deformation through full torus limits](../torus-supported-boundaries/index.md) gives a second way to organize this objective;
allow more than two generators and do not require the invariant special
fiber itself to be ACM. A projection source must avoid the already
excluded missing-section mechanism.

## Embedded conductor and ambient equations

For a hypothetical characteristic-zero sole-support pair of degrees
\(5\le a\le b\), let \(\delta\) be the length of its finite quadratic
conductor boundary and put \(q=\lceil a/2\rceil-1\). The [ambient-norm conductor theorem](../../arguments/linkage/quadratic_covers_and_conductor_descent.md#81-ambient-quadratic-norms-force-conductor-postulation) gives no boundary equation below degree q and
\[
\delta\ge a+b-3+2\left[\binom{q+2}{3}-q\right].
\]
The [endpoint lattice bounds](../../arguments/linkage/quadratic_covers_and_conductor_descent.md#82-endpoint-capacity-and-fixed-cover-carrier-exclusions)
give upper bounds on this same \(\delta\), including an incompatible bound
on specified nonempty actual carrier families in every degree at least five.
No incompatible bound covering arbitrary supported pairs is known. The
constructive question is which actual embedded boundary schemes and
multiplication maps realize the required postulation.
The norm strengthens the use of the existing canonical sequence; its Rao
dimensions are not a second independent budget. The broader degree-d theorem
and the distinct [extremal line argument](../../arguments/linkage/quadratic_covers_and_conductor_descent.md#12-embedded-curve-exclusion-of-the-minimal-boundary)
remain useful outside this particular norm application. Finite-order punctual
MCM lifts do not produce homogeneous ideal columns, and section completion
does not repair the original embedding. An embedded AG conjugate union would
descend automatically. The [supported-linkage constructions](../../arguments/linkage/supported_linkage_operations.md)
produce actual ACM schemes upstairs, while their specified failures leave other
sources and chains open.

The [auxiliary-cover choice](../../arguments/linkage/quadratic_cover_choice.md)
removes splitting as a restriction on applying the stronger nonsplit onset
to an integral carrier: in characteristic different from two, each carrier of degree
greater than two is nonsplit for a general cover in \(r+\lambda q\).
In the characteristic-zero application here, the two reduced lifts and
branch endpoints persist, and both the conormal-moment and uniform
all-minors bounds apply to the same chosen-cover conductor. The latter
gives \(\delta_\lambda\le2\max_k(4S_k-2k)\le2n(n-1)\), where
\(n=ab/4\) and \(S_k\) is the sum of the \(k\) largest annihilator
levels minus the sum of the \(k\) smallest. Those levels depend on the
actual generic algebra, not on the cover.

The [transverse-endpoint control](../../arguments/linkage/endpoint_lattice_capacity.md#transverse-endpoints-throughout-the-cover-pencil)
settles one part of the proposed capacity test. If a pair member is smooth
at an endpoint and its normal covector is independent of the cover's
endpoint covector, that endpoint has capacity \(n(n-1)\) for every
allowed cover. Even one such endpoint exceeds the displayed nonsplit
scalar lower bound, so this comparison cannot exclude that stratum.
It must instead examine sources where both endpoints are aligned smooth
or singular. Their actual equations must control both capacities in the
same cover; favorable divisibilities do not follow merely from unchanged
reduced lifts. This limits the current scalar comparison, not stronger
postulation information or the existence of supported pairs.

The [simultaneous toric-limit comparison](../../arguments/linkage/toric_limit_conductor_comparison.md)
opens a different endpoint question. For the full curve and selected quadratic
graph, \(\delta_i^{\mathrm{pure}}=\delta_i+\alpha_i-\beta_i\), with
\(\alpha_i,\beta_i\) their embedded special-fiber lengths. This recovers the
compatible finite-free specialization inequality when \(\alpha_i=0\), but
general full limits allow either correction sign. Toric concentration can
retain interior information at the ends; extracting an original-conductor
bound requires control of the graph correction and the actual global equations.
The pure special fiber need not be a CI. The scalar transverse limitation above
does not settle this corrected comparison.

For the original fixed cover, the
[carrier framework](../carrier-normalization/index.md#quadratic-cover-exclusions-and-the-remaining-one-lift-sector)
records the all-mate two-lift sextic exclusion and the remaining one-lift
non-Du-Val sector. **In the one-lift case \(Q|_C\ne0\)**, the conductor
scheme is \((P,Q,G)\), while conjugate attachment is \((P,zQ,G)\).
The two-lift branch instead requires its full primary extraction; the
general attachment formula is \(I_{W\cap W',W}=z\mathfrak c\).
The extra endpoint length in attachment must not be used as conductor
capacity. These fixed-cover closures and the
general cover-choice statement are distinct inputs to the comparison.

For an actual equivariant quadratic extension, the
[character-refined norm](../../arguments/linkage/projected_thickening_section_defects.md#equivariant-quadratic-descent-and-the-conductor-norm)
places each forced ambient equation in a specified weight space. This is
the grading of the existing norm mechanism, not an additional scalar
length bound. An invariant supported CI for the fixed quartic is already
excluded in characteristic zero; applying the refinement to a boundary
that has lost CI structure requires its own postulation hypotheses.
The explicit projected-source Rao classes and the separated CI conductor
are different quotients, despite their shared torus action.
