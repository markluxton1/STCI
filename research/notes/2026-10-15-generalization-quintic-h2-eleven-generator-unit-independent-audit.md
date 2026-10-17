# Independent audit: the remaining-mate Delta1 open and eleven generators

Date: 2026-10-15.

Status: **PASS for the new all-remaining-mate condition Delta1 nonzero,
and for exact redundancy of the twelfth generator after the verified
actual coefficient binding and the declared localization.** The
previous h2 factor, reciprocal coordinates, sextic quotient, A4 fiber
criterion, accepted mate closures and twelve-generator reduction are
premises; none was replayed.

This note reviews only the new common unit and its algebraic effect.
It does not claim the remaining incidence is empty, remove a factor
of j, or establish nonlinear conductor descent.

## 1. Delta1 is nonzero on every remaining mate candidate

Use the accepted nonendpoint quintic A4 family, with delta nonzero,
actual j=Jbar, and full inverse support SUP as a necessary condition
for a mate. If j is nonzero, the accepted complete A4 target-fiber
criterion states that Delta1=0 gives an actual off-c point. Therefore
SUP forces Delta1 nonzero in this stratum.

If j=0, the accepted literal expression specializes to

    Delta1=G*(G+3delta^2)*(G+delta^2+2B).               (1)

The accepted G=j=0 mate closure removes the first zero factor. The
accepted entire-line mate closure removes G=-3delta^2,j=0, the second
zero factor. Finally, on G nonzero the accepted A4 target-fiber
criterion makes SUP imply

    L=G+delta^2+2B nonzero.

Indeed L=0 gives D0=delta^2/2+B=-G/2 nonzero and G=-2D0, exactly
the criterion for an off-c point. Thus every factor in (1) is nonzero
on a remaining j=0 mate candidate. This proves

    Delta1 nonzero on all remaining mate candidates,   (2)

for both values of j. This is a new common necessary open obtained
from the accepted closures. It is not asserted for every projection,
every support-incidence point before those closures, or an arbitrary
formal parameter tuple.

The accepted h2 infinity equations imply that H containing A4 forces
G=j=0. Hence H avoids A4 on the same surviving mate locus and may be
normalized as H=t^2+vst+ws^2. This monic normalization is an actual
scope condition, rather than an inversion justified for arbitrary H.

## 2. Actual and captured leading coefficients

In reciprocal source coordinates x=t/s and p=s/t, A4 is (s:t)=(0:1).
For the actual monic h2 factorization Fsrc=H Qactual, one has

    H(0,1)=1,
    Qactual(0,1)=Fsrc(0,1)=Fdet(0,1)=-3j Delta1.        (3)

Thus the actual coefficient of t^6 is -3j Delta1. On the open (2),
its ratio to j is a unit; this statement is the exact identity (3),
not a cancellation by j at field-valued points.

The previously captured Q differs from Qactual by the recorded
common scalar. The finite inverse-map capture clears commonDen and
removes coefficient content delta^4, so

    Qcaptured=(commonDen/delta^4)*Qactual,
    q6=-3*(commonDen/delta^4)*Delta1*j.                (4)

The commonDen is a unit on the original inverse-map denominator
open, and delta is a unit. After explicitly localizing at Delta1,
the entire scalar multiplying j in (4) is therefore a unit. Write

    q6=u*j,       u a unit in the localized ring.      (5)

In polynomial generator captures the retained scalar is often the
saved numerator jNum of actual j. Its denominator is an original
inverse-map unit, so (5) also says q6=uNum*jNum with uNum a unit
after the same localization. The numerator Delta1num represents
Delta1 up to its recorded denominator unit. Inverting Delta1num is
therefore exactly the new Delta1 open on that chart.

The new exact
[unit-binding capture](../validation/2026-10-15-quintic-h2-a4-unit-binding/attempt-01/execution-record.json)
strengthens that comparison to the literal polynomial identity

    delta^4*q6=-3*jNum*Delta1num.                       (5a)

Its declared-unit stripping records exponents zero for q6, delta
exponent one for jNum and delta exponent three for Delta1num, with
no discriminant or K exponents. The remaining ratio is the nonzero
rational -3. Thus, writing Jprim=jNum/delta and
Tprim=Delta1num/delta^3, it also records the polynomial factorization
q6=-3*Jprim*Tprim. Both divisions here are exact polynomial divisions
recorded by the new capture; their factors are units on the original
delta-nonzero chart.

I read the new C source, its exit-zero record, stdout, ratio and
exponent files. It parses the three saved accepted coefficient
artifacts, strips only delta, the discriminant and K, checks the
remaining ratio is a nonzero rational, and then checks the literal
polynomial equality after multiplying negative declared-unit powers
to the other side. Current source and all three input digests agree
with its record. This is a new binding identity between saved
artifacts, not a reconstruction or rerun of any accepted verifier.

Merely knowing that Delta1 is nonzero at candidate field-valued
points would not justify cancelling it in the global polynomial
ring. The operation here is the declared localization on a necessary
candidate open, followed by an exact scalar identity in that ring.

## 3. The retained-j minor is already one of the eleven cubic minors

Retain the coefficient conventions of the accepted twelve-generator
reduction:

    C=[sQ,tQ,sR],       row_i=(q_i,q_(i-1),r_i),
    M_ik=q_i*r_k-q_k*r_i,
    B_ikl=det(rows i,k,l of C),

with q_i=r_i=0 outside 0 through 6. Expanding the row-seven determinant
gives the signed identity

    B_i67=-q6*M_i6,       0<=i<=5.

In particular

    B567=-q6*M56=-u*j*M56.                             (6)

B567 is among the eleven selected cubic minors. Since u is a unit,

    j*M56=-u^(-1)*B567.                               (7)

Let I11 be generated by B_i56 for i=0 through 4 and B_i67 for i=0
through 5. Equation (7) proves the exact ideal equality

    (I11,j*M56)=I11                                   (8)

in the actual localized parameter ring. It uses no division by j
and remains valid if j is zero, a zero divisor or nilpotent. It
needs neither a reduced ring nor a nonzerodivisor assumption on j.
The same proof applies with jNum in place of j.

Combined with the accepted twelve-generator equality on
U=D(q5) union D(q6), (8) identifies the eleven-generator ideal with
the original full rank system on U in this newly localized domain.
The direct redundancy (8) itself does not need U; the equivalence
to all original rank minors still retains U.

## 4. Dividing six cubic generators by Delta1num retains j

Write the more explicit localized identity as

    q6=vUnit*j*Delta1num,

where vUnit is a unit after the original denominator and delta
localizations. The six row-seven minors then satisfy

    B_i67=Delta1num*(-vUnit*j*M_i6).                   (9)

On the new Delta1num-nonzero chart, replacing these six generators
by their quotients by Delta1num preserves the ideal exactly: it
multiplies each generator by a unit. The five B_i56 remain unchanged.
The quotients retain j. In particular the 567 quotient is
-vUnit*j*M56 and still supplies the removed first-matrix minor.

If a polynomial quotient rather than a localized fraction is saved,
its literal divisibility must be checked by the new coefficient
capture. Localized factorization alone does not establish global
polynomial divisibility. Neither formulation permits division by j
or replacement of j*M56 by M56.

In particular, the full Delta1num has a delta^3 factor, whereas q6
has no delta factor. One should not assume global polynomial
divisibility of q6 by the unstripped Delta1num. Equation (5a) gives
a simpler polynomial presentation without that assumption:

    B_i67=(3*delta^(-4)*Delta1num)*(jNum*M_i6).

The parenthesized scalar is a unit on the declared domain. Hence a
polynomial eleven-generator ideal defining the same localized ideal
is

    (B_i56 : 0<=i<=4) + (jNum*M_i6 : 0<=i<=5).         (10)

Its last generator includes jNum*M56. Thus the previously separate
twelfth generator is supplied by the normalized row-seven group,
and the retained-j condition has not been cancelled. Replacing
jNum by Jprim in (10) is another multiplication of six generators
by the original unit delta^(-1).

All original finite inverse-map conditions remain: nonzero delta,
nonzero Delta*K, nonzero cofactor determinant, recorded content and
denominator units, actual projection hypotheses, and U for the full
rank-system comparison. The new Delta1 open is justified by (2).
The proof does not turn the finite inverse-map chart into coverage
of its repeated-root boundary. With raw actual coefficients, (3)
has no finite inverse-map denominator; the captured unit (4) is only
claimed on its original denominator open.

The new result is an eleven-generator presentation on this necessary
remaining-mate open. It supplies no incidence-emptiness certificate
and no implication from the rank equations to full conductor descent.
