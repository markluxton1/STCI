# Nonendpoint quintics: conductor root support instead of mate-degree searches

Date: 2026-10-13 continuation, written after midnight on October 14. Owner:
`quintic_continuation`. Status: **NEW EXACT FAMILY EXCLUSIONS AND A COMPLETE
STRUCTURAL SUPPORT COVER; independent audit in progress.** Accepted older
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

    F = (delta^4/(1296lambda^6)) H3 S5,

where H3,S5 are fixed-degree binary forms with affine coefficient lists in
`evening-h3-proportional/main-H-coefficients.txt` and
`main-S-coefficients.txt`. Their scalar is nonzero. In particular

    H3=(delta+2lambda-1)p^3
       +(3delta lambda-3delta-9lambda+3)p^2
       +(-3delta lambda^2-6delta lambda-3lambda^2+3delta+12lambda-3)p
       -delta lambda^3+3delta lambda^2-lambda^3+3delta lambda
          +5lambda^2-delta-5lambda+1.

Their original scaling is H3=-3lambda^2 H/delta and
S5=432lambda^4(F/H)/delta^3. The displayed scalar therefore has a minus
sign: **F=-delta^4 H3 S5/(1296lambda^6)**. This explicit correction is part
of the written record; only its being a nonzero scalar enters support.

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
with separate independent geometric audit requested.

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

For a finite root x of S5, put c_i=coefficient_(p^i) S5. A root of
multiplicity at least4 satisfies

    S5(x)=S5'(x)=S5''(x)=S5'''(x)=0.                 (B)

The new exact QQ ideal, saturated only by the units in (A) and c5,
returns the unit ideal. Its source, literal four input polynomials and
captured intermediate ideal are preserved in the new validation package.
A separate original-generator witness is being extracted; this algebra
is not yet promoted to an independently audited theorem.

For the exact3+2 case choose x to be the triple root. Dividing by
`(p-x)^3` leaves

    c5 p^2+(c4+3x c5)p+(c3+3x c4+6x^2 c5).

Its discriminant is

    c4^2-4c3c5-6x c4c5-15x^2 c5^2.                 (C)

Thus all3+2 cases, including coalescence into a fifth root, lie in the
exact finite polynomial system S5(x)=S5'(x)=S5''(x)=0,(C)=0.
For SUP additionally H3(x)=H3(y)=0, where
`y=-(c4+3x c5)/(2c5)`. The second relation is imposed after multiplying
by `(2c5)^3`, so no undefined root or scalar is introduced. Both the
unrestricted multiplicity32 incidence and this stronger full support
incidence are active new exact computations. Until their executions and
witnesses finish, the3+2 case is retained as open. No empty-fiber claim is
inferred from generic parameters or a CAS process merely running.

The first direct H3^5 modulo S5 source produced exact large coefficients
but was interrupted during ideal processing. A later full Hermite-rank
approach was also interrupted in favor of this much smaller complete root-
multiplicity cover. Those sources, failed setup interfaces and outputs
remain recorded. Neither unfinished computation supplies a theorem.

## 7. Remaining nonendpoint lanes and next action

The companion new note `2026-10-13-generalization-quintic-l2.md` develops
an all-parameter exclusion of the regular sole homogeneous-root lane,
including L2, its discriminant-zero and coefficient-drop boundaries. Its
independent review is separate. The quotient/conductor proof and all new
higher Taylor conditions are retained there; no accepted old check is
replayed.

Even if the complete h3 support cover closes, the following remain outside
it: homogeneous gcd degrees1 and2 with more than one support point;
the singular target-fiber charts pZ=0 with their denominator-free original
fiber system; other Jbar=0 nonproportional families; actual conductor power
descent on surviving full-support parameters; all other quintic genera;
normal quintics, higher carriers and entirely thick presentations.

The continuation strategy is to exhaust complete support types for the
fixed-degree actual conductor section, then impose full conductor descent.
Its complexity depends on normalization geometry and conductor root
support, not on an unbounded list of mate degrees. A first-symbol root
alone is never treated as a bound on the full conductor multiplicity.
