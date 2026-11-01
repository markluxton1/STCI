# The complexity lane in the broader realization problem

Cross-branch assessment, 2026-10-31. This note answers what the completed
complexity work contributes, what the other branches change about its next
question, and which bounded continuation is recommended. It is a source-level
synthesis, not canonical promotion or a claim to settle unrestricted STCI.
The two short deductions added to the actual-root comparison have the review
status recorded at the end.

The central lesson is that **actual equation realization and support exhaustion
are different computational problems**. We now have geometric comparison maps
for the first and an actual residual pair demonstrating the distinction. The
most useful continuation is to apply those maps to a geometrically specified
surviving family, with all corrections and parameter boundaries retained.

## 1. Fixed evidence and closeout

All embedded characteristic-zero claims below concern
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\) over an algebraically closed
field. Exact calculations use rational or explicitly algebraic coefficients.
Arithmetic statements concern the same integral embedding and the prescribed
special pairs in their sources. No result about one such pair covers every
characteristic-zero presentation.

The review used these committed snapshots, not moving working files:

| Lane | Exact checkpoint | Evidence used |
| --- | --- | --- |
| This complexity/actual-root lane | `28756229308313912eb5e98ab2b21c08d828f78c` | [Intrinsic geometry](INTRINSIC_GEOMETRY_AND_STCI_COMPLEXITY.md), [actual root comparison](ACTUAL_OCTIC_ROOT_LIFT_COMPARISON.md), [torsion-two reduction](QUADRATIC_ROOT_TORSION_TWO_REDUCTION.md) |
| Consolidated account | `fd50fb66a8457628b5d9de2f9e4835cdb8656a46` | `research/STATE.md`, `research/FRONTIER.md`; `research/synthesis/intrinsic_fourth_extension.md`, `projected_thickening_section_defects.md` and `quadratic_covers_and_conductor_descent.md` |
| Spectral realization | `0046beca62e36a1f1d02bdd05dbf900dd5670b56` | `research/synthesis/order_three_roots_and_sextic_lifts.md`, `spectral_pushforward_powers.md`, `spectral_determinant_schemes.md` |
| Arithmetic lifting | `563fa53652fcb1763427a69799b195f7a6d8e438` | `research/supplements/PRIME_TO_P_POWER_EXTRACTION.md`, `FROBENIUS_POWER_LIFTING_PRECISION.md` |
| Four-streams/carriers/surfaces | `7530d052c4ea198916e399de034ba4a16a7c74d2` | `research/notes/2026-10-31-quintic-gorenstein-normalization-exclusion.md`, `2026-10-31-quintic-octic-ade-exclusion.md`, `2026-10-31-pencil-milnor-budget.md`, `2026-10-31-unrestricted-strategy-assessment.md` |
| Intersections and projections | `b271fc5bf20a6920b1540cabd57f095139d8d7a5` | `research/notes/2026-10-31-stci-package-closeout.md` and its projection audit; selected mathematics is also retained in the consolidated account |

Some named source paths exist only on their source branch. Retrieve them as
`git show <checkpoint>:<path>`; they are not missing local dependencies to copy
into this checkout. The intersections checkpoint is the remote branch tip;
its local branch is still at `317d5bc`. The detached `586a84f` worktree is
already in the consolidated ancestry, and `main` at `9d734e1` supplies no newer
contribution. A live `git ls-remote --heads origin` confirmed that the four
active research branches and consolidation have local commits beyond their
published tips. This review does not merge branches or push them.

This lane started clean, with its octic calculator and required support
committed. No unfinished owned worker or pending calculation was resumed.
Previously stopped eliminations remain stopped. Existing exact computations
and their recorded independent reviews are reused; none was rerun merely for
this assessment.

## 2. What this lane has established

The [finite-jet criterion](STCI_COMPLEXITY_AND_QUADRATIC_ROOTS.md#2-reuse-a-finite-verification-theorem-before-discussing-hardness)
tests an actual degree-\((a,b)\) pair using the expected generic length
\(M=ab/\deg C\), when integral. The extra jet layer checks properness too.
At bounded degrees, actual homogeneous coefficients give a finite algebraic
incidence problem. This supplies neither a uniform witness-degree bound nor a
termination rule for every negative instance of unrestricted STCI. Arithmetic
operation counts with supplied matrices are not end-to-end bit bounds.

The [global-source calculation](IDEAL_SHEAF_SPECTRAL_SEQUENCES_AND_GLOBAL_JETS.md)
is more than a reformulation. For this quartic, degree-six global jets become
exact at normal depth five; eleven missing quadratic symbols are accounted for
by a rank-eleven third differential. The intrinsic continuation extracts the
filtered source images, an effective bound for curves on a smooth quadric, and
an eventual but not effective general bound for smooth connected curves in
\(\mathbf P^3\). These depths concern realization at fixed degree, not the
least degrees of a defining pair.

The root work excludes the smooth diagonal torsion-two locus, every smooth
torsion-two pure-direction root, and the complete rank-drop boundary of the
retained mixed chart. The mixed rank-two characteristic-zero calculation is
unfinished. Its finite-field unit ideal is not a characteristic-zero
certificate. The useful gain is a covered reduction with compact certificates,
not an exclusion of all smooth roots.

For a smooth \((2,2)\) root satisfying \(K_1\), the actual octic comparison
is a map from seventeen leading-multiplier coefficients to a quotient of
dimension six to nine. All actual corrections are retained. Its kernel always
has dimension at least eight, but may have a fixed divisor. At the seed it
contains jointly generating multipliers and an explicit proper pair with
\[
[V(F_8,G_8)]=8[C_0]+R,\qquad\deg R=32.
\]
The seed fails \(K_2\). It is a useful realized residual intersection, not a
candidate for the required sole-support length sixteen. More first-compatible
octics at that seed would not address the missing condition.

## 3. What the other lanes change

**Spectral geometry now provides a useful source for a varying-root test.**
At the spectral checkpoint, the smooth exact-order-three locus is an open in
\(\mathbf P^7\), parameterized by four binary linear syzygy entries and their
Hankel minors. This retains the fixed ruling coordinates; arbitrary changes
of those coordinates do not preserve the embedded operator. In a complete
two-parameter slice, six roots pass \(K_1\); four have no actual sextic symbol,
and the other two fail the full cubic-source test, including the free \(q^3\)
correction. The graded families remain valid despite these realization
failures. The larger slice's degree-nine diagnostic is explicitly unreviewed.

The current lane supplies a smaller intrinsic description of that actual
sextic test. The [new degree-six comparison](ACTUAL_OCTIC_ROOT_LIFT_COMPARISON.md#the-first-sextic-comparison-and-the-order-three-consequence)
has
\[
\kappa_f^{(6)}:H_f\longrightarrow
H^0(\Sigma,\mathcal O_\Sigma(3,3))/k\ell^3,
\qquad\dim H_f\le3,\quad\dim\text{target}=11.
\]
Its kernel is exactly the first-compatible actual sextic space, with one
actual sextic per surviving multiplier. On an exact-order-three root, every
later sextic membership target vanishes, **conditional on the corresponding
root lifts existing**. This sharpens the division of labor: solve this actual
source comparison and the root-lifting tower as distinct requirements.
No compressed implementation or runtime gain is claimed.

Under all the saturation, movement-two and full generic coprime-CI hypotheses
of R-0013/R-0014, order three retains only
\((r,s;a,b)=(2,12;6,16)\). With R-0006's smooth full root and everywhere
joint generation, a sole-support pair requires root lifts through exceptional
order nine. The small sextic map does not supply those lifts or the sextic's
degree-sixteen mate. It does not reduce arbitrary STCI to this family.

**The carrier and projection results demand exceptional geometry, not just
more parameters.** The reviewed four-streams result excludes every integral
nonnormal quintic with Gorenstein normalization in every mate degree. The
separate \((5,8)\) result excludes a quintic that is ADE everywhere, including
away from C, without the older reduced-first-symbol assumption. Neither
covers all quintics. The consolidated intrinsic fourth-extension proof also
shows that embedded extension classes can settle a bounded case without a
global surface inequality. These are reasons to retain actual embedding and
conductor data alongside the smooth-root analysis.

Conversely, actual projection sources can fail before mate search: the fixed
elliptic octic member has an extra inverse scheme of projective length twelve,
and the covered power and binary-mixture projected thickenings fail ACM in
their stated characteristic range. Increasing the mate degree does not repair
that fixed member; increasing powers does not repair those covered sources.
The full five-parameter elliptic support/descent locus and other actual sources
remain open. These are useful alternative construction lanes rather than
evidence that every candidate must have a smooth quadratic root.

**Arithmetic isolates an endpoint obstruction to lowering a powered equation.**
Prime-to-p powers in the prescribed supported mixed-characteristic lift can be
extracted at every ramification index. For odd p, strong unramified lifting of
a prescribed \(p^e\)-powered pair loses exactly e Witt digits when passing to
the lower pair. In the specified \(p\ge7\) family this gives maximum precision
\(1+v_p(n)\) for fixed exponent n. Growing precision by growing degrees does
not produce a fixed-degree characteristic-zero witness.

For every still-possible supported trait of that family, the flat closure of
the pure lower root has a nonzero punctual specialization defect T supported
at the two endpoints, with
\(p_a(D_K)=1+2p^2-\operatorname{length}T\). Vanishing of T would give Cartier
extension and an actual quartic equation, contradicting the quartic exclusion.
This is a precise model for a globalization question. No comparison identifies
T with our root classes, a normal-filtration comparison defect, or a conductor
module, and no theorem here excludes or constructs the required T.

**Several attractive summaries carry no new restriction.** The four-streams
Milnor inequality is weaker than the local cluster bound already available for
C0. Arbitrary Chow determinants do not give the prescribed equation-bundle
map. The proposed exact-bundle Hom lemma in the latest closeout lacks a
separate independent proof audit; it is not used as a premise here. High-genus
exceptional covers and bad exceptional fibers can coexist with supported
intersections. None establishes a residual curve downstairs. Additional
calculations of those same budgets are low priority unless they introduce a
new actual-source or global compatibility constraint.

## 4. How the ideal-sheaf diagram organizes the problem

For actual F,G, put X=V(F), Y=V(G), Z=X intersect Y and
\(J=\mathcal I_Z\subset I=\mathcal I_C\). The labelled map
\(\mathcal O(-a)\oplus\mathcal O(-b)\to I\) records both equations.
For a proper pair its image has the Koszul resolution, and the inclusions give
\[
0\to\mathcal O(-a-b)\to\mathcal O(-a)\oplus\mathcal O(-b)\to J\to0,
\qquad0\to J\to I\to I/J\to0.
\]
This is a concrete way to keep C, X, Y, Z and their maps together. The sheaf
I/J includes the thickening along C as well as any residual support; it is not
itself a residual-curve certificate.

The [filtered-complex construction](https://stacks.math.columbia.edu/tag/012K)
organizes source realization via filtered Cech cohomology and full initial
relations via the filtered carrier Koszul complex. Their comparison must retain
the induced filtration \(J\cap I^n\); replacing it by \(I^nJ\) changes the
question. The separate normal-parameter Koszul sequence detects another
comparison defect. The blowup residue map supplies an actual comparison to a
lifted root; it does not identify these spectral sequences or their classes.
These distinctions and the conormal maps are already recorded in the
[ideal-sheaf account](IDEAL_SHEAF_SPECTRAL_SEQUENCES_AND_GLOBAL_JETS.md#1-keep-the-actual-diagram-and-distinguish-its-spectral-sequences).

Thus the spectral sequences are useful when they locate a missing source
image or a genuine extension class. A single larger complex has no established
computational advantage. The transferable object is the polarized filtered
embedding with its actual source maps; the quartic's convenient matrices and
small dimensions are examples, not invariants of an abstract rational curve.

## 5. Recommended next work

1. **Primary continuation: the intrinsic sextic comparison on the smooth
   order-three locus.** Use the full Hankel parameter space, intersect with
   K1 in the fixed embedded frame, and identify (16) with the complete accepted
   sextic incidence on every retained rank stratum. Ask whether its kernel
   contains a nonzero multiplier. Stop at a covered injectivity result, an
   exact compatible sextic with its surviving root conditions, or an explicit
   indispensable boundary still unresolved. An exact survivor should next
   face K2 before a mate search. The existing larger-slice diagnostic may be
   completed as a bounded preliminary test only with all denominator and
   omitted coefficient boundaries reviewed; it is not coverage of the full
   order-three locus. This recommendation targets a small actual-source map
   with a geometric parameter space, not another isolated seed.

2. **Keep an actual construction alternative: the elliptic family's inverse
   support and descent.** The intersections lane has a specified five-parameter
   source. Test full inverse support fiberwise, retaining source smoothness,
   basepoint freedom and finite birationality, then actual pure-power section
   descent on survivors. A total-parameter unit ideal or a generic rank is not
   a fiberwise answer. Stop at an admissible carrier, a covered family failure,
   or a stated remaining stratum. This work belongs with that source's owner;
   the present lane contributes the source-versus-support distinction.

3. **Retain the mixed torsion-two rank-two calculation as a secondary exact
   target.** The boundary is already excluded. Resume only with a specific
   reduction or certificate strategy for the remaining characteristic-zero
   charts, a resource bound, and a coverage check. Its existing finite-field
   computation is a lead, not a reason to repeat the same large elimination.
   A complete answer would close that root stratum under the bridge hypotheses,
   not unrestricted STCI.

For this lane, repeating first-compatible octic constructions, enlarging a
general spectral-sequence framework, or recomputing dependent surface budgets
has less immediate value than the first task. The explicit octic pair should
remain a control for future methods: any claimed sole-support shortcut must
distinguish it from a pair of transverse length sixteen. Generalization should
retain the flag/source quotient and Cartier restriction construction while
recomputing its dimensions for the new embedding.

## Review and limits

Two disjoint read-only assessments, `spectral_branch_context` and
`arithmetic_surface_context` (GPT-6.1 Sol, high reasoning), checked the spectral
and arithmetic/surface connections against the exact snapshots above. Their material suggestions are
adjudicated here: the sextic comparison is the primary local continuation;
the arithmetic endpoint defect is a useful separate model, without an asserted
identification; a new octic stratum remains possible but is not selected before
its higher root conditions are justified. The lead also inspected the
consolidated and intersections evidence and the actual current-lane proofs.

`synthesis_independent_review` (GPT-6.1 Sol, high reasoning) independently
reconstructed the new degree-six restriction quotient, its uniqueness claim,
and the conditional order-three membership consequence. It checked the numerical
row and exceptional-order-nine scope against R-0006/R-0013/R-0014, the strategy
against the named spectral, consolidation, carrier and intersections sources,
and the navigation additions. These passed with no material finding. It reused
the independently reviewed source dimensions and bound on H_f; it did not rerun
their calculators or audit every historical proof. The detailed arithmetic
source assessment was covered by the separate arithmetic/surface reviewer.

All 69 local link destinations in the five changed/new Markdown files resolve;
the canonical validator checks 37 records with zero errors, and whitespace
checks pass. The octic calculator retains its previously reviewed SHA-256
`ab3351b28f6ed49dcb359d811c7f48ff6eb59d8e472ba8522aa9ae7b9982857b`.
No CAS computation was run in this assessment. No theorem is promoted, no old
run is relabelled as fresh, and the unrestricted characteristic-zero question
remains open in the reviewed research account. This is a strategy and
mathematical-interface review, not a new comprehensive literature survey.
