# Historical mathematical investigations

Complete source text preserved below, including explicit hypotheses, calculations, counterexamples and unresolved issues. Compilation is not independent correctness audit or theorem promotion.

---

## Source: 2026-10-11-session-multiplicity-ten-filtration-audit.md

# Quasiprimitive multiplicity-ten filtration: necessary numerical reduction

Date: 2026-10-11.

Status: **DIRECT PROOF AUDIT AND NECESSARY NUMERICAL REDUCTION**. This note
does not exclude degree `(5,8)`, does not classify embedded multiplicity-ten
structures, and does not establish that `C0` is not an STCI.

## 1. Scope and inputs

Work over an algebraically closed field of characteristic zero. Let

`C=C0=[s^4:s^3 t:s t^3:t^4]`,

and suppose `X=V(F5,G8)` has reduced support exactly `C`. The equations have
no common surface factor, so `X` is a projective local complete intersection
of degree 40 and generic multiplicity ten. The argument below requires its
generic transverse algebra to be curvilinear. For a hypothetical defining
pair that requirement follows from the repository's P-011: the quintic must
have generic normal order one. This note audits the filtration argument,
not P-011.

The conormal input is `N_C^*=O_P1(-7)^2`. No assertion is made that `X` is
primitive at every point, that the first-normal quotient of the equations
has regular ratio, or that the ordinary nilradical-power quotients are line
bundles.

Relevant existing records are P-016 and P-042 in
[RESEARCH_RECORD](../RESEARCH_RECORD.md),
[the local multiplicity-six pairing audit](2026-10-05-mf6-pairing-audit.md),
and [the uniform saturated-filtration audit](OCT6_SESSION_FRONTIERS_AND_VALIDATION.md#2026-10-06-session-uniform-audit).
The primary source was freshly opened for this audit:
[Manolache, *Duality for Gorenstein multiple structures on smooth algebraic
varieties*, 2023](https://imar.ro/journals/Revue_Mathematique/pdfs/2023/1-2/10.pdf),
printed pp.142–145. The theorem concerns canonical Gorenstein multiplication
duality; its Remark 2 identifies the filtrations for quasiprimitive
structures. The proof below is a direct local algebra proof for this setting.
The Boratyński original was not freshly fetched in this audit.

## 2. Saturated filtration and duality at every support point

Complete at a support point, choose a tangent parameter `t`, and put
`R=k[[t]]`, `K=Frac(R)`. The completed ring `B` of `X` is finite over `R`:
its two normal coordinates are nilpotent. Cohen–Macaulayness makes `t` a
nonzerodivisor, hence `B` is finite free of rank ten. The special fibre is an
Artin complete intersection and is Gorenstein. Lifting a Frobenius functional
from that fibre produces a functional `lambda:B->R` for which
`B -> Hom_R(B,R)`, `b |-> lambda(b * _)`, is an isomorphism. The determinant
is a unit because it is nonzero modulo `t`.

Generically `B_K=K[v]/(v^10)`. Define the canonical saturated ideals

`N_i=B intersect v^i B_K`, for `0<=i<=10`.

Every quotient `B/N_i` is torsion free over the DVR `R`, so the relevant
submodules split as `R`-modules. Each `E_i=N_i/N_(i+1)` has rank one and is
free. Also `B/N_1=R`: it is a finite integral `R`-subalgebra of `K`, and `R`
is integrally closed. Generic computation, followed by torsion freeness,
gives `Ann_B(N_i)=N_(10-i)`.

For any ideal `J`, its orthogonal for the Frobenius pairing equals its
annihilator. Indeed, if `lambda(bJ)=0`, then `lambda(bjc)=0` for all `c`,
and perfectness forces `bj=0` for every `j`. Consequently `N_9` is dual to
`B/N_1=R`. The restriction of `lambda` identifies `N_9` with `R`, and the
induced pairings

`E_i tensor E_(9-i) -> E_9`

are perfect. For example any functional on `E_(9-i)` extends to `B` by the
saturated direct-summand property; its representing element lies in `N_i`,
and its kernel on passage to the graded piece is `N_(i+1)`. This proves the
claim for the actual multiplication maps, including at nonprimitive points.

The filtration glues because it is intrinsically the saturation of nilradical
powers. Put `L=E_1`. The iterated multiplication `L^i->E_i` is generically an
isomorphism of line bundles, with effective zero divisor `D_i`. Thus

`E_i=L^i(D_i)`, `D_0=D_1=0`.

Associativity and perfect complementary multiplication yield identities and
inequalities of actual divisors, rather than only numerical classes:

`D_i+D_j <= D_(i+j)` for `i+j<=9`,

`D_i+D_(9-i)=D_9` for `0<=i<=9`.

The conormal map onto `E_1` is surjective: the ambient ideal of `C` maps onto
the nilradical, and its square maps into `N_2`. Therefore
`O(-7)^2 ->> L` and `l=deg L>=-7`.

## 3. Exact socle and genus identities

The top piece is `Ann_(O_X)(I_C)`. Gorenstein duality identifies it with
`omega_C tensor (omega_X|C)^(-1)`. Complete-intersection adjunction gives
`omega_X=O_X(5+8-4)=O_X(9)`, while `O_C(1)=O_P1(4)` and `omega_C=O(-2)`.
Hence

`E_9=O(-38)`, and `9l+d_9=-38`.

Effectivity of `D_9`, together with the conormal quotient bound, leaves
exactly three possibilities:

| `l` | quotient direction degree `e=l+7` | `d_9` |
| --- | --- | --- |
| -7 | 0 | 25 |
| -6 | 1 | 16 |
| -5 | 2 | 7 |

The arithmetic genus is `p_a(X)=1+40*9/2=181`, so `chi(O_X)=-180`.
Complementary duality gives `sum_(i=0)^9 d_i=5d_9`; therefore additivity of
Euler characteristic gives

`chi(O_X)=10+45l+5d_9=-180`.

This is precisely five times the socle degree relation, plus ten. It gives
no further independent constraint. A globally primitive structure is
impossible numerically: it would have `D_9=0` and `9l=-38`.

## 4. Complete necessary divisor inequalities in four divisors

Write `A=D_2`, `B=D_3`, `C'=D_4`, and `T=D_9` (the prime on `C'`
distinguishes this divisor from the support curve). The complete defect
sequence is necessarily

`(D_0,...,D_9)=(0,0,A,B,C',T-C',T-B,T-A,T,T)`.

All its effectivity and superadditivity conditions are equivalent to

`0<=A<=B<=C'`,

`2A<=C'`, `2C'<=T`, `A+B+C'<=T`, and `3B<=T`.

Here every inequality holds coefficientwise at every point. To check
equivalence, multiplication by `E_1` gives monotonicity; the new unordered
pairs with both indices at least two are `(2,2)`, `(2,3)`, `(2,4)`, `(2,5)`,
`(2,6)`, `(2,7)`, `(3,3)`, `(3,4)`, `(3,5)`, `(3,6)`, `(4,4)`, and `(4,5)`.
Substitution gives exactly the displayed inequalities, their repetitions,
and complementary equalities. No further pair occurs with index sum at most
nine.

For degrees `a=deg A`, `b=deg B`, `c=deg C'`, this implies:

| `l` | `a` | `b` | `c` |
| --- | --- | --- | --- |
| -7 | 1 through 6 | at most 8 | at most 12 |
| -6 | 0 through 4 | at most 5 | at most 8 |
| -5 | 0 or 1 | at most 2 | at most 3 |

The positive lower bound in the first row additionally uses P-010. If
`l=-7` and `D_2=0`, the canonical embedded triple has pieces `O,L,L^2`;
in codimension two it is primitive everywhere. One normal coordinate
generates its nilradical locally by Nakayama, and a transverse normal
coordinate supplies a smooth local containing surface. Thus it contradicts
the repository's independently audited primitive-triple exclusion. No such
extra lower bound is asserted for `l=-6` or `-5`.

An exact exhaustive enumeration of the resulting degree inequalities gives
198 triples for `l=-7`, 97 for `l=-6`, and 13 for `l=-5`: **308 necessary
degree triples**, not 308 classified structures. The last row is explicitly

`(0,0,0),(0,0,1),(0,0,2),(0,0,3),`

`(0,1,1),(0,1,2),(0,1,3),(0,2,2),(0,2,3),`

`(1,1,2),(1,1,3),(1,2,2),(1,2,3)`.

The standalone enumerator uses only Python's standard library and tests each
retained sequence against every original superadditivity and complementary
condition. It also tests the compact conditions against the original
conditions on every degree triple in the finite bounding boxes. Its source
and exact output are linked in the accompanying execution record:
[multiplicity-ten degree enumeration](../validation/2026-10-11-multiplicity-ten-filtration/execution-record.json).

## 5. Why this does not classify multiplicity-ten structures

Actual coefficientwise divisor data are stronger than the degree
inequalities. Even actual divisor data and perfect graded pairings do not
by themselves construct compatible local saturated ideals, higher normal
jets, or a global embedding in `P^3`. A locally embedded Gorenstein multiple
curve need not be arithmetically Gorenstein. The global complete intersection
requires that stronger property, as recorded in P-035.

The degree of `T` is not the degree of the common first-normal Fitting
divisor. Already the finite-flat multiplicity-ten local complete intersection

`R[[x,y]]/(t*x-y^2,x^5)`

has generic algebra `K[y]/(y^10)`, saturated defects
`D_i=floor(i/2)[t=0]`, and first-normal image `t*x`. Its common Fitting divisor
is `[t=0]`, whereas `D_9=4[t=0]`. The `R`-basis
`x^a*y^b`, `0<=a<5`, `0<=b<2`, proves finite flatness and rank ten;
`x=t^(-1)y^2` proves the asserted filtration. A second model

`R[[x,y]]/(t*x-y^5,x^2)`

has `D_i=floor(i/5)[t=0]`, so its first four defects vanish even though it
is nonprimitive at the special point. These are local shields against false
filtration shortcuts, not projective candidates.

The strongest verified conclusion here is therefore the three possible
line degrees, the exact coefficientwise four-divisor reduction, and the
308 necessary numerical triples. A `(5,8)` exclusion still needs an embedded
extension obstruction, a surface/conductor argument, or another condition
that removes all surviving divisor and higher-jet data.


---

## Source: 2026-10-11-session-quintic-continuation-results-acceptance.md

# Root acceptance: entire endpoint quintic lane excluded

Date: 2026-10-12, closing the post-seal continuation begun October 11.
Author: root. The universal integral-projective-curve STCI question and
the unrestricted characteristic-zero question for fixed
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. No novelty claim is certified.

## 1. The exact new theorem

**PROVED HERE / independently audited.** In the sectional-genus-one
quintic-normalization lane for fixed C0 over every algebraically closed
field of characteristic zero, every admissible intrinsic endpoint
projection has no mate of any positive degree. All four lift parameters
and every positive mate exponent are covered. The center must avoid
the normalization, as required for an actual finite normalization map;
base-point projections are excluded from admissibility, not assumed away
inside a purported parameter exhaustion.

The normalization and lifted curve have the exhaustive pair (S,c) in the
[intrinsic classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md),
with the independently reconstructed
[explicit model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
and [local A4 chart](OCT11_QUARTIC_DEPENDENCIES_AND_DP5_ENDPOINTS.md#source-2026-10-11-session-dp5-a4-local-chart-independent-auditmd).
The frozen [quintic structural frontier](#source-2026-10-11-session-quintic-structural-frontiermd)
and [del Pezzo/conormal audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
supply the actual single A4 normalization, unique line ell and section
Q of 4H with div(Q)=5c. Every hypothetical mate pulls back to a nonzero
scalar Q^k, with degree 4k. The surface and full inverse-support
conditions concern actual schemes and morphisms, not numerical classes
alone.

The intrinsic pair is unique up to polarized isomorphism, but its
permitted projections are not one orbit. The pair automorphisms allow
translations and no residual scaling. Endpoint centers form one orbit
with four lift parameters; nonendpoint centers retain a nonzero
separation modulus as well as four lifts. Earlier four-parameter
wording describes the endpoint family only. **The new theorem does not
exclude the entire genus-one quintic lane.**

## 2. Exhaustive endpoint assembly

The normalized endpoint sections on S minus ell=A2(r,T) are

    X=(1+aT, r+bT, r^3+(g-r)T,
       r^4+(d-2r^2-r)T+T^2), c:T=0.

The three disjoint cases below exhaust all four parameter values.

* **a=0,b!=0:** the [complete support proof](QUINTIC_ENDPOINT_RESIDUAL_SUPPORT_AND_EXCESS.md)
  and [independent audit](2026-10-11-session-quintic-endpoint-a0-polynomial-support-independent-audit.md)
  prove an actual off-c point over C0 for every b,g,d. The degree-six
  residual polynomial cannot have all its roots at the common roots of
  its quadratic and cubic inputs. Denominator-zero fibers are explicitly
  retained; one-root coefficient/derivative conditions contradict, and
  the two-root factorization also contradicts. All images have X0=1.
* **a=b=0:** root accepts the [all-power jet proof](2026-10-11-session-quintic-endpoint-a-b-zero-jet-obstruction.md)
  and [independent direct audit](2026-10-11-session-quintic-endpoint-a0-b0-power-jet-independent-audit.md).
  In the actual fourth chart at generic ell, the map differential has
  transverse kernel D, but the actual downstairs-frame function
  q=Q/X2^4 has D(q^k)=k(5-2r+4g), nonzero for every positive k.
  Every descended function must have D derivative zero. No conductor
  flatness/reducedness hypothesis or higher-contact bound is inferred.
  The separate [twelve-condition check](2026-10-11-session-quintic-endpoint-abzero-first-jet-independent-audit.md)
  verifies the source-section frames and first jets; the power rule is
  the direct all-k proof, not a computational extrapolation.
* **a!=0:** root accepts the [complete support proof](2026-10-11-session-endpoint-a-nonzero-full-support-exclusion.md)
  and [complete independent global audit](2026-10-11-session-endpoint-a-nonzero-global-independent-audit.md).
  Cb=a^2g-ab-b^3=0 gives an actual extra endpoint inverse point or a
  forbidden base point. On Cb!=0 the target residual has exact degree
  seven, with all roots yielding genuine finite-target fibers. The A=0,
  X0=0 and h=0 exceptional cases are checked before division. The sole
  support-compatible h=0 fiber has order exactly two. The
  [independent target-contact proof](OCT11_QUARTIC_DEPENDENCIES_AND_DP5_ENDPOINTS.md#source-2026-10-11-session-endpoint-two-common-roots-target-contact-independent-auditmd)
  derives actual third and fourth jets: every compatible root has order
  at most four, and an order-four root prohibits any second common point.
  Thus one or two common points cannot carry seven roots. Three points
  force U|V with a=3b^2/2; the independently implemented
  [original-variable](#source-2026-10-11-session-three-common-roots-residual-quartic-independent-auditmd)
  and [shifted-variable](2026-10-11-session-endpoint-three-common-roots-shifted-replay.md)
  quartic certificates contradict full root support on every allowed
  parameter value. No finite exceptional set remains in this endpoint
  case.

Root has read the actual complete proofs and audits, reconstructed the
target substitutions and exceptional fibers, the rational-parameter
denominator conditions, the number-of-roots exhaustion, and the
downstairs-frame differential obstruction. The independent global audit
was saved with its complete PASS verdict before its worker later hit a
usage limit. That terminal error does not supply a theorem; the saved
written audit and its bound exact records supply the evidence used here.

The previously accepted [quadric-factor reduction](QUINTIC_CARRIER_CONORMAL_AND_FACTOR_GEOMETRY.md),
[factor audit](2026-10-11-session-quintic-endpoint-factor-independent-audit.md),
and [contact-length audit](2026-10-11-session-quintic-endpoint-factor-contact-independent-audit.md)
remain valid. The separate [direct-r excess proof](2026-10-11-session-quintic-endpoint-a-nonzero-local-excess-bound.md)
provides another route with explicit QQ Bezout certificates. It is not
needed to replace the global target-fiber proof. First-normal degrees
alone supply no bound on later contact lengths.

## 3. Other accepted reductions and the remaining nonendpoint task

Root accepts the direct full-conductor algebra statements in the
[power-descent audit](2026-10-11-session-power-descent-algebra-audit.md):
actual conductor-algebra membership is required; tensor equalizers can
give false positives; in characteristic zero powers cannot repair a
unit nilpotent jet after its reduced phase is resolved; and purity of
the actual normalization quotient makes full generic membership
sufficient for global descent. Split reduced phases may still have
unbounded root-of-unity orders as the projection varies. This is an
exact criterion in the reduced genus-one lane, not a parameter solution.
Its final four-parameter wording is superseded by the two-lane scope
correction in section 1.

The new [nonendpoint filtration and line-jet note](#source-2026-10-12-session-nonendpoint-pole-filtration-and-line-jetmd)
records a direct root reconstruction after that worker's usage-limit
stop. The full pole filtration has generators of weights 2,3,5, giving
seven sections in O(6ell). The pulled quadric has an actual residual
Weil divisor of degree six, with possible prime-degree partitions
6,2+4,3+3,2+2+2. A specified entire-line rank-one subfamily has an
all-power differential obstruction. Seven supporting identities pass
after a retained multiline-expression failure and a protected-name
failure were repaired. **A separate mathematical proof audit of this
new bounded note remains outstanding.** It is not promoted here to an
independently audited nonendpoint theorem; the generic unramified
five-parameter family remains open.

## 4. Antecedents, open scope and epistemic limits

The frozen [all-quartic acceptance](OCT11_QUARTIC_DEPENDENCIES_AND_DP5_ENDPOINTS.md#source-2026-10-11-session-all-quartic-results-acceptancemd)
continues to exclude every integral quartic carrier, with any mate.
Its factor consequence makes both defining degrees at least five.
There is no upper degree bound or theorem forcing an unrestricted
presentation into the newly excluded endpoint family. The accepted
[multiplicity-ten filtration](#source-2026-10-11-session-multiplicity-ten-filtration-auditmd)
leaves 308 necessary numerical profiles for (5,8), not realizations or
a degree-pair exclusion. Other nonnormal quintic genera, normal
quintics, higher carriers, entirely thick presentations, the retained
split-sextic boundary and the distinct common-ancestor incidence remain
open. The universal problem and unrestricted C0 problem are unresolved.

## 5. Exact accepted input versions

These are root-reviewed proof/audit versions. Their SHA-256 values
identify the accepted bytes; mathematical acceptance comes from the
written arguments, not the existence of a hash.

| Input note | SHA-256 |
| --- | --- |
| Intrinsic pair classification | `537e341fb79632997648209efb7728c64229d7bd648cc2721285e8ab04cf0e0f` |
| Explicit-model independent audit | `f19ae25848ba77a5c59f3a9ce53819b24258c03b5d90f234b31ec7581306f8bd` |
| a=b=0 owner proof | `31fce973db8cfdbb223e421692739e35f1d1a8cfc69b6026ab186b0b0d761bd1` |
| a=b=0 independent audit | `6b4dc6de246759667c54953aab0ead3cc295e5226a3b7c85dc39463ece5e10d9` |
| a=0,b!=0 independent audit | `e0586983289a8f802618bdd156552e7b750c0ec3fcbe95e84f743d8851572431` |
| a!=0 complete owner proof | `26b204f51bf7648b1d5c260cf2dba4fe034e076a2bbcb8f01cc4fa6fac5e8881` |
| a!=0 complete global audit | `a47e218d20cf7f835b7f9ce9ee470a85cc4fe146f81e1438bb15e1a5f126f824` |

The source/stream histories retain development failures, corrected
provisional claims and limits. In particular the provisional order-three
bound and the negative sign in a=-3b^2/2 were rejected before acceptance.
The accepted argument uses order four and a=+3b^2/2. Coprime
univariate resultant factors are used with an explicit necessary
simultaneous-vanishing implication, not as an empty-locus assertion for
unrelated multivariate polynomials.

The independent provenance review discloses 20 A4 exact-model script
executions, including 13 original tool observations and seven later
captured replays. Original tool rows lack original raw streams; versions
08/09 were reconstructed, and failed diagnostic 11 was not captured in
the six failure replays. The phrase "every retained failure reproduced"
in that older record is qualified accordingly. The local-chart history
has four executions, including the original protected-name failure and
its replay. Copied sources and successful replays add no independent
theorem or new parameter case. All later histories have separately
scoped records, rather than an inflated aggregate verifier count.

The old October 11 seal is frozen historical evidence. A separate
quintic-continuation record seal is being completed; its PASS, if obtained,
certifies routing, observed bytes and disclosed provenance, not
mathematical truth, novelty or universal resolution. Preparation was
interrupted by explicit usage-limit errors; root is preserving that
draft and completing the final scoped record check without pretending
the interrupted draft had already passed.

Live October 12 inspection found HEAD
`0adab2bd188351a77d961d7f2251c21545aaebcc`, title
`2026-10-11 limit reached`, branch `research/ultra-resume-2026-10-06`.
The earlier `2ba77d1a1177db9390693066c6b185040766c089` is now historical;
root did not create the newly observed commit. It preserves the preceding
October 11 proofs and interrupted validation preparation. This acceptance,
the October 12 nonendpoint reconstruction, its repairs and current canonical
edits are new saved uncommitted continuation data. Root makes no Git mutation.


---

## Source: 2026-10-11-session-quintic-structural-frontier.md

# Quintic carriers: rationality boundary and the degree-five A4 target

Date: 2026-10-11. Owner: `oct11_quintic_structural_frontier`.
Status: **PROVED HERE / DIRECT PROOF AUDITED; NECESSARY STRUCTURAL
REDUCTIONS**. The pi=0 statement is an all-mate exclusion; the other
statements retain the explicit open conductor and carrier strata below.
Scope: an algebraically closed field of characteristic zero, the fixed
smooth rational quartic `C0=[s^4:s^3t:st^3:t^4]`, an integral quintic
`X`, and an arbitrary ambient mate. This is structural progress beyond
the quartic-carrier work, not an exclusion of all quintics or an STCI
resolution. The accompanying
[independent conormal audit](2026-10-11-session-quintic-conormal-and-delpezzo-audit.md)
records the independently checked parts; its status takes precedence
over any unreviewed continuation lead below.

## 1. The actual normalized divisor, rather than a quartic analogy

Let `nu:S->X` be the finite normalization, `sigma:M->S` its minimal
smooth resolution, `H=nu*O_X(1)`, and `L=sigma*H`.

The quintic is regular at the generic point of C0. On its unique smooth
quadric `Q`, the curve has class `(1,3)`. If a quintic were singular
along the entire curve, its restriction to Q would contain twice C0,
leaving class `(3,-1)`, which is not effective. Hence its equation
would be divisible by q, contrary to integrality. This is exactly the
saturated-sheaf-square argument in P-011 of the
[research record](../RESEARCH_RECORD.md), not membership in the
unsaturated ideal square.

The dominating lifted curve `c` is therefore isomorphic to C0. Under
a mate, the full-support theorem also gives
`(nu^{-1}(C0))_red=c`. Intersecting the mate divisor with H gives

    H^2=5, H.c=4, b=4k,
    div_S(nu*G)=5k c ~ 4k H,
    c_num=(4/5)H.

In particular `c_num^2=16/5`. If c were Cartier on S, this would be an
integer, a contradiction. Thus every quintic mate requires a
non-Cartier point of c on its normalization. A smooth normalization,
or a lift avoiding its singular locus, is excluded in every mate
degree. More generally, if r c is Cartier, then
`16r^2/5` is integral, so `5|r`.

Do not replace the relation by `2c~mH`: intersecting with H would give
`8=5m`, which has no integer solution. The quartic double-ribbon
mechanism cannot be imported in this form.

For orientation, `dim I_C0(5)=35`. Restriction of degree-five monomials
onto the binary forms of degree twenty is surjective: sums of five
weights from `{0,1,3,4}` cover `0,...,20`. The first normal map has
the previously verified image `H0(O(13))^2` and kernel `q I_C0(3)`
of dimension seven. These dimensions are not a parameter exhaustion
or a substitute for full conductor descent.

## 2. Rationality through sectional genus three, without a mate

Let pi be the genus of a general hyperplane curve on S. A general
plane quintic has arithmetic genus six, so

    0<=pi<=6; if X is nonnormal, pi<=5,
    K_M.L=2pi-7.

**Theorem.** If `pi<=3`, the normalization of an integral quintic
containing C0 is rational. A mate is not needed.

Here `K_M.L<0`; thus no positive multiple of K_M is effective and
the characteristic-zero surface classification makes M rational or
birationally ruled. Suppose its minimal ruled model has base B of
genus g>=1. Push L down successively through the point blowdowns and
write its ruling degree as `a>0`. At each blowup, the multiplicity
`m_i` satisfies `0<=m_i<=a`: intermediate polarizations are nef, and
the actual positive fiber cycle through the center has total L-degree
a. This holds at infinitely near centers as in the independently
checked [quartic ruled proof](2026-10-09-session-nonrational-normalization-independent-audit.md).

The same elimination of the ruled-section coefficient gives

    5=(2g-2)a^2+(7-2pi)a+sum_i m_i(a-m_i).          (1)

The smooth P1 strict transform `c#` maps constantly to B, hence is
one fiber component. Nefness and the positive component multiplicities
give `4=L.c#<=a`. For pi<=2, (1) instead gives `a<=1`, impossible.
For pi=3, it gives `4<=a<=5` and forces g=1.

If a=4, the final sum must be one. But the possible summands for
integer `0<=m_i<=4` are `0,3,4`, so this is impossible. If a=5,
the sum is zero and every m_i is zero or five. Initially a ruling
fiber has degree five. After each blowup, its strict components lose
an integer multiple of m_i and the new exceptional component has
degree m_i. Inductively the L-degree of every fiber component is
divisible by five. This contradicts `L.c#=4` and finishes the proof.

At pi=4 or five, K_M.L is positive and this proof supplies no
rationality theorem. Do not transfer the quartic rationality conclusion
to these strata.

## 3. The entire sectional-genus-zero lane is excluded

The characteristic-zero vanishing and minimal-degree argument used in
the [quartic genus-zero proof](SECTIONAL_GENUS_ZERO_NORMALIZATION_PROOF.md)
applies with degree five. Namely `K_M.L=-7`,
`chi(K_M+L)=chi(O_M)-1`, and negative nef degree plus vanishing give
`chi(O_M)=1`, `p_g=0`, and `h1(O_M)=0`. Restriction to the general
P1 of degree five gives `h0(S,H)=7`. The complete map is finite
birational onto an integral minimal-degree surface of degree five
in P6. The classification leaves

    S(2,3), S(1,4), S(0,5).

The first two are smooth rational scrolls and are excluded by
`c_num^2=16/5`. On the cone S(0,5), resolve by F5 with negative
section E and `L=E+5f`. Any nonexceptional integral curve of
H-degree four would have strict-transform class `aE+4f`.
Its ruling degree a is a nonnegative integer. If a=0, an integral
vertical curve is a single ruling, of degree one, not four. If a>=1,
its intersection with E is `4-5a<0`, forcing E as a component,
contrary to being a strict transform. Thus the cone cannot even
contain this lifted degree-four curve.

This proves the pi=0 quintic-carrier exclusion in every mate degree.

## 4. A canonical-index filter independent of rationality

If S is Gorenstein, K_S is Cartier and

    K_S.c=(4/5)K_S.H=(4/5)(2pi-7)

must be an integer. Consequently `pi=1` or six. For a nonnormal
quintic this leaves only pi=1. If S is Q-Gorenstein and `rK_S`
is Cartier globally, the corresponding necessary condition is

    5 | r(2pi-7).

Thus pi=0,2,3,4,5 require `5|r`; a non-Q-Gorenstein normalization
remains a separate stratum. A rational singularity alone does not
give a Cartier canonical class.

Normal quintic hypersurfaces are Gorenstein and have pi=6. Nothing
in this filter excludes them.

## 5. Every pi=1 normalization under a mate has exactly one A4 point

By section 2 M is rational. The adjoint proof in the
[degree-four del Pezzo reduction](OCT9_GENUS_ONE_TWO_AND_CONDUCTOR.md#source-2026-10-09-session-genus-one-delpezzo-reductionmd)
now applies with `L^2=5`: `K_M.L=-5`, and vanishing and
Riemann--Roch give one effective divisor `A~K_M+L` with `L.A=0`.
Every component is sigma-exceptional. Minimality and prime adjunction
give `K_M.E>=0` on each exceptional prime. Hence
`A.E>=0`, so negative definiteness forces A=0. Therefore

    K_M=-L, K_M^2=5,
    S is a Gorenstein ADE del Pezzo surface of degree five.

The chosen-canonical-form proof of crepancy is unchanged. Its imported
surface input is [Reid's Du Val characterization](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf),
Theorem 2.1(2). The anticanonical orthogonal lattice is A4 and the
complete anticanonical model embeds in P5; the standard weak del Pezzo
lattice and embedding results are in
[Dolgachev, Chapter 8](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1467/2025/10/CAG-2.pdf),
sections 8.2 and 8.3, particularly Theorem 8.3.2(iii).

Write the Mumford correction as `c#+Z=(4/5)L`. Adjunction on the
smooth rational strict transform gives

    c#^2=2, -Z^2=6/5.                                (2)

The exceptional roots form a subsystem of A4. In the realization
`{e_i-e_j:1<=i!=j<=5}`, components are blocks of coordinate indices
and have type A_(block size-1). Any proper subsystem therefore has
Cartan determinant with no factor five. Its inverse matrix cannot
produce the denominator five in (2). The exceptional configuration
must be the full single A4 chain; there are no additional singular
points of S.

The smooth passage lemma gives one transverse contact with one prime
in this chain. The inverse Cartan diagonal is
`4/5,6/5,6/5,4/5`, so the contact is with the second or third vertex.
For the second vertex, `5Z=(3,6,4,2)`; the third is the reversal.
Numerical equivalence is linear equivalence on the smooth rational M,
and pushing the resulting section down gives the actual relation

    5c ~ 4H, Q in H0(S,4H), div_S(Q)=5c.             (3)

Every normalized mate is a scalar multiple of `Q^k`, with b=4k.
The section Q need not belong to the four-coordinate ambient section
ring. Equation (3) does not supply an ambient quartic carrier.

## 6. A unique tangent line fixes the restriction and projection geometry

We have `h0(S,H)=6` and `h0(c,H|c)=5`; restriction has a nonzero
kernel. Every kernel section has actual divisor `c+ell`, since the
residual effective Weil divisor has H-degree one. It has precisely
one integral component ell with multiplicity one. In the complete
anticanonical embedding, ell is a projective line, hence smooth P1.

Its strict transform is smooth, has `L.ell#=1`, and satisfies
`ell#^2=-1` by adjunction. Numerical degree gives
`ell_num=(1/5)L`, hence its correction has square `-6/5`; it too
passes through an interior A4 vertex. If two distinct such lines
existed, their numerical intersection would be 1/5, whereas the
cross correction for either pair of interior vertices is at least
4/5. Their strict-transform intersection would be negative, which
is impossible for distinct effective curves on a smooth surface.
The line ell is therefore unique.

Every kernel section has the same actual divisor c+ell; the ratio
is a global unit on the proper normal integral S, thus a scalar.
The restriction kernel is exactly one-dimensional and restriction
onto H0(P1,O(4)) is surjective. Consequently c is the full rational
normal quartic in its span P4 inside P5.

The two curves use opposite interior A4 vertices: using the same
vertex would make their strict intersection `4/5-6/5<0`.
For opposite vertices it is `4/5-4/5=0`. Thus c and ell meet only
at the A4 point. The Cartier anticanonical divisor c+ell has
arithmetic genus one, while both components have genus zero, so
their scheme intersection has length two. The line ell is the
tangent line to this rational normal quartic at the A4 point.

Also `5ell~H`, obtained by subtracting (3) from `5(c+ell)~5H`.
If h is the unique section with divisor c+ell and u the section
with divisor 5ell, then

    Q = h^5/u

is a regular section of 4H, with divisor 5c. This identity is
intrinsic; h and u need not descend to the chosen P3 projection.

The original four coordinates constitute a four-dimensional subspace
V of H0(S,H). They define projection from a line in P5 disjoint
from S. Their restriction to c is injective because C0 is not
planar. Hence the projection line meets the hyperplane span of c
in its prescribed rational-quartic projection center, the point
corresponding to the omitted binary quartic s^2t^2 after fixing
the C0 parametrization. Choosing lifts of these four sections
leaves four coefficients in the one-dimensional restriction kernel.
This is a concrete small projection target, with finiteness,
birationality, center avoidance and conductor descent still required.

## 7. The actual conductor has degree five, not a line

In this pi=1 lane finite duality and `omega_X=O_X(H)` give

    I=Hom_X(nu_*O_S,O_X)=nu_*O_S(-2H).

Thus the upstairs actual conductor D is Cartier in |2H|,
with `H.D=10` and `p_a(D)=6`. The downstairs conductor Gamma
is a pure Cohen--Macaulay curve. Computing the difference of the
quintic hypersurface and del Pezzo Hilbert polynomials gives

    P_Gamma(m)=5m-1, deg Gamma=5, p_a(Gamma)=2,
    nu_*O_S/O_X = omega_Gamma(-H), polynomial 5m-4.

These statements concern the entire conductor ideal. They do not
assert that Gamma is reduced, smooth or Gorenstein, or that
`D->Gamma` is everywhere flat. No quartic conductor-line theorem
has been transferred. The next geometric task is whether any of
these four-parameter projections can make a power `Q^k` descend
through its entire conductor; k remains unbounded.

## 8. Continuation boundary and first numerical target

The next fixed-C0 quintic lanes are:

* pi=1: the degree-five A4 del Pezzo target above, with its actual
  projection and full conductor power descent.
* pi=2,3: rational normalization, necessarily either non-Q-Gorenstein
  or with global canonical index divisible by five under a mate.
* pi=4,5: neither rationality nor a complete model classification
  has been proved here; retain the same canonical-index distinction.
* pi=6: normal Gorenstein quintic hypersurfaces, not covered by the
  quartic anticanonical exceptional-divisor classification.

The smallest mate degree after the complete quartic exclusion is
b=8, giving transverse multiplicity ten. The separate
[multiplicity-ten filtration audit](#source-2026-10-11-session-multiplicity-ten-filtration-auditmd)
has 308 necessary degree profiles, not 308 realized structures or a
global parameter exhaustion. Nonregular first-normal ratios, higher
jets and genuine closed-point defect divisors must survive any
subsequent reduction. First-normal rank conditions alone cannot
exclude the quintic lane or the unrestricted STCI question.


---

## Source: 2026-10-11-session-three-common-roots-residual-quartic-independent-audit.md

# Three-common-root family: independent residual-quartic support exclusion

Status: **PROVED (univariate algebra, characteristic zero).** No geometric
exclusion is asserted in this note. The proof handles every parameter in the
specified family with the stated carrier coefficient nonzero; it has no finite
exception set on that locus.

## 1. Corrected parameter family

Let the field be algebraically closed of characteristic zero and let `b != 0`.
The condition that the cubic `U` divide the quartic `V` fixes

\[
a=\frac32b^2,\qquad
g=\frac1{9b}-\frac23,\qquad
d=\frac1{54b^2}-\frac1{9b}.
\]

The initially transmitted negative sign `a=-3b^2/2` is incompatible with
`U | V`. Indeed the exact remainder for that negative sign is

\[
V\bmod U=-z^2-\frac{z}{3b}+\frac{1-6b}{27b^2}.
\]

For the corrected positive sign the quotient is

\[
V=\left(\frac32z+\frac1{6b}\right)U.
\]

Use the definitions from the parent calculation:

\[
\begin{aligned}
U&=2az^3-3bz^2-z+g,&
V&=3az^4-4bz^3-2z^2-z+d,\\
A&=az-b,&h&=az^3+z-g-1,\\
J&=AV-(Az-1)U,&
E&=J^2-(3zA-1)hJ+AUh^2.
\end{aligned}
\]

Since `U | V`, also `U | J` and `U | E`. Write `S=E/U`. The carrier
coefficient in the task is

\[
C_b=a^2g-ab-b^3=-\frac34b^3(2b+3).
\]

Thus its nonzero locus is exactly `b != 0,-3/2`.

## 2. The exact quartic

An exact expansion gives `S=-T/(432b)`, where

\[
\begin{aligned}
T={}&(324b^5+486b^4)z^4-(54b^4+405b^3)z^3\\
&+(270b^3+81b^2)z^2-(72b^3+132b^2+36b)z\\
&+48b^2+352b+12.
\end{aligned}
\]

In particular the leading coefficient of `S` is `C_b/2`; hence `S` has degree
exactly four for every allowed specialization. The degree of `U` is exactly
three because its leading coefficient is `3b^2`.

## 3. Two incompatible necessary resultants

Define

\[
R=(12b^2+116b+3)(72b^4+252b^3+1126b^2+513b+54)
\]

and

\[
\begin{aligned}
D={}&(2b+3)(2b^2+9b+15)^2\\
&\quad\cdot(9216b^6-208896b^5-2002096b^4-2800992b^3\\
&\hspace{52mm}-117672b^2+72b+45).
\end{aligned}
\]

The exact resultant identities are

\[
\operatorname{Res}_z(U,S)=-\frac{3b^5}{2048}R,
\qquad
\operatorname{Res}_z(S,S')=\frac{b^9}{8388608}D.
\]

Exact Euclidean polynomial arithmetic verifies

\[
\gcd_{\mathbf Q[b]}(R,D)=1.
\]

Now suppose every root of `S` were a root of `U`. The quartic `S` has at least
one root, so `U` and `S` would have a common root. Also a quartic whose distinct
roots lie among the at most three distinct roots of a cubic necessarily has a
repeated root. Therefore both displayed resultants would vanish. Since `b`
is nonzero, this would require `R(b)=D(b)=0`, contradicting their exact
coprimality. The argument works without assuming that `U` is squarefree.

Consequently, for **every** allowed `b`, the support of `S` is not contained in
the support of `U`. There are no exceptional parameters on `C_b != 0`.

## 4. Scope and evidence

The result excludes the univariate support condition in the corrected
`U | V` family. It does not on its own classify the other common-root strata,
prove that the displayed polynomial is the required global conductor
obstruction, or exclude a geometric STCI presentation. Those interpretations
remain the parent's responsibility.

The final source is
[verify_session_three_common_roots_residual_quartic_2026_10_11.m2](../computations/verify_session_three_common_roots_residual_quartic_2026_10_11.m2),
SHA-256 `e0762fcc2c959cbf32b87de10ced160b7913b0da5d0de6875917a9a97632727b`.
Its **eight exact assertions passed** in a captured execution. They verify
both divisibilities, exact quotient, carrier coefficient, quartic leading
coefficient, both resultant formulas and the coprimality. The negative-sign
remainder is also printed.

The fresh one-shot execution record, copied source, stdout and stderr are in
[2026-10-11-three-common-roots-quartic-support](../validation/2026-10-11-three-common-roots-quartic-support/execution-record.json).
The copied source is an execution snapshot of this one source, not a second
independent computation. Earlier development invocations of the source were
successful but were not captured as additional execution records; no count
or certificate relies on them.


---

## Source: 2026-10-12-session-nonendpoint-pole-filtration-and-line-jet.md

# Nonendpoint quintics: exact pole filtration and a ramified-line subfamily

Date: 2026-10-12. Author: root, completing the saved calculations of
`oct11_nonendpoint_quadric_structure` after its explicit usage-limit stop.

Status: **DIRECT STRUCTURAL PROOF AND BOUNDED ALL-POWER OBSTRUCTION;
separate mathematical proof audit remains outstanding**. Seven supporting
identities now pass in a captured repaired execution. This is not an
exclusion of the entire nonendpoint family or of all quintic carriers.
Work over an algebraically closed field of characteristic zero.

## 1. The full nonendpoint parameter and actual sections

Use the accepted genus-one normalization pair in the
[intrinsic classification](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md)
and [explicit model](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
On S minus ell use r,T with

    U=(1,r,r^2,r^3-rT,r^4-(2r^2+r)T+T^2), h=T.

The A4 point on c is r=infinity. Translate the two finite double roots
of the projection-center binary quartic to 0,delta, where delta!=0.
Here delta is their difference, rather than the half-separation used
in the midpoint convention of the classification. It cannot be scaled
to one by an automorphism of the pair. The four lift parameters a,b,g,d
give actual sections

    X0=U4+a h,
    X1=U4-delta U3+b h,
    X2=U4-3delta U3+3delta^2 U2-delta^3 U1+g h,
    X3=U4-4delta U3+6delta^2 U2-4delta^3 U1+delta^4 U0+d h.

On c these restrict to r^4, r^3(r-delta), r(r-delta)^3,
(r-delta)^4. They give fixed C0 with target parameter z=(r-delta)/r.
The intrinsic A4 point maps to the nonendpoint z=1. A line center
must still avoid S for an admissible normalization projection.

## 2. All pole sections along ell, with no cancellation shortcut

Put t=T-r^2 and v=t^2-r^3. The affine coordinate ring of S minus ell
is k[r,t], equivalently

    k[r,t,v]/(t^2-r^3-v).

The relation is monic in t, so the monomials r^i t^j v^k, with
i,k>=0 and j=0 or 1, are a vector-space basis. In the genuine fourth
blowup chart (x,u), the rational functions in the U0 frame are

    r=x^(-2)/(1+xu),
    t=x^(-3)/(1+xu),
    v=u*x^(-5)/(1+xu)^3.

Their pole orders along ell are 2,3,5. The leading coefficient of
r^i t^j v^k is u^k and its weight is 2i+3j+5k. At any fixed weight,
distinct basis monomials have distinct k: for fixed k the equality
2i+3j=2i'+3j' with j,j' in {0,1} forces i=i',j=j'. Thus their leading
coefficients are independent polynomials in u. There is no cancellation
among the terms of maximal weight in any nonzero linear combination.

Every rational section of O_S(n ell) restricts to a polynomial on the
complete open A2. Conversely a polynomial whose pole order along ell is
at most n has no other codimension-one pole and is a section of this
Weil divisor sheaf, by its definition on a normal surface. Consequently
the displayed weight filtration is exhaustive. In particular

    H0(S,O(6ell))=span{1,r,t,r^2,rt,v,r^3}.

The separately completed [low-pole-spaces proof](2026-10-11-session-a4-low-pole-spaces.md)
gives the same filtration and an exhaustive classification of prime equations
of degrees two, three and four. Root read and reconstructed that saved proof;
it was completed before its parent worker stopped. No CAS run is claimed for
its geometric section-space argument.

This is a seven-dimensional space of Weil-divisor sections, not a claim
that O(6ell) is Cartier or that these are anticanonical sections.

## 3. The exact residual divisor of the pulled quadric

Set A=a+d-b-g and B=ad-bg. For q=X0 X3-X1 X2, direct expansion in the
U0 frame gives q=T F, with

    F=A v-3delta^2 r^3
      +((4a-3b-g)delta-3delta^3-A)rt
      +(B+(6a-3b)delta^2+3delta^3)r^2
      +(B+delta^4)t+((-4a+b)delta^3-delta^4)r+a delta^4.

Its unique weight-six term is -3delta^2 r^3, so its pole order is
exactly six for every nonzero delta and all four lift parameters.
Since div(U0)=5ell and div(T)=c-4ell, the actual section q of 2H has

    div(q)=c+D, D=div(F)+6ell.

D is effective of degree six and does not contain ell. In the actual
fourth-chart frame the restriction of q to ell is -3delta^2, also
showing that ell is not a divisor of q. Dividing the affine normalized
function by T does not make F a section of H: division by the actual
hyperplane h would have a pole along ell. The endpoint factorization
into two anticanonical sections cannot be transferred here.

The accepted unique degree-one prime on S is ell. Since D excludes it,
the possible degree partitions of its prime components, counting
multiplicities, are exactly

    6; 2+4; 3+3; 2+2+2.

These are possible numerical partitions, not an assertion that each is
realized. Their genera, A4 contacts and full inverse support still need
analysis.

## 4. Entire-line ramification forces an all-power obstruction

Use the fourth chart with B0=1+xu, C0=1+x+x^2u. Here
Q=B0^2 C0^5 is the actual section of 4H with divisor 5c. On ell:x=0,
the four actual projection sections restrict to

    (u-1, u-1+delta, u-1+3delta, u-1+4delta).

The generic target differential has rank one exactly when

    g+3delta^2+2a-3b=0,
    d+6delta^2+3a-4b=0.                     (R)

One can obtain these equations by subtracting the first two rows from
the raw projective tangent matrix (section values, their u derivatives,
their x derivatives). Its 3x3 minors generate precisely the ideal
delta times the two left sides. Since delta!=0, vanishing at generic u
is equivalent to (R). The differential has rank at least one: in the
patch X0!=0, the u derivative of X1/X0 is -delta/(u-1)^2.

Put lambda=(b-a)/delta. On (R), the transverse derivation at generic ell

    K=partial_x+(u^2+lambda u-lambda-a)partial_u

annihilates all three actual target affine ratios X1/X0,X2/X0,X3/X0.
For example the x derivative of X1/X0 is
delta*(u^2+lambda u-lambda-a)/(u-1)^2, so its u derivative cancels;
the other two ratios give precisely the two conditions (R).
The chain rule and quotient rule therefore make K annihilate every
pulled-back downstairs local function.

Use the actual downstairs frame X0^4. At generic ell, X0=u-1 is a unit,
and q0=Q/X0^4 is a unit. Direct logarithmic differentiation gives

    K(log Q)|ell=2u+5,
    K(log X0)|ell=u+lambda,
    K(q0)/q0|ell=5-2u-4lambda.

Here log differentiation means the algebraic expression K(f)/f, with
no analytic logarithm assumption. For every positive k,

    K(q0^k)|ell=k*q0^k|ell*(5-2u-4lambda) != 0.

The last factor has u coefficient -2, and characteristic zero makes
-2k nonzero. Every mate would pull back to a nonzero scalar times Q^k,
so its normalized affine function would have both zero and nonzero
K derivative. Therefore every admissible nonendpoint projection
satisfying (R) has no mate in any positive degree.

This excludes a precisely specified subfamily. The generic unramified
family is open; a first derivative at isolated points is not promoted
to an obstruction for every projection.

## 5. Saved failure history and exact supporting evidence

The [supporting source](../computations/verify_session_quintic_nonendpoint_structure_2026_10_11.m2)
passes seven conditions in
[root repair attempt 05](../validation/2026-10-11-quintic-nonendpoint-structure/attempt-05-root-name-repair/execution-record.json).
The final source SHA-256 is
`24ae9f4b3b2092bf7870f4f09e17307b2feda84000ad91eb6087c022b4892738`.
The record binds its copied source, actual exit zero and separate raw
stdout/stderr. Eight printed PASS lines consist of seven conditions and
one final PASS ALL label; they are not eight mathematical checks.

Attempts 01--03 remain saved from before the worker stopped. Attempt 03
failed the residual-expression assertion because a multiline expression
was parsed incompletely. Root attempt 04 wrapped the intended expression
in parentheses, passed the first two checks, and then failed on the
protected Macaulay2 variable hh. Attempt 05 renamed that variable and
passed all seven conditions. Both repairs and both captured root runs
are retained. These are repaired executions of one checker lineage,
not independent geometric proofs. A separate mathematical audit of the
written filtration and subfamily obstruction remains outstanding.


---

## Source: 2026-10-12-session-nonendpoint-results-acceptance.md

# October 12 root acceptance: nonendpoint quintic progress

Root-reviewed continuation after the morning record seal. The universal
integral projective-curve STCI problem and unrestricted characteristic-zero
problem for `C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. All statements below
concern this literal curve and its projective equivalents over algebraically
closed fields of characteristic zero. No novelty claim is certified.
The [all-quartic acceptance](OCT11_QUARTIC_DEPENDENCIES_AND_DP5_ENDPOINTS.md#source-2026-10-11-session-all-quartic-results-acceptancemd)
and [endpoint quintic acceptance](#source-2026-10-11-session-quintic-continuation-results-acceptancemd)
remain unchanged. Older nonendpoint pending/open labels are superseded
only for the precise completed results accepted here.

## 1. Every coprime conormal pair is excluded in every mate degree

**PROVED HERE / independently audited.** In the actual sectional-genus-one
quintic A4 normalization lane, retain all nonendpoint projection parameters
`delta!=0,a,b,g,d` and require the center to avoid the normalization S.
Every such projection with coprime corrected homogeneous conormal cubics
Ph,Jh has no mate of any positive degree. Thus a hypothetical mate requires

    Res_h(Ph,Jh)=0.

This is a proper closed necessary locus, not a claim that it supports
mates or an exhaustion of that locus. All finite common roots, common
roots at infinity, repeated roots and higher contact remain retained.
The normalization model and lifted pair are the previously accepted
[intrinsic pair](DEL_PEZZO_FIVE_A4_INTRINSIC_AND_EXPLICIT_MODEL.md).
The intrinsic pair's uniqueness does not make its projections one orbit.
The separation modulus cannot be normalized to one.

The accepted proof is assembled from two complete alternatives:

* For `Jbar=d-2g+2b-a!=0`, the corrected moving conormal frames and actual
  A4 cotangent determinant prove cotangent surjectivity everywhere on c.
  Full inverse support from a supposed mate supplies exactly one point
  in each fiber over C0. Two finite Nakayama arguments give exact local
  ring equality along c. The actual Cartier conductor in `|2H|` would
  miss c, contradicting its required restriction degree eight. Root
  accepts the [independent conormal/conductor audit](2026-10-12-session-nonendpoint-all-mate-conormal-conductor-independent-audit.md).
* For `Jbar=0`, put `E=g-3b+2a`. Homogeneous coprimality excludes E=0,
  and E=-3delta^2 is the separately excluded ramified-line family.
  Otherwise the actual A4 normalization fiber has length two. Under
  full support every conductor prime meets c only at A4, so its image
  lies in the two-generator neighborhood. This bounds the sum of
  reduced field degrees at every generic conductor point by two.
  Complete low-pole classification and the explicit line uniformizer
  exclude the distinguished line and every split reduced conductor
  algebra. Each remaining reduced algebra is a single field of degree
  at most two. The full unit-nilpotent logarithm forces Q squared to
  descend whenever any Q power does. Purity and the ambient lifting
  sequence make this an actual degree-eight mate, contradicted by its
  e=3 socle Hom space. Root accepts the [Jbar-zero owner proof](2026-10-12-session-jbar-zero-coprime-conductor-phase-bound.md)
  and [independent phase audit](2026-10-12-session-jbar-zero-conductor-phase-independent-audit.md).

Root has read both written audits and reconstructed the local elimination,
finite module propagation, prime degree classification, line valuation over
the nonclosed field k(L), split degree accounting, full logarithm descent,
purity and socle contradiction. The field-degree bound does not bound full
Artinian conductor lengths. Split phase orders are not bounded abstractly;
the split algebras are excluded geometrically in this specific stratum.
No step uses average conductor degree as rank or first-normal roots as
upper bounds on higher contact.

The first independent conormal expansion had a genuine wrong coefficient
in J. That version and failed streams are retained and explicitly
superseded by the corrected polynomial; the accepted theorem uses only
the corrected forms. Root's local conductor check supplies eight exact
identity groups and the separate phase-audit implementation twelve.
These checks support the algebra, while the written proof establishes
the all-parameter and all-mate-degree implications.

## 2. Other newly accepted structural and bounded results

Root accepts the [independent pole/line audit](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet-independent-audit.md).
The exact pole orders 2,3,5 and cancellation-aware basis exhaust all
low-pole sections. The pulled quadric has actual residual degree six,
with partitions `6,2+4,3+3,2+2+2`, including repeated primes. The specified
entire-line rank-one subfamily has an all-power downstairs-frame
derivation obstruction. Its annihilation statement is evaluated at the
generic point of the line, not asserted throughout the surface chart.

Root accepts the [independent residual-factor/genus audit](2026-10-12-session-nonendpoint-residual-factor-and-genus-independent-audit.md).
The two factor hyperplanes are exhaustive. The entire `2+2+2` partition
is excluded, and map degrees and target classes in `2+4` and `3+3` are
restricted without discarding repeated primes. The conic-plus-quartic
case reduces to eight necessary one-parameter families. Off the factor
hyperplanes the actual integral residual has arithmetic genus one,
including its singular affine cases, maps birationally to the target
residual of arithmetic genus three, and has exact excess contact length
eight. This equality supplies no upper bound at an individual point.

Root accepts the [independent target-fiber audit](2026-10-12-session-nonendpoint-target-fiber-independent-proof-audit.md).
The complete projective source boundary, denominator-free finite fibers,
regular-chart quadratic/cubic system, rank degeneracies, target-one split
and target-infinity degree drops are all retained within their stated
scopes. Every equal-lift projection `a=b=g=d` is base-point free and has
an actual off-c inverse point for every nonzero delta, hence no mate in
any degree. Additional exact bounded exclusions are accepted as stated
in the audit. They are not an exhaustion of the general fiber incidence.

**PROVED HERE / independently audited:** the whole subfamily
G=Jbar=0 is excluded in every mate degree. Root accepts its
[full-support proof](2026-10-12-session-nonendpoint-GJ-zero-full-support-exclusion.md)
and [independent geometric/certificate audit](2026-10-12-session-nonendpoint-GJ-zero-full-support-independent-audit.md),
saved on October 13. The B=0 equal-lift case is covered above. For B!=0,
actual fibers force one lift parameter and an actual nonzero leading
coefficient. A complete exceptional-fiber argument then forces a
degree-five polynomial's roots into three retained targets, including
A4. All twenty-one multiplicity profiles have polynomial Bezout
identities equal to one. Root has read and reconstructed the complete
cover, including the target-infinity degree boundary and every E=0
fiber. The independent standard-library Fraction checker directly
multiplies all exported certificate vectors rather than regenerating
them: eighty assertions in one lineage, with the earlier parser
collision and both captures preserved. No parameter inverse or
saturation occurs in those twenty-one polynomial unit certificates.

## 3. The entire conic-plus-quartic partition is excluded

**PROVED HERE / independently audited.** The eight necessary families
in the accepted residual reduction exhaust the partition `2+4` under
full inverse support. Root accepts the [two-family Type1 proof](2026-10-12-session-nonendpoint-type1-two-family-exclusion.md)
and its [independent reconstruction](2026-10-12-session-nonendpoint-type1-two-family-independent-audit.md),
and the [six-family Type2/Type3 proof](2026-10-12-session-nonendpoint-type23-six-family-exclusion.md)
and its [separate independent reconstruction](2026-10-12-session-nonendpoint-type23-six-family-independent-audit.md).
Every admissible projection in this entire partition has no mate of
any positive degree.

The smooth intrinsic quartic has total restricted-ideal contact length
four with c. Its smooth target image of class (3,1) has intersection
length ten with C0, so full support requires excess length six. In Type1
the complete linear and cubic exceptional parameter strata provide at
most one finite excess length and none at A4. In Type2/Type3 the complete
finite incidence provides at most two excess lengths; actual third and
fourth target jets give exactly one excess at A4, including every
degree-drop stratum. Thus the required six cannot occur. The nonreduced
Type2 parameter component and its nonunit second jet are retained;
its actual third jet and intrinsic first jet give the correct bound.

Root has read the frozen proofs and both audits and reconstructed the
curve isomorphisms, restricted ideals, full parameter strata and actual
target jet argument. The separate supporting implementations check
thirty and fifty-eight conditions respectively; their development
failures remain preserved. Their counts do not replace the all-parameter
proof or count copies and replays as independent lineages.

## 4. Actual conductor quadric, octic and finite necessary incidence

**PROVED HERE / independently audited.** Root accepts the [actual conductor determinant theorem](2026-10-12-session-nonendpoint-restricted-conductor-determinant.md)
and [independent module/ideal audit](2026-10-12-session-conductor-quadric-module-independent-audit.md).
Every admissible finite birational projection in this normalization
lane has a unique ambient conductor quadric up to scalar. Its pullback
generates the entire actual invertible conductor ideal O_S(-2H), with
all multiplicities. This is not a claim that the downstairs ideal is
principal. The latter has generator degrees (2,3,3), syzygy degrees
(4,4), and is an actual ACM degree-five genus-two curve, including
nonreduced cases.

The direct existence proof is
H0(X,I_X(2))=H0(S,I_S(2H))=k, followed by the quintic hypersurface
lifting sequence. The explicit formula additionally uses the actual CM
resolution and rank-one normalization module. Every admissible center
has rank three on the binary quadrics: the basepoint-free rank-two
pencil is retained and excluded by its forced linear presentation
determinant factor. All ten rank-three pivot charts are covered. The
universal five-by-five determinant has no pivot denominator.

Its restriction to c is a nonzero homogeneous binary octic Fdet(P,Q),
where p=P/Q=1-z, p=0 is A4 and Q=0 is target infinity. This remains a
degree-eight form when its affine degree drops. Let H be the complete
homogeneous gcd of the transformed corrected conormal cubics and let
epsilon be one for Jbar=0 and zero otherwise. A mate necessarily satisfies

    Fdet divides (H P^epsilon)^8.

This retains all multiplicity distributions. The exponent eight comes
from the total degree of the actual conductor restriction, not an upper
contact bound deduced from first symbols. The full incidence remains
open, and is not asserted sufficient for support or power descent.

Root has reconstructed the sheaf argument, finite-depth transfer,
irreducible presentation determinant, every center-rank alternative,
actual ideal membership, downstairs resolution and binary support
condition. The explicit determinant/norm scalar comparison uses the
separate captured fifteen-identity source, reused in the independent
audit with that fact disclosed. No fresh model or norm replay is claimed.
On pZ!=0 its normalized quadratic/cubic norm retains every leading
degree drop; vanishing can still represent an allowed doubled c-fiber.
The other target charts keep their separate fiber equations.

The [additional infinity coefficient](2026-10-12-session-nonendpoint-conductor-infinity-coefficient.md)
has a captured standard-library coefficient check. With a=B=0,
Fdet has affine p-degree seven and p^7 coefficient delta^7. Its zero at
target infinity is therefore exactly simple. Combining this with the
accepted geometric bridge excludes every admissible a=B=0 parameter
with Jbar!=0 and sole common conormal root at that endpoint, in every
mate degree. Other roots, Jbar=0 and higher gcd strata remain retained.

## 5. Claims still under independent review

The proposed [entire cubic-pair exclusion](2026-10-12-session-nonendpoint-cubic-pair-contact-reduction.md)
uses the actual degree-seven target contact divisor, an exhaustive
eight-candidate sparse-heptic classification, and a modulus-free source
coefficient identity that no pair of candidates satisfies. Distinct and
doubled cubic factors and homogeneous endpoints are retained. Its owner
evidence assembly is frozen and its fresh independent proof audit is in progress.
No cubic-pair exclusion is accepted here until those reviews finish.

## 6. Current continuation and retained global boundary

The next mathematical target is the complete homogeneous common-root
and actual octic incidence. Continue with actual target fibers, higher
contact or full conductor membership; do not restart the closed coprime,
endpoint or conic-plus-quartic families. Finish the cubic-pair audit.
The integral residual remains open, including its affine singular
cases and required excess length eight. Retain every repeated component,
center, pivot and denominator stratum in the remaining obligations.

Normal quintics, other nonnormal normalization genera, higher minimum
carrier degrees, entirely thick presentations, the retained split-sextic
boundary and distinct common-ancestor incidence remain open. The 308
necessary profiles for `(5,8)` are not realized structures or a degree-pair
exclusion. Neither the all-quartic theorem nor any result here supplies
an upper defining-degree bound, a universal counterexample or an
unrestricted fixed-C0 obstruction.

At this evening resumption the current externally observed HEAD is
`59a7bf73bdd196fa6b03ce9e265c5a1a9edbae58`, title
`2026-10-12 morning limit reached`. The checkout was clean before the
new evening edits. Root did not create that commit. The previous
morning HEAD and the morning status checkpoint are historical snapshots.
The October 13 continuation observes the same HEAD and seven modified
canonical records. Usage-limited workers were authoritatively terminal
before their same handles were resumed after a live ordinary-usage
availability check; no reset credit, purchased credit or model change
was used. The previous goal turn made mathematical progress through
new exact calculations and independent proof audits.
The morning integrity seal remains frozen; a new extension must disclose
changed canonical files separately from the unchanged bound proof data.


---

## Source: 2026-10-12-session-research-status-checkpoint.md

# Research status checkpoint, October 12

Recorded by root at 2026-10-12 15:09 UTC (11:09 EDT), in response to the
user's request for a rundown at the latest pause. This is a current
root-reviewed routing snapshot, not a new full-record seal. Work continues;
the research goal has not been marked complete, blocked or paused.

## Global scope

The universal integral projective-curve STCI problem and the unrestricted
characteristic-zero problem for the literal curve
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. No positive universal theorem,
counterexample, unrestricted two-form presentation or upper bound on
hypothetical defining degrees has been established. No novelty claim is
certified. The new exclusions below concern this fixed curve and its
projective equivalents in characteristic zero, not every rational quartic
or every algebraically closed field.

## Sealed, accepted frontier

1. **PROVED HERE / independently audited:** every integral quartic carrier
   of fixed C0 has no mate in any positive degree. The normal and all
   nonnormal normalization-genus cases are exhausted. The degree-factor
   argument and checked lower-degree exclusions imply that every
   irreducible factor of either defining form has degree at least five.
   See the [all-quartic root acceptance](OCT11_QUARTIC_DEPENDENCIES_AND_DP5_ENDPOINTS.md#source-2026-10-11-session-all-quartic-results-acceptancemd).
2. **PROVED HERE / independently audited:** the entire admissible endpoint
   projection family in the sectional-genus-one quintic A4 normalization
   lane has no mate in any positive degree, for all four lift parameters.
   See the [endpoint root acceptance](#source-2026-10-11-session-quintic-continuation-results-acceptancemd).
   The intrinsic pair is unique, but the nonendpoint projection family
   retains a nonzero separation parameter and is a separate problem.

The latest sealed checkpoint is the
[quintic continuation seal](../validation/2026-10-11-quintic-continuation-seal/result.json),
completed at 2026-10-12 14:22:11 UTC: PASS, 8,387 record checks, 868 local
links and 1,203 bound files. Root freshly recomputed all 1,203 stored
file digests for this rundown: no changed or missing binding was found.
That check certifies the recorded bytes and routing, not mathematical
truth. It reran no mathematical verifier. New October 12 research below
postdates that seal and is not covered by it.

## New independently audited nonendpoint progress

All statements here inherit the accepted actual degree-five A4 pair and
require an admissible center-avoiding projection when interpreted as an
integral quintic normalization. Parameters are `delta!=0,a,b,g,d`.

* **PROVED HERE / independently audited, every mate degree:** let Ph,Jh
  be the corrected homogeneous conormal cubics and put
  `Jbar=d-2g+2b-a`. A hypothetical mate requires
  `Jbar*Res_h(Ph,Jh)=0`. Thus a proper dense open part of this
  five-parameter family is excluded in all mate degrees. The proof
  converts cotangent surjectivity and the necessary single-point fibers
  over C0 into exact local normalization isomorphisms. The actual
  conductor divisor in `|2H|` would then miss the lifted curve, contrary
  to its required restriction degree eight. This is not a first-normal
  bound on higher contact lengths. See the [owner proof](2026-10-12-session-nonendpoint-conormal-cubic-reduction.md)
  and [independent all-mate audit](2026-10-12-session-nonendpoint-all-mate-conormal-conductor-independent-audit.md).
* **PROVED HERE / independently audited, every mate degree:** the
  entire-line rank-one subfamily has an actual downstairs-frame
  differential obstruction to every positive power of Q. See the
  [pole and line-jet audit](2026-10-12-session-nonendpoint-pole-filtration-and-line-jet-independent-audit.md).
* **PROVED HERE / independently audited, structural reductions:** the
  residual Weil divisor has degree partitions `6,2+4,3+3,2+2+2`.
  The full `2+2+2` partition is excluded. The conic-plus-quartic case
  reduces to eight necessary one-parameter families, retaining every
  nonzero delta. Off the two factor hyperplanes the actual integral
  residual has arithmetic genus one, maps birationally to a target
  residual of arithmetic genus three, and needs exactly eight additional
  scheme lengths of contact beyond its intrinsic intersection with c.
  No upper bound on those lengths is asserted. See the
  [residual-factor/genus audit](2026-10-12-session-nonendpoint-residual-factor-and-genus-independent-audit.md).
* **PROVED HERE / independently audited, every mate degree:** every
  equal-lift projection `a=b=g=d` is excluded for all `delta!=0`.
  Complete source-boundary and exceptional-target equations also give
  additional exact bounded exclusions; they do not exhaust the family.
  See the [target-fiber proof audit](2026-10-12-session-nonendpoint-target-fiber-independent-proof-audit.md).

Root has read the new written audits and the corresponding proof scopes.
The corrected conormal coefficient identities are supported by root's
seven-condition M2 checker and an independent twelve-check implementation;
the target-fiber checker has seventeen identities and its independent
gap checker eleven. These support the displayed algebra. The written
geometric arguments provide the scope of each theorem. Failed mathematical
expansions, protected-name failures and checker-operation failures are
preserved separately from successful runs. Replays are not independent
mathematical sources.

## Work in progress, not accepted as completed theorems

* **COMPUTATIONALLY CERTIFIED / geometric audit pending:** for
  `G=g-3b+2a=0`, `Jbar=0`, `B=b-a!=0`, the owner reports exact polynomial
  Bezout certificates for all 21 degree-five root-multiplicity profiles
  supported at target p=0 and the two roots of `p^2-6p+6`. Each coefficient
  ideal generates one even before saturation. A new proof/evidence record
  and a separate audit of the complete root cover, forced parameter
  values, degree drops and every exceptional fiber are being completed.
  The already accepted B=0 equal-lift result does not substitute for this
  audit. See the [new supporting source](../computations/verify_session_nonendpoint_GJ_zero_profile_exclusion_2026_10_12.m2).
* **PROPOSED STRUCTURAL PROOF / audit pending:** a conductor-geometry
  argument proposes excluding the remaining `Jbar=0` coprime-cubic stratum
  in all degrees, which would sharpen the necessary locus to
  `Res_h(Ph,Jh)=0`. Its local fiber-length, global conductor-prime
  accounting and reduction to a square power require independent
  reconstruction. It is not part of the accepted frontier above.
* **ACTIVE COMPUTATION / incomplete:** the eight conic-plus-quartic
  families are being tested with actual contact and conductor data.
  Some necessary finite delta exceptions have been derived in one type;
  no whole eight-family exclusion is accepted yet.

## Continuation priorities and open boundary

First complete the two new audits and preserve their full failed/successful
execution histories. Then resolve the retained common-root and A4
cotangent loci using the denominator-free target-fiber equations, the
eight conic families, the cubic-pair cases and actual higher contact or
conductor membership. Do not infer later contact bounds from tangent data,
nor infer conductor rank two from total degrees ten and five. Split
root-of-unity phases and nonreduced generic conductor algebras require
actual algebra, even when a particular stratum eventually excludes them.

Normal quintics, other nonnormal quintic normalization genera, higher
minimum carrier degrees, entirely thick presentations, the retained
split-sextic boundary and distinct common-ancestor incidence remain open.
The 308 necessary numerical profiles for `(5,8)` are not 308 realized
geometries and are not a degree-pair exclusion. Closing this genus-one
quintic lane would still leave the unrestricted fixed-C0 and universal
questions unresolved.

At this observation HEAD is `0adab2bd188351a77d961d7f2251c21545aaebcc` on
`research/ultra-resume-2026-10-06`. New work is retained in the working
tree. Root has made no Git mutation for this rundown. The older canonical
files still describe the sealed checkpoint; this note explicitly records
the post-seal extension pending the next consolidated acceptance and seal.


---

## Source: 2026-10-12-session-sparse-heptic-cubic-pair-classification.md

# Sparse heptic classification for a pair of quadric cubics

Date: 2026-10-12. Characteristic zero throughout.

Status: **PROVED HERE, by exact polynomial ideal computations and the
elementary pair contradictions below; independent acceptance of its use in
the full geometric argument remains the responsibility of the parent
assembly/audit.** This companion record does not assert an unrestricted
quintic or STCI theorem. It treats exactly the contact configuration stated
in section 1, including all homogeneous endpoint cases.

## 1. Exact scope and endpoint coordinates

On the Segre quadric, a divisor of class `(2,1)` has an equation

    P2(x) + z Q2(x) = 0,

where `P2,Q2` are homogeneous binary quadratics in the first Segre
coordinate. Restricting to `C0(z)=[1,z,z^3,z^4]` gives a binary heptic

    H(z)=h0+h1 z+h3 z^3+h4 z^4+h6 z^6+h7 z^7.

Thus the coefficients of `z^2,z^5` vanish. This restriction is injective:
the six displayed monomials are distinct. An irreducible such divisor is a
smooth rational cubic. Indeed, if the binary quadratics are coprime, the
divisor is the graph of the morphism from their binary coordinate line to
the other ruling. If they have a common binary root, its entire ruling
fiber is a component; conversely every reducible equation linear in the
second ruling has such a common factor. Hence the **binary** resultant of
`P2,Q2`, including a common root at infinity, is the precise irreducibility
filter.

Assume the contact at `z=1` has order exactly one and the remaining six
intersection lengths are supported at at most two points different from
`1`. If there are two distinct points, the profiles, up to swapping their
labels, are `(N,P)=(1,5),(2,4),(3,3)`. There is also the single-point
profile `(6)`.

Use

    u=1/(1-alpha), v=1/(1-beta),
    L_u(Z,W)=u Z+(1-u) W.

These coordinates cover **all** target points except `z=1`. In particular
`u=0` means `alpha=infinity` and `u=1` means `alpha=0`. Their roots are
distinct precisely when `u-v!=0`. The homogeneous heptic is, up to scalar,

    (Z-W) L_u(Z,W)^N L_v(Z,W)^P.

Its value after division by `Z-W` at `(1,1)` is `1`, so the prescribed root
at `1` is always simple. No endpoint is discarded by a finite affine
polynomial-degree convention.

For the source contact coordinates in the parent calculation, the two
roots are `r=delta u, delta v`. A cubic component written
`t+m r+n=0` consequently has

    m=delta s, n=-delta^2 p, s=u+v, p=uv.

## 2. Complete exact classification

Let `I_N` be the ideal generated by the two missing coefficients of
`(z-1)(u z+1-u)^N(v z+1-v)^(6-N)`. Let `R_N` be the determinant of the
four-by-four Sylvester matrix for the binary quadratics

    P2(X,Y)=h6 X^2+h3 X Y+h0 Y^2,
    Q2(X,Y)=h7 X^2+h4 X Y+h1 Y^2.

The checker computes the exact ideal

    I_good = I_N : ((u-v) R_N)^infinity

and verifies equality with the following displayed ideals over `QQ`.
It also verifies `I_good+(u v(u-1)(v-1))=(1)`. Thus every accepted root is
finite and nonzero in the target coordinate, but that conclusion is
obtained **after retaining and filtering** zero and infinity.

| Profile | Complete ideal for the ordered pair `(u,v)` | Ordered solutions |
| --- | --- | --- |
| `(1,5)` | `21v^2-21v+5=0`, `u=11v-5` | 2 |
| `(2,4)` | `63v^4-126v^3+111v^2-48v+8=0`, `u=42v^3-63v^2+42v-10` | 4 |
| `(3,3)` | `7v^4-14v^3+12v^2-5v+1=0`, `u=1-v` | 4 |

Every displayed ideal is reduced. The first two profiles have their root
labels fixed by their unequal multiplicities. The last profile identifies
the two exchanged pairs, leaving two cubics. Hence there are precisely
**eight** irreducible cubics with this contact pattern.

For the single-point profile, the exact ideal of the two missing
coefficients is `(u(u-1))`. These are the sixfold contact at infinity and
the sixfold contact at zero. Both have zero binary resultant. Saturating
by that resultant gives the unit ideal, so **no irreducible cubic has
this single-point sixfold residual contact**.

These equalities prove exhaustion over every algebraically closed field
of characteristic zero: scalar extension of the exact rational ideal
identities preserves them, and saturation removes exactly the loci where
the two roots coincide or the cubic is reducible. The surviving zero-
dimensional ideals are disjoint from the saturated denominator locus.
This is not a generic resultant degree estimate.

For use in pair matching, put `h=s-1`. The same candidates have the much
smaller invariant description:

| Type | Contact profile | Conditions on `(h,p)` | Cubics |
| --- | --- | --- | --- |
| A | `(1,5)` | `h^2=12/7`, `p=8/21+h/2` | 2 |
| B | `(2,4)` | `63h^4-30h^2-1=0`, `p=5/12+h/2-h^2/4` | 4 |
| C | `(3,3)` | `h=0`, `7p^2-5p+1=0` | 2 |

The checker verifies all invariant identities modulo the full candidate
ideals. Their counts agree with the ordered classifications after the
single exchange symmetry in type C. In type B the two roots remain
distinct because `(u-v)^2=2(h^2-1/3)` and the defining quartic does not
vanish when `h^2=1/3`. The analogous distinctness tests are immediate in
types A and C.

## 3. No pair obeys the necessary coefficient identity

The parent residual-factor calculation supplies the necessary identity

    E=s1*s2-3*s1*p2-3*s2*p1+p1+p2+6*p1*p2-1/3=0.       (1)

This section proves that none of the eight candidates can form a pair
satisfying (1). There is no restriction that the two cubic components be
different: the calculation includes a doubled cubic and common contact
points across the two components.

After substituting the invariant conditions, the six pair types give:

| Pair | Reduced value of `E` |
| --- | --- |
| A,A | `2/147-h1*h2/2` |
| A,B | `(1-3h2^2-21h1*h2)/42` |
| A,C | `(2/7)(p2-1/3)` |
| B,B | `((1-3h1^2)(1-3h2^2)-12h1*h2)/24` |
| B,C | `(3h1^2-1)(1-3p2)/6` |
| C,C | `(2/3)(1-3p1)(1-3p2)` |

All six identities are verified as literal polynomial remainders. They
also give elementary contradictions:

* A,A would require `h1*h2=4/147`, whose square cannot equal `(12/7)^2`.
* A,C requires `p2=1/3`, whereas `7p2^2-5p2+1` then equals `1/9`.
* B,C requires either `h1^2=1/3` or `p2=1/3`. The respective defining
  polynomials then equal `-4` and `1/9`.
* C,C likewise requires one of its products to be `1/3`, which is excluded.
* A,B, on squaring the necessary equality and writing `x=h2^2`, requires
  `9x^2-762x+1=0`. Combined with `63x^2-30x-1=0`, this gives `x=1/663`,
  which does not satisfy the latter polynomial.
* B,B, after squaring and reducing by the two quartic conditions, requires
  `2-3(x+y)-216xy=0`, where `x=h1^2,y=h2^2` are roots of
  `63X^2-30X-1`. If `x!=y`, the left side equals `4`. If `x=y`, it forces
  `x=-5/381`, which does not satisfy that quadratic.

In addition, for each of the six unordered type pairs the checker writes
an explicit polynomial Bezout certificate for the generators of the two
candidate ideals together with `E`, and **multiplies the certificate
matrix by the generator matrix to obtain the literal matrix `(1)`**.
The certificate coefficients are preserved in the raw stdout. This is
stronger than reporting a successful generic rank or a unit Gröbner basis
without checking membership in the original generators.

The mathematical consequence of this companion calculation is precisely:
**the stated sparse contact patterns cannot occur in a residual cubic
pair satisfying (1)**. The parent proof must still justify the contact
order at the `A4` image, its support restriction, and (1) for the actual
projection. No first-normal symbol is used here to bound a later contact
length.

## 4. Exact evidence and failure history

The standalone checker is
[verify_session_sparse_heptic_cubic_pairs_2026_10_12.m2](../computations/verify_session_sparse_heptic_cubic_pairs_2026_10_12.m2),
SHA-256 `1e18cdedcd5ed9a4181f6baf21ff5d959ed7e2a9dfcedaf522e546716809fdeb`.

The captured execution record is
[execution-record.json](../validation/2026-10-12-sparse-heptic-cubic-pair-classification/execution-record.json),
SHA-256 `30ce05de9892a50aa56331f35d9717c411de01b4f346c785c7c0e6c201a0958d`.
The final checker ran with `/opt/homebrew/bin/M2 --script`, Macaulay2
`1.26.06`, exited zero, and produced empty stderr. It executed 30 assertion
invocations in 10 substantive blocks: the three distinct-root
classifications, the single-root exclusion, and the six pair identities
with original-generator certificates. The eleventh PASS line is its
terminal summary, not another mathematical check.

The evidence directory preserves all seven development sources and their
stdout/stderr. Two setup/checker attempts failed: the first used protected
Macaulay2 name `hh`; the second extracted coefficients in an unsuitable
multivariable ring and then had no applicable `resultant` method for its
incorrect zeros. Neither is a mathematical counterexample or a successful
check. Four subsequent scratch scripts succeeded before the final source.
Their captured runs are explicit replays after their initial tool runs,
not independent checker lineages. The formal source uses a nested
coefficient ring and its correct endpoint and irreducibility tests.

No canonical record, previously frozen note, Git state, or memory file was
modified by this companion task.
