# Exact quartic symbol image and primitive direction strata

Date: 2026-10-05. This note works in characteristic zero, on the smooth
monomial rational quartic

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3_{x,y,z,w}.
\]

It is a first-conormal calculation. It does not assert existence or
nonexistence of a common local-cohomology ancestor, or of an STCI pair.
The exact companion script is
`research/computations/verify_localcoh_direction_image.py`.

## 1. The image, with the frame fixed explicitly

On the chart \(x=1\), use \(t=y\) and the balanced conormal frame

\[
 U=w-t^4-\frac32t(z-t^3),\qquad V=z-t^3.
\]

For a quartic \(F\in I_{C_0}(4)\), its first normal symbol is

\[
 \sigma(F)=P(t)U+Q(t)V,
\]

where

\[
 P=F_w(1,t,t^3,t^4),\qquad
 Q=(F_z+\tfrac32yF_w)(1,t,t^3,t^4).
\]

Both coefficient polynomials have degree at most nine. If \(P_i,Q_i\)
denote their coefficients of \(t^i\), the image is exactly

\[
 \boxed{\mathcal V=\{(P,Q)\in H^0(O(9))^2:
 P_1=2Q_2,\ P_4=2Q_5,\ P_7=2Q_8\}.}
\]

Thus \(\dim\mathcal V=17\), whereas \(\dim I_{C_0}(4)=18\). The kernel is
\(kq^2\), where

\[
 q=xw-yz,\quad A=x^2z-y^3,\quad B=xz^2-y^2w,\quad C=yw^2-z^3.
\]

Here is a direct proof and a usable inverse. Put

\[
 R=Q-\frac t2P.
\]

For the three cubic generators their affine symbols and resulting \(R\)
are

\[
\begin{array}{c|c|c}
\text{generator}&(P,Q)&R\\\hline
A&(0,1)&1\\
B&(-t^2,\tfrac12t^3)&t^3\\
C&(2t^5,0)&-t^6.
\end{array}
\]

Multiplication by \(x,y,z,w\) multiplies the symbol by
\(1,t,t^3,t^4\), respectively. A symbol \(qH\), with \(H\) quadratic,
is \((p,\frac t2p)\), where \(p=H|_{C_0}\) can be any polynomial of
degree at most eight. Consequently all image symbols have

\[
 R_2=R_5=R_8=0.
\]

Conversely, let \((P,Q)\) satisfy these three equations and define

\[
 J=R_0xA+R_1yA+R_3zA+R_4wA
   +R_6zB+R_7wB-R_9zC-R_{10}wC.
\]

Then

\[
 P_J=-R_6t^5-R_7t^6-2R_9t^8-2R_{10}t^9,
\quad R_J=R.
\]

Since \(Q\) has degree at most nine,
\(R_{10}=-P_9/2\). Hence \(p=P-P_J\) has degree at most eight.
Choose the quadratic lift

\[
 H(p)=p_0x^2+p_1xy+p_2y^2+p_3xz+p_4xw
        +p_5yw+p_6z^2+p_7zw+p_8w^2.
\]

Every quartic with the prescribed symbol is exactly

\[
 \boxed{F=qH(p)+J+cq^2,\qquad c\in k.}
\]

Indeed, the nine forms \(qH(t^i)\), the eight displayed summands of
\(J\), and \(q^2\) are independent quartics in the ideal. The restriction
map from the 35-dimensional space of quartics to \(H^0(O(16))\) is
surjective: quartic monomials on \(C_0\) attain every exponent
\(0,\ldots,16\). Thus \(\dim I_{C_0}(4)=35-17=18\), proving that these
18 forms exhaust it.

## 2. Intersections with primitive binary directions

Write a primitive direction of degree \(e\) as

\[
 r=(r_1,r_2),\qquad
 r_1(s,t)=\sum_{i=0}^e a_i s^{e-i}t^i,\quad
 r_2(s,t)=\sum_{i=0}^e b_i s^{e-i}t^i.
\]

Primitive means the homogeneous binary forms have no common zero. In
particular, this is stronger than checking an affine gcd alone. Write

\[
 h(s,t)=\sum_{j=0}^{9-e}h_j s^{9-e-j}t^j.
\]

The multiplication map \(h\mapsto(r_1h,r_2h)\) is injective, so the
dimension of \(\mathcal V\cap rH^0(O(9-e))\) is the nullity of the
following three scalar equations:

\[
 \boxed{\sum_{i=0}^e a_i h_{3k+1-i}
          -2\sum_{i=0}^e b_i h_{3k+2-i}=0,
          \qquad k=0,1,2,}
\]

where coefficients outside \(0\le j\le9-e\) are zero.

### Degree zero

Each row has coefficients \((a_0,-2b_0)\) in a separate pair of columns.
The direction is nonzero, so all three rows are independent. Therefore

\[
 \boxed{e=0:\quad \dim(\mathcal V\cap rH^0(O(9)))=7}
\]

for every direction.

### Degree one

Each row is the coefficient triple

\[
 (a_1,\ a_0-2b_1,\ -2b_0)
\]

in its own block of three scalar coefficients. Thus the matrix has rank
three unless all three entries vanish; in the latter case its rank is
zero. The exceptional equations imply

\[
 r=(2b_1s,b_1t),\qquad b_1\ne0.
\]

Consequently

\[
 \boxed{e=1:\quad
 \dim(\mathcal V\cap rH^0(O(8)))=
 \begin{cases}
 9,&r\sim(2s,t),\\
 6,&\text{otherwise}.
 \end{cases}}
\]

The exceptional point is precisely the quadric symbol direction. Its
quartic preimage is \(qS_2\), of dimension ten, because all its symbols
are provided by \(qH\) and its one-dimensional symbol kernel is
\(kq^2\).

### Degree two

Set

\[
 D=a_1-2b_2,\quad E=a_0-2b_1,\quad
 T=a_2,\quad K=-2b_0.
\]

In the coefficient basis \((h_0,\ldots,h_7)\), the constraint matrix is

\[
 \begin{pmatrix}
 D&E&K&0&0&0&0&0\\
 0&0&T&D&E&K&0&0\\
 0&0&0&0&0&T&D&E
 \end{pmatrix}.
\]

If \(D\ne0\) or \(E\ne0\), its minors in columns \((0,3,6)\) and
\((1,4,7)\) are \(D^3\) and \(E^3\), so its rank is three. When
\(D=E=0\), its only possibly nonzero columns are \(h_2,h_5\), with
matrix

\[
 \begin{pmatrix}K&0\\T&K\\0&T\end{pmatrix}.
\]

This has rank two provided \((T,K)\ne(0,0)\). If \(T=K=0\) as well,
then

\[
 r=(2s(b_1s+b_2t),\ t(b_1s+b_2t)),
\]

which is not primitive. Hence

\[
 \boxed{e=2:\quad
 \dim(\mathcal V\cap rH^0(O(7)))=
 \begin{cases}
 6,&a_0=2b_1\text{ and }a_1=2b_2,\\
 5,&\text{otherwise},
 \end{cases}}
\]

always under the primitive hypothesis. Both strata occur: \((t^2,s^2)\)
is primitive and exceptional, while \((s^2,t^2)\) is primitive and
generic. The exceptional locus is the primitive open subset of the
projective three-space

\[
 r_1=2b_1s^2+2b_2st+a_2t^2,\qquad
r_2=b_0s^2+b_1st+b_2t^2.
\]

Every primitive exceptional direction has the same scalar kernel:

\[
 \boxed{h_2=h_5=0,\qquad
 h\in\langle1,t,t^3,t^4,t^6,t^7\rangle.}
\]

The displayed span is affine notation for the corresponding homogeneous
degree-seven binary forms. It follows at once from the two-column rank-two
matrix, whether one or both of \(T,K\) are nonzero.

Equivalently, on this locus

\[
sr_1-2tr_2=-2b_0s^3+a_2t^3.
\]

In the coordinates \((a_0,a_1,a_2,b_0)\), with
\(b_1=a_0/2,b_2=a_1/2\), the primitive open subset is defined explicitly
by the nonvanishing homogeneous resultant

\[
 \boxed{\operatorname{Res}(r_1,2r_2)
 =a_0^3a_2-6a_0a_1a_2b_0+2a_1^3b_0+4a_2^2b_0^2\ne0.}
\]

## 3. Dimensions in the ambient quartic space

The preimage of each symbol intersection adds the independent parameter
\(cq^2\). Thus the quartics whose first symbol has the given direction
form linear spaces of dimension eight for \(e=0\), seven or ten for
\(e=1\), and six or seven for \(e=2\). Zero symbols are included in
these linear spaces; selecting an actual pair with primitive common
direction still requires nonzero scalar symbols, appropriate gcd
conditions, and every higher direct-limit equation.

## 4. Coprime quartic pairs exist in every remaining direction

Let \(K_r\) be the scalar kernel computed above and put

\[
 L_r=\sigma^{-1}(rK_r)\subset I_{C_0}(4).
\]

For the exceptional quadric direction \(r_q=(2s,t)\), the calculation
above gives \(L_{r_q}=qS_2\). Every pair in this space shares the
ambient factor \(q\). Hence this direction supplies no ambient-coprime
quartic pair.

For **every other primitive direction of degree at most two**, the
opposite conclusion holds at first-conormal order: there exist
ambient-coprime quartic pairs with linearly independent scalar symbols.
Thus their first-symbol ratio is nonconstant. Here is a constructive
proof.

Any \(q\)-divisible quartic has first symbol
\((p,\frac t2p)\), or zero. Consequently, a quartic with nonzero symbol
in direction \(r\ne r_q\) is not divisible by \(q\). This follows also
by taking the determinant with the quadric row: a nonzero scalar symbol
would otherwise force \(2r_2-tr_1=0\), whose only primitive homogeneous
solution is the degree-one direction \(r_q\).

The table proves \(\dim K_r\ge5\). Choose two independent nonzero
scalars \(h_1,h_2\in K_r\) and use the explicit inverse from Section 1
to lift them to \(F,G_0\in L_r\). The form \(F\) is not divisible by
\(q\). For each irreducible factor \(D\) of \(F\), there is at most one
constant \(c\in k\) for which

\[
 D\mid G_0+cq^2.
\]

Indeed, two distinct constants would imply \(D\mid q^2\), hence
\(D\sim q\), contradicting \(q\nmid F\). Avoiding the finitely many
excluded constants gives

\[
 G=G_0+cq^2,\qquad \gcd(F,G)=1,
\]

while the symbols remain \(h_1r,h_2r\). The field is infinite, so such
\(c\) exists. Their ratio cannot be constant because \(h_1,h_2\) are
independent.

The base ideal generated by \(L_r\) has no hypersurface component:
it contains both \(q^2\) and a form \(F\) not divisible by \(q\).
Equivalently its forms have gcd one. The coprime independent-symbol
pairs comprise a nonempty Zariski-open subset of \(L_r\times L_r\).
The common-factor locus is closed, since for each possible common
factor degree it is the image of the corresponding projective
factor-multiplication incidence; there are only four such degrees.
Scalar-symbol dependence is closed by the two-by-two minors of the
symbol coefficient matrix.

This establishes that coprimality and nonconstant first-symbol ratio
cannot remove any of the other degree-zero, degree-one, or degree-two
directions. It makes no claim that any of these coprime pairs passes
the higher ancestor equations.

The calculation provides a complete exact parametrization of the
first-conormal coefficient space for the \(e\le2\) frontier. It leaves
the higher normal jets as the next research obligation.
