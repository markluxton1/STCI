# Entirely-thick boundary: local pair model at a marked trisecant point

Date: 2026-10-07
Status: NEGATIVE LOCAL RESULT

Let L be a repeated trisecant ruling component of the residual divisor R_F on Q, and let P be one point of the degree-three divisor Z_L=C cap L.

This note asks whether retaining simultaneously
- the multiplicity M of L in R_F,
- the marked point P,
- the mate restriction on L,
- and the ambient Q-transverse coefficient
creates a local compatibility condition not visible in the earlier reduced-line analysis.

It does not, from reduced support alone.

## 1. Correct transverse local coordinates on Q

Since L and C meet transversely at a reduced point P in the generic trisecant case, choose regular parameters (u,y) on Q at P such that
\[
L=(u=0),\qquad C=(y=0).
\]

If L occurs with multiplicity M in R_F, then after removing units and residual factors not passing through P,
\[
F|_Q=y^p u^M\cdot \text{unit}.
\]

Write
\[
G|_Q=y^q R_G(u,y).
\]

## 2. What the support condition says

Along the reduced line L, the residual mate is
\[
R_G|_L=R_G(0,y).
\]

Suppose the exponent assigned to P in the divisor of R_G|_L is e. Locally the STCI support condition says only
\[
R_G(0,y)=y^e v(y),
\qquad v(0)\ne0.
\]

Globally on L, the three exponents e_1,e_2,e_3 at the points of C cap L satisfy
\[
e_1+e_2+e_3=q.
\]

Locally at P there is no further condition on the expansion
\[
R_G(u,y)
=
y^e v(y)
+uA_1(y)+u^2A_2(y)+\cdots.
\]

Thus all derivatives normal to L inside Q remain free, exactly as in the previous thickened-fiber countermodel.

## 3. Adding the ambient normal direction

Choose an ambient parameter z with Q=(z=0). Then locally one may write
\[
F=y^p u^M U + zA,
\]
and
\[
G=y^qR_G(u,y)+zB
\]
after choosing representatives, with U a unit in the displayed leading term.

The coefficient A is the transverse smoothing datum supplied globally by the Q-divisible kernel in the degree-3p recursion. Away from C it need not vanish along L.

The reduced common-support condition does not impose a relation between A and the coefficients A_j(y) in the u-expansion of R_G. If F is transversely smooth because A is a unit, the equation F=0 can locally eliminate z; substituting into G changes higher-order terms but does not alter the basic fact that extra reduced common points on L are governed by R_G(0,y).

Hence the ambient transverse coefficient does not rescue a local marked-point jet obstruction.

## 4. Three marked points do not change the local conclusion

For a generic trisecant
\[
C\cap L=P_1+P_2+P_3.
\]
The only global coupling visible on the reduced line is the degree condition
\[
e_1+e_2+e_3=q.
\]

For any fixed exponent triple, the earlier ruling interpolation audit proves that such reduced restrictions can be prescribed independently on all relevant distinct ruling fibers. The local expansions normal to each L remain unconstrained by reduced support.

Therefore keeping all three marked points still does not produce a new local compatibility equation.

## 5. Consequence

The smallest model containing
- repeated-root multiplicity M,
- the three marked points,
- mate zero allocation (e_1,e_2,e_3),
- and the Q-transverse smoothing coefficient of F
still has arbitrary higher local coefficients compatible with the reduced STCI support condition.

So the obstruction cannot be purely local at one trisecant line if it uses only reduced support.

## 6. What information is still missing

A surviving obstruction must import scheme-theoretic information that reduced support forgets. The candidates are now sharply narrowed to:

1. the actual complete-intersection multiplicity/Noether cluster of (F,G) over C;
2. variation and proximity of that cluster as the point of C moves;
3. a global divisor relation on successive exceptional surfaces;
4. normalization/conductor data of an actual carrier;
5. a relation imposed by the fact that F and G are global homogeneous equations, beyond their separately flexible restrictions.

The first item is the most immediate: compute the local pair ideal at P after the first blowup, retaining simultaneously the horizontal section T corresponding to L and the special point Ptilde=T cap S_Q. This is the first place where generic-along-T multiplicity and marked-point degeneration coexist in one two-dimensional family.
