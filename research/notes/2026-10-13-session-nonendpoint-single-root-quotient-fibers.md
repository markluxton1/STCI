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
from the [Taylor incidence note](2026-10-13-session-nonendpoint-single-root-taylor-incidence.md):

    Gs=-(6B+delta^2-3delta)q-(3a-3B+2delta)q^2+2aq^3,
    2Js=-Gs(1+3q)-(6B+5delta^2-3delta)q
        -(3a+3B+delta-delta^2)q^2+(a+B)q^3.

These equations alone allow repeated and additional common roots. A
sole-common-root hypothesis is imposed explicitly only for the final
support-concentration consequence. Delta remains a parameter, not a
normalized constant.

For variable target `p`, use the actual target-fiber system of the
[diagonal norm note](2026-10-12-session-nonendpoint-diagonal-norm-identity.md):

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

The separate [exact double-root calculation](2026-10-13-session-nonendpoint-regular-l1-double-root.md)
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
