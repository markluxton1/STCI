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
