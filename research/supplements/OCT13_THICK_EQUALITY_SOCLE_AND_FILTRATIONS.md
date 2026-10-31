# Symbolic ribbons, valuation bounds and normalization controls

Complete source text preserved below, including explicit hypotheses, calculations, counterexamples and unresolved issues. Compilation is not independent correctness audit or theorem promotion.

---

<a id="source-2026-10-13-generalization-quintic-continuationmd"></a>

## Nonendpoint quintics: conductor root support instead of mate-degree searches

Date: 2026-10-13 continuation, written after midnight on October 14. Owner:
`quintic_continuation`. Status: **ZERO-CUBIC AND LAMBDA-ONE FAMILY EXCLUSIONS, THE MAIN
THREE-ROOT/FOURFOLD ALTERNATIVES, AND REGULAR SOLE-ROOT L1/L2 HAVE
PASSED INDEPENDENT AUDIT. THE FINAL MAIN 3+2 ORIGINAL-GENERATOR
WITNESS IS IN PROGRESS.** Accepted older
proofs are premises and were not replayed. The universal problem, higher
carriers, other quintic normalization genera and the full nonendpoint
common-root incidence remain unresolved.

### 1. Authoritative inherited scope

Use the accepted characteristic-zero degree-five genus-one A4 pair `(S,c)`
and actual nonendpoint projection with `delta!=0`, all four lift parameters,
center avoidance and finite birationality. The curve `c` maps isomorphically
to the fixed quartic C0. A mate of any positive degree forces the entire
inverse support `nu^{-1}(C0)_red=c` (SUP). The accepted full conductor is an
effective Cartier divisor on S in `|2H|`; its actual restriction to c is the
nonzero binary octic F, retaining all multiplicities and infinity roots.
The accepted support bridge is

    supp(F) subset supp(H P^epsilon),
    epsilon=1 if Jbar=0, and zero otherwise,

where H is the complete homogeneous gcd of the corrected conormal cubics
and P=0 is the intrinsic A4 target. This concerns the actual conductor
section; no upper contact bound is inferred from first-normal data.

The October 13 full cubic-pair audit accepts the entire residual surface
partition 3+3 as an all-mate exclusion, including doubled cubics. Its
stronger SUP exclusion is qualified to Jbar!=0; the Jbar=0 portion uses the
separate accepted all-power line argument. The residual surface partitions
2+4 and 2+2+2 are already excluded. Thus the surface residual is integral
in any remaining mate lane. The conductor quintic S below is a polynomial
factor of the restricted conductor octic; it is not that degree-six
residual surface divisor.

### 2. Complete h=3 parameters and the conductor factorization

The accepted homogeneous gcd classification says h=3 consists of the two
zero-cubic charts and the proportional main chart. On the main chart write
`J=lambda P`, with lambda nonzero. Its complete parameters are

    a=delta(delta+2lambda-1)/(6lambda^2),
    b=delta(delta+2lambda-1)/(3lambda),
    g=delta((lambda-3)delta+lambda+1)/3,
    d=delta((lambda^2-12)delta+lambda^2-2lambda+6)/6.

The accepted/new evening conductor coefficient artifacts give

    F = -delta^4 H3 S5/(1296lambda^6),

where H3,S5 are fixed-degree binary forms with affine coefficient lists in
`evening-h3-proportional/main-H-coefficients.txt` and
`main-S-coefficients.txt`. Their scalar is nonzero. In particular

    H3=(delta+2lambda-1)p^3
       +(3delta lambda-3delta-9lambda+3)p^2
       +(-3delta lambda^2-6delta lambda-3lambda^2+3delta+12lambda-3)p
       -delta lambda^3+3delta lambda^2-lambda^3+3delta lambda
          +5lambda^2-delta-5lambda+1.

Their original scaling is H3=-3lambda^2 H/delta and
S5=432lambda^4(F/H)/delta^3. Only the scalar being nonzero enters
the support argument.

The exact main Jbar and G factors are

    G=delta(lambda^2-4lambda+1)((lambda+1)delta+lambda-1)/(3lambda^2),
    Jbar=(lambda-1)G/2.

Hence all main Jbar=0 values outside lambda=1 have G=Jbar=0 and are already
excluded by the accepted all-power theorem. Lambda=1 is treated below.
Every other main support candidate has the actual open conditions

    delta lambda (lambda-1)(lambda^2-4lambda+1)
      ((lambda+1)delta+lambda-1) != 0.                 (A)

### 3. Both zero-cubic charts are excluded in every mate degree

Use the final evening standard-library certificate, without replaying it:
`validation/2026-10-13-h3-zero-chart-conductor-new/attempt-01-final/` and
`new-exact-support-incidence.json`. On zero-P, delta=-1, a=0, B=-2/3,G=0,
put j=Jbar. Up to nonzero scalar the complete conormal cubic is

    S3=p^3-6p^2+6p+3j.

The actual octic factors exactly as

    F=(2/9) S3 Q5,
    Q5=p^5+(j/3-13/2)p^4+(27/2)p^3
        +(-12-5j/2)p^2+(9/2-3j/2+j^2)p+9j-3j^2.

Both factors are monic, so neither has an infinity root. For j!=0 SUP
requires all Q5 roots to lie on S3. For j=0 the extra A4 point p=0 is
already a root of S3, so precisely the same necessary support condition
holds. It implies Q5 divides S3^5. Exact polynomial division gives five
remainder coefficients in Q[j]; the certificate records a literal Bezout
combination of the first two equal to 1. They have no common algebraic
zero. Thus no j satisfies SUP. The homogeneous coordinate transformation
`(P,Q,j)->(P,P-Q,-j)` takes this actual octic and conormal cubic to the
zero-J chart, retaining p=0 and target infinity. The certificate contains
both exact homogeneous transform identities. Thus the zero-J chart also
fails SUP in its entirety. No center minor is inverted.

This is a direct all-parameter consequence of the saved exact identities,
and it has passed the separate October 14 independent geometric audit.

### 4. The entire lambda=1 main boundary also fails SUP

On lambda=1, Jbar=0 and G=-4delta^2/3!=0. The conductor factors, up to its
nonzero scalar, as H3*p*Q4, where

    H3=(delta+1)p^3-6p^2+(6-6delta)p+4delta,
    Q4=(90delta^2-76delta-58)p^4
        +(-405delta^2+458delta+203)p^3
        +(675delta^2-858delta-261)p^2
        +(-450delta^2+800delta+174)p-400delta.

Since Q4(0)=-400delta!=0, the allowed additional A4 root p=0 does not
help Q4. When its leading coefficient is nonzero, SUP implies Q4 divides
H3^4. The saved compact evening remainder source records four numerator
polynomials of degree22 in delta and a literal Bezout product equal to 1;
its denominators have only `(45delta^2-38delta-29)^9` and constant factors.
They therefore give a complete contradiction on this chart.

At the leading drop `45delta^2-38delta-29=0`, the fixed-degree Q4 has an
infinity root. H3 has no infinity root there, since delta=-1 gives that
quadratic value54. The added A4 p=0 is finite. This also contradicts SUP.
Thus lambda=1 is entirely excluded, not just a rational sample or a
finite list of mate exponents. Evidence:
`evening-h3-proportional/probe_lambda1_compact.m2`, its passing attempt02,
`lambda1-compact-numerators.txt`, denominators and literal Bezout file.

### 5. A general root-support cover for the remaining main chart

The following elementary lemma replaces an unbounded exponent search.
Let H3,S5 be nonzero binary forms of degrees three and five, with
`supp(S5) subset supp(H3)`.

* If S5 has at least three distinct roots, then H3 has exactly three
  distinct roots, all occur in S5, and H3 divides S5.
* If S5 has at most two distinct roots, then either it has a root of
  multiplicity at least four, or its exact multiplicities are3+2.

Indeed the support inclusion bounds the number of S5 roots by three. In
the first case three roots force H3 to be squarefree and every root must
occur in S5. In the second, partitions of5 into at most two positive parts
are5,4+1,3+2. This lemma concerns the full actual polynomial, including
all nilpotent contact multiplicities. Its scope is independent of mate
degree and of the coefficients of the projection family.

Under (A), Jbar!=0, so SUP imposes this support inclusion. The infinity
chart cannot survive: if LC(S5)=0, the actual fixed-degree S5 has an
infinity root and SUP forces LC(H3)=delta+2lambda-1=0. Substituting
`delta=1-2lambda` gives the exact identity

    LC(S5)=-216lambda^4(2lambda-1)^3
           =216lambda^4 delta^3 != 0,

a contradiction. This new source has a successful captured run in
`generalization-quintic-h3/infinity-attempt-02`. Its first attempt had an
unneeded quotient-ring computation after the candidate ideal was already
unit; that tail interface failure is preserved.

If H3 has an infinity root while S5 has none, it has at most two finite
roots and cannot cover three distinct S5 roots. Otherwise its leading
coefficient is nonzero. The exact three coefficients of the pseudoremainder
of S5 by H3 are saved in `h-divides-s-remainder.txt`. Their common factor
lambda^2 is invertible on (A). For those original divided generators Ri,
put

    U=delta lambda (lambda-1)(lambda^2-4lambda+1)
      ((lambda+1)delta+lambda-1) LC(H3) LC(S5).

The new source constructs and verifies a literal polynomial identity

    sum_i Wi Ri = U^2.

The exact Wi are saved in `h-divides-s-witness.txt`. Thus the H3|S5 case
is empty on the declared chart. The first certificate attempt omitted
LC(S5), found no witness through exponent12 and failed its assertion;
the repaired declared-open witness has exponent2 and succeeds. No claim
is made about that omitted leading condition.

### 6. The high-multiplicity support incidence and current work

Write V for the product of the five nonconstant unit factors in (A).
For a finite root x of S5, put c_i=coefficient_(p^i) S5. A root of
multiplicity at least4 satisfies

    S5(x)=S5'(x)=S5''(x)=S5'''(x)=0.                 (B)

The new exact QQ ideal, saturated only by the units in (A) and c5,
returns the unit ideal. Its source, literal four input polynomials and
captured intermediate ideal are preserved in the new validation package.
The original-generator witness is now complete: for the literal four
generators M4 and the stated unit V*c5, the saved 22 MB vector W4
satisfies `M4 W4=(V*c5)^2`. The source asserts that exact product before
saving it; its completion marker and empty stderr are preserved. The
October 14 independent auditor accepts this arithmetic lineage without
re-expanding the same large product.

For the exact3+2 case choose x to be the triple root. Dividing by
`(p-x)^3` leaves

    c5 p^2+(c4+3x c5)p+(c3+3x c4+6x^2 c5).

Its discriminant is

    c4^2-4c3c5-6x c4c5-15x^2 c5^2.                 (C)

Thus all3+2 cases, including coalescence into a fifth root, lie in the
exact finite polynomial system S5(x)=S5'(x)=S5''(x)=0,(C)=0.
For SUP additionally H3(x)=H3(y)=0, where
`y=-(c4+3x c5)/(2c5)`. The second relation is imposed after multiplying
by `(2c5)^3`, so no undefined root or scalar is introduced. The stronger six-generator full-support incidence has completed with
saturated ideal1. The original six-generator witness is being extracted
in `support32-witness-attempt-01`; complete main-family closure is
withheld until its literal product and captured execution are available.
The earlier unrestricted multiplicity32 computation supplies no claim
and is not needed for this support cover.

The first direct H3^5 modulo S5 source produced exact large coefficients
but was interrupted during ideal processing. A later full Hermite-rank
approach was also interrupted in favor of this much smaller complete root-
multiplicity cover. Those sources, failed setup interfaces and outputs
remain recorded. Neither unfinished computation supplies a theorem.

### 7. Remaining nonendpoint lanes and next action

The companion new note `2026-10-13-generalization-quintic-l2.md` proves
an all-parameter exclusion of the regular sole homogeneous-root lane,
including L2, its discriminant-zero and coefficient-drop boundaries. Its
October 14 independent audit has accepted this explicitly scoped theorem. The quotient/conductor proof and all new
higher Taylor conditions are retained there; no accepted old check is
replayed.

Even if the complete h3 support cover closes, the following remain outside
it: homogeneous gcd degree2 with its full two-root or repeated-root support;
the gcd-degree-one singular target-fiber charts pZ=0 with their denominator-free original
fiber system; other Jbar=0 nonproportional families; actual conductor power
descent on surviving full-support parameters; all other quintic genera;
normal quintics, higher carriers and entirely thick presentations.

The continuation strategy is to exhaust complete support types for the
fixed-degree actual conductor section, then impose full conductor descent.
Its complexity depends on normalization geometry and conductor root
support, not on an unbounded list of mate degrees. A first-symbol root
alone is never treated as a bound on the full conductor multiplicity.


---

<a id="source-2026-10-13-generalization-ribbon-numerical-criterionmd"></a>

## A degree-free symbolic-ribbon and valuation criterion

Date: 2026-10-13. Author: `ribbon_general`, delegated by
`global_structure`. Status: **NEW WRITTEN PROOF / INDEPENDENT REVIEW
PENDING**, as a conditional general theorem. Accepted quartic computations are used as inputs, with no
reruns. This note does not claim a solution of either the fixed `C0`
question or the universal STCI question.

The accepted
[weighted-ribbon proof](GENUS_TWO_BISECTION_PROOF.md)
uses an actual Cartier double on the normalization of a quartic. The
construction below supplies a canonical *symbolic* double even when
`2c` is not Cartier. Its numerical degree is controlled by all symbolic
layers of any actual Cartier multiple. This separates the global
existence of the ribbon from the stronger assertion that its degree can
be read directly from a Cartier-double Euler sequence.

### 1. Hypotheses and notation

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

### 2. The symbolic double is always an entire ribbon

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

### 3. Multiplication defects and periodicity

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

### 4. The Euler polynomial gives a sharper first-layer bound

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

### 5. The ambient conormal lower bound

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

### 6. Balanced rational curves: a uniform theorem

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

### 7. A valuation extension for thick singleton carriers

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

### 8. Preserved limits and next structural use

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


---

<a id="source-2026-10-13-generalization-smooth-normalization-independent-auditmd"></a>

## Independent audit of the all-degree smooth-normalization classification

Date: 2026-10-14, America/New_York. Auditor: `frontier_reconcile`.
Status: **PASS FOR THE NEW THEOREM UNDER ITS EXPLICIT SINGLETON-LIFT AND
SMOOTH-NORMALIZATION HYPOTHESES**. This audit reviews the new derivation;
accepted quartic, conductor and fixed-C0 premises were not rerun. The theorem
does not imply that an arbitrary minimum carrier has these hypotheses.

Owner source read:
[degree-free carrier framework](FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md),
SHA-256 `38bff3c497b1c0f8310a623e36c0fd5d6ded0517fc6903115b4321f5672d5848`.
The acceptance here is for section 3 and the finite fixed-C0 classification
in section 4. The later power-compression consequences have their separate
new-theorem dependency and are not promoted by this audit.

### 1. The exact accepted theorem

Let `C subset P3` be a smooth rational curve of degree `d` over an
algebraically closed field of characteristic zero. Let `X` be an integral
degree-`a` hypersurface admitting an actual mate for C, with finite
normalization `nu:S->X`. Require:

    S smooth,
    (nu^-1(C))_red=c,
    nu|c:c->C an isomorphism.

Put `H=nu*O_X(1)`. Then `(S,c)` is a smooth surface of minimal degree
with c its complete hyperplane class. The possibilities are exactly:

| Surface and c | H | a |
|---|---|---|
| P2 and a line | `d h` | `d^2` |
| P2 and a smooth conic | `(d/2) h`, requiring d even | `d^2/4` |
| Smooth rational normal scroll of degree n>=2 | `(d/n)c`, requiring n to divide d | `d^2/n` |

The scroll can be written `F_e`, `c=E+t f`, with `E^2=-e`,
`t>e>=0` and `n=2t-e`. These are finitely many normalization/polarization
types for a fixed d. The conclusion is necessary; it neither constructs
the four-coordinate projection nor proves support or conductor descent.

### 2. Independent reconstruction of the proof

The pullback of a degree-b mate is a nonzero section of `O_S(bH)`.
Its complete zero support is c by the stated singleton inverse-image
condition. On the smooth surface its actual divisor is `m c` for a
positive integer m. Since H.c=d and H^2=a, intersecting yields

    m d=a b,
    c_num=(d/a)H,
    n=c^2=d^2/a.

There is no hypothesis that the downstairs C is Cartier on X. Smoothness
of S makes c Cartier upstairs, so n is an integer. It is positive and
c is ample by numerical equivalence with the positive multiple of ample
H. This is the first place the smooth-normalization hypothesis is essential.

Adjunction on the smooth rational c gives `K_S.c=-n-2`. Thus `K_S.H<0`.
An effective positive canonical multiple would have nonnegative
intersection with ample H, so no such multiple is effective. The standard
characteristic-zero surface classification used in the accepted repository
arguments therefore makes S rational or birationally ruled over a
positive-genus curve.

The second alternative is impossible. A smooth ruled minimal model over
the positive-genus base is reached by point contractions, and the ruling
pulls back to a morphism on S. The rational c maps constantly to the base.
Write the fiber containing it as `F=m0*c+sum mi*Di`. Then

    0=F.c=m0*c^2+sum mi*(Di.c).

Every other component has nonnegative intersection with c on the smooth
surface, and m0 is positive. This contradicts c^2>0, including a reducible
or nonreduced fiber. Hence S is rational and `H1(S,O_S)=0`.

Now use the actual Cartier-curve sequence

    0 -> O_S -> O_S(c) -> O_c(c)=O_P1(n) -> 0.

It yields `h0(O_S(c))=n+2` and surjectivity onto all n+1 sections on c.
The canonical section of O_S(c) is nonzero at each point outside c.
At each point of c, some lifted section is nonzero because O_P1(n)
is globally generated. Consequently the complete system |c| is basepoint
free everywhere, not only generically.

Its morphism `phi:S->P^(n+1)` is finite: a positive-dimensional fiber
would contain a curve D with `c.D=0`, contradicting ampleness. The image
Y is an integral nondegenerate surface. Nondegeneracy follows from using
a basis of the complete linear system. If e is the generic map degree,
the intersection-degree formula and the minimal-degree inequality give

    n=c^2=e*deg(Y),
    deg(Y)>=codim(Y)+1=(n+1-2)+1=n.

Thus e=1 and deg(Y)=n. This includes n=1: then the map is finite
birational onto P2; no scroll-only assumption loses that case.

The degree inequality and Del Pezzo--Bertini classification were inspected
in the primary author source [Eisenbud--Green--Hulek--Popescu, *Small Schemes
and Varieties of Minimal Degree*, introduction](https://arxiv.org/html/math/0404517v5).
For integral surfaces, its list is a plane, an integral quadric/rational
normal scroll, or a Veronese surface. These standard surfaces are normal,
including the singular rational normal cones. Therefore the finite
birational map to Y is an isomorphism: on affine opens, the finite integral
algebra inside the common function field equals the integrally closed
target ring. Smoothness of S eliminates singular cones. The complete
polarized classification follows.

On each resulting rational surface numerical equivalence and linear
equivalence agree. For `P2`, c is h or 2h, so H is respectively d h or
(d/2)h; the latter requires d even. On a scroll `Pic(F_e)=ZE+Zf` and
c has E coefficient one. Therefore the rational equality
`H=(d/n)c` forces `d/n` to be an integer. Squaring gives the carrier
degrees in the table. The necessary divisibility n|d gives a uniform
finite list of smooth normalization types at once, rather than a separate
degree-pair search.

### 3. Every fixed-C0 case in the finite list

For d=4, the line model gives a=16. The conic model gives a=4. Smooth
scroll degree n must divide four and satisfy n>=2, so n=2 or n=4:

* n=2 gives a=8. In `n=2t-e` with `t>e>=0`, the only possibility is
  `e=0,t=1`, hence `S=P1xP1`, `c=(1,1)`, `H=(2,2)`.
* n=4 gives a=4. The scroll models are `e=0,t=2` or `e=2,t=3`;
  together with the plane conic, these fall in the already accepted
  all-integral-quartic exclusion. No new check of that theorem is needed.

Thus the only remaining smooth-normalization singleton-lift candidates
for the literal fixed C0 are

    a=8:  (S,c,H)=(P1xP1,(1,1),(2,2)),
    a=16: (S,c,H)=(P2,line,4h).

Their sectional genera are one and three, obtained directly by adjunction
on H. Their complete H systems have dimensions nine and fifteen.
Those dimensions describe parameter spaces for projections, not an
exhaustion of projection centers. Actual finite birational projection,
the prescribed deleted-middle-monomial restriction to c, full inverse
support and every conductor layer remain active conditions.

### 4. Scope audit and retained limitations

The proof needs neither generic regularity of X along C nor a smooth
mate once the full singleton isomorphic lift is explicitly assumed.
Conversely, the theorem does not provide that lift for a general
generically nonregular carrier. Several primes above C and degree-greater-
than-one lifts have a coefficient-vector divisor relation and are outside
this scalar argument.

A singular normalization cannot simply be substituted into the audited
proof. There c may not be Cartier, its self-intersection may be rational,
and the Cartier-curve exact sequence can fail. A proposed extension to
normal S with smooth Cartier c would be a new theorem requiring its own
precise statement, cone/Picard analysis and review. It is not implicitly
accepted here.

The global existence of high-degree smooth surfaces through C does not
yield mates on those surfaces. Nor does choosing a minimum mate-admitting
carrier force smooth normalization. Entirely thick pairs can remain
singular under `G+F*T`. The remaining normalization and filtered-algebra
branches cannot be discarded by this result.

For the two fixed-C0 models, `H=2c` or `H=4c` supplies a primitive
normalized degree-one section, but an upstairs section is still not an
ambient mate. The separate conductor-power theorem may compress it
under its single-field/unit hypotheses. This audit accepts neither a
geometric residue-degree bound for every projection nor the exclusion of
split conductor phases. No unconditional degree-eight or degree-sixteen
carrier exclusion follows.

### 5. Optional proof simplification, not needed for acceptance

One can obtain `H1(O_S)=0` before surface classification. Every morphism
from the rational c to an abelian variety is constant. If the Albanese
morphism of S had positive-dimensional image, pulling back a suitable
ample divisor on that image would give a nonzero effective divisor D
with `c.D=0`, since c is contracted. Ampleness of c contradicts this.
Thus the Albanese variety is trivial; in characteristic zero this gives
`H1(O_S)=0`. The complete-|c| proof then establishes rationality from
the minimal-degree classification itself.

This alternative explains the same geometric rigidity: an ample rational
curve forbids irregularity. It is supplied as an optional simplification;
the audited owner proof already establishes the necessary vanishing by
the standard surface-classification route.

### 6. Evidence and review boundaries

This is a written independent mathematical reconstruction, including
ampleness, reducible fiber signs, n=1 and n=2 cases, finite-map degree,
normality/isomorphism, all Picard divisibilities and the complete fixed-C0
list. There was no symbolic execution and no inherited verifier rerun.
The live primary check was restricted to the new minimal-degree interface.
Parallel agreement is not used as a proof: the argument above supplies the
reviewed implications.

The all-quartic theorem and the normal-bundle/conductor results retain
their earlier audit provenance. No novelty or universal resolution is
claimed. The mathematical advance accepted here is a finite
normalization-type classification for an entire explicitly stated rational
support lane across all carrier and mate degrees.


---
