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
[target-fiber reduction](2026-10-12-session-nonendpoint-target-fiber-reduction-and-bounded-exclusions.md),
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
[quintic structural frontier](2026-10-11-session-quintic-structural-frontier.md),
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
