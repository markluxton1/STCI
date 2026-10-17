# Regular single-root conductor concentration is impossible in every mate degree

Date: 2026-10-13, completed across local midnight on October 14.
Author: `quintic_continuation/l2_structural`.

Status: **NEW EXACT ELIMINATION AND WRITTEN THEOREM; independent audit
pending**. Accepted existing Taylor, actual-conductor, actual-fiber and
regular-L1 proofs are premises, as requested by the user. None of their
verifiers was replayed. This note closes the remaining regular L2
incidence in that explicitly scoped problem, subject to the new audit.
It does not close denominator-zero, infinity, multiple homogeneous
conormal-root, or Jbar-zero incidences.

## 1. The two new statements

Work over an algebraically closed field of characteristic zero in the
accepted nonendpoint sectional-genus-one quintic A4 normalization model.
Retain every actual projection-center avoidance and finite birational
projection hypothesis. Write `d=delta`, `k=kappa=aq+B`,

    Pc=q^2-6q+6, U=q(k-d)-d^2,
    D=2d(q-1)+q(q-2), E=d^2+d(3q-4)+q(q-2).

Impose the complete finite common-root incidence `Pt(q)=Jt(q)=0`, with
`G=Gs,J=Js` as in the accepted
[Taylor incidence](2026-10-13-session-nonendpoint-single-root-taylor-incidence.md).
The actual octic conductor restriction has expansion

    F(q+t)=sum_(i=1)^8 f_i t^i,
    f1=-d q L1 L2.

The regular chart is `qZ(q)!=0`, where `Z(q)=q Pc U`. Thus `d,q,Pc,U`
are units. We do not invert the original fiber leading coefficient
`A(q)`, either diagonal quotient value, or any unmentioned projection
parameter.

**New local theorem.** On this regular chart, if `L1!=0` and `L2=0`,
then `f2,f3,f4,f5` cannot all vanish. Consequently the actual conductor
restriction has local order at most five at q. This is a statement
about the full section, rather than a bound inferred from its first
normal symbol. It is independent of mate degree and does not require
Jbar nonzero or the sole-root condition.

**New all-mate consequence.** If additionally `Jbar=Js!=0` and q is
the sole common homogeneous conormal root, there is no mate of any
positive degree on the regular chart. The inherited
[quotient-fiber theorem](2026-10-13-session-nonendpoint-single-root-quotient-fibers.md)
already excludes the regular L1 branch under full inverse support.
The remaining branch has `L1!=0,L2=0`, but full inverse support and
the sole-root/Jbar hypotheses concentrate the nonzero degree-eight
actual conductor section entirely at q. That would force local order
eight, contradicting the new local theorem.

The common-root equations by themselves do not impose homogeneous gcd
degree one. Sole-root and Jbar conditions are used only in the last
support-concentration implication. Centers on the normalization remain
inadmissible, as in the accepted model; they are not silently removed
from a claimed unrestricted parameter exhaustion.

## 2. The discriminant and the first genuine unfolding parameter

The following exact new identities explain why four-parameter Taylor
incidence becomes a two-parameter algebraic problem:

    Disc_k(L2)=12 q(q-1)d^5 [d q(q-1)-(q-2)Pc],

    partial_a f2 = -(d q/2) L1 partial_k L2  (mod L2).       (1)

The second identity is modulo the actual complete L2 equation, with
the accepted common-root substitutions already made. In particular,
on `L1!=0` and away from its discriminant, `f2=0` uniquely determines
a. No later coefficients are discarded.

At `q=1`, L2 is the nonzero value `d^5`, so the L2 branch is empty.
At `q!=1,2` the discriminant-zero family, whenever its k-leading
coefficient is nonzero, has

    d=(q-2)Pc/[q(q-1)], k=d E/D,
    L1=0,
    f2=(q-2)^4 Pc^12/[9q^8(q-1)^8]!=0.                    (2)

Thus it cannot meet the new local incidence. Its possible k-leading
drop is treated separately in section 4, rather than lost in `k=dE/D`.
At q=2 the discriminant is a nonzero scalar times `d^4`, so it has
no discriminant-zero family with d nonzero.

## 3. Complete rational cover when q!=1,2 and D!=0

Over an algebraically closed field every point on this chart has an
exact discriminant coordinate m satisfying

    m^2=3-3(q-2)Pc/[d q(q-1)],
    d=3(q-2)Pc/[q(q-1)(3-m^2)],
    k=d(E+m d^2/3)/D.                                  (3)

Conversely the chosen m for a given point is
`m=3(Dk/d-E)/d^2`, so (3) covers both quadratic roots and does not
require choosing one branch of a square root. The pointwise inverse
requires precisely d,D nonzero. Here `m^2-3!=0` because
`q(q-1)(q-2)Pc!=0`. Also

    D=(q-2)(qm-3q+6)(qm+3q-6)/[q(m^2-3)].              (4)

Thus both displayed linear factors in (4) are units on this chart.
Write the following explicit polynomial:

    H=q^4m^2+3q^4m-3q^3m^2-3q^4-15q^3m+3q^2m^2
        +36q^3+27q^2m-144q^2-18qm+216q-108.

On the cover the exact first-factor expression is

    L1=-3m(q-2)Pc^2 H/
          [q^2(q-1)(m^2-3)^2(qm+3q-6)].              (5)

Therefore `L1!=0` forces both m and H nonzero. This justifies the H
division below; H is not saturated away without explanation.
Identity (1) makes the coefficient of a in f2 nonzero. Define

    av=-[f2|_(a=0)]/[partial_a f2]

on this exact chart. Its fully expanded rational function and both
numerator/denominator inputs are saved, rather than suppressed behind
an existence claim.

After substituting `a=av`, let n3,n4,n5 be the literal polynomial
numerators of f3,f4,f5, in the rational function field QQ(q,m).
The exact normalizations are

    n3=(q-2)^5 Pc^7 H g3,
    n4=(q-2)^5 Pc^7 g4,
    n5=(q-2)^5 Pc^7 g5.                               (6)

The saved g3,g4,g5 have total degrees 22,32,32. All factors removed
in (6) are units under the stated assumptions. Thus simultaneous
vanishing of f2,f3,f4,f5 implies `g3=g4=g5=0`.

Compute the literal fixed-degree resultants in m:

    R34=Res_m(g3,g4), R35=Res_m(g3,g5).

The exact QQ gcd is

    gcd(R34,R35)=q^53(q-2)^44 Pc^69.                  (7)

A common finite root of g3,g4,g5 forces both resultants to vanish,
including any leading-degree drop of these polynomials. Formula (7)
then forces one of q,q-2,Pc to vanish, contrary to the chart. The
argument uses only this necessary resultant implication, not a claim
that every resultant root is an actual solution. The literal Bezout
witness for the original resultants is saved separately.

## 4. The k-leading drop D=0 is retained and excluded

This boundary is the leading coefficient of L2 as a polynomial in k;
it is different from a geometric Cramer denominator or the original
fiber leading coefficient A(q). Since q=1 is already impossible,
`D=0,d!=0,q!=0` gives

    d=-q(q-2)/[2(q-1)], q!=2,
    k=-q(q-2)(7q^2-12q+6)/[24(q-1)^3].               (8)

The L2 equation is genuinely linear in k on this chart: its k
coefficient is `-3q^3(q-2)^4/[4(q-1)^2]`, which is nonzero.
Consequently (1) again makes f2 affine with nonzero a coefficient
on L1!=0. More explicitly that coefficient is

    3q^6(q-2)^6 V/[128(q-1)^4],
    V=5q^4-30q^3+66q^2-72q+36.

The drop V=0 is precisely an L1=0 point here and is outside the
new local theorem. After solving f2 for a, the full f3,f4 rational
functions are saved. Their literal numerators satisfy

    gcd(numerator f3,numerator f4)=q^4.              (9)

The saved literal Bezout witness combines those original numerators
to q^4. Since q is a unit, f3 and f4 cannot both vanish. No putative
exception at V=0 or a denominator of the a-solve is silently retained
as a solution: those conditions contradict L1!=0 by (1).

## 5. The target q=2 is retained and excluded

At q=2, L2 is a nonzero scalar multiple of

    6k^2-6d(d+2)k+d^2(d^2+6d+6).

The complete quadratic-field cover is

    mu^2=3, k=d+(3+mu)d^2/6,
    L1=-mu d(d+2mu/3).                              (10)

Because the ground field is algebraically closed and characteristic
zero, the two embeddings of QQ(mu) include both roots. With d nonzero,
L1 nonzero is exactly the retained unit `d+2mu/3!=0`.

In the exact ring QQ(mu)[d,a,z], let h2,h3,h4,h5 be the actual Taylor
coefficients under (10), and let

    h6=1-z*d*(d+2mu/3).

The literal polynomial identity in the saved five-entry column is

    (h2 h3 h4 h5 h6) * C = 1.                       (11)

Its multiplication was asserted exactly before saving C. Under the
retained units h6 can be zero; therefore h2,h3,h4,h5 cannot all be
zero. The witness is over the actual quadratic number field, not a
floating-point embedding or a sample mu value.

An earlier attempted unsaturated unit assertion failed because L1=0
solutions remained. That failure was mathematically informative and
is preserved. Equation (11) applies after the inherited L1 exclusion;
it is not a claim that the unrestricted q=2 Taylor ideal is empty.

## 6. Generalization and exact remaining scope

The new bound is **uniform in mate degree** and follows from the
actual conductor section plus its polynomial deformation in a. The
Jacobian factor L2 is accompanied by a discriminant, and the next
Taylor coefficient detects its simple-root unfolding through (1).
After one coefficient solves the unfolding parameter, three more
coefficients give a finite exact cover obstruction. This avoids
separate searches for every mate exponent.

The local theorem is stronger than the single-root application, but
the order-five bound alone cannot rule out several conductor-support
points sharing total degree eight. No general conductor local-order
bound for arbitrary carriers follows from these particular formulas.
The useful broader scheme is to combine an actual conductor section,
a complete discriminant cover, a nonzero unfolding coefficient and
a literal higher-coefficient Bezout obstruction.

The unclosed incidences remain `Z(q)=0` (including Pc=0 and U=0),
the intrinsic q=0 target, target infinity, Jbar=0 where permitted
A4 contribution can occur, and additional common homogeneous
conormal roots. Other normalization genera and other carrier degrees
are outside this model. The universal projective-curve STCI question
and the unrestricted characteristic-zero C0 question remain open.

## 7. Evidence and failure history

All new sources have prefix
`research/computations/generalization_quintic_l2_` and all outputs are
in `research/validation/2026-10-13-generalization-quintic-l2/`.
The accepted input is the frozen actual primitive octic
`2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/primitive-polynomial.txt`.

The coefficient-cover source generated its exact rational data and
numerators before entering a redundant direct saturation. That
saturation was interrupted after the separate exact resultant route
completed; no saturation result is claimed. Its source and raw outputs
are preserved, and the coefficient artifacts feed the completed
resultant and literal-Bézout sources.

The compact drops source initially encountered M2 syntax and a
protected-name error; its completed third version passed the new
identity calculation. The boundary source retains number-field
fraction-interface, Sequence/matrix-interface, unsaturated-unit,
matrix-lift-interface and ring-coercion failures. They are distinct
attempts, not successful independent proofs. The final clean source,
literal witnesses, raw streams, source snapshots, exit statuses and
hashes are bound by the manifest. Verification counts are restricted
to their stated algebraic identities and do not independently prove
the inherited conductor-module theorem or certify novelty.
