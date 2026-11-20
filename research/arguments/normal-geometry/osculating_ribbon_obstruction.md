# The osculating ribbon does not extend to a primitive triple

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
an exclusion of every thickening or every osculating carrier.

## Proof retaining the moving base coordinate

On \(x_0=1\), put \(u=x_1\), \(X=x_3-u^4\), \(Y=x_2-u^3\).
On \(x_3=1\), use \(c=x_2/x_3\),
\(A=x_0/x_3-c^4\), \(B=x_1/x_3-c^3\). To first order,
\[
 A-2cB=-u^{-8}(X-2uY),\qquad B=u^{-6}Y
                 \pmod{(X,Y)^2, X-2uY}.
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

## Consequences and limits

Suppose a higher thickening has a finite-flat quasiprimitive saturated
order flag beginning with this ribbon, with invertible second quotient
\(E_2=L^2(D_2)\) and effective defect divisor \(D_2\). Then
\(D_2\ne0\): otherwise its length-three truncation would be the
forbidden primitive triple. Generic osculation alone does not supply
this flag, and a positive defect may absorb the obstruction.

If a degree-\(a\) carrier is generically regular along \(C_0\) and
has this osculating first symbol, that nonzero symbol lies in
\(H^0(M(a))=H^0(\mathcal O(4a-8))\). Its zero divisor has degree
\(4a-8\), and the carrier is singular along the curve at those zeros.
For a generically singular carrier the symbol is identically zero, so
there is no such finite zero divisor. The
[exact moving-conductor length](../linkage/conductor_on_a_smooth_carrier.md#exact-length-at-the-moving-osculating-point)
uses a general regular point and does not erase these global defects.

Independent proof review reconstructed the transitions, the nonzero
extension class and both conditional consequences on November 20, 2026.
