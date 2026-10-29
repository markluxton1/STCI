# Veronese projection classification: Step 1C preservation

The primary mathematical owner remains `research/notes/2026-10-07-session-veronese-pencil-classification.md`, with its October 8 independent audit. This integration records the exact distinctions needed in the permanent exposition.

For a finite birational projection of the quadratic Veronese plane to an integral quartic surface, the projection center is a rank-one-free pencil of symmetric three-by-three matrices. If a member is invertible, self-adjoint Jordan decomposition gives exactly the Roman, length-two Jordan, and length-three Jordan types. If every member is singular, the primitive kernel of the adjugate has degree one. The resulting projection has quadric image and generic degree two, so does not normalize an integral quartic. The singular-pencil proof is `research/notes/2026-10-07-session-veronese-singular-pencil.md`.

In characteristic zero, a mate of any positive degree for a smooth rational quartic on one of the three birational carriers would pull back to a scalar multiple of a power of the unique smooth lifted conic equation. Full inverse support forces every point of the conic to have a singleton normalization fiber. Roman type: the six permitted points on the three coordinate axes lie on no conic. Length-two Jordan type: the conductor line has only one permitted singleton point, where immersion forces transverse intersection, contradicting the conic intersection number. Length-three Jordan type: the two permitted points force a conic whose powers fail the first conductor-jet descent condition. The last obstruction is not merely a reduced-fiber count.

This excludes all positive-degree mates for this normalization class, not for every nonnormal quartic. This is source preservation, not a fresh proof audit.

## Explicit length-three conductor-jet calculation

For the length-three map [x²:xy:z²:y²-xz], the singleton fibers over the conductor line x=0 force the lifted conic through [0:0:1] and [0:1:0], transversely. Write its equation f=alpha*x²+beta*x*y+gamma*x*z+delta*y*z, delta nonzero. In the z=1 chart, the downstairs coordinate ring is A=k[x²,xy,y²-x] inside B=k[x,y]. Work over k(y) modulo x². The involution x maps to -x, y maps to -y+x/y; direct substitution fixes the three generators of A modulo x². Therefore every element descending to A must be invariant under this involution.

Modulo x², f=delta*y+x*(beta*y+gamma), whereas its involution image is -delta*y+x*(delta/y+beta*y-gamma). If f to the bth power descends, equality of constant terms forces b even. For positive even b, equality of linear x coefficients forces b*(delta*y)^(b-1)*(2*beta*y+delta/y)=0. In characteristic zero this gives 2*beta*y²+delta=0 as a rational function, impossible with delta nonzero. Thus no positive power descends. This computation is a direct algebraic reconstruction of the cited historical source, not a complete independent audit of the geometric reductions preceding it.
