# First-order control for the simultaneous Jacobian relations

The [simultaneous Jacobian relations](jacobian_sections.md) come from the entire
translated cycle. This control tests what their restrictions modulo \((z,w)^2\)
imply, even when the minors come from the same two homogeneous equations.

Over characteristic zero, write coordinates z,x,y,w and take the actual homogeneous quartics
\[
 F=x^4+z(x^2y+xy^2)+\tfrac32 zw x^2,\qquad
 G=y^4+w(3xy^2-x^2y)-\tfrac12 zw y^2.
\]
They form a proper pair since the restrictions x^4,y^4 to L=V(z,w) are coprime. This example tests the first-order equations outside the translated-cycle locus. Write D_ij for their actual ambient Jacobian minors (ordered z,x,y,w). Work in the first normal neighborhood R=S/(F,G,(z,w)^2), so the derivatives must be taken before imposing the truncation. Put
\[
 P=x^3y^2+\tfrac14 zx^2y^2-\tfrac94 wx^3y,\quad
 Q=x^2y^3+\tfrac14 zxy^3-\tfrac94 wx^2y^2.
\]
Direct polynomial reduction in R gives all of
\[
 D01=wQ,\quad D02=-3wP,\quad D03=2yP=2xQ,\quad
 D13=-3zQ,\quad D23=zP,
\]
\[
 xD12=4zwP,\quad yD12=4zwQ,\quad xyD12=2zwD03.
\]
For verification expand the actual derivatives, then reduce by z^2=zw=w^2=0, x^4=-z(x^2y+xy^2), y^4=-w(3xy^2-x^2y). All nine congruences were independently checked by exact Gröbner reduction over \(\mathbf Q\). In the central quotient k[x,y]/(x^4,y^4),
\[
 D03=2x^3y^3,\qquad \operatorname{Res}_{x^4,y^4}(D03)=2.
\]
Thus the central scalar that would be M1 for a full translated realization is 1, despite simultaneous first-order compatibility of all the stated minor identities. Actual closedness and decomposability of the ambient wedge hold identically, since it is dF wedge dG. The truncation kills the \(zw\) terms of the spectral-Jacobian relation. Any global vanishing argument using that relation needs a condition beyond these first-order congruences.
