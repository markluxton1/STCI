# Endpoint-plane response of the Chow form and the actual Jacobian

Provisional calculation for the [trace and projection investigation](index.md).
Use the notation of the [scope](index.md#scope) and the [Chow restrictions](projection_resultants.md).

## Exact Chow restrictions and first normal variation

On the marked graph chart \(z=Ax+By,\ w=Cx+Dy\), normalize the Chow
form \(R_Z\) to \(R_Z(0)=1\). At \(p_\infty\), use \(r=s/t\) and
parametrize by \([r^4:r^3:u r:v]\). The plane \(z=Ax\) cuts three
stationary sheets and one moving sheet \(r=A\). The plane \(z=By\) cuts
one stationary sheet and three moving sheets \(r^3=uB\). Both plane
sections are contained in \(w\ne0\), where evaluating the second plane
equation gives \(1-(C r^3+D u r)/v\). The Chow products are
\[
 R_Z(A,0,C,D)=\prod_i(1-q_i AD-v_i^{-1}A^3C)^{n_i},
\quad
 R_Z(0,B,C,D)=\prod_i((1-q_i BC)^3-u_i q_i^3 B D^3)^{n_i}.
\]
For the second identity take the product of the three linear evaluations
over \(r^3=uB\). At \(p_0\), using \(r=t/s\), the plane \(w=Dy\) cuts
three stationary sheets and one moving sheet \(r=qD\). The plane \(w=Cx\)
cuts one stationary sheet and three moving sheets \(r^3=C/v\).
Evaluating \(1-Ar-Bur^3\) gives
\[
 R_Z(A,B,0,D)=\prod_i(1-q_i AD-u_iq_i^3 BD^3)^{n_i},
\quad
 R_Z(A,B,C,0)=\prod_i((1-q_i BC)^3-v_i^{-1}A^3C)^{n_i}.
\]
Set \(N_\infty=\sum_i n_i u_i q_i^3\) and \(N_0=\sum_i n_i/v_i\).
The normal derivatives along the full affine charts of lines in \(z=0\)
and \(w=0\), respectively, are
\[
 (\partial_A,\partial_B) R_Z|_{A=B=0}=(-DM_1,-3CM_1-D^3N_\infty),
\]
\[
 (\partial_C,\partial_D) R_Z|_{C=D=0}=(-3BM_1-A^3N_0,-AM_1).
\]
For actual pairs the first response is linear in \((F_z,G_z)|_{z=0}\)
with the plane pair fixed. The second uses \((F_w,G_w)|_{w=0}\).
In each chart the restricted plane pair has constant normalized
resultant \(1\), and its normal resultant derivatives must equal the
displayed polynomials throughout the chart. The common binary pair on
\(L\), the plane data and both normal derivatives come from the same
two equations. Vanishing in the single-moving-sheet directions is
equivalent to \(M_1=0\).

## First variation of all endpoint trace tests

In \(w=1\), move \(z=0\) to \(z=\epsilon(\alpha x+\beta y+\gamma)\).
On a translated branch the section polynomial is
\(r^4-\epsilon(\alpha r^3+\beta u r+\gamma v)\). Newton identities
give the first variations of the root power sums of orders \(1,2,3,4\)
as \(\alpha,0,3\beta u,4\gamma v\), and zero for every higher order.
Let \(L^\alpha,L^\beta,L^\gamma\) denote the variations of weighted
section sums, with \([h_0]h\) the coefficient of the monomial \(h_0\)
in a polynomial \(h(x,y)\). Substituting \(x=r^3/v,\ y=qr\) gives
\[
 L^\alpha(h)=M_1[y]h,\quad L^\beta(h)=3M_1[x]h+3N_\infty[y^3]h,\quad
 L^\gamma(h)=4M_1[xy]h+4N_\infty[y^4]h.
\]
In \(z=1\), move \(w=0\) to \(w=\epsilon(\alpha x+\beta y+\gamma)\).
Now \(r=t/s\), \((w,x,y)=(v r^4,r,u r^3)\), and the polynomial is
\(r^4-\epsilon(\beta q r^3+\alpha r/v+\gamma/v)\). The responses are
\[
 L^\alpha_0(h)=3M_1[y]h+3N_0[x^3]h,\quad
 L^\beta_0(h)=M_1[x]h,\quad L^\gamma_0(h)=4M_1[xy]h+4N_0[x^4]h.
\]

## Actual equations

At \(p_\infty\), let \(f=F(0,x,y,1)\), \(g=G(0,x,y,1)\),
\(P=F_z(0,x,y,1)\), and \(Q=G_z(0,x,y,1)\). The leading binary
forms are coprime since \(L\) is disjoint. The quotient has length
\(ab=4m\) and is supported at the origin. Set
\(J=f_xg_y-f_yg_x,\ U=Qf_y-Pg_y,\ V=Pg_x-Qf_x\).
For the plane direction \(\ell=\alpha x+\beta y+\gamma\),
\[
 L^\ell(h)=\operatorname{Res}_{f,g}(\ell(Uh_x+Vh_y)).
\]
On simple fibers differentiate the two root equations and use Cramer's
rule followed by the residue–trace formula. Extend to the open of
coprime leading forms by regularity of finite-flat trace and global
residue. The extension applies to the nonreduced endpoint algebra.

The product rule now extracts the two entire residue functionals without solving a system:
\[
 \operatorname{Res}(Uh)=L^\gamma(xh)-L^\alpha(h)=3M_1[y]h,\quad
 \operatorname{Res}(Vh)=L^\gamma(yh)-L^\beta(h)=M_1[x]h+N_\infty[y^3]h.
\]
At \(p_0\), use \(f=F(1,x,y,0)\), \(g=G(1,x,y,0)\), \(P=F_w\),
\(Q=G_w\) in the same chart, and the same definitions of \(J,U,V\).
Then
\[
 \operatorname{Res}(Uh)=M_1[y]h+N_0[x^3]h,\quad
 \operatorname{Res}(Vh)=3M_1[x]h.
\]
Perfect CI residue pairing determines the classes \(U,V\) in each
endpoint section algebra. Let \(j=J/(ab)\) be the normalized socle
element characterized by \(\operatorname{Res}(jh)=h(0)\). At infinity,
\[
 xU=y^2U=0,\quad yU=3M_1j,\quad xV=M_1j,\quad y^4V=xyV=0.
\]
In the zero algebra:
\[
 yU=M_1j,\quad x^4U=xyU=0,\quad yV=x^2V=0,\quad xV=3M_1j.
\]
The single-moving-sheet classes \(U\) at infinity and \(V\) at zero
vanish as algebra elements exactly when \(M_1=0\). They are
restrictions of the homogeneous Jacobian minors \(U=-D_{zy},\
V=D_{zx}\) at infinity and \(U=-D_{wy},\ V=D_{wx}\) at zero.
Multiplying \(J\) by the appropriate coordinate \(w\) or \(z\)
homogenizes the displayed degree-one socle identities. The two
responses identify the specific classes whose vanishing would prove
UM1, leaving their simultaneous global compatibility open.
