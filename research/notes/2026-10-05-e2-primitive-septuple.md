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
