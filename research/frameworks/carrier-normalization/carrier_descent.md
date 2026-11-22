# 4. Carrier surfaces, normalization, and conductor

Chapters [2](../residual-construction/two_surfaces.md) and [3](../formal-normal-geometry/from_symbols_to_equations.md) treat both defining equations and their transverse behavior along the curve. Here we **fix one integral carrier** \(X=V(F)\subset\mathbf P^3\) containing \(C=C_0\), and ask whether some second homogeneous equation \(G\) cuts out exactly \(C\) on \(X\).

The central issue is global: **does a divisor supported over \(C\) on the normalization of \(X\) descend to an actual hypersurface section of \(X\)?** The answer involves both divisor classes and conductor gluing.

**Scope boundary.** The [bounded-index normal-carrier exclusion, R-0035](../../results/normal_carrier_bounded_index_exclusion.md), assumes local Cartier indices at most four and inherited normal-carrier inputs. The [pointwise conductor/socle identity, R-0036](../../results/pointwise_conductor_socle_defect.md), requires a single smooth Cartier inverse branch, smooth normalization along it, and an invertible conductor without that branch as a component. Neither is an unrestricted carrier classification.

For a specified normal hypersurface in characteristic zero, a separately
[reviewed Hodge criterion](../../arguments/carriers/normal_carrier_divisor_geometry.md)
characterizes mate existence: the integral curve must be Q-Cartier and satisfy
\(C^2=(\deg C)^2/\deg X\). Its proof distinguishes existence of some mate
from the stronger formula for the least mate degree. Realizing this equality
on an actual higher-degree carrier of \(C_0\) remains a geometric question.

The [general conductor–differential comparison](../../arguments/carriers/carrier_conductor_differential_comparison.md)
constrains smooth normalization and smooth full conductor contacts, with
[singular-gluing controls](../../arguments/carriers/square_descent_and_singular_gluing.md) explaining its
boundary. The [normalization-index and power-descent account](../../arguments/carriers/normalization_indices_and_power_descent.md)
retains actual affine and projective supported constructions beyond C0.
For fixed C0 in characteristic zero, the [Gorenstein-normalized nonnormal
quintic theorem](../../arguments/carriers/quintic_gorenstein_normalizations.md) excludes all mate degrees;
the [toric quintic theorem](../../arguments/carriers/quintic_toric_center_incidence.md)
excludes all mate degrees for toric non-Gorenstein normalizations by
exhibiting extra inverse support for every admissible projection.
Non-toric, non-Gorenstein quintic normalizations and arbitrary higher-degree
carriers remain outside these exclusions.

## 4.1 Passing to the normalization

Let \(\nu:S\to X\) be the finite normalization, and put
\[
H=\nu^*\mathcal O_X(1),\qquad W=(\nu^{-1}C)_{\mathrm{red}}.
\]
The inverse image \(W\) may have several irreducible curves, some mapping to \(C\) with degree greater than one, and possibly isolated points. One must use the **full inverse support**, not just a preferred component.

If \(G\) is a mate of degree \(b\), the pulled-back section of \(bH\) has zero support exactly \(W\). If the curve components are \(\Gamma_1,\dots,\Gamma_t\), its divisor is
\[
\operatorname{div}(\nu^*G)=\sum_{i=1}^t n_i\Gamma_i,\qquad n_i>0,
\]
and hence
\[
\sum_i n_i[\Gamma_i]=b[H]\quad\text{in }\operatorname{Cl}(S).
\]
This is **necessary**. A class-group relation alone is not sufficient, because a rational section on \(S\) need not descend through the nonnormal locus of \(X\).

When \(W\) is a single curve \(c\) mapping isomorphically to \(C\),
the pulled-back divisor is \(nc\sim bH\). Intersecting with \(H\)
gives \(n\deg C=b\deg X\), since \(H\cdot c=\deg C\) and
\(H^2=\deg X\). For a quartic carrier of the fixed quartic this gives
\(n=b\). The curve \(c\) can be non-Cartier even though \(nc\) is Cartier.
The [statement-level review](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/chapters/CARRIER_AND_CONDUCTOR_GEOMETRY.md#editorial-and-verification-status)
records the correction to the divisor coefficient.

## 4.2 The full-conductor descent criterion

The accepted [fixed-carrier theorem, STCI-R-0003](../../results/fixed_carrier_conductor_criterion.md), works for an integral Cohen–Macaulay projective surface with finite normalization and ample polarization. First, an isolated inverse-image point outside the curve components obstructs a mate. In the remaining case define the relation lattice
\[
\Lambda=\ker\left(\mathbf Z^{t+1}\longrightarrow\operatorname{Cl}(S)\right),\qquad
(n_1,\dots,n_t,b)\longmapsto\sum_i n_i[\Gamma_i]-b[H].
\]
A relation produces an upstairs rational section with the prescribed divisor. Along conductor components away from \(C\), its **full conductor-unit classes** determine whether some positive power descends. Denote by \(\Lambda_{\mathrm{desc}}\) the sublattice whose off-\(C\) unit classes are torsion in the appropriate full conductor quotients.

**Fixed-carrier criterion.** A positive power of the polarization has a section vanishing set-theoretically exactly on \(C\) if and only if \(\Lambda_{\mathrm{desc}}\) contains a vector with every \(n_i>0\). For a hypersurface carrier in \(\mathbf P^3\), such a section lifts to an ambient homogeneous mate.

The conductor condition is not merely matching values on the reduced double locus. Nilpotent structure may impose further gluing conditions. In characteristic zero, residual torsion of reduced phases alone does not eliminate these nilpotent defects.

The [full lattice proof](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md) includes the support-covering cone test, primitive-ray arithmetic and exact one-branch mate degrees. The [local descent algebra](../../arguments/carriers/conductor_descent_algebra.md) proves membership, purity and unit-power lemmas, with tensor-equalizer, nonunit and split-phase counterexamples.

This is an **exact theorem for a specified carrier**, not an effective classification of every possible carrier: its class group, inverse branches, and conductor-unit map still have to be computed.

### Necessary first-graph and cluster tests before descent

For the fixed quartic the [branch valuation and marked-ideal Hodge identity](../../arguments/carriers/numerical_surface_pullback.md#branch-valuations-and-the-actual-first-blowup) applies also when the carrier is generically singular along C. The positive relation vector of its mate must lie in the normalized Hodge kernel, whereas the marked ideal's vector participates in the explicit gap split between branch imbalance and vertical principalization. The actual strict mate coefficients are obtained by subtracting the marked-ideal contribution from the branch valuations, with extra inequalities over special points. No-vertical single-root geometry is excluded irrespective of individual Cartierness. The [two-branch Cartier-cluster tests](../../arguments/carriers/numerical_surface_pullback.md#cartier-test-divisors-and-the-degree-three-per-order-boundary) supply exact rational matrices and integer ruling partitions for the degree-three-per-order locus. These necessary filters precede the conductor power test; they do not replace it. For generically regular support the [almost-Cartier criterion AC1--AC4](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#the-normalized-hodge-matrix-and-downstairs-almost-cartier-indices) additionally makes finite actual downstairs index and Hodge equality sufficient. These extensions await independent review.

## 4.3 The special case of one Cartier inverse curve

Suppose \(W=c\) is a single curve, \(\nu|_c:c\to C\) is an isomorphism, and \(c\) is Cartier on \(S\). These are **additional hypotheses**, not properties of an arbitrary normalization.

The accepted [singleton-lift classification, STCI-R-0002](../../results/cartier_singleton_lift.md), applies **assuming a mate exists**. Its key geometry is that the mate yields a positive divisor relation
\[
m c\sim bH.
\]
Consequently \(c\) is ample, and the complete linear system \(|c|\) identifies \(S\) with a normal surface of minimal degree. The proof uses the Cartier property, regularity along \(c\), adjunction, and surface classification. The theorem is a **necessary-model classification**, not a converse construction. Its [complete proof](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#cartier-singleton-models-the-complete-proof) includes regularity along c, rationality, the complete linear system and the singular-cone Cartier polarization.

For our fixed rational quartic, after excluding degree-four carriers by [STCI-R-0001](../../results/quartic_carrier_exclusion.md), three higher-degree normalization/polarization models remain within this restricted class:

| Carrier degree | Normalization | Lift and polarization |
| --- | --- | --- |
| 8 | Smooth quadric \(\mathbf P^1\times\mathbf P^1\) | \(c\sim(1,1)\), \(H\sim(2,2)\) |
| 8 | Quadric cone | \(c\) a smooth Cartier hyperplane conic, \(H\sim2c\) |
| 16 | \(\mathbf P^2\) | \(c\) a line, \(H\cong\mathcal O_{\mathbf P^2}(4)\) |

None of these rows establishes that the required projection or mate exists. Non-Cartier inverse curves, multiple inverse branches, and degree-greater-than-one maps to \(C\) are outside this classification.

## 4.4 Why projections are the next problem

To obtain a carrier in \(\mathbf P^3\) from a listed \((S,H,c)\), choose four sections of \(H\) whose restrictions to \(c\) give the fixed embedded curve \(C\). These sections must define a basepoint-free finite birational map onto an **integral hypersurface**, and the **full reduced inverse support** of \(C\) must equal \(c\).

Even if all these geometric admissibility tests pass, the conductor descent condition for a mate remains. Thus the work splits into three distinct checks:

1. **Projection admissibility:** the four sections produce the required finite birational hypersurface map.
2. **Inverse-support control:** there are no additional curve branches or isolated inverse points over \(C\).
3. **Conductor descent:** an upstairs positive divisor relation gives a descending section, possibly after a power.

The open [projection-model question, STCI-Q-0001](index.md#projection-and-conductor-descent-for-the-three-cartier-singleton-models), asks whether these checks can succeed for any of the three models.

## 4.5 Phase maps and torsion cosets

The accepted [projection-family reduction, STCI-R-0004](../../results/projection_phase_reduction.md), treats fixed finite-type families of admissible projections with the stated Cartier singleton hypotheses. After finite stratification and a finite surjective cover, the full-conductor descent problem is encoded by a morphism into a torus. A parameter admits a mate **if and only if** its phase tuple is torsion.

This is a significant reduction: it replaces an unbounded search over mate degrees by a structured question about the phase image and its torsion points. But the actual phase images and surviving torsion cosets for the three fixed-\(C\) models **have not been computed**. The mate locus need not itself be constructible.

The actual [plane and smooth-quadric examples](../../arguments/carriers/projection_support_differential_obstructions.md) distinguish the two principal failures. In the plane family full inverse support holds but every unit power fails infinitesimal descent. In the quadric families isolated inverse points already obstruct a divisor pullback. These restricted exclusions do not exhaust the complete projection families.

## 4.6 Interface with the simultaneous-equation geometry

These approaches study the same hypothetical pair \((F,G)\), but retain different information:

| Simultaneous \(F,G\) approach | Fixed-carrier normalization approach |
| --- | --- |
| Normal orders and common initial factors | Inverse branches of \(C\) on \(S\) |
| Exceptional directions on \(\operatorname{Bl}_C\mathbf P^3\) | Divisor classes and positive relations on \(S\) |
| Higher transverse contact and successive transforms | Gluing through the full conductor |
| Degeneration of graded second relations | Failure of a global section to descend |

There is a plausible research interface: exceptional directions and their special-point degenerations may reflect branches or conductor behavior of a chosen carrier. But **no general identification of these structures has been proved in the records**. The first task is to formulate an exact comparison for a specified carrier and its normalization, not to assume that the two obstruction theories coincide.


## 4.7 Ruled normalizations and conductor: a marked test family

The [ruled projection result R-0028](../../results/quartic_ruled_projection_geometry.md) gives explicit geometric models in which the distinctions of this chapter can be checked without conflation. The specified cone has finite normalization P(1,1,4) and smooth resolution F4; the projected cubic has finite normalization F1 and a doubled conductor line branched at the two marked endpoints. The projected scroll/cone intersection has reduced support C with two embedded length-one endpoint corrections. Neither normalization nor resolution is the original carrier, and a reduced inverse curve is not enough to certify descent of a hypersurface section.

The [arithmetic ruled four-section R-0029](../../results/quartic_arithmetic_ruled_models.md) adds a specialization test. Its relative Cartier four-section is finite flat over the parameter line with pushforward O plus O(-4) plus O(-8) plus O(-12). The characteristic-zero sections meet at the endpoints, while the characteristic-two fiber is a fourth Cartier multiple of one section. The scheme image of the mu4 orbit fails to commute with restriction to an endpoint, and normalization of the reduced total family does not specialize to normalization of the reduced special curve. This is a concrete warning against interchanging normalization, scheme image, and base change.

The associated flag and dual models, [R-0026](../../results/quartic_flag_conormal_geometry.md) and [R-0027](../../results/quartic_dual_singular_scheme.md), record endpoint contact and embedded Jacobian corrections. They help identify which nilpotent and conductor information a proposed projection-based argument must retain. They do not show that the conductor gluing criterion for an arbitrary integral carrier is automatically satisfied or violated.

A reusable projection test should therefore compute, in order: the finite normalization, the full inverse support and conductor scheme, the actual pullback of the candidate hypersurface section, and the descent condition on the original surface. A smooth resolution or a divisor-class calculation on its own does not replace this test.

## 4.7A Conductor gluing versus the top-socle divisor

The exact fixed-carrier descent criterion [R-0003](../../results/fixed_carrier_conductor_criterion.md) and the pointwise divisor identity [R-0036](../../results/pointwise_conductor_socle_defect.md) address different stages. R-0003 tests whether an upstairs divisor relation supported on the **entire inverse support** descends through the full conductor (possibly after taking a positive power). R-0036 starts with an **already existing actual supported pair**, and only under its smooth single-Cartier-branch and invertible-conductor assumptions identifies the top socle defect as \(D_n=(n-1)A-B|_c\).

The latter implies the pointwise necessary inequality \((n-1)\operatorname{ord}_p(A)\ge\operatorname{ord}_p(B|_c)\). It is not a substitute for full conductor-unit torsion or nilpotent gluing. Nor does a positive class-group relation establish the existence of the actual pair required to invoke R-0036.

The marked cubic and ruled normalizations illustrate why the distinction matters: reduced inverse support, finite normalization, resolution, and scheme-theoretic conductor are different objects. There is no established extension of the singleton divisor identity to multiple inverse branches or non-Cartier inverse curves by summing branchwise formulas.

## 4.7B Full Artinian phases and bounded-power exceptions

For a finite inclusion of characteristic-zero conductor algebras, descent of a power has two distinct parts: the nilpotent logarithm must already descend, while the reduced etale ratio must be torsion. The [finite-Artinian phase treatment](../../arguments/carriers/conductor_descent_algebra.md) makes the test exact. It explains why agreement on the reduced conductor cannot replace full scheme-theoretic gluing.

The [torsion-coset family reduction](normalization_conductor_projection.md#projection-phases-effective-scope-and-geometric-scaling) is conditional on a specified admissible projection family and its constructible phase image. Isolated surviving torsion phases have bounded orders once the image is explicitly controlled; positive-dimensional surviving torsion cosets can have unbounded least orders across carriers. A different [single-field compression theorem](../../arguments/carriers/conductor_descent_algebra.md#10-global-compression-and-characteristic-boundaries) is source-level and conditional on a single residual field at every generic conductor point. Split residual algebras defeat its bound. Neither statement computes the missing conductor phases for the three Cartier singleton models.

## 4.7C The strict-sextic singular-curve alternative

In the conditional (6,16) movement-two setting, a reviewed geometric argument isolates a precise alternative after the multiplier divisor is forced nonreduced. If the strict sextic is normal near multiplier-zero root points, any remaining singular curve \(\Sigma\) must lie on the strict quadric and be a trisecant ruling line, meeting the quadratic root at one ordinary node in the quadric direction. The calculation uses \(16d-2e=10n\), where \(d=H\cdot\Sigma\), \(e=E\cdot\Sigma\), and \(n\le2\) counts transverse nodal contacts. Importantly, \(e\) can exceed \(n\) because of other exceptional contacts. The other alternative is nonnormality at a multiplier zero. See [the detailed argument](../../arguments/carriers/normalization_conductor_phase2_addendum.md#singular-curves-on-the-strict-sextic-two-conditional-alternatives). Neither case has been excluded.

## 4.8 What this chapter does and does not establish

For a normal carrier, the [index and socle comparison](normalization_conductor_projection.md#normal-indices-and-the-exact-socle-bridge)
uses actual local Cartier indices. Investigate indices six and twelve outside
the [bounded-index exclusion](../../results/normal_carrier_bounded_index_exclusion.md).
A separate test is to compute the pointwise socle divisor for an actual
supported pair satisfying [R-0036](../../results/pointwise_conductor_socle_defect.md).
Comparing conductor and normal-filtration defects requires a common actual
pair and a proof of the comparison.

[Historical interface](https://github.com/markluxton1/STCI/blob/267affa79d3ad247f53f98381d9963fdc243df16/research/synthesis/carrier_conductor_socle_interfaces.md).

The proofs give the fixed-carrier conductor criterion, the restricted Cartier singleton-lift classification, and the fixed-family torsion-coset reduction under their respective hypotheses.

The quartic cases supply several fixed-geometry tests. The
[generic nonimmersion-prime audit](../../arguments/carriers/principal_mf6_normalization.md#source-2026-10-08-session-nonimmersion-prime-independent-auditmd)
uses a finite birational map \(\nu\) from a smooth projective surface and a
smooth integral \(c\sim H\) whose restriction \(\nu|_c\) is an immersion
into the ambient projective space. The pulled-back mate is a nonzero
scalar times the \(n\)th power of the defining section of \(c\), with
\(n\) invertible. It proves generic
immersion on every distinct integral curve \(E\) with \(H\cdot E>0\).
The [four MF6 boundary carriers](../../arguments/normal-geometry/mf6_and_nonnormal_structures.md#source-2026-10-07-session-nonnormal-mf6-independent-auditmd)
give fixed characteristic-zero all-degree obstructions from a duplicated
normalization fiber. The [ordinary-pinch and nodal-conductor analysis](../../arguments/normal-geometry/mf6_and_nonnormal_structures.md#source-2026-10-07-session-nonnormal-structural-progressmd)
gives separate contact bounds and a high-contact local control. For genus-two
trisecants, the [exact carrier ideal](../../arguments/carriers/genus_two_trisecant_carrier_proof.md)
gives an eleven-dimensional quartic space and retains the residual conic.
The same proof's nonzero-discriminant obstruction uses the actual normal
ambient blowup and its conductor identification. The [technical appendix](quartic_proof_interfaces.md)
contains the quartic case arguments and links to independent audits.

**Open:** computation of the actual projection phase images and conductor descent for the three models, and treatment of non-Cartier, multiple-branch, or higher-degree inverse lifts.

**Open comparison:** a direct geometric bridge between the common-normal-factor curve of Chapters 2–3 and the normalization/conductor data of an arbitrary carrier.

Continue with [how the exclusion results assemble](degree_exclusions.md), then the [open interfaces](../../MAP.md#questions-and-active-work).


## 4.9 Constructive torsion and the global realization boundary

The [twisted-cubic benchmark](../../arguments/carriers/square_descent_and_singular_gluing.md#torsion-constructions-and-the-limits-of-pinching) exhibits a characteristic-zero corrected square on a normal quadric cone: a non-Cartier Weil-class relation becomes an actual homogeneous cubic after correction by the carrier equation. It is a construction for another curve, and it explains a mechanism that remains worth seeking for the fixed quartic. The accompanying nodal pinching proof shows why freely prescribed phase torsion can violate the smooth marked curve and full inverse-support hypotheses.

The relation lattice also permits products of different global divisor directions whose logarithmic defects cancel. Such cancellation is unavailable by repeatedly powering one fixed ray with nonzero additive defect. An existence investigation must construct the compatible actual sections on the same projective carrier. This is the precise missing implication, rather than a search for arbitrarily large powers with unchanged local defect.

The [carrier-complement and collision controls](../../arguments/carriers/carrier_complement_and_collision_controls.md)
give separate geometric tests: disjoint lines obstruct affine complements for
rational quintics on smooth or nodal cubics, while a concrete conormal collision
computes a local singularity and its next contact depth. These examples concern
their specified curves and carriers; they do not extend the fixed-quartic exclusion
to arbitrary higher-degree surfaces.
