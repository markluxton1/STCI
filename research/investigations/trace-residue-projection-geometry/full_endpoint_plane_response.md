# Full first-order plane-section motion and source Jacobian classes

Exploratory elementary calculation; independent review pending. The task remains calculation on the full CI realization locus. Companion to [ruling resultants](ruling_resultants_and_plane_variation.md). Classical inputs: Newton identities and the finite CI residue-trace theorem (Cattani–Dickenstein–Sturmfels, [Computing Multidimensional Residues](https://arxiv.org/abs/alg-geom/9404011)). No universal vanishing asserted. Work over algebraically closed k of characteristic zero.

At p_infty set w=1, use r=s/t, so (z,x,y)=(r^4/v,r^3/v,q r). Move z=0 to z=epsilon(a x+b y+c). The section polynomial is r^4-epsilon(a r^3+b u r+c v). To first order Newton gives sums of r,r^2,r^3,r^4 equal to epsilon times a,0,3bu,4cv; all higher powers have zero first derivative. For a whole translated cycle define L_infty^a(h),L_infty^b(h),L_infty^c(h) as first variations of weighted section sums in these three directions. With N_infty=sum n_i u_i q_i^3,
\[
 L^a(h)=M_1[y]h,\quad L^b(h)=3M_1[x]h+3N_\infty[y^3]h,\quad
 L^c(h)=4M_1[xy]h+4N_\infty[y^4]h.
\]
At p0 set z=1, use r=t/s, (w,x,y)=(v r^4,r,u r^3). Move w=epsilon(a x+b y+c), section polynomial r^4-epsilon(b q r^3+a r/v+c/v). With N_0=sum n_i/v_i, the respective responses are
\[
 L^a_0(h)=3M_1[y]h+3N_0[x^3]h,\quad
 L^b_0(h)=M_1[x]h,\quad L^c_0(h)=4M_1[xy]h+4N_0[x^4]h.
\]

## Actual equations

At p_infty write f=F(0,x,y,1),g=G(0,x,y,1), P=F_z(0,x,y,1),Q=G_z(0,x,y,1). Leading binary forms are coprime (L is disjoint); f,g have sole common point origin and quotient length ab=4m. Put J=f_x g_y-f_y g_x, U=Q f_y-P g_y, V=P g_x-Q f_x. For any polynomial h and plane direction ell=ax+by+c the first variation is
\[
 L^\ell(h)=\operatorname{Res}_{f,g}(\ell(Uh_x+Vh_y)).
\]
Proof: on simple fibers differentiate the two root equations and solve the 2x2 system by Cramer; then extend the identity to the open of coprime leading forms using regularity of finite-flat traces and global residue (or rational coefficient formulas with leading resultant invertible). This applies to nonreduced endpoint sections; does not divide by J in their algebra.

The product rule now extracts the two entire residue functionals without solving a system:
\[
 \operatorname{Res}(Uh)=L^c(xh)-L^a(h)=3M_1[y]h,\quad
 \operatorname{Res}(Vh)=L^c(yh)-L^b(h)=M_1[x]h+N_\infty[y^3]h.
\]
At p0 use f=F(1,x,y,0),g=G(1,x,y,0), P=F_w,Q=G_w in same chart, and same definitions J,U,V. Then
\[
 \operatorname{Res}(Uh)=M_1[y]h+N_0[x^3]h,\quad
 \operatorname{Res}(Vh)=3M_1[x]h.
\]
By perfect CI residue pairing these identities determine the actual classes U,V in each endpoint section algebra, not merely their traces. Let j=J/(ab) be normalized socle, characterized by Res(jh)=h(0). In the infinity algebra:
\[
 xU=y^2U=0,\quad yU=3M_1j,\quad xV=M_1j,\quad y^4V=xyV=0.
\]
In the zero algebra:
\[
 yU=M_1j,\quad x^4U=xyU=0,\quad yV=x^2V=0,\quad xV=3M_1j.
\]
In particular the single-moving-sheet response U at infinity and V at zero vanishes as an algebra element exactly when M_1=0. These are restrictions of the same homogeneous Jacobian minors: U=-D_zy,V=D_zx at infinity; U=-D_wy,V=D_wx at zero (D_ij=F_iG_j-F_jG_i). With the appropriate homogeneous w or z multiplying J, the displayed degree-one socle identities homogenize on the endpoint planes. This is a concrete same-source comparison problem. The endpoint identities themselves come from cycle geometry and actual CI residue pairing; they do not yet show that these two specific minors vanish. Do not treat them as independent evidence for M_1=0 or infer equality of the two mixed Chow coefficients.
