# Carrier and conductor geometry

**Mathematical consolidation draft — not a new proof or a change in theorem status.** Characteristic zero unless explicitly indicated. This chapter collects the geometry of a surface containing a curve and the obstruction to cutting out precisely that curve with one more equation. Canonical authority remains in the R-records and their proof/audit sources. In particular, the case-by-case quartic theorem is **outlined**, not independently reproved here.

## 1. From a set-theoretic complete intersection to a divisor on a surface

Fix
\[
C=C_0=\{[s^4:s^3t:st^3:t^4]\}\subset\mathbf P^3.
\]
Suppose homogeneous forms \(F,G\) have \(\sqrt{(F,G)}=I_C\). Choosing an **integral** component \(X=V(F_0)\) of \(V(F)\) containing \(C\), the restriction of \(G\) cuts out \(C\) set-theoretically on \(X\), provided \(G\) is not identically zero on \(X\). Because \(V(F,G)\) has pure curve support, \(F\) and \(G\) cannot share a surface component. Thus integral *carriers* are a natural intermediate problem. This reduction does not mean \(F\) itself is irreducible, or that every useful carrier is normal.

Let \(\nu:S\to X\) be the finite normalization, and let \(H=\nu^*\mathcal O_X(1)\). If \(G\) has degree \(b\), its pullback is a section of \(\mathcal O_S(bH)\). Its **entire zero support** is \(\nu^{-1}(C)\), not merely the preferred component mapping birationally to \(C\). This is the first crucial distinction: additional inverse branches and isolated inverse points matter.

When the full reduced inverse support is a single curve \(c\) mapping isomorphically to \(C\), the zero divisor is \(nc\) for some positive integer \(n\), so
\[
nc\sim bH.
\]
Intersecting with \(H\) gives \(n\deg C=b\deg X\), since \(H\cdot c=\deg C\) and \(H^2=\deg X\). Thus \(n=b\) **for a quartic carrier of this quartic curve**, but not for an arbitrary-degree carrier. On a singular normal surface \(c\) need not itself be Cartier; only the relevant multiple is necessarily Cartier. See R-0001 and its [independent assembly audit](../notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md).

The conceptual question is therefore twofold: **can the inverse-support divisor have the required polarization class upstairs, and can its defining section descend through the conductor downstairs?** Neither condition alone suffices.

## 2. The normalization is not the original carrier

The normalization \(S\) remembers divisors and intersection theory more transparently than \(X\), but it can lose gluing conditions. Let \(\mathfrak c\) denote the conductor ideal of \(\mathcal O_X\subset\nu_*\mathcal O_S\). A section upstairs may have the correct zero support and still fail to be a section downstairs because its values or infinitesimal jets disagree across the conductor.

At a generic conductor point, this discrepancy is measured by the **full** unit quotient \(B_\eta^\times/A_\eta^\times\) for the finite local conductor algebra \(A_\eta\subset B_\eta\). Passing to reduced conductor points can discard nilpotent unit obstructions. In characteristic zero the logarithm identifies the nilpotent contribution with additive data, which need not be torsion. Consequently, a torsion condition on the reduced phase does not settle descent.

The fixed-carrier theorem R-0003 packages this as a lattice. If the reduced inverse image consists of curves \(\Gamma_1,\ldots,\Gamma_s\), form
\[
\Lambda=\ker\left(\mathbf Z^{s+1}\longrightarrow\mathrm{Cl}(S)\right),\quad
(n_1,\ldots,n_s,d)\mapsto\sum_jn_j[\Gamma_j]-d[H].
\]
The subgroup \(\Lambda_{\rm desc}\) imposes the generic full-conductor unit conditions modulo torsion. Subject to the theorem's exact hypotheses (integral Cohen–Macaulay carrier, finite normalization, no extraneous isolated inverse points), **a mate on this fixed carrier exists exactly when** \(\Lambda_{\rm desc}\) contains a vector positive on every inverse branch. A suitable power clears torsion and forces conductor membership along the target curve. This is a structural criterion, not an algorithm for arbitrary carriers.

**Source:** [R-0003](../results/fixed_carrier_conductor_criterion.md) and [proof with embedded independent reviews](../notes/2026-10-13-generalization-conductor-theorem.md). Its statement is valid in arbitrary characteristic; the characteristic-zero nilpotent logarithm is a tool for analyzing its phases, not a restriction on the entire fixed-carrier criterion.

## 3. The complete exclusion of integral quartic carriers

The accepted theorem R-0001 says that **no integral quartic surface** containing the fixed \(C_0\) has a set-theoretic mate of any positive degree, in characteristic zero. It does not exclude all higher-degree carriers.

Why is the case analysis finite? A normal integral quartic has its own global exclusion argument. For a nonnormal integral quartic, the arithmetic genus of a general plane section is \(3\), while the genus \(\pi\) of the corresponding normalized section belongs to \(\{0,1,2\}\). The independent assembly audit also proves that the normalization is rational, that generic regularity along \(C\) is automatic, and that the mate would have full inverse support. These facts must not be silently assumed.

The six proof lanes are:

| Surface type | Geometric mechanism |
|---|---|
| Normal integral quartic | Normal-carrier global argument, retaining nonreduced exceptional cycles |
| Nonnormal, \(\pi=0\) | Rational minimal-degree normalization: scroll, Veronese or cone; conductor constraints |
| Nonnormal, \(\pi=1\) | Degree-four ADE del Pezzo normalization; anticanonical projection, Cartier double and ribbon contact partitions |
| Nonnormal, \(\pi=2,\lambda=0\) | Bisection, second-pencil and Cartier-double/ribbon incompatibility |
| Nonnormal, \(\pi=2,\lambda=1\), nonendpoint | Trisecant with distinct contacts; exhaustive conductor decompositions and exceptional chains |
| Nonnormal, \(\pi=2,\lambda=1\), endpoint | Triple contact; exhaustive quartic family, ADE corrections and doubled-horizontal strata |

The last two rows cannot be combined by appealing to a generic trisecant. In particular, an argument that excludes only an irreducible residual conic does **not** exhaust the endpoint family. Similarly, the genus-one projection center is derived from the complete anticanonical model and restriction to the lifted curve, not assumed from a chosen example.

For exact dependencies and links to the six independently reviewed proofs, use the [quartic-carrier dependency graph](../MATHEMATICAL_CONSOLIDATION_QUARTIC_CARRIER_DEPENDENCIES.md), the [accepted assembly](../notes/2026-10-11-session-all-quartic-results-acceptance.md), and the [independent coverage audit](../notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md). This section is a **proof guide**; the six source proofs remain necessary until their arguments have been integrated and checked in full.

A hypothetical STCI presentation of \(C_0\) therefore cannot use a quartic carrier. Combined with the separate lower-degree exclusions, this forces both defining degrees to be at least five. This is a degree bound, not a global nonexistence theorem.

### 3.1 Genus-zero mechanism: vanishing, classification, cone

On a resolution M of the normalization S, write L for the pullback of H. In the sectional-genus-zero case, L is nef and big with L squared equal to 4, and K_M.L=-6. The divisor K_M+L has negative intersection with L and no sections. Kawamata-Viehweg vanishing and Riemann-Roch give chi(O_M)=1. A general normalized hyperplane section Y is P1, and the restriction sequence for H yields h0(S,H)=6. Thus the complete system maps S finitely and birationally to a degree-four minimal-degree surface in P5. The possibilities include scrolls, the Veronese surface and the singular rational-normal quartic cone.

The cone needs its own argument. On its F4 resolution, the hyperplane class is E+4f, with E squared -4. Its class group is Z[f] and [H]=4[f]. For a mate, the quartic-specific relation b(c-H)~0 forces c~H and makes c Cartier. The smooth curve c cannot pass through the cone vertex, whose local ring is singular. The remaining case is covered by the scroll/conductor exclusion. Exceptional corrections on the resolution must be retained; they cannot be dropped simply because c is smooth.

Sources: [genus-zero audit](../notes/2026-10-09-session-normalization-genus-zero-independent-audit.md) and [nonrational-normalization audit](../notes/2026-10-09-session-nonrational-normalization-independent-audit.md).

### 3.2 Genus-one mechanism: intrinsic projection, ribbon, partitions

The normalization is rational by the ruled-surface argument retaining infinitely near multiplicities. Its minimal resolution is a weak degree-four del Pezzo surface; the normal anticanonical model is an ADE two-quadric intersection in P4. Restricting the complete anticanonical sections to the lifted curve determines the projection center: it deletes the middle s²t² coordinate of the rational normal quartic. This is deduced for every carrier in this lane, not assumed from a special family.

An actual Cartier divisor 2c on the normalization defines a Cohen-Macaulay ribbon, including at ADE points where c need not be Cartier. Its nilideal and the entire nonreduced conductor enter the mate obstruction. Replacing this double by the ordinary square of the curve ideal would be incorrect.

The remaining derivative is a binary quartic. Its five multiplicity partitions are [1,1,1,1], [2,1,1], [2,2], [3,1], and [4]. The first two are excluded by the derivative and ribbon-net argument. The remaining three require the complete repeated-partition calculations, including invisible quadric coefficients and boundary directions. The independent Macaulay2 audit records 29 successful checks; earlier failed scaffolding runs are not passing certificates.

Sources: [genus-one interface audit](../notes/2026-10-10-session-genus-one-interface-independent-audit.md) and [repeated-partition audit](../notes/2026-10-10-session-ribbon-repeated-partitions-independent-audit.md).

## 4. Cartier singleton lifts: a necessary classification, not a construction

Under the stronger hypotheses that the entire reduced inverse image is a single curve \(c\cong C\) and **\(c\) is Cartier on the normalization**, R-0002 classifies the possible normalization/polarization pairs. The mate makes \(c\) ample, and \(|c|\) realizes a normal surface of minimal degree. The proof uses the Cartier restriction sequence, surface classification and the singular cone case.

For the fixed quartic \(C_0\), after excluding quartic carriers, three necessary higher-degree models remain:

| Carrier degree | Normalization | Polarization and lift |
|---|---|---|
| \(8\) | \(\mathbf P^1\times\mathbf P^1\) | \(H=(2,2)\), \(c=(1,1)\) |
| \(8\) | Quadric cone | \(H=2c\), \(c\) a smooth Cartier conic |
| \(16\) | \(\mathbf P^2\) | \(H=\mathcal O_{\mathbf P^2}(4)\), \(c\) a line |

These are **necessary candidates only**. One must still produce an admissible projection, verify full inverse support, and solve conductor descent. Non-Cartier lifts, multiple inverse branches and other carriers lie outside this classification.

**Source:** [R-0002](../results/cartier_singleton_lift.md), [proof](../notes/2026-10-14-generalization-cartier-lift-minimal-degree.md), and [independent audit](../notes/2026-10-14-generalization-cartier-lift-independent-audit.md).

## 5. Projection phases: reducing a family without solving it

R-0004 considers finite-type families of projections of such normalizations, subject to basepoint-freeness, finite birationality and full inverse support. After stratification and a finite cover, the conductor data define a phase morphism into a torus. A carrier admits a mate precisely when its phase is torsion. Laurent's theorem constrains the torsion points to a finite torsion-coset envelope.

This does **not** calculate the phase image for the three candidate normalizations, nor imply that an admissible torsion phase exists. Nilpotent conductor constraints and excluded parameter boundaries remain part of the problem.

The explicit plane-normalization family in R-0017 is an instructive counterweight: it has finite birational maps and the correct full singleton inverse support, but a first-order conductor obstruction prevents a mate in every degree **for that family**. Thus correct inverse support is not sufficient for descent, and the example does not exclude all degree-sixteen plane projections.

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

**Sources:** [R-0034](../results/normal_carrier_index_socle.md), [R-0035](../results/normal_carrier_bounded_index_exclusion.md), [normal-carrier torsion proof](../notes/2026-10-14-generalization-normal-carrier-torsion.md), [index/socle independent audit](../notes/2026-10-14-generalization-index12-filtered-compatibility.md), and [historical P-010 derivation](../RESEARCH_RECORD.md).

## 7. The remaining carrier problem

The preceding arguments do not show that \(C_0\) is not a set-theoretic complete intersection. They leave, among other things, higher-degree integral carriers; nonnormal carriers outside the quartic classification; normal carriers with larger local indices; and Cartier singleton projection families whose admissible conductor phases are not determined.

The natural research order is: understand the possible inverse support and divisor class on the normalization; compute the **full** conductor descent obstruction; then test whether a mate can exist. This avoids treating a successful normalization model, a numerical relation, or a reduced phase calculation as an actual STCI construction.

## Editorial and verification status

**Critical review, pass 1:** checked all 16 relative Markdown links against the complete working-branch Git tree: all resolve. Corrected a material overgeneralization in Section 1: the coefficient of the singleton lift in the pulled-back mate divisor is \(n=b\deg X/\deg C\), and equals the mate degree only for quartic carriers of the degree-four curve. Also made explicit why a proper STCI pair has no common surface component. The rest of the chapter has been compared at the statement/scope level with R-0001, R-0002, R-0003, R-0004, R-0017, R-0034 and R-0035; this is **not** an independent audit of the original proofs.

This is the **first permanent-chapter draft**. It integrates accepted statements and the geometric reasons for their scope, while linking rather than duplicating long source proofs. It has not been independently proof-audited; it is **not yet a replacement for canonical R-records or their underlying evidence**. Before retiring historical files, each six-lane proof and each conductor/index lemma must be compared for unique content, and the chapter's references and hypotheses checked line by line.
