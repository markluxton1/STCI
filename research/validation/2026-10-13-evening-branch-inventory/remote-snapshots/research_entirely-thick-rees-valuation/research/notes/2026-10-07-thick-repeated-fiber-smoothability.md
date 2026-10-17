# Entirely-thick boundary: repeated ruling fibers do not force carrier singularity

Date: 2026-10-07
Status: NEGATIVE STRUCTURAL RESULT

Assume the equality-side carrier F has degree 3p and exact order p along C. On Q,
\[
F|_Q=h^pR_F,
\]
and let a trisecant ruling fiber L occur in R_F with multiplicity M>=2.

## 1. Local ambient form along L away from C

At the generic point of L, choose regular local coordinates x,z with
\[
Q=(z=0),\qquad L=(x=z=0).
\]
Since F|_Q vanishes to order M along L,
\[
F=x^M u+zA
\]
with u a unit after localization.

Along L,
\[
\partial F/\partial x=0
\]
when M>=2, but
\[
\partial F/\partial z=A|_L.
\]
Therefore F is smooth at the generic point of L whenever A|_L is nonzero.

## 2. The degree-3p recursion supplies the transverse smoothing term

The exact boundary recursion proved previously is
\[
F=F_{\rm cub}+QK,\qquad
K\in(I_C^{p-1})_{3p-2}.
\]
The QK term is precisely the local zA term above.

At a point of L outside C, the ideal sheaf I_C is the unit ideal. Hence membership
\[
K\in I_C^{p-1}
\]
places no local vanishing condition on K there.

Thus the order-p condition along C does not force K|_L to vanish generically. For a fixed L, nonvanishing of K at its generic point is an open condition on the available kernel space whenever a section not containing L is chosen.

Consequently repeated multiplicity M of L in R_F does not by itself force the ambient carrier F to be singular along L.

## 3. Strategic consequence

The repeated-root equality theorem cannot be upgraded to a carrier exclusion by the argument
\[
M>=2\Rightarrow F\text{ singular along }L.
\]
The Q-divisible kernel is exactly the missing transverse derivative and can smooth the carrier.

This is compatible with the earlier separation result: root multiplicity is special quadric-direction data, while generic carrier behavior along the ruling fiber has an independent transverse degree of freedom.

## 4. Pair geometry is essential

For an STCI pair, the mate G restricted to L is globally constrained: its nonzero residual restriction has zeros supported on the degree-three divisor C cap L.

Thus the remaining possible coupling is not generic singularity of F along L. It must involve compatibility among:
- the transverse smoothing coefficient K|_L for F;
- the restriction of G to L;
- the three marked points of C cap L;
- and the exceptional/valuation data above those points.

In particular, any useful repeated-root obstruction must use behavior at the marked divisor C cap L or variation in the ruling family, rather than the generic point of L.

## 5. Boundary of the claim

This note does not assert existence of a global smooth STCI carrier with arbitrary prescribed repeated residual divisor. It proves only that repeated residual multiplicity plus membership in I_C^p supplies no local mechanism forcing generic singularity along L.

A global singularity statement would require an additional relation forcing every allowable K to vanish on L; no such relation is currently established.
