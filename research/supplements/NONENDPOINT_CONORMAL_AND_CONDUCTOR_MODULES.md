# Conormal and conductor modules

Permanent complete mathematical dossier for the nonendpoint quintic geometry. The original calculations, exact hypotheses, conditional status, counterexamples, failure modes and unresolved cases are preserved below. Independent certificates are mathematical arguments; executable code remains separately located in the repository.

---

## 1. nonendpoint conormal cubic reduction

# Nonendpoint quintics: cubic conormal direction and generic all-degree obstruction

Date: 2026-10-12. Author: root.

Status: **DIRECT STRUCTURAL REDUCTION AND GENERIC ALL-DEGREE OBSTRUCTION;
separate independent audits requested**.
This concerns the genus-one quintic A4 normalization lane for fixed
`C0=[s^4:s^3t:st^3:t^4]`, over an algebraically closed field of
characteristic zero. It does not exclude all quintic carriers, every
mate degree, or the unrestricted STCI problem. The completed endpoint
exclusion is not reopened. Existing sealed records are unchanged.

## 1. Actual projection and balanced conormal direction

Use the [nonendpoint family](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-12-session-nonendpoint-pole-filtration-and-line-jetmd)
and the accepted [intrinsic pair](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md).
On the affine normalization chart let `c:T=0` and `delta!=0`. The four
sections restrict to

    (r^4,r^3(r-delta),r(r-delta)^3,(r-delta)^4).

Their T derivatives on c are

    L0=a-2r^2-r,
    L1=b-2r^2-r+delta r,
    L2=g-2r^2-r+3delta r,
    L3=d-2r^2-r+4delta r.

In the target chart x0!=0 write y=x1/x0, z2=x2/x0, w=x3/x0. The
actual balanced conormal coordinates are

    V=z2-y^3, U=w-(3/2)y z2+(1/2)y^4.

On c, y=(r-delta)/r. Direct differentiation, including the moving y,
gives

    V_T=P(r)/r^7, U_T=J(r)/(2r^7),

where

    P=(g-3b+2a)r^3
      +[6delta(b-a)+delta^3-3delta^2]r^2
      +[delta^2(6a-3b)+2delta^3]r-2a delta^3,

    J=(2d-3g+b)r^3
      +[3delta(g-b)+5delta^3-3delta^2]r^2
      +[3b delta^2+delta^3-delta^4]r-b delta^3.

For example P before expansion is
`r^3 L2-3r(r-delta)^2 L1+2(r-delta)^3 L0`;
J is `2r^3 L3-3r^2(r-delta)L2+(r-delta)^3 L1`.
The cancellation of the prospective higher terms is exact, not a
sampled degree observation.

The opposite target chart uses the reversed coordinates. With its raw
balanced coordinates Vraw and Uraw, choose Uop=Vraw/2 and Vop=2Uraw.
Modulo the square of the curve ideal,

    Uop=y^(-7)U, Vop=y^(-7)V.

Thus both first symbols have the same scalar transition. In particular,
on the opposite chart their T derivatives are J/[2(r-delta)^7] and
P/(r-delta)^7. There is no discarded target-infinity stratum at r=0.

For an actual admissible finite birational projection, the image surface
is generically regular along C0. Its conormal kernel is the kernel of
this generic projection-normal functional. The saturated quotient of
the balanced `O(-7)^2` is therefore determined by the rational ratio
`[J/2:P]`. Let Ph,Jh be their degree-three homogenizations in r and let
h be their homogeneous gcd degree, counting roots at infinity. Then

    L=O(e-7), e=3-h.

This follows either from the global balanced transition or the standard
description of a quotient of `O(-7)^2` by a basepoint-free degree-e
binary pair. It does not assume the normalization is immersive at every
point of c, or equate the common first-normal zero divisor with the top
BF defect divisor. P,J cannot both vanish identically: their constants
would force a=b=0, after which the coefficient of r in P is 2delta^3.

## 2. The socle bound for every possible mate exponent

A mate in this lane has degree 4k and generic multiplicity m=5k, by
the [quintic structural audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md).
The all-quartic exclusion makes k>=2. The generic transverse algebra is
curvilinear. The saturated finite-flat Gorenstein pairing gives

    E_(m-1)=L^(m-1)(D_(m-1)),
    deg E_(m-1)=-6-16k,
    deg D_(m-1)=(5k-1)(7-e)-6-16k >= 0.

Here D_(m-1) is effective. This is the same direct algebraic argument
as the [multiplicity-ten audit](2026-10-11-session-multiplicity-ten-filtration-audit.md)
and [uniform order-one bound](2026-10-06-uniform-order-one-frontier.md).
For primary-source context the Gorenstein duality and its quasiprimitive
BF specialization were freshly inspected in
[Manolache, 2023, pp.143-145](https://imar.ro/journals/Revue_Mathematique/pdfs/2023/1-2/10.pdf).
The displayed numerical inequality is derived here from CI adjunction;
it is not attributed verbatim to that paper.

Consequently:

* If Ph,Jh are coprime, e=3 and the top defect degree is 4k-10.
  Thus k=2 is impossible; any mate would have degree at least twelve.
  Nothing here excludes k>=3.
* A possible degree-eight mate requires h>=1. Equivalently the two
  homogeneous cubics have a common zero, including infinity. This is
  a proper closed resultant locus in the five projection parameters,
  restricted to delta!=0 and actual center avoidance.

To verify properness, at delta=1,a=1,b=g=d=0 the pair is
`P=2(r^3-4r^2+4r-1)`, `J=2r^2`, homogenized to degree three.
The only homogeneous roots of J are r=0 and infinity. Neither is a root
of P, so the pair is coprime. This point proves
that the resultant polynomial is nonzero; admissibility of this
particular point is not asserted. The center-avoidance set is a
nonempty open set: the fixed center point lies in the span of c but
outside S (S's hyperplane section there is c+ell), and the line
extensions meeting S form an incidence of dimension at most two in
the four-dimensional extension space. Hence the coprime open meets
the admissible open. This is a generic degree-eight exclusion, not a
full parameter-space or all-mate-degree exclusion.

## 3. An all-degree obstruction from immersion and the actual conductor

Write `Jbar=d-2g+2b-a`. We now prove the stronger statement:

> Every admissible nonendpoint projection with coprime Ph,Jh and Jbar!=0
> has an actual point outside c mapping onto C0. It therefore has no
> mate of any positive degree. A hypothetical mate must satisfy
> `Jbar * Res_h(Ph,Jh)=0`.

This is a proper closed necessary locus, not its exhaustion. No upper
bound on higher contact lengths is deduced from the first symbols.

Suppose full inverse support holds. Every closed point of C0 then has
exactly one point in its normalization fiber, because c->C0 is an
isomorphism and there are no other points over C0. At a finite r, S is
smooth with coordinates r,T. The derivative tangent to c is nonzero
downstairs. The balanced normal projection vector is `[J/2:P]`; the
coprimality hypothesis prevents its two entries from vanishing
simultaneously at any finite r. The opposite chart checks r=0, while
r=delta is regular in the first chart. Thus the target differential
has rank two and the map on cotangent spaces is surjective at every
smooth point of c.

At the remaining A4 point, use the actual chart Z0=1 from the
[independent local-chart audit](2026-10-11-session-dp5-a4-local-chart-independent-audit.md).
Let alpha=Z1/Z0, beta=Z2/Z0, chi=Z3/Z0. These generate the maximal
ideal; the single surface relation has no linear term. Put

    dZ=alpha beta-chi^2,
    eZ=beta^2-alpha beta chi+chi^3, h=beta+chi.

The actual projection sections on this chart are

    X0=1-alpha+a h,
    X1=1+(delta-1)alpha+b h,
    X2=1+(3delta-1)alpha+3delta^2 chi-delta^3 dZ+g h,
    X3=1+(4delta-1)alpha+6delta^2 chi-4delta^3 dZ+delta^4 eZ+d h.

They all have value one at A4. The three target ratios Xi/X0-1 have
linear coefficient matrix in alpha,beta,chi

    [delta,  b-a, b-a]
    [3delta, g-a, g-a+3delta^2]
    [4delta, d-a, d-a+6delta^2].

Its determinant is `-3delta^3 Jbar`, nonzero under the stated hypothesis.
It therefore surjects onto the full three-dimensional source cotangent
space, including the singular A4 point. Smoothness of S at that point
is neither assumed nor required.

Here is the finite local algebra step. For a finite birational
normalization map with a unique point over a closed point, localize the
target ring A and its normalization B there. B is local and finite
over A, and the residue fields agree. Cotangent surjectivity says
`m_B=m_A B+m_B^2`. Nakayama over B on `m_B/m_A B` gives `m_B=m_A B`.
Consequently B/m_A B is generated by the residue of 1. Nakayama over
A makes B generated as an A-module by 1, so B=A. This proves local
isomorphism rather than only injectivity of tangent vectors.

The projection would therefore be a local isomorphism along every
point of c. Its actual conductor ideal is then a unit there. But the
[accepted quintic conductor computation](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
gives an invertible upstairs conductor ideal O_S(-2H), whose effective
Cartier divisor Dc satisfies

    degree(O_S(Dc)|c)=2H.c=8.

If Dc misses c, its defining section restricts to a nowhere-zero
section of this degree-eight line bundle on P1, which is impossible.
Thus full inverse support cannot hold. Finiteness of the normalization
then gives an actual additional point over C0, contradicting any mate.
This is an entire support/conductor argument and applies to all k.

The necessary locus is proper: the coprime example in section 2 has
Jbar=-1. Both required nonvanishings hold there, and the irreducible
parameter space's admissible nonempty open intersects their nonempty
open. The particular example's admissibility remains unasserted.

The remaining parameters with a common homogeneous root or Jbar=0
are genuinely open for this argument. Their actual conductor restriction
to c, of degree eight, must be supported at the finite common-root
points and the A4 point where cotangent rank can fail. No multiplicity
bound on this restriction follows from the first symbols alone.

## 4. An explicit complete incidence cover of the necessary common-root locus

The homogeneous common-root condition can be retained without expanding
a large resultant. For each actual delta!=0 it is exactly the union of:

* r=0: a=b=0;
* r=infinity: g=3b-2a and d=4b-3a;
* a finite nonzero root rho: P(rho)=J(rho)=0.

In the last case one may solve without losing a stratum:

    g=3b-2a-[6delta(b-a)+delta^3-3delta^2]/rho
      -[delta^2(6a-3b)+2delta^3]/rho^2
      +2a delta^3/rho^3,

    d=(3g-b)/2-[3delta(g-b)+5delta^3-3delta^2]/(2rho)
      -[3b delta^2+delta^3-delta^4]/(2rho^2)
      +b delta^3/(2rho^3).

Repeated roots and multiple common roots remain in this incidence
cover. It does not classify actual higher embedded jets or assert any
surviving parameter admits a mate. At a finite smooth source point
where both target chart and source transverse coordinate are regular,+a common root records a transverse projection rank drop along c.
No root-count or contact bound is inferred from that first symbol.

## 5. Evidence and next step

The [supporting checker](../computations/verify_session_nonendpoint_conormal_cubics_2026_10_12.m2)
verifies the two literal cubic identities, the zero and infinity controls,
the nonzero-pair and coprime examples, and the actual opposite target-frame
transition. Captured execution status must be read from its own new
validation directory; a source file alone is not a successful run.
The first captured run passed the P identity but rejected the hand-expanded
J coefficients. The error was the sign of two terms from expanding
delta*r*(r-delta)^3; its source and raw failure are retained. The corrected
coefficients are +5delta^3-3delta^2 at r^2 and delta^3-delta^4 at r.
Two further runs retained fraction-field differentiation interface failures
after the first five conditions passed. The repaired first-neighborhood
ring implementation then passed all seven supporting conditions. These
four executions are one source lineage, not four independent certificates.
The [separate A4 cotangent checker](../computations/verify_session_nonendpoint_a4_cotangent_rank_2026_10_12.m2)
checks three literal local identities; the Nakayama and conductor argument
is a written proof, not a finite numerical extrapolation.
Separate independent auditors have been asked to reconstruct the quotient
identification, full chart scope and all-degree conductor argument. Those
audits are required before this note is promoted to the independently
audited frontier.

Next, combine the common-root incidence with the residual-divisor/fiber
conditions, retaining all denominator and infinity strata. The e=3 open
survives the numerical argument for k>=3, but section 3 excludes it when
Jbar!=0 by the separate support/conductor proof. The remaining closed
locus still needs full conductor power descent or a stronger geometric
obstruction.


---

## 2. nonendpoint restricted conductor determinant

# Nonendpoint quintics: the actual conductor quadric and its degree-eight restriction

Date: 2026-10-12. Author: `oct12_restricted_conductor_section`.

Status: **DIRECT STRUCTURAL THEOREM AND FINITE NECESSARY INCIDENCE;
independent mathematical audit requested**. This note concerns admissible
finite birational nonendpoint projections in the accepted characteristic-zero
genus-one quintic A4 normalization family for the fixed curve C0. It does not
assert that the necessary incidence is sufficient, empty, or globally exhaustive
for quintic carriers. All older notes and evidence seals remain unchanged.

## 1. Actual graded normalization and projection

Let T be the actual homogeneous anticanonical coordinate ring of S in P5.
The [explicit model audit](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md)
and its [exact model source](../computations/verify_session_quintic_a4_exact_ideal_2026_10_11.m2)
identify its defining ideal with the five quadrics

    q1=Z4^2-Z3 Z5,
    q2=Z2 Z4-Z1 Z5,
    q3=Z2 Z3-Z1 Z4,
    q4=Z2^2-Z3 Z4-Z0 Z5,
    q5=Z1 Z2-Z3^2-Z0 Z4.

The accepted source explicitly checks the free resolution over the six-variable
polynomial ring: its length is three, ranks are (1,5,5,1), and shifts are
(0,2,3,5). Thus T has depth three by Auslander--Buchsbaum; it is arithmetically
Cohen--Macaulay. This uses that actual resolution, not an inference from
normality alone. The accepted source SHA-256 is
`3a48626539da961ca68edd3d3b13a33d39cb154020e52a19c292d06e9ce77ca9`;
its existing [execution record](../validation/2026-10-11-quintic-a4-exact-ideal/execution-record.json)
is reused without a fresh full-model replay. The standard homological formula
was freshly consulted in [Stacks, tag 090U](https://stacks.math.columbia.edu/tag/090U).

Fix an admissible projection, and write R=k[X0,X1,X2,X3], acting on T by
the actual four sections. The projection center avoids S, so R_+T has radical
T_+ and T is finite over R. Its depth over the local ring R_(R_+) is three:
local cohomology with support in R_+ agrees with local cohomology with support
in T_+. Thus its minimal graded R-resolution has length one. The kernel of
R->T is (F), where F is the irreducible degree-five equation of the image.
Finite birationality implies rank one over R/(F).

The numerator of the Hilbert series over R is

    (1+3t+t^2)(1-t)=1+2t-2t^2-t^3.                       (1)

For any square length-one presentation M of T, det M is a scalar times F.
Indeed at the height-one DVR R_(F), T_(F) is killed by F and is a
one-dimensional vector space over its residue field, by birationality.
It has length one, so det M has valuation one at F. Every other height-one
localization of T is zero, so det M has no other prime factor.

## 2. The center-restriction rank-two case is retained and ruled out

Choose two complementary degree-one coordinates h,z, so the six-dimensional
degree-one space is spanned by X0,...,X3,h,z. Let C be the 5 by 3 matrix of
the coefficients of h^2,hz,z^2 in the five surface quadrics after X=0.
Its rank is at least two: rank zero or one would leave a common projective
zero on the binary center, contradicting center avoidance. Rank two is not
excluded by basepoint freeness alone; a binary quadratic pencil can be
basepoint free, and that case must be analyzed.

If rank C=2, its two independent quadrics form a regular sequence in k[h,z].
The binary quotient has Hilbert series 1+2t+t^2. Hence graded Nakayama gives
the minimal R-generators 1,h,z,w, of degrees 0,1,1,2. Equation (1) then forces
the minimal relations to have degrees 2,2,2,3. A square minimal presentation
has the row for w equal to (0,0,0,L), where L has degree one: the first three
entries have degree zero and must be zero by minimality. Consequently its
determinant factors as L times a degree-four determinant. Both factors must
be nonzero because the presentation has nonzero determinant. This contradicts
det M=scalar F with F irreducible of degree five.

Therefore every actual admissible finite birational quintic projection has

    rank C=3.                                           (2)

This conclusion depends on the Cohen--Macaulay resolution, the exact Hilbert
series, and birationality. It is not asserted for arbitrary basepoint-free
binary pencils or arbitrary projections of unrelated surfaces.

## 3. A quadric defining the entire upstairs conductor

Under (2), T/(R_+T) has Hilbert series 1+2t. Thus T is generated over R by
1,h,z. Its minimal presentation has two relations of degree two and one
of degree three. Write the degree-two relations as

    a1(X)+b1(X)h+c1(X)z=0,
    a2(X)+b2(X)h+c2(X)z=0,

where ai are quadrics and bi,ci are linear. Set

    D0=b1 c2-b2 c1.

Eliminating h or z in these two identities gives D0*h and D0*z as actual
cubic polynomials in R. Since 1,h,z generate T, D0*T is contained in the
image R/(F). Hence D0 belongs to the actual conductor.

D0 is not the zero polynomial. If it were zero, the two companion cubic
minors would vanish in T and hence belong to (F). Their degree is three,
less than five, so they would vanish identically in R. The first two columns
of the full presentation would then have all their 2 by 2 minors zero,
forcing its determinant to vanish, a contradiction.

The accepted [entire-conductor calculation](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
gives the actual upstairs ideal I_S=O_S(-2H). The nonzero quadric D0,
pulled back to S, is a section of I_S(2H)=O_S. Since S is integral and
projective, this section is a nonzero scalar. Therefore

    div_S(nu^*D0)=Dc, including every multiplicity.        (3)

This is an identification of the entire actual conductor upstairs. It does
not make the downstairs conductor principal. Downstairs its ideal is
D0*nu_*O_S, with generators D0,D0*h,D0*z in local compatible frames;
the cubic companions retain its nonreduced and branch structure.

There is also a shorter existence and uniqueness proof that does not use
presentation charts. Finite normalization gives nu_*I_S=I_X as actual ideals.
Hence H0(X,I_X(2))=H0(S,O_S)=k. The quintic hypersurface sequence
0->O_P3(-3)->O_P3(2)->O_X(2)->0 and H1(P3,O(-3))=0 lift this unique
nonzero conductor section to an ambient quadric. Its pullback generates
I_S(2H), yielding (3). The graded-module proof remains necessary here for
the explicit determinant formula and rank-three coverage of its center charts.

## 4. A universal five by five determinant, with no center-pivot division

Write each of the five transformed quadrics in the exact form

    qi=ai(X)+bi(X)h+ci(X)z+Ci0 h^2+Ci1 hz+Ci2 z^2.

Let N(X) be the 5 by 5 matrix with row

    (Ci0,Ci1,Ci2,bi(X),ci(X)).

Then

    D(X)=det N(X)                                        (4)

is an actual ambient quadric. On any of the ten parameter charts where
a 3 by 3 center minor Delta is nonzero, eliminate the corresponding three
quadrics from the other two. The Schur-complement identity gives

    det N=Delta*det(two remaining h,z coefficient rows),

up to the fixed row-permutation sign. The latter determinant is D0 for a
basis of the two quadratic relations. Therefore D(X) is nonzero and gives
the same entire divisor (3), up to a nonzero parameter scalar. All ten
rank-three center charts are retained by (2); expression (4) itself has
no division by a center minor. If a chosen minor vanishes, another minor
supplies the proof. The formula is not extended as a conductor claim to
rank-two inadmissible centers.

## 5. Explicit nonendpoint coordinates and the restricted binary octic

Use the actual parameters of the
[target-fiber note](2026-10-12-session-nonendpoint-target-fiber-reduction-and-bounded-exclusions.md):

    B=b-a, G=g-3b+2a, Jbar=d-2g+2b-a, delta!=0.

Take h=T=Z2+Z3 and z=U1=Z4 as complementary coordinates. The exact inverse
linear substitution is

    U3=(X0-X1+B h)/delta,
    U2=(X2-3X1+2X0-G h+delta^3 z)/(3delta^2),
    U0=(X3-2X2+2X1-X0-Jbar h+2delta^3 z)/delta^4,
    Z0=X0-a h-U3, Z1=-U3, Z2=h-U2,
    Z3=U2, Z4=z, Z5=U0.                                 (5)

Only the stipulated nonzero delta, and the characteristic-zero scalar 3,
are divided out. Substituting (5) into the five displayed quadrics defines
the matrix N without any elimination or generic parameter specialization.

Define the homogeneous degree-eight binary form

    Fdet(P,Q)=81 delta^10
       D(Q^4,Q^3(Q-P),Q(Q-P)^3,(Q-P)^4).                 (6)

The fixed scalar is convenient for the fiber norm comparison. Its affine
chart Q=1 uses p=P/Q=1-z_target. The intrinsic A4 point is p=0; target
infinity is Q=0. The form is nonzero for every admissible projection. On the
smooth target quadric, the quintic restriction has class (5,5) and C0 has
class (1,3). Its multiplicity along C0 is one: multiplicity at least two
would leave an effective residual of negative second bidegree. At generic C0,
the regular two-dimensional local ring of P3 has parameters q,u, where q
defines the smooth quadric and u defines C0 on it. Since F modulo q has
u-order one, F is not in the square of the maximal ideal. Thus X is regular
at generic C0, and its normalization is an isomorphism there. The conductor
cannot contain c. This argument is independent of full inverse support.

Formula (6) includes all multiplicities of Dc|c. Its degree is exactly eight
as a homogeneous form, even if the affine p-polynomial loses leading terms.
The scalar delta is retained as a modulus. A polynomial expression with
integer rational coefficients can be obtained by clearing only the explicit
powers of delta in (5); no locus in a,B,G,Jbar is inverted.

The computed A4 value is

    Fdet(0,1)=-3 Jbar Delta1,

    Delta1=G(G+3delta^2)(G+delta^2+2B)
       +Jbar[(delta^2-5B)G-3B(delta^2+3B)]-B Jbar^2.      (7)

Thus conductor at this target can arise from either the actual A4 rank drop
Jbar=0 or the second-point condition Delta1=0. This is an exact value, not
an equality between the first-normal common divisor and the full conductor.

## 6. A finite necessary incidence retaining arbitrary conductor multiplicities

Suppose a mate exists. Its full inverse target support is exactly c.
At every finite smooth point of c where the two actual conormal symbols
do not vanish together, the cotangent map is surjective. The finite
single-fiber Nakayama argument in the
[conormal/conductor audit](2026-10-12-session-nonendpoint-all-mate-conormal-conductor-independent-audit.md)
makes the normalization a local isomorphism there, so Dc misses that point.
At A4 the same argument applies if Jbar!=0.

Let Pn(P,Q),Jn(P,Q) be the degree-three binary forms obtained from the actual
conormal cubics by the source change r=delta Q/P, explicitly by homogenizing
p^3 P(delta/p)/delta^3 and p^3 J(delta/p)/delta^3. This is an invertible
binary-coordinate change for delta!=0. It retains the finite source point
r=0 as Q=0, the intrinsic A4 point as P=0, and all repeated common roots.
Let H be their complete homogeneous gcd, of degree h0 from zero to three.
Let epsilon=1 when Jbar=0 and epsilon=0 otherwise. The support conclusion
just proved is exactly the necessary condition

    supp div(Fdet) subset supp div(H P^epsilon).          (8)

No local conductor multiplicity is bounded by h0, by the multiplicities of
H, or by a first-normal coefficient. Its total degree eight is used instead.
For binary forms over the algebraically closed field, (8) is equivalent to

    Fdet divides (H P^epsilon)^8.                        (9)

Indeed every root exponent of Fdet is at most eight, while every allowed
root occurs in H P^epsilon with exponent at least one. This gives a finite
denominator-free polynomial incidence: for each h0=0,1,2,3 and epsilon=0,1,
introduce binary forms H,A_P,A_J,K and impose

    Pn=H A_P, Jn=H A_J,
    (H P^epsilon)^8=Fdet K,
    deg A_P=deg A_J=3-h0,
    deg K=8(h0+epsilon-1).                              (10)

Impose nonzero H,Fdet and the stated Jbar condition. The case
h0=epsilon=0 is empty because a nonconstant Fdet cannot divide one.
Taking h0 equal to the complete gcd proves necessity; allowing a smaller
common H may add restrictions but cannot create a purported sufficient
STCI condition. One may alternatively factor Fdet into at most four
allowed linear factors with positive exponents summing to eight. Both
descriptions preserve all possible high contact at each allowed point.

This is a necessary incidence for the actual restricted conductor. It does
not certify full inverse support, full conductor-ring power descent, center
avoidance, or existence of a mate. In particular, the quadratic/cubic target
fiber equations on pZ!=0, their Z=0 and p=0 charts, the endpoint chart, and
the allowed doubled r=delta/p fibers remain separate necessary conditions.

## 7. Evidence and continuation boundary

### 7a. Exact comparison with the residual norm, retaining leading drops

On the regular target chart pZ!=0, use the actual quadratic A2 and cubic C3
from the target-fiber reduction. Write

    A2=A r^2+b r+c,
    C3=p A^2 r^3+d r^2+e r+f,
    K0=d-p A b, E0=e-p A c.

The exact compact polynomial norm is

    N0=A c E0^2-b K0 c E0-A b E0 f+b^2 K0 f
        +A^2 f^2-2A K0 c f+K0^2 c^2.

Literal polynomial identities give

    Res_r(A2,C3)=A N0,
    N0=p^2 delta^6 Z^2 Fdet(p,1).                       (11)

Thus a fixed-degree Sylvester determinant has an extraneous factor A,
which must not be used as an off-c point certificate. At A=0 the cubic
quadratic coefficient is d=-p[3delta^2 p(2-p)]^2. It is nonzero on pZ!=0,
because A=0 forces Z=-3delta^2 p(2-p)!=0. In this case the normalized norm is

    N0=d(d c^2-e b c+f b^2),

and detects exactly the affine common roots of the remaining linear A2
and quadratic C3, including the cases b=0. If b=0,c!=0 there is no root
and N0=d^2c^2!=0; if b=c=0 the quadratic C3 has a root and N0=0. When
A!=0 both leading coefficients are nonzero and the usual resultant also
detects exactly the affine common roots. Hence on the stipulated regular
chart, Fdet=0 is exactly the residual common-root condition, with no leading
degree-drop artifact left.

The identity (11) holds polynomially before making any chart restriction.
Its geometric residual-root interpretation is confined to pZ!=0. At Z=0,
p=0, and target infinity, the actual conductor determinant (6) remains
defined; the separate denominator-free target-fiber systems remain required.
Likewise a common residual root r=delta/p is retained: it can be an allowed
ramified doubled fiber, rather than an off-c inverse point.

For additional checking, if L_inf is the coefficient of p^8 in Fdet(p,1),
the literal endpoint identity is

    Res_r(Pinf,Qinf)=B^2 delta^2 L_inf,
    L_inf|B=0=a G[(3delta^2+G)a-delta^3].                (12)

The B=0 factor must not be discarded using the generic resultant identity.
It reflects both the direct off-c endpoint alternatives and the conormal
root when a=B=0, precisely as in the complete target-fiber analysis.

### 7b. Captured evidence and unresolved incidence

The graded-module proof and the universal determinant give the structural
identification. The separate
[diagonal/norm source](../computations/verify_session_nonendpoint_diagonal_norm_2026_10_12.m2)
passes fifteen exact supporting checks, including the literal identity
Fdet(p,1)=81 delta^10 D(1,1-p,(1-p)^3,(1-p)^4). Its final captured
[execution record](../validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/execution-record.json)
has exit zero and empty stderr. The source SHA-256 is
`cc188b7ee97b91710f519d4c357184383437b8b492aad97e09c33c3138cd99e2`.
This is one supporting checker, not fifteen independent proofs. Its two
earlier interface-failure captures remain retained separately.

The owner's eight exploratory formula/interface sources are also preserved
in a [separate replay inventory](../validation/2026-10-12-nonendpoint-conductor-determinant-probes/inventory.json).
They comprise six failed interface replays and two successful formula-printing
replays. The initial tool outputs were not originally written to files;
the inventory labels every capture as an explicit replay of the exact
preserved source. These probes contain no asserted mathematical checks,
and their PASS completion printing is not added to the supporting check count.

An independent audit of the module and conductor argument has been assigned.
No broad parameter Groebner elimination was launched here.

The next work is to use (10) and (11) on the surviving homogeneous conormal
common-root strata. The actual octic replaces a contact heuristic with explicit
full conductor multiplicities; emptiness of its remaining parameter incidence
is still open.


---

## 3. nonendpoint conormal and socle independent audit

# Nonendpoint quintics: corrected conormal cubics and necessary socle bound

Date: 2026-10-12. Auditor:
`oct11_quartic_assembly_audit/degree_factor_audit`, independently assigned
by root. Status: **CORRECTED EXACT IDENTITIES AND DIRECT GLOBAL-FRAME
AUDIT; NECESSARY DEGREE RESTRICTIONS ONLY**.

This note audits the actual nonendpoint family in section 1 of the
[pole-filtration and line-jet note](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-12-session-nonendpoint-pole-filtration-and-line-jetmd),
using the accepted intrinsic A4 pair and fixed characteristic-zero
C0. It does not re-audit every argument of that note, classify its
entire conductor, or exclude generic mates in all degrees. The
projection center must still miss S for an admissible normalization.
No canonical, sealed, or previously frozen proof file is changed.

## 1. The proposed J expansion failed and is explicitly superseded

The first independent execution passed P, both opposite balanced-frame
transitions, and the socle arithmetic, but failed the displayed J
expansion and the moving U first-normal identity. This is an actual
mathematical coefficient failure, not a scaffold or environment failure.
Root independently identified the same expansion error.

The incorrect J had r^2 coefficient
`3delta(g-b)-delta^3-3delta^2` and r coefficient
`3bdelta^2+delta^3+delta^4`. The correct coefficients are

    r^2: 3delta(g-b)+5delta^3-3delta^2,
    r:   3bdelta^2+delta^3-delta^4.

The difference of the correct and incorrect polynomials is
`2delta^3*r*(3r-delta)`, nonzero for every delta!=0 in characteristic
zero. The earlier preliminary approval of that expansion is withdrawn.
The original failed source and raw streams are preserved in
[attempt 01](../validation/2026-10-12-nonendpoint-conormal-independent-audit/attempt-01-wrong-J-expansion/execution-record.json).

## 2. Derivation from the actual moving target coordinates

Let s=r-delta, delta!=0, and use the actual section family in the
linked note. On c its restrictions are

    X0=r^4, X1=r^3*s, X2=r*s^3, X3=s^4.

Write Ai=(partial_T Xi)|c. Then

    A0=a-2r^2-r,
    A1=b+delta*r-2r^2-r,
    A2=g+3delta*r-2r^2-r,
    A3=d+4delta*r-2r^2-r.

On the target chart x0!=0 the actual moving support coordinate is
z=x1/x0, whose restriction is s/r. Define the balanced residuals

    V=x2/x0-z^3,
    U=x3/x0-(3/2)z*(x2/x0)+(1/2)z^4.

Differentiating all the target ratios, including z, gives

    V_T=P/r^7, U_T=J/(2r^7),
    P=r^3*A2-3r*s^2*A1+2s^3*A0,
    J=2r^3*A3-3s*r^2*A2+s^3*A1.

Expanding those identities yields exactly

    P=(g-3b+2a)r^3
      +[6delta(b-a)+delta^3-3delta^2]r^2
      +[delta^2(6a-3b)+2delta^3]r-2a delta^3,

    J=(2d-3g+b)r^3
      +[3delta(g-b)+5delta^3-3delta^2]r^2
      +[3bdelta^2+delta^3-delta^4]r-b delta^3.

The coefficients of U would be wrong if z were frozen to its value
on c before differentiating. The independent checker reconstructs
the entire section family and takes its actual ratio jets.

## 3. The opposite balanced frame has the same scalar transition

In the first target chart write, to first normal order,

    x0=1, x1=z, x2=z^3+V,
    x3=z^4+U+(3/2)zV.

On the opposite chart put the actual moving coordinate w=x2/x3 and

    a_inf=x1/x3-w^3, b_inf=x0/x3-w^4,
    Vraw_inf=a_inf, Uraw_inf=b_inf-(3/2)w*a_inf.

Expansion modulo I_C^2 gives

    a_inf=2z^(-7)U,
    b_inf=3z^(-8)U+(1/2)z^(-7)V.

Consequently the correct adjusted frame is

    Uop=Vraw_inf/2, Vop=2Uraw_inf,
    Uop=z^(-7)U, Vop=z^(-7)V modulo I_C^2.

Both components have the same scalar transition. In particular their
projective ratio glues as a map to a fixed P1, with no residual swap
or unequal twist. On the source r-chart this also gives

    (Uop)_T=J/[2(r-delta)^7],
    (Vop)_T=P/(r-delta)^7.

Thus r=0, which maps to the opposite target endpoint, is covered
correctly. The intrinsic r=infinity point maps to target z=1;
it must also be retained when homogenizing the cubics.

## 4. Homogeneous gcd determines the saturated quotient degree

Let P_h(R,S)=S^3 P(R/S), J_h(R,S)=S^3 J(R/S), and let Gamma be
their homogeneous gcd, of degree h. The pair cannot be identically
zero when delta!=0. Indeed their constant coefficients force a=b=0,
after which P's r coefficient is 2delta^3. Equivalently the exact
denominator-free witness is

    delta*[r]P + 3*[1]P - 3*[1]J = 2delta^4.

After dividing by Gamma, the pair is basepoint free and consists of
binary forms of degree 3-h. Its induced P1 map therefore has degree

    e=3-h, with 0<=e<=3.

This includes a common zero at R/S=infinity and the case where
one polynomial is identically zero. Taking only an affine gcd could
miss a common infinity factor.

For a hypothetical quasiprimitive defining CI, the first saturated
BF quotient is a line bundle L with a surjection
`N_C^*=O(-7)^2 ->> L`. Its generic quotient images are precisely
the displayed U_T,V_T, up to one common rational scalar. Generic
regularity of the quintic and birational normalization identify these
with the actual transverse direction at the generic point. Saturating
the kernel globally determines this quotient uniquely. The adjusted
frame above makes its projective direction pair `[J_h:2P_h]`;
passing to the annihilating first-normal relation `[2P_h:-J_h]`
uses only a constant invertible change of basis. Thus both have the
same homogeneous gcd degree, and

    L=O_P1(e-7), e=3-deg Gamma.

This deduction uses the actual global saturated quotient, not a
choice of first-normal generators with a prescribed common scale.
It imposes no divisibility of one equation's first-normal scalar by
the other's; nonregular first-normal ratios remain permitted.

As an algebraic check that the coprime locus is not identically absent,
delta=1,a=1,b=g=d=0 gives

    P=2r^3-8r^2+8r-2, J=2r^2.

The only finite root of J is zero, where P=-2, and P's leading
coefficient is two, so the homogeneous pair has no infinity common
factor either. This is a polynomial-family check, not a declaration
that this particular projection center is admissible or gives a mate.

## 5. Socle inequality for every hypothetical CI(5,4k)

The quintic is regular at the generic point of C0, so a hypothetical
CI(5,4k) is generically curvilinear of multiplicity m=5k. Complete
intersection adjunction gives `omega_Y=O_Y(4k+1)`. Its top saturated
BF piece is

    E_(5k-1)=Ann_(O_Y)(I_C)
            =omega_C tensor (omega_Y|C)^(-1)
            =O_P1(-16k-6).

The generically nonzero multiplication of the first piece into that
top piece gives `E_(5k-1)=L^(5k-1)(D_top)` with D_top effective.
It follows that

    deg D_top=(5k-1)(7-e)-6-16k
             =(19-5e)k+e-13 >=0.

For k=2, the four possibilities e=0,1,2,3 give respectively
`25,16,7,-2`. Therefore a hypothetical (5,8) pair requires e<=2,
equivalently a nonconstant homogeneous common factor of P_h,J_h.

For coprime cubics e=3, the same condition is `4k-10>=0`, which
requires k>=3. It excludes degree eight and leaves degree twelve
and larger permitted by this one necessary inequality. It is not
an exclusion of generic mates in all degrees or an existence theorem
in the retained degrees. Closed-point defect divisors, nonregular
ratios, higher jets, center avoidance and entire conductor descent
still require their own arguments.

## 6. Preserved executions and exact evidence scope

The final independent standard-library
[source](../validation/2026-10-12-nonendpoint-conormal-independent-audit/verify_conormal.py)
passes twelve exact checks. Its SHA-256 is
`e5a8b003dbec8bcef1d23636e5d50bd058ee25a3ddb3411b00140e1bf9fa29a7`.
The [current execution record](../validation/2026-10-12-nonendpoint-conormal-independent-audit/execution-record.json)
binds the exact source, actual exit zero, command, interpreter,
elapsed time, and separate raw streams.

Attempt 01 preserves the mathematically false J expansion. Attempt 02
preserves the first successful corrected-J source and complete record.
The final execution changes only the printed coefficient-ring metadata
to include the r^-1 used during ratio normalization; it retains the
same twelve mathematical checks. These are three executions of one
checker lineage, including one genuine mathematical failure, rather
than three independent verifiers. The recording wrapper is not a
mathematical verifier. No frozen historical execution index is inflated.

The calculations verify the stated identities. The global saturation
argument and the socle-duality proof supply their geometric scope.


---

## 4. conductor quadric module independent audit

# The quintic conductor quadric: independent module, ideal and incidence audit

Date: 2026-10-12. Author: `degree_factor_audit`.
Status: **DIRECT INDEPENDENT STRUCTURAL PROOF AUDIT; ACTUAL CONDUCTOR
QUADRIC AND ALL ADMISSIBLE CENTER RANKS VERIFIED**. The restricted-octic
incidence remains a necessary condition. Its emptiness and the global STCI
question remain open.

This audit binds the frozen owner note
[nonendpoint restricted conductor determinant](2026-10-12-session-nonendpoint-restricted-conductor-determinant.md),
SHA-256 `fbd0cadc994d9aa40d2459f7853889ad958d82be4744fce8df3e868bb0faf0fb`.
No owner, canonical, previously frozen or Git file was edited. Work over an
algebraically closed field of characteristic zero. The actual normalization
pair and its finite birational projection are inherited from the accepted
quintic lane; this theorem does not classify unrelated normalizations.

## 1. Actual ring, normality, finite graded module and its depth

Let T be the homogeneous coordinate ring of the literal anticanonical
degree-five A4 model S in P5. The accepted
[explicit model](2026-10-11-session-dp5-a4-explicit-model-independent-audit.md)
and [exact source](../computations/verify_session_quintic_a4_exact_ideal_2026_10_11.m2)
give a prime ideal generated by the five displayed quadrics. The source
actually asserts resolution length three, ranks (1,5,5,1), and shifts
(0,2,3,5), in addition to dimension three and the complete elimination
kernel. Its SHA-256 is
`3a48626539da961ca68edd3d3b13a33d39cb154020e52a19c292d06e9ce77ca9`.
The current source agrees with that accepted hash; no fresh replay of its
seventy-two-condition model audit is claimed here.

Auslander--Buchsbaum over the regular six-variable ring gives depth(T)=3,
so T is arithmetically Cohen--Macaulay. This conclusion does not follow
from normality of the projective surface alone. The projective charts are
normal by the accepted direct A2 and A4 chart arguments. Off the cone
vertex, the cone is locally a Gm bundle over those normal charts; its
height-one localizations are therefore normal. The vertex has codimension
three, and T is S2 by Cohen--Macaulayness. Serre's criterion gives normality
of T as well. Depth at least two also identifies T with the full section
ring of O_S(H), so the anticanonical model is projectively normal.

Set R=k[X0,X1,X2,X3] abstractly, with its action through the four actual
degree-one projection sections. Center avoidance says that
Proj(T/(R_+T)) is empty; hence rad(R_+T)=T_+. The quotient is a finite
graded k-vector space. Lifting a homogeneous basis and inducting on degree
expresses every element of T as an R-linear combination of those lifts.
Thus T is a finite graded R-module, without assuming it in order to use
graded Nakayama.

After localizing R at its homogeneous maximal ideal, there is exactly one
maximal ideal of T above it, because rad(R_+T)=T_+. Its localization has
depth three. The finite-map depth equality therefore gives depth_R(T)=3;
see the freshly checked
[Stacks finite-map depth lemma 0AUK](https://stacks.math.columbia.edu/tag/0AUK).
Equivalently, local cohomology has the same support radical. The regular
four-variable R has finite global dimension, and
[Auslander--Buchsbaum 090U](https://stacks.math.columbia.edu/tag/090U)
gives pd_R(T)=1. A minimal graded resolution remains minimal after
localizing at R_+, so it has the same length one globally.

The kernel of R->T is the height-one prime (F), with F the irreducible
quintic equation of the image. Finite birationality gives rank one over
A=R/(F). At the level of fraction fields this is also a statement about
the cones: choose a nonzero projection coordinate X0. The projective
function fields agree, and both cone fraction fields are generated by
that common function field and X0. Thus Frac(A)=Frac(T).

## 2. Why the presentation determinant is F, not a power of F

The length-one resolution is a square free presentation

    0 -> F1 --M--> F0 -> T -> 0.

Its determinant is nonzero because T is torsion over R and the map is
injective between free modules of equal rank. Localize at the height-one
DVR R_(F). The module T_(F) is killed by F and is one-dimensional over
the residue field Frac(A), by the rank-one statement above. Its length
is exactly one. Smith normal form over this DVR consequently gives
valuation_F(det M)=1.

At every other height-one prime, F is a unit and T localizes to zero.
The presentation is then an isomorphism, so det M has no other prime
factor. Since R is a UFD,

    det M = nonzero scalar * F.

This proves the precise determinant assertion for every admissible
projection. It does not use an unspecified generic rank or identify a
support equation with a higher-power Fitting equation.

## 3. All center-restriction ranks and exact generator degrees

Choose complementary degree-one coordinates h,z. Modulo R_+, the entire
ring is exactly k[h,z] divided by the restrictions of the five defining
quadrics. Let C be their 5 by 3 coefficient matrix in h^2,hz,z^2, and
let s=rank(C). These are all the generators of the restricted ideal;
no unexamined higher defining equations occur.

Ranks zero and one leave a projective point on the binary center, so
center avoidance rules them out. At rank two, the two independent
quadrics have no common projective root. They therefore have no common
factor and form a regular sequence in k[h,z]. The entire Artinian
quotient has Hilbert series 1+2t+t^2. At rank three it is exactly
k[h,z]/(h,z)^2, with Hilbert series 1+2t.

The Hilbert numerator of T over R is

    1+2t-2t^2-t^3.

Graded Nakayama determines all minimal generators from the Artinian
quotient. Since pd_R(T)=1, subtraction from this numerator determines
all relation degrees, not merely their number:

    rank two: generators 0,1,1,2; relations 2,2,2,3;
    rank three: generators 0,1,1; relations 2,2,3.

At rank two, the row for the generator of degree two has entries
(0,0,0,L) in the minimal 4 by 4 presentation. The first three entries
have degree zero and must be zero by minimality. Thus det M has the
linear factor L. L and the complementary determinant are both nonzero,
since det M is nonzero. This contradicts the irreducibility of the
degree-five F. Therefore every admissible center has rank three.

This argument explicitly covers the base-point-free binary rank-two
pencil. It does not incorrectly rule it out by base-point freeness alone.
It also leaves no admissible higher-generator chart outside the proof.

## 4. Actual nonreduced conductor membership and a shorter existence proof

At rank three, T is generated by 1,h,z. Write its quadratic relations as

    a1+b1*h+c1*z=0,  a2+b2*h+c2*z=0,

with ai quadrics and bi,ci linear in X. Put D0=b1*c2-b2*c1. Then the
literal elimination identities give

    D0*h=c1*a2-c2*a1,
    D0*z=b2*a1-b1*a2.

Both right sides are cubic polynomials in R. Hence D0*T is contained
in A, because 1,h,z generate the whole T. This is membership in the
actual conductor A:T, not merely vanishing on its radical or on one
branch of the normalization.

If D0=0, the two companion cubics vanish in T. They lie in the kernel
(F), but have degree three, so they vanish as polynomials in R. All
2 by 2 minors of the first two columns of the 3 by 3 presentation then
vanish. Those columns have rank at most one over Frac(R), making the
full determinant zero, contrary to Section 2. Thus D0 is nonzero.

For a finite birational inclusion A subset T with the same fraction
field, Hom_A(T,A) is identified with A:T by evaluating at 1: every
homomorphism is multiplication by its generic scalar, and its value at
1 belongs to A. This is simultaneously an ideal of A and T. Therefore
the projective conductor ideals satisfy nu_*I_S=I_X exactly, including
nilpotent and branch structure.

The accepted actual canonical equalities are

    omega_X=O_X(H), omega_S=O_S(-H).

Finite duality gives the actual invertible conductor ideal
I_S=O_S(-2H). The finite-duality mechanism was freshly checked in
[Stacks 0AX1](https://stacks.math.columbia.edu/tag/0AX1); this uses the
dualizing sheaves and the finite Cohen--Macaulay map, not only a
numerical canonical divisor class. Twisting D0 by 2H now makes it a
nonzero global section of I_S(2H)=O_S. Proper integral S has only
constant global functions. This section is a unit, so D0 generates the
entire upstairs conductor, with every multiplicity.

There is an independent shorter proof of existence and uniqueness.
Projection formula and the exact conductor equality give

    H0(X,I_X(2))=H0(S,I_S(2H))=H0(S,O_S)=k.

Every section of O_X(2) comes from an ambient quadric: the quintic
hypersurface sequence has terms O_P3(-3), O_P3(2), O_X(2), and
H1(P3,O(-3))=0. This vanishing is the freshly checked
[projective-space cohomology formula 01XS](https://stacks.math.columbia.edu/tag/01XS).
Also H0(P3,O(-3))=0, so the lift is unique. Thus the unique ambient
conductor quadric, up to a nonzero scalar, exists directly from the
accepted actual conductor sheaf. The presentation proof additionally
supplies its formula and center-rank coverage.

The downstairs conductor is not generated by D0 alone. Its ideal is
D0*nu_*O_S, with the cubic companions D0*h and D0*z as additional
generators in compatible frames.

## 5. The universal determinant and an auxiliary exact conductor resolution

Write the five original quadrics as

    qi=ai(X)+bi(X)h+ci(X)z+Ci0*h^2+Ci1*h*z+Ci2*z^2.

On each chart where one of the ten 3 by 3 minors Delta of C is nonzero,
row elimination removes the three quadratic monomials h^2,hz,z^2.
The remaining two equations are independent quadratic relations: a
constant dependence between them would be a dependence between the
five original defining quadrics. The Hilbert calculation in Section 3
says there are exactly two independent degree-two relations, so these
form their basis.

Block determinant expansion gives

    det[C | b | c] = sign * Delta * D0.

The chosen Delta is a nonzero scalar at that particular projection.
Every admissible center lies in at least one such chart. Consequently
the universal 5 by 5 determinant is nonzero and gives the same entire
conductor divisor on all charts. A vanishing chosen minor causes no
omission: another minor applies. The universal expression itself has
no pivot denominator.

For clarity about the actual downstairs scheme, put

    E=a1*c2-a2*c1=-D0*h, K=a1*b2-a2*b1=D0*z.

The three generators of the downstairs conductor ideal are D0,E,K.
The full determinant expands as a3*D0-b3*E+c3*K=scalar*F. Thus F is
already in their ideal. Any irreducible common divisor of D0,E,K would
divide F, but cannot equal F because D0 is nonzero of degree two.
Their greatest common divisor is one.

There is a direct proof of the Hilbert--Burch resolution in this case.
The two columns (a1,b1,c1) and (a2,b2,c2) have rank two and are polynomial
syzygies of the signed minors. Over every height-one DVR at least one
minor is a unit, so every polynomial syzygy is an R_p-linear combination
of the two columns. Its uniquely determined coefficient pair belongs
to every height-one R_p. Since the UFD R is the intersection of those
DVRs inside Frac(R), the pair belongs to R itself. Hence these columns
generate the entire syzygy module, and

    0 -> R(-4)^2 -> R(-2) plus R(-3)^2 -> I_Gamma -> 0

is exact. The gcd-one condition gives height at least two; this
resolution and Auslander--Buchsbaum give height at most two and
Cohen--Macaulayness. The ideal is saturated, and the Hilbert series of
R/I_Gamma is

    (1-t^2-2t^3+2t^4)/(1-t)^4
      =(1+2t+2t^2)/(1-t)^2.

Thus the actual downstairs conductor is an arithmetically
Cohen--Macaulay degree-five genus-two determinantal curve. This is an
auxiliary proved consequence; it retains nonreduced cases and does
not assume a flat degree-two conductor cover.

## 6. The restriction to c and finite necessary incidence

The nonendpoint inverse coordinate substitution in owner equation (5)
is invertible for delta!=0. It divides only by powers of delta and by
the characteristic-zero scalar three. Its five-quadratic determinant
therefore covers the whole displayed parameter family, subject to
center avoidance.

The conductor does not contain c, independently of any mate or full
inverse-support assumption. Indeed the smooth target quadric containing
C0 has C0 of class (1,3), and the integral quintic restricts to a nonzero
section of class (5,5). Multiplicity at least two along C0 would leave
an effective divisor of negative second bidegree. The multiplicity is
therefore exactly one. At the generic point of C0, the regular local
ring of P3 has parameters q for the quadric and u for C0 within it.
F modulo q has u-order one, so F does not belong to the square of the
maximal ideal. The quintic local ring is regular there, and normalization
is an isomorphism. Hence its conductor cannot contain c.

The nonzero restriction of the conductor section is consequently a
homogeneous degree-eight binary form. Affine degree loss records a
root at target infinity, not the disappearance of an intersection.
The change r=delta*Q/P is invertible on the binary parameter line,
so it preserves every repeated common root of the homogeneous
conormal pair and correctly exchanges source r=0 with target Q=0.

Under a hypothetical mate, full inverse support makes the finite
normalization algebra local over every target point of C0. At a
smooth-source point with at least one conormal symbol nonzero, its
cotangent map is surjective. The two finite Nakayama steps in the
accepted conormal/conductor audit then give an exact local ring
isomorphism. At A4, the full three-dimensional cotangent determinant
is -3delta^3*Jbar, so the same conclusion holds if Jbar!=0. Both
single-preimage finiteness and the entire singular cotangent space
are retained.

Therefore the support of the restricted conductor form Fdet is contained
in the homogeneous gcd H of the transformed conormal cubics, together
with P=0 when Jbar=0. For a degree-eight binary form this support
inclusion is equivalent to

    Fdet divides (H*P^epsilon)^8,
    epsilon=1 if Jbar=0, and zero otherwise.

The exponent eight bounds each root exponent by the total degree of
Fdet. It does not equate conductor multiplicity with first-normal
multiplicity. The owner's finite incidence in H,A_P,A_J,K therefore
preserves every possible multiplicity distribution, including a single
root of order eight. The h0=epsilon=0 case is empty; all other displayed
degrees are nonnegative. This remains only a necessary incidence.

## 7. Compact norm: the apparent leading factor and every degree drop

The owner writes A2=A*r^2+b*r+c and
C3=p*A^2*r^3+d*r^2+e*r+f. Put K0=d-p*A*b and E0=e-p*A*c.
Modulo A2 the cubic has linear remainder

    ((A*E0-b*K0)*r+(A*f-c*K0))/A.

For A!=0, taking the quadratic norm gives the stated identity
Res(A2,C3)=A*N0. Expanding this expression gives exactly the seven
terms of the owner's compact N0. This independently explains the
apparently extraneous factor A rather than treating a zero resultant
as an off-c certificate on a leading-drop locus.

Write the leading two coefficients of the owner's N polynomial as
n2=3delta^2*p*(2-p) and n1=-delta^3*(6-p^2). Comparison of the
r^3 coefficients in Psi=(pr-delta)C3 gives

    d=A*(p*(2*n1+n2)+delta*A)-p*n2^2.

At A=0, Z=-n2, so on pZ!=0 one has d=-p*n2^2!=0.
The compact expression specializes to

    N0=d*(d*c^2-e*b*c+f*b^2).

For b!=0 the second factor is the exact linear/quadratic common-root
test. For b=0,c!=0 it is nonzero; for b=c=0 the genuine quadratic
C3 has a root over the algebraically closed field. All leading drops
are therefore retained. The normalized norm has exactly the claimed
affine common-root interpretation on pZ!=0, including a possible root
r=delta/p representing an allowed doubled c-fiber.

The literal comparison N0=p^2*delta^6*Z^2*Fdet, its scalar normalization
81delta^10, and the A4/endpoint special values are supplied by the
separate accepted fifteen-identity source. I inspected its exact
construction of the five quadrics, independent coefficient matrix,
quotient identities and captured PASS stream, and verified its source
and stream hashes. No separate fresh symbolic replay of that source
is claimed here. Its exact calculation supports the literal scalar
comparison; the structural proof in Sections 1--5 establishes why the
determinant is the actual conductor.

The endpoint identity retains its B=0 specialization explicitly, and
the geometric norm interpretation is not extended across Z=0, p=0
or target infinity. Those targets retain their separate exact fiber
equations. In particular Fdet=0 is not itself an off-c exclusion when
the common residual root is the allowed doubled c-fiber.

## 8. Evidence accounting and continuation boundary

This audit is a new written structural proof. It launches no new CAS
calculation: the accepted seventy-two-condition model source and the
separate fifteen-identity diagonal/norm source are reused with their
actual captured records. Their check counts do not count as new
independent checker lineages or new executions by this auditor.

The latter source SHA-256 is
`cc188b7ee97b91710f519d4c357184383437b8b492aad97e09c33c3138cd99e2`;
its [captured record](../validation/2026-10-12-nonendpoint-diagonal-norm/20261012T212553449292Z/execution-record.json)
records exit zero and empty stderr. Its sixteen PASS markers comprise
fifteen asserted identities and one completion marker. The owner's
formula-printing probes and retained interface failures remain separate
from those fifteen checks and from this proof.

No failing structural step or omitted admissible center rank was found.
The general finite incidence has not been proved empty. Actual center
avoidance, full inverse support, the exceptional target-fiber equations,
and full conductor-ring power descent are still required in every
remaining common-root stratum. Higher-degree carriers and other quintic
normalization genera lie outside this theorem.


---

## 5. nonendpoint all mate conormal conductor independent audit

# Nonendpoint quintics: independent all-mate conormal/conductor audit

Date: 2026-10-12. Auditor:
`oct11_endpoint_support_global_audit/two_root_contact_audit`.

Status: **PASS: direct independent geometric proof of a necessary locus in
every mate degree.** This sharpens the generic degree-eight restriction,
but does not exclude the remaining resultant and A4 cotangent loci, all
nonendpoint projections, all quintic carriers, or fixed C0 itself.

The audited cubic data are in
[the corrected conormal reduction](2026-10-12-session-nonendpoint-conormal-cubic-reduction.md),
as read with SHA-256
`3576392d41d4f64db506291f7cd0609a6930a80296eeedd7c9ccdfa92352c3f5`.
This new note also audits root's proposed geometric extension, which is
written out below rather than inferred from the earlier numerical bound.
No prior note, canonical record or seal-bound file was changed. No new
CAS execution was needed to resolve an identity gap.

## 1. Hypotheses and the precise all-mate conclusion

Work over an algebraically closed field k of characteristic zero, for the
fixed curve C0 and the accepted genus-one degree-five A4 normalization pair
`(S,c)` of the
[intrinsic classification](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md).
Retain the nonendpoint parameters `delta!=0,a,b,g,d`, and actual center
avoidance. The resulting projection

    nu:S -> X subset P3

is finite birational and is the normalization of its integral quintic
image. Its restriction `c->C0` is an isomorphism. These admissibility
statements are justified explicitly in the
[pole-filtration audit](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet-independent-audit.md).

The accepted
[quintic conductor audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
gives the entire upstairs conductor as the actual invertible ideal

    I_cond,S=O_S(-2H) subset O_S.

Its effective zero divisor `D_cond` is Cartier and linearly equivalent to
`2H`, not merely a numerical conductor cycle. In particular

    deg O_c(D_cond)=2H.c=8.

Let P,J be the corrected cubic numerators in the owner note and let
`Ph,Jh` be their degree-three homogeneous forms on c. Set

    Jbar=d-2g+2b-a.

Then any actual mate, in **any** positive degree, necessarily satisfies

    Res_h(Ph,Jh)*Jbar=0.                     (A)

Equivalently, the locus where the homogeneous pair is coprime and
`Jbar!=0` has no mate in any degree. The proof uses no socle-degree
inequality and does not depend on a bound for the mate exponent.

## 2. P,J detect every smooth-source rank drop along c

On `S\ell=A2`, the coordinates `(r,T)` are regular, c is `T=0`, and
the restriction of the four projection sections is

    (r^4,r^3(r-delta),r(r-delta)^3,(r-delta)^4).

For `r!=0`, use the target chart `x0!=0` and set

    y=x1/x0, z2=x2/x0, w=x3/x0,
    V=z2-y^3, U=w-(3/2)y*z2+(1/2)y^4.

The ideal `(V,U)` equals `(z2-y^3,w-y^4)`; hence its differentials
are an actual basis of the normal cotangent space to C0 at every finite
value of y. In particular there is no extra exceptional finite y at which
this first-symbol test loses a normal direction.

The T derivatives of the actual four sections on c are

    L0=a-2r^2-r,
    L1=b-2r^2-r+delta*r,
    L2=g-2r^2-r+3delta*r,
    L3=d-2r^2-r+4delta*r.

Direct quotient and chain differentiation gives

    V_T=P/r^7, U_T=J/(2r^7),
    P=r^3 L2-3r(r-delta)^2 L1+2(r-delta)^3 L0,
    J=2r^3 L3-3r^2(r-delta)L2+(r-delta)^3 L1.

Thus these expressions include movement of y; they are not derivatives
taken with the image curve parameter artificially held fixed. Expansion
gives exactly the corrected cubics in the owner note. This audit uses
the corrected J, not the earlier rejected expansion.

The image tangent along c is nonzero: for `r!=0`, its y derivative is
`delta/r^2`. If at least one of P,J is nonzero at the source point,
the image of the transverse tangent vector is not in that tangent line.
Consequently the differential from the smooth surface S has rank two,
equivalently the target cotangent map onto the source cotangent space
is surjective.

The point `r=0` is not discarded. There `x3=delta^4!=0`, so use the
reversed target coordinates. If their raw balanced coordinates are
`Vraw,Uraw`, put `Uop=Vraw/2,Vop=2Uraw`. On the overlap, writing
`z2=y^3+V,w=y^4+(3/2)yV+U` and retaining terms modulo `(U,V)^2`
gives

    Uop=y^(-7)U, Vop=y^(-7)V.

Their actual T derivatives therefore extend as

    (Uop)_T=J/[2(r-delta)^7],
    (Vop)_T=P/(r-delta)^7.

Both denominators are nonzero at r=0. The reverse image curve parameter
is `r/(r-delta)`, whose derivative is `-delta/(r-delta)^2`, also
nonzero there. Hence the same rank-two conclusion holds at r=0 whenever
P,J are not simultaneously zero. Explicitly the zero condition there
is `a=b=0`, since `P(0)=-2a delta^3` and `J(0)=-b delta^3`.

Every source point of c except its A4 point is one of these finite r
points. Homogeneous coprimality of Ph,Jh therefore implies immersion at
every smooth-source point of c, with no missing projection rank-one point
or missing opposite target frame.

## 3. The actual A4 cotangent matrix, including its full embedding dimension

At A4 use the accepted chart `Z0=1`, with

    alpha=Z1, beta=Z2, chi=Z3,
    dZ=alpha*beta-chi^2,
    eZ=beta^2-alpha*beta*chi+chi^3.

The local surface equation is

    beta*(chi-alpha^2)+alpha*chi^2=0.

It has no linear term, so the classes of alpha,beta,chi form a basis of
the full three-dimensional cotangent space at this singular point. Both
dZ and eZ lie in the square of its maximal ideal. Thus this calculation
does not replace the singular cotangent space by a smooth normal direction
or discard torsion in a curve conormal sheaf.

Here `U4=1-alpha`, `U3=-alpha`, `U2=chi`, `U1=dZ`,
`U0=eZ`, and `h=beta+chi`. The actual section X0 has value one, so
the target affine ratios are valid at this point. With `B=b-a`, the
linear parts of `Xi/X0-1`, for i=1,2,3, have coefficient matrix

    [ delta,  B,    B                ]
    [3delta,  g-a,  g-a+3delta^2     ]
    [4delta,  d-a,  d-a+6delta^2     ].

Subtracting three and four times the first row from the second and third
gives its determinant directly as

    -3delta^3*(d-2g+2b-a)=-3delta^3 Jbar.

Since `delta!=0` and the characteristic is zero, `Jbar!=0` makes the
target cotangent map surjective at A4 as well. It factors through the
cotangent space of X, because every equation of X pulls back to zero
on S. The singularity of S poses no obstruction to this implication.

## 4. Finite local cotangent lemma: where full inverse support is essential

**Lemma.** Let `A subset B` be a finite inclusion of Noetherian local
rings, with maximal ideals m,n, with equal residue fields. If the map
`m/m^2 -> n/n^2` is surjective, then `A=B`.

Indeed surjectivity gives

    n=mB+n^2.

The finite B-module `n/mB` therefore equals its product with n. Nakayama
over B implies `n=mB`. Equality of residue fields gives `B=A+n`, so

    B=A+mB.

The finite A-module `B/A` now equals `m(B/A)`. Nakayama over A gives
`B/A=0`. These are the ordinary finite-module forms of
[Nakayama's lemma, Stacks 00DV](https://stacks.math.columbia.edu/tag/00DV),
freshly inspected for this audit. No analytic inverse-function theorem,
formal power-series approximation or conductor flatness is used.

For application at a closed point `x in C0`, the finite algebra
`B=(nu_*O_S)_x` is initially allowed to be semilocal. A hypothetical
mate forces the **entire reduced inverse support**

    (nu^(-1)(C0))_red=c.

Because `c->C0` is an isomorphism, there is consequently exactly one
preimage point over x, including no extra isolated point. Thus B has one
maximal ideal and is the local ring of S at that point. Its residue field
and that of `A=O_X,x` are both k. Finiteness over A is retained.

This single-preimage step is indispensable. Localizing one branch of a
multi-preimage fiber and applying the lemma without proving finiteness
would not justify a normalization isomorphism. The mate's full support
supplies precisely the missing hypothesis here.

Under homogeneous coprimality and `Jbar!=0`, Sections 2 and 3 give the
required cotangent surjectivity at every such source point. The lemma
therefore makes nu a local isomorphism at every closed point of C0.
In particular the full actual conductor ideal is the unit ideal at
every point of c.

## 5. The conductor contradiction uses an actual restricted section

The actual effective Cartier conductor `D_cond~2H` would now have support
disjoint from c. Its canonical section restricts to a nowhere-vanishing
section of `O_c(2H)`. This would trivialize that line bundle, whereas

    deg O_c(2H)=2*deg H|c=8.

This is impossible on the complete smooth curve c. It does not require
c itself to be Cartier in S, reduced conductor branches, a smooth
downstairs conductor, or a rank-two flat conductor cover. It uses the
accepted entire invertible conductor ideal, not a replacement cycle.

The contradiction proves (A) in every possible mate degree. It is not
a first-normal upper bound on a later contact multiplicity: first
derivatives here prove cotangent surjectivity, and the finite local
lemma plus full support converts that into an exact ring equality.

## 6. Properness, retained exceptional loci and evidence

The necessary locus is proper. At

    delta=1, a=1, b=g=d=0

the corrected cubics homogenize to

    Ph=2(R^3-4R^2S+4RS^2-S^3), Jh=2R^2S,

and `Jbar=-1`. Their homogeneous roots have no common point. Hence
the product in (A) is a nonzero polynomial. This specific point need
not be asserted admissible: center avoidance is a nonempty open set,
so the complementary nonempty open intersects it in the irreducible
nonendpoint parameter family. The accepted center point lies outside
S, and the bad line extensions are the image of the two-dimensional
S in the four-dimensional extension space, which proves that assertion.

The homogeneous common-root-at-infinity locus already lies in
`Jbar=0`: the two leading coefficients give
`g=3b-2a,d=4b-3a`, hence Jbar vanishes. Thus one may equivalently
retain the A4 cotangent hypersurface together with the finite common-root
incidence. The proposed product formulation remains correct and keeps
all homogeneous frames explicit.

The remaining resultant and A4 cotangent loci are **OPEN** in this audit.
No assertion that they admit a mate is made. The earlier entire-line
ramification conditions satisfy `R3-2R2=Jbar`; their separate all-power
exclusion addresses a subfamily of this retained A4 hypersurface.

I inspected the corrected supporting source, its captured seven-condition
PASS stream and the separate corrected twelve-check conormal output. Those
records support the cubic identities and opposite-frame transition;
their successful execution alone does not prove the new geometric theorem.
The independent new evidence is the explicit finite-point rank argument,
A4 matrix, two-step local lemma and actual conductor-section contradiction
written here. No additional CAS execution was necessary or claimed.


---

## 6. jbar zero coprime conductor phase bound

# The Jbar-zero coprime quintic stratum: actual conductor phase bound

Date: 2026-10-12. Author: `oct12_conductor_phase_geometry`.

Status: **DIRECT PROOF OF A PROPOSED STRENGTHENING; INDEPENDENT AUDIT
PENDING**. The statement is confined to admissible nonendpoint projections
in the accepted genus-one quintic A4 normalization lane for the fixed
characteristic-zero quartic `C0`. It does not close the common-root locus,
all quintic carriers, higher carriers, or the unrestricted STCI question.
No existing canonical or sealed file was edited.

## 1. Proposed theorem and geometric inputs

Use the actual sections and conormal cubics P,J of the
[conormal reduction](2026-10-12-session-nonendpoint-conormal-cubic-reduction.md),
the [intrinsic pair](2026-10-11-session-dp5-a4-intrinsic-pair-classification.md),
the [local A4 chart](2026-10-11-session-dp5-a4-local-chart-independent-audit.md),
and the [entire conductor](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md).
The normalization S is anticanonically embedded in P5, H has square five,
the unique degree-one prime is ell, and c maps isomorphically to C0.
The actual upstairs conductor divisor Dc lies in |2H|, hence has H-degree
ten. Its downstairs scheme Gamma is Cohen--Macaulay of degree five and
arithmetic genus two, and the quotient module is omega_Gamma(-H), pure
of dimension one. The actual section Q of 4H has divisor 5c.

Write

    Jbar=d-2g+2b-a, E=g-3b+2a, delta!=0.

**Claim.** Every admissible nonendpoint projection with Jbar=0 and
coprime homogeneous conormal cubics Ph,Jh has no mate of any positive
degree. Combined with the previously audited Jbar!=0 argument, this
would sharpen the necessary mate locus to

    Res_h(Ph,Jh)=0.

The proof below uses the actual finite normalization and conductor rings.
The degree-ten/degree-five comparison is not used as a rank-two assertion.

Suppose a mate exists. Its pullback is a nonzero scalar times Q^k for some
positive integer k. In particular, the full inverse image of C0 has
support exactly c. A conormal-coprime projection is a local isomorphism
at every finite point of c: the source is smooth there, the map is
immersive, there is only one source point in the fiber, and the finite
Nakayama argument in the conormal reduction applies. Thus Dc misses
every finite point of c.

Both leading cubic coefficients on Jbar=0 equal E. If E=0, both degree-
three homogenizations vanish at infinity, contradicting coprimality.
If E=-3delta^2, Jbar=0 also gives

    g+3delta^2+2a-3b=0,
    d+6delta^2+3a-4b=0.

This is precisely the already excluded entire-line ramification subfamily
in the [pole/line note](OCT11_12_QUINTIC_NONENDPOINT_AND_FILTRATIONS.md#source-2026-10-12-session-nonendpoint-pole-filtration-and-line-jetmd).
We may consequently assume E(E+3delta^2)!=0.

## 2. The actual A4 normalization fiber has length two

At the A4 point p use the actual chart with coordinates alpha,beta,chi:

    B=k[alpha,beta,chi]/(beta(alpha^2-chi)-alpha chi^2),
    h=beta+chi,
    dZ=alpha beta-chi^2,
    eZ=beta^2-alpha beta chi+chi^3.

All four projection sections have value one at p, so X0 is a unit. The
ideal pulled back from the target maximal ideal is generated by Xi-X0,
i=1,2,3; dividing by X0 changes no ideal. Elementary invertible row
operations replace them, on Jbar=0, by

    f1=delta alpha+(b-a)h,
    f2=E h+3delta^2 chi-delta^3 dZ,
    f3=delta^4 eZ-2delta^3 dZ.

These are identities of actual sections in the Z0 frame, not only first
symbols. The exact last combination is X3-2X2+2X1-X0.

In the completed source local ring, f1,f2 eliminate alpha,chi formally
in terms of h, since their linear coefficient determinant is 3delta^3.
To first order,

    alpha=-(b-a)h/delta,
    chi=-E h/(3delta^2),
    beta=(1+E/(3delta^2))h.

Substitution in the source relation has leading term

    E(E+3delta^2) h^2/(9delta^4).

Its coefficient is a unit in k under our hypothesis. Thus quotienting
by the source relation gives k[[h]]/(h^2). The third target generator
has no linear term, so it imposes no further relation on that quotient.
The scheme-theoretic fiber therefore has length exactly two, including
its nilpotent direction. Completion preserves this finite length.

Let y=nu(p). Full inverse support gives precisely one point over y,
namely p. Hence the finite algebra (nu_*O_S)_y is local and agrees with
the local normalization B_p. Its quotient by m_y is the preceding
length-two fiber. Nakayama over O_X,y makes nu_*O_S generated by two
elements in a neighborhood U of y. In particular, for every generic
point eta of a curve through y,

    dim_{k(eta)}((nu_*O_S)_eta / m_eta (nu_*O_S)_eta) <= 2.       (1)

This is an actual local fiber/generator bound, not a global flatness or
average-degree assertion.

Every prime component D_i of Dc passes through p. Indeed D_i is not c,
and Q|D_i is a nonzero section of the line bundle 4H|D_i, of positive
degree 4H.D_i. It has a zero, and all its zeros lie on c. The preceding
local-isomorphism result excludes finite c, leaving p. Its image E_i
therefore passes through y, and its generic point lies in U. Bound (1)
applies to every generic conductor point.

Consequently the sum of the residue-field degrees of the distinct
normalization branches at any such point is at most two. The lengths
of the full Artinian conductor algebras need not be two; higher conductor
exponents are retained. Only their *reduced* field degrees are bounded.

## 3. Every conductor prime of degree at most five would have degree four

On S minus ell use A2 with r,T and t=T-r^2, v=t^2-r^3. The exhaustive
pole filtration in the [low-pole proof](2026-10-11-session-a4-low-pole-spaces.md)
has basis r^i t^j v^k, j=0 or 1, weight 2i+3j+5k. Leading coefficients
are independent at every weight, so cancellation does not hide a higher
pole. In particular the complete space of pole order at most five is

    span{1,r,t,r^2,rt,v}.

If D_i!=ell is a prime curve of H-degree n, its intersection with A2 is
an irreducible principal curve f=0. Normality and the complete A2 chart
give div(f)=D_i-n ell: intersect with H to identify the pole order n,
using H.ell=1. This remains true if the projective prime or its A4 point
is singular; no smoothness or reduced local branch assumption is used.

Dc misses finite c. Thus f(r,0) has no zero over the algebraically closed
ground field and is a nonzero constant. When n<=5 write

    f=A v+B rt+C r^2+D t+F r+G.

Restriction to c:T=0 gives

    f(r,0)=A r^4+(-A-B)r^3+(C-D)r^2+F r+G.

Constancy forces A=B=F=0 and C=D, so f=D T+G. A nonconstant prime
requires D!=0, and avoiding finite c requires G!=0. Its exact pole
order is four. Therefore there are no degree-two, degree-three or
degree-five conductor primes avoiding finite c. The only degree<=5
possibility other than ell is degree four, with equation T=constant!=0.
Multiplicity of a prime in Dc does not change this prime classification.

## 4. The distinguished line is not a conductor component

The actual restriction of the four projection sections to ell is

    (u-1,u-1+delta,u-1+3delta,u-1+4delta).

Thus ell maps isomorphically onto a line L in X. On Jbar=0, the two
entire-line differential rank-drop equations reduce to E=-3delta^2.
We excluded that value, so the projection is immersive at generic ell.

Suppose ell were a conductor component. If it were the only source
branch over generic L, the source fiber would have one point with the
same residue field and a surjective cotangent map; the finite local
Nakayama argument would give a local isomorphism, contradicting the
conductor. There must therefore be another source branch over generic L.
Bound (1), together with ell's degree-one residue field, allows at most
one other branch and forces its field degree to be one. Let D' be its
closure on S. Projection-formula degree gives

    H.D'=[k(D'):k(L)]*deg(L)=1.

The unique degree-one prime on S is ell itself, so D' cannot be distinct.
This contradiction excludes ell. This argument explicitly uses both
the image line's degree and the branch field degree; source curve degree
is not being equated silently with a map degree.

The entire conductor divisor now has degree ten and has no ell component.
Every prime in it has degree at least four, and no prime has degree five.

## 5. No split reduced generic conductor is possible

At a generic conductor point eta put K=k(eta), R=O_X,eta/I_eta and
T=(nu_*O_S)_eta/I_eta. These are the actual possibly nonreduced Artinian
conductor rings. By (1), if Tred is split, it has exactly two field
factors, both equal to K. Their closures D1,D2 are distinct prime curves
mapping birationally onto the same reduced image curve E_eta. Hence

    H.D1=H.D2=deg(E_eta)=e.

Because they each occur with positive integer multiplicity in the
degree-ten divisor Dc, 2e<=10. The prime classification forces e=4.
Their minimal total contribution is eight. A larger multiplicity already
exceeds ten, while minimal multiplicities leave degree two to be supplied
by other conductor primes. There is neither ell nor any other prime of
degree two or less. This is impossible. Thus Tred is not split at any
generic conductor point.

This uses the actual total Cartier-divisor degree and integer prime
multiplicities only after the independent fiber bound. It does not
discard nonreduced conductor schemes. Each actual Tred is consequently
a single field L/K of degree one or two.

## 6. Arbitrary mate power forces a degree-eight mate

Since c is not a conductor component, Q, in any downstairs local frame
of O_X(4H), is a unit at every generic conductor point. The
[full-conductor power audit](2026-10-11-session-power-descent-algebra-audit.md)
proves that for a single residue field L/K the least positive reduced
exponent d, if one exists, equals [K(Qred):K] and is at most [L:K].
Here d is therefore one or two. If a full Q^k lies in R, the unit-jet
lemma says that Q^d itself lies in the full R, retaining every nilpotent
layer. It follows in either case that Q^2 lies in the full R.

This includes successful odd k: in a degree-two field the reduced period
two cannot divide odd k, so a successful odd power must have d=1; its
full unit-jet membership then gives Q and hence Q^2. No parity shortcut
or residue-only descent test is being used.

The normalization quotient omega_Gamma(-H) is pure. Full generic
membership at every conductor component therefore makes Q^2 descend
globally as a section of O_X(8H). The hypersurface section sequence lifts
it to an ambient degree-eight polynomial. Its pullback divisor is 10c,
so it is a genuine degree-eight mate under the supposed full support.

But coprime homogeneous cubics give conormal direction degree e=3. The
accepted complete-intersection socle inequality in the conormal reduction
gives, for k=2,

    deg D_(5k-1)=4k-10=-2,

contradicting effectivity. This excludes every supposed positive mate
power in the stated stratum. The argument closes Jbar=0 with coprime
cubics, including the separately excluded ramified-line value.

## 7. Evidence and continuation boundary

The geometric argument above is direct; small symbolic checks support
the actual target ideal, quadratic coefficient, low-pole restriction,
and parameter exceptions. Execution and source bindings are to be added
after the new verifier runs. Existing records and seals are untouched.
An independent proof audit has been assigned and is pending.

If accepted, the next mate locus is the complete homogeneous common-root
incidence Res_h(Ph,Jh)=0, with finite roots, target infinity, A4 infinity,
repeated roots and higher contact retained. Neither this proof nor its
first-normal consequence bounds the higher embedded defect at those
remaining points. The full conductor algebras remain necessary there.


---

## 7. jbar zero conductor phase independent audit

# Independent audit: Jbar-zero coprime conductor phase bound

Date: 2026-10-12. Auditor:
`oct11_endpoint_a_nonzero_support/a_nonzero_three_common_roots`.

Status: **PASS, independent mathematical audit of the all-mate exclusion
under the stated geometric hypotheses.** The argument uses an actual
normalization fiber, finite module generation, the entire conductor divisor,
full Artinian membership and purity. It does not infer rank from average
degrees or bound the phases of an algebra that remains split.

The audited owner is
[Jbar-zero coprime conductor phase bound](2026-10-12-session-jbar-zero-coprime-conductor-phase-bound.md),
as read with SHA-256
`5749a82f42bce56842c826fc18b8972f85bfc6f4e21276754f7c80a066e3f23a`.
This audit binds its mathematical sections 1--6. At that version its final
section promises forthcoming verifier bindings; their later addition is
not needed as a premise of this proof. Owner, old notes, canonical records,
sealed files and Git were left unchanged by the auditor.

## 1. Precise scope and retained exceptional cases

Work over an algebraically closed field of characteristic zero in the
accepted nonendpoint genus-one quintic A4 pair. Retain arbitrary
`delta != 0,a,b,g,d`, actual center avoidance and finite birational
normalization `nu:S -> X`. The lifted c maps isomorphically to fixed C0.
Write

\[
\bar J=d-2g+2b-a=0,\qquad E=g-3b+2a.
\]

Assume the corrected degree-three homogeneous conormal forms Ph,Jh are
coprime, including their roots at infinity. Every supposed mate pulls
back to a scalar Q^k, where Q is an actual section of 4H with divisor
5c, and forces the full reduced inverse support to be c.

The two cubic leading coefficients both equal E on this hypersurface.
Thus E=0 is incompatible with homogeneous coprimality. The case
E=-3delta^2 is exactly the previously audited entire-line ramification
locus, since its second equation equals twice the first on Jbar=0.
Its separate characteristic-zero derivation obstruction excludes every
positive power. The rest of this proof assumes
`E(E+3delta^2) != 0`. It does not claim the following length-two fiber
calculation on the removed ramified-line locus.

Under a hypothetical mate, coprimality and the actual opposite target
frame give cotangent surjectivity at every finite point of c, including
r=0. Full support leaves one normalization point over each such image.
The finite local Nakayama lemma therefore makes nu a local isomorphism
there. The conductor divisor misses all finite points of c.

## 2. The actual A4 fiber and finite generation

Use the accepted A4 source chart

\[
B=k[\alpha,\beta,\chi]/
  (\beta(\alpha^2-\chi)-\alpha\chi^2),\quad
h=\beta+\chi,\quad d_Z=\alpha\beta-\chi^2,\quad
e_Z=\beta^2-\alpha\beta\chi+\chi^3.
\]

The actual target maximal ideal pulls back, after invertible row
operations and the unit X0, to

\[
f_1=\delta\alpha+(b-a)h,\quad
f_2=Eh+3\delta^2\chi-\delta^3d_Z,\quad
f_3=\delta^4e_Z-2\delta^3d_Z.
\]

These are exact section identities. The first two eliminate alpha,chi
formally, with nonzero linear determinant `3 delta^3`. Their leading
solution is

\[
\alpha=-(b-a)h/\delta+O(h^2),\quad
\chi=-Eh/(3\delta^2)+O(h^2),\quad
\beta=(1+E/(3\delta^2))h+O(h^2).
\]

The source equation then has nonzero leading coefficient
`E(E+3delta^2)/(9delta^4)` on h^2. It therefore generates `(h^2)`
in the one-variable completed ring. The third target generator has
order at least two and cannot remove its surviving first-order h.
The completed fiber is exactly `k[[h]]/(h^2)`, of length two.
Completion preserves this finite length.

Full inverse support implies that p is the only point above y=nu(p).
Consequently the normalization algebra at y is local, finite over
O_X,y, and is the actual source local ring used in that calculation.
Its fiber dimension two makes it a two-generated O_X,y-module by
Nakayama. The two generators extend to a surjection from O_U^2 on
some open neighborhood U of y. This is local module generation,
not flatness or a claim that all conductor algebras have length two.

Each conductor prime D_i meets c. It is not c, since the conductor
misses finite c. The nonzero restricted section Q|D_i has positive
line-bundle degree `4H.D_i`, so it has a zero on this complete integral
curve. Every such zero lies on c, and finite c was excluded. Hence
D_i contains p; its image curve contains y, and its generic point
belongs to U. The two-generator bound therefore applies at every
generic conductor point.

At such a point eta, the finite normalization fiber is an Artinian
k(eta)-algebra whose residue-field degrees sum to at most its dimension,
and that dimension is at most two. This bounds the sum of the reduced
field degrees. It does **not** bound the length of B/I: arbitrary
higher generic conductor exponents remain possible.

## 3. Complete low-degree prime classification

The normal complement S minus ell is A2 with r,t, where
`T=t+r^2` and `v=t^2-r^3`. The complete pole-order-five space is
`span(1,r,t,r^2,rt,v)`, by the already proved valuation filtration.
For a prime D_i other than ell, its affine generator f is irreducible,
and its only possible additional divisor is the boundary ell.
Thus `div(f)=D_i-n ell`, where intersection with H identifies
`n=H.D_i` as its exact pole order.

Avoidance of finite c says that f(r,-r^2) is a nonzero constant.
Writing

\[
f=A_0v+A_1rt+A_2r^2+A_3t+A_4r+A_5
\]

gives

\[
f|_c=A_0r^4+(-A_0-A_1)r^3+(A_2-A_3)r^2+A_4r+A_5.
\]

Constancy forces `A0=A1=A4=0,A2=A3`. A nonconstant prime therefore
has equation `A3 T+A5`, with both coefficients nonzero, and exact
degree four. This proves that among degrees at most five the only
allowed prime other than ell has degree four. It includes singular
projective primes and repeated occurrences of a prime in the conductor.

## 4. Excluding ell over the nonclosed generic residue field

The line ell maps isomorphically to a target line L: its four actual
sections are `(u-1,u-1+delta,u-1+3delta,u-1+4delta)`, which span
the full degree-one system. Its generic residue field is
`K=k(L)=k(u)`, not the algebraically closed constant field.

The required generic cotangent argument can be proved by an actual
target equation, avoiding any residue-field shortcut. In the target
X0 chart let

\[
\ell_2=X_2/X_0-3X_1/X_0+2.
\]

It vanishes on L. Its actual numerator is
`3delta^2 U2-delta^3 U1+E h`. In the fourth source chart,

\[
U_2=x(1+xu),\quad U_1=x^3(1+xu)^2,\quad
h=x(1+xu)+x^2(1+xu)^2,\quad X_0|_{x=0}=u-1.
\]

Consequently

\[
\ell_2=x\frac{E+3\delta^2}{u-1}+O(x^2).
\]

Its ell valuation is exactly one on the retained locus. If ell is
the sole normalization branch over generic L, the finite local
normalization ring B_eta is a DVR with residue K, equal to the
residue field of A_eta. The element ell_2 belongs to m_A and generates
the maximal ideal of B_eta up to a unit. Hence `m_A B=n_B`.
Residue equality gives `B=A+n_B=A+m_A B`; Nakayama on the finite
A-module B/A gives A=B. Thus a sole branch cannot be a conductor
branch. This proof works over K and requires neither an algebraically
closed residue field nor an inverse-function theorem.

If another branch exists, the actual two-generator fiber bound leaves
at most one additional branch and forces its residue-field degree to
be one. Its distinct source prime D' has
`H.D'=degree(map)*degree(L)=1`, contradicting uniqueness of ell.
All branches over a generic conductor point occur in the conductor:
I is proper in the target local ring, so its extension is proper in
each normalization maximal ideal. Thus no uncounted additional
branch can escape this argument. Ell is excluded.

## 5. Split reduced algebras are excluded by degree accounting

Now every conductor prime has degree at least four, and none has
degree five. If a generic full conductor algebra T has split reduction,
the field-degree bound makes it exactly `K x K`. Its two distinct
source primes D1,D2 map birationally onto the same image curve, so
their H-degrees equal its degree e. They occur with positive integer
coefficients in the actual Cartier divisor Dc of total degree ten.
Hence `2e<=10`, and the preceding prime classification forces e=4.

Their minimum contribution is eight; increasing either integer
coefficient makes it at least twelve. Minimum coefficients leave
degree two, which cannot be supplied by any remaining prime now that
ell and all primes of degree two or three have been excluded.
Therefore no split reduced generic conductor occurs.

This accounting does not replace nonreduced conductor schemes by
their reductions: the integer coefficients explicitly retain them.
The possible full generic Artinian algebra has one residue field
L/K of degree one or two. Its nilpotent length is unrestricted by
this field-degree statement.

## 6. Full arbitrary-power membership forces Q squared membership

Trivialize the actual downstairs line bundle O_X(4) at each generic
conductor point. The residue q of Q in T=B/I is a unit, because its
upstairs divisor 5c has no conductor prime. The supposed mate gives
full membership `q^k in R=A/I`, not only a tensor equalizer or reduced
membership.

Here R is Artinian local, Rred=K, and Tred=L is one field of degree
at most two. If alpha=qred belongs to K, its minimum reduced period
is one. Otherwise L/K has degree two and its nontrivial automorphism
sends alpha to zeta alpha, since alpha^k lies in K. All roots of unity
are already in K. Applying the automorphism twice gives zeta^2=1;
since alpha is not in K, zeta=-1. Thus alpha^2 belongs to K, the
minimum period is two, and k must be even. This is why odd successful
k cause no omitted parity case: they require period one.

The full nilpotent step is indispensable. Let d be this period, one
or two, choose a unit r in R lifting alpha^d, and put
`q^d/r=1+n` with n nilpotent in T. A successful k=dm implies
`(1+n)^m in R`. In characteristic zero the finite nilpotent logarithm
gives `m log(1+n) in R`; dividing by m and applying the finite
exponential gives `1+n in R`. Hence `q^d in R`, in every nilpotent
layer. Either value of d implies `q^2 in R`.

For comparison, the abstract split algebra `K x K` permits residues
`(1,zeta)` with arbitrary root-of-unity order; a two-branch bound alone
would not imply this conclusion. That algebra was excluded by the
actual geometry in section 5 before this power argument. Likewise,
two generators do not bound nilpotent conductor length: for
`A=K[[t^2,t^(2m+1)]]` inside `B=K[[t]]`, B has two generators over
A while the conductor quotient B/(t^(2m)) has length 2m. The proof
retains these potential nilpotent lengths rather than replacing T
by a quadratic reduced cover.

## 7. Purity, the actual ambient mate and the socle contradiction

The accepted entire quotient is
`nu_*O_S/O_X=omega_Gamma(-H)`, maximal Cohen--Macaulay on the
Cohen--Macaulay conductor curve, and hence pure of dimension one.
The obstruction class of Q^2 in this quotient twisted by O_X(8)
vanishes at every generic conductor point by full membership above.
Its generated coherent subsheaf would then have finite support;
purity makes it zero. Thus Q^2 descends globally to O_X(8), including
all special conductor points. Residue-only membership would not
justify this invocation of purity.

The quintic hypersurface sequence
`0 -> O_P3(3) -> O_P3(8) -> O_X(8) -> 0` and H1(O_P3(3))=0 lift
that section to an ambient degree-eight form G. Its pulled-back
zero divisor is 10c. Finite surjectivity of nu makes the zero support
of G on X exactly C0, so G is an actual degree-eight mate.

This mate gives a generically curvilinear CI(5,8), of multiplicity
ten. Coprimality fixes its first saturated quotient as
`L=O_P1(3-7)=O_P1(-4)`. Complete-intersection duality fixes the
top socle line as `E9=O_P1(-38)`. Generic curvilinear multiplication
gives a generically nonzero global map `L^9 -> E9`, but its Hom
space is H0(O_P1(-2))=0. Equivalently the effective top defect would
have degree -2. This is the accepted socle bound, now applied to an
actual forced mate rather than an assumed degree reduction.

The contradiction excludes every supposed mate power in this stratum.
Combined with the independently audited Jbar-nonzero obstruction, a
mate anywhere in this nonendpoint genus-one lane must satisfy the
complete homogeneous common-root condition `Res_h(Ph,Jh)=0`.
The common-root, higher-jet and full-conductor incidence remains open;
other quintic normalization genera and higher carriers are outside scope.

## 8. Exact supporting source and preserved failure

The independent
[supporting source](../computations/verify_session_jbar_zero_phase_audit_2026_10_12.m2)
has SHA-256
`946d697ec8dd208e0a02e7b150f9aa2500780d3539ad2a5adde1d1062ebcf70f`.
It passes twelve exact identities: three actual target generators,
cleared linear elimination, the cleared fiber quadratic coefficient,
absence of a third-generator linear term, ell section restriction,
its actual image-line equation and valuation-one numerator, the
ramified-line parameter exception, complete low-pole restriction,
and coincidence of the cubic leading coefficients.

The [captured execution record](../validation/2026-10-12-jbar-zero-phase-independent-audit/execution-record.json)
routes to two source snapshots with separate raw streams. Attempt 01
passes the first six identities and then fails because Macaulay2 has
no `substitute(List,List)` method. Attempt 02 changes only that list
operation to an elementwise apply and passes all twelve identities,
exit zero with empty stderr. The failed source and streams remain saved.
These are two executions of one source lineage; the snapshots are copies,
not additional independent implementations.

The twelve identities are supporting evidence for the written proof.
They do not computationally replace the finite local argument over K,
module propagation, all-prime classification, split accounting, full
nilpotent logarithm, purity or socle duality.
