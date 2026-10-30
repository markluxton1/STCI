# An exact four-root exclusion for a birational elliptic residual image

October 29, 2026. Author: `m2_elliptic/elliptic_binary_search`.
Status: **provisional exact bounded calculation; independent review pending**.
This is a target-incidence exclusion inside the marked smooth-quadric
projection problem. It does not classify the full projection source.

## Literal stratum and result

Work over an algebraically closed field of characteristic zero, with the
source and notation of [the residual-geometry note](2026-10-29-projection-residual-geometry.md).
Assume the determinant divisor is `2c+D`, where `D` is a smooth irreducible
curve of class `(2,2)`, and assume its map to its image `C'` on the target
quadric is birational. Then `C'` has class `(6,2)`, its normalization is
`D` of genus one, and its two target ruling maps have degrees two and six.

If the intersection support `C' cap C0` is contained in the four target
points parametrized by

```
B = 0, infinity, 1, -1,
```

then full singleton inverse support is impossible. The same result holds
for `0,infinity,r,-r`, with any nonzero `r`, by the torus preserving `C0`.
Every subset of the four points is included. The calculation does not
assume that their intersection multiplicities are equal.

The crucial point is that counting four target intersection points is
insufficient: they can split into more than four points on the normalization.
The only genus-one image curves in this exact four-root locus have six
or eight normalized inverse points over `C0`, while `D cap c` has length
four.

The birationality assumption on `D -> C'` is separate from birationality
of the surface map. In particular a degree-two map from `D` onto a graph
of class `(3,1)` is not covered here.

## Complete coefficient source

Write the target quadric as `P1_A x P1_B`, with
`C0: A=B^3`. An equation of class `(6,2)` has the affine form

```
e0(A) + B e1(A) + B^2 e2(A) = 0,
```

where each `ei` has degree at most six. Restriction to `C0` is the binary
form of degree twenty with affine expression

```
P(t) = e0(t^3) + t e1(t^3) + t^2 e2(t^3).
```

Every exponent from zero to twenty occurs exactly once among these three
summands, so restriction is a linear isomorphism onto all binary forms
of degree twenty. Thus every nonzero restriction supported on the stated
four points is, up to scalar,

```
P(t) = t^a (t-1)^c (t+1)^d,
a+b+c+d = 20,
```

where `b` is the multiplicity at infinity, and all four integers are
nonnegative. There are exactly `binomial(23,3)=1771` tuples. Grouping the
coefficients of this polynomial by their exponent modulo three recovers
the unique triple `(e0,e1,e2)`.

A geometrically integral image of the specified bidegree must have
`max deg(ei)=6`, `e2 != 0`, and `gcd(e0,e1,e2)=1`. The first condition
rules out a fixed target ruling at `A=infinity`; the last rules out every
finite fixed target ruling. Of the 1771 tuples exactly 171 pass these
primitive-bidegree conditions.

Put `H=e1^2-4e0e2`. Over the algebraically closed constant field the
quadratic equation is geometrically integral exactly when `H` is not a
square in `k(A)`. If the odd squarefree part of `H` has degree `r`, its
double-cover normalization has genus `floor((r-1)/2)`: its finite branch
points are the roots of that part, and infinity is a branch point exactly
when `r` is odd, so this is immediate from Riemann--Hurwitz.

The exact rational computation exhausts all tuples and retains precisely
three genus-one triples:

| Multiplicities `(a,b,c,d)` at `(0,infinity,1,-1)` | Odd squarefree discriminant degree | Normalized inverse points at `(0,1,-1,infinity)` |
| --- | --- | --- |
| `(2,2,4,12)` | 3 | `(1,2,2,1)` |
| `(2,2,8,8)` | 4 | `(2,2,2,2)` |
| `(2,2,12,4)` | 3 | `(1,2,2,1)` |

The computation is over `QQ`, with polynomial gcds, not over a finite field.
Its squarefree decomposition records odd multiplicities, rather than
using the radical of the discriminant, which would give the wrong genus.

## Normalization point count

For the middle case the three coefficients are

```
e0 = A^6 - 56 A^4 + 28 A^2,
e1 = -8 A^5 + 70 A^3 - 8 A,
e2 = 28 A^4 - 56 A^2 + 1,
```

and

```
H = -48 A^2 (A-1)^2 (A+1)^2 (A^4-110 A^2+1).
```

At each finite point `B=0,1,-1`, put `A=B^3`. Direct substitution gives
`e2(A) != 0` and the quadratic `e2(A)(B-B0)^2`. The discriminant has
even order at each of these `A` values. The normalization therefore has
two points over that value of `A`, and both map to the indicated target
point. At infinity, reverse the degree-six coefficient polynomials and
use `1/B`; the same statement holds since `12-deg H=2` is even. Hence
there are eight distinct normalized points over `C0`.

For the first case,

```
e0 = A^6+24 A^5-88 A^4+88 A^3-36 A^2+8 A,
e1 = 24 A^5-120 A^4+198 A^3-120 A^2+24 A,
e2 = 8 A^5-36 A^4+88 A^3-88 A^2+24 A+1,
H = -16 A(A-2)(A-1)^2(A+1)^6(2A-1).
```

The points at `A=0,infinity` are branched, and those at `A=1,-1` are
unbranched. The quadratic target value again coincides at each point,
so there are `1+1+2+2=6` normalized points. The third case follows also
by `A -> -A, B -> -B`, and the exact verifier counts it directly.

Since a smooth `(2,2)` residual intersects the marked diagonal in total
length four, its normalization can have at most four points supported
there. Six or eight inverse points cannot all lie on the marked
intersection. This proves the exclusion for the stated stratum.

## Evidence and limitation

Run

```
M2 --script research/computations/stci_projection_m2_elliptic_special_2026_10_29.m2
```

The [script](../computations/stci_projection_m2_elliptic_special_2026_10_29.m2)
and [saved output](../computations/stci_projection_m2_elliptic_special_2026_10_29.txt)
record all three surviving genus-one coefficient triples, their exact
normalization counts, the count of 1771 exhausted multiplicity tuples,
and the final marker
`BIRATIONAL_ELLIPTIC_RESIDUAL_FOUR_ROOT_SPECIAL_LOCUS_EXCLUDED`.

The four-root configuration is restricted. Arbitrary four-point support,
other elliptic residual strata, singular or reducible residuals, and
nonbirational maps on the residual remain outside this calculation.
Neither an actual admissible surface projection nor a descending mate is
constructed here; the new result excludes a specified remaining incidence.
