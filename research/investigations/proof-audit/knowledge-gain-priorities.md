# Proof priorities by potential knowledge gain

**Status:** The sole strategic ranking of current research questions, not a new Result. Start at the [active front door](open-items.md) for the overall organization; use the canonical proof/framework owners for mathematical status. The [proof-dependency workbench](README.md) supports specific explanatory improvements, not a competing queue. A short coordinate-free proof can rank low here, while a proof retaining a small exact calculation can rank high.

## Ranking rule and coverage

The problem is whether the **fixed** quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) is a set-theoretic complete
intersection in characteristic zero. A proper pair of degrees \(a,b\)
has \(ab=4m_C+\deg R\). Knowledge includes the geometry of actual pairs,
their cycle arrangements, parameter spaces and limits, as well as constructions
and obstructions. Examples, counterexamples and better formulations can reveal
which questions matter before a bridge to an STCI theorem is known. The degree
identity alone does not explain this geometry.

The order favors expected mathematical knowledge, transfer between
approaches, and a concrete realization or coverage bridge. Readiness
and cost are separate. Nearness to an STCI solution affects the ranking
only if the remaining gap is demonstrably small; no lane below is
known to have such a gap. An exact counterexample may outrank an
additional positive case when it changes which comparison to attempt.

Compare the actual next investigations, not the historical importance of their
frameworks. A restricted scalar test does not inherit the coverage of the whole
deep-contact program. The current choice follows the quartic-pencil
classification to the two-translate sextic criterion below. That
criterion gives a concrete construction test, with nonemptiness still
open. Reassess against the elliptic support locus after the initial
sextic probe.

## Ranked research problems

| Rank | Stable ID | Question for a better argument | Payoff if resolved |
| --- | --- | --- | --- |
| 1 | KG02 | What arrangements and collision strata occur for actual pairs, and what changes when the carrier moves? | Geometry of the realization locus, including repeated cycles and non-invariant ideals |
| 2 | KG05 | Can the whole elliptic inverse scheme be supported and descend? | An explicit finite-algebra family with a precise unresolved support locus |
| 3 | KG01 | What do full toric limits and their embedded corrections say about the same quadratic conductor? | A local/global comparison retaining the information lost by taking pure limits |
| 4 | KG03 | When does a marked absorption direction lift to a proper ambient pair and increase marked length? | A constructive operation or the class obstructing it, not just motion of a residual |
| 5 | KG04 | Can residual-capacity tests reach carriers outside the known ordinary open? | Transfer capacity mechanisms to new actual carriers |
| 6 | KG06 | What replaces Cartier descent on the surviving quintic normalizations? | Test the intrinsic Cartier defect and contact geometry on actual carriers |
| 7 | KG08 | What survives the full quadratic-root obstruction and actual-source incidence? | Distinguish spectral obstructions from lack of global lifts |
| 8 | KG09 | Which changes preserve an actual two-target dual separator? | A source-transfer problem with an exact five-direction first test |
| 9 | KG10 | What obstruction survives arithmetic specialization of varying pairs? | Transfer across characteristics if actual lattices and coverage can be controlled |
| 10 | KG07 | Do the remaining actual ADE sextic pencils reach length nine? | A useful fixed-degree stress test, not the lead mechanism |

### KG01. Projective limits on deep generic normal contact

- **Current comparison.** The [same quadratic conductor](../../arguments/linkage/quadratic_covers_and_conductor_descent.md#82-endpoint-capacity-and-fixed-cover-carrier-exclusions)
  has a global postulation lower bound and two actual endpoint-lattice
  capacities. This compares local and global constraints on one object.
  The [weighted endpoint test](../../arguments/linkage/endpoint_lattice_capacity.md#a-weighted-endpoint-test-on-the-actual-carrier)
  excludes all mate degrees on specified nonempty integral carrier families
  in degrees five and higher; the simultaneous source has more than a
  pencil's worth of parameters. These exclusions do not cover arbitrary
  carriers.
- **Coverage after choosing the cover.** Every integral carrier of degree
  greater than two is nonsplit for a general member of the auxiliary
  quadratic-cover pencil in characteristic different from two. Thus the
  [nonsplit postulation onset](../../arguments/linkage/quadratic_cover_choice.md)
  is available after a carrier-dependent choice. In this characteristic-zero
  comparison, both the conormal-moment and uniform all-minors upper bounds
  apply to that same conductor. The actual endpoint
  divisibilities, Smith capacities and conductor lengths can change with
  the cover; favorable estimates in one member do not transfer to another.
- **Fixed-cover closures.** For the fixed cover, all two-lift integral
  split sextics are excluded in every mate degree, without normality of
  the signed cubic. The one-lift sector is excluded when that surface
  is smooth or Du Val along the lift, and the
  [unique generically singular signed cubic](../../arguments/linkage/signed_cubic_normalization_and_cartier_defect.md)
  is also excluded by its full normalization inverse. A surviving
  one-lift signed cubic must be generically regular along the lift and
  have non-Du-Val behavior somewhere on it. Without requiring normality,
  the actual mate and Cohen–Macaulay structure force the symbolic defect
  strata \(g\in\{5,6,8\}\), with some least principal symbolic index
  divisible by three. These are necessary strata for these signed cubics,
  not exclusions of the strata or a classification of
  all sextics or of split first normal cones. See the
  [carrier framework](../../frameworks/carrier-normalization/index.md#quadratic-cover-exclusions-and-the-remaining-one-lift-sector).
- **Settled transverse stratum.** The [actual cyclic control](../../arguments/linkage/endpoint_lattice_capacity.md#transverse-endpoints-throughout-the-cover-pencil)
  gives endpoint capacity \(n(n-1)\), \(n=ab/4\), for every allowed cover
  if some pair member is smooth and transverse to the cover's endpoint
  covector. Even one such endpoint exceeds the displayed scalar
  postulation lower bound. Varying the cover cannot give a contradiction
  from that comparison on this stratum.
- **Smooth-source scalar decision.** The [full smooth-carrier calculation](../../arguments/linkage/conductor_on_a_smooth_carrier.md)
  answers the broad cover-variation question: a dense open of the actual
  smaller-carrier source defeats the scalar comparison for every allowed
  nonsplit cover and mate degree. A deficit requires tangency to the
  containing quadric at both endpoints. For degree at least six the two
  conormal slopes must agree and be nonzero, leaving at most one candidate
  cover; in degree five there are at most two. The restricted remaining test
  is the higher coefficients and nonsplitting at these candidates, or the
  full lattices at singular endpoints. First-symbol data do not decide
  those remaining cases.
- **One-point embedded test.** The [moving-conductor theorem](../../results/moving_quadratic_conductors.md)
  places the entire boundary at one general point. Its Hilbert-function
  upper estimate exceeds the scalar lower bound for every generic
  transverse Hilbert function in scope; on a generically regular smaller
  carrier even the exact length exceeds it. The further test is therefore
  the kernel on actual homogeneous forms, not another comparison of those
  two scalar estimates. On a declared candidate thickening, an independent
  kernel form in degree \(2d+2<b\) would obstruct the proposed mate.
  Every integral quintic is generically regular, so this closes its
  moving scalar test as well. The exceptional osculating ribbon has a
  nonzero primitive-triple class; a compatible higher flag needs at least
  degree-two defect, and an actual generically regular osculating CI
  supplies that flag. The complete triple classification gives a projective
  line at degree two, a determinant condition at degree three, and every
  defect divisor from degree four onward. Thus higher defect placement
  alone supplies no further obstruction. These triples are non-Gorenstein
  at their defects; their higher embedded extensions and actual homogeneous
  sources remain uncomputed. On a fully Gorenstein-admissible completion,
  the [top-socle source vanishing](../../arguments/one_step_boundary_repair.md#exact-fixed-surface-criterion-when-the-top-layer-has-no-source-sections)
  makes the final determinant automatic for \(a,b\ge4\); the remaining
  source test is nonzero section spaces with no common fixed surface.
- **Next exploratory comparison.** In a simultaneous intrinsic torus limit of
  the curve and its selected quadratic graph, the [conductor identity](../../arguments/linkage/toric_limit_conductor_comparison.md)
  is \(\delta_i^{\mathrm{pure}}=\delta_i+\alpha_i-\beta_i\).
  The full base limit supplies \(\alpha_i\); the graph's embedded correction
  \(\beta_i\) must also be computed. Determine what actual global equations
  force on their difference, beginning with a source where both can be
  calculated. The controls show either sign is possible. This corrected
  degeneration question is not restricted to the nontransverse scalar stratum;
  neither a pure limit nor a local control inherits the original global CI
  postulation theorem automatically.
  The [moving-cover graph at the endpoint](../../arguments/linkage/moving_quadratic_covers.md#the-flat-graph-at-the-endpoint)
  now gives a global fixed-source control: \(\alpha=0\),
  \(\beta=\delta_{\rm generic}\), and pure conductor zero. Substitution
  in the limiting square quadric loses exactly that punctual torsion;
  this is not a bound for arbitrary toric graph families.
- **Decision.** A strict gap on an exceptional source, or an extra
  homogeneous kernel form, would extend the exclusions beyond the
  constructed endpoint-jet families. The broad smooth-source scalar
  question is settled negatively; repeating it adds no coverage. The
  corrected torus comparison remains the exploratory task here because it
  retains embedded information beyond those scalar lengths. The one-point
  map offers another concrete test once a candidate thickening is supplied;
  neither supplies a universal obstruction. The two-lift sextic primary-piece
  calculation is an explanatory control in a closed sector, not a search
  for a surviving mate. The transverse limitation concerns the displayed
  scalar bound; it does not decide stronger postulation information or
  construct a supported pair.

The related deep-contact mechanisms retain their distinct scopes:
[connected normal directions](../../results/connected_normal_directions.md#statement)
force contact beyond depth one (and beyond depth two on the zero
direction-degree boundary); the
[moving-relation theorem](../../arguments/equations/global_lifting_interfaces.md#a-uniform-nonvanishing-theorem-in-relation-degree-at-least-two)
controls saturated degree-one movement with relation degree at least two
and no independent next relation. Nonsaturation and higher order-one
lifts remain with their [formal-normal owner](../../frameworks/formal-normal-geometry/index.md).
The [marked V5 correspondence](../../arguments/residuals/blowup_residual_geometry.md#actual-equations-on-the-zero-direction-edge)
is a separate actual-source and conductor-contact test. These results
neither supply a capacity bound for every cover nor remove its need.

### KG02. Actual Chow arrangements, collisions and full torus limits

The [clean common-quadric theorem](../../arguments/equations/common_quadric_chow_boundary.md)
settles one boundary chart in every degree: its full special scheme has
a balanced effective quadric subcycle forbidding constant sole support
under coprime cofactors and nonzero first cancellation, including restriction
rank drops. For nonzero cofactor restrictions with gcd class \((h_1,h_2)\),
the normal cancellation image is explicit and the kernel has dimension
\((h_1+2)h_2\). When \(h_2=0\), the ordinary-blowup graph and exact
squared center ideal include common trisecant ruling factors and all
higher-contact arcs. These center points lie outside the closure of the
fixed-degree sole-support locus. At \(h_2>0\) the square-ideal model
fails; its higher-order replacement, zero restrictions and common ambient
cofactors remain open. If a cofactor does not contain \(C\), the reduced
base is still locally the same center, so the missing information is
infinitesimal. Closure of varying translate arrangements remains a separate
question; exclusion from the exact Chow-polytope fibre does not settle it.

- **General cycle constraint.** The [trace-moment theorem](../../arguments/torus/chow_arrangement_moments.md)
  forces \(\sum_i n_i u_i/v_i=0\) for pairs with an eigenform generator
  or the specified actual congruences, including invariant CI ideals and
  every reduced CI arrangement, in characteristic different from two. Its
  linear Chow-coefficient equation separates the entire Chow closure of
  that locus from every \(m[C_{u,v}]\) in characteristic zero. This closes
  the proposed path from distinct-translate CIs to full coalescence even if
  the limiting ideal were allowed to cease being a CI. It does not exclude
  non-invariant CI lifts over repeated cycles outside that closure.
- **Realization geometry.** The [fixed-carrier classification](../../arguments/torus/fixed_carrier_chow_arrangements.md)
  describes every mate on the named quartic toric carrier by a monic root
  polynomial with \(c_1=c_2=c_5=0\) and nonzero constant coefficient.
  In characteristic zero at least three distinct translates remain, but partial
  collisions with \(C\) occur. Root-of-unity arrangements are a special locus.
  On the smooth quadric, the divisor classes instead forbid a mate made only
  of these translates. Fixed-carrier incidence is therefore already informative
  without a general exclusion. Reduced CI arrangements on the quartic are
  covered; a repeated cycle supported there need not have that carrier as an
  actual equation.
  Uniqueness makes every classified fixed-generator ideal invariant, even
  with repeated roots. A non-invariant lift supported on this surface must
  therefore lose the quartic as an actual equation.

- **Known.** Opposite completed ends detect raw parameter torsion; on
  a layer the common kernel is the \((x_0,x_3)\)-power torsion. The
  exact first-layer bound is \(\deg R\ge e_L-\text{missed generic
  length}\) when the stripped extremes have the disjoint line of
  multiplicity \(e_L\). There are actual examples of nonzero classes
  missed by **both** ends. A cycle, splitting profile, or Hilbert
  polynomial alone does not supply the moving generators.
  [R-0073](../../results/endpoint_equation_torsion.md#statement)
  · [Moving comparison](../quotient-hilbert-comparison/index.md#relation-persistence-control-and-remaining-bridge)
  · [Generator incidence](../supported-generator-incidence/index.md).
- **Checked finite pilot.** The [two-parameter residual sextic family](../../results/endpoint_equation_torsion.md#the-complete-detection-stratification-of-a-two-parameter-pilot) has fixed extremes, \(e_L=1\), and a fixed CI polynomial, but its missed length is one on the dense parameter open and zero on a parameter divisor where the flat limit contains \(6[L]\). This exactly identifies the detection strata of that family. It shows why those shared data alone cannot provide the needed strict bound; it is not a supported construction or a closure of KG02.
- **Canonical-source refinement.** The [equation-layer theorem](../../arguments/torus/chow_matched_equation_layers.md) makes each end-adapted raw ideal intrinsic and shows that nonadaptation delays all hidden line layers. The explicit first-length change eight to zero is a generator artifact, not erased cancellation. Endpoint Kummer data alone do not determine that raw first length; opposite optimized generators need not be the same representative. The whole filtered degree-labeled sources of the same ideal are the revised comparison target.
- **Moving-carrier comparison.** [R-0079](../../results/quartic_chow_pencil_classification.md)
  settles all actual \((4,4)\) pencils **in characteristic zero**.
  The explicit characteristic-two sole-support construction is
  separate; full positive-characteristic quartic uniqueness
  is not asserted. Each exceptional
  \(2[C_{u,v}]+2[C_{u,-v}]\) has a non-invariant orbit outside the invariant
  quartic Chow closure, with the same vanishing first moment and opposite
  embedded endpoint corrections of length two. On a
  [retained exceptional carrier](../../arguments/torus/quartic_exceptional_carrier_geometry.md#all-mate-degrees-on-a-retained-exceptional-carrier)
  all translated mates are powers modulo that carrier, in degrees divisible
  by four. Changing the mate degree on this carrier preserves the equal
  multiplicities.
- **Equation-side tests.** The [one-carrier trace tower](../../arguments/torus/chow_trace_cone_jets.md)
  constrains arbitrary-degree presentations without requiring an invariant
  ideal. The [relative different](../../arguments/torus/chow_endpoint_different.md)
  detects support count and normalization colength from the actual endpoint
  algebra. Its value on a given pair provides a test for sole support,
  with no global inequality yet ruling out that value in higher degrees.
- **Geometric explanation in degree four.** The
  [exceptional quartic proof](../../arguments/torus/quartic_exceptional_carrier_geometry.md#two-sided-contact-and-the-nodal-even-eight-carrier)
  identifies its support by coincident cubic jets at **both** endpoints
  and exhibits a ten-nodal quartic K3 resolution with an exact
  eight-exceptional-curve divisibility relation. This gives the
  nontrivial two-torsion Weil class responsible for doubled divisors
  on a fixed carrier. The
  [Hilbert--Burch normal-map locus](../../arguments/torus/quartic_chow_pencils.md#hilbert--burch-and-first-normal-interpretation)
  is now classified among **proper quartic pencils**
  by geometric methods after a torus-coordinate
  support reduction. The
  [residual-linkage argument](../../arguments/torus/quartic_chow_pencils.md#residual-genus-excludes-the-triple-branches)
  eliminates \((3,1)\) and \((1,3)\) because a
  degree-eight genus-seven double of a smooth quartic
  would require a conormal quotient \(\mathcal O(-8)\)
  of \(\mathcal O(-7)^{\oplus2}\). The
  [canonical-module argument](../../arguments/torus/quartic_chow_pencils.md#canonical-module-rigidity-of-the-pencil)
  forces the \(\lambda\)-orbit: the
  [direct \((3,3)\) linkage](../../arguments/torus/quartic_chow_pencils.md#the-residual-line-and-the-canonical-module)
  to that residual line gives
  \(\omega_Y(-2)\simeq I_{L_{\mathrm{res}}}/(A,B)\),
  so the line **both presents the canonical module
  and forces its global generators**. Thus the
  classification of actual quartic generators
  is complete in characteristic zero. The
  geometric proof has received a scoped independent
  correctness reconstruction; it does not by itself
  resolve the separate full-perspective review.
  Neither the abstract Ferrand construction nor the
  even-eight class alone establishes uniqueness. The same
  [quartic family](../../arguments/torus/quartic_hilbert_chow_limits.md#hilbert-over-chow-and-the-characteristic-two-collision)
  supplies an \(H\)-orbit of Hilbert points over
  one Chow point, with a normalized \(\mathbf P^1\)
  compactification whose two embedded endpoint
  limits differ from the two improper Grassmannian
  pencil limits. On the normal nodal carrier the
  [Nikulin cover](../../arguments/torus/quartic_exceptional_carrier_geometry.md#the-nikulin-double-cover-and-a-square-root-of-the-mate)
  exhibits the mate as a square and the even-eight
  class recovers parity of its mate multiplicities.
  The characteristic-two construction remains
  a distinct non-invariant single-support
  \((4,4)\) specialization.
  The state-polytope comparison has not been explicitly computed.
- **Corrected two-translate sextic criterion.** A proper \((6,6)\)
  pair supported on \(C_{1,\pm1}\), with an integral carrier invariant
  under \(x_3\mapsto-x_3\), would yield an STCI if the two
  multiplicities differ. They total nine, but the
  [involution--Bézout inequality](../../arguments/torus/fixed_surface_restriction_lifts.md#involution--bezout-bound-and-the-remaining-sextic-locus)
  \(4|n_+-n_-|\ge6\) **excludes \((5,4)\)**.
  The degree-independent inequality requires that the carrier be
  **regular at both supported generic points**; this is proved
  separately for the integral symmetric sextic by the first-normal
  and Hilbert--Burch argument. Only
  \((6,3),(7,2),(8,1)\) and reversals remain with both components.
  The primitive orbit-lattice construction sharpens their consequences:
  \((6,3)\) would yield a degree-six sole-support mate (multiplicity
  nine), while \((7,2)\) and \((8,1)\) yield mate degrees
  (30) and (42), respectively. Thus the first surviving partition
  would already give an actual \((6,6)\) STCI.
  The same argument together with the local
  \(\mathbf Z/2\) divisor class **excludes every such pair
  on a carrier with only ordinary nodes**. The surviving search
  must use more complicated singularities on the quartics.
- **Narrower singular-carrier geometry.** For a normal Du Val sextic,
  the [local class-group and global correction tests](../../arguments/torus/fixed_surface_restriction_lifts.md#ade-local-classes-and-the-global-sextic-correction-budget)
  require off-endpoint odd-order classes (if those singularities occur):
  \(A_{3m-1}\) or \(E_6\) for difference three,
  \(A_{5m-1}\) for difference five, and
  \(A_{7m-1}\) for difference seven. At the endpoints it is
  the **difference of the two branch classes** that must have the
  required order. The rational divisor classes are
  \([C_\pm]=\tfrac23H\), imposing
  \(-Z_+^2=-Z_-^2=38/3\) on the crepant
  resolution. For the \((7,2)\) and \((8,1)\)
  partitions, the [ADE discriminant-form
  denominator test](../../arguments/torus/fixed_surface_restriction_lifts.md#ade-local-classes-and-the-global-sextic-correction-budget)
  additionally forces a common endpoint of type
  \(A_{3m-1}\) or \(E_6\), carrying matching
  nontrivial 3-primary classes of both curves.
  These conditions are necessary, not a construction
  or a general exclusion. A useful next comparison is the simultaneous local
  anti-invariant classes, available odd-torsion singularities and
  the two exceptional-lattice budgets, before testing additional
  homogeneous coefficient families.
- **Remaining equation bridge.** The joint first-layer kernel on a declared
  proper family with \(e_L>0\) remains a distinct question. A bound below
  \(e_L\) would force residual degree there; retain canonical end-adapted
  sources and higher layers. The \(W_0\) control prevents inferring this
  bound from a cycle, a single limit or the shared CI polynomial.

### KG03. Globalizing a marked absorption step

- **Chow control.** The [fixed-quartic collision family](../../arguments/torus/fixed_carrier_chow_arrangements.md#an-actual-partial-collision-in-characteristic-zero)
  is an actual flat family of proper pairs in which marked multiplicity rises
  from one to two and residual degree falls from twelve to eight. Eight is the
  sharp residual floor within this fixed-generator \((4,4)\) translated-cycle
  locus. It provides a realized partial absorption step, not an unrestricted
  iteration or a sole-supported family for the quadratic-graph comparison.
- **Known.** Proper actual families can absorb positive residual degree.
  In R-0049 a moving quartic is absorbed, but a twelvefold residual
  line persists. The marked Quot model separates deforming the marked
  object, lifting its two equations and maintaining properness.
  At a hypothetical endpoint one sufficient embedding vanishing is
  unavailable; the nonzero obstruction **space** is not an obstruction
  class. [R-0049](../../results/sextic_residual_absorption.md)
  · [Marked equation incidence and limits](../../arguments/residuals/marked_deformation_and_absorption.md#7-partial-absorption-and-the-missing-passage-to-sole-support).
- **Scope sharpened.** The [moving twelvefold line](../../arguments/residuals/marked_deformation_and_absorption.md#the-twelvefold-residual-moves-on-the-thick-quadric)
  moves on a fixed carrier but cannot lower the residual degree there.
  A meaningful next step changes the permitted actual equation pair
  and checks the whole residual, not inverse support or line motion alone.
- **First test.** Start with a specified actual proper pair and
  residual component, preferably the twelvefold line control. Compute
  a marked deformation direction that changes the residual component
  and maps to the actual homogeneous two-equation source; compare with
  the full attachment module or prove its obstruction there. Record
  what happens to the generic multiplicity and the full residual cycle
  in the same deformation.
- **Decision.** A reproducible absorption operation preserving actual
  presentations, with a monotone degree budget reaching zero, would
  be a construction. A detected obstruction class gives an informative
  route-specific limit. Adding more twisting, finding local motion,
  or reducing one component is not termination.

### KG04. Residual capacity outside the ordinary open

- **Known.** The [negative-curve correction](../../arguments/curve/normalization_residual_capacity.md)
  annihilates verified negative residual curves and gives the sharp
  half-contact bound on the specified generic single-branch open.
  The split graded family admits a componentwise version. The
  [R-0025 loss identity](../../results/ci_fixed_sextic_jet_rigidity.md)
  instead uses a positive weighted boundary valuation on an actual
  affine-normalization ring. Neither proves the required hypotheses
  on the special closed complement.
- **Checked extension.** The [weighted fixed-residual theorem](../../arguments/curve/normalization_residual_capacity.md#weighted-fixed-quadric-residuals-arbitrary-effective-fixed-divisors) constructs a nonempty actual lifting open for every effective fixed quadric residual of the specified class with no C component, including repeated components, tangencies and shared attachments. It verifies the normalized divisor and local intersections, permits Q-Cartier residuals, and proves the full weighted matrix negative definite by Hodge index on the smooth quadric. Componentwise ruling imbalance is no longer required. Sharp half-contact and even-degree rigidity hold on these opens, not on all lifts of a given residual.
- **Completed pilot.** The [degree-seven, order-two example](../../arguments/curve/normalization_residual_capacity.md#the-degree-seven-pilot-including-the-crossing) is included; repeating its crossing matrix or finding a balanced component inside the now-covered fixed-residual geometry is not the next investigation.
- **Next gate.** Identify an actual exceptional lift where the normal-root/simple quadric-direction-root condition, complete normalized inverse divisor, Q-Cartier status, or local graph/intersection identification fails. Determine which failure prevents a capacity argument before testing an alternative divisor or a verified weighted boundary certificate. Repeated residuals, tangencies and shared attachments by themselves are not failures. A resolution introduces hyperplane-null curves and is not a substitute for the finite normalization without checking their contribution.
- **Decision.** A strict capacity gap on a genuinely new carrier stratum excludes every mate degree there; a precise failure of a sufficient hypothesis identifies the method's boundary, not an existing mate or an automatic obstruction to realization. No exceptional lift classification is claimed by the preservation theorem.

### KG05. Full inverse support and descent for the elliptic family

- **Known.** The smooth basepoint-free birational fibers of the
  five-parameter elliptic double-inverse construction have an exact
  length-twelve residual support test. A specified characteristic-zero
  line is excluded, not the whole parameter space. A suitable pure
  power must still descend through the actual four projection sections.
  [Support criterion](../../results/elliptic_inverse_support.md)
  · [Family and descent](../../arguments/carriers/elliptic_double_inverse_construction.md#5-fiberwise-support-and-actual-descending-equations)
  · [Tested locus](../stci-equation-search/index.md#findings).
- **Checked restriction.** The [relative length-twelve scheme](../../arguments/carriers/elliptic_double_inverse_construction.md#the-support-locus-is-a-nilpotence-locus-inside-a-proper-norm-divisor) is finite flat on the smooth basepoint-free open. Its norm is nonzero at the original member, so all full-support candidates lie in a proper norm divisor; a dense open of the entire five-parameter family fails support. Full support is the nilpotence locus, not merely vanishing of the norm. The remaining locus and descent are still unresolved.
- **Sweep update.** The [normalized meeting divisor](../../arguments/carriers/elliptic_double_inverse_construction.md#the-meeting-norm-divisor-and-its-normalization)
  and a meeting fiber failing support bound the closed full-support locus
  by dimension three. The [actual symbol pencil](../../arguments/carriers/elliptic_double_inverse_construction.md#the-horizontal-symbol-and-the-actual-elliptic-pencils)
  and [residual conductor](../../arguments/carriers/elliptic_double_inverse_construction.md#a-finite-descent-test-on-the-residual-quadric-curve)
  give finite gates, not survivors. Search for support on the normalized
  parameter space first.
- **Next test.** Use the divisor of the length-twelve Cartier section
  and the elliptic cover to characterize the support-in-marked-curve
  locus over the **whole** smooth basepoint-free birational open.
  Retain nonreduced fibers and poles of any chosen coordinates.
  Only on a surviving locus, characterize the conductor or graded
  subalgebra obstruction to a pure power descending.
- **Decision.** A support failure on the whole open would close this
  constructive family in all degrees. A positive result at both gates,
  with explicit proper ambient equations, would be a solution. Support,
  Picard identities, and tested finite samples alone decide neither.

### KG06. The nonnormal quintic gap

The [moving quadratic scalar test](../../arguments/linkage/conductor_on_a_smooth_carrier.md#exact-length-at-the-moving-osculating-point)
cannot exclude any integral quintic: restriction to the containing quadric
forces generic regularity, where the exact length exceeds the lower bound.
This does not close the normalization, fixed-endpoint or embedded-kernel tests.

- **Known.** Toric normalizations are excluded, and the nonnormal
  Gorenstein-normalization route is excluded. The non-toric,
  non-Gorenstein nonnormal case remains open; **normal quintics are a
  separate case**. Numerical proportionality on a candidate
  normalization is not a descended equation.
  [Open carrier cases](../../frameworks/carrier-normalization/open_carrier_cases.md#non-toric-non-gorenstein-quintic-normalizations)
  · [Gorenstein route](../../arguments/carriers/quintic_gorenstein_normalizations.md)
  · [Conductor geometry](../../arguments/carriers/quintic_conductor_geometry.md).
- **Sweep restriction.** The [marked Cartier-index defect](../../arguments/carriers/quintic_conormal_and_factor_geometry.md#the-conormal-defect-of-a-marked-cartier-multiple)
  bounds the sum of direction degree and differential rank-drop degree
  by three in the sole-support lane. Compute these on actual remaining
  carriers; a polarization alone does not determine them.
- **First test.** On an actual degree-five nonnormal model outside
  those two excluded classes, determine the possible local Cartier
  indices and full marked inverse and conductor schemes. Separate
  a numerical multiple, a Cartier multiple, and a section that
  is constant along the required conductor identifications.
- **Decision.** A uniform failure of supports or descent here would
  complete a substantial nonnormal lane in every mate degree. A
  model surviving these tests should become a construction target,
  not be treated as an equation. Do not report a new general minimum
  defining degree without the separate normal cases.

### KG07. The genuine sextic frontier

- **Known.** Proper cubic-contact sextic pencils exist in the three
  surviving primitive triple orbits under the general-pencil ADE
  hypothesis. With a first-order member and dependent quadric
  restrictions the sharp generic length is five, not nine. There
  is an exact proper-pencil Chow criterion; a separate normal
  cyclic-cover argument supplies necessary invariants, not a contradiction.
  [ADE contact gate](../../arguments/carriers/sextic_ade_reduction.md#sharp-length-five-for-pencils-with-a-quadric-divisible-member)
  · [Actual sextic incidence](../supported-generator-incidence/index.md#reconciled-fixed-degree-decision-target)
  · [Normal cover](../../arguments/carriers/sextic_pair_reduction.md).
  The [intrinsic source and determinant argument](../../arguments/carriers/sextic_triple_intrinsic_contact.md)
  now explains the complete source dimensions, restricted contact images
  and first-determinant span in this sector. It gives source dimensions
  in every degree at least four and full determinant image for
  \(a,b\ge5\), \(a+b\ge11\), through the three specified triples.
  The equal-quintic corner has a six-jet interpolation gap in the
  geometric proof, separate from KG07's sextic higher-contact question.
  This settles the source/determinant explanation, while decomposable
  proper pencils satisfying the later contact equations remain the gate.
  It does not classify all higher-degree pairs through the curve.
- **First test.** In one named orbit take the full actual sextic
  source with independent quadric restrictions. Express a higher
  normal contact obstruction on the proper-pencil locus that distinguishes
  the length-nine target from the known cubic-contact examples.
  Keep special strata and all actual source directions; a generic rank
  or the dependent-restriction case does not decide this locus.
- **Decision.** A geometric exclusion or actual supported pencil is
  significant. One orbit does not cover the other orbits or all
  sextic pairs; a conclusion outside ADE needs a separate coverage
  argument. The conditional \((6,16)\) incidence is not \((6,6)\).

### KG08. The entire quadratic-root obstruction locus

- **Known.** The first and second obstruction maps impose different
  lifting conditions. The sparse dual pairing excludes a specified seed,
  not the whole smooth first-compatible locus. For a surviving root,
  actual cubic source compatibility, full-root torsion, and properness
  are additional gates. Positive octic first compatibility can coexist
  with residual degree 32.
  [Second obstruction](../../arguments/spectral/quadratic_root_second_obstruction.md)
  · [Actual lift frontiers](../../frameworks/spectral-roots/open_root_lifts.md)
  · [Octic control](../../arguments/spectral/actual_octic_root_lift_comparison.md).
- **Scope sharpened.** The actual elliptic conormal pencil realizes a
  precise spectral line-bundle comparison in its separate family;
  neither torsion nor coverage of the general smooth quadratic-root
  incidence follows.
- **First test.** Characterize the zero scheme of the second dual
  pairing on the smooth first-compatibility locus, retaining all
  pairings and rank-drop strata. If it is nonempty, intersect it
  with the actual embedded-source condition rather than interpreting a
  point of the local locus as an equation. The nonsaturated moving relation
  needs a separate test retaining its divisor twist; the known quadratic
  gap budget does not bound all such contacts.
- **Decision.** Emptiness under the stated root-to-pair bridge excludes
  that smooth quadratic-root sector, not arbitrary normal roots.
  A surviving actual source gives a family for properness and
  residual testing, not automatic sole support.

### KG09. A degree-uniform common-ancestor obstruction

- **Known.** R-0071 reduces a particular quartic two-target question to a
  full multiplication tensor; the surviving linear directions lie on a
  line or a degree-twelve curve. The #159 length-21 fat-point explanation
  concerns the constant rank-drop scheme, not this remainder. A
  quartic exclusion alone does not prove non-quasi-cyclicity of the
  full module.
  [Current finite remainder](../../frameworks/local-cohomology/open_quartic_ancestors.md)
  · [R-0071 proof owner](../../results/quartic_ancestor_direction_reduction.md).
- **Checked comparison.** The [dual-persistence lemma](../../arguments/local-cohomology/polynomial_duals_and_affine_pencils.md#what-persistence-of-a-two-target-dual-actually-requires) identifies the exact excess-intersection condition for changing actual multiplication sources, and a DVR Tor module for specialized duals that do not lift regularly. Fixed-source re-presentation is separated from enlargement of degrees or ancestors. These standard comparison arguments do not establish the needed all-degree maps or decide the remaining incidence.
- **Conductor limitation.** The [separated-cover conductor quotient](../../arguments/linkage/endpoint_lattice_capacity.md#fixed-local-cohomology-targets-and-what-they-cannot-see)
  kills the two fixed socle targets. Transfer must preserve the actual
  multiplication image and values; the first quadric shift still has
  five source directions to evaluate.
- **Next test.** Find a principal-parts or duality formulation of a
  covector separating the two targets on the remaining line and
  curve, including lower corrections and ambient coprimality. Ask
  explicitly whether it is compatible with the maps between orders
  and with higher-degree actual multipliers.
- **Decision.** A proof on this finite source is useful as a test
  of the mechanism. Only persistence through the full direct system
  and the needed incidence bridge would give the general payoff.
  A new rank certificate with no such interpretation is a lower
  priority than the bridge.

### KG10. Arithmetic tests that survive changing the equations

- **Known.** Supported examples exist in every positive characteristic.
  The prescribed quartic lifting obstructions concern specified families;
  some actual traits carry a nonzero endpoint defect. Effective transfer
  is conditional at unrestricted degrees and does not classify reductions
  of arbitrary hypothetical characteristic-zero pairs.
  [Arithmetic lifting interfaces](../../frameworks/arithmetic-supported-lifts/index.md)
  · [Bounded-degree transfer](../../arguments/arithmetic/effective_characteristic_transfer.md).
- **Sweep restriction.** Compatible actual endpoint lattices give
  a [specialization lower bound on generic conductor length](../../arguments/linkage/endpoint_lattice_capacity.md#arithmetic-control-and-comparison-of-traits),
  not the generic upper bound needed for a contradiction. This is not
  the lower-root endpoint defect.
- **First test.** For a specified powered source, construct the
  comparison predicted for an actual supported trait between its
  endpoint defect and the full conductor or annihilator. Start with
  an explicit control where both sides are available. Then test
  whether the comparison retains the endpoint algebra and is intrinsic
  under changing the degree-labeled presentation. The prescribed
  supported trait itself is not assumed to exist.
- **Decision.** A presentation-independent obstruction plus a coverage
  theorem for reductions would be meaningful. A stronger nonlift
  for just the prescribed source still says nothing about unrelated
  characteristic-zero pairs.

## Current choice and reassessment

Retain KG02 provisionally, but **withdraw the \((5,4)\) sextic probe**:
the involution--Bézout inequality excludes it outright, and the
remaining \((6,3),(7,2),(8,1)\) two-support partitions are excluded
on nodal sextic carriers. The current object is the geometry of
the nonnodal carrier and its anti-invariant local divisor classes
together with the global \(-Z_\pm^2=38/3\) budgets, not another
unrestricted coefficient sweep. The exceptional quartic
classification has **already** acquired a complete geometric
proof: residual genus/Ferrand doubling excludes asymmetric
multiplicities, and self-linkage plus the Hilbert--Burch
canonical module and residual-line restriction classify its
proper pencils. Its next question is no longer proof
replacement but **transferability**: which other lci/ACM
supported unions admit comparably small canonical modules
and two-generator liftability tests, and how do these
interact with the even-eight carrier and vertical
Hilbert-over-Chow fiber? The sextic ADE lattice feasibility
test and the existing KG05 elliptic inverse-support locus
remain distinct competing investigations. None yet has
a general-degree coverage theorem.
On the obstruction side, the trace and different calculations
leave a separate question about arbitrary non-invariant equation
sources.

The common-quadric chart removes the entire \(h_2=0\) boundary and its
higher-order arcs from this probe. Under coprime ambient cofactors and
nonzero first cancellation the balanced subcycle still excludes constant
sole support at other rank drops. The actual higher-order graph question
is now focused on positive-\(h_2\) cancellation, zero restrictions or
common cofactors. Merely computing the already explicit normal image
would not add understanding.
A neglected comparison is the [actual-pair coregularity module](../../arguments/local-cohomology/actual_pair_coregularity.md)
on the explicit quadric/cuspidal-cubic pair with residual double line. It
could clarify how residual geometry detects the second-equation failure,
but no map to filtered lifting defects is yet supplied. That bounded task
is a concrete alternative if the sextic probe reproduces only
containment. A second bounded alternative starts from the classified
osculating triples and computes a next embedded equation module,
Gorenstein extension and source fixed surfaces. It would test actual
embedded schemes beyond the now-settled defect-placement question.
No result here proves KG02 superior to either task or to KG05.

KG05 is the strongest concrete alternative: its whole-family support locus is
well defined and unresolved, with a dimension bound and an exact finite-algebra
test. It is narrower in family coverage but could close or advance an actual
construction. KG01's scalar comparison is ineffective on a dense open of
the full smooth source for every fixed-endpoint cover, and the moving
osculating scalar test fails on every generically regular smaller carrier.
Its surviving questions concern embedded homogeneous kernels and the
toric graph correction. The moving-cover endpoint computes that correction
exactly in one family; control from arbitrary global equations remains open.
These distinctions support a provisional exploration choice, not certainty
about eventual payoff. The sextic target starts with explicit support
and no identified carrier, whereas the elliptic target already has a
finite inverse-support algebra and leaves its whole-family descent open.
Reassess if the sextic probe supplies no constraint beyond containment.

Keep the [marked V5 correspondence](../../arguments/residuals/blowup_residual_geometry.md#the-marked-correspondence-on-the-whole-equality-boundary)
as a distinct transfer/contact test, and KG03 as the actual absorption question.
Neither moving a residual nor changing a cycle alone lifts its two equations.
Keep IDs stable, preserve scoped findings at their owners, and revise the queue
when the expected understanding changes. Do not turn the ranking into a list
of proofs to rewrite.
