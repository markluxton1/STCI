# Cross-repository proof audit: what forces residual support?

**Scope.** A comparison of current proof mechanisms, not a separate research queue or a new exclusion. The [active front door](open-items.md) organizes live questions; the [KG queue](knowledge-gain-priorities.md) alone ranks strategic payoff. Canonical argument/result/framework owners control mathematical claims. This audit records what would justify combining their mechanisms.

The common question is about an **actual proper homogeneous pair** through
the fixed rational quartic in characteristic zero. Its degree identity is
`ab = 4 m_C + deg R`. A bridge must do more than restate this identity:
it should either force a positive contribution to the residual cycle,
preserve the actual equations in a construction reaching zero, or identify
an obstruction shared across proof families.

## Pilot: degree four and the partial degree-five exclusions

### Bottom line

In this audit, \(C=C_0\) denotes the fixed quartic and \(\pi\) denotes sectional genus; neither is a new varying curve or parameter.

* **Quartics are completely excluded:** every integral quartic through the fixed C₀ over algebraically closed characteristic zero, every positive mate degree, all normalization/conductor types. R-0001. The narrower (4,4) contact proof is not the all-degree proof.
* **Quintics are only partially excluded:** all nonnormal quintics with Gorenstein normalization; all quintics with toric normalization; and normal globally ADE quintics for mate degree 8. Normal non-ADE quintics, other mate degrees outside the ADE(5,8) statement, and nonnormal non-toric non-Gorenstein normalizations are not closed by those results.
* The fixed-residual bridge explains an ordinary source open and now many boundary residual configurations. It does not replace the quartic exceptional assembly or quintic conductor/source classification. Repeated residual components, intersections on C and tangencies alone are no longer valid reasons to dismiss the strengthened bridge. A real failure must identify its normal-root, local normalization/intersection, complete divisor, or actual-source hypothesis.

Paths in the tables identify the canonical proof owners; the statements below summarize those owners, not new proofs.

### Quartic mechanisms to preserve

| Scope/result | Exact mechanism and decisive boundary | Authoritative owner/anchor |
|---|---|---|
| Common reduction for all integral quartics | Generic regularity along C from plane-section genus 3 < degree C = 4; sole support forces one full inverse c ≅ C, no extra inverse points, div(G)=bc~bH. On resolution smooth passage meets exactly one exceptional prime; c#²=4−q and q+KZ=2π. This genus argument does NOT automatically extend to quintics. | [arguments/carriers/quartic_carrier_proof.md#1-sole-support-smooth-passage-and-the-common-correction-identity](../../arguments/carriers/quartic_carrier_proof.md#1-sole-support-smooth-passage-and-the-common-correction-identity); [results/quartic_carrier_exclusion.md](../../results/quartic_carrier_exclusion.md) R-0001 |
| Normal quartics, rational singularities | Jaffe's linear-normality obstruction; C0 is not linearly normal. Other normal quartics use the actual irrational-singularity classification, not an ADE-only assertion. | same owner `#3-normal-quartics-exceptional-correction-and-actual-ideal-vanishing` |
| Normal quartics, irreducible anticanonical exceptional support | Global denominator compression plus correction budget t+q=6 and ADE rank/order bound Σγ≤RP/(R+P). Strict gaps cover smooth elliptic, nodal and cuspidal irreducible support together. | same owner `#31-compression-and-the-passage-budget`, `#32-a-single-inequality-excludes-irreducible-anticanonical-support`; [arguments/carriers/normal_carrier_compression.md#1-global-denominator-compression](../../arguments/carriers/normal_carrier_compression.md#1-global-denominator-compression) |
| Normal quartics, reduced reducible exceptional support | Exact complete cycle enumeration leaves 5 rows; 4 compress to quadric mate, last fails actual ideal-versus-numerical defect(3<10/3). Keep complete inverse-column denominators and first-normal budget. | same owner `#33-reduced-reducible-support-the-exact-finite-calculation`; [arguments/carriers/numerical_surface_pullback.md](../../arguments/carriers/numerical_surface_pullback.md) |
| Normal quartics, nonreduced exceptional support | Necessary tree supersets plus low-degree independent exclusions leave Type D, t = 2; the actual maximal ideal pulls back to O(−E), so smooth passage requires t = 1. Numerical graph alone does not finish. | same owner `#34-nonreduced-support-trees-and-the-actual-maximal-ideal` |
| Nonnormal quartics π = 0 | Full normalized system gives two scrolls, Veronese or cone. Scrolls compress descended powers through full nonreduced conductor or violate immersion. Veronese has three fixed-pencil types with distinct inverse-support/first-jet endings. Cone uses full inverse or differential kernel, not only divisor class. | same owner `#4-sectional-genus-zero-finite-normalization-and-descent`; [arguments/carriers/sectional_genus_zero_normalization_proof.md](../../arguments/carriers/sectional_genus_zero_normalization_proof.md); [arguments/carriers/quartic_scroll_nonreduced_conductors.md](../../arguments/carriers/quartic_scroll_nonreduced_conductors.md); [arguments/curve/veronese_quartic_projections.md](../../arguments/curve/veronese_quartic_projections.md) |
| Nonnormal quartics π = 1 | Actual Cartier double/ribbon nilideal O(−6) is permitted. Fixed center deleting middle coordinate + entire quadratic conductor algebra + all binary quartic root partitions exclude projection/descent; repeated 2+2 needs trace/norm for every power. | same owner `#5-sectional-genus-one-a-permitted-ribbon-with-incompatible-projection`; [arguments/carriers/genus_one_ribbon_conormal_net_proof.md](../../arguments/carriers/genus_one_ribbon_conormal_net_proof.md); [genus_one_ribbon_partition_proofs.md](../../arguments/carriers/genus_one_ribbon_partition_proofs.md); [genus_one_211_projection_proof.md](../../arguments/carriers/genus_one_211_projection_proof.md) |
| Nonnormal quartics π = 2, bisection | ACTUAL Cartier double has nilideal O(−8); no generically nonzero map O(−7)^2→O(−8). This is global embedded Hom obstruction, not mere multiplicity or presumed half-integrality. | same owner `#61-bisection-the-global-nilideal-obstruction`; [arguments/carriers/genus_two_bisection_proof.md](../../arguments/carriers/genus_two_bisection_proof.md) |
| Nonnormal quartics π = 2, section | Entire conductor line and actual ambient blowup lift give genuine trisecant. Three distinct contacts handled by all-length inverse-chain inequality. Triple endpoint and doubled-horizontal case require actual normal coefficients, including roots at infinity, and precise ADE attachment positions. | same owner `#62-section-genuine-trisecants-and-an-all-length-graph-inequality`, `#63-triple-contact-actual-normal-coefficients-replace-an-abstract-graph`; [arguments/carriers/genus_two_nonendpoint_proof.md](../../arguments/carriers/genus_two_nonendpoint_proof.md); [genus_two_endpoint_proof.md](../../arguments/carriers/genus_two_endpoint_proof.md); [genus_two_trisecant_carrier_proof.md](../../arguments/carriers/genus_two_trisecant_carrier_proof.md) |

Preserve that these exhaust NORMAL plus nonnormal π = 0, 1, 2, not three selected quartic examples. All are characteristic-zero claims. Actual quartic-carrier STCI examples exist in every positive characteristic, a mandatory scope control.

### Quintic results and partial reductions

| Scope/result | Exact mechanism/current boundary | Owner/anchor |
|---|---|---|
| All candidate integral quintics: necessary reduction | Actual normal-order bound forces order1; supported pair has b = 4k, generic multiplicity 5k; R-0001 rules out k = 1, so first degree is (5,8). Does NOT bound every mate by 8. One full inverse c ≅ C and c ≡ (4/5)H. | [arguments/carriers/quintic_conormal_and_factor_geometry.md#1-generic-order-compressed-degree-and-the-missing-double-divisor](../../arguments/carriers/quintic_conormal_and_factor_geometry.md#1-generic-order-compressed-degree-and-the-missing-double-divisor) |
| Quintic sectional genus0 | Smooth scrolls impossible because c Cartier would have square 16/5; cone S(0,5) cannot contain the required smooth quartic lift. All mate degrees. | same owner `#9-the-sectional-genus-zero-exclusion-also-passes` |
| Low sectional genus reductions | Rational resolution for π ≤ 3 via ruled-degree/integral-gap criterion. π = 1 forces degree-five A₄ del Pezzo, actual section Q with div(Q)=5c, and every pulled-back mate scalar Q^k. These are source reductions, not alone descent exclusions. | same owner `#5-low-sectional-genus-the-ruled-argument-audited`, `#6-sectional-genus-one-forces-a-single-a4-normalization`; [arguments/carriers/ruled_surface_degree_criterion.md](../../arguments/carriers/ruled_surface_degree_criterion.md) |
| NONNORMAL, Gorenstein normalization: COMPLETE all-degree exclusion | Global Cartier K filter forces π = 1. Entire conductor cases: integral gives contact 8 versus differential degree ≤ 3 and local contact ≤ 2h, including vertex; several components force Q itself to descend; multiplicity-five line splits canonical type 2 (contact bound) and type 1 (tame A4 quotient/valuation contradiction). Every multiplicity retained. | [arguments/carriers/quintic_gorenstein_normalizations.md#integral-conductor-full-contact-exceeds-the-differential-degree](../../arguments/carriers/quintic_gorenstein_normalizations.md#integral-conductor-full-contact-exceeds-the-differential-degree), `#several-conductor-components-force-quartic-descent`, `#a-single-conductor-line-with-multiplicity-five` |
| Toric normalization: COMPLETE all-degree exclusion | Polarized toric source + marked-curve classification exhaust candidates; all admissible relative projection centers have an EXTRA inverse point outside c. No mate power can cure this. Includes finite/one-infinity charts and exceptional M locus, now closed. | [arguments/carriers/quintic_non_gorenstein_toric_sources.md#41-this-is-the-only-remaining-polarized-toric-normalization](../../arguments/carriers/quintic_non_gorenstein_toric_sources.md#41-this-is-the-only-remaining-polarized-toric-normalization), `#42-the-marked-curve-is-unique-up-to-a-source-automorphism`; [arguments/carriers/quintic_toric_center_incidence.md#4-exceptional-finite-loci-and-complete-exclusion](../../arguments/carriers/quintic_toric_center_incidence.md#4-exceptional-finite-loci-and-complete-exclusion) |
| Normal globally ADE quintic, mate degree 8: COMPLETE scoped exclusion | Quasi-étale cover, canonical-map/global budgets, exhaustive ADE data, and LOCATION of symbolic-triple quadratic defect. No reduced-first-symbol hypothesis; no singularity assumption on octic. Non-ADE point anywhere, even away from C, lies outside theorem. | [arguments/carriers/quintic_octic_ade_cover_and_triple.md#1-exact-statement-and-proof-inputs](../../arguments/carriers/quintic_octic_ade_cover_and_triple.md#1-exact-statement-and-proof-inputs) through `#6-the-embedded-triple-obstruction-finishes-the-exclusion`; summary [quintic_octic_surface_constraints.md](../../arguments/carriers/quintic_octic_surface_constraints.md) |
| Earlier reduced-symbol(5,8) proof | Eight budgets leave 4A₁+9A₄; actual integral Picard relation makes four nodes even, branched cover/Noether excludes. Independent narrower proof, not needed as an extra hypothesis of stronger ADE theorem. | [arguments/carriers/quintic_octic_surface_constraints.md#4-the-quintic-rank-bound-and-integral-picard-relation](../../arguments/carriers/quintic_octic_surface_constraints.md#4-the-quintic-rank-bound-and-integral-picard-relation) |
| General(5,8) layer census | Three quotient degrees −7, −6, −5; 308 necessary defect-degree triples. Nonprimitive/nonregular-ratio controls remain. This is NOT308 structures and NOT general(5,8) exclusion. | [arguments/carriers/quintic_conormal_and_factor_geometry.md#3-multiplicity-ten-without-global-primitivity-or-a-regular-ratio](../../arguments/carriers/quintic_conormal_and_factor_geometry.md#3-multiplicity-ten-without-global-primitivity-or-a-regular-ratio) |
| General conductor/differential comparison | For degree a ≥ 5, generically regular carrier with sole-support mate: normalization cannot be smooth along c AND full downstairs conductor smooth at all contacts. Full conductor scheme, not reduced support; singular contacts are real exceptions. | [arguments/carriers/carrier_conductor_differential_comparison.md#exact-statement](../../arguments/carriers/carrier_conductor_differential_comparison.md#exact-statement) and `#the-amount-singular-conductor-contacts-must-supply` |

### What genuinely remains outside the fixed-residual bridge

1. **A selected open is not all lifts of a fixed residual.** The bridge constructs a nonempty actual lift open with the prescribed normal-root and local graph conditions. Exceptional equation coefficients for the same T may make the first-normal form vanish or introduce vertical normal components, nonsimple attached roots, or unverified normalization branches. They are not excluded merely because the residual bidegree matches.
2. **Order1 is not ordinary everywhere.** Quartic generic regularity and quintic order1 give a generic branch, not a nowhere-vanishing first-normal symbol at every point of C. The quartic exceptional/ADE correction budgets and quintic A4 contact data explicitly track special points that an ordinary-root argument can miss.
3. **A hypothetical quintic necessarily has a singular normalization point on c.** If normalization were smooth along c, c would be Cartier and its self-intersection 16/5 would be integral, impossible. This follows from the existing necessary relation. It explains why a smooth-along-c open cannot settle the quintic exceptions. The fixed-residual bridge only checks its own local model, not all those possible singularities.
4. **Full inverse support is prior to numerical capacity.** Toric projection extra inverse points already obstruct every mate, regardless of whether numerical branch/capacity data look plausible. The marked divisorial inverse alone must not replace the full inverse scheme/support.
5. **Conductor is not residual quadric section.** Nonreduced conductor gluing and nonreduced T are different objects. The new weighted bridge handles certain repeated residual components; it does not establish that Q^k descends through a nonnormal carrier's conductor. Quartic/genus1 and quintic/A4 proofs remain indispensable.
6. **Finite normalization is not a resolution.** Exceptional root matrices and divisor compression live on resolutions with hyperplane-null curves; the bridge's residual curves have positive degree on finite normalization. Keep their intersection theories and equality conditions distinct.
7. **Normal non-ADE and non-toric non-Gorenstein quintics remain open under this list.** For normal quintics, π = 6 satisfies the Gorenstein genus filter; the nonnormal Gorenstein theorem cannot be applied merely because every hypersurface is Gorenstein. Do not relabel these as excluded by the generic bridge.

### Genuine combinations worth recording, not new claims

* **Bridge first; exceptional assembly second.** Use actual source/normal-root conditions to dispatch the verified lift open, then classify the closed complement by the existing first-normal defects. This can organize quartic proof geography without discarding its exhaustive classification or claiming the same closure for quintics.
* **Capacity + full inverse + descent are sequential filters.** First discard extra inverse points (toric mechanism), then test residual capacity on a supplied normalization, then apply full-conductor descent only to surviving numerical divisors. Passing any one filter is not realization.
* **Local singularity analysis can repair capacity hypotheses.** Existing A_n/A4 actual-ideal and Q-Cartier calculations are useful to determine whether a proposed residual component on a singular normalization has a valid rational intersection and the correct q multiplicity. The computation must concern the actual residual component; an exceptional Cartan graph alone does not identify it.
* **Conductor/differential inequalities can address a capacity-exception stratum**, provided generic regularity/full inverse and the precise smooth/singular-contact hypotheses are verified. The successful quintic proof shows how a vertex first-jet computation restores the total 8 ≤ 6 contradiction; it is a model for handling an exception, not a universal vertex lemma.
* **Actual ideal vanishing versus numerical correction** is a common robust interface: quartic TypeD closes via maximal ideal O(−E), the final reduced cycle via ideal defect, and quintic A4 via full cotangent first jet. These are promising reusable INPUT tests to the bridge, not consequences of numerical negativity.



## Cross-framework interfaces

The following distinguish established comparisons from the further maps or
bounds still needed. See the [open-item list](open-items.md) for re-entry decisions.

| Interface | What is already shared | What would make it a genuine bridge |
| --- | --- | --- |
| **Toric endpoint structure ↔ quadratic conductor** (KG01) | Endpoint capacities and global postulation constrain the same conductor. The [selected-graph identity](../../arguments/linkage/toric_limit_conductor_comparison.md) compares original and pure-limit lengths using both embedded corrections. [R-0078](../../results/moving_quadratic_conductors.md) narrows the smooth-carrier scalar test to exceptional slope parameters and gives a one-point homogeneous-kernel test. | Control the embedded corrections from actual global equations, or detect an extra low-degree form in the one-point kernel. For the fixed-endpoint scalar test only exceptional smooth parameters and singular-endpoint lattices remain; the osculating-cover scalar bound already fails to exclude every generically regular smaller carrier. None of these limitations decides the corrected torus comparison. |
| **Normalization ↔ deep normal contact** (KG04/KG01) | Both measure contact for actual forms. Normalization bounds the weighted valuation sum for a chosen carrier; the infinitely-near contact formula computes that same generic length via the two equations. [Capacity](../../arguments/curve/normalization_residual_capacity.md) · [Depth budget](../../arguments/residuals/generic_contact_depth.md). | On one exceptional lift, match a specified higher-contact contribution to a term in a divisor capacity bound. A tangent symbol by itself is not the next contact contribution; use the documented fixed-tangent controls. |
| **Intrinsic boundary loss ↔ normalized divisor capacity** (KG04) | The corrected ample class and the fixed-sextic valuation loss identity both bound contact, but one uses a complete projective divisor and the other pole data in an explicit affine normalization. [Capacity](../../arguments/curve/normalization_residual_capacity.md) · [Fixed-sextic loss identity](../../results/ci_fixed_sextic_jet_rigidity.md). | On one carrier where both tests can be computed, compare their weights and equality defects. Determine which information survives at the boundary when the projective correction cannot be constructed. Agreement on a bound does not imply the defects coincide. |
| **Local lifting ↔ actual equations** (KG01/KG07/KG08/KG09) | Exact quadric restrictions identify actual sources; moving relations, spectral obstructions, and common-ancestor duality each see additional compatibility. [Actual jets](../../arguments/equations/global_equation_jets.md) · [Moving relations](../../arguments/equations/global_lifting_interfaces.md) · [Sextic ADE](../../arguments/carriers/sextic_ade_reduction.md) · [Root lifts](../../frameworks/spectral-roots/open_root_lifts.md) · [Dual persistence](../../arguments/local-cohomology/polynomial_duals_and_affine_pencils.md). | Construct a comparison on a common, specified actual source which detects the same obstruction class or explains its kernel; matching dimensions and labels are not enough. The gap between actual sextic symbols and the order-five Čech filtration is the natural bounded comparison, not an immediate all-degree claim. |
| **Actual Chow arrangements ↔ full torus limits** (KG02) | The [general first moment](../../arguments/torus/chow_arrangement_moments.md) separates the Chow closure of invariant CI cycles, including reduced arrangements, from complete collision in characteristic zero. The [fixed-carrier theorem](../../arguments/torus/fixed_carrier_chow_arrangements.md) gives finer strata and partial collisions. | Understand non-invariant CI lifts over repeated cycles and their deformations; smoothing into distinct translates is not automatic. [Equation layers](../../arguments/torus/chow_matched_equation_layers.md) retain information lost by cycles. A residual bound still needs joint actual sources, which fixed extremes and the CI polynomial do not determine. |
| **Inverse support and descent ↔ a constructive endpoint** (KG03/KG05/KG06) | Carrier geometry, the elliptic inverse scheme, and the absorption model each distinguish a supported object from an actual descended equation or pair. [Elliptic support](../../results/elliptic_inverse_support.md) · [Conductor cases](../../frameworks/carrier-normalization/open_carrier_cases.md) · [Marked absorption](../../arguments/residuals/marked_deformation_and_absorption.md). | Compare the conductor or graded source conditions on a single surviving model. To use an absorption direction, lift it to both ambient equations and check properness and the entire residual cycle. A supported inverse set or a smaller residual is not a constructed STCI pair. |
| **Arithmetic ↔ a characteristic-zero obstruction** (KG10) | Known nonlifting and endpoint tests attach to a specified model or family. [Arithmetic framework](../../frameworks/arithmetic-supported-lifts/index.md). | Identify data intrinsic under change of the two ambient equations, then prove a coverage statement for reductions of hypothetical pairs. Do not identify endpoint torsion with conductor classes or spectral Picard torsion without a comparison. |

## Established comparisons and remaining gaps

The [common-quadric boundary](../../arguments/equations/common_quadric_chow_boundary.md)
now identifies the full special scheme for coprime cofactors and nonzero
first cancellation, including some restriction rank drops. Near the regular
cofactor locus it identifies the resultant base ideal as the square of the
center ideal and its graph as the ordinary blowup, in every degree and characteristic.
Its balanced effective quadric subcycle excludes constant sole support even
at restriction rank drops under those cofactor/cancellation hypotheses.
Source and graph classification there, deeper cancellation, common cofactors
and closure of varying translated arrangements remain open. Separately,
the [actual-pair coregularity module](../../arguments/local-cohomology/actual_pair_coregularity.md)
is \(H_I^1(S/(f,g))(\deg f)\) under the stated assumptions. The
remaining comparison is from actual filtered equations to this module,
not direct higher local cohomology of an already supported conductor.

These statements retain their actual-source hypotheses. A shared numerical
budget or related terminology does not supply a missing comparison map.

### Positive restrictions and transport

- [Elliptic inverse and descent](../../arguments/carriers/elliptic_double_inverse_construction.md#an-intersection-bound-and-the-missing-descent-step):
  the conormal pencil bounds the marked intersection by six, improving
  to four for birational octics. The generic split branches there are
  transverse, excluding conductor coefficient five, and no mate of
  degree at most five exists. Full inverse support and higher-degree
  descent at the remaining divisorial conductor images are open.
  The [vertical-divisor identities](../../arguments/carriers/elliptic_double_inverse_construction.md#the-vertical-divisor-counts-the-residual-inverse-scheme)
  count the whole inverse scheme with multiplicity and relate it to
  the residual conductor on the marked double cover.
  For a support survivor in the integral residual-curve scope, the
  [length-eight residual conductor test](../../arguments/carriers/elliptic_double_inverse_construction.md#a-finite-descent-test-on-the-residual-quadric-curve)
  gives a finite necessary descent check before any ambient search.
  The [normalization of the meeting norm divisor](../../arguments/carriers/elliptic_double_inverse_construction.md#the-meeting-norm-divisor-and-its-normalization)
  parametrizes the support search and locates degrees six through
  twelve on its singular locus. An actual meeting fiber fails full
  support, so the closed full-support locus has dimension at most three;
  whether it is empty remains open.
  See the [normalization gates](../../frameworks/carrier-normalization/open_carrier_cases.md).
- [Normal symbols and the cubic contraction](../../results/connected_normal_directions.md#what-the-cubic-contraction-misses-in-the-attachment-count):
  the joint bound charges the residual degree visible on \(V_5\).
  A wholly contracted sextic residual has symbol count only one, so
  contraction is not exhaustive attachment. See the
  [actual-contact gate](knowledge-gain-priorities.md#kg01-projective-limits-on-deep-generic-normal-contact).
- [Local cohomology and the contact flag](../../arguments/local-cohomology/polynomial_duals_and_affine_pencils.md#a-target-preserving-quadric-shift-of-actual-contact-sources):
  quadric division transports target values and stabilizes the image
  along a specified ray. The first quartic shift has at most five new
  source directions; determining their actual products remains open.

The [Chow-fiber realization viewpoint](../../arguments/equations/chow_polytope_rigidity.md#from-the-cycle-fiber-to-actual-complete-intersections)
separates cycle collisions, Hilbert lifts and actual proper pairs.
The elliptic norm is a model of stratifying a fixed incidence family,
not an identification of the two parameter spaces.

### Nonreconstruction examples

- [Opposite limits and actual contact](../../arguments/torus/chow_matched_equation_layers.md#opposite-limits-do-not-recover-actual-contact):
  two proper pencils have the same full opposite initials and no raw
  parameter torsion, but different actual contact. Neither is
  Chow-matched or sole-supported. A comparison should retain the joint
  actual-source filtration; the marked-shear criterion describes which
  changes of equations preserve its lower contact thresholds.
- [Binary determinant and canonical layers](../../arguments/torus/chow_matched_equation_layers.md#a-binary-determinant-index-and-what-it-does-not-recover):
  a canonical determinant measures a finite restriction index. Three
  controls fix both indices, the extreme weights and the cycle but
  vary the canonical line layers. The
  [weighted-source gate](knowledge-gain-priorities.md#kg02-actual-chow-arrangements-collisions-and-full-torus-limits)
  remains a module-level comparison, not a search for another scalar.

### Family-specific controls

- [Branch jumps and marked absorption](../../arguments/residuals/marked_deformation_and_absorption.md#a-fixed-carrier-pencil-has-finitely-many-branch-order-jumps):
  each inverse branch contributes at most one jump parameter in a
  fixed-carrier pencil, and the mixed sextic realizes both jumps.
  Separately, the twelvefold residual moves on the thick quadric
  without passing its fixed-carrier degree floor. Neither constructs
  a sole-support pair.

## How to use the audit

1. Use the shared obstruction or realization gate as the unit of comparison,
   rather than choosing a paper, a matrix, or a new low-degree case.
2. Keep the exact known scope and strongest counterexample beside each gate.
   Record a failed comparison when it isolates a real missing hypothesis.
3. Promote a proof-replacement item only when it removes a hypothesis,
   transfers a mechanism, or reveals what the finite test measures. Keep
   exact certificates that carry extra scheme or characteristic information.
4. Select among these directions after reviewing the consolidated list;
   this audit does not commit the project to completing the low-degree
   exception cases one at a time.

