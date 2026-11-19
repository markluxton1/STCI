# Intrinsic source and determinant images for the primitive triples

Fix characteristic zero, the embedded quartic
\(C=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\), and one of the three
primitive triples \(T\) in the
[ADE reduction](sextic_ade_reduction.md#three-remaining-primitive-triple-orbits).
Write \(I=\mathcal I_C\), \(J=\mathcal I_T\), and \(R\) for the
ideal of its primitive ribbon. Its successive layers are
\(L=\mathcal O_C(-6)\), \(L^2=\mathcal O_C(-12)\), with first
normal relation \(M=\mathcal O_C(-8)\); here the displayed integers
are degrees on \(C\simeq\mathbf P^1\), while an ambient twist by
\(d\) adds \(4d\). Set \(V_d=H^0(J(d))\).

This proof replaces source-matrix ranks for the first-normal image,
restricted cubic-contact image and determinant image. The two unrestricted
coefficient-map ranks \(\operatorname{rank}\Theta=18,12\) are not used
or reproved. The argument does not replace the separate higher-contact
test or assert an STCI construction or exclusion. Independent
reconstruction on 2026-11-19 accepted the sheaf maps, sparse quartic
identities, interpolation, regularity, determinant lemma and higher-degree
corollary. The five principal identities were also checked directly by
small exact substitutions, without a monomial-source rank calculation.

## Two intrinsic evaluation maps

In the accepted frame write \(I=(q',y)\), \(R=(q',y^2)\),
\(J=(q',y^3)\). Then
\[
 A:=J\cap I^2=IR,
 \qquad 0\to A\to I^2\to L^2\to0,
 \qquad 0\to A\to J\xrightarrow{h}M\to0.                 \tag{1}
\]
These are sheaf identities, so purity and the primitive layers include
both endpoints. The quadric \(q=x_0x_3-x_1x_2\) has first ribbon
coefficient
\[
 \mu=A(z)+\tfrac z2B(z)
 =1-4z^2\quad\hbox{or}\quad(r+\tfrac12)z.
\]
As a section of \(L(2)=\mathcal O(2)\), its zero scheme \(Z\)
consists of two distinct points: \(\pm1/2\) in the principal orbit,
and \(0,\infty\) in the algebraic orbits. Their images under the
degree-three ruling map \(z\mapsto z^3\) on the quadric are distinct.

First, the ribbon evaluation
\[
 H^0(I(4))\longrightarrow H^0(L(4))=H^0(\mathcal O(10))             \tag{2}
\]
is onto. The subsystem \(qH^0(\mathcal O_{\mathbf P^3}(2))\)
gives \(\mu H^0(\mathcal O(8))\), because quadrics restrict onto
all binary octics. The remaining quotient is evaluation at \(Z\).
The quadric restriction quotient of \(I(4)\) is
\(fH^0(Q,\mathcal O_Q(3,1))\), where \(f\) cuts out \(C\) in
\(Q\). At a zero of \(\mu\), the coefficient of \(f\) in the
ribbon direction is nonzero, since \(q,f\) generate the conormal
fiber and the quotient to \(L\) is surjective. The very ample
system \(\mathcal O_Q(3,1)\) separates the two points. This supplies
the two missing evaluations. In particular \(h^0(R(4))=18-11=7\).

Next, the quadratic ribbon evaluation
\[
 H^0(I^2(6))\longrightarrow H^0(L^2(6))=H^0(\mathcal O(12))       \tag{3}
\]
is onto. By (2), its \(qH^0(I(4))\) subsystem gives
\(\mu H^0(\mathcal O(10))\). The
[order-two quadric flag](../torus/equation_pair_rank_and_weights.md#characters-of-all-double-surface-equation-spaces)
has quotient \(f^2H^0(Q,\mathcal O_Q(4,0))\). Modulo \(\mu\),
evaluation of these sections is a nonzero fiber factor times
\(P(z^3)\); polynomials of ruling degree four separate the two
distinct ruling images of \(Z\). This proves (3).

The same flag gives \(h^0(I^2(6))=23\) and
\(H^1(I^2(6))=0\). Therefore (1) and (3) give
\[
 h^0(A(6))=10,\quad H^1(A(6))=0,\quad
 h(V_6)=H^0(M(6))=H^0(\mathcal O(16)),\quad \dim V_6=27.          \tag{4}
\]
No rank of a monomial-source matrix is an input to (2)–(4).
More generally, this proof of (2) and (3) works for any such ribbon
direction whose quadric contact divisor is reduced and whose two points
have distinct degree-three ruling images; it does not assert the
existence of a compatible primitive triple in every such direction.

## Quartic interpolation from five sparse sections

The quotient \(R/J=L^2\) defines
\(\rho:H^0(R(4))\to H^0(\mathcal O(4))\). We prove it onto by
explicit sections, without assuming a dimension for \(V_4\).

For an algebraic orbit put \(a=r+3/2\), \(b=r+1/2\), and
\[
 c_0=x_0^2x_2-x_1^3,\quad
 c_1=x_0x_2^2-x_1^2x_3,\quad
 c_2=x_2^3-x_1x_3^2.
\]
In the homogeneous algebraic chart \(\gamma=0\), the ribbon is
\(m=0\) to first order. The two ribbon quartics
\[
 H_0=x_0c_1-(2-a)x_2c_0,\qquad
 H_1=x_1c_1-(2-a)x_3c_0
\]
have residual quadratic coefficients \(b\) and \(b^2z\), and
\(q^2\) has coefficient \(b^2z^2\). For example
\(c_0=y\),
\(c_1=(2-a)z^3y+y^2-z^2m\), proving the first two identities
directly. Coordinate reversal exchanges the conjugate algebraic
triples and gives the degree-four and degree-three coefficients in
the opposite chart. Since \(b\ne0\) for both roots, these five
sections span \(H^0(\mathcal O(4))\).

For the principal orbit retain those cubics and put
\[
 \ell_0=x_2-x_1/4,\quad \ell_1=x_3-x_0/16,\qquad
 \chi(z)=1+2z+4z^2.
\]
Let \(K\) lift a polynomial of degree at most eight linearly to an
ambient quadric using
\[
 z^0,\ldots,z^8\ \longmapsto\
 x_0^2,x_0x_1,x_1^2,x_0x_2,x_0x_3,x_1x_3,x_2^2,x_2x_3,x_3^2.
\]
Thus \(K(p)|_C=p\). Define \(H_{ij}=c_i\ell_j-qK(p_{ij})\)
with the following five polynomials:

| \(ij\) | \(p_{ij}\) | \(\rho(H_{ij})\) |
| --- | --- | --- |
| 00 | \(z/2+2z^2\) | \(4\chi\) |
| 10 | \(z^3/4+z^4/2+z^5\) | \(z\chi\) |
| 20 | \(z^6/2+z^7/2\) | \(z^2\chi/4\) |
| 01 | \(1/8+z/2+z^2/2+2z^3\) | \(-4-16z^3\) |
| 21 | \(z^5/8+z^6/8+z^7/2+z^8/2\) | \(-z/16-z^4\) |

These are direct identities modulo \(y^3\) in the actual triple
substitution
\(U=(1+z)y-\gamma y^2/6\),
\(V=(-2-8z)y+4\gamma y^2/3\), \(\gamma=96+192z\).
The constant and linear coefficients of each \(H_{ij}\) vanish.
One can check the first-order cancellation before any expansion:
\(\ell_0|_C=-z\mu/4\),
\(\ell_1|_C=-(z^2+1/4)\mu/4\), and
\(p_{ij}=\ell_j|_C\,(c_i\text{'s first coefficient})/\mu\).
Only five specified products and their quadratic coefficients are
involved; there is no ambient-space elimination.

The first three residuals span \(\chi k[z]_{\le2}\).
Modulo \(\chi\), the identities \(z^3=1/8\), \(z^4=z/8\)
make the last two residuals \(-6\) and \(-3z/16\).
They span the two-dimensional remaining quotient. Hence \(\rho\)
is onto in the principal orbit too. Together with \(h^0(R(4))=7\),
this proves
\[
 \dim V_4=2                                                        \tag{5}
\]
for all three triples by interpolation, not a complete-source rank.

## The restricted cubic-contact image

The quotient
\[
 A/(IJ)\simeq L^3
\]
is locally generated by \(y^3\). Its degree-six map is
\(-\Theta:H^0(A(6))\to H^0(L^3(6))=H^0(\mathcal O(6))\),
with the sign set by \(F=h_Fq'-\Theta_Fy^3+\cdots\).
For \(H\in H^0(R(4))\),
\[
 \Theta(qH)=-\mu\rho(H).
\]
Thus the image contains \(\mu H^0(\mathcal O(4))\), of dimension
five, by quartic interpolation.

The remaining image is determined at the two zeros of \(\mu\).
The quadric quotient identifies
\[
 H^0(A(6))/qH^0(R(4))
 \simeq\{P\in H^0(\mathbf P^1,\mathcal O(4)):
            P\text{ vanishes at both ruling images of }Z\}.       \tag{6}
\]
Indeed (3) and (2) show that a quadric quotient lifts into \(A(6)\)
exactly when its normal coefficient vanishes at \(Z\); the kernel
is \(qH^0(R(4))\). The right-hand side has dimension three.

In the principal chart put \(\nu=(T_0-zS_0/2)\gamma\). Modulo
\(q'\), write \(q=\mu y-\nu y^2\), \(V=By+S_0\gamma y^2\).
For \(F\in A(6)\), its quadratic terms in \(q,V\) have coefficients
\(a_2,a_1,a_0\), and write \(b_0\) for the \(V^3\) coefficient.
The quadric restriction is \(P(z^3+V)V^2\), so
\(a_0'=3z^2b_0\). Vanishing on the triple gives
\(a_2\mu^2+a_1B\mu+a_0B^2=0\). At a simple root \(z_0\) of
\(\mu\), with \(B(z_0)\ne0\), this implies \(a_0(z_0)=0\).
Differentiation gives
\(a_1(z_0)=-B(z_0)a_0'(z_0)/\mu'(z_0)\).
The cubic coefficient there is
\(-\Theta_F(z_0)=-a_1(z_0)\nu(z_0)B(z_0)+b_0(z_0)B(z_0)^3\).
Substituting \(a_0'=3z^2b_0\) and \(b_0=P'(z^3)\) gives
\[
 -\Theta_F(z_0)=B(z_0)^2
 \left(\frac{3z_0^2\nu(z_0)}{\mu'(z_0)}+B(z_0)\right)P'(z_0^3).
                                                                    \tag{7}
\]
At \(z_0=1/2\) the bracket is zero; at \(z_0=-1/2\),
\(\nu=0,B=2\), so the coefficient is nonzero. Polynomials in (6)
have freely variable first derivatives at their two prescribed distinct
zeros, since they are the product of the two linear factors with an
arbitrary quadratic. Therefore
\[
 \Theta(\ker h)=H^0(\mathcal O(6)(-p)),\quad p=1/2
 \qquad\text{(principal orbit)}.                                  \tag{8}
\]
For an algebraic orbit \(\gamma=0,B=1\); at zero, (7) has nonzero
coefficient. Reversal gives the same statement at infinity for the
conjugate root, hence for each orbit at both endpoints. The two
derivatives in (6) vary independently, so
\[
 \Theta(\ker h)=H^0(\mathcal O(6))
 \qquad\text{(either algebraic orbit)}.                            \tag{9}
\]
In particular the restricted ranks are six and seven, and the joint
ranks are \(17+6=23\) and \(17+7=24\), respectively. No full
coefficient matrix is needed.

## Regularity and a reusable determinant-span lemma

The primitive layer filtration of \(\mathcal O_T\) has terms
\(\mathcal O_C,L,L^2\). Their ambient degree-four twists have
\(H^1=0\) and section dimensions \(17,11,5\). Thus (5) gives
\(H^1(J(4))=0\). Similarly \(H^2(J(3))=H^1(\mathcal O_T(3))=0\),
using the twists \(\mathcal O(12),\mathcal O(6),\mathcal O\),
and \(H^3(J(2))=0\). Consequently \(J\) is 5-regular.
[Mumford's regularity theorem](https://www.math.stonybrook.edu/~roblaz/Reprints/Laz.PAG.Chapt1.pdf),
Theorem 1.8.3, makes \(J(5)\) globally generated and gives
\(H^1(J(d))=0\) for every \(d\ge4\).

It also proves the all-degree source formula
\[
 \dim V_d=\binom{d+3}{3}-12d+15\qquad(d\ge4),
\]
since the three primitive layers have total Euler characteristic
\(12d-15\). For an algebraic triple the same filtration is torus
equivariant. With the centered action its layer section characters are
the integer intervals \([-2d,2d]\), \([-2d+3,2d-3]\),
\([-2d+6,2d-6]\). Subtracting them from the ambient character gives
all source-weight profiles for \(d\ge4\), not merely the three
finite rows in the sextic chapter.

The primitive case of the existing
[intrinsic triple contact module](../normal-geometry/quartic_pair_obstruction.md#6-what-a-neighborhood-only-proof-still-needs)
is the rank-two generator bundle on \(C\),
\[
 D=J/(IJ),\qquad 0\to L^3\to D\to M\to0,                         \tag{10}
\]
which is locally free because \(J=(q',y^3)\) is a local complete intersection.
Its determinant is \(\mathcal O(-26)\). The contact map is the
ordinary determinant of actual equation sections in \(D(6)\):
\[
 \Omega_3:\bigwedge^2 V_6\longrightarrow
 H^0((\det D)(12))=H^0(\mathcal O(22)).                            \tag{11}
\]
This proves the degree-22 target intrinsically, including cancellation
of the apparently higher affine coefficients.

**Determinant-span lemma.** Let \(0\to B\to E\to A\to0\) be a
rank-two extension on \(\mathbf P^1\), and let actual sections
\(V\to H^0(E)\) map onto \(H^0(A)\). If the image of the
kernel is \(H^0(B)\), with both degrees nonnegative, then their
determinants span \(H^0(AB)\). The same holds when the kernel image
is \(H^0(B(-p))\), provided \(\deg A\ge0,\deg B\ge1\) and
\(V\) generates the fiber \(E_p\). Indeed determinants against
kernel sections span \(H^0(A)H^0(B)\), or
\(H^0(A)H^0(B(-p))=H^0(AB(-p))\), by binary-form multiplication.
In the second case a pair independent at \(p\) supplies the single
remaining evaluation. This concerns the span of determinants, not
the decomposable zero locus.

Apply the lemma to \(E=D(6)\), \(A=M(6)=\mathcal O(16)\),
\(B=L^3(6)=\mathcal O(6)\), using (4), (8), (9).
In the principal case, 5-regularity gives the needed fiber generation:
actual quintics generate \(J(5)\), hence its quotient \(D(5)\);
multiplying a pair independent at \(p\) by a linear form nonzero
there gives two actual sextics independent in \(D(6)_p\).
Therefore, for all three triples,
\[
 \operatorname{im}\Omega_3=H^0(\mathcal O(22)),\qquad
 \operatorname{rank}\Omega_3=23,\qquad \dim\ker\Omega_3=328.         \tag{12}
\]

## All higher equation degrees

The same mechanism gives a useful unequal-degree strengthening. For
\(a,b\ge6\), the determinant of actual equations is onto:
\[
 V_a\otimes V_b\longrightarrow
 H^0((\det D)(a+b))=H^0(\mathcal O(4(a+b)-26)).                    \tag{13}
\]
For equal degrees it factors through \(\bigwedge^2V_a\).
To prove this, multiply sextics in (12) by ambient forms \(P,Q\)
of degrees \(a-6,b-6\). Determinants multiply by \((PQ)|_C\),
because \(D\) is a sheaf on \(C\). Products span
\(S_{a+b-12}\). If that degree is at least two, restriction onto
all binary forms of degree \(4(a+b-12)\) is surjective, and binary
multiplication with \(H^0(\mathcal O(22))\) proves (13). The
degree-zero case is (12). In the remaining degree-one case, the
restrictions \(1,z,z^3,z^4\) times all polynomials of degree at
most 22 span every degree through 26, also proving (13).

Thus the equal-degree contact rank is \(8a-25\) for every \(a\ge6\).
The targets measure this first determinant condition for the fixed
primitive triple; larger degrees do not change it into the full
higher-multiplicity condition. Neither surjectivity nor the kernel
dimension constructs a proper sole-supported intersection.
