# Carrier descent and socle interfaces

**Status:** thematic navigation, not new theorem authority. Read [carrier geometry](04-carriers.md) for the normalization and conductor framework. The canonical records determine all hypotheses.

## Distinct obstruction mechanisms

The fixed-carrier [conductor criterion](../results/fixed_carrier_conductor_criterion.md) (R-0003) uses the complete inverse support and full conductor-unit descent, not only reduced double-locus data. The [Cartier singleton classification](../results/cartier_singleton_lift.md) (R-0002) gives necessary minimal-degree models, not actual projections or mates. For the fixed quartic, these are the two degree-eight quadric models and the degree-sixteen plane model. The [projection phase reduction](../results/projection_phase_reduction.md) (R-0004) describes the torsion-phase test in admissible families, but does not calculate their phase images.

A different approach uses local Cartier indices on a **normal integral carrier**. [R-0034](../results/normal_carrier_index_socle.md) compares the actual local Cartier index with top-socle defects and normal-layer torsion. Carrier multiplicity cannot replace actual Cartier index. [R-0035](../results/normal_carrier_bounded_index_exclusion.md) excludes normal carriers of the fixed characteristic-zero quartic with every actual on-curve local index at most four, under the inherited torsion-reduction and quadratic-direction hypotheses. It leaves higher indices and nonnormal or entirely-thick presentations outside its scope.

## An exact bridge, with restrictive hypotheses

[R-0036](../results/pointwise_conductor_socle_defect.md) gives an identity of **actual divisors** for an actual supported complete intersection when the carrier is generically regular along C, its normalization is smooth along a single smooth Cartier inverse curve c isomorphic to C, and the conductor is invertible with no c component. Writing A for the transverse differential zero divisor, B for the conductor divisor and D_n for the top socle defect, the result is:

    D_n = (n-1) A - B restricted to c.

This is not established for multiple branches, non-Cartier lifts, singular normalization along c, or a generically singular carrier. Its Jacobian argument also requires the relevant characteristic restriction. It is a real conductor-to-normal-filtration interface, but not a universal comparison of all defect theories.

## Decision gates for a candidate carrier

1. Check integrality, proper intersection and degree. In characteristic zero, [R-0001](../results/quartic_carrier_exclusion.md) already excludes integral quartic carriers.
2. Compute the **entire** reduced inverse support on the normalization, including extra branches or isolated points.
3. For a Cartier singleton lift, verify admissible four-section projection, finite birationality, full inverse support, and **full** conductor descent. R-0002 and R-0004 do not perform these computations for a chosen family.
4. For a normal carrier, determine **actual** local Cartier indices and test every inherited hypothesis of R-0034 and R-0035.
5. Apply R-0036 only after verifying its smooth singleton and conductor assumptions; compare divisors, not merely degrees.
6. Finally check the descended section gives an actual homogeneous mate with exactly the required support.

[R-0017](../results/singleton_plane_conductor_descent.md) excludes a specified degree-sixteen plane-projection family and a broader two-fixed-coordinate sublane, detecting a nilpotent conductor obstruction invisible in reduced support. It does not exclude all plane projections. [Q-0001](../questions/cartier_projection_models.md), asking whether any of the three Cartier singleton models actually yields a mate, remains open.

## Next mathematical tests

- Compute admissible projection parameters and torsion phases for one surviving family.
- Test R-0036 on an actual family meeting its smooth singleton hypotheses.
- Investigate higher actual Cartier indices outside R-0035, especially six and twelve.
- Compare with [normal-filtration defects](normal_filtration_boundary_obstructions.md) only through a common actual supported pair; do not identify conductor and initial-equation defects by analogy.

This chapter supplements, rather than replaces, the existing carrier chapter. No proofs, audits or historical source files are changed.
