# Nonendpoint quintic: target fibers and full-support obstructions

Permanent complete mathematical dossier, including projective boundary conditions, denominator-free fiber equations, exact root and rank cases, and bounded all-degree consequences. All conditional hypotheses and failure modes are preserved.

---

## 1. nonendpoint conductor infinity coefficient

# A simple conductor-root coefficient at target infinity

Date: 2026-10-12. Author: `oct12_restricted_conductor_section/residual_norm_identity`.

Status: **EXACT COEFFICIENT IDENTITY, WITH A CAPTURED STANDARD-LIBRARY CHECK**.
The auxiliary [diagonal norm note](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#4-nonendpoint-diagonal-norm-identity)
and its fifteen-check source remain frozen. No previously sealed file or
canonical summary is edited here.

Let `F(p)` be the exact polynomial bound in that note and put `a=B=0`.
Direct coefficient extraction gives, for every `delta,G,J`,

    coefficient_(p^8) F=0,
    coefficient_(p^7) F=delta^7.                    (1)

Since `delta!=0`, homogenization of `F` to degree eight has exactly a
simple zero at `p=infinity`. This uses the literal section, not an
upper bound inferred from its first-normal zero locus.

The [new coefficient checker](../computations/verify_session_nonendpoint_conductor_infinity_coefficient_2026_10_12.py)
reads the frozen 344-monomial primitive polynomial, validates its exact
SHA-256, and reconstructs it through elementary integer polynomial
arithmetic using Python's standard library. It performs no `eval`, uses
no CAS dependency, and does not replay the fifteen-check M2 source.
The [captured run](../validation/2026-10-12-nonendpoint-conductor-infinity-coefficient/20261012T213137628207Z/execution-record.json)
records the source, input and raw-output hashes and passed with exit
code zero and empty stderr.

The following geometric consequence depends on the separate
[restricted-conductor determinant argument](NONENDPOINT_CONORMAL_AND_CONDUCTOR_MODULES.md#2-nonendpoint-restricted-conductor-determinant).
Its independent mathematical audit is ongoing at this note's freeze.
Once that argument identifies `F` with a unit multiple of the actual
degree-eight conductor restriction, its zero at target infinity has
exactly length one on every admissible projection with `a=B=0`.
The conormal cubics already have a common root at that endpoint, because
their constants vanish there (`a=b=0`). Under full inverse support all
other conductor zeros must be supported at another common conormal
root, or at the A4 point if `J=0`.

In particular, with `J!=0`, a parameter value for which the sole common
conormal root is target infinity cannot have full inverse support:
that point has length one while the total conductor restriction has
degree eight. This is conditional on the actual-conductor geometric
bridge, rather than inferred solely from a polynomial degree match.
It is not a full common-root incidence exclusion or a universal STCI
statement.


---

## 2. nonendpoint GJ zero full support exclusion

# Nonendpoint quintics with G=J=0: complete inverse-support exclusion

Date: 2026-10-12. Author: `oct11_endpoint_a_nonzero_support/a_nonzero_local_excess`.
Status: **COMPLETE BOUNDED PROOF PROPOSED; EXACT POLYNOMIAL
CERTIFICATES CAPTURED; pending independent geometric audit**.
This note excludes the entire displayed G=J=0 nonendpoint subfamily
in every mate degree. The unrestricted nonendpoint family, the other
quintic normalization strata and the universal STCI problem remain open.
No canonical, previously sealed, or frozen owner file is edited.

## 1. Claim and actual geometric scope

Work over an algebraically closed field of characteristic zero. Use the
actual intrinsic pair and nonendpoint sections in the
[target-fiber reduction](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md#4-nonendpoint-target-fiber-reduction-and-bounded-exclusions),
Sections 1--3. That note is frozen during its separate audit; this is a
new continuation beyond its explicitly open G=J=0 lead.

On the complete open S minus ell=A2(r,T), put

    U3=r^3-rT,
    U4=r^4-(2r^2+r)T+T^2,
    B=b-a, G=g-3b+2a, J=d-2g+2b-a.

The nonzero modulus delta is retained. In the subfamily G=J=0 the actual
four sections are

    X0=U4+aT,
    X1=U4-delta U3+(a+B)T,
    X2=U4-3delta U3+3delta^2r^2-delta^3r+(a+3B)T,
    X3=U4-4delta U3+6delta^2r^2-4delta^3r+delta^4+(a+4B)T.

Assume that the projection center is disjoint from S. The lifted curve
c is T=0; its target is fixed C0=[1:z:z^3:z^4], with
z=(r-delta)/r. The intrinsic A4 point is the missing c-point r=infinity
and has target z=1. Every off-c point mapping to C0 lies in the displayed
affine chart: finite ell-points have quadric value -3delta^2 and the
remaining ell-point is A4 on c. These are the verified projective-chart
facts from the preceding reduction, Section 2.

**Claim.** For every a,B and nonzero delta in this subfamily, under center
avoidance there is an actual point off c mapping to C0. Hence
(pi^{-1}(C0))_red=c cannot hold. The full-support theorem imported in the
[quintic structural frontier](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-11-session-quintic-structural-frontiermd),
Section 1, makes that equality necessary for a mate, so this is an
all-mate-degree exclusion in the stated normalization/projection lane.

If B=0, the claim is already proved in Section 9 of the frozen reduction:
it is the complete a=b=g=d subfamily. Thus it remains to prove the claim
for B!=0. No division by B in this note silently discards that case.

## 2. The doubled c-fiber forces a unique lift parameter

Suppose for contradiction that the projection has full inverse support.
Set

    k=B/delta^2,                     k!=0.

Use p=1-z for finite targets. The exact three linear target constraints
and actual normalization equation are

    F1=delta r^3-(delta r+B)T-p lambda=0,
    F2=3delta^2r^2-delta^3r-p^2(3-p)lambda=0,
    F3=delta^4-2delta^3r+p^3(2-p)lambda=0,
    X0=lambda.

For p!=0, eliminating only lambda gives the denominator-free system in
Section 4 of the frozen reduction. Its final equation is

    J0=pT^2+[delta r+B-p(2r^2+r-a)]T+r^3(pr-delta)=0.

At the actual c-point

    p_c=-1/k,       r_c=delta/p_c=-k delta,

the two linear T-coefficients H12,H13 vanish, as do their constant terms.
The remaining equation is exactly

    T*[p_c T+p_c a+B-delta-delta^2/p_c]=0.

If the bracket's constant coefficient is nonzero, its second root gives
an actual off-c point above that finite target; center avoidance forbids
lambda=0. Thus full support forces

    a=2k^2 delta^2-k delta
     =2B^2/delta^2-B/delta.                  (1)

With (1), this exceptional c-fiber is the doubled T=0 fiber. It is
retained, rather than erroneously excluded by a first-normal argument.

## 3. Target infinity forbids a quintic degree drop

The target z=infinity requires X0=X1=X2=0. For a nonzero r, solving the
first actual coordinate difference gives

    T=delta r^3/(delta r+B).

The remaining equations are the exact polynomials from Section 8 of the
frozen reduction,

    Pinf=-delta^2r^2+(B^2-delta B+a delta^2)r+a delta B,
    Qinf=3delta^2r^2+(3delta B-delta^3)r-delta^2 B.

After substituting B=k delta^2 and (1), they satisfy

    Qinf=3delta^2(r+k delta)(r-delta/3),
    Pinf(-k delta)=-k^3 delta^5!=0,
    Pinf(delta/3)=-delta^4 L/9,
    L=(1+3k)^2-9delta k^2(1+2k).             (2)

The r=-k delta value has denominator zero and is explicitly impossible.
At r=delta/3 the denominator is delta^2(k+1/3). If it vanished,
k=-1/3 and L=-delta/3!=0. Therefore L=0 gives r=delta/3 with a nonzero
denominator, and its T is nonzero. It is an actual off-c inverse point
at infinity; center avoidance supplies X3!=0. Consequently a hypothetical
full-support projection must satisfy

    L!=0.                                  (3)

This handles the projective leading-coefficient boundary before any
root-count argument. It is not an assumed generic degree condition.

## 4. A compact actual off-c branch and its quintic equation

For p!=0,2 define

    P6=p^2-3p+3,        Pc=p^2-6p+6,
    E=(1+3k)p-3-6k,
    E_s=delta^2(3-p)+3B(2-p)=-delta^2 E,
    r_s=delta(3-p)/(3(2-p)),
    lambda_s=delta^4/[3p^2(2-p)^2].

If E!=0, define

    T_s=delta^2 P6 Pc/[9p(2-p)^2 E]
       =-delta^4 P6 Pc/[9p(2-p)^2 E_s].

Direct substitution in the actual F1,F2,F3 gives zero identically. The
remaining normalization equation, retaining T^2 and the actual forced a,
is the exact identity

    X0(r_s,T_s)-lambda_s
       =delta^3 Pc W(p)/[27p^2(2-p)^3 E^2],                 (4)

where the compact degree-at-most-five polynomial is

    W(p)=p P6 E^2
          -9delta(p-2)(k p^2-2kp-1)
             *(2k^2p^2-6k^2p+kp^2+6k^2-4kp+6k+1).       (5)

Its leading coefficient is exactly L from (2), and W(2)=2. Thus (3)
makes W a polynomial of degree exactly five. The exact source verifies
the actual three constraints and (4), rather than merely a formal
elimination numerator or a first transverse jet.

## 5. Every W-root lies among three retained exceptional targets

We prove that full support forces every W-root into

    {0,rho_plus,rho_minus},
    rho_plus=3+sqrt(3), rho_minus=3-sqrt(3).                (6)

These are p=0 and the two distinct Pc-roots. The p=0 value is the actual
intrinsic-A4 target z=1 and is deliberately retained. We do not assert
that all three targets are individually allowed; an enlarged necessary
root set suffices for the contradiction below.

Let p0 be a root of W outside (6). It is not 2, by W(2)=2. First suppose
E(p0)!=0. Then (4) gives X0=lambda_s. If P6(p0)!=0, the displayed T_s
is nonzero, while lambda_s is also nonzero, so this is an actual off-c
inverse point and contradicts full support.

If P6(p0)=0 instead, T_s=0. Since Pc(p0)!=0, the exact identity

    p(3-p)-3(2-p)=-Pc

shows r_s!=delta/p. Yet the three constraints and X0=lambda_s!=0 would
make that actual c-point r_s map to z=1-p. The embedded curve c has
the injective target parameter z=(r-delta)/r, forcing r_s=delta/p.
This is a contradiction. Thus a P6-root with E!=0 cannot be a W-root.

It remains to retain, rather than divide away, E(p0)=0. The polynomial
identity

    3(2-p)W-delta P6^2 Pc is divisible by E                 (7)

is checked exactly. Since p0!=2, delta!=0 and Pc(p0)!=0, (7) and
W(p0)=0 force P6(p0)=0. At a P6-root the displayed r_s is also

    r_s=delta/(3-p).

Moreover delta r_s+B=E_s/[3(2-p)]=0, so H12=H13=0 at that actual
point. Both remaining linear-equation constants vanish: this is the
second rank-one compatible fiber from Section 6 of the frozen reduction.
It is distinct from r=delta/p because Pc and P6 have no common root.
The actual J0 equation there is a quadratic in T with leading p!=0
and constant r_s^3(pr_s-delta)!=0. It has a nonzero T-root in the
algebraically closed field. Center avoidance makes the reconstructed
lambda nonzero. This is another actual off-c inverse point.

Every E-zero W-root outside (6) has therefore been settled by its actual
fiber, and no exceptional denominator remains. This proves (6). The
argument also allows p=3 and k=-1/3 whenever their actual formulas do;
neither is deleted by an auxiliary saturation.

## 6. Twenty-one complete coefficient profiles have polynomial unit certificates

Over the algebraically closed characteristic-zero field choose s with
s^2=3 and set rho_plus=3+s,rho_minus=3-s. From degree five, leading
coefficient L!=0 and (6), there are nonnegative integers i,j,h such that

    i+j+h=5,
    W(p)=L p^i(p-(3+s))^j(p-(3-s))^h.                     (8)

There are exactly twenty-one such triples. All multiplicities, including
every possible order at p=0, are retained. Write c_t=[p^t]W and let
q_t^{i,j,h} be the corresponding coefficient of the monic profile on
the right of (8). Its leading coefficient is one, so (8) is exactly the
following five coefficient equations, with no missing sixth equation:

    f_t^{i,j,h}=c_t-L q_t^{i,j,h}=0,       t=0,1,2,3,4.   (9)

For each of the twenty-one triples the captured exact source constructs
five polynomials b_t^{i,j,h} in QQ(s)[k,delta] satisfying

    sum_(t=0)^4 f_t^{i,j,h} b_t^{i,j,h}=1.                (10)

The source multiplies the five-generator row by its certificate column
and asserts equality to the actual constant matrix {{1}} in each case.
Every certificate is printed in full in the
[certificate artifact](../validation/2026-10-12-nonendpoint-GJ-zero-normalized-lead/twenty-one-polynomial-bezout-certificates.txt).
The final identities require no saturation or inverse parameter. They
are polynomial identities in k,delta, with only constant coefficients
in the number field QQ(s), and therefore remain true after embedding
that field into any algebraically closed characteristic-zero field.
Swapping the choice of s merely swaps j,h in the exhaustive list.

For example, the profile (i,j,h)=(0,0,5) has certificate

    (s/9+1/2, 2s/9+1, 4s/9+2, 2s/3+4, 2s/3+8).

The five symmetric exceptional profiles also have explicit polynomial
certificates, not solely unit Groebner-basis output. For (5,0,0) one is

    b0=-32k delta^2/9-26delta^2/9+44k/9+34delta/9+49/18,
    b1=-52delta^2/9+16k/3+8delta/3+37/9,
    b2=-8delta^2+8k/3+4delta/3+10/3,
    b3=-16delta^2/3+4/3,       b4=0.

Thus every one of (9)'s systems is impossible. This contradicts the
root factorization (8), proving that full support is impossible for
B!=0,G=J=0. Together with the previously proved B=0 case, it proves
the stated complete G=J=0 subfamily exclusion.

## 7. Evidence, failures, and continuation boundary

The [exact supporting source](../computations/verify_session_nonendpoint_GJ_zero_profile_exclusion_2026_10_12.m2)
passes ten structural check groups and twenty-one direct polynomial
Bezout identity checks. Its SHA256 is

    44d3b193783dc76562febe23af452a5b863b65b5f992dc6b1f83fad4a0c8fc33.

The [execution record](../validation/2026-10-12-nonendpoint-GJ-zero-normalized-lead/execution-record.json)
captures the copied final source, exact command, exit zero, raw stdout,
raw stderr, source/output hashes, and the twenty-one certificate vectors.
The certificate artifact's SHA256 is

    46e1c3daa4c1b927a91bb65c747775de243533d4c6dc98b9562324fbb99aa304.

Seven failed source versions are retained with re-executed raw errors:
an exploratory ring-variable coefficient export, reserved profile syntax,
Sequence/List concatenation, unsupported lift(Matrix,Matrix), fraction-
field coefficient extraction, multivariate rather than univariate
coefficient extraction, and a protected dd variable. Three successful
exploratory sources are separately captured: normalization factorization,
the original saturated twenty-one profile search, and inverse-variable
certificate construction whose inverse-variable coefficients all vanish.
There are eleven recorded executions but only one accepted mathematical
checker source; replay and exploratory counts do not enlarge the scope.

This proof controls actual inverse fibers and every exceptional target
needed by its root cover. It uses no generic-rank exhaustion claim and
no first-normal bound on higher contact. The remaining nonendpoint
frontier includes G or J nonzero, especially the homogeneous conormal-
resultant boundary identified separately by root. This result does not
exclude those strata, all genus-one quintics, or unrestricted STCI.


---

## 3. nonendpoint GJ zero full support independent audit

# Independent audit: nonendpoint G=J=0 full-support exclusion

Date of mathematical checks: 2026-10-12. Final audit saved: 2026-10-13.
Auditor: `oct11_endpoint_support_global_audit/two_root_contact_audit`.
Status: **PASS: geometric root cover and direct exact polynomial certificates**.

This audits the frozen [owner proof](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md#2-nonendpoint-gj-zero-full-support-exclusion), SHA256
`9a3532827eaf3c45efcbf9759681d7070045923465710b19d06efc4799a06d33`.
No correction to its mathematical claim is required. The result excludes the
whole displayed `G=J=0` nonendpoint projection subfamily in every mate degree.
The unrestricted nonendpoint family and the universal STCI problem remain open.

## 1. Scope and geometric inputs

Work with fixed `C0=[1:z:z^3:z^4]` over an algebraically closed field of
characteristic zero, in the accepted intrinsic A4 quintic model. Retain
`delta!=0` and require the projection center to avoid the intrinsic surface
`S`. Here `B=b-a`, `G=g-3b+2a`, and `J=d-2g+2b-a`; this `J` is the lift
parameter, also denoted `Jbar`, rather than the first-normal cubic numerator.

The [target-fiber reduction](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md#4-nonendpoint-target-fiber-reduction-and-bounded-exclusions)
supplies the complete affine chart `S minus ell=A2(r,T)`, the actual sections
`X0,...,X3`, and the embedded curve `c:T=0`, with parameter
`z=(r-delta)/r`. The missing `r=infinity` point is the intrinsic A4 point
on `c`, mapping to `z=1`. Finite points of `ell` have quadric value
`-3delta^2`, so cannot give off-`c` inverse points of `C0`; the remaining
point of `ell` is the A4 point. Thus every possible off-`c` inverse point
is covered by the displayed affine chart, including inverse points at
target infinity. These previously audited chart facts are necessary here.

The accepted quintic full-support theorem makes
`(pi^{-1}(C0))_red=c` necessary for every mate degree. The argument below
contradicts that condition using actual fibers, including the quadratic
transverse term `T^2`. It uses no first-normal length bound. The case
`B=0`, namely `a=b=g=d`, is already excluded in Section 9 of the target-fiber
reduction and its [independent audit](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md#5-nonendpoint-target-fiber-independent-proof-audit).
The new argument therefore treats `B!=0` without losing the `B=0` case.

## 2. The forced parameter and the projective degree boundary

Put `k=B/delta^2!=0` and `p=1-z`. For a finite target, the exact equations,
with the actual normalization scalar `lambda=X0`, are

```text
F1 = delta r^3-(delta r+B)T-p lambda = 0,
F2 = 3delta^2 r^2-delta^3 r-p^2(3-p)lambda = 0,
F3 = delta^4-2delta^3 r+p^3(2-p)lambda = 0,
X0 = lambda.
```

These are invertible linear combinations of the actual target equations.
If the equations held with `lambda=0`, all four sections would vanish,
contrary to center avoidance. Thus reconstructing a solution of these
equations cannot produce a spurious projective point with zero coordinates.

At `p_c=-1/k`, `r_c=-k delta`, the two linear transverse constraints
become compatible and the remaining equation is exactly

```text
T*(p_c T+p_c a+B-delta-delta^2/p_c)=0.
```

Its reconstructed scalar is `lambda=k^4 delta^4!=0`, independently of `T`.
A nonzero second root gives an actual off-`c` point, so full support forces

```text
a=2k^2 delta^2-k delta=2B^2/delta^2-B/delta.             (A)
```

With (A), this fiber is genuinely doubled at `T=0`. No division by
`2-p_c` or `3-p_c` was used; in particular `k=-1/2` and `k=-1/3` are covered.

For target infinity, the equations are `X0=X1=X2=0`. When `r=0`, the
first coordinate difference and `B!=0` force `T=0`, so there is no off-`c`
point there. For `r!=0`, they force `delta r+B!=0` and
`T=delta r^3/(delta r+B)`. The actual remaining polynomials satisfy

```text
Qinf=3delta^2(r+k delta)(r-delta/3),
Pinf(-k delta)=-k^3 delta^5!=0,
Pinf(delta/3)=-delta^4 L/9,
L=(1+3k)^2-9delta k^2(1+2k).
```

The point `r=-k delta` is excluded explicitly, rather than discarded by
denominator cancellation. If `L=0`, then `r=delta/3` has nonzero
denominator: its possible vanishing would force `k=-1/3`, but at that
value `L=-delta/3!=0`. Its reconstructed `T` is nonzero and it is an
actual off-`c` point at target infinity; center avoidance gives `X3!=0`.
Consequently full support forces `L!=0`. This is a geometric proof of
the exact degree condition used next, covering the leading-coefficient
boundary before the finite-root argument.

## 3. Actual quintic equation and every exceptional root

Define

```text
P6=p^2-3p+3,             Pc=p^2-6p+6,
E=(1+3k)p-3-6k,
r_s=delta(3-p)/(3(2-p)),
lambda_s=delta^4/(3p^2(2-p)^2),
T_s=delta^2 P6 Pc/(9p(2-p)^2 E).
```

For `p!=0,2` and `E!=0`, the independent checker verifies `F1=F2=F3=0`
and the actual normalization identity

```text
X0(r_s,T_s)-lambda_s=delta^3 Pc W/(27p^2(2-p)^3 E^2),
W=p P6 E^2-9delta(p-2)(kp^2-2kp-1)
    *(2k^2p^2-6k^2p+kp^2+6k^2-4kp+6k+1).
```

In particular `[p^5]W=L` and `W(2)=2`. Thus full support gives an actual
degree-five polynomial, rather than an assumed generic-degree numerator.

Take a root of `W` outside `{0,3+sqrt(3),3-sqrt(3)}`. Its `Pc` value
is nonzero, and `p=2` is impossible. All remaining cases are covered:

- If `E!=0` and `P6!=0`, then `T_s!=0` and `lambda_s!=0`. The actual
  normalization identity gives an off-`c` point of the required target.
- If `E!=0` and `P6=0`, then `T_s=0`. The actual embedded `c` would
  require `r_s=delta/p`, whereas
  `p(3-p)-3(2-p)=-Pc!=0`. Thus this cannot be a root of `W`.
- If `E=0`, the exact polynomial identity that
  `3(2-p)W-delta P6^2 Pc` is divisible by `E` forces `P6=0`.
  Now `r_s=delta/(3-p)` and `delta r_s+B=0`. Both linear transverse
  constraints and their constants vanish. The remaining actual equation is
  `J0=pT^2+[delta r_s+B-p(2r_s^2+r_s-a)]T+r_s^3(pr_s-delta)=0`.
  Its leading coefficient and constant are nonzero. It therefore has a
  nonzero `T` root over the algebraically closed field, giving an actual
  off-`c` point. Its scalar is explicitly `lambda=delta r_s^3/p!=0`.

For the last case, `P6` has no roots at `0,2,3`, and is coprime to `Pc`;
the independent checker verifies the explicit identity
`((5-p)/3)P6+((p-2)/3)Pc=1`. Hence the nonzero constant and the asserted
inequality `r_s!=delta/p` do not conceal an exceptional coincidence.
At `p=3`, `E=3k!=0`, so no omitted division by `3-p` occurs: that
division was used only on the `P6=0` case. At `k=-1/3`, `E=-1`, and
there is no `E=0` fiber. The target `p=0` is deliberately retained with
every possible multiplicity; the branch formula is never evaluated there.

Thus full support forces every root of `W` into the three displayed
distinct targets, with no uncovered finite denominator or projective fiber.

## 4. Complete profiles and direct certificate verification

Choose `s` with `s^2=3`. The degree and root-cover conclusions force

```text
W=L p^i(p-(3+s))^j(p-(3-s))^h,
i,j,h>=0, i+j+h=5.
```

There are exactly 21 triples. They include every order `0,...,5` at
`p=0`. The leading coefficients already agree, so each profile is exactly
five equations `f_t=[p^t]W-L[p^t](monic profile)=0`, for `t=0,...,4`.
The [owner's exported artifact](../validation/2026-10-12-nonendpoint-GJ-zero-normalized-lead/twenty-one-polynomial-bezout-certificates.txt)
prints five polynomials `b_t` for each profile, with `sum f_t b_t=1`.

The independent verifier parses those actual exported vectors and directly
multiplies them with sparse standard-library `Fraction` polynomial
arithmetic in `Q[p,k,delta,s]/(s^2-3)`. It regenerates no Groebner basis
or certificate vector. Every product is exactly `1`; every `b_t` contains
no `p` and is a polynomial in the parameters, with only constant rational
number-field coefficients. No saturation, inverse parameter, or omitted
parameter fiber is present in these identities. They specialize under
every embedding `Q(s)` into the algebraically closed characteristic-zero
field. Changing the choice of `s` swaps `j,h` in an already complete list.
Therefore all 21 necessary profiles are impossible.

## 5. Captured evidence and conclusion

The independent [source](../validation/2026-10-12-nonendpoint-GJ-zero-independent-audit/verify_fraction_certificates.py)
has SHA256 `de3e420cb004884b7771322468756fdab362f035ed69657e152428cb71c83ceb`.
Its accepted [execution record](../validation/2026-10-12-nonendpoint-GJ-zero-independent-audit/attempts/20261012T213210690020Z/execution-record.json)
captures the actual command, source snapshot, certificate-input snapshot,
raw stdout and stderr, and their SHA256 hashes. It records exit `0` and
**PASS, 80 assertions**: 15 structural identities, 21 checks that the
certificate vectors are parameter polynomials, 21 monic-profile checks,
21 direct exported-certificate products, and two completeness/degree checks.
These are assertions in one independent checker lineage, not 80 separate
geometric results. The recorded executable is
`/Library/Developer/CommandLineTools/usr/bin/python3`.

The earlier [failed attempt](../validation/2026-10-12-nonendpoint-GJ-zero-independent-audit/attempts/20261012T213152010950Z/execution-record.json)
is retained with source and raw streams. Its failure was a parser syntax
collision between the Macaulay2 variable `del` and the Python keyword;
the accepted source aliases that token to `par_delta`. No mathematical
identity failed, and no failed capture was overwritten.

The accepted independent record binds the unchanged owner note, source
`44d3b193783dc76562febe23af452a5b863b65b5f992dc6b1f83fad4a0c8fc33`,
owner execution record
`8e317259cf5e7fa71f16cfcd71f5e630354b4c52471c1329698bfb62582d1bb2`,
and actual exported certificate input
`46e1c3daa4c1b927a91bb65c747775de243533d4c6dc98b9562324fbb99aa304`.
No owner, canonical, historical seal, or Git file was changed by this audit.

**Audited conclusion:** `B!=0`, `G=Jbar=0` cannot have full inverse
support under the stated hypotheses. Combined with the separately audited
`B=0` exclusion, this proves the whole `G=Jbar=0` nonendpoint subfamily
admits no mate in any degree. Other nonendpoint parameter strata remain
open; this result is not a proof of non-STCI for `C0` or of the universal
projective-curve STCI statement.


---

## 4. nonendpoint target fiber reduction and bounded exclusions

# Nonendpoint quintics: complete target-fiber equations and bounded exclusions

Date: 2026-10-12. Author: `oct11_endpoint_a_nonzero_support/a_nonzero_local_excess`.
Status: **DIRECT STRUCTURAL REDUCTION AND BOUNDED ALL-MATE-DEGREE
EXCLUSIONS; pending independent mathematical audit**. No canonical or
previously sealed file is edited. The entire nonendpoint family remains open.

## 1. Actual pair, modulus and convenient lift parameters

Use the actual sections and chart in the
[pole-filtration and line-jet note](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-12-session-nonendpoint-pole-filtration-and-line-jetmd),
with delta!=0 over an algebraically closed field of characteristic zero.
The accepted normalization pair and its complete open S minus ell=A2(r,T)
are supplied by the [intrinsic pair classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
and [explicit model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
Assume the projection center avoids S whenever using an actual finite
normalization projection. Delta is retained as a modulus throughout.

Put

    B=b-a, G=g-3b+2a, J=d-2g+2b-a.

Then b=a+B, g=a+3B+G, d=a+4B+2G+J. The actual sections are

    U3=r^3-rT, U4=r^4-(2r^2+r)T+T^2,
    X0=U4+aT,
    X1=U4-delta U3+(a+B)T,
    X2=U4-3delta U3+3delta^2r^2-delta^3r+(a+3B+G)T,
    X3=U4-4delta U3+6delta^2r^2-4delta^3r+delta^4
       +(a+4B+2G+J)T.

On c:T=0 they give fixed C0 with target parameter z=(r-delta)/r.
The intrinsic A4 point maps to z=1, which is a nonendpoint of C0.

## 2. All off-c inverse points lie in this affine source chart

On the finite fourth-chart parameter u of ell, the four sections restrict to

    (u-1,u-1+delta,u-1+3delta,u-1+4delta).

Their quadric value is -3delta^2, so none of these finite ell-points maps
to C0. The missing ell-point is the intrinsic A4 point; it belongs to c
and maps to [1:1:1:1], i.e. z=1. Therefore every off-c point mapping to
C0 occurs in the actual complete open A2(r,T), with T!=0.

The following target-chart analysis consequently retains source infinity:
it does not mistake the A4 point for an affine point, or silently omit a
second source chart that could contain off-c inverse support.

## 3. Three linear target constraints and one actual normalization equation

For finite target z let p=1-z and let lambda=X0 be its projective scalar.
The three combinations of the actual coordinates give

    F1=delta r^3-(delta r+B)T-p lambda,
    F2=3delta^2r^2-delta^3r+G T-p^2(3-p)lambda,
    F3=delta^4-2delta^3r+J T+p^3(2-p)lambda.

Indeed X0-X1=p lambda, X2-3X1+2X0=p^2(3-p)lambda,
and X3-2X2+2X1-X0=-p^3(2-p)lambda for
lambda*(1,z,z^3,z^4). The combinations are invertible once X0 is
specified. Thus the full finite-target fiber is exactly

    F1=F2=F3=0, X0=lambda.

Under center avoidance any actual solution has lambda!=0: otherwise all
four actual sections vanish. All transverse terms, including T^2 in X0,
are retained. This is an exact fiber description rather than a first-jet
or tangent approximation.

## 4. A denominator-free reduction for every p!=0

Define

    H12=G+p(3-p)(delta r+B),
    H13=J-p^2(2-p)(delta r+B),
    R2=-delta r(pr-delta)*((3-p)r-delta),
    R3=delta(pr-delta)*(p(2-p)r^2+delta(2-p)r-delta^2),
    J0=pT^2+[delta r+B-p(2r^2+r-a)]T+r^3(pr-delta).

Eliminating only lambda, by division by the stated nonzero p, gives the
exact equivalent system

    H12 T+R2=0, H13 T+R3=0, J0=0.

Here lambda=(delta r^3-(delta r+B)T)/p. The equivalence follows from
F2-p(3-p)F1 and F3+p^2(2-p)F1, with J0=p(X0-lambda).
Consequently every leading-coefficient or minor degeneracy is retained.
If H12!=0 or H13!=0, solve the corresponding linear T equation and
substitute into the other equation and J0. If both vanish, Section 6
gives the complete compatibility analysis. No generic-rank hypothesis
replaces this case distinction.

## 5. A quadratic/cubic residual system on the specified regular chart

Put

    Z=Gp(2-p)+J(3-p),
    A=(3delta^2+G)p(2-p)+J(3-p),
    A2=A r^2+delta[delta^2p(p-3)+3Bp(2-p)+G(2-p)-J]r
       +delta^2[Bp(p-3)-G],
    N=delta^2(pr-delta)*[3(2-p)r-delta(3-p)],
    M=delta^2[3Jr^2+delta(2G-J)r-delta^2G].

The determinant of the three linear equations in (T,lambda,constant) is

    delta*p*(pr-delta)*A2.

Equivalently H12 R3-H13 R2=delta(pr-delta)A2. On the exact open
pZ!=0, Cramer's rule in F2,F3 gives

    T=-N/Z, lambda=M/(p^2Z).

The remaining normalization equation is

    Psi=p^2Z^2r^4+p^2Z(2r^2+r-a)N+p^2N^2-MZ
        =(pr-delta)C3,

where C3 is a polynomial of degree at most three in r. Its leading
cubic coefficient is pA^2. This statement allows A=0 and degree drop.
The quotient is an actual polynomial identity, not division by a curve
class or deletion of a fiber.

For r!=delta/p, the exact residual equations are therefore

    A2(r,p)=C3(r,p)=0.

Conversely every such solution on pZ!=0 reconstructs an off-c point.
If its T were zero, the four coordinate constraints and X0=lambda!=0
would say that the actual c-point r maps to z=1-p; its embedded target
parameter forces r=delta/p, a contradiction. If lambda were zero,
the actual projection would have a base point. Thus no additional scalar
or T artifact is discarded under the stated center-avoidance hypothesis.

Full inverse support consequently forces all common roots of this
quadratic/cubic pair to lie at r=delta/p on this chart. This is a compact
structural reduction; it does not prove that condition impossible for
all parameters. The locus Z=0 is governed by Section 4, not omitted.

## 6. All rank-one compatible fibers for p!=0

Suppose H12=H13=0. Compatibility requires R2=R3=0. The solutions are
exactly either

    r=delta/p,

or

    p^2-3p+3=0, r=delta/(3-p).

For completeness, r=0 makes R3=delta^4!=0. Otherwise, away from
pr=delta, R2 forces (3-p)r=delta; p=3 is impossible, and substituting
this value into the remaining quadratic gives
-delta^2(p^2-3p+3)/(3-p)^2. At either root of that p-polynomial,
r is nonzero and pr-delta!=0. These targets are the primitive cube
roots z=1-p, and are explicitly retained.

In the second case J0 is a quadratic in T with leading coefficient p!=0
and constant r^3(pr-delta)!=0. It has a nonzero root over the algebraically
closed field. Center avoidance makes its scalar lambda nonzero. Hence it
gives an actual off-c inverse point and excludes every mate degree.
Equivalently this excludes the precisely specified strata

    p^2-3p+3=0, r=delta/(3-p),
    G=-p(3-p)(delta r+B),
    J=p^2(2-p)(delta r+B),

for every a, subject to center avoidance.

In the first case J0 is

    T*[pT+pa+B-delta-delta^2/p].

Full support forces pa+B-delta-delta^2/p=0; otherwise the second T-root
is a genuine off-c point. With that coefficient zero the affine fiber
has only T=0, with its actual doubled structure retained. The rank-one
condition itself is

    G=-(3-p)(delta^2+Bp),
    J=p(2-p)(delta^2+Bp).

This gives a necessary exceptional-parameter condition, not an exclusion
of the allowed doubled fiber.

## 7. The intrinsic A4 target z=1, i.e. p=0

There is no affine c-point above this target. The exact off-c affine
equations are

    delta r^3-(delta r+B)T=0,
    3delta^2r^2-delta^3r+GT=0,
    delta^4-2delta^3r+JT=0.

Any common affine point has T!=0, since the first equation at T=0
forces r=0 while the third is then nonzero. Center avoidance supplies
X0!=0, so every such point is an actual off-c inverse point.

If J!=0, solve T=(2delta^3r-delta^4)/J. The remaining equations are
the cubic and quadratic

    P1=Jr^3-delta^2(delta r+B)(2r-delta),
    Q1=J(3r^2-delta r)+Gdelta(2r-delta).

Their leading coefficients J and 3J are nonzero. Their exact resultant is

    Res_r(P1,Q1)=-J^2 delta^6 Delta1,
    Delta1=G(G+3delta^2)(G+delta^2+2B)
           +J[(delta^2-5B)G-3B(delta^2+3B)]-BJ^2.

Thus J!=0,Delta1=0 excludes a mate in every degree; full support on
J!=0 requires Delta1!=0. No affine root at infinity or zero T is hidden
by this resultant because both leading coefficients remain nonzero and
T=0 was excluded directly.

If J=0, the third equation forces r=delta/2. Put D0=delta^2/2+B.
The first two equations are delta^4/8-D0T=0 and delta^4/4+GT=0.
An affine inverse point exists exactly when D0!=0 and G=-2D0, then
T=delta^4/(8D0). If D0=0 there is no point, even when G=0.
The J=0 case must not be inferred from the vanishing of the specialized
cubic/quadratic resultant.

## 8. The target endpoint z=infinity

The target equations are X0=X1=X2=0. In the source they are exactly

    delta r^3-(delta r+B)T=0,
    3delta^2r^2-delta^3r+GT=0,
    X0=0.

T=0 gives the unique affine c-point r=0. For off-c points with r=0,
the first two equations force B=G=0 and X0=T(T+a); thus such a point
exists precisely when a!=0,B=G=0, with T=-a. It maps to the endpoint
unless it is a forbidden projection base point.

For r!=0 the denominator Dr=delta r+B cannot vanish, by the first
equation. Solve T=delta r^3/Dr. The other equations reduce to

    Qinf=(3delta^2+G)r^2+(3delta B-delta^3)r-delta^2B,
    Pinf=-delta^2r^2+(B^2-delta B+a delta^2)r+a delta B.

If B!=0, a common root is automatically nonzero. Also Pinf(-B/delta)
=-B^3/delta!=0, so no denominator-zero root enters. Since Pinf has
nonzero quadratic leading coefficient, no common projective root at
r=infinity is introduced when Qinf drops degree. Consequently on B!=0
an off-c endpoint inverse point exists exactly when Res_r(Pinf,Qinf)=0.
This is another all-mate-degree excluded stratum.

If B=0, the r!=0 roots give r=a, a!=0 and
(3delta^2+G)a=delta^3. Together with the r=0 branch, the complete B=0
condition for an off-c affine endpoint inverse point is

    a!=0 and [G=0 or (3delta^2+G)a=delta^3].

If a=0 there is no off-c affine point above this endpoint. The endpoint
analysis and Sections 3--7 cover all projective target points of C0.

## 9. A complete new subfamily exclusion: a=b=g=d

This subfamily is B=G=J=0. If a!=0, (r,T)=(0,-a) has image
[0:0:0:delta^4], so it is an actual off-c endpoint point, with no base
point alternative.

It remains to take a=0. For p!=0,2,3 put

    r_s=delta(3-p)/(3(2-p)),
    lambda_s=delta^4/[3p^2(2-p)^2],
    P6=p^2-3p+3, Pc=p^2-6p+6,
    T_s=-delta^2 P6 Pc/[9p(2-p)^2(3-p)].

Direct substitution satisfies all three target constraints. The remaining
actual normalization equation is

    X0-lambda_s=delta^3 Pc V(p)/[27p^2(2-p)^3(3-p)^2],
    V(p)=p(3-p)^2 P6-9delta(2-p).

V is monic of degree five with p^4 coefficient -9. It has no roots
p=0,2,3: its values there are -18delta,2,9delta. At a root of P6,
V=-9delta(2-p)!=0. We claim V has a root outside Pc=0.

If all its roots were among the two distinct Pc-roots, evaluate at such
a root rho. Using rho^2=6rho-6 gives

    V(rho)=9[(5rho-6)-delta(2-rho)].

The two ratios (5rho-6)/(2-rho) are distinct: this fractional linear
map has nonzero determinant. Hence for any fixed delta, at most one
Pc-root is a V-root. All five roots would therefore be that one rho,
forcing V=(p-rho)^5. Comparing the p^4 coefficient gives rho=9/5,
but Pc(9/5)=-39/25!=0. This contradiction proves the claim.

Choose the asserted V-root outside Pc. The preceding value checks make
all denominators nonzero and P6!=0. Then T_s!=0, lambda_s!=0,
and X0=lambda_s, giving an actual off-c inverse point. This proves
every displayed projection with a=b=g=d has no mate in any degree,
for every nonzero delta. It is a bounded subfamily, distinct from the
entire-line ramification locus G=-3delta^2,J=0.

## 10. Why the endpoint septic proof does not transfer verbatim

The endpoint quadric divided into two anticanonical sections and left an
integral degree-five residual curve avoiding A4. In this nonendpoint
family the actual residual is the degree-six Weil divisor from the
pole-filtration note, with possible prime partitions 6,2+4,3+3,2+2+2;
there is no anticanonical quotient avoiding A4. The target z=1 is the
intrinsic A4 image, and its affine equations lose their scalar column.
The regular-chart denominator Z may also vanish identically, e.g. G=J=0.
These are actual structural differences rather than permissible generic
exceptions to drop.

The equations here preserve these differences. They yield finite systems
of degree at most two and three on the specified regular chart, explicit
rank-one fibers, and exact exceptional-target obstructions. They do not
bound all higher contact lengths in the remaining families or certify
full parameter exhaustion.

As a continuation lead within G=J=0 and B!=0, the rank-one c-fiber forces
a=2B^2/delta^2-B/delta. The off-c branch still has the displayed r_s and
lambda_s, with

    E_s=delta^2(3-p)+3B(2-p),
    T_s=-delta^4 P6 Pc/[9p(2-p)^2 E_s].

The captured exploratory source factors the remaining normalization
numerator as delta^2 Pc times a degree-at-most-five polynomial V_B.
Under full support its leading coefficient is nonzero by the target-
infinity test, and V_B(2)=2delta^5. Its potential roots at p=0 are real
intrinsic-A4 pole strata; they cannot be discarded using the endpoint
root-count proof. This is an open continuation reduction, not a full
G=J=0 exclusion.

## 11. Exact execution record and retained exploratory failure

The [supporting source](../computations/verify_session_nonendpoint_target_fibers_2026_10_12.m2)
passes seventeen exact identity checks. The
[execution record](../validation/2026-10-12-nonendpoint-target-fibers/execution-record.json)
binds its actual copied source, command, exit zero, raw stdout/stderr
and hashes. The final PASS ALL label is not an eighteenth check.
There is one accepted checker; captured replays do not increase the
distinct mathematical source count.

Four exploratory source snapshots and their captured executions are also
retained. The initial determinant/cubic script reached correct identities
but failed during optional coefficient printing because it used an
unsupported three-argument substitute call. That failed source and stderr
remain present. Three successful scratch factorizations supply provenance
for the two exceptional-target resultants and the open G=J=0 continuation
lead; they are not promoted into full-family exclusion certificates.
The written geometry supplies center avoidance, source-chart completeness
and all-mate-degree quantifiers independently of these execution counts.


---

## 5. nonendpoint target fiber independent proof audit

# Nonendpoint target fibers: independent projective-coverage and exclusion audit

Date: 2026-10-12. Author: `degree_factor_audit`.
Status: **DIRECT INDEPENDENT PROOF AUDIT OF THE STATED BOUNDED
EXCLUSIONS; ADDITIONAL EXACT CHECKS OF OMITTED COEFFICIENT AND
SPECIALIZATION STATEMENTS**. The full nonendpoint family, the remaining
quintic lanes, and the global STCI question remain open.

The audited owner note is
[target-fiber reduction and bounded exclusions](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md#4-nonendpoint-target-fiber-reduction-and-bounded-exclusions),
SHA-256 `c5c7b5b75babd6aa8881f2afc0489e2816f546bd79865e4e1e3458564abb7d5c`.
It was read without modification. All owner execution-manifest source and
stream hashes were checked against the actual files and matched. The
owner's seventeen accepted identities were inspected as supporting
identities, not counted as seventeen new executions or as a substitute
for the geometric arguments below.

Work over an algebraically closed field of characteristic zero, with
delta!=0. In this note `J=d-2g+2b-a` is the owner's lift parameter;
it is not the cubic first-normal polynomial denoted J in the separate
conormal audit. Put B=b-a and G=g-3b+2a.

## 1. Upstream hypotheses and the all-degree bridge

The accepted input is the actual normal anticanonical degree-five surface
S and its smooth rational quartic c, described in the
[explicit model audit](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
This audit checks fiber coverage and exclusions on that model; it does
not reprove the upstream classification of every admissible normalization
pair. The nonendpoint sections are exactly the sections displayed in the
owner note, with the entire delta modulus retained.

When the four sections have no common zero, they define a morphism
phi:S->P3 with phi^*O(1)=H. Since H is ample, no curve can be contracted,
so phi is finite onto its surface image. The image is nondegenerate:
its restriction to c is the fixed nondegenerate quartic C0. The degree
identity is

    5=H^2=deg(phi)*deg(phi(S)).

A surface of degree one in P3 is a plane, which is incompatible with
nondegeneracy. Hence deg(phi)=1 and phi is finite birational; normal S
is the normalization of the resulting integral quintic. Thus center
avoidance is sufficient for the actual normalization projection used by
the owner note.

The accepted
[quintic structural reduction](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit)
supplies the actual section

    Q=h^5/U0, div(Q)=5c, Q=T^5 on the complete affine open U0=1.

A hypothetical mate of degree 4k pulls back to a scalar Q^k. Equivalently
its effective zero divisor is 5kc. Therefore a point y outside c with
phi(y) in C0 is an all-mate-degree obstruction: the downstairs mate
vanishes at phi(y), while its pulled-back section is nonzero at y.
Every hypothetical mate degree is covered, since the accepted divisor
and degree reduction requires the mate degree to be a positive multiple
of four. This bridge uses an actual section and actual zero divisor;
mere set support without that divisor argument would not suffice.

## 2. Complete projective source boundary

In the anticanonical coordinates, the reduced complement of Z5!=0 is
exactly

    ell={Z2=Z3=Z4=Z5=0}.

The chart Z5=1 is the complete A2(r,T) used by the owner. On ell with
Z1=1, put u=Z0. Its four projection sections are exactly

    (u-1,u-1+delta,u-1+3delta,u-1+4delta).

Their pulled quadric value is -3delta^2. Hence no finite u point maps
to C0, which lies on that quadric. These points are also never base
points, because the first two sections differ by the nonzero delta.

The unique omitted point of ell is

    P0=[1:0:0:0:0:0].

It is the intrinsic A4 point and belongs to c. At P0 the actual
sections are (1,1,1,1), so it is not a base point and maps to target
z=1. There is no further off-c source boundary above C0. In particular,
source r=infinity is this intrinsic point on c, while target z=infinity
comes from the affine c-point r=0. These two infinities cannot be
identified.

Consequently every off-c inverse point above C0 occurs in A2(r,T) with
T!=0. All subsequent affine equations retain the full off-c source
support once this boundary argument has been supplied.

## 3. Finite targets: exact equations and the regular-chart scope

For finite target z, put p=1-z. The point of C0 is
lambda*(1,z,z^3,z^4), with lambda!=0. The three triangular combinations
of X0,...,X3 used to define F1,F2,F3 are invertible after X0 is specified.
Thus F1=F2=F3=0 together with X0=lambda is the exact fiber system.
If the reconstructed lambda were zero, all four sections would vanish;
center avoidance excludes that possibility.

For p!=0, eliminating lambda yields exactly

    H12*T+R2=0, H13*T+R3=0, J0=0.

This elimination divides only by the explicitly nonzero p. It neither
removes T^2 from X0 nor assumes a generic linear rank. On the further
open pZ!=0, the two equations F2,F3 have invertible coefficient matrix
in (T,lambda), and Cramer's rule gives the owner's T=-N/Z and
lambda=M/(p^2 Z). F1 becomes the displayed A2 residual after removing
the c factor pr-delta.

The normalization polynomial Psi has degree at most four in r and
is exactly divisible by pr-delta. Its quotient C3 has degree at most
three, with cubic coefficient p*A^2. This coefficient statement was
not asserted by the owner's final identity checker and is checked by
the independent source linked below. It allows A=0; no degree-drop
locus is removed.

For r!=delta/p on pZ!=0, A2=C3=0 reconstructs a point of the exact
fiber. If T=0, the known embedding c->C0 would force r=delta/p;
if lambda=0, the point would be a base point. Both alternatives are
excluded under the stated conditions. Conversely every off-c point
on this chart satisfies this quadratic/cubic system. The conclusion
is an exact reduction on the stated open, not a full parameter
exclusion. Z=0 remains governed by the denominator-free system.

Any future projective resultant of the degree-two/degree-three pair
must separately handle their shared leading-coefficient degeneration
A=0: a common homogeneous root at infinity does not by itself produce
an affine off-c point. The owner currently makes no such resultant
claim.

## 4. Rank-one compatibility includes the primitive cube roots

If H12=H13=0, compatibility requires R2=R3=0. For p!=0, delta!=0,
the factorization of R2 exhausts the alternatives. The root r=0
does not work because R3=delta^4. Away from pr=delta, the other
alternative is (3-p)r=delta; p=3 is impossible. Substitution into
R3 gives the condition

    p^2-3p+3=0, r=delta/(3-p).

These two p values correspond to z^2+z+1=0, the two primitive cube
roots. They are not generic-rank artifacts. At these points r!=0 and
pr-delta!=0, so J0 is a quadratic in T with nonzero leading coefficient
p and nonzero constant r^3(pr-delta). It has a nonzero root over the
algebraically closed field. Center avoidance then makes lambda nonzero,
and the point is an actual off-c inverse point. The specified rank-one
parameter strata are excluded in every mate degree.

At the alternative r=delta/p, the exact quadratic is

    T*(p*T+pa+B-delta-delta^2/p).

Unless the second factor has zero constant coefficient, it supplies
an off-c point. The equality pa+B-delta-delta^2/p=0 is therefore
necessary for full support. With equality, the doubled T=0 fiber
remains allowed; the owner correctly does not exclude it.

## 5. Target z=1 and the correct direction of Delta1

The intrinsic A4 point supplies the c-point above z=1. There is no
affine c-point above this target. On the affine open, the three
p=0 equations are exactly the owner's equations, and T=0 cannot
solve them: the first then forces r=0, while the third is delta^4.

For J!=0, eliminating T gives P1 and Q1 with degrees exactly three
and two, respectively, and nonzero leading coefficients J and 3J.
The accepted resultant is -J^2*delta^6*Delta1. These fixed leading
coefficients prevent a degree-drop root at infinity. Thus

    J!=0 and Delta1=0

gives an affine common root, necessarily T!=0; center avoidance
supplies X0!=0. This is an all-degree exclusion. The condition
J!=0 and Delta1!=0 merely avoids this obstruction. It is not itself
an excluded stratum and does not certify full inverse support.

For J=0, the third equation forces r=delta/2. The first two become
delta^4/8-D0*T=0 and delta^4/4+G*T=0, with
D0=delta^2/2+B. A point exists exactly when D0!=0 and G=-2D0.
If D0=0, the first equation is a nonzero constant. This correctly
handles the specialization that the general resultant cannot handle.

## 6. Target infinity and degree-drop resultants

The endpoint has equations X0=X1=X2=0. The affine c-point is r=T=0.
For r=0 and T!=0, the equations require B=G=0, a!=0 and T=-a.
Its X3 value is delta^4-J*a; center avoidance is needed if this value
vanishes. This precisely explains the owner's base-point caveat.

For r!=0, the first equation forces Dr=delta*r+B!=0 and
T=delta*r^3/Dr. The remaining equations are exactly Pinf=Qinf=0.
On B!=0, Qinf(0)=-delta^2*B is nonzero, and

    Pinf(-B/delta)=-B^3/delta!=0.

Thus neither a zero-r root nor a denominator-zero root can enter.
Pinf has fixed quadratic leading coefficient -delta^2, so it has
no homogeneous root at infinity. Consequently the nominal
quadratic resultant remains an exact common-affine-root test even
when Qinf drops degree. On B!=0 its vanishing gives an actual
off-c endpoint point, conditional on center avoidance, and excludes
every mate degree. No explicit expanded infinity resultant is
claimed here or needed for this criterion.

At B=0 the exact factorizations are

    Pinf=delta^2*r*(a-r),
    Qinf=r*((3delta^2+G)*r-delta^3).

Hence the complete off-c condition is exactly the owner's
a!=0 and [G=0 or (3delta^2+G)*a=delta^3], including the separate
r=0 branch. With a=0 there is no off-c affine endpoint point.

## 7. Equal lifts: the all-degree proof is complete for every delta!=0

For a=b=g=d, B=G=J=0. This entire subfamily is base-point free.
On the affine open, a hypothetical base point would make all three
coordinate combinations zero. The third would force r=delta/2,
but the second would then equal delta^4/4, a contradiction. Section 2
already rules out every boundary base point. Thus these maps really
are finite birational quintic projections by Section 1.

If a!=0, (r,T)=(0,-a) maps to [0:0:0:delta^4]. It is an off-c point
with a nonzero target scalar, independent of any generic assumption.

For a=0, use the owner's r_s,T_s,lambda_s, valid on p!=0,2,3.
The three target constraints are satisfied exactly, and the remaining
equation factors as the displayed nonzero rational prefactor times
Pc*V, where

    Pc=p^2-6p+6,
    P6=p^2-3p+3,
    V=p^5-9p^4+30p^3-45p^2+(27+9delta)*p-18delta.

The special values V(0)=-18delta, V(2)=2, V(3)=9delta remove those
three denominators. Modulo P6, V=-9delta*(2-p); hence a V-root is
not a P6-root. Modulo Pc,

    V=9*((5p-6)-delta*(2-p)).

The two distinct Pc-roots cannot both be V-roots: the map
(5p-6)/(2-p) has determinant four and its denominator is nonzero
at either root. If every V-root belonged to Pc, all five roots
counted with multiplicity would therefore be one Pc-root rho.
Monicity would give V=(p-rho)^5. Its next coefficient forces rho=9/5,
but Pc(9/5)=-39/25. This contradiction proves a V-root outside Pc.

At that root, all denominators are nonzero and P6 and Pc are nonzero.
Hence T_s!=0, lambda_s!=0 and X0=lambda_s, producing an actual
off-c inverse point. Every equal-lift projection, for every nonzero
delta, therefore has no mate in any degree.

## 8. Open continuation claims and precise verification boundary

The owner correctly leaves the general nonendpoint family open. This
audit also leaves the open G=J=0, B!=0 continuation lane open. Its
forced value a=2B^2/delta^2-B/delta follows from the rank-one c-fiber
at p=-delta^2/B and the condition of Section 4. On this lane,
Qinf=delta*(delta*r+B)*(3r-delta). Full support requires
Pinf(delta/3)!=0. After the forced-a substitution,

    9delta*Pinf(delta/3)
      =-(delta^5+6delta^3B-9delta^2B^2+9delta B^2-18B^3).

This verifies the stated bridge from the infinity test to the
nonvanishing leading coefficient of the exploratory V_B polynomial.
The complete V_B factorization and its V_B(2) specialization were
read in the owner's hash-verified exploratory source and streams;
they were not independently recomputed by this bounded audit and
are not promoted here into a fresh full-family certificate.

No mathematical failure was found in the closed bounded exclusions.
Classification hypotheses are inherited from the accepted upstream
pair theorem. The general quadratic/cubic parameter incidence, the
remaining parameter incidences arising from Z=0 fibers, and higher
contact lengths remain unexhausted.

## 9. New bounded execution and preserved checker failure

The [new independent source](../validation/2026-10-12-nonendpoint-target-fiber-independent-audit/verify_proof_gaps.m2)
checks eleven coefficient, boundary, remainder and specialization
statements omitted from the owner's seventeen assertions. Its source
SHA-256 is
`3cac9be6e6bfe7fdd3502f5e66e70f5c34fb024c5ed67e5f9922a8ac50e8ddfc`.
The [captured execution record](../validation/2026-10-12-nonendpoint-target-fiber-independent-audit/execution-record.json)
records the actual Macaulay2 command, exit zero, elapsed time, and raw
stdout/stderr hashes. The final PASS ALL line is not a twelfth check.

One earlier execution failed at the first assertion because the
checker used coefficient(r^3,C3) in a flat multivariate ring. That
operation extracts a single monomial coefficient; it does not extract
the coefficient polynomial in r. The exact failed source and streams
remain in
[attempt 01](../validation/2026-10-12-nonendpoint-target-fiber-independent-audit/attempt-01-coefficient-extraction-error/execution-record.json).
The corrected source extracts the whole coefficient by the third
r derivative at r=0, divided by six. The whole V polynomial is also
checked instead of incorrectly using the same monomial-coefficient
operation for its p coefficients.

There is one independent checker lineage with two actual executions:
one checker-operation failure and one accepted pass. No owner source,
canonical record, previously frozen source, or Git state was edited.
