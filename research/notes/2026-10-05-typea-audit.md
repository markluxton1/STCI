# Independent reconstruction of the type-A multiplicity-five exclusion

Date: 2026-10-05. Scope: characteristic zero, the monomial smooth rational
quartic `C0`, and the Bănică--Forster numerical type

\[
L=O_{\mathbf P^1}(-7),\qquad D_2=D,\quad D_3=D_4=2D,\qquad \deg D=3.
\]

This audit reconstructs all parameter charts and the terminal extension
obstruction underlying the type-A part of P-025. It supplies the previously
missing durable derivation and exact computation. It confirms that exclusion;
it does not establish non-STCI, or a statement about arbitrary multiple-curve
types. The Bănică--Forster description and the numerical classification in
P-016 are the inputs.

The independent verifier is
`research/computations/verify_typea45.py`. It starts with the exact embedded
chart transition, derives the killing-section rank matrix, computes both
exceptional quotient lines, and computes all higher cocycles from the moving
coordinate. Run it with any SymPy-equipped Python, for example:

```
/private/tmp/stci-cas-venv/bin/python research/computations/verify_typea45.py
```

## 1. Every double-to-triple quotient stratum

Use the P-010 split frames

\[
u=b-\frac32za,\quad v=a,\qquad
u'=\tfrac12a',\quad v'=-3Wa'+2b',
\]

where

\[
W=\frac{z^3+a}{z^4+b},\qquad
 a'=\frac z{z^4+b}-W^3,\qquad
 b'=\frac1{z^4+b}-W^4.
\]

For the finite quotient chart set \(m=u+\theta v,\ell=v\). Both linear
frames have transition \(z^{-7}\). The exact quadratic coefficient is

\[
h_2=3\theta^3z^{-5}-\frac32\theta^2z^{-4}
       +\frac34\theta z^{-3}-\frac38z^{-2}
       \in H^1(O(-7)).
\]

A triple of defect divisor \(D\) requires a nonzero section
\(\delta=d_0+d_1z+d_2z^2+d_3z^3\in H^0(O(3))\) killing this class in
\(H^1(O(-4))\). The three equations, multiplied by \(8/3\), have matrix

\[
\begin{pmatrix}
0&-1&2\theta&-4\theta^2\\
-1&2\theta&-4\theta^2&8\theta^3\\
2\theta&-4\theta^2&8\theta^3&0
\end{pmatrix}.
\]

Its minor on columns \(0,1,3\) is \(-16\theta^4\). For \(\theta\ne0\),
its unique projective kernel is

\[
(d_0,d_1,d_2,d_3)=(0,2\theta,1,0),\qquad
\delta_U=z(z+2\theta),\quad \delta_V=w+2\theta w^2.
\]

Although \(\delta_U\) has affine degree two, it is a section of \(O(3)\):
its divisor includes the point at infinity. The exact identity

\[
\delta_U h_2=6\theta^4z^{-4}-\frac38
\]

uniquely gives

\[
\gamma_U=\frac38,\qquad\gamma_V=6\theta^4,
\qquad \delta_Uh_2+\gamma_U=z^{-4}\gamma_V.
\]

There is no global ambiguity because \(H^0(O(-4))=0\).
The triple ideal on either chart is

\[
I_3=(A,B,C,T),\quad
 A=\delta m-\gamma\ell^2,\quad B=m\ell,
 \quad C=m^2,\quad T=\ell^3.
\]

The required triple epimorphism fails wherever \(\delta=\gamma=0\):
there the transverse ideal is \((m\ell,m^2,\ell^3)\), of colength four
instead of three. This elementary flatness test closes the two exceptional
quotient strata:

* At \(\theta=0\), the rank is two and every killing section is
  \(\delta_U=z^2(d_2+d_3z)\). Its unique gluing solution is
  \(\gamma_U=3(d_2+d_3z)/8,\gamma_V=0\). The remaining homogeneous linear
  factor is a common zero of \(\delta,\gamma\), including the case when
  that zero is at infinity.
* At the missing quotient point use \(m=v,\ell=u\). Direct expansion gives
  \(h_2=3z^{-5}\), so killing requires \(d_2=d_3=0\).
  Then \(\delta_U=d_0+d_1z\),
  \(\delta_V=w^2(d_0w+d_1)\), \(\gamma_U=0\), and
  \(\gamma_V=3(d_0w+d_1)\). Again the homogeneous linear factor supplies
  a common zero.

This covers all of the quotient projective line. For \(\theta\ne0\), the
ambient automorphism

\[
[x_0:x_1:x_2:x_3]\longmapsto[x_0:cx_1:c^3x_2:c^4x_3]
\]

preserves \(C_0\), scales \((z,u,v)\) by \((c,c^4,c^3)\), and carries the
kernel parameter to \(\theta/c\). Taking \(c=\theta\) reduces every
remaining case to \(\theta=1\). Thus the following computation is exhaustive,
not a test of one isolated quotient point.

## 2. The unique triple-to-quadruple extension

Henceforth

\[
\delta_U=z(z+2),\quad\gamma_U=\frac38,
\qquad\delta_V=W+2W^2,\quad\gamma_V=6.
\]

Coefficient functions on the second chart are evaluated at the **moving**
coordinate \(W\), through the necessary normal degree, throughout.
The first normal coefficient of \(A_V\) is
\(p_3\delta_Um\) with \(p_3=z^{-10}\). Let \(q_B,q_T\) be the
coefficients of \(m\ell,\ell^3\) in \(A_V-p_3A_U\).
The prescribed next layer is \(L^3(2D)=O(-15)\), and the intrinsic
conormal map has values

\[
A\mapsto\rho,\quad B\mapsto\gamma\delta,
\quad C\mapsto0,\quad T\mapsto\delta^2.
\]

Its gluing obstruction is

\[
h_3=\frac{q_B\gamma_U\delta_U+q_T\delta_U^2}{p_3}
    =\frac z{16}+\frac14+8z^{-5}-64z^{-6}-144z^{-7}.
\]

There are no coordinates in the nontrivial Cech range
\(z^{-1},\ldots,z^{-4}\) for \(H^1(O(-5))\). The unique local corrections
are

\[
\rho_U=-\frac{z+4}{16},\qquad
\rho_V=8-64w-144w^2,
\qquad\rho_U+h_3=z^{-5}\rho_V(1/z).
\]

Their uniqueness uses \(H^0(O(-5))=0\). Epimorphism holds: at the two finite
zeros of \(\delta_U\), \(\rho_U\) equals \(-1/4,-1/8\), and at infinity
\(\rho_V(0)=8\). Equivalently each chart has
\(\gcd(\delta,\rho)=1\).

The quadruple ideal is generated locally by

\[
E=\delta A-\frac\rho\gamma B
 =\delta^2m-\delta\gamma\ell^2-\frac\rho\gamma m\ell,
\quad F=m^2,\quad H=\delta m\ell-\gamma\ell^3,
\quad J=\ell^4.
\]

Here \(\gamma\) is a unit on both full standard charts. To see that these
are the complete kernel, the syzygies of the row
\((\rho,\gamma\delta,\delta^2)\) are generated by
\((\delta,-\rho/\gamma,0)\) and \((0,\delta,-\gamma)\), since
\((\delta,\rho)=1\). The remaining generators of \(I_C I_3\) also lie
in this ideal. For example

\[
\ell E-\delta H=-\frac\rho\gamma m\ell^2,
\qquad \ell H+\gamma J=\delta m\ell^2.
\]

These two identities and \((\delta,\rho)=1\) put \(m\ell^2\) in the
kernel ideal everywhere. The other normal multiples follow directly.
Thus no extra local ideal generators or parameter strata have been omitted.

## 3. Terminal obstruction and descent across the defect divisor

The fifth layer is \(L^4(2D)=O(-22)\). A local reference conormal map has
values

\[
\phi(E)=0,\qquad\phi(F)=\gamma^2,
\qquad\phi(H)=\rho,\qquad\phi(J)=\delta^2.
\]

Over the generic point these values can be computed by the formal
substitution

\[
m=\frac\gamma\delta\ell^2+
  \frac\rho{\delta^3}\ell^3+
  \frac{\rho^2}{\gamma\delta^5}\ell^4\pmod{\ell^5},
\]

which solves \(E=0\). Evaluate any ideal generator, extract its
\(\ell^4\) coefficient, and multiply by \(\delta^2\).

The denominators in this substitution do **not** remove the defect points
from the proof. All four assigned generator images are regular functions on
the full chart. Every relation among the generators is sent to zero over the
generic point, hence everywhere, because the target line bundle is
torsion-free over the integral base curve. Consequently these assignments
define actual homomorphisms on the full charts, including \(D\). The rational
substitution is only a device for calculating those regular homomorphisms.
Also \(\phi(F)=\gamma^2\) is a unit, so these reference maps are epimorphisms.

The verifier checks that the second-chart generator images satisfy precisely

\[
\phi_U(F_V)=z^{-22}\gamma_V^2,\qquad
\phi_U(H_V)=z^{-22}\rho_V(1/z),\qquad
\phi_U(J_V)=z^{-22}\delta_V(1/z)^2.
\]

Thus their discrepancy factors through the remaining generator line.
The leading coefficient of \(E_V\) relative to \(E_U\) is
\(p_4=z^{-13}\). Since
\(\operatorname{Hom}(O(-13),O(-22))=O(-9)\), the obstruction to gluing the
local maps is

\[
h_4=\frac{\phi_U(E_V)}{p_4}\in H^1(O(-9)).
\]

Exact moving-coordinate computation gives

\[
\begin{aligned}
h_4={}&-\frac5{384}-\frac5{64}z^{-1}-\frac5{96}z^{-2}
 +\frac5{48}z^{-3}-\frac5{24}z^{-4}+\frac5{12}z^{-5}\\
 &-\frac56z^{-6}+\frac53z^{-7}+10z^{-8}
 -\frac{124}3z^{-9}+168z^{-10}+432z^{-11}.
\end{aligned}
\]

The constant term and powers at most \(-9\) are standard Cech coboundaries.
The eight remaining coordinates are

\[
\left(-\frac5{64},-\frac5{96},\frac5{48},-\frac5{24},
 \frac5{12},-\frac56,\frac53,10\right).
\]

This vector is exactly \(8/3\) times the vector in P-025; a common scalar
change of generator frame accounts for the normalization. Its first coordinate
is already nonzero in characteristic zero. Therefore the unique epimorphic
quadruple route cannot extend to the prescribed multiplicity-five type.
Together with the exhaustive quotient analysis, this confirms the type-A
exclusion in P-025 on every chart.

## Validation and limits

The script passed on 2026-10-05 using SymPy and exact rational arithmetic.
It independently reconstructs the entire type-A claim rather than accepting
its previously recorded terminal vector as an input. No approximate
root-finding, finite-field scan, or frozen transition coefficient is used.
The original Bănică--Forster classification of the relevant structures remains
the theoretical input. The conclusion excludes the stated multiplicity-five
type on `C0`; it imposes no bound on other degree pairs.
