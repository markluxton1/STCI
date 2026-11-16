## Dependency guide: actual projection and ramification boundary

This file derives necessary fiber and singularity conditions using the **complete anticanonical embedding** and the actual projected curve, conditional on the ADE del Pezzo/D5 reduction. Its ramification countershield prevents the false inference that isolated smooth-source ramification is automatically excluded. The [conormal-net reduction](genus_one_ribbon_conormal_net_proof.md) controls the ribbon directions; the [repeated-partition calculation](genus_one_ribbon_partition_proofs.md) handles particular contact strata. Neither should be read as a uniform elimination of all genus-one carriers.

---


Permanent detailed mathematical record, including all proofs, calculations, counterexamples and explicit unresolved conditions.

# Genus-one projection: fiber conditions and ramification counterexample

Status: **PROVED HERE as necessary conditions**, assuming the separately
accepted degree-four ADE del Pezzo normalization and D5 torsion reduction.
This note does not exhaust the remaining projection parameters or exclude
every genus-one carrier. No frontier file is edited.

## 1. Binding the complete embedding to the actual C0

Let a hypothetical quartic mate have normalization S with H=-K_S,
H^2=4 and ADE singularities, in the accepted sectional-genus-one lane.
Its full reduced inverse-image curve c is isomorphic to fixed C0, and
an even mate degree b gives b c~b H. The accepted D5 correction in either
surviving type has order two. Hence 2c~2H, and there is a section Q of
2H with div_S(Q)=2c. This does not assert that Q descends to the quartic.

The complete anticanonical embedding realizes S as an intersection of
two quadrics in P4 and h0(H)=5. The restriction map to c has zero kernel:
a nonzero hyperplane section containing c would have degree four,
so it would be exactly c, making c Cartier. A smooth Cartier curve
cannot pass through a singular surface point, contradicting the D5
correction. Thus H0(S,H) identifies with H0(P1,O(4)); c is a rational
normal quartic in this complete embedding. Choose its coordinates as

    (Y0,Y1,Y2,Y3,Y4)=(s^4,s^3t,s^2t^2,st^3,t^4).

The original projection is exactly deletion of Y2. Write

    (x0,x1,z,x2,x3)=(Y0,Y1,Y2,Y3,Y4).

The six quadrics in the actual rational-normal-quartic ideal are

    q01=x0 z-x1^2,          q02=x0 x2-x1 z,
    q03=x0 x3-x1 x2,        q12=x1 x2-z^2,
    q13=x1 x3-z x2,         q23=z x3-x2^2.

They are linearly independent and span its six-dimensional space of
quadrics. The projection center lies outside S, so the surface pencil
has a member with nonzero z^2 coefficient. A basis may therefore be
chosen as

    Q1=-q12+alpha q01+beta q02+gamma q03+delta q13+epsilon q23
       =z^2+A z+R1,
    Q2=a q01+b q02+c0 q03+d q13+e q23=L z+R,

where c0 is a scalar coefficient, distinct from the curve c. Explicitly

    A=alpha x0-beta x1-delta x2+epsilon x3,
    L=a x0-b x1-d x2+e x3,
    R1=-alpha x1^2+beta x0 x2+gamma(x0 x3-x1 x2)
       +delta x1 x3-epsilon x2^2-x1 x2,
    R=-a x1^2+b x0 x2+c0(x0 x3-x1 x2)+d x1 x3-e x2^2.

Here L is not identically zero. Indeed L=0 forces Q2 to be a multiple
of q03, whose projection would lie on the quadric x0 x3-x1 x2=0;
that contradicts a birational degree-four image. Restriction to c is
injective on linear forms, so L_c is also nonzero.

## 2. Exact fiber condition and the repeated-contact reduction

Set z_c=s^2t^2. On c the linear relation gives R_c=-z_c L_c. The
fiber over a point of C0 with L_c nonzero has its unique point z=z_c.
At a zero of L_c, the equation Q2 imposes no condition, and Q1 has
the roots

    z=z_c,       z=-A_c-z_c.

A mate forces the full inverse support to have no isolated extra point:
an invertible-sheaf section on the integral normalization cannot have
an isolated zero off its only curve component. Hence the necessary and
sufficient condition for singleton geometric fibers along c is

    Supp div(L_c) subset Supp div(D_c),     D_c=A_c+2z_c.

Equivalently, rad(L_c) divides D_c as homogeneous binary polynomials.
This is a support condition, not a scheme divisibility assertion.

The binary quartics are

    L_c=a s^4-b s^3t-d st^3+e t^4,
    D_c=alpha s^4-beta s^3t+2s^2t^2-delta st^3+epsilon t^4.

The middle coefficient of L_c is zero, whereas that of D_c is two.
If L_c had four distinct zeros, the equal degrees and displayed support
condition would imply D_c is proportional to L_c, impossible in
characteristic zero. Therefore every hypothetical mate in this lane
requires

    discriminant(L_c)=0.

Its nonzero conductor hyperplane must meet the rational normal quartic
with a repeated contact. This is a uniform necessary reduction; it does
not depend on choosing either ADE survivor or an explicit family.

Completing the square gives a useful discriminant identity. Let

    z'=z+A/2,     T=A^2/4-R1,     W=R-A L/2.

Then Q1=z'^2-T, Q2=L z'+W and the projected quartic is
W^2-T L^2=0. Along c,

    W_c=-(D_c/2)L_c,       T_c=D_c^2/4.

At a singleton conductor crossing P, if ord_P(L_c)=ell and
ord_P(D_c)=d, then ell>=1, d>=1 and the restriction of the quadratic
discriminant 4T to c has exact order 2d. Its leading coefficient is
the square of the leading coefficient of D_c. These identities alone
do not impose d>=ell or determine the ADE type.

## 3. Exact singularity criterion at a coincident fiber

On the chart s=1, put u=t/s and use the three coordinates normal to c

    v=z-u^2,       w=x2-u^3,       h=x3-u^4,

with x0=1 and x1=u. The normal-gradient rows of Q1,Q2 along c are

    (D(u),B(u),C(u)),       (L(u),B2(u),C2(u)),

where

    D=2u^2+alpha-beta u-delta u^3+epsilon u^4,
    B=beta-(1+gamma)u-delta u^2-2epsilon u^3,
    C=gamma+delta u+epsilon u^2,
    L=a-b u-d u^3+e u^4,
    B2=b-c0 u-d u^2-2e u^3,
    C2=c0+d u+e u^2.

There is no u component because both quadrics vanish on c. At a
coincident fiber D(P)=L(P)=0, the normalization S is singular exactly
when

    B(P) C2(P)-C(P) B2(P)=0.

If this determinant is nonzero, S is smooth there and the projection
has differential of rank one at that point. The opposite affine chart
gives the analogous endpoint condition. A leading quadratic
discriminant zero is consequently not, by itself, a singular-normalization
passage condition.

## 4. Why isolated smooth-source ramification cannot be excluded by the
generic differential lemma

The accepted local-unit differential lemma assumes rank(d nu)<=1
generically along an integral source prime E. That assumption is
essential. Consider the exact local finite normalization

    A=k[u,v^2,uv] subset B=k[u,v],
    X: x^2=u^2 y,       x=uv, y=v^2.

The conductor is (u) in B. Away from its origin the map has rank two;
at u=v=0 it has rank one. The smooth curve c=(v=0) maps isomorphically
onto the u-axis, and the ambient function y has pullback v^2 with
divisor exactly 2c. Every geometric fiber over that curve is a
singleton. Thus an isolated rank-one point on a smooth normalization
can be compatible with both a smooth image curve and a local pure-power
mate. This example is a local countershield, not a projective C0 mate.

In particular one must not conclude that every zero of L_c lies in
Sing(S). Such a stronger conclusion needs an additional argument,
for example one using the entire conductor and global power descent.

## 5. Coverage warning for the two toric surface models

Dolgachev's author-hosted [Classical Algebraic Geometry](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf),
Theorem 8.6.3 and Table 8.6, identify the pencil symbols of 4A1 and
A3+2A1 as [(11)(11)1] and [(21)(11)]. They have at most three marked
pencil points, and the simultaneous quadratic normal form makes each
polarized surface projectively unique. Models are respectively

    ae=c0^2, bd=c0^2;       ab=c0^2, c0 d=e^2.

This uniqueness classifies surfaces, not pairs consisting of a smooth
RNC and the particular middle-coordinate projection. Changing the
parameter on the RNC by PGL2 induces a transformation of P4 and moves
the projection center. Its original direction is the coefficient of
s^2t^2; under a general parameter change that direction is no longer
the deleted middle coordinate. An argument that moves two of the
curve's singular passages to s=0,t=0 must carry the center along.

Consequently the previously excluded four-A1 family, and the new
[A3+2A1 family](https://github.com/markluxton1/STCI/blob/a88e52b20b799ead49699a23a1d4691a96f66cf5/research/supplements/OCT9_DELPEZZO_ROOTS_AND_PROJECTION.md#source-2026-10-09-session-a3-two-a1-projection-familymd),
do not become exhaustive solely because they parametrize smooth RNC
curves on the unique toric models after such a parameter change.
The repeated-root locus of L_c and its global descent conditions remain
the precise continuation target at this note's scope.

## 6. Reproducible evidence

The independent checker
[verify_session_genus_one_projection_2026_10_09.py](https://github.com/markluxton1/STCI/blob/3a50e7675d965bd5fa15084189aaab750620bca3/research/computations/verify_session_genus_one_projection_2026_10_09.py)
verifies the six literal RNC quadrics, both normalized equations, every
normal-gradient entry, the completed-square identities, the local
countershield identities, and all A3+2A1 family identities.
These calculations check the representations of the preceding proofs;
they do not classify every repeated-root projection parameter.

## 7. Exact conductor coordinates and fixed-curve fiber condition

For the genus-one projection of the preceding projection analysis, the fixed rational normal quartic in retained coordinates \((x_0,x_1,x_2,x_3)\) and omitted coordinate \(z\) is \([U^4:U^3V:UV^3:V^4:U^2V^2]\). Write the six defining quadrics as
\[
\begin{aligned}
E_0&=x_0z-x_1^2,&E_1&=x_0x_2-x_1z,&E_2&=x_0x_3-x_1x_2,\\
E_3&=x_1x_2-z^2,&E_4&=x_1x_3-zx_2,&E_5&=zx_3-x_2^2.
\end{aligned}
\]
For a normalized pair \(Q_1=-E_3-aE_0-bE_1-cE_2-dE_4-eE_5\), \(Q_2=fE_0+gE_1+hE_2+iE_4+jE_5\), the entire conductor algebra from the preceding projection analysis has coefficients
\[
\begin{aligned}
A&=ax_0-bx_1-dx_2+ex_3,\\
R_1&=x_1x_2-ax_1^2+bx_0x_2+c(x_0x_3-x_1x_2)+dx_1x_3-ex_2^2,\\
L&=fx_0-gx_1-ix_2+jx_3,\\
R&=-fx_1^2+gx_0x_2+h(x_0x_3-x_1x_2)+ix_1x_3-jx_2^2.
\end{aligned}
\]
With \(z_c=U^2V^2\), restriction to the curve yields \(R_C=-z_cL_C\) and \((R_1)_C=z_c^2-A_Cz_c\). Over a zero of \(L_C\), the two possible omitted coordinates are \(z_c\) and \(A_C-z_c\). The singleton full-inverse-support condition therefore forces
\[
\operatorname{Supp}\operatorname{div}(L_C)\subseteq\operatorname{Supp}\operatorname{div}(A_C-2z_c).
\]
Since \(L_C\) has zero middle coefficient while \(A_C-2z_c\) has middle coefficient \(-2\), a squarefree \(L_C\) is impossible. This is a necessary support condition, not an assertion that all repeated-root strata are excluded by the same argument. The exact symbolic companion is [verify_session_genus_one_entire_conductor_2026_10_09.py](https://github.com/markluxton1/STCI/blob/5484e6f7760cee5f5512c01529856910007151e7/research/computations/verify_session_genus_one_entire_conductor_2026_10_09.py).





## 8. Entire genus-one conductor by graded modules

The conductor identity above admits a short, complete algebraic proof, worth retaining separately from its computational verification. Let \(T=k[x_0,x_1,x_2,x_3]\), \(A_X=T/(F)\), and \(B=T[z]/(Q_1,Q_2)\), where \(Q_1=z^2-Az-R_1\), \(Q_2=Lz+R\), and \(F=R^2+ALR-R_1L^2\). The projection identifies the fraction fields, and the integral degree-four image has equation \(F\), so \(A_X\hookrightarrow B\). The two quadrics form a complete intersection and \(B\) is normal under the genus-one hypotheses.

If \(R\) were divisible by \(L\), the equation \(Q_2\) would factor into linear forms on the integral nondegenerate surface. Hence \(L,R\) form a regular sequence in \(T\), and \(C_\Gamma=T/(L,R)\) is the **entire** coordinate ring of a plane conic, possibly reducible or doubled. In \(B\),
\[
Lz=-R,\qquad Rz=AR-LR_1.
\]
Thus \((L,R)\) annihilates \(B/A_X\), and monicity of \(Q_1\) gives a surjection \(C_\Gamma(-1)\twoheadrightarrow B/A_X\). The Hilbert series are
\[
\operatorname{HS}(B)=\frac{(1+t)^2}{(1-t)^3},\quad
\operatorname{HS}(A_X)=\frac{1+t+t^2+t^3}{(1-t)^3},\quad
\operatorname{HS}(C_\Gamma)=\frac{1+t}{(1-t)^2}.
\]
Since \(\operatorname{HS}(B)-\operatorname{HS}(A_X)=t\operatorname{HS}(C_\Gamma)\), the surjection is an isomorphism **in every graded degree**, not merely after removing finite-length modules. Consequently
\[
B/A_X\cong C_\Gamma(-1),\qquad
\operatorname{cond}(A_X,B)=\operatorname{Ann}_{A_X}(B/A_X)=(L,R).
\]
Moreover, \((L,R)B=(L)\), so the entire upstairs conductor has coordinate ring
\[
B/(L)=C_\Gamma[z]/(z^2-Az-R_1).
\]
It is free of rank two over \(C_\Gamma\), including over doubled or reducible conics. The trace-zero generator \(w=z-A/2\) satisfies \(w^2=A^2/4+R_1\). The calculation fixes the conductor scheme and quadratic algebra without passing to radicals. The fixed-curve coefficient restrictions are established in Section 7 above.

