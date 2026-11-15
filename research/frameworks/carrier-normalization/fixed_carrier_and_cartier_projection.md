# Fixed carriers, Cartier models, and admissible projections

[Carrier Framework](index.md) · [Original section addresses](normalization_conductor_projection.md)

## Fixed-carrier existence and the shared descent mechanism

The [carrier chapter](carrier_descent.md#42-the-full-conductor-descent-criterion) introduces the relation lattice and the full conductor test. The [proof of R-0003](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#4-an-exact-fixed-carrier-criterion-including-thick-support) applies in arbitrary characteristic to integral Cohen–Macaulay projective surfaces with finite normalization and ample polarization, including generically singular carriers where the reduced marked curve need not define an APic class.

The [local algebra](../../arguments/carriers/conductor_descent_algebra.md) proves the underlying mechanism and its limitations. Membership is in the fiber-product conductor ring, not merely a tensor equalizer. In characteristic zero, nilpotent logarithmic defects must vanish; the reduced phase can then have finite order. If each reduced upstairs algebra is a single field, its extension degree bounds a sufficient exponent. Split phases such as (1,zeta) have unbounded least orders even with two branches. A nonunit can behave differently; powers of t on a cusp enter its conductor. None of these statements computes an actual phase image.

The relation cone offers both obstruction and construction. Its Hilbert basis has a full-support member sum exactly when the union of basis supports covers all inverse curves; an individual basis member can miss branches. Products from distinct global divisor directions can cancel opposite logarithmic defects, whereas powers along one fixed divisor ray cannot. See [the constructive cone application](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#constructive-use-of-the-descent-lattice).


## Necessary Cartier singleton models and actual projection tests

In characteristic zero, assuming an actual mate and an isomorphic Cartier singleton inverse curve \(c\), [R-0002](../../arguments/carriers/fixed_carrier_descent_and_cartier_models.md#cartier-singleton-models-the-complete-proof) gives \(c^2=d^2/\deg X\) for a rational curve of degree \(d\) and classifies the normalized models and integral polarizations. After the [characteristic-zero quartic-carrier exclusion, R-0001](../../results/quartic_carrier_exclusion.md), the [carrier chapter](carrier_descent.md#43-the-special-case-of-one-cartier-inverse-curve) lists the surviving degrees \(8,8,16\) and [the tests for actual projections](carrier_descent.md#44-why-projections-are-the-next-problem).

The [explicit projection proofs](../../arguments/carriers/carrier_conductor_differential_comparison.md#projection-support-and-differential-obstructions) expose different failures. The plane map [s⁴:s³t:st³+z⁴:t⁴+s³z] is an actual finite degree-sixteen normalization with full inverse support z=0, but every positive mate degree is excluded by a polynomial derivative identity. The general two-fixed-coordinate sublane has the same obstruction. Its generic conductor residue is already trivial, while a nonzero first nilpotent jet survives every power. By contrast, the two actual smooth-quadric families have isolated inverse points, so fail before unit descent. The corrected quadric audit retains seven forced endpoint extras in the kappa family and the exact four-or-five extra points in the companion family. Neither argument exhausts the complete projection space.

The [twisted-cubic corrected-square benchmark](../../arguments/carriers/square_descent_and_singular_gluing.md#torsion-constructions-and-the-limits-of-pinching) shows that characteristic-zero singular-carrier torsion can produce an actual homogeneous pair for a different curve. The abstract nodal pinching counterexample shows why local phase torsion alone can destroy the marked full-support requirement. These constructive and negative controls explain the missing geometry rather than presuming nonexistence for the quartic.


## Projection phases, effective scope, and geometric scaling

[R-0004](../../results/projection_phase_reduction.md) works in a specified finite-type family of admissible Cartier-singleton projections. After stratification and a finite cover, full conductor descent is a torus torsion-phase test. Its proof keeps nilpotent equations, generic conductor components and excluded specialization boundaries. The actual phase images of the three quartic models remain uncomputed. Their on-C thresholds are 5,5,13; with phase order E, every positive multiple of E at least the relevant threshold is a mate degree, with any additional degrees confined to smaller multiples.

The [torsion and rational-phase proofs](../../arguments/carriers/projection_torsion_and_rational_phase_bounds.md) distinguish a finite torsion-coset envelope from a constructible mate locus. For an explicitly presented rational constructible phase image W=⋃(Y_i−B_i), the effective method partitions supports into vanishing blocks, applies Mann's ratio bound P\(S\)=∏_{prime≤S}prime, and solves binomial systems by Smith normal form. With maximal translated support degree d and support size S in dimension D, isolated torsion orders are at most P\(S\)d^D; this is a bound, not a divisibility assertion. A common annihilating exponent may use P\(S\)lcm(1,...,d^D). Each coset must still be tested against the removed boundaries B_i. Positive-dimensional retained torsion cosets have unbounded orders. The [raw-input corollary](../../arguments/carriers/projection_torsion_and_rational_phase_bounds.md#from-explicit-projection-input-to-a-decision-procedure) first constructs actual admissible conductor/phase data; its termination theorem is not an executed fixed-model calculation.



## Five-coordinate geometry of the phase

For an admissible fixed-\(C_0\) Cartier-singleton projection \(S\to X\subset\mathbf P^3\), adjoining the primitive section \(Q\) to the four projection sections gives a finite image \(Y\subset\mathbf P^4\), with coordinates \([U_0:U_1:U_2:U_3:Q]\). Projection from the last-coordinate point is finite birational onto \(X\). The hyperplane \(Q=0\) pulls back to \(2c\) or \(4c\) in the three normalized models and has reduced support \(C_0\).

For \(\zeta\in k^\times\), let \(T_\zeta\) scale only the fifth coordinate. If two conductor branches have identical \(U_i\) coordinates and primitive-section ratio \(\zeta\), their images lie in \(Y\cap T_\zeta\(Y\)\). A descending mate power requires the relevant constant ratios to be roots of unity **and** requires full nilpotent conductor descent. This is a geometric reformulation of the phase obstruction, not an exclusion. The hyperplane curve \(Q=0\) is common to these intersections for every \(\zeta\); a naive intersection-degree argument must first remove this forced component before counting additional branch curves. The fixed-degree affine split-conductor example below shows why phase orders cannot be bounded from finite presentation or smooth singleton inverse support alone. Any useful global bound must invoke the actual projective polarization, contact divisor, or differential/conductor budget. [Original five-coordinate formulation](../../arguments/carriers/projection_conductor_contact_and_phase.md#actual-projection-spaces-and-conductor-phases).



## Actual projection coefficient spaces

For the three primitive Cartier singleton models (smooth quadric, quadric cone, plane), the restriction kernels of the full section spaces to the fixed quartic have dimensions 4, 4, 10. Choosing lifts of the four fixed coordinate sections is an affine graph space of dimensions **16, 16, 40**, respectively, before equivalences. Basepoint freeness gives finiteness by ampleness, but birationality and **full inverse support** are additional conditions. For the graded section ring (B=\bigoplus_{b\ge0}H^0(S,bH)) and the four-section subring \(R\), the primitive ray section \(Q\) has a degree-\(b\) mate precisely when \(Q^b\in R_b\), with the prescribed normalization/support hypotheses. Source: [current proof](../../arguments/carriers/projection_conductor_contact_and_phase.md#actual-projection-spaces-and-conductor-phases).



## Fixed-degree affine control with unbounded phase

Let \(B=k[u,v]\), \(\lambda=\alpha+\beta\), \(\mu=\alpha\beta\), \(y=v^2-\lambda uv\), (h=y+\mu u^2=\(v-\alpha u\)\(v-\beta u\)), \(z=vh\), and \(A=k[u,y,z]=k[u,y]\oplus h k[u,y]v\). The carrier relation is \(z^2-\lambda uhz-yh^2=0\); the **entire conductor** is (hB). The quotients are \(A/hB=k[u]\) and (B/hB=k[u,v]/(\(v-\alpha u\)\(v-\beta u\))). For \(Q=v^q\), \(Q^n\in A\) exactly when \(\alpha^{qn}=\beta^{qn}\). Choosing \(\alpha/\beta\) of order \(N\) coprime to \(q\) forces least descent exponent \(N\). The inverse support of the indicated affine downstairs line is the smooth line \(v=0\). This disproves any algebra-only universal bound on phase order, **not** a projective fixed-\(C_0\) bound. Same source.


