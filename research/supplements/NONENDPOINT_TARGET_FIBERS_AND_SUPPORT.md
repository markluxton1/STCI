# Nonendpoint actual target fibers and full inverse support

Fix the embedded curve \(C_0=[s^4:s^3t:st^3:t^4]\), an algebraically closed characteristic-zero field, and the accepted anticanonical degree-five A4 pair \((S,c)\). Retain arbitrary \(\delta\ne0\), the four lift parameters \(a,b,g,d\), and an actual line center disjoint from \(S\), giving a finite birational projection \(\nu:S\to X\) onto an integral quintic. The restriction \(c\to C_0\) is an isomorphism. A hypothetical mate forces **full** reduced inverse support \((\nu^{-1}C_0)_{red}=c\), denoted SUP; it excludes isolated extra inverse points as well as extra curves. The proofs below concern this exact family, not every quintic carrier. The intrinsic pair is proved in [the A4 model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md); actual projection coordinates and every target boundary are in [the target-fiber chapter](NONENDPOINT_TARGET_FIBERS_AND_SUPPORT.md). This chapter owns the literal target-fiber equations, denominator-free rank alternatives, all target endpoints, and the G=J=0 and equal-lift full-support exclusions. A resultant zero alone never replaces the actual off-c equations.

<a id="4-nonendpoint-target-fiber-reduction-and-bounded-exclusions"></a>
<a id="5-nonendpoint-target-fiber-independent-proof-audit"></a>

## Complete actual target-fiber equations

### 1. Actual pair, modulus and convenient lift parameters

Use the actual sections and chart in the
[pole-filtration and line-jet note](NONENDPOINT_RESIDUAL_FACTORIZATION_AND_GENUS.md#3-nonendpoint-pole-filtration-and-line-jet-independent-audit),
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

### 2. All off-c inverse points lie in this affine source chart

On the finite fourth-chart parameter u of ell, the four sections restrict to

    (u-1,u-1+delta,u-1+3delta,u-1+4delta).

Their quadric value is -3delta^2, so none of these finite ell-points maps
to C0. The missing ell-point is the intrinsic A4 point; it belongs to c
and maps to [1:1:1:1], i.e. z=1. Therefore every off-c point mapping to
C0 occurs in the actual complete open A2(r,T), with T!=0.

The following target-chart analysis consequently retains source infinity:
it does not mistake the A4 point for an affine point, or silently omit a
second source chart that could contain off-c inverse support.

### 3. Three linear target constraints and one actual normalization equation

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

### 4. A denominator-free reduction for every p!=0

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

### 5. A quadratic/cubic residual system on the specified regular chart

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

### 6. All rank-one compatible fibers for p!=0

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

### 7. The intrinsic A4 target z=1, i.e. p=0

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

### 8. The target endpoint z=infinity

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

### 9. A complete subfamily exclusion: a=b=g=d

For a=b=g=d, B=G=J=0. This entire subfamily is base-point free.
On the affine open, a hypothetical base point would make all three
coordinate combinations zero. The third would force r=delta/2,
but the second would then equal delta^4/4, a contradiction. The complete projective-source boundary analysis below
rules out every boundary base point. These maps have pullback polarization H, which is ample. A positive-dimensional projective fiber would contain a curve of H-degree zero, so no curve is contracted and the proper map is finite. The four sections are linearly independent, hence the surface image is nondegenerate and cannot be a plane. The degree formula

    5=H^2=degree(map)*degree(image)

therefore gives degree(map)=1 and a degree-five integral image. Since S is normal, this finite birational map is its normalization. Thus the base-point-free calculation produces actual admissible quintic projections throughout this subfamily, before their full-support rejection.



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

### 10. Why the endpoint septic proof does not transfer verbatim

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

For the bounded reduction within G=J=0 and B!=0, the rank-one c-fiber forces
a=2B^2/delta^2-B/delta. The off-c branch still has the displayed r_s and
lambda_s, with

    E_s=delta^2(3-p)+3B(2-p),
    T_s=-delta^4 P6 Pc/[9p(2-p)^2 E_s].

The exact polynomial reduction factors the remaining normalization
numerator as delta^2 Pc times a degree-at-most-five polynomial V_B.
Under full support its leading coefficient is nonzero by the target-
infinity test, and V_B(2)=2delta^5. Its potential roots at p=0 are real
intrinsic-A4 pole strata; they cannot be discarded using the endpoint
root-count proof. This bounded reduction is used by the complete G=J=0 support exclusion below; by itself the displayed factorization is not that full exclusion.


<a id="1-nonendpoint-conductor-infinity-coefficient"></a>

## A simple conductor root at target infinity

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


<a id="2-nonendpoint-GJ-zero-full-support-exclusion"></a>
<a id="2-nonendpoint-gj-zero-full-support-exclusion"></a>
<a id="3-nonendpoint-GJ-zero-full-support-independent-audit"></a>
<a id="3-nonendpoint-gj-zero-full-support-independent-audit"></a>

## Full inverse-support exclusion when G=J=0

### 1. Claim and actual geometric scope

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
[quintic structural frontier](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md#1-quintic-conormal-and-delpezzo-audit),
Section 1, makes that equality necessary for a mate, so this is an
all-mate-degree exclusion in the stated normalization/projection lane.

If B=0, the claim is already proved in Section 9 of the frozen reduction:
it is the complete a=b=g=d subfamily. Thus it remains to prove the claim
for B!=0. No division by B in this note silently discards that case.

### 2. The doubled c-fiber forces a unique lift parameter

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

### 3. Target infinity forbids a quintic degree drop

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

### 4. A compact actual off-c branch and its quintic equation

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

### 5. Every W-root lies among three retained exceptional targets

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

### 6. Twenty-one complete coefficient profiles have polynomial unit certificates

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


## Projective coverage and exact boundary directions

### 2. Complete projective source boundary

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

### 3. Finite targets: exact equations and the regular-chart scope

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

### 4. Rank-one compatibility includes the primitive cube roots

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

### 5. Target z=1 and the correct direction of Delta1

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

### 6. Target infinity and degree-drop resultants

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


## Exact support and characteristic scope

The mathematical proofs above retain the actual homogeneous equations, local rings and nonreduced conductor membership used by the inherited independent reviews. Necessary exact computational support is retained in [verify_session_nonendpoint_conductor_infinity_coefficient_2026_10_12.py](../computations/verify_session_nonendpoint_conductor_infinity_coefficient_2026_10_12.py), [verify_session_nonendpoint_GJ_zero_profile_exclusion_2026_10_12.m2](../computations/verify_session_nonendpoint_GJ_zero_profile_exclusion_2026_10_12.m2), [verify_fraction_certificates.py](../validation/2026-10-12-nonendpoint-GJ-zero-independent-audit/verify_fraction_certificates.py), [verify_session_nonendpoint_target_fibers_2026_10_12.m2](../computations/verify_session_nonendpoint_target_fibers_2026_10_12.m2), [verify_proof_gaps.m2](../validation/2026-10-12-nonendpoint-target-fiber-independent-audit/verify_proof_gaps.m2). No inherited computation was rerun for this consolidation.

These conclusions are proved in characteristic zero for the specified admissible nonendpoint A4 normalization family. The finite local Nakayama and actual-module arguments are not themselves characteristic-zero-specific, but the displayed balanced frames, separable curve maps, coefficient inversions and nilpotent power-rigidity applications must retain their stated hypotheses. No positive-characteristic all-family exclusion is inferred. The fixed C0 has [a quartic-carrier construction in every positive characteristic](POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).
