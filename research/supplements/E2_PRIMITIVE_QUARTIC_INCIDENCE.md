# E2 obstruction, primitive structures, and quartic incidence

Consolidated mathematical source material. Sections retain original claims, calculations, hypotheses, and qualifications; their inclusion does not upgrade unverified arguments to theorems.

---

## 2026-10-05-e2-full-obstruction

# e=2 quartic-carrier obstruction: stabilizer, generic cross-section, and surviving family

Date: 2026-10-05

Status: **characteristic-zero continuation**. The ambient-stabilizer statement and the three-parameter exclusion are PROVED; the full four-parameter obstruction formulas are an exact computational result with strong cross-checks, including exact specialization checks. The explicit surviving family and the resulting falsification of the universal cubic exclusion are independently reconstructed and verified. Nothing here constructs a quartic carrier or an STCI presentation.

Throughout,
[
C_0=[s^4:s^3t:st^3:t^4]subsetmathbf P^3.
]

## 1. Ambient stabilizer — PROVED

The embedding linear system is
[
W=langle s^4,s^3t,st^3,t^4anglesubset H^0(O_{mathbf P^1}(4)).
]
In characteristic zero the only (PGL_2) transformations preserving (W) are
[
zmapstolambda z,qquad zmapstolambda/z.
]
The kernel of
[
operatorname{Stab}_{PGL_4}(C_0)	ooperatorname{Aut}(mathbf P^1)
]
is trivial. Hence
[
oxed{operatorname{Stab}_{PGL_4}(C_0)congmathbf G_mtimesmathbf Z/2.}
]
In the formal coordinates used below the torus acts by
[
zmapstolambda z,qquad Umapstolambda^4U,qquad Vmapstolambda^3V.
]
There is no hidden continuous ambient symmetry reducing a general (e=2) quotient to the earlier two-parameter family.

## 2. Generic e=2 symmetry cross-section

On (A_2B_0
e0), projective scaling plus the genuine ambient torus normalize a general (e=2) quotient to
[
oxed{A=x+az+z^2,qquad B=1+bz+dz^2.}
]
This is a generic cross-section to the actual symmetry, **not literally an affine chart of (P^5)**.

The resultant is
[
oxed{Delta=1-ab+a^2d-2dx+b^2x-abdx+d^2x^2.}
]
Basepoint-free is equivalent to (Delta
e0).

On (xd
e0), inversion acts by
[
oxed{(x,a,b,d)mapstoleft(rac{x}{d^2},rac ad,rac bx,rac d{x^2}ight).}
]
Thus the previously studied (x=b=0) family is codimension two in the essential generic moduli.

## 3. Formal-neighborhood audit — independently audited

The nonlinear two-chart transition was independently reconstructed. A crucial point is
[
oxed{w
e1/z}
]
off the reduced curve. Freezing (w=1/z) destroys higher-order information contributing to the obstruction. Calculations using a frozen opposite-chart coordinate must not be reused unless separately corrected.

Several exploratory slice/factorization claims from the research conversation were discarded during this audit and are not promoted here.

## 4. Three-parameter b=0 family — PROVED

For
[
A=x+az+z^2,qquad B=1+dz^2,
]
put
[
Delta_0=1+a^2d-2dx+d^2x^2.
]
The quadratic graph corrections and all five cubic obstruction numerators (G_i(a,d,x)) were independently regenerated. Exact Gröbner reduction gives
[
oxed{Delta_0in(G_1,ldots,G_5).}
]
Consequently
[
G_1=cdots=G_5=0LongrightarrowDelta_0=0.
]
Hence no basepoint-free member of this entire three-parameter family extends from the relevant primitive triple to a primitive quadruple. This strictly strengthens the earlier (x=b=0) result.

## 5. Full four-parameter cubic obstruction — exact computation with strong cross-checks

For
[
A=x+az+z^2,qquad B=1+bz+dz^2,
]
the cubic mismatch has form
[
M_3=rac{N(z;x,a,b,d)}{32z^{25}Delta^3}.
]
The five relevant coefficients of (N) are each exactly divisible by (Delta^2). Therefore
[
oxed{Omega_i=rac{G_i(x,a,b,d)}{32Delta},qquad i=1,ldots,5.}
]
The exact (G_i) are persisted in
`../computations/e2_full4_obstruction_2026-10-05.txt`.

Exact checks:
- (b=0) reproduces all five independently audited three-parameter obstruction polynomials;
- (x=b=0) reproduces the retained two-parameter obstruction polynomials.

## 6. Universal cubic e=2 exclusion — FALSE

The attempted implication
[
oxed{Omega=0LongrightarrowDelta=0}
]
is **FALSE**.

On (dx=1), write (u=bx-a). Then
[
Delta=rac{u^2}{x}
]
and all five obstruction numerators factor as (G_i=uQ_i). On
[
a=-rac12,
]
all five original (G_i) vanish when
[
u=rac12-2x,
]
equivalently (b=-2). Thus
[
oxed{A=z^2-rac12z+x,qquad B=1-2z+rac1xz^2}
]
satisfies
[
oxed{G_1=cdots=G_5=0.}
]
Its resultant is
[
oxed{Delta=rac{(4x-1)^2}{4x}.}
]
For (x
e0,rac14), the pair is basepoint-free. Therefore the corresponding (e=2) primitive triple extends to a primitive quadruple.

This falsifies the proposed universal **first nontrivial extension-obstruction strategy**. It does not construct a quartic carrier.

## 7. Scope and revised frontier

Do **not** infer:
- existence of an (e=2) quartic carrier;
- existence of an STCI presentation;
- failure of the desired no-quartic-carrier theorem for (C_0);
- failure of the global STCI conjecture.

The surviving family proves only that the first nontrivial extension obstruction is insufficient.

The immediate (e=2) question is:

> Exactly what infinitesimal multiplicity/order does a genuine (e=2) quartic carrier force, and does the explicit surviving primitive quadruple extend through the next required stage?

The sharp test family is
[
A=z^2-rac12z+x,qquad B=1-2z+x^{-1}z^2.
]

Continued higher-order (e=2) computation is not automatically the highest-value global strategy. Other live branches remain:
- equivariance/representation-theoretic interpretation of (Omega);
- (e=1);
- (e=0);
- whether the local-cohomology route can treat (e=0,1,2) uniformly.

All formal calculations in this note currently carry the characteristic-zero caveat.


---

## 2026-10-05-e2-primitive-septuple

# Primitive-septuple theorem for the (4,7), e=2 branch

Date: 2026-10-05

## Status

**PROVED / INDEPENDENTLY AUDITED (characteristic zero).**

This note records the structural consequence of an actual complete-intersection
carrier. It is independent of the classification of the P-044 obstruction
zero locus.

Let
\[
C=C_0=[s^4:s^3t:st^3:t^4]\subset \mathbf P^3
\]
and suppose
\[
Y=V(F_4,G_7),\qquad Y_{\mathrm{red}}=C,
\]
is a characteristic-zero complete intersection whose quasiprimitive
Bănică--Forster branch has \(e=2\).

## Theorem

Then \(Y\) is a globally primitive multiplicity-seven structure of type
\[
L=O_{\mathbf P^1}(-5).
\]
If the Bănică--Forster graded pieces are
\[
E_i=L^i(D_i),\qquad i=0,\ldots,6,
\]
then
\[
D_2=D_3=D_4=D_5=D_6=0.
\]

Moreover, writing
\[
M=\ker(N_C^*\twoheadrightarrow L),
\]
one has
\[
M=O_{\mathbf P^1}(-9)
\]
and the primitive complete-intersection conormal sequence is
\[
0\longrightarrow L^7
\longrightarrow O_C(-4)\oplus O_C(-7)
\longrightarrow M\longrightarrow0.
\]
Thus its kernel is naturally
\[
K\simeq L^7=O_{\mathbf P^1}(-35).
\]

Consequently every genuine \((4,7),e=2\) carrier determines a basepoint-free
P-044 zero, and its quartic generator contains the corresponding canonical
primitive triple \(C_3\).

## Proof

For a smooth rational quartic in characteristic zero,
\[
N_C^*\simeq O_{\mathbf P^1}(-7)^2.
\]
The \(e=2\) quotient is therefore
\[
N_C^*\twoheadrightarrow L,\qquad L=O_{\mathbf P^1}(e-7)=O(-5).
\]

The complete intersection has degree \(4\cdot7=28\). Since \(\deg C=4\),
its generic multiplicity along \(C\) is seven. Its arithmetic genus is
\[
p_a(Y)=1+\frac{4\cdot7(4+7-4)}2=99,
\]
hence
\[
\chi(O_Y)=-98.
\]

For a quasiprimitive multiplicity-seven curve, the Bănică--Forster
Cohen--Macaulay filtration has line-bundle quotients
\[
E_i=L^i(D_i),
\]
where \(D_1=0\) and the defect divisors \(D_i\) are effective. Additivity in
the filtration gives
\[
\chi(O_Y)=\sum_{i=0}^6\chi(E_i).
\]
Since \(C\simeq\mathbf P^1\) and \(L=O(-5)\),
\[
\chi(E_i)=1-5i+\deg D_i.
\]
Therefore
\[
-98
=7-5(1+\cdots+6)+\sum_{i=2}^6\deg D_i
=-98+\sum_{i=2}^6\deg D_i.
\]
Thus
\[
\sum_{i=2}^6\deg D_i=0.
\]
Effectivity forces
\[
D_2=\cdots=D_6=0.
\]
In the Bănică--Forster quasiprimitive filtration these defects measure exactly
the isolated failure of primitivity, so their vanishing makes \(Y\) globally
primitive.

The determinant of
\[
0\to M\to O(-7)^2\to O(-5)\to0
\]
gives
\[
M=O(-9).
\]
For a primitive multiplicity-seven extension, the standard primitive conormal
sequence (Bănică--Forster, Proposition 2.3 in the convention audited for this
project) gives
\[
0\to L^7\to \nu_Y|_C\to N_C^*\to L\to0.
\]
Because \(Y=(F_4,G_7)\),
\[
\nu_Y|_C=O_C(-4)\oplus O_C(-7)
       =O_{\mathbf P^1}(-16)\oplus O_{\mathbf P^1}(-28).
\]
Its image in \(N_C^*\) is \(M\), yielding
\[
0\to L^7\to O_C(-4)\oplus O_C(-7)\to M\to0.
\]
Hence
\[
K\simeq L^7=O(-35).
\]

Finally a primitive septuple has canonical primitive truncations
\[
C=C_1\subset C_2\subset C_3\subset C_4\subset\cdots\subset C_7=Y
\]
associated with the same quotient \(N_C^*\twoheadrightarrow L\). Therefore its
canonical triple extends to a primitive quadruple, so its quotient parameters
are a basepoint-free P-044 zero. The actual quartic \(F_4\) contains \(Y\), and
therefore contains \(C_3\).

## First-normal kernel warning

Before global primitivity or first-normal surjectivity is known, one must not
use
\[
\deg K=e-4b-9
\]
unconditionally. If the first-normal pair has common-zero/cokernel divisor
\(A\), the image is \(M(-A)\), and determinant bookkeeping gives
\[
\boxed{\deg K=e-4b-9+\deg A.}
\]
Only after \(A=0\) is established does the simpler formula apply. For the
present primitive \((4,7),e=2\) structure it gives \(\deg K=-35\).

In particular, do not argue that a named septic lies in \(I_C^2\), or that one
named first-normal section is individually nowhere zero. Locally one may have
\[
F=x,\qquad G=ax+y^7.
\]
The pair generates the complementary conormal line.

## Separate audited calculation: cubics through the double

This calculation is useful for stratification but is **not** a consequence of
the primitive-septuple theorem.

On \(x_0=1\), with moving coordinates
\[
x_1=z,\qquad x_2=z^3+v,\qquad
x_3=z^4+u+\frac32zv,
\]
the first jets are
\[
[q]=u+\frac12zv,\qquad [A_3]=v,
\]
\[
[B_3]=-z^2u+\frac12z^3v,\qquad [D_3]=-2z^5u.
\]
For a double defined by
\[
u=A(z)\epsilon,\qquad v=B(z)\epsilon
\]
and a cubic
\[
H=\ell q+\alpha A_3+\beta B_3+\gamma D_3,
\]
the condition that \(H\) contain the double is
\[
A(z)(\ell-\beta z^2-2\gamma z^5)
+B(z)\left(\frac12z\ell+\alpha+\frac12\beta z^3\right)=0.
\]

For
\[
A=z^2+az+x,\qquad B=1+bz+dz^2,
\qquad
\ell=\lambda_0+\lambda_1z+\lambda_2z^3+\lambda_3z^4,
\]
this is the rank-drop condition for
\[
M_2=
\begin{pmatrix}
x&0&0&0&1&0&0\\
a+\frac12&x&0&0&b&0&0\\
1+\frac b2&a+\frac12&0&0&d&-x&0\\
\frac d2&1+\frac b2&x&0&0&\frac12-a&0\\
0&\frac d2&a+\frac12&x&0&\frac b2-1&0\\
0&0&1+\frac b2&a+\frac12&0&\frac d2&-2x\\
0&0&\frac d2&1+\frac b2&0&0&-2a\\
0&0&0&\frac d2&0&0&-2
\end{pmatrix},
\]
with columns
\[
(\lambda_0,\lambda_1,\lambda_2,\lambda_3,\alpha,\beta,\gamma).
\]
Thus
\[
H^0(I_{C_2}(3))\ne0\iff \operatorname{rank}M_2<7.
\]
For the explicit P-044 survivor
\[
a=-\frac12,\qquad b=-2,\qquad d=x^{-1},
\]
the kernel is generated by
\[
(-4x^3,8x^3,-2x,4x,4x^4,4x^2,1),
\]
recovering the P-045 cubic.

**OPEN:** there is no theorem that a genuine \((4,7),e=2\) carrier must satisfy
this cubic rank drop. Do not impose it as a carrier equation without a separate
proof.

## Consequence for the frontier

Every genuine \((4,7),e=2\) carrier must satisfy both
\[
\text{P-044}=0
\]
and
\[
H^0(I_{C_3}(4))\ne0.
\]
These conditions are necessary, not sufficient: quartic containment of
\(C_3\) does not by itself prove compatibility through \(C_4,\ldots,C_7\).

The immediate \(e=2\) task is therefore to derive the general algebraic
incidence condition
\[
H^0(I_{C_3(A,B)}(4))\ne0
\]
in the moving \(e=2\) coordinates and intersect it with the basepoint-free
P-044 obstruction locus before attempting unrestricted P-044 saturation or
higher primitive obstructions.


---

## 2026-10-05-e2-quartic-incidence

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


---

## 2026-10-05-p044-survivor-cubic

# P-044 survivor family: cubic carrier obstruction

Date: 2026-10-05

## Status

**PROVED / INDEPENDENTLY AUDITED (characteristic zero).**

This note concerns only the explicit basepoint-free P-044 survivor family. It
does **not** classify the full P-044 zero locus and does **not** exclude the
entire \(e=2\) branch.

Let
\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3
\]
and write
\[
q=x_0x_3-x_1x_2,\quad
A_3=x_0^2x_2-x_1^3,\quad
B_3=x_0x_2^2-x_1^2x_3,\quad
D_3=x_2^3-x_1x_3^2.
\]
For
\[
A=z^2-\tfrac12z+x,\qquad
B=1-2z+x^{-1}z^2,\qquad x\ne0,\tfrac14,
\]
let \(C_3(x)\) be the canonical primitive triple obtained from the moving
coordinate P-044 construction.

Define
\[
\boxed{
H_x=D_3+4x^2B_3+4x^4A_3+
(-4x^3x_0+8x^3x_1-2xx_2+4xx_3)q.}
\]

## Theorem

For every allowed specialization \(x\ne0,\tfrac14\):

1. \(H_x\in H^0(I_{C_3(x)}(3))\).
2. \(H_x\) is irreducible.
3.
   \[
   H^0(I_{C_3(x)}(4))=H_xH^0(O_{\mathbf P^3}(1)),
   \qquad h^0(I_{C_3(x)}(4))=4.
   \]
4. Consequently this P-044 survivor family cannot be induced by the quartic
   member of a characteristic-zero \((4,7)\) STCI presentation of \(C_0\).

No exhaustion of the full P-044 zero locus is used.

## 1. Exact primitive-triple containment

On \(x_0=1\), the formal coordinates used by P-044 are
\[
x_2=z^3+v,\qquad x_3=z^4+u+\tfrac32zv.
\]
The opposite parameter is
\[
w=\frac{z^3+v}{z^4+u+\tfrac32zv},
\]
so \(w=1/z\) only modulo the normal ideal.

A Bezout identity \(sA+tB=1\) is
\[
s=\frac{2(2x-z)}{x(4x-1)},\qquad
t=\frac{2z-1}{4x-1}.
\]
The audited moving-coordinate calculation gives the canonical triple
\[
u=A\epsilon-t\gamma_U\epsilon^2,\qquad
v=B\epsilon+s\gamma_U\epsilon^2
\pmod{\epsilon^3},
\]
where
\[
\gamma_U=
-\frac{
8x^3+16x^2z^2-18x^2z+4x^2
-12xz^3+8xz^2+3z^4
}{8x^3}.
\]
Thus
\[
\begin{aligned}
x_0&=1,\quad x_1=z,\\
x_2&=z^3+B\epsilon+s\gamma_U\epsilon^2,\\
x_3&=z^4+(A+\tfrac32zB)\epsilon+
(-t+\tfrac32zs)\gamma_U\epsilon^2.
\end{aligned}
\]
Exact substitution gives
\[
[\epsilon^0]H_x=[\epsilon^1]H_x=[\epsilon^2]H_x=0.
\]
The identity is in the localization
\[
\mathbf Q[x,x^{-1},(4x-1)^{-1},z]
\]
(with powers of \(2\) inverted), exactly matching the allowed parameter range.

As an independent linear-algebra check, every cubic through \(C_0\) is
\[
\alpha A_3+\beta B_3+\gamma D_3+
q(\lambda_0x_0+\lambda_1x_1+\lambda_2x_2+\lambda_3x_3).
\]
Imposing vanishing through order \(\epsilon^2\) gives a one-dimensional kernel
generated by
\[
(\alpha,\beta,\gamma,\lambda_0,\lambda_1,\lambda_2,\lambda_3)
=(4x^4,4x^2,1,-4x^3,8x^3,-2x,4x),
\]
which is exactly \(H_x\).

The next coefficient is generically nonzero, so the cubic generically contains
the canonical triple but not the canonical quadruple. This extra fact is not
used in the theorem.

## 2. Irreducibility

The curve \(C_0\) is nonplanar, and direct coefficient comparison after the
parametrization shows
\[
h^0(I_{C_0}(2))=1,
\]
generated by \(q\).

If \(H_x\) were reducible, primality of \(I(C_0)\) would force a proper factor
of degree \(1\) or \(2\) to contain \(C_0\). A linear factor is impossible by
nonplanarity; a quadratic factor must therefore be proportional to \(q\).

But modulo \(q\),
\[
H_x\equiv D_3+4x^2B_3+4x^4A_3.
\]
On the line of \(V(q)\)
\[
[x_0:x_1:x_2:x_3]=[1:0:T:0],
\]
this becomes
\[
T^3+4x^2T^2+4x^4T=T(T+2x^2)^2,
\]
whose leading coefficient is \(1\). Hence it is never identically zero and
\(q\nmid H_x\). Thus \(H_x\) is irreducible for every allowed specialization.
The argument is fiberwise and leaves no exceptional allowed \(x\).

## 3. Hilbert polynomial of the primitive triple

For this \(e=2\) primitive triple,
\[
\operatorname{gr}O_{C_3}=O_C\oplus L\oplus L^2,
\qquad L=O_{\mathbf P^1}(-5),
\]
and \(O_C(1)=O_{\mathbf P^1}(4)\). Hence
\[
\chi(O_C(n))=4n+1,\quad
\chi(L(n))=4n-4,\quad
\chi(L^2(n))=4n-9.
\]
Therefore
\[
P_{C_3}(n)=12n-12,
\]
so
\[
\deg C_3=12,\qquad \chi(O_{C_3})=-12,\qquad p_a(C_3)=13.
\]
The primitive local model is curvilinear, hence \(C_3\) is locally
Cohen--Macaulay and pure of dimension one.

## 4. Divisibility of every containing quartic

Let \(F\in H^0(I_{C_3}(4))\). Suppose \(H_x\nmid F\). Since \(H_x\) is
irreducible, \(H_x,F\) form a proper complete intersection
\[
Y=V(H_x,F)
\]
of type \((3,4)\). Thus
\[
\deg Y=12,\qquad p_a(Y)=19,\qquad \chi(O_Y)=-18.
\]
Scheme containment \(C_3\subseteq Y\) gives
\[
0\to K\to O_Y\to O_{C_3}\to0.
\]
The two schemes have the same degree, so Hilbert-polynomial additivity makes
\(K\) zero-dimensional. Therefore
\[
-18=-12+\operatorname{length}K,
\]
which is impossible. Hence \(H_x\mid F\).

Conversely every \(H_x\ell\), with \(\ell\) linear, vanishes on \(C_3\).
Therefore
\[
H^0(I_{C_3}(4))=H_xH^0(O(1)),
\]
and multiplication by nonzero \(H_x\) is injective, giving dimension \(4\).

## 5. Exclusion from a (4,7) STCI pair

If a hypothetical quartic member inducing this triple were \(F_4\), then
\[
F_4=H_x\ell
\]
for a nonzero linear form \(\ell\). Put \(P=V(\ell)\). Set-theoretically
\[
V(F_4,G_7)=V(H_x,G_7)\cup V(\ell,G_7).
\]
If \(\ell\mid G_7\), the common zero set contains the plane \(P\). Otherwise
\(G_7|_P\) is a nonzero positive-degree homogeneous polynomial and its zero
locus is a nonempty plane curve. Since \(C_0\) is nonplanar,
\(C_0\cap P\) is zero-dimensional, so this plane curve cannot be contained in
\(C_0\). In either case
\[
\sqrt{(F_4,G_7)}\ne I(C_0).
\]

Thus the explicit P-044 survivor family is excluded as the quartic carrier of
a \((4,7)\) STCI presentation.

## Scope / frontier

This theorem kills the **known explicit** basepoint-free P-044 survivor family.
It does not show that this is the full P-044 zero locus. The immediate
remaining \(e=2\) question is therefore classification (or geometric exclusion)
of all other basepoint-free P-044 zeros, not extension of this explicit family
farther up the primitive tower.


---

## 2026-10-06-dx1-p044-classification

> **SUPERSEDED STATUS NOTICE (2026-10-06 cleanup):** The residual saturation calculation requested below was subsequently completed exactly. The Macaulay2 unit-ideal/saturation certificate in `research/computations/session_dx1_saturation_2026_10_06.m2` and its recorded output closes the residual open set. Together with the audited boundary calculation, the basepoint-free P-044 locus on the dx=1 slice is exactly P-045. This note is retained as provenance for the pre-certificate argument and its identified gap; do not use its OPEN conclusion as current status. See `research/AUDITED_STATE_2026-10-06.md`, Section G.

# dx=1 P-044 classification

Date: 2026-10-06

Status: **OPEN pending one residual saturation calculation.** Independent audit found a genuine gap in the previous residual-open argument: coprimality of two multivariate resultant factors does not imply that their common affine zero set is empty.

On the slice
[
d=x^{-1},qquad u=bx-a,
]
the resultant is
[
Delta=u^2/x.
]
Thus the basepoint-free locus is (D(xu)).

The exact P-044 coordinates specialize as (G_i=uQ_i). Two coordinates have
[
Q_2=(2a+1)R_2,qquad Q_4=2(b+2)R_4.
]

## Audited boundary pieces

On (b=-2), the exact residual calculation shows that every extra common zero has (u=0), hence (Delta=0). Therefore on (D(Delta)),
[
b=-2, P	ext{-044}Longrightarrow a=-1/2.
]

On (a=-1/2), the dedicated exact verifier shows
[
P	ext{-044}Longrightarrow b=-2quad	ext{or}quad u=0.
]
The second alternative lies on (Delta=0). Hence the basepoint-free part of this boundary is exactly P-045.

## Residual open set: still open

On
[
D!left(xu(2a+1)(b+2)ight),
]
P-044 implies
[
R_2=R_4=Q_5=0.
]
After (b=(a+u)/x), exact elimination gives
[
operatorname{Res}_u(R_2,R_4)=-36x(2a+1)P_{24}(a,x),
]
[
operatorname{Res}_u(R_2,Q_5)=-36x^2(2a+1)^2P_{25}(a,x),
]
and
[
gcd(P_{24},P_{25})=1quad	ext{in }mathbf Q[a,x].
]

These identities are exact, but the former conclusion that they prove emptiness was invalid: two coprime multivariate polynomials can have isolated common zeros. The independent audit found such resultant intersections, including ((a,x)=(-1,1/4)) and ((-3/2,1/4)); those sampled points lift only to (u=0) and hence are not counterexamples, but they demonstrate the logical gap.

The required repair is an exact certificate that
[
V(R_2,R_4,Q_5)cap D!left(xu(2a+1)(a+u+2x)ight)=arnothing,
]
equivalently that the corresponding saturated ideal is the unit ideal. Direct SymPy Gröbner/Rabinowitsch attempts timed out on 2026-10-06, so no replacement certificate is claimed here.

Therefore the complete classification
[
d=x^{-1},quadDelta
e0,quad P	ext{-044}
iff
a=-rac12,quad b=-2
]
is **not yet proved**.

Consequently the no-carrier statement on the whole (dx=1) slice is also **OPEN pending this residual calculation**. Its final implication remains valid: if the classification is repaired, P-045's cubic-factor theorem excludes a quartic carrier.

Verifier/diagnostic:
`research/computations/verify_dx1_p044_residual.py`.

Boundary verifier:
`research/computations/verify_dx1_a_half_boundary.py`.
