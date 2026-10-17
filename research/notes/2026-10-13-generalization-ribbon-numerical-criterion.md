# A degree-free symbolic-ribbon and valuation criterion

Date: 2026-10-13. Author: `ribbon_general`, delegated by
`global_structure`. Status: **NEW WRITTEN PROOF / INDEPENDENT REVIEW
PENDING**, as a conditional general theorem. Accepted quartic computations are used as inputs, with no
reruns. This note does not claim a solution of either the fixed `C0`
question or the universal STCI question.

The accepted
[weighted-ribbon proof](2026-10-10-session-weighted-ribbon-conormal-independent-audit.md)
uses an actual Cartier double on the normalization of a quartic. The
construction below supplies a canonical *symbolic* double even when
`2c` is not Cartier. Its numerical degree is controlled by all symbolic
layers of any actual Cartier multiple. This separates the global
existence of the ribbon from the stronger assertion that its degree can
be read directly from a Cartier-double Euler sequence.

## 1. Hypotheses and notation

Let `k` be an algebraically closed field of arbitrary characteristic.
Let `C subset P3` be a smooth integral projective curve of degree `d`
and genus `g`. Let `S` be a normal integral projective surface with a
finite birational morphism `f` onto an integral surface in `P3`, as
for a normalization of a carrier. Let `c subset S` be a reduced prime curve such
that `f|c:c->C` is an isomorphism. Set

    H=f*O_P3(1),   a=H^2>0,   H.c=d.

Assume there is an actual effective Cartier relation

    r c ~ b H,   r,b positive integers.

Here `r c` means the divisor with that Weil divisor and its divisorial
ideal; the assumption includes Cartierness and actual linear
equivalence. It is stronger than a numerical equivalence. Intersecting
with `H` gives

    r d = b a.

A normalization of an integral carrier with a mate supported exactly
over `C` supplies this relation when there is exactly one inverse prime
and it maps birationally to `C`. Because the normalization is finite,
the latter prime then maps isomorphically to the normal curve `C`.
The absence of extra inverse points is an upstream support condition,
not a conclusion of the present proof.

Let `pi` be the arithmetic genus of a general effective Cartier
member of `|H|`. In the characteristic-zero carrier applications this
is the genus of the smooth general pulled-back hyperplane. Define

    kappa = K_S.H = 2 pi - 2 - a.

No Gorenstein assumption on `S` is needed. The intersection `K_S.H`
is defined using the Cartier divisor `H`; alternatively the right side
can be taken as the definition of `kappa`. The general member avoids
the isolated singularities of the normal surface. Using arithmetic
genus here avoids imposing a positive-characteristic smoothness
assertion on the pulled-back hyperplane linear system.

For each `i>=0` define the reflexive divisorial ideal and its layer

    I_i = O_S(-i c),    E_i = I_i/I_(i+1).

Thus `I_0=O_S` and `E_0=O_c`. Write `ell=deg E_1`.

## 2. The symbolic double is always an entire ribbon

**Lemma.** Under the normality and smoothness hypotheses above,

    R_2 = Spec_S(O_S/I_2)

is a Cohen--Macaulay ribbon on the entire smooth curve `c`, including
every singular point of `S`. Its nilideal is the line bundle `E_1`.
More generally, every `E_i` is a line bundle on `c`.

**Proof.** A divisorial rank-one reflexive sheaf on a normal surface
has depth two at each closed point. The exact sequences

    0 -> I_j -> O_S -> O_S/I_j -> 0,
    0 -> I_(i+1) -> I_i -> E_i -> 0

and the depth lemma therefore give depth at least one to the two
quotients at closed points of their one-dimensional support. Thus
they have no finite-length torsion.

Normality identifies `I_1` with the ideal of the reduced curve `c`:
locally, functions in this ideal are exactly regular functions having
positive valuation at the height-one prime of `c`. Divisorial
valuation inequalities also give

    I_i I_j subset I_(i+j).

In particular `I_1` annihilates `E_i`, so `E_i` is a coherent
`O_c`-module. At the generic point of `c`, the local surface ring is a
DVR; `E_i` has rank one over its residue field. The depth statement
shows it is torsion-free on `c`. A torsion-free rank-one coherent
sheaf on a smooth curve is a line bundle.

The radical of `I_2` is `I_1`, and `I_1^2 subset I_2`. Hence the
nilideal of `O_S/I_2` is exactly `E_1`, its square is zero, and

    0 -> E_1 -> O_R2 -> O_c -> 0

is the ribbon sequence. This proof requires neither `2c` Cartier nor
`S` Gorenstein. QED.

Ordinary ideal squares and ordinary nilradical powers must not replace
the divisorial ideals in this lemma. Their quotients can acquire
finite-support torsion; the reflexive/symbolic construction is what
proves the asserted global Cohen--Macaulay and line-bundle properties.

## 3. Multiplication defects and periodicity

Multiplication induces nonzero, hence injective, maps of line bundles

    E_i tensor E_j -> E_(i+j).

They are isomorphisms at the generic point of `c`. Consequently there
are effective divisors `D_i` on `c` with

    E_i = E_1^i(D_i),    D_0=D_1=0,
    D_i+D_j <= D_(i+j).

All divisor inequalities are coefficientwise. This is symbolic
filtration data, not a proof of primitivity or a determination of
higher normal jets.

Since `r c` is Cartier, the divisorial ideals have actual periodicity

    I_(i+r)=I_i tensor O_S(-r c),
    E_(i+r)=E_i tensor O_c(-bH).

In particular

    E_r=O_c(-bH),    deg E_r=-b d=-r d^2/a.

Applying multiplication to `E_1^r -> E_r` yields the first bound

    ell <= -d^2/a.                                      (1)

More generally, for every positive integer `j`, choose a positive
integer `n` with `r | n j`. The multiplication map
`E_j^n -> E_(nj)`, together with periodicity, gives

    deg E_j <= -j d^2/a.                                (2)

These are inequalities of rational numbers; the left sides are
integers. They do not require generic immersion into `P3`.

## 4. The Euler polynomial gives a sharper first-layer bound

For a normal surface in the carrier setting,

    chi(O_S(mH)) = (a/2)m^2 - (kappa/2)m + chi(O_S).

One can obtain this formula without using a singular-surface
Riemann--Roch correction theorem. The hyperplane exact sequence and
the degree/Euler formula for line bundles on the general Cartier
hyperplane curve give, for every integer
`m`,

    chi(O_S(mH))-chi(O_S((m-1)H)) = ma+1-pi.

The stated polynomial is the unique solution with its given value at
`m=0`.

Set `R_r=Spec_S(O_S/I_r)`. Since `I_r=O_S(-bH)`, its Euler sequence
gives

    chi(O_Rr) = chi(O_S)-chi(O_S(-bH))
               = -(a b^2+b kappa)/2.

Thus the constant `chi(O_S)` cancels. Rationality of the surface, a
prescribed value of its Euler characteristic, and invertibility of
its dualizing sheaf are unnecessary for this numerical step.

Its symbolic filtration has successive quotients `E_0,...,E_(r-1)`.
Riemann--Roch on `c` therefore gives the exact identity

    sum_(i=0)^(r-1) deg E_i
       = -(a b^2+b kappa)/2 - r(1-g).                    (3)

Using `deg E_i >= i ell`, for `r>=2` we obtain

    ell <= -[a b^2+b kappa+2r(1-g)]/[r(r-1)]
         = -[r d^2/a+d kappa/a+2(1-g)]/(r-1).            (4)

Equivalently,

    r(r-1)ell + 2 sum_i deg D_i
       = -a b^2-b kappa-2r(1-g).

When `r=2`, there are only `E_0` and `E_1`, so (4) is an equality:

    ell = -(a b^2+b kappa)/2 - 2(1-g).                  (5)

For `r>2`, (4) need not be an equality. The total Euler characteristic
does not determine the double-ribbon degree without controlling the
multiplication defects. This is precisely where copying a quartic
Cartier-double calculation to an arbitrary Cartier multiple would
lose information.

## 5. The ambient conormal lower bound

Assume first that `f` is an immersion at the generic point of the
symbolic ribbon `R_2`. A sufficient carrier condition is that the
normalization is an isomorphism at the generic point of `C` and the
carrier is regular there. Pullback of the ambient ideal induces

    N_C/P3^* = I_C/I_C^2 -> E_1.

It is generically nonzero: in the sufficient carrier condition it is
even generically surjective, since the ambient ideal generates the
curve ideal in the DVR of the regular carrier. Global immersion of
`R_2`, including along the conductor, is not required.

Let `M` be any upper bound on the degree of a line subbundle of
`N_C/P3`. A nonzero map `N_C^* -> E_1` dualizes to a generically
injective map `E_1^(-1) -> N_C`. Saturation can only increase the
degree of its image, so

    ell >= -M.                                        (6)

For `C=P1` and

    N_C/P3 = O(u) direct_sum O(v),

one can take the exact bound `M=max(u,v)`. For a semistable normal
bundle on a curve of genus `g`, one can take
`M=deg(N_C)/2=2d+g-1`; this bound does not assert semistability.

Combining (1), (4), and (6) gives the degree-free necessary conditions

    d^2 <= a M,

    a b^2+b kappa+2r(1-g) <= r(r-1)M,                  (7)

or, after eliminating `b`,

    r[d^2-aM]+d kappa+a[2(1-g)+M] <= 0.                (8)

Violation of either condition excludes a mate satisfying the stated
normalization, support, and generic-immersion hypotheses.

## 6. Balanced rational curves: a uniform theorem

Suppose `C=P1` and its accepted or separately established normal
splitting is balanced:

    N_C/P3=O(2d-1)^2.

Then every relation above with generic immersion satisfies

    d^2 <= a(2d-1),

    r[d^2-a(2d-1)]+2d(pi-1)+a(d+1) <= 0.              (9)

For equal curve and carrier degrees, `a=d` and `b=r`. Condition (9)
simplifies to

    2 pi <= (r-1)(d-1).                               (10)

In particular, an actual Cartier double `2c~2H` has

    E_1=O_P1(-d-2pi),

and is incompatible with the embedding whenever `2pi>d-1`. This is
a single theorem for every degree `d`, rather than a list of degree
pairs. The accepted quartic bisection input has `d=a=4`, `r=b=2`,
`pi=2`; the theorem gives `E_1=O(-8)` and contradicts the accepted
`N_C0=O(7)^2`. No part of that accepted calculation was rerun here.

For comparison, the accepted quintic genus-one normalization has
`a=5,d=4,r=5,b=4,pi=1`. Bound (4) gives `ell<=-7/2`, hence
`ell<=-4`, while the conormal lower bound is `ell>=-7`. Thus this
general theorem alone does not exclude that remaining quintic lane.
The existence of its symbolic double is proved, but its degree is
not forced to be the prohibited quartic degree `-8`.

## 7. A valuation extension for thick singleton carriers

Generic immersion is exactly the assertion that the first ambient
normal direction survives on `R_2`. There is a useful weaker
version when that direction is killed.

Let `q>=1` be the minimum valuation at the generic point of `c` of
the pulled-back ambient ideal `I_C`. Assume `f|c` remains the given
isomorphism. The pulled-back ideal is globally contained in `I_q`
by the defining divisorial valuation condition. Its square is
contained in `I_(2q) subset I_(q+1)`. Since `I_1` annihilates `E_q`,
pullback therefore defines a global map

    N_C/P3^* -> E_q.

This map is generically nonzero by the definition of `q`. Saturating
its dual gives `deg E_q>=-M`, while (2) gives
`deg E_q<=-q d^2/a`. Hence

    q d^2 <= a M.                                    (11)

For balanced rational curves this is

    q d^2 <= a(2d-1).

It applies to thick singleton normalizations without asserting a
nonzero first-ribbon conormal map. In that setting the Euler
first-layer bound (4) still holds algebraically, but cannot be
combined with (6) unless `q=1`. Multiple inverse branches, inverse
curves mapping with degree greater than one, and non-smooth inverse
curves require a different formulation and are outside this theorem.
Condition (11) is necessary under the stated hypotheses; it does not
prove either singleton inverse support or the isomorphism `c~=C`.

## 8. Preserved limits and next structural use

The symbolic-ribbon construction removes the need for an actual
Cartier double. It does not create a Cartier relation that was not
already supplied by a mate, nor determine its least possible index.
Replacing `(r,b)` by `(nr,nb)` is always permitted and preserves the
relation, but need not preserve sharpness of the Euler bound. More
precisely, put `A=d^2/a` and `B0=d kappa/a+2(1-g)`. The right side
of (4) is `-A-(A+B0)/(r-1)`, so increasing `r` weakens that bound
when `A+B0>=0` and strengthens it when `A+B0<0`. For `a=d`,
`A+B0=2(pi-g)`. In the weakening case one should use the smallest
available actual relation, not infer a new small-index relation.

The most useful structural continuation is to prove a uniform
upper bound on the relevant Cartier index or to control the
effective multiplication defects `D_i` by surface singularities and
conductor descent. That would strengthen (4) without restarting a
degree-pair enumeration. The inequalities themselves do not exclude
all large carrier degrees, and there is no unrestricted non-STCI
conclusion here.
