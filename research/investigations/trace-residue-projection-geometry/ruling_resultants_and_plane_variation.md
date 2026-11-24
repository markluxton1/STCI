# Ruling resultants on one quadric and normal variation along endpoint planes

Exploratory elementary calculation, pending independent review. Governing question: calculate M_1 on the full translated-cycle CI realization locus. No universal vanishing asserted. Classical inputs are the Chow product formula and proper CI Chow/resultant identity, already established in [the coefficient dictionary](../../arguments/torus/chow_arrangement_moments.md). See also [complementary projections](complementary_projections.md), [quadratic components](quadratic_chow_components.md).

Write [z:x:y:w], C_(u,v)=[s^4:s^3t:u st^3:v t^4], q=u/v. For a cycle Z with multiplicities n_i and sum m, put h_Z(T)=prod(1-Tq_i)^n_i. On Q(T): zw=Txy use [T s0 r0:s1 r0:s0 r1:s1 r1]. For an actual proper pair (F_a,G_b), ab=4m, its two binary ruling resultants on the Segre chart are, after dividing by the same nonzero constant Res(F|L,G|L),
\[
 \operatorname{Res}_r=(s_0s_1)^{ab}h_Z(T),\qquad
 \operatorname{Res}_s=(r_0r_1)^{ab}h_Z(T)^3.
\]
This follows from the homogeneous complementary-projection formulas. At T=0 the parametrization degenerates into z=0; identities hold polynomially there, but are not assertions that this Segre map remains a morphism at its base point. For T outside the spectral roots and nonzero, the intersection on the smooth quadric is supported at the two endpoints, with total length ab at each (intersect the CI cycle with the quadric; the restriction of zw-Txy is (1-Tq_i)zw on each component, order four at each endpoint). Multiplicity of the ruling resultant at each spectral root counts the degree of the corresponding curve over the ruling, times cycle multiplicity. The 1:3 ratio does not itself imply first-moment vanishing.

## Exact Chow restrictions and first normal variation

On the marked graph chart z=Ax+By, w=Cx+Dy, normalized Chow form R_Z has R_Z(0)=1. At p_infty use r=s/t; points are [r^4:r^3:u r:v]. Plane z=Ax cuts three stationary endpoint points and one moving point r=A. Plane z=By cuts one stationary point and three moving points r^3=uB. Since these plane sections never meet w=0 except when the plane contains the opposite endpoint (which it does not in these chart equations), the normalized Chow factors follow by evaluating 1-(C r^3+D u r)/v. Thus
\[
 R_Z(A,0,C,D)=\prod_i(1-q_i AD-v_i^{-1}A^3C)^{n_i},
\quad
 R_Z(0,B,C,D)=\prod_i((1-q_i BC)^3-u_i q_i^3 B D^3)^{n_i}.
\]
For the second identity use prod_{r^3=uB}(a-br)=a^3-b^3 uB. These are exact polynomial identities, not a truncation. Similarly at p0 with r=t/s, the plane w=Dy cuts three stationary points and one moving r=qD; w=Cx cuts one stationary and three moving r^3=C/v. Evaluate 1-Ar-Bur^3 to obtain
\[
 R_Z(A,B,0,D)=\prod_i(1-q_i AD-u_iq_i^3 BD^3)^{n_i},
\quad
 R_Z(A,B,C,0)=\prod_i((1-q_i BC)^3-v_i^{-1}A^3C)^{n_i}.
\]
Define N_infty=sum n_i u_i q_i^3 and N_0=sum n_i/v_i. Then the normal derivatives along the full affine chart of lines in z=0 and w=0, respectively, are
\[
 (\partial_A,\partial_B) R_Z|_{A=B=0}=(-DM_1,-3CM_1-D^3N_\infty),
\]
\[
 (\partial_C,\partial_D) R_Z|_{C=D=0}=(-3BM_1-A^3N_0,-AM_1).
\]
The first of these is linear in the first normal equation data (F_z,G_z)|_{z=0} for actual pairs, with the whole plane restrictions (F,G)|_{z=0} fixed. The second likewise uses (F_w,G_w)|_{w=0}. All restrictions of these plane pairs to lines avoiding the respective endpoint have nonzero resultant, constant under the chart normalization. The actual normal derivative of the binary resultant must equal the displayed polynomials for all C,D or A,B. This is an explicit calculation on the entire two endpoint-plane charts, not merely a scalar at L. Their shared binary restriction is (f,g); the normal data and plane data come from the same two homogeneous equations. M_1=0 is precisely the identically vanishing normal derivative in the single-moving-point directions (A along z=0, D along w=0). No condition N_0=N_infty=0 is asserted.

Next: compare the two plane-source linear response identities for arbitrary actual translated CI pairs. Keep the full configurations and allow repeated components. Determine what same-source compatibility imposes on the linear parts; do not assume equality of the two ruling derivatives. The extra cubic terms carry the second transverse character and may constrain compatibility without classifying carriers.
