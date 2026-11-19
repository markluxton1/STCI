# Sextic filtration and source comparisons

[Framework orientation](index.md) · [Original section addresses](weights_and_limits.md)

## VI. The filtrations together in the sextic example

### Comparison diagram

Let \(\mathcal Y\) be the flat projective orbit closure over a
parameter chart of one direction, with special fiber \(Y_\pm\).
Read the sheaves on \(Y_\pm\) by pushforward along the closed fiber
inclusion. The inclusion of \(C\) gives the relative normal ideal
\(\mathcal K=\mathcal I\mathcal O_{\mathcal Y}\) (with \(\mathcal I\)
pulled back from \(\mathbf P^3\)), and let \(\mathcal K_\pm\) be its
image on the special fiber. The two routes are
\[
\begin{array}{ccc}
 \mathcal O_{\mathcal Y}
   &\xrightarrow{\text{full weight limit}}&\mathcal O_{Y_\pm}\\
 \downarrow\scriptstyle{\operatorname{gr}_{\mathcal K}}
   &&\downarrow\scriptstyle{\operatorname{gr}_{\mathcal K_\pm}}\\
 \operatorname{gr}_{\mathcal K}\mathcal O_{\mathcal Y}
   &\xrightarrow{\text{base change, then quotient}}&
      \operatorname{gr}_{\mathcal K_\pm}\mathcal O_{Y_\pm}.
\end{array}
\]
At the bottom, reduction induces a surjection after tensoring with
the special residue field, because the images of the powers of
\(\mathcal K\) are the powers of \(\mathcal K_\pm\).
Flatness of the power quotients over the parameter DVR suffices for
the bottom map after tensoring to be an isomorphism, by the
degreewise Tor sequence. The flat projective family gives the
specialization in the top row and preserves the Hilbert polynomial.
The endpoint construction in Part IV takes a finite image over a
parameter on the curve itself.
[Normal-cone base-change criterion](../../results/normal_cone_slice_specialization.md#statement) ·
[Finite-flat slice with different normal algebras](../../results/supported_length_five_defect_specialization.md) ·
[Geometric endpoints versus opposite Hilbert limits](../../investigations/quotient-hilbert-comparison/index.md#method).

### A verified full sextic limit

<a id="4-the-hilbert-scheme-limit-remembers-relations-between-equations"></a>

The proper \((6,6)\) example [R-0046](../../results/sextic_three_generator_full_limit.md) demonstrates why the full saturated Hilbert limit cannot be reconstructed from the two displayed weight initials. After cancellation and syzygy lifting, its special ideal is
\[
J_+=(q^3,b_4q,a_6b_4),\qquad
a_6=x_0^2x_3(x_0^2x_2-x_1^3),\quad b_4=x_0^3x_2.
\]
It is ACM, with generator degrees \(6,6,10\), syzygy degrees \(10,12\), and the preserved complete-intersection Hilbert polynomial \(36d-144\). The [full proof](../../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit) establishes the flat contracted family, saturation, and resolution. The example has residual support: it is **not** a sole-support sextic pair.

<a id="41-how-the-boundary-cycle-changes-in-the-full-limit"></a>

Both fibers have residual degree \(32\), but the plane cubic \(V(x_2,x_0x_3^2-x_1^3)\) specializes to the cycle \([L_{13}]+2[L_{01}]\). Neither fiber has embedded associated components. The [exact cycle and endpoint-scheme proof](../../arguments/torus_sextic_residuals.md#cycles-and-endpoint-schemes-of-the-three-generator-limit) retains the local charts and multiplicities; the generic torus quotient is \(k\). This residual-cycle change is distinct from the separate sole-support incidence argument.

### Supplementary sextic source spaces and pencils

<a id="sextic-source-spaces-and-pencils"></a>
<a id="6-from-invariant-examples-to-the-supported-ci-hilbert-locus"></a>
<a id="7-parameter-spaces-pencils-fixed-loci-and-deformation-strata"></a>

The actual degree-six order-two source \(H^0(\mathcal I_C^2(6))\) is **23-dimensional**, with torus-weight dimensions \((1,1,2,2,2,2,3,2,2,2,2,1,1)\) in weights \(6,\ldots,18\). Its monomial coefficients \(c_{w,i,j}\) satisfy, separately at each weight,
\[
\sum c_{w,i,j}=\sum i\,c_{w,i,j}=\sum j\,c_{w,i,j}=0.
\]
These are the value and two first normal coefficients; the [global equation-jet proof](../../arguments/equations/global_equation_jets.md#exact-global-freedom) establishes the global sheaf-power condition. On the containing quadric \(Q\), the double-sextic restriction is \((bc^3-ad^3)^2\) times a section of \(\mathcal O_Q(4,0)\). This source calculation is distinct from the [actual cubic matching problem](../../arguments/spectral/rank_strata_and_sextic_lifts.md) and the [sole-support sextic reduction](../../arguments/carriers/sextic_pair_reduction.md), which in characteristic zero or \(p\ge7\) requires generic curvilinear length nine under its hypotheses.

The degree-six equation space vanishing on \(C\) has dimension \(59\), so sextic pencils form \(\operatorname{Gr}(2,59)\), dimension \(114\). Pencils entirely of double sextics form \(\operatorname{Gr}(2,23)\), dimension \(42\), codimension \(72\). The analogous quartic equation space has dimension \(18\), and quartic pencils have dimension \(32\). This codimension describes a **constant-pencil** condition, not arbitrary dependence of normal symbols over \(k(C)\). Actual sole support and generation require the [moving-ideal criterion](../../results/moving_ideal_generator_criterion.md).

The quartic root pencil \(z^4-\eta z+\eta-1\) has characteristic-zero discriminant \((\eta-4)^2(-27\eta^2+40\eta-16)\). At \(\eta=1\), a separable root exits the quotient torus at zero; the \(\eta=\infty\) boundary and collisions of marked and residual points are different events. These are calculations for this parameter line, not a general root-space classification. [Root-pencil proof](../../arguments/torus/root_pencil_geometry.md#3-three-ways-the-pencil-leaves-the-open-arrangement).

### What the new weight information does and does not test

The eleven missing second-order sextic symbols have verified unshifted
weights \(7,\ldots,17\) (centered \(-5,\ldots,5\)). Their cokernel is
canonically \(H^1(\mathbf P^3,I_C^3(6))\), and the unique-quadric flag
splits its character list into eight weights from
\(H^1(Q,\mathcal O_Q(3,-3))\) and three from
\(H^1(Q,\mathcal O_Q(2,-2))\), with the appropriate generator-weight
shifts; see [the weight-by-weight proof](../../arguments/equations/global_equation_jets.md#verified-characters-and-the-quadric-flag-cohomology).
This explains the symbol deficit cohomologically but does not yet identify
the quadric filtration with the target filtration of the order-five Čech
differential, nor certify a supported pair. For the three surviving ADE primitive triples, the
[sextic contact argument](../../arguments/carriers/sextic_ade_reduction.md#geometry-of-the-cubic-contact-incidence)
constructs proper decomposable cubic-contact pencils using the
nonzero joint kernel and absence of a fixed surface component.
The [intrinsic primitive-triple proof](../../arguments/carriers/sextic_triple_intrinsic_contact.md)
now derives the source dimensions, restricted contact images and full
determinant span by quadric interpolation and regularity. For the
algebraic orbits, the primitive layers also recover the torus characters
without ambient source matrices. The determinant image remains full for
every pair of degrees at least six; it does not determine the
decomposable zero locus or a moving supported ideal.
The [fourth-coefficient test](../../arguments/carriers/sextic_ade_reduction.md#sharp-length-five-for-pencils-with-a-quadric-divisible-member)
gives a sharp length-five bound on proper pencils with a first-order member
and dependent quadric restrictions. Higher contact with independent
restrictions is open. Applying the residual examples to a torus limit
requires specifying a moving family and tracking its full initial ideal.

### Source map and scope

<a id="proofs-of-orbit-multiplicities-and-full-limits"></a>
<a id="1-orbit-families-and-the-residual-boundary"></a>
<a id="5-the-geometry-of-invariant-curve-strata"></a>
<a id="11-eight-quotient-points-and-a-quadruple-residual-line"></a>
<a id="12-six-quotient-points-and-a-twelvefold-residual-line"></a>
<a id="13-a-noncurvilinear-quotient-of-the-same-length"></a>
<a id="2-fixed-point-incidence-forces-residual-boundary-for-eigenpairs"></a>
<a id="3-residual-curves-move-before-they-acquire-boundary-support"></a>
<a id="31-specializing-divisors-not-attracting-individual-points"></a>
<a id="32-absorption-changes-the-decomposition-into-marked-and-residual-cycles"></a>

| Part | Established on the stated inputs | Conditional statement or open comparison | Proof homes |
| --- | --- | --- | --- |
| I | Balanced conormal, transverse transport and frame divisor | A transverse boundary moves the marked support off the coordinate torus | [Conormal transition](../../arguments/quartic_specialization_and_symbols.md#conormal-transition-p-009-characteristic-jump-in-the-normal-bundle-of-c_0), [normal map](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#a-reduced-tropical-model-and-the-exact-normal-map), [transverse control](../../arguments/torus_sextic_residuals.md#a-transverse-limit-with-generic-length-two) |
| II | Actual normal symbols, binary resultant, full normal cone | The quotient-relation resultant bound uses a full generic binary CI and an actual sole-supported lci thickening | [Global resultant](../../arguments/normal-geometry/formal-normal-intersection.md#coprime-first-normal-forms-and-the-global-resultant), [equation comparison](../../arguments/filtered_equation_comparison.md), [quotient-relation bound](../../results/nonsaturated_first_relation_resultant.md) |
| III | Full opposite limits and moving-ideal generation | Extreme gcds require a hypothetical sole-support pair. The trace and length-eight restrictions have their stated equivariance hypotheses | [Hellus–Hübl](https://arxiv.org/pdf/1312.7661), [weight restrictions](../../arguments/torus/equivariant_degree_bounds.md), [full supported limits](../../arguments/torus_hilbert_boundary.md), [sextic bound](../../arguments/torus_sextic_residuals.md#the-sharp-sextic-eigenpair-bound) |
| IV | Endpoint lattices, conductor, pure intrinsic limits and embedded lengths | Strict movement is conditional on an actual sole-support CI. Full opposite-endpoint algebras and moving equation incidence remain open | [Constant quotient descent](../../arguments/torus_embedded_quotients.md), [moving modification](../../arguments/torus/tropical_thickenings_and_endpoint_duality.md#the-entire-finite-modification), [intrinsic comparison](../../arguments/torus_hilbert_boundary.md#endpoint-fibers-in-the-two-intrinsic-limits) |
| V | CI postulation and degree exhaustion for a pure containing curve | Sole support is tested by the full degree budget, with residual boundary degrees included | [Two surfaces](../residual-construction/two_surfaces.md), [degree exhaustion](../../arguments/torus_embedded_quotients.md#pure-curve-degree-exhaustion), [orbit degrees](../../arguments/torus_sextic_residuals.md#orbit-curves-and-finite-quotient-degree) |
| VI | R-0046 gives a saturated ACM limit with three generators and residual degree \(32\) | Base change for the relative normal cone of a proposed family needs its own hypotheses. Recovery of arbitrary supported CI presentations from opposite limits is open | [R-0046 proof](../../arguments/torus_sextic_residuals.md#the-saturated-three-generator-full-limit), [normal-cone criterion](../../results/normal_cone_slice_specialization.md), [supported-boundary framework](index.md#directional-loci) |

Other reviewed sextic controls retain their separate proof sections
for [length-eight and length-six quotient schemes](../../arguments/torus_sextic_residuals.md#eigenpair-residual-controls),
[moving residual divisor limits](../../arguments/torus_sextic_residuals.md#moving-residual-curves-and-their-full-limit),
and [residual absorption](../../arguments/torus_sextic_residuals.md#residual-absorption-in-a-proper-flat-family).
The [historical source review](https://github.com/markluxton1/STCI/blob/ddcb50e003aff185d48455f6edec420e7bec34a8/research/synthesis/toric_sextic_residuals_and_limits.md#L625-L631)
records the scope of the original residual and full-limit checks.


## Related proof developments

- [Mixed-weight sextic and full limits](../../arguments/torus/mixed_sextic_residual_limits.md)
- [Actual endpoint-four sextics](../../arguments/carriers/endpoint_four_actual_sextics.md)
- [Split sextic conductors and multiplicity-six restrictions](../../arguments/carriers/split_sextic_conductor_and_contact.md)
- [Split sextics with two ramified roots](../../arguments/carriers/split_sextic_two_ramified_roots.md)
