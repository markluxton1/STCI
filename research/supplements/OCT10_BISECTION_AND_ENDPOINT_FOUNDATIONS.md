# Historical mathematical investigations

Full original mathematical text follows. Preserve source-level evidence status, counterexamples, corrections and unresolved boundaries; no independent re-audit or result promotion.

---

## Source: 2026-10-10-latest-pause-rundown.md

# Latest-pause rundown and live audit supplement

Snapshot: 2026-10-10, approximately 13:35 UTC. This is a status record,
not a replacement for the canonical audited state or a new integrity seal.
It distinguishes the saved October 9 frontier from the October 10 audit
results that have just arrived. No novelty claim is made.

## Global scope

The universal integral projective-curve STCI problem remains **OPEN in
this repository**. The unrestricted characteristic-zero problem for
`C0=[s^4:s^3t:st^3:t^4]` also remains **OPEN**. The recent work concerns
integral quartic carriers and does not force an arbitrary presentation to
have a quartic member. Higher minimum carrier degrees and entirely-thick
presentations remain outside the quartic exclusions.

## Established quartic frontier

The [canonical audited state](../AUDITED_STATE_2026-10-07.md) and
[October 9 acceptance](2026-10-09-session-results-acceptance.md) retain
the independently accepted results:

- Every normal integral quartic carrier for fixed `C0` is excluded in
  characteristic zero, in every mate degree.
- Every sectional-genus-zero normalization, and every smooth
  normalization, is excluded in every mate degree. The complete
  degree-four minimal-degree classification includes both smooth scrolls,
  the Veronese surface, and the rational-normal-quartic cone.
- Every nonnormal integral quartic containing any smooth rational
  degree-four curve has rational normalization, without a mate hypothesis.
- A genus-one normalization is an ADE degree-four del Pezzo surface.
  Under a mate, the complete exceptional type is `4A1` or `A3+2A1`,
  the mate degree is even, and the actual linear equivalence is `2c~2H`.

## Genus one: complete argument, final acceptance integration pending

The [remaining-partitions proof](2026-10-09-session-ribbon-repeated-partitions-complete.md)
covers `[4]`, `[3,1]`, and `[2,2]`, including coefficient and direction
boundaries. The earlier squarefree and `[2,1,1]` arguments complete the
five partitions of the four conductor-contact zeros. The proof retains
the literal omitted-middle projection center and the entire conductor.
It excludes mates in every degree, rather than merely a bounded range.

The [October 10 interface audit](2026-10-10-session-genus-one-interface-independent-audit.md)
has finished and accepts the whole implication chain through squarefree
and `[2,1,1]`: full inverse support, actual Cartier double, singular ADE
points, complete ribbon net, ambient lift, and fixed projection coordinates.
It states that acceptance of the remaining-partition proofs closes every
genus-one quartic carrier, with no further interface hypothesis.

The separate remaining-partition auditor has reported a successful new
Macaulay2 countercheck: **29 exact conditions**, terminal exit zero. Its
[saved result](../validation/2026-10-10-repeated-partitions-independent-audit/result.json)
records universal net/support ideal equality for `[3,1]` and `[2,2]`, an
exhaustive direction chart, and an independent conductor section proving
the all-powers obstruction. At this snapshot its written audit and final
provenance record are being saved. Thus the complete exclusion has passed
the reported independent mathematical checks; canonical reconciliation
and root acceptance of the final saved audit are still outstanding.

A real evidence-attribution error was found in the old `[2,1,1]` note:
its cited current Python checker lacked some claimed checks. The written
proof passed the separate audit. A new M2 companion supplied **42 exact
identities over QQ**, with terminal PASS, and
[both execution attempts](../validation/2026-10-10-genus-one-interfaces/execution-record.json)
are retained. Historical checker passes must not be attributed to the
previously missing identities.

## Genus two: structural progress, no mate exclusion

The [adjoint model](2026-10-09-session-genus-two-adjoint-conic-model.md)
has independently accepted core inputs: on the rational minimal resolution,
`L^2=4`, `K.L=-2`, and `f=K+L` is a basepoint-free rational pencil with
`f^2=0` and `L.f=2`. Its exceptional primes are vertical `(-2)` curves
and at most two disjoint horizontal `(-3)` sections. The separate
[mate-strata audit](2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md)
retains BOTH possibilities

    (lambda,q)=(0,4):  c#^2=0, f.c#=2;
    (lambda,q)=(1,3):  c#^2=1, f.c#=1.

The claim that only `q=4` survives was corrected and must not be reused.
The newly saved [marking and section pause audit](2026-10-10-session-genus-two-marking-and-section-pause-audit.md)
accepts the owner's remaining ruled/plane marking sections, while retaining
the exceptional-graph obligations. In particular, internal chain
attachments and satellite blowups invalidate proposed simple arm-budget
or star assumptions. Conditional small-graph bounds do not constitute a
geometric exclusion until their hypotheses are proved. Both mate strata
remain open.

The new [entire-conductor independent audit](2026-10-10-session-genus-two-entire-conductor-independent-audit.md)
accepts a substantial additional reduction without a mate: all singularities
of the normalization are rational, the actual downstairs conductor scheme
is a reduced line with no embedded or isolated points, and the entire
upstairs conductor is a finite flat double cover with algebra

    O_P1 direct-sum O_P1(-2),  w^2=delta,  delta in H0(O_P1(4)).

This retains singular and nonreduced covers, including `delta=0`.
It does not make the upstairs conductor Cartier. The quartic has generic
order exactly two along the line. Turning the conductor/adjoint model into
a uniform mate obstruction is still required. An ambient line-blowup lift
has a new proposed argument but is not certified by this snapshot.

## Other open routes and continuation record

The principal MF6 finite candidate locus is necessary, not an actual
classified carrier list. Its at-most-630 bound does not exclude those
parameters. The 22 second endpoint-family points of degrees `3,4,15`
retain every lower lift line. Remaining common-quartic-ancestor strata,
early `e=2` defects, higher carrier degrees, entirely-thick presentations,
and the totally ramified split-sextic boundary remain open.

The historical [October 9 seal](../validation/2026-10-09-late-continuation-seal/README.md)
records **97 distinct sources with latest PASS evidence / 110 explicitly
indexed executions**, plus **2006 integrity checks / 313 scoped local
links**. These counts apply to that frozen record; the October 10 results
have not been silently added, and the seal does not certify later edits.

Live Git HEAD was inspected as `406d63db72000a3951497a0ba2a8fbfbc13e8ead`,
commit title `2026-10-09 afternoon limit reached`. The morning HEAD in the
older acceptance is historical. New research files are present as
untracked files; this status pass performed no Git mutation.

The old temporary CAS Python currently lacks SymPy. The new independent
checks use the verified Macaulay2 1.26.06 runtime. This current runtime
failure does not invalidate preserved historical execution evidence.

Immediate continuation: finish and reconcile the full genus-one audit;
then pursue the genus-two conductor/adjoint model while preserving both
mate strata and all nonreduced conductor cases. Even full exclusion of
every quartic carrier would leave the unrestricted problem open.


---

## Source: 2026-10-10-session-bisection-primary-descent-sources.md

# Primary-source verification for the bisection descent audit

Date: 2026-10-10. Auditor: `bisection_full_audit/primary_descent_sources`.
Status: **PRIMARY SOURCES VERIFIED; reduced-surface scope guard supplied**.
No canonical frontier file is changed here.

## Kollár: degree-zero line-bundle descent

Source: [Chapter 2, Canonical Models](https://web.math.princeton.edu/~kollar/book/chap2.pdf),
June 1, 2010 draft. Proposition 76(1) is on printed page 35 (PDF page 35,
zero-based page 34); its proof is on printed page 36.

The hypotheses are a rational surface singularity, a proper log minimal
resolution, and a line bundle having degree zero on **every** exceptional
prime. The conclusion is that its direct image is locally free of rank
one and that the natural pullback map recovers the original line bundle.
No Gorenstein or prior Q-Cartier hypothesis is imposed. The proof uses
vanishing of first cohomology on every exceptional cycle, degrees on its
reduction, and formal functions. Section 3 allows normal excellent
surfaces; the characteristic-zero projective setting is covered.

Application guard: rationality of the target singularities and degree
zero on all exceptional primes must be established separately. For the
accepted resolution with rational exceptional (-2)- and (-3)-curves,
adjunction gives nonnegative canonical intersection, as required for
minimality with zero boundary.

## Craighero--Gattazzo: the literal degree-(4,4) exclusion

Source: [Craighero--Gattazzo, 1986](https://www.numdam.org/item/RSMUP_1986__76__177_0.pdf),
Rendiconti del Seminario Matematico della Università di Padova 76,
177--200. Printed pages 177--178 impose an algebraically closed field
of characteristic different from 2 and 3. Proposition 4 is on printed
page 187 (PDF page 12, zero-based page 11). Its displayed equation,
checked visually, is the intersection-cycle equation `F.G=4 C0` for
`C0=[s^4:s^3t:s t^3:t^4]`. The paper's convention makes surfaces reduced.
This is a degree-(4,4) exclusion, not an unrestricted STCI theorem.

**Scope repair for the descended quartic (proved here).** Suppose the
integral quartic `X` and a degree-four form `G` have intersection support
exactly `C0`. Every irreducible factor of `G` cuts a nonempty curve on
`X`, so it contains `C0`. No factor is linear. Any reducible or nonreduced
`G` therefore consists of two degree-two factors, both proportional to
the unique quadric `q`. But `q` cannot be a mate: on `q`, the quartic
carrier cuts class `(4,4)`, whereas `C0` has class `(1,3)`. Consequently
`G` is integral and reduced, and Proposition 4 applies.

## Observation record

Both PDFs were opened and their relevant searchable text inspected
through the browsing tool. Its screenshot output did not expose an
image through this execution wrapper. The CG PDF was therefore fetched
read-only to `/private/tmp/stci-cg1986-source-audit.pdf` and page 12
rendered with `pdftoppm`; the equation and curve coordinates were
visually checked in `/private/tmp/stci-cg1986-p187.png`. These temporary
paths are observations, not durable dependencies of the mathematical
argument. The initial restricted-network fetch failed to resolve the
host; the authorized read-only fetch succeeded. No failure is hidden
and no failed source retrieval is treated as mathematical evidence.


---

## Source: 2026-10-10-session-bisection-ribbon-conormal-microaudit.md

# Bisection ribbon and ambient conormal microaudit

Date: 2026-10-10. Auditor: `bisection_full_audit/primary_descent_sources`.
Verdict: **ACCEPT** Sections 2--4 of the
[full independent bisection audit](2026-10-10-session-genus-two-bisection-full-independent-audit.md).
Input SHA256:
`5aa6eeedb31ff2fe316b706c3c0e86ff78d9beca01c9f92dfa5d7fafcc283133`.
This hash was checked directly after reading the source. The earlier
primary-source audit is unchanged.

## Exact hypotheses checked

Work over an algebraically closed field of characteristic zero. The
embedded reduction is the literal smooth rational curve
`C0=[s^4:s^3t:s t^3:t^4]`. The normal integral projective surface S is
Cohen--Macaulay, with `chi(O_S(mH))=1+2m^2+m`. Its actual finite
normalization morphism maps a smooth embedded `c_S` isomorphically to C0
and is an isomorphism away from the accepted conductor line Gamma.
There is an actual Cartier section Q with entire divisor `2c_S` and
`2c_S~2H`. Numerical equivalence or generic multiplicity alone would
not supply this last input.

## Purity and the global nilideal

The Cartier quotient `R=V(Q)` of the CM surface is pure CM of dimension
one. At the generic point of c_S the normal surface is a DVR, so R has
length two and its nilideal J has generic rank one with generic square
zero. The coherent image `J^2` inside `O_R` is supported at finitely many
points. Purity forbids such a nonzero subsheaf, so `J^2=0` everywhere.
Thus J is an `O_c_S`-module. Any torsion in that module would again be a
finite-support subsheaf of `O_R`, hence zero. Smoothness of c_S makes
this rank-one torsion-free module a line bundle.

The Cartier sequence gives `chi(O_R)=1-7=-6`. The reduction sequence
then gives `chi(J)=-7`, hence `J=O_P1(-8)`. No Gorenstein or
Q-Gorenstein property of S is used.

## Normal bundle and the actual ambient map

I checked both displayed derivative coefficient lists independently.
They force ten coefficients to vanish immediately, and the remaining
two satisfy a matrix of determinant eight. Consequently
`H0(N_C0/P3^*(6))=0`. Together with `deg(N)=14` and splitting on P1,
this yields `N=O(7) direct_sum O(7)`, so
`Hom(N^*,O(-8))=0`.

The morphism `R->P3` induces `I_C0->J`. Its square maps into `J^2=0`,
and the reduction is the given closed embedding, so the induced map
`I_C0/I_C0^2 -> J` is globally `O_C0`-linear. Formation of this map
does **not** require an immersion over Gamma. On the dense complement
of Gamma, normalization is an isomorphism and R is a closed subscheme
of P3. There `I_C0` generates the nonzero nilideal J. The global map
is therefore generically surjective and nonzero, contradicting the
displayed Hom vanishing. I found no gap in this interface.

## Scope and reusable consequence

This accepts the exclusion of the entire genus-two bisection mate lane
once its independently established Cartier equivalence is supplied.
The ribbon argument itself proves the stronger conditional statement:
**any** genus-two normalization in this fixed embedding admitting
`2c_S~2H` is impossible, regardless of which lane supplies that input.

More generally, a rational ribbon R with nilideal
`O(-p_a(R)-1)` and a morphism generically closed onto an embedded C in
P3 requires `p_a(R)<=max{a,b}-1`, where `N_C/P3=O(a)+O(b)`.
Here it would require `7<=6`.

The separate `lambda=1` section lane has not thereby been excluded:
its actual order-two Cartier compression is not an accepted input.
Higher-degree carriers, the unrestricted C0 question, and the universal
STCI problem remain open. No canonical frontier file is edited here.


---

## Source: 2026-10-10-session-continuation-results-acceptance.md

# October 10 resumed continuation: accepted results and exact frontier

The universal projective-curve STCI question and the unrestricted
characteristic-zero question for
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. This acceptance extends the
[earlier October 10 acceptance](2026-10-10-session-results-acceptance.md),
whose proof and evidence bytes are preserved. No novelty claim is made
without the separate literature assessment.

All new mate exclusions here concern the fixed monomial curve and its
projective equivalents over every algebraically closed field of
characteristic zero. An arbitrary smooth rational quartic embedding is
not silently substituted. The field, carrier degree, entire conductor,
and unresolved higher-degree scope are essential.

## 1. The complete genus-two bisection lane is excluded

**PROVED HERE / independently accepted.** An integral quartic carrier
of fixed C0 whose finite normalization has sectional genus two admits
no mate in the `lambda=0` stratum, in any positive mate degree.
The bisection, ordinary bisecant and tangent boundaries are all covered.

Root accepts the full
[bisection independent audit](2026-10-10-session-genus-two-bisection-full-independent-audit.md)
after reading its proof and independently reconstructing both its
Cartier compression and its global ribbon contradiction. The argument
uses the following complete chain, rather than a bounded root-of-unity
or exceptional-graph search.

1. The accepted mate identity gives a smooth lift `c` on the rational
   resolution M with `c^2=0`, `K_M.c=-2`, and `f.c=2` for the connected
   adjoint pencil `f=K_M+L`. Its actual correction Z is effective,
   rational and exceptional, supported on vertical `(-2)` curves.
2. The complete `|c|` is a second connected rational pencil. Its product
   with `|f|` has degree two onto `P1 x P1`. The normal Stein cover W
   is finite flat, with branch class `(2,2)`, and is a degree-four ADE
   del Pezzo. The resolution M is obtained from its crepant resolution
   V by exactly four point blowups, allowing all infinitely near and
   intersection centers.
3. With R the actual integral relative canonical divisor, the
   [second-pencil audit](2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md)
   proves an equality of actual rational divisors

       Z+R=(1/2) sum_t k_t F_t,   sum_t k_t=4.

   Here F_t is the entire fiber with all multiplicities and k_t counts
   centers. Thus `2Z` is integral and exceptional. The accepted
   numerical-to-linear lemma on M upgrades this to the actual Weil
   equivalence `2c_S~2H` on the finite normalization S. Consequently
   `2c_S` is an effective Cartier divisor, cut by a genuine quadratic
   section Q on S. This section is not assumed ambient.
4. Normality makes S Cohen--Macaulay. Its Cartier double curve is
   therefore pure CM, with smooth reduction `c_S~=C0` and generic
   length two. Its nilradical J has square zero: J squared is
   generically zero, hence would be a finite-support subsheaf of the
   pure CM curve. The same purity makes J torsion-free of rank one
   on the smooth reduction, so J is a line bundle.
5. The accepted normalization/conductor sequence, equivalently
   rational-resolution Riemann--Roch, gives

       chi(O_S(mH))=2m^2+m+1  for every integer m.

   The exact Cartier sequence gives `chi(O_(2c_S))=1-7=-6`.
   Since `chi(O_c)=1`, it follows that `J=O_P1(-8)`. This step does
   not require a Cartier canonical divisor on S.
6. The actual morphism `2c_S -> S -> X -> P3` induces a global map
   `I_C0/I_C0^2 -> J`: the ambient ideal pulls into J and its square
   maps to zero. Off the conductor line, normalization is an
   isomorphism, so the actual double curve is locally a closed
   subscheme of P3. The map is generically surjective and nonzero.
7. The already known repository P-009 gives
   `N_C0/P3^*=O_P1(-7) direct-sum O_P1(-7)`. Root independently
   reconstructed the derivative coefficient calculation; the
   [new Jacobian audit](2026-10-10-session-quartic-normal-bundle-independent-audit.md)
   supplies two cubic kernel columns independent at every point,
   including both endpoints. But

       Hom(O(-7) direct-sum O(-7), O(-8))=H0(O(-1))^2=0,

   contradicting the required nonzero global map.

The global double-curve lemma in steps 4--7 applies whenever a
genus-two normalization with these exact Euler characteristics has an
actual Cartier `2c_S~2H` supported on the unique embedded lift. It is
not confined to smooth normalization points. It also excludes a
section-stratum candidate if an independently established integral
`2Z` supplies that same Cartier equivalence. There is no assertion
that every section correction has this property.

The proof uses a full globally existing ribbon. It does not infer
global pole or higher-multiplicity behavior from tangent data.

## 2. Every nonendpoint trisecant section case is excluded

**PROVED HERE / independently accepted.** Root accepts the
[nonendpoint continuation audit](2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md)
and its separately written
[relative Morse/branch audit](2026-10-10-session-relative-morse-conductor-branches-independent-audit.md)
after reading their complete arguments. They exclude every genus-two
`lambda=1` mate whose actual conductor line meets C0 at three distinct
points. There is no bound on mate degree or exceptional chain length.

The normal ambient model has actual exceptional-section divisor
`D_T` of class `(2,2)` on `P1_Gamma x P1_f`. The accepted no-B theorem
forces a degree-zero horizontal prime B, with `c.B=0`. The proof first
exhausts every decomposition of `D_T` containing its Gamma fiber:
double B, a graph plus a fixed f-fiber, two horizontal fibers with
distinct f-fibers, and two horizontal fibers with a double f-fiber.
Each is excluded by the full inverse-support condition at contacts
away from horizontal contractions, or by actual smoothness of T at
the specified B contact. This includes B having correction coefficient
zero when a second horizontal prime is present.

An integral residual of class `(1,2)` makes B the sole horizontal
prime and forces its correction coefficient to be one. Its two other
curve contacts supply the two branch values of a degree-two map of
P1, so it crosses B at two distinct transverse points. The relative
formal proof preserves the actual conductor branch ideals and gives
only endpoint A-chains, with all lengths allowed. At the single
curve contact the exact correction coefficient is

    a = ((n+1-k)/(n+1)) / (1+1/(n+1)+1/(m+1)) < 1,

for `n>=1`, `m>=0`, `1<=k<=n`. This contradicts the required `a=1`.
Twelve exact symbolic identities independently countercheck the
all-length formulas; the global support and branch arguments supply
their hypotheses. Two protected-name scaffold failures are preserved
with their exact sources and raw streams in the
[execution record](../validation/2026-10-10-genus-two-nonendpoint-trisecant-continuation-audit/execution-record.json).

This result does not use `c.B=0` to conclude that the images on T are
disjoint: vertical ADE chains can separate them on M. It retains all
reducible and nonreduced conductor configurations before excluding them.

## 3. Preserved weaker bisection reductions and superseded survivors

The independently checked four-blowup and
[even-fiber arguments](2026-10-10-session-genus-two-bisection-even-fiber-exclusion.md)
first left only odd partitions `[3,1]` and `[1,1,1,1]`. The older
second-pencil note's retained `[2,1,1]` was superseded by the local
integral-correction argument. The
[quadratic-descent note](2026-10-10-session-genus-two-bisection-quadratic-descent.md)
then forced a reduced split conductor and a root-of-unity ratio of
unbounded order. Its formula has orientation `m^2=rho*delta`.
Those were necessary conditions, not realized surviving carriers.
The accepted ribbon proof now excludes all of them, including every
root-of-unity order, without changing the preserved weaker sources.

## 4. Exact normal-bundle verification and current repository state

The new independent
[Macaulay2 source](../computations/verify_session_quartic_normal_bundle_2026_10_10.m2)
checks eight exact Jacobian, projective rank and coefficient-matrix
conditions over QQ. Root copied its exact source to an isolated cwd
and observed a successful replay with exit code zero. Its source SHA-256
is `e939b142ee32a89c43e08131f8668a7c5c0e73eebdbcfa81c004de951ff5d62a`.
The [root replay manifest](../validation/2026-10-10-normal-bundle-root-replay/execution-manifest.json)
binds command, source copy, raw streams and elapsed time. This is an
additional execution of one original source, not an additional verifier
for its copied bytes. The normal-bundle splitting itself is inherited
P-009, not claimed as a new theorem.

Live inspection after the pause found HEAD
`2ba77d1a1177db9390693066c6b185040766c089`, title
`2026-10-10 afternoon limit reached`, on
`research/ultra-resume-2026-10-06`. The earlier October 10 acceptance's
`406d63...` live label is a historical observation. Root performed no
Git mutation. The new work and canonical routing are working-tree
evidence beyond that snapshot.

The historical **97 distinct latest-PASS sources / 110 indexed
executions** and October 9 integrity seal remain frozen historical
records. New execution histories and integrity checks are recorded
separately. A record seal certifies bytes and links; its check count
does not certify the mathematical quantifiers.

## 5. Remaining frontier at this acceptance

Genus zero, genus one, normal carriers, smooth normalization and
nonrational normalization have their previously accepted full quartic
exclusions. The genus-two bisection lane is now also excluded.

The remaining integral-quartic lane is the genus-two `lambda=1`
section stratum with an endpoint triple-contact trisecant. The
three-distinct-contact case is now excluded. The two endpoint lines
are exchanged by coordinate reversal; their remaining full local
families are under independent audit. Zero coefficients of a present
horizontal prime, vertical ADE chains linking it to the curve, and
doubled-horizontal residual conductor schemes must remain covered
before a complete endpoint exclusion.

Higher minimum carrier degrees, entirely thick presentations, the
22 retained ancestor-family points with all lower lift lines, the
principal at-most-630-point necessary locus, early-defect strata and
the totally ramified split-sextic boundary remain outside this result.
No theorem forcing a quartic carrier has been established.


---

## Source: 2026-10-10-session-endpoint-double-horizontal-normal-coefficient.md

# Endpoint double-horizontal normal coefficient

Date: 2026-10-10. Author: `bisection_weighted_normalization`.
Status: **PROVED HERE / bounded auxiliary observation**. This records a
normality restriction in the endpoint section/trisecant investigation;
it does not itself exclude that entire stratum.

Use the accepted actual normal ADE strict transform T in
Bl_Gamma(P3). At the endpoint trisecant Gamma=(x2,x3), use the affine
blowup chart

    a=x1, y=x2, b=x3/x2, x0=1,
    C0: a=b=r, y=r^3.

The double-horizontal residual case has actual equation

    T=-c1 a^2 b^2
      +y[(b-a)(A+B b+C b^2)+c1 a-a b^2(c2+c3 b)]
      +y^2(c2+c3 b)=0,
    c1!=0.

Its exceptional intersection is 2B0+2F0, where

    B0=(a=y=0),      F0=(b=y=0).

Here B0 is the horizontal section contracted in T->S, and F0 is a
line in the endpoint conic fiber. The letters B,C inside the coefficient
polynomial denote constants, not these curve names.

Along F0 all first partial derivatives of T vanish except possibly

    partial T/partial y = a(c1-A).

Consequently A=c1 would make the entire nonempty affine open of F0
singular on T. A normal surface is regular in codimension one, so the
accepted normality of T excludes this equality. Thus

    A!=c1.

This eliminates a potential radical-alignment exception in the A!=0
contact calculation using the actual global fiber, rather than imposing
a generic coefficient hypothesis.

There is also exact global degree bookkeeping for the first normal
coefficient. Write E for the exceptional divisor of the ambient blowup,
whose product coordinates are (Gamma, plane-pencil). Then

    H|E=O(1,0),       E|E=O(1,-1),
    T|E=O(2,2),      (T-E)|E=O(1,3).

The derivative in the normal direction to E is a section of O(1,3).
Its restrictions to the displayed B0 and F0 are respectively

    h_B=b(A+B b+C b^2),       h_F=a(c1-A).

Their complete degrees are three on B0 and one on F0. Hence, after the
normality restriction A!=c1, the only zero of h_F on the complete F0
is its endpoint contact. This excludes an additional unseen singular
point at the other affine chart of F0. The three zeros of h_B, counted
with multiplicity, must still be treated scheme-theoretically; repeated
zeros do not justify assuming only A1 surface singularities.

Possible contact A3/A5/A7 attachments and the resulting rational
correction cycle are separate obligations of the endpoint local audit.
No torsion-two relation or final section-case exclusion is asserted
merely from these derivative and degree observations.


---

## Source: 2026-10-10-session-endpoint-local-ade-correction-audit.md

# Endpoint triple conductor contact: local ADE and correction audit

Date: 2026-10-10. Author: `trisecant_endpoint_research/local_endpoint_ade`.
Status: **PROVED HERE CONDITIONALLY; parent/global coverage audit pending**.
No canonical record is edited by this note. This is a local statement for
the displayed full equation, not an exhaustion of all quartic carriers.

## 1. Inputs and the precise local statement

Work over an algebraically closed field of characteristic zero. The
ambient blowup and crepant normal ADE conic-model theorem is an input;
this note does not re-prove it. Put

    Gamma={x2=x3=0}, a=x1/x0, y=x2/x0, b=x3/x2.

The literal quartic lifts as `(a,b,y)=(r,r,r^3)`. In the endpoint
triple conductor configuration the full strict-transform equation is

    F = a*b*(u*(b-a)-v*a*b)
        + y*((b-a)*(A+beta*b+gamma*b^2)
              +v*a-a*b^2*(d+e*b))
        + y^2*(d+e*b),                                  (1)

with `u!=0`; the coefficient `v` is the coefficient named `c` in the
parent's formula. The conductor component is `B_T={a=y=0}`. Assume
its strict transform B on the crepant minimal resolution has `B^2=-3`,
and that the strict transform C of the literal curve is disjoint from B.
Assume the S-exceptional fiber containing B has no other horizontal
prime. Its other vertices are precisely the ADE exceptional primes
above singular points of T on B_T.

The mate correction Z is orthogonal to pullback L, so its coefficients
on this graph are uniquely determined by

    Z.E = -C.E,       Z.B = -C.B = 0.                     (2)

The embedded smoothness/uniformizer input gives exactly one transverse
C contact with one exceptional prime, of intersection one. The global
lambda-one reduction requires `z_B=coeff_B(Z)=1` when B is the sole
contributing horizontal prime. Under these inputs (1) instead forces
`z_B<1`, in every parameter case. The cases below preserve all higher
terms of (1).

## 2. Only one singular point on B_T is possible

The restriction to the ambient exceptional surface `y=0` is

    a*b*(u*(b-a)-v*a*b).

After removing B_T, the residual conductor restricted to B_T is
`u*b^2`, globally a binary quadratic on the b-projective line. It has
only the double zero `b=0`; it is nonzero at infinity. At every other
point of B_T the derivative of F in the a direction is nonzero.
Consequently T is smooth there. Thus the entire ADE graph attached to
B comes from the single point `(a,b,y)=(0,0,0)`.

No additional invisible vertical chain is allowed: under the stated
crepant normal-model input, vertical (-2)-curves contract precisely to
ADE singular points of T. This paragraph is where the full global
binary quadratic on B_T is used, rather than its affine germ alone.

## 3. A nonzero A: B attaches an endpoint of an A_n chain

The quadratic part of (1) is

    y*(A*b+(v-A)*a)+d*y^2.

If `A!=0`, it has rank two. Formal splitting in characteristic zero
gives `X*Y=z^(n+1)` for some finite `n>=1`, because the point is ADE.
Here X has linear term `A*b+(v-A)*a+d*y`, and Y has linear term y;
the remaining linear coordinate z parametrizes the Hessian kernel.

Along B_T, X has order one. A smooth branch of `XY=z^(n+1)` for
which X has order one attaches an end of the A_n resolution chain.
Equivalently, its first blowup direction is off the Hessian kernel,
on the corresponding smooth component of the rank-two tangent cone.
This conclusion remains valid if z has higher order on B_T.

Label the chain so B meets E_1. By the uniformizer condition C meets
one E_j transversely with multiplicity one, `1<=j<=n`. If R_n is the
positive A_n Cartan matrix, then

    (R_n^-1)_(1,1)=n/(n+1),
    (R_n^-1)_(1,j)=(n+1-j)/(n+1).

Eliminating the chain coefficients from (2) gives

    z_B = ((n+1-j)/(n+1)) / (3-n/(n+1)) < 1/2.            (3)

In particular this is incompatible with `z_B=1`. No bound on n,
and no assumption that C attaches an end, is used.

## 4. A=0 and v nonzero: the internal A_n position is controlled

This is the case where saying merely "rank-two quadratic part" would
leave a dangerous internal attachment. The actual full equation
controls it. Define power series in b (in fact polynomials)

    P=-u*b-v*b^2,
    Q=v-beta*b-(gamma+d)*b^2-e*b^3,
    R=beta*b^2+gamma*b^3,
    S=d+e*b.

Then exactly, with no omitted term,

    F=P*a^2+Q*a*y+S*y^2+u*b^2*a+R*y.                    (4)

Choose the formal square root `q=sqrt(Q^2-4*P*S)` with `q(0)=v`.
This is a unit. Put `alpha=(Q+q)/2` and `t=P/alpha`; alpha is a
unit. The following linear change in (a,y) has unit determinant q:

    X=alpha*a+S*y,       Y=y+t*a,
    a=(X-S*Y)/q,        y=(alpha*Y-t*X)/q.

The quadratic part of (4) is exactly XY. For

    ell_X=(u*b^2-R*t)/q,
    ell_Y=(R*alpha-u*b^2*S)/q,
    X'=X+ell_Y,         Y'=Y+ell_X,

the entire equation is

    F=X'*Y'-ell_X*ell_Y.                                 (5)

The orders are decisive: `ord_b(ell_X)=2`, with leading coefficient
`u/v`, and `ord_b(ell_Y)>=2`. If ell_Y vanished identically, (5)
would be reducible in the completed local ring, contrary to normal
ADE. Thus for finite `m=ord_b(ell_Y)>=2`, absorbing a unit turns
(5) into `X'*Y'=b^(n+1)`, with `n=m+1>=3`.

Along B_T one has exactly `(X',Y')=(ell_Y,ell_X)`, so the respective
orders are `(n-1,2)`. Along C, `a=b=r,y=r^3` gives `ord_r(X')=1`,
since its linear term is `v*r`; (5) then gives `ord_r(Y')=n`.
Both branches have b as a uniformizer. The standard toric charts of
the A_n resolution therefore show

    B meets E_(n-1),       C meets E_1,

once, away from exceptional crossings. For example, the chart at E_i
has monomials `X'=s^i*t^(i-1)`, `Y'=s^(n+1-i)*t^(n+2-i)`, `b=s*t`;
the nonzero t coordinate gives precisely these valuations.

The inverse Cartan entries are now

    (R_n^-1)_(n-1,n-1)=2*(n-1)/(n+1),
    (R_n^-1)_(n-1,1)=2/(n+1).

Equation (2) consequently forces the exact coefficient

    z_B = [2/(n+1)] / [3-2*(n-1)/(n+1)]
        = 2/(n+5) < 1.                                  (6)

This excludes every internal A_n configuration arising from (1),
including parameter cancellations of arbitrary order. An arbitrary
internal A_n attachment, divorced from (4), has not been excluded.

## 5. A=v=0 and d nonzero: the graph is D4, with distinct outer contacts

The quadratic part is `d*y^2`, and the cubic part in the tangent
plane is `u*a*b*(b-a)`, with three distinct linear factors. A direct
blowup gives the exact resolution graph and contact positions without
discarding the higher terms. In the b-chart put `a=b*z,y=b*w`.
After division by b^2, the equation is

    (d+e*b)*w^2 + u*b*z*(1-z)
      + w*(beta*b*(1-z)+gamma*b^2*(1-z)
           -b^2*z*(d+e*b)).                               (7)

The reduced exceptional line is `b=w=0`, parametrized by z. Its only
singular points are `z=0,1,infinity`. At z=0 the quadratic part is
`d*w^2+u*b*z+beta*b*w`, which is nondegenerate; at z=1 it is
`d*w^2-u*b*(z-1)`, also nondegenerate. The a-chart gives the same
nondegenerate quadratic part at infinity. Resolving these three A1
points produces the D4 graph, with a central (-2)-curve and three
outer (-2)-curves.

B follows z=0,w=0 and meets its A1 exceptional outer arm. C follows
z=1,w=b^2 and meets a different outer arm. At each A1 blowup their
direction is the b-axis; the central component has the z-axis
direction. Thus both contacts are transverse and away from the
central/outer intersections.

For the positive D4 Cartan matrix, an outer diagonal entry of the
inverse is 1, and the entry between distinct outer arms is 1/2.
The B equation in (2) therefore yields

    3*z_B=z_B+1/2,       z_B=1/4.                         (8)

The graph is specifically D4. A numerical D7 example obtained by
allowing arbitrary ADE graphs is not realized by these parameters.

## 6. A=v=d=0 is incompatible with the normal ADE model

In this case every quadratic term vanishes, while the nonzero term
`u*a*b*(b-a)` survives in degree three. The surface has multiplicity
three at the origin. A hypersurface ADE point has multiplicity two,
so this case is incompatible with the structural input.

## 7. Scope and verification

Equations (3), (6), and (8) exhaust the four coefficient cases of
(1) and contradict `z_B=1`. This closes the displayed endpoint
triple-contact configuration, conditional on the global reduction to
(1), the normal crepant conic model, B^2=-3, the absence of other
horizontal primes in this fiber, and the embedded smooth contact
input. It does not establish the full endpoint or lambda-one theorem
until those inputs and coverage are independently audited.

The formal splitting and ADE terminology agree with the primary
reference [Miles Reid, The Du Val singularities](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf),
especially its A_n/D_n equations and resolution graphs. The key
internal attachment computation here is the exact factorization (4)
and (5), not a cited generic-rank argument. The D4 contact calculation
is the explicit blowup (7).

Companion exact identity checker:
[verify_session_endpoint_local_ade_2026_10_10.m2](../computations/verify_session_endpoint_local_ade_2026_10_10.m2).
It verifies polynomial identities, the symbolic A_n Schur complement,
and the D4 inverse-matrix entries. Those algebraic checks supplement
the written resolution/contact proof and do not substitute for it.

Final checker execution: **PASS, 16 exact identities over QQ**, exit
zero, source SHA256
`cbe568f673086ed5f4084aedba3e4075470938c5b0bef223de75f7d65c8337d4`.
The [execution record](../validation/2026-10-10-endpoint-local-ade/execution-record.json)
preserves three failed setup/parser attempts, the preceding passing
execution with mechanically altered print labels, and the final passing
execution. A [separate diagnostic record](../validation/2026-10-10-endpoint-local-ade/diagnostic-record.json)
preserves two exploratory calls, including one failed debug run. None
of these attempts changes the frozen historical 97-source/110-run index.


---

## Source: 2026-10-10-session-genus-one-interface-independent-audit.md

# Independent interface audit for the complete genus-one quartic lane

Date: 2026-10-10. Auditor: `oct10_genus_one_interfaces`.
Status: **PROVED HERE / interfaces accepted**, conditional only on the
separately assigned complete exclusions of contact partitions `[4]`,
`[3,1]`, and `[2,2]`. No canonical file is edited. This is an audit of
the hypotheses and quantifiers linking the accepted component results;
it does not substitute agreement between agents for any component proof.

## 1. Precise proposed conclusion and audit outcome

Work over an algebraically closed field of characteristic zero. Let
`X=V(F)` be an integral quartic surface in `P3` containing

    C0=[U^4:U^3V:UV^3:V^4],

and suppose the normalization sectional genus is one. The proposed
conclusion is that there exists no homogeneous polynomial `G` of any
positive degree satisfying `V(F,G)=C0` set-theoretically.

The interfaces audited below do cover **every** such hypothetical mate.
They impose no bound on its degree, no first-normal-order assumption,
no prior reducedness assumption on a conductor, and no choice of a
displayed toric family. Once the complete `[4]`, `[3,1]`, and `[2,2]`
proofs are independently accepted, together with the already accepted
squarefree and `[2,1,1]` exclusions, the proposed conclusion follows.
There is no additional geometric hypothesis needed between these steps.

The conclusion is confined to this sectional-genus-one normalization
lane for integral quartic carriers of the fixed `C0`. It says nothing
by itself about sectional genus two, higher carrier degrees, a general
smooth rational quartic projection center, positive characteristic, or
the universal projective-curve STCI problem.

## 2. Full inverse support must precede the divisor class relation

The [nonrational-normalization independent proof](2026-10-09-session-nonrational-normalization-independent-audit.md)
and its referenced automatic generic-regularity argument apply to an
integral nonnormal quartic containing any smooth rational degree-four
curve. Sectional genus one implies that the quartic is nonnormal: a
normal quartic has a general smooth plane section of genus three.
Thus those accepted hypotheses apply here.

Generic regularity along `C0` supplies exactly one integral curve `c`
above its generic point under the finite normalization `nu:S->X`.
It is finite birational over `C0`, hence isomorphic to it: on each
affine open its coordinate ring is an integral algebra contained in
the common function field, and the downstairs ring is integrally
closed. A second curve over `C0` would also dominate `C0` under the
finite map and give a second generic inverse point, which is impossible.
The strict transform `c#` on a resolution is likewise isomorphic to
`c`; a proper dominant birational map of integral curves is
quasi-finite, hence finite, and the target is normal.

Additional isolated inverse-image points may exist without a mate.
They cannot be silently removed merely because `c->C0` is an
isomorphism. Under the hypothetical mate, however, `nu*G` is a
nonzero section of the invertible sheaf `O_S(bH)`, where
`b=deg(G)` and `H=nu*O_X(1)`. Its zero support is exactly the full
inverse image of `C0`. On the normal integral surface `S`, a nonzero
Cartier section has a pure curve zero scheme; normal surfaces are
Cohen--Macaulay and quotienting by a nonzerodivisor preserves purity
in dimension one. An isolated point away from `c` would therefore
be impossible. Consequently the full support under a mate is `c`.

Write the resulting Weil divisor as `m c`. Intersection with the ample
Cartier divisor `H` gives

    4b=(bH).H=(m c).H=4m,

so `m=b`, including when `G` has high order along the curve. Thus the
actual input to the lattice step is

    div_S(nu*G)=b c,        b c ~ b H.

This establishes the coefficient and removes the isolated-point issue
before any class, double-curve, or power-descent assertion is made.

## 3. Rationality, ADE reduction, and the actual order-two double

The [accepted rationality proof](2026-10-09-session-nonrational-normalization-independent-audit.md)
needs no mate. Its multiplicity bound `0<=m_i<=a` is proved at every
successive blowup, including infinitely near centers. The ruled-surface
identity contradicts the degree-four rational curve whenever the
normalization is nonrational. It applies to this lane and gives a
rational normalization.

The [independent genus-one ADE proof](2026-10-09-session-rational-genus-one-ADE-independent-audit.md)
then applies to its minimal resolution `sigma:M->S`, with
`L=sigma*H`. It proves the actual linear equivalences `K_M~-L` and
`K_S~-H`, and a compatible crepant equality, before invoking the
Du Val criterion. The intermediate effective adjoint divisor is
exceptional and vanishes by negative definiteness; the argument
does not assume rational singularities or Gorensteinness prematurely.
It follows that `M` is weak del Pezzo of degree four and `S` is a
Gorenstein ADE del Pezzo surface with ample anticanonical divisor `H`.

The [independent D5 proof](2026-10-09-session-delpezzo-D5-root-independent-audit.md)
uses the actual class `Z=L-c#` in the free Picard group of rational
`M`. Adjunction and `L.c#=4` give `c#^2=2`, hence `Z^2=-2`.
The pullback of the effective Cartier divisor `b c` gives
`b Z` in the exceptional lattice `R`. The downstairs smoothness
of `c` proves `Z` is not in `R`: otherwise `c~H` would be Cartier,
the surface would be regular along `c`, and the exceptional correction
would be zero. The signed-coordinate saturation proof covers every
exceptional subsystem in the integral `D5` lattice and leaves only
`4A1` and `A3+2A1`. In both survivors `sat(R)/R` has order two.

Thus `b` is even and `2Z` belongs to `R`. Using
`Cl(S)=Pic(M)/R` gives the genuine linear equivalence of Weil divisors

    2c ~ 2H.

In particular `2c` is Cartier, not merely numerically equivalent to
a Cartier divisor. Since it is effective, there is an actual nonzero
section `Q` of `O_S(2H)` with entire divisor exactly `2c`. The quotient
of two sections with that same divisor is a global constant unit on
the normal projective integral surface. Consequently a hypothetical
mate of degree `2n` has pullback equal to a scalar multiple of `Q^n`.
This assertion covers all positive `n`; it does not presume that `Q`
itself descends to `X`.

## 4. Complete anticanonical embedding and the fixed missing coordinate

The primary input was checked directly in the author's hosted
[Dolgachev, Classical Algebraic Geometry](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf),
Theorem 8.3.2(iii), Theorem 8.3.4, and Theorem 8.6.2. For a degree-four
weak del Pezzo resolution, the complete anticanonical map contracts
exactly the zero-degree curves and produces a normal anticanonical
model. This model is projectively normal and is an intersection of
two quadrics in `P4`, including the singular del Pezzo cases.
These are classical input theorems, not results newly proved here.

To identify that model with this particular `S`, note that
`H0(M,L)=H0(S,H)` by `sigma*O_M=O_S`. Its dimension is five; it also
follows from Riemann--Roch and vanishing on `M`. The morphism induced
by `|H|` on `S` is finite because `H` is ample and is birational
because the four original sections already give the birational
normalization map to `X`. Its image is the normal model in the cited
theorem. A finite birational map to a normal target is an isomorphism.
Thus this `S` itself is embedded as the normal integral two-quadric
complete intersection in `P4`; there is no unproved identification
of two possibly different normalizations.

The restriction `H0(S,H)->H0(c,O_P1(4))` has zero kernel. A hyperplane
divisor containing `c` would have degree four, equal to `H.c`, so
ampleness forces its entire divisor to be `c`. Then `c` would be
Cartier. A smooth Cartier curve on a two-dimensional local surface
ring forces the surface ring to be regular there: lift a generator
of the curve maximal ideal and adjoin the one Cartier equation;
these generate the maximal ideal of dimension two. The curve would
avoid all exceptional images, forcing the nonzero `D5` correction
to vanish. This contradiction proves injectivity. Both spaces have
dimension five, so restriction is an isomorphism and `c` is the
complete rational normal quartic in this embedding.

The original four sections restrict to the four literal monomials of
the fixed `C0`. Choose the unique fifth section restricting to
`U^2V^2`. The complete coordinates can therefore be chosen exactly as

    (Y0,Y1,Y2,Y3,Y4)=(U^4,U^3V,U^2V^2,UV^3,V^4) on c,

with the original projection deleting `Y2`. Its center misses `S`,
because the original four sections generate the pullback line bundle
everywhere. No general `PGL2` parameter change is needed. Diagonal
parameter changes and reversal used later preserve this particular
center; arbitrary parameter changes must not be treated as doing so.

## 5. Entire conductor and sign conventions

The [entire-conductor proof](2026-10-09-session-genus-one-entire-conductor.md)
and [independent algebra audit](2026-10-09-session-genus-one-entire-conductor-algebra-independent-audit.md)
have all their conditional geometric hypotheses established by section 4.
One pencil member has nonzero `z^2` coefficient because the center
misses `S`; cancel that coefficient from the other. Its remaining
linear coefficient `L` cannot vanish identically, since otherwise
the image would lie on a nonzero quadric, contradicting its integral
quartic degree. Restriction of a linear form to `c` is injective,
so `L_C` is also nonzero. It has degree four and cannot vanish along
the entire lifted curve.

In the conductor note's convention the equations are

    Q1=z^2-Az-R1,        Q2=Lz+R,
    F=R^2+ALR-R1 L^2.

It proves the injection `A_X->B`, regularity of the sequence `L,R`,
and exact equality `B/A_X=(T/(L,R))(-1)` before taking annihilators.
Thus `(L,R)` is the entire conductor ideal, and the upstairs conductor
is the actual Cartier divisor `L=0`. Its algebra is finite flat of
rank two over the entire plane conic, including two lines and double
lines. Normality plus the two-quadric complete-intersection model
also makes the homogeneous coordinate ring normal; a vertex module
or an omitted finite-length conductor correction is not being assumed
away.

The uniform projection note uses the alternative convention
`Q1=z^2+A'z+R1'`. These are identical after `A'=-A`, `R1'=-R1`.
The singleton condition is `A_C-2z_C=0` in the conductor convention
and `A'_C+2z_C=0` in the uniform convention. This harmless change
must be carried through a literal checker; it is not an additional
geometric assumption.

At each zero of `L_C`, the complete projective projection fiber has
the two roots of this monic equation. No point with all retained
coordinates zero is available, since the center is outside `S`.
The full-support argument from section 2 therefore forces the roots
to coincide. In the six-quadric coefficient convention this says

    rad(L_C) divides D_Q1,

where `D_Q1` is the omitted-coordinate derivative restricted to `c`.
Only support divisibility is used. This condition is valid at smooth
or singular source points and does not invoke the invalid assertion
that every isolated rank-one point must be singular on `S`.

## 6. Cartier double, full ribbon net, and all direction charts

The [independent ribbon-net proof](2026-10-09-session-genus-one-ribbon-net-independent-audit.md)
has precisely the three inputs established above: the normal
two-quadric `S`, embedded smooth rational normal `c`, and `Q` with
entire divisor `2c`. Its local proof applies at every point of `c`,
including every ADE point at which `c` is non-Cartier. The quotient
by `Q` is one-dimensional Cohen--Macaulay, its reduction is a DVR,
and its generic length is two. The injection into the localization
at its unique minimal prime forces the nilideal square to vanish;
the nilideal is then a torsion-free rank-one module over the DVR.
Hence this actual Cartier double is a ribbon globally. This argument
does not replace the symbolic double by the ordinary square of the
curve ideal; that replacement would be false at the displayed ADE
local models.

The complete-intersection resolution gives surjectivity from ambient
quadrics to `H0(S,2H)`. Lift `Q` to a third ambient quadric. It is
independent of the two surface equations and is a nonzerodivisor in
their integral quotient. The double is therefore a `(2,2,2)` complete
intersection of genus five. The ribbon exact sequence then gives
nilideal `O_P1(-6)`.

Its nilideal square-zero property gives `I_c^2` contained in `I_D`.
Its embedding therefore defines the everywhere-surjective quotient
`I_c/I_c^2 -> I_c/I_D`, and `I_c/I_D` is precisely this nilideal.
Conversely `I_D` is the inverse image of the quotient's kernel, so
this quotient determines every actual embedded ribbon here. The direct conormal computation
in the ribbon audit gives `I_c/I_c^2=O_P1(-6)^3` and **every** quotient
as a nonzero direction `eta=(eta0,eta1,eta2)`. The associated net is
exactly

    M(d) eta=0,
    M(d)=[[d0,d1,d2],[d1,d2+d3,d4],[d2,d4,d5]].

The matrix equations have rank three at every nonzero direction.
Since the actual double is a three-quadric complete intersection,
its defining quadrics span this entire kernel net, and the original
surface pencil is a two-plane in it. Thus using this net loses no
double or surface pencil arising from a mate.

The direction condition `eta1^2 != eta0 eta2` is necessary: the
complementary orbit has a cubic surface as the common net base locus,
and every pair of quadrics in it contains that surface. Such a pair
cannot define the assumed integral degree-four surface. The use of
general parameter automorphisms to prove this intrinsic orbit
statement is legitimate because degree, containment, and integrality
are preserved. The subsequent fixed-projection calculations keep
the original center and use only its stabilizing diagonal changes
and reversal. These are distinct uses of the parameter action.

## 7. Squarefree and [2,1,1] coverage

The omitted-coordinate derivative map on the six quadric space is

    D_d=d0 U^4-d1 U^3V-2d3 U^2V^2-d4 UV^3+d5 V^4.

Its only kernel is the quadric `E2`. The matrix `M(E2)` is invertible,
so that kernel misses every net above. Thus the two independent
surface quadrics have independent derivatives. Choose one with
`d3=0`; its derivative is the nonzero quartic `L_C`, whose middle
coefficient vanishes. The other has `d3!=0`, so its derivative has
nonzero middle coefficient. If `L_C` is squarefree, singleton support
would force these two degree-four forms to be proportional. Their
middle coefficients contradict that. This uniformly excludes the
partition `[1,1,1,1]`.

The [complete [2,1,1] proof](2026-10-09-session-ribbon-211-projection-independent-audit.md)
then uses the exact three-dimensional derivative space. The direction
chart `eta0!=0` and its reversal cover every direction except
`(0,1,0)`, which is explicitly treated. On the main chart the three
forms `G0,G1,G2` have common basepoint only when
`eta=(1,u,u^2/4)` with `u!=0`; that basepoint is simple and unique.
Off this locus, every geometric fiber of the derivative map contains
at most two points, as seen from its degree-at-most-two coordinate
ratio and its `G2=0` fiber. Therefore the three distinct zeros of a
`[2,1,1]` quartic cannot all satisfy the singleton requirement.

On the unique basepoint locus, a center-preserving diagonal change
sets `u=1`. Removing its common linear factor gives a basepoint-free
cubic map. Infinity has no finite companion; exact cross products
show its only double fiber is the pair defined by
`t^2+t/4+1/4`. For three distinct singleton-contact zeros, one must
be the basepoint and the other two this double fiber. The zero-center
coefficient condition and divisibility by that quadratic force one
unique candidate `L_C`, and it has a fourth distinct zero outside
that fiber. Thus it fails singleton support. The proof retains the
whole net rather than dropping the derivative-invisible `E2` term,
and covers every endpoint and direction-coordinate boundary.

## 8. Exact remaining obligation and conditional closure

A nonzero binary quartic over the algebraically closed field has one
of the five multiplicity partitions

    [1,1,1,1], [2,1,1], [2,2], [3,1], [4].

The first two are excluded by section 7. The other three are the
explicit scope of the independently assigned remaining-partition
audit. Its required conclusion must cover every derivative-invisible
quadric coefficient and direction boundary, not just an example
pencil or a numerical root. The [owner's completed reconstruction](2026-10-09-session-ribbon-repeated-partitions-complete.md)
states such coverage, and the root's separate `[4]` and bounded
`[2,2]` arguments support two parts; their mathematical acceptance
is being handled outside the present interface task.

If that remaining coverage is accepted, every hypothetical mate has
been contradicted: its normalization and Cartier double necessarily
enter the audited fixed-center net, its nonzero `L_C` necessarily
belongs to one of the five partitions, and every partition is
excluded. No assumption that the displayed toric families exhaust
marked curve/projection pairs is needed. No genus-one conductor
smoothness hypothesis is left outstanding: the entire conductor
formula retains all schemes until a particular surviving pencil
itself forces a smooth conic, if that is used by its final proof.

At this note's writing the **interfaces are accepted**, while
promotion of the entire genus-one no-mate theorem remains conditional
on the separately audited remaining-partition coverage. This is a
logical dependency boundary, not an identified gap in the application
of the accepted rationality, ADE, D5, anticanonical, conductor, ribbon,
squarefree, or `[2,1,1]` results.

## 9. Evidence scope

This audit read the cited repository proofs in full and checked the
primary anticanonical model statements directly. The exact conormal
and derivative formulas, Hilbert-series identities, and local ribbon
arguments are reproduced or traced above; no new black-box finite
enumeration is used to establish this logical interface result.
The previous execution and record-integrity seals retain their
original scopes and do not count this later note as a rerun.

A delegated read-only microaudit by `ribbon_interface_microaudit`
independently accepted the local ribbon argument, the kernel-net
exhaustiveness, the intrinsic off-conic obstruction, and every `[2,1,1]`
direction/basepoint chart. Its separate exact checks used standard-library
rational polynomial arithmetic and confirmed the displayed kernels,
derivatives, both cross products, elimination, unique double fiber,
remainder matrix, rank witness, candidate kernel, final factorization,
and distinct extra image. Its mathematical finding agrees with the
arguments above and identifies no additional hypothesis.

It did identify an evidence-attribution error in the older `[2,1,1]`
note, section 5. That note says the current
`verify_session_genus_one_projection_2026_10_09.py` checks the divided
cubic, cross products, remainder matrix and candidate factorization.
Reading the entire current source shows that it checks the uniform
projection and an `A3+2A1` displayed family instead. The separate
`derive_session_rnc_ribbon_net_2026_10_09.py` contains the net basis,
derivatives and common-basepoint gcd, but also lacks the full divided
cubic calculation. Thus their existing passing executions must not
be attributed to those missing checks. This is a provenance correction,
not a failure of the written `[2,1,1]` proof.

The new independent [Macaulay2 companion](../computations/verify_session_genus_one_211_interfaces_2026_10_10.m2)
supplies 42 exact identities over `QQ`, covering the rank-three net
minors, derivative injectivity, all three actual basis kernels and
derivatives, simple basepoint and its division, two cross products,
third cross product on the unique candidate, exact remainder matrix,
rank-two witness and kernel, the four-root factorization, and the
extra distinct derivative image. Its observed terminal execution
returned exit zero and `PASS` in `0.521622041` seconds on 2026-10-10.
The first scaffold run was terminal with exit one because `net` is
a protected Macaulay2 global name; renaming it `netCoefficients`
resolved that implementation error without altering any identity.
Both attempts and the actual passing source hash are recorded in
[the execution record](../validation/2026-10-10-genus-one-interfaces/execution-record.json).

The formerly used temporary Python environment was rechecked and
currently lacks SymPy; the desktop-bundled Python does as well. Those
observations are retained in the execution record. They do not turn
the historical Python passes into current passes, and the new
companion uses the currently verified Macaulay2 `1.26.06` runtime.


---

## Source: 2026-10-10-session-genus-two-bisection-full-independent-audit.md

# Independent continuation audit: the entire genus-two bisection lane is excluded

Date: 2026-10-10. Auditor: `bisection_full_audit`.
Status: **PROVED HERE / independent mathematical audit accepted**.
This note changes no canonical frontier file. It supplies a stronger
structural conclusion than the original requested conductor audit:
**no genus-two quartic mate for the fixed curve can lie in the
`lambda=0` bisection stratum.** The `lambda=1` section stratum, higher
carrier degrees, the unrestricted fixed-curve question, and the universal
STCI question are not settled by this result.

Work throughout over an algebraically closed field of characteristic
zero. The fixed curve and its projective equivalents are

    C0=[s^4:s^3*t:s*t^3:t^4] in P3.

This is a proof with the actual finite normalization, actual Cartier
double, and its full global nilpotent structure. It is not a
first-normal approximation to an unrestricted mate.

## 1. Accepted inputs and the audited second-pencil reduction

Let `X` be an integral nonnormal quartic containing C0, whose
normalization has sectional genus two. Put

    nu:S->X, sigma:M->S, H=nu*O_X(1), L=sigma*H.

The accepted entire-conductor and adjoint inputs give a smooth rational
M, rational singularities on normal S, and

    K_M^2=0, L^2=4, K_M.L=-2,
    f=K_M+L, f^2=0, K_M.f=-2,
    R sigma_*O_M=O_S.

The complete `|f|` is a connected rational pencil. Assume a hypothetical
mate in the bisection lane. Its smooth embedded lift `c_S` is isomorphic
to C0, and its strict transform c on M satisfies

    c^2=0, K_M.c=-2, f.c=2,
    L equivalent_Q to c+Z,

where Z is effective rational, sigma-exceptional, supported on vertical
smooth rational (-2)-curves, and orthogonal to L. Its exceptional
correction is not integral. These hypotheses are precisely the
`lambda=0` lane, not all genus-two mates.

I independently checked the [second-pencil audit](2026-10-10-session-genus-two-bisection-second-pencil-independent-audit.md):

* `0->O_M->O_M(c)->O_c->0` and rationality give `h0(c)=2` and generation
  everywhere. The Stein factor has genus zero; its finite map to the
  target has degree one since otherwise the complete system has at
  least three sections. Thus `|c|` is a connected rational pencil.
* `(f,c)` is dominant of degree two. Its normal Stein cover W of
  `P1 x P1` is finite flat: normal surface rings are CM, and the finite
  module over the smooth base is locally free. Trace splits the algebra.
  Restriction to each general ruling has upstairs P1, giving branch
  line bundle `O(1,1)`, hence branch class `(2,2)`.
* Finite duality gives `omega_W=phi*O(-1,-1)` and `(-K_W)^2=4`.
  Anti-ampleness of omega and the birational Leray sequence imply
  rational singularities, rather than assuming them from rational
  birationality. Thus W is Gorenstein ADE. Its crepant minimal
  resolution V has `K_V^2=4`, and M is obtained from V by exactly four
  point blowups, including infinitely near centers.
* For the actual integral relative canonical divisor R, the resulting
  equality is `Z+R equivalent_Q to 2f`. Clearing denominators and
  using the complete connected pencil shows this is an actual sum
  of entire fibers, `Z+R=sum q_t F_t`. Intersecting each part with
  K gives `q_t=k_t/2`, where k_t counts the four blowup centers over t.
  In particular

      Z+R=(1/2)sum_t k_t F_t,
      sum_t k_t=4,
      2Z=sum_t k_t F_t-2R.

These equalities retain all component multiplicities and intersection
centers. The total-transform exceptional basis verifies
`K_M.R_t=R_t^2=-k_t` even at infinitely near centers.

Thus 2Z is an integral exceptional divisor. The integral numerical
class `2c+2Z-2L` is trivial on the smooth rational M by the accepted
numerical-to-linear lemma. Pushing the resulting actual linear
equivalence to normal S gives

    2c_S ~ 2H.

This is an actual Cartier equivalence. In particular there is a
nonzero section `Q in H0(S,O_S(2H))` with entire divisor `2c_S`.
The exceptional class has exact order two, so every mate degree is
even. These are normalization statements; Q need not be ambient.

## 2. Independent normal-bundle calculation for the literal C0

Write `F=(s^4,s^3*t,s*t^3,t^4)`. The tangent and Euler sequences
give `deg N_(C0/P3)=14`. To compute the splitting, twist the conormal
sequence by `O_P1(6)`. A global section of `N^*(6)` is a tuple of
quadratic binary forms

    a_i=A_i s^2+B_i s*t+C_i t^2

satisfying both polynomial identities

    sum_i a_i (partial F_i/partial s)=0,
    sum_i a_i (partial F_i/partial t)=0.

Here the Euler condition `sum a_i F_i=0` follows from the two
derivative conditions since the common degree is four. Conversely
these two derivative identities say the Euler-kernel section maps
to zero in `Omega_P1(6)`. They therefore compute precisely the
global conormal sections, without discarding the points s=0 or t=0.

The coefficients of the first identity, from s^5 to t^5, are

    4A0, 4B0+3A1, 4C0+3B1, 3C1+A2, B2, C2.

Those of the second are

    A1, B1, C1+3A2, 3B2+4A3, 3C2+4B3, 4C3.

The endpoint equations immediately kill ten of the twelve unknowns.
The remaining two satisfy

    3C1+A2=0, C1+3A2=0,

whose determinant is eight. In characteristic zero all twelve
coefficients are zero. Thus `H0(N^*(6))=0`.

By the splitting theorem on P1, write `N=O(a)+O(b)` with a+b=14.
The preceding vanishing implies a,b>=7, hence

    N_(C0/P3)=O_P1(7) direct_sum O_P1(7).

In particular

    Hom(N_(C0/P3)^*, O_P1(-8))=0.

This is a direct exact calculation for the fixed monomial quartic;
it is not an assertion about all rational-quartic projections.

## 3. The actual Cartier double is a ribbon with nilideal O(-8)

Let `R_C=V_S(Q)` be the entire double curve. Since S is a normal
surface, it is CM. Since Q is a section of an invertible sheaf and
is nonzero on integral S, it is a nonzerodivisor. Therefore R_C
is a pure CM curve with support exactly the smooth embedded c_S.
At its generic point the normal surface is a DVR and div(Q)=2c_S,
so R_C has generic length two.

Let J be its nilradical. Generically J has rank one and J^2=0.
The image J^2 in O_(R_C) is thus supported at finitely many points.
A pure CM curve has no nonzero coherent subsheaf supported at
finitely many points, so J^2=0 everywhere. The same argument shows
that J has no finite-support torsion. Hence J is a rank-one
torsion-free O_(c_S)-module, and, since c_S is smooth, is a line
bundle. This proves that the actual full R_C is a ribbon.

The nilideal's degree can be calculated without assuming any
Gorenstein or Q-Gorenstein property of S. The accepted rational
resolution and Riemann--Roch give, for every integer m,

    chi(O_S(mH))=chi(O_M(mL))=1+2m^2+m.

The exact Cartier sequence is

    0->O_S(-2H)->O_S->O_(R_C)->0.

Consequently

    chi(O_(R_C))=1-7=-6.

The reduction sequence `0->J->O_(R_C)->O_(c_S)->0` and
`chi(O_(c_S))=1` imply `chi(J)=-7`. Thus

    J=O_P1(-8).

Equivalently this ribbon has arithmetic genus seven. No formula
for a canonical divisor on non-Gorenstein S entered this argument.

## 4. The actual ambient conormal map gives a contradiction

The actual normalization morphism, followed by the inclusion of X,
restricts to a morphism

    j:R_C -> X -> P3,

whose reduction is the given closed embedding c_S~=C0. The ambient
ideal sheaf `I_(C0/P3)` pulls back into J. Because J^2=0, its square
pulls back to zero. This gives a global O_(C0)-linear homomorphism

    I_(C0/P3)/I_(C0/P3)^2 = N_(C0/P3)^* -> J.

This statement uses the full ribbon, including every point where
normalization can fail to be an immersion. Such points do not
prevent formation of the global conormal map.

The map is nonzero. Indeed the accepted entire conductor is a line
Gamma, while C0 has degree four and is not that line. On the dense
open of C0 outside Gamma, normalization is an isomorphism with X.
There R_C is an actual closed subscheme of X and hence of P3.
For that closed immersion the ambient ideal of the reduced curve
generates its nilideal. Thus the displayed map is generically
surjective onto a line bundle, and in particular nonzero.

Section 2 and Section 3 show simultaneously that the target is
O(-8) and that no nonzero homomorphism to it can exist. This is the
contradiction. Therefore the entire genus-two bisection mate lane
is excluded for the fixed C0 in characteristic zero.

The obstruction is global. A generic/local conormal map exists,
but it cannot extend to the required global nilideal. The proof
does not infer multiplicities from tangent support data; the
Cartier equivalence forces the whole CM ribbon before its
conormal map is used.

## 5. The originally requested conductor chain remains valid but weaker

I independently audited Sections 2--4 of the [quadratic-descent note](2026-10-10-session-genus-two-bisection-quadratic-descent.md),
and the [even-fiber exclusion](2026-10-10-session-genus-two-bisection-even-fiber-exclusion.md).
Their necessary reductions are valid. They are superseded as open
mate possibilities by the contradiction above.

The exact normalization sequence gives `h0(S,2H)=11`, against ten
ambient quadratic sections. On the entire conductor

    p_*O_D=O_Gamma (+) O_Gamma(-2), w^2=delta,
    Q|D=m+a w.

The common-conductor square identifies a=0 with ambient descent.
For the section having divisor 2c_S, a=0 would give a quadric mate.
The unique quadric q containing C0 has curve class (1,3), while
X restricts to (4,4), so it cannot be a mate. Thus a!=0 and can
be normalized to one. Q is a nonzerodivisor on D since D is CM
and none of its components, of total degree two, is c_S.

If m=0, the full Q^2 descends to an ambient quartic and yields a
(4,4) mate, excluded by Craighero--Gattazzo. The exact primary
statement is verified in [the source audit](2026-10-10-session-bisection-primary-descent-sources.md):
Proposition 4, printed page 187, over an algebraically closed
field of characteristic different from two and three. The
paper's convention requires reduced surfaces. The descended
quartic here is necessarily integral reduced: every factor would
contain nonplanar C0; a nonintegral degree-four factorization must
therefore consist of its unique quadric q twice, already excluded
by the same divisor-class argument. This supplies the scope guard
required for that citation.

If m!=0, existence of a descended positive power gives the exact
whole-section identity

    m^2=rho*delta,
    rho=((1+zeta)/(1-zeta))^2,
    zeta a root of unity distinct from 1,-1.

The orientation is m^2=rho*delta, not its reciprocal. One can
derive it directly at the generic algebra by dividing the
involuted section by the nonzerodivisor Q. A characteristic-zero
root of unity has no nilpotent correction. The equality extends
over the line because the relevant sheaves are invertible.
It forces a nonzero square delta=r^2 and m=alpha r. The full
conductor is reduced split, with Q restrictions (alpha+1)r and
(alpha-1)r. The ratio condition for descent is

    ((alpha+1)/(alpha-1))^n=1.

Here alpha!=0,+1,-1 and n>=3; these orders were not bounded by
the quadratic algebra alone. This was a necessary reduction,
not an actual surviving surface or mate construction.

For each even positive k_t, the actual Z_t is integral. Its
positive support contains complete exceptional fibers: an
outside zero coefficient adjacent to it would make Z.E>0,
contradicting (c+Z).E=0 and c.E>=0. Hence at a singular point
contacted by c, O(c+Z_p) is a genuine line bundle of degree zero
on every exceptional component. Kollár's Proposition 76(1)
descends it, giving local Cartierness of actual c_S. A smooth
Cartier curve through a surface point forces that local ring
to be regular, a contradiction. The primary theorem and its
proper log minimal resolution hypothesis are checked in the
same source audit; the accepted exceptional (-2)/(-3) curves
have K.E>=0, and any needed log refinement preserves all
degree-zero conditions. Thus every positive k_t is odd, leaving
only [3,1] and [1,1,1,1] before the ribbon obstruction.

The original second-pencil audit's retained [2,1,1] is a valid
earlier weaker snapshot; the even-fiber note supersedes it.
The original quadratic-descent note repeats that weaker table,
so its retained [2,1,1] must not be presented as the latest
necessary blowup list. The present full exclusion supersedes
all of these hypothetical surviving lambda-zero partitions.

## 6. The proposed contact identification also has a valid conditional proof

For completeness, Section 5 of the owner note can be promoted as
a conditional lemma under its hypothetical bisection and split
descent assumptions. It is no longer needed to exclude the lane.

Every exceptional fiber met by c has positive correction and
lies wholly in Supp(Z), by the support-closure argument. Thus
its graph is entirely vertical (-2). In the accepted normal ADE
ambient conic model T these graphs are contracted, while only
horizontal (-3) curves can be contracted by T->S. Therefore S
is ADE near c_S, and in particular Gorenstein there. Its actual
conductor ideal is omega_S and is locally invertible. Hence D
is Cartier near every point of c_S intersecting D.

Let d be its local Cartier equation at such a point. On the
ribbon R_C, d meets the reduction properly and is a
nonzerodivisor on both O_(c_S) and J. Quotienting the ribbon
sequence by d shows

    length(O_(R_C)/(d))=2*length(O_(c_S)/(d)).

In the split conductor algebra with Q=m+w=alpha r+w, the
quotient by Q is locally O_Gamma/(r^2), since alpha^2-1 is
nonzero. Its length at a zero of r is twice the order of r.
These two lengths describe the same scheme R_C intersect D.
The common conductor ideal pulled to c_S is precisely the
ambient ideal of Gamma intersect C0. Its degree is two in
the accepted bisection line-position theorem. Therefore

    div_Gamma(r)=Gamma intersect C0

as entire degree-two schemes, not just as supports. At a
simple contact, Q has order one on each of the smooth split
conductor components; a smooth S would make c_S Cartier and
Q a unit times its squared equation, forcing even order on
each component. Thus each simple contact would be singular
on S. A tangent double contact is not excluded by that
parity observation alone.

The existence of the forced global ribbon, however, has
already contradicted the balanced normal bundle regardless
of these contact types.

## 7. Continuation boundary and evidence

All conclusions above are exact sheaf, divisor, and polynomial
arguments. No sample or bounded search replaces any universal
quantifier in the bisection exclusion. The derivative identities
in Section 2 can be checked independently coefficient by
coefficient, and are included in full for that purpose.

The preserved weaker sources and primary-source audit retain
their own attribution. The current proof introduces no new
Macaulay2 execution count. It is independently checked against
the actual source notes rather than counting parallel-agent
agreement as proof.

The remaining genus-two mate lane is lambda=1, with c^2=1,
f.c=1 and length-three conductor contact. This note supplies
no exclusion there. The full genus-two quartic carrier lane,
unrestricted C0, and universal projective-curve question must
retain exactly their separately audited status.
