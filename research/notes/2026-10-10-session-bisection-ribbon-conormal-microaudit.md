# Bisection ribbon and ambient conormal microaudit

Date: 2026-10-10. Auditor: `bisection_full_audit/primary_descent_sources`.
Verdict: **ACCEPT** Sections 2--4 of the
[full independent bisection audit](2026-10-10-session-genus-two-bisection-full-independent-audit.md).
Input SHA256:
`5aa6eeedb31ff2fe316b706c3c0e86ff78d9beca01c9f92dfa5d7fafcc283133`.
This hash was checked directly after reading the source. The earlier
primary-source audit is unchanged.

## Exact hypotheses checked

Work over an algebraically closed field of characteristic zero. The
embedded reduction is the literal smooth rational curve
`C0=[s^4:s^3t:s t^3:t^4]`. The normal integral projective surface S is
Cohen--Macaulay, with `chi(O_S(mH))=1+2m^2+m`. Its actual finite
normalization morphism maps a smooth embedded `c_S` isomorphically to C0
and is an isomorphism away from the accepted conductor line Gamma.
There is an actual Cartier section Q with entire divisor `2c_S` and
`2c_S~2H`. Numerical equivalence or generic multiplicity alone would
not supply this last input.

## Purity and the global nilideal

The Cartier quotient `R=V(Q)` of the CM surface is pure CM of dimension
one. At the generic point of c_S the normal surface is a DVR, so R has
length two and its nilideal J has generic rank one with generic square
zero. The coherent image `J^2` inside `O_R` is supported at finitely many
points. Purity forbids such a nonzero subsheaf, so `J^2=0` everywhere.
Thus J is an `O_c_S`-module. Any torsion in that module would again be a
finite-support subsheaf of `O_R`, hence zero. Smoothness of c_S makes
this rank-one torsion-free module a line bundle.

The Cartier sequence gives `chi(O_R)=1-7=-6`. The reduction sequence
then gives `chi(J)=-7`, hence `J=O_P1(-8)`. No Gorenstein or
Q-Gorenstein property of S is used.

## Normal bundle and the actual ambient map

I checked both displayed derivative coefficient lists independently.
They force ten coefficients to vanish immediately, and the remaining
two satisfy a matrix of determinant eight. Consequently
`H0(N_C0/P3^*(6))=0`. Together with `deg(N)=14` and splitting on P1,
this yields `N=O(7) direct_sum O(7)`, so
`Hom(N^*,O(-8))=0`.

The morphism `R->P3` induces `I_C0->J`. Its square maps into `J^2=0`,
and the reduction is the given closed embedding, so the induced map
`I_C0/I_C0^2 -> J` is globally `O_C0`-linear. Formation of this map
does **not** require an immersion over Gamma. On the dense complement
of Gamma, normalization is an isomorphism and R is a closed subscheme
of P3. There `I_C0` generates the nonzero nilideal J. The global map
is therefore generically surjective and nonzero, contradicting the
displayed Hom vanishing. I found no gap in this interface.

## Scope and reusable consequence

This accepts the exclusion of the entire genus-two bisection mate lane
once its independently established Cartier equivalence is supplied.
The ribbon argument itself proves the stronger conditional statement:
**any** genus-two normalization in this fixed embedding admitting
`2c_S~2H` is impossible, regardless of which lane supplies that input.

More generally, a rational ribbon R with nilideal
`O(-p_a(R)-1)` and a morphism generically closed onto an embedded C in
P3 requires `p_a(R)<=max{a,b}-1`, where `N_C/P3=O(a)+O(b)`.
Here it would require `7<=6`.

The separate `lambda=1` section lane has not thereby been excluded:
its actual order-two Cartier compression is not an accepted input.
Higher-degree carriers, the unrestricted C0 question, and the universal
STCI problem remain open. No canonical frontier file is edited here.
