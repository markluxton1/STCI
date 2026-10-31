# STCI package closeout: audited claims, geometry, and exact remaining work

October 31, 2026. Consolidator: root, with independent obstruction,
existence, projection and geometric review lanes. **The package is
closed out with the unresolved interfaces specified below. All new
mathematics remains reviewed provisional. No canonical promotion is made.**

Throughout,
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_k,
\]
with \(k\) algebraically closed of characteristic zero. **The unrestricted
STCI question remains open.** No actual defining pair or theorem covering
all higher-degree carriers is supplied. For proper containing pairs retain
\[
[V(F_a,G_b)]=m_C[C_0]+R,\qquad ab=4m_C+\deg R.
\]
The ambient normal order of an equation differs from \(m_C\).
Exceptional vertical data is not automatically a curve in \(R\).

## 1. Actual state and authority

The initial checkout was clean on
*codex/intersections-containing-quartic-2026-10-27*, HEAD *317d5bc*.
No checkout, merge, reset, commit or push was performed. Evidence paths
were preserved. Completion was determined from saved arguments,
assertions and final output markers, rather than commit titles, dates
or interrupted agents' last messages.

Retrieval followed [AGENTS.md](../../AGENTS.md), [INDEX](../INDEX.md),
[MAP](../MAP.md), [STCI_GAME](../STCI_GAME.md),
[STCI_SEARCH](../STCI_SEARCH.md), [authority](../AUTHORITY.md) and
[contribution](../CONTRIBUTING_AGENT.md) rules. Accepted reviewed
results were used as premises without replaying their inherited proofs.

The promoted baseline is unchanged:
[R-0001](../results/quartic_carrier_exclusion.md), with its accepted
factor/lower-degree reduction, forces both defining degrees at least
five; [R-0020](../results/quartic_conormal_characteristic_jump.md)
supplies the balanced conormal splitting; and
[R-0003](../results/fixed_carrier_conductor_criterion.md) is an exact
fixed-carrier full-conductor criterion. None classifies all higher-degree
presentations. R-0003 retains its recorded provenance limitation:
independent reviewers are reported in the proof note without a separate
identified audit artifact.

## 2. Final audit/status table

| Claim or computation | Final verdict and literal scope | Evidence and independent review |
|---|---|---|
| All-degree actual-quadric-residual obstruction | **PASS** for \(m\ge1,a\ge3m,b>0\), with full reduced irreducible horizontal first root, actual reduced residual and ordinary attachments. A nonempty dense open of every full actual source meets the hypotheses. | [Source](2026-10-30-stci-game-obstruction.md); [final audit](2026-10-31-stci-closeout-obstruction-audit.md); [geometric cross-review](2026-10-31-stci-closeout-geometric-review.md) |
| Component-slope balance | **PASS necessary condition** for full reduced horizontal ordinary root components. Vertical factors cannot be deleted before applying it. | [Audit §4](2026-10-31-stci-closeout-obstruction-audit.md) |
| Weighted subalgebra, including the mixed sextic seed | **Previously reviewed exclusion in every mate degree**, for the squarefree axis-free scalar-coefficient source. Repeated/axis boundaries remain outside it. | [Theorem](2026-10-30-weighted-subalgebra-line-obstruction.md); [audit](2026-10-30-weighted-subalgebra-line-audit.md) |
| Common-cubic lifting source | **Previously reviewed** actual scheme containment and \(R\ge mR_H,\deg R\ge2m\), including doubled rulings, for its literal proper pairs. | [Source](2026-10-30-stci-game-quadric-boundary.md); [audit](2026-10-30-stci-game-quadric-boundary-audit.md) |
| Elliptic double-lift torsion, global sections and fixed octic normalization | **PASS for the literal construction and fixed member** \((\mu,\rho)=(2,0)\): smooth, basepoint-free finite birational map, integral degree-eight image. | [Source](2026-10-30-stci-game-existence.md); [final audit](2026-10-31-stci-closeout-existence-audit.md); [saved output](../computations/stci_game_existence_2026_10_30.txt) |
| Fixed octic inverse support and normal geometry | **Rejected in every mate degree.** Affine length 24/projective isolated length 12; order two, vertical degree twelve, horizontal \((6,2)\) root with elliptic normalization. Scheme-theoretic image containment passes; equality and multiplicity one are unproved. | [Existence audit §§3–4](2026-10-31-stci-closeout-existence-audit.md) |
| Full five-parameter double-lift and degree-five filter | **OPEN support/descent locus.** Degree-five exclusion passes only on a verified actual irreducible quadratic first-normal-form locus. | [Existence audit §§5–6](2026-10-31-stci-closeout-existence-audit.md) |
| Primitive elliptic order-two residual; coplanar-support obstruction | **Previously reviewed necessary conditions and exclusion.** Zero-middle support fails actual source extension for every contact distribution. Full primitive elliptic and order-one loci remain open. | [Survivor](2026-10-30-projection-order-two-survivor.md); [extension theorem](2026-10-30-projection-elliptic-target-incidence.md); [prior audit](2026-10-30-projection-elliptic-target-incidence-audit.md) |
| Explicit palindromic elliptic target | **PASS target incidence; FAIL marked source extension.** Four unique smooth normalized contacts of order five; preserved as a useful intermediate example. | [Target source](2026-10-30-projection-elliptic-target-palindromic.md); [projection audit](2026-10-31-stci-closeout-projection-audit.md); [new control](../computations/stci_closeout_palindromic_independent_2026_10_31.m2), [output](../computations/stci_closeout_palindromic_independent_2026_10_31.txt) |
| Balanced degree-ten resultant/number-field chart | **Completed classification, independent PASS.** Excludes the stated nonzero-middle affine degree-ten discriminant chart, not all elliptic targets. | [Saved classification](../computations/stci_projection_elliptic_target_degree_ten_resultant_2026_10_30.txt); [new independent control](../computations/stci_closeout_degree_ten_independent_2026_10_31.m2), [output](../computations/stci_closeout_degree_ten_independent_2026_10_31.txt); [audit](2026-10-31-stci-closeout-projection-audit.md) |
| Balanced degree-twelve discriminant chart | **STOPPED / UNFINISHED.** The source was built; nonzero-middle saturation never reached its completion marker. Lower charts and the separate resultant route do not finish it. | [Source](../computations/stci_projection_elliptic_target_2026_10_30.m2); [stopped wrapper](../computations/stci_projection_elliptic_target_nonzero_middle_2026_10_30.m2), [partial output](../computations/stci_projection_elliptic_target_nonzero_middle_2026_10_30.txt); [audit/specification](2026-10-31-stci-closeout-projection-audit.md) |

The saved obstruction output reaches
*GAME_OBSTRUCTION_GEOMETRIC_CONTROLS_PASS*; the existence output reaches
*EXISTENCE_SOURCE_FIXED_INPUT_AND_NORMAL_GEOMETRY_EXACT_CHECKS_PASS*,
after its image, symbol, discriminant and scheme-containment stages.
The degree-ten output reaches *DEGREE_TEN_PARAMETER_CLASSIFICATION_COMPLETE*.
These markers complete their displayed stages, not every nearby general
claim. The new controls end in *INDEPENDENT_GCD_LAYER_CONTROL_COMPLETE*
and *PALINDROMIC_TARGET_CLOSEOUT_CONTROL_COMPLETE*, each with exit zero.
The stopped degree-twelve output lacks *NONZERO_MIDDLE_SATURATION_DONE*.

## 3. Strongest established geometric principles

### The actual quadric residual contradicts proportionality

Use sheaf powers \(V_{a,m}=H^0(\mathcal I_C^m(a))\). On the unique
quadric \(Q\), \([C]=(1,3)\) and \(\mathcal O_Q(1)=(1,1)\).
Assume exact normal order \(m\), \(q\nmid F\), and a **full**
reduced irreducible horizontal first-normal divisor. Require the actual
restriction
\[
\operatorname{div}_Q(F)=mC+T,\qquad [T]=(a-m,a-3m)
\]
with \(T\) reduced, no \(C\) component, reduced nonendpoint \(T\cap C\),
and a simple attached normal root at every intersection. The local
blowup graph makes the normalization regular and the attachment simple.

Under a hypothetical mate, factor reduction and the irreducible first
form force the carrier integral. Its finite normalization has a single
inverse curve \(\Gamma\to C\) of degree \(m\). For
\(H=\nu^*\mathcal O(1)\), the mate divisor would be \(r\Gamma\sim bH\).
Hyperplane degree and restriction to the **actual** residual give
\[
ab=4mr,\qquad b(2a-4m)=r(4a-6m).
\]
Every attachment contributes exactly \(r\), from its local divisor
equation; multiplicities are not guessed from total degrees. Elimination
requires
\[
2a^2-7am+8m^2
=2(a-7m/4)^2+15m^2/8=0,
\]
which is impossible. The two actual curve classes detect that the
inverse curve cannot be proportional to the hyperplane polarization.

For every \(a\ge3m\), cubic residual quadratics and ambient forms span
the complete actual \(T\)-restriction system. Products of cubic symbols
give a basepoint-free actual system of class \((4a-7m,m)\).
Characteristic-zero incidence/Bertini, connectedness and actual
value/vertical-derivative jets yield a nonempty dense open satisfying
all hypotheses. Full abstract symbol surjectivity is unnecessary.
The final audit gives a direct incidence argument, avoiding an unchecked
immersion hypothesis in the previously cited Bertini formulation.

For several full reduced horizontal ordinary components, with covering
and direction degrees \(e_j,d_j\), the same actual attachments yield
\[
\frac{\sum d_jr_j}{\sum e_jr_j}=7-\frac{16m}{a},
\qquad \exists j:\ d_j/e_j\le7-\frac{16m}{a}<7.
\]
This is only necessary. The special complement with vertical factors,
repeated roots, low slopes or defective attachments remains open.

### Large lifting spaces can preserve a fixed residual

In the reviewed common-cubic source at \(d=3m+2\),
\[
F=f_2H_3^m+K,\quad G=g_2H_3^m+L,\quad
K,L\in H^0(\mathcal I_C^{m+1}(d))=qV_{3m,m},
\]
both equations lie in \((q,H_3^m)\). Every proper pair therefore contains
the actual scheme \(V(q,H_3^m)\), retaining \(mR_{H_3}\).
The lifting kernel vanishes on \(Q\), so its dimension cannot move
that residual restriction. Similarly, cancellation over \(k(C)\)
need not produce an actual homogeneous polynomial row. These statements
retain their family hypotheses.

### A valid normalization model can still fail full inverse support

The elliptic construction uses
\[
E:y^2=x^3-x,\quad T=(i,1-i),\quad
M=\mathcal O_E(4O),\quad L=\mathcal O_E(O+T).
\]
Order-four torsion gives \(L^4=M^2\), \(L^2\ne M\).
For \(A=(y+1-i)/(x-i)\) and
\(\phi=(y+(1+i)x)^2/x\), the divisor calculation produces four
actual sections \(\phi,\phi A,\phi A^3,\phi A^4\) of \(M^2\).
Their quadratic lifts give the marked degree-two map. On
\(S_\mu=V(Q_1+\mu Q_0)\), \(\Gamma=V(Q_0)\sim H=(2,2)\),
so \(b\Gamma\sim bH\) is linearly possible upstairs.

The fixed member realizes a genuine octic normalization, then fails
through isolated extra inverse support. A nonzero Cartier zero divisor
on the smooth source cannot have those isolated points. The affine
\(Q_0=1\) cone chart is a free étale double cover of the projective
complement, explaining 24 versus 12 even for nonreduced schemes.

Its full first symbol has class \((18,2)\), vertical degree twelve and
horizontal \((6,2)\), with arithmetic genus five and normalization
genus one, hence total delta four. Its horizontal slope three equals
the required \(7-16m/a\) at \((8,2)\); the vertical part makes it
outside the ordinary theorem. The extra scheme's image factors through
the vertical divisor, but local conductor contributions and image
multiplicities remain unknown. Matching degrees twelve proves no equality.
The ambient deck action \(\mu\mapsto-1/\mu\) need not preserve
the source surface; the old degree-one inverse argument is inapplicable
without its missing hypotheses.

### Target incidence, source extension, inverse support and descent are distinct

For the surviving diagonal order-two source, the elliptic residual
maps birationally to a target \(C'\subset Q\) of class \((6,2)\).
Its ruling bundles obey \(L^2=\mathcal O_D(Z)\), \(M=L^3\).
The degree-twenty function \(B^3/A\) has only three branch values
and four points over one. This is a necessary finite cover problem,
not a completed enumeration or source construction.

The support quartic \(t^4+a t^3+b t^2+c t+d\) has \(b=0\)
exactly when the four marked images on \(C_0\) are coplanar:
hyperplane restrictions omit \(s^2t^2\). The actual Picard identities
and degree-two interpolation then force the two proposed source
pencils to coincide, contradicting the elliptic \((2,2)\) embedding.
The exclusion covers every contact distribution.

The example \(R=t^4+\alpha t^3+\alpha t+1\), \(\alpha^2=-4/5\),
\(P=R^5\), really has elliptic target normalization and four unique
smooth normalized contacts of order five. It passes target incidence,
but fails marked source extension by coplanarity. A source must next
pass full inverse support and finite birationality, then full-conductor
descent, including nilpotent gluing. A Picard identity alone does not
descend a section. A successful pure-power coordinate identity is
stronger and itself guarantees full inverse support.

## 4. Completed existence/obstruction exchange and general STCI impact

E1's common-cubic lift failed uniformly because every correction
preserved residual rulings. E2's shared moving normal factors were a
source proposal, not a supported pair. Independently, N3 enlarged
test-line exclusions to the entire actual quadric residual on the
ordinary open in every full degree/order source.

E3 changed the inverse curve to an elliptic double cover. Its torsion,
global sections and fixed octic are real. Its fixed carrier fails in
every mate degree. N3 accepts that this does not exclude E3's full
five-parameter source: its observed vertical and singular horizontal
data change the ordinary hypotheses.

The strongest surviving existence strategy is to absorb extra inverse
support in those actual parameters, preserve the morphism and birational
octic image, then achieve pure-power descent. The degree-five filter
requires verified irreducibility of the actual quadratic first normal
form; degenerate-leading strata remain. Raising the mate degree on
the failed fixed carrier cannot help.

The independent non-existence strategy has a broader result to retain:
actual divisor/attachment balance across degrees, component slopes,
fixed-boundary rigidity and the previously reviewed arithmetic
conductor-jet mechanism. The missing universal bridge is control of
special vertical, repeated, low-slope and defective attachments in
actual global pairs; the opponent's proposal does not delimit that
program.

The [arithmetic continuation](2026-10-29-search-continuation.md)
retains an attained degree-\(p\) minimum on its specified two-non-binomial
source. It supplies no all-pairs lower bound. The constructibility
equivalence between characteristic-zero nonexistence and growth of
the all-pairs \(\delta(p)\) is a reduction, not its execution.
[Residual constructions](2026-10-28-containing-intersections-synthesis.md)
and [quantitative bounds](2026-10-28-residual-degree-synthesis.md)
remain scoped inputs; flexible attachment and zero numerical floors
do not prove absorption or STCI.

Thus ordinary carriers in these dense opens and the explicit failed
sources are removed. No exhaustive classification, universal residual
floor, all-pairs arithmetic growth theorem or actual characteristic-zero
defining pair follows. The general question remains open.

## 5. Ranked unresolved interfaces: literal next conditions

These are continuation specifications for existing questions, not new
assignments. Ranking reflects proximity to an actual equation and
clarity of the missing test; no source is asserted exhaustive.

1. **Five-parameter elliptic double-lift: support, then descent.**
   Work over \(B=\mathbf Q(i)[\mu,\rho_0,\rho_1,\rho_3,\rho_4]\)
   with \(U_j=V_j+\rho_jQ_0\), using the exact quadratic rows in
   the existence source, and invert \(\mu(\mu^2-1)\) for smooth
   source quadrics. Retain fiberwise projective basepoint saturation
   and degree-eight image/birationality. The first unexecuted condition is
   \[
   (Q_1+\mu Q_0,Q_0-1,
   U_0U_4-U_1U_3,\ U_1^3-U_0^2U_3,\
   U_1^2U_4-U_0U_3^2,\ U_3^3-U_1U_4^2)=(1)
   \]
   on every retained geometric parameter fiber. Equivalently saturate
   the projective inverse ideal by \(Q_0^\infty\) and the irrelevant
   ideal; no additional \(Q_0\) saturation is needed in \(Q_0=1\).
   Saturation followed by specialization cannot replace fiberwise
   conditions. On a surviving admissible stratum ask
   \(Q_0^b\in\langle U^e:\sum e_j=b\rangle\bmod(Q_1+\mu Q_0)\).
   The monic \(Z_2^2\) rule gives matrices \(169\times84\) for
   \(b=6\), \(289\times165\) for \(b=8\), plus one target column.
   Membership is equality of ranks on **all** strata. These universal
   matrices and the support-unit locus are unexecuted.
   [Full ring, basis, saturation and admissibility specification](2026-10-31-stci-closeout-existence-audit.md).

2. **Primitive elliptic target and actual marked extension.**
   For every positive four-part contact partition \(\sum n_i=20\),
   take \(P(t)=\prod(t-t_i)^{n_i}\) with distinct nonzero support,
   normalize one \(t_i=1\), and regroup uniquely as
   \(e_0(t^3)+t e_1(t^3)+t^2e_2(t^3)\).
   Require primitive actual bidegree \((6,2)\), elliptic normalized
   discriminant \(e_1^2-4e_0e_2\), exactly four normalized inverse
   points, and noncoplanar marking. Then construct the two marked
   source degree-two pencils, the \((2,2)\) embedding and four
   extended sections. The balanced chart has
   \(P=(t^4+a t^3+b t^2+c t+1)^5\) over
   \(\mathbf Q[a,b,c,s_0,s_1,s_2,s_3]\).
   Divide its discriminant by
   \((A^4+s_3A^3+s_2A^2+s_1A+s_0)^2\) and set its eight
   remainder coefficients to zero. The saved unfinished job
   saturates by \(b\,\operatorname{disc}(R)\).
   The actual degree-twelve chart also retains \(4b+3a^2\ne0\).
   Primitive bidegree, separable residual quartic, endpoint and
   normalized-point conditions are further tests. This degree-twelve
   chart remains uncomputed; degree-ten completion does not exhaust it.
   [Full coefficient ring, boundaries, outputs and extension tests](2026-10-31-stci-closeout-projection-audit.md).

3. **Order-one complete marked projections.**
   Use Segre \(ad=bc\), \(\Delta=b-c\),
   \(B=(a^2,ab,dc,d^2)\), and \(U_i=B_i+\Delta A_i\)
   with arbitrary \(A_i\in H^0(\mathcal O(1,1))\):
   sixteen scalar parameters. Impose determinant order exactly one,
   retain all seven principal coefficient opens, and test basepoints,
   full inverse support and birationality. On \(\Delta=1\),
   \(b=h+1/2,c=h-1/2\), the first unresolved off-diagonal condition is
   \[
   (ad-h^2+1/4,\ q(U),c_0(U),c_1(U),c_2(U))=(1)
   \]
   constructibly on every retained fiber. The \(c_j\) are the three
   cubic generators of \(I_{C_0}\). Then test
   \(\Delta^{2b}\in\langle U^\alpha:|\alpha|=b\rangle\).
   No complete order-one output exists.
   [Literal ring, equations, excluded orders and descent matrix](2026-10-31-stci-closeout-projection-audit.md).

4. **Special carrier complement and the universal bridge.**
   The next geometric implication is a valid replacement for
   \(b\deg T=\sum_jr_j(\widetilde T\cdot\Gamma_j)\)
   with actual local corrections for vertical, repeated and
   nonordinary data, or an exclusion of their realization by actual
   global pairs. A saturated horizontal cover, formal cancellation
   or matching defect degrees does not supply it. E3's proposed
   quotient/join-of-two-conics picture has no computed residual
   inverse class or saturation; that missing interpretation is not
   a uniform residual floor.

## 6. Changed files, validation and stopped computations

The common game ledger, search synthesis, STATE, FRONTIER, MAP, INDEX
and decision guide were reconciled around final statuses. Excluded
mate searches were removed as current recommendations. Historical
failed sources, counterexamples, exact computations and audit paths
remain available. Four October 30 source/review notes received current
review notices without rewriting accepted mathematics.

New evidence consists of this report, four closeout audits, two
bounded exact controls with saved output, and the
[validation record](../computations/stci_package_closeout_validation_2026_10_31.json).
No canonical result or question record was changed.

The new degree-ten independent resultant/gcd-layer control ran under
a stated external 60-second cap and completed in approximately thirty
seconds. The new palindromic number-field control also had a 60-second
cap; its final run completed in under one second, with degrees at most
twenty and no parameter Gröbner computation. Both passed. No large
Gröbner job was restarted, and the projection lane reported no running
job at its closeout.

The earlier degree-twelve saturation remains stopped, with source and
partial output preserved. The five-parameter support elimination,
universal degree-six/eight descent matrices, general primitive elliptic
incidence and order-one endpoint remain specified but unexecuted.
The interrupted degree-ten multivariate method is preserved as
interrupted; the independent resultant route completed that endpoint.

Final command results, link counts and inherited whole-tree limitations
are in the validation record. A clean core or changed-file link check
does not imply that historical snapshot links are all valid.

- Canonical validator: **37 records checked, zero errors**.
- Core navigation links: **300 destinations in 12 files, zero missing**.
- All modified/new Markdown: **492 destinations in 16 files, zero missing**.
- Whitespace/diff checks pass; canonical result/question files are unchanged.
- The whole-tree scanner reports **362 inherited flags**, exactly the
  clean-baseline list: 289 in archives, 63 in validation snapshots and
  ten live-note formula matches. There are no new flagged destinations;
  repairing historical snapshot links is outside this closeout.
- The change set has **21 files**: seven navigation/ledger files, four
  source-status notices, five new report/audit notes, four new exact-control
  files and the validation JSON. No commit or push was made.
