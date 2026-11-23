# Transverse Chow coefficients and determinantal CI realization

**Scope and status.** Focused reformulation of the existing reduced-cycle
realization theorem, with a self-contained interpolation argument and precise
multiplicity limitations. The evaluation criterion is established in
[Chow-polytope rigidity](../equations/chow_polytope_rigidity.md#realization-of-a-reduced-chow-matched-cycle);
the coefficient/moment dictionary is classical multisymmetric invariant
theory (Vaccarino, *The ring of multisymmetric functions*, Ann. Inst. Fourier
55 (2005), 717–731,
[primary source](https://www.numdam.org/articles/10.5802/aif.2111/)).
The moment-matrix equivalence below is an elementary deduction, **not yet
independently reviewed**. No unrestricted characteristic-zero STCI exclusion
or universal \(M_1=0\) statement is claimed.

## 1. The entire arrangement, without selecting a carrier

Let \(k\) be algebraically closed and let
\[
 C_{u,v}=[s^4:s^3t:u st^3:v t^4]\subset\mathbf P^3,
 \qquad (u,v)\in T=(\mathbf G_m)^2.
\]
An effective degree-\(4m\) cycle with this Chow polytope is
\(\sigma=\sum_i n_i[(u_i,v_i)]\in\operatorname{Sym}^m T\),
with \(\sum n_i=m\). There is no preferred component and no chosen
carrier/mate. The central question is to determine the locus
\[
 R_{a,b}\subset\operatorname{Sym}^m T,\qquad ab=4m,
\]
consisting of cycles realized by **actual proper homogeneous**
surface pairs of degrees \(a,b\).

Embed the transverse torus by the characters \(1,u,v\) into the
projective toric parameter plane:
\[
 (u,v)\mapsto[W:U:V]=[1:u:v]\in\mathbf P^2.
\]
The intrinsic input is the torus character lattice; this projective
embedding is a convenient, nonunique presentation. The full homogeneous
transverse zero-cycle Chow form is
\[
 \mathcal C_\sigma(X,Y,Z)
 =\prod_i(W_iX+U_iY+V_iZ)^{n_i}.
\]
It is well-defined projectively and normalized on \(T\) by
\([X^m]\mathcal C_\sigma=1\). It records **both** paired
transverse coordinates, unlike the ratio-only specialization
\[
 H_\sigma(A,B)
 =\frac{\mathcal C_\sigma(0,-B,A)}{\mathcal C_\sigma(0,0,1)}
 =\prod_i(A-q_iB)^{n_i},\qquad q_i=U_i/V_i=u_i/v_i.
\]
The denominator is a nonzero coefficient on the parameter torus.
Thus
\[
 M_1(\sigma)=\sum_i n_iq_i
 =-[A^{m-1}B]H_\sigma .
\]
In characteristic zero, the universal assertion
\(R_{a,b}\subset V(M_1)\) for **all** bidegrees remains open.
The proof is known in particular low-degree and other restricted
cases; see
[chow realization and first-moment separation](chow_realization_moment_separation.md#2-the-universal-separator-and-its-exact-target).
In positive characteristic the diagonal \(m[(u,v)]\) may itself
satisfy \(M_1=0\) when \(\operatorname{char}k\mid m\).

The trace/norm interpretation of \(H_\sigma\), both extreme mixed
coefficients, the integral (4,4) binomial pair in characteristics
zero/two, and the full cubic/quartic spectral surjectivity are
already developed in
[sections 11–13](chow_realization_moment_separation.md#11-the-two-extreme-mixed-coefficients-of-the-quadric-spectrum-equation).
In particular, all depressed quartic \(H_\sigma\) with nonzero
constant term occur among invariant (4,4) CI arrangements, while
the full \(\mathcal C_\sigma\) remains more restrictive.
Therefore further universal (4,4) constraints cannot consist only
of additional equations in the \(H_\sigma\)-coefficients.

## 1.1 The first moment is already a *linear full-Chow coefficient*

The **existing** quotient-spectrum identity above can be expressed directly
and polynomially in the *full* paired transverse coordinates, without a
division by any individual parameter. Let
\[
 D=\prod_i v_i^{n_i}\ne0,\qquad
 E_{1,m-1}(\sigma)=
 \sum_i n_i u_i v_i^{n_i-1}\prod_{j\ne i}v_j^{n_j}.
\]
Then
\[
 \tag{M}
 \boxed{
  [Z^m]\mathcal C_\sigma=D,\quad
  [YZ^{m-1}]\mathcal C_\sigma=E_{1,m-1}=D\,M_1(\sigma).
 }
\]
Here \(E_{1,m-1}\) is an **elementary multisymmetric function**
of the \(m\) paired points (including repetitions). In particular
\[
 M_1=0\iff
  [YZ^{m-1}]\mathcal C_\sigma=0
 \iff
 \left.\partial_Y\mathcal C_\sigma\right|_{(X,Y,Z)=(0,0,1)}=0.
\]
The last equality can be normalized as
\(M_1=(\partial_Y\mathcal C_\sigma/\mathcal C_\sigma)(0,0,1)\).
This is a **single linear hyperplane condition on the full
projective zero-cycle Chow coefficients**, not merely a rational
condition on the \((u_i,v_i)\). It extends as a polynomial
hyperplane to the entire projective Chow closure, although the
ratio expression needs \(D\ne0\). On the deepest interior diagonal
\(\mathcal C=(X+uY+vZ)^m\), it has value
\(muv^{m-1}\ne0\) in characteristic zero.

There is a geometric toric dictionary which also retains the
second transverse coordinate. In the parameter plane
\([W:U:V]=[1:u:v]\), set
\[
 \xi=\frac UV=\frac uv,\qquad
 \eta=\frac{U^2}{WV}=\frac{u^2}v.
\]
The first character selects the unique containing quadric
\(Q_\xi=V_{\mathbf P^3}(x_1x_2-\xi x_0x_3)\).
The second selects the cubic scroll
\(R_\eta=V_{\mathbf P^3}(x_0x_2^2-\eta x_1^2x_3)\).
Their intersection cycle is the translated quartic
\(C_{\eta/\xi,\eta/\xi^2}\) plus the two fixed
endpoint ruling lines, as derived in
[the spectral–Jacobian bridge](spectral_jacobian_first_jet_bridge.md#1-set-up-and-the-two-intrinsic-quotient-characters).

In the **projective parameter plane**, the two character fibers
are, respectively, the **lines** \(U-\xi V=0\)
and the **conics** \(U^2-\eta WV=0\).
They meet at the fixed boundary point \([1:0:0]\)
and at exactly one interior point
\[
 [W:U:V]=[\xi^2:\xi\eta:\eta].
\]
Thus the two-dimensional transverse torus may be read as a
marked line/conic incidence. In these coordinates
\[
 \mathcal C_\sigma(X,Y,Z)
 =\Bigl(\prod_i\xi_i^{-2n_i}\Bigr)
   \prod_i(\xi_i^2X+\xi_i\eta_iY+\eta_iZ)^{n_i}
\]
and the ratio in (M) becomes
\[
 \tag{M'}
 \boxed{
 \frac{[YZ^{m-1}]\mathcal C_\sigma}
      {[Z^m]\mathcal C_\sigma}
 =\sum_i n_i\xi_i=M_1(\sigma).}
\]
The conic parameters \(\eta_i\) cancel from this *single*
coefficient ratio; nevertheless the requirement that **the
same two equations** realize the full paired arrangement
necessarily couples both characters. That coupling is
the genuinely unknown step in the all-degree moment theorem.

### The exact equation-side coefficient

Let \(J=(F_a,G_b)\) be a **proper actual homogeneous CI**
with entire fundamental cycle equal to \(\sigma\).
Use the two-parameter line family
\[
 \ell_{y,z}:\quad x_3=x_0,\qquad
       x_0+yx_1+zx_2=0.
\]
Write its binary restrictions as
\[
 \widehat F_{y,z}(r,s)=F(-yr-zs,r,s,-yr-zs),\quad
 \widehat G_{y,z}(r,s)=G(-yr-zs,r,s,-yr-zs).
\]
Let \(\mathscr R_{F,G}(y,z)
=\operatorname{Res}_{[r:s]}(\widehat F_{y,z},\widehat G_{y,z})\),
using any fixed resultant convention. Since
\(\ell_{0,0}=V(x_0,x_3)\) misses every translated quartic,
\(\mathscr R_{F,G}(0,0)\ne0\).
The classical **Chow form/resultant identity** for an
actual proper CI, including generic multiplicities, gives
\[
 \frac{\mathscr R_{F,G}(y,z)}
      {\mathscr R_{F,G}(0,0)}
 =\prod_i
  \left[\prod_{t^4=1/v_i}
    (1+yt+zu_it^3)\right]^{n_i}.
\]
For each translated component the linear coefficients
in \(y,z\) vanish, and its mixed \(yz\) coefficient
is \(-4u_i/v_i\). Therefore
\[
 \tag{R}
 \boxed{
 \frac{[yz]\mathscr R_{F,G}}
      {\mathscr R_{F,G}(0,0)}
 =-4M_1(\sigma)
 =-4\,
   \frac{[YZ^{m-1}]\mathcal C_\sigma}
        {[Z^m]\mathcal C_\sigma}.
 }
\]
Equivalently,
\[
 \boxed{M_1(\sigma)=0
   \iff [YZ^{m-1}]\mathcal C_\sigma=0
   \iff [yz]\mathscr R_{F,G}=0.}
\]
### The Chow coefficient and first-jet residue are the *same* obstruction

For an entire translated-cycle CI, the
[spectral–Jacobian first-jet identity](spectral_jacobian_first_jet_bridge.md#4-the-first-moment-is-a-perfect-residue-pairing-of-first-jets)
states, for
\(F=f_0+x_0p+x_3q+\cdots\),
\(G=g_0+x_0r+x_3s+\cdots\),
\[
 2M_1=\operatorname{Res}_{f_0,g_0}(ps-qr).
\]
Comparing this with (M) and (R) gives the
**three simultaneous exact presentations**
\[
 \tag{Triple}
 \boxed{
  \frac{[YZ^{m-1}]\mathcal C_\sigma}
       {[Z^m]\mathcal C_\sigma}
  =-\frac14
    \frac{[yz]\mathscr R_{F,G}}{\mathscr R_{F,G}(0,0)}
  =\frac12\operatorname{Res}_{f_0,g_0}(ps-qr).
 }
\]
Thus the elementary multisymmetric coefficient,
the mixed second-order polar of the *actual
Sylvester resultant*, and the first-jet
Macaulay/Serre pairing agree on the **whole**
translated-cycle CI incidence, without invariance.
For the unresolved universal moment theorem,
the required identity is **not** any of these
equalities—they are already proved
conditionally on being a translated-cycle CI.
It is the new statement that the three
equal quantities always **vanish**.

The full projective transverse Chow form is
not the Grassmannian Chow form of the degree-\(4m\)
curve. The restriction of the Grassmannian Chow form
to the line family is the actual resultant;
(R) connects their **distinguished coefficients**
through the four-point section of every
translated quartic.

This is an **exact coefficient bridge from the actual two
defining equations to the full two-dimensional Chow
polynomial**, with arbitrary translated residual components
and multiplicities. The final equivalence already follows
from the accepted linear Chow separator in
[chow_arrangement_moments.md](chow_arrangement_moments.md#a-regular-function-on-the-chow-space);
the explicit parameter-plane equation and specialized
binary Sylvester resultant make its algebraic content
particularly transparent. The proof of the underlying
coefficient/resultant dictionary is classical (Chow forms
and elementary multisymmetric functions; cf.
[Vaccarino, 2005](https://www.numdam.org/articles/10.5802/aif.2111/)).
No new universal vanishing is deduced: the assertion
that **every** such actual resultant has \([yz]=0\)
remains open for arbitrary non-invariant nonreduced CIs.
The general Chow factorization and the existence of two
defining equations do not individually prove it.

## 1.2 The complete CI resultant as a product of two-step toric norms

This makes explicit the **entire**, not merely mixed-linear,
resultant of a translated-cycle CI, using exactly the two
independent torus characters
\(\xi=u/v,\ \eta=u^2/v\). It specializes the established
four-point section polynomial in
[chow_realization_moment_separation.md](chow_realization_moment_separation.md#2-the-universal-separator-and-its-exact-target)
and the classical Chow-form/resultant identity,
not a new universal vanishing theorem.

On the hyperplane \(x_3=x_0=1\), a translated
quartic \(C_{u,v}\) meets the plane in the four points
\[
 (X,Y)=(t,ut^3),\qquad t^4=v^{-1}.
\]
The same points, scheme-theoretically, are the
length-four affine CI
\[
 \tag{N1}
 XY=\xi,\qquad Y^2=\eta X^2.
\]
Indeed \(X^4=\xi^2/\eta=1/v\), and then
\(Y=\xi/X=ut^3\).

Its normalized Chow/norm polynomial is
\[
 \begin{aligned}
 P_{u,v}(y,z)
  &=\prod_{t^4=1/v}(1+yt+zut^3)\\
  &=1-\frac{y^4}{v}
    -4\frac uv yz
    +2\frac{u^2}{v^2}y^2z^2
    -\frac{u^4}{v^3}z^4\\
  &=\tag{N2}
    \boxed{1-4\xi yz-\frac{\xi^2}{\eta}
                       (y^2-\eta z^2)^2}\\
  &=\boxed{(1-2\xi yz)^2-
           \frac{\xi^2}{\eta}(y^2+\eta z^2)^2}.
 \end{aligned}
\]
The last formula follows **without expanding**:
pair the four points by the involution
\(t\mapsto-t\). For \(s=t^2\),
\(s^2=\xi^2/\eta\), each pair contributes
\[
 (1+yt+zut^3)(1-yt-zut^3)
 =1-2\xi yz-s(y^2+\eta z^2).
\]
Taking the remaining quadratic norm over
\(s=\pm\sqrt{\xi^2/\eta}\) gives (N2).
Thus the factorization is literally the composition
of two quadratic norms for
\(k(t)/k(t^2)/k(t^4)\). It geometrically remembers
the paired-\(\pm t\) involution as well as both
transverse characters.

If
\([Z]=\sum_i n_i[C_{u_i,v_i}]\)
is the **entire** cycle of a proper actual CI,
the normalized binary Sylvester resultant of
its line-family restrictions satisfies the **full
product identity**
\[
 \tag{N3}
 \boxed{\frac{\mathscr R_{F,G}(y,z)}
              {\mathscr R_{F,G}(0,0)}
      =\prod_i P_{\xi_i,\eta_i}(y,z)^{n_i}.}
\]
The right side allows repeated translated
components and nonreduced scheme structure;
the resultant sees the fundamental cycle,
including its multiplicities.

**First coefficients, with multiplicities.**
Write \(M_j=\sum_i n_i\xi_i^j\). Expanding (N3)
through total degree four gives
\[
 \tag{N4}
 \begin{array}{ll}
 [yz]\widehat{\mathscr R}=-4M_1,
 & [y^2z^2]\widehat{\mathscr R}=8M_1^2-6M_2,\\
 [y^4]\widehat{\mathscr R}
   =-\displaystyle\sum_i n_i\frac{\xi_i^2}{\eta_i},
 & [z^4]\widehat{\mathscr R}
   =-\displaystyle\sum_i n_i\xi_i^2\eta_i.
 \end{array}
\]
Here \(\widehat{\mathscr R}=\mathscr R/\mathscr R(0,0)\).
Moreover \(\widehat{\mathscr R}\in
k[yz,y^4,z^4]\), reflecting its
\(\mu_4\)-invariance on the four-point
sections; no full \(\mathbf G_m\)-invariance
of the defining ideal is presumed.

The two **axis spectra** are
\[
 \tag{N5}
 \widehat{\mathscr R}(y,0)=
 \prod_i(1-\xi_i^2\eta_i^{-1}y^4)^{n_i},
\qquad
 \widehat{\mathscr R}(0,z)=
 \prod_i(1-\xi_i^2\eta_i z^4)^{n_i}.
\]
For each **paired** toric point, the two
axis parameters multiply to \(\xi_i^4\).
The mixed \(yz\) coefficient instead
records the **first power** \(\xi_i\)
and therefore distinguishes the choice
of fourth-root/paired torus coordinate.
The axis spectra alone forget that
pairing. This is a concrete structural
reason the first moment is genuinely a
*mixed* coefficient.

**The individual quartic norm factors form a toric
surface in coefficient space.** Write
\(P_{\xi,\eta}
 =1+A yz+B y^4+C y^2z^2+D z^4\). Then
\[
 A=-4\xi,\quad B=-\xi^2/\eta,\quad
 C=2\xi^2,\quad D=-\xi^2\eta,
\]
and hence
\[
 \tag{N6}\boxed{A^2=8C,\qquad C^2=4BD.}
\]
Conversely, on the locus \(A,B,D\ne0\),
these equations recover
\(\xi=-A/4\), \(\eta=-\xi^2/B\).
Thus actual translated-CI resultants lie
in the **multiplicative Chow image of this
explicit two-dimensional toric surface**
inside the space of line-family resultants.
The universality conjecture is that the
**additional condition of being a resultant
of two actual homogeneous surface equations**
forces the linear coefficient
\([yz]\widehat{\mathscr R}=-4M_1\) to vanish.
The toric factor relations themselves
do not imply it (a single factor with
\(\xi\ne0\) is already a counterexample
to such a bare implication).

### Full two-chart Chow pullback: the cycle determines actual ideal-membership equations

The [focused full-Chow pullback theorem](full_transverse_chow_pullback_envelope.md)
uses the first degree-four weight space with **three**
monomials:
\[
 D_+=x_1^4,\quad P_+=x_0^2x_1x_2,\quad
 R_+=x_0^3x_3.
\]
They simultaneously give the two-dimensional
transverse quotient
\([D_+:P_+:R_+]=[1:u:v]\).
For a cycle \(\sigma=\sum_i n_i[(u_i,v_i)]\),
the \(m+1\) coefficients of the
**actual homogeneous pullback**
\[
 \Phi_\sigma^+(\lambda,\mu;x)
 =\mathcal C_\sigma(\lambda P_++\mu R_+,
                   -\lambda D_+,-\mu D_+)
 =\prod_i[\lambda(P_+-u_iD_+)
           +\mu(R_+-v_iD_+)]^{n_i}
\]
belong to **every proper CI ideal**
whose entire fundamental cycle is \(\sigma\).
On the dense coordinate torus their
coefficient ideal is exactly
\(\cap_i I_{C_i}^{n_i}\) (ordinary powers,
characteristic zero). A coordinate-reversed
weight-twelve quartic triple produces
a second coefficient ideal; their sum
has **set-theoretic support exactly**
\(\cup C_i\), without residual coordinate
lines. This supplies a canonical
*full paired Chow-cycle-to-actual-ideal*
interface—not just the quadric spectrum.

On the ambient dense torus every realizing
CI is a rank-\(m\) finite-flat
**moving quotient** of the constant
fat-point algebra
\(B_\sigma=
 k[u^{\pm1},v^{\pm1}]/\cap\mathfrak m_i^{n_i}\)
of rank
\(N=\sum_i\binom{n_i+1}{2}\).
The exact kernel rank is
\(\delta_\sigma=\sum_i\binom{n_i}{2}\).
This recovers invariance for
**reduced** full cycles (\(\delta=0\));
doubled components introduce one
moving tangent-line choice per support.
The **norm** of the generic linear
form in the moving quotient is
\(\mathcal C_\sigma\), so \(M_1\)
is literally its trace of \(u/v\).
The unproved UM1 step is that
*projective two-endpoint extension*
as a two-surface CI forces this trace
to vanish. The quotient and
coefficient ideal alone do not.

## 2. Coefficients of the full Chow form are mixed symmetric functions

Write
\[
 \mathcal C_\sigma(X,Y,Z)
 =\prod_i(X+u_iY+v_iZ)^{n_i}.
\]
Its coefficients are the elementary **multisymmetric**
functions of the pairs. In characteristic zero define the mixed
power sums
\[
 \mu_{r,s}(\sigma)=\sum_i n_i u_i^r v_i^s,
 \qquad r,s\ge0.
\]
The formal identity
\[
 \log\mathcal C_\sigma(1,Y,Z)=
 \sum_{\substack{r,s\ge0\\r+s>0}}
 \frac{(-1)^{r+s-1}}{r+s}
 {r+s\choose r}\mu_{r,s}Y^rZ^s
\]
expresses **each** \(\mu_{r,s}\) as a polynomial in the
coefficients of the normalized \(\mathcal C_\sigma\) over
\(\mathbf Q\) (and in characteristic zero), via formal logarithm
and coefficient comparison. This is not a claim that all those
power sums freely generate independent coordinates; they satisfy
the usual multisymmetric relations. In small positive
characteristic do not divide by \(r+s\); retain the elementary
multisymmetric coefficients or work directly with evaluation
matrices. The Laurent moment \(M_1=\mu_{1,-1}\) is a regular
function on the **torus** cycle space, and is recovered from
the normalized specialization \(H_\sigma\) rather than this
nonnegative-index expansion.

## 3. Degree/weight evaluation maps and coefficient determinants

First assume **all \(m\) points are distinct**, with cycle
multiplicity one. Set the ambient intrinsic weights
\(\operatorname{wt}(x_0,x_1,x_2,x_3)=(0,1,3,4)\).
For each degree \(d\) and weight \(w\), let
\[
 \Lambda_{d,w}=
 \{(p,q)\in\mathbf Z_{\ge0}^2:
 \ \alpha_1=w-3p-4q\ge0,\
 \alpha_0=d-\alpha_1-p-q\ge0\}.
\]
These index *exactly* the degree-\(d\), weight-\(w\)
ambient monomials: the corresponding monomial is
\(x_0^{\alpha_0}x_1^{\alpha_1}x_2^p x_3^q\),
which restricts to the transverse character \(u^pv^q\)
times the intrinsic torus weight factor.

Put
\[
 E_{d,w}(\sigma)=
 \big(u_i^pv_i^q\big)_{\ 1\le i\le m,\ (p,q)\in\Lambda_{d,w}} .
\]
Then
\[
 \ker E_{d,w}= H^0(\mathbf P^3,I_{|\sigma|}(d))_w,
\]
the exact vector space of weight-\(w\) containing surfaces.
No surface generator is chosen to define it.

**Symmetric moment matrix.** Let
\(\mathcal J_m=\{(r,s)\ge0:r+s\le m-1\}\) and define
\[
 \boxed{\quad
 \mathsf M_{d,w}(\sigma)=
 \bigl(\mu_{r+p,s+q}(\sigma)\bigr)_{
 (r,s)\in\mathcal J_m,\ (p,q)\in\Lambda_{d,w}}.
 \quad}
\]
If \(V_m=(u_i^rv_i^s)_{i,(r,s)\in\mathcal J_m}\), then
\[
 \mathsf M_{d,w}=V_m^{\,t}E_{d,w}.
\]
For \(m\) **distinct** points, the evaluation map from
polynomials of total degree at most \(m-1\) onto \(k^m\)
is surjective: for each point \(p_i\), multiply \(m-1\)
linear forms, each vanishing at one of the other points
but not at \(p_i\). Thus \(V_m\) has full row rank,
\(V_m^t\) is injective, and
\[
 \boxed{\quad
 \ker\mathsf M_{d,w}=\ker E_{d,w};
 \qquad
 \operatorname{rank}\mathsf M_{d,w}
   =\operatorname{rank}E_{d,w}.
 \quad}
\]
This elementary equivalence works in **every characteristic**
when moments are defined directly from distinct points.
The additional assertion that the entries can be recovered
from the \(\mathcal C_\sigma\)-coefficients by the displayed
logarithm is **characteristic zero**.

In particular, existence of a nonzero degree-\(d\),
weight-\(w\) containing eigenform is exactly the vanishing
of the maximal-column-rank minors of \(\mathsf M_{d,w}\).
These are polynomial equations in full Chow coefficients
in characteristic zero. They are symmetric in the \(m\) points
and impose restrictions on the *whole arrangement*.

For degree \(a,b\) with \(ab=4m\), the existing reduced-cycle
theorem states more precisely:
\[
 \sigma\in R_{a,b}^{\rm red}
 \iff
 \begin{cases}
 \text{for one }(w_F,w_G)=(a,3b)\text{ or }(3a,b),\\
 U=\ker E_{a,w_F}\ne0,\quad V=\ker E_{b,w_G}\ne0,\\
 \text{there exist }F\in U,\ G\in V
       \text{ with }\gcd(F,G)=1.
 \end{cases}
\]
Here the kernels are identified with their actual homogeneous
surface spaces. The final properness condition is essential:
the **rank equations alone are not sufficient**. Under this
condition the curves contribute total degree \(4m=ab\),
so Bézout exhausts the intersection, leaving no residual
curve and forcing generic multiplicity one.
The coprime-pair locus is a nonvanishing/constructible
condition on the equation kernels, not a claim that the CI
realization locus is cut out by equations alone.

**Explicit reduced (4,4) test.**
The two required weight spaces yield
\[
 E_{4,4}=
 \begin{pmatrix}
 1&u_1&v_1\\\vdots&\vdots&\vdots\\1&u_4&v_4
 \end{pmatrix},\qquad
 E_{4,12}=
 \begin{pmatrix}
 u_1^4&u_1v_1^2&v_1^3\\
 \vdots&\vdots&\vdots\\
 u_4^4&u_4v_4^2&v_4^3
 \end{pmatrix}.
\]
Both ranks must be at most two. Their \(3\times3\)
minors are direct relations among the transverse points;
the equivalent symmetric moment-matrix minors are
relations among the \(\mathcal C_\sigma\)-coefficients.
The first matrix detects collinearity in \(\mathbf P^2\);
the second expresses a different, nonlinear restriction
on the *same four points*. Actual CI realization additionally
requires suitable independent forms without a common
factor; these qualifications are settled by the cited
reduced-cycle theorem.

## 4. Exact boundary of the conclusion and research question

For repeated components \(n_i>1\), the Chow cycle does not
identify the scheme structure of a possible CI thickening.
Simple evaluation detects **only reduced support**.
Replacing \(\mu_{r,s}\) by \(\sum n_i u_i^r v_i^s\)
does **not** encode length-\(n_i\) transverse local
intersection algebras or a common proper pair. Moreover in
characteristic dividing \(n_i\), weighted traces may lose
support information. Any weighted realization criterion must
control local intersection lengths, possible normal jets,
and the full ideal, not merely the multiplicities in
the symmetric power sum.

The problem to carry forward is:
\[
 \boxed{\text{For }ab=4m,\quad
 \text{which homogeneous symmetric polynomial relations
 in the coefficients of }\mathcal C_\sigma
 \text{ vanish on }R_{a,b}\subset\operatorname{Sym}^mT?}
\]
We seek **degree-uniform** relations analogous to \(M_1=0\),
preferably derived from the joint existence of two
containing surfaces, rather than selecting one carrier
and searching for a mate. The moment matrices provide
an explicit, exact bridge for reduced cycles; eliminating
the unknown equation coefficients inside the kernel
and understanding repeated cycles are the genuine
unsolved extensions. In particular, the unresolved
characteristic-zero all-bidegree moment-vanishing claim
must not be assumed as a premise.

**First bounded next check:** simplify the two (4,4)
moment-matrix determinantal systems symbolically in
the coefficient ring of \(\mathcal C_\sigma\), confirm how
their common vanishing interacts with \(M_1\),
and compare to the existing reduced-cycle criterion.
Do not confuse necessary rank conditions with the
nonvanishing/properness gate, and do not infer an
unrestricted higher-degree obstruction from these
small-degree identities.
