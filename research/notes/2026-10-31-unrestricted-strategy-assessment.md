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

## 6. Executed comparison: canonical gluing versus duality specialization

The recommended bounded selection was carried out after the preceding
assessment was reported. Two fresh `gpt-6-astra/ultra` workers, without
nested delegation, examined concrete mechanisms: construct a global source
from the surviving elliptic target and its marked rational curve; or obtain
a new global constraint by specializing actual CI duality through the full
torus limits. No additional local-type or cover classification was assigned.

### The duality-specialization mechanism

**Independently checked diagnostic, with the scope recorded below.** The
correct object to specialize is the relative dualizing complex, not an
assumed invertible special canonical sheaf. This is the distinction in
[Stacks, §109.19](https://stacks.math.columbia.edu/tag/0E6N) and
[§86.9](https://stacks.math.columbia.edu/tag/0E5W). Write R=k[[tau]], let
X be a full flat Hilbert degeneration, let Z be its special curve, and
let `0 -> T -> O_Z -> O_H -> 0` remove its endpoint embedded points.
Put `s=a+b-4`, and on P3_R set

\[
\Omega=\mathcal Ext^2(\mathcal O_X,\mathcal O(-4)),\qquad
\mathcal E=\mathcal Ext^3(\mathcal O_X,\mathcal O(-4)).
\]

The producer's base-change calculation gives

\[
0\to\Omega/\tau\Omega\to\omega_H\to\mathcal E[\tau]\to0,
\qquad \mathcal E/\tau\mathcal E\simeq T^D,
\]

with Omega R-flat and the two finite-length modules of equal length at
each endpoint. Codimension two and the nonzerodivisor tau leave only
Ext degrees two and three; the base-change exact sequence supplies these
claims. The primitive generator of the rank-one free module
`H0(X,Omega(-s))` specializes to a nonzero map

\[
\mathcal O_Z(s)\longrightarrow\Omega/\tau\Omega\subset\omega_H.
\]

It kills T and factors through O_H(s). **Nonzero need not mean generically
invertible** on the nonreduced generic transverse algebra. If generic
invertibility is separately established, the inclusions
`O_H(s) subset Omega/tau Omega subset omega_H` have successive quotient
lengths ell and ell, where `ell=length(T)`. This recovers the existing genus
budget; it is not a second numerical equation.

The producer calibrated the actual twist on the existing
[all-degree line control](2026-10-30-four-streams-degeneration.md), without
creating another family. With
`f_tau=Y A_tau+tau X^d`, `g=Y^d` and
`A_tau=Z^(d-1)+tau^2 W^(d-1)`, on `A_tau != 0` use
`h=Y+tau X^d/A_tau`, `k=X^(d^2)`. The determinant changing these generators
is `(-1)^d tau^d A_tau^(1-d)`, so adjunction gives
`tau^d eta_(f,g)=+/- A_tau^(d-1) eta_(h,k)`.
The inherited saturation relations show that tau^d kills the saturation
quotient, and this exponent is minimal where A_tau is invertible.
The resulting special canonical section on the hull
`H=V(Y,X^(d^2))` is `Z^((d-1)^2)`; the opposite limit gives
`W^((d-1)^2)`. Its zero length is `d^2(d-1)^2=2 ell`.
Thus the actual twist accommodates both endpoint defects.

The inspected [Gallego–González–Purnaprajna paper](https://arxiv.org/abs/1211.5458)
allows non-Cohen–Macaulay multiple flat limits; it provides no contrary
fixed-quartic theorem. [Van Straten–Warmt](https://arxiv.org/abs/1104.3070)
uses an almost-complete-intersection presentation, which an arbitrary full
initial ideal need not have. No perfect pairing on every endpoint defect
was inferred from that result.

**Disposition:** do not select this as a standalone campaign. A new argument
must control the canonical lattice, the generic rank of the specialized
map, or its two opposite specializations using additional quartic geometry.
Derived duality describes those data but does not bound them. Constructively,
the limits show legitimate ways a supported CI can acquire defects. This
stops the proposed shortcut, not all uses of degeneration or duality.

### The construction mechanism and proposed next experiment

The [canonical-extension proposal](2026-10-31-elliptic-canonical-extension.md)
uses the nodal genus-four curve obtained by gluing the elliptic residual
to the marked rational curve at the four inverse points. It identifies the
canonical quadric source and separates actual line-bundle gluing from
projective agreement at the nodes. The proposal includes smooth quadrics
and quadric cones, with a sufficient global extension and contact test.
Its proof and exact remaining gates are in the linked note.

The constructive candidate is the existing
[palindromic elliptic target](2026-10-30-projection-elliptic-target-palindromic.md),
whose smooth-source extension fails. That does not dispose of the cone
model retained by [R-0002](../results/cartier_singleton_lift.md).
**Component Picard compatibility is not yet verified for this target.**
The identity `L^2=O_E(Z)` in the earlier survivor record used actual-source
compatibility and cannot be assumed from target ramification alone.
Conditional on that equality, its Möbius marking selects the canonical
cone. The subsequent gluing, contact and mate-descent gates remain separate.

The proposed next experiment is to replay the existing exact target data,
check the component Picard equality, then evaluate the intrinsic node-gluing
and contact conditions. A failure stops this candidate; a success constructs
an admissible degree-eight carrier and then permits its separate actual
mate-descent test. No pass or carrier is claimed here. The experiment is
not a passport enumeration, a new classification, or an exhaustive source.

### Independent challenge and current disposition

A fresh `gpt-6.1-sol/high` reviewer, independent of both producers and with
no nested delegation, reconstructed the canonical-extension criterion and
challenged the allocation. The [audit](2026-10-31-elliptic-canonical-extension-audit.md)
found no material defect and supports the one fixed-target experiment.
It checked the reducible canonical embedding, the cone vertex and Cartier
conditions, actual node-gluing residues, unique section recovery, and the
coefficient-one argument for surface birationality and full inverse support.
It also checked the conditional cone inference without assuming the
unevaluated component Picard equality.

For the alternative, the reviewer reconstructed the Ext base-change
sequence, the nonzero-versus-generically-invertible distinction, and the
actual-twist line calibration. The optional paper-specific pairing
discussion was not audited and is not a premise of the allocation.
The resulting diagnostic is independently checked within that boundary.

**Recommendation at this checkpoint, subsequently executed in §7:** run
the one fixed palindromic-target test
in the stated order: independent target replay and normalized support;
component Picard equality; residue gluing; unique-section recovery and
nonzero contact determinant. Stop this candidate at its first failed gate
and extract the obstruction's geometric meaning. If all gates pass, an
actual degree-eight carrier is obtained and its full conductor/mate descent
is the next separate question. Failure is not authorization to enumerate
further targets. No reduction of arbitrary STCI pairs to this construction
is asserted or needed for a successful existence example.

Both producers and the reviewer completed their bounded assignments, and
this recommendation was reported before the technical experiment started.
At that checkpoint no candidate gate had been run and no carrier or mate
was established. All contributions remained reviewed provisional results.

## 7. Fixed-target test completed: polarization fails, with a spin interpretation

The [fixed-target calculation and geometric extraction](2026-10-31-palindromic-polarization-spin.md)
complete the selected experiment. The exact target replay passes: the
elliptic normalization, four normalized contact points, and reduced
disjoint ruling boundaries are verified. The component Picard test fails:
`H0(E,L^2(-Z))=0`. The restriction matrix in the proof has determinant
`486 eta/25 != 0`, with eta^2=-4/5. Thus these four marked points do not
form a hyperplane section in the elliptic embedding by |2L|. The candidate
stops here; residue gluing, section recovery, contact and mate descent
were deliberately not run.

The useful generalization concerns the complete balanced contact data,
not another parameter slice. For any smooth elliptic target with the
specified disjoint boundaries and full `(5^4)` fiber, Riemann--Hurwitz and
that fiber give `O_E(2Z)=L^4`. The remaining defect
`delta=L^2 tensor O_E(-Z)` is two-torsion. It is exactly the theta
characteristic induced by the odd-ramification map `f=B^3/A`. Component
polarization requires trivial/odd spin; this fixed target has
nontrivial/even spin. The proof checks the primary odd-ramification
construction rather than transferring a cover-counting theorem.

**Effect on the full question:** the result identifies a global line-bundle
obstruction invisible to degrees and contact counts. It explains why the
old successful target incidence does not furnish either the specified
smooth source or its cone alternative. The canonical-extension criterion
remains a sufficient construction tool. No theorem says that every target
with this passport has even spin, and no reduction of arbitrary STCI pairs
to such elliptic covers is known. Odd spin would pass only this component
gate, leaving node gluing and the contact condition. Existence remains live.

**Disposition:** close this fixed target and do not assign another support
or cover enumeration. A future balanced elliptic construction would need a
mechanism producing the required spin together with the actual functions
A,B; merely selecting another branch partition does not supply that input.
No new technical continuation is selected at this checkpoint. A uniform
nonexistence use would need an additional arbitrary-pair implication, while
an existence use needs one source satisfying the remaining sufficient
conditions. Neither is currently established by the spin calculation.

Independent review of the proof, replay coverage, spin interpretation and
stopping decision is recorded with the result. The broader goal remains
active and unresolved; this is a completed bounded experiment, not a
resolution of unrestricted STCI.

## 8. Subsequent selection: birational transport and complement pencils

**Status: independently reviewed provisional deductions and allocation.**
The [bounded independent audit](2026-10-31-transport-pencil-strategy-audit.md)
reconstructs the arguments and checks their geometric and strategic scope.
After the fixed-target result was reported, two fresh
`gpt-6-astra/xhigh` workers independently assessed the mechanisms below,
using primary literature and the existing proofs. Neither tested another
elliptic target, classified local structures, or launched a technical
campaign. Both completed their bounded read-only assignments. The lead
also checked a projective-bundle theorem relevant to globalizing the
affine construction. The findings concern what these mechanisms supply;
they do not change the unrestricted answer.

### Birational transport must transport transverse thickness

[Mella–Polastri, Theorem 1 and Corollary 1](https://arxiv.org/pdf/0906.4858)
give Cremona equivalence of birational embeddings in codimension at least
two. [Ciliberto–Cueto–Mella–Ranestad–Zwiernik, §2.2 and Remark 2.4](https://people.math.osu.edu/cueto.5/CremonaLinearizations.pdf)
give a constructive treatment and a correction to the earlier proof.
These supply a birational transformation of this reduced rational curve
to a line, with both ambient maps defined at the respective general
points. They do not assert transport of complete-intersection equations.

Such an ordinary equivalence is an ambient isomorphism near those general
points. Consequently strict transforms of two divisors cutting out a
reduced CI retain generic intersection multiplicity one. If their proper
intersection in P3 had sole support C, Bézout would force `ab=4`.
Nonplanarity excludes a degree-one factor and the unique containing
quadric excludes two independent quadrics. Taking powers of the same
equations leaves their strict transformed supports unchanged. Thus
linearizing the reduced embedding does not create the required thickening.
This diagnostic does not apply when C is an indeterminacy center, or
exclude transport of a genuinely nonreduced CI.

The alternative blowup link with a conic on V5 is already developed in the
[equation dictionary and support criterion](2026-10-28-blowup-residual-geometry.md).
On that common model the actual strict-transform intersection must be
supported on the exceptional divisor E over C. Support on the image
surface in V5 is insufficient: its inverse image also contains the other
exceptional divisor, whose rulings can be genuine residual trisecants
downstairs. Another Cremona model or section-ring presentation does not
solve this existing condition. A viable new construction needs a specified
thickened CI and a reason its pair-dependent exceptional corrections work,
or a construction on a model centered on C supplying those corrections.

### The complement pencil is equivalent to the global question

For this irreducible curve put `U=P3\C`. There is an elementary equivalence

`C is STCI  <=>  U admits a nonconstant morphism to P1`.

Indeed, a supported pair of degrees a,b gives
`[F^(b/g):G^(a/g)]`, where g=gcd(a,b). Conversely,
`Pic(U)=Pic(P3)=Z` because the ambient schemes are regular and the omitted
set has codimension two. The two sections defining a morphism extend
across C as sections A,B of O(n). Nonconstancy forces n>0. Their common
zero set is contained in C; there is no common hypersurface component,
and projective intersection theory makes their nonempty support equal C.
Every such morphism is affine: the inverse images of the standard affine
charts are the affine principal opens D_+(A) and D_+(B). Thus affineness of
the surface fibers is automatic and provides no additional test.

After choosing irreducible factors of an STCI pair, its equalized pencil
has connected generic fiber. A nontrivial rational composition of degree
d would force d to divide both b/g and a/g, since its zero and pole fibers
each have a single irreducible support. Over C, the complement U is simply
connected by general position. The orbifold surjection of
[Artal Bartolo–Cogolludo, Proposition 1.5](https://arxiv.org/pdf/1002.2097)
therefore allows at most two multiple fibers, with coprime multiplicities
if both occur. This is compatible with b/g and a/g, not a contradiction.
The logarithmic differential of F^(b/g)/G^(a/g) has poles along the carrier
surfaces inside U; it is not a regular form on U with boundary only over C.
The resolved pencil uses `(F^(b/g),G^(a/g))`, not automatically `(F,G)`.
These distinctions prevent inappropriate reduced-cover or boundary
arguments. The [earlier pencil control](2026-10-30-four-streams-pencil.md)
already rules out bounding exceptional-cover genus from rational support.

The equation pencil on U is different from the
[two-hyperplane projection on the full CI](2026-10-30-fixed-surface-configuration.md#4-the-plane-pencil-converts-every-admissible-pair-into-one-finite-cover).
There `Z=V(F,G)` denotes the entire, generally nonreduced curve;
`[x0:x3]:Z -> P1` has degree ab. Its reduction C maps by `[s^4:t^4]`,
of degree four, with the two marked totally ramified fibers. This reduced
map is separable in characteristic zero and in odd characteristic, and
purely inseparable in characteristic two. Its usual ramification formula
does not become a formula for a reduced degree-ab cover: Z is not one.

A nonexistence use needs an additional comparison using the embedded
quartic, such as a specified negative quotient of an actual nef Hodge
bundle; no such comparison has been obtained. A construction of a
fibration on this exact complement would suffice for existence, but the
equivalence alone does not produce one. Neither multiple-fiber patterns
nor abstract affine surface fibrations supply the required embedded
boundary contraction.

### A literature restriction on polynomial amplification of a bundle section

The affine Serre/Ferrand construction is recorded in the
[literature ledger](../LITERATURE_LEDGER.md#ferrand--szpiro).
Suppose a section of a rank-two bundle E on P3 has zero scheme supported
on C. A possible construction would apply two globally defined fiberwise
homogeneous polynomial maps
`P:E -> L1`, `Q:E -> L2`, of positive fiber degrees r,s, whose only common
zero in every fiber is the origin. Evaluating them on the section would
give a supported pair in the two line bundles.

This construction cannot improve a genuinely nonsplit E in characteristic
zero. The powers P^s,Q^r induce a morphism
`P(E) -> P(L1^s direct-sum L2^r)` over P3, of fiber degree rs. If rs>1,
[Amerik–Kuznetsova, Theorem 2](https://arxiv.org/pdf/1609.00910) forces both
bundles to split: its base hypotheses are simple connectedness and
`H1(B,L)=0` for every line bundle, both satisfied by P3. If r=s=1, the
fiberwise no-common-zero condition itself gives an isomorphism of E with
the split target. The theorem is used over C; the conclusion transfers to
an algebraically closed characteristic-zero field by descent to a finitely
generated subfield, base change, and the splitting criterion for bundles
on projective space.

Geometrically, uniformly eliminating all unwanted fiber directions is
already too strong: this type of nonlinear operation cannot remove the
projective bundle's failure to split. This is a consequence of a published
theorem, not a newly claimed STCI obstruction. Actual pairs are not known
to arise from such everywhere nondegenerate bundle maps. Maps allowed to
degenerate away from the particular section remain possible; their
degeneration must be controlled rather than assumed harmless. No claim
about all nonhomogeneous operations or all thickenings follows.

The characteristic comparison is concrete: in characteristic p, relative
Frobenius gives `P(E) -> P(F_B^*E)` over B, of degree p on each projective
line fiber, including when E is nonsplit. It illustrates why the
characteristic-zero splitting theorem cannot simply be transferred.
Frobenius does not thereby make the target bundle split or give equations
for the projective curve.

### Recommendation and stopping conditions

Do not launch a birational-model enumeration, an exceptional-cover
classification, or a fiberwise-powering search from these findings.
The two principal mechanisms currently lack, respectively, exceptional
correction data and an independent complement-fibration construction or
quartic-specific comparison. The bundle theorem identifies an additional
precise limitation of a seemingly constructive operation. None justifies
discarding the possibility that C is STCI.

Reopening one of these routes requires a *specified mechanism to test*,
not a proof of success in advance: name the source thickening and its
exceptional corrections, the actual sheaf comparison, or the controlled
degeneration of a bundle map along its section. State an outcome that adds
information beyond the equivalent two-equation condition. Stop once that
mechanism succeeds or its essential premise fails; do not append adjacent
examples automatically. This stops only these bare mechanisms, not the
existence program or the overall research goal. At this selection
checkpoint no such next technical experiment is recommended.

A fresh `gpt-6.1-sol/high` reviewer independently reconstructed the three
deductions, checked the primary theorem hypotheses, projectivization
conventions and characteristic comparison, and challenged the allocation.
No material mathematical defect remained. The reviewer confirmed that
stopping is justified only for the bare mechanisms just tested, without
demanding a proof of prospective success before exploration. In particular,
the earlier graph-residual construction proposal is not disproved; it
still needs a specified family and correction mechanism. The reviewer
completed the assignment. No canonical result was promoted, no inherited
certificate was rerun, and no new technical campaign was started.

## 9. A constructive paired cover clears polarization, then fails gluing

The next selection supplied a concrete input rather than another passport
or arbitrary target. Primary work on hyperelliptic odd coverings motivated
pairing the branch values **within** the zero and pole groups of a
degree-five rational map. An explicit rational degree-four map and a
double-cover base change then construct a smooth elliptic E with actual
functions A,B of degrees two and six. The
[construction and proof](2026-10-31-paired-elliptic-construction.md) establish
birationality, full contact five at four distinct smooth marked points,
trivial induced spin, and the genuine equalities `O_E(Z)=L^2`, `M=L^3`.
This is a positive construction of the target data that the previous
fixed target failed to supply. It is not a carrier or a mate.

A fresh reviewer independently checked the construction and recommended
one canonical residue experiment. That recommendation and its first-failure
rule were reported before the experiment proceeded. The residue calculation
then identifies the gluing ratios, up to one common scalar, with
`J(x_i)=x_i(x_i-a)/(x_i-u)^3` at four distinct points of P1. The
degree-three map J cannot have all four points in one fiber. Thus the
node-gluing class is nontrivial, despite compatible polarizations on each
component. The [audit](2026-10-31-paired-elliptic-construction-audit.md)
independently reconstructs the normalization, actual coordinate-section
divisor and quadratic residues, including the branches at infinity.

**Effect on the full problem:** spin and the actual ruling divisors can
be controlled geometrically, so their earlier failures do not eliminate
the constructive interface. Compatibility on the reduced union is a
further global condition, not a numerical consequence of them. The
degree comparison explains this particular failure without another cover
classification. It gives no exclusion of every elliptic target or
arbitrary STCI pairs. For existence, a subsequent mechanism in this
interface needs to impose node gluing together with the component data;
for nonexistence, a general incompatibility or arbitrary-pair reduction
is still missing.

These two target tests have exposed different global compatibility
conditions but have not produced an actual carrier. Do not let the next
allocation become another attempt to repair this target one condition at
a time. Returning to this interface needs independent geometric input
controlling the global embedding, with the later mate problem retained.
No replacement technical campaign is selected by this failure.

**Disposition:** stop this target. Section recovery, source contact,
carrier construction and mate descent were not run. No adjacent root
choice, cover, or target enumeration is assigned. The preceding ribbon
retrieval located existing net/projection evidence and did not reopen any
closed quartic carrier. The constructive producer and independent reviewer
completed their tasks. The contributions remain reviewed provisional;
unrestricted characteristic-zero STCI remains open.

## 10. Arbitrary-pair selection: foliation and affine boundary losses

Two fresh, bounded literature investigations returned to arbitrary pairs
after the target construction in §9. Their
[deductions and source hypotheses](2026-10-31-foliation-affine-selection.md)
are preserved together. They do not select another technical campaign.

The normalized rational-pencil foliation has C in its singular locus.
Its transverse two-form either vanishes along all C or defines a finite
non-Kupka divisor of degree `4e-14`, where O(e) is its normal determinant.
The latter alternative extends the smooth-component line-bundle argument
past intersections with other singular components, but supplies no bound
in the first alternative. When the raw form has no divisorial factor,
all C is non-Kupka and its Baum–Bott residue is exactly `(a+b)^2/4`:
off-C singular curves have zero residue because the actual form there is
a unit times an exact differential. The nonzero residue and pointwise
vanishing are compatible. This is information about the full transverse
singularity, not a contradiction on the reduced curve.

The affine investigation separates the residual-degree budget as
`ab-4m=(ab-mu)+(mu-4m)`, using the generic degree mu of `(f,g,ell)`.
The two terms distinguish generic loss at infinity from sheets escaping
when the target approaches the distinguished axis. The same argument
gives `dm <= mu <= ab` for a curve of degree d, so it is not a
quartic-specific characteristic-zero obstruction. The original reduced
affine equations already give a finite map of degree four with ab=6:
finiteness removes one gap while leaving the residual boundary line.
Jelonek's nonproperness bound and Mondal's semidegree equality criterion
do not force either gap positive or construct simultaneous equality.
Vénéreau's derivative estimates need subalgebra input that ambient ideal
containment does not provide.

These are useful deductions and scope corrections, not another excluded
class of STCI pairs. Compared with §9, the positive target construction
achieved actual geometric data but stopped at one independent gluing
condition; the present arbitrary-pair tests reach all pairs but currently
give compatible conditions. Neither breadth without a new implication nor
a succession of narrow failures should dictate the next allocation.

**Recommendation:** stop the bare applications just tested. No next
technical experiment is selected at this checkpoint. A proposed restart
should identify new input controlling an actual normalized residue, a
strict boundary-loss comparison, or a construction attaining compatibility
in the fixed projective embedding. These are directions for specifying a
test, not claims that such a mechanism has been found. An unproved
mechanism is eligible for exploration when its premise and informative
outcomes are concrete; a proof of success is not required beforehand.

**Stopping conditions:** first test the proposed mechanism's essential
input. Stop or redirect if the foliation theorem requires an unavailable
Kupka/component condition, if a derivative estimate needs unsupported
subalgebra membership, if a finite map leaves its projective degree loss
uncontrolled, or if the output merely recovers the existing degree budget.
Do not append local singularity classifications, affine coordinate-pair
lists or adjacent target repairs. For existence, one actual construction
can suffice; for nonexistence, any restricted conclusion still needs a
justified route to arbitrary pairs. C being STCI remains a live possibility.

The fresh [independent audit](2026-10-31-foliation-affine-selection-audit.md)
reconstructs the deductions and challenges this allocation. It added the
exact finite-map control, checked the primary source hypotheses and
confirmed that an informative unproved mechanism remains eligible for
exploration. No unresolved material correction remains. The two producers
and reviewer completed their bounded tasks. No canonical status is changed,
and no new technical round has begun.

## 11. Constructive selection: finite pullbacks and controlled bundle degeneration

The next selection deliberately sought a source producing both equations
together, and a published operation allowing bundle-map degeneration away
from a chosen section. Two fresh `gpt-6-astra/xhigh` workers checked those
distinct mechanisms and their primary literature. No map-degree search,
monad enumeration or new ribbon classification was started.

### A finite-pullback source closes by a general lifting principle

A finite map `Phi:P3 -> P3` with sole reduced inverse image of the twisted
cubic equal to C0 would pull back its known (2,3) pair to a genuine STCI
pair (2d,3d). Unlike ordinary Cremona transport, this map could create
transverse thickness. Poonen's extension theorem supplies highly polarized
ambient extensions of reduced curve maps, but no inverse-support control.

The selection led to a new precise geometric implication, recorded in
[the proof note](2026-10-31-finite-pullback-lifting.md). The full inverse
scheme W would inherit the twisted cubic's pulled-back resolution. Thus
all its ambient-twist sections lift and it has no equations of degree d.
The degree relation `3e=4d` forces 3|d. On a rational thickening, Pic(W)
has no 3-torsion in characteristic different from three. Consequently
the pencil giving `W -> T = P1` must be `O_W(d/3)`. Its two sections
lift to ambient forms A,B, and the absence of degree-d correction terms
forces all four coordinates of Phi to be their cubic monomials. The
ambient map then collapses into the twisted cubic, a contradiction.

The bounded verification and its stop rule were reported before a fresh
independent reviewer reconstructed it. It excludes the entire proposed
finite-pullback source, with no degree bound or transverse-type assumption.
The underlying lemma separates four actual inputs: torsion-free choice of
the required polarization root, scalar global units, lifting of its
sections, and absence of ambient correction sections. For a rational
normal curve of degree N in PN, the same proof applies when N divides d
and is invertible in the field; a smooth rational reduced inverse curve
of degree coprime to N forces that divisibility.

**Effect on the full question:** this is a construction-source exclusion
and reusable global lifting principle, not an arbitrary-STCI obstruction.
It even holds in characteristic two, where C0 has the inherited (4,4)
STCI pair. This proves that the source is nonexhaustive. The line target
used to encode a pair of equations has degree-d correction equations and
does not satisfy the lemma. No claim of publication novelty is made.

### Controlled degeneration exists, but does not yet give a split target

[Forster–Wolffhardt, Theorem 1.5](https://www.math.lmu.de/~forster/eprints/zeroschemes.pdf)
provides a substantive affine mechanism: when det(E) is trivial on the
zero scheme of s, the identity `psi(s)+lambda*h=1` controls a map
`Phi=psi tensor psi+i(lambda):E -> E-dual`, with determinant lambda².
The transformed section has exactly the same zero scheme, including
where the map loses rank. Thus degeneracy away from the section can be
controlled by an actual identity; the earlier uniform bundle-splitting
restriction does not disprove this principle.

Its target, however, is E-dual. If its determinant premise were imposed
on P3 with support C0, restriction forces `det E=O` and E-dual is already
isomorphic to E. The theorem is affine; a projective use additionally
needs its global input sections and identity. Neither that operation nor
the inspected monad/symmetric-power descriptions supplies the split
rank-two target. Ferrand's projective supported double and bundle section
already exist by the theorem in Szpiro, Chapter 4, §3; their existence is
not the missing input and does not justify another ribbon classification.

**Recommendation and stopping conditions:** the finite-twisted-cubic
source is now closed by the proof, so stop it in all degrees. Do not
replace it automatically by another target. Retain the general lifting
lemma for sources that actually meet its hypotheses. Stop the bare
Forster–Wolffhardt transplant: a renewed bundle construction needs a
specified operation into two line bundles and an independent identity or
extension mechanism controlling its zero support. This may be an
unproved mechanism proposed for a bounded test; success need not be known
in advance. Neither result justifies treating C0 as non-STCI. No next
technical campaign is selected by these findings.

The fresh `gpt-6.1-sol/high` [audit](2026-10-31-finite-pullback-lifting-audit.md)
covers the preserved lifting proof, its characteristic/generalization
claims, Poonen/Jamet source scopes and the displayed Forster–Wolffhardt
deduction. It verified the actual assessment and resolved two wording
clarifications about scheme-theoretic factorization and smooth rational
support. No material correction remains. Ferrand's proof and the monad
literature were not independently re-audited by this reviewer. Both source
workers and the reviewer completed their bounded tasks. No numerical
computation or canonical promotion was performed.

## 12. Arbitrary-pair roots and the limits of a residual-budget interpretation

The user's subsequent clarification reiterates the purpose of the earlier
normal, jet, spectral-sequence and asymptotic work: start with actual proper
intersections containing C, compare multiplicity and singular/attachment
behavior with the global budgets, and investigate both absorption of R
onto C and a positive lower bound on R. Those are useful broader questions.
A local defect is not automatically a residual cost, and a numerical
budget need not be strict. The root mechanism below was assessed against
that distinction rather than adopted as a new compulsory lane.

The [all-pair root investigation](2026-10-31-polarization-root-budget.md)
extends the previous Picard argument to any hypothetical supported CI Z.
Its polarization H has a unique fourth-root isomorphism class L, with
`L|C=O_P1(1)`. The full, possibly Z-graded section algebra A is finite
over its fourth Veronese `B=S/(F,G)`, is Cohen–Macaulay, and has
`omega_A=A(4(a+b-4))`. The proof uses saturated section modules and the
explicit finite-group trace pairing, not a normal-domain extension theorem.

Its reduction has normalization k[s,t] with finite vertex defect D.
The invariant part of D consists exactly of the missing degree-four
coordinate s²t². Multiplication further forces the image of H0(L) on C
to be zero or one of the two marked coordinate lines, and the image of
H0(L²) to have dimension at most one. These are constraints on lifted
linear series; no nonzero section is forced. They do not contradict the
known first-neighborhood obstruction or produce a new defining pair.

The existing twisted-cubic (2,3) CI supplies a decisive scope control.
Its canonical ribbon has a unique cubic polarization root M with
`h0(M)=0` and `h0(M²)=1`. Its root algebra is Gorenstein with nonnormal
reduction, whose normalization defect is supported in degrees one and
two. Thus even global CI duality does not force root sections or normal
reduction. Its invariant defect is zero: this control does not construct
the quartic's nonzero invariant defect or settle its realizability.

**Relation to the residual budget:** D is a defect at the affine cone
vertex. Degree by degree it is the image of the obstruction map into
`H1(J tensor L^n)`, so it records section extension through nilpotents.
It is not a term in `ab=4m+deg R`. For the C-primary component of a
proper intersection with R present, the full section ring need not equal
the embedded coordinate ring, and the inherited CI adjunction twist is
not automatic. A comparison with actual attachment/duality data is needed
before this package can bound R or guide an absorption construction.
No such comparison has been obtained in this test. The R=0 control shows
why a generic claim that every vertex defect spills into R would be false,
while leaving the quartic-specific invariant defect unresolved.

**Recommendation and stopping conditions:** preserve the structural
package and stop the bare root mechanism. No cover, semigroup or ribbon
classification is assigned. Reopen only for a specified theorem constraining
the invariant defect together with its nilpotent extension, an actual
construction of the required two-relation Veronese, or a justified comparison
with the residual attachment budget. Merely naming one of these missing
conditions is not a selected method. A concrete unproved mechanism can
be tested, but stop when it only recovers root existence, Gorensteinness,
the fixed missing coordinate or a known section obstruction. Existence
remains live; no unrestricted exclusion or positive residual floor follows.

A fresh `gpt-6.1-sol/high` reviewer independently checked the deductions
and control, repaired the trace-extension justification, and caught an
incorrect affinization description: the affine reduced root model retains
D, whereas affinizing its puncture removes D. The preserved note now
distinguishes these operations. The [completed artifact audit](2026-10-31-polarization-root-budget-audit.md)
covers the corrected statement, its boundary-map interpretation, and this
recommendation; no material finding remains unresolved within that scope.
The source/retrieval workers completed their bounded assignments; no
numerical computation or canonical promotion was performed.

## 13. Normal-order extraction and a uniform contact requirement

The user's pointwise normal-order proposal leads back to an existing
intrinsic construction, not a need for new local classifications. The
[October 26 filtration note](2026-10-26-normal-torsion-spectral-genus-budget.md)
already associates a saturation-defect divisor to every degree of the
full initial ideal. Its ordinary torsion and saturated-divisor accounts
are equivalent under the stated curvilinear hypotheses. They must not
be counted as separate costs. For a single generically nonzero symbol,
the common coefficient zeros also define a divisor; an identically zero
symbol calls for a higher generic order, rather than a Cartier zero divisor.
Fiberwise coefficient vanishing and stalk normal order remain distinct.

The [new extraction, §§8–9](2026-10-28-residual-degree-blowup-bounds.md)
places these divisors beside the full-primary genus and attachment
identities and draws a degree-independent consequence of the **inherited**
actual-pair graph inequality. If a supported pair has generic multiplicity
m and exact chosen-equation orders r,s, then

\[
\frac{m-rs}{m}\ge\frac{16\sqrt{15}-30}{49}\simeq0.6524027.
\]

The numerator is the horizontal exceptional contact remaining after the
first blowup. Thus a successful construction needs substantial repeated
normal contact; a transverse initial intersection cannot suffice. The
constant's reciprocal appeared earlier for a different conditional
relation-order ratio. The contribution here is its uniform actual-pair
interpretation, not a new basic inequality or a publication-novel constant.
For a general proper pair, the same extraction gives a residual-fraction
bound when its stated right side is positive.

**Effect on strategy:** this supplies concrete asymptotic search guidance
of the kind the user intended. It also identifies a limitation: the
degree budget sees generic contact, while point defects and attachment
enter the constant term of the Hilbert polynomial. The full normal
filtration and actual residual scheme are needed to compare those budgets.
Neither an Euler-characteristic identity nor the first graph's nef cone
supplies a universal upper limit on the surviving contact. The preceding
root-algebra defect likewise has no established conversion into residual
degree. These approaches now have useful objects and necessary conditions,
but no additional strictness theorem or global equation construction.

**Recommendation before another round:** retain the contact fraction and
intrinsic divisors as filters and measurements for an actual global
construction or a proposed all-pair comparison. Do not initiate another
local-type enumeration, a first-blowup numerical sweep, or a sequence of
root-algebra examples. Existence remains live: a specified mechanism that
creates the required contact and absorbs the full residual is worth a
bounded test even before its success is known. Nonexistence requires an
additional uniform restriction on actual pairs; a restricted obstruction
without an exhaustive reduction cannot supply it. No such new mechanism
is selected by this extraction alone.

**Stopping conditions:** stop a follow-up if it only recomputes the
inherited graph bound, renames a saturation defect, writes an equivalent
genus/attachment identity, or realizes formal contact without a specified
global lifting argument. Reopen for a concrete new geometric comparison
or construction and identify its first falsifiable implication before
assigning work. This is a continuing selection rule, not a requirement to
prove a conjectured mechanism before investigating it. The unrestricted
characteristic-zero STCI question remains open.

A fresh `gpt-6.1-sol/high` reviewer independently checked the numerical
extraction, normal-symbol distinctions and genus scope, and challenged
the stopping recommendation. Its artifact-review addendum is linked in
the [existing graph audit](2026-10-28-residual-degree-blowup-audit.md).
This bounded review reuses the previously reviewed graph theorem and
filtration identities; it does not rerun them or promote any result.

## 14. Prescribed ribbon absorption and the limit of automatic embedding lifts

The next selection compared a uniform positivity mechanism with an actual
component-coalescence construction. Both were checked against primary
literature before a technical experiment was chosen. Fresh isolated
`gpt-6-astra/xhigh` workers handled the two selections; a fresh
`gpt-6.1-sol/high` reviewer challenged their implications. The review
changed the constructive recommendation rather than merely endorsing it.

### Ambient Hilbert-scheme nef classes repeat the movement degree

For the existing full tropical family
`f:P1 -> Hilb^m(A2)_0`, let B be its finite-flat tautological algebra and
`e=deg B`. The [ABCH paper](https://arxiv.org/pdf/1203.0316), Theorem 2.4,
Proposition 3.1 and Corollary 3.2, identifies the ambient divisor classes
H and Delta/2 on `Hilb^m(P2)`, the Plücker class `D_k=kH-Delta/2`, and
the nef cone generated by H and `D_(m-1)`.

The actual family's support is fixed in A2, so `f*H=0`. Trivializing
O(k) on that affine chart identifies its pulled-back tautological bundle
with B. Thus `f*D_k=det B` as line bundles, and every ambient nef-class
inequality is just `beta*e>=0`. The [existing tropical proof](2026-10-31-tropical-descent.md)
already gives e>0. The boundary half-class has degree -e, which is
consistent because the family lies inside that boundary; its defining
section pulls back to zero, not an effective divisor of negative degree.
For small k this is a determinant-class identity, not a use of an
everywhere-defined Grassmannian map. The complex numerical theorem
transfers by descent and field extension to algebraically closed
characteristic-zero fields.

This is a uniform redundancy statement for **ambient nef divisors**,
not for every intrinsic punctual-Hilbert or equation-incidence condition.
No such extra condition was supplied. Stop this positivity application;
no chamber computation or punctual-type list is assigned.

### A genuine construction survives the independent challenge

[Drézet, Proposition 3.2.6 and Theorem 3.2.7(ii)](https://arxiv.org/html/1409.4175v3#S3.SS2)
gives a global maximal reducible deformation of a given ribbon when its
conormal is O_C(-Delta) for a reduced divisor of distinct points. The
general fiber consists of two smooth components meeting transversally.
The broader nonzero-section criterion in part (i) is local. The proof
also glues ample line bundles; a blanket claim that it has no polarization
data would be wrong.

The initial selection correctly noted that the theorem does not itself
prescribe this P3 embedding, but stopped too early. The reviewer showed
that line-bundle and section extension can fill that gap in a useful
range. The subsequent **marked embedding test**, with its recommendation
and stopping condition reported before work, proved a stronger general
criterion. Over a locally Noetherian base, for a proper flat
finite-presentation family containing a flat fixed C, the given central
embedding extends étale-locally while
fixing C if

\[
H^1(W,T_{\mathbf P^3}|_W\otimes I_{C/W})=0.
\]

The [preserved construction](2026-10-31-marked-absorption-deformations.md)
applies this first over the complex numbers to every given embedded ribbon on C0 with conormal
O_P1(-d), 0<=d<=6. The actual restricted tangent bundle is
`O(5)^2 + O(6)`, so the marked obstruction group vanishes. One component
of Drézet's deformation supplies the flat fixed mark after trivializing
its P1 family. The d=0 case uses an explicit split-ribbon deformation
instead of silently extending the positive-divisor hypothesis.
An explicit finite-presentation spreading argument transfers the existence
construction to arbitrary algebraically closed characteristic-zero fields;
this is separate from the stated field scope of Drézet's theorem.

Consequently the prescribed ribbon is a limit, in the fixed P3 and with
C0 fixed, of C0 together with a second rational quartic meeting it in d
points. Sufficiently large fixed twists and the existing actual-equation
lifting interface place this entire embedded family inside a proper
two-equation family. Its cycles are

\[
[Y_0]=2[C_0]+R_0,\qquad
[Y_t]=[C_0]+[C_t]+R_t,\qquad \deg R_0=\deg R_t=ab-8.
\]

Thus four units of the full residual degree relative to C0 are actually
absorbed. The prescribed ribbon and the d-point attachment of the two
quartics are retained scheme-theoretically. Extra residual attachment is
not prescribed, and full-primary extraction is not asserted flat.

Partial absorption was already proved in October 27. The gain here is
the **prescribed embedded ribbon** and the general marked-lifting method,
without assuming that a chosen global carrier is smooth along C. This
does not construct a degree-eight CI, an STCI endpoint, or an operation
that can be iterated until the residual disappears.
Increasing the equation twists guarantees containment but leaves only
four units absorbed in this operation while ab grows. It therefore gives
no asymptotic route to a vanishing residual fraction by twisting alone.

### The automatic criterion has a uniform endpoint boundary

For every hypothetical supported CI Z of degrees a,b>=5, put
`c=a+b-4` and `J=I_(C0/Z)`. Euler, CI duality and the coordinate-ring
generation in degree one give the exact formula

\[
h^1(T_{\mathbf P^3}|_Z\otimes J)
=19+ab\left(\frac32(a+b-4)-4\right)>0.
\]

This is a space in which marked-embedding obstructions can lie. It is
**not** a nonzero obstruction class, nor proof that a particular
deformation fails. Its concrete implication is that the sufficient
vanishing argument that produces the ribbons cannot automatically
produce any supported CI endpoint. Absorption may still succeed by
choosing deformation directions whose actual obstruction classes vanish.

**Recommendation and stopping conditions:** retain this positive
construction and its general lifting lemma. Stop at the proved boundary;
do not replace it by a d=7 ribbon classification or an unquantified
iteration through multiplicities. A justified next construction needs
a specified compatible deformation/equation family and a mechanism
controlling its actual classes and residual support. Merely counting
the nonzero obstruction space supplies neither existence nor nonexistence.
The unrestricted characteristic-zero question remains open. The
[independent audit](2026-10-31-marked-absorption-deformations-audit.md)
records the source scopes, marked lift, actual-pair application, endpoint
calculation and the corrected strategy rationale; no canonical promotion.

## 15. Obstruction detectors, global coefficient costs, and compatibility

The user's subsequent geometric description distinguishes an abstract P1,
its containment in surfaces, compatible embeddings of those surfaces in
P3, and the requirement that their full images intersect only along C.
These are useful distinctions in what a result actually establishes,
not a compulsory sequence of investigations. The preceding construction
retains the embedded ribbon and actual surfaces containing it; the
remaining residual shows exactly which compatibility it does not supply.

Two fresh `gpt-6-astra/xhigh` workers checked mechanisms aimed at the
remaining obstruction classes and repeated normal contact. A fresh
`gpt-6.1-sol/high` reviewer challenged both selections. No local-type,
degree or valuation-chamber enumeration was started.

### Semiregularity: the supported target also vanishes

[Iacono–Manetti](https://arxiv.org/pdf/1112.0425), under their regular-zero-locus
setup, annihilate actual embedded Hilbert obstructions under the semiregularity map, with a
stronger supported target in the proof of Theorem 11.1. The ordinary
ambient target \(H^3(P^3,\Omega^1)\) is zero. The perfect-complex and
proper-morphism extensions in [Pridham](https://webhomes.maths.ed.ac.uk/~jpridham/semireg2.pdf)
have the same limitation for their ordinary ambient trace components.
This says nothing by itself about the values of the original classes.

The supported refinement was initially left open. A subsequently
reported bounded test proves a stronger uniform statement in
[the marked-deformation note, §6](2026-10-31-marked-absorption-deformations.md#6-supported-semiregularity-also-has-zero-target-for-smooth-projective-curves):
for every smooth projective curve \(C\subset P^n\), \(n\ge2\),

\[
H_C^n(P^n,\Omega^{n-2})=
\mathbb H_C^{2n-2}(P^n,\Omega^{<n-1})=0.
\]

The normal filtration makes every candidate ambient two-form section
on every finite neighborhood of C negative; coherent duality proves the
displayed vanishings. No rationality, balanced-normal-bundle or equation
hypothesis is needed. The vanishing holds in every characteristic;
the cited obstruction-annihilation theorem retains its characteristic-zero
scope. All thickenings have the same support groups.

Thus this **particular supported detector**, as well as the ambient one,
supplies no extra restriction or construction. It does not make every
possible marked obstruction comparison vacuous. Embedded deformations
of an existing global CI, even while retaining fixed C, are already
unobstructed by lifting its equations. Realizing an independently
prescribed abstract marked deformation is a different relative problem.
Neither that equation freedom nor the zero semiregularity target cancels
the marked classes automatically.

### Valuation completeness is not a global pole estimate

[Herrera Govantes–Mahboub–Olalla–Spivakovsky, Theorem 6.2 and Remark 3.34](https://arxiv.org/pdf/1406.0657)
provide complete key-polynomial expansions for a fixed valuation. Their
coefficients range over the valued field, and integral rescaling at one
place can introduce poles elsewhere. The theorem's ordinal bound on the
sequence is not a simultaneous divisor-height bound in terms of the
original homogeneous degrees a,b.

[Corvaja–Zannier, Theorems 1.1 and 1.1*](https://www.numdam.org/article/BSMF_2011__139_4_437_0.pdf)
do give independent global information for an actual reduced-curve
relation \(z=1+u+v\): they bound distinct zeros outside S and, with
controlled support, bound height. S contains both zeros and poles of u,v.
The theorem has independent and multiplicatively dependent branches;
independence is not an absolute prerequisite. A small controlled ratio
of boundary complexity to height is one sufficient way to obtain a
strong bound, while absolute support bounds can also be useful.

No checked theorem supplies such coefficient/support control for an
arbitrary pair's successive normal cancellations. Enlarging S to include
all newly introduced zeros and poles records their cost but does not bound
it. Nor are the counted points automatically residual curves downstairs:
a separate geometric comparison with actual normal contact or residual
support is required. The [earlier direct-coordinate test, §2B](#b-two-marked-fibers-and-function-field-abc)
and the October 21/26 normal-lattice and genus accounts already identify
these missing inputs. Changing from coordinate functions to cancellation
coefficients does not supply them.

**Recommendation and stopping conditions:** retain the positive prescribed
absorption result, and stop these bare semiregularity and valuation-height
applications. Do not use the nonzero marked obstruction space as a
contradiction, or replace actual obstruction classes by their traces.
Reopen only for a specified relative detector with information beyond the
zero targets, or an actual coefficient relation with independent support
control and a proved normal-contact/residual consequence. Such a mechanism
may be unproved when selected for a bounded test; merely naming the missing
comparison is not a method. No replacement technical campaign is selected
by this assessment. The unrestricted characteristic-zero STCI question
remains open.

The [audit continuation](2026-10-31-marked-absorption-deformations-audit.md)
covers the general supported-vanishing proof, source scopes, the dependent
height branch and these stopping decisions. The initial suggestion that
the specified supported target might remain useful is superseded by the
proved vanishing; other relative or marked complexes remain unexamined.

## 16. Pinching, abstract supported sections, and the marked projective image

This selection returns to existence, allowing several inverse branches or
a cover of C0 on a carrier's normalization. The positive full-conductor
relation cone is already part of [R-0003](../results/fixed_carrier_conductor_criterion.md).
Cancellation between different divisor directions, including cancellation
of characteristic-zero logarithmic defects, is explicitly recorded in
[the October 27 conductor interface, §4](2026-10-27-absorption-characteristic-conductor-interface.md#4-a-different-positive-characteristic-replacement-cancel-defects).
It is not a new mechanism supplied by this selection. The singleton
classification [R-0002](../results/cartier_singleton_lift.md) does not cover
these inverse images.

### What pinching really supplies

[Ferrand, Theorems 2.2(iv), 5.4 and §6](https://www.numdam.org/article/BSMF_2003__131_4_553_0.pdf)
supplies scheme pushouts under the stated affine-neighborhood hypotheses
and gluing of invertible sheaves. Projective inputs alone do not ensure
projectivity: §6.2 gives a proper nonprojective pinch. A compatible ample
polarization, descending along the finite surjection, removes that issue.
The [Temkin–Tyomkin generalization](https://arxiv.org/pdf/1305.6014), Theorem
6.2.1(ii)(b) and Corollary 6.3.3 in the author version, strengthens pushout
existence and flat-module descent, not the prescribed ambient embedding.

There is a useful positive sufficiency statement. Take a polarized
Ferrand pushout S of an integral normal projective surface T along a closed scheme
D mapping finitely onto E. Assume T→S is finite surjective,
E has reduced support C≅P1, the full reduced inverse image of C is
Γ=⋃Γ_i=supp(D), and an invertible sheaf L on S pulls back to H on T.
Suppose a section q of H^b has divisor Σn_iΓ_i, with every n_i>0.
Then some q^N lies in I_D H^(bN): locally its equation is in the radical
of I_D, and a finite cover gives a common exponent. The compatible pair
(q^N,0 on E) descends to a section of L^(bN) whose zero support is exactly
C, since this can be checked after the finite surjection. There is no
off-C conductor condition in this setup.

Thus pinching is a genuine operation constructing abstract surfaces and
supported sections; it is not merely the fixed-carrier criterion restated.
The preceding deduction is the elementary supported-pinching instance
of that criterion, not a new theorem or an actual C0 construction in P3.
It retains the full scheme D, not just its reduced curve.

### The unresolved realization, with two possible routes

Write g:D→E and let M=L|E, with gluing α:H|D≅g* M. The actual degree-one
sections are the equalizer

    H0(S,L) = ker[H0(T,H) ⊕ H0(E,M) → H0(D,g* M)],
    (u,v) ↦ α(u|D) − g*v.

To embed this S itself in P3, four compatible sections must separate the
whole scheme and restrict on C to the marked span
⟨s^4,s^3t,st^3,t^4⟩. In particular L|C must be O_P1(4).
Taking a high tensor power to obtain an embedding into some projective
space does not retain this marked polarization. If S itself were an
integral hypersurface of degree at least two with L=O_S(1), the hypersurface
sequence gives h0(S,L)=4. This is an inexpensive necessary check for that
realization; it is not an obstruction to all projections or all carriers.

Alternatively, a four-section series can give a finite birational P3
image X different from the designed pushout S. This remains a possible
construction. One must then check the full inverse support over C0 and
descent through the actual, possibly larger conductor of T→X. The section
already descending to S need not descend to X. Insisting that the original
pushout embed would prematurely discard this alternative.

[Hartshorne–Polini, Propositions 7.1–7.3 and Corollary 7.4](https://arxiv.org/html/1301.3222#S7)
do not exclude the remaining multibranch setup. Their STCI-to-local-APic
argument assumes the smooth curve meets the singular locus only finitely;
it cannot be applied when C is contained in the conductor. The abbreviated
singleton-fiber language in the October 27 notes must be read with this
hypothesis. No broader exclusion is inferred here.

### Recommendation, stopping conditions, and independent review

Do not start a pinching-type, covering-degree or conductor-phase
classification from these general theorems alone. The selection found
no concrete marked four-section construction to test. Reopen for specified
pinching/projection data with a plausible mechanism for the prescribed
series and either direct embedding or descent through its actual image.
Success need not be proved before selecting a bounded experiment. Its
questions should be whether those sections give the required image,
whether full inverse support is retained, and whether the supported
section descends there. Stop a chosen experiment when its mechanism fails;
do not automatically enumerate adjacent degrees or local types.

From the existence side, one successful candidate can settle STCI and
the supported-pinching operation remains available. From the nonexistence
side, failure of a pinching model excludes only that source, without an
exhaustive reduction of arbitrary defining pairs. No new arbitrary-pair
constraint, carrier, mate or canonical promotion is claimed by this pass.

Two fresh workers performed bounded read-only selection: an
`gpt-6-astra/xhigh` construction scout and a `gpt-6.1-sol/high` primary-source
scout. A separate fresh `gpt-6.1-sol/high` reviewer independently challenged
the recommendation and checked the supported-power descent argument.
The review corrected two overly restrictive readings: pinching supplies
real abstract constructive input, and direct closed immersion of the
designed pinch is sufficient rather than necessary. The recommendation
above incorporates both corrections. All three assignments stop here;
no further technical campaign is selected. The unrestricted
characteristic-zero STCI question remains open.

Final wording review: **PASS** for this section, its FRONTIER and
literature-ledger summaries, and the two linked October 27 scope
clarifications. The Temkin–Tyomkin theorem-number attribution was checked
by the primary-source scout, not separately rechecked by the challenge
reviewer. This is a reviewed selection assessment, not a promoted result.

## 17. A concrete elementary modification and the end of its bounded test

The next selection compared liaison/elementary modifications with
mixed-characteristic lifting. Fresh `gpt-6-astra/xhigh` workers handled
the two source checks. A fresh `gpt-6.1-sol/high` reviewer challenged their
nonselection recommendations and found a concrete construction input.
Another fresh reviewer at the same setting challenged that candidate
before its bounded test, then independently reconstructed the proof.

### Construction input, result, and geometric extraction

The [quadric modification](2026-10-31-quadric-modification.md) constructs
an actual rank-two bundle E with c1=10,c2=28 inside O(6)². The section
defining 2C on Q lifts to E, and its complete lift space gives

    F=c0²+qH4,   G=c2²+qK4,

with both quartic corrections arbitrary. A section of E supported on C
would have cycle 7C; its image would be an actual CI with cycle 9C.
This supplied a precise existence test. Requiring a completed supported
section before selection would have discarded a legitimate construction
source. The existing fixed mixed-weight carrier and common-boundary
exclusions do not cover this full space.

The reported first-cancellation test now closes the entire source.
Cancellation beyond multiplicity two requires H|C=s^12T4 and
K|C=t^12T4. For nonzero T4, the next normal correction must supply
4s^11t^11, while all available corrections lie in

    s^12 H0(O_P1(10)) + t^12 H0(O_P1(10)) ⊂ H0(O_P1(22)).

The required section has order eleven at both marked endpoints; each
allowed summand has order at least twelve at one endpoint. Its middle
coefficient cannot be supplied. The generic multiplicity is exactly
three and residual degree is 24. If T4=0, both generic normal orders are
two, and the inherited actual-cycle inequality gives residual degree
at least four. Failed first cancellation gives multiplicity two.
Thus every proper pair in the whole source has residual degree at least
four. The [audit](2026-10-31-quadric-modification-audit.md) records the
exhaustive alternatives and independently checked hypotheses.

This adds a positive global bundle construction and a proved limitation
of its full section space. Its reusable geometric content is the
comparison between a required normal correction and the restriction
image of actual ambient sections; the endpoint degree gap makes this
test decisive. It is not an exclusion of arbitrary sextic pairs or an
all-degree elementary-modification theorem. No larger-power sequence is
selected. Such a continuation would require a new mechanism, not the
mere existence of adjacent cases.

### Arithmetic comparison and precise stopping conditions

The arithmetic check retrieved the existing [full coefficient incidence,
§2](2026-10-28-stci-search-logic-audit.md), rather than creating a duplicate
Hilbert-scheme reformulation. For a known characteristic-p point z of
that finite-type proper supported-pair incidence, a characteristic-zero
DVR trait through z, allowing residue extension and ramification, exists
exactly when p is not nilpotent in its local ring. This is the standard
closure-to-trait application of [Stacks, Lemma 32.15.1](https://stacks.math.columbia.edu/tag/0CM1),
not a new operation or a computed horizontal component. A compatible
global embedded flat system over one complete mixed-characteristic DVR,
retaining the support ideal containments and CI presentation, algebraizes
by [Stacks, Lemma 76.43.1](https://stacks.math.columbia.edu/tag/0A00).
The compatible supported lifts themselves remain missing.

An unramified W2 failure does not exclude ramified lifts: x²=p has a
ramified lift of x=0 but none over Z/p². The
[higher-degree (16,p) examples](2026-10-29-arithmetic-beyond-binomial.md)
therefore remain unresolved under simultaneous deformation of both
equations; their fixed-carrier jet obstruction cannot be substituted for
a statement about the full incidence. The checked
[Granger–Schulze deformation theorem](https://arxiv.org/html/1804.01316)
works with analytic curve germs and equicharacteristic semigroup control,
and supplies no projective mixed-characteristic support mechanism here.

**Recommendation:** close the proved quadric source test and retain the
arithmetic horizontal-component question as an unselected interface.
Reopen arithmetic work for an actual support-preserving lifting operation
or a structural calculation on the full simultaneous-pair incidence;
do not freeze the known carrier or start prime enumeration. One successful
lift or geometric source can settle existence. Excluding chosen sources
or special-fiber points cannot settle nonexistence without an exhaustive
reduction. The construction and its source exclusion have independent
proof review; the arithmetic scope statements have independent strategy
review and no claimed new calculation. All bounded assignments are
complete, and unrestricted characteristic-zero STCI remains open.

Final assessment review: **PASS** by
`modification_lifting_strategy_review`, reusing the separate
`quadric_modification_gate_review` proof audit for the completed source
test. The reviewed final wording retains all correction quartics,
the positive bundle construction, the ramification qualifications and
the absence of an automatic next-degree campaign.

## 18. Intrinsic normal obstruction, finite-thickening Picard groups, and punctual extension

The next selection asked whether the preceding global correction gap
could constrain arbitrary defining pairs. A fresh `gpt-6-astra/xhigh`
worker checked the intrinsic Picard/Atiyah interpretation and the
existing multiple-quadric matrix counterexample. A fresh
`gpt-6.1-sol/high` reviewer independently reconstructed the resulting
uniform theorem and its characteristic comparison. A separate
`gpt-6-luna/high` retrieval worker checked only the status and scopes of
the six untracked quintic/nonnormal notes in the shared checkout; their
different carrier sources were not incorporated or modified.

The [new note](2026-10-31-punctual-quadric-lifting.md) and its
[audit](2026-10-31-punctual-quadric-lifting-audit.md) establish three
connected statements, by standard lifting methods with explicit proofs:

1. For every finite n≥2, Pic(nQ)→Pic(Q) is injective. Its
   characteristic-zero image is exactly the diagonal. In characteristic
   p>0, the image consists of O_Q(a,b) with p^e dividing a−b, where p^e
   is the least p-power at least n. Frobenius supplies the extensions
   through that order; a nonzero Frobenius image of the first Čech
   obstruction prevents the next order. This is one uniform statement,
   not a prime or thickness enumeration.
2. In every characteristic, every ruling class on Q admits a rank-one
   MCM extension to every finite nQ that is invertible away from any
   one prescribed point. Coherent extension and double dual supply
   the actual sheaf. A class outside the Picard image forces a nonfree
   point there. The statement bounds the support by one point, not its
   scheme length, number of generators or other defect cost.
3. The sextic normal-correction quotient maps explicitly through its
   Koszul boundary and the adjunction boundary for C⊂Q to H2(K_Q).
   Its class 4s^11t^11 maps to ±4γ, agreeing up to fixed sign with
   the obstruction to lifting O_Q(2,6). This proves a comparison of
   the displayed classes; it does not identify the two realization
   problems or supply an arbitrary-pair comparison theorem.

The relevant literature input is the [square-zero Picard sequence](https://stacks.math.columbia.edu/tag/0C6Q)
and the [Atiyah/conormal obstruction interpretation, Proposition 2.10](https://arxiv.org/pdf/1007.1671).
The direct Čech computation supplies the arbitrary-characteristic
normalization. The punctured cohomology calculation, coherent extension
and local depth argument are written out in the source; no blanket
normal-surface reflexivity claim is applied to a nonreduced scheme.

**What this changes.** The preceding source exclusion has an explicit
intrinsic interpretation. Its straightforward extension using only
Picard imbalance is now known to be inadequate: one point on C can
support a nonfree MCM extension with any prescribed ruling imbalance.
This is positive geometric flexibility, not evidence that the STCI
equations exist. It also does not invalidate the possible use of a
quantitative bound on the amount of defect allowed by those equations.

For an actual supported pair, the known identity q^N=AF+BG supplies
a two-by-two homogeneous presentation with determinant q^N, retaining
the actual equation column. The [earlier matrix example](2026-10-31-simultaneous-equation-geometry.md)
already shows why its layers need not be line bundles. The present
uniform extension has arbitrary reduced ruling class and a prescribed
single nonfree point, but supplies neither that example's global ACM
two-generator presentation nor the required equation column supported
exactly on C. These are the substantive remaining conditions. The
global extensions for different n are not asserted compatible, despite
compatible line bundles on the punctured thickenings.

**Recommendation and stopping conditions:** stop the bare Picard
nonlifting argument here. A justified continuation needs a specified
consequence of the actual presentation/normal action/column that bounds
or constructs its permitted defect. Merely locating defects on C, or at
the marked endpoints, is insufficient; merely calling an MCM sheaf ACM
would be a substantive error. No classification of sheaves or local
defect types is selected. From the existence side the theorem supplies
flexible local Cohen–Macaulay objects; from the nonexistence side it
locates the missing global presentation constraint. Neither establishes
an unrestricted conclusion. The independently reviewed work remains
provisional, with no canonical promotion.

## 19. Actual matrix columns, normal-action defects, and the limit of operation invariants

Two fresh `gpt-6-astra/xhigh` scouts examined the actual presentation
constraint left by §18: one studied the all-order normal q-action, the
other constructive determinant-preserving operations. A fresh
`gpt-6.1-sol/high` reviewer independently reconstructed their deductions
and challenged their recommendation. The bounded sources and review are
preserved in the [presentation-boundary note](2026-10-31-quadric-presentation-boundary.md)
and its [audit](2026-10-31-quadric-presentation-boundary-audit.md).
The assignments are closed; none is retained for a larger-N campaign.

**Actual gain from the first investigation.** For a hypothetical
supported pair and least N with q^N∈(F,G), its determinant presentation
has cokernel M=I_{Y,NQ}. The reduced equation column has common divisor
rC and a finite residual base scheme T supported on C. The calculation
identifies the actual inclusion of q^(N−1)M in Ann_M(q), and their
quotient is a line twist of O_Q/(c^e I_T), with 0≤e≤r−1. Thus normal
action can fail along an entire multiple eC as well as at points.
This is an all-order description of a specific geometric defect, not
an assumption that all layers are line bundles or all defects punctual.
The finite length 2ab−4r(a+b)+6r² is the familiar quadric intersection
budget; the new dictionary does not strengthen that budget or compare
the defect with a residual curve outside C.

**Actual gain and correction from the second.** A column from O(−a)
in a determinant-q^N matrix whose saturated image on Q is O(α,β)
requires the full equality (α+a,β+a)=(ν,3ν) to have divisor νC.
Integral q-pole transvections preserve that image line while every
intermediate reduction remains nonzero and generically rank one.
This excludes a specified operation sequence from the standard seeds.
It does not exclude arbitrary matrices or operations.

The reviewer supplied an explicit escape: the known endpoint-defect
matrix is transformed to qI, and a subsequent pole operation on q²I
gives q²I+v w, with v=(x0²,x2²)^t and w=(−x2²,x0²). Its determinant
is q⁴ and its saturated image O_Q(−2,0) has the required ruling
difference 2. Nevertheless its column class is (2,4), and its nonfree
locus contains an unwanted ruling line. The parent accepted this
challenge: merely changing the ruling difference is already possible
and is an inadequate next construction target. This single control
tests the scope of a proposed universal inference; it is not the start
of a seed classification.

The literature check retained the generation, linearity and distinct
support-factor hypotheses of the Kerner–Vinnikov determinant results.
Cohn's elementary-generation counterexample prevents an unsupported
exhaustiveness assumption. Neither literature input supplies a general
classification of the arbitrary-twist presentation at issue. The
proofs and exact primary-source links are in the source note.

**Reassessment of recent progress.** The full sextic correction-space
exclusion remains a real source theorem, with a residual floor, rather
than a theorem for all sextic equations. Its Picard interpretation
exposes a global obstruction, while the uniform punctual extension
theorem shows how nonfree sheaves can accommodate every ruling class.
The present work determines a defect of the actual equation ideal and
exhibits additional constructive flexibility. None of these establishes
that the required global two equations cannot exist. The earlier
prescribed-ribbon absorption is also genuine positive input: it moves
residual degree onto C, but its automatic embedding criterion does not
reach a supported endpoint. Nonzero obstruction spaces must still not
be mistaken for nonzero obstruction classes.

The user's compatibility hierarchy clarifies this distinction. An
abstract curve, an abstract curve in surfaces, compatible maps of those
surfaces, and their actual images with sole intersection C in P3 impose
different conditions. Every new result should identify which passage
it controls. That is an interpretive test, not an instruction to build
a theory at every level. Here the determinant presentation retains
actual ambient equations; forgetting its distinguished column or its
normal action loses precisely the compatibility still at issue.

**Recommendation before another round:** close these two bounded
investigations and stop further multiple-quadric bookkeeping as a
default direction. No new technical experiment is selected at this
checkpoint. On the existence side, an explicit operation on homogeneous
equations or a concrete embedded surface source would be useful only
if it adds control of the full boundary divisor and unwanted support;
a changed numerical class alone no longer qualifies. On the
nonexistence side, the missing input is a comparison valid for arbitrary
pairs between the retained normal-action defect and an actual global
capacity or positive residual degree. The displayed identities do not
provide it. Searching for a matrix with the final successful column is
equivalent to the original problem, not a new construction mechanism.

**Stopping conditions:** do not continue by enumerating thicknesses,
local modules, finite base schemes or neighboring seeds. Reopen only
when a proposed operation or comparison specifies additional input,
its applicability to the actual homogeneous equations, and what a
positive or negative outcome would establish. A construction can settle
existence within a special family; an exclusion needs an exhaustive
reduction to settle nonexistence. Neither direction receives priority
merely because it produces quicker local calculations. The continuing
assessment remains part of the process, and unrestricted
characteristic-zero STCI remains open.

Final-state independent review: **scoped PASS** by
`matrix_boundary_strategy_review`; see the companion audit, including
its final strategy-assessment disposition. No canonical promotion.

## 20. Ambient transport, a genuine projection source, and its conductor obstruction

After §19 closed the matrix round, two fresh `gpt-6-astra/xhigh`
scouts examined actual birational transport and global multiple-curve
constructions. A fresh `gpt-6.1-sol/high` reviewer challenged the
nonselection recommendations. The results and the subsequently selected
test are preserved in the [ambient-source note](2026-10-31-ambient-transport-and-projection.md)
and its [audit](2026-10-31-ambient-transport-and-projection-audit.md).

**Completed alternative-source findings.** The common blowup of C in
P3 and a conic in V5 cannot resolve a nontrivial Cremona map to P3,
in any degree: a birational hyperplane pullback is a nonample nef
integral divisor of cube one, and the two boundary rays H,L have
cubes one and five. Only the original contraction is possible. This
does not exclude further centers or different resolutions. A separate
explicit quadratic Cremona transport of the supported double twisted
cubic gives the actual cycle 2C+3ℓ+M after all surface factors are
removed. The tangent ℓ and endpoint secant M carry four residual
degree units. Its fixed cubic carrier is already excluded for every
mate, so this is a completed geometric control, not a new search.

The multiple-curve scout verified Singh–Walther's 2007 Question 3.6
for this exact quartic: finding even a same-radical Cohen–Macaulay
ideal is a substantive historical question, not an automatic step.
The source does not establish its current resolution status. ACM and
AG thickenings must remain distinct; in P3 an AG curve is a CI.
Canonical idealization increases cone embedding dimension, and an
isomorphic projection from a larger spanning projective space retains
too many linear sections to be ACM. These findings close the respective
automatic shortcuts, not all embedded canonical extensions or projections.

**Why an experiment was nevertheless selected.** The parent supplied
the classical actual three-quadric CI on the rational normal quartic
D in P4, with f=b²−az, g=c²−dz, h=z²−2bc+ad. The reviewer identified
scheme-changing projection as a real escape from the isomorphic-projection
objection. For every positive u,v, W_uv=V(h,f^u,g^v) is an actual AG
source, and forgetting z gives an actual scheme Y_uv with reduced
support exactly C. The construction itself supplies support. Its
source/image cokernel is S/K_uv up to twist, where K_uv is the
four-generator coefficient ideal of f^u,g^v modulo h. Irrelevant
torsion of this cokernel measures the failure of the image to be ACM.
This is additional constructible data, not a request for unknown final
equations.

The uniform positive-integer (u,v) test and stopping conditions were
reported before it began: test the whole source, allow an ACM result
to motivate an AG check, stop at a uniform failure or at case-dependent
work without a mechanism, and do not automatically add powers of h.
A new `gpt-6-astra/xhigh` worker carried out the uniform proof; a
different fresh `gpt-6.1-sol/high` reviewer reconstructed it independently.

**What the test actually proved.** Every projected scheme Y_uv fails
to be AG, hence fails to be a scheme-theoretic CI. For u≥2, its
conductor at p_a is generated by two elements, both necessary; for
v≥2, the same holds at p_d. If the image were Gorenstein, finite
birational duality with the Gorenstein source would force that conductor
to be invertible. The contradiction uses the full nonreduced source.
The remaining (1,1) image is an isomorphic projection with nonzero
global deficiency. No exponent enumeration or computer algebra was
needed. The uniform ACM question for other u,v remains open in this
investigation and is not needed for the direct CI-source exclusion.

**Geometric gain.** This source reaches actual thickenings on the
correct C in P3 with no residual component. The obstruction is instead
the failure of the endpoint conductor to be Cartier on the source.
It identifies a precise compatibility defect of the ambient projection,
and yields a reusable coefficient/conductor test for quadratic covers.
The source does not fail merely because its divisor class or reduced
support was wrong. In the smallest case the conductor obstruction is
absent but global section deficiency remains; these are separate conditions.

The proof also explains a characteristic distinction without a prime
search. It extends when p does not divide 2uv. For odd characteristic
and equal Frobenius powers u=v=n=p^e, the coefficient calculation instead
makes the projective conductor the Cartier ideal
r^((p^e−1)/2)O_W. The specific non-Cartier obstruction disappears.
Further finite duality then forces incompatible CI degrees: their product
would be 8n² and sum 5n. The odd-Frobenius images therefore also fail
AG/CI, while their local Gorenstein and ACM status remains unresolved.
In characteristic two, the same operation gives the known quartic CI
pair and its powers. Projection there is finite flat radicial of rank
two on the full schemes, although it is an isomorphism on the reduced
curves, so the birational conductor argument does not apply. This
comparison isolates two failures and a known success of one explicit
operation; it does not select a prime or exponent campaign.

**Recommendation and stopping conditions.** Close the entire selected
characteristic-zero two-parameter source as a direct construction of a CI scheme. Do not
continue with another exponent or a nearby projection center without a
new operation that controls the non-Cartier conductor and the global
section deficiency together. This theorem does not exclude a different
CI thickening with the same radical, including a thicker scheme that
contains Y_uv; it must not be phrased as saying that the support of
Y_uv is not STCI. A successful modified source could still settle
existence. No exhaustive reduction of arbitrary pairs to this source
is established, so the nonexistence program gains a source theorem
and a general diagnostic, not an unrestricted obstruction. The
characteristic-zero STCI question remains open.

The alternative-source proofs and the projection proof have distinct
independent review coverage in the companion audit. Final assessment
preservation received **scoped PASS** from
`projection_conductor_proof_review`, retaining the separate alternative-source
review. All bounded assignments are complete; no canonical promotion.

## 21. An arbitrary-pair boundary bound and automatic conjugate descent

The next bounded question was whether the preceding conductor test
adds anything for an **arbitrary** hypothetical supported CI, while
also checking the converse construction. Two fresh
`gpt-6-astra/xhigh` workers examined these distinct directions. A fresh
`gpt-6.1-sol/high` reviewer reconstructed the boundary and construction
identities; a different fresh `gpt-6-astra/xhigh` reviewer challenged
the parent's graded inequality and strategic recommendation. No nested
delegation or endpoint classification was used. The
[source](2026-10-31-quadratic-cover-boundary.md) and
[audit](2026-10-31-quadratic-cover-boundary-audit.md) preserve their scopes.

**What has genuinely been added.** Given any supported CI of degrees
alpha,beta, its full primary lift W in the fixed quadratic cover is
finite birational on the full nilpotent scheme. The conductor boundary
Delta downstairs is locally Gorenstein; upstairs it is exactly the
quadratic pullback of Delta. These statements do not require W to be
Gorenstein. The missing fifth coordinate gives the actual homogeneous
quotient B/A=T(-1), where T is the saturated coordinate ring of Delta.
Duality yields a canonical injection T(alpha+beta-5) into omega_T,
even when W is not ACM. Hence

\[
\ell\Delta\ge\alpha+\beta-3.
\]

The stronger retained statement compares the dimensions of ambient-form
restrictions in complementary degrees: H_Delta(n)+
H_Delta(alpha+beta-5-n) is at most length Delta. This is a classical
canonical-module constraint applied to the actual quadratic boundary,
not a new duality theory. It is absent from the focused inherited
notes inspected, with no claim of literature novelty. The attachment
length alpha beta+2 length Delta is instead a genus identity; it must
not be counted as an independent obstruction.

Geometrically, an actual two-equation scheme must compensate for the
extra linear section of its separated rational-normal-quartic branch
by a sufficiently large endpoint boundary, with the appropriate
graded canonical pairing. The defect is not merely optional bad
behavior: some defect is required for descent to four coordinates.
This concerns the user's last compatibility level, the actual
polarized images and their equations, rather than only abstract curves
or abstract Gorenstein gluings. The inequality applies in every
characteristic other than two, so it supplies no characteristic-zero
contradiction on its own.

**Which shortcuts are now closed.** The full primary lift of a local
supported CI in this exact cover can be non-Gorenstein: one explicit
length-three transverse control has defect four and two-dimensional
socle at the endpoint, while both conductor boundary algebras remain
Gorenstein. Thus the preceding Gorenstein-source theorem cannot be
extended to every pair by simply taking its primary lift. This single
control answers that logical question; no further local examples are
needed. A separate reduced-union control already has Cartier endpoint
attachment and local Gorensteinness but fails the global canonical
twist and linear-section condition. Local gluing alone is insufficient.

**Existence is simplified, not excluded.** For every pure W supported
on D in the quadratic cover, its union with its involutive conjugate
is automatically the full inverse image of its actual scheme image.
The union is AG if and only if the image is AG, and an AG curve in
P3 is a CI. Thus one constructed AG conjugate union would settle
existence; there is no independent descent obstacle after that.
Symmetrizing the already excluded power sources leaves their image
unchanged and does not supply such a construction.

Manolache's linkage extensions explain how non-Gorenstein branches
can glue to a Gorenstein union, but require actual embedded extension
maps and do not establish the global ACM property. Hartshorne's
anticanonical-divisor construction on a surface inside this smooth
quadric becomes the problem of finding the requisite supported
hypersurface section. The quadric G-liaison theorem does not preserve
the fixed branches or select the conjugate partner. None of these
checked theorems supplies a new embedded operation here. Their exact
primary propositions and limitations are preserved in the source.

**Recommendation and stopping conditions.** Preserve the all-pair
bound as a necessary construction constraint and stop the present
boundary investigation. The nonexistence direction has no independent
upper bound on the conductor and no comparison forcing positive
residual degree. The existence direction has an exact sufficient
construction, but no new operation producing it. Neither absence
counts as evidence that C is not STCI.

Do not begin a boundary-length, endpoint-type, multiplicity or degree
classification. Reopen for an independent geometric comparison that,
at residual degree zero, would force length Delta below alpha+beta-3
or violate the stronger restriction-function inequality; an
uncalibrated upper bound alone is insufficient. Alternatively, reopen
for a concrete embedded operation whose support, attachment and
global sections can be tested together with a prospect of an AG union.
A bounded test may fail; it must add an input beyond prescribing the
desired final object. If it yields only an attachment identity, a
rephrasing of global equations, or another local type with no relevant
comparison/construction, stop and reassess rather than expand the cases.
Report that input and stopping condition before the next experiment.
The unrestricted question remains open.

Both independent reviews returned **scoped PASS**. The graded reviewer
required the generalization to say A-module generation, rather than
mere algebra generation by one integral element; the final source
incorporates that correction. It also distinguishes ambient restriction
dimensions from all sections on the finite boundary. The final audit
records the source fingerprint and accepts this assessment's stopping
decision. All four bounded assignments are complete; no canonical
promotion and no further technical experiment selected.

## 22. Liaison comparison and a supported basic-double-link operation

The next selection asked for new input beyond §21, with two fresh
`gpt-6-astra/xhigh` workers: one compared global contact and liaison
constraints with the conductor inequality, and one sought an actual
embedded operation. A fresh `gpt-6.1-sol/high` reviewer challenged the
proposal and reconstructed its viability check. The
[source](2026-10-31-supported-linkage-selection.md) and
[audit](2026-10-31-supported-linkage-selection-audit.md) preserve the
proofs, literature hypotheses and stopping decision. No nested
delegation or parameter enumeration was used.

**The proposed second budget was dependent.** The branch's Rao
dimension in degree n is exactly delta−H_Delta(n−1)−
H_Delta(alpha+beta−4−n). Its nonnegativity and numerical conjugate-link
symmetry therefore repeat the previous canonical inequality. Actual
MCM presentations carry additional information, as the liaison
literature makes clear, but no incompatible constraint on that
presentation was supplied. Maximum-genus estimates have the wrong
direction for an upper conductor bound. Fixed support and multiplicity
alone also admit Ferrand ribbons of arbitrarily negative genus; those
particular ribbons are not ACM and are not claimed to have an AG
conjugate union. Jaffe's cited higher-blowup theorem assumes generic
smoothness of both defining surfaces and does not cover the retained
arbitrary normal orders. These distinctions prevent counting the same
descent defect as two independent constraints.

**A real construction was found and rejected uniformly during selection.**
Let P be the ideal of D in the smooth quadratic cover, with the known
supported regular sequence f,g. The basic double link

\[
I=(f^u)+g^vP,\qquad u,v>0,
\]

is an actual saturated ACM thickening of D, of multiplicity 1+2uv,
with the fixed ambient polarization. It is distinct from the prior
complete-intersection power source. Its exact presentation supplies
a decisive early test: for u≥2 its transverse generic ideal has three
minimal generators in a regular local ring of dimension two, so the
branch is generically non-Gorenstein. The conjugate branch meets it
only at endpoints and cannot repair that generic defect. For u=1 the
actual image retains the quartic norm of f, excluded by R-0001 and its
factor reduction. Thus the whole displayed operation fails, before
any proposed spinor/MCM degree-sum calculation. That speculative
degree-sum equality was not proved, used, or retained as a claim.

**The useful generalization prevents nearby case expansion.** More
generally, any homogeneous branch ideal containing G P for a nonzero
quadric G has the actual sextic q N(G) in its image ideal, where q is
the quadric through C. Every irreducible factor has degree at most
four. The CI degree divisibility and the accepted low-degree factor
exclusion show that a supported CI ideal cannot contain such a sextic.
Consequently every supported basic double link with quadratic multiplier
fails, regardless of the containing section's degree or coefficients.
This applies beyond ACM or Gorenstein branches. Higher-degree
multipliers and arbitrary finite chains remain outside the theorem.

**Assessment and stopping.** The construction genuinely supplies
supported ACM thickenings, showing that global ACMness by itself does
not repair generic canonical compatibility. The all-pair Rao identity
is a dependency check, not a new inequality. The multiplier theorem
is an exclusion of a broad specified operation, with no reduction
of arbitrary STCI pairs to it. None of these findings favors a
nonexistence conclusion for C.

No next technical experiment is selected. Do not respond by enumerating
higher multipliers, alternate containing sections or finite BDL chains.
A new operation must specify actual sections and explain how it could
retain a generic CI algebra while escaping the low-degree norm equation,
then permit a simultaneous attachment/section-ring test. A new
obstruction must retain information beyond the already determined
Rao dimensions and provide a calibrated comparison at R=0. An
unproved mechanism may be tested, but its new input and success/failure
consequences must be reported first. Stop when the proposed comparison
collapses to the existing identity or an operation fails a uniform
necessary condition. The unrestricted characteristic-zero question
remains open.

Independent reconstruction and final preservation review returned
**scoped PASS**, including the quadratic-multiplier generalization
and this selection decision. The audit identifies the final source
fingerprint and the inherited theorem evidence reused. Both scouts
and the reviewer have completed their bounded assignments. No
canonical promotion or further technical experiment is claimed.

## 23. The continuous section problem is solvable; algebraic realization remains

This selection stepped away from the quadratic-cover source. Two fresh
`gpt-6-astra/xhigh` scouts examined complement geometry and rational
plane-normalization descent independently. A fresh
`gpt-6-astra/xhigh` reviewer reconstructed the parent's global
topological consequence and challenged the complement recommendation;
a fresh `gpt-6.1-sol/high` reviewer checked the plane-descent selection.
No nested delegation or local classification was used. The
[complement source](2026-10-31-complement-sections-and-topology.md) and
[audit](2026-10-31-complement-sections-and-topology-audit.md) preserve
the proof and the distinct review scopes below.

**A global result, with a genuine generalization.** For every smooth
connected complex degree-d space curve C, not just the rational quartic,
every topological complex rank-two bundle E on P3 minus C has a
continuous nowhere-zero section exactly when c2(E) vanishes. The
Gysin sequence gives h² exact order d and zero integral cohomology
in degrees five, six and seven. The S3 sphere-bundle obstruction
sequence therefore has only its top-Chern obstruction: both possible
higher mod-two obstruction groups vanish. This checks torsion and
sufficiency, rather than merely observing a vanishing Euler class.
For E=O(a) plus O(b), the criterion is precisely d dividing ab.

Consequently every Bézout-admissible degree pair for C0 passes the
**entire classical continuous-section problem** for the bundle that
the equations would use. This is not an assertion that every
topological method involving carriers or singularities is exhausted.
It identifies one complete obstruction problem whose further
calculation cannot decide the remaining question.

Hartogs extension supplies the exact contrast: a holomorphic section
of the same bundle extends across C to P3 and is algebraic. For positive
degrees, a holomorphic nowhere-zero section on the complement is
therefore exactly a supported pair of homogeneous equations. The
unresolved passage is continuous-to-holomorphic realization, with no
additional analytic-to-algebraic issue for these particular sections.

**Why affine splitting does not supply that passage.** Successful
equations would define an algebraic extension with middle bundle
O(a) plus O(b), trivial subbundle and quotient O(a+b). That extension
must be nonsplit: all homomorphisms from the positive middle bundle
to O vanish by Hartogs. Its nonzero class, represented by 1/(FG) on
the actual two-open cover, is compatible with success and required
by it. The checked Asok–Bachmann–Hopkins theorem concerns a trivial
direct summand on a smooth affine corank-one base. The complement
is nonaffine, and a positive-rank Jouanolou replacement changes the
rank–dimension relation and still requires actual section descent.
Affine A1 representability also retains its source and target
hypotheses and compares homotopy classes, not individual maps.

**The constructive normalization alternative still lacks actual data.**
The known arithmetic degree-sixteen plane source and its larger tested
variation remain useful examples, but their exclusions do not cover
all four quartics extending the marked line series. R-0004 already
retains the full phase and infinitesimal-conductor criterion for power
descent. Ferrand pushouts and Kollár's finite relations do not furnish
the prescribed four sections or ensure that their actual image has
the designed conductor. Designing a reduced point pairing alone loses
the nilpotent gluing that the known source requires. No new plane
projection or mate was produced by the checked literature.

One elementary global limitation on an ambient-symmetry design is
worth retaining. If a birational map f:P2→P3 is given by degree-d
forms F_i, and a **single** nonidentity projective automorphism sigma
satisfies f(p)=f(sigma p) along a reduced divisor D, then deg D≤2d.
Indeed all crossminors F_i(F_j composed with sigma) minus
F_j(F_i composed with sigma) have degree 2d and vanish on D. If its
degree were larger, all would vanish identically; birationality would
then force sigma to be the identity. For quartics the bound is eight.
The full conductor class 51L counts multiplicity and does not imply
that its reduced degree exceeds eight. Components paired by distinct
automorphisms cannot have their degrees summed in this argument,
and a conductor deck map need not extend to P2. The local inertia/phase
check is a consequence within the existing phase criterion and does
not select a new conductor classification.

**Recommendation and stopping.** Retain the global continuous-section
criterion and its essential algebraic-extension distinction. Do not
start a classical Euler or secondary-section-obstruction calculation
for these bundles, since it has been completed uniformly. Do not
start a conductor-inertia or plane-symmetry classification: the
selection supplied limitations on a proposed design, not its missing
global four-section data. Neither conclusion favors nonexistence.

A future complement proposal must name a strict descent or realization
operation for the actual holomorphic/algebraic section, or an algebraic
obstruction retaining the relevant global data. A future normalization
proposal must supply actual sections or compatible pinching/projection
data with a mechanism for their full power descent. An unproved
mechanism may be tested; a reformulation alone does not justify a new
campaign. Report its added input and stopping conditions before
starting. No further technical experiment is selected here, and
unrestricted characteristic-zero STCI remains open.

Both independent reviews returned **scoped PASS**. The complement
review verifies the full obstruction calculation and the actual
holomorphic/algebraic predicates; the plane review verifies the
separate symmetry bound and its limited constructive implication.
The audit preserves distinct scopes and the source fingerprint.
All four bounded assignments are complete. No canonical promotion.

## 24. The primary algebraic Euler detector also sees only degree

This continuation asked whether the preceding continuous section could
be realized by an available analytic or algebraic construction, and
whether a refined algebraic characteristic class retains information
that the classical test lost. The two literature scouts had fresh
contexts: gpt-6-astra/xhigh for analytic realization and
gpt-6.1-sol/high for algebraic extensions and Euler classes. A fresh
gpt-6-astra/xhigh reviewer independently challenged the proposed
selection and reconstructed the proof. No nested delegation was used.

Before writing the new proof, the parent reported the reviewer's
recommended bounded test and stopping condition: compute the twisted
Chow–Witt comparison uniformly; close this detector if it repeats
degree divisibility, or identify its actual extra necessary condition
if it does not. No local classification or secondary tower was selected.
The [source](2026-10-31-algebraic-complement-obstructions.md) and
[audit](2026-10-31-algebraic-complement-obstructions-audit.md) preserve
the completed result and actual-state review.

**Genuine gain and generalization.** For every smooth connected degree-d
curve C in P3 over an algebraically closed field of characteristic
different from two, and every line bundle L on its complement U,
the forgetful map from twisted Chow–Witt CH2(U,L) to ordinary CH2(U)
is an isomorphism, with target Z/d. Consequently the characteristic
Euler class of any rank-two bundle vanishes exactly when its ordinary
c2 does. For O(a) plus O(b), this is exactly d dividing ab.

The proof uses the nonaffine-valid Bloch–Ogus argument and computes
the required étale vanishings directly by purity. It does not apply
an affine splitting theorem to U. The two top cohomology groups vanish
because a point on C pushes forward to a degree-one point of P3.
Rationality and the special quartic embedding play no role.
Ordinary algebraic K0 gives the same conclusion for the necessary
virtual extension equality. Geometrically these invariants forget
the actual equations and their common-zero support; even the quadratic
cycle refinement does not recover that information in this degree.

**What the realization literature actually added.** Stopar supplies a
genuine Oka principle beyond Stein bases, but its 1-convex source
hypothesis fails on U. The q-convex-with-corners result supplies two
positive Levi directions, short of its line-bundle extension theorem's
three-direction requirement in dimension three; extending a line bundle
would still not supply our section. Subellipticity of U as a target
does not make it a suitable source for the section theorem. These are
precise failures of the checked implications, not an analytic no-go theorem.

**Existence and nonexistence.** Every Bézout-admissible pair for C0 passes
the ordinary Chow, virtual K-class and twisted Euler conditions as well
as the full continuous test. This provides neither new equations nor
a contradiction, and gives no basis for preferring nonexistence. It
does eliminate these proposed detectors as a source of a stronger
all-pair necessary condition. The immediate nonplanar (1,d) control
also proves that passing them is insufficient for actual section
realization at a specified degree pair.

An abstract extension class still supplies an unspecified middle
bundle. Requiring that bundle to be O(a) plus O(b), with its actual
injection, reformulates the global equation problem until a construction
forces the identification. Testing the reflexive extension of a
separately supplied class is a verification method, not a source of
such classes. Raising a successful pair to equal degree is likewise
not an independent asymptotic existence mechanism.

**Recommendation and stopping.** Close this primary Euler calculation
uniformly, and stop the checked analytic theorem applications at their
failed hypotheses. Do not move automatically to higher motivic stages,
more positive twists, local extension types, or degree enumeration.
The complement route remains available only with an actual strict
realization/descent operation or a specified further algebraic
obstruction whose evaluation has a precise implication for arbitrary
pairs. No next technical experiment is selected here.

This conclusion fits the user's compatibility hierarchy: satisfying
cycle, bundle and homotopy data does not supply surfaces embedded
together in P3 with their entire intersection supported on C.
It also preserves the opposite possibility: a construction controlling
that last step in one source would suffice for existence, even without
classifying all sources. The scoped independent review passed; all
three assignments are complete. No canonical promotion, and the
unrestricted characteristic-zero STCI question remains open.

## 25. The projected powers fail ACM through an explicit global section

This selection tested a constructive intermediate target: a homogeneous
ACM thickening supported on the fixed C0 in its actual P3. Such a
construction would be substantive, although it would not itself settle
STCI. The earlier projected-power family had supplied support and had
been excluded as AG, but its ACM status was explicitly left open.
Reopening that precise question did not reopen the closed CI claim.

Two fresh gpt-6-astra/xhigh scouts checked residual-perfection and
embedded-doubling literature. A fresh gpt-6-astra/xhigh strategy reviewer
challenged the proposal and allowed only an all-parameter mechanism
or one structurally selected actual construction, with no exponent grid.
The parent reported that recommendation and stopping rule before the
test. The source scout's coherent context was then reused for the proof;
a separate fresh gpt-6.1-sol/high reviewer independently reconstructed
it. No nested delegation was used.

**New result and geometric content.** For every positive u,v in
characteristic zero, the actual image of V(h,f^u,g^v) fails ACM.
Writing the two coefficients of the omitted coordinate as Q=a q and
T=d t, the product H=q t survives modulo the coefficient ideal but
is killed by an irrelevant-primary ideal. It therefore supplies a
nonzero Rao class, with lower bounds 1,2,1 in degrees
2u+2v-3 and the next two.

More concretely, H z has compatible expressions in the retained
coordinates on the two charts covering the image, yet no global
ambient polynomial represents it. The new obstruction is an actual
failure of the ambient restriction map. It is not the previous local
non-Cartier conductor and is not a residual component. The
[source](2026-10-31-acm-construction-selection.md) and
[audit](2026-10-31-acm-construction-selection-audit.md) preserve the
explicit section, proof and independent review scopes.

**Generalization extracted.** The argument does not depend on the
particular covering quadric. For two linear coefficients and quadratic
remainders forming a homogeneous parameter sequence, any quadratic
monic covering equation gives the same power-projection obstruction.
Changing that quadric alone cannot repair the family; the underlying
curve may change. The algebra works whenever uv is nonzero in the
field, including characteristic two with odd exponents. It says nothing
about the divisible-exponent cases containing the known Frobenius
constructions.

**The second constructive check also has a concrete outcome.** The
classical quadric–cubic link to two skew lines gives three explicit
outputs under the checked residual machinery. The boundary determinant
ideal retains the lines; its natural Fitting ideal is P intersect m³
and adds only a cone-vertex defect; full Kitt recovers P, the original
quartic ideal. A nonzero Koszul socle class explains failure of the
sliding-depth and broader cycle hypotheses. This is more informative
than saying a theorem does not apply, but it remains a limitation of
that supplied source, not of all residual constructions.

**Existence versus nonexistence.** No ACM thickening was produced.
The all-power result closes a genuine operation and identifies exactly
what a replacement must repair. Its generalization eliminates simple
changes of the covering quadric within the same parameter construction.
It does not show that every supported thickening has such a section
defect, supply a positive residual-degree bound, or favor nonexistence
of STCI. A successful different ACM construction would still be a
meaningful step; an AG construction in the fixed P3 would settle
existence directly.

**Recommendation and stopping.** Close the inherited power source
as a producer of ACM images, not just AG images. Close the tested
skew-line residual presentation and its determinant/Fitting/Kitt
variants. Do not continue with exponents, neighboring quadrics or
local linkage types. A renewed construction needs an actual operation
that changes the embedded global deficiency while preserving support;
a renewed nonexistence argument needs a reason that this kind of
defect persists for arbitrary defining pairs. Neither new input is
supplied here, so no next technical experiment is selected.

The final source passed two independent reviews with separate
responsibilities. All four bounded assignments are complete.
No canonical promotion; unrestricted characteristic-zero STCI remains open.

## 26. The same defect survives arbitrary binary mixtures; no new lane selected

The next selection asked whether replacing independent powers by
\(\Phi(f,g),\Psi(f,g)\), for arbitrary homogeneous binary forms with
positive degrees u,v and isolated common zero at the origin, could
produce an ACM image. This
is an actual operation with automatic support control, but it had no
identified mechanism for changing the missing ambient section.

A fresh gpt-6-astra/xhigh scout and a separate fresh
gpt-6-astra/xhigh strategy reviewer independently found the same
determinant replacement for the previous product. Primary literature
supplied the precise Jacobian-socle theorem. The reviewer recommended
only one uniform proof extraction, then closure, rather than a new
construction campaign. The parent reported that recommendation and
the stopping conditions before the proof investigation. No binary-form,
degree or coefficient classification was launched.

**Exact gain.** The [source, §3a](2026-10-31-acm-construction-selection.md#3a-arbitrary-binary-mixtures-retain-the-same-defect)
proves that every such mixed source fails ACM when uv is nonzero in
the field. The odd coefficients of the two substituted equations give
a two-by-two matrix relative to the two linear chart coordinates.
Its determinant H is irrelevant torsion; modulo those coordinates it
becomes the binary Jacobian socle generator. Finite free substitution
preserves that nonzero generator and yields the same Rao lower bounds
1,2,1. The parameter-sequence generalization of the preceding result
persists; characteristic two is allowed for odd uv.

The actual geometric object is the section Hz. It has compatible
representatives on the two charts covering the image, yet no ambient
polynomial represents it. Mixing the two functions changes the source
scheme while retaining this failure of the projected section ring.
The auxiliary binary algebra explains the determinant, but is not
being identified with the entire generic transverse algebra.
The precise literature dependency is Eisenbud–Ulrich, Appendix
Theorem A.5; no new general socle theorem is claimed.

**Why this does not transfer automatically to arbitrary pairs.**
A pure primary lift of a hypothetical supported CI need not have
this two-equation source presentation or even be ACM. Its quotient
by the downstairs ring has no irrelevant torsion precisely because
the downstairs ring is CM. Asking for a nonzero class in that torsion
therefore states a contradiction target; it does not construct one.

Even the displayed source class need not survive a quotient that keeps
the same reduced curve. Reduction to the rational normal quartic D
gives \(B_D/A_{C_0}=k(-1)\): only the omitted degree-one section z is
missing, and the four retained quartics generate every section in
degrees at least two. Thus the class \(H_{uv}z\), of degree
\(2u+2v-3>1\) when u+v>2, maps to zero after reduction to D. This
blocks a functorial persistence shortcut. It does not provide a CI
quotient or rule out a different universal invariant.

**Existence versus nonexistence.** The result explains and closes a
whole support-preserving operation. It does not make nonexistence
more likely, exclude arbitrary ACM thickenings, or supply a lower
bound on a genuine residual curve. An actual ACM thickening in the
fixed P3 remains a substantive constructive intermediate target;
an AG one would settle existence. The nonexistence direction still
needs an independent restriction on arbitrary defining pairs.
Neither naming their Rao defect nor repeating the conductor/attachment
identity supplies that restriction.

**Recommendation and stopping.** Close independent powers and all
homogeneous binary mixtures together. Do not seek different degrees,
binary coefficients, quadrics or a complete Rao-module classification
inside this mechanism. No next technical experiment is selected.
Reopening requires either an actual support-preserving embedded
operation with a reason it can alter the global section defect, or a
new all-pair comparison with a specified geometric input and a
discriminating consequence. For example, an independent strict upper
bound contradicting the existing conductor lower bound would qualify;
requesting that bound without any mechanism does not.

The new proof is independently reviewed in the
[audit appendix](2026-10-31-acm-construction-selection-audit.md).
This continuation consolidates the preceding result rather than adding
a new source catalog. All bounded assignments are complete. The
unrestricted characteristic-zero STCI question remains open, and
existence remains a live possibility.

## 27. Carrier defects and sheaf modifications do not yet supply the next bridge

This selection compared the new carrier differential result with an
actual literature construction on the fixed P3. It selected no
technical experiment. The purpose was to identify a new input affecting
arbitrary pairs or an embedded construction, after §26 closed the
binary-substitution source.

### The two defining surfaces have necessary defects, but their budgets are different

The current [all-degree carrier note](2026-10-31-carrier-conductor-differential-bound.md)
and its embedded review imply the following trichotomy for **each**
integral defining carrier of a hypothetical characteristic-zero STCI:
it is generically singular along C0, its normalization is singular on
the inverse curve, or its full conductor is singular at a contact with
C0. The factor reduction and low-degree exclusion remain inherited
premises. The trichotomy does not place the two carriers' failures at
the same point or in the same alternative.

For a generically regular carrier of degree a whose normalization is
smooth along the inverse curve c, its geometric quantities are
\[
c^2=16/a,\qquad D\cdot c=4a-14+16/a,\qquad
\deg H_{\rm diff}\le7-16/a.
\]
The incompatible smooth-contact comparison gives a required **lower**
contribution from singular conductor contacts. It supplies no upper
bound on those contributions. Neither generic singularity along C0
nor a singular normalization can be dropped from the remaining regimes.

This surface-normalization conductor is different from the finite
endpoint conductor of the full nonreduced intersection in the
[quadratic-cover note](2026-10-31-quadratic-cover-boundary.md).
That note's \(\delta\ge a+b-3\) is another lower requirement. Neither
source supplies a morphism or filtration comparing the two conductor
modules in a direction that would contradict either bound.

The shared tangent direction does not supply that missing comparison.
The earlier [actual first-layer identification, §§1–4](2026-10-14-generalization-transverse-differential-socle-bound.md)
already identifies the dual saturated normalization direction with
\((J/J^2)_{\rm tf}\), when its generic-regularity and singleton Cartier
lift hypotheses hold; its [independent audit](2026-10-14-generalization-transverse-socle-independent-audit.md)
preserves that scope despite the older source header's pending wording.
Applying it to both eligible carriers makes
their saturated directions equal. This is an inherited compatibility
statement, not a new obstruction or a reduction of singular lifts.

### A concrete sheaf construction and its precise limits

Work over C for this literature application. Let \(i:C_0\hookrightarrow
\mathbf P^3\). The basepoint-free pair \(s^7,t^7\) supplies an actual
surjection and kernel
\[
0\longrightarrow F\longrightarrow\mathcal O_{\mathbf P^3}^{\,2}
\longrightarrow i_*\mathcal O_{\mathbf P^1}(7)\longrightarrow0.
\]
[Jardim–Markushevich–Tikhomirov, Proposition 3.1](https://arxiv.org/pdf/1501.00736)
applies with \(L=\mathcal O_{\mathbf P^1}(-1)\), since \(L(2)=
\mathcal O_{\mathbf P^1}(7)\). It gives a rank-two torsion-free
instanton sheaf of charge four. Its reflexive hull is \(\mathcal O^2\);
locally along C0 its kernel is \(\mathcal O\oplus I_{C_0}\).
The sequence twisted by -1 gives
\[
H^1(F(-1))=H^0(\mathbf P^1,\mathcal O(3)),\qquad h^1=4.
\]
Thus this is an actual sheaf singular along the chosen embedded curve,
with nonzero intermediate cohomology. It does not provide a new
homogeneous coordinate ring or an ACM thickening.

Two general restrictions explain why the obvious repairs do not finish
this operation. First, a kernel of a vector bundle E mapping to a
codimension-two-supported quotient has reflexive hull E. Two locally
free extensions equipped with an isomorphism off C0 are isomorphic
globally, by [Hartshorne, Remark 1.8](https://escholarship.org/content/qt4j1747kh/qt4j1747kh.pdf).
This does not forbid deformations changing the restriction on the
complement. Second, even such a flat deformation of this particular F
cannot become a split rank-two bundle: its fixed Chern classes are
\(c_1=0,c_2=4\), whereas \(\mathcal O(r)\oplus\mathcal O(-r)\)
has \(c_2=-r^2\). After any common twist t the required split degrees
would satisfy \(a+b=2t,\ ab=t^2+4\), with discriminant -16.
This elementary check concerns the fixed flat class, not operations
changing Chern classes or other possible supported thickenings.

The [Horrocks monad construction described by Malaspina–Rao, §1](https://arxiv.org/pdf/2202.00304)
also supplies no such repair. Its split middle bundle P on P3 has
rank \(2+\operatorname{rk}A+\operatorname{rk}B\); the original
rank-two E remains the cohomology \(\ker(P\to B)/\operatorname{im}A\).
Eliminating those extra terms while controlling a supported section
requires additional data, not provided by the monad theorem.

The recent [Ballico–Cid-Ruiz–Singh, Theorem A](https://arxiv.org/html/2602.09201v2)
likewise does not fill this gap. It gives generic flatness, for one
fixed twist j and all ordinary power thickenings, for a smooth family
over a Noetherian domain containing a field of characteristic zero.
It does not give cohomology vanishing,
arbitrary supported ideals, or mixed-characteristic specialization.

### Disposition, review and stopping

These comparisons identify the actual objects produced by the checked
operations and the missing implications. They provide no new
unrestricted nonexistence theorem. An actual ACM thickening remains a
meaningful constructive target, and an AG thickening in P3 would settle
existence. No numerical failure above should be transferred to a
different operation without checking its hypotheses and output.

**Recommendation:** select no technical experiment from these inputs.
Do not enumerate conductor singularities, instanton charges, monad maps
or adjacent degrees. Reopening requires a specified support-preserving
operation into an actual ideal/section, or a geometric comparison of
the two specified conductor modules with a discriminating consequence.
A proposed mechanism may be unproved; a restatement of the desired
vanishing or bound is insufficient. Stop its first test if it only
recovers a sheaf presentation or one of the existing lower budgets.

Two fresh gpt-6-astra/xhigh scouts performed the separate carrier and
existence selections. A fresh gpt-6.1-sol/high reviewer independently
challenged the recommendation, checked the primary theorem scopes and
reconstructed the sheaf/cohomology deductions. The new Chern-class
check received a separate bounded confirmation. No nested delegation,
numerical experiment or new local classification was used.
The reviewer returned a scoped PASS on the actual written §27;
its suggested precision about smoothness and the base in Theorem A
was incorporated. No material finding remains unresolved.

This review reuses the carrier note's recorded provisional proof status;
it is not a fresh audit or canonical promotion of the concurrent work.
The inspected carrier-note fingerprint is
fbad7b8b4e708edb8b94c7d1e2be2237a20f8ff7b14f858ee42c1f07125cd24f.
Its concurrent files were preserved without editing or staging them.
All selection assignments are complete. Unrestricted characteristic-zero
STCI remains open; no next technical round has begun.

## 28. Low-degree norms strengthen the boundary requirement for every pair

This continuation supplied a concrete all-pair input to the existing
quadratic-boundary inequality. It did not choose a new carrier family.
For any hypothetical pair of defining degrees
\(5\le\alpha\le\beta\), set
\[
e=\alpha+\beta-4,\qquad
q=\left\lceil\frac{\alpha}{2}\right\rceil-1.
\]
Retain the actual full primary lift \(A\subset B=A+Az\) and its
conductor boundary \(\Delta\), of length \(\delta\). The
[consolidated proof, §3a](2026-10-31-quadratic-cover-boundary.md#3a-the-quadratic-norm-forces-additional-conductor-postulation)
now gives
\[
H_\Delta(n)=\binom{n+3}{3}\quad(0\le n<q),
\]
and the stronger necessary bound
\[
\boxed{\quad
\delta\ge\alpha+\beta-3+
2\left[\binom{q+2}{3}-q\right].
\quad}
\]
For every surviving characteristic-zero pair, q is at least two,
so the displayed scalar bound strictly strengthens the old
\(\delta\ge\alpha+\beta-3\).

**New input and geometry.** A homogeneous conductor element h of
degree d makes hz descend to an ambient polynomial P of degree d+1.
Its norm \(P^2-(2bc-ad)h^2\) is a nonzero equation of the actual
complete intersection, of degree 2d+2. The nonsquareness used here
is in the fraction field of the ambient polynomial ring; h may be
nilpotent on the intersection. Since there is no nonzero equation
below degree \(\alpha\), no conductor equation can have degree
below q.

Thus the finite boundary, despite its two-point reduced support,
cannot lie on any ambient hypersurface of degree below q. Its full
infinitesimal structure retains all ambient restrictions in that
range. The existing canonical injection forces later postulation
as well. Combining these facts at \(n=q-1\) gives the displayed
length bound. The additional term grows cubically in the smaller
defining degree, but remains a lower requirement.

This norm is a new explicit all-pair application of a mechanism
previously used to close particular projection/linkage sources.
The scalar estimate uses the earlier canonical inequality; it is
not a second independent duality budget. Kreuzer's canonical-module
literature remains the checked background, with no use of a stronger
maximal-degree Cayley–Bacharach assertion. No optimality or
literature-priority claim is made.

The proof separates two reusable statements: a norm-based
initial-degree bound for quadratic-generated graded extensions,
and a purely graded postulation estimate. Their precise hypotheses
are retained in the source. No assertion that arbitrary curves
admit this cover is made. The algebra itself is not a new
characteristic-zero-specific mechanism; the low-carrier premise
for C0 is the characteristic-zero input.

**Existence versus nonexistence.** An actual candidate with too little
conductor postulation is ruled out by this condition, which also
specifies more of what a successful construction must supply. There
is no upper bound on the available conductor length contradicting it.
The result neither produces a residual curve nor proves a positive
residual-degree floor, and does not favor nonexistence of STCI.

**Selection, review and stopping.** A fresh gpt-6-astra/xhigh scout
checked the relevant sources and proposed the bounded extraction;
a separate fresh gpt-6-astra/xhigh reviewer challenged its all-pair
scope and approved only this uniform proof. The parent reported
the recommendation and stopping condition before proceeding.
The scout's coherent context was reused for the derivation, and a
fresh gpt-6.1-sol/high reviewer independently reconstructed the
argument and checked the written source. The
[audit appendix](2026-10-31-quadratic-cover-boundary-audit.md)
records the actual review state and fingerprint.

Stop after this bound. Do not start degree grids, endpoint-scheme
classifications or a search for an unspecified upper bound. A next
test needs an actual construction to check against the requirement
or a new geometric comparison that constrains this same boundary.
No further technical experiment is selected. All three assignments
are complete; no nested delegation or numerical experiments occurred.
The result remains provisional and unrestricted STCI remains open.

## 29. Conductor endomorphisms retain the embedding problem; liaison addition has actual input

This selection compared a possible global use of the quadratic conductor
action with an actual construction operation on the smooth covering
quadric. It selected no new classification or technical experiment.
The setting is the fixed characteristic-zero C0 and the full hypothetical
supported CI from the [boundary note](2026-10-31-quadratic-cover-boundary.md).
All statements below use its actual graded rings, not just the reduced
curve or generic function field. These are independently reviewed
provisional deductions, with the scope recorded below.

**The CM conductor does not repair the embedded curve.**
Write \(A=S/(F_\alpha,G_\beta)\), \(e=\alpha+\beta-4\),
\(A\subset B=A+Az\), \(z^2=r=2bc-ad\), and
\(\mathfrak c=\operatorname{Hom}_A(B,A)\), \(T=A/\mathfrak c\).
The exact sequence
\[
0\longrightarrow\mathfrak c\longrightarrow A\longrightarrow T
\longrightarrow0
\]
and the already established depths two and one give
\(\operatorname{depth}\mathfrak c=2\). This is a consequence of the
existing boundary result, not another independent restriction.
The conductor is MCM over A, but has dimension and depth two over
the four-dimensional covering ring E, so is not MCM over E.

Finite duality identifies \(\mathfrak c(e)=\omega_B\). The canonical
endomorphism construction therefore gives
\[
B^\sharp=\operatorname{End}_B(\mathfrak c)
        =\operatorname{End}_A(\mathfrak c).
\]
For the second equality, localize in the common full total quotient
algebra: c has rank one there, so its A-endomorphisms are multiplication
operators and commute with B. The primary branch is unmixed.
[Hochster–Huneke, §2.2(f,h), Proposition 2.7](https://arxiv.org/pdf/math/0211172)
identify this ring as the finite S2-ification. Here B is CM off its
cone vertex, and the graded section sequence gives
\[
B^\sharp=\bigoplus_{n\in\mathbf Z}H^0(W,\mathcal O_W(n)),\qquad
B^\sharp/B=H^1_{\mathfrak m}(B)=M_W.
\]
Thus this operation fills the section ring of the same projective
scheme W. It does not change W's given ambient restriction maps or
turn their coordinate image B into an ACM quotient. The full graded
ring can include negative-degree nilpotent sections; it is not
automatically another standard graded quotient in the same coordinates.

There is actual quadratic action on the conductor,
\(\mu:\mathfrak c\to\mathfrak c(1)\), with \(\mu^2=r\), and on \(M_W\).
Since \(B^\sharp\mathfrak c\subset\mathfrak c\), one has
\(\mathfrak c M_W=0\), so the latter is a module over
\(T[z]/(z^2-r)\). But multiplication by z does not preserve the even
copy of T in the quadratic conductor boundary: it sends it into
the odd summand. No compatible z-action on the two terms of
\(T(e-1)\hookrightarrow\omega_T\) is inherited by that argument.

The full action, with its embedding retained, has an exact meaning.
In \(R=A[z]/(z^2-r)\),
\[
\ker(R\longrightarrow B)
=\{zh-\mu(h):h\in\mathfrak c\}.
\]
A relation \(p+zq=0\) says exactly that \(q\in\mathfrak c\) and
\(p=-\mu(q)\); stability under z follows from
\[
z(zh-\mu(h))=-\bigl(z\mu(h)-\mu^2(h)\bigr).
\]
Geometrically, this records which multiples of the omitted coordinate
descend, and their actual descended sections. It reconstructs the
embedded branch ideal. Asking for the allowable embedded conductor
and action, without a further comparison, restates that equation
problem. Keeping only module ranks or twists drops these crucial maps.

The second E-syzygy of c is MCM and is eligible for the quadric module
classification, but its maps back to c, the embedding into A, and
mu remain to be supplied.
[Drozd, Lemma 2 and Theorem 2](https://arxiv.org/pdf/math/0409243)
require the actual curve to be ACM for its ordinary E-type module to
be ACM/MCM. That hypothesis is unavailable for arbitrary W.
[Hartshorne–Migliore–Nagel, §5](https://academicweb.nd.edu/~jmiglior/HMN.pdf)
retain a compatible surjection as well as Rao and MCM modules for
non-ACM curves. Those data may contain more than numerical postulation,
but no checked theorem makes their actual conjugate compatibility
impossible here.

**Liaison addition has a real support-compatible input, with an early failure.**
For ideals \(I_1,I_2\) on Q3 and a regular pair \(F_i\in I_i\), the
same paper's Definition 2.1 and Lemma 2.2 give the saturated ideal
\[
J=F_2I_1+F_1I_2
\]
and exact sequence
\[
0\to E(-d_1-d_2)\to I_1(-d_2)\oplus I_2(-d_1)\to J\to0.
\]
Its support includes both input curves and \(V(F_1,F_2)\);
its Rao module is the direct sum of the shifted input modules.
Consequently using the deficient reduced union \(D\cup\sigma D\)
as an input cannot repair its Rao module. This does not exclude
using the two ACM rational normal curves separately.

Indeed put \(P=I_D\), \(f=b^2-az\), \(g=c^2-dz\), and choose
\[
F_1=f,\qquad F_2=g^3-4d^4f.
\]
On \(\sigma D\), \(f=2s^6t^2\) and \(g=2s^2t^6\), so
\(F_2\in\sigma P\). Also \((f,F_2)=(f,g^3)\), a regular sequence
supported on D by the accepted power-source calculation. Therefore
\[
J=F_2P+f\,\sigma P
\]
is an actual ACM curve supported on \(D\cup\sigma D\).
It adds the two branches and a CI thickening on D; it does not
assert equality of the two conjugate primary structures.

The existing obstruction applies immediately:
\(f\sigma(f)\in J\). Every D-primary extraction contains J, and its
conjugate also retains this invariant quartic. Their union therefore
descends with a quartic equation in its ideal, ruling out a supported
CI image by the accepted low-carrier exclusion. The same gate applies
to every such addition retaining \(F_1=f\), regardless of \(F_2\).
This is a check of available input using an existing obstruction,
not a new exclusion of liaison addition generally.

[Casanellas–Drozd–Hartshorne, Proposition 3.4](https://arxiv.org/pdf/math/0307378)
does give an operation when an N-type sheaf N has an orientable
rank-two ACM subsheaf with locally CM quotient N' of rank at least
two. It uses sufficiently general sections and even G-liaisons to
obtain a resolution with N'; this is N-type only under the additional
vanishing \(H^1_*(N'^\vee)=0\). The operation neither prescribes this
fixed support nor the conjugate partner, and even G-liaison preserves
Rao modules up to twist. It does not supply the missing equation maps
in the successful form required here.

**Comparative decision and stopping.**
The conductor calculation prevents replacing the actual coordinate
ring by its CM section ring and claiming an embedded repair. It also
isolates an actual action on the Rao module, without asserting an
unproved action on T or a second numerical budget. The liaison check
shows that support and ACMness can be achieved together upstairs;
their achievement still need not remove a forbidden downstairs
equation or give the required conjugate canonical structure.

For existence, reopening needs an actual embedded operation escaping
that norm with specified support and conjugation control. For
nonexistence, it needs a defined constraint on the actual conductor
action or presentation maps beyond the existing scalar identities.
A result deciding such a proposed test is not required in advance.
No spinor-twist, Rao-module, endpoint or liaison-chain classification
is selected. These findings supply neither an upper conductor bound
nor residual positivity; STCI existence remains live.

Two fresh gpt-6-astra/xhigh scouts performed the separate literature
and input checks; a fresh gpt-6.1-sol/high reviewer challenged the
selection and independently reconstructed its consequential claims.
The preliminary assertion that support-compatible liaison input was
missing was corrected by the explicit pair above before reliance.
No nested delegation, numerical experiment or local classification
was run, and no further technical experiment was selected.

**Review disposition.** The scouts were
/root/quadratic_action_global_selection and
/root/quadric_liaison_construction_selection; both assignments are
complete. The independent reviewer,
/root/conductor_module_strategy_challenge, checked the written §29
at assessment-file SHA256

    1cd97fe66a8d0f4fb5dc75ac097d23d599a9bd8bcba11b38101542796f0d2182

and returned scoped PASS subject to one CDH hypothesis clarification.
That clarification is incorporated above: orientable rank-two ACM
subsheaf, locally CM quotient of rank at least two, and the additional
dual-cohomology condition for an N-type output. The parent checked
the correction; the subsequent edits only record this review state.
No material finding remains unresolved in this section.

The review independently covered the canonical-endomorphism theorem's
application, equality of endomorphism rings, full graded section-ring
and Rao quotient identifications, conductor annihilation and quadratic
action, graph reconstruction, syzygy depth and E-type distinction,
the exact liaison theorem and its saturation/ACM consequence, explicit
regular pair and norm persistence, and comparative stopping decision.
It reused the accepted low-carrier and supported-power proofs rather
than re-auditing them. These scoped passes do not promote a canonical
result or prove an unrestricted STCI conclusion.

## 30. Marked covers clarify a missing section; arithmetic and residual constructions need embedded input

This checkpoint concerns the unrestricted question over algebraically
closed fields of characteristic zero
for \(C_0=[s^4:s^3t:st^3:t^4]\). It closes the marked-cover and arithmetic
selection checks, and checks a new positive residual-intersection source.
The recommendation and stopping conditions were reported before the
short geometric extraction below. No prime, degree, endpoint or
presentation classification is selected.

**What the cover interface already retains.**
For every hypothetical proper pair
\(Y=V(F_\alpha,G_\beta)\), \(Y_{\mathrm{red}}=C_0\), the pencil
\(\pi=[a:d]:Y\to B=\mathbf P^1\) is finite flat of degree
\(n=\alpha\beta=4m\), with reduced map \(f(t)=t^4\). Its module is
\[
\pi_*\mathcal O_Y\simeq
\bigoplus_{i=0}^{\alpha-1}\bigoplus_{j=0}^{\beta-1}
\mathcal O_B(-i-j).
\]
These are existing [fixed-surface results, §§4–6](2026-10-30-fixed-surface-configuration.md),
including actual multiplication by the ambient coordinates. The two
marked hyperplanes are fibers of this same nonreduced algebra, not
independent conditions on an abstract rational curve.

Only the reduced cover is étale off the marked fibers in characteristic
different from two. For \(m>1\), the full cover is generically nonreduced.
The existing [trace identity and different](2026-10-31-cyclic-cover-duality.md#4-the-precise-different-of-the-cyclic-projection)
give
\[
\operatorname{Tr}_{Y/B}
=m\operatorname{Tr}_{C_0/B}\circ\mathrm{red}.
\]
In characteristic zero, or odd characteristic not dividing m, the
generic trace pairing has rank four on an algebra of dimension \(4m\).
Its radical is the nilradical. If the characteristic divides m, the
trace is zero. Thus for \(m>1\) the ordinary discriminant is identically
zero; this is not an effective two-point branch divisor. Dividing
the trace by m does not produce an algebra retraction.

[SGA 1, I.5.5 and I.8.3](https://arxiv.org/pdf/math/0206203)
identify étale categories across nilpotent thickenings. The tame
specialization results in XIII.2.8–2.12 concern covers of smooth curves
with the specified boundary. These statements do not retain and lift
the embedded transverse nilpotent algebra of Y. A tame reduced cover
therefore does not supply a supported mixed-characteristic pair.
The prime-to-characteristic Jacobian-socle theorem is already used
in the repository; a nonzero socle element supplies neither étaleness
nor such a lift.

**One new geometric extraction, not an additional obstruction.**
The [short corollary in cyclic-cover duality §5.1](2026-10-31-cyclic-cover-duality.md#51-the-punctured-retraction-cannot-extend-over-the-pencil)
now proves that the unique punctured retraction cannot extend over B.
Writing \(L=\mathcal O_Y(1)=\pi^*\mathcal O_B(1)\), a retraction over B
would split restriction from \(H^0(Y,L)\), of dimension four, onto
\(H^0(C_0,L|_{C_0})\), of dimension five. Its impossibility expresses
the already known missing section \(s^2t^2\).

The argument generalizes to any linearly normal containing scheme
and a contained curve whose given embedding is not linearly normal:
there is no retraction preserving the polarization compatibly with
restriction. It is characteristic free and consistent with the
known characteristic-two STCI. It supplies no exclusion of an
unpolarized retraction, no identification of the obstructing endpoint,
and no new residual-degree bound. This closes the extraction without
an endpoint-obstruction classification.

**A cover theorem that applies, and what its output leaves open.**
[Landesman–Vakil–Wood, Theorem 3.2 and Remark 3.3, pp.16–18](https://arxiv.org/pdf/2203.01840)
give the corrected Casnati–Ekedahl relative canonical embedding and
self-dual resolution for a finite locally free Gorenstein cover of
degree at least three. A nonreduced source is allowed. For the actual
CI above its fibers are zero-dimensional Gorenstein schemes, and its
relative canonical bundle is \(\mathcal O_Y(\alpha+\beta-2)\).
The theorem re-embeds Y in the projective bundle associated to
\((\pi_*\mathcal O_Y/\mathcal O_B)^\vee\); it does not by itself
construct the desired cover algebra.

The constructive gap needs a precise statement. For an abstract
finite cover with the displayed module splitting, the line bundle
\(L=\pi^*\mathcal O_B(1)\) already has four sections and is globally
generated by the base pencil. Its complete series therefore gives
an actual morphism to \(\mathbf P^3\). The missing conditions are a
cover with the specified reduced support, restriction image exactly
\(\langle s^4,s^3t,st^3,t^4\rangle\), separation of the nilpotent
structure giving a closed immersion, and a complete-intersection
image. They are not the existence of four sections or basepoint
freeness. Also, self-duality of the underlying split module does not
alone give the algebra-linear duality identifying the relative
canonical bundle with the required power of L. That identification
for the actual CI cannot be imported into an abstract construction
from its module splitting alone.

**Arithmetic: reuse the established reduction.**
[STCI_SEARCH §3](../STCI_SEARCH.md#3-characteristic-p-the-correct-minimum-degree-target)
and its [logic audit](2026-10-28-stci-search-logic-audit.md)
already show that nonexistence in characteristic zero is equivalent
to divergence of the minimum defining degree over all positive-
characteristic pairs. The existing [arithmetic analysis](2026-10-28-stci-search-arithmetic.md)
explains why an all-pairs divisibility condition \(p\mid m\) would
suffice, whereas its proof for one binomial class does not. The
mixed-characteristic discussion in §17 also separates a horizontal
incidence component from an unramified first-order lift. None of
the newly checked cover statements proves either a universal
divisibility condition or a horizontal component. Isolated prime
tests and fixed-carrier failures are not a substitute.

**New positive literature: the actual height-two specialization.**
[Batavia–Pandey–Walther, arXiv:2610.25680v1, §5](https://arxiv.org/pdf/2610.25680v1)
construct STCI residual intersections. Theorem 5.1, pp.22–24, starts
with a regular sequence of length \(n>1\) in a Gorenstein local
ring and \(s\ge n\); Theorem 5.2, pp.25–27, starts with a height-three
Gorenstein Pfaffian ideal and \(s\ge3\). Their homogeneous
specialization in §2.4 uses a sequence regular on both ambient ring
and quotient, preserving height.

For the height-two output of the explicit Theorem 5.1 pattern,
\(s=n=2\). Writing the input as \((u,v)\), its matrix and ideal are
\[
X'=\begin{pmatrix}x&\lambda\\\lambda&0\end{pmatrix},
\quad
J=(xu+\lambda v,\lambda u,\lambda^2),
\quad
\sqrt J=\sqrt{(\lambda,xu)}.
\]
The radical identity follows directly from \(\lambda^2\in J\) and
reduction modulo \(\lambda\), and survives any substitution. Its
geometric output is
\[
V(\lambda,xu)=V(\lambda,x)\cup V(\lambda,u).
\]
If \(\lambda,x,u\) are nonzero positive-degree homogeneous forms in
the coordinate ring of \(\mathbf P^3\), both branches have dimension
at least one. If their union has support exactly the irreducible
\(C_0\), both already have that support. Thus the requested
specialization already supplies a supported two-equation pair.
The operation can alter its transverse structure, but cannot remove
an unwanted component of either branch.

A literal nonzero linear \(\lambda\) cannot contain the nondegenerate
\(C_0\). Higher-degree entries require actual homogeneous forms,
degree balance \(\deg x+\deg u=\deg\lambda+\deg v\), and support
control. The radical formula does not establish that arbitrary
substitution preserves the colon identity or residual hypotheses.
The height-three theorem cannot produce this codimension-two curve
through a height-preserving specialization. An additional height-
dropping map needs its own support and two-equation argument.
These are limits of the checked explicit operation, not exclusions
of residual constructions generally.

**Recommendation, comparative value and stopping conditions.**
The recent all-pair gain remains the strengthened conductor
postulation bound of §28; this checkpoint adds a geometric
interpretation of the missing section and rules out two automatic
uses of the new sources. It adds no incompatible upper bound and
no actual characteristic-zero supported pair. The compatibility
problem now sits in actual multiplication, polarization and ambient
embedding maps; retaining all those maps without an independent
constraint merely presents the original equation problem again.

Existence remains an equal possibility. One actual supported
construction or suitable simultaneous lift can settle it. A
nonexistence direction needs an implication for arbitrary pairs,
such as a new constraint on their full boundary algebra; a family
exclusion needs an exhaustive reduction. No further technical
experiment is selected from the sources checked here.

Reopen with a named geometric operation and a specific ambient
property to test, or a defined all-pair comparison beyond the
existing identities. A successful outcome need not be known in
advance. Stop the proposed test if it forgets the nilpotent algebra,
assumes the needed embedding/duality, already requires a supported
pair as input, or returns only an existing identity. Do not extend
that failure into nearby primes, endpoints, degrees or presentations
without a new unrestricted implication.

**Review state.** Fresh bounded scouts
/root/arithmetic_global_mechanism_selection and
/root/marked_cover_tame_selection used gpt-6-astra/xhigh;
/root/new_residual_stci_source_selection used gpt-6.1-sol/high.
The fresh independent reviewer
/root/arithmetic_cover_strategy_challenge used gpt-6.1-sol/high,
challenged the recommendation, and reconstructed the no-retraction
proof and residual-support argument. Its correction that four
globally generating sections already exist for the split cover,
and its algebra-linear duality qualification, are incorporated.
All selection assignments are complete; no nested delegation or
numerical experiment was performed. No canonical promotion is made.

The same independent reviewer then checked the written source §5.1,
this §30 and the corresponding literature-ledger entry, returning
**scoped PASS with no material correction**. The inspected source
SHA256 was

    bdf7331c3163d2189b41671261777cf481353315fb351610f7dc32a2f655fb4e

and the assessment SHA256 before this review record was

    7037df155b78b8fe1c54e6f8c44cdf439ef86958bf0685ead3cf56f3e3173bae

The check covered the proof, generalization, characteristic scope,
full-versus-reduced cover distinction, canonical-embedding application,
residual radical and support argument, and comparative stopping.
The SGA statements reuse the earlier bounded primary-source reviews;
this was not a new SGA or whole-repository audit. The parent separately
corrected and checked the two internal anchors and opening field
wording excluded from the review disposition. Subsequent changes
to this section only record this review state.

## 31. The exact Cox fiber closes a reduction shortcut, not the STCI question

This bounded selection concerns the fixed C0 over an algebraically
closed field of characteristic zero. Two fresh scouts checked
affine-fibration and ambient Cox/principalization mechanisms.
Independent challenge recommended one short uniform extraction,
reported before preservation, and no further technical experiment.

**Actual gain and inherited input.**
The [new compact deduction](2026-10-31-cox-fiber-and-power-defects.md)
uses the published Cox presentation for the exact quartic blowup.
The ordinary Rees special fiber at the affine-cone vertex is
\[
\mathcal F(I_{C_0})=k[Q,U,V,W]/(UW+V^2).
\]
The special-fiber algebra has dimension three; its projective
spectrum is a two-dimensional quadric cone. Every power therefore
has analytic spread three, excluding
a two-generated reduction of any ordinary or symbolic power.
A hypothetical STCI pair need not be such a reduction.

All-power saturation and symbolic-equals-ordinary were already
proved in the [October 5 quadric theorem](2026-10-05-literature-new-routes.md#2-uniform-theorem-for-integral-curves-on-a-smooth-quadric);
the weaker October 7 bound is not the full existing result.
The extraction does not rebrand this inherited theorem as new.
The same elementary quadric sequence now makes the global section
defect explicit:
\[
h^1(\mathcal I_{C_0}^r(3r-2))=2r-1\quad(r\ge1).
\]
For any integral type-(a,b) curve on a smooth quadric, with
\(1\le a\le b,\ b\ge3\), the corresponding value at degree
\(br-2\) is \(\max\{(b-a)r-1,0\}\), in every characteristic.
These are missing ambient sections on the ordinary codimension-two
thickening, not on the Cartier multiple inside the quadric.
This explains the already recorded failure of the eventual-CM
hypothesis in symbolic-Rees construction criteria. It does not
transfer the defect to arbitrary supported CI structures.

**Affine morphisms do not supply an independent fibration input.**
The [existing complement-pencil argument, §8](#8-subsequent-selection-birational-transport-and-complement-pencils)
already proves that STCI is equivalent to a nonconstant
\(f:\mathbf P^3\setminus C_0\to\mathbf P^1\), and every such
morphism is affine. Its fibers are complements of C0 in the pencil hypersurfaces,
with no implied affine-plane or ruled structure.

[Dubouloz–Kishimoto, Theorem 6](https://arxiv.org/pdf/1408.1328)
requires negative logarithmic Kodaira dimension of the general
smooth geometrically connected affine surface fibers; its printed
field hypothesis includes infinite transcendence degree over Q.
Its output also shrinks the base and makes a finite étale base
change. It neither constructs f nor establishes the missing
fiber hypothesis.
[Gurjar–Masuda–Miyanishi, Theorem 2.8](https://sci-tech.ksc.kwansei.ac.jp/~kayo/cmn/papers/lnd_def_final_02.pdf)
requires every closed fiber of the given smooth affine morphism
to be an affine plane. Generic smoothness does not give that.
[Dinh–Jelonek, Theorem 3.4](https://d-nb.info/1185855084/34)
removes stratified generalized critical values, including
asymptotic critical values; ignoring degeneration at infinity
would unjustifiably turn the pencil into a global topological
bundle. The missing boundary behavior is the issue to control.

**Finite ambient chambers do not principalize arbitrary pencils.**
[Hu–Keel, Propositions 1.11 and 2.9](https://arxiv.org/pdf/math/0004017)
controls complete linear systems and rational contractions on a
Mori dream space. The rational-contraction condition cannot be
assumed for a selected pencil: its resolution can extract divisors
mapping dominantly to the parameter line.
[Wlodarczyk, Theorem 1.0.1](https://www.math.purdue.edu/~wlodarcz/singularities/Resolution.pdf)
principalizes each specified ideal, without a uniform estimate
charging all later contact against the original projective degrees.

One uniform geometric control makes the distinction concrete.
For every \(N\ge2\), the same-degree pair in \(\mathbf P^3\)
\[
X^N,\qquad XZ^{N-1}+Y^N
\]
has sole reduced support the line \(L=V(X,Y)\). On \(Z=1\)
at its generic point, put \(u=X,\ v=Y,\ w=u+v^N\). Its ideal is
\[
(u^N,u+v^N)=(w,v^{N^2}).
\]
Successive ordinary blowups in a generic transverse surface
must retain the valuation \(\nu(w)=N^2,\ \nu(v)=1\), and
\(\nu(u)=N\). Thus the fixed Mori dream blowup of the reduced
line does not provide a fixed finite modification principalizing
all these pencils. All this contact remains over the line;
there is no residual curve downstairs.

This control disproves a bound based only on the fixed support
or finite ambient chamber list. It does not disprove a bound
depending on the actual degrees, nor construct a pair for C0.
The desired new theorem would have to account for those degrees
and the global coefficients sustaining the additional centers.

**Comparative decision and stopping.**
The exact Cox ring is useful available global input. Its finite
generation, the automatic affineness of a complement pencil,
and per-ideal principalization do not themselves supply a
construction or an unrestricted obstruction. Asking for a
relative algebra is also not a construction unless it is
identified with this exact complement.

For existence, an independently supplied map or embedded
operation remains sufficient to select a test. For nonexistence,
the next comparison must constrain the selected pair's additional
centers or full fiber boundary together with their global degree
cost, beyond the inherited first-blowup inequality. The current
results supply neither a positive residual-degree floor nor a
reduction of arbitrary pairs to powers of I. No chamber, affine-
fiber, power or normal-form classification is selected.

The scouts /root/affine_fibration_global_selection and
/root/formal_ambient_contraction_selection used fresh
gpt-6-astra/xhigh contexts. The independent reviewer
/root/ambient_fibration_strategy_challenge used gpt-6.1-sol/high,
checked the primary hypotheses, reconstructed the Cox
specialization and equalized-pencil control, and then proved
the cohomology formula independently. The printed
codimension-(d-1) scope of the symbolic-Rees theorem and the
local-only conclusion of Cowsik's criterion were corrected
before reliance. No nested delegation or computation was run.

**Final written-artifact review: scoped PASS.**
The reviewer checked the proof note, this section and the new
literature-ledger entry. One dimension ambiguity was corrected:
the special-fiber algebra has dimension three and its Proj is
two-dimensional. The actual fiber description was also clarified.
The reviewer then verified the corrected states at SHA256

    7b6c7a7fd8115efb67819cf3dd6cc2f561883d9799593058c4423afa8c33874b
    research/notes/2026-10-31-cox-fiber-and-power-defects.md

    a9a9a10be67c3f56f10a989ebafd94ac0b3600b2408295690d8fd7e14850f6d6
    research/notes/2026-10-31-unrestricted-strategy-assessment.md

The proof, characteristic-free cohomology generalization, source
qualifications, cone-vertex interpretation, inherited-versus-extracted
status and stopping decision pass within their stated scopes.
The assessment fingerprint precedes this review record; subsequent
changes only record the review state. All three assignments are
complete and no new task is assigned to these contexts.
No canonical promotion or unrestricted STCI conclusion follows.

## 32. Residual maps retain the equations; the nonnormal quintic exclusion expands

This checkpoint reassesses the unrestricted characteristic-zero
question using the once-linked curve of an arbitrary defining pair
and the completed parallel quintic theorem. It selects neither a
Buchsbaum classification nor the next quintic singularity stratum.
The fresh independent challenge supports preserving the exact
geometric dictionary and a rational-curve generalization, without
a further technical experiment.

**The all-pair residual interface is already developed.**
Let \(Y=V(F_a,G_b)\), \(A=a+b\), and
\(I_D=(F_a,G_b):I_{C_0}\). The
[reviewed residual construction](2026-10-28-residual-liaison-construction.md)
already proves, for every proper pair with \(a,b\ge4\),
\[
\deg D=ab-4,\qquad
p_a(D)=\frac{(A-4)(ab-8)}2,\qquad
M_D=k(5-A).
\]
The last module has its unique nonzero degree at \(A-5\).
For a hypothetical supported CI, the generic transverse algebra
of D is the Artinian Gorenstein algebra of Y modulo its socle:
\([D]=(ab/4-1)[C_0]\). D is then a supported multiple curve,
not a residual component outside C0.

The existing source also gives the full minimal resolution,
low-degree equation recovery, flat colon families through
multiplicity changes, and applicable ambient-Hilbert-scheme
unobstructedness. Recognizing a diameter-one Rao module adds
none of these results anew. Smoothness of the ambient Hilbert
scheme does not establish existence of its required fixed-support
and fixed-partner locus.

**The retained geometric extraction identifies the actual maps.**
The added [bundle interpretation in §4](2026-10-28-residual-liaison-construction.md#october-31-geometric-extraction-a-fixed-bundle-still-retains-the-equations)
writes the existing resolution using
\(\mathcal E=T_{\mathbf P^3}(-2)\oplus\mathcal O(-1)\):
\[
0\to\mathcal E\xrightarrow{\Phi}
\mathcal O(b-3)\oplus\mathcal O(a-3)\oplus\mathcal O^3
\to\mathcal I_D(A-3)\to0.
\]
Its fixed three-row block has kernel \(\mathcal O(-3)\) off C0.
The two remaining rows restricted to that kernel are exactly
\(G_b,F_a\), up to sign and order. Hence full fiber rank off C0
is equivalent to absence of common zeros there. Mere sheaf
injectivity is already true for every proper pair and does not
exclude residual curves.

The [recovery generalization, §2.2](2026-10-28-residual-liaison-construction.md#22-equation-recovery-for-every-smooth-rational-space-curve)
holds for every smooth rational embedded curve C of degree d,
in every characteristic:
\[
(I_D)_n=(I_Y)_n\quad(n\le a+b-4).
\]
Indeed \(H^0(\omega_C(t))=H^0(\mathcal O_{\mathbf P^1}(dt-2))=0\)
for \(t\le0\), and the CI ideal has no first cohomology.
When \(a,b\ge4\), this recovers both equations and the marked
partner. This generalizes equation recovery, not the quartic's
specific Rao module, resolution or family claims.

**The literature provides constructions, but does not impose this support.**
[Nagel, Theorem 1.2, Corollary 5.4 and Remark 5.5(ii)](https://arxiv.org/pdf/math/0212217)
does supply locally free presentations and a bundle-section
interpretation for arithmetically Buchsbaum schemes. Its output
does not prescribe the radical and marked linked partner.
[Kleppe, §2.1 and Theorem 5.10](https://arxiv.org/pdf/1111.7020)
gives the Rao/Koszul presentation and component/generization
information through Betti data; those deformations can change
the support and required low-degree equations.
[Hartshorne, Theorem 2.4(b)](https://arxiv.org/pdf/math/0302078)
gives a descending elementary biliaison for a nonminimal member
of its class. The descending divisor and partner need not retain
this support or linkage flag. Reversing that operation still
requires actual divisors and maps with the desired common zero set.
The checked theorems therefore do not select a new supported
construction, although their constructive content is genuine.

**The quintic completion is a substantive class exclusion.**
At source commit fd9e628, the
[completed parallel theorem](2026-10-31-quintic-gorenstein-normalization-exclusion.md)
excludes every integral nonnormal quintic with Gorenstein
normalization as a defining carrier for C0, for every positive
mate degree and every full conductor scheme. Its integrated
review is recorded in source §6. This assessment reuses that
reviewed provisional evidence; it does not re-audit the proof
or rerun the first-jet certificate.

Compared with §27, the added cases include reducible conductors
with all multiplicities and the remaining conductor supported on
one line with multiplicity five. In this actual source, the root
divisor denominator forces conductor components through the marked
non-Cartier point. Its quadratic conductor algebra, contact
constraint and purity turn supported power descent into descent
of the forbidden quartic root. The single-line case uses its
actual canonical-module type and A4 contact.

The reusable method combines divisor-denominator incidence,
local conductor action and global purity. Arbitrary carriers do
not come with these same divisor, incidence or quadratic-algebra
data. The theorem leaves normal quintics and non-Gorenstein
normalizations outside its scope, as well as other degrees.
The earlier all-degree differential trichotomy remains unchanged:
generic singularity along C0, a singularity of the normalization
on its inverse curve, or singular full-conductor contact can
supply the surviving defects. It gives no opposing upper budget.

**Comparative recommendation and stopping conditions.**
For existence, a supported residual with the actual fixed block
and required fiber rank would work; the new presentation does not
construct it. For nonexistence, the fixed module or bundle alone
does not obstruct those maps. Likewise the completed quintic
theorem excludes a larger source without reducing arbitrary
pairs to that source.

This checkpoint selects no Betti-tuple, liaison-chain,
next-quintic-stratum or local-conductor classification. Reopen for
an actual operation controlling the marked partner and common
zero set, or a defined comparison of the actual conductor objects
that imposes a new all-pair constraint. Stop if the proposed
operation forgets that incidence, substitutes sheaf injectivity
for fiber rank, or only re-encodes the two original equations.
Unrestricted STCI existence remains live.

The residual scout /root/universal_residual_liaison_selection
used a fresh gpt-6-astra/xhigh context. The bounded carrier-impact
assessment /root/quintic_completion_global_assessment used
gpt-6.1-sol/high and reused recorded proof-review evidence.
The fresh independent challenger
/root/residual_and_carrier_strategy_challenge used
gpt-6.1-sol/high, checked the primary theorem statements,
reconstructed the bundle and rational-curve deductions, and
corrected the sheaf/fiber injectivity distinction before reliance.
No nested delegation or new computation was performed.

**Final written-artifact review: scoped PASS.**
The independent reviewer checked both source additions, this
assessment and the ledger entry, finding no mathematical
correction necessary. It inspected source SHA256

    067684ab756489a0a620f34027bec07823c309ecbe63023bf8a452f752e0fd48

and assessment SHA256

    0d6615a28e746abf8d6a7135adf271a0444bc5dfad4df66fc85d2c237a89f734

The parent then corrected a duplicate equation label in the source
to (2d), clarified that this checkpoint's nonselection does not
override separately owned parallel work, and added review records.
No mathematical claim changed. The source audit identifies the
resulting source fingerprint and the exact editorial difference.
All three bounded assignments are complete. The carrier proof
review is reused at its recorded scope, not represented as a
new independent proof audit. No canonical promotion or
unrestricted STCI conclusion follows.

## 33. Finite maps repackage the pair; supported closure does not force residual support

The [finite-map and cover-moduli check](2026-10-31-finite-maps-and-cover-moduli.md)
tests two global mechanisms against the full characteristic-zero
question. Its elementary deductions are useful clarifications,
not an additional STCI obstruction. Independent proof, source-scope
and written-preservation reviews pass within the stated scopes.

**Exact gain and limitation.** An STCI in projective space is
exactly a reduced inverse image of a linear space under some
finite endomorphism. For a supported pair on C0, the explicit
completion is
\[
[F^b:G^a:x_0^{ab}:x_3^{ab}].
\]
The construction already needs F and G. Its additional power
ramification factors out, leaving precisely the relative
Jacobian of the existing finite pencil. Total-invariance
theorems do not apply: the target is a line, different from C0.
This closes the proposed completion shortcut, not finite-map
methods generally.

The second extraction is constructive. Any already embedded
finite flat thickening over a nonempty open part of the pencil,
with reduced support C0 there, has a unique flat scheme closure
in the pencil's plane bundle. The closure is supported on C0,
misses the exceptional divisor, and descends to a locally CM
thickening in the original P3. The argument generalizes to any
curve disjoint from the axis of a finite linear pencil.

Thus support itself is preserved by closure. Gorenstein fibers,
the required splitting, canonical duality and two global equations
need not be preserved. A residual-at-infinity argument must
concern extensions of the equations with these conditions,
not arbitrary extensions of the supported scheme. This locates
the missing bridge at the actual ambient ideal, in the user's
curve/surface/map/ambient compatibility picture.

**Literature changes the proposed moduli premise.** Poonen's
affine algebra space requires a global basis; the pencil's
nontrivial vector bundle instead uses a frame bundle and
change-of-basis action. Benoist supplies complete families
inside the punctual binary-CI locus, including rational
examples for consecutive unequal degrees. Complete base
therefore does not automatically force a non-CI fiber.
The checked Hurwitz properness requires generic étaleness,
and branchvariety properness requires reduced sources.
Neither applies to the full nonreduced hypothetical CI.
The proof note records the exact statements and primary links.

**Comparison with the strongest recent gains.** The new all-pair
conductor postulation bound in §28 and the completed quintic
exclusion in §32 remain actual necessary conditions or class
exclusions. The former lacks a conflicting upper bound; the
latter lacks an exhaustive reduction of arbitrary pairs.
Sections 31–32 identify exact section defects of specified
sources and recover equations from residual maps. This check
does not turn those scoped results into an unrestricted bound.
It adds a positive closure operation and removes two false
shortcuts, leaving the global equation problem open.

**Recommendation and stopping conditions.** No further technical
test is selected from either mechanism. Existence would follow
from one actual ambient construction whose supported closure
has the required global ideal. The checked theorems do not
produce it. Nonexistence would require a comparison applying
to every embedded pair or to an exhaustively reduced class;
neither the old different nor abstract moduli supplies one.

Reopen for an actual operation on ambient sections or ideals
which preserves support and controls their global defect, or
a precise new inequality on the same full embedded object.
Stop if the input is simply the missing pair, if reduction
replaces the full nonreduced cover, or if total invariance,
global framing or boundary positivity is assumed without proof.
No map-degree, Artin-algebra or endpoint classification follows.
This decision does not override the separately owned carrier
investigation recorded in FRONTIER.

**Independent challenge and preservation: scoped PASS.**
The two scouts used fresh gpt-6-astra/xhigh contexts; the
independent challenger used fresh gpt-6.1-sol/high. The latter
reconstructed the deductions, checked the primary-source
hypotheses, and explicitly challenged nonselection for an
overlooked construction. It confirmed the stronger elementary
closure operation without requiring Hilbert–Chow, but found
no source-backed control of the remaining global ideal.
Its written review found no material correction.

The reviewed assessment SHA256, before review metadata, was

    985848ad71c549d6bcf0151bf2ccc3e9df4c674d1552b257c80606c68c1f7c32

The ledger state was

    83842cc611b145ce7b53725f5f0eed4c28bd86691898158e14a88487026de27d

The [source §6](2026-10-31-finite-maps-and-cover-moduli.md#6-independent-review-and-disposition)
records its exact reviewed state and subsequent metadata/citation
changes. No nested delegation or new computation was performed.
All three assignments are complete; these contexts are not
reused for a broader investigation. No canonical promotion or
unrestricted mathematical status change follows.

## 34. Patching and quantization retain a global presentation gap

This checkpoint tests two mechanisms suggested by §33's supported
closure: patch actual affine equations, or use the full contact
identity to obtain equations through quantization. A fresh
independent challenge confirms positive smooth-cone flexibility
and two precise limitations. It selects no further classification.
Proof, source-scope and written-preservation reviews pass.

**Stable patching sees only the determinant, once a matrix exists.**
The actual overlap of the hyperosculating affine charts has ring
\[
R=k[u,v,w,w^{-1}],\qquad
u=x_1/x_0,\ v=x_2/x_0,\ w=x_3/x_0.
\]
[Bass–Heller–Swan, Theorems 1–2, pp. 62–63](https://numdam.org/item/PMIHES_1964__22__61_0.pdf)
and polynomial homotopy invariance give
\[
K_1(R)=K_1(k[u,v])\oplus K_0(k[u,v])
      =k^\times\oplus\mathbf Z.
\]
The units \(cw^n\) represent both summands. Thus determinant
detects the entire stable class: an already constructed
\(M\in GL_2(R)\), after diagonal determinant correction, is
stably elementary. This does not construct M, factor it in
rank two, preserve its chosen section, or control degrees.

The independent reviewer supplied a concrete missing-premise
check. The reduced affine pairs
\[
(f,g)=(v-u^3,w-u^4),\qquad
(h,j)=(u/w-v^3/w^3,\ 1/w-v^4/w^4)
\]
generate the same reduced ideal on the overlap. Along their
support \(v=u^3,w=u^4\), differentiating in the conormal
basis \((f,g)\) gives
\[
\binom h j\equiv
\begin{pmatrix}-3u^{-6}&2u^{-7}\\-4u^{-7}&3u^{-8}\end{pmatrix}
\binom f g\pmod{(f,g)^2}.
\]
The determinant is \(-u^{-14}\), whereas every ambient unit
restricts to \(cu^{4n}\). Hence no ambient invertible matrix
relates these pairs, despite equality of their full ideals.
Geometrically this is the familiar degree-14 normal determinant
versus ambient degree-four polarization. It concerns the
reduced curve; a thick CI has a different conormal determinant.
This control explains why stable K1 cannot be started from
equality of ideals. It is not a new unrestricted exclusion.

[Keshari–Tikader, Theorem 1.2](https://arxiv.org/pdf/2307.02441)
does lift a prescribed conormal orientation to the same full
affine ideal under a monic-localized lifting hypothesis. Its
bound \(2n\ge d+3\) fails for rank n=2 over the dimension-two
coefficient ring used for an affine three-space chart. Its
Corollary 2.10 also requires two comaximal elements of one
affine ring, unlike x0,x3 in the homogeneous coordinate ring.
Neither result supplies the weighted projective presentation.
The inherited [two-chart criterion](2026-10-30-four-streams-affine-endpoints.md#1-once-actual-split-sections-glue-the-missing-line-is-not-an-extra-obstruction)
already proves that actual split sections would suffice.

**Quantization gives a positive smooth compatibility result.**
The [contact-note continuation, §6](2026-10-31-contact-global-consequence.md#6-quantization-of-the-smooth-cone-and-a-supported-cohomology-limit)
shows that every line bundle on the smooth punctured quartic
cone admits a formal Moyal-module quantization. Picard torsion
kills its Atiyah–Chern classes; the global Moyal splitting and
symmetric second coefficient give zero truncated Atiyah class. The argument
generalizes to smooth rational Legendrian curves, with the
same constant symplectic ambient hypothesis.

This is an actual positive application of the smooth theorem.
It quantizes a line bundle on the reduction, not the structure
sheaf of an arbitrary thick intersection. The source also
computes rational support cohomology of the full affine cone,
including its vertex: only degree four survives. Therefore
the checked rational supported trace-density vanishing test
would be automatic even if a full quantization were supplied.
Integral degree-six torsion Z/4 survives, so the conclusion
does not exhaust all refinements. Both calculations extend
in their stated scopes, without a new STCI constraint.

**A constructive theorem does not preserve the needed filtration.**
The reviewer also checked Stafford's actual cyclicity and
two-generator algorithms through Leykin. These give genuine
Weyl-module operations, but two operator generators can have
principal symbols cutting out a larger support than the
associated graded ideal. The contact note retains an elementary
example exhibiting the cancellation. Formal-to-filtered
algebraization and control of the two principal-symbol radicals
are both missing. No operator search is selected on the basis
of the two-generator theorem alone.

**Comparative decision.** Existence remains possible: neither
smooth contact quantization nor stable patching produces an
incompatibility. The positive quantization removes a proposed
smooth obstruction, while the explicit transition control
locates a real failure for reduced presentations. Neither
extends automatically to the full thick object.

The separately owned [genus-two carrier continuation](2026-10-31-quintic-genus-two-toric-source.md)
has meanwhile supplied a more concrete existence source: a
non-Gorenstein toric normalization with the marked quartic and
an actual quartic root upstairs. Its first finite projection
has five extra inverse points, so that center fails every
mate; the proposed variation retains the source and marked
curve and tests precisely this inverse-support defect.
The note also extracts the general bound \(a\le dr\) for an
integral carrier generically regular along C, with an actual
sole-supported mate, whose resolved normalization
has a connected general fiber of hyperplane degree
\(r<d=\deg C\), using an actual mate's effective total transform.
Under these hypotheses, C0 and conic fibers exclude a at least nine.
These are reviewed provisional findings in source §§2–3,6–7;
this assessment reuses that recorded review without rerunning
its proof or certificate. The source does not exhaust arbitrary
carriers. Its actual marked projection is a better-defined
construction test than a new stable or rational invariant
classification; its continuation remains with its existing owner.

Stop these bounded selections after preserving their deductions.
Reopen for an actual section-preserving, degree-controlled
patching operation, or a filtered module construction whose
two principal symbols have exactly the required radical.
For nonexistence, a finer detector needs a proved implication
from every full supported pair and a nonautomatic value.
An unstable or equivariant invariant is not selected simply
because the stable or rational detector loses information.
No matrix, degree, operator or local-thickening classification
follows. This decision leaves the separately owned carrier
investigation unchanged.

**Independent challenge and written preservation: scoped PASS.**
The patching scout used a fresh gpt-6.1-sol/high context; the
quantization scout used fresh gpt-6-astra/xhigh for the
nonreduced/smooth comparison and new implications. A fresh
gpt-6.1-sol/high challenger reconstructed the deductions and
checked the sources, including the later Baranovsky–Huey
paper and constructive Stafford algorithms. It supplied the
reduced transition control and integral torsion qualification,
and challenged the possible constructive bridge through Weyl
modules. Neither candidate supplied a justified next test.

The main written review found no material correction. Its
assessment fingerprint, before metadata and the later
parallel-carrier paragraph, was

    6a093da15be522f1788a3bfc0a0eb1f8b4f7f97a4d37ba0ac8975aab9aca9f32

The added carrier paragraph received a separate scope review.
That check required explicit generic regularity and the
connected general fiber; after correction it passed at

    1b70e8bb586411e69b34bfe1c9780c054d0e71daae49636269825ee5a6056587

The parent then made the source's integral-carrier,
sole-supported-mate and same-hypotheses qualifications literal,
without changing the scoped conclusion. This paragraph reuses
the parallel source's proof evidence, rather than re-auditing it.
The parent also made the two suggested wording clarifications
and updated status records. The
[contact audit, §6](2026-10-31-contact-global-consequence-audit.md#6-october-31-quantization-and-support-cohomology-continuation)
identifies the proof state and exact review boundary. No
computation, nested delegation or canonical promotion occurred.
All three assignments are complete and their contexts are
retired from further research.

## 35. General genus bounds and normalized-blowup positivity leave the ambient problem open

This bounded comparison asks whether the full multiple curve's genus,
or positivity on the blowup of its actual ideal, supplies the missing
upper capacity for concentration on C0. The sources apply to the full
scheme, but the checked bounds accept every surviving degree pair.
The new geometric extraction is a componentwise multiplicity identity.
Its proof, stopping recommendation and written preservation have
passed independent review within their provisional scope.

**The general nonreduced genus bound has strict room.**
Let Y be a hypothetical CI of type (a,b), with 5<=a<=b, supported
on C0. Its degree is D=ab and its least containing-surface degree
is s=a. This s belongs to Y, not to its reduced quartic, which
lies on a quadric. [Beorchia–Lella–Schlesinger, Theorem 1.1](https://arxiv.org/pdf/1806.08731)
recalls the bound, valid for every locally Cohen–Macaulay space
curve when D>=2s+1,
\[
p_a(Y)\le B(D,s)=\binom{D-s}{2}-\binom{s-1}{3}.
\]
It makes no primitive or normal-flatness assumption. For a CI,
\[
B(ab,a)-\left(1+\frac{ab(a+b-4)}2\right)
=\frac{a(a-1)}6(3b^2-9b-a+8)>0,
\]
because the last factor is at least (3a-4)(a-2)>0.
Thus it excludes no surviving pair, even before additional
support conditions are considered.

The literature has advanced beyond the conjectural sharpness
statement in the 2018 paper: [Sammartano–Schlesinger, Theorem 1.1](https://arxiv.org/pdf/2501.00809)
proves sharpness throughout D>=2s+1 (and D=s), in characteristic
zero. Its multiple-line and biliaison constructions do not impose
fixed C0 support or the required arithmetic Gorenstein structure.
Consequently no bound using only D and s in the full locally CM
class can close this gap. A support-sensitive theorem remains
possible. A test depending only on the usual CI Hilbert series,
resolution or canonical twist also accepts ordinary smooth CIs
of the same type; the marked support must enter essentially.

**The normalized blowup accounts exactly for every component.**
The [blowup-note §10](2026-10-28-residual-degree-blowup-bounds.md#10-normalizing-the-blowup-of-the-full-ci-preserves-its-component-multiplicities)
proves, for every proper CI in P3 in every characteristic,
\[
[Y]=\sum_jm_j[C_j],\qquad
\nu^*E=\sum_i\rho_iD_i,\qquad
\sum_{i\ {\rm over}\ C_j}\rho_i[k(D_i):k(E_j)]=m_j.
\]
Here E is the exceptional divisor of the actual CI-ideal blowup,
E_j its reduced component over C_j, and nu its finite normalization.
The proof uses the projective-line bundle over full Y, not just its
reduction. It also applies to lci curves in any smooth threefold.
Every normalized Rees divisor is centered on an actual curve
component; point-centered divisors on further resolutions are a
different issue. The weighted sums recover ab and the exact full
residual-cycle degree. They do not create or force residual support.

For L=O(b), [Ein–Lazarsfeld, Proposition 3.1](https://arxiv.org/pdf/math/9810004)
bounds the unweighted center sum by \(b^3\). The component identity
already bounds it by \(ab^2\). The reviewer also checked their
Remark 3.2: its subtracted intersection number is \(b(b-a)^2\),
leaving \(ab(2b-a)\ge ab^2\). This stronger published version
therefore adds no constraint either. These are bounds for every
proper pair, with or without residual components.

At the generic point of C, put m=length(O_Y), q=min(ord F,ord G)
and c=lct(I_Y). [de Fernex–Ein–Mustaţă, Theorem 0.1](https://arxiv.org/pdf/math/0205171)
gives c>=2/sqrt(m), while the first exceptional divisor gives
c<=2/q. Even [Demailly–Hiệp, Theorem 1.5](https://arxiv.org/pdf/1201.4086),
over the complex analytic transverse surface, gives only m>=q squared
after comparison. [Kaveh–Khovanskii, Theorem 9.1](https://arxiv.org/pdf/1310.7979),
applied to the two primary ideals I_Y and the maximal ideal, gives
the same inequality. It cannot be applied as stated to the two
individual principal ideals. These bounds are weaker than the
existing m>=ord(F)ord(G), so none controls later surviving contact.

**Recommendation and stopping conditions.**
Stop both mechanisms at these deductions. No genus-type, valuation
tree, threshold or degree classification is selected. Reopening
requires a specified input that uses the fixed embedded support:
an upper bound on the allowed full normal/contact budget, a
comparison forcing a positive genuine residual degree, or an
operation producing compatible global equations. Naming such a
missing theorem alone does not justify another technical round.

This leaves existence and nonexistence live. An actual construction
needs only one successful pair; exclusion needs an implication valid
for every pair or an exhaustive reduction. The separately owned
marked carrier construction in §34 retains a concrete inverse-support
test, and is not extended or reclassified here. The present result
clarifies the passage from local multiplicity to ambient intersection
geometry without settling it. The unrestricted characteristic-zero
question remains open.

**Independent review.** The genus selection used a fresh
gpt-6-astra/xhigh context for the nonreduced bound and current
sharpness theorem. The birational applicability selection used
fresh gpt-6.1-sol/high, as did the independent challenger. The latter
reconstructed the componentwise proof, its residual-inclusive
generalization and the polynomial gap, and checked the immediately
available stronger positivity bound before endorsing the stop.
No nested delegation or numerical search was used. These bounded
assignments are complete; their contexts are retired from further
research. All new deductions remain provisional.

The final written-preservation review found no material error.
The parent adopted its suggested explicit exponent notation.
The [blowup audit, §8](2026-10-28-residual-degree-blowup-audit.md#8-october-31-addendum-normalized-ci-ideal-blowups-and-genus-selection)
records the exact pre-metadata states and scope. No canonical
promotion or unrestricted status change follows.

## 36. Pencil unions give a normal-degree Milnor bound; orbit closure supplies no presentation

The selection after §35 examined actual global pencils and
support-preserving torus limits. It yielded one new all-pair
necessary inequality, rather than another singularity classification.
The [pencil proof](2026-10-31-pencil-milnor-budget.md) is provisional;
independent proof challenge and written-preservation review pass.
The subsequent §37 comparison shows that its inequality is already
implied by a stronger local bound for C0. This section records the
initial extraction, not an additional surviving quartic constraint.

**New geometric implication.** For any smooth connected support C
of degree d and genus g, equalize a hypothetical defining pair to
degree D, retaining the powers. Let m=D^2/d and let mu be the
generic transverse Milnor number of a general pencil member.
Then
\[
dD(m+1-\mu)\ge(\deg N_{C/\mathbf P^3})m.
\]
For C0 this is mu<=D^2/4+1-7D/8. The argument uses unions of
k general members of that same pencil. Their pairwise transverse
intersection length is m; their polar degree follows by
inclusion–exclusion. The nonnegative special-point vanishing-cycle
correction is a quadratic polynomial in k, whose leading
coefficient must be nonnegative. Thus full contact and the
embedded normal degree enter the same inequality.

The proof retains all exceptional points and monodromy through
Siersma–Tibăr's nonisolated-singularity theorems. It needs no
smooth carrier, normal-flatness, saturated first relation or
balanced normal bundle. It transfers from C to algebraically
closed characteristic-zero fields, and further power equalization
does not improve it artificially. The line control attains equality.
No claim of literature priority or independence from every existing
normal budget is made.

This adds a condition for any actual construction, but no checked
global input forces mu above it. Large local intersection length
can coexist with small mu. The correction is a vanishing-cycle
quantity on surfaces, not a residual curve. A proposed comparison
with first normal orders, conductor or higher-contact budgets must
prove that comparison before using it.

**Torus and GIT selection stops.** The existing full torus limits
retain support and Hilbert polynomial while potentially losing AG
and the two-equation presentation. The newly checked
[Bertone–Cioffi–Orth–Seiler, Corollaries 5.5 and 6.18](https://www.mathematik.uni-kassel.de/~seiler/Papers/PDF/Loci.pdf)
give open AG/strict-CI loci and constructive recognition algorithms.
They do not preserve these loci at a flat boundary. The reviewer
checked that those algorithms would require an actual specified
boundary ideal and a support-constrained deformation with the
necessary generator conditions, neither supplied here.

[Hattori–Zanardini, Theorem A.1](https://ems.press/content/serial-article-files/50397)
passes from Chow stability of an already proper equal-degree CI
to stability of its generating system. It supplies no converse
preservation. Their Corollary 4.5 constructs stable systems with
a common hypersurface factor. Therefore GIT stability alone does
not even retain proper intersection. Fixed Chow cycles forget
the embedded nilpotent structure; no Hilbert-boundary campaign
is selected.

**Source correction affecting possible affine input.** A separate
independent check found a proof gap in Mandal–Zinna arXiv:2511.07589,
Theorem 4.2 Step 3: tensoring the Serre sequence yields J/cJ,
not the image ideal J/(c). The omitted term is nonzero even for
J=(x,y), c=x in a polynomial ring. The stronger affine statements
remain claims of that preprint with this identified gap; the
[literature ledger](../LITERATURE_LEDGER.md#mandal--zinna-2025-preprint)
records the exact witness and scope. The classical affine-space
result and the explicit affine quartic presentations are unaffected.
This is not a claim that every theorem in that preprint is false.

**Recommendation and stop.** Complete and preserve the general
Milnor deduction, then stop both selections. Reopening needs
a specific global lower bound conflicting with its upper budget,
an operation producing compatible ambient equations, or a
support-preserving deformation with independently controlled
global generators. No degree, spectrum, local-algebra or
boundary classification follows. Existence remains possible.
One successful construction suffices; restricted failures still
require an exhaustive reduction to imply nonexistence.

The orbit/source synthesis used fresh gpt-6-astra/xhigh; the
pencil-source selection, separate affine proof check and fresh
independent strategy/proof challenge used gpt-6.1-sol/high.
The reviewer verified the new inequality and challenged both
nonselection and possible constructive input. No nested delegation
or computation campaign occurred. The final written review found
no material correction; [source §5](2026-10-31-pencil-milnor-budget.md#5-independent-review)
preserves its exact states and scope. The assignments are complete
and their contexts retired. No canonical status change follows.

## 37. The Milnor inequality is locally automatic for C0

The next comparison resolves the previously explicit uncertainty
about the force of §36. The global polar proof is valid, but its
inequality adds no transverse restriction for the quartic. The
[pencil-note §6](2026-10-31-pencil-milnor-budget.md#6-cluster-interpretation-and-a-stronger-local-bound)
preserves the exact local geometry and proof.

At the geometric generic point of C, let I=(P,Q) be the parameter
ideal and principalize it as I O_X=O_X(-Z), with
Z=sum rho_i E_i. Put epsilon_i=-Z.E_i>=0 and let A_i be the
log discrepancy. The original pencil gives the morphism on this
resolution; epsilon_i is its degree on a dicritical divisor.
For T=m+1-mu, the exact identities are
\[
m=\sum_i\varepsilon_i\rho_i,\qquad
T=\sum_i\varepsilon_iA_i.
\]
Thus T/m is a weighted average of discrepancy/order ratios,
at least the log canonical threshold c. Combining this with
the published local inequality mc^2>=4 gives
\[
T\ge2\sqrt m.
\]
For C0 this is T>=D, stronger than the global bound T>=7D/8.
The same redundancy holds whenever deg N_C<=2d^(3/2).
This comparison is uniform; it does not enumerate valuations.

The base-cluster formulas also make the user's normal-direction
picture precise: m=sum n_p^2, while
T=sum n_p+b=2n_0+sum of n_p at nonorigin free points.
Here b counts geometric branches. Satellite multiplicities cancel
in this last linear expression, although they still contribute
to contact. Residue degrees are retained by geometric generic
base change. The existing first-blowup bound controls instead
the quadratic total sum_{p!=0} n_p^2. Combining that inherited
bound with the equality case of the local theorem gives T>D,
or T>=D+1 for a hypothetical quartic pencil. This is an existing
global restriction combined with local theory, not extra force
from the polar argument.

**Constructive input exists locally.**
[Lipman–Watanabe, Theorem 1.1 and Corollary 1.1.2](https://www.math.purdue.edu/~jlipman/papers/2dmult.pdf)
construct complete transverse ideals from antinef exceptional
divisors. [Verma, Theorem 2.1 and Corollary 2.2](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/94C4B0C472F46CD24566F28AD01D4FB0/S0027763000003044a.pdf/joint_reductions_of_complete_ideals.pdf)
supplies local two-element reductions. These preserve the integral
closure and multiplicity, not an arbitrarily specified full
parameter algebra.

Campillo–Greuel–Lossen provide equisingular parametrization/equation
deformations with actual algebraic representatives; see
[Theorems 2.7 and 2.10](https://arxiv.org/pdf/math/0511407) and
[Theorem 4.2, Remark 4.3(4)](https://arxiv.org/pdf/math/0701002).
Their local constructive content must not be dismissed as only
formal. It supplies no homogeneous degree-D sections along the
fixed embedded quartic or control of their common zeros elsewhere.
Two separate local realizations also need not form the required
global pencil.

After global principalization of a proposed ideal K, the needed
operation would produce a basepoint-free pencil in
pi*O_P3(D) tensor O_X(-E), while retaining the selected transverse
reduction. Relative local generation does not do this. Increasing
D alone changes D^2=4m, so generation by many sections at large
twist is no automatic support-preserving two-section construction.
No such global operation is supplied by the checked sources.

**Recommendation.** Stop the Milnor-budget lane with its corrected
scope and retain its exact special-point identity and valuation
interpretation. Do not classify clusters to pursue an inequality
already true locally. A new selection needs an actual global
construction, or control of cluster and branch variation over C
that constrains the homogeneous equations beyond these generic
formulas. Both existence and nonexistence remain open.

The cluster comparison used a fresh gpt-6-astra/xhigh context;
the constructive applicability check and separate independent
proof/strategy review used fresh gpt-6.1-sol/high. The reviewer
reconstructed the local formula, inequality, proximity identities
and strictness corollary. No nested delegation, valuation sweep
or code execution was used. Written-preservation review passes;
[source §6](2026-10-31-pencil-milnor-budget.md#6-cluster-interpretation-and-a-stronger-local-bound)
records the exact reviewed states and scope. All three bounded
assignments are complete and their contexts retired. These
deductions remain provisional; no canonical status changes.
