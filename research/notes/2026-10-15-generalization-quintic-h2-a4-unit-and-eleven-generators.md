# One A4 unit open removes the retained-j twelfth generator

Date: 2026-10-15. Status: **NEW SCOPE AND EXACT COEFFICIENT BINDING;
independent review completed** in the
[eleven-generator unit audit](2026-10-15-generalization-quintic-h2-eleven-generator-unit-independent-audit.md).
Accepted conductor, coefficient, intrinsic-fiber and closed-lane theorems are
premises. This does not assert emptiness of the h2 incidence.

## 1. Delta1 is nonzero on every remaining mate candidate

Write `j=Jbar`, `S0=G+3delta^2`, `L=G+delta^2+2B`. The accepted A4
target-fiber criterion gives `Delta1!=0` under SUP when j is nonzero.
When j is zero the accepted polynomial formula gives

```
Delta1=G*S0*L.
```

The accepted G=j=0 mate exclusion removes G=0. The accepted entire-line
ramification mate exclusion removes j=0,G=-3delta^2. Finally SUP forces
L nonzero: if L=0 and G is nonzero, then `D0=delta^2/2+B=-G/2!=0` and
`G=-2D0`, giving the forbidden actual off-c A4 fiber from the accepted
criterion. Therefore

```
Delta1 != 0                                               (1)
```

on every remaining mate candidate, for both values of j. This is a
necessary open after the stated accepted mate exclusions; it is not a
claim that every SUP projection before those exclusions satisfies (1).

The accepted h2 infinity equations give G=j=0, so that lane is already
closed for mates. A remaining h2 candidate thus has finite monic
`H=t^2+vst+ws^2`. Its source A4 point is s=0, where H has value one.

## 2. Actual and captured coefficient units

For the actual source conductor `Fsrc=H Qactual`, the accepted literal
value is

```
Qactual(0,1)=Fsrc(0,1)=-3*j*Delta1.                       (2)
```

On the accepted finite inverse-map chart the captured coefficient vector
is multiplied by `kappa=commonDen/delta^4`, a unit after delta and the
recorded inverse-map denominator are inverted. Thus

```
q6=-3*kappa*j*Delta1.                                    (3)
```

In particular q6/j is a unit in the localized actual coefficient ring
where delta, the inverse-map determinant and Delta1 are units. This
statement does not divide by j, which may be zero or nilpotent.

There is a particularly simple exact binding in the saved polynomial
numerators. Write Jnum and Dnum for the saved actual Jbar and Delta1
numerators from the accepted rational cover. The new captured arithmetic
proves the literal polynomial identity

```
delta^4*q6=-3*Jnum*Dnum.                                  (4)
```

No discriminant or K powers occur in this identity. The
[new FLINT source](../computations/generalization_quintic_h2_a4_unit_binding_2026_10_15.c)
reads only those three saved polynomials, removes only declared-unit
powers, finds constant ratio -3, and then asserts (4) as a polynomial
identity by cross multiplication. Its
[execution record](../validation/2026-10-15-quintic-h2-a4-unit-binding/attempt-01/execution-record.json)
has exit zero, empty stderr and exact input/source digests. No accepted
coefficient construction or verifier is repeated.

## 3. An eleven-generator polynomial presentation

Use the independently reviewed twelve-generator reduction and write

```
R=D_H Q,       M_ik=q_i r_k-q_k r_i,
B_ikl=det(rows i,k,l of [sQ,tQ,sR]).
```

Its twelve raw generators are Jnum*M56 and the eleven selected cubics
`B_i56 (i=0..4), B_i67 (i=0..5)`, on the candidate open
`(q5,q6)!=(0,0)`. Since

```
B_i67=-q6*M_i6,
delta^4*B_i67=3*Dnum*(Jnum*M_i6),                         (5)
```

the same localized ideal has the polynomial presentation

```
B_i56,          i=0,...,4,
Jnum*M_i6,      i=0,...,5.                               (6)
```

There are eleven polynomials. The case i=5 in the second group is the
previously separate Jnum*M56, so the twelfth generator is redundant.
The conversion uses only the common unit `3*Dnum/delta^4`. It keeps the
whole Jbar-zero locus and never cancels Jnum.

Equivalently the eleven cubic generators alone give the shared support
ideal after the stated localization. The compact polynomial second
group in (6) has lower degree than the cubic forms. These are equalities
of localized ideals over nonreduced coefficient rings, with the
candidate-open and actual-cover hypotheses preserved.

The full declared unit open for the finite inverse-map calculation may
therefore use delta, `Delta*K`, the exact-h2 cofactor determinant, and
Dnum. Projection admissibility and the original fiber conditions remain
necessary when interpreting a surviving parameter as an actual carrier.
This note supplies no emptiness certificate and makes no extension of
the rational inverse map onto its repeated-root denominator boundary.
