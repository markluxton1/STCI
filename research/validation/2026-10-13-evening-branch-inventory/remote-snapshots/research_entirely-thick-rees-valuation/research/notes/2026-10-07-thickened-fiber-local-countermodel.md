# Entirely-thick boundary: local test of the thickened-fiber jet hypothesis

Date: 2026-10-07  
Status: **NEGATIVE RESULT — reduced STCI support does not constrain higher mate jets**

This note tests the open question at the end of \`2026-10-07-thickened-fiber-jets.md\`.

## 1. Local setup on the quadric

Let \(L\) be a ruling component of the residual divisor \(R_F\), occurring with multiplicity \(M\). Near a point of \(L\), choose regular coordinates \((x,y)\) on \(Q\) with
\[
L=(x=0).
\]
Let \(h=0\) cut out \(C\cap Q\). After removing units and other residual factors not vanishing generically on \(L\), write
\[
F|_Q=h^p x^M u
\]
with \(u\) a unit.

Write the mate as
\[
G|_Q=h^q R_G,
\]
and expand
\[
R_G=A_0(y)+xA_1(y)+\cdots+x^{M-1}A_{M-1}(y)+x^M B(x,y).
\tag{1}
\]

## 2. Reduced-support condition

Away from \(C\), \(h\) is a unit. The reduced zero set of \(F|_Q\) near \(L\) is then simply
\[
x=0,
\]
independently of the multiplicity \(M\).

Consequently an extra common point of \(F\) and \(G\) on \(Q\setminus C\) occurs exactly when
\[
x=0,\qquad A_0(y)=0
\]
at a point outside \(C\).

Thus the condition that the reduced common support on \(Q\) be contained in \(C\) imposes a condition only on
\[
R_G|_L=A_0(y).
\]
It imposes no condition on
\[
A_1,\ldots,A_{M-1}.
\]

### Proposition

Multiplicity \(M\) of a ruling component \(L\) in \(R_F\) does not, from reduced support alone, force any condition on the first \(M-1\) transverse jets of \(R_G\) along \(L\).

This remains true even though the reduced restriction \(R_G|_L\) must have all of its zeros supported on the degree-three divisor \(L\cap C\).

## 3. Explicit local family

Fix any admissible nonzero \(A_0(y)\) whose zero set is contained in \(L\cap C\). Then for arbitrary power series or polynomial coefficients
\[
A_1(y),\ldots,A_{M-1}(y),
\]
the pair
\[
F=h^p x^M,\qquad
G=h^q\left(A_0(y)+xA_1(y)+\cdots+x^{M-1}A_{M-1}(y)\right)
\]
has no additional reduced common point near \(L\setminus C\).

Hence there is an arbitrarily large family of higher mate jets with identical reduced-support behavior.

## 4. Consequence for the discrepancy calculation

The cokernel
\[
H^1(Q,O_Q(3q-2p,q))
\]
computed in the thickened-fiber note is a genuine interpolation discrepancy when \(2p>3q+1\), but reduced STCI support does not require \(R_G\) to hit a special point or subspace of the full thickened-fiber jet target.

Therefore that cokernel is **not an STCI obstruction by itself**.

The numerical coincidence
\[
h^0(O_Z(3q,q))=2p(q+1),\qquad v=2pq
\]
also has no established obstruction-theoretic meaning at this stage.

## 5. What survives from the quadric argument

The robust information is exactly zeroth order along each distinct ruling component:

1. \(R_F\) has at most \(\min(p,q)\) distinct ruling components.
2. Their multiplicities sum to \(2p\).
3. On each reduced component \(L_i\), every zero of \(R_G|_{L_i}\) is supported on \(L_i\cap C\).
4. Higher transverse jets of \(R_G\) are not controlled by reduced support.

Thus repeated-root multiplicity is a constraint on \(F\), but it does not automatically multiply the number of independent conditions imposed on \(G\).

## 6. Strategic consequence

This closes the simplest attempt to combine the repeated-root reduction with ordinary jet-discrepancy interpolation on \(Q\).

To exploit the multiplicities \(M_i\), one needs genuinely scheme-theoretic information beyond reduced support, for example:

- the sectionwise intersection coefficients \(c_i\) on the first exceptional surface;
- the local complete-intersection length along \(C\);
- integral closure/Rees valuations of the pair ideal;
- or normalization/conductor constraints.

The next promising calculation is therefore to relate \(M_i\) to the **sectionwise coefficient \(c_i\)** using local intersection multiplicity at the point \(T_i\cap S_Q\), not by trying to constrain higher jets of the mate from support alone.
