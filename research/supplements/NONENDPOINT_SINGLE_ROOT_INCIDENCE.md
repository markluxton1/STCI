# Nonendpoint single-root incidence

Complete mathematical arguments and exact incidence calculations, with all hypotheses and limitations retained.

---

## 2026-10-13-session-nonendpoint-regular-l1-double-root

# The regular L1 rational branch has an exact double conductor root

Date: 2026-10-13. Author: `oct12_restricted_conductor_section/residual_norm_identity`.

Status: **DIRECT EXACT DOUBLE-ROOT IDENTITY FOR A SPECIFIED FAMILY;
INDEPENDENT AUDIT REQUESTED**. The actual-conductor identification is
inherited from the
[independent module audit](2026-10-12-session-conductor-quadric-module-independent-audit.md).
The separate quotient-fiber argument owns the claim that this rational
family is the surviving regular L1 branch under full inverse support.
No full common-root incidence exhaustion or global STCI result is claimed.
All older sources and notes remain unchanged.

Use the finite common-root parameters and exact coefficients of the
[Taylor incidence note](NONENDPOINT_SINGLE_ROOT_INCIDENCE.md#2026-10-13-session-nonendpoint-single-root-taylor-incidence):

    F(q+t)=t(u0+u1 t+...+u7 t^7),
    kappa=aq+B, Pc=q^2-6q+6.

Consider the explicit rational family

    delta=Pc(q-2)/[q(q-1)],
    kappa=delta+delta^2(2q-3)/[3(q-1)(q-2)],
    B=kappa-aq, G=Gs, J=Js,                         (1)

where Gs,Js are the complete common-root solutions in that note. Retain

    q(q-1)(q-2)Pc!=0.                              (2)

These are actual relations among projection parameters; delta is not
normalized to one. The conditions retain the modulus and every forbidden
denominator. They ensure delta is nonzero and the regular fiber denominator
does not vanish: on (1),

    U=q(kappa-delta)-delta^2
      =-delta^2 Pc/[3(q-1)(q-2)]!=0,
    Z(q)=q Pc U!=0.                                (3)

Exact substitution into the two frozen coefficient polynomials gives

    u0=0,
    u1=(q-2)^4 Pc^12/[9q^8(q-1)^8]!=0.              (4)

The second expression is independent of a. Its nonvanishing follows
from the explicitly retained factors (2); there is no numerical sampling
or Gröbner calculation. The underlying common-root substitution already
gives F(q)=0. Thus the actual conductor restriction has exactly order
two at q for every admissible projection in (1)--(2). This is a literal
coefficient calculation of its actual section, rather than a contact
bound inferred from a first-normal symbol.

In particular, if J!=0 and q is the sole common homogeneous conormal
root, full inverse support would force the entire degree-eight conductor
restriction to be supported at q. Its order two from (4) contradicts
that requirement. Hence the explicitly specified single-common-root
family cannot have a mate in any degree. Applying this consequence to
every regular L1 case also requires the separately justified quotient-
fiber necessity of (1), including its degree-drop case; that proof is
not replaced by this computation.

The [three-check source](../computations/verify_session_nonendpoint_regular_l1_double_root_2026_10_13.m2)
reads only the frozen u0,u1 polynomial artifacts and verifies both
identities (4) and the exact fiber-rank expression (3). It does not replay
the fifteen-check determinant source, the endpoint proof or the complete
Taylor expansion. Its
[20261013T142957009441Z captured run](../validation/2026-10-13-nonendpoint-regular-l1-taylor-branch/20261013T142957009441Z/execution-record.json)
has three supporting checks, a completion marker, exit zero and empty
stderr. Source SHA-256 is
`b223eb5e4e063bbbe3273ac4b82a2e98317412b5c92149fa692218180e217074`.

The earlier exploratory source evaluated u1,u2,u3,u7. It found (4),
and merely found the remaining displayed coefficients to be linear in
a after the same branch substitution. They are unnecessary for the
double-root obstruction and are retained as exploratory continuation
artifacts. That execution is not a parameter-space exhaustion.


---

## 2026-10-13-session-nonendpoint-single-root-quotient-fibers

# Actual quotient fibers separate the two first Taylor factors

Date: 2026-10-13. Author: `oct12_restricted_conductor_section`.

Status: **EXACT QUOTIENT IDENTITIES AND A STRUCTURAL NECESSARY BRANCH
REDUCTION; INDEPENDENT AUDIT REQUESTED**. This note uses the actual
nonendpoint genus-one quintic A4 model and the
[audited conductor theorem](2026-10-12-session-conductor-quadric-module-independent-audit.md).
It does not assert parameter-space exhaustion, a first-normal bound on
higher contact, a global quintic exclusion, or a universal STCI result.
All earlier frozen sources, notes and canonical records are unchanged.

## 1. Hypotheses and inherited actual fiber system

Work over an algebraically closed field of characteristic zero. Retain
`delta!=0`, the actual center-avoidance condition and finite birational
projection hypotheses of the audited model. Let `q!=0` be a finite
common conormal root, and impose the complete solutions `G=Gs,J=Js`
from the [Taylor incidence note](NONENDPOINT_SINGLE_ROOT_INCIDENCE.md#2026-10-13-session-nonendpoint-single-root-taylor-incidence):

    Gs=-(6B+delta^2-3delta)q-(3a-3B+2delta)q^2+2aq^3,
    2Js=-Gs(1+3q)-(6B+5delta^2-3delta)q
        -(3a+3B+delta-delta^2)q^2+(a+B)q^3.

These equations alone allow repeated and additional common roots. A
sole-common-root hypothesis is imposed explicitly only for the final
support-concentration consequence. Delta remains a parameter, not a
normalized constant.

For variable target `p`, use the actual target-fiber system of the
[diagonal norm note](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#4-nonendpoint-diagonal-norm-identity):

    Z=Gp(2-p)+J(3-p),
    A=(3delta^2+G)p(2-p)+J(3-p),
    b=delta[delta^2p(p-3)+3Bp(2-p)+G(2-p)-J],
    c=delta^2[Bp(p-3)-G],
    A2=A r^2+b r+c,
    N=delta^2(pr-delta)[3(2-p)r-delta(3-p)],
    M=delta^2[3Jr^2+delta(2G-J)r-delta^2G],
    Psi=p^2 Z^2 r^4+p^2 Z(2r^2+r-a)N+p^2 N^2-MZ,
    C3=Psi/(pr-delta).

The last division is an exact polynomial division. On `pZ!=0`, common
finite roots of `A2,C3` other than `r=delta/p` reconstruct actual points
of the normalization outside c mapping to the target curve point.
This actual reconstruction, rather than just a resultant vanishing,
is the support obstruction used below. The root `r=delta/p` is the
diagonal c point; double or triple fibers supported there are permitted
by full inverse support.

The present quotient argument applies to the regular chart

    qZ(q)!=0.                                            (1)

The intrinsic A4 target `q=0`, target infinity and the entire `Z(q)=0`
locus remain outside (1); they are not removed by saturation or declared
empty. The denominator-free original fiber equations govern them.

## 2. A linear/quadratic quotient and its normalized common-root norm

Write

    kappa=aq+B, Pc=q^2-6q+6, P6=q^2-3q+3,
    U=q(kappa-delta)-delta^2, rho=delta/q.

On the complete common-root incidence, the fiber polynomials have exact
diagonal factors:

    A2(r,q)=(r-rho)L(r),
    C3(r,q)=(r-rho)Q(r),                            (2)

where `L` has degree at most one and `Q` at most two. Put

    L=Aq r+l0, Q=q Aq^2 r^2+eQ r+fQ,
    Aq=A(q),
    OffNorm=Aq fQ-l0 eQ+q Aq l0^2.                  (3)

The exact identities are

    Res_r(L,Q)=Aq OffNorm,
    OffNorm=delta^2 q^5 U^2 L1,                    (4)
    Z(q)=q Pc U,
    Aq=q^2[(kappa-delta)Pc+delta^2(3-q)],

with the same first Taylor factor as the earlier coefficient note:

    L1=3kappa(q-1)^2 Pc+delta q(3-2q)Pc
       -3delta^2(q-1)^2(q-3).

The factor `Aq` in the fixed-degree resultant is a false leading-degree
factor. It is removed in `OffNorm`, not taken as evidence of an actual
extra point. Here is the degree-drop check, retained explicitly.

If `Aq!=0`, L is linear and (3) vanishes exactly when its unique finite
root also solves Q. If `Aq=0` on (1), the inherited actual cubic has
nonzero quadratic coefficient

    d=-q[3delta^2q(2-q)]^2.

Indeed `A(q)=0` and `Z(q)!=0` force `q!=2`. After dividing by the
diagonal factor, Q is a genuine linear polynomial with `eQ=d!=0`.
Then `OffNorm=-l0 eQ`; its vanishing says `l0=0`, so L is identically
zero and Q still has a finite root. If `l0!=0`, there is no common
finite root. Thus on (1), `L1=0` always produces an actual common finite
quotient root, including this leading-coefficient drop.

Under full inverse support, every such root must be the diagonal rho.
For `Aq!=0` this is the unique root of L; for `Aq=0` it is the unique
root of Q. Therefore the necessary conditions on the regular L1 branch
are

    L(rho)=Q(rho)=0.                                (5)

This does not prohibit doubled or tripled source fibers supported on c.
It only excludes the alternative actual point outside c.

## 3. Solving the allowed diagonal exception without losing P6=0

Set

    S=3(kappa-delta)(q-1)(q-2)+delta^2(3-2q),
    T(kappa)=6(kappa-delta)^2 q(q-1)(q-3)
              +delta(kappa-delta)q Pc
              -4delta^2(kappa-delta)(2q^2-6q+3)
              -delta^3 Pc+3delta^4(q-2).

Both quotient values in (5) have exact compact expressions:

    L(rho)=delta q S,
    Q(rho)=q^2 delta^2 Pc T(kappa).                 (6)

The first condition excludes `q=1` and `q=2`, because S there is,
respectively, `delta^2` and `-delta^2`. Since q is nonzero, (1) also
implies `Pc!=0` and `U!=0`. The remaining S equation solves as

    kappa=delta+delta^2(2q-3)/[3(q-1)(q-2)].         (7)

After precisely this substitution, the following identities hold:

    U=-delta^2 Pc/[3(q-1)(q-2)],
    Aq=-delta^2 q^3 P6/[3(q-1)(q-2)],
    L1=delta P6[Pc-delta q(q-1)/(q-2)],
    Q(rho)=delta^5 q^2 Pc^2/[3(q-1)(q-2)^2]
            *[delta q(q-1)-Pc(q-2)].               (8)

The last equation is essential. Using L1 alone would miss the
`P6=0`, hence `Aq=0`, degree-drop stratum. Conditions (5) and (8), with
the retained units, force in every case

    delta=Pc(q-2)/[q(q-1)],
    kappa=delta+delta^2(2q-3)/[3(q-1)(q-2)],
    q(q-1)(q-2)Pc!=0.                              (9)

When P6 vanishes, (8) still supplies the first relation in (9).
The quotient proof never divides by P6 or Aq. It permits that actual
double/triple diagonal fiber before using the conductor section.

The separate [exact double-root calculation](NONENDPOINT_SINGLE_ROOT_INCIDENCE.md#2026-10-13-session-nonendpoint-regular-l1-double-root)
substitutes (9) into the actual conductor restriction and proves

    F(q+t)=u1 t^2+terms of degree at least three,
    u1=(q-2)^4 Pc^12/[9q^8(q-1)^8]!=0.              (10)

Thus the actual section has order exactly two at q on the specified
family, independently of a. If `J!=0` and q is the sole common
homogeneous conormal root, full inverse support would require the
nonzero degree-eight conductor section to be supported only at q,
hence to have order eight there. Equations (9)--(10) contradict this.
Consequently, under these explicit hypotheses, the entire regular
L1 branch has no mate in any degree. This is an actual-section
multiplicity calculation, not a contact bound from first-normal data.
If J vanishes or further common roots occur, an allowed contribution
elsewhere remains possible and this support-concentration exclusion
does not apply.

## 4. L2 is a different, diagonal Jacobian factor

With G,J fixed at Gs,Js for the projection under consideration, take
partial derivatives in the variable target p, not in the parameter q.
Define the diagonal wedge

    W=(partial_r A2)(partial_p C3)
      -(partial_p A2)(partial_r C3), evaluated at (r,p)=(rho,q).

The exact identity is

    W=delta^5 Pc^2 L2,                              (11)

where

    L2=3q(q-1)[2delta(q-1)+q(q-2)]kappa^2
       -6delta q(q-1)[delta^2+delta(3q-4)+q(q-2)]kappa
       +delta^5q+3delta^4(q-1)(3q-2)
       +6delta^3q(q-1)(2q-3)+3delta^2q^2(q-1)(q-2).

The earlier literal Taylor identity is `F'(q)=-delta q L1 L2`.
On (1), L1 governs actual residual quotient roots through (4), whereas
L2 governs this diagonal wedge through (11). Their roles are different.
Vanishing of the wedge is not claimed to bound a later contact order
or to classify the whole remaining fiber. On the sole-common-root,
`J!=0` support problem, removal of regular L1 leaves `L2=0` with all
seven exact Taylor vanishing conditions still required. That incidence
is open.

At `q=1`, the separate Taylor identity `F'(1)=-delta^7` already gives
an exact simple root without requiring (1). At `q=2`, the regular L1
quotient exception is impossible by S, but the L2 branch remains.
When `Pc=0`, L1 is nonzero but `Z(q)=0`; (2)--(11) are not used to
replace the denominator-free fiber equations on that stratum. The
other `Z(q)=0` component `U=0`, intrinsic A4 point and target infinity
likewise remain separately recorded. These open cases, J=0 and higher
homogeneous gcd degree prevent a whole-locus conclusion.

## 5. Evidence and continuation bindings

The [eleven-check source](../computations/verify_session_nonendpoint_single_root_quotient_2026_10_13.m2)
has SHA-256
`52a9c7d479505b7d92e5aeb52e939cf2d6c88049b138eee96ec1651159bd1133`.
It loads the frozen actual conductor polynomial, constructs the
target-fiber pair and proves (2)--(4), (6)--(8), (11), as well as the
literal first Taylor factorization. Its
[20261013T142805543474Z captured execution](../validation/2026-10-13-nonendpoint-single-root-quotient/20261013T142805543474Z/execution-record.json)
has eleven supporting passes, a completion marker, exit zero and empty
stderr. Captured stdout SHA-256 is
`3b1174f808e02d235b6a14b7e0b2f82e9a4f6b1f257e33adab97d8177c485a68`.
It performs rational identities on the explicitly retained unit charts;
it contains no Gröbner parameter elimination or numerical sampling.

The exploratory predecessor has two source-version captures: the first
`20261013T142200484073Z` passed one identity before the protected M2 name
`poly` stopped execution; the renamed `quotientRing` version
`20261013T142216997848Z` passed four assertions and printed formulas.
Both source snapshots and raw outputs are retained in the same
validation lineage. The later eleven-check source is separate. The
fifteen-check norm, audited determinant and earlier endpoint sources
were not replayed or edited.

The branch necessity proved here binds the separate three-check
double-root source SHA-256
`b223eb5e4e063bbbe3273ac4b82a2e98317412b5c92149fa692218180e217074`,
its [20261013T142957009441Z execution](../validation/2026-10-13-nonendpoint-regular-l1-taylor-branch/20261013T142957009441Z/execution-record.json),
and owner note SHA-256
`01e8314753a1e3e058427d0d474a307c150153170862c74021193d2ca4151a03`.
That source proves (10) directly from frozen coefficient artifacts.

The highest-value continuation is the remaining regular L2 incidence:
reduce the next actual Taylor coefficients modulo its compact quadratic
in kappa while retaining coefficient drops, actual center admissibility,
the homogeneous sole-root condition and q=1,2 boundaries. No first-jet
argument should replace the actual higher coefficients. The Z=0 and
multi-root/J=0 support incidences require their own original fiber data.


---

## 2026-10-13-session-nonendpoint-single-root-taylor-incidence

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
[diagonal norm note](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#4-nonendpoint-diagonal-norm-identity).
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
