# Realization questions and open interfaces

The characteristic-zero STCI question for the fixed \(C_0\) is open.
Existence and nonexistence remain possible. This page records concrete
mathematical gaps, constructions and possible investigations, not an ordered agenda; [selection criteria](RESEARCH_DECISION_GUIDE.md)
help choose a bounded investigation. Exact statements and proofs are in the
[cataloged Results](CATALOG.md) and their proof homes.

The broader problem is to describe proper intersections containing C0, their
multiplicity and residual cycle, embedded multiple structures realized by actual
equations, and supported ACM or AG structures. A useful construction may stop
short of sole support, and a general lemma may matter for other curves. Failure
of a specified source describes what a different realization must change; it
does not accumulate into an exhaustive classification without a coverage proof.

The torus pilot gives two concrete Investigation entrypoints:
[two-equation incidence on a declared supported family](investigations/supported-generator-incidence/index.md)
and [comparison of moving quotients with full limits](investigations/quotient-hilbert-comparison/index.md).
The endpoint comparison now determines pure intrinsic limits and embedded
lengths, while full equation incidence remains open. The
[finite residual controls](investigations/torus-residual-controls/index.md)
are complete within their explicit computational scope and resolve neither
question. Their Frameworks explain the selection criteria without assigning
this lane priority over independent constructions or obstructions.

## Selection boundary

The completed contributions below leave several different realization
questions. The recommendations select bounded next tests from those actual
inputs; they do not assign a new research round or treat one source as
exhaustive. Their exact committed scope is recorded in the integration commit.
The [selection guide](RESEARCH_DECISION_GUIDE.md) explains what the combined
results change and how to choose between constructive and obstructive aims.

## Broader interfaces

| Interface | Available result or construction | Missing implication or bounded test |
| --- | --- | --- |
| Actual global pairs | [Exact source spaces](supplements/ACTUAL_EQUATION_SPACES.md), [Chow/complement equivalents](synthesis/global_equations_and_constructions.md) | Produce a proper pair with exhausted cycle, or prove an incompatibility covering every relevant source; dimension and equivalent formulation alone do neither |
| Torus limits and supported deformations | [Full invariant limits](synthesis/global_equations_and_constructions.md#the-supported-hilbert-locus-and-its-full-torus-boundary), [explicit residual controls](arguments/torus_sextic_residuals.md) | The sharp eigenform sextic quotient bound is eight; a residual full limit needs a degree-ten generator. For sole support, consider both full-ideal limits and their attracting loci, then test two-generation on moving ideals; a selected I_C-primary boundary is a useful local probe, not the default classification. Residual examples do not establish supported incidence or coverage |
| Formal normal realization | [Simultaneous compatibility](frameworks/formal-normal-geometry.md#simultaneous-realization-and-compatibility-problems) | Connect an embedded generic thickening to one ambient scheme and two compatible global carriers. Test equality with their intersection and then sole support |
| Embedded lower thickenings | [One-step and filtration tests](synthesis/03-infinitesimal-geometry.md) | Determine a proper decomposable determinant-zero point in the actual equation spaces across a justified family of lower embeddings |
| Normal filtration under specialization | [Prescribed \(\mu_4\) normal initial ideals](results/quartic_normal_initial_base_change.md), [quotient-to-Hilbert investigation](investigations/quotient-hilbert-comparison/index.md) | For a declared moving family, control specialization of the filtered equation data separately from projective flatness. The prescribed family provides an explicit failure of associated-graded base change |
| General roots and initial ideals | [Root and normal-filtration tools](synthesis/normal_filtration_boundary_obstructions.md) | Handle singular/nonreduced roots, nonsaturation, extra generators, noncoprime next relations and failure of joint generation; no arbitrary entirely-thick→movement-two reduction is known |
| Normal Koszul pages and extended Rees torsion | [Incoming differential filtration](results/normal_koszul_comparison_defect.md), [extended Rees persistence](supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md#7-consequences-limits-and-next-questions) | Compare the page filtration of \(\Delta\) with the \(u\)-power filtration of equation-module torsion over \(\mathcal O_C[u]\). The explicit Rees duration family proves its own page match. A general sheaf-level identification is open |
| Punctual comparison defects | [Statements and proofs](arguments/punctual_comparison_defects.md#statements-and-proofs) | [Punctual relative defect under sole support](#punctual-relative-defect-under-sole-support) |
| Conditional sextic incidence | [Structured incidence](supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#6-the-exact-remaining-scheme), [forced norm for actual pairs](synthesis/normalization_conductor_phase2_addendum.md#actual-quadric-cycle-norm-bridge), [unique actual lift](synthesis/rank_strata_and_sextic_lifts.md) | Cubic matching determines at most one actual sextic on the necessary root open; resolve the surviving root/target incidence and then a mate and support. Generic-conic, zero-defect pencil and endpoint strata remain; the seed and free cube-orbit chart are already excluded within their exact scopes |
| Actual carrier families | [Fixed-carrier descent](synthesis/04-carriers.md), [Q-0001](questions/cartier_projection_models.md), [phase reduction](results/projection_phase_reduction.md), [plane conductor test](results/singleton_plane_conductor_descent.md) | Compute admissible images, full inverse support and complete conductor phase; include non-Cartier/multiple-branch carriers outside singleton classification |
| Elliptic projection | [Canonical gluing](synthesis/projection_and_elliptic_gluing.md) | Pass component polarization, actual node gluing, determinant support and projection admissibility simultaneously; palindromic and paired examples fail at different gates |
| Elliptic double-inverse construction | [Actual five-parameter source](synthesis/elliptic_double_inverse_construction.md) | Test full inverse support fiberwise while retaining smoothness, basepoint freedom and finite birationality, then test actual section descent; the failed fixed member does not decide the family |
| Sole-support sextic pairs and their cyclic cover | [Sextic profiles and normal cover](supplements/SEXTIC_PAIR_REDUCTION.md) | The three divisor profiles, nonreduced common symbol, index-nine point and cover invariants constrain realization; no incompatible upper irregularity bound or global construction is known |
| Uniform residual control | [Attachment/capacity and finite jets](synthesis/residual_intersections_and_jets.md) | Prove a positive residual bound on a covered global family including exceptional strata, or construct pairs reaching zero; one carrier certificate is not uniform |
| Residual absorption and modifications | [Marked ribbon construction](synthesis/marked_deformation_and_absorption.md), [actual quadric modification](synthesis/quadric_modification_and_global_corrections.md) | Iterate an actual transfer while preserving the marked embedding, equation lifts and properness; the specified quadric modification's complete lift space has positive residual degree, while general modification sources remain open |
| Normal surface geometry | [Quintic–octic ADE theorem](synthesis/quintic_octic_surface_constraints.md), [sextic ADE reduction](supplements/SEXTIC_ADE_REDUCTION.md) | Non-ADE quintics remain outside the (5,8) exclusion; the sextic pencil still needs actual source compatibility and higher contact after its primitive-triple reduction |
| Nonnormal carrier geometry | [Gorenstein-normalized quintics](synthesis/quintic_gorenstein_normalizations.md), [remaining toric center incidence](synthesis/quintic_toric_center_incidence.md), [conductor differential](synthesis/carrier_conductor_differential_comparison.md) | Decide full inverse support on the remaining M locus before testing actual power descent; singular local gluing alone does not realize the projective carrier |
| Spectral graded families and ambient equations | [Order-three parameterization](synthesis/order_three_roots_and_sextic_lifts.md), [actual source quotient](synthesis/actual_octic_root_lift_comparison.md), [torsion-two charts](synthesis/quadratic_root_torsion_two_lifting.md) | The completed 24-point affine slice has no compatible sextic; test the full root incidence with its rank boundaries and all corrections. Positive octic constructions remain useful for containing intersections |
| Finite jets and equation search | [Intrinsic global jets](synthesis/global_equation_jets.md), [bounded certificates](synthesis/bounded_equation_certificates.md) | Use actual source-image filtrations and full nonlinear corrections; existential finite realization is distinct from a uniform effective witness-degree bound |
| Contact and tropical descent | [Endpoint-to-limit comparison](results/intrinsic_limits_endpoint_fibers.md), [constant-quotient equation criterion](results/constant_quotient_equation_criterion.md#statement) | Test surviving high-contact or noncurvilinear endpoint fibers against actual sextic sources in one moving rank-nine family satisfying a divisor profile. Recover the full opposite-endpoint algebra and moving generator incidence |
| Marked dual/ruled geometry | [Fixed geometry](synthesis/01-problem-and-curve.md) | Construct a proved map from actual equation/conductor data to marked contact schemes, retaining nilpotents and endpoint corrections |
| Characteristic comparison | [Explicit equations](supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md), [endpoint image comparison](arguments/torus_embedded_quotients.md), [effective transfer](supplements/EFFECTIVE_CHARACTERISTIC_TRANSFER.md) | Analyze the integral image and base-change defect in a declared embedded quotient family; quotient flatness alone does not give flat projective images. All-pair degree growth remains conditional, and fixed-carrier or prescribed-lift restrictions do not exclude unrelated presentations |

For a hypothetical characteristic-zero sole-support pair of degrees
\(5\le a\le b\), let \(\delta\) be the length of its finite quadratic
conductor boundary and put \(q=\lceil a/2\rceil-1\). The [ambient-norm conductor theorem](synthesis/quadratic_covers_and_conductor_descent.md#81-ambient-quadratic-norms-force-conductor-postulation) gives no boundary equation below degree q and
\[
\delta\ge a+b-3+2\left[\binom{q+2}{3}-q\right].
\]
No incompatible upper bound is known. Its constructive question is which actual
embedded boundary schemes and multiplication maps realize this postulation.
The norm strengthens the use of the existing canonical sequence; its Rao
dimensions are not a second independent budget. The broader degree-d theorem
and the distinct [extremal line argument](synthesis/quadratic_covers_and_conductor_descent.md#12-embedded-curve-exclusion-of-the-minimal-boundary)
remain useful outside this particular norm application. Finite-order punctual
MCM lifts do not produce homogeneous ideal columns, and section completion
does not repair the original embedding. An embedded AG conjugate union would
descend automatically. The [supported-linkage constructions](synthesis/supported_linkage_operations.md)
produce actual ACM schemes upstairs, while their specified failures leave other
sources and chains open.

The [embedded fourth-extension calculation](synthesis/intrinsic_fourth_extension.md) closes the previously missing neighborhood-only route for the two allowed (4,4) types. It does not supply a general classification of higher-length thickenings or higher-degree actual sources; those remain separate interfaces above.

### Successive jet discrepancies in actual equation spaces

For the fixed \(C_0\) in characteristic zero, when do successive normal-jet
conditions become dependent in primitive or quasiprimitive filtrations?
Treat actual carriers of degree at least five and residual intersections
involving a quartic as separate settings. Use the actual global section
sources and the targets modified by saturated layer divisors. In a specified
degree and family of lower embeddings, determine an intrinsic rank-defect
locus for a successive restriction map, including its special strata. Seek
an explicit relation to the punctual [R-0030 comparison defect](results/local_filtration_comparison_defect.md)
of the map from the minimal generators of the full normal initial ideal
to the associated graded of the actual equation module.

A negative expected condition budget leaves the actual ranks to be checked.
The [order-one calculation](results/order_one.md#historical-jet-discrepancy-comparison-scope-limited)
defines the discrepancies and links the finite \(2R\) evaluation. The
[ruling-fiber rank jump](results/jet_geometry.md) concerns \(e=2\).
The \(e=0,1\) sources have their own calculations, including the
[comparison-zero direction](supplements/OCT7_SATURATION_REES_AND_CARRIER_CLASSIFICATION.md#comparison-zero-point)
and the [repaired Cartier intersection argument](supplements/OCT7_SATURATION_REES_AND_CARRIER_CLASSIFICATION.md#repair-of-the-fixed-ruling-stci-implication).
These are models for the comparison. [R-0001](results/quartic_carrier_exclusion.md)
closes the integral quartic-carrier mate cases, including the historical
\(e=0,1\) order-one targets.

### Quartic common ancestors in local cohomology

For the fixed \(C_0\) over an algebraically closed characteristic-zero field,
can actual quartics \(F,G\in I_4\) and a homogeneous \(\alpha\in M_{-7}\)
satisfy \(F\alpha=u\), \(G\alpha=v\), where \(M=H_I^2(S)\), \(I=I_{C_0}\),
\(S=k[x,y,z,w]\), \(u=xz/(qB)\), and \(v=yw/(qB)\), with \(q=xw-yz\)
and \(B=xz^2-y^2w\)? The [finite order-four reduction](supplements/LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md#uniform-finite-reduction-for-the-remaining-degree-four-locus)
puts \(\alpha\) in the 30-dimensional space \((0:_M I^4)_{-7}\), with
principal-part order exactly four. Each quartic source is 18-dimensional.
The [ruling-ratio slices](supplements/LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md#new-all-stage-exclusion-both-ruling-ratio-slices),
[two pure constant directions](supplements/LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md#independent-audit-of-pure-constant-quartic-directions),
[explicit all-stage family](supplements/LOCAL_COHOMOLOGY_ANCESTOR_OBSTRUCTIONS.md#3-an-integral-coefficient-functional-excludes-the-whole-explicit-family),
and [normalized parity family](supplements/LOCALCOH_CONTACT_PARITY_AND_MF6_TYPE.md#a-corrected-polynomial-dual-exclusion-for-the-normalized-parity-family)
have their own exact exclusions. The [two rational endpoint families](supplements/LOCAL_COHOMOLOGY_DEGREE15_CERTIFICATES.md)
have primitive direction degree two and pure cubic top \(h=t\). Their
certificates exclude target \(u\) for every admissible direction and affine
lower correction in those families.

Recast the remaining incidence using [successive jet discrepancies](#successive-jet-discrepancies-in-actual-equation-spaces).
For the remaining primitive conormal directions of degrees zero, one, and
two, retain the ambient-coprime quartic lifts. Test the top-symbol lifts
and both lower multiplication equations in the full finite tensor.
Non-quasi-cyclicity of the full module needs an argument beyond this fixed
degree. The quartic-mate theorem concerns sole support, whereas the ancestor
[generic length calculation](supplements/LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md#2026-10-05-localcoh-generic-length)
gives a degree-four residual cycle for any such pair.

### Multiplicity-six incidence in actual jets

For a saturated quasiprimitive length-six structure, express the finite
incidence conditions through successive jet ranks on a declared actual
source. Test whether the saturated divisors and the higher-jet maps
together explain the rank strata. The [perfect pairings](supplements/MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mf6-pairing-audit)
use finite-flat Gorenstein duality. The [rank-six Fitting identity](supplements/MULTIPLICITY_MIXED46_AND_MF6.md#1-mf6-including-the-torsion-and-generation-steps)
also uses generation by the two ambient normal coordinates in the embedded
lci setting.

For a hypothetical characteristic-zero \((4,b)\) pair with sole support
\(C_0\) and \(e=0\), the [global bound](supplements/MULTIPLICITY_MIXED46_AND_MF6.md#2026-10-05-mf6-further-audit)
is \(\deg D_2\ge3\). For bidegree \((4,6)\) and \(e=0\), set
\((d_2,d_3)=(\deg D_2,\deg D_3)\). The [nonregular exclusion](supplements/LOCALCOH_CONTACT_PARITY_AND_MF6_TYPE.md#independent-audit-of-the-mf6-degree-three-nonregular-exclusion)
for \((d_2,d_3)=(3,6)\) leaves the regular-ratio case to the general
[quartic-mate theorem](results/quartic_carrier_exclusion.md). The
\((d_2,d_3)=(4,5)\) type also has its own
[complete exceptional-fiber exclusion](supplements/MULTIPLICITY_SIX_QUARTIC_CONTACT.md#4-complete-remaining-exceptional-fiber)
in bidegree \((4,6)\). These closed mate cases supply saturated filtration
and actual source tests for the structural comparison.

### Split sextic carriers

Fix \(C_0\) over an algebraically closed field of characteristic zero.
Consider an integral sextic of exact normal order two whose first exceptional
divisor is the reduced sum of two distinct integral, content-free sections
with no vertical component. A hypothetical sole-support mate must pass the
[split numerical and first-normal reductions](supplements/SPLIT_SEXTIC_AND_MULTIPLICITY_SIX_RESTRICTIONS.md#p-041-torsion-corrected-sharpening-of-the-surviving-split-sextics).
Keep the \([4]\) and \([2,2]\) strata separate.
The [fixed ramified first-normal specimen](supplements/RESIDUAL_CYCLES_AND_SPLIT_CONFIGURATIONS.md#proved-the-fixed-p-041-boundary-normal-form-has-no-stci-carrier)
has an all-mate exclusion from higher jets. In the \(d=1,[2,2]\) family
with both residual ruling roots totally ramified and the two low evaluation
zeros at their preimages, the [full higher-jet reduction](supplements/SPLIT_SEXTIC_TWO_RAMIFIED_ROOTS.md#result-and-scope)
leaves a necessary one-parameter line. The
[bounded next test](supplements/SPLIT_SEXTIC_TWO_RAMIFIED_ROOTS.md#surviving-line-and-continuation-requirements)
is to compute its normalization, conductor and numerical branch
intersections, including exceptional parameter values. Integrality, mate
descent and sole support still require separate checks. The
[nonramified \([4]\) charts](supplements/RESIDUAL_CYCLES_AND_SPLIT_CONFIGURATIONS.md#2026-10-05-split4-nonramified)
and [further \([2,2]\) chart](supplements/RESIDUAL_CYCLES_AND_SPLIT_CONFIGURATIONS.md#an-additional-22-chart-for-continuation)
retain their own higher-order lifting and conductor tests.

### Higher-order Rees data for entirely-thick pairs

Consider a hypothetical proper characteristic-zero pair with sole reduced
support \(C_0\) and both exact generic normal orders \(p,q\ge2\). These orders
lie outside the [order-one Bănică–Forster bounds](results/order_one.md).
At or near equality in the [exceptional-cycle bounds](results/entirely_thick.md),
can a finite invariant of successive transforms and Rees data force a
residual curve downstairs or rule out the required normalization or
conductor support?

The [fixed tangent-form examples](synthesis/rees_and_vertical_controls.md#5-counterexample-family)
have unbounded transverse length. The [affine saturation-defect controls](synthesis/rees_and_vertical_controls.md#5-an-intrinsic-saturation-defect-unbounded-with-fixed-generic-algebra)
also allow unbounded special-point defects with a fixed generic filtered
algebra. The open step is to use the higher-order data, including the
geometry of successive exceptional surfaces, to obtain an additional
restriction on projective degrees or support.

### Punctual relative defect under sole support

For a smooth integral marked curve \(C\) in a smooth threefold, let
\(J\subset I_C\) be generated by a regular sequence of two equations.
If \(\sqrt J=I_C\) and \(\Delta_\eta=0\) at the generic point of \(C\),
can the relative comparison defect \(\Delta\) be nonzero at isolated
points? If so, what is the smallest supported example? If it vanishes,
which duality or support condition forces vanishing? This is a local
question about the full equation comparison of
[R-0030](results/local_filtration_comparison_defect.md#statement).

The [punctual comparison controls](arguments/punctual_comparison_defects.md#statements-and-proofs)
separate actual residual support from torsion that survives in the filtered
equation quotient. The [degree-four cancellation](results/initial_equation_cancellation_counterexample.md)
fails generic vanishing. For a control with a nonzero actual slice defect
and zero relative defect, see the
[bounded length-five test](#supported-length-five-degeneration).

### Comparing the normal cone with marked Quot incidence

For a specified proper pair with intersection ideal \(J\), compare
\(\operatorname{gr}_{\mathcal I_C}(\mathcal O/J)\) with a marked lower
thickening in the [Quot incidence for residual absorption](synthesis/marked_deformation_and_absorption.md).
Projectivizing the full normal cone on the exceptional surface can discard
zero-section data. The open task is to construct a comparison of the two
deformation problems with its kernel and cokernel and to specify the normal
relations that the comparison retains. See the [formal-normal framework](frameworks/formal-normal-geometry.md)
and the [normal-filtration account](synthesis/normal_filtration_boundary_obstructions.md).

## Tests that distinguish a new implication from a repeated computation

For a proper degree-\((a,b)\) pair containing \(C_0\),
\([V(F,G)]=m[C_0]+R\) and \(ab=4m+\deg R\). The exact finite-length
criterion tests an **actual** pair; a uniform theorem needs quantified source
coverage. Full initial ideals must include cancellation-generated relations.
Exceptional vertical curves do not automatically supply \(R\ne0\).

A leading symbol, an abstract graded Picard relation, an all-orders formal
lift, and a global homogeneous equation are different realizations. In a
fixed symbol fiber, all allowed lifts enter the obstruction quotient; the
[general lifting lemma](synthesis/global_lifting_interfaces.md) makes that
check precise. The conditional sextic seed's exact witness kills the free
\(q^3\) direction, so that seed is an all-lifts exclusion; this says nothing
about every remaining root.

Stopped construction families are not exhausted subjects. Revisit one when
there is a new actual source, a missing boundary calculation, a provable
coverage extension, or an informative counterexample. A new notation or
another equivalent condition alone is not a completed advance.

The [projected-section obstruction](synthesis/projected_thickening_section_defects.md) closes power and homogeneous binary-mixture repairs of its stated source at the weaker downstairs ACM gate. Its missing ambient section is useful information about projection of nonreduced schemes. A different source must change that section-image mechanism; increasing the powers in the covered characteristic range does not do so. This does not identify source/image torsion with the relative comparison defect below. Constructing an actual ACM thickening downstairs remains distinct from constructing an ACM scheme on the covering quadric.

## Recommended next bounded tests

The [comparative assessment](RESEARCH_DECISION_GUIDE.md#recommended-allocation-and-stopping-outcomes)
favors octic multiplier geometry for bounded positive constructions and the
ADE (6,6) contact problem for a covered degree sector. Torus limits offer a strong organizing lens for the (6,6) or ACM target: consider attracting loci of full invariant limits and test the generator behavior of moving ideals. This need not precede independent local arguments. These are proposed choices, not new
assignments or mathematical status changes. The toric and elliptic sources
retain their value as bounded carrier investigations.

1. **Determine octic multiplier kernels and their common-zero divisors.**
   Apply the [actual octic quotient](synthesis/actual_octic_root_lift_comparison.md#application-to-the-24-first-compatible-order-three-roots)
   to the 24 known first-compatible roots, whose sextic tests are complete.
   Positive kernel-dimension bounds do not prove joint generation. Stop at
   exact kernels and fixed divisors, with proper pairs where joint generation
   holds, or a precise missing representation. The existing perturbation
   argument already gives generic length eight and residual degree 32 in
   that case; do not re-prove it root by root. Higher contact is a separate
   question, and sole support for (8,8) would require length sixteen.
2. **Decide higher contact in the three surviving ADE (6,6) triple orbits.**
   Use the [complete triple classification and actual sextic spaces](supplements/SEXTIC_ADE_REDUCTION.md#three-remaining-primitive-triple-orbits),
   retaining all 27 dimensions, including the seven directions beyond
   quartic-source multiples. The first contact equation is known; higher
   coefficients through order eight and properness remain. Stop at an
   exclusion covering all three orbits at a stated contact stage, an exact
   proper pair of generic length nine (which exhausts degree 36), or a
   precise missing representation. This covers the ADE general-pencil
   sector only. The non-ADE singularity/cover question remains below.
3. **Consider opposite invariant-limit strata and moving-ideal two-generation.**
   Use the [full-limit formulation](synthesis/global_equations_and_constructions.md#proposed-test-supported-deformations-of-an-invariant-boundary-ideal).
   For a chosen CI degree pair or ACM Hilbert polynomial, consider the bounded supported Hilbert locus and its full invariant-limit attracting sets. Test actual moving-ideal generators on these loci; a selected fixed ideal and its supported deformation problem remain valid local probes. Retain full relations, possible embedded points,
   and incidence \(C_0\subset Y\subset V(I_{C_0}^N)\). Existing invariant
   quadric multiples supply controls or exploratory ACM candidates, not a
   demonstrated supported (6,6) boundary. The
   [explicit three-generator limit](results/sextic_three_generator_full_limit.md)
   has the (6,6) Hilbert series and is a demonstrated limit of a CI with
   residual curves; its support is not C0, so it is a generator/flatness
   control rather than a candidate in this supported incidence.
   A first task may stop at a useful stratification or a usable local deformation representation, or identify precisely why either is unavailable. A subsequent
   test seeks an actual supported CI/ACM deformation or an exclusion of the
   declared boundary family. The general fiber may break symmetry; invariant
   CI ideals themselves are excluded in characteristic zero. Tangent weights,
   a pure hull, or two extreme forms do not replace the full deformation.
4. **For the conditional (6,16) direction, use the intrinsic sextic map on a
   justified cover of the full order-three family.** The
   [fixed-frame parameterization](synthesis/order_three_roots_and_sextic_lifts.md)
   and [comparison map](synthesis/actual_octic_root_lift_comparison.md) reduce
   first-compatible actual sextics to a map from a space of dimension at most
   three to an eleven-dimensional quotient. Retain K1, all rank strata, the
   quadric-cube correction and actual source images. Stop at a compatible
   nonzero sextic with its next root-lifting obligation identified, a covered
   component exclusion, or a precise missing boundary. The completed affine
   slice needs no further audit or mate search. Even a full smooth-root
   exclusion would remain within the stated saturated/movement-two bridge.
   This is distinct from the degree-(6,6) sector in item 2; arbitrary ruling
   frame changes are not ambient symmetries of the fixed C0.
5. **Finish the toric M incidence when closing that carrier source is the aim.**
   Use the [final center proof](synthesis/quintic_toric_center_incidence.md),
   retaining `M=0`, `Delta*K0*d*N*U0*V1*V2!=0` and `W | h*W'`, together with
   every projection-admissibility condition. The multiplicity patterns are
   `5+0`, `4+1` and `3+2`; U0, V1 and V2 have already been excluded. Set an
   explicit resource bound and stop at one admissible support-positive center,
   a coverage-certified exclusion, or a precise unresolved representation.
   Only a support-positive survivor warrants actual power descent; q squared
   is the degree-(5,8) target, not proof of descent of all powers. A negative
   answer closes this toric source, not every non-Gorenstein normalization.

The arithmetic mechanism offers another precise question: can its required
positive endpoint root defect occur in the actual complete-intersection,
annihilator, linkage and duality data? A useful comparison must add information
beyond the genus identity. The prescribed `p=7,n=7,E=6` finite diagnostic
should follow such a comparison, not substitute for it. Its result would
remain about that prescribed family of lifts.

## Other independent candidates

These are alternatives with different payoffs. A task can test an unproved
mechanism when its input, question and stopping outcomes are explicit. None is
an instruction to interrupt an already running investigation.

1. **Find admissible fibers of the actual elliptic construction.** Use the
   [five-parameter quadratic sections](synthesis/elliptic_double_inverse_construction.md).
   First test full inverse support on each geometric parameter fiber, retaining
   source smoothness, basepoint freedom, finite birationality, boundary fibers
   and all off-curve inverse points. A unit-ideal
   calculation in the total parameter ring is not the fiberwise condition.
   Then test pure-power descent on surviving strata. Stop at an admissible
   carrier, a covered family exclusion, or a precise unresolved stratum. The
   fixed member's extra inverse scheme has projective length twelve; it is not
   twelve asserted distinct points, and a higher mate degree cannot repair it.

2. **Test compatibility of the sextic cyclic cover with its embedded defects.**
   Start with a hypothetical characteristic-zero sextic pair having sole reduced
   support C0. The [selected sextic checkpoint](supplements/SEXTIC_PAIR_REDUCTION.md) already
   constructs the normal order-three cover and computes its necessary invariants,
   including \(K_Y^2=72\) and profile-dependent Euler characteristic and lower
   irregularity bounds. Recomputing these is not the next test. Investigate an
   additional compatibility with the index-nine local classes, polarization and
   three defect profiles, or construct such data. Under the additional general-pencil
   ADE hypothesis, use the [three surviving primitive-triple orbits](supplements/SEXTIC_ADE_REDUCTION.md)
   and the computed actual sextic source and first contact equation; higher
   contact and support are still open. Stop at a new comparison,
   actual model, or an identified missing hypothesis. Distinguish the normal
   covering surface from a resolution; smooth-surface inequalities require their
   own hypotheses. No contradictory upper bound is currently proved.

3. **Construct an actual homogeneous ACM thickening downstairs.** This target
   is weaker than AG, which in codimension two would give a complete intersection.
   Generic type two is allowed at the ACM stage. Start from an actual ideal or
   finite-projection source and determine the image's section module; do not
   transfer ACMness from the covering quadric. An exact supported ACM ideal,
   a diagnosed failure of the chosen source, or a concrete missing realization
   map is an interpretable outcome. The existing [section-defect theorem](synthesis/projected_thickening_section_defects.md)
   and [liaison constructions](synthesis/supported_linkage_operations.md) specify
   what the covered sources accomplish and where they fail.
   The torus method above is an alternative way to organize this objective;
   allow more than two generators and do not require the invariant special
   fiber itself to be ACM. A projection source must change the already
   excluded missing-section mechanism.

4. **Decide the surviving zero-defect two-node sextic pencil at its declared low-order level.** Under the existing conditional (6,16) hypotheses, use the actual pencil \(F_6=H_1H_2+\eta q^3\), with \(\eta\ne0\) necessary for a supported pair. Retain the eleven symbol equations, all twenty-five second-obstruction pairings, full-root torsion including node gluing, and complete cubic source incidence. Use the [rank-certified block map or its proved pivot cover](synthesis/rank_strata_and_sextic_lifts.md#7-pivot-charts-as-local-equations-for-the-geometric-zero-locus); do not cancel the multiplier at its zeros. Stop at coverage-certified emptiness, an exact point satisfying every declared condition with its unique actual sextic, or a precise indispensable missing representation. A survivor still needs a degree-sixteen mate, properness and sole support. This tests the whole surviving stratum, rather than another seed or a closed neighboring chart.

5. <a id="supported-length-five-degeneration"></a> **Decide relative defect in a fixed supported length-five degeneration stratum.** Over \(A=k[[t]]\), take \(I=(x,y)\) and regular-sequence ideals \(J\subset A[[x,y]]\) with quotient free of rank five, \(\sqrt J=I\), generic algebra \(k((t))[y]/(y^5)\), and closed algebra \(k[x,y]/(x^2+y^3,xy)\). Can the R-0030 relative comparison defect be nonzero? The [current control](results/supported_length_five_defect_specialization.md) has zero relative defect despite nonzero closed-fiber defect. Use the full relative initial ideal and \(\operatorname{in}_I(IJ)\). Stop at one verified relative counterexample or a coverage theorem for this exact stratum. Sample computations leave the rest of the stratum open. This is a local structural question.

6. **Track one actual equation obstruction as the quartic embedding varies.**
   The [projection-center moduli](supplements/QUARTIC_PROJECTION_MODULI.md)
   identify C0's special orbit among smooth projected quartics. Choose a
   characteristic-zero one-parameter family leaving that orbit while retaining
   smooth embeddings, and first construct a relative marked source for one
   specified lifting problem. Only then ask whether the corrected actual
   equation map persists, vanishes or changes rank. Stop at a represented
   comparison with controlled rank strata or a precise missing relative
   source. The existing coarse moduli coordinate does not distinguish all
   orbits, and the [fixed-symbol lemma](synthesis/global_lifting_interfaces.md)
   does not supply a quotient bundle under variation. This exploratory
   question changes the reduced embedding; it is not a torus translate of C0
   or a transfer theorem for its STCI status.

## Closed families and reasons to revisit them

| Covered result | What a genuinely new question would change |
| --- | --- |
| [Characteristic-zero quartic carriers](results/quartic_carrier_exclusion.md), including [normal carriers](results/normal_carriers.md) | A different characteristic, embedding or geometric application; no new mate search on an excluded fixed carrier |
| [Invariant supported CI ideals in characteristic zero](supplements/EQUIVARIANT_DEGREE_BOUNDS.md) | Study full invariant boundary ideals and deformations that may break symmetry; invariant reduced support alone does not make a CI ideal invariant |
| [Power and binary-mixture projected sources](synthesis/projected_thickening_section_defects.md) | An actual source or multiplication changing the missing-section mechanism, or the explicitly excluded characteristic-divisibility case |
| [Specified skew-line residual/Fitting operations](synthesis/supported_linkage_operations.md#classical-residual-operations-on-the-skew-line-link) | A different residual operation with a demonstrated effect on the actual ideal or support |
| [Fixed elliptic octic member](synthesis/elliptic_double_inverse_construction.md) | Change the carrier parameters and pass full inverse support; changing only its mate degree cannot remove extra inverse points |
| [Balanced degree-ten and palindromic target charts](synthesis/projection_and_elliptic_gluing.md) | The unfinished degree-twelve chart, a different contact distribution or a different source extension; target incidence alone is insufficient |
| [Extremal conductor boundary](synthesis/quadratic_covers_and_conductor_descent.md#12-embedded-curve-exclusion-of-the-minimal-boundary) | New information about embedded postulation or multiplication; adjacent-length enumeration alone supplies no upper capacity bound |
| [Gorenstein-normalized nonnormal quintics](synthesis/quintic_gorenstein_normalizations.md) | A non-Gorenstein source or a genuinely different carrier regime; increasing mate degree does not reopen this class |
| [Globally ADE quintics in degree (5,8)](synthesis/quintic_octic_surface_constraints.md) | A non-ADE singularity or a different degree pair; repeated first symbols are already covered |
| [Quartic Milnor budget comparison](synthesis/pencil_milnor_budget.md) | Additional information beyond the local multiplicity and complete-ideal bounds; the existing global inequality is not an independent quartic obstruction |
| [Order-three affine four-parameter slice](synthesis/order_three_roots_and_sextic_lifts.md) | A justified part of the full parameter locus or a different construction objective; all 24 geometric points already fail the actual sextic tests |
| [Exact Chow bundle reformulation](synthesis/chow_bundle_maps.md) | An operation producing the prescribed map with the required determinant, or a new restriction on every such map; arbitrary Chow-power determinants do not supply it |

## Questions still needing a workable entry point

The surviving universe remains wider than these tests: higher-index and non-Cartier carriers, multiple-branch inverse support, nonsaturated and extra-generator normal patterns, common generic singularities, non-Gorenstein separated branches, and rank-zero matrix transitions are not exhausted. Neither recent success nor an equivalent reformulation makes one program compulsory.

Promising broader questions include realizing singular conductor gluing compatible
with an actual projection, passing from the [spectral graded families](synthesis/spectral_determinant_schemes.md)
to actual ambient equations, and extending [tame projection sections](supplements/TAME_PROJECTION_SECTIONS.md)
to other covers. All-power spectral splitting is already in the maintained
account; its ambient realization is the remaining bridge. These questions need
precise source and comparison hypotheses. Three comparisons narrow the next test.

- For a surviving degree-at-least-five family, link the [normal-flatness](results/saturated_first_relation_normal_flatness.md),
  [resultant](results/nonsaturated_first_relation_resultant.md),
  [socle](results/full_conormal_socle_budget.md), and
  [constant-relation lifting](results/constant_first_relation_lifting.md)
  tests to actual homogeneous pairs. Check saturation and properness before sole support.
- For a finite flat or curvilinear family, compare the
  [filtered equation defect](results/local_filtration_comparison_defect.md)
  with [quasiprimitive residual cycles](results/quasiprimitive_residual_cycles.md)
  and the [explicit quartic residual geometry](results/ci_quartic_explicit_residual_geometry.md).
  Seek a proved comparison or a counterexample under stated hypotheses.
  An exceptional vertical curve alone gives no residual curve downstairs.
- Beyond the [bounded-index exclusion](results/normal_carrier_bounded_index_exclusion.md),
  determine which [index and socle constraints](results/normal_carrier_index_socle.md)
  and [pointwise conductor defects](results/pointwise_conductor_socle_defect.md)
  extend to higher index, nonnormal carriers, or inverse support outside the
  singleton Cartier hypotheses.
The surface-normalization conductor and the separated quadratic-cover conductor
are different objects; their bounds cannot be combined without a proved map.
A proposed generalization remains a question until its proof and review are
incorporated, regardless of an encouraging special case.
