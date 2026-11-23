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

### Current first-moment probe

The current investigation focuses on UM1 itself: why should the spectral
polynomial \(H_\sigma(T,1)=\prod_i(T-u_i/v_i)^{n_i}\) be depressed in
the distinguished quadric-pencil coordinate for every actual complete
intersection with full translated support? The target includes arbitrary
non-invariant repeated structures. An arbitrary translation of the spectral
coordinate, containment of a translate, or a bounded determinant truncation
does not establish this assertion.

The November 23 parallel investigation extended vanishing through residual
liaison and actual sign symmetry, and identified a sharper section-defect
boundary. Its reviewed findings below replace the initial probes.
The next bounded question is how degeneration of the same two equations
constrains that defect; no general CI-compatible modulus relation or
unrestricted vanishing theorem has been established. Full spectral
classification is not a prerequisite to this first-coefficient question.

## Motivation

[Full torus boundaries (STCI-F-0001)](../../frameworks/torus-supported-boundaries/index.md),
[embedded torus quotients (STCI-F-0002)](../../frameworks/embedded-torus-quotients/index.md),
and [global equation realization (STCI-F-0006)](../../frameworks/global-equation-realization/index.md)
motivate this investigation: respectively, moving supported equations,
embedded quotient limits, and realization by actual homogeneous equations.
The central interface is whether those objects encode compatible data for
the same proper equation pair.

## Findings

- [Residual liaison](../../results/chow_moment_residual_speciality.md)
  proves vanishing when the reduced support's smallest equation space is
  exhausted by the actual CI sources. Conormal and conductor bounds cover
  one double with simple companions in all degrees and one triple with
  simple companions in all degrees in characteristic zero. The precise
  cohomology dimension is \(\dim(I_Y)_a-\dim J_a\), so it measures
  reduced-support postulation, not independent hidden nilpotent freedom.
  The [quartic–quintic analysis](../../arguments/torus/chow_quintic_mate_partitions.md)
  leaves only \((4,1)\) and \((3,2)\) unexcluded in characteristic zero.
- [Actual sign symmetry and ACMness](../../results/chow_acm_parity_vanishing.md)
  force \(M_1=0\), without a CI presentation or fixed Hilbert numerator,
  in characteristic different from two. Thus both invariant pure hulls
  of a hypothetical characteristic-zero sole-supported CI must be non-ACM.
  Nonzero moment requires a [nonstandard-sign generator in the head of
  the finite section defect](../../arguments/torus/chow_section_parity_defect.md).
  The single reduced quartic exhibits this defect; its acquisition by
  actual CI limits is the remaining source-sensitive question.
- The [Hilbert-scheme form](../../arguments/torus/chow_hilbert_symplectic_form.md)
  gives \(f^*\omega=2M_1\,dx_0\wedge dx_3\), including repeated
  components. An exact twisted-cubic-plus-line control shows that endpoint
  collapse and a Gorenstein central fiber alone do not force isotropy.
  The [boundary-modulus interpretation](../../arguments/torus/spectral_boundary_modulus.md)
  makes depression equivalent to triviality in
  \(J(\mathbf P^1,2\infty)\simeq\mathbf G_a\). The additive target
  is constructed; compatibility with actual CI/Cartier relations is not.

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
  remains open; its proof owner records the precise scoped reconstruction
  and inherited inputs.
- The [saturation and interpolation theorem](../../arguments/torus/spectral_interpolation_and_polar_saturation.md)
  identifies opposite-chain membership for coordinate-saturated ideals. A full
  translated-support CI is automatically saturated this way; the second chain
  gives no independent cofactor gate. On the distinct-spectral-value stratum,
  \((H,K)\) recovers paired torus points with their multiplicities, including
  nonreduced cycles. Spectral collisions need higher polars. Recovering those
  cycle parameters does not replace full-chain membership and the norm test
  on the actual two-generator ideal.
- The [fixed-depth source controls](../../results/fixed_depth_determinant_incidence.md)
  give scheme-level affine-product incidence and actual residual pairs
  cancelling every bounded fixed containing-surface test. They can be
  reduced CIs of normal integral carriers, with generic multiplicity one on
  \(C\); their residual components need not be translates. Thus they do not
  settle the full translated-cycle question here. The characteristic-zero
  [two-product Jacobian criterion](../../results/jacobian_radical_support.md)
  is a compact alternative exact support incidence, using both full
  equations through a source-dependent growing-degree Jacobian.
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
  the intended fibers. The [Hilbert-stratum refinement](../../results/arrangement_strata_and_orders.md)
  shows that constant Hilbert polynomial already forces those ranks locally
  constant on a reduced stratum; reduced CI arrangements with at least five
  components must be nonplanar at an endpoint. Normal flatness of all its infinitesimal neighborhoods
  remains an additional condition for its Rees blow-up to have the intended
  fibers. Independently, the [smooth separated model](../../arguments/torus/relative_arrangement_blowup_family.md#3-a-smooth-simultaneous-blow-up-model-on-the-resolved-quotient)
  has the desired fiberwise blow-ups and an exact section-space dictionary,
  now including arbitrary individual vanishing orders; it is not identified with the singular arrangement blow-up without
  principalization. The one-curve \(V_5\) contraction is known, but a
  complementary contraction for multiple curves across boundary strata is
  not constructed.

## Remaining questions and bounded tests

The following are **proposed tests**, not a priority ranking:

- Retain the Rees degeneration of an actual two-generator ideal and the
  induced map to its invariant pure hull's finite section defect. Determine
  which equal-degree opposite-sign generator pairs and matrix coefficients
  can be reached. Start with the known opposite-limit controls before
  probing a declared new degree/source sector. The goal is a new restriction
  on actual CI origin, not another proof that arbitrary pure curves can
  carry the defect. Compare this with constructing a modulus-compatible
  norm relation on a named carrier; the strategic queue owns priority.

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
