# Characteristic-zero STCI: geometric research integration

Date: October 30, 2026. Branch: `codex/stci-char0-four-streams-2026-10-30`.
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

## State at this integration checkpoint

The four retained proof notes and four independent audits preserve the
actual progress and failures. Retired duplicate arguments generated no
additional retained proof notes. Main and the consolidated branch have not
been modified. The research branch contains these proposals and a short
index link; no result has been promoted.

The characteristic-zero STCI objective remains unresolved and active. The
next substantive investigation is simultaneous endpoint compatibility of
arbitrary **higher** affine supported structures, retaining full nonlinear
transitions and the actual fixed ambient twists. Further work should aim
for an all-pairs inequality or an actual equality construction. Repeating
the reduced determinant obstruction, a fixed-carrier calculation, or a
first-normal valuation calculation would not complete that task.
