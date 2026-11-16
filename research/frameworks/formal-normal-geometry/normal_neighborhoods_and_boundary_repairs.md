# Normal neighborhoods and boundary repair mechanisms

[Formal normal Framework](index.md) · [Original section addresses](normal_filtration_boundaries.md)

## Geometric orientation: successive neighborhoods of the curve

The primary geometric object is an embedded multiple structure supported on
the fixed rational quartic \(C\), not a list of coefficients in normal
coordinates. Blowing up \(C\) in \(\mathbf P^3\) exposes the normal
directions on the exceptional ruled surface
\(E=\mathbf P(N_{C/\mathbf P^3})\). A surface's first nonzero normal
symbol cuts a divisor on \(E\); common components and special fibers
encode shared normal directions and concentration of contact. This is
the geometric setting for the normal-order and common-factor tests below.

Successive thickening layers ask a different question: whether a specified
embedded multiple curve extends by one more layer. The associated conormal
modules, multiplication maps and extension classes measure compatibility
of those successive neighborhoods. An endpoint divisor may allow a
cohomological obstruction class to be repaired, but this does not by
itself realize the repaired structure by homogeneous equations.

Finally, an actual pair of hypersurfaces imposes **global source
conditions** beyond either exceptional-divisor geometry or abstract
thickening theory. Its full filtered equation module can contain
relations invisible in its initial normal forms. These three levels
(geometric contact, embedded extension, and global equation realization)
organize the results that follow. Their comparison maps, where not
proved, remain research questions rather than implicit identifications.

For torus limits the same objects carry weight decompositions. These
weights can refine the possible normal layers and extension maps, but
the deformation back to a non-invariant complete intersection may use
nonzero-weight directions. Thus a fixed-point calculation is a
necessary boundary test, not a restriction to invariant generators.


## Three levels of the geometric obstruction problem

For a smooth curve C with ideal I and an actual two-equation regular-sequence ideal J=(F,G) contained in I:

1. **Normal structure:** normal layers, their torsion, saturation, and socle of a supported multiple curve.
2. **Initial equations:** the full I-initial ideal of J, including cancellation-generated initials, and the filtered actual equation module J/IJ.
3. **Global realization:** actual homogeneous forms, compatible jets, properness, common factors, and residual support.

These are not interchangeable. In particular, a punctual initial-ideal defect does not by itself prove residual support; a vertical exceptional cycle need not descend to a residual curve.


## Accepted anchors

- [R-0010](../../results/saturated_first_relation_normal_flatness.md): normal flatness under saturated first-relation and full generic binary-CI assumptions.
- [R-0016](../../results/nonsaturated_first_relation_resultant.md): nonsaturated resultant and defect budget under stated conditions.
- [R-0019](../../results/quasiprimitive_residual_cycles.md): conditional saturated residual-cycle and first-normal restrictions.
- [R-0030](../../results/local_filtration_comparison_defect.md): canonical local exact comparison between initial-equation generators and the filtered actual equation module. Under its smooth-carrier hypotheses the defect is supported at simultaneous carrier singularities along C.
- [R-0032](../../results/full_conormal_socle_budget.md): conormal and socle budget for actual supported complete intersections, with its degree-bound assumptions.
- [R-0033](../../results/constant_first_relation_lifting.md): lifting obstruction for particular constant-first-relation models, not all moving relations.

The [normal torsion and genus note](../../arguments/normal-geometry/curvilinear_genus_and_defects.md#normal-torsion-spectral-genus-budget) compares ordinary graded torsion and saturated-layer divisors in the generically curvilinear supported setting. They measure the same genus contribution and must not be counted twice. Further spectral claims in that note have the proof and review scopes stated there.


## Boundary-repair and one-step arguments

The [boundary-repair note](../../arguments/normal-geometry/normal_boundary_weighted_initials.md#normal-boundary-strata-weighted-initials-and-lifting) supplies a principal-parts test for an identified linear obstruction in H^1(C,V): the class dies under V to V(D) exactly when its image in H^1(C,V(D)) is zero. On P1 this admits a common-divisor multiplication-kernel test. Repair by an arbitrary divisor of a given degree does not imply a prescribed geometric repair or actual homogeneous realization.

The [one-step note](../../arguments/one_step_boundary_repair.md#2026-10-27-one-step-boundary-obstruction), with [independent audit](../../arguments/one_step_boundary_repair.md#2026-10-27-one-step-boundary-obstruction-audit), constructs an extension class for a fixed lower embedded Cohen-Macaulay thickening with generically curvilinear normal algebra. The existing power-relation divisor consumes part of the next permitted divisor; the remaining allowance, together with vanishing of the pushed-forward extension class and surjectivity, governs its specified one-step extension.

For the final Gorenstein step (generic length at least three), that note argues that no additional divisor allowance remains: the relevant extension class must vanish, and perfect top-layer multiplication is also required. **These claims retain their stated scopes.** They do not give a general ambient obstruction comparison, a global STCI exclusion, or a converse from splitting to two global equations.


## From exceptional normal divisors to the full filtered equation module

For a regular codimension-two embedding C in a smooth threefold, let I be its ideal and J=(F,G) a proper complete-intersection ideal contained in I. Set S=gr_I(O_X)=Sym(I/I²), H=in_I(J), and Q_n=H_n/(S_+ H)_n. The actual equation module J/IJ carries its induced I-filtration. The canonical comparison has an exact sequence

    0 -> Delta_n -> Q_n -> gr^n(J/IJ) -> 0,

where Delta_n=in_n(IJ)/(S_+ H)_n. In particular, minimal generators of the full initial ideal need not survive as independent generators of the filtered equation module. This is the comparison in [R-0030](../../results/local_filtration_comparison_defect.md), with its full construction and counterexample in [the ideal-filtration supplement](../../arguments/normal-geometry/ideal_filtrations_quartic_exclusion.md#2026-10-23-ideal-filtrations-independent-investigationmd).

The full initial ideal is itself not determined by the two displayed leading forms. In the regular transverse local ring, J=(x²,x²+y³)=(x²,y³), so the displayed order-two symbols generate only (X²), whereas the full initial ideal is (X²,Y³), of colength six. The [higher-initial investigation](../../arguments/normal-geometry/formal-normal-intersection.md#explicit-cancellation-examples) gives further local examples and the prescribed characteristic-two quartic computation. None of these local models by itself constructs a global STCI.

Simultaneous carrier singularity is necessary for the comparison defect under the R-0030 hypotheses. The characteristic-two quartic has a fourth initial equation from cancellation and its comparison defect vanishes. [R-0031](../../results/quartic_char2_fourth_equation_kernel.md) · [Open sole-support question](open_normal_geometry.md#punctual-relative-defect-under-sole-support)

A [finite-flat supported length-five control](../../results/supported_length_five_defect_specialization.md) has zero relative comparison defect but a nonzero defect on its actual closed transverse fiber. Its coefficient-specialized relative normal algebra has length eight while the actual closed algebra has length five. An exceptional-slice calculation needs a base-change argument to detect the punctual relative defect. Homogenizing the two equations gives an intersection cycle \(5[L]+2[D]\) with residual conic \(D\). The fixed-quartic sole-support question remains open.

Neither Delta_n nor cancellation is the saturated first-relation resultant defect of [R-0016](../../results/nonsaturated_first_relation_resultant.md), the quasiprimitive residual-cycle divisor of [R-0019](../../results/quasiprimitive_residual_cycles.md), or the rank shortfall of a global jet map. Identifying any two requires an additional comparison argument.


## Endpoint divisors as geometric repairs of extension classes

For a fixed obstruction \(o\in H^1(\mathbf P^1,\mathcal O(-r))\), \(r\ge2\), and an effective divisor of degree \(B\), write \(n=r-2\). Serre duality identifies the obstruction with a functional on \(H^0(\mathcal O(n))\). If the divisor is cut out by \(h\in H^0(\mathcal O(B))\), then the obstruction dies after twisting by that divisor precisely when
\[
\langle o,hq\rangle=0\quad\text{for all }q\in H^0(\mathcal O(n-B)).
\]
Thus allowing the divisor to vary asks for a nonzero kernel of a catalecticant multiplication map. A dimension argument supplies such a divisor for every scalar obstruction when \(B\ge\lfloor r/2\rfloor\); for a vector-valued obstruction the **same divisor** must lie in the kernels of all component maps. A prescribed socle boundary is still more restrictive.

This is a precise *cohomological* criterion, not a proof that the allowed socle divisor modifies the ambient embedded-lifting obstruction in this way. The missing comparison of obstruction complexes and the actual global homogeneous source are separate requirements. The detailed derivation and limits are in [the boundary supplement](../../arguments/normal-geometry/normal_boundary_weighted_initials.md#normal-boundary-strata-weighted-initials-and-lifting), with the fixed-lower embedded criterion in [the one-step supplement](../../arguments/one_step_boundary_repair.md#2026-10-27-one-step-boundary-obstruction).

