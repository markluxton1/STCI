# Resume reconciliation and structural research assessment

Date: 2026-10-06. Status: **RECONCILIATION / RESEARCH STRATEGY**.
No new mathematical theorem or computational exclusion is claimed here.

This assessment reads `CODEX_RESUME_2026-10-06.md`,
`AUDITED_STATE_2026-10-06.md`, `RESEARCH_RECORD.md`, and
`SUCCESSOR_HANDOFF.md` together with the relevant restored sources and
retained audit notes. The audited state is authoritative. Historical
recommendations in the other records do not override it.

## Checkout and historical boundary

The checkout was clean at the start of this reconciliation, on
`research/ultra-resume-2026-10-06`, HEAD `781f00c`. The historical
`ultra_mode` tip is `2e53a7b`, whose commit records the interrupted
five-hour session. Neither branch was switched or reset. No modification
to `main` was made.

The resumed branch restores selected working sources over the audited
consolidation. A source being restored, or an old calculation using exact
arithmetic, does not establish its mathematical conclusion. This session
used three read-only, nondelegating reviews to check the local-cohomology,
primitive/dx1, and carrier lanes. Agreement between those reviews is not
a replacement for the independently audited arguments already in the
repository. No substantial calculation was launched during reconciliation.

## Where the interrupted work had reached

The interruption left several active lanes rather than a single nearly
completed global theorem:

- Quartic local cohomology had been reduced to an order-four ancestor
  space of dimension 30, with 18 quartic multipliers and an exact
  74-dimensional multiplication target. The full incidence is 148
  bilinear equations in 66 variables. General degree-two direction charts
  and contact experiments were unfinished.
- Primitive degree-two quotient work had found actual fourth-obstruction
  zeros, disproving a proposed blanket primitive-quadruple exclusion.
  It then moved toward ambient quartic containment of the canonical triple.
  The restored `primitive47universal` sources retain both the universal
  generation/contact route and the unfinished arbitrary-triple incidence.
- MF6 work had progressed from numerical lists to intrinsic divisor
  identities and higher-normal valuation calculations. The remaining
  constant-direction type `(d2,d3)=(4,5)` had an exhaustive two-parameter
  triple family, a generic quartic kernel, and an unclassified exceptional
  incidence locus.
- Normal carriers and split sextics had acquired significant geometric
  reductions. Their remaining configurations were bounded or reduced to
  parameter families, rather than excluded.

References: `2026-10-06-localcoh-incidence.md`,
`2026-10-06-localcoh-e2-incidence-charts.md`,
`2026-10-06-mf6-type4-incidence.md`, and the restored sources they cite.

## Retained results and their precise scope

1. **Uniform order-one structure.** A quartic carrier has
   `L=O(e-7)`, `0<=e<=2`, with uniform early bounds:
   `(deg D2,deg D3)<=(5,8),(3,5),(1,2)` for `e=0,1,2` respectively.
   The audited minimum for `e=0` is initially one; the retained additional
   quartic-containment argument on fixed `C0` improves it to three.
   For arbitrary carrier degrees with an order-one equation, `e<=6` and
   bounded early defects hold, together with `16/a<=7-e` for the
   order-one carrier. These are not upper bounds on equation degrees or
   total multiplicity.
2. **Primitive fourth / quartic containment.** On the reduced,
   basepoint-free universal fourth-obstruction locus for `C0`, the
   canonical triple has a nonzero distinguished cubic `T` and
   `H0(I_C3(4))=T H0(O(1))`. Independent contact reconstruction certifies
   that this holds at every admissible specialization.
   Consequently the `e=2` branches of `(4,7)` and `(4,8)` are excluded.
   The same argument applies whenever a larger pair has a primitive
   canonical fourth. It does not exclude arbitrary larger `e=2` pairs
   with early defects.
3. **Local-cohomology reductions and exclusions.** The finite order-four
   bound, exact incidence specification, direction bound `e<=2`, and
   first-conormal image are retained. Both ruling-ratio slices, the pure
   constant directions, and the corrected normalized parity family are
   excluded under their recorded hypotheses. The generic-length theorem
   forces a surviving pair to have a curvilinear triple along the generic
   point, a cyclic ancestor of generic length four, and residual cycle
   degree four. These facts do not settle the full incidence.
4. **MF6.** The finite-flat saturated Gorenstein pairings and intrinsic
   first-normal pole identity are retained. On fixed `C0`, a quartic
   `e=0` carrier has `deg D2>=3`; the `(3,6)` nonregular branch is
   excluded. A possible survivor of that type has regular first-normal
   ratio. The `(4,5)` exceptional incidence and the `e=1` types remain.
5. **Normal and split carriers.** The stated normal quartic exclusions
   survive. Remaining rational-resolution B1/B2/B3/D configurations have
   compressed mate-degree bounds, reaching 13824 in the coarsest row.
   The totally ramified split `[2,2]` family reduces to the recorded
   one-parameter line `F_tau=-B^2+tau q K`; that line remains open.

References: the authoritative state sections A--F;
`2026-10-06-primitive-quadruple-audit.md`, section 5;
`2026-10-05-mf6-further-audit.md`; and
`2026-10-06-split22-finite-reduction.md`.

## Corrections and unproved statements

- The older assertion that all primitive degree-two fourth extensions
  fail is false. Primitive extensions exist; actual quartic containment
  supplies the audited obstruction in the stated degree pairs.
- The dx1/P-044 residual classification is **OPEN**, exactly as required
  by audited section G. The retained diagnostic establishes resultant
  identities and multivariate coprimality, not residual-open emptiness.
  A unit-ideal certificate after saturation by
  `x*u*(2*a+1)*(a+u+2*x)` is still missing.
- There is a potential comparison to investigate before repeating that
  elimination: the universal fourth-zero locus has linear equations
  `b0=-2*a1`, `b1=-2*a2`, apparently specializing to the old cross-section
  conditions `a=-1/2,b=-2`. An exact identification of the two coordinate
  and obstruction implementations has not been established in this
  reconciliation. This observation is a proof-comparison lead, not a
  repair of the authoritative dx1 gap.
- The faulty historical parity/seed scripts confused generator-coordinate
  coefficients with actual quartic forms. Their products had the wrong
  degree and their coefficient checks were vacuous. They are not proof
  inputs. The retained corrected parity certificate uses actual products.
- A lifted pure cubic top symbol is not an ancestor construction. In
  particular, a zero of its scalar coefficient does not imply target
  generation fails: the retained DVR counterexample has a cyclic module
  whose special fiber is not Gorenstein. The quartic-carrier primitive
  theorem must not be transferred to local-cohomology pairs, whose
  intersection has a degree-four residual cycle.
- Generic quartic kernels, interrupted resultants, and incomplete rank
  computations do not cover exceptional parameter values or infinity.
  Split-root reductions and normal denominator bounds are not exclusions.

## Genuine frontier

The repository has not proved that `C0` is not STCI. The global separation
is between the uniformly constrained **order-one branch** and the still
open **entirely-thick branch**. Within the quartic-carrier branch, `e=0`
and `e=1` remain, as do larger `e=2` pairs with allowed early defects.
Local cohomology retains all untreated degree-zero/one/two direction
strata and the full quartic incidence, followed by higher multiplier
degrees if necessary. The normal exceptional configurations, surviving
split families, and normalization/conductor descent obligations remain.

First-symbol arguments alone do not address the pole strata or the
entirely-thick branch. A structural continuation must retain higher
normal jets, saturated lattices, conductor data, or equivalent valuation
information.

## Preferred next structural task

Use the remaining MF6 constant-direction type `(d2,d3)=(4,5)` as the
smallest concrete test of a general principle: **bounded effective
defect must annihilate the actual embedded extension obstruction**.
This is a proposed proof task, not a newly proved principle beyond the
specific annihilation statements already recorded.

The existing exhaustive triple family has

    R=A+B(z-2)+z^2-2z+4,
    delta=z(z+2)R+16,
    Res_z(delta,R)=256.

Quartic containment forces `h=delta*S`. Its cubic normal coefficient is

    f3=-T/(8*delta^2*S),
    ord(D3-D2)=max(0,ord S-ord T)

at every finite point, including multiple zeros of delta. Here S is a
section of O(5), while the permitted total excess defect is only one.
Thus almost its entire zero divisor must cancel in T. Generic parameters
are already excluded. The useful next question is whether this required
cancellation can occur for an irreducible quartic anywhere on the complete
incidence, including rank drops and the moving infinity chart.

First formulate that question intrinsically as divisibility of sections
or annihilation of an extension class, and seek a short argument using
the complete quartic image and the one-unit pole budget. This could
eliminate a whole defect type without enumerating pole placements. If a
finite calculation is needed, it should certify the resulting high-common-
divisor or module-rank condition with its open loci, rather than expand
the previously interrupted full resultant. A special surviving quartic
must be retained if the structural claim fails.

Keep the actual quartic variable in the full linear incidence and allow
the possible extra defect point to range over P1. Geometrically the
question is whether the fourth layer can be an elementary modification
with at most one additional defect point. This formulation can handle
rank-drop quartics and the infinity point directly; the generic kernel
vector alone cannot. Any finite certificate should derive the nonlinear
second-frame transformation before using homogeneous divisor conditions.

This task has a complete two-parameter starting family and a precise
contradiction threshold. It is therefore a more controlled next move than
the unfinished 43-variable local-cohomology charts or the 66-variable
bilinear system. It may also supply a useful model for the remaining
quartic `e=0/e=1` early-defect geometry.

The next local-cohomology structural task is analogous but distinct:
derive target-specific pole restrictions on the highest ancestor
coefficient. For `e=2` that coefficient belongs to O(1), so there is only
one top-symbol zero. Its possible cyclic-module degeneration must be
analyzed without assuming Gorenstein special fibers. The corrected
parity polynomial-dual method provides a model for a later exact
certificate after structural reduction.

## Immediate reproducibility boundary

The source/exporter and several JSON certificates are restored, but the
following referenced generated inputs are absent in this checkout:

- `computations/localcoh-incidence-tensor.txt` and
  `computations/localcoh-incidence-bases.txt`;
- `computations/localcoh-symbol-numerators.txt`;
- the general `computations/localcoh-e2-incidence-2026-10-06.py` chart
  exporter and exported chart systems;
- the parity discovery `.m2` file;
- `scratch/mf6_type4_incidence.json`.

The retained tensor exporter correctly sums all four generator
contributions and can regenerate its two outputs. The MF6 exploration
source can regenerate its generic matrix and S,T data. Other missing
coordinate prerequisites need to be located or reconstructed before
claiming a live certificate rerun. Their absence does not reverse the
audited mathematical status; it limits immediate reproducibility.

Validation in this reconciliation consisted of reading the specified
records and relevant sources, comparing their scopes, inspecting branch
and file provenance, and checking generated-input availability. Existing
mathematical verifiers were not rerun, and no new substantial calculation
was begun.
