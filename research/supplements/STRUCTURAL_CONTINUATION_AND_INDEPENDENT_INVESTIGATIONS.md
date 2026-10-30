# structural continuation and independent investigations

Complete mathematical dossier preserving the actual investigations, calculations, exact conditions, negative results, and unresolved boundaries. Administrative commentary is retained pending editorial consolidation, not treated as proof authority.

---

## 2026-10-19-independent-investigation-report

# Independent investigation: saturated normal cones, moving roots, and exceptional cycles

Date: 2026-10-19. Starting branch: `main`.
Research branch: `codex/normal-cone-rigidity-2026-10-19`.

**Status:** new research proposals with separate independent audits, not
canonical promotions. The unrestricted characteristic-zero STCI problem
for `C0=[s^4:s^3t:st^3:t^4]` remains open.

## A. Main findings

### A1. A global normal-flatness theorem for actual lci thickenings

Let `C` be a smooth connected projective curve in a smooth threefold,
`Y` an actual lci thickening with `Y_red=C`, `J=I_C O_Y`, and
`E=N_(C/X)^*`. Suppose:

1. The **full generic ordinary initial ideal** is a coprime binary
   complete intersection `(f_r,g_s)`, with `2<=r<s`.
2. The actual first relation
   `R=ker(Sym^r E -> J^r/J^(r+1))` is a line **subbundle**.

Then every ordinary normal layer `J^i/J^(i+1)` is locally free on `C`,
and every graded fiber is a binary complete intersection of degrees
`(r,s)`. No balanced-conormal assumption, smooth-root assumption, or
joint generation by two chosen displayed symbols is needed. The
characteristic-zero formulation suffices for this investigation.

The proof uses the saturated ordinary powers `P_i`, whose successive
layers `B_i` have perfect complementary multiplication pairings into
the actual socle line `S`. With `d=r+s-2`, generic Gorenstein symmetry
gives `Ann(P_i)=P_(d+1-i)`; exact MCM duality then gives
`B_(d-i)=Hom(B_i,S)`. Saturation of the first relation forces
`P_i=J^i` through `i=s`.

Write `h=deg E`, `a=deg R`. Duality fixes

    deg S=(s-1)h-(s-r)a/r.

The kernel `T` of the degree-s first-relation quotient onto `B_s` is a
line subbundle and has

    deg T=s h-s a/r.

The relative resultant of the first form and this second **quotient**
relation is a generically nonzero section of

    (det E)^(rs) tensor R^(-s) tensor T^(-r).

Its degree is zero. Projectivity forces it to be nowhere zero, hence
the relations are coprime in every fiber. Their abstract graded CI
maps to the saturated graded algebra. The top map is an isomorphism
between equal-degree lines, and perfect graded pairings make every
graded map an isomorphism. Degree-one generation finally gives
`P_i=J^i` for all `i`. This removes the possible later ordinary-layer
torsion rather than assuming it away.

Source: [general theorem and proof, Section 8](2026-10-19-saturated-first-relation-spectral-bridge.md).
The same note proves the balanced full-root spectral bridge and retains
the nonsplit second-generator extension.
Independent reconstruction: [filtered bridge audit](2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit.md).
Additional adversarial review: [normal-flatness audit](2026-10-19-normal-flatness-adversarial-audit.md).

A separate local proof uses the accepted sharp codimension-two
Artinian Gorenstein Hilbert-function bound. Length `rs`, Loewy degree
at most `r+s-2`, and exact transverse first order `r` force the entire
special Hilbert function to equal the CI envelope. A DVR argument then
makes every ordinary layer flat. This second proof removes projectivity
and also treats `r=s` under its explicit constant-exact-order hypothesis;
the saturated first kernel is a sufficient condition of the appropriate
rank. Its [source](2026-10-19-filtered-generic-ci-normal-flatness.md) and
[separate audit](2026-10-19-filtered-local-normal-flatness-independent-audit.md)
record the additional classical dependency. It supplies independent
support for A1 rather than a finite check of the resultant proof.

### A2. Moving nonreduced full roots are excluded in that actual class

Over characteristic zero, let `Z subset P1_base x P1_direction` be a
finite-flat Cartier root divisor of class `(epsilon,r)`, `epsilon>0`.
If `O_Z(0,s)=pi*O(n)` for any `s>0`, then `Z` is reduced. Moreover, if
`g=gcd(epsilon,r)`, its irreducible components have classes

    t_i(epsilon/g,r/g),  t_i positive integers,  sum t_i=g.

In particular, coprime `epsilon,r` force an integral root.

The auxiliary theorem is that

    Pic(P1 x P1) -> Pic(2D)

is injective for every effective divisor `D` with both bidegrees
positive. A trivialization on `2D` makes logarithmic transition
differentials vanish in `Omega_surface|D`; the vanishing
`H1(Omega_surface(-D))=0` then detects both ambient Chern-class
coordinates. A repeated component of a moving spectral root would
contain just such a doubled divisor and contradict injectivity.
Singular and reducible divisors are retained throughout.

Combining A1 with [STCI-R-0008](../results/spectral_root_picard_criterion.md)
and this Picard argument yields a direct exclusion of actual
`C0`-supported lci thickenings whose first full root is moving and
nonreduced, **provided the full generic CI and saturated-first-line
hypotheses hold**. This includes repeated irreducible multisections
and mixtures of components, beyond powers of one moving section.

For movement two, a spectral survivor must be an integral reduced
`(2,r)` divisor, possibly singular, or (for even `r`) a union of two
distinct smooth rational `(1,r/2)` divisors. Ramified nonreduced
**fibers** of a reduced total root remain allowed.

Source: [nonreduced-root proof](2026-10-19-spectral-nonreduced-root-obstruction.md).
Independent reconstruction: [spectral audit](2026-10-19-spectral-nonreduced-root-independent-audit.md).
A shorter general-base argument for moving pure powers is preserved
in [the pure-power note](2026-10-19-filtered-saturated-duality-moving-purepower-bridge.md).

### A3. Exact exceptional-cycle balance and new support restrictions

In the broader proper-intersection setting for `C0`, write

    [V(F,G)]=m[C0]+R_res,  delta=deg R_res=de-4m.

Let `p,q` be the exact generic normal orders of the displayed equations.
On the first blowup write the strict-surface intersection cycle as
`R_res~+Y_exc`, and put `lambda=E_exceptional . R_res~`. If
`[Y_exc]=A alpha+B beta` on `P1_base x P1_direction`, then

    B=m-pq,
    A=lambda+7(m+pq)-4(dq+ep).

If all horizontal common first-symbol root components have slope
`base degree / degree over C0 >= rho`, effectivity gives `A>=rho B`.
In an entirely-thick STCI, with `x=d/p`, `y=e/q`, this yields

    ((7-rho)/4)xy+7+rho >= 4(x+y).

The inherited STCI-specific restrictions give `x,y>=3`. Consequently:

- Some common horizontal root component must have slope `<7`.
- If the sole common horizontal root is a graph, its degree is at most
  six.
- If all common horizontal roots have slope at least two, then
  `min(x,y)<=16/5` is excluded, including the normalized pair `(4,4)`.
- For a sole degree-one graph root, `x=3` forces `y>=8`.

These conclusions retain arbitrary vertical exceptional multiplicity.
They concern common roots of the **displayed first symbols**, which
are different from the full initial-ideal root in A1--A2.

The exact balance also gives the residual correction

    7de+28pq+5 delta >=16(dq+ep).

If no residual component lies on the unique quadric, its coefficient
improves from five to one. These are necessary inequalities, not a
residual-existence theorem.

Source: [cycle balance, slope refinement, and examples](2026-10-19-exceptional-cycle-balance-and-vertical-counterexamples.md).
Independent reconstruction: [cycle audit, including slope addendum](2026-10-19-exceptional-cycle-and-vertical-family-independent-audit.md).

### A4. Counterexamples and actual higher-degree carriers

The local family

    f=t^N u^p+v^a,  g=f+u^b,  a,b>p>=2

has pure support `V(u,v)` and is finite free of rank `ab` over `k[t]`.
Its first strict-surface intersection has vertical coefficient
`N(b-p)`, unbounded while the generic multiplicity and displayed
orders are fixed. On the subsequence `N=aL`, even the full generic
filtered algebra is fixed up to isomorphism. Replacing `g` by `g-f`
removes the vertical component. The source also gives a homogeneous
projective pure-line example. Thus vertical exceptional multiplicity
is neither a residual curve downstairs nor an invariant of the ideal
independent of its chosen generators.

Two explicit one-parameter smooth-quadric normalization families were
also constructed. Their images are actual integral degree-eight
surfaces containing literal `C0`. Each has isolated extra points in
the full inverse support of `C0`, so no member admits a mate of any
positive degree. The simpler family's full inverse support is
computed exactly; at parameter `gamma=1` it is the diagonal plus
exactly five isolated points. These families do not exhaust the
degree-eight projection model.

Source: [actual degree-eight families](2026-10-19-quadric-antidiagonal-fourfold-line-proposal.md).
Independent reconstruction: [carrier audit](2026-10-19-quadric-antidiagonal-fourfold-line-independent-audit.md).

## B. Dependencies, authority, and precise frontier change

The investigation used the promoted records
[STCI-R-0001](../results/quartic_carrier_exclusion.md),
[STCI-R-0008](../results/spectral_root_picard_criterion.md),
[STCI-R-0009](../results/moving_purepower_boundary.md), and
[STCI-R-0003](../results/fixed_carrier_conductor_criterion.md)
within their stated scopes. The fixed normal bundle is the
characteristic-zero `N_C0=O(7)^2`. No quartic proof was rerun.

For the numerical `d/p,e/q>=3` input, the exact inherited proof is
the [entirely-thick independent audit](2026-10-06-session-thick-independent-audit.md).
The legacy [entirely-thick topic](../results/entirely_thick.md) is
navigation, not an ID-bearing promoted theorem. This metadata authority
gap is recorded explicitly; no stronger universal claim is inferred.
The STCI factor reduction and low-degree exclusion have promoted support
in R-0001 and its linked audit.

The genuinely new bridge is A1, proved in the source and independently
reviewed, rather than an inference from a prior summary. It closes
later special-point normal-layer degeneration within its exact
saturated-first/generic-CI class. A2 then excludes all moving
nonreduced full roots within that actual class. A3 supplies additional
support-sensitive restrictions without requiring that first relation
to be a saturated line. No canonical result, question, state, or
frontier record was edited or promoted.

An independent local Hilbert-function argument is preserved in
[the local normal-flatness proposal](2026-10-19-filtered-generic-ci-normal-flatness.md).
It has its own classical dependency and a separate
[independent audit](2026-10-19-filtered-local-normal-flatness-independent-audit.md).
It is also a reviewed but unpromoted proposal. The projective theorem
has the self-contained resultant/duality proof and does not depend on
this additional classical bound or on the local route's broader scope.

## C. Most promising connection

Gorenstein duality controls a finite-support defect that previously
separated generic formal algebra from the full spectral curve. The
second quotient relation has a generically nonzero resultant of degree
zero. This is the mechanism forcing uniformity; generic coprimality
alone would not suffice. It makes the full Picard obstruction directly
applicable to an actual intersection in a nontrivial infinite class.

The blowup work complements that bridge by retaining chosen-equation
and vertical-cycle information. Its counterexamples show why the
uniformity proof must use the full algebra and projectivity, rather
than interpreting vertical degeneration as a residual component.

## D. Remaining obstacles

1. **Nonsaturated first relation.** Determine the torsion and its
   duality constraints when the first actual kernel is not a
   subbundle. The exact early-layer identification used in A1 then
   fails. The local proposal preserves an explicit nonsaturated
   counterexample; saturation cannot simply be dropped.
2. **Non-CI generic tangent algebra.** An actual transverse Artin CI
   can have an ordinary initial ideal with three or more generators.
   Its generic graded algebra need not be Gorenstein. The complementary
   saturated-power duality in A1 then has no established symmetric
   index formula.
3. **Reduced roots and ambient lifting.** A1 provides graded/spectral
   uniformity; it does not supply arbitrary embedded Cartier lifts of
   a singular root in the actual blowup. Integral singular roots and
   distinct-component roots require actual ambient obstruction data.
4. **Exceptional support distribution.** The class `(A,B)` and its
   slope budget do not determine higher contact along each direction.
   A further global constraint on multiplicities is still missing.
5. **Full-support normalization families.** The explicit degree-eight
   exclusions have isolated inverse points. They do not compute phase
   images for projections that actually satisfy the required full
   singleton inverse support, or address all higher carriers.

No shared singular point of arbitrary defining surfaces is assumed.

## E. Recommended continuation and evidence checks

First study the torsion of the earliest nonsaturated relation and how
its length changes the degree-zero resultant calculation. A useful
target is an exact effective-defect formula replacing the zero degree
in A1; one must keep the torsion in every comparison map. In parallel,
investigate codimension-two non-CI generic initial ideals with the
smallest number of additional generators, using their actual
annihilator flags rather than assuming graded Gorenstein symmetry.

For the saturated generic-CI class, direct effort toward reduced
singular roots and the equal-slope rational-component pairs identified
in A2. Additional nonreduced spectral scans are unnecessary in that
class. The chosen-symbol slope theorem gives a separate way to select
surviving normalized-degree regions without conflating the two root
objects.

All principal results have full proof text and separate review evidence;
there is no uncompleted elimination computation underlying the reported
claims. Closing verification checked all 13 new notes and 70 local
Markdown links, with all targets present.
`python3 research/computations/validate_records.py` checked 10 canonical
records with zero errors. `git diff --cached --check` passed after a
whitespace-only correction to one audit. These are repository integrity
checks; mathematical validity rests on the proofs and independent
reconstructions, including a separate adversarial review of A1.

The package is committed on
[the research branch](https://github.com/markluxton1/STCI/tree/codex/normal-cone-rigidity-2026-10-19).
The exact closing commit is identified in the investigation message.
Standard external inputs, with direct primary links, are identified in
the respective source and audit notes.


---

## 2026-10-16-session-structural-continuation

# October 16 structural continuation and successor entry

The universal integral-curve STCI question and unrestricted characteristic-zero
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. This record supplements
[the current audited frontier](../AUDITED_STATE_2026-10-14.md) and
[the successor handoff](../SUCCESSOR_HANDOFF_2026-10-14.md). The October 13
all-branch reconstruction remains an accepted premise; no branch-source
or accepted mathematical verifier was replayed in this continuation.

The current externally observed checkpoint is
`bf124f8ab962ef0ed4085397034c50ee8d0d7162`, title
`2026-10-15 afternoon limit reached`. The primary agent did not create
that commit. This continuation has further working-tree changes.

## 1. The strongest structural generalization

The new [intrinsic finite-root-family theorem](2026-10-15-generalization-intrinsic-finite-root-family.md)
and [independent new-scope audit](2026-10-15-generalization-intrinsic-finite-root-family-independent-audit.md)
remove the rational-base and split-normal-bundle hypotheses from a fixed
bounded smooth-root family. If `A=Z^2_E`, `nu=E.Z`, and
`nu>max(A,0)`, all successive correction lines have negative degree
`A-m nu`. Relative cohomology gives obstruction bundles of rank
`g_Z-1-A+m nu`, compatibly with arbitrary parameter base change, including
nilpotent directions. The embedded-Cartier ideals are unique whenever
they exist, so their closed obstruction schemes remain in one fixed
finite-type space and eventually stabilize as schemes.

For the actual blowup of **any** fixed smooth space curve of degree e
and genus gamma, the actual exceptional ruled surface obeys

```
A=(4e+2gamma-2)r^2-2r nu,
A=2g_Z-2+4er-2nu.
```

Fixed `(r,nu)` fixes numerical class and Hilbert polynomial. One smooth
Cartier Hilbert open therefore contains all smooth connected roots of
that class. If `nu>4g_Z+5`, a hypothetical infinite lift also requires
a positive integer d satisfying

```
d<=max_(a>=1 integer)(2aer-nu a^2),
(d-1)(d-2)>=e r(r-1).
```

Incompatibility makes the stable scheme empty, and gives a finite
uniform empty stage N over the whole fixed family. Under a valid
actual-CI bridge, `s-r<=N`. The theorem does not compute N, bound all
numerical classes, or treat singular/nonreduced roots. Its new intrinsic
proof and audit state characteristic-zero scope.

This contains the preceding balanced-rational movement-two result:
for e>=4 and every r>=2, all smooth roots of class `(2,r)` have no
infinite formal lift. Movement-one roots of order r>=2 are also excluded
for e>=3; for r=1,e>=4, their all-orders lifts are exactly containing
quadric germs smooth along C. The broader inequalities, rather than
separate carrier degrees, are the continuing geometric mechanism.

## 2. Characteristic and actual-CI bridge

The [formal characteristic addendum](2026-10-15-generalization-smooth-root-characteristic-scope-addendum.md)
accepts the balanced-rational formal theorem and finite tower in every
algebraically closed characteristic, with its explicit normal-bundle
and smooth-root hypotheses.

The [inseparable-root actual-CI bridge](2026-10-15-generalization-inseparable-root-blowup-bridge.md)
now also has a [full independent new-scope PASS](2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit.md).
It uses the actual root prime over `k(C)` and an uncompleted standard
basis, retaining inseparable residue fields. The original strict-divisor
intersection is locally `(h,u^(s-r))`, without saturation or removal
of a vertical component. Its Cartier-root stages are precisely those
with `m<s-r`. Thus the same gap bound applies in every characteristic
within the literal saturated-line, joint-leading-generation, full
generic-initial-CI and smooth-full-root hypotheses. No assertion about
literal C0 splitting in bad characteristics is inserted.

## 3. Arithmetic reduction of all mate powers

The [effective rational phase theorem](2026-10-15-generalization-effective-rational-phase-bound.md)
and [arithmetic review](2026-10-15-generalization-effective-rational-phase-bound-independent-review.md)
are accepted. For an explicit rational constructible phase image,
Mann's theorem, finite cyclotomic calculations and Smith normal form
give a finite exact coset/boundary certificate. It decides torsion
existence, detects unbounded least mate degrees through a surviving
positive-dimensional coset, and bounds phase orders by `P(S)d^D` if
only isolated cosets survive. The three fixed projection models have
on-C thresholds 5,5,13, so the corresponding least-degree bounds are
that phase bound plus 4 or 12.

The whole fixed normalization families stay over Q, retaining all
branch choices. A stronger corollary starts from finite rational
section/module data for these three fixed models and constructs the
actual phase image by a terminating algebraic procedure; the written
review contains its scope addendum. A fresh
[October 16 raw-input scope audit](2026-10-16-generalization-raw-projection-decision-independent-audit.md)
now passes the final admissibility and generic-freeness formulation.
The precise finite rational input is one of the three fixed source
rings with H,c,Q, four polynomial parameter sections with their prescribed
C0 restrictions, and finite constructible parameter conditions. The
terminating algorithm decides whether any actual carrier in that input
family has any mate, and whether its least mate degrees are unbounded
or admit a computable uniform bound. It does not require an oracle for
unspecified class groups or arbitrary coefficient fields.
No actual phase image, Mann partition list, or family decision has been
computed. Neither practical complexity nor a numerical C0 bound follows
from the existence of the algorithm.

## 4. The dedicated quintic target

Accepted shared reductions now include the global remaining-mate
Delta1 unit, exact q6-to-j scalar binding, eleven-generator reduction,
automatic `(q5,q6)=1`, and the equivalent eight-equation logarithmic
ODE on the declared rational inverse-map chart. The reviewed eta
spectral accelerator retains one ideal rather than separate degree,
root or norm-factor cases.

The new [global monic h2 ODE model](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md)
is the next whole-h2 target. It uses the original parameters, a monic
quadratic H, four conormal remainders, two actual-conductor remainders,
eight ODE coefficients and three derived accelerators: seventeen equations
in nine variables, with only `delta*E*Delta1` inverted. Its purpose is
to retain the repeated-root and cover-determinant boundary that the
earlier rational inverse-map chart could not cover. The
[final global scope audit](2026-10-16-generalization-quintic-h2-global-monic-ODE-independent-audit.md)
now passes the whole-h2 cover and current exact artifact bindings. Its
[runnable input](../computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
is saved and passed a load-only check. One subsequent capped global QQ
saturation reached GB but produced no result, as recorded below. The one
next saturation target is `h2GlobalIdeal : h2GlobalDomainUnit^infinity`,
with all repeated-root and cover boundaries retained in the same model.

The quintic is not closed. The earlier h3, coprime, endpoint and stated
residual-partition exclusions remain accepted. Other quintic
normalizations and retained h1 singular/intrinsic/common-root scope
remain separate obligations. A whole-h2 unit-ideal certificate would
not by itself prove a whole-quintic theorem.

## 5. Computation and continuation state

- The [global quadratic-root second model](2026-10-15-generalization-quadratic-root-global-second-dual-compression.md)
  and [complete model audit](2026-10-15-generalization-quadratic-root-global-second-dual-compression-independent-audit.md)
  replace the full rank-sixteen second obstruction by twenty-five
  complete scalar pairings, without coefficient charts or thirty-nine
  new quartic unit variables. The homogeneous branch discriminant
  retains infinity. Its input is complete, not an emptiness result.
- Its one M2 launch failed in supervisor RSS monitoring. The child CPU
  limit was set; wall/RSS supervision did not complete. PID32960 was
  subsequently confirmed absent, its original exit code was not
  recovered, and no GB completion marker exists. Do not infer N<=5.
- Quintic ODE attempt07 and spectral attempt08 both reached the GB/
  domain-saturation stage and ended at their 45-second limits, with
  exit -15, their PIDs reaped, and no ideal result. They are not live.
- Global monic h2 input completion is preserved separately from failed
  assembly/printing interfaces. Its fresh load-only attempt05 exited
  zero with empty stderr, PID38681 reaped. This was no saturation run.
- The new [whole-h2 global QQ attempt06](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/execution-record.json)
  reached saturation and stopped at its polled 1536-MiB RSS threshold,
  after 58.564 seconds and 118.528 process CPU seconds. Actual exit -15,
  PID39519 reaped, private group absent. It supplied neither a completed
  ideal nor a unit certificate. The memory guard's own-child preflight
  and frozen source review passed before launch; no `/bin/ps` monitor
  was used. This is separate from the earlier failed inverse-chart
  attempt06 and from the quadratic-root supervisor failure.
- All twenty-two finite family-two exception-root closures and the
  accepted large quintic witnesses remain premises; none was replayed.

The [proof-record index](../validation/2026-10-15-structural-acceptance/index.json)
separates accepted scopes, pending scopes and terminal computations.
Hashes and link checks are document-integrity evidence, not proof.
The full research goal remains active.


---

## 2026-10-16-generalization-quintic-h2-global-QQ-prospect-terminal-record

# Terminal record: one whole-h2 global QQ saturation prospect

The one authorized global prospect ended without a mathematical result.
It loaded the accepted seventeen-equation, nine-variable input over
`QQ`, reached the single saturation by `delta*E*Delta1`, and was stopped
when the M2 process exceeded the sampled memory threshold. This is
bounded computation evidence; it does not prove that the incidence is
empty or nonempty. There is no unit-ideal output or certificate.

The authoritative data are the
[execution record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/execution-record.json),
[fresh preflight record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/preflight-record.json),
[last sampled metrics](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/live-metrics.json),
and [last stage](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/stage.txt).

## Actual execution and cleanup

| Field | Recorded value |
| --- | --- |
| M2 PID and private process group | `39519` |
| Supervising tool session | `82234`, subsequently closed |
| M2 start UTC | `2026-10-16T11:35:33.981234+00:00` |
| M2 terminal UTC | `2026-10-16T11:36:32.545921+00:00` |
| Wall time | `58.564014667` seconds |
| CPU time | `118.528412` seconds |
| Actual M2 exit | `-15` (SIGTERM) |
| Stop reason | `polled-memory-stop-threshold` |
| Peak resident bytes | `1611595776` |
| Peak physical-footprint bytes | `1597376144` |
| Memory stop threshold | `1610612736` bytes (1536 MiB) |
| Last stage | `before-global-QQ-saturation-by-delta-E-Delta1-only` |
| Cleanup | `SIGTERM-private-group`, then `private-group-absent` |
| Caught or cleanup exception | Both `null` |

The private process group was terminated and the M2 child reaped. The
owner subsequently resumed tool session `82234`; the supervisor returned
exit zero and the terminal text
`TERMINAL interrupted polled-memory-stop-threshold exit -15`.
The supervisor exit zero records successful handling of the bounded
interruption. It is not an M2 success code. There is no live execution
handle from this prospect and no restart was made.

The configured wall threshold was 120 seconds, with cleanup grace; the
OS CPU soft and hard limits were both 120 seconds. The memory guard
sampled `max(resident,physical-footprint)` for the M2 PID every 0.25
seconds. It is a polled stop threshold, not a hard aggregate or virtual
memory bound. A fresh own-child preflight passed before the M2 process
was launched, including inherited CPU-limit verification, memory
monitoring, and private-group termination/reaping.

## Exact source, input and output binding

The
[frozen M2 driver](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/source.m2)
has SHA256
`c6d6fceaeb16182a226373dfc19efe3d8816d0cc4797e7186f26bd038051735b`.
The
[frozen runner](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/runner.py)
has SHA256
`e47317ab64eeb5968aba839880955a54ba55396ae7358dcb0b5f8718a2f6be04`.
These are the independently reviewed hashes in the
[prelaunch source record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/prelaunch-source-review.json).

The loader hash was checked against the accepted load-only execution
record. The exact seventeen-generator data have SHA256
`c29dff74c9b120df41b7c59852d81d88d9d7004fa6e8586cda961eafd82e5008`;
the exact domain polynomial has SHA256
`4bd9af1e22bcf421017a2b0213cdc74e5dfbd9451860c1c644c24104977e778b`.
The loader itself has SHA256
`f5db87f6ea8dbd7d32411621bec3c68221ceaa9dc48a54e5dd3e82312535d1b4`.
All are bound in the execution record. No accepted coefficient
assembly, theorem verifier, or prior prospect was rerun.

The sole new algebra operation was

```macaulay2
saturate(h2GlobalIdeal, ideal h2GlobalDomainUnit)
```

over `QQ`. Its domain is exactly `delta*E*Delta1`. There is no inverse of
the rational-cover determinant, quadratic discriminant, a q coefficient,
or `Jbar`; repeated and cover-boundary points remain in this model.
The precise geometric scope is the accepted
[global monic ODE incidence](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md)
and its
[independent audit](2026-10-16-generalization-quintic-h2-global-monic-ODE-independent-audit.md).

The 193-byte
[stdout](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/stdout.txt)
contains only the loader's confirmation of the exact saved input. Its
line `No GB/saturation executed` describes the load-only library stage;
the driver's later stage marker records entry into the new saturation.
The
[stderr](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/stderr.txt)
is empty. Neither `saturated-ideal.txt` nor `is-unit.txt` exists, and no
`saturation-complete` marker was reached.

The generic earlier bounded driver was not used for this prospect. Its
exact checkpoint bytes are retained as
[generic-runner-at-checkpoint.py](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-06-global-QQ-saturation/generic-runner-at-checkpoint.py),
recovered from checkpoint
`bf124f8ab962ef0ed4085397034c50ee8d0d7162`, with SHA256
`55d370623116a153645974d755e3e0805a3eb054f087734d5206ddb7128b7018`.
Thus this new runner does not change the source binding of earlier
execution records.

The global h2 incidence remains an accepted necessary target whose
emptiness has not been decided. No additional CAS run is part of this
record.


---

## 2026-10-16-generalization-quintic-h2-global-monic-ODE-independent-audit

# Independent audit: one global monic h2 ODE incidence

Date: 2026-10-16.

Status: **PASS for the new global monic cover, original-parameter
coefficient assembly, and transfer of the accepted ODE/spectral
algebra to the domain delta*E*Delta1 nonzero.** The seventeen
equations in nine variables retain the finite inverse-map boundary.
This is a necessary incidence for every remaining actual h2 mate
candidate, not an emptiness or mate-existence theorem.

The reviewed proposal is
[the global monic incidence note](2026-10-15-generalization-quintic-h2-global-monic-ODE-incidence.md).
Accepted conormal forms, the actual octic, the global h2 conductor
factor, previous mate closures, the Delta1 open, and ODE/spectral
proofs are premises. No accepted proof or verifier was replayed.
This audit uses written coefficient calculations and read-only
source/artifact/hash inspection. No CAS was run during completion
of this audit, and no model assembly or elimination was repeated.

## 1. Monic coverage and exact homogeneous gcd degree

For any remaining actual h2 mate candidate, a common factor at source
infinity would force G=j=0 by the accepted leading-coefficient
equations. The accepted mate closure excludes that lane. Thus the
complete degree-two homogeneous gcd has nonzero t^2 coefficient,
and its unique monic representative is

    H(x)=x^2+v*x+w,       x=r/delta=t/s.

This monic chart is therefore global for the remaining h2 mate
candidates. It imposes no distinct-root hypothesis. It also does
not normalize delta to one.

Write the literal normalized cubics as

    P=G*x^3+P2*x^2+P1*x-2a,
    Jc=(G+2j)*x^3+J2*x^2+J1*x-a-B,

where

    P2=6B+delta^2-3delta,       P1=3a-3B+2delta,
    J2=6B+3G+5delta^2-3delta,   J1=3a+3B+delta-delta^2.

Set A=G, Bc=P2-vG, C=G+2j, Dc=J2-v(G+2j). The leading two
coefficients of (Ax+Bc)H and (Cx+Dc)H match the cubics identically.
Their remaining coefficients match precisely when

    -2a-w*Bc=0,       P1-v*Bc-w*A=0,
    -a-B-w*Dc=0,      J1-v*Dc-w*C=0.                  (1)

These are exactly the four saved cover equations, with no coefficient
system inverted. Direct expansion gives

    E=A*Dc-Bc*C
     =G*(3G+4delta^2)-2j*(6B+delta^2-3delta).          (2)

The terms involving v cancel. The unit E is the determinant of the
two homogeneous linear cofactors A*t+Bc*s and C*t+Dc*s. At field
points they are independent exactly when they are coprime, so (1)
and E nonzero give complete homogeneous gcd degree two. This
includes affine degree drops of either cubic. A zero cubic or a
proportional cofactor pair instead has E=0 and is correctly outside
the exact-h2 domain.

## 2. Fixed-degree octic reversal and monic division

For the accepted actual Fdet(p,1)=sum_(i=0)^8 f_i*p^i, reciprocal
source coordinates give Fsrc(1,x)=sum f_i*x^(8-i). Put q7=q8=0
and define downward

    q_i=f_(6-i)-v*q_(i+1)-w*q_(i+2),    i=6,...,0.

For the coefficient of x^(i+2) in H*Q, this is exactly
q_i+v*q_(i+1)+w*q_(i+2)=f_(6-i). Therefore all coefficients
of degree at least two match, and the remaining two coefficients
are exactly

    r0=f8-w*q0,
    r1=f7-v*q0-w*q1,
    Fsrc=H*Q+r1*x+r0.                                (3)

The two explicit equations r0=r1=0 are retained. The accepted
geometric factor theorem supplies them for every actual h2
projection; this assembly does not promote that theorem to an
unproved divisibility assertion over an arbitrary nonreduced
conormal-cover base. After the equations are imposed, (3) is an
exact ring identity on the incidence.

Monic division introduces no parameter denominator. Fixed degree
eight reversal and degree six quotient retain all coefficient drops
and the source point at infinity. In particular q6=f0 and
q5=f1-v*q6 have the intended A4 interpretation.

## 3. The new global domain does not invert Delta or K

The domain is exactly

    delta*E*Delta1 nonzero,
    Delta1=G(G+3delta^2)(G+delta^2+2B)
      +j[(delta^2-5B)G-3B(delta^2+3B)]-B*j^2.         (4)

Delta1 is necessary for all remaining mate candidates by the accepted
closures and A4 support argument. Delta=v^2-4w and
K=v^2+6vw+6w^2+2w are not factors of the declared unit product.
Thus the repeated finite-root boundary and the failed rational
inverse-map boundary remain represented by the original equations.
An accepted inconsistency on part of that boundary may be used as
a theorem, but no such locus is silently cancelled from this model.

For the unscaled actual quotient, the accepted A4 coefficients give

    q6=-3j*Delta1,
    q5=-2(G+3delta^2)*Delta1 modulo j.                (5)

There is no captured inverse-map scalar here. The accepted automatic
open proof now applies with kappa=1: the explicit Delta1-square
membership, or its equivalent quotient-ring argument, gives
(q5,q6)=1 after (4). This is an exact ideal equality and includes
nonreduced bases. It needs neither Delta nor K to be a unit.

The previous ODE and spectral proofs use monic H, (5), the Delta1
unit, coefficient unimodularity and field scalars 2,3. They therefore
apply unchanged to this original-parameter ring before any rational
inverse of the four cover equations. Their earlier actual use on a
smaller inverse-map chart does not limit this algebraic transfer.

## 4. The seventeen-equation system and its precise meaning

Using eta=dv-2u, the eight ODE coefficients are exactly

    2w(i+1)q_(i+1)+[(2i-d)v+eta]q_i
                         +2(i-1-d)q_(i-1),
    i=0,...,7.                                        (6)

These are twice the coefficients of H*q'-(dx+u)q. The change from
u to eta is invertible. The accepted globally unique ODE-witness
argument applies by (5), so (6) is the same shared rank/support
incidence on this domain, including its j=0 allowance.

There are four equations (1), two equations (3) and eight equations
(6), making fourteen. The three accepted derived equations

    (d-5)(d-6),       j(d-6),
    (d-5)P6(eta)+(6-d)P5(eta)

bring the saved presentation to seventeen equations in the nine
variables delta,a,B,G,j,v,w,d,eta. They belong to the same localized
ODE ideal, so appending them changes no scheme on (4). The temporary
variables p and x used in assembly are not additional model variables.

On actual admissible h2 projections, this incidence expresses the
accepted restricted-conductor support obligation. Every remaining
actual h2 mate candidate lies in it. The model does not impose center
avoidance or all original fiber conditions, and it does not establish
full inverse support or nonlinear conductor descent. An algebraic
survivor is therefore not automatically a projection or a mate.

## 5. Source, failure lineage and completed-output bindings

I read the current and frozen
[assembly source](../computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2),
the attempt-02 record and streams, the
[completion source](../computations/generalization_quintic_h2_global_monic_ode_completion_2026_10_15.py),
and the
[attempt-04 completion record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-04-completion/execution-record.json).
The assembly source uses the literal accepted octic, the reversed
coefficients and recurrence above, the four cover equations, (2),
the eight ODE equations, the three accelerators and precisely (4).
It writes all groups and seven q_i, asserts (2) and (3), then writes
the degree list before the final informational print.

The attempt-02 process exits one: its error is at that final
equation-count print, after stdout records the quotient/remainder
and cofactor assertions passing and after all data files were
written. This remains a failed process and is not relabelled a
fully passing CAS run. Its complete outputs are the bound inputs
to the separate Python completion; the earlier protected-name and
path/shape failures remain preserved as separate attempts.

The completion strips only boundary whitespace when reading the
expanded matrix entries, checks the exact four-group concatenation
4+2+8+3=17, checks a seven-entry Q vector, and copies the saved
model artifacts. It does not reread the primitive octic, reconstruct
the model, or run any CAS. Its record reports exit zero and empty
stderr.

On October 16 I independently checked, read-only: both current and
frozen assembly source hashes; the current completion-source hash;
the assembly's primitive-input hash; all seventeen completion-input
hashes; byte equality of all four copied model artifacts; exact
group/whole-vector equality; and all seven individual q_i files
against the completed Q vector. Every check passed. The completion
stderr is empty. This verifies current artifact bindings without
rerunning the mathematical assembly.

The new currently runnable
[load-only input](../computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
reads the completed seventeen-equation row and domain polynomial
over QQ in the stated nine-variable order. It asserts the ring,
matrix shape and nonzero domain polynomial, and retains the objects
h2GlobalRing, h2GlobalEquations, h2GlobalIdeal and
h2GlobalDomainUnit. It constructs no coefficient map and calls no
Groebner basis or saturation operation. The domain polynomial is
loaded as data for a future localization; the load-only script does
not itself localize or prove the domain nonempty.

I also read the
[attempt-05 load-only record](../validation/2026-10-15-quintic-h2-global-monic-ode/attempt-05-load-only/execution-record.json),
its input-binding metadata and streams. The record has exit zero
and empty stderr. A read-only check confirmed the current and frozen
input-source hashes, both current completed-data hashes, and both
output-stream hashes against that record. This successful load is
distinct from attempt-02's failed final print and attempt-04's
successful non-CAS completion. No CAS was invoked by this audit.

The one global future target is therefore the saved seventeen-equation
incidence localized at (4). No Gröbner basis, saturation, resultant
or emptiness computation for this global model is certified here.
A result restricted to Delta*K nonzero cannot close this larger
incidence. The unrestricted quintic and STCI questions remain outside
the conclusion of this audit.
