# Nonnormal carriers in the broader STCI investigation

Date: 2026-10-31. Scope: closeout and cross-branch strategy for the fixed
`C0=[s^4:s^3t:st^3:t^4]` over an algebraically closed field of characteristic
zero, with positive characteristic used as a comparison. This is a synthesis
and recommendation, not a new canonical result or an authorization to launch
another calculation. The unrestricted characteristic-zero question is open.

## 1. What this lane has actually established

The central gain is a carrier-class theorem with no bound on the mate degree:
an integral nonnormal quintic with Gorenstein normalization cannot be a carrier
of a sole-supported intersection on C0. The
[proof and independent review](2026-10-31-quintic-gorenstein-normalization-exclusion.md)
include integral, reducible and nonreduced full conductors. Their common
mechanism is actual conductor contact and descent of a quartic root, not
merely a numerical Cartier index. The separate
[globally ADE theorem](2026-10-31-quintic-octic-ade-exclusion.md) excludes
quintic–octic presentations whose quintic has only ADE singularities everywhere.
It does not exclude all normal quintics or all mate degrees on them.

Two reusable restrictions extend beyond that quintic theorem:

- The [differential comparison](2026-10-31-carrier-conductor-differential-bound.md)
  applies to an integral carrier of any degree at least five that is generically
  regular along C0. Its normalization cannot be smooth along the full lifted
  curve while its full scheme-theoretic conductor is smooth at every contact.
  Singularity generically along C0 is outside the theorem.
- The [fiber-degree inequality, §3](2026-10-31-quintic-genus-two-toric-source.md)
  gives `a<=dr` for a generically regular degree-a carrier of a smooth degree-d
  curve, with an actual sole-supported mate and a resolved-normalization
  fibration of hyperplane fiber degree r<d. For C0, conic-fiber models of
  degree at least nine are excluded. It is not a classification of every
  normalization, and does not apply unchanged to a higher-degree inverse curve.

The next source was genuinely constructed. The
[toric quintic](2026-10-31-quintic-genus-two-toric-source.md) has non-Gorenstein
singularities, the fixed marked quartic, and an actual section q of 4H with
`div(q)=5c`. Polygon and marked-curve arguments make this source exhaustive
within toric quintic normalizations. Its displayed projection has five extra
inverse points, so no mate of any degree can work on that projected surface.
The [center calculation](2026-10-31-quintic-toric-center-incidence.md) now excludes
the whole one-infinity boundary, the generic finite centers and three further
exceptional curves. One explicit locus M=0 remains, with an exact support
condition. The interrupted calculation did not classify that locus.

These are independently reviewed provisional findings. The promoted
[quartic-carrier exclusion](../results/quartic_carrier_exclusion.md) remains
the lower-degree anchor: both degrees of a hypothetical characteristic-zero
presentation must be at least five. No fifth-degree or unrestricted exclusion
follows by accumulating the special classes above.

## 2. Which branches were compared

The comparison refreshed origin and read the following committed states.
Some other worktrees acquired new edits while this review was running; those
edits are outside these fixed snapshots. Branch names are locators, not proof
authority. A source path in this table is retrievable by
`git show <commit>:<path>` even when its file is not in this checkout.

| Branch and fixed commit | Contribution relevant to this lane | Exact remaining limitation |
| --- | --- | --- |
| `main`, `9d734e1b03dc2de1faf3d2497ce2916cec5c4dac` | Promoted quartic-carrier exclusion and fixed-carrier support/conductor criteria in `research/results/` | This older branch is not a summary of all later research. |
| `origin/codex/intersections-containing-quartic-2026-10-27`, `b271fc5bf20a6920b1540cabd57f095139d8d7a5` | Reviewed actual elliptic double-inverse construction and package closeout; `research/notes/2026-10-31-stci-package-closeout.md` and its existence/projection audits | The fixed octic has extra inverse scheme of length twelve; its complete five-parameter support/descent family remains open. |
| `restructure/mathematical-consolidation`, `fd50fb66a8457628b5d9de2f9e4835cdb8656a46` | Maintained proof homes and broader containing-intersection account, including `research/synthesis/elliptic_double_inverse_construction.md`, `quadratic_covers_and_conductor_descent.md` and `supported_linkage_operations.md` | This committed integration predates our Gorenstein-normalization and toric-source checkpoints. Its later integration edits were not treated as reviewed committed mathematics. |
| `codex/stci-char0-four-streams-2026-10-30`, `7530d052c4ea198916e399de034ba4a16a7c74d2` | Our commits `fd9e628` and `843acdf`, plus actual source failures and arbitrary-pair comparisons in [the strategy assessment](2026-10-31-unrestricted-strategy-assessment.md) | Primary topological/algebraic Euler tests and the pencil Milnor budget do not add the needed quartic obstruction. The final proposed Chow Hom lemma has an explicit independent-review gap; it is not a premise here. |
| `codex/positive-characteristic-degree-bounds-2026-10-31`, `563fa53652fcb1763427a69799b195f7a6d8e438` | Actual positive-characteristic equations and reviewed prescribed-power lifting/precision restrictions; `research/supplements/FROBENIUS_POWER_LIFTING_PRECISION.md`, `EFFECTIVE_CHARACTERISTIC_TRANSFER.md` | Necessary ramification and endpoint defects do not construct a characteristic-zero lift or exclude unrelated presentations. |
| `codex/spectral-realization-2026-10-31`, `0046beca62e36a1f1d02bdd05dbf900dd5670b56` | Actual spectral torsion/determinant schemes and complete actual-sextic test of one root slice; `research/synthesis/order_three_roots_and_sextic_lifts.md`, `spectral_pushforward_powers.md`, `spectral_determinant_schemes.md` | A rational seven-dimensional root parameter space is not an exhausted incidence. One tested slice closes; the larger-slice lead is explicitly unreviewed. |
| `codex/stci-complexity-torsion-two-2026-10-31`, `28756229308313912eb5e98ab2b21c08d828f78c` | Actual octic-source quotient and a proper homogeneous (8,8) pair with generic length eight and residual degree 32; `research/supplements/ACTUAL_OCTIC_ROOT_LIFT_COMPARISON.md` | First compatibility and joint generation do not extend the obstructed seed to sole support. Properness does not establish irreducibility of either carrier. |

The detached `966a` checkout at `586a84f` retains a consolidation checkpoint
on projected-source section defects, not another current carrier calculation.
The `d121` checkout moved during this review onto
`codex/quintic-octic-closeout-2026-10-31` at the same `7530d05` snapshot;
no additional committed mathematical difference was present at that inspection.
This assessment makes no branch merge, rebase, retirement, push or canonical
promotion. Each source keeps its own review status.

## 3. How the findings change each other

**Singularity is now a meaningful constraint, but not a universal prescription.**
The quintic theorem rules out a whole normalization class, even with bad
conductor schemes. It therefore justifies studying non-Gorenstein quintic
normalizations. It does not justify assuming that every useful higher-degree
normalization must be non-Gorenstein. The elliptic construction at b271fc5,
preserved in the fd50fb6 proof home, already gives a smooth quadric X with
`H=(2,2)`, an integral degree-eight image, and an elliptic curve Gamma mapping
two-to-one onto C0. The degree is different, and the inverse over C0 is not
an isomorphic copy of C0. The generic-regularity and singleton hypotheses of
our broader differential/fiber comparisons therefore do not apply unchanged.
That source is a concrete route outside our excluded hypotheses, although its
tested projection still fails full support. Its implicit octic has a degree-twelve
vertical first-symbol divisor and a singular horizontal root of class (6,2);
it is not automatically within the saturated smooth (2,2)-root setting of
the spectral and octic-source comparisons.

**An actual section upstairs is a stronger starting point than a numerical
relation, and still leaves a substantive projection problem.** The toric source
has the actual q, not just `5c` numerically proportional to H. The elliptic
family has actual global quadratic sections extending its prescribed map on
Gamma. Both subsequently face full inverse support and membership of a pure
power in the coordinate subalgebra generated by the four projection sections.
Our quintic theorem derives a contradiction from exactly that actual descent.
The two constructions can share this test without identifying their local
conductor algebras or their inverse-curve degrees.

**The equation branches show where a carrier proposal must meet its embedding.**
On the spectral branch, exactly six smooth roots in a two-parameter slice pass
the first embedded compatibility test; four have no actual sextic symbol, and
the remaining two fail the complete cubic source system. This excludes that
slice of the conditional (6,16) movement-two row, not every sextic. On the octic
branch, every smooth first-compatible root has actual octics passing the first
comparison; the source quotient retains all permitted equation corrections.
The explicit seed even produces a proper pair. Nevertheless, its second root
obstruction is nonzero. For its (8,8) pair, the actual cycle identity is

    64 = 4*8 + 32,

where 32 is the degree of a genuine residual curve downstairs. This gives useful
geometry beyond STCI and a control for proposed absorption operations. It is
not a sole-support candidate waiting only for a longer computation. Both octics
have normal order two along C0; an integral member is therefore nonnormal along
C0. Factorization/irreducibility must be checked before attaching a single
normalization to either equation. Our generic-regularity theorem cannot be
silently applied to those carriers.

**Characteristic comparison explains a mechanism, not a limiting proof.**
The positive-characteristic branch supplies actual quartic-carrier presentations
for the same C0 in every p>0. For the prescribed family `(F_p,H_4^n)` with p>=7,
its strong unramified Witt precision is `1+v_p(n)`. A surviving supported
characteristic-zero trait would require `p|n`, ramification at least p-1, and
positive endpoint specialization defect. Increasing n gives arbitrarily high
finite precision while changing degrees; it does not give a single compatible
fixed-degree lift. Nor is the lower-root endpoint defect automatically our
normalization conductor defect. A proof relating them would need an actual map
between the objects and control of the marked homogeneous equations.

**Degree and genus remain accounting constraints; the discriminating data are
embedded and local-to-global.** Proper complete intersections of fixed degrees
have the same Hilbert polynomial and arithmetic genus in every characteristic.
A hypothetical nonreduced structure supported on C0 must carry those invariants
through its nilpotent layers and attachment data. The invariants do not force
that structure to be the smooth general member or distinguish it from a pair
with residual components. The four-streams comparison separately shows that
its continuous/primary Euler tests see degree divisibility, and the proposed
quartic Milnor inequality is already implied by stronger local inequalities.
These are reasons to avoid another unconnected numerical budget, not reasons
to discard genus, conductor degrees or Hilbert functions when an actual
normalization, embedded thickening or equation-source map makes them effective.

The normalization quotient, arithmetic endpoint defect, spectral lifting
obstruction and octic source quotient measure different failures. No reviewed
comparison identifies these modules or allows their dimensions to be added
as independent obstruction budgets. Similarly, Gorensteinness of a transverse
complete-intersection algebra is not Gorensteinness of a surface normalization.

## 4. Recommended next work, with stopping outcomes

1. **Finish the existing toric support question in one bounded investigation.**
   Use the remaining M=0 condition in the [center note](2026-10-31-quintic-toric-center-incidence.md).
   The retained h has two distinct roots and W has degree five; sole inverse
   support requires every root of W to lie at those two points. The three
   unordered multiplicity patterns are 5+0, 4+1 and 3+2. Factored coefficient
   equations, or exact divisibility on the normalization of M, provide a more
   targeted formulation than an unbounded total-plane Groebner run. The possible
   outcomes are a covered exclusion of toric quintic normalizations, an actual
   admissible center for full conductor/power-descent testing, or a precisely
   unresolved algebraic locus. Full support by itself still does not construct
   a descending mate. Do not continue into arbitrary genus-three or higher-degree
   classifications merely because this calculation ends.
2. **Then broaden constructively through the existing elliptic double-inverse
   family.** Work with the actual five-parameter sections, smoothness,
   basepoint-free projection and degree-eight image conditions in the frozen
   proof home. First determine whether the fiberwise full inverse-support locus
   is nonempty on the admissible locus. A calculation only over the function
   field of parameters does not cover its exceptional fibers. Test coordinate
   subalgebra membership of a pure power only on surviving support strata. This
   changes both degree and the inverse-curve geometry in a source already built;
   it is better motivated than inventing a new degree-eight normalization solely
   to avoid the quintic theorem. Its single failed member does not exclude the
   family, and increasing the mate degree cannot repair that member's extra
   inverse points.
3. **Use the actual octic pair as a parallel geometric control, not an automatic
   absorption program.** A bounded question is to factor the carriers and identify
   the residual degree-32 scheme and its attachment to C0, then compare its actual
   normalization/conductor with the root-source obstruction if those maps can be
   constructed. A successful result would explain which geometric change a
   residual-reducing operation must make. No such operation is presently supplied;
   the known second-obstructed root should not be revived unchanged.

The first item has the clearest near-term completion criterion. The second is
the stronger existing avenue for broadening this lane. The third is valuable
if it yields a concrete comparison morphism or residual operation; a dictionary
of similarly named defects alone is not enough. The speculative toric
height-two degree-eight source has not been constructed and reviewed here.
It is a possible later alternative, not a result or the preferred immediate task.

These recommendations preserve the broader objective of understanding actual
containing intersections and singular carriers. A failed special construction
can be informative, and a successful containing pair matters even with residual
support; neither should be relabeled an unrestricted STCI conclusion.

## 5. Review and repository disposition

The lead inspected fixed local and remote branch states and the relevant proof
homes, including the maintained consolidation account. Independent reviewer
`/root/branch_crosswalk` reconstructed the spectral, arithmetic and octic scopes,
then challenged the cross-lane recommendation against the existing elliptic
construction. It specifically distinguished an octic mate on a quintic from a
degree-eight normalization, proper pairs from integral carriers, and the
second-obstructed octic seed from a sole-support candidate. The final written
scope review passed after adding the required p>=7 qualifier to the prescribed
arithmetic family. It does not re-audit every inherited proof or certify the
unfinished recommended investigations.

The separate `/root/center_closeout_audit` closed the pending U0/V1/V2
specialization gap by independent polynomial identities, denominator and
parameter-boundary checks, and native execution. The center note preserves its
exact scope and evidence. No new calculation of M, elliptic-family support,
octic residual decomposition or arithmetic lifting is part of this closeout.

The retained finite JSON is an actual input to the exception calculation, not
disposable printed output. The interrupted M scratch calculation is described
with its failed stopping condition, without preserving an unnecessary execution
tree. Existing proof/audit/certificate paths remain. Other source worktrees were
inspected without edits, no canonical record was changed, and no claim was
promoted. Navigation in this checkout links the closeout and its open boundary.
