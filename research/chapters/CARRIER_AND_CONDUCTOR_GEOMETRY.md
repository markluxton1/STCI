# Carrier and conductor geometry

A mate on an integral surface must have the right **entire inverse
support**, the right divisor class on its normalization, and compatible
sections over its full conductor. The quartic exclusion and higher-degree
candidate models use these operations in different geometric settings.
The unrestricted characteristic-zero question for the fixed
\(C_0=[s^4:s^3t:st^3:t^4]\) remains open.

## 1. A sole-support pair gives a divisor, not just a preferred inverse branch

For an integral carrier \(X\) with finite normalization \(\nu:S\to X\),
write \(H=\nu^*\mathcal O_X(1)\). A degree-\(b\) mate pulls back to a
Cartier section whose entire zero support is \(\nu^{-1}(C_0)\). When
this is a single curve \(c\cong C_0\), its divisor is
\[
nc\sim bH,\qquad n\deg C_0=b\deg X.
\]
Only for equal-degree quartic carrier and curve does this give \(n=b\).
Additional inverse branches and isolated inverse points cannot simply be
discarded. The [full-support proof and smooth-passage argument](../synthesis/quartic_carrier_proof.md#1-sole-support-smooth-passage-and-the-common-correction-identity)
explain which hypotheses remove them in the quartic case. The lifted
curve can remain non-Cartier at singular normalization points even when
its relevant positive multiple is Cartier.

If two forms cut out \(C_0\), every irreducible factor of either is itself
an integral carrier with the other as mate. Coprimality and purity prove
this even for repeated factors. The [factor proof](../synthesis/05-exclusions.md#52-factors-and-the-degree-bound)
then combines the plane, quadric, classical cubic and quartic exclusions
to force every irreducible factor to have degree at least five in
characteristic zero.

## 2. Normalization separates divisor class from conductor gluing

A section upstairs with the correct divisor may fail to descend. The
obstruction uses values and nilpotent jets on the **whole** conductor
square. Reduced conductor phases alone can lose additive gluing data.
The [full fixed-carrier descent theorem](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md)
owns the exact relation lattice and its positive-vector criterion;
[conductor descent algebra](../supplements/CONDUCTOR_DESCENT_ALGEBRA.md)
owns the local power/purity arguments. These are tests on an actual
carrier, not constructions for arbitrary higher-degree candidates.

Characteristic changes this step: a prime-characteristic power can kill
nilpotent conductor obstructions, and differentiating a mate power loses
its degree scalar when the characteristic divides it. In every positive
characteristic the fixed curve admits an actual quartic-carrier STCI;
see [the construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).

## 3. The all-degree quartic exclusion and its common mechanisms

The accepted [R-0001](../results/quartic_carrier_exclusion.md) excludes every
integral quartic carrier of fixed \(C_0\) in characteristic zero against
a mate of arbitrary degree. The [complete proof](../synthesis/quartic_carrier_proof.md)
reconstructs the geometry rather than repeating an old list of open cases:

- All lanes share the actual divisor relation and correction identity
  \(q+K_MZ=2\pi\), where \(\pi\) is the normalized sectional genus.
- Normal quartics use exceptional passage, rank/order and ideal-vanishing
  budgets; the final TypeD step is an equality of pulled maximal ideals.
- Nonnormal quartics have rational normalization. Genus zero uses the
  full scroll/Veronese/cone conductor geometry. Genus one forces a
  fixed-center del Pezzo ribbon projection and its five contact partitions.
- Genus-two bisections force a global nilideal \(\mathcal O(-8)\),
  incompatible with the fixed balanced conormal bundle. Sections force
  actual trisecants; the two-crossing cases share an all-length chain
  inequality, while the doubled-horizontal endpoint uses its cubic
  normal coefficient and actual ADE attachments.

The general ruled-surface criterion and ribbon Hom threshold isolate
reusable lemmas. The [numerical-pullback proof](../synthesis/numerical_surface_pullback.md)
owns the comparison between numerical correction and actual normal
degree. Distinct local proofs and counterexamples remain where they add
information; none reopens a closed quartic-mate case.

The [characteristic comparison](../synthesis/quartic_carrier_proof.md#8-what-changes-in-positive-characteristic)
states the precise invertibility, separability, Frobenius, conormal and
global-surface boundaries. The theorem does not transport to positive
characteristic or exclude higher-degree characteristic-zero carriers.

## 4. Cartier singleton lifts: a necessary classification, not a construction

Under the stronger hypotheses that the entire reduced inverse image is a single curve \(c\cong C\) and **\(c\) is Cartier on the normalization**, R-0002 classifies the possible normalization/polarization pairs. The mate makes \(c\) ample, and \(|c|\) realizes a normal surface of minimal degree. The proof uses the Cartier restriction sequence, surface classification and the singular cone case.

For the fixed quartic \(C_0\), after excluding quartic carriers, three necessary higher-degree models remain:

| Carrier degree | Normalization | Polarization and lift |
|---|---|---|
| \(8\) | \(\mathbf P^1\times\mathbf P^1\) | \(H=(2,2)\), \(c=(1,1)\) |
| \(8\) | Quadric cone | \(H=2c\), \(c\) a smooth Cartier conic |
| \(16\) | \(\mathbf P^2\) | \(H=\mathcal O_{\mathbf P^2}(4)\), \(c\) a line |

These are **necessary candidates only**. One must still produce an admissible projection, verify full inverse support, and solve conductor descent. Non-Cartier lifts, multiple inverse branches and other carriers lie outside this classification.

**Source:** [R-0002](../results/cartier_singleton_lift.md), [proof](../supplements/FIXED_CARRIER_DESCENT_AND_CARTIER_MODELS.md), and [independent audit](../supplements/QUADRATIC_ROOT_AND_BLOWUP_INCIDENCE.md).

## 5. Projection phases: reducing a family without solving it

R-0004 considers finite-type families of projections of such normalizations, subject to basepoint-freeness, finite birationality and full inverse support. After stratification and a finite cover, the conductor data define a phase morphism into a torus. A carrier admits a mate precisely when its phase is torsion. Laurent's theorem constrains the torsion points to a finite torsion-coset envelope.

This does **not** calculate the phase image for the three candidate normalizations, nor imply that an admissible torsion phase exists. Nilpotent conductor constraints and excluded parameter boundaries remain part of the problem.

The [explicit plane-normalization family in R-0017](../supplements/PROJECTION_SUPPORT_AND_DIFFERENTIAL_OBSTRUCTIONS.md) is an instructive counterweight: it has finite birational maps and the correct full singleton inverse support, but a first-order conductor obstruction prevents a mate in every degree **for that family**. Thus correct inverse support is not sufficient for descent, and the example does not exclude all degree-sixteen plane projections.

**Sources:** [R-0004](../results/projection_phase_reduction.md), [R-0017](../results/singleton_plane_conductor_descent.md).

## 6. Normal carriers: local Cartier indices and socle compatibility

A separate restriction arises when \(X\) is **normal** and a mate cuts a multiple \(nC\) on it. At a point \(P\in C\), let \(r\) be the actual local Cartier index of \(C\) on \(X\), with \(n=kr\). The local power/socle identity of R-0034 reads
\[
D_{n,P}=(k-1)A_{F,P}+kD_{r,P},
\qquad
2\sum_i\operatorname{length}(T_i)_P=nD_{n,P},
\]
under its curvilinear complete-intersection and filtration hypotheses. Here the \(T_i\) are torsion in the ordinary conormal-power layers. The **actual Cartier index is not surface multiplicity**; substituting one for the other invalidates the argument.

For \(C_0\), R-0035 combines these constraints with the normal-carrier torsion reduction, the low-degree carrier exclusion and the inherited P-010 quadratic-direction obstruction. The result excludes normal integral carriers with a mate **when every on-curve local Cartier index is at most four**. Indices six, twelve and higher are not excluded by this theorem, and the result says nothing about nonnormal carriers.

The inherited P-010 calculation comes from the two embedded charts of \(C_0\), not merely abstract splitting of its conormal bundle. Its finite-direction class is
\[
h_\theta=3\theta^3z^{-5}-\frac32\theta^2z^{-4}
+\frac34\theta z^{-3}-\frac38z^{-2}\in H^1(\mathcal O(-7)),
\]
and the remaining direction gives \(3z^{-5}\). Both are nonzero in characteristic zero. The index/socle audit treats these coefficients as **previously accepted inputs**, not as a fresh verification.

**Sources:** [R-0034](../results/normal_carrier_index_socle.md), [R-0035](../results/normal_carrier_bounded_index_exclusion.md), [normal-carrier torsion proof](../supplements/NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-normal-carrier-torsion), [index/socle independent audit](../supplements/NORMAL_CARRIER_SYMBOLIC_TORSION.md#2026-10-14-generalization-index12-filtered-compatibility), and [historical P-010 derivation](../RESEARCH_RECORD.md).

## 7. The remaining carrier problem

The preceding arguments do not show that \(C_0\) is not a set-theoretic complete intersection. They leave, among other things, higher-degree integral carriers; nonnormal carriers outside the quartic classification; normal carriers with larger local indices; and Cartier singleton projection families whose admissible conductor phases are not determined.

The natural research order is: understand the possible inverse support and divisor class on the normalization; compute the **full** conductor descent obstruction; then test whether a mate can exist. This avoids treating a successful normalization model, a numerical relation, or a reduced phase calculation as an actual STCI construction.

The [quartic-carrier technical appendix](QUARTIC_CARRIER_TECHNICAL_PROOFS.md) now preserves the genus-one exact algebra, nonendpoint all-length inequality, and endpoint ADE/doubled-horizontal budget in a compact permanent home. It identifies source calculations still requiring retention.


The shared algebra belongs to [full conductor membership and power descent](../supplements/CONDUCTOR_DESCENT_ALGEBRA.md), and the exact pointwise bridge to [conductor, differential and actual socle](../supplements/CONDUCTOR_JACOBIAN_AND_SOCLE.md). The former starts with a proposed section and tests descent; the latter starts with an actual supported pair and computes its socle divisor. Their hypotheses and logical directions are different. The [twisted-cubic benchmark and pinching control](../supplements/TORSION_CONSTRUCTIONS_AND_PINCHING_LIMITS.md) keep constructive torsion visible without claiming an actual quartic carrier.

The full fixed-carrier criterion is characteristic independent. The minimal-degree classification, nilpotent logarithmic rigidity and all-positive-degree plane differential exclusion above have their stated characteristic-zero scope; Frobenius can remove finite nilpotent defects in characteristic p. For this fixed embedded quartic, [every positive characteristic has a quartic-carrier construction](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier).

## 8. Proof preservation and consolidation decisions

This section is a **claim-level editorial disposition**, not permission to delete the supporting source files. The permanent exposition now contains the theorem statement, shared reductions, and decisive mechanism of each lane. What follows identifies the material that remains mathematically necessary for reconstructing those proofs.

| Claim / proof component | What this chapter now preserves | What still requires an exact technical proof | Disposition |
|---|---|---|---|
| Shared nonnormal reductions | Generic regularity, rationality, full inverse support | Ruled intersection with infinitely near multiplicities; purity and normalization-fiber arguments | Retain source as technical proof |
| Normal quartic exclusion | Scope and global exceptional-cycle strategy | Reduced and nonreduced graph enumerations, necessary-superset argument, final exceptional passage | Retain both audit/proof sources |
| Genus zero | Vanishing, six sections, minimal-degree classification, singular cone class-group argument | All-scroll and Veronese universal exclusions; cone exceptional correction | Retain technical proofs |
| Genus one | ADE degree-four del Pezzo, forced projection center, Cartier ribbon, five partitions | Entire-conductor algebra, complete ribbon net, universal ideals for [4], [3,1], [2,2], direction boundaries | Retain complete proof and exact validation |
| Genus two shared | Adjoint pencil, two numerical strata, actual ADE strict transform | Null-curve classification, full conductor algebra, normality and correction lemmas | Retain upstream proofs |
| Genus-two bisection | Full ribbon and global conormal-map contradiction | Cartier-double and nilideal derivation; independent normal-bundle calculation | Retain exact proof |
| Genus-two nonendpoint | All effective decompositions and all-length exceptional-chain contradiction | Complete divisor case split, chain equations and contact inequalities | Retain exact proof |
| Genus-two endpoint | Four coefficient regimes and complete ADE/doubled-horizontal exhaustion | Quartic ideal identity, local A/D correction equations, doubled-horizontal arbitrary-root argument | Retain exact proof |
| Final degree bound | Coprime factor reduction, quadric class, independent cubic exclusion | Primary cubic source and no-circularity evidence | Retain proof audit |

### Where the detailed mathematics should live

A **permanent proof section** is appropriate for arguments whose content is concise and structurally central: the normalization divisor-degree calculation; the factor reduction; the genus-two numerical dichotomy; and the global bisection conormal contradiction. These can be expanded and checked directly in this chapter without reproducing whole historical sessions.

A **technical appendix** is appropriate for long but reusable computations: the genus-one universal ideal and conductor certificates, normal-quartic exceptional graphs, nonendpoint all-length chain solutions, and endpoint ADE/doubled-horizontal calculations. Such an appendix should preserve exact formulas, hypotheses, and independently checked computational evidence, not merely a PASS label.

An **audit/evidence record** remains appropriate for independent replays, failed scripts, corrections, primary-source verification, and the assembly audit's attribution. These are evidence about the proof rather than the mathematical exposition itself. They should remain reachable from the permanent proof or appendix; a passing bounded computation is not a substitute for the universal argument.

### What is and is not redundant

The [quartic-carrier dependency graph](../synthesis/quartic_carrier_proof.md) and the six-lane table in Section 3 overlap in *orientation*, but the graph still provides a compact dependency map. They are candidates for eventual navigation consolidation, **not** proof deletion.

The older [irreducible-residual endpoint note](QUARTIC_CARRIER_TECHNICAL_PROOFS.md#endpoint-irreducible-graph-extracted-geometric-argument) is mathematically narrower than the full endpoint reduction: it cannot be used as an exhaustive proof. Its unique calculations should be checked against the full reduction before it is considered redundant. Likewise, the [earlier bisection quadratic-descent note](../supplements/GENUS_TWO_BISECTION_DESCENT.md) provides a weaker conductor route; its conditional content is not automatically disposable because the global conormal contradiction is stronger.

**No deletion decision is justified solely by a newer theorem's stronger conclusion.** The criterion is whether a historical source contains a unique valid argument, counterexample, hypothesis check, computation, or useful failure explanation absent from the retained permanent material.

### Immediate proof-integration order

First, write the short intrinsic arguments directly into the chapter and check their hypotheses. Second, prepare one quartic-carrier technical appendix organized by the six lanes, with links to original exact proofs. Third, compare each historical source against the appendix claim by claim and record any genuinely unique content. Only then consider retiring duplicated narrative files; preserve the R-0001 theorem and independent audits throughout.

## Editorial and verification status

**Critical review, pass 1:** checked all 16 relative Markdown links against the complete working-branch Git tree: all resolve. Corrected a material overgeneralization in Section 1: the coefficient of the singleton lift in the pulled-back mate divisor is \(n=b\deg X/\deg C\), and equals the mate degree only for quartic carriers of the degree-four curve. Also made explicit why a proper STCI pair has no common surface component. The rest of the chapter has been compared at the statement/scope level with R-0001, R-0002, R-0003, R-0004, R-0017, R-0034 and R-0035; this is **not** an independent audit of the original proofs.

This is the **first permanent-chapter draft**. It integrates accepted statements and the geometric reasons for their scope, while linking rather than duplicating long source proofs. It has not been independently proof-audited; it is **not yet a replacement for result records or their underlying evidence**. Before retiring historical files, each six-lane proof and each conductor/index lemma must be compared for unique content, and the chapter's references and hypotheses checked line by line.

## 9. Generic nonimmersion and four MF6 boundary carriers

The generic nonimmersion-prime lemma in [the original proof](../supplements/OCT8_MF6_NORMALIZATION_AND_PRINCIPAL_BOUNDARIES.md#source-2026-10-08-session-nonimmersion-prime-independent-auditmd) applies to a finite birational map from a smooth projective surface, a smooth lifted divisor c linearly equivalent to the pullback polarization H, an immersion on c, and a mate pullback equal to a nonzero scalar times the nth power of the defining section of c, with n nonzero in the ground field. Every distinct integral curve E with positive H-intersection must be generically immersive. The proof uses vanishing derivative minors along E, a unit-pivot kernel vector, and cancellation of the nonzero section in the local domain of E *before* evaluating at a point of E intersect c. It does not apply when the characteristic divides n or to isolated rank-drop points.

The [four explicit nonnormal MF6 boundary carriers](../supplements/OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-nonnormal-mf6-independent-auditmd) are excluded in every mate degree in characteristic zero. Their affine finite normalization has a unique reduced lifted quartic and a duplicated fiber whose two points impose a root-of-unity equation on any descending mate power. The relevant quadratic parameter has norm 1/3, contradicting that equation. This is a fixed-carrier statement about four specified quartics, not a general nonnormal exclusion or an exclusion of all pencil members.

The [ordinary pinch and nodal conductor analysis](../supplements/OCT7_MF6_AND_NONNORMAL_STRUCTURES.md#source-2026-10-07-session-nonnormal-structural-progressmd) proves transversality for an immersed lifted curve at an ordinary pinch. Under explicit ordinary-singularity assumptions this yields a four-versus-six scroll conductor count and a six-point Roman Veronese no-conic obstruction. A separate nodal-conductor local model admits smooth embedded image curves of arbitrarily high conductor contact, so reduced branch counts cannot be used without the ordinary hypotheses.

These arguments are incorporated as source-preservation statements, not independently certified new theorems. The Veronese Jordan classification and Mumford numerical-pullback proof still need detailed integration.

## 10. Numerical self-intersection versus normal degree

The [numerical pullback proof](../synthesis/numerical_surface_pullback.md) establishes the exact nonnegative difference between the normal degree and numerical self-intersection for an integral carrier regular generically along the smooth curve. Its conormal identification and exceptional-matrix argument have been independently reviewed. The split-sextic application retains its separate numerical antecedents, and the identically-zero polynomial branch remains separate.

## Exact genus-two trisecant carrier linear system

For the fixed rational quartic on `Q=(x0*x3-x1*x2=0)`, every trisecant line lies in the ruling meeting C in length three. It is `Gamma_a=(x2-a*x0,x3-a*x1)` for finite `a`, or `Gamma_infinity=(x0,x1)`. The intersection divisor on C is `t^3-a*s^3`; over an algebraically closed characteristic-zero field, the two ambient types are three distinct contacts (`a!=0,infinity`) and a triple contact (`a=0,infinity`). Over a nonclosed field, diagonal scaling may not identify nonzero parameters without cube roots.

Put `z=x2-a*x0`, `w=x3-a*x1`, `q=x0*x3-x1*x2`, `A=x0^2*x2-x1^3`, `B=x0*x2^2-x1^2*x3`, `D=x2^3-x1*x3^2`, and `T_a=D-2*a*B+a^2*A`. The exact homogeneous ideal of forms containing C and double along Gamma is `I(C) intersect (z,w)^2=(q*z,q*w,T_a)`. Its quartic space is `F=q*Q2+T_a*L0`, where `Q2` is quadratic in `(z,w)` and `L0` is an ambient linear form; dimensions are 7+4=11. On Q, `div(F|Q)=C+2*Gamma+(Q intersect (L0=0))`. The residual conic may degenerate and must not be discarded. These ideal and dimension statements are unconditional within the fixed-curve setup; see [the source proof](../supplements/GENUS_TWO_TRISECANT_CARRIER_PROOF.md).

The source's subsequent discriminant and correction-cycle exclusion requires the **actual normal ambient-line-blowup realization** and conductor identification; it is not a free-standing proof from the ideal calculation. In the three-contact case the discriminant at each `r^3=1` is a square; requiring vanishing at all contacts gives `a0=2*c1`, `a1=-b0`, `b1=2*c0`, and then `Delta=4*(v^3-u^3)*((c0^2+b0*c1)*v+(b0*c0-c1^2)*u)`. The nonzero-discriminant graph argument is conditional on that realization and does not address the identically-zero discriminant or endpoint line within this source. Later audited genus-two exclusions belong to the complete carrier theorem; do not confuse this conditional historical argument with their proof status.
