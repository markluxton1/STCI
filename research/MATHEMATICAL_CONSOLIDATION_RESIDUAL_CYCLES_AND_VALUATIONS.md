# Mathematical consolidation: residual cycles, exceptional contact, and valuations

**Thematic assessment; no new theorem promotion or fresh computation.** Sources: R-0019, R-0023–R-0025, the CI-cycle and adaptive-valuative notebooks, and the weighted-initial-ideal continuation.

## Three distinct geometric objects

1. **Residual fundamental cycle downstairs.** For a proper pair of surfaces of degrees d,e containing C, write [V(F,G)]=m[C]+R, where m is the length of the generic transverse two-dimensional regular-local parameter algebra. Bezout gives de=4m+deg R. R≠0 is an actual extra one-dimensional component, not a higher local contact at a point.
2. **Residual zero-cycle on an auxiliary surface.** R-0019 assumes a finite-flat curvilinear thickening with a saturated order flag and a smooth auxiliary Q meeting properly. It proves [rho cap sigma]=(m-1)T+D_(m-1) and A<=D_(m-1). These are *zero-cycle/divisor* statements, not ideal identities and not by themselves a residual one-dimensional component of V(F,G).
3. **Exceptional/infinitely near geometry.** Blowup boundary divisors, vertical exceptional cycles and weighted initial ideals encode transverse contact and degeneration. They may guide an obstruction, but a vertical exceptional cycle is not automatically the image of a residual curve downstairs. A pushdown or a generic-multiplicity argument is required.

## Concrete mathematical benchmarks

- **R-0023:** one explicit quartic pair has C plus a smooth degree-12 genus-16 residual meeting C transversely at 18 points. A special pair has C plus a line and smooth degree-11 genus-12 residual, with five line–residual nodes, seventeen C–residual and one C–line attachments. These are actual scheme unions verified in the cited audits, not just blowup pictures.
- **R-0024:** at that particular pencil the fixed-boundary Grassmannian fibre is smooth of dimension 14 and has five independent formal/etale-local residual-node smoothing coordinates. This is not an explicit global polynomial arc or a universal deformation result.
- **R-0025:** for one selected sextic Fstar and proper degree-16 mates, the exact order-12 jet-kernel calculation forces generic multiplicity <=22, hence residual degree >=8. This is a genuine downstairs residual conclusion, but only for that fixed sextic and mate degree; the independent normal-division check ran in CI, while Macaulay2 was not rerun there.

## A valuable correction to the valuation heuristic

The adaptive-valuative notebook observes that for an **actual two-generator parameter ideal** J in the regular two-dimensional local ring at eta_C, colength equals Hilbert–Samuel multiplicity and is invariant under integral closure. Thus full Rees-valuation data can determine m, even though arbitrary ideals of the same integral closure may have different colength. Do not use the arbitrary-ideal counterexample to dismiss valuations for actual complete intersections.

Conversely a fixed monomial-weight fan is inadequate: J_N=(x-y^2,y^N) has colength N, but every monomial weight in the original coordinates assigns the same ideal value independent of N. Adapted coordinates/infinitely near valuations reveal the difference. A partial set of valuation inequalities generally yields a **lower**, not upper, bound for m; proving R≠0 by the degree budget requires m<de/4.

The weighted-initials note further insists on full initial ideals, not just the initials of F and G. It keeps monomial-containing initial ideals, since nilpotent thickenings make the normal-torus tropical locus uninformative. Coefficient valuations depend on a rational normal frame; arbitrary K[[X,Y]] series need not support the naive Gauss minimum without tail bounds.

## Organizing decision

Create a **Residual cycles and valuative contact** chapter, distinct from (but cross-linked to) the normal-filtration chapter. Organize by the geometric level of the conclusion:
- cycle of actual intersection and generic transverse multiplicity;
- auxiliary residual zero-cycles and defect divisors;
- exceptional boundary/weighted-initial/infinitely near data;
- promotion bridges from contact data to a downstairs residual conclusion;
- exact examples and failed shortcuts.

The central open bridge is to extract a global upper bound on m or construct an actual residual branch from intrinsic local/exceptional data. R-0025 is a restricted successful model of the former, not a general solution.

## Next content review

Review characteristic-dependent constructions and arithmetic lifting (R-0012, R-0020, R-0021, R-0029, R-0031), asking which effects are Frobenius/coalescence, which are bundle-splitting, and which are genuine integral nonlifting statements. Preserve the distinctions rather than one slogan about characteristic two.


## Theme 6: global quartic incidence and deformation

**Parameter space.** For the fixed C, V=H^0(I_C(4)) has dimension 18. Proper quartic pencils form an open U in Gr(2,V), dimension 32. The universal complete intersection is flat with Hilbert polynomial 16n-32 and arithmetic genus 33. This is a *family of complete intersections containing C*, not a family of STCI presentations.

**Attachment map.** The determinant of the two first normal sections is in det(N_C^*(4))=O_C(18). Where nonzero, it gives a rational attachment-divisor map beta:U-->P H^0(O_C(18)). At the distinguished four-component pencil beta=9p0+9pInfinity. The deformation-laboratory note and independent audit calculate a surjective differential of rank 18 there, leaving a 14-dimensional local fixed-boundary fiber. This is a local statement, not surjectivity of the global map.

**Residual genus and motion.** For a general proper quartic pencil containing C, the independently reviewed but unpromoted blowup/Bertini argument gives a smooth degree-12 genus-16 residual with 18 transverse attachments. R-0023 provides one *exact* rational benchmark. The explicit one-equation perturbation G_lambda=G+lambda*x0^2*Q splits eight units of endpoint attachment from 9p0+9pInfinity to p0+9pInfinity plus eight moving points; it does not certify global residual smoothness. A different root pencil preserves the concentrated boundary while varying the four-sheet configuration. Thus constant arithmetic genus, constant attachment divisor, and constant normalization are different constraints.

**Fixed-boundary smoothing.** R-0024 gives exact ordered-source ranks 19 (affine boundary), 5 (node classes), and 24 (joint), yielding projective boundary rank 18 and five independent node-smoothing directions in the 14-dimensional fixed-boundary fiber. After labeling nodes, its completed local ring has five smoothing and nine other parameters. No explicit global polynomial arc is asserted. In particular, a first-order fixed-boundary perturbation need not preserve the boundary at higher orders.

**Three kinds of universality must not be conflated.** (i) The Grassmannian family includes all proper quartic pencils containing the fixed C. (ii) The determinant boundary map is defined only where the first-normal determinant is nonzero, and the rank/smoothing results are at particular points. (iii) Osculating and bitangent plane families are separate incidence constructions with their own finiteness and transversality hypotheses. Their degree formula and scheme structure should be checked in their source before inclusion as established global theorems.

**Interesting geometry to retain:** migration of genus between normalization and singular gluing, endpoint collision of attachment points, fixed-boundary smoothing of residual nodes, the root-pencil four-sheet configuration, and the topology/conductor viewpoint. These deserve a home even when they yield no STCI exclusion.

**Audit still required:** locate and review the exact W_osc/W_bit universal plane-family source and its independent audit, including the rank-de and pushforward degree formulas. They are not verified by the documents inspected in this pass. Do not silently promote them based on summary mentions.

**Sources:** research/notes/2026-10-25-ci-cycle-deformation-laboratory.md; research/notes/2026-10-25-ci-cycle-exploration-audit.md; research/notes/2026-10-25-ci-cycle-geometry-notebook.md; research/notes/2026-10-25-ci-cycle-fixed-boundary-node-smoothing.md; canonical R-0023 and R-0024.
