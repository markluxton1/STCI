# Strategy assessment for the unrestricted characteristic-zero question

**Scope:** the fixed smooth rational quartic
`C=[s^4:s^3t:st^3:t^4]` over an algebraically closed field of characteristic
zero, with arbitrary homogeneous defining degrees. **STCI remains open.**
This is a research-allocation assessment, not a new theorem or promotion.
It closes the two investigations following the
[October 30–31 integration](2026-10-30-four-streams-integration.md).
The user requested this assessment before another research round, and
requested that extraction, generalization and strategic reassessment become
continuing parts of the process. Existence remains a live possibility.

## 1. What the recent work has added

The principal gains are geometric necessary conditions and sharper
understanding of which information the global equations retain. They do
not establish a new exclusion of all surviving degrees, or construct a
characteristic-zero STCI pair.

| Contribution and evidence | Actual addition | Effect on both possible answers |
|---|---|---|
| [Jacobian/contact identity](2026-10-31-cyclic-cover-duality.md), with its linked independent audit | For every hypothetical proper supported pair, the actual Jacobian minors generate the socle sheaf and `M12-2M03` lies in `(F,G)`. This is more than a numerical socle budget. | A construction must satisfy the identity. A nonexistence argument still needs an incompatibility with global equations; involutivity itself supplies none. |
| [Full tropical descent](2026-10-31-tropical-descent.md), with its linked independent audit | The full saturated finite-flat family must move in characteristic zero: its tautological degree is positive. The endpoint index formula is exact, and this full family cannot be the global intersection of two Cartier divisors upstairs. The movement deduction uses the existing Hellus–Hübl obstruction. | A possible STCI must use genuinely moving transverse structure. The easy global CI presentation of the reduced curve upstairs is not a presentation of its required full thickening. This constrains construction as well as obstruction. |
| [Affine endpoint criterion](2026-10-30-four-streams-affine-endpoints.md) and [fixed surfaces](2026-10-30-fixed-surface-configuration.md), with linked audits | The omitted endpoint detects residual attachment; the finite flat plane-pencil algebra retains normal multiplication invisible in restrictions to the two planes and Q. | These are exact tests for actual pairs. Neither supplies a universal strict inequality or a pair attaining equality. |
| [Full conductor boundary](2026-10-31-tropical-conductor.md), with linked audit | Finite duality retains the full boundary algebra, its pairing and its embedding; no unjustified Gorenstein assumption on the saturated family is needed. | This is a useful application of classical duality. Its determinant identity recovers the existing genus budget, rather than adding another obstruction. |
| [All-multiplicity moving control](2026-10-31-moving-family-descent.md), including the separately reviewed affine extension | Positive movement, curvilinear fibers and both locally CI endpoint contractions coexist for every multiplicity. Both entire affine pieces have actual two-polynomial presentations. Their fixed projective thickenings are not homogeneous CIs. | Local compatibility has substantial flexibility. A construction must solve the global presentation problem; a local obstruction must use additional data absent from this control. The affine failure is quantified over presentations of these fixed thick schemes, not every affine presentation of reduced C. |
| [Multiple-quadric matrix control](2026-10-31-simultaneous-equation-geometry.md), with linked audit | A determinant-`q^2` matrix with defects at the marked endpoints need not factor through two determinant-`q` maps, even with an arbitrary intermediate rank-two bundle. | Iterating line-bundle calculations on Q is not justified. Its distinguished column cuts out two lines, so the control does not settle matrices whose column has reduced support C. |

These are independently reviewed **provisional** contributions, not newly
promoted results. The all-quartic-carrier exclusion and resulting degree
floor `a,b>=5` are inherited [R-0001](../results/quartic_carrier_exclusion.md),
not discoveries of this round. The present assessment does not claim that
all possible uses of the new identities have been exhausted.

## 2. Closeout of the two bounded investigations

Both producers were fresh `gpt-6-astra/ultra` workers with bounded tasks and
no nested delegation. They completed their tests and stopped. The following
handoffs were initially producer deductions. The fresh strategy reviewer
subsequently reconstructed the displayed elementary matrix and ramification
arguments; the generalized-divisor and Picard-theory source applications
did not receive a full independent audit. Section 5 records that boundary.

### A. The distinguished column on a multiple quadric

Let `Y=V(F_a,G_b)` be a proper homogeneous complete intersection and suppose
`q^N=AF+BG`, where `q=x0*x3-x1*x2`. Put `X=NQ`. The matrix

\[
M=\begin{pmatrix}F&-B\\G&A\end{pmatrix}:
\mathcal O(-a-b)\oplus\mathcal O(-2N)
\longrightarrow\mathcal O(-b)\oplus\mathcal O(-a)
\]

has cokernel `I_(Y,X)`, embedded in `O_X` by the row `(-G,F)`.
Indeed, if `-Gu+Fv=q^N h`, then
`-G(u+Bh)+F(v-Ah)=0`; regularity of `(F,G)` makes
`(u+Bh,v-Ah)=t(F,G)`. This identifies exactly the matrix image.
The relevant object is thus an effective generalized divisor **with its
ideal embedding and split global presentation**. Its quotient must have
reduced support C. Merely requiring the module's nonfree locus to lie in C
loses that condition. [Hartshorne, *Generalized Divisors and Biliaison*,
§2, Proposition 2.1](https://arxiv.org/pdf/math/0301162) supplies the general
divisor language; it does not decide existence of these presentations.

Even generic invertibility along C cannot be assumed from sole-support
local CI hypotheses. In `K[[u,v]]`, take `F=u^2`, `G=v^2`, `q=u+v`.
In characteristic zero the minimal nilpotence exponent of q modulo `(F,G)`
is three, and

\[
q^3=(u+3v)F+(3u+v)G.
\]

Every matrix entry is in the maximal ideal, so the cokernel has two minimal
generators over `K[[u,v]]/(q^3)` and is not invertible. This is a local
control, not a global realization on C. It rules out an unproved passage
from the local CI assumption to a line bundle with only isolated defects.

On the other hand, `U=Q\setminus C` is affine because C has ample class
`(1,3)` on Q. Successive nilpotent layers are `O_Q(-2j)|_U`, so their first
and second cohomology vanish. The exact sequence for Picard groups of
thickenings gives `Pic((NQ)\setminus C) = Pic(Q\setminus C)` for every finite
N; see [Stacks, §37.4](https://stacks.math.columbia.edu/tag/0C6Q).
The extension issue lies across C, not in lifting line bundles on this
affine complement.

**Extracted content and disposition:** retain generalized divisors that may
be non-Cartier along the whole curve, their ideal embeddings and the actual
global presentation. This is a more faithful formulation and identifies a
missing hypothesis in a proposed simplification. It currently offers no
new uniform restriction or construction. Stop classification of arbitrary
modules or simple-quadric factors. Reopen only with a theorem or construction
that uses the distinguished quotient support and adds information beyond
the original two homogeneous generators. The local countermodel does not
exclude a stronger theorem using global STCI hypotheses.

### B. Two marked fibers and function-field abc

Write `z=t/s`. Every degree-a coordinate monomial restricts to a scalar
multiple of `z^w`, after removing its common homogeneous factor, with
`w=alpha1+3*alpha2+4*alpha3`. Thus a defining equation restricts to
`sum c_i z^(w_i)=0`. Linear independence of distinct Laurent powers implies
that every minimal nonempty vanishing subsum has just one weight, hence
constant ratios. Pullback to any dominant reduced curve cover preserves
this fact. This treats arbitrary polynomials, not merely binomials.

For a smooth connected projective reduced curve `D` and finite degree-r map
`h:D -> C=P1` in characteristic zero, let
`S=h^(-1){p0,p_infinity}_red`. Riemann–Hurwitz gives

\[
2g(D)-2+|S|=\sum_{P\notin S}(e_P(h)-1).
\]

If normal-direction functions require further zeros or poles in a set S',
the right side acquires `|S'\setminus S|`. This identifies the budget in
function-field differential estimates: interior ramification and additional
divisor support. [Corvaja–Zannier, *An abcd theorem over function fields and
applications*, pp. 438 and 443](https://www.numdam.org/article/BSMF_2011__139_4_437_0.pdf)
states the nondegeneracy/support hypotheses and the differential estimate.
The finite flat nonreduced CI cover has a nilpotent different; it is not
a reduced degree-ab cover to which an ordinary branch-divisor argument
applies. The existing [pencil control](2026-10-30-four-streams-pencil.md)
also prevents assuming bounded auxiliary-cover genus from rational support.

**Extracted content and disposition:** direct restriction forgets the
transverse geometry we need. The same degeneracy applies to monomial
parametrizations more generally; the displayed logarithmic Hurwitz identity
applies to any reduced cover of P1 with two marked target points. Neither
generalization is a new STCI theorem. Stop the direct-coordinate
abc/Wronskian route. Reopen only after an actual-pair construction supplies
a nondegenerate relation, a comparative bound on interior branching and
extra divisor support, and a geometric consequence for construction or
exclusion. A bound is needed before more cover classifications are useful.

## 3. What is exhausted, and what is only a reformulation

The **tested shortcuts** are exhausted: constant tropical families; forcing
a residual curve from movement or local Gorensteinness alone; automatic
simple-quadric factorization; reduced-coordinate abc; first-trace detection;
and reduced-Lagrangian rigidity applied to the entirely thick structure.
Each has a stated failure mechanism in the linked evidence. This does not
retire tropical geometry, valuations, contact geometry, or generalized
divisors as subjects.

The affine endpoint equality, full finite-cover nilpotence, distinguished
generalized divisor with split presentation, and fully glued fixed-twist
formal pair are **exact formulations** of the remaining global condition.
They become progress only when they expose an independently usable
construction, restriction, comparison or general geometric principle.
In particular, [the existing formal-pair equivalence,
§6](2026-10-27-formal-neighborhood-residual-visibility.md) already extends
fully compatible twisted formal sections to homogeneous equations. There
is no further algebraization problem after those exact data and uniform
power containment have been supplied. Likewise, writing a Serre bundle
does not establish its required splitting.

The earlier primitive elliptic and order-one projection incidences remain
unresolved in the [equation search](../STCI_SEARCH.md) and
[October 29 continuation](2026-10-29-search-continuation.md). These are actual
parameterized homogeneous sources with precise admissibility and descent
tests. The [order-two survivor](2026-10-30-projection-order-two-survivor.md)
has a primitive elliptic residual and a specified extension problem. Their existence
value is real: one successful actual pair would settle the unrestricted
question. But an unfinished incidence is not itself evidence of a viable
construction, and another empty slice would not establish nonexistence.
No new admissible source or sufficient descent mechanism has emerged here.

## 4. Comparing directions and recommending the next allocation

| Direction | What would advance the full question | Present evidence and limitation |
|---|---|---|
| Existence | Construct an actual proper pair with generic multiplicity `ab/4`, or supply equivalent full global data with a proved sufficient construction. A bounded family is legitimate if it has a reason to reach this endpoint. | Affine and local flexibility is substantial; movement is a requirement to incorporate. None of the recent controls supplies the missing homogeneous pair. An experiment needs a justified next step in an existing exact source or a new construction source. |
| Nonexistence | Prove an incompatibility valid for arbitrary pairs, or a reduction placing every hypothetical pair in an already excluded class. | The new contact and movement conditions are necessary but compatible with tested local models. No strict global inequality or exhaustive reduction has been found. |
| Geometric understanding | Generalize a mechanism with its correct hypotheses, identify what information is lost by a model, or establish a flexibility theorem that changes constructive expectations. | This is a substantive outcome even without an immediate contradiction. It must alter the model, a proposed construction, or a precise missing implication; further examples of the same failure do not suffice. |

**Recommendation:** do not automatically extend either just-completed
investigation or open another local classification. At present no specific
new theorem route is sufficiently supported to recommend a technical
campaign. The next allocation, after this assessment is reported, should
be one bounded selection investigation: compare a concrete construction
mechanism with a genuinely new global implication, using primary literature
and the existing controls. Give the constructive possibility equal standing;
the aim is to understand realizability, not to manufacture a quick
contradiction. This is a recommendation for selecting the next mathematical
experiment, not a claim that a promising construction has already been found.

At its start, that selection investigation must name the two concrete
mechanisms being compared and the proposed new input for each. An existing
source with a new sufficient construction or extension step is eligible;
novel notation or a new source is not required. It must produce at most one recommended next
experiment with: exact hypotheses and quantifiers; the actual geometric
object; the new input beyond an equivalent formulation; an explanation of
what either outcome teaches about unrestricted STCI; and a stopping rule.
It may instead conclude that neither candidate currently merits expansion,
identifying the particular missing input for each.
It must not demand a proof of the desired theorem before exploration:
a specific unproved mechanism with meaningful outcomes is enough to test.

**Stopping conditions for that allocation and any ensuing experiment:**

1. Stop and integrate once a construction, a new general implication, or a
   decisive failure of the proposed mechanism is obtained; do not append
   neighboring cases automatically.
2. Stop expansion if the proposed step is only a renamed global
   two-generator/splitting condition or repeats an existing genus budget.
   A claimed arbitrary-pair exclusion must not assume an unproved reduction
   to primitive, saturated, smooth-root, generically invertible or
   fixed-degree structures. A constructive experiment may deliberately
   choose such a class: success still proves existence. Its assumptions
   must be compatible with the actual proposed construction, and failure
   remains restricted to that source.
3. A local example or classified family must test a named general principle
   or a concrete construction mechanism. After it has done so, extract the
   result and its useful generalization before assigning more examples.
4. An empty construction family updates that source, not the global answer.
   A surviving local model updates feasibility, not projective existence.
   Lack of a contradiction is not failure; a proved flexibility mechanism
   or a better global construction target may be the main result.
5. If the bounded selection finds no distinct mechanism, report that outcome
   and its missing input. Do not replace it with a series of narrower tests.

No next research round is launched by this record. The broader goal remains
active and mathematically unresolved.

## 5. Independent strategy challenge and disposition

A fresh `gpt-6.1-sol/high` reviewer, with no inherited conversation and no
nested delegation, challenged this draft against the linked evidence.
The reviewer accepted the bounded selection allocation after these
corrections, all applied by the lead:

- **Material scope correction:** the original stopping rule could bar a
  special-family construction because its hypotheses did not exhaust
  arbitrary pairs. Such hypotheses are legitimate construction choices;
  only a claimed exhaustive reduction or unrestricted exclusion needs
  proof of coverage. Repeated countermodels must not become a rule against
  existence experiments.
- **Source correction:** existing projection sources are already concrete,
  with exact unresolved support and extension tests. The missing ingredient
  is a justified next step in those sources or a new source, not a lack of
  any explicit candidate framework.
- **Operational correction:** name the two mechanisms and their new inputs
  at the start of the selection investigation. If neither is selected, name
  its missing input rather than initiating an indefinite strategy loop.

The reviewer independently checked the matrix-kernel argument and twists,
the local cubic identity, minimal nilpotence exponent and two-generator
noninvertibility conclusion, the Laurent-weight minimal-subsum argument
and its pullback, and the logarithmic Hurwitz identity. These elementary
claims have bounded independent review. The reviewer did **not** audit the
external generalized-divisor/Picard theory applications or reconstruct all
earlier proofs; those earlier notes retain their own linked audit status.
The lead consulted the linked primary sources while closing the handoffs.
Nothing here has been canonically promoted.

The reviewer found no evidence-supported replacement technical campaign.
Both producers and the reviewer have completed their assignments; none is
continuing into new cases. The recommendation is reported before any next
research round, with the mathematical objective still unresolved.
