# Entirely-thick boundary: sheaf-colon recursion by the quadric

Date: 2026-10-07
Status: PROVED SHEAF COLON / HOMOGENEOUS SATURATION STEP OPEN

Let I=I_C be the ideal sheaf of the smooth rational quartic C in P3 and let Q be its unique quadric equation.

## 1. Regular-embedding associated graded

Because C is smooth of codimension two in the smooth threefold P3, C is a regular embedding. Hence
\[
\operatorname{gr}_{\mathcal I}O_{P^3}
=\bigoplus_{m\ge0}\mathcal I^m/\mathcal I^{m+1}
\simeq \operatorname{Sym}_{O_C}(\mathcal I/\mathcal I^2).
\]

The first normal class of Q is a section
\[
\bar Q\in H^0(C,\mathcal I/\mathcal I^2(2)).
\]
Since Q is smooth along C, this class is nowhere zero. Equivalently it defines a line subbundle direction in the rank-two conormal bundle.

Locally trivializing the conormal bundle with \bar Q as one basis vector, multiplication by \bar Q on every symmetric power is multiplication by an indeterminate in a polynomial algebra. It is injective.

## 2. Sheaf colon identity

For every p>=1,
\[
(\mathcal I^p:Q)=\mathcal I^{p-1}.
\]

Proof: inclusion from right to left is immediate. If Qf lies in \mathcal I^p, reduce f modulo \mathcal I^{p-1}. Its lowest nonzero I-adic initial form, if any, lies in Sym^j(I/I^2) for j<p-1. Multiplication by \bar Q is injective and produces a nonzero class in degree j+1<p, contradicting Qf in I^p. Hence f lies in I^{p-1}.

This is local/sheaf-theoretic and requires no Rees-algebra linear-type hypothesis.

## 3. Consequence for the degree-3p kernel

If a homogeneous polynomial K of degree 3p-2 satisfies
\[
QK\in (I_{\rm hom}^p)_{3p},
\]
then after sheafification
\[
K\in H^0(P^3,\mathcal I^{p-1}(3p-2)).
\]

Thus
\[
(I_{\rm hom}^p:Q)_{3p-2}
\subseteq
H^0(\mathcal I^{p-1}(3p-2)).
\]

The reverse containment at the sheaf level is equality. The only unresolved issue for the homogeneous ordinary power is whether every global section on the right is represented in degree 3p-2 by the ordinary power I_{\rm hom}^{p-1}.

Equivalently, the only possible failure of
\[
(I_{\rm hom}^p:Q)_{3p-2}=(I_{\rm hom}^{p-1})_{3p-2}
\]
comes from saturation/irrelevant-ideal torsion of the ordinary power.

## 4. Recursive shape if saturation holds in this degree

If
\[
H^0(\mathcal I^{p-1}(3p-2))=(I_{\rm hom}^{p-1})_{3p-2},
\]
then the kernel from the degree-3p quotient note is exactly
\[
K_p=Q\,(I_{\rm hom}^{p-1})_{3p-2}.
\]

Combined with surjectivity onto H^0(Q,O(2p,0)), every boundary carrier has
\[
F=F_{\rm cub}+QK,
\]
where F_cub is a linear combination of products of p cubic equations of C and
\[
K\in(I^{p-1})_{3p-2}.
\]

This would give an exact recursion lowering normal order by one while lowering ambient degree by two.

## 5. Literature boundary

The sheaf-colon statement is standard regular-embedding/conormal algebra. Literature on Rees algebras and powers of rational normal curves is related but does not directly establish the homogeneous saturation assertion for this projected rational quartic, so no such theorem is imported here.

## 6. Next target

Determine
\[
H^0(\mathcal I^m(3m+1))/(I_{\rm hom}^m)_{3m+1}
\]
for m=p-1.

A vanishing result proving this quotient zero for all m would close the colon recursion. Otherwise an explicit nonzero quotient would identify the precise symbolic/saturated correction to the equality-boundary carrier space.
