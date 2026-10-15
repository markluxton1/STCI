# Independent review of torsion geometry on the second zero locus

Date: 2026-10-15. Reviewer: `universal_root_obstruction`.
Status: **PASS for the stated structural Picard, determinant, and
specified-component dimension claims**. The universal first incidence,
its accepted seed differential, and the actual second section's accepted
nonzero value are premises. No accepted certificate was replayed and no
new seed was evaluated.

Reviewed proof:
[torsion divisors and the second zero locus](2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry.md).

## 1. Intrinsic torsion and its ambient divisors

For a smooth `(2,2)` curve, both ruling systems have degree two. With an
origin on its elliptic normalization, the deck involution of a divisor
class with sum `a` is `p -> a-p`. Therefore the product of the two deck
involutions is translation by the degree-zero difference `eta=B-A`.
Its exact order is exactly the order of `eta`. This statement concerns
automorphisms of the root curve; it does not lift them to the ambient
formal neighborhood.

The local-moduli argument in the proposal is valid after an etale choice
of an origin with `A=O(2O)` and suitable finite level structure. The data
are an elliptic modulus, a nonzero Picard point `eta`, and two projective
coordinate frames. The two distinct degree-two systems give an embedding:
a pair of identified points would be interchanged by both ruling deck
involutions and force their centers, hence the systems, to agree;
a simultaneous ramification point forces the same equality. Thus this
parameter description covers the smooth root open locally with its
correct eight dimensions.

For fixed `n`, multiplication by `n` is etale on the relative elliptic
Picard curve in characteristic zero. Its kernel is finite etale, and
pullback along the free Picard parameter gives a smooth codimension-one
torsion condition. No transversality to the first compatibility scheme
follows from this ambient statement alone. Distinct exact-order strata
are open and closed within the fixed `n`-torsion condition, explaining
the stated equality of local germs at the order-two seed for each fixed
even `n`.

## 2. The cubic determinant is exactly the order-two locus

The equivalence `eta^2=1 <=> det M=0` is correct on the smooth root open.
If `eta^2=1`, the first ruling deck involution preserves the second
line bundle. It induces a nontrivial projective involution on the second
ruling: a trivial induced involution would fix both coordinates of the
embedded curve and hence the curve itself pointwise. A constant direction
coordinate change diagonalizes this involution. The odd quadratic
eigenspace consists only of multiples of `uv`, which cannot cut a smooth
`(2,2)` divisor. The root equation is therefore even, so its coefficient
matrix has rank at most two.

Conversely, rank one is excluded by basepoint freeness: all coefficient
quadratics would be proportional and have a common homogeneous base
zero. Rank two puts the fiber quadratics in a pencil. A degenerate
annihilator of that pencil is evaluation at a direction point, so it
means a common direction root. The corresponding fixed direction section
meets the remaining `(2,1)` component in degree two, contradicting
smoothness. A nondegenerate annihilator can be taken by a constant
projective direction change to the annihilator of `span(u^2,v^2)`.
The diagonal equation then gives `A^2=B^2` by its zero divisors.
The two line bundles are unequal for an embedded smooth `(2,2)` root,
so the order is exactly two.

All determinant-zero matrices on this open have rank exactly two.
The determinant hypersurface is smooth at every rank-two matrix, so
the proposal's global smooth-divisor statement on this open is justified.

## 3. The dimension drop is proved on the named component

At the accepted seed, the determinant differential is `12 delta b1`.
The variation `delta b1=1, delta c0=4` is killed by the accepted first
quotient differential: the only potentially nonzero rows are `4-4`
and `2-2`. It is not scalar variation of the seed. The determinant
functional takes value twelve on it. Thus the smooth four-dimensional
first compatibility component is transverse to the order-two divisor
at this seed. Their intersection has one smooth three-dimensional local
component there, whose reduced global irreducible component is the
specified `D`.

The actual second section is already known to be nonzero at the same
point. Its restriction to `D` is therefore not identically zero. The
support of its zero scheme is a proper closed subset of the irreducible
three-dimensional variety `D`, and hence has dimension at most two.
This is an actual dimension bound, not a dimension expectation from a
rank-sixteen vector bundle.

This argument does not control other components of the torsion
intersection or exact orders greater than two. It applies to the local
branch through the seed for fixed even spectral degrees, including eight
and twelve. It does not bound the entire torsion union, prove emptiness
of the second zero locus, or supply an actual CI. The proposal preserves
all those boundaries, as well as `s>4` in its stated CI application.

No commit or memory update was made.
