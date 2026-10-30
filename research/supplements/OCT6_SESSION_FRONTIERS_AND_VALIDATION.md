# October 6 session mathematics, uniform order one, and finite reductions

Topical preservation of mathematical source material and associated audit qualifications; session chronology is not an endorsement of any claim.

---

## 2026-10-06-multithread-consolidation

# Multi-thread consolidation — 2026-10-06

Status: repository integration record.

Baseline: audited main at 98d71dd.

Reviewed active branches:
- research/ultra-resume-2026-10-06
- research/e2-47-closeout-2026-10-06
- research/preserve-reset-2026-10-06
- research/quartic-incidence-synthesis-2026-10-06
- research/quartic-jet-geometry

Historical/provenance branches research/local-audit-e2, research/consolidate-2026-10-06, and ultra_mode were not treated as new inputs.

## Promoted

1. Exact dx=1/P-044 saturation closure from the Codex continuation. The full P-044 residual saturation is the unit ideal; together with the audited boundary this closes the dx=1 slice exactly as P-045.
2. Entirely-thick blowup-cycle necessary inequality and equality-boundary repeated-root reduction.
3. Corrected full-inverse-image normalization/conductor support criterion and the asymptotic descent theorem when all nonnormality is supported on C.
4. Literature/provenance refreshes, including the audit of claimed later resolutions.
5. The quartic jet/ruling geometry and jet-budget framework as a structural supplement only.

## Not promoted

- Side-thread assertions that the characteristic-zero (4,7),e=2 branch remains open. Those branches forked before the audited consolidation and are superseded by the primitive-triple factorization theorem in AUDITED_STATE Section B.
- Broad P-044/quartic-incidence closure programs aimed at re-closing that already-closed branch.
- Codex scratch MF6/local-cohom calculations, generated validation mirrors, and large exploratory datasets. They remain on the Codex branch for provenance and future work but are not canonical mathematical state.
- The old faulty localcoh parity/seed scripts.

## Canonical effect

AUDITED_STATE Section G is upgraded from OPEN to an exact slice classification. New Sections I-K record the entirely-thick inequality, conductor theorem, and structural jet supplement. The global statement remains unchanged: the repository does not yet prove that the smooth rational quartic is not STCI, and the entirely-thick branch remains open.


---

## 2026-10-06-resume-reconciliation

> **Historical status (2026-10-28):** This October 6 reconciliation predates the accepted complete quartic-carrier exclusion (R-0001). Its open quartic-mate and MF6 case labels are historical, not active existence questions. Preserve its mathematical evidence and negative audit findings.

# Resume reconciliation and structural research assessment

Date: 2026-10-06. Status: **RECONCILIATION / RESEARCH STRATEGY**.
No new mathematical theorem or computational exclusion is claimed here.

This assessment reads `CODEX_RESUME_2026-10-06.md`,
`AUDITED_STATE_2026-10-06.md`, `RESEARCH_RECORD.md`, and
`SUCCESSOR_HANDOFF.md` together with the relevant restored sources and
retained audit notes. The audited state is authoritative. Historical
recommendations in the other records do not override it.

## Checkout and historical boundary

The checkout was clean at the start of this reconciliation, on
`research/ultra-resume-2026-10-06`, HEAD `781f00c`. The historical
`ultra_mode` tip is `2e53a7b`, whose commit records the interrupted
five-hour session. Neither branch was switched or reset. No modification
to `main` was made.

The resumed branch restores selected working sources over the audited
consolidation. A source being restored, or an old calculation using exact
arithmetic, does not establish its mathematical conclusion. This session
used three read-only, nondelegating reviews to check the local-cohomology,
primitive/dx1, and carrier lanes. Agreement between those reviews is not
a replacement for the independently audited arguments already in the
repository. No substantial calculation was launched during reconciliation.

## Where the interrupted work had reached

The interruption left several active lanes rather than a single nearly
completed global theorem:

- Quartic local cohomology had been reduced to an order-four ancestor
  space of dimension 30, with 18 quartic multipliers and an exact
  74-dimensional multiplication target. The full incidence is 148
  bilinear equations in 66 variables. General degree-two direction charts
  and contact experiments were unfinished.
- Primitive degree-two quotient work had found actual fourth-obstruction
  zeros, disproving a proposed blanket primitive-quadruple exclusion.
  It then moved toward ambient quartic containment of the canonical triple.
  The restored `primitive47universal` sources retain both the universal
  generation/contact route and the unfinished arbitrary-triple incidence.
- MF6 work had progressed from numerical lists to intrinsic divisor
  identities and higher-normal valuation calculations. The remaining
  constant-direction type `(d2,d3)=(4,5)` had an exhaustive two-parameter
  triple family, a generic quartic kernel, and an unclassified exceptional
  incidence locus.
- Normal carriers and split sextics had acquired significant geometric
  reductions. Their remaining configurations were bounded or reduced to
  parameter families, rather than excluded.

References: `2026-10-06-localcoh-incidence.md`,
`2026-10-06-localcoh-e2-incidence-charts.md`,
`2026-10-06-mf6-type4-incidence.md`, and the restored sources they cite.

## Retained results and their precise scope

1. **Uniform order-one structure.** A quartic carrier has
   `L=O(e-7)`, `0<=e<=2`, with uniform early bounds:
   `(deg D2,deg D3)<=(5,8),(3,5),(1,2)` for `e=0,1,2` respectively.
   The audited minimum for `e=0` is initially one; the retained additional
   quartic-containment argument on fixed `C0` improves it to three.
   For arbitrary carrier degrees with an order-one equation, `e<=6` and
   bounded early defects hold, together with `16/a<=7-e` for the
   order-one carrier. These are not upper bounds on equation degrees or
   total multiplicity.
2. **Primitive fourth / quartic containment.** On the reduced,
   basepoint-free universal fourth-obstruction locus for `C0`, the
   canonical triple has a nonzero distinguished cubic `T` and
   `H0(I_C3(4))=T H0(O(1))`. Independent contact reconstruction certifies
   that this holds at every admissible specialization.
   Consequently the `e=2` branches of `(4,7)` and `(4,8)` are excluded.
   The same argument applies whenever a larger pair has a primitive
   canonical fourth. It does not exclude arbitrary larger `e=2` pairs
   with early defects.
3. **Local-cohomology reductions and exclusions.** The finite order-four
   bound, exact incidence specification, direction bound `e<=2`, and
   first-conormal image are retained. Both ruling-ratio slices, the pure
   constant directions, and the corrected normalized parity family are
   excluded under their recorded hypotheses. The generic-length theorem
   forces a surviving pair to have a curvilinear triple along the generic
   point, a cyclic ancestor of generic length four, and residual cycle
   degree four. These facts do not settle the full incidence.
4. **MF6.** The finite-flat saturated Gorenstein pairings and intrinsic
   first-normal pole identity are retained. On fixed `C0`, a quartic
   `e=0` carrier has `deg D2>=3`; the `(3,6)` nonregular branch is
   excluded. A possible survivor of that type has regular first-normal
   ratio. The `(4,5)` exceptional incidence and the `e=1` types remain.
5. **Normal and split carriers.** The stated normal quartic exclusions
   survive. Remaining rational-resolution B1/B2/B3/D configurations have
   compressed mate-degree bounds, reaching 13824 in the coarsest row.
   The totally ramified split `[2,2]` family reduces to the recorded
   one-parameter line `F_tau=-B^2+tau q K`; that line remains open.

References: the authoritative state sections A--F;
`2026-10-06-primitive-quadruple-audit.md`, section 5;
`2026-10-05-mf6-further-audit.md`; and
`2026-10-06-split22-finite-reduction.md`.

## Corrections and unproved statements

- The older assertion that all primitive degree-two fourth extensions
  fail is false. Primitive extensions exist; actual quartic containment
  supplies the audited obstruction in the stated degree pairs.
- The dx1/P-044 residual classification is **OPEN**, exactly as required
  by audited section G. The retained diagnostic establishes resultant
  identities and multivariate coprimality, not residual-open emptiness.
  A unit-ideal certificate after saturation by
  `x*u*(2*a+1)*(a+u+2*x)` is still missing.
- There is a potential comparison to investigate before repeating that
  elimination: the universal fourth-zero locus has linear equations
  `b0=-2*a1`, `b1=-2*a2`, apparently specializing to the old cross-section
  conditions `a=-1/2,b=-2`. An exact identification of the two coordinate
  and obstruction implementations has not been established in this
  reconciliation. This observation is a proof-comparison lead, not a
  repair of the authoritative dx1 gap.
- The faulty historical parity/seed scripts confused generator-coordinate
  coefficients with actual quartic forms. Their products had the wrong
  degree and their coefficient checks were vacuous. They are not proof
  inputs. The retained corrected parity certificate uses actual products.
- A lifted pure cubic top symbol is not an ancestor construction. In
  particular, a zero of its scalar coefficient does not imply target
  generation fails: the retained DVR counterexample has a cyclic module
  whose special fiber is not Gorenstein. The quartic-carrier primitive
  theorem must not be transferred to local-cohomology pairs, whose
  intersection has a degree-four residual cycle.
- Generic quartic kernels, interrupted resultants, and incomplete rank
  computations do not cover exceptional parameter values or infinity.
  Split-root reductions and normal denominator bounds are not exclusions.

## Genuine frontier

The repository has not proved that `C0` is not STCI. The global separation
is between the uniformly constrained **order-one branch** and the still
open **entirely-thick branch**. Within the quartic-carrier branch, `e=0`
and `e=1` remain, as do larger `e=2` pairs with allowed early defects.
Local cohomology retains all untreated degree-zero/one/two direction
strata and the full quartic incidence, followed by higher multiplier
degrees if necessary. The normal exceptional configurations, surviving
split families, and normalization/conductor descent obligations remain.

First-symbol arguments alone do not address the pole strata or the
entirely-thick branch. A structural continuation must retain higher
normal jets, saturated lattices, conductor data, or equivalent valuation
information.

## Preferred next structural task

Use the remaining MF6 constant-direction type `(d2,d3)=(4,5)` as the
smallest concrete test of a general principle: **bounded effective
defect must annihilate the actual embedded extension obstruction**.
This is a proposed proof task, not a newly proved principle beyond the
specific annihilation statements already recorded.

The existing exhaustive triple family has

    R=A+B(z-2)+z^2-2z+4,
    delta=z(z+2)R+16,
    Res_z(delta,R)=256.

Quartic containment forces `h=delta*S`. Its cubic normal coefficient is

    f3=-T/(8*delta^2*S),
    ord(D3-D2)=max(0,ord S-ord T)

at every finite point, including multiple zeros of delta. Here S is a
section of O(5), while the permitted total excess defect is only one.
Thus almost its entire zero divisor must cancel in T. Generic parameters
are already excluded. The useful next question is whether this required
cancellation can occur for an irreducible quartic anywhere on the complete
incidence, including rank drops and the moving infinity chart.

First formulate that question intrinsically as divisibility of sections
or annihilation of an extension class, and seek a short argument using
the complete quartic image and the one-unit pole budget. This could
eliminate a whole defect type without enumerating pole placements. If a
finite calculation is needed, it should certify the resulting high-common-
divisor or module-rank condition with its open loci, rather than expand
the previously interrupted full resultant. A special surviving quartic
must be retained if the structural claim fails.

Keep the actual quartic variable in the full linear incidence and allow
the possible extra defect point to range over P1. Geometrically the
question is whether the fourth layer can be an elementary modification
with at most one additional defect point. This formulation can handle
rank-drop quartics and the infinity point directly; the generic kernel
vector alone cannot. Any finite certificate should derive the nonlinear
second-frame transformation before using homogeneous divisor conditions.

This task has a complete two-parameter starting family and a precise
contradiction threshold. It is therefore a more controlled next move than
the unfinished 43-variable local-cohomology charts or the 66-variable
bilinear system. It may also supply a useful model for the remaining
quartic `e=0/e=1` early-defect geometry.

The next local-cohomology structural task is analogous but distinct:
derive target-specific pole restrictions on the highest ancestor
coefficient. For `e=2` that coefficient belongs to O(1), so there is only
one top-symbol zero. Its possible cyclic-module degeneration must be
analyzed without assuming Gorenstein special fibers. The corrected
parity polynomial-dual method provides a model for a later exact
certificate after structural reduction.

## Immediate reproducibility boundary

The source/exporter and several JSON certificates are restored, but the
following referenced generated inputs are absent in this checkout:

- `computations/localcoh-incidence-tensor.txt` and
  `computations/localcoh-incidence-bases.txt`;
- `computations/localcoh-symbol-numerators.txt`;
- the general `computations/localcoh-e2-incidence-2026-10-06.py` chart
  exporter and exported chart systems;
- the parity discovery `.m2` file;
- `scratch/mf6_type4_incidence.json`.

The retained tensor exporter correctly sums all four generator
contributions and can regenerate its two outputs. The MF6 exploration
source can regenerate its generic matrix and S,T data. Other missing
coordinate prerequisites need to be located or reconstructed before
claiming a live certificate rerun. Their absence does not reverse the
audited mathematical status; it limits immediate reproducibility.

Validation in this reconciliation consisted of reading the specified
records and relevant sources, comparing their scopes, inspecting branch
and file provenance, and checking generated-input availability. Existing
mathematical verifiers were not rerun, and no new substantial calculation
was begun.


---

## 2026-10-06-session-conductor-support

# Full inverse-image support and asymptotic conductor descent

Date: 2026-10-06. Status: **PROVED under the stated hypotheses;
independently audited by the frontier auditor and a separate local-algebra
auditor**.
This note corrects a missing support hypothesis in the historical P-032
formulation and gives a conditional construction valid in every
characteristic. It is not a resolution of the universal STCI problem.

Let X=V(F) be an integral hypersurface in P3 over an algebraically closed
field, C an integral curve in X, and nu:S->X the finite normalization.
Write H=nu*O_X(1), Q=nu_*O_S/O_X, and c=Ann(Q). Let

    W=(nu^{-1}(C))_red

denote the **entire** reduced inverse image, including possible isolated
points. A finite morphism does not ensure that W is pure dimensional.

## 1. An obstruction before divisor classes or descent

If X has an STCI mate G for C, the nonzero pullback of G is a section
of O_S(bH) whose zero set is exactly W. Its zero scheme is an effective
Cartier divisor on the integral normal surface S. Every minimal prime
of a nonzero principal ideal in a Noetherian domain has height one.
Consequently W has no isolated zero-dimensional irreducible component.

Thus an isolated point in the full inverse image of C excludes **every
mate degree on this fixed carrier**. It does not exclude C as an STCI
on a different carrier.

The historical P-032 notation implicitly replaced W by the union of its
curve components. That replacement requires a purity check. Finiteness
rules out exceptional divisors over closed points, but does not rule out
isolated inverse-image points.

The fixed-degree corrected criterion is: there exists an effective
Cartier divisor A on S with |A|=W, an isomorphism O_S(A)=O_S(bH), and
descent of its canonical section to O_X(b). Equivalently the canonical
section must match a section on the full conductor scheme. The proof
of P-032 then applies verbatim. If W is pure dimensional, A can be
written as a positive integer combination of **all** curve components
of W; if W is not pure dimensional, no such A exists.

## 2. Asymptotic descent when all nonnormality lies on C

**Conditional theorem.** Assume Supp(Q) is contained in C. Then the
following are equivalent:

1. C has an STCI mate on X, of some positive degree;
2. there are b>0 and an effective Cartier divisor A on S such that
   |A|=W and O_S(A) is isomorphic to O_S(bH).

Necessity follows by pulling back a mate. For sufficiency transport
the canonical section of A to s in H0(S,O_S(bH)). The conductor c is
an ideal both in O_X and in nu_*O_S: locally for A subset B,
c={a in A : aB subset A} satisfies cB=c, hence nu_*c_S=c.
Its ideal on S, denoted c_S,
has zero set contained in W, since Supp(Q) is contained in C.

Let I_A=O_S(-A). Since V(c_S) is contained in V(I_A), locally
I_A is contained in radical(c_S). Noetherianity and quasi-compactness
give a single positive N with

    I_A^N contained in c_S.

In each trivialization of O_X(b), the coefficient of s^N therefore
belongs to the conductor. It belongs to O_X; these coefficients glue
because the trivializations are pulled back from X. Hence s^N descends
to t in H0(X,O_X(Nb)). The restriction map

    H0(P3,O(Nb)) -> H0(X,O_X(Nb))

is surjective, since H1(P3,O(Nb-deg F))=0. An ambient lift G has zero
set C on X, by finite surjectivity and |V(s^N)|=W. This is the required
pair (F,G). The proof uses no Frobenius and works in all characteristics.

This removes the **existence of some mate** conductor obstruction for
carriers whose nonnormal locus is entirely supported on C. It does
not remove conductor descent at a prescribed degree and does not
produce the requisite positive Cartier divisor or its linear equivalence.
Additional nonnormal curves away from C remain a genuine loophole.

## 3. Exact control example already present in the checkout

The retained characteristic-zero verifier verify_general_conductor_power.py reconstructs
the cubic pinch surface

    X: x^2 w-y^2 z=0

and its smooth-scroll normalization with affine chart

    (x,y,z,xi,w)=(u,ur,1,r,r^2).

For the indicated twisted cubic C, the full pulled-back ideal on this
chart is

    (h u,h(r+1))=(h) intersect (u,r+1),
    h=r-1-u(1+r).

The two factors are comaximal because h(0,-1)=-2. This example requires
characteristic different from two; the verifier works over Q. Thus the preimage
contains the divisor h=0 and an isolated reduced point (u,r+1).
The obstruction in section 1 already excludes this fixed carrier.
The verifier also checks that this same twisted cubic is STCI on
another carrier by the standard degree-(2,3) pair. Its existence must
remain visible: the obstruction is carrier-specific.

The verifier's docstring points to the 2026-10-05 literature note for
the unit-ratio example, but that explanation is absent from the retained
version of the note. This present support proof does not rely on the
missing explanatory text or on a sampled power calculation.

## 4. Primary-source background and continuation boundary

The Stacks Project effective-Cartier discussion supplies the standard
local nonzerodivisor and pure-codimension-one facts:
https://stacks.math.columbia.edu/tag/01WQ and
https://stacks.math.columbia.edu/tag/0B3Q.
The conductor argument above is proved here directly; no novelty claim
is made.

For future thick-carrier work, first test purity of W, then decide
whether Supp(Q) is contained in C. If it is, the remaining global
task is positive Cartier support and hyperplane linear equivalence
upstairs. If it is not, keep the full nonreduced conductor square and
residue-unit gluing data. Normalization does not by itself supply either.


---

## 2026-10-06-session-literature-refresh

# Literature refresh, scope audit, and failed-resolution check

Date: 2026-10-06. Lane: independent literature audit. The controlling repository
state read for this audit was `research/AUDITED_STATE_2026-10-06.md`; the existing
ledger and `2026-10-05-literature-new-routes.md` were treated as claims to check,
not substitutes for primary sources. No canonical file was changed in this lane.

## Findings that change the source record

1. A missed 2022 preprint explicitly claims a negative resolution for space
   curves. Its crucial prime-ideal inference is false, with an elementary exact
   counterexample below. It supplies no accepted projective counterexample.
2. The original Robbiano–Valla chapter explicitly proves the positive result for
   **ACM monomial** space curves. Its publisher preview now makes that scope
   directly inspectable. A survey's arbitrary-ACM statement cannot be attributed
   to this primary chapter without an additional source.
3. Jaffe's accessible primary paper reports the characteristic-zero cone-carrier
   exclusion in arbitrary degree. This removes cones from the rational-quartic
   search, although the original cone-paper proof was inaccessible in this run.
4. A separate positive-characteristic audit found an exact proof failure in the
   broad Mandal–Zinna v1 and a counterexample to one of its stated global CI
   theorems. Its broad statements require an unverified-preprint label. The
   narrower separately published conditional results remain separate.

These findings strengthen provenance and eliminate misleading shortcuts. They
do not decide whether the smooth rational quartic, or every integral projective
space curve, is an STCI.

## A. Dated primary open-status evidence

David Eisenbud and Joe Harris, *The Practice of Algebraic Curves* (AMS, 2024),
Example 3.13, printed pp. 64–65, identifies the smooth quartic

\[
C_0=[s^4:s^3t:st^3:t^4]
\]

and retains its two-arbitrary-equation radical problem as open. The publisher
preview was verified through targeted indexed text; direct full-PDF retrieval
through the web tool failed on this run. The source is
<https://www.ams.org/bookstore/pspdf/gsm-250-prev.pdf>.

Takumi Murayama's MA665 notes are explicitly labelled Spring 2026 and compiled
2026-04-28: <https://www.math.purdue.edu/~murayama/ma665.pdf>. The compilation
date was refreshed in indexed primary text. The companion author notes retain
the universal irreducible-projective-curve question and the characteristic-zero
quartic example:
<https://www.math.purdue.edu/~murayama/LocalCohomology.pdf>, section “Back to
Curves,” Open Question and Example 11. The latter text was refreshed in indexed
primary text; direct PDF opening failed. Accordingly the exact MA665 question
number from the earlier ledger was not independently refreshed here.

Hartshorne–Polini's actual source remains
<https://arxiv.org/abs/1907.05472> and
<https://arxiv.org/html/1907.05472v1>. Its local-cohomology/coregularity criterion
is an affirmative characterization of a suitable pair, not the assertion that
such a pair always exists. The canonical unresolved local-cohomology incidence
problem remains consistent with that source.

**Epistemic conclusion.** No accepted later unrestricted resolution was found
by the searches recorded in section F. This is a dated search conclusion. The
2024 and 2026 author sources are dated open-status evidence, not logical proof
that no unindexed resolution exists.

## B. Exact audit of the 2022 negative claim

Vahap Erdoğdu, *Radically finite rings and space curves*,
<https://arxiv.org/abs/2209.04489>, v1 submitted 2022-09-09, has no later version
in the inspected arXiv history. Its abstract and Corollary 4.4 assert that space
curves are not always STCI. The full proof is directly accessible at
<https://arxiv.org/html/2209.04489>, section 4, Theorem 4.3 and Corollary 4.4.
The corollary concerns the affine polynomial ring in three variables; it is not
an explicit integral projective-curve construction.

The theorem's argument first establishes a unique maximal ideal above an ideal
generated by two elements, then tries to establish that it is the unique
**prime** ideal above that ideal. The decisive inference is that a contraction
which is a G-ideal makes the prime above it maximal. The G-ideal condition gives
the existence of a maximal ideal with that contraction; it does not identify
every prime above the contraction with that maximal ideal.

### An elementary counterexample to that exact inference — PROVED HERE

Let k be any field and

\[
R=k[x,y]_{(x,y)},\qquad A=R[T].
\]

Then R is a finite-character UFD of dimension two: it is local, with unique
maximal ideal M=(x,y). In the displayed construction in the proof choose

\[
\Pi_1=x,\quad \Pi_2=y,\quad z=1-y,\quad f=T,
\quad g=y+(1-y)T.
\]

These choices satisfy every relation used there, including \(\Pi_2+z=1\).
The element 1-y is a unit of R. Consequently

\[
P^*=(x,g)\subset A
\]

is prime, because elimination of T gives

\[
A/P^*\simeq R/(x)\simeq k[y]_{(y)},\qquad
T\longmapsto-\frac{y}{1-y}.
\]

It has height two. It is properly contained in the height-three maximal ideal

\[
M^*=(x,y,T).
\]

For example y is nonzero in the displayed quotient, so y is not in P*. Since
P* is already prime,

\[
\sqrt{(\Pi_1,g)}=P^*\ne M^*.
\]

At the same time the quotient is local, so M* **is** its unique maximal ideal;
the paper's intermediate statement about the intersection of maximal ideals
holds in this example. This isolates the exact failure: a unique maximal ideal
does not make the smaller defining prime maximal. No appeal to computation is
needed.

The contraction \(P^*\cap R=(x)\) also satisfies the existential property of a
G-ideal used in the paper: the distinct maximal ideal
\((x,yT-1)\) of A contracts to (x), with quotient k(y). That existence does not
change the nonmaximal prime P* above the same contraction.

**Scope.** This disproves a particular implication in the proof, so the
negative-resolution corollary is unsupported by that proof. It does not prove
that every affine space curve is STCI, or that the theorem's whole statement is
false under every possible interpretation of “radically finite.” Searches did
not find a correction or a refereed replacement proof.

## C. The arbitrary-ACM claim is not reconstructed from its cited primary source

The Robbiano–Valla original chapter's publisher page is
<https://link.springer.com/chapter/10.1007/BFb0061654>. Its official two-page
preview is directly readable at
<https://page-one.springer.com/pdf/preview/10.1007/BFb0061654>.

Printed pp. 391–392 explicitly describe section 2 and Corollary 2.3 as proving
that projective **monomial** space curves with Cohen–Macaulay coordinate ring
are STCI in every characteristic. The proof uses the special determinantal
structure of this monomial family. This is primary verification of a positive
theorem under its monomial hypothesis.

Clare D'Cruz's survey,
<https://arxiv.org/html/2003.09101v1>, Theorem 2.7, literally states a broader
arbitrary-ACM-curve assertion, citing this chapter and Stückrad–Vogel. Its
reference 62 identifies the latter as “On the number of equations defining an
algebraic set of zeros in n-space,” Teubner-Texte 48 (1982), pp. 88–107. The
full Stückrad–Vogel text was not accessible in this audit. Thoma's 1993 text
also mentions ACM curves broadly inside a monomial discussion:
<https://archive.mpim-bonn.mpg.de/948/1/preprint_1993_86.pdf>, introduction,
printed p. 2.

**Safe ledger entry.** ACM monomial P3 curves are verified STCI; a modern
survey states the broader arbitrary-ACM assertion, whose original proof and
hypotheses have not been reconstructed. Do not use the broad assertion as a
verified theorem merely because it appears in the survey. The accessible
original chapter does not supply it. This source gap does not itself refute the
broader assertion.

## D. Cone carriers and primitive structures

Jaffe's primary author paper
<https://arxiv.org/html/alg-geom/9410008>, introduction, reports that in
characteristic zero its prior papers prove \(d\leq g+3\) when one STCI carrier
is a cone. The introduction's surfaces are reduced and irreducible. Thus a
smooth rational quartic cannot have a cone carrier, regardless of its degree.
This is a useful all-degree restriction in addition to the already recorded
cubic and rational-singularity exclusions.

The original cone paper is David B. Jaffe, *Space curves which are the
intersection of a cone with another surface*, Duke Math. J. 57 (1988),
859–876, <https://doi.org/10.1215/S0012-7094-88-05738-9>. The publisher/Euclid
full text was unavailable through the current web access. Classification:
**primary author-reported theorem; original proof not rederived here**.

The primitive source remains Ellia,
<https://arxiv.org/abs/1409.3801>, with original author PDF
<https://dm.unife.it/philippe.ellia/Docs/Ellia-primCI-arXiv.pdf>. Its primitive
hypothesis means local containment of the multiple structure in a smooth
surface. Its finite numerical restrictions do not exhaust the entirely-thick
branch. No newer unrestricted primitive-to-arbitrary reduction was found.

## E. Affine/positive-characteristic theorem audit is a separate artifact

See the independently written companion
`2026-10-06-positive-characteristic-literature-audit.md` for theorem-by-theorem
hypotheses, the 2018 Das theorem, newer published conditional results, and the
exact Mandal–Zinna v1 proof audit. The broad preprint is
<https://arxiv.org/html/2511.07589v1>.

Two barriers persist for a projective transfer: the affine cone is a
two-dimensional subscheme in a four-dimensional ring, and for a projective
curve which is not already a scheme CI its cone vertex is not lci. Affine
equations also need a homogeneous/infinity compatibility argument. The
published affine results and Frobenius constructions for special projective
families do not establish every integral projective P3 curve in fixed positive
characteristic.

## F. Search provenance and route assessment

Searches on 2026-10-06 included:

- projective/space-curve STCI with 2025 and 2026, including arXiv restrictions;
- integral/singular projective curves and counterexample terminology;
- rational quartic/Macaulay curve unrestricted two-equation problems;
- primitive multiple structures, cone carriers, and original ACM source chains;
- exact title/identifier searches for Erdoğdu's negative claim and corrections.

Search-engine crawl or “published” labels were not treated as publication
dates. For example, older PDFs appeared with recent crawl labels. ArXiv
submission/version histories and publisher bibliographic records control.
Secondary aggregators and TheoremDB were discovery leads, not theorem
evidence. No forum, aggregator, or database status was promoted to a primary
proof.

**Research judgment.** The most valuable new information in this lane is the
elimination of false global shortcuts and the missing cone-carrier restriction.
The canonical mathematical frontier still has the open e=0/e=1 order-one
branches and the entirely-thick branch. A new argument must control the latter
or produce a truly arbitrary presentation; neither a finite primitive list nor
an affine lci theorem substitutes for it. For the singular integral universal
case, local singularity and cone-vertex lci hypotheses need their own audit:
smooth-support filtration results cannot simply be transferred to that case.


---

## 2026-10-06-session-localcoh-progress

# A finite corner exclusion and the inverse-system defect boundary

Session started 2026-10-06; checkpoint completed 2026-10-07. Scope: the
characteristic-zero monomial rational quartic C0 and its two fixed
local-cohomology targets. This is an exact family exclusion and a structural
reduction. The full quartic incidence and the universal STCI question remain
open.

## 1. Three complete zero-at-origin corner families are excluded

Use the balanced normal-dual direction

\[
p=1+a_1t+a_2t^2,\qquad r=b_0+b_1t+b_2t^2
\]

and the order-four pure cubic symbol
\(c_i=t p^i r^{3-i}\), \(i=0,1,2,3\). Thus its top coefficient has
its single zero at t=0. This section treats the complete corner b0=0;
primitivity then guarantees p(0) nonzero, so its normalization to one loses
no candidate.

The three exact top-image annihilators from the audited 32-by-30 matrix,
after b0=0, give

\[
b_1=-6(a_1^2+a_2),\qquad a_2(a_2+a_1^2)=0.
\]

On a2=0 the remaining equation is

\[
(b_2-18a_1^3)(b_2+6a_1^3)=0;
\]

on a2=-a1^2 it is

\[
(b_2-2a_1^3)(b_2-10a_1^3)=0.
\]

If a1=0, the direction is not primitive as a homogeneous quadratic pair.
The a2=0, b2=-6a1^3 branch is also nonprimitive: both forms contain
1+a1*t. Every other branch is primitive. The actual ambient torus
automorphism of C0 transforms a normal-dual pair by

\[
(p(t),r(t))\longmapsto(l^4p(t/l),l^3r(t/l)).
\]

After dividing by l4 and choosing l=a1, every primitive direction in this
corner is one of exactly three normalized directions:

| Name | p | r |
| --- | --- | --- |
| corner18 | 1+t | -6t+18t² |
| corner2 | 1+t-t² | 2t² |
| corner10 | 1+t-t² | 10t² |

The coefficient h=t remains a nonzero scalar multiple of t, absorbed by
scaling the ancestor. Each target is a torus eigenvector, so existence of
the two multiplier equations is preserved by this normalization.

For each of the three symbols the fixed top map has a unique affine line of
lifts a=a*+lambda*k. The one-dimensional kernel k is the retained T3(-7)
section. Using the **actual** audited 74-by-18 quartic multiplication tensor,
the companion calculation finds a polynomial row n(lambda) satisfying

\[
n(\lambda)^T L(a^*+\lambda k)=0,\qquad n(\lambda)^T e_{72}=1.
\]

These identities exclude even the single target u for every lambda over
every characteristic-zero field extension. Hence all quartic common
ancestors with h=t and r(0)=0 are excluded. This assertion includes every
lower-order correction; it is not a sampled parameter computation.

Reproduce the saved identities using only Python's standard library:

    python3 research/computations/session-localcoh-corners.py

Regenerate the rational lifts and one-variable Macaulay2 module duals:

    /private/tmp/stci-cas-venv/bin/python research/computations/session-localcoh-corners.py --regenerate

The JSON certificate stores the three rational seeds, common kernel and
complete polynomial duals. The verifier checks the coordinate hashes,
target columns, all 18 polynomial identities, and each exact pure cubic
top. The generator and the three .m2 and dual-text files are retained. The
top-image branch classification is the displayed exact algebra, with no
numerical inference.

## 2. The socle pencil forces the top divisor to be an actual defect

The following derivation uses the already proved finite bound and generic
length theorem. The parent research agent independently audited the sheaf,
duality, endpoint normalization and Euler-characteristic arguments on
2026-10-07. This is a proved structural reduction under those antecedents.

Suppose a common quartic ancestor alpha survives. Its saturated annihilator
defines a pure Cohen--Macaulay quadruple Z supported on C0. Indeed its cyclic
module embeds in the finite inverse-system sheaf, which has no torsion at
closed curve points; at the generic point its length is exactly four and
its Hilbert function is (1,1,1,1). Write its saturated filtration pieces

\[
E_0=O_C,\quad E_1=L=O_C(e-7),\quad
E_2=L^2(D_2),\quad E_3=L^3(D_3),\qquad 0\le D_2\le D_3.
\]

The deepest piece E3 is the saturated socle. Multiplication by alpha gives
a faithful map

\[
O_Z\hookrightarrow\omega_Z(-3).
\]

Here local duality identifies the inverse-system sheaf supported on Z with
omegaZ(4), and alpha has ambient twist -7. Since I_C annihilates E3, the
restriction lands in

\[
\operatorname{Hom}_{O_Z}(O_C,\omega_Z)(-3)
\simeq\omega_C(-3)=O_{\mathbf P^1}(-14).
\]

The images of F and G in O_Z are in E3: they are socle elements generically,
and the lower filtration quotients are torsion free, so socle membership
propagates to every curve point. Their alpha-images are the fixed socle
sections u,v. The raw numerators xz and yw must not themselves be used as
a basepoint-free pencil: their curve restrictions have common endpoint
factors. On x=1, writing t=y, the first-normal determinant of (q,B) relative
to the balanced frame (U,V) is t³. The residues of xz=t³ and yw=t⁵ therefore
normalize to 1 and t². On the other affine chart these glue to the
homogeneous pencil (s²,t²) in H0(O_P1(2)), which has no common projective
zero. Thus, after twisting by O(4), the restriction of alpha to E3 is everywhere
surjective. It is a morphism of line bundles and hence an isomorphism:

\[
\boxed{E_3=O(-14),\qquad \deg D_3=7-3e.}
\]

The pure top coefficient h consequently has exactly divisor D3. A zero of h
cannot simply be discarded as an irrelevant degeneration. For e=2 this
gives deg D3=1 and leaves only

\[
(\deg D_2,\deg D_3)=(0,1)\quad\text{or}\quad(1,1).
\]

The first triple is primitive in the first case. In the second it has a
defective fiber at the one top-zero point. There is no implication that the
fourth structure is primitive in either case.

For completeness, chi(OZ)=4+6*deg L+deg D2+deg D3. Serre duality gives
chi(omegaZ(-3))=-chi(OZ)-48. The faithful alpha map has finite cokernel of
length

\[
2(\deg D_3-\deg D_2).
\]

Thus the (1,1) e=2 case makes alpha an isomorphism
OZ=omegaZ(-3): Z is Gorenstein and omegaZ=OZ(3). This numerical and
duality condition is necessary; it does not prove an ambient realization
or an STCI presentation.

## 3. Both e=2 local defect types are possible

Let D=k[[c]], R=D[[U,V]], and eij=U^(-i-1)V^(-j-1) in the transverse
inverse-monomial module. The counterexample

\[
\alpha=c e_{03}+e_{11}
\]

has exact annihilator

\[
\operatorname{Ann}(\alpha)=(U^2,V^2-cU).
\]

Its quotient is free of rank four over D with basis 1,V,U,UV. Generically
U=V²/c and the algebra is curvilinear. At c=0 it is the Gorenstein complete
intersection (U²,V²), with Hilbert function (1,2,1). Saturated powers have
E1 generated by V, E2 by U, E3 by UV. The relations V²=cU and V³=cUV give
D2=D3=(c=0). Nevertheless UV*alpha=e00, so the socle image is a unit at
the top-zero point. This proves the defective (1,1) case cannot be removed
by the relative Gorenstein argument or by the basepoint-free target pencil.

The other model

\[
\alpha=c e_{03}+e_{10},\qquad
\operatorname{Ann}(\alpha)=(U^2,UV,V^3-cU)
\]

has rank-four flat quotient with basis 1,V,V²,U. Here D2=0, D3=(c=0),
and U*alpha=e00. Its special abstract fiber has two-dimensional socle; the
cyclic inclusion into the inverse system does not remain injective on that
fiber. This is the retained generic-length countermodel. These local
examples distinguish the primitive triple from the defective triple and
preserve the failed shortcut against assuming every fiber is curvilinear.

## 4. Exact rational normalization when both endpoint coordinates are nonzero

The corner exclusions close h=t, r(0)=0. On h=t, p(0)*r(0) nonzero, the actual
torus and common direction scaling normalize p(0)=r(0)=1. The equations give

\[
b_1=-6(a_1^2+a_2)-2a_1-\tfrac32,
\]

\[
16a_2^2+(16a_1^2+12)a_2+12a_1^2+4a_1+3=0.
\]

The latter quadratic has discriminant
16(2a1+1)³(2a1-3). Its rational normalization is

\[
a_1=\frac{k^2+3}{2(1-k^2)},\quad
a_2=-\frac{k^2+2k+3}{2(k+1)^2},\quad
b_1=\frac{(k-3)(k^2+2k+3)}{(k-1)^2(k+1)}.
\]

Put qk=k²+2k+3. The final quadratic factors exactly into these two choices:

\[
\boxed{
b_2=-\frac{2(k^2-4k+5)q_k^2}{(k-1)^3(k+1)^3}
\quad\text{or}\quad
b_2=-\frac{2(k^2+1)(k^2-2k-1)q_k}{(k-1)^3(k+1)^3}.
}
\]

The homogeneous resultants are, respectively,

\[
\frac{8q_k^2(9k^4-21k^3+5k^2-31k+134)}{(k-1)^6(k+1)^6},
\]

\[
-\frac{8q_k(3k^4-2k^3-6k^2-18k-9)}{(k-1)^5(k+1)^6}.
\]

Primitivity retains exactly k≠1,-1 and the corresponding nonzero resultant.
The only point of the original finite chart omitted by finite k is
a1=a2=-1/2, b1=1,b2=-2. It is nonprimitive: its pair is
(1-t)(1+t/2),(1-t)(1+2t). Consequently these two rational families cover
**every primitive direction in the h=t endpoint chart with p(0)*r(0) nonzero**.

The exact companion `session-localcoh-origin-parametrize.py` checks all three
top-image identities, the quadratic discriminant, the final factorization,
both resultants and the omitted boundary. The two rational families are
stored in `session-localcoh-origin-families.json`. After retaining lambda,
the remaining endpoint incidence has only two parameters. A generic module
exporter `session-localcoh-origin-family-module.py` contracts the complete
actual tensor over QQ(k)[lambda]; any generic dual it finds still requires
an audit of every exceptional denominator/root locus.

## 5. The other endpoint boundary is retained completely

If p(0)=0, primitivity gives r(0) nonzero. Normalize r(0)=1 and write
p=a1*t+a2*t², r=1+b1*t+b2*t². The three top-image equations reduce exactly
to b1=8*a1²*a2 and

\[
4a_2(2a_1+1)
\left((2a_1+1)^2b_2+
2a_2^2(2a_1-1)(16a_1^4+8a_1^2+5)\right)=0.
\]

On a2=0, primitivity means a1*b2 nonzero. The torus normalizes b2=1,
giving (a1*t,1+t²). The actual ambient coordinate-reversing involution sends
normal-dual directions to (t²*r(1/t)/2,2*t²*p(1/t)), as follows from the
independently audited quartic symbol reversal formula. It also reverses the
linear top coefficient. Thus this direction with h=t becomes normalized
parity (1+t²,4*a1*t) with constant h. The existing exact parity certificate
excludes it, transporting the two target eigenclasses by their exchange.

On a2 nonzero, the torus normalizes a2=1 without changing a1. There are
exactly two remaining one-parameter families:

\[
p=k t+t^2,\qquad
r=1+8k^2t-
\frac{2(2k-1)(16k^4+8k^2+5)}{(2k+1)^2}t^2,
\qquad k\ne-\tfrac12,
\]

with resultant

\[
-\frac{(2k-1)(32k^6+32k^4+24k^3+26k^2+6k+1)}{(2k+1)^2},
\]

and the exceptional family

\[
p=-\tfrac12t+t^2,\qquad r=1+2t+b t^2,
\qquad \operatorname{Res}(p,r)=(b+8)/4\ne0.
\]

The exceptional family must be retained: the top equations vanish there for
every b. `session-localcoh-origin-boundary.py` verifies this split and its
resultants and saves the family JSON. Taken with Sections 1 and 4, this is a
complete direction classification for primitive e=2 top coefficient h=t:
the three finite corner families and the reversed parity family are
excluded; four one-parameter direction families remain for the actual
quartic multiplier incidence, each with the single lower coefficient lambda.

## 6. Computation status and continuation

For the **first** rational family of Section 4, a Macaulay2 calculation over
QQ(k)[lambda] returned a dual n with n^T L=0 and n^T u=1. The complete dual,
not merely its existence, is saved. Clearing its coefficient denominators
gives a polynomial dual, independently verified against all actual tensor
columns by `session-localcoh-origin-generic-dual.py` using Python's standard
library. This proves exclusion for **every lambda** outside a finite
exceptional k locus.

The cleared ancestor denominator is 120(k-1)^9(k+1)^9, and the dual's target
evaluation is the nonzero constant 89514547200 times

\[
(k-1)^{14}(k+1)^{11}(k^2-4k+5)^5(k^2+2k+3)^8
\]

times the four polynomials

\[
3k^4-9k^3-19k^2-43k-4,
\quad 9k^4-21k^3+5k^2-31k+134,
\quad 13k^4+26k^3+34k^2+6k-7,
\]

\[
729k^{13}+1620k^{12}+2889k^{11}-11268k^{10}-26574k^9
-39642k^8+94014k^7+272968k^6+454897k^5+62256k^4
-571463k^3-1210068k^2-966908k-379834.
\]

The factors k±1 are outside the chart. The factor k²+2k+3 and the middle
quartic are outside the primitive resultant-open locus. An independent
2026-10-07 audit has now **excluded the quadratic locus k²−4k+5=0 at both
roots for every lambda**, using the complete saved number-field dual and
a new standard-library verifier against all 18 actual tensor columns.
The two remaining quartics and degree-thirteen polynomial are finite
**unresolved exception loci** of this particular dual; no existence follows
from their vanishing. They are square-free, pairwise coprime and inside the
primitive chart, leaving 21 geometric direction parameters, each with its
full lambda fibre. See
[`2026-10-07-session-localcoh-independent-audit.md`](2026-10-07-session-localcoh-independent-audit.md)
for the complete coverage and denominator audit and
`verify_session_localcoh_q2_dual_2026_10_07.py` for the quadratic certificate.
The first family remains an exact open family exclusion rather than a
complete exclusion.

Run the independent identity verifier:

    python3 research/computations/session-localcoh-origin-generic-dual.py

The polynomial JSON, raw rational dual, rational seed, field-module exporter
and .m2 script are durable. They preserve all parameter denominators and
scope. The other three direction families of Sections 4 and 5 still need
the actual multiplier incidence.

The earlier five-variable quotient-module calculation was interrupted
after a bounded run before a kernel/evaluation result. Its script and chart
JSON remain inspectable; no exclusion follows from the unfinished run.
Top-zero points outside the endpoints need their own torus-normalized
chart. Neither the two rational-family parametrization nor the completed
corner certificate resolves these remaining incidence problems.


---

## 2026-10-06-session-mf6-progress

# MF6 constant-direction type (4,5): moving-chart annihilator reduction

Started 2026-10-06; resumed 2026-10-07 after a usage-limit interruption.
Characteristic zero; fixed monomial quartic
`C0=[s^4:s^3t:st^3:t^4]`.

**Status: PROVED HERE, INDEPENDENTLY AUDITED.** The complete
`e=0,(d2,d3)=(4,5)` branch is excluded, including every quartic rank-drop
fiber and infinity. On 2026-10-07 the root agent independently audited
the moving-support derivative correction, the degree-loss and infinity
annihilator argument, the shifted coefficient ideal, and the full
four-dimensional exceptional quartic fiber. The self-contained exact
verifier passed after adding direct ideal-membership witnesses and the
full fiber reconstruction.

The earlier note `2026-10-06-mf6-type4-incidence.md` remains a correct
historical record of its generic-only calculation. This continuation
supplies the missing intrinsic annihilator condition; it does not promote
that generic kernel to the complete family.

## 1. Complete triple family and quartic variable

The retained degree-four triple reduction exhausts the mixed constant
normal directions after torus normalization `m=U+V,y=V`. Its parameters
are arbitrary `A,B`, with

    R=A+B(z-2)+z^2-2z+4,
    delta=z(z+2)R+16,
    gamma=3R/8,
    Res_z(delta,R)=256.

Thus `delta` has degree four with leading coefficient one, has no infinity
zero, and has no finite common zero with `R`. The discarded homogeneous
coefficient chart `C=0` in the original triple construction fails
flatness, rather than being omitted generically.

Let `F` be any quartic in the complete eight-dimensional space with
first-normal form `h(U+V)`. In the finite moving frame, write its quadratic
and cubic coefficients as `Q,E,K`, where `Q` is the `y^2` coefficient
at `m=0`, `E` the `my` coefficient, and `K` the `y^3` coefficient.
Triple containment is precisely

    delta Q+(3/8)R h=0.

Coprimality forces `h=delta S`, where `S` is a section of `O(5)`.
Every nonzero incidence quartic has `S!=0`: the first-normal kernel of
the mixed quartic space is the single line `<q^2>`, and its quadratic
restriction at `m=0` is nonzero, so `q^2` fails the triple equation.
Consequently the generic formal root is

    m=f2*y^2+f3*y^3+...,
    f2=3R/(8delta),
    f3=-T/(8delta^2 S), T=3RE+8delta K.

No kernel dimension or generic parameter assumption enters these formulas.

## 2. The moving second chart through cubic order

The actual second support parameter is

    W=(z^3+y)/(z^4+m+(3z/2-1)y).

It must be retained in the cubic calculation. In particular, replacing
`W` by `1/z` too early loses a derivative term. The balanced second normal
coordinates are

    a'=z/(z^4+m+(3z/2-1)y)-W^3,
    b'=1/(z^4+m+(3z/2-1)y)-W^4,
    U'=a'/2, V'=-3W a'+2b',
    m'=U'+V', y'=V'.

For a general formal root `m=f(z)y^2+g(z)y^3`, direct expansion gives

    f_infinity(1/z)=z^7 f(z)+p2(z),
    g_infinity(1/z)=z^14 g(z)+C(z)f(z)+D(z)f'(z)+P(z),

where

    p2=(-3z^5+6z^4-12z^3+24z^2)/8,
    C=-2z^11+9z^10-12z^9,
    D=-z^12/2+z^11,
    P=7z^9/16-25z^8/8+9z^7-14z^6+19z^5-18z^4.

The derivative term is the support-coordinate correction. The exact
companion `../computations/verify_mf6_infinity_universal.py` derives these
identities using cubic truncated polynomial arithmetic, with `f,f',g`
independent variables.

Put `w=1/z` on the reduced support. The specified triple has

    delta_infinity=w^4 delta(1/w),
    gamma_infinity=6Aw+6B(1-2w)+48w^2,
    S_infinity=w^5 S(1/w).

In the actual second quartic chart

    x3=1, x2=w,
    x1=w^3+2(m'-y'),
    x0=w^4+y'/2+3w(m'-y'),

let `E_infinity,K_infinity` denote the `m'y'` and `y'^3`
coefficients of `F`, and put

    T_infinity=8 gamma_infinity E_infinity
               +8 delta_infinity K_infinity.

The cubic root there is
`g_infinity=-T_infinity/(8delta_infinity^2 S_infinity)`.
Define the triple-dependent polynomial

    J=3R delta C+3(R' delta-R delta')D+8delta^2 P,
    Jhat=w^17 J(1/w).

The root transition yields the identity

    w^9 T_infinity=w^8 T(1/w)-S_infinity Jhat.       (1)

It holds for every incidence quartic, including all larger exceptional
kernels: its proof uses the universal formal-root transition. The saved
generic vector is only an additional independent direct quartic check.
Exactly `deg J=17` and `Jhat(0)=1/2`.

## 3. Intrinsic one-unit annihilator and the degree argument

The exact DVR lattice lemma in the preceding MF6 audit gives, at every
finite point,

    ord(D3-D2)=max(0,ord S-ord T).

At a zero of `delta`, `R` is a unit, so this remains true for multiple
zeros of `delta`; no simple-root assumption is used. At infinity
`delta_infinity(0)=1`, and the same formula is

    ord_infinity(D3-D2)
      =max(0,ord_0 S_infinity-ord_0 T_infinity).

Therefore a total excess degree at most one is equivalent to the
existence of a nonzero section `L` of `O(1)` annihilating the cubic
residue on the zero divisor of `S`: if the effective excess is one
point, choose that point as the zero of `L`; if it is zero, choose
any nonzero `L`. This includes repeated zeros and the possible extra
point at infinity. Write

    L(z)=l0+l1z, L_infinity(w)=l0w+l1.

The finite condition is exact polynomial divisibility

    L T=S Q.                                      (2)

The degree bound on `Q` must be derived rather than guessed. Let
`n=deg_z S`, so `0<=n<=5` and `ord_0 S_infinity=5-n`.
The left side of (1) has order at least nine, while
`S_infinity Jhat` has order exactly `5-n<=5`. Hence
`w^8 T(1/w)` must have exactly that order. Thus

    deg_z T=n+3,
    deg_z Q<=4.

This conclusion includes all affine degree losses in `S`; in particular
it controls rather than omits infinity zeros.

Multiplying (1) by `L_infinity/S_infinity` and using (2) gives

    w^9 L_infinity T_infinity/S_infinity
      =w^4 Q(1/w)-L_infinity Jhat.                 (3)

The infinity annihilator condition says that the left quotient is
regular at `w=0`. Thus the right side is divisible by `w^9`.
The first term has degree at most four. If
`j_i=coeff_(w^i) Jhat`, coefficients five through eight require

    [j4 j5] [l0]   [0]
    [j5 j6] [l1] = [0]
    [j6 j7]        [0]
    [j7 j8]        [0].                            (4)

For a compact independent specification, set `alpha=A-12,beta=B-4`.
Then the five required coefficients are

    j4=alpha^2/2+8alpha-4beta^2,
    j5=alpha^2-8alpha beta+16alpha+16beta^2-72beta,
    j6=-2alpha^2+16alpha beta-16alpha-32beta^2,
    j7=4alpha^2-32alpha beta-80alpha+64beta^2+288beta,
    j8=-8alpha^2+64alpha beta+128alpha-64beta^2.

The six two-by-two minors of this four-by-two matrix have exact ideal

    ((A-12)^2,(A-12)(B-4),(B-4)^2).

This is certified twice: by an exact rational Groebner calculation, and
by eighteen explicitly recorded linear-polynomial coefficients whose
three combinations of the six minors give `alpha^2,alpha beta,beta^2`.
Conversely every minor has no term below total degree two. Thus the
ideal equality can be checked solely by polynomial expansion, without
trusting a Groebner-basis output. The witnesses are embedded directly
in `verify_mf6_infinity_universal.py`; their discovery output is also in
`../scratch/session-mf6-minor-membership.json`.

Consequently any nonzero `L` forces `A=12,B=4` over an algebraically
closed characteristic-zero field. This conclusion uses the whole
incidence space and the annihilator on `P1`; no resultant, generic
kernel, rank-seven localization, or fixed pole placement is needed.

## 4. Complete remaining exceptional fiber

At `A=12,B=4`,

    delta=(z^2+2z+4)^2, R=z^2+2z+8.

The complete triple/quartic coefficient matrix has rank four, and its
kernel has dimension four. The saved generic kernel specializes to zero
here, so it supplies no quartics at this point.

Direct calculation of the full kernel gives exactly

    H0(I_triple(4))=C3 * H0(P3,O(1)),

where the explicit cubic is

    C3=64x0^2x2+64x0^2x3-64x0x1x2+32x0x1x3
       -16x0x2^2-8x0x2x3-4x0x3^2-64x1^3-32x1^2x2
       +16x1^2x3+8x1x2^2+4x1x2x3-x1x3^2+x2^3.

The companion `../scratch/session-mf6-special-fiber.py` derives the
complete mixed quartic basis, computes all four special kernel vectors,
and certifies equality with `C3*<x0,x1,x2,x3>` by an exact quartic
monomial coefficient matrix of rank four. Its exact output is preserved
in `../scratch/session-mf6-special-fiber.json`.

Every nonzero remaining quartic thus has an ambient plane factor. It
cannot occur in a defining pair with radical support `C0`: if the plane
factor divides the mate, the pair has a common surface; otherwise the
mate restricts to a nonzero positive-degree homogeneous equation on
that plane and cuts a nonempty projective curve in it. That curve would
be contained in the integral nonplanar `C0`, which is impossible.

This proves that the
`e=0,(d2,d3)=(4,5)` numerical branch is empty for the hypothesized
`(4,6)` presentation of `C0`. It does not settle the unrestricted STCI
question for `C0`, larger degree pairs, `e=1`, or the entirely-thick branch.

## 5. Additional exact boundary evidence and discarded work

For provenance, the seven nonzero rows of the original 13-by-8 matrix
have signed maximal minors exactly equal to the saved primitive kernel
vector (no nonconstant common factor). Their ideal has geometric support
at six points:

    (12,4), (-12,-2),
    (0,B), B^2-2B+4=0,
    (-12,B), B^2+4B+40=0.

The exploratory Groebner output is in
`../scratch/session-mf6-rank-boundary.json`. These other rank-drop fibers
need not be separately classified for the proof, because (4) eliminates
them independently of the quartic kernel. An attempted algebraic-field
factorization of all six fibers was interrupted after checking two
members at `(12,4)`; no missing factorization is used as evidence.
The useful exact special fiber was instead checked by rational linear
algebra. No full resultant was launched in this continuation.

## Reproduction and remaining audit

Run with bytecode disabled:

    PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_mf6_infinity_universal.py
    PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/scratch/session-mf6-special-fiber.py

The universal verifier reconstructs the complete original coefficient
matrix, its generic vector for the additional direct chart check, and
the entire four-dimensional exceptional quartic fiber from the original
ideal basis. It has no generated-JSON input dependency. Its universal
proof inputs are the exact formal transition, the complete mixed quartic
first-normal kernel, the four-by-two polynomial matrix, and the explicit
ideal-membership witnesses. The shorter special-fiber scratch verifier
reads the regenerated matrix and reconstructs the same original quartics;
it is corroboration rather than a necessary external proof input.
## Completed independent audit and exact validation

On 2026-10-07 the root agent separately derived (1)--(4), including
`deg T=deg S+3` when `S` loses degree, and checked the global length-one
annihilator on both charts. The root also reconstructed the shifted
`j4,...,j8` by hand and independently computed their minor ideal
`(alpha,beta)^2` in SymPy. It checked that the sole remaining full fiber
has rank four, rather than substituting its vanishing generic vector.
The proof was accepted under the stated characteristic-zero, fixed-C0,
quasiprimitive saturated-filtration hypotheses.

The final combined verifier passed through all assertions, including
both the exact Groebner equality and the explicit membership witnesses,
nonzero `S`, nonlinear moving-support correction, direct generic chart
expansion, and complete exceptional-fiber cubic factorization. Its
stdout is preserved in
`../scratch/session-mf6-infinity-universal-output.txt`.
The optional witness parser initially treated `beta` as SymPy's beta
function; explicit local symbols corrected this software-only issue,
and the entire combined verifier was rerun successfully. No mathematical
assertion depended on that failed parser run.

The next open MF6 branch is `e=1`, with types `(0,4),(1,3),(2,2)`.
The regular `e=0,(3,6)` member remains open. This result therefore
eliminates all remaining **nonregular constant-direction** `(4,6)`
strata, while leaving those stated regular and degree-one-direction
possibilities.


---

## 2026-10-06-session-normal-carrier-progress

# Session normal-carrier progress: exceptional passage and reduced cycles

Started 2026-10-06; persisted and extended 2026-10-07 after interruption.
Scope: characteristic zero, the fixed smooth monomial rational quartic
`C0=[s^4:s^3t:st^3:t^4]`, an integral **normal quartic carrier**, and an
arbitrary ambient mate. This is a new session note, not a replacement for
the canonical audited state. On 2026-10-07 `frontier_audit` independently
accepted sections 2--6, including a separately rebuilt exact enumeration;
the root also audited the passage, Cauchy and local `A2` arguments. The
nonreduced tree enumeration in section 9 was then independently rebuilt
and accepted; the root separately checked the cohomology/tree proof and
the Type-D passage argument against the primary source. Verification
also reran the stabilized sources live with matching output hashes.
The complete normal-quartic exclusion below is accepted under the
explicitly recorded classification, compression, ADE-classification and
normal-sheaf inputs.

## Checkpoint and claimed progress

1. **PROVED / independently audited:** a smooth embedded curve
   passes through an isolated surface singularity by meeting exactly one
   exceptional prime transversely at a smooth point of the reduced
   exceptional divisor on its resolution.
2. **PROVED / independently audited:** the anticanonical
   intersection and numerical correction satisfy `t+q=6`; Cauchy's
   inequality and denominator compression leave `t=1` for `d=1`, and
   `t in {1,2}` for `d=2,3`.
3. **PROVED / independently audited:** every irreducible
   anticanonical exceptional divisor is excluded, including a singular
   irreducible genus-one divisor.
4. **PROVED through an independently audited exact reduction:** for reduced reducible
   anticanonical divisors, an exhaustive cycle/ADE numerical scan leaves
   five configurations. Four compress to a forbidden quadric mate. The
   fifth has compressed mate degree six and is then excluded by the
   independently proved normal-sheaf defect formula, using its six `A1`
   points and one `A2` point.
5. **PROVED / independently audited:** the nonreduced divisor has a rational
   SNC tree support; the complete bounded graph enumeration leaves only
   Type-D coefficient-two passages, which the Type-D coordinate basis
   excludes. Thus every normal quartic carrier is excluded.
6. **OPEN:** nonnormal quartic carriers, higher-degree minimum carriers,
   and the entirely-thick branch. No conclusion that `C0` is not STCI is
   asserted.

The normal quartic lane for `C0` is now closed, whatever the mate degree.

## 1. Inputs reconstructed and checked

The controlling state is `research/AUDITED_STATE_2026-10-06.md`. Its normal
lane already excludes rational-singularity quartics, positive-genus ruled
quartics, avoidance of the nonrational locus, and smooth simple-elliptic
exceptional divisors. The remaining rational-resolution types of
Ishii--Nakayama have

| `d=-E^2` | types | `rho(M)` |
|---:|---|---:|
| 1 | B2/B3 | 11 |
| 2 | B1 | 12 |
| 3 | D | 13 |

Here `sigma:M -> S` is the **minimal** smooth resolution, `H` is the
hyperplane pullback, and `K_M=-E` with integral effective exceptional `E`.
The minimality, effective discrepancy divisor, Picard numbers and
exhaustiveness are explicit in [Ishii--Nakayama's author
preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1370.pdf),
pp.7, 14, 17, 19 and 23, and in the
[published paper](https://www.jstage.jst.go.jp/article/jmath1948/56/3/56_3_941/_pdf).
The saved convenience extraction `/private/tmp/stci-normalquartic-rims1370.txt`
was inspected in this session. The classification is geometric, not an
inference from an ADE table or examples.

The proof of `2026-10-06-normal-rational-carrier-compression.md` was
rechecked: a mate gives `c+Z == H`; clearing the denominators produces an
integral numerically trivial divisor on the rational surface `M`, hence a
principal divisor. Pushforward and ambient section lifting produce a
mate of exactly the numerical denominator `n`. Every actual mate degree
is divisible by `n`. The argument requires normality, a rational **whole
resolution**, and existence of a mate. In particular one cannot use
numerical coincidence on an arbitrary nonrational resolution to discard
local Picard torsion.

The determinant proof also remains applicable: all exceptional classes
have rank at most `9+d`, and minimality gives
`sum (b_i-2)_+ <= d` for `b_i=-E_i^2`. Thus its bounds 1536, 4608, 13824
are valid even for nonreduced or singular `E`.

The normal-sheaf inequality in `2026-10-05-mumford-normal-bound.md` was
read through its ideal-principalization proof. For a generically regular
carrier it supplies the exact nonnegative defect

`deg N_(C/S) - (C#)^2 = (Z_ideal-Z_num).c >= 0`.

It applies here since a normal surface is regular at the generic point
of the curve. Contributions over different singular points are additive.
The global first-normal symbol of a quartic is a nonzero pair of binary
forms of degree nine, so its total common order is `9-e <= 9` and
`deg N_(C/S)=7-e`. These identities use the audited balanced normal bundle
`N_C=O(7)^2` of the fixed `C0`. We retain the audited stronger `e<=2`,
although only `e>=0` is needed in the new exclusions.

## 2. Smooth passage lemma, including singular primes and crossings

Let `p` be an isolated singular point of an integral normal surface
`S` containing a smooth curve `C`, and let `sigma:M -> S` be any smooth
proper resolution. Its strict transform `c` maps isomorphically to `C`:
the rational lift from the smooth proper curve extends by the valuative
criterion, giving a section and hence a closed immersion.

At its point `x` over `p`, let `E_i` run through the exceptional prime
curves. For every local function `f in m_(S,p)`, its pullback vanishes on
every exceptional prime above `p` with integer order at least one. Since
`M` is smooth, each prime divisor is locally principal, and the product
of their distinct local equations divides `sigma^*f`. This remains true
when an exceptional prime is singular or several exceptional primes
cross: smoothness of `M`, not smoothness of these divisors, supplies the
local divisor factorization. Restriction to `c` gives

`ord_x(f|c) >= sum_(E_i over p) (c.E_i)_x`.

The maximal ideal of `S` maps onto the maximal ideal of `C`; some `f`
therefore restricts to a uniformizer of the smooth curve, of order one.
The strict transform must meet the exceptional fiber. Thus

`sum_(E_i over p) c.E_i = 1`.

Every nonzero term is a positive integral scheme intersection length.
Consequently `c` meets exactly one exceptional prime, with intersection
length one. That point is smooth on the prime and outside all other
exceptional primes; otherwise the relevant local intersection length or
the sum would be at least two. The intersection is transverse. In the
matrix notation, the passage vector at each singular point is a single
standard basis vector, not an arbitrary nonnegative vector.

For the rational normal quartics at hand, `E` is connected: Proposition
1.1 of Ishii--Nakayama gives `h^0(E,O_E)=1`. An exceptional prime with
coefficient zero in `E` is disjoint from its support, as follows from
minimality and adjunction in the preceding compression note. Connected
exceptional fibers therefore show that the support of `E` is the entire
fiber of the unique nonrational singular point. All other singular fibers
are ADE. The already proved avoidance exclusion forces `C` through this
nonrational point. Its anticanonical passage `t=c.E` is thus precisely the
coefficient of the exceptional prime selected by the passage lemma.

## 3. A small anticanonical passage bound

Write all exceptional primes as `E_i`, put `A_ij=-E_i.E_j`,
`E=sum a_i E_i`, `m_i=c.E_i`, and `Z=sum z_i E_i` with
`z=A^(-1)m`. Set

`t=a^T m=c.E > 0`, `q=m^T A^(-1)m=-Z^2`, `d=a^T A a=-E^2`.

Adjunction on the smooth rational strict transform gives `c^2=t-2`.
The mate relation gives `c+Z == H`, whose square is four. Orthogonality
to exceptionals gives `(c+Z)^2=c^2+q`, so

`t+q=6`.

Cauchy--Schwarz in the positive definite form `A` gives

`t^2 <= d q = d(6-t)`.

Hence the positive integer possibilities are `t<=2` for `d=1,2`, and
`t<=3` for `d=3`. Equality occurs at `(d,t)=(1,2)` or `(3,3)` and forces
`z=(t/d)a`, respectively `2a` or `a`. In both cases `Z` is integral and
the numerical denominator is one. Compression would produce a plane
mate, impossible for a nondegenerate degree-four curve. Thus

| `d` | remaining `t` |
|---:|---|
| 1 | 1 |
| 2 | 1 or 2 |
| 3 | 1 or 2 |

In particular a nonreduced surviving exceptional divisor must have a
prime with coefficient one or two available to the smooth passage; for
`d=1` the selected prime has coefficient one.

## 4. Irreducible anticanonical divisors are excluded

If `E=aP` is irreducible as a support, then `d=a^2(-P^2)<=3` forces
`a=1`. Thus every irreducible `E` here is reduced. Its arithmetic genus
is one by adjunction. The passage lemma gives `c.E=1`, including when
`E` is a nodal or cuspidal rational curve: a smooth embedded `C` cannot
meet its singular point on `M`.

Orthogonality gives local correction `Z_irr=E/d`, with contribution
`q_irr=1/d`. The whole correction is `q=5`, so the ADE points on `C`
would have to contribute `5-1/d`. Their total root rank is at most
`N=8+d`, because `H`, the irreducible `E`, and the ADE roots are independent.

Every **nonrational isolated hypersurface** singular point on a smooth
curve has first-normal common order at least two. To verify this without
a local irrational-singularity classification, straighten the smooth
support to the `x` axis. Order one would give a quadratic term
`x(ay+bz)+Q(y,z)` with `(a,b)!=(0,0)`. Its quadratic rank is at least two.
The characteristic-zero analytic/formal splitting lemma then writes
the isolated hypersurface germ as `uv+h(w)`, or as a nondegenerate
quadratic germ. Isolation makes `h` a nonzero one-variable power series;
the result is an `A_n` rational double point. This contradicts
nonrationality. The argument transfers from complex coefficients in the
same way as the classification inputs in the earlier note.

At most seven of the nine first-normal zeros remain for ADE points.
Jaffe's smooth curve--ADE classification, recorded and checked in
`2026-10-05-normal-quartic-carriers.md`, gives the harmonic inequality

`q_ADE <= N P/(N+P)` with `P=sum s_i <=7`.

It now contradicts the required correction in every row:

| `d` | required `q_ADE` | harmonic maximum | positive gap |
|---:|---:|---:|---:|
| 1 | 4 | `63/16` | `1/16` |
| 2 | `9/2` | `70/17` | `13/34` |
| 3 | `14/3` | `77/18` | `7/18` |

This excludes all irreducible exceptional anticanonical divisors, without
assuming smooth ellipticity or any upper bound on the mate degree.

## 5. Reduced reducible divisors: exact cycle reduction

Suppose `E` is reduced and reducible, with `k` primes. Connectedness was
proved above. Adjunction on each prime gives

`sum_(j!=i) E_i.E_j = 2-2p_a(E_i)`.

A prime of arithmetic genus one would have no neighbors and contradict
connectedness. Every prime therefore has arithmetic genus zero and is a
smooth rational curve, with total intersection two with the others.
The connected weighted multigraph is a cycle. For `k=2` the two primes
have intersection two; for `k>=3` its edges have intersection one. It
may have coincident intersection points or tangent intersection schemes;
the matrix reduction does not assume simple normal crossings. The smooth
passage avoids all such points by section 2.

Minimality gives `b_i=-E_i^2>=2`. Since the coefficient vector is all
ones,

`sum_i (b_i-2)=d`, `2<=k<=9+d`.

These are a genuinely finite set of cycle matrices: choose a weak
composition of `d` into `k` entries and set the diagonals to two plus
those entries. The matrix for the two-prime cycle has off-diagonal `-2`;
larger cycles have adjacent off-diagonal `-1`. Its negative definiteness
is equivalently the positive definiteness of this matrix; all the listed
matrices are positive definite because at least one diagonal exceeds two.

The passage lemma makes `m_irr` a unit vector. Thus each numerical
candidate is determined by the selected diagonal entry
`q_irr=(A^(-1))_(jj)` and the common denominator of column `j`.
The ADE points must satisfy

`N_ADE<=9+d-k`, `P_ADE<=7`, `q_ADE=5-q_irr`.

The exact companion enumerates every allowed ADE pair row, every multiset
of them under these rank and order budgets, and every cycle column. It
uses the entire correction-column denominator, not merely the denominator
of its square. Rotations/reflections and identical `(d,k,q,index)` data
are deduplicated, which does not affect existence in these numerical tests.

Exactly five configurations remain after the correction equality:

| `d` | cycle weights | selected prime | `q_irr` | ADE pairs | compressed degree |
|---:|---|---|---:|---|---:|
| 1 | `(-2,-3)` | `-2` | `3/2` | seven `A1` | 2 |
| 1 | `(-2,-3)` | `-2` | `3/2` | five `A1`, one `A3^2` | 2 |
| 1 | `(-3,-2,-2,-2)` | opposite `-3` | 2 | six `A1` | 2 |
| 2 | `(-4,-2,-2,-2)` | opposite `-4` | `3/2` | seven `A1` | 2 |
| 3 | `(-5,-2,-2,-2)` | opposite `-5` | `4/3` | six `A1`, one `A2^1` | 6 |

The four denominator-two rows are impossible: the conditional
compression theorem produces a quadric mate. For `C0` the unique-quadric
obstruction rules it out. This is an actual compressed mate conclusion
under the hypothetical original mate, not a cancellation of a local
torsion scalar without its global hypothesis.

## 6. The degree-six numerical survivor is excluded by normal-sheaf defect

The final row uses all seven allowed ADE first-normal orders. The
nonrational point uses at least two. Hence the whole first-normal common
order is exactly nine and `e=0`. The available global normal-sheaf defect
is therefore

`deg N_(C/S)-(C#)^2 = 7-4=3`.

Each of the six `A1` passages contributes `1/2` to this nonnegative
defect, by the exact local model already proved in
`2026-10-05-mumford-normal-bound.md`. The `A2^1` passage contributes
`1/3`. To check the latter directly, use

`S: xy=z^3`, `C: x=z=0`.

The ordinary point blowup resolves this `A2` surface with two `(-2)`
curves. On the `y` chart, put `y=t,z=tu,x=t^2u^3`; the strict support is
`u=0`, and its ideal is `(x,z)=(tu)`. On the `x` chart the ideal is
generated by `x`. On the `z` chart put `x=zX,y=zY`, so `z=XY` and
`(x,z)=(XY)`. The ideal exceptional coefficient is one on each of the
two exceptional curves. The numerical coefficient at the prime met by
the support is `2/3`, from the inverse of `[[2,-1],[-1,2]]`. The defect
is thus `1-2/3=1/3`.

The `A2^1` smooth pair is the unique `A2` passage from Jaffe's
classification (the two symmetric ends are equivalent), so this model
applies to the surviving row. Contributions over all other points are
nonnegative by the proved ideal-principalization comparison. Therefore

`3 >= 6*(1/2)+1/3=10/3`,

a contradiction. Equivalently the surviving nonrational passage would
need too little ideal correction for its numerical correction `4/3`.
This eliminates the final reduced-cycle numerical configuration.

## 7. First checkpoint boundary and evidence (superseded by sections 8--11)

The independently audited new conclusion is: **a normal quartic carrier for
`C0` in characteristic zero, if it has any mate, must have a reducible
nonreduced exceptional anticanonical divisor.** Its smooth nonrational
passage selects a coefficient-one prime for `d=1`, or a coefficient-one
or coefficient-two prime for `d=2,3`. The exact identities `t+q=6` and
the existing denominator bounds remain necessary.

At this first checkpoint it was not a normal-quartic global exclusion:
the nonreduced case was retained. The next step was a classification or an exact graph audit
of the nonreduced anticanonical cycles under `a^T A a=d<=3`, relative
nefness, rank at most `9+d`, and the selected coefficient at most two.
One must preserve the local smooth-passage condition and the full
correction denominators, and must not identify these configurations with
reduced cusp cycles.

Exact companion and saved output:

- `research/computations/verify_session_normal_carrier_progress.py`;
- `research/computations/session_normal_carrier_progress_2026-10-07.json`.

The companion checks the rational gaps, passage-bound arithmetic, exact
cycle enumeration, all ADE correction/index data used in the scan, the
five remaining numerical rows, and the final defect contradiction.
Its output checks numerical implications, not existence of the surfaces,
the source classification, or the geometric passage lemma. Those are
separate proof obligations explicitly supplied above.

## 8. New checkpoint: the nonreduced support is a rational SNC tree

Status: proof supplied and independently accepted by the root on 2026-10-07.
This supplies the smaller exact graph problem for the nonreduced lane;
its complete enumeration is recorded in section 9.

On the smooth projective rational surface `M`, both `H^1(O_M)` and
`H^2(O_M)` vanish. For any nonzero **proper** effective subdivisor
`0<D<E`, the sequence

`0 -> O_M(-D) -> O_M -> O_D -> 0`

and Serre duality give

`H^1(O_D) = H^2(O_M(-D)) = H^0(O_M(K_M+D))^*`

`=H^0(O_M(D-E))^*=0`.

The last vanishing follows because `E-D` is a nonzero effective divisor:
a global section of its negative ideal would be a global regular
function on the proper connected surface vanishing there, hence zero.
This is an actual cohomology statement, not an inference from arithmetic
genus alone.

Every prime of the now retained reducible `E` is a proper subdivisor, so
it has arithmetic genus zero and is a smooth rational curve. If `E` is
nonreduced, its reduced support `R=E_red` is also a proper subdivisor.
It is connected, has `h^0(O_R)=1`, and the above argument gives
`h^1(O_R)=0`; therefore `p_a(R)=0`. Adjunction, adding the individual
prime adjunction formulas, gives

`sum_(i<j) E_i.E_j = k-1`.

Connectedness forces at least `k-1` graph edges, each carrying a positive
integer intersection length. Equality forces a tree with simple edges of
intersection length one. There are no tangent intersections, and no
three primes can pass through the same point, since that would produce
a cycle of three pairwise edges. Consequently the support is a simple
normal crossing tree of smooth rational curves.

The residual matrix equations are thus exactly

`A_ii=b_i>=2`, `A_ij=-1` on tree edges and zero elsewhere,

`A a = b-2`, `a_i in Z_(>0)`, `a^T A a = sum a_i(b_i-2)=d`,

`1<=d<=3`, `2<=k<=9+d`, `some a_i>1`.

Positive definiteness remains mandatory. At the nonrational point the
selected smooth-passage prime has `a_j=1` if `d=1`, or `a_j in {1,2}`
if `d=2,3`; its correction is the selected diagonal of `A^(-1)` and its
full numerical denominator is that inverse column's denominator.
Every other point on `C` is ADE with the same rank and first-normal
budgets as above, but now the required correction is

`q_ADE = 6-a_j-(A^(-1))_(jj)`.

Since `a_i>=1`, the diagonal excess satisfies
`sum(b_i-2)<=d<=3`, so these are a finite set of nonisomorphic trees of
at most twelve vertices with at most three total units of diagonal
excess. This finite numerical graph problem is a **necessary** condition
for the classified surfaces. Passing it will not establish realizability
or a smooth local passage, and failing it would supply an exclusion only
after all its equations and admissible rows are independently audited.

The root supplied a further coefficient-one simplification. At a prime
with `a_i=1`, the equation `Aa=b-2` says that the sum of neighboring
coefficients is two. It is therefore either a leaf attached to a
coefficient-two prime or a valency-two vertex with two coefficient-one
neighbors. The latter situation propagates along coefficient-one
vertices and cannot reach a larger coefficient without encountering a
coefficient-one leaf; connectedness of a finite tree with some coefficient
greater than one forces the first case. Thus every coefficient-one prime
of this nonreduced tree is a leaf attached to a coefficient-two prime.

## 9. Exact nonreduced tree enumeration

Status: exact source completed and `PASS` in the live checkout on
2026-10-07; `frontier_audit` independently rebuilt the graph enumeration
and obtained the same 381802 trials, 195 cycles and twelve post-compression
rows. Sections 8 and 10 have separate root proof audits. Verification
independently reran the stabilized source in 22.899 seconds with a saved
JSON hash matching this checkout's output.

The source `verify_session_normal_nonreduced_trees.py` enumerates every
unweighted nonisomorphic tree of sizes two through twelve by adding a
leaf at every vertex of every tree at the previous size, then comparing
exact rooted tuple codes over all possible roots. Induction is exhaustive
because every tree has a leaf. The counts by size are

`1,1,2,3,6,11,23,47,106,235,551`.

For each tree it enumerates every nonnegative excess vector `v=b-2` of
total one, two or three. There is no missing zero-excess case: positive
definite `A` and `Aa=0` would imply `a=0`, contrary to effective nonzero
`E`. Every necessary positive excess vector has sum at most three, by
section 8. Leaf Schur elimination checks positive definiteness with exact
fractions and solves `Aa=v`; every resulting solution is independently
substituted into the full original equations. The filter retains exactly
positive integral coefficients and `d=a.v in {1,2,3}`, with `k<=9+d`.
Weighted tree isomorphisms are then deduplicated by exact tuple codes.

The 381802 diagonal modifications leave 195 numerical canonical cycles:
nine for `d=1`, 59 for `d=2`, and 127 for `d=3`. These are a finite
**superset** of the classified geometric configurations. No analytic
realizability or proper-subcycle cohomology conditions are imposed, so
discarding all of them is legitimate; retaining one would not establish
existence on a quartic.

At every possible selected coefficient one or two allowed by section 3,
the source solves the unit-column correction exactly, takes the least
common denominator of **every** entry in that column, and compares
`6-t-q_irr` with every ADE multiset under the rank and order budgets.
There are 236 exact correction matches. The known compressed mate-degree
exclusions up through degree five eliminate 224. Twelve rows remain:

| nonrational rank | `q_irr` | `t` | number of rows | ADE data |
|---:|---:|---:|---:|---|
| 5 | 2 | 2 | 5 | correction 2, rank 4--7, order 3 or 4 |
| 7 | 2 | 2 | 2 | correction 2, rank 4 or 5, order 4 |
| 8 | 2 | 2 | 1 | four `A1` points |
| 8 | `17/6` | 2 | 4 | one `A1` and one `A2^1` |

**Every remaining row has `d=3` and `t=2`.** Their compressed degrees are
six or twelve. The saved JSON includes the full 195 graph/diagonal/
coefficient data and each surviving full correction column, so this
assertion can be reconstructed rather than inferred from a total count.

Exact source:
`research/computations/verify_session_normal_nonreduced_trees.py`.
Saved output:
`research/computations/session_normal_nonreduced_trees_2026-10-07.json`.
The source emits JSON on stdout and makes no internal file writes. Its
only dependency is the earlier reduced-cycle companion, whose exact
ADE root matrices and multiset states are revalidated through `runpy`.

## 10. Type D has anticanonical passage one on every smooth embedded curve

Status: source and geometric proof independently accepted by the root on
2026-10-07. This proof does not depend on the tree enumeration or a mate.

Ishii--Nakayama §2.4, author preprint p.23 (published p.955), supplies the
following exact description for **all** Type-D surfaces, by the exhaustive
Main Theorem. There is a separation `rho:M -> P^2` of a smooth plane
quartic `B` and an effective cubic divisor `G`. It satisfies

`K_M+H ~ rho^*(K_(P^2)+B) ~ rho^*O_(P^2)(1)`.

Thus `H-E ~ rho^*O_(P^2)(1)`. More precisely, the four basis sections
of `H` are

`xi0=phi4`, `xi1=phi3 rho^*x`, `xi2=phi3 rho^*y`,
`xi3=phi3 rho^*z`,

where `phi3` cuts out the **entire** exceptional divisor `E`, including
its multiplicities, and `phi4` cuts out the pulled-back smooth hyperplane
section `D`, which is disjoint from `E`. The three pulled-back coordinate
sections have no common zero on `M`. The image of `E` is
`p=(1:0:0:0)`, and projection from `p` is the map induced by `rho`.
The explicit basis and the image assertion are in the source; they are
not reconstructed from a generic cubic example.

Near the exceptional fiber `E`, `xi0` is a unit in a local trivialization.
The three affine ambient coordinates `xi1/xi0`, `xi2/xi0`, `xi3/xi0`
generate the maximal ideal of `p` on `S`. Their pullback ideal is exactly
`O_M(-E)`: each has the factor `phi3`, and the three remaining coordinate
sections are basepoint-free. On any smooth curve `C` through `p`, the
maximal ideal of `S` maps onto the maximal ideal of `C`, whose order is
one. Restricting the pulled-back ideal to its isomorphic strict transform
therefore gives

`c.E = 1`.

This holds even when `E` is nonreduced. It forbids the selected
coefficient-two passage in every row remaining in section 9. In
particular the elimination is geometric, rather than a prediction of an
unverified lower bound for the local Jacobian common order.

## 11. Complete normal-quartic exclusion and its boundary

Sections 1--10 and their independent audits establish:

> For `C0=[s^4:s^3t:st^3:t^4]` in characteristic zero, no integral normal
> quartic surface can be a carrier in a set-theoretic complete
> intersection presentation, whatever the mate degree or common singular
> points.

The older rational-singularity, ruled-resolution and avoidance exclusions
dispose of the earlier classes. The reduced-`E` case is independently
accepted in sections 2--6. Rational-surface cohomology reduces nonreduced
`E` to the finite tree problem; the exact numerical scan leaves only
Type-D coefficient-two passages, which section 10 excludes.

The primary classification and analytic ADE inputs are stated over the
complex numbers. The theorem applies over **every algebraically closed
characteristic-zero field** as follows. A hypothetical finite-degree
pair has finitely many coefficients. Radical equality with the homogeneous
prime ideal of the fixed `C0` has finite witnesses: both carrier equations
belong to that prime, and a positive power of each of its finitely many
generators belongs to the two-equation ideal. Descend those coefficients
and witnesses to a finitely generated subfield `k0` of characteristic zero.
Its algebraic closure can be taken inside the original algebraically
closed field. Faithfully flat descent from the original field shows that
the carrier over that algebraic closure is integral and normal; thus the
model over `k0` is geometrically integral and geometrically normal. These
properties persist after field extension. Embed `k0`, and then its
algebraic closure, in the complex numbers. The finite polynomial witnesses
still express the same radical equality after this extension, and `C0`
remains its fixed smooth nondegenerate quartic. The resulting complex
hypothetical pair contradicts the complex proof above. This transfer
uses neither uncountability of the original field nor specialization of
singularity types at an uncontrolled parameter value.

Independent audit:
`research/notes/2026-10-07-session-normal-carrier-independent-audit.md`,
and `research/notes/2026-10-07-session-normal-nonreduced-independent-audit.md`,
with separately built reduced-cycle and nonreduced-tree numerical data.
The certificate sources stabilized at SHA-256
`57c73e7fc597d892dde3628dc0a7c0da2e6e61514af7890118e057f29b5cef13`
(reduced-cycle companion) and
`fca8eb7c177d88d00adcf5c60f664f8bbf9926abaf586762f22bfedf4199a2a7`
(nonreduced-tree companion). Numerical verification and geometric proof
audits remain distinct; the Type-D coordinate factorization is a primary-
source geometric input, not an output discovered by the enumeration.

The result is explicitly about **normal quartic carriers for the fixed
curve `C0`**. It does not exclude nonnormal quartic carriers, pairs whose
minimum carrier degree exceeds four, or the entirely-thick branch, and
does not prove `C0` is not STCI. The universal integral-curve problem
therefore remains open in this repository.


---

## 2026-10-06-session-thick-independent-audit

# Independent audit of the uniform entirely-thick numerical restriction

Date: 2026-10-06. Status: **proved necessary condition**, independently
derived from the blowup intersection identities; a further **proved
conditional boundary reduction** is included below. Neither assertion
excludes the entire thick branch. No claim of novelty is made.

## Hypotheses and properness

Work over an algebraically closed field of characteristic zero. Let
`C ⊂ P³` be a smooth nondegenerate rational quartic, lying on its smooth
quadric `Q`, with ruling convention `C=(1,3)`. The checked normal bundle is
`N_(C/P³)=O_P¹(7)⊕O_P¹(7)`.

Suppose homogeneous forms `F_a,G_b` have reduced common projective support
exactly `C`. Write their exact generic normal orders along `C` as `p,q`;
the entirely-thick branch has `p,q≥2`. The argument works for arbitrary
positive `p,q` and does not require either surface to be integral.

The two forms have no common irreducible surface factor, since that factor
would be a component of their common zero support. Neither is divisible by
the quadric equation: if one were, its common zero set with the other would
contain the zero divisor of the other's restriction to `Q`, which cannot
have support `C` alone because `(b,b)` is not a positive multiple of
`(1,3)`. A restriction identically zero on `Q` also gives a common surface.

Consequently `F|Q=h^p R_F` and `G|Q=h^q R_G`, where `h=0` cuts out `C`
on `Q`, and the nonzero residual sections have classes

    R_F ∈ H⁰(Q,O_Q(a-p,a-3p)),
    R_G ∈ H⁰(Q,O_Q(b-q,b-3q)).

The displayed exponents need not be the exact orders on `Q`: a residual
section can itself be divisible by `h`. They imply `a≥3p,b≥3q` nonetheless.

Put `B=Bl_C P³`, let `H` be the hyperplane pullback, and let `E` be the
exceptional divisor. The strict transforms are effective Cartier divisors

    D=aH-pE,  D'=bH-qE.

They have no common surface component, so their scheme intersection is a
proper Cartier complete intersection on the smooth threefold `B`. It is
Cohen--Macaulay and pure of dimension one. Its fundamental cycle `W=D·D'`
is effective. The blowup is an isomorphism off `E`, and the original
equations have no common point off `C`; hence the entire scheme
intersection, and in particular its cycle, is supported in `E`.

This addresses possible hidden issues: nonreduced surface equations and
vertical exceptional components are allowed; an embedded zero-dimensional
component does not arise in this Cartier complete intersection. In any
event, a zero-dimensional component could not change the cycle numerics.

## Independent numerical derivation

Use the same bidegree convention as P-020:

    E≅P¹×P¹,
    H|E=O_E(4,0),  E|E=O_E(7,-1),
    H³=1,  H²E=0,  HE²=-4,  E³=-14.

Write the class of the effective curve cycle on `E` as `(u,v)`. The two
intersection numbers determine this class, because

    H·W=4v,
    E·W=7v-u.

Direct expansion in the blowup gives

    H·D·D' = ab-4pq,
    E·D·D' = 4(aq+bp)-14pq.

Therefore

    v = ab/4-pq,
    u = 7ab/4+7pq-4(aq+bp).                         (T1)

Every irreducible effective curve on `P¹×P¹` has nonnegative bidegrees.
Taking positive cycle multiplicities preserves this property, including
for vertical fibers. Thus an STCI pair must satisfy

    ab≥4pq,
    7ab+28pq≥16(aq+bp).                            (T2)

With `α=a/p,β=b/q`, the second inequality reads

    7αβ/4+7≥4(α+β),  α,β≥3.                       (T3)

For `α=3`, it forces `β≥4`; by symmetry, `β=3` forces `α≥4`.
In particular every pair with both `a=3p` and `b=3q` is excluded, at all
normal orders. For `a=b=6,p=q=2`, the formula gives `(u,v)=(-5,5)`,
recovering the thick-sextic contradiction in P-018.

The inequality does not give an upper bound on `p,q,a,b` and does not
exclude the region of large degree-to-order ratios. Its proof does not
assume any bound on later normal jets or local contact multiplicity.

## Further consequence at numerical equality

Assume now the boundary values

    a=3p,  b=4q.

Then `(T1)` gives `(u,v)=(0,2pq)`. Every irreducible curve in the support
of `W` therefore has class `(0,1)`: these are constant sections of the
exceptional `P¹`-bundle over `C`. Let their distinct supports be
`T₁,...,T_r`. There are no vertical components in this equality case.
Restriction of each strict-transform divisor to `E` gives

    D|E=(5p,p),  D'|E=(9q,q).

Every `T_j` is a component of both restricted divisors. Fiber degree
therefore bounds the number of distinct sections:

    r≤min(p,q).                                    (T4)

The quadric-direction section is `S_Q=Q^strict∩E`, with class `(1,1)`.
Each `T_j` meets `S_Q` in exactly one reduced point: geometrically `S_Q`
is the graph of a degree-one automorphism from the base to the normal
direction projective line, and `T_j` has constant direction.

Here

    R_F has class (2p,0),
    R_G has class (3q,q).

Thus `R_F` is a binary form of degree `2p` in the coordinate indexing the
trisecant ruling lines of `Q`. Consider one distinct ruling component
`ℓ` of `R_F`. It is contained in `V(F)`. The restriction `G|ℓ` is
nonzero, or else `ℓ` would be an extra common curve. Equivalently
`R_G|ℓ` is a nonzero section of `O_ℓ(q)`. Since `q>0`, it has a zero
`P`. The STCI support condition forces that zero to lie in `ℓ∩C`,
because `G|ℓ=(h|ℓ)^q(R_G|ℓ)` and every zero of `G|ℓ` must lie in `C`.

Let `P̃` be the point of `S_Q` above `P`. The restriction of the
`p`-th normal form of `F` to `S_Q` is exactly `R_F|C`; its value at `P`
is zero. Similarly the restriction of the `q`-th normal form of `G` is
`R_G|C`, so its value at `P` is zero. Hence

    P̃∈D∩D'∩S_Q.

This conclusion also holds if `h|R_G`, in which case the latter normal
form vanishes identically on `S_Q`. It only uses divisibility by `h^q`,
not the assertion that `q` is the exact order of `G|Q` along `C`.

Purity of the Cartier intersection makes every point of `D∩D'` belong
to its one-dimensional support, which here is `T₁∪...∪T_r`. Each `T_j`
supplies only one point on `S_Q`. Distinct ruling lines of this family are
disjoint, so distinct components `ℓ` require distinct such points. Thus

    R_F has at most r≤min(p,q) distinct ruling roots. (T5)

The multiplicities sum to `2p`; at least one root therefore has
multiplicity at least `ceil(2p/min(p,q))`. This is a repeated-root
reduction on the equality boundary, not a contradiction or a construction.
It does not use the split/content-free/no-vertical assumptions of P-020.

If one additionally assumes the first-normal divisor of `F` has no
vertical component, then `r=p` is impossible: factoring off `p` constant
sections leaves an effective divisor of class `(5p,0)`, which is a nonzero
union of vertical fibers. Under that additional hypothesis `(T4)` can be
strengthened to `r≤min(p-1,q)`.

## Why first tangent forms cannot cap the cycle multiplicities

Over the generic coefficient field `K=k(C)`, fix normal orders `p=q=2`.
For any integer `n≥1`, take the two local equations

    f=y²+x^(2n+1),
    g=y²+2x^(2n+1)

in `K[[x,y]]`. In characteristic zero both germs are irreducible, since
the exponent `2n+1` is odd. They have the same first tangent polynomial
`y²` and reduced common support the origin. Subtracting their equations
gives the exact transverse length

    length K[[x,y]]/(f,g)=2(2n+1)=4n+2.

On the blowup chart `y=xz`, the strict-transform equations are

    f'=z²+x^(2n-1),
    g'=z²+2x^(2n-1).

Their intersection is supported at the same exceptional tangent direction,
with exact length

    length K[[x,z]]/(f',g')=2(2n-1)=4n-2.

Thus the excess over the product `pq=4` is arbitrarily large while the
normal orders and first tangent forms remain fixed. This directly
invalidates any inference that the coefficient of a common tangent
component in `W` is bounded by its multiplicity in the two first-normal
divisors. The effective-cycle proof of `(T1)--(T3)` never makes that
inference. These are local models, and no claim is made that they
globalize to projective STCI pairs on the quartic.

## Relation to the existing normalization frontier

P-019 and P-020 give sharper necessary conditions for a thick sextic under
specified branching hypotheses, and P-027 closes the smooth-normalization
clean-conductor case. None of those hypotheses follows from the cycle
effectivity argument above. P-032 still requires an effective Cartier
divisor on the full normalization, numerical/linear equivalence to a
hyperplane multiple, and section descent through the full conductor
square. The new cycle inequality and equality-root reduction supply
necessary restrictions before that descent analysis; they do not remove
its non-Cartier, extra-conductor, or higher-contact loopholes.


---

## 2026-10-06-session-uniform-audit

# Uniform BF audit, degree strengthening, and the surviving e=2 branch

Date: begun 2026-10-06, completed after resumption on 2026-10-07.
Status: **DIRECT PROOF AUDIT AND NECESSARY NUMERICAL REDUCTIONS**.
This note does not prove that C0 is not STCI. It does not assert a global
exclusion of every quartic carrier with e=2.

## 1. Inputs, independent representation, and scope correction

The canonical state, resume reconciliation, uniform order-one note,
primitive-fourth audit, and finite-flat pairing audit were compared.
The BF duality/effectivity statements survive the direct local argument
below. Their use still requires the smooth characteristic-zero rational
quartic normal bundle N*=O(-7)^2, complete-intersection adjunction,
and generic normal order one. The quartic assertion that the carrier has
generic normal order one is the repository's separately checked P-011
input; this note does not reprove P-011.

There is a genuine scope discrepancy in the pre-session canonical state.
Section B proves the e=2 branches of (4,7) and (4,8), whereas section H
says broadly that the quartic e=2 branch is excluded. The resume
reconciliation correctly states that larger pairs with early defects
remain open. The primitive-fourth argument applies to a larger pair
when D2=D3=0; those vanishings are not uniform consequences of BF
duality. Sections 4--6 below give exact local CI controls and small-degree
reductions showing why this distinction matters.

The primary-source BF cross-check was refreshed from Manolache,
*Duality for Gorenstein multiple structures on smooth algebraic varieties*,
Rev. Roumaine Math. Pures Appl. 68 (2023), 141--148:
[publisher PDF](https://imar.ro/journals/Revue_Mathematique/pdfs/2023/1-2/10.pdf).
The theorem is on printed p.143, embedded structures in Remark 1 on
pp.144--145, and coincidence of the filtrations for quasiprimitive
structures in Remark 2 on p.145. The proof here is an independent local
algebra representation; agreement with the reference is not its proof.

## 2. Direct proof of the saturated duality and effective defects

At a support point complete the ambient local ring to k[[t,x,y]].
Let B be its complete-intersection quotient with smooth reduced support
R=k[[t]]. Smooth support and Cohen--Macaulayness make t a
nonzerodivisor. Nilpotence of the two normal coordinates makes B finite
over R, hence finite free. Its special fibre is an Artin complete
intersection, so it is Gorenstein. Lift a functional on the special
fibre that is nonzero on its socle to an R-linear functional lambda on
B. The determinant of the multiplication pairing modulo t is nonzero;
therefore B -> Hom_R(B,R), b -> lambda(b*_), is an isomorphism.

Suppose the generic transverse algebra is K[v]/(v^m), K=Frac(R).
This holds when one defining equation has nonzero linear normal term:
formal elimination reduces the other equation to a nonzero multiple
of v^m. Put

    N_i = B intersect v^i B_K,       E_i=N_i/N_(i+1),
    0 <= i <= m,                   s=m-1.

Every B/N_i is R-torsion free, so each saturated step is a direct
summand. The E_i are free rank-one R-modules. The nilradical is N1;
the constant-coefficient quotient B/N1 is an integral R-subalgebra of
K, hence R itself. Generically and then integrally by torsionfreeness,

    Ann_B(N_i)=N_(m-i).

For any ideal J the lambda-orthogonal equals Ann(J): if lambda(bJ)=0,
then lambda(bjc)=0 for all c in B, and nondegeneracy implies bj=0.
A functional on N_(s-i)/N_(s-i+1) extends to B because the saturated
filtration splits over R. Its representing element under the Frobenius
pairing lies in N_i, and the kernel of its restricted functional is
N_(i+1). Thus E_i pairs perfectly with E_(s-i). Taking i=0 shows that
lambda maps E_s isomorphically to R. Consequently the actual maps

    E_i tensor E_(s-i) -> E_s

are isomorphisms. This checks maps, not just degrees or line-bundle
classes. It also explains why ordinary nilradical powers cannot replace
the saturated filtration: their quotients may have R-torsion.

Globally let L=E1. The iterated multiplication L^i -> E_i is generically
an isomorphism of line bundles on the smooth curve and hence has an
effective zero divisor D_i. Therefore E_i=L^i(D_i), D0=D1=0.
Associativity gives, as actual effective-divisor statements,

    D_i+D_j <= D_(i+j),        D_i+D_(s-i)=D_s.          (BF)

The top layer is Ann(I_C). Gorenstein duality identifies
Hom_(O_X)(O_C,omega_X) with omega_C; therefore

    E_s = omega_C tensor (omega_X|C)^(-1).

This proves the exact input used in the uniform note. It applies to the
saturated quasiprimitive CI structure. It makes no assertion about
ordinary powers, standalone nongorenstein lattices, or the branch where
both equations have generic normal order at least two.

## 3. A uniform degree strengthening beyond the retained bounds

Assume a,b>=4, generic normal order one for at least one equation, and
N*=O(-7)^2. The conormal epimorphism onto L has

    L=O(e-7),     e>=0,     c=7-e,     m=ab/4, s=m-1.

Here ab must be divisible by 4. Adjunction gives

    deg D_s = c*(ab/4-1)+14-4(a+b).                   (1)

Effectivity first gives c>0, hence e<=6. Multiplying (1) by 4c and
completing the product gives the stronger necessary degree condition

    (c*a-16)(c*b-16) >= 256-56*c+4*c^2.               (2)

This is equivalent to top-defect effectivity, rather than an additional
geometric hypothesis. It displays degree restrictions missed by listing
only e<=6 or 16/a<=c. For the four highest direction degrees it becomes

| e | Exact necessary inequality | Each defining degree must be at least |
|---|---|---:|
| 3 | (a-4)(b-4)>=6 | 5 |
| 4 | (3a-16)(3b-16)>=124 | 6 |
| 5 | (a-8)(b-8)>=40 | 9 |
| 6 | (a-16)(b-16)>=204 | 17 |

For e=3 both factors are nonnegative because a,b>=4, and the right
side is positive. For e=4, if both factors were negative their product
would be at most 16; for e=5 the corresponding bound is 64 after
multiplying by four; for e=6 it is 144. Each is smaller than the
required right side. A mixed-sign product is also impossible, so both
factors must be strictly positive. This proves both degree lower bounds,
including for a mate that may be thick generically. It does not transfer
the geometric normal-sheaf inequality to a thick mate.

For completeness, (2) has right sides 60,64,76 for c=7,6,5
(e=0,1,2). None is negative. The exact constraints for e=1,2 are
(6a-16)(6b-16)>=64 and (5a-16)(5b-16)>=76.
At e=2,a=4 the latter is precisely b>=7. These conditions give no
upper bound on either degree and do not exclude the high-degree
order-one branch.

## 4. Why the primitive factorization stops at its stated hypotheses

For a quartic carrier m=b and the top formula is

    deg D_(b-1)=(3-e)*b+e-9.

At e=2 this is b-7. For b=7 the entire defect divisor vanishes.
For b=8, superadditivity forces D2=D3=0 because twice either one
is bounded by a divisor of degree one. The canonical primitive fourth
then exists, so its quotient lies on the audited fourth-obstruction
zero locus. On that locus the defining quartic lies in

    H0(I_(C3)(4))=T*H0(O_(P3)(1)).

Its nonzero plane factor forces an extra curve when intersected with
any mate, proving the two exclusions. The same argument works at
any larger b when D2=D3=0. It does not force these equalities once
b-7 permits nonzero early defects. The existing parity theorem does
give an all-b exclusion on its explicit parity quotient family with
D2=0, but it does not cover every quadratic quotient or D2=1.

## 5. Exact local CI controls against a numerical overclaim

Let R=k[[t]] and take integers r,h>=2. The local algebra

    B_(r,h)=R[x,y]/(t*x-y^r, x^h)

is finite free with basis x^i*y^j, 0<=i<h, 0<=j<r. One can see
this by first taking R[x]/(x^h) and adjoining the monic relation
y^r-t*x. It is a complete intersection supported on (x,y).
After inverting t it is K[y]/(y^(r*h)) with x=t^(-1)y^r.
Writing k=r*i+j shows that the saturated layer E_k has generator
t^(-i)y^k, whereas the image of E1^k has generator y^k. Hence

    d_k=ord_t D_k=floor(k/r),       0<=k<r*h.         (3)

This formula satisfies superadditivity and complement duality exactly:

    floor(i/r)+floor((r*h-1-i)/r)=h-1.

Two controls are directly compatible with the e=2 top degree:

| b=r*h | Local equations | (d2,d3,d_(b-1)) |
|---:|---|---|
| 9 | t*x-y^3, x^3 | (0,1,2) |
| 12 | t*x-y^2, x^6 | (1,1,5) |

In each case d_(b-1)=b-7 and the uniform early bounds are satisfied.
Thus even finite-flat, two-normal-generator, local CI and Gorenstein
duality do not promote the primitive exclusion to every b. These are
local numerical controls, not projectively embedded multiple curves
on C0 and not STCI counterexamples or constructions. They establish
the insufficiency of the proposed numerical inference.

## 6. A sharper small-degree surviving frontier

For e=2, repeated multiplication gives

    deg D2 <= floor((b-7)/floor((b-1)/2)),
    deg D3 <= floor((b-7)/floor((b-1)/3)).              (4)

In particular b=9,10,11 have D2=0 and deg D3<=1. A survivor must
have deg D3=1; otherwise the primitive factorization applies. Write
D3=p. At p, superadditivity and complement duality force every
top defect to lie at p:

* b=9: D3+D5=D8 and D5>=D3, so the top degree two is spent at p.
* b=10: 3D3<=D9, so the top degree three is spent at p.
* b=11: 3D3<=D9=D10. Moreover D10=2D5, so its coefficient
  at each point is even. Its coefficient at p is therefore at least
  four, exhausting the total degree four.

Consequently the complete divisor sequence is an integer profile
d_i*p. Exhausting the finitely many integers allowed by (BF) gives

| b | Complete permissible profiles (d0,...,d_(b-1)) |
|---:|---|
| 9 | (0,0,0,1,1,1,2,2,2) |
| 10 | (0,0,0,1,1,2,2,3,3,3) |
| 11 | (0,0,0,1,1,2,3,3,4,4,4); (0,0,0,1,2,2,2,3,4,4,4) |

The companion `verify_session_uniform_bf_profiles.py` independently
enumerates every complementary profile, imposes effectivity,
monotonicity (the i=1 multiplication case), all superadditivity
inequalities, and d2=0,d3=1. It checks exactly these lists.
The b=9 profile has the genuine local CI control above. The other
profiles remain necessary numerical possibilities; the verifier does
not assert their embedded or local nonmonomial existence.

## 7. Intrinsic fourth-layer annihilation and an isolated universal export

When D2=0 the primitive triple has ideal-generator bundle fitting in

    0 -> L^3 -> V=I_(C3)/(I_C*I_(C3)) -> M -> 0,
    L=O(-5), M=O(-9).

Its class c lies in H1(O(-6)). A fourth layer with
E3=L^3(D3) induces a quotient V->E3 whose restriction to L^3
is the canonical multiplication section. Applying Hom(-,E3) gives
the necessary annihilation

    c maps to zero in H1(O(-6+D3)).                   (5)

If c is represented by coefficients c1,...,c5 of z^-1,...,z^-5,
a quadratic annihilator exists exactly when

    det [[c1,c2,c3],[c2,c3,c4],[c3,c4,c5]]=0.           (6)

This is multiplication of Laurent cocycles, so it includes the moving
infinity point when sections are treated homogeneously. For b=9..11
the stronger degree-one annihilator is necessary: the four-by-two
matrix with rows (c1,c2),(c2,c3),(c3,c4),(c4,c5) must have nonzero
kernel. The condition is rank at most one, not merely (6).

The session exporter `session_uniform_e2_hankel.py` imports the retained
exact moving-coordinate generator and writes only
`scratch/session_uniform_e2_hankel.json`. It derived c_j with a
single homogeneous-resultant denominator Delta; the Hankel determinant
reduces to P16/Delta, with P16 homogeneous of degree sixteen and
1112 monomials. The numerator vanishes to order at least six in
(2a1+b0,2a2+b1). Its parity specialization is

    - (beta+2)^6*(beta^2+8beta+36)
       *(beta^4+8beta^3-24beta^2-256beta-432)/1024.

Division by the specialized Delta=beta^2 gives the actual determinant.
At beta=-6,-2,6 the fourth vectors are respectively
(64,0,-8,0,0), (0,0,0,0,0), and (-128,0,160,0,-192);
the determinants are 512,0,-163840, matching the independent retained
parity certificate. There was no useful general polynomial
factorization, and no universal incidence exclusion was completed.

This export is exact derived data from the established generator,
not an independent audit of that generator. The open primitive-triple
problem combines actual quartic contact, the resultant-open condition,
and (5). For D2=1 a defective-triple gluing state is needed before
using any fourth class. The primitive calculation does not apply there.

The exporter also saves all six exact minors of the four-by-two
degree-one annihilator matrix, with their resultant denominator powers.
Their reduced numerator term counts are 392,412,447,416,412,392.
Thus the sharper b=9..11 necessary condition has a reproducible complete
polynomial specification. No saturation or emptiness certificate for its
intersection with the full ambient quartic-contact incidence is claimed.

## 8. Reproduction and continuation boundary

The new finite profile check and isolated Hankel export use

```sh
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/verify_session_uniform_bf_profiles.py
PYTHONDONTWRITEBYTECODE=1 /private/tmp/stci-cas-venv/bin/python research/computations/session_uniform_e2_hankel.py
```

The first is a genuinely exhaustive numerical check under explicitly
listed inequalities. The second regenerates the existing universal
fourth class and a new determinant; it does not replace the independent
ambient quartic-contact audit. Neither is a global STCI certificate.

The durable frontier is: the BF input is valid under the order-one
quasiprimitive CI hypotheses; high-e order-one pairs satisfy the
stronger degree products (2); the e=2 quartic branch remains open in
larger degrees unless early defects or the full actual carrier/annihilator
incidence are excluded. The entirely-thick branch is separate.


---

## 2026-10-06-session-validation

# Session exact validation and reproducibility record

Started 2026-10-06; continued and completed 2026-10-07.
Status: **EXACT LIVE VALIDATION / REPRODUCIBILITY**, with two documented verifier repairs.
The dated filename is retained across the continuation. This note does not by itself prove any global STCI claim.

## Counts and environment

There are **55 distinct source checks with a successful latest execution**. The initial executions gave 53 passes and 2 failures. Both failures were investigated before changing their sources; the two repaired-source reruns passed. Three additional compatibility-copy diagnostic runs are retained separately: one pass and two failures. The MF6 owner subsequently completed the universal verifier with self-contained incidence reconstruction, explicit minor-membership witnesses, and the full exceptional fiber. That changed source was rerun once and passed; its earlier successful output is retained. Thus there were 61 complete top-level verifier/exporter executions: 55 initial distinct-source checks, 2 repaired-source reruns, 3 diagnostic copies, and 1 meaningful source-completion rerun. Prefix evaluations used to diagnose failures and imported subsidiary modules are not inflated into additional source-check counts.

The 41-source baseline suite consists of 38 Python files named in the computation README, the historical mixed-(4,5) Python verifier, and two Macaulay2 verifiers. Its initial result was 40 passes and 1 failure; the repaired boundary verifier makes its latest result 41 passes. The remaining fourteen distinct checks are one tensor exporter, two incidence verifiers, two supplementary retained checks, five fresh MF6/dx1 checks, three new normal-carrier arithmetic checks, and one source-reconstructed dx1 saturation audit.

The baseline was run on branch `research/ultra-resume-2026-10-06`, starting from HEAD `4103561f3e271e03d8069e7f09def3889b4eb4da`. The continuation started from the clean retained snapshot at HEAD `3ffda7548a863387429adab61eefe02575e86297`. These are observation points, not asserted final commit IDs. No branch was switched or reset by this validation lane.

- Python: `/private/tmp/stci-cas-venv/bin/python`, version 3.14.8.
- SymPy: 1.14.0.
- Macaulay2: `/opt/homebrew/bin/M2`, version 1.26.06.
- Python executions used `PYTHONDONTWRITEBYTECODE=1`.
- The baseline passed checks were not rerun merely because the user resumed on the following day.

Exact commands, elapsed times, exit statuses, source hashes, and logs are stored in [`validation-index.json`](../validation/2026-10-06-session/validation-index.json). Environment observation files are [`environment.json`](../validation/2026-10-06-session/environment.json) and [`environment-2026-10-07.json`](../validation/2026-10-06-session/environment-2026-10-07.json). The replay drivers are [`run_suite.py`](../validation/2026-10-06-session/run_suite.py) and [`run_fresh_2026_10_07.py`](../validation/2026-10-06-session/run_fresh_2026_10_07.py). They expect the recorded runtime paths, so a successor must adjust those paths if the temporary Python environment disappears.

## Baseline per-source results

| Source | Initial result | Latest result | Exact run log |
|---|---|---|---|
| `computations/verify_all_quartic_primitive_obstruction.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_all_quartic_primitive_obstruction.log) |
| `computations/verify_c0.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_c0.log) |
| `computations/verify_chow_form.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_chow_form.log) |
| `computations/verify_chow_pencil_45.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_chow_pencil_45.log) |
| `computations/verify_degree6.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_degree6.log) |
| `computations/verify_dx1_a_half_boundary.py` | FAILED | PASS | [log](../validation/2026-10-06-session/verify_dx1_a_half_boundary_repaired.log) |
| `computations/verify_dx1_p044_residual.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_dx1_p044_residual.log) |
| `computations/verify_general_conductor_power.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_general_conductor_power.log) |
| `computations/verify_localcoh_constant_direction_apolar.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_constant_direction_apolar.log) |
| `computations/verify_localcoh_degree4_allstage_certificate.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_degree4_allstage_certificate.log) |
| `computations/verify_localcoh_degree4_counterexample.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_degree4_counterexample.log) |
| `computations/verify_localcoh_direction_image.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_direction_image.log) |
| `computations/verify_localcoh_finite_principal_parts.m2` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_finite_principal_parts.log) |
| `computations/verify_localcoh_generic_length_model.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_generic_length_model.log) |
| `computations/verify_localcoh_pure_direction_audit.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_pure_direction_audit.log) |
| `computations/verify_localcoh_quartic_ratio_t_slice.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_quartic_ratio_t_slice.log) |
| `computations/verify_mf6_defect12.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mf6_defect12.log) |
| `computations/verify_mf6_type3.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mf6_type3.log) |
| `computations/verify_mixed46_regular.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mixed46_regular.log) |
| `computations/verify_normal_bundle.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_normal_bundle.log) |
| `computations/verify_normal_quartic_simple_elliptic.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_normal_quartic_simple_elliptic.log) |
| `computations/verify_normal_rational_carrier_compression.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_normal_rational_carrier_compression.log) |
| `computations/verify_p044_survivor_cubic.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_p044_survivor_cubic.log) |
| `computations/verify_positive_quartic_descent.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_positive_quartic_descent.log) |
| `computations/verify_primitive_obstruction.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_primitive_obstruction.log) |
| `computations/verify_primitive_quadruple_universal.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_primitive_quadruple_universal.log) |
| `computations/verify_primitive_quartic_factor_audit.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_primitive_quartic_factor_audit.log) |
| `computations/verify_primitive_triple_parity.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_primitive_triple_parity.log) |
| `computations/verify_quadric_powers.m2` | PASS | PASS | [log](../validation/2026-10-06-session/verify_quadric_powers.log) |
| `computations/verify_residual_cycle.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_residual_cycle.log) |
| `computations/verify_split22_boundary_lift.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split22_boundary_lift.log) |
| `computations/verify_split22_boundary_survivor.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split22_boundary_survivor.log) |
| `computations/verify_split22_chart_audit.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split22_chart_audit.log) |
| `computations/verify_split22_finite_reduction.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split22_finite_reduction.log) |
| `computations/verify_split4_nonramified.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_split4_nonramified.log) |
| `computations/verify_typea45.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typea45.log) |
| `computations/verify_typeb45_boundary.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typeb45_boundary.log) |
| `computations/verify_typeb45_corner.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typeb45_corner.log) |
| `computations/verify_typeb45_dense.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typeb45_dense.log) |
| `computations/verify_typeb45_endpoint_certificate.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_typeb45_endpoint_certificate.log) |
| `scratch/degree6/verify_mixed45_reduction.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mixed45_reduction.log) |

The three primitive generator-driving checks ran sequentially in the retained `validation/2026-10-06-session/isolated` snapshot. Their generators rewrite formula JSON and Macaulay2 sources, so the snapshot preserves all generated data while leaving the existing research formulas unchanged. The universal primitive verifier invokes both its exact M2 membership companions with checked subprocess exits. The source and generated-output hashes are in [`isolated-source-output-hashes.json`](../validation/2026-10-06-session/isolated-source-output-hashes.json).

Known faulty historical `localcoh-symbol-paritycheck.m2` and `localcoh-symbol-seedcheck.m2` were not executed or used as proof inputs. The older resultants-only dx1 diagnostic is retained as a diagnostic; its passing gcd assertion does not certify residual emptiness.

## Missing local-cohomology coordinates restored

The unchanged retained exporter `computations/localcoh-incidence-tensor.m2` regenerated its two absent files. Its exact assertions checked 30 ancestors, 18 actual quartic forms of degree four, target dimension 74, and preservation of the combined product/target row space. The source SHA-256 was

    c81ff40cd8a83cdbe527401b038d75a9748f2b2b10c09214fb0520e3ecb69377

The output hashes were:

| Coordinate file | SHA-256 |
|---|---|
| `localcoh-incidence-tensor.txt` | `05702619ef67a6fed4420e24a5530eccb18e4700d8e1f1ba5cae89b7899cc60b` |
| `localcoh-incidence-bases.txt` | `ee3e320f240b77c370ad21704c97aeec12b619f55c6ad8aff829aef9235d8dcc` |
| `localcoh-symbol-numerators.txt` | `4989e3ed86a06221b828b1ede99085325fb9740ad02dd1c542e547c8f5809406` |

The tensor and basis hashes agree **exactly** with both previously retained JSON certificates. The retained `localcoh-symbol-top.json` hash also agrees with both certificates. The formerly absent symbol-numerators file was extracted as the 30 ancestor lines `bases[1:31]`, in the same order and with a trailing newline. Its equality with those lines is checked by both incidence verifiers. No coordinate convention or stored certificate was edited.

| Source | Initial result | Latest result | Exact run log |
|---|---|---|---|
| `computations/localcoh-incidence-2026-10-06.py` | PASS | PASS | [log](../validation/2026-10-06-session/localcoh-incidence-2026-10-06.log) |
| `computations/localcoh-incidence-parity-dual-2026-10-06.py` | PASS | PASS | [log](../validation/2026-10-06-session/localcoh-incidence-parity-dual-2026-10-06.log) |

The fixed-direction certificate proves the exclusion only for normalized direction `(1+t^2,-2t)`, including all lower-order coefficients. The polynomial parity dual proves its stated normalized family exclusion over all characteristic-zero extensions. These exact reruns do not establish emptiness of the full quartic incidence. See [`regenerated-coordinate-hashes.json`](../validation/2026-10-06-session/regenerated-coordinate-hashes.json) and the [exporter log](../validation/2026-10-06-session/localcoh-incidence-tensor.log).

## Boundary verifier failure and chart repair

The initial `verify_dx1_a_half_boundary.py` failed at `G.reduce(u)` because SymPy inferred the integer coefficient domain from the residual polynomials but `u=bx+1/2` has a rational coefficient. An isolated one-line `domain=QQ` compatibility change exposed a second issue: ordinary ideal membership was false in the undivided residual ideal.

After dividing the four displayed numerators by `(b+2)^2`, every residual still contains a factor `x`. The exact QQ Gröbner basis was

    [b*x-8*x^2-4*x, x^3+x^2/2+x/16],

with remainder

    rem(u)=8*x^2+4*x+1/2.

At `x=0` this residual system vanishes while `u=1/2`, so the literal unsaturated membership statement cannot hold. The intended `dx=1` chart requires `x!=0`. Removing the verified common factor `x` on that chart gives

    [b-8*x-4, x^2+x/2+1/16],

and `rem(u)=0`.

The repaired source explicitly states the chart, verifies divisibility by `x`, divides the residuals by `x`, and computes over QQ. Its conclusion is now scoped to `a=-1/2` and `x!=0`. The calculation does not claim ordinary membership in the earlier undivided ideal or make any assertion at `x=0`.

- Original source hash: `871f5f68e0a179a77e0626e904e2841e786ffa189bd093017cf5233ffa122d87`.
- Repaired source hash: `296eeefc0496b390d3b230d08fc8330ef3170ee4a5e1ad19a9a556715f10bf2e`.
- [Original failing log](../validation/2026-10-06-session/verify_dx1_a_half_boundary.log), [QQ-only failing log](../validation/2026-10-06-session/compat_verify_dx1_a_half_boundary_QQ.log), [membership diagnostic](../validation/2026-10-06-session/dx1-boundary-membership-diagnostic.txt), [chart diagnostic](../validation/2026-10-06-session/dx1-boundary-saturation-diagnostic.txt), and [successful repaired log](../validation/2026-10-06-session/verify_dx1_a_half_boundary_repaired.log) preserve the correction rather than hiding the failed premises.

The separately regenerated five-equation Macaulay2 boundary audit agrees with the reduced geometric implication; its exact boundary radicals are recorded in the fresh checks below.

## Supplementary retained checks and polynomiality repair

| Source | Initial result | Latest result | Exact run log |
|---|---|---|---|
| `computations/verify_e2_quartic_incidence.py` | FAILED | PASS | [log](../validation/2026-10-06-session/verify_e2_quartic_incidence_repaired.log) |
| `computations/verify_localcoh_direction_contact_survivor.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_localcoh_direction_contact_survivor.log) |

The unlisted `verify_e2_quartic_incidence.py` initially failed its assertion that every entry of `J2` has literal denominator one. Exact inspection found only rational constant denominators `4,8,16`, no parameter denominators, and all 18 entries polynomial over QQ. The scoped repair asserts polynomiality over QQ in `x,a,b,d,z` and exact equality after expansion; it does not change the entries or promote the script beyond its own **exact regression / computational cross-check** scope.

An initial diagnostic copy compared `Poly(...).as_expr()` to the unexpanded expression with structural equality and failed. That diagnostic failure concerns expression representation, not a changed polynomial. A second diagnostic copy that permits constant denominators passed. The final repaired source uses explicit QQ construction and expanded equality, and its complete rerun passed.

- Original source hash: `66a725a4fa44038f183319a2c77e3fa64ca42dccf9d9a4d06e5b1f4d1a17dad3`.
- Repaired source hash: `cb210f61e9a154c8a9d1c1a388e75e1a02a3c89b13bfd8157c1bce942c6e8559`.
- [Initial failure](../validation/2026-10-06-session/verify_e2_quartic_incidence.log), [exact denominator diagnostic](../validation/2026-10-06-session/e2-j2-denominator-diagnostic.json), and [successful repaired log](../validation/2026-10-06-session/verify_e2_quartic_incidence_repaired.log).

The contact-survivor script proves only that its explicit coprime ambient pair has second transverse contact but its forced highest inverse coefficient has uncancelled poles, so it has no global quartic ancestor. It does not classify the full contact chart.

## Fresh checks on the 2026-10-07 continuation

| Source | Initial result | Latest result | Exact run log |
|---|---|---|---|
| `computations/session_dx1_boundary_2026_10_06.m2` | PASS | PASS | [log](../validation/2026-10-06-session/session_dx1_boundary_2026_10_06_2026_10_07.log) |
| `computations/session_dx1_compact_certificate_2026_10_06.m2` | PASS | PASS | [log](../validation/2026-10-06-session/session_dx1_compact_certificate_2026_10_06_2026_10_07.log) |
| `computations/verify_mf6_infinity_universal.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_mf6_infinity_universal_completed_2026_10_07.log) |
| `computations/verify_session_dx1_independent_2026_10_06.py` | PASS | PASS | [log](../validation/2026-10-06-session/verify_session_dx1_independent_2026_10_06_2026_10_07.log) |
| `scratch/session-mf6-special-fiber.py` | PASS | PASS | [log](../validation/2026-10-06-session/session-mf6-special-fiber_2026_10_07.log) |

The universal MF6 infinity script independently derives the nonlinear support/frame transition through cubic order, checks the generic chart as an additional regression, and computes the universal annihilation boundary-minor ideal

    ((A-12)^2,(A-12)(B-4),(B-4)^2).

Its reduction forces `(A,B)=(12,4)` under the recorded annihilation/one-excess-defect hypotheses; the generic kernel is not used to extrapolate the universal boundary rank condition. The completed universal source also reconstructs the full incidence matrix without a generated JSON proof input, checks explicit polynomial combinations witnessing each generator of the boundary-minor ideal, and derives its complete exceptional quartic fiber. Its source SHA-256 is `75bd764fadce1dbd538ac9f23c2039164cbac4e49fd597de7bd46c8e03b42b9e`. The earlier successful source SHA-256 was `3037a2203977e7812ce5d7769667f8a1ab010ba57786ff971e28598f00835bfe`; both run logs remain inspectable. The separate complete special-fiber script cross-checks that its four-dimensional quartic space is exactly `C*H0(O(1))`. This generated JSON was retained in an isolated fresh snapshot; its SHA-256

    059a5188dd40a69ceb921c88fc2830d9a7ffc07eae6678adf6eec72df327fcf3

agrees exactly with the prior repository JSON. The shared MF6 incidence fixture hash is in the special-fiber result record, so the direct fiber check can be rerun with its precise matrix input. The finite matrix calculation and the surrounding geometric argument have distinct roles; this validation note does not replace the proof of the pole/annihilation reduction.

The dx1 compact M2 run computes the common colon exponent and prints `colon equality: true` for the supplied six-generator ideal. The boundary M2 run prints true for the full basepoint-free radical `(2a+1,b+2)` and both boundary radical implications. These boolean outputs were checked explicitly in [`semantic-output-checks.json`](../validation/2026-10-06-session/semantic-output-checks.json), in addition to the process exits.

The independent dx1 Python companion verifies the full polynomial identity `sum(Q_i*C_i)=s^2` by expansion over QQ in a different engine. It also uses exact rational interval arithmetic to certify a real zero of the insufficient three-equation subsystem on its open set, while the two omitted numerators stay nonzero. The displayed decimal intervals summarize exact rational inequalities. The strict inequalities certify the contraction argument; floating point arithmetic is not used for its assertions.

The retained historical resultant-gcd check therefore remains useful evidence for why a full five-equation certificate was necessary. The independent expansion verifies the supplied ideal-membership identity directly rather than treating CAS agreement as an audit.

## Hash integrity and remaining reproducibility limits

The [before hash manifest](../validation/2026-10-06-session/source-hashes-before.json), [after hash manifest](../validation/2026-10-06-session/source-hashes-after.json), [fresh input hashes](../validation/2026-10-06-session/fresh-input-hashes-2026-10-07.json), and individual repair/result JSONs preserve the executed source boundary. The original baseline sources changed only in the explicitly documented boundary and supplementary polynomiality repairs. The neighboring `session_dx1_saturation_2026_10_06.m2` was still being completed by its owning research lane when the first broad manifest was taken; its final source and witness are hashed as fresh independent-check inputs. That neighboring source change is recorded, not silently attributed to the earlier baseline.

The tensor/basis/numerator reproducibility gap is repaired. The MF6 type-4 incidence fixture is present and hashed. Missing general `localcoh-e2-incidence-2026-10-06.py` exporter/chart systems and the historical parity discovery M2 file remain unavailable in this checkout. They were not claimed as live reruns. The retained corrected parity dual is self-contained once the regenerated tensor coordinates and stored top map are present.

No unavailable-runtime or missing-fixture failure remains in the executed set. The temporary Python runtime is a future reproducibility dependency, while the persisted exact formulas, snapshots, hashes, and output logs provide a continuation-ready evidence record independent of its continued availability. Passing a verifier establishes only its recorded finite identities, ranks, memberships, or scoped family calculation; it does not settle the unrestricted STCI question for C0 or for every integral curve.

## Additional stabilized normal-carrier and dx1 audits

Four further sources were copied with their dependencies into `validation/2026-10-06-session/isolated-additional-2026-10-07` and rerun after owner coordination. The previous 51 passing latest checks were not repeated.

| Source | Live result | Exact run log |
|---|---|---|
| `computations/audit_dx1_saturation_2026_10_07.py` | PASS | [log](../validation/2026-10-06-session/audit_dx1_saturation_2026_10_07_validation_2026_10_07.log) |
| `computations/verify_session_normal_carrier_progress.py` | PASS | [log](../validation/2026-10-06-session/verify_session_normal_carrier_progress_validation_2026_10_07.log) |
| `computations/verify_session_normal_independent_audit.py` | PASS | [log](../validation/2026-10-06-session/verify_session_normal_independent_audit_validation_2026_10_07.log) |
| `computations/verify_session_normal_nonreduced_trees.py` | PASS | [log](../validation/2026-10-06-session/verify_session_normal_nonreduced_trees_validation_2026_10_07.log) |

The reduced normal-carrier companion reconstructs the complete inverse ADE columns, enumerates the reduced cycle/ADE numerical constraints, and verifies the numerical normal-sheaf contradiction in its last row. The separately implemented independent scan imports no primary normal companion and finds the same five correction configurations, with full denominators `2,2,2,2,6`. Both regenerated reports agree byte-for-byte with their prior retained JSON outputs. This validates the arithmetic; the geometric passage, classification, compression, and local defect arguments are separately audited inputs.

The stabilized nonreduced tree source has SHA-256 `fca8eb7c177d88d00adcf5c60f664f8bbf9926abaf586762f22bfedf4199a2a7`; its reduced-source dependency has SHA-256 `57c73e7fc597d892dde3628dc0a7c0da2e6e61514af7890118e057f29b5cef13`. The independent live run took 22.899 seconds and its JSON output hash `52c5633b19828017636f1a88e74d8989129edb9d4a6abbfefb850ce893402c36` agrees exactly with the owner's retained report. It verifies:

- 381802 tree diagonal modifications under the stated rank/excess budgets;
- 195 admissible positive integral anticanonical cycles;
- 236 exact correction matches, of which 12 remain after degree-at-most-five compression;
- all 12 remaining rows have `d=3,t=2`;
- zero rows remain after applying the **external geometric Type-D passage input `t=1`**.

The source checks every successful leaf-elimination solve against its original linear equations and uses full inverse-column denominators. Its last filter is an arithmetic application of a geometric premise; the computation does not itself prove that premise or the classification's exhaustion of surfaces. The stronger normal-quartic conclusion requires the separately audited geometric argument in the normal-carrier/frontier notes.

The new dx1 audit has SHA-256 `6c2fcf9747814a6dff5f06af9043c2dc2d6fa2123a39fda23715c2f09393fc63`. It independently regenerates all five `Q_i` from the dated obstruction dump, proves their specialization denominators and equivalence on the basepoint-free chart, checks equality with the legacy source inputs, and expands the saved shifted 5-by-6 witness over QQ. It also establishes the exact comparison with the retained universal coordinate implementation: reversed obstruction coordinates differ by the stated factor 32, and the resultants agree. Its generated standalone M2 source, metadata, and output all agree byte-for-byte with the prior retained files; the generated M2 assertions check both ideal containments, the colon/saturation equality, the radical, and the two boundary square ideals.

The [additional input manifest](../validation/2026-10-06-session/additional-input-hashes-2026-10-07.json), [three-source results](../validation/2026-10-06-session/additional-results-2026-10-07.json), and [nonreduced result](../validation/2026-10-06-session/additional-nonreduced-result-2026-10-07.json) retain exact replay boundaries. These four new checks add to the existing record; they do not turn arithmetic agreement into a global STCI theorem.


---

## 2026-10-06-split22-finite-reduction

# Two totally ramified residual roots: a full higher-jet reduction

## Result and scope

Work over an algebraically closed field of characteristic zero on

\[
 C_0=[s^4:s^3t:st^3:t^4].
\]

Retain P-020's **integral carrier, reduced/content-free split first-normal
exceptional divisor, and no vertical component** hypotheses. Consider
only the `d=1,[2,2]` family whose two residual ruling roots are the totally
ramified rulings. The two low evaluation zeros are at their preimages.
This is the complete family parameterized in
`2026-10-05-split-sextic.md`, not merely its fixed specimen.

**Proved necessary reduction.** If a carrier in this entire family has an
STCI mate of any degree, its low-factor parameter must be

\[
 \boxed{h=-\tfrac12.}
\]

Up to the diagonal automorphisms of `C0`, and up to multiplying the carrier
by a nonzero scalar, the remaining carriers have the one-parameter form

\[
\begin{aligned}
 F_\tau={}&-B^2+\tau q\mathcal K,\qquad \tau\ne0,\\
 \mathcal K={}&q(-16x_0^2+16x_1^2-x_3^2)
 +16x_1A-16x_2A+4x_3B-x_2D+8q^2,
\end{aligned}
\]

where `q,A,B,D` have their repository meanings. No STCI mate is constructed,
and this line is not excluded. Its possible extra conductor and further
normalization data must remain in the frontier. The other `[2,2]` root
configurations and the surviving `[4]` families are outside this theorem.

**Exact certificate:**
`research/computations/verify_split22_finite_reduction.py`.
Run with `/private/tmp/stci-cas-venv/bin/python` in this checkout. The full
certificate passed on 2026-10-06. The new normal-sheaf argument is in
`2026-10-05-mumford-normal-bound.md`; root independently audited that proof.
A separate adversarial audit of the present reduction was requested.

## Exact local state and the global Jacobian zero divisor

Put

\[
 a=h-\tfrac12,\quad c=3a^2+2a+1,
 \quad a\ne0,\quad 2a+1\ne0,\quad u_0u_8\ne0.
\]

The last conditions are the existing content-free endpoint conditions;
`2a+1=2h`. In the finite blowup chart set

\[
 x_0=1,\quad x_1=z,\quad x_2=z^3+e,\quad
 x_3=z^4+e((1-a)z+W).
\]

The low section is `e=W=0`. Let `f=F/e^2` be the strict-transform equation.
The ambient carrier `F`, including all its `lambda q^3` lifts, is the exact
one displayed in the older split-sextic note. Define

\[
\begin{aligned}
 R={}&a(u_0+u_2z^2+u_3z^3+u_5z^5+u_6z^6+u_8z^8)
             -2(a+1)z^4,\\
 G={}&u_2-au_3z+\beta z^2+(a^2+a+1)u_5z^3
             -a(a+2)u_6z^4+cu_8z^6,\\
 \beta={}&a\lambda-\frac{(a+1)(a^2+1)}a.
\end{aligned}
\]

Exact expansion gives the two Jacobian components along the low section:

\[
 f_W=-zR,\qquad f_e=-a^2zG.
\]

Also `f(z,0,W)=u(z)W^2-zRW`, with
`u(z)=(R+z^4)/a`. Thus the section is regular generically on the integral
strict surface, independently of whether another nonnormal curve meets it
at finitely many points. The local normal-sheaf theorem therefore applies.

The finite endpoint Hessian determinant is `-2a^3u0^2`; the reversed
endpoint determinant is `-2a^3u8^2`. Both are nonzero. At the finite
endpoint `fW=-a u0 z+...`; at the reversed endpoint the corresponding
component is `a u8 z+...`. Each endpoint is an `A1` germ with Jacobian
common order exactly one. All other base points are covered by the finite
chart with `z!=0`, so the exact global zero-divisor length is

\[
 \boxed{\delta=2+\deg\gcd(R,G).}                         \tag{1}
\]

This formula includes `G=0`, when `gcd(R,0)=R` and `delta=10`. Treating a
zero polynomial as though it had a degree-six bound would be incorrect.
That separate case is closed below.

The ambient normal extension has determinant degree eight and its
Jacobian target degree twelve. Consequently

\[
 \deg N_{\Gamma/D}=\delta-4.
\]

P-020/P-023 force `Gamma#^2=13/5` for an STCI mate. The exact normal-sheaf
defect formula therefore gives

\[
 \operatorname{Def}(\Gamma)=\delta-4-13/5.
\]

Both endpoints contribute `1/2` to this defect, so `delta>=8`.
This uses numerical intersections, where cancelling the positive integer
mate scale is legitimate. No scale is cancelled in a local class group,
and no Cartier index bound is inferred by cancelling it.

## Nonzero G: exact division and the very small remaining defect budget

Suppose first that `G!=0`. Equation (1) gives `delta<=8`; hence

\[
 \delta=8,\qquad \deg G=6,\qquad G\mid R.
\]

In particular `c!=0`. Write

\[
 R=(N+az^2/c)G.
\]

The quotient's linear coefficient is zero by the coefficient of `z^7`.
Its constant coefficient is nonzero because `R(0)=a u0!=0`. Then `u2!=0`.
The coefficient of `z` forces `u3=0`. The coefficients of `z^3,z^5`
together force `u5=0`, without deleting any exceptional root of
`a^2+a+1`. The remaining equations are

\[
\begin{aligned}
 u_0&=Nu_2/a,\\
 u_6&=\frac{Nc^2u_8}{a(2a+1)^2},\\
 \beta&=\frac{a^2(3a+2)u_2}{Nc},\\
 \frac{a^3(3a+2)u_2}{Nc^2}
 -\frac{N^2(a+2)c^2u_8}{(2a+1)^2}&=-2(a+1).
\end{aligned}                                                   \tag{2}
\]

All divisions in (2) are by previously established nonzero quantities.
The factor `3a+2` is **not** divided out here.

The diagonal automorphism `z -> t z` acts, after normalizing the residual
evaluation, by `Rnew=t^-4 R(tz)` and `Gnew=t^-2 G(tz)`. It sends
`N -> N/t^2`. Since the base field is algebraically closed and `N!=0`,
we may take `N=1`. Put `tau=N^2u8`; equivalently one may use the invariant
coordinate `y=z^2/N` before the normalization.

The total defect is `7/5`. The two endpoints consume one, leaving

\[
 \boxed{\operatorname{Def}_{\rm interior}=2/5.}             \tag{3}
\]

A single interior `A1` on the smooth low curve would contribute `1/2`,
contradicting (3). This excludes every carrier with even one such node;
no assumption about the other singular points is required.

## The cubic and its Hessian remainder

For `3a+2!=0`, solve (2) by

\[
\begin{aligned}
 P&=\frac{c^2[-2(a+1)+\tau(a+2)c^2/(2a+1)^2]}{a^3(3a+2)},\\
 b&=\frac{a^2(3a+2)P}{c},\qquad
 V_6=\frac{\tau c^2}{a(2a+1)^2}.
\end{aligned}
\]

Here `u2=P`, `u0=P/a`, `u6=V6`, `u8=tau`, and `beta=b` after taking `N=1`.
In particular `P!=0`, `tau!=0`. Define the cubic

\[
 H_3(y)=P+by-a(a+2)V_6y^2+c\tau y^3,
 \qquad Q(y)=1+ay/c.
\]

The next two exact coefficients of `f` are

\[
\begin{aligned}
 L(y)={}&aP+(-a^2+3ab+2a+5)y
       -a(3a^2+4a+2)V_6y^2+a(9a^2+6a-1)\tau y^3,\\
 H_2(y)={}&a+2a^3V_6y+2a^2(a^3-a^2-a-1)\tau y^2.
\end{aligned}
\]

Set

\[
 B_2=a^3y^2-a^2QL+Q^2H_2,
 \qquad D_2=4y^2H_2/a-L^2.
\]

At a simple root of `G(z)=H3(z^2)`, differentiation **before** imposing
the collision equation gives

\[
 \det\operatorname{Hess}_{z,e,W}(f)
       =-2z^2(G'(z))^2 B_2(z^2).
\]

Thus every simple root with `B2!=0` is `A1`. Let `Brem` be the remainder
of `B2` modulo `H3`. When `H3` is squarefree, absence of nodes would force
all three remainder coefficients to vanish. Their exact Groebner basis
contains `a tau` and `2a^2+a`, impossible on the content-free domain.
So every mate-compatible cubic must have a repeated root.

For arbitrary cubic `H3`, a necessary condition for no simple-root node is

\[
 \boxed{H_3\mid B_{\rm rem}(H_3')^2.}                    \tag{4}
\]

At a double root the squared derivative already supplies multiplicity two;
at a triple root it supplies at least three. At a simple root it is a
unit, so (4) is exactly the needed vanishing there. Therefore (4) does
not impose an unjustified condition at a repeated root.

Clear denominators in (4) and remove only known invertible factors.
Exact elimination gives, up to those invertible factors,

\[
 (a+1)^4 S_1(a)S_2(a)S_3(a)=0,
\]

where

\[
\begin{aligned}
 S_1&=3a^4+8a^3+40a^2+36a+9,\\
 S_2&=8a^4-6a^3+33a^2+36a+9,\\
 S_3&=2a^7+15a^6+48a^5+39a^4+2a^3-3a^2+4a+1.
\end{aligned}
\]

The exact univariate Groebner element is proportional to
`a^2(a+1)^4(2a+1)^11(3a+2)^2 S1 S2 S3`.
A linear-in-`tau` Groebner element has leading coefficient proportional to
`(a+1)^2(2a+1)^7(3a+2)`. Consequently, away from `a=-1` and forbidden
values, these are finite parameter strata. The certificate preserves these
polynomials and checks every exceptional stratum, rather than interpreting
a generic sample as a complete elimination.

## Closing all three finite strata and the divided parameter value

On `S1=0`, the cubic has a triple root

\[
 y_0=(a+2)c/[3(2a+1)^2],
\]

and `tau` is the rational expression checked in the certificate. The
values `y0,Q(y0),D2(y0),B2(y0)` are all units in `Q[a]/(S1)`.
There are therefore two interior collisions, each with collision order
and Jacobian order three. The nonzero transverse determinant allows a
formal Morse elimination of `(e,W)`; its residual leading coefficient is
a nonzero multiple of `B2`, and its order is six. The germ is `A5`.

The curve index is also controlled, not inferred solely from the
singularity's name. The Morse critical section has `(e,W)=O(t^3)`, where
`t=z-z0`. Along the original smooth low curve, both Morse coordinates have
order at least three and their product has order six with nonzero leading
coefficient. Their orders are thus exactly three. The local `A5` class is
three, and the normal-sheaf defect is `3^2/6=3/2`, already exceeding (3).

On `S2=0`, exact elimination gives

\[
 \tau=-\frac{48944a^3-40956a^2+375576a+181341}{2593080}.
\]

The cubic has one double root and one simple root. The double-root value
`y0` and `Q,D2,B2,H3''` there are units modulo `S2`. The same argument
with order two gives an `A3` germ of low-curve class two and normal defect
`2^2/4=1`, again impossible. The certificate verifies these unit statements
by exact reduction and gcd, including all algebraic roots of `S2`.

On `S3=0`, the exact corresponding `tau` value makes `P=0` identically in
`Q[a]/(S3)`. It gives `u0=0`, violating endpoint content-freeness.

The exceptional chart `a=-2/3` in (2) has

\[
 \tau=1/18,\quad u_6=-3/4,\quad \beta=0,\quad u_2=U\ne0,
 \qquad H_3=U-2y^2/3+y^3/18.
\]

For its version of (4), the three remainder numerators have polynomial
gcd one in `Q[U]`. This chart has no node-free member and is excluded.

## Closing the identically-zero G stratum

If `G=0`, content-freeness forces `c=0`, and the other coefficients force

\[
 u_2=u_3=u_5=u_6=\beta=0.
\]

Indeed `c=0` has no common root with any of the other coefficient factors
`a,a^2+a+1,a+2`; no exceptional coefficient vanishing has been suppressed.
Now `delta=10`, and the allowed interior defect is `12/5`.
Put `r=z^4`. Then

\[
 R=a u_0-2(a+1)r+a u_8r^2,
\]

while the coefficient of `e^2` along the low curve is

\[
 H_2(z)=a+2a^2u_8(a^3-a^2-a-1)z^4.
\]

There are only the following possibilities.

- If the quadratic in `r` has distinct roots and `H2` is nonzero at both,
  all eight interior points are `A1`. Their defect is four.
- `H2`, being linear in `r` with nonzero constant, can vanish at only one
  of the two distinct roots. Scale that four-point cluster to `z=1`.
  Reduction modulo `c=0` then gives
  `u8=-3a-11/4`, `u0=3/4-3a`. The transverse `(z,W)` Hessian is invertible;
  the residual cubic coefficient is `(10a+11)/84`, a unit modulo `c`.
  These four germs are `A2`. The low curve has class one: the Morse
  parameter is `e`, which vanishes identically on the curve, so it is one
  of the coordinate branches. The other four germs are `A1`.
  Total interior normal defect is `4/3+2=10/3`.
- If the quadratic has a double root, scale it to `z=1`, obtaining
  `u0=u8=(a+1)/a`. Both `H2` and the transverse Hessian determinant are
  units modulo `c`. The residual Morse order is four, giving four `A3`
  germs of low-curve class two. Their total defect is four.

None equals `12/5`. This closes the case that a degree-six bound on a
nonzero polynomial would have missed.

The defects used here are the **normal-sheaf defects** `i^2/n` for the
smooth low curve of class `i<=n/2` in `A_(n-1)`. They are not the
numerical-pullback self-intersection corrections `i(n-i)/n`. In this scope
one can obtain the former by subtracting the latter from the local
Jacobian/conormal length `i`; the exact defect formula in the companion
normal-sheaf note provides the global bookkeeping.

## Surviving line and continuation requirements

The sole remaining value is `a=-1`, equivalently `h=-1/2`. In the normalized
chart,

\[
\begin{aligned}
 u_0&=-16\tau,&u_2&=16\tau,&u_6&=-4\tau,&u_8&=\tau,\\
 \beta&=-8\tau,&\lambda&=8\tau,
\end{aligned}
\]

and

\[
 G=2\tau(z^2-2)^2(z^2+2),\qquad
 R=-\tau(z^2-2)^3(z^2+2).
\]

This is the displayed carrier `Ftau=-B^2+tau q K`. At the two simple
collisions `z^2=-2`, finite exact scratch Morse calculations made the
residual vanish through degree six for all `tau`; this suggested an extra
conductor locus and was a reason to stop short of a global exclusion.
That finite-jet observation is **not** a proof of an identically vanishing
Morse residual or a completed normalization calculation, and is not used
in the theorem above.

The next mathematical move is to compute the normalization/conductor and
actual numerical branch intersections of this line, with all exceptional
`tau` values preserved. The other two collision points have `z^2=2`,
collision order three and Jacobian order two, so the clean ordinary-node
argument does not apply. Integral-carrier existence, global mate descent,
and radical support still require their own checks. The global conductor
loophole must not be replaced by a tangent-form or class-group shortcut.

## Provenance and failed reductions preserved

The fixed specimen was already excluded in the 2026-10-05 note by actual
higher jets. The present work used that family's **entire exact ambient
lift fiber**, the newly proved normal-sheaf defect inequality, and polynomial
elimination. It did not extrapolate from the fixed specimen.

The first attempted universal `degree G<=6` inference overlooked `G=0`.
That oversight was caught during the resumed 2026-10-06 audit; the companion
normal-sheaf note was amended with the explicit `G!=0` qualification, and
this certificate closes the omitted stratum independently. A further
false shortcut would identify normal-sheaf defects with inverse-Cartan
self-intersection corrections; the different values are recorded above.

The nonramified `[4]` certificate also required two resultant-sign repairs:
`Res(P-2z,1+(P/2-2)z)=-(P-2)^2/2`, and the finite-root `[2,2]` analogue
is `-(P-2)(P-2t)/2`. The repaired verifier now passes all its image, content,
selected `A3`, and symbolic ambient-lift checks. Its mathematical content
conditions were unchanged.


---

## 2026-10-06-uniform-order-one-frontier

# Uniform first-jet and defect bounds beyond fixed carrier degree

Date: 2026-10-06. Status: **PROVED conditional on the checked BF duality
and characteristic-zero rational-quartic normal-bundle inputs**; the
algebraic bounds were independently audited in
`2026-10-06-primitive-quadruple-audit.md`, section 6. This is a necessary finite early-jet reduction, not
an upper bound on either defining degree or total multiplicity.

Let C be a smooth nondegenerate rational quartic over an algebraically
closed field of characteristic zero. Suppose a homogeneous pair (F_a,G_b)
has reduced projective support C, with at least one equation of generic
normal order one along C. We may take a,b>=4: a quadric carrier is excluded
by the ruling-class argument, and cubic carriers of arbitrary mate degree
are excluded by Craighero--Gattazzo. This note does not cover pairs whose
two equations have generic normal order at least two.

The transverse algebra is curvilinear at the generic point, so the
complete-intersection multiple structure is quasiprimitive. Write its
generic multiplicity and saturated BF pieces as

    m=ab/4,  E_i=L^i(D_i),  D_0=D_1=0,  0<=i<m.

The finite-flat local Gorenstein pairing audit in
`2026-10-05-mf6-pairing-audit.md` applies at every multiplicity. Thus
the multiplication divisors satisfy

    D_i+D_j <= D_(i+j),
    D_i+D_(m-1-i)=D_(m-1).

The first line-bundle quotient is

    O_P1(-7)^2 -> L=O_P1(e-7),  e>=0,

and the two homogeneous binary sections giving it have degree e and no
common zero. Adjunction and the top BF piece give

    E_(m-1)=omega_C tensor (omega_X|C)^(-1)
           =O_P1(14-4(a+b)).

Set c=7-e and s=m-1. Then

    deg D_s = c s + 14 - 4(a+b).                       (U1)

Since a+b>=8, the last constant is at most -18. Effectivity in (U1)
therefore forces c>0, proving the uniform bound

    0 <= e <= 6.                                     (U2)

This applies for arbitrarily large a,b in the order-one branch. Increasing
the equation degrees cannot make the primitive first quotient direction
have unbounded degree.

For the second defect, write s=2q+r, 0<=r<=1. Since s>=3, q>=1.
Repeated multiplication and effectivity imply q D_2<=D_s, so

    q deg D_2 <= 2cq + cr + 14 - 4(a+b) < 2cq.

The strict inequality follows from cr<=7 and 14-4(a+b)<=-18.
The same argument with s=3q+r, 0<=r<=2, gives

    q deg D_3 <= 3cq + cr + 14 - 4(a+b) < 3cq,

because cr<=14. Hence the following bounds are uniform over both carrier
degrees and multiplicity:

| e | Upper bound on deg D2 | Upper bound on deg D3 |
| --- | ---: | ---: |
| 0 | 13 | 20 |
| 1 | 11 | 17 |
| 2 | 9 | 14 |
| 3 | 7 | 11 |
| 4 | 5 | 8 |
| 5 | 3 | 5 |
| 6 | 1 | 2 |

At e=0, deg D2=0 would produce an embedded primitive triple of type
O(-7), excluded by P-010 for every characteristic-zero smooth rational
quartic. Thus deg D2>=1 in that row. The stronger degree-one/two exclusion
under investigation for a quartic carrier must not be applied to arbitrary
carrier degree.

## Additional lower bound for the order-one carrier

Suppose F_a is the equation whose generic normal order is one, and set
S=V(F_a). It is integral: any irreducible factor of a defining equation
must contain C, by intersecting with the mate, so more than one factor
would give normal order at least two. It is regular at the generic point
of C. Its torsion-free conormal along C is L, hence

    deg N_(C/S)=7-e.

On the normalization the unique lift C^nu of C is smooth and isomorphic
to C. The mate's pullback Cartier divisor is m C^nu, with m=ab/4;
finiteness of normalization creates no additional curve supported over
a closed point. Thus its numerical pullback satisfies

    (C^nu)^# == (4/a)H,  ((C^nu)^#)^2=16/a.

The audited numerical-normal-sheaf inequality in
`2026-10-05-mumford-normal-bound.md` applies even if S is nonnormal at
finitely many points of C. It gives

    16/a <= 7-e,
    a >= ceil(16/(7-e)).                             (U4)

Combined with a>=4, the order-one carrier's necessary lower degree for
e=0,...,6 is respectively 4,4,4,4,6,8,16. This bound is on the degree
of the generically regular carrier; if the mate is thick along C it does
not transfer to that mate. The finite-order defect bounds above are
independently audited; this additional geometric deduction is recorded
with its explicit reliance on the proved normal-sheaf inequality.

## Companion bound for local-cohomology ancestors

For the fixed C0 let u,v be the recorded first-socle targets of degree -3.
If equal-degree homogeneous multipliers F_d,G_d and an ancestor alpha obey
F_d alpha=u, G_d alpha=v, then alpha has degree -(d+3). Suppose at least
one multiplier has nonzero first conormal symbol and alpha has top
principal-part order n>=3. Its top quotient is

    O_P1(7n-4d-5) tensor Sym^(n-1)(k^2).

Contraction by the nonzero linear symbol kills that top section. In
characteristic zero it is a pure (n-1)-st power in the perpendicular
primitive degree-e direction, multiplied by a nonzero binary section.
Consequently

    7n-4d-5-(n-1)e >= 0,
    (7-e)(n-1) >= 4d-2.                              (U3)

For d>=1 this again forces e<=6. If d>=4, the quotient of order two has
no global sections, so n>=3 is automatic for a nonzero ancestor. Coprimality
and the fixed-degree principal-part bound provide a finite maximum n for
each d, but do not bound d. If both multiplier first symbols vanish, the
linear contraction argument does not apply and no e-bound is asserted.

## What this reduction supplies and what remains

The order-one STCI branch can now be organized through finitely many first
direction degrees and bounded early divisor degrees, before allowing either
surface degree to grow. The binary coefficients and divisor positions still
vary in positive-dimensional parameter spaces; this is not a finite list
of curves or a completed classification of embedded triples and quadruples.
Nor does a permitted early structure imply an arbitrarily long Gorenstein
filtration or a global arithmetically Gorenstein thickening.

The entirely thick branch remains separate. Its leading binary tangent
forms do not determine later horizontal multiplicity, and its valid state
must retain higher normal jets, Rees/valuation data, or equivalent information.
The uniform bounds here do not repair the tangent-only recurrence defeated
by y^p+x^(p+r).

This is a direct consequence of the checked normal bundle, saturated BF
duality, and complete-intersection adjunction. No claim of novelty is made.
