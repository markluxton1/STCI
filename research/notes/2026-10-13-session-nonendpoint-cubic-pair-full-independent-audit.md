# Independent full audit: the nonendpoint residual cubic-pair lane has no mate

Date: 2026-10-13. Auditor: `oct12_type1_two_family_audit`.

Status: **PASS, WITH THE EXPLICIT SCOPE QUALIFICATION IN SECTION 1.** The
entire residual partition 3+3 in the accepted nonendpoint genus-one quintic
A4 normalization family is excluded in every mate degree, including a
doubled residual cubic. Full inverse support itself is excluded by the
contact-classification argument only on Jbar!=0. This does not close the
integral residual lane, other quintic normalizations, higher-degree carriers,
unrestricted C0, or the universal STCI problem.

The frozen [owner proof](2026-10-12-session-nonendpoint-cubic-pair-contact-reduction.md)
was read at SHA-256
`7276aa227795695682684f4e1468a45d07c4513eb5a8465190966274d4464f2a`.
The [cubic-contact companion](2026-10-12-session-nonendpoint-cubic-contact-symbolics.md)
has SHA `0b85a793349a0a35c6b9f1b3ea0a677d90d2076d14f2f28257ab5b86c1b1fb4c`;
the [sparse-heptic companion](2026-10-12-session-sparse-heptic-cubic-pair-classification.md)
has SHA `58ceb45611e48755169b78fc9a3b8d666853c705f1d2281a8f6a80a489a96bc8`.
No owner, companion, canonical, old seal-bound file or Git state was edited.

## 1. Correct theorem, actual setting and retained exceptions

Work over an algebraically closed field of characteristic zero, for the fixed
C0 and the accepted degree-five A4 normalization pair. Retain delta!=0 and
every actual center avoiding the surface. The induced projection is finite
birational, and c maps isomorphically to C0. A hypothetical mate implies the
complete inverse-support condition SUP, including no isolated extra point.

Use B=b-a, G=g-3b+2a, Jbar=d-2g+2b-a, so A=a+d-b-g=G+Jbar. The 3+3
partition lies on A=-3delta^2. The upstream
[residual audit](2026-10-12-session-nonendpoint-residual-factor-and-genus-independent-audit.md),
SHA `db72f936486253cf91e82645de9c3b6b23562dac9da49eee6ee31f0cb94b5322`,
proves under SUP that every prime cubic is a smooth rational normal cubic
with equation t+m r+n=0, and maps isomorphically to a smooth Q-curve of class
(2,1). The pushforward cycle retains multiplicity; a doubled source cubic
is permitted. The line-cover and ruling-degree-drop alternatives are already
excluded in that upstream proof, rather than discarded by selecting a minor.

The frozen owner's section 7 has a stronger formulation than its proof:
it asserts failure of SUP on the entire lane. On Jbar=0, however,
A=-3delta^2 forces G=-3delta^2, the entire-line rank-one stratum. The accepted
[pole/line audit](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet-independent-audit.md)
excludes all mates there by the actual candidate-power obstruction; that
does not itself establish failure of SUP. I identified this distinction;
the owner withdrew the stronger assertion in the separate
[scope qualification](2026-10-13-session-cubic-pair-theorem-scope-qualification.md),
SHA `0dce1ea4cee349a6a4520285a56152c6243c1ffaf6cb4d7607e6c1c253c59d7b`.

The precise conclusions accepted here are:

* If Jbar!=0, no such projection satisfies SUP, including distinct or doubled
  residual cubics.
* If Jbar=0, no such carrier has a mate, by the separate all-power obstruction;
  failure of SUP is not claimed.
* Thus the entire residual 3+3 lane has no mate in any degree.

## 2. Actual contact at infinity and the complete heptic

On a source cubic put T=r^2-mr-n. Its four actual coordinate sections are
cubic polynomials with leading coefficient -1, so their homogeneous values
at r=infinity are all nonzero. The smooth source and target cubic are
isomorphic; epsilon=1/r is therefore an actual smooth curve parameter there.
For the actual Q-chart equation eta-zeta^3 of C0, where
eta=X2/X0 and zeta=X1/X0, direct expansion gives first coefficient Jbar.
My fresh checker independently verifies that the numerator X0^2 X2-X1^3,
after homogenizing each Xi to epsilon^3 Xi, has first coefficient -Jbar.
Its denominator has constant value (-1)^3, giving the same Jbar. Hence
the contact is exactly one when Jbar!=0. No first-normal estimate of a
later contact order is used.

The primitive Segre factorization of the degree-three curve map is

    (X0,X1,X2,X3)=(L0 Q0,L0 Q1,L1 Q0,L1 Q1),

with homogeneous L_i of degree one and Q_i of degree two, both pairs
basepoint-free. Each factor is nonzero at infinity since all Xi are nonzero
there. Normalize L_i to have affine leading coefficient one and Q_i to have
leading coefficient -1. Then L1-L0=kappa is constant. It is nonzero: if it
vanished, the first Segre projection would be constant, whereas a smooth
(2,1) curve has that projection of degree one. Thus every division by
kappa in the owner's formulas is justified on the full admissible class,
without assuming a generic center minor.

Comparing X2-X0 gives kappa=a-g+3delta m-3delta^2 and

    Q0=(X2-X0)/kappa
       =-r^2-[3delta n+delta^3+(g-a)m]r/kappa-(g-a)n/kappa.

The actual divisor's r^2 coefficient condition gives
kappa(B-delta m)=3delta^2(m-delta). Together with X3-X1-X2+X0 this gives
the exact Q1-Q0 formula in the owner. The r^2 coefficient of X0 determines
L0=r-(m^2+m+a-q), hence all four factor formulas follow from the primitive
factorization and actual coordinate comparison.

The complete contact form is the binary heptic

    K=L1 Q0^3-L0 Q1^3.

The exact ambient identities, independently checked afresh, are

    X0^2 X2-X1^3=L0^2 K,
    X2^3-X1 X3^2=L1^2 K.

Consequently the extra ambient ruling factors are removed, and no common
root is lost because L0,L1 are coprime. This includes target X0=0 and all
other Segre-chart endpoints. The affine leading term of degree seven
cancels; its degree-six coefficient is
-kappa-3(B-delta m)=-Jbar. Thus K has exactly one binary zero at infinity
and six finite contact lengths.

Both ambient cubic restrictions are divisible by the actual polynomial T:
before restriction their expressions are divisible by the affine ideal
generator T of c. Substituting T(r) preserves that exact divisibility even
when T has a repeated root. The two coprime L_i then imply T divides K
with full multiplicity. Under SUP every finite root of K is a root of T;
the binary root at infinity is already accounted for. This is the precise
interpretation of the owner's affine-support statement.

The intrinsic restricted curve ideal has finite length two and infinity
length one. At infinity h=T/v belongs to the actual ideal of c and has
expansion -epsilon+O(epsilon^2), since v=t^2-r^3 has pole three. Hence the
intrinsic total length is three, whereas C0.(2,1)=7. The contact classification
below uses the entire target intersection divisor to control the four
excess lengths, rather than a bound from tangent data.

## 3. Complete homogeneous classification, including all endpoints

A (2,1) target curve has equation P2(U,V)W0+Q2(U,V)W1. Restricting to
C0, where the Segre coordinates are (1:z^3) and (1:z), gives the binary
heptic with possible affine exponents 0,1,3,4,6,7. The two missing
coefficients are z^2,z^5. This restriction is injective because these six
monomials are distinct. Coprimality of the two binary quadratics is exactly
the irreducibility filter: a shared homogeneous root yields a ruling
component, while coprime quadratics give a smooth graph over their first
coordinate line. A four-by-four homogeneous Sylvester resultant includes
the common root at infinity and every leading-degree drop.

For each finite source T-root r=delta u, the target root is represented by
u z1+(1-u)z0. This is defined at u=0 (target infinity) and u=1 (target zero),
and never vanishes at z=1. Distinct roots have profiles (1,5),(2,4),(3,3),
up to exchanging labels; repeated T must have the separate profile (6).

I constructed the binary coefficients afresh as finite binomial sums, not
by replaying the owner's expanded-polynomial coefficient extraction.
The resulting exact sparse ideals, saturated only by root distinction and
the binary resultant, equal

    15: (u-11v+5, 21v^2-21v+5),
    24: (u-42v^3+63v^2-42v+10,
             63v^4-126v^3+111v^2-48v+8),
    33: (u+v-1, 7v^4-14v^3+12v^2-5v+1).

All three are zero-dimensional, reduced, and disjoint from both the
saturated bad locus and u v(u-1)(v-1)=0. Thus zero and infinity are retained
before the exact ruling-factor filter, rather than omitted by a denominator.
The ordered counts are 2,4,4. The last identifies exchanged root labels,
leaving two contact quadratics. For type 24, h=s-1 separates the four
solutions: v=1/2+h/(21h^2+1), and its denominator cannot vanish on
63h^4-30h^2-1=0. Hence the list has exactly eight source T quadratics.

The repeated-root sparse ideal is exactly (u(u-1)); both surviving endpoints
have zero binary resultant, and saturation by that resultant is the unit
ideal. No irreducible cubic has a repeated-root T in this contact setting.
This excludes repeated roots of T only; it does not remove a repeated
cubic component of the residual divisor.

The independently verified invariant equations are

    15: h^2=12/7, p=8/21+h/2;
    24: 63h^4-30h^2-1=0, p=5/12+h/2-h^2/4;
    33: h=0, 7p^2-5p+1=0,

with s=1+h and p=uv. These necessary equations retain all algebraic branches.

## 4. Actual source coefficient comparison and all six pair contradictions

I delegated a separate narrow algebra reconstruction and then read and
reconstructed its written argument, rather than treating the worker's
agreement as proof. The frozen
[coefficient subaudit](2026-10-13-session-nonendpoint-cubic-pair-coefficient-independent-subaudit.md)
has SHA `8dc9ca3c3623a42023ed8acee208dc1b8272b3942e91c68d4b43d6994d72c316`.
Its conditional geometric hypotheses are supplied by Sections 1–3 here.

Put S=s1+s2, Sprod=s1s2, P=p1+p2, Pprod=p1p2,
Cross=s1p2+s2p1, and x=B/delta^2. Matching the actual F with

    -3delta^2(t+delta s1r-delta^2p1)(t+delta s2r-delta^2p2)

first gives a=-3delta^2 Pprod and
G=3delta^2(S-1)-6x delta^2+3delta. After those substitutions define

    Q2=delta(Sprod+x^2-xS)-x+1,
    Q0=delta(x-Sprod+1/3-P+3Pprod)-1,
    Q1=delta(x+9Pprod-3Cross)-1.

The exact full residual difference is

    3delta^3 Q2 r^2+3delta^3(Q0+Q2)t+delta^4 Q1r.

The original coefficients are therefore zero only if Q2=Q0=Q1=0.
Since Q1-Q0=delta E, the necessary condition is

    E=Sprod-3Cross+P+6Pprod-1/3=0.

Only the known nonzero delta is divided out. No difference between factors,
roots or field branches is inverted. The complete extra coefficient equation
is retained in the companion/subaudit; it is unnecessary for an exclusion
because this one necessary condition already fails.

The six invariant type pairs reduce E respectively to

    15/15: 2/147-h1h2/2;
    15/24: (1-3h2^2-21h1h2)/42;
    15/33: (2/7)(p2-1/3);
    24/24: [(1-3h1^2)(1-3h2^2)-12h1h2]/24;
    24/33: (3h1^2-1)(1-3p2)/6;
    33/33: (2/3)(1-3p1)(1-3p2).

None can vanish under its field equations. The mixed 15/24 case forces
e=h2^2=1/663, contradicting 63e^2-30e-1=0. In 24/24, distinct e-roots
give sum 10/21 and product -1/63, contradicting the squared equality;
equal e-roots give e=1/12 or e=-1/3, both excluded. These arguments retain
both signs and all coincident values. The other four pair contradictions
are the direct nonzero rational values in the subaudit. The fresh algebra
checker additionally verifies six unit ideals and explicit diagonal tests
for types 15,24,33. Thus a doubled residual cubic is included, and common
contact points between distinct components are never removed by saturation.

This contradicts the actual necessary coefficient equation for every
possible pair when Jbar!=0. Combining with the independent entire-line
all-power obstruction when Jbar=0 proves the stated entire-lane no-mate
theorem, with the scope qualification from Section 1.

## 5. Independent executions, bindings and failure history

The fresh [binary/contact checker](../validation/2026-10-13-cubic-pair-full-independent-audit/verify_binary_contact.m2)
has SHA `11fa7ca6e9c22936226d82da22daf70ea55da7f381e7f4ea12a9a1e41360adbf`.
Its [one captured execution](../validation/2026-10-13-cubic-pair-full-independent-audit/attempt-01/execution-record.json)
passed 30 distinct conditions, exited zero and had empty stderr. Stdout
SHA is `0f03e86091a50cbcd6e1fd260b65590a7f4f94c326b9a46834e1506c6d7828ca`.
There was no failed development execution in this new binary lineage.

The separate fresh
[coefficient checker](../computations/verify_session_cubic_pair_coefficient_subaudit_2026_10_13.m2),
SHA `a067b9847fc4150a302aa229e6a626ecf78480a66cebfd776da525e347477e7a`,
passed 38 distinct conditions in its final capture. Its three development
versions retain one protected-name setup failure and two successful versions
with 29 and 38 conditions. The independent sources are two checker lineages,
not four independent proofs. The coefficient subaudit includes the direct
written six-pair contradictions; the original sparse companion additionally
preserves literal original-generator Bezout certificates and their products.

I freshly verified all 56 files in the owner's assembly manifest against
their recorded digests, and all 18 bindings in the coefficient subaudit
manifest. The [input inspection](../validation/2026-10-13-cubic-pair-full-independent-audit/input-binding-inspection.json)
records the owner comparison separately from mathematical acceptance.
The owner's two checker lineages preserve twelve executions, six failed and
six successful, including all wrong coefficient interfaces and protected
names. Successful scratch replays are not independent lineages. No historical
mathematical verifier was rerun for this audit.

The stronger frozen SUP theorem is corrected by the separately bound owner
qualification; it is not silently interpreted as a proven result. The entire
all-mate theorem needs no further algebraic or geometric repair within its
stated scope.
