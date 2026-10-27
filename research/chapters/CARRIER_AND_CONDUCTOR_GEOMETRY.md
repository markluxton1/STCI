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

### 1.1 Reduction to integral factors and the lower-degree bound

For a genuine set-theoretic presentation \(V(F,G)=C\), the two forms are coprime: a common irreducible factor would contribute a surface to their intersection. Let \(f\) be any irreducible factor of \(F\). Then \(f\) and \(G\) are coprime, so \(V(f,G)\) is a nonempty projective complete intersection of pure dimension one. Its support is contained in the irreducible curve \(C\), hence is exactly \(C\). Thus **every irreducible factor of either defining equation is itself an integral carrier with a mate**; multiplicities of factors do not alter the support argument.

For the fixed curve, linear carriers are impossible because \(C\) is nonplanar. Its unique quadric \(Q\) is smooth, with \(C\) of bidegree \((1,3)\); an ambient equation of degree \(b\) restricts to \((b,b)\), which cannot equal a positive multiple of \((1,3)\). Integral cubic carriers are excluded by the separately verified classical theorem, and integral quartic carriers by R-0001. Therefore **each irreducible factor** of \(F\) and \(G\) has degree at least five, and in particular \(\deg F,\deg G\ge5\). This conclusion does not assume the defining equations are irreducible and does not establish that any higher-degree presentation exists. See the [degree-factor audit](../notes/2026-10-11-session-degree-factor-and-mf6-scope-audit.md).

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

The full factor reduction and the resulting degree bound are proved in Section 1.1; the quartic-carrier theorem is its deepest input.

### 3.0 Shared reductions and the normal case

The assembly audit proves three prerequisites before splitting the nonnormal cases: generic regularity of every integral quartic along the fixed curve, rationality of every nonnormal quartic normalization, and full inverse support of a hypothetical mate. The rationality argument uses the ruled-surface intersection identity with **all infinitely near multiplicities**; it does not rely on the existence of a mate. Full inverse support uses purity of the pulled-back Cartier divisor and rules out isolated normalization points above C.

For a **normal integral quartic**, the proof is a separate global surface argument, not an instance of the normalized sectional-genus-zero, -one or -two classification. Its inherited inputs include normal-quartic classification, rational-singularity and ADE-pair results, actual normal-sheaf bounds, and necessary exceptional-graph enumerations for both reduced and nonreduced cycles. The enumerations eliminate a necessary superset; they do not assert realization of each graph. The final exceptional-passage argument is geometric. The independent assembly audit checks that the required small-degree exclusions were proved independently and do not invoke the quartic-carrier theorem being assembled.

Sources: [normal global audit](../notes/2026-10-07-session-normal-global-adversarial.md), [nonreduced-cycle audit](../notes/2026-10-07-session-normal-nonreduced-independent-audit.md), and [assembly audit](../notes/2026-10-11-session-all-quartic-dependency-assembly-independent-audit.md).

### 3.1 Genus-zero mechanism: vanishing, classification, cone

On a resolution M of the normalization S, write L for the pullback of H. In the sectional-genus-zero case, L is nef and big with L squared equal to 4, and K_M.L=-6. The divisor K_M+L has negative intersection with L and no sections. Kawamata-Viehweg vanishing and Riemann-Roch give chi(O_M)=1. A general normalized hyperplane section Y is P1, and the restriction sequence for H yields h0(S,H)=6. Thus the complete system maps S finitely and birationally to a degree-four minimal-degree surface in P5. The possibilities include scrolls, the Veronese surface and the singular rational-normal quartic cone.

The cone needs its own argument. On its F4 resolution, the hyperplane class is E+4f, with E squared -4. Its class group is Z[f] and [H]=4[f]. For a mate, the quartic-specific relation b(c-H)~0 forces c~H and makes c Cartier. The smooth curve c cannot pass through the cone vertex, whose local ring is singular. The remaining case is covered by the scroll/conductor exclusion. Exceptional corrections on the resolution must be retained; they cannot be dropped simply because c is smooth.

Sources: [genus-zero audit](../notes/2026-10-09-session-normalization-genus-zero-independent-audit.md) and [nonrational-normalization audit](../notes/2026-10-09-session-nonrational-normalization-independent-audit.md).

### 3.2 Genus-one mechanism: intrinsic projection, ribbon, partitions

The normalization is rational by the ruled-surface argument retaining infinitely near multiplicities. Its minimal resolution is a weak degree-four del Pezzo surface; the normal anticanonical model is an ADE two-quadric intersection in P4. Restricting the complete anticanonical sections to the lifted curve determines the projection center: it deletes the middle s²t² coordinate of the rational normal quartic. This is deduced for every carrier in this lane, not assumed from a special family.

An actual Cartier divisor 2c on the normalization defines a Cohen-Macaulay ribbon, including at ADE points where c need not be Cartier. Its nilideal and the entire nonreduced conductor enter the mate obstruction. Replacing this double by the ordinary square of the curve ideal would be incorrect.

The remaining derivative is a binary quartic. Its five multiplicity partitions are [1,1,1,1], [2,1,1], [2,2], [3,1], and [4]. The first two are excluded by the derivative and ribbon-net argument. The remaining three require the complete repeated-partition calculations, including invisible quadric coefficients and boundary directions. The independent Macaulay2 audit records 29 successful checks; earlier failed scaffolding runs are not passing certificates.

Sources: [genus-one interface audit](../notes/2026-10-10-session-genus-one-interface-independent-audit.md) and [repeated-partition audit](../notes/2026-10-10-session-ribbon-repeated-partitions-independent-audit.md).

### 3.2a Shared genus-two geometry and exhaustion

On the minimal resolution M of a genus-two normalization, the adjoint divisor f=K_M+L is a connected basepoint-free conic pencil. The actual exceptional correction Z satisfies q=-Z²>0, lambda=K_M.Z a nonnegative integer, q+lambda=4 and lambda²<=q. These force exactly two possibilities: (lambda,q)=(0,4) and (1,3). The bisection and trisecant cases are therefore exhaustive; an older assumption that q always equals four would miss the latter.

In the trisecant case the conductor line lies in the degree-three ruling of the unique smooth quadric containing C. Its intersection with C is described by a cubic with either three distinct roots or a triple endpoint root; the opposite endpoint is obtained by reversal. The normal ADE model is the strict transform in the blowup of the conductor line; **it is not the potentially non-Gorenstein normalization S**. The actual conductor retains split, singular and nonreduced covers. These are shared prerequisites, not additional unexamined case assumptions.

Sources: [genus-two adjoint audit](../notes/2026-10-09-session-genus-two-adjoint-independent-audit.md), [null-curve and correction audit](../notes/2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md), [entire-conductor audit](../notes/2026-10-10-session-genus-two-entire-conductor-independent-audit.md), and [normal strict-transform audit](../notes/2026-10-10-session-genus-two-blowup-lift-normality-independent-audit.md).

### 3.3 Genus-two bisection: a global conormal contradiction

The genus-two normalization admits a second-pencil reduction, with bisection case denoted lambda=0 in the source. Under a hypothetical mate, the accepted conductor geometry produces an **actual Cartier double** R_C supported on the smooth lifted curve c. Its Cohen-Macaulay purity makes the nilideal J square-zero globally, not merely generically, and the source calculates J=O_C(-8). This is a genuine ribbon on the normalization, including its singular points.

The morphism from this ribbon to P3 induces a global conormal map N*_(C/P3) -> J. It is nonzero: away from the conductor line the normalization is an isomorphism, so the embedded ribbon generates its nilideal from the ambient curve ideal. For the fixed C in characteristic zero, N*_(C/P3)=O(-7) direct sum O(-7). Hence Hom(N*,O(-8))=0. Contradiction. This **global** argument excludes the whole bisection lane; the older quadratic-conductor chain remains a valid but weaker conditional analysis.

Source: [bisection independent proof and audit](../notes/2026-10-10-session-genus-two-bisection-full-independent-audit.md).

### 3.4 Nonendpoint trisecant: support and exceptional chains

In the lambda=1 trisecant stratum, the lifted curve is a section of the second ruling. A hypothetical mate forces **singleton inverse support at every conductor contact**: all points in the normalization fiber above a point of C must lie on the single lifted curve. On the normal conic model the exceptional divisor has bidegree (2,2); a distinguished horizontal component B has class (1,0). The audit exhausts multiplicity two on B, multiplicity one with reducible residual, and multiplicity one with integral residual.

In the integral residual case the residual has class (1,2), is a smooth rational graph over the ruling, and meets B in two transverse points. Exceptional corrections are then controlled by ADE chains at the contacts. The exact chain solution, with arbitrary chain lengths and all contact positions, contradicts the required correction budget. This is a universal positivity/intersection contradiction, not a finite search through short chains. The proof's independent symbolic replay supplements rather than replaces that argument.

Sources: [nonendpoint independent audit](../notes/2026-10-10-session-genus-two-nonendpoint-trisecant-continuation-independent-audit.md) and [owner's conic obstruction](../notes/2026-10-10-session-genus-two-nonendpoint-trisecant-conic-obstruction.md).

### 3.5 Endpoint trisecant: the full quartic family matters

At the endpoint, the conductor contact is triple, and the nonendpoint transversality argument cannot simply be reused. The owner first derives the **complete** quartic equation from the ideal identity I(C) intersect (x2,x3)^2=(q*x2,q*x3,D). Its exceptional polynomial is then exhausted by the four coefficient regimes c0 nonzero; a1 nonzero; a1=0 with b1 nonzero; and a1=b1=0 with c1 nonzero. The last regime includes doubled horizontal components, while the preceding regime includes triple residual contact and local A/D configurations.

The independent audit checks the coefficient-zero and doubled-component gaps, the two distinct residual intersections, triple-contact ADE corrections, and arbitrary ADE roots in the doubled-horizontal case. Each regime contradicts the mate correction identities. Reversal handles the opposite endpoint. A former argument restricted to irreducible residual curves was **not** an exhaustion proof and cannot stand in for these additional cases.

Sources: [full endpoint reduction](../notes/2026-10-10-session-genus-two-endpoint-full-quartic-reduction.md), [independent coverage audit](../notes/2026-10-10-session-genus-two-endpoint-full-independent-audit.md), [local ADE correction audit](../notes/2026-10-10-session-endpoint-local-ade-correction-audit.md), and [doubled-horizontal audit](../notes/2026-10-10-session-genus-two-endpoint-double-horizontal-independent-audit.md).

## 3.6 Two short proofs extracted from the genus-two sources

**Numerical dichotomy.** On the smooth rational resolution \(M\), let \(L\) be the pulled-back hyperplane class, \(c^\#\) the smooth strict transform of the curve, and \(Z\) the effective rational exceptional correction, so that \(c^\#\equiv L-Z\) and \(L\cdot Z=0\). The adjoint-pencil argument gives \(L^2=4\) and \(K_M\cdot L=-2\). Put
\[
q=-Z^2>0,\qquad \lambda=K_M\cdot Z\in\mathbf Z_{\ge0}.
\]
Negative definiteness of the exceptional lattice proves \(q>0\); the classification of its vertical and horizontal components gives \(\lambda\ge0\). Adjunction on \(c^\#\cong\mathbf P^1\) gives
\[
-2=(c^\#)^2+K_M\cdot c^\#
=(4-q)+(-2-\lambda),
\]
hence \(q+\lambda=4\). The exceptional intersection estimate gives \(\lambda^2\le q\). Consequently \(\lambda^2+\lambda\le4\), so \(\lambda=0\) or \(1\). The resulting pairs are \((0,4)\) and \((1,3)\). Moreover, for the conic pencil \(f=K_M+L\),
\[
f\cdot c^\#=2-\lambda,
\]
which is respectively a bisection or a section. The only inherited nontrivial inequality is the exceptional estimate \(\lambda^2\le q\); its proof and the classification of exceptional components remain in the [null-curve audit](../notes/2026-10-09-session-genus-two-nullcurve-mate-independent-audit.md).

**Bisection contradiction.** In the \(\lambda=0\) case, the second-pencil calculation yields the *linear*, not merely numerical, equivalence \(2c\sim2H\) on the normal surface \(S\). This is obtained by showing \(2Z\) integral in the exceptional lattice and using numerical-to-linear equivalence on the rational resolution. A section of \(\mathcal O_S(2H)\) therefore defines a Cartier double \(R_C\) with entire support \(c\). Since \(S\) is normal and hence Cohen–Macaulay, \(R_C\) is a pure Cohen–Macaulay curve of generic length two. Its nilradical \(J\) is generically square-zero; purity excludes a nonzero finite-support \(J^2\), so \(J^2=0\) everywhere. The same purity makes \(J\) torsion-free of rank one on the smooth rational \(c\), hence a line bundle.

The rational-resolution Riemann–Roch computation gives
\[
\chi(\mathcal O_S(mH))=1+2m^2+m.
\]
The Cartier sequence for \(R_C\) therefore gives
\[
\chi(\mathcal O_{R_C})=\chi(\mathcal O_S)-\chi(\mathcal O_S(-2H))
=1-7=-6.
\]
As \(\chi(\mathcal O_c)=1\), the reduction sequence gives \(\chi(J)=-7\), hence \(J\cong\mathcal O_{\mathbf P^1}(-8)\). The morphism \(R_C\to\mathbf P^3\) induces
\[
N^\vee_{C/\mathbf P^3}=I_C/I_C^2\longrightarrow J.
\]
This map is nonzero: off the conductor line the normalization is an isomorphism and the embedded double has nilideal generated by the ambient curve ideal. But the independently calculated splitting \(N^\vee_{C/\mathbf P^3}\cong\mathcal O(-7)^{\oplus2}\) gives
\[
\operatorname{Hom}\bigl(N^\vee_{C/\mathbf P^3},J\bigr)
=H^0(\mathcal O(-1))^{\oplus2}=0.
\]
This contradiction excludes the bisection stratum. It uses the entire Cartier double, not an assumed first infinitesimal neighborhood. The exact derivation of \(2c\sim2H\), the splitting calculation and the purity arguments are in the [independent bisection proof](../notes/2026-10-10-session-genus-two-bisection-full-independent-audit.md).

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

The [quartic-carrier dependency graph](../MATHEMATICAL_CONSOLIDATION_QUARTIC_CARRIER_DEPENDENCIES.md) and the six-lane table in Section 3 overlap in *orientation*, but the graph still provides a compact dependency map. They are candidates for eventual navigation consolidation, **not** proof deletion.

The older [irreducible-residual endpoint note](../notes/2026-10-10-session-genus-two-endpoint-irreducible-conic-obstruction.md) is mathematically narrower than the full endpoint reduction: it cannot be used as an exhaustive proof. Its unique calculations should be checked against the full reduction before it is considered redundant. Likewise, the [earlier bisection quadratic-descent note](../notes/2026-10-10-session-genus-two-bisection-quadratic-descent.md) provides a weaker conductor route; its conditional content is not automatically disposable because the global conormal contradiction is stronger.

**No deletion decision is justified solely by a newer theorem's stronger conclusion.** The criterion is whether a historical source contains a unique valid argument, counterexample, hypothesis check, computation, or useful failure explanation absent from the retained permanent material.

### Immediate proof-integration order

First, write the short intrinsic arguments directly into the chapter and check their hypotheses. Second, prepare one quartic-carrier technical appendix organized by the six lanes, with links to original exact proofs. Third, compare each historical source against the appendix claim by claim and record any genuinely unique content. Only then consider retiring duplicated narrative files; preserve the canonical R-0001 theorem and independent audits throughout.

## Editorial and verification status

**Critical review, pass 1:** checked all 16 relative Markdown links against the complete working-branch Git tree: all resolve. Corrected a material overgeneralization in Section 1: the coefficient of the singleton lift in the pulled-back mate divisor is \(n=b\deg X/\deg C\), and equals the mate degree only for quartic carriers of the degree-four curve. Also made explicit why a proper STCI pair has no common surface component. The rest of the chapter has been compared at the statement/scope level with R-0001, R-0002, R-0003, R-0004, R-0017, R-0034 and R-0035; this is **not** an independent audit of the original proofs.

This is the **first permanent-chapter draft**. It integrates accepted statements and the geometric reasons for their scope, while linking rather than duplicating long source proofs. It has not been independently proof-audited; it is **not yet a replacement for canonical R-records or their underlying evidence**. Before retiring historical files, each six-lane proof and each conductor/index lemma must be compared for unique content, and the chapter's references and hypotheses checked line by line.
