# e=2 quartic incidence: first exact compression and chart stratification

Date: 2026-10-05

## Status

**EXACT COMPUTATION / COMPUTATIONAL CROSS-CHECK.** This note does not classify the quartic-incidence locus and does not eliminate the characteristic-zero (4,7), e=2 branch.

## Direct quartic basis

For a degree-four monomial with exponent vector (i0,i1,i2,i3), restriction to (1,z,z^3,z^4) is z^(i1+3i2+4i3). The 35 monomials have 17 distinct weights, hence the kernel has dimension 18.

The verifier chooses differences of equal-weight monomials. In the notation (weight; exponent; reference exponent), the basis is:

    (3;(3,0,1,0);(1,3,0,0))
    (4;(2,1,1,0);(0,4,0,0))
    (4;(3,0,0,1);(0,4,0,0))
    (5;(2,1,0,1);(1,2,1,0))
    (6;(1,2,0,1);(0,3,1,0))
    (6;(2,0,2,0);(0,3,1,0))
    (7;(1,1,2,0);(0,3,0,1))
    (7;(2,0,1,1);(0,3,0,1))
    (8;(1,1,1,1);(0,2,2,0))
    (8;(2,0,0,2);(0,2,2,0))
    (9;(1,0,3,0);(0,2,1,1))
    (9;(1,1,0,2);(0,2,1,1))
    (10;(0,2,0,2);(0,1,3,0))
    (10;(1,0,2,1);(0,1,3,0))
    (11;(1,0,1,2);(0,1,2,1))
    (12;(0,1,1,2);(0,0,4,0))
    (12;(1,0,0,3);(0,0,4,0))
    (13;(0,1,0,3);(0,0,3,1))

Thus h^0(I_C(4))=18 is reproduced directly without using a preselected generating set.

## Canonical triple and matrices

Use A=x+az+z^2, B=1+bz+dz^2 and Delta=1-ab+a^2d-2dx+b^2x-abdx+d^2x^2. With the exact Bezout pair sA+tB=1, the canonical triple is u=A eps-t gamma_U eps^2 and v=B eps+s gamma_U eps^2 in the checked moving coordinates.

The general gamma_U was independently reconstructed from the moving transition. Its specialization to a=-1/2, b=-2, d=x^(-1) agrees identically with the independently audited P-045 formula.

For each basis quartic F_j, write F_j|C3 = J_1j eps + J_2j eps^2 mod eps^3. Both jet polynomials have degree at most 14. Multiplication of the second jet by Delta clears its parameter denominator on D(Delta). Coefficient comparison gives two 15 x 18 exact matrices M^(1) and M^(2), hence a 30 x 18 stacked matrix.

## Generic rank and a concrete six-dimensional chart

At (x,a,b,d)=(2,3,5,7), Delta=57, exact ranks are rank M^(1)=12 and rank stacked=18. The same ranks occur at the exact rational basepoint-free points (1,2,-1,3), (3,-2,4,1), and (2/3,1,2,-1). At all four points the induced second-order map on ker M^(1) has rank 6.

Using generic pivot columns (0,1,2,3,4,5,6,8,10,13,14,16) and coefficient rows 0,...,11, the 12 x 12 first-order pivot minor factors exactly as

    det P = d^7 (b+2) Delta / 128.

Hence on D(d(b+2)Delta) one has the explicit rational kernel parametrization N=(-P^(-1)Q; I_6), after ordering pivot and free columns, and reduced obstruction R=M^(2)N.

The symbolic entries of R have not yet been promoted to durable formula data. The next calculation should fraction-free reduce this R, factor its entries/minors, and seek a small rank certificate.

## P-045 is a lower first-order rank stratum

For P-045, a=-1/2, b=-2, d=x^(-1). The displayed rank-12 chart degenerates because b+2=0, but this is not merely a bad pivot choice. At x=1/2,1,2,3,-1 the verifier obtains rank M^(1)=11. Thus quartics containing C2 form a seven-dimensional space on P-045, not the generic six-dimensional space.

On that seven-dimensional kernel the second-order map has rank 3, so the full stacked rank is 14 and h^0(I_C3(4))=4. As a stronger symbolic regression, the verifier checks over Q(x) that H_x x_0, H_x x_1, H_x x_2, H_x x_3 have zero first and second jets on the canonical triple.

Therefore H^0(I_C3(4)) != 0 iff ker R != 0 for a fixed 18 x 6 kernel matrix is only a chartwise statement on the rank-12 locus. The full incidence locus must also include lower-rank strata of M^(1), beginning with P-045.

## Consequence for P-044 intersection

The target remains V(G_1,...,G_5) intersect quartic incidence intersect D(Delta), but computation should be stratified: (1) on rank M^(1)=12 use six-dimensional kernel charts and reduced R; (2) analyze rank M^(1)<=11 separately. P-045 lies in the second stratum and is already geometrically excluded by P-045.

This prevents saturation by a generic kernel-chart denominator from accidentally deleting the known P-045 component or another genuine lower-rank component.

## Reproducibility and epistemic status

Durable verifier: research/computations/verify_e2_quartic_incidence.py.

- 18-dimensional quartic basis: **EXACT COMPUTATION**.
- Generic/sample ranks: **EXACT COMPUTATION** at the stated fibers.
- Pivot determinant d^7(b+2)Delta/128: **EXACT COMPUTATION**.
- P-045 ranks and symbolic H_x x_i containment: **COMPUTATIONAL CROSS-CHECK** of P-045.
- Global quartic-incidence classification: **OPEN**.
- Elimination of the full e=2 branch: **OPEN**.

No theorem-level claim is promoted here.


## 7. Sharpening on the dx=1 test bed

**EXACT COMPUTATION.** Restricting the same rank-12 pivot minor to (d=x^{-1})
gives
[
det P=rac{(bx-a)^2(b+2)}{128x^8}.
]
On this slice
[
Delta=rac{(bx-a)^2}{x}.
]
Therefore, on the basepoint-free locus, (x
e0) and (bx-a
e0), and this
single six-dimensional kernel chart covers every point with (b
e-2).

Consequently the combined P-044/quartic-incidence problem on (dx=1) has a
particularly clean stratification:

1. (b
e-2): use the single rank-12 chart and its reduced (6)-column
   second-order obstruction;
2. (b=-2): analyze the lower-rank/boundary behavior separately.  The known
   P-045 family lies on this divisor.

This does **not** prove that every point of (b=-2) has first-order rank 11,
nor that P-045 exhausts the P-044 locus there.  Those statements remain
**OPEN** until separately computed.

A direct attempt to symbolically factor a full (6	imes6) reduced minor was
stopped because expression growth became severe even after the (dx=1)
restriction.  No determinant or factorization from that interrupted
calculation is being reported.  The next implementation should use
fraction-free polynomial linear algebra or modular evaluation/reconstruction,
rather than expanding rational SymPy determinants.
