# Phase 2 Step 1C — comparison batch 2

Sources read: `2026-10-08-session-nonimmersion-prime-independent-audit.md`, `2026-10-07-session-nonnormal-mf6-independent-audit.md`, and `2026-10-07-session-nonnormal-structural-progress.md` under `research/notes/`.

Destinations checked: `research/synthesis/normalization_conductor_projection.md`, `research/synthesis/04-carriers.md`, `research/chapters/CARRIER_AND_CONDUCTOR_GEOMETRY.md`, `research/chapters/QUARTIC_CARRIER_TECHNICAL_PROOFS.md`, and `research/synthesis/normal_filtration_boundary_obstructions.md`.

| Source claim | Finding in checked destinations | Owner |
|---|---|---|
| Generic nonimmersion-prime lemma: finite birational smooth normalization, c linearly equivalent to H, pullback mate a power, immersion on c, mate degree nonzero in k; positive-H-intersection primes generically immersive | Missing detailed lemma and proof in checked destinations | Carrier and conductor geometry |
| Four explicit nonnormal MF6 quartic boundary carriers have no mate in any degree in characteristic zero, by affine finite normalization and quadratic norm obstruction | Missing detailed fiber-norm argument in checked destinations | Carrier and conductor geometry; MF6 cross-reference |
| Ordinary pinch transversality, scroll branch-point count, Roman conic obstruction, and nodal conductor arbitrary-contact countermodel | Partial: broad genus-zero and inverse-support discussion exists, but precise mechanisms not found | Carrier and conductor geometry |

The nonimmersion proof uses a unit pivot and vanishing 2x2 derivative minors on a possibly singular prime, then cancels a nonzero power in the prime's local domain *before* evaluating at a point on c. It fails when characteristic divides mate degree; isolated rank drops are not covered.

The MF6 boundary argument has four explicitly specified carriers, not a general nonnormal exclusion. A mate would force equality of a power on two normalization points with identical downstairs image; the resulting root-of-unity condition contradicts the quadratic norm 1/3. The general pencil remains outside scope.

The nodal conductor local model permits arbitrarily high conductor contact despite a smooth embedded image curve, refuting a reduced-branch-count argument.

**Status:** provisional destination gaps, not global absence certificates. Other permanent owners still need checking. Historical sources unchanged; no mathematical correctness promotion.
