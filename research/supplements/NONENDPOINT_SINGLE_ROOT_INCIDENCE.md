# Nonendpoint single-root incidence and actual quotient fibers

Fix the embedded curve \(C_0=[s^4:s^3t:st^3:t^4]\), an algebraically closed characteristic-zero field, and the accepted anticanonical degree-five A4 pair \((S,c)\). Retain arbitrary \(\delta\ne0\), the four lift parameters \(a,b,g,d\), and an actual line center disjoint from \(S\), giving a finite birational projection \(\nu:S\to X\) onto an integral quintic. The restriction \(c\to C_0\) is an isomorphism. A hypothetical mate forces **full** reduced inverse support \((\nu^{-1}C_0)_{red}=c\), denoted SUP; it excludes isolated extra inverse points as well as extra curves. The proofs below concern this exact family, not every quintic carrier. The intrinsic pair is proved in [the A4 model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md); actual projection coordinates and every target boundary are in [the target-fiber chapter](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md). The common-root reductions below are necessary conditions and specified branch exclusions; they do not exhaust the full conductor incidence. L1 and L2 arise from different actual maps, and inverse-denominator/degree-drop boundaries are retained.

<a id="2026-10-13-session-nonendpoint-regular-l1-double-root"></a>

## The regular L1 double conductor root

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

Exact substitution into the two exact coefficient polynomials gives

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


<a id="2026-10-13-session-nonendpoint-single-root-quotient-fibers"></a>

## The two quotient fibers and the diagonal exception

### 1. Hypotheses and inherited actual fiber system

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

### 2. A linear/quadratic quotient and its normalized common-root norm

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

### 3. Solving the allowed diagonal exception without losing P6=0

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

### 4. L2 is a different, diagonal Jacobian factor

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
seven exact Taylor vanishing conditions still required. The reviewed geometric bridge at the end of this chapter excludes its regular L1!=0, L2=0, qZ(q)!=0 sole-root sublocus; it does not solve the entire incidence.

At `q=1`, the separate Taylor identity `F'(1)=-delta^7` already gives
an exact simple root without requiring (1). At `q=2`, the regular L1 quotient exception is impossible by S; the L2 branch is covered by the exact two-embedding field calculation in the reviewed bridge.
When `Pc=0`, L1 is nonzero but `Z(q)=0`; (2)--(11) are not used to
replace the denominator-free fiber equations on that stratum. The
other `Z(q)=0` component `U=0`, intrinsic A4 point and target infinity
likewise retain their separate exact fiber equations. The Z=0 boundary, J=0 and higher homogeneous gcd degree prevent a whole-locus conclusion.


<a id="2026-10-13-session-nonendpoint-single-root-taylor-incidence"></a>

## All Taylor coefficients and the target-zero stratum

### 1. Exact finite common-root parameters

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

### 2. All eight exact Taylor coefficients and the seven necessary equations

Let `F(p)` be the exact primitive conductor polynomial of degree at most
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

The exact checker verifies the automatic factor and the reconstruction
by all eight extracted coefficients. The expanded polynomial arrays
`u0,...,u7` are retained together, beginning with
[`u0`](../validation/2026-10-12-nonendpoint-single-root-taylor/20261013T142033115594Z/nonendpoint_single_root_u0.txt).
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

### 3. A compact first-coefficient factorization

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

### 4. The target-z=0 common-root stratum has a simple conductor zero

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


## Exact support and characteristic scope

The mathematical proofs above retain the actual homogeneous equations, local rings and nonreduced conductor membership used by the inherited independent reviews. Necessary exact computational support is retained in [verify_session_nonendpoint_regular_l1_double_root_2026_10_13.m2](../computations/verify_session_nonendpoint_regular_l1_double_root_2026_10_13.m2), [verify_session_nonendpoint_single_root_quotient_2026_10_13.m2](../computations/verify_session_nonendpoint_single_root_quotient_2026_10_13.m2), [verify_session_nonendpoint_single_root_taylor_2026_10_12.m2](../computations/verify_session_nonendpoint_single_root_taylor_2026_10_12.m2), [verify_session_nonendpoint_single_root_compact_first_coefficient_2026_10_13.m2](../computations/verify_session_nonendpoint_single_root_compact_first_coefficient_2026_10_13.m2). No inherited computation was rerun for this consolidation.

These conclusions are proved in characteristic zero for the specified admissible nonendpoint A4 normalization family. The finite local Nakayama and actual-module arguments are not themselves characteristic-zero-specific, but the displayed balanced frames, separable curve maps, coefficient inversions and nilpotent power-rigidity applications must retain their stated hypotheses. No positive-characteristic all-family exclusion is inferred. The fixed C0 has [a quartic-carrier construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).


## Reviewed geometric bridges for the regular sole-root branches

In the following inherited bridge notation, \(d=\delta\) is the nonzero modulus (not the fourth lift parameter), \(k=\kappa\), and \(f_i=[t^i]F(q+t)\). Thus \(f_1=u_0\), \(f_2=u_1\), and generally \(f_i=u_{i-1}\). The full regular-L2 source uses this local notation; the preceding sections retain the four lift parameters \(a,b,g,d\) and write the modulus as \(\delta\).


The preceding direct exact coefficient reductions do not solve a full parameter incidence. The following independent geometric arguments supply the additional full-support implications on the stated regular sole-root charts; other L2, Z=0, multi-root and Jbar-zero situations retain their explicit boundaries.

## 7. Regular L2: geometric elimination cover and retained exceptional loci

The owner L2 theorem asserts that, on the accepted finite common-root
incidence and regular chart `qZ(q)!=0`, with `L1!=0,L2=0`, the actual
Taylor coefficients f2,f3,f4,f5 cannot all vanish. Here

    Pc=q^2-6q+6, U=q(k-d)-d^2,
    D=2d(q-1)+q(q-2), E=d^2+d(3q-4)+q(q-2),
    Z(q)=q Pc U.

The exact coefficient identity
`partial_a f2=-(dq/2)L1 partial_k L2 (mod L2)` justifies solving for a
only where the L2 root is simple and L1 is nonzero. No original fiber
leading coefficient or unstated center parameter is divided out.

The finite cover is complete. q=1 is impossible because L2=d^5. q=2 is
handled by its two-embedding quadratic-field cover. Away from q=1,2,
the D=0 boundary makes L2 genuinely linear in k and is handled separately.
On D!=0, a discriminant-zero root has the displayed L1=0 value and lies
outside the new L1!=0 theorem. The remaining points have the algebraic
coordinate m in [the complete owner cover equations](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-13-generalization-quintic-l2). Both signs are covered because
the inverse formula determines m from the actual k; no chosen square-root
branch is lost. All rational-cover denominators are units under d,q,Pc,
q-1,q-2,D nonzero and m^2!=3.

The audit initially flagged the extra polynomial H removed from the f3
numerator. The owner now records the exact identity

    L1=-3m(q-2)Pc^2 H/
      [q^2(q-1)(m^2-3)^2(qm+3q-6)].

Consequently m and H are units on the retained L1!=0 chart. This repairs
the proof gap that would arise from removing H without this identity.
The three normalizations of f3,f4,f5 therefore preserve every candidate.
A common finite m root forces both fixed-degree resultants R34,R35 to
vanish. This implication is valid even when their m-leading degrees drop;
no converse resultant implication is being used.

The completed literal original-resultant witness combines R34,R35 to
`q^53(q-2)^44 Pc^69`, a unit on this chart. The completed D=0 witness
combines the original f3,f4 numerators to q^4. On D=0 the displayed a
coefficient can vanish only when L1 does, by the same derivative identity;
its additional quartic V is therefore not a missing a-solve stratum.
At q=2 the owner gives an original five-generator witness, over the exact
field QQ(mu), mu^2=3, for f2,f3,f4,f5 together with
`1-z*d*(d+2mu/3)`. Both embeddings apply to the characteristic-zero
algebraically closed ground field, so the two L2 roots are retained.
The inverse equation imposes precisely the stated d,L1 units.

The exact original-generator witnesses are retained in the [complete regular-L2 proof](QUINTIC_A4_CONDUCTOR_AND_SEXTIC_INCIDENCE.md#2026-10-13-generalization-quintic-l2). Its inputs, targets and coefficient columns are necessary support; a recorded gcd or saturated ideal printout alone is insufficient. The inherited independent review inspected their construction without presenting that as a fresh execution.

**Audit conclusion: the local regular-L2 theorem and its all-mate
single-root consequence are proved by the displayed cover and completed
literal owner certificates, within their precise scope.** The latter
consequence additionally needs Jbar nonzero and q to be the sole common
homogeneous conormal root. Then full support concentrates the actual
nonzero degree-eight binary section at q, forcing order eight, while
nonvanishing of at least one of f2 through f5 gives order at most five.
The regular-L1 geometric bridge is reviewed explicitly in section 8.

This does not prove an order bound on Z=0, target infinity, q=0, Jbar=0,
or the excluded L1 branch. It does not exclude several support points
sharing conductor degree eight. All those distinctions survive handoff.

The independent audit additionally verifies nine small rational-cover
identities directly, without loading F or an inherited source. They
include the compact discriminant, the cover equation and inverse, the
L1/H identity, the D factor, and the D=0 solve. On D=0 the exact relation
is `L1=-q(q-2)V/[8(q-1)]`, confirming directly that V=0 is the already
excluded L1=0 boundary. The original full L2 discriminant at q=2 is
48d^6; the normalized quadratic after removing 2d has discriminant 12d^4.
Either is nonzero for d nonzero. This clarifies an exponent slip in the
owner note without changing its conclusion. The [small rational-cover identity source](../validation/2026-10-14-quintic-independent-audit/l2-cover-algebra.m2) supplies the exact cover controls. The full original-generator Bezout witnesses remain in the linked owner proof; this small check does not replace them.

## 8. Independent review of the existing regular-L1 geometric bridge

The quotient-fiber identities above combine with the following finite-point reconstruction to prove the regular-L1 support implication. The exact coefficient check and double-root identity are inherited evidence, not fresh computations.

On `qZ(q)!=0`, the actual finite normalization-point reconstruction in
the accepted fiber model applies to common quotient roots. Put
`rho=d/q`. After removing the diagonal factors, the exact linear and
quadratic quotients are L and Q, with normalized quotient norm

    OffNorm=d^2 q^5 U^2 L1.

When Aq!=0, L is a genuine linear polynomial. On L1=0 its unique finite
root also solves Q. When Aq=0, the accepted cubic's quadratic coefficient
is `-q[3d^2q(2-q)]^2`, nonzero on this chart. Thus Q after diagonal
division is a genuine linear polynomial. Its leading coefficient is
nonzero, and OffNorm=0 forces the constant L to vanish identically; Q
still has a finite common root. This retains the leading drop rather
than mistaking a fixed-degree resultant factor Aq for a point.

Full inverse support forces every such root to equal rho; an off-diagonal
root reconstructs an actual normalization point outside c. It follows
that `L(rho)=Q(rho)=0`. A doubled or tripled fiber supported at rho is
allowed at this stage and is not excluded by saturation.

The exact equation `L(rho)=dq*S=0` excludes q=1,2 and gives
`k=d+d^2(2q-3)/[3(q-1)(q-2)]`. The exact Q(rho) equation then forces

    d=Pc(q-2)/[q(q-1)].

That last equation is used even when `P6=q^2-3q+3` vanishes and Aq=0.
The proof does not divide by P6, so this degree-drop component is retained.
The actual-section identity on these precise parameters is

    F(q+t)=f2*t^2+terms of degree at least three,
    f2=(q-2)^4 Pc^12/[9q^8(q-1)^8] != 0.

All factors in this expression are units under the stated chart and the
just-derived exclusions q=1,2. If Jbar!=0 and q is the sole common
homogeneous conormal root, the accepted support bridge requires the
nonzero degree-eight conductor form to be concentrated at q, hence to
have order eight. Its actual order two contradicts that requirement.

**Audit conclusion: the regular-L1 all-mate exclusion is now independently
accepted in exactly this sole-root, Jbar-nonzero, qZ-nonzero scope.** This
supplies the previously pending geometric premise needed for section 7's
combined regular sole-root theorem. No such conclusion is extended to
Z=0, other conormal roots, or an allowed A4 contribution when Jbar=0.
