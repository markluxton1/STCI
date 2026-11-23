# The first moment and the Hilbert-scheme symplectic form

**Status.** Characteristic zero over an algebraically closed field.
The residue lead supplied the interpretation;
the generalizations and algebraic-geometry reviewers independently checked
this written account. No universal
first-moment vanishing follows from the construction alone.

## 1. An exact pullback formula

Write \(z=x_0,w=x_3,x=x_1,y=x_2\). A proper homogeneous CI avoiding
\(L=V(z,w)\) is finite flat of degree \(N=ab\) over \(k[z,w]\),
and hence defines
\[
 f:\mathbf A^2_{z,w}\longrightarrow\operatorname{Hilb}^N(\mathbf A^2_{x,y}).
\]
Let \(\omega_H\) be the classical symplectic form extending
\(\sum_j dx_j\wedge dy_j\) on distinct-point configurations. Then
\[
 f^*\omega_H=
 \operatorname{Res}_{F,G}(F_zG_w-F_wG_z)\,dz\wedge dw.             \tag{HF1}
\]

**Proof.** At a reduced fiber, implicit differentiation at each root gives
\[
 \det\frac{\partial(x_j,y_j)}{\partial(z,w)}
 =\frac{F_zG_w-F_wG_z}{F_xG_y-F_yG_x}(x_j,y_j).
\]
Summing is the ordinary reduced-fiber residue formula. Apply this on the
total universal base (the resultant-nonzero homogeneous CI source times
\(\mathbf A^2_{z,w}\)): both sides of (HF1)
are regular there, and its reduced-fiber locus is dense. The identity
therefore extends over the universal source and specializes to families
whose fibers can be everywhere nonreduced. This argument uses regularity
of the Hilbert-scheme form, not an assumption that a repeated configuration
has independently moving labeled roots. \(\square\)

Grading makes the residue coefficient constant. It equals
\(\operatorname{Res}_{f_0,g_0}(ps-qr)\) on the central binary CI,
with the first normal coefficients as in the
[established first-jet bridge](spectral_jacobian_first_jet_bridge.md#4-the-first-moment-is-a-perfect-residue-pairing-of-first-jets).
For the entire translated cycle that bridge proves, including nilpotents,
\[
                    f^*\omega_H=2M_1\,dz\wedge dw.             \tag{HF2}
\]
Thus UM1 is equivalently isotropy of this particular projection-family
map. Nonzero \(M_1\) would make its differential symplectic, including
at the central binary-Gorenstein point.

## 2. Endpoint collapse and a Gorenstein center do not force isotropy

Consider the actual homogeneous CI
\[
                 F=x^2-zy,\qquad G=y^2-wx.                     \tag{HF3}
\]
Its quotient is free over \(k[z,w]\) on \(1,x,y,xy\): the two monic
relations form a Gröbner basis with relatively prime leading monomials
\(x^2,y^2\). Its central fiber is the Gorenstein CI \((x^2,y^2)\).
Along either parameter axis all fiber support is the origin, so both
axis arcs land in the punctual Hilbert–Chow fiber. Nevertheless
\[
 \operatorname{Tr}(xy)=3zw,\qquad F_zG_w-F_wG_z=xy,
 \qquad\operatorname{Res}_{x^2,y^2}(xy)=1,
 \qquad f^*\omega_H=dz\wedge dw.                              \tag{HF4}
\]
For the trace, multiplication by \(xy\) has diagonal entries
\(0,zw,zw,zw\) in the stated basis. For \(zw\ne0\), its support
consists of the origin and the three nonzero roots
\(x^3=z^2w,\ y=x^2/z\). Projectively the CI is the twisted cubic
\([z:x:y:w]=[s^3:s^2t:st^2:t^3]\) plus the line \(x=y=0\).
It is not a translated-quartic cycle and is not a counterexample to UM1.

This proves that a homogeneous two-equation presentation, finite flatness,
a central Gorenstein fiber and collapse of both axes do not imply (HF2)
vanishes. In particular, the two axis tangent directions at the punctual
fiber point have nonzero symplectic pairing; smooth isotropic-fiber
reasoning cannot be applied to the whole singular tangent space there.

Removing the origin branch gives the flat rank-three ideal
\((x^2-zy,y^2-wx,xy-zw)\), free on \(1,x,y\). Its central fiber
is \((x,y)^2\), which is not Gorenstein. This exhibits a loss of the
CI condition in this control, not a theorem that all residual removal
must have that effect.

## 3. The additional full-support condition

Every generic translated quartet is an orbit of
\(\mu_4\) acting by \((x,y)\mapsto(ix,-iy)\). The quotient coordinates
\(X=x^4,Y=y^4,T=xy\) satisfy \(XY=T^4\), and one quartet has
\[
 X=v^{-1}z^3w,\quad Y=u^4v^{-3}zw^3,\quad T=(u/v)zw.
\]
Hence the symmetric-product cycle map has an exact finite-group symmetry
absent from (HF3). Repeated schemes need not have invariant ideals.
Equivariant Hilbert/quiver constructions therefore require an additional
lift, as in the existing distinction between invariant cycles and ideals.

A useful remaining question is whether a homogeneous finite-flat CI lift
of this full quartet-cycle map can have nonzero pulled-back form while
extending through the central Gorenstein locus. This is unproved. Dropping
the quartet condition is explicitly disproved by (HF3).

The underlying symplectic construction is classical: Beauville,
[*Variétés kählériennes dont la première classe de Chern est nulle*](https://math.univ-cotedazur.fr/u/beauvill/pubs/jdg.pdf).
See §5, Proposition 5 and its proof, pp. 766–767. That construction is
complex analytic. For the affine-plane form here, the distinct-point
formula defines a rational algebraic form over \(\mathbf Q\); regularity
after base change to \(\mathbf C\) descends faithfully flat and then
persists over algebraically closed characteristic-zero fields.
Kuznetsov, [*Quiver varieties and Hilbert schemes*](https://arxiv.org/abs/math/0111092),
is relevant to actual equivariant ideals, not a replacement for the missing
equivariance of an arbitrary nonreduced CI lift. Here we apply the classical
form through the explicit source-residue identity and endpoint countercontrol.
