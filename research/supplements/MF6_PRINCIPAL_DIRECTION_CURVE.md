# The principal direction sextic has an elliptic normalization

This is the actual parameter curve from the fixed-C0 principal
\(e=1,d_2=1\) contact calculation, not a curve of realized STCI mates.
The contact-space and candidate-determinant applications keep their own
hypotheses. Work first over an algebraically closed field of characteristic
zero. In the affine chart \(b=1\), its equation is
\[
\begin{aligned}
H(p,r)={}&8p^3-(64r^2+128r+16)p^2\\
&+(96r^4+512r^3+592r^2+128r+6)p\\
&-576r^6-960r^5-880r^4-544r^3-220r^2-60r-9.
\end{aligned}
\]
The corresponding weighted homogeneous curve has weights
\(\operatorname{wt}(p,r,b)=(2,1,1)\). All missing projective and contact
charts remain in that original curve; a birational chart is not a claim
that every contact frame is regular.

Put
\[
x=r+\tfrac12,\quad W=(p+2-4x)/x^2,\quad
A=-W^3+8W^2-12W+72,\quad C=2(W^2-6W+36).
\]
Direct substitution gives the exact identity
\[
H(-2+4x+Wx^2,x-\tfrac12)=-8x^4(Ax^2-2Cx+C).
\]
The quadratic in x has discriminant
\(8W^2(W-6)(W^2-6W+36)\). Its cubic factor has three distinct roots,
so this discriminant is not a square even over an algebraic closure of
the constant field. There is also no polynomial content in W:
\(C-A=W^2(W-6)\), while \(C(0)=C(6)=72\), so \(\gcd(A,C)=1\).
Finally \(H(p,-1/2)=8p(p+2)^2\) is not the zero polynomial, so no
component was lost on x=0. These observations prove geometric integrality
of the original direction curve, not merely irreducibility of a sampled
quadratic fiber.

On \(xWA\ne0\), set \(Y=(Ax-C)/W\). Then
\[
Y^2=2(W-6)(W^2-6W+36),\qquad x=(C+WY)/A.
\]
The latter equation recovers \(r=x-1/2\) and \(p=-2+4x+Wx^2\),
so the displayed maps are birational. With
\(X_E=2(W-4),Y_E=2Y\), the normalization has Weierstrass model
\[
\boxed{Y_E^2=X_E^3+96X_E-448},\qquad
\Delta=-143327232=-2^{16}3^7,\quad j=2048/3.
\]
It therefore has genus one. The same explicit birational argument and
nonzero discriminant apply after reduction in characteristic other than
two or three; this does not transport the contact-space or mate-exclusion
arguments without their additional hypotheses.

The [exact identity checker](../computations/verify_session_mf6_principal_elliptic_2026_10_08.py)
retains the literal H, inverse map, nonsquare discriminant, corrected
\(r=-1/2\) fiber and elliptic invariants. The earlier incorrect expression
\(8(p+2)^3\) for that fiber is not retained as a mathematical claim.
The geometric integrality and genus explanation is the proof above;
an existing recorded execution is reused, with no fresh rerun or
assertion that the candidate parameter locus is empty.
