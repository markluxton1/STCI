# The osculating ribbon and its minimal triple repairs

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
an exclusion of every thickening or every osculating carrier. The least
possible second-layer defect has degree two, and the actual minimal CM
triples form a projective line with involution-paired defect divisors.

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
be local complete intersections there. For higher defect degrees,
annihilating the obstruction class alone does not ensure surjectivity
of the extension map. No classification of those triples is claimed.

## Carrier consequences and limits

Generic osculation alone does not supply the finite-flat flag used above.
Its minimal defect triples do not construct a supported CI or a mate.

If a degree-\(a\) carrier is generically regular along \(C_0\) and
has this osculating first symbol, that nonzero symbol lies in
\(H^0(M(a))=H^0(\mathcal O(4a-8))\). Its zero divisor has degree
\(4a-8\), and the carrier is singular along the curve at those zeros.
For a generically singular carrier the symbol is identically zero, so
there is no such finite zero divisor. The
[exact moving-conductor length](../linkage/conductor_on_a_smooth_carrier.md#exact-length-at-the-moving-osculating-point)
uses a general regular point and does not erase these global defects.

Independent proof review reconstructed the transitions, nonzero extension
class, sharp defect minimum, complete degree-two triple classification,
local non-Gorenstein type and conditional carrier consequence on November
20, 2026.
