# Cubic carriers behind the degree-two primitive-fourth zero locus

Date: 2026-10-05. Scope: characteristic zero and the fixed monomial smooth
rational quartic

\[
C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3.
\]

This note independently reconstructs the geometric meaning of the
degree-two primitive-fourth zero locus and the quartics carrying its
canonical primitive triple. The universal primitive-fourth obstruction
calculation is recorded separately by the primitive-quadruple investigation.
Its vanishing locus, on the open set of coprime binary quadratic pairs, is
the linear locus used below. No primitive multiple curve constructed here
is asserted to be a global complete intersection.

## 1. Frames, obstruction degrees, and the factorization of the quadratic jet

On the first affine chart write

\[
z=t/s,\quad a=x_2/x_0-z^3,\quad b=x_3/x_0-z^4,
\quad u=b-\frac32za,\quad v=a.
\]

The split conormal frame has transition \(u'=z^{-7}u\),
\(v'=z^{-7}v\) to first order. A quotient to \(L=O(-5)\) is specified
by a coprime pair of binary quadratics, written on this chart as

\[
u\longmapsto A(z),\qquad v\longmapsto B(z).
\]

Its kernel is \(M=O(-9)\). Consequently

\[
\operatorname{Hom}(M,L^2)=O(-1),\qquad
\operatorname{Hom}(M,L^3)=O(-6),\qquad
\operatorname{Hom}(M,L^4)=O(-11).
\]

Both cohomology groups of \(O(-1)\) vanish. Thus each quotient has a
unique embedded primitive triple, with no free extension parameter. The
next two obstruction spaces have dimensions five and ten respectively.

Let \(D=A'B-AB'\), where primes denote ordinary differentiation in \(z\).
The moving-coordinate calculation in
`research/scratch/primitive47/obstruction.py` gives the following
Bezout-independent expression for its quadratic cocycle:

\[
\boxed{
h_2=-\frac{2A+zB}{8z^5}
       \left(12A^2+3z^2B^2+4z^2D\right).
}
\]

Indeed the first displacement of the opposite affine coordinate is

\[
W_1=-z^{-5}A-\frac12z^{-4}B.
\]

The quadratic ambient jets are

\[
u'_2=-\frac52z^{-11}A^2-3z^{-10}AB-\frac38z^{-9}B^2,
\quad
v'_2=3z^{-12}A^2-z^{-11}AB-\frac94z^{-10}B^2.
\]

Using \(b_V'(1/z)A-a_V'(1/z)B=D\), and multiplying the quadratic
coefficient of \(b_V(W)u'-a_V(W)v'\) by \(z^9\), proves the boxed
formula. In particular, this calculation retains the displacement of the
base coordinate; fixing \(W=1/z\) would omit its final summand.

Write \(\gamma_U\) for the nonnegative Laurent part of \(h_2\). With
\(m=Bu-Av\), the first-chart primitive-triple equation is

\[
m+\gamma_U\ell^2=0\pmod{\ell^3}.
\]

## 2. A distinguished cubic on the fourth-obstruction zero locus

The separately computed universal fourth-obstruction vanishing locus is

\[
A=a_0+a_1z+a_2z^2,\qquad
B=-2a_1-2a_2z+b_2z^2.
\]

Define

\[
q_0(z)=2A+zB=2a_0+b_2z^3.
\]

The homogeneous resultant on this locus is

\[
a_0^2b_2^2+6a_0a_1a_2b_2+4a_0a_2^3-2a_1^3b_2.
\]

In particular, coprimality implies \((a_0,b_2)\ne(0,0)\), so
\(q_0\) is a nonzero section of \(O(3)\).

Use ambient coordinates \([x:y:Z:W]\), and set

\[
Q=xW-yZ,\quad
R_1=x^2Z-y^3,\quad
R_2=xZ^2-y^2W,\quad
R_3=yW^2-Z^3.
\]

The distinguished cubic is

\[
\boxed{
T=Q(2a_0a_1x+2a_0a_2y+a_1b_2Z+a_2b_2W)
  +a_0^2R_1+a_0b_2R_2-\frac{b_2^2}{4}R_3.
}
\]

It lies in \(I(C_0)_3\), and its first conormal symbol in the split
\((u,v)\) frame is

\[
\sigma_1(T)=-\frac{q_0}{2}(B,-A).
\]

Here is an elementary uniqueness derivation. The cubic first symbols have
the form

\[
P=c_0+c_1z-c_5z^2+c_2z^3+c_3z^4+2c_6z^5,
\]

\[
Q_{m n}=c_4+\frac12c_0z+\frac12c_1z^2
                 +\frac12c_5z^3+\frac12c_2z^4+\frac12c_3z^5,
\]

so \(Q_{m n}-zP/2=c_4+c_5z^3-c_6z^6\). A symbol proportional to
\((B,-A)\) therefore has a scalar of degree three proportional to
\(q_0\). Equating coefficients gives the displayed cubic. This also
covers \(a_0=0\) or \(b_2=0\) individually: the other coefficient is
nonzero on the coprime locus. Thus the cubic with this conormal direction
is unique up to scalar.

The boxed quadratic-cocycle formula verifies directly that \(T\) contains
the canonical primitive triple. Substituting \(u=A\ell,v=B\ell\) gives
zero constant and linear coefficients for \(T\); its quadratic
coefficient is \(-q_0\gamma_U/2\). The correction
\(m=-\gamma_U\ell^2\) contributes the opposite coefficient, because
the first symbol of \(T\) is \(-q_0m/2\).

## 3. Every quartic containing this triple is a cubic multiple

The exact quartic-symbol image is independently verified in
`research/computations/verify_localcoh_direction_image.py`:

\[
Q_{{\rm n},2}=P_1/2,\quad
Q_{{\rm n},5}=P_4/2,\quad
Q_{{\rm n},8}=P_7/2,
\]

and the kernel of the symbol map is \(kQ^2\). On the present degree-two
direction locus, a quartic symbol has the form \(h(B,-A)\), where

\[
h=h_0+h_1z+h_3z^3+h_4z^4+h_6z^6+h_7z^7.
\]

Take the universal exact lift of this symbol from that verifier, and add
\(kQ^2\). Let \(f_2\) denote its quadratic coefficient after the straight
substitution \(u=A\ell,v=B\ell\). The actual coefficient on the
canonical triple is \(f_2-h\gamma_U\). This expression is independent
of the polynomial Bezout gauge: the second correction has normal kernel
coordinate exactly \(-\gamma_U\).

Introduce the two linear expressions

\[
E_0=4a_0^2h_6-2a_0b_2h_3+b_2^2h_0,
\qquad
E_1=4a_0^2h_7-2a_0b_2h_4+b_2^2h_1.
\]

The coefficients of \(f_2-h\gamma_U\) at degrees four and one are
\(-b_2E_0/8\) and \(-a_0E_0/4\). The coefficients at degrees five and
two are \(b_2E_1/8\) and \(a_0E_1/4\). Since \((a_0,b_2)\ne(0,0)\),
vanishing requires \(E_0=E_1=0\). These two equations have rank two
on the entire coprime locus and are equivalent to

\[
h=q_0(c_0+c_1z+c_3z^3+c_4z^4).
\]

With this substitution the only remaining condition is

\[
k=4a_0a_2c_3+2a_1b_2c_1.
\]

For explicit coefficient checking, before that substitution the remaining
coefficients at degrees six, three, and zero are respectively

\[
\frac{b_2}{4}
 (4a_0a_1h_7-4a_0a_2h_6-2a_1b_2h_4+b_2k),
\]

\[
\frac12(4a_0^2a_1h_7-4a_0^2a_2h_6-2a_0a_1b_2h_4
 -2a_0a_2b_2h_3+2a_0b_2k-a_1b_2^2h_1+a_2b_2^2h_0),
\]

\[
-a_0(2a_0a_2h_3-a_0k+a_1b_2h_1-a_2b_2h_0).
\]

It follows that the quartic space has dimension four. The four products
\(xT,yT,ZT,WT\) are linearly independent, contain the triple, and span
it. Therefore

\[
\boxed{
H^0(\mathcal I_{C_3}(4))=T\,H^0(O_{\mathbf P^3}(1)).
}
\]

The assertion already holds for the primitive triple; imposing the fourth
layer cannot produce an irreducible quartic carrier. In particular, every
quartic containing a primitive quadruple on this fourth-obstruction zero
locus has the same cubic factor. This supplies a carrier exclusion once
the numerical filtration of a hypothetical complete intersection forces
that primitive triple. It does not exclude multiple structures whose
third layer has nonzero defect.

## 4. A sample fifth obstruction vanishes, with no STCI implication

For \(A=z^2+1,B=-2z\), the first-chart correction coefficients through
degree four are all zero. On the second chart the successive primitive
equation coefficients are

\[
\gamma_V=4+8w^2+3w^4,
\]

\[
\rho_V=-18w-50w^3-39w^5-9w^7,
\]

\[
\tau_V=102w^2+360w^4+\frac{1695}{4}w^6
                   +\frac{405}{2}w^8+\frac{135}{4}w^{10}.
\]

The successive moving-coordinate Laurent cocycles are

\[
h_2=-4z^{-1}-8z^{-3}-3z^{-5},
\]

\[
h_3=18z^{-7}+50z^{-9}+39z^{-11}+9z^{-13},
\]

\[
h_4=-102z^{-13}-360z^{-15}-\frac{1695}{4}z^{-17}
                         -\frac{405}{2}z^{-19}-\frac{135}{4}z^{-21}.
\]

Thus \(h_3\) has no Laurent terms \(z^{-1},\ldots,z^{-5}\), and
\(h_4\) has none of \(z^{-1},\ldots,z^{-10}\). The sample extends to a
primitive quintuple, uniquely at these two extension steps. The displayed
second-chart coefficients are the exact Laurent splittings:
\(\rho_V=-z^6h_3\), \(\tau_V=-z^{11}h_4\), written in \(w=1/z\).
In computing \(h_4\), both \(\gamma_V\) and \(\rho_V\) are evaluated at
the full moving coordinate \(W\) before truncation.

Its distinguished cubic is

\[
T=x^2Z-2y^2Z+2xyW-y^3.
\]

An exact restriction of the full eighteen-dimensional quartic space to
the first-chart embedding \(u=(z^2+1)\ell,v=-2z\ell\), modulo
\(\ell^4\), has rank fourteen and kernel
\(\langle xT,yT,ZT,WT\rangle\). Each of these products restricts
identically to zero in this sample; \(Q^2\) does not contain its triple.

## 5. Scope and pitfalls

The scalar \(q_0\) in the cubic conormal symbol is a section of \(O(3)\),
and it vanishes at points. The cubic is therefore not a surface smooth
along the entire curve. For the sample \(q_0=2\) on the first affine
chart, its homogeneous divisor is three times the point at infinity.
In the chart \(W=1\), the cubic has leading term \(2xy\) at that point,
so it is singular there. The primitive extensions and the cubic factor
are entirely compatible with the existing exclusion of characteristic-zero
STCI presentations on cubic surfaces.

No arbitrary \(\operatorname{GL}_2\) change of the split normal frame,
nor arbitrary base \(\operatorname{PGL}_2\) change, may be used to
normalize the binary quadratic pencil while keeping the nonlinear
transition fixed. Such transformations require transport of the full
embedded jet. The ambient symmetries visibly preserving \(C_0\) include
the torus and the coordinate-reversing involution; these alone do not
identify every coprime quadratic pair.

The fifth-order sample is an exact calculation for one quotient. It
establishes neither a universal fifth-order vanishing statement nor
algebraizability of an infinite formal surface. The universal quartic
carrier identity, in contrast, was derived with symbolic coefficients and
uses only the coprimality-open condition. All conclusions in this note are
stated in characteristic zero; special positive characteristics require
their own coefficient and denominator checks.
