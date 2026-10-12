# Endpoint a!=0: full-jet excess bound and exclusion with at most two contacts

Date: 2026-10-11. Author: `oct11_endpoint_a_nonzero_support/a_nonzero_local_excess`.
Status: **DIRECT LOCAL-INTERSECTION PROOF WITH EXACT ALGEBRAIC CERTIFICATES;
pending independent audit**. This note changes no canonical or frozen record.
It proves the displayed endpoint a!=0 full-support condition impossible when
U and W have at most two distinct common roots. It does not by itself treat
the three-common-root stratum or nonendpoint projection centers.

## 1. Scope and retained transverse equations

Use the actual endpoint projection and center-avoidance hypotheses in the
[quadric-factor reduction](2026-10-11-session-quintic-endpoint-quadric-factor-reduction.md)
and its [independent audit](2026-10-11-session-quintic-endpoint-factor-independent-audit.md).
On the smooth affine normalization chart the coordinates are

    X0=1+aT, X1=r+bT,
    X2=r^3+(g-r)T, X3=r^4+(d-2r^2-r)T+T^2.

Work over an algebraically closed field of characteristic zero, with a!=0,
and assume for contradiction full reduced inverse support of C0 is c:T=0.
The two exact residual equations are

    K=ar^4-br^3-r^2-(1+g)r+d
      +T*(1+ad-bg-2ar^2-ar+br)+aT^2,
    E=U+T*P1+T^2*P2,
    U=g-r-3br^2+2ar^3,
    W=K(r,0)=ar^4-br^3-r^2-(1+g)r+d,
    P1=a^2r^3+2a(g-r)-3b^2r,
    P2=a^2(g-r)-b^3.

Indeed q pulls back to TK and X0^2 X2-X1^3 pulls back to TE. These
identities retain every transverse term. The factor audit proves that
the total excess intersection length length(O_D/(E)) is seven, all
supported at finite common roots of U and W, where D=V(K) is integral.
The present proof bounds these actual excess lengths, not their first jets.

## 2. Endpoint avoidance and the resultant's harmless chart factor

Put Cb=a^2g-ab-b^3. If Cb=0, the actual affine point

    r=b/a, T=-1/a

has X0=X1=X2=0. If also X3=0 it is a projection base point, contradicting
center avoidance. Otherwise it maps to the endpoint [0:0:0:1] of C0
and lies off c, contradicting full inverse support. Thus Cb!=0.

The exact resultant in the actual transverse variable factors as

    Res_T(K,E)=(ar-b)^2 H(r),
    deg H=7, [r^7]H=-a^4.

The square factor arises from the point with X0=X1=0 in the cubic-plus-
quadric target equations; those two equations alone also vanish along
the target line X0=X1=0. The factor is not silently interpreted as C0.

At a common root rho of U and W, set w=a rho-b. Substitution of U(rho)=0
gives the exact identity

    Cb=w*(a+w^2-3aw rho).

Consequently w!=0 at every possible excess support point. The factor
(ar-b)^2 is therefore a unit near rho and can be removed there.

The order of H at rho equals the total local intersection length of K,E
in the r-fiber over rho. To justify this even when D is singular, K/a is
monic quadratic in T. Over the DVR k[[r-rho]] the algebra defined by K/a
is free of rank two, and the resultant is, up to a nonzero scalar, the
determinant of multiplication by E. When the resultant is not identically
zero, the determinant's valuation is the length of its cokernel. Splitting
the finite fiber gives the sum of the local intersection lengths. H has
nonzero leading coefficient, so this finiteness condition holds.

Under full support, any common point of K,E in this fiber with T!=0 and
X0!=0 would map to affine C0 and is excluded. A point with X0=0 must have
X1=0 to satisfy the pulled cubic, hence r=b/a; this does not occur at rho
because w!=0. Thus the only supported common point in the rho-fiber is
(rho,0), and ord_rho H is exactly the actual excess length at that point.
This includes a double K-root at T=0 and singular D.

## 3. The second transverse root excludes one derivative factor

Write r=rho+s. The equations U(rho)=W(rho)=0 determine

    g=rho+3b rho^2-2a rho^3,
    d=rho+2rho^2+4b rho^3-3a rho^4.

At s=0 the full equations become

    K=T*(M+aT), E=T*(P1+P2T),
    M=1-3rho^2w^2,
    P1=-3rho w^2, P2=-w^2*(3a rho-w).

Define

    S1=1+3w rho^2*(3a rho-w),
    S2=1-6w rho+3w^2rho*(2rho+1).

Exact expansion of H gives

    [s]H(rho+s)=-w S1 S2,
    aP1-MP2=-w^3 S1.

If S1=0 then rho!=0, since S1=1 at rho=0. Also M!=0: if M=0,
the second identity gives aP1=0, impossible with a,w,rho all nonzero.
The second K-root T=-M/a is therefore nonzero and is also an E-root.
At this point X0=1-M=3rho^2w^2!=0, so it is an actual off-c point
mapping to affine C0. Full support consequently forces S1!=0.

Thus an excess length at least two requires S2=0. S2 is the exact
Jacobian determinant of K,E at (rho,0), but only serves here to
parametrize the higher-jet analysis that follows; no order bound is
inferred from this determinant alone.

## 4. All multiple-contact parameters and their higher coefficients

Assume S2=0 and put q=w rho. Necessarily q!=0. Solving S2 gives

    D=6q^2-6q+1,
    w=-D/(3q), rho=q/w.

D!=0 because w!=0. These formulas exhaust S2=0, including singular
residual-curve cases; they impose no smoothness assumption on D_K.

Let c_j=[s^j]H(rho+s). The exact coefficient c_2/S1 is

    ((243q^5-162q^4+27q^3)*a
      +1944q^8-6480q^7+8316q^6-5292q^5+1890q^4
      -468q^3+99q^2-15q+1)/(81q^4).

At q=1/3 this expression is -1/27 for every a. Hence that entire
exceptional parameter case has excess length exactly two. In particular
it is not lost by division by 3q-1.

For q!=1/3, excess length at least three forces the unique value

    a=-D^2 A4/(27q^3(3q-1)^2),
    A4=54q^4-72q^3+15q^2-3q+1.

At this value the exact next coefficient and the remaining unit factor are

    c_3=D^3 N6 N9/(2187q^7(3q-1)^4),
    S1=-N6/(3q-1)^2,
    N6=162q^6-216q^5+72q^4-27q^3-3q^2+6q-1,
    N9=8748q^9-20412q^8+18954q^7-8262q^6+1458q^5
       -252q^4+180q^3-66q^2+12q-1.

The retained denominator conditions q!=0,D!=0,q!=1/3 and S1!=0
are all explicit. The original a!=0 and Cb!=0 remain in force;
excluding further parameter values cannot weaken the bound below.

## 5. Exact certificates prove order at most four and uniqueness at order four

Let J be the resultant in s of the two quotient polynomials

    U(rho+s)/s, W(rho+s)/s.

After substituting the forced a from Section 4, compute c_3,c_4,J as
elements of QQ(q), retaining their actual numerators. The exact identities are

    gcd(num c_3,num c_4)=D^3,
    gcd(num c_3,num J)=D^3.

These are not numerical samples. The [fourteen-check M2 source](../computations/verify_session_quintic_endpoint_a_nonzero_local_excess_2026_10_11.m2)
derives both numerators directly from the retained full equations and
exports their rational coefficient lists. The independently generated
[Bezout certificates](../validation/2026-10-11-quintic-endpoint-a-nonzero-local-excess/bezout-certificates.json)
give, for each displayed pair, explicit polynomial multipliers over QQ
whose combination is D^3. A standard-library Fraction verifier multiplies
the exported polynomials and checks both identities exactly. Thus neither
pair can simultaneously vanish when D!=0.

If the excess length were at least five, then c_3=c_4=0, contradicting
the first certificate. Therefore every excess length is at most four.

If an excess length is four, then c_3=0. The second certificate forces
J!=0. Consequently the two quotient polynomials have no common root
over the algebraically closed field. Any other common U,W root would
give such a root; even an additional common multiplicity at rho would
do so at s=0. Thus an order-four excess forces rho to be the only common
root of U,W, with no additional common multiplicity.

## 6. Consequence for at most two distinct common roots

If there are no common roots, the necessary seven-excess condition fails.
If there is just one common root, its excess is at most four, again less
than seven. If there are two distinct common roots, neither can have
excess four, since that would force it to be the only common root.
Each then has excess at most three, for a total at most six. This is
also less than seven. Repeated roots and singular residual curves are
already covered by actual intersection lengths in Sections 2--5.

Hence full inverse support is impossible throughout the endpoint a!=0
family with at most two distinct common U,W roots. The three-distinct-
common-root family remains a separate obligation in this note.

## 7. Execution provenance and failure corrections

The [execution record](../validation/2026-10-11-quintic-endpoint-a-nonzero-local-excess/execution-record.json)
binds the final checker source, its snapshot, commands, raw streams,
four recorded source-version executions, and the two Bezout checks.
The source has SHA-256
`84d8ffa69ff8e74f971112cc3a8e18efe33832af8c6ed5ab0bd0a8b26c67fccd`.
The recorded final run returned zero with fourteen passing M2 checks.
There is one mathematical M2 checker; its recorded replays and source
copies do not constitute additional distinct checker results.

Three failed source versions are preserved. The first two assertions
failed because unparenthesized multiline M2 assignments silently omitted
the following-line terms. An initial tentative quotient-ring diagnosis
was superseded by inspection of the actual parsed equations. Parentheses
repaired the source; the fraction-field presentation was retained and
every resulting rational identity is interpreted with the explicit
nonzero conditions above. The third version passed all fourteen checks
but failed while exporting coefficients because q had the wrong ring
binding. Rebinding to QQ[q] repaired only that export.

Earlier scratch resultant and parameter scripts are exploratory leads,
not additional accepted theorem certificates. The source's exact identities
and Bezout certificates support the algebraic calculations; the preceding
local determinant and support arguments supply the geometric quantifiers.
