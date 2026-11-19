# Open carrier, projection, and conductor cases

## Boundary-valuation generalization

The [fixed-sextic all-degree theorem](../../results/ci_fixed_sextic_jet_rigidity.md) proves a positive residual-degree bound on one explicit integral sextic by working on an affine chart of its normalization. The open question is **not** to repeat its degree-by-degree jet calculations on more specimens. It is to identify a geometrically defined class of carriers for which the [conditional boundary criterion](../../results/ci_fixed_sextic_jet_rigidity.md#conditional-interface-for-other-carriers) can be checked uniformly: (i) a globally principal marked preimage and actual factorization \(g=Q^nP\), (ii) boundary valuations with controlled degree-dependent poles, and (iii) no nonzero regular \(P\) with strictly positive order at all selected boundaries. The generic intersection multiplicity and residual-degree inequality must then be established separately.

**Decision gate:** first determine whether a proposed carrier class satisfies these hypotheses, or identify a structural counterexample. Only then pursue mate-degree computations. This is a proposed investigation, not an assertion that the split-sextic, ADE, quintic, or elliptic cases satisfy the criterion. Keep conductor descent and full inverse support as independent requirements.

## Split sextic carriers

Fix \(C_0\) over an algebraically closed field of characteristic zero.
Consider an integral sextic of exact normal order two whose first exceptional
divisor is the reduced sum of two distinct integral, content-free sections
with no vertical component. A hypothetical sole-support mate must pass the
[split numerical and first-normal reductions](../../arguments/carriers/split_sextic_conductor_and_contact.md#p-041-torsion-corrected-sharpening-of-the-surviving-split-sextics).
Keep the \([4]\) and \([2,2]\) strata separate.
The [fixed ramified first-normal specimen](../../arguments/residuals/quasiprimitive_residual_cycles.md#proved-the-fixed-p-041-boundary-normal-form-has-no-stci-carrier)
has an all-mate exclusion from higher jets. In the \(d=1,[2,2]\) family
with both residual ruling roots totally ramified and the two low evaluation
zeros at their preimages, the [full higher-jet reduction](../../arguments/carriers/split_sextic_two_ramified_roots.md#result-and-scope)
leaves a necessary one-parameter line. The remaining [normalization and conductor comparison](../../arguments/carriers/split_sextic_two_ramified_roots.md#surviving-line-and-continuation-requirements)
requires numerical branch intersections, including exceptional parameter values. Integrality, mate
descent and sole support still require separate checks. The
[nonramified charts for partition 4](../../arguments/residuals/quasiprimitive_residual_cycles.md#2026-10-05-split4-nonramified)
and [a further chart for partition 2,2](../../arguments/residuals/quasiprimitive_residual_cycles.md#an-additional-22-chart-for-continuation)
retain their own higher-order lifting and conductor tests.

## Higher contact in the ADE (6,6) triple orbits

Use the [complete triple classification and actual sextic spaces](../../arguments/carriers/sextic_ade_reduction.md#three-remaining-primitive-triple-orbits),
retaining all 27 dimensions, including the seven directions beyond
quartic-source multiples. Proper cubic-contact pencils exist for all
three triples. Their source dimensions and first determinant images now
have an [intrinsic proof](../../arguments/carriers/sextic_triple_intrinsic_contact.md),
including the source dimensions in every degree at least four and full
determinant images for \(a,b\ge5\) with \(a+b\ge11\). These statements
do not impose the later contact equations. The [uniform fourth-coefficient
test](../../arguments/carriers/sextic_ade_reduction.md#sharp-length-five-for-pencils-with-a-quadric-divisible-member)
gives a sharp length bound of five for proper pencils with a first-order
member and dependent quadric restrictions. Continue the length-nine test
on pencils with independent quadric restrictions. For a proper pair,
length nine exhausts degree 36. The triple reduction uses the general-pencil
ADE hypothesis. The [singularity and cover comparison](#compatibility-of-the-normal-sextic-cyclic-cover)
applies to the general normal carrier.

<a id="the-remaining-toric-quintic-m-locus"></a>

## Non-toric, non-Gorenstein quintic normalizations

The [toric center proof](../../arguments/carriers/quintic_toric_center_incidence.md)
excludes all toric normalizations of quintic carriers for the fixed quartic
in characteristic zero. The case of non-toric, non-Gorenstein
normalizations remains open.

## Full inverse support in the elliptic construction

Use the
[five-parameter quadratic sections](../../arguments/carriers/elliptic_double_inverse_construction.md).
On every smooth basepoint-free fiber, a Cartier zero scheme of length twelve
on the residual divisor tests full inverse support. All of it must lie
set-theoretically on the marked elliptic curve. Equivalently the augmented
matrix in the [support criterion](../../arguments/carriers/elliptic_double_inverse_construction.md#a-length-twelve-scheme-testing-every-basepoint-free-fiber)
must have rank 613. The original member has all twelve units of length off
the elliptic curve.

On the characteristic-zero line with \(\mu=2\) and
\(\rho_0=\rho_1=\rho_3=0\), meeting the marked elliptic curve restricts
the length-twelve scheme to six geometric parameter values. Each is
basepoint-free and has an extra inverse point, which excludes every mate
degree on this line. The remaining question is whether a smooth
basepoint-free birational fiber elsewhere in the family passes the support
test and has a pure power descending to an actual homogeneous equation.
[Equation-search investigation](../../investigations/stci-equation-search/index.md#findings).

## Compatibility of the normal sextic cyclic cover

Start with a hypothetical characteristic-zero sextic pair having sole reduced
support C0. The [selected sextic checkpoint](../../arguments/carriers/sextic_pair_reduction.md) already
constructs the normal order-three cover and computes its necessary invariants,
including \(K_Y^2=72\) and profile-dependent Euler characteristic and lower
irregularity bounds. An additional compatibility remains to be established with the index-nine local classes, polarization and
three defect profiles, or construct such data. Under the additional general-pencil
ADE hypothesis, use the [three surviving primitive-triple orbits](../../arguments/carriers/sextic_ade_reduction.md#sextic-pairs-with-an-ade-pencil-carrier)
and the [remaining higher-contact locus](#higher-contact-in-the-ade-66-triple-orbits).
Distinguish the normal covering surface from a resolution when applying
smooth-surface inequalities. No contradictory upper bound is currently
proved.
