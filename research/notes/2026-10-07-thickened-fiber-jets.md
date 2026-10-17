# Entirely-thick boundary: thickened-fiber jet calculation

Date: 2026-10-07  
Status: **PROVED restriction-rank formula / OPEN STCI jet-incidence condition**

Let \(Q=P^1_x\times P^1_y\). The residual mate is
\[
R_G\in H^0(Q,O_Q(3q,q)).
\]
Let \(L_i\) be distinct fibers of the \(x\)-projection, with multiplicities \(M_i\) in
\[
R_F=\prod_i L_i^{M_i},\qquad \sum_i M_i=2p.
\]

## 1. Restriction to disjoint thickened fibers

Let
\[
Z=\sum_i M_iL_i.
\]
Since \(Z\) has class \((2p,0)\), there is an exact sequence
\[
0\to O_Q(3q-2p,q)\to O_Q(3q,q)\to O_Z(3q,q)\to0.
\tag{1}
\]

If \(3q-2p\ge-1\), then
\[
H^1(Q,O_Q(3q-2p,q))=0,
\]
so the restriction map
\[
H^0(Q,O_Q(3q,q))\to H^0(Z,O_Z(3q,q))
\]
is surjective.

More generally, the rank and cokernel are given exactly by the cohomology of (1).

## 2. Dimension of the full jet target

Each \(M_iL_i\) records \(M_i\) transverse coefficients, each a section of \(O_{P^1}(q)\). Therefore
\[
h^0(O_Z(3q,q))=(q+1)\sum_iM_i=2p(q+1).
\tag{2}
\]

When \(3q-2p\ge-1\), arbitrary transverse jets through order \(M_i-1\) can be prescribed independently on all repeated ruling fibers.

Thus repeated roots of \(R_F\) alone do not force special jets of \(R_G\).

## 3. Boundary in the p/q ratio

The automatic-surjectivity range is
\[
2p\le3q+1.
\tag{3}
\]

If \(2p>3q+1\), the thickened-fiber restriction map cannot be surjective. In fact the source has degree only \(3q\) in the transverse \(x\)-direction, so values on a divisor of degree \(2p\) satisfy interpolation relations.

This creates a genuine dichotomy inside the \((3,4)\) normalized boundary:

- **low-p regime** \(2p\le3q+1\): even the full repeated-root jets of the mate are freely interpolable;
- **high-p regime** \(2p>3q+1\): global transverse-degree relations appear.

The original first-stage inequality did not see this ratio.

## 4. Exact cokernel size in the high-p regime

Put
\[
m=2p-3q-1>0.
\]
Then \(3q-2p=-m-1\). Since \(q\ge0\),
\[
h^1(Q,O_Q(3q-2p,q))
=
h^1(P^1,O(-m-1))\,h^0(P^1,O(q))
=
m(q+1).
\]
Hence the thickened-fiber restriction map has cokernel dimension
\[
(2p-3q-1)(q+1).
\tag{4}
\]

This is a concrete discrepancy space.

## 5. Relation to the exceptional budget

The full thickened-fiber target has dimension \(2p(q+1)\), whose leading term is \(2pq\). The first exceptional higher-contact budget at \((3,4)\) is exactly
\[
v=2pq.
\]

The equality of leading terms is suggestive but not yet an identity: the jet target includes \(2p\) additional scalar degrees, and the intersection budget counts multiplicities rather than vector-space dimensions.

## 6. What is still missing

Reduced support of \(V(F,G)\) equal to \(C\) does **not** imply that \(R_G\) has prescribed values on the full thickening \(Z=\sum M_iL_i\). The calculation above only describes the ambient interpolation map.

To obtain an STCI obstruction one must prove that the support condition, proper-transform purity, or sectionwise Noether data forces the jet of \(R_G\) along \(M_iL_i\) into a proper incidence subset of
\[
H^0(M_iL_i,O(3q,q)).
\]

Without such a theorem, the discrepancy (4) is not an obstruction.

## 7. Next attack

The most promising place to derive that incidence condition is local at the length-three divisor
\[
L_i\cap C.
\]
Write the two residual equations on \(Q\) in coordinates transverse to \(L_i\), expand \(R_G\) through order \(M_i-1\), and impose that no branch of the complete intersection escapes \(C\).

This should determine whether the successive mate jets must have zeros supported on the same three-point divisor, or whether higher transverse coefficients are genuinely free. A local counterexample would settle the question just as usefully.
