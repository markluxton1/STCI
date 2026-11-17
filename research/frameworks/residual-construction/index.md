---
id: STCI-F-0007
type: framework
title: Residual cycles, attachment, and construction by deformation
status: in_use
scope: "#scope"
bridges: "#bridges"
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

### Two presentations of fixed-degree multiplicity

The [normal-jet rank strata](../../arguments/residuals/marked_deformation_and_absorption.md#fixed-degree-multiplicity-strata-of-actual-pairs)
and the [Chow-divisibility filtration](../../arguments/torus_hilbert_boundary.md#reconciled-chow-filtration-and-finite-sextic-weight-partition)
describe the **same closed condition on actual proper containing pairs**:
\(m_C\ge r\). The first uses finite transverse multiplication
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
