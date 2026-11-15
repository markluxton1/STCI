---
id: STCI-F-0005
type: framework
title: Carrier normalization, projection, and conductor descent
status: in_use
scope: "#scope"
bridges: "#bridges"
aliases:
  STCI-Q-0001: "#projection-and-conductor-descent-for-the-three-cartier-singleton-models"
---
# Carrier normalization, projection, and conductor descent

## Scope

This framework studies a fixed integral carrier \(S\subset\mathbf P^3\)
containing the embedded rational quartic
\(C_0=[s^4:s^3t:st^3:t^4]\), and asks whether a second homogeneous
surface cuts out \(C_0\) set-theoretically on it. The decisive data live on
the normalization: the **full reduced inverse support**, its divisor classes,
the actual polarization, and descent across the full conductor. A numerical
class relation upstairs is necessary, but need not descend to an equation on
the nonnormal carrier.

The companion developments [carrier descent](carrier_descent.md),
[degree exclusions](degree_exclusions.md), [technical proof interfaces](quartic_proof_interfaces.md),
[normalization and phase comparisons](normalization_conductor_projection.md), and
[open carrier cases](open_carrier_cases.md) collect the geometric orientation,
scoped low-degree exclusions, and remaining interfaces. Proofs remain in
their cited sources. The full-inverse-support and descent questions below remain open outside their covered cases.

## Normalization and full inverse support

Let \(\nu:X\to S\) be the finite normalization and put
\(H=\nu^*\mathcal O_S(1)\). The reduced inverse image
\(W=(\nu^{-1}C_0)_{\rm red}\) can have several curve components, components
mapping with degree greater than one, and isolated points. If a mate exists,
its pullback has support exactly (W\); an isolated point away from those
curves already obstructs it. For curve components \(\Gamma_i\), the pulled
back divisor has the form \(\sum_i n_i\Gamma_i\), with every \(n_i>0\),
and is linearly equivalent to \(bH\). This full-support requirement must
precede any reduction to a preferred branch.

For a fixed carrier, the exact criterion combines positive divisor relations
in \(\mathrm{Cl}(X)\) with the torsion behavior of the section's **full
conductor-unit classes** away from \(C_0\). In particular, nilpotent
conductor structure can impose descent conditions invisible on the reduced
double locus. A class-group relation alone is not a mate. See the
[fixed-carrier conductor criterion](../../results/fixed_carrier_conductor_criterion.md)
and [descent algebra](../../arguments/carriers/conductor_descent_algebra.md).

The normal and nonnormal settings require distinct arguments. For specified
normal hypersurfaces in characteristic zero, the Hodge criterion is a
Q-Cartier and self-intersection test; realizing its numerical equality on an
actual carrier is separate. For nonnormal surfaces, the full conductor and
normalization map govern descent. Smooth-normalization/full-conductor
comparisons have their own hypotheses and controls in
[carrier conductor–differential comparison](../../arguments/carriers/carrier_conductor_differential_comparison.md).
These statements do not transfer automatically between normal, smooth
normalization, and singular normalization regimes.

## Projection, polarization, and low-degree scopes

A normalized model only becomes a carrier after choosing four sections of
its polarization that restrict to the prescribed embedded \(C_0\). They must
produce a basepoint-free finite birational map onto an integral hypersurface,
and the full reduced inverse support must be the intended curve or curves.
Even then, an upstairs divisor needs actual conductor descent. Thus projection
admissibility, inverse-support control, and conductor descent are separate
stages. The [Cartier singleton models](#projection-and-conductor-descent-for-the-three-cartier-singleton-models)
are a restricted necessary classification, not existence results.

The degree exclusions retain their hypotheses. The fixed quartic carrier
exclusion is in characteristic zero and uses its stated integral-carrier
setup; it does not imply an unrestricted exclusion of all equation degrees.
The nonnormal quintic theorem in characteristic zero excludes every mate
degree when the normalization is Gorenstein; normal quintics and
non-Gorenstein normalizations are outside that theorem. A separate globally
ADE quintic theorem excludes sole-supported pairs of degree \((5,8)\) when
the quintic surface has only rational double points; it does not exclude all
quintic-octic pairs. See [degree exclusions](degree_exclusions.md),
[the Gorenstein-normalized quintic proof](../../arguments/carriers/quintic_gorenstein_normalizations.md),
and [the ADE quintic proof](../../arguments/carriers/quintic_octic_ade_cover_and_triple.md).

The quintic toric \(M=0\) source is a concrete non-Gorenstein normalization
model with an explicit projection-center incidence problem. Its remaining
incidence and conductor questions are not resolved by the Gorenstein or ADE
exclusions; see [the toric source account](../../arguments/carriers/quintic_non_gorenstein_toric_sources.md)
and [open carrier cases](open_carrier_cases.md).

Elliptic normalization and projection constructions likewise retain their
own polarization and gluing data. An elliptic double-inverse construction
can supply actual normalized sections, while the projection and conductor
conditions decide whether they yield a carrier mate; it is not a generic
normalization argument. See [elliptic projection and gluing](../../arguments/carriers/projection_and_elliptic_gluing.md).

## Distinct sextic directions

The ADE quintic-octic exclusion and split-sextic investigations are separate
problems. For split sextic carriers, the fixed ramified specimen is excluded,
while a different one-parameter line remains for normalization and conductor
analysis. Neither conclusion follows from the ADE theorem. Keep the explicit
[split-sextic question](open_carrier_cases.md#split-sextic-carriers) and its
remaining cases distinct from quintic carrier classification.

## Connections to other frameworks

This normalization lens interfaces with
[formal normal geometry](../formal-normal-geometry/index.md), which records
infinitesimal and simultaneous-realization constraints along \(C_0\), and
[spectral roots](../spectral-roots/index.md), which organizes genus-one
pushforward and Picard-torsion constructions. Formal compatibility, spectral
sections, and normalized divisor data can each be present without producing
an actual ambient mate: projection, full inverse support, and conductor
descent still have to be checked.

## Bridges

- For a specified carrier, compute the full inverse support, its positive
  divisor-relation lattice, and the conductor-unit map; establish descent of
  an actual section, not only a numerical or reduced-support condition.
- For each proposed normalized source, verify the chosen polarization,
  four-coordinate projection, integral hypersurface image, and full inverse
  support before applying a mate criterion.
- For the three Cartier singleton models, determine whether any admissible
  projection survives both full inverse-support and actual conductor-unit
  descent. The exact open question is preserved below as STCI-Q-0001.
- Keep the toric quintic, elliptic, ADE, and split-sextic interfaces separate
  unless a proved map identifies their normalization and conductor data.

## Projection and conductor descent for the three Cartier singleton models

**Question.** For the fixed \(C_0\), can any of the three necessary normalization/polarization models in [STCI-R-0002](../../results/cartier_singleton_lift.md) occur as an actual integral carrier with **full singleton inverse support** and a set-theoretic mate?

The remaining necessary work includes admissible four-coordinate projections, full inverse-image support, and actual conductor-unit descent. A model's appearance in the classification is **not** an existence result. The question is restricted to the Cartier, singleton, degree-one lift hypotheses; other lifts remain outside this classification.

[STCI-R-0004](../../results/projection_phase_reduction.md) reduces these admissible families to constructible phase images and torsion-coset questions, but does not compute those images or cosets.

See the [independent review](https://github.com/markluxton1/STCI/blob/a69956b9a4d4c0c1a7a5c23ce6442885e6fcef2d/research/notes/2026-10-14-generalization-cartier-lift-independent-audit.md), which checks the necessary classification and leaves actual incidence open. The proposed decision procedures have not been executed on these families.

## Literature

Use the shared accounts of [carrier surfaces and divisor classes](../../literature/README.md#carrier-surfaces-divisor-classes-and-blowups)
and [known exclusions for the smooth rational quartic](../../literature/README.md#the-smooth-rational-quartic-and-its-known-exclusions)
for exact external hypotheses and source boundaries.
