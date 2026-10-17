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
