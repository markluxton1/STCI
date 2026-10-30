# Historical mathematical investigations

Complete source texts below, retaining mathematical arguments, hypotheses, counterexamples, corrections and unresolved cases. No new independent audit or theorem promotion.

---

## Source: 2026-10-15-formal-branch-ruled-model-degree-bound-review.md

# Smooth formal branch and the ruled-model degree bound

Date: 2026-10-15.

Status: independent conceptual review of the normalization and intersection-theoretic steps in the proposed no-infinite-lift argument. This note assumes the stated algebraization-as-a-branch theorem applies; it does not re-prove that theorem, establish existence of an all-orders Cartier lift, or promote the resulting exclusion to an accepted repository theorem.

## Input and purpose

Let `B = Bl_C(P^3)` for the smooth rational quartic `C`, let `E = P^1 x P^1`, and let `Z` be a smooth curve of class `(2,2)` on `E`. Thus `Z` has genus one. Assume an all-orders lift yields a smooth formal surface `V` along `Z`, transverse to `E`, with

`N_{Z/V} = O_Z(7,-1)`, of degree `12`.

Assume moreover that `V` is a formal branch of an actual integral surface `W` in `B`. The original concern was whether the entire completion of `W` must equal this branch. The degree-bound argument reviewed below does not need that assertion. Other formal branches, or other curves of `W cap E`, may remain.

## 1. Normalization preserves the chosen smooth branch

The precise local input is that, at each closed point `z` of `Z`, the induced maximal-ideal completion of `V` is a regular two-dimensional minimal branch of `O_{W,z}^`. This is the meaning of "formal branch" needed here; a merely generically finite formal map into `W` would require a separate argument.

Surfaces of finite type over a field are excellent, and their normalization is finite. For an excellent reduced local ring, normalization and completion identify the completed local factors of the normalization with the normalizations of the completed branches. The chosen branch is regular, hence normal already. Its normalization factor therefore coincides with it. In particular the selected point of the normalization of `W` has regular completion, hence is a regular point.

The global formal branch makes these local choices compatible. Equivalently, each local integral element of the normalization maps into the regular formal branch because the latter is integrally closed in its fraction field. This gives a morphism from `V` to `W^nu`; reducing modulo the ideal of `Z` gives a section `Z -> W^nu` over `Z`. Its image `Z'` is isomorphic to `Z`, the normalization is smooth along `Z'`, and its formal completion along `Z'` is the chosen `V`.

Reference for the normalization/completion mechanism: Stacks Project, [Branches of the completion, Section 15.110](https://stacks.math.columbia.edu/tag/0C27), especially the proof of Lemma 15.110.8. It decomposes the completed normalization into completed local normal factors and identifies their minimal branches. One should check this exact local branch hypothesis when inserting the algebraization theorem into the final proof.

Resolve the normalization with centers outside its regular neighborhood of `Z'`. This yields a smooth projective surface `T` containing the same curve `Z'`, with unchanged formal neighborhood. Write `Z` again for this curve. Consequently

`Z^2_T = 12`.

Let `H` denote the pullback of a hyperplane under `T -> W -> B -> P^3`. It is nef. Since `H|E = O_E(4,0)` and `Z = (2,2)`,

`H.Z = 8`.

The surface `W` is not `E` because the selected branch is transverse to `E`. Thus its image in `P^3` is a surface, and the map is birational onto that image. If its degree is `d`, the projection formula gives

`H^2 = d > 0`.

Surface resolution references: Stacks Project, [Resolution, Section 54.14](https://stacks.math.columbia.edu/tag/0BGJ). Resolution can preserve a prescribed regular open set. Since the starting normalization is projective, the resulting smooth proper surface is projective.

## 2. Hartshorne's theorem supplies a ruled model near the curve

Hartshorne's Theorem 4.1 applies because

`Z^2 = 12 > 4 g(Z) + 5 = 9`.

It gives a geometrically ruled surface `R -> Z` and a section `Z_0` such that `(T,Z)` and `(R,Z_0)` are equivalent. "Equivalent" is defined in the paper as a birational map inducing the identity on the curve and an isomorphism on open neighborhoods of it. In particular

`Z_0^2 = 12`.

Primary reference: R. Hartshorne, *Curves with high self-intersection on algebraic surfaces*, Publ. Math. IHES 36 (1969), 111--125, [Theorem 4.1, printed p. 122; definition on printed p. 111](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf).

## 3. The square comparison is valid

Resolve the birational map into a common smooth surface

`q: U -> T`, `p: U -> R`.

Because the birational equivalence is an isomorphism near the curves, this can be done with all point-blowup centers outside those neighborhoods. Put `L = q^*H` and `D = p_*L`. Choose an actual Cartier divisor representing `L` before pushing forward; `R` is smooth, so its pushforward is Cartier. Equivalently this construction is well-defined on numerical divisor classes.

For a single point blowup `b: X' -> X`, any divisor class `A'` has a unique expression

`A' = b^*A + c E_b`,

where `A=b_*A'`; orthogonality and `E_b^2=-1` imply

`(A')^2 = A^2 - c^2`.

Iterating through `p`, using total-transform exceptional classes if desired, gives

`H^2 = L^2 = D^2 - sum_i c_i^2 <= D^2`.

No sign assertion for the coefficients `c_i`, and no nefness assertion for `D`, is required for this inequality. The neighborhoods of `Z` are unchanged, so

`D.Z_0 = L.Z = H.Z = 8`.

Also `D` is nef: for any integral curve `Gamma` on `R`, its total transform `p^*Gamma` is effective, hence

`D.Gamma = L.p^*Gamma >= 0`.

Here `L` is nef because it is a pullback of `H`.

The point-blowup factorization used above is standard for proper birational morphisms between smooth surfaces; see Stacks Project, [Lemma 54.17.1](https://stacks.math.columbia.edu/tag/0C5Q).

## 4. The numerical bound

Write the numerical class of `D` on the ruled surface as

`D == a Z_0 + b f`,

where `f` is a fiber. Here `a=D.f` is an integer. Nefness gives `a>=0`; if `a=0`, then `D^2=0`, contradicting `D^2>=H^2>0`. Hence `a>=1`. From `Z_0^2=12`, `Z_0.f=1`, and `f^2=0`,

`8 = D.Z_0 = 12a+b`,

and therefore

`D^2 = 12a^2+2ab = 16a-12a^2`.

For integral `a>=1`, this expression is at most `4` (its value at `a=1`); for `a>=2` it is negative and hence impossible here. Thus in fact `a=1`, `D^2=4`, and

`d = H^2 <= 4`.

This establishes the contested square comparison and degree estimate, under the stated local branch input. It does not assert that `W` has only one branch along `Z`.

## 5. Connection to the proposed contradiction

The remaining elementary geometric implication is that the strict transform `W` has generic multiplicity `m>=2` along `C`: the effective divisor `W|E` contains the entire integral `(2,2)` curve `Z`, whose degree over `C` is two. For a general fiber of `E -> C`, the degree of `W|E` is precisely `m`, so `m>=2` even if extra components exist.

Consequently a general plane section of the integral image surface of degree `d<=4` is an integral plane curve singular at the four distinct points where the plane meets `C`. Each such singularity has delta invariant at least one. This contradicts the arithmetic-genus bound `(d-1)(d-2)/2<=3`.

To use this as a finished exclusion, the parent proof should explicitly state the algebraization theorem's exact branch conclusion and the generic-plane-section/Bertini hypotheses. The normalization and ruled-model square comparison themselves do not require G3 in `B`, G3 in `W`, or exclusion of extra formal branches.


---

## Source: 2026-10-15-session-structural-results-acceptance.md

# October 15 structural research acceptance and continuation record

Date: 2026-10-15. Integrator: primary agent.
Subsequent accepted scope extensions, the whole-h2 global model and current
process state are recorded in the
[October 16 continuation](2026-10-16-session-structural-continuation.md).
The universal integral-curve STCI question and unrestricted characteristic-zero
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. This record accepts new written
arguments only at their stated scope. Previously accepted proofs and
certificates were premises and were not replayed.

The latest externally observed checkpoint is
`2e9ea8100d39a181fe7010160366b940be531b8d`, title
`2026-10-15 morning limit reached`. The primary agent did not create it.
The current authority remains
[the audited frontier](../AUDITED_STATE_2026-10-14.md), updated on October 15,
with [the successor handoff](../SUCCESSOR_HANDOFF_2026-10-14.md).

## 1. Shared quintic incidence, without factor-case fan-out

Accepted new inputs and reductions are:

- The [intrinsic A4 contact bound](2026-10-14-generalization-quintic-intrinsic-a4-contact-bound.md)
  and its independent review. Every surviving `j=0` candidate has contact
  at most two. On h2, H misses A4, so the sextic Q cannot be supported only
  at A4. Hence every remaining candidate, for either value of j, satisfies
  `Res(H,Q)=0`.
- The [twelve-generator ideal-sheaf reduction](2026-10-15-generalization-quintic-h2-twelve-generator-support-system.md)
  and [independent audit](2026-10-15-generalization-quintic-h2-twelve-generator-independent-audit.md).
  On the monic finite-H chart and `D(q5) union D(q6)`, eleven fixed cubic
  minors plus one retained-j minor define exactly the same ideal sheaf
  as all seventy-seven original rank minors. This includes nonreduced
  coefficient bases but does not change the field-valued scope of the
  original root-support interpretation.

The quintic incidence is not proved empty. Norm factors remain together
in the shared ideal; they are not declared forbidden projection factors.
Other quintic normalizations and the retained singular/common-root
boundaries remain open.

## 2. A uniform formal first-relation frontier

Accepted: [the uniform tower theorem](2026-10-15-generalization-uniform-root-tower-finite-determinacy.md),
[cohomology review](2026-10-15-generalization-uniform-root-tower-cohomology-independent-audit.md)
and [embedded-ideal functor review](2026-10-15-generalization-uniform-root-tower-functor-independent-audit.md).
For a fixed balanced rational formal neighborhood, `lambda>3epsilon`
makes every correction unique. All obstruction stages therefore remain
closed schemes on one fixed finite-type coefficient open and eventually
stabilize as schemes. The stable locus represents compatible formal
Cartier ideals, retaining singular/nonreduced roots and parameter bases.
The cutoff N is existential and depends on the full formal embedding
and fixed `(epsilon,r)`; one adjacent equality is not a cutoff certificate.

Within the accepted actual-CI bridge, only stages `m<s-r` are supplied.
Thus `s>r+N` forces the stable formal locus. Without a further theorem,
this is neither algebraization nor emptiness of that locus.

The [torsion/second-zero geometry](2026-10-15-generalization-quadratic-root-torsion-second-zero-geometry.md)
and [independent audit](2026-10-15-generalization-quadratic-root-torsion-second-zero-independent-audit.md)
are also accepted. On smooth `(2,2)` roots, exact order-two ruling
difference is the cubic coefficient determinant. Its specified component
D through the accepted seed is three-dimensional; the second zero locus
inside D has support dimension at most two. Other components and torsion
orders are retained.

## 3. All mate powers in fixed projection families

Accepted: [the full phase-space/torsion-coset theorem](2026-10-15-generalization-projection-torsion-coset-reduction.md)
and [independent family review](2026-10-15-generalization-projection-torsion-coset-independent-review.md).
After finite stratification, the actual fixed normalization families have
one finite-type torus phase image, retaining full inverse support and all
nilpotent conductor equations. Relative Noether normalization is spread
before rational localization to retain specialized conductor curves.
The nilpotent locus is closed per rational-matrix stratum and constructible
overall. A carrier has a mate exactly when its phase tuple is torsion.

Laurent's theorem gives finitely many relatively open pieces of torsion
cosets inside the actual constructible image, with deleted boundaries
retained. Positive-dimensional surviving cosets mean unbounded least mate
degrees between actual carriers; only zero-dimensional survivors mean a
uniform bound; no surviving coset means no mate anywhere in the family.
These alternatives have not been decided for the three actual C0 families.

The on-C thresholds are concretely 5,5,13 for the two degree-eight models
and degree-sixteen plane model. Once phase order E is finite, every
multiple of E at least the threshold descends. All smaller mate degrees
form a finite subset of its multiples. This includes carriers generically
singular along C, not just the generically regular lane.

## 4. A new all-order geometric exclusion

The [smooth movement-two formal nonexistence theorem](2026-10-15-generalization-smooth-root-formal-nonexistence.md)
uses ample-normal formal algebraization as a branch, then a ruled model
near the unchanged root curve and an opposing plane-section genus bound.
It addresses every `r>=2` simultaneously for balanced rational degree-e
curves with `e>=4`. The focused
[branch/ruled-model review](#source-2026-10-15-formal-branch-ruled-model-degree-bound-reviewmd)
passes its conditional steps. The full
[independent source-hypothesis and global audit](2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md)
now passes the theorem, general numerical criterion, and the finite-r
corollary. The image surface would have degree `d<=r+2` but also
`(d-1)(d-2)>=e r(r-1)`, which is impossible for e>=4,r>=2.
For each fixed r, the accepted tower consequently has a uniform finite
empty stage on the smooth movement-two open. Under the accepted actual-CI
bridge this gives `s-r<=N`, not exclusion of every finite-gap pair.
The original main proof is characteristic zero. The separately reviewed
formal characteristic extension and subsequent inseparable actual-CI
bridge are accepted in the October 16 continuation at their literal scope.

The owner preserves a failure shield for an attempted effective cutoff:
a long finite primitive jet can lie in `g^alpha+u^k` without an actual
smooth algebraic branch. A Hilbert-section count alone therefore does
not preserve the normal degree used by the formal argument.

## 5. Exact computation and process state

The new h2 shared-system attempts are preserved separately:

- Attempts01,02,03 timed out during input/preparation and supplied no
  incidence elimination.
- [Attempt04 FLINT preparation](../validation/2026-10-15-quintic-h2-unified-incidence/attempt-04-flint-preparation/execution-record.json)
  exited zero with empty stderr. All twelve exact generators and declared
  unit divisions were produced, with a cross-engine binding of the first
  cubic. Generator degrees are 37 and 49--52. This is preparation only.
- [Attempt05 modular prospect](../validation/2026-10-15-quintic-h2-unified-incidence/attempt-05-modular-global-prospect/execution-record.json)
  reached its 45-second timeout before a stage marker. No mathematical
  result was obtained; its exit code was not retained. The owner polled
  handle 81785 on October 15 at 19:07 UTC and confirmed it was closed.
  No live PID was recorded. Do not restart that source unchanged: its
  input was slow and a later variable would shadow a built-in.

The accepted degree-fifteen original-tensor certificate and all twenty-two
finite family-two exception-root closures remain premises. They were not
rerun. Large accepted witnesses were not recomputed or rehashed here.

The [new proof-record index](../validation/2026-10-15-structural-acceptance/index.json)
binds accepted and provisional notes separately. Its hashes and local-link
checks are document integrity evidence, not mathematical verification.
The full goal remains active; no universal construction, counterexample,
complete quintic exclusion or unconditional carrier-degree bound is claimed.


---

## Source: 2026-10-16-generalization-quintic-h2-global-QQ-guard-independent-review.md

# Independent prelaunch review: one guarded global QQ saturation prospect

Date: 2026-10-16.

Status: **PASS for the reviewed driver and corrected runner sources,
conditional on the runner's fresh in-process preflight passing before
Macaulay2 launch.** This is a source/runtime-control review, not a
mathematical result from the prospect. The reviewer started no CAS,
coefficient assembly, saturation or benchmark.

Reviewed files:

- [global QQ driver](../computations/generalization_quintic_h2_global_QQ_saturation_2026_10_16.m2),
  SHA256 c6d6fceaeb16182a226373dfc19efe3d8816d0cc4797e7186f26bd038051735b;
- [guarded runner](../computations/run_quintic_h2_global_QQ_saturation_guarded_2026_10_16.py),
  SHA256 e47317ab64eeb5968aba839880955a54ba55396ae7358dcb0b5f8718a2f6be04.

## 1. Exact mathematical input and computation scope

The driver loads the already audited load-only input over QQ, checks
seventeen equations and nine ring variables, and calls exactly one
saturation of h2GlobalIdeal by ideal(h2GlobalDomainUnit). That saved
domain polynomial is delta*E*Delta1. The driver introduces no cover
discriminant, K, q coefficient or j inverse. It does not reconstruct
the actual octic or replay any accepted verifier or model assembly.

The driver saves a stage before the load, after the load and before
the saturation; on completion it saves the resulting generators and
the unit-ideal comparison. Its own output explicitly treats a unit
comparison as provisional until an exact certificate in the original
generators is extracted and checked. No mathematical outcome of that
computation is asserted by this review.

Read-only checks confirmed that the current loader still matches
the accepted attempt-05 source digest and both completed model-data
files still match its input digests. The runner now obtains the
expected loader hash from that accepted execution record, rather
than merely recording its current hash and comparing it to itself.

## 2. Fresh preflight is mandatory and fails before M2

The runner checks all bound input hashes before its preflight. It
then loads libproc, checks the declared rusage-info structure size,
and samples its own process. A small private-session child reports
its PID, process group and inherited CPU limits, allocates a small
buffer, and is sampled for resident/footprint data. The same
private-group termination/reap helper is tested on that child.

Any exception in input checking, monitor setup, child probing or
preflight-record writing returns a blocked-before-M2-launch record.
The actual M2 Popen is strictly after that try/except. An older
standalone preflight record does not bypass the fresh preflight in
this runner. If a capability is denied there, no M2 is started.

## 3. Resource controls and process evidence

The reviewed settings are 120 seconds wall time, RLIMIT_CPU soft and
hard both 120 seconds, and a 1536 MiB stop threshold on the maximum
of the M2 PID's sampled resident memory and physical footprint,
polled every 0.25 seconds. The memory control is accurately described
as a polled threshold, not a hard virtual-address or aggregate
process-group memory limit. The wall threshold initiates group
cleanup; a short termination/reap grace period is separate from the
computation's threshold.

M2 is launched with start_new_session=True, so its private process
group is the returned PID. PID/group provenance is written
immediately after Popen. Every subsequent operation, including that
initial record and console output, is within the try/finally that
stops and reaps the owned group. The final source catches exceptions
for recording rather than rethrowing before terminal evidence is
saved. Signal races where a group exits before SIGKILL are handled.

Monitor failure during the actual job triggers cleanup. Normal
completion also checks for remaining members of the private group.
Unexpected group-cleanup exceptions are recorded, with a direct-child
reap fallback; this is not silently reported as confirmed group
absence. Terminal evidence includes the actual process exit code,
reason, elapsed time, child CPU accounting, sampled memory peaks,
cleanup events and stream hashes. Nonzero process exits are
distinguished from successful completion.

The runner refuses a restart if this single attempt already has an
execution record. It freezes its own source and the M2 driver and
records their hashes. This review applies to the specific hashes
above; changes require an updated source review and new bindings.

## 4. Review boundary

The first source draft had a post-Popen gap before its cleanup try
and rethrew exceptions before saving terminal evidence. Those issues
were reported and corrected before this PASS review. The current
runner also binds the expected loader hash and handles the noted
termination races. Read-only Python syntax and current loader/model
binding checks passed; no subprocess or CAS was started by those
checks.

The reviewed sources are suitable for the one authorized bounded
prospect after their fresh preflight passes. The execution record,
stage, exit code and cleanup events must still be inspected after
the attempt. A timeout, memory stop or process failure supplies no
emptiness conclusion. A successful unit-ideal output would still
require its original-generator certificate before mathematical
promotion. This review neither reports a global h2 exclusion nor
closes the quintic or STCI problem.

## 5. Read-only terminal evidence review

The one attempt is now terminal. I read its
[execution record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/execution-record.json),
fresh preflight record, stage, streams, last metrics and prelaunch
source-review metadata. I started no runtime probe, CAS, subprocess
job or rerun of the prospect during this review; checks were file
reads, JSON comparisons and hashes.

The fresh preflight passed before M2 launch, with its probe child
reporting CPU limits 120/120 and its cleanup recording the private
group absent. The separate fresh-preflight file exactly matches the
preflight object embedded in the execution record. The actual M2
PID and private process group were both 39519.

The actual terminal status is **interrupted**, with stop reason
polled-memory-stop-threshold and M2 exit code -15 (SIGTERM). The
recorded wall time is 58.564014667 seconds and child CPU accounting
is 118.528412 seconds. Peak sampled resident memory is 1,611,595,776
bytes, or 1536.9375 MiB, slightly above the declared 1536 MiB polled
threshold; peak physical footprint is 1,597,376,144 bytes, or about
1523.377 MiB. The final metrics file records the same peaks. These
are measured values from the polled process; they do not constitute
a hard memory cap.

Cleanup records SIGTERM-private-group followed by private-group-absent.
Both caught_exception and cleanup_exception are null. Thus the
audited runner's terminal evidence reports the private group gone
after termination and reaping. The supervisor's successful return
must not be confused with mathematical completion of the M2 job.

The last stage is
before-global-QQ-saturation-by-delta-E-Delta1-only. Neither
saturated-ideal.txt nor is-unit.txt exists, and there is no
saturation-complete stage or completion line. Stdout contains only
the loader's successful seventeen-equation/nine-variable message;
its sentence saying no GB/saturation was executed describes that
load-only subscript, not the later driver attempt. Stderr is empty.
No saturation result or unit-ideal claim was produced.

Read-only verification passed for both current and frozen driver
hashes, both current and frozen runner hashes, all three bound
inputs, and both stream hashes against the terminal record. The
reviewed source hashes are unchanged from section 1. The expected
loader and completed-data bindings therefore remained intact for
this attempt.

This attempt supplies a bounded computation/resource record and
**no emptiness conclusion**. The global seventeen-equation problem
after delta*E*Delta1 remains the handoff target. No accepted proof,
model assembly or completed verification was rerun by this audit.


---

## Source: 2026-10-16-generalization-raw-projection-decision-independent-audit.md

# Scope audit of the raw projection-family decision corollary

Date: 2026-10-16. Reviewer: `phase_family_audit`.
Status: **PASS for the precise explicit rational fixed-model input below.**

Reviewed only [Section 9 of the effective phase-bound note](2026-10-15-generalization-effective-rational-phase-bound.md)
and [Section 8 of its independent review](2026-10-15-generalization-effective-rational-phase-bound-independent-review.md),
including the newly added admissibility paragraph. The accepted finite-phase
theorem and explicit-`W` Mann/SNF/boundary theorem are premises; their proofs
were not replayed. No actual phase image, CAS computation, or family decision
was attempted.

## Reviewed claim and input

The corollary is an **algorithm-existence and termination theorem** from an
explicit projection-family presentation, without a separately supplied phase
image. Input consists of one of the three specified fixed rational normal
graded source rings, its prescribed `H,c,Q`, four sections with polynomial
parameter coefficients over `Q`, and finite `Q`-constructible parameter
restrictions. The prescribed restrictions of the sections to `c` must hold
or be imposed by their finite coefficient equations. Arithmetic, ideal and
module presentations, and zero tests are consequently effective.

Within this scope, the composite procedure constructs a rational phase-image
presentation and applies the accepted explicit-`W` decision procedure. It
decides whether the input family contains a mate-admitting carrier, whether
least mate degrees are unbounded, and computes a valid uniform bound in the
bounded case. This does not assert those outputs have already been computed.

## Why the new raw-input bridge passes

The admissibility paragraph supplies a genuine effective step. Basepoint
incidence and extra inverse points outside `c` are polynomial formulas on
finitely many projective affine charts, so effective algebraically closed
field quantifier elimination computes their parameter conditions. Once
basepoint free, the accepted ampleness argument makes the source map finite
before birationality is tested. Thus the image algebra `A subset B` and its
finite quotient module `B/A` are available without first assuming degree one.
For an explicit certificate, these source rings are standard graded in the
`H`-grading: basepoint freeness makes `B/(f_0,...,f_3)` finite-dimensional,
and a computable finite monomial basis lifts to `A`-module generators of `B`
by induction on degree. Flattening `B/A` preserves the actual fibre image.
A homogeneous monic Groebner basis of the image ideal preserves its leading
monomials and Hilbert polynomial on a computed open. The degree formula then
filters the degree-one locus. All closed complements are revisited, including
those of opens where the generic map has degree greater than one. Actual
integral surface images in `P3` are hypersurfaces. There is no circular
admissibility oracle in this step.

After this filter, finite-module syzygies and annihilators compute generic
common conductors. The searches for Noether coordinates, finite module
generators, bases, and separable primitive elements have finite certificates
checkable over the computably presented fields `Frac(R)` and `Frac(R)(x)`.
The accepted geometric existence results guarantee search termination; a
parameter piece need not be a rational variety.

The module generic-freeness proof is sufficient: retain both generation
directions for a monic module Groebner basis and its Buchberger reductions,
then invert their coefficient denominators. Standard module monomials give
a free localized parameter module, possibly of infinite rank. Applying this
to the relevant cokernels preserves fibre kernels and inclusions. The
[Derksen--Kemper primary source, Theorem 2.13 and Algorithm 2.14](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.28.pdf)
supports the related domain-ring method; the note correctly supplies its
own module argument rather than attributing that extension to the source.
Monic finiteness certificates for entire conductor quotients are retained
before rational-function localization.

On each `Q`-integral affine parameter piece, a computed nonzero localization
element leaves a closed complement with finitely many computable prime
components of strictly smaller dimension. The resulting finite recursion
retains all exceptional strata. Effective quantifier elimination finally
computes the actual constructible phase image, including inequalities and
deleted boundaries, so the accepted explicit-`W` procedure applies.

## Corrections and limits

This audit made three clarifications in Section 9: prescribed restrictions
to `c` are explicit input conditions; image Hilbert data are preserved using
a homogeneous monic basis; and the source ring is called *finitely
presented*, rather than ambiguously *finite*, as a graded algebra.

No unresolved algorithmic gap was found for this input. The PASS does not
extend to arbitrary unspecified normalizations, noncomputable coefficients,
or unpresented parameter restrictions. It gives no implementation, practical
complexity estimate, actual phase equations, numerical bound for the whole
three families, or decision which outcome holds for them. The independently
accepted explicit-`W` theorem is unchanged. The unrestricted fixed-C0 and
universal projective-curve STCI questions remain open.


---

## Source: 2026-10-17-generalization-normal-carrier-extremal-ray-synthesis.md

# Normal carriers: extremal-ray sufficiency and the all-degree local certificate

Date: 2026-10-17. Author: `normal_generalization`.

Status: **NEW PROOF AND SYNTHESIS, PENDING INDEPENDENT AUDIT.** The
normal-carrier torsion/index theorem, the intrinsic local power--socle
comparison, the symbolic-triple defect certificate, the accepted exclusion
of integral `C0` carriers of degree at most four, and the all-index-at-most-
four normal exclusion are premises. They are not reverified here. The new
step is the extremal-ray sufficiency theorem in Section 1 and its use in
Section 2 to turn the intrinsic local divisor budget into a necessary **and
sufficient** criterion for a mate. Sections 3--5 assemble, without enlarging
their scope, the strongest presently proved all-degree consequences.

This note does not exclude unrestricted normal carriers and does not resolve
the fixed `C0` or universal STCI problem.

## 1. A mate is equivalent to Hodge-index equality on a normal hypersurface

Let `k` be algebraically closed of characteristic zero. Let

```
X subset P3_k
```

be a normal integral hypersurface of degree `a`, let `H=O_X(1)`, and let
`C subset X` be an integral curve of degree `e`. If `C` is `Q`-Cartier, its
rational self-intersection `C^2` is defined.

**Extremal-ray theorem.** The following conditions are equivalent.

1. There is a hypersurface `G` not containing `X` such that
   `Supp(X intersect G)=C`.
2. Some positive Cartier multiple of `C` is linearly equivalent to a
   positive multiple of `H`.
3. `C` is `Q`-Cartier and

   ```
   C^2=e^2/a.
   ```

4. `C` is `Q`-Cartier and its numerical class is `(e/a)H` in
   `N^1(X)_Q`.

Thus, for normal hypersurface carriers in characteristic zero, there is no
additional global torsion or ambient-lifting condition after the
`Q`-Cartier self-intersection reaches the Hodge-index boundary.

### Proof

The implications (1) => (2) => (3) are immediate but are included to fix
the exact multiplicities. If the mate has degree `b` and divisor `mC` on
`X`, then

```
mC ~ bH,             me=ab,
C^2=(b/m)(H.C)=e^2/a.
```

Condition (4) also follows.

Assume (3). Put

```
g=gcd(a,e),     mu=a/g,     v=e/g,
Delta=mu C-vH in Cl(X)_Q.
```

Then

```
Delta.H=mu e-v a=0,
Delta^2=(a/g^2)(aC^2-e^2)=0.                       (1)
```

Choose a positive integer `q` such that `L=q Delta` is Cartier. The Hodge
index theorem for the normal projective surface `X` says that the
intersection form is negative definite on `H^perp subset N^1(X)_R`.
Equation (1) therefore makes `L` numerically trivial.

It remains to upgrade numerical triviality to linear triviality. The
hypersurface sequence

```
0 -> O_P3(-a) -> O_P3 -> O_X -> 0
```

and the vanishing of intermediate cohomology of line bundles on `P3` give
`H^1(X,O_X)=0`. In characteristic zero the identity component `Pic^0(X)`
is therefore trivial. A numerically trivial line bundle lies in `Pic^tau`,
whose quotient by `Pic^0` is finite, so `L` is torsion. The accepted
SGA/Kummer hypersurface input says that `Pic(X)` is torsion-free. Hence

```
L ~ 0.
```

Consequently a positive multiple of `Delta` is principal, and for some
`q'>0`

```
q' mu C ~ q' v H.                                  (2)
```

The canonical section of `O_X(q'mu C)`, transported through (2), is a
section of `O_X(q'v)` with zero divisor exactly `q'mu C`. The restriction
map

```
H^0(P3,O(q'v)) -> H^0(X,O_X(q'v))
```

is surjective because `H^1(P3,O(q'v-a))=0`. A lift is an ambient mate and
cannot be divisible by the equation of `X`, since its restriction is
nonzero. This proves (1). The same Hodge argument shows directly that (3)
and (4) are equivalent.

The proof isolates the characteristic-zero input precisely: it suffices in
any characteristic to know that every numerically trivial line bundle on
`X` is trivial. The local Jacobian/socle results used later have their
separate tame-index restriction.

## 2. The intrinsic local divisor is a necessary-and-sufficient mate test

Now suppose `C` is smooth. Retain the accepted notation from the intrinsic
normal-index theorem. Saturating the first normal symbol of `X` gives a
line quotient `B` of `N^*_(C/P3)` with `deg B=-ell`. At an on-curve point
`P`, let

```
r_P       = actual local Cartier index of C on X,
A_P       = vanishing order of the saturated first normal symbol,
D_(r_P),P = top ordinary-power/socle defect of the actual local
             Cartier multiple r_P C.
```

Put `R=lcm_P r_P`. The accepted intrinsic comparison, which assumes no
mate, constructs the effective rational divisor

```
E_X,C = sum_P (A_P+D_(r_P),P)/r_P [P]
```

and proves

```
deg E_X,C=ell-C^2.                                  (3)
```

Combining (3) with the extremal-ray theorem and Hodge index gives the new
sharp alternative

```
sum_P (A_P+D_(r_P),P)/r_P
    >= ell-e^2/a,                                   (4)
```

and, in characteristic zero,

```
equality in (4)  <=>  C has a mate on X.             (5)
```

Equivalently, define the **normal Hodge gap**

```
Gamma_X(C)=e^2/a-C^2
          =deg E_X,C-(ell-e^2/a) >= 0.               (6)
```

Then `Gamma_X(C)=0` is exactly the mate locus among normal `Q`-Cartier
carriers. If `Delta=mu C-vH`, equation (1) reads

```
Delta^2=-mu^2 Gamma_X(C).                            (7)
```

This removes a formerly separate global obligation: finite local indices
alone still do not imply torsion, but finite local indices **plus equality
in the intrinsic local budget** do. The equality forces the global Cartier
ray and the ambient lift.

The line-bundle form of the accepted comparison remains stronger than
(4):

```
O_C(R E_X,C)=B^(-R) tensor O_X(-RC)|C.
```

It should be retained in positive genus even when only the scalar Hodge gap
is being used.

## 3. Exact exponent and minimal mate once the boundary is reached

Assume the equivalent conditions of Section 1. For every point of `C` on
`Sing(X)`, let `r_P` be the actual local Cartier index, and put

```
R=lcm_P r_P,       g=gcd(a,e),
mu=a/g,            v=e/g.
```

The accepted local detection theorem now gives the exact order of the
primitive Weil class and not merely an upper bound:

```
t=R/gcd(R,mu).                                      (8)
```

The mate degrees on this fixed carrier are exactly

```
b=k t v,       k=1,2,3,... .                        (9)
```

The minimal generic transverse length is

```
n_min=mu t=lcm(mu,R).                               (10)
```

In particular

```
a divides e^2 R.                                    (11)
```

Equations (8)--(10), together with (5), give a complete numerical
description on a fixed normal carrier: the intrinsic equality decides
existence; the actual local indices determine the least mate and every
higher mate. No independent section-lifting or hidden global torsion factor
remains.

This is not an effective classification of all normal carriers: computing
`C^2`, the local indices and the full defects can still be difficult, and
unbounded indices occur even in elementary local hypersurface models.

## 4. Strongest current all-degree consequence for the fixed rational quartic

Specialize to

```
C0=[s^4:s^3t:st^3:t^4],       e=4,
N_C0^*=O_P1(-7)^2.
```

Let `X` be a normal integral carrier of degree `a`. If `C0` is not
`Q`-Cartier, it has no mate on `X`. If it is `Q`-Cartier, define
`ell,A_P,r_P,D_r,P` as above. The exact normal-carrier decision criterion
is

```
sum_P (A_P+D_(r_P),P)/r_P = ell-16/a.               (12)
```

Every equality candidate satisfies all of the following, in every mate
degree.

1. `a>=5`. With `g=gcd(a,4)`, `mu=a/g`, `v=4/g` and
   `R=lcm_P r_P`,

   ```
   t=R/gcd(R,mu),
   b_min=v t,
   n_min=lcm(mu,R),
   a | 16R.
   ```

   The accepted low-degree theorem also forces `b_min>=5`.

2. Let `s=max_P r_P`. The accepted symbolic-triple improvement of the
   local power--socle inequality gives

   ```
   4a^2-(7s+6)a+16s <= 0,
   s >= ceil(a(4a-6)/(7a-16)).                       (13)
   ```

   The separately accepted all-index-at-most-four theorem strengthens the
   small cases to

   ```
   s>=5.                                             (14)
   ```

   Conversely, for each fixed `s`, (13) bounds `a` by the larger root

   ```
   a <= ((7s+6)+sqrt((7s+6)^2-256s))/8.              (15)
   ```

   This is a finite carrier-degree reduction for every bounded-index
   class, not a universal index bound.

3. The pointwise Frobenius identity and local power formula hold:

   ```
   2 sum_i length(T_i)_P=r_P D_(r_P),P,
   D_n,P=(n/r_P-1)A_P+(n/r_P)D_(r_P),P.              (16)
   ```

   Thus `r_P D_(r_P),P` is even; in particular a positive defect at odd
   index is at least two.

4. In the constant-direction branch `ell=7`, the first-layer torsion
   divisor `T_3` of the global symbolic triple obeys the accepted
   carrier-wide certificate

   ```
   2 <= deg T_3
      <= sum_(r_P=2) A_P
         +(1/2)sum_(r_P>=4) r_P D_(r_P),P.            (17)
   ```

   Its support must also satisfy the accepted apolar condition: degree two
   forces the appropriate doubled endpoint divisor; degree three forces
   either the mixed three-point divisor or an endpoint doubled divisor plus
   one point. Index-three primitive multiples contribute neither local
   defect nor symbolic-triple torsion.

Statements (12)--(17) are one simultaneous all-degree certificate. They do
not treat different singular points as separate hypothetical
presentations, replace actual indices by ADE labels, or discard higher
jets. In particular, every hypothetical normal carrier lies on the
Hodge-index equality boundary and must contain an on-curve singularity of
index at least five; as carrier degree grows, its maximum actual index must
grow at least asymptotically like `4a/7`.

## 5. What was removed, and what remains

The new theorem removes **global lifting as a separate hypothesis or
obligation in the normal branch**. More precisely, after `Q`-Cartierness,
the scalar equality `C^2=e^2/a` (or equivalently equality in (4)) forces:

* torsion of the primitive Weil relation;
* its exact order from actual local indices;
* an effective Cartier divisor supported exactly on `C`;
* and an ambient hypersurface lifting that divisor.

The remaining boundaries are exact.

1. **Normality.** The Hodge step applies to Cartier multiples on a normal
   surface, and the accepted local formula uses normality in the colon
   identity and in regularity of `z^r/h`. A nonnormal carrier requires its
   normalization, conductor colengths, residual phases and possibly several
   inverse branches. The accepted singleton Cartier-lift conductor formula
   is a separate partial replacement, not a consequence of this note.

2. **Unbounded actual local indices.** No universal bound on `r_P` follows
   from smoothness of `C0`, the carrier degree, or surface multiplicity.
   The local models `xy-z^r=0` with the smooth curve `(x,z)` have arbitrarily
   large index and zero primitive defect. Equations (13)--(17) say exactly
   how such high indices must be distributed globally but do not exclude
   them.

3. **Curve-specific symbolic obstruction.** The improvement from the
   general balanced-rational threshold to the fixed `C0` certificate uses
   the accepted nonzero constant-direction primitive-triple obstruction.
   An analogous obstruction is not proved for every balanced rational
   curve.

4. **Characteristic.** Section 1 works whenever numerically trivial line
   bundles on `X` are trivial. Characteristic zero supplies this for normal
   hypersurfaces through the accepted Picard inputs. The local
   power--socle theorem extends when every actual index is prime to the
   characteristic, but wild indices and a characteristic-`p` replacement
   for the global Picard step remain open.

5. **Other generic algebras.** If both defining equations have generic
   normal order at least two, neither one is a normal order-one carrier and
   the generic algebra need not be curvilinear. That entirely-thick branch
   remains governed by the separate conormal/socle and formal-root program.

The normal branch has therefore been reduced, without a degree-by-degree
mate search, to a sharply stated geometric question:

> Can a normal integral hypersurface containing `C0` realize the extremal
> equality `C0^2=16/a` while satisfying the exact local divisor,
> high-index, parity and symbolic-triple support conditions (12)--(17)?

A proof that the intrinsic inequality (4) is always strict for `C0` would
close every normal carrier in every degree at once. It would not by itself
close nonnormal or entirely-thick carriers.


---

## Source: 2026-10-19-regular-reducible-root-independent-audit.md

# Independent audit: a regular formal surface cannot lift the equal split root

Date: 2026-10-19. Reviewer: `regular_reducible_audit`. The local Cartier,
intersection-length, completion-transitivity, and companion-containment
steps were separately checked by `regular_reducible_audit/local_check`.

Status: **PASS for the precise conditional nonexistence statement below.**
This is an independent review note, not a promoted result record. No accepted
mathematics or canonical metadata is changed. In particular, this note does not
apply the smooth-root statement STCI-R-0005 to a singular root.

## 1. Exact statement and inputs

Work over an algebraically closed field of characteristic zero with the fixed
smooth rational quartic `C0`. Let

    B = Bl_C0(P3),  E = P1 x P1,  O_E(E) = O_E(7,-1).

The first factor is the base `C0`. Fix `q >= 1`, and let `D1,D2` be distinct
smooth integral divisors of class `(1,q)` on `E`. Put

    Z = D1 union D2

with its reduced scheme structure. Suppose compatible embedded effective
Cartier lifts on all exceptional neighborhoods produce a Cartier formal
surface `V` in `B-hat_E`, whose reduction modulo the exceptional parameter is
exactly `Z`.

**Claim audited.** Such a lift cannot have `V` regular at every point of at
least one full component `Di`.

The words “at every point” are essential: regularity only at the generic
point of a component is automatic here and does not satisfy this hypothesis.
The assertion permits arbitrary tangency and intersection multiplicities
between `D1` and `D2`.

The accepted blowup conventions and the branch normalization, resolution,
multiplicity, and plane-genus mechanisms are recorded in
[STCI-R-0005](../results/smooth_root_formal_obstruction.md) and its
[independent source audit](2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md),
especially Sections 1--3 and 5--6. They are used within their stated scope;
the accepted smooth-root exclusion itself is not replayed. The new points
checked here are the self-intersection of a component of a reducible root,
the change of completion center, retention of the companion component, and
the resulting numerical contradiction.

The primary algebraicity input is
[Bost, Theorem 3.5 and Corollary 3.8, printed pp. 187--188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=27).
The smooth-center version applies to a smooth connected projective curve
and a smooth formal surface with ample normal line; its algebraic closure
has the same dimension. The lci-center corollary also permits a proper
connected center that is not smooth. These are geometric results over a
field, with no number-field or analytic-convergence hypothesis. The
accepted source audit checks that the printed dimension condition includes
curves; the text extraction of the PDF loses the equality stroke.

## 2. Local algebra and the component normal degree

Write `E=(u)`. At an intersection point `p`, choose equations `a,b` of
`D1,D2` on `E` and lifts to the completed regular local ring of `B`.
After multiplying the equation of `V` by a unit, its equation is

    g = a*b + u*h.

At `p`, both `a,b` vanish, so the linear part of `g` is `h(p)*u`.
Consequently regularity of `V` at `p` forces `h` to be a unit. This argument
does not require that `a,b` be independent parameters: it includes tangent
components and higher intersection multiplicities.

Inside the regular full completed local ring of `V` at `p`,

    u = -a*b/h,
    I_D1 = (u,a) = (a),   I_D2 = (u,b) = (b).

Thus both components are Cartier there and

    length O_V,p/(a,b) = length O_E,p/(a,b).

Away from their intersection, the root is smooth and the differential of
its local equation already has a nonzero component tangent to `E`; hence
`V` is automatically regular there. It follows in particular that
regularity along one full `Di` implies regularity along all of `Z`.

The exceptional parameter is a nonzerodivisor on `V`: locally `g mod u`
is a nonzerodivisor on the smooth integral surface `E`, so `u,g` form a
regular sequence. Its zero divisor on `V` is exactly `D1+D2`. Restricting
the associated divisor identity to `D1` gives

    deg N_(D1/V)
       = deg O_D1(E) - (D1.D2)_V
       = (7q-1) - (D1.D2)_E
       = (7q-1) - 2q
       = 5q-1.                                      (1)

This is a normal line of positive degree for every `q>=1`, hence is ample
on the smooth projective curve `D1`. The same computation holds for `D2`.

## 3. Algebraization and why the other component is retained

Complete `V` along `D1`. The inclusion `D1 subset E subset B` permits
completion in two stages; completing `B-hat_E` further along `D1` gives
`B-hat_D1`. The resulting `V-hat_D1` is a closed smooth formal surface in
`B-hat_D1`, admits `D1` as its scheme of definition, and has normal line
(1). Bost's smooth-center theorem therefore gives an integral algebraic
surface `W subset B` containing this formal branch.

Formal containment along `D1` must not be replaced by an unsupported
claim that `W` has only this branch. Nevertheless it forces the algebraic
companion `D2` to be contained in `W`:

1. Choose any `p in D1 intersect D2`; such a point exists because the
   total intersection number is `2q>0`.
2. Let `w` be a local algebraic equation of `W` in `B` near `p`. It is
   zero on `V-hat_D1` and hence in its full maximal-ideal completion at
   `p`.
3. That full completion is exactly the full completion of the original
   `V` at `p`, by transitivity of completion. It contains the completed
   germ of `D2` as the quotient by `(b)` in Section 2. Thus `w` is zero
   in the completion of `O_D2,p`.
4. The map from the noetherian local domain `O_D2,p` to its completion
   is injective. Therefore `w` already vanishes in `O_D2,p`. This gives
   algebraic containment on a nonempty open subset of `D2`; integrality
   of `D2` and closedness of `W` give `D2 subset W` globally.

The argument uses an actual intersection point, the same full completed
branch at that point, and the algebraic curve `D2`. Mere abstract
isomorphism of formal surfaces would not justify it. Nor would it
justify retaining a second component disjoint from the completion center.
Here it gives scheme-theoretic containment of the reduced curves
`D1+D2` in the effective Cartier divisor `W|E` on the smooth surface `E`.

There is a shorter valid route in this specific setting. Section 2 shows
that `V` is smooth along its entire support `Z`; the center `Z` is proper,
connected, and Cartier in `V`. Its normal line is `O_Z(E)`, of degree
`7q-1>0` on each irreducible component, hence ample on `Z`. Bost's lci-center
Corollary 3.8 then algebraizes the full `V` directly, and reduction modulo
`u` immediately retains both components. The smooth-center route above
also proves the proposed continuation step explicitly.

## 4. Normalization, degree, and Hodge index

The selected formal branch is regular. On the algebraic normalization
of `W` it lifts uniquely and is the completion of a regular neighborhood
of an embedded copy of `D1`. This is the same finite-normalization and
whole-curve gluing mechanism checked in Section 3 of the accepted source
audit, now applied to the smooth center `D1`. Extra algebraic branches
are allowed. Resolve the normalization away from this regular
neighborhood, obtaining a smooth projective surface `T` with

    D1^2 = 5q-1.

Since `u` is nonzero on the selected formal branch, `W` is distinct from
`E`. Its image `S subset P3` is an integral surface and `W` is its strict
transform. Let `H` be the pullback to `T` of a hyperplane and put
`d=deg S`. Then

    H is nef,  H^2=d>0,  H.D1=4q.

Hodge index on `T` gives

    d*(5q-1) <= (4q)^2,
    d <= 16q^2/(5q-1) <= 4q,                         (2)

where the last inequality is equivalent to `q>=1`. No ruled-surface
classification or strict high-self-intersection threshold is needed for
this equal split case.

Let `m` be the generic order of `S` along `C0`. The restriction `W|E`
has degree `m` on a generic exceptional fiber and contains `D1+D2`.
Each component has fiber degree `q`; thus

    m >= 2q.                                         (3)

This lower bound remains valid with every additional algebraic branch,
exceptional intersection component, and multiplicity retained.

## 5. Numerical contradiction

The accepted plane-section argument for an integral degree-`d` surface
of generic multiplicity `m` along the smooth quartic gives

    (d-1)(d-2) >= 4m(m-1)
                >= 4(2q)(2q-1)
                 = 16q^2-8q.                        (4)

It uses a general integral plane section, transverse intersection with
the four points of `C0`, and the arithmetic genus after blowing up those
points. No assumption of ordinary plane singularities or absence of
residual surface branches is present.

For positive integral `d<=4q`,

    (d-1)(d-2) <= (4q-1)(4q-2)
                = 16q^2-12q+2
                < 16q^2-8q,

because the positive difference is `4q-2`. This contradicts (4). The
boundary `q=1` is included: (2) gives `d<=4`, whereas (4) demands at least
`8` on its left side, whose maximum in that range is `6`.

## 6. Outcome, limitations, and frontier impact

The proposed theorem passes the audit after making the following points
explicit: regularity is along a full component, not just generically;
the normal degree is computed in the regular formal surface; completion
along the component retains the same full local branch at its
intersection with the companion; and companion containment is an
algebraic consequence of local vanishing, rather than an assumed
equality `W|E=Z`.

This excludes an all-orders Cartier lift of the specified reduced equal
split root whenever its total formal surface is regular along `Z`.
It does not exclude a lift whose formal surface is singular at one or
more points of `D1 intersect D2`, roots with different component classes,
nonreduced roots, or any actual complete intersection without a separate
bridge to this exact formal-lift setting. In particular it supplies no
unrestricted characteristic-zero STCI conclusion.

Authority status remains **reviewed proposal/evidence, not promoted**.
No new computation is needed for the argument, and no finite checks or
load-only CAS tests are offered as a substitute for the geometric proof.


---

## Source: 2026-10-19-regular-singular-root-smoothing-audit.md

# Independent audit: regular formal surfaces with singular movement-two roots

Date: 2026-10-19. Reviewer: `regular_singular_smoothing_audit`.

**Outcome: PASS for the precise conditional nonexistence statement below.**
The new smoothing step is valid. It closes the reduced singular-root case
only when the resulting formal surface is regular at every point of the
whole root. The argument does not establish that an arbitrary all-orders
Cartier lift, or an arbitrary actual complete intersection, has this
regularity property. No canonical result has been changed by this audit.

## 1. Exact scope and authority

Work over an algebraically closed field `k` of characteristic zero with the
fixed rational quartic `C0` and the accepted balanced normal bundle
`N_(C0/P3)=O_P1(7)^2`. Put

    B=Bl_(C0)(P3), E=P1_base x P1_direction,
    O_E(E)=O_E(7,-1), H|E=O_E(4,0).

Let `r>=2`, and let `Z` be a **reduced effective Cartier divisor** of class
`(2,r)` on `E`, finite flat of degree `r` under the first projection
`p:Z->P1_base`. Suppose compatible embedded effective Cartier lifts of
`Z` on every exceptional neighborhood define a formal surface `Vhat` that
is **regular along all of `Z`**. Then such a lift does not exist.

The promoted input [STCI-R-0005](../results/smooth_root_formal_obstruction.md)
concerns a smooth full root; its [accepted independent audit](2026-10-15-generalization-smooth-root-formal-nonexistence-independent-audit.md)
supplies the algebraic branch, ruled-model degree, and plane-section
arguments used as premises here. This review checks their new interface
with a singular root and supplies the new smoothing argument. It does
not reopen the inherited proof or its accepted numerical inequalities.
[STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md)
is not needed: ampleness and smoothing below hold for every finite-flat
root of the indicated class, including components of differing slopes.

## 2. Normal line, connectedness, and algebraization

Let `u` be an exceptional equation and `g` a local equation of `Vhat`.
Since `g mod u` cuts out the Cartier divisor `Z` in `E`, `u` remains a
nonzerodivisor on `Vhat`, and

    I_Z O_Vhat=(u,g)O_Vhat=(u),
    N_(Z/Vhat)=O_Z(E)=:N=O_Z(7,-1).

Thus the exceptional topology on `Vhat` is its `Z`-adic topology. In
particular it is a closed formal subscheme of `B` completed along `Z`.
Regularity of `Vhat`, rather than smoothness of `Z`, is the hypothesis
that gives a smooth formal surface over the perfect field `k`.

The exact sequence

    0 -> O_E(-2,-r) -> O_E -> O_Z -> 0

and Kunneth show `H0(O_Z)=k`, because `H0(O_E(-2,-r))` and
`H1(O_E(-2,-r))` vanish. Hence `Z` is connected. Each irreducible component
has class `(a,b)` with `0<=a<=2`; finiteness over the first factor gives
`b>=1`. Consequently

    deg(N|component)=7b-a >= 5.

The normal line is therefore ample on `Z`, without any descent or
equal-slope hypothesis. The finite-projection hypothesis matters here:
a vertical fiber of class `(1,0)` would instead have normal degree `-1`.

[Bost, Corollary 3.8, printed p. 188](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf#page=28)
allows a proper connected lci scheme of definition in a smooth formal
scheme and assumes its normal bundle ample; it does not require that
scheme of definition to be smooth. It gives an integral algebraic
closure `W` of dimension two containing the formal branch. The dimension
condition is `dim Z>=1`; the PDF text extraction renders its sign
incorrectly. This is the appropriate variant for singular `Z`.

## 3. Normalization still preserves the entire singular root

At a closed point `z` of `Z`, the maximal-ideal completion of the chosen
formal surface is regular of dimension two. It is a minimal completed
branch of the integral algebraic surface `W`. Excellence identifies the
completed normalization factors of `W` with the normalizations of its
completed branches. The selected branch is already normal and regular.
See [Stacks, Lemma 15.110.8 and its proof](https://stacks.math.columbia.edu/tag/0C2E).

The compatibility argument in the accepted smooth-root audit uses only
normality of the formal surface. On a normal-domain formal chart with
ring `R`, the algebraic coordinate domain of `W` injects into `R` through
the chosen minimal branch. Every element of its finite integral closure
maps into `Frac(R)` and is integral over `R`, hence belongs to `R`.
Uniqueness makes these maps agree on overlaps. The resulting morphism
`Vhat->Wnu` reduces to a section

    Z -> Wnu x_W Z -> Z.

Because normalization is finite, this section is a closed immersion.
Its image is a copy of the original `Z`, including its singularities,
and `Wnu` is regular along it. The formal neighborhood of that image is
the selected branch. This does not identify any additional branch of
`W` with it.

Resolve the projective normalization away from this regular neighborhood,
obtaining a smooth projective surface `T` containing the unchanged
Cartier curve `Z`. Resolution preserving a regular open is available
for surfaces; see [Stacks, Resolution](https://stacks.math.columbia.edu/tag/0BGJ)
and the accepted branch audit cited above. If `S` is the integral image
surface in `P3` and `H` is its hyperplane pullback to `T`, then

    Z^2=deg N=7r-2,   p_a(Z)=r-1,
    H.Z=4r,          H^2=d=deg S>0.

`W` is not `E`, since `u` is nonzero on the formal surface. Thus `W` is
the strict transform of `S` and the map to `S` is birational. `H` is nef.

## 4. Independent cohomology calculation

The divisor sequence tensored by `O_E(7,-1)` is

    0 -> O_E(5,-r-1) -> O_E(7,-1) -> i_*N -> 0.

Push this sequence along the first projection `p_E:E->P1`. Both direct
images of `O_E(7,-1)` vanish, while

    R1(p_E)_* O_E(5,-r-1)=O_P1(5) tensor H1(P1,O(-r-1)).

Since the latter vector space has dimension `r`, this gives the stronger
identity

    p_*N = O_P1(5)^r.                                      (1)

In particular

    H1(Z,N)=0,  H1(Z,N tensor p^*O_P1(-1))=0,
    h0(Z,N)=6r.

For a finite morphism, `p^*p_*N -> N` is surjective: on affine rings it
is the multiplication map `B tensor_A M -> M`. Equation (1) therefore
proves that `N` is globally generated. These assertions do not assume
that `Z` is integral or nonsingular. Equivalently, the two proposed
Kunneth computations have kernels `O_E(5,-r-1)` and
`O_E(4,-r-1)` respectively and give the same vanishings.

## 5. Smoothing on the fixed algebraic surface

This is the new step. Embedded deformations of the Cartier curve `Z` in
the smooth surface `T` have tangent space `H0(N)` and obstruction space
`H1(N)`. Local lifts exist by lifting a regular sequence. Thus the Hilbert
scheme of `T` is smooth at `[Z]`. For a source that explicitly covers a
singular lci subscheme, use [Hartshorne, *Lectures on Deformation Theory*,
Theorem 6.3 and its following remark, and Theorem 9.3](https://math.berkeley.edu/~robin/math274root.pdf#page=42).
The introductory Theorem 1.1 alone assumes a nonsingular subscheme and
would not by itself justify this application.

Choose a smooth integral neighborhood `A` of `[Z]` in the Hilbert scheme,
and let `U subset T x A` be its universal curve. After shrinking `A`, it
is a relative effective Cartier divisor. Locally, the universal ideal
reduces to the principal Cartier ideal `(f)` on the central fiber;
flatness and Nakayama lift its generator to a local equation `F`.
Properness lets these local neighborhoods cover every nearby fiber.
The relative Cartier criterion is [Stacks, Lemma 31.19.9](https://stacks.math.columbia.edu/tag/062Y).

At a closed point `z` of the central `Z`, choose parameters `t_j` on `A`
whose tangent vectors form a basis of `H0(N)`. Modulo the central ideal,
the coefficients `partial F/partial t_j` are precisely the evaluations
of those normal sections. Global generation gives one with nonzero value
at `z`. Hence `F` is not in the square of the maximal ideal of the smooth
ambient `T x A`, and `U` is regular, equivalently smooth over `k`, at `z`.
This also covers the original singular points of `Z`.

The nonsmooth locus of `U` over `k` is closed. Its image in `A` is closed
because `U->A` is proper, and it misses `[Z]`. Shrink `A` again to make
all of `U` smooth over `k`. The generic fiber of `U->A` is regular,
since its local rings are localizations of regular local rings of `U`.
Its field `k(A)` is perfect in characteristic zero, so this generic
fiber is smooth. The nonsmooth locus of the morphism `U->A` consequently
has proper closed image. There is a nonempty open of smooth fibers.
Here one must distinguish smoothness of the total space over `k` from
smoothness of its map to `A`; generic smoothness and properness supply
the latter only over a dense open. For the field-smoothness criterion see
[Stacks, Lemma 33.25.2](https://stacks.math.columbia.edu/tag/04QP).

Since `h0(O_Z)=1`, upper semicontinuity gives `h0(O_(U_a))<=1` near
`[Z]`; the fibers are nonempty, so this equals one. A smooth proper fiber
over algebraically closed `k` is therefore connected and integral.
See [Stacks, Lemma 36.32.1](https://stacks.math.columbia.edu/tag/0BDN).
Thus a nearby smooth connected curve `Z_a subset T` exists. The universal
Cartier family over connected `A` makes it algebraically equivalent to
`Z`, so

    Z_a^2=7r-2,   g(Z_a)=r-1,   H.Z_a=4r.                 (2)

No claim that this smoothed curve lies on the original exceptional
divisor, or that it yields a new embedded formal lift in `B`, is needed.
Its only role is to permit the established ruled-surface numerical
argument on `T` with the invariants (2).

## 6. Numerical contradiction and boundary

For `r>=2`,

    7r-2 > 4(r-1)+5.

Apply the accepted high-self-intersection and nef-divisor argument to
`Z_a subset T`. [Hartshorne, *Curves with high self-intersection on
algebraic surfaces*, Theorem 4.1](https://www.numdam.org/item/PMIHES_1969__36__111_0.pdf#page=12)
gives the ruled model near this smooth curve; the accepted intersection
argument gives

    d <= max_(a integer >=1) [8ra-(7r-2)a^2] = r+2.        (3)

For the opposing bound, use the **original** `Z`, not its smoothing.
Formal containment in `W` reduces modulo `u` to scheme-theoretic
containment `Z subset W|E`. The difference is effective on the smooth
surface `E`. Its generic fiber degree shows that the generic
multiplicity `m` of `S` along `C0` satisfies `m>=r`. Extra exceptional
components or other branches can only add effective fiber degree.
The accepted general-plane-section argument now gives

    (d-1)(d-2) >= 4m(m-1) >= 4r(r-1).                   (4)

But (3) gives `(d-1)(d-2)<=r(r+1)`, and

    4r(r-1)-r(r+1)=r(3r-5)>0  for every r>=2.

This contradiction passes the proposed exclusion.

The added hypothesis is regularity of the **whole formal surface**.
At a singular point of the reduced root, smoothness of the ambient
threefold and the Cartier property of the formal equation alone do
not imply it. If the formal equation is locally `g=f+u*a+...` with
`df=0` on `E`, regularity requires a nonzero linear contribution in
the transverse direction, for example `a(z)!=0`. The audit does not
prove that contribution exists for every root lift. Singular formal
surfaces remain outside this theorem, as do arbitrary actual complete
intersections without a bridge to the stated formal object.

The proof of Sections 2--6 in fact does not use reducedness once a
finite-flat effective Cartier `Z` of class `(2,r)` and a regular formal
surface are supplied: the component ampleness criterion, sequence (1),
and universal-family smoothing still apply. This is a transparent
scope strengthening of the argument, not a claim that nonreduced roots
in the actual STCI problem satisfy its regularity hypothesis.

## Review record

The reviewer independently reconstructed the normalization and smoothing
interfaces and both cohomology calculations. A separate subreviewer,
`smoothing_check`, checked the Hilbert universal-family argument and the
primary deformation, relative Cartier, and semicontinuity references.
No exact-CAS calculation, inherited proof rerun, canonical promotion,
or git operation was used. The regularity boundary is unresolved by
this argument and must survive any later result promotion.


---

## Source: 2026-10-20-conditional-2-12-singular-gluing.md

# Conditional (2,12;6,16;2): finite singular-root bridge and Picard gluing

Date: 2026-10-20. Author: `singular_gluing` worker.

Status: **new proposal and exact reduction; finite bridge, strata,
gluing formulas and torsion matrix independently reviewed by
`incidence_audit` with verdict PASS on 2026-10-20**.
The inherited premises below are promoted. The finite singular-root
extension and the explicit gluing/determinant presentation in this note
are new arguments, not additional promoted records. No accepted verifier
or inherited proof was rerun. No low-order nonempty incidence or global
pair is asserted.

## 1. Exact scope and authority

Work over an algebraically closed field `k` of characteristic zero, with

    C0=[s^4:s^3t:st^3:t^4] in P3,
    E=N*_(C0/P3)=O_P1(-7)^2.

The conditional global object is an actual complete intersection
`Y=(F6,G16)` with reduced support **exactly** `C0`, FULL generic ordinary
initial ideal a coprime binary CI of degrees `(2,12)`, and actual
degree-two kernel a line subbundle of movement two. Thus

    R=O_P1(-16) -> Sym^2 E=O_P1(-14)^3,
    f in H0(O_P1(2)) tensor Sym^2(k^2),

and the three base-quadratic coefficients of `f` have no common zero.
The full root `Z=(f)` is a Cartier divisor of class `(2,2)` in
`S=P1_base x P1_direction`. The Picard line is

    L=O_Z(1,-1),               required: L^12=O_Z.

Here bidegrees list the base ruling first. Interchanging both signs in
`L` changes none of its triviality or torsion conditions.

Inherited promoted premises, used with their literal hypotheses:

* [STCI-R-0010](../results/saturated_first_relation_normal_flatness.md):
  the actual ordinary normal algebra is a locally free CI family with
  the same degrees `(2,12)` and coprime first/second pair in **every**
  fiber. This theorem requires sole reduced support `C0`, the FULL
  generic CI hypothesis, and the ACTUAL saturated first relation.
* [STCI-R-0008](../results/spectral_root_picard_criterion.md): the graded
  second quotient relation gives the full-scheme condition `L^12=O_Z`.
  It does not give embedded or global realization.
* [STCI-R-0011](../results/moving_nonreduced_spectral_root_obstruction.md):
  full spectral descent makes this moving root reduced and forces
  every component to have the same slope. Thus `Z` is integral of
  class `(2,2)`, or is the union of two distinct `(1,1)` curves.
* [STCI-R-0007](../results/quadratic_root_obstruction_model.md): the
  universal first incidence and the complete twenty-five-pairing
  second test are valid on the full basepoint-free quadratic family,
  including singular roots. The promoted actual-CI interface there
  invokes the smooth-root bridge R-0006. Section 2 supplies a new
  finite bridge to justify necessity at singular roots in this exact
  normal-flat setting.

The indexed [STCI-R-0006](../results/actual_ci_smooth_root_bridge.md)
and its source proof expressly assume a smooth full root. No previously
promoted finite singular-root bridge was found. The October 19
normal-flatness results do not, by their statement alone, assert
embedded Cartier lifting on singular roots. This is the authority gap
addressed by the proof below; it is not resolved by silently broadening
R-0006.

## 2. Finite bridge without smoothness of the root

**Proposed finite bridge.** Under the actual-pair hypotheses of section
1, the common order-two transforms of the two original equations on
`B=Bl_(C0) P3` have local ideal

    I'=(p,u^10)                                                   (1)

at every point of the full root `Z`. Here `u` is an exceptional equation,
`p mod u` is a unit multiple of the actual Cartier equation `f` of `Z`
in the exceptional divisor, and `(p,u)` is a regular sequence. There
is no assertion that the surface `(p)` is smooth. Consequently this
intersection supplies an embedded Cartier lift of `Z` on
`V(I_E^10)` and all exceptional neighborhoods `E_m=V(I_E^(m+1))`
with `m<=9`. In particular both the first and the complete second
ambient obstruction necessarily vanish even when `Z` is singular.

**Proof.** Normal flatness identifies the relative graded ideal in
`Sym E` with one locally generated by a degree-two form `f` and a
degree-twelve form `g`, coprime in every fiber. Fix a closed point of
`C0`, and work in the actual local ring `A=O_(P3,c)`, filtered by the
regular curve ideal `J=I_(C0,c)`. Choose actual local lifts

    P in I intersect J^2,          H in I intersect J^12

whose symbols are these two local generators of the FULL relative
graded ideal. Then `I=(P,H)` in the actual local ring. Indeed initial
order reduction using `f,g` gives

    I subset (P,H)+J^N                 for every N;

Krull intersection in the finite module `A/(P,H)` gives the asserted
equality. This is not a statement merely over `k(C0)` or after
completion. The two pairs `(F,G)` and `(P,H)` minimally generate the
same height-two CI ideal, so their change matrix is in `GL2(A)` by
Nakayama.

The two degree-two symbols of the displayed global equations must
jointly generate `R`: the actual degree-two kernel is generated by
their local scalar combinations. If their scalar coefficients both
vanished in the fiber at a base point, its image could not equal the
line subbundle `R` in that fiber. More concretely their coefficients
are

    alpha in H0(O_P1(8)),          beta in H0(O_P1(48)).

They have no common zero. Neither is identically zero, since a sole
section of either positive-degree line bundle has a zero and could
not generate `R` everywhere. Thus both original equations have
generic order two and their original strict transforms are obtained
by division by the common exponent `u^2`.

Pull back the invertible change matrix and divide both entries by
`u^2`. The resulting ideal is exactly

    (F/u^2,G/u^2)=(P/u^2, u^10 H/u^12).

At each point of `Z`, the reduction of `H/u^12` on the exceptional
divisor is the value of `g` in that root direction. Fiberwise
coprimality says this is nonzero, including a ramified fiber or a
singular point of the total root curve. Hence `H/u^12` is a unit in
the local blowup ring and (1) follows with `p=P/u^2`.

The restriction of `p` modulo `u` generates the Cartier ideal of `Z`
in the smooth exceptional surface. Therefore `(u,p)` is a regular
sequence. Reducing (1) modulo `u^10` leaves the principal invertible
Cartier ideal generated by `p`. On overlaps these are local
generators of the **same actual ideal**, so they glue with units.
This gives the stated embedded Cartier lift and its lower stages.

This argument uses no UFD assertion for the possibly singular surface
`(p)`, and it does not deduce divisibility just from generic transverse
multiplicity. The unit is supplied by the uniform relative standard
basis and its fiberwise resultant. The exponent `u^10` is retained:
dividing the second standard-basis equation by `u^12` in the
transformed ideal, or saturating by `u`, would destroy the object.

For support, the restrictions of the original strict equations on
`E` are `alpha*f,beta*f`; their coefficient pair has no common zero.
Their intersection on `E` has support exactly `Z`, with no whole
exceptional fiber. Off `E` the blowup is an isomorphism and the
original supported CI has no common point. This proof concerns a
supported CI; with residual components allowed, these conclusions
require a separate argument.

**Scope boundary.** Equation (1) and the finite lifting conclusion use
the actual supported pair and all the normal-flatness hypotheses. An
arbitrary low-order incidence point does not come equipped with
`P,H`, an invertible actual generator change, or this certificate.
No inference of actual existence is made in the reverse direction.

## 3. Reduced root types and a uniform nontriviality calculation

An integral `(2,2)` curve has arithmetic genus one. If singular, its
normalization is `P1` and its total delta invariant is one, so its
only planar singularity in characteristic zero is a node or a cusp.
Each integral `(1,1)` component is a smooth rational curve. Two
distinct such components have intersection length two: either two
transverse nodes, or one tangency of length two. These cases exhaust
the reduced equal-slope roots; a special nonreduced **fiber** of
`Z -> P1` remains allowed.

The following calculation applies uniformly to every full Cartier
divisor of class `(2,2)`:

    0 -> O_S(-1,-3) -> O_S(1,-1) -> L -> 0.

Kunneth gives `H0(O_S(1,-1))=0` and
`H1(O_S(-1,-3))=0`. Therefore

    H0(Z,L)=0,                       L is not O_Z.                (2)

On every reduced equal-slope component `deg L=0`. Thus `L` belongs to
the multidegree-zero Picard group and (2) rules out its identity
element on all the strata under consideration.

## 4. Cuspidal and tangent-component strata are empty

For an integral cuspidal root, normalization has local inclusion

    k[[t^2,t^3]] subset k[[t]],       conductor (t^2).

The quotient of local units contributing to `Pic^0` is
`1+t*k mod t^2`, with multiplication giving addition in `k`. Since
the normalization is rational, `Pic^0(Z)=G_a`. In characteristic zero
this group has no nonzero 12-torsion. Hence `L^12=O` would force
`L=O`, contradicting (2). The entire cuspidal stratum is excluded.

For two `(1,1)` components tangent with intersection length two, the
normalization has two rational components and the conductor quotient
identifies their length-two jets. Locally a model is

    k[[x,y]]/(y*(y-x^2)) -> k[[t]] direct-sum k[[s]],

with conductor `(t^2,s^2)`. Modulo the conductor the image is the
diagonal `k[e]/(e^2)` in two copies of that ring. The local unit
quotient has a multiplicative constant and an additive first jet;
the independent global constants on the two normalization components
remove the multiplicative factor. Consequently `Pic^0(Z)=G_a`.
The same torsion-free argument and (2) exclude the full tangent-pair
stratum. No passage to the reduced intersection point is made: its
length-two conductor jet is precisely the additive gluing datum.

These exclusions precede ambient lifting and do not depend on a
smooth-root theorem.

## 5. Actual nodal gluing, including its equation

Let `Z` be integral nodal, with normalization
`nu:P1_T -> Z` and preimages `p,q` of its node. The two ruling maps
`x,y:P1_T -> P1` have degree two. Therefore `nu^*L=O_P1`, but this
does **not** imply `L=O_Z`.

Choose a nowhere-zero section `sigma` of `nu^*L`. Compare its two
values in the common fiber `L_node` and set

    lambda = sigma(p)/sigma(q) in k^*.

Scaling `sigma` does not change `lambda`; exchanging the branches
inverts it. This is the actual conductor gluing parameter. It obeys

    L^12=O_Z  iff  lambda^12=1,        and lambda != 1.             (3)

The last inequality is (2). It is not enough to verify that the
pullback of `L^12` to the normalization has degree zero: it always
does.

Here is a formula directly in ruling coefficients. Write
`x=[X0(T):X1(T)]`, `y=[Y0(T):Y1(T)]` with basepoint-free homogeneous
degree-two pairs. Choose indices `i,j` nonzero at the node. The
trivialization of `nu^*L` obtained from the two `O(2)` pullbacks gives

    lambda = Yj(p)*Xi(q)/(Xi(p)*Yj(q)).                            (4)

The common degree makes this independent of choices of homogeneous
lifts of `p,q`. Changing the ruling charts gives the same gluing
parameter, and branch exchange inverts it.

For example, choose `p=0,q=infinity`, move their common images to
infinity in both rulings, and write

    x(t)=(a*t^2+b*t+c)/t,
    y(t)=(d*t^2+e*t+h)/t,
    a*c*d*h != 0.

Then (4) is `lambda=a*h/(c*d)`. Distinct node tangent directions
give `a*h != c*d`. The exact spectral equation in this chart is

    (a*h)^12 - (c*d)^12 = 0,
    a*c*d*h*(a*h-c*d) != 0,                                       (5)

in addition to the conditions that the displayed normalization map
has the stated integral nodal `(2,2)` image. This chart is a way to
compute the invariant; it does not replace the actual original
coefficient coordinates in the ambient obstruction incidence.

## 6. Two-node reducible gluing

Let `Z=D1 union D2`, with each `Di` of class `(1,1)` and their two
transverse intersection points `z1,z2`. Choose trivializations
`sigma_i` of `L|Di`. At each node put

    g_j = sigma_1(z_j)/sigma_2(z_j) in k^*,
    lambda = g_1/g_2.

Rescaling either component trivialization changes both `g_j` by the
same factor, so `lambda` is intrinsic up to inversion. The two-node
normalization/conductor sequence gives `Pic^0(Z)=G_m`, with this
parameter. The exact condition is again (3), and `lambda !=1` follows
from (2). Discarding either node would erase the modulus.

The `g_j` are computed from the actual two ruling maps on the two
components exactly as in (4), using degree-one homogeneous pairs.
An equivalent normal form under separate ruling automorphisms is

    D1: y=x,                 D2: y=lambda*x,
    lambda in k^* minus {1}.

The intersections are at zero and infinity, and the eigenvalue ratio
of the relative ruling automorphism is `lambda` up to inversion.
The spectral equation is `lambda^12=1`. When the relative
automorphism becomes parabolic, its fixed points coalesce into the
tangent-component stratum of section 4; its length-two gluing must
be retained and is additive, not a free surviving root of unity.

## 7. A single finite torsion presentation retaining the smooth locus

For an entirely coefficient-based incidence, use the exact sequence

    0 -> O_S(10,-14) --f--> O_S(12,-12) -> L^12 -> 0.

Both ambient `H0` groups vanish, both ambient `H2` groups vanish,
and the two `H1` groups have dimension `143`. Thus

    H0(Z,L^12) = ker T_12(f),
    T_12(f): H1(O_S(10,-14)) -> H1(O_S(12,-12)).                   (6)

There is a reproducible sparse `143 x 143` matrix linear in the nine
coefficients of `f`. Dehomogenize as

    f(z,w)=sum_(a,b=0..2) c_(a,b) z^a w^b.

Use domain basis `z^i w^(-j)`, `0<=i<=10`, `1<=j<=13`, and target
basis `z^k w^(-ell)`, `0<=k<=12`, `1<=ell<=11`, where the negative
powers are the standard Cech bases for the negative-direction line
bundles. Then

    T_12[(k,ell),(i,j)] = c_(k-i,j-ell)

when both subscripts lie in `{0,1,2}`, and is zero otherwise. Terms
outside the Cech cohomology range are discarded, not interpreted as
additional equations.

For a reduced connected equal-slope root, a multidegree-zero line
bundle has a nonzero section if and only if it is trivial: a nonzero
section on a component is nowhere zero, and its values at the
intersection points force every adjacent component section to be
nonzero; connectedness then propagates the trivialization. Hence

    det T_12(f)=0  iff  L^12=O_Z                                 (7)

on the reduced equal-slope locus. This equation retains the smooth
genus-one locus with nonidentity 12-torsion, the nodal roots with
the actual modulus (3), and the two-node pairs with the two-node
modulus of section 6. It automatically has no cuspidal or tangent
points after restriction to these actual root strata.

There is also an appropriate scheme-theoretic reading. At a
geometric point satisfying (7), `h0(L^12)=1` and the matrix has
corank one. Locally reduce its invertible `142 x 142` block; the
remaining scalar is a unit times its determinant. On its zero
scheme the kernel is a line bundle and gives a relative section of
`L^12`; its fiber is nowhere zero on `Z`, so evaluation is an
isomorphism after localization. Conversely a relative
trivialization makes the scalar vanish. Thus the determinant
incidence has the same local scheme structure as relative
triviality on these retained root families, not just the same
closed points.

One must first impose reduced equal-slope roots. For unbalanced
reducible curves a section may be supported on a positive-degree
component, and `det T_12=0` alone need not mean triviality. The
promoted component theorem provides precisely the needed
restriction; it must not be dropped from the incidence.

## 8. What this reduction does and does not settle

The singular-root part of the structured incidence is now precise:
cuspidal and tangent-component roots are excluded by full Picard
torsion; integral nodal roots retain (3)-(5); two-node pairs retain
the ratio of the two conductor identifications; and smooth roots
retain nonidentity 12-torsion. The determinant (6)-(7) presents the
same condition in the original nine root coefficients. It can be
combined with the actual `k`-linear sextic-symbol image condition,
the universal first incidence, and all twenty-five second pairings.

No nonempty low-order point has been produced by this note, nor has
the combined incidence been proved empty. If it survives, the first
unresolved **global** lifting condition need not be the next abstract
Cartier obstruction. The universal first incidence determines a
canonical cubic root correction `G0` on the first base chart. The
degree-three jet of an actual global sextic must satisfy

    [F3-alpha*G0] mod (f) = 0.                                    (8)

The global-symbol computation in
`../computations/conditional_2_12_symbol_map_2026_10_20.py` presents
the allowed sextics with the prescribed symbol as
`F=F0(alpha*f)+lambda*q^3`, where `q` is the quadric containing `C0`.
Consequently (8) is a finite `k`-linear matching problem using those
actual sextic jets. In the computation's coordinates it is

    F3-alpha*G0 = f*(ell(z)*u+m(z)*v),
    deg ell, deg m <= 7.

One must not divide by `alpha`: its zeros are part of the problem.
The abstract root next has its third obstruction at exceptional
stage `E3` (normal degree five), followed by the remaining finite
tower through `E9`. It is a logically separate condition from
matching the jets of a global sextic. A global realization
additionally requires
actual `k`-coefficient polynomials of degrees `6,16`, a degree-12
standard-basis certificate with the FULL resulting initial pair
coprime, and the global gcd/Bezout support argument. Abstract graded
torsion or low-order embedded compatibility supplies none of those
certificates by itself.

The independent `incidence_audit` review reconstructed the relative
standard-basis lift at closed points, the same exceptional division
exponent on both original equations, the conductor parameters, and
the torsion determinant argument, and reported PASS. Its substantive
scope correction was to put the global cubic matching (8) before
the abstract third Cartier obstruction as the first unresolved
global lifting condition. This section records that correction.
Canonical promotion is not part of this contribution.
