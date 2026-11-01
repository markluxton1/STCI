# Quintic–octic closeout and its interfaces with the broader problem

Date: 2026-10-31. Status: **independently reviewed provisional synthesis**.
Fixed curve \(C=[s^4:s^3t:st^3:t^4]\) over an algebraically closed field
of characteristic zero. This closes the normal-defect/carrier-singularity
investigation and compares its result with selected committed research.
It does not begin a neighboring-degree investigation, promote a theorem,
or claim that the unrestricted STCI question is resolved.

## 1. What this lane has established

The [fixed-singularity note](2026-10-31-quintic-octic-fixed-singularities.md)
and [review](2026-10-31-quintic-octic-fixed-singularities-audit.md) identify
the geometric location of the required ordinary-layer torsion in an actual
hypothetical proper pair \(Y=V(F_5,G_8)\), \(Y_{\rm red}=C\).
The allowed first quotients \(L=\mathcal O(-q)\), q=5,6,7, and torsion
totals 35,80,125 remain necessary data, not realizations.

The ordinary torsion is supported exactly at the common first-symbol zero
divisor B, the fixed simultaneous singularity locus of the two carriers.
Replacing G by \(G+FH_3\) preserves the ideal and every ordinary or
saturated layer. It varies the containing octic; it cannot remove residual
support from a fixed intersection. A general octic has at least twelve
moving A9 points outside B. Ellia's primitive singularity argument cannot
be applied across B: there is no locally smooth defining member there.

The [ADE continuation](2026-10-31-quintic-octic-ade-exclusion.md), with its
[independent review](2026-10-31-quintic-octic-ade-exclusion-audit.md), proves
that the quintic cannot be globally ADE, even with repeated first-symbol
zeros. The proof uses information beyond a first-order coefficient count:

1. The actual divisor \(10C\sim8H\) yields a nontrivial order-two Weil
   class \(5C-4H\), hence a connected quasi-étale double cover of the quintic.
2. The globally ADE hypothesis controls the resolved cover's invariants.
   Its canonical map supplies a stronger bound than Noether alone, leaving
   four q=7 configurations after the full ADE rank calculation.
3. Their actual symbolic triples force saturated quadratic defect degrees
   1,0,2,1. Degrees zero and one fail the constant-direction obstruction.
   In the degree-two case the singularities require two distinct points,
   whereas the embedded cocycle permits only a double endpoint.

The important reusable feature is the passage from an actual divisor to
a global cover, followed by an obstruction retaining the location of
the embedded defect. A large torsion total alone gives neither step.
The actual homogeneous non-ADE control in the first note has generic
multiplicity five and residual degree twenty; it demonstrates flexibility
of containing equations, not a multiplicity-ten supported construction.
This lane has reached its stopping condition: a reviewed new carrier-class
restriction, a precise failure of the primitive comparison, and an actual
residual-support control.

## 2. Combined carrier boundary

The separate reviewed provisional
[Gorenstein-normalization theorem](2026-10-31-quintic-gorenstein-normalization-exclusion.md)
excludes every mate degree for an integral **nonnormal** quintic with
Gorenstein normalization, including all full conductor schemes. Together
with this lane it gives the following exact picture for (5,8):

| Quintic carrier | Disposition | Scope of the input |
|---|---|---|
| Normal, globally ADE | Excluded | This lane, only the (5,8) pair |
| Normal, with a non-ADE singularity somewhere | Open | The point may be off C; ADE only along C is insufficient |
| Nonnormal, Gorenstein normalization | Excluded | Separate conductor theorem, every mate degree |
| Nonnormal, non-Gorenstein normalization | Open, with additional restrictions | Full inverse support and actual section descent still required |

“Gorenstein normalization” is not “Gorenstein quintic”: the hypersurface
itself is Gorenstein, and the conductor theorem explicitly requires
nonnormality. Nor can the ADE theorem be applied to a nonnormal quintic
merely because its normalization has ADE singularities.

The [genus-two source note](2026-10-31-quintic-genus-two-toric-source.md)
and its inherited structural audit remove sectional genera zero and one
from the nonnormal boundary. The remaining normalization sectional genera
are 2–5; rationality is established through genus three. In genus two the
marked curve is a section of the conic ruling on the resolution, with
essential horizontal exceptional correction. These are restrictions on
actual polarized normalization models, not a classification of all survivors.

This combination changes where a quintic search can usefully take place.
It does not exclude all quintics, all (5,8) presentations, or presentations
of higher defining degrees. All the new carrier contributions remain
reviewed provisional mathematics; the promoted lower-degree exclusion
[R-0001](../results/quartic_carrier_exclusion.md) retains its own scope.

## 3. What the other branches contribute, and what this lane returns

The comparison fixes the following committed sources; later edits are
outside its evidence perimeter:

- Characteristic-zero carrier and strategy branch: `7530d052c4ea198916e399de034ba4a16a7c74d2`.
- Spectral realization: `0046beca62e36a1f1d02bdd05dbf900dd5670b56`.
- Complexity/torsion-two: `28756229308313912eb5e98ab2b21c08d828f78c`.
- Positive-characteristic degree/lifting: `563fa53652fcb1763427a69799b195f7a6d8e438`.
- Cleanup integration: committed `fd50fb66a8457628b5d9de2f9e4835cdb8656a46`,
  with a subsequent active working draft observed but not treated as reviewed
  committed evidence. The legacy `317d5bc` branch is already an ancestor of
  the selected characteristic-zero checkpoint; it is not an additional
  independent result stream.

For a source on another branch, read its fixed Git object with
`git show <commit>:<path>`. The paths below identify mathematical owners,
not a request to merge another branch's navigation or rerun its computations.

### Actual roots and actual equations

At the spectral checkpoint,
`research/synthesis/order_three_roots_and_sextic_lifts.md` supplies a full
parameterization of smooth order-three spectral roots and completes one
two-parameter lifting slice. Four of its six first-compatible roots fail
the actual sextic symbol test; the other two fail the cubic lift, retaining
the full allowed corrections. The larger-slice continuation is explicitly
unreviewed and is not used here. The graded constructions in
`research/synthesis/spectral_pushforward_powers.md` do not by themselves
supply embedded equations for C.

At the torsion-two checkpoint,
`research/supplements/QUADRATIC_ROOT_TORSION_TWO_REDUCTION.md` closes the
pure-direction and exceptional rank-drop families while retaining an open
mixed-direction rational chart. Finite-field emptiness there is not rational
emptiness. Its
`research/supplements/ACTUAL_OCTIC_ROOT_LIFT_COMPARISON.md` builds an
intrinsic first-lift map modulo **all actual equation corrections**, and
finds substantial first-lift flexibility. It also certifies an actual proper
(8,8) pair with transverse length eight and residual degree 32.

These results sharpen this lane's construction standard: a surviving root,
a graded CI, and even an actual first lift need not give sole support.
Conversely, the quintic result demonstrates why support and location of a
small saturated-layer divisor can eliminate numerical survivors. It gives
no reduction of those other source spaces to the four ADE rows.

There are distinct torsion classes here. The spectral class
\(\eta=\mathcal O_\Sigma(-1,1)\in\operatorname{Pic}(\Sigma)\) is not
the quintic class \(5C-4H\in\operatorname{Cl}(S)[2]\). Their orders do
not define a comparison map. The quintic's generically curvilinear,
nonzero-linear-symbol setup is also not automatically a smooth quadratic
spectral-root model.

### A genuine cover comparison, with a missing hypothesis

The spectral checkpoint's `research/supplements/SEXTIC_PAIR_REDUCTION.md`
already constructs an order-three **Weil-class** cover of a normal sextic
carrier and computes invariants of that normal covering surface. It permits
nonrational singularities and leaves a necessary irregularity lower bound
without a contradictory upper bound. Its normal cover cannot be substituted
for a smooth minimal resolution in a surface inequality without correction.

Thus this lane supplies a successful example of the missing kind of step:
control resolution invariants and the canonical map, then compare an actual
embedded defect. It does not supply that control for singular sextic covers
or for normal non-ADE quintics. This is a comparison of existing results,
not authorization to extend the present degree investigation.

### Symmetry and arithmetic give different restrictions

At the positive-characteristic checkpoint,
`research/supplements/EQUIVARIANT_DEGREE_BOUNDS.md` proves a
characteristic-zero exclusion whenever either equation is homogeneous for
weights (0,1,3,4), with arbitrary mate. Its proof includes the reduction from
one such equation to two, so it also covers a nonconstant weight-homogeneous
factor. It is an independently reviewed family theorem, not a reduction of
arbitrary pairs to that family.

There is an immediate useful consequence for the actual octic system:
**a hypothetical (5,8) pair has no weight-homogeneous member among
\(G_8+F_5H_3\)**, and F5 itself is not weight-homogeneous. Otherwise that
member and F5 would be a supported pair in the excluded family, since their
ideal equals \((F_5,G_8)\). This restriction applies to the non-ADE boundary
as well. Properness excludes a zero member of the family. The restriction
does not follow from an ADE assumption or a bound on torsion.

The same branch's `research/supplements/FROBENIUS_POWER_LIFTING_PRECISION.md`
instead treats prescribed powered-quartic special fibers. It establishes
exact strong Witt precision and necessary ramification, and forces a nonzero
endpoint specialization defect in surviving supported traits. Those results
do not construct characteristic-zero lifts or constrain every unrelated
characteristic-zero pair. Their endpoint embedded-point sheaf is not the
quintic multiplication divisor D2. The shared value is sensitivity to where
a defect occurs; identifying these sheaves would require new evidence.

## 4. Recommended next work and explicit stopping rules

**First scientific priority: finish the existing marked toric-source test.**
The [genus-two source](2026-10-31-quintic-genus-two-toric-source.md) has
already supplied actual data beyond numerical compatibility: a non-Gorenstein
normal surface X, a marked rational normal quartic c, and a section
\(q\in H^0(X,4H)\) with entire divisor 5c. Its source and marked-curve
reduction is exhaustive within toric quintic normalizations. One finite
projection fails because the full inverse of C consists of c plus five
isolated points. The other admissible relative centers are not excluded at
the pinned checkpoint.

The next two tests should remain sequential:

1. Finish full inverse-support analysis for the admissible centers taking c
   to the fixed projective-equivalence class of C. Include exceptional center
   loci and endpoint fibers. A generic-center calculation does not close the
   source. If every center has extra inverse support, stop with an all-mate
   exclusion of this toric source.
2. For surviving centers only, test whether \(q^2\) belongs to the actual
   ambient octic restriction image. This is the degree-eight power-descent
   question through the full conductor, not just equality of line bundles.
   A positive answer must recover the octic and verify the proper supported
   intersection. A negative answer excludes that center for (5,8), without
   claiming that all powers fail.

The carrier owner already has an ongoing center continuation; this is a
recommendation to complete and review that work, not to duplicate it here.
A closed toric source would still leave nontoric non-Gorenstein sources and
normal non-ADE quintics. Do not automatically expand to another genus or degree.

**For the normal non-ADE boundary, require a new global comparison before
another singularity census.** The order-two class still exists on a normal
quintic, but the ADE proof's resolved cover invariants and local tables no
longer follow. A meaningful reopening input would be an actual marked
quintic family with controlled resolution corrections, or an independently
proved replacement inequality covering the intended class. A list of locally
possible singularities alone would not replace either ingredient.

The broader [strategy assessment](2026-10-31-unrestricted-strategy-assessment.md)
also explains what not to repeat. The Milnor inequality is already implied
by stronger local geometry in its stated C0 application (§37); the primary
complement invariants only detect degree compatibility (§§23–24). They add
no independent contradiction here. Its §38 proposed Chow Hom lemma and
exceptional-cover applicability closeout explicitly lack separate independent
review. They are not accepted proof inputs for this synthesis. An exact
reformulation or a proposed lemma is not an actual construction mechanism.

## 5. Preservation, integration and review

The four original lane files were preserved byte-for-byte in commit
`fd9e628`, already contained in the selected characteristic-zero checkpoint.
This closeout reuses them instead of recommitting duplicate untracked copies.
The d121 worktree was moved, after exact preservation checks, onto
`codex/quintic-octic-closeout-2026-10-31`, based at `7530d052`.

The cleanup worktree's active draft already contains
`research/synthesis/quintic_octic_ade_cover_and_triple.md` and associated
navigation updates. That is observed ongoing integration, not a claim of
committed or reviewed cleanup acceptance. Its owner retains the destination
proof homes. This pass changes no other investigator's worktree, imports no
competing navigation, and leaves canonical promotion to its separate process.
When this synthesis is integrated, retain its combined carrier boundary,
the distinction among torsion/defect objects, the invariant-octic consequence,
and the bounded next-test recommendation in the owning mathematical homes.

The new evidence is source comparison and the one-line invariant-family
consequence of the existing weight theorem. No inherited computation is
rerun and no new calculation script is needed.

Independent reviewer `/root/mathematical_reviewer` checked the complete
written synthesis against the pinned owning sources, including the combined
carrier boundary, new invariant-octic consequence, actual toric test sequence,
and differing review/scope limits on the other branches. Its disposition is
**scoped PASS, with no unresolved material finding**. A separate source
reader, `/root/branch_interfaces`, checked faithful preservation of the three
spectral, complexity and arithmetic contributions and the one-line consequence.
Neither review certifies the active cleanup draft, upgrades the unreviewed
larger spectral slice or Chow proposal, or promotes a canonical record.
Both bounded review assignments are complete; no further research is queued
in this lane. Recommendations above are future selection criteria.
