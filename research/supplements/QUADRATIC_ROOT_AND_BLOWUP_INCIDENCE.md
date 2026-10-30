# quadratic root and blowup incidence

Permanent subject dossier retaining complete mathematical source arguments, their hypotheses, corrections, counterexamples and unresolved scope.

---

## 2026-10-14-generalization-quadratic-root-second-obstruction

# The second ambient obstruction is nonzero on the smooth torsion-two seed

Date: 2026-10-14. Author: `universal_root_obstruction`.
Status: **NEW EXACT ACTUAL-CHART CALCULATION; independent review in progress**.
The accepted embedded chart is an input. The accepted spectral obstruction
interpretation is an input. This note computes one new higher class,
without retesting accepted chart or conormal statements.

## 1. The hierarchy detects geometry that both first tests permit

The [universal quadratic incidence note](OCT14_QUINTIC_ROOT_AND_NORMAL_CARRIER_REVISIONS.md#source-2026-10-14-generalization-quadratic-root-universal-incidencemd)
constructs the actual first obstruction scheme `K`, proves it is smooth
of dimension four at the seed

    f=(z²+4)u²+(z²−8)v²,

and proves that this smooth elliptic root curve has ruling-difference
line bundle of exact order two. Hence both the actual first ambient
obstruction and the accepted spectral descent condition permit this
seed. Its **second** ambient obstruction is nonzero.

The second obstruction is relevant when no independent relation has yet
appeared by normal degree four, namely when the next relation degree
`s` satisfies `s>4`. In particular this includes the accepted numerical
abstract families with `s=8` and `s=12`. At `s=4`, the second relation
changes the target; the computation below does not give an exclusion.

This is a statement about the actual ambient first-relation lifting
problem. It becomes a necessary condition for actual supported complete
intersections only within a proved actual-CI-to-root-curve bridge and its
hypotheses. No unrestricted actual CI or STCI conclusion is asserted.

## 2. Retain the full chart, base motion, and equation unit

Use the accepted exact normal chart, with

```
den = z⁴+u+(3/2)zv,
w   = (z³+v)/den,
a'  = z/den−w³,
b'  = 1/den−w⁴,
u'  = a'/2,
v'  = −3w a'+2b'.
```

Its reduced base transition is `w=z^-1`; its first normal transition is
`u'=z^-7u`, `v'=z^-7v`. Set

```
f0=(z²+4)u²+(z²−8)v²,
f1=(1+4w²)u'²+(1−8w²)v'².
```

For the equation transition factor normalized by `z^-16`, choose the
first normal unit coefficient

    L1=(−5z^-4−8z^-6)u+(−(1/8)z^-1−(11/2)z^-3)v.

The first compatible cubic corrections can be chosen as

```
G0=(z/8)u²v−(3/4)uv²+(z/8)v³,
G1=−32w u'³+48u'²v'+64w u'v'².
```

Substitution into the accepted exact chart gives the literal identity
in normal degree three

    [ z¹⁶(f1+G1) ]_3 − G0 − L1*f0 = 0.                (1)

The unit `L1` differs from the quotient preimage `h` in the first-incidence
note by `2z*epsilon`, where `epsilon=[w−z^-1]_1`. This is the first
variation of `z²w²`. Keeping this term, rather than replacing `L1` by
`h`, is necessary in normal degree four. The nonlinear base coordinate
`w` is retained in both `f1` and `G1` throughout the substitution.

Let

    R4=[ z¹⁶(f1+G1) ]_4 − L1*G0.                    (2)

The terms subtracted in (2) come from the product of the first unit and
the first local correction. Unknown second unit coefficients multiply
`f0`; unknown quartic local corrections are Cech coboundaries. Thus the
second actual class is exactly the Laurent projection of (2), modulo
those multiples and coboundaries.

## 3. One sparse Serre-dual pairing proves nonvanishing

The second target is

    H1(Z,O_Z(-12,4))
      =coker[ H1(O(-14,2)) --f0--> H1(O(-12,4)) ],

with dimensions `39 -> 55 -> 16`. Use powers `z^-11,...,z^-1` in the
middle group, and `z^-13,...,z^-1` in the source. The multiplication map
is injective, since its kernel is `H0(Z,O_Z(-12,4))=0`.

Write `R4=sum_(i=0)^4 r_i(z) u^(4-i)v^i`. Only four coefficients are
needed for a nonzero dual pairing:

```
                  coefficient z^-3     coefficient z^-1
r1  (u³v)              5/8                    0
r3  (uv³)              9/8                  −3/32.
```

These coefficients follow from the exact substitution in (2). The
companion script also records every other quartic coefficient, so this
is a bounded computation with full retained output.

Put `a=z²+4`, `c=z²−8` and define

    lambda(r)=coefficient_z^-1[−c*r1+a*r3].           (3)

The polynomial dual vector is `(0,−c,0,a,0)`. It annihilates every
multiple of `f0` by a binary quadratic: on the odd source monomial `uv`
the coefficient is `a*(−c)+c*a=0`, while the other two source monomials
have only even target powers. The degree of each dual polynomial is two,
within the allowed degree ten. Therefore it also annihilates the full
Cech image of `H1(O(-14,2))`. It ignores all removed Cech coboundaries.

Using the displayed four coefficients gives

    lambda(R4)=−5/8+9/8−3/8=1/8 != 0.              (4)

Hence the actual second ambient class is nonzero. The complete rational
matrix calculation independently records multiplication rank `39` and
augmented rank `40`; the sparse identity (3)--(4) is already a proof.

## 4. This is a universal higher-obstruction mechanism on K

The seed calculation has a family-level consequence; it need not lead
to a list of further seeds. On the basepoint-free universal first
compatibility scheme `K`, the first compatible Cartier ideal is unique:
its possible differences lie in `H0(Z,O_Z(-5,3))`, which vanishes on
this entire open. The first corrections therefore glue, up to their
equation units, into the universal first lift.

Consequently there is a canonical second obstruction section over `K`.
Its rank-sixteen vector bundle is the relative version of

    coker[ H1(O(-14,2)) --f--> H1(O(-12,4)) ].

More precisely, on projective coefficient space the exact sequence is

    H1(O(-14,2)) tensor O_K(-1)
       --f--> H1(O(-12,4)) tensor O_K -> Q2 -> 0,

and the obstruction section has values in `Q2 tensor O_K(1)`.
The universal equation contributes the coefficient-space `O(1)` factor.
The multiplication map has constant rank thirty-nine: `pi_*O_Z(4)` is
globally generated of rank two and degree six, so twisting it by
`O(-12)` has no sections. Thus the cokernel is genuinely a vector
bundle, without deleting exceptional coefficient strata inside the
basepoint-free open.

The first class defines `K`; the second class is a section on `K`, not
another unrelated scalar test on the original parameter space. Its
nonzero value (4) proves that it is not identically zero on the
four-dimensional component through the smooth seed. Nonvanishing is
open, so a nonempty open subset of that component, and hence its
generic point, fails the second lifting step. The second zero locus on
that component remains to be determined. A rank-sixteen target on a
four-dimensional component does not by itself prove that zero locus is
empty, and no such claim is made.

This gives the structural next problem: describe the common zero scheme
of the actual higher-obstruction sections on `K`, intersected with the
spectral torsion loci, while retaining all equation-unit and second
relation extensions. The present computation proves that the hierarchy
adds a genuine obstruction after both the first class and Picard torsion
have passed. No additional seed or carrier-degree enumeration is needed
for that conclusion.

## 5. Exact artifacts and boundaries

- [Standard-library exact verifier](../computations/generalization_quadratic_root_seed_second_obstruction.py).
- [Full rational output and sparse dual certificate](../computations/generalization_quadratic_root_seed_second_obstruction.json).

Run with `python3 research/computations/generalization_quadratic_root_seed_second_obstruction.py`.
The verifier computes the accepted chart to normal degree four, verifies
(1), retains both the equation unit and nonlinear base motion in (2),
checks the full multiplication rank, and proves the simple pairing (4)
exactly. It does not sample, use floating point, or invoke a large CAS.

The seed has not been lifted through second exceptional order, so it
supplies no formal or projective CI construction. The result excludes
this first-relation seed from a first-principal-ideal lift through normal
degree four when `s>4`; it does not exclude every smooth root divisor,
every torsion order, or unrestricted `C0`. No commit or memory update
was made.


---

## 2026-10-14-generalization-quadratic-root-second-obstruction-independent-audit

# Independent review of the actual second obstruction at the smooth seed

Date: 2026-10-14. Author: `geometric_locus`.

Status: **THE NEW SECOND CLASS, SPARSE NONZERO PAIRING, AND STATED
FAMILY CONSEQUENCE PASS INDEPENDENT REVIEW.** The full embedded chart is
accepted input. No accepted chart or spectral theorem audit is repeated.
The calculation concerns the first principal relation through normal
degree four, so its stated CI application requires `s>4` and a proved
actual-CI-to-root-curve bridge with the relevant hypotheses.

Reviewed files:

- `2026-10-14-generalization-quadratic-root-second-obstruction.md`;
- `../computations/generalization_quadratic_root_seed_second_obstruction.py`;
- the accepted exact chart as recorded in
  `../computations/generalization_moving_first_relation_operator.py`.

The nonzero scalar below was derived independently by hand from the full
chart. It does not rely on the parent script's row reduction or on its
larger dual certificate.

## 1. The cubic patch and equation unit are consistent

Use the accepted exact chart

    den=z^4+u+(3/2)zv,
    w=(z^3+v)/den,
    a'=z/den-w^3, b'=1/den-w^4,
    u'=a'/2, v'=-3w a'+2b'.

For the seed put

    f0=(z^2+4)u^2+(z^2-8)v^2,
    f1=(1+4w^2)u'^2+(1-8w^2)v'^2.

The first base displacement is

    epsilon=[w-z^-1]_1=-z^-5 u-(1/2)z^-4 v.

Thus `beta=2z epsilon=-2z^-4 u-z^-3 v` and the proposed equation unit
is exactly `L1=h0+beta`, with `h0` the quotient preimage in the first
independent review. In particular, the unit has retained the base motion.

At normal degree three, the accepted derivation and the base factor give

    [z^16 f1]_3=Df0+beta f0.

The leading linear normal transition gives

    [z^16 G1]_3=-32z^-6 u^3+48z^-5 u^2v+64z^-6 uv^2,

for

    G1=-32w u'^3+48u'^2v'+64w u'v'^2.

The previously checked exact identity for `Df0-f0 h0` then proves

    [z^16(f1+G1)]_3-G0-L1 f0=0,

with

    G0=(z/8)u^2v-(3/4)uv^2+(z/8)v^3.

This independently verifies the first patch identity, including its unit.

For a quartic local correction and a second unit `L2`, the degree-four
gluing equation contains `L1 G0+L2 f0`. Therefore the proposed discrepancy

    R4=[z^16(f1+G1)]_4-L1 G0

has the correct sign and all required contributions. The unknown `L2`
is precisely a multiple of `f0` in the quotient target. No additional
`L1^2 f0` term is forced: the free second coefficient belongs to the unit
`1+L1+L2`, and would absorb such a reparameterization of the unit.

## 2. Independent sparse quartic calculation

Only the coefficients of `u^3v` and `uv^3` at powers `z^-3` and `z^-1`
are needed. Write `Uj=[u']_j`. The first two layers are

    U1=z^-7 u,
    U2=-(5/2)z^-11 u^2-3z^-10 uv-(3/8)z^-9 v^2.

To obtain the pure `v^3` coefficient in `U3`, set `u=0` and
`t=z^-3 v`. The full chart gives the exact rational expression

    u'=(z^-3/2)*((1+(3/2)t)^2-(1+t)^3)/(1+(3/2)t)^3.

Its numerator is `-(3/4)t^2-t^3`. Expanding the denominator to the
needed order gives

    [u']_(v^3)=(19/16)z^-12 v^3.

Consequently the `uv^3,z^-3` coefficient of `z^16[u'^2]_4` is

    2*(19/16)+2*(-3)*(-3/8)=37/8.              (1)

No other normalized term contributes to the four required coefficients.
This can be checked without expanding their full polynomials. Give
`z,u,v` weights `1,0,-1`. At normal degree `n`, the weights of `w,u',v'`
are respectively `-1-4n,-3-4n,-4-4n`. In normal degree four, the weights
of the four terms of `z^16 f1` are

    u'^2: -6,    4w^2u'^2: -8,
    v'^2: -8,   -8w^2v'^2: -10.

For `u^3v` these allow powers at most `z^-5`; for `uv^3` only the first
term reaches `z^-3`, as computed in (1), and none reaches `z^-1`.
The three normalized `G1` terms have weights `-10,-10,-12`, so they
cannot contribute to these four coefficients either.

Finally multiply the explicit `L1` and `G0`. Their contributions give

```
                         z^-3 coefficient    z^-1 coefficient
R4: u^3v                      5/8                   0
R4: uv^3          37/8-(-5/8+33/8)=9/8          -3/32.
```

This derives all four coefficients in the main note directly from the
full chart and the first patch data.

## 3. The scalar is a valid quotient obstruction

The second target is the Cech quotient

    H1(O(-14,2)) --f0--> H1(O(-12,4)),

with target powers `z^-11,...,z^-1`. Its Serre dual has five polynomial
entries of degree at most ten. Let `a=z^2+4`, `c=z^2-8`. The vector

    q=(0,-c,0,a,0)

belongs to this dual space and annihilates multiplication by `f0`.
Indeed the odd source monomial `uv` gives `-ac+ca=0`, while the two
even source monomials pair with zero entries. Thus

    lambda(R)=coefficient_z^-1(-c R_u3v+a R_uv3)

is a well-defined functional on the cokernel. Its degree-two entries
also annihilate removed Cech powers: powers below `-11` cannot be
shifted to `-1`, and nonnegative powers cannot contribute.

The four checked coefficients give

    lambda(R4)=-(5/8)+(9/8)+4*(-3/32)=1/8 != 0.

This proves nonvanishing of the actual second ambient class. The
multiplication map has rank thirty-nine by the constant-rank argument
below; adjoining a single vector with this nonzero pairing therefore
raises the rank to forty. A full row reduction is not needed for this
conclusion.

## 4. The stated family consequence is valid

On the entire basepoint-free open, the possible difference between two
first Cartier lifts is a section of `O_Z(-5,3)`. The first review proved
that its `H0` vanishes everywhere there, using the globally generated
rank-two pushforward of degree four. Thus the first lift is unique as
an ideal, even though its local equations can differ by units. The
first compatibility scheme is the scheme-theoretic zero locus of the
first obstruction, so local first lifts exist over it and their
uniqueness glues them. This also applies to its nonreduced parameter
structure by the relative cohomology/base-change statement with zero
`H0` and constant-rank presentations.

The second multiplication map has constant rank on this same open.
The finite-flat pushforward has an exact sequence

    0 -> O(-2)^3 -> O^5 -> E4=pi_*O_Z(0,4) -> 0.

The bundle `E4` is globally generated, rank two, degree six. Its
splitting degrees lie between zero and six; after twisting by `O(-12)`
neither has sections. This proves injectivity of the thirty-nine-column
second multiplication map for every basepoint-free coefficient point.

Over projective coefficient space, the universal root equation has
coefficient twist `O(1)`. Hence the natural exact presentation is

    39 O_K(-1) --f--> 55 O_K -> Q2 -> 0,

with `Q2` locally free of rank sixteen. The normalized discrepancy
scales linearly with the universal equation. Its canonical second
obstruction is accordingly a section of `Q2 tensor O_K(1)`, as stated
in the main note. Uniqueness of the first ideal ensures that local
choices of first equations and units give the same quotient section.

At the smooth seed this section is nonzero. The first compatibility
scheme is smooth of dimension four there, so there is a unique
irreducible component through that point. The section is not identically
zero on that component; its nonvanishing locus is a nonempty open
subset and contains the generic point. This proves generic failure
of the second lifting step on that component. It does not prove that
the second zero locus is empty and does not assert torsion throughout
the component.

For `s>4`, no independent second relation has entered by this normal
degree, so the first-principal-ideal obstruction is relevant to the
stated bridge lane. For `s=4` the target can change, and no exclusion
was proved. The result leaves higher zero loci, their intersections
with torsion strata, later ambient extensions, and actual polynomial
realization unresolved.

No commit or memory update was made.


---

## 2026-10-14-generalization-quadratic-root-universal-incidence-independent-audit

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


---

## 2026-10-14-generalization-blowup-root-curve-primitive-bridge

# Saturated first relations turn an actual CI into a primitive root-curve multiple

Date: 2026-10-14. Author: root. Status: **WRITTEN GEOMETRIC THEOREM;
independently audited under the stated hypotheses**. The
[independent bridge audit](QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md#2026-10-14-generalization-blowup-root-curve-bridge-independent-audit)
includes separate local-algebra and conormal reviews, a shorter local
proof, and a defect-boundary family. The spectral root-curve criterion and its
already reviewed ambient obstruction class are premises. This note
supplies a bridge from an actual supported complete intersection to
that obstruction. It does not assert that the obstruction is nonzero.

## 1. Hypotheses

Let C be a smooth curve in a smooth threefold X over an algebraically
closed field of characteristic zero. Let Y=(F,G) be an actual complete
intersection supported exactly on C. Use the ordinary I_C-adic initial
ideal. Assume:

1. Its first nonzero generic normal relation has degree r and its actual
   degree-r relation sheaf R is a saturated line subbundle of Sym^r N_C^*.
2. Both actual equations F,G have generic normal order r. Their leading
   symbols generate R at every point. Equivalently their coefficient
   pair in local frames of R has no common zero on C.
3. The full generic initial ideal is a binary regular sequence (f_r,g_s),
   with s>r, and g_s coprime to f_r. Set k=s-r and assume k>=2.
4. The actual Cartier root divisor Z of f_r on the exceptional divisor
   of Bl_C X is smooth, hence reduced. Smoothness of its reduced support
   alone is insufficient. It may be treated componentwise if disconnected.

The first hypothesis often forces the second when the two equations
generate the whole actual relation sheaf; it is nevertheless stated
explicitly here. A divisor where both leading coefficients vanish is a
genuine excluded hypothesis, not a set to be saturated away. At such
points vertical exceptional components may occur.

Let B=Bl_C X, let E be its exceptional divisor, and let D_F,D_G be the
strict-transform Cartier divisors. Their local equations are obtained
by dividing the pullbacks of F,G by the r-th power of an exceptional
equation. Write Y'=D_F intersect D_G.

## 2. The strict intersection has support exactly Z

Off E the blowup is an isomorphism and the original intersection has
no point off C. Hence Y' is supported on E. On E the two transformed
equations are a f_r and b f_r, where a,b are the actual leading
coefficients. Since a,b have no common zero, their common zero set on
E is exactly Z. In particular no exceptional fiber P1 over a point of
C is a curve component of Y'. Such a fiber could be shared only if
both leading coefficients vanished there, or if f_r vanished on the
whole fiber; both possibilities are excluded by the hypotheses.

The two strict divisors have no common surface component, since their
images would be a common surface component of F,G. They form a
regular sequence on the smooth threefold B. Thus Y' is a pure
one-dimensional complete intersection with reduced support Z; there
is no discarded isolated or embedded component.

At the generic point of C, the usual normal blowup calculation for
the binary regular sequence (f_r,g_s) gives transverse length k=s-r
on every root branch. Indeed one may choose a standard basis of
normal orders r,s generating the actual completed generic ideal: a
lift of g_s together with an original equation whose leading symbol
is f_r generates the full initial ideal, hence the actual ideal by
filtered division. Both original equations were divided by u^r, so
this invertible change of generators preserves their strict-intersection
ideal. On a chart with exceptional parameter u, its generators reduce to

```
f_r+O(u),   u^(s-r)(g_s+O(u)) modulo the first equation.
```

A smooth root is simple over the generic point, and g_s is nonzero
there. Eliminating the first equation leaves u^k. Therefore the
generic algebra of Y' along each component of Z is curvilinear of
length k. This calculation uses the full generic initial regular
sequence, not merely two chosen original normal orders.

## 3. The first normal layer is a line bundle everywhere

The conormal sequence for Z subset E subset B is

```
0 -> O_Z(-E) -> N_(Z/B)^* -> O_Z(-Z_E) -> 0.          (1)
```

Project the first normal symbols of D_F,D_G to the last term. They
are precisely a df_r,b df_r. Smoothness of Z makes df_r a local
generator of O_Z(-Z_E), and the coefficient pair is basepoint-free.
Thus their joint normal-symbol map surjects onto the last term.
Here df_r is the full conormal differential on E, including its base
direction; it is not just the fiber derivative. Smooth ramification
of Z over C causes no failure of this surjectivity.

Their determinant vanishes generically on every component of Z:
the intersection has transverse length k>=2 and is generically
curvilinear. The determinant is a regular section of a line bundle
on the smooth reduced Z, so it vanishes identically. The two first
symbols therefore have rank one at every point, and at least one
has a unit projection to the last term of (1). Their image K is a
line subbundle, with an isomorphism

```
K -> O_Z(-Z_E).
```

This splits (1). Its quotient is canonically O_Z(-E). In particular
the **actual** first ordinary normal layer of Y' is

```
J/J^2 = O_Z(-E),   J=I_Z O_(Y'),                    (2)
```

without a point-supported torsion term. This conclusion would be
false if joint leading base points had been removed instead of
retained.

## 4. The entire strict intersection is primitive

The preferred proof is local on the smooth strict surface and works
before completion. At a point p of Z, choose one transformed equation
h whose leading coefficient is a unit. Since h|E=a f_r with a(p)!=0
and Z is smooth in E, the surface S=(h) is smooth at p and meets E
transversely along Z. An exceptional equation u therefore cuts out
Z as a reduced Cartier divisor on S.

The other transformed equation h_2 restricts to a nonzero equation
on S supported exactly on Z. The regular local surface ring is a
UFD, so h_2|S is a unit times u^e. Its generic multiplicity is the
already computed k=s-r; consequently e=k and

```
I_(Y',p)=(h,u^k).
```

This proves embedded primitivity everywhere and identifies its
surviving conormal with O_Z(-E). It also realizes Y' locally as a
Cartier divisor on the exceptional thickening E_k=V(I_E^k).

For completeness, the original formal argument is consistent with
this direct proof. At a point of Z complete and lift a curve parameter
t. Purity makes t a nonzerodivisor, and the local ring A of Y' is finite free of
rank k over R0=Bbbk[[t]]. Its nilradical J has J^k=0 everywhere, by
purity and the generic nilpotence bound. From (2), Nakayama makes
J a principal ideal generated by a lift z of its free first layer.
The reduction of A modulo t is consequently generated by z. Thus
R0[z]/(z^k) maps surjectively to A; both are free of rank k, so the
map is an isomorphism.

Hence Y' is an actual embedded primitive k-fold curve everywhere
along Z. Its local smooth containing equation has first relation
K from Section 3, and its surviving conormal is O_Z(-E). This is
stronger than generic curvilinearity or a numerical socle match.
No socle-degree enumeration is needed to obtain primitivity here.

## 5. Consequence for the ambient root-curve obstruction

Let J_E=O_E(-E). The square-zero first neighborhood of E has the
reviewed class

```
kappa in Ext1_E(Omega_E,J_E).
```

For its smooth Cartier root divisor Z, restriction and contraction
with df_r gives the conormal extension (1), whose class is

```
kappa(df_r) in H1(Z,O_Z(Z_E) tensor J_E|Z).           (3)
```

Section 3 splits that extension. Therefore every actual supported
complete intersection satisfying the hypotheses must have

```
kappa(df_r)=0.                                     (4)
```

The local ideal (h,u^k) shows that I_E^k is contained in I_(Y'),
and I_(Y')/I_E^k is locally the invertible ideal generated by h on
E_k. Thus the primitive k-fold structure is an actual global Cartier
lifting of Z into E_k and supplies compatibility of the same
Cartier relation through every exceptional order strictly below k.
Those are the root-curve obstruction bundles already identified in
the spectral note. If their relevant H0 groups vanish, compatible
finite principal ideals are unique, but their actual obstruction
classes must still be evaluated; negative bundle degree is not
itself a nonvanishing theorem.

For the accepted C0 conormal O(-7)^2, E=P1 x P1 and
J_E=O(-7,1). A first quadratic relation of movement degree two
has root divisor of type (2,2). The entire family has first target

```
H1(Z,O_Z(-5,3))
 = coker[H1(O(-7,1)) --f--> H1(O(-5,3))],
dimensions 12 -> 16 -> 4.
```

Thus one universal lifting incidence on the coefficients of f is
necessary for every actual CI in this lane, independently of
both hypersurface degrees. This is the appropriate shared next
problem, rather than enumerating the numerical profiles of the
abstract elliptic graded families.

## 6. Boundaries and audit disposition

The theorem leaves nonzero first-relation defects, singular or
nonreduced root divisors, noncoprime next relations and k=1 outside
the primitive conclusion. The generic normal order of the chosen
two equations, their joint leading base points, and full original
set-theoretic support are substantive hypotheses. None is inferred
from generic Hilbert data alone.

The independent audit passes the generic blowup multiplicity, exact
support and absence of vertical fiber components, global conormal
splitting, entire embedded primitivity, and necessity kappa(df_r)=0.
It retains the first-relation defect boundary explicitly: the family
F=t f_r+h_(r+1), G=F+f_r^q, with f_r squarefree, h_(r+1) coprime,
and q>=2, is supported exactly on C=(x,y) but has actual first
relation t O_C f_r. Both leading coefficients vanish at t=0, and
the strict intersection contains that entire exceptional fiber.
Saturating the first relation cannot discard this boundary.

The actual ambient class still has to be evaluated. The accepted
spectral criterion, normal bundle, ambient chart and earlier carrier
exclusions were not reverified.
The universal STCI question and unrestricted C0 remain open.


---

## 2026-10-14-generalization-blowup-root-curve-bridge-independent-audit

# Independent audit of the actual-CI blowup/root-curve bridge

Date: 2026-10-14. Status: **NEW GEOMETRIC BRIDGE PASSES UNDER ITS
LITERAL HYPOTHESES**. Reviewer: independent bridge-review worker, with
separate local-algebra and conormal subreviews. This is a written
mathematical audit, not a finite computation or a claim of ambient
obstruction nonvanishing.

Reviewed source:
[blowup/root-curve primitive bridge](QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md#2026-10-14-generalization-blowup-root-curve-primitive-bridge).
The accepted
[spectral root-curve theorem](MOVING_POWER_AND_SPECTRAL_ROOTS.md#2026-10-14-generalization-spectral-root-curve-relations)
and its
[independent audit](MOVING_POWER_AND_SPECTRAL_ROOTS.md#2026-10-14-generalization-spectral-root-curve-independent-audit)
are premises. Their spectral descent criterion, ambient extension class,
and cohomology targets were not reaudited. No previous CAS or carrier
certificate was replayed.

## 1. Precise conclusion and hypotheses

Let `C` be a smooth curve in a smooth threefold `X` in characteristic
zero. Work on a connected component of `C` when necessary. Let an actual
complete intersection `Y=(F,G)` have reduced support exactly `C`. Retain
all the hypotheses in the reviewed source:

- The first actual ordinary normal relation has degree `r`; its relation
  sheaf is a saturated line subbundle `R` of `Sym^r N_C^*`.
- The two **chosen actual equations** have generic normal order `r`, and
  their degree-`r` symbols jointly generate `R` at every point of `C`.
- At the generic point of `C`, the **full ordinary initial ideal**, not
  just two selected initial forms, is the binary regular sequence
  `(f_r,g_s)`, where `s>r`, `g_s` is coprime to `f_r`, and `k=s-r>=2`.
- The actual Cartier root divisor `Z=(f_r)` on the exceptional divisor
  `E` of `B=Bl_C X` is smooth. In particular, `Z` itself is reduced;
  smoothness of its reduced support alone is insufficient.

Then the intersection `Y'=D_F intersect D_G` of the strict-transform
Cartier divisors has support exactly `Z`, contains no vertical
exceptional-fiber curve component, and is everywhere an embedded
primitive `k`-fold structure on `Z`. Its first ordinary normal layer is
canonically `O_Z(-E)`. The conormal extension

```
0 -> O_Z(-E) -> N_(Z/B)^* -> O_Z(-Z_E) -> 0             (1)
```

splits, so the actual first ambient root-divisor obstruction obeys

```
kappa(df_r)=0.                                        (2)
```

The conclusion concerns this stated lane of actual supported complete
intersections. It makes no claim that the hypotheses exhaust all STCI
presentations, and it makes no claim that the fixed ambient obstruction
has a nonzero value.

## 2. Support, vertical fibers, and purity

Locally write the exceptional equation as `u`. Because each chosen
equation has normal order `r`, its strict transform is obtained by
dividing its pullback by `u^r`. On `E`, the two transformed equations
restrict to `a f_r,b f_r`. The coefficient pair `a,b` has no common zero
on `C`, and the line-subbundle condition means that `f_r` is not the zero
binary polynomial on any exceptional fiber.

The common zero set on `E` is therefore exactly `Z`. Away from `E`, the
blowup is an isomorphism, and the original pair has no common point away
from `C`. Thus `Supp(Y')=Z`. In particular, no entire exceptional fiber
is a component of the strict intersection.

Neither strict divisor contains `E`. A common surface component outside
`E` would give a common surface component of the original pair. Hence
the strict equations have height two in the smooth threefold `B` and
form a regular sequence. Their intersection is a one-dimensional
Cohen--Macaulay scheme with no embedded or isolated component. No
component or closed point has been discarded in this argument.

## 3. Generic transverse multiplicity really is `s-r`

Let `K` be the function field of `C`, and complete the generic normal
local ring to `K[[x,y]]`. Choose a lift `H` in the actual ideal whose
initial form is `g_s`. Use one original equation with nonzero generic
leading coefficient as `P`; its initial form is a nonzero scalar
multiple of `f_r`. Since these initial forms generate the **entire**
initial ideal, successive filtered division gives

```
(P,H)=(F,G) in K[[x,y]].                              (3)
```

One can also obtain (3) from equality of the two finite colengths: the
coprime homogeneous initial forms of `P,H` give colength `rs`, equal to
the colength determined by the stated full initial ideal of `(F,G)`.
Consequently these two generating pairs differ by an invertible local
matrix. Both original equations were divided by the same `u^r`, so this
change of generators preserves the strict-intersection ideal.

On a normal blowup chart `x=u,y=uv`, that ideal is

```
( P/u^r, H/u^r )
 = ( f_r(1,v)+O(u), u^(s-r)(g_s(1,v)+O(u)) ).          (4)
```

After a finite extension of `K`, each generic root can be treated
separately. The root is simple because the actual root divisor is
smooth and reduced, finite over `C`, and generically separable in
characteristic zero. Coprimality makes the second parenthesis a unit at
that root. The first equation eliminates the root coordinate, leaving
the transverse algebra `L[[u]]/(u^k)`, where `L` is the root field and
`k=s-r`. This proves the claimed multiplicity on every root component.

Two arbitrary selected orders would not justify (3) or (4). The full
generic initial complete-intersection hypothesis is doing substantive
work here.

## 4. Direct local proof of primitivity everywhere

There is a shorter proof than the completion argument in the reviewed
source, and it proves a useful additional local normal form. Fix
`p in Z`. Choose one transformed equation `h` whose leading coefficient
is a unit at `p`. This is possible by joint leading basepoint freeness.
Since

```
h|E = a f_r,                 a(p) != 0,
```

and `Z` is smooth in `E`, the surface `S=(h)` is smooth at `p` and meets
`E` transversely along `Z`. In particular the exceptional equation `u`
cuts out `Z` as a reduced Cartier divisor on the regular local surface
`S`.

Let `h_2` be the other strict equation. Its restriction to `S` is
nonzero and has zero set exactly `Z`. In the regular local ring
`O_(S,p)`, it must therefore be

```
h_2|S = epsilon u^e,              epsilon a unit.       (5)
```

Indeed a two-dimensional regular local ring is a UFD, and `(u)` is the
only height-one prime in its zero set. The generic multiplicity from
Section 3 fixes `e=k`. Lifting the unit in (5) gives the exact local
ambient ideal

```
I_(Y',p) = (h,u^k)                                   (6)
```

already before completion. This proves the entire embedded primitive
conclusion at every point, not only generic curvilinearity. It also
proves directly that the surviving conormal is the exceptional
conormal `O_Z(-E)`.

The source's completion/Nakayama proof passes as well: over a completed
smooth-curve parameter ring the local algebra is finite free of rank
`k`; a generically zero submodule is zero by torsion freeness, so `J^k=0`;
the invertible first layer makes `J` principal; the resulting surjection
from the rank-`k` truncated polynomial algebra is an isomorphism. The
direct proof (6) avoids those auxiliary finiteness and nilpotence steps.
For readability, its coefficient field should be denoted `Bbbk` rather
than `k`, since `k` already denotes the multiplicity.

## 5. Conormal splitting, including ramification points

For an independent check of the source's conormal argument, put

```
L=O_Z(-E), M=O_Z(-Z_E), V=I_Z/I_Z^2.
```

Let `phi` be the map from the two equation line bundles to `V` given by
their first normal symbols. The quotient map `q:V -> M` sends these
symbols to `a f_r,b f_r` in the conormal line, or to `a df_r,b df_r`
under its differential embedding in `Omega_E|Z`. Hence `q phi` is
surjective.

The determinant of `phi` vanishes at the generic point of every
component of `Z`: independent linear terms there would give transverse
length one, contrary to `k>=2`. Since `Z` is reduced, this regular
determinant section vanishes identically. Locally choose a symbol `v`
with `q(v)` a unit and complete it to a basis `v,e` of `V`. Writing the
other symbol as `av+be`, the zero determinant forces `b=0`. Thus

```
K=im(phi) is a line subbundle,  K -> M is an isomorphism,
V/K = L canonically.                                  (7)
```

This splits (1). Moreover, with `J=I_Z O_(Y')`, the ordinary first layer
is exactly

```
J/J^2 = I_Z/(I_Z^2+I_(Y')) = V/K = O_Z(-E),            (8)
```

so no point-supported torsion has been suppressed.

Here `df_r` means the **full differential on `E`**, including the base
direction. No unramifiedness hypothesis on `Z -> C` is needed. For
example, at a smooth ramification point the root equation may be
`f=t-v^2`: its fiber derivative vanishes at the origin, but
`df=dt-2v dv` does not. Using only the fiber derivative would invalidate
this argument.

## 6. Actual exceptional lifts and the obstruction implication

The local form (6) also globalizes the higher-order interpretation.
Writing `E_k=V(I_E^k)`, one has `I_E^k subset I_(Y')`, and
`I_(Y')/I_E^k` is locally generated by the nonzerodivisor `h` on `E_k`.
It is therefore an invertible ideal on `E_k`. Thus `Y'` is an actual
Cartier lifting of `Z` into `E_k`, and restriction gives compatible
Cartier liftings through every exceptional order strictly below `k`.
This does not supply lifts at or beyond order `k`.

The first obstruction implication can also be checked directly from
the conormal diagram. Restrict the ambient cotangent extension to `Z`:

```
0 -> L -> Omega_B|Z -> Omega_E|Z -> 0.
```

Its extension class is the restriction of the accepted first-neighborhood
class `kappa`. Pull it back along

```
df_r:M -> Omega_E|Z.
```

Because `Z` is smooth, the pullback middle term is precisely `V`, giving
(1). Consequently

```
class(1) = df_r^*(kappa|Z)
         in Ext1_Z(M,L)
          = H1(Z,O_Z(Z_E) tensor O_Z(-E)).              (9)
```

The splitting in (7) proves (2). This uses the actual geometric class,
not merely the dimension of its cohomology target. An opposite Cech
extension convention can negate its representative and has no effect
on the vanishing assertion.

## 7. Nonzero first-relation defects must retain their base points

The hypotheses cannot be replaced by saturation of a defective first
relation. The following family exhibits the precise failure without
any degree enumeration.

In `A3_(t,x,y)`, let `C=(x,y)`. Choose a squarefree homogeneous binary
form `f_r(x,y)` and a homogeneous form `h_(r+1)(x,y)` coprime to `f_r`.
For an integer `q>=2`, set

```
F=t f_r+h_(r+1),       G=F+f_r^q.                     (10)
```

This is an actual height-two complete intersection supported exactly on
`C`: its common zero set is `f_r=h_(r+1)=0`, whose only normal-plane point
is the origin. Both chosen equations have generic normal order `r`.
Over `Bbbk(t)`,

```
(F,G)=(t f_r+h_(r+1), h_(r+1)^q),
```

and the coprime initial forms give the full generic initial complete
intersection of degrees `(r,q(r+1))`, with gap at least two. The
saturated first relation has the smooth root divisor given by the
distinct constant root sections of `f_r`.

However, the **actual** degree-`r` relation sheaf is `t O_C f_r`, whose
inclusion has a first-relation defect at `t=0`. Both actual leading
coefficients vanish there. On the exceptional divisor, the restrictions
of the two strict equations are both `t f_r`, so their intersection
contains the entire exceptional fiber over `t=0`.

Thus the nonzero defect is a real boundary stratum. Its joint leading
base point cannot be deleted or cured by replacing `t O_C f_r` with its
saturation. This family is outside the reviewed theorem and does not
contradict it.

## Audit disposition

The generic blowup length, exact support/no-vertical-component claim,
global first-layer splitting, entire embedded primitivity, and necessity
`kappa(df_r)=0` all pass under the literal hypotheses. The direct local
normal form `(h,u^k)` supplies a structural proof with no socle-profile
or degree enumeration. The retained boundaries are the actual
first-relation defect and its base points, singular or nonreduced root
divisors, noncoprime next relation, generic initial ideals outside the
stated binary complete-intersection form, unequal chosen normal orders,
and gap one. The value of the fixed ambient obstruction remains a
separate new problem. The universal STCI question and unrestricted
characteristic-zero `C0` remain open.


---

## 2026-10-14-generalization-cartier-lift-independent-audit

# Independent audit: Cartier rational lifts on normalizations of arbitrary degree

Date: 2026-10-14, America/New_York. Auditor: `frontier_reconcile`.
Status: **PASS FOR THE NEW SINGULAR-NORMALIZATION EXTENSION UNDER ITS
EXPLICIT CARTIER, SINGLETON AND DEGREE-ONE LIFT HYPOTHESES**.

Source audited:
[Cartier-lift minimal-degree theorem](OCT14_CARTIER_LIFTS_AND_MOVING_RELATIONS.md#source-2026-10-14-generalization-cartier-lift-minimal-degreemd),
SHA-256 `0a120c0caf2847b38c749fd47adddc0896a864c1b44e1646225889b34f7055ba`.
The [smooth-normalization theorem](OCT13_THICK_EQUALITY_SOCLE_AND_FILTRATIONS.md#source-2026-10-13-generalization-smooth-normalization-independent-auditmd)
is an accepted premise and was not rechecked. This audit concerns only the
new singular scope, cone polarization and added consequences. No inherited
verifier, mathematical source or remote branch was reread to reconfirm it.

## 1. Exact theorem and new scope

Over an algebraically closed field of characteristic zero, let a smooth
rational curve C of degree d have an actual mate on an integral degree-a
hypersurface X. Let `nu:S->X` be its finite normalization and
`H=nu*O_X(1)`. Assume the full reduced inverse image is a single smooth
curve c mapping isomorphically to C and **c is Cartier on S**.

Then the complete system |c| identifies S with a normal minimal-degree
surface. In addition to the accepted smooth entries, the only new entry is
a rational-normal cone of degree

    n=c^2=d^2/a>=2,
    H=(d/n)c,
    n divides d.

For fixed C0, the accepted all-quartic theorem leaves exactly three
normalization/polarization targets:

    a=8:  P1xP1, c=(1,1), H=(2,2);
    a=8:  quadric cone, c a smooth Cartier conic, H=2c;
    a=16: P2, c a line, H=4h.

The new target is the quadric cone. Actual projections and complete
conductor descent remain conditions, so none of these entries asserts an
existing mate. Non-Cartier lifts and multiple or nonisomorphic inverse
curves remain outside the theorem.

## 2. Independent review of the extra singular argument

At a closed point of c, let R be the normal surface local ring and f a
local Cartier equation. Since `R/(f)` is the regular one-dimensional
local ring of c, a lift t of its parameter together with f generates
the maximal ideal of R. Thus its embedding dimension is at most two,
equal to its dimension. R is regular. At the generic point normality
already gives a DVR. Therefore S is regular along all of c; over the
algebraically closed characteristic-zero field it is smooth there.
Its possible singularities are isolated and disjoint from c.

The actual mate divisor gives `m c~bH`, `md=ab`. This makes O_S(c)
ample directly: a positive power is the ample O_S(bH). In particular
`n=c^2=d^2/a` is a positive integer. Cartierness supplies the integral
self-intersection even though S may have singularities elsewhere.

Choose a resolution `sigma:M->S` that is an isomorphism near c. No
exceptional component occurs in the pullback of c, because the resolution
centers lie away from its support. Consequently

    c_M=sigma*c,
    c_M^2=n,
    m c_M~b L, where L=sigma*H is nef and big.

Adjunction takes place in the unchanged smooth neighborhood of c_M and
gives `K_M.c_M=-n-2`. Hence

    K_M.L=(m/b)(-n-2)<0.

An effective canonical multiple has nonnegative intersection with the
nef L, so none exists. The already used characteristic-zero surface
classification makes M rational or birationally ruled over a
positive-genus curve. The latter ruling extends after the point
contractions to its minimal ruled model. Its restriction to the rational
c_M is constant, so c_M is a fiber component. Intersecting that effective
fiber with c_M gives

    0=m0*c_M^2+sum mi*(Di.c_M),

with m0>0 and every remaining intersection nonnegative. This contradicts
n>0. Therefore M is rational. Notice that c_M need not be ample on M;
positive self-intersection is enough for this ruling contradiction, and
nefness of L is enough for the canonical argument.

Normality gives `sigma_*O_M=O_S`. The degree-one Leray edge sequence has
an injection

    H1(S,O_S) -> H1(M,O_M)=0.

Thus `H1(S,O_S)=0`. This step requires no vanishing of
`R1 sigma_*O_M` and no prior rational-singularity hypothesis. In
particular the proof has not smuggled such a hypothesis into the new
singular scope.

The accepted complete-system argument now applies using the actual
Cartier sequence

    0 -> O_S -> O_S(c) -> O_c(c)=O_P1(n) -> 0.

Its proof uses ampleness, this restriction surjectivity and the degree
bound, rather than smoothness away from c. It gives a finite birational
map to an integral normal minimal-degree surface. A finite birational
map to a normal target is an isomorphism. The surface classification
therefore supplies the plane, Veronese, smooth scroll or rational-normal
cone; in dimension two there is no additional singular family.

## 3. Cone Picard computation and integral polarization

For the degree-n rational-normal cone with n>=2, its minimal resolution
is F_n. Write its exceptional negative section E and fiber f, with

    E^2=-n, E.f=1, f^2=0.

The hyperplane pullback is `L_c=E+n f`. This is the usual cone
polarization: it has degree zero on the contracted E, degree one on
each ruling f and square n. The smooth Cartier hyperplane c avoids
the vertex, consistently with regularity along c established above.

Pullback on line bundles is injective. Indeed, if a line bundle A
pulls back trivially, the projection formula and
`sigma_*O_M=O_S` give

    A=sigma_*sigma*A=sigma_*O_M=O_S.

Every pulled-back Cartier line bundle has degree zero on the contracted
E. In the free Picard group `Pic(F_n)=ZE+Zf`, a class xE+yf
therefore satisfies

    -n x+y=0,

so it is an integer multiple of L_c. Since c itself pulls back to
L_c, injectivity implies `Pic(S)=Z[c]`, with no unnoticed fractional
or torsion generator. Thus the ample H is an integer multiple q c,
and

    d=H.c=q n,
    q=d/n,
    n divides d,
    a=H^2=d^2/n.

This proves the only extra integrality constraint needed by the singular
extension. For n=1 the cone is P2 and already belongs to the line entry.

For d=4, the new cone degrees are n=2 and n=4. The latter would have
a=4 and is removed by the accepted theorem. The former has a=8 and
is the quadric cone with H=2c. Together with the two accepted smooth
higher targets this gives the complete three-entry list.

## 4. Additional degree-free corollary: downstairs Cartier rational curves

The source's normal-carrier consequence is correct. In fact its scope
can be strengthened without using the characteristic-zero classification.

**Corollary, every characteristic.** Let C be a smooth integral curve of
degree d and genus g over an algebraically closed field. Suppose an
integral degree-a hypersurface X contains C as a Cartier curve and has
an actual mate for C. Then X is normal and

    a divides d^2,
    2g-2=d^2/a+(a-4)d.                         (G)

Consequently a is a positive divisor of d^2 and satisfies the strict
bound `a<4+(2g-2)/d`, independent of the mate degree. For rational C,
the only numerical possibilities are

    X a plane, C a line or smooth conic;
    X a quadric, C a smooth Cartier conic.

In particular every smooth rational curve of degree d>=3 is non-Cartier
on every integral carrier on which it has a mate. This statement is about
Cartierness on X itself; it does not exclude the three nonnormal
Cartier-normalization-lift targets above.

Proof of normality. The same quotient-regular local argument makes X
regular along the smooth Cartier C. The mate's Cartier zero divisor D
has reduced support C. In the regular neighborhood of C it is `m C`
for one positive integer m; away from C both Cartier divisors are zero.
Thus `m C~b O_X(1)` globally, and C is ample. Every codimension-one
nonregular component would be a projective curve disjoint from C.
Its restriction of O_X(C) would be trivial, since the canonical section
has no zero there; ampleness would require strictly positive degree.
This is impossible. Thus X satisfies R1. A hypersurface is Cohen--Macaulay,
hence S2, so Serre's criterion makes X normal. This argument permits
possible isolated singularities away from C.

Now `n=C^2=d^2/a>0` is an integer, proving `a divides d^2`.
Cartier adjunction in the smooth neighborhood of C, together with
`omega_X=O_X(a-4)`, gives equation (G). The strict bound follows by
dividing it by d and retaining the positive summand d/a.
For rational C, this becomes

    (a-4)d=-n-2=-d^2/a-2.                     (A)

Thus a>=4 is impossible. For the three remaining positive carrier
degrees, equation (A) gives respectively

    a=1: (d-1)(d-2)=0;
    a=2: (d-2)^2=0;
    a=3: d^2-3d+6=0.

The last polynomial has negative discriminant, so has no real, hence
no positive integer, root. This proves the numerical list. These are
ordinary integer intersection calculations in every characteristic,
not equations reduced modulo the field characteristic. No Frobenius
or surface-resolution input is used.

For fixed C0, the corollary directly forces a genuine non-Cartier
singularity on every normal mate-admitting carrier, in every degree.
This conclusion does not require repeating the inherited all-quartic
proof. A nonnormal carrier may still have a Cartier lift upstairs while
C is non-Cartier downstairs; complete conductor descent remains the
obstruction in that case.

## 5. Review boundaries and continuation

The extension changes the support lane from smooth S to normal S with
Cartier c. It does not classify the non-Cartier singularities, bound their
Cartier indices, or force every presentation to have a degree-one
singleton lift. A finite inverse curve of degree greater than one, or
several inverse-image primes, requires its actual coefficient-vector
divisor relation.

The three fixed-C0 normalization targets have a primitive normalized
degree-one section Q with divisor 2c or 4c. The source's assertion that
normalized mates are scalar powers follows from the exact polarization
and the fact that two nonzero projective sections with the same divisor
differ by a global unit, hence a scalar. Whether any such power descends
through the full conductor is a separate question. This audit establishes
neither single-field residue bounds nor a uniform bound on split phase
orders for their actual four-coordinate projections.

No mathematical verifier was executed. The review consists of the new
local regularity, resolution/Leray and cone Picard arguments and the
displayed additional adjunction proof. The previously accepted smooth
proof and all-quartic result retain their original provenance. Neither a
universal STCI theorem nor an unrestricted counterexample is claimed.
