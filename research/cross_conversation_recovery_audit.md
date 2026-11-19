# Cross-conversation mathematical recovery audit

Status: **in progress; provisional inventory, not mathematical authority**. Started 2026-11-17. This file is a temporary audit ledger, **not** a new Result, Argument, or Framework. Preserve mathematical claims rather than conversation chronology. Do not promote a claim solely because an earlier chat described it as verified.

## Method and coverage

Sources: accessible conversation-history retrieval (August–November 2026), recovered November 5 pasted proof transcripts, and keyword/content inspection of the current GitHub `main` tree. Conversation retrieval is selective, **not an exhaustive list of all chats/projects**. GitHub keyword matches show possible coverage, not proof-level identity. The repo's prior internal 344-file audit is not evidence that all historical chats were covered.

Legend: **M** matching repo content (compare exact hypotheses before closing); **P** potential omission; **V** proof verification required; **X** rejected/false/superseded. Counts are *topic clusters*, not claims or conversations. H15 has been integrated as R-0074; other recovered statements retain their scoped proof homes.

| ID | Approx. source date | Recovered claim or construction | Repo comparison / source | Disposition / next gate |
|---|---|---|---|---|
| H01 | Aug 23 | On the unique smooth quadric, (C\sim(1,3)); ((2,4)) CI can specialize to (C+Z), (Z\sim(3,1)), not to (2C) by the proposed conormal quotient | `research/arguments/curve/fixed_quartic_geometry.md`; conormal results; exact degeneration argument not yet checked | M; compare precise exclusion and characteristic |
| H02 | Aug 23 | Generic two-quadric STCI claim was for a different quartic; this (C) has unique quadric | `research/arguments/curve/fixed_quartic_geometry.md` | X; do not recover false construction |
| H03 | Sep 30–Oct 1 | ((4,5)) exclusion, pole/regular-ratio correction, 7 ((4,6)) types and 15 pole strata | `research/results/normal_carriers.md`; `research/arguments/normal-geometry/ideal_filtrations_quartic_exclusion.md`; further exact match pending | M/V; distinguish proven exclusions from abandoned case lists |
| H04 | Oct 6–9 | Normal quartic carrier exceptional lattices, primitive classes, conductor descent; previous overbroad claims and failed saturation/local-cohomology arguments | `research/arguments/carriers/normal_primitive_carriers_and_bounds.md`; `normal_carrier_divisor_geometry.md` | M/V; no automatic promotion of historical exclusions |
| H05 | Oct 6–7 | Entirely-thick necessary inequalities (ab\ge4pq), (7ab+28pq\ge16(aq+bp)); tangent symbols alone insufficient | `research/results/entirely_thick.md`; `research/arguments/normal-geometry/thick_equality_socle.md` | M; check exact hypotheses |
| H06 | Oct 7 | Coordinate-torus compactification: (C^\circ\cong\mathbf G_m), tropical rays \(\pm(1,3,4)\); boundary descent creates residual line | `research/arguments/torus/tropical_thickenings_and_endpoint_duality.md` | M; substantially preserved |
| H07 | Oct 7 | For a **general coordinate tetrahedron**, 16 distinct boundary punctures and four tropical rays of weight 4; proposed six edge-resultant walls / toric blowup interpretation | No direct `tetrahedron` match; coordinate-torus chapter is a *different* compactification | Complete formulas on realized frames; realizability classification and historical parameter-fan recovery not claimed |
| H08 | Oct 7 | Claimed generic affine two quadrics compactify to projective ((2,2)) CI | Explicitly retracted in historical discussion | X; exclude |
| H09 | Oct 9 | Rational normal quartic in (\mathbf P^4): six minimal Hankel quadrics; three equations set-theoretically, not scheme-theoretically | No exact repo comparison yet | Verified P4 set-support proof integrated; distinct from fixed P3 curve |
| H10 | Oct 12 | Quintic normalization divisor identities (5c\sim4H), (5\ell\sim H), (c+\ell\sim H); descent through conductor unresolved | `research/arguments/carriers/quintic_conductor_geometry.md`, `root_descent_and_conductor_defects.md` | M/V; do not promote descent as solved |
| H11 | Oct 19–25 | Characteristic-2 nonlinear transitions, ribbon/triple lifting and residual valuations | `research/arguments/arithmetic/z4_intrinsic_arithmetic_mechanism.md`; `research/arguments/residuals/valuations_and_residual_contact.md` | M; compare specific claims |
| H12 | Oct 31 | Conditional sextic lift, (Q^3) freedom, root-node alternatives; Frobenius binomial components | `research/arguments/arithmetic/positive_characteristic_constructions.md`; sextic jet/spectral arguments | M/V; avoid conflating conditional and established claims |
| H13 | Nov 1 | Hilbert full limits versus proper equation realization and descent | `research/arguments/torus_hilbert_boundary.md`; `research/results/supported_hilbert_full_limits.md` | M; crucial limitation explicitly retained |
| H14 | Nov 5 | Finite embedded torus quotient, endpoint algebras, actual homogeneous equation criterion | `research/arguments/torus_embedded_quotients.md` | M; substantially preserved |
| H15 | Nov 5 | **Chow-polytope rigidity**: (P_Z=mP_C\iff Z=\sum a_i[\lambda_iC]), (\sum a_i=m), over algebraically closed field | Recovered original proof from `Pasted text(20261105-173726).txt` and related pasted records. Search for “Chow polytope”, “oblique edges”, “Minkowski additivity” gave no direct repo matches | M; cycle-level theorem reconstructed and reviewed in [the full-weight proof](arguments/equations/chow_polytope_rigidity.md); no scheme or equation-realization claim |
| H16 | Nov 5 | Chow rigidity identifies a **set**, not scheme structure, with (\operatorname{Sym}^m(T/T_C)); only after full Chow polytope equality, not projected polygon equality | Same recovered transcripts; `research/investigations/supported-generator-incidence/index.md` covers related incidence but not exact theorem | Set-level bijection and exact curve stabilizer verified; scheme-locus claim excluded |
| H17 | Nov 13 | Enriched boundary reconstruction of dense-torus intersections: schemes, filtrations and compatibility defects | User supplied the question reconstruction on Nov 19; [scoped proof owner](arguments/torus/boundary_reconstruction_and_defects.md) | Context recovered, not a verbatim transcript. Degree bounds, finite-order counterexamples and explicit defects proved; general enriched reconstruction remains open |

## Priority proof gate: H15

**Resolved at the cycle level in [R-0074](results/chow_polytope_rigidity.md).** The [full Chow-polytope rigidity argument](arguments/equations/chow_polytope_rigidity.md) proves H15 for effective one-cycles over an algebraically closed field of arbitrary characteristic. It fixes the full column-weight normalization in the coefficients of two hyperplanes. Equality is literal, not up to projection or translation.

The endpoint-support gate is proved by restricting the component Chow forms to hyperplanes in the span of coordinates 0 and 3: nonvanishing is equivalent to avoiding the opposite coordinate line. Orbit endpoints then force support to contain 0 and 3. The separating face is the minimum-column-0 face; its column-2 width is three for a full-support quartic and zero for each of the two plane quartics and the reduced coordinate line. Minkowski additivity and degree exhaustion finish the proof without a projected-edge inference.

The [standard-library determinant replay](arguments/equations/chow_polytope_rigidity.support/verify.py) checks the three integer Sylvester determinants, exact initial coefficients, and unit-coefficient face witnesses. The written support and characteristic arguments received independent reconstruction; the final retained checker was replayed independently. This does not rely on the historical source's assertion of an audit.

R-0074 is the canonical Result. The [H16 follow-up](arguments/equations/chow_polytope_rigidity.md#set-level-symmetric-power-fiber-h16) proves the exact curve stabilizer and symmetric-power bijection on geometric points, not a scheme-locus identification or equation realization.

## Priority recovery gate: H07

For a general choice of four coordinate hyperplanes meeting (C) transversely in disjoint divisors of degree four, (C^\circ=\mathbf P^1\setminus16\) points. Tropical rays corresponding to the four boundary divisors have weights four. Distinguish this from the **special** coordinate torus compactification with only two rays. The [H07 proof](arguments/torus/general_coordinate_boundary.md) now covers all realized contact patterns: normalization order vectors determine primitive rays and gcd multiplicities, including simultaneous collisions and tangencies. A proper ray-only toric model has flat multiplication, smooth exactly for primitive contacts. The simple edge example is retained. A finite constructible root-pattern stratification is proved, not a global polyhedral parameter fan. The formulas cover every realized frame, not a classification of realizable partitions. Exact historical equivalence remains unverified.

## Explicit non-goals

- No wholesale import of chats, redundant historical notes, or abandoned computational certificates.
- No reopening all normal-carrier special cases merely because they occurred in early conversations.
- No promoting false ((2,2)) claims, unproved common-singular-point assertions, or unsupported global descent.
- No inference that absence of a keyword is proof of absence from the repository.

## Next audit pass

1. H16's set-level description and exact curve stabilizer are checked; scheme structure is not inferred.
2. H07 contact/weight/toric-model geometry is checked for all realized frames; require a precise definition/source before claiming a historical global parameter fan.
3. Continue earlier August–October conversation retrieval in large thematic batches, deduplicate by mathematical claim, and close M items after exact content comparison.
4. Only after verification, place genuinely new mathematics into an existing canonical Result/Argument/Framework/Investigation and retire this temporary ledger when its purpose is complete.

**Coverage accounting:** 17 historical topic clusters inventoried; 1 new typed Result added ([R-0074](results/chow_polytope_rigidity.md)); H15 integrated with a reviewed cycle-level proof; H07's undefined historical parameter-fan claim and H17's general enriched reconstruction remain open, alongside several matching-but-unclosed clusters. No exhaustive conversation count is available.

## Integrated follow-up and proof inventory

The [bounded crosswalk](investigations/proof-audit/recovery-crosswalk.md) distinguishes exact owners from unverified historical equivalence. H09 now has a [three-equation set-support proof for the different P4 curve](arguments/curve/rational_normal_quartic_background.md#background-example-the-rational-normal-quartic-in-p4); H17 now has [precise reconstruction bounds and defects](arguments/torus/boundary_reconstruction_and_defects.md); its general enriched reconstruction problem remains open. The [linear-algebra inventory](investigations/proof-audit/README.md) and [file-level appendix](investigations/proof-audit/executable-evidence.md) are evidence maps, not new theorem classifications. R-0024 now has a geometric joint-rank proof while retaining its source-geometry certificate.

This remains a provisional recovery ledger. Checked bounded statements are
not claims of exact equivalence with unread historical transcripts; filename
matches are navigation evidence only. Proof-replacement priorities in the
inventory do not rank research approaches to unrestricted STCI.

## H17 recovered checkpoint

The user-supplied reconstruction removes the missing-context blocker, without
claiming a verbatim historical transcript or an already proved universal theorem.
The [H17 owner](arguments/torus/boundary_reconstruction_and_defects.md) separates
embedded intersections with the whole thickened boundary from separate face
images; gives bounded-degree reconstruction (including the equality bound for
containing C), a C-preserving finite-order counterexample with restricted
ordinary Rees data, a linear containment obstruction and a radical torus-support
defect. Properness and sole support are distinct from compatibility and lifts.
A general enriched-face reconstruction/realization theorem is still open.
