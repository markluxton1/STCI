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
final collision. The [quartic-pencil classification](../../results/quartic_chow_pencil_classification.md)
exhibits a distinct non-invariant realization locus outside the
invariant \((4,4)\) Chow closure with the same vanishing moment.
The [one-carrier trace](../../arguments/torus/chow_trace_cone_jets.md)
extends the equation to some non-invariant presentations in all degrees.
Ambient smoothability does not imply smoothability through
translated-component cycles.

The exceptional family now has a geometric description at several
distinct levels. [Simultaneous endpoint cubic contact](../../arguments/torus/quartic_exceptional_carrier_geometry.md#two-sided-contact-and-the-nodal-even-eight-carrier)
forces the opposite-sign translates; on the carrier \(G_1\)
the minimal K3 resolution has a ten-node configuration and an
explicit **even eight** whose half maps to a nontrivial order-two
Weil divisor class. A
[Hilbert--Burch normal-map locus](../../arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
records generic doubled support without assuming
invariant equations. The
[geometric uniqueness argument](../../arguments/torus/quartic_chow_pencils.md#proof-route)
now upgrades it to a complete quartic-pencil classification:
liaison excludes the asymmetric multiplicities, while
the dual Hilbert--Burch canonical presentation and a
residual-line restriction yield the \(\lambda\)-orbit.
The classified non-invariant \(H\)-orbit moves **inside one Hilbert
fiber over a fixed Chow point** and acquires embedded corrections at
its opposite ends. It does not prove a general relation between
state polytopes and the relative endpoint different.
The [characteristic-two collapse](../../arguments/torus/quartic_hilbert_chow_limits.md#hilbert-over-chow-and-the-characteristic-two-collision)
is a non-invariant single-support quartic CI, outside the
multi-support classification in that characteristic.

The [fixed-carrier symmetry lattice](../../arguments/torus/fixed_surface_restriction_lifts.md#symmetry-and-the-multiplicity-lattice)
turns certain nonnegative integer combinations of actual
mate cycles into new actual mates. The proposed two-translate
sextic test has a sharp correction: \((5,4)\) is impossible by the
[involution--Bézout bound](../../arguments/torus/fixed_surface_restriction_lifts.md#involution--bezout-bound-and-the-remaining-sextic-locus);
the remaining unequal partitions are impossible on a nodal sextic.
For a normal Du Val sextic, the surviving
[ADE local classes and global correction budget](../../arguments/torus/fixed_surface_restriction_lifts.md#ade-local-classes-and-the-global-sextic-correction-budget)
must be satisfied simultaneously. Those tests do not
exclude arbitrary higher-singularity carriers or solve STCI.

The next geometry concerns higher-degree repeated-cycle lifts and the
boundary of their moment-constrained loci. A parameter escaping the
torus can leave the fixed-polytope fiber, so its compactification must
retain the full projective limiting cycle.

The [clean common-quadric boundary](../../arguments/equations/common_quadric_chow_boundary.md)
supplies the full special scheme in every degree \(a,b\ge3\) whenever
ambient cofactors are coprime and first cancellation is nonzero on the
quadric. Its balanced effective quadric subcycle excludes constant sole
support, including restriction rank drops. For nonzero restrictions with
gcd class \((h_1,h_2)\), the exact normal image and kernel dimension
\((h_1+2)h_2\) are known. When \(h_2=0\), the resultant ideal is
the squared center ideal and the graph is the ordinary blowup; this also
excludes these center points from the closure of fixed-degree sole-support
pairs, regardless of higher contact. When \(h_2>0\), the square-ideal
model fails, and its graph and deeper cancellation remain unresolved.
Zero restrictions, common ambient cofactors and other global strata remain
outside that graph theorem. For the fixed monomial quartic the special
cycle is outside the exact Chow-polytope fibre; its appearance in the
closure of varying translated arrangements remains a separate question.

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

The [equation-recovery interface](../../arguments/torus/fixed_surface_restriction_lifts.md)
starts with the translate coordinates themselves: each coefficient of
\(F(1,t,ut^3,vt^4)\) must vanish at every chosen \((u,v)\).
This constrains arbitrary surfaces. Repeated intersection multiplicities
require the joint transverse algebra, not repeated point evaluation.
Restriction to the fixed quartic gives a simultaneous syzygy-descent module
and its first annihilator; higher normal extensions determine whether a
power of the carrier equation enters the ideal. Ordinary restriction alone
does not determine that power, even for same-degree proper pairs.

The smooth quadric gives a contrasting answer: all its translates have the
same ruling class \((1,3)\), so their positive sum cannot be a degree-\(N\)
hypersurface section of class \((N,N)\). Thus the carrier geometry matters.
The [moving quartic locus](../../results/quartic_chow_pencil_classification.md)
permits collision partitions excluded on the fixed toric quartic. Its
exceptional non-invariant thickenings supply a fixed-cycle comparison
with both full torus limits.

The [all-order primary computation](../../arguments/torus/fixed_carrier_chow_arrangements.md#all-order-primary-structure-and-attachment-on-the-classified-carrier) on the classified fixed toric quartic calculates saturated layers from the semigroup. In its actual quartic collision residual degree drops from 12 to 8 and marked attachment from 18 to 12, but full thick attachment rises from 18 to 24. Extracting full primaries before and after absorption is not a flat-primary argument. The binomial-interpolation calculation is characteristic zero; it does not realize other carriers.

The [fixed auxiliary-quadric cut TS4](../../arguments/torus/fixed_carrier_chow_arrangements.md#a-fixed-auxiliary-quadric-detects-the-same-punctual-defect-at-every-collision)
shows that in the classified arrangements the
pointwise torsion divisor of \(Y_N\cap Q\)
is \(3(N-3)p_0+(N-1)p_\infty\), irrespective
of repeated-root collisions. The direct
source computation and the signed attachment
formula agree. This provides a control:
a stable fixed-cut resultant does not imply
stable reduced attachment, full attachment,
or residual degree. A complete moving
family with different carriers still
requires its actual equation source and
primary extraction.

The [explicit (4,6) proper pair TS5--TS7](../../arguments/torus/fixed_carrier_chow_arrangements.md#an-actual-non-lci-curvilinear-triple-the-conormal-torsion-is-visible)
has a full marked primary triple
whose generic transverse algebra is
curvilinear but whose cusp conormal
module has torsion \(k[[x]]/(x^2)\).
The pointwise attachment splits into
two torsion units and five determinant
units at that endpoint. It is a
useful actual-source check on
the filtration and local-cohomology
comparisons, not another sole-support
or arithmetic degeneration claim.

The [BF triple and actual-pair attachment TR1--TR4](../../arguments/residuals/residual_capacity_and_constructions.md#triples-the-full-attachment-has-only-two-independent-divisors) upgrades the \((4,6)\) triple calibration to a general statement: at multiplicity three the full-primary non-lci conormal torsion equals the saturated second normal defect, so every proper-pair full attachment layer is determined by that divisor and the actual equation determinant. The earlier semigroup calculation supplies one global family, not the underlying proof. At higher multiplicity the two-invariant collapse has not been proved; toric root collisions still cannot be treated using a universally monotone full-attachment invariant.

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
