# Nonendpoint quintics: complete target-fiber equations and bounded exclusions

Date: 2026-10-12. Author: `oct11_endpoint_a_nonzero_support/a_nonzero_local_excess`.
Status: **DIRECT STRUCTURAL REDUCTION AND BOUNDED ALL-MATE-DEGREE
EXCLUSIONS; pending independent mathematical audit**. No canonical or
previously sealed file is edited. The entire nonendpoint family remains open.

## 1. Actual pair, modulus and convenient lift parameters

Use the actual sections and chart in the
[pole-filtration and line-jet note](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md),
with delta!=0 over an algebraically closed field of characteristic zero.
The accepted normalization pair and its complete open S minus ell=A2(r,T)
are supplied by the [intrinsic pair classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md)
and [explicit model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md).
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
