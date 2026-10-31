# Characteristic-zero STCI: geometric research integration

Date: October 30, 2026; continued October 31.
Branch: `codex/stci-char0-four-streams-2026-10-30`.
Research base: `317d5bc`; the consolidated branch was inspected at
`0b18029`. This is a research decision record, not theorem authority.

The question is whether
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k,
\qquad k\text{ algebraically closed of characteristic zero},
\]
is the reduced support of an intersection of two homogeneous surfaces.
No resolution is claimed. Any argument must allow arbitrary degrees,
shared singular points, carriers singular along the whole curve,
non-normal carriers, and non-flat normal filtrations, unless a reduction
has actually removed that case.

## Selection after the literature check

The user's selection criterion is geometric progress on the full question.
An expanding list of excluded subfamilies is not the target. Four initial
independent assignments examined quadric/blowup geometry, normalization
projections, thick structures, and normal-carrier indices. Primary-literature
checks preceded commitment to the revised directions.

The following sources materially changed allocation:

- [Jaffe, *Applications of iterated curve blow-up*](https://arxiv.org/abs/alg-geom/9410008):
  the finite degree list assumes the surfaces have no common singular
  points. It cannot be imposed on the unrestricted problem.
- [Hartshorne–Polini, *Quasi-cyclic modules and coregular sequences*](https://arxiv.org/abs/1907.05472):
  Theorems 3.1 and 4.5 and Proposition 4.2 give a carrier-independent
  necessary condition. The repository already uses it in P-024, P-037,
  P-039 and P-043; another finite quartic ancestor computation is not a
  fresh general approach.
- [Hellus–Hübl, *A general result on complete intersections with an application to the Macaulay curve*](https://arxiv.org/abs/1312.7661):
  opposite extreme-weight pieces obey strong necessary conditions.
  Their two-equation special fibers must be distinguished from Hilbert
  flat limits, which retain additional equations.
- [Manolache, *Gorenstein Multiple Structures on Smooth Algebraic Varieties*](https://arxiv.org/abs/0706.2204):
  duality concerns the appropriate canonical filtrations. It does not
  justify symmetry or saturation of every ordinary normal filtration.
- [Ellia, *Complete intersections primitive structures on space curves*](https://arxiv.org/abs/1409.3801):
  primitive hypotheses limit the numerical sieve. It does not remove
  simultaneous-singular or entirely thick structures.

These are sources for method selection, not new results. A bounded literature
search found no resolution; that is not proof that no unindexed result exists.

## First integration and changes of direction

1. **Quadric/blowup stream retired.** The existing
   [blowup geometry](2026-10-28-blowup-residual-geometry.md) and
   [graph bounds](2026-10-28-residual-degree-blowup-bounds.md) already give
   the exact all-pairs support criterion and the available nef inequalities.
   No additional uniform constraint was found. Repackaging those results
   would not be new progress.
2. **Projection enumeration deferred.** The primitive elliptic survivor
   is a precise constructive subproblem, but a degree-twenty passport
   enumeration would address one normalization source without a reduction
   from arbitrary carriers. The scout returned a handoff and stopped;
   no enumeration was run.
3. **Higher-index normal-carrier sieve retired.** The literature bounds
   retain singularity hypotheses. No uniform actual-index argument for
   arbitrary normal carriers was found. No new index table was generated.
4. **Entirely thick geometry retained.** The question is whether the actual
   embedded geometry supplies a uniform constraint beyond the known
   socle/normal-filtration budget. Isolated numerical cases are not the
   intended output.
5. **Opposite torus degenerations initiated in fresh context.** Test a
   universal geometric bridge using actual flat limits, fixed-point
   defects and the Cohen–Macaulay hull. A counterexample to the bridge
   is valuable only insofar as it prevents an invalid general inference.
6. **Geometric local cohomology initiated in fresh context.** Test whether
   a common cyclic ancestor has an intrinsic global duality or saturation
   interpretation, rather than extending the low-degree incidence search.

The two fresh research workers were explicitly requested as
`gpt-6-astra/ultra`; the bounded independent literature scout as
`gpt-6.1-sol/high`. Initial difficult workers retained the parent route.
Workers with completed retrieval or crowded context were stopped rather
than given another broad task. No nested delegation was authorized.

## Verification boundary

At this first integration there is no new accepted mathematical result.
Candidate counterexamples and proposed geometric bridges require fresh,
independent proof reconstruction. Neither agreement between workers nor
successful finite calculations can discharge that requirement.

## Second integration: novelty checks and the retained geometric question

The entire-thick and local-cohomology streams were retired after deeper
retrieval found the proposed canonical-defect bridge and its non-Gorenstein
counterexample already in the record:

- [October 6 local-cohomology progress, Sections 2–3](2026-10-06-session-localcoh-progress.md)
  already gives the faithful canonical-module map, finite defect and
  complementary Gorenstein/non-Gorenstein models.
- [October 5 generic-length note](2026-10-05-localcoh-generic-length.md)
  already disproves the implication from a full first-socle generator to
  fiberwise Gorensteinness of the ancestor's annihilator.
- [October 7 adversarial socle-bridge audit](2026-10-07-session-socle-bridge-adversarial-audit.md)
  distinguishes ancestor multipliers from equations annihilating that
  ancestor.

The new lower-length variant and a restatement of the standard transverse
Gorenstein test were discarded as duplicate contributions. The latter also
needed a correction: a thickening does **not** automatically carry a global
retraction to its reduced curve or an O_C-algebra structure. Finite freeness
is valid in completed local coordinates after choosing a lifted parameter.
No accepted repository proof was changed.

The [opposite-degeneration note](2026-10-30-four-streams-degeneration.md)
supplies the retained candidate contribution: full torus limits retain
sole support, with finite defects at the fixed points; an explicit
all-degree line example disproves several general defect-based shortcuts;
and the quartic's missing linear-coordinate class is unchanged on passing
from a limit to its pure Cohen–Macaulay hull. The last statement isolates
a geometric problem about prescribed lifts of the pure hull to P4.
These proposed proofs have been assigned to a fresh independent reviewer,
explicitly `gpt-6.1-sol/high`, rather than the proposing researcher.

Two fresh `gpt-6-astra/ultra` investigations now test broader consequences:
the nonlinear neighborhood and missing linear series, and resolution of an
arbitrary actual defining pencil. Neither is assigned a finite degree or
carrier family. Their stopping condition is a new uniform implication or
an explicit, evidenced reason the proposed bridge fails; a reformulation
does not count as success.

The next integration must record the literal statements that survive
review, their geometric meaning, and what changes for the unrestricted
question. A failed universal bridge must not be re-described as an
exclusion of the quartic.

## Third integration: independently checked geometric conclusions

Fresh independent proof reconstruction found no material correction in
three retained contributions:

1. [Opposite degenerations and pure hulls](2026-10-30-four-streams-degeneration.md),
   with [audit](2026-10-30-four-streams-degeneration-audit.md): for arbitrary
   hypothetical pairs, full torus limits keep sole support on C, while
   non-Cohen–Macaulay defects are confined to its endpoints. Removing those
   defects does not change the missing-coordinate lifting class. A family
   of actual supported line complete intersections demonstrates why
   positive defects in both limits are compatible with existence.
2. [First-neighborhood persistence](2026-10-30-four-streams-linear-series.md),
   with [audit](2026-10-30-four-streams-linear-series-audit.md): the omitted
   coordinate is obstructed already on V(I_C^2), by the actual projection
   normal extension. If both equations have normal order at least two,
   that neighborhood is retained in both limits and pure hulls. Therefore
   the nonzero class persists automatically in this entire branch. This
   resolves the proposed test in a way that **prevents** a nonexistence
   argument based merely on its nonvanishing. Quadric Cartier multiples
   of every multiplicity at least two supply lci/Gorenstein controls; their
   higher-twist Rao groups remain nonzero.
3. [Exceptional covers of unbounded genus](2026-10-30-four-streams-pencil.md),
   with [audit](2026-10-30-four-streams-pencil-audit.md): for d>=2, e>=1 and
   n=d(e+1), the two integral degree-n carriers
   G=Y^n+X^d(Z^(de)-W^(de)), F=G+X^n have sole support a line. Their unique
   normalized exceptional prime has normalization D times P1, where
   beta^d=1-t^(de) and g(D)=(d-1)(de-2)/2. This disproves automatic
   rationality or unramifiedness of the cover even for integral,
   equal-degree, entirely thick carriers. It gives arbitrarily large
   degrees, not every integer degree, and is not a quartic construction.

All three contributions remain reviewed provisional research, not canonical
promotions. They are geometric constraints or counterexamples to proposed
general implications. **None excludes all presentations of C0 or constructs
one.** Hand proofs, exact family calculations and independent reconstruction
provide the evidence; no numerical search or simulation was used.

## User-directed affine-endpoint continuation

The user suggested comparing the affine STCI presentations obtained by
removing either hyperosculating hyperplane, and using point valuations on
k(C) to control extension at infinity. A fresh worker was assigned that
question, with existing P-007 and the October 27 full-formal-section
equivalence supplied explicitly. Those results already locate the ordinary
leading-form and full fixed-twist compatibility requirements; neither is
being offered again as a new discovery.

The [affine-endpoint note](2026-10-30-four-streams-affine-endpoints.md)
and its [fresh independent audit](2026-10-30-four-streams-affine-endpoints-audit.md)
now establish the concrete specialization without fixing a carrier,
multiplicity or degree:

- Actual pairs on both entire affine charts, compatible as sections of
  O(a) plus O(b), extend uniquely to homogeneous equations. Any residual
  would lie on the omitted line, disjoint from C, contradicting connectedness.
- For any chosen affine radical pair on U0, let Y be its ordinary
  homogenization and m its generic thickness along C. Then
  \[
  Y_{\rm red}=C\quad\Longleftrightarrow\quad
  e_{p_\infty}(Y)=m.
  \]
  Here e is Hilbert–Samuel multiplicity. Equivalently the full completed
  endpoint ideal contains a power of the ideal of C. Connectedness forces
  every nonempty residual union to attach at that sole omitted endpoint.
- The reduced affine generating pairs cannot be related by an invertible
  matrix on the entire overlap: their conormal determinant is -t^(-14),
  whereas restrictions of ambient units have exponents divisible by four.
  This is a reduced-structure obstruction, not a higher-thickening theorem.
- The exact nonlinear transition and an explicit cancellation distinguish
  coefficient orders from the ambient degree valuation. Full fixed-twist
  formal gluing remains sufficient by the inherited theorem; finite jets
  and scalar orders do not establish it.

This is an application and sharpening of existing geometric principles,
not a claim to have discovered connectedness or formal algebraization.
Its relevance is an exact unrestricted target for the user's proposed
valuation direction. A strict endpoint inequality for **every** affine
supported pair would prove nonexistence; one equality pair would prove
existence. Neither has been obtained.

## Fourth integration: the two planes and Q as simultaneous test surfaces

The user clarified that the two hyperosculating planes should constrain
the actual defining surfaces together with Q, rather than serve only as
an affine cover. The [fixed-surface investigation](2026-10-30-fixed-surface-configuration.md)
and [independent audit](2026-10-30-fixed-surface-configuration-audit.md)
retain that full configuration. A fresh `gpt-6-astra/ultra` researcher
developed it; a separate `gpt-6.1-sol/high` reviewer reconstructed the
proofs. Both assignments ended at the stated mathematical stopping point.

Three conclusions change the next test:

1. For every r>=2, the proper pairs
   `(c0^r,c2^r)` and `(c0^r,c2^r+q*x0^(3r-3)*x3)` have identical
   actual equations on `D=Q union V(x0) union V(x3)`, including overlaps,
   yet generic thickness r^2 and r along C. For even r their degree
   products also satisfy the necessary divisibility by four. Thus the
   full fixed-surface schemes do not determine transverse thickness.
   This does not say that those fixed data have any STCI lift.
2. Every proper containing pair satisfying the two endpoint-plane
   conditions gives the finite flat projection `[x0:x3]`, of degree ab,
   with module `E = direct sum O(-i-j)` for 0<=i<a and 0<=j<b.
   Multiplication by q is a map `N:E -> E(2)`. The quadric intersection
   is its cokernel; under the common-Q-support condition, STCI is exactly
   nilpotence of N. This is a standard criterion applied to the entire
   pair, with no degree or carrier restriction. The algebra multiplication
   and its realization by the actual equations remain essential.
3. A tempting first-trace obstruction fails. The explicit proper pair
   `F=x1^4-x0^3*x3+q*x1*x2`,
   `G=x2^4-x0*x3^3+2*q*x1*x2` satisfies all three boundary-support
   conditions and has identically zero trace(q), but at x3/x0=1 its
   characteristic polynomial is `(T^4-T^2+T)^4` and trace(q^2)=8.
   Its residual sheets cancel in the first trace. The general first
   trace depends only on the two layers below the leading fiber forms,
   as proved by deformation and the Jacobian-weighted residue identity
   of [Cattani–Dickenstein–Sturmfels](https://arxiv.org/abs/alg-geom/9404011).

The last example tests an unrestricted proposed implication; it is not
another quartic exclusion. No higher-moment parameter scan is initiated.
The simultaneous fixed surfaces remain useful because they identify the
actual normal action that a complete compatibility argument must control.
Nilpotence is an exact formulation, not a new obstruction by itself.

## Fifth integration: actual Jacobians, contact geometry, and the tropical model

The next continuation tested finite-cover duality and checked primary
logarithmic/toroidal literature before opening further lanes. The latter
gave no applicable constraint on the missing normal action: the available
statements either concern reduced support or introduce pair-dependent
modifications without the needed global bound. No separate log-boundary
calculation was launched.

The [Jacobian/contact investigation](2026-10-31-cyclic-cover-duality.md)
and [independent audit](2026-10-31-cyclic-cover-duality-audit.md) yield an
actual equation constraint for every hypothetical characteristic-zero
supported pair. If Mij are the 2-by-2 gradient minors, all six generate
the socle sheaf and, in its twist O_C(6), recover the tangent Plücker
sextics. In particular
\[
M_{12}-2M_{03}\in(F,G),\qquad (F,G):M_{12}=I_C.
\]
The plane-pencil different is the nilpotent ideal
`S(-3p0-3pInfinity)`, not a Cartier ramification divisor on Z.
The first identity expresses involutivity for the contact structure
whose affine symplectic form is `dx0 wedge dx3 - 2 dx1 wedge dx2`.
It holds in the actual defining ideal, not only its radical.

The investigator was a fresh `gpt-6-astra/ultra` worker, with bounded
literature support and independent proof reconstruction by separate
`gpt-6.1-sol/high` workers. Review found that a proposed absolute-duality
normalization was not covered by the cited relative statements. An
elementary varying-projection argument replaced it, and the unnecessary
stronger assertion was removed. The revised conclusions pass review.
The relative Jacobian-socle input is credited to the existing October 14
proof, not claimed anew. A genuine Legendrian twisted-cubic STCI shows
why involutivity by itself cannot be a general nonexistence theorem.

The user then suggested tropical compactification and characteristic
comparison, without making that route compulsory. The
[tropical-model note](2026-10-31-tropical-model-characteristic.md) and
[independent audit](2026-10-31-tropical-model-characteristic-audit.md)
give a positive geometric statement: after the unimodular torus change
`(t,u,v)=(x1/x0,x0^2*x2/x1^3,x0^3*x3/x1^4)`, the whole curve is
`P1 times {(1,1)}` in `Y=P1 times G_m^2`, cut out scheme-theoretically
by u-1 and v-1. This is an actual schön tropical compactification in
every characteristic. Its morphism to P3 contracts the two boundary
tori, and the induced normal map `O_C^2 -> N_C/P3` has invariant
factors (3,4) at each endpoint. This gives an explicit geometric origin
for fourteen units of normal degree and retains their point valuations.
Clearing the two particular equations' denominators introduces a line;
this is not a proof that all choices must acquire residual support.

Characteristic two makes the reduced fourth-power cover inseparable.
Independently, characteristic dividing the generic thickness kills the
trace and relative Jacobian. The existing characteristic-seven (4,7)
construction supplies a concrete control with tame reduced cover and
zero trace. The tropical CI persists in characteristic zero, so these
observations locate rather than solve its projective descent problem.
The general tropical existence theorems establish a schön/lci model
after choosing a very affine open; the stronger global Cartier-STCI
claim for arbitrary curves is not settled by the checked sources.

## Sixth integration: full tropical movement and the Hamiltonian limit

The next allocation tested genuine consequences of the new contact and
tropical statements. Two fresh `gpt-6-astra/ultra` researchers worked on
separate geometric questions. A fresh `gpt-6.1-sol/high` reviewer checked
the tropical proof, while the earlier contact reviewer was reused for a
coherent bounded extension. Both revised source states passed independent
hand reconstruction. The assignments ended at those proved conclusions;
no degree-family or higher-moment search was opened.

The [full tropical-descent theorem](2026-10-31-tropical-descent.md), with
[audit](2026-10-31-tropical-descent-audit.md), adds a condition for every
hypothetical characteristic-zero supported pair. Close its full torus
scheme in Y=P1×G_m^2, saturating the entire ideal at both boundaries.
The result W is finite flat of rank m=ab/4 over the parameter t of C,
not over the earlier plane-pencil base. It is a finite modification of Z,
whose cokernel has endpoint lengths δ0,δInfinity. Its algebra B is
globally generated and has degree e satisfying
\[
\delta_0+\delta_\infty=e+m(2a+2b-7),\qquad e>0.
\]
The strict inequality says that the **entire embedded punctual scheme
must move**. Degree zero would make its multiplication and coordinate
sections constant; the image would be torus invariant and its saturated
CI ideal would admit two weight-eigenvector generators, contradicting
the inherited Hellus–Hübl condition. This uses the full Artin algebra,
not the conditional first-symbol movement parameter of earlier records.

Moreover W admits **no** scheme-theoretic presentation as the intersection
of two global effective Cartier divisors on Y. All line bundles on Y
are O(d), and nonzero sections require d>=0. Such a presentation would
give, by adjunction and finite-flat duality,
`2e = -m(d1+d2)`, forcing e=0. This is an all-presentations statement
upstairs, not an STCI contradiction downstairs. W can still be locally
a CI, and its reduced curve remains the global CI (u-1,v-1).

The actual endpoint subalgebras give weighted monomial bounds and
`0<e<=m(4m-2a-2b+3)`, but this coarse inequality leaves the surviving
degrees untouched. The inherited characteristic-seven example has
constant W=(v-1,(u-1)^7); the same equations in characteristic zero give
seven distinct constant sections. This directly contrasts constant
Frobenius thickness with the movement necessary in characteristic zero.

The [Hamiltonian continuation](2026-10-31-contact-global-consequence.md)
and [audit](2026-10-31-contact-global-consequence-audit.md) identify a
different boundary. In the entirely thick branch, the Hamiltonians
raise the nilpotent filtration, exponentiate on the punctured cone,
kill the whole socle, and force both homogeneous cofactors A,B to lie
in I_C. Their deformation complex consequently has an infinite-dimensional
socle contribution to its zeroth analytic stalks. Reduced-Lagrangian
constructibility/rigidity results cannot be imported. An actual entirely
thick twisted-cubic CI also has no commuting homogeneous generators of
its defining ideal. This closes those proposed shortcuts, not the branch.

The useful next question is whether a moving full punctual family can
have the required endpoint contractions and an actual homogeneous CI
image. Its normal algebra, contraction lattices and global equation
structure must all be retained. The positive movement and failure of
a split two-divisor presentation upstairs do not yet decide that question.

## Seventh integration: full conductor data and a moving all-multiplicity control

Two fresh `gpt-6-astra/ultra` researchers tested the full conductor
condition and the proposed incompatibility between movement and
Gorenstein endpoint contractions. Each received a bounded independent
`gpt-6.1-sol/high` audit. Both proofs passed hand reconstruction without
material corrections. All four assignments ended after their scoped
deliverables; no nested delegation or new degree enumeration occurred.
Primary literature on finite duality, canonical ideals, Ferrand pinching
and primitive multiple curves was checked before reliance.

The [conductor formulation](2026-10-31-tropical-conductor.md), with
[audit](2026-10-31-tropical-conductor-audit.md), keeps the source W
potentially non-Gorenstein. At either endpoint A⊂B, its actual conductor
c gives a finite Gorenstein algebra D=B/c of length 2δ and a unital
subalgebra E=A/c of length δ. A chosen Frobenius functional on A over
the parameter DVR gives a perfect residue multiplication pairing on D
with E equal to its orthogonal complement. The exact fiber product
A=B×_D E recovers the entire contraction. This is an application of
classical duality and pinching, now retaining the full finite boundary
schemes of this nonreduced modification. It is not a new theorem about
reduced normalizations or a claim of an STCI exclusion.

Globally the actual conductor module is
`pi_*c = B^vee tensor O(14−4(a+b))`. Its degree identity is exactly the
previous genus formula, so it gives no independent numerical constraint.
An explicit local CI with weighted saturation
`B=R[U,V]/(U²+t²V²,UV,V³)` has a non-Gorenstein special fiber but
Gorenstein conductor quotient: c=(t⁸,t⁶U), δ=15 and length(B/c)=30.
This prevents replacing the dualizing module of an arbitrary W by a
line bundle. The Frobenius functional is not the algebra trace, which
can degenerate on nilpotents.

The [moving-family construction](2026-10-31-moving-family-descent.md)
and [audit](2026-10-31-moving-family-descent-audit.md) resolve the
local-contraction test in the opposite direction from an obstruction.
The cubic
`S=V(x0²x2−x1³+x2³−x1x3²)` is smooth. For every m≥2 its Cartier
multiple Z_m=mC is locally CI, and its full tropical closure W_m is
locally CI with every fiber curvilinear. The section conormal changes
from O(−2) on S to O(6) upstairs; its quotient direction has degree
six. Hence
\[
\deg\pi_*O_{W_m}=3m(m-1)>0,\qquad
\delta_0=\delta_\infty=2m(m-1).
\]
Both exact endpoint images are `R[t⁴V]⊂R[V]/(V^m)`, using the actual
changed parameter z and V' at infinity. Thus movement, local CI
structure, curvilinear fibers and both Gorenstein contractions coexist
in every multiplicity. This is a control for a proposed universal
implication, not a new restricted STCI case to pursue.

The same images fail the global homogeneous condition for every m:
their least equation degree is three, while a hypothetical (3,b) CI
would require both 3b=4m and m=2b by degree and genus. This contradiction
concerns these particular thick schemes, not all possible thickenings
of C. The local tests cannot distinguish them from a potential solution
without also retaining the global equation module. Further punctual
classification is therefore deferred unless it supplies a uniform
constraint on that module or constructs the required two sections.
The already established globally glued fixed-twist formal-pair criterion
remains an available route; no new algebraization gap is asserted.

## Eighth integration: affine generators and the global matrix obstruction

The next two fresh `gpt-6-astra/ultra` assignments retained the actual
global equation module: one tested endpoint interpolation and Serre
bundles, the other the restricted Koszul complex and matrices on
multiple quadrics. The first produced no new uniform implication and
stopped without a new note. Its proposed projected-ribbon diagnostic
was also stopped: its initially claimed CI Hilbert-polynomial match
was incorrect (degree eight, genus five is not the (2,4) CI polynomial),
and developing another ribbon variant would not improve the existing
controls. No conclusion uses that abandoned claim.

The [moving-family note, §6](2026-10-31-moving-family-descent.md)
now includes a separately reviewed classical affine strengthening.
Every lci thick curve in A3 whose reduction is A1 is an actual scheme
CI: affine nilpotent invariance makes its determinant conormal trivial,
the affine Serre extension gives a rank-two projective module, and
Quillen–Suslin makes that module free. Thus both entire affine pieces
of every Z_m in the moving control have genuine two-polynomial
presentations. Every generating pair for either fixed affine ideal,
when ordinarily homogenized, acquires a residual curve in the omitted
plane, attaching as a union at the omitted endpoint. Otherwise purity
would identify the resulting projective CI with the already excluded
scheme Z_m. This quantifies over presentations of those fixed thick
schemes, not over every affine STCI presentation of the reduced C.
The existing `gpt-6.1-sol/high` reviewer checked this coherent extension;
its source-locator and section-number corrections were applied.

The multiple-quadric route does retain global equations: an actual pair
gives q^N=AF+BG and hence a two-by-two matrix with first column (F,G)
and determinant q^N. The proposed simplification to successive
determinant-q factors is false. The
[short geometric counterexample](2026-10-31-simultaneous-equation-geometry.md)
and [independent audit](2026-10-31-simultaneous-equation-geometry-audit.md)
use
\[
M=\begin{pmatrix}
x_1^2&x_1x_2+q\\ x_1x_2-q&x_2^2
\end{pmatrix},\qquad\det M=q^2.
\]
On Q its rank-zero scheme is the square of the ideal of the two
marked endpoints. Each determinant-q factor would have rank one
everywhere on smooth Q, so their composition would vanish along the
zero divisor of a map of line bundles. It cannot have only those
isolated rank-zero points. This excludes factorization even through
an arbitrary rank-two intermediate bundle. A fresh
`gpt-6.1-sol/medium` reviewer reconstructed this bounded geometric proof
and its exact cokernel layers; no material correction was required.

The cokernel is globally ACM and generically rank one on 2Q, but
its natural q-image is I_T(-1), with a punctual defect at T={p0,p∞}.
Thus the ACM total object need not have line-bundle or ACM layers on Q.
Even placing the defect at the two marked points does not restore the
proposed factorization. The example's first column defines two lines,
however, so it does not satisfy the actual STCI column-support condition.
No obstruction to matrices satisfying that stronger condition has been
proved. The preceding Koszul degree/socle calculations only reproduced
existing budgets and were not retained as new theorems.

These tests leave the global equation condition intact. Homogeneous
endpoint interpolation must use the actual frame x3=v t^4, including
the factor v^(−n) in degree n, and the actual local parameter z=τu/v;
freezing these nonlinear data would change the problem. Serre
construction alone returns a bundle whose required splitting remains
unproved. The next substantial investigation needs a uniform argument
for the actual homogeneous pair or its distinguished column, or a
construction of that pair. Neither another local-type list nor a
classification of arbitrary matrix factorizations is adopted as an agenda.

## 9. Closeout and continuing strategy assessment

At the user's request, the two bounded investigations following §8 ended
before any further research round. The
[unrestricted strategy assessment](2026-10-31-unrestricted-strategy-assessment.md)
preserves their findings: the distinguished-column matrix is the embedded
ideal of a generalized divisor on NQ, without an automatic invertibility
claim; direct two-marked-fiber abc loses transverse information, with the
missing ramification budget made explicit. The short elementary arguments
received a bounded independent check; the assessment identifies the source
applications that did not receive a full independent mathematical audit.

A fresh strategy reviewer challenged the allocation and corrected a bias
against special-family constructions: one such success can settle existence,
whereas a special-family exclusion needs a further reduction to settle
nonexistence. The assessment compares genuine new constraints, exact
reformulations, failed shortcuts and constructive flexibility. No specific
technical campaign is selected. It recommends a bounded comparison of
concrete mechanisms, with explicit new inputs and stopping conditions,
after the recommendation has been reported.

The [decision guide](../RESEARCH_DECISION_GUIDE.md#continuing-extraction-and-strategy-assessment)
now makes result extraction, useful generalization and strategic review
continuing parts of the research process. Every result should teach us
about the larger problem; a quick contradiction is not the required output.
Existence remains a live possibility, and new examples should answer a
named question before more cases are assigned. Both producers and the
fresh reviewer completed their assignments without starting another round.

## State at this integration checkpoint

The retained proof notes and independent audits preserve the actual
progress and failures. Retired duplicate arguments generated no additional
retained proof notes. Main and the consolidated branch have not been
modified. The research branch contains these proposals and navigation
updates; no result has been promoted.

The characteristic-zero STCI objective remains unresolved and active. The
contact identity, strict movement of the full tropical family, and exact
affine, conductor and finite-cover formulations are available inputs. They
do not yet supply an incompatible global constraint or an actual supported
pair. Local flexibility and the existing exact projection sources remain
constructive evidence to understand, with their precise limits retained.
The current allocation and stopping conditions are those in §9 and the
linked assessment; earlier suggestions in this record are not automatic
continuations. Main and the consolidated branch remain untouched.
