# Two quadratic Chow components and the first normal source jets

Exploratory comparison; no new universal vanishing claimed. The governing question is hyperplane containment of the full translated-cycle CI realization locus. Companion to [complementary projections](complementary_projections.md) and [research map](README.md).

## Two components

On the graph chart z=Ax+By, w=Cx+Dy at L=V(z,w), normalize the Chow form by its value at L in the marked Plucker trivialization. Its quadratic term for every translated cycle is
\[
 -M_1(AD+3BC)=-2M_1(AD+BC)+M_1(AD-BC).
\]
Rank-one tangent matrices describe pencils of lines through a fixed point in a fixed plane. The determinant part vanishes on every such pencil. This is the elementary symmetric-square / exterior-square decomposition of quadratic forms on a tensor product of two 2-dimensional spaces (characteristic zero). The normalization uses the marked coordinate splitting; not an arbitrary trivialization of the Chow line bundle.

The local origin of 1:3 is visible at the opposite endpoint, in w=1 with parameter r=s/t: z=r^4/v, x=r^3/v, y=u r/v. The section z=Ax has three stationary sheets at r=0 and one moving sheet r=A; the complementary equation w=Dy detects 1-q AD. The section z=By has one stationary sheet and three moving sheets r^3=uB; the complementary equation w=Cx detects (1-q BC)^3. Normalize at the disjoint line. This is the same geometric calculation as the complementary ruling pushforwards, now in the two pencil deformations.

## General cycle comparison (classical trace/residue, no CI hypothesis)

Work over algebraically closed characteristic-zero k. For any pure cycle missing L, let c_AD,c_BC denote the respective coefficients in the formal logarithm of its normalized Chow form (log only through degree two is needed). Write T_0 for the constant Laurent coefficient of the ordinary spectral trace T and S for the constant differential trace. On normalized branches over z=0 use w=1, h=z/w, a=x/w,b=y/w. The classical Chow section product and residue theorem give
\[
 c_{AD}=-\sum n_P\,\mathrm{res}_P(a\,db/h),\qquad
 c_{BC}=-\sum n_P\,\mathrm{res}_P(b\,da/h).
\]
Indeed the derivative at A=0 of the weighted sum of b on h-Aa=0 is the derivative of sum res b dlog(h-Aa), i.e. -sum res b d(a/h)=sum res a db/h; the Chow section product supplies the minus sign. The other coefficient follows by exchanging a,b. Therefore
\[
 c_{AD}+c_{BC}=-T_0,\qquad c_{AD}-c_{BC}=S.
\]
For the sum use res d(ab/h)=0 and the residue of ab dh/h^2; for the difference use the opposite endpoint sign for the differential trace. This is an elementary consequence of the classical Chow product and residue-trace compatibility (Tate, [Residues of differentials on curves](https://www.numdam.org/articles/10.24033/asens.1162/)). It also explains the trace and differential trace as the two coefficients of a single quadratic Chow term, rather than introducing them independently. On translated cycles all linear terms vanish so log and normalized Chow coefficients agree in degree two; T_0=4M_1 and S=2M_1 recover -M_1,-3M_1.

## Source-side question

For an actual CI, use the classical Chow-resultant identity. Write F=f+zp+wq+zw h_F+... and G=g+zr+ws+zw h_G+..., omitting pure normal squares and higher terms. In the AD chart (z,w)=(Ax,Dy) and the BC chart (z,w)=(By,Cx) the mixed second variation of the binary pair is identical: xy(h_F,h_G). It cancels in the difference of the two mixed resultant coefficients, or of their logarithms. The remaining difference depends only on first normal jets, and the established first-jet residue bridge identifies it with Res_(f,g)(ps-qr) on the translated locus. Thus the determinant component is exactly the part of quadratic Chow variation not detected by rank-one pencils and not dependent on second normal equation jets.

The target can now be formulated as equality of the two mixed coefficients for every actual translated-cycle CI realization: c_AD=c_BC. The 1:3 relation, which holds on ALL translated cycles, would then imply both are zero. This is not proved; arbitrary CI pairs need not have equal coefficients. No claim that existence of a resultant, or any one plane-section restriction, gives equality. The useful open question is what simultaneous compatibility of the same two homogeneous equations with the two ruling projections constrains this difference. Keep the full Chow realization locus primary; no classification of sole-support structures is needed.
