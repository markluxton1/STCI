# Master Goal Specification: STCI Status of $C_0$

**Overarching Goal:** Determine definitively whether the smooth rational quartic space curve $C_0 \subset \mathbb{P}^3_k$ ($k$ algebraically closed, $\operatorname{char}(k) = 0$) is a set-theoretic complete intersection (STCI).

## Stratified Proof Architecture

### Stage 1: The Normal Carrier Hodge Gap Theorem
**Objective:** Prove that for every normal integral hypersurface $X$ of degree $a \ge 5$ containing $C_0$, the Hodge gap is strictly positive:
$$\Gamma_X(C_0) = \sum_P \frac{A_P + D_{r_P, P}}{r_P} - \left( 7 - \frac{16}{a} \right) > 0$$
thereby precluding $C_0^2 = 16/a$ and proving that **no normal carrier of any degree admits an STCI mate**.

**Key Constraints for Candidate Equality Surfaces:**
1. Maximum local Cartier index $s = \max_P r_P \ge 5$.
2. Degree bound: $4a^2 - (7s+6)a + 16s \le 0 \implies s \ge \lceil a(4a-6)/(7a-16) \rceil$.
3. Parity condition: $r_P D_{r_P, P}$ is even.
4. Torsion certificate on the symbolic-triple divisor $T_3$:
   $$2 \le \deg T_3 \le \sum_{r_P=2} A_P + \frac{1}{2} \sum_{r_P \ge 4} r_P D_{r_P, P}$$
   with apolar support restricted to the specified endpoint / mixed configurations.
5. Divisibility: with $g = \gcd(a, 4)$ and $R = \operatorname{lcm}_P r_P$, $a \mid 16R$.

### Stage 2: Non-Normal Carriers and Conductor Phase Tori
**Objective:** Prove that no non-normal carrier $X \supset C_0$ admits an STCI mate.
1. **The Three Cartier Singleton Models:**
   - Model 1: $a = 8$, normalization $S = \mathbb{P}^1 \times \mathbb{P}^1$, $H = (2, 2)$, $c = (1, 1)$.
   - Model 2: $a = 8$, normalization $S$ a quadric cone, $H = 2c$, $c$ a Cartier conic.
   - Model 3: $a = 16$, normalization $S = \mathbb{P}^2$, $H = \mathcal{O}(4)$, $c$ a line.
   - For each model, analyze the 16-parameter projection families and use Laurent's theorem / Mann's bounds to prove that the constructible phase image in the conductor torus contains no admissible torsion points (empty torsion cosets).
2. **Non-Cartier / Multi-branch Conductors:**
   - Use the full conductor lattice descent criterion $\Lambda_{\text{desc}} = \ker[\mathbb{Z}^{s+1} \to \operatorname{Cl}(S)]$ to obstruct descent of rational multiples across singular branches.

### Stage 3: Entirely Thick Complete Intersections
**Objective:** Prove that no pair of surfaces $(F, G)$ with $\operatorname{ord}_{C_0}(F) \ge 2$ and $\operatorname{ord}_{C_0}(G) \ge 2$ can have reduced intersection $C_0$.
- Apply conormal Loewy-socle and moving-relation obstruction towers: show that the gap-cost $\Delta \ge \frac{1}{2}\epsilon(s-r)(s-r+1) + \delta$ and formal-root obstruction bundle forces non-vanishing obstruction at every finite truncation order.

### Stage 4: Synthesis and Conclusion
Assemble Stages 1, 2, and 3 into an exhaustive, watertight proof that $C_0$ is **NOT** a set-theoretic complete intersection in characteristic zero.
