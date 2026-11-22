---
id: STCI-F-0007
type: framework
title: Residual cycles, attachment, and construction by deformation
status: in_use
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0075, STCI-R-0076, STCI-R-0077]
    to: [STCI-F-0007]
    at: "#interfaces"
---
# Residual cycles, attachment, and construction by deformation

## Scope

Start with a proper pair through the fixed quartic, with cycle
\([V(F_a,G_b)]=m[C_0]+R\) and \(ab=4m+\deg R\). The multiplicity \(m\)
comes from the actual generic transverse algebra. Degree exhaustion then
tests sole support. A curve on the exceptional divisor may instead account
for contact at a single point of \(C_0\); a separate comparison is needed to infer residual support in projective space.

The [geometry of two surfaces](two_surfaces.md) relates generic normal
length to the common graph and the two contraction maps. The
[residual geometry](residual_geometry.md) distinguishes the capacity,
attachment, and actual equation mechanisms. They are useful both for
constructing containing intersections and for proving that a specified
source always leaves residual degree.

## Interfaces

For all slopes possible under sole support, an isolated or disconnected
common zero set of the two leading forms on the exceptional surface
forces residual degree. Isolated scheme lengths and attachments to
distinct connected curve components give an explicit lower bound.
[Residual attachment from the two symbols](../../results/connected_normal_directions.md#connectedness-and-residual-attachment).

[Generic length and common normals](two_surfaces.md#21-generic-length-and-common-normal-directions),
[residual mechanisms](residual_geometry.md#residual-statements-and-their-distinct-mechanisms),
and [attachment constructions](residual_geometry.md#attachment-and-actual-global-constructions)
are distinct from realizing a projective residual scheme by homogeneous
proper equations. The realization question also connects to
[formal normal geometry](../formal-normal-geometry/index.md) and
[global equation realization](../global-equation-realization/index.md);
[spectral roots](../spectral-roots/index.md) supplies graded Picard data
for octic constructions.

For integral quintics with toric normalization, every proper mate
candidate through \(C_0\) has a positive-degree residual curve. The
proof detects an extra point above \(C_0\) on the normalization. In
the elliptic octic construction, the length twelve counts zeros on a
divisor of the source quadric. An off-curve zero obstructs a mate on a
birational fiber, while computing \(\deg R\) requires an actual pair of
surfaces in \(\mathbf P^3\). [Quintic exclusion](../../results/toric_quintic_carrier_exclusion.md) ·
[Elliptic support theorem](../../results/elliptic_inverse_support.md)

### The normalized carrier refines the graph capacity

The [branch valuation and marked-ideal square identity](../../arguments/carriers/numerical_surface_pullback.md#branch-valuations-and-the-actual-first-blowup) refines the scalar first-graph slack by resolving a specified integral carrier. The strict mate is the actual divisor `div(G)-qD`; its horizontal and vertical coefficients retain the branchwise and special-point data. For sole support the total exceptional energy must be supplied by excess branches, and the normalized branch matrix governs the allowed positive valuation vector. No-vertical single-root carriers are excluded in every degree; [Cartier ruling clusters](../../arguments/carriers/numerical_surface_pullback.md#cartier-test-divisors-and-the-degree-three-per-order-boundary) give explicit all-order residual-root divisibility on the degree-three-per-order locus. These are new fixed-carrier necessary filters, not additive scalar residual bounds or a constructed residual absorption. Review pending.

The [ample strict-carrier compression](../../arguments/residuals/blowup_residual_geometry.md#lefschetz-compression-on-ample-strict-carriers) transfers the actual-index method to a smooth sole-support strict intersection on the first blowup. If its multiplicity is \(c\) and the ample strict carrier is generically regular along it, then its index lcm \(R\) satisfies \(c/R\mid\gcd(a,p)\). Under the stated section-lifting inequalities, a nontrivial quotient gives a lower-degree ambient mate. On the \((3p,4q)\) edge with \(p\le q\) those inequalities hold. In particular the entirely-thick \((6,8;2,2)\) case has a generically curvilinear first strict intersection, a normal general strict octic and an actual index-eight point (LC4). This uses R-0077 and the characteristic-zero low-degree exclusion; it neither proves normality of the original octic nor excludes the pair. Review pending.

The [pointwise graph resultant and finite modification formulas](../../arguments/residuals/blowup_residual_geometry.md#socle-defects-on-the-two-presentations-of-the-first-graph) identify the divided exceptional resultant with \((c-1)\Theta+D_{\rm top}\) for a generically curvilinear sole-support strict CI, where \(\Theta\) is tangency of its normal line to the exceptional surface. This is the specialization of [CF1--CF4](../../arguments/normal-geometry/curvilinear_genus_and_defects.md#cartier-cuts-and-finite-modifications-of-the-saturated-filtration), valid for actual Cartier cuts and finite modifications of curvilinear thickenings in arbitrary smooth ambient threefolds. On the \((3p,4q)\) edge, the finite map to the image quintic CI in \(V_5\) has length defect \(pq(q-1)\) at the marked point, with pointwise top-defect change \((c-1)\xi-(q-1)\), \(\xi=0,1\) from the actual conormal modification. The [marked-line obstruction ML9](../../arguments/residuals/blowup_residual_geometry.md#all-orders-the-marked-line-comparison-by-interpolation) eliminates primitivity at the prescribed marked point for every mixed \((3p,4q)\) edge pair with \(2\le p\le q\), without ADE or normality assumptions. Thus the globally primitive mixed \((6,8)\) row is excluded, not merely conditionally: only the mixed slope-four and endpoint slope-five rows remain there, with positive marked defect in the mixed row. Of the five necessary global primitive order pairs on the full edge, mixed directions survive this test only at \((10,4),(21,3)\); endpoint directions remain subject to their separate splitting and line contact. The [full marked finite-modification lattice](../../arguments/residuals/blowup_residual_geometry.md#full-marked-finite-modification-lattice-in-the-primitive-at-the-point-stratum) identifies the completed image ideal for \(q=2\) in the primitive graph stratum as \((y^2-x^2t,t^{2p})\), with multiplication defects \(D_j=2\lfloor j/2\rfloor\); for a generically regular image carrier the local index is two (marked \(D_{2p+1}\)) or \(4p\) (multiplicity at least three). The opposite [smooth marked image-carrier lane](../../arguments/residuals/blowup_residual_geometry.md#the-opposite-marked-stratum-a-smooth-image-carrier-and-a-forced-graph-defect) gives strict equations \(xv=t^{2p},v^q=0\), defects \(D_j=\lfloor j/(2p)\rfloor\) and marked index \(2p\) on the strict carrier. A degree-two image mate there would descend to an original degree-four mate by exact conic trace cancellation, so is excluded. For \(q=2\) and an integral smaller image carrier its minimal image mate degree is therefore four; for \(p=2\) an actual index-eight point away from the smooth marked point is forced. These deductions await independent review.

The [edge recovery theorem SC6](../../arguments/residuals/blowup_residual_geometry.md#recovering-generic-curvilinearity-in-all-orders-on-a-subset-of-the-edge) shows that on the mixed \((6,4q;2,q)\) edge the strict sextic always has order one, and for \(q\ge2\) a general strict carrier of the other equation is normal with at least \(9q-10\) distinct moving index-\(4q\) points. The first strict CI must be nonprimitive somewhere for \(q>2\). Across the full \((3p,4q)\) edge, global primitivity on the graph has only the five necessary order pairs \((2,2),(5,19),(6,8),(10,4),(21,3)\), by the [primitive edge arithmetic](../../arguments/residuals/blowup_residual_geometry.md#primitive-graph-structures-on-the-full-degree-threefour-slope-edge). This is not the classical primitive list on \(C_0\); it applies to the first strict intersection. The [normal K3 torsion theorem](../../arguments/carriers/normal_carrier_symbolic_torsion.md#a-uniform-torsion-bound-on-normal-k3-carriers) also gives an all-mate-degree bound \(R\le16\) on globally ADE degree-two image carriers in \(V_5\), with a mate there in degree at most eight; conic vanishing for an actual lift to the original problem is separate. The results are pending review.

### Two presentations of fixed-degree multiplicity

The [normal-jet rank strata](../../arguments/residuals/marked_deformation_and_absorption.md#fixed-degree-multiplicity-strata-of-actual-pairs)
and the [Chow-divisibility filtration](../../arguments/torus_hilbert_boundary.md#reconciled-chow-filtration-and-finite-sextic-weight-partition)
describe the **same closed condition on geometric points of the actual
proper containing-pair locus**: \(m_C\ge r\). Their natural
scheme structures need not agree: the normal-jet minors and the
pullback Chow linear equations are not asserted to generate the
same ideal or have identical infinitesimal structure. The first uses finite transverse multiplication
matrices and is adapted to local thickness and attachment questions;
the second is the pullback of
\(\mathbf P(Q^rE_{ab-4r})\) under the proper-pair Chow map and is
adapted to global cycle incidence and residual-degree bookkeeping.
In either presentation \(ab=4m_C+\deg R\), and multiplicity can rise
while residual degree falls along a specialization **remaining proper**.

Do not use Chow divisibility on an improper limiting pair or a
Hilbert-boundary cycle as a substitute for a flat residual
construction or two global defining equations. The fixed-degree
terminal condition is exact but does not show its stratum is nonempty.

The [attachment layer identities](../../arguments/residuals/residual_capacity_and_constructions.md#layerwise-attachment-duality-on-a-non-gorenstein-primary-component) bound actual attachment from below using complementary normal-layer defects of the full primary. [Local duality](../../arguments/local-cohomology/actual_pair_coregularity.md#actual-attachment-equation-modules-are-the-dual-annihilator-layers) identifies the actual attachment equation quotient with dual annihilator layers. The [toric collision](../../arguments/torus/fixed_carrier_chow_arrangements.md#all-order-primary-structure-and-attachment-on-the-classified-carrier) shows full attachment can increase during absorption. [Finite graph transfer](../../arguments/residuals/blowup_residual_geometry.md#signed-finite-transfer-throughout-the-interior-equality-boundary) now allows an image residual conic. These exact comparisons do not prove universal positivity.

The [independent TS4 quadric-cut calculation](../../arguments/torus/fixed_carrier_chow_arrangements.md#a-fixed-auxiliary-quadric-detects-the-same-punctual-defect-at-every-collision)
verifies the sign and both endpoint coefficients
in the new residual-corrected cut formula
on a whole actual arrangement family.
Despite a change in generic marked
multiplicity, the punctual cut divisor
\(3(N-3)p_0+(N-1)p_\infty\) is fixed.
The residual attachment is not recoverable
from that cut divisor alone.

## How residual degree can change

The [explicit quartic pairs](../../arguments/residuals/explicit_quartic_residuals.md)
show different attachment and splitting at the same residual degree; the
[fixed boundary deformation](../../arguments/residuals/fixed_boundary_smoothing.md)
smooths internal nodes with the marked attachment divisor fixed. In the
[marked absorption construction](../../arguments/residuals/marked_deformation_and_absorption.md),
a different deformation transfers part of the residual cycle into the
multiple structure. There are three separate lifts to check: the marked
quotient, its common embedded structure, and the actual pair of equations.
A local length increase or a smoothing of the residual abstract curve
need not give this transfer.

The [fixed-toric-quartic collision](../../arguments/torus/fixed_carrier_chow_arrangements.md#an-actual-partial-collision-in-characteristic-zero)
is another actual flat proper-pair control: marked multiplicity rises from one
to two while residual degree falls from twelve to eight. The three-support
constraint makes eight the sharp floor in this fixed-generator \((4,4)\)
translated-cycle locus. It realizes partial absorption but cannot be iterated
to sole support within that locus. Its total family is not supported on \(C_0\)
alone, so the supported quadratic-graph comparison needs a separate bridge.
The [general Chow moment](../../arguments/torus/chow_arrangement_moments.md)
also prevents complete coalescence in the Chow closure of invariant CI
arrangements in characteristic zero, even with moving carriers. The
[non-invariant quartic orbit](../../results/quartic_chow_pencil_classification.md)
shows that other repeated cycles occur beyond the invariant quartic
Chow closure while still satisfying the first moment. Its fixed cycle
supplies a flat-limit control without any increase of marked multiplicity.
The [comparison of mates on the same carrier](../../arguments/torus/fixed_surface_restriction_lifts.md#comparing-multiplicities-on-one-fixed-carrier)
gives a different transfer that keeps the ambient carrier fixed.
Two differing multiplicity ratios on two translates give a sole-support
mate by extending a rational section. In the
[sextic test](../../arguments/torus/fixed_surface_restriction_lifts.md#a-two-translate-sextic-construction-criterion),
one proper pair and the involution would supply both ratios. Existence
of that pair is open.
The initial proposed \((5,4)\) sextic multiplicity partition is
already **excluded** by the involution--Bézout inequality
\(4|n_+-n_-|\ge6\). Only the positive two-support partitions
\((6,3),(7,2),(8,1)\) and reversals remain numerically;
all are excluded if both common endpoints are smooth or Du Val
by the [orbit-lattice/contact and mixed Hodge theorem](../../arguments/torus/fixed_surface_restriction_lifts.md#the-sextic-symmetric-arrangement-must-escape-ade-at-an-endpoint),
pending independent audit. The remaining fixed-carrier absorption construction would need at least one worse endpoint, not simply a carrier with higher ADE index.
The [finite-group multiplicity-lattice result](../../arguments/torus/fixed_surface_restriction_lifts.md#symmetry-and-the-multiplicity-lattice)
explains the algebraic mechanism behind the conditional transfer.


The [local-index attachment test](../../arguments/residuals/residual_capacity_and_constructions.md#local-index-forces-residual-attachment) gives a different necessary residual condition on every generically regular integral carrier: an actual multiplicity \(m\) requires every marked point where \(r_P\nmid m\) (including infinite order) to lie on the residual. The marked degree bound then gives a residual-degree lower bound from the number of such points. It is valid even when the normalized Hodge gap is zero; that gap together with finite downstairs index already decides fixed-carrier existence in some degree. The two residual lower bounds need not be additive.

The [two-blowup calculation](../../arguments/residuals/blowup_residual_geometry.md)
tracks the full normal ideal and distinguishes horizontal and vertical
exceptional contributions. For a *fixed* degree and actual proper pair,
the [finite normal-jet test](../../arguments/residuals/finite_normal_jets.md)
computes the generic length needed for exhaustion. A uniform bound in a
family has to include the actual equation parameter space and its special
strata.

## Invariant residual chains and absorption

For an actual proper pair in any bidegree, remove the gcd \(H\) of its
extreme forms in one intrinsic torus direction. Let \(e_L\) be the
multiplicity of the disjoint line \(L_{12}\) in the intersection of the
remaining two forms, and let \(\kappa_L\) be the generic length there of
the first equation layer missed by both endpoints. Then
\(\deg R\ge e_L-\kappa_L\). If \(H\) is generically a unit on the line,
the extreme forms alone force residual degree at least \(e_L\). If the
full limit has sole support, all of \(e_L\) must instead occur in that
kernel. This distinguishes line-supported relations in a presentation
from a line actually present in the specialized cycle.
[Endpoint and residual degree proof](../../results/endpoint_equation_torsion.md#proof).

The [invariant orbit-curve analysis](../../arguments/torus_hilbert_boundary.md#invariant-residual-supports-and-absorption-limits)
sharpens the attachment problem: every reduced irreducible curve
invariant under the intrinsic torus and distinct from \(C_0\)
meets \(C_0\) only at the endpoints, **unless** it is the
coordinate line \(L_{12}\), which is disjoint from \(C_0\).
That line occurs in an actual invariant proper \((3,4)\)
intersection containing \(C_0\), connected through other
residual lines. Hence connectedness of the full intersection
does not force direct endpoint attachment of every residual
component. This rules out an overly restrictive incidence
model, without altering any previously established residual
degree bound.

Under flat specialization preserving the marked curve,
the coefficient of \([C_0]\) in the fundamental cycle
can increase by specialization of residual cycle; the
remaining residual degree decreases accordingly. A moving
invariant quartic can collide with \(C_0\) at cycle level,
but this does not construct a flat two-equation realization.
For absorption questions, distinguish **cycle transfer**,
**embedded Hilbert realization**, and **global generator
realization**. The unresolved implication belongs jointly
to this Framework, the [full torus boundary Framework](../torus-supported-boundaries/index.md),
and [global equation realization](../global-equation-realization/index.md).

## Bridges

- For a proper characteristic-zero pair through the fixed quartic, compute the generic transverse quotient of its component on the quartic in the fixed torus frame. If the linear map from its kernel to its quotient along the base tangent has rank below \(\lceil(4b-7)/7\rceil\), where \(b\) is the larger degree, the projective intersection has a residual curve. This detects residual support without classifying its components. [Generic movement test](../../results/torus_quotient_movement_bounds.md#statement).
- To iterate absorption, preserve the mark, lift the complete embedded
  ideal through the actual source spaces, and prove that the next proper
  pair transfers further cycle degree. The specified
  [quadric modification](../../arguments/residuals/quadric_modification_and_global_corrections.md)
  leaves positive residual degree throughout its full lift space.
- On a covered carrier family, seek an exact residual floor or construct
  pairs attaining its boundary. The
  [normalization capacity](../../arguments/carriers/normalization_residual_capacity.md)
  gives a nef comparison; equality may still require conductor descent
  on an [actual normalized carrier](../carrier-normalization/index.md).
- For proper sextic pencils through the surviving ADE triples with a
  first-order member and dependent quadric restrictions, the
  [sharp residual floor](../../arguments/carriers/sextic_ade_reduction.md#sharp-length-five-for-pencils-with-a-quadric-divisible-member)
  is sixteen. At equality the factorization \(G=qP\) splits the residual
  cycle into degree eight from the quadric and degree eight from the
  quartic \(P\), counted with intersection multiplicities.
- The [octic source](octic_multiplier_kernels.md) offers a concrete
  construction: determine the actual multiplier kernels and their fixed
  divisors. Where they generate jointly, the existing argument gives
  length eight along \(C_0\) and residual degree \(32\). The
  [spectral framework](../spectral-roots/index.md) supplies the root data;
  sole support for a proper \((8,8)\) pair requires length sixteen.
- The [torus boundary framework](../torus-supported-boundaries/index.md)
  supplies explicit residual splitting and transfer controls as well as
  a limit that needs an extra generator. A residual example can explain a
  mechanism without serving as a boundary point of the supported locus.
  Comparing the full normal cone with a [marked Quot incidence](../formal-normal-geometry/open_normal_geometry.md#comparing-the-normal-cone-with-marked-quot-incidence)
  requires a map retaining the relations used by the deformation.

The [quadric restriction and contact rigidity synthesis](quadric_restriction_and_contact_rigidity.md) distinguishes the degree-independent Picard-class obstruction to sole support from the sharp, computational sextic multiplicity bound. It reformulates the latter as a uniform symbolic-power vanishing on quartic carriers and identifies residual quartic cycles as possible geometric proof inputs, without asserting the vanishing has a calculation-free proof.

## A fixed sextic controlled by its normalization boundary

[R-0025](../../results/ci_fixed_sextic_jet_rigidity.md#proof) now bounds every
mate degree on one explicit sextic using three boundary valuations. In
characteristic zero a degree-b mate has branch order at most floor(b/2),
and every even-degree maximizer defines the same ideal as the quadric power.
The degree-sixteen bounds are sharp: multiplicity 16 and residual degree 32.
The retained rank-683 replay is independent weaker evidence, not proof-bearing
for this route. The Result separates the positive-characteristic bound and
equality scopes; it does not address other sextics or unrestricted STCI.

### Conditional boundary-valuation interface

For the **single fixed sextic** Fstar, R-0025 proves the sharp all-degree
bound by global divisibility by its marked Cartier equation and three
boundary valuations. Its [conditional criterion for other carriers](../../results/ci_fixed_sextic_jet_rigidity.md#conditional-interface-for-other-carriers)
separates the necessary checks: global divisibility on a normalization
chart, degree-dependent pole budgets, and no simultaneous positive
boundary orders for nonzero regular functions. A separate local
multiplicity comparison and positive residual-degree bound are required.
These hypotheses are verified for Fstar only; establishing them on other
carriers is an open route, not a universal sextic or global STCI exclusion.

### What a moving residual still does not supply

The [marked thick-quadric family](../../arguments/residuals/marked_deformation_and_absorption.md#the-twelvefold-residual-moves-on-the-thick-quadric)
moves the twelvefold line and changes where its contact lies, while
its degree cannot drop farther on that carrier. This is not the inverse
support/descent problem on a normalization. The next useful absorption
test needs a direction in both actual global equation spaces that
preserves properness and raises the generic marked length; track the
entire residual cycle, not just its moved line or attachment divisor.
No such degree-decreasing step is known on this control.
