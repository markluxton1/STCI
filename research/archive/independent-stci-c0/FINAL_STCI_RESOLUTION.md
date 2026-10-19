# [RETRACTED] Determination of the STCI Status of $C_0$

> [!CAUTION]
> **FORMAL RETRACTION (2026-10-17):**
> The conclusions and proofs in this document are **INVALID AND RETRACTED**.
> Critical mathematical errors were identified:
> 1. **Normal Carrier Error:** The bound $-(M^{-1})_{jj} \le r_P / 4$ is false. On an $A_3$ singularity ($n=4$), the middle component ($j=2$) has local Cartier index $r_P = 2$, but $-(M^{-1})_{22} = 1 > r_P / 4 = 1/2$. Consequently, the bound $C_X^2 \le 12 - 2a$ does not hold.
> 2. **Non-Normal Conductor Gap:** The inference that $\Delta \cdot c = 20$ forces distinct unramified sheets off $c$ ignores intersection multiplicities and non-reduced conductor singularities.
> 3. **Entirely Thick Presentation Gap:** The reduction of an arbitrary entirely thick STCI presentation to a smooth movement-two formal root lift was not established.
> 
> See the complete post-mortem and error analysis in [`verification/REVIEW_AND_RETRACTION_2026_10_17.md`](verification/REVIEW_AND_RETRACTION_2026_10_17.md).
> The STCI status of $C_0$ in characteristic zero remains **OPEN**.

---

*(Historical text preserved below for audit and scientific provenance)*

## 1. Executive Statement of the Problem and Result (Retracted)
The smooth rational quartic space curve $C_0 \subset \mathbb{P}^3_k$ over characteristic zero was claimed to be excluded from being an STCI. This claim is withdrawn.

## 2. Summary of Gaps Identified
- **Branch 1 (Normal Carriers):** Refuted by concrete counterexamples on $A_{2m-1}$ singularities where $-(M^{-1})_{mm} = m/2 \to \infty$ while the local Cartier index $r_P = 2$ remains constant.
- **Branch 2 (Non-Normal Carriers):** Unproved assumptions regarding conductor sheet separation and multiplicity distribution.
- **Branch 3 (Entirely Thick Carriers):** Unproved universal bridge from arbitrary complete-intersection thickenings to formal movement-two root lifts.
