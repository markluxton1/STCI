# Entirely-thick boundary: first-blowup marked-point coupling audit

Date: 2026-10-07
Status: STRUCTURAL AUDIT / NO c_T-versus-M_T INEQUALITY FROM SEMICONTINUITY

Fix a horizontal component T of the first exceptional intersection cycle on
\[
B=\operatorname{Bl}_C P^3,
\qquad E=P(N_{C/P^3}),
\]
and let P=T cap S_Q be the marked point where T meets the quadric-direction section.

The goal is to put the generic coefficient c_T and the special repeated-root multiplicity M_T into one local model.

## 1. Blowup coordinates

Locally on C choose a parameter t and transverse parameters y,z with
\[
I_C=(y,z),\qquad Q=(z=0).
\]

On the blowup, the exceptional divisor is locally the projective normal-direction bundle with homogeneous coordinates
\[
[Y:Z]=[y:z].
\]

The strict transform of Q meets E in the section
\[
S_Q=[1:0].
\]

If F and G have exact generic orders p and q along C, write their initial normal forms as homogeneous binary forms
\[
f_p(t;Y,Z),\qquad g_q(t;Y,Z).
\]
Their common zero scheme on E is the first exceptional intersection W.

A horizontal component T corresponds generically to a common linear factor
\[
L_T(t;Y,Z)
\]
of these two binary forms over k(C). Its coefficient c_T in W is the generic intersection multiplicity of the two transformed divisors along T; equivalently it is determined in the completed two-dimensional local ring at the generic point of T.

## 2. The marked root multiplicity is a section-intersection phenomenon

The equality-boundary repeated-root multiplicity M_T is detected where T meets S_Q.

It is not obtained by taking a finite flat family of zero-dimensional complete intersections parameterized by T and then specializing its length. Rather, it records the order with which the restriction of the F-symbol to the distinguished section S_Q vanishes at the point
\[
P=T\cap S_Q.
\]

Thus c_T and M_T are two measurements of the same first-blowup geometry but in different directions:

- c_T: generic transverse intersection of D and D' along T;
- M_T: tangency/vanishing of the F-symbol along S_Q at T cap S_Q.

Ordinary upper semicontinuity of fiber length does not compare them.

## 3. Why a naive local trivialization is misleading

In a local trivialization of E over an open subset of C, write a section as
\[
[1:\lambda(t)].
\]
Then S_Q is [1:0]. A different constant graph [1:\lambda_0] with nonzero constant lambda_0 does not meet S_Q inside that trivializing open set.

The actual intersection T cap S_Q therefore depends on the global ruled-surface geometry and on transition functions. It cannot be modeled correctly by declaring both T and S_Q to be coordinate axes in one product chart over all of C.

This is precisely why modifications concentrated at P can alter M_T without altering the generic germ along T and hence without altering c_T.

## 4. No semicontinuity inequality

There is therefore no legitimate argument of the form
\[
M_T\le c_T
\]
or
\[
c_T\ge\Phi(M_T)
\]
coming merely from upper semicontinuity of local complete-intersection length.

Such an inequality would require an additional global divisor/line-bundle relation controlling how T approaches S_Q.

This strengthens the earlier root-budget separation result: even after placing both invariants on the first blowup, they are not fibers of one finite flat length function.

## 5. The correct coupling datum

The first place a genuine relation can occur is the divisor theory of the ruled surface E itself.

One should compute:
1. the divisor classes of T and S_Q in Pic(E);
2. their intersection number T.S_Q;
3. the divisor of the restriction of the first normal form f_p to S_Q;
4. how the common-factor divisor sum c_j T_j sits relative to S_Q;
5. whether the equality u=0 forces a relation among local intersection multiplicities
   \[
   I_P(T_j,S_Q),
   \]
   the root multiplicities M_j, and the section coefficients c_j.

This is a global ruled-surface calculation, not a local semicontinuity calculation.

## 6. Immediate next target

Use the known identifications
\[
E\simeq P^1\times P^1,\qquad
H|_E=O_E(4,0),\qquad
E|_E=O_E(7,-1)
\]
to identify the exact classes of:
- constant horizontal sections T_j;
- the quadric-direction section S_Q.

Then compute T_j.S_Q and the restriction of D|_E and D'|_E to S_Q.

This should determine whether the repeated-root multiplicities are already encoded by the intersection divisor
\[
W|_{S_Q}
\]
and, crucially, whether the coefficients c_j enter that divisor or disappear after restriction.
