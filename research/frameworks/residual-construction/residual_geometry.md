# Residual intersections: actual cycles, attachment, and equation sources

For the fixed quartic, the unrestricted characteristic-zero STCI question
remains open. Study a general proper pair \(Y=V(F_a,G_b)\) through
\(C=C_0\) by its actual cycle \([Y]=m[C]+R\), with
\(\deg R=ab-4m\). A strict bound on generic length can force residual
degree; a curve on an exceptional divisor alone cannot. [Chapter 2](two_surfaces.md)
introduces the approaches; this page routes directly to their full proofs.

## Residual statements and their distinct mechanisms

| Statement | Proof home and essential scope | What it does not supply |
|---|---|---|
| [R-0019](../../results/quasiprimitive_residual_cycles.md) | [Saturated quasiprimitive flag proof](../../arguments/residuals/quasiprimitive_residual_cycles.md): triangular multiplication determinant, finite-flat identification, proper auxiliary residual zero-cycle | A scheme equality or a residual-curve theorem for arbitrary nonsaturated flags |
| [R-0023](../../results/ci_quartic_explicit_residual_geometry.md) | [Explicit quartic residuals](../../arguments/residuals/explicit_quartic_residuals.md): exact homogeneous ideal unions, Jacobian and connectedness certificates | A classification of quartic pairs |
| [R-0024](../../results/ci_quartic_fixed_boundary_smoothing.md) | [Fixed-boundary smoothing](../../arguments/residuals/fixed_boundary_smoothing.md): actual global tangent maps of ranks 19,5,24 and node-family charts | Removal of residual degree or an explicit polynomial coefficient arc |
| [R-0025](../../results/ci_fixed_sextic_jet_rigidity.md) | Full proof in its record: one selected sextic, arbitrary mate degrees, normalization and three boundary valuations; even-degree maximal mates are rigid in characteristic zero | A theorem on arbitrary sextics |

The explicit (2,3) quartic benchmark has a smooth degree-twelve genus-sixteen
residual meeting \(C\) in eighteen transverse points. At the (1,1) benchmark
that residual is a line and smooth degree-eleven genus-twelve curve with
five transverse internal nodes. The five smoothing parameters remain
independent with the exact marked attachment divisor fixed. Smoothing changes
residual singularities, not the cycle degree twelve.

For the fixed sextic, [R-0025](../../results/ci_fixed_sextic_jet_rigidity.md#proof)
now gives \(n\le\lfloor b/2\rfloor\) for every proper degree-\(b\) mate,
so at degree sixteen \(m_C\le16\) and \(\deg R\ge32\), sharply.
Three actual boundary lines of the affine normalization control polynomial
vanishing; a noncancellation argument replaces the rank-683 dependence.
In characteristic zero every even-degree maximizer is a carrier multiple
plus a scalar quadric power, so its full intersection scheme is fixed.
The bound extends outside characteristics 2 and 37; the record states the
more restricted positive-characteristic equality scope. The old normal-division
certificate remains an independent check of its weaker order-twelve kernel,
not a premise of the sharp theorem. No other sextic is covered.

## Attachment and actual global constructions

The [full-primary attachment account](../../arguments/residuals/residual_capacity_and_constructions.md)
proves the exact marked-divisor identity including non-lci torsion, its
normal-nilpotent correction to full attachment, universal degree bounds,
and necessary tests for residuals of degrees one and two. Its local control
has a unit determinant but marked attachment length two and full attachment
length six. This distinguishes a useful correction from a misleading
conormal-only detector.

The [normalization capacity account](../../arguments/carriers/normalization_residual_capacity.md)
explains the common nef mechanism for a carrier smooth along \(C\), normal
with marked singularities, or nonnormal with a single/multiple divisorial
inverse. Its smooth case gives the sharp uniform bound \(\deg R\ge ab/3\).
A positive Hodge gap gives capacity; a zero gap leaves a potential endpoint
and does not establish conductor descent. [Prescribed singular carriers](../../arguments/carriers/prescribed_singular_carriers.md)
realize arbitrary A-type local indices and actual smooth residuals cancelling
the local class, with exact attachment lengths.

The [all-degree construction account](../../arguments/residuals/residual_global_models.md) proves
generic smooth residual geometry and attachment-map dominance for
\(a,b\ge4\), and realizes every effective marked attachment divisor for
\(a,b\ge7\). All contact can be concentrated at one point while generic
multiplicity stays one and the smooth residual retains its full degree.
The [reverse-linkage account](../../arguments/residuals/residual_liaison.md) recovers equations from
the embedded once-linked curve, proves its relative flatness through
multiplicity jumps, and identifies the deformation space preserving this
incidence. Full-primary extraction is a different, potentially nonflat
operation.

## Exceptional geometry and what survives each model

The [two-blowup model](../../arguments/residuals/blowup_residual_geometry.md) retains actual sections,
\(B=\operatorname{Bl}_C\mathbf P^3=\operatorname{Bl}_\Gamma V_5\), both
exceptional divisors and both projections. Its anticanonical surface has
normalization \(E\) and conductor \(2(E\cap Q')\). An original trisecant
residual can contract to a point on \(V_5\); an exceptional curve can map to
a genuine curve there while recording only thickness along \(C\) downstairs.
The exact support test is on the graph.

The [Rees and vertical controls](../../arguments/normal-geometry/rees_and_vertical_controls.md) show that
all divisorial Rees valuations of a full lci curve ideal are visible over
generic curve points, with an exact coefficient/residue-degree budget. The
ordinary Segre numbers are fixed by the CI degrees. Nevertheless intrinsic
first-relation saturation defect and chosen-pair vertical degeneration can
grow without changing the generic filtered algebra. An explicit projective
pure-support example prevents vertical exceptional geometry from becoming
a residual-curve criterion.

## Valuations, finite jets, and formal geometry

The [valuation/contact account](../../arguments/residuals/valuations_and_residual_contact.md) distinguishes
parameter-ideal multiplicity recovered from full integral-closure data from
arbitrary colength, includes complete point-basis weights and residue degrees,
and proves the correct coefficient-adic domain and intrinsic flag construction.
Its contact cycle recognizes actual residual support by connectedness and
point multiplicity, but does not prove positivity for every pair. The four-line
control proves that branch contact need not equal the conductor boundary.

The [generic contact-depth theorem](../../arguments/residuals/generic_contact_depth.md) extracts a
power-invariant mechanism: per-level tangent budgets and Noether's formula
bound generic intersection by \((h+1)rs\), yielding depth and surviving-tail
requirements. On an unbalanced smooth quadric curve of type \((1,n)\),
every hypothetical supported pair needs generic contact depth at least
\(n-1\). Deep contact is locally possible; a global upper-depth theorem
remains missing.

The [finite normal-jet criterion](../../arguments/residuals/finite_normal_jets.md) is exact at fixed
degrees, even for singular integral curves and weighted reducible curves.
Its sharp cutoff is \(M+1\) without a prior properness check; known
coprimality permits cutoff \(M\). All monomial multiples of the two actual
jets enter the ideal matrix. Scalar equation parameters remain in the
constant field even when matrix rank is computed over \(k(C)\).
No witness-degree bound or general solver is supplied.

The [full formal account](../../arguments/residuals/formal_residual_visibility.md) shows what remains
after generic localization: attached residual germs can have exactly the
same generic transverse algebra as a sole-support germ. Completion along
\(C\) retains the attached germs. Projective-space G3/Lefschetz extends two
globally glued **fixed-twist** all-order sections; uniform power containment
then gives an exact STCI reformulation. Compatible finite jets and arbitrary
local generators are weaker data.

## Root configurations, conductor, and characteristic

The [toric sextic configurations](../../arguments/torus_sextic_residuals.md)
give eigenform intersections with eight or six quotient length units and
explicit boundary cycles, a sharp length-eight bound for all eigenform sextic
pairs in every characteristic, and mixed-weight splitting and absorption
families. Their full three-generator limit remains ACM with the CI Hilbert
series, but has a necessary degree-ten equation and residual boundary curves.
These are actual curve configurations downstairs; they are not exceptional
vertical components or a sole-support deformation.

The [root-pencil account](../../arguments/torus/root_pencil_geometry.md) supplies a continuous
four-sheet family with fixed \(9p_0+9p_\infty\) marked boundary, varying
elliptic branch modulus, a double-marked-component member, residual-root
collisions and a weighted-line boundary at infinity. It retains the
conductor/generalized-Jacobian calculation, a larger-delta eight-component
control, balanced-boundary interpretation and two-scale mixed-characteristic
collision tree. These are explicit laboratories, not invariants of every
pair.

The [embedded quotient comparison](../../arguments/torus_embedded_quotients.md)
separates abstract finite algebras from their projective images. Its flat
characteristic-zero four-root collision has genus 28, whereas the prescribed
characteristic-two quartic CI has genus 33. Its actual endpoint lattices explain
the difference without forbidding characteristic-zero nonreduced quotients.

The degree, length, linkage and finite-scheme attachment mechanisms have
characteristic-free forms with their stated hypotheses. The balanced-normal
first-blowup constants require characteristic different from two; the
certified rational residual and fixed-boundary examples have characteristic-zero
scope. Every positive characteristic admits an actual supported pair with
a quartic carrier; its [complete construction](../../arguments/arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier)
is displayed alongside the characteristic-zero carrier exclusion. Individual
mechanism homes state which additional arguments extend and which do not.
A characteristic-two coalescence or positive-characteristic supported endpoint
is never used as a characteristic-zero obstruction.

The [proper-cut and layerwise identities](../../arguments/residuals/residual_capacity_and_constructions.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component) retain the attachment correction explicitly. A positive complementary-layer failure on an actual curvilinear primary gives a residual-degree lower bound. The [attachment quotient](../../arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers) gives the dual annihilator tower without curvilinearity. Neither implies that a missing formal symbol produces such a defect.

The [finite marked-index rigidity gate MJ1--MJ4](../../arguments/residuals/blowup_residual_geometry.md#finite-index-rigidity-of-higher-marked-jets)
illustrates why the actual image algebra must be
closed under multiplication, even when a proposed
full-rank lattice has the correct determinant.
It yields a low-jet restriction on the primitive
marked equality boundary, not on arbitrary
curvilinear or higher-embedding-dimension
residual primaries.

## Exact remaining interfaces

A family-level jet obstruction must control **every actual mate**, including
rank-drop strata, before converting length to positive residual degree.
A saturated-flag divisor formula must establish finite flatness, saturation,
and proper auxiliary intersection before it applies. A formal construction
must produce the two globally compatible fixed-twist equations and uniform
power containment. None of these missing implications is supplied by merely
passing local numerical tests or observing residuals in examples.

A conditional sextic symbol has a further lift freedom \(\eta q^3\).
Thus a fixed-lift cubic failure cannot exclude all sextics with that symbol
without checking this extra direction. The complete corrected calculation
belongs to [the conditional sextic account](../../arguments/carriers/normalization_conductor_phase2_addendum.md);
its leading-symbol and higher-jet tests remain distinct from a proper-mate
length bound.

## Related proof developments

- [Special planes, lines, and their incidence with containing surfaces](../../arguments/curve/special_plane_and_line_sections.md)
