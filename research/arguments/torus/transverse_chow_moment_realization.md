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
