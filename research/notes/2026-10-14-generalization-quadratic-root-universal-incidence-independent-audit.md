# Independent review of the universal quadratic incidence and smooth seed

Date: 2026-10-14. Author: `geometric_locus`.

Status: **THE NEW UNIVERSAL MATRIX, SMOOTH ZERO, TORSION, AND LOCAL
DIMENSION CLAIMS PASS INDEPENDENT REVIEW.** The accepted actual first
ambient derivation is an input. This note does not repeat its chart audit,
the spectral theorem audit, or the proposed actual-CI-to-root-curve bridge
audit. No higher ambient lift or actual complete intersection is established.

Reviewed files:

- `2026-10-14-generalization-quadratic-root-universal-incidence.md`;
- `../computations/generalization_quadratic_root_curve_universal_incidence.py`.

The displayed formulae were checked independently from the accepted operator.
The explicit seed identity was first derived by hand. Two standard-library
`fractions.Fraction` calculations independently verified the reduced
differential below and the main note's full Jacobian minor `-405`.

## 1. Universal matrix and constant rank

For `f=a u^2+b uv+c v^2`, multiplication by a correction `A u+B v`
has coefficient vector

    (a A, b A+a B, c A+b B, c B).

Projection of a product with `p=p0+p1 z+p2 z^2` from the source powers
`z^-6,...,z^-1` to the target powers `z^-4,...,z^-1` gives exactly the
Toeplitz block `T(p)` in the main note. This checks all blocks of `A_f`.

Applying the accepted operator without projection first gives

    Df = d0 u^3+d1 u^2v+d2 uv^2+d3 v^3,

where

    d0=-5 a z^-4+3 b z^-5+a' z^-3,
    d1=-6 a z^-3-(7/2)b z^-4+6 c z^-5+b' z^-3+(1/2)a' z^-2,
    d2=-(3/4)a z^-2-(21/4)b z^-3-2 c z^-4+c' z^-3+(1/2)b' z^-2,
    d3=-(3/8)b z^-2-(9/2)c z^-3+(1/2)c' z^-2.

Collecting `z^-4,...,z^-1` gives all sixteen entries displayed in the
main note, including its base-derivative contributions.

The injectivity proof works on the entire basepoint-free open, including
singular and nonreduced root divisors. In fact the finite flat projection
`pi:Z->P1` gives

    0 -> O(-2)^2 -> O^4 -> E=pi_*O_Z(0,3) -> 0.

Thus `E` is a globally generated rank-two vector bundle of degree four.
Its two splitting degrees belong to `{0,...,4}`. Therefore
`H0(E(-5))=0`, and the divisor sequence implies that the multiplication
map `H1(O(-7,1))->H1(O(-5,3))` is injective. This establishes rank twelve
everywhere on the stated open.

Consequently the augmented rank condition and the incidence `A_f h=d_f`
give the same scheme there: locally an invertible twelve-row minor solves
uniquely for `h`, and the remaining four equations are the components of
the rank-four quotient obstruction. This is a scheme statement, not only
an equality of sets.

## 2. Exact seed identity and geometric smoothness

Put

    a=z^2+4, c=z^2-8, f0=a u^2+c v^2,
    h0=(-3z^-4-8z^-6)u+(-(1/8)z^-1-(9/2)z^-3)v.

Direct substitution gives

    Df0-f0 h0
      =32z^-6 u^3+((1/8)z-48z^-5)u^2v
       +(-(3/4)-64z^-6)uv^2+(1/8)z v^3.

Its specified Cech projection is zero, so this is an exact compatibility
certificate. In the prescribed source basis the vector is

    (-8,0,-3,0,0,0, 0,0,0,-9/2,0,-1/8).

The homogeneous coefficient quadratics are squarefree and disjoint.
Neither vanishes at base infinity. Over a root of `a`, the fiber point
has `v=0`, and smoothness follows from the simple root of `a`; the same
argument applies to a root of `c`, with `u=0`. Elsewhere a fiber partial
derivative is nonzero. At infinity both coefficients are nonzero, so the
fiber partial derivatives again give smoothness. This proves geometric
smoothness directly in both base charts. Equivalently the double cover
has four distinct branch points. Its root divisor is connected of genus
one.

Thus the first ambient obstruction does vanish on a smooth `(2,2)`
root curve. A proposed universal smooth-root exclusion at this order
would be false.

## 3. Independent differential calculation

The dual of the target Cech space consists of four polynomials
`q0,...,q3` of degree at most three, paired by taking the `z^-1`
coefficient of `sum q_i d_i`. The annihilator of multiplication by `f`
is given exactly by

    a q0+b q1+c q2=0,
    a q1+b q2+c q3=0.

At the seed, `b=0` and `gcd(a,c)=1`, so a basis of this four-dimensional
annihilator is

    qE=(c,0,-a,0), z qE,
    qF=(0,c,0,-a), z qF.

The differential of the quotient obstruction can therefore be computed
without choosing an inverse of any universal minor. Its four pairings
with a coefficient variation `delta f` are those of

    D(delta f)-h0 delta f

against this basis. In coefficient order

    (a0,a1,a2,b0,b1,b2,c0,c1,c2),

the resulting matrix is

```
     [  0    2   0   1/4  0   2    0   -2    0  ]
     [  1    0   8    0   4   0   -1    0  -20  ]
R =  [ -5/2  0   4    0   2   0  -1/2   0    2  ].
     [  0    8   0    1   0  -4    0    4    0  ]
```

The minor on columns `(a0,a1,a2,b2)` is `576`. Hence the quotient
differential is surjective. Since the correction directions already
span the twelve-dimensional image of `A_f0`, the full sixteen-equation
incidence Jacobian has rank sixteen.

As a separate consistency check, a second Fraction calculation built
`A_f` from its Toeplitz blocks and `d_f` from the displayed sixteen
formulas, differentiated `A_f h-d_f`, and obtained determinant `-405`
on the precise sixteen columns in the main note. The two computations
therefore verify the rank by different minors and different matrix
sizes.

The affine incidence is smooth of dimension five at `(f0,h0)`.
Projectivizing the nonzero equation `f0` removes one free scalar
direction. Uniqueness of `h` then gives a smooth four-dimensional
compatibility scheme at `[f0]`. Smoothness of the root curve is open,
so the compatible smooth-root locus has this positive local dimension.
This does not say that the ruling difference is torsion throughout it.

## 4. The seed's ruling difference has exact order two

Write `A=O_Z(1,0)`, `B=O_Z(0,1)`, and `eta=B tensor A^-1`.
On any smooth basepoint-free diagonal root curve

    a(z)u^2+c(z)v^2=0,

the section `c` of `A^2` vanishes exactly twice along the divisor of
the section `u` of `B`. Indeed at such a point, `a` and `v` are units
and the equation is `c=-a(u/v)^2`. Hence `A^2` and `B^2` are isomorphic.

The two degree-two complete linear systems cannot be isomorphic:
otherwise the two projections would differ by a projective automorphism
of `P1`, and the embedded curve in `P1 x P1` would be a graph rather
than a smooth divisor of type `(2,2)`. Thus `eta` is nontrivial of exact
order two. This argument proves the claim for the seed and, more
generally, for every smooth diagonal root curve.

An equivalent elliptic argument uses the deck involution
`sigma(z,[u:v])=(z,[-u:v])`: it preserves `B`, whereas its action on
`Pic^2` is `L -> A^2 tensor L^-1`. Again `B^2=A^2`.

Using the already accepted spectral theorem as a premise, the seed
therefore passes its even-degree descent condition. The present review
does not independently re-prove that theorem. First ambient compatibility
and spectral torsion coexist at this exact seed. Actual second ambient
compatibility, later lifts, polynomial realization, and support remain
separate questions.

## 5. Optional diagonal-slice classification

This section is an additional exact lemma, not needed for the preceding
review or the next obstruction calculation. Work geometrically over an
algebraically closed field of characteristic zero and impose `b=0`.
For a smooth diagonal root curve, `a,c` are squarefree, have no common
homogeneous root, and at least one has polynomial degree two.

The preceding dual basis remains exhaustive with

    q=(cL,cM,-aL,-aM), deg L,deg M<=1.

Set `W=ca'-ac'`. Its pairings with `Df` are the `z^-1` and `z^-2`
coefficients of

    E=-3ac z^-4+W z^-3+(3/4)a^2 z^-2,
    F=-(3/2)ac z^-3+6c^2 z^-5+(1/2)W z^-2.

Projection before pairing gives the same residues: discarded powers
below `-4` are at most `-5`, while every dual polynomial has degree at
most three; discarded nonnegative powers also cannot contribute.
The four compatibility equations are therefore

    (3/2)a0 a1-4a1 c2-2a2 c1=0,
    (3/4)a0^2-5a0 c2-3a1 c1-a2 c0=0,
    6c2^2-(5/2)a0 c2-(3/2)a1 c1-(1/2)a2 c0=0,
    -2a0 c1-a1 c0+12c1 c2=0.

Subtracting twice the third equation from the second gives
`a0^2=16c2^2`. Smoothness forces `c2!=0`: if `c2=0`, then `a0=0`
and the first equation gives `a2 c1=0`; either the coefficient
quadratics have a common root at infinity or `c` has a double root
there. Put `C=c2` and `P=a2`.

When `a0=4C`, any solution with `a1,c1` nonzero has `a,c`
proportional, contradicting basepoint freeness. Thus `a1=c1=0`,
`P c0=-8C^2`, and `P!=0`.

When `a0=-4C`, either `a1=c1=0` and `P c0=32C^2`, or

    P c0=-100C^2,
    P c1=-5C a1,
    a1^2=-(44/5)PC.

All three alternatives are smooth. In the last case the two quadratic
discriminants are `(36/5)PC` and `180C^3/P`, both nonzero. The only
possible common finite root is `z=-16C/a1`; substitution into `a`
gives `-(540/11)C`, also nonzero. In the two even alternatives the
squarefreeness and absence of common roots are immediate from the
displayed nonzero constants.

Under scaling of `f` and the compatibility-preserving coordinate change
`z -> lambda z, v -> lambda^-1 v`, every smooth compatible diagonal
curve has one of these three normal forms:

    (z^2+4)u^2+(z^2-8)v^2;
    (z^2-4)u^2+(z^2+32)v^2;
    (z^2+t z-4)u^2+(z^2-5t z-100)v^2, t^2=-44/5.

The two signs of `t` are identified by `lambda=-1`.

No commit or memory update was made.
