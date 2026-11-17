---
id: STCI-F-0006
type: framework
title: Global equation realization for supported intersections
status: proposed
scope: "#scope"
bridges: "#bridges"
---
# Global equation realization for supported intersections

## Scope

For the fixed embedded quartic \(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), organize what it takes for two *actual homogeneous forms* to have a prescribed supported intersection. The characteristic-zero STCI question remains open in unrestricted degree. A local multiple structure, normal symbol, cycle, Chow equation, complement pencil, or abstract bundle section retains only part of a global pair. The [global equations account](../../arguments/equations/global_equations_and_constructions.md) gives the geometric mechanisms; the [actual equation-jet filtration](../../arguments/equations/global_equation_jets.md) tracks their source maps.

For a proper pair of degrees \((a,b)\), the cycle identity \(ab=4m_{C_0}+\deg R\) makes \(m_{C_0}=ab/4\) equivalent to sole support. This is an exact existence reformulation, not an independent multiplicity bound. A viable obstruction must supply a structural restriction on **arbitrary actual pairs**, beyond the classical intersection formula or a change of parameter space.

The fundamental object is the labelled map
\(\mathcal O_{\mathbf P^3}(-a)\oplus\mathcal O_{\mathbf P^3}(-b)\to I_{C_0}\)
whose components are the equations. Its image must define a proper complete intersection and have no residual support if the goal is STCI. The [Sylvester Hom identity](../../arguments/equations/chow_bundle_maps.md#the-prescribed-sylvester-bundles-already-retain-the-equations) recovers forms directly from a map of the prescribed bundles; the required nonzero Chow-power determinant is still an existence condition. The [complement calculation](../../arguments/equations/complement_section_obstructions.md) distinguishes the checked continuous and primary algebraic conditions from actual homogeneous section realization. The [Chow/bundle and complement criteria](../../arguments/equations/global_equations_and_constructions.md#geometric-orientation-the-locus-of-globally-presented-multiple-curves) are equivalent formulations or necessary shadows only when their stated hypotheses hold; a cycle identity or a section on the complement does not by itself provide homogeneous lifts with the required base locus.

## Interfaces

[Formal normal geometry](../formal-normal-geometry/index.md) concerns local
compatibility; [carrier normalization](../carrier-normalization/index.md)
requires full inverse support and conductor descent; and
[residual construction](../residual-construction/index.md) tracks residual
cycles. None alone supplies a proper homogeneous pair with sole support.
[Projection and liaison](projection_and_liaison.md) studies supported ACM
sources and section defects.

## Available mathematics and controls

- Actual source spaces at fixed degree and normal order and their successive lifting quotients are computed in [global equation jets](../../arguments/equations/global_equation_jets.md). They show why independently selected sections of \(\mathrm{Sym}^r(I/I^2)\) need not come from equations. Finite compatible-jet existence is not an effective bound on all degrees: no general all-degree cutoff is established from a rank plateau or a finite truncation.
- The [octic/root comparison](../../arguments/spectral/actual_octic_root_lift_comparison.md) has an actual source map and a proper pair of transverse length eight with residual degree 32. This illustrates compatibility without sole support, not a solution to the unrestricted question.
- [Projected thickenings](../../arguments/linkage/projected_thickening_section_defects.md) distinguish an ACM source upstairs from its image in \(\mathbf P^3\): the displayed power and binary-mixture images fail ACM when the positive degree product is nonzero. This does not exclude other projected sources or arbitrary supported thickenings.

## Bridges

The unresolved implication is from compatible local/normalized data to two homogeneous sections whose full intersection is supported exactly on \(C_0\). A viable bridge must identify the actual source spaces, lift every required jet through their quotient maps, handle base points and conductor gluing, and then prove properness and eliminate residual components. Conversely, a universal obstruction must cover all equation degrees; the existing fixed-degree calculations and actual jets do not supply an effective all-degree bound.

For witness bounds and fixed-degree tests, see [exact finite certificates](../../arguments/equations/bounded_equation_certificates.md). A separate question asks how an actual equation obstruction changes as the [embedding varies](bounded_equation_search.md). Use [projection and liaison](projection_and_liaison.md) for the companion construction interface. The shared literature records the hypotheses for
[Chow and determinantal representations](../../literature/README.md#chow-forms-and-global-determinant-representations)
and for [affine results and the projective gap](../../literature/README.md#affine-lci-theorems-and-the-projective-gap).
