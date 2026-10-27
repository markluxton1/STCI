# Formal normal geometry and residual intersections: provisional research interface

**Status:** exploratory synthesis, not a theorem or a change to canonical authority. This note supplements [Chapter 2](02-two-surfaces.md), [Chapter 3](03-infinitesimal-geometry.md), and the [dependency map](DEPENDENCIES.md). For precise claims use [canonical results](../results/INDEX.md) and [authority rules](../AUTHORITY.md).

## 1. Setup and objects (see the primary treatments)

For the fixed characteristic-zero rational quartic, begin with a proper intersection containing C, **without** requiring sole reduced support. The cycle identity, the distinction between generic length and the STCI specialization, and the warning against interpreting vertical exceptional curves as residual components are developed in [Chapter 2](02-two-surfaces.md) and [Residual intersections and jets](residual_intersections_and_jets.md).

The normal cone, the full I-initial ideal (including cancellation-generated equations), and the strict-transform intersection on the blowup are **three different constructions**. Their precise definitions and the limitations on comparing them are in [Chapter 2](02-two-surfaces.md), [Chapter 3](03-infinitesimal-geometry.md), and [Normal-filtration defects](normal_filtration_boundary_obstructions.md). No identification between these objects is assumed here.

This note's distinct purpose is to develop the **valuation and specialization research interface**, which is still provisional.

## 2. Generic formal algebra and specialization

At \(\eta=\eta_{C_0}\), the completed transverse regular local ring is (noncanonically) \(K[[u,v]]\), \(K=k(C_0)\simeq k(t)\). The ideal \(J_\eta\) is \((f,g)\), and, since the surfaces have no common component, its colength is \(m\). If \(r=\operatorname{ord}_\eta(f)\), \(s=\operatorname{ord}_\eta(g)\), then \(m\ge rs\), with equality precisely when their initial binary forms are coprime over \(\overline K\); see [Chapter 2](02-two-surfaces.md). Common first factors encode generic normal directions, not global factors of \(F,G\).

Working over \(\overline K\) separates geometric generic directions. Choosing a point \(p\in C_0\) and completing \(K\) at its discrete valuation gives \(k((t_p))\) after choosing a local parameter (with residue field \(k\)); this is **not** the algebraic closure of \(K\). In characteristic zero, Puiseux extensions describe an algebraic closure of \(k((t_p))\). These valued extensions can organize branching and specialization of generic directions, but a valuation at \(p\) does not by itself prove the existence of a residual global curve.

The global sheaf of normal jets, its saturation defects, and the behavior over special points retain information absent from \(K[[u,v]]\). The full root scheme of a saturated first relation, including repeated and nonreduced fibers, is essential; see [Chapter 3](03-infinitesimal-geometry.md).

## 3. Exceptional directions, cancellation, and valuations

The common zero scheme of the two leading normal forms on \(E\) can have components dominating \(C_0\) (not necessarily sections), special-fiber components, and embedded or nonreduced features. Successive blowups can separate some persistent contacts, but no general finite-step classification or implication \(\text{vertical exceptional component}\Rightarrow R\ne0\) is asserted.

The appropriate structural question is how the **full filtered ideal**, rather than a chosen pair of initial forms, controls the transforms and their exceptional intersection. Cancellation is a geometric source of higher initial relations; it should be understood through initial ideals, Rees constructions, and valuations, **not** treated as an invitation to enumerate polynomial examples. Weighted initial ideals and tropical/Gröbner methods may help organize valuations and changes of normal direction. Tropicalizations of the individual generators need not determine the initial ideal or tropicalization of \(J\); generator-independent statements require the whole ideal. Seek intrinsic invariants and global constraints first; use examples only to distinguish precise competing assertions.

The valuation tree of persistent horizontal directions and their specializations is a **possible organizing picture**, not an established classification or a canonical tree. It requires a precise choice of valuations and a proof that any proposed invariant is independent of coordinates, generators, and blowup sequence.

## 4. Where this fits among established results

For the scoped root, graded-relation and actual-CI bridge theorems R-0005–R-0009, use [Chapter 3](03-infinitesimal-geometry.md). For local initial-ideal comparison and saturation, use [Normal-filtration defects](normal_filtration_boundary_obstructions.md). For proper residual cycles, examples and global jet obstructions, use [Residual intersections and jets](residual_intersections_and_jets.md). For fixed-carrier normalization and conductor descent, use [Chapter 4](04-carriers.md) and [Carrier/socle interfaces](carrier_conductor_socle_interfaces.md). The quartic-carrier exclusion [R-0001](../results/quartic_carrier_exclusion.md) remains closed.

**None of these references proves the valuation-theoretic classification proposed below.** In particular, moving from generic formal data to an actual supported pair requires hypotheses not provided by the valuation picture.

## 5. Focused theorem-level questions (all open)

1. **Generic-to-global interface.** What hypotheses on the full initial ideal and its saturation make a horizontal common-direction scheme extend to a controlled global root relation, including special-point defects? Can those defects be related to global normal-jet restrictions?
2. **Residual detection.** Can a generator-independent invariant of successive transforms or the normal filtration distinguish a pure \(C_0\)-supported intersection from one with \(R\ne0\)? Prove a direction of implication before attempting numerical bounds; exceptional vertical curves alone do not suffice.
3. **Valuation-theoretic structure.** Is there a finite intrinsic invariant of persistent generic normal directions, their specialization, and higher cancellation that constrains \(m\), \(R\), or the realizability of \(J\) by global homogeneous equations?
4. **Connection to established obstructions.** Can one verify the precise extra hypotheses that transfer the graded/root-scheme criteria or carrier-conductor restrictions to an actual pair in a nontrivial family of degrees \(d,e\ge5\)?

A productive next round should choose one or two of these interfaces **only after** assessing leverage against the current [frontier](../FRONTIER.md). Generalize beyond \(C_0\) only when doing so is cheap or clarifies a proof. Prefer a structural lemma, counterexample to a proposed implication, or a sharply isolated missing implication over computational casework. This note imposes no mandatory method or priority order.
