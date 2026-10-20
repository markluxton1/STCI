# Space Curves I–VI: selective research intake

Date: 2026-10-19. Target base: `84dacd99c54915b1bbb224bb01565f01716445de`.
Branch: `codex/space-curves-intake-2026-10-19`.

This is an evaluated intake of historical evidence and proposed additions. **No
claim is promoted to a canonical STCI result by this intake.** Source files are
copied verbatim, including their original status labels, historical priorities,
and limitations. Those labels do not override the [current authority policy](../../AUTHORITY.md).
The [manifest](manifest.json) identifies every copied file and its SHA-256.

## Scope and retrieval

The principal current question concerns the fixed characteristic-zero curve
`C0=[s^4:s^3t:st^3:t^4]`. The review also includes results for general integral
curves, smooth curves on quadrics, and rational quintics. It starts with
`C ⊂ V(F,G)_red`; equality requires accounting for the entire global degree
budget and possible residual components. Vertical exceptional curves over closed
points are not automatically extra components of the intersection downstairs.

The comparison used the current research index, authority policy, the eleven-result
promoted index, and relevant result, evidence and topic records. All six source artifact
inventories were screened; focused proof/audit reading was directed to potentially
useful differences. This is not a fresh mathematical audit of every artifact or a
new literature-status search. The [source inventory](source-artifact-inventory.json)
records titles and hashes of 98 artifact files, including the few duplicated
worker records in VI, rather than implying 98 distinct theorems.

| Source project | Local directory under `/Users/markluxton/Projects/` | Decision |
| --- | --- | --- |
| Space Curves | `space_curves` | Import rational-quintic proofs, recorded reviews, lattice script, and corrected coordinate benchmark. |
| Space Curves II | `space-curvers` | No files imported: baseline/codepth, twisted cubic and bounded C0 ideal computations are already covered here. |
| Space Curves III | `space-curves-on-high` | Import complementary normalization/conductor examples and their symbolic companion. |
| Space Curves IV | `space-curves-terra-xhigh` | Import the explicit fivefold conormal collision and its first-blowup computation. |
| Space Curves V | `amrl` | No files imported: the `(4,7)` contact exclusions and modular probes concern quartic mate cases already closed here. Retain their process lessons in this review. |
| Space Curves VI | `artifact-mediated-research-lab-v0.4-corrected` | Import the fixed-degree jet criterion/audit, global-coefficient controls, general contact-depth argument and relevant context. |

## 1. Highest priority: fixed-degree finite normal-jet criterion

**Exact imported claim.** Let `k` be algebraically closed, `C ⊂ P3` integral
of degree `d`, and `F,G ∈ I_C` nonzero homogeneous forms of positive degrees
`a,b`. If `d` does not divide `ab`, they cannot define `C` set-theoretically.
Otherwise set `M=ab/d`, `R=O_(P3,eta_C)`, `m=I_C R`, and `J=(F,G)R`. Then

\[
V_+(F,G)_{\mathrm{red}}=C
\quad\Longleftrightarrow\quad
\operatorname{length}_R R/(J+\mathfrak m^{M+1})=M.
\]

The source proves this in arbitrary characteristic. It also gives a weighted
test for a reduced pure union `C=union C_i`, of component degrees `d_i`: with
`B_i=floor(ab/d_i)` and truncated generic lengths `t_i` at exponent `B_i+1`,
the criterion is `sum d_i*t_i=ab`. Equal component multiplicities are not assumed.

**Why import it.** This provides a sufficient finite state for a supplied global
pair, even when both equations have high normal order and their leading forms
share factors. It connects local calculations to residual-component exclusion
through the global degree budget. It complements the restricted formal-root and
normal-flatness results STCI-R-0005 through STCI-R-0011; it does not depend on
their saturated-relation, smooth-root or generic binary-CI hypotheses.

The proof uses a Nakayama length lemma, removal of a hypothetical common factor,
and complete-intersection degree/purity. The `M+1` cutoff is sharp without an
extra proper-intersection hypothesis. In chosen normal coordinates, the test is
the rank of the **full ideal multiplication map** in
`k(C)[u,v]/(u,v)^(M+1)`, not the span of two jet coefficient vectors.

**Evidence and review.** [Source proof VI-011](space-curves-vi/state/artifacts/integrated/ARTIFACT-20260906-011-finite-normal-jet-certificate.md),
[recorded worker audit](space-curves-vi/state/artifacts/provisional/WORKER-20260906-finite-jet-audit.md),
and [Macaulay2 companion](space-curves-vi/scripts/finite_normal_jet_certificate.m2).
The donor describes a proof and an independent audit. The September records are
untracked working-tree files, and its event stream does not contain a September
integration event. Here the status is **source proof and audit imported;
canonical promotion pending review**. No new independent proof audit is claimed.

**Limits.** This is an exact fixed-degree reduction, not a computed witness locus
for C0, a practical general solver, or a uniform bound on possible witness degrees.
It does not decide the unrestricted STCI question.

### Global coefficients and characteristic controls

[VI-012](space-curves-vi/state/artifacts/integrated/ARTIFACT-20260906-012-global-coefficients-and-frobenius.md)
supplies a useful counterexample to relaxing global unknown coefficients from
`k` to `k(C)`. For `C_n=(s^(n+1):s^n t:s t^n:t^(n+1))`, `n>=2`, take
`Q=xw-yz`, `S_n=yw^(n-1)-z^n`, and the degree-`n+1` pencil
`<y S_n,w S_n>`. A function-field combination has normal ideal `(v,u^2)`
of length two, matching the nominal degree budget. Every nonzero **constant**
combination in that pencil instead has generic length one. The relaxed solution
does not come from a global member of that degree.

The same note analyzes the particular binomial pair
`(S_n, x^n w-y^(n+1))`: its support is `C_n` exactly when the characteristic
is `p>0` and `n` is a power of `p`. In characteristic zero its generic length
is one rather than `n`, with residual curves accounting for the remaining
degree. This is an assertion about this pair, not nonexistence of other pairs.
The companion includes a twisted-cubic positive control with a mixed term.

These are formulation controls, with the coefficient example covered by the
imported audit. VI-012 mentions an “Artifact 013” that is absent from the donor
artifact inventory; no such record has been manufactured or used. Its direct
calculation and the VI-011 criterion are the supplied evidence.

## 2. General contact depth from a surface-effective threshold

**Exact proposed use.** Work conservatively in characteristic zero with a smooth
integral curve `C` of degree `d` and a hypothetical homogeneous defining pair
of degrees `a,b`, generic normal orders `p,q`, and generic intersection length
`m=ab/d`. At the generic normal plane, let `h` be the greatest depth of a common
infinitely-near point, the origin having depth zero. The imported argument gives

\[
m\le(h+1)pq,\qquad
h\ge\left\lceil\frac{ab}{dpq}\right\rceil-1.
\]

If a smooth containing surface `S` admits no mate for `C` and has effective
threshold `tau=inf{a/p : aH-pC is effective}`, component exclusion forces
both slopes `a/p,b/q>=tau`. Thus `h>=ceil(tau^2/d)-1`. For a smooth curve
of bidegree `(u,v)` on a smooth quadric, with `u,v>0` and `u!=v`, use
`tau=max(u,v)` and `d=u+v`. In particular, every hypothetical pair for
`C_(1,n)` has `h>=n-1`. Powering either equation preserves the normalized
ratio `m/(pq)` and the underlying contact depth.

**Why import it.** The general family formulation is useful for the entirely-thick
and valuation programs. The current topic record already retains `a>=3p,b>=3q`
for C0; this adds an explicit interpretation as forced generic contact depth
across an unbounded family of curve degrees. It is a necessary condition, with
no contradiction from depth alone: `(y,y+x^N)` attains arbitrarily large depth
locally. It is not an upper bound or an all-degree non-STCI theorem.

**Evidence and review.** [VI-003, sections 1–2](space-curves-vi/state/artifacts/integrated/ARTIFACT-20260823-003-surface-threshold-second-resultant.md),
[VI-005](space-curves-vi/state/artifacts/integrated/ARTIFACT-20260823-005-contact-depth-and-quadric-families.md),
and the [Jaffe/contact-depth scope audit](space-curves-vi/state/artifacts/integrated/WORKER-20260823-jaffe-contact-depth-audit.md).
The latter distinguishes closed-point surface type from horizontal generic
contact; it is a source/scope audit, not a complete independent promotion audit
of every claim in VI-003 or VI-005. **Proposal with source argument; no canonical
promotion here.** The second-resultant assertions later in VI-003 are context,
not separately adopted by this intake.

[VI-010](space-curves-vi/state/artifacts/integrated/ARTIFACT-20260823-010-horizontal-recurrence-boundary.md)
retains the counterexample `y^p+x^(p+r)`: the same leading tangent form can
produce different next multiplicities. Its historical assertion that a finite
cutoff was unavailable is qualified at fixed degrees by VI-011. No uniform
all-degree cutoff follows. Generic contact depth and vertical exceptional type
remain different invariants.

## 3. Rational-quintic benchmark on cubic surfaces

**Smooth case.** Over an algebraically closed characteristic-zero field, a smooth
irreducible rational curve `C` of degree five on a smooth cubic `X` has class
`2L-E1` in a suitable six-line blow-down marking. Exactly five lines on `X`
are disjoint from `C`. They are complete curves in `X\C`, so that complement
is not affine. The theorem applies on every eligible smooth containing cubic;
it does not require a unique containing surface or a unique embedded quintic.

**One-node case.** If `X` is a normal integral cubic with exactly one `A1`
singularity and `C` is smooth, irreducible, rational, degree five, and avoids
the node, the imported argument likewise finds a complete degree-one curve
disjoint from `C`. The proof uses the weak-del-Pezzo resolution and a bounded
E6 lattice calculation: 120 eligible numerical classes, each orthogonal to
three of the 15 specified line classes. It is not a theorem for worse
singularities, curves through the node, or all containing surfaces.

**Why import it.** These are substantive auxiliary results not found in the
current C0-focused records. They broaden the general curve/affine-complement
program without changing the fixed-quartic frontier. Non-affineness on the
specified carriers does not establish unrestricted non-STCI for the quintic.

**Evidence and review.** [I-014](space-curves-i/research-state/artifacts/ARTIFACT-20260821-014.yaml),
[smooth independent reconstruction I-015](space-curves-i/research-state/artifacts/ARTIFACT-20260821-015.yaml),
[review event 019](space-curves-i/research-state/runs/EVENT-20260821-019.yaml),
[I-019](space-curves-i/research-state/artifacts/ARTIFACT-20260821-019.yaml),
[nodal reconstruction I-020](space-curves-i/research-state/artifacts/ARTIFACT-20260821-020.yaml),
[review event 025](space-curves-i/research-state/runs/EVENT-20260821-025.yaml),
the [lattice script](space-curves-i/research-state/scripts/nodal_cubic_quintic_lattice.py),
and [resolution literature record](space-curves-i/research-state/literature/LIT-20260821-043.yaml).

The smooth reconstruction names a distinct original agent. I-014 retains a
stale uncertainty about lacking review; I-015 and event 019 explicitly supply
that review. The nodal proof and review both name `/root`; its independence is
less clearly evidenced despite the donor's `independently_checked` label.
**Imported source-reviewed claims; target promotion pending**, with an explicit
independence gap for the nodal case. The lattice script has not been rerun here.
The optional applications to three explicit nodal witnesses require I-018,
which is not imported; only the general stated-hypothesis theorem is proposed.

### Corrected coordinate benchmark

[I-012](space-curves-i/research-state/artifacts/ARTIFACT-20260821-012.yaml),
[I-013](space-curves-i/research-state/artifacts/ARTIFACT-20260821-013.yaml),
[I-023](space-curves-i/research-state/artifacts/ARTIFACT-20260821-023.yaml),
and the two [coordinate](space-curves-i/research-state/scripts/vahlen_quintic_exact.py)
and [incidence](space-curves-i/research-state/scripts/vahlen_base_locus_discriminant.py)
scripts preserve a rational quintic model, low-degree kernels and a corrected
forced base line. In its coordinates the line is
`V(3U2-5U0,3U3-5U0-5U1)`. Use I-023's correction; do not revive the earlier
incorrect display. The on-line resultant and on-curve singularity incidence
are partial discriminant information, not a full singular-cubic classification.
The model is not identified with a unique projective-equivalence class called
Vahlen's quintic. These are **archived computational inputs**, with no fresh
replay or promotion here.

## 4. Complementary normalization/conductor examples

[III-012](space-curves-iii/research-state/artifacts/ARTIFACT-20260821-012.json)
and [III-013](space-curves-iii/research-state/artifacts/ARTIFACT-20260821-013.json),
with their [worked note](space-curves-iii/research-state/experiments/2026-08-21-explicit-examples.md)
and [symbolic script](space-curves-iii/research-state/experiments/explicit_examples.py),
give two characteristic-zero C0 examples:

- On the cuspidal cubic `y^3-x^2z=0`, the required divisor proportionality
  holds after normalization, but a nonzero additive polar part `-3z^(-2)`
  in the nonreduced-conductor quotient obstructs descent of every positive power.
- On the ruled cubic `xz^2-y^2w=0`, local pinch-point torsion is compatible
  with a mate, but the normalization classes `H=(2,1)` and `Ctilde=(2,0)`
  are not positively proportional.

**Use and status.** These explain distinct stages of the
[fixed-carrier criterion STCI-R-0003](../../results/fixed_carrier_conductor_criterion.md).
The exclusions do not advance the current cubic/quartic frontier. The source's
`independently_checked` labels come from `codex-root` acting multiple roles;
the symbolic script does not independently establish the class-group or conductor
identifications. **Historical examples, target review pending**, retaining their
Hartshorne–Polini source dependencies. No separate theorem promotion is proposed.

## 5. A concrete repeated-conormal-root failure

[IV-031](space-curves-iv/research-state/artifacts/ARTIFACT-20260822-031.yaml),
[IV-032](space-curves-iv/research-state/artifacts/ARTIFACT-20260822-032.yaml),
and the [collision script](space-curves-iv/experiments/c4_root_collision.py)
with its [conormal helper](space-curves-iv/experiments/c4_conormal.py) give an
explicit quartic through C0 whose conormal divisor has a fivefold root.
At that root the first transform has a nonzero normal derivative (coefficient
`2`), so the local contributions are `p1=5,p2=0`. The source interprets the
characteristic-zero surface–curve pair as `A_(9,5)` and total type as `(8)`.

**Use and status.** This is a concrete guard against equating repeated conormal
roots or a large ADE label with persistence after blowup. The exact polynomial
checks are separate from the formal Morse/type interpretation. The source does
not prove global irreducibility or normality of this quartic. Its historical
`(4,5)` search priorities are superseded by
[STCI-R-0001](../../results/quartic_carrier_exclusion.md). **Computational example
with interpretation requiring review**, not a new open quartic mate case.
The surrounding determinant-locus claims and the old `p2>=7` branch budget are
not imported as usable results; those require additional source dependencies.

## Decisions for II and V

II's exact C0 Hilbert dimensions through degree ten and four ideal generators
duplicate current records and scripts. Its finite generator-span check is not
a proof in all degrees by itself. Its broad STCI conjecture is not a theorem.

V's formal contact matrix and its `(4,7)` nonempty-open-family exclusion are
historically useful, but their mathematical exclusion is subsumed by
STCI-R-0001. Its finite-field scans over `F5,F7,F11` do not establish emptiness
over algebraic closures or characteristic zero. The record of terminated
symbolic-power/primary-component computations supplies no mathematical output.
The method lesson is retained: use structured contact modules and exact rank
conditions before repeating an expensive elimination. No renewed computation
of these closed quartic cases is recommended.

## Provenance and remaining review

Four donor directories have no local Git metadata. I and VI have Git roots,
but **every selected file from those two projects is untracked** at the recorded
donor HEAD. The branch/HEAD fields in the manifest identify the surrounding checkout,
not a commit containing this mathematics. Exact copied bytes, original paths,
per-file status and SHA-256 are therefore the provenance anchor. Donor projects
were not modified. Source artifact IDs are namespaced by project directory;
identically numbered artifacts from different projects must not be conflated.

Historical IDs, literature links and source run commands inside copied files
retain their original meaning. This is a selective packet, not the whole donor
dependency graph. The explicit gaps above are retained rather than filled with
invented records. Donor literature assertions are dated source evidence, not a
fresh literature search or a novelty assessment.

Recommended next promotion candidate: VI-011, together with its coefficient-field
qualifications and global-coefficient control. Next structural candidate: the
component-exclusion/contact-depth claim from VI-003/005. Quintic claims belong
to a separate benchmark topic, and the two example packets can remain evidence.
Any promotion must follow the [contribution checklist](../../CONTRIBUTING_AGENT.md)
and provide a reviewed canonical record with explicit hypotheses and evidence.

The unrestricted characteristic-zero C0 problem, higher carriers, arbitrary
entirely-thick presentations, and the universal curve problem remain open here.
See [validation and replay instructions](VALIDATION.md) for exactly what was checked.
