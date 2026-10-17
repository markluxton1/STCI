# A finite common-root Taylor incidence and a simple-root exclusion

Date: 2026-10-13; computation began 2026-10-12.
Author: `oct12_restricted_conductor_section/residual_norm_identity`.

Status: **DIRECT EXACT COEFFICIENT REDUCTION; INDEPENDENT AUDIT REQUESTED**.
The geometric use below depends on the
[audited actual conductor quadric](2026-10-12-session-conductor-quadric-module-independent-audit.md).
This is a necessary incidence, not an exhaustion, a sufficient condition,
or an all-quintic theorem. Delta remains a genuine parameter. Older norm,
determinant, endpoint, captured and canonical records are unchanged.

## 1. Exact finite common-root parameters

Use `B=b-a`, `G=g-3b+2a`, `J=d-2g+2b-a`, with `delta!=0`,
in characteristic zero. The conormal polynomials in the target coordinate
`p=1-z` are

    Pt=G+(6B+delta^2-3delta)p+(3a-3B+2delta)p^2-2ap^3,
    Jt=G+2J+(6B+3G+5delta^2-3delta)p
       +(3a+3B+delta-delta^2)p^2-(a+B)p^3.

They are the corrected cubic pair after the regular finite-target
normalization described in the
[diagonal norm note](2026-10-12-session-nonendpoint-diagonal-norm-identity.md).
Let `q!=0` be a specified finite common root. The complete equations
`Pt(q)=Jt(q)=0` solve without any further division as

    Gs=-(6B+delta^2-3delta)q-(3a-3B+2delta)q^2+2aq^3,
    2Js=-Gs(1+3q)-(6B+5delta^2-3delta)q
        -(3a+3B+delta-delta^2)q^2+(a+B)q^3.          (1)

This incidence includes repeated common roots and further common roots;
it does not silently impose homogeneous gcd degree one. The target
`q=0` is the intrinsic A4 point and is treated in the earlier conductor
records. Target infinity is likewise a separate common-root stratum.

Write `kappa=aq+B`, `Pq=q^2-6q+6`, and

    U=q(kappa-delta)-delta^2.

The regular fiber denominator and the two diagonal rank coefficients
specialize exactly to

    Z(q)=q Pq U,
    H12(delta/q,q)=-(3-2q)U,
    H13(delta/q,q)=q(4-3q)U.                         (2)

Thus the regular Cramer chart `qZ(q)!=0` additionally requires `Pq U!=0`.
The exceptional strata `Pq=0` and `U=0` are explicitly retained. On
`U=0`, both displayed rank coefficients vanish and the exact remaining
fiber equation on the diagonal is `qT^2=0`; the doubled source fiber
is allowed by full inverse support. It is not removed by saturation.

## 2. All eight exact Taylor coefficients and the seven necessary equations

Let `F(p)` be the frozen primitive conductor polynomial of degree at most
eight, defined by the compact norm identity and identified with the
actual conductor restriction by the separate module audit. Write

    F(p)=sum_(n=0)^8 f_n(delta,a,B,G,J)p^n,
    Fstar(q+t)=F(q+t)|_(G=Gs,J=Js).

There is the exact automatic factor

    Fstar(q+t)=t*(u0+u1 t+u2 t^2+u3 t^3
                 +u4 t^4+u5 t^5+u6 t^6+u7 t^7),     (3)

where the compact, complete definition of the eight polynomials is

    u_i=sum_(n=i+1)^8 binomial(n,i+1)q^(n-i-1)
                         f_n(delta,a,B,Gs,Js), i=0,...,7.  (4)

The captured checker verifies the automatic factor and the reconstruction
by all eight extracted coefficients. Expanded polynomial artifacts
`u0,...,u7` are preserved with individual hashes in the successful
[coefficient capture](../validation/2026-10-12-nonendpoint-single-root-taylor/20261013T142033115594Z/coefficient-artifacts.json).
They have respectively 196,230,210,199,166,133,96,61 monomials before the
change from `B` to `kappa` (the counts are descriptive and do not prove
independence of the equations).

Now impose actual projection-center avoidance, `J=Js!=0`, full inverse
support, and that the specified finite root q is the only common
homogeneous conormal root. This includes the intended gcd-degree-one
stratum, but does not assert that (1) alone enforces it. The normalization
is a local isomorphism on c away from q under these hypotheses, including
at the A4 point because J is nonzero. Hence the actual degree-eight
conductor restriction is supported only at q. Its section is nonzero,
and therefore

    u0=u1=u2=u3=u4=u5=u6=0, u7!=0.                  (5)

These are seven explicit necessary polynomial equations in the four
parameters `delta,a,B,q`, with retained nonvanishing and actual
admissibility conditions. No Gröbner elimination, existence, emptiness
or parameter-space exhaustion of (5) is asserted here. The upper
coefficients u7,u6,u5 have no generic nonconstant factor in the initial
exact factor output; that observation supplies no exclusion on its own.

## 3. A compact first-coefficient factorization

The first of (5) has a much smaller structural expression:

    u0=-delta q L1 L2,                              (6)

with

    L1=3kappa(q-1)^2 Pq+delta q(3-2q)Pq
       -3delta^2(q-1)^2(q-3),

    L2=3q(q-1)[2delta(q-1)+q(q-2)]kappa^2
       -6delta q(q-1)[delta^2+delta(3q-4)+q(q-2)]kappa
       +delta^5q+3delta^4(q-1)(3q-2)
       +6delta^3q(q-1)(2q-3)+3delta^2q^2(q-1)(q-2).

Both factors depend only on `delta,q,kappa`; in particular L2 has no
separate dependence on a after this coordinate change. It is a quadratic
in kappa. The resulting necessary union is `L1=0` or `L2=0`.
Its geometric branches are not classified by this coefficient alone.

When `q!=1` and `Pq!=0`, the first branch permits an exact linear solve

    kappa=delta^2(q-3)/Pq
          -delta q(3-2q)/(3(q-1)^2).                (7)

The exceptional values cannot be discarded from (7):

* At `q=1`, `L1=delta` and `L2=delta^5`.
* At `Pq=0`, `L1=-3delta^2(q-1)^2(q-3)` is nonzero,
  because these two roots are neither 1 nor 3. Thus (5) requires L2=0
  on this stratum. Here `Z(q)=0`; the original rank equations apply.

For continuation, the exact representative of L2 modulo Pq is preserved
in the supplemental capture. In grouped form it is

    L2 mod Pq = q*[delta^5+39delta^4+198delta^3+198delta^2
                  -(30delta^3+312delta^2+396delta)kappa
                  +(114delta+198)kappa^2]
                -48delta^4-252delta^3-252delta^2
                +(36delta^3+396delta^2+504delta)kappa
                -(144delta+252)kappa^2.             (8)

## 4. The target-z=0 common-root stratum has a simple conductor zero

At `q=1`, equations (3) and (6) give the universal exact identities

    Fstar(1)=0, Fstar'(1)=-delta^7!=0.               (9)

Thus the actual conductor restriction has exactly a simple zero at this
target on every admissible projection satisfying the common-root
equations (1). This statement uses the actual section and its derivative,
rather than inferring a conductor-length bound from its first symbol.
It is valid even if there are additional common conormal roots.

Consequently an admissible projection with `J!=0` and sole common
homogeneous conormal root `q=1` cannot have full inverse support: that
root has length one while the total conductor restriction has degree
eight. This excludes the stated single-root subfamily in every mate
degree. It does not exclude the same q=1 incidence with another common
root or with an allowed A4 contribution when J=0.

## 5. Evidence inventory and failure shields

There are two separate source lineages; neither is a global incidence
solver or an independent proof of the conductor module theorem.

The [eight-check source](../computations/verify_session_nonendpoint_single_root_taylor_2026_10_12.m2)
has final SHA-256 `b5bd8a304dbc5acc6767e364088e25deac1af89d78766f38263c6bb8441dfbc1`.
Its captured [20261013T142033115594Z execution](../validation/2026-10-12-nonendpoint-single-root-taylor/20261013T142033115594Z/execution-record.json)
passed eight supporting identities plus a completion marker, exit zero,
empty stderr. The earlier 20261012T213559186745Z execution passed only
the first two identities before M2 rejected `sum` on a Sequence; its
actual failed source and raw outputs are retained. Converting the
sequence to a list repaired the interface. A separate exploratory
20261012T213307390552Z capture expanded and factored all coefficients
successfully but did not contain the eight-check assertions.

The [four-check compact-factor source](../computations/verify_session_nonendpoint_single_root_compact_first_coefficient_2026_10_13.m2)
has final SHA-256 `7ee03582fa3836ae08ed3020e4b21f31b77e641c4e210a0307353853d34f01fb`.
Its captured [20261013T142344895262Z execution](../validation/2026-10-13-nonendpoint-single-root-first-coefficient/20261013T142344895262Z/execution-record.json)
passed four identities plus a completion marker, exit zero, empty stderr.
The earlier 20261013T142251479590Z source lacked parentheses around
the multiline L2 expression. M2 completed the first-line assignment
and evaluated the later lines separately, causing the first assertion
to fail. That source and raw failure remain captured. A diagnostic
execution printed the missing lower coefficients; its retained source
is debugging history, with no original raw-output disk certificate.
Parenthesizing the complete expression repaired this parse error.

The endpoint and fifteen-check norm proofs were not replayed. No
parameter-stratum exhaustion, global nonendpoint exclusion, upper degree
bound, first-normal bound on higher contact, or universal STCI claim
is drawn from these coefficient checks.
