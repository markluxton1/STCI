# Proof priorities by potential knowledge gain

**Status:** The sole strategic ranking of current research questions, not a new Result. Start at the [active front door](open-items.md) for the overall organization; use the canonical proof/framework owners for mathematical status. The [proof-dependency workbench](README.md) supports specific explanatory improvements, not a competing queue. A short coordinate-free proof can rank low here, while a proof retaining a small exact calculation can rank high.

## Ranking rule and coverage

The problem is whether the **fixed** quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) is a set-theoretic complete
intersection in characteristic zero. A proper pair of degrees \(a,b\)
has \(ab=4m_C+\deg R\). An argument gains knowledge here if it explains
why actual homogeneous pairs must leave residual support, produces an
actual pair with none, or identifies a transferable constraint separating
these alternatives. The degree identity alone does none of these.

The order below favors, in order: a mechanism applicable across degrees
or carriers; an exact bridge to global equation realization; a decisive
test of an actual constructive family or a significant degree frontier;
and then an explanation of a bounded local or computational gate.
Readiness and cost are kept separate from payoff. The two highest ranks
are not promises of short proofs. A counterexample to a proposed
mechanism is useful if it pinpoints the missing hypothesis; failure on
a sample is not an exclusion of the surrounding family.

This pass follows the current [research map](../../MAP.md) across actual
equations, formal normal geometry, torus limits, residual deformation,
carrier normalization, spectral roots, local cohomology, and arithmetic.
It checks current proof owners and documented controls rather than
replaying the old inventory or re-auditing every archived file.

## Ranked research problems

| Rank | Stable ID | Question for a better argument | Payoff if resolved |
| --- | --- | --- | --- |
| 1 | KG01 | What projective equation constraint limits the required deep normal contact? | Direct degree-independent mechanism |
| 2 | KG02 | When must an actual moving ideal expose residual support in its equation layers? | All-degree torus/actual-generator bridge |
| 3 | KG03 | Can a marked absorption step close at **zero** residual degree? | Direct constructive bridge, or a precise obstruction to it |
| 4 | KG04 | Can residual-capacity tests reach carriers outside the known ordinary open? | Transferable all-mate exclusions on new carrier strata |
| 5 | KG05 | Can the full elliptic inverse scheme be supported on the marked curve and descend? | A concrete potential construction, in every mate degree |
| 6 | KG06 | What replaces Cartier descent on the surviving quintic normalizations? | A substantial low-degree gap, not all quintics |
| 7 | KG07 | Do actual sextic pencils in the remaining ADE loci reach length nine? | A fixed-degree decision and test of higher-contact mechanisms |
| 8 | KG08 | Can the quadratic-root obstruction be made uniform over its zero scheme? | Excludes or isolates a broad, but conditional, local-root sector |
| 9 | KG09 | Does a two-target dual obstruction persist under changes of order and degree? | A potential all-degree local-cohomology bridge |
| 10 | KG10 | What global obstruction survives arithmetic specialization of varying pairs? | Could turn prescribed-family arithmetic into an obstruction to actual varying pairs |

### KG01. Projective limits on deep generic normal contact

- **Known.** Noether's formula and the quadric slope imply that any
  defining pair needs common points beyond depth one; at least \(pq/4\)
  of the generic contact is beyond that depth, where \(p,q\) are its
  starting normal orders. Exact line-bundle recurrences are available along
  a specified horizontal section path. Fixed tangent forms can have
  unbounded local contact, and tangent data do not determine the next
  multiplicity. The normal-jet cutoff is fixed-degree, not an all-degree
  reduction. [Depth](../../arguments/residuals/generic_contact_depth.md#4-smooth-quadric-family)
  · [Horizontal paths](../../arguments/residuals/horizontal_blowup_recursions.md)
  · [Actual finite jets](../../arguments/residuals/finite_normal_jets.md).
- **Checked uniform sector.** The [moving-relation theorem](../../arguments/equations/global_lifting_interfaces.md#a-uniform-nonvanishing-theorem-in-relation-degree-at-least-two) proves the next-order class is nonzero in characteristic zero for saturated degree-one movement, relation degree at least two, and no independent next relation. The mechanism is incompatibility of shared Laurent corrections, not a sampled rank. The order-one geometric zero locus is classified separately, without a higher-lift or scheme-structure claim. Positive first-relation defect divisors and other normal initial ideals remain outside the theorem.
- **Projective constraint found.** For every possible defining degree,
  the two first symbols must have a connected, pure curve of common
  directions. On the zero direction-degree boundary the sole section's
  normal bundle forces more than \(pq/2\) generic contact beyond depth
  two in characteristic zero. The characteristic-three cubic–quartic
  pair exhausts its contact by depth two. [Residual and deep-contact theorem](../../results/connected_normal_directions.md#statement).
- **Next test.** On this boundary the remaining issue is an upper
  bound from the actual equation sources, or a pair that sustains the
  required tail. At \((3p,4q)\) it suffices to decide the
  [marked quintic criterion on \(V_5\)](../../arguments/residuals/blowup_residual_geometry.md#actual-equations-on-the-zero-direction-edge)
  for one endpoint and one mixed direction, including the conic normal
  value that detects a contracted residual line. For positive direction
  degree the second-blowup test needs a nef twist of the actual
  multisection's normal bundle, or a comparison that retains the other
  components meeting a chosen center.
  The basepoint-free moving first relation of degree one now has the
  uniform nonvanishing theorem just stated in orders at least two.
  Its next unresolved tests are the divisor twists that record
  nonsaturation and higher lifting of the order-one zero locus; the quadric control
  prevents an indiscriminate nonvanishing claim.
  [Moving-relation operator](../../arguments/equations/global_lifting_interfaces.md#8-the-next-order-operator-for-a-moving-relation).
- **Decision.** A bound stronger than the required tail on this stratum
  is a real exclusion there. If the mechanism needs one section, it
  must be extended separately to multisections, branching, ramification
  and vertical components before it covers arbitrary pairs. Counting
  depths or rewriting \(ab=4m_C\) is not progress on this bridge.

### KG02. Actual equation layers and the two torus ends

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
- **Next test.** Pick one declared proper bidegree family with
  \(e_L>0\). Derive a projective bound on the joint first-layer kernel
  directly from the two degree-labeled equation sources, on the **same**
  family at both ends. Check the \(W_0\) missed-class example first.
- **Decision.** A uniform bound below \(e_L\) forces residual degree on
  that family; a verified full supported family passing the test is
  useful for equation recovery. Do not infer either from an unperformed
  attracting-family plan, a top Chow cycle, or a single limit ideal.

### KG03. Globalizing a marked absorption step

- **Known.** Proper actual families can absorb positive residual degree.
  In R-0049 a moving quartic is absorbed, but a twelvefold residual
  line persists. The marked Quot model separates deforming the marked
  object, lifting its two equations and maintaining properness.
  At a hypothetical endpoint one sufficient embedding vanishing is
  unavailable; the nonzero obstruction **space** is not an obstruction
  class. [R-0049](../../results/sextic_residual_absorption.md)
  · [Marked equation incidence and limits](../../arguments/residuals/marked_deformation_and_absorption.md#7-partial-absorption-and-the-missing-passage-to-sole-support).
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

- **Known.** Toric normalizations are excluded, and the nonnormal
  Gorenstein-normalization route is excluded. The non-toric,
  non-Gorenstein nonnormal case remains open; **normal quintics are a
  separate case**. Numerical proportionality on a candidate
  normalization is not a descended equation.
  [Open carrier cases](../../frameworks/carrier-normalization/open_carrier_cases.md#non-toric-non-gorenstein-quintic-normalizations)
  · [Gorenstein route](../../arguments/carriers/quintic_gorenstein_normalizations.md)
  · [Conductor geometry](../../arguments/carriers/quintic_conductor_geometry.md).
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

## Outcome of this bounded pass

KG01, KG02, KG04, KG05 and KG09 have the scoped checked advances recorded above. None closes its unrestricted research question. The later KG07 integration establishes the source/determinant explanation recorded in its known state; its higher-contact first test remains open. KG03, KG06, KG08 and KG10 retain their first tests and stopping conditions. In particular no absorption-to-zero construction, remaining quintic classification, full sextic decision, uniform quadratic-root exclusion or presentation-independent arithmetic obstruction is claimed. The ranking measures potential knowledge gain, not completion.

## Where to start, and how to use the queue

- **Highest payoff:** KG01. Work on a precisely specified horizontal
  stratum first, not a purported universal contact-depth formula.
- **Best immediate pilot:** KG04. There is a concrete test for a new
  carrier: state the actual normalization and complete test-divisor
  support, compute its branch weights, and either give a strict
  inequality or name the first hypothesis that fails. This can inform
  KG01 without presupposing a universal solution.
- **Best separate construction check:** KG05's support locus before
  any descent or degree search. This asks whether a known obstruction
  kills an actual family rather than whether a random coefficient
  sample happens to work.
- **Keep as evidence or park:** Smith factors and character lattices
  retain scheme or torsion data; keep them. Further cleanup of already
  geometric proofs or of isolated determinants is valuable editorially
  but is not an unrestricted research priority. The [boundary-reconstruction owner](../../arguments/torus/boundary_reconstruction_and_defects.md) gives marked gluing,
  reconstruction and nonalgebraization results that delimit the
  diagram question; reopen only for precisely specified additional
  retained data and a named realization problem. Primary topological
  tests on the complement are already understood; do not rerun them
  without an algebraic section obstruction
  ([complement comparison](../../arguments/equations/complement_section_obstructions.md)).

Keep IDs stable and revise the ranking when coverage or payoff changes.
Log the exact class tested and the strongest surviving counterexample.
Promote to an Investigation only when there is a declared source, a
test and a stopping condition, and to a Result only after proof and
review. A useful negative answer and a scope correction belong in the
queue too; neither needs to be turned into a stronger theorem.
