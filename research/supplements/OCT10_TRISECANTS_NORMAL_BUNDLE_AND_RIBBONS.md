# Historical mathematical investigations

Full original mathematical text follows. Preserve source-level evidence status, counterexamples, corrections and unresolved boundaries; no independent re-audit or result promotion.

---

## Source: 2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md

# Continuation audit: the nonendpoint trisecant stratum is excluded

Session date: 2026-10-10. Auditor: `trisecant_nonendpoint_audit`.
Status: **PROVED HERE / independent global coverage audit passed**, using
the accepted inputs identified below. No canonical frontier file is
edited. This proves a bounded mate exclusion for the fixed monomial
rational quartic in characteristic zero; it does not resolve arbitrary
carrier degrees or the universal STCI question.

## 1. Binding source and scope

The owner proof is
[the nonendpoint trisecant conic obstruction](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-nonendpoint-trisecant-conic-obstructionmd),
SHA-256
`5d02eb6f79da5e4c367a472a5ce711dfe42953bfb78abefed82459027831c975`.
The following separately accepted inputs were read in full for this audit:

* [Normal ambient conic model](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-blowup-lift-normality-independent-auditmd),
  SHA-256 `8b2f8b2c73f95b5b71854425359fc9c8dfa188156ccc8375bc8acd513619d41b`.
* [Actual entire conductor](2026-10-10-session-genus-two-entire-conductor-independent-audit.md),
  SHA-256 `77bc3c17b7832907fd2d859de6e4d82735f6b279efb923ecd9a865fbc0767550`.
* [Lambda-one marked-prime classification](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-lambda-one-marked-prime-auditmd),
  SHA-256 `c7dd16ed8d9c18c921faaaaba130daec59fd2aec845f4ce59a9232567bb22f34`.
* [Exclusion with the degree-zero horizontal prime absent](2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md),
  SHA-256 `f6ac621d0906917947cbc5ea2ecb91c7ef85ab81129e8b1e2a9527fb47c07f26`.

Let `X` be an integral nonnormal quartic carrier of

    C0=[s^4:s^3t:st^3:t^4]

over an algebraically closed field of characteristic zero, and suppose
its normalization has sectional genus two. Assume a mate of any positive
degree exists in the retained lambda-one stratum. The accepted inputs
then give a resolution `M`, the smooth embedded lift `c#`, and

    f.c#=1,       c# ~ L-Z,
    Z effective rational sigma-exceptional,
    K_M.Z=1,      Z.E=-c#.E for every sigma-exceptional prime E.

There is an actual normal Du Val strict transform

    rho:M -> T subset Bl_Gamma(P3),
    D_T=E_B|T,       E_B=P1_Gamma x P1_f,       [D_T]=(2,2).

Only vertical (-2) exceptional curves are contracted by `rho`; the
subsequent map `T->S` contracts the horizontal (-3) sections. The
absence-of-B exclusion forces the actual prime

    B=e0-e_i-e_j,       B^2=-3,       f.B=1,       c#.B=0.

Its image `B_T` is a whole fiber of `E_B->Gamma`, of class `(1,0)`.
There can be at most one other horizontal prime. The coefficient of
`B` in `Z` is **not** assumed positive in the reducible-divisor cases.

Assume `Gamma` is a nonendpoint trisecant of fixed `C0`. Equivalently
it is a line in the degree-three ruling of the unique smooth quadric,
with parameter neither zero nor infinity. Its three curve contacts
are distinct in both their Gamma coordinates and their f coordinates.
For example, after a diagonal automorphism they are the three roots
of `t^3-s^3`, while the actual plane-pencil map on `C0` is `[s:t]`.
This elementary assertion is also recorded in
[the conductor-line position note](2026-10-10-session-genus-two-conductor-line-position.md).

**Conclusion:** no such mate exists. The proof below exhausts all
effective divisor decompositions of `D_T`, including nonreduced ones.

## 2. Where the singleton-support test is valid

Because `f|c#` has degree one, the image `c_T` is the actual section of
`T->P1_f` obtained by composing the inverse of `c#->P1_f` with `rho`.
The map `c#->c_T` is an isomorphism. Thus each Gamma-contact corresponds
to one specified point and one specified f-coordinate on `c_T`.

Let `G` be the hypothetical mate. At any Gamma point `p` on `C0`,
`G(p)=0`; therefore the pullback of `G` vanishes at every point of the
actual finite inverse conductor `D->Gamma` above `p`. Its zero-set on
`S` is exactly `c`. Since `c->C0` is an isomorphism, the support of
that inverse-conductor fiber must be a singleton, the point of `c`.

This test can be transferred from `S` to `D_T` at every Gamma point
which is not the image of a contracted horizontal prime: `T->S` is an
isomorphism there. It cannot be transferred blindly over the image
of a horizontal section. We use precisely this qualified test.

In particular the argument never infers that `c_T` avoids `B_T` from
`c#.B=0`. The curves can be separated on `M` by an ADE chain and meet
after that chain contracts on `T`. It also never assumes that the
finite inverse conductor, or `D_T`, is reduced.

Every horizontal prime supplies a Gamma-fiber component of `D_T`.
Conversely a Gamma-fiber component has `L`-degree zero and f-degree
one, and its strict transform is one of those horizontal primes.
Consequently an additional horizontal contraction cannot occur over
an unlisted Gamma point in any divisor case below.

## 3. Exhaustion of effective divisor decompositions

On `P1 x P1`, every effective prime has nonnegative bidegree.
Since `B_T` has degree `(1,0)` and `D_T` degree `(2,2)`, its
multiplicity is one or two. This includes every scheme multiplicity.

### Multiplicity two on B

If `D_T=2B_T+F` with `[F]=(0,2)`, then `F` is two f-fibers, possibly
equal. There are at least two C0 contacts away from `p_B` with
different f-coordinates. Equal f-fibers cannot contain both specified
points. Distinct f-fibers give two different points above every Gamma
point away from `p_B`, violating singleton support. There is no other
horizontal prime in this class budget.

### Multiplicity one, reducible residual

Write `D_T=B_T+R` with `[R]=(1,2)`. There is exactly one prime of
positive first degree in any reducible `R`; the remaining primes are
f-fibers. Its first degree is one, and its second degree is zero or
one. Hence the exhaustive possibilities are

    R=G_(1,1)+F_(0,1),
    R=B'_T+F_(0,2),

where the second expression includes equal or distinct f-fibers.
A reducible divisor of class `(1,1)` is already in the second case.

If `G_(1,1)` is irreducible, it maps isomorphically to Gamma. Together
with the fixed f-fiber it gives singleton support above at most the
one Gamma point where they intersect. There is no second horizontal
prime; the at least two contacts away from `p_B` therefore contradict
the support test.

In the second expression, if `B'_T=B_T` this is the preceding
multiplicity-two case. Otherwise there are two horizontal fibers.
For two distinct f-fibers the third C0 contact, away from both
horizontal-image points if they are contacts, has two inverse points.
If one or both horizontal-image points are not contacts there are
still more contacts away from them. In every case singleton support
fails at some contact away from both horizontal-image points.

For a double f-fiber the only potential divisor is

    D_T=B_T+B'_T+2F0,       p_B != p_B'.

At least one C0 contact is away from both horizontal-image points.
If either image point is not a C0 contact, there are at least two
contacts away from both with distinct f-coordinates, which cannot
both lie on `F0`. Thus the two horizontal-image points must be two
of the three C0 contacts, and the remaining contact lies on `F0`.
The f-coordinate of the contact over `p_B` differs from that last
contact's coordinate. At that point `D_T` is locally just the reduced
smooth component `B_T`; neither `B'_T` nor `F0` passes through it.
Its defining equation on the smooth `E_B` has nonzero differential.
The same is therefore true for the defining equation of `T` in the
smooth ambient blowup, and `T` is smooth at that point. The resolution
is an isomorphism there, so `c#` meets `B` there, contradicting
`c#.B=0`.

This last argument covers the important case in which the coefficient
of `B` in `Z` is zero and the other proper horizontal prime contributes
the required canonical correction. No premature assertion that
`p_B` is a C0 contact was used.

## 4. The integral residual has two transverse crossings

It remains that `R` is an irreducible divisor of class `(1,2)`.
Its projection to `P1_f` has degree one. There is no fixed f-fiber
component, so this projection is finite and `R` is the graph of a
morphism from `P1_f`; in particular it is a smooth rational curve.
Its other projection, to Gamma, has degree two and is separable.

There is no additional horizontal fiber in this divisor. Thus `B`
is the sole horizontal sigma-exceptional prime. All vertical primes
have canonical degree zero, while `K_M.B=1`, so

    a := coeff_B(Z) = K_M.Z = 1.

This positivity is established only now. The actual pullback divisor
of `G` has positive B coefficient, so `G` vanishes at its Gamma image
`p_B`. Set-theoretic equality `X intersect V(G)=C0` forces `p_B` to
be one of the three contacts.

The other two contacts are away from all horizontal contractions.
Their residual fibers are singletons, hence they are branch values
of the separable degree-two morphism `R->Gamma`. Riemann--Hurwitz
gives total ramification degree two for a degree-two map of P1.
These are already its two distinct branch values. It is consequently
unramified over `p_B`, and `R` intersects `B_T` at two distinct
transverse points.

There is no singular point of `T` on `B_T` outside these crossings:
there `D_T` is a reduced smooth divisor on the smooth `E_B`, so its
equation has nonzero differential. At a crossing choose coordinates
with `E_B=(r=0)` and actual branches `(u,r)`, `(v,r)`. Its equation is

    F=uv+r h(u,v,r).

The separately delegated
[relative formal Morse and specified-branch audit](#source-2026-10-10-session-relative-morse-conductor-branches-independent-auditmd),
SHA-256 `a88aacc867f2cfae9e77ee8e54e88875b395f6446935dfc24f8ad540008e5153`,
proves directly that formal coordinates preserving `r` give

    F=xy+g(r),       (u,r)=(x,r),       (v,r)=(y,r).

If singular, `g` has finite order at least two. A harmless unit
rescaling gives `xy=r^(n+1)` and preserves these actual branch
ideals. The explicit resolution charts in that audit show that the
two specified branches meet the opposite endpoints of the exceptional
A_n chain, transversely. For A1 they meet its sole exceptional curve
at distinct points. This is consistent with the primary normal forms
in [Reid's Du Val notes, Table 1 and section 2.2](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf),
which this audit also read directly. The local argument is algebraic
over every algebraically closed characteristic-zero field, using
completed local rings; it does not require the field to be C.

Hence the sigma-fiber containing `B` consists of the (-3) curve `B`
and at most two A-chains attached at endpoints. No finite chain-length
bound, A1-only assumption, or D/E graph enumeration is being used.

## 5. Exact all-length contradiction

The contact of `c_T` over `p_B` must be at a singular point of `T`;
otherwise `c#` would meet `B` directly. The accepted embedded-smooth
uniformizer condition implies that `c#` meets exactly one exceptional
prime in that connected sigma-fiber, transversely once. Label the
chain over this contact by `1,...,n`, with B attached at node 1, and
let `k` be the contact node, `1<=k<=n`. The other crossing supplies a
chain of length `m>=0`, where zero means the crossing is smooth.
The section `c_T` has one f-coordinate over `p_B` and cannot contact
both crossing chains.

For completeness, the exact solution on the contact chain is

    z_i = a*(n+1-i)/(n+1) + i*(n+1-k)/(n+1),       i<=k,
    z_i = a*(n+1-i)/(n+1) + k*(n+1-i)/(n+1),       i>=k.

These formulas agree at k, vanish at the opposite virtual boundary
`i=n+1`, have virtual boundary `z_0=a`, and satisfy the second
difference equation `2z_i-z_(i-1)-z_(i+1)=1_(i=k)`.
Thus its neighboring coefficient is

    z_1 = n*a/(n+1) + (n+1-k)/(n+1).

The other chain has no source and contributes `m*a/(m+1)`. Since
`Z.B=-c#.B=0`, the exact B intersection equation yields

    a = ((n+1-k)/(n+1)) /
        (3-n/(n+1)-m/(m+1)).

Its denominator is exactly

    d = 1 + 1/(n+1) + 1/(m+1) > 1.

The numerator is positive and strictly less than one. Equivalently
the strict gap has the exact positive formula

    1-a = ((k+1)/(n+1)+1/(m+1))/d > 0.

Therefore `a<1` for all `n>=1`, `m>=0`, `1<=k<=n`, contradicting the
necessary value `a=1`. This proves the irreducible residual exclusion.

## 6. Exact computation, failures, and preserved boundaries

The geometric proof and positivity argument above are the proof.
The independently supplied symbolic script is only a countercheck of
the rational identities. An isolated replay of its initial bytes
failed after six passing identities because `source` is a protected
Macaulay2 global. A minimally repaired copy failed after nine passing
identities because `denominator` is also protected. Both full sources,
stdout, stderr, execution metadata, and hashes are retained in

[the continuation validation directory](../validation/2026-10-10-genus-two-nonendpoint-trisecant-continuation-audit/README.md).

Renaming just those two identifiers to `chainSource` and
`chainDenominator` gives the final source hash
`6a8b08f36f28c37865a2fd6708652e1d857fb2695c023687940186b2f91f4c7a`.
Its isolated Macaulay2 1.26.06 execution passed **12 exact rational
identities**, exit zero, observed tool chunk `e1c56e`, wall time
0.683747833 seconds (subprocess time 0.658300333 seconds). Its checked
expressions retain symbolic n, m and k; this is not a finite graph
search. The source is a repaired version of the same mathematical
checker, not a new distinct mathematical source. The historical
97-source/110-execution index is untouched.

All divisor types of `(2,2)` containing B, zero B correction when
another horizontal prime occurs, the unique satellite allowed in
the marked model, arbitrary A-chain lengths, and singular or
nonreduced finite inverse conductors are covered by this exclusion.
The relative local geometry forces the endpoint attachment in the
irreducible residual case; it is not imposed as a marked-graph
shortcut.

The endpoint triple-contact trisecants remain outside this proof:
their unique Gamma-contact supplies no two distinct residual branch
values. The lambda-zero stratum, higher carrier degrees, unrestricted
fixed-C0 STCI, and the universal projective-curve question remain
**OPEN**. No novelty or literature-resolution claim is made.


---

## Source: 2026-10-10-session-positive-characteristic-primary-refresh.md

# Positive-characteristic primary-source refresh, 2026-10-10

Status: bounded literature verification. This supplements the [2026-10-06 audit](2026-10-06-positive-characteristic-literature-audit.md). It adds a precise later toric extension, independently rechecks Moh's official abstract, and records the continuing full-text access limit for Hartshorne. It asserts no universal projective STCI theorem and no new theorem proved in this repository.

## Moh: the official abstract and the exact projection hypotheses

T. T. Moh, *Set-theoretic complete intersections*, Proc. Amer. Math. Soc. **94** (1985), 217–220, DOI [10.1090/S0002-9939-1985-0784166-1](https://doi.org/10.1090/S0002-9939-1985-0784166-1).

The [official AMS abstract](https://www.ams.org/proc/1985-094-02/S0002-9939-1985-0784166-1/) explicitly states:

1. Every projective monomial curve in `P^n_k` is an STCI when `char(k)=p>0`. The abstract does not require `k` to be algebraically closed for this monomial assertion.
2. Over an algebraically closed field of characteristic `p>0`, a projective curve `C` is an STCI if it admits a linear projection to `P^2` whose center misses `C`, whose image is birational to `C`, and whose plane image has only cusps as singularities.

Access provenance: direct browser opens of the AMS article and its PDF variants failed; the final direct article retry returned HTTP 403. A browser **search** for `"Set-theoretic complete intersections" "Moh" "cusps"` returned the AMS page itself with its complete official abstract and bibliography. The verification therefore uses indexed text from the publisher's own abstract, not an aggregator's paraphrase and not the full proof. No theorem numbering, proof details, or specialized meaning of "cusp" beyond that official abstract has been independently verified here.

The first statement applies to the literal monomial quartic `C0=[s^4:s^3t:st^3:t^4]` in every positive characteristic, by membership in that stated family. This is a direct family application, not a transfer from an affine theorem. The second statement does **not** assert that every projective curve admits such a projection. In particular, a generic nodal plane projection does not satisfy its displayed singularity hypothesis.

## Later constructive toric extension: retain full parametrization

Margherita Barile, Marcel Morales, and Apostolos Thoma, *On Simplicial Toric Varieties Which Are Set-Theoretic Complete Intersections*, J. Algebra **226** (2000), 880–892, DOI [10.1006/jabr.1999.8195](https://doi.org/10.1006/jabr.1999.8195).

The [primary publisher abstract](https://www.sciencedirect.com/science/article/pii/S0021869399981954) states that every simplicial affine **or projective** toric variety **with full parametrization** is an STCI in positive characteristic. It also describes the proofs as constructive and the resulting equations as binomial. Its other abstract statements give almost-STCI results in arbitrary characteristic; those are weaker than STCI and must remain separate.

Access provenance: a browser search for `"Set-theoretic complete intersections" "Moh" filetype:pdf` returned the ScienceDirect primary page with this abstract. A subsequent direct page open failed. This refresh verifies the abstract-level assertion, not the paper's detailed definition of full parametrization or numbered theorem statements. Neither "simplicial" nor "with full parametrization" may be dropped. This statement supplies a toric extension of the monomial result; it provides no result for arbitrary integral projective curves.

## Hartshorne: bibliographic record, continued proof-access boundary

Robin Hartshorne, *Complete intersections in characteristic p>0*, Amer. J. Math. **101** (1979), 380–383, DOI [10.2307/2373984](https://doi.org/10.2307/2373984), [JSTOR primary record](https://www.jstor.org/stable/2373984).

The record and Moh's primary bibliography confirm this reference. Direct opens of the JSTOR PDF and DOI destination did not return its full text. Consequently this refresh does not claim to have inspected Hartshorne's original equations, theorem number, or proof for the Macaulay/Cremona quartic. The later author-hosted research paper Singh–Walther, *Local cohomology and pure morphisms*, [PDF](https://www.math.utah.edu/~singh/publications/singh_walther_pure.pdf), Example 3.5, printed pp. 294–295, explicitly attributes the characteristic-`p` STCI result for the kernel of `k[w,x,y,z] -> k[s^4,s^3t,st^3,t^4]` to Hartshorne. The author PDF opened successfully and its text at this example was directly inspected. That is corroborating historical attribution, not a substitute for reading Hartshorne's proof. The quartic's positive-characteristic **projective** STCI status is independently covered by Moh's verified monomial-family assertion above.

## Bounded contemporary search and continuation scope

Searches included combinations of `projective curves`, `set-theoretic complete intersections`, `positive characteristic`, `algebraic closure of a finite field`, and `2025`/`2026`. No checked primary statement from this bounded search establishes STCI for every integral curve in `P^3` over `Fpbar`, or over an arbitrary algebraically closed field of positive characteristic. This is a search result, not a proof that no such theorem exists.

The recent [Mandal–Zinna publisher abstract](https://www.sciencedirect.com/science/article/abs/pii/S0021869325006295), J. Algebra **690** (15 March 2026), 101–113, DOI 10.1016/j.jalgebra.2025.10.042, concerns affine threefolds over characteristic-zero `C1` fields, with trivial conormal and a torsion Grothendieck-class hypothesis. It supplies no positive-characteristic projective transfer. Its abstract must not be merged with the different 2025 preprint audited in the earlier note.

The earlier affine/projective, lci-at-the-cone-vertex, and SCIP distinctions remain in force. No canonical repository file was changed by this refresh.


---

## Source: 2026-10-10-session-primary-literature-frontier-refresh.md

# Primary literature frontier refresh, October 10

Date: 2026-10-10. Lane: literature_frontier_refresh.
Status: **PRIMARY SOURCE SCOPES REFRESHED; bounded literature assessment**.
No canonical frontier file was edited by this lane.

The controlling records inspected were the current
[literature ledger](../LITERATURE_LEDGER.md), the
[October 6 source audit](2026-10-06-session-literature-refresh.md), the
[positive-characteristic proof audit](2026-10-06-positive-characteristic-literature-audit.md),
and both October 10 acceptance records, including the
[resumed continuation acceptance](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-continuation-results-acceptancemd).
The latter records the accepted genus-one exclusion, genus-two bisection
exclusion, and three-distinct-contact trisecant exclusion for fixed
C0=[s^4:s^3t:s t^3:t^4]. Its endpoint trisecant remainder and higher-degree
remainder are retained. Literature scopes below do not independently certify
those repository proofs.

## 1. Current open-status evidence has precise dates and access limits

- Eisenbud--Harris, *The Practice of Algebraic Curves* (AMS, 2024),
  [official publisher preview](https://www.ams.org/bookstore/pspdf/gsm-250-prev.pdf),
  Example 3.13, printed pp.64--65, retains the two-arbitrary-equation
  radical question for the literal fixed C0. The same passage records a
  one-parameter family of projective orbits of smooth rational quartics.
  Consequently a proof for the displayed deleted-middle-monomial projection
  must not be declared a proof for all smooth rational quartic embeddings.
  Indexed publisher text was refreshed; direct PDF opening failed.
- Murayama, [MA665 author notes](https://www.math.purdue.edu/~murayama/ma665.pdf),
  Spring 2026, **compiled April 28, 2026**, Question 2.6.40 and Remark
  2.6.41, printed p.199, still state the irreducible projective-curve
  question as open. Both the compilation date and the numbered question
  were independently refreshed in indexed primary text. This is dated
  author evidence, not a theorem proving that later work cannot exist.
- Murayama's [companion author notes](https://www.math.purdue.edu/~murayama/LocalCohomology.pdf),
  section 5, printed p.5, Open Question and Example 11, retain the
  characteristic-zero rational quartic question and distinguish the
  affirmative positive-characteristic result. The final displayed coordinate
  has a typo in indexed text; the intended standard curve is identified by
  the surrounding description. Direct PDF opening failed; indexed primary
  text was inspected.
- Hartshorne--Polini, [*Quasi-cyclic modules and coregular sequences*](https://arxiv.org/html/1907.05472),
  abstract, introduction and Example 7.10(1), retain the universal irreducible
  P3 question and the characteristic-zero quartic question. Example 7.10(1)
  explicitly distinguishes characteristic p>0. Their module conditions are
  criteria and necessary conditions, not proof of their universal existence.

The bounded searches on this date found no accepted primary resolution of
the universal question or the unrestricted fixed-C0 question. This negative
search result is **not** proof of open status, an exhaustive novelty search,
or a reason to dismiss an unindexed argument.

## 2. Exactly what the classical quartic-carrier exclusions establish

| Primary source and actual location | Verified scope and relevant boundary |
|---|---|
| Craighero--Gattazzo, [1986 Numdam PDF](https://www.numdam.org/item/RSMUP_1986__76__177_0.pdf), pp.177--178 and Proposition 4, p.187 (PDF zero-based p.11) | The literal Cremona quartic is not the intersection of **two quartic surfaces**, over an algebraically closed field of characteristic different from 2 and 3. It excludes (4,4), not (4,b) for every b. The paragraph immediately before Proposition 4 observes that an integral quartic containing C0 cannot have C0 as a double curve, using its trisecants. |
| Craighero--Gattazzo, [1989 Numdam PDF](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf), title, abstract and pp.171--173 | Over an algebraically closed characteristic-zero field, every smooth rational quartic is excluded on **every cubic surface**, with a mate of arbitrary degree. This is an all-(3,b) result, not an all-(4,b) result. |
| Jaffe, [actual arXiv PDF](https://arxiv.org/pdf/alg-geom/9410008), Theorem 11.11, printed p.45 (zero-based p.44); [HTML source](https://arxiv.org/html/alg-geom/9410008v1) | A quartic with **rational singularities** cutting a smooth curve set-theoretically with an arbitrary surface forces the curve to be linearly normal. The displayed theorem is over C; the introduction states characteristic-zero scope. The proof replaces a mate singular along C by g+fh, so no hidden generic-smoothness restriction is imposed on the original mate. Nonnormal quartic carriers are not covered by a rational-singularity hypothesis on their finite normalization alone. |
| Ellia, [actual arXiv PDF](https://arxiv.org/pdf/1409.3801), Corollary 16 and Remarks 17--18, printed p.8; [HTML source](https://arxiv.org/html/1409.3801) | Characteristic-zero **primitive** STCI numerical restrictions retain (4,7), along with nine higher-degree pairs. Thus this source does not already exclude all quartic carriers. Primitive means local containment in a smooth surface; the entirely thick branch is outside this theorem. The retained numerical pair is not a constructed surface pair or existence theorem. |

Jaffe's Theorem 13.1 and its finite degree list require that the two surfaces
have **no common singular points**. Removing that hypothesis is not licensed
by the quartic theorem or by the existence of the finite list. These sources
provide no theorem forcing an arbitrary presentation of C0 to use a quartic
carrier.

## 3. The conductor literature overlaps with the new lane

Hartshorne--Polini, [*Divisor class groups of singular surfaces*](https://arxiv.org/pdf/1301.3222)
([HTML](https://arxiv.org/html/1301.3222)), supplies these interfaces:

- Example 6.10, pp.20--21: the smooth nine-point plane model with
  H=(4;2,1^8), elliptic conductor and a double line. Example 7.16,
  pp.29--30, computes its smooth STCI curves.
- Corollaries 7.9--7.10, p.27: ordinary singularities and ordinary nodes,
  characteristic zero, and C not contained in the singular locus. They exclude a
  rational quartic, but not all singular-normalization degenerations.
- Remarks 2.5, 3.2, pp.4,7: for singular normalization the conductor quotient
  applies to G={d in APic(X): pullback(d) in Pic(S)}. A Cartier multiple
  upstairs is additional data.
- Example 7.13 and Remark 7.14, pp.28--29: a special ruled cubic has
  root-of-unity STCI orders of arbitrary size; the STCI locus need not
  be open or closed.

**Continuation inference.** These are appropriate interfaces for an actual
Cartier multiple and full conductor descent. They do not justify a bounded
mate-order search.

Ronconi, [*Sui monoidi di ordine quattro di P3 singolari in codimensione uno*](https://www.numdam.org/item/RSMUP_1985__74__23_0.pdf),
summary and introduction, printed p.23, proves that each complex quartic
monoid singular in codimension one has **some** curve that is not STCI on
that prescribed monoid. That quantifier does not identify the curve with C0
or exclude C0 on every quartic. The prior
[1984 monoid paper](https://www.numdam.org/item/?id=RSMUP_1984__72__49_0)
classifies carriers on which all curves are STCI. Its full PDF was
inaccessible here; the 1985 introduction identifies characteristic different
from 2 and 3. It is not used as an uninspected all-quartic exclusion.

## 4. Positive characteristic and apparent modern shortcuts remain separate

The [independent positive-characteristic refresh](#source-2026-10-10-session-positive-characteristic-primary-refreshmd)
records current primary abstract checks. Verified affirmative projective
families must not be enlarged to all integral projective curves. The earlier
exact cone-vertex and infinity-compatibility objections remain relevant.

Live arXiv histories were refreshed on October 10:

- [Mandal--Zinna, 2511.07589](https://arxiv.org/abs/2511.07589)
  still displays only v1, submitted November 10, 2025. Its claims concern
  affine local-complete-intersection curves and surfaces. The existing exact
  proof audit is not repaired by refreshing the unchanged abstract.
- [Erdoğdu, 2209.04489](https://arxiv.org/abs/2209.04489)
  still displays only v1, submitted September 9, 2022. The October 6
  countercheck of its unique-maximal-to-unique-prime inference remains an
  obstruction to importing the claimed negative resolution.
- [Hassanzadeh, 2409.05705](https://arxiv.org/abs/2409.05705)
  displays v2, February 12, 2025, with residual-intersection scope and stated
  forthcoming JLMS publication. Perfect subideals of the same radical are
  not automatically ideals generated by two forms.

No corrected proof of the two audited v1 shortcuts was identified. This is a
version-history observation, not a claim that no correction exists outside
the inspected records.

## 5. Bounded novelty assessment and search provenance

Among the **checked primary sources**, none states the new complete
fixed-C0 genus-one quartic exclusion or an exclusion on all integral quartic
carriers with arbitrary mate degree. Jaffe treats rational-singularity
quartics; Hartshorne--Polini treat ordinary carriers and specified examples;
Ellia still retains the primitive (4,7) possibility. These comparisons
identify a meaningful scope extension in the repository proof, while **not
certifying novelty**. A complete theorem excluding every quartic carrier
would still leave arbitrary higher-degree and entirely thick presentations.

Search families included the exact Cremona/Macaulay curve names; rational
quartic with quartic carrier and arbitrary mate; (4,7); Jaffe, Ellia and
Craighero--Gattazzo citation chains; Ronconi quartic monoids; and projective
space-curve STCI with 2025/2026. Dated primary author statements and actual
theorem hypotheses control this note. Crawl-time labels, secondary summaries,
TheoremDB, forums and aggregators were discovery results, not theorem or
novelty evidence. Four overly restrictive arXiv/date searches returned no
hits; broader queries and direct identifier/version opens followed. Empty
searches are access/search limitations.

Further novelty work should trace citations of the quartic and primitive
papers, and compare nonnormal genus-one and genus-two degenerations directly.
It should not infer a published all-quartic theorem from a paper merely
mentioning quartic surfaces, or infer universal resolution from a new
bounded-carrier exclusion.



---

## Source: 2026-10-10-session-quartic-normal-bundle-independent-audit.md

# Fixed quartic normal bundle: independent Jacobian certificate

Date: 2026-10-10. Auditor: `quartic_normal_bundle_audit`.
Status: **PROVED HERE as an independent verification of the existing P-009**.
The possible application to a normalization ribbon is stated separately and
requires its geometric hypotheses; this note makes no global STCI claim and
edits no canonical frontier file.

Let `k` be algebraically closed of characteristic zero, and let

    j:P1 -> P3, [s:t] -> [s^4:s^3t:st^3:t^4].

Then `j` is a closed immersion. Its image is covered by `x0!=0` and
`x3!=0`. On the first chart the inverse parameter is `x1/x0=t/s`; on
the second it is `x2/x3=s/t`. These chart maps identify the image with
the corresponding affine lines, including both endpoints. In particular
the curve is smooth and its normal sheaf is a rank-two vector bundle.

## 1. Euler and homogeneous derivative presentation

The pulled-back Euler sequence and the tangent sequence give

    0 -> O_P1(1)^2 -> O_P1(4)^4 -> N_C0/P3 -> 0.

To justify the left term, the two homogeneous partial derivative columns
map `O(1)^2` into `O(4)^4`. Their span contains the radial Euler column
since `s*d_s j+t*d_t j=4*j`; after quotienting that radial column the
induced map is the actual tangent map. Characteristic zero ensures `4`
is invertible. The resulting rank-two subbundle is therefore precisely
the preimage of `T_P1` in the Euler bundle. Dualizing yields

    0 -> N_C0/P3^* -> O_P1(-4)^4 --J--> O_P1(-1)^2 -> 0,

where

    J = [[4s^3,3s^2t,t^3,0],
         [0,s^3,3st^2,4t^3]].

The `4x2` cubic matrix

    V = [[-2t^3,0],
         [3st^2,t^3],
         [-s^3,-3s^2t],
         [0,2s^3]]

satisfies `JV=0`. Its six maximal minors are, in row-pair order,

    -2t^6, 6s^2t^4, -4s^3t^3,
    -8s^3t^3, 6s^4t^2, -2s^6.

They have no common projective zero: the first is nonzero when `t!=0`
and the last when `s!=0`. Thus `V` gives a rank-two subbundle

    O_P1(-7)^2 -> ker(J)=N_C0/P3^*.

It is an isomorphism on every fiber, hence an isomorphism of vector
bundles. Therefore

    N_C0/P3 = O_P1(7) (+) O_P1(7).

This proves the splitting without a generic-rank argument or a computer
inference. The exact Macaulay2 companion checks the displayed identities
and projective rank conditions over `QQ`. All coefficients and minors
remain valid after any extension of an algebraically closed
characteristic-zero ground field.

## 2. Independent quadratic-kernel check

Write a potential degree-two derivative syzygy as

    u0=a0 s^2+a1 st+a2 t^2,
    u1=b0 s^2+b1 st+b2 t^2,
    u2=c0 s^2+c1 st+c2 t^2,
    u3=d0 s^2+d1 st+d2 t^2.

Comparing the six coefficients in each row of `J*u=0` gives

    4a0=0, 4a1+3b0=0, 4a2+3b1=0,
    3b2+c0=0, c1=0, c2=0,
    b0=0, b1=0, b2+3c0=0,
    3c1+4d0=0, 3c2+4d1=0, 4d2=0.

The only residual pair is `c0=-3b2`, `b2+3c0=-8b2=0`, so all
twelve coefficients vanish. The companion verifies that the determinant
of this `12x12` coefficient matrix has absolute value `2^15`.
Consequently `H0(N^*(6))=0`, independently excluding `O(6)(+)O(8)`.
The two cubic columns above then provide the full splitting directly.

The repository already contains this splitting as P-009 in
[`RESEARCH_RECORD.md`](../RESEARCH_RECORD.md), via a two-chart conormal
calculation and [`verify_normal_bundle.py`](../computations/verify_normal_bundle.py).
The new source supplies a short, independently runnable certificate under
the currently available Macaulay2 runtime. It does not count the old
result as a new theorem.

## 3. Conditional ribbon obstruction and its exact limitation

For any line bundle `J0=O_P1(-8)`, the proved splitting gives

    Hom_C0(I_C0/I_C0^2,J0)
        = H0(O_P1(-1))^2 = 0.

Hence a scheme morphism `r:R -> P3` whose reduced restriction identifies
`R_red` with `C0`, and whose square-zero ideal is `J0`, cannot induce a
nonzero global map

    I_C0/I_C0^2 -> J0.

If `r` is generically an immersion of the ribbon, this map is necessarily
generically nonzero, so such an `r` cannot exist. The implication follows
directly by pulling back the ambient ideal into the nilpotent ideal:
products of two pulled-back ideal sections vanish, so the map factors
through the conormal bundle. If the map were zero at the generic point,
the morphism would factor there through the reduced curve and could not
be a ribbon immersion.

For the root's proposed application, establishing the *global* ribbon,
its square-zero ideal `O(-8)`, and generic immersion is indispensable.
In particular a doubled Weil divisor on a singular surface need not be
a ribbon without the Cohen--Macaulay and duality argument. This audit
does not replace those required geometric checks by tangent data.

Here is that general ribbon argument, independently of the unresolved
carrier hypotheses. Suppose a normal surface `S` contains a smooth
reduced integral curve `c`, the effective Weil divisor `2c` is Cartier,
and `D=2c` is Cohen--Macaulay. Normality identifies `I_c` with the
functions of valuation at least one at the generic point of `c`, and
`I_D=O_S(-2c)` with valuation at least two. Consequently
`I_c^2 subset I_D`, so `J=I_c/I_D` is square-zero. The sequence

    0 -> J -> O_D -> O_c -> 0

and the depth lemma give depth one for `J` at every point of `c`.
Equivalently, any parameter of the smooth local curve ring is a
nonzerodivisor on `J`: the associated primes of the CM curve `D` are
its generic points, and the parameter avoids the sole generic prime.
The generic rank of `J` over `c` is one, from the length-two quotient of
the normal-surface DVR at the generic point. Thus `J` is a torsion-free
rank-one sheaf on a smooth curve and therefore a line bundle. This
proves that `D` is a ribbon; no regularity of `S` at all points of `c`
is required for this step.

If `S` is additionally Gorenstein near `c`, Cartier adjunction makes
`omega_D=omega_S(D)|D` invertible. Finite duality for `c subset D` gives

    omega_c=Hom_D(O_c,omega_D)
           =J tensor omega_D|c,

because the annihilator of `J` in a ribbon is `J` itself. Therefore

    J=omega_c tensor (omega_D|c)^(-1).

In particular, **conditional on** `c=P1`, `2c~2H`, `H.c=4`, and
`K_S.c=-2`, one obtains `deg(omega_D|c)=6`, hence `J=O(-8)`.
A finite normalization morphism to a quartic carrier is an isomorphism
away from the conductor. If `c` is not contained in that conductor,
its restriction to `D` is generically a ribbon immersion, so the
nonzero-conormal-map contradiction applies. This establishes the
root's proposed mechanism from these explicit hypotheses. Verifying
that every carrier in the intended stratum satisfies them remains the
root's separate geometric audit.

## 4. Exact execution evidence

The source is
[`verify_session_quartic_normal_bundle_2026_10_10.m2`](../computations/verify_session_quartic_normal_bundle_2026_10_10.m2).
Its command, source hash, raw stdout/stderr, exit code, and assertion count
are recorded in the sibling validation directory
`research/validation/2026-10-10-quartic-normal-bundle-independent-audit/`.


---

## Source: 2026-10-10-session-relative-morse-conductor-branches-independent-audit.md

# Relative formal Morse splitting preserves the actual conductor branches

Date: 2026-10-10. Author: `relative_morse_axis_audit`.
Status: **PROVED HERE / independent local audit**. This verifies the local
claim in section 4 of the
[nonendpoint trisecant obstruction](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-nonendpoint-trisecant-conic-obstructionmd).
It does not by itself verify that note's global hypotheses or remaining
steps. No canonical frontier file is edited.

## 1. Precise statement

Let k be an algebraically closed field of characteristic zero. In the
completion of a smooth threefold at a closed point take coordinates
`u,v,r`. Suppose a surface germ is given by

    F = uv + r h(u,v,r) = 0,

and the Cartier divisor cut out by `r=0` has the two actual reduced
branches `(u,r)` and `(v,r)`. Suppose the surface is smooth or has a Du Val
singularity. Then it is smooth or of type A_n. In the latter case the
strict transforms of the two specified branches meet opposite ends of
the minimal crepant exceptional chain, transversely. For A_1 they meet
the same exceptional curve at two distinct points.

The assertion concerns these specified branch ideals, rather than two
arbitrary smooth curves on an A_n surface. The parameter-preserving
argument below supplies precisely that distinction.

## 2. A direct parameter-preserving splitting algorithm

The power series ring `k[[u,v,r]]` is complete for the r-adic topology.
Suppose at some stage, with coordinates `x,y,r`, the equation has the
form

    F = xy + g(r) + r^N H(x,y,r),       N >= 1.

Decompose the error exactly as

    H(x,y,r) = a(r) + x A(x,y,r) + y B(x,y,r).

This is always possible by separating the constant term in x,y and
then allocating each remaining monomial to x or y. Set

    X = x + r^N B(x,y,r),
    Y = y + r^N A(x,y,r).

These are invertible formal coordinates with r fixed: their x,y
Jacobian is the identity modulo the maximal ideal. An exact identity
gives

    F = XY + g(r) + r^N a(r) - r^(2N) A(x,y,r)B(x,y,r).

After expressing x,y in the new coordinates, the last term is still
divisible by `r^(2N)`. Thus each step absorbs the constant error into
g and at least doubles the r-adic error order. Starting with `N=1`,
the coordinate changes and g converge in the r-adic topology. Their
limits give invertible formal coordinates satisfying

    x = u mod r,       y = v mod r,
    F = xy + g(r).

In particular the original branch ideals are exactly

    (u,r) = (x,r),       (v,r) = (y,r).

There is no appeal here to a splitting lemma that might silently
change the divisor `r=0` or its branch labels.

If the surface is singular, the linear part of F vanishes, so g has
order at least two. Also g cannot be identically zero: `xy=0` has a
nonisolated singular locus and is not a Du Val surface. Write

    g(r) = r^m epsilon(r),       m >= 2,       epsilon(0) != 0.

Multiplication of the defining equation by a unit, followed by
rescaling one of x,y by a unit, gives `xy=r^m` (a constant sign is
absorbed too). This final normalization need not be the identity
modulo r, but it leaves the two branch ideals `(x,r)` and `(y,r)`
unchanged. Hence the pair consisting of the surface and its specified
two branches is the standard A_(m-1) pair. If g has order one, the
surface is smooth. The normal-form classification agrees with
[Reid's Du Val notes, Table 1 and section 2.2](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).

## 3. Explicit resolution and branch endpoints

For `xy=r^m`, the standard minimal resolution is covered by m smooth
charts with coordinates `(a_i,b_i)`, indexed by `i=0,...,m-1`, and
map

    x = a_i^(i+1) b_i^i,
    y = a_i^(m-i-1) b_i^(m-i),
    r = a_i b_i.

The transition from chart i to i+1 is

    a_(i+1) = 1/b_i,
    b_(i+1) = a_i b_i^2.

Each displayed monomial formula is compatible with this transition
and satisfies `xy=r^m`. These charts are the regular toric subdivision
of the original cone: in the quotient lattice
`N=Z^2+(1/m)(1,-1)Z`, subdivide between `(0,1)` and `(1,0)` by the rays
`(j/m,1-j/m)`, `j=1,...,m-1`. Adjacent rays form a lattice basis, and
the subdivided fan has the same support, so its map to the original
affine toric surface is proper and birational.

The exceptional curves form a chain of m-1 curves. The j-th one is
`a_(j-1)=0` in chart j-1 and `b_j=0` in chart j; its normal-coordinate
transition is the square of the coordinate on its P1, giving degree
-2. The residue canonical form pulls back as

    (dx/x) wedge dr = da_i wedge db_i,

so the resolution is crepant. With only (-2) exceptional curves it is
minimal. Thus it is the minimal crepant A_(m-1) resolution.

The branch `y=r=0` has strict transform `b_0=0` in chart 0 and meets
the first exceptional curve `a_0=0` transversely at that chart's
origin. The branch `x=r=0` has strict transform `a_(m-1)=0` in the last
chart and meets the last exceptional curve `b_(m-1)=0` transversely
at that chart's origin. Neither strict transform meets any other
exceptional component. For m=2 the two chart origins are distinct
points on the single exceptional P1.

## 4. Audit conclusion and small wording qualification

The local all-length A-chain assertion used by the nonendpoint
trisecant argument passes. In particular a transverse crossing of the
two reduced actual conductor branches cannot lead to a D_n or E_n
configuration, and the branch belonging to B attaches at an endpoint
of the A-chain for every n.

The only wording qualification is that one first obtains
`xy+g(r)`, with coordinate changes exactly zero modulo r. Replacing g
by a pure power uses a harmless unit rescaling (or a reparameterization
of r); it preserves the specified branch ideals. This qualification
does not alter the geometric endpoint conclusion or any subsequent
intersection calculation.


---

## Source: 2026-10-10-session-results-acceptance.md

# October 10 root acceptance and continuation frontier

The universal integral projective-curve STCI problem and the unrestricted
characteristic-zero problem for fixed
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. This record accepts the proof
and audit chains below, superseding the corresponding open genus-one
language in the October 9 acceptance and the latest-pause rundown.
No novelty claim is made without a separate literature assessment.

Unless explicitly broadened, statements concern fixed `C0` over every
algebraically closed field of characteristic zero and an integral quartic
carrier `X` in `P3`. They do not impose a bound on the minimum carrier
degree in an arbitrary presentation. The October 9 and earlier acceptance
records retain their historical proofs, exact runs and scopes.

## 1. The entire genus-one quartic-carrier lane is excluded

**PROVED HERE / independently accepted.** If the finite normalization of
an integral quartic `X` containing fixed `C0` has sectional genus one,
there is no homogeneous form `G` of any positive degree with
`V(X,G)=C0` set-theoretically. There is no additional first-normal-order,
bounded mate degree, reduced conductor or displayed-family hypothesis.

Root accepts the completed
[interface audit](OCT10_BISECTION_AND_ENDPOINT_FOUNDATIONS.md#source-2026-10-10-session-genus-one-interface-independent-auditmd)
and [remaining-partitions audit](2026-10-10-session-ribbon-repeated-partitions-independent-audit.md)
after reading their arguments, the owner partition proof and the actual
exact companions. The proof is the following complete chain:

1. A mate forces the whole inverse image to have support the unique
   embedded smooth lift `c`; normal-surface Cohen--Macaulay purity removes
   extra isolated points. Its actual pulled-back divisor is `b c`, with
   coefficient fixed by degree, not merely set-theoretic support.
2. The accepted rationality, canonical adjoint and `D5` saturation proofs
   make the normalization an ADE del Pezzo of degree four. The entire
   exceptional type is `4A1` or `A3+2A1`, the mate degree is even, and
   `2c~2H` is an actual Cartier equivalence.
3. The complete anticanonical embedding is a normal two-quadric surface
   in `P4`. Restriction to `c` is an isomorphism on its five linear
   sections. Thus its coordinates are exactly the five quartic monomials,
   while the original projection deletes `Y2=U^2V^2`. The center is outside
   the surface. The primary anticanonical theorem includes singular ADE
   models; no smooth del Pezzo hypothesis is being transferred.
4. The actual Cartier double `2c` is a ribbon even at singular points.
   Its nilideal is `O_P1(-6)`, and its conormal quotient gives the entire
   quadratic net `M(d) eta=0`, `eta1^2-eta0 eta2 != 0`. No actual ribbon
   or surface pencil is omitted by this parameterization.
5. The entire conductor is the actual plane conic `(L,R)`, including
   singular and nonreduced schemes. Full inverse support requires
   `rad(L_C)` to divide the other projection derivative. The nonzero
   binary quartic `L_C` has zero middle coefficient. Its five root
   partitions are squarefree, `[2,1,1]`, `[3,1]`, `[2,2]`, and `[4]`.
6. Squarefree and all `[2,1,1]` cases are excluded by the separately
   checked derivative map, including its only common-basepoint locus.
   The [complete repeated-partition proof](2026-10-09-session-ribbon-repeated-partitions-complete.md)
   and separate audit exclude every remaining partition. Endpoints,
   zero direction coordinates and the derivative-invisible coefficient
   are retained; only center-preserving diagonal changes and reversal
   are used to normalize the actual projection.
7. For `[3,1]` and `[2,2]`, independent equality of the complete bilinear
   net/support ideals with explicit linear ideals excludes every hidden
   determinant branch. Actual singular lines eliminate `[4]` and the
   surviving `[3,1]` pencil. The sole `[2,2]` pencil has a smooth conic
   conductor and nonconstant trace-square/norm ratio. Any positive
   power descending would force that ratio to be constant, so every
   exponent is excluded, including the split quadratic-cover case.

The independent computation is over `QQ` and extends to every
characteristic-zero field. Factorization and root-of-unity arguments use
the algebraically closed constant field. The upstream complex ADE input
retains its separately stated finite-coefficient descent. This result
must not be enlarged to arbitrary smooth rational quartics: their
projection centers need not be equivalent to the fixed deleted-middle
center.

Consequently the only remaining integral quartic-carrier normalization
lane for fixed `C0` is sectional genus **two**, using the already accepted
normal, genus-zero, smooth-normalization and nonrational exclusions.
This consequence is still not an unrestricted all-degree theorem.

## 2. New genus-one exact evidence and corrected attribution

The new independent [M2 interface companion](../computations/verify_session_genus_one_211_interfaces_2026_10_10.m2)
verifies **42 exact identities** for the entire `[2,1,1]` calculation.
The separate [M2 repeated-partition companion](../validation/2026-10-10-repeated-partitions-independent-audit/countercheck.m2)
verifies **29 exact conditions**, including full ideal equality and a
different conductor section from the owner's calculation.

Root copied their exact source bytes into a separate snapshot cwd and
observed both terminal passes; actual subprocess streams, commands,
elapsed times, hashes and copied sources are retained in the
[root replay manifest](../validation/2026-10-10-genus-one-root-replay/execution-manifest.json).
These are two additional executions of two source paths, not four new
mathematical verifiers. The proof's geometric quantifiers are supplied
by the written audits, not by the number of identities.

The older `[2,1,1]` note incorrectly attributed some checks to its
current Python companion. The new interface audit explicitly corrects
that attribution and supplies the missing exact certificate. Historical
passes must not be represented as checking identities absent from their
source. Protected-name and parser scaffold failures, and the failed
SymPy import, remain in the separate execution records. No dependency
installation or historical failure deletion was performed.

## 3. Genus-two actual conductor-line theorem

**PROVED HERE / independently accepted without a mate hypothesis.**
Root accepts the [entire-conductor audit](2026-10-10-session-genus-two-entire-conductor-independent-audit.md).
In the accepted genus-two situation the resolution is rational,
`L^2=4`, and `K_M.L=-2`. Every singularity of the normal surface `S`
is rational, without assuming `K_S` Cartier or Q-Cartier. Negative
canonical degree gives `H2(O_S)=0`; Leray and rationality of `M`
give `R1 sigma_*O_M=0`. Proper duality then gives
`R sigma_*omega_M=omega_S`.

Quartic hypersurface adjunction and finite duality identify the actual
conductor ideal `I` with `nu_*omega_S`. Its maximal Cohen--Macaulay
property makes the downstairs conductor pure CM. The exact polynomial
`chi(O_X(m))-chi(I(m))=m+1` forces that entire scheme to be a reduced
line `Gamma`, with no embedded or isolated points.

Natural MCM biduality and closed-immersion duality give
`nu_*O_S/O_X=omega_Gamma=O_P1(-2)`. The entire upstairs conductor `D`
is therefore a finite flat double cover with algebra

    p_*O_D=O_P1 direct-sum O_P1(-2),
    w^2=delta,       delta in H0(O_P1(4)).

The trace splitting is global. Singular, split and nonreduced covers,
including `delta=0`, are retained. `D` is connected Gorenstein of genus
one and hyperplane degree two, but is not asserted Cartier on `S`.
General transverse-plane genus proves generic quartic order exactly two
along `Gamma`. This is a structural reduction, not a mate exclusion.

## 4. Accepted markings and a bounded section-case exclusion

The [marking audit](2026-10-10-session-genus-two-marking-and-section-pause-audit.md)
accepts the remaining ruled/plane marking steps of the
[adjoint model](2026-10-09-session-genus-two-adjoint-conic-model.md),
including the exact vertical `D8` lattice. The complete pencil
`f=K_M+L` is rational and basepoint-free, `f^2=0`, `L.f=2`.
Both mate strata must remain:

    (lambda,q)=(0,4): c#^2=0, f.c#=2;
    (lambda,q)=(1,3): c#^2=1, f.c#=1.

**PROVED HERE / bounded exclusion.** In the second stratum, the
[marked-prime audit](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-lambda-one-marked-prime-auditmd)
and [independent no-zero-horizontal audit](2026-10-10-session-genus-two-no-zero-horizontal-independent-audit.md)
exclude both one- and two-proper-horizontal-line cases when the
degree-zero horizontal prime `B=e0-e_i-e_j` is absent. A survivor
therefore requires `B` present. The anti-nef cycle pulled back from a
uniformizer of the smooth embedded curve is integral and has contact
coefficient one; the proofs retain full predecessor and descendant
chains, not a count of unused centers alone.

The `B`-present free-child and satellite cases remain open in these
proofs. Internal chain attachments invalidate the proposed star shortcut.
The bisection stratum remains open as well. The separate frozen
[source line-budget note](2026-10-10-session-genus-two-lambda1-horizontal-line-budget.md)
retains its old pending two-line label; the independent audit supplies
the bounded acceptance without rewriting that historical source.

## 5. The actual normal ambient conic model is accepted

**PROVED HERE / independently accepted without a mate.** Root accepts
the [blowup-lift independent audit](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-blowup-lift-normality-independent-auditmd)
after reading its complete proof and checking the cited primary proper
duality and blowup inputs. It accepts the
[owner proposal](2026-10-10-session-genus-two-blowup-lift-normality-proposed-audit.md)
at its recorded hash; the frozen proposal label is superseded by this
separate audit and acceptance, not silently rewritten.

The actual ambient equations of the conductor line correspond through
natural rank-one canonical-duality identifications to a basis of the
complete basepoint-free adjoint pencil. They have a globally regular
common factor `g` in `H0(-K_M)`. The pulled-back ambient line ideal is
exactly `O_M(-div(g))`, including absence of a residual base scheme.
Consequently the morphism lifts to `B=Bl_Gamma(P3)` and has as its image
the actual integral strict transform `T` of `X`.

Exact generic order two gives

    T~4H_B-2E_B,        omega_T=O_T(-E_B),
    rho*omega_T=omega_M.

The proper-duality trace `rho_*omega_M -> omega_T`, untwisted using the
last equality, gives a generically nonzero `O_T`-linear map
`rho_*O_M -> O_T`. Its restriction to `O_T` is a nonzero global constant
because `T` is proper integral. Rescaling forces equality of the two
algebras in the common fraction field, proving normality. This does not
assume normality or higher-direct-image vanishing in advance. Properness
of the target is essential; the audit preserves the affine cusp
counterexample to a version omitting it. Compatible canonical forms
then give an actual crepant equality, hence `T` has ADE singularities.
The original finite normalization `S` need not be Gorenstein.

The ruling of the blowup is the actual family of planes through `Gamma`,
and `T` cuts an actual conic in every fiber. Only vertical `(-2)` curves
are contracted in `M->T`; horizontal `(-3)` sections can be contracted
in `T->S` instead. On the smooth lift the common-factor equality gives

    tau=length(Gamma intersect C0)=4-f.c#.

Thus the bisection stratum is an actual length-two secant/tangent line
case and the section stratum is an actual length-three trisecant case,
including repeated contacts. Length three forces the line onto the
unique smooth quadric containing `C0` and into its degree-three ruling.
This accepted normal conic model excludes neither mate stratum by
itself. Further residual-conductor and double-pencil arguments are
separate ongoing proof obligations.

## 6. Retained unrestricted scope and evidence

The principal MF6 at-most-630-point necessary locus is not a classified
carrier list. The 22 second endpoint-family points of degrees `3,4,15`
retain every lower lift line. Other ancestor strata, early `e=2` defects,
higher minimum carrier degrees, entirely-thick presentations, and the
totally ramified split-sextic boundary remain open. Neither the entire
genus-one theorem nor a future all-quartic theorem would settle those
unrestricted cases.

The October 9 seal's **97 distinct latest-PASS sources / 110 indexed
executions** and **2006 integrity / 313 local-link checks** remain
historical frozen counts. New records are separately indexed and are
not silently added. Live HEAD is `406d63db72000a3951497a0ba2a8fbfbc13e8ead`,
title `2026-10-09 afternoon limit reached`; older morning HEAD references
are historical. Root performed no Git mutation.


---

## Source: 2026-10-10-session-weighted-normalization-and-double-ribbon-obstruction.md

# Weighted normalization and the forbidden genus-seven double ribbon

Date: 2026-10-10. Author: `bisection_weighted_normalization`.
Status: **PROVED HERE, supplied for root acceptance**. This is a separate
structural record of the attempted weighted-incidence approach and the
stronger obstruction that supersedes it. No canonical frontier is edited.
All assertions below concern the fixed smooth rational quartic

    C0=[s^4:s^3t:st^3:t^4]

over an algebraically closed field of characteristic zero. The normal-bundle
calculation itself works in characteristic different from two. The proof
does not establish the unrestricted C0 or universal STCI question.

The root and another independent audit had already identified the same
ribbon obstruction when this author reported it. Agreement is not the
proof; the exact ring and conormal arguments below are the evidence. The
[child conormal audit](#source-2026-10-10-session-weighted-ribbon-conormal-independent-auditmd)
checks the complete CM, Euler, derivative, and generic-immersion interfaces.

## 1. Accepted inputs and the original weighted-ring target

Let X be an integral nonnormal quartic whose normalization S has sectional
genus two, and let H be the pulled-back ambient hyperplane. Write
P=k[x0,x1,x2,x3], A=P/(F4), and

    B=direct-sum_{m>=0} H0(S,O_S(mH)).

The accepted entire-conductor theorem gives an actual line Gamma with
ambient ideal (l0,l1), and an exact sequence

    0 -> O_X -> nu_*O_S -> O_Gamma(-2) -> 0.

The two l_i are independent linear forms. Since H1(X,O_X(m))=0 for every
integer m (the quartic hypersurface restriction sequence on P3 proves
this), taking global sections gives an exact sequence of graded P-modules

    0 -> A -> B -> (P/(l0,l1))(-2) -> 0.

In particular B is generated as a P-module by 1 and any nonambient
quadratic section Q. The quotient generator is its image in degree two.
For a bisection mate, the audited second-pencil argument supplies an actual
section Q with complete Cartier divisor 2c_S and 2c_S~2H; it is nonambient
by the unique-quadric class obstruction. The ensuing ring calculation does
not assume a split or reduced upstairs conductor.

## 2. Exact two-generator P-module presentation

There are uniquely specified ambient cubics A3,B3 with

    l0 Q=A3,       l1 Q=B3

in B. Consequently l1 A3-l0 B3 vanishes in A, and hence equals a scalar
multiple of F4. That scalar is nonzero. If it were zero, unique
factorization and coprimality of l0,l1 would give

    A3=l0 C2,      B3=l1 C2.

The domain B would then imply Q=C2 from l0(Q-C2)=0, contradicting that Q
is nonambient. Scaling F4 gives l1 A3-l0 B3=F4.

The graded matrix

    P(-3)^2 -> P direct-sum P(-2),
    [[-A3,-B3],[l0,l1]]

is injective over the domain P, since its determinant is the nonzero
quartic F4. Its cokernel maps onto B, and its Hilbert series is

    (1+t^2-2t^3)/(1-t)^4.

The same series follows from the preceding conductor exact sequence:

    (1-t^4)/(1-t)^4 + t^2/(1-t)^2
       = (1+t^2-2t^3)/(1-t)^4.

Thus the surjection from the cokernel to B is an isomorphism degree by
degree. This proves the exact presentation and Cohen--Macaulayness of B,
without a separate vanishing theorem for negative twists. It also proves
that the quartic carrier equation is precisely the determinant of the
two cubic relations. This is an exact structural statement, not a generic
rank assertion.

## 3. The weighted Hilbert--Burch ideal

The cubics A3,B3 vanish on Gamma. Indeed their restrictions on the entire
upstairs conductor are l_i Q=0. The pullback of sections from Gamma to its
finite flat double cover is injective, so their downstairs restrictions
are zero. Choose quadratic forms a,b,c,d with

    A3=a l0+b l1,       B3=c l0+d l1.

For W=P[z], deg(z)=2, the weighted presentation of B is

    R0=z l0-A3,
    R1=z l1-B3,
    R2=z^2-(a+d)z+ad-bc.

The third relation follows in the domain B by multiplying by l0 and
using the first two, then canceling the nonzero l0. The two syzygies are

    (z-d)R0+b R1-l0 R2=0,
    c R0+(z-a)R1-l1 R2=0.

Equivalently R0,-R1,R2 are the maximal minors of

    [[z-d,c],[b,z-a],[-l0,-l1]].

The ideal has codimension two: away (l0,l1), it eliminates z and imposes
the nonzero quartic F4, while over (l0,l1) the monic relation R2 leaves
dimension two. Hilbert--Burch therefore gives the numerator

    1-2t^3-t^4+2t^5

over denominator (1-t)^4(1-t^2). The resulting series is precisely the
series of B, so the surjection W/(R0,R1,R2) -> B is an isomorphism.
Changing the quadratic decompositions of A3,B3 only changes R2 by the
first two relations and does not change B.

This was a finite prospective parameter incidence: for a fixed actual
length-two secant/tangent Gamma, A3 and B3 lie in I_C0(3) intersect I_Gamma,
and the determinant quartic also vanishes along C0. However this incidence
is unnecessary for the mate question because the actual double section
already yields the obstruction below.

## 4. The actual double section would be an embedded CM ribbon

Since B is generated by x0,...,x3,Q and Q is killed, B/(Q) is generated
in degree one. Its Proj is therefore closed embedded in P3. It is also
the actual Cartier zero scheme Y=div(Q) on S, whose reduced scheme is
the smooth embedded lift c_S~=C0 and whose generic multiplicity is two.
In the preceding presentation its ambient ideal is

    (A3,B3,ad-bc).

The Hilbert--Burch degrees are (3,3,4), with two degree-five syzygies.
Consequently this would be a degree-eight Cohen--Macaulay double curve
of arithmetic genus seven supported on C0.

The ribbon statement does not rely solely on this graded calculation.
A normal surface is Cohen--Macaulay, and cutting by the nonzero section
Q makes Y a CM curve. Let J be the kernel of O_Y -> O_C0. At the generic
point J has rank one and J^2=0. Globally J^2 is supported at finitely many
points and is a subsheaf of O_Y. A one-dimensional CM scheme has no
nonzero finite-support subsheaf of O_Y, so J^2=0 everywhere. J is then
an O_C0-module and has no torsion for the same reason. Smoothness of C0
implies that J is a line bundle. Thus Y is a ribbon, including every
point lying above the conductor and every ADE point on c_S.

The accepted rational resolution gives, for every integer m,

    chi(O_S(mH))=2m^2+m+1.

The Cartier sequence for Q yields

    chi(O_Y(mH))=chi(O_S(mH))-chi(O_S((m-2)H))=8m-6.

Since O_C0(H)=O_P1(4) and chi(O_C0(mH))=4m+1,

    chi(J(mH))=4m-7,
    J=O_P1(-8).

In particular the sign of the linear term of chi(O_S(mH)) matters.
Replacing it with the dualizing polynomial would give the wrong degree.

## 5. Exact normal-bundle obstruction

Let N=N_C0/P3. To calculate H0(N(-8)), dual Euler and cotangent sequences
identify its dual obstruction with the map

    K -> H0(P1,O(4)),
    K=ker[H0(O(2))^4 -> H0(O(6))],
    (P0,...,P3) |-> sum P_i d f_i,

where (f0,f1,f2,f3)=(s^4,s^3t,st^3,t^4). The first map sends P to sum P_i
f_i and is surjective, since the four degree-four monomials multiplied
by all degree-two monomials span all seven degree-six monomials. Hence
K has dimension five. A basis is

    (st,-s^2,0,0), (t^2,-st,0,0), (0,t^2,-s^2,0),
    (0,0,st,-s^2), (0,0,t^2,-st).

Dividing their differential expressions by t ds-s dt gives respectively

    s^4, s^3t, 2s^2t^2, st^3, t^4.

The map is therefore an isomorphism in characteristic different from
two. Exactness and Serre duality give

    H0(P1,N(-8))=0.

Since deg(N)=14, the splitting theorem gives N=O(7) direct-sum O(7).
Only the vanishing, rather than the full splitting, is needed below.

For any embedded ribbon Y in P3 with reduction C0 and nilideal J, the
ambient ideal I_C0 pulls back into J. Since J^2=0, this induces a
surjection

    I_C0/I_C0^2=N^* -> J=O(-8).

No nonzero map exists: Hom(N^*,O(-8))=H0(N(-8))=0. This contradicts
the actual embedded ribbon obtained from B/(Q). Thus no such quadratic
section Q with complete divisor 2c_S can exist.

An equivalent proof avoids the weighted ring completely. The Cartier
ribbon Y=div(Q) maps by normalization to P3 and extends C0. Pullback of
I_C0 again gives a global conormal map to O(-8), which is generically
nonzero because normalization is an isomorphism off the actual conductor
line and Y has nonzero generic nilpotents. The same vanishing contradicts
this. This second proof applies to any actual Cartier equivalence
2c_S~2H, even before checking whether Q is the extra quadratic generator.

## 6. Mathematical consequence and retained scope

Under the audited genus-two bisection second-pencil input, 2c_S~2H is
an actual Cartier equivalence. The obstruction therefore excludes the
entire bisection mate stratum, without any root-of-unity order bound,
conductor splitting, local fiber enumeration or reduced-cover assumption.
The split-conductor power-descent and blowup-partition reductions remain
valid intermediate results; they are superseded as a research target by
this stronger obstruction.

The genus-two section/trisecant stratum is separate. If an endpoint or
other section analysis supplies the same actual Cartier equivalence,
this obstruction applies there too. No such equivalence is asserted here
from a numerical or merely rational divisor relation. Higher carrier
degrees and the unrestricted problems remain open.

No CAS execution, new historical verifier count, literature novelty claim
or canonical-file acceptance is attached to this record. The five
displayed differential identities are exact hand computations with an
independent written audit.


---

## Source: 2026-10-10-session-weighted-ribbon-conormal-independent-audit.md

# Independent audit: the weighted ribbon conormal obstruction

Date: 2026-10-10. Auditor: `weighted_ribbon_conormal`, delegated by
`bisection_weighted_normalization`. Status: **PROVED HERE, conditional
on the accepted genus-two bisection reduction**. This is an independent
geometric audit; the identities below are written out exactly, and no
additional computer execution is asserted. No canonical frontier file
was edited by this auditor.

## 1. Inputs and the result

Work over an algebraically closed field of characteristic zero. Let

    C0=[s^4:s^3t:st^3:t^4] in P3.

Let `nu:S->X` be the normalization of an integral nonnormal quartic
containing the smooth embedded C0, and write H for the pulled-back
hyperplane bundle. In the accepted normalization sectional-genus-two
stratum,

    chi(O_S(mH))=2m^2+m+1.

Suppose the bisection mate reduction supplies an actual section

    Q in H0(S,2H),   div(Q)=2c_S,

where the reduced prime curve `c_S` maps isomorphically to C0. In
particular this is an actual effective Cartier double divisor; the
statement is stronger than a numerical doubling relation. The
[second-pencil audit](OCT10_GENUS_TWO_ENDPOINT_AND_BLOWUP_AUDITS.md#source-2026-10-10-session-genus-two-bisection-second-pencil-independent-auditmd)
supplies precisely this actual relation in its bisection mate setting.

**Conclusion:** these inputs are incompatible with the specific
embedding of C0. Consequently a mate cannot exist in this bisection
stratum. The proof does not need to classify the conductor cover,
root-of-unity ratios, exceptional graphs, or singular conic fibers.
It does not by itself exclude the separate section/trisecant stratum,
all other quartic normalizations, or carriers of higher degree.

## 2. An actual Cartier double divisor with smooth reduction is a ribbon

Set `R=V(Q)` on S. A normal surface is Cohen--Macaulay. Since Q is a
nonzerodivisor, R is a Cohen--Macaulay curve, including at every
singular point of S. At its generic point, S has a discrete valuation
ring and Q has valuation two. Thus the nilradical J of R has generic
rank one and `J^2` vanishes generically.

The coherent subsheaf `J^2` of `O_R` is therefore supported on finitely
many closed points. A one-dimensional Cohen--Macaulay scheme has no
nonzero subsheaf of its structure sheaf supported on finitely many
points: locally a nonzerodivisor in the maximal ideal annihilates no
nonzero element, whereas some power of that maximal ideal would kill
a finite-length submodule. Hence `J^2=0` everywhere.

The square-zero J is an `O_{c_S}`-module. Its torsion is again a
finite-support subsheaf of `O_R`, and therefore vanishes. Since c_S
is a smooth curve, a coherent rank-one torsion-free sheaf on it is a
line bundle. We have an exact ribbon sequence

    0 -> J -> O_R -> O_{c_S} -> 0.

This argument uses neither smoothness of S along c_S nor a local ADE
classification. It retains the entire double structure at all closed
points.

## 3. The nilradical has degree minus eight

The effective Cartier equation gives, for every integer m,

    0 -> O_S((m-2)H) -> O_S(mH) -> O_R(mH) -> 0.

Taking Euler characteristics,

    chi(O_R(mH))
      =(2m^2+m+1)-(2(m-2)^2+(m-2)+1)
      =8m-6.

The reduced curve is P1 with `H|c_S=O_P1(4)`. If `J=O_P1(d)`, the
ribbon sequence instead gives

    chi(O_R(mH))=(4m+1)+(4m+d+1)=8m+d+2.

Consequently

    J=O_P1(-8).

The sign of the linear term matters: the polynomial above is for
`O_S`, not `omega_S`. Substituting the dualizing-sheaf polynomial
`2m^2-m+1` here would incorrectly give a degree-minus-twelve
nilradical. That incorrect value is not used.

## 4. Exact Euler and derivative computation for the fixed quartic

Write `i:P1->P3` for the displayed parametrization and `N` for its
normal bundle. Twisting the pulled-back Euler sequence by O(-8)
gives

    0 -> O(-8) -> O(-4)^4 -> i^*T_P3(-8) -> 0.

By Serre duality, the dual of its map on first cohomology is

    H0(O(2))^4 -> H0(O(6)),
    (P0,P1,P2,P3) |-> P0 s^4+P1 s^3t+P2 st^3+P3 t^4.

This map is surjective. Its monomial images have t-exponents
`{0,1,2}`, `{1,2,3}`, `{3,4,5}`, and `{4,5,6}`, which cover every
exponent from zero to six. Thus

    H0(i^*T_P3(-8))=0,

and the kernel of the displayed multiplication map is
five-dimensional. The following is an exact basis of that kernel:

    P^(0)=(st,-s^2,0,0),
    P^(1)=(t^2,-st,0,0),
    P^(2)=(0,t^2,-s^2,0),
    P^(3)=(0,0,st,-s^2),
    P^(4)=(0,0,t^2,-st).

Independence is immediate from their respective free coefficients;
alternatively, the seven monomial equations for a quadratic syzygy
leave exactly these five parameters.

Now twist the tangent-normal sequence by O(-8):

    0 -> O(-6) -> i^*T_P3(-8) -> N(-8) -> 0.

The dual of its map
`H1(O(-6))->H1(i^*T_P3(-8))` sends a syzygy P to

    sum_j Pj d(fj),
    f=(s^4,s^3t,st^3,t^4).

The syzygy identity and Euler's identity make this differential a
unique quartic multiple of `t ds-s dt`. Direct differentiation of
the five basis syzygies above gives respectively

    s^4 (t ds-s dt),
    s^3t (t ds-s dt),
    2s^2t^2 (t ds-s dt),
    st^3 (t ds-s dt),
    t^4 (t ds-s dt).

Thus the dual map, in the displayed syzygy basis and the ordinary
quartic monomial basis, is exactly

    diag(1,1,2,1,1).

It is invertible in characteristic zero. The cohomology sequence,
together with the already proved vanishing of
`H0(i^*T_P3(-8))`, now yields

    H0(N(-8))=0.

For completeness, `deg(N)=4*4-2=14`. Splitting a vector bundle on
P1 and using this vanishing therefore also gives

    N=O(7) direct_sum O(7).

The vanishing, rather than the named splitting type, is the part
needed below. This exact calculation depends on the specific
missing-middle-coordinate quartic. It is not asserted for an
arbitrary projection of the rational normal quartic without checking
its analogous derivative map.

## 5. The morphism of the entire ribbon to P3 gives a contradiction

The normalization morphism followed by the inclusion X in P3 defines
a morphism `R->P3` reducing to the given embedding of c_S as C0.
The ideal of C0 pulls back into the nilradical J, and its square pulls
back to zero because `J^2=0`. Therefore it induces a global homomorphism
of vector bundles on the reduced curve,

    I_C0/I_C0^2 = N^* -> J=O(-8).

Its space of global homomorphisms is

    Hom(N^*,O(-8))=H0(N(-8))=0.

Nevertheless this homomorphism must be nonzero at the generic point
of C0. The conductor downstairs is a line, whereas C0 is a
nondegenerate quartic; C0 is not contained in that line. At its
generic point the normalization S->X is therefore an isomorphism.
There R is an actual Cartier double curve in X, and its composition
with the closed embedding X in P3 is a closed embedding. In this
neighborhood the ambient ideal of C0 generates J in the double
curve, giving a surjective conormal map at the generic point. A
generically surjective rank-one target map cannot be the zero global
map. This is the desired contradiction.

Only generic immersion is needed here. The entire R->P3 need not be
an embedding along the conductor, and no unproved global embedding
has been assumed.

## 6. Relation to the weighted normalization presentation

The separate weighted-ring reconstruction places S in
`P(1,1,1,1,2)`, with weight-two coordinate z represented by the extra
quadratic section Q. This weighted space is smooth near C0, since
at least one of its weight-one coordinates is nonzero on every
point of C0. Along the zero section its conormal bundle restricted
to C0 is

    N_C0/P3^* direct_sum O(-8).

For the specific ribbon `R=V(Q)`, the weight-two coordinate z is
identically zero on R, so its O(-8) conormal direction maps to zero
in J. The remaining map is exactly the impossible ambient P3 map
proved above. The existence of the extra O(-8) summand in the
weighted conormal therefore does not evade the obstruction.

The direct normalization-morphism proof in Section 5 does not
depend on correctness of a weighted Hilbert--Burch reconstruction.
It remains valid with the actual Cartier doubling and genus-two
Euler polynomial as its stated inputs.

## 7. Preserved scope

The bisection-stratum exclusion is conditional on the upstream
actual relation `2c_S~2H`, not on a merely numerical class equality.
Its ribbon and generic conormal arguments include singular points
of the normalization and the entire conductor. No conclusion about
the section/trisecant branch, arbitrary carrier degrees, the
unrestricted fixed-C0 STCI question, or the universal STCI question
is supplied by this note alone.
