# The remaining Jbar-zero candidates have intrinsic conductor contact at most two

Date: 2026-10-14. Status: **ALL-PARAMETER CONTACT BOUND; independently
audited** in the
[new A4 contact review](2026-10-14-generalization-quintic-intrinsic-a4-contact-independent-audit.md).
The actual conductor octic and complete
intrinsic A4 target-fiber criterion are accepted inputs. The accepted
all-power exclusion of `G=Jbar=0` is used as a premise, without replaying
its proof. This note does not exclude all `Jbar=0` projections or all
quintic carriers.

## 1. Scope and intrinsic coefficient identities

Use the accepted nonendpoint genus-one quintic A4 normalization family,
with nonzero delta and an actual admissible finite birational projection.
Write `j=Jbar`, retain the actual parameters `a,B,G`, and let F be the
actual primitive conductor octic in target `p=delta/r`. The intrinsic
A4 point is p=0. A mate forces full inverse support, denoted SUP.

The new exact identities are

```
F(0)|_(j=0)=0,
[p]F|_(j=0)=-2 G (delta^2+2B+G)(3delta^2+G)^2,       (1)
[p^2]F|_(j=0,G=-3delta^2)=-108 delta^5(delta^2-B).    (2)
```

Only these two coefficients are needed; the conductor section is not
replaced by first-order normal data. The characteristic-zero scalar
constants and nonzero delta are retained.

The [new coefficient source](../computations/generalization_quintic_intrinsic_a4_contact_2026_10_14.m2)
reads the accepted actual primitive polynomial, extracts these coefficients,
and asserts the displayed literal identities. Its
[captured execution](../validation/2026-10-14-quintic-intrinsic-a4-contact/attempt-01/execution-record.json)
records input/source digests, exit zero and empty stderr. It does not
reconstruct the conductor determinant or replay an accepted verifier.

## 2. Exact A4 contact bound after the accepted G=j=0 closure

Put

```
D0=delta^2/2+B,       L=delta^2+2B+G=2D0+G.
```

The accepted A4 target-fiber criterion for j=0 gives an off-c inverse
point precisely when `D0!=0` and `G=-2D0`. Therefore, whenever j=0 and
G is nonzero, SUP forces

```
L != 0.                                                    (3)
```

Indeed L=0 would give `D0=-G/2!=0` and exactly that forbidden inverse
point. This uses the actual fiber criterion with its nonzero denominator;
the D0=0 exception is not discarded.

Assume j=0 and G is nonzero. If `G+3delta^2!=0`, identity (1) and (3)
give exact conductor contact one at A4. If `G=-3delta^2`, (1) vanishes.
SUP and (3) then force `B!=delta^2`, since B=delta^2 would make L=0.
Identity (2) is consequently nonzero, so the contact is exactly two.
Thus

```
j=0, G!=0, SUP  ==>  ord_A4(F) is exactly 1 or 2.            (4)
```

The accepted theorem already excludes mates on G=j=0. Consequently
**every surviving j=0 mate candidate has intrinsic conductor contact at
most two**. This new argument does not analyze SUP on G=0; that lane is
removed by its separate accepted mate-exclusion proof.

This is one intrinsic contact argument across the whole parameter family.
It is independent of the degree of the common first-symbol gcd and does
not enumerate conductor multiplicity partitions.

## 3. Both values of Jbar satisfy the same h2 norm condition

On the actual h2 locus, the independently reviewed
[conductor--differential factor theorem](2026-10-14-generalization-quintic-h2-conductor-quotient.md)
gives homogeneous `Fsrc=H Q6` in source coordinates `x=T/S=r/delta`.
The intrinsic point is `S=0`. If H contains that point, the accepted
leading-coefficient equations give G=j=0. That entire mate lane is already
closed. Thus every surviving h2 candidate has H(A4) nonzero.

If j is nonzero, SUP requires Q6 to be supported on H, so necessarily
`Res(H,Q6)=0`.

If j=0 and `Res(H,Q6)!=0`, the permitted support of Q6 consists only
of the additional A4 point. Since Q6 is a nonzero degree-six binary form,

```
Q6 = constant*S^6.
```

As H misses A4, this would give conductor contact exactly six at A4,
contradicting (4). Therefore every surviving h2 mate candidate, for either
value of j, satisfies the single homogeneous necessary condition

```
Res(H,Q6)=0.                                               (5)
```

This removes the pure-A4 exception from the small quadratic-algebra norm
test. On the declared finite inverse-map chart, the saved exact norm
factorization then imposes `N12*N18=0` for j=0 as well as j nonzero.
All denominator, content and actual-projection hypotheses of that capture
remain in force. This is a necessary two-factor incidence, not an
emptiness certificate. The repeated-root and projective infinity charts
remain in the shared homogeneous sextic support system; no inverse
discriminant is used in the proof of (5).
