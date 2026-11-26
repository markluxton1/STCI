# Complementary coordinate projections and Chow restrictions

Provisional calculation for the [trace and projection investigation](index.md).

Write [z:x:y:w] and C_(u,v)=[s^4:s^3t:u st^3:v t^4], q=u/v, eta=u^2/v. Three coordinate pairings define rational maps to P^1 x P^1; each is resolved by blowing up the two corresponding disjoint coordinate lines. Their common permutohedral refinement also resolves the consecutive-ratio product map. The first two are the two ruling projections on each Q_q: xy=qzw. The maps on C have degrees 1 and 3 onto graphs of bidegree (1,1), respectively. The third maps with degree 2 onto the graph eta lambda=beta^2 of bidegree (1,2) in ([z:w],[x:y]).

## Homogeneous Chow restriction formulas

For each pairing the joining lines of points in the two complementary coordinate lines form a P^1 x P^1 in Gr(2,4); restriction of the CI Chow form equals the binary resultant of the actual F,G restricted to that joining line. It has bidegree (ab,ab)=(4m,4m). For the first pairing use [a0:a1]=[z:x], [c0:c1]=[y:w]. For the second use [b0:b1]=[z:y], [d0:d1]=[x:w]. For the third use [l0:l1]=[z:w], [h0:h1]=[x:y]. Up to nonzero scalar, the three restrictions are
\[
R_1=a_1^{3m}c_0^{3m}\prod_i(a_1c_0-q_i a_0c_1)^{n_i},
\quad
R_2=b_1^m d_0^m\prod_i(b_1d_0-q_i b_0d_1)^{3n_i},
\]
\[
R_3=l_0^m l_1^m\prod_i(h_1^2 l_0-\eta_i h_0^2 l_1)^{2n_i}.
\]
Check componentwise using the resultant on its parameter P^1: for pairing one the two hyperplane equations restrict to s^3(a0 t-a1 s), t^3(c0 v t-c1 u s); for pairing two to s(b0 u t^3-b1 s^3), t(d0 v t^3-d1 s^3); for pairing three to l0 v t^4-l1 s^4, st(h0 u t^2-h1 s^2). Multiplicativity of the resultant gives the displayed factors including endpoint contributions. The formula holds at cycle level even without CI; for CI each expression is the resultant of the same two homogeneous surfaces in different joining-line families. Boundary factors cannot be dropped from actual homogeneous resultant identities.

## Common center L=V(z,w)

On the Grassmannian chart of lines z=A x+B y, w=C x+D y, normalized Chow form equals 1 at zero. Its quadratic part for a translated cycle is -M_1(AD+3BC). To check: on B=C=0 the first restriction is prod(1-q_i AD)^n_i, and on A=D=0 the second is prod(1-q_i BC)^(3n_i). There are no other quadratic monomials and no linear terms because intrinsic torus weights on A,B,C,D are -1,-3,3,1 (line coordinates transform with weight difference). In particular on A=C=-p,B=D=-r the quadratic term is -4M_1 pr, recovering the existing plane-section Chow coefficient. Thus the 1:3 ruling degrees are precisely the relative weights of the two mixed Hessian terms. This is a cycle-level identity, not a CI consequence. The Hessian vanishes exactly when M_1=0 in characteristic zero.

## Product map

The consecutive ratios (alpha,beta,gamma)=(x/z,y/x,w/y) give Q'_q: alpha=q gamma, and the translated graph beta=eta q gamma^2. The two marked base points of the (alpha,gamma) pencil yield the same direction parameters (reciprocal under the opposite local coordinates). The spectral equation homogenizes to bidegree (m,m), and M_1 is its first mixed coefficient normalized at the appropriate marked corner. A homogeneous degree-d source maps on the product torus to F(1,alpha,alpha beta,alpha beta gamma). Its exponent set is the staircase simplex 0<=k<=j<=i<=d in the alpha,beta,gamma exponents, equivalently the pullback of the original degree-d linear system with its boundary constraints. This describes precisely which product equations descend as original homogeneous surfaces, without a carrier choice. The third resultant separately remembers eta, but the full paired transverse Chow polynomial remains necessary to encode correlation of q and eta.

## Ruling resultants on one quadric

Write [z:x:y:w], C_(u,v)=[s^4:s^3t:u st^3:v t^4], q=u/v. For a cycle Z with multiplicities n_i and sum m, put h_Z(T)=prod(1-Tq_i)^n_i. On Q(T): zw=Txy use [T s0 r0:s1 r0:s0 r1:s1 r1]. For an actual proper pair (F_a,G_b), ab=4m, its two binary ruling resultants on the Segre chart are, after dividing by the same nonzero constant Res(F|L,G|L),
\[
 \operatorname{Res}_r=(s_0s_1)^{ab}h_Z(T),\qquad
 \operatorname{Res}_s=(r_0r_1)^{ab}h_Z(T)^3.
\]
This follows from the homogeneous complementary-projection formulas. At T=0 the parametrization degenerates into z=0; identities hold polynomially there, but are not assertions that this Segre map remains a morphism at its base point. For T outside the spectral roots and nonzero, the intersection on the smooth quadric is supported at the two endpoints, with total length ab at each (intersect the CI cycle with the quadric; the restriction of zw-Txy is (1-Tq_i)zw on each component, order four at each endpoint). Multiplicity of the ruling resultant at each spectral root counts the degree of the corresponding curve over the ruling, times cycle multiplicity. The 1:3 ratio does not itself imply first-moment vanishing.

## Symmetric and alternating quadratic components

On the graph chart z=Ax+By, w=Cx+Dy at L=V(z,w), normalize the Chow form by its value at L in the marked Plucker trivialization. Its quadratic term for every translated cycle is
\[
 -M_1(AD+3BC)=-2M_1(AD+BC)+M_1(AD-BC).
\]
Rank-one tangent matrices describe pencils of lines through a fixed point in a fixed plane. The determinant part vanishes on every such pencil. This is the elementary symmetric-square / exterior-square decomposition of quadratic forms on a tensor product of two 2-dimensional spaces (characteristic zero). The normalization uses the marked coordinate splitting; not an arbitrary trivialization of the Chow line bundle.

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

For an actual CI, use the classical Chow-resultant identity. Write F=f+zp+wq+zw h_F+... and G=g+zr+ws+zw h_G+..., omitting pure normal squares and higher terms. In the AD chart (z,w)=(Ax,Dy) and the BC chart (z,w)=(By,Cx) the mixed second variation of the binary pair is identical: xy(h_F,h_G). It cancels in the difference of the two mixed resultant coefficients, or of their logarithms. The remaining difference depends only on first normal jets and equals the residue by the [first-jet residue bridge](../../arguments/torus/spectral_jacobian_first_jet_bridge.md). Thus the determinant component is exactly the part of quadratic Chow variation not detected by rank-one pencils and not dependent on second normal equation jets.

Equality of the mixed coefficients for all full translated-cycle CIs would prove UM1. The restriction identities hold componentwise and leave this simultaneous source question open.
