---
id: STCI-F-0005
type: framework
title: Carrier normalization, projection, and conductor descent
status: in_use
scope: "#scope"
bridges: "#bridges"
relations:
  - kind: uses
    from: [STCI-R-0075, STCI-R-0076]
    to: [STCI-F-0005]
    at: "#projection-polarization-and-low-degree-scopes"
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
its pullback has support exactly \(W\); an isolated point away from those
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

**Read the [full carrier-degree × mate-degree coverage
map](degree_exclusions.md) before using isolated low-degree results.**
The complete characteristic-zero theorem excludes every
**integral quartic carrier with every mate degree**;
it does **not** settle higher carrier degrees. The
degree-five and degree-six programs contain
**several entire all-mate exclusion families**,
not just the pairs \((5,8)\) and \((6,6)\).
These results overlap; a special-projection certificate
already covered by a full normalization theorem
is valuable proof geometry, but not additional
disjoint carrier coverage.

**New mixed-degree bridge (pending independent mathematical audit).**
For any actual sole-supported pair of unequal
degrees \(a<b\), if at least one equation
has generic normal order one along \(C_0\),
a general member of the linear system
\(kG_b+F_aH^0(\mathcal O(b-a))\)
is **integral normal**, and together
with \(F_a\) defines the **same CI
ideal**. This is an application of
classical Bertini to the entire
actual-generator system, not to an
arbitrary abstract thickening. Since
every quintic equation has generic
normal order one, **all**
hypothetical \((5,b)\), \(b>5\),
pairs have a *normal degree-\(b\)*
carrier—even if the original
quintic is nonnormal.
For \(b=4n\), the exact index theorem
then forces an order-five primitive
class \(\Delta=nC_0-H\) with
\(R/\gcd(R,n)=5\). **The actual
first-symbol movement improves this
to an exact statement**:
for the *general normal larger
generator* the local moving
\(A_{5n-1}\) points force
\(\boxed{R=5n}\).
Thus \(R=10,15,20,25\)
at larger degrees \(8,12,16,20\),
respectively. The local moving
singularities can produce
these large indices
**automatically**; this is
a realization reduction and
defect-localization tool,
**not** an exclusion.
See the [full lemma and proof](../../arguments/carriers/normal_carrier_divisor_geometry.md#47-unequal-degree-pairs-can-acquire-an-actual-normal-carrier)
and [carrier-degree synthesis](degree_exclusions.md#normal-carrier-replacement-across-unequal-defining-degrees).
Equal-degree pencils and mixed pairs
with both orders at least two retain
their separate analysis.

**Classical primitive starting point.**
[Ellia (2015), Theorems 12 and 15,
Corollary 16](../../literature/README.md#ellia)
already gives stronger uniform
marked \(A_n^k\) normal
surface geometry for a
**primitive** CI and a
finite list of ten primitive
rational-quartic degree pairs.
None has a degree-five
generator or is \((6,6)\).
Consequently every
hypothetical pair of those
degrees has a
**common singular point on
\(C_0\)**; for quintic
pairs the intersection
is generically curvilinear
but nonprimitive at
finitely many points.
This does **not** prove the
unrestricted common-singular
point assertion. The new
mixed Bertini lemma allows
those finitely nonprimitive
points, whereas Ellia's
stronger primitive theorem
requires a smooth containing
surface locally at
**every** point.

For degree five, [Gorenstein-normalized
nonnormal quintics](../../arguments/carriers/quintic_gorenstein_normalizations.md)
and [toric-normalized quintics](../../arguments/carriers/quintic_toric_center_incidence.md)
are excluded in **every mate degree**.
The normal [globally ADE quintic theorem](../../arguments/carriers/quintic_octic_ade_cover_and_triple.md)
excludes the specified \((5,8)\) case,
not every normal quintic mate.
The [all-degree normal-carrier index/Hodge criterion](../../arguments/carriers/normal_carrier_divisor_geometry.md)
gives necessary exact-index spectra for **any**
mate degree on a normal quintic; it is not
a classification of all normal quintics.
Non-Gorenstein, non-toric quintic normalizations
remain among the [open cases](open_carrier_cases.md).

For degree six, the [two-lift norm theorem](../../arguments/linkage/two_lift_sextic_exclusion.md)
and eligible [one-lift conormal theorem](../../arguments/linkage/one_lift_sextic_conormal_exclusion.md)
exclude **all mate degrees in their carrier sectors**;
the [split-cone conductor and thick-sextic constraints](../../arguments/carriers/split_sextic_conductor_and_contact.md)
and [fixed-sextic all-mate valuation theorem](../../results/ci_fixed_sextic_jet_rigidity.md)
cover further sectors. Separately, **every hypothetical
\((6,6)\) pair** admits the [normal general-pencil
reduction](../../arguments/carriers/sextic_pair_reduction.md),
with an index-nine cyclic cover and strong
ADE/higher-contact restrictions. This does
not yield a general normal sextic for a
fixed \((6,b)\) pair with \(b\ne6\).
The [remaining sextic strata](open_carrier_cases.md)
are not retired by the pair-specific theorem.

The elliptic double-inverse construction supplies actual quadratic sections
and a finite birational octic example. A length-twelve zero
scheme tests full support on every smooth basepoint-free fiber of the
five-parameter construction. The characteristic-zero search excludes one
entire parameter line at this support test. For the rest of the family, a
birational fiber with full inverse support and an actual descending power
are still needed to produce a mate. See the
[elliptic carrier case](open_carrier_cases.md#full-inverse-support-in-the-elliptic-construction).

## Boundary valuations as a mate-degree obstruction

The [fixed-sextic rigidity theorem](../../results/ci_fixed_sextic_jet_rigidity.md) provides a different necessary test from divisor-class and conductor descent. On an affine normalization chart, the restriction of a degree-\(b\) mate factors as \(g=Q^nP\), with \(Q\) defining the marked preimage and \(P\) regular. Boundary divisorial valuations constrain the pole budget of \(g\); when no nonzero regular \(P\) can have positive order at every selected boundary, they bound \(n\) linearly in \(b\). A separate generic-local calculation converts that bound into a lower bound for residual degree.

For the **displayed sextic only**, three boundary valuations give \(n\le\lfloor b/2\rfloor\) for every mate degree and hence positive residual degree for every proper mate containing \(C_0\). The [conditional criterion](../../results/ci_fixed_sextic_jet_rigidity.md#conditional-interface-for-other-carriers) is not known for other carriers. Unlike a conductor descent obstruction, it can exclude mates before testing whether a putative upstairs section descends. It does **not** replace the full inverse-support, polarization, or descent tests for a construction. The next generalization question is whether a geometrically defined carrier class admits the required global divisibility, pole budgets, and boundary nonpositivity; see [open cases](open_carrier_cases.md#boundary-valuation-generalization).

## Quadratic-cover exclusions and the remaining one-lift sector

In characteristic zero, use the fixed smooth cover
\(X:z^2=r=2x_1x_2-x_0x_3\). Splitting of an integral carrier in this
cover forces an even degree and a norm expression \(F=P^2-rQ^2\).
The [split-carrier conductor calculation](../../arguments/linkage/split_carrier_norm_and_conductor.md#split-carrier-the-conductor-is-an-actual-complete-intersection)
identifies the conductor scheme with \((P,Q,G)\) **in the one-lift case
\(Q|_{C_0}\ne0\)**; the conjugate-branch intersection is then
\((P,zQ,G)\). The latter includes the extra endpoint attachment and is
not the conductor scheme. In the two-lift case these equations do not
present the finite separated-branch conductor; the general attachment
formula on the branch is \(I_{W\cap W',W}=z\mathfrak c\).

For an integral sextic with \(\deg P=3\), \(\deg Q=2\) and
\(P|_{C_0}=Q|_{C_0}=0\), the signed cubic contains both reduced lifts.
The [two-lift exclusion](../../arguments/linkage/two_lift_sextic_residual_rulings.md#normalizing-the-doubled-marked-ruling)
rules out every mate degree, without normality of the signed surface.
The proof uses its polarized intersection geometry and exhausts the two
residual ruling fibers, including their doubled and nonnormal cases.

If the signed cubic contains just one lift \(D\), the
[conormal budget](../../arguments/linkage/one_lift_sextic_conormal_exclusion.md#one-lift-sextics-the-conormal-zero-budget)
excludes every mate when it is smooth or Du Val along \(D\).
The [unique generically singular signed cubic](../../arguments/linkage/signed_cubic_normalization_and_cartier_defect.md)
has normalization \(\mathbb F_2\), hyperplane class \(E+4f\), and two
full inverse sections of class \(E+2f\); their classes exclude every
mate as well. The surviving one-lift surface is therefore generically
regular along \(D\) and non-Du-Val somewhere on it. The symbolic-layer
proof requires an actual proper sole-support mate and Cohen–Macaulayness,
which the signed hypersurface supplies; it needs no normality along \(D\).
Every such survivor has common-derivative-zero length
\(g\in\{5,6,8\}\), with total intrinsic defect respectively
\(1/3,4/3,10/3\). A nonzero degree-six derivative gives \(g=5\) or
\(6\); if it vanishes identically, generic regularity forces \(g=8\).
Some local least-principal-symbolic-power index is divisible by three.
These are necessary strata, not exclusions of those strata.

These closures concern a fixed auxiliary cover. The
[cover-choice theorem](../../arguments/linkage/quadratic_cover_choice.md)
makes every integral carrier of degree greater than two nonsplit in a
general cover of the specified pencil. This theorem and the unique
singular-cubic normalization exclusion hold in every characteristic
different from two; the Du Val/K3 exclusions above remain characteristic
zero. In the characteristic-zero conductor application, both the moment
and all-minors bounds apply in the chosen cover. At a smooth-transverse
endpoint the capacity is already fixed at \(n(n-1)\) for all allowed
covers, where \(n=ab/4\); even one such endpoint defeats the displayed
scalar postulation comparison. If the smaller carrier is smooth at both
endpoints, the [conormal slopes](../../arguments/linkage/conductor_on_a_smooth_carrier.md#the-two-fixed-endpoints-leave-at-most-one-common-parameter)
isolate at most one candidate for a scalar deficit in degree at least
six and at most two in degree five. Higher jets at those choices, or
the full lattice at a singular endpoint, can still affect the outcome. The
[local/global interface](../global-equation-realization/projection_and_liaison.md#embedded-conductor-and-ambient-equations)
records this remaining gap. No general sextic exclusion or stronger
minimum defining degree follows.

For the distinct [one-point osculating cover](../../arguments/linkage/conductor_on_a_smooth_carrier.md#exact-length-at-the-moving-osculating-point),
the exact scalar comparison fails on every generically regular smaller
carrier, including every integral quintic. Its surviving test concerns
the kernel on actual homogeneous forms; this does not close the
fixed-endpoint candidates, singular lattices or normalization-descent
questions just described.

## Distinct sextic directions

The older sextic investigation concerns a **split first normal cone**:
two distinct first-normal sections, rather than splitting in the auxiliary
quadratic cover. Its fixed ramified specimen is excluded, while a different
one-parameter line remains for normalization and conductor analysis.
No equivalence with quadratic-cover splitting has been proved, so the
new two-lift exclusion does not close this frontier. Keep the explicit
[first-normal-cone question](open_carrier_cases.md#sextic-carriers-with-split-first-normal-cone)
and the ADE quintic-octic problem separate.

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
- Keep the toric quintic, elliptic, ADE, first-normal-cone and quadratic-cover interfaces separate
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


### Quartic-carrier proof interfaces by mechanism

- [Quartic carrier lanes and genus-one algebra](quartic_carrier_six_lanes_and_genus_one.md)
- [Trisecant contradictions and alternative proof routes](quartic_carrier_trisecant_and_proof_routes.md)
- [Veronese projections and genus-zero normalization](quartic_carrier_veronese_and_genus_zero.md)
- [Genus-one ribbon nets and normalization restrictions](quartic_carrier_genus_one_and_ribbon_nets.md)
- [Genus-two bisections and conductor geometry](quartic_carrier_genus_two_conductor.md)
- [Trisecant carrier ideals and discriminant boundary](quartic_carrier_trisecant_discriminant.md)

These are distinct proof mechanisms, not interchangeable exclusions. The [original technical section addresses](quartic_proof_interfaces.md) remain available for older citations; consult the focused developments for their exact hypotheses and full arguments.


### Normalization and conductor topics

- [Fixed carriers, Cartier models, and admissible projections](fixed_carrier_and_cartier_projection.md)
- [Projection pairings and conductor descent failures](projection_pairings_and_conductor_failures.md)
- [Cubic and conic conductor schemes](cubic_and_conic_conductor_schemes.md)
- [Quintic carrier support and A4 conductor contact](quintic_carriers_and_a4_contact.md)
- [Cartier indices, normal socles, and sextic applications](cartier_indices_and_sextic_applications.md)

Projection admissibility, full inverse support, and conductor-unit descent are separate tests. The [original normalization section addresses](normalization_conductor_projection.md) remain navigable.

### Contact tests on actual marked normalizations

The [Cartier-index comparison](../../arguments/carriers/quintic_conormal_and_factor_geometry.md#the-conormal-defect-of-a-marked-cartier-multiple) bounds the degree of the conormal direction plus its rank-drop divisor, without assuming a smooth normalization along the marked curve. The residual gap is to compute those quantities on surviving actual carriers, rather than infer them from the polarization. On the [endpoint V5 correspondence](../../arguments/residuals/blowup_residual_geometry.md#a-conductor-requirement-on-the-endpoint-carriers), a generically regular integral component with smooth inverse normalization needs specified excess from nonsmooth conductor contacts. That requirement does not decide those contacts or cover interior equality slopes with a common conic.
