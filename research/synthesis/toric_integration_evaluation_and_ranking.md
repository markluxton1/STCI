# Evaluation of the Toric-Based Surface-Pair VGIT Branch Against `main` and Ranked Integration Roadmap

- **Author:** Gemini (explicitly authored by Gemini, not ChatGPT)
- **Branch / Worktree:** `evaluate_toric_integration_stci`
- **Date:** 2026-11-01
- **Status:** Comparative mathematical review and ranked execution plan; preserves canonical authority boundaries (`AGENTS.md`, `research/AUTHORITY.md`)

---

## 1. Executive Summary: `main` vs. `codex/vgit-surface-pairs-torus-2026-11-01`

### 1.1 State of `main` (`06f7693`)
Prior to `codex/vgit-surface-pairs-torus-2026-11-01`, `main` already integrated the initial torus-degeneration reassessment (`7a04ea7`), establishing:
- **Curve stabilizer:** The connected projective stabilizer of $C_0 = \{[s^4:s^3t:st^3:t^4]\} \subset \mathbf P^3$ in $\operatorname{PGL}_4$ has dimension $1$, given by the diagonal $\mathbf G_m$-action
  $$t \cdot [x_0:x_1:x_2:x_3] = [x_0 : t x_1 : t^3 x_2 : t^4 x_3] \quad \text{(centered weights } (-2,-1,1,2) \text{ on } S_1\text{)},$$
  together with the involution $[x_0:x_1:x_2:x_3] \mapsto [x_3:x_2:x_1:x_0]$ (`research/synthesis/torus_attracting_strata_and_generator_incidence.md`).
- **Torus-invariant pair obstruction in characteristic $0$:** By the promoted eigenform trace theorem ([R-0001](../results/R-0001-global-splitting-obstruction-for-the-model-rational-quartic.md)), no pair of $T$-semi-invariant homogeneous polynomials $(F_a, G_b)$ in characteristic $0$ cuts out $C_0$ set-theoretically (`research/synthesis/torus_attracting_strata_and_generator_incidence.md`).
- **Residual-control mechanism:** A 1-parameter family of 2-generated ideals $I_\tau = (q^3 + a_\tau, b_4 q)$ (with $q = x_0 x_3 - x_1 x_2 \in I_{C_0}$ and $a_\tau = x_1^4 x_3^2 - 2\tau x_0 x_1^2 x_2 x_3 + \tau^2 x_0^2 x_2^2$) has full saturated flat limit
  $$I_0 = \lim_{\tau\to 0} I_\tau = (q^3 + x_1^4 x_3^2,\; b_4 q,\; b_4 x_1^4 x_3^2),$$
  acquiring a genuine minimal generator in degree $10$ because the pencil limit $W_0 = \langle q^3 + x_1^4 x_3^2, b_4 q\rangle$ acquires a common factor on the $\tau\to\infty$ side (`research/synthesis/toric_sextic_residuals_and_limits.md`).
- **Active non-toric and semi-toric work streams on `main`:**
  1. Degree-$(6,6)$ general and ADE primitive-triple reductions (`research/supplements/SEXTIC_PAIR_REDUCTION.md`, `research/supplements/SEXTIC_ADE_REDUCTION.md`).
  2. Intrinsic filtered-Čech source-deficit and actual equation spaces for sextics and octics (`research/synthesis/global_equation_jets.md`, `research/supplements/ACTUAL_EQUATION_SPACES.md`, `research/synthesis/rank_strata_and_sextic_lifts.md`, `research/synthesis/order_three_roots_and_sextic_lifts.md`, `research/synthesis/actual_octic_root_lift_comparison.md`).
  3. Downstairs ACM thickenings, projected section defects, and quadratic-cover conductor descent (`research/synthesis/projected_thickening_section_defects.md`, `research/synthesis/quadratic_covers_and_conductor_descent.md`, `research/synthesis/supported_linkage_operations.md`).
  4. Local-to-global normal-filtration comparison defect ([R-0030](../results/R-0030-normal-filtration-comparison-obstruction-criterion.md), `research/synthesis/normal_filtration_boundary_obstructions.md`), tropical endpoint thickenings (`research/synthesis/tropical_thickenings_and_endpoint_duality.md`), and arithmetic Frobenius root specialization (`research/supplements/FROBENIUS_POWER_LIFTING_PRECISION.md`).

### 1.2 What the Toric Branch `codex/vgit-surface-pairs-torus-2026-11-01` (`c171cb2`) Adds
Commit `c171cb2` introduces `research/synthesis/vgit_surface_pairs_and_full_limits.md` and `research/computations/verify_vgit_surface_pairs.py`, providing four foundational advances over `main`:

1. **Intrinsic Primary-Power Neighborhood Bound ($N = ab/4$, All Characteristics):**
   Every actual sole-supported proper complete intersection $J = (F_a, G_b)$ with $V(J)_{\mathrm{red}} = C_0$ is unmixed of codimension $2$ (by Macaulay's unmixedness theorem for complete intersections in $S = k[x_0,x_1,x_2,x_3]$) and therefore $I_{C_0}$-primary of generic multiplicity $m = \deg(J)/\deg(C_0) = ab/4$. Since $C_0$ is smooth, $I_{C_0}^{(m)} = I_{C_0}^m$ at every point of $C_0$, and saturation forces
   $$I_{C_0}^{ab/4} \subset I_{C_0}^{(ab/4)} \subset J \subset I_{C_0}.$$
   Consequently, the closed nested-Hilbert locus $H_{ab/4}$ of ideals satisfying $I_{C_0}^{ab/4} \subset J \subset I_{C_0}$ contains all actual supported complete intersections of degrees $(a,b)$ and all of their flat $T$-limits $J_0, J_\infty$ without requiring an unspecified nilpotent exponent $N$. In particular:
   - $(6,6) \implies m = 9 \implies H_9$,
   - $(5,8) \implies m = 10 \implies H_{10}$,
   - $(8,8) \implies m = 16 \implies H_{16}$,
   - $(6,16) \implies m = 24 \implies H_{24}$.

2. **Compact Surface-Pair Parameter Spaces ($X_d$ and Unequal-Degree Bundles $\mathbf P(E)$):**
   - For equal degrees $a = b = d$: $X_d = \operatorname{Gr}(2, V_d)$ where $V_d = H^0(\mathcal I_{C_0}(d))$. For $d = 6$, $\dim V_6 = 59$ with centered $T$-weights in $[-9, 9]$ and profile
     $$(1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 4, 4, 4, 4, 3, 3, 2, 2, 1),$$
     giving $\dim \bigwedge^2 V_6 = 1711$, Plücker weights in $[-17, 17]$, $34$ VGIT chambers, and at most $630$ coarse extremal-weight blocks $X_{\ell,u} = \{W : \min \operatorname{wt}(W) = \ell, \max \operatorname{wt}(W) = u\}$.
   - For unequal degrees $a < b$: equivalence of pairs $(F_a, G_b) \sim (c_1 F_a, c_2 G_b + H_{b-a} F_a)$ is parameterized by the projective bundle $\mathbf P(E) \to \mathbf P(V_a)$ with fiber $\mathbf P(V_b / (F_a S_{b-a}))$ over $[F_a]$ (after quotienting out all ambient multipliers $S_{b-a}$, since $F_a \in I_{C_0}$ ensures $F_a S_{b-a} \subset V_b$).

3. **Full-Intersection Graph $\Gamma_d \subset X_d \times \operatorname{Hilb}^{P_{d,d}}$ and the Proper-Limit Lemma:**
   Over the open locus $U_d^{\mathrm{prop}} = \{[W] \in X_d : \gcd(W) = 1\}$, $(W)$ is a proper complete intersection with fixed Hilbert polynomial $P_{d,d}(n) = \binom{n+3}{3} - 2\binom{n-d+3}{3} + \binom{n-2d+3}{3}$. Let $\Gamma_d = \overline{\{(W, (W)) : W \in U_d^{\mathrm{prop}}\}}$ and $\Gamma_d^{\mathrm{supp}} = \Gamma_d \cap (X_d \times H_{d^2/4})$.
   - **Proper-Limit Lemma:** If $(W_\tau, (W_\tau)) \to (W_0, J_0)$ in $\Gamma_d$ and $\gcd(W_0) = 1$, then $(W_0)$ already has Hilbert polynomial $P_{d,d}$, so $(W_0) \subset J_0$ forces $J_0 = (W_0)$.
   - **Consequence (All Characteristics):** Any limit $(W_0, J_0) \in \Gamma_d$ where $J_0$ acquires extra minimal generators ($J_0 \supsetneq (W_0)$) must have a **non-proper limiting pencil** $\gcd(W_0) \neq 1$.
   - **Consequence (Characteristic $0$):** For any point $(W, J) \in \Gamma_d^{\mathrm{supp}}$, neither the positive limit $(W_+, J_+)$ nor the negative limit $(W_-, J_-)$ can have a proper limiting pencil ($\gcd(W_\pm) = 1$), because $W_\pm$ is $T$-invariant and $J_\pm \subset I_{C_0}$ would make $(W_\pm)$ a $T$-invariant complete intersection supported on $C_0$, contradicting [R-0001](../results/R-0001-global-splitting-obstruction-for-the-model-rational-quartic.md). Thus **both** $W_+$ and $W_-$ must lie on the common-factor boundary $\gcd(W_\pm) \in I_{C_0} \setminus k^\times$.

4. **Two-Polarization State Polytopes and Exact Boundary-Character Discrepancy:**
   Combining the Plücker polarization $\mathcal O_{X_d}(1)$ and a Hilbert polarization $\mathcal L_n$ yields joint state intervals $[r\ell(W) + s\ell_H(J),\, ru(W) + su_H(J)]$ and the exact boundary-character formula on the residual control family $W_\tau = \langle q^3 + a_\tau, b_4 q\rangle$:
   $$\chi_T((I_0)_n) - \chi_T(((W_0))_n) = \chi_T((I_0/(W_0))_n) = -5\bigl(N_{n-10} - N_{n-12}\bigr).$$

---

## 2. Ranked Evaluation of `main` Work Streams Benefiting from the Toric Approach

We evaluate every major active work stream on `main` against the combined toric toolkit (weight decomposition under $T$, invariant-limit stratification on $H_{ab/4}$, surface-pair VGIT on $X_d$ and $\mathbf P(E)$, and the full-limit graph $\Gamma_d^{\mathrm{supp}}$) and rank them by their **direct mathematical leverage in moving the STCI problem forward**.

| Rank | Work Stream on `main` | Target Degrees / Regime | Core Toric Mechanism | Expected Mathematical Payoff |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Degree-$(6,6)$ ADE Primitive-Triple & Double-Sextic Reduction** (`SEXTIC_ADE_REDUCTION.md`, `SEXTIC_PAIR_REDUCTION.md`) | $(6,6)$, $m=9$, char. $0$ | The two algebraic orbits $(A,B)=(rz,1)$ ($12r^2+4r+3=0$) are **$T$-fixed** triple ideals; the principal orbit $(A,B)=(1+z,-2-8z)$ is a single $T$-orbit whose $t\to 0,\infty$ limits degenerate to $T$-fixed boundary triples. The $27$-dim triple source $V_{\mathrm{triple}} \subset V_6$ and the contact maps $h, \Theta$ diagonalize into 1D/2D $T$-weight blocks! | Diagonalizes the $27$-dim sextic source, the $17$-rank first-normal map $h$, the $12$-rank cubic contact map $\Theta$, and the quadratic contact identity $h_G\Theta_F - h_F\Theta_G \equiv 0$ on $\operatorname{Gr}(2,27) \subset X_6$, directly attacking `FRONTIER.md` Priority #2. |
| **2** | **Common-Factor $\gcd(W_\pm)$ Stratification & Opposite-Limit Graph Fibers on $X_6 \times H_9$** (`torus_attracting_strata_and_generator_incidence.md`, `vgit_surface_pairs_and_full_limits.md`) | $(6,6)$, $m=9$, char. $0$ & all char. | In char. $0$, every $(W,J) \in \Gamma_6^{\mathrm{supp}}$ forces $\gcd(W_+), \gcd(W_-) \in I_{C_0}$ of degree $e_\pm \in \{2,3,4,5\}$. Stratify the boundary $\Delta_6^{\mathrm{cf}} \subset X_6$ by $e = \deg \gcd(W_0)$ and compare Plücker weight blocks of $\operatorname{Gr}(2, V_{6,2}) = \operatorname{Gr}(2,23)$ vs. $\operatorname{Gr}(2, V_6) = \operatorname{Gr}(2,59)$. | Directly addresses `FRONTIER.md` Priority #3: classifies the exact boundary strata of $X_6$ that can host $T$-limits of supported $(6,6)$ pairs, bounds their Plücker weights, and computes exact syzygy/degree-drop requirements for $J_0 \supsetneq (W_0)$. |
| **3** | **Torus-Equivariant Filtered-Čech Source-Deficit Filtration & Unequal-Degree Surface-Pair VGIT** (`global_equation_jets.md`, `rank_strata_and_sextic_lifts.md`, `actual_octic_root_lift_comparison.md`) | $(6,6)$, $(5,8)$, $(8,8)$, $(6,16)$ | The intrinsic filtered-Čech differential $d_3: E_3^{2,-2} \to E_3^{5,-4}$ (rank $11$) on $H^0(\operatorname{Sym}^2 E(6))$ ($33$-dim) and the octic recursion $V_{8,3} = q V_{6,2}$ inside $V_{8,2}$ ($80$-dim) are $T$-equivariant. Combine with unequal-degree VGIT bundle $E_F = V_b / F_a S_{b-a}$ and $H_{ab/4}$. | Diagonalizes the $33 \to 40$ sextic second-order symbol obstruction and $80$-dim octic source into tiny integer $T$-weight blocks ($\dim \le 3$ per weight), and establishes explicit weight profiles and $H_{ab/4}$ bounds for $(5,8)$, $(8,8)$, and $(6,16)$ (`FRONTIER.md` Priorities #1 & #4). |
| **4** | **Torus-Graded Quadratic-Cover Conductor Boundary & Downstairs ACM Section Defects** (`projected_thickening_section_defects.md`, `quadratic_covers_and_conductor_descent.md`, `supported_linkage_operations.md`) | All $(a,b)$ via $Q_3 \to \mathbf P^3$ (char. $\neq 2$) | The double cover $Q_3 = \operatorname{Proj} S[z]/(z^2 - (2bc-ad))$ is $T$-equivariant with uncentered $\operatorname{wt}(z)=2$ (centered $\operatorname{wt}(z)=0$). Thus the missing section $H_{uv}z \in B_{uv}/A_{uv}$ and the conductor boundary $T = S/J_\Delta$ carry canonical $T$-gradings. | Refines `FRONTIER.md` Candidate #3: proves that the missing ambient section $1 \mapsto H_{uv}z$ lies in centered $T$-weight $0$, and decomposes the conductor ideal $J_\Delta = (I_A :_S H_{uv})$ and ambient norm $f_A^2 - (2bc-ad)g_A^2$ by $T$-weights. |
| **5** | **Torus-Equivariant Normal-Filtration Comparison Defect & Arithmetic/Tropical Endpoint Algebra Comparison** (`normal_filtration_boundary_obstructions.md`, `tropical_thickenings_and_endpoint_duality.md`, `FROBENIUS_POWER_LIFTING_PRECISION.md`) | Endpoint local/global interface, char. $0$ & $p\equiv 2\pmod 3$ | Both the normal-filtration comparison defect $\Delta_n = \operatorname{length}(J_n/I^{(n)}) - \operatorname{length}(I^{(n)}/(I^{(n)}\cap J_{n+1}))$ ([R-0030](../results/R-0030-normal-filtration-comparison-obstruction-criterion.md)) on $T$-fixed limits and the arithmetic specialization root defect $T = I_{Z_0}/I_{D_0}$ at $\{p_0,p_\infty\}$ carry canonical endpoint $T$-gradings. | Connects the local endpoint defect $\operatorname{length}(T) = 1 + 2p^2 - p_a(D_K)$ in `FROBENIUS_POWER_LIFTING_PRECISION.md` to the tropical endpoint lattice conductors $\delta_0 + \delta_\infty$ (`tropical_thickenings_and_endpoint_duality.md`) and $T$-graded filtration jumps. |

---

## 3. Detailed Analysis of Each Ranked Work Stream

### 3.1 Rank 1: Degree-$(6,6)$ ADE Primitive-Triple & Double-Sextic Reduction via Torus Weights
- **Current state on `main` (`SEXTIC_ADE_REDUCTION.md`, `SEXTIC_PAIR_REDUCTION.md`):**
  In the $E_1$/primitive-triple branch of the degree-$(6,6)$ reduction (where both sextics contain a curvilinearity-1 triple thickening $I_{\mathrm{triple}}$ of $C_0$ of generic multiplicity $3$ and normal degree $-6$), all candidate triple loci reduce to **three stabilizer orbits**:
  - One rational principal orbit $(A(z), B(z)) = (1+z, -2-8z)$ with $S_0 = 4/3, T_0 = 1/6, \gamma(z) = 96(1+2z)$, and
  - Two conjugate algebraic orbits $(A(z), B(z)) = (rz, 1)$ over $\mathbf Q(\sqrt{-2})$ with $12r^2 + 4r + 3 = 0$, $S_0 = 0, T_0 = 1, \gamma(z) = 0$.
  For each of the three orbits, the space of sextics containing the triple locus has dimension $27$ ($20$ from $I_{\mathrm{triple},4} \cdot S_2$ plus $7$ genuine sextic directions). Along any such sextic $F$, the first normal coefficient $h_F$ (rank $17$) and the cubic contact polynomial $\Theta_F = \gamma E_F - K_F$ (rank $12$, joint $(h,\Theta)$ rank $26$, joint kernel $1$) must satisfy the quadratic contact identity
  $$h_G \Theta_F - h_F \Theta_G \equiv 0$$
  for a pair $(F,G)$ to achieve intersection multiplicity $9$ at the triple locus.
- **Why the toric approach transforms this stream:**
  1. **Exact $T$-invariance of the algebraic orbits:** Under the affine chart $x_0 = 1$ where $T$ acts with uncentered weights $\operatorname{wt}(x_1)=1, \operatorname{wt}(x_2)=3, \operatorname{wt}(x_3)=4$, the substitution for the algebraic orbit $(A,B) = (rz,1)$ is
     $$x_1 = z,\qquad x_2 = z^3 + y,\qquad x_3 = z^4 + \Bigl(r + \frac{3}{2}\Bigr) z y + m.$$
     Because $\operatorname{wt}(z) = 1$, $\operatorname{wt}(y) = 3$, and $\operatorname{wt}(m) = 4$, **every term in this substitution is homogeneous of uncentered weight $(1,3,4)$**! Consequently:
     - The algebraic triple ideal $I_{\mathrm{alg}}$ is **strictly $T$-invariant**.
     - Its $27$-dimensional sextic space $V_{\mathrm{alg},6} \subset V_6$ decomposes directly into $T$-weight subspaces $V_{\mathrm{alg},6} = \bigoplus_{w=-9}^9 V_{\mathrm{alg},6}[w]$.
     - For a $T$-weight sextic $F$ of uncentered weight $w \in \{0,\dots,24\}$, $h_F(z)$ is a scalar multiple of $z^{w-4}$ and $\Theta_F(z) = -K_F(z)$ is a scalar multiple of $z^{w-9}$!
  2. **$T$-orbit geometry of the principal orbit:** The principal orbit $(A(z), B(z)) = (1+z, -2-8z)$ is a single $1$-dimensional $T$-orbit: under $z \mapsto \lambda z$, the rescaled triple locus sweeps out the rational family of non-invariant triples and degenerates as $\lambda \to 0$ and $\lambda \to \infty$ to $T$-fixed boundary triple ideals. Moreover, its $27$-dimensional sextic space $V_{\mathrm{prin},6}$ is filtered by $T$-weights, and the bilinear map $\bigwedge^2 V_{\mathrm{triple},6} \to k[z]$, $(F \wedge G) \mapsto h_G \Theta_F - h_F \Theta_G$, can be analyzed directly on the Grassmannian $\operatorname{Gr}(2, 27) \subset X_6 = \operatorname{Gr}(2,59)$.

### 3.2 Rank 2: Common-Factor $\gcd(W_\pm)$ Stratification & Opposite-Limit Graph Fibers on $X_6 \times H_9$
- **Current state on `main` + `c171cb2`:**
  By the Proper-Limit Lemma (`vgit_surface_pairs_and_full_limits.md`), in characteristic $0$ every point $(W, J) \in \Gamma_6^{\mathrm{supp}} \subset X_6 \times H_9$ has both its positive and negative $T$-limit pencils $W_+, W_-$ in the common-factor boundary
  $$\Delta_6^{\mathrm{cf}} = \{[W_0] \in X_6 : \gcd(W_0) \in I_{C_0} \setminus k^\times\}.$$
- **Why the toric approach advances this stream:**
  Since $W_0 = \langle D \cdot A_{6-e}, D \cdot B_{6-e} \rangle$ is $T$-invariant and $D = \gcd(W_0) \in I_{C_0}$ is a $T$-semi-invariant homogeneous polynomial of degree $e \in \{2, 3, 4, 5\}$ (as $I_{C_0}$ starts in degree $2$ with the unique quadric $q = x_0 x_3 - x_1 x_2$ of centered weight $0$), $\Delta_6^{\mathrm{cf}}$ stratifies canonically by $e = \deg \gcd(W_0)$:
  1. **$e = 2$ ($D = q$):** Since $I_{C_0,2} = k \cdot q$ ($\operatorname{wt}(q) = 0$), every $e=2$ common-factor pencil has the form $W_0 = q \cdot \langle A_4, B_4 \rangle$ with $\langle A_4, B_4 \rangle \in \operatorname{Gr}(2, S_4)$ and $\gcd(A_4, B_4) = 1$. Its Plücker weights lie in $[-16, 16]$ (within the double-sextic subspace $V_{6,2} \subset V_6$).
  2. **$e = 3$ ($\deg D = 3$):** $D \in V_3$ ($4$-dimensional, centered weights $\{-3, -1, 1, 3\}$) and $\langle A_3, B_3 \rangle \in \operatorname{Gr}(2, S_3)$.
  3. **$e = 4$ ($\deg D = 4$):** $D \in V_4$ ($15$-dimensional) and $\langle A_2, B_2 \rangle \in \operatorname{Gr}(2, S_2)$.
  4. **$e = 5$ ($\deg D = 5$):** $D \in V_5$ ($34$-dimensional) and $\langle A_1, B_1 \rangle \in \operatorname{Gr}(2, S_1)$.
  By computing the exact $T$-weight profiles of $V_{6,2}$ ($23$-dimensional), $V_{6,3}$ ($1$-dimensional, spanned by $q^3$ of weight $0$), and the strata $\Delta_6^{\mathrm{cf}}(e)$, together with the Hilbert-function deficit $\dim (J_0)_n - \dim (W_0)_n$ required for $(W_0, J_0) \in \Gamma_6^{\mathrm{supp}}$, we obtain exact numerical and structural obstructions on which boundary strata can support a degree-$(6,6)$ limit in $H_9$.

### 3.3 Rank 3: Torus-Equivariant Filtered-Čech Source Deficit & Unequal-Degree Surface-Pair VGIT
- **Current state on `main` (`global_equation_jets.md`, `rank_strata_and_sextic_lifts.md`, `actual_octic_root_lift_comparison.md`):**
  The intrinsic filtered-Čech spectral sequence for $\mathcal I_{C_0}(d)$ identifies the second-order symbol space $E_3^{2,-2}(d) \cong H^0(\operatorname{Sym}^2 E(d-6))$ and the differential $d_3: H^0(\operatorname{Sym}^2 E(d-6)) \to E_3^{5,-4}(d)$. For $d=6$, $H^0(\operatorname{Sym}^2 E) \cong S_2^{\oplus 3} \oplus S_0$ has dimension $33$, the cubic target $T_9$ has dimension $40$, and $d_3$ has rank $11$, leaving a $22$-dimensional achievable second-order symbol space $V_{6,2}/V_{6,3}$ (`global_equation_jets.md`). For $d=8$, $V_{8,2}$ has dimension $80$ and $V_{8,3} = q V_{6,2}$ has dimension $23$. Meanwhile, unequal-degree pairs such as $(5,8)$ and $(6,16)$ are highlighted in `FRONTIER.md` Priorities #1 and #4.
- **Why the toric approach advances this stream:**
  Both the Koszul-wall complex and the filtered-Čech differential $d_3$ are strictly $T$-equivariant. Decomposing the $33 \to 40$ map for $d=6$ and the $80$-dimensional space $V_{8,2}$ for $d=8$ by centered $T$-weights breaks the rank-$11$ obstruction into independent weight blocks of dimension at most $3$, giving an explicit weight-by-weight basis of the $11$ missing symbol relations. Simultaneously, for unequal degrees $(a,b) \in \{(5,8), (6,16)\}$, we can compute the exact $T$-weight profiles of $V_a$, $V_b$, the quotient bundle $E_F = V_b / (F_a S_{b-a})$ over $T$-weight generators $F_a \in V_a$, and the intrinsic primary-power bounds $H_{10}$ (for $(5,8)$) and $H_{24}$ (for $(6,16)$).

### 3.4 Rank 4: Torus-Graded Quadratic-Cover Conductor Boundary & Downstairs ACM Section Defects
- **Current state on `main` (`projected_thickening_section_defects.md`, `quadratic_covers_and_conductor_descent.md`, `supported_linkage_operations.md`):**
  Under the finite double cover $\pi: Q_3 = V(z^2 - \Delta_0) \to \mathbf P^3$ branched along $\Delta_0 = 2x_1 x_2 - x_0 x_3$, $C_0$ lifts to $C^+ \subset Q_3$ (cut out by $z - (x_1 x_2 + x_0 x_3) = 0$ on $C_0$), and any downstairs ACM thickening $Z \subset \mathbf P^3$ supported on $C_0$ with $H^1(\mathcal I_Z(*)) = 0$ has missing-section defect controlled by $H_{uv} z \in B_{uv}/A_{uv}$ and conductor ideal $J_\Delta = (I_A :_S H_{uv})$.
- **Why the toric approach advances this stream:**
  Because $\Delta_0 = 2x_1 x_2 - x_0 x_3$ has uncentered $T$-weight $4$ and centered $T$-weight $0$, assigning $\operatorname{wt}_{\mathrm{unc}}(z) = 2$ (and $\operatorname{wt}_{\mathrm{cen}}(z) = 0$) makes $\pi: Q_3 \to \mathbf P^3$, the lifted curve $C^+$, the conjugate curve $C^-$, and the involution $\sigma(z) = -z$ **strictly $T$-equivariant**! Therefore:
  - For any $T$-invariant thickening $Z_0 \in H_{ab/4}$, the extension class $H_{uv} z \in B_{uv}/A_{uv}$ is homogeneous of centered $T$-weight $0$.
  - The conductor ideal $J_\Delta = (I_A :_S H_{uv})$ and the conductor quotient $T = S/J_\Delta$ are $T$-graded, allowing weight-by-weight analysis of the ambient norm identity $f_A^2 - (2bc-ad)g_A^2 \in I_Z$ and the section-repair multiplication maps.

### 3.5 Rank 5: Torus-Equivariant Normal-Filtration Comparison Defect & Arithmetic/Tropical Endpoint Algebra Comparison
- **Current state on `main` (`normal_filtration_boundary_obstructions.md`, `tropical_thickenings_and_endpoint_duality.md`, `FROBENIUS_POWER_LIFTING_PRECISION.md`):**
  The local-to-global filtration defect $\Delta_n(J)$ ([R-0030](../results/R-0030-normal-filtration-comparison-obstruction-criterion.md)) measures the discrepancy between $J \cap I^{(n)}$ and $I^{(n)}$ across filtration steps, while `FROBENIUS_POWER_LIFTING_PRECISION.md` isolates the finite endpoint module $T = I_{Z_0}/I_{D_0}$ supported at $\{p_0, p_\infty\}$ of length $1 + 2p^2 - p_a(D_K)$, and `tropical_thickenings_and_endpoint_duality.md` studies tropical endpoint conductor lattices $A_0 \subset B_0, A_\infty \subset B_\infty$.
- **Why the toric approach advances this stream:**
  At the two $T$-fixed endpoints $p_0 = [1:0:0:0]$ and $p_\infty = [0:0:0:1]$, the local rings carry opposite $T$-actions ($s = x_1/x_0$ has weight $+1$ at $p_0$, while $u = x_2/x_3$ has weight $-1$ at $p_\infty$). Relating the $T$-graded conductor defect $\delta_0 + \delta_\infty$ of tropical endpoint subalgebras to the arithmetic specialization root defect $\operatorname{length}(T) = 1 + 2p^2 - p_a(D_K)$ unifies the local endpoint obstructions across characteristic $0$ and characteristic $p$.

---

## 4. Iterative Execution Plan on `evaluate_toric_integration_stci`

We will execute the ranked recommendations in order, with each step accompanied by:
1. Exact mathematical formulation and intrinsic/geometric proofs where available, plus minimal standard-library Python verification scripts where finite rank or weight-block certificates are required.
2. Independent review by a dedicated subagent (following `research/CONTRIBUTING_AGENT.md` and `AGENTS.md`), with proactive subagent retirement immediately after each review completes.
3. Canonical record validation via `python3 research/computations/validate_records.py`.
4. Frequent commits authored by **Gemini** (`Gemini <gemini@google.com>`) pushed to `origin evaluate_toric_integration_stci`.
