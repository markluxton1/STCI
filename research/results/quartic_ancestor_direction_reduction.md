---
id: STCI-R-0071
type: result
title: Direction reduction for the fixed quartic common-ancestor incidence
scope: "#scope"
statement: "#statement"
proofs:
  - name: finite moments and actual multiplication
    at: "#proof"
    using: [STCI-R-0020]
    review:
      state: accepted
      basis: reconstructed
      at: "#review"
---
# Direction reduction for the quartic common-ancestor incidence

## Scope

Work over an algebraically closed field \(k\) of characteristic zero, with
\[
C_0=[s^4:s^3t:st^3:t^4],\quad S=k[x,y,z,w],\quad
I=(q,A,B,C),\quad M=H_I^2(S),
\]
where \(q=xw-yz,\ A=x^2z-y^3,\ B=xz^2-y^2w,\ C=yw^2-z^3\).
Fix the independent socle classes
\[
u=\frac{xz}{qB},\qquad v=\frac{yw}{qB}.
\]
The finite statement concerns \(\alpha\in E=(0:_M I^4)_{-7}\) of
principal-part order four, with pure cubic top, and actual quartics
\(F,G\in I_4\) satisfying \(F\alpha=u,\ G\alpha=v\).
The [existing finite reduction](../supplements/LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md#uniform-finite-reduction-for-the-remaining-degree-four-locus)
puts every common ancestor with degree-four multipliers into this setting.

On \(x=1\), use the balanced frame
\[
V=z-t^3,\qquad U=w-t^4-\tfrac32tV.
\]
Describe the top in divided-power coordinates by
\[
c_i=h\,p^i r^{3-i},\qquad 0\le i\le3.
\]
Here \((p,r)\) is the affine expression of a primitive pair of binary forms
of common degree \(e\), and \(h\) is a binary form of degree \(7-3e\).
Primitivity includes both parameter endpoints. The common first-normal
form is \(m=rU-pV\).

## Statement

Every such common quartic ancestor has \(e=1\), and each of \(p,r\) is
nonzero at both toric endpoints. After the actual torus action and common
direction scaling it therefore has
\[
p=1+t,\qquad r=b+ct,\qquad bc(b-c)\ne0.
\]
There is a necessary direction equation
\[
(2-b)P_{12}(b,c)=0,
\]
where the degree-twelve polynomial \(P_{12}\) is defined by the exact
six-by-six determinant in [the remaining interface](#remaining-interface).
This includes all possible lower principal parts and all actual quartic
multiplier choices on the excluded direction strata.

More explicitly, the proof excludes every constant direction, every
quadratic direction, and every linear direction with a component zero at
either toric endpoint. It leaves the actual two-target incidence on the
displayed line and curve as an open problem.

## Proof

### The finite top and lower tests

The [finite-bound proof](../supplements/LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md#a-finite-principal-part-bound-for-quartic-local-cohomology-ancestors)
first forces \(F,G\in I_4\) and ambient coprimality. The generic
intersection length is at most three, using the characteristic-zero
degree-\((4,4)\) exclusion. Torsion-freeness of finite inverse systems
along \(C_0\), and \(H^0_{\mathfrak m}(M)=0\), then give \(I^4\alpha=0\)
globally. The order-three argument excludes the lower-order possibility.
The balanced normal bundle, supplied by R-0020, gives \(e\le2\).
These are the antecedents of the all-stage quartic consequence.

The [audited tensor reconstruction](../validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.m2)
identifies \(E\) with a thirty-dimensional space of numerators
\(H/(q^4B^4)\), \(H\in S_{13}\). It checks the full \(I^4\) annihilation
condition, injectivity of the Ext-stage map, all eighteen actual quartic
columns, all 540 products and both targets. Its target space has dimension
74 and equals the complete degree-\(-3\) next-stage Ext image.

Write \(c_{i,j}\) for the coefficient of \(t^j\) in \(c_i\). The top map
\(\Theta:k^{30}\to k^{32}\) has rank 29. Its image is defined exactly by
\[
\begin{aligned}
5c_{0,0}-6c_{1,1}-4c_{2,2}-8c_{3,3}&=0,\\
c_{0,2}-8c_{3,5}&=0,\\
c_{0,4}+2c_{1,5}+12c_{2,6}-40c_{3,7}&=0.
\end{aligned}
\]
Thus every admissible nonzero top has the complete affine lift fibre
\(\alpha=\alpha_{\rm top}+\ell\kappa\), with
\(\ker\Theta=k\kappa=H^0(\mathcal T_3(-7))\).
The verifier chooses its section and kernel by rational row reduction of
the existing top map.

Let \(\mu_j\) denote the residue functional of \(\alpha\) on homogeneous
normal polynomials of degree \(j\). For a quartic
\(F=F_1+F_2+F_3+\cdots\), with normal-homogeneous \(F_j\), the exact
multiplication tests are
\[
\begin{array}{ll}
\mu_3(QF_1)=0 & Q\in\{U^2,UV,V^2\},\\
\mu_2(LF_1)+\mu_3(LF_2)=0 & L\in\{U,V\},\\
\mu_1(F_1)+\mu_2(F_2)+\mu_3(F_3)=1. &
\end{array}
\]
The corresponding last right side for \(G\) is \(t^2\).
These are the principal-part form of the recorded full tensor equations.
For example the socle normalization follows directly from
\[
B=V(t^3+V)-t^2q,\quad xz=t^3+V,\quad
yw=t^2(t^3+V)+tq.
\]
Their residues in \(q,V\) are \(1,t^2\), and \(q=U+tV/2\) has
Jacobian one.

A useful consequence removes multiplier coordinates early. At least one
first symbol is nonzero, since the quartic first-symbol kernel is \(kq^2\)
and the targets are independent. Write that symbol \(F_1=fm\).
Since \(mF\alpha=0\),
\[
0=\mu_2(fm^2)+\mu_3(mF_2)=f\,\mu_2(m^2).
\]
The cubic term vanishes because \(m(p,r)=0\). Hence every ancestor satisfies
\[
\boxed{D=r^2\mu_{20}-2pr\mu_{11}+p^2\mu_{02}=0.}
\tag{1}
\]
Here \(\mu_{ij}=\operatorname{res}(U^iV^j\alpha)\).
This uses the nonzero socle equations with their stated right sides.

The new verifier extracts these moments directly from the existing
numerators. In the \(q,V\) coordinates it expands
\[
B^{-4}
=\sum_{k\ge0}\binom{k+3}{3}
\frac{t^{2k}q^k}{V^{4+k}(t^3+V)^{4+k}}.
\]
Only \(k\le3\) contributes after division by \(q^4\).
Extracting \(q^{-1}V^{-1}\), with \(U=q-tV/2\), reconstructs the saved
cubic top map and all ninety quadratic moments over \(\mathbb Q\).

If \(L_\alpha:k^{18}\to k^{74}\) is the recorded multiplication map and
\(\pi\) is projection modulo \(\langle u,v\rangle\), both targets require
\(\dim\ker(\pi L_\alpha)\ge2\). In the saved coordinates \(\pi\) keeps
rows 0 through 71. The same criterion applies after restricting to the
complete actual first-symbol source of dimension \(n\), with required
projected rank at most \(n-2\).

### Constant directions

The [pure-axis proof](../supplements/LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md#independent-audit-of-pure-constant-quartic-directions)
excludes the two axes, including zero-symbol multiplier boundaries.
For mixed constants the ambient torus acts transitively on directions,
so normalize \((p,r)=(1,1)\).
The three top equations and (1) give exactly
\[
(h_0,\ldots,h_7)=
\left(a,b,c,\frac{5a-6b-4c}{8},
-\frac c4-12d+40e,\frac c8,d,e\right),
\]
\[
\ell=\frac{-85a+110b-736c+3520d-10880e}{672}.
\]
The resulting five-dimensional ancestor space is injectively
parameterized by \((a,b,c,d,e)\).

The complete first-symbol quartic source has dimension eight. It is the
kernel of the coefficient matrix of
\[
\left(F_z+(1+\tfrac32t)F_w\right)(1,t,t^3,t^4),
\]
whose rank is ten on the eighteen actual quartics.
Contract the full tensor with this source and project modulo the target
pencil. Constant rational row relations give an equivalent
eleven-by-eight matrix \(T(a,b,c,d,e)\) of linear forms.
Both targets would require \(\operatorname{rank}T\le6\).

Set \(P=[128:64:0:2:1]\). The exact projected rank at \(P\) is four.
In the affine chart \(e=1\), every seven-by-seven minor therefore vanishes
through order two at \(P\). Its cubic jet lies in the span of the
three-by-three minors of the seven-by-four linear matrix
\[
L\,T(a,b,c,d,0)\,R,
\]
where \(L,R\) are rational left and right nullspace bases of \(T(P)\).
This follows by putting the rank-four constant matrix into block form
and taking the degree-three term of each determinant.
The exact dimension of that cubic span is fourteen.

There are 330 homogeneous degree-seven forms in five variables.
The order-zero, order-one and order-two conditions give fifteen
independent linear conditions, and the cubic condition gives six more.
Let \(V\) be this 309-dimensional permitted space. The span \(W\) of
the degree-seven minors lies in \(V\).
Reduction of their coefficient matrix over \(\mathbf F_{32003}\) is
defined and has rank 309. Rational rank is at least this modular rank,
so \(W=V\) over \(\mathbb Q\).
In particular
\[
(a-128e)^7,\quad(b-64e)^7,\quad c^7,\quad(d-2e)^7
\]
belong to \(W\), because their jets through degree three vanish at \(P\).
Thus the projective rank-at-most-six locus consists exactly of \(P\).
At \(P\) the full restricted multiplication rank is four, and adjoining
either target raises it to five. This excludes \(P\) and the entire
mixed constant orbit over every characteristic-zero extension.

### Quadratic directions

Here \(h\) is linear. The actual torus and reversal reduce its zero to
the endpoint case \(h=t\) or the interior case \(h=1+t\), up to nonzero
scalar. The torus acts on normal-dual directions by
\[
(p(t),r(t))\longmapsto
(\lambda^4p(t/\lambda),\lambda^3r(t/\lambda)).
\]
Reversal sends a degree-two pair to
\[
\left(\tfrac12t^2r(1/t),\,2t^2p(1/t)\right).
\]
It exchanges the two endpoint component conditions, and fixes the
interior zero orbit. It also exchanges \(u,v\) up to a nonzero scalar.

Primitivity at zero gives two complete charts. Write
\[
p=1+at+bt^2,\quad r=c+dt+et^2,
\]
or, when \(p(0)=0\),
\[
p=at+bt^2,\quad r=1+dt+et^2.
\]
The degree-two binary resultant used throughout is
\[
\mathcal R=(p_2r_0-p_0r_2)^2
 -(p_2r_1-p_1r_2)(p_1r_0-p_0r_1).
\]
Its nonvanishing expresses projective primitivity under every specialization.

For \(h=t\), the ideals of the three top equations and all coefficients
of (1), saturated by \(\mathcal R\), are the unit ideal in both charts.
This excludes every endpoint top, including all lower corrections.

For \(h=1+t,\ p(0)=0\), the saturated ideal is exactly
\[
\begin{gathered}
4a^2+4a+5=0,\quad 4b+2a-3=0,\quad
2d+2a+5=0,\\
e-2a+5=0,\qquad 14\ell+246a-115=0.
\end{gathered}
\]
Over \(\mathbb Q(i)\), the projected actual tensor has rank seventeen
at \(a=-1/2+i\). Rational conjugation covers its other root. Each
fibre therefore has at most one quartic preimage of the target pencil.

For \(h=1+t,\ p(0)=1,\ r(0)=0\), the exact saturated equations are
\[
a^2+1=0,\quad 2b+a-1=0,\quad d+a+1=0,\quad
e-2a+4=0,\quad 7\ell-2a+2=0.
\tag{2}
\]
On the open \(be\ne0\), equation (1) and primitivity imply
\(p\mid\mu_{20}\) and \(r\mid\mu_{02}\).
Their pseudo-remainders, together with the top equations, have the
following exact saturated ideal after eliminating \(e\) by the first
top equation,
\[
4b+2a-3c-2=0,\quad 2d+2a+5c+2=0,\quad
5c^2+4ca+4a^2+8c+4=0.
\tag{3}
\]
The last equation is \(4(a+c/2)^2+4(c+1)^2=0\).
The verifier checks these saturated ideal equalities over \(\mathbb Q\).
If \(b=0\) or \(e=0\), reversal puts the direction into one of the
two component-zero charts already retained. This proves coverage of
the complete projective direction space.

One conjugate component of (3) is
\[
a=-c/2+i(c+1),\quad
b=(2-2a+3c)/4,\quad d=-a-1-5c/2,\quad e=2a-4-5c.
\]
Its primitivity polynomial, up to a nonzero scalar, is
\[
(c+1)^2\left(c^2+\left(\tfrac12-\tfrac92i\right)c-\tfrac12-3i\right).
\]
The constant coefficient of (1) has \(\ell\)-coefficient \(7c\).
It forces a polynomial \(\ell(c)\). At \(c=0\) its value is
\((2i-2)/7\), precisely (2). Thus it covers every lower correction
on the primitive component.

For this \(\alpha(c)\), two seventeen-by-seventeen minors of
\(\pi L_{\alpha(c)}\) have degrees 51 and 31. Their exact gcd becomes
a unit after removing factors of the displayed primitivity polynomial.
The rows and columns are specified in the verifier. Hence every primitive
point has projected rank at least seventeen. Rational conjugation covers
the second component. This excludes every quadratic direction.

### Linear directions at the endpoints

Reversal moves a component zero at infinity to zero. Primitivity and the
actual torus then give exactly four types
\[
(p,r)=(at,1),\quad(at,1+t),\quad(1+t,ct),\quad(1,t),
\]
with \(a\ne0\) or \(c\ne0\) in the respective parameter families.
For the first two families, scaling the curve parameter fixes \(a\)
and normalizes the other linear coefficient to zero or one.
For the third and fourth, the torus sends the two remaining coefficients
to \(a/\lambda,c/\lambda^2\). Algebraic closedness supplies the square
root in the fourth normalization.

Let \(h=\sum_{j=0}^4h_jt^j\). Form \(N\) in
\((h_0,\ldots,h_4,\ell)\) from the three top equations and the first
three coefficients of (1). For the first two families,
\[
\det N=\frac7{18}a^3(2a-1)^3
\prod_{f\in\mathcal A}f(a),
\]
where
\[
\mathcal A=\{4a^2+2a+1,\ 4a^2+4a+5,\ 20a^2+4a+1,\
4a^3-8a^2-3a-1,\ 16a^3+12a^2+8a-1\}.
\]
For the third,
\[
\det N=\frac{896}{9}c^3
(3c^6-38c^5+183c^4-360c^3+4c^2+528c-640).
\]
All eleven simple-factor cases are checked over their complete exact
quotient fields. The full top and quadratic equations give a
one-dimensional ancestor space in each. Adjoining either target to the
full actual multiplication map increases its rank by one.

The three rational exceptions \((t/2,1),(t/2,1+t),(1,t)\) each leave a
three-dimensional ancestor space and a seven-dimensional actual
first-symbol source. In the rational kernel coordinates
\((z_0,z_1,z_2)\) chosen by the verifier, the projected tensor has a
nine-by-seven constant row compression. Its saturated six-minor ideals
are respectively
\[
(z_0,z_1)^4,\quad
(22z_0-7z_2,\ 44z_1+7z_2)^4,\quad
(z_0+2z_2,z_1)^4.
\]
Each leaves one projective support point. The full multiplication rank
there is three, and either target increases it to four. This proves the
linear endpoint exclusion and completes the stated direction reduction.

## Remaining interface

Every surviving direction now has \(p=1+t,\ r=b+ct\) and
\(bc(b-c)\ne0\). Form \(N(b,c)\) from the same three top equations and
the coefficients of \(t^0,t^1,t^2\) in (1). Define
\[
P_{12}(b,c)=
\frac{36\det N(b,c)}{7(2-b)^3(b-c)^3}.
\]
The verifier checks that this is a polynomial of total degree twelve
with 49 terms. A nonzero ancestor requires \(\det N=0\), giving the
line \(b=2\) and the curve \(P_{12}=0\) on the stated open.

On each part, retain the full kernel in
\((h_0,\ldots,h_4,\ell)\), impose every coefficient of (1), and test
\[
L_\alpha f=e_{72},\qquad L_\alpha g=e_{73}
\]
in the full seventy-four-row tensor, with actual eighteen-coordinate
quartics. Ambient coprimality remains a necessary condition from the
all-stage low-degree theorem. Both nonzero target equations remain.

The [socle-pencil and conormal splitting](../supplements/LOCAL_COHOMOLOGY_CONORMAL_GEOMETRY.md#intrinsic-conormal-splitting-required-by-every-common-quartic-ancestor)
give \(d_3=4\) in this degree-one lane.
The [primitive-triple exclusion](../supplements/OCT7_LOCALCOH_ENDPOINT_AND_SIMULTANEOUS_TARGETS.md#simultaneous-target-repair-for-primitive-e1-quartic-ancestors)
and [complete degree-one-defect exclusion](../supplements/OCT8_LOCALCOH_AND_CONDUCTOR_ENDPOINTS.md#1-the-entire-e1d21-common-quartic-ancestor-lane)
leave \(d_2=2,3,4\), with their separately excluded algebraic and
quadric-direction fibres removed. These are geometric conditions to
retain when resolving the displayed line and curve.

## Evidence

The only new exact support is
[the replay verifier](quartic_ancestor_direction_reduction.support/verify.py).
It reads the existing numerator, top-map, quartic-basis and full-tensor
files in `research/computations`. It reconstructs quadratic and cubic
residues, checks all five quadratic chart ideals, the two projected
tensor minors, the constant-orbit ranks, all linear endpoint fields
and exceptional projective loci, and the interior determinant.
Temporary Macaulay2 input is generated outside the repository.

Replay from the repository root with Python 3.12 or later, SymPy 1.14.0
and Macaulay2 1.26.06 on `PATH`,

```sh
python3 research/results/quartic_ancestor_direction_reduction.support/verify.py
M2 --script research/validation/2026-10-08-family2-quadratic-audit/actual-tensor-reconstruction.m2
python3 research/computations/verify_localcoh_pure_direction_audit.py
```

All three commands were completed on 2026-11-10 with Python 3.12.16,
SymPy 1.14.0 and Macaulay2 1.26.06. The original full tensor was
reconstructed literally. The new calculation uses rational arithmetic,
complete exact number fields, and one certified modular linear-rank
lower bound accompanied by the rational upper bound proved above.

## Review

The finite moment reduction and quadratic direction proof received an
independent reconstruction. The reviewer recomputed all ninety quadratic
moments by the inverse \(q,B\) coordinate change, replayed the five
rational saturated ideals, and independently checked both conjugate
component-zero fibres by restriction of scalars to \(\mathbb Q\).
An independent first-lower-contact calculation in the actual
six-dimensional quartic source gave two five-by-five minors with
monic gcd \((c+1)^{11}\), confirming the primitive conic coverage.
The maintained verifier retains the full-tensor route.

The constant-orbit reviewer independently reconstructed the
fourteen-dimensional cubic space, checked the dimension-309 argument,
and replayed the direct tensor binding and modular coefficient rank.
This establishes characteristic-zero coverage of the entire projective
ancestor family. The linear boundary was independently reconstructed
from the four normalization cases, determinant factors, complete-field
kernel calculations and three exceptional saturated minor ideals.
The integrated verifier was replayed in the owning checkout.

During review a draft residue loop omitted the \(q^0V^4\) contribution
to the quadratic moments. Its bounds were corrected before the final
replay. The corrected quadratic and cubic coefficients agree with the
independent reconstruction. Acceptance covers the three excluded
direction strata and the necessary interior direction equation.
The line-and-curve two-target incidence remains unresolved.

## Limitations

The characteristic, embedding, quartic multiplier degrees and two fixed
targets are part of every claim. The primitive linear interior incidence
still needs its full lower multiplication test.
The [generic length theorem](../supplements/LOCAL_COHOMOLOGY_DIRECTION_AND_APOLARITY.md#2026-10-05-localcoh-generic-length)
would give a proper common-ancestor pair generic length three along
\(C_0\) and residual cycle degree four. Sole-support carrier theorems
have their own support hypotheses. Non-quasi-cyclicity of the entire
module quantifies over higher multiplier degrees as well. The
unrestricted characteristic-zero STCI question remains open.
