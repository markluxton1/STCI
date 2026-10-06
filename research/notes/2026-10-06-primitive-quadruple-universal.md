# Universal primitive-fourth classification and the ambient quartic obstruction

Status: exact universal classification and carrier theorem, verified over
characteristic zero. The result excludes the degree-two direction branches
of hypothetical `(4,7)` and `(4,8)` complete intersections on the fixed curve
`C0=[s^4:s^3t:st^3:t^4]`. It does not settle STCI for `C0`, other rational
quartics, arbitrary curves, or positive characteristic.

The computation corrects the plausible universal exclusion suggested by
the samples in `2026-10-05-uniform-multiplicity.md`: primitive quadruples of
conormal quotient type `O(-5)` **do exist**. Their quotient directions form
a resultant-open subset of a linear projective three-space. The obstruction
to the indicated complete intersections is instead that every ambient
quartic containing their canonical primitive triple factors as a cubic
times a linear form.

## Formal coordinates and complete parameter coverage

Use the first ambient chart

\[
z=x_1/x_0,\quad v=x_2/x_0-z^3,\quad
u=x_3/x_0-z^4-\tfrac32zv.
\]

The opposite moving coordinate is

\[
W=\frac{z^3+v}{z^4+u+\tfrac32zv},
\]

and its split normal coordinates are

\[
u'=\tfrac12\left(\frac z{z^4+u+\tfrac32zv}-W^3\right),\quad
v'=-\frac{3zW}{z^4+u+\tfrac32zv}+W^4+
\frac2{z^4+u+\tfrac32zv}.
\]

To first order both normal coordinates transition by `z^-7`. Specify
the quotient `O(-7)^2 -> L=O(-5)` by

\[
A=a_0+a_1z+a_2z^2,\qquad B=b_0+b_1z+b_2z^2,
\quad u\mapsto A\ell,\quad v\mapsto B\ell.
\]

These are homogeneous binary quadratics, even when an affine leading
coefficient vanishes. Their projective resultant is

\[
\Delta=a_0^2b_2^2-a_0a_1b_1b_2-2a_0a_2b_0b_2+
a_0a_2b_1^2+a_1^2b_0b_2-a_1a_2b_0b_1+a_2^2b_0^2.
\]

The sole parameter restriction is `Delta != 0`. The matrix sending
degree-at-most-one Bezout coefficients `(S0,S1,T0,T1)` to the coefficients
of `(S0+S1 z)A+(T0+T1 z)B` is

\[
\begin{pmatrix}
a_0&0&b_0&0\\a_1&a_0&b_1&b_0\\
a_2&a_1&b_2&b_1\\0&a_2&0&b_2
\end{pmatrix}.
\]

Its determinant is `Delta`, including affine degree drops. Thus the
Bezout gauges exist uniquely over the entire resultant-open set; no
additional leading-coefficient charts, generic-pencil normalization, or
unexamined boundary directions enter the computation. Reversing the
coefficient vectors gives the opposite-chart gauges, with the same
determinant. We do not use arbitrary changes of the split frame or base
coordinate to normalize quotient directions: those would require changing
the full nonlinear transition.

Set `m=Bu-Av`, whose line type is `M=O(-9)`. Then

\[
\operatorname{Hom}(M,L^2)=O(-1),\qquad
\operatorname{Hom}(M,L^3)=O(-6).
\]

Because both cohomology groups of `O(-1)` vanish, each direction has a
unique embedded primitive triple. A zero fourth obstruction also produces
a unique primitive quadruple, since `H0(O(-6))=0`.

## Exact fourth obstruction and its entire zero locus

For `d=A'B-AB'`, the quadratic cocycle is

\[
h_2=-\frac{2A+zB}{8z^5}\left(12A^2+3z^2B^2+4z^2d\right).
\]

Write `gammaU` for its nonnegative Laurent part and put
`gammaV=(-z*(h2-gammaU))|_(z=1/w)`. The canonical triple has
`m+gammaU ell^2=0` on the first chart and
`m'+gammaV(W) ell'^2=0` on the second. Polynomial Bezout coefficients
`SA+TB=1` give its first-chart parameterization

\[
u=A\ell-T\gamma_U\ell^2,\qquad
v=B\ell+S\gamma_U\ell^2.
\]

All coefficient functions in the opposite equation are evaluated at the
moving coordinate `W` **before truncating**. The cubic coefficient of that
equation, multiplied by `z^9`, gives a Laurent cocycle `h3`; its
coefficients of `z^-1,...,z^-5` represent `H1(O(-6))`.

The universal exact result is

\[
(c_1,\ldots,c_5)=(G_1,\ldots,G_5)/\Delta,
\]

where each `Gi` is a homogeneous degree-eight polynomial. Their complete
expanded values, not a numerical fit, are preserved in
`research/scratch/primitive47universal/equations.json`. If `I=(G1,...,G5)`
and `K=(2a1+b0,2a2+b1)`, the verified exact certificates are

\[
I\subseteq K,\qquad
\Delta^3(2a_1+b_0)^3\in I,\qquad
\Delta^3(2a_2+b_1)^3\in I.
\]

Consequently, on `Delta != 0`, all five coordinates vanish **if and only if**

\[
\boxed{b_0=-2a_1,\qquad b_1=-2a_2.}
\]

This is a set-theoretic classification; the powers in the membership
certificates are not a claim that the obstruction scheme is reduced.
Its projectivized parameter space is an open subset of a linear `P3`.
The restricted resultant is

\[
\Delta_0=a_0^2b_2^2+6a_0a_1a_2b_2+4a_0a_2^3-2a_1^3b_2.
\]

In particular, `(a0,b2)` cannot both vanish. Equivalently, the fourth-zero
directions satisfy

\[
2A+zB=q_0=2a_0+b_2z^3.
\]

For example `A=z^2+1, B=-2z` has
`h2=-4/z-8/z^3-3/z^5`, `gammaU=0`,
`gammaV=4+8w^2+3w^4`, and all five fourth coordinates zero. The prior
nonzero sampled direction `A=z^2,B=1` lies outside this locus.

## Every quartic carrier is a cubic multiple, on all charts

Use ambient coordinates `[x:y:Z:W]`, and define

\[
Q=xW-yZ,
\]

\[
\boxed{
T=Q(2a_0a_1x+2a_0a_2y+a_1b_2Z+a_2b_2W)
+a_0^2(x^2Z-y^3)+a_0b_2(xZ^2-y^2W)
-\frac{b_2^2}{4}(yW^2-Z^3).
}
\]

This cubic is in the ideal of `C0`; its first normal symbol is
`-q0(B,-A)/2`. It contains the canonical primitive triple and quadruple.
The universal verifier checks the latter directly through third order in
`ell`, using the unique gluing correction for the quadruple.

The first-symbol image of ambient quartics in `I(C0)` has dimension 17,
with kernel `kQ^2`; its three missing linear combinations are
`Qnormal_2=P_1/2`, `Qnormal_5=P_4/2`, `Qnormal_8=P_7/2`.
For direction `(B,-A)` on the fourth-zero locus, an admissible symbol is
`h(B,-A)`, with

\[
h\in\langle1,z,z^3,z^4,z^6,z^7\rangle.
\]

Thus its quartic lift has seven coefficients, the six coefficients of
`h` and the coefficient `k` of `Q^2`. Restricting these lifts to the
canonical triple gives the following seven-by-seven matrix, with columns
ordered `(h0,h1,h3,h4,h6,h7,k)` and rows ordered by the coefficient of
`z^0,...,z^6` in the quadratic normal jet:

\[
\begin{pmatrix}
a_0a_2b_2&-a_0a_1b_2&-2a_0^2a_2&0&0&0&a_0^2\\
-a_0b_2^2/4&0&a_0^2b_2/2&0&-a_0^3&0&0\\
0&a_0b_2^2/4&0&-a_0^2b_2/2&0&a_0^3&0\\
a_2b_2^2/2&-a_1b_2^2/2&-a_0a_2b_2&-a_0a_1b_2&-2a_0^2a_2&2a_0^2a_1&a_0b_2\\
-b_2^3/8&0&a_0b_2^2/4&0&-a_0^2b_2/2&0&0\\
0&b_2^3/8&0&-a_0b_2^2/4&0&a_0^2b_2/2&0\\
0&0&0&-a_1b_2^2/2&-a_0a_2b_2&a_0a_1b_2&b_2^2/4
\end{pmatrix}.
\]

Its minor in zero-based rows `(0,1,2)` and columns `(4,5,6)` is
`-a0^8`; that in rows `(4,5,6)` and columns `(0,1,6)` is
`-b2^8/256`. Because `Delta0 != 0` implies `(a0,b2) != (0,0)`, these
two minors cover every admissible direction and prove rank at least three.
The four independent quartics `xT,yT,ZT,WT` lie in the kernel. The cubic
is never zero: its `y^3` coefficient is `-a0^2`, and its `Z^3`
coefficient is `b2^2/4`. Hence these multiples are linearly independent,
proving rank exactly three on the full resultant-open locus.

For the primitive triple `Y3` and quadruple `Y4`, this proves

\[
\boxed{
H^0(\mathcal I_{Y_3}(4))=
H^0(\mathcal I_{Y_4}(4))=
T\,H^0(O_{\mathbf P^3}(1)).
}
\]

An equivalent compact solution of the matrix is

\[
h=q_0(c_0+c_1z+c_3z^3+c_4z^4),\qquad
k=2a_1b_2c_1+4a_0a_2c_3.
\]

The coincidence between the fourth-zero locus and the rank-two exceptional
quartic first-symbol direction locus is independently obtained in the
local-cohomology direction investigation. It explains why a generic
first-symbol rank count would miss this family.

## Consequence for hypothetical complete intersections

For a quasiprimitive complete intersection `(4,b)` supported on `C0`,
the checked filtration duality in `2026-10-05-uniform-multiplicity.md`
gives, when `L=O(-5)`, top defect degree `b-7`. At `b=7` the entire
structure is primitive. At `b=8`, superadditivity and complementary
divisor duality force `D2=D3=0`, so its canonical fourth structure is
primitive. Thus either branch requires a direction in the classified
fourth-zero locus and its defining quartic must contain `Y3`.

The carrier theorem forces `F4=T*H` with `H` a nonzero linear form.
For any homogeneous mate `Gb` of positive degree, `V(H,Gb)` is a
projective plane curve or the whole plane. It is contained in
`V(F4,Gb)`, and it cannot be contained in the nonplanar integral curve
`C0`. Therefore `V(F4,Gb)` cannot have support exactly `C0`.

This excludes the **e=2 branches** of `(4,7)` and `(4,8)` on `C0`.
The same argument excludes any `(4,b)` whose e=2 canonical quadruple is
primitive. It does not exclude e=0 or e=1 at these degrees, nor e=2
structures with a defect before the fourth layer, nor carriers of higher
degrees. The cubic `T` can be singular at the zeros of `q0`; its existence
does not furnish a smooth supporting surface or an STCI construction.

## Reproduction and continuation evidence

One repository-local command verifies the full calculation, including
exact ideal membership and all-chart rank minors:

```sh
python research/computations/verify_primitive_quadruple_universal.py
```

It requires SymPy and Macaulay2's `M2`. The verified session used
`/private/tmp/stci-cas-venv/bin/python` and Macaulay2 1.26.06. The script
does not depend on other files under `/private/tmp`. It regenerates its
inspectable scratch equations, derives all jets with sparse polynomial
arithmetic, checks ten directions against the original independent
rational-series implementation, verifies the universal cubic restrictions,
and runs exact Macaulay2 certificates. The ten sample comparisons are
cross-checks; the global conclusions come from the polynomial identities,
resultant-localized membership certificates, and covering minors.

The durable files are `verify_primitive_quadruple_universal.py`,
`scratch/primitive47universal/{generate.py,equations.json,classify.m2}`,
and `scratch/primitive47universal/{quartic_contact.py,quartic_contact.json,
quartic_contact.m2}`. The independent theoretical reconstruction is in
`2026-10-05-primitive-carrier-theory.md`; the frontier-audit lane is
checking the quadratic cocycle and contact matrix by a separate
Bezout-independent computation.

A tempting fifth-order exclusion also fails for the sample
`A=z^2+1,B=-2z`: its fifth obstruction is zero, as recorded with exact
Laurent coefficients in the theory note. The productive next question is
therefore the uniform ambient compatibility of an e=2 primitive triple,
and then the remaining case `deg D2=1`; increasing sampled primitive
orders does not address the ambient quartic factor obstruction.
