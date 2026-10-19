# Independent STCI Determination for $C_0$

> [!WARNING]
> **STATUS AS OF 2026-10-17:**
> An initial attempt to prove that $C_0$ is not an STCI across all carriers failed due to fatal mathematical errors (notably the breakdown of the $c \le r_P/4$ bound on $A_{2m-1}$ singularities and conductor multiplicity gaps).
> 
> The claimed non-STCI theorem is **RETRACTED**.
> The problem remains **OPEN**.
> 
> Full post-mortem and counterexample details are recorded in [`verification/REVIEW_AND_RETRACTION_2026_10_17.md`](verification/REVIEW_AND_RETRACTION_2026_10_17.md).

## Problem Statement
Determine definitively whether the smooth rational quartic curve
$$C_0 = [s^4 : s^3 t : s t^3 : t^4] \subset \mathbb{P}^3$$
is a set-theoretic complete intersection (STCI) over an algebraically closed field of characteristic zero ($k = \mathbb{C}$).

## Current Genuine Frontier
1. **Normal Carriers:**
   - The Extremal-Ray criterion $\Gamma_X(C_0) = 16/a - C_0^2 = 0$ is a valid necessary and sufficient condition in characteristic zero.
   - Proving $\Gamma_X(C_0) > 0$ universally requires genuinely bounding the singular contributions without assuming $c \le r_P/4$ (which fails for $A_3$ and higher $A_k$).
   - The question of whether an extremal normal carrier can exist remains open.
2. **Non-Normal Carriers:**
   - The three Cartier singleton models ($a=8, 8, 16$) require rigorous phase-space analysis of the 16-parameter projection families rather than naive distinct-point conductor counts.
3. **Entirely Thick Carriers:**
   - Requires bridging general complete-intersection thickenings to the formal obstruction tower.
