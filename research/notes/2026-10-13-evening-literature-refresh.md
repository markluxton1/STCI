# Literature refresh through October 13, 2026

Date: 2026-10-13, America/New_York. Lane: literature_refresh.
Status: **PRIMARY SOURCE SCOPES REFRESHED; bounded search; no universal resolution found.**
No canonical file was edited by this lane. This note does not independently
audit the new repository carrier proofs or certify their novelty.

The controlling records inspected were [the literature ledger](../LITERATURE_LEDGER.md),
[the current audited state](../AUDITED_STATE_2026-10-07.md),
[the October 10 primary refresh](2026-10-10-session-primary-literature-frontier-refresh.md),
[the October 6 positive-characteristic proof audit](2026-10-06-positive-characteristic-literature-audit.md),
and [the October 10 positive-characteristic primary refresh](2026-10-10-session-positive-characteristic-primary-refresh.md).
The current repository claims concern fixed
`C0=[s^4:s^3t:s t^3:t^4]` in characteristic zero, including all integral quartic
carriers and specified quintic normalization/projection families. Those
quantifiers remain distinct from all rational quartic embeddings and from the
universal integral-projective-curve question.

## 1. Current status: exactly what was found

No inspected primary source gives an unrestricted affirmative theorem for
every integral projective curve in `P^3`, a valid algebraically closed
characteristic-zero counterexample, or two arbitrary homogeneous defining
forms for fixed C0 in characteristic zero. This is a **bounded negative search
result**, not a proof that no unindexed resolution exists.

- David Eisenbud and Joe Harris, *The Practice of Algebraic Curves*, AMS,
  GSM 250 (2024), Example 3.13, printed pp.64–65,
  [official preview](https://www.ams.org/bookstore/pspdf/gsm-250-prev.pdf).
  The indexed publisher text again describes the two-equation question for
  the literal displayed C0 as “one of the most famous open problems in the
  theory of curves” (12 words). It also records a one-parameter family of
  projective orbits of smooth rational quartics. Direct PDF access failed;
  the indexed primary text was inspected. The 2024 date is bibliographic,
  not the search engine's crawl/publication label.
- Takumi Murayama, *MA665 Algebraic Geometry II*, Spring 2026,
  [author notes](https://www.math.purdue.edu/~murayama/ma665.pdf),
  Question 2.6.40 and Remark 2.6.41, printed p.199.
  The question asks whether irreducible projective curves are STCI, and the
  historical remark explicitly retains its open status after Perron's
  correction of Vahlen. Direct PDF opening failed; the indexed author text
  at the numbered question was refreshed. The April 28 compilation date is
  from the earlier checked primary note; it was not independently extracted
  anew in this refresh.
- Robin Hartshorne and Claudia Polini,
  [*Quasi-cyclic modules and coregular sequences*](https://arxiv.org/html/1907.05472),
  abstract, Setting 5.1, and Example 7.10(1), directly refreshed. The paper
  treats coregularity/codepth criteria and necessary conditions. Its
  characteristic-zero C0 problem remains undecided in Example 7.10(1), while
  the positive-characteristic example is affirmative. Their explicit
  wording includes “the still open problem” (4 words), referring in the
  abstract to connected curves in P3. Neither the criteria nor the
  vanishing of higher local cohomology constructs the required sequence.

The [Murayama companion notes](https://www.math.purdue.edu/~murayama/LocalCohomology.pdf),
section 5, Open Question and Example 11, were independently found again in
indexed author text. They retain the irreducible P3 question and literal
smooth rational quartic example. This is corroborating dated evidence, not
a contemporary resolution search by the notes' author.

## 2. Quartic-carrier overlap and the novelty boundary

The following actual theorem scopes were refreshed in primary full text.

| Source and exact location | Established scope | Boundary relevant here |
|---|---|---|
| Craighero–Gattazzo, [1986 original PDF](https://www.numdam.org/item/RSMUP_1986__76__177_0.pdf), introduction pp.177–178 and Proposition 4, p.187, PDF zero-based page 11 | Fixed Cremona/Macaulay quartic is not the intersection of two quartic surfaces over an algebraically closed field with characteristic different from 2 and 3 | Excludes `(4,4)`, not `(4,b)` for every b. The preceding trisecant argument prevents an integral quartic carrier from being double along C0. |
| Craighero–Gattazzo, [1989 original PDF](https://www.numdam.org/item/RSMUP_1989__81__171_0.pdf), abstract and introduction pp.171–173 | Every smooth rational quartic over an algebraically closed characteristic-zero field is excluded on every cubic surface with arbitrary mate degree | Gives all `(3,b)`, not all `(4,b)`. |
| David B. Jaffe, [*Applications of iterated curve blow-up to set theoretic complete intersections in P3*](https://arxiv.org/html/alg-geom/9410008v1), Theorem 11.11, printed p.45 | A quartic surface with rational singularities whose intersection with another surface is set-theoretically a smooth curve forces that curve to be linearly normal; displayed statement is over C | Does not cover every nonnormal quartic carrier. The proof's replacement `g -> g+fh` removes a mate singular generically along C; it does not require the original mate to be smooth there. |
| Philippe Ellia, [*Complete intersections primitive structures on space curves*](https://arxiv.org/html/1409.3801), introduction, Corollary 16 and Remarks 17–18 | Characteristic-zero primitive STCI numerical restrictions for smooth rational quartics leave ten degree pairs, including `(4,7)` | Primitive requires local containment in a smooth surface. Quasiprimitive with simultaneous isolated singularities and thick structures have separate scope. A surviving numerical pair is not an existence theorem. |

Jaffe's finite degree list and Theorem 13.1 retain the **no common singular
points** hypothesis; the introduction explicitly places that hypothesis
before its bounds. Ellia's retained higher pairs are
`(6,26),(12,18),(10,28),(9,48),(22,50),(20,67),(19,84),(18,118),(17,220)`.

Hartshorne–Polini,
[*Divisor class groups of singular surfaces*](https://arxiv.org/html/1301.3222),
Proposition 7.1, characterizes STCI on a chosen surface by `r C=m H` in
APic when C meets its singular locus in finitely many points. Corollaries
7.9–7.10 exclude a smooth rational quartic on characteristic-zero surfaces
with at most ordinary singularities and ordinary nodes, with C outside the
singular locus. Example 7.16 treats a particular rational quartic surface
with elliptic conductor, not every degeneration. These interfaces preserve
the necessity of full Cartier/conductor data. Example 7.13 and Remark 7.14
also prevent replacing arbitrary mate orders by a presumed uniformly
bounded order from an open/closed-locus argument.

**Bounded novelty assessment.** None of these checked sources states the
repository's all-integral-quartic-carrier exclusion for fixed C0 with an
arbitrary positive mate degree, or its newest specified quintic exclusions.
The repository has extended the checked source scopes if its assembled
proofs hold. This is not a priority or novelty certificate. It supplies no
claim that an arbitrary STCI presentation must have a quartic carrier.

## 3. Positive characteristic: the verified family and the remaining gap

T. T. Moh, *Set-theoretic complete intersections*, Proc. AMS 94 (1985),
217–220, DOI 10.1090/S0002-9939-1985-0784166-1,
[official AMS abstract](https://www.ams.org/proc/1985-094-02/S0002-9939-1985-0784166-1/),
was refreshed through indexed publisher text. The monomial result concerns
every projective monomial curve in characteristic p>0. The other result
requires an algebraically closed field of positive characteristic and a
linear plane projection whose center misses the curve, is birational on
the curve, and has a plane image with only cusps. All those hypotheses are
present. Direct article/PDF access returned errors, including 403, so this
is abstract verification, not a new inspection of the original proof.

Consequently **fixed C0 is an STCI in every positive characteristic** by
the monomial-family theorem. This does not establish the universal
projective statement. The repository's separate all-smooth-rational-quartic
construction has its own proof scope and is not a direct application of
Moh's disjoint-center projection clause.

The inherited Cowsik–Nori theorem concerns affine curves. The cone over a
projective space curve is a surface in A4, so it is outside that curve
theorem. The established Das finite-field-closure affine-surface result
requires lci at every point. The cone of a projective curve that is not
already a scheme-theoretic CI fails lci at the vertex: the two local
generators at the irrelevant maximal ideal would imply two minimal
homogeneous generators globally. This is the exact repository cone
obstruction, not a negative theorem about positive-characteristic
projective STCI.

No checked theorem from the refreshed searches proves every integral
projective curve in P3 is STCI over Fpbar or over every algebraically
closed field of characteristic p. Even an affirmative theorem over
Fpbar would not by itself cover curves whose coefficients generate a
transcendental extension of Fp. Degree-zero Picard torsion also does not
eliminate Neron–Severi or full conductor obstructions on a chosen carrier.

## 4. Modern toric input is especially explicit about its restricted rank

Anargyros Katsabekis and Apostolos Thoma,
[*Radical splittings of toric ideals*](https://link.springer.com/article/10.1007/s10801-026-01593-w),
J. Algebraic Combinatorics 64 (2026), article 42,
**published September 28, 2026**, DOI 10.1007/s10801-026-01593-w.
Publisher full text was accessible and inspected.

The abstract identifies radical splitting with **binomial** arithmetic
rank for height-two toric ideals. Section 4, Remarks 4.7, gives radical
splitting number 2 in positive characteristic and 3 in characteristic
zero for symmetric projective monomial curves
`[u^d:u^(d-a)v^a:u^(d-b)v^b:v^d]`, where `a+b=d` and
`gcd(a,b,d)=1`. Fixed C0 has `(a,b,d)=(1,3,4)`, so this directly
confirms its binomial rank is 3 in characteristic zero. It does not
exclude two arbitrary forms. This is a sharper source-specific scope
than describing the paper merely as recent toric work.

## 5. Mandal–Zinna: published conditional results and a still-unrepaired v1

The primary publisher abstract and introductory theorem extract were
refreshed for *Set-theoretic complete intersection for curves in affine
three-folds*, J. Algebra 690 (15 March 2026), 101–113,
[publisher page](https://www.sciencedirect.com/science/article/abs/pii/S0021869325006295),
DOI 10.1016/j.jalgebra.2025.10.042. Theorem 1.2 concerns a dimension-three
affine algebra over a characteristic-zero C1-field, a height-two lci
ideal with free conormal of rank two, and torsion Grothendieck-group
class. The ring-level variant adds the condition that every stably free
rank-three module is free. This gives an affine conditional theorem;
it has no compatibility condition at projective infinity.

The separately published *Set-theoretic complete intersection for smooth
surfaces in a smooth affine algebra*, J. Algebra 693 (1 May 2026), 36–53,
[publisher page](https://www.sciencedirect.com/science/article/abs/pii/S0021869326000165),
DOI 10.1016/j.jalgebra.2025.12.026, still has the smooth affine Fpbar
ambient, trivial conormal and torsion Grothendieck-class hypotheses in
its abstract. Missing rendered dimension formulas were not silently
filled in. It gives no universal projective theorem.

[arXiv:2511.07589](https://arxiv.org/abs/2511.07589) still shows only
v1, submitted **November 10, 2025**. Native arXiv metadata was also
independently retrieved through the connected Sider Scholar tool.
The abstract claims arbitrary dimension-three affine lci curves are
STCI and gives analogous four-dimensional Fpbar claims. The broad v1
must be labeled **CLAIM WITH AN INVALID DISPLAYED PROOF**, not a verified
general theorem: the October 6 exact audit applies unchanged. This
qualifies the ledger's abstract-only “verified abstract theorem” wording.
Refreshing an unchanged abstract does not repair the proof.

The faulty Step 3 was directly inspected again in
[v1 full text](https://arxiv.org/html/2511.07589v1), following equation (1).
It substitutes `J/(c)` for the tensor quotient `J/cJ`. To independently
reconstruct the exact countercheck, take

```
A=k[x,y,z], J=(x,y), c=x,
0 -> A -> A^2 -> J -> 0,
t |-> (-yt,xt), (a,b) |-> ax+by.
```

With `B=A/(x)`, the displayed last term `J/(x)` gives a complex
`B -> B^2 -> (y)` whose middle kernel is `B(1,0)` but whose preceding
image is `yB(1,0)`. Its middle homology is `B/(y)`, nonzero. If the
notation instead means the actual tensor quotient `J/xJ`, the class of
x in `(x,y)/(x^2,xy)` is nonzero and killed by y, so the assertion of
local rank-one freeness fails. This exact computation invalidates the
splitting step. The separate real-sphere example in the October 6 audit
refutes the unrestricted arbitrary-Noetherian-ring CI claim; it is not
a projective counterexample over an algebraically closed field.

No revised arXiv version or primary correction to that step was found.
The newer peer-reviewed titles were not conflated with this v1.

### Two additional 2026 affine papers discovered

Lisa Mandal, *Set theoretic complete intersection of ideals in a Laurent
polynomial ring*, Communications in Algebra 54(11) (2026), 3565–3573,
[publisher abstract](https://www.tandfonline.com/doi/abs/10.1080/00927872.2025.2604611),
DOI 10.1080/00927872.2025.2604611, published online January 13, 2026.
The abstract requires a dimension-n affine algebra over Fpbar with n>=3,
an lci ideal of height n in `A[T,T^-1]`, free rank-n conormal and torsion
Grothendieck class. It proves STCI under those assumptions. It does not
close the homogeneous-projective gap.

**DISCOVERY LEAD ONLY:** Lisa Mandal and Md. Ali Zinna,
*On the minimal number of generators of local complete intersection
ideals in affine four-folds*, J. Pure Appl. Algebra 230(11) (2026),
article 108384, DOI
[10.1016/j.jpaa.2026.108384](https://doi.org/10.1016/j.jpaa.2026.108384).
The title/authors/DOI were returned by connected OpenAlex metadata
record W7204541041; the journal issue and article number also appear
in MathNet citation indexing. Secondary discovery text describes a
three-generator bound over Fpbar under reduced-K0 vanishing.
The primary publisher text and proof were inaccessible in this lane,
so that formulation is **not used as a verified theorem**. A successor
should retrieve its primary abstract and actual hypotheses before
comparing it with the audited v1. In particular, a smooth affine
surface that is not a scheme CI need not be a non-STCI, and supplies
no projective counterexample by itself.

## 6. Another tempting negative claim still has no repaired source

Vahap Erdoğdu,
[*Radically finite rings and space curves*](https://arxiv.org/abs/2209.04489),
still shows only v1, submitted **September 9, 2022**. Its abstract
claims a negative conclusion about space curves. The exact October 6
[unique-maximal/unique-prime countercheck](2026-10-06-session-literature-refresh.md)
remains controlling; no revised version or primary corrected proof was
located. The invalid argument is not an established resolution of the
user's projective algebraically closed problem.

## 7. One bibliographic correction to the inherited ledger

S. Hamid Hassanzadeh,
[*Set-theoretically perfect ideals and residual intersections*](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms.70108),
was published in **J. London Math. Soc. 111(3) (2025), e70108**,
first published **March 6, 2025**, DOI 10.1112/jlms.70108.
The publisher's indexed primary abstract and bibliographic block
were inspected; direct Wiley opening failed. The ledger's “to appear”
wording is outdated even though arXiv metadata remains v2 of February
12, 2025. Its residual-intersection perfectness and cohomological-CI
claims retain Serre-condition hypotheses. Neither perfectness nor
cohomological complete-intersection behavior says that a same-support
ideal has two generators.

## 8. Search and access provenance

Search date throughout: October 13, 2026. Primary theorem statements,
not search-engine crawl ages or secondary summary labels, control all
verified scope assertions above. Queries included:

1. `"set-theoretic complete intersection" "projective" "curves" "2026"`;
   `"set-theoretic complete intersections" "integral projective"`;
   `"set-theoretic complete" "projective curves" "2025" "2026"`.
   Returned dated author sources, affine papers and many irrelevant hits;
   no accepted unrestricted projective resolution was identified.
2. `"rational quartic" "set-theoretic" "quartic"`;
   `"rational quartic" "quartic surfaces" "set-theoretic"`;
   `"Cremona quartic" "set-theoretic complete"`;
   `"quartic" "set-theoretic complete intersections" "Jaffe" "2026"`;
   `"rational quartic" "set-theoretic" "2025" "2026"`.
   Actual Craighero–Gattazzo, Jaffe and Ellia theorem locations were
   inspected after discovery; no checked all-integral-quartic theorem
   emerged.
3. `site:ams.org/bookstore/pspdf/gsm-250-prev.pdf "famous" "quartic"`;
   `site:math.purdue.edu/~murayama/ma665.pdf "Question 2.6.40"`;
   `site:ams.org "0784166" "monomial"` and the corresponding `"cusps"`
   query. These returned the indexed publisher/author originals and
   allowed exact primary scope checks despite direct PDF/403 failures.
4. `"projective curves" "set-theoretic complete" "positive characteristic"`;
   `"quintic" "set-theoretic" "nonnormal" "curve"`.
   Restricted toric/cuspidal families and conductor papers were found.
   The first query supplies no universal positive-char theorem.
5. `"Mandal" "Zinna" "set-theoretic" "2026"`;
   exact-title and `"four-folds"`, `"108384"`, DOI queries.
   The two conditional J. Algebra papers and the Laurent paper were
   checked on primary publisher text. The affine-fourfold paper remained
   a metadata/discovery lead after DOI and issue-page access failures.
6. `"Set-Theoretically Perfect Ideals and Residual Intersections" "2026"`;
   publisher-domain exact-title query; `"Radical splittings of toric ideals"
   "2026"`. These supplied the actual JLMS publication correction and
   the September 28 toric primary article.
7. Direct current arXiv abstract/version records for `2511.07589`,
   `2209.04489`, `1907.05472`, `2409.05705`, `1312.7661`, plus actual
   HTML theorem locations for Jaffe, Ellia and Hartshorne–Polini.
   No later versions repairing the two audited v1 arguments appeared.

Connected-tool provenance: a Sider Scholar OpenAlex search for
`set-theoretic complete intersection curves`, filtered from 2024 and
sorted by newest, returned numerous irrelevant results. A second
concise author/title search also missed the affine-fourfold target.
These outputs are search limitations, **not absence evidence**. Native
arXiv lookup for `2511.07589` succeeded and agreed with the primary
record. Exact-DOI OpenAlex retrieval for the affine-fourfold paper
succeeded, but supplied no inspected primary theorem text. No external
messages were sent, and no items were imported to a scholarly library.

## 9. Continuation consequences

- Keep the universal statement and unrestricted characteristic-zero C0
  problem unresolved. The inherited strongest carrier results have their
  repository proof/audit provenance, not external-resolution status.
- Correct the ledger's broad Mandal–Zinna v1 framing using the existing
  exact audit; do not downgrade the distinct conditional published papers.
- Update Hassanzadeh's publication status and the recent toric entry's
  exact symmetric-monomial/binomial-rank scope.
- Retrieve the new JPAA paper's primary theorem before using it. Its
  indexed affine dimension/field/K-theory restrictions must not be
  dropped even if the abstract eventually confirms the discovery text.
- For a serious novelty assessment of the all-quartic and quintic proofs,
  continue citation-chain and nonnormal-degeneration comparison. The
  bounded search here does not settle priority.
