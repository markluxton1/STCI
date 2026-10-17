# Full filtered compatibility with local Cartier indices

Date: 2026-10-14. Author: `socle_audit`, including an independent
reconstruction of the root's new Jacobian/index argument.
Status: **PROVED NEW STRUCTURAL THEOREMS AND ALL-DEGREE EXCLUSION FOR
NORMAL C0 CARRIERS WITH ACTUAL ON-CURVE LOCAL INDICES AT MOST FOUR.**
Accepted inputs are the normal-carrier torsion/index reduction in
`2026-10-14-generalization-normal-carrier-torsion.md`, the full socle
duality/budget, the splitting N_C0^* = O(-7)^2, the exclusion of integral
carriers of degree at most four, and P-010's nonzero quadratic obstruction
for every constant first direction. Those inputs were not reverified.
Only the new filtered/index compatibility and its consequences are
proved and audited here. No canonical-state file is edited.

## 1. Ordinary free layers are powers, even in the presence of torsion

Let Y be a complete-intersection thickening of a smooth integral curve C,
whose generic transverse algebra is curvilinear of length n >= 2. Put

    J = I_C O_Y,
    L_i = J^i/J^(i+1),
    T_i = torsion(L_i),
    B_i = L_i/T_i,
    B = B_1.

Purity gives J^n = 0 everywhere. Every B_i for 0 <= i < n is a line
bundle. The direct sum of the T_i is a graded ideal: the product of a
torsion section with any normal-layer section is torsion. The ordinary
associated graded algebra is generated in degree one, hence so is its
torsion-free graded quotient. Therefore multiplication surjects

    B^i -> B_i.

A surjection between line bundles is an isomorphism. This proves

    B_i = B^i,  including J^(n-1) = B^(n-1).    (1)

This concerns the ordinary J-adic filtration. A saturated BF filtration
is a different filtration and may have nonzero multiplication divisors.
There is no conflict with earlier BF defect calculations.

Write deg B = -ell and J^(n-1) = Soc(Y)(-D), with D effective. The
accepted actual socle line gives

    deg D = (n-1)ell + (2g-2) + e(4-a-b),      (2)

where e = deg C and a,b are the defining hypersurface degrees. The
ordinary Euler-characteristic budget, together with (1), yields

    2 sum_i length T_i = n deg D.              (3)

No primitive hypothesis on Y, torsion-free layer hypothesis, or global
retraction to C is used.

## 2. The Frobenius identity is pointwise

Complete at P in C and choose a lift t of its curve parameter. The
local algebra A of Y is finite free of rank n over R = k[[t]]. Indeed
normal variables are nilpotent, and Cohen--Macaulay purity makes t a
nonzerodivisor. It is a relative complete intersection, so A^vee =
Hom_R(A,R) is free rank one as an A-module.

Choose z in J whose first symbol generates B locally. Its powers
generate each B_i by (1). Thus

    A_0 = R[z]/(z^n) subset A

is a full lattice. Its induced J-filtration is strict: the least
nonzero z-power in a polynomial has nonzero image in the corresponding
free normal layer. Comparing its graded pieces with L_i gives

    length_R(A/A_0) = sum_i length_R(T_i)_P.    (4)

Choose an A-module generator lambda of A^vee. The multiplication
pairing lambda(xy) is perfect over R. Finite duality identifies the
actual socle Ann_A(J) with R via lambda: explicitly,

    Hom_A(R,A^vee) = Hom_R(R,R) = R.

If s generates the socle, lambda(s) is a unit. Write
z^(n-1) = t^(D_P) u s, u a unit. The Gram matrix on
1,z,...,z^(n-1) is anti-triangular and has determinant a unit times
lambda(z^(n-1))^n. Its valuation is n D_P. The perfect Gram determinant
on an R-basis of A is a unit; passage to a full sublattice doubles its
index in the determinant. Therefore (4) proves the stronger identity

    2 sum_i length_R(T_i)_P = n D_P.           (5)

The independent reconstruction checks both the strict filtration and
the socle identification; no trace pairing on a nonreduced algebra is
mistaken for a perfect pairing.

## 3. The local normal-index theorem

Work in the complete regular ambient ring

    T = k[[t,x,y]],  I = (x,y),
    S = T/(F),

where S is a normal surface domain and C is the smooth curve defined
by I. Suppose a mate has divisor n C on S. Let r be the actual local
Cartier index of C, so r divides n, and put k = n/r. Choose h in S with
div(h) = r C; normality makes such a rational principal representative
regular. The mate is u h^k for a unit u in S. Units do not change its
ideal, so the two relevant local complete intersections are

    W_r = S/(h),  W_n = S/(h^k).

Let A_F,P denote the vanishing order on C of the carrier's first normal
symbol after saturating its rank-one direction. In local normal
coordinates one may write

    F_1 = t^(A_F,P) u_0 y,  u_0 a unit,         (6)

with z = x generating the free first normal quotient. For r >= 2,
W_r and W_n have the same free first-normal quotient: their generic
kernel is the direction of F_1, and taking the torsion-free quotient
saturates that same rank-one direction. Thus this z works for both.

Let D_r,P and D_n,P be their actual top-power/socle defects. The exact
compatibility theorem is

    D_n,P = (k-1) A_F,P + k D_r,P.             (7)

Its proof retains the full embedded algebra, not only the tangent cone.

### 3.1 Normality gives the colon comparison

For the ideal I in S,

    (h^k : I) = h^(k-1)(h : I).               (8)

To check the nontrivial inclusion, if c I is contained in (h^k), choose
a normal parameter z whose valuation at C is one. Then val_C(c) >=
kr-1. The rational function c/h^(k-1) has C-valuation at least r-1,
and nonnegative valuation at every other height-one prime, because
h has divisor only r C. It is regular by normality. Dividing the
containment by h^(k-1) gives its membership in (h:I).

Modulo h^k, (8) gives the isomorphism of actual socle lines

    Soc(W_n) = h^(k-1) Soc(W_r).              (9)

Also

    w = z^r/h in Frac(S)

is regular: z has C-valuation one, and the divisor of z has only
nonnegative coefficients at other primes. Its restriction to C is
generically nonzero. Writing v = ord_C,P(w), one obtains from
z^(n-1) = h^(k-1) w^(k-1) z^(r-1) and (9)

    D_n,P = D_r,P + (k-1)v.                   (10)

### 3.2 The relative Jacobian is an actual socle generator

The key standard input is the formal Artinian CI Jacobian theorem:
over a field of characteristic zero, the determinant of the defining
Jacobian generates the socle. A primary formulation, valid more
generally when the characteristic does not divide the length, is
Eisenbud--Ulrich, *Duality and socle generators for residual
intersections*, [Theorem 8.5, PDF pages 50--51](https://arxiv.org/pdf/1309.2050).
This applies to nonhomogeneous formal CI equations, not just graded
ones.

Here W_r is finite free of rank r over R: its generic transverse length
is r and it is a pure one-dimensional CI. Let

    j_r = det(partial(F,h)/partial(z,y)).

Generically j_r belongs to the socle by the standard theorem; purity
therefore shows j_r I = 0 globally. Its reduction modulo t is the
Jacobian of the length-r Artinian CI fiber, and generates that fiber's
socle in characteristic zero.

The actual socle is base-change-compatible in this situation. An
A-module generator of Hom_R(A,R) identifies Hom_A(R,A) with R;
after reduction modulo t it identifies the reduced line with
Hom_(A/tA)(k,A/tA), since the augmentation dual is the socle of the
dual algebra. Consequently j_r generates the actual R-socle by
Nakayama. This is the needed global-over-R justification; being a
generic socle generator alone would not suffice.

### 3.3 Differentiation identifies the extra defect

In S the exact identity z^r = h w holds. Lift it to T, differentiate
with respect to z,y, wedge with dF, and reduce modulo (F,h). The term
h dw vanishes, and terms from the lifted multiple of F disappear.
One obtains in the actual socle of W_r

    w j_r = r z^(r-1) det(partial(F,z)/partial(z,y)).

The top power z^(r-1) is annihilated by I. Thus the last factor reduces
to its restriction on C, which is a unit times t^(A_F,P) by (6).
Since j_r generates the socle and z^(r-1) generates its top-power
subline, this proves

    ord_C,P(w) = A_F,P + D_r,P.                (11)

Combining (10) and (11) proves (7).

If r=1, then C is Cartier on the normal hypersurface and is smooth.
The hypersurface is smooth at P: a principal quotient by C is a regular
one-dimensional local ring, so the ambient surface has embedding
dimension at most two and is regular. Thus A_F,P = D_r,P = 0, and
(7) remains valid with the evident conventions.

The class index r does not bound A_F,P or D_r,P. For example index-four
D_n singularities may have large higher corrections. Formula (7)
charges those corrections rather than suppressing them.

## 4. A pointwise index bound gives a linear carrier-degree bound

For C0 let F have degree a, let the mate have degree b, and put
n = ab/4. A normal carrier makes the generic CI algebra curvilinear.
The ordinary first free layer is O(-ell), with ell <= 7. Equations
(1)--(2) give

    deg D = (n-1)ell - 4(a+b) + 14,
    deg A_F = 4a - 14 + ell,
    deg D + deg A_F = n(ell-16/a).             (12)

Let s be an upper bound on the actual local Cartier indices of C0
at points on F. Since k = n/r >= n/s, summing (7) gives

    deg D >= (n/s-1) deg A_F,
    s(ell-16/a) >= 4a-14+ell.                  (13)

For a >= 5, the right side is positive under a hypothetical mate;
therefore ell-16/a > 0. The ratio

    (4a-14+ell)/(ell-16/a)

decreases in ell because its derivative has numerator
14-4a-16/a < 0. Using ell <= 7 in (13) yields the uniform bound

    s >= (4a-7)/(7-16/a),
    4a^2-(7s+7)a+16s <= 0.                    (14)

Thus a pointwise bound on actual curve indices bounds carrier degree
linearly; it is stronger than merely bounding the least common multiple
of many indices and using a | 16R. It imposes no bound on the number of
singular points or their D_n higher-jet complexity.

For s <= 4, (14) forces integer a <= 6. Accepted low-degree exclusions
leave only a=5,6. The actual indices divide12, hence the accepted
Cartier integrality gives a | 192 and eliminates a=5. The accepted
index/torsion theorem then gives the minimal degree pair (a,b)=(6,8),
with R=12 and n=12. Equivalently one can use the accepted index12
reduction first and apply the sharper local formula below.

For a smooth rational degree-e curve with balanced normal bundle
O(2e-1)^2, put lambda = 2e-1. The same proof gives

    deg A_F = ea-2lambda+ell,
    deg D + deg A_F = n(ell-e^2/a),
    s >= (ea-lambda)/(lambda-e^2/a),           (15)

when deg A_F > 0 and the denominator is positive. These conditions are
forced by the preceding inequality for a genuinely non-Cartier carrier
point. The ratio decreases in ell when
ea+e^2/a >= 2lambda; this holds for integer e,a in the balanced rational
setting (strictly for e>=3 by AM--GM). Degenerate smooth line cases
with zero numerator and denominator are outside the non-Cartier
application. The characteristic-zero Jacobian hypothesis remains in
force.

## 5. Closing the entire actual-index-at-most-four class

Apply the accepted index12 reduction: a minimal mate yields the same
unordered pair (6,8), length12. The other defining surface is not
assumed normal. The four initially possible first-layer slopes are

    ell = 4,5,6,7,
    deg D = 2,13,24,35.

At every point with local index at most four, k = 12/r >= 3. Formula
(7) gives D_P >= 2 A_F,P. For a normal octic,

    deg D - 2 deg A_F = 9ell-78 < 0

for every ell <= 7. Hence the normal octic carrier is impossible.

For a normal sextic,

    deg D - 2 deg A_F = 9ell-62.

Effectivity forces ell=7, deg D=35, deg A_F=17, with total slack one.
Pointwise the exact slack is

    D_P - 2 A_F,P = (k-3)A_F,P + k D_r,P.      (16)

An index-two point has k=6 and A_F,P >= 1, costing at least three; it
is impossible. An index-three point has k=4 and costs
A_F,P+4D_r,P. An index-four point has k=3 and costs 3D_r,P.
Since R=12 requires an index-three and an index-four contribution,
the total slack one forces

    D_r,P = 0 at every index-three/four point,
    sum_(r=3) A_F,P = 1,
    no index-two points.                      (17)

In particular there is exactly one index-three point with first-symbol
vanishing order one. Simultaneous index-four points are all retained;
their total first-symbol vanishing order is sixteen. No classification
or independent bound on their higher local jets has been used.

## 6. Primitive symbolic triple contradiction

For each index-three/four point, (5) applied to W_r and (17) give zero
ordinary layer torsion. The R[z]/(z^r) lattice is therefore the entire
algebra:

    W_r = R[z]/(z^r).

For j <= r, the image of the symbolic ideal I_(C/X)^(j) is (z^j) in
this algebra. To check this without assuming a primitive hypothesis,
the two ideals agree after inverting t by their C-valuations. The
quotient R[z]/(z^j) is R-torsion-free, so the ordinary ideal (z^j) is
already saturated and equality descends. Consequently the symbolic
triple is locally R[z]/(z^3) at every index-three/four point.

At all remaining points the curve has index one, and the carrier is
smooth by the argument in Section 3; its symbolic triple is likewise
primitive. Thus the global symbolic triple defined by O_X(-3C) is an
embedded primitive triple everywhere along C0. This is a conclusion
from the full filtered compatibility, not an imposed primitive-pair
assumption.

Its free first conormal quotient is the same saturated carrier
direction as B_1 of the length-twelve thickening, namely O(-7).
The map O(-7)^2 -> O(-7) has constant coefficients on P1, so its first
initial relation is a fixed linear form m. Primitivity makes the next
relation space exactly mV. The accepted P-010 quadratic obstruction
for this constant embedded primitive triple is nonzero in every
direction. This is a contradiction.

Therefore:

**No normal integral carrier of C0 in characteristic zero can admit a
mate if every actual local Cartier index of C0 at points of that carrier
is at most four. This is an all-carrier-degree and all-mate-degree
exclusion.**

It includes arbitrary simultaneous D/E rational-double-point
singularities and A1,A2,A3 mixtures along C0, using the accepted class
index bounds. Singularities away from C0 are irrelevant. No normality
of the other defining hypersurface, primitive initial presentation, or
D_n complexity bound is required.

## 7. What survives

The complete class with indices dividing12 still permits actual
index-six or index-twelve points. Those points have k=2 or k=1 in
the length-twelve formula and are not closed by Section 5. In
particular an index-twelve point can support a pole in the first-symbol
ratio and evade the stronger first-layer comparison. The local theorem
now gives the exact simultaneous system

    D_P = (12/r_P-1)A_F,P + (12/r_P)D_(r_P),P,
    2 sum_i length(T_i)_P = 12D_P,
    sum_P D_P = 11ell-42,
    sum_P A_F,P = 4a-14+ell,
    ell in {4,5,6,7},
    lcm_P r_P = 12.

These equations retain all higher primitive-index socle defects and
simultaneous support points. They do not claim that any remaining
system lifts to a global pair or that C0 is non-STCI. The unrestricted
normal, nonnormal, and entirely thick branches remain open.

## 8. Audit provenance

The ordinary free-layer theorem was first proposed by `socle_audit`
and independently reconstructed by the root and the
`index12_multiplication` worker. The root then proposed the pointwise
Frobenius identity, the local Jacobian/index formula, and the resulting
symbolic-triple contradiction. This note independently reconstructs
all of those new steps, explicitly checking the socle's base change,
the normal-domain colon argument, the shared free normal generator,
and the saturation identifying symbolic triples.

The primary Jacobian theorem was inspected for this new bridge; no
previously accepted repository calculation was rerun. Parallel agent
agreement is not the proof: Sections 1--6 contain the actual arguments.
No memory file was used for this continuation.

