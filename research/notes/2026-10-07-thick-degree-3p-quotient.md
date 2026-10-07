# Entirely-thick boundary: exact degree-3p quotient modulo the quadric

Date: 2026-10-07
Status: PROVED

Let C=[s^4:s^3t:st^3:t^4] be the smooth rational quartic, Q its unique smooth quadric, and I=I_C.

## 1. Cartier restriction on Q

On Q=P1xP1, C has class (1,3), so
\[
I_C^p O_Q=O_Q(-p,-3p).
\]
After twisting by 3p,
\[
I_C^pO_Q(3p)=O_Q(2p,0).
\]

Thus restriction gives
\[
(I^p)_{3p}\longrightarrow H^0(Q,O_Q(2p,0)).
\]

The target has dimension 2p+1.

## 2. Surjectivity from cubic equations

For p=1,
\[
\dim I_3=20-h^0(C,O_C(3))=20-13=7.
\]
The unique quadric Q times linear forms contributes a 4-dimensional subspace. Therefore
\[
I_3/(Q S_1)
\]
has dimension 3, matching
\[
H^0(Q,O_Q(2,0)).
\]
The restriction map is therefore an isomorphism on this quotient.

Choose cubic equations A_0,A_1,A_2 whose restrictions form a basis of H^0(P1,O(2)) in the ruling-base coordinate.

For arbitrary p, products of p such cubics lie in (I^p)_{3p}. Their restrictions are products of p binary quadratics. The multiplication map
\[
\operatorname{Sym}^p H^0(P^1,O(2))
\to H^0(P^1,O(2p))
\]
is surjective (equivalently every binary monomial of degree 2p is a product, or linear combination of products, of p binary quadratics).

Hence
\[
(I^p)_{3p}\twoheadrightarrow H^0(Q,O_Q(2p,0))
\]
is surjective for every p>=1.

Consequently
\[
(I^p)_{3p}/\big((I^p)_{3p}\cap(Q)\big)
\cong H^0(Q,O_Q(2p,0)),
\]
and this quotient has dimension exactly
\[
2p+1.
\]

## 3. Interpretation

Every possible equality-boundary restriction
\[
F|_Q=h^pR,\qquad R\in H^0(O_Q(2p,0))
\]
already has a lift obtained from products/linear combinations of p cubic equations of C.

Thus the non-Q-divisible part of the degree-3p boundary contains no hidden higher-Rees obstruction.

The STCI equality condition restricts R to the nonlinear repeated-root locus with at most min(p,q) distinct roots, but every such R still lifts to I^p in degree 3p.

## 4. Where ambient freedom remains

The fiber over a fixed residual binary form is an affine translate of
\[
K_p=(I^p)_{3p}\cap(Q).
\]
Equivalently
\[
K_p=Q\,(I^p:Q)_{3p-2}.
\]

No claim is made here that
\[
(I^p:Q)=I^{p-1}.
\]
That colon identity would require a separate associated-graded/Rees argument.

Hence the remaining ambient classification problem is exactly the kernel/colon problem, not the boundary restriction problem.

## 5. Strategic consequence

The equality a=3p is rigid on Q but flexible enough that every allowed binary residual divisor lifts. Therefore one cannot exclude the (3,4) boundary from the F-side restriction alone.

Any further obstruction must use at least one of:
- the Q-divisible kernel K_p;
- compatibility with the mate G;
- singularity/normalization properties of the chosen lift;
- or higher pair/valuation data.

This sharply separates the solved quotient problem from the unresolved ambient problem.
