# Historical mathematical investigations

Complete source text preserved below, including explicit hypotheses, calculations, counterexamples and unresolved issues. Compilation is not independent correctness audit or theorem promotion.

---

## Source: 2026-10-13-generalization-higher-moment-and-loewy-bounds.md

# Reflection, higher moments, and sharp codimension-two Loewy bounds

Research batch: 2026-10-13, continued 2026-10-14. Contribution from the
`socle_audit/higher_moments` worker. No global STCI conclusion is asserted.

## Status and scope

**PROVED HERE:** the reflection identity and its equality criterion in §1;
the characteristic-free structural proof in §2; the sharp length/Loewy and
all-increasing-moment bounds in §3; and the explicit sharpness family in §4.

The codimension-two drop-by-at-most-one theorem is also **KNOWN**. A modern
primary research statement is J. Jelisiejew, S. K. Masuti, M. E. Rossi,
*On the Hilbert function of Artinian local complete intersections of
codimension three*, arXiv:2202.04021v2, §3, equation (3.2):
<https://arxiv.org/html/2202.04021v2>. It credits Macaulay, Briançon, and
Iarrobino, and cites V. Bertella, *Hilbert function of local Artinian level
rings in codimension two*, J. Algebra 321 (2009), 1429–1442, Theorem 2.6,
for realizations. The proof below removes any need to transfer
characteristic hypotheses from those references.

Throughout §1, let `(A,m,k)` be a finite local Gorenstein algebra over its
residue field `k`, with

\[
h_i=\dim_k \mathfrak m^i/\mathfrak m^{i+1},\qquad
n=\dim_k A,\qquad
d=\max\{i:\mathfrak m^i\ne0\},\qquad
M=\sum_{i=0}^d i h_i.
\]

Thus `d` is the last nonzero degree, and `m^(d+1)=0`. In §§2–4 assume
additionally that `k` is infinite and `A=k[[x,y]]/I`, with `I` primary to
`(x,y)`. These hypotheses hold for the completed generic transverse
algebra of a complete intersection supported on a curve over an
algebraically closed field. Let `b=ord(I)` denote the least order of a
nonzero element of `I`; use `b`, rather than `m`, to avoid conflating this
integer with the maximal ideal.

## 1. Exact reflection identity, not merely a first-moment estimate

Set

\[
T_i=\dim_k\mathfrak m^i=\sum_{j=i}^d h_j,
\qquad
\Delta_i=n-T_i-T_{d-i+1},\quad 1\le i\le d.
\]

Choose a linear functional `lambda:A->k` nonzero on the one-dimensional
socle. The pairing `lambda(ab)` is perfect. Consequently

\[
\dim_k\operatorname{Ann}(\mathfrak m^i)=n-T_i.
\]

The inclusion `m^(d-i+1) subset Ann(m^i)` proves

\[
\boxed{\Delta_i=
\dim_k\bigl(\operatorname{Ann}(\mathfrak m^i)/
\mathfrak m^{d-i+1}\bigr)\ge0.}
\]

Also `Delta_i=Delta_(d-i+1)`, and `Delta_1=Delta_d=0` when `d>=1`,
because `Ann(m)=m^d` is the socle.

If `X` has probability mass `h_i/n` at `i`, then

\[
\boxed{X\ \le_{\rm st}\ d-X.}
\]

Indeed, at every integer threshold `i`,
`P(X>=i)=T_i/n <= 1-T_(d-i+1)/n=P(d-X>=i)`.
This is the complete first-order stochastic dominance statement;
equivalently, `E f(X)<=E f(d-X)` for every increasing real function `f`
on `{0,...,d}`.

For any real odd function `phi` on the centered support, put `c=d/2`.
Summation by parts gives the exact identity

\[
\boxed{\sum_{i=0}^d h_i\phi(i-c)
=-\frac12\sum_{i=1}^d\Delta_i
\bigl(\phi(i-c)-\phi(i-1-c)\bigr).}
\tag{1}
\]

In particular, every increasing odd central moment is nonpositive:

\[
\sum_{i=0}^d h_i(i-d/2)^{2r+1}\le0
\qquad(r\ge0).
\]

The first instance gives `M<=nd/2`. If `phi` is strictly increasing at
each adjacent pair of support points, equality in (1) is equivalent to
every `Delta_i` vanishing. The following conditions are therefore
equivalent:

1. `M=nd/2`;
2. one, hence every, central odd power moment vanishes;
3. `Ann(m^i)=m^(d-i+1)` for every `i=1,...,d`;
4. `h_i=h_(d-i)` for every `i`;
5. `gr_m(A)` is Gorenstein.

For `(3)=>(5)`, an element of `m^i` outside `m^(i+1)` cannot annihilate
`m^(d-i)`, because `Ann(m^(d-i))=m^(i+1)`. Thus the product pairing
`G_i x G_(d-i) -> G_d` is perfect. Conversely a graded Gorenstein
algebra has symmetric Hilbert function, which implies equality of all
tails and annihilators. This proof includes `i=0,d` by the usual
`Ann(A)=0`, `Ann(0)=A` conventions.

**Edge cases.** For `d=0`, `A=k`, `n=1`, the tail sum is empty, every
central moment is zero, and the equality conditions are vacuous or
automatic. For `d=1,2`, the endpoint deficit identities force all
`Delta_i=0`, so every local Gorenstein algebra in these socle degrees
has a Gorenstein associated graded algebra.

A quantitative refinement is available when
`D=nd/2-M>0`, necessarily `d>=3`. For `r>=0`, let

\[
O_{2r+1}=\sum_i h_i(i-d/2)^{2r+1},\qquad
\alpha_r=\begin{cases}1&d\text{ even},\\2^{-2r}&d\text{ odd},\end{cases}
\]

and

\[
\beta_r=(d/2-1)^{2r+1}-(d/2-2)^{2r+1}.
\]

Since only `Delta_2,...,Delta_(d-1)` can contribute, their positive
discrete-derivative weights give

\[
\boxed{\alpha_r D\le -O_{2r+1}\le\beta_rD.}
\tag{2}
\]

In particular no higher central odd moment can vanish while the first
one is negative. Higher moments reweight the same annihilator defects;
they are not independent existence obstructions without further data.

## 2. Characteristic-free drop theorem from one Jordan block

Write `G=gr_m(A)=k[X,Y]/I*`, where `I*` is the ideal of initial forms.
The equality `ord(I)=b` gives `h_i=i+1` for `0<=i<b`.

Choose a nonzero order-`b` element of the original ideal `I`. Over an
infinite field, choose a linear coordinate `x` such that its degree-`b`
initial form remains nonzero after restriction to `x=0`. Complete it by
a coordinate `y`. Then

\[
A/xA\cong k[[y]]/(y^b).
\tag{3}
\]

To justify (3) directly, every original ideal element restricts to a
series of order at least `b` in `y`, and the chosen element restricts to
one of order exactly `b`; ideals of `k[[y]]` are principal. Independently,
restriction of the initial ideal gives

\[
G/(X)\cong k[Y]/(Y^b).
\]

No assertion that taking associated graded commutes with this quotient
is needed. These are two direct restriction calculations.

For `i>=b-1`, multiplication by `X` maps `G_i` onto `G_(i+1)`.
Therefore

\[
\mathfrak m^{i+1}=x\mathfrak m^i+\mathfrak m^{i+2}
\quad\Longrightarrow\quad
\mathfrak m^{i+1}=x\mathfrak m^i
\tag{4}
\]

by Nakayama applied to `m^(i+1)/x m^i`.

Put `K=Ann_A(x)`. The perfect Gorenstein pairing identifies `K`, as a
`k[[y]]`-module, with `(A/xA)^vee`. By (3) its `y` action consists of
one Jordan block of length `b`. In particular its submodules are exactly
`y^aK`, `0<=a<=b`.

Set `F_i=K cap m^i=y^(a_i)K`. The containment

\[
yF_i\subseteq F_{i+1}\subseteq F_i
\]

implies `a_i<=a_(i+1)<=a_i+1`, so
`dim(F_i/F_(i+1))<=1`. The exact sequence obtained from (4) gives

\[
\dim_kF_i=\dim_k\mathfrak m^i-\dim_k\mathfrak m^{i+1}=h_i
\qquad(i\ge b-1).
\]

Hence

\[
\boxed{h_i-h_{i+1}\in\{0,1\}\quad(i\ge b-1).}
\tag{5}
\]

This proves the classical codimension-two drop theorem in all
characteristics. The argument needs only the infinite-field coordinate
choice, not differentiation, Lefschetz theory, or classification of
Hilbert functions. Before degree `b-1`, the function rises by one.

The same argument also gives a modest extension: for an arbitrary
Artinian quotient of `k[[x,y]]` of socle type `t`, `Ann(x)` has `t`
Jordan blocks, and a submodule of this `k[[y]]`-module has at most `t`
generators. Thus every decline after the initial rising segment is at
most `t`. The Gorenstein case is the one-block case `t=1` above.

## 3. Sharp length/Loewy bound and a stronger moment bound

From `h_(b-1)=b` and (5), the earliest possible descent to one is

\[
B=(1,2,\ldots,b-1,b,b-1,\ldots,2,1),
\]

with last degree `2b-2`, length `b^2`, and first moment
`b^2(b-1)`. Thus

\[
\boxed{d\ge2b-2,\qquad n\ge b^2,\qquad
d\le n-(b-1)^2-1.}
\tag{6}
\]

For the final inequality, subtract one from every nonzero Hilbert
entry. The initial rise contributes `b(b-1)/2`; the forced descent
contributes `(b-1)(b-2)/2`. Hence
`n-(d+1)>= (b-1)^2`.

Equality in the last inequality of (6) holds exactly when the Hilbert
function is `B` followed by `n-b^2` additional entries equal to one.

There is a stronger statement at fixed `n,b`. Put `q=n-b^2>=0` and let
`h^max` be `B` followed by `q` ones, with last degree
`d_max=2b-2+q=n-(b-1)^2-1`. Every admissible Hilbert function satisfies

\[
\sum_{j=0}^i h_j\ \ge\ \sum_{j=0}^i h^{\max}_j
\qquad\text{for every }i.
\tag{7}
\]

For `i<=2b-2`, this follows from the forced pointwise lower baseline.
For `2b-2<i<=d`, every entry is at least one. For `i>d`, the left-hand
side is already the total length `n`. These cases prove (7).

Thus the degree distribution of `A` is stochastically dominated by the
distribution `h^max/n`. Every increasing function `f` satisfies

\[
\boxed{\sum_i h_i f(i)\le
\sum_{i=0}^{2b-2}B_i f(i)+
\sum_{r=1}^q f(2b-2+r).}
\tag{8}
\]

Equality for any strictly increasing `f` is equivalent to `h=h^max`.
In particular

\[
\boxed{M\le b^2(b-1)+q(2b-2)+\frac{q(q+1)}2.}
\tag{9}
\]

Unlike the weaker substitution of (6) into `M<=nd/2`, (9) uses the
whole forced staircase. Relative to that substitution it gains
`q(b-1)^2/2`. All power moments of positive degree have the corresponding
sharp upper bound from (8).

An equivalent useful expression is

\[
\boxed{M\le\frac{n(n-1)-(b-1)^2(2n-b^2)}2.}
\tag{10}
\]

If only `ord(I)>=a` is known, then (10) remains valid with `a` in place
of `b`: the correction `(b-1)^2(2n-b^2)` increases on
`1<=b<=sqrt(n)`. Its real derivative is
`2(b-1)(2n-2b^2+b)>=0` there. In particular every algebra of embedding
dimension two has `b>=2`, giving the sharp uniform estimate

\[
\boxed{M\le(n^2-3n+4)/2.}
\tag{11}
\]

## 4. Explicit sharpness in every characteristic

For any `b>=1` and `q>=0`, set `N=b+q` and

\[
A_{b,q}=k[[x,y]]/(x y^{b-1},\ x^b+y^N).
\]

This is an Artinian complete intersection: its only prime support is
`(x,y)`, and the two generators form a regular sequence in the regular
two-dimensional ambient ring. For a local degree order with `x^b`
leading `y^N` when `N=b`, an enhanced standard basis is

\[
x y^{b-1},\quad x^b+y^N,\quad y^{N+b-1}.
\]

The last element comes from
`y^(b-1)(x^b+y^N)-x^(b-1)(x y^(b-1))`; all remaining S-pairs reduce
immediately. This calculation uses no divisions or characteristic
restrictions. Its standard monomials are

\[
y^j\ (0\le j\le N+b-2),\qquad
x^a y^j\ (1\le a\le b-1,\ 0\le j\le b-2).
\]

Consequently `n=b^2+q`, `d=2b-2+q`, and the Hilbert function is exactly
`h^max`. Thus (6), (8), and (9) are sharp, including in positive
characteristic. For `b=1`, the rectangle of mixed monomials is empty
and the family is simply the curvilinear algebra `k[[y]]/(y^(q+1))`.

## 5. What this contributes to the STCI search

The transverse generic algebra of a hypothetical two-equation
thickening is a codimension-two Artinian complete intersection.
Its Hilbert filtration therefore obeys these uniform inequalities for
all equation degrees. They replace repeated low-degree Hilbert-function
casework with a single structural package: reflection defects, a
one-block argument, and a sharp staircase moment bound.

These necessary local conditions are compatible with explicit local
complete intersections of arbitrarily large socle degree. A global
exclusion must still use the conormal filtration, its degree/extension
data, or another compatibility constraint preventing these local
algebras from occurring globally on the curve. No local numerical
bound here is by itself a global STCI obstruction.


---

## Source: 2026-10-13-generalization-quintic-continuation.md

# Nonendpoint quintics: conductor root support instead of mate-degree searches

Date: 2026-10-13 continuation, written after midnight on October 14. Owner:
`quintic_continuation`. Status: **ZERO-CUBIC AND LAMBDA-ONE FAMILY EXCLUSIONS, THE MAIN
THREE-ROOT/FOURFOLD ALTERNATIVES, AND REGULAR SOLE-ROOT L1/L2 HAVE
PASSED INDEPENDENT AUDIT. THE FINAL MAIN 3+2 ORIGINAL-GENERATOR
WITNESS IS IN PROGRESS.** Accepted older
proofs are premises and were not replayed. The universal problem, higher
carriers, other quintic normalization genera and the full nonendpoint
common-root incidence remain unresolved.

## 1. Authoritative inherited scope

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

## 2. Complete h=3 parameters and the conductor factorization

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

## 3. Both zero-cubic charts are excluded in every mate degree

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

## 4. The entire lambda=1 main boundary also fails SUP

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

## 5. A general root-support cover for the remaining main chart

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

## 6. The high-multiplicity support incidence and current work

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

## 7. Remaining nonendpoint lanes and next action

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

## Source: 2026-10-13-generalization-ribbon-numerical-criterion.md

# A degree-free symbolic-ribbon and valuation criterion

Date: 2026-10-13. Author: `ribbon_general`, delegated by
`global_structure`. Status: **NEW WRITTEN PROOF / INDEPENDENT REVIEW
PENDING**, as a conditional general theorem. Accepted quartic computations are used as inputs, with no
reruns. This note does not claim a solution of either the fixed `C0`
question or the universal STCI question.

The accepted
[weighted-ribbon proof](OCT10_TRISECANTS_NORMAL_BUNDLE_AND_RIBBONS.md#source-2026-10-10-session-weighted-ribbon-conormal-independent-auditmd)
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


---

## Source: 2026-10-13-generalization-smooth-normalization-independent-audit.md

# Independent audit of the all-degree smooth-normalization classification

Date: 2026-10-14, America/New_York. Auditor: `frontier_reconcile`.
Status: **PASS FOR THE NEW THEOREM UNDER ITS EXPLICIT SINGLETON-LIFT AND
SMOOTH-NORMALIZATION HYPOTHESES**. This audit reviews the new derivation;
accepted quartic, conductor and fixed-C0 premises were not rerun. The theorem
does not imply that an arbitrary minimum carrier has these hypotheses.

Owner source read:
[degree-free carrier framework](OCT13_CONDUCTOR_REES_AND_GENERAL_FRAMEWORK.md#source-2026-10-13-generalization-global-carrier-frameworkmd),
SHA-256 `38bff3c497b1c0f8310a623e36c0fd5d6ded0517fc6903115b4321f5672d5848`.
The acceptance here is for section 3 and the finite fixed-C0 classification
in section 4. The later power-compression consequences have their separate
new-theorem dependency and are not promoted by this audit.

## 1. The exact accepted theorem

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

## 2. Independent reconstruction of the proof

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

## 3. Every fixed-C0 case in the finite list

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

## 4. Scope audit and retained limitations

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

## 5. Optional proof simplification, not needed for acceptance

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

## 6. Evidence and review boundaries

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

## Source: 2026-10-13-generalization-socle-independent-audit.md

# Full conormal socle budget: independent audit and general consequences

Date: begun 2026-10-13, completed 2026-10-14. Status: **PROVED**, conditional
only on the stated smooth-support hypotheses and, when used, the slope
bound (S). This is an independent review of the new mathematics in
`2026-10-13-evening-entirely-thick-rees-progress.md`. Previously accepted
quartic, blowup, saturation, and higher-jet results were taken as inputs;
none of their computations was rerun. No canonical-state file is edited.

## 1. Audit verdict and scope

The full conormal-filtration theorem, exact socle line, Frobenius
inequality, defect identity, and balanced-rational equality argument in
Sections 2--7 of the reviewed note are sound. No substantive repair is
needed. The proof correctly permits torsion in intermediate normal
layers, and correctly uses the actual Loewy index of the entire generic
algebra rather than either chosen equation order.

The only clarifications needed for a reusable statement are these:

* For an arbitrary support curve, the real-valued defects need not be
  integers. They are integers in the reviewed C0 specialization.
* The choice lambda = mu_max(N) uses the characteristic-zero symmetric
  slope theorem. The elementary globally generated twist choice works
  in every characteristic and is sufficient for all arguments below.
* Equality gives a globally Gorenstein associated graded algebra on any
  smooth support curve. Its description by a constant algebra requires
  the extra balanced rational normal-bundle hypothesis.

The global STCI problem remains open. These are necessary structure
theorems for a proposed complete-intersection thickening, not an
existence theorem or an unrestricted exclusion.

## 2. Fixed notation

Let C be a smooth integral curve of degree e and genus g in P3, and let
Y = V(F_a,G_b) be a complete intersection with Y_red = C. Put

    J = I_C O_Y,
    n = length O_(Y,eta) = ab/e,
    d = max { j : J_eta^j != 0 },
    L_j = J^j/J^(j+1),
    T_j = torsion(L_j),  B_j = L_j/T_j,
    h_j = rank B_j,
    M = sum j h_j,
    L = e(a+b-4) - (2g-2).

Assume every torsion-free quotient V of Sym^j N_C^* satisfies
deg V >= -lambda j rank V. Write

    delta_j = deg B_j + lambda j h_j,
    t_j = length T_j,
    Delta_j = delta_j + t_j,
    Delta = sum Delta_j,
    Asym = nd - 2M.

All delta_j and t_j are nonnegative. The audited theorem gives

    S = Ann_Y(J) = omega_C tensor O_C(4-a-b),
    J^d = S(-D),  D effective,
    n(lambda d-L) = lambda Asym + 2 Delta.       (1)

Here and below deg D means the degree of the effective divisor; when
writing a numerical identity involving D we use deg D explicitly.

## 3. Equality is global self-duality on every smooth support

Suppose lambda d = L. Then (1) forces Asym = 0 and all delta_j = t_j = 0.
The generic Frobenius inclusions all become equalities, so h_i = h_(d-i)
and the generic associated graded algebra is Gorenstein.

The global multiplication maps induce

    B_i -> B_(d-i)^* tensor J^d.                 (2)

These maps are generically isomorphisms. Their two bundles have the
same degree because deg B_j = -lambda j h_j and J^d = S has degree
-lambda d. Thus their determinants are nonzero sections of degree-zero
line bundles on the smooth proper curve. Every map (2) is an
isomorphism. Hence every pairing

    L_i tensor L_(d-i) -> S

is perfect everywhere on C. The entire associated graded algebra is
therefore a sheaf of graded Gorenstein algebras, with socle line S.

This proves more than generic Hilbert-function symmetry. It controls
all closed support points and gives the intrinsic filtered identities

    Ann_Y(J^i) = J^(d-i+1),  1 <= i <= d.        (3)

To prove (3), take a local section z annihilating J^i. If its first
nonzero normal symbol occurs at index j < d-i+1, the perfect pairing
L_j x L_(d-j) -> S gives a section of J^(d-j), hence of J^i, whose
product with z is nonzero. This is a contradiction.

All O_Y/J^i and J^i are Cohen--Macaulay sheaves of dimension one: their
successive quotients are vector bundles on C. Since Y is Gorenstein,
Cohen--Macaulay duality then also gives

    Hom_Y(O_Y/J^i, O_Y) = J^(d-i+1),
    Hom_Y(J^i, O_Y) = O_Y/J^(d-i+1).             (4)

The second identity follows by dualizing 0 -> J^i -> O_Y -> O_Y/J^i -> 0;
the sheaf Ext^1 of its Cohen--Macaulay quotient into O_Y vanishes.
This standard input is supplied by Stacks Project
[Lemma 47.16.7](https://stacks.math.columbia.edu/tag/0B5A), specialized to
the normalized dualizing complex O_Y[1] locally. Tensoring (4) with
omega_Y yields the corresponding canonical-module formulation.

Neither (3) nor (4) identifies O_Y with an O_C-algebra. A global
retraction Y -> C and splitting of the embedded formal neighborhood
remain separate questions.

## 4. A stronger torsion identity away from numerical equality

Assume only Asym = 0. This is equivalent to the generic associated
graded algebra being Gorenstein. The maps (2) remain generically
isomorphisms between bundles of equal rank h_i = h_(d-i), hence are
injective with torsion cokernel. Let epsilon_i be its length and put
t = sum t_j. Since

    deg J^d = -lambda d + delta_d,
    delta_d = lambda d-L-deg D,

one gets the individual inequalities

    epsilon_i = h_i delta_d - delta_i - delta_(d-i) >= 0.  (5)

Summing (5), and using (1) with Asym = 0, gives the exact new identity

    sum epsilon_i = 2t - n deg D.               (6)

In particular

    2t >= n deg D.                             (7)

If the entire normal filtration is torsion free, t = 0; then D = 0 and
every epsilon_i = 0. Thus (2)--(4) hold globally even when lambda d > L.
This is a support-point obstruction beyond the scalar budget: failure
of the top power to reach the actual socle forces enough intermediate
torsion to pay at least n deg D/2, and additional torsion measures the
degeneracy of the complementary-layer pairings.

For any order-one presentation, the generic algebra has embedding
dimension one, hence is K[z]/(z^n), with d = n-1 and all h_j = 1.
Consequently Asym = 0 automatically and (5)--(7) apply. If all its
normal layers are torsion free, the natural surjections L_1^j -> L_j
are isomorphisms of line bundles; therefore

    L_1^(n-1) = omega_C tensor O_C(4-a-b).

That is a global Picard-group condition, stronger than equality of
degrees. Torsion is precisely where this primitive-multiple-curve
description can break down.

## 5. Entirely thick presentations force exact early layers

Let m >= 2 be the smallest generic order of an element of the local
complete-intersection ideal; equivalently m = min(p,q) for a chosen
generating pair with exact generic normal orders p,q. For 0 <= j < m,
the conormal quotient map has no generic kernel. Its kernel is a
subsheaf of a vector bundle and therefore vanishes globally. Thus

    L_j = Sym^j N_C^*,  0 <= j < m.             (8)

In particular every entirely thick presentation has L_1 = N_C^*,
including at all special support points. If nu = deg N_C / 2, (8) gives

    Delta_j = j(j+1)(lambda-nu),  j < m,
    2 Delta >= [2m(m^2-1)/3](lambda-nu).        (9)

For characteristic zero, choose lambda = mu_max(N_C). If N_C is
unstable, lambda > nu and the budget has strictly positive compulsory
slack. Numerical equality is possible only when N_C is semistable.
More precisely,

    n(lambda d-L)
       >= lambda Asym + [2m(m^2-1)/3](lambda-nu).  (10)

This is a general normal-bundle obstruction applying to all degrees
simultaneously. In the balanced C0 case lambda = nu = 7, its compulsory
early-layer contribution is zero, so the ambient extension obstruction
must supply additional information.

## 6. Higher moments and uniform Loewy bounds

The companion independent derivation is in
`2026-10-13-generalization-higher-moment-and-loewy-bounds.md`.
Its elementary Frobenius and generic-linear-parameter arguments give,
in every characteristic over an infinite coefficient field:

* The distribution h_j/n is stochastically dominated by its reflection
  j -> d-j. Every odd central moment is nonpositive, and equality in
  any strictly increasing odd central test forces Asym = 0.
* For codimension-two Artin Gorenstein algebras of initial ideal order
  m, the Hilbert function begins 1,2,...,m and thereafter falls at most
  one at each step. Thus

      d <= n-1-(m-1)^2.                        (11)

The companion proof was independently checked at its delicate step:
both A/xA = K[[y]]/(y^m) and gr(A)/(x*) = K[y]/(y^m) are computed by
restricting the original ideal and its initial ideal separately. It
does not interchange quotient and associated graded without proof.
After generic-linear multiplication is surjective from degree m-1,
Nakayama gives m_A^(i+1) = x m_A^i. Frobenius duality identifies Ann(x)
as one K[y] Jordan block, and its intersections with the powers of m_A
have successive drops at most one. The explicit sharpness family has
the stated three-element standard basis; its rectangle of mixed
monomials plus the pure-y chain gives the claimed Hilbert sequence
without characteristic-dependent coefficients.

There is a stronger sharp moment statement. Put k = n-m^2 >= 0. The
Hilbert distribution at fixed n,m is stochastically dominated by the
sequence

    (1,2,...,m,m-1,...,2,1, followed by k extra ones).

Consequently

    M <= M_max(n,m)
      = m^2(m-1)+2(m-1)k+k(k+1)/2
      = [n(n-1)-(m-1)^2(2n-m^2)]/2.            (11a)

This is sharp in every characteristic, as witnessed by the local CI
(x y^(m-1), x^m+y^N), where N = n-(m-1)^2-m+1 >= m. Combining
Riemann--Roch, 2 Delta = 2 lambda M-nL, with (11a) gives

    nL <= lambda[n(n-1)-(m-1)^2(2n-m^2)].      (11b)

With the normal-bundle instability cost retained, its stronger version
is

    lambda[n(n-1)-(m-1)^2(2n-m^2)]-nL
        >= [2m(m^2-1)/3](lambda-nu).           (11c)

For all entirely thick C0 presentations, using m >= 2 already yields

    n[4(a+b)-14] <= 7(n^2-3n+4), n=ab/4.     (11d)

When only a lower bound on m is known, the corresponding bound remains
valid: the correction (m-1)^2(2n-m^2) increases on 1 <= m <= sqrt(n).

Combining (11) with (1) gives a degree-independent necessary inequality

    L <= lambda [n-1-(m-1)^2],                 (12)

and combining with (10) yields

    n{lambda[n-1-(m-1)^2]-L}
        >= [2m(m^2-1)/3](lambda-nu).           (13)

For C0, (12) specializes to

    7ab >= 16(a+b) + 28(m-1)^2 - 28.           (14)

These do not bound degrees uniformly or settle the higher-order branch.
They replace independent degree-by-degree checks with structural tests
of the entire generic algebra and its global normal filtration.

## 7. Continuation boundary

The equality obstruction from the ambient second neighborhood is a
separate new proof being independently reviewed in a companion note.
It must not be folded into the accepted socle-budget theorem without
checking relation lifting and the multiplicity-sensitive coefficient
extraction. The accepted nonzero marked-direction extension class is
used as an input, not recomputed.

The most informative unresolved data away from equality are now the
generic annihilator deficits, the torsion in every normal layer, the
determinant lengths epsilon_i when the generic graded algebra is
Gorenstein, and the degree defects of the first initial-relation bundle.
The structure above preserves all higher normal orders; no tangent-only
multiplicity cap or generic-to-special root comparison has been used.



---

## Source: 2026-10-13-generalization-thick-equality-extension.md

# A uniform generator filtration and strict equality obstruction

Date: 2026-10-13, completed across midnight into 2026-10-14.
Status: **NEW PROOF, independent audit in progress**. The accepted socle-budget
and constant-graded-algebra theorem is an input. Previously audited normal
transition and constant-direction obstruction results are also inputs; they
were not rerun. This note proves additional structure and a proposed strict
quartic boundary exclusion, uniformly in the hypersurface degrees.

## 1. Inputs and scope

Let `C=C0=[s^4:s^3t:st^3:t^4]` in characteristic zero, and suppose

    Y=V(F_a,G_b),  Y_red=C.

The complete intersection has no common surface component. Put
`J=I_C O_Y`, `n=ab/4`, and let `d` be its generic Loewy index. The
accepted theorem in
`2026-10-13-evening-entirely-thick-rees-progress.md` gives

    mu=7d+14-4(a+b),
    n mu=7 Asym+2 Delta,
    Asym>=0, Delta>=0, mu>=0.

Here the quantities retain all normal layers and their special-point
torsion. On `mu=0` the full global associated graded algebra is

    gr_J O_Y = direct_sum_j O_P1(-7j) tensor B_j,
    B=k[x,y]/(f_r,g_s),

where `f_r,g_s` are a homogeneous regular sequence over the ground
field. The normal frame and the graded quotient map have constant
coefficients. The accepted equality identities are

    ab=4rs,  d=r+s-2,  4(a+b)=7(r+s).           (1)

The degrees `r,s` belong to the full initial ideal, rather than merely
to the first symbols of the chosen hypersurface pair. All higher
cancellations remain allowed.

The previously verified P-010 quadratic transition gives the
defect-free primitive-triple obstruction for every constant linear
normal relation `m=U+theta V`:

    h_theta=3(theta^3 z^-5 - theta^2 z^-4/2
                 +theta z^-3/4-z^-2/8)
              in H^1(O_P1(-7)).               (2)

It is nonzero for every finite `theta`. The missing direction has
class `3z^-5`, also nonzero. This is imported from
`2026-10-06-localcoh-constant-direction-apolar.md` and the accepted
constant-direction primitive-multiple-curve frontier. No new verification
of (2) is needed.

The new arguments below use (2) only after constructing and testing the
appropriate obstruction for an arbitrary-degree binary relation.

## 2. The actual generator filtration

Write `I=I_C`, `Q=I_Y` in the ambient smooth threefold, and

    M=Q/IQ,
    F^j M=image(Q intersect I^j -> Q/IQ).

For any full initial ideal `K=in_I(Q)` locally generated by a
homogeneous regular sequence of positive degrees `r,s`, there is a
canonical identification

    gr_F M=K/(S_+K),  S=Sym N_C^*.             (3)

In particular, when `r<s`, the degree-`s` relation bundle is a line
subbundle of the actual generator bundle and the degree-`r` relation
bundle is its quotient. Under the equality model this proves

    0 -> O(-7s)
      -> O(-4a) + O(-4b)
      -> O(-7r) -> 0.                         (4)

For `r=s`, one instead gets `O(-4a)+O(-4b)=O(-7r)^2`.

The complete proof is in the independently derived companion
`2026-10-13-generalization-thick-generator-filtration-audit.md`.
Its essential local step is a finite Koszul cancellation algorithm:
for lifts `f,g` of the regular initial symbols,

    Q intersect I^j
       =I^max(j-r,0) f + I^max(j-s,0) g,
    in_I(IQ)=S_+K.                             (5)

Krull intersection first proves that these local lifts generate the
whole ideal. Every cancellation of their leading terms is a Koszul
syzygy of the regular initial symbols, so it can be removed without
losing the indicated coefficient orders. This proves (5) including
arbitrary higher normal terms.

Thus (4) neither assumes a global change of homogeneous generators nor
assumes that the embedded formal neighborhood splits. Its quotient
coefficients are actual global sections

    alpha in H^0(O(4a-7r)),
    beta  in H^0(O(4b-7r)),

with no common zero. It follows that `7r<=4a,4b<=7s`.
This interval condition alone supplies no contradiction: at `(a,b)=(6,8)`
and `(r,s)=(2,6)`, the exact sequence has numerical form

    0 -> O(-42) -> O(-24)+O(-32) -> O(-14) -> 0.

The crucial additional obstruction comes from the ambient second
formal neighborhood.

## 3. A direction-support theorem for arbitrary binary relations

The following structural statement is independent of `a,b`.

**Binary relation obstruction.** Let a smooth curve have balanced split
conormal `H^-1 tensor V`, with `dim V=2`. Assume an embedded ideal has
full constant initial ideal generated by a homogeneous regular sequence
`f_r,g_s`, where `r<s` and `s>=r+2`. For each constant linear relation
`m in V`, let `h_m in H^1(H^-1)` be the obstruction to a defect-free
primitive triple in that direction. In characteristic zero, every
linear factor of `f_r` must have `h_m=0`.

Here a constant binary relation means compatibility with the natural
map from the symmetric conormal algebra, so that its relation direction
is globally constant after twisting by `H^r`. This hypothesis is
available on the accepted equality boundary.

To prove the statement, choose local normal frames with scalar linear
transition, and let `D` denote the quadratic part of the ambient
transition. Acting on a homogeneous degree-`r` polynomial by the chain
rule gives the degree-`r+1` discrepancy

    D(f_r).

Local higher-order corrections to a lift of `f_r` change this by a
Cech coboundary. A change in the unit used to glue the relation
generator changes it by `f_r` times a linear normal form. Base-coordinate
motion changes the leading scalar transition by the same kind of
multiple and disappears in this quotient. Since `s>=r+2`, the only
degree-`r+1` initial relations are `f_r V`. Consequently existence of
the actual ideal requires vanishing of the class

    [D(f_r)] in
       H^1(H^-1) tensor (Sym^(r+1)V / f_r V).  (6)

This constructs the obstruction for the actual relation; it does not
infer it merely by analogy with the already known linear case.

Now factor `f_r=m^t H_0(m,ell)` with `t>=1`, where
`H_0(0,1)!=0` and `(m,ell)` is a constant basis of `V`. Define a
constant linear functional on degree-`r+1` binary forms by extracting
the coefficient of

    m^(t-1) ell^(r+2-t).

Every form in `f_r V` is divisible by `m^t`; therefore this functional
descends to the quotient in (6). The Leibniz rule gives

    D(f_r)=t m^(t-1) H_0 D(m) + m^t D(H_0).

The second term is annihilated by the functional. In the first term,
the only contribution to the designated coefficient is

    t H_0(0,1) times the coefficient of ell^2 in D(m).

The induced map on cohomology thus sends (6) to

    t H_0(0,1) h_m.                            (7)

In characteristic zero the scalar multiplying `h_m` is nonzero.
Vanishing of (6) implies `h_m=0`. Apply this argument to each distinct
linear factor, with its actual multiplicity. No simplicity of the
roots is assumed. This proves the direction-support theorem.

Its geometric content is that the quadratic ambient transition must
preserve every divisor direction of the lowest constant normal
relation. The test remembers the next normal order. It is not a
tangent-only intersection-multiplicity estimate and does not compare
generic and special ruling-root multiplicities.

The detailed embedded gluing and coefficient extraction proof is in
`2026-10-13-generalization-thick-equality-geometry.md`. Independent
review is being recorded separately.

## 4. The entire quartic equality boundary is excluded

For `C0`, every constant direction has nonzero obstruction (2).
Every nonzero degree-`r` binary form over the algebraically closed field
has a linear factor. Therefore the direction-support theorem excludes
the constant graded-CI model whenever `s>=r+2`.

The equality arithmetic forces exactly that gap, in every degree.
Indeed from (1),

    16(a-b)^2
       =49(r+s)^2-256rs
       =49(s-r)^2-60rs >=0.                   (8)

If `s=r`, the right side is negative. If `s=r+1`, it is at most
`49-60*1*2<0`. Thus positive `r,s` satisfying (1) have

    s-r>=2.                                  (9)

The sharper real inequality is

    s/r >= (79+16 sqrt(15))/49 approximately 2.877.

For an entirely thick pair `r>=2`, this gives an even larger gap; the
weaker (9) is all the proof needs. Combining (2), (6)--(9) proves the
new proposed uniform conclusion

    mu>0 for every characteristic-zero C0
    complete-intersection thickening with reduced support C0. (10)

In particular the accepted budget becomes strict:

    7d+14-4(a+b)>=1,
    n mu=7 Asym+2 Delta>0.                    (11)

Equivalently,

    d >= ceil((4(a+b)-13)/7).

This excludes the constant `(2,6)` Loewy-six equality algebra for a
`(6,8)` presentation. Such a presentation would now require `d>=7`.
The statement does not exclude the higher-Loewy branch or place a
uniform upper bound on `d`.

## 5. The generalization and the remaining gap

The generator theorem (3) works for any smooth support curve and any
regular initial complete intersection. If the normal bundle is
`H tensor k^2` and the full graded normal algebra is constant, its
minimal relation bundles are `H^-r,H^-s`, giving the global sequence

    0 -> H^-s -> O_C(-a)+O_C(-b) -> H^-r -> 0.

The direction-support theorem uses only the quadratic embedded
transition and has no hypersurface-degree bound. It reduces the
constant initial-relation problem to the zero locus of the line
obstruction `m -> h_m`. If that locus is empty, a constant graded-CI
model with a generator gap of at least two is impossible. If it is
nonempty, the theorem confines every factor of the lower relation to
that locus, yielding a structural classification target instead of
an enumeration of hypersurface degrees.

In characteristic `p`, the coefficient `t` in (7) can vanish. A pure
`p`-th power relation is therefore not excluded by this derivative
argument. The theorem is deliberately restricted to characteristic
zero; it does not transfer the quartic conclusion to positive
characteristic.

The unsolved branch has positive global defect or Gorenstein
asymmetry. The accepted equality theorem does not make its first
relation constant, and meromorphic normal corrections can acquire
poles. Extending the argument beyond equality requires a theorem that
charges those poles and moving relation directions to the nonnegative
budget `Delta`, rather than treating the new strict inequality as a
complete STCI obstruction.

Thus the global STCI problem remains open. The progress is a uniform
filtered-generator theorem and a degree-independent exclusion of the
zero-defect quartic boundary, subject to the recorded independent audit
of the new obstruction argument.

## 6. Beyond equality: the first relation pays a global defect

There is a useful extension that requires neither `mu=0` nor a generic
Gorenstein initial algebra. Define the actual initial-relation sheaves

    K_j=ker(Sym^j N_C^* -> L_j).

They are torsion-free subsheaves of vector bundles on the smooth curve,
so they are vector bundles, even when `L_j` has torsion. Exactness gives

    deg K_j=-7j rank K_j-Delta_j.              (12)

Suppose the first generic relation occurs in degree `r`, is unique,
and has no independent relation in degree `r+1`:

    rank K_r=1, rank K_(r+1)=2,
    (K_(r+1))_eta=(K_r)_eta times V.          (13)

If `Delta_r=0`, twisting its inclusion into `Sym^r N_C^*` produces a
degree-zero line subbundle of a trivial bundle. The inclusion is
constant, so `K_r=O(-7r) f_r` for a fixed binary form. Multiplication
then injects

    O(-7(r+1)) tensor f_r V -> K_(r+1).

Its determinant is a nonzero section of a line bundle of degree
`-Delta_(r+1)`. Since that defect is nonnegative, it must vanish, and
the injection is an isomorphism. The quadratic obstruction of Section 3
therefore applies and yields a contradiction. Thus

    Delta_r>=1 under (13).                    (14)

This is a uniform exclusion of a zero-defect first relation even when
the rest of the normal algebra has defects or Gorenstein asymmetry.
Its hypotheses involve the first two relation ranks, rather than the
hypersurface degrees.

An even stronger statement holds if the first generic relation
direction is constant and its entire failure to extend as the saturated
constant line occurs in a divisor `D`. Precisely, suppose (13) and

    K_r=O(-7r) f_r(-D),  delta=deg D.

The constant saturated line `O(-7r) f_r` lies in the ambient symmetric
conormal bundle. Formula (12) gives `delta=Delta_r`, including possible
torsion in `L_r`; no torsion is silently discarded.

The generic span of `K_(r+1)` is `f_r V`. Since this is a constant
subbundle of the ambient degree-`r+1` symmetric conormal bundle, the
entire sheaf `K_(r+1)` lies in it: compose its inclusion with the
torsion-free constant quotient and use generic vanishing. In symbols,

    K_(r+1) subset O(-7(r+1)) tensor f_r V.    (15)

This is the saturation argument needed when the actual degree-`r+1`
relation sheaf is modified at special points. Equality with `f_r V`
is unnecessary, because the obstruction is tested in the larger
quotient killing the whole saturated span.

On a chart, let `h` be the local defining function of `D`, and lift
the local initial generator `h f_r` to an actual ideal element. Modulo
the saturated span `f_r V`, its degree-`r+1` discrepancy is

    h D_ambient(f_r).

The moving-base derivative of `h` contributes only a multiple of
`f_r`; the same is true of the gluing unit. Both disappear in the
quotient in (15). Local higher corrections are Cech coboundaries.
The corresponding global obstruction therefore lies in

    H^1(O(delta-7))
        tensor (Sym^(r+1)V / f_r V).           (16)

The twist `O(delta)` is the dual of the divisor factor in `K_r`.
Equivalently, the class in (16) is obtained from the untwisted quadratic
transition class by multiplication by the global section defining `D`.
Applying the factor coefficient functional from Section 3 gives the
new necessary condition

    D times h_m=0 in H^1(O(delta-7))
      for every linear factor m of f_r.       (17)

This extends the accepted scalar-divisor contact condition from a
linear relation to an arbitrary-degree binary relation, with every
factor and every factor multiplicity retained. Characteristic zero is
again essential when the coefficient functional multiplies by that
multiplicity.

The accepted apolar kernel description of (2) now yields a structural
classification of the small-defect possibilities, uniformly in `r`:

- `delta<=1` is impossible for a constant generic relation direction.
- At `delta=2`, all factors of `f_r` must be the same pure endpoint
  direction. The divisor is respectively `2[0]` or `2[infinity]`.
- At `delta=3`, all factors still have one and the same constant
  direction. For a finite mixed direction `m=U+theta V`, `theta!=0`,
  the divisor is exactly `[0]+[-2theta]+[infinity]`; for an endpoint,
  the divisor has the corresponding doubled endpoint plus one point.
- If a constant `f_r` has at least two distinct linear factors, then
  `Delta_r=delta>=4`.

To see the last two claims without repeating the earlier apolar rank
calculation, use its already established kernels. A degree-three
divisor annihilating a mixed direction is

    D_theta=st(t+2theta s).

For distinct nonzero `theta` these divisors differ. An endpoint needs
a doubled `t` or doubled `s`, whereas `D_theta` has both endpoints
simple. A divisor killing both endpoints would be divisible by
`s^2t^2` and have degree at least four. Thus a common annihilating
divisor of degree at most three cannot serve two distinct directions.

These are necessary conditions. They do not assert that an allowed
power relation and divisor lift to a flat thickening, or that their
higher obstruction vanishes. They sharply reduce the constant generic
relation branch without proceeding one hypersurface degree at a time.
The new sheaf obstruction (16)--(17) is being independently reviewed;
its later audit status must be preserved.

## 7. Moving relations pay a quadratic gap cost

The positive-defect first relation also admits a structural reduction.
Retain a unique first generic relation in degree `r`, and let `s>r`
be the degree of the next independent generic relation. This means
that throughout `r<=j<s` the generic relation space is generated by
the first relation and its normal multiples, of dimension `j-r+1`.

Let `W` be the saturation of `K_r` in `Sym^r N_C^*`. It is a line
subbundle, so its fibers never vanish. Write

    W=O(-7r-epsilon),
    K_r=W(-D),  delta=deg D.

The twisted inclusion `W(7r)=O(-epsilon)->Sym^r V tensor O` is a
basepoint-free tuple of binary-form coefficients. Consequently
`epsilon>=0`, and it is exactly the degree of the relation-direction
map

    phi:C=P1 -> P(Sym^r V).

The relation is constant exactly when `epsilon=0`. Exactness and
torsion accounting give

    Delta_r=epsilon+delta.                    (18)

For `t=j-r>=0`, multiplication of `W` by degree-`t` conormal forms is
fiberwise injective: multiplication by a nonzero binary form over a
field is injective. Its image is therefore a subbundle

    A_j=W tensor Sym^t N_C^*
       =O(-7j-epsilon)^(t+1)
       subset Sym^j N_C^*.

It is the saturation of `K_j`, since their generic spans agree.
Moreover multiplying the actual `K_r=W(-D)` gives the sandwich

    A_j(-D) subset K_j subset A_j,  r<=j<s.   (19)

Thus `A_j/K_j` is a torsion sheaf of length `t_j` with

    0<=t_j<=(j-r+1)delta,
    Delta_j=(j-r+1)epsilon+t_j.               (20)

At `j=r`, `t_r=delta`. Summing these exact defects, with the remaining
normal-layer defects nonnegative, proves the new uniform lower bound

    Delta >= epsilon (s-r)(s-r+1)/2 + delta.  (21)

This is a quadratic cost in the gap before the next independent
relation. It holds with arbitrary layer torsion and does not rely on
the equality model or a generic Gorenstein associated graded algebra.
The degree of the moving relation and the divisor where the actual
relation fails to saturate are separated and retained.

The full socle budget, retaining `Asym` rather than assuming it vanishes,
turns (21) into

    n mu >= 7 Asym+epsilon(s-r)(s-r+1)+2delta. (22)

For a moving relation, `epsilon>=1`; for a constant relation the
pole theorem in Section 6 imposes `delta>=2`, and `delta>=4` when the
constant binary form has two distinct factors. This produces a
degree-independent choice: relation movement pays a quadratic
gap cost, while a constant relation pays a prescribed pole divisor.
Neither branch can be omitted.

The argument works on any smooth curve with `N_C=H tensor k^2`.
Write the saturated first-relation line as

    W=H^-r tensor A^-1,

where `A` is the pullback of `O(1)` under the relation-direction map.
It is globally generated and has nonnegative degree. Replacing
`epsilon` by `deg A` gives exactly (19)--(21). Thus the structural
gap cost is not specific to a rational quartic. Neither generic
Gorensteinness nor symmetry of the normal Hilbert function is required
for (21) or (22).

## 8. The next-order operator for a moving relation

The cubic fixed-direction obstruction must not be evaluated on a
moving relation without retaining the base derivative. The accepted
embedded chart identities, expanded once to derive this new operator,
give

    W=z^-1+epsilon_base+O(normal^2),
    epsilon_base=-z^-5 u-(1/2)z^-4 v,

    z^7 u'=u+D_u+O(normal^3),
    D_u=-(5/2)z^-4 u^2-3z^-3 uv-(3/8)z^-2 v^2,

    z^7 v'=v+D_v+O(normal^3),
    D_v=3z^-5 u^2-z^-4 uv-(9/4)z^-3 v^2.

For a basepoint-free moving relation of degree one, write its leading
binary form on the first chart as

    f(z;u,v)=A(u,v)+z B(u,v),  deg A=deg B=r.

On the other chart it is `w A+B`. Expanding at the moving coordinate
and discarding only multiples of `f V` yields the exact additional
term `-z^2 epsilon_base B`. Thus the degree-`r+1` obstruction operator
is

    D_u partial_u f + D_v partial_v f
       +(z^-3 u+(1/2)z^-2 v) B,
       modulo the moving span f(z)V.          (23)

The last term survives because `B=partial_z f` need not be a multiple
of `f`. This is the precise reason the constant-direction zero-locus
theorem cannot simply be applied pointwise to a moving direction.

The exact fractional expansion is preserved in
`research/computations/generalization_moving_first_relation_operator.py`
and its JSON output. It uses only standard-library fractions and
truncates every normal polynomial at order two. This is a new
calculation of the moving-relation operator, rather than a repeated
verification of the accepted normal bundle or fixed-direction class.

For a basepoint-free degree-one relation, the saturated degree-`r+1`
relation bundle is `O(-7(r+1)-1)^2`, and the quotient obstruction
bundle fits into

    0 -> O(-7)^2 -> O(-6)^(r+2) -> Q -> 0.

Equation (23) must vanish in `H^1(Q)`. One may express this as a
uniform binary-polynomial recurrence, with five cohomology
coefficients and six linear-form unknowns, independently of the
hypersurface degrees. No proof of the vanishing or nonvanishing of
that moving-relation class is claimed here; (21)--(22) already charge
its movement to the exact global budget.

## 9. Provenance and continuation record

- Accepted input: `2026-10-13-evening-entirely-thick-rees-progress.md`,
  Sections 2--7, for the full budget and constant equality algebra.
- Previously verified input: P-010 and
  `2026-10-06-localcoh-constant-direction-apolar.md`, for nonzero
  defect-free primitive-triple obstruction in every constant direction.
- New independent filtered-module derivation:
  `2026-10-13-generalization-thick-generator-filtration-audit.md`.
- New quadratic transition/factor extraction derivation:
  `2026-10-13-generalization-thick-equality-geometry.md`.
- New first-relation/pole-budget extension: Section 6 here, with an
  additional independent sheaf-scaling check requested from the
  filtered-generator agent.
- New saturation/gap-cost theorem: Section 7 here, with an additional
  independent bundle-image check requested from the same agent.
- New exact moving-relation operator: Section 8 and
  `generalization_moving_first_relation_operator.py` with its JSON
  output. No uniform moving-relation exclusion is claimed.
- Independent review requested from the agent auditing the socle
  theorem; the result of that review must be recorded before promoting
  (10) to the canonical audited state.

No degree-by-degree search or reverification of the accepted input was
needed. The only new computation derives the moving-relation operator
for continuation. No memory file was used by this subtask.


---

## Source: 2026-10-13-generalization-thick-equality-geometry.md

# A quadratic formal-neighborhood obstruction to every zero-defect C0 thickening

Date: begun 2026-10-13; completed 2026-10-14. Owner:
`thick_extension/equality_geometry`. Status: **PROVED new reduction and
C0 equality exclusion; Sections 2--3 and the gap deduction independently
audited by socle_audit**. This note uses
the accepted socle/equality theorem and accepted P-010 quadratic line
obstruction as inputs. Those results are not reverified. It does not
exclude positive-defect thickenings or resolve whether C0 is STCI.

## 1. Statement and antecedents

Let C be a smooth rational curve with balanced conormal bundle

    N_C^* = O_P1(-lambda) tensor V,  dim V=2.

Suppose an embedded thickening Y of C has constant normal algebra

    gr_J O_Y = direct_sum_j O_P1(-lambda*j) tensor B_j,
    B = k[u,v]/(f,g),  deg f=r, deg g=s, r+2<=s.

Here the isomorphism includes the actual quotient map from
`Sym N_C^*`; f and g are constant polynomials in one fixed balanced
frame, not merely a pointwise abstract description of each fiber.

For every constant linear direction m in V, let h_m be the quadratic
obstruction class to the embedded primitive triple with constant ideal
`(m,ell^3)`, where ell is any complementary constant direction. It is a
class in H1(O(-lambda)), up to nonzero scalar changes of m and ell.

**Direction-support theorem.** In characteristic zero, every linear
factor m of f must satisfy h_m=0. More generally, in positive
characteristic this conclusion holds for every factor whose multiplicity
in f is nonzero in the field. Consequently, if every h_m is nonzero,
no such constant graded complete-intersection thickening with r+2<=s
can exist.

For C0=[s^4:s^3*t:s*t^3:t^4] in characteristic zero, the accepted P-010
calculation gives lambda=7 and h_m!=0 for every m. Therefore the
zero-defect equality boundary in the accepted full socle theorem is
empty, in every hypersurface degree pair.

The P-010 coefficients are recorded, with the full balanced charts, in
`2026-10-05-typea-audit.md`, Section 1. The socle/equality theorem is
`2026-10-13-evening-entirely-thick-rees-progress.md`, Sections 2--7.

## 2. The obstruction to lifting the smallest initial relation

Write X=P3 and K=I_Y. Work modulo I_C^(r+2). On each standard affine
chart of C, choose normal parameters u,v lifting the fixed balanced
conormal frame, together with a local parameter on C. The completed
local ambient algebra on that chart has the form O_U[[u,v]]. On the
overlap the first-order normal transition is scalar z^(-lambda), and
through quadratic degree it has the form

    u' = z^(-lambda) (u+q_u) mod I_C^3,
    v' = z^(-lambda) (v+q_v) mod I_C^3,

where q_u,q_v are quadratic in u,v with Laurent-polynomial coefficients.
The other chart's base parameter W equals 1/z modulo I_C; its deviation
from 1/z is of normal order at least one. Define the quadratic
derivation on constant normal polynomials by

    delta = q_u*d/du + q_v*d/dv.

Because f is the unique lowest-degree relation and s>=r+2, the actual
initial ideal in degrees r and r+1 is

    in(K)_r = k f,
    in(K)_(r+1) = f V.

On each affine chart choose a lift in K of the leading relation f.
Modulo I_C^(r+2) it can be written

    P_U = f(u,v)+R_U(z,u,v),
    P_V = f(u',v')+R_V(W,u',v'),

with R_U,R_V homogeneous of normal degree r+1. The choices exist
locally by the definition of the initial ideal. They exist on the full
affine chart as well: the short exact coherent sequence for the relevant
truncated ideals has vanishing first cohomology on that affine chart.

Expanding the second lift in the first chart gives

    z^(lambda*r) P_V
       = f + delta(f) + z^(-lambda) R_V(1/z,u,v)
         mod I_C^(r+2).

Replacing W by 1/z in R_V is valid at exactly this stage: R_V already
has normal order r+1, so the resulting error has order at least r+2.
This argument does not freeze the moving base coordinate at an order
where it contributes.

The difference of these two ideal elements has order at least r+1.
Its symbol therefore belongs to fV. Passing to

    Q = Sym^(r+1) V / f V

gives

    [delta(f)] + z^(-lambda)[R_V(1/z)] - [R_U] = 0.

Thus the Cech class

    o_f = [delta(f)] in H1(O(-lambda)) tensor Q

must vanish. Changing local lifts changes it by a Cech coboundary.
Multiplying an ideal lift by a unit with a first-normal correction
changes the expression by fV, already zero in Q. Changes in the lift of
the scalar conormal transition, including moving-coordinate changes,
likewise contribute only fV. No global retraction of Y to C or splitting
of its filtered algebra is assumed.

## 3. A constant factor extracts an accepted line obstruction

Over the algebraically closed field, take a linear factor m of f with
multiplicity t>=1. Choose a complementary linear form ell and write

    f = m^t H,
    H mod m = c ell^(r-t), c!=0.

The homogeneous polynomial delta(f) has degree r+1. Take the constant
linear functional on Sym^(r+1)V extracting the coefficient of

    m^(t-1) ell^(r+2-t).

It descends to Q because every element of fV is divisible by m^t. The
Leibniz rule gives

    delta(f)= t m^(t-1) H delta(m) + m^t delta(H).

The extracted coefficient is therefore

    t c times the ell^2 coefficient of delta(m) mod m.

But the latter coefficient is exactly the quadratic line-obstruction
cocycle h_m: modulo m, the normalized normal transition for m has the
form

    m' = z^(-lambda)(m+h_m ell^2) mod (m,I_C^3).

The constant linear functional commutes with both Cech restrictions and
the scalar transition z^(-lambda). Hence it takes o_f to t c h_m in
H1(O(-lambda)). If o_f=0 and t is invertible, then h_m=0. This proves
the direction-support theorem.

This is also the elementary logarithmic factor argument: a derivation
delta(f) divisible by f can occur only when each factor of f with
invertible multiplicity is preserved by the derivation. The coefficient
extraction makes that argument valid directly in the cohomological
quotient, including repeated factors.

## 4. Applying accepted P-010 data to C0

Use the accepted balanced frames

    u=b-(3/2)za, v=a,
    u'=a'/2, v'=-3Wa'+2b',
    W=(z^3+a)/(z^4+b),
    a'=z/(z^4+b)-W^3,
    b'=1/(z^4+b)-W^4.

For m=u+theta*v and ell=v, the accepted quadratic line-obstruction is

    h_theta = 3 theta^3 z^(-5) - (3/2) theta^2 z^(-4)
            + (3/4) theta z^(-3) - (3/8) z^(-2).

For the missing direction m=v, ell=u, it is

    h_infinity = 3 z^(-5).

In H1(O(-7)), z^(-1),...,z^(-6) are the usual Cech basis. In
characteristic zero, h_theta is nonzero for every theta because its
z^(-2) coefficient is -3/8. The missing-direction class is also
nonzero. The direction-support theorem consequently excludes every
constant graded CI(r,s) with s>=r+2, regardless of the size of r and s.

## 5. Every C0 zero-defect equality has the required gap

The accepted socle/equality theorem gives, for any hypothetical
zero-defect complete intersection Y=V(F_a,G_b) with support C0,

    ab=4rs,
    4(a+b)=7(r+s),
    d=r+s-2.

We order r<=s. The discriminant of a,b is nonnegative. Substitution
gives

    49(s-r)^2 >= 60rs.

This immediately excludes r=s. It also excludes s=r+1 because then
the left side is 49 and the right side is at least 120. Hence s>=r+2.
No generator-filtration theorem is needed for this gap deduction.

In the order-one case the constant algebra may have embedding
dimension one; it can still be written as k[u,v]/(f,g), with r=1 and
f linear. The same argument applies whenever it occurs on equality:
the two displayed degree relations again imply s>=r+2. In the entirely
thick case r>=2, so the result applies directly to the branch requested.

Therefore every hypothetical complete-intersection thickening of C0
in characteristic zero has the strict full-normal budget

    mu = 7d+14-4(a+b) > 0,
    n mu = 7 Asym + 2 Delta,
    n=ab/4.

Since mu is integral, mu>=1. If arithmetic forces mu to be a multiple
of four, its smallest permitted value is four. This strict inequality
uses the full higher-normal algebra through d and its initial relation;
it is not a tangent-only cap on horizontal multiplicity.

For the formerly retained thick pair (a,b)=(6,8), the socle theorem had
d>=6 and equality d=6 forced graded degrees (r,s)=(2,6). That equality
model is now excluded; every such hypothetical thickening must have
d>=7 and mu>=7.

## 6. Limits and continuation

There is a useful extension that does not assume equality or a complete
intersection. Define the actual normal relation bundles

    K_j=ker(Sym^j N_C^* -> J^j/J^(j+1)).

They are vector bundles because they are subsheaves of vector bundles
on the smooth curve. With the accepted normal defects Delta_j,

    deg K_j = -7j rank K_j - Delta_j.

This formula includes the torsion length of the quotient. Suppose the
generic first relation is unique in degree r, and there is no independent
relation in degree r+1. Thus rank K_r=1 and rank K_(r+1)=2. If
Delta_r=0, then K_r(7r) is a degree-zero line bundle with an injection
into a trivial bundle. Its inclusion is constant and its cokernel is
locally free, so K_r=O(-7r)f for a constant f.
Multiplication gives a rank-two injection

    O(-7(r+1)) tensor fV -> K_(r+1).

Its torsion cokernel has length

    deg K_(r+1) + 14(r+1) = -Delta_(r+1).

Nonnegativity of both this length and Delta_(r+1) forces
Delta_(r+1)=0 and makes this injection an isomorphism. The relation
lift and factor extraction therefore apply verbatim. Consequently, on
C0 in characteristic zero,

    Delta_r >= 1

whenever the generic first relation is unique and there is no independent
adjacent relation. This obstruction is local in the normal filtration;
it does not require zero defects in any higher layer, Gorenstein
duality, or a bounded hypersurface degree.

The result excludes the entire zero-defect boundary uniformly. It does
not bound d from above. Positive-defect thickenings can have variable
graded relation subbundles, normal-layer torsion, and effective defects;
those may kill or modify the obstruction. The accepted budget records
their total cost but does not currently exclude them.

The natural extension is to make the obstruction cost quantitative for
a nonconstant lowest relation line in Sym^r N_C^*, including its
coefficient divisor and possible order-(r+1) extra initial generators.
Any such theorem must preserve the moving-coordinate terms and all
special points; an abstract generic Artin model does not supply a
global two-hypersurface representation.

The cohomological proof applies to other smooth rational curves with
balanced conormal bundle if their quadratic direction obstructions are
known. It places the support of the first homogeneous relation in the
zero locus of the direction-obstruction map. C0 has empty zero locus,
which is the structural reason its equality boundary disappears.

More explicitly, over the direction projective line P(V), write M for
the tautological line O(-1). The quadratic derivation induces

    h in H1(O_C(-lambda)) tensor Hom(M,Sym^2(V/M)).

Since V/M=det(V) tensor M^(-1), choosing a determinant normalization
identifies this with a vector-valued cubic section of O_P(V)(3).
Changing the normal coordinate lifts changes the cohomology class by
a coboundary; radial terms are zero after projection to V/M. Thus,
unless this vector-valued cubic is identically zero, its common zero
set consists of at most three direction points. Every constant first
relation with an adjacent-degree gap has to factor over those points.

For C0 the accepted coefficients homogenize to

    h(A,B)=3B^3 z^(-5)-(3/2)AB^2 z^(-4)
          +(3/4)A^2B z^(-3)-(3/8)A^3 z^(-2).

Its four coordinates are the four cubic monomials with nonzero scalar
coefficients, so they have no common zero in P1. This identifies the
C0 mechanism with a general finite-direction reduction rather than a
separate degree-by-degree exclusion.

Characteristic-zero multiplicities are essential in this proof. If the
characteristic divides all factor multiplicities, delta(f) may vanish
for Frobenius reasons; moreover the displayed C0 coefficients use 2 and
3. No positive-characteristic exclusion is claimed.

## 7. Provenance and operational notes

The new proof uses accepted repository statements rather than repeating
their verification. One attempted scratch invocation of the old
`/private/tmp/stci-cas-venv/bin/python` failed because SymPy is no longer
installed in that environment. No result in this note depends on that
attempt; the accepted P-010 transition coefficients suffice, and the
new proof is symbolic and cohomological.

Memory was used only for the higher-normal-jet failure shield, then
replaced by current repository inspection: MEMORY.md lines 164--171;
rollout id `01a02fb1-2af7-7fa3-897c-9d6527951ac9`. No older
checkout-specific theorem status was transferred here.


---

## Source: 2026-10-13-generalization-thick-generator-filtration-audit.md

# The actual generator bundle from a complete-intersection initial ideal

Date: 2026-10-13. Status: **PROVED, independent filtered-module derivation**.
This note assumes the accepted equality-rigidity theorem from
`2026-10-13-evening-entirely-thick-rees-progress.md`; it does not recheck
that theorem. It proves the proposed bridge from a globally constant
graded complete intersection to the actual generator bundle. The result
is necessary structure, not an STCI exclusion.

## 1. Statement and canonical filtration

Let `X` be a smooth threefold, let `C` be a smooth curve regularly
embedded in `X` with ideal `I`, and let `Y` have ideal `Q subset I`. Suppose `Q` is
locally a complete intersection of codimension two. Put

    S = gr_I O_X = Sym_(O_C)(I/I^2),
    K = in_I(Q) = ker(S -> gr_J O_Y),
    J = I O_Y,
    M = Q/IQ.

The initial ideal uses the **entire** ideal `Q`, rather than just the
initial symbols of a chosen pair of generators. Give `M` the decreasing
filtration

    F^j M = image(Q intersect I^j -> Q/IQ).

Assume locally on `C` that `K` is generated by a homogeneous regular
sequence of positive degrees `r,s`, with `r<=s`. Then there is a
canonical identification of graded `O_C`-modules

    gr_F M = K/(S_+ K),                         (1)

where `S_+` is the ideal of positive-degree elements of `S`.
In particular the right side is the bundle of minimal homogeneous
relations of the full associated graded algebra.

If `r<s`, let `W_r` and `W_s` denote its rank-one degree-`r` and
degree-`s` pieces. The filtration has exactly two jumps and gives the
canonical exact sequence

    0 -> W_s -> M -> W_r -> 0.                 (2)

If `r=s`, the filtration has one jump and identifies `M` with the
rank-two degree-`r` relation bundle. Neither statement asserts that the
filtered algebra `O_Y` or the embedded formal neighborhood splits.

The formulation (1) applies to any smooth support curve. A balanced
normal bundle is needed only to identify the relation bundles below.

## 2. Local standard generators without a completion hypothesis

Work at a point of `C`. Let `R=O_(X,p)` and retain `I,Q` for the local
ideals. The associated graded ring is a polynomial ring in two normal
variables over `O_(C,p)`. Choose homogeneous generators

    f_0 in K_r,  g_0 in K_s,

forming a regular sequence. By the definition of the initial ideal,
they have lifts

    f in Q intersect I^r,  g in Q intersect I^s

with precisely these initial symbols. We first show `Q=(f,g)` in `R`.

Given `q in Q`, its leading symbol lies in `(f_0,g_0)`. Lift the
homogeneous coefficients of that expression and subtract the
corresponding multiples of `f,g`. The resulting element is still in
`Q`, and its `I`-order increases. Repeating finitely, for every integer
`N` one obtains

    q in (f,g)+I^N.

Apply the Krull intersection theorem to the finite local module
`R/(f,g)` and the image of `I`, which lies in its maximal ideal. It
gives

    intersection_N ((f,g)+I^N) = (f,g).

Thus `Q=(f,g)`. This argument uses a separate finite elimination for
each `N`; it never assumes that an infinite coefficient series already
belongs to the algebraic local ring. One could instead use the
completion and faithfully flat descent, but neither is needed.

Because `Q` has codimension two and `R` is regular, these two generators
form a regular sequence. Their only syzygies are multiples of
`(-g,f)`. Since `f,g in I`, their classes freely generate `M` over
`R/I`.

## 3. Strictness and all higher cancellations

For integers `t<=0`, set `I^t=R`. The precise local formula is

    Q intersect I^j = I^(j-r) f + I^(j-s) g.   (3)

The inclusion from right to left is immediate. For the converse, write
`h=alpha f+beta g` and suppose `h in I^j`. Give the two coefficients
weighted orders `ord_I(alpha)+r` and `ord_I(beta)+s`.

If their minimum `ell` is less than `j`, the degree-`ell` leading
terms cancel. Therefore their leading symbols satisfy a homogeneous
syzygy

    alpha_0 f_0 + beta_0 g_0 = 0.

Since `(f_0,g_0)` is a regular sequence, that syzygy is Koszul:

    alpha_0 = c_0 g_0,  beta_0 = -c_0 f_0,
    degree c_0 = ell-r-s.

In particular a nonzero cancellation at `ell<r+s` cannot occur. Lift
`c_0` to `c in I^(ell-r-s)` and replace the coefficients by

    alpha' = alpha-cg,  beta' = beta+cf.

This leaves `h` unchanged and increases their minimum weighted order.
After at most finitely many such corrections, both weighted orders
are at least `j`. Then

    alpha' in I^(j-r),  beta' in I^(j-s),

which proves (3). The argument includes arbitrary higher-order terms
of `f,g`; it uses the regularity of their initial symbols, not an
assumption that the generators are homogeneous in normal coordinates.

## 4. Quotienting by `IQ`: why minimal initial relations survive

We also need the strictness statement

    in_I(IQ) = S_+ K.                          (4)

The inclusion `S_+K subset in_I(IQ)` follows by lifting products of
positive-degree normal symbols and symbols of elements of `Q`.
For the other inclusion, start with a presentation

    h=alpha f+beta g in IQ,  alpha,beta in I.

Apply the same cancellation algorithm as in section 3. Every Koszul
correction preserves `alpha,beta in I`, because the correction terms
`cg,cf` belong to `I` and `r,s>=1`. At the leading order of `h`, its
symbol is therefore a sum of positive-degree coefficients times
`f_0,g_0`. It lies in `S_+K`, proving (4).

The intersection filtration on `Q` identifies its graded module with
`K`; the induced image filtration on `M=Q/IQ` is its strict quotient.
Consequently (4) proves (1). The filtration and these identifications
are intrinsic, so the local calculations glue without choosing a
global filtered basis.

For `r<s`, formula (3) reads particularly simply after quotienting:

    F^j M = M                   for j<=r,
    F^j M = (R/I)[g]            for r<j<=s,
    F^j M = 0                   for j>s.

Thus `F^sM` is the line subbundle `W_s`, and the quotient is `W_r`.
This proves the exact sequence (2).

## 5. The balanced rational equality model

Suppose now `C=P1`, `N_(C/X)=O(lambda)^2`, and the full graded algebra
is the accepted constant model

    gr_J O_Y = direct_sum_j O(-lambda j) tensor B_j,
    B = k[x,y]/(f_r,g_s),

compatibly with the natural surjection from `Sym N_C^*`. The forms
`f_r,g_s` are a homogeneous regular sequence over `k`. Flat scalar
extension makes them a regular sequence over each `O_(C,p)` too.
The minimal relation bundles are exactly

    W_r = O(-lambda r),  W_s = O(-lambda s).

Consequently, when `r<s`,

    0 -> O(-lambda s) -> M -> O(-lambda r) -> 0. (5)

For an actual global complete intersection in `P3` of degrees `a,b`,
with `degree C=e`, restriction of its Koszul presentation identifies

    M = O_C(-a) + O_C(-b)
      = O_P1(-ea) + O_P1(-eb).

Indeed the Koszul map has coefficients `(-G,F)`, which vanish on `C`,
so its restriction is zero. Right exactness gives the identification
with `Q/IQ`; no vanishing of a Tor term is being assumed.
Thus (5) is precisely

    0 -> O(-lambda s)
      -> O(-ea) + O(-eb)
      -> O(-lambda r) -> 0.                    (6)

This establishes the proposed generator sequence under the accepted
global constant graded-CI hypothesis. It does not identify `(r,s)`
with the normal orders of the original two homogeneous equations.

## 6. Concrete numerical and symbol consequences

Taking determinants in (6) gives

    e(a+b) = lambda(r+s).                      (7)

Write the quotient map as `(alpha,beta)`. Its entries are the actual
degree-`r` initial coefficients of `F,G` against the unique constant
minimal relation direction, and satisfy

    alpha in H^0(O(ea-lambda r)),
    beta  in H^0(O(eb-lambda r)).

Surjectivity means that they have no common zero on `P1`. Both numbers
`ea,eb` must satisfy

    lambda r <= ea,eb <= lambda s.             (8)

For example, if `ea<lambda r`, then `alpha=0`; surjectivity would force
`beta` to be nowhere zero, hence `eb=lambda r`. The kernel would then
be `O(-ea)=O(-lambda s)`, contradicting `ea<lambda r<lambda s`.
The other lower bound is symmetric, and the upper bounds follow from
(7). Thus (8) retains even the cases in which one entry is zero.

For `C0`, `(a,b,r,s,lambda,e)=(6,8,2,6,7,4)` gives

    0 -> O(-42) -> O(-24)+O(-32) -> O(-14) -> 0,
    alpha in H^0(O(10)),  beta in H^0(O(18)),
    alpha and beta have no common zero.

The line kernel is locally represented by `(-beta,alpha)`. Its
interpretation as an order-six generator belongs to the filtered
ideal. The sequence does **not** supply a global homogeneous
combination of the original sextic and octic whose normal order is
six: that would require an additional ambient lifting statement.

For `r=s`, the conclusion is stronger in a different way:

    M = O(-lambda r)^2.

The splitting uniqueness on `P1` forces `ea=eb=lambda r`. On a smooth
rational curve in `P3` the balanced normal value is `lambda=2e-1`.
Combining `ab=e r^2` with `ea=eb=lambda r` gives `lambda^2=e^3`.
For integral `e>1`, this is impossible because

    e^3-(2e-1)^2 = (e-1)(e^2-3e+1) != 0.

Thus equal initial-generator degrees cannot occur on this equality
boundary for a balanced smooth rational curve of degree greater than
one. This final arithmetic consequence assumes the equality length
identity `ab=e rs`, already established by the accepted graded model.

## 7. Scope and continuation

The theorem proves a uniform filtered-generator bridge; it has no
degree bound and permits arbitrary higher-order terms. The full global
initial-CI hypothesis is essential. A merely generic initial algebra
does not guarantee that these relation bundles extend without torsion
or modified degrees at special points.

The next useful step for the quartic equality model is to combine the
now-proved basepoint-free pair `(alpha,beta)` with the actual ambient
normal-image subspaces and the obstruction to lifting the order-`s`
kernel. Any such further condition must be proved separately. The
extension itself can be non-split and does not yield an STCI
contradiction for `(6,8)`.

No memory-derived theorem and no computational experiment was used in
this derivation. The only imported mathematical input from the current
record is the explicitly accepted constant graded-CI equality model.

## 8. A divisor-twisted obstruction at arbitrary first relation degree

Added 2026-10-14. Status: **PROVED necessary condition under the
constant generic direction and adjacent-rank hypotheses**. This
extension uses the accepted quadratic ambient transition and its line
obstruction classes. It does not recompute their coefficients or
apolar ranks.

For the full normal algebra of a hypothetical `C0` thickening, set

    L_j=J^j/J^(j+1),
    K_j=ker(Sym^j N_C^* -> L_j),
    Delta_j=degree(L_j)+7j rank(L_j).

Here `degree(L_j)` means `degree(L_j/T_j)+length(T_j)`, so all torsion
is included. Suppose `r` is the first generic initial-relation degree,
`rank K_r=1`, and its generic relation direction is a fixed nonzero
binary form `f in Sym^r V`, in the balanced frame `N_C^*=O(-7) tensor V`.
Assume also

    rank K_(r+1)=2.                            (9)

This excludes an independent adjacent-degree generic relation. No
global complete-intersection hypothesis on the initial ideal is needed
for this part.

The saturation of `K_r` in `Sym^r N_C^*` is the constant line
`O(-7r) f`. Consequently there is a unique effective divisor `D` with

    K_r=O(-7r) f(-D),
    delta:=degree D=Delta_r.                   (10)

Indeed `K_r` is torsion free as a subsheaf of a vector bundle; on the
smooth curve it is a line bundle. Its generic direction determines
the displayed saturated line. From the full exact sequence
`0->K_r->Sym^r N_C^*->L_r->0`, including torsion in `L_r`, one gets

    degree K_r=-7r rank K_r-Delta_r=-7r-Delta_r,

which proves the degree assertion. Torsion in a normal quotient is
therefore charged to `D`, rather than discarded in passing to the
saturation.

Multiplication by the two normal directions gives
`fV` as the generic degree-`r+1` relation space. By (9), that is its
entire generic relation space. Hence its saturation is exactly

    overline K_(r+1)=O(-7(r+1)) tensor fV.      (11)

This follows directly by intersecting the constant generic subspace
`k(C) tensor fV` with the ambient bundle. Choose a constant complement
of `fV` in `Sym^(r+1)V`; its projection detects any section outside
the stated saturation. Special-point torsion or elementary
modifications can make `K_(r+1)` smaller than (11), but cannot add an
element outside (11).

Let

    Q_f=Sym^(r+1)V / fV,
    o_f=[delta_ambient(f)] in H^1(O(-7)) tensor Q_f,

where `delta_ambient` is the quadratic derivation of the accepted
normalized normal transition. Choose the nonzero section `h_D` of
`O(delta)` with zero divisor `D`, determined up to a scalar. The
necessary obstruction condition is

    h_D o_f=0 in H^1(O(delta-7)) tensor Q_f.    (12)

In particular, the twist is `delta-7`, independent of `r`.

Here is a direct local lift and gluing proof. On the two standard
affine charts let the local coefficients of `h_D` be `h_U(z)` and
`h_V(W)`, with

    h_V(1/z)=z^(-delta) h_U(z).

These coefficients generate the inclusion of (10) into its
saturation. Locally choose ideal lifts, through normal degree `r+1`,

    P_U=h_U(z) f(u,v)+R_U(z,u,v),
    P_V=h_V(W) f(u',v')+R_V(W,u',v'),

where each `R` has homogeneous normal degree `r+1`. Such lifts exist
by the definition of `K_r`. They can be taken on each entire affine
chart: after choosing the chart's normal coordinates, the relevant
truncated ideal is a coherent module over that affine base, and the
surjection to `K_r` lifts its section because first cohomology
vanishes there. The lifts are required only modulo `I^(r+2)`.

Use the accepted scalar first normal transition
`(u',v')=z^(-7)((u,v)+quadratic terms)` and the moving base coordinate
`W=1/z+epsilon`, where `epsilon` has positive normal order. Multiplying
the second lift by `z^(7r+delta)` and expanding gives, modulo `I^(r+2)`
and multiples of `f` by normal linear forms,

    z^(7r+delta) P_V
       =h_U f+h_U delta_ambient(f)
          +z^(delta-7) R_V(1/z,u,v).          (13)

The additional term from the moving coefficient is
`z^delta h'_V(1/z) epsilon f`, of normal degree `r+1`;
it belongs to `fV` and is exactly why it disappears in this quotient.
Corrections to the scalar gluing unit likewise multiply `f` by a
normal linear form and disappear. Substituting `1/z` for `W` in
`R_V` changes it only in normal degree at least `r+2`, since `R_V`
already has degree `r+1`.

The difference between the expression (13) and `P_U` is an actual
ideal element with normal order at least `r+1`. Its symbol lies in
`K_(r+1)`, and hence in the saturation (11). Passing to `Q_f` gives

    h_U [delta_ambient(f)]
       +z^(delta-7)[R_V(1/z)]-[R_U]=0.

This is precisely the Cech coboundary equation for (12). The scalar
transition `z^(delta-7)` proves the asserted line-bundle twist.
The proof retains the actual divisor, possible torsion in `L_r` and
`L_(r+1)`, and the moving base parameter. It needs neither an ambient
retraction valid on all charts at once nor a formal splitting of the
thickening.

Finally factor `f=m^t H(m,ell)` over the algebraically closed field,
where `(m,ell)` is a constant basis and `H(0,1)=c!=0`. The coefficient
of `m^(t-1) ell^(r+2-t)` defines a constant functional on `Q_f`.
As in the binary factor calculation, the Leibniz rule sends the
quadratic discrepancy to

    t c h_m,

where `h_m in H^1(O(-7))` is the accepted line obstruction for `m`.
The same functional commutes with multiplication by `h_D`. Therefore
in characteristic zero (12) implies, for **each** linear factor,

    h_D h_m=0 in H^1(O(delta-7)).              (14)

Thus the already accepted divisor/pole annihilation condition for a
linear direction is forced for every factor of an arbitrary-degree
constant lowest relation. This generalizes the obstruction in normal
order without repeating hypersurface-degree cases. It is a necessary
condition; annihilation of these extracted line classes is not asserted
to suffice for lifting the full binary relation.

For a balanced conormal `O(-lambda) tensor V` on another rational
curve the identical proof replaces `7` by `lambda` throughout, giving
`h_D o_f=0` in `H^1(O(delta-lambda)) tensor Q_f`.

The two structural hypotheses remain essential. If the lowest generic
relation moves in `P(Sym^r V)`, its base derivative need not be a
multiple of `f` and contributes an additional term. If an independent
degree-`r+1` generic relation exists, (11) and the factor extraction
quotient must be modified. Neither stratum is excluded by this note.

## 9. Quadratic gap cost for a moving first relation

Added 2026-10-14. Status: **PROVED necessary defect inequalities**.
This argument has no constant-direction hypothesis and does not
require the generic initial ideal to be a graded complete intersection.

Retain `N_C^*=O(-7) tensor V` and the full kernels `K_j` and defects
`Delta_j` from Section 8. Suppose the first generic relation has degree
`r` and `rank K_r=1`. Its saturation is a line subbundle

    W=overline K_r subset Sym^r N_C^*,
    W=O(-7r-epsilon),  epsilon>=0.

After twisting by `O(7r)`, this subbundle gives the map of relation
directions

    phi:P1 -> P(Sym^r V),
    phi^* O(1)=O(epsilon).

The saturation ensures that the defining vector of degree-`epsilon`
sections has no common zero. Thus `epsilon` is exactly the degree of
this map, and a nonconstant relation direction has `epsilon>=1`.
For a unique effective divisor `D` one has

    K_r=W(-D),  delta:=degree D,
    Delta_r=epsilon+delta.                    (15)

Let `s>r`. Assume for every `j` with `r<=j<s` that the generic relation
space has no independent generator beyond the first one; explicitly,
with `t=j-r`,

    (K_j)_eta=(W)_eta Sym^t(N_C^*)_eta,
    rank K_j=t+1.                            (16)

The first equality is the precise generic-span hypothesis; it follows
when `s` is the degree of the next independent minimal generator of
the generic initial ideal. The range stops **before** degree `s`.
In this range the generic normal-layer rank is `r`, so these layers
are nonzero and their indices occur in the full defect budget.

Consider multiplication of symmetric normal forms:

    W tensor Sym^t N_C^* -> Sym^j N_C^*.

At each point of `C`, the line `W` is represented by a nonzero binary
form of degree `r`. Multiplication by that form is injective on the
space of degree-`t` binary forms, since the binary polynomial ring is a
domain. The map therefore has constant rank `t+1` on all fibers. Its
image is a saturated subbundle

    A_j= W tensor Sym^t N_C^*
       = O(-7j-epsilon)^(t+1).                (17)

By (16), the composition `K_j -> Sym^j N_C^* -> Sym^j N_C^*/A_j`
vanishes at the generic point. Its target is locally free, hence
torsion free; a generically zero morphism into that target is zero.
Consequently `K_j subset A_j`. Ideal multiplication of the actual
first relation `K_r=W(-D)` also gives

    A_j(-D) subset K_j subset A_j.            (18)

In particular `overline K_j=A_j`. The quotient `A_j/K_j` is a finite
torsion sheaf, of length `t_j`. The inclusions (18) imply

    0<=t_j<=(t+1)delta,
    t_r=delta.                               (19)

All torsion in the normal quotient `L_j` is still retained. Taking
degrees in the full kernel exact sequence gives
`degree K_j=-7j rank K_j-Delta_j`. Taking degrees in
`0->K_j->A_j->A_j/K_j->0` and using (17) therefore gives the exact
formula

    Delta_j=(t+1)epsilon+t_j,   r<=j<s.       (20)

Hence, writing `k=s-r`, the full nonnegative defect budget satisfies

    Delta >= sum_(j=r)^(s-1) Delta_j
          = epsilon k(k+1)/2 + sum_(j=r)^(s-1) t_j
          >= epsilon k(k+1)/2 + delta.        (21)

The final `+delta` uses `t_r=delta`; omitting it gives the proposed
weaker bound `Delta>=epsilon k(k+1)/2`. Thus a moving first relation
forces at least `k(k+1)/2` units of global defect across a gap of length
`k` before the next independent generic relation. This is uniform in
the hypersurface degrees and in the first normal relation degree.

The mechanism distinguishes two costs: moving the generic direction
charges `(t+1)epsilon` at every layer in the gap, whereas the actual
coefficient divisor is represented by the torsion lengths `t_j` and
need not be charged at its maximum possible value in every layer.
No assertion `t_j=(t+1)delta` is made.

For a balanced conormal `O(-lambda) tensor V` on another rational
curve the same proof replaces `7` by `lambda`; formulas (15)--(21)
are unchanged. The result requires the rank-one first relation and
the generic-span range (16). It supplies a lower defect bound rather
than an exclusion of every positive-defect thickening.


---

## Source: 2026-10-13-generalization-thick-relation-obstruction-independent-audit.md

# Independent audit: constant initial relations and the strict C0 socle budget

Date: begun 2026-10-13, completed 2026-10-14. Status: **PROVED**, with the
accepted P-010 nonzero quadratic direction classes used as inputs. This
audits only the new relation-lifting and factor-extraction argument in
`2026-10-13-generalization-thick-equality-geometry.md`, plus the new
first-relation defect extension proposed by `thick_extension`.
Previously verified direction coefficients and their nonvanishing are
not recomputed. No canonical-state file is edited.

## 1. Verdict

The argument is valid. It excludes every zero-defect equality model for
C0 in characteristic zero simultaneously, and proves a positive degree
defect for a unique first initial relation whenever no independent
initial relation appears at the next normal order.

The essential hypothesis is the constant quotient map from the actual
conormal algebra, rather than an abstract isomorphism of graded fibers.
The earlier equality theorem supplies that hypothesis. No assertion
that the filtered embedded neighborhood splits is needed.

## 2. General relation-obstruction theorem

Let C = P1 be smoothly embedded in a smooth threefold, with

    E = N_C^* = O(-lambda) tensor V, dim V=2.

Let K be the ideal of an embedded thickening Y with reduced support C.
Suppose its initial ideal has

    in(K)_r = O(-lambda r) tensor k f,
    in(K)_(r+1) = O(-lambda(r+1)) tensor fV,

for a fixed nonzero binary form f of degree r >= 1. Thus f is the unique
first relation, and the next normal order has only its linear multiples.
Let h_m in H1(O(-lambda)) denote the quadratic embedded obstruction
associated to a constant linear direction m in V.

Then for every factor m of f of multiplicity t whose image in the field
is nonzero,

    h_m = 0.                                   (A)

In characteristic zero every factor satisfies this conclusion. Hence
if every h_m is nonzero, the displayed initial-relation pattern is
impossible for every r simultaneously.

## 3. Independent check of relation lifting

Choose the two usual affine charts of P1 and ambient formal normal
parameters u,v lifting its fixed balanced conormal frame. On the overlap
write the transition through quadratic order as

    (u',v') = z^(-lambda)[(u,v)+(q_u,q_v)] mod I_C^3.

Let delta = q_u partial_u + q_v partial_v. The second chart base
coordinate W equals 1/z modulo I_C; it need not equal 1/z in the
embedded neighborhood.

The definition of the initial relation and affine coherent lifting
provide local ideal elements

    P_U = f(u,v)+R_U(z;u,v),
    P_V = f(u',v')+R_V(W;u',v') mod I_C^(r+2),

where R_U,R_V have normal degree r+1. Multiplying P_V by the chosen
unit z^(lambda r) preserves membership in K. Its expansion is

    z^(lambda r)P_V
      = f + delta(f) + z^(-lambda)R_V(1/z;u,v)
        mod I_C^(r+2).

The moving base coordinate creates no omitted term: substituting 1/z
for W changes R_V by normal order at least r+2. The polynomial f is
constant, so there is no derivative of a coefficient function in its
degree-r symbol. A first-normal correction to the scalar transition or
to the chosen leading lift produces a multiple of f by a linear form.

Subtracting P_U from the normalized P_V gives an ideal element of
normal order at least r+1. Its degree-(r+1) symbol belongs to fV.
Therefore

    [delta(f)] = 0
       in H1(O(-lambda)) tensor [Sym^(r+1)V/fV].  (B)

Changing either local lift only changes its representative by a Cech
coboundary. This proves (B) for the actual embedded ideal, with every
moving-coordinate contribution accounted for at the relevant order.

## 4. Independent check of repeated-factor extraction

Factor f = m^t H, with H mod m = c ell^(r-t), c != 0, and ell a
constant complement to m. Take the coefficient functional extracting

    m^(t-1) ell^(r+2-t)

from Sym^(r+1)V. It kills fV because every element of fV is divisible by
m^t. Applying the Leibniz rule gives

    delta(f) = t m^(t-1) H delta(m) + m^t delta(H).

The extracted coefficient is t c times the coefficient of ell^2 in
delta(m) modulo m. That is exactly the quadratic direction cocycle h_m.
All spaces have the same scalar transition z^(-lambda), so this constant
coefficient functional induces a map on the Cech cohomology in (B).
Its image is t c h_m. For t nonzero in the field, (A) follows.

This argument handles every repeated factor. It does not assume that
the root set is reduced or infer a bound on higher contact from the
first tangent cone. In positive characteristic, a factor with
multiplicity divisible by the characteristic is invisible to this
first derivative; no exclusion is claimed there.

## 5. Uniform consequence for C0 equality

The accepted P-010 premise says h_m != 0 for every constant direction
m on C0 in characteristic zero. The accepted full socle equality gives
the actual constant graded CI

    k[u,v]/(f_r,g_s), r <= s,
    ab = 4rs,
    4(a+b) = 7(r+s),
    d = r+s-2.

Its ordinary hypersurface degree discriminant implies

    49(s-r)^2 >= 60rs.

Thus r=s is impossible. If s=r+1, the left side is 49 while the right
side is at least 120. Hence s >= r+2, so the first two initial relation
spaces are precisely k f_r and f_r V. Every f_r has a linear factor
over the algebraically closed field. The theorem above contradicts the
accepted nonzero direction class.

Therefore every complete-intersection thickening of C0 in
characteristic zero has

    mu = 7d+14-4(a+b) > 0,
    n mu = 7 Asym + 2 Delta, n=ab/4.             (C)

This applies to the entirely thick and order-one branches. It excludes
all equality models at once, independently of the degrees of their
hypersurfaces or the degree of the first relation. For the retained
entirely thick (a,b)=(6,8) pair, d=6 is excluded and hence d >= 7,
mu >= 7. Positive-defect models remain unresolved.

## 6. New extension beyond equality: the first relation pays a defect

For any C0 presentation, put

    K_j = ker(Sym^j N_C^* -> L_j).

The kernel is a vector bundle on C0. The exact sequence, with torsion
in L_j retained, gives

    deg K_j = -7j rank K_j - Delta_j.           (D)

Suppose rank K_r = 1 and rank K_(r+1) = 2. The first assumption says
there is a unique initial relation in degree r; the second says its
linear multiples are the only relations at degree r+1. If Delta_r = 0,
twisting K_r by O(7r) gives a degree-zero line subbundle of a trivial
bundle on P1. It is O and its inclusion is a fixed nonzero binary form f.

Multiplication by the conormal bundle gives an injection

    O(-7(r+1)) tensor fV -> K_(r+1).

Its source and target have rank two. Their determinant degree
difference equals -Delta_(r+1) by (D), and also equals the nonnegative
length of their torsion cokernel. Since Delta_(r+1) >= 0, both are zero.
Thus K_(r+1) is exactly the constant bundle fV.

Sections 2--4 now contradict the accepted nonzero direction class.
Therefore, in characteristic zero,

    rank K_r = 1, rank K_(r+1) = 2
        imply Delta_r >= 1.                   (E)

No generic Gorenstein associated graded algebra, no zero total defect,
and no bounded degree pair is assumed in (E). This is a strict local
cost in the global degree/torsion budget. For example, inserting (E)
into (C)'s original nonnegative budget gives n mu >= 7 Asym + 2 whenever
these relation-rank hypotheses hold.

## 7. Fixed-direction effective-divisor extension

There is a further valid conditional extension. Suppose the generic
first relation direction is a fixed f, but

    K_r = O(-7r)(-D) tensor k f

for an effective divisor D, and rank K_(r+1) = 2. Since K_(r+1) has
generic direction fV and is a subsheaf of the conormal bundle, it is a
subsheaf of O(-7(r+1)) tensor fV globally. Projection to the quotient
by this saturated constant bundle annihilates its next-order symbols.
Relation lifting as above therefore gives an obstruction in

    H1(O(D-7)) tensor [Sym^(r+1)V/fV].

The new leading coefficient is the defining inclusion section of D.
The moving-base derivative of that coefficient contributes a multiple
of f and disappears in this quotient. Factor extraction gives, for
every factor m of invertible multiplicity,

    h_D h_m = 0 in H1(O(D-7)),                 (F)

where h_D is the section defining D. Thus the familiar pole-clearing
condition extends from a linear direction to every factor of an
arbitrary constant binary first relation. Here deg D = Delta_r by (D).

Any claimed numerical lower bound on deg D beyond (E), or restriction
on how many distinct factors f can have for a given deg D, must use the
specific apolar kernels of the accepted h_m classes. Such apolar claims
are not needed for the uniform equality exclusion proved above.

The accepted kernel descriptions cited in
`2026-10-06-localcoh-constant-direction-apolar.md` give the stronger
small-divisor classification now recorded in Section 6 of
`2026-10-13-generalization-thick-equality-extension.md`. Those accepted
kernels are used as inputs. The new comparison of their possible
common divisors was independently checked:

* No nonzero divisor of degree at most one annihilates a direction.
* A mixed finite direction theta != 0 first has a degree-three
  annihilator, uniquely proportional to st(t+2 theta s).
* The two endpoint directions require a divisor divisible by t^2 or
  s^2, respectively.

The mixed cubic has each endpoint only once, so it cannot kill either
endpoint class. Distinct mixed directions have nonproportional unique
cubics. A divisor killing both endpoint classes is divisible by s^2t^2
and has degree at least four. Therefore, under the fixed-direction
first-relation hypotheses,

    Delta_r >= 2;
    Delta_r <= 3 forces f to be a power of one linear form;
    f with at least two distinct linear factors forces Delta_r >= 4.

At degree two the single direction must be an endpoint, with its
doubled endpoint divisor. At degree three a mixed direction has the
unique divisor [0]+[-2 theta]+[infinity], while an endpoint has its
doubled endpoint plus one additional point. This is a necessary
classification of support directions and divisors, not a proof that
any surviving model has all higher obstructions zero.

## 8. Boundary of the result

The proof controls a fixed first relation and the actual next normal
layer. It fails if a new independent relation already appears at degree
r+1, or if the first relation varies in projective direction along C.
Those failures are concrete continuation strata, not silently excluded
cases. Positive defects can also clear the cohomological class as in
(F). The current results do not rule out those strata or resolve C0's
STCI status.

