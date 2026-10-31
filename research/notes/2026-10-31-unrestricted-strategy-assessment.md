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
