# Deformations through invariant supported limits

## Supported deformations from full opposite limits

The [supported-generator incidence investigation](../../investigations/supported-generator-incidence/index.md) owns the concrete bounded-family test, including actual moving-ideal generators and its completion criteria. The [quotient–Hilbert comparison investigation](../../investigations/quotient-hilbert-comparison/index.md) separately tracks what transverse quotient and endpoint information survives specialization. For the full-limit setup, see [the original formulation](../../arguments/equations/global_equations_and_constructions.md#proposed-test-supported-deformations-of-an-invariant-boundary-ideal).

The distinction governing both investigations is **full embedded ideal versus its extreme equation forms, pure hull, or fundamental cycle**. The [three-generator sextic limit](../../results/sextic_three_generator_full_limit.md) is a flat generator control with residual curves, not a sole-supported (6,6) boundary. An invariant supported complete-intersection ideal is excluded in characteristic zero under [R-0040](../../results/invariant_supported_ci_exclusion.md), but a moving general fiber need not be invariant. Neither fact settles the bounded attracting-family incidence problem.

## General arrangements and the CI realization locus

Geometric cycles in the full Chow-polytope fiber are parameterized by
\(\operatorname{Sym}^m(\mathbf G_m^2)\); a one-dimensional subtorus or
coset gives a smaller arrangement family. For each degree type \(ab=4m\),
retain actual CI ideals over these cycles. CI is a property of such a lift,
not of the cycle alone, and a general distinct-point arrangement is not a CI.

The [trace-moment theorem](../../arguments/torus/chow_arrangement_moments.md)
forces \(\sum_i n_i u_i/v_i=0\) for pairs with an eigenform generator or
the specified actual congruences, including invariant CI ideals and every
reduced CI arrangement, in characteristic different from two.
A linear equation in Chow coefficients expresses the condition and
separates the entire Chow closure of this locus from \(m[C_{u,v}]\) in
characteristic zero. This is stronger than losing CI structure only at the
final collision. It does not exclude a different, non-invariant CI lift over
a repeated cycle outside these equation classes and their cycle closure.
Ambient smoothability does not imply
smoothability through translated-component cycles.

The next geometry includes those repeated-cycle lifts, their possible
components and deformations, and the boundary of the moment-constrained
realization locus. A parameter escaping the torus can leave the fixed-polytope
fiber, so its compactification must retain the full projective limiting cycle.

## Actual arrangements on a fixed toric surface

The [fixed-carrier arrangement theorem](../../arguments/torus/fixed_carrier_chow_arrangements.md)
classifies every degree-\(N\) mate on the quartic
\(x_2^4=x_0x_3^3\) whose cycle consists of translates of \(C\).
Its root polynomial has nonzero constant coefficient and vanishing
coefficients \(c_1,c_2,c_5\), exactly the gaps of \(\langle3,4\rangle\).
In characteristic zero at least three distinct translates remain, but partial
collisions occur. The Frobenius/root-of-unity family is a special sublocus.
Every reduced CI arrangement on this carrier has it as an actual generator;
this inference fails for repeated-cycle support alone.
Uniqueness makes all the classified fixed-generator ideals invariant,
including repeated-root arrangements. A non-invariant lift with this support
cannot retain the carrier as one of its two defining equations.

The smooth quadric gives a contrasting answer: all its translates have the
same ruling class \((1,3)\), so their positive sum cannot be a degree-\(N\)
hypersurface section of class \((N,N)\). Thus the carrier geometry matters.
The [moving quartic locus](../../arguments/equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle)
permits collision partitions excluded on the fixed toric quartic. Understanding
its non-invariant thickenings and discriminant strata is a substantive question
even without a known route to an STCI obstruction.

## Concentrating interior information at the endpoints

The full intrinsic torus limit replaces the interior by a constant endpoint
algebra, with embedded endpoint lengths computed by
[R-0070](../../results/intrinsic_limits_endpoint_fibers.md). To compare the
quadratic conductor, degenerate the selected-root graph simultaneously.
The [exact comparison](../../arguments/linkage/toric_limit_conductor_comparison.md)
is \(\delta_i^{\mathrm{pure}}=\delta_i+\alpha_i-\beta_i\), where
\(\alpha_i\) and \(\beta_i\) are the embedded lengths downstairs and upstairs.
The existing torus theorem computes the former, not the latter. Controls
realize both signs of the correction. The open question is what actual global
equations force on this difference; discarding embedded points or applying a
CI postulation theorem directly to the pure limit loses required information.
