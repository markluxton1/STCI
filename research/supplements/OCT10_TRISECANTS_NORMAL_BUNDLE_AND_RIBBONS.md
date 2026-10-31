# Historical mathematical investigations

Full original mathematical text follows. Preserve source-level evidence status, counterexamples, corrections and unresolved boundaries; no independent re-audit or result promotion.

---

## Source: 2026-10-10-session-primary-literature-frontier-refresh.md

# Primary literature frontier refresh, October 10

Date: 2026-10-10. Lane: literature_frontier_refresh.
Status: **PRIMARY SOURCE SCOPES REFRESHED; bounded literature assessment**.
No canonical frontier file was edited by this lane.

The controlling records inspected were the current
[literature ledger](../LITERATURE_LEDGER.md), the
[positive-characteristic proof audit](AFFINE_PROJECTIVE_AND_LITERATURE_LIMITS.md),
and both October 10 acceptance records, including the
[resumed continuation acceptance](../synthesis/quartic_carrier_proof.md).
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

The [independent positive-characteristic refresh](AFFINE_PROJECTIVE_AND_LITERATURE_LIMITS.md)
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

## Source: 2026-10-10-session-relative-morse-conductor-branches-independent-audit.md

# Relative formal Morse splitting preserves the actual conductor branches

Date: 2026-10-10. Author: `relative_morse_axis_audit`.
Status: **PROVED HERE / independent local audit**. This verifies the local
claim in section 4 of the
[nonendpoint trisecant obstruction](GENUS_TWO_NONENDPOINT_PROOF.md).
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
