---
id: STCI-F-0009
type: framework
title: Local cohomology and simultaneous ancestors
status: in_use
scope: "#scope"
bridges: "#bridges"
---
# Local cohomology and simultaneous ancestors

## Scope

For \(S=k[x,y,z,w]\), \(I=I_{C_0}\), and \(M=H_I^2(S)\), multiplication
in \(M\) retains normal principal parts that are invisible to the reduced
curve. The [local cohomology and conormal account](../../arguments/local-cohomology/local_cohomology_conormal_geometry.md)
relates this module to transverse jets. One obstruction strategy would
show that \(M\), in characteristic zero, is not quasi-cyclic; the
[literature on Hellus–Hübl](../../literature/README.md#hellus--hübl-2016)
gives the context for using two global equations in this comparison.
One can also ask a bounded question about two specified socle targets
and actual multipliers of a fixed degree.

In the fixed quartic multiplier problem, the
[finite direction reduction](../../results/quartic_ancestor_direction_reduction.md)
uses a quadratic moment of the common normal direction together with the
full actual multiplication tensor. It excludes primitive directions of
degrees zero and two and the linear endpoint boundary. The surviving
directions lie on a line and a degree-twelve curve; solving the top
coefficient condition on them leaves two distinct lower target equations
and ambient coprimality. The
[full two-target question](open_quartic_ancestors.md) gives the
normalization, the exact remaining conditions, and the independent
all-stage and endpoint controls.

## Mathematical scope and interfaces

The [finite direction reduction](../../results/quartic_ancestor_direction_reduction.md)
applies to the specified quartic test; the
[two-target equations](open_quartic_ancestors.md) remain unresolved.
The [polynomial-dual argument](../../arguments/local-cohomology/polynomial_duals_and_affine_pencils.md)
and [all-stage obstructions](../../arguments/local-cohomology/local_cohomology_ancestor_obstructions.md)
apply to their stated families, not arbitrary multipliers.
[Formal normal geometry](../formal-normal-geometry/index.md) shares
normal directions, filtrations, and embedded-structure questions;
[residual construction](../residual-construction/index.md) provides a
complementary geometric interpretation when actual multipliers give
proper pairs. The formulations are related without being equivalent.

## Bridges

Work on the two surviving interior components in the actual equation
tensor. Preserve the full kernel of top-and-quadratic data because different
kernel vectors can admit different lower corrections. The
[polynomial-dual technique](../../arguments/local-cohomology/polynomial_duals_and_affine_pencils.md)
and the [all-stage examples](../../arguments/local-cohomology/local_cohomology_ancestor_obstructions.md)
give mechanisms for excluding declared families while retaining all
allowed lifts. A higher-degree multiplier brings different source and
principal-part spaces; the fixed quartic test cannot supply full-module
coverage.

A common ancestor and an embedded thickening are different realizations.
Even a positive quartic ancestor answer has a residual consequence: the
[generic-length calculation](../../arguments/local-cohomology/direction_and_apolarity.md#2026-10-05-localcoh-generic-length)
gives a residual cycle of degree four for any such pair. The characteristic-zero quartic carrier theorem does not answer
this fixed two-target question.

### Does the conductor quotient retain the two targets?

For an actual supported CI in the separated quadratic cover, the
[conductor contains the relative socle](../../arguments/linkage/endpoint_lattice_capacity.md#fixed-local-cohomology-targets-and-what-they-cannot-see). Thus the two fixed socle targets become zero in the conductor quotient; it cannot supply the separating covector directly. A transport must keep the full multiplication image and the actual target values, for example through the degree-and-contact shift, rather than identify the targets with conductor classes. The first five added multiplier directions on the quartic shift still need to be evaluated.
