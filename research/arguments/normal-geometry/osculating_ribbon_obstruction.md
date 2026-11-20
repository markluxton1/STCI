# The osculating ribbon and all its embedded triple extensions

Work in characteristic zero with the fixed quartic
\(C_0=[s^4:s^3t:st^3:t^4]\). The conormal quotient defined by its
osculating planes has kernel \(M=\mathcal O_{\mathbf P^1}(-8)\) and
quotient \(L=\mathcal O_{\mathbf P^1}(-6)\). Its canonical embedded
extension class is
\[
  2[u^{-2}]\ne0\quad\text{in }H^1(\mathbf P^1,M^\vee L^2)
                         =H^1(\mathbf P^1,\mathcal O(-4)).
\]
Thus the associated ribbon has no embedded primitive triple in
\(\mathbf P^3\). The argument concerns this fixed quotient; it is not
an exclusion of every thickening or every osculating carrier. Among pure
CM triples containing this fixed ribbon and generically curvilinear along
the curve, the least second-layer defect has degree two. The minimal
triples form a projective line with involution-paired defect divisors.
The same bundle classifies every larger defect: degree three has an
explicit determinant condition, and every divisor of degree at least
four occurs. These triples are not Gorenstein at their defects.

## Proof retaining the moving base coordinate

On \(x_0=1\), put \(u=x_1\), \(X=x_3-u^4\), \(Y=x_2-u^3\).
On \(x_3=1\), use \(c=x_2/x_3\),
\(A=x_0/x_3-c^4\), \(B=x_1/x_3-c^3\). To first order,
\[
 A-2cB=-u^{-8}(X-2uY)\pmod{(X,Y)^2},\qquad
 B=u^{-6}Y\pmod{(X,Y)^2+(X-2uY)}.
\]
These transitions identify \(M,L\). The kernel \(X-2uY\) is the
osculating direction: in the moving-cover coordinates \(y=Y\),
\(q=X-uY\), it is \(q-uy\).

A primitive triple extending the ribbon would locally be
\(X=2uY+\alpha(u)Y^2,\ Y^3=0\), with \(\alpha\) regular on
the affine chart. Exact substitution in the ambient coordinate change gives
\[
\begin{aligned}
c&=u^{-1}-u^{-4}Y+(-u^{-5}\alpha+2u^{-7})Y^2,\\
B&=u^{-6}Y+(2u^{-7}\alpha-5u^{-9})Y^2,\\
A&=2u^{-7}Y+(3u^{-8}\alpha-10u^{-10})Y^2.
\end{aligned}
\]
In particular \(A-2cB=(-u^{-8}\alpha+2u^{-10})Y^2\).
The opposite-chart equation \(A=2cB+\beta(c)B^2\) would require
\[
                    \beta(1/u)=-u^4\alpha(u)+2u^2.
\]
Regular polynomials \(\alpha,\beta\) cannot satisfy this identity:
the \(u^2\) term is in neither chart's coboundary range. Dividing by
\(u^4\) gives the stated nonzero Laurent class. The
[canonical embedded-extension theorem](formal-normal-intersection.md#the-canonical-embedded-extension)
shows that these local equations cover all primitive triple lifts, not
merely a chosen coordinate ansatz. The
[raw integral transitions](../arithmetic/z4_lifting_and_deformation.md#raw-integral-normal-coordinates)
provide the same coordinate change. The class here differs from the
\(-6[u^{-2}]\) class for the distinguished arithmetic ribbon: the
quotient direction is different.

## Sharp defect degree and the actual minimal triples

Suppose a higher thickening has a finite-flat quasiprimitive saturated
order flag beginning with this ribbon. Write \(E_2=L^2(D_2)\), where
\(D_2\) is the effective divisor of its **actual multiplication**
\(L^2\to E_2\). Write \(I=I_{C_0}\) and \(J_2\) for the ribbon
ideal. Restriction to its length-three truncation gives a
map from the canonical extension \(\mathcal E\) to \(E_2\):
\(I J_2+I^3\) maps to the third layer and vanishes there. Hence the
extension class must map to zero in \(H^1(\mathcal O(-4)(D_2))\).
Serre duality identifies \(2[u^{-2}]\) with the middle-coefficient
functional on binary quadratics. It is not evaluation at a point, so
\(\deg D_2\ge2\). At degree two the divisor's binary equation must
be \(a s^2+c t^2\). Thus the two defects are paired by \(u\mapsto-u\),
including a doubled endpoint. This is the
[residual involution of osculating planes](../curve/special_plane_and_line_sections.md#3-osculation-and-its-residual-involution),
not merely a numerical degree coincidence.

The minimum is realized, with all local surjectivity conditions retained.
Put \(m_0=X-2uY\), \(\ell_0^2=Y^2\). The canonical extension has
transitions
\[
 m_\infty=-u^{-8}m_0+2u^{-10}\ell_0^2,\qquad
 \ell_\infty^2=u^{-12}\ell_0^2.
\]
For \(E_2=\mathcal O(-10)\) with frame \(e_\infty=u^{-10}e_0\),
all maps are given by
\[
 \phi(m_0)=2c e_0,\quad \phi(\ell_0^2)=(a+cu^2)e_0;
 \qquad
 \phi(m_\infty)=2a e_\infty,\quad
 \phi(\ell_\infty^2)=(a/u^2+c)e_\infty.
\]
The maps for \((a,c)=(1,0),(0,1)\) identify
\(\mathcal E\simeq\mathcal O(-10)^2\); their local determinant is
\(-2\). Every nonzero pair gives a surjection, including at the
zeros of the multiplication section. By the
[one-step extension criterion](../one_step_boundary_repair.md#2-exact-one-step-repair-theorem),
its kernel pulled back to \(J_2\) is an ambient ideal defining a pure
CM triple. Conversely any degree-two-defect triple supplies such a map.
Up to target scalar, these embedded triples therefore form \(\mathbf P^1\).

Locally at a defect the ideal is
\((x^2,xy,y^2-f(t)x)\), with \(\operatorname{ord}f\) its multiplicity.
It is free over \(k[[t]]\) with basis \(1,y,x\). At \(f=0\) the
Artin fibre has square-zero maximal ideal of dimension two, hence CM
type two. These triples are non-Gorenstein at their defects and cannot
be local complete intersections there. The classification below retains
the surjectivity condition in every defect degree.

## All pure CM triples containing the fixed ribbon

Let \(Z\supset Z_2\) be a pure CM triple containing the ribbon with
ideal \(J_2\). No additional global retraction or finite-flat flag is
needed for this length-three assertion. At the generic point, its
length-three algebra has \(I^3=IJ_2=0\). Purity therefore gives these
equalities on \(\mathcal O_Z\) everywhere. The kernel
\(T=J_2/I_Z\) is killed by \(I\), has rank one on \(C_0\), and
has no punctual torsion. Thus it is a line bundle
\(T=\mathcal O(d-12)\), and the triple supplies a surjection
\[
 \mathcal E=J_2/(IJ_2+I^3)\simeq\mathcal O(-10)^2
                         \longrightarrow\mathcal O(d-12).
\]
Conversely the kernel of \(J_2\to\mathcal E\to T\) is an ambient
ideal because \(I\) kills \(T\). The resulting exact sequence
\(0\to T\to\mathcal O_Z\to\mathcal O_{Z_2}\to0\) proves purity,
Cohen--Macaulayness and generic length three. This direct argument also
covers zero multiplication, beyond the cited criterion's prescribed
nonzero power inclusion. The computed splitting identifies the map
with a pair
\[
 (A,C)\in H^0(\mathcal O(d-2))^2,
 \qquad A,C\text{ have no common zero},
\]
modulo simultaneous nonzero scalar. Its actual second multiplication is
\[
                         f=s^2A+t^2C.                 \tag{1}
\]
The triple is generically curvilinear exactly when \(f\ne0\); then
\(d=\deg\operatorname{div}(f)\) is its actual defect degree.
In particular \(d\ge2\). This classifies embedded ideals containing
the fixed ribbon, not merely abstract isomorphism types.

For \(d=2\), (1) recovers the projective line above. For \(d=3\),
write \(f=a_0s^3+a_1s^2t+c_0st^2+c_1t^3\). Its unique lift is
\(A=a_0s+a_1t,\ C=c_0s+c_1t\). It gives a triple exactly when
\(a_0c_1-a_1c_0\ne0\). Thus vanishing of the cohomological
obstruction alone is insufficient even in degree three.

For every \(d\ge4\), **every nonzero binary form \(f\) of degree
\(d\) occurs**. Indeed \((s^2,t^2)_d=H^0(\mathcal O(d))\), and
all solutions of (1) differ by
\[
                 (A,C)\longmapsto(A+t^2H,C-s^2H),
                   \qquad H\in H^0(\mathcal O(d-4)).
\]
A common zero can occur only at a zero of \(f\). At each such point,
the values of \(A,C\) lie in the one-dimensional kernel of
\((s^2,t^2)\), and evaluation of \(H\) is onto. Hence failure of
surjectivity there removes one proper affine hyperplane from the space
of solutions. Over the infinite ground field their finite union cannot
exhaust it. For a fixed divisor, choosing a representative \(f\)
identifies the embedded triples with this nonempty open subset of an
affine space of dimension \(d-3\). Multiple roots impose no additional
surjectivity condition. At every defect the local ideal is still
\((x^2,xy,y^2-f(t)x)\), so the type-two/non-Gorenstein conclusion
holds in every positive defect degree.

There is also one noncurvilinear triple. If \(f=0\), the pair is
\((t^2H,-s^2H)\); having no common zero forces \(d=4\) and
\(H\) constant and nonzero. Its ideal is \(I^2\), the first
infinitesimal neighborhood, outside the quasiprimitive sector.

The extension/surjection mechanism and local defect normal form are
classical [Bănică--Forster constructions](../../literature/README.md#embedded-multiple-curves-and-the-osculating-quotient).
The explicit class, splitting and resulting divisor classification are
the calculations specific to this quotient.

For the generically curvilinear triples \((f\ne0)\), equivalently
\([A:C]\) is a map \(\mathbf P^1\to\mathbf P^1\)
of degree \(d-2\), and the defect is its coincidence divisor with
\([-t^2:s^2]\). Constants give the minimal involution fibres, while
degree-one maps explain the cubic determinant condition.

## Characteristic and the meaning of osculation

The algebraic statements for the **fixed quotient** \(X-2uY\) hold
over every algebraically closed field of characteristic different from
two. The integral transitions, nonzero class \(2[u^{-2}]\), splitting
determinant \(-2\), and surjection arguments need no other restriction.

In characteristic three this quotient is not singled out as the unique
osculating direction: the second Hasse derivative of
\([1:u:u^3:u^4]\) vanishes, so every tangent-containing plane has
contact at least three. The chosen plane family still has divisor
\(3p+(-p)\), but uniqueness of its osculating interpretation is not
claimed there. Nor does the algebraic extension broaden the
characteristic-zero moving-cover theorem: in characteristic three
\((t-ps)^4\) is already in the ambient linear series. At characteristic
two the obstruction and splitting argument change, and are not covered.

## Carrier consequences and limits

Generic osculation of a carrier alone does not supply a higher embedded
thickening or its flag. The classified triples do not construct a supported
CI or a mate. Their non-Gorenstein defects do not preclude a later
Gorenstein thickening: that is a separate embedded-extension and
actual-equation question. Since every divisor of degree at least four
is realized, defect placement alone gives no further exclusion there.

An **actual** pure solely supported CI on a generically regular
osculating carrier does supply the flag. Its generic algebra is
\(k(C_0)[y]/y^n\). Intersecting its powers of \((y)\) with
\(\mathcal O_Y\) gives saturated sheaves \(\mathcal F_i\) whose
successive quotients are \(I\)-annihilated torsion-free rank-one
sheaves on the smooth curve, hence line bundles. Multiplication respects
the flag, and the first conormal quotient has saturated kernel
\(M=\mathcal O(-8)\). Its rank-three truncation is therefore one
of the classified triples. In particular its actual \(\deg D_2\)
is at least two. This implication uses the supplied CI, not the carrier
alone.

If a degree-\(a\) carrier is generically regular along \(C_0\) and
has this osculating first symbol, that nonzero symbol lies in
\(H^0(M(a))=H^0(\mathcal O(4a-8))\). Its zero divisor has degree
\(4a-8\), and the carrier is singular along the curve at those zeros.
If it contains one of the classified triples, the local ideal shows
that its first symbol is divisible by the actual multiplication section:
\(D_2\le\operatorname{div}(\text{first symbol})\), so
\(2\le\deg D_2\le4a-8\) in the generically curvilinear case.
For a generically singular carrier the symbol is identically zero, so
there is no such finite zero divisor. The
[exact moving-conductor length](../linkage/conductor_on_a_smooth_carrier.md#exact-length-at-the-moving-osculating-point)
uses a general regular point and does not erase these global defects.

Independent proof review reconstructed the transitions, nonzero extension
class, splitting, classification in every defect degree, local
non-Gorenstein type and conditional carrier consequence on November 20,
2026. Separate geometric review checked the odd-characteristic extension
and the exceptional osculating interpretation in characteristic three.
The actual-CI flag and first-symbol divisibility were separately checked.
