# Regular-ratio degree-(4,6) pairs: a pure horizontal direction is impossible

Date: 2026-10-05. Scope: characteristic zero, the monomial rational quartic
\(C_0=[s^4:s^3t:st^3:t^4]\). This note is independent of the main ledgers.
It addresses the **regular-ratio branch only**: after subtracting an ambient
quadratic multiple of the quartic, the sextic has normal order at least two.
The quotient regularity cannot be inferred for a general pair.

## Result and exact hypotheses

**PROVED here and independently audited.** Suppose forms \(F_4,G_6\)
cut out \(C_0\) set-theoretically in characteristic zero, the first normal
quotient is regular, and the common primitive horizontal direction has degree
\(e=0\). In the balanced affine conormal frame

\[
 x_0=1,\quad x_1=z,\quad x_2=z^3+V,\quad
 x_3=z^4+U+\tfrac32zV,
\]

the first normal form of \(F\) cannot be a multiple of \(V\), and cannot
be a multiple of \(U\). Thus both coefficients of its constant horizontal
factor must be nonzero. This excludes the entire two-point boundary of the
constant-direction parameter line, including all its quartic parameters;
it is not just a generic-rank computation.

The proof uses the global residual divisor on the unique quadric, and only the
cubic and quartic transverse jets after that restriction. No claim is made
about the mixed direction or \(e=1\), or about the nonregular branch.

## Dependencies rechecked

Set

\[
 q=x_0x_3-x_1x_2,\quad A=x_0^2x_2-x_1^3,
 \quad B=x_0x_2^2-x_1^2x_3,\quad D=x_2^3-x_1x_3^2.
\]

The script derives the degree-four ideal space from these generators and
checks its dimension 18 and normal-image rank 17. Its first-normal kernel is
\(kq^2\). It also verifies that the 18 forms \(qI_C(4)\) together with
\(A^2,AB,B^2,BD,D^2\) have rank 23. The fact that these span the full
symbolic-square sextic space is P-017/P-022; the existing `verify_degree6.py`
independently proves saturation and the dimension. The present script checks
all linear-algebra identities actually used below.

P-021 permits subtracting a quadratic multiple of \(F\) in the regular
branch. Thus take \(G\in I_C^{(2)}(6)\). A genuine pair has neither carrier
\(q\)-divisible: otherwise its intersection with the other equation has an
extra residual curve on the quadric. Generic transverse length is six, since
\(\deg(F)\deg(G)=24=6\deg C_0\). Formal elimination of the generically
smooth quartic therefore makes every transverse coefficient through order
five vanish. In particular the quadratic normal form of \(G\) is divisible
by the linear normal form of \(F\).

## Complete pure-direction quartic space

Define

\[
\begin{aligned}
 P_6&=x_0x_1x_3^2+x_0x_2^3-2x_1^2x_2x_3,\\
 P_7&=2x_0x_2^2x_3-x_1^2x_3^2-x_1x_2^3,\\
 P_9&=2x_0x_3^3-3x_1x_2x_3^2+x_2^4.
\end{aligned}
\]

Exact linear algebra proves that every quartic with first normal form
\(h(z)V\) has the unique expression

\[
 F=A(c_0x_0+c_1x_1+c_3x_2+c_4x_3)
       +c_6P_6+c_7P_7+c_9P_9+\kappa q^2.
\]

In the affine normal coordinates,

\[
 h=c_0+c_1z+c_3z^3+c_4z^4+c_6z^6+c_7z^7+c_9z^9,
\]

and the \(U^2\) coefficient of \(F\) is

\[
 R=\kappa+c_6z-c_7z^2+3c_9z^4.
\]

Thus \(F=hV+RU^2+\text{other terms of normal order at least two}\).
The term “other” here includes terms involving \(V\); after the formal
solution \(V=-(R/h)U^2+\cdots\), these do not affect that quadratic
coefficient.

## The quadric forces the sextic residual

Use Segre coordinates

\[
 (x_0,x_1,x_2,x_3)=(a_0b_0,a_0b_1,a_1b_0,a_1b_1),
 \qquad c=a_1b_0^3-a_0b_1^3.
\]

On \(Q\), \(A=a_0^2c\), \(B=a_0a_1c\), \(D=a_1^2c\).
Write \(F|_Q=c\rho\), \(G|_Q=c^2\sigma\), where \(\rho\) has
bidegree \((3,1)\), and \(\sigma\) is a nonzero binary quartic in
\((a_0,a_1)\).

Because the coefficient of \(U^2\) in a general \(qI_C(4)\) sextic has
\(z\)-degree at most nine, while the coefficient of \(U^2\) in \(D^2\)
has leading term \(4z^{10}\), divisibility of \(G_2\) by \(V\) forces
the \(D^2\) coefficient to be zero. Therefore \(a_0\mid\sigma\).
The exact residual identity on the ruling \(a_0=0\) is

\[
 \rho(0,a_1;b_0,b_1)=c_9a_1^3b_0.
\]

If \(c_9=0\), both \(\rho\) and \(\sigma\) contain the ruling
\(a_0=0\). That line is then contained in \(V(F,G)\), and is not \(C_0\).
This excludes the full \(c_9=0\) boundary.

Suppose henceforth \(c_9\ne0\). At
\(P=C_0\cap\{a_0=0\}=\{a_0=b_0=0\}\), the affine chart
\(a_1=b_1=x_3=1\) has
\(x_0=a_0b_0,x_1=a_0,x_2=b_0\). The ambient derivative
\(\partial F/\partial x_0\) at \(P\) is \(2c_9\), so \(F\) is smooth
there. Moreover \(\rho=c_9b_0+O((a_0,b_0)^2)+O(a_0)\), and
\(c=b_0^3-a_0\), so \(C_0\) and \(\rho\) intersect with multiplicity
one on \(Q\). Both \(F\) and \(Q\) project formally isomorphically
to the \((x_1,x_2)=(a_0,b_0)\) plane at this point, because their
\(x_0\) derivatives are nonzero. The same two curve germs consequently
have intersection multiplicity one on the smooth surface \(F\). In
particular \(a_0\) is a parameter on the smooth germ \(\rho\).

On the smooth surface \(F\), let \(v\) be a local equation of \(C_0\).
Generic transverse order at least six implies \(v^6\mid G\) in the local
ring at \(P\): the coefficients of smaller powers vanish identically along
the integral curve. Restrict to the smooth germ \(\rho\). Since
\(i_P(C_0,\rho)=1\), \(G|_\rho\) has order at least six. The identity
\(G|_Q=c^2\sigma\) then forces \(\sigma|_\rho\) to have order at least
four. But \(a_0\) is a parameter on \(\rho\), and \(\sigma\) is a
binary quartic. Consequently

\[
 \sigma=\gamma a_0^4,\qquad\gamma\ne0.
\]

Equivalently,

\[
 G=\gamma A^2+qF',\qquad F'\in I_C(4).
\]

Divisibility of \(G_2\) by \(V\) forces \(F'\) to have pure first normal
form \(h'V\), so \(F'\) belongs to the same eight-dimensional quartic
space. Here no cancellation of a torsion class, no smooth-normalization
assumption, and no sextic normalization argument is involved.

## A universal cubic-jet rigidity identity

Let \(R'\) be the \(U^2\) coefficient associated to \(F'\). Eliminating
\(F\) gives

\[
 V=-\frac RhU^2+O(U^3),
\]

and the cubic coefficient of \(G\) is

\[
 R'-\frac{h'}hR.
\]

It must vanish. Thus \(hR'-h'R=0\).
Subtract a scalar multiple of \(F\) from \(F'\) so that \(c'_9=0\).
This does not affect \(hR'-h'R\). Its \(z^{11}\) coefficient is then
\(-4c_9c'_7\), so \(c'_7=0\). Its \(z^{10}\) coefficient becomes
\(-2c_9c'_6\), so \(c'_6=0\). Its \(z^9\) coefficient then becomes
\(c_9\kappa'\), so \(\kappa'=0\). Hence \(R'=0\), and since
\(R\ne0\), the polynomial identity gives \(h'=0\). All eight quartic
coefficients are zero. Thus the original \(F'\) was a scalar multiple of
\(F\).

Modulo \(F\), therefore, \(G=\gamma A^2=\gamma V^2\). Because
\(R\) has leading coefficient \(3c_9\ne0\), \(V\) has transverse order
exactly two on \(F\) at the generic point of \(C_0\). Consequently
\(G\) has order exactly four, contrary to the required six. This excludes
\(c_9\ne0\), and completes the pure-\(V\) proof.

The coordinate reversal \((x_0,x_1,x_2,x_3)\mapsto(x_3,x_2,x_1,x_0)\)
preserves \(C_0\), and exchanges the two pure constant directions up to
nonzero scale in the balanced frames (its coefficient action is already
verified in P-025). Hence the pure-\(U\) case is excluded too.

## Computation, epistemic boundary, and next investigation

Run

```
/private/tmp/stci-cas-venv/bin/python research/computations/verify_mixed46_regular.py
```

with SymPy 1.14.0. The script derives the full pure quartic space, checks the
residual identity and smoothness derivative, detects the sextic \(D^2\)
coefficient, checks the three successive polynomial coefficients proving
rigidity, and independently checks the formal cubic coefficient. It does not
substitute finite sampling for the exhaustive polynomial argument.

The remaining degree-zero directions have both coefficients nonzero. The
torus \(z\mapsto\lambda z\) acts on \(U,V\) with weights four and three,
so all these directions form one orbit; normalize the direction to \(U+V\).
This substantially reduces the degree-zero regular frontier, but does not
settle it. The most valuable immediate continuation is the corresponding
mixed-direction residual restriction plus cubic-contact rigidity, preserving
all quartic parameters and exceptional cases. The \(e=1\) regular branch
remains separate.
