# Ruled normalizations and the conditional sextic lifting problem

## Paired-secant cubic

The finite normalization of the cubic x0*x2^2=x1^2*x3 is F1, with hyperplane class E+2f. On x0=1 its local ring inclusion is k[r,rw,w^2] inside k[r,w]. The upstairs conductor is (r); the downstairs conductor is the reduced double-line ideal (x1,x2). The conductor section maps two-to-one to the line, branched at the endpoints. The strict quartic lift has class 2E+2f, but the full inverse ideal is (w-r^2)(r,w), with an embedded length-one defect at each endpoint. The same F1 is the smooth cubic scroll S(1,2) in P4, projected from the omitted middle coordinate. On the smooth quadric the cubic cuts C0 plus the two limiting tangent trisecants. In characteristic two the conductor cover is inseparable and the scroll is a tangent developable.

Sources: [current proof](ruled_surface_degree_criterion.md#cubic-scroll-normalization) and [current proof](ruled_surface_degree_criterion.md#paired-secant-cubic-normalization-conductor-and-gauss-dual). Independently reviewed geometry, not a new STCI result.

## Projection cone and four-section quartic

The projected cone over C0 has ring k[s^4,s^3t,st^3,t^4], missing the integral element s^2t^2. Its normalization is the complete fourth Veronese cone, with conductor supported at the vertex and an upstairs dual-number quotient. The correct factorization is F4 contracting the negative section to the normal cone, followed by finite normalization of the projected cone. F4 itself is not finite over the projected cone. The related four-section quartic has conductor (x0,x1)^2 downstairs; its transverse ring is k[v^3,v^4,b] inside k[v,b], with conductor v^6. Full inverse ideals can have embedded endpoint corrections of colength six.

Sources: [current proof](ruled_surface_degree_criterion.md#paired-secant-cubic-normalization-conductor-and-gauss-dual) and its independent audit. Elementary transformations and mu4 arithmetic remain in the ruled-geometry family.

## Conditional (6,16) singular-root interface

The October 20 proposal assumes an actual supported (6,16) pair, full generic coprime normal CI (2,12), and an actual saturated movement-two first relation. The (2,2) spectral root Z must satisfy O_Z(1,-1)^12 trivial. A reviewed finite singular-root bridge has transform ideal (p,u^10), providing finite embedded Cartier lifts even for singular Z. Full spectral torsion eliminates cuspidal and tangent-component roots; smooth, nodal, and two-node reducible roots retain their gluing conditions. The next global step is cubic-jet matching for a genuine sextic, [F3-alpha*G0] mod (f)=0, without dividing by alpha at its zeros. Abstract Cartier lifts do not yield global equations or a support certificate.

The October 21 conductor-budget proposal originally depended on an anticanonical contraction hypothesis. The independent continuation audit subsequently VERIFIED that hypothesis in the precise actual-pair setting: a cubic-image model V is a smooth integral threefold with canonical bundle O(-2), and the strict sextic descends to an integral anticanonical surface T. Finite duality and the local monic double-cover normalization then exclude singular-curve contacts at ramified simple base zeros. Combined with the separate nodal analysis, the reviewed result gives a sharp NECESSARY alternative for any actual pair: the multiplier alpha has a multiple base zero, or alpha vanishes at a node of the full root. For a smooth full root the necessary discriminant equation is Disc_8(Ncomp(tau))=0, of degree 28 in the root coefficients. These exceptional strata have not been eliminated; no complete exclusion follows. A different proposed nodal normalization obtained by dividing by a nonunit was rejected as nonfinite. Its suggested integral replacement is not yet certified normal or equipped with an exact conductor.

Sources: [current proof](../spectral/singular_root_actual_pair_bridge.md) and [current proof](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-conductor-ramification). Conditional cross-family work.

## Seven-cubic contraction and five-quadric anticanonical model

The conditional \((2,12;6,16;2)\) actual-pair geometry has a **separate** exact projective construction, not implied by the sextic symbol matrix. Write \(q=x_0x_3-x_1x_2\), \(A=x_0^2x_2-x_1^3\), \(B_0=x_0x_2^2-x_1^2x_3\), \(D_0=x_2^3-x_1x_3^2\). The seven cubics
\[
qx_0,\ qx_1,\ qx_2,\ qx_3,\ A,\ B_0,\ D_0
\]
generate \(I_{C_0}(3)\) and define \(\phi:\operatorname{Bl}_{C_0}\mathbf P^3\to V\subset\mathbf P^6\). In corresponding coordinates \(y_0,\ldots,y_6\), the image \(V\) is cut out **scheme-theoretically** by the five quadrics
\[
\begin{aligned}
&y_0y_5-y_2y_4+y_1^2,\quad y_0y_6-y_2y_5+y_1y_3,\\
&y_1y_5-y_3y_4+y_0y_2,\quad y_1y_6-y_3y_5+y_2^2,\quad
y_4y_6-y_5^2+y_1y_2.
\end{aligned}
\]
The homogeneous ring has free resolution of ranks \((1,5,5,1)\), shifts \((0,2,3,5)\); \(V\) is a smooth integral degree-five threefold with \(\omega_V=\mathcal O_V(-2)\). Projection to \([y_0:y_1:y_2:y_3]\) has base ideal defining the smooth conic \(\Gamma=\{y_0=\cdots=y_3=0,\ y_4y_6-y_5^2=0\}\). Its graph identifies \(\operatorname{Bl}_{C_0}\mathbf P^3=\operatorname{Bl}_\Gamma V\), contracting the strict transform of the unique quadric.

Every sextic in \(H^0(I_{C_0}^2(6))\) is a quadratic expression in these seven cubics and descends to \(T\in|\mathcal O_V(2)|\), with \(\omega_T=\mathcal O_T\). **For an actual supported pair** the low-degree carrier exclusion forces the sextic, its strict transform, and \(T\) to be integral, and the quadric cannot be a component. Finite duality for the normalization \(Y\to T\) identifies \(\omega_Y\) with its full conductor ideal, and the resulting conductor curve \(\Delta\) satisfies \(\omega_\Delta=\mathcal O_\Delta\), even if the conductor is nonreduced or \(Y\) is not Gorenstein. A generically reduced irreducible conductor component of multiplicity one must have arithmetic genus at most one. This global restriction drives the reviewed exclusion of ramified contacts over **simple** zeros of the multiplier \(\alpha\). It does not exclude repeated zeros or nodal root contacts where \(\alpha\) vanishes.

The exact cubic model, graph identification, conductor duality, and simple-zero exclusion received an independent **PASS under the conditional actual-pair hypotheses**. A different nodal example's purported finite normalization by dividing by a nonunit was explicitly **rejected** and is not used. No unconditional \((6,16)\) or STCI exclusion follows. [Cubic image and conductor construction](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-cubic-image-and-conductor-interface); [independent review and rejected nodal claim](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-surface-audit-cont2).

## Exact global sextic-symbol restriction in the conditional (6,16) lane

For the fixed characteristic-zero quartic, the second normal jet map
from \(H^0(I_{C_0}^2(6))\) has a 23-dimensional source, a rank-22 image
in a 33-dimensional target and kernel \(kq^3\). The
[exact map and eleven image equations](../spectral/rank_strata_and_sextic_lifts.md#2-the-exact-global-k-linear-symbol-map)
are computed using the actual global source. On the conditional locus,
testing \(\alpha f\) in that image fixes the sextic up to addition of
\(\eta q^3\). The [actual cubic-jet test](../spectral/rank_strata_and_sextic_lifts.md#7-first-unresolved-global-lift-the-actual-sextic-cubic-jet)
checks this whole affine line.

The [structured incidence](../spectral/rank_strata_and_sextic_lifts.md#6-the-exact-remaining-scheme)
also imposes both ambient obstruction tests and full spectral torsion,
including nodal gluing. The [independent audit](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-incidence-audit)
reviews the exact symbol map and conditional necessity. Realization by a
proper supported pair still requires the
[global equation certificate](../spectral/rank_strata_and_sextic_lifts.md#8-what-a-realization-would-have-to-certify).

## The finite source incidence and its constant-rank cubic obstruction

Let \(S=H^0(I_C^2(6))\), and let \(\rho_2:S\to H^0(\operatorname{Sym}^2N_C^\vee(6))\) be the computed rank-22 map. Write the proposed leading symbol as \(\alpha f\), with \(f=a(z)u^2+b(z)uv+c(z)v^2\). The eleven explicit linear image equations for \(\alpha f\) define the first necessary coefficient incidence, subject to the actual saturated movement-two and nonzero-section conditions. In particular, no division by \(\alpha\) is permitted at its zeros.

For a chosen compatible sextic, the next condition is
\[
(F_c)_3-\alpha G_0=f(\ell u+m v),\qquad\deg\ell,\deg m\le7.
\]
The sixteen correction coefficients map into forty cubic coefficients by multiplication by nonzero \(f\). This map is injective in the polynomial ring and therefore has constant rank sixteen; its image is locally a subbundle and the obstruction is a section of the twenty-four-dimensional quotient. **No rank-drop stratification of this multiplication map is required.** Singular roots and multiplier zeros remain exceptional for the other conditions.

The full necessary incidence also imposes the twenty-five second-obstruction pairings and full-root spectral torsion, including nodal gluing. Its projection to root/multiplier parameters can be constructible rather than closed. The known smooth seed fails the cubic quotient obstruction, but no emptiness or nonemptiness result for the full incidence follows. Even a point satisfying all these conditions does not yet provide a proper degree-sixteen mate or prove sole reduced support.

## Coefficient-level cubic obstruction without elimination

Let \(W_7=k[z]_{\le7}\), and let \(T_9\) denote binary cubics in \(u,v\) whose four coefficients are polynomials in \(z\) of degree at most nine. For \(f=a u^2+buv+cv^2\), with \(a,b,c\in k[z]_{\le2}\), define
\[
\mu_f:W_7^2\longrightarrow T_9,\qquad
(\ell,m)\longmapsto f(\ell u+mv).
\]
Writing a target cubic as \(h=h_0u^3+h_1u^2v+h_2uv^2+h_3v^3\), the exact coefficient equations are
\[
h_0=a\ell,\qquad h_1=b\ell+am,\qquad
h_2=c\ell+bm,\qquad h_3=cm.
\]
These are polynomial equations, including at roots of \(a\), \(c\), or the discriminant \(b^2-4ac\). No coefficient division or choice of a nonvanishing root coefficient is required.

For \(f\ne0\), the map \(\mu_f\) is injective: if \(f(\ell u+mv)=0\) in the integral domain \(k[z,u,v]\), then \(\ell=m=0\). Thus every compatible cubic has a **unique** correction pair, and the cokernel dimension is \(4(10)-2(8)=24\). This is a statement about the fixed-\(f\) linear map, not about twenty-four independent equations on the nonlinear parameter scheme \((f,\alpha,F_c)\). On the nonzero-root open, the matrices \(\mu_f\) form a constant-rank family, so the obstruction is a well-defined cokernel section; its zero scheme may have excess dimension or singular components.

The displayed four polynomial identities are an alternative exact computational representation of the quotient obstruction. They allow direct coefficient comparison without computing 24 moving quotient coordinates. The eleven first-symbol equations, the second-obstruction pairings, and the full-root spectral conditions remain additional constraints. In particular, the constant rank of \(\mu_f\) neither excludes singular quadratic roots nor proves the existence of a proper degree-sixteen mate.

## Varying the sextic lift: the missing \(q^3\) direction

The preceding rank-sixteen calculation fixes a chosen sextic \(F_c\) with the prescribed quadratic normal symbol. But the kernel of the quadratic-symbol map is \(kq^3\), so every sextic with that symbol is \(F_c+\eta q^3\). Since \(q\) vanishes to normal order one, \(q^3\) contributes a generally nonzero cubic jet. Write \(\tau=(q^3)_3\) in the same local cubic-coefficient model. **Existence of some compatible sextic lift** therefore requires
\[
(F_c)_3-\alpha G_0+\eta\tau=f(\ell u+mv)
\]
for a scalar \(\eta\) and \(\deg\ell,\deg m\le7\). The fixed-lift quotient class \(b=[(F_c)_3-\alpha G_0]\) must lie in the line spanned by \([\tau]\) in \(\operatorname{coker}\mu_f\), rather than necessarily vanish there.

Equivalently, the correct varying-lift map is
\[
\widetilde\mu_f:W_7^2\oplus k\longrightarrow T_9,\qquad
(\ell,m,\eta)\longmapsto f(\ell u+mv)-\eta\tau.
\]
It has rank sixteen if \(\tau\in\operatorname{im}\mu_f\), and rank seventeen otherwise. Thus the **varying-lift** obstruction has codimension twenty-four or twenty-three, respectively. The earlier constant-rank assertion applies only to the correction submap \(\mu_f\), not to \(\widetilde\mu_f\). On the generic fiber over \(k(z)\), if \(q_1\) is the nonzero linear normal symbol of \(q\), then \(\tau=q_1^3\); for a quadratic \(f\), the necessary generic condition for \(\tau\in f\cdot k(z)[u,v]_1\) is that \(f\) be proportional to \(q_1^2\). This generic divisibility alone is not sufficient for membership in the bounded polynomial correction space \(W_7^2\).

In the stated bounded coefficient model this question is now settled exactly: the [rank-drop classification](../spectral/rank_strata_and_sextic_lifts.md#5-the-exceptional-root-as-a-degeneracy-locus) proves that the enlarged map has rank sixteen only at the single projective root \([f]=[(u+zv/2)^2]\), and rank seventeen elsewhere. The necessary actual-pair open \(f(-z/2,1)\not\equiv0\) excludes that point. Thus the varying-lift cubic quotient has rank twenty-three throughout that admissible open, and cubic compatibility determines a unique actual sextic. This classifies a linear ambiguity; it does not compute the remaining nonlinear incidence or supply a mate.


The coefficient equations become \(h_i+\eta\tau_i=(a\ell,\ b\ell+am,\ c\ell+bm)_i\), with the fourth coefficient \(cm\). They remain division-free. Any claim that a seed fails the cubic comparison must specify whether the test allowed the \(q^3\) direction; a fixed-lift failure alone does not exclude all sextics with the same quadratic symbol. The independently computed second obstruction is unaffected by this logical distinction, subject to its original hypotheses.

## Existing full-lift exclusion on the free cube-orbit chart

The historical [free cube-orbit global sextic calculation](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-cont2-free-orbit-global-sextic-exclusion) already includes the previously omitted \(\eta q^3\) freedom. It concerns a **restricted chart**, not all quadratic roots: the multiplier is the canonical cube norm of the quadric-line restriction, both endpoint coefficients are nonzero, and no two roots lie in the same primitive-cube orbit. The application to actual supported pairs additionally depends on the separate quadric-cycle norm necessity bridge.

After the first ambient equations and the chart normalization, its candidate scheme is
\[
h_6=h_5=d_3=d_1=0,\quad h_4=-2h_7,\quad
t=\tfrac{27}{4}h_7^3+\tfrac{15}{32}h_7,\quad
d_2=108h_7^3-\tfrac92h_7,\quad
p(h_7)=648h_7^4+45h_7^2-4=0.
\]
The source computation retains the free sextic coefficient \(\eta\). Two of its full cubic equations specialize to
\[
E_4=\tfrac34\eta+\tfrac{369}{16}h-\tfrac{891}{2}h^3,\qquad
E_8=\tfrac18\eta+\tfrac{27}{32}h-\tfrac{81}{4}h^3.
\]
Their difference \(E_4-6E_8=18h-324h^3\) eliminates \(\eta\), and the exact polynomial certificate is
\[
1=\frac{162h^2-1}{4}p(h)
 +\left(81h^3+\frac{77}{8}h\right)(E_4-6E_8).
\]
Thus the **entire stated free-orbit chart is empty**, even allowing the sextic lift to vary by \(q^3\). The historical note records independent rational-arithmetic verification. This is a stronger scoped exclusion than a single failed seed, but it does **not** decide the endpoint strata, orbit collisions, or unrestricted movement-two incidence. The retained collision-boundary computation uses multiplication by \(\alpha\) in \(k[z]/(D)\) and cannot be replaced by cancellation of \(\alpha\).

The general warning about testing only one lift remains essential. For the saved smooth seed, however, the exact coefficient row also annihilates the q³ direction, as shown below; its −384 pairing therefore already excludes all lifts. Independently, the full-lift unit certificate resolves the separate free-orbit subfamily. Neither calculation exhausts the uncovered strata.

## Two-node root strata: exact exclusions and retained pencils

The historical [forced-norm two-node continuation](https://github.com/markluxton1/STCI/blob/6e5fecb713e5a5c7aa79010b4338bd4e08e9ec54/research/supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-singular-continuation2) gives more than an unclassified singular-root boundary. Under its stated actual-pair, saturated movement-two, forced-norm and two-node hypotheses, it computes the nonzero cubic-defect locus. The generic component decomposes into a line and a conic. The **entire generic line component** is excluded by exact first-incidence plus spectral-torsion unit calculations for \(w=1\) and the primitive cube-root branches. The nonzero-defect \(B=0\) and \(C=0\) boundaries are also excluded, the latter by the actual involution \(x_0\leftrightarrow x_3,\ x_1\leftrightarrow x_2\). These are scoped coefficient-scheme exclusions, not an unrestricted characteristic-zero theorem.

The surviving nonzero-defect locus from that calculation is the generic conic
\[
B_1=B_2=C_1=1,\quad C_2=w,\quad w^3=1,\qquad
2(x^2+xy+y^2)+3=0,
\]
with the explicit nonvanishing conditions and remaining coefficient relations in the historical note. The bounded conic computation was interrupted; **it supplies neither emptiness nor a surviving point**.

The other retained stratum has both cubic defects zero, \(\kappa_1=\kappa_2=0\). Its exact global sextic family is
\[
F_6=H_1H_2+\eta q^3,
\]
where the global cubics \(H_i\) have the prescribed first symbols. For an actual sole-support pair, \(\eta\ne0\): otherwise \(F_6\) factors into cubic carriers, contradicting the characteristic-zero lower-degree exclusion after factor reduction. The pencil is a necessary source description, **not** a construction of a supported pair.

The two-node continuation identifies the complete twenty-five second pairings, spectral torsion, and actual cubic-jet matching as the next tests for these retained strata. Its original note records the independent-review status and exact computational artifacts; this synthesis does not extend unreviewed component calculations beyond their stated scope.

## Actual quadric-cycle norm bridge

Let \(k\) be algebraically closed of characteristic zero and fix
\(C_0=[s^4:s^3t:st^3:t^4]\subset\mathbf P^3\). Suppose an actual proper
pair \((F_6,G_{16})\) has sole reduced support \(C_0\), full generic
ordinary initial ideal a coprime binary complete intersection of degrees
\((2,12)\), and an actual saturated movement-two first relation.
[R-0010](../../results/saturated_first_relation_normal_flatness.md) supplies
the coprime fiberwise initial algebra. By
[R-0011](../../results/moving_nonreduced_spectral_root_obstruction.md) and
component degrees in the spectral descent condition, the full root \(Z\)
is reduced of class \((2,2)\), integral or a union of two distinct
\((1,1)\) curves. On \(B=\operatorname{Bl}_{C_0}\mathbf P^3\) with
exceptional divisor \(E\), the [finite singular-root bridge](../spectral/singular_root_actual_pair_bridge.md#2-finite-bridge-without-smoothness-of-the-root)
gives the actual common order-two transform ideal \((p,t^{10})\) at
every full-root point. The original degree-two symbols are \(\alpha f\)
and \(\beta f\) with nonzero multipliers that jointly generate the
relation line everywhere, and \(\alpha\) has degree eight.

Let \(Q=(q=0)\) for \(q=x_0x_3-x_1x_2\). On this smooth quadric
\(C_0\) has class \((1,3)\) with first ruling map \(\pi_3:z\mapsto z^3\).
The quadric direction section of \(E\) has class \((1,1)\) and equation
\(q_1=u+zv/2=0\) in the balanced frame. For
\(f=a(z)u^2+b(z)uv+c(z)v^2\), let \(\tau=f(-z/2,1)\), the homogeneous
quartic cutting out the contact of \(Z\) with that section. Under the
stated hypotheses, \(\tau\ne0\) and the sextic multiplier is the
complementary norm of \(\tau\) up to scale, with its full divisor
\(\pi_3^*\pi_{3*}\operatorname{div}(\tau)-\operatorname{div}(\tau)\).

### The quadric direction is not a root component

An actual supported pair cannot have `Q` as a component of `F6`.
Otherwise `G16|Q` is a nonzero effective Cartier divisor with sole
reduced support `C0`: `G` cannot contain `Q`, since the global pair
has no common hypersurface factor. Such a divisor would be `m*C0`,
whereas its class is `(16,16)` and `C0` has class `(1,3)`. No
integer `m` gives these two classes.

Consequently `tau` is not identically zero. Indeed if `tau=0`,
then the restriction `F6|Q` has order at least three on `C0`.
The remainder would have class

    (6,6)-3(1,3)=(3,-3),

which is not effective on the smooth quadric. Hence `F6|Q` would
vanish identically, forcing the already excluded quadric factor.

Thus an actual global pair satisfies the additional open condition

    q1 does not divide f,             tau != 0.

This removes a permitted reduced two-component spectral stratum.
Whether an earlier global lifting test already removes it is a
separate implication, not assumed here.

### Residual quadric divisors and the exact contact scheme

The restrictions are

    div(F6|Q)=2C0+R,      R of class (4,0),
    div(G16|Q)=2C0+T,     T of class (14,10).

Both multiplicities along `C0` are exactly two, since their generic
symbols restrict to nonzero multiples of `tau`. The residual
divisor `R` is a sum of ruling fibers, with their actual positive
multiplicities. The divisors `R,T` have no common component and no
common point outside `C0`, by sole reduced support of the original
pair. In particular

    R.T=40.

The strict transform `Q'` is isomorphic to `Q`: blowing up a
Cartier divisor `C0` on the smooth quadric does not change that
surface. Under this isomorphism, `E|Q'=C0`, and restriction of the
common order-two transforms gives precisely the divisors `R,T`.

At a point of the full root meeting the quadric direction section,
restrict the actual transformed ideal `(p,t^10)` to `Q'`. Since
`tau` is nonzero, `(p,t)` on the smooth surface `Q'` has finite
colength, equal to the root/quadric-direction intersection
multiplicity `nu` there. The regular-sequence filtration gives

    length O_(Q',x)/(p,t^10)
      =10*length O_(Q',x)/(p,t)=10*nu.                    (1)

This does not require `p=0` to be smooth. Away from the full root,
the transformed ideal is the unit ideal near `E`, so there are no
other residual intersection points on `C0`.

Summing (1) gives exactly

    R.T=10*(Z . Q_direction)=10*4=40.                    (2)

Thus the elementary quadric degree budget saturates; it gives no
numerical contradiction. It also identifies all contacts and their
scheme lengths rather than treating a vertical exceptional curve
as a residual component downstairs.

### The forced norm, with collision and ramification multiplicities

The local formula implies more than the total equality (2). Each zero
of `tau` gives a contact point of `R,T`, so its ruling fiber belongs to
`R`. Write `R=sum m_y L_y` as a divisor of ruling fibers. Since
`T.L_y=10` and `T` has no component `L_y` for `m_y>0`, restriction to
each such fiber gives

    10*m_y
       =sum_(x in C0 intersect L_y) i_x(R,T)
       =10*sum_(x in pi3^-1(y)) ord_x(tau).

Identifying a sum of ruling fibers with its divisor on the ruling base,
the actual divisors satisfy

    R=pi3_* div(tau).                                    (3)

On the affine quadric chart the equation of `C0` is `v=b-z^3`,
and `F6|Q=v^2 R4(b)`. Comparing its second symbol with `alpha*f`
gives `alpha(z)*tau(z)=R4(z^3)`. Together with (3), this yields

    div(alpha)=pi3^* pi3_* div(tau)-div(tau).              (4)

Thus the actual degree-eight multiplier is uniquely determined
projectively by `tau`, including branch points and repeated roots.
If `zeta` is a primitive cube root of unity, an explicit formula is

    alpha(z) proportional to tau(zeta*z)*tau(zeta^2*z).    (5)

Formula (5) is a polynomial construction; there is no division by
`alpha` or by a function vanishing on `C0`. If
`tau=sum_(j=0)^4 t_j z^j`, the coefficient of `z^m` in the right
side is

    sum_(2j=m) t_j^2
      +sum_(j<k, j+k=m) e_(j,k)*t_j*t_k,

where `e_(j,k)=2` if `j=k mod 3`, and `e_(j,k)=-1` otherwise.
So the same map is defined over QQ without adjoining `zeta`.
In homogeneous coordinates the product is `tau(s,zeta*t)*tau(s,zeta^2*t)`.
It is a nonzero section for every nonzero `tau`.

Explicitly the coefficient vector is

    A0=t0^2,
    A1=-t0*t1,
    A2=t1^2-t0*t2,
    A3=2*t0*t3-t1*t2,
    A4=t2^2-t0*t4-t1*t3,
    A5=2*t1*t4-t2*t3,
    A6=t3^2-t2*t4,
    A7=-t3*t4,
    A8=t4^2,

where

    t0=c0,
    t1=c1-b0/2,
    t2=c2-b1/2+a0/4,
    t3=-b2/2+a1/4,
    t4=a2/4.

One may impose `alpha_i*A_j-alpha_j*A_i=0` for all `i<j`, with
`alpha!=0` and `tau!=0`, or eliminate the projective multiplier by
substituting `[alpha_0:...:alpha_8]=[A0:...:A8]`. The latter makes
the eleven global-symbol equations homogeneous cubics in the nine
coefficients of `f`; it does not alter the actual root coordinates
or erase any norm ramification stratum.

All ramification multiplicities are retained in this argument.
At zero or infinity the map `pi3` has ramification index three:
if `tau` has order `m` there, its norm divisor has order `m`, its
pulled-back norm has order `3m`, and (4) gives order `2m` for
`alpha`. In an unramified orbit, with orders `m_0,m_1,m_2` for
`tau`, (4) gives orders `m_1+m_2,m_2+m_0,m_0+m_1` for `alpha`.
Thus repeated roots, collisions within an orbit and the two branch
fibers are covered without a genericity exception.

This supplies an exact additional necessary global-pair condition
on the low-order scheme: impose the projective equality in (5),
or substitute its quadratic coefficient vector for `alpha`, on
the open `tau!=0`. When the four roots of `tau` lie in distinct
unramified `pi3` fibers, the sextic symbol restriction on Q already
forces this multiplier. On collision and branch strata that
restriction can leave other choices; (3)-(5) retain the one forced
by the ACTUAL supported pair and its gap-ten contact ideal. No
claim that this condition is new on every component of the earlier
incidence is made.

As a consistency check, at the saved smooth seed

    tau=z^4/4+2z^2-8,

the coefficient vector in (5), multiplied by 16, is

    z^8-8z^6+96z^4+256z^2+1024,

the previously computed projective multiplier. This algebraic
identity does not make that already obstructed seed a survivor.

### Independent review of the norm argument

The separate `surface_bound` reviewer reported PASS for sections 1–4
of the October 20 `incidence_audit` argument. The reconstruction checked
restriction of the actual transformed ideal to \(Q'\), regularity from
\(\tau\ne0\), the absence of a ruling component in \(T\) shared with
\(R\), the affine comparison `F6|Q=v^2 R4(b)`, and the homogeneous and
rational coefficient formulas with collisions and ramification. This
review concerns the necessary norm condition. It also supplied the unit
observation used in the separate local surface calculation below.
[Original argument and scoped review](https://github.com/markluxton1/STCI/blob/a779730c6645e293cc0a501597bd4e09a50b36d6/research/supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#6-independent-review-of-the-norm-argument).

## Local surface singularities and the remaining scope

For \(H\) the pullback of a hyperplane, the strict sextic has class
\(D=6H-2E\). A smooth member has \(c_2=28\), \(K^2=-4\) and
\(\chi(\mathcal O_D)=2\) by Noether’s formula. Near a smooth root point
where \(\alpha|_Z\) has a simple zero, the strict sextic has equation
\(Ap+t^{10}B\) with \(A|_Z=\alpha|_Z\) in local frames. Here \(B\) is a
unit. The other multiplier \(\beta\) is a unit there, so the invertible
change from the actual generators to \((p,t^{10})\) forces the
off-diagonal coefficient \(B\) to be a unit. The simple zero makes
\((A,p,t)\) a system of parameters and the germ is of type \(A_9\).
The divisor \(\operatorname{div}_Z(\alpha)\) has length sixteen.

For a zero of multiplicity \(m\ge1\), the special model
\((t+z^m)p+t^{10}\) has type \(A_{10m-1}\). Setting \(x=t+z^m\) and
absorbing the multiple of \(x\) in \(t^{10}-z^{10m}\) into \(p\) gives
\(xp'+z^{10m}\). This example alone gives no classification of
multiple-zero germs. A global exclusion also needs a vanishing-cycle
bound and control of singular roots and nonnormal strict surfaces,
including singular curves and exceptional fibers. The reviewed
[normal-surface and reduced-divisor argument](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus)
and [nonnormal local models](../spectral/rank_strata_and_sextic_lifts.md#nonnormal-conductor-budget-and-local-escape-models)
address these questions in their stated scopes.

## Geometric exceptional locus for actual pairs

The October 21 independently reviewed geometric argument gives a necessary condition beyond the sextic symbol incidence. Under actual sole support and the saturated movement-two hypotheses, the full-root multiplier divisor cannot be reduced. For a normal strict sextic, local singularities force total Milnor number at least 144, whereas the global resolution argument bounds it by 50. The nodal extension uses the ample strict mate to eliminate nonnormal singular curves when the divisor is reduced. Hence candidates must lie on the explicit degree-52 discriminant-resultant exceptional locus
\[
\operatorname{Disc}_8(N_{\rm comp}(\tau))\,\operatorname{Res}_{8,4}(N_{\rm comp}(\tau),\Delta)=0,\qquad\Delta=b^2-4ac.
\]
The degrees in the original root coefficients are 28 and 24. The earlier degree-64 condition also included `Disc_4(Delta)`; the reviewed nodal extension removes that factor, since singular roots with a reduced multiplier divisor have already been excluded. Every homogeneous infinity root remains included. Whether the exceptional locus contains an actual pair remains open. [Proof and dependencies](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus).

## Singular curves on the strict sextic: two conditional alternatives

The reviewed geometric continuation further classifies a singular curve \(\Sigma\) on the strict sextic, provided that the sextic is normal near the multiplier-zero points of the full root. Let \(n\le2\) count its transverse contacts with ordinary root nodes, \(d=H\cdot\Sigma>0\), and \(e=E\cdot\Sigma\). Multiple multiplier fibers can contribute additional contacts with \(E\), so **one must not set \(e=n\)**. The strict mate gives the exact degree identity
\[
16d-2e=10n.
\]
If \(\Sigma\) is not contained in the strict quadric \(Q'\sim2H-E\), effectivity gives \(e\le2d\), whence \(12d\le10n\le20\). For \(d\ge2\) this is impossible; \(d=1\) forces \(n=2\), then \(e=-2\), also impossible. Thus \(\Sigma\subset Q'\).

The intersection of the strict sextic with \(Q'\) has ruling class \((4,0)\). Consequently \(\Sigma\) must be a trisecant ruling line, with \(d=1\), \(e=3\), \(n=1\), meeting the full root at one ordinary node in the quadric direction. Its multiplicity in the sextic-quadric intersection is at least two. The forced norm then requires additional multiplier multiplicities along its ruling orbit. The line is not an endpoint branch fiber.

Accordingly, a remaining actual pair under these hypotheses must exhibit **either** nonnormality at a multiplier-zero root point **or** this precise singular trisecant ruling line. This is a conditional classification, not an exclusion. See the [reviewed source](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus), section 7.

## Exact failed seed: the row also kills the free lift

The smooth torsion-two root \(f_0=(z^2+4)u^2+(z^2-8)v^2\) has a unique projective multiplier \(\alpha_0=z^8-8z^6+96z^4+256z^2+1024\) satisfying all eleven quadratic-symbol image equations. Its compatible first cubic correction is
\[
G_0=(z/8)u^2v-(3/4)uv^2+(z/8)v^3.
\]
Use target coordinates \(P_0,\ldots,P_{10},Q_0,\ldots,Q_{10},R_0,\ldots,R_{10}\), followed by \(T_{i,j}\), the coefficient of \(z^ju^{3-i}v^i\). The source's exact annihilating row is
\[
\begin{aligned}
&P_4+64P_8-192P_{10}+Q_5-16Q_7\\
&+3T_{0,0}-12T_{0,2}+48T_{0,4}-192T_{0,6}+768T_{0,8}\\
&-2T_{1,1}+8T_{1,3}-32T_{1,5}+128T_{1,7}-512T_{1,9}.
\end{aligned}
\]
It annihilates all 23 actual global sextic source columns and all sixteen correction columns, whereas its pairing with \((\alpha_0f_0,\alpha_0G_0)\) is −384. In particular, the free cubic direction is
\[
\tau=(u+zv/2)^3,
\]
and its row pairing is \(3-2(3/2)=0\). Thus the exact certificate excludes **every** global sextic lift for this fixed seed, including arbitrary additions of q³. It is not merely a test of one chosen lift. The independent consolidation review checked the saved exact source matrices as well as this coefficient calculation.

The source system has 39 unknowns (23 actual sextic coefficients and sixteen correction coefficients), coefficient rank 39 and augmented rank 40. The full source matrices identify the coefficient conventions. The seed also fails the separately accepted second obstruction. Singular roots, all twenty-five second-obstruction pairings, spectral gluing, and the global mate problem remain for the full parameter incidence. [Exact inputs and replay](../spectral/rank_strata_and_sextic_lifts.md#9-reproduction-and-verification-limits), [independent linear-algebra review](../spectral/rank_strata_and_sextic_lifts.md#2-independent-linear-algebra-reconstruction).

## What the conditional (6,16) computation actually tests

This lane is a controlled illustration of the distinction between a root scheme, an ambient symbol, and an actual supported pair. Its quadratic normal root and movement-two relation impose a spectral condition on the full root, but the degree-six symbol must also lie in the **rank-22 image** of the global map from the 23-dimensional space of sextics vanishing twice along C. Its one-dimensional kernel is generated by \(q^3\); the eleven independent linear constraints on the 33 symbol coefficients are therefore genuine global-source conditions, not optional genericity assumptions.

The cubic-image and conductor calculation adds a further restriction **conditional on an actual supported pair**: the multiplier has a multiple base zero or vanishes at a node of the full root. The smooth-root discriminant condition and the remaining exceptional strata are necessary tests, not a proof that a proper pair exists or that every (6,16) pair is excluded. In particular, the rejected nonfinite nodal normalization cannot be used to close the nodal stratum.

These conditions sit at different logical levels: (i) root and formal normal algebra; (ii) actual global sextic source; (iii) conductor geometry for a supported pair; and (iv) the still-unresolved exceptional locus. Their conjunction is a candidate-family test, not a universal implication between the global determinant, residual-jet and conductor-descent routes. See [Chapter 3](../../frameworks/formal-normal-geometry/from_symbols_to_equations.md#311-embedded-one-step-lifting-and-the-actual-homogeneous-source) and [proved arrows and proposed bridges](../../frameworks/spectral-roots/index.md#bridges).

## Why the conditional sextic conductor does not solve descent

The seven-cubic contraction supplies an exact anticanonical surface model **assuming an actual supported pair**. Its duality calculation constrains the conductor of that model, and the simple-zero argument eliminates a specified ramification stratum. This is logically different from the full-conductor descent test for an independently chosen normalization and a proposed mate: in the sextic argument the pair is an antecedent, whereas in the projection program its existence is the conclusion sought.

The eleven linear equations defining the global sextic-symbol image likewise impose necessary realization conditions without selecting a proper degree-sixteen mate. The remaining multiple-base-zero and nodal-contact loci therefore require direct treatment; neither the cubic-image duality nor the symbol rank closes them. For the general descent framework and the role of nilpotent conductor phases, see [Chapter 4](../../frameworks/carrier-normalization/carrier_descent.md#42-the-full-conductor-descent-criterion) and [the projection phase synthesis](conductor_descent_algebra.md).

## Remaining boundaries

No arbitrary projection classification, full conductor phase image, higher-index exclusion, global spectral realization, or unrestricted characteristic-zero STCI theorem follows. The broader source branches are integrated by subject elsewhere; the restrictions here remain conditional and do not claim that every carrier falls in this lane.


Source for the stronger reviewed result: [the actual-pair cubic-model and conductor argument](https://github.com/markluxton1/STCI/blob/20b05fb7ee16f14e4e371c7e0dce7256ba11b480/research/supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-surface-audit-cont2), sections 2–6. Its independent review reports PASS for the cubic-model interface, full conductor duality, and ramified simple-base-zero exclusion, while expressly rejecting the defective nodal normalization. The finite singular-root bridge remains reviewed.


### Geometric scope of movement two

The canonical reduction STCI-R-0014 identifies movement epsilon with the degree of the coefficient map from C to the projective space of binary degree-r forms. Its first normal-root divisor has bidegree (epsilon,r) on P1_base x P1_direction. In the conditional (6,16) setting, r=2 and epsilon=2, so the full first root is a divisor of bidegree (2,2). Saturation means the coefficient map has no base points; it does not exclude root collisions or ensure coprimality of specialized initial forms. Generic binary-CI coprimality and saturation are separate assumptions. The six numerical rows, including (r,s;a,b)=(2,12;6,16), are necessary candidates only under the complete hypotheses of STCI-R-0013 and STCI-R-0014; they are not a classification of arbitrary STCI presentations.

Source: research/results/movement_two_six_rows.md (STCI-R-0014), geometric clarification in commit ccc9c3965e1645ed2569405e0194e31edb38e9d0.

## The common lifting mechanism

For the exact linear-algebra statement separating a fixed symbol from its affine lift fiber, see [global lifting interfaces](../equations/global_lifting_interfaces.md). Here the symbol map has domain dimension 23, image rank 22, and kernel kq³. The cubic correction map μ_f has constant rank 16 for f≠0. Its actual obstruction is therefore the cubic target modulo `im μ_f + k(q³)_3`, of dimension 23 on the actual-pair-admissible open, with the single rank-drop root classified in [varying actual-source lifts](../spectral/rank_strata_and_sextic_lifts.md). This calculation measures the obstruction to meeting the chosen cubic correction space with an **actual global sextic fiber**; it is not a dimension count proving the nonlinear incidence empty. Higher ambient classes, spectral gluing, a proper degree-sixteen mate, and sole support remain separate.

## Endpoint-four: the finite actual-equation question

On the retained integral nodal endpoint-four chart, normalize a0=1 using the actual ambient torus and its square-root cover as proved in [endpoint-four actual sextics](endpoint_four_actual_sextics.md#endpoint-four-sextic-constructions). The root coefficients become
\[
a=1+2b_2z+z^2,\quad b=(\rho+1)z/2+b_2z^2,\quad c=\rho z^2/4,\qquad \rho^{12}=1,\quad\rho\ne1.
\]
Every target second symbol z^8f has the actual sextic family displayed in that proof, with the full free q³ coefficient. For each nontrivial twelfth root, over its exact cyclotomic field and retaining the nodal and finite-ruling opens, the remaining question is whether some actual global degree-sixteen form has remainder after division by F6 vanishing through normal degree eleven, with a coprime degree-twelve term.

The coefficients of that mate remain global constants. The actual first-relation multiplier must be nonzero at the endpoint where z^8 vanishes, and the two multipliers must generate the saturated relation line everywhere. These are open and generation conditions on the finite incidence, not consequences of its low-order equations. Both node branches and their gluing modulus rho must be kept. Assuming a regular formal surface would fall into the already excluded scope of R-0018 and would remove the intended singular problem.

The fixed-carrier certificate for the selected rho=−1, b2=0, q³-coefficient=1 excludes only that particular member. The whole endpoint-four family, the distinct tau=z³(1+z) endpoint chart, and nonzero-endpoint orbit collisions remain open. A completed unit ideal or exact obstruction for one retained open would close that chart alone.

## Characteristic range of this conditional lane

The retained lane, its six-row reduction and spectral gluing inputs are characteristic-zero statements. Some proof components are algebraic in wider ranges, but they do not transfer that full hypothesis package. The regular-sequence formula `length A/(p,t^10)=10 length A/(p,t)` and the injectivity of multiplication by nonzero f are characteristic independent when their stated rings, parameters and nonzero conditions exist. The displayed balanced coordinates and source matrices use denominators, notably2; reduction modulo a prime also requires the asserted ranks and kernel to survive. The free cube-orbit treatment uses a separable cubic ruling action and primitive cube roots, so its stated chart is not transported to characteristic3.

The nonzero rational seed pairing −384 is an obstruction over Q; it gives no such contradiction after reduction at primes dividing that value, and any other-prime application must still verify the actual source and inherited hypotheses. The global Milnor/Hodge surface bound is separately characteristic zero. No positive-characteristic exclusion follows by reducing that numerical argument or the degree52 equation. This is compatible with the [actual quartic-carrier construction in every positive characteristic](../arithmetic/positive_characteristic_constructions.md#every-positive-characteristic-quartic-carrier) for the fixed embedding.


## Consolidated historical source: `research/supplements/STRUCTURAL_CONTINUATION_AND_INDEPENDENT_INVESTIGATIONS.md`

# Actual source incidence and monic differential reductions

Complete mathematical dossier preserving the actual investigations, calculations, exact conditions, negative results, and unresolved boundaries. Administrative commentary is retained pending editorial consolidation, not treated as proof authority.

---

<a id="2026-10-19-independent-investigation-report"></a>

## Independent investigation: saturated normal cones, moving roots, and exceptional cycles

Date: 2026-10-19. Starting branch: `main`.
Research branch: `codex/normal-cone-rigidity-2026-10-19`.

**Status:** research with separate independent audits. The unrestricted characteristic-zero STCI problem
for `C0=[s^4:s^3t:st^3:t^4]` remains open.

### A. Main findings

#### A1. A global normal-flatness theorem for actual lci thickenings

Let `C` be a smooth connected projective curve in a smooth threefold,
`Y` an actual lci thickening with `Y_red=C`, `J=I_C O_Y`, and
`E=N_(C/X)^*`. Suppose:

1. The **full generic ordinary initial ideal** is a coprime binary
   complete intersection `(f_r,g_s)`, with `2<=r<s`.
2. The actual first relation
   `R=ker(Sym^r E -> J^r/J^(r+1))` is a line **subbundle**.

Then every ordinary normal layer `J^i/J^(i+1)` is locally free on `C`,
and every graded fiber is a binary complete intersection of degrees
`(r,s)`. No balanced-conormal assumption, smooth-root assumption, or
joint generation by two chosen displayed symbols is needed. The
characteristic-zero formulation suffices for this investigation.

The proof uses the saturated ordinary powers `P_i`, whose successive
layers `B_i` have perfect complementary multiplication pairings into
the actual socle line `S`. With `d=r+s-2`, generic Gorenstein symmetry
gives `Ann(P_i)=P_(d+1-i)`; exact MCM duality then gives
`B_(d-i)=Hom(B_i,S)`. Saturation of the first relation forces
`P_i=J^i` through `i=s`.

Write `h=deg E`, `a=deg R`. Duality fixes

    deg S=(s-1)h-(s-r)a/r.

The kernel `T` of the degree-s first-relation quotient onto `B_s` is a
line subbundle and has

    deg T=s h-s a/r.

The relative resultant of the first form and this second **quotient**
relation is a generically nonzero section of

    (det E)^(rs) tensor R^(-s) tensor T^(-r).

Its degree is zero. Projectivity forces it to be nowhere zero, hence
the relations are coprime in every fiber. Their abstract graded CI
maps to the saturated graded algebra. The top map is an isomorphism
between equal-degree lines, and perfect graded pairings make every
graded map an isomorphism. Degree-one generation finally gives
`P_i=J^i` for all `i`. This removes the possible later ordinary-layer
torsion rather than assuming it away.

Source: [general theorem and proof, Section 8](../spectral/spectral_pushforward_powers.md#projective-normal-flatness-by-duality-and-resultants).
The same note proves the balanced full-root spectral bridge and retains
the nonsplit second-generator extension.
Independent reconstruction: [filtered bridge audit](../spectral/spectral_pushforward_powers.md#2026-10-19-filtered-saturated-duality-moving-purepower-independent-audit).
Additional adversarial review: [normal-flatness audit](../normal-geometry/normal_flatness_and_filtered_ci.md#2026-10-19-normal-flatness-adversarial-audit).

A separate local proof uses the accepted sharp codimension-two
Artinian Gorenstein Hilbert-function bound. Length `rs`, Loewy degree
at most `r+s-2`, and exact transverse first order `r` force the entire
special Hilbert function to equal the CI envelope. A DVR argument then
makes every ordinary layer flat. This second proof removes projectivity
and also treats `r=s` under its explicit constant-exact-order hypothesis;
the saturated first kernel is a sufficient condition of the appropriate
rank. Its [source](../normal-geometry/normal_flatness_and_filtered_ci.md#2026-10-19-filtered-generic-ci-normal-flatness) and
[separate audit](../normal-geometry/normal_flatness_and_filtered_ci.md#2026-10-19-filtered-local-normal-flatness-independent-audit)
record the additional classical dependency. It supplies independent
support for A1 rather than a finite check of the resultant proof.

#### A2. Moving nonreduced full roots are excluded in that actual class

Over characteristic zero, let `Z subset P1_base x P1_direction` be a
finite-flat Cartier root divisor of class `(epsilon,r)`, `epsilon>0`.
If `O_Z(0,s)=pi*O(n)` for any `s>0`, then `Z` is reduced. Moreover, if
`g=gcd(epsilon,r)`, its irreducible components have classes

    t_i(epsilon/g,r/g),  t_i positive integers,  sum t_i=g.

In particular, coprime `epsilon,r` force an integral root.

The auxiliary theorem is that

    Pic(P1 x P1) -> Pic(2D)

is injective for every effective divisor `D` with both bidegrees
positive. A trivialization on `2D` makes logarithmic transition
differentials vanish in `Omega_surface|D`; the vanishing
`H1(Omega_surface(-D))=0` then detects both ambient Chern-class
coordinates. A repeated component of a moving spectral root would
contain just such a doubled divisor and contradict injectivity.
Singular and reducible divisors are retained throughout.

Combining A1 with [STCI-R-0008](../../results/spectral_root_picard_criterion.md)
and this Picard argument yields a direct exclusion of actual
`C0`-supported lci thickenings whose first full root is moving and
nonreduced, **provided the full generic CI and saturated-first-line
hypotheses hold**. This includes repeated irreducible multisections
and mixtures of components, beyond powers of one moving section.

For movement two, a spectral survivor must be an integral reduced
`(2,r)` divisor, possibly singular, or (for even `r`) a union of two
distinct smooth rational `(1,r/2)` divisors. Ramified nonreduced
**fibers** of a reduced total root remain allowed.

Source: [nonreduced-root proof](../spectral/spectral_torsion_and_syzygy_splitting.md#2026-10-19-spectral-nonreduced-root-obstruction).
Independent reconstruction: [spectral audit](../spectral/spectral_torsion_and_syzygy_splitting.md#2026-10-19-spectral-nonreduced-root-independent-audit).
A shorter general-base argument for moving pure powers is preserved
in [the pure-power note](../spectral/spectral_pushforward_powers.md#2026-10-19-filtered-saturated-duality-moving-purepower-bridge).

#### A3. Exact exceptional-cycle balance and new support restrictions

In the broader proper-intersection setting for `C0`, write

    [V(F,G)]=m[C0]+R_res,  delta=deg R_res=de-4m.

Let `p,q` be the exact generic normal orders of the displayed equations.
On the first blowup write the strict-surface intersection cycle as
`R_res~+Y_exc`, and put `lambda=E_exceptional . R_res~`. If
`[Y_exc]=A alpha+B beta` on `P1_base x P1_direction`, then

    B=m-pq,
    A=lambda+7(m+pq)-4(dq+ep).

If all horizontal common first-symbol root components have slope
`base degree / degree over C0 >= rho`, effectivity gives `A>=rho B`.
In an entirely-thick STCI, with `x=d/p`, `y=e/q`, this yields

    ((7-rho)/4)xy+7+rho >= 4(x+y).

The inherited STCI-specific restrictions give `x,y>=3`. Consequently:

- Some common horizontal root component must have slope `<7`.
- If the sole common horizontal root is a graph, its degree is at most
  six.
- If all common horizontal roots have slope at least two, then
  `min(x,y)<=16/5` is excluded, including the normalized pair `(4,4)`.
- For a sole degree-one graph root, `x=3` forces `y>=8`.

These conclusions retain arbitrary vertical exceptional multiplicity.
They concern common roots of the **displayed first symbols**, which
are different from the full initial-ideal root in A1--A2.

The exact balance also gives the residual correction

    7de+28pq+5 delta >=16(dq+ep).

If no residual component lies on the unique quadric, its coefficient
improves from five to one. These are necessary inequalities, not a
residual-existence theorem.

Source: [cycle balance, slope refinement, and examples](../residuals/blowup_residual_geometry.md).
Independent reconstruction: [cycle audit, including slope addendum](../residuals/blowup_residual_geometry.md).

#### A4. Counterexamples and actual higher-degree carriers

The local family

    f=t^N u^p+v^a,  g=f+u^b,  a,b>p>=2

has pure support `V(u,v)` and is finite free of rank `ab` over `k[t]`.
Its first strict-surface intersection has vertical coefficient
`N(b-p)`, unbounded while the generic multiplicity and displayed
orders are fixed. On the subsequence `N=aL`, even the full generic
filtered algebra is fixed up to isomorphism. Replacing `g` by `g-f`
removes the vertical component. The source also gives a homogeneous
projective pure-line example. Thus vertical exceptional multiplicity
is neither a residual curve downstairs nor an invariant of the ideal
independent of its chosen generators.

Two explicit one-parameter smooth-quadric normalization families were
also constructed. Their images are actual integral degree-eight
surfaces containing literal `C0`. Each has isolated extra points in
the full inverse support of `C0`, so no member admits a mate of any
positive degree. The simpler family's full inverse support is
computed exactly; at parameter `gamma=1` it is the diagonal plus
exactly five isolated points. These families do not exhaust the
degree-eight projection model.

Source: [actual degree-eight families](carrier_conductor_differential_comparison.md#smooth-quadric-isolated-inverse-points-prohibit-every-mate).
Independent reconstruction: [carrier audit](carrier_conductor_differential_comparison.md#smooth-quadric-isolated-inverse-points-prohibit-every-mate).

### B. Dependencies and remaining cases

The investigation used the records
[STCI-R-0001](../../results/quartic_carrier_exclusion.md),
[STCI-R-0008](../../results/spectral_root_picard_criterion.md),
[STCI-R-0009](../../results/moving_purepower_boundary.md), and
[STCI-R-0003](../../results/fixed_carrier_conductor_criterion.md)
within their stated scopes. The fixed normal bundle is the
characteristic-zero `N_C0=O(7)^2`. No quartic proof was rerun.

For the numerical `d/p,e/q>=3` input, the exact inherited proof is
the [entirely-thick independent audit](../normal-geometry/rees_and_vertical_controls.md#supported-cycle-bidegrees-and-the-universal-numerical-restriction).
The [entirely-thick topic](../../results/entirely_thick.md) gives the
notation and context for that numerical restriction.
The STCI factor reduction and low-degree exclusion have support
in R-0001 and its linked audit.

The genuinely new bridge is A1, proved in the source and independently
reviewed, rather than an inference from a prior summary. It closes
later special-point normal-layer degeneration within its exact
saturated-first/generic-CI class. A2 then excludes all moving
nonreduced full roots within that actual class. A3 supplies additional
support-sensitive restrictions without requiring that first relation
to be a saturated line.

An independent local Hilbert-function argument is preserved in
[the local normal-flatness proposal](../normal-geometry/normal_flatness_and_filtered_ci.md#2026-10-19-filtered-generic-ci-normal-flatness).
It has its own classical dependency and a separate
[independent audit](../normal-geometry/normal_flatness_and_filtered_ci.md#2026-10-19-filtered-local-normal-flatness-independent-audit).
It is also a reviewed proposal. The projective theorem
has the self-contained resultant/duality proof and does not depend on
this additional classical bound or on the local route's broader scope.

### C. Most promising connection

Gorenstein duality controls a finite-support defect that previously
separated generic formal algebra from the full spectral curve. The
second quotient relation has a generically nonzero resultant of degree
zero. This is the mechanism forcing uniformity; generic coprimality
alone would not suffice. It makes the full Picard obstruction directly
applicable to an actual intersection in a nontrivial infinite class.

The blowup work complements that bridge by retaining chosen-equation
and vertical-cycle information. Its counterexamples show why the
uniformity proof must use the full algebra and projectivity, rather
than interpreting vertical degeneration as a residual component.

### D. Remaining obstacles

1. **Nonsaturated first relation.** Determine the torsion and its
   duality constraints when the first actual kernel is not a
   subbundle. The exact early-layer identification used in A1 then
   fails. The local proposal preserves an explicit nonsaturated
   counterexample; saturation cannot simply be dropped.
2. **Non-CI generic tangent algebra.** An actual transverse Artin CI
   can have an ordinary initial ideal with three or more generators.
   Its generic graded algebra need not be Gorenstein. The complementary
   saturated-power duality in A1 then has no established symmetric
   index formula.
3. **Reduced roots and ambient lifting.** A1 provides graded/spectral
   uniformity; it does not supply arbitrary embedded Cartier lifts of
   a singular root in the actual blowup. Integral singular roots and
   distinct-component roots require actual ambient obstruction data.
4. **Exceptional support distribution.** The class `(A,B)` and its
   slope budget do not determine higher contact along each direction.
   A further global constraint on multiplicities is still missing.
5. **Full-support normalization families.** The explicit degree-eight
   exclusions have isolated inverse points. They do not compute phase
   images for projections that actually satisfy the required full
   singleton inverse support, or address all higher carriers.

No shared singular point of arbitrary defining surfaces is assumed.

### E. Recommended continuation and evidence checks

First study the torsion of the earliest nonsaturated relation and how
its length changes the degree-zero resultant calculation. A useful
target is an exact effective-defect formula replacing the zero degree
in A1; one must keep the torsion in every comparison map. In parallel,
investigate codimension-two non-CI generic initial ideals with the
smallest number of additional generators, using their actual
annihilator flags rather than assuming graded Gorenstein symmetry.

For the saturated generic-CI class, direct effort toward reduced
singular roots and the equal-slope rational-component pairs identified
in A2. Additional nonreduced spectral scans are unnecessary in that
class. The chosen-symbol slope theorem gives a separate way to select
surviving normalized-degree regions without conflating the two root
objects.

All principal results have full proof text and separate review evidence; there is no uncompleted elimination computation underlying the reported claims. Mathematical validity rests on those proofs and independent reconstructions, including the separate adversarial review of A1.

The package is recorded at
[the research commit](https://github.com/markluxton1/STCI/tree/6be25be178b1e34e1209172f92dee6816e7aa87b).
The exact closing commit is identified in the investigation message.
Standard external inputs, with direct primary links, are identified in
the respective source and audit notes.

---

<a id="2026-10-16-session-structural-continuation"></a>

## October 16 structural continuation and successor entry

The universal integral-curve STCI question and unrestricted characteristic-zero
`C0=[s^4:s^3t:st^3:t^4]` remain **OPEN**. The October 13
all-branch reconstruction remains an accepted premise; no branch-source
or accepted mathematical verifier was replayed in this continuation.

The current externally observed checkpoint is
`bf124f8ab962ef0ed4085397034c50ee8d0d7162`, title
`2026-10-15 afternoon limit reached`. The primary agent did not create
that commit. This continuation has further working-tree changes.

### 1. The strongest structural generalization

The new [intrinsic finite-root-family theorem](../spectral/finite_root_families_and_smooth_obstructions.md#2026-10-15-generalization-intrinsic-finite-root-family)
and [independent new-scope audit](../spectral/finite_root_families_and_smooth_obstructions.md#2026-10-15-generalization-intrinsic-finite-root-family-independent-audit)
remove the rational-base and split-normal-bundle hypotheses from a fixed
bounded smooth-root family. If `A=Z^2_E`, `nu=E.Z`, and
`nu>max(A,0)`, all successive correction lines have negative degree
`A-m nu`. Relative cohomology gives obstruction bundles of rank
`g_Z-1-A+m nu`, compatibly with arbitrary parameter base change, including
nilpotent directions. The embedded-Cartier ideals are unique whenever
they exist, so their closed obstruction schemes remain in one fixed
finite-type space and eventually stabilize as schemes.

For the actual blowup of **any** fixed smooth space curve of degree e
and genus gamma, the actual exceptional ruled surface obeys

```
A=(4e+2gamma-2)r^2-2r nu,
A=2g_Z-2+4er-2nu.
```

Fixed `(r,nu)` fixes numerical class and Hilbert polynomial. One smooth
Cartier Hilbert open therefore contains all smooth connected roots of
that class. If `nu>4g_Z+5`, a hypothetical infinite lift also requires
a positive integer d satisfying

```
d<=max_(a>=1 integer)(2aer-nu a^2),
(d-1)(d-2)>=e r(r-1).
```

Incompatibility makes the stable scheme empty, and gives a finite
uniform empty stage N over the whole fixed family. Under a valid
actual-CI bridge, `s-r<=N`. The theorem does not compute N, bound all
numerical classes, or treat singular/nonreduced roots. Its new intrinsic
proof and audit state characteristic-zero scope.

This contains the preceding balanced-rational movement-two result:
for e>=4 and every r>=2, all smooth roots of class `(2,r)` have no
infinite formal lift. Movement-one roots of order r>=2 are also excluded
for e>=3; for r=1,e>=4, their all-orders lifts are exactly containing
quadric germs smooth along C. The broader inequalities, rather than
separate carrier degrees, are the continuing geometric mechanism.

### 2. Characteristic and actual-CI bridge

The [formal characteristic addendum](../spectral/finite_root_families_and_smooth_obstructions.md#2026-10-15-generalization-smooth-root-characteristic-scope-addendum)
accepts the balanced-rational formal theorem and finite tower in every
algebraically closed characteristic, with its explicit normal-bundle
and smooth-root hypotheses.

The [inseparable-root actual-CI bridge](../spectral/uniform_root_towers_and_inseparable_bridges.md#2026-10-15-generalization-inseparable-root-blowup-bridge)
now also has a [full independent new-scope PASS](../spectral/uniform_root_towers_and_inseparable_bridges.md#2026-10-15-generalization-inseparable-root-blowup-bridge-independent-audit).
It uses the actual root prime over `k(C)` and an uncompleted standard
basis, retaining inseparable residue fields. The original strict-divisor
intersection is locally `(h,u^(s-r))`, without saturation or removal
of a vertical component. Its Cartier-root stages are precisely those
with `m<s-r`. Thus the same gap bound applies in every characteristic
within the literal saturated-line, joint-leading-generation, full
generic-initial-CI and smooth-full-root hypotheses. No assertion about
literal C0 splitting in bad characteristics is inserted.

### 3. Arithmetic reduction of all mate powers

The [effective rational phase theorem](projection_torsion_and_rational_phase_bounds.md#2026-10-15-generalization-effective-rational-phase-bound)
and [arithmetic review](projection_torsion_and_rational_phase_bounds.md#2026-10-15-generalization-effective-rational-phase-bound-independent-review)
are accepted. For an explicit rational constructible phase image,
Mann's theorem, finite cyclotomic calculations and Smith normal form
give a finite exact coset/boundary certificate. It decides torsion
existence, detects unbounded least mate degrees through a surviving
positive-dimensional coset, and bounds phase orders by `P(S)d^D` if
only isolated cosets survive. The three fixed projection models have
on-C thresholds 5,5,13, so the corresponding least-degree bounds are
that phase bound plus 4 or 12.

The whole fixed normalization families stay over Q, retaining all
branch choices. A stronger corollary starts from finite rational
section/module data for these three fixed models and constructs the
actual phase image by a terminating algebraic procedure; the written
review contains its scope addendum. A fresh
[October 16 raw-input scope audit](projection_torsion_and_rational_phase_bounds.md#reviewed-claim-and-input)
now passes the final admissibility and generic-freeness formulation.
The precise finite rational input is one of the three fixed source
rings with H,c,Q, four polynomial parameter sections with their prescribed
C0 restrictions, and finite constructible parameter conditions. The
terminating algorithm decides whether any actual carrier in that input
family has any mate, and whether its least mate degrees are unbounded
or admit a computable uniform bound. It does not require an oracle for
unspecified class groups or arbitrary coefficient fields.
No actual phase image, Mann partition list, or family decision has been
computed. Neither practical complexity nor a numerical C0 bound follows
from the existence of the algorithm.

### 4. The dedicated quintic target

Accepted shared reductions now include the global remaining-mate
Delta1 unit, exact q6-to-j scalar binding, eleven-generator reduction,
automatic `(q5,q6)=1`, and the equivalent eight-equation logarithmic
ODE on the declared rational inverse-map chart. The reviewed eta
spectral accelerator retains one ideal rather than separate degree,
root or norm-factor cases.

The new [global monic h2 ODE model](https://github.com/markluxton1/STCI/blob/63b401a4b399c435fe292820dcbf630470e01ff6/research/supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence)
is the next whole-h2 target. It uses the original parameters, a monic
quadratic H, four conormal remainders, two actual-conductor remainders,
eight ODE coefficients and three derived accelerators: seventeen equations
in nine variables, with only `delta*E*Delta1` inverted. Its purpose is
to retain the repeated-root and cover-determinant boundary that the
earlier rational inverse-map chart could not cover. The
[final global scope audit](#2026-10-16-generalization-quintic-h2-global-monic-ode-independent-audit)
now passes the whole-h2 cover and current exact artifact bindings. Its
[runnable input](https://github.com/markluxton1/STCI/blob/bb5b1d5348097028738db196c262fe44b81b69ca/research/computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
is saved and passed a load-only check. One subsequent capped global QQ
saturation reached GB but produced no result, as recorded below. The one
next saturation target is `h2GlobalIdeal : h2GlobalDomainUnit^infinity`,
with all repeated-root and cover boundaries retained in the same model.

The quintic is not closed. The earlier h3, coprime, endpoint and stated
residual-partition exclusions remain accepted. Other quintic
normalizations and retained h1 singular/intrinsic/common-root scope
remain separate obligations. A whole-h2 unit-ideal certificate would
not by itself prove a whole-quintic theorem.

### 5. Computation and continuation state

The complete global quadratic-root second model uses twenty-five scalar pairings and retains the homogeneous branch discriminant, including infinity. Its completeness is not an emptiness result. The bounded quintic ODE, spectral and global QQ saturation attempts did not complete an ideal computation or unit certificate. The twenty-two finite family-two exception-root closures and accepted large quintic witnesses remain separate premises.

---

<a id="2026-10-16-generalization-quintic-h2-global-qq-prospect-terminal-record"></a>

## Whole-h2 global saturation remains open

The accepted seventeen-equation, nine-variable model over `QQ` retains
repeated roots and the finite cover boundary. Its
[runnable input](https://github.com/markluxton1/STCI/blob/bb5b1d5348097028738db196c262fe44b81b69ca/research/computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
loads the exact equations and domain polynomial. The target is

```macaulay2
saturate(h2GlobalIdeal, ideal h2GlobalDomainUnit)
```

on the domain `delta*E*Delta1 != 0`. No rational-cover determinant,
quadratic discriminant, quotient coefficient or `Jbar` is additionally
inverted. A bounded attempt did not complete this saturation and supplied
no ideal, dimension, unit certificate or emptiness conclusion. The global
H2 incidence remains undecided. Its geometric scope is the
[global monic ODE incidence](https://github.com/markluxton1/STCI/blob/63b401a4b399c435fe292820dcbf630470e01ff6/research/supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence)
and the [independent argument](#2026-10-16-generalization-quintic-h2-global-monic-ode-independent-audit).

---

<a id="2026-10-16-generalization-quintic-h2-global-monic-ode-independent-audit"></a>

## Independent audit: one global monic h2 ODE incidence

Date: 2026-10-16.

Status: **PASS for the new global monic cover, original-parameter
coefficient assembly, and transfer of the accepted ODE/spectral
algebra to the domain delta*E*Delta1 nonzero.** The seventeen
equations in nine variables retain the finite inverse-map boundary.
This is a necessary incidence for every remaining actual h2 mate
candidate, not an emptiness or mate-existence theorem.

The reviewed proposal is
[the global monic incidence note](https://github.com/markluxton1/STCI/blob/63b401a4b399c435fe292820dcbf630470e01ff6/research/supplements/QUINTIC_H2_MONIC_ODE_AND_OPEN_INCIDENCE.md#2026-10-15-generalization-quintic-h2-global-monic-ode-incidence).
Accepted conormal forms, the actual octic, the global h2 conductor
factor, previous mate closures, the Delta1 open, and ODE/spectral
proofs are premises. No accepted proof or verifier was replayed.
This audit uses written coefficient calculations and read-only
source/artifact/hash inspection. No CAS was run during completion
of this audit, and no model assembly or elimination was repeated.

### 1. Monic coverage and exact homogeneous gcd degree

For any remaining actual h2 mate candidate, a common factor at source
infinity would force G=j=0 by the accepted leading-coefficient
equations. The accepted mate closure excludes that lane. Thus the
complete degree-two homogeneous gcd has nonzero t^2 coefficient,
and its unique monic representative is

    H(x)=x^2+v*x+w,       x=r/delta=t/s.

This monic chart is therefore global for the remaining h2 mate
candidates. It imposes no distinct-root hypothesis. It also does
not normalize delta to one.

Write the literal normalized cubics as

    P=G*x^3+P2*x^2+P1*x-2a,
    Jc=(G+2j)*x^3+J2*x^2+J1*x-a-B,

where

    P2=6B+delta^2-3delta,       P1=3a-3B+2delta,
    J2=6B+3G+5delta^2-3delta,   J1=3a+3B+delta-delta^2.

Set A=G, Bc=P2-vG, C=G+2j, Dc=J2-v(G+2j). The leading two
coefficients of (Ax+Bc)H and (Cx+Dc)H match the cubics identically.
Their remaining coefficients match precisely when

    -2a-w*Bc=0,       P1-v*Bc-w*A=0,
    -a-B-w*Dc=0,      J1-v*Dc-w*C=0.                  (1)

These are exactly the four saved cover equations, with no coefficient
system inverted. Direct expansion gives

    E=A*Dc-Bc*C
     =G*(3G+4delta^2)-2j*(6B+delta^2-3delta).          (2)

The terms involving v cancel. The unit E is the determinant of the
two homogeneous linear cofactors A*t+Bc*s and C*t+Dc*s. At field
points they are independent exactly when they are coprime, so (1)
and E nonzero give complete homogeneous gcd degree two. This
includes affine degree drops of either cubic. A zero cubic or a
proportional cofactor pair instead has E=0 and is correctly outside
the exact-h2 domain.

### 2. Fixed-degree octic reversal and monic division

For the accepted actual Fdet(p,1)=sum_(i=0)^8 f_i*p^i, reciprocal
source coordinates give Fsrc(1,x)=sum f_i*x^(8-i). Put q7=q8=0
and define downward

    q_i=f_(6-i)-v*q_(i+1)-w*q_(i+2),    i=6,...,0.

For the coefficient of x^(i+2) in H*Q, this is exactly
q_i+v*q_(i+1)+w*q_(i+2)=f_(6-i). Therefore all coefficients
of degree at least two match, and the remaining two coefficients
are exactly

    r0=f8-w*q0,
    r1=f7-v*q0-w*q1,
    Fsrc=H*Q+r1*x+r0.                                (3)

The two explicit equations r0=r1=0 are retained. The accepted
geometric factor theorem supplies them for every actual h2
projection; this assembly does not extend that theorem to a
divisibility assertion over an arbitrary nonreduced
conormal-cover base. After the equations are imposed, (3) is an
exact ring identity on the incidence.

Monic division introduces no parameter denominator. Fixed degree
eight reversal and degree six quotient retain all coefficient drops
and the source point at infinity. In particular q6=f0 and
q5=f1-v*q6 have the intended A4 interpretation.

### 3. The new global domain does not invert Delta or K

The domain is exactly

    delta*E*Delta1 nonzero,
    Delta1=G(G+3delta^2)(G+delta^2+2B)
      +j[(delta^2-5B)G-3B(delta^2+3B)]-B*j^2.         (4)

Delta1 is necessary for all remaining mate candidates by the accepted
closures and A4 support argument. Delta=v^2-4w and
K=v^2+6vw+6w^2+2w are not factors of the declared unit product.
Thus the repeated finite-root boundary and the failed rational
inverse-map boundary remain represented by the original equations.
An accepted inconsistency on part of that boundary may be used as
a theorem, but no such locus is silently cancelled from this model.

For the unscaled actual quotient, the accepted A4 coefficients give

    q6=-3j*Delta1,
    q5=-2(G+3delta^2)*Delta1 modulo j.                (5)

There is no captured inverse-map scalar here. The accepted automatic
open proof now applies with kappa=1: the explicit Delta1-square
membership, or its equivalent quotient-ring argument, gives
(q5,q6)=1 after (4). This is an exact ideal equality and includes
nonreduced bases. It needs neither Delta nor K to be a unit.

The previous ODE and spectral proofs use monic H, (5), the Delta1
unit, coefficient unimodularity and field scalars 2,3. They therefore
apply unchanged to this original-parameter ring before any rational
inverse of the four cover equations. Their earlier actual use on a
smaller inverse-map chart does not limit this algebraic transfer.

### 4. The seventeen-equation system and its precise meaning

Using eta=dv-2u, the eight ODE coefficients are exactly

    2w(i+1)q_(i+1)+[(2i-d)v+eta]q_i
                         +2(i-1-d)q_(i-1),
    i=0,...,7.                                        (6)

These are twice the coefficients of H*q'-(dx+u)q. The change from
u to eta is invertible. The accepted globally unique ODE-witness
argument applies by (5), so (6) is the same shared rank/support
incidence on this domain, including its j=0 allowance.

There are four equations (1), two equations (3) and eight equations
(6), making fourteen. The three accepted derived equations

    (d-5)(d-6),       j(d-6),
    (d-5)P6(eta)+(6-d)P5(eta)

bring the saved presentation to seventeen equations in the nine
variables delta,a,B,G,j,v,w,d,eta. They belong to the same localized
ODE ideal, so appending them changes no scheme on (4). The temporary
variables p and x used in assembly are not additional model variables.

On actual admissible h2 projections, this incidence expresses the
accepted restricted-conductor support obligation. Every remaining
actual h2 mate candidate lies in it. The model does not impose center
avoidance or all original fiber conditions, and it does not establish
full inverse support or nonlinear conductor descent. An algebraic
survivor is therefore not automatically a projection or a mate.

### 5. Exact model and checking boundary

The [assembly source](https://github.com/markluxton1/STCI/blob/add6e1664e6d9db84e67fb0276a318a804b3d2f8/research/computations/generalization_quintic_h2_global_monic_ode_export_2026_10_15_attempt02.m2) derives the model from the literal accepted octic, reversed coefficients, recurrence, four cover equations, eight ODE equations and three accelerators. Its polynomial assertions check the cofactor and quotient/remainder identities. The retained seventeen-equation row and original domain polynomial supply precisely the incidence (4); grouped and individual coefficient exports are redundant representations.

The new currently runnable
[load-only input](https://github.com/markluxton1/STCI/blob/bb5b1d5348097028738db196c262fe44b81b69ca/research/computations/generalization_quintic_h2_global_monic_ode_input_2026_10_16.m2)
reads the completed seventeen-equation row and domain polynomial
over QQ in the stated nine-variable order. It asserts the ring,
matrix shape and nonzero domain polynomial, and retains the objects
h2GlobalRing, h2GlobalEquations, h2GlobalIdeal and
h2GlobalDomainUnit. It constructs no coefficient map and calls no
Groebner basis or saturation operation. The domain polynomial is
loaded as data for a future localization; the load-only script does
not itself localize or prove the domain nonempty.

Loading the completed input checks its ring and equation presentation. It is distinct from assembling the coefficients and supplies no saturation or elimination result.

The one global future target is therefore the saved seventeen-equation
incidence localized at (4). No Gröbner basis, saturation, resultant
or emptiness computation for this global model is certified here.
A result restricted to Delta*K nonzero cannot close this larger
incidence. The unrestricted quintic and STCI questions remain outside
the conclusion of this audit.
