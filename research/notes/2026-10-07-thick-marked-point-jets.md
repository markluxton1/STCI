# Entirely-thick (3,4) boundary: marked-point jets versus section budgets

Date: 2026-10-07
Status: PROVED separation of invariants / OPEN coupling problem

## 1. Two different invariants

On the first exceptional surface E, fix a constant common section T and let P=T intersect S_Q, where S_Q is the quadric-direction section.

Let r=ord_T(D|E). This is a divisorial multiplicity: it records whether the entire section T is a component of the first exceptional divisor and with what multiplicity.

Let M_T be the multiplicity at the corresponding ruling root of the residual binary form R_F. Equivalently, M_T is a vanishing order at the marked point P of the restriction of the p-th normal form to S_Q.

These are different kinds of data:
- r is generic along T;
- M_T is a jet order at one point P on the transverse moving section S_Q.

There is no formal inequality r >= M_T.

## 2. Local countermodel to naive coupling

Use regular local coordinates (x,z) on E near P with S_Q=(z=0) and T transverse to S_Q. A function
    A=z+x^M
has restriction
    A|S_Q=x^M,
so its marked-point restriction has order M, while A is not divisible by a local equation of T for a suitable transverse choice of T.

Thus arbitrarily high marked-point vanishing can occur without high divisorial multiplicity along T.

Therefore the hoped-for route
    M_T large => r large => c_T large
is invalid without additional global structure.

## 3. Consequence for the repeated-root argument

The audited repeated-root theorem remains useful, but only as a marked-point jet constraint:
    sum_T M_T = 2p,
with at most min(p,q) marked points.

It cannot by itself be inserted into the sectionwise Noether budget
    sum_T c_T = 2pq.

Any inequality c_T >= Phi(M_T,...) must use information beyond local smooth-surface intersection theory.

## 4. Where coupling can come from

The quadric Q supplies extra global structure. The marked point P is not arbitrary: it is the intersection of T with S_Q, and the residual ruling line associated to P is globally contained in V(F). The STCI condition then forces all zeros of G on that ruling line back onto C.

Hence the promising object is not M_T alone, but the restriction of G (and possibly higher transforms of F,G) to the corresponding ruling line L_T subset Q.

For a root of multiplicity M_T in R_F, F|Q contains L_T with multiplicity M_T in the residual factor. Meanwhile
    G|L_T = (h|L_T)^q (R_G|L_T)
and R_G|L_T is a degree-q section whose zeros must all lie at L_T intersect C. Since that intersection is a single point with multiplicity three for the trisecant ruling convention, the support condition forces R_G|L_T to be supported at that same point.

This converts the earlier existence-of-a-zero argument into a stronger one-variable restriction problem.

## 5. Next exact question

Determine the possible section R_G|L_T in H^0(L_T,O(q)) under the condition that every zero is supported at P=L_T intersect C.

Over an algebraically closed field this forces
    R_G|L_T = lambda * ell_P^q
for some nonzero scalar lambda,
unless R_G|L_T is identically zero.

Thus on every ruling component L_T of R_F, the mate residual restricts to a pure q-th power at the distinguished point.

This is a substantial sharpening of the existing repeated-root statement.

## 6. New target

Exploit the simultaneous conditions
    R_F = product_i L_i^{M_i},  sum M_i=2p,
and
    R_G|L_i = lambda_i ell_{P_i}^q  or 0
for at most min(p,q) distinct ruling lines L_i.

Since R_G has bidegree (3q,q), these pure-power restrictions are interpolation conditions on a single global section of O_Q(3q,q).

The next calculation is therefore finite-dimensional and global on Q:
compute the codimension/rank of the restriction map from H^0(O_Q(3q,q)) to the jets on the selected ruling lines, allowing the zero restriction case, and compare it with the freedom in choosing the roots of R_F.

This reconnects the entirely-thick branch to the project's jet-condition/discrepancy framework.
