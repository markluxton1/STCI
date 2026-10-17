# Entirely-thick boundary: quadric section and exceptional intersection divisor

Date: 2026-10-07
Status: PROVED CLASS CALCULATION / IDENTIFICATION ISSUE FLAGGED

On the first blowup B=Bl_C P3 let E be the exceptional surface. Use the established convention
\[
E\simeq P^1\times P^1,\qquad
H|_E=O_E(4,0),\qquad
E|_E=O_E(7,-1).
\]

## 1. Class of the quadric-direction section

The strict transform of the unique quadric is
\[
\widetilde Q=2H-E.
\]
Hence its intersection with E is
\[
S_Q=\widetilde Q|_E=(2H-E)|_E.
\]
Therefore
\[
[S_Q]=(8,0)-(7,-1)=(1,1).
\]

So
\[
\boxed{S_Q=(1,1).}
\]

At the (3,4) boundary the horizontal components T_j of W have class
\[
[T_j]=(0,1).
\]
Using the P1xP1 intersection form,
\[
T_j.S_Q=(0,1).(1,1)=1.
\]
Thus every T_j meets S_Q in one reduced point when the intersection is transverse, and in total intersection multiplicity one in all cases.

## 2. Restriction of W to S_Q

At the boundary
\[
W=D.D'=\sum_jc_jT_j,
\qquad
\sum_jc_j=2pq.
\]
Therefore as an intersection divisor on S_Q,
\[
W|_{S_Q}=\sum_j c_jP_j,
\qquad P_j=T_j\cap S_Q,
\]
and
\[
\deg(W|_{S_Q})=2pq.
\]

This is the first natural divisor on the marked section that retains the sectionwise coefficients c_j.

## 3. Restricting the two exceptional divisors

At the boundary
\[
D|_E=(5p,p),\qquad D'|_E=(9q,q).
\]
Since S_Q=(1,1), their degrees on S_Q are
\[
D.S_Q=5p+p=6p,
\qquad
D'.S_Q=9q+q=10q.
\]

These degrees are not the residual-root degrees 2p and the mate fiber degree q. They include the full first-normal divisors on E, not merely their restrictions after removing the contribution associated with C on Q.

Thus one must not identify D|S_Q directly with R_F or D'|S_Q directly with R_G without accounting for the relevant line-bundle identifications and fixed factors.

## 4. Important coordinate issue

A root of
\[
R_F\in H^0(Q,O_Q(2p,0))
\]
selects a trisecant ruling fiber L in Q. That fiber meets C in a degree-three divisor.

By contrast a horizontal exceptional section T_j meets S_Q in one point P_j.

Therefore the statement “a ruling root corresponds to P_j” requires an explicit map between:
- the ruling-base P1 parameterizing trisecant fibers of Q;
- the base C=P1 of the exceptional bundle E;
- and the graph S_Q=(1,1).

For C=(1,3), the projection from C to the trisecant-ruling base has degree three. Hence a generic ruling root has three preimages on C.

This must be reconciled with the one-point intersection T_j cap S_Q before comparing
\[
\sum c_jP_j
\]
with the repeated-root divisor of R_F.

## 5. Consequence

The divisor W|S_Q is well-defined and retains the c_j coefficients, but a direct coefficient comparison c_j versus M_j is not yet justified.

The next calculation must write the explicit Segre parametrization
\[
C=[s^4:s^3t:st^3:t^4]
\]
as a (1,3)-curve on Q, identify both ruling projections, and identify the exceptional P1xP1 coordinates used in
\[
H|_E=(4,0),\qquad E|_E=(7,-1).
\]

Only after this coordinate dictionary is fixed can one decide whether a root of R_F gives one horizontal section, three marked points, or a ramified combination in W|S_Q.

This is a potentially important consistency check on the existing equality-root argument.
