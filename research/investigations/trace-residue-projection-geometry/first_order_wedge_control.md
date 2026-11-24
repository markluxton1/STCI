# First normal-order compatibility of the full Jacobian wedge is insufficient

Exploratory negative control, pending independent review. This addresses the proposed direct proof of regularity of D03/(zw) from the common origin and closedness of the six Jacobian components. Governing question remains M1 on the entire actual translated-cycle CI locus. It does not disprove UM1. Classical input: Grothendieck residue in the binary CI (Cattani–Dickenstein–Sturmfels, https://arxiv.org/abs/alg-geom/9404011). Compare [adjunction](adjunction_and_coordinate_quotients.md), [logarithmic syzygy](logarithmic_syzygy_and_opposite_lines.md), and the existing [first-jet formula](../../arguments/torus/spectral_jacobian_first_jet_bridge.md).

Over characteristic zero, write coordinates z,x,y,w and take the actual homogeneous quartics
\[
 F=x^4+z(x^2y+xy^2)+\tfrac32 zw x^2,\qquad
 G=y^4+w(3xy^2-x^2y)-\tfrac12 zw y^2.
\]
They form a proper pair since the restrictions x^4,y^4 to L=V(z,w) are coprime. These are NOT asserted to have a translated cycle or even to contain a translate. Write D_ij for their actual ambient Jacobian minors (ordered z,x,y,w). Work in the first normal neighborhood R=S/(F,G,(z,w)^2), so the derivatives must be taken before imposing the truncation. Put
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
For verification expand the actual derivatives, then reduce by z^2=zw=w^2=0, x^4=-z(x^2y+xy^2), y^4=-w(3xy^2-x^2y). These reductions were also checked by exact rational polynomial arithmetic for every displayed identity. In the central quotient k[x,y]/(x^4,y^4),
\[
 D03=2x^3y^3,\qquad \operatorname{Res}_{x^4,y^4}(D03)=2.
\]
Thus the central scalar that would be M1 for a full translated realization is 1, despite simultaneous first-order compatibility of all the stated minor identities. Actual closedness and decomposability of the ambient wedge hold identically, since it is dF wedge dG. This is a negative control on the truncation, not a counterexample to any theorem requiring the entire translated support. The spectral-Jacobian relation in this truncation does not test its zw term, and the full relation is not asserted. No endpoint-support, global annihilator or spectral membership assertion is made for this pair.

Conclusion: one cannot derive D03/(zw) regularity merely from the six first-order relations plus the fact that the ambient two-form is a genuine closed decomposable Jacobian wedge. The missing condition must use more of the full support than those truncated identities. Do not spend further iterations collecting equivalent residue/divisibility formulations. Keep the one test D03 in (F,G,z) and use genuine global restrictions from the original full translated-cycle realization.
