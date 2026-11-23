---
id: STCI-I-0006
type: investigation
title: Chow arrangements, embedded limits, and equation incidence
status: active
scope: "#scope"
question: "#question"
findings: "#findings"
relations:
  - kind: motivates
    from: [STCI-F-0001, STCI-F-0002, STCI-F-0006]
    to: [STCI-I-0006]
    at: "#motivation"
---
# Chow arrangements, embedded limits, and equation incidence

## Scope

Work over an algebraically closed field of characteristic zero with the fixed
smooth rational quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) and its transverse translates
\(C_{u,v}=[s^4:s^3t:u st^3:v t^4]\), \((u,v)\in T=(\mathbf G_m)^2\).
The question concerns actual proper homogeneous two-surface intersections
whose **entire fundamental cycle** is a positive integral sum of these
translates, with degree exhausted. It allows multiple and nonreduced
translated components but no other curve components. It is not the
sole-support problem alone, and it asserts no characteristic-zero STCI result.

## Question

For degrees \((a,b)\) and \(m=ab/4\), can the cycle, Hilbert, and actual
equation-incidence descriptions be connected strongly enough to construct or
obstruct a proper pair realizing a full translated cycle? In particular, can
the embedding and boundary conditions lost by the Chow quotient be recovered
from endpoint data and the same two global equations?

## Motivation

[Full torus boundaries (STCI-F-0001)](../../frameworks/torus-supported-boundaries/index.md),
[embedded torus quotients (STCI-F-0002)](../../frameworks/embedded-torus-quotients/index.md),
and [global equation realization (STCI-F-0006)](../../frameworks/global-equation-realization/index.md)
motivate this investigation: respectively, moving supported equations,
embedded quotient limits, and realization by actual homogeneous equations.
The central interface is whether those objects encode compatible data for
the same proper equation pair.

## Findings

- **UM1 remains a conjecture.** If a proper actual CI \(Z=V(F_a,G_b)\) has
  \[
  [Z]=\sum_i n_i[C_{u_i,v_i}],\qquad n_i>0,\qquad \sum_i n_i=ab/4,
  \]
  then the proposed conclusion is \(\sum_i n_i u_i/v_i=0\). This includes
  repeated translated components with their cycle multiplicities. The
  [proof boundary and recognized special cases](../../arguments/torus/universal_first_moment_proof_boundary.md)
  do not establish the general non-invariant nonreduced case.
- The first moment has equivalent Chow-coordinate, actual-resultant, and
  first-normal-jet expressions **on the full translated-cycle incidence**;
  these identities do not force it to vanish. The [moment and resultant
  arguments](../../arguments/torus/transverse_chow_moment_realization.md),
  [Jacobian and first-jet bridge](../../arguments/torus/spectral_jacobian_first_jet_bridge.md),
  and [full-Chow envelope](../../arguments/torus/full_transverse_chow_pullback_envelope.md)
  own the formulas and their exact scope. The latter's UM1 implication
  remains open and its stated review status should be checked before relying
  on its new claims.
- The three parameter spaces stay distinct: the [normalized Chow quotient](../../arguments/torus/chow_quotient_fan_and_blowup_comparison.md)
  compactifies orbit **cycles**; the [endpoint calculation](../../arguments/torus/arrangement_endpoint_delta.md)
  describes Hilbert data for **reduced unions** and shows their Hilbert
  polynomial varies; and the [relative arrangement argument](../../arguments/torus/relative_arrangement_blowup_family.md)
  studies actual equation spaces and blow-ups. A cycle limit is not by itself
  a flat embedded limit or a realization by two equations.
- For the reduced distinct \((4,4)\) locus, the two endpoint conditions give
  an exact realization criterion. The [marked-arrangement argument](../../arguments/torus/marked_arrangement_forgetful_geometry.md)
  also gives its open forgetful reconstruction and a proposed
  arrangement-first compactification; these do not cover arbitrary
  non-invariant repeated-cycle presentations.
- For arrangement blow-ups, restriction of the original universal scheme
  union need not give the reduced union on a special fiber. On finite
  endpoint-rank strata, the correct union is **re-formed** and is flat with
  the intended fibers. Normal flatness of all its infinitesimal neighborhoods
  remains an additional condition for its Rees blow-up to have the intended
  fibers. Independently, the [smooth separated model](../../arguments/torus/relative_arrangement_blowup_family.md#3-a-smooth-simultaneous-blow-up-model-on-the-resolved-quotient)
  has the desired fiberwise blow-ups and an exact section-space dictionary;
  it is not identified with the singular arrangement blow-up without
  principalization. The one-curve \(V_5\) contraction is known, but a
  complementary contraction for multiple curves across boundary strata is
  not constructed.

## Remaining questions and bounded tests

The following are **proposed tests**, not a priority ranking:

- On a specified endpoint-rank stratum, determine whether normal flatness
  holds for the re-formed union and whether its Rees family agrees with the
  restriction of the original Rees family. Start with the explicit small
  contact cases in the [relative arrangement argument](../../arguments/torus/relative_arrangement_blowup_family.md#7-direct-fiberwise-rees-blow-ups-a-completed-two-curve-model).
- Compare the smooth separated blow-up with the arrangement blow-up by
  testing whether the pulled-back arrangement ideal can be principalized;
  then determine whether any resulting map supports a multiple-curve
  analogue of the \(V_5\) contraction. A section-space identity alone does
  not provide that morphism.
- For the actual-equation incidence, test whether endpoint evaluation and
  properness conditions extend over a chosen collision stratum while
  retaining the same two generators. The reduced \((4,4)\) model is an
  available bounded test; its conclusions must not be promoted to
  non-invariant or nonreduced equation pairs without a separate argument.
- For UM1, the exact remaining gate is to derive vanishing of the
  distinguished first-moment coefficient from the full support of the same
  actual equation pair. The [corpus review](../../arguments/torus/universal_first_moment_corpus_review.md)
  compares the existing approaches and records why moment identities,
  invariant cases, and endpoint budgets alone do not settle it.

## Arrangement-first compactification

The reusable projective all-subsets configuration model, its compatible
forgetful maps, flat family of sources mapping to \(\mathbf P^3\), and the
distinction between that flat source and its possibly nonflat embedded image
are now recorded in the
[marked-arrangement argument](../../arguments/torus/marked_arrangement_forgetful_geometry.md#7-arrangement-first-compactification).
That construction is a proposed compactification of arrangements; it does
not assert a universal flat family of embedded unions or an unrestricted
complete-intersection locus.
