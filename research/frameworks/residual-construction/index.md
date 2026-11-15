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

## Mathematical ownership and retrieval

This Framework owns the residual cycle of an **actual proper pair**, its
generic length, attachment, and deformation or absorption. Start with
[generic length and common normals](two_surfaces.md#21-generic-length-and-common-normal-directions),
then [the distinct residual mechanisms](residual_geometry.md#residual-statements-and-their-distinct-mechanisms)
and [attachment versus global constructions](residual_geometry.md#attachment-and-actual-global-constructions).
The [formal-normal Framework](../formal-normal-geometry/index.md) owns
filtered local ideals and simultaneous carrier compatibility; the
[global-equation Framework](../global-equation-realization/index.md) owns
actual homogeneous source realization. Neither local contact nor an
exceptional-divisor curve alone proves projective residual support.
The [spectral Framework](../spectral-roots/index.md) owns Picard-root input;
this Framework owns the residual-degree consequences of an actual octic pair.

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
