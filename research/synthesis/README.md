# Mathematical synthesis of the STCI project

This is a **guided mathematical exposition**, not a replacement for canonical result records or source proofs. The fixed characteristic-zero test curve is
\[
C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3.
\]
The question whether it is a set-theoretic complete intersection remains **open**.

The historical jet-discrepancy model and its status corrections are summarized in [order-one structure](../results/order_one.md); obsolete quartic-mate cases remain closed by R-0001, while higher-degree jet-dependence questions survive.

Read [the dependency map](DEPENDENCIES.md) to see which arguments connect and which are independent. For precise scope, use [canonical results](../results/INDEX.md), [current state](../STATE.md), [frontier](../FRONTIER.md), and [authority policy](../AUTHORITY.md).

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
