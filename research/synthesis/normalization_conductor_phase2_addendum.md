# Ruled normalizations and the conditional sextic lifting problem

## Paired-secant cubic

The finite normalization of the cubic x0*x2^2=x1^2*x3 is F1, with hyperplane class E+2f. On x0=1 its local ring inclusion is k[r,rw,w^2] inside k[r,w]. The upstairs conductor is (r); the downstairs conductor is the reduced double-line ideal (x1,x2). The conductor section maps two-to-one to the line, branched at the endpoints. The strict quartic lift has class 2E+2f, but the full inverse ideal is (w-r^2)(r,w), with an embedded length-one defect at each endpoint. The same F1 is the smooth cubic scroll S(1,2) in P4, projected from the omitted middle coordinate. On the smooth quadric the cubic cuts C0 plus the two limiting tangent trisecants. In characteristic two the conductor cover is inseparable and the scroll is a tangent developable.

Sources: [current proof](../supplements/CUBIC_SCROLL_AND_RULED_SURFACES.md#cubic-scroll-normalization) and [current proof](../supplements/CUBIC_SCROLL_AND_RULED_SURFACES.md). Independently reviewed geometry, not a new STCI result.

## Projection cone and four-section quartic

The projected cone over C0 has ring k[s^4,s^3t,st^3,t^4], missing the integral element s^2t^2. Its normalization is the complete fourth Veronese cone, with conductor supported at the vertex and an upstairs dual-number quotient. The correct factorization is F4 contracting the negative section to the normal cone, followed by finite normalization of the projected cone. F4 itself is not finite over the projected cone. The related four-section quartic has conductor (x0,x1)^2 downstairs; its transverse ring is k[v^3,v^4,b] inside k[v,b], with conductor v^6. Full inverse ideals can have embedded endpoint corrections of colength six.

Sources: [current proof](../supplements/CUBIC_SCROLL_AND_RULED_SURFACES.md) and its independent audit. Elementary transformations and mu4 arithmetic remain in the ruled-geometry family.

## Conditional (6,16) singular-root interface

The October 20 proposal assumes an actual supported (6,16) pair, full generic coprime normal CI (2,12), and an actual saturated movement-two first relation. The (2,2) spectral root Z must satisfy O_Z(1,-1)^12 trivial. A reviewed finite singular-root bridge has transform ideal (p,u^10), providing finite embedded Cartier lifts even for singular Z. Full spectral torsion eliminates cuspidal and tangent-component roots; smooth, nodal, and two-node reducible roots retain their gluing conditions. The next global step is cubic-jet matching for a genuine sextic, [F3-alpha*G0] mod (f)=0, without dividing by alpha at its zeros. Abstract Cartier lifts do not yield global equations or a support certificate.

The October 21 conductor-budget proposal originally depended on an anticanonical contraction hypothesis. The independent continuation audit subsequently VERIFIED that hypothesis in the precise actual-pair setting: a cubic-image model V is a smooth integral threefold with canonical bundle O(-2), and the strict sextic descends to an integral anticanonical surface T. Finite duality and the local monic double-cover normalization then exclude singular-curve contacts at ramified simple base zeros. Combined with the separate nodal analysis, the reviewed result gives a sharp NECESSARY alternative for any actual pair: the multiplier alpha has a multiple base zero, or alpha vanishes at a node of the full root. For a smooth full root the necessary discriminant equation is Disc_8(Ncomp(tau))=0, of degree 28 in the root coefficients. These exceptional strata have not been eliminated; no complete exclusion follows. A different proposed nodal normalization obtained by dividing by a nonunit was rejected as nonfinite. Its suggested integral replacement is not yet certified normal or equipped with an exact conductor.

Sources: [current proof](../supplements/SINGULAR_ROOT_ACTUAL_PAIR_BRIDGE.md) and [current proof](../supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-conductor-ramification). Conditional cross-family work.

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

The exact cubic model, graph identification, conductor duality, and simple-zero exclusion received an independent **PASS under the conditional actual-pair hypotheses**. A different nodal example's purported finite normalization by dividing by a nonunit was explicitly **rejected** and is not used. No unconditional \((6,16)\) or STCI exclusion follows. [Cubic image and conductor construction](../supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-cubic-image-and-conductor-interface); [independent review and rejected nodal claim](../supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-surface-audit-cont2).

## Exact global sextic-symbol restriction in the conditional (6,16) lane

For an actual supported \((F_6,G_{16})\) pair with **full fiberwise coprime** generic normal CI \((2,12)\) and an **actual saturated movement-two** first relation, write the basepoint-free quadratic first root \(f=a(z)u^2+b(z)uv+c(z)v^2\) and the degree-six symbol \(\sigma_2(F_6)=\alpha f\), where \(\alpha\in H^0(\mathbf P^1,\mathcal O(8))\) is nonzero. A global sextic does **not** have an arbitrary symbol in \(H^0(\mathcal O(10))^3\). The exact map
\[
H^0(I_{C_0}^2(6))\longrightarrow H^0(\operatorname{Sym}^2N_{C_0/\mathbf P^3}^{\vee}(6))
\]
has source dimension 23, rank 22, kernel \(kq^3\) (with \(q=x_0x_3-x_1x_2\)), and image cut out by **eleven independent linear equations** in the 33 symbol coefficients \(P_j,Q_j,R_j\). A source basis consists of \(q^2\) times the ten quadrics; \(qA\) times \(x_0,x_1,x_2,x_3\); \(qB\) and \(qD\) times \(x_2,x_3\); and \(A^2,AB,AD,BD,D^2\), with \(A=x_0^2x_2-x_1^3\), \(B=x_0x_2^2-x_1^2x_3\), \(D=x_2^3-x_1x_3^2\). The eleven equations are, in order,
\[
\begin{gathered}
P_9-2Q_{10},\quad Q_0-2R_1,\quad P_0-2Q_1+4R_2,\quad
3P_1-2Q_2-4R_3,\\
P_2-2Q_3+4R_4,\quad P_3-2Q_4+4R_5,\quad P_4-4R_6,\quad
P_5-2Q_6+4R_7,\\
P_6-2Q_7+4R_8,\quad P_7+2Q_8-12R_9,\quad P_8-2Q_9+4R_{10}.
\end{gathered}
\]
Substituting \(P=\alpha a,Q=\alpha b,R=\alpha c\) gives **eleven bilinear global-symbol equations**. They do not invert \(\alpha\) at its zeros. For fixed compatible \((f,\alpha)\), global sextics with this symbol differ by \(\eta q^3\).

The next necessary global lifting equation compares the **actual cubic jet** of such a sextic with the unique first-compatible local cubic correction \(G_0\):
\[
(F_c)_3-\alpha G_0=f(\ell(z)u+m(z)v),\qquad \deg\ell,\deg m\le7.
\]
This is a finite 40-coefficient condition, distinct from the first and second local ambient classes and from the full spectral torsion criterion. The smooth torsion-two seed \(f_0=(z^2+4)u^2+(z^2-8)v^2\) admits a unique projective multiplier \(\alpha_0=z^8-8z^6+96z^4+256z^2+1024\) satisfying the eleven equations, but it **fails** the cubic comparison (an exact annihilating pairing is \(-384\)) and already fails the independently accepted second obstruction. This is a seed exclusion, not emptiness of the combined incidence.

The reviewed singular-root bridge uses the actual transformed ideal \((p,t^{10})\) and proves necessity of the ambient classes even for singular reduced roots, under the stated actual-pair hypotheses. The remaining structured scheme also retains all twenty-five second-obstruction pairings and full-scheme spectral torsion (including nodal gluing); its emptiness, nonemptiness, and realization by a globally supported pair are **unresolved**. The independent audit passed the exact symbol map and conditional necessity reductions, without establishing a general STCI exclusion. [Symbol map and cubic comparison](../supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-symbol-map); [global incidence](../supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-global-realization-incidence); [independent audit](../supplements/CONDITIONAL_2_12_SURFACE_AND_SYMBOL_GEOMETRY.md#2026-10-20-conditional-2-12-incidence-audit).

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

In the stated bounded coefficient model this question is now settled exactly: the [rank-drop classification](rank_strata_and_sextic_lifts.md#5-the-exceptional-root-as-a-degeneracy-locus) proves that the enlarged map has rank sixteen only at the single projective root \([f]=[(u+zv/2)^2]\), and rank seventeen elsewhere. The necessary actual-pair open \(f(-z/2,1)\not\equiv0\) excludes that point. Thus the varying-lift cubic quotient has rank twenty-three throughout that admissible open, and cubic compatibility determines a unique actual sextic. This classifies a linear ambiguity; it does not compute the remaining nonlinear incidence or supply a mate.


The coefficient equations become \(h_i+\eta\tau_i=(a\ell,\ b\ell+am,\ c\ell+bm)_i\), with the fourth coefficient \(cm\). They remain division-free. Any claim that a seed fails the cubic comparison must specify whether the test allowed the \(q^3\) direction; a fixed-lift failure alone does not exclude all sextics with the same quadratic symbol. The independently computed second obstruction is unaffected by this logical distinction, subject to its original hypotheses.

## Existing full-lift exclusion on the free cube-orbit chart

The historical [free cube-orbit global sextic calculation](../supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-cont2-free-orbit-global-sextic-exclusion) already includes the previously omitted \(\eta q^3\) freedom. It concerns a **restricted chart**, not all quadratic roots: the multiplier is the canonical cube norm of the quadric-line restriction, both endpoint coefficients are nonzero, and no two roots lie in the same primitive-cube orbit. The application to actual supported pairs additionally depends on the separate quadric-cycle norm necessity bridge.

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

The historical [forced-norm two-node continuation](../supplements/CONDITIONAL_2_12_SINGULAR_AND_CONDUCTOR.md#2026-10-21-conditional-2-12-singular-continuation2) gives more than an unclassified singular-root boundary. Under its stated actual-pair, saturated movement-two, forced-norm and two-node hypotheses, it computes the nonzero cubic-defect locus. The generic component decomposes into a line and a conic. The **entire generic line component** is excluded by exact first-incidence plus spectral-torsion unit calculations for \(w=1\) and the primitive cube-root branches. The nonzero-defect \(B=0\) and \(C=0\) boundaries are also excluded, the latter by the actual involution \(x_0\leftrightarrow x_3,\ x_1\leftrightarrow x_2\). These are scoped coefficient-scheme exclusions, not an unrestricted characteristic-zero theorem.

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

The preceding root and symbol data acquire a stronger necessary multiplier only from an **actual** degree-(6,16) pair with sole reduced support, full generic coprime ordinary initial CI (2,12), and actual saturated movement-two first relation. Let `B=Bl_C(P3)`, `E` its exceptional divisor, and use the reviewed transformed ideal `(p,t^10)` at every full-root point. Let `Q=(q=0)`, `q=x0x3-x1x2`, identify `C~(1,3)` on Q, and write `pi3:C→P1_ruling`, `z→z^3`. The quadric direction is `q1=u+zv/2`; for `f=a u²+buv+c v²`, put `tau=f(-z/2,1)`. This is a homogeneous quartic. The argument below explains why its **actual residual cycle**, rather than merely its generic symbol, forces the complementary norm multiplier. It preserves the independently reviewed source proof.

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

The local formula implies more than the total equality (2). Write
`R=sum m_y L_y` as a divisor of ruling fibers. Since `T.L_y=10`,
and `T` has no component `L_y`, restriction to that fiber gives

    10*m_y
       =sum_(x in C0 intersect L_y) i_x(R,T)
       =10*sum_(x in pi3^-1(y)) ord_x(tau).

Hence the actual divisors satisfy

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
Its homogeneous version is nowhere zero for every nonzero `tau`.

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


## Geometric exceptional locus for actual pairs

The October 21 independently reviewed geometric argument gives a necessary condition beyond the sextic symbol incidence. Under actual sole support and the saturated movement-two hypotheses, the full-root multiplier divisor cannot be reduced. For a normal strict sextic, local singularities force total Milnor number at least 144, whereas the global resolution argument bounds it by 50. The nodal extension uses the ample strict mate to eliminate nonnormal singular curves when the divisor is reduced. Hence candidates must lie on the explicit degree-52 discriminant-resultant exceptional locus
\[
\operatorname{Disc}_8(N_{\rm comp}(\tau))\,\operatorname{Res}_{8,4}(N_{\rm comp}(\tau),\Delta)=0,\qquad\Delta=b^2-4ac.
\]
The degrees in the original root coefficients are 28 and 24. The earlier degree-64 condition also included `Disc_4(Delta)`; the reviewed nodal extension removes that factor, since singular roots with a reduced multiplier divisor have already been excluded. Every homogeneous infinity root remains included. This does not prove the exceptional locus empty. See the historical geometric-audit-and-exceptional-locus note for the proof and its dependencies.

## Singular curves on the strict sextic: two conditional alternatives

The reviewed geometric continuation further classifies a singular curve \(\Sigma\) on the strict sextic, provided that the sextic is normal near the multiplier-zero points of the full root. Let \(n\le2\) count its transverse contacts with ordinary root nodes, \(d=H\cdot\Sigma>0\), and \(e=E\cdot\Sigma\). Multiple multiplier fibers can contribute additional contacts with \(E\), so **one must not set \(e=n\)**. The strict mate gives the exact degree identity
\[
16d-2e=10n.
\]
If \(\Sigma\) is not contained in the strict quadric \(Q'\sim2H-E\), effectivity gives \(e\le2d\), whence \(12d\le10n\le20\). For \(d\ge2\) this is impossible; \(d=1\) forces \(n=2\), then \(e=-2\), also impossible. Thus \(\Sigma\subset Q'\).

The intersection of the strict sextic with \(Q'\) has ruling class \((4,0)\). Consequently \(\Sigma\) must be a trisecant ruling line, with \(d=1\), \(e=3\), \(n=1\), meeting the full root at one ordinary node in the quadric direction. Its multiplicity in the sextic-quadric intersection is at least two. The forced norm then requires additional multiplier multiplicities along its ruling orbit. The line is not an endpoint branch fiber.

Accordingly, a remaining actual pair under these hypotheses must exhibit **either** nonnormality at a multiplier-zero root point **or** this precise singular trisecant ruling line. This is a conditional classification, not an exclusion. See the [reviewed source](../supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-geometric-audit-and-exceptional-locus), section 7.

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

The source system has 39 unknowns (23 actual sextic coefficients and sixteen correction coefficients), coefficient rank 39 and augmented rank 40. The row above is the small adequate support; the full source matrices retain the coordinate identification. The seed also fails the separately accepted second obstruction, but that independent exclusion is not needed for this cubic certificate. No emptiness result for the full parameter incidence follows: singular roots, all twenty-five second-obstruction pairings, spectral gluing, and the global mate problem remain.

## What the conditional (6,16) computation actually tests

This lane is a controlled illustration of the distinction between a root scheme, an ambient symbol, and an actual supported pair. Its quadratic normal root and movement-two relation impose a spectral condition on the full root, but the degree-six symbol must also lie in the **rank-22 image** of the global map from the 23-dimensional space of sextics vanishing twice along C. Its one-dimensional kernel is generated by \(q^3\); the eleven independent linear constraints on the 33 symbol coefficients are therefore genuine global-source conditions, not optional genericity assumptions.

The cubic-image and conductor calculation adds a further restriction **conditional on an actual supported pair**: the multiplier has a multiple base zero or vanishes at a node of the full root. The smooth-root discriminant condition and the remaining exceptional strata are necessary tests, not a proof that a proper pair exists or that every (6,16) pair is excluded. In particular, the rejected nonfinite nodal normalization cannot be used to close the nodal stratum.

These conditions sit at different logical levels: (i) root and formal normal algebra; (ii) actual global sextic source; (iii) conductor geometry for a supported pair; and (iv) the still-unresolved exceptional locus. Their conjunction is a candidate-family test, not a universal implication between the global determinant, residual-jet and conductor-descent routes. See [Chapter 3](03-infinitesimal-geometry.md#311-embedded-one-step-lifting-and-the-actual-homogeneous-source) and [dependencies](DEPENDENCIES.md).

## Why the conditional sextic conductor does not solve descent

The seven-cubic contraction supplies an exact anticanonical surface model **assuming an actual supported pair**. Its duality calculation constrains the conductor of that model, and the simple-zero argument eliminates a specified ramification stratum. This is logically different from the full-conductor descent test for an independently chosen normalization and a proposed mate: in the sextic argument the pair is an antecedent, whereas in the projection program its existence is the conclusion sought.

The eleven linear equations defining the global sextic-symbol image likewise impose necessary realization conditions without selecting a proper degree-sixteen mate. The remaining multiple-base-zero and nodal-contact loci therefore require direct treatment; neither the cubic-image duality nor the symbol rank closes them. For the general descent framework and the role of nilpotent conductor phases, see [Chapter 4](04-carriers.md#42-the-full-conductor-descent-criterion) and [the projection phase synthesis](../supplements/CONDUCTOR_DESCENT_ALGEBRA.md).

## Remaining boundaries

No arbitrary projection classification, full conductor phase image, higher-index exclusion, global spectral realization, or unrestricted characteristic-zero STCI theorem follows. The broader source branches are integrated by subject elsewhere; the restrictions here remain conditional and do not claim that every carrier falls in this lane.


Source for the stronger reviewed result: [the actual-pair cubic-model and conductor argument](../supplements/CONDITIONAL_2_12_CONTINUATION_AND_SEXTIC_EXCLUSIONS.md#2026-10-21-conditional-2-12-surface-audit-cont2), sections 2–6. Its independent review reports PASS for the cubic-model interface, full conductor duality, and ramified simple-base-zero exclusion, while expressly rejecting the defective nodal normalization. The finite singular-root bridge remains reviewed.


### Geometric scope of movement two

The canonical reduction STCI-R-0014 identifies movement epsilon with the degree of the coefficient map from C to the projective space of binary degree-r forms. Its first normal-root divisor has bidegree (epsilon,r) on P1_base x P1_direction. In the conditional (6,16) setting, r=2 and epsilon=2, so the full first root is a divisor of bidegree (2,2). Saturation means the coefficient map has no base points; it does not exclude root collisions or ensure coprimality of specialized initial forms. Generic binary-CI coprimality and saturation are separate assumptions. The six numerical rows, including (r,s;a,b)=(2,12;6,16), are necessary candidates only under the complete hypotheses of STCI-R-0013 and STCI-R-0014; they are not a classification of arbitrary STCI presentations.

Source: research/results/movement_two_six_rows.md (STCI-R-0014), geometric clarification in commit ccc9c3965e1645ed2569405e0194e31edb38e9d0.

## The common lifting mechanism

For the exact linear-algebra statement separating a fixed symbol from its affine lift fiber, see [global lifting interfaces](global_lifting_interfaces.md). Here the symbol map has domain dimension 23, image rank 22, and kernel kq³. The cubic correction map μ_f has constant rank 16 for f≠0. Its actual obstruction is therefore the cubic target modulo `im μ_f + k(q³)_3`, of dimension 23 on the actual-pair-admissible open, with the single rank-drop root classified in [varying actual-source lifts](rank_strata_and_sextic_lifts.md). This calculation measures the obstruction to meeting the chosen cubic correction space with an **actual global sextic fiber**; it is not a dimension count proving the nonlinear incidence empty. Higher ambient classes, spectral gluing, a proper degree-sixteen mate, and sole support remain separate.

## Endpoint-four: the finite actual-equation question

On the retained integral nodal endpoint-four chart, normalize a0=1 using the actual ambient torus and its square-root cover as proved in [endpoint-four actual sextics](../supplements/ENDPOINT_FOUR_ACTUAL_SEXTICS.md). The root coefficients become
\[
a=1+2b_2z+z^2,\quad b=(\rho+1)z/2+b_2z^2,\quad c=\rho z^2/4,\qquad \rho^{12}=1,\quad\rho\ne1.
\]
Every target second symbol z^8f has the actual sextic family displayed in that proof, with the full free q³ coefficient. For each nontrivial twelfth root, over its exact cyclotomic field and retaining the nodal and finite-ruling opens, the remaining question is whether some actual global degree-sixteen form has remainder after division by F6 vanishing through normal degree eleven, with a coprime degree-twelve term.

The coefficients of that mate remain global constants. The actual first-relation multiplier must be nonzero at the endpoint where z^8 vanishes, and the two multipliers must generate the saturated relation line everywhere. These are open and generation conditions on the finite incidence, not consequences of its low-order equations. Both node branches and their gluing modulus rho must be kept. Assuming a regular formal surface would fall into the already excluded scope of R-0018 and would remove the intended singular problem.

The fixed-carrier certificate for the selected rho=−1, b2=0, q³-coefficient=1 excludes only that particular member. The whole endpoint-four family, the distinct tau=z³(1+z) endpoint chart, and nonzero-endpoint orbit collisions remain open. A completed unit ideal or exact obstruction for one retained open would close that chart alone.

## Characteristic range of this conditional lane

The retained lane, its six-row reduction and spectral gluing inputs are characteristic-zero statements. Some proof components are algebraic in wider ranges, but they do not transfer that full hypothesis package. The regular-sequence formula `length A/(p,t^10)=10 length A/(p,t)` and the injectivity of multiplication by nonzero f are characteristic independent when their stated rings, parameters and nonzero conditions exist. The displayed balanced coordinates and source matrices use denominators, notably2; reduction modulo a prime also requires the asserted ranks and kernel to survive. The free cube-orbit treatment uses a separable cubic ruling action and primitive cube roots, so its stated chart is not transported to characteristic3.

The nonzero rational seed pairing −384 is an obstruction over Q; it gives no such contradiction after reduction at primes dividing that value, and any other-prime application must still verify the actual source and inherited hypotheses. The global Milnor/Hodge surface bound is separately characteristic zero. No positive-characteristic exclusion follows by reducing that numerical argument or the degree52 equation. This is compatible with the [actual quartic-carrier construction in every positive characteristic](../supplements/POSITIVE_CHARACTERISTIC_CONSTRUCTIONS.md#every-positive-characteristic-quartic-carrier) for the fixed embedding.
