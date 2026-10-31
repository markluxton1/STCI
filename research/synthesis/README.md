# Mathematical synthesis of the STCI project

This is a **guided mathematical exposition**, not a replacement for canonical result records or source proofs. The fixed characteristic-zero test curve is
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3.
\]
The question whether it is a set-theoretic complete intersection remains **open**.

The historical jet-discrepancy model and its status corrections are summarized in [order-one structure](../results/order_one.md); obsolete quartic-mate cases remain closed by R-0001, while higher-degree jet-dependence questions survive.

The three main forward research routes are the **embedded lower-thickening/determinant route**, the **uniform residual-jet route**, and the **fixed-carrier conductor-descent route**. These are programs with missing implications, not established reductions of the unrestricted STCI problem. See [current frontier](../FRONTIER.md).

Read [the dependency map](DEPENDENCIES.md) to see which arguments connect and which are independent. For precise scope, use [canonical results](../results/INDEX.md), [current state](../STATE.md), [frontier](../FRONTIER.md), and [authority policy](../AUTHORITY.md).

**Varying-lift qualification.** A compatible quadratic symbol determines a sextic only modulo \(\eta q^3\). Since \(q^3\) has normal order three, the correct existence test for some sextic lift is \(h+\eta(q^3)_3=f(\ell u+mv)\). The correction map alone has rank sixteen; the augmented map including \(\eta\) has rank sixteen or seventeen depending on whether \((q^3)_3\) lies in its image. Consequently a fixed-lift cubic failure does not, without checking this extra direction, exclude every lift of the same symbol. The reported \(-384\) pairing must be checked against \((q^3)_3\) before it is used as a varying-lift obstruction. See [the precise correction](normalization_conductor_phase2_addendum.md#varying-the-sextic-lift-the-missing-q3-direction).


## Document status

The six numbered chapters and the named mathematical supplements below form the permanent exposition. Files named `phase2_*` and `normalization_conductor_phase2_*` record dated source intake, reconciliation, integration checkpoints, and source dispositions. They are **historical working records**, not additional chapters, current task lists, or competing theorem authority. Retain them where they identify a specific mathematical gap, source disposition, or independently useful failure; consult the permanent exposition and canonical results for current status.


## Integrated mathematical topics (October 30 consolidation)

The chapters now provide explicit entry points into the migrated source packages:

| Mathematical question | Start with | Detailed retained derivations |
| --- | --- | --- |
| Marked conormal versus quadric and secant-plane flags; dual discriminant intersection | [Chapter 1](01-problem-and-curve.md), §§1.2–1.3 | [Dual flags](../supplements/QUARTIC_DUAL_FLAGS_AND_BITANGENTS.md), [projection geometry](../supplements/QUARTIC_PROJECTION_AND_SPECIAL_GEOMETRY.md) |
| Proper residual cycles, coefficient valuations and full initial ideals | [Chapter 2](02-two-surfaces.md), §2.10 | [CI-cycle valuations](../supplements/CI_CYCLE_VALUATIONS_AND_CONTACT.md), [intrinsic valuations](../supplements/INTRINSIC_VALUATIONS_AND_CONTACT_GEOMETRY.md) |
| Principal-parts boundary repair and embedded equation modules | [Chapter 3](03-infinitesimal-geometry.md), §3.12 | [Weighted initials and repair](../supplements/NORMAL_BOUNDARY_WEIGHTED_INITIALS_AND_LIFTING.md), [one-step criterion](../supplements/BOUNDARY_ONE_STEP_AND_ENDPOINT_SCOPE.md), [Delta embedding](../supplements/DELTA_EMBEDDING_NORMAL_AND_REES_GEOMETRY.md) |
| Scroll/cone normalizations, conductor and four-section specialization | [Chapter 4](04-carriers.md), §4.9 | [Ruled surfaces](../supplements/CUBIC_SCROLL_AND_RULED_SURFACES.md) |
| Multiplicity-three residual quartics and the (4,4) exclusion boundary | [Chapter 5](05-exclusions.md), §5.8 | [(4,4) multiplicity and genus](../supplements/INTRINSIC_44_MULTIPLICITY_AND_GENUS_BUDGETS.md) |
| Open bridges to actual global equations | [Chapter 6](06-frontier.md), §6.14 | Corresponding source packages above; canonical status in [results](../results/INDEX.md) |

These are subject-level reading routes, not certifications of every preserved historical argument. The source supplements retain detailed proofs and limitations and preserve detailed arguments whose specialization would be lost in a chapter summary. Do not infer an established theorem from inclusion in a synthesis chapter.

## Chapters

1. [Problem and fixed geometry](01-problem-and-curve.md)
2. [Two surfaces and their intersection](02-two-surfaces.md)
3. [Jets, roots, and multiple structures](03-infinitesimal-geometry.md)
4. [Carriers, normalization, and conductor](04-carriers.md)
5. [Exclusion arguments](05-exclusions.md)
6. [Surviving questions](06-frontier.md)

## Focused supplements — choose by the question, not by date

The six chapters are the main reading route. The four supplements below have **different jobs**, so none needs to be read merely to understand the others:

| If you need to understand… | Read | Distinct contribution |
| --- | --- | --- |
| An actual carrier, its local Cartier index, conductor or top socle | [Carrier descent and socle](carrier_conductor_socle_interfaces.md), after [Chapter 4](04-carriers.md) | Scoped R-0017 and R-0034–R-0036 results beyond the basic fixed-carrier framework |
| Saturation, full initial ideals, punctual comparison defects or one-step lifting | [Normal filtrations and boundary obstructions](normal_filtration_boundary_obstructions.md), after [Chapter 3](03-infinitesimal-geometry.md) | R-0010/R-0016/R-0030/R-0032/R-0033 and carefully labeled provisional lifting tests |
| Actual residual curves, fixed-boundary deformations or global jet bounds | [Residual intersections and jets](residual_intersections_and_jets.md), after [Chapter 2](02-two-surfaces.md) | Scoped R-0019 and R-0021–R-0025, distinguishing examples from universal claims |
| Valuation and specialization **research questions**, rather than accepted theorems | [Formal normal geometry](formal-normal-intersection.md) | Provisional generic-to-global and Rees/valuation framework; not a separate theorem authority |

## Reading the conductor phase calculations

For the carrier route, start with [Chapter 4](04-carriers.md) for the exact fixed-carrier criterion, then [carrier/conductor/socle interfaces](carrier_conductor_socle_interfaces.md) for the restricted pointwise identity. The long [projection synthesis](normalization_conductor_projection.md) retains distinct exact calculations: full quadratic conductor power descent, finite-Artinian nilpotent and etale phases, torsion-coset families, and the conditional single-field power bound. They are not interchangeable hypotheses or an executed exclusion of the three remaining Cartier singleton models.

## Ambient source completeness versus normal-jet realization

The [formal-normal ideal-power theorem](formal-normal-intersection.md#12-what-the-exact-ideal-power-theorem-contributes) supplies all homogeneous sections of \(I_C^m(d)\) in the stable range \(d\ge3m\). [Chapter 2](02-two-surfaces.md#27a-ambient-ideal-powers-and-normal-symbols) and [Chapter 3](03-infinitesimal-geometry.md) distinguish that source description from the image of normal-symbol and finite-jet maps. The distinction is necessary for both the global determinant and uniform residual-degree programs; it is not an additional STCI exclusion.

## The conditional (6,16) calculation

The [detailed source calculation](normalization_conductor_phase2_addendum.md#coefficient-level-cubic-obstruction-without-elimination) computes eleven actual sextic leading-symbol equations and gives a division-free four-equation test for the unique possible cubic correction. The correction map has constant rank sixteen and a twenty-four-dimensional quotient obstruction. A specified smooth seed passes the leading-symbol equations but fails the cubic comparison by an exact nonzero pairing. The [frontier](06-frontier.md#611c-the-finite-616-incidence-after-the-cubic-simplification) describes the remaining joint incidence with second obstructions and full-root torsion. Neither the failed seed nor the source calculation excludes the entire family.

## Numerical screening before a source computation

For a proper pair with sole support the degree-four curve, \(4\mid de\), equivalently \(4/\gcd(4,d)\mid e\). This is only a necessary degree filter; if a residual curve exists, \(de=4m+\deg R\). See [the exclusion chapter](05-exclusions.md#54-a-useful-degree-five-consequence) and [Chapter 2](02-two-surfaces.md#23a-the-exact-divisibility-condition-when-residual-degree-vanishes).

## How the integrated arguments fit together

The six chapters now cover the six major investigation families without treating them as one proof. The following table identifies the *missing implication* at each interface, so a new calculation can be placed by mathematical purpose rather than by date.

| Starting information | Established or reviewed tool | Missing implication |
| --- | --- | --- |
| Two actual hypersurfaces and their generic transverse algebra | Projective residual-cycle degree, scoped residual examples and jet bounds (Chapter 2) | Uniform control of residual support for all relevant global pairs |
| An embedded lower thickening with saturated layers | Conditional root and socle results; reviewed one-step extension-class test (Chapter 3) | Classification of admissible lower embeddings and their actual global equation images |
| A normal valuation or weighted initial calculation | Full initial ideals, integral lattices and ideal-power source theorem (formal-normal supplement) | Coordinate-independent obstruction that forces a residual projective curve |
| A characteristic-two supported presentation | Explicit mu4 degeneration, filtered fourth equation and prescribed arithmetic nonlifting (Chapter 3) | A specialization principle applicable beyond the prescribed embedded model |
| A normalized integral carrier and inverse curve | Full-conductor descent and restricted Cartier/phase criteria (Chapter 4) | Computation of descent for the relevant higher-degree carriers |
| Marked contact, flag, dual and ruled geometry | R-0026–R-0029 models and endpoint corrections (Chapters 1 and 4) | A proved compatibility map to actual equation modules or conductor descent |

The **actual global equation source** is the recurring checkpoint. Formal solutions, local jets, abstract filtrations, divisor classes and numerical constraints do not become a set-theoretic complete intersection without actual proper homogeneous equations. Conversely, a failure for one fixed source family does not exclude all higher-degree pairs.

For navigation, read [the dependency map](DEPENDENCIES.md) for logical arrows, [Chapter 6](06-frontier.md) for candidate deliverables, and the [canonical frontier](../FRONTIER.md) for current research priorities. The synthesis chapters are not a new authority layer.

**Why four files remain:** the carrier and filtration supplements are scoped-result guides, the residual supplement connects examples and jet bounds, and the formal-normal supplement is an explicitly speculative method proposal. Combining them now would obscure those status differences and create a long mixed-authority document. Their overlapping setup should instead be delegated to Chapters 2–4.

**Evidence convention.** **Established** means supported by a promoted result or specifically identified audited source; **conditional** means its hypotheses must be checked before application; **provisional** means the discussion is an organizing interpretation or a research question. The synthesis does not promote new theorems.
