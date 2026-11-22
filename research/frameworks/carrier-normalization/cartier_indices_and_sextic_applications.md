# Cartier indices, normal socles, and sextic applications

[Carrier Framework](index.md) · [Original section addresses](normalization_conductor_projection.md)

## Minimum actual carriers and Cartier-index compression

The [canonical compression proof](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#canonical-compression-on-a-minimum-actual-carrier) chooses a carrier of minimum degree **among carriers that occur in an actual defining pair**. In characteristic zero, for a generically regular carrier and local Cartier exponent e, Picard torsion-freeness compresses its mate to eC~nH. For the fixed quartic, n=4e/a≥a and e≥a²/4; a genuinely minimum sextic carrier would require 3|e and e≥9. Choosing instead a minimum-degree surface merely containing C would invalidate the argument: the smooth quadric contains C but is not a possible sole-support carrier in characteristic zero.

This mechanism can be used constructively as a lower-complexity target or obstructively as a local-index constraint. The proof uses no genus calculation; its degree-d formulation is in the same mathematical home. Generic singularity along C remains an essential boundary. The [all-characteristic almost-Cartier criterion](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) removes the characteristic restriction in this compression for generically regular hypersurfaces, pending independent review.


## Normal indices and the exact socle bridge

[R-0034](../../results/normal_carrier_index_socle.md) uses actual local Cartier index r, not surface multiplicity. For an actual mate multiplicity n=kr, the pointwise socle relation is D_n=(k−1)A_F+kD_r, with ordinary normal-layer torsion satisfying 2Σlength\(T_i\)=nD_n. [R-0035](../../results/normal_carrier_bounded_index_exclusion.md) uses its inherited normal-carrier and quadratic-direction hypotheses to exclude the regime where all actual on-curve indices are at most four; the accepted formulation does not treat arbitrary higher indices or nonnormal carriers. The [S2 extension of the actual power-socle proof](../../arguments/carriers/normal_carrier_symbolic_torsion.md#normality-is-unnecessary-the-actual-almost-cartier-power-theorem) removes normality when the carrier is generically regular and the actual downstairs indices are used. The extension awaits independent review.

[R-0036](../../results/pointwise_conductor_socle_defect.md), for an already existing supported pair with its smooth singleton Cartier lift and invertible conductor, gives D_n=(n−1)A−B|c as an equality of actual divisors. It implies coefficientwise inequalities, not just a degree bound. It is not a substitute for full conductor-unit membership, and it has no established branchwise extension by summing over multiple inverse curves. See [the exact interface](carrier_descent.md#47a-conductor-gluing-versus-the-top-socle-divisor).

A separate [normal-carrier divisor reformulation](../../arguments/carriers/normal_carrier_divisor_geometry.md) preserves the source's proposed equivalence between a Q-Cartier Hodge equality and an actual positive divisor relation, together with its suggested local-socle certificate. That source strengthening remains explicitly pending independent mathematical audit; relocating its full proof does not replace the stated inputs of R-0034/R-0035.


The [normalized first-graph theorem](../../arguments/carriers/numerical_surface_pullback.md#branch-valuations-and-the-actual-first-blowup) gives another index constraint for entirely-thick carriers, where the downstairs reduced almost-Cartier class need not exist: for two inverse branches without vertical fibers the low-slope branch has positive numerical square strictly below `16f_i^2/a`, so its upstairs Cartier index exceeds `a/(16f_i^2)`. At degree-three-per-order and with two degree-one lifts the [ruling-cluster and square table](../../arguments/carriers/numerical_surface_pullback.md#cartier-test-divisors-and-the-degree-three-per-order-boundary) makes the necessary divisibility explicit and excludes Cartier low lifts. This is not the original normal-index bound; its proof is an actual two-branch numerical and Cartier-lattice comparison. Independent audit is pending.

## Conditional sextic applications and the remaining implication

The [conditional sextic treatment](../../arguments/carriers/normalization_conductor_phase2_addendum.md) retains the actual rank-22 global source, all q³ lift freedom, constant-rank cubic correction map, the quadric-cycle norm proof including collision and branch multiplicities, free-orbit unit certificate, remaining two-node conic and zero-defect pencils, degree-52 exceptional locus, and the singular-trisecant/nonnormal alternative. [Endpoint-four actual sextics](../../arguments/carriers/endpoint_four_actual_sextics.md#endpoint-four-sextic-constructions) provide complete second-symbol lifts and a single-carrier necessary jet exclusion, not a construction or exhaustion of the family.

The common mechanism is a global section whose admissible local class must lift through an actual source module and then descend through an actual conductor. Divisor classes, reduced phases, first symbols and formal roots each forget different information. Their comparison can guide constructions and exclusions only after establishing a common actual carrier or pair. No all-carrier coverage theorem, full h=2 incidence solution, or unrestricted characteristic-zero STCI conclusion follows.


## Characteristic range of the mechanisms

| Mechanism | What extends, and what fails |
| --- | --- |
| Full conductor fiber product, pure generic-to-global descent, fixed-carrier relation cone | Characteristic independent under the stated finiteness, depth and support hypotheses. |
| Nilpotent unit-power rigidity | In characteristic zero, a nonzero logarithmic defect survives every power. In characteristic p, a sufficiently large p-power kills a finite nilpotent defect; it leaves non-torsion residue phases untouched. |
| Single-field extension-degree compression | The proved form uses characteristic zero and all roots of unity in the residue field. It is not a theorem for arbitrary Q-algebras or arbitrary inseparable residue extensions. |
| Plane differential exclusion | The identity forces b=0 in the field. It excludes every b>0 in characteristic zero; in characteristic p it only excludes b not divisible by p. A p-power can evade the differential test. |
| Minimal-degree Cartier singleton classification | The retained proof uses characteristic-zero surface classification. No unrestricted positive-characteristic extension is asserted. |
| Conductor–socle Jacobian comparison | The pointwise proof extends when the Jacobian factor n is invertible, with the same geometric hypotheses and actual socle input; in characteristic dividing n the Jacobian may vanish although the socle does not. |
| Conditional sextic global-symbol algebra | An exact rational calculation extends only after its denominators and necessary rank minors remain invertible. The characteristic-zero Milnor/Hodge surface contradiction is a separate input and cannot be transported just from a matrix rank. |

For this fixed embedding, every positive characteristic admits an actual STCI with a quartic carrier; the [complete characteristic-specific construction](../../arguments/arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) proves this directly. Thus the characteristic-zero quartic-carrier exclusion and the nilpotent power obstruction must not be stated without their characteristic range. Positive-characteristic witnesses at each finite level do not supply one characteristic-zero or infinite-formal descending power.

For a prescribed degree rather than eventual powers, [sections and modules through normalization](../../arguments/carriers/normalization_section_and_module_descent.md) proves the exact fiber-product and module-factorization criterion, including full inverse support, all branch degrees, integral singular curves and the normalized-blowup support test. The supported-conductor power argument there is a distinct direct proof.


## Related proof developments

- [Conditional (6,16): singular roots, cubic source, and conductor](../../arguments/spectral/conditional_2_12_singular_and_conductor.md)
- [Ramification and the principal socle comparison](../../arguments/carriers/ramification_and_socle_controls.md)
- [Genus-one conductor and genus-two adjoint and projection](../../arguments/carriers/genus_one_two_adjoint_and_conductor.md)
- [Actual projection spaces and conductor phases](../../arguments/carriers/projection_conductor_contact_and_phase.md)
