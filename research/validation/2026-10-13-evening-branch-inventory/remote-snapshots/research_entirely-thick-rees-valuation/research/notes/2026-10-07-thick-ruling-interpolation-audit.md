# Entirely-thick (3,4) boundary: ruling-line interpolation audit

Date: 2026-10-07
Status: CORRECTION + PROVED interpolation calculation / NO NEW EXCLUSION

## 1. Correction to the marked-point note

The previous continuation incorrectly strengthened the ruling-line condition to a pure q-th power at a single point.

With the convention C=(1,3) on Q=P1 x P1, the ruling components of R_F in class (2p,0) are trisecant ruling lines. A relevant line L meets C in a degree-three divisor
    Z_L = L intersect C.
Therefore the STCI support condition implies only that the zero divisor of
    R_G|L in H0(L,O(q))
is supported on Z_L. It need not be concentrated at one point.

If Z_L consists of three distinct points P1,P2,P3, then projectively the allowed nonzero restrictions are
    lambda * l1^e1 l2^e2 l3^e3,
    e1+e2+e3=q,
with finitely many exponent triples. Degenerate trisecant fibers are handled by the corresponding length-three divisor; the same conclusion is that the allowed restrictions form a finite union of one-dimensional vector subspaces after the support points are fixed.

Thus the previous pure-power assertion should not be used.

## 2. Exact restriction rank on distinct ruling fibers

Write
    R_G in H0(Q,O(3q,q)).
Let L_1,...,L_r be distinct fibers of the ruling containing the components of R_F.

The simultaneous restriction map
    H0(Q,O(3q,q)) -> direct_sum_i H0(L_i,O(q))
is surjective whenever r <= 3q+1.

Proof: factor the section space as
    H0(P1,O(3q)) tensor H0(P1,O(q)).
Restriction to r distinct fibers is evaluation of the first factor at r distinct points, tensored with the identity on the second factor. Evaluation
    H0(P1,O(3q)) -> k^r
is surjective for r <= 3q+1.

On the (3,4) boundary the audited bound gives
    r <= min(p,q) <= q < 3q+1.
Hence all ruling-line restrictions can be prescribed independently.

## 3. Codimension of the support condition

For a fixed exponent choice on each trisecant fiber, the allowed restriction on L_i is a one-dimensional vector subspace of the (q+1)-dimensional H0(O_Li(q)). It therefore imposes q independent linear conditions.

Because the simultaneous restriction map is surjective, r fixed exponent choices impose exactly
    r q
linear conditions on R_G.

Allowing all exponent triples produces a finite union of such codimension-rq linear subspaces. It does not change the dimension.

Since
    h0(Q,O(3q,q))=(3q+1)(q+1),
and r<=q, these conditions are far from exhausting the available section space.

Therefore a dimension count based only on the restrictions of R_G to the ruling components of R_F cannot exclude the (3,4) boundary.

## 4. Multiplicity M_i of a component of R_F does not strengthen this restriction

If
    R_F = product_i L_i^{M_i},  sum M_i=2p,
the support condition on the reduced ruling line L_i depends only on L_i, not on M_i. Repeating L_i in R_F does not create additional independent restrictions on R_G|L_i.

To exploit M_i one must use higher transverse jets of R_G along L_i, not merely its restriction to L_i.

This is the key structural conclusion of the interpolation audit.

## 5. Correct next object: jets normal to the ruling line

A multiplicity-M_i component L_i^{M_i} in R_F supplies a thickened ruling line in the residual divisor of F on Q. The natural next map is therefore not
    R_G -> R_G|L_i,
but restriction to an infinitesimal neighborhood
    R_G -> R_G|_{M_i L_i}
or, equivalently, the first M_i-1 normal derivatives along L_i.

The STCI support condition should constrain the zero schemes of these transverse jets because F vanishes to higher order along L_i.

This is exactly where the jet-condition/discrepancy framework can interact nontrivially with the entirely-thick branch.

## 6. Numerical reason this may matter

The multiplicities satisfy
    sum_i M_i=2p
while r<=min(p,q).

Restriction to reduced fibers costs only rq conditions. A full M_i-jet prescription would scale instead like
    q * sum_i M_i = 2pq,
which is exactly the scale of the first exceptional Noether budget
    v=2pq.

This numerical coincidence is potentially structural:
    total repeated-root multiplicity x mate fiber degree = 2p*q = v.

It is not yet a theorem. But it identifies the first higher-jet calculation whose natural condition count lives on the same scale as the entire exceptional intersection budget.

## 7. Next target

Compute the restriction map
    H0(Q,O(3q,q)) -> H0(M_i L_i, O(3q,q)|_{M_i L_i})
for disjoint ruling fibers and determine precisely which transverse jets are forced by the STCI support condition, rather than merely by F vanishing on L_i^{M_i}.

The map itself is standard interpolation. The hard point is identifying the correct support/incidence condition on the mate jets. Any claim that all M_i jets are prescribed would require proof and must not be inferred from reduced support alone.
