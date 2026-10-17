# Primary literature frontier refresh, October 10

Date: 2026-10-10. Lane: literature_frontier_refresh.
Status: **PRIMARY SOURCE SCOPES REFRESHED; bounded literature assessment**.
No canonical frontier file was edited by this lane.

The controlling records inspected were the current
[literature ledger](../LITERATURE_LEDGER.md), the
[October 6 source audit](2026-10-06-session-literature-refresh.md), the
[positive-characteristic proof audit](2026-10-06-positive-characteristic-literature-audit.md),
and both October 10 acceptance records, including the
[resumed continuation acceptance](2026-10-10-session-continuation-results-acceptance.md).
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

The [independent positive-characteristic refresh](2026-10-10-session-positive-characteristic-primary-refresh.md)
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

