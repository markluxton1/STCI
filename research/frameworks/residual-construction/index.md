---
id: STCI-F-0007
type: framework
title: Residual cycles, attachment, and construction by deformation
status: in_use
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0075, STCI-R-0076]
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
